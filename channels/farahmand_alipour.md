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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 16:31:23</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5673" target="_blank">📅 12:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5672">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جمهوری اسلامی سالی حدود یک میلیارد دلار به حزب‌الله پول میده،  در حالی که  بودجه استان خوزستان  امسال  ۱۴۲ میلیون دلار  بودجه استان سیستان و بلوچستان  ۱۲۶ میلیون دلار  و بودجه آذربایجان شرقی  ۸۴ میلیون دلاره.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/5672" target="_blank">📅 12:46 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farahmand_alipour/5671" target="_blank">📅 12:42 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5670" target="_blank">📅 11:24 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5669" target="_blank">📅 11:07 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5668" target="_blank">📅 10:32 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5667" target="_blank">📅 10:30 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5664" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5663" target="_blank">📅 09:51 · 31 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5661" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5660">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsdBrk39VUkaHgUUDD1WoOmMQmDMorD3dhmQvAO7we9CoD6EHJ8_PsYOX_BGSktm-NENl7KEAXE616KH2zV5sCqbG36qPbbQ-xmkgpvTf99pllSTU9IPdA0_IMSxk1qG6Xqlt8CW38BZ02J-SBY4PnWVk0fv-Bj3mVVWrVf0bhCro15YMeXEGtQK0iG-HN8ww2hE3GAqONoMk5CqEU8JXbhAMOeFuD6BWgw45hNNWLTgBu2GNYpDPj4KIK9kXC2PN5wdOLzXxxVSGGySY0vz7gyocrGk-pVFptS6iZecRscGil-JSr1MYurFryI-32rCSFuTSgayzzviY_LJBOsNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5660" target="_blank">📅 23:07 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5659" target="_blank">📅 22:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5658">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhH5Q_Yl0mlHfnJP_mSCe_yUdtDdPCNVt14k5vHA6bxiDZk1hFRH_l5RX4Yn3TVVLwp0556ERIZHUEL-PbKdP-TiLnj0y18JM-1W6QIbGhAodZmbZ7fNohqfiukceq11DjLSy-DA0sC7_dkMfB_vRU9QL266D0IJ4Wn9vI4p-3mPs8RrUtgWziJSN5BwSlcpZrfyRXrturavu4j2CglYgvbhlcrz9tLDEgXqKivTuhS6LIf7MB62e8tLaujhQmEcAacwAaAZ9s_ZpeloTxoGz7qtOqF2HLFB7BGdNteP4ATjGB-EAGTRNDSzEh7ZuV6_S-MNRhhnxnIRDG4QkqzRcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل حملات را متوقف کرد
ولی اعلام کرد از مناطق تحت کنترلش در جنوب  لبنان بیرون نخواهد رفت.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5658" target="_blank">📅 18:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5657">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyPY5xgDAbZiaIUqY_p8zj4eNco4l0Ld9WKsogZz2ntVSbwyMFXdpwNXK_sgp_F473RNbyC9yrGj6IcN3UEoraSIf0SrE7suFHk6Tg6SbU3OAbmF0mfzVKqSSVIzN00EUjgOCZnt1h2uDbdiOnQaXWBfWqSn6h2t0F0HS7dYTQ1denw97MM-kJ7aHcHeuOcEmoOhzO22zmZrmFy05vMuEXfb0BePcGJoJmxCkjWa85hocWw0QwJq1uhWJK3cWnSPuRf_5mYjNRuMrBE7QOOFTCgXH_6cJoRcT8kZpKkgNwgkjI8DbE4NSYCz_ZpFRD-e83BSaoW5_QzsJK7g1tviFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در واکنش به جمهوری اسلامی :
فرماندهی مرکزی آمریکا، سنتکام،   بسته‌شدن تنگه هرمز را رد کرد.
سنتکام : تا الان ۵۵ کشتی تجاری با محموله‌ای معادل ۱۷ میلیون بشکه نفت از تنگه عبور کرده‌اند و نیروی دریایی آمریکا هم در منطقه حضور دارد تا مطمئن شود این مسیر همچنان باز می‌ماند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5657" target="_blank">📅 18:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5656">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">جی‌دی ونس در خصوص لبنان:
من فقط می‌خوام به مسیحیان لبنان بگم: ایمان‌تون به عیسی مسیح رو حفظ کنید و بدونید که در دولت ایالات متحده دوستان خوب زیادی دارید که برای برقراری صلح در منطقه تلاش می‌کنن.
مشکل اساسی مسیحیان لبنان، یا دلیل خشونتی که باهاش روبه‌رو هستن، اینه که حزب‌الله، به‌عنوان یک سازمان تروریستی، عملاً در لبنان مستقر شده و اونجا رو پایگاه خودش کرده. گاهی از خاک لبنان به اسرائیل حمله می‌کنه و طبیعتاً اسرائیل هم در دفاع از خودش پاسخ می‌ده. به همین دلیل، یک درگیری دائمی و فرسایشی ادامه پیدا می‌کنه</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5656" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5655">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
جمهوری اسلامی در حمایت از تروریست‌های حزب‌الله لبنان، تنگه هرمز را بست.
اینها دیگه راه گردنه گیری و گروگانگیری رو یاد گرفتن.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5655" target="_blank">📅 16:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5654">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11b10561df.mp4?token=UQb-7N-R2h0Q5I5z_3Xo6Sw31PQIAX40N-HUlRKlt-hXmpXBjWi7qDmbChVVaS5kaMEku0MdSUKY-eEF5-wmFW0X1cMdsThFhHnXbftCBI7pnPPhFfQMV6yYPpWcCm1HgDlJY2hW6j01ZOyMDV-pTax6PwwgsA_3wJehRvoeR24lbckUkBrt8PqyLkF-YxPf-XWeAAUfiRtzjnWf2ZIoHsQc9oW_BByWquUaQLD7wKRbqfEUYWW4ZZHrhyQv8uW_YFMSz7kkpoaGz5bPt9eMQOzQdwLMeuYAqdx408IBH12pmUvH3YKLZBGHVmspoAX3bt1E_8Ulnp9_LYdetLYVuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11b10561df.mp4?token=UQb-7N-R2h0Q5I5z_3Xo6Sw31PQIAX40N-HUlRKlt-hXmpXBjWi7qDmbChVVaS5kaMEku0MdSUKY-eEF5-wmFW0X1cMdsThFhHnXbftCBI7pnPPhFfQMV6yYPpWcCm1HgDlJY2hW6j01ZOyMDV-pTax6PwwgsA_3wJehRvoeR24lbckUkBrt8PqyLkF-YxPf-XWeAAUfiRtzjnWf2ZIoHsQc9oW_BByWquUaQLD7wKRbqfEUYWW4ZZHrhyQv8uW_YFMSz7kkpoaGz5bPt9eMQOzQdwLMeuYAqdx408IBH12pmUvH3YKLZBGHVmspoAX3bt1E_8Ulnp9_LYdetLYVuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوه ا‌وه خیلی دارند بدجور میزنن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5654" target="_blank">📅 16:13 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5653" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5652" target="_blank">📅 15:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5651">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBqt_H7gHVLmfgWo4W6RFhteEMCHEA1Vud2G1_0vwwABDVswPr1J4ir20FMuJzKMrzYIi0aUCMTzdp6yo1LUx6qAkieem_GQ06w2w5xeLPJGSxVNO9gtEvEGgpSLo4pdJBrdAWyN0lNYpI28U9mZQSh4BsY5JfHKeIk7gz7hTXIG6kF6ddIo1ntuXU7masMk04Ze85pzLu9a0xUVeWib-ow7qNxxyYVDFYWc4qfc55lTp1QTdwefFq3bQavrIGR8ui_0wygyEQFLw9FaFa1hvsqhXU5LAInMyUbk4SPPSj00aW8yucguVl3wi85xQzc4DpNLIpEaKKiGob2EtZTwcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس
قاب‌هایی جمع‌آوری کرده از جنوب لبنان
گفته بودید یک معادله تازه ایجاد کردید!
همون موقع که پتروشیمی ماهشهر رو هم قربانی کردید!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5651" target="_blank">📅 15:11 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5650" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5649" target="_blank">📅 14:29 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5648" target="_blank">📅 10:58 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5646" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5644">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdtrRfQnzrSLnVowz0S8wUcFVpysO-bLH1I67Yi6Fqf6PRNtXv3k5N7b6PFK_6I89A3P11S-y7dUGU6BDZMV1B6u6nz7O1vPcoBewtZu3VO9A9XwsYp6NxyY68Q_OnZo1qVw0Te9IoK2nJhTjj4JN-Mgnejy1KYD1I07MawlP7yfGLvvfV79F7a8oamW_6GaQ__OD0tSvM2DSaZWQHsdekGpoF7NlNbdgqzqE9Ivw8aMmLby8W3s6ijXNWCWfd93rqtGc9Qsi_TlKyiOtDCBps-boA-fu9KpAjShUvNbos-LKuJlDIesz7xMdXISUfDJ5x_J8FaIXiw-7tQLC9485w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=XO7JbC9J3-smSBRSg21dcZXS5gzy7oe5Nwccq3ypkgPBIHJZSoFHScyzqwqlvbxnGsahO5vHn8H7MOjWp5JspxQGSYKaQbYiIBwjWHxYrqmlX3Z0new8In72pFHUtIUlKELXfZ1LKRZ13hqDFHNfJC5TWztpmux983EvoopEXaiOCGZxmq9MqJY_pufxBye1ReLWJZLr4se5HF4irGF-QewWohJDnysVfon7R3N3w2b4QpFQRkcA08LSVGlHMKvu1w9n3cQL9snVOPU0Mqx3M9K8OMk33q2y7cL4Tr23YJwUOtotG7cZWs_7qESX_nyq9LnbBTW5nN_AmOd7rfz1gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e75af7dcb.mp4?token=XO7JbC9J3-smSBRSg21dcZXS5gzy7oe5Nwccq3ypkgPBIHJZSoFHScyzqwqlvbxnGsahO5vHn8H7MOjWp5JspxQGSYKaQbYiIBwjWHxYrqmlX3Z0new8In72pFHUtIUlKELXfZ1LKRZ13hqDFHNfJC5TWztpmux983EvoopEXaiOCGZxmq9MqJY_pufxBye1ReLWJZLr4se5HF4irGF-QewWohJDnysVfon7R3N3w2b4QpFQRkcA08LSVGlHMKvu1w9n3cQL9snVOPU0Mqx3M9K8OMk33q2y7cL4Tr23YJwUOtotG7cZWs_7qESX_nyq9LnbBTW5nN_AmOd7rfz1gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صبح در جنوب لبنان
و بند اول پیش شرط جمهوری اسلامی</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5644" target="_blank">📅 09:52 · 30 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5643" target="_blank">📅 07:48 · 30 Khordad 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hJ9Jc4fdE6Dr7h1UOClvcH2D54Mam-mMeAS_aoxPSXpCs-fsk5ORPvdwKvlxh37h2cXXCe37JSpBwKZaVlTtJ0k10f_P1EtIWbYZS5gxZTshWVlV76r2DVvKkHRPGRWDzyEKtxSKO5-ja6dgMqedZTu8vZ_s3qwNyE9B6R_xDhGPp9aplUKpmwkU7FLcXqXB0VLeVHCYjVfyd_sdvhBJyNn4j7aoCN-MnfuH2Ybf2tTGZNmmZ5ZC4AG9WJMC4FeLvRKK-p1kPGvXJDgnuPUyeS7Mluyhu67YuUdPBXnXb9SWs0tNlYA3z3emlKc-jbU9C2NBpKaY60lj3doNIeEmGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxqHPNP2P8iA3X-PcgAOXPr4Uyl4-tQgAvi_ASpz_PVXv5K7eAH2GjZuMcFgDGjxwIZGeyo-JG2xEpPLIdOXGOWJXFT6TT4itFAscq1HDbgxgslurjQaYQ5coyA9QqFd3UjbLexjsgzB1KgGOqAePOq5n4IzJbjAU3uWwtV0iY7GVSYWQueAcyZt-po_BFcHu2Nu8f6zkdoYzWhYrhpga2K5me3ONsz1TRiiZrrbJfhCkSTtxd1_xtImtxjWANDz4k8h5ZtSHpPxIijQxk_zmm0SKt7SZB6G7qfTGDMIRFC_nomsTkKeoDv4-H2ADr-tdZp6Spv132YWCfHGFrDAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=jL4cIatn8IpBA6mw3hnJw91NQu8yf1Ov_Fjc8UOtQQE9n0Ef4WdzpF_rw8Mk8cvm2HDgA-zp8GdZONYeUTL3KXcHX_z0Zpa0zGn_ry-5ZEAVe2MzYEA9wpjB0zKacbC5U7I_i6q_pvP6K65HlZQVUPY092-n4NNGLVD1qvOT-yj5B8BnjsmEW1rF_gmVmI5r2_AVWgMX8COgGoy_7wjWLiTTvNGf0NO79bIzj5AHjVEIRzfD9K0pL9Wa59icT0uiYouE6PVj1Ap0tp975XKk90N1gEo6b3ftONlaTHqMtFE-wUV4AD-LQmqd3wUtqdqreaXGv6KZWRwVJtZlJh1jew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=jL4cIatn8IpBA6mw3hnJw91NQu8yf1Ov_Fjc8UOtQQE9n0Ef4WdzpF_rw8Mk8cvm2HDgA-zp8GdZONYeUTL3KXcHX_z0Zpa0zGn_ry-5ZEAVe2MzYEA9wpjB0zKacbC5U7I_i6q_pvP6K65HlZQVUPY092-n4NNGLVD1qvOT-yj5B8BnjsmEW1rF_gmVmI5r2_AVWgMX8COgGoy_7wjWLiTTvNGf0NO79bIzj5AHjVEIRzfD9K0pL9Wa59icT0uiYouE6PVj1Ap0tp975XKk90N1gEo6b3ftONlaTHqMtFE-wUV4AD-LQmqd3wUtqdqreaXGv6KZWRwVJtZlJh1jew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8vcOihzH_ghWBypNgFag5BpkgBU80UU3PAa67a7NdhWPTQ-FR4fbJ_UzT7tVVzOpu4WSb1njM4dISo0ioGSDGOGjT4920757BUCLYrp08EEERoxaOkW_kNYGtOXlc8LZXn48tS5BDci48uS8wZUsY1byh1Vl1zsLBwwBIDaaJ380xrfIgQ_b6SrDVpQ2lhrv7pueqVQxXnKkD9hyewprLoxKF6x97GI4OYDZf5xVJoVsD0ipcX9GBtAEOQHBq6BUqI9q8Zl34QU5CqAoLy_YZgdXAN62uptAGnoIm2ajygSnjuJzOY57bBt7lfLgiE6mSn7uKEE2owcgq5ZOPXtZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO771Za7sgBgFPqz_Bn_UZ_c83cBMFeCOIltXqyaBDnPYv7zUFZCtD6TzE76qMVteI9WpyGRrsUaHmudJNy7AZgJP8FDlkMFoN3tIV3ah9BroTAM2YvmNW5N6mLSf5kKpKoWVz-T5xei8ihXbCCzGFwgSswHB0TQvO-sL00tLpk4GZahOrH5iqtLL3kmZ6X8QoBAKDD_mC0OfKBAYfbgCAdsNaxZ4euOeHrViK7Dq6jQkUnvvZxnVdCdLcNJgcG2TTgqEatTauCG45T08RcGJewDvBGqnxKGaLU1at6xpIVXv_D-hNx8Xni_wq-hnCulJjPxtOqRCBhhAWBfS7c3Fg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foaEkFCiB2mcXVY-oOeNZMhMthp5qjXKPYFVjLMkgJ3VEEfXYLWVEd5I0gDzylxKC6dKUoBJjo3NqJG3KyI3dafaQtqCu18zp1bUQy6-76gyiLOHTlBPTpm4RO7hsJVbGVzGAnX78fHG_mDmDM9DFQPaLdY9RgJSLySOXkg74USpSRODHNVxSVH3ddKYtMKDdEz8_D56S0IUFXRnvuLK61tnalTX5FGxn8m0DDT4iBcI5_BSBf89aucXvS5rpQgnGNk8H4yqMK6L-nhcrqgtidnqfs8StzpDcESlXO95O6j8k90hOBKRdL7hcThbXxniWjUTYF4O9lDFW2c_A4m6wg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=Bf8gBonHw2GJ46YsHvGQmUZt5NQ1tzE0-r5mrjRCiMFkDpReVYcJzFjBcWHnsAFU1fX66u-4leIeeawSshXPh6pBkjrrYA1na6rC1xUocn6Z6G9NTfSKpy1BEtz5-OCtghHTylqp7TBspw4jtOpGTbhVPgW-b5BDiEWzTTnL0PrNeQZls4So4F3JkYrV_i1NH3IzTqrYOYrDeYuKRue2DlmLjsV67pYKXMta4WUj2dN4hUuEkUj86Th2YnyEPhQCDtAtmGOt5XQYdIE1sGiet_Tf_Ax7Crph6kr-kPc44QwimlGF03I9APtJaQdhftsfPIw-ROTOruxSXNGh7yhyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=Bf8gBonHw2GJ46YsHvGQmUZt5NQ1tzE0-r5mrjRCiMFkDpReVYcJzFjBcWHnsAFU1fX66u-4leIeeawSshXPh6pBkjrrYA1na6rC1xUocn6Z6G9NTfSKpy1BEtz5-OCtghHTylqp7TBspw4jtOpGTbhVPgW-b5BDiEWzTTnL0PrNeQZls4So4F3JkYrV_i1NH3IzTqrYOYrDeYuKRue2DlmLjsV67pYKXMta4WUj2dN4hUuEkUj86Th2YnyEPhQCDtAtmGOt5XQYdIE1sGiet_Tf_Ax7Crph6kr-kPc44QwimlGF03I9APtJaQdhftsfPIw-ROTOruxSXNGh7yhyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESqUSU4up7EcD5bupzubeWIcpxGZW7qej_uprlKK2DvcvW7eRR2ub7znAAF_pbtKkl2X6YnGW-1BNQTHe6ai4Od6W_IHcHGGwTg7_fRYgMyza8EU0q93-uCIjtIzQNAb3wk37_xkO5I9fQuJXctxt2ohPFvD4tNbmo2A0OEJ68weTkyI38hRNMPt2N-oi138hgAzgfDlleGxWXQ8nSh6YYa98a8ouwlBMY1X-Tmg6oGsyur11NnbFJFg7Xgz-6_8emJteSicmxYh1JITZjbrRy9sACdMX40uUWKFLNLu6q8TTbVlNS-OwqkAOquBkvJgsJKBQufPNyOKGIFJtOZw6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLLcvJ-qZ-PkfKOHzre9TkhbWQ2suy5-Jt-iI4FA_bEuxeXCTKoP60batm6J5VGCR5BYhRC7gKW6aiaB2zp3GUn65tF_okb2F2wBLo2x1kslDmk1uH7_uNxoDovc-ypHkEfVyt4p255WWyxKRekdMdh-SyMgWD3p5qgkjxWyxiYF5rmv6FRTDa3Xde9cGN2cb3cjdKAzGKSlS-uf6lbN0UcghMb-QYyAzw_v-7TSgA9O3j9tciE46PKUaLc3dv-b7TAkOG2DG6Y7tREWSqFs7mT3_FQiD4c6dW-Acsv1yTuMeoJhUvph1sYevi6qLlCsALbqrelYMRAdyjlJU2QnZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJZpLrcNlcVtNP1JntzQjAceRqO_V__kBCesGessuYoCZBsh_yGH1ivDxxmPECa9tT1dP_VFRhX4tl_YBy7Mlzeo-lpBmWhasB8BgmpBxkv4iJiLlLwZsltmPD14QNUjl8Xo_Jhy7x6JMEg5SwwC8A939OFWQgEwRLA6IS4mh1Vu6IAKPlNb_6x8HjDPuVxLGBmd2yS0wu6TXLClNP-HGD_HPidoH6zN5n0Kwps9FRjRbR0xnEjZDu1DeX9yUm2YJS5bab6PfENcbVoHewgT6UYttXZWoIt5sIQs6055tGyPxaoQuLjymdBnVlplY439OC0L2kyrqaF2eoXuNuunWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgRX6IeUYrjo4UXJ1pfrksfKEEm2syxBMgI50useGE3Dr7PJeBcmaWN0sEZYCb7KT8wCjSTMDeVOA11e5xE4X3mFzCwvWlncye6BFD0MO8bHmhXaVIuK1n47pZ6lQYFuZ61vILzWlb6FgGzf4qP4yjGzX8UhC2ADFnHbI1A_i7WLWqxLhTD-hF-Ga78DhrBy7d_yNXPaRXaDoNTPHxRvPntUiTG4IBX14GGclKF5M2DEq8H18qKiSV0KyaMPTthAo0gaUiJYquPdSvdmunGSRH_IqlwjnsBb8ia99QQVHxrUhtTLnuQs8IJ9fUuaMK8TdhdW52p_b1FWv2Vgg-5y4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=XYsuWNSbziZ4aLq_rsegScjxgpGyjhSMDii9mNyLc3BcO5yhOjGi6SLB2y0iBCm6PAqncnPoConQr_3hf66AP3tQT-gfkpJhrlcUxTF_Tv0XOgqBSCocEZk3runIH0Vzf4HGeZTmIFeUVI0WbhhT6T_rUOz0f49kmnejY_hPDPtrNsQqwpYOYNLGjGAWJS93P47mUcQXIMh3T2gqxsU1nqPf-2sAaSiJ6tbqqaIGYuNdLvdh1l-NjFMXUokFEQjbUCLKHGCTISRF1MMUjuyMJsn140EshpJH1qQLn9o4lziCAnwjMdOj3b-kdq8bslLfNTcD_0xjsokAa7an-DCY3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=XYsuWNSbziZ4aLq_rsegScjxgpGyjhSMDii9mNyLc3BcO5yhOjGi6SLB2y0iBCm6PAqncnPoConQr_3hf66AP3tQT-gfkpJhrlcUxTF_Tv0XOgqBSCocEZk3runIH0Vzf4HGeZTmIFeUVI0WbhhT6T_rUOz0f49kmnejY_hPDPtrNsQqwpYOYNLGjGAWJS93P47mUcQXIMh3T2gqxsU1nqPf-2sAaSiJ6tbqqaIGYuNdLvdh1l-NjFMXUokFEQjbUCLKHGCTISRF1MMUjuyMJsn140EshpJH1qQLn9o4lziCAnwjMdOj3b-kdq8bslLfNTcD_0xjsokAa7an-DCY3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKeIy07Ax0i0kadWPCjzURig7H0Ia01HKIfaBGQ9pBuK7lZiy3qdzktqtSDjfrcpONzaD1kSFsp86ltnDo-JObgdw0LBW6t7CePyHOggj09tH-PssjkaDpVj_F3-Ha1-7NJyUz7mELSOdm6EOIORbraoW6NxDLtLQ5tk5BhpNuQCy26gNePjUmZ21psTgQUoL4_g_fAAEvrJk2I7Zeif1yqCU_eFvOVn7dUYdCP1vyDp5BxGOrySWGFVCQ6ka5w-9zRNXup7VbDx7R_H3e3FiDTiuDw7lQEIxDuH8RSUtnEK-ly9cxfIdByMoN-HEWMGmHDh2yIcer5nNYb5ENnorA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=jwgkyVlU56IFG1lo0cA6DiQ9rLs0rtRrgH_iuN70aS6vKERul-TTGKkkeZjGXQu9DezNXW-C5RUbJoV6A0UQ2ArjKwc9t_oqs3ztRr7p3foPoMd3-wI1BQyGqmL34Uj6rE3vSP-fAvKsqy64_Xq7I3OwkoF6x7iBGCjRj0VGCnH5MMoQFOATyN2vCGr848NvQ9kJuGFPizFRm1JNKCEkufFO49W_kGMfqmuT-cSUXaU3iIcDm7XP16GGHKH25xk6f41j8QpyN7wHuKOC8XQbCtd-aUfCrmaNUYzWKuGzh8MEjVXoIk7mtSshqrvYGQs4RZ_NSNGj11ZiX_4vN0sWtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=jwgkyVlU56IFG1lo0cA6DiQ9rLs0rtRrgH_iuN70aS6vKERul-TTGKkkeZjGXQu9DezNXW-C5RUbJoV6A0UQ2ArjKwc9t_oqs3ztRr7p3foPoMd3-wI1BQyGqmL34Uj6rE3vSP-fAvKsqy64_Xq7I3OwkoF6x7iBGCjRj0VGCnH5MMoQFOATyN2vCGr848NvQ9kJuGFPizFRm1JNKCEkufFO49W_kGMfqmuT-cSUXaU3iIcDm7XP16GGHKH25xk6f41j8QpyN7wHuKOC8XQbCtd-aUfCrmaNUYzWKuGzh8MEjVXoIk7mtSshqrvYGQs4RZ_NSNGj11ZiX_4vN0sWtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnmGLyMRYfT4xsNDcpF4RdtSws6bUBDaF7fTieSz5Cx5ZpG743cTtIRvk9VSgRNq2XfQ88V0BQn37mFYqNMIVlNQ-DL2eeFNGMXURAWuX5L2PyiXi4_SaFR0OLsxIkl7SWaa31Arg6OGy0qvgaK6jNKNifI0XEieS_eTj5_GaYZcmdDF56-8vrxjXoPooPCszY6KcPL4LZAmNbSImGfdsW6rhziverBnAXKi-vNrJRmOsFmwr2CjezBdHnQVEjlAusLSIlt2DGEiU9wok8g2qL1NZ-AzcekF77HveZm4oCmt31A27TptlGi2IOyRkVjfGojuvF-KxnF_R-au0YxieA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=dxgXo7wxouUWsQho87oyFoLINNGvIXVFzbiBskhmyBx0-_KY_9B-lt2qlf1qfh5DHvJjIjbE6w45GEaISEi0uPcZgnTUaCg__HUtvG1K-_TJW0Y5LLbfcaSOHXaJalNcMpjVu2Bh4hHDNfuurIhpF1DaCESBzA0AFbOlaUkdYWNQi69QnK3zBpx6Qe4o8wpkZLIzequ_-fYSnVF3SIC02yEMwaaFlTQ01nvhms06rYyrMb-Dl9AQh-46dE3V6Sa_TQU2ML42orrjmza3uPpJwmKaIi5tqnObm9BoXXUwIb52t8g4q7x4rXF8UZNtpPzOv2sKfLmysIkq93oBNsefNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=dxgXo7wxouUWsQho87oyFoLINNGvIXVFzbiBskhmyBx0-_KY_9B-lt2qlf1qfh5DHvJjIjbE6w45GEaISEi0uPcZgnTUaCg__HUtvG1K-_TJW0Y5LLbfcaSOHXaJalNcMpjVu2Bh4hHDNfuurIhpF1DaCESBzA0AFbOlaUkdYWNQi69QnK3zBpx6Qe4o8wpkZLIzequ_-fYSnVF3SIC02yEMwaaFlTQ01nvhms06rYyrMb-Dl9AQh-46dE3V6Sa_TQU2ML42orrjmza3uPpJwmKaIi5tqnObm9BoXXUwIb52t8g4q7x4rXF8UZNtpPzOv2sKfLmysIkq93oBNsefNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=HO1jWIkp3DEF8oTD0M9iFLHz4qP6DjG205GsVx8m-fzXXw78bZxRTzL0tS4Us04FPUI3KVZhqGnZK5C38wcoVpybL9P9q42kVzGwoIsImC-o_SPCbs_9DEfWauM36qdlWJgBet01SBSD63wd_fr2oEvidC6rVpImVJOegBBD8f7CKH603rjiaLqb8R0EftQg84Yfr-_9QhPqKopFo7hEwcIyB1rc3efpgwyR0cJWV334yFOxJfDdOZFX3rWdTuvdrdtyanfAhLa2oFBRZXvWk_epglOvpD9WtxWE0N1O8pfY86Xjuub8GENqyn-a4pPfQEhiaafBlthAvU6yEfieXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=HO1jWIkp3DEF8oTD0M9iFLHz4qP6DjG205GsVx8m-fzXXw78bZxRTzL0tS4Us04FPUI3KVZhqGnZK5C38wcoVpybL9P9q42kVzGwoIsImC-o_SPCbs_9DEfWauM36qdlWJgBet01SBSD63wd_fr2oEvidC6rVpImVJOegBBD8f7CKH603rjiaLqb8R0EftQg84Yfr-_9QhPqKopFo7hEwcIyB1rc3efpgwyR0cJWV334yFOxJfDdOZFX3rWdTuvdrdtyanfAhLa2oFBRZXvWk_epglOvpD9WtxWE0N1O8pfY86Xjuub8GENqyn-a4pPfQEhiaafBlthAvU6yEfieXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr4wEMixvTotpHIj8iGfBknteVQcefl7zw0fKvzdElU3t24yjf7TTMKQT030B1MSXNlZ3A58UDCeXEn-7fAQfo0SuUoelg7GHTMaTyF4Wj7RliiY_236RBwcTqxdu_SI7Zc9TaAfh-9l4G8ALmBme8gkHE9d0Dy7gg334B8IRVePQcckqwIhKpPaGKd-0GuIfTVvV3XLWMgpJ31Ex1FXOWnYsPult0hpuWwUx8jQ58S2G9Os4_-ThQCk3fnLEmy3wckP2S98j5ookJvGvJYU0EUo8R6eV_jv7ZNSNmgWgbY9aP59J3-DFXvYqXt22KrpnaysRYDRyU53VqQEDKZpkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-uM327sj99-YipwSmT0Pjvlmos7POQcv-hnDkcEYuM7XU-O3Jq2dstl5eZv3jF_jv4HGn5WFuRt7CoRYthvAy9dcegnEM4j_BrQh8Ta7J8FHgalnfrZQuV_Tk5FnFLPcJUa0qb8IF-h7WXEaidwaZ5Mp-a2FoR_77OJ6X5WVrktw4JBgdUH3z-K_WWlF7D4dIOGMLlPIiWgAX_9eJrTXtr6onJ3yXB3rhtcYRxxEXMSh190KZ9T3mbX_FRQN7Hd17jd9awPAezVuCYt7JMhXhL4NDe8JSMb6MnU5okPq3tRfznq7WVCLCYn1GFqLvKgE8s78Rwi8rnFeUYO0bCJ6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYApdTNCsuBYGkRXVgp_afkVPLTtPiDi3qpItkd69Ia1q8mDZ8ENknd6AfCF_5yysmWX4jGRSAKxFLbdiKbM5_RBH3cp8nVuG-wFaBLwKp-6m8MtmBFTQfyLAdFUfe76b3AWufbmpPT36EZSENsvAZxsTG3LpxCHysw0M-k3PqWOC3vfOjVzIV1U7jU12XP7wZbchG1-TTYx-tNxRH6eRWrEuvCuFdKrn-kD-3C8s_ReNBXv1sV2AsBOruM3YSvgLihn7To90MTD-gtbNvrvDmIvF1hXHqalo4a4M93ygSMYPZWJd7imVxsQnt5a2cXrjcQ5pbBg-hp4WLMz9gkcPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCKYd1d5lsemxsbeZf0cVB3MK3M-hRk5ZLtM9d1X9Cf4tQuniqA5lpT8vko4h8qKG8Jj9sNxD6QErqkuyieaj68sUIf74L4EaJe_MbjJIwLw6Mq3vQP6YgCAj8tUyZnUSjQPWgD202l3G88VMlfkkMXeSJsjlVfSvjteV-i0Dc6V_YpnrfkcY3julYusVtIrII6aAExo_BI0exWQrEUBZfA_Ti9QhySVtefOjftFQU_3WAvvFCNUSGnqb4IhctFol2qInob88qIvwq31X7bRJd2h3GlySb0VS7dn-_HU8SiESBO92d1Rp239hoec4VFvni-0s99WcnedGiRRujG5Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=taQo60SGGFynysgu0chy-c7k1bvpuAfIP8AL0vqcfKsbn4Ro0KoDqnCngPloLqUTCJNOSuzPvpDvsRjojxAFyoUnwuN2Ag7y8n0ONgXv2_dBEzjEfmsP_8gFhx_NZBINqJi9c8MiBeC_LPa4R_HrPcZvjzj7ftZafkG9oL4vtgC0Ik1QMKWm3u1atv3yheqHuto_aAvC5BrF49rP_DjTQLusDB4WTGOvpxPFhUcGO51_MouDe2wIeY5AxtQiTqvVsY1icwcCQKHILUoHBx5rx2mzYnCNk5a2c5UUlg2l20RcegkRrBnk5O-BX_Cu7cvoh-pIXjvJRcjb1SROVCOpkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=taQo60SGGFynysgu0chy-c7k1bvpuAfIP8AL0vqcfKsbn4Ro0KoDqnCngPloLqUTCJNOSuzPvpDvsRjojxAFyoUnwuN2Ag7y8n0ONgXv2_dBEzjEfmsP_8gFhx_NZBINqJi9c8MiBeC_LPa4R_HrPcZvjzj7ftZafkG9oL4vtgC0Ik1QMKWm3u1atv3yheqHuto_aAvC5BrF49rP_DjTQLusDB4WTGOvpxPFhUcGO51_MouDe2wIeY5AxtQiTqvVsY1icwcCQKHILUoHBx5rx2mzYnCNk5a2c5UUlg2l20RcegkRrBnk5O-BX_Cu7cvoh-pIXjvJRcjb1SROVCOpkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieBBfsztnMFVupOUhH-N164jbeR2gnam4sj3FbmgAZ6w-LkZUK6iexNgiLz9m5NZA4fWAKaJDbTFahjnWVmKrQUc5T8B-bCxnMbbhMwn4vhEUYskn098wRru1q_lSJLpaQCArYp1EkZg14-T9mDW8zRD6-gCA_HZNMpregYFS1lyN6msnUUP3T7ZmCvhUg6YAm0HgOM5-b7seH0G0NQzWWxsUUKD3ezAmQkTtUZHSXyWT9DgN4QURz2RhF7dQPuyoECf9ycb_weQHzR6TynhYJH2id9GuhDG1v8rjaWOGDO4nfesBFDnSo5v0t-JoUlRhaUPWU6jZghvLlOOcIsF7L5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieBBfsztnMFVupOUhH-N164jbeR2gnam4sj3FbmgAZ6w-LkZUK6iexNgiLz9m5NZA4fWAKaJDbTFahjnWVmKrQUc5T8B-bCxnMbbhMwn4vhEUYskn098wRru1q_lSJLpaQCArYp1EkZg14-T9mDW8zRD6-gCA_HZNMpregYFS1lyN6msnUUP3T7ZmCvhUg6YAm0HgOM5-b7seH0G0NQzWWxsUUKD3ezAmQkTtUZHSXyWT9DgN4QURz2RhF7dQPuyoECf9ycb_weQHzR6TynhYJH2id9GuhDG1v8rjaWOGDO4nfesBFDnSo5v0t-JoUlRhaUPWU6jZghvLlOOcIsF7L5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKOocnLQFThmdCwBUapK25Z_q4tWZHBFREqOHGwQ1lhaM8-e-NVzCpNQFLVgbphk_ovQOrAiWgrzsRODolX5vC2M1V9TlfGucWTMpwl5VH-7fg-RLCY99xohTwCm6syqYBUZAVd3DZfyAed_2Orx7HKtKWuplg1PcVD8uHjFaxpy3PP6JZQ-LiMd6F001cyx-PDJ2eSx4PDZUPdLLINU3jF4SUL1WyGTTo1osBvFQV_aJnE-eN6tj41CP87z6wz2BOnYWk6J26F_rfDnzqcLD1Stigc7lyt8hJOMdUQeLDg3tPZVmuuiiXoVZiXYjXajl00ez5WY0gLz22ZlhtTVfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-EqcFLBDr8V0rzR4WhvmbYKuPSZmdQqKMSBOIqmLeCwT4yr5mMr1nGd3Tuk2d478L-t2A4DEz5Od11I81anye-BFDNodIy2-itYsSrtaN-f4P8c54whZxPt5iC6-nQjgSBTVc_Th4GTdhPXIJFpVgbQqWcYUknlcy6sGYLOqDJA_x1HI5XUJMbeMBg291NlHXWg5745f82A4YIsVGF2CLpJ4C6VdIe7b_KrB_X6SUe8VsE5O9LxERBzgovM-U7PFOgb9R0f8szMF5huH3s2HQcFlmFmGfnP4o_0Du4k9b8Yk5LetaOqP1losw0v42t9i1DKh90OXV4R3lDnZ_a4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MybaUGy2OPd1hi00-klUCScWI7O18L2xQg5FSrbaJhodlD6EtpAOMtrNjjUZR76WyL3O6lYNLz14RLMS1RL4-OmjyHJey5Aakpa391nq5yGCL77Gcu1pYPZE_3f_YJ0HM_X9qrmQSU8TrUGatyf4uU6Yjb5rE1jiSwYyHKyA6JkoWxeM_9xNDn0QF4WwDtHRugdH0bDQ5sXmlbD4OQ1Z0epj_7ACrRS7KSVsl0ltvZbbzfU9yWzc5s_nxj6PEoya-hGg0xw-WecDBkk-MGLeBFBJ9AFXA9LNa20kjhghqObFLeT15FL4UqAfd0n9ffYfNmLxIX7SEFLytRLvp8hxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHkNwVKhsD0kyscS3VZxsb1sa9UtWyZtpMmFeFUQZdX8N6tj0VjOwVoHIv6bxaubPNSfon9x4_lYy1fBc--i0MIatq2TLpv4cmNyKiixbuqi1NqZJKBawotAwYfH1IU74YKBZToXg8K7cKy7MBlQbwPWZap8tlYmtSZqKF8PEz92-SRsU9yoIIVe72uB4VtMOVoAlGAvE9Rv_83mrm6b_LlaDmMlrlyktJqapkcVspbV4kEnwBuFWFxFieoDMh5gV86MsJFqcRY_-Npp7sAmCOeCE07ifIfIp8wVK3Z6naMwCXpA8ajMopf95FVRvu4G8ZtklhaYqIAK0QlhewqjCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNi58cGK5E5Zomd4TtkMu4WTBpa3P2ndtenKmhZo7GRKPOe1pbJZpZ2bSddWxgohxdU_0Al3Y8I4HqAgUk9LVnDwZVDKb65_YyW1rrGKYrv8C4wVxqqBrshoyfWRi8lY_4GqKyi8lwL0U17kvjk0XdYC7fI2yZ6KwwmQCxBPJNZA36ahSSJNe6lD3p4lZecv3NY0wamj-duxVfK7SbSS_sOuqZIGBu4KIgjXV5zvf-ZdNSo-0N99eO0tm8qY72_o1Tq6z0066Qlou7uX-lGkzpwphzTiKQwRMT7-Wf6L_jiTcOUyNqY5ZWyW8GSISausih4wFnYjphlaz66JviRT5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=d0QRsA4CEZ3tq0nTV46cV1u9ReBvwNNQfvErtGV2Mtv6imj3hrB3kWuk6infBdtpzxrHRi75TwX2Gfd03pUjM0-nRUTS1d2wzF4FRAtnBZgluUnwqxU-JHH5pYYhsaWme-OyTkoUCt70LvJsdgkWypCJj22gz16-piXEkty5a53Ml-DKBc2BvwzjwP46QHjiC8uZ_k_-oJc6a340bDt_XrF_H7IDRfOxDXGUSkem421-OI2IMUdPziKZpNzdL3HoLMlKkwjyC97OlHYj8B17iYi-S3suQxjP8Rf8uZBcn4qujd7---54yh2Jz21M2pSaMpwOXVBGSS85VH7RqrLq3brSpejC_HtA3nk-6YyFnw9aAlAPSFwHR6_I0Q7IkT7CEuuAz7HoqGbQzY875M16TDTBdignDOm1WmYRsLNR9aTuYYNZt8g2OEsi7frCwKqK_82b_p-_3kRPmE9tuZGDfsDR3mDZjyrJxUPn2U2q1ruQTQL4ZOduwX5lN7Ub3It2eF6l_tKWuPe-4Te2FyAM0LVXJMkaX7Cjqzcs9JjoTt-0lM02P-O61Q1e583lQ6g_-DcDszSUx4iQzYY8lj0mHgHeKsNuPwax5emZRw0erOll5Xfvx9uYYP45NNwbTVevM5eHf1ful4kCIrkEr9-VPa-NqEUPOlpTy7we_Rziht0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=d0QRsA4CEZ3tq0nTV46cV1u9ReBvwNNQfvErtGV2Mtv6imj3hrB3kWuk6infBdtpzxrHRi75TwX2Gfd03pUjM0-nRUTS1d2wzF4FRAtnBZgluUnwqxU-JHH5pYYhsaWme-OyTkoUCt70LvJsdgkWypCJj22gz16-piXEkty5a53Ml-DKBc2BvwzjwP46QHjiC8uZ_k_-oJc6a340bDt_XrF_H7IDRfOxDXGUSkem421-OI2IMUdPziKZpNzdL3HoLMlKkwjyC97OlHYj8B17iYi-S3suQxjP8Rf8uZBcn4qujd7---54yh2Jz21M2pSaMpwOXVBGSS85VH7RqrLq3brSpejC_HtA3nk-6YyFnw9aAlAPSFwHR6_I0Q7IkT7CEuuAz7HoqGbQzY875M16TDTBdignDOm1WmYRsLNR9aTuYYNZt8g2OEsi7frCwKqK_82b_p-_3kRPmE9tuZGDfsDR3mDZjyrJxUPn2U2q1ruQTQL4ZOduwX5lN7Ub3It2eF6l_tKWuPe-4Te2FyAM0LVXJMkaX7Cjqzcs9JjoTt-0lM02P-O61Q1e583lQ6g_-DcDszSUx4iQzYY8lj0mHgHeKsNuPwax5emZRw0erOll5Xfvx9uYYP45NNwbTVevM5eHf1ful4kCIrkEr9-VPa-NqEUPOlpTy7we_Rziht0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKYykgt-mF4gc1k72l3tGCtg9X6nQCRw30zn7Vx4zMDQY5eg5kmm8PILLur8t4FzL5FQDUcY4mrCWmwMIfMqqG1kvvnbL-44OPbDiYnNgPgVxTOIkqWrDv3pYvASWlfE8LlFHpUcvPbP1LeorkkbrJagnKMoAwwuPWWKLqbym8abdC3OqnbyGsYtQLcORgm9PkxfBmWZ2i-o1Sew7nwVIKHYhQyA38dLigIw0qY4Zw3nTmyN1NuiYElJi_5XEUgf-alFs1sbgSyq4xVnfAK4vAfwIkbMwmi2BcBKiGbwaPuiy7NwBmajdXRF8XBQPCmtFrrfPKmSMGXcJyyPkJmKBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=ebQAbWKoql7ld7WD6YfA4PT8hP9-5OpZRk_hMJMg3j3fz0YKNBDTgIPuboqK_Z64OestAqgq93mh2uDPFT3YBjR1kWDoEfFs356-UqrSyoQMnIXNpO7GbiEtOwshH6PMzmYNGW1EN-ZXiBP-Q_9a-8jq8gwg-wNn28g_7Y2hs04JWWINLMYjPCVtr3l24SfWURnIxN54bl1rigaKFwYLQGDfKTYxD7HeiWk2QfZ3uCRhArg-OELVGPywRY10gG8bHeFkz5oTg3N4RTMEk9s1QAgBt6PSRejuqi00bS5bYN0zjeqRyGC5Fsb68jLWtsjmOCEtyVNm0jhhSISdgWG6zYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=ebQAbWKoql7ld7WD6YfA4PT8hP9-5OpZRk_hMJMg3j3fz0YKNBDTgIPuboqK_Z64OestAqgq93mh2uDPFT3YBjR1kWDoEfFs356-UqrSyoQMnIXNpO7GbiEtOwshH6PMzmYNGW1EN-ZXiBP-Q_9a-8jq8gwg-wNn28g_7Y2hs04JWWINLMYjPCVtr3l24SfWURnIxN54bl1rigaKFwYLQGDfKTYxD7HeiWk2QfZ3uCRhArg-OELVGPywRY10gG8bHeFkz5oTg3N4RTMEk9s1QAgBt6PSRejuqi00bS5bYN0zjeqRyGC5Fsb68jLWtsjmOCEtyVNm0jhhSISdgWG6zYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=HAma8UcLPAEL_awG00crP4RVXfA6Yxpf5RPulhmZGcoD0OMr3cAJI2ZJjn9oYIxbW3-Acyzv_pd6TLE40kJJNFvu_2NYqxKd8pT13AO9dhdSAyUMaugeb4HLRtqJPPLVn47egWg-aWygYq5oK_R-ioub7yedlZVibwjDY1I-Faxpgh-9yl0AcJC6A7k6pFgqQYNC-m9Jg8njDuY8tAPxjXnrAGQSJ-hPIN_6BNQsDl19uOAea9m8g8A9jjh29dnvNLJp57QCbf3mbYzfn-R5nuuW0bg8XQSzqeSI-NSn5kck4yKRO33SFl-9nahuGqmVg0NkdNixWGfogsAb1lRLUYDIrt29tOWRRIyPBtxAMxcVQ56cM3KH9oeupkjN4LZLlb7Uk41VEZiQ2zbNIQLve6pRvw_acyXYBMLricC9L4r3ZDpYhUTOEnrkczjtuFpANvIvysu1GxTL3D6_D3UAPUAVv6nXhKebeDpwpg-gK2XvX7cQnB-B5ZHxbEjHSsoYEQhmbP1HtsAZ3lndv1beo00sbLElPc3nLYB_ekZOd6OZekZvCyiGWDRYz_VF-bGG5xW-Wtlgq18hBYV5WH9K1RflySLlio9qHZhfoOUn-w10HP97-5agYmgKHUsyM_owlFvHycHdafFHr2eVoybqajojiUhLv4bVt7tx9dsQjZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=HAma8UcLPAEL_awG00crP4RVXfA6Yxpf5RPulhmZGcoD0OMr3cAJI2ZJjn9oYIxbW3-Acyzv_pd6TLE40kJJNFvu_2NYqxKd8pT13AO9dhdSAyUMaugeb4HLRtqJPPLVn47egWg-aWygYq5oK_R-ioub7yedlZVibwjDY1I-Faxpgh-9yl0AcJC6A7k6pFgqQYNC-m9Jg8njDuY8tAPxjXnrAGQSJ-hPIN_6BNQsDl19uOAea9m8g8A9jjh29dnvNLJp57QCbf3mbYzfn-R5nuuW0bg8XQSzqeSI-NSn5kck4yKRO33SFl-9nahuGqmVg0NkdNixWGfogsAb1lRLUYDIrt29tOWRRIyPBtxAMxcVQ56cM3KH9oeupkjN4LZLlb7Uk41VEZiQ2zbNIQLve6pRvw_acyXYBMLricC9L4r3ZDpYhUTOEnrkczjtuFpANvIvysu1GxTL3D6_D3UAPUAVv6nXhKebeDpwpg-gK2XvX7cQnB-B5ZHxbEjHSsoYEQhmbP1HtsAZ3lndv1beo00sbLElPc3nLYB_ekZOd6OZekZvCyiGWDRYz_VF-bGG5xW-Wtlgq18hBYV5WH9K1RflySLlio9qHZhfoOUn-w10HP97-5agYmgKHUsyM_owlFvHycHdafFHr2eVoybqajojiUhLv4bVt7tx9dsQjZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=mhBeLv-QmgqVeyCBFxZik1p5rGMhxt5uP8w3qxU2uX_ExgIop6c4C4twhUMp-W2Q9bb3PjP2AC7ej9MCggVWbsh6eIWGtyEY5NfOiMMRCV_0d-esfH2az0jF2j3OJ_yGgnravq6BFioGHnUzaz96Dk0PP59tDLX1hIk-mHWLbacHaRCkBcLl1fLKgNqk84JlH4Xbtmgw_PhCRa3TWoACYP4PLHFgCQ8kAV63RO50_XCWD9dqXyWHGHojCNkZtmiPzra8zEa1k2aOVuUQEbP4uE08u6C2m1ipUaQHegnvCRAGOycIkb2Bs_aKdZBFIe-a3Fq20RHPAW9jhpQp2_DcCIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=mhBeLv-QmgqVeyCBFxZik1p5rGMhxt5uP8w3qxU2uX_ExgIop6c4C4twhUMp-W2Q9bb3PjP2AC7ej9MCggVWbsh6eIWGtyEY5NfOiMMRCV_0d-esfH2az0jF2j3OJ_yGgnravq6BFioGHnUzaz96Dk0PP59tDLX1hIk-mHWLbacHaRCkBcLl1fLKgNqk84JlH4Xbtmgw_PhCRa3TWoACYP4PLHFgCQ8kAV63RO50_XCWD9dqXyWHGHojCNkZtmiPzra8zEa1k2aOVuUQEbP4uE08u6C2m1ipUaQHegnvCRAGOycIkb2Bs_aKdZBFIe-a3Fq20RHPAW9jhpQp2_DcCIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tuU2JdjR5InhQ74d0PjqMbH9o5MZhrM-2eh4c-oGaRFUbV7bL6BVF7BS-w2O93_P3Zc38srOQlxsdO0Eo3fduF_TRBmKi-Ir3RSUeTJOMXXqRnQLU0-u2mDl1_GTFaWMOJBwLPlAJbHvpYkci7ncwhRup3NEYWt3jzyje-bhydF5JLOJqqESQvwWzqoj6vdiQQu5QwaQ3zUt1gr1GDxt-7bhJ6DGIR-tvnFNHz5sWdQ7HsXbaw-AlnR6qJPs0D0VQyMYKIkk4WTm5iMAei1aORxBrEBTubR-8yaU9cCVgjJNK_3L-Ho-mF18gMyg_FStT7hp_6iH5leuVdxHWm3bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Je91-SzqcMcrvqVy_x5pNDNO_zWYG0x7WXRPYVOjLdKYLZO8jByNaAtZOizDZnP98X-CHlEizErZZJQefAhSQdVOjYKlPXSw1Sei_Hmq47Lg-WA3vgzxXHxEHvtF7o0IcduP-Web8v0iaDozzfhlCF2uIdt3igvVM4euWfc3OVnSOGJJaMDrnysJqXi1GzCHzxf5oIDMip7HHFI_ylZMIPFVYThqdxaSH-Fj0ZoiBtvKMh2_3NZ8QWL2MSJ_DXd3I8cBNqIR1aGPe7a4Qh56awPg0sNVTObI7_vzTnJpTOgE4Qp2pUOcWxmzWwdyVyGPAUo7Uf0dz3Jic73XM2CBEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvekIhkeCo45cu3H-eEF9rY4kIFKQon66s2ROtnNX5G3jUgBIVJ6BbgELiH05Vj6qqCYzRUk-scmjG67HCh0IhbLttaLc71lMoLjvEAlpr0sF8wSkNEhcU5pcURhBVlSv3eJcSuaPkmfyNDXjsWhRsClo5wIOzd-tmq_iyXvBvEZ9zARHvLX_uMGGBgXUNEoIUxF_JVkt7Pa5j73MyPBl5NxJMzxCJtAVWWEksNEehviiWFK8JaPXZNkPSqF20FNay2lllR6U4B6xsbNBZDv5x0GLQKeL2qRBm4RzCqWg7Exdm7ZImdlM88r0RxqjkSr8iRmu0te_tbq9yEpsKzV9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RF4R-GdZXxiiEWBG5lpRTxL_zGBmZEyyyaQ73AbviwFekCr0Uye-vRBUu0Qxs-NNTwUDMFspD8dDJRc5Cry62di5PLe7u9GJplBNGMIdCZQleSrZT87S2FstYlZdDGjBnqgP4ebIYPt10ZDyIFuR2DejcIPrZmNzq0SBu2AGAsA7_zyy3y-KLXSZzg-oM_vM1pjyTQj1RTrWq9JoiLvsWPUbmeVUbmBbcl4iIYGJKThR3B08iNqQYYUanCRgTk0OVvDowG0gyDarI8ikbb568i5Hi4MXGY-ztD8oq_V1Z8IxKb_BHTftRWJYBvtnhwZsWTKM9LQde2fwNmb5ZNeMHg.jpg" alt="photo" loading="lazy"/></div>
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
