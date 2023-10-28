import { TestBed } from '@angular/core/testing';

import { CloudburstService } from './cloudburst.service';

describe('CloudburstService', () => {
  let service: CloudburstService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CloudburstService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
