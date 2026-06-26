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
<img src="https://cdn4.telesco.pe/file/txEDj6jrL0VBS5W3Ml8mgcXNWNzRtkXCTciQADms9K536QgiD2y0vH8NH3cIB4N3BDRnybWkPegWz_EOtdP_6TtFHH1Osl7ISGH2QVBpRRCsFbrMY5CEno2uBoTru_bjxdJ-qNxJSXyh_fOGd738oxINHIT4tEmnAJ6c6p7vl7dqYPeZUvkXWzR2EhgG0imafB0L4NYRA4Dj3mO1xQS4erpR-8rYaAdKm3uRMuOs85cKBhEIQ46tUkDvMXwctt1LLpn4Xlso_1Jt3jvlDs1Ae0EIN5Tr21DvZznf07CXvR-3zlz_eN0wCCuqSoxcoNhTDkFLD2bjRfZziujCC0sW_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 183K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 20:43:45</div>
<hr>

<div class="tg-post" id="msg-78790">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbC9FLapV29t79anyw7SXpGg_eSPn_ohX5GJLA-1zzipC8yOsM4oF3v4lqyzToS2_tKuvVqgpRuzcm64l8d-PITRLM04f3wopIvB99zoepc1-UKsBOQyyfibq7sl1UPnLRt125_IWkHWWHkhfdPUFzErqCPQTR6fvuXkbxCtpT5AsNM2Td-N2KrzViRb-AZkn0pixI8UuufxmZtEGTrIp0EonZbk1UJflkVRyFntLYb3BFPswpunqcWfgGCCEShP0Lm1kppIvSOZ7IaxjtyPo3UtZ_oreMecpylkdldNIzH0pyl99Tz4ciIRFhJqnmA1sC3YkfnZhQ_d_Wxuu4hxfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارگردان موش سرآشپز اعلام کرد که قسمت دوم این انیمیشن هرگز ساخته نمی‌شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/funhiphop/78790" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78789">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g - کاربر و زمان نامحدود - 480000 تومان
🟡
سرور 100g - کاربر و زمان نامحدود - 530000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/funhiphop/78789" target="_blank">📅 20:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78787">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">چیزی نیست دوستان قعر جدول لیگ ملت های والیباله  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/funhiphop/78787" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78786">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phCXUAi4vCoDXUL1K8LQUoznOYFSCNSHsAJQq9qwx8hq6orjxWxrvd96v7qHmBxyuCdP3aUGXo4XjlIAz_fcl49lFUTId-kPVmaumKZOEjr7HEmhmyS3iXZLk_eTG6S1rglnBvxRpyE-FSW55hlK3t5dPhfFF5nJUU3pnmSc0EoLITc80ekePkAbjqIPqN7VcV0j18pa2LKgo2SreE1gsYr6pavF4BgjC-BFJI0LL2qfHSDCpIwF7LXpDBhPHrp0K8HdhP7l8fZ0C5oIUijAwte4lzBe1BT4pP5_Ni-e8LInBVheQKWTt4ndkhl0x1A0cioCzbazyV2aaKFIEtIK5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست دوستان قعر جدول لیگ ملت های والیباله
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/78786" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78785">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDr_pZpSihWOSFCY-xaeVEzr7AHDmU5a6fFI5DonBSWHlZqAtyqVMgqMJNhoTMspPcTKcjSdD6YHIwVxftHlJpwAqg1lM5jQ7UKb4Ylue-l7MAjYUhQj_QsEvzBq5lA1OywyRx9P6xRkCEWRlSy_GyTMZbLCoKTb9nW6Jn_jDsbJPDtl_Nvd_EoYh4BCPJbWCk_UOLl2SOB-DLPvBzClAugpOIkLVMRd6fNMJ5CoZkJ4OBd5Jbxk2ro93VA61BadDalWdwNgPACOYXfi-TCZrKfyh9K3xlxwg_DXah-M5_iajC1XLRJLI5QTOWGVjds7A3xw7vMEAAjf4ue43Bn_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/78785" target="_blank">📅 19:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78784">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">امشب نروژ، فرانسه را تحقیر خواهد کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/funhiphop/78784" target="_blank">📅 19:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78783">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">این دیگه چه عنیه اینستا درست کرده ریلزارو فول اسکرین میکنی نمیشه اسکرین شات گرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/78783" target="_blank">📅 19:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78781">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کاش این قضیه حمایت از همجنس گرایی رو زمانی که شیث رضایی و فرهاد مجیدی تو تیم ملی بودن گسترش میدادن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/funhiphop/78781" target="_blank">📅 18:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78780">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYaDawQsbnx4vzTotWN34-y7ie4_Q5Y_gUn65sD1igFoD0aB2BfcfmHk70GGCaavO-23YIf0z_ECjN6PyAjyxsYSeKrEUg_34cCuqySkUO44xUp59VAisajMkbTszCbjpDdnXgEC-SwzMGkkc1p3qfV5z8zjcP7R01ulsvDEvf8UCd8QbdH9LM5CisTLSCnony9noFM5xTF6u2X7mMFMfPKyIgIDOP3tXVPRz3v_PLKyxLRSh06cRMAdfQaRAMX3izioO3YrdlSuNF2uruYJY7eKERaQd4a_72rEb5P2-E-zeiuWwg8Sk78Qy8q1zDcDObmHVL_2HBVZAa3mrIBy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/funhiphop/78780" target="_blank">📅 18:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78779">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyIUXq_rdrP8hBmMg0mOrq-acEICn4DOGOm9cDwEksINQ0J_TmIDHePnI8NPt0UWKv4byFepxwFDTOMXTqCTo8ObVDmCvhUTxGyfEsOJbJGdPOOWg8mhPUkMqxO4qRQF6IGVuo_ve9nzzsRXYvY8MRp_BXEFrfaAJR3TDVPFStSEgGWvSm581ZQTIBTLAXM6XgIDKp1ZN2a9kHXi434a7hvG0Ks65VMUiP0VBcG_cwtK-ND4tSjOEIP3O6CqER0UfgdPDfZQmoilDquLA-PwWox-H6x3HrCxA7ExIOV4tLWrI2b2vw5uZwdWove1pFiFWpv2hcsG9yu-jT0ek4UiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبی هیجان‌انگیز از جام جهانی ۲۰۲۶ در ریتزوبت
🔥
⚽️
فرانسه
🇫🇷
- نروژ
🇳🇴
⚽️
عراق
🇮🇶
- سنگال
🇸🇳
⚽️
عربستان
🇸🇦
- کیپ‌ورد
🇨🇻
⚽️
اسپانیا
🇪🇸
- اروگوئه
🇺🇾
⚡️
وقتشه شانس خودت رو با بهترین ضرایب و متنوع‌ترین بازارهای شرط‌بندی امتحان کنی.
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
G5
🅰
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/funhiphop/78779" target="_blank">📅 18:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78778">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/923838e44b.mp4?token=VO2KRxEiOBzsUU1ljebpjclBGr99g6pCHUAf3sDEVLOJvBvogfT0eYDUwFv77oPWXgjkfmKsjbJFYw7Ts3ZWBfMktOPk60C4FKPWU_GsJ7uTlNqGt9ZD3zHegcFc4FuneiPQ13ifT1WW53k8quCLvWYs7LIO8mwgSBGitfsep0FlgvnXIawUFglYa5Uch80wL4RxMk_SaAZK_vX2FZtX4DbQY9wP1a_YIV4nZIamichNGF7nifjYqil0S3v0wp5Be9_-fZvgfbulgWULCOMnBUhLlNhs94KtDSzSyIru108JwbETgKdAWqLG3sToS9MsIfn7MNCV_VDlOSrSOyMJOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/923838e44b.mp4?token=VO2KRxEiOBzsUU1ljebpjclBGr99g6pCHUAf3sDEVLOJvBvogfT0eYDUwFv77oPWXgjkfmKsjbJFYw7Ts3ZWBfMktOPk60C4FKPWU_GsJ7uTlNqGt9ZD3zHegcFc4FuneiPQ13ifT1WW53k8quCLvWYs7LIO8mwgSBGitfsep0FlgvnXIawUFglYa5Uch80wL4RxMk_SaAZK_vX2FZtX4DbQY9wP1a_YIV4nZIamichNGF7nifjYqil0S3v0wp5Be9_-fZvgfbulgWULCOMnBUhLlNhs94KtDSzSyIru108JwbETgKdAWqLG3sToS9MsIfn7MNCV_VDlOSrSOyMJOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمام سجاد شاهی عجب موزیک خفنی داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/78778" target="_blank">📅 17:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78777">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9Ysskb73pT5WItdHP-aPndZ0L4tBNunXBTyYgVm6wXO6ZKA05D6Y01Dv7DDHhex7xguz-yOkEhnIUjMr_Kru-_-UFo9ynvO74qndtVxOG-kceh6atL2sE1diT4gnixPLwHQRejUPdgKX-_qmwN7AtwESI-D7IDVLgrg5DJzBtNRntGMrRKqeQRrP-zpO9-SX-bST6bIV_ZLjJoGDKYCaB5jxaGsENPlUKciKUpPLsANAV0lx44rRYlaFyasbY95dw3MyzEGdQa3lyH33nb2NFJB-b6HhRSwCWdH6WZlRr691J1Av_Iti1f1ymCvwIHv171airkKc7QP5rvMWVU1sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپفارسی نمونه واقعی جمله "کینه میماند"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/78777" target="_blank">📅 17:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78776">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">منابع عربی از هشدار حمله موشکی تو امارات میدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78776" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78775">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">منابع عربی از هشدار حمله موشکی تو امارات میدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78775" target="_blank">📅 16:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78774">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4rC53no_eKAuWxELdfZLaWxlFfwjV1jMxM4jqN-3tZo26xAH05_a0drrv0UOpR40Qa-yq6bULd2irhVaw108yIgM8T26SHFmbahMR7FRMI4Q_wuZ9VnQ-ziyRQOS0l8vkMjAcuJjHpFDvWhR2EG-EAEWJJ7lQna_AWnqmFcBPAHmW8smvZkKik9VrzALBJOUKMXgU5vfG-m_s8w7rnpgPcnnGNvaeIat1ztSvkeyG3VRHHnpnZG59diYxCM4pLYGHfDhmeA8DJ7-10Sf77f-DTn6SrS_uWupTbj58hpWrZ4xhtqFnI89bJNzflFkonyz0zSA4b_9-qPMdran_u7Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع اسرائیل برداشته یه توییت به زبان فارسی زده و عراقچی پزشکیان و قالیباف رو هم تگ کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78774" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78771">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئال نیکو پازو ۶۰ میلیون فروخت به کومو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78771" target="_blank">📅 16:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78770">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e63ecc73.mp4?token=vBEQBP2AHMF0HdSjELSqmoI1IoAN4RgvlrziMBfY1AwNibe6b3HGqFUr9jqlM3S3JWRJDWM5fe2h_U5M7UAIHJxIoIFp6VVSn0FgNQ5Gigpaj83HNsqFAdm7dsEGNa-6Shtsu7P8-ezURChEHKPHUMidbNT39rDcjREm6i50ebFFYSpQ4ENFu6rQCtJq2zVUScST0Hoo0JATl7cS_qy1nULEV9T_f1h7QFVvPqK31Hn-bHxfxVD7gPpg1FTiiq0T37yTGoll2aPl5slS-I30jEfYwAqWAVM2YfAZUksJ3nztyW9DnENYLpV8AcZ-d35rjIhkW8O9QapksLAO2Y79cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e63ecc73.mp4?token=vBEQBP2AHMF0HdSjELSqmoI1IoAN4RgvlrziMBfY1AwNibe6b3HGqFUr9jqlM3S3JWRJDWM5fe2h_U5M7UAIHJxIoIFp6VVSn0FgNQ5Gigpaj83HNsqFAdm7dsEGNa-6Shtsu7P8-ezURChEHKPHUMidbNT39rDcjREm6i50ebFFYSpQ4ENFu6rQCtJq2zVUScST0Hoo0JATl7cS_qy1nULEV9T_f1h7QFVvPqK31Hn-bHxfxVD7gPpg1FTiiq0T37yTGoll2aPl5slS-I30jEfYwAqWAVM2YfAZUksJ3nztyW9DnENYLpV8AcZ-d35rjIhkW8O9QapksLAO2Y79cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسنّین خلق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78770" target="_blank">📅 15:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78769">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78769" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78768">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ueobnusgu-4ZclXuUlkdT_YDyiyfM1OlalU3xuhIlr7pInAcJBkYLW-ksjo1gEyTa0A8luVdez6_BoD88aX_uGaovSb2b3hmYgW7_eCHqzbGA-SKKanQ83B7RisUJHk4YxdwP5Lvuc9ntDtkGQimlVyfvpcZ-tyqXQ63RgT2PI4uNta8G4Ou-advGF1RgiJmBFysK82jOK75n5ATw0FaKFKZ330tH21FkNUzXsgE1pjkVKU0rbsEhIqFf1FCl2hL8XEBi0LLSeLAp2zcxEGxjl8xgPrEbSJzNBT7m8rv3w_g1xAE8suT6Y3PXmrAMWludgAgqV0OL7Kh6MGKhutoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78768" target="_blank">📅 15:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78767">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بهترین ترکی که بعد جنگ منتشر شد چی بود بنظرتون؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78767" target="_blank">📅 15:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78766">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینایی که از علی گرامی حمایت میکنن اینستا بهش شماره کارت دادن یا تلگرام
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78766" target="_blank">📅 14:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78765">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCdoJJUhw7f3cE13RFgNQtbga0hhVPWyzvuPu4WaoGZBTjQA7sPfM3ozRr0ebRHA4G9wGcu_fb_JFTptw1WuU6WbIN3FkhgUZYnXudfmnRol9XmOVoJOtLONyiTX9t9fbgf62vzuGIgqTMXkyge3j2Bb6V6ffrtjLPp3fmXWAFvIM5kPjDGKvPG6LXlCYRM5VxL1w-m1S8bpn0uoyjAeOOaScdrhSyBzTgUM9VkXxM7Mx02aZN5pt4qvltIyk1dV-CLXO5QZFvcN_06RxFcbNatL0_WhCAoE2OFGYYSq_t7T4BJ-8nRvZNkDbFjCNX9N0H0iPWyNoXh5qDZ4NwmckQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمبود خواب داره بهم فشار میاره، چرا دارم دونفرو تو عکس میبینم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78765" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78764">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">علی گرامی به کدوم قبله قسمت بدم نخونی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78764" target="_blank">📅 13:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78759">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه‌چنل بزنم فرم بزارم برعکسشو بزنید؟</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78759" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78758">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه‌چنل بزنم فرم بزارم برعکسشو بزنید؟</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78758" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78757">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یعنی چی که به بابام میگم سند خونه رو بده هفته‌ بعد دوتا سند میارم برات میگه نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78757" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78755">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQcOR9mY6qdwv3kabMEIM06E1jG9nfUa9_o_f3gxXbaM4clxfznnAX4N2L4eke-n89sQfoQ7OkFLCxBOrbmo69nDSHEYvpwVFCblSNQstmA1-LxgfB5iEdZrk60tyqZnKaqPD3nbRfQ2oG1L7DopHZ4-Rco3ZRtD1BvCOFOK7wUNR_z0PV2BV7gQAOe9zeijeGLLTJHQs2dnViniRPmgOYJTumODVP6o1QLjU9lyZu6EfghvAj9ABusW8AZNZV3aWtCcMNv14zzeW5zsJ7wQ679te8yhHYVz4FdNmsZ4rqoE69cjdnc_FLr3UH2coEtpbptsU-E5jlGu1sgNuhx6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78755" target="_blank">📅 12:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78754">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKCyaQRQGlkEyzsxdAyk33mt-SC08IalS6Po_c44-9ofOyJNqOt6R6Wn9cZRVvfrZQhsEoRb7Jdp60khGVIoKsP8X7TSIlEY9yVxJ_PhCbcDwOV12frli8I-af0nZBlnfTAHz4gSY2HPRf1XiHy3vkGHyc5GaOvG6HzSR4aYnPdb-Y8PNAido9LUnyZeAYM5Flfz2JfFPtrQGhVfXWFMhKlxn-u2jM-EpipAnSa_WvC1rTy2cnoH9frlr5EUPE4XIU5AMC6ArJ6cG09P_S9ul5ACr-b-FVcF5thkp196T1FVCnfl59AYD9ciSozEczyUL6z2i9P7PAbFOIu6_qIteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمومش کن تروخدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78754" target="_blank">📅 12:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78753">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مصرو خوب نگاه کنید، وضعیت ده سال ایندمونه اینطور که مشخصه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78753" target="_blank">📅 11:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78752">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78752" target="_blank">📅 11:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78751">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRr4ABEaipsNoTP0sD0MWR_GQIGNoisxWYtXNNjw0vn2j6dGxhxTI92u0qWrf6J6tQ_WUZBcnEYUndTbBVEdijvzcfQx0sq8hUEctikB2cWP2Gshes6Ml6kxCtt1ZZc3jBiMPib-gktx27Kn4CYv9_fifz-wW-wxhUV8Ml2C6C3OrAnvnO6_i2oAmeVAe-Pq5vyrm0Bb18_mh_DmCKcxlvHZ8I0MNMKn9u0s5Unr5C5YjxrqCOp-SsqE_lsHrnfGKkGwBPCkWI_kY2LmslySdhx9xGzMXNKfBptaDxNtz8fB5pI5N66azU-1NwRlrKqJkQY20_Lj3NRnXR1jalRZMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78751" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78750">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎉
پیش‌بینی بدون باخت
🎉
بیمه پیش‌بینی
👇🏻
ویژه مسابقه ایران
🇮🇷
vs مصر
🇪🇬
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78750" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78749">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_M4-MsEdhEdtn26LQY0oPLrz-BBfh3b5TQtJsvJqVH0_qbmnnFsHpJzDwatB15cCdFE6zlSmt6LFVI42l8111DIdDsaXhbjaCcuAijqanYcwbdNx2qabV6zqaM79RquIDRLZY99DyIIv_VfyBnjXOPgYcDzQ8IwBf70i5Or4_2BT4LAJ6Wdw94fm0jtT4lz68KJcCTzWGaJOzUqsYmeZKfHwua6byqIC8XzRe6D3xo5ZbcGEQBCpDYgpHuIKAB94m37COOC1N8nVk7nhlS2HetFIHBBHoMn1xmWEmxO8GN8FLabjAL0SYpVKx0v15oRSUnuGOou7wKChA5XpP34fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
برای اولین بار در ایران و فقط در Winro
🇮🇷
🎉
پیش‌بینی بدون باخت
🎉
ویژه مسابقه ایران
🇮🇷
vs مصر
🇪🇬
✔️
حداقل
0️⃣
1️⃣
میلیون ریال واریز کنید و روی برد ایران
🇮🇷
شرط بزار ، در صورت باخت از وینرو فری بت بگیر
🟩
⚽️
اگر ایران بازی را ببازد، تا سقف
0️⃣
1️⃣
میلیون ریال،
0️⃣
0️⃣
1️⃣
🔣
مبلغ شرط شما به‌صورت فری‌بت (Free Bet) به حسابتان بازگردانده می‌شود.
✔️
تنها سایتی که این بونوس را ارائه می‌دهد
✔️
فقط برای مسابقه ایران مقابل مصر معتبر است
✔️
حداقل شارژ موردنیاز:
0️⃣
1️⃣
میلیون ریال
چگونه فری‌بت را نقد کنیم؟
کل مبلغ فری‌بت را روی یک شرط با ضریب 1.80 یا بالاتر قرار دهید و سپس سود حاصل را برداشت کنید.
🅰
r5
⏳
فرصت را از دست ندهید!
🎰
همین الان وارد شو و فرصت را از دست نده!
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78749" target="_blank">📅 11:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78748">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دکی ناموسا بیار پول این ویناکو بده کصونه واویلا بازیاشو بس کنه، همین مونده بود بیف سر قرضو قوله ببینیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78748" target="_blank">📅 11:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78747">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بابا خستم کردید، چطوری هر ده روز یبار روز دختره</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78747" target="_blank">📅 10:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78746">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بابای رافینیا پولای رافی رو پیچونده، و الان رافینیا هیچ پولی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78746" target="_blank">📅 10:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78745">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ویناک خطاب به دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78745" target="_blank">📅 10:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78744">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چند روز بعد شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78744" target="_blank">📅 03:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78743">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هرچی دارید رو ببندید روی برد هلند و ژاپن
این سری دیگه جدیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78743" target="_blank">📅 01:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78742">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج  بماند به یادگار   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78742" target="_blank">📅 01:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78741">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سلام فرید جان خیلی وقته که دیگه صدای انفجار شنیده نمیشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78741" target="_blank">📅 00:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78738">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سیتی عجب سکسیه، هیچوقت تیمش ناقص نیست، همیشه بهترینارو میخره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78738" target="_blank">📅 00:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78737">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">۹۰ درصد رپرا و اطرافیانشون حرومزادن، سعی نکنید بین اینا خوب و بد رو جدا کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78737" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78736">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbo-Z5M51-k_cHQnNMCCU_4E_oL_z4JH2XIIwFUmcdM938h0xpeb6ZhiJcMcRW5YjzgMdoKsOJ7MZ2e5ligbf_Jena5hLLExZdUClAUGUNeTp7dNSAA1OvvnP5TGaEKmualH64UD94bTmVEJUYp5RhTyQipLUaVQVcdI22PzfPRuWtfgiU-kKVGZdLCOTQTPvRO5REnbwUK1JTGX3isWv8unMqOKFomt69hNrG9X50yg3GZl9LCo8uV5sUTZnGeM_9fCbBK-d-zJ2qBQDfDbybHi9svVPE2rMjMadHDN4Gj-iGQamfQ_y6F6GmaI-3uYKWiVIIio_76RL8Tx6ARblg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو اسرائیل دنبال قاآنی میگشتیم
تو هیئت بغل عکس خامنه ای پیداش کردیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78736" target="_blank">📅 00:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78735">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTzf6hcITUoPKU6hQTqln3Wg7koMR_TPNA_i3_Nsc0UzV5_eTGGaoYQkOrlpJkS02LXoZR5bzOBA92n_5IOPB2hKKge17QDLDshdOgZILpjsUH-aq1RDlcUXPD4O7rZ7Dm-0b63qDTDOjW9-gIyoTqE-mkxRoONlXuzpALEIXM3-3Vka6m-RMkDhwTwJxxdaz7LTRvY6VIc9IBwKA6i4YFPD10HVgO747NbYw78_hJpoVlWqV3bc_wLdJgqC-aRPyxn7Gje8M3hDl0GhMmwhQMF8se5hz-je0zqIs632U9qG8k3-SGVziWr8KXmVfq5V1MhaWFptfgn6ubF9CEhXCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقر شاه با حجاب
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78735" target="_blank">📅 23:56 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78731">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">هرچی دارید ببندید رو برد آلمان و ساحل عاج
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78731" target="_blank">📅 23:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78730">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMvEZG416tc7CoWoJgPiRYMCF6Upn5mzJtnStFAuVOX2dBSUGoAjnIGZb1GqjExDP8FBF9ZyiON29wAIuBXjwmQ5azsK4yTA8nZyQ7I-CFapbFy8WI6yI8V9o5ngj_VBLSa_HNA-tit9K-m4SmIgNtR6ZmxBOpfvq9qqR1voUUqIbNErr9iQMyjkSPNK1QeddGkMbigTEVoGBw6Wcv5PgOhwHRYvb2kuUHfosoQeI7jQNT9EKQhP74FdRhF2C1Y-fBf9KmevvPPMxOMRqLx-jezaABaCORPoFVU6WQGdsGsbbb26lco5a_XmOrkukf5sMvBWGTWzbzqq2QCCbvWCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تروخدا منو از ایران نجات بدید، مگه میشه تو کشور ۱۰۰ میلیونی یه نفر عاقل پیدا نشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78730" target="_blank">📅 21:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78729">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We8L_gNcsrCigCvXMimkGsmeZHwamuan3yTz5z-gr9r-GGc47kcpTLiNoBNBlkSSek8l4rmV7iHbn0ifqrY699EpKmdD5cZ3iobGhTeCw8SwC1as_os0qhxakiDpRn5zV4-gGh6xFd81s71hKbKNlVMmKK7sdCpi0mmrw5PFutPB2kRGOBoVnNVnaFPLwH1Q-xx4dLJ2oizAqqFw-O2yUGveckg6DQOQXr8W2fXbfWIpVamJ9nbD9ESPdxEJkj-CZhbeqI-ZGmcW3jPM6qoMb5cT3IhdiYb_tOq1diwKFh09BOvX_w8aqMiOEV_tbfdkmv-cdmYaosaDUclGH1Np3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78729" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78728">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipTPggwmWZBJFiCR9TQX_dcryWadWYvc4_k_MNQhnaGuIzkpvcBpyhER1r_LuK8XtH0HEkM8AkaHyGTVr051gUva3wcZsrBvSL8lIfPtYjnxfBgGtqHEEUhoepldd5fg0ESaDV73a4eP-XMrwYOmUvDnohjutkM2TNZwwgVRD3dVQzKnGXYmF5mpKxZLsOTBhTPYRRbVzKI5uX2gYqwMWAH6VJJBs7tN_6ycxgFSLMAFrLRBoMp981voyWbscCKRTeFSrfcMjWBxVwLJhU2jIsTSjvNefV1FRaDm9TJEyGSxD7XD5vvtRYuRliFhTNHksTDzYxHYQsJRO77uPBp76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه هوش مصنوعی داره مرز هارو رد میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78728" target="_blank">📅 20:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تو چند ساعت اخیر کریپتو ریخت و ۵۰۰ میلیون دلار آب شد رفت زیر زمین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78725" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78724">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">لازمه یادآوری کنم که کوچک‌ترین ارزشی از ارزش‌های ما کم نشد هنوز تنگه هرمز دست ماست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78724" target="_blank">📅 20:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78723">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">یاد صابر کاظمی افتادم چقد این پسر گل بود
روحش شاد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78723" target="_blank">📅 20:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veRp0PPZuNokPFC9o_0nVmXZkag3DEG79fOI0QgRPsMha0HEzYxqJfKdwy7udpd90jkQEB3m-zvNrTLKqXeuv0sP9Lbw0JciJB9kK9Q3K103zE4blTaj1T7uApTp5hpP64hyb0JHoPZjnGEdegN86dOupIwBUD4GgArscXxlzxyXgkwPFxH-KV_T4Vl-gyqmHpoHbkGMQ2Avm4hFiwV9ERaiNRo0sqb7gNqJg1kLUZsCN52iHZAa1_6KV93R1ANl3e5ZWn7Ip-xJpCEX_mqsomrsmnYWZctusYCCHAzUaSrd_IprLDXHrs8_u01F2UwfK-ZJ1GYVCXzjR66txjDQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق حاجی توافق
سپاه باز اعلام کرده تنگه بسته‌ست و فقط کشتی‌هایی که مجوز سپاه رو داشته باشن می‌تونن رد شن.
برا اثبات جدی بودنش هم الان یه کشتی که می‌خواست از تنگه رد شه رو زد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78721" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">شمر و حسین رفتن برا فایت آخر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78720" target="_blank">📅 17:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مارکو روبیو درباره ایران:
سیستم ایران هنوز توسط روحانیون رادیکال هدایت می‌شود.
همیشه اینگونه بوده و همچنان به همین صورت هدایت می‌شود.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78719" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">میشی فروزان
بلاد بودم نبودی اونروزا
یروز نبودم زدنت فرودگاه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/78718" target="_blank">📅 14:59 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llTbKnRbwnsKwtgvwDpihOZv7al35nreaW9H4XYMVyk_3QX26yXIM3l1Iu4UhIMqXa-UmdOg2y8eJsXlL_P4inNowjlbNPBWTFt86JXrfscBjU3UStog2kZ9EvgJKcWmgndQNpK9HZhsz91yGY9yLlXJ299y9BWxgwl504_3MD2OEpFTTrRAhyGTJYCIU9pYVujKp2vwygBWhoWFslw5dC7elWAusE1g8xeU1qxLE5DaaYt0SBZB_oGVRLIEG0lq3la6yjd3hf1KQbLqAC6GbN83hIk3LKyIdczP66P_z4h9Dth9ZtKiduddIWHDR0LV5I97IjdbK9elmGBb-8yJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید ویناک به نام "Gin" ریلیز شد.
📺
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/78717" target="_blank">📅 14:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78716">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78716" target="_blank">📅 14:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCaowTlgzg6ttKbRSscj8cfgu1Gfvl0PoBnVZj_BsOf3QdYaKkcjJI6NxTE80uWyNUAM5uhmGJLYVA-5Y0kxhAug5MIPnfuPe1J-N5-KnHgLWRimlkusXFZnReSv-xzFLPM6F8q7QBxdRI03xR1MqVUW8j3M3D0iu3de-G8PIJIsFGV7scboKJUrNnr4rhWcO0Cs4znuMR5edhyPX4I5AtpRyriIrsZhMqMJe9g_OAAX_wJUcEf7eeVhbHK_P8F3N4IcTvlQE6v6lPIrlCzccnTpqZ8WTnbpuKxigFkc9M-bSJp_29hen5j66zIYg7vzFQBlnh1T9p2DuX-Kr44pKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gta خریدم تا عشق حال به راه باشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78715" target="_blank">📅 14:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78714">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">من نمیدونم داستان چیه ولی علی الحساب کصمادر علی گرامی تا ببینم چخبره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78714" target="_blank">📅 14:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78713">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ویس جدید آدرویت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78713" target="_blank">📅 14:11 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78712">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJqTwJ7lHExnPgY0FYkOA2GRb-rWqQ4E9q5Yio3nI7d8NmP0jro7blVptsmI9fAsohTwgxSMvvlH8zAFJFmpKL_7QvC30pFEMc2km3hlOFu9_Xd_sE6olEow418SW3rNH-i5-s9eTB_ZA2zNDwbN67LcEF0nZPx_bgAE18xXzSMQoHuRs1gOYvYceEMXeQMpPGwD8HJGsOi1YOzFpkJybylD24eX1buU26h-aJVK-V-W4WWqT4Y4-8_HSP_jCqYIca96lMtKudO9RG1vT2Ew8-cWXnkW7XN7o9xFrovTF7B8i2OK5fBV5ilvVKmk4RsqiNi9_Et9bZRBeO7plq0w4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78712" target="_blank">📅 12:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78711">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کاش اینایی که برا محرم شهریه یماه باشگاهو دادن بیارن کارتاشونو بدن من حیف نشه از فردا که نمیان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78711" target="_blank">📅 11:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78710">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=GZCIYbbkvK05fcMow-xE0ZRKnHkD08p9-zkacqaatj10C9wkqBYll5R50qZw_iv4OvxBk3SpGEIBo8zWBLblNgTtRxbJumXC45K3kOezzj-av52SfeC0iT7lUgOEuHW4NIcs4sTaURSRaBTpQ8QktnL_9IkOkaymhTpednT8PIXHSDU0f1wK-WJ25xJ3L1FEhnuNQoAE2t5rzPCaKQ8ha8z7ccXFo0O5WGZ1xfFvqvsZoWfaP86lBsUS2WRgh5R5shC9HeFmRz69ivq9oSD5i7RjRgO0FyOLCMOWjHmKg8DXdobKWou3htKHnvLcAZfTdquLW3BuzBwjkgnIyYdODw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ade4f7604.mp4?token=GZCIYbbkvK05fcMow-xE0ZRKnHkD08p9-zkacqaatj10C9wkqBYll5R50qZw_iv4OvxBk3SpGEIBo8zWBLblNgTtRxbJumXC45K3kOezzj-av52SfeC0iT7lUgOEuHW4NIcs4sTaURSRaBTpQ8QktnL_9IkOkaymhTpednT8PIXHSDU0f1wK-WJ25xJ3L1FEhnuNQoAE2t5rzPCaKQ8ha8z7ccXFo0O5WGZ1xfFvqvsZoWfaP86lBsUS2WRgh5R5shC9HeFmRz69ivq9oSD5i7RjRgO0FyOLCMOWjHmKg8DXdobKWou3htKHnvLcAZfTdquLW3BuzBwjkgnIyYdODw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78710" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شیر امسال خوب غرش میکنه، فک کنم بازیگر عوض شده</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78709" target="_blank">📅 11:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78708">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ذرت حاجی ذرت
ترامپ : وای! سنا رأی خود در مورد ایران را از ۵۰ به ۴۸ مخالف به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر کردند. از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه متشکرم.
این رأی، ایران را در معرض توجه قرار می‌دهد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78708" target="_blank">📅 11:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78707">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کص ننت آروم بزن خوابیدیم</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78707" target="_blank">📅 11:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78706">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78706" target="_blank">📅 10:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78705">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">امروز قراره توسط آمریکا تجاوزی سنگین رخ بده
از همین الان میگم چیزی از ارزش هامون کم نشده
❤️
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78705" target="_blank">📅 10:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78704">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fY4NAoCciT80S1hu5U9RE7Qph1r3kF5bXZ6zu4VsiOCVau5hVjBTtVi64BmMtRGm9fldnk2xxDvfS6hhp_6pj6ZJ1tl8gANFtdvAhZxuczGaIPHmSVpnux4qtgVDHCXLxbLXZvacry0LEuBVKsRhp9QXIp0ny53oppL3fya-wfjH6agUbKcUfha-_kPI6fFA85Q9-ks2cwfrD-1IndhDfxmO15G7x_v_TBL9JmkzV6LCMw2w0WBqZURYMkNdPb6oQ-AkxUb8aSwtIe3AG4Q7XxqEz_zkYSuyEb3Y26fLueG0MH_l4sEaAnT4iiegwUOh_pH0w9XMbwZzvLfFOsiVng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب 20 دقیقه بازی کرد و حتی یک بار هم مصدوم نشد
اینه شاهزاده فوتبال
🔥
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78704" target="_blank">📅 10:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78701">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=ccX3n93YKQU44L0k5mF77ZV7cqVcjjYI_5hFIAyZd0YVBHrOMSXDVvz5y1ViO6spIUNuy_7nQ1qgx1wGWTb60xSHxtU8TFftqCzneFuSBPMAV42eGhvYJxZacWZgqdWWOvtkAxhTbVj2l5fM96UIUktCjigjGDZaQhRhFJaTXxeQWuNx1YMIZX4EyfFQsukg3SCE9pRVORiiOx9H-DRqVRNvUnYAMm_3by4X9kRrs8C0YGSN4UEdvpRSEossrRHgyH65ArkcgEhVWJfIbW82ox4dMzW2wIP2efHpdbiv5LmRjYNi282Ru_4KM81KtCB_1PGJN-ZAcMM8OWEycp2hAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd2d4d123.mp4?token=ccX3n93YKQU44L0k5mF77ZV7cqVcjjYI_5hFIAyZd0YVBHrOMSXDVvz5y1ViO6spIUNuy_7nQ1qgx1wGWTb60xSHxtU8TFftqCzneFuSBPMAV42eGhvYJxZacWZgqdWWOvtkAxhTbVj2l5fM96UIUktCjigjGDZaQhRhFJaTXxeQWuNx1YMIZX4EyfFQsukg3SCE9pRVORiiOx9H-DRqVRNvUnYAMm_3by4X9kRrs8C0YGSN4UEdvpRSEossrRHgyH65ArkcgEhVWJfIbW82ox4dMzW2wIP2efHpdbiv5LmRjYNi282Ru_4KM81KtCB_1PGJN-ZAcMM8OWEycp2hAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاج اقا بنظر شما آقای روحانی کلید تدبیرش کار انجام میده؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78701" target="_blank">📅 10:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هیچوقت فکر نمی‌کردم با صدای علی اکبر که داره آماده میشه بره نبرد از خواب بیدار شم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78698" target="_blank">📅 09:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78694">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">خب دوستان یک ساعت استراحت کنید تا بریم سراغ بازی جذاب چک و مکزیک
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78694" target="_blank">📅 03:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78692">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وینیسیوس تو بهترین شبش هم باید ثابت کنه کصخله
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78692" target="_blank">📅 03:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78690">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaWO1NV071xlEmbJLeU11WreGfIpPWsaKd9RrRdhtLxGJ-jCzGJBryQFpMjLyIMMqsCH-4EbNaIxEfnZt-FiRwhswR8wfsxvjEvSe6qewADbii5yfrNCOotQ6XUSPs03-pioiXFKTnCXQglNlsm8iXyuOC5zhUhbqoL-09bD4VrUnxElzEK0PYNBLWGuBDz13tZhASOQxz-tAlZDYzfp4WOayjBkrRPFrYwBHEmCn042QwQmfBACpte00h9ZtPvrFqNEwmg4MBIrxCA0z0gr1mdTVmd6VWvSFbK3qeBqe2AOgfmNH07NIRM3jm-E6xXv3XKOZbG5SReanL1PWcvLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بایرن عجب جواهری قاپید</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78690" target="_blank">📅 03:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78688">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/78688" target="_blank">📅 02:55 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78684">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">با این جدول تیمای سوم که همشون دارن سه امتیازی میشن، ایران از مصر امتیاز نگیره نمیره بالا</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/78684" target="_blank">📅 02:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78682">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">من یچیو نفهمیدم، تیم ملی فوتبال تیم جمهوری اسلامیه تیم ملی والیبال تیم پهلوی؟
خب خار هردو رو بگایید چرا تبعیض</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/78682" target="_blank">📅 02:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78681">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">کصخلا آدم فضاییا یه فرد باهوش میبرن به دردشون بخوره، میمونو میخوان چیکار</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/78681" target="_blank">📅 02:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78677">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">من دقت کردم از وقتی که دیگه کشتی کج ندیدم کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/78677" target="_blank">📅 01:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78674">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ی پیشگوی شیشه ای خارجی گفته امشب مسی و رونالدو(آدم فضاییا)، وینی و نیمارو میدزدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/78674" target="_blank">📅 01:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78673">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شاید باورتون نشه ولی تیم ملی ایتالیا دوازده ساله که تو جام جهانی هیچ باختی نداشته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/78673" target="_blank">📅 01:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78672">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">قضیه لست دنس رو جمع کنید، مسی گفته اگه بدنم یاری بده ۲۰۳۰ هم هستم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/78672" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78671">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poCYv19EG0u18qiEIkFvSCod53x9LF7oxdY9K-6pFNDK61MiqLXRXqD23fjIqSw7GPMZqMxy3TeTsRMpSujK1KPuo6FNeEGT654mPPLZVBpfZe07r5Pl4g0aYpzHSrh1oiDs3lYhIQS3zv3G1kGoAzTpUyHtIJ6BvK4RntCM0I477MAtOeXiLSIH1-ZnrOwwZzb1x8fp4_XS9pUvPu02e2-3YmXQX54P8RlFeEgOjzor3GMIGIOWq6SSEYyKjK5AhA2sdWyMa2LE-Vkh_Pk9gcE5CSfWk5OvIdSVa43rEAb9IhLf0RZOXzIl3YgMfavzrxq7W3JaqAccgVEstC9oSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سخنی هم از مادر عروس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/78671" target="_blank">📅 23:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78670">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تلگراف: ترامپ با توافقی که الان با ایران کرده؛ فقط میخواست جنگ رو تموم کنه و تنگه هرمز رو باز کنه تا قیمت نفت پایین بیاد و از فشارهای دموکرات ها کم کنه. ترامپ بعد از انتخابات ۱۲ آبان ماه کنگره و سنا این توافق الان رو کنار میذاره و دنبال توافق جدیدی میره که هرچی ایران داره رو ازش بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/78670" target="_blank">📅 22:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78669">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g - کاربر و زمان نامحدود - 480000 تومان
🟡
سرور 100g - کاربر و زمان نامحدود - 540000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78669" target="_blank">📅 21:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78668">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4xYLmdda8oo0BcDFDkVNDA_zk6OvLGuhgJ9i_n8q56fBQrGaGtF1iYmhaIxjCpNdPqhBuh9ujBqGDdQjCD_3HP0PKgRbZs9fvMYhYW3KwEQDWbyhAzjZA8luvkOdx6ROhJc_bxNVuTzHvKUa1wKIANkoYKCVOmFgxkvoBzFzFLuyGWMU0I3C8nNW2WOC7sJKpYf3MIQ6lO8BVYarUK8R62zrt5UwOCW9NHhi2VVjcnXsdK9nTon9lvx5bTZJrfwOX9K3kiCGdm9yLt6KpO6lZojQ9J2NMCVyDEqT5IyFaAkeElgQbg5AzX-8Xsa58XKv9aTC1Gs4Og_ZpQXA6AD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام آقا ببخشید این رپر کیریاتون چند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78668" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78667">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw-eGUkUAtgY6eirM13cmbqmHiM_hKqlMD1peEeq62kFeXr4BBcekQ84IUKPe2kzd5iKs8LW3uNQDTOlgjpv1FyUye0vT057GDpq3pewnZE1bYZDBmzOnmVYOHAsMvKE9KJx45Giu3kMR8UmP0BXspwJ6YZQCcSAb49ChbBc7J5gu0zJ30BcKAiamuLeud64CYBU6rVxriQnc8A7jeoM-udLybZ-h-XmF6DsfgfyFsoR3Vh6YIBBRcTg29PwMHwLZ6nId0rqDDQ3nkXk46d-0NoFrSkYxG7eAFjqMcqipIb4lwWhd5Wmf2oXU1NJ7EmQP4OzWbvDbQSt8r1C_uUbuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا زده ها شما چرا اینجوری صحبت میکنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78667" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78666">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بنیامین نتانیاهو: چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78666" target="_blank">📅 19:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78665">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بنیامین نتانیاهو:
چهره خاورمیانه را تغییر دادیم، بیشتر هم تغییر خواهیم داد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78665" target="_blank">📅 19:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78663">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=IxH1O1MRc5-sY59BFuoWemlTEaKh1_DZY_M64CVjf6HJyrQoxqK7uw4qkwT6E6EzOvb5z6JYRLjD7e0c12yl-yye-NS7w2TtYLnC3F3Iu0R0RRfNYF9Zjcib8HLZrIjK5ZBYtYPm9p25xRAaByqiGDCaCtIoma2OlDOaXtRYS-RN8eZMXGYCKoJimTnloI9zfQHBA4HchUu_IbFLZaarAoXe5LYs8pOAhuNaayhOkU0-L_7vrWPweGRedfpfBqQUJwGAGmSg6Skuf4HYUhCAUX4oboTXu2AXDiz-jLFhHXSc4Oac6DYwLuEjMVqO0G7SW6OhG9lBNnSREu9Nv18gnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0e4cc84.mp4?token=IxH1O1MRc5-sY59BFuoWemlTEaKh1_DZY_M64CVjf6HJyrQoxqK7uw4qkwT6E6EzOvb5z6JYRLjD7e0c12yl-yye-NS7w2TtYLnC3F3Iu0R0RRfNYF9Zjcib8HLZrIjK5ZBYtYPm9p25xRAaByqiGDCaCtIoma2OlDOaXtRYS-RN8eZMXGYCKoJimTnloI9zfQHBA4HchUu_IbFLZaarAoXe5LYs8pOAhuNaayhOkU0-L_7vrWPweGRedfpfBqQUJwGAGmSg6Skuf4HYUhCAUX4oboTXu2AXDiz-jLFhHXSc4Oac6DYwLuEjMVqO0G7SW6OhG9lBNnSREu9Nv18gnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماشالا مهدی، ماشالا به این تاکتیک پسر
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78663" target="_blank">📅 18:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78660">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خدایا کاش سریعتر GTA 6 بیاد که GTA 5 ارزون شه بتونم GTA 4 بخرم بازی کنم</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78660" target="_blank">📅 18:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78659">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">راکستار:
نسخه فیزیکی GTA 6 فقط شامل کد دیجیتال هست؛ دیسکی در کار نیست (البته فعلا به خاطر جلوگیری از لیک شدن بازی)
- پلی‌استیشن: GTA 6 بهترین تجربه خودش رو روی PS5 ارائه میده؛ همکاری سونی و راکستار گیمز تأیید شد
-گیم GTA 6 روی PS5 تقریبا بدون هیچ لودینگی اجرا میشه!
-ظاهرا داستان GTA 6 مثل Red Dead Redemption 2 به صورت فصل‌بندی‌شده و اپیزودی روایت میشه
-بازی GTA 6 در استور پلی‌استیشن به‌عنوان یک تجربه کاملا سینگل پلیر ثبت شده
﻿
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78659" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78656">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=NUrlLCbFqtmikCTj8Rnx4DxCPAEri_XdeEq5KP0Hkc7v9Tq8ftgi_5awTHdv4YZYWapu3E7L4jNLKpiEZKWI19rRyCIHRmfPBHNYog1KJNmXkUP-cfiSDEhTJ-p-0RBDzuu-2axDrkQ89f9WWeB4Jq8r3LH__M-c6KuRKyzmEow_x3xVf1KqVlhO8leGzByaCckq4KPU8wJKlgkToQCSrzaO9udGZkq6IzVaVC0LyPrfLhlk49xPrro48u8ko7bcGPLopCmjU1lVm6LBVZxrgmq3X8bA7i_xy1rlV_MwDSr5SckWTIr1CIx801-Evrrai_a2CbI8s-NN0dv5nTA_L2rKmflA5fh3ILtonFRFTVFzFYs9o5pOeQlACwSt7oL-fiIf-SHCA-r0D3noUNHApvnpwxYpEZcq6WDVbn9ce-gCOGlXePp-r83CBfUvvkfnCMMxio_bFUMKEkloZlARYDwb5SzQwvK1XzK9p21N04oniX-xasV6aS8_i1LYyq-lMuZ_HbN8QkVGJLUISW1VQ_EUKv-KnLIJ88NzyXyhrED6ORJba7VvJsax5BkF-PadK2Ya_JflTQ1cz1gMZQtUkapNrTMbmbSy56GJxErbeI9z6blI0VEa_F_R4Rkgt2CD42E1ub5r3FWb0BnN9gLRumvKB52mRbSgMweino36yz8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79017d5ab5.mp4?token=NUrlLCbFqtmikCTj8Rnx4DxCPAEri_XdeEq5KP0Hkc7v9Tq8ftgi_5awTHdv4YZYWapu3E7L4jNLKpiEZKWI19rRyCIHRmfPBHNYog1KJNmXkUP-cfiSDEhTJ-p-0RBDzuu-2axDrkQ89f9WWeB4Jq8r3LH__M-c6KuRKyzmEow_x3xVf1KqVlhO8leGzByaCckq4KPU8wJKlgkToQCSrzaO9udGZkq6IzVaVC0LyPrfLhlk49xPrro48u8ko7bcGPLopCmjU1lVm6LBVZxrgmq3X8bA7i_xy1rlV_MwDSr5SckWTIr1CIx801-Evrrai_a2CbI8s-NN0dv5nTA_L2rKmflA5fh3ILtonFRFTVFzFYs9o5pOeQlACwSt7oL-fiIf-SHCA-r0D3noUNHApvnpwxYpEZcq6WDVbn9ce-gCOGlXePp-r83CBfUvvkfnCMMxio_bFUMKEkloZlARYDwb5SzQwvK1XzK9p21N04oniX-xasV6aS8_i1LYyq-lMuZ_HbN8QkVGJLUISW1VQ_EUKv-KnLIJ88NzyXyhrED6ORJba7VvJsax5BkF-PadK2Ya_JflTQ1cz1gMZQtUkapNrTMbmbSy56GJxErbeI9z6blI0VEa_F_R4Rkgt2CD42E1ub5r3FWb0BnN9gLRumvKB52mRbSgMweino36yz8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/78656" target="_blank">📅 18:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78655">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
پسر چی داره میشه تو این دنیا
ترامپ دو ساعت پیش: همه از نتانیاهو متنفرن
قوه قضائیه یه ساعت پیش: ازین به بعد هر کس علیه آمریکا شعار بده یا حرف بزنه، 1 سال حبس یا جریمه نقدی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78655" target="_blank">📅 18:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78654">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiZrll6r-518r8OWWGhn4WWdsngq024paxCxgiGTB3Sq5U8xMhwHNdQ1FQbB4jOn9krAC2KbekPy-eabBUE9LG20J6iD82fE0UGOwD7mu_qX02iKlpOt9SGUKE2lK-YB4xYUn3XC86Oz4R5y0-Rs9l44m4g46cdyRRxq3Tj9Ocx6fIYldLAytuA3_MUiGg0eaSel8dHW7_OX_SBZrgNRvA9CV5ckHvkujeYUO38zPsTUwJr8xyqucQjaDAgRTXSRPdnuyz7-hSgQpMZqDQywVTfsv2B0efAmVr_hufBBZ0jnpUxRefe-6ef61dG7dHHlZ3bTfJncBvaG_qqNdPjPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا بخدا داری اشتباه میزنی، سیستم بدنی باید حین پیر شدن افت کنه نه پیشرفت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78654" target="_blank">📅 17:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78652">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">از این ۲۰.۳۰ روز نهایت استفاده رو از کل کل سر مسی و رونالدو ببرید، فردا روزی که اینا نیستن بشینید راجب یامال و وینی بحث کنید همتونو فحش کش میکنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78652" target="_blank">📅 17:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78651">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نفت wti شده 70دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78651" target="_blank">📅 17:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78650">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222f81be11.mp4?token=XSIzFlorSXoXoqyipQRROIBY2j8MU1mswh68HBZFJM01mn5AdLhjc8dr9WXRfrGhrUUEuheNKuYBWa3y1Zv_Ra8Ah9I2gIXzAJkPjcce_b0JYddwUbOLBvTRT64-UCW3g3ir_Ox8tcF2rux9UKanNuNZGAKdGNgJWXxJXolgINOEjdTeTr7e-R0_PSQbFqR5r1mb7C9qMKssAlSZ2Et0K6TbXf5ljndUN5oCdCpMxz1vO-Pf6IQ_4OHClHnDFi_gIJW4J-kq4LxZQDXPElPKWwwW_3zdMcE4udybo42LkEOxwnLlgyxg7ymLJmp72ab1gIe7pUtV39Qp-wDHTRW6-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222f81be11.mp4?token=XSIzFlorSXoXoqyipQRROIBY2j8MU1mswh68HBZFJM01mn5AdLhjc8dr9WXRfrGhrUUEuheNKuYBWa3y1Zv_Ra8Ah9I2gIXzAJkPjcce_b0JYddwUbOLBvTRT64-UCW3g3ir_Ox8tcF2rux9UKanNuNZGAKdGNgJWXxJXolgINOEjdTeTr7e-R0_PSQbFqR5r1mb7C9qMKssAlSZ2Et0K6TbXf5ljndUN5oCdCpMxz1vO-Pf6IQ_4OHClHnDFi_gIJW4J-kq4LxZQDXPElPKWwwW_3zdMcE4udybo42LkEOxwnLlgyxg7ymLJmp72ab1gIe7pUtV39Qp-wDHTRW6-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">که ترامپ گفته آمریکا میخواد به ایران ذرت بفروشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78650" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78649">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سامان خب آخه...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78649" target="_blank">📅 16:13 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
