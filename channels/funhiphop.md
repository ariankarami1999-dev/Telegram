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
<img src="https://cdn4.telesco.pe/file/Oj-V3Vw093Xhedu_DoRhJiMUvwfyU4MBVosb-SKMo31GDoyR2RbtnM-912mrVPjcPeEr66LHTXRhEKDVq-UfWT5udfmyKdXeQCnz7IPor_meKyL8PnSNQOAbg9EDjGuEx8T2Q_vyWTHap4hUexbNKMc70atocHz-Sp7Q3GbLoBg9J6ShnGcRyfG-0CMsMWY80GnXnntqqfZYYhQbsTT2etbeWIsu7Et0VlFGUqG02D56SL6Extd88L6W0oWcv25HushI5C1tD8aa_5sKdqwMcK_AaS9afgrYXuXGyP088JguI7Nbcm8saOetyarp0WsBbY_9ak92OvdrfshRJgzarg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 156K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 14:55:14</div>
<hr>

<div class="tg-post" id="msg-75430">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">نیویورک تایمز: هدف اولیه جنگ، به قدرت رسوندن محمود احمدی نژاد به عنوان رهبر ایران بود/در اوایل جنگ خانه احمدی نژاد مورد اصابت قرار گرفت تا وی از حصر خانگی ازاد شده و کودتا کند.  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/funhiphop/75430" target="_blank">📅 14:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75428">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بیانات-رهبر.pdf</div>
  <div class="tg-doc-extra">115.2 KB</div>
</div>
<a href="https://t.me/funhiphop/75428" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تا ساعتی دیگر پیام متنی و pdf شده رهبر به‌مناسبت دومین سالگرد شهادت شهید رئیسی منتشر خواهد شد.  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/funhiphop/75428" target="_blank">📅 14:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75426">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgAcG-rgYB7H8zAGimXuKXQdrR2CRj0kXVIn0m-IH5LI88ohtQeifvcyaWVPDN68uFnZS9tcsP1uiMFXc608SMDAAn_Vt2CYS5IHnG3jJfIswgi6rPJGYQcONenMrF3EhHVXLagQNsVTc7I8tTvvTittMnf2o0KrEy39FPtkvTIxkTgXt44hAcrLCcwx2fKWeINl1XaMZSTYpGB9CQx2eA2j4amsAcfrHf2QdpD2NumC4G73Gce0jMbWCiNtxoESOqN-WyTMrDQG3eEop0ubPFvmnKspCrMByBiZ7ZWsKaoVo3UmijIV9AZafw13icz36979w_nDjLgKzrbxm05JlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf67fa05f.mp4?token=dhuHIy8mKtgWu0outsl_CsWEBnd90zgXtF5D0FaZlSIG-AFswNS5SYZ9h1UWTZjRHSAE22gvTK7-u4Xuh1PmxkQNJIBIqtTSNtFm76ft-xgR5RXPPpggJdufrtAl6QDB45IvPhw0NvxpcDKx82CH0SG9Zwa8mVbmLP4_8-Nv-B6Tcl-ehtDNTDvK16MowrgRiGLIL2oeeWIDaeToW80CQHmJP4Rwh1qi5UIp6fdZ372xbNxQVRKCs3MtWJBSRVcjqwBGxQ6eG9_zYb-ZDeO__a_CEbB22V6UM6bq6uuhaHOGZI71JotVVNp8mOquKmMDhz5yUch1McMq_XWZ2qi9wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf67fa05f.mp4?token=dhuHIy8mKtgWu0outsl_CsWEBnd90zgXtF5D0FaZlSIG-AFswNS5SYZ9h1UWTZjRHSAE22gvTK7-u4Xuh1PmxkQNJIBIqtTSNtFm76ft-xgR5RXPPpggJdufrtAl6QDB45IvPhw0NvxpcDKx82CH0SG9Zwa8mVbmLP4_8-Nv-B6Tcl-ehtDNTDvK16MowrgRiGLIL2oeeWIDaeToW80CQHmJP4Rwh1qi5UIp6fdZ372xbNxQVRKCs3MtWJBSRVcjqwBGxQ6eG9_zYb-ZDeO__a_CEbB22V6UM6bq6uuhaHOGZI71JotVVNp8mOquKmMDhz5yUch1McMq_XWZ2qi9wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانر مک‌گرگور دوباره به UFC برگشته و تو اولین بازیش هم قراره 11 جولای مقابل مکس هالووی قرار بگیره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/funhiphop/75426" target="_blank">📅 14:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75425">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی:…</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/funhiphop/75425" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75424">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOskVX_tl8QqgQ3bqkMfyRXGQ2dg0cWzWK5KWvKu9XQe-5u6Na9vijdw8Km3KLA0MamvT4xzVQNneH52sX6PoxGN5LOTsWxIxRmmydiFYnG_V62vKgnPmMSgwLwkn-q2zZP0G5haAZwlBNyOHVP2_5lESUg6_Lcqa5QHQAwrZ2zpr5XQYScbtWIfvl1vu5jFUXWS2JkXrfdVh8RamDZYLOvAvLmBShO8OGj0MvJeSmCgK7wGJUiP0zEDBFMVvqXsYn6XqDIfZ8fzPv6BZOE9FQrjUZhJ_dQpOV0g1_c0YChzjumSkbSD-Nv--LpsPIYh9Qc2-FE5heaE3n3ZTA5Jgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
اکنون روز ۸۲ام
#Iran
در خاموشی دیجیتال است و پس از ۱۹۴۴ ساعت، کشور هنوز تا حد زیادی از اینترنت جهانی قطع است.
در دورانی که قطع ارتباط حتی برای چند دقیقه بحران محسوب می‌شود، ایران همچنان رکوردها را می‌شکند، معیشت‌ها را نابود می‌کند و حقوق را تضعیف می‌کند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/funhiphop/75424" target="_blank">📅 13:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75423">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رشید مظاهری قصد داشته است با تغییر چهره و پرداخت رشوه به ماموران مرزبانی از مرزهای غربی به‌صورت غیرقانونی از کشور خارج شود که در هنگام خروج‌‌ بازداشت می‌شود./ به همین دلیل هست که در زندان مرکزی ارومیه به سر میبرد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/funhiphop/75423" target="_blank">📅 13:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75422">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تا ساعتی دیگر پیام
متنی
و pdf شده
رهبر به‌مناسبت دومین سالگرد شهادت شهید رئیسی منتشر خواهد شد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/funhiphop/75422" target="_blank">📅 13:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75421">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزیر کشور دوست و همسایه پاکستان مجددا برای گفتگو با مقامات ایرانی عازم تهران شد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/funhiphop/75421" target="_blank">📅 12:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75420">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">صرافی ایرانی اکسکوینو مردم و اسکم کرد. قوه قضاییه داره دفتر های این صرافی و پلمپ میکنه.  البته نا نگفته نمونه که مدارک اسکم این صرافی از چهار سال پیش توسط فعالان رسانه ای اراعه شده بود ولی کسی اهمیت نمیداد و بالاخره این اهمیت در این روز ها شکل گرفت.  @FunHipHop…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/funhiphop/75420" target="_blank">📅 12:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75418">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/funhiphop/75418" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75417">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/funhiphop/75417" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75416">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gnq97tbhGZPA3FeIH3juRLz45UrvfwxweaDPdwt4JetlbFCXeqmSATP-Fu5gHND17rmEWiQ5oUZaR2SbxBlP1wWCQGQAdlR3KA4Ly7WAvRZXvbZPhXnI9SeSLg1tPBvPx4xQCkV8abZ1FnaRzpxH4InSKy5Wc8_VgyEQFT3avdrorIZq_DP8OxgAxsk5NX4CdmrEhEHCUhJ5-iQT6CgpxUbavwMRRWck81MIakANSkPZBAr8E8CqFIQzXIsK-0wdpnLUx1iLlcUfMIISnww3jgkUyM5dSBE-uPIP4xFUHQr892pXHNyOOmwEviCLPr0COl7dUp5mu-s7y3AyOf2NCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز:
هدف اولیه جنگ، به قدرت رسوندن محمود احمدی نژاد به عنوان رهبر ایران بود/در اوایل جنگ خانه احمدی نژاد مورد اصابت قرار گرفت تا وی از حصر خانگی ازاد شده و کودتا کند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/funhiphop/75416" target="_blank">📅 12:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75415">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k83W9hvQEX-zeM2LyFOfOXSoqAqeYyffj1mLeGidxkDsF4e4AMHHdV4NcleWC5-to8l_SS8cZHZHpsKUMFbndJs7u25QSbjZsh69RTXRS-2F-NT-AxEJiWROmBlIJWc5wgdRzUJqheF53Fedm1_JMsCrQUYGKTQKHA-JRKvyn1AWQL_iKvULp4bjAfBzgsW2EGn3Tp9dHp1lTekxvkcWKib96w4PExevea6zThASN_oQPH5bjDlaRLdYKB3W5BY3nDkG1Y133SsYdqh_2IhbhzhNy0te_rSC2tbtIE5bz2GjuTOkcA6khSGLD6P6SOU60kBA9GgTIdBvHJbekNSqPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسری وصلی های جزئی به اینترنت داشتیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/funhiphop/75415" target="_blank">📅 11:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75414">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtLL6db6DR1Sb7X5gxH1cHxevvqkLYdpSETNQN6Pxzs1nz3pqTwDtj3pNP6vcZaMwFGDXMbclmmXgNAmpJwDGoemB7OdZDmCUbpfm7nJjmnuRSRcB1_jg0vei2DAS6WX7d7rx1SY_ygn7iM5pyQtgWtirP_IV4aL88at5LKRGrjvytO52dblWyNc-QmDgch0_D02RaCr_hi6JzOFnST7vpGAwEoZjq9KwovtrONVwNXwZ0kXasG2p5G6NVEJ7mnzyW-1M82DVoXx4BGsh4O3iyOgGjKk48vxwauU9Ai4YQN_Y4vXqZLbqFpki1yUbIOwqu1g_Y_iJ0a6weQpmrWaBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Velora VPN | تجربه اینترنت بدون محدودیت
گیگی فقط و فقط 180 T به مدت محدود
‼️
⚡
اتصال پایدار و سرعت واقعی
🎮
مناسب بازی و پینگ پایین
📺
بدون قطعی برای یوتیوب، اینستا و استریم
🛡
سرورهای اختصاصی V2Ray
✅
تست رایگان قبل خرید
✅
پشتیبانی سریع و دائمی
📦
پلن‌های اقتصادی: 5GB | 950T
10GB | 1800T
20GB | 3500T
50GB | 7500T
100GB | 13,000T
📩
خرید و پشتیبانی:
@VeloraSupports</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/funhiphop/75414" target="_blank">📅 11:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75413">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سپاه:  اگر بازم بهمون حمله کنید اینبار جنگ رو از حالت منطقه‌ای به حالت فرا منطقه‌ای می‌رسونیم.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/funhiphop/75413" target="_blank">📅 11:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75412">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سپاه:
اگر بازم بهمون حمله کنید اینبار جنگ رو از حالت منطقه‌ای به حالت فرا منطقه‌ای می‌رسونیم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/funhiphop/75412" target="_blank">📅 11:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75411">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">حمله بعدی امریکا کوتاه هست و میان یه لایه دیگ رو حذف میکنن و دوباره مذاکره میکنن و فشار میارن که تسلیم بشن.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/funhiphop/75411" target="_blank">📅 10:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75410">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGcU0wFkfk45qVHU0pOSPtT1js1aREqBJeJDPV5YD1sosgsy2tk6R4WqHDP6hHgMD8W9pw869nCKGiKL0d7gA4gDmpY0trlQz-9E-YCTnfLKHV1dNhIYPbu6-qRbLy9rNCj04xd2ceKMyKc89sgt02VMVzQDi6YHq92Vfqo2CLNU_Gv1HoqLjT13m4EgfgVTdq6WBlIKk9Z0Dl3xF8PA4sp0o_wT84qwSr5_XFdQx7gVigkagZjLsDvtMEoe7hIfbGkchVBh4wpEK-dZ4oY6a_WevDl2fvaSoB_GXKnew0uy8MB8qgF03Bd9shJA2KO4aXpaLr26nkJwY2WCCsd6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای از ۱۸ مه نشان می‌دهد که ایران چهار ورودی از پنج ورودی تأسیسات موشکی زیرزمینی آبیک در استان قزوین را پاکسازی کرده است.
پنجمین ورودی تا حدی پاکسازی شده است.
این سایت در جریان حملات هوایی آمریکا و اسرائیل برای به دام انداختن موشک‌ها در داخل، عمداً مورد حمله قرار گرفت.
ارزیابی‌های گسترده‌تر اطلاعاتی آمریکا نشان می‌دهد که ایران اکنون دسترسی به حدود ۹۰ درصد از شبکه موشکی زیرزمینی خود را بازیابی کرده است.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/75410" target="_blank">📅 10:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75408">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGwy5gcFEh963Asyqxci_bZeh48a9C8k-8jGh_CAej8igzcind3KmNkI9EWNPoBXxaI4QAOF5YIskHcbnAAWtvxdjDa_LRQ_8vCU6GyJ0FrVJocs91Zl4nhx8LH1g9nHJ_O7yvn_prG4ho5ho1YJ6Vn3dcN60UrpGDXoIXbv6tLLZVFXFfBiei-TfSUOv9RYgfzGonk1rGk-wOcEW3rW-kUbV6qsnLsnEiOjTYsGugB25svB21k6bt-W_MwnZF13k5TNwZu9uFZ5qvYHFA50TMWJ6Mnf3d8djkyZiFH1S2dxDu-mxMUgzTJfi0LmnLffP8h3tfIKS9PVjag1roJWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A7NNK9PIBm8vI3yJdEjuGaUuGXVqch7PLkWffmR07AifcXdhIZAo0KSUhvLjsdElSjB8LjARA7keCdxCOj53e1bzhLRwriLBJqum_Stgw4vbr3LSMXVySqKL8zCofjyMJEYT6zZzkjx9Wprtd1WLOI2Gi7I5Np4tr_tGqW3VCVe2hDlLuUNgxnyheueK7n0bxKWhKW5ZGANJOt08Sfe6aZw4jxzEXAK2imaSDfYfRwbyEJTVK8RIK031asSWp9H8IjsAK-G6CpkgX8_Tbpg9gfL6yHmCAmP5Rs2zzANsP996PXy-FJyrBh_Lz5SH7LICd76JtonQi07vf1Os8AkqUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به مناسبت قهرمانی آرسنال، همچنین یادی میکنیم از جاویدنامان امیرحسین الوند و علیرضا صیدی
❤️
@FunHipHop
l Farid</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/funhiphop/75408" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75405">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شمال یجوری داره بارون میاد که شبیه افسانه ها شده
سال های پیش اصلا چنین بارونایی نمیومد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/funhiphop/75405" target="_blank">📅 08:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75404">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پوتین رسید چین
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/funhiphop/75404" target="_blank">📅 08:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75403">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrlkaYGZjFdJqbmDjs3lD4TcOt2eG5LwWYmcSNvk976wngnCs83PFo-9X7d65vOChq3YbsfNh3pqSXKIDKYfgk-zpVWOANxg-hapUaqpu3aFxHDQfw-5yexg-sR4A6eIxj4GVjRCS2CThNL_BW8HF2FFrcCzTtTeteGeYdpVQgmJoUdGGHVyh7bJs8-fnbpmLY9mV9XlumiTcCitKuo_Mvt3WqtTtKPkvh7gEBTBa-2lXB6YfpKCYeTx_XyIXCnimk4UTyhaVqUONiyBFkhWofnuv_ZbrZRBLDzQGFYbN92-4PeASap2z17PSi6WCB6hJp0R4abzSxJ_hOydvcljPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی ایرانی اکسکوینو
مردم و اسکم کرد
.
قوه قضاییه
داره دفتر های این صرافی و
پلمپ
میکنه.
البته نا نگفته نمونه که مدارک اسکم این صرافی از چهار سال پیش توسط فعالان رسانه ای اراعه شده بود ولی کسی اهمیت نمیداد و بالاخره این اهمیت در این روز ها شکل گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/funhiphop/75403" target="_blank">📅 06:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75401">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نیویورک تایمز کاملا از حیطه کنترل عقل خارج شده:
پیش از آغاز جنگ با ایران، آمریکا و اسرائیل نقشه‌ای برای نصب
محمود احمدی‌نژاد
، رئیس‌جمهور سابق ایران، به عنوان رهبر ایران طراحی کردند.
این نقشه زمانی به مشکل خورد که
احمدی‌نژاد
در روز اول جنگ در حمله‌ای اسرائیلی به خانه‌اش زخمی شد.
از آن زمان تاکنون به صورت عمومی دیده نشده و محل فعلی او نامعلوم است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/funhiphop/75401" target="_blank">📅 03:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75400">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آکسیوس:
برخلاف ادعاهای ترامپ که می‌گوید یک ساعت تا صدور دستور حمله فاصله داشته، مقامات ارشد می‌گویند ترامپ اصلا تصمیمی برای حمله نگرفته بوده است!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/funhiphop/75400" target="_blank">📅 03:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75399">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کانال ۱۲ رژیم صهیونیستی جنایتکار بد:
ترامپ در ۲۴ ساعت گذشته هم در گفت‌وگوهای عمومی و هم خصوصی موضع تند درمورد ایران داشته است.
او در جلسه‌ای با برخی از نزدیکان حامی حمله گفته که هنوز گزینه حمله را کنار نگذاشته و این احتمال وجود دارد که انجام شود.
در مورد زمان‌بندی، حتی در گفت‌وگوهای خصوصی نیز ترامپ یک جدول زمانی «مبهم» ارائه داده که بین یک تا چهار روز متغیر است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/funhiphop/75399" target="_blank">📅 02:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75398">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پس از ۷ تلاش ناموفق، بالاخره با عقب نشینی برخی جمهوری خواهان، دموکرات‌ها موفق شدند و سنای آمریکا طرحی را تصویب کرد که مصوبه کنگره را برای ادامه حملات نظامی به ایران الزامی می‌کند.
سنا با رأی ۵۰ به ۴۷، اکنون به طور رسمی «قطعنامه اختیارات جنگ در ایران» را پیش برد.
این رأی فقط گامی اولیه در سنا محسوب می‌شود. و حتی اگر هر دو مجلس کنگره این قطعنامه را تصویب کنند، انتظار می‌رود که ترامپ آن را وتو کند.
اما دموکرات‌ها می‌گویند این اقدام حائز اهمیت خواهد بود و می‌تواند طرز فکر رئیس‌جمهور را در جنگ تغییر دهد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/funhiphop/75398" target="_blank">📅 01:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75397">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAmTVdQGphnnaGdScDhbBqvQ_VikEwAfqTxP0qhMwCnb_SLZIl9a70_48sgU8oxPqxFllpsEwTz14lA7IXbnTxZxgVGyP6UdOWqKIzXEqQBCcEwnJ4AvxrkKKD-kFy4Dl2NNlmXMDgNm2lzH-pbUrDl25XFGpBOZaPINbUtVGTk3P2hFCVaoClI4hRBdsXHSYDU2xL-A-XtLOKoR6fzYlqEtak0zEvP_elGAUSDGG95F9omhefdPq9fm2xsvHKIYtb_drsmOitmZcWW4kvkh937WDJ1JHk590yLO7tLUs1_I-4-ETtAOnCeQTiwIXuFu2Quq-sFbmiZ2lHL-QhB_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک تایمز:
فیفا قصد دارد بار دیگر ورود پرچم شیر و خورشید و پوشاک مرتبط با آن را به استادیوم‌های جام جهانی در مسابقات ۲۰۲۶ ممنوع کند.
این پرچم همچنین در جام جهانی قطر ۲۰۲۲ محدود شده بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/funhiphop/75397" target="_blank">📅 01:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75396">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlIan87fFvD_DvNgqzLON99XC1T5Hxi34ZDlFshGxWtZBZMvcC2ubXong-4aCSg9zPTLdtuZQrrdebE0eG-y6-10OAPCjy0NJglLTzPJvSf262Vg3jtwwqm-TnrryDMu2CRdNHXTozsh2z0M2cjcog6qfYjP3clAwGuNC20UALRjj5oXxwv1l49AacWChU4q8onttsoWDi_Mlh_Slo7ZjqNeLO5oFduQPZGMqyaJwFdRz3HDhEMur9sVeQuHdUyhYUejoGX0WDJgZm3UgB4n9V-yOn9ID3N_LIB3PJAWOeS-HOdMQyMJSUbhiz5rqwRuPeKUYAsquSNX1NAK7B_sxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور عراقچی:
ماه‌ها پس از آغاز جنگ علیه ایران، کنگره آمریکا به نابودی ده‌ها فروند هواپیما به ارزش میلیاردها دلار اذعان کرد.
اکنون به‌طور رسمی تأیید شده است که نیروهای مسلح قدرتمند ما نخستین نیرویی در جهان بودند که جنگنده پیشرفته و پرآوازه F-35 را سرنگون کردند. (به اجدادم قسم اون f15-E بود)
با درس‌هایی که آموخته‌ایم و دانشی که به‌دست آورده‌ایم، مطمئن باشید بازگشت به میدان جنگ با شگفتی‌های بسیار بیشتری همراه خواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/funhiphop/75396" target="_blank">📅 00:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75395">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yp33TtOg-kO8d8JoaDS-LToGZ8b5UsbHamSdKiX3-4ITeKjuum1nExq7rqLj99UcLx5Ibolz3_4uSi8IBKmSjrRX1THo6SqqYwluFcHxoSxNgoRT3aoQ45lRcHDI4gCRagcNXkDWQ6qH-cyZzqoWkb7Rs-Mwx3W6ZJsJ-oLt375HSyuYbGLiszL6nUJwk2MrEoDaVBTIt2XGe0qi2lziyOpC73yf3LqCPTtX9kllit-MjMuJPNQyWukBnIJhLeYJpUIW1sntq5WVDC-E6tFqYd8C0J9tgxSIdbsYQ8xsNgxkrHHQrjSVZw4RsVIC1PeVQGmmKejzH0rfxbP2KPZvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مناسبت قهرمانی آرسنال در لیگ برتر، یادی کنیم از جاویدنام عارف جعفرزاده
❤️
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/funhiphop/75395" target="_blank">📅 00:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75394">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آرسنال پس از ۲۲ سال قهرمان لیگ برتر انگلستان شد
🏆
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/funhiphop/75394" target="_blank">📅 23:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75393">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دیگه به هادی چوپان نمیشه لقب آرسنال داد باید به همون مادرجنده کفایت کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/funhiphop/75393" target="_blank">📅 23:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75391">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حکم پژمان جمشیدی صادر شد و به ۹۹ ضربه شلاق تعزیری محکوم شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/funhiphop/75391" target="_blank">📅 23:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75390">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d909bc992.mp4?token=cG-9-gV2MdTZSNvdohwC5aAYwoQ-Icnp1iN55RCw8jwlVCgwfKWeV3Va5RgrfSkQ8D9GLt1iuYbO5YyyIhOIdH_YGa0LszPWPi--KpwstrQvH4e7Ad2T5xXwNgUjCjZRZys7ptagP9prDtysWvOdhSLQvrAbaVe8tJ1HQh0L41E4jvXSf-QxGua-y-KT_FWBdce-URp2USVKaLy9r8O5XmlBchWgHZXWCcL3jdFsXLqv8tIQMybB5O1VrfIMzuOhvAIYWp0SWtBXHP7WKQKbv9zJq704ALyEKdkXgTp3fYCyggg3BhNk7W0-6042-rFcE_cM0VmQueEOC83fXmytfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d909bc992.mp4?token=cG-9-gV2MdTZSNvdohwC5aAYwoQ-Icnp1iN55RCw8jwlVCgwfKWeV3Va5RgrfSkQ8D9GLt1iuYbO5YyyIhOIdH_YGa0LszPWPi--KpwstrQvH4e7Ad2T5xXwNgUjCjZRZys7ptagP9prDtysWvOdhSLQvrAbaVe8tJ1HQh0L41E4jvXSf-QxGua-y-KT_FWBdce-URp2USVKaLy9r8O5XmlBchWgHZXWCcL3jdFsXLqv8tIQMybB5O1VrfIMzuOhvAIYWp0SWtBXHP7WKQKbv9zJq704ALyEKdkXgTp3fYCyggg3BhNk7W0-6042-rFcE_cM0VmQueEOC83fXmytfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده سنتکام به کنگره:  مدرسه میناب در سایت فعال موشکی قرار داشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/funhiphop/75390" target="_blank">📅 23:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75389">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فرمانده سنتکام به کنگره:  مدرسه میناب در سایت فعال موشکی قرار داشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/75389" target="_blank">📅 23:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75388">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🛍
تخفیف ویژه تا پایان امشب
🛍
دوباره تخفیفمون رو تمدید کردیم
😍
هر گیگ فقط 149 هزار تومن
‼️
✅
پینگ عالی و پایدار
✅
بدون ضریب و محدودیت کاربر
✅
لینک ساب برای مدیریت حجم
✅
پشتیبانی ۲۴ ساعته روی همه سرورها   200 گیگ شارژ شد
⭐️
تا تموم نشده به ادمین پیام بده…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/75388" target="_blank">📅 23:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75387">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🛍
تخفیف ویژه تا پایان امشب
🛍
دوباره تخفیفمون رو تمدید کردیم
😍
هر گیگ فقط 149 هزار تومن
‼️
✅
پینگ عالی و پایدار
✅
بدون ضریب و محدودیت کاربر
✅
لینک ساب برای مدیریت حجم
✅
پشتیبانی ۲۴ ساعته روی همه سرورها
200 گیگ شارژ شد
⭐️
تا تموم نشده به ادمین پیام بده
🔗
کانال مشتریان
🔗
خرید</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/75387" target="_blank">📅 23:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75385">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">من سیتی گل خورد
قهرمانی آرسنال از همیشه نزدیک تره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/funhiphop/75385" target="_blank">📅 22:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75382">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceda97bf16.mp4?token=fmPaLy5E9AF4IzpaY8Zmd5NRw5bcKZgPAEsVck8wl6ZQpYl0zNqnadSDRJ7nENR5dXVYSpSRm3jhQqBLda1rdo_MVM9eqXjrnnUg-ZE3LwX0QwuoI5JLPUMDKAWjTF-ivXCNfYCx2Saa9kX6CjmkFbtrCJX4FgtcxQdEY4YwKmPzw5FHK6yKlYd4DOR3AXObe-6ts-7Jfxe8YgI4CY-SGfYjQ1ObJasb8TG69PS2OKs2MJH2gozTHgywJF5X5vzgP_n-fJ0fFbwvAY87VOjm4GL3MKW7NFCj8rOF8Hf0Chx2TZTwjJtu0KdKrEGvBHtRD8t3PupPjFvC3Zxfh1uEGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceda97bf16.mp4?token=fmPaLy5E9AF4IzpaY8Zmd5NRw5bcKZgPAEsVck8wl6ZQpYl0zNqnadSDRJ7nENR5dXVYSpSRm3jhQqBLda1rdo_MVM9eqXjrnnUg-ZE3LwX0QwuoI5JLPUMDKAWjTF-ivXCNfYCx2Saa9kX6CjmkFbtrCJX4FgtcxQdEY4YwKmPzw5FHK6yKlYd4DOR3AXObe-6ts-7Jfxe8YgI4CY-SGfYjQ1ObJasb8TG69PS2OKs2MJH2gozTHgywJF5X5vzgP_n-fJ0fFbwvAY87VOjm4GL3MKW7NFCj8rOF8Hf0Chx2TZTwjJtu0KdKrEGvBHtRD8t3PupPjFvC3Zxfh1uEGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جِی‌دی ونس :
ایران کشوری بسیار پیچیده است. کشوری است که من تظاهر نمی‌کنم آن را بفهمم...
این یک تمدن بزرگ و پرافتخار است.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75382" target="_blank">📅 22:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75381">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9aacc343d.mp4?token=hCH86vyERau5k__advfp-rrFXUsfnrykJCJhptBzGY148UppKKp75_PqyXXPJnGc8jQv6FPzysyJeJeXDgy775fC-V19ogwA2_6qRIkTDJDvKu0Y45-xq9Opn6P8Z0zcZkqDNb5BYIxv0CjeqACE1W92FAGcIsxxeHl1uFgz3Yjz4_uBxQ6Z9saVT7aYGKuAmfUKhUWLIjxNEbx1tsjjF2wQJ4jDfYW9h_7sL3aAUFSEyVXGht9E9spw1OjUK1mAgnlwOIgyC505a54KjSUJjeowb2rRb9NtC2NifmeqB33YUyCxXqMK-VyyI-PJxC8If2tkJ2U8JOaqYGjVfpmVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9aacc343d.mp4?token=hCH86vyERau5k__advfp-rrFXUsfnrykJCJhptBzGY148UppKKp75_PqyXXPJnGc8jQv6FPzysyJeJeXDgy775fC-V19ogwA2_6qRIkTDJDvKu0Y45-xq9Opn6P8Z0zcZkqDNb5BYIxv0CjeqACE1W92FAGcIsxxeHl1uFgz3Yjz4_uBxQ6Z9saVT7aYGKuAmfUKhUWLIjxNEbx1tsjjF2wQJ4jDfYW9h_7sL3aAUFSEyVXGht9E9spw1OjUK1mAgnlwOIgyC505a54KjSUJjeowb2rRb9NtC2NifmeqB33YUyCxXqMK-VyyI-PJxC8If2tkJ2U8JOaqYGjVfpmVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنان قصار استاد جی‌دی ونس درمورد ایران:
تا هنگامی که ندانید، هرگز نمی‌دانید.
تنها کار خوبی که ما می‌توانیم برای ایران انجام دهیم، مذاکره با حسن نیت است...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/funhiphop/75381" target="_blank">📅 22:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75380">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امشب به احتمال خیلی زیاد آرسنال قهرمان لیگ برتر میشه
پیشاپیش به طرفداران این تیم تبریک میگم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/funhiphop/75380" target="_blank">📅 21:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75379">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مقام امنیتی ایالات متحده به کان نیوز:  تدارکات مشترک ایالات متحده و اسرائیل برای از سرگیری عملیات نظامی علیه ایران تکمیل شده است، انتظار میر‌ود ترامپ به زودی تصمیم بگیرد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/funhiphop/75379" target="_blank">📅 21:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75377">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssxKiA21NvbCOtEGhpM2eTEz3U-_g3-kAha11AYBnUB4cgEH_BOXH0oveee5DmhxxsCKiUBwc2WB13F76lEc7NImOVLvTREiPegROvoUkLulkMsp6p1qedDZ5B2Bx9E1nSZKU7nN7yl0wFgPumB8BZOQte-bS0Ax0RNxfOv1cRwu7Vh1dDoByvAD-jCMKgwAAmdLTCnznjICmtyt02JJ2Gg4tT_jl0b9Akyru8cJiaQAlbz3bL3ndM16_X59c2e_zY1HNlr2vXzVbgeUA9X2Sbqw_Jij3bvA8SvclAXZFdO1sK9w8FoEm_08jsby7JgZ97qDhS-Xp10x3bXAzsygGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گیگی ۲۰۰ پول وی پی ان میدم که برم اینستا از هر سه تا ریلز دوتاش صدای آنچلوتی باشه که میگه نیمار جونیور؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/funhiphop/75377" target="_blank">📅 21:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75376">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!   دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
( فقط 300 گیگابایت موجوده! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/75376" target="_blank">📅 21:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75375">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مقام امنیتی ایالات متحده به کان نیوز:
تدارکات مشترک ایالات متحده و اسرائیل برای از سرگیری عملیات نظامی علیه ایران تکمیل شده است، انتظار میر‌ود ترامپ به زودی تصمیم بگیرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/funhiphop/75375" target="_blank">📅 21:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75374">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbEWOGJgvKt229a1lZKWbJ3ZYCTB9tEjmZPJ_KDiLJ7zuxL4wV4x5jrj4tqPHpS-IT53CKkgKF5IMFPF8s7PTGPyhWeZYMJQ4oX2424WCLhiJrI_lZFaj3DQfEWkC7-V8KpjMhCqy68zhumepUur5uKh7oB4L3wi1szJS67qB-G1z7Z3sYDpfRsowl96rKfSPtptzaS5nWTMxAxN-d5M3qgSSUFBKkLzCfqxhlVJjrf6QItEllSscCBw5TG8o_tcQiXPQFV_169PQcSFMICsG5RWSXocSsw9CbPnoE9gl4OLo3orohg6O01dC8b8ZSbzVZLrB1YSSx7VlL1jobMSVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و استاد جنگ هوایی و دریایی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/75374" target="_blank">📅 21:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75373">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">زن رشید مظاهری با این استوری اعلام کرد رشید مظاهری بازداشت شده و جونش در خطره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/funhiphop/75373" target="_blank">📅 20:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75371">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7tA0uz04Je9bSX6oqMFf60Vh4E5RHZ5kFAEjr_j9WV6y_1akP8OxdkB65Q8IweIQeC96P68kKFauOS01NRFlmbI2-ExygK3Ji2k6_HP7622w3i3n6rYhaSSvCSWrao9fHzy-xbQjoL5cSrKiOGmR2farizrRfuLVPpePeqO3BYZMzpES7qCXOjqwJCfKQONWVtwtRLmfM08lCZkQewfaFvTE7UziMZjejquBWUaNo94H7uqfLZzPLS-UjXGCd0fdhVWDytsZ1U1POJxwdROT3aF9H_jWCXuYLsDzI2Z55fglJmhR4pdwlaZKpJ92ynzDU5VdznLufN_QO2Oa8GQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏علیرضا نجاتی با قید وثیقه آزاد شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/75371" target="_blank">📅 20:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75370">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کانال ۱۲ اسرائیل: درحال حاضر اقداماتی برای اطمینان از اجرای یک حمله گسترده درصورت لزوم، در حال انجام است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/funhiphop/75370" target="_blank">📅 20:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75369">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فیفا: هر پرچمی جز پرچم زسمی کشورها وارد ورزشگاه بشه باهاش برخورد میکنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/75369" target="_blank">📅 20:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75368">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7FlxeKLCaOWlsAWCF6ZqQ4xKN92TJX-Bi__T0483hyfc2OCjeN5j2nIWTzi6koOk2X-NhFrX2f6b-XNhO3wRSbqvSwKCDNb1a0nGMzgLvNoWvZJzcCbRkAawQeL5j_Zu-L--tNVgj_WVVYu3Y6dWkiq3zoCZi7-PpPIhMlVM4bXaiIJan7NFh3grpPQWep45kHwlvbHehB1BrQjMDYoC61x7Q1z4Yn0H4cbHN5lJosrJb5GKRplKs1WImkhu3ISAiABszw5K-G5ggdyjfAFKJyHfxJIoNYi99pI_dE8HYvD_eG9tle32MUIOtHH4YEhdl8ix47drekgKP4puE5i9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرتون همچین غولی براش مهمه تو فینال با اسپرز بازی کنه یا تاندر کون جفتشون میزاره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/75368" target="_blank">📅 19:47 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75367">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTORNADO Ping</strong></div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 139 هزار تومان!
😈
(
فقط 300 گیگابایت موجوده!
)
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/75367" target="_blank">📅 19:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75366">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این حرفای منو جدی نگیرید همشون “ترولن” و  تیکه انداختن به حرفای کلیشه ای بعضی افراده اگه به دلتون گرفتید دیگه نگیرید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/funhiphop/75366" target="_blank">📅 19:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75365">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ:
تنگه هرمز متعلق به ایران نیست. این آب‌های بین‌المللی است — این کار برای آنها نیست.
آنها درس خود را گرفته‌اند.
اگر امروز بروم، ۲۵ سال طول می‌کشد تا بازسازی کنند. اما ما نمی‌رویم، ما این کار را درست انجام خواهیم داد...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/funhiphop/75365" target="_blank">📅 18:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75364">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ درباره ایران:
فکر می‌کنم خیلی مهم است که اورانیوم غنی شده را به دست آوریم.
شاید تاثیر روانی‌اش بر آنها بیشتر از هر چیز دیگری مهم باشد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/funhiphop/75364" target="_blank">📅 18:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75363">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ رد داده:
کشورهای خلیج در حال مذاکره با ایران هستند و
اسرائیل
هم همینطور.
دیروز تماسی دریافت کردم و به من گفتند، «آقا، می‌توانید صبر کنید؟ ما خیلی به یک توافق نزدیکیم.»
و  من به ایران مهلتی دو یا سه روزه می‌دهم، شاید تا جمعه یا شنبه. یک بازه زمانی محدود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/funhiphop/75363" target="_blank">📅 18:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75362">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ درمورد ایران:
ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم.
هنوز مطمئن نیستم ولی خیلی زود خواهیم فهمید.
من یک ساعت با آغاز حمله به ایران فاصله داشتم و اگر منصرف نمی‌شدم آن اکنون اتفاق می‌افتاد.
به هرحال قایق‌ها و کشتی‌ها بارگیری شده‌اند و ما آماده شروع هستیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/funhiphop/75362" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75361">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1vYstRPffhQqwrl7ldlmqAGnrqwzCf8mC7muEvHCeaatlLmY8iWBjjM57IYRoatg9cmEqShhM6X0ix5m-OHckqPtBsdrvwK1gThWncrEXxRjt1MvC_ZOpcM4X4FlpjdrZ8BPUWQeTnc9X5dWpj_uh1hqihyTe5AbU-7Gn5Px1H91jCusu9eJg7-3-0VOemn_vWoe8JZPMPvZigRsC3oNBsBl5VLbiq1mZQ7p0uC0E3LL8633vyShW_1k8lDdxwsPM16nD12ssA25BYhUgFwTJqohS7_zgxAzkzi8LS8G2w_43FxlMn1dhRRNDo5jZajcSdGnaUG_neB01vZ67YJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون دکتر عراقچی:
ایالات متحده می‌گوید حمله به ایران را «موقتا» متوقف کرده تا فرصت مذاکره فراهم شود؛
اما در عین حال از آمادگی خود برای انجام حمله‌ای گسترده در هر لحظه سخن می‌گوید.
این یعنی تهدید را فرصتی برای صلح می‌دانند!
ایران یکپارچه متحد است و با قاطعیت آماده مقابله با هر تجاوز نظامی است.
برای ما، تسلیم شدن هیچ معنایی ندارد؛ یا پیروز می‌شویم یا شهید می‌شویم.
و همانطور که شهید رجب بیگی گفت: ما ملتی بزرگ هستیم، بیایید نام خود را در تاریخ ثبت کنیم؛ از میان همه رنگ‌ها، قرمز را انتخاب کردیم، و از میان همه انواع مرگ، شهادت را برگزیدیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/funhiphop/75361" target="_blank">📅 18:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75360">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">همیشه یادتون باشه که بازارهای مالی بسیار باهوش هستند و زودتر از هرکس دیگه ای (حتی خود ترامپ) اتفاقات آینده رو انعکاس میدن
دیروز بعد از صحبت ترامپ، تغییرات بازارهای مالی نه تنها نشان از سازش و مذاکره نمیده، بلکه بیشتر احتمال وقوع حمله رو تقویت میکنه
پ.ن: بورس آمریکا دوشنبه هفته آینده تعطیله و این هفته بهترین فرصت برای ترامپه که هم حمله رو انجام بده هم بازارهای مالی رو کنترل کنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/funhiphop/75360" target="_blank">📅 17:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پشمام معین میخواد واسه دعوت شدن نیمار به تیم ملی برزیل تو جام جهانی آهنگ بخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/funhiphop/75357" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX5UryCO4jA60bHNyeofMJ7btiv4RjIF4tAaeU1nk46BzfjRy3mr5Y2HOZAXhKeaavM9DhHYrGcEmQCp7P9-x9aavcT8nMlEbECRbSLPKx8__XetoAVyrB19gESv3B1dofnMRpJIIa5CotrEoBRqBF4fVQ09q64yd7fNJoGQDALF_k1Fqqaq91CM5-EsO4jWfARGi0V2A9OkzNclLUzuwwS65CtaaHI5Re6L4-Sxa2xea685vtyR4CBq3gbT__stZIiibsBjkrdUM42JB86fplxRIb5wgqzrn8SFj2kWp5eJUOlt12DKHXRZL5-wO0tdfpwaip0t09C3I8TaLyoJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی ناموسا تاکتیک های ناشناختتو برای خودت نگه دار به اینا آموزش نده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/75356" target="_blank">📅 16:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d9062d93.mp4?token=Lz8i3sFJ_hCYrLxEHibwLUt2EkP0iUuw_D9t_H6WMDMHDzGHmLTxIRncqohFrMZVv8dKVdDL9wF9EZi8Kkd3_6OX6HmU-mNR_Mxj1KUtqW_gPGLZSCFbIGl5Wmj-ABlNX9xwBdZ_t4rojuPq7eKYpQC144mlKPfPOE1gve0E8rxkrWbUjUzuymhjHgkVCMZgfpLB9LByV3ojq-hvSrqGbYe6Ou0wZdeztt1oLV0N1iUkl0jqfiD66HeeVQPcv-EPGKBLvV40XhFgqlBLwZD3ES8FLismDv2dPGRyxxz2KMywd-WeooNckFI6A4lPpEDr02AGrnEuKukYNHtOAVFbsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d9062d93.mp4?token=Lz8i3sFJ_hCYrLxEHibwLUt2EkP0iUuw_D9t_H6WMDMHDzGHmLTxIRncqohFrMZVv8dKVdDL9wF9EZi8Kkd3_6OX6HmU-mNR_Mxj1KUtqW_gPGLZSCFbIGl5Wmj-ABlNX9xwBdZ_t4rojuPq7eKYpQC144mlKPfPOE1gve0E8rxkrWbUjUzuymhjHgkVCMZgfpLB9LByV3ojq-hvSrqGbYe6Ou0wZdeztt1oLV0N1iUkl0jqfiD66HeeVQPcv-EPGKBLvV40XhFgqlBLwZD3ES8FLismDv2dPGRyxxz2KMywd-WeooNckFI6A4lPpEDr02AGrnEuKukYNHtOAVFbsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راستی امروز سالگرد کشته شدن ابراهیم رئیسیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/75355" target="_blank">📅 16:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📶
بهترین ارائه دهنده فیلترشکن
🤝
آیپی static (ثابت) ، مناسب ترید و وبگردی (اینستاگرام - یوتیوب و....)
🔥
| بالاترین سرعت ممکن روی تمامی اپراتور ها
✅
تعرفه سرویس ها زمان دار :
🥑
1 گیگ | 4  روزه ⇐ 290 تومان
😼
3 گیگ | 9 روزه ⇐ 850 تومان
🛍
5 گیگ | 14 روزه…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/75354" target="_blank">📅 16:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSeniorVpn</strong></div>
<div class="tg-text">📶
بهترین ارائه دهنده فیلترشکن
🤝
آیپی static (ثابت) ، مناسب ترید و وبگردی (اینستاگرام - یوتیوب و....)
🔥
| بالاترین سرعت ممکن روی تمامی اپراتور ها
✅
تعرفه سرویس ها زمان دار :
🥑
1 گیگ | 4  روزه ⇐ 290 تومان
😼
3 گیگ | 9 روزه ⇐ 850 تومان
🛍
5 گیگ | 14 روزه ⇐ 1,250 تومان
☄️
10 گیگ |  20 روزه ⇐ 2,300 تومان
🥶
20 گیگ | 24 روزه ⇐ 3,880 تومان
🚀
50 گیگ | 30 روزه ⇐ 8,770 تومان
💢
💢
تعرفه سرویس‌های بدون محدودیت :
💆‍♂️
1 گیگ ¡ کاربر نامحدود  ⇐348 تومان
💆‍♂️
3 گیگ ¡ کاربر نامحدود  ⇐ 1,000 تومان
💆‍♂️
5 گیگ به بالا ¡ کاربر نامحدود ⇐گیگی 290
💆‍♂️
10 گیگ به بالا ¡ کاربر نامحدود ⇐گیگی 250
✔️
جهت استعلام قیمت حجم بالای 100 گیگ و اوت باند ویژه فروش همکاری (1TB) به پشتیبانی پیام بدید
🙄
خرید از طریق پشتیبانی :
✅
@VpnSenior_admin
💵
پرداخت به صورت ارزی شامل تخفیف می‌شود
___
꧷
📣
@vpnsenior</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/funhiphop/75353" target="_blank">📅 16:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKRuWBgLweR2Yyd3YMOkjnr4PBuBkVaClpVfQ109RqDNpdsbS5BnkW0_kvGELxWmUl9llSYRXU14RDcI1JZXQ_UoAujGEVgmdVt7GKOieB_NGHOVOMni4PsHFhZrq4dIpns62nLt2gR3RhgV5xcNkpkZ1VKzDxbgpWl17ebKxxxT3xtdUldIBCDaSXk8I5mKhHeJE-1QPCXd6t96W4EdeaABHcPbND8fUSYgtbVgJuIBLQLGbUiXQA-uMr5w4BEVXyYI5zrDCS8pNXruGXqXzlk85g5afaAXhftS8V4sQgmeeNOhff6nx_l3cRkNUs9si4rmOjSSej8y0TFDlhUbcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید سردار آزمون و آرزوی موفقیت برای تیم ملی جمهوری اسلامی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/funhiphop/75352" target="_blank">📅 15:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ گفت که پس از درخواست رهبران کشورهای حوزه خلیج فارس برای زمان بیشتر جهت مذاکرات، حمله برنامه‌ریزی‌شده آمریکا به ایران را متوقف کرده است.
این در حالیست که چندین مقام خلیج فارس به منابع ما گفته‌اند که از هیچ طرح حمله‌ای از سمت آمریکا مطلع نبوده‌اند که بخواهند مخالفتی کنند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/funhiphop/75351" target="_blank">📅 15:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گیگی ۲۰۰ پول وی پی ان میدم که برم اینستا از هر سه تا ریلز دوتاش صدای آنچلوتی باشه که میگه نیمار جونیور؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/funhiphop/75350" target="_blank">📅 15:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سازمان عفو بین‌الملل:
تعداد اعدام‌ها تو جهان تو سال 2025 به بالاترین سطح ثبت‌شده تو 44 سال گذشته رسیده و اعدام‌های انجام شده به‌دست جمهوری اسلامی، اصلی‌ترین عامل این افزایش بوده است.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/75349" target="_blank">📅 15:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ینی اگه قطریا دیروز کونی بازی درنمیاوردن الان داشتن میزدن؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/75348" target="_blank">📅 14:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرگزاری مهر: شنیده شدن انفجارهای مهیب در قشم. ماهیت این انفجارها هنوز مشخص نیست.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/75347" target="_blank">📅 14:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرگزاری مهر:  فعالیت پدافند قشم.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/75346" target="_blank">📅 14:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سعی کنید تا حد امکان از نوبیتکس استفاده نکنید فعلا، آمریکا بدجور سیخ کرده روش هر لحظه ممکنه همچیشو فریز کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/funhiphop/75345" target="_blank">📅 14:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اهواز امروز  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/75344" target="_blank">📅 13:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75342">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-cRrQZ6j5MQszQsxCBB2Z9t_aNsKfdvM0JhDdMGm2sE40vFWaA5Lo3N9QtztcwRaaa0q8dUARgvpzFMglSwiFVklbOPI-3zkXsFmkkLZ1DS-OTj1GKQ1F13_M30UpfDxPUxb4FHwiYYgow1iRfiZp1v1LdCGevZROjw1ZXeKqwBC0gcFlH5mmS8hHmnsKDJxldSOiClJeCZqM1lz5Koj8GOcYaj5nxgTFnwwYkpUvTDeGij765qFv0QI_Oat60SUUEHqjKp-PgHuQmqu_qN7f9svOO3qWj3MsdmpEak6hOMq98R--xBvN2l0vbcIlq6PLpIq9CzbdCMhtSGwTPLnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اهواز امروز
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/funhiphop/75342" target="_blank">📅 13:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75341">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90d827a7ab.mp4?token=BddZkMR2WgnM0MGeYNZOHu-4BRo17uAb2KJwt4ZA3XZFN_w6lFxnmq_LQ6xqQ2TP9_bncPVF7BEhpxLZg5d3Fkkmkc1xX64YJgW87xVHL17LFXISzcyaud2nZ9Q3aR8xRT_24NYwrd5RUaYVq_4OQ-vcmZ4qbLcCFff1lnQ2gDplquzPZi4U0_vsC4vPgCe4eb4t0JDvaVPdhPWFwYOSD3JkN73_SQ5cKy0vznGd5Q0gATp0S1kVfF7u1sW02zNbEskBwIYn6qQPec96x-8KhB_cxRS6PYx4mFgJ6rRZ2WYXeKug-Tmbs-KvhBcECKILU-1LrtfMhtnhHGHvvCaqxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90d827a7ab.mp4?token=BddZkMR2WgnM0MGeYNZOHu-4BRo17uAb2KJwt4ZA3XZFN_w6lFxnmq_LQ6xqQ2TP9_bncPVF7BEhpxLZg5d3Fkkmkc1xX64YJgW87xVHL17LFXISzcyaud2nZ9Q3aR8xRT_24NYwrd5RUaYVq_4OQ-vcmZ4qbLcCFff1lnQ2gDplquzPZi4U0_vsC4vPgCe4eb4t0JDvaVPdhPWFwYOSD3JkN73_SQ5cKy0vznGd5Q0gATp0S1kVfF7u1sW02zNbEskBwIYn6qQPec96x-8KhB_cxRS6PYx4mFgJ6rRZ2WYXeKug-Tmbs-KvhBcECKILU-1LrtfMhtnhHGHvvCaqxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بصورت خیلی عجیبی امروز به لبنان اتک نزدن  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/funhiphop/75341" target="_blank">📅 13:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75340">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بصورت خیلی عجیبی امروز به لبنان اتک نزدن
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/75340" target="_blank">📅 13:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75339">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">He said she was Persian   میشه  پسره گفت ایرانیه یادگرفتم ممنون
❤️</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/funhiphop/75339" target="_blank">📅 13:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75338">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">Diddy:
He said she was Persian and started speakin' Farsi
پسره گفت ایرانیه و شروع کرد به فارسی حرف زدن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/75338" target="_blank">📅 13:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75337">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مدیرعامل جهاددانشگاهی
:
به دانشجوهایی که ازدواج کنند ۳۰ میلیون وام تعلق می‌گیرد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/funhiphop/75337" target="_blank">📅 13:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75336">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تسنیم:
رسانه‌های اسرائیلی اعلام کردند یک هواپیمای مقامات دولتی اسرائیل لحظاتی پیش به سمت امارات پرواز کرده است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/75336" target="_blank">📅 12:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75335">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYN1T0lo_MBHk9MSb-6bqBdrY5bmakGyLlwPrjO3MKIqgr9OkjDlRGHniZ05CLhDUdVSOXJGYTsKDyCGrEK9xzq_LIdvk53N76kfh0j2e9TJz_In-ugfQupBpxURtDrJT3dDUp7i9z8Ja60E9k5G8AhMlRoZsDJVPJitd6z2efrOZhmreaQLMDYDpw0ImVX_CwM5GUAMTQTWnsxErmpgzGUh_06lh0B21_43660oXGfDmbBndWm-ZjNuE1tzXqbGqunOXA8ysTH29euKzXYG0pLa8R3PYlBOKjzQuuFNRHSWCmd3v6ClUil2SlHisUu2a59LYmfdSzKdk3T0HlfpkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادر فکر میکند شخصیت اصلی داستان است
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/75335" target="_blank">📅 11:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75334">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یعنی ترامپ ریسک حمله قبل جام جهانی رو میکنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/funhiphop/75334" target="_blank">📅 11:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75330">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGqdktz4Qgy9_V9s6gBT9UhJr3Ffvjn4JNr59gSOebxTvjJxqof4J8zQGwso_Ea88rS8dUy1zXgvWa69KU14XVmbH9SGHGmMgJGIIwkspE5qedjNAkk_OHLn1ZyRjMuqvysXwvmexnJ1TPOYWLuBJ4Yvj6cRgg8LX9PsTM1qs7LpCX7g_waTJjq4eyWiv_zeQOoQap45hQsycL9hPaBXlp3sURnM-OmAdvOqzEgSreWUAUR1TjrNKM2EMaep2BHMFwsfhQpHrm8GZkJ3VsfoWXwXItCeSnrfEsTpX7TqLdQlP5-GFgR5SceN2mOX-AtRvx_HRYqMPQaisbaF6jughw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GlHNDwlriN84Oj1hNPzWqRccXpkPgBRN3BGbOc190QQJ883FJNkyjak-Q5w3Zl8YPhrGF5V0ttwaNhG_EgUpF8jAU4zN3k_0ILd8tAg4--vHEPSUzDHgciMSml7oIkvicA7WQM154PYCU7ud2DP0fASjJvw-yBcSsior1dwq5aYvnc0Xjh4ZIbDcA5mp1S5B7oFGx11hStJphx_kGM4MPycGTYSN75DsTpcWZJPpGf20nwpevidM3QIBZz5_tEE8B_1lYcfl7UAKpyfy7XaGDy1jc0_csyIMtzeZkWiEzAAQ6D-MkMRD4BUEl0vLZkbTi7wyAeKnT1EpqNzlEDWvHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QfU-Jsg6muJ23Ngm0rmhtpOpuDxSZFUV7B92mUiJ425MvQuWxZfkFcxhtRXgBAkf4lku7g3gN8eINr3IEF5rdR5Z8UZIdpFj5ePEYmWFlKpQ9iiAkttNr9rtlXdUG0Q1LWZhPX_aCtjgdp0fdfZDFAqIXTb2UXw7E1Wr65K_tZ-zpzHGb5yav9OKzLE6PnDVNmejAmCXPCc-EkSYTUQiePZsVMjoyvGL7g_IdhMSZ27uq4dc1xV7AadyOhVRW_IzExCWjHh2jXXnQdSStG0TxSPcEFTZhF7e9ymlZaL5lfdsSEjaqhTIFu584P9zfuVaCpLGgzp4XPExVuYtBvXS-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rEX0bv3yPOWCi916oGlDf5WteFEVFbHN21fXdDwABUANm-FP3s6Rn_FWE1HZQoL037bg_SsubO0S2FTyeZkagIYruKh3am4IRUprOjG97vmlEJ0lX--68HuRXY_ctcdqW2L8fTWMoL34qWY5H-hbg2WEgCmiWAqppj-ScjdMUvDAVkeLzGAeEm_0B5V_NhLDtNcpEhmL0ofaeSTlEKX1pMIqt74M2BqBoo0Iykq2pE6e-fk2piygQaYi6zcT_3NFyZguzui9YFw4HrBs_OtdSpOyuSOIrrw2kgrqCTalYfrXkqMShdq-Kt5xYuImBs0VCY1A6hFO3LrBryYInrat7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راک‌استار رسما اعلام کرد جی‌تی‌ای ۶، ۲۸ آبان امسال منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/75330" target="_blank">📅 11:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75329">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فرمین لوپز جام جهانی رو از دست داد بخاطر مصدومیت</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/75329" target="_blank">📅 11:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75328">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بورس ایران بلاخره باز شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/75328" target="_blank">📅 10:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75327">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHdEloshb4bsPm0_8bjOTILl4azQfKPWt4BiYIC-9yk-KrAo3NisGDGOX9alRoM0pIEgvd6divCHoTAlhvzccXuAgoIWToXgQvbbCkuAIaPZ2-flbjF0MuYvsiiuxoZe3E5WTB-1kC2k2AH94br_OmRm-lW22dA_8TCw263u-HZ-vcqo9Zz6RefGw3BdpYhMZ8SETW8H1D08WlBKESfJPSauYRyUaT-AmgksXGUHD8xpo4749zRuLEkc1ee3BbNxqN8cK9hrFMsjRiPdXvs4AKuG_HEfCZL8pfeoM1dH-EUElXKOwgZfzEOO9WCsizzFMLXXCyArbpORDNVY16Op8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ایران بلاخره باز شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/75327" target="_blank">📅 10:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75323">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس:
ما در حال کار بر روی چارچوب قانونی هستیم که توسط مجلس شورای اسلامی برای مدیریت تنگه هرمز تصویب خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/funhiphop/75323" target="_blank">📅 08:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75322">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a0f52793.mp4?token=nrskSmX5X1-X0Rl0ZCJEjnmOUHtWhKmwjj6b74z3mPpBJb3b9IEgQiPAhYlRB366yfGZk0yeKqTaIqxhA4t5dqbZPpgvR9RwgbQP3Z_cS6dMXRi71VmITQ14co_8EobSeEWWY-jRZuMetw0oCPN827ywdnJlLfcMAG_MwU28Bb_o0DiOeo72gZQ2Wkqxywrylzm754dAtsgp5ETWA2upWL8kHP3952vc5veubufWq3A99BbSeE-OTLUA26l4kjmnqCsSEolS00AAnpD0cCkRRVexsvdgxX5qSlbYATKh95X6T4oONHuW7_zEwqVB0EMgnrpU9VHOEhtB3d57S3otHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a0f52793.mp4?token=nrskSmX5X1-X0Rl0ZCJEjnmOUHtWhKmwjj6b74z3mPpBJb3b9IEgQiPAhYlRB366yfGZk0yeKqTaIqxhA4t5dqbZPpgvR9RwgbQP3Z_cS6dMXRi71VmITQ14co_8EobSeEWWY-jRZuMetw0oCPN827ywdnJlLfcMAG_MwU28Bb_o0DiOeo72gZQ2Wkqxywrylzm754dAtsgp5ETWA2upWL8kHP3952vc5veubufWq3A99BbSeE-OTLUA26l4kjmnqCsSEolS00AAnpD0cCkRRVexsvdgxX5qSlbYATKh95X6T4oONHuW7_zEwqVB0EMgnrpU9VHOEhtB3d57S3otHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی از من خواسته اند تا حمله نظامی برنامه ریزی شده خود به جمهوری اسلامی ایران را که برای فردا برنامه ریزی شده بود، متوقف کنم.…</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/funhiphop/75322" target="_blank">📅 03:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75321">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ:
ما حمله‌مان به ایران را ۲ تا ۳ روز به تعویق انداختیم چون عربستان سعودی، قطر و امارات فکر می‌کنند که به توافق بسیار نزدیکی رسیده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/funhiphop/75321" target="_blank">📅 01:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75317">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7hS9LeqD0-s4_QBKRuo3WCLl-dqi6u3lqjveH30LVeMTiWK_EJ0AufXW3c0mjfS8p2T94FDrQ_hCD5cc64VKI1Krp-ZLpIZ0E3Fk7l7C-CwemGxTpryWHTJ-y3hdsZOcgGfetma_bpl6dGINGJydb8xAl3UQfs02k388v2r3OYHzL2QUrvvWstWds1C8XweGgXhACIahm9U99zc1QeqT86XJ68CjfXEPUIzut3bsT6LMDuZAkxbonmuyP-9jGqli8YPzRrgBgQN3bLfLkWl9vN14c_wRHdDM7ed_vZplAXfZT2ScYwc4z9pXVPveDt4lzKc0UuSJgc0A_DBM1KSig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/funhiphop/75317" target="_blank">📅 00:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75316">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کارلو آنچلوتی تو یه حرکت انتحاری ژائو پدرو رو از لیست برزیل برا جام جهانی خط زد.  پ‌ن: نیمار دعوت شده  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/75316" target="_blank">📅 00:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75315">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XC14ZOCUDL3jWeUgnd3QeUbaDfYvX0DTasxxrsJsJaiSrwOobMrRaMzPU5z1mA2PC_rbm6QNPYVCGHTpF-RHY_KKrVxGgGXlxEtbCHwuQikxg2Uc9hIFew0xrS6u6l5HpeZHAgKjfgMtfubOFYYF9so5YYnL2CK1ULHadL1McGO3SXg-2no29nu8IjFG7GOZtFshwUZl7z57e7zhckHW0mz1lB9rYFkbaCMgZGPgO7Q1hDA7QyCWqlc6_lXc4K7SrVSFebFibs5whyEfkO4TMgZVk2SFEEM63kagu7JIvbcs7fdCq47dr5EVJvYiWVwmxzrwlfmnJKhrLf5Wd2v_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارلو آنچلوتی تو یه حرکت انتحاری ژائو پدرو رو از لیست برزیل برا جام جهانی خط زد.
پ‌ن: نیمار دعوت شده
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/75315" target="_blank">📅 00:38 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75314">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کل تلگرام دارن با کانفیگا رایگان سونیک وصل میشن شماهم وصل شید:
@SonicVPNRBot</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/funhiphop/75314" target="_blank">📅 00:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75313">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پدافند هوایی اصفهان درحال فعالیت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/funhiphop/75313" target="_blank">📅 00:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75312">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppa6bp4TPP6pq_Ft-NtTHmY0zvvQTgF_7aiXUhW2X8KPZ8GyDxNujlM2mMDJ5QKxj0MrTb1XkJ08xUEHU40_Hqo3VojErwrONVK44GHJTmECk4bBnRWh7YqEznARr0D_Sp7yt4ke6YGBAw5JR9KolxZSudJyBlRGNr6APUaKTPIM34bNdyS82mn36CpDUMkPWPmRAzRrXmaN177RIYk2jxsA_McLsUy1ziAOIFOjdyv2m2v2L4qOAVL9OTdslMT2-DcHBVOAGAVeN6DUrfMqB6RdSPiv9CKw99bHD3hwcTi99HHwaRq_ewS1x3_dwbx-80AVHpRdQBttLH9oZkbReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
فیلد مارشال رضایی
برای حمله نظامی ضرب‌الاجل تعیین می‌کند و سپس خودش آن را لغو می‌کند!
با این امید واهی که ملت و مسئولان ایرانی را تسلیم کند!
مشت آهنین نیروهای مسلح قدرتمند و ملت بزرگ ایران آنها را مجبور به
عقب‌نشینی و تسلیم
خواهد کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/75312" target="_blank">📅 23:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75311">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">فوری: پپ گواردیولا در آخر فصل منچسترسیتی رو ترک میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/funhiphop/75311" target="_blank">📅 23:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75310">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">با رفتن پپ از لیگ انگلیس، دوران پادشاهی آرسنال با رهبری آرتتا رسما شروع میشه و تا سالها هیچکس نمیتونه جلوی این تیم رو بگیره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/funhiphop/75310" target="_blank">📅 23:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75309">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فوری:
پپ گواردیولا در آخر فصل منچسترسیتی رو ترک میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/funhiphop/75309" target="_blank">📅 23:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75308">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">باز حداقل الان ۱۰۰٪ سهام کمپانی های خودرو سازی داخلی دست خودمونه
نه که ۲۰ درصد بنز دست ما باشه نصفیش دست اجنبی‌ها
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/funhiphop/75308" target="_blank">📅 23:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75307">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQCJQcs1l57CYuuxowy0C0vsEIrqHO__iRzpzDV5u4UvxigCxkCtYW3OPO569lIM-mCcTv3Q8Kxc-6An62dUweb7hu1d0MBciGJm0PY2dgw41chXESLviWF1m7qFhOgAETo_2T5EKuUmW-VvYL9B9M8sH5HGhmpEXBcOVP9MLIwYGlff6x7EskeMBc2wbM58oxq_kPAOWzhIq8n3FnqwZxVL0EUgCVsk3VOAwMUF9f6KzUDqEOqXcLDObeETv9UDn-OCZzPqZJqQQ24njUC5EGfTJBUStIPPpS28cxY9T32oryvg4RV7A4P1yzTKxfvrgWczzf27o3YW7-3mILfPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی از من خواسته اند تا حمله نظامی برنامه ریزی شده خود به جمهوری اسلامی ایران را که برای فردا برنامه ریزی شده بود، متوقف کنم.…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/75307" target="_blank">📅 23:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75306">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNDWZi292RNNhj4c6BTOWxQk_2HRstVpFdOjzUhjMiBou29Aj8iu1mRPhIShk2sEFMoPwBSamNiyOO1DtABkUkS7xg00vUFCrXZIpADcpYcTU9ApC-UHp_rTxdNIWKoyy97V7_PYSwAKCo7lJo869mVmxxDC1S7Rf3mkbjL5S6xr9mqfels2KjCT3LRQgvR2a9FonDeHEL3uomcgYOrcpzMVAe6VBN0OC578uXeO1HBwepOEJd1-z0HUV18Vgtdg8stJtz5VmlDrVfI6ZmktBSqPMX_q5QuLnv54Lvr1UoyYglTgdpSs4LupkaP2xsT4dwmUcqXGDLqehSRvmldpGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و محمد بن زاید آل نهیان، رئیس جمهور امارات متحده عربی از من خواسته اند تا حمله نظامی برنامه ریزی شده خود به جمهوری اسلامی ایران را که برای فردا برنامه ریزی شده بود، متوقف کنم. به امید توافقی که خواهد شد که برای ایالات متحده آمریکا و همچنین تمامی کشورهای خاورمیانه و فراتر از آن بسیار قابل قبول خواهد بود.
مهمتر از همه، این توافق شامل عدم وجود سلاح هسته ای برای ایران خواهد بود! با توجه به احترامی که به رهبران فوق الذکر دارم، به وزیر جنگ، پیت هگزث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین و ارتش ایالات متحده دستور داده ام که فردا حمله برنامه ریزی شده به ایران را انجام نخواهیم داد، بلکه به آنها دستور داده ام که  در صورت به توافق نرسیدن آماده باشند تا با یک حمله قابل قبول و در مقیاس بزرگ و کامل علیه ایران آماده باشند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/funhiphop/75306" target="_blank">📅 22:42 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
