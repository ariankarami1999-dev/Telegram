<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/r3LpllfWVpwHykhgQ7_c-vmXeO-NEVKYHUcQb3Z4cxQ6BKZkxd6p8nqQjA5EuQZx-bQXmwq6cEyjW8J91TE8L3SE69QvUwofW4-qwymJWE4_DRQvTGyDSEcvXsgJs_WU9p5qlzxpaa-tbWWAJev-NJEmA9hMJ9YKB4qg9XtMV627tu4wNao6mR_RLxfddtopoIIa-m-516oZ2R5Xx0p99fPmqjx2Lf5khQfH4wFQgs8busQJPjsbOani6rA5y1_JwlwLy6WfQtduvZ4N3rPiYNHggnHaH9gnjm6uZNs-WpF5j9kuwLWZdp-At0Q8rmLFILTW0hZyWU9GBgI_A6RVIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 14:21:26</div>
<hr>

<div class="tg-post" id="msg-5673">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTiHHa-YXTxQSSorFKHxNGavcGKzlqJfvcr5zRlQz5KMYU9NsAC1rRDHqhx3lmpa67xR_uRLyFMp9vy8FoMXM38-KdBguvomctElUwmqtsGuXs435GJvlfHyqaaJxuhxlYbGTWwk_xNeu0erW9TtNAXrAYdeN1wE0Q4XsPMEploQIiJI7lZDAa4PysDUGBpSpi68uhuSGnz-ICmx5BdMIaoa-fd1dZcdy9uwe0ssTB9LrsmEg7pxV67v9GA3c6ovWLWqETqYdlqXelblB7uZUj4e1mWW6pByHn1giDEn-dcu_2oRbjaQ0VKa68npnrgk_f5mHq2MHY_awa64no48Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی میگن همونطور که آمریکا به اسرائیل سالانه کمک میکنه،
ما هم به حزب‌الله کمک میکنیم.
امریکا سالانه ۳.۷ میلیارد دلار به اسرائیل کمک میکنه. این مبلغ میشه ۱.۴ درصد از بودجه ایالت نیویورک!!
بودجه ایالت نیویورک ۲۵۴ میلیارد دلاره!
میزان کمک آمریکا به اسرائیل میشه اندازه
۱.۱ درصد بودجه کالیفرنیا!
ولی حجم کمک جمهوری اسلامی به حزب الله میشه ۷ برابر بودجه استان خوزستان!
۱۲ برابر بودجه آذربایجان شرقی!</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5671">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2VchZg_KIe1nUsEPl5XuMt5ion6kWkkZ6STBX2cTHaRUPPQA2m7ZWHdrg40e-uuFSiUdCiFNKQbxxlXp6SHOURkCEHlS9HSCeCzA_1wtTfrcsAYcZ7b8PZbGNYfA09NMnsZrL838Yi65hVzvTzLK0xSaovujQD48G2LDtEPRB81eMmHW1nz1DAgofZZPbwps6XFWCC2q9d2Sub1tnnP2SHKUkg1ojn8ZKfO2ivTiYZnz6W7k5sfJCXtXXNU4raoOINQeRrOzvjaQU3mqu0LIN6Omtyb9MYjh6sZFM2DCaaR20tspfroRyQsOHAjvGkyWALy1JU1eU3OX22jobNVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،
در حالی که
بودجه استان خوزستان
امسال  ۱۴۲ میلیون دلار
بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار
و بودجه آذربایجان شرقی
۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5670">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2XT7SAcOvHN2TvfAOhQ7qlCmXZzgjSL-gz66ArLCsA4wu0PB9tDX0NlocguSyc-qr35uAflE4-NFZkbIoyJoGYc7PO0OrWbHrIgoMeQKPL1wUU5P2oT3nzUfweFrpmXFXqv2hNX8KsWMNqIK9-nxV5gK40VNxws7U53ILclFUGqW50RFdRIWFisjMmT8fGDpLXnvLkWRaS_BvfquHdmjPzdAr06Xx6Fi_DOwdavAijfeFoXaelp1reHD6x9TZUSQZsrQq93WT_AOk3cuz36zIQevya4mms2DFvqPSzWHvEJJxLqH615TTbhqSRZ63Ta5xRoxvIF3mRNPLTZemU2ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - جاده منتهی به فرودگاه بیروت و تشکر از جمهوری اسلامی برای آتش‌بس در لبنان.
دولت لبنان و اسرائیل درست ۳ هفته پیش
یعنی در ۴ ژوئن به یک آتش بس رسیدند،
سپاه و حزب‌الله سریعا بیانیه دادند و مخالفت کردن! چون نمیخواستند دستاورد
دولت لبنان به حساب بیاد.
در این ۳ هفته ۵۴۱ لبنانی دیگر کشته شدند
و بالاخره پذیرفتند!
حزب الله پول و سلاحش رو از جمهوری اسلامی میگیره، نه از دولت لبنان، برای همین این دستاورد هم باید میرفت برای صاحب کارش!
به قیمت کشته شدن ۵۴۱ نفر بیشتر!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5669">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/228de5708d.mp4?token=UlaYoaIzlRzrTQDUpFS7NKJSIQJtKvdKPxZSCBj5eO_Ie994k2Qkd-JWf_6hkft_w45F5yekGWR0zap7XXVkIIe6k1Q9TQK7gQmM4vSPojQDlT00ZlDSj5yEDrgoW8HNe-yBfCxZcX79S_wk7XKpgoEUWmw7Ck1R2fL1PtWIaG89231GQ3QD7UkaLoy0s4Ww_YU8OOydvjLMDoQImxOo00Zx5rKPWiFTxEKLGTfh4kyF_NzSrmU8h7FOvSfcKNKQoKeQCpKz5CbZ3wF031zn_MGaCjejlULPNYAI5v3PQrWZ9bmV6xgrsd_wVA0PXG5eGnWTx7C6REm_bBnzp_qH8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/228de5708d.mp4?token=UlaYoaIzlRzrTQDUpFS7NKJSIQJtKvdKPxZSCBj5eO_Ie994k2Qkd-JWf_6hkft_w45F5yekGWR0zap7XXVkIIe6k1Q9TQK7gQmM4vSPojQDlT00ZlDSj5yEDrgoW8HNe-yBfCxZcX79S_wk7XKpgoEUWmw7Ck1R2fL1PtWIaG89231GQ3QD7UkaLoy0s4Ww_YU8OOydvjLMDoQImxOo00Zx5rKPWiFTxEKLGTfh4kyF_NzSrmU8h7FOvSfcKNKQoKeQCpKz5CbZ3wF031zn_MGaCjejlULPNYAI5v3PQrWZ9bmV6xgrsd_wVA0PXG5eGnWTx7C6REm_bBnzp_qH8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در مظلومیت شیعه …</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5668">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Q9REQKwkxoKTOhgRO-L3kR5L3fwkkACyZw77ZkYGccXTsYK1QS-bHFcOx99K2xK5xOxtuu2EtBewdExNcASD4xlmgxwMKRXvprmZ0HvJZ1pmAxIKVbs3KCQBqb6M6M0Mr-YP58NFVSYXrTTseGE6OAuMkv3Ym9QX5fDTRqfQkdmxQIu-CJsuFUR-leO-iwtsWwmJIBw1o1csaKNEX2gGtESsUBUWL5XigkobinaKI1CMMk63sAOAwxa1NaMkoIk8Fm4qJkkRZ4aUyB-fQnTYN1peJ_ah_riiiETOTQJlnxdPjbWgJIpFf-eprh8-FQB05sbh62F1mOdLLXtwMF4k6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd9d936798.mp4?token=Q9REQKwkxoKTOhgRO-L3kR5L3fwkkACyZw77ZkYGccXTsYK1QS-bHFcOx99K2xK5xOxtuu2EtBewdExNcASD4xlmgxwMKRXvprmZ0HvJZ1pmAxIKVbs3KCQBqb6M6M0Mr-YP58NFVSYXrTTseGE6OAuMkv3Ym9QX5fDTRqfQkdmxQIu-CJsuFUR-leO-iwtsWwmJIBw1o1csaKNEX2gGtESsUBUWL5XigkobinaKI1CMMk63sAOAwxa1NaMkoIk8Fm4qJkkRZ4aUyB-fQnTYN1peJ_ah_riiiETOTQJlnxdPjbWgJIpFf-eprh8-FQB05sbh62F1mOdLLXtwMF4k6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاخی … رهبرشون تنها و مظلومه!
یه چیزی درخواست داده که هیچ کدوم از سران ج‌ا، جز جلیلی! بهش رای نداده!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5667">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=gK0XgcpVHDD3uMtwK03hcDWwAht29uOU8qqwNtj-9J7euZZtFP3mJgLZVCoKZAegDn9PnVa5iwMjxmVihxQ1kCgbrADL3s53c2kVKxQLjs71nlI0MRUEMjowKf4IhPvReb-Cd0N-IMtEIm2B6uxNhzHLmw3S0jrYn4qqbve_lpHIH8tM3NnmJyv-vu9oit3VpxtftxH8BtL5Tgi-6b2Rz7fq7dGkzJVieM7GWRQtD5RxVyWs5JfWFBrVOl9vuKmXjeKIjef2JMZSLYxOdqK0dkpL9d5JRiKPJA9ezGDzmV6cBLIS4yDckthnHpPsv7Z_w6N8zSs4fzLZeq2GqehzWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3016eb3.mp4?token=gK0XgcpVHDD3uMtwK03hcDWwAht29uOU8qqwNtj-9J7euZZtFP3mJgLZVCoKZAegDn9PnVa5iwMjxmVihxQ1kCgbrADL3s53c2kVKxQLjs71nlI0MRUEMjowKf4IhPvReb-Cd0N-IMtEIm2B6uxNhzHLmw3S0jrYn4qqbve_lpHIH8tM3NnmJyv-vu9oit3VpxtftxH8BtL5Tgi-6b2Rz7fq7dGkzJVieM7GWRQtD5RxVyWs5JfWFBrVOl9vuKmXjeKIjef2JMZSLYxOdqK0dkpL9d5JRiKPJA9ezGDzmV6cBLIS4yDckthnHpPsv7Z_w6N8zSs4fzLZeq2GqehzWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم آتش‌بس دیروز
شب گذشته ارتش اسرائیل توانست
کوه «علی‌ طاهر» در اطراف  «نبطیه»
را تحت تسلط خود در بیاورد.
در زیر این کوه جمهوری اسلامی شبکه‌ای گسترده از تونل‌ها ایجاد کرده بود، هم برای انبار کردن موشک و اسلحه، هم برای حمله
به شمال اسرائیل و هم اینکه یک مقر فرماندهی و پناهگاه امن برای نیروهای تروریست‌های حزب‌الله بود.
ارتش اسرائیل تخمین میزند که هم اینک در این تونل‌ها، ده‌ها، با شاید صدها نیروی حزب‌الله گیر افتاده باشند.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5664">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=DsoV8DIdYQollLQVePZK-wx0UT6OKpgl73rgpDM3NauQSNn1_1BFQwym1qrPK0kUnhkQIfOhTTMMjOENPDHaUf7KdPsfEwtFc2LTd6mDiYo-60I-umeM5cYG2e-GUbH6I0fvDkAbIf6QdqNDMs5v1ccC9UUBlDLnk5YrB3ILGfcdIG7PjUKIeQTl8Bcw8jaIEQSN4ICm13mG6GidLjnivwaxY_8c-6OOaE5FSnvzEJm2Y32_TeSfp5Y8wN_wb01vP5_F_Jd_MzKEcdcFMRdgTraYDDXinKP7shexJbXUkQgLS12xAzy45RPgqq01HQJmFOG19oUu8xn4-1q5BIJ5exBUm_FkSsrij-rCnj5UQNhBpSqY2Xg53Uh9FyxwIkGiJS7PD8jVPIayi1iF2L4cDMP54-RYyVOrrcmvw3UDK4WIVEnfURa_-G0wGWc_anW7vL7R8FzckGDdgiBHHZsBHUdPt5boMJjE6q2OV03Y6yFbfFjEL6GLCm-TiCKKl-729fXVnbJOa4rA3-wS_pOONQtmUepZuW-CDZ6lETsv7oKqpU7v11NoziCdLh3BnxweNNguOMooO53QxsNLgu9ftzd8l8lm-c009C0jAvWZnT3fJCycGxf39HPHT3SzIInRA0ffZ7wlpwW4qGytWFRAwIxG6_0_4IZPbD_GYUtvzCU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd300c19c9.mp4?token=DsoV8DIdYQollLQVePZK-wx0UT6OKpgl73rgpDM3NauQSNn1_1BFQwym1qrPK0kUnhkQIfOhTTMMjOENPDHaUf7KdPsfEwtFc2LTd6mDiYo-60I-umeM5cYG2e-GUbH6I0fvDkAbIf6QdqNDMs5v1ccC9UUBlDLnk5YrB3ILGfcdIG7PjUKIeQTl8Bcw8jaIEQSN4ICm13mG6GidLjnivwaxY_8c-6OOaE5FSnvzEJm2Y32_TeSfp5Y8wN_wb01vP5_F_Jd_MzKEcdcFMRdgTraYDDXinKP7shexJbXUkQgLS12xAzy45RPgqq01HQJmFOG19oUu8xn4-1q5BIJ5exBUm_FkSsrij-rCnj5UQNhBpSqY2Xg53Uh9FyxwIkGiJS7PD8jVPIayi1iF2L4cDMP54-RYyVOrrcmvw3UDK4WIVEnfURa_-G0wGWc_anW7vL7R8FzckGDdgiBHHZsBHUdPt5boMJjE6q2OV03Y6yFbfFjEL6GLCm-TiCKKl-729fXVnbJOa4rA3-wS_pOONQtmUepZuW-CDZ6lETsv7oKqpU7v11NoziCdLh3BnxweNNguOMooO53QxsNLgu9ftzd8l8lm-c009C0jAvWZnT3fJCycGxf39HPHT3SzIInRA0ffZ7wlpwW4qGytWFRAwIxG6_0_4IZPbD_GYUtvzCU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دوربین جنایتکاران جمهوری اسلامی
قتل‌عام مردم ایران در شب‌های خونین ۱۸-۱۹ دیماه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5663">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=ZTcmzVI6U-QqcajRLrY4E3uAR5azFaQF41-wq3cMmyzGmhODTqzJSZzQLi81kkaolZTJby1904aAPayg8exkecAglepDArdow6QdmEJpOYGG81IYKKIKc7knPd0ij_WsqSBm3QhpcP2HsVAea0-sOmLmmUBbc1CaaBNclPwFPIe6Lker-kSvpPVYmLiXZEFuwAwhQSZGqfqStbJDP7xBGE5cOO0tJv56pQrBl49Z5BnQMaNcSmo8XLrv4R2t0uzeBmM-amh8g4RvpR6w4Zw7b798VzNMWh0ayO_7bsoaw9BFWJw3628pmdmbkEnIl2CiTBQCTeA-wMTq9vsT8JSzSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/845f6aff27.mp4?token=ZTcmzVI6U-QqcajRLrY4E3uAR5azFaQF41-wq3cMmyzGmhODTqzJSZzQLi81kkaolZTJby1904aAPayg8exkecAglepDArdow6QdmEJpOYGG81IYKKIKc7knPd0ij_WsqSBm3QhpcP2HsVAea0-sOmLmmUBbc1CaaBNclPwFPIe6Lker-kSvpPVYmLiXZEFuwAwhQSZGqfqStbJDP7xBGE5cOO0tJv56pQrBl49Z5BnQMaNcSmo8XLrv4R2t0uzeBmM-amh8g4RvpR6w4Zw7b798VzNMWh0ayO_7bsoaw9BFWJw3628pmdmbkEnIl2CiTBQCTeA-wMTq9vsT8JSzSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمزه صفوی
فرزند مشاور ارشد خامنه‌ای :
در ۴۰ سال گذشته جمهوری اسلامی همواره سودای ساخت بمب هسته‌ای رو داشته و تمام تلاشش رو کرده. اما برنامه‌هاش لو رفتن!
جمهوری اسلامی پنهانی دو سایت «فردو» و «نطنز» رو پنهانی داشت جلو می‌برد که «لو» رفتن!</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5661">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=MNSDA3eSeOIwC2pFw4c-nSTwXFs2ebR4jRFB0R2Cu68zlLbVUWpPKHIYlMhStEYFoPNIrVJiXV62h9zKY9h8uLidyKQwnEaNbHMOpL5BwnwPCkzRK6GBRYi9A1EtqInSzPjWMOZQC531gz4gqY3IQBgPOOrbTFCsInaDz1K2mJheFnK1jifCirxqUIdV2qytvKnLVs_UVC5G2PgPSUU2n9Mn3xxjvCdAIve_OobSI3zF13X4SFZy3JaOGENsfqww_ZdaMaY2yfzVugTynQCi1BsjLWREBZKZZzQ2zr1XsyV5RsjGys4iLDG9zM-XGxI1-CCxxLQjM4mF7VjkOQWmWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28d8f2fab.mp4?token=MNSDA3eSeOIwC2pFw4c-nSTwXFs2ebR4jRFB0R2Cu68zlLbVUWpPKHIYlMhStEYFoPNIrVJiXV62h9zKY9h8uLidyKQwnEaNbHMOpL5BwnwPCkzRK6GBRYi9A1EtqInSzPjWMOZQC531gz4gqY3IQBgPOOrbTFCsInaDz1K2mJheFnK1jifCirxqUIdV2qytvKnLVs_UVC5G2PgPSUU2n9Mn3xxjvCdAIve_OobSI3zF13X4SFZy3JaOGENsfqww_ZdaMaY2yfzVugTynQCi1BsjLWREBZKZZzQ2zr1XsyV5RsjGys4iLDG9zM-XGxI1-CCxxLQjM4mF7VjkOQWmWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsdBrk39VUkaHgUUDD1WoOmMQmDMorD3dhmQvAO7we9CoD6EHJ8_PsYOX_BGSktm-NENl7KEAXE616KH2zV5sCqbG36qPbbQ-xmkgpvTf99pllSTU9IPdA0_IMSxk1qG6Xqlt8CW38BZ02J-SBY4PnWVk0fv-Bj3mVVWrVf0bhCro15YMeXEGtQK0iG-HN8ww2hE3GAqONoMk5CqEU8JXbhAMOeFuD6BWgw45hNNWLTgBu2GNYpDPj4KIK9kXC2PN5wdOLzXxxVSGGySY0vz7gyocrGk-pVFptS6iZecRscGil-JSr1MYurFryI-32rCSFuTSgayzzviY_LJBOsNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5659">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ssDqKg-utSYYsZs8qHsH4qAP6dUsleRZKn_tMsTRTz0IPFSmg9ZX3rUNb96QYmst93EKIVtc129rOyS8h4hRf1kf6YDnQADwiiC1l7v8WQMjCEJt3CZkybsZUq0qqlEEb1soKXMf1DIB0Dk8HUOdvuHC7Rpw7aAg-0HRXIdF2A9sLokj29723u_Q3XETKDVoWKYQR0nQp0KPMk0izyG23sOVGe3L85RJehsOHQFYjhoGy-AhywVeNkF3nK4vjgtn-Nyuje5wmSQpPNMFiKzfgXkkyG9wKnwUpHOf5rgqlvMqL2rLpZ3Y9Y37JE6VTvgZN88aK80A61Ws-PHM519hgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adbaa46b5.mp4?token=ssDqKg-utSYYsZs8qHsH4qAP6dUsleRZKn_tMsTRTz0IPFSmg9ZX3rUNb96QYmst93EKIVtc129rOyS8h4hRf1kf6YDnQADwiiC1l7v8WQMjCEJt3CZkybsZUq0qqlEEb1soKXMf1DIB0Dk8HUOdvuHC7Rpw7aAg-0HRXIdF2A9sLokj29723u_Q3XETKDVoWKYQR0nQp0KPMk0izyG23sOVGe3L85RJehsOHQFYjhoGy-AhywVeNkF3nK4vjgtn-Nyuje5wmSQpPNMFiKzfgXkkyG9wKnwUpHOf5rgqlvMqL2rLpZ3Y9Y37JE6VTvgZN88aK80A61Ws-PHM519hgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غزه</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhH5Q_Yl0mlHfnJP_mSCe_yUdtDdPCNVt14k5vHA6bxiDZk1hFRH_l5RX4Yn3TVVLwp0556ERIZHUEL-PbKdP-TiLnj0y18JM-1W6QIbGhAodZmbZ7fNohqfiukceq11DjLSy-DA0sC7_dkMfB_vRU9QL266D0IJ4Wn9vI4p-3mPs8RrUtgWziJSN5BwSlcpZrfyRXrturavu4j2CglYgvbhlcrz9tLDEgXqKivTuhS6LIf7MB62e8tLaujhQmEcAacwAaAZ9s_ZpeloTxoGz7qtOqF2HLFB7BGdNteP4ATjGB-EAGTRNDSzEh7ZuV6_S-MNRhhnxnIRDG4QkqzRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyPY5xgDAbZiaIUqY_p8zj4eNco4l0Ld9WKsogZz2ntVSbwyMFXdpwNXK_sgp_F473RNbyC9yrGj6IcN3UEoraSIf0SrE7suFHk6Tg6SbU3OAbmF0mfzVKqSSVIzN00EUjgOCZnt1h2uDbdiOnQaXWBfWqSn6h2t0F0HS7dYTQ1denw97MM-kJ7aHcHeuOcEmoOhzO22zmZrmFy05vMuEXfb0BePcGJoJmxCkjWa85hocWw0QwJq1uhWJK3cWnSPuRf_5mYjNRuMrBE7QOOFTCgXH_6cJoRcT8kZpKkgNwgkjI8DbE4NSYCz_ZpFRD-e83BSaoW5_QzsJK7g1tviFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=BTTTrHCGsbrwiq29YtCyvwkXJBnLo9W6u6-MuUNT2EPLU3Pvc3ucUb02uO8kSHc6ttcLwCxW-M5WV2eOLhGAmPaU7sEAt5814Kh05ppm8TtQFb9LFLP9572DN8GQDNw24se1NUN821qWcGJfwRVknE1sSNxyKSbVrk9NVujN7zEfemIulsA96VNYUckrtIls2buUpqiqZnbeZNbpqBLYrHSMVzIg2Nu7-6zoZzdhxqr_9U7ksjQ2r-nH63yVq06q8SeAErHJT1UrvrfY-058qrlYzhTOPhrzOgVoevQVTyn2YSPCeeqHel5lbtqlJ86HJRs5vlXWzJ1HZ1_70S04Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5653">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=HTz1JHvvlT4B7jwsmd2izHA9tMjOq4UuxBxEgYIqYb1pJd9ddwa1egA0jHqQSTdZj362sNxbmVrVnBZgiGMJLYPpS7eOYsNrwNtFLzMOWqb5FMjbv3lX0dRDAUoOwkuNFF4MT0X79FtvjL1oOXpOJlTv9aC2TGMpWWsSx6J1Ox9bsLvckspkkNnQz1lQtxmC5uk8XGWwrheZG9NeYqgJAjO5y8C2zVr1bJlgDVcIjque-OnCgNfvHb0FPFZaR9rTB-A9dxTy-WIxL82FFb7dlaU0bFnWjrQrosXxQviU8mrEAN_5diZy7VPWhDXGtt6_cDkMAwPyocKu_F9g-YesJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5130bbfc36.mp4?token=HTz1JHvvlT4B7jwsmd2izHA9tMjOq4UuxBxEgYIqYb1pJd9ddwa1egA0jHqQSTdZj362sNxbmVrVnBZgiGMJLYPpS7eOYsNrwNtFLzMOWqb5FMjbv3lX0dRDAUoOwkuNFF4MT0X79FtvjL1oOXpOJlTv9aC2TGMpWWsSx6J1Ox9bsLvckspkkNnQz1lQtxmC5uk8XGWwrheZG9NeYqgJAjO5y8C2zVr1bJlgDVcIjque-OnCgNfvHb0FPFZaR9rTB-A9dxTy-WIxL82FFb7dlaU0bFnWjrQrosXxQviU8mrEAN_5diZy7VPWhDXGtt6_cDkMAwPyocKu_F9g-YesJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجتبی، فرمانده کل قوا ۱۲۰ روزه قایم شده :))
خودش هم در جنگ ۱۲ روزه رفته بود «کمین» کرده بود برای دشمن!
که در جنگ ۴۰ روزه غافلگیرش کردن!
«ما اینجوری نیستیم!
خود ما پیشاپیش لباس رزم می‌پوشیم»!
مجتبی کجاست؟  :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5652">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=NdzeWBQJf0QVec9v_R_5jTa3tm6ZtNtGilzEW2ThZ2RsY8lif6cyLyVTx2NFtl5-zXjk-Off592LA9cKiyT4768Y7fVOIfLrTx5QdeqKbxjq-lXOfMa6Um_y8NNtv0wm0fk6HEwo0SIJV5tH859iuG_vMyaA20akf2UIMfYVFWnJl7yY6XLm1VAn1ecM8ixPw1M6kC82-DFmmAXFPc8GOdIQhic0btmJ2R7r8W3C9FYYaFgv9JpEcUZxbU7LJKW-hAszGXFGila2c01y_ZFn_bzhJqIYfXQ8Stcm51Zw6ao03cR8z7LytD33ohIXRWFjxWiVW3IvZms-17igN6wmGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a19f9c1ecb.mp4?token=NdzeWBQJf0QVec9v_R_5jTa3tm6ZtNtGilzEW2ThZ2RsY8lif6cyLyVTx2NFtl5-zXjk-Off592LA9cKiyT4768Y7fVOIfLrTx5QdeqKbxjq-lXOfMa6Um_y8NNtv0wm0fk6HEwo0SIJV5tH859iuG_vMyaA20akf2UIMfYVFWnJl7yY6XLm1VAn1ecM8ixPw1M6kC82-DFmmAXFPc8GOdIQhic0btmJ2R7r8W3C9FYYaFgv9JpEcUZxbU7LJKW-hAszGXFGila2c01y_ZFn_bzhJqIYfXQ8Stcm51Zw6ao03cR8z7LytD33ohIXRWFjxWiVW3IvZms-17igN6wmGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اورانگوتان رو!
هر مسجد یک شعبه حزب جمهوری اسلامی
قاتلان فرزندان ایران بین همین‌ها هستن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBqt_H7gHVLmfgWo4W6RFhteEMCHEA1Vud2G1_0vwwABDVswPr1J4ir20FMuJzKMrzYIi0aUCMTzdp6yo1LUx6qAkieem_GQ06w2w5xeLPJGSxVNO9gtEvEGgpSLo4pdJBrdAWyN0lNYpI28U9mZQSh4BsY5JfHKeIk7gz7hTXIG6kF6ddIo1ntuXU7masMk04Ze85pzLu9a0xUVeWib-ow7qNxxyYVDFYWc4qfc55lTp1QTdwefFq3bQavrIGR8ui_0wygyEQFLw9FaFa1hvsqhXU5LAInMyUbk4SPPSj00aW8yucguVl3wi85xQzc4DpNLIpEaKKiGob2EtZTwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5650">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=bmgmybFga61-5WZxOkgCIz-KtydbGG9Ewug1mFQkKIaXGhcQgC_HpOXjzaZf8s7rlVFlunzfduV4boxGMQm1uISl1d_fzgEmFhxth4f3mBhq7DebJTkK2fq9wP8xZstVFY3SupEFhT4srZ7nfOjwqtsrmtq5n6yBXze2kfZf9fSkYW9rRbom2aS2UG_iUGgg3teRC_kL1LSkOwrmxK30U8CDcpnGEn5mUq98v58l2lPjrbnZujmhWSAEOQKDZ1fIbovE-jwA-M2Ghp5McFwgKyv9zNvhTyW3PRaU0cjF71G7BPoE4I3Dgy5c2AfMEga0WoV9oB8pzRFdEgnmB8gZZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecdbcd4679.mp4?token=bmgmybFga61-5WZxOkgCIz-KtydbGG9Ewug1mFQkKIaXGhcQgC_HpOXjzaZf8s7rlVFlunzfduV4boxGMQm1uISl1d_fzgEmFhxth4f3mBhq7DebJTkK2fq9wP8xZstVFY3SupEFhT4srZ7nfOjwqtsrmtq5n6yBXze2kfZf9fSkYW9rRbom2aS2UG_iUGgg3teRC_kL1LSkOwrmxK30U8CDcpnGEn5mUq98v58l2lPjrbnZujmhWSAEOQKDZ1fIbovE-jwA-M2Ghp5McFwgKyv9zNvhTyW3PRaU0cjF71G7BPoE4I3Dgy5c2AfMEga0WoV9oB8pzRFdEgnmB8gZZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5649">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=EeyC8rJcQqnIPKSCEs5KZTj1xA4dlVp84w1lp9oTyHYNRmHhh3Ls_m2-Soharu3DwABwfT6n8uE3L05vztee7ogwma3RA9VXnOc2gYFXvhWhJvxCS7iYwSmjc8-sx9C2asBOBzb05rbxBJOCPamPh3-eoacdKPuOGemEkFlK_HaN4CQq7hqr214OCZYiZ8EwG5uE9VqIIggqZYwvRQgGHNrsF16zA7vuMYdSTEb8akwiW9ss_DKG_A-fkChCp1OiHCgBCFuadO8P477NHnXHiAmdqU5IENIKhlnyrl-X6SSTe2_8-WNUAXluc7ilDWK00wW5mjiEPwqdkp0yEUwLAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5aba790b1.mp4?token=EeyC8rJcQqnIPKSCEs5KZTj1xA4dlVp84w1lp9oTyHYNRmHhh3Ls_m2-Soharu3DwABwfT6n8uE3L05vztee7ogwma3RA9VXnOc2gYFXvhWhJvxCS7iYwSmjc8-sx9C2asBOBzb05rbxBJOCPamPh3-eoacdKPuOGemEkFlK_HaN4CQq7hqr214OCZYiZ8EwG5uE9VqIIggqZYwvRQgGHNrsF16zA7vuMYdSTEb8akwiW9ss_DKG_A-fkChCp1OiHCgBCFuadO8P477NHnXHiAmdqU5IENIKhlnyrl-X6SSTe2_8-WNUAXluc7ilDWK00wW5mjiEPwqdkp0yEUwLAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نمیخواید بخشی از مراسم تشیع جنازه خامنه‌ای رو در لبنان برگزار کنید؟</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5648">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=UEvnIGOsO-0ZkYjf71S_I1Q7GEQXGzfULwj2QHEE2elOBSlUBsRnn3sPQ_Y3rD9l3QXi8WU9bsUz270AxuUb-D2NZgf4JgpH_cvYRC4WA8C9i6FpTEE5lxVbhgPxNYKeuyydGgYXGEs4POWBgLv8DZ1IaH1nBe7k0i1GzK7yPClKO3TRJu2voggS77cFSBacIS2MCaJJpRTB6sHIbw52dVtyEKOuNUcojC-Aev4WKG96cfnq8wFwDDY3Dyr3Z1QInmII_EyuW7J0BRWu9A_StbVIO1G3_dynJ0HL_nDjPpigXSCsCJwcndlhiVN9haYbiuKAMV4tD403jNYTIycwig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eec8cc86d.mp4?token=UEvnIGOsO-0ZkYjf71S_I1Q7GEQXGzfULwj2QHEE2elOBSlUBsRnn3sPQ_Y3rD9l3QXi8WU9bsUz270AxuUb-D2NZgf4JgpH_cvYRC4WA8C9i6FpTEE5lxVbhgPxNYKeuyydGgYXGEs4POWBgLv8DZ1IaH1nBe7k0i1GzK7yPClKO3TRJu2voggS77cFSBacIS2MCaJJpRTB6sHIbw52dVtyEKOuNUcojC-Aev4WKG96cfnq8wFwDDY3Dyr3Z1QInmII_EyuW7J0BRWu9A_StbVIO1G3_dynJ0HL_nDjPpigXSCsCJwcndlhiVN9haYbiuKAMV4tD403jNYTIycwig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان - حومه نبطیه
از مراکز اصلی شیعه‌نشین در جنوب لبنان
و از مقرهای گروه تروریستی حزب‌الله</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5646">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naLycJRnZgI8nl2sbwfdEtv0iCKM9eyHG0h5r5cZvKjJKXHCy3GLYD-qHli6H3BbUZZaPyQE5m4Vkvg4WAaPHE80up-1Z3pq6RO0pljb8IMOvip5gPD-R4LwWQHE6iT6xFZP2gncPkysKW6NlsIXnhUm61PYB-yLzOrG4YE86cO51VwnRwNbmU0iDwO_jLgI5PooYY9t0TBZaa5GNU9WMbd7fLQtEYDk675yBtpkXQ5EtI3M2GIFTmjHUaogpDqoxGSwNpz97HHScOakKaxk-8OjSbgHT1Do3Rz-pimjiFCwKKfNfd3iqlOTgvbNGgwjC7RTO0GfmLeVfksH7xFiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21669172c8.mp4?token=W6NIUtmo1ksLBybDdZ5epDwc1PsTZaAhpdOfS9CR9Kzy8ZgHCk1uHZdpT-O2kOij0z1G_QX3HymCtp_d0bbvOL226FiAk903jgxefnLHAf-4wTHwN_9RJXFrcF7-RjH_EV10tXSu2XvbYyV3ueIQCN4Qb5eHrEk7cCvdV4ASkAYDWrQoEdNttDAxTEMVBH2lwLMK1rrOv_kXfC1fselyTyCtcKp_oquX4wJYbqX_VDvoTPYkmMffs86mC_yA7nAV9oenawbacOA3S0xFel52PsaNl6_W-r2b30pC274A-68oORwxDU_tQ_MggD8W4rgLtWn2KfV6lcq-XiMe_atqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21669172c8.mp4?token=W6NIUtmo1ksLBybDdZ5epDwc1PsTZaAhpdOfS9CR9Kzy8ZgHCk1uHZdpT-O2kOij0z1G_QX3HymCtp_d0bbvOL226FiAk903jgxefnLHAf-4wTHwN_9RJXFrcF7-RjH_EV10tXSu2XvbYyV3ueIQCN4Qb5eHrEk7cCvdV4ASkAYDWrQoEdNttDAxTEMVBH2lwLMK1rrOv_kXfC1fselyTyCtcKp_oquX4wJYbqX_VDvoTPYkmMffs86mC_yA7nAV9oenawbacOA3S0xFel52PsaNl6_W-r2b30pC274A-68oORwxDU_tQ_MggD8W4rgLtWn2KfV6lcq-XiMe_atqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر امروز شبکه المیادین
(شبکه خبری عربی زبان شیعیان لبنان
که با پول مردم ایران کار میکنه)
در حالی که حدود ۱۲۰ روزه «انتقام گیرندگان خون خامنه‌ای» در جنوب لبنان
زیر گلوله و آتش هستن،
تامین کنندگان پول و سلاح‌شون در ایران
مشغول صیغه و همسریابی و غذا و….
سوار جیپ صورتی شدن و….. بودن.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdtrRfQnzrSLnVowz0S8wUcFVpysO-bLH1I67Yi6Fqf6PRNtXv3k5N7b6PFK_6I89A3P11S-y7dUGU6BDZMV1B6u6nz7O1vPcoBewtZu3VO9A9XwsYp6NxyY68Q_OnZo1qVw0Te9IoK2nJhTjj4JN-Mgnejy1KYD1I07MawlP7yfGLvvfV79F7a8oamW_6GaQ__OD0tSvM2DSaZWQHsdekGpoF7NlNbdgqzqE9Ivw8aMmLby8W3s6ijXNWCWfd93rqtGc9Qsi_TlKyiOtDCBps-boA-fu9KpAjShUvNbos-LKuJlDIesz7xMdXISUfDJ5x_J8FaIXiw-7tQLC9485w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=ieEIACcZ9UFAIBSJItEL_0ujeCqbKTV8ReaZ19o-_2I0x0U8WuGqZC9Wb7TgpkVtJR-bx1EbCs-mx9x8Vow00O3lVdEOO92hSd6gTuvIeRxx_RaqgunU9XCkHUmLoRBzy_MOqIgV8uarzz5V0t4WtLbwVSN59Tq7JOQiiDPuw3KO6gLODcdRvskwkARMyyWDPC8cQC46XDJX_eA55-RAMGaHfcTiaxeTZjSRoKanRg5kmHFxCISrKPQTA9afX1yufJ7xi6fX9gggaSGg51dB3SswAbGBczOOCF581i41NQzwa-Pt7g3A5-DCvLwRbse9goH_6Jp90i7FmyFgnXWHnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=ieEIACcZ9UFAIBSJItEL_0ujeCqbKTV8ReaZ19o-_2I0x0U8WuGqZC9Wb7TgpkVtJR-bx1EbCs-mx9x8Vow00O3lVdEOO92hSd6gTuvIeRxx_RaqgunU9XCkHUmLoRBzy_MOqIgV8uarzz5V0t4WtLbwVSN59Tq7JOQiiDPuw3KO6gLODcdRvskwkARMyyWDPC8cQC46XDJX_eA55-RAMGaHfcTiaxeTZjSRoKanRg5kmHFxCISrKPQTA9afX1yufJ7xi6fX9gggaSGg51dB3SswAbGBczOOCF581i41NQzwa-Pt7g3A5-DCvLwRbse9goH_6Jp90i7FmyFgnXWHnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5643">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3r7wNeUVh9FCfA6SqBnJoE7K8OPQkpxz_G9lU-5Uvwml-Z1V28J9jE6kXsmZEkrwnp2UaNIruzKywBOpLat_wro08nPmcBI8u2ySqnC3VRbhgWXceAANP2M4dmidADIv54stpP7g0U1-mZf07FnGpuPfqCAFmS_U7hgCY4_JzEUUUvvZO7xyHyH9tZkRNtpQe__Z2M6PNNFYMtMfJQFWKCkbxETx9WsiRPwHEiloQNyEU9oQgRu5KkOdqvvcqrC1M_t_xv52uSEyy9bbfKjZqCGB6nih0pwGkH5wImE6tBSJjW_399uut-5u6hlSdA3z-VjdrX4QRw0buaX_RqkVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکومت یزید هیچ کدام از اسرای کربلا را محاکمه و اعدام نکرد!
حتی به بازماندگان کمک مالی هم کرد.
جمهوری اسلامی هزاران نفر جوان معترض رو قتل عام کرد و بعد هر روز دست
به اعدام هم میزنه.
۸۰٪ از آمار اعدام جهان به دست جمهوری اسلامیه و قربانیانش مردم ایران هستن.
کربلا به دست مسلمانان افراطی رخ داد، که برای ثواب بردن و مقابله با فتنه، در این جنگ شرکت کردند. ۹۰٪ شون هم هیچ پولی نگرفتند! انگیزه‌شون فقط ثواب بود! محرک اصلی اونها هم روحانیون مسلمان بود که سخنرانی کرده بودند براشون و توجیه‌شون کرده بودن و ریختن خون حسین رو حلال
اعلام کرده بودند و حتی ثواب برای مسلمانان.
اسرائیل هیچ زندانی فلسطینی رو اعدام نکرده تا کنون! هرگز!
هیچ حکومتی پلیدتر از جمهوری اسلامی و حامیانش نیست!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=XQ_9gHh6HF6KRT18Z_Mt5ZrGxSz8YD3meEn1RztsEQPKwPNyYBhm_aa4-ZLywQtD2QCadfpngluHLEAmpXngIZ5JKPcdAaewRW8WU6KO9tZOag9ehdMxcQvVCJiyeEE_XCwLPtpOpkIWIdEL-sf3uqbIe7y1naDEqtyJXgIwMO8DDZF465HY090v-IdUJcfRTrdYtxz11IZL3S3AEBVMutPojXOBipT1IiDjfIkudzGrsaS7-_J4GBVRE0LMNpd36_wDkOpKxvU9JfjHhO6FWBOAg0SH04yPqqPrmvlIreEiTUxFWdu1PDIV8RFKfXXyw25RtrwLaL7x9BmjQ-lLOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=XQ_9gHh6HF6KRT18Z_Mt5ZrGxSz8YD3meEn1RztsEQPKwPNyYBhm_aa4-ZLywQtD2QCadfpngluHLEAmpXngIZ5JKPcdAaewRW8WU6KO9tZOag9ehdMxcQvVCJiyeEE_XCwLPtpOpkIWIdEL-sf3uqbIe7y1naDEqtyJXgIwMO8DDZF465HY090v-IdUJcfRTrdYtxz11IZL3S3AEBVMutPojXOBipT1IiDjfIkudzGrsaS7-_J4GBVRE0LMNpd36_wDkOpKxvU9JfjHhO6FWBOAg0SH04yPqqPrmvlIreEiTUxFWdu1PDIV8RFKfXXyw25RtrwLaL7x9BmjQ-lLOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDKJttGj95ZzJcgbov5rJAqIXccoUOpJB9htxcGBuvkPEwEFB3Z65l9vvo3-MGungWnpaxsbnJ466uClk8KOKzqNylS7DhyKumHgzpMeWvVM1O0G7L7CpqGM1O-APaerbWpS67I0YACnERw3GQ_-TmovYFT7fbpOTXiSFL6pda72q7vwydKCrQBpqmL9z8gavCjW2QXLDa2QkdJOTPm5b10r4Tpozaqvk19Z5lqCREUSv1htqlgpAWgLqTeqqBoBDp3j2XkQdKOjitAx2n_ATlDZlgafVBQZUE0S_qm22wE4fhRogBhnqq6-QzhjtJzVlUxSJ-uyDjhXy7Zczg8wkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwSPxIyg9VT9k32nogCP4FQzLP-CZe9hCnCDWvbuvGI1Uhk25EbAWjUn59qXYG_dLR7TWxxntRHQ3QtHLazhcqOsCCiAx2HW_-zz0QD-xZ9MRed-m53O0YStniQUwYdAK6BsVmDL1hleKQJoaYvctSZa3W09cfVlToaVQLWFYbC_Vw0mzJnOY4OBoZrVlty1oV00TnmOs1mQvlm0NOqc_Cd2U9j1iPKfvut97YOG0nXKVT5S6WYJ-RcSwmvdXtlKgsiddCzAZNEEWhmYlPiTldoTfb9GV8YGNlMpz9WMnCdW4KX2n805ZXg9pbWNSwk2IgMM22Or1NoOAS0aQe-meA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=sJq-2XxJ68sR0LiysIZk9G4h_9E93unZ1k_V5dBSecD7g7kwIVA4VQXp3v6K91BzJYuH-Tz6veAofj7x9UDug72RwOibQ0ZePqVgdvBzYi6DZdVxk5Oik-syN10M7kziDTHEOdjfU1tW8rNE02I2CObmM9mJ2yo2RLTLd1TFDU1OtOp5y807Y2ArP37xVg6-67yHncUTeAyrp6b_4vc49aGTJNSb5XRrDRXr-z3tSJ_JYBGhOt_G8P_xXSRAFuycxtDvBFbiLUsv53-pQ2ynDWnSrBgyAYfAIOlCO69a0eIarrX7nfUfISvjncHfKxAICqmbsftwPP3CmrFrc8xPXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=sJq-2XxJ68sR0LiysIZk9G4h_9E93unZ1k_V5dBSecD7g7kwIVA4VQXp3v6K91BzJYuH-Tz6veAofj7x9UDug72RwOibQ0ZePqVgdvBzYi6DZdVxk5Oik-syN10M7kziDTHEOdjfU1tW8rNE02I2CObmM9mJ2yo2RLTLd1TFDU1OtOp5y807Y2ArP37xVg6-67yHncUTeAyrp6b_4vc49aGTJNSb5XRrDRXr-z3tSJ_JYBGhOt_G8P_xXSRAFuycxtDvBFbiLUsv53-pQ2ynDWnSrBgyAYfAIOlCO69a0eIarrX7nfUfISvjncHfKxAICqmbsftwPP3CmrFrc8xPXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PprvcDqgetFCXxIA5xYbbVKWf82YOekc5eIrxV-I2w5NLQkdsFT6kycjiwVnIKKz-RZHrfvVi9rLuDB0TM0TRQXRT_LLDKeK3cHRu_N4vxZy3v_0U9Pc5pYBWDhzpLrh_5fThixZY9XsMLz8w3iv6UD33A8xt0au77RGDcQ-shI8e9FFX0FjN5LhtpxOxdeKssf0SybTyVswuT11WRRvu3yOjLc9CmnuQVNAo4KIX5tFYI4FpVKH2fXzrGqqGM4ckduxRIH27OQk_E_anF9InJ8IBb0-Dyjuuc2b3EhvnUDlGfd3voMr_kVDe18AI_YQyguQOWs2maCLzVPCcLffIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JV_BfMoYQDt1i0ISzDxIpKclMTeaZJEhv5x6jLidGj24l0Hm_uEfhsRy2XB00fn6JYGbsgLI3naS_L2nothh7eFXWYYTtRC4Ziho7wTDkkk1L2KjAe6bqsTjzoUDTqgh68jDZFw_bMbu_TggeBccjtkJ3VmFNw4k9xrhYoAxbLpxihXL1HyWT2WYamAycKz67GA1g8fk_arMtA1vuhVnaX2tEH_7r3UWd9Vp1op_XFgNckUC9YeC2nQiPvEy1aAqKNtetwA6igA3fe0gzG_rL4KHCeMh035KN6yV0n2rzct3Uz6e8dw35Zr8tSWwlsqsWg_UsohAQJWQUHtuFTukxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVQ1AztE5oZveEhSjYrQQh0s_smGYjzxo-NQsoEIueHHSwOSLMOJpHP1_qkpq6rXEYDulX3Ui_RhMG18O8ZNKb-MqME9lOw2H4faX6NvZR9N_gRazTM5pupdtJcIbsoSjCdFNTFOFAuLI8knulAnZa7kmk10J_BLlD5Px2cG1s69oabnYefAUyo8WDxMq3MlPD4C9u2uh4YjNK-hZ7KSJLe_R2nrYsbUUF428KSmK3ATw_2-jYB71_4Hyyr6DqbZDogfqMLXRCI8_WKHFe2b25pUbLUENzUl8p8J_vezxTq75lNq8pYSx5Atstc9GscNwWaBvnSvSKS3lPMnOj49xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fA7W7CpdRP-hzBTjcZ6pRwMxCH7LRoSxWvDSqick7lRvglzENPKVHkiC62AZYfWNYm0EB0NyP_EunnwxBEh-1zZwBIY8UfXSPGP1EcBor2REtT3IPF0FbkycmN8i6zgb3KfmNWRFObVHE5pk9oEr4zIQxeaMD0XY-KSatjad-1cciNKIZaCZYfeGpzjphitxXzLz4iKajVu8uYgL6VEbdeBo_C4vgIZamI6tk6sy-tK0UvI_liViQOWb9zPnuAdFuaW7Y8hoAexOzMDjD-pkIX-J712zAselSSWgtTd2k_Yuar_OCP42WMR3HNzvbmOS9WFZD74WLFaWkeD3wV5-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aA18DsO7IDbXJoOsksTMjbs5tzcKqzLYdRiyY5FRLGBBcXzw9oa39R_QHO_YjsMd4LnbIW0E6vOvAU5kAI9ZGd4Mot6KcyTVhefrZ8Nx41imPcSmQPgbmsTnDjboF0VwDbH6K-zXG4iTDYwfO9pp9UGk6qgdi6Eyey1NhBJ0iuG9UPIF550oUY3Pz2xEljek850t4nHqBTfOgPADuFQ8GDTuaWQC1rjKIgvqjKy9y8NQOD70fUrls7pWtmMIqT55yvr-Pxx03xgffwdS8FQDfr26KPpju8E9x7iSOvn9Ddz7Sf8Z6cNKJWGONpSNEMVOTas2j8saFYBC3pmrOdwmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=QVyZ8pnXr6eB0PHv55g28irMtwIc7VdifHV6yYuGwhWklddIUkpSk-orzV3BoYr6YkLk0HLaH5Q6dts6eG9ug-a99qxPzfU57OWgXFSd3NGNYW7f_77G9aotCflFCNvL9uIEYR4AxZ92M8WvT6W34_hWrIxXRmgH8Rtl4V4jxGUTn1qZmG80OKpo-AH5gm6fVpDZy45UWbZTvoTEi-L5R9-cIt7S9Fx7w1ehGY1aICRPFvOeEUypv31lcdjDN70ykjQ6NfxvLTtAopkptHu-i8NKjqVOZUyAsjvua5gGIU1vpWQuTuNGiIOFO5cLAd1atbxh0wV7i7upP-NLlZ7Bww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=QVyZ8pnXr6eB0PHv55g28irMtwIc7VdifHV6yYuGwhWklddIUkpSk-orzV3BoYr6YkLk0HLaH5Q6dts6eG9ug-a99qxPzfU57OWgXFSd3NGNYW7f_77G9aotCflFCNvL9uIEYR4AxZ92M8WvT6W34_hWrIxXRmgH8Rtl4V4jxGUTn1qZmG80OKpo-AH5gm6fVpDZy45UWbZTvoTEi-L5R9-cIt7S9Fx7w1ehGY1aICRPFvOeEUypv31lcdjDN70ykjQ6NfxvLTtAopkptHu-i8NKjqVOZUyAsjvua5gGIU1vpWQuTuNGiIOFO5cLAd1atbxh0wV7i7upP-NLlZ7Bww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=lPuyAGf5fVYBih6ztu7rq4FhzOvCQ5zj9fd7dNBWDB27qfLOXdzaz7muV43cY91K45TcHL3uMUPfSEmhfzCPHSbjvrQcCj1mkQhrXQflW-79inG6K8ltr7dfdhoGivhD5RioSkQowgHwtlx9I1lf5ZIIyZ5DYxaVNhlIQeR5mnUDZ5CpJmazrI65QojT45oeIvNImKT3wpjXp2INFqfiEdQthfPU_jek3TgkYcA2yCFoELUNi9VlYqc4wTgrqJg1osBL777XWZi5Glg8Jln7Q9GOluov5lbTobrH8fBCAOYTW9He9i4adtmlvkYbYegj5FkCsMWSW05Cz9CXHnX1IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=lPuyAGf5fVYBih6ztu7rq4FhzOvCQ5zj9fd7dNBWDB27qfLOXdzaz7muV43cY91K45TcHL3uMUPfSEmhfzCPHSbjvrQcCj1mkQhrXQflW-79inG6K8ltr7dfdhoGivhD5RioSkQowgHwtlx9I1lf5ZIIyZ5DYxaVNhlIQeR5mnUDZ5CpJmazrI65QojT45oeIvNImKT3wpjXp2INFqfiEdQthfPU_jek3TgkYcA2yCFoELUNi9VlYqc4wTgrqJg1osBL777XWZi5Glg8Jln7Q9GOluov5lbTobrH8fBCAOYTW9He9i4adtmlvkYbYegj5FkCsMWSW05Cz9CXHnX1IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=YiLaxRm6DANytpKKK5GmkOMeKo_shvynl8YIpuH-jDOIz5WumFNVs6MBdJWy0Vm6c5dAcB4PKI9D2eSA0pNxID3_U1jpTpWPZsM2teayXpTiDBL15gpSt5vV9Jsu_A8SwqUZQbbCtfDxj0NE9IgpfK_bLZizeGkzZRtJX9qm34TFHvNHluvFa9-1BnSd_Vjnd-hL3L-3VNPgLOk3-6E_pHyaIrp2Zc3cfSLIf8fFm4Sf4UiLBXkFz9QXeeJtaos4nRx4GxLnAnnYcmlMB6IsSCogaxfZngK7oV5Gk8QDl4Oj1Hz21Ya3Z7kzyGjq4ih6tRWVh16NInuW2wOMW81AlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=YiLaxRm6DANytpKKK5GmkOMeKo_shvynl8YIpuH-jDOIz5WumFNVs6MBdJWy0Vm6c5dAcB4PKI9D2eSA0pNxID3_U1jpTpWPZsM2teayXpTiDBL15gpSt5vV9Jsu_A8SwqUZQbbCtfDxj0NE9IgpfK_bLZizeGkzZRtJX9qm34TFHvNHluvFa9-1BnSd_Vjnd-hL3L-3VNPgLOk3-6E_pHyaIrp2Zc3cfSLIf8fFm4Sf4UiLBXkFz9QXeeJtaos4nRx4GxLnAnnYcmlMB6IsSCogaxfZngK7oV5Gk8QDl4Oj1Hz21Ya3Z7kzyGjq4ih6tRWVh16NInuW2wOMW81AlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=ZlZmW3Frt284hUlQCO544isP4rABid6J2NVNrnAcn8siYn7G8yviCHlLZ9a0KDGohHlCstmatSKFISm3O_0Xyt15WQrifLvLCHh4P8LYdr6K2AXEnvtbHt6nK0sVL8aS0I-3iDeIWiEQR60q7k0n5rijzO0EOs1jn000P-cREDpDBg3Pn3QO8RAsqKCcX16S4jUglJ-h6r5IhZXCPMKJzURqmiEFAwGvjNr5XmW1asPMdzMF4smMHkmawLcp3VkGXsz6BuCKCrCzdOyhwBepSG5vloDzenbPADTWXQO-qJGYOU4HIhx4ZV6JpU5gjxwGjHjoUu1-1bB3St5ojH9vIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=ZlZmW3Frt284hUlQCO544isP4rABid6J2NVNrnAcn8siYn7G8yviCHlLZ9a0KDGohHlCstmatSKFISm3O_0Xyt15WQrifLvLCHh4P8LYdr6K2AXEnvtbHt6nK0sVL8aS0I-3iDeIWiEQR60q7k0n5rijzO0EOs1jn000P-cREDpDBg3Pn3QO8RAsqKCcX16S4jUglJ-h6r5IhZXCPMKJzURqmiEFAwGvjNr5XmW1asPMdzMF4smMHkmawLcp3VkGXsz6BuCKCrCzdOyhwBepSG5vloDzenbPADTWXQO-qJGYOU4HIhx4ZV6JpU5gjxwGjHjoUu1-1bB3St5ojH9vIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx0T-YR64h5KvfJFoYvIwERksm9AOhBlhqg-kbigQ0A9ge75x1oM1iMseWy4LGTvX-RDCaHqepkbzk-YWD8qSvHck-FaaAM6UEC_qhSg4BAa-HAt5r-Kys-OfYiZp4DbB_LjnQpuQ5Oo_ShjJeCziqn8pU68f_8OLETYQwfXZIvN88rWcSdXSkbewfcv5py77yIWgaEpmg870voeFHzBXPsnmxiFTRwfxMI9F5Xb9lvlkVJc5ERPzymsfwoNk59c9gaOoiNLlsbaNxle9qEOnzaEe_nrhSP_iNdsPyUSm8I3JjTUtbUMstUO5vFCT07_YhtEfXY43BGlPcGlMibDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOdiFVgTSIrjY0TtDB3-lVhgYwry-Koa70HZNb4F8Rq2v2vpPXjScAvRcdohLqtPmnZahkzds3pzgHiTAzHMmHfkTu4XlINYPue3VfKHVHZ9_VM9Fr9UP6N_68oVI8NM4w5BHRqdQEuLavqUsfIT-zaZxHn1rUko8Ae-oGAR3BeodOT2qve_3sctazDyJCQFDZZvGr6Q-YRkmYJabQHtV2pfqzhAaIEvvqew9Oyuq_1X8DiG1U5ZB99l8a7yQuwpviJfQO7SNvSbVP0gMV07-D9Ti_kskQigfCK-nOIlG16yA71e2n5WsIRY5LfMD-NLNxY5pphey8gxdm01qWtwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=EKTWYYaCQPAIDLg4kklEUId1QWymjKKkKEvQDPocLyJOynLFT85rBaMOHHL4Ti4xMNT5GpYzVeJiC_NjgOiVM_4zBI7AfJcJpD2UGUphmJjDYPpoGzQOEHKlFZdje1UR1VrO3LAZggpaZYKkW9FaNF0yh5g9X9J_gnjXLII9N0wS4wTirT_L7d347uGIR2pBjwESuVIqRhA_1Lz6KpMSNrM7Vj4caQWNnMw2z3BsbdgyVdgo4ha1oMFNjSprrKdHD6ti99k_NKVaWGueBgPK_ZzhikMlTsmLQ6heG3XwjOrsAUD2cjgrCE48YovWQxbmmxI6hi-nhwxlvu3V62YVZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=EKTWYYaCQPAIDLg4kklEUId1QWymjKKkKEvQDPocLyJOynLFT85rBaMOHHL4Ti4xMNT5GpYzVeJiC_NjgOiVM_4zBI7AfJcJpD2UGUphmJjDYPpoGzQOEHKlFZdje1UR1VrO3LAZggpaZYKkW9FaNF0yh5g9X9J_gnjXLII9N0wS4wTirT_L7d347uGIR2pBjwESuVIqRhA_1Lz6KpMSNrM7Vj4caQWNnMw2z3BsbdgyVdgo4ha1oMFNjSprrKdHD6ti99k_NKVaWGueBgPK_ZzhikMlTsmLQ6heG3XwjOrsAUD2cjgrCE48YovWQxbmmxI6hi-nhwxlvu3V62YVZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skiOjVJsPLwWiGq4rgvfclQc3kL0A6WiL6HHBancIQWiwhTjEPL_T7NBnEf1x3hBilsLbW1s9a4yXRjuvX_B0hYMJVu8ZXlmefSniuAipph93MbmfumjyafrTQmZsFzahoXX8VYnWeDNacbP8fsnP-iZrHwRZ_qvTwslnzNx1tTD0GJlqI4TbJnCTA3TfjRuB-FRsJExZQTTNzd3MSm8mpKjX8ySei4JGfPZqwXKhNm_susWr31DT9YsBIYLAfFW6RcPMJvyE9m6jWdmEICcEmwH40xqBYW_ZwxNgFTkqE4GXH3R1-NKpgsOddg-kmHm42EKQ_jmvL6p7_p5x1ZIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=BniJ5WP07Rz_csQWYjqvX8qCPEhCKeyvTN2oco_6PM5RBp9EHhFYUvcvJqL9muOvswDx9FJoVjbIqmNuCz2YPpECBpwi1dkylcqBgCEjIYFr1ScKH5yCw_zuLp0_OYVF1EfoNF8tVu5IXiQy9fpID7nhiAsad4mWo-oB8YEvb5-_pE094A0hfEf5vu4IGeC0XnZEboAfnBG1QLEm2NSs2pldMC_v0A6CXF0lu-5qDTWre1T-DnGgWxacpmzeKSYTwtGshQNeQXlwWqeShFBsStg7jievL1VVcLt2KvA_behEB6E2d-SdZSffnXZgvujeQcyLBaavGxp7l9YUR550EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=BniJ5WP07Rz_csQWYjqvX8qCPEhCKeyvTN2oco_6PM5RBp9EHhFYUvcvJqL9muOvswDx9FJoVjbIqmNuCz2YPpECBpwi1dkylcqBgCEjIYFr1ScKH5yCw_zuLp0_OYVF1EfoNF8tVu5IXiQy9fpID7nhiAsad4mWo-oB8YEvb5-_pE094A0hfEf5vu4IGeC0XnZEboAfnBG1QLEm2NSs2pldMC_v0A6CXF0lu-5qDTWre1T-DnGgWxacpmzeKSYTwtGshQNeQXlwWqeShFBsStg7jievL1VVcLt2KvA_behEB6E2d-SdZSffnXZgvujeQcyLBaavGxp7l9YUR550EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWoerlmMBo3kyd0KRFwxpU5_y4WH_6OHbQ_GQYd73_8ErFGvpqKb9pov8tCAfHZo-pCSUAQksn9_EvvFSVOq_S9DMJboam7sbFUxCQBbxNENxTw32I7aPI9T5YqBy55BV4KwgF0J9GDkAZYyPQQ9ANlbRTg8jF6eaDYo6rW1Dv9WXt2jm14kJDZsKz8B0amQ2hA4tc4daoMynvEHBIKaMqH1bfCXCGbpbF_r_83Krip4x6pEPzMF1LFKRoOpG_kJ38XCnJKZYzzooXxOpyltC7-a4zn9vfGcNF0pvYsfajBJVo0AJPGzChUcb8uMDCjKfDwRb0axQVn7EJPBAmLGDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMJHl6h7IiYJFNx6fUIuE311zAg1EeMucsRSTyERu52YyjHoRVFWdMzaYL3l6jA95XWhfrv1Cz0rwR78E6YsDwe8p3uBq6W0W_FTAFOb5dN0VBK8WbNzAIjvlTdEH0nUs3vTxp0wU2PZs_b7AeQ0JcgWHPLmglzFeX31Uy9QuEJxwCNeZEyresHwPy7LDwRCNBI0wMgAq9_eUWjyNt75GIUtSPtMeSq2J_Id3dHQ3Hl6bkePrJJtCBrq3ksS5AXCzB1jfkn6vD_dVuCYqETSquVbWfQkZd2nP8AIbneFgWsxJSwahw3c2aNn2QhQiYArJBYJCmDhonN8o2-64QxIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=kNIbokRUwAVz0MsW70oE3yYGhozdVo_523gRZDeAD12ME5mZu5nktRabLE7KFKxP_-YewF5-4kxUOiDxUOXGXFcLh1zIgqzEE5LHvL0jqqXj5x9xK0xqKi12r8IZywqNFp2_0IOdMZaVTMTLfN_HSVsXtFHG8IJPEjBIvRpeinVteJ7Rv5n3ZuLFqlXAycVF7XgaXEvEq2u6Ity3i8B1GyAC9a34Rda7dFJJLzT-7-35dw_tQUI033-dd7iuFnpu4-N19E2WPa9kcmz0oJtVozyFPimNQ0axW6Bm4NxF4StJcVE1nyATA9nE_J6bQD-KSRwFNV-PLu6IkpwgD4x8mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=kNIbokRUwAVz0MsW70oE3yYGhozdVo_523gRZDeAD12ME5mZu5nktRabLE7KFKxP_-YewF5-4kxUOiDxUOXGXFcLh1zIgqzEE5LHvL0jqqXj5x9xK0xqKi12r8IZywqNFp2_0IOdMZaVTMTLfN_HSVsXtFHG8IJPEjBIvRpeinVteJ7Rv5n3ZuLFqlXAycVF7XgaXEvEq2u6Ity3i8B1GyAC9a34Rda7dFJJLzT-7-35dw_tQUI033-dd7iuFnpu4-N19E2WPa9kcmz0oJtVozyFPimNQ0axW6Bm4NxF4StJcVE1nyATA9nE_J6bQD-KSRwFNV-PLu6IkpwgD4x8mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=MaZviR7vEDQXecKqChwzSxnL93UKHB2SqQ_Ye0-ekLiV3t1v8uGnLRcp3yoRBoaGl3iZ-XF9Iia5DZUkt8w436g9uPlTLpoMSqHf08piGUYaZTN857dpOFj84dy36kQhFNT2kcebwR5t4kfwbfiHnnRdWD-EqGxve_Gm3D3NknSUVcMpsd-mdTBIh5G4lZeJO_1QasIq0a35bgFjjI75OQvpBt3OGllM_HjGR5H_J_H9uq2VDnHpcAGhPPqO6rNDcUhawRYTj2dfwWo5iGTntVCeZuRhJc1b5XAh-knFKXxwYisk-8_jebnI34k-tJnomC61FGInEbMx02_wl0eY4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=MaZviR7vEDQXecKqChwzSxnL93UKHB2SqQ_Ye0-ekLiV3t1v8uGnLRcp3yoRBoaGl3iZ-XF9Iia5DZUkt8w436g9uPlTLpoMSqHf08piGUYaZTN857dpOFj84dy36kQhFNT2kcebwR5t4kfwbfiHnnRdWD-EqGxve_Gm3D3NknSUVcMpsd-mdTBIh5G4lZeJO_1QasIq0a35bgFjjI75OQvpBt3OGllM_HjGR5H_J_H9uq2VDnHpcAGhPPqO6rNDcUhawRYTj2dfwWo5iGTntVCeZuRhJc1b5XAh-knFKXxwYisk-8_jebnI34k-tJnomC61FGInEbMx02_wl0eY4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRFWiwFRaEM1gw13_NmceYl-ekLaUxD5VtLB1N7WnQhLVDg77stR7BUrzzNH5qYm1YoYyc5US0LY24XGYXL5aifb13IXujczsrrN5b3aS6iiHqoKsd4gkeyAUIWAOch8jCFk8z87qc-H3y-PPwpIfm2OJ-tbNCNfPtWnL2FachJi3pKBkfrXmPl_-ZgiR0gcoxY8rG0SQcqWUi7E8lU-Pf-cSp8D8_pmmMDm-c1xz-U5VGXehQQMko4ZkgRDbxwWfD_WiFidjxrmyWeKxl38LGnMeeCpVmgVbbDP5SDjbJwUV8Jhshbdjd_PAX9pxH6ZpiJA_ZA3_j4Tu_6vYO6IBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlVba7iT34_e29mY_p37J7g5R2CwI7JiuM40uF8Cjt2j4NsePY6haw5JXVZ05gAXV1R9W7SLcAWBf7pxutbAM8p2f9tD2PWsyyhxJqWCTjxZ5qpA1ZGjWMhCWSlP3UCA46amCqo-plKn0eFnI0X5CwDXzJUyaYtDsr00Cm2UIWF1lopUXroO_UZQc2SCEfk9bIrcfLgG2h2rF8xD5cLb6ZL94XWHR_dk0dNY5VuDzKDjXuBU1l2yvAqkXlyDEoOhuvvNLv6MtAfCMgoWJw-33xZUOiU3cF0fl45bD4oeDmes3qqiM2SJwxJ-A1ftz4VaQmjESpdEpUPO4H5XKZUpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFsDeNDNOOhcq2-LHOIc_iRcfBGeXbM-lfpg69uuB26JdkN1jKw7tkIqNkUxMcJoUjYE0fUOTZ4vhVmn4eWUNFlteRRc7xxYEwrx7B6SOGYx2GlhCDy6nm1HxDM3Iq7KkhHPw9NwWp0fk46oJ2MXFhPwZmdrMejNtpUvngptevN1LqpoObOe3em5q0r-S1JEjFqTLWF7QY4JCanQ4_B9DCAkb53IW_iowHc53x9zv6ImCkm-hQIJzQxFcyq4NSvlPXO_AJIWMZrGjJSv1yDXgZrNHFKcAGUnfqVTQ8XvPktp8exr4L9v5Ysmz-YHgVf_KU6k6S0kUv8nLcM4aIK6Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=PKpkJ8JddOY3hJbGY_XexU3q522Xw42xoFwzuxttD0AsssMSjGR8cu89ZVJhCgB4KUYkd4wxOlv5cxOtN4O-ZixzoFqFC7nM-B3j682DAve6J9Ca2mkbjBliFWlnoHFfCv1UJE8t0x_jzAUF6UZPgEuezpkKcm9K098BRQVmBwI4R5zObF-vHqFft02K1EnJviCmNsixpGA6Uot5Fsv1mMvFvmD4tbV3rXpLwljRuFoLemuw7KeygX9O7g7hAjFPwjvWSXE0srKB2ZLN0INzOpMYYtrXlOo_YyUIgMCJ8GAxnPBgI2omGGYjuTML-dPY1HSJ3UvaxoyUfzF4qBoRcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=PKpkJ8JddOY3hJbGY_XexU3q522Xw42xoFwzuxttD0AsssMSjGR8cu89ZVJhCgB4KUYkd4wxOlv5cxOtN4O-ZixzoFqFC7nM-B3j682DAve6J9Ca2mkbjBliFWlnoHFfCv1UJE8t0x_jzAUF6UZPgEuezpkKcm9K098BRQVmBwI4R5zObF-vHqFft02K1EnJviCmNsixpGA6Uot5Fsv1mMvFvmD4tbV3rXpLwljRuFoLemuw7KeygX9O7g7hAjFPwjvWSXE0srKB2ZLN0INzOpMYYtrXlOo_YyUIgMCJ8GAxnPBgI2omGGYjuTML-dPY1HSJ3UvaxoyUfzF4qBoRcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyHHh-i_9pZKsziaUJB1MxagyvxD3bsJHqM51VnVsIkAi7FxjYV8wl7duT6sjN_ZArmxoE-8Y6cq_MvyfwyoqT-PqDUS0S0WssGWyGtqGWsWlTp3BNVoWw5zU-tFIjiy4C8_i7MnAotz8ixuuvibjVJCK7j9vQaXPrI231LuxtCRwPHUVKyEdDdXHEEqhZTPzlp28JgyZX3pjzZ-YnAY6jBj2H81MbaB1EKq1er4uBjR-zrLf3a71PcNoDfs7UFDV0n9F4NwcXmJjKsS6i9TeGuf7HUFQUIY_V8OSd2GzMdIRdaeChVnAjDlty_ivkIouBvlb9JmvzJtkHGovo4QbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiG4IRTH0kF3tSq7EU9u9OISSTQJ73QYg3ikmT-eSoPTZz8wuvdWmL3VQtoWxMNx1yHlnAuyoX_0h-JxIr-22dRNjbPDSoPE5YQahAskHwfu-7DzCjKtcJ92R_ehqR4Sez24wiL4P9FI9gwSMTNZX76x8CBEOWw6eQcv2EuMC_wY8jE9-QwvwodHHzyCJStEoUVDI5nMc_PhfHC8g5CN73Md-sz380QPkIyz8qrRUTjtX2VUBQ75lA4_RN-4rvuO0asvl9PscAKbtLfcldQSb0gFLbA9ey6Ct7HnPspdsaKUSXtSfgxzMSlb03gUSXjo9SeNbsMe0v956geCmz4aAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODFQAJvloV-oIjSaDr6Zr1Bzvbmnaej7sjyVNQqH1M09qbvuihu9KCafofGsL1_Lb8T56frH34G4Dsm4skWecXPpMPwKjbHndifYt34Dx74QfX1nm5_uysz7a4chG9-_FbziB8QNQb59aZtDm6zYBhm6rncXv0Z8WKZ4FKWWMiFrBMYTZrXd1gmoXOtlMbXcmaxdjdUa559n98IN1VgrjWjPI93USKi7DtqX5wars2L5gFuguzkM-cthkWuUxq5LJfQ45fjsWj7M0jJ-tbC59kb1H1stuAg6GYtePAWcWKj7hVdx6ySQMYgh2rjPR5UhaGR451505TUGznbjwZDyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3iIBrtalF1BCYAhcp13K0Psv8hFWyhl3pczHKk8VJ_rcPM8TBAmehilEXbMiR4-NKZ8vL7_6CRPS0PYFUbo_YOPkCBLqPCDvjPTs4IOc9nx8rN7OldM3rd7ajUwpdcQg2HsUdQynWjaP7fSBjKzM0n5xcSawSmiKITWwZQyd5r4Bgofmf4zJg5xgI-ArvJpp4MMPAsho_gqTIRQfl1kmNumuHE22Gqc5g46r_UtP73OVTRB4v86dGKWrBtl-iVWzsXTROrEdv7z-gjJgeEPSkQ7a8M9IVpNqET4Q7WSBHlzb9-zhAe0jlMH0deKDaFM6GmZz-F47mLBUyBYCaSDTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=aqMykCLKutJpgiQrKsgqCCGJErxP-C-LCUCbbHZfG6tkP3W86eukQpjRsV-IW2Nw8hdsnrG5FSme5t3nDDiGgd50HTi-GBKWteCqSi9V_0ks_3GTtLw0n6UY9hjzjYt-6kTz5DI11VNTjHKrZdYi_1FRm5gXoKsoz6ZtK4JOM0ayrYbq4vkO8SX_Nj43FejaRKV-SoAUFPT_4C6pJj1pEoIIxN9jGU6_PCGkBg_HXtAArbHLiSxdOdicDjCUIxtPmNuH4eeskBEiZyVRSS5juiaJURGudTTA2exnZE6zcUV714tNOWyGC5KUjMzGpsPseB9Egp8vpxVK8ishPjeK5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=aqMykCLKutJpgiQrKsgqCCGJErxP-C-LCUCbbHZfG6tkP3W86eukQpjRsV-IW2Nw8hdsnrG5FSme5t3nDDiGgd50HTi-GBKWteCqSi9V_0ks_3GTtLw0n6UY9hjzjYt-6kTz5DI11VNTjHKrZdYi_1FRm5gXoKsoz6ZtK4JOM0ayrYbq4vkO8SX_Nj43FejaRKV-SoAUFPT_4C6pJj1pEoIIxN9jGU6_PCGkBg_HXtAArbHLiSxdOdicDjCUIxtPmNuH4eeskBEiZyVRSS5juiaJURGudTTA2exnZE6zcUV714tNOWyGC5KUjMzGpsPseB9Egp8vpxVK8ishPjeK5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hsZq9hPjsZQq87ITXaZCML7BzwRS0Jd1S0P_817tXu2k9xlS7CcYqMwnSEsiTF4ajGOnQgyOk28_6f5kSNTY8uiouGou8kGsMAjlWDMQYnKv9EdiZGPrsE7sOkZD0K1E2edvs4T1fzkzpHeo5_VMg5liIQRKs3WzNQrtYVsPalfyBjxp1eYNezTN2sDXs8kbgClBUXHlXWHVt3y6Uq4BNrbspTUphG1Wd7xuh8NYn7zSUC7DumDD6Mb1KB6h812DMzGkxDU7Rw6d58l6HzIBTcZ1ni4M6YPb_tdvipsL52u01ffhjq5k_giIO_uubWNQSdKUZydob4E3lgt0RuFCdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=CmWqHrpS6pWBn08MiciW6eEDlvJAgtDe1cbq-76o1pMj85iL5BI3NvEbfKY3MlciKZOAoQDpx9oYCPkuAoZYNXLXzjPy-Z34o57vXNpzc6eEoiB1ZIKlnPbX7HgvMUicvheXBIg4whv003EhIpnLnZUl6_4USjgAonGuK8UUsN2juW0u_x1fmldr3UjcaYg6hS7n17aIUztwJ_sjpcNgmPpSY8KtmF2MbeimhQTjKsyPAMHFZMVmGdemOgpZMRktoGpPMRQns36fliUM2gwcDnQfUbEalSJ_21UDxFgwOR864sd0HG0xzfE0cwH_sBl1UssFhSm3nfqnqMjCeSaqNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=CmWqHrpS6pWBn08MiciW6eEDlvJAgtDe1cbq-76o1pMj85iL5BI3NvEbfKY3MlciKZOAoQDpx9oYCPkuAoZYNXLXzjPy-Z34o57vXNpzc6eEoiB1ZIKlnPbX7HgvMUicvheXBIg4whv003EhIpnLnZUl6_4USjgAonGuK8UUsN2juW0u_x1fmldr3UjcaYg6hS7n17aIUztwJ_sjpcNgmPpSY8KtmF2MbeimhQTjKsyPAMHFZMVmGdemOgpZMRktoGpPMRQns36fliUM2gwcDnQfUbEalSJ_21UDxFgwOR864sd0HG0xzfE0cwH_sBl1UssFhSm3nfqnqMjCeSaqNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=p6klmWWb70XcUfKRtLVON137Cu1M-BZysgbXlq7bafwGM4xOPUMeYFVIuqaTGVyw028lt_K0V2ZrylFsSsLNm0rIDwVwOMFkmK3EGVvAnOxAYr1cbWHwRoBVTGYiNaXCekghKF6f1KZkblUOiNngur3Frp88kWo6a_VtufSJX9DfYHqNmY0y-KZeYd42rsedNBzCL1tY-45DujxEGqkm4q3y4ThDdfzRxJwPjEgYi36ZUI3ozjrP5OXMIGSeEbbtOab0CwFSAtKwc3A9PKF9eyk1bdbM9oxjIwkHAWgeVDLh9QTTazqE7_oOQFHv4sol8hHi5dVBf2cEICfPWyEV4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=p6klmWWb70XcUfKRtLVON137Cu1M-BZysgbXlq7bafwGM4xOPUMeYFVIuqaTGVyw028lt_K0V2ZrylFsSsLNm0rIDwVwOMFkmK3EGVvAnOxAYr1cbWHwRoBVTGYiNaXCekghKF6f1KZkblUOiNngur3Frp88kWo6a_VtufSJX9DfYHqNmY0y-KZeYd42rsedNBzCL1tY-45DujxEGqkm4q3y4ThDdfzRxJwPjEgYi36ZUI3ozjrP5OXMIGSeEbbtOab0CwFSAtKwc3A9PKF9eyk1bdbM9oxjIwkHAWgeVDLh9QTTazqE7_oOQFHv4sol8hHi5dVBf2cEICfPWyEV4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ku-vCvn_1rvasGqrr_RV_psQAmj3eXdogIzaC86Sq9qULC6Zn-tQKV_JtJDRQbX7A1iL1b1nYam8Zce45M4hcdYt4onHCk6yYsN-AvwM0FGUbMN5Vpm3fG_8KwgwK6RSOUf50NPprQU4V0xfqj9Zp0NhdaGb0ntbETx_vh_DvNYc9Dd3qLWDqkH9rxxsT2V2CttB9V9y0LC74QYNM5s3dBa1LjHi5eaJ0TDFL0Zp59fGRZf8g_fCumIoH4rgQ1eT5cH0NKlXO6my_fL6zhHs5zIqvtqbFyDDgpibIbpNBSmw4Gv0Y7B7_OcTbRt3WeKotzNu2uoyuoRKyzjhS2aZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=Ac400SPtCu9e9X4sB_L1w0oB_0XXOQC_SvApst19gdvsduNk9DpTK54tTJHM6foWUr9sjVsWv0E8FxKgtSikRLWgxzff8vuJ0XNsanygLs9vLFt9eMUMd3Ux6X7JbHviicPWP37YuzA2gZqo88GsatYJViuMYjZHdgu-bHvxsxxEx8-9_omnMIsGZpGYV4ogbQDQGJSte7iUu5DEVUYn8r87SKGak2aCAgllTA8obZ52eSGxsz1W2Zn_3VlpYJ2sVcMm5dVu7AuRiVWaf4IxgCr2ph4Pjo5PBaxbcICz5QCdNBXmmRlysO_dJqeFcQ7sHjAm90ihO5RCGKRYlu-iaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=Ac400SPtCu9e9X4sB_L1w0oB_0XXOQC_SvApst19gdvsduNk9DpTK54tTJHM6foWUr9sjVsWv0E8FxKgtSikRLWgxzff8vuJ0XNsanygLs9vLFt9eMUMd3Ux6X7JbHviicPWP37YuzA2gZqo88GsatYJViuMYjZHdgu-bHvxsxxEx8-9_omnMIsGZpGYV4ogbQDQGJSte7iUu5DEVUYn8r87SKGak2aCAgllTA8obZ52eSGxsz1W2Zn_3VlpYJ2sVcMm5dVu7AuRiVWaf4IxgCr2ph4Pjo5PBaxbcICz5QCdNBXmmRlysO_dJqeFcQ7sHjAm90ihO5RCGKRYlu-iaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=gV7E6uFvu6vGyCD0oS2yVi8hsfIrbecetHzSXLiJ5089JtMkRKOpEykF7BbP_50K5vlWC6p9CG1v7xSAtNbcQpPB_kNDTtd9-NegrsbhiD4hJzdIR2VFLQ_24_u5WwU-N1D_OXfqV1CXzCEORWrLvjkBHmZtrfZlQjPughEaEhFM93OODtSITHWCKH-QP6m0HxLHexykLRm0j5hjlGuvvd5Ef7tNl9xoGjZOzxgU_jXm4K9rAaWCHBLs_caL5AfVmpAj66qNpQk-f3L5lQ1wTtPOP7MeGvsU1Ii3iJswCtSKrhP5Q8jV2HpOtoi-KoiejSa2TjxVYjuUdgxCp0co3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=gV7E6uFvu6vGyCD0oS2yVi8hsfIrbecetHzSXLiJ5089JtMkRKOpEykF7BbP_50K5vlWC6p9CG1v7xSAtNbcQpPB_kNDTtd9-NegrsbhiD4hJzdIR2VFLQ_24_u5WwU-N1D_OXfqV1CXzCEORWrLvjkBHmZtrfZlQjPughEaEhFM93OODtSITHWCKH-QP6m0HxLHexykLRm0j5hjlGuvvd5Ef7tNl9xoGjZOzxgU_jXm4K9rAaWCHBLs_caL5AfVmpAj66qNpQk-f3L5lQ1wTtPOP7MeGvsU1Ii3iJswCtSKrhP5Q8jV2HpOtoi-KoiejSa2TjxVYjuUdgxCp0co3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brOcaHl7oRo5lAEXQP8hb0ImFdQDJJKJLTJ8QsXQ5g9r9pYYebJbqNrsy8WfJhNHHV9viPv4rMq1im3pNnBXADxLccG1F67MF621Hh8O_VRbtyKS0DrHKbQz4wJsQry8ZskzeAtYPWZndCHyEbNPaUdSHKEfF8LR7W48Hc1ERdno0shUx4W-ar4zrjadLdht8JL3sncarlAH-uT4P4uluX6YsUfhTdpvgHC-jN1dDOo2wyM2Rj2XFsexmyag7iduODRJiZtaYT-Fz-NDI9MOkmzBgi6HzVmys9z4m5BU-AfmMNP0GmIdqG4kdHp033eSoGaD1FH0uvuMy-DY45dJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnxrEMSTcWoMpA4CFobLd9kfeIUwmmpnh37ss6avNfBbNZV6n_kTcDCtrm3N_sXPX1cM3sCOe5dhHe_d2YVBqurMuCWTX6yguWFi5p2K7h7_uXo0fH7_hJMJyvZmsz3zBoBtiv--gIbDaX-sEfsHQfdMv3MOhPUlNOrJnDM_wPss9cXUYvGCTkfpGvw_iR67_jfMf8FKCLxDuFd4ovxEKZaBOwg9IO6Gyb0K7FUMvs6RAMZCfyK3dZS-4JslzcASzX5sFhpXyETXLku-fvGD3rKCRzMbYJGJEMsyf8zJ5LqS6CYpIn_G8E_08VvyhUlzQPFn5zq3K8x7ICDe9DwYCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای حزب‌الله ۱۵ سال در خاک سوریه و در جنگ داخلی سوریه مشارکت داشتند
تا اینکه یک روز همه شون فرار کردن!
مجبور شدن فرار کنن!
نیروهای جمهوری اسلامی با کمک هواپیماهای باری ارتش روسیه به ایران گریختند، نیروهای حزب‌اله
هم زمینی به لبنان برگشتند، گریختند.
و بعد به سرعت نیروهای احمد شرع
سراسر سوریه رو گرفتند.
بین نیروهای شرع و حزب‌الله ۱۵ سال
جنگ و خاطرات خونین وجود داره.
احمد شرع اما در این ۲-۳ سالی که قدرت گرفته سکوت کرده، اما اگه نیاز بشه، می‌تونه تا ۱۰۰ هزار نیرو روانه لبنان و مناطق تحت کنترل حزب‌الله کنه.
انگیزه بالایی هم دارند!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuFFZ4CHnBGHsb9qJikMpN5_zNe6eybwwE0qyImRcbrfdRWKBPeDE6XEMpuf-X0rZ62jYs7mNA35FleCRuVNOJKuOvKe3SUAXYiQuMvniN1aw5nHiYPX94dMPYDmTv-UXFvzyZdHzytCCIekxtWoojPH8mVi3JBVgpCjauVyZeQ6McIIKgeRXrLm_zkKX3CIInTF2r4xfWZOmcklGcPZat2lJQ_gbG2Qojxlk_rkZxzI93zeZ4ypPkBcEmslMwXyASkzP22R8yVUne63E5PAzx2H_pW56JFtrdc9ziByBkShOMindaMtL9Jh-bowbBAQ6_ESNaB4eLaqqc7dAiIU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoU7kzdbVfIDiSf2_1O7P7fkCQm1ZRKlBLZk9guyhpD0OYl9wjxEtHrIhGjH29tahqmnEL05VmojuwCdgpvcziMwtnugwgsVqDrGea41hiccDN0FXYv6-Pc7ezhOCHAmlVUOZlxWefUKL7391LGNB6QfB556sIsT9yaAtWlpf3MRBhyVsWNSYSiQ7Pu09VEiAOTdHgxC9usfjZ5Ate8wVUH41EMk9A1lDzvRN30H3YptflW9n9F9uusWHZJEfKy2YpWLFwzRifpwNQMEcGap2XQmiOps3BDyIhQ3QS2jMtXt-7erHkHaCnGBWyDJKepR1F7nAII2GbuJ7bbV5joEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=vGak3JyBlJS9d59OwH4TZsQlJyEpb5dNguvYDJ7WXzk0QEbpoef6GAAiFynffL0ngVhwWjSVXR4GuhASJhAY5H83SBixPHi-ee4gRIsav6q3EyUmoi9ALJ6EqfKJmFeH11lmia0aTeWzq2WGo-_6lNSdETb6Hc8cu5lsvYEJ_zUcCDkADkZwVgUzj_4juAX8B_y1swxOa02p8EgISWKyKYn6mfNaokjqYTPD4t8sZER2bR5Q_cf7gQnPqOAJCJyKCQKLyOWsVlrHdt8xMOnkJnE6N1e5C3wTdO7Ej3uY6HVS7u1MFs_qajxV6nAMc-5W9hnKk1WscV2sLUVYQyC6og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=vGak3JyBlJS9d59OwH4TZsQlJyEpb5dNguvYDJ7WXzk0QEbpoef6GAAiFynffL0ngVhwWjSVXR4GuhASJhAY5H83SBixPHi-ee4gRIsav6q3EyUmoi9ALJ6EqfKJmFeH11lmia0aTeWzq2WGo-_6lNSdETb6Hc8cu5lsvYEJ_zUcCDkADkZwVgUzj_4juAX8B_y1swxOa02p8EgISWKyKYn6mfNaokjqYTPD4t8sZER2bR5Q_cf7gQnPqOAJCJyKCQKLyOWsVlrHdt8xMOnkJnE6N1e5C3wTdO7Ej3uY6HVS7u1MFs_qajxV6nAMc-5W9hnKk1WscV2sLUVYQyC6og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieHi6p7dSDLYqiXAynvp82tEe2BDYb4SNUevqJxkVMWa6Bn5_5iPrT29XRYdwEC1fjKxrq8OgC3L6MdvMIhw9eRrVkTC30iSNEV30ZcA_k--d3jqruKDUhO7d7P6G9KtzztzexOWKVYnkiro0kiyx2VYBnAmWO9fNc7fePhM5AmGZ46w2Plehzm_qdS_1f7wKu4ReXenKrTmKqkuwD1ueOn3CpzYlnmvR9V6LRE0-jVPOmsnH-s3NafpSfSNBLf5wyxi2vrZrRuhCmRy5SKMVCTM5pW1Yvg9tTuAe_cB95iUiQkpRIFw-2P1m95NHHiwK3p_qBrsoiIx2064srC-HTPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieHi6p7dSDLYqiXAynvp82tEe2BDYb4SNUevqJxkVMWa6Bn5_5iPrT29XRYdwEC1fjKxrq8OgC3L6MdvMIhw9eRrVkTC30iSNEV30ZcA_k--d3jqruKDUhO7d7P6G9KtzztzexOWKVYnkiro0kiyx2VYBnAmWO9fNc7fePhM5AmGZ46w2Plehzm_qdS_1f7wKu4ReXenKrTmKqkuwD1ueOn3CpzYlnmvR9V6LRE0-jVPOmsnH-s3NafpSfSNBLf5wyxi2vrZrRuhCmRy5SKMVCTM5pW1Yvg9tTuAe_cB95iUiQkpRIFw-2P1m95NHHiwK3p_qBrsoiIx2064srC-HTPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jojc_dIugNkKLFIRfK0VV_11T-VVx9HRKDRUtoOR5U94lcSzW6H28DMm66syGhzlKOe84nFEqX1YS8DPkbG2aJSAGJ9XwrcPBCX8xCjZbch4WvFkw23cjW9Zwi2nUHab03imNrBtv3cTB6GZe1w8nH44a_onalFik8XuHGmC1GZlI6VMPim6VtBXV2JoyMJAu6e7SDY4-kwhgKS3-zR8OlrjtqkZpmz0oSzWldFZVW8js8gn5GLMA_9r-x1HKdaVHNCkUrAU4jSl8RKOTVUWYBQvOYDPi9z5u-2qQA88foJfNeFCAjTAaBVSA9SIcXACE2KVTrDcdYkdGWtfEtBcMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmsdLns9FZ45XHRBAHihnLfbgthNlA9HcCkhgL6QLILTKzizaztENpIzLqVHUco8sVYIpFMzrunJ9jhPsoA4vSR5RC-0hH_AXiBOQoWNw4dnj7VtMzmlno2RJBJwDw6-Hab44UEIsgoRs4ot_HsZWRfhy2Zmn2rQJTVhljNjOE3ftd3GQxml2M3D5noNvdYt_MT5ZTj2gvj1a0aD_rUCBVWjFdHUzh-q6BiK_YqNymIuqMrYlfOpDOfs5GZ6n75xv_h4MUHOIJ0RlEgQkkMe5wC4WN5ZP4fqPi6Mo62Ji9VSOB2v9Hia5q_R2D4WRhdbE7OAMRdvXX-R9mUgSy61_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UV301N1zbTmTLASTKaUK3nk2kC1ZCihXnsON3Th4ELPIu2KtF3M5KEURdy1Jju4ymEcfCg4wbGftu48i0eF6OhwaMnWB8mgIDx1iAwTu560jF-jPGBKtD6rFrYsP1YZ8Ev-3OAn_SzMtBfAFRaqTn1kMmnzssCRpcg8v_KiVi8ihCaUhJbaJq4COsD2ZgMxwRkLjB7Ig4NpZl_vjYUpcXYbf1xtmBJU1m2HMvqgKER79yFtnxQ-f0heuWVI5lyJVqFKrvIfjesNASXawPTdIQ_DQEMyuoUXiyH4Uzu2xBWsshtmRzKnJB69IrKIZVLGye4_ViPl_L8vYj5V345CwMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNN6R9HjbOFLsPu9OylUatSq8YxTIcSd7wDaWQVilylvsNvyF1YmNWjdXSOaraHSL9ud6f2zTh7Ujno_kpIxpll-tJiwAZ9JQhi9Lk4-BJ45vrcHAYhTjsQY9n2O3UaDBeuhYocfXQh_8jk6tDqM5KC2vDpyYniaFEGZJcnwq7ihwgvJ3_QS381xLlGUpCt_N-4Cv-2nIcaJSXv57VBujQ7VRFr5p3ftVfY0nQ7FnMDtVhMU2rxlDkPhLCPbejonESZEOm4ArgmCPbjqJ_-Rb41PEuXnrO-gJwzia7-4awQplqnWLuVqOuQwxg5waF7BAj1yRNYpGSO5kE56KFrqwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez_7ftoGmN4YhkRn7TuXXKu4WdfoiiV-L68o2vcIH2aekdMArVZHyp9-oH2_Qkm6fFIW-McP6FDs0eVOXlVhmdFYC6iIdPiAROqJPje3hRay_qu4JcqeNsrB3RlwJGHRNlrD_m3bXhjGhLgtsKZr1x646JARu008Rl_Dn2zYVRADf3yS4w1LPSOMH1VwYY7cdNJSI_QxHnOZRRgzBI80wBaXt-vgZhQyyNwEWYWAMHJ4Zgs88FF8jbWWAtZBOfQEKDt6uIoLda5b2feNtRIDtxhSObXpRyBy2HJ097MBA_VBbOSkoA2ZXoySFNjXhwDAv944taWsnbbQKjKWWqu4MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=TH3X4M-ZxhxEZjd1ucXrb5F10aUGMWF36EMy0o9asao5_lNMeUfi_fNNNHe3LKrOBaRAYogQJ8lk6mBoSfXznL3kXvmQbnvI0oBTD-mwcFkt9Hc74N0DDpfC2MbZKVKM3Z3R_kRZrPs38ciH1EZnpeZ93eNmqUVsBY5Ujj7nzGMpZMpXDu8ATSqYvja2ek6mtPXF0nq8TzU3PI_Cp7iU_zUh0efB6g7zTxbZKDlnSiuZTSOSpWF8vK9ZPwHzAds4L17KfvVHv8_wSEFnZCo-K-PdoGm5QDBAodMoHPxmkVAP9jV-9STgGEbNn9j1qPb36a-NJHGCjHB-U60yTi3MnRzglPgWMX7-5q1RhysfaMHxHMVFZjO9SS6wtVzWVBbZX-tjokhHEaSkJ7QOo75_RLPSliM37-VY1KeLSuvm-3FwNGOzffp6lRISet16dL7AvrDvfZ-9NNGVGYABs2LEXZCpF2y1qShDQ8wTonpAxCbCc2vPLqQrwgs_Zvi7YtNwc-6uzYvY3o_ZSG2WSUl-5dItw6MEpSX0iWY9Ep-gDEVqsa0YMrLOXzzBRJ2YocaeoSz_GCwp2lsZuslCcKrCydL2PCFeFdBvdHF9-_yyM6hzj9RdwwBMIW64zMu-fhz_05t5L5sWGznGGfrfa1_NQDRUuhdt-gv_6rkKwaZkI84" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=TH3X4M-ZxhxEZjd1ucXrb5F10aUGMWF36EMy0o9asao5_lNMeUfi_fNNNHe3LKrOBaRAYogQJ8lk6mBoSfXznL3kXvmQbnvI0oBTD-mwcFkt9Hc74N0DDpfC2MbZKVKM3Z3R_kRZrPs38ciH1EZnpeZ93eNmqUVsBY5Ujj7nzGMpZMpXDu8ATSqYvja2ek6mtPXF0nq8TzU3PI_Cp7iU_zUh0efB6g7zTxbZKDlnSiuZTSOSpWF8vK9ZPwHzAds4L17KfvVHv8_wSEFnZCo-K-PdoGm5QDBAodMoHPxmkVAP9jV-9STgGEbNn9j1qPb36a-NJHGCjHB-U60yTi3MnRzglPgWMX7-5q1RhysfaMHxHMVFZjO9SS6wtVzWVBbZX-tjokhHEaSkJ7QOo75_RLPSliM37-VY1KeLSuvm-3FwNGOzffp6lRISet16dL7AvrDvfZ-9NNGVGYABs2LEXZCpF2y1qShDQ8wTonpAxCbCc2vPLqQrwgs_Zvi7YtNwc-6uzYvY3o_ZSG2WSUl-5dItw6MEpSX0iWY9Ep-gDEVqsa0YMrLOXzzBRJ2YocaeoSz_GCwp2lsZuslCcKrCydL2PCFeFdBvdHF9-_yyM6hzj9RdwwBMIW64zMu-fhz_05t5L5sWGznGGfrfa1_NQDRUuhdt-gv_6rkKwaZkI84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgvQ5Q7SqtFF_OtEp1bjeTaCkN7pyu1H3HNgvRxpXyR1-AZktbNa42y8dSKM0yXIa0rg6P8dB1HBtuAHC1SyZTzXoMnxV4w92iye0L59FtyCL_DzTYAT4qq-9vP6VjJC8jhWDqww5_2jT9T_AgtibVfE8dOg7L69BCuGDjkhYWsORTJdK0n5o2tcKBxQ5JKj9CujtcsU0SUAAPCuAImweaOrb5Ni0_YRKs7189eY4WDX7P_kvIb3OJc2eBCUugQ1T9teTLnu9Tv1IO91IWC6ionbjUJUDgJXPItahpAizfwn24LcAe-bqeJ9nZnM9JIMFTYCDZIFZ3SX16E7oXTUyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=jmzDyOMI-s8BoP9AUrP4gYhHKnH9usAVw9f6qdDmLXC2AThpZFoMLmjddLE5zEr3QdcpsI2iyTHUEdjo27IEoD9lvh_97_OqNREf8dDDmBkYVCii7szCapyh8OfQk3KF3Ywp5G-JvNF9ucnDED9_e4Lcj-4kbRk5iXQ_Y6IXr_tOG-9X9O1vFTWjCF2XTw7vTGSZufyJS1WQMthRe8L5T0oOvgaVs-oh7QOpWpn7obNzseRlM3JTI0K2RKW6EO0MUYob__WGw6mON8SM4wHDXCZJqDPuqAI0Y9ly9I8hx1JMdJX_wOlka72lYpkNZwI1hc4Dq1-yfWwU-kq26wRH-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=jmzDyOMI-s8BoP9AUrP4gYhHKnH9usAVw9f6qdDmLXC2AThpZFoMLmjddLE5zEr3QdcpsI2iyTHUEdjo27IEoD9lvh_97_OqNREf8dDDmBkYVCii7szCapyh8OfQk3KF3Ywp5G-JvNF9ucnDED9_e4Lcj-4kbRk5iXQ_Y6IXr_tOG-9X9O1vFTWjCF2XTw7vTGSZufyJS1WQMthRe8L5T0oOvgaVs-oh7QOpWpn7obNzseRlM3JTI0K2RKW6EO0MUYob__WGw6mON8SM4wHDXCZJqDPuqAI0Y9ly9I8hx1JMdJX_wOlka72lYpkNZwI1hc4Dq1-yfWwU-kq26wRH-Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=BNhZ3VQa0x18eoanoH47HmtEkrvqhgRDMSZGNufLoxNnFJprPiWiXKOEfabOyFtJqmLNHiPzF_-Aidh0MV6ZJ9xMIkWvi76gEJlAsGeBA7TTJZvFcdk2O4Z9TrnjRLcP0iBAbNkIOQFa5Cq8lEvdlntXWXdTSULDRFMIfixA6_6P6o3WDZfXTeuVXxcG7RD3TuAmyVQ8WrHat9Q17oGXDV83QHsPnuIPKYCctHEpqsQdOb7obMvO622ib-LmujbCqOZRc9_0VL3TKV9ELJs7KOyZKrJqekAEPB_uwM1HjhUkmwMO-Mfnpie3nNaElar-R2RxXleA2WUr0GvToNFfvXp3rY2rPMLQ9S61CvHlrzo3UzbBwOGeMgFoa51zt4kM3CrZd1O3gFZWeY6IO4yD_oo--s5EZ8_zqjyDF9HQYj-ooMGwQKXR-dUPYsemHEWE3Ms9el8Mmade9H7gomoRRWG67A1IkYxSer0LNdSV1Mbbt4VJ-5sYIT2NaRm6ohbWh98OvseUy6wffP_u9uSvaNajfIL3IznIN4ohjUGhRGT-rO7a3yb7UPhbzvQRI3J80avYCDy7k8iTpVQNEoHklHvAZfA7rVuWPGnx1nDyPL9R6uq9ZqlnZ--UUt5UrsHmskqcfcd5sKjLF7FS5DeOQ6bYQaMZez2IKIDTShlvneQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=BNhZ3VQa0x18eoanoH47HmtEkrvqhgRDMSZGNufLoxNnFJprPiWiXKOEfabOyFtJqmLNHiPzF_-Aidh0MV6ZJ9xMIkWvi76gEJlAsGeBA7TTJZvFcdk2O4Z9TrnjRLcP0iBAbNkIOQFa5Cq8lEvdlntXWXdTSULDRFMIfixA6_6P6o3WDZfXTeuVXxcG7RD3TuAmyVQ8WrHat9Q17oGXDV83QHsPnuIPKYCctHEpqsQdOb7obMvO622ib-LmujbCqOZRc9_0VL3TKV9ELJs7KOyZKrJqekAEPB_uwM1HjhUkmwMO-Mfnpie3nNaElar-R2RxXleA2WUr0GvToNFfvXp3rY2rPMLQ9S61CvHlrzo3UzbBwOGeMgFoa51zt4kM3CrZd1O3gFZWeY6IO4yD_oo--s5EZ8_zqjyDF9HQYj-ooMGwQKXR-dUPYsemHEWE3Ms9el8Mmade9H7gomoRRWG67A1IkYxSer0LNdSV1Mbbt4VJ-5sYIT2NaRm6ohbWh98OvseUy6wffP_u9uSvaNajfIL3IznIN4ohjUGhRGT-rO7a3yb7UPhbzvQRI3J80avYCDy7k8iTpVQNEoHklHvAZfA7rVuWPGnx1nDyPL9R6uq9ZqlnZ--UUt5UrsHmskqcfcd5sKjLF7FS5DeOQ6bYQaMZez2IKIDTShlvneQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=lEub9YLR8lrLSEHlZEP5n_IRCAcFK9WQWmppMRTA3-qmOAlbhCiIcTChcfnavU_Tz9iuhtZQwREhf1TUV-S9Uxx_7KjB3nvLC6rxmyAfc4aVFKg2_jfX2oHvqKqu27_AGI_HpOD55BXHAEFMH026NwulkWy0p9yAucvUGKZl8Jffs4DLHNLaZS0jRR2-Wek0WgQgJiSl3YciZcYquxZAAb2c2E4l9TfaTrnf34YB5wq0QNrHkAlDSvu1WceYl6DNj3PRcEznJOfQGOOKqn2pUDeH8WhOkP_aLN6djY0MznxJzuTt7uSVVPGUdp_7bzRCrhOPXkdw5g3GyXNqlBnEzIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=lEub9YLR8lrLSEHlZEP5n_IRCAcFK9WQWmppMRTA3-qmOAlbhCiIcTChcfnavU_Tz9iuhtZQwREhf1TUV-S9Uxx_7KjB3nvLC6rxmyAfc4aVFKg2_jfX2oHvqKqu27_AGI_HpOD55BXHAEFMH026NwulkWy0p9yAucvUGKZl8Jffs4DLHNLaZS0jRR2-Wek0WgQgJiSl3YciZcYquxZAAb2c2E4l9TfaTrnf34YB5wq0QNrHkAlDSvu1WceYl6DNj3PRcEznJOfQGOOKqn2pUDeH8WhOkP_aLN6djY0MznxJzuTt7uSVVPGUdp_7bzRCrhOPXkdw5g3GyXNqlBnEzIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KsgCfJ6Zj4hNegwGma1PnHKrIQEoSJBPxlK0P1WNR6ZPBsp7LrCJbOeh431s_CDjJjZMH9spgFXg0X1hj4hDzNSWQHlLn10GiSn-4guLg-cp6Xgrp_FnsybrxO0T86oXy-sGDw2fJR2CmjEd9_65ypXLftdKzFKS3no2z5wgUvSucXz7FTGml5n4HLTbdqXy0sTS5xHQLnk_torbDXvS3hFZUyEMEMFb-on6G-ek4r9pHp355UnShoSC_baZzh14Hw78P9nvBL-L1OG0-7ugo0oEywzkuaBAVBbBIn8sdd0DuFrXuk7vi_0lh7vObQpEToezDDAWhJaDbRthuMk8rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmRQIYU94pVEPwkKLqSDd-xFXzT6JBOZfW4yYxG2JNnYtjbs1Uiy2ziAMKW5D_A2ldK5kiOUfFp1gagy1oRON1uOyY3qqyZO7Oxkgoca5DDkX2e_pOjHyJ_zeFBvyQQwSJqhejv9OJvR_1ct4Hbch1T6qBBN6Muc_py9-_UMeFslEEjZAFzDJ7vvgIVFscDWXFKIxF0X-Pg-IK-p9MuFQhRXlGITGDH9w7uu0MRII2nuEAZsf2XGJdKtHTWIT7ldgUxCVvbSOZKP7JtwO7kwjAP8ScJkdC4j6IG_DlLi4CqoEpJ6pAqM9P3-RalSbnC37dXjeVdrhzQdcPO483TmLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2cUHvg99G5gkVKEoCO6grgpNPqiJiK-oJZ3IsBQQA_2T4yCBjUSuT6IKTGkAeT5T8ZyR6413DUGB_qsO1e7LaIH16g2Y78LHMqIauijuztWhQ_G0I60MnKzTvrhUf108vKqKFsgPWX6Wmw3aMj9-jpipIIk6v8yLhlZhGZZp9P1WFgbodzWojGeZpoU_yzUJ92LihYO7uOY2uptWzV8meA8ggl4Z7rwZUZP7v9TbvbL3mH0hn8C-pfU1tAlOorRUk-M6hQDpBK6iUIaP0K0MaQogQbG13hdjSJ59PNmt2_JPe64o-XN5WMF4mxa9OesBI0yFNgcwMYr1ECoI5lKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGt4VdUsmbZCmTOs4oZEYrT1Im2B_BQs7-dkKdFvk2aDbYtkJvdZMcfEZLZj_xVAjXct27U8T5WkM-JjQmYTMneAvFv2gyIXIe646cHEg2ZtXhGW7FJdIix7WejJxYkTm62yQDYvDWN6BBiywcZNEAHlh21qinrdJZXqMp3Kpliw6rn6UL2e3LbkcqSP-BulKCoYz1F-VzmqCaYJdXZn4dFE--ZDOfx19kVSvQ9VFNHDAyVnwBHL_k5PN5pOd2pUN5qMDkJpq9-EfYj85j77LrwC2bNZ8YDNTBHl9aYBZgW9DYLBXa9mj3wLuQieV9rSJ2CFS71cSNz7AGiFBM8RQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
