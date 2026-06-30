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
<img src="https://cdn4.telesco.pe/file/h5YAyUuFU2gx8IEElS0qQZl0qEaMdMFt6_mUa9vv7GGhLHHLqRLcWjT5sfMT2hHxIEWYmGFCmPLOul3M8dPn1rmR4kT0UPNVvx7nuvpP4gQ0vnmLLhIscnLiNQm2gjAHeV1Ys0lnpjQS2SBHsKxW_74pj9PP6AO605ePml__bJOKxJV8E45XtAkRfOB65Y1jTL7sM4B_Pyf0mC4CV4NHc8guXpdVXbLXsiUZdrQQd-JYNNP937I76RoMlJmnAFv-RHX6_VyU6GZSXj0FuJaYQXfj1uMcnMGf467Cm5W9RdPlgqHzAEkvPAYLs-YJuxxRkcj1Sq8cMetnuNh3whq-og.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 10:19:16</div>
<hr>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swX_EEbd8ka955gUXa8mjqa3j00ezQAkz8Wd7L1Hn8nEVCuzYntInb8g1G8PB3j6jbX4UYMq1UngMzJnI8rgc3lE54-OZHvEEC7lmVXj9eHTB40f2RWOPjlorBYln1aTS7c-p_wiO2RNOrA7kmRphQSOc0UeJaygPurCnf1Rb67TwkZ50HA1l8eTOYYvvlwCQR7ZpkYQIG4WVmRXAjTwnAez9JZILcbTNSVbzVSyCXsJDd-x8x5-WRr99AUPX3fjklB0Hi9lPLdyzpLvm9Gzs2Vx1XB-jCvs1Sm7pk8JGZla7Rbk-bZhviEfnSZg7kAgCRgsKTOywsOD2TcHt8niaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=jzbZbj7-scTgVJCSvdCzLPqTPNSkL_kbhOu_bzF3pTJ0WkGIXPtm55X7VDOj7plM9xS_VWyajJa8zUbSQveaeWC1styvAQ_9iFWkaihXHVs2e2o_1HG6AOw0irFmiishZ7blo31IShoBRlg6IOxT2yewkE5w96Ntkx0myBj7SkGxtDeA1NImw7E3C7nq9GNhowif7eIHyJmCvZLKVzTpfwFsxBJxGIrE07KGgfgN3qmp4nrfzsi22FKA2e8S-4fnZdbrbzb8jL_dUG41gVR-oTGNaBFxxHs2eMhAobUjC1vBKRCLy4TqCFV1rm6cP3nYlU9iWXoWZGymhUq3CIl92g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=jzbZbj7-scTgVJCSvdCzLPqTPNSkL_kbhOu_bzF3pTJ0WkGIXPtm55X7VDOj7plM9xS_VWyajJa8zUbSQveaeWC1styvAQ_9iFWkaihXHVs2e2o_1HG6AOw0irFmiishZ7blo31IShoBRlg6IOxT2yewkE5w96Ntkx0myBj7SkGxtDeA1NImw7E3C7nq9GNhowif7eIHyJmCvZLKVzTpfwFsxBJxGIrE07KGgfgN3qmp4nrfzsi22FKA2e8S-4fnZdbrbzb8jL_dUG41gVR-oTGNaBFxxHs2eMhAobUjC1vBKRCLy4TqCFV1rm6cP3nYlU9iWXoWZGymhUq3CIl92g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=vgzk22LsggUDmZnLuPT2s08bPum_1MfE3BjuTaZzEGppBvYIeV6faedWDyneNIlIMUDemibVFcoq9S7mrWip9b0LfhAK4-pN2_qkuQzC0TNtIoVOSzJ7IAiZRlCVkSM6r8_KJM-tBCs_tNCIQqiTVQ-VdF5kvT_cPi2JYCzhtVKxh8GSkZPfBdsb-O3xUyn8kKkNEh27Xd2-AG4ncNgqXiJFVNHjQcHqFD9dPCDN4QA5KBs2eWIc0Q3hoSKSJCoPtdxzXTuslDgYIJvBAsIGDj5Vk30zo5xf8H3aqaReuOnEM_PuHcxVfdHHJ9rgqF5ixdgNVnYfPUFYtolNkhRAZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2jXUzua6hqCme7db5HWAsnQpa4fSpg6wrDhaMKcv0NSw4IfhepNxyKTR0VKuswg2bQm6dqIjVuWN9vNMt0tgWoPIa25z3eVX6rx2F3xzLI7YBDjS0ptFM-mAAh0BpkiJpKMZbV61VDsyz92q8qIC6B0UO_5t8MCXWIqH1DYyIsTDXJOLPHRjxQ3t0_qiYmeKCsCn042cC5BM8gBNyDkY1fI9-m1wRB5jeeHkW5p_UyX-OZoRn_nJCNYDrU9ipt_p0JJU8YQy4f3-nH3fXsDN1TNa7RAx8m8XwTzMaqfcLyiSkCEwIgTc9013Shnsp8H96M3EeWlGfE6pzyBze7HHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=cGcq508OQsu3q24pjLGWWVsFUn130EycN0gSx7k12EHMyu3khCgz9MDekURo6mDdsIGom5paHbEE7Z3wikdMgscKf13eRRGXIX3gNq6IhwlidvgjsuDM05WzzKjSeyvZDUvJHs1g6ZeUxh9WqoD1lXHGGVCubIIQNa_WS33ajhwkGhKsf8euMbyAw6FR0zN1-Ln9Qx3MQAcFzzKdfd-cokW9WXnhr-3Cxn_fVBAjcBs_rddSatgScyMGfacmwb5KjA6mdff6CZTWDw2aRZgiX2Thj63dc5Y061V391fFTjsEsOytMdmpAbJas89bvP1pTiORRuDsaLfXqx26c3ri-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS5S9d764T9zFk6An4H5s1vCscROBLJiiwGNHZ3PKoNqthjA7EcQ0OEiwVRGC45CrT-B9nfORTMt-zTaBzRuhnwOSAi0N573j2jYXeYHfJjSPJ5MurKlKB607h538uhofhuzsdPrUsKIlOTR0h4fj-UV8LHj-AeaqFVtOq_ia2nYNQcxCdd28v3yIazw3z2Ih453pO2vA11hfz3ufIZ5FU6CWS0lJ0KH_i4U9toPEpr0xUMzz277_Mxdqcxk98bl4rlWjbku7LR-QPbnDZS5NoNMqnOKmnzjRLZ_pskoTfEzF_YClS8gjtIL2KssvvaMGtx2l3EZqqsPISxlkzr3eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti8Uz9ARcybXL0HKjBVxmxbf7kS8YOBH18zWqzQl7OOmnOhajooddGtQiqH5K8rmIy_W97Svteux9Rgheqgg7hEYWTVtNyK-aP2yiQ8MbPIvIBcbuMSgDtO5RjsKzznju3mQOAMDeu6lJ-q11twyKlwsSla6sd7d0g37yzLmiXQsLvvJLJHRQbyyY7uw17pNKrSLA0yXcDi7YaUQf5kk-pOD0ZMHSFFcqCpvN0ag4_TPhyaukyIzoS-Xs3Bc9GjKl6Uilf-1C20uhnyx3gXxUEQXXSIkN7RVTOpb4fWwBgTgf99yCp-8LCuhRwHj0aPDT8xSiL5GSZAZmUtBYUsi6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vbxhInx35vFu0JMUt4IUIzodAnxhF2MWmPAajg0GqW42xgmayS-ES3ciwQciSScDKBPeZFrztt3UDKqLS4G5ogCQCgrogz7aiCa_bUfFRUQWTmozTXpJAkJQt9rxTQI1UcZFS5thU5vH3jfOU31hsLugPfoiQurzgD6tO6NceMChq2UXNE2gXjaFs5z3yyC3u9m88Sb7ArSjM4qsAobICnkdei4nyLRon7vT_ArqseVTk5joxKLOPxtu4XZ0E908EerRYowcMjguzhWOFq_BxKoo6C3e8D3HX4WLx4hfHygV0--Qmk4_gcAsxL5DfuqtVVVWHnV5_gD2t6fRHmNo1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vbxhInx35vFu0JMUt4IUIzodAnxhF2MWmPAajg0GqW42xgmayS-ES3ciwQciSScDKBPeZFrztt3UDKqLS4G5ogCQCgrogz7aiCa_bUfFRUQWTmozTXpJAkJQt9rxTQI1UcZFS5thU5vH3jfOU31hsLugPfoiQurzgD6tO6NceMChq2UXNE2gXjaFs5z3yyC3u9m88Sb7ArSjM4qsAobICnkdei4nyLRon7vT_ArqseVTk5joxKLOPxtu4XZ0E908EerRYowcMjguzhWOFq_BxKoo6C3e8D3HX4WLx4hfHygV0--Qmk4_gcAsxL5DfuqtVVVWHnV5_gD2t6fRHmNo1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TahEAJjyzkLcwG_A_tgJ_nSwAK0ogmhz3o9DzS74uyJDrht38vN9GU_I5wKvhtsC40k-B0xio9OiadKyIbtP_hqkpsRf1qAbJ3Fw9vAZlWrHnRqGmXy-2ypZ12THdwfQmHSgg7MeFDYZXwYyZUBvf_0xAzx0trY_6H_6uMUpD0fc2FE-stvKNQzHzbF6GgkGcZ4rgq9gGABscl_9jH-QDsLGeNoTLhcH-ldhbsof49sFIdldqw3IiHGIqeMHIqx3b0t6dnpxCJxow5VxovrFfnbUOgQx2rTOJNDs4gVnBc6mgTxygOM6RnjA9YbjMyDJUcmhnCN_LNHnJFCDSd5Qg0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9TahEAJjyzkLcwG_A_tgJ_nSwAK0ogmhz3o9DzS74uyJDrht38vN9GU_I5wKvhtsC40k-B0xio9OiadKyIbtP_hqkpsRf1qAbJ3Fw9vAZlWrHnRqGmXy-2ypZ12THdwfQmHSgg7MeFDYZXwYyZUBvf_0xAzx0trY_6H_6uMUpD0fc2FE-stvKNQzHzbF6GgkGcZ4rgq9gGABscl_9jH-QDsLGeNoTLhcH-ldhbsof49sFIdldqw3IiHGIqeMHIqx3b0t6dnpxCJxow5VxovrFfnbUOgQx2rTOJNDs4gVnBc6mgTxygOM6RnjA9YbjMyDJUcmhnCN_LNHnJFCDSd5Qg0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=Xk1xG0W3VSl_CvtsYN6tJLms2G4rzzsRy36LImw-cnHt1tjqt5TaSnia__qx26Fi-IrzFov9EcRgUFeQkGf1LjZAyaxa_0FAUU55roHLtbVdvuWl4bY7af016h-SM69HQ-NMj8ws_Ehb7dA-c_TheefnbaPQIvukVYR12QL2rYfjY3_3ZhJmw_JT_0bxhgZDRyvGButzfqTLoiofUVj1Ih8Tab0shSDVbNVFxcPhYfVViKYSvMTy0YMwC1Wrq1IC8YXM8zJGJU-8RTdGJmQsdwSOLJL09gTyS691qEm37SIYOKpKfu25Gd71ZDFto3uFqxnL_rNs60OBQrexrV2aeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvztdfVtj9TfByy9vnraHfetouPFFNNQ7M1mSDFN9PsWO9nZmlU-_SU8KSxxzWOvPJHFb9l3sbbzS1vOSYIS3ERYaR0gD4S8VlFBsU5z9VWH5YogCVTsFkKTLwDMXex_hVBP94EaZS5S8t_BkPSsIBS2CuSeRjk6voR6QnHTVTUe7JJ1tMvzQA_5dQqFWLNmo56zzFTsip_AS_jJ9RjDKnC9quVXkR5i-O1-k4lk6-ygBaaN91OuFicUO3JTAWIGPEFKGYKcs0vP-xKBYgkD6PWK1S87hPAUgTzbNRRV0tAwOoDFadfm3ZGhVBKrTMOnUaBvbdap64KhpVAPcxwlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=akq5WJp14bhlbIiyUSA1FdCVD6vLGnKvXUQtfdXoKKLSJ0ORsOyG-WUHMzi_d6STDOaTVEYxGGPHUx7jplmxKv8oz2APedwqgKaDxqd5w-pV0Kiv9fm80VT9q-rjklPYzii_nEJwhLIusJj70JLQHTEgUPfHakT7ZeTE04ShNDq8pM4LwT8gWOKTtOhcHMr7mGxphV3dutlKCp9ZayrFrQyOW7gCWmZOk2cSZ7D2n3Z9kskpsyHjOmxxtixWE4R1pPio4kDkfdggw5_3pXRemzK-ZaiSJDf0mWAohyLHOWK-6eLpp4uYE3SdU-SUhNZ34mpWIeljHCA49kc3iyNaSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=akq5WJp14bhlbIiyUSA1FdCVD6vLGnKvXUQtfdXoKKLSJ0ORsOyG-WUHMzi_d6STDOaTVEYxGGPHUx7jplmxKv8oz2APedwqgKaDxqd5w-pV0Kiv9fm80VT9q-rjklPYzii_nEJwhLIusJj70JLQHTEgUPfHakT7ZeTE04ShNDq8pM4LwT8gWOKTtOhcHMr7mGxphV3dutlKCp9ZayrFrQyOW7gCWmZOk2cSZ7D2n3Z9kskpsyHjOmxxtixWE4R1pPio4kDkfdggw5_3pXRemzK-ZaiSJDf0mWAohyLHOWK-6eLpp4uYE3SdU-SUhNZ34mpWIeljHCA49kc3iyNaSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qDIoFiL5DR8OV0FJLUDttEVA81pgYbLyE5zz61AG9sa-fAuGXTvXKxMaHPv62F1HP-uOhqwqqbZ91dLsQ3zw5tmPzJbTHccNcLg4JPROZ3mtBaHyVO66oWKjSjiQ4tTklGOjLprq1f72VCw0n90FJNGJAd6PoSVuL6cV2goDHkj4yETKD5cZ0rhYHWhfMs7VaOuTBKqL3B4bjVzEYq6Te_qWazU3SdvMqnnQhPwWYiGXcyEQKw33mZF4IDuj8Hj1gI0STka32kOYr9FIi-N3WfDatdjYWH4i2ps5OuxH4CulE7QVIs0KHF_W8lyw7wfVWuEVJxEEHbKgeZEPjOY2cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qDIoFiL5DR8OV0FJLUDttEVA81pgYbLyE5zz61AG9sa-fAuGXTvXKxMaHPv62F1HP-uOhqwqqbZ91dLsQ3zw5tmPzJbTHccNcLg4JPROZ3mtBaHyVO66oWKjSjiQ4tTklGOjLprq1f72VCw0n90FJNGJAd6PoSVuL6cV2goDHkj4yETKD5cZ0rhYHWhfMs7VaOuTBKqL3B4bjVzEYq6Te_qWazU3SdvMqnnQhPwWYiGXcyEQKw33mZF4IDuj8Hj1gI0STka32kOYr9FIi-N3WfDatdjYWH4i2ps5OuxH4CulE7QVIs0KHF_W8lyw7wfVWuEVJxEEHbKgeZEPjOY2cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Vahz6obxbAoqstAxuTMkuWWiqxQHz-JwHM_5z8clcUXiqSVtD6C6FiezdR1gNBW0oq6deW8Azso50a_EYoR40OLQc5Nr-rrdxI7Y2ybs7eAuN-CNv9niVoVnMX_NXPZTUjqNoFrrnHkyEJHsrLPIPk7XlCc0M6G2iOH2KSeFCoU1Eaj077qWUhxGMkMEz4snMMX9ho82p6ORb7bg87x2pkF-gkjlgZTpLDSoK4GOapAOR9r9qjAx-9ylVlATUIedWRp8UqOkIJVsl0uSttLi25l1wk4bTWDOiPkw80GZytXD57SR0rD9Tq1yy0T3bg-wckGv5_ZTW5sRwYculMIQJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=reiGs8j4Tebyr7SbcscWsiQmI9bXwz5sL8rGByVCQCoYrUCBl2KQiBU8FBY-mLVtRHSx5wn-2XSY8MzZhd9Q1B_hQybUzReFxUynkDWobyuPDwL6ilc-cMEP2o0tqzDXwkNayXSSXth9ynT0EAzMQGfGEZw--6oKAQWTsiNdcN5E_1rXFJ4YQtC2FQ7jg25uPkg-GEzPnaT9265B2a-FTjDz2311br5p59Kypao6TsEXe7WPPw0kk4Mz-28dAC-7v-8G8OAjGZzUKsOTCgVCL8jMCXnY8tuGlUKF1muNeyhSFT-Vhi0S2TDyS3MiEvVZ-zw8y9ATTVPRovK5qpAONw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=reiGs8j4Tebyr7SbcscWsiQmI9bXwz5sL8rGByVCQCoYrUCBl2KQiBU8FBY-mLVtRHSx5wn-2XSY8MzZhd9Q1B_hQybUzReFxUynkDWobyuPDwL6ilc-cMEP2o0tqzDXwkNayXSSXth9ynT0EAzMQGfGEZw--6oKAQWTsiNdcN5E_1rXFJ4YQtC2FQ7jg25uPkg-GEzPnaT9265B2a-FTjDz2311br5p59Kypao6TsEXe7WPPw0kk4Mz-28dAC-7v-8G8OAjGZzUKsOTCgVCL8jMCXnY8tuGlUKF1muNeyhSFT-Vhi0S2TDyS3MiEvVZ-zw8y9ATTVPRovK5qpAONw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoP1nszTs9AZrALFJpgip2u3uBKxNKQYkCAnNT1ZA6A0Gq3MHtmYlYD0zi0u1l95NA4t2OF5akPfe-lKYeg52_v3su-u3ZdAq_pWMcPiwC78-fIS6vuS4DcJwZccR5p3zkFp8dQdj1bGe-3X016zpBz7JDCmH3tEh70BCaF1YpfPb2emEwwiVn8ny7wpSWfHUzQUtdMS5zVpCPtyh6jADhMzGcmgAiwddNoM2HVW8CxcFkv3sBaQtdKeshb4npcYq73tLIEyKsc6hG0-mwYpVGE8Vr9FaWhc-0K47bQp0puMecUzRYWapw3J4A6bJDhx4s7b6fcY_l3Mvzw_P-lCQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=BNwGl-041A5NUj0uT6d_Z8xW8bqM38_MzVvadPlWPRDwo2J9rGqAkDmlk48-gP_y17IUuoKCTVwmXFGLtGQJOWyy8FeKu8OygrkUoax9L087_mT8RtQ5ydoawsV-IADJ3-Jso5sc0DRRKYCVw80SgCwiQn7bqV87WWmSdR_hdqqzcNlGcYfVJnyiOYPb1IJ8mFvoLHZgQ5SlewPQN2-IRiCBhdsTsSKXOZrYVd2PlQPmqEgQcEIOL-5sZXgrWcvOe700Z0_4-98X3ckLM-mQlTsZO1lIIh7haw_3sPVySlGeLVJBu3xe37Oon-E1Xb7CMVKVJINJAD1ra2bYXqHauw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=BNwGl-041A5NUj0uT6d_Z8xW8bqM38_MzVvadPlWPRDwo2J9rGqAkDmlk48-gP_y17IUuoKCTVwmXFGLtGQJOWyy8FeKu8OygrkUoax9L087_mT8RtQ5ydoawsV-IADJ3-Jso5sc0DRRKYCVw80SgCwiQn7bqV87WWmSdR_hdqqzcNlGcYfVJnyiOYPb1IJ8mFvoLHZgQ5SlewPQN2-IRiCBhdsTsSKXOZrYVd2PlQPmqEgQcEIOL-5sZXgrWcvOe700Z0_4-98X3ckLM-mQlTsZO1lIIh7haw_3sPVySlGeLVJBu3xe37Oon-E1Xb7CMVKVJINJAD1ra2bYXqHauw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ftcnLFrMvI0SDIDq4Qa0B7cf4l20EwfEpjTxjmcdvtSHVJTOAVSPyclPocluy912yr7xK7L6LCPWMNKoetPyilUP22fREGwXKUYJPJAaC3jcJU4_GyHPRO4tEBpEijf-8-WSvmwKLYxvDKdzTLyHSYKo_ESNItHCSlkDKoOtcf-UXKbeVAyxkVfilJVax-APDyoOZ-mBGSjzLgWk1h1eyqKId-sSO5ldgPUv6D-EPN2k2nPSPuBysit2gd5J-w_LaHIXMvffj-rwd5f4xs-sFW3ROXmsDvj7PPXO3s-OoLC8dWKB7hNHVxMgnf3d5DVneGV6paRG8IM1ifL9cz-_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=ftcnLFrMvI0SDIDq4Qa0B7cf4l20EwfEpjTxjmcdvtSHVJTOAVSPyclPocluy912yr7xK7L6LCPWMNKoetPyilUP22fREGwXKUYJPJAaC3jcJU4_GyHPRO4tEBpEijf-8-WSvmwKLYxvDKdzTLyHSYKo_ESNItHCSlkDKoOtcf-UXKbeVAyxkVfilJVax-APDyoOZ-mBGSjzLgWk1h1eyqKId-sSO5ldgPUv6D-EPN2k2nPSPuBysit2gd5J-w_LaHIXMvffj-rwd5f4xs-sFW3ROXmsDvj7PPXO3s-OoLC8dWKB7hNHVxMgnf3d5DVneGV6paRG8IM1ifL9cz-_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fP-lQMgU986XnWqs3EXgKfybzdResUOwuh183IT1GZQ-S2Y89AK6wSVrzUtJTxGv48gkUQyG6PWCR_x1YSjy_C7DAzUdLtPcNwlAEuyjU_gUTJbofQgD4guAXNQ6wClOXgxonRIU03I9aB5-4qzww8CU1BB1XqnUvbNUIEmUIqPlIO0yUdZ8wqWT5b2O5Bfaq9lbeXD70KYEssepfMm6Wx8_bVERkPltZFpHNC7AUAE00Dmiy4ybZV_PA2yxbn8IaNZ74ZFFMAjO2ReKUVPR73rIijR1x6SZcWPwLY7dJ8VlGW3luTCHBg0c0jh8HwyQsRDxCLfnwn_TsNrC-R1kTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=SYgT7iQ7pJWpebSaHrkE62x2uACRPRMz-XlJa5tuqIw4DFgeOWrN5slzM5pVNTLQ8Gy3qlbYJfrhQhfNgRPzRqJFGUN8Y0RAN48kk52P4zPBlxSrek8Ny0-BrqGftOKgramc6DYZqvJqyCitSoF5hKRBM1QiPFwzwES7_Fj1jAukuzdh_kWTOVpyWeAvKlTjQrQKYXhRJV2eaxmMuU3nNkX9F1iG15G6cT_7jjr9UNyEMGkjAySc-onPOhAeDAdq8K88vpr-7BfcPwos5OWCV3wFEZ6T-kcqadbxTNd1nmmWk6VGWP_ySY2fxFO4tqr9x6xJTGIBPdBlkW508rn0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=SYgT7iQ7pJWpebSaHrkE62x2uACRPRMz-XlJa5tuqIw4DFgeOWrN5slzM5pVNTLQ8Gy3qlbYJfrhQhfNgRPzRqJFGUN8Y0RAN48kk52P4zPBlxSrek8Ny0-BrqGftOKgramc6DYZqvJqyCitSoF5hKRBM1QiPFwzwES7_Fj1jAukuzdh_kWTOVpyWeAvKlTjQrQKYXhRJV2eaxmMuU3nNkX9F1iG15G6cT_7jjr9UNyEMGkjAySc-onPOhAeDAdq8K88vpr-7BfcPwos5OWCV3wFEZ6T-kcqadbxTNd1nmmWk6VGWP_ySY2fxFO4tqr9x6xJTGIBPdBlkW508rn0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=ScFIol0y_hm4IRVH9Ubce1lUakXyZIBb0vJVdRdu-83Hjn6WMLDxXRXdTfMNqBHglO0E5_hJYjwP9uP6C9FpMT8nRfVln8WUsr1-if_z-sgjyUN97tN4p5nRdv9aD2WAmkry-tQm7UGJPL85gD0T8tCXGUXU36CCyoHrwQftp-yMmpHlt1ClI3KLCed-yWJ9pRPJufMCC9M97Ke0lBkY4xBvm69FAIdWIdms4RvGhxdw_fDk77bV64lY1RhrjkikWB9FI2-vxuyrwWUctoyhaFESF1JF7BkM-gDLyJkLQuwdf8aIyyawgxCC59pnJ1Mjz2QqiM3X4ODVi6NF4g8OIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=ScFIol0y_hm4IRVH9Ubce1lUakXyZIBb0vJVdRdu-83Hjn6WMLDxXRXdTfMNqBHglO0E5_hJYjwP9uP6C9FpMT8nRfVln8WUsr1-if_z-sgjyUN97tN4p5nRdv9aD2WAmkry-tQm7UGJPL85gD0T8tCXGUXU36CCyoHrwQftp-yMmpHlt1ClI3KLCed-yWJ9pRPJufMCC9M97Ke0lBkY4xBvm69FAIdWIdms4RvGhxdw_fDk77bV64lY1RhrjkikWB9FI2-vxuyrwWUctoyhaFESF1JF7BkM-gDLyJkLQuwdf8aIyyawgxCC59pnJ1Mjz2QqiM3X4ODVi6NF4g8OIzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3COGPDukrVbqp3_YROkqZ0vlHQDw_x1bNduAfce7w8A8qokySOuxnukIr9_FzxvVeQGjr1QCTa3a6DjPfi724DcwAkWT53urEZC_FKdSaci6H1PgtGGuoJkQsjDzUNvXd67OTt4-mVy7YW8tUd6Fv_qxUrlbtHhijJJ4mhwMHqOSjOH3KjY8CoaQAQ6adQrRk5GZcluuZwNrI5XKU1Rdeh5oIpYZsqRxb5TKmmVMhMW4d9loTK2L7H-ZdTejiMOOBrvda6lDDwNr9VAT01KT_Lb1v7xMC0z7fUQj0mJpBObjnluIAYBO592Jtq-rZtL7j0QLNkfDpl95Hakr9JT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XhHqhNwn-1HN4hXtCXauwGsKGsJEEuzybpBdJXm9nsdNHLQddnNekBP9stmUe5v6NbRDsEJfcCU-FpvyTrSxcD42wxWO0JK9WIupoWn1RWBltW0SP9_eEjCWVvQkVjiyYde6nsNt2_kREMpIlwTJ8e63VXQ8ZfOxlr058wg2V4tQgoG06qseUz9UzIR9972OvTbY6tSgrvAo2ZJYT4zlLwvq1BaJr1OkXarPu7M1xhFMDro8Z8lMlrQr3vuxbKJpxGZ4ldOa0PE0bQQZ12SAgG48YGQHGPCB5wCYi8K6ZLAhjQbPBXT7Bp3JWx1Z36X9oEDvwNIaaYIQxIulJkEfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qSNf-0ZWvkOIpajNBoPcNJ1Y8M7VV5hQ_ZD0CUl9-4VNLAMcu52_yf4TAYxyvzfHo8RqyFFLluwuAHTRgbbOiPJoDHEgqe1qZyEng_wVIQI7j_uEQM1nYSiVJv5c_jQXDC9XIcsMefwL9QjBVGH1WN0rG0VirIrzy60LqcsDz1DbcmXGFQA8zofcNUosn_StSci56A44nHyzV8h5mTVeGSHKucduxJ8DHFuMwxfI1iRUAzSHSr_XgLZBEtyrw-6cr3HKY-Ilq8j820SLRUqcRGAEagmbaytza1I_4j7gAl4OWtQ27XFu58c07-rM86EhBpwzoDAG7ZyJxoaHJMJBMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=A4-gQZLouIZy_mfSkPg3yiKd1YhoHhSWdIfu_gqe1XUS5vQrbrBYyoEDmC7-CTT30kCenjfp2JMw2rPu7kaUQ8rOda_9k0PzloC5n-JQ-kYDfWOlkVU0Vz0tfb9bnIHdd67sQEBE1EXKdV33mVhqXkODjyC2WxSk6hsZSOtTQiOzosSrbPRRguVkYiwO3ntuBtFaH37AC1iPk4bfzBa9t8ZtOzdoM366bOVCI65zlzWMRgwbzxzJ2dsieVqW1YXhJABwXtmFd6aGeD8IvqH1M7mzEbuhIZyj7THZYnbcT1Fb3OF5btMgSDg2qcQgUU6NkGjrOfu-OThh1mP8S3Iz5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=A4-gQZLouIZy_mfSkPg3yiKd1YhoHhSWdIfu_gqe1XUS5vQrbrBYyoEDmC7-CTT30kCenjfp2JMw2rPu7kaUQ8rOda_9k0PzloC5n-JQ-kYDfWOlkVU0Vz0tfb9bnIHdd67sQEBE1EXKdV33mVhqXkODjyC2WxSk6hsZSOtTQiOzosSrbPRRguVkYiwO3ntuBtFaH37AC1iPk4bfzBa9t8ZtOzdoM366bOVCI65zlzWMRgwbzxzJ2dsieVqW1YXhJABwXtmFd6aGeD8IvqH1M7mzEbuhIZyj7THZYnbcT1Fb3OF5btMgSDg2qcQgUU6NkGjrOfu-OThh1mP8S3Iz5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUQBCtO4QVe8nZL_8OYWc-iQLtB0WHgJVx0CdmoHW85JPm9WnVlPnf0EeDtPVIxBpokdwk8d6cNgw7-nMqDLWgkMbMkEKA7ltNn1mr4cvs6AdloOp_3Ajq5BojQ-UXQ61hpjVuTo680rsRskw22M79XtPhV62vWi-P9SwX_6CPUSoLI8MIRemN2cQWF8ol577OUupk0kbG4Wdx-ADhlcFA7aY9wIZT4OXR9SmjdF0t4a-3QvLVIudyKSv-CCYyDGZUYvIXhwPL2O7vrS4rnuGaHXcmwqY_te_mUx1Nqzez5MTozzJCbKkGgLypq56mvdReQDB9OWwvaqJB2Sw7ld98k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaUQBCtO4QVe8nZL_8OYWc-iQLtB0WHgJVx0CdmoHW85JPm9WnVlPnf0EeDtPVIxBpokdwk8d6cNgw7-nMqDLWgkMbMkEKA7ltNn1mr4cvs6AdloOp_3Ajq5BojQ-UXQ61hpjVuTo680rsRskw22M79XtPhV62vWi-P9SwX_6CPUSoLI8MIRemN2cQWF8ol577OUupk0kbG4Wdx-ADhlcFA7aY9wIZT4OXR9SmjdF0t4a-3QvLVIudyKSv-CCYyDGZUYvIXhwPL2O7vrS4rnuGaHXcmwqY_te_mUx1Nqzez5MTozzJCbKkGgLypq56mvdReQDB9OWwvaqJB2Sw7ld98k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=X-K58r-ol0TePuFP1u8KEoXf5SoC-P9iSoV8v4LC8eAFYL4nmMSGYErxpP_PLIxgSp-fOXCuaVS9kdDMT73PlIBn3YtFa826paL9DnQtyvDFjeWxK_F8wTdeQjc-E09pFKBzWBEyzPW1NmjkrHuDX_rEVLFPpP8lNxk9VF_9s-wvYjIwdkP4iF3P9aJ6tCsYBnf91tadtenu5LlnRg1wS37CUL4ZmK3r6I6lI2gn1rOjMej2xe7qtMLuwnZRBH4V14nS0OgjG91KFZTtJAX1FxECMx6QAljvPPf8aL4gAnYVEAhND3QGUO5rHVpudUVoNVUfpkd5LYWW5rZywbeHUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=X-K58r-ol0TePuFP1u8KEoXf5SoC-P9iSoV8v4LC8eAFYL4nmMSGYErxpP_PLIxgSp-fOXCuaVS9kdDMT73PlIBn3YtFa826paL9DnQtyvDFjeWxK_F8wTdeQjc-E09pFKBzWBEyzPW1NmjkrHuDX_rEVLFPpP8lNxk9VF_9s-wvYjIwdkP4iF3P9aJ6tCsYBnf91tadtenu5LlnRg1wS37CUL4ZmK3r6I6lI2gn1rOjMej2xe7qtMLuwnZRBH4V14nS0OgjG91KFZTtJAX1FxECMx6QAljvPPf8aL4gAnYVEAhND3QGUO5rHVpudUVoNVUfpkd5LYWW5rZywbeHUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMLME0pNs_EX1qqUMKDL4dqJJr9a8Wcnu6XjXImH6BAhjp99z4jnUEJKAvprnbz2B__hgNHZTbvz5RhrYGOLNechrY5I3ZbChh2qDa_Y53KyVkoUZiJfhR8Ou8KA18n2aow64533seDNhTgidZWMA2pzppdQlMUdaGmdpvAeNTLRcJK9XDawxgjRMfoxdanVyrEOhvoCvej5DvRSwXDB8DNGgTSzDAH-CSmClCtjDm45-LScK0De90KixegVmGw6QGi6_fgyok4WC4LMi_vHE7AsbAEjcCr1id57q_EVP1HTsUDdm_0eksQx5gVn3_foXLmY2vZ-JrJSmZHuRuH02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHD5jou3_LsIXSssD6K_QdI_M_LEV80DMVrdYy0r9x-b_w-l6RYstQOujBjkjLxdcktRFh_qHrCK74Con-VTzhlKcIGA4BIJBL9wqHtNXsTmpRyyaAKfrMOaKCgdMuNaw2E_vU5UtNBiiIusCGkUKweukBtmCS3NC061gv10rFIRNsBxogGQqtx0_VVEcuvBuXm92fVUbUB0EKpqQ9fNXzfjz1wLP5ZAVqq5U1BMLK4u8ooEZcniL0OxaoIeEiS8u99QHS2x6mhAGbWrwmbgY5mXhQNkyxfQ5kbdoIIrOlW2_yqw0V3xPPkqisJZcfIpkt0jXopclqfwIqwRsE3cFBmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHD5jou3_LsIXSssD6K_QdI_M_LEV80DMVrdYy0r9x-b_w-l6RYstQOujBjkjLxdcktRFh_qHrCK74Con-VTzhlKcIGA4BIJBL9wqHtNXsTmpRyyaAKfrMOaKCgdMuNaw2E_vU5UtNBiiIusCGkUKweukBtmCS3NC061gv10rFIRNsBxogGQqtx0_VVEcuvBuXm92fVUbUB0EKpqQ9fNXzfjz1wLP5ZAVqq5U1BMLK4u8ooEZcniL0OxaoIeEiS8u99QHS2x6mhAGbWrwmbgY5mXhQNkyxfQ5kbdoIIrOlW2_yqw0V3xPPkqisJZcfIpkt0jXopclqfwIqwRsE3cFBmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdrgktlUS1dgGxUujXve0KfvR7LK_HInMLJ922NVk_m6GGV9yokHy_oTUQWWHk6Mkmtb5PwlQMh9URugfhJDux2E8et65O7mUIHqANN9uSfrT9kjvcVtQITCnjFQ_lwfJz4PV6r0JeFGU85KSb-h2iSm7DLFtybzfS8Ttn1QKVtqoArpykpSiRaZM-_IgTlVbg63FGzl7nAgE0zTA925crr5clNL1gqXfiecF8EYO5fTgk12zOWzHPMp9a5v7I2cwFoT8vFuko3WVBrO9x2DMZE06D9JS3qwg7_T0Zq3s9D5OOMeC8mEkX1vtEkTRQDNx2fBQx68mZppfqB_vLueRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=gCq9U1m7g3rH8SNfkI1VU8l9VSZydMEhe2su6_wo6W0qgdB7hmg2BGyjOmDz2IkUxqLxsO2A3T5T9I3iTc5o8Tk7GIn_GP_aYL-SCzz_bhN_kHkphx9zQ8BSkz0KxWLUXC7PSTRpr1pxaCboGB_lj52LT52-vbXjd0qGNjny3Isgmy4hNNJMXeqC1E25MgKZQdoetR_sACwGrhcg3wZlJQIQqCPj5bCCGiZ86cwd7WObHuoUzIQ5_fdrUkABBsSEpCp3zveODgYdHRLqcCbKtDJeYJxod5AqbH9l7uNs0atlqNJSMyJdLSTazhXyE5kBLn6L6UV0JRLyM9vj9TtswA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=gCq9U1m7g3rH8SNfkI1VU8l9VSZydMEhe2su6_wo6W0qgdB7hmg2BGyjOmDz2IkUxqLxsO2A3T5T9I3iTc5o8Tk7GIn_GP_aYL-SCzz_bhN_kHkphx9zQ8BSkz0KxWLUXC7PSTRpr1pxaCboGB_lj52LT52-vbXjd0qGNjny3Isgmy4hNNJMXeqC1E25MgKZQdoetR_sACwGrhcg3wZlJQIQqCPj5bCCGiZ86cwd7WObHuoUzIQ5_fdrUkABBsSEpCp3zveODgYdHRLqcCbKtDJeYJxod5AqbH9l7uNs0atlqNJSMyJdLSTazhXyE5kBLn6L6UV0JRLyM9vj9TtswA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=dtBW9l_GRwIsyTW8cOJZqBk_msWlfdWtLuw5mAabgNN42rkf5jowzYTIY_B_Aj3DXqJn1E4lq7rT-xxxPWBITvgaZEk2btlxV9TrQOmSS4KqRriXiaRea8y3-E8ME_4FAGsYF7u2UFLTz4jTY4Ur2yTkXHFyxpipa9ka1tfLVPxHLsNPfDImnJkHeLwlBDtizsuzw5W7SJgwL8UJhDKEb5GTlUFIgDUs8eADE_2B9nvTEaIE6ivO9PsoIHSqEJZoAV-GyYnmzpl3exuldcgIbiOsNoX4bhmJAd5uUUOpY6seQ6GzlbuOGqoOmpYWBX6thYaCW1qHHsWv7zEn7P4ipg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=dtBW9l_GRwIsyTW8cOJZqBk_msWlfdWtLuw5mAabgNN42rkf5jowzYTIY_B_Aj3DXqJn1E4lq7rT-xxxPWBITvgaZEk2btlxV9TrQOmSS4KqRriXiaRea8y3-E8ME_4FAGsYF7u2UFLTz4jTY4Ur2yTkXHFyxpipa9ka1tfLVPxHLsNPfDImnJkHeLwlBDtizsuzw5W7SJgwL8UJhDKEb5GTlUFIgDUs8eADE_2B9nvTEaIE6ivO9PsoIHSqEJZoAV-GyYnmzpl3exuldcgIbiOsNoX4bhmJAd5uUUOpY6seQ6GzlbuOGqoOmpYWBX6thYaCW1qHHsWv7zEn7P4ipg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=HAuG-Kymb0l0Qn040TGKKOzmJosYiCi11F_a3Yu5KE2qMjneGexOpJ_G14EHai-ji-oa027m2Xl7k7i1wmLTOGKkodikefKPwCyfXgvHHU43ZGmAHPm217qGm-QOZShs6j5anIWlx2w88LDApa70_PKBRqZkidApzu8XSk-TG8MKggtddd7-NnxdXg_YWwOalYLuHfXjtcdrAm6uJoqQIKBt_7iFeH9bKqahg4BobhjKD_ZlYYqXUoiJNL_PWf4UigdIk9UvHnvB_-AJGnnjU2pDPru-TFAIB0qP7H7G7H84PbUkSzz8RQdIarpaKdIBMV2q1pzRV7PmwK3VpG9mPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=HAuG-Kymb0l0Qn040TGKKOzmJosYiCi11F_a3Yu5KE2qMjneGexOpJ_G14EHai-ji-oa027m2Xl7k7i1wmLTOGKkodikefKPwCyfXgvHHU43ZGmAHPm217qGm-QOZShs6j5anIWlx2w88LDApa70_PKBRqZkidApzu8XSk-TG8MKggtddd7-NnxdXg_YWwOalYLuHfXjtcdrAm6uJoqQIKBt_7iFeH9bKqahg4BobhjKD_ZlYYqXUoiJNL_PWf4UigdIk9UvHnvB_-AJGnnjU2pDPru-TFAIB0qP7H7G7H84PbUkSzz8RQdIarpaKdIBMV2q1pzRV7PmwK3VpG9mPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOtQpEc-4enUMrQBGyBtEcTiD1UvbDrh5NwB1BJWVW4vaee0VT-RLZCdJy4uKrwpcD4rnx_yXx-Mf1dmpMo4LiSyas7gFjl5qiqTnuqvBjImVAJ20kaqym3IDock-7y2zVxPvMnlc9KSHP3OKg_WShiIDEf84wbzYJGan5PDcXzqVUTAsClp9G3BVuYu-AYNv7i53AyU6woxB_vgeuX8PSoLEw9MUw7p4kUAF40Etf2qWsw90ltArm-TRcbZpZ1UgqffbI0glo0MNRlU7EgnhPt6126YLyVRgRUcooLsfEuoMPNV1YiAr6VGZiZL-egzjCjJ9k8c7Y4e4tGSsuN_PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIp8DcPunjcRHioa7QwaTos-PwYw94nsE9d3G0aGoF4_SRoxi8pBCg9RjGgtz2biz5FqbzvBhywfQd0DYgwqlACsngNCdBuDJ77oRCHZAikmrcSQlFqHpTOZcKt6LZTSbM5KVw9LC9rxgsK_PaRvNGKKD6-lHwr6rmaDs-FkOhZNEsy1nW0-H61w-C-U-ubQPMK3qBkRJvXyH0eJWNXmGmMKupv0eHzwMzYUrdByl0rXTYPvQLhB90w23_k3tUl2Xclr9pEUUkYFDN2xYgSByqHuboSdw3iBYWF7evMHHUSp9mPxT0iKpFUXxb6ajm9qfwcaH3YkWQA7Yqpuafbr3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=N-Xz6djG0uC3fiAZatEldol1vfrYOCcJTxbh2uuE4B13ECDJdSZuxYMLJeEQb66eFTUNzbLjN_IbUccmuZHi2O0LhFrm6EvyIf5fo_HSRB5XYgXUg-PMZc8LSn_-BKXJ6fKNESEEcm1I1nTEh6XMvZvuBt3AGRVq5iUKIvYfY8-K2Sq8EPY-5wVy9vFcwYn__zzQm3YG8S_CW8uSTN4qSuy4jVeXT46WdZjnmG52t-dDcWAKf5zzCAxJNMTJoN3BBdoA9sNPEv5xIsfn3BWPwwZZUzltMUm-oeevgxTJg1lMgnKQrviQR9Sqgh1v1rNNkDuDHCMC2qS59-LzTiodmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=N-Xz6djG0uC3fiAZatEldol1vfrYOCcJTxbh2uuE4B13ECDJdSZuxYMLJeEQb66eFTUNzbLjN_IbUccmuZHi2O0LhFrm6EvyIf5fo_HSRB5XYgXUg-PMZc8LSn_-BKXJ6fKNESEEcm1I1nTEh6XMvZvuBt3AGRVq5iUKIvYfY8-K2Sq8EPY-5wVy9vFcwYn__zzQm3YG8S_CW8uSTN4qSuy4jVeXT46WdZjnmG52t-dDcWAKf5zzCAxJNMTJoN3BBdoA9sNPEv5xIsfn3BWPwwZZUzltMUm-oeevgxTJg1lMgnKQrviQR9Sqgh1v1rNNkDuDHCMC2qS59-LzTiodmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIulv5001OY7JimMuQxuuLavhHlSszHc1nRIIlmyC5FC4O_hSdlCc4hE4ovckOqmF57sZnckOTbpqWZnDZierHOQ4qhkjJiNRuEBi86xO8eKg0O-g-tqeUt5tD8yIFSe_mE9h9cWotsFYN4rQv30ow9n2MpnqICCNl82GNxWeLKX63CUUN6RvWHUPTQvgZznhbmSqmI9zic2N_J9BnUtsAP8pA18kEKV2TtrdTgkUSTCmc2X5NUmmFDxZC0MecXdP6gF9xS5qWJG1nZuW7BC3yjsi7EnCqP4_Ym8X2CI3Pb7hSPPARef1OpwKH4JJdE2mYFGM9wUXZusiZpzVxpvvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL0W1CfZ9ZP2zI_uAnLK5pK97mXWvqyr6Vu1cX9CbVokw551IL5F0a7LPEF_Ze1HbhaOAyarjcBUXf3gKndOckkWr3aIa6nmYY2Hq92awtmE2SmGKhdbmc6sjYjh3OMngGffXdGU49gHzbPa5ue8uwlZMlKlurA_3DstgOHm6eqhrFNUxwDYr94INxyigvksQ3feryiU3Cyl7JMTaUtSDLl7xNlmE_w56qfjX_RXZ2kFtGxazc6jLjt7DIUrLfx0-w9FKICq94F0HAqlE7kApb5lqwsJjTjshm1-WSlNUKXeT5Lu8tGZ9im2bT9VJV-EAdOGKhby2MB_CAqz7VwSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=sSzLMVtN7SfRHF5tEyyLfSPYOc0XlBxFtiLE0KmTArtO_3KjhrtMezTi0spAyGq82fGDash87lfqccUyuR6lhqkQQSgd1UDcCW-GNVve4a0qo6InjdDS1VnEBLStGGkfUUu9o6WVAeX0Xcd-4SZZNjUvlU_-JowUOR-HfjelYJ0_sTurYNuJj7sud2rQnbB36kA9gBhSDjjbvwYaTPhVvZAkdjJF6mOfHEvkRsEAQbL_3z9jsBGJ5MUHpWbLfCIswMD1V2TfgkJAWdnj2RY1N30UkPMQmcms6jhWDjDWjq8wv5ILULNH8bfTWiOQ9ylISeL_ibpj7eybzyf2JtLuzwK97kkYihaww811LS47WcdzyvUWAMmfv66SqC9Mn8s0Bbgb88ws5EdGsNcz5RNa3mWMMcVbKRHwF8ZtutWLr0eSoZlA2SElHi4dfvtHC8M4H8iwXqnmbzNUSAByq94Zv_b60ShiY05IGkEDLr765DTq2GhmGY_CE6bjs1BCyt88Cj9-wHw-OOmKritGgk7kdjDWHNPVON4rAbbeja0R_0h2Wzuv4W3kQ1ipgEgRj5Ayh-ONiBNko0Wwo5m1Ci39NAS7T091pSH_VYgS04yzHFL5fcyPlab071GwFDIL8nIZgM6lwES0Y8Asz9zK7X6wr_OatdvD-auLs2It9wbyHog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=sSzLMVtN7SfRHF5tEyyLfSPYOc0XlBxFtiLE0KmTArtO_3KjhrtMezTi0spAyGq82fGDash87lfqccUyuR6lhqkQQSgd1UDcCW-GNVve4a0qo6InjdDS1VnEBLStGGkfUUu9o6WVAeX0Xcd-4SZZNjUvlU_-JowUOR-HfjelYJ0_sTurYNuJj7sud2rQnbB36kA9gBhSDjjbvwYaTPhVvZAkdjJF6mOfHEvkRsEAQbL_3z9jsBGJ5MUHpWbLfCIswMD1V2TfgkJAWdnj2RY1N30UkPMQmcms6jhWDjDWjq8wv5ILULNH8bfTWiOQ9ylISeL_ibpj7eybzyf2JtLuzwK97kkYihaww811LS47WcdzyvUWAMmfv66SqC9Mn8s0Bbgb88ws5EdGsNcz5RNa3mWMMcVbKRHwF8ZtutWLr0eSoZlA2SElHi4dfvtHC8M4H8iwXqnmbzNUSAByq94Zv_b60ShiY05IGkEDLr765DTq2GhmGY_CE6bjs1BCyt88Cj9-wHw-OOmKritGgk7kdjDWHNPVON4rAbbeja0R_0h2Wzuv4W3kQ1ipgEgRj5Ayh-ONiBNko0Wwo5m1Ci39NAS7T091pSH_VYgS04yzHFL5fcyPlab071GwFDIL8nIZgM6lwES0Y8Asz9zK7X6wr_OatdvD-auLs2It9wbyHog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETiQvGYSReBOFMyLCw6DZHdMvuo4-cE4r3ib3xHrX-pVu-LxC5_XDEid1iGOycB0-Ewwr8UsCPIpSuhvGX4jK_1l3Fxb0qKh8JyU6GfYzSvVcn4BB26WEWhMeQUY1gQBErD7cxl8EpVGpCw1WQqBNSLVZbDCVn6TfU1hAMb4w2F2YcWiBJ7VDx_ZgiXkeExMg2ePxqFE50i9NRb1qno7ohT5BUlXrJmuTFo0VwSe75rAq0240-ZZizGacdiDP2LwbwxJB8xyOYgaJ1HbPRCgZ3y8PdBcCZGcADI6lB-VG4XIUuPDP8r3NAGfu8zM3GIhX9cTIL8A7U_EpIjPT-mkJNgk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETiQvGYSReBOFMyLCw6DZHdMvuo4-cE4r3ib3xHrX-pVu-LxC5_XDEid1iGOycB0-Ewwr8UsCPIpSuhvGX4jK_1l3Fxb0qKh8JyU6GfYzSvVcn4BB26WEWhMeQUY1gQBErD7cxl8EpVGpCw1WQqBNSLVZbDCVn6TfU1hAMb4w2F2YcWiBJ7VDx_ZgiXkeExMg2ePxqFE50i9NRb1qno7ohT5BUlXrJmuTFo0VwSe75rAq0240-ZZizGacdiDP2LwbwxJB8xyOYgaJ1HbPRCgZ3y8PdBcCZGcADI6lB-VG4XIUuPDP8r3NAGfu8zM3GIhX9cTIL8A7U_EpIjPT-mkJNgk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=W3jPI2X1UN1TWMefuRi45DkHngZMO47hcRyHsOK8IHgyZbbLEhK0bumAFQp7XKqBjG_jKyOxt3n1z6nnTFb9iinHhhpfDb5bnVAal5G55Di7YQgK6rnI2XZGyF6MA22Ye170CP-eudz5SSvAco3rCONC5ZMVDHOg8AvyPbRrYXp41Zc2O4oNidI9wsTjQr0uvKn2DAwhn0ZnAjEG8rabKm7oFphVtfZqkSzdZtkrCBvf-veIA7v0ocbUTpoWwTH5EyJ3-6MKIbjrMPlwJW8AbWrIevn_HnyYE-2Ho_FrC6ajUQGDoujbbH5DoXlg8lEpoY3ipCS2WRZIboEt6gFr-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=W3jPI2X1UN1TWMefuRi45DkHngZMO47hcRyHsOK8IHgyZbbLEhK0bumAFQp7XKqBjG_jKyOxt3n1z6nnTFb9iinHhhpfDb5bnVAal5G55Di7YQgK6rnI2XZGyF6MA22Ye170CP-eudz5SSvAco3rCONC5ZMVDHOg8AvyPbRrYXp41Zc2O4oNidI9wsTjQr0uvKn2DAwhn0ZnAjEG8rabKm7oFphVtfZqkSzdZtkrCBvf-veIA7v0ocbUTpoWwTH5EyJ3-6MKIbjrMPlwJW8AbWrIevn_HnyYE-2Ho_FrC6ajUQGDoujbbH5DoXlg8lEpoY3ipCS2WRZIboEt6gFr-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=Qh_DpDYhpzGvloyV9STMRxTXplEm9F1mE7CORsbMGIw8CFVQmXRIeMm5fjA8lj5MOd7zaP9Jz-ear9sR_u2N8zbSQqE10YUbmZxiOgJrsc9c4dnvG50t4paGmivQ4H64Bu80nlK71nV6sCVnDuDdvq1SnknPuNo9k4ywQCF6v2Vv-BigHoLtiS5RI5y0VSntZ1Mrbs1CaSFU1ZR9BHfMeGKwwOsCGbTr4rehl-1nFlVG1aSy2aBsUd11dgBlaXmgbX_i46ZHOhtsgkjL-AEPu-UwyS90U1htcJnJCHBq6Sg-gZ54FJb0fnejPZGfi0XGLcYtfdSy01ZwlaSNXInkgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=Qh_DpDYhpzGvloyV9STMRxTXplEm9F1mE7CORsbMGIw8CFVQmXRIeMm5fjA8lj5MOd7zaP9Jz-ear9sR_u2N8zbSQqE10YUbmZxiOgJrsc9c4dnvG50t4paGmivQ4H64Bu80nlK71nV6sCVnDuDdvq1SnknPuNo9k4ywQCF6v2Vv-BigHoLtiS5RI5y0VSntZ1Mrbs1CaSFU1ZR9BHfMeGKwwOsCGbTr4rehl-1nFlVG1aSy2aBsUd11dgBlaXmgbX_i46ZHOhtsgkjL-AEPu-UwyS90U1htcJnJCHBq6Sg-gZ54FJb0fnejPZGfi0XGLcYtfdSy01ZwlaSNXInkgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEfLfuBYDEvvoYuFK0_8WJn9eroGl5K8cG22icUyFQj7RNYlOSRjfcFlJgMJQK6yTjhPMcF0rs3JB-ryER0cYGJiRRXERAYaRtNdiXcEd55uV7qmTpoJz3kNdP_nQNaTOz0WV5suudao-PBuokJlgW18T1ymQy0kfHLdYcMgBWAq9CvR58lHC66FWUaGjrO4nLMx8yFzjnD1ODwoJxQtgw37EdL05MiLZF9yKyBMWVlgML-G9JLO2WfZdHxBZVOUsrIQP8XgKDBS-3y-LsaRwMIfoC5gs15EPFaPrRpOhlHUpmlB848INAKjS3R7_66VrDLm5UAMBhFfwMjkM3Iumw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkoJTkPhVaSgtry1meED4_cwPurbQMI4_n4IBN8MTX1vIhXu8ZdxCEcpLvVfiPsVPBDtZ4Rg0QQBfdaerPhitjuswoR1gO6ijfXnCscHa2ozvEW-YV6uaSqalvy1x5dsw_5j1f5UVoM7v4mJ7UFjRf_dzC-CYAnAvRQKqpvo9ViX_rVhl2QWSYE6Qsp6M2ZsBBY2g1lsBsZ2Pc5IwWbI5QxoYCIoCp_CJ02H8L9OB1--EOvOoE6layXy3Hamc9IHsgeoKzF5dMs9yr7n3xraKE59g1bZ4VHKG_M0WnfqfExQv3Sd2ZuT3dEvFo9n8e5myF5rCkg4XV2NSykBj_PUog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSGiTE1T0RjVQAk8COY9obpXPJ7dp-fGmgY6R6QwXP9lMWtQv1Gl68DxMrU2UTi6SV5Jtq8AZgarVmSovvayW3fdX7PKIk4MOvOmpVEkUjqYoc8GCx7kyof_G4XKvII1adezid-TFVCZFLuKC3d4TJ9_GKeH6J8kbrhtLZNNv_5cWbukP_qd7S6tzEC-75mGk-RHkciH4kCeyhZM4gfAuqrSYMqDlGA6umBrDt6CHlvMB144bo7U0wdE5GpKVzhnZP1mxG7XcS1QDVvfUis7QqMZVIMQwU5zYVfzbF73ECszYh-p_agYpAz3rtpOfJ62h5q8p08GHVmnWpy5QSj7xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFDX0wAllWdCcZjupelt2bQz8rHI9wJ_K3trw-optpK8XDF0frxpz0u9QyDCf9_uYgS7210ql0W6kyA4XWbuNMh8g0zQ6fhe_J55tfhKm9mMCyo7QQ4f9ohIpWVJHaatA0b4HD41Tpd69_0qnd7X67fJkC7lafkSu1j-z0loF9Jp9XUUuEKV33Cf4fsaXpPHiRfWS3DgjkUTN_WEkHxpSvOniSiPpjMdzvAg-9J5XNbpe0y4KvWtcc8jXvBk57xrmqldvq-UTca0zToXvLYnJeJDej1DHpmSvO2NerYDAhHdkUvo8wuyAhk_TKlMPjMYVLJfgtasN7P1dIoyE7ihrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT6ZEL5P4vZubqNsuj2PsiAFqdkxH1YMgzlWtl5NzDTUzchSbgx_8zjRiSbGX8IYzfUAy2zxMpLJxncxfPxorpKnJCdJKx2g5D0pUkyC5_BYDn4YDYLZrjS5gBo4sxcRggsNxDiuE2EwtooOTD1hnbhrnR4SXXb1myKvkkgP8J3kPKKAmDZb8gMieoRQyNz_xOgPF_--cO4QMPuYaE1MFwsWniDQf2YDJtR1zQxWbIrPEqANPrP97_KnLVfwfae7W__AU1groKzijGSF1CA2cWfrBv3G4KIEBRBITjI-ZJqmpL2GCr1Gi-JLXii-4gPOVKhT5H_8bksSWdhO_4a2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=Khf-wFusd4_GQlanygHxnXcWzMsxJk-e73fB268a-97Kn56BH2uh79fqTzFeWUtJs-rdm98DL4TXISfHxAjsQVfyLtthSLRmMu2UlzJUPFI8fIhdgcQEy45etwfesWTv0drZctrcYd3rC6_MhcFFb96ea3VgmQVg732nH8NIdBWHlqpjG_R70LnmUsh2Uj244k5Vgu5oj9TqvnTqM6hrzTCMdIWHbHcheBkUmyFho8eYcJDQEJROLg3lme8jNlS25w-VB-xENwMlbSFY7QqldBhvgerbTL5nAOlt7pTkUk6TNTLr-qhXWgpJvHpJlDsAkYoygcpSH0zNrs0YJT7b9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=Khf-wFusd4_GQlanygHxnXcWzMsxJk-e73fB268a-97Kn56BH2uh79fqTzFeWUtJs-rdm98DL4TXISfHxAjsQVfyLtthSLRmMu2UlzJUPFI8fIhdgcQEy45etwfesWTv0drZctrcYd3rC6_MhcFFb96ea3VgmQVg732nH8NIdBWHlqpjG_R70LnmUsh2Uj244k5Vgu5oj9TqvnTqM6hrzTCMdIWHbHcheBkUmyFho8eYcJDQEJROLg3lme8jNlS25w-VB-xENwMlbSFY7QqldBhvgerbTL5nAOlt7pTkUk6TNTLr-qhXWgpJvHpJlDsAkYoygcpSH0zNrs0YJT7b9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=hMHhIWqrBrTrd9w3Ksw6Io6Vs2Un-LnBajf0rysSGZKszEvNns_g4514UGShyQqz4s1q_30WlgQmuSn--ivF4gpIMBghVUla8PzcIuBmWvLyDbDj6sMIyf7vR1VD5f7lqt2UYG5SC3_SmD9MJ4MwjMJ1qKtvkdODxgAGZGzolgVFWGHnAwC3MHMXwbV4F1IepM23aNnQYtj-YUVz-OmwvEjNfp_J7rE5NjL4qHiEH-_fIPICa_B0mt7QhMnlKW2Objixuz3nrSBE1XA58cWxoJ8TV4NFG1cVMthEx5T1xYHi7vO-xits2To-uBqZtbT749YZRQByIEMQsxJllmwz9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=hMHhIWqrBrTrd9w3Ksw6Io6Vs2Un-LnBajf0rysSGZKszEvNns_g4514UGShyQqz4s1q_30WlgQmuSn--ivF4gpIMBghVUla8PzcIuBmWvLyDbDj6sMIyf7vR1VD5f7lqt2UYG5SC3_SmD9MJ4MwjMJ1qKtvkdODxgAGZGzolgVFWGHnAwC3MHMXwbV4F1IepM23aNnQYtj-YUVz-OmwvEjNfp_J7rE5NjL4qHiEH-_fIPICa_B0mt7QhMnlKW2Objixuz3nrSBE1XA58cWxoJ8TV4NFG1cVMthEx5T1xYHi7vO-xits2To-uBqZtbT749YZRQByIEMQsxJllmwz9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz1w-fpo4YOyo1qUiQj9uNPL3J-NSb27XRExZx6o2E1U4y2hdxo7TlciDN6VE9ttkKAfBCXv23okGy30Sba-7Gjwug1bFWUA5eWBTkpwchKx4-M8KQQtNJqZz5d89L3ykFXCAqmWhhFkgFuuN7ZykNlpcAFJ_JrLfFyKM3to1h6X6HRPhBgroDGmjUcYqJlpteokBUa2IQUB-RgpATq0XX-n9moGg2p9hcSTfGTLkeQLX_KmU9eC0xGP4OjqDpXhakshBR8jfjkcQhBL-GuRKUjf54BBKJSXrCRgQwyJbog6LX5ZqbQjJBTviwfOzWPwcSWqg8hq9clAu64oMpBx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYW0lJlhQMDKqty73dN6NBe4-XyZI4iMDD8knBr3VjXumPMQDhFzretoJPOxiH-MrFBX-E9CD1gwIgBTjj22WZQUZoZRcU-8Gkf1X0lAGBtEfxPmHPdPqmqjReIUWQnBvZ3LBeQofQ1aYc7TkVZFaUp44BeZazA7T3Uf9WiMS-dzeBHYAWTPDGvrawNb50f9eQVN4mgleFUpZLWkpMg5nUx0dw5ZRQJHFeKNi0DNkFK5wPiW9LplYxiSfZzR-FrwBZ3P4nJC3FuE0EWHWNyAK8m7U_VHZeLHMRxp7gm41pJGHRwtzZUKn8K4j8BqN-vxOdYVzQ0_kT2SC_lytNKMcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=N02lp_-TzPHTRvncpP63vzMf-sOqIAYSvcnZTvCEXIaHpr_4dta8RkS9w6n7MMK0MDdS_SoYod51huFjw65wvlSWGqfqCpMcf2nrGdBPSE8vCqd5B7IxSMlK2eGVLCwU-xoakXO6UU72LBc4FR-pjLAAD_HFrJGDcmFDh7ChRDs92MilXj9j_8x2eDVxtzr7FcDev4ADHI2sbL-GfWD3a4h5Ghbd5qGCRgdp-brN11kCdJuoH3tAT58dLTyDAsPVuqPMN0j18BB24nB4p4saD_HxzJLnHB6q7lqrb7iZJn-L22jB01Ai6qKGEt4_dleEOEet_vOf_MfOdS7YAYA_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=N02lp_-TzPHTRvncpP63vzMf-sOqIAYSvcnZTvCEXIaHpr_4dta8RkS9w6n7MMK0MDdS_SoYod51huFjw65wvlSWGqfqCpMcf2nrGdBPSE8vCqd5B7IxSMlK2eGVLCwU-xoakXO6UU72LBc4FR-pjLAAD_HFrJGDcmFDh7ChRDs92MilXj9j_8x2eDVxtzr7FcDev4ADHI2sbL-GfWD3a4h5Ghbd5qGCRgdp-brN11kCdJuoH3tAT58dLTyDAsPVuqPMN0j18BB24nB4p4saD_HxzJLnHB6q7lqrb7iZJn-L22jB01Ai6qKGEt4_dleEOEet_vOf_MfOdS7YAYA_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=BMDwhh8cNDzKZQwD1cme_Rxxt49UC02nhQirJSbLcOzWz8zhiiaPcBu0jN34d6EEqbmH1igJQAq5RwGyQewzW_w8h1N-vgYtnG0VzJYrP6wLGKiCr5-yKnA1d7sS8EqYub8mB8vX-lVgwr8CjBwyz3Z6vEryoPHX2zYwxpQq7fzDUFMD4V-q0fgJifs2v7_n9ie1S8s_z7yHxgadL-Tc1KYjFVYvsYuJ1HQhIdkwH0OnhTYsw3mX3el6ucDN5KdmwfsRBjNL99MOyWrKSEDc8WiyrXlLTUsLlTxJbSwQQVwV4a1Bf9GJmnHNvLSfPHoNw6S_iw-UUKAiU9UEbYRd8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=BMDwhh8cNDzKZQwD1cme_Rxxt49UC02nhQirJSbLcOzWz8zhiiaPcBu0jN34d6EEqbmH1igJQAq5RwGyQewzW_w8h1N-vgYtnG0VzJYrP6wLGKiCr5-yKnA1d7sS8EqYub8mB8vX-lVgwr8CjBwyz3Z6vEryoPHX2zYwxpQq7fzDUFMD4V-q0fgJifs2v7_n9ie1S8s_z7yHxgadL-Tc1KYjFVYvsYuJ1HQhIdkwH0OnhTYsw3mX3el6ucDN5KdmwfsRBjNL99MOyWrKSEDc8WiyrXlLTUsLlTxJbSwQQVwV4a1Bf9GJmnHNvLSfPHoNw6S_iw-UUKAiU9UEbYRd8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJRrd8DFPTH-ftRJ4hZNNpfOhn686uRr0xUBMpnVIhWfkVrY3CuS8NRwihWjXRItc6I53qpm89TiSInXFgGDsdNsJqwCdqIoP4hKmMKYqGd2yIURhWboVj4HAk-oNKHTjdnibmBtRRzOUen6K-3wR4B_rGkgRgsY4KmQLDwdNsjLF9IBC1NhqRvHG04z4k99LCqgb-I7MC9CXCMGogZFY2ZUOw66_gd9nfMM4MgvXwVFfe7axMznTno-g8JINherjwoAZbQ7ADtgTeJjyYVw1GQP6giopKRu4NOK849kPiUgkJusLCqyZj9yBE5edTfdq33Vln65n8iDgMtV7R_76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tngfZ_hwHA1cc98G2XaXfhuG1TfZEkDsIrWQcO_t5bw0AW9ZcX4p5IlPDLUqu_lf_bSIUXxLUXE6CpAyvwvzhhgFkK9gdH3SsOnOAJPSGBQDh35yx6qMlSxQd7IDNy-KZb_PQggQLGleMaRYKpqh71En9HcalO-RGlq8qoxi9uY0ZRuESgUCCQKGrttd6tCHZH5p703SYRxZ63MDAJQivU4Em1NGZslCeRHgoGu0ZMANEuSexSzMH1xcRvvRZMdnUBjH1axCb3XHUECi0O5hmIp0xBBRRf7dfY5h3-5lh48X_mwDygCWejOoeYenSjNdyIjKg0WXSanbD0hak9Y-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RUnm3Whcd_wF1ZDxD3MtSlLRLiIhaSLBnoe02xgMsjS8AQD4cLEZQlYkgVLZEtS5nRGujoLwMYcy935wvpeG5e46ZeDipiXZe2F2U5JCtcQMYQhNunx2E9N7FGdI0YCUREvt9Y2YgqInONX2F-CJcFe1pk-pvQ99tG31Pt9XtUIvmq5DXdTS76FClxy9qSpf6E6-XQUXOaO53j9HwbDv2Rn31uYu8v2V_2C2t7hNSjXkgSl0Se6QJKyh06JCb0ReHRu9YUcmrBWLL4grc__MpSOI1KMqfDfFiaNv1z5rZWfhqJxvAktmMEvbfndjG7YeAO_qAaZte73SCSvvdSf9PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=RuYeJMcbDsFYZqqHYBR1QE7wCKKCawKrqepdGlnEWu-HjJ3gSuTodauMpBvDQBSks1qetuaqXLw-FQjj_GRDckfgjcntjM_thLIcP0TcCWrkIYM2D6C-MR5MmJzpeYPdLxSNmLD8H-1FwL49kTB861HQOQ5BygGQJGXSGA7NdfyoT8bR1HnK9n5yLT_n0xaQYk20O54ETfo6ZZ7Ao2ymZLPGnFdoTfWO-j8T0rxSuLVOq17C6jjl6dCHBLKf972wd_i5vA0PM3yqWCiz8nJjK3QkZA3Lvm9iINhPEdO77BiX2_AAI8aP5b_u_4muxb4EmMcXf5ZAlwxX9zHc4pYKRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=RuYeJMcbDsFYZqqHYBR1QE7wCKKCawKrqepdGlnEWu-HjJ3gSuTodauMpBvDQBSks1qetuaqXLw-FQjj_GRDckfgjcntjM_thLIcP0TcCWrkIYM2D6C-MR5MmJzpeYPdLxSNmLD8H-1FwL49kTB861HQOQ5BygGQJGXSGA7NdfyoT8bR1HnK9n5yLT_n0xaQYk20O54ETfo6ZZ7Ao2ymZLPGnFdoTfWO-j8T0rxSuLVOq17C6jjl6dCHBLKf972wd_i5vA0PM3yqWCiz8nJjK3QkZA3Lvm9iINhPEdO77BiX2_AAI8aP5b_u_4muxb4EmMcXf5ZAlwxX9zHc4pYKRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrCuYD8siMamIDc-L2lrW0kguP1u1-hFdFnQNQpwK5K8wxVAQ4PbOLQ1--qRCDGRpXpQ8d7tgT42dPfLvvW5x5FnLi_HpZPM1gbwXr2TLuVp5us3HYn_gMNdmW4BpFH5HmFndoVCMlVwkvPrrSzYbMrQzEzaKJWJlZVjFn6robQ_eQkj9Xz5ViEa39SSno5Gpn7JmxXHjbX5kzgU2qOt92cd2-Sp9fEZSbhnOJjQJUpIT22iDdgd923rJaA1_fDAJBXl5JtobaAg4tfHBar1dW6d_vm9jrSSKxneMMEP_1WLfHPtgHbe4dK97YLJUWFsn-H9v9i8oBli95EZc-udpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJ76-kjt3vLqeIDeZ7e0-QyuFDtm9fzFvrTz5A9GpdLPAv6GRsW4nTOoRwkKTk7yzrJ-q8UIe7c8K8jIDaDAFoiDT6fHcEwZVGEwMDUbYK0WGMDuF5S_a2Bm4mRahTH1ld8Q6K-dsy9y0U_UCHEAuT4Fa_Rk6G2ysvEr3XErL0q_YVn5BIQPhDUIjnSPPeQMEmc_JyT_NhCKRyLHt7zUXQqrJ8NUoL2OOhaMlYR4fBX34UfeCkO96PeORDd4_WEh7d4Q1OeuWpKN5IoZeL9Wpo2h3I85LNnbq_yh8IWBfifQ70THSgMZyODGQ1TvISMXe9dzSXMG_JrBNIThID9z_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPKi8DxVkJN_jntP1uXPqvbsQAxWbUivgo1Dxa62O81p1uwjmRHwPDICHJu_X3QAWZUbeKLeqneq4G7lzkVKptpJUzYHC_utMxRsviKxAgp0cS7TPXku4tY4QGujn9_niiAVJtJ4U7hjbbuV3m_l-vy38GvJEvFT8VdrHZOzxpP4THfhh9gRvGYfQbVuFtBtW8JxFxZow5MBro_ycEWTX1sMvDTEE6ot71ZO33KzR-_iyr2wmLF_FfV3wlXEOfQ15UNQMmCfoROh6c9EdPxUr_GsimljxL5uGSbBqJtolSODTY-3kZnRukh4XC1gZ-dVU5wu55ukQHL4Pzc-05FbFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8MF33URqcEuIX0TLDvuMMuP2yE2osBwhUdXCXcPHm6m4LwmN80Cv_tTBzk0LAPbhile0XfsCXntHjANfM-EegxORR3vX2zVmcp8fOOvncgkXd23l5Vr9jDxR93OqMYgvGQMDLC7QFffegqxEadiaH3feAMiNxXCQ52VNNq6pwxNKawQRZITRieA6ghx1kxIPzSJpMTJxYI4ykC6YsH6oqMqY7NL1MTrS9FyJH9C_jJCDLyhqgoQFetLx7FvEaellsQtircnkTiBguB_nqGUXrU2WiBX-8AtXuJZkZjC_kyzSC7_RZ2-6XCfZVE4Awb4NRwkb4zaaFwvZLeVJavjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=pHeLaSjw4DA-pCd0JKIGtX7i_thHr_kZ-ouYWvuRxrCRqrIn2ZepP2zIiixUQ7inw4PlqR_hRE8j5One_NxudLZ26mN3YteHnyek4YPjMz5O-OmIjkmOtRwKw32toDTTj7yujM-emc0zHRtsLQaSNbhXeTb5Oiyug00TJ1YfUFUVZpSe-H-_Lxk7a8-Gk8UUancunNs30RB5dy9kvxxS5F1hI0SG1f3rB5guBaJPD3L0T1FTG4xkNFiTPNDnGRFJcFPQjJAVWT9wFY4-pQyW_OZyKZWG1Bw-dO68PQYnBvhphcp4Hw8BR9YDLOPxcjcucLFt8nIrwmXCTfoJd4B8CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=pHeLaSjw4DA-pCd0JKIGtX7i_thHr_kZ-ouYWvuRxrCRqrIn2ZepP2zIiixUQ7inw4PlqR_hRE8j5One_NxudLZ26mN3YteHnyek4YPjMz5O-OmIjkmOtRwKw32toDTTj7yujM-emc0zHRtsLQaSNbhXeTb5Oiyug00TJ1YfUFUVZpSe-H-_Lxk7a8-Gk8UUancunNs30RB5dy9kvxxS5F1hI0SG1f3rB5guBaJPD3L0T1FTG4xkNFiTPNDnGRFJcFPQjJAVWT9wFY4-pQyW_OZyKZWG1Bw-dO68PQYnBvhphcp4Hw8BR9YDLOPxcjcucLFt8nIrwmXCTfoJd4B8CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uG_0MTbbImhd_14I72jO-EcbSpLi2f8XMduYNPgS3p1YBfPwNWnRIuy866IEkG_dUXhJ9Q609KV0JNj0Vp67H37EkLXl0EM4f8NE1MSCg2vQFSVfExRw90KcsDN4J3C2f3wIXPss3hzMZkR6ym85zRaHgLvUsVfYhH-zHGjXOb1CPwvKG6wAofIZUwLEtk_sO_x7bI2-iRxoqHWMZcQECxNwPnkz2dXFetDqNiUzQGgBHKUuJ3GRtQAG9yOXhSA7wU08Sd1t85-zVUoSd9Qfacf_NVQMHwiuCUtg7mLpJAhE43qCyevn4ib_iMNB1IigcVGWax3-pn5r7K-3WhdN9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP5BrhQCFBhy-O8XAKLK3tfauVFUtILsphYh8HzFmpQy3xejFBuq55c9WR2JZvKrPiGqZF-eKN1wEDNHgMUQNvgh-ZvHrpk5MsvtWWdjxTEH0aPzwYofUo4xXwKPhakjn2kS--n7evqnZrLgAOUHRsrCDS2IXQtNXu5mlqP2p3WRRX3nWWF67c7xwHuiwNaSBUSPVj4XAzp3aq8jTb7nuIWqghGqY0cWhRrx9d_mPSLiCfe64VPYmRxtScL0c65ZUwm6biB9BYL4P4iSfsL8pUJvPPnX2G7VZzg0Otm7QMyTB7yEQ1jWs38nhpEMzX2_jvdbuVUajF-eaXa9ECu6wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Khnl1NWlmtE37xSMnc98UPofNqKfy9cuti0tNMbTZ6ViWlMTo7vyLS5GyvsAGguv_aYNFI4UcnxI9LkagBkJFwJLzsv5_wMH19PYhsYwKH-EPhFl-PcKXwFkrUqZDFHLxTVJn7OcUOlJz3ZQrmCgA3wm8NoJyK37MF6hM0ar8ei2WWP3yupHW2sLtDwXMuXQyoImf94bYrC-OKZMMSfpVzNVF8B8MNjEuzpxG9sNvSaHmXNUkSgdKxsCjnrMwfoIEKa0YIcNJ61qN2lzS4sgCqHl7TaiHjnXTC8qAuZ1Jj3Q664KKZvceJarEre3scm2NN5iQ5xhkSBcJNpPhPt-4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=tGNPxpRhAJyCUJNqRPk-I_cqg_eQrbOCPaa4BXkfEq9WWaQmSYhsdOEvNbX0P3VHjDG6jUxL0MN5G-_AayHqUXUKR-DUf3bCxFEhvCmGKPRvw8GTLb380CRRhHC6omyf6OMPZ_A7xThgFuZg_pfd5ajvSGyMd0oQQPEolDYf8bwSdxAFVz0uTZnVGt0_dnStXZdvuvLz95tvvDKWNvIqo0ruqOpVaKuzLU3vGtMRxK6ITkD7POfi4vQoms441FWT66mvR1GpiVV3Rsp6SO0YCLX9Gqk6SoApnQJTnz7v0VwRxF-80pcXH8yBLMvZLLsJs5Ou_WrPVMdnAVIzjnXpQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=tGNPxpRhAJyCUJNqRPk-I_cqg_eQrbOCPaa4BXkfEq9WWaQmSYhsdOEvNbX0P3VHjDG6jUxL0MN5G-_AayHqUXUKR-DUf3bCxFEhvCmGKPRvw8GTLb380CRRhHC6omyf6OMPZ_A7xThgFuZg_pfd5ajvSGyMd0oQQPEolDYf8bwSdxAFVz0uTZnVGt0_dnStXZdvuvLz95tvvDKWNvIqo0ruqOpVaKuzLU3vGtMRxK6ITkD7POfi4vQoms441FWT66mvR1GpiVV3Rsp6SO0YCLX9Gqk6SoApnQJTnz7v0VwRxF-80pcXH8yBLMvZLLsJs5Ou_WrPVMdnAVIzjnXpQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=k7r1Bl4vM0GJkQOGeAuZGVgx9cAv1qsbUXdpsZkqcuiB6mQlebAUvYKy_dheo6ea914UpzSI431nCRTZUJ7jezTStDYdrRRn6YMvKzg7wTO-z39ZqxcVybCYH-2ci2hDFLqDz0XOcs3tuZURAnsdJR0GfkkjGcz4rp6YDMW2eX7nvtIPePli9SGBGQ_lA_lfBrTt3r3LiCtQX3ADDqnU2Ovi-0D0Cihwb9dRIPM3h2NAL70XGcBot8VAkItTMmfvumK9-qRCZT6zg6_5zKI1lqKfcLo2kSWB5UYNnGMP00qAa1UCPtiIXgIyXeru9aMMP_Z9Y36fc0mf0hKU4ApvTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=k7r1Bl4vM0GJkQOGeAuZGVgx9cAv1qsbUXdpsZkqcuiB6mQlebAUvYKy_dheo6ea914UpzSI431nCRTZUJ7jezTStDYdrRRn6YMvKzg7wTO-z39ZqxcVybCYH-2ci2hDFLqDz0XOcs3tuZURAnsdJR0GfkkjGcz4rp6YDMW2eX7nvtIPePli9SGBGQ_lA_lfBrTt3r3LiCtQX3ADDqnU2Ovi-0D0Cihwb9dRIPM3h2NAL70XGcBot8VAkItTMmfvumK9-qRCZT6zg6_5zKI1lqKfcLo2kSWB5UYNnGMP00qAa1UCPtiIXgIyXeru9aMMP_Z9Y36fc0mf0hKU4ApvTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=kTb6ckx-QX4yUxg2wpSsT3kh1E0_mzbCQg1JGlY1k0GFbXh2Qi9Oodh3g2SI1siGwgBUdJqp7NUxMQEWprmzn5_9Yz8NevONUiyFrpT0kDNvdY5d4UNV31QmqFwbfbIevHkF7g8SMOQ8nPpSGiJTZXaECkkLY9OGQM2HcDBFrbPwJZslIAYXGp426kMmc6AqcdjKEbFl8D1N7hj9971SK7lwSvkb8r4HVQsTjMyCyWATklK_5jhiRi1FCo4swRABkUg9ocVJfo6quVmeIo2N4Qd8ZkJGuQ4qpn9hA6ySioQu0Q07USqZOAM1hcEylYGU2YxMBuODL6Nc_DEo-jpAEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=kTb6ckx-QX4yUxg2wpSsT3kh1E0_mzbCQg1JGlY1k0GFbXh2Qi9Oodh3g2SI1siGwgBUdJqp7NUxMQEWprmzn5_9Yz8NevONUiyFrpT0kDNvdY5d4UNV31QmqFwbfbIevHkF7g8SMOQ8nPpSGiJTZXaECkkLY9OGQM2HcDBFrbPwJZslIAYXGp426kMmc6AqcdjKEbFl8D1N7hj9971SK7lwSvkb8r4HVQsTjMyCyWATklK_5jhiRi1FCo4swRABkUg9ocVJfo6quVmeIo2N4Qd8ZkJGuQ4qpn9hA6ySioQu0Q07USqZOAM1hcEylYGU2YxMBuODL6Nc_DEo-jpAEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APyo8kFkJ12dWTAPACtDJlPGiM__mTxBJaX9jlWRjAaMKcAm0IvdRQLPGSHTFVIfuw3WvrdRtmCYV13At4E39Pk5fw7Dd_8rDQF6xfm8o5NNzTuBqCc48pdcP5jAimnCu8Ck9KY-UP7fg2_41_jTqRqN8-SixGLNpJvbuC9t_K2Al8FRcKnqZHNTyz274QFpMMIAo25d7crITsq7yHcba4wbJMP6T4xeIGNGmUzzk-D-RN1cy4nUCFF5sbbf692rnz8kffqL5B25vc4ZYsONu7rwJUvePoPKFLDav8qj_KX4IykcSCqORmcjbB-AwoyR8oFgGjOTeSiPpILCRzmpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyPA31qshDChtZ9gA9WF5K4C7jJhyC8oXb0kcTqkcaKoKvACphctT9Ha-iVDf8j7UM5rhoTvKu7VkkyG8po8AH0J_sWKJvPcduB14batfnb5MFgqahhD0YbCILxFFudHnHjMZWZYiWUjPbycLPYbpqCU5MeHUFhRIj9Py4clJ-wEn0MdamdJnppqMDkWYZ-HxOq1mRrGMbovi6vmjFY188pJQDkdsF1a-UJ5jKMosooZCQHTFHRal6R9THSd-3i1ivNQJU6v9yNLFUwJnYsdCqK4sITWomfuCKq4HA--Zaf9Hy5ORNeObD6G1xuMu7vwDILQW830Pal0cnouh_pZ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5694">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceeQv-c9Tr40vLaDXguXghgin-OlgJRGiv66eKNBQAdWtMeiL24ge4YzUYm24w9KtoMUbmKUrkpkTAhJFk2Rq4-eDBVrORBv6le37uIbFDNGf0INtNSGjijB4IzRP4qyUEuaZ7xkhn-r_NSuWjerUr9FrkPjYeHQlOEphhKj1xcQd-s3bhc-CWYdeBwesWoMiPiUm9dxSDY20V7LPOBNmG1eK22SEQbYMUl6RXiFlAwrJBTE9ZABzQvshaInB_oygfI-r09a4Hlhecz0wqE9OexSEpPscu2V-etwCYJVvdFtkA6NfjTZL7ZQdP8yib1hwTYVQDBciBTltYOt6NvJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcrEO-7Q4kTqIQzTv6dGUJgp1HwUv5nZLe4zD48MK8yfADtnsKc3Hvpyaw4YmH_7CvebvB_aU_zuqIZo7Xs7HTAAH85QG7YtI7mJF-l28nfWEaMVxzIdgmOxjM-zNNP4bnaF_h506TKmIQtfNfe9L_3jygLVlNQhu5kpWWCmCmaJdUNTE9vHjhKmQNHY5bEtHPWM0cHyiFYXo24Y6lrjExb33-KjRwCjJw2UXKk4d-SJK7wt7JxbRAz862H_-iERUiCwNTvLx2bSC14TlDnI_nY0aX-oyuKNZ5xpJHDXYOu8-kd7cof5J-pAUFvQ76ixclK4D_3f1dijayo7Q34LFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HRBlVcqnsfiH5ifbFbOEyIjallORNpozwvLPtnQrcm5983wLnIC5xzLEg8u9kGXL3YrwYhNieAW5t8HbtmDL1n478nR7cDcFihi64c72x-KarqF9fPzlSrgHAAUfyuJOj84UdRopolcz2NVhM34_9cm0MAxi_hoduevPS9byRyB4FdAav30yB8YkPwkZUibk_1rL8iPRv6mAhG3z-F9kW2k8-jA-MYMkgbw4ihFMkwPYjqT2_VpnP2yzAmxe0Mw_59qUygHwuz0NuxQqgjgN0pWBPC3t4Q_yUGUvAG24CShBJk-sWQrAvR-PJL7c7Jy1pmT1H1hW7oI6Eg9X-J0_IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyL8obqJIdQcgisEE2iMc9qjbZPDndm5_VVBqHrYeBw412TuQwZ_BgSqiP_1qR1lBedl0G0iI0OHeNdUWU-yaYnWUJfl-Sig4hF14bFp1AcLqDG-480aoa4ioxpmlLpTFo7s27sVQeCY9Z5_V_abJxBLFmEVlqSMOXDP2V6OcaUmUnARuOZFNtf9hjoOxMrQfPcyoA3aOw0aVsa9xx6X1VnJsg1jxzGk8xFlr7DWrLE-KY8nkgCWySeDzn7_tAwFvXiPaGBQd6dGqNSTmUUYzc2-SVTSUiZri51702mz4Z9YpMGb_VswzZe8FokCprtNa8xa3fWu3Gnx4ExMdg1P1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cy4N0FNxAd_aCA6KxlIWOK05kJvcyT9Vukceps6f8JWlfwPmjQZUFByJuVe7WbxQSAWwOM31H8ut96gvPbumbbMgyBdUb8IXniqNq0T74g0kefYjRg5x_eB4O7tKHQbcv370yMPq3cpnitqJpj5zLk6u3KKPqha7HchHZ56EQKb-9gaprW85Ca4M5YJq9uvNjMA32jqA-R6z9c88bcXSyY8O_ZqEjvhrrWKk8RWaoM1_ZlYv20jTH1kt8otSiyVUAp5uc0QKuiGjgS9gzTFCRCWlmD2b6EtjO9_0zTQNAvVXsQpGWN6gbjub3qcKm5owFZbJZ3RZOBMm1_2wfD9_uQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روایت یک جراح از سلاخی بی‌صدای سیستم درمان در روزهای جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5694" target="_blank">📅 20:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5693">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏بیانیه وزارت امور خارجه ج‌ا درباره نتایج مذاکرات با جی‌دی ونس:
‏ما یک واحد کنترل درگیری‌ها برای تثبیت خطوط جبهه در خاورمیانه، از جمله لبنان، ایجاد کرده‌ایم.
‏یک کانال ارتباطی اضطراری (هات‌لاین) ایجاد شده است که از طریق آن در صورت بروز مشکل در تنگه هرمز می‌توان با ایران تماس گرفت.
‏یک کارگروه درباره پرونده هسته‌ای تشکیل شده است که بلافاصله پس از اجرای کامل بند ۱۳ توافق توسط ایالات متحده، کار خود را آغاز خواهد کرد.
‏ما با قطر توافقی درباره آزادسازی دارایی‌های بلوکه‌شده ایران امضا کرده‌ایم.
‏ما اسنادی از ایالات متحده دریافت کرده‌ایم که به ما اجازه می‌دهد به مدت ۶۰ روز نفت، گاز و محصولات پتروشیمی را بدون تحریم به فروش برسانیم.»</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5693" target="_blank">📅 15:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5692">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏نورالدین الدغیر خبرنگار الجزیره در تهران درمورد نتایج مذاکرات سوئیس:
‏ایجاد سازوکاری نظارتی درباره لبنان با نام «واحد نظارت بر درگیری» با حضور لبنان، واشنگتن، قطر و ایران
‏· به‌منظور تضمین بازگشایی تدریجی تنگهٔ هرمز، مقرر شد خط ارتباطی مستقیم (خط داغ) برای مواقع بروز هرگونه مشکل ایجاد شود.
‏امضای یادداشت تفاهم میان ایران و قطر دربارهٔ اجرای آزادسازی دارایی‌های بلوکه‌شدهٔ ایران
‏· وزارت خزانه‌داری آمریکا (OFAC) معافیت‌های ۶۰ روزه برای نفت و پتروشیمی صادر کرد
‏· تشکیل سه کمیته (هسته‌ای، تحریم‌ها و نظارت) برای مذاکرات ۶۰ روزه/انتخاب</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5692" target="_blank">📅 12:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5691">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpamAoHJk3kpRsgWalM1bdjVj2WAsVqQDvSWvC7JrfKEJ1VQv2fqNBDpM0A45EMxuSpdNRM_30_AWEXugElhN002Me5h_YU1h_rmTUF9N3IV_lbixSd-hb9SLGCYef86kVjgsBWRo2Nw-lp0HTVCoilyZ_r9XNyEjm2tCqZnRbJbmCes1a5BaTECReXU8YuFzy08TbxZRBh-s5UxQAo2INLC-gZB8vqMkVYxD1uXA9jDy6ydW7rgYjnMWEIB3BglsBZJOepA16-sesKY-Ir_9auyWlZ0zp2G6HZImMUhIPU0pAKn13_KcjB8v5aFMnh8Eo8ZV9s1B3vTVUSqBhiy0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دوباره از ایتالیا انتقاد کرده
که چرا علیه حکومت جمهوری اسلامی
کنار ما نبودید.
این انتقادها و حرف‌ها  شاید ۲ ماه پیش،
۳ ماه پیش یک معنایی داشت!
حالا با اسرائیل که کنارت بود چی کار کردی؟
خودت که «ناوگان بزرگی» داریم!
و بزرگ‌ترین ارتش دنیا دستت بود
چی کار کردی؟ مارکو روبیو وزیر خارجه‌ات حتی صحبت هم نمیکنه!
که توی بازی‌ای که تو درست کردی آلوده نشه!
بی‌آبرو نشه!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5691" target="_blank">📅 00:01 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5690">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZV72w_oqcyZ-2v_JLYjMt8E7nzXjhZ6wOF-wgGPKyArJJA4TJmN9RsUdlw4_Su04vKiq20Ic6RGrEtVNnlBhsX8LTxqT11Rm_y6gdmcOLFBvAeiuySQFIgms9rB_1G4Y7AZzLuvw38Q8H7RZl5lXt0WX6K9IK4bKIkdOcR1I0izhJ6XopSPG8Rzp4Vx2oDaiiD2hyP6N16S-Rl4PJ8U1gTJrhSj1LNnKQ-puEnN407V9Dj4JA18mVPuUsv3drBEFXh8QHUP99qjXenPvT4NdTRNO1P94PI-GdRS8i1ebvtb3bvqqKTAnjQrscafP-SktA2d1jblD0L1zmwzrQN7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5690" target="_blank">📅 23:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5689">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
گزارشی از شنیده شدن صدای یک انفجار قدرتمند در دوحه پایتخت قطر</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5689" target="_blank">📅 23:21 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5688">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oENcyf2EkVsE9F4LBecwWl_V-mUsSAaIPGpRvvu3_0nZdlm6vdLrE5b2X9WaIM3uh_979SZLfMLEoUe82nth0oVsCkUGKK8YYBbUoDOH7_CUK6jXgLqPxtjVLrFMnYIaZpdHP1a8_Viqmu4uVteV4R0YkDCI6cemUsRsYtl3TT3qVNwHIIQrmAOPDF2Covl3atwkMpZlVORLHPPZ6BjYCUZzKLPo1y6xCw_Dr2VmsKvvg9Wq-l8dkshJJt12XYaP-l40aB6CTW2oorCayhSe4nyfBFZLgbMxl5msQ9qsN21rVCv1UV5JJUsPGmHuU1_2jPzBEc3D9WaielqJ2bsbQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاه لس‌آنجلس</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5688" target="_blank">📅 22:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5687">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBEPRN4GZqq3pQF2A47IT8ZQJorADM_oagt3w74yFSUEl8PYYIrZD5LffhgrkQWO6E7x8tQ1ItwXt2gPeY30PJqOX0ibVIHjK1y36xWszONOyYulR1qkSSJB7ni-CxvdeGQrSbCW5_E2Jps_EUCcGxamiRqt-97JyNvJYaotSDRh_EBnjtRLt8lvhd9eQ11kLALQWsdeUs8ke7A2OfkAUS0pnLGA3Qr-Yi5UAT3WuVrJPGB9hmdbPaEl_ls9g3Jwsy4YCXLP5gTRUz6EQFUIZ-7TEZa-HKVPlQ7YZtSBlQenQXgN7d0r0vQOo3iOLQVIU4L9Mc5-fycwjOmLl0F7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان و قطر از ترامپ خواستن
یک توییت بزنه تا دل شغال طرقبه راضی بشه.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5687" target="_blank">📅 22:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5686">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN904SE4Pyc6Cr6GSqQ7gcDqjIbf3oj94tMcctIShk98lYoHR8xfqzS4c1q9CfcwrqehMcUGuQpZXh_kAw0ticQvduYD9nXJAp8bfW4zXLFl5LYRGUqc0urqlZIw0HbP1WiF6MXVuJPn4OVFt3drShbFAV_cNzv_yJc3xnzDISM_i97Hhib0AEzqR4ALiacA3hm0StKDfj8k3_rp-ueB39sTOzfRw6ffsWxvSc1WuL6G5sieTvVrTxF4CprQnGfys1w3vYp5yG8NT3oTDzaq82Vs9zLMgnO1q9SF2HBt7iFS317-p8NEcsC4Y8SpyYdMV61cqp77o8kdDre1rKb8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس و امام قالیباف</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5686" target="_blank">📅 22:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5685">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H45_XCa0Km84r4FsYsLf_Aw4uz6_o-pIQfKylkZrX8FDWWuGeOXw_FaJo8EC5ZUMqUnwCBFvQnasCjecar_fiiqCd_bqwxQ__6naO1xM95H6Fz5ZpMOuTy78UjiubwqokzxWF2viGDJk5XZkkSh_5PYXIDHk-jS3YxShMqb8dtBGi4qap_k2FZrd6vVDa66KmDQvpLjg92A9KhiZm5oVp6_zeAUs5MoU1os0JPWwyvqMCflIte7wk--Mj5VYz6hsRxpT2HSA0QLY7UcWg4gEWkqR5qUPm_1SlCRvGVwjls6EUtzfE_o0HPV7gRSeMP2Kz2cVJGvyRK259fGPujxEIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل از حذف «زکی یوسف محمود ابومصطفی» از اعضای تروریست حماس خبر داد.
او در ۷ اکتبر به اسرائیل حمله کرد و از جمله «یاگیل یعقوب» ۱۲ ساله را ربود.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5685" target="_blank">📅 21:50 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
