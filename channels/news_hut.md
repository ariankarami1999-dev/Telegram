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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 18:00:25</div>
<hr>

<div class="tg-post" id="msg-68265">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwK1O-t8oZaj6EIk3Pn6Kx_Z6TDtRKS_shEO4PeAkChk6vaKOLaz4xEq44D_tEWEhl_iA-YL_2iT5bIMZrmmjMEoqvpHECXFmOJgETnYGMb3eXtmle1-UbtdeC7hpgN5YhJKXYdLwtML9qP1ciW5UEmk0QFRCC-kEgAM7sUk4KFrGINqYj1aXS8CR6zkqxkAgrTDoxtpvazhY25kVyhK6JGfvJdBB2o0OpYQ7u8UqtA6s5H5y36zsS9IlVGVBbG8YvdeW9J5CumjQi1UtNDKeqgoCD0SAuGLNJPp3JO_nRHfUeA-aM2D0UYM-M-STtDTSdPC2jj_w1yCHFNK0VRh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لاشه پهپاد انتحاری آمریکایی FLM-136 LUCAS در نزدیکی بندرعباس
پهپاد LUCAS در واقع همتای آمریکایی پهپاد ایرانی «شاهد-۱۳۶» و یک پهپاد تهاجمی یک‌طرفه (انتحاری) و کم‌هزینه است.
@News_Hut</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/news_hut/68265" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68263">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/news_hut/68263" target="_blank">📅 17:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68262">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/68262" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68261">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/68261" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68260">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دیشب تو اوج حملات، ترامپ از جمهوری اسلامی بابت آزادکردن یک شهروند آمریکایی که تو سال ۲۰۲۴ بازداشت شده بود، تشکر کرد
خلاصه اگه امشب حمله‌ای نشد یا شدت حملات کم بود دلیلش رو بدونید
#hjAly‌</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/68260" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68259">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl3TNsk80NrGid6Y2KXtRg_7y938MHMP76UIm3QIUXLs6IrXRLMgkZBkDJijcvOkJDV81fxz-fRNpmmcmYtthU3T9uNux1oVSTE7W9gaoizc7tdmWnGo4ruGBJIQThikvgV0WlSp0Q3i06wrgw46LBea0p0w2HoAKwsVkOhVH_FU5MEcavWZkGnSVVSTxblhmkfByMpuzzGurL9ysDbyt7gEChGL8LDsuBOrNChbA7i1xT1YUeDTEDpNiwdp3e1HzaTUOE0xBEYRiFsTztxIvExTO0MvwmBgZXkmYWOdS2imnQh6vFFgZyj9t0LY1_NGz85JbTiLLtDuwIPNh5vszg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوارنگاره جدید میدان ولیعصر تهران که نوشته «who is D nexT one»و هشتگ لیندسی گراهام هم زیرش قرار داره.
همچنین ‌حروفDT- اول نام دونالد ترامپ رو برجسته نوشتن!
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68259" target="_blank">📅 15:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68258">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">💢
مرد پاکستانی ، عاشق محمدرضاشاه
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/68258" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68257">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQAQu4QGRgmmrmAx1TiISUP4MZ8RJw7k60uNrrH_FiumPmJjycEIe7yjJld9T4g_atTXEtiP1zm59MYe2lQuSFPIrqySiRXjVh63tAAC98jS20_MrnvWQMaUVhMfziSWR63HvLCIDUftSZO9LM-raoQa1vahjUTrfz6YPEDPx35XyEKpWJ1_SLtjWUejfMTSbfsetKH8vP0eibqT8LNcMWLSOfYAO7q_rK3gYxujcw3-teqG_pkxmiuwChiRF9hk6iOziYmtMGfGHJ5E57gG8Z9l5OoqjeDV_gN6UfIDpxp3yp_k-xCL4nky1cITLh1jTVzIothHA-wf-VJC6-T4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نتانیاهو سفر برنامه‌ریزی‌شده خود به ایالات متحده را به تعویق انداخت؛ این تصمیم پس از آن اتخاذ شد که مراسم خاکسپاری سناتور سابق، لیندزی گراهام، به زمانی دیگر در اواخر ماه جاری موکول گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/68257" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68256">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/68256" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68255">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBUImbbH47PBsBuzbROs_rCZR6MuveW8wPebRjITDIs8mt3IdTAl5KOPLYPFw_lUCT_jozJeHygH23A_Rt5e7DNz8HfzhcF5eaBTCiq2-mlvCelFi3dh9VGYYg8t_1BESNimim7Gaa-pGsZhwQoBTLBhJu9gT-fJyigglcSYmcfgW95wkC33cyAuQHaSXlu61-jogs4Hrlg8JDreQ_l1vXfem2Zp79kJ1yQTaDISuf9Nfj3XTp3ALkrQld4eIchxonPfYji4GFp449m7zfqMHGf_SWqRsDGMr_xb7n7W9tlGk-8uPzBs20MSbDlJot9Ps0mDjMgu6sBZUi55d6poNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فینال جام جهانی 28 تیر (یکشنبه) ساعت ده و نیم شبه؛
- یازدهمی‌ها فرداش عربی نهایی دارن
- دوازدهمی‌ها هم دو روز بعدش عربی نهایی دارن
بهترین راه اینه که فینال رو با گزارش عربی نگاه کنید
دیگه عذاب وجدان نمی‌گیرید
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68255" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68254">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAYYGzolDVf-pU7j2k1wg2DzFBp2rHWkRBk4Q4_58StwiRi1g5M1sNF-cTWZvUJtuM8yCvSl03KNAW0PGCmPIxg2vnaqlZFzDrwd2m_7eFOQM-bIfCajeMSDRAOsbWonYMNv3Yj4UgNgOHSd-xsCFYIpbZ9LB2c_fG9hZFij4-objtwUtTQdv7FtQQdGiZs0UufGZ_LGpkzp55dt7f91ru67bTj5vYR9ojzCbMTA1T_S3puszBY0KI_mTZY90F8jQxOe_X3BSAtSAMcR43n3sPG2WPrRPEr2Ab4sVAhdGTXLZiG77jL31zOnfLn7f_zc3gXTt9yWV9Pf5oiTSudqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:  کارگاه قیرسازی حرم آتیش گرفته!  @News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68254" target="_blank">📅 13:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68253">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68253" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68252">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVaCSL5XtNsXqbHm2kH6a6Q9Wg8OlXq9S6wURjxJYxxTTEly5YlRYruV-8iinUOcmqBkecFMED7WfLubedV7GG8dKqc6OW-jk9-gYJFAVmOkaiD4ch1CBVttx2_NBL4l-qGUTKFAcP-Jkb3IIWHGNLHkbXhybrKOQlO0SgbPMgIHx7aFdqzCFsZaSz5QUVtYOWwPI0mgo-ZXg_JMjcE89AMxh8DP1SK0vcceHb9rIHgwaCUd-8Tl6k9pNjUzWpfwpeM1xo_qLvxrxlt391gNF9FQQsUkkRL09KaVv2_MvF0kAx0tO9ysUrwX2ftyS6MvTJIdk3ViyPJKX2cVASEHIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتش‌سوزی در حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68252" target="_blank">📅 12:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68251">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68251" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68250">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlO0y1BmTZlmKQHlE1PGh47EtMZTwinyZEpmWw_aCDqNEv2Z0EsOIdfkNg6nIrmBp8B80xwcus7a5SmE8Za33zu9hFVO6XcdVLRORTLfeqkX21yaRe2Pp3IaxEAOOy3tcm4WC5-JJOVV797hTm9DsTZkW-LSX4SiDnbbJ2aFyLpvAk5RxTQ3tMVxcxd7Q2kWJwbo6rU99HVuHf3F8ITQWhcG4mI2zHrU2Tj8yZm7QEYw0MU9bME5t8qs7265MS66i-rcvL_DL9NAnaTDZBuzjaLiZTLvSOlaQWak1m14jYjMdBDRCm5LAXdcj1y1fgftEePnjDW7nXK385rjiv6CVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ:
ایران اجازه داده یک شهروند آمریکایی که در دسامبر ۲۰۲۴ و در دوران ریاست‌جمهوری جو بایدن بازداشت شده بود، از کشور خارج شود.
این زن اکنون در سلامت کامل و شرایطی مناسب خارج از ایران قرار دارد. آمریکا از این اقدام مبتنی بر حسن نیت ایران قدردانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68250" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68249">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68249" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68248">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68248" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68247">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⏺
صحبت های روح‌الله زم درباره حلقه نارمک و جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68247" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68246">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYp0b4gh2gqoRfL4EZJ4w83Wo6HR2FSR6N_CWh93-_x0xmKCjvCLGNkRRbCNPGp9l4_-RBU8v654nIZbKtg3Wj8khi_HbEIJTVNyO7D6Gujjl7ob3jAhXZTVuCCK7QXTBRyYJydz-VftSUzp-vWEO5la7FhlTFHDYYOFVUQPKW0mhvO-cL_PLxbuNDpHnSZMg_nePjojVXYhLLeZ2Gdu1Li7Hos9VQgcgYmEwmPsQWfX9uGz_pxsXh3kNx22gQlEclPrOtYaVbnD8BUEbzwk8XRR_bO-YQDAobLcTlWCN-H6aeCxMvZEvy6NFFPvYLHnO9Yfx_3MuQiv30ylMQZl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان به نقل از دو منبع آگاه:
دونالد ترامپ، رییس‌جمهوری آمریکا، در حال بررسی گزینه‌های گسترش عملیات نظامی علیه جمهوری اسلامی است. به گفته این منابع، در نشست سه‌شنبه اتاق وضعیت کاخ سفید، راه‌های تشدید فشار بر حکومت ایران برای کاهش کنترل آن بر تنگه هرمز بررسی شد.
بر اساس این گزارش، ترامپ احتمال عملیات برای تصرف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و حمله به تاسیسات زیرزمینی کوه «پیک‌اکس» که گفته می‌شود با برنامه هسته‌ای جمهوری اسلامی مرتبط است را بررسی می‌کند. با این حال، او گفته است ممکن است عملیات زمینی برای تصرف جزیره خارک را کشور دیگری انجام دهد.
سی‌ان‌ان همچنین گزارش داد جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگویی تاکید کرده است که جنگ تنها با ابزار نظامی به نتیجه نمی‌رسد و در کنار فشار نظامی، گفت‌وگو برای حل بحران نیز ضروری است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68246" target="_blank">📅 09:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68245">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68245" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68244">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68244" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68243">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68243" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68242">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68242" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68241">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5AhL3fFixE9Q3w-4P28_Oo5La_8RHgf2WbRgrMnoGfAzKfHiX4LwC9b0LyMzZ3gm4pkxXB2Mwq5xF-OPCXbc0IUAmm930EFLmu-trBUL5BYg163q724t7kAmzIMueQBKlBSEPUAEiuOtB2cdHrpeOTBUQHp-JSm_4vGvLGvtb3ItIyz6CLGWcgV3W6pn-MzjHzIK3kQZxEL8BnMYgu0AoYngrAYY0YlIsYw-R2Y4i3YvEgOO2b5T05ydEf5Kov7roJVQ29Zo4ZmBs_WRAo5XrTQXOIAnSjssCfcD_gd-6PvQuOfUDed5RcNXH7H7nT3H__UJ_7s2I1Qy0SMBhpGiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68241" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68240">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68240" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68239">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68239" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68238">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
بندرعباس بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68238" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68237">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68237" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68236">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68236" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68235">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68235" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68234">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">من خودم رئالیم ولی برای مسی باید ایستاده دست زد
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68234" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68233">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=hRd0T7btYjimxOpZNx5eDR6KBFvuZI4NZ4Qt227ZS90BAKRMl2NzhSkPTpr90y7LLEKhB_U5AFl7dGNmYOZNu9FMfbvghDMOv7etCfps_pq9XaxocDiK1n-vJ6XDWtuG-9gdpa1P_heIoGu3efmBpar1MPHOI-qeCHNCp3H1-bxiCJMsocw1w7YwWMwphwsZzWqXyrkWUetaZrDgpmYAw8WUfgcCXHhxg2mgbglokqK8Ojaf0hEPROE3Ixpb6doKkKr_wHnTxPCdbhp5nPwoYGOzKFFxovqe1BaZcf-0HcH8KTSS5H9v8BhSriRG_eH2jhCWd3A3xZgbJVf98zcY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=hRd0T7btYjimxOpZNx5eDR6KBFvuZI4NZ4Qt227ZS90BAKRMl2NzhSkPTpr90y7LLEKhB_U5AFl7dGNmYOZNu9FMfbvghDMOv7etCfps_pq9XaxocDiK1n-vJ6XDWtuG-9gdpa1P_heIoGu3efmBpar1MPHOI-qeCHNCp3H1-bxiCJMsocw1w7YwWMwphwsZzWqXyrkWUetaZrDgpmYAw8WUfgcCXHhxg2mgbglokqK8Ojaf0hEPROE3Ixpb6doKkKr_wHnTxPCdbhp5nPwoYGOzKFFxovqe1BaZcf-0HcH8KTSS5H9v8BhSriRG_eH2jhCWd3A3xZgbJVf98zcY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68233" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68232">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گللل دومممم آرژانتین
💢
💢
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68232" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68231">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گگیایایتیلیاایایاااللل دوممممم</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68231" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68230">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68230" target="_blank">📅 00:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68229">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گلللللل تساوی آرژانتین به انگلیسِ کثیف
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68229" target="_blank">📅 00:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68228">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">درووود بر روح پاک مارادونااااااا درود بر بیبییی</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68228" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68227">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کلم کیریه، کیر تو انگلیس کیر تو کیراستارمر #hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68227" target="_blank">📅 00:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68226">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379978a151.mp4?token=bkA95a00RUeByJdiUx01pl0XPvZZnPUymAjfoLCvkuHFzr5EeXKOyrhFAL62G-CpmpWp_dOugYXL_paMAFeWfaoUCQ7MRaJmSEzvpv3oOOyVBoHuFSNa1bOKNLwM3NoMp7qPbVEmkbSCvvMznM5PwuvSufgXnUMsaGmI9qXKP2bc_Mrl9LMCod-G3kuLfQA9qqbTtdf9_QU3TY7PdksX1Y_r0byJyQ4OYaVcD6I5xbEBmta7W-YRdCtKDqVIB4j4UYI08XfzPEFDs5bjDuoN5_S4RWc2-8WimjMLdI3ylQ3CdiC-dhlDo_UMDKDDYPYgetsoaC5uRaWKR4VQnWg-7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379978a151.mp4?token=bkA95a00RUeByJdiUx01pl0XPvZZnPUymAjfoLCvkuHFzr5EeXKOyrhFAL62G-CpmpWp_dOugYXL_paMAFeWfaoUCQ7MRaJmSEzvpv3oOOyVBoHuFSNa1bOKNLwM3NoMp7qPbVEmkbSCvvMznM5PwuvSufgXnUMsaGmI9qXKP2bc_Mrl9LMCod-G3kuLfQA9qqbTtdf9_QU3TY7PdksX1Y_r0byJyQ4OYaVcD6I5xbEBmta7W-YRdCtKDqVIB4j4UYI08XfzPEFDs5bjDuoN5_S4RWc2-8WimjMLdI3ylQ3CdiC-dhlDo_UMDKDDYPYgetsoaC5uRaWKR4VQnWg-7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی به زودی شکست خواهد خورد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68226" target="_blank">📅 00:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68225">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94485380c.mp4?token=JWhi4BQw3j8x6PjoORFzLqrIh38X2jbRqZFqxMWxDVg0viFYR4I9eEtXCDOEcNGEtfsjxp7zNGKGd9WnJ8SjXw6-08-CpqVmd-zcWEUgCQVZNE-SBZDHMjMoPMcSwjFYcClvz_WuAJxde_s8thMDqg_wGETXIlpN8I4uzuRhz-Ok24RAtOW3W4MUUpxswJNRG_2WiWWGA96Ym63f8UyVAltwaHIqw3v-UC9t1vaJ_VmwKdbG1JeJNtsp7A0GQNkPwc8vdtqaOtvfSeAyaqMaJQ9jNloyxH1PsauZXob8hGMcFooPOx1GGldUU8p_6pVrq1oXt-3eByez-EteosO4Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94485380c.mp4?token=JWhi4BQw3j8x6PjoORFzLqrIh38X2jbRqZFqxMWxDVg0viFYR4I9eEtXCDOEcNGEtfsjxp7zNGKGd9WnJ8SjXw6-08-CpqVmd-zcWEUgCQVZNE-SBZDHMjMoPMcSwjFYcClvz_WuAJxde_s8thMDqg_wGETXIlpN8I4uzuRhz-Ok24RAtOW3W4MUUpxswJNRG_2WiWWGA96Ym63f8UyVAltwaHIqw3v-UC9t1vaJ_VmwKdbG1JeJNtsp7A0GQNkPwc8vdtqaOtvfSeAyaqMaJQ9jNloyxH1PsauZXob8hGMcFooPOx1GGldUU8p_6pVrq1oXt-3eByez-EteosO4Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه حمله آمریکا به سپاه راسک سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68225" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68224">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گل اول انگلیس به آرژانتین توسط گوردون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68224" target="_blank">📅 23:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68223">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
انگلیس اولیو زد به آرژانتین
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68223" target="_blank">📅 23:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68222">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=KKC97cGQchIC6oS3gs1VF11VaBcylBU4skvAGDiYa1GL_MNHlWhzo8mnsz_CfrlftUaa2_MA_mlYAWEozJfmHww8b7KR9-RuhoYLvPbg2axg2o5CJR6V9LZfAb7y1cKT19mT0aApndrRr6UORm1rSen1bHcK73H1UZgXhg0eLCSywBE9vGVm82L2KXU-Ma-JHhOTuCM53uCckxpsQDPp4I3Q67LQSuvzVRL4uuKg7Waj9jHOgV76gdog7_GJtgLiVf2bH6pYNdI0cYEMV81XyRerFZoFXe3OcClf9o53gOdT6XtNcabFnNzuI2uMdBYq0wPH_0Dx88HBH6odgeLmwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a007633a2.mp4?token=KKC97cGQchIC6oS3gs1VF11VaBcylBU4skvAGDiYa1GL_MNHlWhzo8mnsz_CfrlftUaa2_MA_mlYAWEozJfmHww8b7KR9-RuhoYLvPbg2axg2o5CJR6V9LZfAb7y1cKT19mT0aApndrRr6UORm1rSen1bHcK73H1UZgXhg0eLCSywBE9vGVm82L2KXU-Ma-JHhOTuCM53uCckxpsQDPp4I3Q67LQSuvzVRL4uuKg7Waj9jHOgV76gdog7_GJtgLiVf2bH6pYNdI0cYEMV81XyRerFZoFXe3OcClf9o53gOdT6XtNcabFnNzuI2uMdBYq0wPH_0Dx88HBH6odgeLmwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شما به این نتیجه رسیدید که نمی‌توانید با سپاه پاسداران مذاکره کنید، آیا این به این معنی است که ممکن است آنها را مانند داعش از بین ببرید؟
🇺🇸
ترامپ:
بله. همینطور است. درست زمانی که داشتم به اینجا می‌آمدم، تماسی دریافت کردیم و آنها (ایرانی‌ها) می‌خواهند ملاقات کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68222" target="_blank">📅 23:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68221">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48590994cc.mp4?token=u5zm4Kd8gsigeXGiC-P-iuOmBabxFNJUiCpfQGpGQtF06bEFxEBMpW2ZRC1gfvITRzzNdPrX-ugdtMFmcjCiPEbeah4PATB8rqYN6kSigSN-dtyNpIAylBOXBNoA3v9IblCIhkiMWTBzakS5n3hLvpzpbffYYYC43gajeeLrb3bKUC4QPskFT0MejnZ1uH8rY6cswuU7qkqxGeVJMx41rrjMftaZApYwKhRoFj0HwSF_6fOxRg54Mgi8rpoNLo9kymZkCSEJLrORssp8rqhXFuSkS9MPLY9gDG2W5i6ouUijvbyQbBoYIe6H6Gel9DMemilEUqbX6VjFdE1zOeRgaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48590994cc.mp4?token=u5zm4Kd8gsigeXGiC-P-iuOmBabxFNJUiCpfQGpGQtF06bEFxEBMpW2ZRC1gfvITRzzNdPrX-ugdtMFmcjCiPEbeah4PATB8rqYN6kSigSN-dtyNpIAylBOXBNoA3v9IblCIhkiMWTBzakS5n3hLvpzpbffYYYC43gajeeLrb3bKUC4QPskFT0MejnZ1uH8rY6cswuU7qkqxGeVJMx41rrjMftaZApYwKhRoFj0HwSF_6fOxRg54Mgi8rpoNLo9kymZkCSEJLrORssp8rqhXFuSkS9MPLY9gDG2W5i6ouUijvbyQbBoYIe6H6Gel9DMemilEUqbX6VjFdE1zOeRgaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68221" target="_blank">📅 23:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68220">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">برق بعضی از مناطق اهواز قطع شده، خونه ها دارن می‌لرزن
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68220" target="_blank">📅 23:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68219">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ
مادرقحبه‌ی هزارپدر
: ایرانیا خیلی دنبال توافقن می‌خوان جلسه بزارن
#hjAly‌</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68219" target="_blank">📅 23:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68218">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
گزارش ممبرا از اهواز:
اهواز قطع برق منطقه احداثی
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68218" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68217">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده #hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68217" target="_blank">📅 23:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68216">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ead41427.mp4?token=t-JRpK-B98xryzCUXgFduVAynynv2IT2oEScSjk0gF-N1EvSCgUOLM4mubTaYrT7wQ9Wg5GUY8E_RmcqM_WEq44iAsWVeEEfOo1hWZfe-4tFnJEgIx_nG3ADl9rjLKc64kW6nC5hWU7PWupoSdln1Wxfng7UDjptZPRfrXH5m8LjXH4gFwslQnIdJyWAAKtB4ez1oHsnsdhFlSa73_XTrcifQj3VTFjnXUIcBQM1PeTMbjy1iFEHLk1vP09tlIF8sxtGjHq4lRPk2H7UVsR5PkaZcP7GV7isdbFeMpQpEK3M55bDfduEXU141NscxM-O5bHJ7uBOMmZfvQWe9e-Wig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ead41427.mp4?token=t-JRpK-B98xryzCUXgFduVAynynv2IT2oEScSjk0gF-N1EvSCgUOLM4mubTaYrT7wQ9Wg5GUY8E_RmcqM_WEq44iAsWVeEEfOo1hWZfe-4tFnJEgIx_nG3ADl9rjLKc64kW6nC5hWU7PWupoSdln1Wxfng7UDjptZPRfrXH5m8LjXH4gFwslQnIdJyWAAKtB4ez1oHsnsdhFlSa73_XTrcifQj3VTFjnXUIcBQM1PeTMbjy1iFEHLk1vP09tlIF8sxtGjHq4lRPk2H7UVsR5PkaZcP7GV7isdbFeMpQpEK3M55bDfduEXU141NscxM-O5bHJ7uBOMmZfvQWe9e-Wig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اهواز رو وحشتناک دارن میزنن
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68216" target="_blank">📅 23:03 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68215">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ممبرا از اهواز گزارش لحظه‌ای می‌دن، حداقل تا الان ۱۲ بار صدای انفجار شدید شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68215" target="_blank">📅 23:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68214">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
اهواز رو دارن میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68214" target="_blank">📅 22:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68213">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
گزارش ممبرا:
مجدد انفجار در اهواز خیلییی شدید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68213" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68212">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmatglHO8yea672lGaXboRQzeTExIV81oWap0wO1FrLjtoAp3MRx3RFWYkTu1OtFDirHJThXSmRQ-KZgQNxJmgM6gMSQg6NwXcRCO1rLLbx3tDvAxAlYDxTA-DNpY3z11roY_Yj-g60OGo07CUk8MGwRm3VVHlq9WtZ6_TRLITffHbTHpKnkk__jZ14PxYJp0XRWTHdWE0aLpJj_lLmaQxKufuGnwS0RsuN2Ux8_s-8QE4rVomBX70reWXKSp7eCfObcQAFJVW6Ba8SyC4tb7zoR6RDbb95BqKzAdwF_rNZyUkSmyJjutDBiylC8AbTtXh39DZFtpaBFqg6SWWzEeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند؛ تنگه‌ای بین‌المللی که برای تجارت جهانی حیاتی است.
ارتش ایالات متحده در پی دستور فرمانده کل قوا، ایران را پاسخگو می‌داند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68212" target="_blank">📅 22:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68211">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68211" target="_blank">📅 22:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68210">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
گویا انفجار ها خیلییی شدید بوده
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68210" target="_blank">📅 22:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68209">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68209" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68208">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=bI0nV4qdHQGfyZWpzGWDZv5JQPvOdQOvSuFKmIr9u1FLeOfAYY-asgC69ZDB6iouQThT7VmpJoYBEgoQRhP-Yg0wWJFt82BaHKM3bQReEqF2rb9KHseJkUSp7aHr8p4eWTmlMA4gDZ-oZIinGaRbAawPvAI_A_Bf_zzGZGkLdwtiPicHXe3B232ibkq0w05tK2PK-dj1qf4qSV_hrgf4m31ZF715xmTp3Vnzp10pEeYn4kXbaleImdRBd_-Sr4bSUbYso-w5XYr9z8HyKRLgFvr5o3Mv2G2xh0HZfBY_-whISLbx2ruNP_fEfh454xTsnjTLz9F67DvJsdmwpOrM9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c19ec2f58.mp4?token=bI0nV4qdHQGfyZWpzGWDZv5JQPvOdQOvSuFKmIr9u1FLeOfAYY-asgC69ZDB6iouQThT7VmpJoYBEgoQRhP-Yg0wWJFt82BaHKM3bQReEqF2rb9KHseJkUSp7aHr8p4eWTmlMA4gDZ-oZIinGaRbAawPvAI_A_Bf_zzGZGkLdwtiPicHXe3B232ibkq0w05tK2PK-dj1qf4qSV_hrgf4m31ZF715xmTp3Vnzp10pEeYn4kXbaleImdRBd_-Sr4bSUbYso-w5XYr9z8HyKRLgFvr5o3Mv2G2xh0HZfBY_-whISLbx2ruNP_fEfh454xTsnjTLz9F67DvJsdmwpOrM9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68208" target="_blank">📅 22:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68207">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
سه انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68207" target="_blank">📅 22:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68206">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=FVn7YvZtuAjDO7thSWQcTIqznclLYZpflELqTyhd4NQwpGumUg4Hqjb0_MClW9zJnGUgeasQwzLqek7VK1x70WOqKmg8VRyHKOTo2aGdhVo-dv6XO0eWcBmj8uzp-OBlxq0mRw4ELkgQirSEiDYZ4YRxJ9TunrjYurXlVL4yvb6owhUepDrTUc_1Mg7MNaA5jmPH1somvFYT0a2amtwYn0scjdwF4LYYwXdINpWmXKhwXuB8j_qTPBx6xyRJW-c6WQ92aAEOzMgGWGxbL-BHnWuzx-ISFzqW7jOTlQ1l1sUG4Wo-mdAO2YYr-ttLKIgyztszBlckJQJvLcmIYbGmkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f6a0a0f4.mp4?token=FVn7YvZtuAjDO7thSWQcTIqznclLYZpflELqTyhd4NQwpGumUg4Hqjb0_MClW9zJnGUgeasQwzLqek7VK1x70WOqKmg8VRyHKOTo2aGdhVo-dv6XO0eWcBmj8uzp-OBlxq0mRw4ELkgQirSEiDYZ4YRxJ9TunrjYurXlVL4yvb6owhUepDrTUc_1Mg7MNaA5jmPH1somvFYT0a2amtwYn0scjdwF4LYYwXdINpWmXKhwXuB8j_qTPBx6xyRJW-c6WQ92aAEOzMgGWGxbL-BHnWuzx-ISFzqW7jOTlQ1l1sUG4Wo-mdAO2YYr-ttLKIgyztszBlckJQJvLcmIYbGmkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از کسی که در برنامه زنده می‌خواست شب‌پره بگیره چه انتظاری داشتید آخه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68206" target="_blank">📅 22:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68205">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
یه هموطن داشت از محل برخورد موشک ها به چابهار فیلمبرداری میکرد که یهو برج مراقبت دریایی رو زدن
‌
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68205" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68204">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvuiLuyyEXPgdbfqdNYDx4ELN7ecBSy_yIRdqfeYWqBOKGs1xbOVBJp-nQLOwBdl4q0fvFRmkokFAYPOZgkwB1E-4hPSshXFg4uHOlQ8nwccSDRgE7VWjJcNXwpoFgh9Ca1oXrTt5CbqB6seA5MWbUMMdvQiuTc30IgRgffW1LRy_dhSOJIs2e6aJqEZNj2rAAmTRIK1mP0mN2SZkG40liOCE9Gq6AayC1tL8HSZ-PVsZ_az7EWeQe0uRau12DFQgRd-8JFzxhubZTrhKr7nFJsRruyxLEFDRUzRZE-KFrjrm2EiLh7RRTtQyS48VGD2lYVMZepzS3k0lUC_8NyjdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68204" target="_blank">📅 21:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68203">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🇺🇸
فاکس نیوز به نقل از ترامپ:
حملات علیه ایران هفته آینده گسترش خواهد یافت، و خاورمیانه خود را برای اتفاقاتی که بعداً رخ خواهد داد، آماده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68203" target="_blank">📅 21:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68201">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VAgZUj-j-yA2ho_tm_zpzri8WbKzN1jjaEvyXnWPsQxA-0OOTo9Kg-4GSjkRtsRie1Sd0iGozbW301PxI2g-XFdyniwl9nF1P941AND6Ht5HwVMTnZ7u3sQP_yxct7pd2ZCtTTANjmUnbyX-mJp1fPltc3MJ4eSlDXxXDAZv--rd05c9tJS-xK70wbhpBZfqbulMZKX-3pO395p_8Uc8t1uZgt1OtrYFuk8smfsnN23-C9y8yRLfPgwNCDqPQdKGnAZFU0NoDYnC5IQwmQ2wS9enmAu_DThRgcDLtwYiW6fwdBpKfqg-XFEV9PDzUagGVZfvCzsXGl29cTo2SIjy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEBQfgXut5MoRiMjGdRp-3zguC7fTZIzLEoACPn_n45BVO7x1ssN_wS7R2Mu59AvIxYdkDdxpghLAje-DxEjZmQo_zDcSoOs27fvBMlQ_wDBf6w0git42jSJphG8V326vspRnFoUBF5Bi7XY5eEfJIcY7-z9drkvk3EM_gs8m-G40LI17aqbIrBZNIyog6ADBPPI4EqYge3a3fnEx0YEqSmdEG9UL6nEpMEMr25jp7gf4OJaI9uTILd1XeToq-OjPlbJlRE-GETufDYjsVJ-hHyFeqr83OzpnC3cuDM0vBrCurTnMX-EnStm4OB8cGO7E1phU3UWslxqKhHakq-zgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ترکیب انگلیس و آرژانتین برای بازی امشب
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68201" target="_blank">📅 21:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68200">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
قالیباف:
همزمان با درگیری‌ها، باید از ابزارهای دیپلماسی و مذاکره نیز استفاده کنیم، به گونه‌ای که منافع ملی را تأمین و تقویت کند.
همانطور که بارها تاکید کرده‌ام، مذاکره در این مرحله به معنای تسلیم یا ارائه امتیازات نیست، بلکه در کنار جنگ، بخشی از استراتژی مقاومت و حفظ منافع ملی است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68200" target="_blank">📅 21:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68199">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
قالیباف:
برای ما مسجل است که انتقام خون آقای شهیدمان را به ثمر خواهیم نشاند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68199" target="_blank">📅 21:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68198">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
محمدباقر قالیباف:
تفاهم‌نامه وقتی معنا دارد که مفادش معتبر و در حال اجرا باشد. اگر ایران از آن سودی نبرد، دلیلی برای پایبندی وجود ندارد. ما بر اساس اصل «چشم در برابر چشم» عمل می‌کنیم و در برابر بدعهدی، متقابلاً واکنش نشان می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68198" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68197">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68197" target="_blank">📅 21:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc9lHH_ZnM4ve35uVzdyOgGurwZBDHFQQWuPIa3nZoGetuGgaeTS9X7Gdod1RLJVwWphdaQ2OIOA2u9M_tMBXpHD2hP5yWA5r6vIyf1RSKncuGz6Ukc7ejKKv4Ly-mVzadknwholFna0Bn3gYXJMLBnUWynmbty32HOan6ITFZNrqjJ5kCQex8j_2c0NBfnXqANqysmEdXXlo1nJaC8RdM3yLVQofBp-8w3xTU1Fky84jK83RFjpCpYpnLzRl2sJWECMZTdWx5l-utKkx_JZLAylTgaXkZJ30r6aDWIBloPdHq85vPoT04aU_STm-9ubw7aICIYmbojWTD5C5w8VnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر شهدای حمله آمریکا به پادگان ارتش در ‎بمپور.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68196" target="_blank">📅 20:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOMO9qYO3IdxEudYcQB2PiORVaxWecmU_l9FpSM77fUqt_LICNlbNXWGcNu4GfpJQIZvjw32ILMRFc4LC2rI7GTFrnYA3YBhgdoqQYiaQOpINOmGXKzfp8pebWeOThhTJmEBQL7K_lztZRUiWtmbxv1mHOxcFJO51VLK94QWCyJYqYKByv9zxrfEfY_uh5dDkGiG-xcHGRXLZYi579c2VIaR1_QNYbpfm_V_khKQGvFuaDzqTZN0SIZJ4cs1G7NIUpFDdIuAhy4Z3WpsKNz9I31EVkpGOLoxlR8maQ_Xw-hfCb5f_P_nokrD3MLKVYqW86jJGu3nYhynMhx3R8K3nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب عادل دو تا اسطوره‌ی تکرار نشدنی رو آورده، فوتبال ۳۶۰ رو از دست ندین،
کص‌خار میثاقی
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68195" target="_blank">📅 20:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68193">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMreza</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCqmqK_x4u1fN7mK63XuLYtAmCnhpIdKjwRqbKaYztlYQmDjjaSlW8bjCLuIOyDT5MpeXbOjBDCzzl5_7lHVLWQYmTCkUkMP-tdNRX22KboYQqya5XJFBW7qDmAO5BMT2-5w7hQHPUZrETBZSotAmxjUlnctzcxdKd5GqPxgKZ-JGfg0pKX8v6RGGQATrwuZYWBjsObsnXYm-pwCXh4CyNLOoBmZZHtCQtetk0nSUUHJxkxCuNYGz92tvyE_NuXOGy0sxvQHogL_BVn0KINxI8yPrR-lVEMFW5ucWuxTVdWilxz8uLPSs55U9xicFpfUw4nskJANA3A6_wy7ffRm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vcF6B3H_jUtxogRQIi1SKcSHl2IQFsg_Aqlw71VrdsB101plBLbc9opGh04JpTKGc13brGgxaFiLJaXnPq0tEL-MeML9Rh_jrfhrkN8sLamphsZy6ALN_KKRChIA6TweX0QhuIaBqmBd7cmsH1sLIa3yFcRCf_PwbVmAOLM8DHSadS9MhhVuBFZ5pJb0GzJerzNPNC8BSfgNabhOO7jYgDxfPFr1BlnYbhz_q7BCudOY02ONr1FQEjZzNcG0PXCSG6WrN3GBXuvu14ZY4pgiIe6HG96aCCQCbbpnlkMQmWDhyhEF4cZk1F82kYfoLf7vBQ2RYkpGvv691xh63nm61g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Siuuuuuuu
❌
Zhiuuuuuu
✅</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68193" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68192">
<div class="tg-post-header">📌 پیام #30</div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68192" target="_blank">📅 20:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68191">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j52am25i5kemhhR36q_63b7PMUS2T3kgsxt5P680bp_yflHzrzvX7qpw4013wqMmNXo5KQkcjL_eUZOHFz4UMhHHM3paGzVpvQHfzG6gSAuFojvKbCHMJpagoKwOuPrF_tGQL2N5t7a9yFmt962YY0f3KEwm65FknJCLdHIDJ-bjg8k_evp8pFZYJShdIe4pEdqUpiNx6fr3YCHSwLdATDw1tr17flDGOoy0EBMuSoARLuh6OdIc0yfa1_1UMcFa06sCJZKHIxVmXYNTjtk50drnIISt4o4OoE9w7NfraGSlDHIU2g-mQfyYooYeMIq-mC-TdQE5Ajo2-OutfWbsxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو خامنه‌ای کرایه اسنپ نداشت بره سازمان؟
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68191" target="_blank">📅 20:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68190">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرونالدو</strong></div>
<div class="tg-text">اخه من چکارم؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68190" target="_blank">📅 20:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68189">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rODDanmQcbuFWRSXfCBBdbiiGZFlHTgx7gGsCIPBzjwChGyv3WgKfdQ0Z_ldqz3gz9QzbAx4gnrp0devOyTHsbJPdRyw7qimCfDzxvxAPXd-oVFVN4gAsKOMbUOyvkWOoQ0_YghNHqISb_Y7_fkZPgPCiYhbP0zt_V9DJlx_uuPeM0iqtPQxF81rPDIcHaA-jcWac_-oces9uPkKd78gBcpno6NTiqEkpeaI1EH_dDmr_ET4lbHGsp5Miyq0SGMu6nyHnyh6MZ0tVDSxFrlxIMc_hvoZ6QliALfHdYcWGfcdlniHeZy8PXWDmCd5gx2jvCdP8kc66jVy-A3Y_CH2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:  #hjAly‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68189" target="_blank">📅 19:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68188">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=na-foUyQ7yvA9q6rLPo5uojcyh5bbMLc1HKl9DD7HKIsAb7M2-w-XqDsOST96o_2uHeJ4bpPE2u3SxKiSLHw2ATL4QsEWDzWOS7MVEt2VSZiYPgF9lDRTR5pkT5BSrFiiC1oZT4FnXpJDjm2_7cMMn6h9PWeKNCK7uBnG_X5JUXZ1BESialW4HVZTzI2b678HV8Gd-yAOV3G9CMZloAU_91dBTuf8RkaRcBzvVLzF3BjXk2AVVUw2HJViFlv4LlCYq1zBjmN6Na40nizSCMI0IH5kfZeQUsh9ekidijuxwjEJvLUvq0wnQCWcxqwJ584nxxDWJuDaNDUNxBoYIFRMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b2e5150b.mp4?token=na-foUyQ7yvA9q6rLPo5uojcyh5bbMLc1HKl9DD7HKIsAb7M2-w-XqDsOST96o_2uHeJ4bpPE2u3SxKiSLHw2ATL4QsEWDzWOS7MVEt2VSZiYPgF9lDRTR5pkT5BSrFiiC1oZT4FnXpJDjm2_7cMMn6h9PWeKNCK7uBnG_X5JUXZ1BESialW4HVZTzI2b678HV8Gd-yAOV3G9CMZloAU_91dBTuf8RkaRcBzvVLzF3BjXk2AVVUw2HJViFlv4LlCYq1zBjmN6Na40nizSCMI0IH5kfZeQUsh9ekidijuxwjEJvLUvq0wnQCWcxqwJ584nxxDWJuDaNDUNxBoYIFRMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به یاد سربازان تیپ ۳۸۸ بمپور
💔
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68188" target="_blank">📅 19:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68187">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پاساز علاءالدین خبری نیست، ویدیو های منتشر شده مربوط به‌ گذشته‌ست
#hjAly‌</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68187" target="_blank">📅 19:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68186">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mG0VSbQLmXcurLGxYYtuu1GhQHlDZOF904O7QssZoRlcS3-U8JFExb0k0d32XLTGk-EQ8gOoMc7St2fYpkRjStsP3v8ul-19TujBU542X77USn2xv7frfdZ8FJLDm1OMIoaLITR61ZdoEDfGLovhxd51gaYMccZW8hzqTR6immRgclbCGKDdiyxQhBQTdHoOakICOGP6WLv8I65L54y5PMDC41jofcWfeT4d5rJxNLRVZXApzRzQw0Cj1e8IjKWBZ795yJNNths_rjgEbZN8e3PyeIvciu77nWgk-Rwbq2mgNaJFiL8kmCvLtSoK0WJp2DFAkFC9I9t5e-XTsmRorw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:
❌
ادعا: رسانه‌های دولتی ایران مدعی هستند که نیروهای آمریکایی در تاریخ ۱۴ ژوئیه به یک انبار غیرنظامی گندم در هویزه حمله کرده‌اند. این ادعا نادرست است.
✔️
واقعیت: در تاریخ ۱۴ ژوئیه، نیروهای آمریکایی اهداف نظامی ایران را در بندرعباس، خورموج، اهواز، قشم، تنب، بوشهر و کوه استک هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را تضعیف کنند. در همین حال، ایران غیرنظامیان بی‌گناهی را که از این تنگه عبور می‌کنند و همچنین در کشورهای همسایه حوزه خلیج [فارس] حضور دارند، هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68186" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68185">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8ggYzqgjGxOWKlRzVBMgfl0qmbJB2DtiBQBVXDHtjIg8PRrQ1W4cbBJBd8aVoPE4zoZFNfPZsAgc5F0ro3PZiQwU2FYMoqi_2Z37Ys7d_fX6lURfqqg9oMT_W1vLMvQJB5-t0lxHukMCCEwaQRo3dGMvsjtLwd1ZD6tPoLr95yacNxQd_5-qosQXb_zVZbTHbTSYxbXJ-T7SuQnTC8dDTEfRtdUIPfTAo3MLe4iwRsCv8DNwKHyo8yr_1YS00Mh5svlLMJIpVPm7FPuEgyNvdd2sDi38mNTZjXVKFmfrg5JcSrZoLSX6X3RswHWS5T10PupcWLtLqyb4yeWFQ_5ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قراره تا ساعات آینده ممدباقر بیانیه‌ای درباره جنگ و تحولات روز کشور منتشر کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68185" target="_blank">📅 18:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68184">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7R2HCZU8Lglj4C7GnY1J0l2pFyey4BM9FxdvjzOTMbIKcAdaYI-Z4uLn43HXXzYuSb44i4kKXG44xuVSrhcVvGq8JTGpywzhJHxcJa7BExww3e62i-oCcRlJLKQHwvCQOAJ4t06o5_V9j_fJkwZolFN5jIBgWIHdj-wBAvQ1z8kDqdG7Yfvx8EA7QnoG01gEU7HxcdymRKtQF_T1tVQq9k7zRVicdmBNRlBXSCtqCjcz4DG0x-TEt2rpdThUOacimV-gCehXdSmt7w9GfW0CX97ya9Tt1_Ep4EjYH_KCP8IPTGIEBGgaRWxL020dMFEvre7VByzPtxuOtxpMl9yZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
از زمان ازسرگیری محاصره دریایی بنادر ایران در ۱۷ ساعت گذشته، نیروهای آمریکایی مسیر دو کشتی تجاری را که قصد عبور از این محاصره را داشتند، تغییر داده‌اند. ارتش ایالات متحده همچنان هوشیار و آماده است تا از رعایت کامل مقررات اطمینان حاصل کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68184" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68183">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68183" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68182">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg0c_fFAM3Eas1F8QjOOTZ8DqFgOJJHFijR3HUD7nQiofktCIu148cVSSlHMjV-KEckaQQaiAemvQ_HFYgZKCm_Kkj1QjOlHDmYkM6dLLRMwxZpK1bCDZ9YG7i0oTrBwkKyzdrrjsi9Ps03mFxNI3HJQ_RtDXQ7KREK-VpGRReCLVQsJsWuyCdDx91J4clUXq6BytOnqWC3uxlO0exFvy89TwBVi0gmaCTxv8fveYkJgOg3xuVbf0AInJ0pwNvOsUKd19JJoLIKF3JQRlzhJViZ7Aw13Bcrk76bgYQaqw7nbp8cWnd-xxyb58vpBN0oxDR1tqGM3zxwlqDGEYXqtNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68182" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68181">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
انفجار در جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68181" target="_blank">📅 18:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68180">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=gCffOcrqy28QUAu9MAV6FuILCyjsQvSwNYegXxly-CUyCc4jxjLCoSxGAM3QahyPf2niTHHW2j_9AFHkhVDF0ZgOUsqhFhXJcJ23aeDR_374Uqrr6Ff8CUp3lXQW6qN_ATXYltQIH_ceaGV6XSQtA8XHjz7xVoa0uWwSHuwblJOKQIutXb6AKLOXiDDbg5D1TViQ--PwszXAmXE_c84qqASXpNHjs-3NmdvvvUWWiCYrSxl05aMKPd9_ZxOSKyW50Vh6CoT5D4yfTLoSmP-FduhntuKugCAMVhhaKfcB7wwaKOgdu7MOSKLVYF12iFtEC_A0zJAM0i5Udzw5gI0ebA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415d2aa12e.mp4?token=gCffOcrqy28QUAu9MAV6FuILCyjsQvSwNYegXxly-CUyCc4jxjLCoSxGAM3QahyPf2niTHHW2j_9AFHkhVDF0ZgOUsqhFhXJcJ23aeDR_374Uqrr6Ff8CUp3lXQW6qN_ATXYltQIH_ceaGV6XSQtA8XHjz7xVoa0uWwSHuwblJOKQIutXb6AKLOXiDDbg5D1TViQ--PwszXAmXE_c84qqASXpNHjs-3NmdvvvUWWiCYrSxl05aMKPd9_ZxOSKyW50Vh6CoT5D4yfTLoSmP-FduhntuKugCAMVhhaKfcB7wwaKOgdu7MOSKLVYF12iFtEC_A0zJAM0i5Udzw5gI0ebA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
منوچهر متکی وزیر خارجه اسبق جمهوری اسلامی کاملا جدی اومده گفته:
باید به پایگاه های آمریکا در منطقه حمله زمینی کنیم و صدتا اسیر بگیریم ازشون و بیاریم ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68180" target="_blank">📅 18:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68179">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68179" target="_blank">📅 17:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68178">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=sD9h-vT-bpyBr2OWXOtYXVAOf23fv-ZgzA0muk5QAGcHc5RZAwbDdh1W9DZ69O-X5JmFkguAQs4a0K8qpCAGwV8KhK2HjHf9tCFvcqjdpu3iH4YItui-V52iF6mXJ4skSGsQrGP8H968Av61sM8xxVnp7oEAaqtc2PIE4pVf3RBn2I5Wr6v25DUc4y9LX7l4Q_pYD-JVBLJQwmlMu9vZdsC06f1eO5MFV0C5lPKdhwv4p4k4CgK3PEg48bshVP4XyrUgmYkPLGXQj82I4qrbwiwusCjX0osKhv3jNSeOTKnJ_kP6fH29ZAtGXwYwuury0rhaxHcivqFlqnsGlxI4Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f97b887b.mp4?token=sD9h-vT-bpyBr2OWXOtYXVAOf23fv-ZgzA0muk5QAGcHc5RZAwbDdh1W9DZ69O-X5JmFkguAQs4a0K8qpCAGwV8KhK2HjHf9tCFvcqjdpu3iH4YItui-V52iF6mXJ4skSGsQrGP8H968Av61sM8xxVnp7oEAaqtc2PIE4pVf3RBn2I5Wr6v25DUc4y9LX7l4Q_pYD-JVBLJQwmlMu9vZdsC06f1eO5MFV0C5lPKdhwv4p4k4CgK3PEg48bshVP4XyrUgmYkPLGXQj82I4qrbwiwusCjX0osKhv3jNSeOTKnJ_kP6fH29ZAtGXwYwuury0rhaxHcivqFlqnsGlxI4Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از وایرال‌ترین ویدیو ها در 24ساعت اخیر در توییتر فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68178" target="_blank">📅 17:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68174">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpYrT6dr-dUA5KySgG_ThbKVEG9yNoE845FvBqQ7Q_pTDaoPJCAIbhkdp7yEMADNIlhAalX9IylF6JjQyDC_ousJAz6hmyj7kJ4Pv2jvd3__HsbSiKe9oPIGxZe_khAlEeRJYH8DoCY7Nos39RL8IO7sj6SW7II0A0bkdO20_eVYR0JKWUop5z99aig0mnsriTfsV_a0qSXuiMldWqeg94cIfXzYUo4hXQMNJFm4Yhgd6Hm26HobDdGWRhCU1wUZPa9YI4KoGIUYRCWMqmkwK32Dn5xBDnZYpHf2PzZfEeyHMj3cwZi7zpESnpKAhvsht8opAoF8PdfACTqNj22A6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=WNV9RtNyqWoDH8Yunr9NJbc-aHV5lNo_jy4UMa4D7sgHLNcIzeDQDfNAZMfVrwst3m_ju3GQqrbky72qpbqZHYdZgDY5RsXzmXfCo-WXpJPIx-9BGddtQNQyGvpixaCtA69bqtAwxWHXOfOO9rLOVyInAQoWBgJp9ylt2V6wsIDQ1jlA-s71iqZMCK63N-6BKRNhrATR4qYz_vGDom94fgef5UE9u8GSTnY_6CDlBiI72HKA5Ys_PLEpPvBAd0GOLNzMPIyZI2cw1X0O3CAZp9vNmqLhFPbqg6SW0J4jLhsfORwPplZ_73mAc9GZtOQBhjRNX0wQ9UsVZa2pigvNig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5effcc1b8.mp4?token=WNV9RtNyqWoDH8Yunr9NJbc-aHV5lNo_jy4UMa4D7sgHLNcIzeDQDfNAZMfVrwst3m_ju3GQqrbky72qpbqZHYdZgDY5RsXzmXfCo-WXpJPIx-9BGddtQNQyGvpixaCtA69bqtAwxWHXOfOO9rLOVyInAQoWBgJp9ylt2V6wsIDQ1jlA-s71iqZMCK63N-6BKRNhrATR4qYz_vGDom94fgef5UE9u8GSTnY_6CDlBiI72HKA5Ys_PLEpPvBAd0GOLNzMPIyZI2cw1X0O3CAZp9vNmqLhFPbqg6SW0J4jLhsfORwPplZ_73mAc9GZtOQBhjRNX0wQ9UsVZa2pigvNig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی منتشر شده از انفجار در چابهار صبح امروز
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68174" target="_blank">📅 16:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68173">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=Y6edt6_mLAbt1aTnB7Thcr31xNa3-xmEn8-3c_ZBEw9L9EpV_24J5A9sjAXZEMK9F9enKtgWwqWOCSr1av04IQYmSN0MJkWjZHNs8Sf39tdjtE0WpFmB0gLMU1Q_6QjtCJnGJ2mTlrR4TCZVVQWv0ViHofELmjOk5ShUgVWLJ6xDhMhTgBCkXLwv8R6z2PB2AZmcY0ZvUydRtMMLkeAzwnG05uiShfv42wf-tGTdNv_MhYg8m5rCmmOCguHMlKak10bZSyCA6oSgnCQlrrzVp6wlW8C_U5JPlFAuvy3nh0op24gWa9OUbL_C3zoPM-pww_flAKpHubaakZA2WBwkQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d7965cf40.mp4?token=Y6edt6_mLAbt1aTnB7Thcr31xNa3-xmEn8-3c_ZBEw9L9EpV_24J5A9sjAXZEMK9F9enKtgWwqWOCSr1av04IQYmSN0MJkWjZHNs8Sf39tdjtE0WpFmB0gLMU1Q_6QjtCJnGJ2mTlrR4TCZVVQWv0ViHofELmjOk5ShUgVWLJ6xDhMhTgBCkXLwv8R6z2PB2AZmcY0ZvUydRtMMLkeAzwnG05uiShfv42wf-tGTdNv_MhYg8m5rCmmOCguHMlKak10bZSyCA6oSgnCQlrrzVp6wlW8C_U5JPlFAuvy3nh0op24gWa9OUbL_C3zoPM-pww_flAKpHubaakZA2WBwkQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۷:۳۰ صبح به وقت شرقی روز ۱۵ ژوئیه، دور دیگری از حملات علیه ایران را به انجام رساند.
سنتکام در جریان این موج عملیاتی ۹۰ دقیقه‌ای، با استفاده از مهمات دقیق‌زن، سامانه‌های پدافند ساحلی و همچنین محل‌های نگهداری و سکوهای پرتاب موشک‌های کروز در جزیره تنب بزرگ را هدف قرار داد.
این حملات توانایی ایران برای حمله به کشتی‌های تجاری در تنگه هرمز را بیش از پیش تضعیف کرد
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68173" target="_blank">📅 15:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68172">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=A00NLhR2hvhD07b6kA5_uEks9FBNckG3Oso-r4I7atUjSKOPw3VABJRRMiP-BvK8ZUbv92dAjWlxXp5-Kr9AoxU95cRKnO3L3fy7LDfj_KH3_D_tnEDIqs22rGaoqun-psm4ppqb6C4bCOZsgQAu4uR8UaESOg8PTj92uRjAqxRHCUA_XPqgExIoAlqWBnIZFCWJH04VQZs7Gj0KujtucFd-K7MFgyLiFSuVdpuinBV3wqhfWcYMXEhcWjQx6OW2vEdH9mvsGkd1qYVoDjR98AYdC69f1Qb9nQ8YLRRPrWaVU4L_K6nFI64tBLzKOOiDkaPRxEiJHW7tjZ47iHzSTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23686eac2.mp4?token=A00NLhR2hvhD07b6kA5_uEks9FBNckG3Oso-r4I7atUjSKOPw3VABJRRMiP-BvK8ZUbv92dAjWlxXp5-Kr9AoxU95cRKnO3L3fy7LDfj_KH3_D_tnEDIqs22rGaoqun-psm4ppqb6C4bCOZsgQAu4uR8UaESOg8PTj92uRjAqxRHCUA_XPqgExIoAlqWBnIZFCWJH04VQZs7Gj0KujtucFd-K7MFgyLiFSuVdpuinBV3wqhfWcYMXEhcWjQx6OW2vEdH9mvsGkd1qYVoDjR98AYdC69f1Qb9nQ8YLRRPrWaVU4L_K6nFI64tBLzKOOiDkaPRxEiJHW7tjZ47iHzSTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGfAdksSN5hNITjiR0Fx3SnRuX6-bxzMjLrvx1_PzoS60qaF1rDwajDHAPHITi3UqZG0sPOycerT-N_EsbDzzfT6fKZHqONeMvBE01_zvAJxE3Y1i7XFBegl6qW6qs7kHFXAEs_oXhafqowzUrvkUH6Vr4XJOK2er167Z3ZyKMUpa9bwmPPoQgH5J5qP7fJsoiJUz42UvDFyUqXp3bLrm9aJaba8xJ56Fa49Rj4I3YcJEBnreZJL8zPb8MYGvoO-FRkn0H6YIybeoDIfg70itWJdftAuZkPn6PBV3oWIiAA_WWy_gwtjJbs_vOnub5q6zpkut0jTYr0Z_1tcyWrKMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری حامد‌لک:
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68171" target="_blank">📅 15:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68170">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2EDKL3aNC1SKQFXTlqCVBsoyxOJRP474tv3B3Kuow6TbfXvl_RI_WLmOgbOpkidfzSLqmSFje3wuid9QqvdLlmlv-zDWZ-nsWjpQ5PJ-yYpoPaPHyqbIF0TiScrOv5Ux235jnmEKeEO2brgRbbmvBnWgdu756aL97YTxcMxZHFvQmghLIEYbrM35yrquWQyJZ3aQBzAmB0_FBsu8mLH5lD3Sbgyl2GOZU5ZipGMXuMhqLqlzXYYGE-pPbOssk-ACSiI3BceZbEes5UtNdEYH5wRPhiN6EMJJfxwI1JAAKsgOdmfTwHtMqVWKbQ6OwB6QBtUQYKxDCDwritKW6fZRg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
پنج انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68169" target="_blank">📅 14:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68168">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">علاوه بر اینکه سوالات یکیه و باید همزمان امتحات گرفته شه، تسنیم اومده گفته فقط نهایی دوازدهمیا تو روز ۲۵ و ۲۷ لغو شده، این درحالیه که دوازدهمیا اصلا ۲۷‌ام امتحان ندارند و یازدهمیا دارن!  باید منتظر واکنش رسمی اموزش و پرورش باشید @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68168" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68167">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le7c4CIWlACBUSvCldDSdVDJtmkRj8MmHOjCaQfh2opQbLzUbA6sUfSnlAndxhZco1FCniqSHpbeZnTVuMIIZKs0Q8WJkI6jrA8B6CO298_fu1C4YdL0cMvb7UO_cxRecbEvZ3mVqZ9_wIa2Nmy9J3vD3oF4Jk_WKJgGv6sp5KsDxThVfW0k6733CifGR0McIFFsIxnFcP5OpcwkMjSwfQFd4UaNRG_DZtBVt4asLQ5PMwDMgiciv6u1DWi6fceFdfpmX9zpbTvRM5BN_GkfPipt9NIz0FBCIorU1JbWXytWHioPehNU6ynwD8PZT8f_zkT6j5HP9PVQLvcBfOwaUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری نهایی رو فقط برا چند منطقه لغو کردین، کاش این دو روز کل ایران رو لغو می‌کردین تا فاجعه‌ای دوباره مثل میناب رخ نده... #hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68167" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68166">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=WNIBEYd7Ls-BMmKLuv2lC5Aq0eQJ97AyFKMNwXX5GGDx_uHcbgQIC5fkt-SfEDWndjmS9KUCnNobEorx855KjKOEle29qs4tPPixRuxFxh7wsXDa8TRzryP1q3NhjknBVJneqKBNWDiRCrH_21l5mh07MgwI37ef9LCej4zt5CWddpIvjmYyo_G_93gbetMdnlxFwlVK2_jDMlcEixALwVep1OFzye7oAwMWeXCOBvdXDHDu88GRsaWaYaB-EzCw73SLKyXnnejbhuT9VeVP4wa-5DYPxiX26Im0KwzlE9CMQUaGVbLg-b29UnL_O41memfuJsYtmHdumqFKJ-xZfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=WNIBEYd7Ls-BMmKLuv2lC5Aq0eQJ97AyFKMNwXX5GGDx_uHcbgQIC5fkt-SfEDWndjmS9KUCnNobEorx855KjKOEle29qs4tPPixRuxFxh7wsXDa8TRzryP1q3NhjknBVJneqKBNWDiRCrH_21l5mh07MgwI37ef9LCej4zt5CWddpIvjmYyo_G_93gbetMdnlxFwlVK2_jDMlcEixALwVep1OFzye7oAwMWeXCOBvdXDHDu88GRsaWaYaB-EzCw73SLKyXnnejbhuT9VeVP4wa-5DYPxiX26Im0KwzlE9CMQUaGVbLg-b29UnL_O41memfuJsYtmHdumqFKJ-xZfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خسارت وارد شده به یک دکل مخابراتی در بندرعباس پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68166" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68165">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
#فوری؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.  وزارت آموزش و پرورش:  بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68165" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68164">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
#فوری
؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه 25 تیر و شنبه 27 تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68164" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68163">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4ApINT5sd7cDWJKUgSSZwjO_QAH5okwqQke3B7z4E4Gayh3neg6AaOjZ24UB4rKmKlVXe4SNdiTJTXLzguZL9mmfcmHONxdixzKFbjpxqzITcZyGHKZDEncRiU5VfgtlvPvnUY-Icui0FuMIV0ixFoe_a7nda2P0jI1UNSeFXqI-okLElUvuOTmMR1uy5PyBuzl9IYGlSs_c22mL_ku06FYoHC_GyPp0m71qmz0W7tGH5IFcvryf_kpENT4z0Zs4PPOMN5id94AfhbipfxBlRKATflYdcNvII3BYPgH0tTIklJoXYkjKTDo-Pe4e6fAoGHBLXh6Sp0irHgyPsXjwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ صبح به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) موجی از حملات را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانمندی‌های نظامی‌ای است که نیروهای ایرانی برای حمله به کشتی‌های تجاری در تنگه هرمز به کار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68163" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68160">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFCnFLItTD8435l1LFgFj2TIz8_prK-dddisuj0WHubfVGRvrYqw_qJqPzAdvnNFCBra0Wex8aetQ9-oY6d8RuCSsAlBtkDoCvUEsigP4aPBq4CcCkk_xMf27TlDXqwvFiAetSYFwtGhvkUmVeqUOnLgu4hvXvypKuPlboC1jlXSOYZXTpLUAwqAWz9prWCrPPuBFbM4s1snNs11jzjGNiptepVxRnpVK3L2EZT6jWWAT0Q-jR1KI_m3vDg10EC7v9dmrVUndcnpUBQ7QYfoUGlgiyv80Ix-4zBAjaavjYvRb0vblwxtHnB4t2yrnH7EDRe2lo8CwP2G2ro4jSAaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/giNxfjLO8KIPPyxADe2m-GOLEuY2yU53EpPekzv-fRtU3AMZzqJ1uOtcnLEvuCdtWwAU6Ohn1Q8WjHC1DS7U2v6ccwad4YJ_q6B37xEkujFKk5fiIedoGYOv8fTTxlOX45vAR2WjcBIXhpGay2k8m00u2XXCmSc-0K-PkYq3NzndjAAPRq6223pk1RCCXOUyiXBFA2FZL68QPrFyaDVIVbUy5ofEoPx8OhuN9tr3q6lcOtn8vAGSp4QcatC0v6ATNqa5jmWbT5I6_BWy5QTGiXxEkb4QDQzXWDKodCnwF6fUVTx9nHRZPej4K8BZw6QZ-hp1i0NSI3v3W8LGiIloLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=EVgc0B6aCZt6HB-ILC9Kz2J-tsOEbtYhQ3WSJm_XKJSh0piWJGNNAIobjR_ttNUZD-N4CGFgqJidPqTZ0d7IUiWOy5Y7l2aiFWpxpfewt7mxqFHHgk8m551b43SQAEW4Tc4p7gjHO2TYRsnzYA-RIPRXRN9GW90DVYqIp2Wl0L_Jl7SM7VbyMWaRNolg3_xSrWARSR7q-zz3heX8vRPjXLAHpu4haA7umEFPDy5gjuynDrSCPIG5-PFehB8-vdnRt3nG2mjwnmPMiUfmjj6I-bKubl7cJz7hKomOxXOVWThhbblL01pz38ngpyUB_R1YiVDG58OK1_SWRU1xl5-urg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=EVgc0B6aCZt6HB-ILC9Kz2J-tsOEbtYhQ3WSJm_XKJSh0piWJGNNAIobjR_ttNUZD-N4CGFgqJidPqTZ0d7IUiWOy5Y7l2aiFWpxpfewt7mxqFHHgk8m551b43SQAEW4Tc4p7gjHO2TYRsnzYA-RIPRXRN9GW90DVYqIp2Wl0L_Jl7SM7VbyMWaRNolg3_xSrWARSR7q-zz3heX8vRPjXLAHpu4haA7umEFPDy5gjuynDrSCPIG5-PFehB8-vdnRt3nG2mjwnmPMiUfmjj6I-bKubl7cJz7hKomOxXOVWThhbblL01pz38ngpyUB_R1YiVDG58OK1_SWRU1xl5-urg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68160" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68159">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7HllFOuXJz3vhIofSklowBpOJ_k6BzVpMEvPGBx65-9YhTTVf-rw6KExSOMllk-6zoOmlNMdoh4w7EQ17mK7NKeOsqrwUakid9W8VjAdE2-yFIybENNK70sz1LI6xHfZ20hZtUvTFCBMqwn3Flrc3nWm8IynlqOC9S1w6ttFWreqgnkjYHt15QSnw0LYz26qAjtIrGoHTWysqGl63Mf25_YoexByM5TgkZ3S61CqI2ck6ul0WQI30fz8f1C5OVePx4db_k4EJwKtOHpCDVQPn86wZXuIf8BlvJXs_549MHnU-5WXg2tHybeZkdZaWcMxlozco30cDTDoJZ62XKEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68159" target="_blank">📅 13:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68158">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntCR8Br0TPR7QvKXcyliDRQFBDyQ5ZRHUFS2iStIPa5Ky3je9eBd6loZ3zqp9fV6hd7lyAG1O5255CY_5gJhXaH-izvi0GEsR3svPLIHZWNdfdP-HWh3cQUzomtrzlG2GT06gGPWgUVZCKToDWFYToSaHuH8UrUx0tsJRr7N_4oeBpT1N_xTd_veHXQ17FCDGe-waPnhwfFe4le1gorNQ5S7ycB45950YRcggXRav74xRzYnCJ-ufTV6mMkzKQdaBtnc4PMOh61v4dQbE_m_67bW14oaN-8e5UGL2uKlKoN86JaMaiaNMIVeYFWKJhXv9HmXfyzqlEx6rvTdEDKDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرِ داریوش فرضیایی (عمو پورنگ)، بعد از تحمل یه دوره بیماری، تو سن 90 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68158" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
