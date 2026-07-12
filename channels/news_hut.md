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
<img src="https://cdn4.telesco.pe/file/R40UbZuKXA7oHquC-G2mIX8M-XVY2G5K45mKiYWzmyM7Y8IC8aF2lKcOZKgPfQOhstpgzVBR84thxhnEadibitDgChbtUtpP0y7kzdVPWLkNL4pbosr9P5SN00hk0GFDiztVgAXU9SFR3MIM4wb8CwxTMKTnSbvWD4YfpxVIf5NU52RKCNZAYm46QpU9uTRmQn9AL6naKhUbevfmlH6QOUphOr-ChHMXJIPZPsOt5mL8yja3Isj8jFPcjw5FaIOPJrXqjqKeUX2qVogNzpFGSinYqLAe52_VYS7NoXiGTMcPsX_lP4g4se35PFVZL01yXA7KHth-kSkokaNx0LMZtA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 181K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 11:09:31</div>
<hr>

<div class="tg-post" id="msg-67893">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5JO8oj6TiPXfxFXFBEuLvRR2Bsuy94cEGAXykRSA8cSSKRZgQIMLhJshrS3Q-oyEmr8H400ayLSp9v4tC7lGeCNC9Q0DVt_n-d-OIvTPIhv1zVGCLDQTiZrCIamQYMKZSOesEEg5C2msFvjd0KXB03mtXO-M6G0Jj9BX30NKyei9Mux2LHFV_Nqojlac9BvbgVQIN89ttbiVBYk6v-gWzQIeyB3-IyFQDVXUrAxOfQltC_2YAH4Zc9glqexmN9YwJnkWLYMQwlGujeQ3dg8Wkuh0-6qxMNGUsWJ3pEQb9KwS-F3WSv1kAXtpVCjl9bpeH56Ig-XFb5fkUYGDH0kdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ:
سناتور لیندی گراهام، یکی از بزرگترین شخصیت‌ها و سناتورهایی که تا به حال می‌شناختم، از دنیا رفت. او همیشه فعال بود و یک آمریکایی واقعی بود. ما لیندی را بسیار دلتنگ خواهیم شد. جزئیات و برنامه‌های مراسم تشییع پیکر او متعاقباً اعلام خواهد شد. چه خبر غم‌انگیزی!
@News_Hut</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/news_hut/67893" target="_blank">📅 10:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67892">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDxQXll24mOFqniywF86zHqRxVkVRtLfGz6kh33rdtqOYUSN4kmNh2NkmZRKTrF8DTUISOULKLrca2BejnbnfV69vdDUqqyjNVn8NZOMjhPlOs0WW9gfhdQ0ajKovNPyRPDmQ02BCSVejSSRpx0PAYUX1E0uetnpZg8DMFetJAItkOVbGrSNeymMr4kfgmlHiVswpPch_7VDETiU_-S6ML10PN1g-iQCO2UKbISlb8cxk9Gnr3JxcxNrfVQz9n5FGPjr607dc6UQFeWCc6MhwmjNAHs2Tz-4nL3FhTE4S5XSUPgtbovAKvpbbNq-mCFKWJyGUKWB0amDAULUehCOWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ان‌بی‌سی‌ نیوز:
در حال بررسی صدای ضبط شده از بی‌سیم پلیس مربوط به واکنش نیروهای امدادی به یک مورد ایست قلبی در خانه لیندسی گراهام است.
این شبکه همچنین گزارش می‌دهد که عکس‌هایی از شخصی دریافت کرده است که به احتمال زیاد لیندسی گراهام است و او را روی برانکارد از خانه خارج میکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/67892" target="_blank">📅 10:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67891">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CB61_-4et-npGTWkU8NgnGhAPRZkL6pKlsoj619ZtOvrqSHNw449PhnBFTsWk4MFHyp0soElm2Cw6JWHJdzey3raaxY8UvF5QFU9kz4z-SGQevsjfgFWneJ2Opoyiy_66t0BbHYP6Av3S9F9l8ls5UuXd9A6E4qKy-q67dSyphukUokdJVt7XR8bdrIRndcnYBZrP71RhcILiBbEuN-j-p2xATpBlaJ1ft42EXMslMxTFk4RaX2XwvKReC4LP0OqILPXmJ8ZNTswX3ZfKWm9bVqIaJ4ydUD8n0fjXhb4WgYJLQhcL2BW8u-Si7X2sran_uJiYiliUySlxtQ7O-0EJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#RIP, great man
🫡
🖤
#hjAly‌</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67891" target="_blank">📅 10:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67890">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHG_1B8n8RvtXkKBE7rWeTqDsRP47F56MLCmeLzAlNbXj6NZS05ytPJeYT0HNrpuwypBAS-IbtmUyOfWRs-66qyL-A12KAAQVmKNcS0daiDN6mPl1n1yIG4XpqWjyBcTWug5dcwclj7EvKv7jhagHTfdp8z9oK_BllCFS1VU-W_vDMpBd5bODeBj2Ae80OPzfJn6RQItkAzdTSpCbkcSBbo4ye8piJ9pIAjDUtJPS5C5Fkt-1t5HiRKpHviNSYR1kh2WH8555W2PbdPjFz5EknO3F30i5AFwobZi96Gk71-rSzezGNVRUL_Ej-66qO3FifJOWvbP_o2859JOnMwvsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:   دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت.  @News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67890" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67889">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJTJxusanixgKxANJOn2Z8UqavpcDW4MrKxUrX_2sIeDHRr-KJATF76LAnp7DM0ntAzU62wbf3G7JBgZMaGsnu-qODMXxfbD9gNghxP40zC8Nqd3Zx413lHp7B76yfILIzJKi6grFO8_Z1dn7Jx_fYGvvwfYdf-xa1Cr-aibGDmHJLBRsTnXoCtBLCQ46d4HyAwIgo_XCdWtRyiUXmfWQUdmtHaUT_W10JgPOcpLdO2Fq7n3aPD0iUXC62rs5GLfqn661mp5sXJrLV8Xpdp2s2X_phA_Xa59-F7L7ooGBoWNWcJUlMcamLX37nVgwqQXSnLGQiNuODckzPyyzDwBBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
بیانیه دفتر سناتور لیندسی گراهام:
دفتر لیندزی گراهام، سناتور ارشد جمهوری‌خواه، اعلام کرد که او شامگاه شنبه پس از یک بیماری کوتاه و ناگهانی درگذشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/67889" target="_blank">📅 09:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67887">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVMjXNhhi-NHuR80GLac8HYbXdzZy4spU5MQTiUwUyeX_wzM8lpYXw7V_WS5BWkBnrLyiIRPkIFujiU17WCa8otAUCUWP4foQIhTbtqoN39ihmQHmFMEBXvj_6Mi4683ivFY6ajKGk1mNtPs23iThd1Ozfg14VpgLcdG2H1VTjFQon8e0u2lhsQoDPAIkg21KLl1QzEuYXTMABJTr_cD1vhkV_x39k3oCpX_OS-3QyRMhnqLCqd5EfO-0j_mvVMvM8BF3_tC31EDdYmRdzQ6GEoouxrx7NF8opaxbJOTG7pLL9lP076KeiQEqYyIzyYO2NioMsX5VkWLRpN_pBVxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#فوری
؛
لیندسی گراهام سناتور جمهوری‌خواه آمریکایی و از حامیان انقلاب شیر و خورشید درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/67887" target="_blank">📅 09:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67886">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
تصاویری که سپاه از حمله به پایگاه های آمریکایی در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/67886" target="_blank">📅 09:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67885">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AHAG5g2pJwwfcSRYzYvdvxbPDeusJAvZwJTWau0Wir2Q2VxNwG4S3pYe5i8bcSPkqBeg8avnIuDEa7VbHvypthz817HOyQDBGZYmTTMj9dnMHpfqLfQ2066r4jBFOMqUZtW58dNP9J9K2HsA5I3W9ZebrPBFNxQOS-Shs8DVhRwWoqzUrnZ-h6h4oXnFzNlOwpnnOs90MGeeZWgH1WGcTuETNiheyG9wsj18ACj2PGDZRQzM7bHJxIIBFU4SpIbnyzFB_y5N5Pk7eWmstYmV9drN1wwVJLPzj6RdaYqMFBXqt45p7ehvkeeq60Lr1DhImtpj-3FCmfCgNJdnZaMAxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/51a23206ab.mp4?token=AHAG5g2pJwwfcSRYzYvdvxbPDeusJAvZwJTWau0Wir2Q2VxNwG4S3pYe5i8bcSPkqBeg8avnIuDEa7VbHvypthz817HOyQDBGZYmTTMj9dnMHpfqLfQ2066r4jBFOMqUZtW58dNP9J9K2HsA5I3W9ZebrPBFNxQOS-Shs8DVhRwWoqzUrnZ-h6h4oXnFzNlOwpnnOs90MGeeZWgH1WGcTuETNiheyG9wsj18ACj2PGDZRQzM7bHJxIIBFU4SpIbnyzFB_y5N5Pk7eWmstYmV9drN1wwVJLPzj6RdaYqMFBXqt45p7ehvkeeq60Lr1DhImtpj-3FCmfCgNJdnZaMAxYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سرباز روس خودشو به موش مردگی زده تا کوادکوپتر اوکراینی شکارش نکنه
اپراتور اوکراینی میگه: «نگاه کن لعنتی طوری نقش بازی میکنه که دی کاپریو جلوش کم میاره»
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67885" target="_blank">📅 09:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7O7-qLkfYWOHBltPeXc3djqJb35nVjJzjPYJvxVRzFqV85_lr5HvDbirnm4MdlN8IPKFxqQ2iPBJAanOVHNAgGucLeVZbnpA4oFKHRXaMGJ5bWuPU237nSPdMDEO_uT1utycWaZnph5RMQz-zWGHpdJ-MAEG9CbPk64cJIAC7AAhd1vO-n5Dm3eafE-sU-v_Tu4dKb7Vjv_DmMyoN86TK9ePKPYWy2lHCQ-c4uwvFKzJJIg_9l9zAkpw_Fp6hleY-SUSRImppCotZVm_qAiaDX3J5RA-H6esKu4zmqTAbkz9SGLTKHxXHE-vZxJUfmemkmwFQzz5_FLDi7ExgXXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ادامه حملات سپاه به کشور قطر
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67883" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67882">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=Vwwq4dwz5DdAgQX8ZLqKwRW12bRWxviA2T_ZVLQBA1Hh94H3qAbFH81uULOvmUHElafW_rD_zcu2KVmLQJZzggZA6sfSbTGZqMm1f4QN2VUY25L1QYA4DepYUC3IDHlbuvmZjARiikXx4KUG2V40QzQMOYT3_YqdJ0SAjMc0Y1MFo4H9Ph6ZcmC3HuKhD5r33rb7NuP0_MvlDBK2kD78Q_dJ45cbXWb_UqjERSzYCJ83ipb3D3iPe1IVwwTry2Xpn0gwlv3DCnJ5M4H8e54pReTY0odfnPhsR5fdU-8-mBw_B-EqknLhnrZUayJ4LVCLtlNz0DuTRJ4cT-oyt4UIEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=Vwwq4dwz5DdAgQX8ZLqKwRW12bRWxviA2T_ZVLQBA1Hh94H3qAbFH81uULOvmUHElafW_rD_zcu2KVmLQJZzggZA6sfSbTGZqMm1f4QN2VUY25L1QYA4DepYUC3IDHlbuvmZjARiikXx4KUG2V40QzQMOYT3_YqdJ0SAjMc0Y1MFo4H9Ph6ZcmC3HuKhD5r33rb7NuP0_MvlDBK2kD78Q_dJ45cbXWb_UqjERSzYCJ83ipb3D3iPe1IVwwTry2Xpn0gwlv3DCnJ5M4H8e54pReTY0odfnPhsR5fdU-8-mBw_B-EqknLhnrZUayJ4LVCLtlNz0DuTRJ4cT-oyt4UIEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
تقابل سامانه پاتریوت در قطر با موشک‌های شلیک شده سپاه پاسداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67880" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67879">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=nSh6pJBIsNlLSwlVbFeE5FLzqWz628rCtUt8BEFD78wohB1UGmK3TCVjG86QJeHyX30FenPgRylxE3lCffJdLe6ocnci2pA1DRaRkfNnzlHpX6jZ9L0gmdqQI9XLN3z9VlA5veynnpSG2JOFVMpA8zxIYpyyp4aWfHLMRyvu1yDGgzsJdlm30kZ2ia9I2wLDPzrP_8zNLXuEAfoOvzfmLK3WGEaChIeftzH0HTFCY51v7TTSacZLBwQblq1FuzzjTL1lBk4oDwShpTZNv33DC-DCedPWwgBYM4Lt_lcUch_LkOAO-aCKNB2nSco9Pm6qYmsJ4V7whqbjV9W-bpUACQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=nSh6pJBIsNlLSwlVbFeE5FLzqWz628rCtUt8BEFD78wohB1UGmK3TCVjG86QJeHyX30FenPgRylxE3lCffJdLe6ocnci2pA1DRaRkfNnzlHpX6jZ9L0gmdqQI9XLN3z9VlA5veynnpSG2JOFVMpA8zxIYpyyp4aWfHLMRyvu1yDGgzsJdlm30kZ2ia9I2wLDPzrP_8zNLXuEAfoOvzfmLK3WGEaChIeftzH0HTFCY51v7TTSacZLBwQblq1FuzzjTL1lBk4oDwShpTZNv33DC-DCedPWwgBYM4Lt_lcUch_LkOAO-aCKNB2nSco9Pm6qYmsJ4V7whqbjV9W-bpUACQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67875">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
😍
🔵
برداشت آنی
👌🏼
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67875" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67874">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2hsyane3XEPNEsG2LlSqlWJmRsZwTNbo-yE4CcFWZJ9MbA39BxPIMZvQqwsq9Vrl6QxC-FRK_8u8d8XM_DF-c8YyTFD5pivHBIq0aPXw36xsK_uYblI4BnyN8zqkXvQb8Zd9pv2Dn7UTlCWZiIEfj6EFDqOMh7kZLcBh7hmKu34mkeqPBBF-Ui691u0iiY57yMAM773n91kynupOYwlcjelYSRJi89qiQ2xHdiaXza5dWpblv5ygXUH_d8uvCvp3XgJf1LWkx8sz9qxnwj5MiEGzT9mfwOLuVJEKPFEjVA0ZtOo3GzdFYJgfbIbWDJk4GoXE5VyECuLcdDcadLfxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تنها سایتی که توی جام جهانی هوای مردم‌ رو‌داشته تا باخت سنگین ندن
⛔
📣
خودم بدون نگرانی از باخت شرط میبندم با کمترین استرس
🛍
از این لحظه 20% شارژ اضافی همیشگی یعنی به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان بدون قیدو شرط میده
💰
🤩
🤩
درصد هم برگشت وجه در  صورت باخت،دیگه چی میخوای؟!
🌐
betinja.bet
🌐
betinja.bet
کانال هدایا
a20
@betinjabet</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67874" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67873">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaRDi0U6p-B7CoKTA_bF7zuxt6Z4v9jX4c6NnYmmDQovnGge-v5KKdCZxn2MLGmgJTL72FlUhWM6GArfK-FVFCqcbxYf4zLjdWZ6nkm4Ww597s_s1vqbAnlz_aamZXCweWfvKR0gLRAbzY8Wwe3cKV5Z4uX3ozTrcItyqCCp7y5jE0C6Dzq_gAtqquAl3KOw2urdxvZZOPQJ8lWFJFAwGJgmUe-8bFRTBAgpLz60e34OnE9eb-rq4eMAWryUx-4wN7G6datWoCb22Y4dp7hZNB7tAQF1kfsi4F7IM0CthK6eNOoanMoS7pLfrVvpV0cBQljSChhtSJ5HzpuQrPMmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/news_hut/67873" target="_blank">📅 04:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67872">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نتانیاهو: تو جام جهانی طرفدار آرژانتیم،</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67872" target="_blank">📅 04:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67871">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپمپ بنزین</strong></div>
<div class="tg-text">ما که منتظریم اقا
❤️</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67871" target="_blank">📅 03:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67870">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67870" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67869">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67869" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67868">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
هرگونه خبری مبنی به حمله به تهران یا فعال شدن پدافند تهران کاملا فیکه
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67868" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67867">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گروهمونو که دارین؟
😴
https://t.me/+5NElXlQWt_05OTlk</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67867" target="_blank">📅 03:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67866">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=G1-bSYBBgRiJRmXLv4TZkQyM6ufL7lO5z_1M5Zvonf99hshwCgZrcJiiy_J1Yo57zD7L_QDNoVU0TYiBTfWOEOORyo0dC9CDEucKbSh4-yyt1EwpJ6BZvQPlUF8NswcX2E7_CBwYpDY_2KeNpdK4wpYn6VYDC_jsP6YJr9J_EUQDNwu_lkcVq02gQnVyS4n4vQIVI-lVn3gJmEXqetjIY_lGPP_PrWzDatoCqjgwjrf6Pg0UcxJlJpj8H7Hs9cbx8xwe3fxGiZA27xateFOqfkGdUV6jParmuPG8CQAK3N0PwxeNwS5MuY8jOHVpalmbthvBar1fC8Y27vQYrsb_xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=G1-bSYBBgRiJRmXLv4TZkQyM6ufL7lO5z_1M5Zvonf99hshwCgZrcJiiy_J1Yo57zD7L_QDNoVU0TYiBTfWOEOORyo0dC9CDEucKbSh4-yyt1EwpJ6BZvQPlUF8NswcX2E7_CBwYpDY_2KeNpdK4wpYn6VYDC_jsP6YJr9J_EUQDNwu_lkcVq02gQnVyS4n4vQIVI-lVn3gJmEXqetjIY_lGPP_PrWzDatoCqjgwjrf6Pg0UcxJlJpj8H7Hs9cbx8xwe3fxGiZA27xateFOqfkGdUV6jParmuPG8CQAK3N0PwxeNwS5MuY8jOHVpalmbthvBar1fC8Y27vQYrsb_xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی  جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67866" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67865">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRazis</strong></div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی
جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67865" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67864">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/67864" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67863">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝒕𝒆𝒏𝒂</strong></div>
<div class="tg-text">آخرین باری که کل کشور باهم دینی خوندیم رئیس جمهور مملکتو خرس خورد
امسالم که اینجوری شد
فکرکنم سال دیگه انقلاب شه
😂</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67863" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67862">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oe2XOtjva2LB2VGq5jhgJ6e3W2oV-i5dP5Ys_Ow3pZoYi-QacAp0X0pikEuK6wSgPdeNMOr70toD2lFtT2_tHZs02P5V0Rx2bzelub1dFME6p7YH1Jt0rg7OpAlCbjPdiQRrrL-Txz4UZOHxrpd-QL7NjqaK7Vd4UbxjFdeNuRaRs2amQQjww7r5s2xqg3bqmQRbRDOZf43Eeig4WKyW9ut6yGcoOX9n07ZlqLYGlq3eXYfyk-S6aFXqkxYhuUIEY0a4DRcv6d_Vwp7p-UbJyHtCjy1GhQiPM5E-SvnSKEEvVsK0p9qAtTciqa-zw30LDw77hFwWXEpKOP7ujjcF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقیش اینه به تعویق بیفته حداقلِ حداقل تو جنوب کشور، ولی اینطور کل سیستم امتحانات نهایی بهم می‌ریزه و باید بخش هاییش داخلی بشه، و البته با این مسئولایی که ما داریم چنین چیزی بعیده #hjAly‌</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67862" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67861">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0s2EJQl8mBGjPPHWRpD_f5pVYCrAfSOQ8Oa9U-KcRn0F4UwloNa4C4Vl9DgJk47vfdrkqfr8asoVKAcKVfZE40tx9vcZzouc3_xkvErRnkUNzvIofevoLIM3EKhSxkS43KmiLO_jZpsalE9rya7YZ9Tf0FUTKuF-4QS7NJEvb4v_SxHFHXIdlEMjHbaKRP7V500N5gfXuesCPHhX08tE3VnZPuzEZKH_Npdgel4auwI6fw7Y1G0LMa_ItQCHaU4SzZm7zfh8p5cg0ppZEh973-jRkg5ZAxhO3zIxWTeeosHXIG8EgwbjuRP0aKtOQ0wrM3adjYa7FjNhVmP7ZJiIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه #hjAly‌</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67861" target="_blank">📅 03:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67860">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6Z9kSKba2meQT5sfvRkBhSiZHElg6VTi3NP3yuchE4iOSoSHyNsRuYaFhshT660dMPZAr8Lm2KJ4PYN_c1M9tSAvkFw-wa7mA4_wm6uIA_Z4wNo6hK5IbBCDB9U2Jh-sLekvF5hMuNI6PwLqnsDeHxj5jRdAiuDBuijIWmlUftEmMKxsRH2crMMZAmIHzweeWXwSzJ1WQxZxPj9FaN3KGvWVqzwtCmObIoLAZ00LLjpSa9-hIe7nFc7--ntYTDcRompVT9UE5AytheI4NYnF_2nXoYt0_vjRfNUSaAU7etI2zriMcmq8WwZCbCH9hpo1yYaAlJsYe7XPMCN5H6IBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67860" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67859">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-N8U6nSJv4H97nSZuVOP6M4hubJBk3iNSCil--J0aouiTKk75NS5YgsLsk4khAWNrwiN9PTZtzbv1Ra4G7_vRcZkAUD9O1RXgjilAd56RZQ-3iMCjNS89KJ7zxx9_S8warI3bpWtl2OBlJ74JquLWWolvao4uwK_JI9lXCP8cgTt9GyF2TLE__Ckld0KqCqpsJlNpNPwFJcFTabDSdbeFBPvM_iebi4bSs-lEqIOd7gJW3O0SkthyqNWps-yl_JYfKjCKVfI2CFb9trcciUUc9pVowJhbaacdqAKMv-yYYvxUfX1S-epkkOGppBJ_2ufbcTebVxvnzeGRpm8Ius1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:  ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.  @News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67859" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67858">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
نایا:
دو انفجاری که در جزیره قشم شنیده شد، نتیجه درگیری‌هایی در آب‌های خلیج فارس بود.
نیروی دریایی سپاه پاسداران انقلاب اسلامی و ارتش ایران با ناوهای جنگی آمریکایی درگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/67858" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67857">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
دو انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67857" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67856">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=SIgO08EJTLNZaKnrECbrRM2o4_nGVv30rErXoejZJHjboSO2pUoaWJV73RY88fK2IaTVEkbEfZXcdoJ0ez7ElrUR7s1AvH03UcHy5kT1MZUzlmQoQ7Bqc6_9Y39ng6iYpIEzOVexGQF0rUTgFIeBrlg3HksR2J9r3vKyAkoqbAkPBxLkQIH_GZSTAwvywdBUjXuklP1gpsJ-5kklGQE5bzvOXg9wph0w-qXwB7RpQ1-6abt0dES3Ipv9PE3DNfN4bvS7PPlS-Q2ISoLwspCRcePsNJTySkMGvyOJ6xL-02Z9FMNg3BA2ih0WXFNBguWSKWwhdRHV4W_sVOCC5N_c9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=SIgO08EJTLNZaKnrECbrRM2o4_nGVv30rErXoejZJHjboSO2pUoaWJV73RY88fK2IaTVEkbEfZXcdoJ0ez7ElrUR7s1AvH03UcHy5kT1MZUzlmQoQ7Bqc6_9Y39ng6iYpIEzOVexGQF0rUTgFIeBrlg3HksR2J9r3vKyAkoqbAkPBxLkQIH_GZSTAwvywdBUjXuklP1gpsJ-5kklGQE5bzvOXg9wph0w-qXwB7RpQ1-6abt0dES3Ipv9PE3DNfN4bvS7PPlS-Q2ISoLwspCRcePsNJTySkMGvyOJ6xL-02Z9FMNg3BA2ih0WXFNBguWSKWwhdRHV4W_sVOCC5N_c9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فارس:
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67856" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67855">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صدا و سیما در عسلویه: صدای ۴ انفجار در این منطقه شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67855" target="_blank">📅 03:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67854">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
چابهار رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67854" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67853">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
❌
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67853" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67852">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCJeuNd1Y0qUVS4einezdVbs5CJi9pzw5cFJi531_1LmGu7U0733uXkPaCqArR1LTqZ5YrzqdvwigLHvLZez20P_j-vtLaJT9CcCayyYEPQXECb9_bRb-E1ZLme_H8yQLNmpM8qymAZLm4hIOyJPcCJCUE0td5XPpoduovy2FABaBzchtWzXu-KKZUTPeqdNBYnX0uyO9izLge8yGpRHTIlITrc1CFB9ITpLknlOgi67scBYgItpDzBM-gtc1WYzr7zToRtg2dFCIMSuGxV4CldLmYBjC1Q2lvtc5V2yOf46aEh4i605BXGWHlwMGpr_9ENVja5y8qEx2g5ugNMJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:
ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67852" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67851">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=oK7sYIVHi0FhBTPcKdtjfkrZY5SFih1FNzEinYSEyHmkhK5EEJZlJZiV2eM4gOUw1Rjf0IQg-BAnlhjzN-kYSlPnfrUf_DcgIjgn3tAHW_UajOy17MP3um2flRzlgvywKYT09p9q49qMuV2Ahe1T7k56rRkZmhsq3a_ZrbQUJ2zxPLhPz75amc3nDuf7MLKZWaZRRAI20nkk875pZK29oIDRYpXegQ8TkdvddJgpjz_x06CwnQPxHJ6gNlzNRJiwJ7wmLm-jUdUTYGXq6rzergcQgmzIihzX2guun-DqRDS_xyqSaiRhYiDTRID9tV_WwFESs7qeJfMQ1jKKl4k7wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=oK7sYIVHi0FhBTPcKdtjfkrZY5SFih1FNzEinYSEyHmkhK5EEJZlJZiV2eM4gOUw1Rjf0IQg-BAnlhjzN-kYSlPnfrUf_DcgIjgn3tAHW_UajOy17MP3um2flRzlgvywKYT09p9q49qMuV2Ahe1T7k56rRkZmhsq3a_ZrbQUJ2zxPLhPz75amc3nDuf7MLKZWaZRRAI20nkk875pZK29oIDRYpXegQ8TkdvddJgpjz_x06CwnQPxHJ6gNlzNRJiwJ7wmLm-jUdUTYGXq6rzergcQgmzIihzX2guun-DqRDS_xyqSaiRhYiDTRID9tV_WwFESs7qeJfMQ1jKKl4k7wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شلیک موشک های آمریکایی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67851" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67850">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام):
ساعت 7:15 بعد از ظهر امروز پس از اینکه نیروهای سپاه پاسداران انقلاب اسلامی به یک کشتی کانتینری با پرچم قبرس که از تنگه هرمز عبور می کرد، M/V GFS Galaxy که در حال عبور از تنگه هرمز بود، به طور آشکار، نیروهای فرماندهی مرکزی ایالات متحده، سومین دور حملات خود را علیه ایران آغاز کردند. یکی از خدمه غیرنظامی ناپدید شده است و کشتی به دلیل آتش سوزی داخل کشتی و خسارت قابل توجه موتورخانه قادر به ادامه سفر نیست.
ایران فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم پس از پاسخگویی به حملات قبلی به کشتی‌های تجاری در اختیار داشت، اما باز هم شکست خورد.
در پاسخ، ایالات متحده هزینه سنگینی را با ادامه کاهش توانایی ایران برای حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67850" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67849">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=oU3imfjZ-CZna5Wabf0r64umLUxAXb0GK9l4V4KvK0o1U8mtmHhfboNyi--GJaUnBnZO26V_lVV3XkbajXW0zWsjanxc9VjB54KJgaod5bJ8v3Z2ydbv0fUHlLQeMiVtihljUL0qzNL91prZSRNUMPlOwcduQM4TKTVEzKc41VpaXIqupeWTuzfJDF7sgJ7RhTmDyUn5W4wl9J8GJTKIM1SkIebj2YdwoLTCUStfHk0MzX3CiP_iFyyrRoegdYIGc7m4dlNtCl9kcp9UKB47De82OnQ_ujbZ0RFgya9aLar4ocQV4ADCG8-fuEYwyHeVivvS7zN7V5DycSq92ebfqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=oU3imfjZ-CZna5Wabf0r64umLUxAXb0GK9l4V4KvK0o1U8mtmHhfboNyi--GJaUnBnZO26V_lVV3XkbajXW0zWsjanxc9VjB54KJgaod5bJ8v3Z2ydbv0fUHlLQeMiVtihljUL0qzNL91prZSRNUMPlOwcduQM4TKTVEzKc41VpaXIqupeWTuzfJDF7sgJ7RhTmDyUn5W4wl9J8GJTKIM1SkIebj2YdwoLTCUStfHk0MzX3CiP_iFyyrRoegdYIGc7m4dlNtCl9kcp9UKB47De82OnQ_ujbZ0RFgya9aLar4ocQV4ADCG8-fuEYwyHeVivvS7zN7V5DycSq92ebfqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67849" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67848">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
🇮🇷
باراک راوید به نقل از یک مقام ارشد آمریکایی:
ارتش آمریکا در پاسخ به شلیک سپاه به سمت یک کشتی تجاری، چند هدف ایرانی در منطقه تنگه هرمز رو هدف حمله قرار داده .
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67848" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67847">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67847" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67846">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/67846" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67845">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
بوشهر رو بد زدن
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67845" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67844">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67844" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67843">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67843" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67842">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=qq8CW4H0iD_coKKXeSFzs_WHqX_mnA8dn68JZ9Qg-c3bWjXAXQ_fklowdRCkxpIsVYfYMXvtN6eA14nqtYaRSzhfQA1NXrPdCP0Lfknlaal5P1tPjKa9Y2oSBr8f9XRwxr7hOxhhEMoXgqYIQb6eminThnFZFaKnIRcYsWTTpV552AmMBuLQFvsR8j6XI0C9d3FD9CAl7DAKnUqp30yGlAou6BJ6lIF91e9hyWCcJaS-ojbOWAARgNVpQZm9rfp6lqcvNhxEOaPFRnausmQyvJjg99LLBfUEZ7vrYIsdJdJ2AtN1vYBMzZ4loPOsuwe3EH4cbeSwcz2TUecWSwXNeBrNKUbuIimCUA-r4-8arB2X23xeJphAEp6k0UYsybSRlpgQgGadUuRV21wo0zQ9KlLjvQ7g52JyetgfkiVGYv8WEG4CvNWck78AbU6brBVQivXLySfZgXlGerDXio-qxIVPK-LLKIz86fXmx7EpGCUMlZ9oNX_8RnbcajxvcEWTGrAbFgV60wMotZNE4Udw8-N54wxH7ixmcuZN6x4MwYImKZ8FFfKJko4T8H2BrYvkRqQTd1uxrm3nmqfoCI-mGPH_7eS9bjySV0Io4fu1fsinFut32IAXtGJuGhC_DVzMjh-TmyjXzjO4R1NRhgD21UAdKfCIIJeVYNZm5it2dTo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=qq8CW4H0iD_coKKXeSFzs_WHqX_mnA8dn68JZ9Qg-c3bWjXAXQ_fklowdRCkxpIsVYfYMXvtN6eA14nqtYaRSzhfQA1NXrPdCP0Lfknlaal5P1tPjKa9Y2oSBr8f9XRwxr7hOxhhEMoXgqYIQb6eminThnFZFaKnIRcYsWTTpV552AmMBuLQFvsR8j6XI0C9d3FD9CAl7DAKnUqp30yGlAou6BJ6lIF91e9hyWCcJaS-ojbOWAARgNVpQZm9rfp6lqcvNhxEOaPFRnausmQyvJjg99LLBfUEZ7vrYIsdJdJ2AtN1vYBMzZ4loPOsuwe3EH4cbeSwcz2TUecWSwXNeBrNKUbuIimCUA-r4-8arB2X23xeJphAEp6k0UYsybSRlpgQgGadUuRV21wo0zQ9KlLjvQ7g52JyetgfkiVGYv8WEG4CvNWck78AbU6brBVQivXLySfZgXlGerDXio-qxIVPK-LLKIz86fXmx7EpGCUMlZ9oNX_8RnbcajxvcEWTGrAbFgV60wMotZNE4Udw8-N54wxH7ixmcuZN6x4MwYImKZ8FFfKJko4T8H2BrYvkRqQTd1uxrm3nmqfoCI-mGPH_7eS9bjySV0Io4fu1fsinFut32IAXtGJuGhC_DVzMjh-TmyjXzjO4R1NRhgD21UAdKfCIIJeVYNZm5it2dTo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67842" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67841">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-mGWNOX0YnOPd4cjSET_EXjbyBPdABE8bfXe0BKeBX2-TZ0B2HVNLwebPhzLDc5wVQHz0R1x_k0eKm81L_6yxDqBYQCMFqv0PKxQdpILaBnODkI0yZy-3MpjStMYsgBwR9dp0Wuif6Da0gsBxCPNoxtGjLngCkJJoyft0qzGBz1iNUWVTYlgCFdOjJ1PBBlNAoRo5QbRN88ynY5OvtOeqpCx8Oqzac7xq-qr8ZsYHCL4Tei1epv0w9JTet_SFCvk5vw3hdfJsuCFh9oPP_LF0JnUqJmPGIfVR5mWTcQcuiXLWvqwMe25ltM106w7qDoQP1tb1NRcBkVYazj_p6fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به بندر دیر
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67841" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67840">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
چند انفجار شدید در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67840" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67839">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:   من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67839" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67838">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های شدید در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67838" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67837">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=EebxJ-yVxdnKyH396roQAzeyw7Bqlza9YurW4fwy6-RvL47pCr3vly14rfRoEoU3laaojPvj4Ceq7znqzvmn_45FjXaWcaJm5oNYDp20O4wAS9y3re0MdKdwXmDhj0pmOb0fbk1cIzBKs-SoMo7LvpgaVkU1RA3IW6CHkrHWdT9D2QSl9axap4oUcN0mdZo5iGg8m9MaQvUTK6uw2FPLOzqGgz5FURjhA8IT8o1wh3sKQSN_p5HfgUlFrlFHJmuXqbr2WRTNNUSYN7mABdGmNa7u1r_5I_oE1kCB-BMtj0HLMa3xbP3jT0C9hFBf3XdmF7MTQRZwHud8XY-f0UfzfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=EebxJ-yVxdnKyH396roQAzeyw7Bqlza9YurW4fwy6-RvL47pCr3vly14rfRoEoU3laaojPvj4Ceq7znqzvmn_45FjXaWcaJm5oNYDp20O4wAS9y3re0MdKdwXmDhj0pmOb0fbk1cIzBKs-SoMo7LvpgaVkU1RA3IW6CHkrHWdT9D2QSl9axap4oUcN0mdZo5iGg8m9MaQvUTK6uw2FPLOzqGgz5FURjhA8IT8o1wh3sKQSN_p5HfgUlFrlFHJmuXqbr2WRTNNUSYN7mABdGmNa7u1r_5I_oE1kCB-BMtj0HLMa3xbP3jT0C9hFBf3XdmF7MTQRZwHud8XY-f0UfzfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از بحرین به سمت اهدافی در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67837" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67836">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خسته شدیم از این چص‌حملات خدایی، قشنگ بزنید جاکشا
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67836" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67835">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
ارتش آمریکا رسما حملاتش به ایران رو آغاز کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67835" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67834">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از حمله به بندر دیر و بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67834" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67833">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67833" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67832">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش‌های اولیه مبنی بر شنیده شدن صدای انفجار در منطقه عسلویه منتشر شده است. منتظر تایید این خبر هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67832" target="_blank">📅 02:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67831">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=EJrWOtLymFXgvAuK5OQH9wJ6yWYCY9rOB-Baf8EoFsJadL3NNruHsti45dBSiJis99Ey6noHJGYNVPge5tD895MfQDfoNsImzg5n4abTaS0RKI8FBJqDa-jvIs7WuCsorHcPt_sFzwdkEMmaq1yXSxkQhE8ZgxIDY2lLnorPqUpQdJTlD4Z9iJHQHOI9LWuT6EZG0qSr8HGeUildxhZp59urksXIP_UMEvy3sspKsziH9niGni7hc5e6-XhbgDU4g9bhwE4uhxJeZ6y8Wtqs1v_ckWU1zGsbaHMs2KyTkcljL44hmUMsofpREHdsPDiVe4RHcMPemHB3mDxbRyRhHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=EJrWOtLymFXgvAuK5OQH9wJ6yWYCY9rOB-Baf8EoFsJadL3NNruHsti45dBSiJis99Ey6noHJGYNVPge5tD895MfQDfoNsImzg5n4abTaS0RKI8FBJqDa-jvIs7WuCsorHcPt_sFzwdkEMmaq1yXSxkQhE8ZgxIDY2lLnorPqUpQdJTlD4Z9iJHQHOI9LWuT6EZG0qSr8HGeUildxhZp59urksXIP_UMEvy3sspKsziH9niGni7hc5e6-XhbgDU4g9bhwE4uhxJeZ6y8Wtqs1v_ckWU1zGsbaHMs2KyTkcljL44hmUMsofpREHdsPDiVe4RHcMPemHB3mDxbRyRhHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:
من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67831" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67829">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
تابناک:
گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67829" target="_blank">📅 02:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67828">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه
#hjAly‌</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67828" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67827">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.  @News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/67827" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67826">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9unOJV6Rc0MuPo6VFeYCS79Jc2_nb1uHeiG6ONixhcoInjbJYEs5tpNDTECe6ZQoB93TmPCL6do7yudwX77gXCZgOOLWL1ALQqJxTQCt-G0P0bfDbNth6YW5Dnkc-8rOLPOpsfG-yLlGzDWRm6eRpqqpr90op-IZGEDawM0Kr99sTf0gGlF-yxAmJWl4QU6TOMn2GSCOQrw4W5z5dqEbY4q5uIVCirfdHJpA7zspSsCGgOByn2_3nRJ7jRTDVdEtZg5NeiY7kM18Qc_MG7t5w05LiU2Cj9lOVZhJpV-ledTIkJdYLqIsJ72sSCq-i4_J-n-C2U03nwQvNkmKYD9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67826" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67825">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZvZbL-CljeflEDyVWziJM1TShr4HBTcBLg8P_J_YEvu0lMqpKtHgu5tuE9mpkBkxU6ypThBraVPgVPsXEZ0jJRoWRJv3vGr-csCdv63Wqiyz465sKn6Vd0ZpR-HjnIYPa78H56OmdNgVNwjoY-c9cSAu4ApmLJWoE2AFZggCFnNXZKvgE7lpQr7_Y7Xs_HRLO1B9auvVPa5cfKARTcnN3ciTxzlJ1p4zbisadz-usj7iS6Qj-ZjHalKm-O13bVdIbqdjrKM6zixC_y4snkbLHN1uPgbzk_M9dt7PdTZBHk_SuemFvhhXGQrIVjqTgL0gmSnjebOi_S_spIQ669gSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هم اکنون زیرنویس شبکه خبر
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67825" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67824">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUYNHOy2lqmzk5CTRByfOGB220Af_yxfImuhAjWYjmIWSbv_BpYs1mnhkMSFIMLYZPyjKxfV6J8JCQPK5YTol7X5A3mn8emgdU6uLOzw3AQNzfgA3inEeZrOlZNvWYuq5wzlgASji7OsemoA1yKHeh8KIe9chye6wXhSKm6jWnWiP1M23SbwFbh59b93YexziIKkfhiPgXzz2u01Ygf5gzgn4qsXWvkCb14kaMZr4mEmWZHo-LAiu-xO0WDKXcsNmfUc8njRPO5hSmOsrOT5uEGEFXIZxkuvLfDR_UC0ghNjKwYpDSLoTGKvLbuGG0rpUYxgG_tZkJDfLvxXJx0ApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67824" target="_blank">📅 01:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67823">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
صابرین نیوز :
به دستور مقام معظم رهبری، حضرت آیت‌الله خامنه‌ای، مدظله العالی ورود به تنگه هرمز مسدود شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67823" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67822">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67822" target="_blank">📅 01:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67821">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه :
همون‌طور که توی بیانیه قبلی گفته بودیم، هرگونه دخالت خارجی و تعیین غیرقانونی مسیر حرکت کشتی‌ها در تنگه هرمز، با واکنش قاطع ما روبه‌رو می‌شه و روند افزایش تردد دریایی در این تنگه رو مختل می‌کنه.
چند ساعت پیش، با وجود این هشدارها، چند کشتی با تحریک طرف‌های خارجی سعی کردن از مسیرهای غیرمجاز عبور کنن و به اخطارها و دستور تغییر مسیر هم توجهی نکردن.
در نتیجه، یکی از این کشتی‌ها که با خاموش کردن سامانه‌های خودش امنیت دریانوردی رو به خطر انداخته بود، هدف تیراندازی هشداردهنده قرار گرفت و متوقف شد.
از این لحظه و با توجه به شرایط امنیتی ایجادشده در پی دخالت‌های غیرقانونی خارجی،
تنگه هرمز تا اطلاع ثانوی بسته می‌شه
و تا زمانی که مداخلات آمریکا در این منطقه ادامه داشته باشه،
هیچ کشتی‌ای اجازه عبور از این تنگه رو نخواهد داشت.
همچنین اگر دشمن متجاوز به بهانه این حادثه، که خودش باعث به وجود اومدنش شده، دوباره دست به حمله بزنه، پاسخ ما قاطع خواهد بود و پایگاه‌های جدید دشمن در منطقه رو هدف قرار میدیم.
کشورهایی هم که اجازه دادن نیروهای آمریکایی و اسرائیلی از خاکشون برای این اقدامات استفاده کنن، مسئول عواقب این دخالت‌ها هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67821" target="_blank">📅 01:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67820">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
#فووووری
؛سپاه پاسداران انقلاب اسلامی از مسدود شدن کامل تنگه هرمز خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/67820" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67819">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ii0JE_oygLj2Nn55I5LUZduj1LUfAnFrw8ki9JcoBQzy1RB-DoZAz7fqu7f6nJG8066fL3JO_0uLu88Q2UoN-ONwiYPUGE5eh2L1Q0PpKTH0235KifDZCjaXrFMk_AChTrmLDCF2WLAFLBjWoFK_Yi-OHf4Ls_Y1QGsPzI2Var5Y83mxTic8dJeLAs-VNX9K22kyo4oRoR6em-Q5-9q4cf-BtVRCelNJl2vAOjcss8doT5oqE6AZCMIPjP5BLduwhbL5AaHp0TZKm1EJbcVJUQwUPtKhyf4Oyt9DTPhTfSZsui9nEbk6yCGBMSX2swIYtbpkSELrVPTIBqzmZm-pAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67819" target="_blank">📅 01:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67815">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TaXGdaOhwYX1WmM-OYvdbkH7PI6bjxAWvjVuomGbWv4gx4LFkohVLoMn1r-yk7IvwbOuMiwhO75f0QlWmFTgDWdo9s3MNsIMn93rAegeRswiSBmaqX_tWUizyAFacEvS-6KAAxIuhq85e-Xp7IJWL0ZxPnF8055rVTNuxXjyFEO9ZXFJgG54JyIa-n5930yBRew0-M5nHVCAhBspCodwCelWUCTEUcxfJL1OE6zNmOLT1xkyg00Xg1uadDYxmoYCMbHczJX9yxAGuYGums1viCmuiCWwVtYD0o5CNXq5_YnPyjYXisUeYBzlHmffFUbfi2pwlMgVEZHKeaix4FW-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTDRD5hbtc3zNuLXNIQ81luRd2GpWSl1DSC9s6Y4FNT-XotQuaSsOgMfU7KMs_LXzGYeR-DyKZjuBFcHLCxkiEdujQnfMqRkp6C5J_pGIdeUdnWqBHMG06BpmsEi358IUlN40AnN_-V-XtdJVzNSEuFJ8J9cKCbGcccALd3MqhO93gh8X6CA9TGqFgBJs2msd77zIcClOzlII4No8A94QOck-JsFM0ljKl2X3QS2E9Zry3D3K-5kxpLqU6fIGoa7FAfxqnhve9apCbFpMnxnzjzPaw8_WWxPRrsAm_7f5YcRz9ezZ312qkNzeICnTdh2Hlpnaa62ssGUO8PORLfdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSsrrDXIRqwP_bYI4WoVWpbSIvr2sC5kmGils_GRQH_0q28jUty8ontIcGcbb3QWvqgMZOrGJx1LVleopnhLACE22rbzhMTzIj9-i7sNQGyvuoY9OIBATHoq7w-Bk7g3Z2G-qPxRpFy1YZFqaQLqFKay1Y6N7Fp234xygjrRfQo0cA6rpx-tTnOjtOnwEDh2X1GxUgMQZi2p54LPEKSE2hW4tk54cJiUD_hS_tKgx1aCBk52A84uBTbjAv5F4neMymwGvKwM799Lh6Q12ruklq_eELQuwL4GrS9G-mjOwC1fKrvH9D8SiCYc0EPwMxTcjVTsU7J1LiWevTr1ArM5ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NpfHDoqFEFVwEAGywrNMgovJhpkAvY-bEscehHhs2Wl6t1RZJglDr2MJ53dwMrLUYv8kXtM1o0X1DjMpu-GROEgbcbYuGPwYc33Ne59xbUXTKIkzssBaH0v45hhn2mxO1oigML7-eNK0pr9OHFHxwge4AaKnfu8LB6uBf7u16lg10Xs6vbUb4rl6cUWY-InWOH0rtqoqHRDkMdnLe9wE1cS4a0VGfWnMMXEn9sPDsTokzbxBKlpWTsgXN-cqKFc0KI3ZjGMoNPJocl-BbOiDBXlXbKuEmujzqwsq1R_rJ6g_z3YCFLejhiE_0ip2TI3rwcPCO5zxSODPN-uojMbcfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
هواپیماهای باری نظامی آمریکایی از نوع C-17 در سه پایگاه نظامی که توسط ایالات متحده در داخل اردن اداره می‌شوند، فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67815" target="_blank">📅 00:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67814">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=uWbU4Uz-rD_wmoLI_t8wlmM_rpodgILDefPvSiev3-OQzV3VqgJ70--0VqoRjiF-HoD0K37SQ8MCkATDTlFNHMgwHeGJWz0ilgw5dsJoV18PotzL6xpbmscBFF3NH8GOiPvAEkpatylgeeDgpqgEVNiJ3uuxUbby4XUFSkWOseM957c3QElykc6sJlfm8NfuK7Beqzp1uwpsO0oohkKY1BVFANkXLLkpesgnOhNEc4RVMKt8ZSY53VXcEf0fWyHfQz0cv7EJZqrE6z4fS_yq9Mdd_Ww2rxiO6y3mxrm3Z4-ivnTS1O4DTi0IMeNtGpEcXiWE549syJeWtXgQTBeeKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=uWbU4Uz-rD_wmoLI_t8wlmM_rpodgILDefPvSiev3-OQzV3VqgJ70--0VqoRjiF-HoD0K37SQ8MCkATDTlFNHMgwHeGJWz0ilgw5dsJoV18PotzL6xpbmscBFF3NH8GOiPvAEkpatylgeeDgpqgEVNiJ3uuxUbby4XUFSkWOseM957c3QElykc6sJlfm8NfuK7Beqzp1uwpsO0oohkKY1BVFANkXLLkpesgnOhNEc4RVMKt8ZSY53VXcEf0fWyHfQz0cv7EJZqrE6z4fS_yq9Mdd_Ww2rxiO6y3mxrm3Z4-ivnTS1O4DTi0IMeNtGpEcXiWE549syJeWtXgQTBeeKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک پسر هیجده ساله یه رولزرویس رو یک روز بعد از ترخیص شدنش از رو کفی دزدیده
یعنی رولزرویس رو تریلی ماشین‌بر بوده این با هیجده سال سن اومده دزدیدتش.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67814" target="_blank">📅 00:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67813">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKpB2E5uWI_zkTBiPG6Ie6e0sZuirabJh_u2IGnPHHjyYYnQ2WqqQXccdEgK7atXW9olKCMgpe_bkZktgY8yzpkfjt4l3CL-0nAQJG05x9Ntz3KzYJ4WIdBMchLI6HO0-c6rWu7Du-gBBV6QGHykuMV1yJzEQ5YCr3rPLwoWzsirG1CtrqV7Y2QUBRUmTQj9xHfncq4NK5mGj3LoIsXELulgVJYn3n1w-jwb6TG8-LBbFWRaphPWtoD4lXDYAQvmGyrbWiRyP6DV_xqPm2INhw_B-Y-ZhGzaRr0gSx4eyK_3c0MF5m_OKlHdb4WnzTrUxmoELhub2GwatDEmh9tSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کانال 14 اسرائیل:
اعلامیهٔ مهلت ۲۴ ساعته دولت ترامپ، که روز جمعه، ۱۰ جولای، صادر شد و از ایران خواسته بود تا حملات در تنگه هرمز را متوقف کند و از آزادی تردد کشتی‌ها در این منطقه اطمینان حاصل کند، در ۳ ساعت آینده به پایان می‌رسد.
این توییت دو ساعت قبل زده شده و تقریبا یک ساعت دیگه مهلت یک روزه ترامپ تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67813" target="_blank">📅 00:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67812">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
🇺🇸
مهلت اعلام‌ شده ترامپ تا پایان روز شنبه به‌وقت شرق آمریکا ادامه داره که میشه حدود ساعت ۷:۳۰ صبح روز یکشنبه به وقت تهران…
تا اون موقع به ایران فرصت داده ترامپ که اعلام بکنه که تنگه هرمز بازه…
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67812" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67811">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9Rc4e35rNir_crS_vbzUgWIFv34dZS5wM1A8SAxwUmpKsn1WIJoAY1ZFpAb4MO-HHoeIhHH1VH-4WUr3riJFR53Rt1v42ejpLE0hE81P6N2EjFK0igjyiK1Cq3XrO_gfPaGazqsT0JggG3NTL5wpIBxpy3Y67axXXNcZtByFctv_4-rmUoS1JJsmaDUTd6R4kA1CBcUB96Ry0XAXO4SR5hkYfu6tMT4vKngfQmO4E5nsLPL_MIljRLfGORB4Z663VA0d-ZAVl2obVtVMdpSiLYwDzFz3zHCPQQszIqduYhyMGKbhvFVPi0FIIdjSvm3Zo43lq0Nr9r4la7yQW_KCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پویان مختاری گرداننده‌ی سایت های قمار که خودشو مخالف شاهزاده رضا پهلوی جلوه داده بود و معتقد بود عاشق جمهوری اسلامیه؛
امروز صبح ساعت ۶ با هواپیما به فرودگاه امام تهران اومد؛ که توسط وزارت اطلاعات بازداشت و راهی گونی و منتقل به طویله شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67811" target="_blank">📅 23:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67810">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTR-ElkJf1qMH0hyF7iNzgZ9RanSw05VCdRwnHarPz0v495J2GqjJdpggSJSbem2R4mmOmaD3qZQOyeCxh0jBgjAih-270gvIhiRqeG9aDLSMsaH0xo6sYu7G1YyAhMG-yhVtTUR0XdwtOIpLGHDkimsQFDCJWUAKTfkXzVgEQveU2D18wKLkcP5GGEmYvELSGv6r5l20suSerlFS3E6pCYPQ0QpU4xE3dpczC4tw_XJn9ofvcwjHDl-45CzO6hRMd-7_23627G8eij_KpdVfhZSenb0TgInZE7eYxy9NYmw0BmrLpX7LsBpBOhJWYr04nZWcE-78D2Hya5bEdjzbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی قلهکی:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67810" target="_blank">📅 23:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67809">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
اکسیوس:
ایران نتوانست در این جلسه، موافقت عمان با این پیشنهاد را جلب کند و مجبور شد این پیشنهاد را برای بحث و بررسی داخلی در تهران مطرح کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67809" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67808">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHe4X27kWpHdQJaW6AMFMN4dZvFesQBDl4oIe7QpVJavdM70btofaXCAtPg2t_jSYAs2ZVNyAOz3Zpc_N9IF9sYdPsdfJUf9IvFTxQNtb6DjtCJT61SsBPYE9iS09eSGHrrtZe9mAqnEfo6OXzMJEPS7nO0o3X7tYXH1tItL6y5-wPc3SPMpZpql2X8xGHcHRg5khrGQ6pnC0BZVdB-vIwEj4mymANBWQPTg3iVA2eI4wohgJWPPjmwtxZO6nOf41h6-VKULaq_TE_siwO99Je5aObmkICLB4kSwk_1LXqrGrgkQGPQVjIVf_xuRfAlrnr_kjewWW0Vi-S71w7wtJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:عمان پیش نویسی را برای مدیریت کشتیرانی از طریق تنگه هرمز با استفاده از دو کریدور جداگانه کنترل شده تهیه کرده است.
بر اساس این پیشنهاد که هنوز نهایی نشده است، کریدور جنوبی از طریق آب‌های سرزمینی عمان برای کشتیرانی آزاد در شرایط پیش از جنگ باز می‌ماند.
کشتی‌هایی که از کریدور شمالی از طریق آب‌های سرزمینی ایران استفاده می‌کنند، به تایید قبلی تهران نیاز دارند، اگرچه ایران هزینه‌های ترانزیت را تحت ترتیب پیشنهادی اعمال نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67808" target="_blank">📅 22:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67807">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=aA1jmFtrD5zPgkIEFX3iEmkRjcAdopLQlSxeFM2arCNwe4lVB-kj5LMqMMZ5vZEnjNzJ9VYmijwSbG-aIN6JVIHIhqaMeB_b5gF7znD96PXobtJIDGSOhs8BU4Uc2eb9LytfzoclMuxjM5doINAkx9U51cdoMfw1Szk9qCP9tiRf7LufF6JTNbzy1z-Qv2DGwn0jfDOCkNnW9s8_ImJ6qNqspuef9hba5PIQqYIFYWWkNKisv23saPP9dVkBO1k2L0OUBf9ZLMQN3gb9UNzwtuNnsJY0n7mJc1yp-xRKujKvzKxvu0BXJ7dYACyL5218fdMnYRFGMo2CePAQhOTPMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=aA1jmFtrD5zPgkIEFX3iEmkRjcAdopLQlSxeFM2arCNwe4lVB-kj5LMqMMZ5vZEnjNzJ9VYmijwSbG-aIN6JVIHIhqaMeB_b5gF7znD96PXobtJIDGSOhs8BU4Uc2eb9LytfzoclMuxjM5doINAkx9U51cdoMfw1Szk9qCP9tiRf7LufF6JTNbzy1z-Qv2DGwn0jfDOCkNnW9s8_ImJ6qNqspuef9hba5PIQqYIFYWWkNKisv23saPP9dVkBO1k2L0OUBf9ZLMQN3gb9UNzwtuNnsJY0n7mJc1yp-xRKujKvzKxvu0BXJ7dYACyL5218fdMnYRFGMo2CePAQhOTPMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سی‌ان‌ان: برای نخستین بار جزئیاتی از حمله موشکی رژیم جمهوری اسلامی به ناو آبراهام لینکلن منتشر شد
.
شبکه سی‌ان‌ان در گزارشی به موضوع شلیک موشک‌های رژیم جمهوری اسلامی به ناو هواپیمابر یو اس اس آبراهام لینکلن پرداخت و جزئیات تازه‌ای از این رخداد را منتشر کرد.
این گزارش در حالی منتشر می‌شود که تنش‌های نظامی میان واشینگتن و تهران همچنان در سطح بالایی قرار دارد و موضوع امنیت ناوگان آمریکا در منطقه بار دیگر مورد توجه رسانه‌های بین‌المللی قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67807" target="_blank">📅 22:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67806">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
کانال 15 اسرائیلی:
ایالات متحده منتظر پاسخ ایران به درخواست‌هایش مبنی بر توقف حملات به کشتی‌ها در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67806" target="_blank">📅 21:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67804">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=Qti0Gf-T6lORmCOKCab2OAcnlJQQvK8_0_UdQI_AFqwvAEW3rauEgvrpvqThonJBru1PMhKjUJtzUC-H3wJVMpwkcKXLMPR1abgN-8B0oLdahqEahotB3dtTpKyo6LvHVRBFKk1BI4qVUV1GsUvDuaA9WNM-yoeigcasibLZ0hYvNScyztV_0JXyWTCnr_1PvklJ6XCmavhkJy6VF7bPmUXrUVxUBievGKI29N9v5hT8XNapGzTkwvReAyjXhG_tWLJ_SCem1FbT4qtQSaV-LMrVfzK4pc78sYuEIIQBokV9exZNu_4fV0_NE1zyhKJEuMahJISKcqKOYYFNU7dn2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=Qti0Gf-T6lORmCOKCab2OAcnlJQQvK8_0_UdQI_AFqwvAEW3rauEgvrpvqThonJBru1PMhKjUJtzUC-H3wJVMpwkcKXLMPR1abgN-8B0oLdahqEahotB3dtTpKyo6LvHVRBFKk1BI4qVUV1GsUvDuaA9WNM-yoeigcasibLZ0hYvNScyztV_0JXyWTCnr_1PvklJ6XCmavhkJy6VF7bPmUXrUVxUBievGKI29N9v5hT8XNapGzTkwvReAyjXhG_tWLJ_SCem1FbT4qtQSaV-LMrVfzK4pc78sYuEIIQBokV9exZNu_4fV0_NE1zyhKJEuMahJISKcqKOYYFNU7dn2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارتش دفاعی اسرائیل:تروریست‌های حزب‌الله در حال انتقال موشک‌های ضدتانک در داخل منطقه امنیتی در جنوب لبنان بودند.
این تروریست‌ها موشک‌های ضدتانک را به یک ساختمان در آن منطقه منتقل کردند، که نیروهای دفاعی اسرائیل (IDF) آن را از هوا هدف قرار دادند تا این تهدید را از بین ببرند.
پس از این حمله، انفجارهای ثانویه شناسایی شدند که نشان‌دهنده وجود سلاح در داخل ساختمان بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67804" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67803">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=rHQk5AlE3xQX4ZkuezsxVBo5IvNdQ5YEOjUye2YqRfZdTvB3-4GQcvX_YDS_7MPt0a54js13M-aker-DWXNdobLJ9F5p6-myIBYvR8agdhKziItB1jgnhj0fY7QbZD5v_7ZdAhkqh-0yQLmUbeQRxFRasPIfFWBVInm5AyAuww6QRuM3MKsj4bSiEWuCRt6uqqfNlV62xy64z6Aidg0fQz3-fHjAKpxobW3TdNFydYt9QVI7caqSM31z1thBRdBoKNZQdu_9ZJkYL-SzZ6tjwKoU-n_JDglFl9fPy3unZqT7P4xZPDkQs6l-KgWiDV7NCLCVwhv4J6wL92IAWR8uwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=rHQk5AlE3xQX4ZkuezsxVBo5IvNdQ5YEOjUye2YqRfZdTvB3-4GQcvX_YDS_7MPt0a54js13M-aker-DWXNdobLJ9F5p6-myIBYvR8agdhKziItB1jgnhj0fY7QbZD5v_7ZdAhkqh-0yQLmUbeQRxFRasPIfFWBVInm5AyAuww6QRuM3MKsj4bSiEWuCRt6uqqfNlV62xy64z6Aidg0fQz3-fHjAKpxobW3TdNFydYt9QVI7caqSM31z1thBRdBoKNZQdu_9ZJkYL-SzZ6tjwKoU-n_JDglFl9fPy3unZqT7P4xZPDkQs6l-KgWiDV7NCLCVwhv4J6wL92IAWR8uwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که رسانه جبهه پایداری از تغییر موضع ممد سامتینگ نسبت به مذاکره با آمریکا منتشر و وایرال کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67803" target="_blank">📅 20:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67801">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWwAfgXQSr8HGRAkAEEUFztEjoSBgLCYiH9WWTSQB5DsiBLm4cQ1a-AfKES-HtakD1Yp52gYBj5lBVRII2DRjp7DlBE2IyaZxvDQ9vBfNQG5HeB8Jf7h4SYrNHMoLrfF7h8_34eE7xd27OGGlUEFwNFLHc0nhqsB4OoJgqYuBEcpv59T6fV5oyRE6jXYyrkvq01kHpv-CQMq4DIydOO9N8gP8FRs24UBlu0bFqBpH6GCOf1CDlUZT7hsEXP9fXqlhsZDgtQEGvRP1NuoyXUiPaIBxwQCKRip1DQiaZvF08phFBiwWmcvreM3ADYzgu0R6yWdm0x_g0EMgZrGaViSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i86JOrSFPTtFIhC5tsQng13z6VS6rI7TnGbXs8xnKb_VwMT8IYHQMZ_FEmefaO3E7OZ-BDcUsOY4eWJUxTbjKHPQt8kruL_A1XMLvh7JqfIAHcTmFQkhWGxgVXlra79iY8Kymb7SbhhPz7kwGn4RnudkwNSgea9ksqtsa1iib4iyDzlwjOwXk6WhKezzw2FBA0UQCN8YO27HdxAVhJVlNgBAH8eeViq6BDCzEcp8mLUGNgbY3O9pvqK0IqhtVj5pJFoT4i8wQ1MazYc1gmX_d--GiBc5mVHCaPTX1yYJWUWjH7ScouSdX0xAhVEpxrgIXd5ADt-HXb61xZMS5lxgyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بسیاری از هواپیماهای تانکر سوخت‌رسان آمریکایی از پایگاه هوایی الامیر سلطان در عربستان سعودی خارج می‌شوند. این هواپیماها معمولاً پایگاه‌های خود را در منطقه ترک می‌کنند، زیرا نگران هدف قرار گرفتن توسط دشمن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67801" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67798">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-rD1CoEJBCVOVlIF_2QKIhqCd2U50IYh_D4F22gqgx--eVeOALEpfa-YU3sp6O_Gh7e7Yvy4bKlx12wrDsMWPhDufmvgRYkZDOVSwxkZQhSo_cWbW5amR3zQvwLpy8WKbf7uu7-JvhOHIwhO1CrQ4IUC52fNQ3sZY5n6zAPoIrKL_qJaoaysfuz1n-0487hfzwaG_Zehs5z8bQMDSfLVhCVYVQx0ZQuFAu7zjgOtmvaOtoX0_VrxsUIJ9hwXOWy-aNAiowAM8V-QpzjQ5XbIGQ5pP7W21GlBUs-2pNH6Pd8UW_xG1YACJCgs9FBKs1fqg7fDdG7zr9bj3Rnelkang.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
پیش‌بینی نتیجه 2 بازی‌ باقیمانده 1/4 نهایی انجام و در کانال تلگراممون آپلود شده
⏳
🇳🇴
⚔️
‌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
󐁧󐁢󐁥󐁮󐁧󐁿
🇨🇭
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
بت جی‌جی</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67798" target="_blank">📅 19:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67795">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbKK9Hr5YHPaHJcXESBncI0Nqy4KlZICmxcDBIWxq2z0QQOyuFQABNA9YaP2Jh185v-WH_DRwq-T6zg4hFGxP4phxBFDWiMj_EntXnt7ANTYF42eHM-r-dc0fQFE7xrygZAzjQXWJsBvljtpl87SNYngBgOcYrSShhztsAdpm_dSbVo6rVTM2AxBH799zIOjpXAPXB9cqfUcJ2IG1MNAP7UjdlipK9nrjX_Fw-ZCEvkE7X7Uxdee169MWcofUdptZf2W9JdzFJArPdKT9ZODNg-qQlgi_GshPtYpjQAIQdyFzP4Cic10b6R7ptfjb5740bg1lVtG891HmyBWp0fogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته یک دیپلمات مطلع، مقامات قطری در حال مشارکت در مذاکرات میان ایران و عمان در مسقط پیرامون تنگه هرمز
هستند.
یک منبع منطقه‌ای اعلام کرد که طرفین در حال گفتگو درباره بیانیه‌ای احتمالی برای بازگشایی کامل «مسیر میانی» در تنگه هرمز (که در آب‌های بین‌المللی واقع شده است) جهت تردد کامل و آزادانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67795" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67794">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=PQtjn3bHZQSvwbCUwgonZ0yDBdj3dZxmTwuGzDa-5Jr0GU6Clie7ICll65hyyeKvpMeW7S6FEoKi2-fvRRYoFBrK9aiEdBcMBWlfCnHo4XyRusr2kLa4dAelp1qT6mmSaV_tKhuhgQ61zFLGQNukLO-xR0kPol5h_QnyaTuF6H4bM9bjddsGv7BDBkZKH1XG9Nq65nZ1z6p1m41GEBazlM1BC6uuwVLfV154gFKf4zK6Cm8bajs4rPnsWO-S5A_vKxe0kV48OSdhdl3qW1249QntbMFUYmbmr5JlDXRjE5OF9bmQYXTnWmDEzrvLcxxP309ejP7dsK_ZZPRLRYMq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=PQtjn3bHZQSvwbCUwgonZ0yDBdj3dZxmTwuGzDa-5Jr0GU6Clie7ICll65hyyeKvpMeW7S6FEoKi2-fvRRYoFBrK9aiEdBcMBWlfCnHo4XyRusr2kLa4dAelp1qT6mmSaV_tKhuhgQ61zFLGQNukLO-xR0kPol5h_QnyaTuF6H4bM9bjddsGv7BDBkZKH1XG9Nq65nZ1z6p1m41GEBazlM1BC6uuwVLfV154gFKf4zK6Cm8bajs4rPnsWO-S5A_vKxe0kV48OSdhdl3qW1249QntbMFUYmbmr5JlDXRjE5OF9bmQYXTnWmDEzrvLcxxP309ejP7dsK_ZZPRLRYMq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریاست‌جمهوری core:
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67794" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67793">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9DHuXq9DwBi-FPKvmjCtR9QzW_9fse602o19sWyFgRpktXd5AGve-fhd8ovlwDch0G0IoSEAoq-leYgeUsM5PyKtYM6klIod72TK__2nHqAtg4fjbdza4kljsDZsCDIOFmuOMPLy2cIOIIK0E53LEUlrO8Q9PP2Ij1ar4B00auIBSYNJuQKOs1Gh2jXFJCULRIWf9BSnaiGsytSyBesfi3c-HVb0lcQh4akhGiV8rRH3SbGX6u6oTH8AJu-B0WgUcxGtEanbNvBW784CHH1l0T8fdRX9nYUz9bfwz0mwxve8DqL0R4iSqeMDA3TfTokoUB7d_DpF2JkyLVnVUcyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری مهر:
یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67793" target="_blank">📅 17:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67792">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZegQGKAj1lfQvh4e4Gx2SQbWRi7fYI-y_8waheHoIow69bBMGoiKSkF_YgOwH4mne_b3arKGw5GMU5iyxpezZfjCSt-sPCSjgzETXow_bmoIYnwiNyLnVVfiWEgyxHY9bwROjBmP5wqAVFbwYIqtWrlFqhNxVvS8HUUKaTSP7Fcx5m1QOt0rPNtEe6aKU8X-4hMs1fNb446XdPAoxhIUJsPOGl-X18KN1V8yNjOIXYnz2m_NuRvUNnEL80BZMHuRFmoJjjXDujOGH9LQwcMXCMIM3TcACdaLD2FZPVspyTtQJoyHceo-USdSco8u9utPqlDFSfvxlHcb70p99Tufw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستهای این توله‌سگ خمینی رو ببینید؛ مشخصه تا حالا حتی یک ساعت هم به سیاه و سفید دست نزده. یک عمر از خون و جیب مردم ایران مکیده و حالا هم نشسته میگه «جنگ جنگ تا پیروزی»!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67792" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67791">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=BwkAb1NsG95JoycPjWnRUk9e7yg8681hklmi-EZupZuD3JD4WtmFhXWVgwSDETRx8igbPETbmsC74J4pHExjs1P9kSFwcsisRlrjpzyYS3SskMsqpbvAuOnsV3UwrVsvkvfGJ86hMyJnLtXzL_5quPzvT2mrCxTTLtGKE1RZGmW_D_JpywS9ITp1yeMC5o9YhryW8DGUW4tNeJ5JXHVoh3cIbxD8iAICB-FB4Ojl33FAIurG-o53-nmixHIluXGf3780LhnN7hvQi6UfDA2JJm9_EKX2t6vEPaG1KNiyHNBL6_nfKfHvqeZd0E3TH1GwdlS0hilQHTwXC1IhkDmVAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=BwkAb1NsG95JoycPjWnRUk9e7yg8681hklmi-EZupZuD3JD4WtmFhXWVgwSDETRx8igbPETbmsC74J4pHExjs1P9kSFwcsisRlrjpzyYS3SskMsqpbvAuOnsV3UwrVsvkvfGJ86hMyJnLtXzL_5quPzvT2mrCxTTLtGKE1RZGmW_D_JpywS9ITp1yeMC5o9YhryW8DGUW4tNeJ5JXHVoh3cIbxD8iAICB-FB4Ojl33FAIurG-o53-nmixHIluXGf3780LhnN7hvQi6UfDA2JJm9_EKX2t6vEPaG1KNiyHNBL6_nfKfHvqeZd0E3TH1GwdlS0hilQHTwXC1IhkDmVAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کوچه پس کوچه های مملکت، یه دختر و پسر شروع کردن بوسه و مالیدن همدیگه، تا اینکه دختره دستشو برد روی شومبول پسره
👀
یکی از همسایه‌هام وقتی دید داره کار به جاهای باریک میکشه اومد و گفت جمع کنین بیست نفر دارن از پشت پنجره نگاتون میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67791" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67790">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
ویدیو وایرال شده از بساط عرق خوری لات های کرج
😳
امیرعلی امیرعلی امیرعلی....
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67790" target="_blank">📅 16:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67788">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUx3GBCDuArcpHto5TAYNlTutFfbx0_qXKoNtej4YjKMLskL8f9vvujI4Jy5MmkwvqrW66mJlDDF8y63XGU4WRrtQ8WMBV-9ajU2bypuaYOyHAKYVOTnxEZwQazHM4VBwn8CQ8lwSYS-Kp3d2FRCeIbA3MVIppfatLlUBIo8SDkYobz4LHqrKrslqD_BvFscgrqED8yTWT5vm0_UOTYwiPoHQfFLQ0a7qgujupzrAz9ucUuB5FS-MoGvmM42n1Lk7S4aguzrn4lsxIOx-LFVCJ6LD_ck-2UJEx3lL9lqDFKNfLveGc3vNPCGKa3La9CV57LvWihewEFwZ8qaHpvKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=d-zH9xYGXBCLnk7DhGr-28QHWysfiTevv4rCUHtfHlPu8NZOFwV7xXdzd8k7OeCJhc5KeDGi4kqFDUzwO3Uigd0HcmRl_ZpZnLPECOatLSICJ4jiV_yg1cYH1IDrYdmJ33qhsws-fZ5eFNCJbWePhxQYSaPqBMv-myTEKM6mqXg993wqpG_IEXusMys4kKrfu0TL-LlzOYQwRR8nmbhan7_FuLBn6ZtSYD8xy6Bk75dCvF1VeEydlkfTzvBsIUu3b4Bi4P4gBg4DzvtAkXf1jhnI7aBwsxCDXiW0C6EE8LOhQxVeOWz1Envdbo6aAku5pZhc5CABwscYpNE_EUtbUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=d-zH9xYGXBCLnk7DhGr-28QHWysfiTevv4rCUHtfHlPu8NZOFwV7xXdzd8k7OeCJhc5KeDGi4kqFDUzwO3Uigd0HcmRl_ZpZnLPECOatLSICJ4jiV_yg1cYH1IDrYdmJ33qhsws-fZ5eFNCJbWePhxQYSaPqBMv-myTEKM6mqXg993wqpG_IEXusMys4kKrfu0TL-LlzOYQwRR8nmbhan7_FuLBn6ZtSYD8xy6Bk75dCvF1VeEydlkfTzvBsIUu3b4Bi4P4gBg4DzvtAkXf1jhnI7aBwsxCDXiW0C6EE8LOhQxVeOWz1Envdbo6aAku5pZhc5CABwscYpNE_EUtbUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات سنگین ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67788" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67787">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=lZRugM9imvu85rJoqDPzY8eZdFHx75Nw9Y3v8X1wAiHfBMcZf8em8EyGVJ6n7yhuhBsRnMqaW0smDvMbJVy8s_ZjzpEXvKAJ1VprA9fbji7Rtost4qIyXknactXTD-vLvhOG-qwQK3Yo3EXV2rr4gcn8BsrNTBlxBOWdgHfaH_K0SqH79KGerobyZd8fb7Ye0VTB_ENTvXQVBOSnNYNDd0M5gCLWOmHqz4Wb_DuEDrbcuWTiMYVa91qQWwvmtyS7Oi22aN65-ODeorZfpw8ZqZ0AuPVU7Blhovlc2u_YxAp-zQBQ4hKBsD-s1DdFpBrXe77vqmFwurqT4JLuuELuqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=lZRugM9imvu85rJoqDPzY8eZdFHx75Nw9Y3v8X1wAiHfBMcZf8em8EyGVJ6n7yhuhBsRnMqaW0smDvMbJVy8s_ZjzpEXvKAJ1VprA9fbji7Rtost4qIyXknactXTD-vLvhOG-qwQK3Yo3EXV2rr4gcn8BsrNTBlxBOWdgHfaH_K0SqH79KGerobyZd8fb7Ye0VTB_ENTvXQVBOSnNYNDd0M5gCLWOmHqz4Wb_DuEDrbcuWTiMYVa91qQWwvmtyS7Oi22aN65-ODeorZfpw8ZqZ0AuPVU7Blhovlc2u_YxAp-zQBQ4hKBsD-s1DdFpBrXe77vqmFwurqT4JLuuELuqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری فاکس نیوز:
رئیس‌جمهور می‌گوید ایران دوباره به میز مذاکره بازگشته است. آیا شما واقعاً معتقدید که ایران با نیتی صادقانه و با حسن نیت به میز مذاکره برگشته است؟
🔴
هارلی هیپ‌من، تحلیلگر سیاست خارجی:
قطعاً نه. البته دوست دارم این‌طور باشد. هیچ‌کس خواهان جنگ نیست، اما ایران کنترل تنگه هرمز را رها نخواهد کرد. آنها به اهرم راهبردی‌ای دست یافته‌اند که به‌گمان خودشان، شاید حتی از یک بمب هسته‌ای نیز برایشان ارزشمندتر باشد. همچنین قرار نیست از تسلیحات هسته‌ای خود دست بکشند. بنابراین، آنها به دنبال حل‌وفصل مسالمت‌آمیز این مناقشه نیستند.
احتمالاً این وضعیت تا ماه‌های اکتبر و نوامبر به شکل اقدام و واکنش متقابل ادامه خواهد یافت و پس از آن، ترامپ میداند که در آن مقطع چه اقدامی باید انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67787" target="_blank">📅 14:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67786">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای:   آنها باید بدانند که این امر، متوقّف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقّق خواهد شد و بزودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد.   @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67786" target="_blank">📅 14:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67785">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:   عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67785" target="_blank">📅 14:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67784">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
انتقام خواست ملّت ما است و به‌طور حتمی باید صورت بگیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67784" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67783">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:
عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67783" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67782">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
پولیتیکو:
آمریکا انتظار داره جمهوری اسلامی در بیانیه‌ای که قراره امروز منتشر بشه، «به‌طور صریح یا ضمنی» قبول کنه که در حملات اخیر به کشتی‌رانی در تنگه هرمز مرتکب اشتباه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67782" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67781">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY4YpKrXzp4b4QZyyna2YJ7e4D7hdUVvu_kmChx4mbP-_vqZI0uwUm0ZaAfAYLCQXuglbHg2tkl3I8XB1jevXqNCO8CyKrdm3JEGqeNjkwQ-MeqbckmhZ1d6tDTW1yimatsP_r4Wvx3kMqvslHkpZGmq33NeYsGAdh45qTLWiY-VQVkBHjsyOX1enhkdMW9m2GyLMwXG72zpiATOXUyxpAM7vD_7R_FqMBiQIfeZgO2MnaylvQGPYUdXZqIdHvPDYr3LQAsBs-aB0hHX3rsPe-F-J4ZKk7UmbLBhiB8NywKE8j9C8qy57CAAW0WXmchFraCirlT6InOK0nbZ5RQgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب رو باید تا صبح بیدار بمونیم که ديگه کم کم جام جهانی داره تموم میشه؛
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس vs نروژ
🇳🇴
| 00:30
🇦🇷
آرژانتین vs سوئیس
🇨🇭
| 04:30
🇮🇪
کانر vs هالووی
🇺🇸
| 02:30
[این فایت خیلی مقدمات داره و احتمالا ساعت 5 صبح شروع بشه]
🇮🇷
دانش آموز vs دین و زندگی
📚
| 07:00
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67781" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
