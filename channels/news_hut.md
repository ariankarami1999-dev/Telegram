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
<img src="https://cdn4.telesco.pe/file/i871apWkffRI_T15boix7iBelk-uQC8wQk7xfuk8hbA06nZiHpYC5eBI391lrpgdQtRMcsfmSdjrLHUu3DPzlPMxdgEkOlCH8wOSpBXoORbcCNEEzQkuEYSef0fQp-rUeazATDWCCnEkEUYDbX_mnurg2AqhOd8vnVbSyuMkAl51LRxZPbKLE_ECK3aLzpIN4kROSNeKqFy_bV-fwxph1yvMwdnS0TAMAnhpsV22V-X9qEiTcURTpAa9Th3cBc9mWYLAojALwsIReDNDEdaKfq41WHc74x4jN--zgqU4aU7vCFobrRDUogv361juSaq40T4JcskFZ_wV12ObN0yGuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 169K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 19:40:15</div>
<hr>

<div class="tg-post" id="msg-68267">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Prwi-zfgwY6nw7hKOFuWm97YqZ20uBuFvWJLbTsioCzirI3HIqGBtqEvWhY8ortcRvCg-QspNRGZ4q3Cpo09WX5vYpuOPPTK-GYD9nv2SoVWZ0T4TmJgKB_Rc_YMYkgqe-K8xzUYwukHNao_rNeD5r1zWeuNOfIAoGxj-JUqVvpe58scPo_ghaHjivbO1ljOK9KfYCsVQrI8YMZWTzvjYgulr3wHpqEe-7KGPJitZF9m46KKqWjsdwfVIMcALEar6DBS1L3xEdkNq0Q_8FPUTwcojXnd4qOWO0NXJhjj4HQ4yaHLJmJv6z_3Qk4pZuwCZjgneInhGCI52hxEqoGlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 523 · <a href="https://t.me/news_hut/68267" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68266">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06389032d8.mp4?token=tZCNlel5jKzQ2AdbtCW3WgGQAhDymIBVIAgF8iH2jahZfrNFZFTD0aW8sS1JaNO5wi3YGsKcixW_7Qx8PpG3Y-KzKOnMISDKePluiFCX7YsgXv1WWmVDAjyBDDCTMwHqZmsQI2lyZIiiOw0htG_wRSoW1FdHsf4sTawi7NMMx1vV54n6crSCOl0DUcawMvhHtASUisGcFaFBTPGLMYs-z6aH6gjaXMXheI2tRX7HikvXVQC1Ghm_3ftOIjylo1umtSAA4GvaUD8bWtpt5pNRndwgevoWFLFrng_eTb8sidgTsyhoeubNFo7G_3eXSgCc2mcgLOoN13pVPJNw_epcNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06389032d8.mp4?token=tZCNlel5jKzQ2AdbtCW3WgGQAhDymIBVIAgF8iH2jahZfrNFZFTD0aW8sS1JaNO5wi3YGsKcixW_7Qx8PpG3Y-KzKOnMISDKePluiFCX7YsgXv1WWmVDAjyBDDCTMwHqZmsQI2lyZIiiOw0htG_wRSoW1FdHsf4sTawi7NMMx1vV54n6crSCOl0DUcawMvhHtASUisGcFaFBTPGLMYs-z6aH6gjaXMXheI2tRX7HikvXVQC1Ghm_3ftOIjylo1umtSAA4GvaUD8bWtpt5pNRndwgevoWFLFrng_eTb8sidgTsyhoeubNFo7G_3eXSgCc2mcgLOoN13pVPJNw_epcNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، درباره ایران:
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، این تصمیم با خودشان است.
اما ما قرار نیست ۱۵۰ هزار نیروی زمینی برای تغییر رژیم اعزام کنیم، مگر اینکه خودِ مردمِ حاضر در میدان بخواهند به چنین نتیجه‌ای برسند.
البته ما در هر صورت قصد اعزام نیرو نداریم، اما پیشنهادِ اعزام نیرو عملاً به این معناست که ارتش آمریکا باید این کار را برای مردم ایران انجام دهد.
ما دیگر دنبال چنین کارهایی نیستیم؛ واقعاً نیستیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/news_hut/68266" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68265">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwK1O-t8oZaj6EIk3Pn6Kx_Z6TDtRKS_shEO4PeAkChk6vaKOLaz4xEq44D_tEWEhl_iA-YL_2iT5bIMZrmmjMEoqvpHECXFmOJgETnYGMb3eXtmle1-UbtdeC7hpgN5YhJKXYdLwtML9qP1ciW5UEmk0QFRCC-kEgAM7sUk4KFrGINqYj1aXS8CR6zkqxkAgrTDoxtpvazhY25kVyhK6JGfvJdBB2o0OpYQ7u8UqtA6s5H5y36zsS9IlVGVBbG8YvdeW9J5CumjQi1UtNDKeqgoCD0SAuGLNJPp3JO_nRHfUeA-aM2D0UYM-M-STtDTSdPC2jj_w1yCHFNK0VRh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لاشه پهپاد انتحاری آمریکایی FLM-136 LUCAS در نزدیکی بندرعباس
پهپاد LUCAS در واقع همتای آمریکایی پهپاد ایرانی «شاهد-۱۳۶» و یک پهپاد تهاجمی یک‌طرفه (انتحاری) و کم‌هزینه است.
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/68265" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68263">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=Pf99yjhevzXKvXjK1gRTi2vB2B30kI7xspe8LzrxixZ0up5mOLTccO65NeedlGbvuj3Ss4oU4wrvN4vbvhvXCqzTeGl5KGxpHcfD5KsyvBMptow9BGP4UqdUIpn9BQCPZG0NDn25XzJxwwriDqNp-Z0T5Ciu_mDYdBDcx9Vs-oT6DIHXT7UATGXAX_BysOwTIn7TAaqNK0IbMJimOYjx96GmSHE-WxVQM5LXNeTN6uAOfXUKYZcI0lbYLmYTsrbVAEZoLNN8SI2FvFmga_q8a7Ms-yAzLSgJHdFSt5ktOBzL0rb_Ovq1P0W1b0ibG7NBuCAUKuq-9aQrQ090gKn99w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=Pf99yjhevzXKvXjK1gRTi2vB2B30kI7xspe8LzrxixZ0up5mOLTccO65NeedlGbvuj3Ss4oU4wrvN4vbvhvXCqzTeGl5KGxpHcfD5KsyvBMptow9BGP4UqdUIpn9BQCPZG0NDn25XzJxwwriDqNp-Z0T5Ciu_mDYdBDcx9Vs-oT6DIHXT7UATGXAX_BysOwTIn7TAaqNK0IbMJimOYjx96GmSHE-WxVQM5LXNeTN6uAOfXUKYZcI0lbYLmYTsrbVAEZoLNN8SI2FvFmga_q8a7Ms-yAzLSgJHdFSt5ktOBzL0rb_Ovq1P0W1b0ibG7NBuCAUKuq-9aQrQ090gKn99w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عموپورنگ هم اینطوری بصورت دردناک برای مادرش گریه کرد:
من دیگه مامان ندارم...
دیگه در باز کنم کی بگه چی اوردی برام؟
💔
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/68263" target="_blank">📅 17:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68262">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=uN7Ygx_z7gph5Mvm9zNKcar3LTXTOeML06uakYetT_4XWCSPY18U3-ZA4tvwrcCmW6BuvFzfpzzd4NCm_AlZtYSZTSGvdnALxKsvhfyCxFCDoS_IKKFBwfQd62WorsUxh-fGi6iYPmdx5K4HmM7X3Scg4mrHORlCGqir4Vhcy4_V8PB-8439V8jjjXrixXWHTk3mCu4VhcMZwKtXecf3TPcEaXnHwWrpqwJ8GY9mXV_lhT2K8E3Sih3RadX8ivmmZE8Cn-mOmA_8mpzCW1pDw4QQKR6HzPjNzrE_Bhr7FFWVnbCYH2uq8kz0kiJpzJRoLvlIutkdrbxyH6587kG3YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=uN7Ygx_z7gph5Mvm9zNKcar3LTXTOeML06uakYetT_4XWCSPY18U3-ZA4tvwrcCmW6BuvFzfpzzd4NCm_AlZtYSZTSGvdnALxKsvhfyCxFCDoS_IKKFBwfQd62WorsUxh-fGi6iYPmdx5K4HmM7X3Scg4mrHORlCGqir4Vhcy4_V8PB-8439V8jjjXrixXWHTk3mCu4VhcMZwKtXecf3TPcEaXnHwWrpqwJ8GY9mXV_lhT2K8E3Sih3RadX8ivmmZE8Cn-mOmA_8mpzCW1pDw4QQKR6HzPjNzrE_Bhr7FFWVnbCYH2uq8kz0kiJpzJRoLvlIutkdrbxyH6587kG3YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام:
هواپیماهای جنگنده F-35A متعلق به نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط هواپیمای تانکر KC-135 هستند، در حالی که در حال انجام گشت‌های هوایی بر فراز خاورمیانه می‌باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/68262" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68261">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahq509R6cejKpo1XI1IxS88WOjefyVY_pgN0lhmzV9SgpP72tCpsN0XHrDnyIB0c8yAOjqxNHuyW_kxJnZKbeOoRktLY4zc37FaHQVK4UG38NOH7Hcbc3jqrxg1K6MHz2HVRmeaScmAxzxxEqrwdQobzwqjjSW2yzElPRGLd4KvEgL7XRSWGz3i4VXG8_MG4gjZzD0-17DJ5nocjZJusxB--q93tjPigvdJLEokOtSqL9S262zz0iGkF2onXJD4sEmfU0Vs6UEJ9XA3jDFd-Gp_Klvw6wyGpggOmsxh-LaHKu17Sas_p9ID_vRJ7Fi4V7ecBHVK2SKy-uDic3TKcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سال ۱۲۸۷، محمدعلی شاه قاجار مجلس رو بخاطر مخالفتش با ایدئولوژیِ مشروطیت با کمکِ روس‌های حرومی، به توپ بست، و بعد از اون
دوره‌ی دیکتاتوری و استبداد سنگینی
تو ایران شکل گرفت و
آزادی‌خواهان کشته می‌شدند
یک‌سال بعد با اینکه ستارخان تو محاصره شدید بود ولی جبهه هایی شکل گرفت و شمالی‌ها از گیلان و بختیاری‌ها از جنوب به سمت تهران لشکر کشی کردند، و بعد از به‌هم پیوستنشون، سه روز درگیری خیابونی شکل گرفت و در نهایت، روز ۲۵ تیر ۱۲۸۸ محمدعلی شاه به سفارت روسیه فرار کرد و تهران فتح شد
خلاصه که مردم حتی بعد از
یک سرکوب و کشتار سنگین
باز هم ناامید نشدند
و پس از اتحاد اقوام ایرانی
، در
نهایت به خواسته‌شون رسیدند
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/68261" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68260">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دیشب تو اوج حملات، ترامپ از جمهوری اسلامی بابت آزادکردن یک شهروند آمریکایی که تو سال ۲۰۲۴ بازداشت شده بود، تشکر کرد
خلاصه اگه امشب حمله‌ای نشد یا شدت حملات کم بود دلیلش رو بدونید
#hjAly‌</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68260" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68259">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl3TNsk80NrGid6Y2KXtRg_7y938MHMP76UIm3QIUXLs6IrXRLMgkZBkDJijcvOkJDV81fxz-fRNpmmcmYtthU3T9uNux1oVSTE7W9gaoizc7tdmWnGo4ruGBJIQThikvgV0WlSp0Q3i06wrgw46LBea0p0w2HoAKwsVkOhVH_FU5MEcavWZkGnSVVSTxblhmkfByMpuzzGurL9ysDbyt7gEChGL8LDsuBOrNChbA7i1xT1YUeDTEDpNiwdp3e1HzaTUOE0xBEYRiFsTztxIvExTO0MvwmBgZXkmYWOdS2imnQh6vFFgZyj9t0LY1_NGz85JbTiLLtDuwIPNh5vszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوارنگاره جدید میدان ولیعصر تهران که نوشته «who is D nexT one»و هشتگ لیندسی گراهام هم زیرش قرار داره.
همچنین ‌حروفDT- اول نام دونالد ترامپ رو برجسته نوشتن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/68259" target="_blank">📅 15:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68258">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">💢
مرد پاکستانی ، عاشق محمدرضاشاه
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68258" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68257">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQAQu4QGRgmmrmAx1TiISUP4MZ8RJw7k60uNrrH_FiumPmJjycEIe7yjJld9T4g_atTXEtiP1zm59MYe2lQuSFPIrqySiRXjVh63tAAC98jS20_MrnvWQMaUVhMfziSWR63HvLCIDUftSZO9LM-raoQa1vahjUTrfz6YPEDPx35XyEKpWJ1_SLtjWUejfMTSbfsetKH8vP0eibqT8LNcMWLSOfYAO7q_rK3gYxujcw3-teqG_pkxmiuwChiRF9hk6iOziYmtMGfGHJ5E57gG8Z9l5OoqjeDV_gN6UfIDpxp3yp_k-xCL4nky1cITLh1jTVzIothHA-wf-VJC6-T4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نتانیاهو سفر برنامه‌ریزی‌شده خود به ایالات متحده را به تعویق انداخت؛ این تصمیم پس از آن اتخاذ شد که مراسم خاکسپاری سناتور سابق، لیندزی گراهام، به زمانی دیگر در اواخر ماه جاری موکول گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68257" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68256">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=Oseok4iiALXD89GC5wg8kt2dhu00nrgQt8qkm8RoWrZAG50P5RuJZHNW608m_A4xeW4Q6HvaNxqzPfQ0poqUrUUy033HveKEna9ir2Mvlnrmpy362j1Vu8telMoZONPdJ1_YsFf6S8JrTmsS2QN233NPZ58sLJcBFR-mz2nMB3--M6GY7NtJyupzPCmloxziddEp13c7PX6lANSJC5Dpqye9qsLTe2PqhaObQ4c7Wc4zr5zwBIzwfwldfljIjav5LeEwr_EuIWZ9JVxG_vtJyWRx2OcAsgKyCfJ_XumKvaByCovtG_dhL3fLLUf8TbpAMBmgMXTJwd7fIp0Nif1y_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=Oseok4iiALXD89GC5wg8kt2dhu00nrgQt8qkm8RoWrZAG50P5RuJZHNW608m_A4xeW4Q6HvaNxqzPfQ0poqUrUUy033HveKEna9ir2Mvlnrmpy362j1Vu8telMoZONPdJ1_YsFf6S8JrTmsS2QN233NPZ58sLJcBFR-mz2nMB3--M6GY7NtJyupzPCmloxziddEp13c7PX6lANSJC5Dpqye9qsLTe2PqhaObQ4c7Wc4zr5zwBIzwfwldfljIjav5LeEwr_EuIWZ9JVxG_vtJyWRx2OcAsgKyCfJ_XumKvaByCovtG_dhL3fLLUf8TbpAMBmgMXTJwd7fIp0Nif1y_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش مجری‌ها وقتی یارو میگه تشییع خامنه‌ای ۴۰ میلیون نفر حضور داشتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68256" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68255">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBUImbbH47PBsBuzbROs_rCZR6MuveW8wPebRjITDIs8mt3IdTAl5KOPLYPFw_lUCT_jozJeHygH23A_Rt5e7DNz8HfzhcF5eaBTCiq2-mlvCelFi3dh9VGYYg8t_1BESNimim7Gaa-pGsZhwQoBTLBhJu9gT-fJyigglcSYmcfgW95wkC33cyAuQHaSXlu61-jogs4Hrlg8JDreQ_l1vXfem2Zp79kJ1yQTaDISuf9Nfj3XTp3ALkrQld4eIchxonPfYji4GFp449m7zfqMHGf_SWqRsDGMr_xb7n7W9tlGk-8uPzBs20MSbDlJot9Ps0mDjMgu6sBZUi55d6poNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فینال جام جهانی 28 تیر (یکشنبه) ساعت ده و نیم شبه؛
- یازدهمی‌ها فرداش عربی نهایی دارن
- دوازدهمی‌ها هم دو روز بعدش عربی نهایی دارن
بهترین راه اینه که فینال رو با گزارش عربی نگاه کنید
دیگه عذاب وجدان نمی‌گیرید
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68255" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68254">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAYYGzolDVf-pU7j2k1wg2DzFBp2rHWkRBk4Q4_58StwiRi1g5M1sNF-cTWZvUJtuM8yCvSl03KNAW0PGCmPIxg2vnaqlZFzDrwd2m_7eFOQM-bIfCajeMSDRAOsbWonYMNv3Yj4UgNgOHSd-xsCFYIpbZ9LB2c_fG9hZFij4-objtwUtTQdv7FtQQdGiZs0UufGZ_LGpkzp55dt7f91ru67bTj5vYR9ojzCbMTA1T_S3puszBY0KI_mTZY90F8jQxOe_X3BSAtSAMcR43n3sPG2WPrRPEr2Ab4sVAhdGTXLZiG77jL31zOnfLn7f_zc3gXTt9yWV9Pf5oiTSudqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:  کارگاه قیرسازی حرم آتیش گرفته!  @News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68254" target="_blank">📅 13:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68253">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=KyQLTae1nmQEVeW38HABCxud_WkMPPbew_SKjYTX846wz7NQYVGDxY0uw1nB_p2y88ZJFXsfSk7J5hyilADCRL_8gn7mfsx50lwxwAzrLV0HM3lNCgq3T-YQGrNvc60LwWWCo42a3RK1Ue2kQYzV0WfAcKZaTy9pS8Q9S6TLOZslHTGgDTBiH4h7iuiRp2XVcVm52tZ0bglu_5XzmGaL0XAV9KnwPMReaVrpJi7yPGUYXg3LXUQ-2EDZH8C42yLrpxlyDG-SEMK2wx8pO80-maeJBkCNUCTRHaHlV6ZnqtyvnUowKKAmdHXd9yq20bUg_q6_2JdK6iALRMedhp3AJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=KyQLTae1nmQEVeW38HABCxud_WkMPPbew_SKjYTX846wz7NQYVGDxY0uw1nB_p2y88ZJFXsfSk7J5hyilADCRL_8gn7mfsx50lwxwAzrLV0HM3lNCgq3T-YQGrNvc60LwWWCo42a3RK1Ue2kQYzV0WfAcKZaTy9pS8Q9S6TLOZslHTGgDTBiH4h7iuiRp2XVcVm52tZ0bglu_5XzmGaL0XAV9KnwPMReaVrpJi7yPGUYXg3LXUQ-2EDZH8C42yLrpxlyDG-SEMK2wx8pO80-maeJBkCNUCTRHaHlV6ZnqtyvnUowKKAmdHXd9yq20bUg_q6_2JdK6iALRMedhp3AJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تسنیم:
کارگاه قیرسازی حرم آتیش گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68253" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68252">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVaCSL5XtNsXqbHm2kH6a6Q9Wg8OlXq9S6wURjxJYxxTTEly5YlRYruV-8iinUOcmqBkecFMED7WfLubedV7GG8dKqc6OW-jk9-gYJFAVmOkaiD4ch1CBVttx2_NBL4l-qGUTKFAcP-Jkb3IIWHGNLHkbXhybrKOQlO0SgbPMgIHx7aFdqzCFsZaSz5QUVtYOWwPI0mgo-ZXg_JMjcE89AMxh8DP1SK0vcceHb9rIHgwaCUd-8Tl6k9pNjUzWpfwpeM1xo_qLvxrxlt391gNF9FQQsUkkRL09KaVv2_MvF0kAx0tO9ysUrwX2ftyS6MvTJIdk3ViyPJKX2cVASEHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتش‌سوزی در حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68252" target="_blank">📅 12:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68251">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314324694e.mp4?token=W6BvFi11QIA_YFtSL87B0voeKMIzqAIUU5-QePjIbZKDbx4INGeeM1_4HnBw7rCjgC4upCEl8EMr-Y3PVgncRFKQVufjZGIjI9z-nFywN6XRgLrXx_lfQmRTFhwE47hNCLzJddNBzJEypBkzbg0LKhi2QviC15Kx1D0e6LAfRpzn_9CceH90TOF1Z4sjZ60ESQy74GackiBnvL9RMgac09TJ_cFmq5JcvL3I49EFjpCSyDV7f7ubI9Qa278G_Kn5sx7ZRfR0Fi_FlbEnhR7QHvCZ6zJU0VWG9YthXCzv85zBL4pWOdUdjj0cWxI94OvRtIaa7xCLzxviTvczAsz_76G0DqxQyDAqW1G_FNmO1GUpgCOu-Bi7ZLoN3ZovuzU9HnEO5E_uN5OfcVVr2ignhUpfB2jRMQOkz_V7OMO2CD9VpgYcliMsDzZwMmaRk1Y3v3gaFjKzd4uCPkajxFe2eCs1YixdsPAorD-9F4CPGbkiZJXw-UWJXjZ5y56M0V55Alsu2rhEO1ER0NfV-5PLkwFHXtQN_GlzqfhRNdIwlclDKVaVxUMit34L1kQ4siM-8F9BX6u8qx8BFnq6n17cq7NcnxmGE45Pz2UzrsWumkG0u0u7XSVYMMkWvdr_vLaB4b35QYrNLq1Pi2bTkO_Ur7E4x_WqMt5yg6Go4JbFGpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314324694e.mp4?token=W6BvFi11QIA_YFtSL87B0voeKMIzqAIUU5-QePjIbZKDbx4INGeeM1_4HnBw7rCjgC4upCEl8EMr-Y3PVgncRFKQVufjZGIjI9z-nFywN6XRgLrXx_lfQmRTFhwE47hNCLzJddNBzJEypBkzbg0LKhi2QviC15Kx1D0e6LAfRpzn_9CceH90TOF1Z4sjZ60ESQy74GackiBnvL9RMgac09TJ_cFmq5JcvL3I49EFjpCSyDV7f7ubI9Qa278G_Kn5sx7ZRfR0Fi_FlbEnhR7QHvCZ6zJU0VWG9YthXCzv85zBL4pWOdUdjj0cWxI94OvRtIaa7xCLzxviTvczAsz_76G0DqxQyDAqW1G_FNmO1GUpgCOu-Bi7ZLoN3ZovuzU9HnEO5E_uN5OfcVVr2ignhUpfB2jRMQOkz_V7OMO2CD9VpgYcliMsDzZwMmaRk1Y3v3gaFjKzd4uCPkajxFe2eCs1YixdsPAorD-9F4CPGbkiZJXw-UWJXjZ5y56M0V55Alsu2rhEO1ER0NfV-5PLkwFHXtQN_GlzqfhRNdIwlclDKVaVxUMit34L1kQ4siM-8F9BX6u8qx8BFnq6n17cq7NcnxmGE45Pz2UzrsWumkG0u0u7XSVYMMkWvdr_vLaB4b35QYrNLq1Pi2bTkO_Ur7E4x_WqMt5yg6Go4JbFGpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام تصاویری از حملات به ایران منتشر کرده است.
این تصاویر شامل برخاستن جنگنده‌های «اف/ای-۱۸ئی سوپر هورنت» نیروی دریایی ایالات متحده از ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس آبراهام لینکلن» و شلیک موشک‌های کروز «بی‌جی‌ام-۱۰۹ تاماهاوک» از ناوشکن‌های موشک‌انداز کلاس «آرلی برک» است.
اهداف مورد حمله شامل پرتابگرهای متحرک موشک (TEL)، سایت‌های پرتاب پهپاد، هواپیماهایی که پیش‌تر قطعاتشان جدا و از رده خارج شده بودند، و یک دکل مخابراتی بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68251" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68250">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlO0y1BmTZlmKQHlE1PGh47EtMZTwinyZEpmWw_aCDqNEv2Z0EsOIdfkNg6nIrmBp8B80xwcus7a5SmE8Za33zu9hFVO6XcdVLRORTLfeqkX21yaRe2Pp3IaxEAOOy3tcm4WC5-JJOVV797hTm9DsTZkW-LSX4SiDnbbJ2aFyLpvAk5RxTQ3tMVxcxd7Q2kWJwbo6rU99HVuHf3F8ITQWhcG4mI2zHrU2Tj8yZm7QEYw0MU9bME5t8qs7265MS66i-rcvL_DL9NAnaTDZBuzjaLiZTLvSOlaQWak1m14jYjMdBDRCm5LAXdcj1y1fgftEePnjDW7nXK385rjiv6CVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ:
ایران اجازه داده یک شهروند آمریکایی که در دسامبر ۲۰۲۴ و در دوران ریاست‌جمهوری جو بایدن بازداشت شده بود، از کشور خارج شود.
این زن اکنون در سلامت کامل و شرایطی مناسب خارج از ایران قرار دارد. آمریکا از این اقدام مبتنی بر حسن نیت ایران قدردانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68250" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68249">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=nTjCUxwO1M8kkDwqZCkbouyunaNn_-U9PfFj8jeumDxXwMzwTwSCo48YnFSOAMZUrmnIECCNw83-kGCEoSIZU5H_7gsdjJR9gfmsyY-aRczK4O140OgBd0r9zJ212rW9I3oA3kLqYm0MqItUvo7gSH9YCd9vkijJsoJMXYhjJsEfWy_2uiwTq1R0gDgsdY78TGRn4ivXkIAyb1DtlofHCD7m0znjT_DpGXm1GbmPmRst7dwCy4MzyYhzQPfHbNgakTQfCjwGaTBgwOgGz14mxhok3KfDcATiqmLwJAwOMrW0RUJTwPKbEVu4GGb-GJ9efS8fwPAnJZbz-RSui_q4qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=nTjCUxwO1M8kkDwqZCkbouyunaNn_-U9PfFj8jeumDxXwMzwTwSCo48YnFSOAMZUrmnIECCNw83-kGCEoSIZU5H_7gsdjJR9gfmsyY-aRczK4O140OgBd0r9zJ212rW9I3oA3kLqYm0MqItUvo7gSH9YCd9vkijJsoJMXYhjJsEfWy_2uiwTq1R0gDgsdY78TGRn4ivXkIAyb1DtlofHCD7m0znjT_DpGXm1GbmPmRst7dwCy4MzyYhzQPfHbNgakTQfCjwGaTBgwOgGz14mxhok3KfDcATiqmLwJAwOMrW0RUJTwPKbEVu4GGb-GJ9efS8fwPAnJZbz-RSui_q4qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پهباد شاهد در حال رفتن به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68249" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68248">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=USAzWNXmfW-Tg4_-aAqTAEyeo2Z9tQycbXDBDoVN9PLvKaf5dngueVmva82FhMvr7NnCs8DDpo8cMsKaedfnop03ANZyrszP2O8qP6CxEINm0D3Dct2sRnufrZgQ6u9XXCZVxnwiIx11Pqna6R4fug1dg2OmUuuxc-AGP-xXtlo0tBausAPNe3nPe3XQMU9eWE0rj_Nak082iYjezpSqEIK8Kh3ppXqnXqIYhwM1VFLnhcpsc3sFt20-F9NnvO8e7YfIc6JioIEKGI0fo2fK6ewJO0kAbx-9Nm_CyxzIXXHDV4XnxCqrzk17VwT1VUq5IoQwwfCZzC_ZfFAeQNmKtqnfHO3hotQ8GhgdCOpLmxVpBxGvndqf2LX2MeaooaZPvxwT2npRh4xmjEMyOorgf2yW02YVgrOczx5AemWgWg9lBf8WQDxATCWp6rtRRnfxDxGmn-fA08gnhrZ-IXA7DOiBmHoqEFEb30tFhdw_DMVSplL2LUvu4ijj_r55xznqXITXUENpWaeiFWJdTsgxJMEm6lj-EOE3_xlFlovk2I7AyuzxT_N19-0jTLBnNMcTnx_c2fKuXGPKuUQ88tttJOi-cn6hpCz1f1B12L4eL9avmIxm-p2eC8wJ7Th21djIwRMl2u2otnZWutbtLif7JpwzfZgQEYtzUxEFYnxiiL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=USAzWNXmfW-Tg4_-aAqTAEyeo2Z9tQycbXDBDoVN9PLvKaf5dngueVmva82FhMvr7NnCs8DDpo8cMsKaedfnop03ANZyrszP2O8qP6CxEINm0D3Dct2sRnufrZgQ6u9XXCZVxnwiIx11Pqna6R4fug1dg2OmUuuxc-AGP-xXtlo0tBausAPNe3nPe3XQMU9eWE0rj_Nak082iYjezpSqEIK8Kh3ppXqnXqIYhwM1VFLnhcpsc3sFt20-F9NnvO8e7YfIc6JioIEKGI0fo2fK6ewJO0kAbx-9Nm_CyxzIXXHDV4XnxCqrzk17VwT1VUq5IoQwwfCZzC_ZfFAeQNmKtqnfHO3hotQ8GhgdCOpLmxVpBxGvndqf2LX2MeaooaZPvxwT2npRh4xmjEMyOorgf2yW02YVgrOczx5AemWgWg9lBf8WQDxATCWp6rtRRnfxDxGmn-fA08gnhrZ-IXA7DOiBmHoqEFEb30tFhdw_DMVSplL2LUvu4ijj_r55xznqXITXUENpWaeiFWJdTsgxJMEm6lj-EOE3_xlFlovk2I7AyuzxT_N19-0jTLBnNMcTnx_c2fKuXGPKuUQ88tttJOi-cn6hpCz1f1B12L4eL9avmIxm-p2eC8wJ7Th21djIwRMl2u2otnZWutbtLif7JpwzfZgQEYtzUxEFYnxiiL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون طرفدار حکومت:
من الان شرایط ازدواج ندارم چون نه خونه دارم نه ماشین
بدیهی ترین چیز برای ازدواج اینه حداقل ماشین و خونه داشته باشی اما خب من ندارم و پدرمم پول نداره که بخره
دلیل وضعیت الان بخوام کوتاه توضیح بدم ؛ سخنان حضرت اقا یک طرف ، وضعیتی که مسئولین درست کردن یک طرف
الان ما باید تا30 سالگی بدوویم تا بتونیم یک زندگی متوسط درست کنیم
الان یک میلیارد طوریه ک ما شما با هفت الی هشت سال کار هم نمیتونی بهش برسی و انقدر هم پول کمیه که شما باهاش نمیتونی یک واحد اپارتمان بخری
با این اوضاع 50 شبه کف خیابونم و هیچ ربطی بهم ندارن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68248" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68247">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⏺
صحبت های روح‌الله زم درباره حلقه نارمک و جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68247" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68246">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYp0b4gh2gqoRfL4EZJ4w83Wo6HR2FSR6N_CWh93-_x0xmKCjvCLGNkRRbCNPGp9l4_-RBU8v654nIZbKtg3Wj8khi_HbEIJTVNyO7D6Gujjl7ob3jAhXZTVuCCK7QXTBRyYJydz-VftSUzp-vWEO5la7FhlTFHDYYOFVUQPKW0mhvO-cL_PLxbuNDpHnSZMg_nePjojVXYhLLeZ2Gdu1Li7Hos9VQgcgYmEwmPsQWfX9uGz_pxsXh3kNx22gQlEclPrOtYaVbnD8BUEbzwk8XRR_bO-YQDAobLcTlWCN-H6aeCxMvZEvy6NFFPvYLHnO9Yfx_3MuQiv30ylMQZl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان به نقل از دو منبع آگاه:
دونالد ترامپ، رییس‌جمهوری آمریکا، در حال بررسی گزینه‌های گسترش عملیات نظامی علیه جمهوری اسلامی است. به گفته این منابع، در نشست سه‌شنبه اتاق وضعیت کاخ سفید، راه‌های تشدید فشار بر حکومت ایران برای کاهش کنترل آن بر تنگه هرمز بررسی شد.
بر اساس این گزارش، ترامپ احتمال عملیات برای تصرف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و حمله به تاسیسات زیرزمینی کوه «پیک‌اکس» که گفته می‌شود با برنامه هسته‌ای جمهوری اسلامی مرتبط است را بررسی می‌کند. با این حال، او گفته است ممکن است عملیات زمینی برای تصرف جزیره خارک را کشور دیگری انجام دهد.
سی‌ان‌ان همچنین گزارش داد جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگویی تاکید کرده است که جنگ تنها با ابزار نظامی به نتیجه نمی‌رسد و در کنار فشار نظامی، گفت‌وگو برای حل بحران نیز ضروری است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68246" target="_blank">📅 09:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68245">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68245" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68244">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sh2c7CiExExDZH_6VF5C6tdVG9rMUcQGnyFGy0YG7fkVv3rn24zEBONEuOkVky__U2AwTVIl1V61XIi8mVoThO6LluGLhJ1_4gJmhR3v_I5fxTpXnEpIPNLcP9cOOjNzPoQyGVWIp7eU-3_x8m0hUUMY-H4QgroNE9B4eCmaYDS0EZw8QJI68S7Fad7iCMpkYM0MtQrAk-ekT4BQbhKGipAWZL8jx4YhG9ts85QvYURc-ny17Yig0amG5SznsBvdh1IoObbxCkjpseh2ytTZiQ9eXJV7pPMRNvE6YvpXC2lGT38tjBPnb7Aj-5LITqBLdIy8YkKIKXtM7dHMGB9LIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68244" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68243">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=Lo6AKHUP9Fk5clS3OJv7rfYNKvB54WW8jUMgCw6mOEWR93gtkwZoH-K26lV2Y-R4qg-tw9LA0oive37t8nvjQm_XCAL9k_6I_ALK5lyxXFGyLoAaKVK1F5o3b62awdb1gSdF0OokYztiQ3EMXeIIfe4AHUb1fF09Uv4uGUvy0fc2ndPT01cMyYzeEeYJb1vUdMupmXPEC2_NlZ9l71K3McweZbSXPDPCH4M8StvJYKA7RGBzAKNSVcGS4i-IFi8h52cbEuUQRIeEvDC1Xt_fdo8ycQh-Fqk2T_JK8RfHdmbUdmROJxer136IgwR15hqCYaUOd3hqwwQ9fESQmsmcbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=Lo6AKHUP9Fk5clS3OJv7rfYNKvB54WW8jUMgCw6mOEWR93gtkwZoH-K26lV2Y-R4qg-tw9LA0oive37t8nvjQm_XCAL9k_6I_ALK5lyxXFGyLoAaKVK1F5o3b62awdb1gSdF0OokYztiQ3EMXeIIfe4AHUb1fF09Uv4uGUvy0fc2ndPT01cMyYzeEeYJb1vUdMupmXPEC2_NlZ9l71K3McweZbSXPDPCH4M8StvJYKA7RGBzAKNSVcGS4i-IFi8h52cbEuUQRIeEvDC1Xt_fdo8ycQh-Fqk2T_JK8RfHdmbUdmROJxer136IgwR15hqCYaUOd3hqwwQ9fESQmsmcbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرتاب‌های متعدد موشک‌های پدافندی پاتریوت به سمت پهپادهای ایرانی:
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68243" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68242">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=TMRPmpKlyVsYXg-F9UvJ2nAeu9ISU2Ev4nxt0pKftAWGPLuh2e5U2E3MASDMqDzdOVaDfao_CwWHhgDpQy1CLURjBqOFowxit0AJTpooBkoy7ewXoXsWsjhXgkKAmnLaETr4jpx-FQnTMMWE0xNTxG5ycuM5w7noeeutC6iJYXb1pMUBZCFE01SUKcFBSosBysya_uPPOVEVpa-WmaM1xO5sj0sUnxta1KRydC-iBhu9ZeKjojspLdCnwK2PXSsL24zF6jBAhy4nE0S2ceKaWREPKUo5LSMYAAX6ZY0EUovpCS7uDYBiZmTjKW5OfQwH5C0zuz5NRT3egFQ1uCzezw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=TMRPmpKlyVsYXg-F9UvJ2nAeu9ISU2Ev4nxt0pKftAWGPLuh2e5U2E3MASDMqDzdOVaDfao_CwWHhgDpQy1CLURjBqOFowxit0AJTpooBkoy7ewXoXsWsjhXgkKAmnLaETr4jpx-FQnTMMWE0xNTxG5ycuM5w7noeeutC6iJYXb1pMUBZCFE01SUKcFBSosBysya_uPPOVEVpa-WmaM1xO5sj0sUnxta1KRydC-iBhu9ZeKjojspLdCnwK2PXSsL24zF6jBAhy4nE0S2ceKaWREPKUo5LSMYAAX6ZY0EUovpCS7uDYBiZmTjKW5OfQwH5C0zuz5NRT3egFQ1uCzezw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68242" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68241">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5AhL3fFixE9Q3w-4P28_Oo5La_8RHgf2WbRgrMnoGfAzKfHiX4LwC9b0LyMzZ3gm4pkxXB2Mwq5xF-OPCXbc0IUAmm930EFLmu-trBUL5BYg163q724t7kAmzIMueQBKlBSEPUAEiuOtB2cdHrpeOTBUQHp-JSm_4vGvLGvtb3ItIyz6CLGWcgV3W6pn-MzjHzIK3kQZxEL8BnMYgu0AoYngrAYY0YlIsYw-R2Y4i3YvEgOO2b5T05ydEf5Kov7roJVQ29Zo4ZmBs_WRAo5XrTQXOIAnSjssCfcD_gd-6PvQuOfUDed5RcNXH7H7nT3H__UJ_7s2I1Qy0SMBhpGiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68241" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68240">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68240" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68239">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=LhOxDybPoruMwjkZfUTOYG_vhn-sOs4Z5z5URZYYrMrzd30Aoa0jmbAqq_pyd2XlIP3Ls5g7EVIKRC1DiRRjvSoLKgDQQRKXsGCUTrGODMThkLtEc61WdKlPsv99oZPk2px7FKySj95fGJSx3E4WMKno5Cv2VZJusX_WB1LIsDSF3pjHWwQc1U4M7YV1C1DmLSZUVLN8RG2GQAmAzzavMw2Nyqf8LEwi-JbKtryFu-ww0pze4DctnazNKmMGKEjyoeN567sRxnWGi8yetcVpjWQlmkO89k6D-Ac6fOifjli-R_Irsv_wN6inQBmovEFIZGi0DZaJgdsYzD8tyu6DUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=LhOxDybPoruMwjkZfUTOYG_vhn-sOs4Z5z5URZYYrMrzd30Aoa0jmbAqq_pyd2XlIP3Ls5g7EVIKRC1DiRRjvSoLKgDQQRKXsGCUTrGODMThkLtEc61WdKlPsv99oZPk2px7FKySj95fGJSx3E4WMKno5Cv2VZJusX_WB1LIsDSF3pjHWwQc1U4M7YV1C1DmLSZUVLN8RG2GQAmAzzavMw2Nyqf8LEwi-JbKtryFu-ww0pze4DctnazNKmMGKEjyoeN567sRxnWGi8yetcVpjWQlmkO89k6D-Ac6fOifjli-R_Irsv_wN6inQBmovEFIZGi0DZaJgdsYzD8tyu6DUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام تصاویری از اصابت چندین موشک هلفایر به موتورخانه نفتکش M/T Belma که در خلیج فارس در حال حرکت به سمت جزیره خارگ بود را منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68239" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68238">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
بندرعباس بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68238" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68237">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbAHB3MmS-NJN7rIJDxCUGXDHID73YIwMI5c8f0y4U3lpwdKDgf31R7oMHy82VweF0AS4bTKgkPrKYDPvHDM82FF5zWeP0yVCW4U_sG0uOk98wRVqT67WQgzU5yD9-tZIbvhPYpNpv4bpgF8NWOiZ3C528if_EoDEUz2ZeM72hPyw1WNXF9dxjBqhXKzFjpxk5qhYdeptyGUUI-tkeDqeZzzkGr_5ZLwjcEIlFFLZWtvreHV_rv13C2IMW4b2NK5meUn0EOsYPp0516Zhq8AC71-Ef6nm1wSrd7VM2NlG58DIlXZB_dcY8-BGOM0NDzMu3jxRhzrvSB4cNsuKB1JDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68237" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68236">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68236" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68235">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N7Pf6hcg60a87mJkA3gexSrUPN_ZQlRTFg_xkD74_Nzz8UhqTjZuxzRWAjn5VanqAvoJI983baNY_JEW_KCDBQBiHKAaU-xYxveEUmX0_hBgEs9p98tusw7HiUobCvSmxJ-FmhQUx4jmQacz2fjiB5Bj-XipVgR5tufHeV6g-hzcV1waC40w6NszX30z8NATqOcURjPAP2Mni6-NfEaHF8KLk3BEIi12snZJHYxuAok_Z2g7-rZ2VtUzlLOgCz941nMsY-XovDZZbI95fpqIwOh6qmx-1AIIPs_QwHoLvp7bcfysNNIfXbSO7TvOtUXHwI-CHYzU0C-pd7JwaFqk-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68235" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68234">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">من خودم رئالیم ولی برای مسی باید ایستاده دست زد
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68234" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68233">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=hRd0T7btYjimxOpZNx5eDR6KBFvuZI4NZ4Qt227ZS90BAKRMl2NzhSkPTpr90y7LLEKhB_U5AFl7dGNmYOZNu9FMfbvghDMOv7etCfps_pq9XaxocDiK1n-vJ6XDWtuG-9gdpa1P_heIoGu3efmBpar1MPHOI-qeCHNCp3H1-bxiCJMsocw1w7YwWMwphwsZzWqXyrkWUetaZrDgpmYAw8WUfgcCXHhxg2mgbglokqK8Ojaf0hEPROE3Ixpb6doKkKr_wHnTxPCdbhp5nPwoYGOzKFFxovqe1BaZcf-0HcH8KTSS5H9v8BhSriRG_eH2jhCWd3A3xZgbJVf98zcY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=hRd0T7btYjimxOpZNx5eDR6KBFvuZI4NZ4Qt227ZS90BAKRMl2NzhSkPTpr90y7LLEKhB_U5AFl7dGNmYOZNu9FMfbvghDMOv7etCfps_pq9XaxocDiK1n-vJ6XDWtuG-9gdpa1P_heIoGu3efmBpar1MPHOI-qeCHNCp3H1-bxiCJMsocw1w7YwWMwphwsZzWqXyrkWUetaZrDgpmYAw8WUfgcCXHhxg2mgbglokqK8Ojaf0hEPROE3Ixpb6doKkKr_wHnTxPCdbhp5nPwoYGOzKFFxovqe1BaZcf-0HcH8KTSS5H9v8BhSriRG_eH2jhCWd3A3xZgbJVf98zcY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68233" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68232">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گللل دومممم آرژانتین
💢
💢
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68232" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68231">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گگیایایتیلیاایایاااللل دوممممم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68231" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68230">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68230" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68229">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68229" target="_blank">📅 00:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68228">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">درووود بر روح پاک مارادونااااااا درود بر بیبییی</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68228" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68227">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کلم کیریه، کیر تو انگلیس کیر تو کیراستارمر #hjAly‌</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68227" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68226">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379978a151.mp4?token=HUWqAelQ3nltKHBwAFPlUs2ZI_-3Oipb5Ui2MWr5Jy-LQzOALENxi6cLLQkx78yMlctWfSFV5yWS2fo3fsHTTCNsDLoLeFZ1d4ruilILUFEHzYfIZiXwkB_5ilNsUuCq06_EysZ_4ITNgJ-c4bqHj8QyS7mP-5nVk3e_o47C4YhUOkJyKyZ9ie5gutAmsYEdfwHkj1KeGEHs3wz5V_Xn16FmHb3rVvWj3xHr0EKurbgj1g_kvy-7fTz6gz2lCxioOe9btzbudT1fGA9zl-Fdn7y6s_AKuNwyzQ3lulugO-gtEqAoB4HD2uN2GDVsDMSjyBDiAUu-UkVvOnSBegm1AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379978a151.mp4?token=HUWqAelQ3nltKHBwAFPlUs2ZI_-3Oipb5Ui2MWr5Jy-LQzOALENxi6cLLQkx78yMlctWfSFV5yWS2fo3fsHTTCNsDLoLeFZ1d4ruilILUFEHzYfIZiXwkB_5ilNsUuCq06_EysZ_4ITNgJ-c4bqHj8QyS7mP-5nVk3e_o47C4YhUOkJyKyZ9ie5gutAmsYEdfwHkj1KeGEHs3wz5V_Xn16FmHb3rVvWj3xHr0EKurbgj1g_kvy-7fTz6gz2lCxioOe9btzbudT1fGA9zl-Fdn7y6s_AKuNwyzQ3lulugO-gtEqAoB4HD2uN2GDVsDMSjyBDiAUu-UkVvOnSBegm1AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی به زودی شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68226" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68225">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94485380c.mp4?token=t94dVsuHcCp9MIAnd1JrKTdq1txN0XNdnslsMj7YIJ9-vHf8_xYRfWaJy56PY9GJ0cYLxiIXZfmdWxThv7jRrGsRKTlXOIJ6E4Z9m7XpT4Gwp5a41rn1hxMxN31R-T1qhX54r8QWI5wGJSoQ905WkyySCAZUxnXoAoPopkY9u4U9lFCItQETH3jroYx8gv0QPJPZip051lcMBFC4ueEwoxBz1xWTxY0muUl-oZmZ-NUJfGAZCL3QyNSJjMwlIWoO1Ek3rDlLfoMLpE9CwomWx87SVf-9OhiMN5YOFr0EZ9YwJPNSL5oLs0xtXB7O-9zGiLXYmGK8_YetuxZtTcaRCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94485380c.mp4?token=t94dVsuHcCp9MIAnd1JrKTdq1txN0XNdnslsMj7YIJ9-vHf8_xYRfWaJy56PY9GJ0cYLxiIXZfmdWxThv7jRrGsRKTlXOIJ6E4Z9m7XpT4Gwp5a41rn1hxMxN31R-T1qhX54r8QWI5wGJSoQ905WkyySCAZUxnXoAoPopkY9u4U9lFCItQETH3jroYx8gv0QPJPZip051lcMBFC4ueEwoxBz1xWTxY0muUl-oZmZ-NUJfGAZCL3QyNSJjMwlIWoO1Ek3rDlLfoMLpE9CwomWx87SVf-9OhiMN5YOFr0EZ9YwJPNSL5oLs0xtXB7O-9zGiLXYmGK8_YetuxZtTcaRCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به سپاه راسک سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68225" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68224">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به آرژانتین توسط گوردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68224" target="_blank">📅 23:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68223">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
انگلیس اولیو زد به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68223" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68222">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=QjJDMcPp_vlfAhjv2uDKM1SK8zVWH0b93L8bsWhCnNrZevlUNPu_xtTn-XZgptRUGPdWbA4HJkSkml758zOCK6MdYppHnpQDRiBuWHQ45BcCFBog0f3dM04RGmg4OWYqaNejqpysgXIsF-2dbiM9sdOSgARPl3noNo4KfYzah_9DdiNOMEQHIptXeEPNIW-OkNSyIrKhjviSrq6Elmvh1WkWw32eCz9AfWkzhJxstgUrvVBxTZxWeKbTZWU5mRT_m_DfUyYyMHWWb8UbKZD8NcxSMGx8aIP5mElZin2Cb1mA2KGfe93GXXV4VfpJX-RYiwTKl2fAwPc3QX1mNGvMUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=QjJDMcPp_vlfAhjv2uDKM1SK8zVWH0b93L8bsWhCnNrZevlUNPu_xtTn-XZgptRUGPdWbA4HJkSkml758zOCK6MdYppHnpQDRiBuWHQ45BcCFBog0f3dM04RGmg4OWYqaNejqpysgXIsF-2dbiM9sdOSgARPl3noNo4KfYzah_9DdiNOMEQHIptXeEPNIW-OkNSyIrKhjviSrq6Elmvh1WkWw32eCz9AfWkzhJxstgUrvVBxTZxWeKbTZWU5mRT_m_DfUyYyMHWWb8UbKZD8NcxSMGx8aIP5mElZin2Cb1mA2KGfe93GXXV4VfpJX-RYiwTKl2fAwPc3QX1mNGvMUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما به این نتیجه رسیدید که نمی‌توانید با سپاه پاسداران مذاکره کنید، آیا این به این معنی است که ممکن است آنها را مانند داعش از بین ببرید؟
🇺🇸
ترامپ:
بله. همینطور است. درست زمانی که داشتم به اینجا می‌آمدم، تماسی دریافت کردیم و آنها (ایرانی‌ها) می‌خواهند ملاقات کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68222" target="_blank">📅 23:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68221">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48590994cc.mp4?token=D6iuJiKerjKrJK5ks7SvwNFjLU-tV6_PEBp3Au-F3yNajMCc7yLBZ80u3EsRZ-nHurr_TiUWv0Yr6pEo7lWR1TchylKDRCk5KlJwpf6eVAlp_fg82IDbS2UOoC7qX1hvnYX--Lj22jiyZbMPpPFSV7fiQX4ajm_NEH9rIdF0_I-GUFwh5yfHAx4pPBf8SSgNAwmKjzCTrYYXOVmNANjs3upi4Vgc7Jitby6PMo9cGVDwZmozuAksB2ENeBQkMEQYB1NVCQkSFw0et87HrJFtV-SEJYB_CvcmN3SlA0-ca5dNXWWthSoguJ9-YjcIZDihVoPiPL33aVHphOCatSijmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48590994cc.mp4?token=D6iuJiKerjKrJK5ks7SvwNFjLU-tV6_PEBp3Au-F3yNajMCc7yLBZ80u3EsRZ-nHurr_TiUWv0Yr6pEo7lWR1TchylKDRCk5KlJwpf6eVAlp_fg82IDbS2UOoC7qX1hvnYX--Lj22jiyZbMPpPFSV7fiQX4ajm_NEH9rIdF0_I-GUFwh5yfHAx4pPBf8SSgNAwmKjzCTrYYXOVmNANjs3upi4Vgc7Jitby6PMo9cGVDwZmozuAksB2ENeBQkMEQYB1NVCQkSFw0et87HrJFtV-SEJYB_CvcmN3SlA0-ca5dNXWWthSoguJ9-YjcIZDihVoPiPL33aVHphOCatSijmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68221" target="_blank">📅 23:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68220">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">برق بعضی از مناطق اهواز قطع شده، خونه ها دارن می‌لرزن
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68220" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68219">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ
مادرقحبه‌ی هزارپدر
: ایرانیا خیلی دنبال توافقن می‌خوان جلسه بزارن
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68219" target="_blank">📅 23:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68218">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
گزارش ممبرا از اهواز:
اهواز قطع برق منطقه احداثی
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68218" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68217">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68217" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68216">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ead41427.mp4?token=dFY6mfndTbx5TO1Q_bblOVxufZ9MabCFLaLqqk48_dtnLmHu46MGzXEKY4kRburGWf_1BFydoXZdavNhvCo2t4MnhLCJVNSerMeTiT6mMdTgTvTNaEWUt8GTsZqCJRts0NMa155r3yHezTAjHdQ7d6eiGm-umgaiVkZHFJBAfMtGxXVbQlnm_-brhSKQPZDpXULhQwZUhv5vDBrALxhnM5qXsgR1f5KCLoi7IYpQZezDUiYZzZyjrLweXBrBx3ceZKJ4miDo0DQFWqWCmPB9MrW3NJ7BOLfzvTIrzIRWeepRUvMIKI03PwdKd2SF0XRXv0Bbk9-7ThbfMg0BnWnB-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ead41427.mp4?token=dFY6mfndTbx5TO1Q_bblOVxufZ9MabCFLaLqqk48_dtnLmHu46MGzXEKY4kRburGWf_1BFydoXZdavNhvCo2t4MnhLCJVNSerMeTiT6mMdTgTvTNaEWUt8GTsZqCJRts0NMa155r3yHezTAjHdQ7d6eiGm-umgaiVkZHFJBAfMtGxXVbQlnm_-brhSKQPZDpXULhQwZUhv5vDBrALxhnM5qXsgR1f5KCLoi7IYpQZezDUiYZzZyjrLweXBrBx3ceZKJ4miDo0DQFWqWCmPB9MrW3NJ7BOLfzvTIrzIRWeepRUvMIKI03PwdKd2SF0XRXv0Bbk9-7ThbfMg0BnWnB-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اهواز رو وحشتناک دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68216" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68215">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68215" target="_blank">📅 23:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68214">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
اهواز رو دارن میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68214" target="_blank">📅 22:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68213">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
گزارش ممبرا:
مجدد انفجار در اهواز خیلییی شدید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68213" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68212">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eobjG70t1_5scAwkZfegMfcAMOBejai9FtpNiFBdJcRKcwEHD55HiGlXO3ZzIl5vb0crX2NMD9SCnBiv3V36fYj4SG0A9Q6yAZKyzWz-ecI-ihu7p1NibYR69c9EZOkn8mBnWutcm1ZpypAGmJ7V-tf9K8leDAGY1CHD_xgzF4ZOBNxfKMFTrPmxQWjXlGPTZDL9_XSOi6iVtgCm7U7PQUsxt8QPsuaEyo62wNEg2pcz93j-41BGYvWjavLPX64LglJy7cmHYVidbHc6T_zlno9902bLFf4iBi20BwFCaK9qGGhdJ-vRpzli0S6Bc9XW1uUbjy4p8_YOgYdnyfD_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند؛ تنگه‌ای بین‌المللی که برای تجارت جهانی حیاتی است.
ارتش ایالات متحده در پی دستور فرمانده کل قوا، ایران را پاسخگو می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68212" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68211">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68211" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68210">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
گویا انفجار ها خیلییی شدید بوده
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68210" target="_blank">📅 22:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68209">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68209" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68208">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=ukWSQUbaVBqdjnQG7Y7Avtp9UvPM37yI8cyQgiupZl4z3lph_3qSfjtO06iEE3kMrkjFNIVxgL0PUrFMGE1Bg2vNhoqc2jmKGUAPaNxh_SqHEgEMxXTvljMXE6i1rNS38EO9ealHNE2Kuw2RWbd9ehOKvbdQpVmd9ameEHEHUxqrzGkJCGhoOziAgizVsUzkjYso6Dlu5sys3I7Fm8X1Tj98H-S18mwugypb99By6hbo2I1eK1EtF_VbioFAxbE88WEG7cYlvckspEl92rJUE-AnFfP0x_BQUvGXZJOqxc2QNe_A6cUcW2-LacffB2CmXyuiidyl20Lzpc-vjCEnTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=ukWSQUbaVBqdjnQG7Y7Avtp9UvPM37yI8cyQgiupZl4z3lph_3qSfjtO06iEE3kMrkjFNIVxgL0PUrFMGE1Bg2vNhoqc2jmKGUAPaNxh_SqHEgEMxXTvljMXE6i1rNS38EO9ealHNE2Kuw2RWbd9ehOKvbdQpVmd9ameEHEHUxqrzGkJCGhoOziAgizVsUzkjYso6Dlu5sys3I7Fm8X1Tj98H-S18mwugypb99By6hbo2I1eK1EtF_VbioFAxbE88WEG7cYlvckspEl92rJUE-AnFfP0x_BQUvGXZJOqxc2QNe_A6cUcW2-LacffB2CmXyuiidyl20Lzpc-vjCEnTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68208" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68207">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
سه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68207" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68206">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=WYpKqQKI-n3tSarzraHFk6Q6MgpdVRSsHWDTb22ZydCIJ3Yq_Y5GAaYERrga85zA6jz6-twTAnAU90-LpMDvySPFG7_EfzFXlxCw_dzkcnCpkAtyk66wYYbvp2Nm5LTd0-FwqTql2qhPzmRBrcrcXI0VXJFy6TPAkAnanW2wud4PNfa_fjwMd9Lj0Fqf6LoaOac7mebli5HWBxL1-ofIbCfAlDxtNy2uGO6LGejT9DIvY8xFWdC5RE03vg_-88AJqGsauk05lXXEsBxY-1EkTSKHvEkzXeYPX2LaAPzBzOANwW7gIceba-rk3ti4ONGnh8waZc12WItksBfqShID2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=WYpKqQKI-n3tSarzraHFk6Q6MgpdVRSsHWDTb22ZydCIJ3Yq_Y5GAaYERrga85zA6jz6-twTAnAU90-LpMDvySPFG7_EfzFXlxCw_dzkcnCpkAtyk66wYYbvp2Nm5LTd0-FwqTql2qhPzmRBrcrcXI0VXJFy6TPAkAnanW2wud4PNfa_fjwMd9Lj0Fqf6LoaOac7mebli5HWBxL1-ofIbCfAlDxtNy2uGO6LGejT9DIvY8xFWdC5RE03vg_-88AJqGsauk05lXXEsBxY-1EkTSKHvEkzXeYPX2LaAPzBzOANwW7gIceba-rk3ti4ONGnh8waZc12WItksBfqShID2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از کسی که در برنامه زنده می‌خواست شب‌پره بگیره چه انتظاری داشتید آخه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68206" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68205">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
یه هموطن داشت از محل برخورد موشک ها به چابهار فیلمبرداری میکرد که یهو برج مراقبت دریایی رو زدن
‌
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68205" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68204">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqCD07Q0fUgFBkZD76YrrgJvMziDEjQ8cZh3LrDZiJJKpsjvrnRBe5sqy3cLhuItIlJMdLHhMWphXf-iKfagTXNqzHCgIeDbKlpq29o855ly9gaauxhCxPK8oCpvO47QOZvyhJMpCwm9Xbtut49GLh9BHA97o10_buQCz7h-6jNXm_8mRKyJr_jX0fzVYI4wWc11Fh4nklO99O9AT_Wbw3RZb9RrIZnjHcqfAYL1cRRJb0ZeZGKSisrpIcFH141eQhprMOiURhs_pF-V3V7TyZ5r0DyldvkGf1MU-ZPHCVG2dv7Kd4gzovJjjCusP99QfpnN9efbts7mq4-ITzELIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
امور کنسولی وزارت خارجه آمریکا تو ایکس، یه بار دیگه به شهروندانش یادآوری کرد که هشدار سطح 4 برای چند کشور از جمله ایران
🇮🇷
، عراق
🇮🇶
، لبنان
🇱🇧
و یمن
🇾🇪
صادر شده.
+هشدار سطح 4 به این معنیه که آمریکا از شهروندانش میخواد که به دلیل خطرناک بودن اوضاع، به این کشورها اصلا سفر نکنن و یا اگر اونجا هستن فورا ترک کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68204" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68203">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🇺🇸
فاکس نیوز به نقل از ترامپ:
حملات علیه ایران هفته آینده گسترش خواهد یافت، و خاورمیانه خود را برای اتفاقاتی که بعداً رخ خواهد داد، آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68203" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68201">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PzDUfZHo9qKCPB2vPw2a6dSKn24dWrGAm0mws0cr958U7C4PybSyjGu8msa-kzJzBxRI3o0yQPiJY3FXUTSnNNjP9ShJiBkp0oqzc5xiGzqYf70tV4wdh0kSyiHU6VbeeGBcDbjzKsws8d6Vs5OozQUP0yYjs6pBV96cv6VvXGCfPlY7WAkw_yVwsiGDXrUzB0ngeO7EbZvhKZ1VXHXNzl5qXmuoq50Jtd00EEhIuZC2p6v4NpKGjSmscapL7MABqa4KDTPXqpn4ImCMvf6m5swoFpSWV7QnOluO6JdZwEbB98BhsIrDSCIYcnNcHJo4TCo51anThCWnFxRKKhpiLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i07Jy3zJRZcS8YICPK36NdbOY6HqGx8OzH3dJs6abLitY0YvCepYfAEpaGlsYtyE5xyR00Vmtd87Xhpaq5Bn3D0fY2mPFExuTry07Cif68tHWkGLrzOMo-na8JSYXG32ZgZwuLNJ0IHH_EmgbSdNPzobPd1hPTil68TcgG3PCdzH2xG8EiCOWtElWio174Fn4-cBUt2PSIUKzb05IwOksUxXH-7LE4yrx2HIuAadV1hEP9Z4B00KsaLzoAj3Ql48e6lVHTkgqev93LA8Ct86jZPF8h9_agwIu8owrNzvdDmwGUrdf-f7BCg-DXcJkLT4Uj7Y-9lUlrcrwyaqNls75w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ترکیب انگلیس و آرژانتین برای بازی امشب
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68201" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68200">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
قالیباف:
همزمان با درگیری‌ها، باید از ابزارهای دیپلماسی و مذاکره نیز استفاده کنیم، به گونه‌ای که منافع ملی را تأمین و تقویت کند.
همانطور که بارها تاکید کرده‌ام، مذاکره در این مرحله به معنای تسلیم یا ارائه امتیازات نیست، بلکه در کنار جنگ، بخشی از استراتژی مقاومت و حفظ منافع ملی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68200" target="_blank">📅 21:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68199">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
قالیباف:
برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68199" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68198">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
محمدباقر قالیباف:
تفاهم‌نامه وقتی معنا دارد که مفادش معتبر و در حال اجرا باشد. اگر ایران از آن سودی نبرد، دلیلی برای پایبندی وجود ندارد. ما بر اساس اصل «چشم در برابر چشم» عمل می‌کنیم و در برابر بدعهدی، متقابلاً واکنش نشان می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68198" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68197">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.  @News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68197" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68196">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT8c2iqvJeAUbcGN3Wr052CzKeUQcBTJtDCcW1HGPg1TIak7j9_r9MCqPkYUF-QHU1deB-vlfOhOjQsAFVgOANgpgTQAs-9cmt1hdNoShcgVtaS3QD9-2OX7FHPpQ6MRW37aUHGX3VQSkD0SFutjfUz7RK0nu9lS3bJuJOdjBDZBa_L0KYczQulN6gZ1Z_jELKSmHZFWo9fMJ1fbAM6aQeir0VHuMFNi8Uz8qZeThwxjGuU3CLEjbdAuy7qjWWXXqdlx8ilSNYVO1sSMznufBGN5gU17f_VycXC7YoCINbdaACKmt_M-hYpjlK9GcEM3sh0jBA0_AUDpz0CxWnJ0yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر شهدای حمله آمریکا به پادگان ارتش در ‎بمپور.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68196" target="_blank">📅 20:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68195">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9KIF13hvNR0clOOv4VySM0I_xihK77gBJt6hioJvCFTug9khu1CDdow3iaiwi4BWUcd-av6Kv2CX28Zlkzptf-bo_Hcqoh1IYO0fr90MfpvMaf2shN1-Wgij4eDU6ps4lwhpcUF-SKDcDyqr6m4NEtEweDCv_u0R_M9SGDCZrYHHMf1YzWS0SwrWr6hx53C5YDKPj-vXZLvKxNRa1HUkxsGLTqRAfUYc_tSbbBD_5XKB994ywcrxAnKFVTHiYO5fV_T_V0jFClmdrqb76tCjXxucS7f1B9IcCr5Qg-BxoPJnts_ZYmtUlrWWGrrNHCRE9NxY4Bhr7XRl9NMEXOOTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب عادل دو تا اسطوره‌ی تکرار نشدنی رو آورده، فوتبال ۳۶۰ رو از دست ندین،
کص‌خار میثاقی
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68195" target="_blank">📅 20:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68193">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMreza</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kD8tEsRSLi29zp9R6fckQ6pX7ymtdESLbQNbc-fjmcxKvlTWah-35y3Xq7bWz3KkJ1SqZTtitDBrYzM77YdyTtsrfgUx_9k7-sBPGSTpJNrDgIQZxEAViTYwY75edyIn_v93xcxlxcN-2rxdx8KcQHeOg5ONbqZ7dyIhJzE-tYo_fmq-yo76lCdGg9nG0aKBW5SQEQI_qD8x98X74fHOA92c-ucglO67e0NLIF5KXt_LFIP6cF8p5_4vs-0xAfsQdpi-nOUiOfadOmpBQL61J9XwLdqiESVdb1tTJoB7p3DyPo3hi0fw6oFTZPq0O5omCzdtFyRGQoKWnSaR29IN_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hVAP5klg-WWVvCoqT4pawHSaYNhqZUdmragF_qu_e2KIrfYpm7sJdUVQxsd82IMWTYrQ44mTlppNV0trC4Z3KTetpXSadjTTEF_0Xd9wtYEe-iVZjJi85qiOD7ZqMzpVcMRtwea-MEv-94zqEhUPlScxQIk37t9F1StHRpZ4r__Y8B2KWimk6yG7AYyB52t6IFjcpYU0RBWiz2T9z1WJHzklsbyszFQyRr72ziIMaaDcJcDlMg4Yo20qz4fp5Jirk-cSncBLdsh6SbVKTNS1-RtAeSo2bIORqfQF4_LTq25RtSAcLsT9qHgRhoT2Nd44Zzhrje0X8KZSOxvZzWCt2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Siuuuuuuu
❌
Zhiuuuuuu
✅</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68193" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68192">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=QSZYo7OT4OrP_0Igvk30CE2wkMnvfjyfuIgNvpWYzoXiz2snBFg-pI9FOA0JJY-MS2C9GY85E8B5_Bouj-f1nkX5EPuQQDdfioukVjsqyKzoEFUNvvzlQTY5s3L3rcRXxn7vvjCSkXhIvO5CSgI7XpipHi112_35inpn9d8978rffQS6wmCYQ8cNjhuD5VzIPnTl3XiuifRBFonf9Hv9pNlgLwHej2tZ0H3ZExUFpwQtnkkK8PVRKindP5ajG4e3dQZIsboNUWbdua5Q8aGDo5BjwTWg3TrEAZ-LBaClbgeoqmwFdp8fK-1EiP5vlUSonNbR9uSmvI7RMaVGxTB0rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e6c5a6cd.mp4?token=QSZYo7OT4OrP_0Igvk30CE2wkMnvfjyfuIgNvpWYzoXiz2snBFg-pI9FOA0JJY-MS2C9GY85E8B5_Bouj-f1nkX5EPuQQDdfioukVjsqyKzoEFUNvvzlQTY5s3L3rcRXxn7vvjCSkXhIvO5CSgI7XpipHi112_35inpn9d8978rffQS6wmCYQ8cNjhuD5VzIPnTl3XiuifRBFonf9Hv9pNlgLwHej2tZ0H3ZExUFpwQtnkkK8PVRKindP5ajG4e3dQZIsboNUWbdua5Q8aGDo5BjwTWg3TrEAZ-LBaClbgeoqmwFdp8fK-1EiP5vlUSonNbR9uSmvI7RMaVGxTB0rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا صبح می‌شه به کریستیانو خامنه‌ای خندید ولی کانال زشت می‌شه پس بسه، فک می‌کنه کریس آمریکاییه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68192" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68191">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_N9EfIxwf3iGGi_W4uXEDNACCDkbZyCYYQ3g4kMyeZy4olOvNC75Nm_Hrz69MKw_ZqZzE_4ZGyKQkrUajal14Vy6LjH9JlZQzsr-YxwM8sOS-7n69Ai1_5d0JQZYSZ_kqDugALAx91sA4C9DcMU4Zr3M_eyMQ9K2LYyHxu6kLLEKdYFXwlWgG4n7JBOgZCObJdRvrQuc2OIYwmOw4zUbpDZZv0RDMpjMzTKXwvXCFUowCuvBUnbdX8TP6HyfITvRfrK01VPGn2yeIJ2TZJXDvMUGqHbk9sqBt3LFCzg5HgqGGJ-nyl9AU-JLURXWd2vU93AXmMnHLgq-l7ThdeRFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو خامنه‌ای کرایه اسنپ نداشت بره سازمان؟
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68191" target="_blank">📅 20:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68190">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرونالدو</strong></div>
<div class="tg-text">اخه من چکارم؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68190" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68189">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6LlpHhHbIsKR_TZ7UQ0HvTfpWo6ARMMej7XoFqbWiSNhlvbvY24V9-n3zJk2k13t3sGsHt2b08aQJHrE7wdDZWpfu8_gCgeLjtmvf82cI6n8SWAE1oGiSNyx2u5wRvLEH607WxOqxO5eC-t_v90PXpDd1CVwUnetvm5bKI0dGNYZ-5GB0hoXcVDdhAayWt7YrIZlA57kNLjQnvlovqao--zqgZALC1EypdT8zmf1UK6zOdR_Ww1orZ7p4NbyIxwKwnh731M2c1aTO_o8s4obYz1Y-G1da27j7nOQLtJfV3yLOIhFHlCnZAsg31R0AkYKZBBMa9edF8HCb225XbxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:  #hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68189" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68188">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=JgeAkIMU13BGBCnrogZZRT9ibgImBT2JbtleBEP15MAlsN4zNrhn2_VnDqIlSuMFGtubO6Id_aNJaPPsUeUg0VEQo5yFyY7dji8qi16Fsyon1dMsp0XvcT8XZna5vVuLzdiZ3mwv7wq9Xj0ETY435E3KgBwVM8RGYY7Bwrx3lfLbHDp8HsVZbyoGJV23Hnds_L_79Xwb7FP7By8pQU25KyRzcx3Xr_XbYDDAiQp0e1K90Vp-v6boX9QuxzhOv2OUOgzUJ0o10NyBUDL_mHto2Y7RzfKreQw3tVlJcjegiZNCoH6hQzotjHok7VHfnt1A-ccjLoU2JwpQdGmDnjFZxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=JgeAkIMU13BGBCnrogZZRT9ibgImBT2JbtleBEP15MAlsN4zNrhn2_VnDqIlSuMFGtubO6Id_aNJaPPsUeUg0VEQo5yFyY7dji8qi16Fsyon1dMsp0XvcT8XZna5vVuLzdiZ3mwv7wq9Xj0ETY435E3KgBwVM8RGYY7Bwrx3lfLbHDp8HsVZbyoGJV23Hnds_L_79Xwb7FP7By8pQU25KyRzcx3Xr_XbYDDAiQp0e1K90Vp-v6boX9QuxzhOv2OUOgzUJ0o10NyBUDL_mHto2Y7RzfKreQw3tVlJcjegiZNCoH6hQzotjHok7VHfnt1A-ccjLoU2JwpQdGmDnjFZxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یاد سربازان تیپ ۳۸۸ بمپور
💔
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68188" target="_blank">📅 19:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68187">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پاساز علاءالدین خبری نیست، ویدیو های منتشر شده مربوط به‌ گذشته‌ست
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68187" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68186">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX3c3mbehU32q51pJHyt3dvLXP-lNGL0bAemTA1CmjCQ7sBUi8NvtwgEebzE-TTFzwOQiIxAnmFcRLwx4TUB7Yvyxl1uXTQ6qhKmnlClIebuYT_dEXv87UmnmZ3gd2cwL50u8kkxhc-ZdrjmDQ8absbuByYxPleNZw0OtgE9wpgsQLYcsXHnPdHW_yrYpAuAyuCoqERPENO0Lf6PsTOLjuR8hwpYk6nIU_GLDCuO5qYEf6XY34sN43ykA-GnE8Op26gFI4nXC2aZPtnGKTRVc88TbydO88dNM5iW4x6SjLJL3XWoQ1EY8ofEMC4Mf7AUMzTe7jdKsxWSZcSuokAEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:
❌
ادعا: رسانه‌های دولتی ایران مدعی هستند که نیروهای آمریکایی در تاریخ ۱۴ ژوئیه به یک انبار غیرنظامی گندم در هویزه حمله کرده‌اند. این ادعا نادرست است.
✔️
واقعیت: در تاریخ ۱۴ ژوئیه، نیروهای آمریکایی اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. در همین حال، ایران غیرنظامیان بی‌گناهی را که از این تنگه عبور می‌کنند و همچنین در کشورهای همسایه حوزه خلیج [فارس] حضور دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68186" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68185">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-t29xzPH1g9zodeLcrK6GbwN0j-0-CDmZbAAb_nCk_d6oROv3WDxqlVhXtEpgEKCRfhDb7mY5yVPHv-U8QNi9T4ST9MhihCVwIg88seJTsAzQGiwk3ACNVvsEhHin8FLMplYGutLSw5hsvJE4Sx2DFXeZFxXTyEByWBiF0ax-xmyXDrA9JgzfiR3u_NTB_9kp7uQsINqFWzfSD728PSMoT6PtS5JI9Tr1CxwjoyvuNnUuR_UWa-7P5XOzAzNa_rlo8j_LdIoECm7c_NXNmih_Ib5fdfKMhqhSAUMaFirGi5GwqgkWuNFstrWRei65giWN23yVIM5dkmDPSGbl2oeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68185" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68184">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-wSaNy6tZfFxcYCmKg54_jz2BUfBp4eN7HgR0sXOtD0vsNfE4Y4HLxqyQoKu4UUUnfUl82xOh7q2iopR01WEKDb3nF-Nh1FDWOYthnM32Z8B5WdPZfi3HsadwwjnSUJhEZCb6k8Iezhj62kEdeVigS4KKPcU4QS7aogO7cp6RP0Qs9tRGXVINx3QGDFpXUs_3Dp97vOVBQ6sOXKfP7mRBWRgf3x_a1s3STV1Tn-m4aVwcaNgdW7e9QTL2TBt7nTJ-IjxCUBwgITRYtbWmw32IxmqUY06uMKgVjV7ylxbCGNtrHGMbjaN-apM-6zPFuBMOq9m5ihmWWPk700NXJziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره دریایی بنادر ایران در ۱۷ ساعت گذشته، نیروهای آمریکایی مسیر دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند. ارتش ایالات متحده همچنان هوشیار و آماده است تا از رعایت کامل مقررات اطمینان حاصل کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68184" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68183">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/68183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68183" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68182">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc2XfnNfJSvGXe1cIjgyyNqmjdqcJFYVPZaKtd2N0Frw7LHG1z85iCGTK6ZceMEYD_unxftI0UETrwP_peRUwvHjOd1SgLvftVyh7V-fzi2rHTb2yGwRQYrTgtaItjex61PvcPUw1WRdc57xq-hUMrOg-HpV9EuJLudGRNT9A3_FzX0FmfK3mo6sAYMeII12OIGeBNdBzTOrX2NL8ls8UYk8E5deqCDhk-fzLGOYA52yREoPhx4M2jLotLTwnJ8W6Udlkc0Hy8hmRCOHk1LSGaQG4g59qjkzX8e1a0tXbX-RHj8BnfUCkYiyVYv3K_pcwDMOUre2L6y7tgpcv6pT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
Stand for Victory |
مجموع کل جایزه  250,000€
🎁
جوایز برتر:
🥈
جای دوم — 33,000€
🥉
جای سوم — 20,000€
4️⃣
جای چهارم — 10,500€
5️⃣
جای پنجم — 8,000€
🏅
جایگاه 6 تا 10 — 4,000€ هر نفر
🎖
تا جایگاه 450 جایزه دریافت می‌کنند
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68182" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68181">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
انفجار در جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68181" target="_blank">📅 18:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68180">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=XQZBPW6ydCe_T9cG6PuucnREnrebG2inlcv12cisupK2f4LyY1SvPCC5AVn5L9_wkfpmfsdQMauNV9xXZiGFReHrqe5aKDdoPbyHhpJ6SLM6m-IiGeCgB1KbsQQEqwbt-BahS_hH1XcOY3wovT-zl3oy8YRYWKbeJqlOCpdF8vDNW3KI2VNASCdNac5YwaUhOAk6TVt1qm6fDrOHcbonYN4u03POw9GVT017oqqEGhvWAce3f85NNHySliWX-FaK94GstQo-TfIg7GzP2EZ7_tHo7oHUsshYhJK4xKiwiypYaBRKE97oqUV2oNeN7ue0OQggku2_kR7jBjiyxKVGJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=XQZBPW6ydCe_T9cG6PuucnREnrebG2inlcv12cisupK2f4LyY1SvPCC5AVn5L9_wkfpmfsdQMauNV9xXZiGFReHrqe5aKDdoPbyHhpJ6SLM6m-IiGeCgB1KbsQQEqwbt-BahS_hH1XcOY3wovT-zl3oy8YRYWKbeJqlOCpdF8vDNW3KI2VNASCdNac5YwaUhOAk6TVt1qm6fDrOHcbonYN4u03POw9GVT017oqqEGhvWAce3f85NNHySliWX-FaK94GstQo-TfIg7GzP2EZ7_tHo7oHUsshYhJK4xKiwiypYaBRKE97oqUV2oNeN7ue0OQggku2_kR7jBjiyxKVGJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
منوچهر متکی وزیر خارجه اسبق جمهوری اسلامی کاملا جدی اومده گفته:
باید به پایگاه های آمریکا در منطقه حمله زمینی کنیم و صدتا اسیر بگیریم ازشون و بیاریم ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68180" target="_blank">📅 18:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68179">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=LqGU91Nl5X8WorNbpMeU9nWAOAt8Wn0kAukx9HLXeXUM2fTiEdAcP8oiutDKWfSMsX-5jWHQF6_UgLFbOHvwUOr3bFmkYF6AsLAhwMrtvbCTGGnWd8kPWlKyW8U_2Msyqc8HelnPZuASI3q4uwyDOvgJrTJP1N9IHxMT2u3hk36c5OXgUlSbkpQ4pRw1pxEWPBqfPatPeGYocee28dRvbJ8o-OuWW6Xeh5ru5nkvuQg5w8grpqgrEJ_BoyFfQVfossYKrsQgvnJHwPY7hRwD1Cfka0rBspWrrX0rfydy4r-pNNC5Oilb5LLYRYOPSxADRqMYm37yHpZC1q1PhJq6kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1331c1b8f5.mp4?token=LqGU91Nl5X8WorNbpMeU9nWAOAt8Wn0kAukx9HLXeXUM2fTiEdAcP8oiutDKWfSMsX-5jWHQF6_UgLFbOHvwUOr3bFmkYF6AsLAhwMrtvbCTGGnWd8kPWlKyW8U_2Msyqc8HelnPZuASI3q4uwyDOvgJrTJP1N9IHxMT2u3hk36c5OXgUlSbkpQ4pRw1pxEWPBqfPatPeGYocee28dRvbJ8o-OuWW6Xeh5ru5nkvuQg5w8grpqgrEJ_BoyFfQVfossYKrsQgvnJHwPY7hRwD1Cfka0rBspWrrX0rfydy4r-pNNC5Oilb5LLYRYOPSxADRqMYm37yHpZC1q1PhJq6kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمسخر لهستان و شوروی توسط چپ‌کش اعظم رونالد ریگان فقید:
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68179" target="_blank">📅 17:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68178">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=e71-4ZHS215UrhHlYS-0ty1okySv6jkURP3NMS2Lf4D9oFeU-g3Zjl1SpTqHFCkrXsR2Lm9TmjDGfomMIOJJSCNdM1lSTwdKEbxVIn3F75w1CLzEACGNggmXvVSsUOvtGdRGn-s7BD3CMV8wVcwyY1bnjji7U_kHPW_hK9iMhV97L8JasEjpvBQfvnM3fWyVTBuZebWsGS-2xxwn_2S7DtfUkSbXGwpNXlx9Ej0e_sVQyNsPNXA-7YxDMokxUKxQeIv0xV6Gh_UaWKjEjsD9NBooPmq-pCdCqR0b61NpSOwWEzGjXZ26f2woJMSr0S5CEaNKVlfhBFJw-a6dRcCmKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=e71-4ZHS215UrhHlYS-0ty1okySv6jkURP3NMS2Lf4D9oFeU-g3Zjl1SpTqHFCkrXsR2Lm9TmjDGfomMIOJJSCNdM1lSTwdKEbxVIn3F75w1CLzEACGNggmXvVSsUOvtGdRGn-s7BD3CMV8wVcwyY1bnjji7U_kHPW_hK9iMhV97L8JasEjpvBQfvnM3fWyVTBuZebWsGS-2xxwn_2S7DtfUkSbXGwpNXlx9Ej0e_sVQyNsPNXA-7YxDMokxUKxQeIv0xV6Gh_UaWKjEjsD9NBooPmq-pCdCqR0b61NpSOwWEzGjXZ26f2woJMSr0S5CEaNKVlfhBFJw-a6dRcCmKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از وایرال‌ترین ویدیو ها در 24ساعت اخیر در توییتر فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68178" target="_blank">📅 17:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68174">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IU_0mhZko2xl5jiy6P6DWSRonKECm0_lwNCRY-W6n4ukFfaXYPwnUhAnk6z5oAZ6-_WSG2fliKO_QpcKEgPqdeZhcqKEMeCUS_fWw_DV-VeCZ18wGgYqFZ7pLzL0YI1i33LgNuzwAy-U7US7NEqy2_Pk09Wnl7PvOko4z-R2erW9PpDM1U3mVF-TOqA466WyaGBokUOc1ursWFAiezrVAneFGnJf5fiGIbZzXw0xjqHVYpEX5Co1lyvKz7s_2WTvx0uXgRB0cx5lBGbi_8KF6jT3EZK0gXIznxmEYrpQ2QYPAOrfn_ptsY2guALt9s3kpYiefPw4XdzMCf6_m7iJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=isYPweD0sPHneCyNXvxniJrwqYde-tx6NAMEkKXX-FHCVlRd1IdPMkffKDDswwwb9_y5oQhxCI-WiqZC_1zxHWVEQEdSmW8gXfYgT7YlM9JcO1BzzX0V3zkFh4mqWl9ozO6CMhDRhp9BLN-A7TAuvFjXFjvTcUJvSC48krjeNJjECXXs7_Iq4A3Na5_4HHpbVYr-YrqJo6NMS-7DcLyziZ4UsukN-TRGEeph117uz6_h_SAA1lsmwlIH9pY4zj6jpOwJY-qQPSKBt1hjAFJrLm9JDWsT83Kjtzx3fTOdEuqfrxI9gcKjjhGJMVEJzieWe7_Fp4te23dPBL0ryhp45A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=isYPweD0sPHneCyNXvxniJrwqYde-tx6NAMEkKXX-FHCVlRd1IdPMkffKDDswwwb9_y5oQhxCI-WiqZC_1zxHWVEQEdSmW8gXfYgT7YlM9JcO1BzzX0V3zkFh4mqWl9ozO6CMhDRhp9BLN-A7TAuvFjXFjvTcUJvSC48krjeNJjECXXs7_Iq4A3Na5_4HHpbVYr-YrqJo6NMS-7DcLyziZ4UsukN-TRGEeph117uz6_h_SAA1lsmwlIH9pY4zj6jpOwJY-qQPSKBt1hjAFJrLm9JDWsT83Kjtzx3fTOdEuqfrxI9gcKjjhGJMVEJzieWe7_Fp4te23dPBL0ryhp45A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی منتشر شده از انفجار در چابهار صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68174" target="_blank">📅 16:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68173">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=b2bJDyzT-F9mU1GyUansvDo9Q8L03N4zw14UqV2H7RqoAAqTQacjH3EoowAzrDL1_a-kDozrYf10pMj9wwPWkJ06ZOn9bOEkuyk_8TQvKmw2qAJkbMznasVCNKjiRuw0IEqqyCwZWszzEOtc-bYWA4_5e0s3CaBRhUuQvFZiVLtRdH-ofE9AVPNY2SCVkUS7pTfXA3L0h2UXeWvZbOLOQQFQ-BAa34l7PnV-ewwWiNUm-n2HevFxm3tbCtCaRmMq9qs0zLemKuXWASK6IpqxrqjJt9Ya1LwbSikQjHQNtlgz2rGgI7_XfiGGCRTdx4pPa5-_ILHjtv9i935cWUqX-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=b2bJDyzT-F9mU1GyUansvDo9Q8L03N4zw14UqV2H7RqoAAqTQacjH3EoowAzrDL1_a-kDozrYf10pMj9wwPWkJ06ZOn9bOEkuyk_8TQvKmw2qAJkbMznasVCNKjiRuw0IEqqyCwZWszzEOtc-bYWA4_5e0s3CaBRhUuQvFZiVLtRdH-ofE9AVPNY2SCVkUS7pTfXA3L0h2UXeWvZbOLOQQFQ-BAa34l7PnV-ewwWiNUm-n2HevFxm3tbCtCaRmMq9qs0zLemKuXWASK6IpqxrqjJt9Ya1LwbSikQjHQNtlgz2rGgI7_XfiGGCRTdx4pPa5-_ILHjtv9i935cWUqX-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۷:۳۰ صبح به وقت شرقی روز ۱۵ ژوئیه، دور دیگری از حملات علیه ایران را به انجام رساند.
سنتکام در جریان این موج عملیاتی ۹۰ دقیقه‌ای، با استفاده از مهمات دقیق‌زن، سامانه‌های پدافند ساحلی و همچنین محل‌های نگهداری و سکوهای پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68173" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68172">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=qRRXGcwoFh3TeZbht9-sWuyCMYxanM7VPrWiosSaBiwAgn0p-1VyTuWZGC231eRqxcTVPjTQrQUuL12tGp2d3rt3BFslPqTHAKyqr6DbqJibSzIRFI4Meq896lnzjg3LrOE5H1KBvA4pId5wkPxuIcOU8mjYva1_1C0ihloM0LVqIB-xeVwpjVDZqPzwMblrq20pJP2tWPdtj--X85A8twqnkdI55PXq82Wi8qJCf3S2PeKOpWhPfHZocCIkhnrmuUV9qlINK0XHaq1z-jkxe8tYGf_ThOtgGgAQJ5nzl9kUI6fBAdnI6mQxFoCNsowQkMg0Bedc2njVYVhew2nDug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=qRRXGcwoFh3TeZbht9-sWuyCMYxanM7VPrWiosSaBiwAgn0p-1VyTuWZGC231eRqxcTVPjTQrQUuL12tGp2d3rt3BFslPqTHAKyqr6DbqJibSzIRFI4Meq896lnzjg3LrOE5H1KBvA4pId5wkPxuIcOU8mjYva1_1C0ihloM0LVqIB-xeVwpjVDZqPzwMblrq20pJP2tWPdtj--X85A8twqnkdI55PXq82Wi8qJCf3S2PeKOpWhPfHZocCIkhnrmuUV9qlINK0XHaq1z-jkxe8tYGf_ThOtgGgAQJ5nzl9kUI6fBAdnI6mQxFoCNsowQkMg0Bedc2njVYVhew2nDug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جنایت ۱۸ و ۱۹ دی ماه؛
تا مدرسه میناب و پادگان بمپور؛
نام‌ها عوض می‌شوند
اما قاتل یکی‌ست:
جمهوری اسلامی؛
حکومتی که برای ماندن؛
ایران را می‌سوزاند
و جوانانش را قربانی می‌کند.
#hjAly‌
@News_Hut
|
@HutNewsPlus</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68172" target="_blank">📅 15:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68171">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGfAdksSN5hNITjiR0Fx3SnRuX6-bxzMjLrvx1_PzoS60qaF1rDwajDHAPHITi3UqZG0sPOycerT-N_EsbDzzfT6fKZHqONeMvBE01_zvAJxE3Y1i7XFBegl6qW6qs7kHFXAEs_oXhafqowzUrvkUH6Vr4XJOK2er167Z3ZyKMUpa9bwmPPoQgH5J5qP7fJsoiJUz42UvDFyUqXp3bLrm9aJaba8xJ56Fa49Rj4I3YcJEBnreZJL8zPb8MYGvoO-FRkn0H6YIybeoDIfg70itWJdftAuZkPn6PBV3oWIiAA_WWy_gwtjJbs_vOnub5q6zpkut0jTYr0Z_1tcyWrKMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری حامد‌لک:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68171" target="_blank">📅 15:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68170">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7nsUrD0NSwQFnk1om9O-n-ZPKb_j8ttpO_52BJduc-iB9X8Myu3lPrBTqyFJe6myNjhVFHW60hZqAObeWhRLeby32V_F92Cgj9OGyayIBJv8w49_afDBvchXXiea9TiqiQci9QNQuJvdv_RLzHDEDcLjIPa0doXoTYz30mM_Id2eAJG16sd1jd3kHqWL2V8pZ-xszvs71FUm57EdZvuuCdXL2KkLPpJiw0po3GvFlqamMJ9aTnP-NEueOwWLox6vxmmygZgLYHG7tmGsnhjKDPzrY8hDFSncu6VrjBFN71tB9O8KPk3HCIEvR3NjniNamrHaPjL2xpO5DYOH04T8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
چهارشنبه ۲۴ تیر ۱۴۰۵ جام جهانی ۲۰۲۶ مرحله نیمه‌نهایی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- انگلیس - آرژانتین
🇦🇷
ساعت ۲۲:۳۰
ورزشگاه؛ مرسدس بنز آتلانتا
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68170" target="_blank">📅 14:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68169">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
پنج انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68169" target="_blank">📅 14:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68168">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">علاوه بر اینکه سوالات یکیه و باید همزمان امتحات گرفته شه، تسنیم اومده گفته فقط نهایی دوازدهمیا تو روز ۲۵ و ۲۷ لغو شده، این درحالیه که دوازدهمیا اصلا ۲۷‌ام امتحان ندارند و یازدهمیا دارن!  باید منتظر واکنش رسمی اموزش و پرورش باشید @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68168" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68167">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le7c4CIWlACBUSvCldDSdVDJtmkRj8MmHOjCaQfh2opQbLzUbA6sUfSnlAndxhZco1FCniqSHpbeZnTVuMIIZKs0Q8WJkI6jrA8B6CO298_fu1C4YdL0cMvb7UO_cxRecbEvZ3mVqZ9_wIa2Nmy9J3vD3oF4Jk_WKJgGv6sp5KsDxThVfW0k6733CifGR0McIFFsIxnFcP5OpcwkMjSwfQFd4UaNRG_DZtBVt4asLQ5PMwDMgiciv6u1DWi6fceFdfpmX9zpbTvRM5BN_GkfPipt9NIz0FBCIorU1JbWXytWHioPehNU6ynwD8PZT8f_zkT6j5HP9PVQLvcBfOwaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری نهایی رو فقط برا چند منطقه لغو کردین، کاش این دو روز کل ایران رو لغو می‌کردین تا فاجعه‌ای دوباره مثل میناب رخ نده... #hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68167" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68166">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=Hv0h7WPJuKlz806NAAkaLaU_X6Q8pDSvbtCb8yPe3WuuRJI2Bf8I8GXGflkmqX0RnscJD-3aLS2V1amd6D6LekhkrSQNmbQQW5Kk7H_Fiw90pWAJbQfQveCOeZWGTTnfUnjUl8M4zOC-geXOmUfwW3S52HqsnNM6p_ilVwqm5wPHfRI08ioQUTiz-thSdlidqXaXGTE4hkXjUyQZ9CMBbd2CechIpF1o1Lz_BPODRY443zZlHBpa8ky-nSQWf7sbeG_9pEIjrV55zYcBMqYBM0trLX6V51JlRFIMT1RB7eoog30vFSUcF1GXmh0eqsMTfV65uiRX4WZQvSyQQIuF8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=Hv0h7WPJuKlz806NAAkaLaU_X6Q8pDSvbtCb8yPe3WuuRJI2Bf8I8GXGflkmqX0RnscJD-3aLS2V1amd6D6LekhkrSQNmbQQW5Kk7H_Fiw90pWAJbQfQveCOeZWGTTnfUnjUl8M4zOC-geXOmUfwW3S52HqsnNM6p_ilVwqm5wPHfRI08ioQUTiz-thSdlidqXaXGTE4hkXjUyQZ9CMBbd2CechIpF1o1Lz_BPODRY443zZlHBpa8ky-nSQWf7sbeG_9pEIjrV55zYcBMqYBM0trLX6V51JlRFIMT1RB7eoog30vFSUcF1GXmh0eqsMTfV65uiRX4WZQvSyQQIuF8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خسارت وارد شده به یک دکل مخابراتی در بندرعباس پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68166" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68165">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
#فوری؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.  وزارت آموزش و پرورش:  بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68165" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68164">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
#فوری
؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه 25 تیر و شنبه 27 تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68164" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68163">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5fujX_sJkCny2Zn6TCHDxWcj730MyB84GP4PBWotKzVTFmf9WIZHLSm6hrETYsiqajh7z5UiB0rgmpwSnYkvACaSEkji-A7WxJxfyPbzIcnjdtBW6u87EkQ2EL1u14-wpud0WCddsFUjWswp4hJ15_fzkwXwP0kR461TpfW_DYYxTNChPINbS2Jw3abDyu3uOGtkvYgSJX1s2aijbkQ-IePgGfQAldYbdj6EoYbR8ZxxRdRgh6p4jJqUOFLSsuodZ-EakR-KWW7ov_nNQ1bf_kkeKNzYC7VvNZoDmB0U1gk6CpS5TAhGKC7LmyRzY42qFDgHfUHRwIofXxLZQM0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ صبح به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) موجی از حملات را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانمندی‌های نظامی‌ای است که نیروهای ایرانی برای حمله به کشتی‌های تجاری در تنگه هرمز به کار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68163" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68160">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlMuzvueQxg4lVGJG1_TUzVjxvty6SYe-zQUv-wI1L1-bWieYc76h54BwLLjsn5wVYRuY8OnYl7FRnPo2dVX9HBDzMgLDXAGryVoqO_B5c7pYlGk8NYyvnvhmDfWYfutLeWejRewMvnRKqnT1U23CiKZD9JVYvICZzKJKuXf4aynYxfohK9zQAbyWUY-ck3v_hInV29s1fS1fam-L4LnNuEKDFqun5EwyPlAcPVmgIO24kO4hAUE-fnKx1zc_PstABOlptXoRmQPUgc4WYZznpEzHgnM9hUo3BXIb4ja4KpNw6MT1iVM-pDNebWrUqTe03LtUps7eS3oCZogPs-Mog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJ3y0lzulTWcrWybHIIJkI-bkKQ0A-uv35f2MB_wpGYbbjzdrOFsNVII4kMmgdCoY8mV1qkk1EeBxCFERAy5nqGw5e_tT3F1y76xQ5VE0Tm40bQSdvmCp2-Go6wBOfTQ1m5SZf7-IyAdrcMsiO6ZHgw2-0gq8xbOunmUNUMNxZTv9N9BbapBornxRoKtCHrxO0wYn_QoahIQtL9YAAjcxSDMojA7dFTTyp7pOBvt05yyJGJfead5ufD-sqIFEIle4A_2iyEF2uPJevKnEFpLJG1PEtj0oNdUm35XQOJT9f3dss3ElzDBRMjkBGDaEEAhO8E5HSRBkGyDe1GLSV7mcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=F22QItM-hzKyKinD9NKAF2VD2DSDVO8TW4Ow5_alQvTAfuA_xjNaQY8icib6NHVnVqr1TCoHRMgGSJwSPBX13ohkg67AzRzrwJoBCpeIQ0LIXD8E0gNIPf6HWOemCdQZQ973zFLKDGgabha6DASO0FL5iVMeYJ-otK6ExyMm7c6LoZY5mmYTUAoxuZ3_Yf3Hu71PIfnteRFl4Y0LIRV0fnaai0iJGnqfT4GRtFFTjctZLRbbQSz1W9FnIsBep1XEcUziYFlRRnsn6LN1zms7iZpqruzaA7bfVZPh7g1AL1OymMWweLRnbnd6jtJXvCGCvlf6DDvqIxp_OpTFHx6j2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=F22QItM-hzKyKinD9NKAF2VD2DSDVO8TW4Ow5_alQvTAfuA_xjNaQY8icib6NHVnVqr1TCoHRMgGSJwSPBX13ohkg67AzRzrwJoBCpeIQ0LIXD8E0gNIPf6HWOemCdQZQ973zFLKDGgabha6DASO0FL5iVMeYJ-otK6ExyMm7c6LoZY5mmYTUAoxuZ3_Yf3Hu71PIfnteRFl4Y0LIRV0fnaai0iJGnqfT4GRtFFTjctZLRbbQSz1W9FnIsBep1XEcUziYFlRRnsn6LN1zms7iZpqruzaA7bfVZPh7g1AL1OymMWweLRnbnd6jtJXvCGCvlf6DDvqIxp_OpTFHx6j2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68160" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
