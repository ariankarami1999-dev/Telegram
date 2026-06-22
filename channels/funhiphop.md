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
<img src="https://cdn4.telesco.pe/file/Zai4LCb0uhtXYbzoHIons0JyxEsqsqGySXsWD5lnwAlQzyMX7G5rf7yimedA6kHjULBKtTCXQpteImxQxouzHMlIR-uqmoraalO6lekhptjEf8P1Sm4_mrFFx9gkfPkLh9a_yv8pkxJ16yaRfHkfB1hHqyBNI1WBGsBfJHpxHp2lkMzA1Vpb6xnJlCsjYEB-ufC5ui89HAngBtDE4JKO1P2NhDkHEvudGg_ujCu4Q_bwNIEmAsxIcKz46-8QCM02yujYYfRTfItrHaQT-N1oH_eJQvcJ8WVUG31iFA6YbjWrlKBA0QSWsNlUURlOCYeWRZralpBGyOrSxJH6YW-QyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 168K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 02:28:59</div>
<hr>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/funhiphop/78538" target="_blank">📅 01:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78537">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=TAk7DY2eGIDifjdkaBU1aO_EZ0LGiTJtBwP3puRT_pcAh0u6FgnE8T311v2HPtr5zMhBo_lDXB2zHzG2YCgH57L0wXILz_X7TKDRA9S8k-zlcwUaCHwhKm_qu05VYV7NXUpINFBthEBmCcqViGOQL89PpJ4-c47Rp5fdJ-RXKE9gC61M8xym0c-lKvTc9jkai96t6Ijz72gy-nEGS1ea12f8_nxBGoyavskJEpsVM-JC1PQgc2EJS93lVVoWytVI6P4WJm7vxG36WSxCTEJvCJrjVWdiCIGo9c2MFgTU3DjvCOo_d686R8LSyiChvi686FeSxtiYLpOo8Jqc5OGFYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=TAk7DY2eGIDifjdkaBU1aO_EZ0LGiTJtBwP3puRT_pcAh0u6FgnE8T311v2HPtr5zMhBo_lDXB2zHzG2YCgH57L0wXILz_X7TKDRA9S8k-zlcwUaCHwhKm_qu05VYV7NXUpINFBthEBmCcqViGOQL89PpJ4-c47Rp5fdJ-RXKE9gC61M8xym0c-lKvTc9jkai96t6Ijz72gy-nEGS1ea12f8_nxBGoyavskJEpsVM-JC1PQgc2EJS93lVVoWytVI6P4WJm7vxG36WSxCTEJvCJrjVWdiCIGo9c2MFgTU3DjvCOo_d686R8LSyiChvi686FeSxtiYLpOo8Jqc5OGFYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/78537" target="_blank">📅 01:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6mr9CXGnKfGUpjzY3VCYSE80W1SBTzi6eve0hQJ6COI9MH_hOdKCwNawpHGOkrp-bShG-T4qwfjzO-_oEHFO0sHn8AJ4sZ1F4_g6CiAh5-bhiN1_2fKami71rgxGSDxdmvVj2ufJLrY3KPIIRt1gSBEIWhvhtYPY_TrmoFJw4zNawH4eK-7vV-RHk-UWEgp4qd8lNBY3ArJvIicRssL-BiWCuBvvQ0iqD2tGWaND8b8Hlzim4Sj6vjoldGU__c5VRm3T9hWOC-ANXTYIZ3aXXgRzCI9k8X_ynBXhsDhH6xETOjL7Y3xO6mNw1IP-F04li4jTI5Zk_YGiwQsycsWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان هشدار تخلیه برای تماشاگران ورزشگاه رو صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/funhiphop/78536" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/funhiphop/78535" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/funhiphop/78534" target="_blank">📅 01:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78533">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آمریکا تمام تحریم های نفتی ایرانو به مدت ۶۰ روز برداشت و ایران تو این مدت میتونه به قیمت بازار آزاد نفت بفروشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/funhiphop/78533" target="_blank">📅 01:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امباپه احتمال زیاد موقع پایان کریرش بهترین بازیکن تاریخ جام های جهانی باشه جلوتر از پله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/funhiphop/78532" target="_blank">📅 00:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کصکشا اینارو من ۴ سال پیش دیدم، چیز جدید ارائه بدید</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/funhiphop/78531" target="_blank">📅 00:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">امباپه چی زد خارکصده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/funhiphop/78529" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7xJZ9qKalydf9OV1dh9t6IyKYcPzrPudPvmzCdTle_X-3pnch5iJ0Xfbj5O3tQsaM1CpUnqWWX2_fcMxD_CNgefcYh8GT1LSsUakHO2r7lqv3clwz94NAbSlaV9lXrUyaILG3Kjyjpf9CoC8lddqlqFbNYqT1smOqF92IaUBseT8b8CxySBXq5ZXuKEJsTCHsfwP5UFWUqZqH8Bw_B2VOYiSx2GJI39jfWnpkLUpggc7WFYh2VnBtXd5DL1YK4UuQ1hA3MMv5f4y9vc1JJH3hftPfY8_pqdzTTdxLIj7b_R5e5Zlg7G2Xh1m-9uLAteq28q-Svw5Aoei3An8w8_rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی جدی مجلس چهارماهه که کامل بسته‌ست تا کسی نباشه که جلوی باقرشاه و پزشکیان رو بگیره.
یه سری از نماینده‌ها هم علنی دارن صحبت از کودتا می‌کنن و برا یکشنبه آینده فراخوان دادن که برن جلو در مجلس، اگه باز شد که برن تو و اگر هم نشد همون تو خیابون جلسه برگزار کنن درمورد روند مذاکرات و جنگ و اینا تصمیم گیری کنن.
یه سری حرفای ضد و نقیض هم درمورد تصمیم نماینده ها برای استیضاح فوری عراقچی و حتی پزشکیان و باقرشاه وجود داره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/funhiphop/78528" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دالگخیز:
پسفردا به ناتو اتک دادن کیرمم نیس چون زمانی که ما به ایران حمله کردیم کیرشونم نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/funhiphop/78527" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427abb0164.mp4?token=AcHlMlA0v09XmnWTNfVsFUQcLc0KGtGCWeRiVl_D87MMPTKQrLQgv2o9nkU7-a3v9xu7xZabwDnMgQ9dqjr9nETBeQMrRTKNz0hClvB3Ixxx5otz3fl6gWB8_LEKybtPq3QHGyHKL6j0vdItXLBHBfO2TTpN9XetRH8fZjMwKUzgpnxWgNBuBS-QfqM7aUUACZl-CII36uEFy7m4GSdN2GTvz-oT1l_X88gAzCCn26jFAptU9zcSj837DmilRI94kg-N_A04dlNNvQfiSy3Df7otHn4UKHCJArRI3YldrXoT30oNMnZjC-WgdNosgaHMwYQizi3ofsZuQ1CQRJ7cJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427abb0164.mp4?token=AcHlMlA0v09XmnWTNfVsFUQcLc0KGtGCWeRiVl_D87MMPTKQrLQgv2o9nkU7-a3v9xu7xZabwDnMgQ9dqjr9nETBeQMrRTKNz0hClvB3Ixxx5otz3fl6gWB8_LEKybtPq3QHGyHKL6j0vdItXLBHBfO2TTpN9XetRH8fZjMwKUzgpnxWgNBuBS-QfqM7aUUACZl-CII36uEFy7m4GSdN2GTvz-oT1l_X88gAzCCn26jFAptU9zcSj837DmilRI94kg-N_A04dlNNvQfiSy3Df7otHn4UKHCJArRI3YldrXoT30oNMnZjC-WgdNosgaHMwYQizi3ofsZuQ1CQRJ7cJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویناکیا چیه دیگه کیرم دهنت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/funhiphop/78526" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگه این جمهوری اسلامیه از آمریکا مواد غذایی میگیره میده دست بابک زنجانی که صادر کنه</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/funhiphop/78525" target="_blank">📅 23:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ: دارایی‌های آزاد شده نزد ایران برای خرید مواد غذایی از کشاورزان ما استفاده خواهد شد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/78524" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قالیباف: توافق برای آزادسازی ۱۲ میلیارد دلار نهایی شده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/78523" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قالیباف: توافق برای آزادسازی ۱۲ میلیارد دلار نهایی شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/funhiphop/78522" target="_blank">📅 23:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پسرا رو برد فرانسه میبندن مردا رو برد مساوی عراق</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/funhiphop/78521" target="_blank">📅 23:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln_YGyBZL7K5HWWqlnB3vTfnuMaPAw7mATcGhh0MbM6WMA_OoCBiup2H-EJyHVMnKV0G664ZZy_MgN3LF22BHWZPVt2vXXLtSl2VAhCIyIaDpXqjnt0bv0TJ_JYPn8x4HddoYGJFhKTHS_A5-2yCxU-d6kgsWy_uJkix59RzwFCIMFHaTLVe1-AHjWF09m5UCXcsdMAx3GkyhmaV41MMz7k2LGgSjuYHHVr-6u4rkNu1uUcCa92zDodhm3pUgifVaJhttDzMdJW_fWY7WpkaLZ_dzecqPc-SpPFXy2AeJoaEW-LPVU-ivgLGrCMj5l5glnFq-wxOx00Rny0SHkDMzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب رسمی فرانسه واس بازی امشب
اگه ببرن میرن مرحله بعدی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/funhiphop/78520" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تا الان صعود این تیما به مرحله بعدی قطعی شده:
آلمان، امریکا، ژنرال، مکزیک، النصر، آرژانتین.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/funhiphop/78519" target="_blank">📅 23:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2ukvJiP3PwUPLkdDb09g7iK3S4TVHwXwF_uiH-nNfczQ0UHy3ZgAxCzac2uAwALnE7RI8MjSFgNfGQrH6f2BKnahY0FR2HuoaUaLL2MD_BF5peoCffrTG12RUceCKdwOWBYNNhFOM0t0SNaBoxMU88HhwPov7UMgPf6Kj1wD9hUYyrGcQECWwzbKhtPG_TWpLjVF4kXKFU6BAp0Tq7jZgwbjzGO7kfPrk3L6UXB1Z9Bd7cEL-jAF3WaerYqZWLzV4qhb2gi_GLZVp4plnY2XOGaSFd8qg15GigdHoghUhSZG4BcDrj-AispSChzofSccnfwiKGBWG7yLCqdAJlZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TwHoFKAdJMrVwqTCJSkwfkhWXbEhxk1XIiz5RAqGy49T26jnmrmBtaca4LBdciCNwKR9tQhoE_TlsWpplMwyl1IBjKntAinqn-i20ql7SzbczaNx4dYm2bmPj1hwR5nyfKOyPcWABO7De_vgza91appnnc11n5oshjM8lcV-dEcAuQLJK2uIWRAPkyQNbxft2bR6Dz5UwiR1PJ2NDnsJ_5CzqUUD8cocQLoO1oc2ip9IU0Fma26zI6IYO93qMEY9Wzn4lTzbZwFq_NGVFpJMUC19oicQW7l1pRrQkOj__HDpVM2cOes2DFr78BjVa3X_mkuVx0Rxk8ocpMkmt-RNPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/funhiphop/78517" target="_blank">📅 23:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خداوندا سپاسگزارم در دوره ای زندگی میکنیم که سعادت دیدن بازی اسطوره بی چون و چرای ورزش جهان را داریم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78514" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رونالدو فقط و فقط ۹ تا گل فاصله داره تا آقای گل جام های جهانی بشه</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78509" target="_blank">📅 21:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">متاسفانه نیمه اول تموم شد و قراره به مدت ۱۵ دقیقه از تماشای بازی خداوند اصلی فوتبال محروم بشیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78508" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe4s3FzXSpwl0Yfcxbq4qOOnUSggt_rGfCkUpRqfwVkYr32EWL-a7mEu9Q0E9QYNe5xH-9F-te-DVoICThysNyPVvnbLh5pnI3Iddr-9nbQ_SOLKc2HHNk3c-fg_dkuisvWuSkPVOtuMRUA4oRX10Si017PK4tWuHhamNe6RPZCcRlyDSixkw0DjWrnJ8m8viFvN-ZbYzrFrRdBBAo8eu6vTvWQ9iNooAN_I4CSU_w4u1oH6Q-Wlxgenyoz0ZWFbcTntFzvU56dD88y5uZ_PjKkjYksmuHRzXDKTn7nc49kPcC1Ewm35uAbakdZ7mbvrSz3c4tM3ygEwhTVwRDwEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78507" target="_blank">📅 21:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78506">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiDboPs8_Wy2IgTDBZhdbSmYEWWarHOxc8EdprPCwheTXxwmCe9CAiRgUwjKW-kgD39TugFIpfB4zuYAJmFM-PggHZyrOXwDZhQw91mfAHB5piorJRlVV961u2TRRYPzkIdqN55i8O4VvpXtvKa66bXLQeS9ThYZ3regvNsmmOGouzEQhNNlOlbOOUq61ko0jVoxWrlQgS6hIyOv0z7TstcBReQTYh36tcEifqFrPRS9vQ_pyWAKcKpM8DyxB6OCnTpojoERZKW9RugaEGh9TRx5RAlCpHr7ZAgBdbqmG2wq_kJcZGmIqLWZPtxJQq5YoHAUEoQS84195xWOXFJXsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78506" target="_blank">📅 21:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">رکورد کلوزه شکسته شد
سر تعظیم فرود میاوریم به احترام لیونل آندرس مسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78505" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78500">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رونالدو اینو میرید رسانه ها عزیزاشو میگاییدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78500" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پشمام
چی گرفت بیرانوند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78498" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وقتشه پرتغال یه ستاره بزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78497" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نویسنده کتاب تاریخ فوتبال اوانس داد و پنالتی رو زد بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78496" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NDSHkcEiAhblYQRvCVPsQUvTilRQu0lYdLc86n0S4oOOFG1q-5BJ7sQEaY9LXo9b6m8WA23w51q5LsrIgyTKwcVRXSERlypah4drYkjizk9DCJTsyOxS84Mvq10PCkXI7Mjp4gVBDRbWHGDkA8tkgL5rGNTirwPfs6lmvAj-Tb5TnIypXl8x5gmNlFhYlFdOdpl6jSvVGXC0rG_4tojz2EtChtxaowk0oGM0XROJ8JDx6enqdrL-I9bkANh2oSQ-HtgKUVODJ8Y2ZtKV77Z-qOdlXPeGiFJ3SS2MsyK560t6eXs-RiQjFfd_okk6nCTNifhl7z38dfoCCn1Qmd7t6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پیام رو نخونید!
نماینده رباط کریم رسما درخواست فیلترینگ میم الاسکی را به کمیته مربوطه ارسال کرد!
میم الاسکی با سابقه 4 سال بزرگترین چنل میم بودن بهترین پست های کل تلگرامو جارو میکنه و با ذکر منبع میزنه چنلش و باعث شده مجلس از دستش فشاری شه!
جهت حمایت ازش جوین شید:
@meme_ol_ski</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78493" target="_blank">📅 20:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">چیزی به بازی پروردگار فوتبال جهان، حضرت لیونل مسی نمونده
به امید درخشش برترین بازیکن تاریخ
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/funhiphop/78492" target="_blank">📅 20:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=dwhm1DWPmCRTqca0Swot6f1hgF-cT_fef1LyjAOEN4Y73HsX-uzWtIQW-u36l4Q9mm9E0TAFactYXvau2tsPYvEY3nqKtHU6I0UkUkGW8ECjreo2QVX9jUdAASLB3dLi6ElYwNdG6LmLnJfTEQ7ncXYfqw5Hxryc4PhQf_FJHaLcMnFUy3ZaEeHI5qslQYKezDjBa7JlrwI7dJy16mGK0Ma_wyMo5K_SsGXk3P6Bhh5J1iK63X_ptXSPvqycnse87J5GKg-co9lEA_OdQcJVb3l3ygDaTAczVresQnCek7KWVOhuxeG3n4YlWMO7e7U9r_Bwyd_BaFTohED7_7gvTyol__tfHpTh9TL9KkMcIFbdMLSSi3JyvCsUZZEdsYJtsu278SalxQh9nQZX4Pao5MPZZbpjmJ_b1cSuKIhkaoz4RDK3sQEUS6FvUjgLZjYr6MXJaSUfObEZX6UIwFCa-KoMhEqUWQqSq8wFqMXQmnJDQpvAkpNBi9FjNAZFhl0i8qEl5QiSiqS4faSdD_DZg--loMDmRv7T2GgfUpZN0PQwvTQh_WvKnmE3m7qG5sJRaitlfj1EgWMfG6D8aXWES2k3Xsx-6GCfkRsX-m6sQp8MAeztb1puxaU6FaYLRRpi7Nyd5AWwBNMkcvPCEDh9lzfRjUeqYbURhnBLBBNljzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=dwhm1DWPmCRTqca0Swot6f1hgF-cT_fef1LyjAOEN4Y73HsX-uzWtIQW-u36l4Q9mm9E0TAFactYXvau2tsPYvEY3nqKtHU6I0UkUkGW8ECjreo2QVX9jUdAASLB3dLi6ElYwNdG6LmLnJfTEQ7ncXYfqw5Hxryc4PhQf_FJHaLcMnFUy3ZaEeHI5qslQYKezDjBa7JlrwI7dJy16mGK0Ma_wyMo5K_SsGXk3P6Bhh5J1iK63X_ptXSPvqycnse87J5GKg-co9lEA_OdQcJVb3l3ygDaTAczVresQnCek7KWVOhuxeG3n4YlWMO7e7U9r_Bwyd_BaFTohED7_7gvTyol__tfHpTh9TL9KkMcIFbdMLSSi3JyvCsUZZEdsYJtsu278SalxQh9nQZX4Pao5MPZZbpjmJ_b1cSuKIhkaoz4RDK3sQEUS6FvUjgLZjYr6MXJaSUfObEZX6UIwFCa-KoMhEqUWQqSq8wFqMXQmnJDQpvAkpNBi9FjNAZFhl0i8qEl5QiSiqS4faSdD_DZg--loMDmRv7T2GgfUpZN0PQwvTQh_WvKnmE3m7qG5sJRaitlfj1EgWMfG6D8aXWES2k3Xsx-6GCfkRsX-m6sQp8MAeztb1puxaU6FaYLRRpi7Nyd5AWwBNMkcvPCEDh9lzfRjUeqYbURhnBLBBNljzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس علوم غریبه و جادوگری در شبکه ۱۴ اسرائیل:
دلیل اینکه یهو رفتارای ترامپ ۱۸۰ تغییر کرده اینه که ایرانیا با استفاده از یه سلاح الکترومغناطیسی با فرکانس پایین که توسط ایران و روسیه و کره شمالی ساخته شده، مغز ترامپ رو دستکاری کردن و این افکار مذاکره و امتیاز زیاد دادن و اینا رو تو ذهنش کاشتن؛
از منم خواسته شده که مغز نداشته‌ی ترامپ رو به حالت عادی برگردونم، منم دارم تمام تلاشم رو می‌کنم خواهیم دید چه خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78491" target="_blank">📅 20:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ایموند داداش این چه کاری بود کردی</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/78490" target="_blank">📅 20:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahe5IBlL2rs5dYT1EBkm5Hzw8lfFxur7-40GAlkzmtlnz4sSkDlFlAv9p1Xi9J6vLVjOK6AcSmOw9rLsYhv4sVBPg8xWFBszUZXso-G0TrgXG3zcdQ9djPV2NRVvC57i2d6KGygnx8AfVrKMlKShy0P468dPOvJJh8NKl43LohEgcbalLQzL7yhsgyUMWIBjDEwIylBNLw7CK4VD5OBsUbwYzU_iGrQyTkly1V4RvIP3eT8L0idiYGp4-TkJRy1hUp1VeoOM-QM-MWmnG4wEkimquDGIQd_AmJJ5QsRtyplh_WpZ6PgWitDNuiftnasn1bjCPpeSWpc5tEY1xrZi2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد سوارز جوان شد
بازیکن جدید لینک شده به بارسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78489" target="_blank">📅 18:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فدایی به هرکسی دیس داد طرف بعدش چرا زنشو طلاق داد, اون از هیچکس اینم از حصین.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78488" target="_blank">📅 18:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">فدایی به هرکسی دیس داد طرف بعدش چرا زنشو طلاق داد, اون از هیچکس اینم از حصین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78487" target="_blank">📅 18:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حصین زنشو طلاق داد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78486" target="_blank">📅 18:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آمریکا تمام تحریم های نفتی ایرانو به مدت ۶۰ روز برداشت و ایران تو این مدت میتونه به قیمت بازار آزاد نفت بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78485" target="_blank">📅 17:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHQ0Av46h2IFoaSf7pf6ujbzj7IFm5hCZqachT79lxbxM6Rz_0M1FvZG85nwQRbyWgLj-8B9aV9l9-eEQbbIj1_6jQHrYrSWGm0gvmwy-KGfTPJTBrFADiLic1OE6N0YtKNP0lJtJ91jBGoeZ5QvvUH1IjKvOw37S8_Y1C4nu5_p7eEEuRt71RCqXE1Ruoa2Cq8ViSdZ75YxXsKyp3AyzsA-u8t1gd9ifDuHvnVGj8P_Kbd5HXgtNDqWuruKRGVWWrRg-LOfYkn_Ge2ajpzoBCuXfkU0cxBdsxpmiUtZVv8vZ6xm4F81nl1sEAjfbU0H_HcueLGmuM1OBg1LeWglmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودمونیم ترکیب دیشب ژنرال جلو بلژیک چقد هجومی بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78484" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78483" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDmZGhGT6IeHaG7nEbTmPxLX_4OpNuWTD4haH5y_So9hnEak9ELTIEEBI43o_8XKJn2PqCyWVYH6OD5UyaeOtjWWq_cw4pe_-aVNKeBpToz-CEnCCxiX3v2YLH-cfcFgVzSh7DNEPR36AHqlxoe0eXOMdYcrNqJ4BUjyxbj8MDA1u7mQ9zLE_xaImM_PWD8TyX0XI6QG283znZgsbjegP17jVDEwaXsVszAMOwuUbyqfSNyalKE0F5Gi9X5QE0J3vcysYh47Ow39YvJNRBXpirOl_EyEr6bgt9bIbEqxvhD0Y6V_hoMYqAlNsIPTFtuoeOu_oq01fP9xeTxP6Z3l6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
G1
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78482" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رفیقم زنگ زده میگه ضریب عراق جلو فرانسه خوبه ها
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78480" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfa646697.mp4?token=Ty7KHZe9AmFvX_YmULcxS3hLzl3yJIMgwFOFze60QFyuEw1cvg2NnRjBEJVo6rYqD4jKvgV0l-RPnnlztXYgJdcMl7S0WGVawQ5TQEUykVWymZjZ0XxBJfwCHaAbXioVbnupNFxJlHJPpxMUswvOQ--I-UzAZTnAAl6ywqad-e0xUPsCg4q8TT12eSmd7nbDat6QdF5qKuthlqonbwFT7ispaZ8lU49kCQ-zGbb_UcqlazVJ5Cy54GmdFV3AWBzUFs9_FVCDpeuyAroVa5GB_BdyxaXXGrNnDltfWYfGigaLJeuP1OXQa9ipyeCMft6Hr8LhfIx72oo-yuBaN0owqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfa646697.mp4?token=Ty7KHZe9AmFvX_YmULcxS3hLzl3yJIMgwFOFze60QFyuEw1cvg2NnRjBEJVo6rYqD4jKvgV0l-RPnnlztXYgJdcMl7S0WGVawQ5TQEUykVWymZjZ0XxBJfwCHaAbXioVbnupNFxJlHJPpxMUswvOQ--I-UzAZTnAAl6ywqad-e0xUPsCg4q8TT12eSmd7nbDat6QdF5qKuthlqonbwFT7ispaZ8lU49kCQ-zGbb_UcqlazVJ5Cy54GmdFV3AWBzUFs9_FVCDpeuyAroVa5GB_BdyxaXXGrNnDltfWYfGigaLJeuP1OXQa9ipyeCMft6Hr8LhfIx72oo-yuBaN0owqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78479" target="_blank">📅 16:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">برنامه ابوطالب فقط اون تیکه هاییش که اینستا میزارن جالبه، بقیشو ندیدید هم ندیدید</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78478" target="_blank">📅 16:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کورتوا حسین کنعانی رو فالو کرده، احتمالا بمب 150 میلیون تومنی پرز کنعانی باشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78477" target="_blank">📅 15:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پشه مادرجنده مگه قرار نبود فقط شبا نیش بزنی</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78476" target="_blank">📅 14:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK0er49TfgniShfO86WidDhXtpMB9-odAet3SiYmRbdKD_c-9LJ1yD1Cq7Tk6pbcXEazsBp6i7ig3aEFc3l1qO66hTkHgmExSvtpoDFvZSF_SqLtxXrExGKEx-dt78sT7ER0Soi1tscPOi9F-4JlPgSbmvNfUN3SzjwhAzvpDjYgqnmhpl13lfwTJrsaBl1bboJelByjzGfJEWS7vQX4XviMuWa7YrLdn8Mdsjb47ONclCbIKbCi9Ml-TS4yAIc1akO2BroAvBervCH6NQgslsPTIpmQxTLFIn3fI7wyv-wVnl7Gt6J9CYGbgTl4PglYEXcbguk13tfuEND-WRxMrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا اینطوری قانع نشده بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78475" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78474">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تو جام‌جهانی فقط در صورتی که دستشونو بگیرن تو دهنشون فحش بدن اخراج میشن؟ یعنی حالت عادی بگن کص ننت هیچی نمیشه؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78474" target="_blank">📅 14:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78473">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezG851J6PcV9FKSvbAwGPymDWJSGq14fZvcB9ynTa0T2TwRZYM_4DlmUCbG_Jn3XaR-vY17IzqdrXZAo7l-y12FBDB8TthmMqDsVor0yUTIBrrmY0wgM2JBI9ftSejgMIAW8IUCMel7_hPTHk1mPW6Ru0q7Vooowd_jjPTifWR-zujR1M5fSkyXo9rirRLWInl7fTXJK7tGO1E-w1heB-p7tsaQ_xuSKFQgXiTmAMEoaz0G-PmfrxKE0zNVTWJHiArl5LxLOym8jRb1OyXKREslylL6xi-8dqbZY6L1d1ZnndFmATp4Fltm8uB8FWsnAoRNRIz1dyO6bg6pGn1Kyug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش کبیر از اون دنیا هم رفت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78473" target="_blank">📅 13:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78472">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">با توجه به اتفاقات اخیر بنظرتون بهترین آرتیست نسل چهار کیه؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78472" target="_blank">📅 13:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کیرم بعد ی دوری بسیار طولانی استعفا داد و برگشت پیش خودم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78471" target="_blank">📅 12:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هر سری که کارت بلو میگیرم جنسش یه لول افت کرده، چه گوهی دارید میخورید</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78469" target="_blank">📅 12:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">هر سری که کارت بلو میگیرم جنسش یه لول افت کرده، چه گوهی دارید میخورید</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78468" target="_blank">📅 12:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_7AodVo5P1Ce_AQ2FYc0snSqSY3jc6WroXnm4IsS0z2UcktBSpfKXkr2wiBrmhqwf5G2yyH36jPDH61HmaTsxcjKcpS1ZGxgHPEBhPTtW6DRQHfKnqTkyrIhZ1DYcKj6GU4dgZBr23hEzAkzfTwd93JCBFunsSFRGnHZbpLUKP2bNTStWq4FuzEqhzhu4p8sm1KtK9i_80dbGh52ENCdG9RRt1cM0aI0-kG3ZG5EVln7GBr9yYKEXsKLJaZ206m-cg9L-n1l-8CguyOWmnC0LCBzI60l0-CMRr74_z3b8F37NR-KapIswiaxLq24bd1YzcR4wH22HVhjGwyIGuQ9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصر هم بازی خودش رو برد و جدول گروه این شکلی شد :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78467" target="_blank">📅 12:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78466">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHX_gjR6Uc_fI-wKnxGBEc8leVSJ_IkZwMtmhEyDviXzEQ0syvCB_4XnDpkL2_uIRyu2LATjDro7bsoPumJhokh5gV49NVwj8Oe0_fNhV09zQ2FYDdrpyzfeoDhuSkiUBxmWY0pwAGzv2Ub0Y_ynp4_4yZTyLp0eptYcpaP-oJeNUPf9Ac-HoUfkgKKLG-YJSav6ud3PpLFqIamB6nolMHRfen6srtvORjCX4cNRk7FyZnTdrqjtM9YZzwNV22f1SerI9MY8bgKA5LnDgbX95otvJvSOPSVN4KsThnRID2T2EhfIt1zyhhrbo7lOSub-621H8QglFKXJeyQRZLlB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب الان این چیه کیرم تو دهنت
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78466" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78465">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78465" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78464">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4A5iEm_hduIkQBui_MAwEo_oF7BbBTqXa8MKbq60tpxlCOuESdmTNysnHUt03Lfd49aqk6YYVBBTDX2FB2nKkWdSMQWaRJwClLms0EIXcrx0BTYQD_Gl_kL3L37GtAApfgmVE_Q5DSuOHBXdrCIDRQiYqeeCy4nIfYV6K6_U8-_Z61dyPn4qAIzPqBWJ-smaLlXJLRm9IH2oZMe_J4kMKKlcGTfmYqNKKhirVEvrV1dZgQnzv55y5PWKW2q0B4xXlnuTgH7AqRraV8oL-Qkeua0xgkGNJp9p14eMkfeifEC-ONaNLtzBuLWLRV4N6xP8UWl7tfQcJTeQ1X-8yywKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
R1
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78464" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxuHTnPPAtJvI63NRRvcGKLWYJS1jJoF2meJgZtOOnf8MMnh7fgWYkh_URWKMtSnSN7h6M2FPXdinMpu-QPwTHuvJvrENfNfs-Nd03sSv_Kx8p3dAxq68o3qowck6Hlz_Z6KGPi_kRESWobHcqwVFXBDhaKry7YTuTcw1skr7ePc6Bj4fMZRAI-xPe_VjVBB9lsYmivG9zDqRhQ47PxI2vS3Rk7AfsEaZlbZBCSMH4GaULC5i2_YEQVK96_4pie_GItGeAYRsv1xN8vOjfj4Q6hQNJ2LhQp4wfRl35spIkCVs1jNWU689vBzywyOwUx-LiOLNwe2NAlmOssyk1CY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشاسین تیراختور
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78463" target="_blank">📅 10:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naF-oCngAZ1RxsnjoyaDVcyeqxLti7IXLUPKV-G5f7z9QFeWVrYU4bugLTORX46Nf-7Vrio6lO-kzbZ9a6Ijih0JZLZdLJa9ncpKDC0XLQ9tjRhqrvFAzQaYprFhR3GfpvLERov0ejUah2RPRvrQPz2uu_zI5ZB-QQ1DpwnhUKdyTbPNB8958Vi1YQsDRVw50uExwfgZ7RBqZ5z7OadriRDGaEBg3S1WWUsM3gjOE0j7I6IObwZ_WVIsl3eJ9sCteST0hWElXCXfxUqPRX7ljhDSIRehGH3VMY093bENStiwcquxr2BMqpzhp0SqifJN0sOp9cVorfM8_w4fQJKyxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رائفی پور آمریکایی ها ام استادیوم بوده مثل اینکه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78462" target="_blank">📅 03:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">از وقتی یادم میاد موسلرا فوق العاده گلر کسشریه
چطوری نزدیک ۲ دهه گلر فیکس اروگوئه بوده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78459" target="_blank">📅 03:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هم اکنون ریزش شدید فالوور های گلر کیپ ورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78458" target="_blank">📅 02:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">پس فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78457" target="_blank">📅 01:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6NDTtIIsqsI1WJ2XFODSNbPhPZx0m9K4e_W1O7MGhb7BBjNdedwf2UnSlO2-wEPiZdcs9q3jt6ftN9ukQqz7mqfzaGoi2QFTo24QIqrBNdi4KbZ5apTS3MbiTTEOArusH8uBUQIWXmVv5atrey3i3ZwJmMM886tLU1MozIgoy0ey87dPQI857SoQ6vioSf3KZH7dFeKqJTF50KPbcOwNKDOtyVH6LUB4pZXxYMoRmCklg3H_JEwUxNu5jloGKaRBVYc2SFOc14LvHa5VOWtGb8p_gU5C0lK_SxSK0WsN4EQMtAf0UKH7YlKLidDLZEAaI2nLEuXBgx49WwvgL5zPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اما آخرین پست مربوط به فوتبال.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78456" target="_blank">📅 01:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الان بیرانوند هی اینستاشو رفرش میکنه ببین فالووراش ده میلیون شدن یا نه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78455" target="_blank">📅 01:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7DhUU7quAEcu5DVZ1oghvwP4HNXmgy8f_R59SIWWcsVvusK8GQvRQ_daudsJIePnTOuBr2R76yXSPjyd6wmfvAAKR5h62JMDMZ8Ty0fbpkuxODMA0vYqcArue0g1dYPAlWVBpDMXLO-ImFQBriSzAhscMs1OpAhhMocRhB-Aeomj2-kHfGTprCOXTmfVcVYAplM2JUoK2H21jgSn3I8Cm8Yyr43mNi5dFLBHbAosc6a-NPziwI_jmsFiGkpiBr2NUqjCuIJq45MLVSWMl35N-XOVpB6TG0IT-ws-4kQrDCwK2kEDtGJKMvvY2pcnhDWIPZtr7j3q2CgYvyZgVyWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید قالیشاه: ما اینطوری از کشورمون دفاع میکنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78454" target="_blank">📅 01:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZN8yTVJBHIORFrxPkOOR5pulm16IZKRg6_go_LjYq3PaJf8Hu-DYenVy9T29O-JZqA3XNIpcjxrFPQ9mYJHjA0f4iCkMHIuIbrCCpi93q7qvBZaCxQt5Zq00-UCHD1fPaHAwXmoRJ94zBCp2z-zQ8uOrMQzniuAlUUMg59KBkarnOoGrzKeH0GHFaVZ7dP3Ehiu25r2VyzGQ9lxs3lZ0yXT_wyLejrp0U_bcIQpizCGcJm-yeDpJBbx60c8_bEvQFQkLJVoptSQcFjdncvKM8-AsqCjORHdi9fk-pPEuSqc0SHPAfpRCvsrcttTAutdy9S4_Ym8vqvOqWq5OUXIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت بده نویر
اعتراف کن بوفون
تایید کن کاسیاس
به راستی او بهترین دروازه بان تاریخ نیست؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78453" target="_blank">📅 01:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خب کصخل کورتوا هم نبود بلژیک گل خورده بود</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78452" target="_blank">📅 01:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ولی جدای شوخی واقعا مساوی گرفتن از بلژیک ده نفره اونم با شیش تا دفاع و ی هافبک دفاعی کار خفنی نیست، اگه بیرانوند امشب رو دور نبود ممکن بود باز نتیجه ای مثل بازی انگلیس رقم بخوره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78451" target="_blank">📅 01:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ولی جدای شوخی واقعا مساوی گرفتن از بلژیک ده نفره اونم با شیش تا دفاع و ی هافبک دفاعی کار خفنی نیست، اگه بیرانوند امشب رو دور نبود ممکن بود باز نتیجه ای مثل بازی انگلیس رقم بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78450" target="_blank">📅 01:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خبرنگار خطاب به کنعانی: چجوری تونستید بلژیک رو متوقف کنید؟
کنعانی: رفتیم تو اتوووووبوووووث.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78449" target="_blank">📅 01:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXd9woOWhevkjl-uHjikUkFyS-J2mJkrKh5Imhm_udvDsHkuQrUQLIKmPM9bCLCvW0ndbuPFQFTHAI3dukGcDQeOPrBAa4l2CnGFeiml8--7ix4NpENZPL9qq5UsihsrRSV5AbO1yyrK89CSv08CR6fsEqU8HwNPp-YKfAxCFJzZe-Q3pgvYpqlknHn09ST07PjS2zaO2mfyaa0smO_oIT-5pa3OUU43ks5hCHCdBUCnQbZi_a4Jlfiw3rGFXUAoSbe2cbjS3NN-XWSVEoZh2v3xgyryNdLYAwnzdx62JqT3KM8He0ErXgptmZiutMcR3TSP6rs1MeJK4Le2lBTUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شوخیو بزاریم کنار کسمادر بقیه بهترین دروازه بان ایران ایشونه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78448" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5SLAMlczhAxXuBq0vtjzhcOKcuitEaJ5cVZPixpwYgv3Z71V7fPzBHb0AzlF4zQvXvL1T38qE1wV9I9k8tkKTkvylYCi_dZgFzxIojKqPqgAQPdrnJQ8DL-NCNY6EYIgISUqxv5ZD7MtXB4oAFnc9kEs-yd3GDfXxNu7oki_0ksW3pxrU7KH-9VH2WKydF-75rVF4nvhssNQk39_T6_ng19EPl5iX-sA_jGCogFHpfapRgUpeFz6BLOHJvcINqpsn5wItOdK57sGAM6zgPRtWKpdXJTdEgEk3Hx_4tpye5WFV--Cw6zFCpISjavyXHcjz8NOwUss7miyzWn-TMAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی الان بیرانوند قراره ۱۳ میلیون فالور بگیره؟</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78447" target="_blank">📅 01:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCFotd-dzaqMJvpOAq2tcWbSou5XWeYBcP_up7QcW2UcYYkO-BICIgcvaj9pAheoIwR_0iIm4uvkTILdaKXyT6yp3ZEBYGq_rzc3L9JGw7iO2keMDJRA2h3Jas5I6q72zywhD3XuNnTLa6Z4NVZdkcKHypnVQXLd5ofYXZx59CyC_wKuPCZ7nPiVMes7Hor_CPBbEKwa-soKgWWtcLRF5StKyeVYTp1DeRzj_uMD-Ww8wQs6_miiqIMXqYrhrNmWt_3xTGIJufOryKQXerhdXWAdzH7ppYqUM1IMD_HwfuOMCTFa9Z6G3wyz-tx7-e7IBfG7ScIShGkp1sT2QEjVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78446" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78445">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htaBK-Lf-lqXco7tCc4_WleaHCHl7hMqQAtcv3apQEPBSsswDVROCJas2DQ2d-Y6lNlMLdW3VkDcFQY6-slb4gvRl_Lm7hWq5-ej2233CYcIIUVOeXTxl2okuPkCs36MJWd7Lc1M9jTMdKXmVKuBlRiCbg1IVPG-IPLl1MoDDdE08vO1aGhTbfpOT4Scj6_Z8ITYV0yOWy0uMZmINGtHUtRUNFwrkY4Epy5R6Y2mVjEcgoymcuGrvQeCyAN5WuWlsxRlESKKdibDTUwa241Z-32Fd0c2l6R_bRBTlGrLyH2R4LzYEH549rYeNb42kk9uEOHFqG5N_tJypZh_fmQdew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78445" target="_blank">📅 00:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نمره بیرانوندو  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78444" target="_blank">📅 00:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78442">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtUIVgKkhJM4UsmgiZVPN7QACHdP8D8H4iAY9m_3CIpb6yBK-MIjienkacgD36D4DwHCoszqE_wcWE-Tw13a4NYxvXXhoTxkHXGph5JeSbtaBd5p_EmLgIzsGVDkWj0XNLdNZN6Ukbd5-uJZLsax1exrUIXipIUmtHx9mSmkM1JpEEjOT_wKmtylXNlUHUVSw__CDTh-wsDJGCr2iZ81-6V6hV8FL9T7dbN2x_UxUWu-C6HR7e4rRBJms8SMD1GncVY6MPuvrZ3jqp7b4v5er2V4awWcZJpdjDhjU0pIbE_PZ6SPvpHJvpCTDEbudeAoRLiJc1L8M85hqlQZgitC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمره بیرانوندو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78442" target="_blank">📅 00:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78441">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یعنی الان بیرانوند قراره ۱۳ میلیون فالور بگیره؟</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78441" target="_blank">📅 00:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25a83c28b2.mp4?token=Z5L2StCDn9khg_g_scN6wGA1kPdSas2kHZjIYOBAJsVsO_k9cJUhSBDTyU5bZwyxjumAkqp_E0ugwUtP-nPaaGIdWydJldrGidGl-0wa5XM2l86BX3NbMe_om4J4B1IgKJHcb-zKFhNNrgqOBdHwd0wwr817OLQubxpkRGJiTPCJ8SKOoU9c2tLYzbX81wzYFUfv80teCflPOq2tMM_QE6LHn7nU8DnK-llJfLVySiLU3n_pOXonwh8RjFJ-dO-RhSF7dtoXFoI9dYLd_5HtjJCw8yah42KYGbToxAzH2Yv3QORrYol5ECESfTb3s3a2oVT291NYcdtPVL2dwtWI5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25a83c28b2.mp4?token=Z5L2StCDn9khg_g_scN6wGA1kPdSas2kHZjIYOBAJsVsO_k9cJUhSBDTyU5bZwyxjumAkqp_E0ugwUtP-nPaaGIdWydJldrGidGl-0wa5XM2l86BX3NbMe_om4J4B1IgKJHcb-zKFhNNrgqOBdHwd0wwr817OLQubxpkRGJiTPCJ8SKOoU9c2tLYzbX81wzYFUfv80teCflPOq2tMM_QE6LHn7nU8DnK-llJfLVySiLU3n_pOXonwh8RjFJ-dO-RhSF7dtoXFoI9dYLd_5HtjJCw8yah42KYGbToxAzH2Yv3QORrYol5ECESfTb3s3a2oVT291NYcdtPVL2dwtWI5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکتیک ژنرال برا بازی امروز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78434" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امریکا هم نمی تونه این تنگه رو باز بکنه</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78433" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78430">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d6215a59f.mp4?token=OZh6CgLgF6MAVGIVE-riJ4roiF3lAxJvgWXywFWUnrkDiHVRyAytw9-ZxR_Gsd7E5f0Upf0swVBgLxLgASrhNXhbqmPXqEzmq7zmAO_4SFERiOGssBgDTxRfrS04IYkHS7b9hjDGRirKyvyRLTV93cp7VWTlM0uFg79z4HXBxdmKMUrSbYrg_K-pkcgFukoT-a-_beYjIB0NHSNp-hUrR0dAtQeX4jkKvZgsHSYQUSdSswaPmg6N-xhCkp1D2Tr8OU9ZqtW8xWUUOFSbAlULXV4dYGXMUf1u8dBJgW-tgAGJShkpjsUJDN-lURZvVlfRbsgyaPSmknH5fpRbkZL9Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d6215a59f.mp4?token=OZh6CgLgF6MAVGIVE-riJ4roiF3lAxJvgWXywFWUnrkDiHVRyAytw9-ZxR_Gsd7E5f0Upf0swVBgLxLgASrhNXhbqmPXqEzmq7zmAO_4SFERiOGssBgDTxRfrS04IYkHS7b9hjDGRirKyvyRLTV93cp7VWTlM0uFg79z4HXBxdmKMUrSbYrg_K-pkcgFukoT-a-_beYjIB0NHSNp-hUrR0dAtQeX4jkKvZgsHSYQUSdSswaPmg6N-xhCkp1D2Tr8OU9ZqtW8xWUUOFSbAlULXV4dYGXMUf1u8dBJgW-tgAGJShkpjsUJDN-lURZvVlfRbsgyaPSmknH5fpRbkZL9Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح ایکیو اینو حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78430" target="_blank">📅 00:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78428">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سیاه پوست فیکس میذاری همین میشه دیگه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78428" target="_blank">📅 00:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بلژیک اخراجی داد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78426" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqPdbVRuCofhluM00uWv97o13M4x0uSzIxUmyQp4F7v65W0Qyk3ToNNbLoWIKZ1ec3kEPOJCmONytNMicxMZTXCZJd_xfOBJNFppm9h16iT3urhUIVyroqm0PTZTDX3G4koN9p-HJIJS5hfL7M_shMaFx1B1S5KMpRJ2c-TyJBSd7dj0Vl9sWKAM58H2ddF3YKTv37_1Onw7pgPbCNCrd9k0-_X7VSoaloVhG-tVpCRaKTVEJ0fDbncSzIkLK2ZuP4J4vLOalWEhAX3S-X50kfW9vD-1H7fV2TNLZ6X2QWZlTir98NYaBphbWdV5Ern5HFq7Tj_6HUAzhNXjHQx6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر تماشاگر ایرانی
رشید مظاهری کجاست؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78414" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78412" target="_blank">📅 23:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دیبروینه سوپرگل میزنه و بلژیک میبره
بماند به یادگار
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78410" target="_blank">📅 23:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78407">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عباس قانع راجب شیر و خورشید: پرچماشون فیک باشه ولی دلشون با تیم ملی باشه اوکیه</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78407" target="_blank">📅 23:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78406">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فوتبالو سیاسی نکنید دوستان</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78406" target="_blank">📅 23:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78404">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">من کاملا فوتبالی از این تیم کیری بدم میاد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78404" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78403">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فوتبالو سیاسی نکنید دوستان</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78403" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آفساید شه کون میدم   @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78399" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آفساید شه کون میدم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78397" target="_blank">📅 22:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78392" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78390" target="_blank">📅 22:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78385">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بیرانوند همانند شهید تنگسیری ایستادگی کرد تا تنگه رو بسته نگه داره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78385" target="_blank">📅 22:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بازی تیم مردمی بلژیک هم شروع شد
ببینیم چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78382" target="_blank">📅 22:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نتانیاهو:
سال‌ها به ما می‌گفتند"نمی‌توانید به خاک ایران حمله کنید."
بله، می‌توانید عملیات‌های موساد انجام دهید. «ما هم عملیات‌های زیادی انجام دادیم، من هم تعداد زیادی را تایید کردم.» اما نمی‌توانید نیروی نظامی‌مان را به ایران بفرستید.
ما این را تغییر دادیم، ما خلبان‌های شجاع‌مان را به آسمان‌های ایران فرستادیم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78381" target="_blank">📅 22:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uF5FsR6j10YzBocHVerN6Gjw-DmU_dI_eSOE3BxholYs7iFS6cBYF2obEyQF01gb6eq3WiwVoioiJtSm1WclrDHJg2zH_9WYk22V5dQ6doDPFqwF3VhOphE6qoqvYnVDWeQfrU0uW_yjyEwkhnUdYtfnj88x3GZQL1P7myuW_0MTzwCCXk6GlNYxGxXYRWIog1lTv3czGNkPx3LMer30hBHQmOtnFYFVyUVowt0KloAg89lBeR65q4Qbe_bcKkYABFQDUD24tFq0dIWND_cXJu7Yad9UWbNinaQoL4rnrZlEhGkgGF1cmwJ1AKWnWN-Lp4jjO9gzea733hA2jA-g2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78377" target="_blank">📅 21:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78376">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رو برد مساوی ایران بزنید پولدار شید</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78376" target="_blank">📅 21:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaXTzDH9nEhP3Dn0soinRBkyeof_L3f6alyx8hMqOCUa9-nVwqm1n-aUyy3BCy_IuyyiLMzTQgEqCadyrAzuGW9a6CekcAwyfURNZtmUxkFf7tvBpw-auEPhQP6e-O-u5e2TNMteuKLCmuDSTncnLWcpM2X2y2BiZZ0HHqkFFghy4gqJCJp6Ceh-15SBvbEK-ATF_Rp2wKU_yMz0ckIrlGlCp9q9LHAASITtyvSLfT6YlZ7VL59TDwNUucjRBaX5SRNeCGCehSa_UxrZujzDiuyXCYcrbBxxcHS1IEIbvRsnPqLUreFJ3uFAfYzFXN5EDWXfmCuAX70fJ2WodWUDaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال کاملا حجومی چیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78375" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
