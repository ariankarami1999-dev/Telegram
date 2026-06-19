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
<img src="https://cdn1.telesco.pe/file/P6qKMhYxDG-c1D6KlB1hDJyP5RqYbvTkSPTGk0QhwFd-_jv1wIEQlfCH1ujPOWIvvTbBWO4DtHtzYizPQl6IfA-U9CPHmtbgduv4KVSnqq1Qg-m8AtC0kTWpPJ1hOQIPTaJG6Ae7egw0U_6GknTHMXOsqU52g0Qm8QqKsyH-fAQWmHBeFtsqBeXPjndy-QAFoYJL-mumqnaX-IDt_23v_kYN_xLxH0EDUmYvginEmxyZQXGxuVYs6oY5AjvLtgc5PWY8tPq8yHA_9sh15BL5OKpDMkE5tYQNd3-gDBkzhLSL8HCAuZT9ny5fLzpUDGaRhKxn9JbbbWnVS0Vr0Q1Pnw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.36M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 23:41:36</div>
<hr>

<div class="tg-post" id="msg-76533">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzxrrJ1ucf19rL96DS1ikS3CWbAESec3ZuxLUmfUuSA7eyohhrqdkc9vXVidbKen00Y1B5dmleQTp9OZ2x51BT_4GXMOJiCVrwfqbvB6i9CBK7-2TEH5cG77SKEJn1tL6FLCAJrIMrC3muziTGbev1Fg4eipdhIVw_HQztC0jMBME6y_B13W-FrTXUKkk53AgquQJFz1Nx1I3is8zlzOrlYPN_k1OsH6l_vnI6dN3sk_M7OFfGTA2gfp_oFetdZ_9dx7jwXfGRqaCWkXUV3GUtk2YMAl44KnNWEFxng3jYCvHd4bN65UeBLarAorrQRbZLl5ZY1iF7ll6PA-GmTihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس‌جمهوری آمریکا، در مصاحبه‌ای با برنامه «آکسیوس شو» با دفاع از تصمیم خود برای شروع عملیات نظامی در ایران، مقام‌های جمهوری اسلامی را «بسیار باهوش» و «نابغه‌های بدوی» توصیف کرد و هشدار داد که آن‌ها در عین حال بسیار غیرقابل‌پیش‌بینی هستند.
ترامپ با اشاره به مداخله نظامی اخیر ایالات متحده گفت: «من مجبور به اقدام شدم تا جلوی آن‌ها را بگیرم؛ چون اگر سلاح هسته‌ای داشتند، حتما از آن استفاده می‌کردند و با منفجر کردن چند شهر، از جمله در اسرائیل، هرج‌ومرجی واقعی به راه می‌انداختند.»
او با تاکید بر اینکه اگر اقدام او در لغو برجام نبود، اسرائیل سال‌ها پیش نابود شده بود، توافق دوران اوباما را مسیری هموار برای دستیابی جمهوری اسلامی ایران به بمب اتم دانست. ترامپ همچنین با ابراز شگفتی از زمان‌بندی تقابل با ایران افزود: «چیزی که مرا غافلگیر کرد این بود که آن‌ها این‌قدر منتظر ماندند. آن‌ها صبر کردند تا من به قدرت بازگردم؛ البته این کارشان عمدی نبود. هیچ‌کس، حتی با وجود سلاح‌سازی ساختار حکومتی علیه من، فکر نمی‌کرد بازگردم، اما من با خروشی بزرگ‌تر از قبل بازگشتم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/VahidOnline/76533" target="_blank">📅 22:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76525">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشجویان متحد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JzkE-K9d-BprIyTkREwYhaVt2MA3nDtRXi4xMLgca8Lij3-t1A-OqZP22wHUMEaTiH5mefy6wkdw0KLhpfoi_6y-m732H2vaiXZ1Jr_WHMvAMISLiZb5Bso247ftQRY6YNQZJkEi6aBw7YKIkoh68v4d6c6-sZo7nmzTb4NIXZ89gsOA1tfhTX6YrRW_UF2zIa9xxmMFncVbzF-Qi8bzWLIL-ThlKFHSYpS7R-ORyq-qQJnksDsvNaakbzNI30p8kvUrZrKZTXb_0eDVHTolGLW2sImJ9AKtJl9gwbIgAICBvu_w-gzzviHxCU8Rdc5q_VU0NaNgaBOfnBCZD0kAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9GGkXMCk-keeJ6dMlsYQ4gzkRyN8ETzdM9tdQI6Jrg6JgW4WX5NG0OwJdnkup7jiO-V9pdiM7BcNuN461m2y8A-A1z4oWooDO0gWmmwqjiNHcpOlh7mWCj8i7hrqSR1UXMJ21bagxR4AKGXYfCloeXOxJKagPyqjtTKBXcLWiCI8obF-DUGWyW86FtY5lWKENmN5EzN7ExHFIp4ZYVRSQVy20MOwLEsPkdUzhOwfFOqplseXMfLTqJWk8w1YbShdXQ4dbpG62UELZRcOAM9qV5dXY2qAL5HxikEezuTjheAkZ7SN4jUTnLyMN8hocfluDi2g14nCB6LQ2Z4L-1lvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6iAkPNWia7riu5unbXyA7JHdjhyxtxP5wSWUhP1zpeEQ90qqH2YVRU5me_Nu30T0zPi7HuWGKeY4Vz7w_2Dpez_jMaTDxj4Da-iS4bpWZeOmtBWeZ5E-vqSNNFt1gQ1jSCejP8mPhc04TyscY6DtJCujM29RqFDiQ6y8jiiaZVm1Q5DZmaZt5QaugCihUQSuyXTs_guCAnNVek-5QVnDp97ajT6pMda1GEGiJWQDUh-cC5TxH8pi6fchdNJoAWirkyw4uP59wnYy_PKrPMVWycs1cxb4F0DqCUJHBgz6P7poeS_qzOXnGoNpIFgKtbLmKJOGKCdWLzca_HXtDKWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHv1jaSKe1onpip6j_nKd0FzKdsSfrg7rA2-lhGoDQ_HuBzpQIXYC_Bc76ogXmSDkLT_8c3mA1pOZUlQEfXrNqgCvS9WTKdp44zOrQ65T4B3lKGeCcM9p4O0sDZdfR7_b60I-Oy-OYqP944cQdLFDB7j_fnvyseBOYk2D9_DO5gENyYNwdDoMmvCktNUiu4OrfErXm9wabqdDglYNq9YwMYXlrme2ekuVzPNzr5Z0Kzk1ZL-nGPFaVkd6-9ELzYRapAupfyc8Evbw6OdaO92vqa0rfElo1lbaunMOkjztDox5v9_jSHVl6CDo11_oJzX8hT7d_mFIXtEimdXAHlfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e4d2z7ggmV5KsrztHj0rEglsl9GuiCL5mTLEyWEoGYZ9YX6TN5HXhaXJ_QDFFKvL5Lk-KoxZgciDMQjyb0DYSCW4ul0bkUIuLhFYv_qgo2AMhPz3zfV-W_VDtHi8QAyx4BC2LQegAZkdmiSCxU7rgKb574A66-qJWGKJHCtjpQwh7DcCx4T6E8OjrJeZ04WXaaICBWeqbjgQ18VABsMAofmPVMInaxv1gGzQ0AW0KRkJIsEAgKv6mnLknuynupZ_ANXi_fnO321_3Hil2yGeQ8CjCIRxg7oi1F7lMxq4RvndtrxpRrq1ceyZu-kQwoxSm_jDdzNLbmfknWto06crhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K_jjrFxOUHJFwdCdAYNWzC3etf7UoprKifsWdODYm24nliImvKEJ_ypHEV0-Fk_QioBfIUQkpF6z-1A2lz-gjVvS7e72V5sfdQ9d93ZL7mvc5yGW8wb5yf7enVZ8Q-pU1uuxmwkVf9UF_qvi3OpDRyN62-oC17QwdDBrhh0S_dn3mLrtafVISc8VWaF581ycWmC_tLI7G-kr_4PYROnUjAa_Il8_vIPZyTErlpLMcu7V3-PFuGzs1btw6_LpnbUDkqg7gEZ71zEew-WriwMFpX2v5RQmkcbTR2hxu3MJXTOS6bzziSRDJzLG06C6yunmA6TyX6F-_51oTnw6ur-orw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIXNaQ70Q72zXPsFwWrr26D0WAJhby6bK_k5nkplERExCfzY3sn8XpyMbQWzwvS5WIyfiPNSHQTSqd02YCiLVoY-VChLKKVAgHnNdjjlO0h-hAWS8PhB2Qc2xBF6GK0O6FOHB4l-x37USlbQDNRblaIAQWbuiLFdTLX5aCwlPd8sUHs2fs59y_zzgRoQhLInAu3T92DlhOwq1PoA2IDoNLYx9pI4X1MrJTvzZRcSIT6lbvL2JsR_edWO0_bazRKV2t-UAQPApohZec9G0OreE30UyPn2vbwGQlk8waU_KkCn1P4nXY-i8mobi3uGYtOj-ML0c5rj2hD7Qt4upajqQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1Scn9A0kbtctrPMFKgmQYVH0y19MIe2GciBGQS1IwUOkvoP9_mO6sWN7A2HTpP73TD2GazUiTojHaY5gN7tDQDO_aCQqefIG3Ds1Q1gUK4r8csPz-j-2WZwP5QLJOVTw8MlbJNmKPhBO6cJlrCgwddLdCf6rpapdN2MvFJgmq2csIs5DIMNFx0lPzc10Q9hOFEJb6TzyA2OWJGPbtF7MwwgHBg1u-DJ-AeVLJPGpAVck2_p60lHPd8PETMVOxp221hTlPKsiwjUAYauaSRlCCoJZQVnCO71qgxravABuTHDI5xKXa2aIEZgedPB7IKrBm_NpWrPjxUDfoh5xIkgVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
صدور حکم اخراج برای هفت دانشجوی دانشگاه شریف؛ صدور حکم غیابی برای یکی از دانشجویان بازداشتی؟
🔻
بر اساس گزارش‌های رسیده به دانشجویان متحد، کمیته انضباطی دانشگاه شریف، برای هفت دانشجوی این دانشگاه حکم بدوی اخراج صادر شده است. اسامی دانشجویان به شرح زیر است:
🔻
رضا دالمن، ورودی کارشناسی ارشد ۱۴۰۳ مهندسی کامپیوتر: اخراج و چهار سال محرومیت از تحصیل
🔻
فاطمه خاکپور، ورودی کارشناسی ۱۴۰۳ شیمی: اخراج
🔻
حسین شادمان، ورودی کارشناسی ارشد ۱۴۰۴ مهندسی صنایع: اخراج
🔻
سپنتا سعیدی، ورودی کارشناسی ۱۴۰۴ مهندسی کامپیوتر: اخراج و پنج سال محرومیت از تحصیل
🔻
مسیحا باقری، ورودی کارشناسی ۱۴۰۲ مهندسی کامپیوتر: اخراج
🔻
فریبرز کهن‌زاد، ورودی کارشناسی ۱۴۰۰ مهندسی برق(تغییر رشته به مهندسی صنایع): اخراج و پنج سال محرومیت از تحصیل
🔻
پرنیان خدابخشی، ورودی کارشناسی ۱۴۰۲ مهندسی و علم مواد: اخراج و پنج سال محرومیت از تحصیل
🔻
همچنین در برخی رسانه‌ها خبر صدور حکم اخراج برای «آریانا کوچکی»، ورودی کارشناسی ۱۴۰۰ مهندسی صنایع، نیز منتشر شده است. هر چند بر اساس گزارش‌هایی که به دست ما رسیده، ایشان در حال حاضر بازداشت هستند و خبری در مورد برگزاری کمیته بدوی ایشان نداریم. هر چند صدور حکم غیابی برای دانشجویان بازداشتی در جمهوری اسلامی، پدیده تازه‌ای نیست.
🔻
لازم به ذکر است از میان هفت نفر یاد شده، کمیته سه تن(سپنتا سعیدی، حسین شادمان، مسیحا باقری) با محوریت فعالیت در شبکه‌های اجتماعی و کمیته چهار تن دیگر با محوریت اعتراضات اسفندماه برگزار شده است.
ارتباط با ما:
@Public_anjmotahed
🆔
@anjmotahed</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/VahidOnline/76525" target="_blank">📅 22:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76524">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=YaPJ1aWLFd5dFEtjiba7b_bFWsBGIqTWBpSMG2_V5OKPgyJN2j9kUvD2v0p0w-WYXMic_CjLiNvBZR7YnIqmjLOsBPGMqGlzitNWnAwReWzTBJkSi3hr9s6L6AiDnEHRGxT-RUeFzWQa9Ylg2f12eUv48aMjRLCO3tSqoUdpRdrm0MPKHfhtfJtLh9P64XG1mfkk1nQDArFanFLLmTgQg_MPSDq_fPDM2tE2xPf5cT4FT06u-OjTuDF7eGF0dV1h9zFXnTeWdwIjEAF1VV6rPqnOk1RqtA222yo-O4inDAkghx--CdgKBWwUuQPNtdiKC93h22X8t0394IUUuduTJg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba856aba9d.mp4?token=YaPJ1aWLFd5dFEtjiba7b_bFWsBGIqTWBpSMG2_V5OKPgyJN2j9kUvD2v0p0w-WYXMic_CjLiNvBZR7YnIqmjLOsBPGMqGlzitNWnAwReWzTBJkSi3hr9s6L6AiDnEHRGxT-RUeFzWQa9Ylg2f12eUv48aMjRLCO3tSqoUdpRdrm0MPKHfhtfJtLh9P64XG1mfkk1nQDArFanFLLmTgQg_MPSDq_fPDM2tE2xPf5cT4FT06u-OjTuDF7eGF0dV1h9zFXnTeWdwIjEAF1VV6rPqnOk1RqtA222yo-O4inDAkghx--CdgKBWwUuQPNtdiKC93h22X8t0394IUUuduTJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه جی‌دی ونس با زیرنویس فارسی
گفت‌وگو با:
الی بث استاکی، مجری و مفسر محافظه‌کار مسیحی آمریکایی، میزبان پادکست Relatable در شبکه BlazeTV
برنامه‌ای که در آن از زاویه‌ای مذهبی و راست‌گرایانه به سیاست، فرهنگ، خانواده و مسائل اجتماعی آمریکا می‌پردازد.
او در میان مخاطبان اوانجلیکال و محافظه‌کار آمریکا چهره‌ای شناخته‌شده است و در این گفت‌وگو با جی‌دی ونس، معاون رئیس‌جمهور آمریکا، درباره ایمان، خانواده، سیاست داخلی، اسرائیل و توافق با ایران صحبت می‌کند.
یک ساعت درباره مسیحی زندگی کردن
حرف زدند
و ده دقیقه درباره نقش و نفوذ اسرائیل در سیاست آمریکا و توافق با ایران برای مخاطبی از اون نوع
اینجوری می‌پرسه: می‌خواهید یک مادر معمولی چه بداند؟
متن این دقایق:
https://telegra.ph/JDVance-06-19
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/VahidOnline/76524" target="_blank">📅 22:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76523">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daGB3X_GDzmsAqozY34lMF1hqbsHCnRIC2qBfy7Zs4mtqvm5L0f2ppz-zQ_EZFmsFGXirwcpLHZkva-fcZbaFbHGtYkCgOIF3PlyTylR5r8eyf-JFDI-OOasVC0zO4iPsM2hFIRJzesKLueTZOckQnMblcoIDP3iZt4nrvaRTKDJQF67gXYfYVz6TTNkXByAOrXiSODM-2aVe8Gz8lF_BsoT2H_TKNXYjLj6fFeOfGASWcIbQJIZvrFCu30uHxmHzYV2OulHeVq407-l-fivSYq6x-I8eMcfFyuMlAg3xnwcDGjOLssAK40y1uY87MIB7fcHmh-7ngufya8-CJdNAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در یک گفت‌وگوی تلفنی با شبکه ان‌بی‌سی نیوز گفت که روز جمعه با مقام‌های اسرائیلی صحبت کرده و از آن‌ها خواسته است با گروه حزب‌الله بر سر آتش‌بس توافق کنند.
بر اساس مطلبی که خبرنگار این شبکه در شبکه ایکس منتشر کرد، ترامپ به این مقام‌ها گفته است: «بعضی وقت‌ها فقط باید آرام بگیرید و از عقلتان استفاده کنید.»
این خبرنگار همچنین افزود که ترامپ مشخص نکرد آیا مستقیماً با ‌بنیامین نتانیاهو، نخست‌وزیر اسرائیل، گفت‌وگو کرده است یا خیر.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/VahidOnline/76523" target="_blank">📅 22:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76522">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eIo4Vhi2jQAPKOcWtty-Hkxm0VfxPZ45zBt20UABQO4Za-dsnwCKcNO-U9MLhwuWmX9lSp2R5LY2rIpH0FltWF_YD4zei3fgQI5lqhvFKk0Su6gWXCMaTihZDz6dxjR2HWkb0YdGDIqSfZxIhwhJgoTOYmhOjvLm4AB5UB6QDV-2acXnS_QkWOlr1xhVAribmgDjPaUt7jjHvYOh_WBxCUH2MJTuZHMY71zkpNvJwEk41j56jbvI6kUzeipNW7zUR0JfnbUTPyECqFvYlKYeXhljvclkb1gix2u3KSDOTO51-fIeNbGh0opuh3RNNTf86e1ggKBaxB8IgVibYNC2BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نعیم قاسم، دبیرکل حزب‌الله لبنان، گفت: «تا زمانی که توان ایستادگی داریم، چرا باید تسلیم شویم؟.»
او تحویل سلاح‌های حزب‌الله را رد کرد و افزود این سلاح‌ها برای مقابله با اسرائیل هستند.
نعیم قاسم همچنین گفت که ما تصمیمی «به سبک کربلا» گرفتیم و این تصمیم همچنان به قوت خود باقی است.
دبیرکل حزب‌الله لبنان ادامه داد: «ما وحدت نیروهای مقاومت را حفظ کرده‌ایم و وحدت جنبش امل، حزب‌الله و سایر نیروها همچنان در کنار ما برقرار است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/VahidOnline/76522" target="_blank">📅 20:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76521">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX3ZKCO-9pFR-azgfXzLcnD6yOB-PrMa6mDqZPsW61oQNmmcTwbVCzc0B5olSKGxtSeUgGXr2NSSzuzSJoHLUmO6QN9Zso45UM7iEHSjlCYMOukc9L7DiQUoR4ikUp96Ae7F_YnwsigSpfTukEfLxD6596xFbSulPn3p8yqdPRMrlMtHoQV7ngkZOH_g4orWZGejG8Wn0Uxvsr3run_TWl1xd2hzNhjN22M3T7Zcy30hA2bMw3pLL7RvbTf9Uj7FbUKAT44x5NoJ1Sb1EtN5af14cenLf9rEyqsQPzr_Z0pHp7UaMKHf5C9pbgOQmqCUYVyJoWvuEjKkIlShVnJJ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقائی، سخنگوی وزارت خارجه ایران، روز جمعه دعوت جمهوری اسلامی از بازرسان آژانس بین‌المللی انرژی اتمی برای حضور در ایران و انجام بازرسی از تاسیسات هسته‌ای را رد کرد.
او گفت: «بازرسی از تاسیساتی که دسترسی آژانس به آنها به‌دلیل حملات نظامی متوقف گردید، منوط به روند مذاکرات و نتیجه آن خواهد بود.»
پیشتر جی‌دی ونس، معاون رئیس جمهور آمریکا پس از اعلام توافق اخیر در گفت‌وگو با شبکه ان‌بی‌سی گفته بود که بر اساس تفاهم‌نامه میان واشینگتن و تهران، بازرسان آژانس بین‌المللی انرژی اتمی «قطعاً» به ایران بازخواهند گشت.
اسماعیل بقائی همچنین گفت در حال برنامه‌ریزی برای برگزاری یک نشست طی روزهای آینده هستیم.
نشست بین نمایندگان ایران و ایالات متحده که قرار بود جمعه در سوئیس برگزار شود، لغو شد.
سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد: «با توجه به اینکه امضای متن یادداشت تفاهم در بامداد ۲۸ خرداد به صورت دیجیتالی انجام شد، برگزاری نشست مزبور در سوئیس فوریت ندارد.»
او همچنین گزارش‌ها درباره بسته شدن تنگه هرمز را «بی‌اساس» دانست و گفت کشتیرانی در این مسیر در حال انجام است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 203K · <a href="https://t.me/VahidOnline/76521" target="_blank">📅 18:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76520">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rvwn0cq-so5ecbxrtB-CNTXAVIc_ydcRohHjiSTUpp_x60Tqo0W6Zf8Yc5HWCQyPPJvNYifT2DU-7HQW22DzjqSUApZKtpeZO5AcHIvscbCWrELz648Ncu5XvcIX1fit1puEbfGHK-S6rmfQKDrucxnIAh7qkleHQuKuJiQlntPsPC5EwRHcd0K8Ii-6mAcAyLJj04uIvjDT-TJpvO-3P7EwzRgQ90lNssgu2jQjkDEhVRaaqhJDeFJcuco1kCn8QqsUrU5Rx_0d81tbNGHGZYjpbDOso6GUVvq6OfX_uMFpZ9Zh0A19XUUNUREsArjgsDGMFsYjGP7VxvqL33Apww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام ارشد آمریکایی به رویترز گفت که اسرائیل و حزب‌الله بر سر یک آتش‌بس توافق کرده‌اند که قرار است از ساعت چهار بعدازظهر روز جمعه به وقت محلی آغاز شود.
این مقام که نخواست نامش فاش شود، افزود که مذاکره‌کنندگان آمریکایی و قطری با کمک ایران این توافق را نهایی کرده‌اند.
این مقام همچنین گفت: «درک ما این است که پس از تبادل آتش امروز، اسرائیل و حزب‌الله اکنون در وضعیت آتش‌بس قرار دارند.»
شبکه العربیه نیز به نقل از یک مقام آمریکایی از توافق برای برقراری آتش‌بس بین اسرائیل و حزب‌الله از جمعه خبر داد.
این در حالی است که نخست‌وزیر اسرائیل ساعتی پیش اعلام کرد نیروهای نظامی این کشور تا هر زمان که لازم باشد، در خاک لبنان باقی می‌مانند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/76520" target="_blank">📅 17:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76518">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R_DbgQvx34mq1YhsBIGuT87fqxB7LFgfiQoW31oTgAmff1wZaVx2oD6xwS3-wHqK_zBJtfMLBn5Q-cVyrrS8jabIvkl-xn435sCsJkyqrJpoogxtm8QGgBNG6aubq1vHGAm_NZtbzmaxXAnvWGHUjYoXA6xcE8Y1qeUt5gkEyS6ObktsfcTgt1EDUO4pj7n99sZ_A70jhVcbJG8p_lE4dasYhqwanlw9KHCMJuVHoILO0Mp6eJ81rd5VR3FV5rRvlJXzLhrv9jI4vl8Y7FYePQRD9FzDXVxEx2rAXpmxT5nIwkrl1fHOIzBv5RvN21YN9eGNtIMKkkRHgsPiVlBDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/957528437f.mp4?token=g-gn1flGFO1MZDnl4JyRxGBfwYEFdzVmb6uU8LmF4tSIJlwWus9FASlbgpnCD6qSrxH9TF28wYOMgzNOBzeWho2cyVokEW_34pDElPI58KcnWyG0PtdMxNyuaIJ1ds_YDFIFWamk7z50m6fjASP1ZFxJXJHUxV2Dm0O6gl3tClcTTPwr-x6B4J39bk9KQDkb_7u1VyyREhZSXFF_LVyK74Mjn3vegtP3K7su5ogFAnopW9RZhuNjANRaCfreaaDZ8ywd9NbIRt5wsiBmRS9WVTPU0wxG8fcySb6HS_Pq0z1dPNG-j7-FWe0cMK3LG__6SrPRRjUeJXngdRHmFodfSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/957528437f.mp4?token=g-gn1flGFO1MZDnl4JyRxGBfwYEFdzVmb6uU8LmF4tSIJlwWus9FASlbgpnCD6qSrxH9TF28wYOMgzNOBzeWho2cyVokEW_34pDElPI58KcnWyG0PtdMxNyuaIJ1ds_YDFIFWamk7z50m6fjASP1ZFxJXJHUxV2Dm0O6gl3tClcTTPwr-x6B4J39bk9KQDkb_7u1VyyREhZSXFF_LVyK74Mjn3vegtP3K7su5ogFAnopW9RZhuNjANRaCfreaaDZ8ywd9NbIRt5wsiBmRS9WVTPU0wxG8fcySb6HS_Pq0z1dPNG-j7-FWe0cMK3LG__6SrPRRjUeJXngdRHmFodfSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر امور خارجه ایتالیا روز جمعه اعلام کرد در واکنش به گزارش‌ها درباره اظهارات دونالد ترامپ سفر برنامه‌ریزی‌شده خود به ایالات متحده را لغو می‌کند.
آنتونیو تایانی در شبکه اکس نوشت: «سخنان شدیدا توهین‌آمیز رئیس‌جمهوری ترامپ… به همه مردم ایتالیا اهانت می‌کند.»
به گزارش شبکه ایتالیایی «لا۷» ترامپ درباره دیدار خود با ملونی در نشست گروه هفت گفته بود: «ملونی آن‌قدر می‌خواست با من عکس بگیرد که فقط از روی دلسوزی با او موافقت کردم.»
@
VahidOOnLine
جورجیا ملونی، نخست‌وزیر ایتالیا، در واکنش به اظهارات اخیر دونالد ترامپ، رئیس‌جمهوری آمریکا، این سخنان را «کاملاً ساختگی» خواند و گفت از نحوه رفتار او با متحدان «مبهوت و شگفت‌زده» شده است.
او تاکید کرد: «نمی‌دانم چرا رئیس‌جمهور ایالات متحده این‌گونه با متحدان خود رفتار می‌کند» و افزود این نخستین‌بار نیست که چنین مواضعی از سوی ترامپ مطرح می‌شود.
ملونی همچنین این رویکرد را «مایه تاسف» دانست و گفت او قاطعیتی را که در برابر دشمنان غرب نشان نمی‌دهد، در قبال برخی رهبران متحد خود به کار می‌گیرد.
نخست‌وزیر ایتالیا در پایان تأکید کرد: «یک چیز را باید به خاطر بسپارد؛ من و ایتالیا هرگز التماس نمی‌کنیم.»
در ادامه این تنش‌ها، آنتونیو تایانی، وزیر امور خارجه ایتالیا، نیز اعلام کرد سفر برنامه‌ریزی‌شده خود به آمریکا را لغو کرده و این اظهارات را «توهین به مردم ایتالیا» خواند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/76518" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76517">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکمیته پیگیری وضعیت بازداشت‌شدگان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgYEkkPXkA6RwIJ7Gs6joLZo2ppOwNA_3_AWs-Ijr36yfI-MoDF80amstjanfq3Ulik5nRigA8HkkhuZAzQoVqmgSCPrmFhIWcDQcCoqrFK-8IYmL47uLVtzjna-G1vYmD2WbI58FTfblvxR12qTt5cLXTwCKzFWwsfjtUDqpdYaC0PRmP6T7eG6YLjmIDCqmTjTO-2Qbo9evhyQuA4hHxHqQNxyRj6TqkAuVJoT_340lbYY07KZu_M-JVAeZKD_hCnH2DIc9Qr_m-mg35j2mjAk1dK0dzq7M7nzZd9S7Co_Ctk5lNNjdyEZmhXwWYPtJCJPLSltSk4gQANz1As1kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅️
#محمد_نوروزی
، شهروند افغانستانی ساکن ایران، که در روز ۲۵ دی‌ماه ۱۴۰۴، در منزل مسکونی‌اش دستگیر شده بود، توسط دادگاه به شش‌سال زندان محکوم شد.
🔹️
طبق گزارش رسیده به کمیته پیگیری، محمد نوروزی پس از بازداشت به آگاهی ملارد منتقل شده و پس از ۴ روز همراه با ضرب‌وشتم فیزیکی به زندان قزلحصار منتقل شد. او طی این مدت مدام تهدید می‌شد که رد مرز شده و از ایران اخراج خواهد شد.
🔹️
او در نهایت با قرار وثیقه یک میلیارد تومانی از زندان آزاد شد و سپس توسط دادگاه به اتهام "اجتماع و تبانی و تبلیغ علیه نظام" به شش سال زندان محکوم شد.
این حکم هم‌اکنون در مرحله تجدیدنظر قرار دارد.
🆔️
@Followupiran</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/VahidOnline/76517" target="_blank">📅 17:22 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76516">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSYhSkpsBtyi80V9Eglhk-YATwih_bJJm-ip14EtN0kHMKlsuT68dYef7yph9m7WcMtOvZmvNdWaoWWuWkodiO9vjh-24wtxEQSew41naNrGW6MS_ndIy4VdCk-XH1xM7eG0YK5B3lXMawwNr-RfFgwDvtUksXe9A294_7utN-1e4aWd-Vl-70sBlP8qXQYxiKTWyHLK_fUBg6UaYxVH40RDyOKwbDxWQ_07_6gXDf6uuD2YOiC4uD-ZFgYLQpuZ1TDqXkmxitc60102rtkEh85Kxu6p6DxdUP-WS9qU7lhJfIoErgXFdDsiaYSnKQhsMlI_hKb5lLJGA1GRitUzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز جمعه بار دیگر گفت که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در لبنان باقی خواهند ماند و وعده داد که حزب‌اللهِ مورد حمایت ایران برای حملاتش «بهای بسیار سنگینی» خواهد پرداخت.
او روز پنجشنبه، ساعاتی بعد از امضای تفاهم‌نامه پایان دادن به جنگ توسط ایران و آمریکا، نیز بر ادامه حضور ارتش اسرائیل در مناطقی از جنوب لبنان تأکید کرده بود.
نتانیاهو در بیانیه روز جمعه که پس از اعلام کشته شدن چهار سرباز اسرائیلی در لبنان از سوی ارتش منتشر شد، گفت: «اسرائیل حمله به سربازان یا قلمرو خود را تحمل نخواهد کرد و بابت این حملات بهای بسیار سنگینی از حزب‌الله خواهد گرفت.»
او افزود: «اسرائیل تا هر زمان که برای حفاظت از جوامع شمالی لازم باشد، در منطقه امنیتی جنوب لبنان باقی خواهد ماند.»
یسرائیل کاتز، وزیر دفاع، نیز گفته بود که ارتش در لبنان خواهد ماند و افزود که به هر حمله‌ای «با نیروی قابل توجه» پاسخ خواهد داد.
لبنان اعلام کرده بر اثر حملات اسرائیل در سراسر این کشور ۱۸ نفر کشته شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/VahidOnline/76516" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76515">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P_VduYcEbjwHvtE52U5DiGav7OBBal_J9I41usaeBfUHFUFoTiEyA8CZVbKpElrOCmslgAnJy24LLrVW_JCyskr8oBz2bKpPrBG4Kh2-YwibViok2ax22inJdfLHH8t26NrNfuHgz17wMaXoru9T0h1WbqKSp72rH7CR7nnXulcaCR5KY0WOuuM918jqg8Sj5ywnJH1LdLGi39_2AzfPzPvXNxN8TUl9hVOaUTZEfEgVeDS76S1kNZuy5L0YcHo9zrrnosIMLxm5YnKZ3ATB94MHsLGuRM72XvY29kRqBHWLA-GZQHIsN6zKXuL9DIgtwQnLxsjpW4GI-7E5yBfDJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینعلی شهریاری، رییس کمیسیون بهداشت و درمان مجلس جمهوری اسلامی، در گفت‌وگو با دیده‌بان ایران، با اشاره به ادامه «تعطیلی مجلس» گفت: «مجلس را بستند تا هر آنچه خواستند امضا کنند.»
او با تاکید بر اینکه تفاهم‌نامه با آمریکا در نهایت باید به تصویب مجلس برسد، افزود: گذشت آن زمان که برجام را در ۲۰ دقیقه در مجلس تصویب کردند. ما یک بار از این موضوع آسیب دیده‌ایم و نباید دوباره همان اتفاق تکرار شود.
شهریاری همچنین از اظهارات عباس عراقچی، وزیر خارجه جمهوری اسلامی، درباره احتمال رقیق‌سازی اورانیوم غنی‌شده انتقاد کرد و گفت موضوع هسته‌ای نباید در مذاکرات مطرح شود، زیرا به گفته او «جزو خطوط قرمز» جمهوری اسلامی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/VahidOnline/76515" target="_blank">📅 17:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76514">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lM5Erqfax9nx26WsAR_865OtRq3RWuG375rypNubW61goI2JgkPqtcZvZdg19vN6ttLNziQ3ZUE4jVF5dVXs_iAer4b1jKRwtMZHcGoqT_y9YtBVHSa4OKxsrGbfDHKH2ymNeepyzYi8K5SinLyBp6fCyrGHnLf4ieSutLd8MleCQW9ho0Gym7ZP_rS4b_Cuf4PX3QMtGH0ucMKzyXIadE6V1sr5LbTlsfqG4bBqFe2EV6yFBLkG6qvUXkahukon759tlLYx3A6-mM7ye3GcdR1hLYhzLJ9hObG3pN0WQmg-2QlMF_6uxtkRBJGchQ4hFGm5sYilMgmtfvrwOE9cfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام پیشین مرتبط با تحریم های ایران درباره «صندوق ۳۰۰ میلیارد دلاری»: پیش نیازش لغو همه تحریم هاست که دکمه روشن و خاموش ندارد
میعاد ملکی، مدیر پیشین «دفتر هدف‌گذاری تحریم‌های خزانه‌داری آمریکا» در یادداشتی درباره موضوع «صندوق ۳۰۰ میلیارد دلاری» برای ایران که بسیاری از کارشناسان درباره آن ابراز تردید کرده‌اند، می‌نویسد: با کنار گذاشتن موضوع معافیت/مجوز نفتی و نگرانی‌های مربوط به عدم اعمال تحریم‌های جدید، باتوجه به الزامات برای اجرای واقعی بند ۶ (صندوق بازسازی ۳۰۰ میلیارد دلاری) و بند ۷ (لغو همه تحریم‌ها) به این نتیجه می‌رسیم که مذاکره‌کنندگان آمریکایی یا می‌دانستند که توافق نهایی ناممکن است، یا این یادداشت تفاهم فقط تصمیم‌گیری را به آینده موکول می‌کند.
ملکی که خود در طراحی تحریم‌ها علیه حکومت ایران نقش داشته در این یادداشت می‌نویسد: این چیزی است که «اجرای کامل» در عمل، فراتر از امتیازهای هسته‌ای، به آن نیاز دارد:
بند ۶ — صندوق ۳۰۰ میلیارد دلاری:
صدور معافیت ریاست‌جمهوری از تحریم‌های الزامی بخش ساخت‌وساز ایران طبق ماده ۱۲۴۵ قانون IFCA (معافیت‌های ۱۸۰ روزه قابل تمدید که در هر دوره نیازمند اطلاع‌رسانی به کنگره هستند).
خارج کردن سپاه از فهرست سازمان‌های تروریستی خارجی (FTO)، زیرا در غیر این صورت سرمایه‌گذاران با خطر مسئولیت کیفری به دلیل «حمایت مادی» مواجه خواهند بود و هیچ مجوزی این مشکل را برطرف نمی‌کند.
استفاده از معافیت مبتنی بر منافع ملی در قانون ISA (قانون تحریم های ایران) برای سرمایه‌گذاری در بخش انرژی و نفت.
در نتیجه، هیچ نهاد سرمایه‌گذاری حاضر نیست میلیاردها دلار سرمایه را بر پایه معافیت‌های شش‌ماهه قابل تمدید متعهد کند.
بند ۷ — لغو همه تحریم‌ها:
ماده ۱۰۴ قانون CISADA (قانون جامع تحریم‌ها، پاسخگویی و واگذاری سرمایه‌گذاری‌های مرتبط با ایران) رئیس‌جمهور اختیار معافیت ندارد؛ تحریم‌ها الزامی هستند و لغو آن‌ها مستلزم تصویب قانون جدید در کنگره است.
ماده ۱۲۴۵ قانون NDAA (قانون مجوز دفاع ملی آمریکا) معافیت‌های ۱۲۰ روزه قابل تمدید که در هر دوره نیازمند ارائه گزارش اجباری به کنگره هستند.
تعیین بخش مالی ایران به عنوان «نگرانی پول‌شویی» تحت ماده ۳۱۱ قانون پاتریوت: این موضوع نیازمند مقررات‌گذاری جداگانه از سوی شبکه مقابله با جرائم مالی وزارت خزانه‌داری آمریکا (FinCEN) است و صرفا از طریق دفتر کنترل دارایی‌های خارجی (OFAC) حل نمی‌شود.
تحریم‌های مرتبط با تروریسم، حقوق بشر و موارد همپوشان با پرونده روسیه: هر کدام مستلزم اقدامات حقوقی مستقل و جداگانه هستند.
ملکی در ادامه می‌نویسد: «لغو همه تحریم‌ها» یک دکمه روشن و خاموش نیست، بلکه پروژه‌ای چندساله در حوزه قانون‌گذاری و مقررات‌گذاری است و کنگره نیز در آن حق رای دارد. و این پرسش مطرح است که چگونه می‌توان اتحادیه اروپا را وادار کرد محدودیت‌های مرتبط با ایران را که در چارچوب پرونده‌های مربوط به روسیه وضع شده‌اند، لغو کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/VahidOnline/76514" target="_blank">📅 17:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76513">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZoeW53iBL0ROeIEaMt8BSCPpSzsjruz7gZV6pizcpShFv3HezbtIJzrUAwV38mWFjg5JIy0N7SSatiN7E-CwK89jGmW4rIZbqNIsWu7sWceVivgEbSfXu7D33yswikkyGpLBqiKnHJM5V1FvdWs6SRevqGDl8wZHQ2e9qzla6KPoZe06QwDYbAuFD3uhu1mLyx1zGDJwcyqf7XH-HGWZl8icKYYDYJStC8km_31w-Hb9uHYUUAlZDSpWbTGLc2R8Ex_jxKnIpGcX20bipNz8qzN9yYpmz6yNP2AdhdaDmzcPJNKyzjCB62-W1j2JEOTLadELxnGuaQu82O7dmLkuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه هاآرتص در تحلیلی نوشت توافق دونالد ترامپ با جمهوری اسلامی، برخلاف انتظار بنیامین نتانیاهو، نه‌تنها به تقویت موقعیت سیاسی او منجر نشد، بلکه شکاف بی‌سابقه‌ای میان واشینگتن و تل‌آویو ایجاد کرده و نخست‌وزیر اسرائیل را در آستانه انتخابات با بحرانی تازه روبه‌رو کرده است.
روزنامه هاآرتص در تحلیلی نوشت نتانیاهو امیدوار بود سفر ترامپ به اسرائیل و حمایت علنی رییس‌جمهوری آمریکا، مهم‌ترین برگ برنده او در انتخابات پیش‌رو باشد.
به نوشته این روزنامه، نتانیاهو انتظار داشت این سفر پس از «پیروزی کامل» بر جمهوری اسلامی، سقوط حکومت ایران و انتقال ذخایر اورانیوم غنی‌شده برگزار شود، اما اکنون نه‌تنها هیچ‌یک از این اهداف محقق نشده، بلکه ترامپ تقریباً هر روز با اظهاراتی تحقیرآمیز از نخست‌وزیر اسرائیل انتقاد می‌کند.
هاآرتص افزود توافق آمریکا و جمهوری اسلامی در اسرائیل به‌طور گسترده «فاجعه‌بار» تلقی می‌شود، زیرا ترامپ برخلاف وعده‌های اولیه خود، جنگ را بدون تحقق اهداف اعلام‌شده پایان داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/VahidOnline/76513" target="_blank">📅 17:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4P250CZDMqX3GPUadbYrW6-l7GNygNmH7Jw9I-jgnWVhzKUzY4SDwvf2nttspg0yeT0h3YsbQKkOYA_vx7F2Pa4FAI-jaTOooyHz2vNijsXt8McuOFkC22ePWW7G5YbEry53cbk77-suNFpOAERhoKXJCyeOuAUSUQfJKuXg2TE-xQxmDskVn-Lo545VpcsbeRufOVTeokySSz0cpQciE-ZI7wUY08W7PZhqzB99PcibVkK2DGo3oGodRwReEqG-RYeoj8HOZuRsgHfiKJVzhHc-a4qgbiWBSyfJolrl-YClNW7oTxqwZF8SmV1mXwnWng64iPigvJW84lPqASl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«معین بصیری» ۲۱ ساله، ساکن شهرک اندیشه تهران، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ هدف شلیک مستقیم قرار گرفت و جان خود را از دست داد.
به گفته منابع آگاه، گلوله از نقطه‌ای مرتفع و از روی پشت‌بام شلیک شده و به قلب معین اصابت کرده است.
او در پی این جراحت جان باخت و پیکرش پس از انتقال به کهریزک، به بهشت زهرا منتقل شد.
نزدیکانش می‌گویند پیکر معین بصیری را از بهشت زهرا تحویل گرفتند و مراسم خاکسپاری او روز ۲۱ دی‌ماه برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/VahidOnline/76512" target="_blank">📅 17:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76511">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IM0ePqrFxrHudhTzuFLilMzL1C5dRhGWe5qsUBynsEj-wS9jLL_jAXfPETGq271JRfVqouZiIgBMYAGKE60MEnq0TC4DZJRXVegd1LS27AmciA9l8jDTl_H5d4im_rNC4U9dgeqCpPwySx3u4qVTP46reH8EIRko1JczOq6Sa9AwmLriAU_eiPRfHX3IgdJHTc-_3IL5MlqW9TGfN9DefeOWC2VaQUt7T1-Y5mWSFtVnv2q2HWsnxDYv-QeXqvib_vvn4iJYF1FQUaPSS6zGoZyERF1-xWpIH-nuZnNUiOb0M--X07tdCJAfGwBAIqF8ij19h-1Zgd05WP70yTHV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست‌های ترامپ، ترجمه ماشین:
«جنگ، ایران را تضعیف کرده است! ایران دیگر نه نیروی هوایی دارد، نه نیروی دریایی، نه تجهیزات ضدهوایی، نه رادار، و عملاً هیچ چیز دیگری هم ندارد؛ با این حال دموکرات‌های احمق می‌گویند ایران الان از چهار ماه پیش وضع بهتری دارد. اصلاً می‌توانید تصور کنید کسی با چنین حرفی قسر در برود؟ بعضی‌ها چقدر می‌توانند احمق باشند؟؟؟
رئیس‌جمهور، دی‌جی‌تی»
realDonaldTrump
«ما از سرِ درماندگی دیدار نکردیم؛ ایران بود که از سرِ درماندگی آمد. کارشان تمام است! این ۶۰ روز را هم طی می‌کنیم. هیچ پولی گیرشان نمی‌آید، حتی ده سنت!»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/VahidOnline/76511" target="_blank">📅 17:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76509">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XtHpLkcK2-DXWHMcIzPpz1qI-3Yl87hxxA18qOpR1HIY3sPIGnFh_GJ7zCMjEP1MXGq0Gndm1xYTcQtOvsoUgWs374Vx2HISG5hGdOmYQMPBwwCnE5s8bf6IV5MXwDC49yh4Q3E4Xqkt5pebsfso0V-gJVxV8jsRqIvS-UIZ3deet1NKtVfJnNoVM8907F4f8TGZ0dnpJKTg4f3bbPw4voQ3o-NL-eTviSkICHM79CkePuMj_dfIbqIVebZpdM36q3VVVvMTO6S0Myks9VXBlfX8HXg1Lg0aWLVr5hpbUllZUQ0QFB4R1yg3DBZ_s_rV1jW_gjQ1LMLFrNyeZlGuIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HMITvgy-4ovmjdOUoO9HkbkyrwDZzZ8GVroPJAZlBjM4rUpZauQhv8iDwiv_tV09Rz20vLBey3wegN2iethT_fMg7XJ7AdLODnqDKg6g9As1Q98_-ADqC57JyJ-q3FQBae0HTNj5A3w0YXkPEDebf9HymL4nV501OkLVE2rTi5KQ6DVl7e18rNIY9SyZS7S4JDvkNnGx-jilZHZgwSVrJ_9Y3tidfFX1smwJrXCyqmJJVRB5IOP7gMtzV8JgiT6OD0IlaGGpKFcATyV7ELOQczJudOySItx21COfHTZR58DcA-vOjk5s4tb3c0BuYG2aJWvRRC1n1117lZkXuNb6Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر خارجه فرانسه می‌گوید پاریس تا زمانی که اطمینان حاصل نکند مذاکرات درباره برنامه هسته‌ای تهران انتظاراتش را برآورده می‌کند، با لغو تحریم‌های شورای امنیت سازمان ملل متحد علیه ایران موافقت نخواهد کرد.
ژان نوئل بارو روز جمعه ۲۹ خرداد این موضوع را اعلام کرد. فرانسه یکی از اعضای دارای حق وتوی شورای امنیت سازمان ملل است.
بارو گفت تا زمانی که مذاکرات آمریکا با ایران به ابهامات مربوط به برنامه موشک‌های بالستیک جمهوری اسلامی و حمایت تهران از نیروهای نیابتی پاسخ ندهد، ثباتی در منطقه برقرار نخواهد شد.
او افزود: «ما به یک تغییر اساسی در رویکرد ایران نیاز داریم.»
@
VahidHeadline
وزیر خارجه فرانسه: کشتار معترضان دی‌ماه را فراموش نکنیم، مردم ایران بزرگ‌ترین قربانیان جنگ بودند
بارو که با تلویزیون «فرانس انفو» مصاحبه می‌کرد در پاسخ به پرسشی درباره سیاست فرانسه پس از «امضای تفاهم‌نامه پایان جنگ» ایران و آمریکا در قبال تهران گفت: «مردم ایران، بزرگ‌ترین قربانیان این جنگ بودند. آن‌ها از یک سو گرفتار سرکوبند و از سوی دیگر به رویشان بمب ریخته می‌شود. ما کشتار ژانویه (دی‌ماه) را که در آن خشونت دولتی بدون تمایز، معترضان مسالمت‌آمیز را هدف قرار داد، فراموش نمی‌کنیم.»
فرانسه حملات نظامی آمریکا و اسرائیل به جمهوری اسلامی را «غیرقانونی» توصیف و بارها اعلام کرد که در این جنگ شرکت نمی‌کند.
دونالد ترامپ تفاهم‌نامه پایان جنگ با ایران را در کاخ ورسای و در حضور امانوئل مکرون امضا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/VahidOnline/76509" target="_blank">📅 17:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAKvC-8XkyFmqV8SdmdWnKrNgUGj-VDk4g36H4xvk-kplluPE8v8lbPkbxnSorhOBar_Mp4eB9V0yFg7T2nvH_mZuunntRSiWL4jaVpPUiqkzUbYp06D4tdoC0ZlBsbjQw4l9Z1FUWxAJJv8i767jXnNhLBTwwgcLTMMnWGs46sxWv09kOcOGQTkkLvg9NzBbBHpS2Ekyhm-v6JZXT_dtF7VHPLojkpBeIHddMn5bs0y2V_m6HJ0UK1YLcZGGSHNFsKCGKk_YOk0VVo2SNJCT5DTJablMNjW8P4ng0mXiuzpwvOX8WtNGm05sRaMQYQhAXmvNnOXWP0L6grwM4o3gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال از قول منابع آگاه گزارش داده که طبق توافق پایان جنگ، ایران حق دسترسی به شش میلیارد دلار منابع مسدود شده در قطر برای واردات اقلام انسان‌دوستانه و غیرتحریمی از خود آمریکا خواهد داشت.
به گفته یک دیپلمات آگاه از جزئیات توافق، این منابع مالی به‌صورت مرحله‌ای و در بازه زمانی آتش‌بس تمدیدشده ۶۰ روزه آزاد خواهد شد و تنها برای خرید کالاهای آمریکایی قابل استفاده خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/VahidOnline/76508" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76505">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIJQ_XSbWXxEcv9MJuLAnHbzr1g28bJYWrFv46_xxKASFUkw6enkEu0WxtdYA5auwRSS8AGyeCu4Wst0-cdXEFk7W1jG_ed0CCFv5IC6iPqPQzBPC3P1Qxhs-Rzhvl5TKsW0QAOGmv_PT1rY6ijODnYWZ0_kbMWUFobiHAmnOsrfYJB-xG0mW_hrOy5vK59Rv6cgGyN_PvC6Q-SfKwTDbP7KhWQfImBa0-IY1IGNTcAMQXPUJ1ud-RwOjdwK3iD1jcWO6JC2F7bMZU9ivsXzDCy3Qz10gaRDdl0nOgzuqBynblHEWha3te2r4jhUAZWd7S-pH3igUS44Cjztm_WFjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNO2jBPqYn2U2AlB5LRB7qEvkHbigVnJgJs0H5bzBd_Vx2l3rHy8MdxQarVp9IxYGsyF5oj2W8TUFBe5rCoXHoMZKSpffV1vPnXwxNUV2xfkUXqWor3bCUQRtD9_IcihiiBXXborBM66CWJ4uniDExE4jYmeDYZD0o26bK7rn6PHHUKKI79VQZOwyRZrz1Pajrl4ITB5rCbGRh5lLPkdpOULPQ795IiU2uQIfgSekyDdseYyOiVhtvSNS1I_CvJFHMklKbELeRYh7MDXU8L9R_aSstfEi0gcTmaPHme83Yvhqaj4iIvQtOaXnId5pd4nE-0JZe4bj6dIqNeUV5mGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVsJJNy3E5A4GtK2BQRigly8zyMXesBsIi37zI9aaR4r_V2DW-HWjEv2A221N9dNxaT7Tavpx-1y0bbHt3t7L6pxAsTLjTPj9AGUy4Cailnb7Y13nsS3XId2esz9LdghUGTZrYz7I_3z56IHji3BExfMj71Rrlnwl4F6oHkm_rUJXtPEvxe2DJ7y4zryZgqK-CfegmLZIifD48bbgxA_CreRy-TVENxQYV2JpotDMpsc3eX_KXtsu0expl0P9CUaphzglRcFvhZLRIhXOIpZvcM0pWu-yNCd1_QIG7072c0gddL6eoxii80NQAvplHyrfF68E50jvXcBzNBmGyIKYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بيكر علی حسن‌پور را بعد از ۱۰۴ روز به خانواده
‏تحويل دادند
‏
🔸
⁧
#علی_حسن‌پور
⁩ در ۲۵ خرداد ۱۳۸۸ در خیابان آزادی تهران بر اثر اصابت گلوله به سر کشته شد. خانواده او پس از ۱۰۴ روز سرگردانی، سرانجام پیکر وی را میان اجساد مجهول‌الهویه پزشکی قانونی کهریزک شناسایی کردند.
🔸
اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است.
🔸
علی حسن پور یکی از این افراد است. سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/61687/ali-hassanpur
@IranRights</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/VahidOnline/76505" target="_blank">📅 17:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76504">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrX9U9gaIQ3Eg2Ukq38vSX7QZaluj191y4nZkU4mIaJfTKaZ0Hpv6OZVQuPv-kwLOVCdt6msB-HKZAUUx4TwfWE9RwqD4izBmFcOKM7PobJjhoZG5o98t3t_1PaCoYHwNPa1RyuHnD3_PkrGyVOMTBIo9pAvluNt36VXHRcP7cUaBxEWf93fmoIoVvZ4UvGDcS5visCzEHK0xJfrS9JjzMeik5Tb3mDOYTiisXeZXhjMJ7auFphFkCQbiNFYplOxiEr_l15nuxdE5A1pDeqKo-p8PYao1XipU_puR4Gxr8yfv-ZzjnQeWxNo_GXmGn3CElYhYIYnmRHKP0irk4c9QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ملی لبنان می‌گوید در حملات اسرائیل به شهرک‌های شرقیه، حاروف، کفررمان، کفرجوزو کفرصیر در جنوب این کشور دست‌کم ۱۶ نفر کشته شده‌اند.
به گزارش رسانه‌های محلی لبنان، از ساعات اولیه بامداد امروز، حملات توپخانه‌ای ارتش اسرائیل به شهر نبطیه و مناطق اطراف آن ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/VahidOnline/76504" target="_blank">📅 17:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76503">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xxe9ao1UnvQBPqj754jUEKYjPoB0wt2VwJX6O5lvlrGGU0QfeoG1ERTa2BTNTYGrXNUziT0wguMULEZiVQY0RZDhlVD4cm48h39P_SmEI5vDV8SvREFw-HLMwgkFn8ob-I7Dq6aWJ6lRvSvim74BED8U-dmdwQtTYZCv1KQovGYuvxF4fngOsPO5WFE6EiKAWYrvJmUop0ZfIE1Au4s3hmaJB__muZNVVYwQ1_F-AVnF947BEQpJAeA1zARUz_R2LHJlVFfin520xKW579_U4aL0IbtmZ77apCobIO39u4-_P3QeBY-FdiSE_--50NCxWwcC-p9ocxnJVPnLsy0u1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی اعلام کاخ سفید مبنی بر لغو سفر معاون دونالد ترامپ به سوئیس، وزارت خارجه این کشور اروپایی رسما خبر لغو سفر هیئت آمریکایی و لغو مذاکرات تهران و واشینگتن در روز جمعه را تأیید کرد.
لغو آغاز فوری مذاکرات بین دو کشور متخاصم تنها یک روز پس از امضا و رسمی شدن تفاهم‌نامه‌ای رخ می‌دهد که یکی از مهم‌ترین بندهای آن ۶۰ روز فرصت برای مذاکره درباره فعالیت هسته‌ای ایران است. قرار بود این ۶۰ روز بلافاصله در روز جمعه آغاز شود.
اما خبرگزاری تسنیم، نزدیک به سپاه پاسداران، روز پنج‌شنبه خبر داد که مذاکره‌کنندگان ایرانی پیش از آغاز دور بعدی گفت‌وگوهای صلح نیاز دارند نشانه‌هایی از اجرای توافق موقت از سوی آمریکا مشاهده کنند و هنوز تأییدی درباره سفر هیئت ایرانی به ژنو وجود ندارد.
در پی این انتشار این خبر بود که سخنگوی کاخ سفید هم در بیانیه‌ای که پنج‌شنبه شب منتشر شد، اعلام کرد ونس و هیئت آمریکایی آماده بودند به محض نهایی شدن برنامه مذاکرات، عازم شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/VahidOnline/76503" target="_blank">📅 17:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76502">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cEu90BI0WCXS5_WSeTPVFQkgGzPm7tAKHfLFy1UiP4LaFYq44mS-2kvOXwCsZN4JPUB-mADUAe9MBCrXQWvcf387RmsCBvxAALQyMPksSJBi_KjRoqBLXh0CqPFVfiSs9r0AaCGlalthVoHOseu2KETJvXImA8sWHtYzeDc108zdzz5Mh4fxyyp2uXwu22uJ1fXouTKXauWCCFgfMMA5vTHzMYTrO61HfTsnUhMZNjAd3kU6I2XprDgKUYnMaplocfJJ7MP91GeKoNsGdjXGzIFUbM_DJYW9D0pThhd9gc4iyeki8eataONh8hHqelBjUhYzQgWaDuD6j4nE1ZeOiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود قنبری‌راد، متخصص امنیت شبکه و از کارکنان یکی از شرکت‌های تهران، با اتهاماتی از جمله «اجتماع و تبانی علیه امنیت ملی»، «جمع‌آوری اطلاعات طبقه‌بندی‌شده» و «ارائه اطلاعات به اسرائیل» روبه‌رو شده است.
بر اساس گزارش‌ها، محمود قنبری‌راد، شهروندی ۴۰ ساله و متأهل، اردیبهشت‌ماه سال جاری در منزل شخصی خود بازداشت شده است.
یک منبع مطلع به دویچه‌وله گفته بود که او هیچ سابقه فعالیت سیاسی یا مدنی نداشته و به‌عنوان متخصص امنیت شبکه مشغول به کار بوده است.
گزارش‌ها حاکی است که او در تماس تلفنی از زندان، پرونده خود را «ساختگی» توصیف کرده و گفته است که برای پذیرش اتهامات تحت فشار قرار دارد. همچنین اعلام شده که وی از زمان بازداشت تاکنون از دسترسی به وکیل محروم بوده است.
بر اساس اطلاعات منتشرشده، محمود قنبری‌راد ابتدا حدود یک ماه در زندان اوین نگهداری شده و سپس به زندان فشافویه منتقل شده است.
همچنین گفته شده که او از نوعی اختلال عصبی رنج می‌برد و خانواده‌اش نسبت به وضعیت جسمی و حقوقی او ابراز نگرانی کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 201K · <a href="https://t.me/VahidOnline/76502" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76501">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Skpd1uFa5Tc5j7hEtON5W29k14gvEKlLIFYwfJ2MVR-8CzSEqUMUNzaS0OQ3uIG75pn3exggtUS0HUVjOw6tZ8v6ukajmRMWvk4PRxJor9i2AZKUYevNaOekskJam4-O1xJOFGEdVENjpHWr2O4VR2Ecnw1WMNk5N4VTif4rkVHhWoz8ZgsRnG6ZuWjFz_-CwTIGjhHI4YzlnQXZ96-q6Ja86NQSVXNWBiH5oBH5aUc3a70X7cJqo7bxQaEzZ_mlLDPAiNFSp-VYqWIzlorF9OOTEG20Lb_3r7rPhw43hertZjk3nNZych-9D_q39-Oov9-IO5C7scJEP92OXxRHiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از امضای تفاهم‌نامه میان واشنگتن و تهران  را
منتشر
کرد.
این تصویر مربوط به مراسم امضای تفاهم‌نامه در کاخ ورسای فرانسه است؛ جایی که ترامپ در حاشیه سفر خود به فرانسه و پس از پایان نشست سران گروه ۷ (G7) حضور داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76501" target="_blank">📅 05:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76500">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UWgk4x8EwIukcgcBfAx0K8coWjIY_rNd1BWcJDU5q-m5znUmqPxRQlElNclpac2OeMwrp4rh8XcYtBJkpEgdcJVjLUi23v_CRz-oQrAqs0rnmaMb4iern_FNaRdH3SqhEMs-yCcSYkX68pe2eO4ZCcIpTitY0XbGcfCz6Tvu9_u3m4-nlQZyfTGS-H0Qokrha32owTId6IV_zDkmjZXozll69Zo5dUJNg29V4QVse_7Zk5TnDwZN1GpQejNPyn6N1WJPa48oixC5fBpWNEt3EcEwErCIB1czkemn5FgJTmLGqq4TJTGYjeoyxe884yAVKQKt45h4rR_Oi-2XyhgSoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در«گفتگو ی تصویری با اکسیوس» گفت یادداشت تفاهم امضاشده با حکومت ایران را می‌توان «نوعی تسلیم کامل» از سوی تهران دانست.
او این اظهارات را در پاسخ به پرسشی درباره تفاوت میان خواسته پیشین خود برای «تسلیم بی‌قیدوشرط» و مفاد تفاهم‌نامه مطرح کرد.
مجری آکسیوس در این مصاحبه به ترامپ یادآوری کرد که در آغاز درگیری‌ها گفته بود تنها «تسلیم بی‌قیدوشرط» را از ایران خواهد پذیرفت، اما یادداشت تفاهم امضاشده چنین تصویری را نشان نمی‌دهد. ترامپ در پاسخ گفت: «خب، احتمالا در واقع تسلیم بی‌قیدوشرط است. فکر می‌کنم همین‌طور باشد.»
رئیس‌جمهوری آمریکا همچنین با اشاره به جنگ اخیر گفت ایالات متحده ایران را «کاملا از نظر نظامی شکست داده است». او با تمجید از توان نظامی آمریکا افزود واشینگتن توانست محاصره دریایی موثری علیه ایران اعمال کند و هیچ کشتی‌ای نتوانست از آن عبور کند.
ترامپ همچنین گفت پس از جنگ با ایران، محدودیتی برای قدرت خود نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76500" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76499">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TUOCZG2NdhOHiK019PLRj-exDCqO-hO8tjvMtw6wSAG_6LK4gEFcHVIRWD8uLBh10s6B7yJgXWX5Mi9UC0SeLyRKCbmuAK95xLVSnCX7s1ZML0Ks07te4LhmHzkGfkvezd-NZDk2hw61sD0TGBUA1uuY_CdAq_qrG_fkGsk7UerL9yReWScglvrQ1katYfxhBXQO2sh2ocCO33UOYIDwhCnZJn-FsDmXpR1M16rG23BqyI2Z_Bb_WFJT3rI8PNJSr2gY_SNmU2bVdX7My8ytILKJGFvrJzYp44qInumofypBghRyLew3grLbfAyq4vJ0eMy2w1TZrATm1zfj8RLzuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دفتر جی‌دی ونس، معاون ترامپ، در اطلاعیه‌ای اعلام کرد که او سفر خود به سوئیس برای شرکت در مذاکرات با جمهوری اسلامی را لغو کرد، زیرا برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و تدارکات و هماهنگی‌های این مذاکرات ساده یا قابل پیش‌بینی نیست.
در این اطلاعیه آمده است: «برنامه‌های مربوط به گفت‌وگوهای فنی پیش رو هنوز نهایی نشده است و هیات آمریکایی آماده بود در نخستین فرصت ممکن عازم شود، اما تدارکات و هماهنگی‌های این مذاکرات هرگز ساده یا قابل پیش‌بینی نبوده است. در حال حاضر، معاون رییس‌جمهوری امشب عازم سفر نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76499" target="_blank">📅 05:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76498">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BP8Vh3IY8lLpyggUMo36eD8W8wQeqYJ5v9Zm2THUJ4N2Iew7-_eMWAnF6lscJzcxpQ6_4GR5r661cjkG80hewHkUDS3rRnIP4h_r6qatTX423zayaHZyHsLkhuubNombzIbYXvZsMf834Zn1DI6MfRKPc3Nhj_LXW0Kf6KK2uwXxlXEfeoMt4WOSsssKcOaiTJ6DRU9VKMX13E2sjFygsyQEnZXLKywzfuvNJTV5Za6TLNjobgXylrbbCgesK9hWLdUcWC4deUq_SuaAKN2dEdUnNiR1NwvwLPyJ05j3QKpnr_9Dhr24VhMnnGTN-qLO2t4_S_rTiRezAMUOZ-3Bng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آسوشیتدپرس گزارش داد استیو ویتکاف، فرستاده دونالد ترامپ، پنجشنبه‌شب در نشستی غیرعلنی با قانون‌گذاران آمریکایی اعلام کرده است تهران از آژانس بین‌المللی انرژی اتمی برای بازرسی از تاسیسات هسته‌ای خود دعوت خواهد کرد و روند شناسایی محل نگهداری مواد غنی‌شده را آغاز می‌کند.
بر اساس این گزارش، ویتکاف به رهبران کنگره و اعضای کمیته‌های امنیت ملی گفته است تفاهم‌نامه میان آمریکا و ایران هیچ توافق جانبی نداشته است. با این حال، تهران و آژانس بین‌المللی انرژی اتمی نامه‌ای جداگانه تنظیم کرده‌اند که در آن دعوت از بازرسان آژانس و ادامه همکاری‌های نظارتی مطرح شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76498" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76497">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siuihYPvKoPrBLFObLqodneyFgvS9rP4wkVkwnZd5CGmhFeSE5rSwYaYaDltI3nA9aTVnZR2KdtGVicvRvKnzCP_AEkDZCsegSR5UUUhT1sHNcu-4MKLn6jPJK4g902j35mjFL0BnEDsbz3a8-7X-scqcU8dnUer5vtdrMNoMf2rMmti0hxxNWhEhKWwqZ_BoUyovp4CfsduX3AOLjXGqVZUmhAY4Max1HqooMJp0c89Oe3eDl-hGmaKotrPZh6gWv2wipBy5O06hq5fRkYLTjsR3bSlYLpCHSm7fjJ1IjaD5AL8XLwFAuj89Ig3-Hm7zKNOLdRE97Dv7JNnf7Tulw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجه اتحادیه اروپا، گفت هنوز برای بحث درباره لغو تحریم‌های اتحادیه اروپا علیه ایران زود است و این موضوع پس از دستیابی به یک توافق هسته‌ای با ایران بررسی خواهد شد.
او پیش از نشست رهبران کشورهای عضو اتحادیه اروپا به خبرنگاران گفت: «زمانی که شرایط فراهم شود، کشورهای عضو درباره مناسب بودن لغو تحریم‌ها گفت‌وگو خواهند کرد، اما هنوز به آن مرحله نرسیده‌ایم.»
اتحادیه اروپا در حال حاضر مجموعه‌ای از تحریم‌های چندجانبه علیه بیش از ۷۰۰ فرد و نهاد در ایران اعمال کرده است که شامل ممنوعیت سفر و مسدود شدن دارایی‌ها می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76497" target="_blank">📅 00:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76496">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pU-_LHOhfrk-3snpx7tSpQ2kOF00VzoAEtyXOwcWAvo2w7LJcfy8wULuHEOG-pTXUPHl5DBvEo5LLa9Xp4x6EL4huC8t9OF7V9NwKxVtRW6EEFFbe2YunVXMGDnOp8zyPYGfLCmI7bmAXm1T3YCcLkdjSljrvzxP9HbtGX0zQNKwM0e6wzUjvL3Y6VXiuazu3VBH_rLuHml_uRvBbb46IF3nbClN8lCuYhqJBYBNK83lssRovkH0V8qKOHEiy8d07LeEi8jY6sms9LRGy_3uH15Zknn15EQOYR-VN_fOn5frRAUhDoy7nHUCncFKGcre1DLGccNbObjmnubQEOKQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین به نقل از یک منبع آگاه گزارش داد هیات مذاکره‌کننده جمهوری اسلامی به دلیل ادامه حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس برای آغاز نخستین دور مذاکرات ۶۰ روزه را به حالت تعلیق درآورده است.
المیادین افزود: تهران پیش‌تر به آمریکا و میانجی‌ها اطلاع داده بود که پرونده لبنان در ادامه یا توقف مذاکرات نقشی محوری دارد و هشدار داده است حملات اسرائیل تا عمق ۱۰ کیلومتری خاک لبنان نقض یادداشت تفاهم و توافق چارچوب است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76496" target="_blank">📅 23:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76495">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WuWt7lkTqxwCIsxAnQBuOEWlqQn8AFwwxcqaNe82lWU79DMCxTaGg41FC3_1bVT3Uu55mlHHSYDOWSjyDpBR4ck-WT9_Slm_4555sFEe1iv9d_cPwr4KV4oYS84Y_V6qYZ7SRE4-IpeXpA17efldrmIc5KS4-qDI_KQ_k2fQCSXk0WYbCRUukl0zK3G2shp66GK2NjqFXcr3wHkoOTjgcBjToZcRi_xX-p9oFhobLjkAmMsQjGz3sto7togkUhqDabwY-iypirNoawCil_ltrMab3xXaOmFuN1M0cVpt6q4W_MQWM8hjNJhVzNS7YnfcCjm2c22EuxMTwxWM0b9lZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت کاخ سفید:
رئیس‌جمهور دونالد ج. ترامپ تهدیدی را حل کرد که واشنگتن چهل سال صرف مدیریت آن کرده بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
یک پیروزی برای آمریکا.
🇺🇸
WhiteHouse
ترجمه با هوش مصنوعی به تصویر اضافه شده.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/76495" target="_blank">📅 22:49 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76494">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JgQBzeRFK5BBc0OxL7ahEc4XC7e2rlMHeefO8yTu2SgiUl5BJ9bgIH5ONBn4_WRhZszLbMPUidNpBWT8m19ZE8VURcsyR3k1pU4d6VT8xFN1-dXaydzrwy-0Cwq_hl38T_74W0OXNfFa3jx-TCqf_8UDlWeUkiCUdJgDLv0nP2VF_E2ZwbtRe9rVFFpYsPvU6n-rcnUItxI2i3X1cd5estyzELFSpdqajvnzdLO457EiHgJG5wJslkLGHjSmRLfW9SKGfU8AxLcGTI-jfmKr656HHVo1vaAZuMa0RQRiyn-5Vx6pPwm8m1gjXS0uuF1dz6gx0yUhcNWYGUGV7S1ZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'
بیانیه شورای عالی امنیت ملی
'
منابع حکومتی:
🔹
در اجرای بند ۵ یادداشت تفاهم اسلام‌آباد، کشتی‌های تجاری متقاضی عبور از تنگه هرمز باید درخواست خود را به مدیریت آبراه خلیج فارس (PGSA .ir) ارسال نمایند.
🔹
به موجب یادداشت تفاهم اسلام‌آباد، به مدت شصت روز، هیچ‌گونه هزینه‌ای از متقاضیان اخذ نخواهد شد و این هزینه‌ها توسط دولت جمهوری اسلامی ایران تأمین می‌گردد.
🔹
بر این اساس به مدیریت آبراه خلیج فارس دستور داده شده است، در جهت تحقق اهداف تفاهم‌نامه درخواست‌ها را با سرعت و اولویت رسیدگی و پاسخ دهد.
🔹
با توجه به شرایط خاص و وجود برخی مخاطرات ایمنی در مسیر عبور و به دلیل لزوم حصول اطمینان از تردد ایمن و جلوگیری از حوادث دریایی، لازم است کشتی‌ها در مسیر و زمان اعلامی به آنها عبور نمایند تا به تدریج، امکان تردد افزایش یابد.
🔹
ترتیبات اجرایی و جزییات فنی عبور از تنگه هرمز از طریق مدیریت آبراه خلیج فارس اعلام می‌گردد.
🔹
در خصوص سایر موضوعات، از جمله مین‌زدایی، اقدامات لازم مطابق بند ۵ یادداشت تفاهم اسلام‌آباد انجام خواهد شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76494" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76493">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bhHnFUDQ6YCwZQIRT5Mdh4E_opZcbnfesvNF7PpJlyb9h89KzzAhuT0kX90cB0boyVpPurbbckqTs4CusVc7GLPxo6ZWt0JqAwXjajv_Ky9ZQRe5piRpJJANgMNDQoqpQszX7Oqh704MlJyyj45Qtie-oi3wui1XZ--2i5a0jUXMxCea1G715zsxBjqrD3jm5f-xlSuV0evstQlec0YI6z92aWCSTH_D4ephJwMrOlB2afp0HTHP_LMjGMalPwk0jba4b2cq1n9Kg-KSAYnYcGBwdtkKdTC51kLykUBb65yKbsGhZSJQKXfsimE43O8K-t6SETbX-w-jI2HZNNsjUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: انتظار آتش‌بس کامل در همه جبهه‌ها از جمله لبنان را دارم
ترجمه ماشین:
ایالات متحده به صلح متعهد است و ما همه در منطقه خاورمیانه را تشویق می‌کنیم که به تعهد خود برای فراهم کردن امکان پیشرفت زیبای مذاکرات ما پایبند بمانند.
بازارها از آنچه در حال رخ دادن است استقبال می‌کنند: قیمت نفت به‌شدت پایین آمده و سهام به‌شدت بالا رفته است.
ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76493" target="_blank">📅 22:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76492">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPourostad وحید پوراستاد🔷(Vahid Pourostad)</strong></div>
<div class="tg-text">« پیام منتسب به مجتبی خامنه‌ای در واقع نوعی فاصله‌گذاری حساب‌شده با تفاهم ایران و آمریکا است. مجتبی خامنه‌ای رهبر جمهوری اسلامی اجازه امضا را داده، اما مسئولیت سیاسی و اجرایی آن را بر دوش پزشکیان و شورای عالی امنیت ملی گذاشته است.
پیام همزمان رو به داخل و بیرون نوشته شده است. در داخل می‌گوید رهبر با رضایت کامل وارد این مسیر نشده و دولت باید پاسخگوی نتیجه باشد. در برابر آمریکا هم این سیگنال را می‌فرستد که تفاهم، زیر فشار ترامپ و دولت او به‌معنای عقب‌نشینی قطعی نیست؛ بلکه مشروط است و اگر شروط ایران محقق نشود، موافقت نهایی رهبر با توافق نهایی هم تضمین‌شده نخواهد بود.
در واقع متن، بیش از آن‌که اعلام رضایت از توافق باشد، تلاشی برای حفظ دست بالا در مرحله بعدی است: هم مسیر مذاکره باز می‌گذارد، هم امکان عقب‌نشینی تبلیغاتی حفظ می‌شود, هم به واشینگتن گفته می‌شود که فشار بیشتر ضرورتا به انعطاف بیشتر ایران منجر نخواهد شد»
@pourostadv</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76492" target="_blank">📅 22:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76491">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P0DaY-3K-Jn7yBvHiNRvEUSoZN-Zx6_bmg28Gbn8RmQJJ7eGU91yQx7ag8uOCzKuKpV8uQ602UIN9CARKWHMr77unOnJgOkjOsGn4A7LoisOeu8Zftqf-t9HGbMNlMp4Ii39Norddt7GgNDuaezBaWSNxdXiATI6b6Fb0s1iysQL8DDk1ErPIzlkekRvJ3mh8tAnAI4_adP3eNb3eKVcQ9c4biRWPeEHWWnTNYfWoa5mbH8cJdEQYgxpVQ699PnfWDO0HLxKUF4wdOb99xrxAEbrKd1s9M0r4RsRmU6eDjh-laoP2d2rWmJc-42BKXSbJWZhFtnNPO3EdYX3ssuGEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسئول
گردن‌نگیر
جوان شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/76491" target="_blank">📅 21:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76490">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VtAN2pfoW_CiinvzNTJgj0FV5HTK6FK8p_elBPEYkOIlUg2ns_4RLxa7n9lkADOMNKWqdFGg53zXSsUJtyXeefBnf4rL2asPkkpUX16-h_ZNNgjB9y80ZTYFCuaYhzisKFg_L9h2OvWgSDwYtd45GZHezDi2BRQgg-kYZ5VH724tHnmys9vW0oz0sStKZrKXEFLWCuqJqIE_CMpcXXYWlpGeHzTCb5FXX633UXV1TFWMrBefK_o9r71wYAnrKuu876NVPvkSJRuABSRiTs6-TSB7fycFJYE907g7bF7HIN_v_vcqIay7zJeXnrPU5XuFp1kxwzaZCahTW4yxGkolDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پنج‌شنبه شب متن پیام مکتوبی منسوب به مجتبی خامنه‌ای را منتشر کردند که در آن رهبر جمهوری اسلامی درباره امضای تفاهم‌نامه میان ایران و آمریکا گفته است که «نظر دیگری» داشته و مسئولیت آن را بر عهده مسعود پزشکیان، رئیس شورای عالی امنیت ملی، و دیگر اعضای این شورا دانسته است.
در این پیام درباره توافق با ایالات متحده آمده است:
«بنده علی‌الاصول، نظر دیگری داشتم ولی از باب تعهدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیت ملی از طرف خود و سایر اعضا در پاسداشت حقوق ملت ایران و جبهه مقاومت به بنده دادند و تصریح به قبول مسئولیت آن نمودند، اجازه آن را صادر نمودم‌.»
در این پیام به تفاهمنامه اخیر به عنوان «تفاهم‌نامه‌ای بین رئیس‌جمهوران ایران و آمریکا» اشاره و گفته شده است که رهبر جمهوری اسلامی و مردم از این لحظه «منتظر تحقق شروط گفته ‌شده» خواهند بود.
در این پیام آمده که مذاکرات حضوری آینده «به معنی پذیرش نظر دشمن نخواهد بود.»
VahidOOnLine
در تیتر و متن نامه و خبرهایی که درباره‌اش تولید میشه بسیار تاکید دارند که این تفاهم‌نامه‌ای بین پزشکیان و ترامپه و نمی‌گن بین ایران و آمریکا
در واکنش‌ها از کوچک‌نمایی نقش
قالیباف
یا محافظت ازش با سپر کردن پزشکیان هم میگن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/76490" target="_blank">📅 21:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76489">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/elNwgC8nw2RVzRm8jeD4NvCuoW0w0cusC-gVeGi9fPu574kNa5HSD50gB6bRdevn-QczxLZ8t4MFs3Fv4eI-n8x_4Dfj8h3hS49pfBHxy1Ndsq-EFTL3IyIAMcr7lVQ-cByBYR883my5cr3GDlKkDQu1XiV1K2BvJ5mjbD2XIYHLDje_7CFuoB94STEqhNZJgtwQIfVz70ID7aZdrlnucNGJUTui-zNnQkNLR_c6nUL1q4FlUD5m70dtqTKW0QdPSXhdCbAMX-lhZIKaMoADK6rLi_e88_xt4Zi8xnV5KKA4mpHgVVnzzZnOwWkB-O2JI_w-10HXPpZX4B5DvsBKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران در کار نیست.
این خبر جعلی است!
تنها چیزی که نصیب آمریکا شده، موفقیت، کاهش قیمت نفت و پیروزی است.
بازار سهام را ببینید.
تبلیغات «دُمکرات‌ها» در جریان است!!!
رئیس‌جمهور دی‌جی‌تی
(توضیح: Dumocrat بازی زبانی تحقیرآمیز با Democrat است؛ از ترکیب ضمنیِ dumb به معنی «احمق» و Democrat. در ترجمه می‌شود چیزی مثل «دُمکرات‌ها» یا «دموکرات‌های احمق» آورد، بسته به لحن مورد نظر.)
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76489" target="_blank">📅 20:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76488">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gYrXOmu6zTG4g_YioYI9emSJeGuzrd1PNZUCy1H200tOYd72UYVxRkB2YDAoM6N0xWd17eQu-pWHgMsG_mvzbk7lxRKoLAWmvyAHu9VlgkarryMJGMruugYJVXMvkZei48kwLedpYrxrsGcddDttHIyLPnLP7nn7TXoU3GRcHdUgCTbkbRVdPXfzwPO6GixpWplpE92SzOCZZeGg_zMZInP7z10JqVed5cyCwDcQmIxnhytAcUBwmfp5iP-Ia8T0ZNCvO5MFDc4ZhSbELf2t0gjGzl6k7xnVC2xDzlOFD_V5Bt8J2nNyk2u-8KVWKjus_jJlX8dOSktbmtMLHkZM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام پایان محاصره دریایی
پست سنتکام، فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
امروز، نیروهای آمریکا مطابق دستور رئیس‌جمهور، محاصره‌ی همه‌ی رفت‌وآمدهای دریایی به مقصد بنادر و مناطق ساحلی ایران و از مبدأ آن‌ها را رفع کردند.
نیروهای آمریکایی مانع عبور کشتی‌ها به سوی بنادر ایران در خلیج فارس و خلیج عمان، یا خروج از آن‌ها، نمی‌شوند.
همه‌ی تلاش‌های نظامی آمریکا برای اجرای محاصره متوقف شده است.
کشتی‌های بزرگ نیروی دریایی ما در منطقه‌ی کلی باقی خواهند ماند تا اطمینان حاصل شود که همه‌ی جنبه‌های توافق رعایت، اجرا و به‌طور کامل لازم‌الاجرا و مؤثر باقی می‌ماند.
CENTCOM
البته سنتکام ننوشته خلیج «فارس»
🔄
آپدیت:
توییت رو ویرایش کردند و در نسخه جدید اون جمله مربوط به خلیج فارس رو کلا حذف کردند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76488" target="_blank">📅 20:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76487">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JrdppuD07m0jq0zLy3a7wUIgVDH8_z_7ET8lCFsLaqNHDvJqzX9wnoSAwtI-wZhrqQPvpgaxGT1sZX_ETXhG4aeeIit-ZkvtNy8Shyzy-5URUdyGS_66ft6nbO-9YZKaXIw6koBZxznkrMCy3gfuQVmX7KT9ezmra9A7PlRvYsIDpQsWC9jsv5orgrrWOSWUbxxR2FLymTcSN_YDrWPHqUPi0kZzXyiz0AK1NY4IDgur-YcjBdEdzVCV2CYywH_cwRh-z7galCzO2u3qDuZNXwIch6L4hGHA0eMHk-LqP5h-64ZkAk46zaW0ah9CNX-FshXCIpbrqHPkducuewoK7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره: ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار. realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/76487" target="_blank">📅 20:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76485">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=dlSRKIHfyfWwN_7Gh7gfZt-3pBYsGjf_6ftYA7B2Bjdyczlgh2ukEpDlSGwvflHL3pLkDSWHtCsyu4F5Ny4R2cFFO0uTaocvhppX95tswYowyPt59KaWSphCGjXx897DVF09-bFtgrkKIpHQQezYUjX1RCTVt400OCBRPQP5Abmsfs8ugQqvNU_MBHuxEezEP43U1h-WrLKKHTN3q9iD1JID4bR_EMSj9_QeymF2pebaDyTs3N7RmC2pu1A4egC4Gs-SkoGFwY9GwMadYCk9UFSJEkTeGXhegtwz6UaJh4Hhqmp4ydiHsr2fOKBFX4O6ov8J5y9YKGwLZU8zd_V3UA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d4e8375c.mp4?token=dlSRKIHfyfWwN_7Gh7gfZt-3pBYsGjf_6ftYA7B2Bjdyczlgh2ukEpDlSGwvflHL3pLkDSWHtCsyu4F5Ny4R2cFFO0uTaocvhppX95tswYowyPt59KaWSphCGjXx897DVF09-bFtgrkKIpHQQezYUjX1RCTVt400OCBRPQP5Abmsfs8ugQqvNU_MBHuxEezEP43U1h-WrLKKHTN3q9iD1JID4bR_EMSj9_QeymF2pebaDyTs3N7RmC2pu1A4egC4Gs-SkoGFwY9GwMadYCk9UFSJEkTeGXhegtwz6UaJh4Hhqmp4ydiHsr2fOKBFX4O6ov8J5y9YKGwLZU8zd_V3UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی در ایران که ریاست هیئت مذاکره‌کننده ایرانی با نمایندگان آمریکا را برعهده داشت، عصر چهارشنبه در مصاحبه‌ای مفصل با تلویزیون حکومتی در ایران به نهایی شدن تفاهمنامه میان تهران و واشنگتن واکنش نشان داد و آن را موفقیتی بسیار بزرگتر از مقابله نظامی با ایالات متحده دانست.
او در مورد دستاوردهای ایران گفت: «هر آنچه را که با اقدام نظامی می‌خواستیم به دست بیاوریم، چندین برابر آن را از طریق مذاکره گرفتیم؛ اصلا قابل قیاس نبود. هر جنگی ممکن است پیروزی‌هایی داشته باشد، اما اگر این پیروزی‌ها در نهایت به یک سند حقوقی و سیاسی منجر و ثبت نشود، هیچ منفعتی نخواهد داشت.»
او در بخشی از صحبت‌های خود درباره انتقام کشته شدن علی خامنه‌ای گفت: «همان‌طور که خونخواهی امام حسین، ظهور امام زمان است، خونخواهی رهبر شهید هم آزادی قدس است... صد نتانیاهو بند کفش امام شهید ما هم نمی‌شود.»
قالیباف در مورد وضعیت تنگه هرمز هم گفت: «تنگه هرمز هرگز به شرایط قبل بازنخواهد گشت. البته این به آن معنا نیست که ما در تنگه هرمز بخواهیم برخلاف قوانین بین‌المللی و مقررات دریانوردی عمل کنیم.»
@
VahidHeadline
قالیباف در مصاحبه‌ای که همزمان با انتشار مفاد تفاهم‌نامه تهران و واشنگتن از صداوسیما پخش شد، گفت برای حضور در مذاکرات با دولت دونالد ترامپ تمایلی نداشت و به دلیل نقش ترامپ در کشتن قاسم سلیمانی، «کراهت شدید» برای ورود به این روند احساس می‌کرد. او افزود که با وجود این مخالفت شخصی، به درخواست مقام‌های جمهوری اسلامی مسئولیت مذاکرات را پذیرفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/76485" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76484">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzfSWIzEyhPKneuIC-w79XZCXxYsttRCMjtV7565hZ0ZYTuz3vMs2MKjMgM6_a_IFh8wlzr7cO30xuB132BKXUlM1FlcUrk5gwv5KXxfudHzx_6f3cR2GCh1eBUOrZk_A7xRQqbGRHtehSbKhzDVMy0Tviv2f5AGf7dpJKCq4fbyDOQwXiZh_DByF-sUX8o4xYhZ6BAaCIztYxlHqobsxdE4HACiKiCoWENxQiGze5K0VTx2fLv3R94jvoT70vm0_TCkydHInpTszG5qos-aUASA41J8RP3sne_6u5O60QxC20z1kluiEynnzcli39dQ-0HtDSVxHsjrdr3pBKaYmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، یک روز بعد از امضای تفاهم‌نامه ایران و آمریکا در نخستین موضع‌گیری خود اعلام کرد که نیروهای اسرائیلی از جنوب لبنان عقب‌نشینی نخواهند کرد و تا هر زمان که لازم باشد منطقه حائل امنیتی خود را در آنجا حفظ خواهند کرد.
این اظهارات پس از آن مطرح شد که دونالد ترامپ، رئیس‌جمهور آمریکا، طی روزهای اخیر از عملیات اسرائیل علیه حزب‌الله لبنان انتقاد کرد و آن را بیش از حد «تهاجمی» دانست.
نتانیاهو در یک مراسم رسمی گفت: «ما امنیت و رونق را به شهرهای شمالی بازخواهیم گرداند.»
او افزود: «این امر مستلزم حفظ منطقه امنیتی در جنوب لبنان است؛ مستلزم آن است که آنجا را ترک نکنیم، تا زمانی که نیازهای امنیتی اسرائیل چنین ایجاب کند.»
رسانه‌های رسمی لبنان پیش‌تر گفتند که در حملات صبح پنجشنبه ارتش اسرائیل به جنوب لبنان، ساعاتی بعد از امضای تفاهم ایران و آمریکا، سه نفر کشته شدند.
از سوی دیگر، یک مقام ارشد اسرائیلی پنجشنبه به خبرگزاری رویترز گفت که اسرائیل «در حال انجام مذاکراتی سرسختانه» با ایالات متحده دربارهٔ موضوع ادامه استقرار نیروهای اسرائیلی در جنوب لبنان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/76484" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76483">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شروع سخنرانی جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
🔸
دیشب، ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرد.
این بالاترین میزان از آغاز درگیری است.
🔸
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آنها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است که دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به تعهد خود عمل می‌کنیم.
🔸
شما چیزهایی درباره ۳۰۰ میلیارد دلار یا ۲۴ میلیارد دلار، یا این یا آن عدد یا مقدار پول خواهید شنید، و واقعیت ساده این است که تنها راهی که ایرانی‌ها به هیچ یک از این منابع دست پیدا کنند — حتی یک سنت، به هر حال، از ایالات متحده آمریکا تحت هیچ شرایطی — اما
تنها راهی که آن‌ها می‌توانند از این معامله بهره‌مند شوند این است که کاملاً مطیع باشند و رفتار خود را تغییر دهند.
اگر ایرانی‌ها رفتار خود را تغییر ندهند، برنامه نظامی و هسته‌ای آن‌ها همچنان نابود خواهد شد؛ اگر رفتار خود را تغییر دهند، آنگاه رابطه‌ای تحول‌آفرین با خاورمیانه خواهند داشت.
این یک برد-برد برای ماست.
🔸
در ایران تقسیمات واقعی وجود دارد.
آنچه دیده‌ایم این است که عمل‌گرایان در حال پیروزی در بحث هستند.
🔸
من کسانی را دیده‌ام که به این توافق شک دارند — افرادی می‌گویند ایرانی‌ها هرگز رفتار خود را تغییر نخواهند داد.
خب، شاید این درست باشد، و اگر چنین باشد، آن‌ها هیچ‌کدام از مزایای این معامله را به دست نمی‌آورند. اما آیا ارزش امتحان کردن ندارد؟
🔸
می‌گویم دوره ۶۰ روزه رسماً امروز شروع شده است.
پس بله، توافق دیروز شروع شد — ما امروز ساعت ۶۰ روزه را شروع خواهیم کرد.
🔸
تمام چیزی که رئیس‌جمهور دیروز گفت این است که، البته، کشورها حق دفاع از خود را کنار نمی‌گذارند.
اسرائیل حق دفاع از خود را کنار نمی‌گذارد اگر حزب‌الله به اسرائیل راکت یا پهپاد شلیک کند.
ایرانی‌ها حق دفاع از خود در کشورشان را کنار نمی‌گذارند، اما
ما انتظار داریم که به عنوان بخشی از توافق نهایی، آن‌ها نتوانند موشک‌هایی بسازند که بتواند به طور گسترده کل جهان را تهدید کند،
و این همان چیزی است که رئیس‌جمهور ایالات متحده دیروز گفت. و ببینید، خیلی ساده است: نمی‌توانید به کشوری — چه اسرائیل، چه ایران — بگویید که حق دفاع از خود را نداشته باشد.
🔸
خبرنگار: رئیس‌جمهور ترامپ دیروز گفت که اگر مذاکرات این دور به مشکل بخورد، شما را مقصر خواهد دانست. آیا نگرانید که او شما را به عنوان مقصر معرفی کند؟
جی‌دی ونس: نه، اصلاً. فکر می‌کنم رئیس‌جمهور شوخی می‌کرد، همان‌طور که اغلب این کار را می‌کند.
🔸
جی‌دی ونس درباره تنگه هرمز:
ما هرگز نمی‌خواهیم این اتفاق دوباره بیفتد، درست است؟ این موضوع مربوط به عوارض نیست.
این درباره اطمینان از این است که تنگه‌ها هرگز به عنوان نقطه گلوگاهی برای اقتصاد جهانی استفاده نشوند.
صادقانه بگویم، این چیزی نیست که ایرانی‌ها بخواهند.
🔸
جی‌دی ونس درباره برداشتن تحریم‌ها:
صادقانه بگویم، ما این را به عنوان امتیاز بزرگی به ایرانی‌ها نمی‌دیدیم — ایران... این را به عنوان امتیاز به آن‌ها نمی‌دید، چون چیزی که مانع فروش نفت آن‌ها می‌شد تحریم‌ها نبود.
آن‌ها بدون هیچ تخفیفی مقدار زیادی نفت می‌فروختند، چون تحریم‌ها اساساً بی‌اثر بودند.
در آن زمان، کاری که تحریم‌ها انجام دادند این بود که سیستم مالی ایران را به نوعی به سیستم بانکداری سایه‌ای منتقل کردند.
با برداشتن تحریم‌ها، ما در واقع قادر خواهیم بود کمی ببینیم که سیستم مالی آن‌ها پول را کجا می‌فرستد و از کجا دریافت می‌کند. این یک مزیت واقعی است.
🔸
آنچه به برخی از منتقدان توافق که شنیده‌ام می‌گویم، کسانی که می‌گویند «خب، ایران تمام این مزایا را به دست خواهد آورد».
تکرار می‌کنم آنچه را که گفته‌ام و احتمالاً باید چندین بار تکرار کنم: مزیتی که ایرانی‌ها به دست می‌آورند و قبلاً نداشتند چیست؟ و پاسخ هیچ است.
آنها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتار خود را تغییر دهند. اگر رفتارشان را تغییر دهند، این چیزی است که باید جشن گرفت.
🔸
هیچ‌کس نمی‌تواند حق دفاع از خود یک کشور دیگر را نادیده بگیرد — اسرائیل حق دارد از خود دفاع کند.
اما اساساً، اسرائیلی‌ها، درست مانند همه‌ی مردم دیگر، باید به این روند صلح که اساساً برای آن‌ها و کل منطقه مفید است، احترام بگذارند.
🔸
در انتقاد از اسرائیل: به نظر می‌رسد که ما درست در آستانه یک پیشرفت بزرگ در توافق هستیم، و ناگهان یک انفجار بزرگ در یک مرکز جمعیتی غیرنظامی در بیروت رخ می‌دهد و بسیاری از افرادی که هیچ ارتباطی با حزب‌الله ندارند جان خود را از دست می‌دهند. این قابل قبول نیست.
🔸
توافق هسته‌ای اوباما اجازه غنی‌سازی داد — توافق ما این اجازه را نمی‌دهد.
توافق اوباما اجازه انباشت مواد با درجه تسلیحاتی را داد؛ توافق ما در واقع به نابودی آن انبار مواد غنی‌شده منجر می‌شود.
توافق اوباما بیش از یک میلیارد دلار پول آمریکایی به آنها داد؛ این توافق هیچ دلار پول آمریکایی به آنها نمی‌دهد.
🔸
آنها تعهدات هسته‌ای بسیار مشخصی داده‌اند.
آنها متعهد به نابودی ذخیره بسیار غنی‌شده‌ای شده‌اند که در اختیار دارند.
اما نکته دوم، تنها کاری که ما انجام داده‌ایم برداشتن محاصره در تنگه است — که اساساً آن را به وضعیتی که قبل از درگیری بود بازمی‌گرداند.
🔸
خانم‌ها و آقایان، کلمات مهم نیستند، ما درباره تأیید صحت صحبت می‌کنیم.
🔸
فرض کنیم — دو سال بعد، آن‌ها آنچه را که ما باید در برنامه هسته‌ای ببینیم انجام داده‌اند و تحریم‌ها را طبق توافق آزاد می‌کنیم.
سپس تصمیم می‌گیرند که برنامه هسته‌ای را دوباره بسازند.
البته در این صورت، آن تحریم‌ها دوباره باز خواهند گشت.
و به همین دلیل است که این موضوع واقعاً شبیه یک دکمه تنظیم است: هرچه رفتار خوبشان را افزایش دهند، ما می‌توانیم تسهیلات اقتصادی را افزایش دهیم؛ اگر رفتار خوبشان را کاهش دهند، می‌توانیم آن را قطع کنیم.
🔸
آنچه واقعاً اتفاق افتاد این است که ما یکشنبه یادداشت تفاهم را امضا کردیم. این موضوع شرایط توافق را تثبیت کرد.
ایرانی‌ها به ما آمدند و گفتند: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً این را درک نمی‌کردم—می‌خواستم متن را فوراً منتشر کنم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «باشه، ما تا جمعه صبر می‌کنیم.»
و سپس در طول دوشنبه و سه‌شنبه، در حالی که رئیس‌جمهور در نشست جی۷ بود، شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را تشویق می‌کردند که این کار را انجام دهند.
ما قطعاً به آنها می‌گفتیم:
«ما تمایل شما برای عدم انتشار متن تا جمعه را درک می‌کنیم، اما می‌دانید که ما در یک نظام دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق را ببینند. ما قطعاً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها تصمیم گرفتند که رئیس‌جمهورشان آن را امضا کند، رئیس‌جمهور ما آن را امضا کند، و سپس متن را به عنوان یک سند امضا شده فوراً منتشر کنند.
🔸
اینکه فکر کنیم فروش چند میلیون دلار نفت قرار است اقتصاد ایران را به طور بنیادین تغییر دهد، درست نیست.
🔸
در مورد وجوه مسدود شده، مقدار پول — صادقانه بگویم نمی‌دانم.
اعدادی بیش از ۱۰۰ میلیارد دلار شنیده‌ام. در واقع اعدادی بیش از ۲۰۰ میلیارد دلار هم شنیده‌ام.
بیشتر آن در حساب‌های ایالات متحده نیست؛ بیشتر آن یا در خلیج فارس است، یا در اروپا، یا جای دیگری.
اما مقدار دقیق پول را نمی‌دانم — مقدار زیادی است.
🔸
من گزارش‌هایی دیده‌ام — نمی‌دانم این از کجا آمده — که قطری‌ها میلیاردها دلار و دارایی‌های ایرانی را آزاد کرده‌اند.
این اصلاً درست نیست. برای قطری‌ها غیرممکن است که بدون موافقت ما این کار را انجام دهند، و قطعاً بدون اینکه ما ببینیم.
🔸
درباره موشک‌های ایرانی:
توانایی آن‌ها در پرتاب موشک به طور قابل توجهی کاهش یافته است.
آیا این توانایی صفر شده؟ خیر. اما به طور قابل توجهی کاهش یافته است.
ما آن مأموریت را رها نکرده‌ایم. ما آن را به انجام رسانده‌ایم.
🔸
خدا را شکر. خوشحالم که پاپ چیزهای مثبتی درباره تفاهم‌نامه ما گفته است.
🔸
آنچه ما می‌گوییم این است که
نیروها را به سطح قبل از درگیری بازمی‌گردانیم،
قصد نداریم چند گروه ناو هواپیمابر اضافی را آنجا نگه داریم.
ایرانی‌ها این را نمی‌خواهند؛ صادقانه بگویم، ما هم این را نمی‌خواهیم.
🔸
خبرنگار: چه کسی آن صندوق ۳۰۰ میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
جی‌دی ونس: تمایل زیادی از سوی دنیای عرب و حتی خارج از دنیای عرب وجود دارد که اگر ایران رفتار مناسبی داشته باشد، واقعاً در آن دخالت کنند.
🔸
کمی به توانایی رئیس‌جمهور ایمان داشته باشید، با توجه به اینکه او ما را تا اینجا رسانده است، می‌تواند ما را به گام نهایی برساند.
🔸
دونالد جی. ترامپ تنها رئیس دولتی در سراسر جهان است که در این لحظه نسبت به ملت اسرائیل همدردی دارد.
اگر من در کابینه دولت اسرائیل بودم، شاید به تنها متحد قدرتمندی که در سراسر جهان دارم حمله نمی‌کردم.
🔸
در سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط دست‌های آمریکایی ساخته شده و با مالیات‌های آمریکایی پرداخت شده‌اند.
مشکل اسرائیل دونالد جی. ترامپ نیست، و هر کسی در اسرائیل که فکر می‌کند بزرگ‌ترین مشکلشان رئیس‌جمهور ایالات متحده است، باید بیدار شود و واقعیت وضعیت کشورشان را درک کند.
🔸
خبرنگار: چه چیزی مانع ایران می‌شود که در آینده برنامه هسته‌ای خود را بازسازی و از سر بگیرد؟
جی‌دی ونس: اول از همه، آنها باید پول زیادی به دست آورند تا بتوانند برنامه هسته‌ای خود را بازسازی کنند
.
c-span
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/76483" target="_blank">📅 19:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76482">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHUrd_hAdA1HN8cpuGrU79JSGMLyHeWVHGSvMDLeBtc0o0gFpzVCnNHcvKY-teXGCrjP5NPrxi30j9cYCzdpOFQADUcRcKffMqtyrivsTBKOUfynh3OS7aYv05vkdDGyxclH27siWOHKaRjptMdovX4MkdWJHJ5HrG_EeEGufyQWex5mrLKwE4QkaadE4VaOo4WLOzTGLWIp75wCDMEzcnvxGGa6LQr4qXoElqa5kP5N0yGO1ovrLiSpMPAxF_h2fDHwa0nBRR98AIWlmV1GpLMiD4Y9H_mO9qK7DSw8VGM9UALJfpNTNbyHydpS_RF9vrGe1kWueknVDTldS3uGSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر کشور و رییس سازمان امور اجتماعی ایران می‌گوید به افرادی که در تجمعات شبانه «دوقطبی‌سازی» می‌کردند، در یک نامه به طور «محرمانه» تذکر داده است.
«محمد بطحایی»، بدون اشاره به نام این افراد گفته است که «مورد اول مربوط به یک سازمان و تشکل سازمانی بود و در دو مورد دیگر به‌صورت فردی، نامه‌ محرمانه و البته همراه با احترام و تکریم برای افراد مورد نظر ارسال شده است.»
پس از اینکه گفته شد ایران و آمریکا به امضای تفاهم‌نامه‌ای برای رسیدن به یک توافق پایدار نزدیک هستند، برخی مخالفان این توافق که از چهره‌های نزدیک به جبهه پایداری، تشکل سیاسی اصولگرا و تندرو در ایران هستند، علیه «عباس عراقچی» و «محمدباقر قالیباف» شعار دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76482" target="_blank">📅 18:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76481">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TRQu2-IZk2ZlzAAkJRa91_hUcQuutRHY297XU4TjZA4j9DC4YeWQxtJHSYxNUzgCXjkQgMyfhw33lAoLUFDiWZEGjWVKlY8vtyNQ5ba-g5sDxjmkNZPHRAfn-8mc8yhTkH98fRUbkDBGt39bOqXRsQsg-uYFIVJ9Fb6MogWS-WSmy7fZWiymn7n2My2t8ml_RPKSWAQ1j2agZpRmRd5hbiyGilyEnsYnHonZDfTV4Qv0UAeYZFtTDANBafoMWAOtzUt8A1UPinGQla_J2KM2dWDBvV27ZnZdzHAPESkPXYEFwUE1DNX5uqlKf2Q54yNKsGtsSAN6icloL3HsHjzJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرنا: به پاکستان گفته شده "نیازی به برگزاری نشست حضوری در سوئیس نیست"
ننوشتند کی گفته:
منابع دیپلماتیک پاکستان گفتند که سفر برنامه ریزی شده شهباز شریف نخست وزیر این کشور به سوئیس لغو شده است.
این منابع مدعی شدند که از آنجایی که یادداشت تفاهم اسلام‌آباد از سوی رئیس جمهوری اسلامی ایران و رئیس دولت ایالات متحده به امضا رسیده است، به طرف پاکستانی اعلام شد ‌که اکنون نیازی به برگزاری نشست حضوری در سوئیس نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 264K · <a href="https://t.me/VahidOnline/76481" target="_blank">📅 17:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76480">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/upE-QaQbAIc76bad0CS2REsfTpLoWJER_zx3bK52lfHF-EDtQg9gLkYtBGoBPKxo9VUsXdCzywnhAyADxB9atpikcCLBGiGr8dtZNrtwXMnX0rs0hQqTIyaNTBfQdSahcygVF8SbEw8TyA6EelkXZ9IJ_4QLbf1PG3pYwKj3O_ZyzJ0HQDJSCF-JyM0VlHWhySMD4xEZ_UCqYLd7xYyYxuo6mE6xVhA1kss0eybHRxolMfN-MZlWeIzX5YbWRQ7acDN1LZUI7QWQ7jB_Jb336FTUIyW1kU29fMJK9hFhOnsoJd67bZPVDonPrYj6p64tGXgckjYgffGsQW5XmpNy6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ ترجمه ماشین:
«نفت در جریان است، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد، جهان امن خواهد بود! بازارهای سهام غرش‌کنان پیش می‌روند، مشاغل در سطح رکورد هستند، و قیمت‌ها در حال کاهش‌اند؛ مقرون‌به‌صرفه شدن! کشور ما مثل هیچ‌وقتِ دیگر قدرتمند، امن و محترم است. «خواهش می‌کنم!» رئیس‌جمهور دی‌جی‌تی»
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76480" target="_blank">📅 17:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76479">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/skNIzE_r9J-bFNaUxDRUsQHd3zSp4iwYQT8RJctmOPXGmFuIrd_eVGrh-nIQqueu1O3SVribzbTiuH-GZu8YzheOBx1te_9O5BHaRfLFGKh4PSopthfs47jn7uXmCk9KhG5Z5Zwd-06w2faWpw4waRLTAu7RxgtBdi1ujJqhEKdSR7GiZXJbCznUBhynFldiYUtjN8GplhFGtOeXhU1keOabD0GRNVeH6PRVNhEMgTpm9YG_GW7e0wa4S87jysVQw7lh2-AnpZunvoTJzgbFnX3sgaOOKh1UxSfIWczj7RxQiakjS_8lSgyrOJeG5rGLO0r5XzTbB78MTdURDnBFgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند دقیقه پیش ترامپ: "پاپ لئو از توافق صلح آمریکا و ایران تمجید کرد."
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76479" target="_blank">📅 16:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76478">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tBzeNeS0oCHJW3IMF0Q4-CLK8FSi12EXOEMJUSALX6mMwoH5zp-dPPFrsNFyJyfJujR1a5KdFBFQFWK_iLD8A2GXTjaSC_HvNsh9pQpYqsjqKhSBhR_uCa01oYE0uSNGh_dGWs6g-L5zSSmcEAxeg16veRXLuP1tlx6jbqkbzR1B2ttqary8GiqGa49zcF5jlRbYXsrfAxIx44XxckffexqgZIL46WHG1FoNSPTcD1718aan5PBbK9JHsRRRS4kRgcOZ02wr1zYypumpW3S9LjEGvY2zbWEUOZkXM90ysAduN9tl3ZyTe8csJ-QZUqFu82dF3VFvD1R5k1f2Ge2gIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست چند ساعت پیش ترامپ:
این احمق‌ها که فکر می‌کنند من در قبال ایران به اندازه کافی سخت‌گیر نبوده‌ام، در حالی که بازار سهام همین الان به رکوردی تاریخی رسیده و قیمت نفت هم دارد «سقوط» می‌کند، یا حسودند، یا آدم‌های بدی هستند، یا احمق‌اند.
آمریکا را دوباره عظیم کنیم!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/76478" target="_blank">📅 16:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76477">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gqgHFs1niqINjKb_fOnUUdvNdY6r4Dm2utug1HWpkWdvshDtpZQGD562utgJE53-PyZNQ2Lr4mx7jsCp3_Cii9snPXTkavt7dqhZ4EZeY8ja1Kr1FTjlf5Sp2zHfLYuXJWPBvx0f_DfJFMOTimzehWJh-chZeSyPk4_kgWMAd9AwJ1VXWFtKhV5Tw7rclFQg8h62yKJB27UaWFPVD7M9mOv8zlRGBhCF9brlF4JJv4dRk4j-CtziKYpVE4RRlULySc63vKQ1z7BaUpZ0-u5B3TPQF13MXllprs2sCbMoovxLT1I1_dgR8ig-RkK-GCwW6NirIsfR5bM9_3x5_kGmmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا، روز پنج‌شنبه ۲۸ خرداد در یک موضع‌گیری درباره تفاهم‌نامه اسلام‌آباد تأکید کرد که ارتش آمریکا قرار است «چماق بزرگ پشت مذاکرات» باشد.
او همچنین تأکید کرد که هر گونه تغییر در اندازه حضور نظامی آمریکا در خاورمیانه «بسته به شرایط» خواهد بود.
این نخستین اظهار نظر هگست در پی امضای تفاهم‌نامه اسلام‌آباد میان تهران و واشینگتن است که بامداد پنج‌شنبه توسط رئیس جمهور ایران هم امضا شد و رسمیت یافت. دونالد ترامپ ساعتی پیش از مسعود پزشکیان سند را امضا کرده بود.
متن تفاهم‌نامه‌ای که دولت آمریکا به امضایش رضایت داد حتی از چند روز پیش از امضا شدن هم انتقادهایی در پی داشت، انتقادهایی که با انتشار متن کامل آن افزایش یافت.
به نظر می‌رسد که سخنان وزیر دفاع آمریکا هم تا اندازه‌ای پاسخ به همین انتقادها باشد.
به گفته پیت هگست،‌ آمریکا «از موضع قدرت به توافق با ایران رسید».
@
VahidHeadline
وزیر دفاع آمریکا همچنین گفت که برخی کشورهای اروپایی آماده‌اند در عملیات پاکسازی مین‌ها در تنگه هرمز مشارکت کنند.
هگست در عین حال از بریتانیا خواست نقش گسترده‌تری ایفا کند و گفت که این کشور باید «گام بیشتری بردارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/76477" target="_blank">📅 16:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76476">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITAGifMIXgjj2U1gkXO2TlE06a0prVrNCOVeQo4bBoFYzOwK5s1_u93oW6BGQfdCdHvH-Bw70ohXvzu14Ya5NDbySXLYBbhoVktMRXba28jHdjLWI9OqRzfFDh0MS_nBUhGQksS8g7U7y1Cp8ctAKhbHu8sIc_q0U497UAB2amU06v8LjRDCBBNuzyM4v93kgeWe_aPMKLVFBWmtG9_Hw68bE53WGKjy0yzfUhNCoVFarZRn8ye2hl3anh58rF4M_mh_nBGGb1QH-FDvlT0BE30nr1HLQ-XdmHQf_pdPA0nesPvPG6ygp2nvf5KUXDbopw3coVptslP1-jbb3x5jRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه کیفری استان قم، پرستو احمدی، خواننده، و هشت نفر دیگر از دست‌اندرکاران و نوازندگان «کنسرت کاروانسرا» را به‌طور جداگانه به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال ممنوعیت از فعالیت هنری محکوم کرد.
اتهام این هنرمندان در این حکم قضایی جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای مبتذل و خلاف اخلاق در بستر فضای مجازی» عنوان شده است.
پرستو احمدی ۲۱ آذر سال ۱۴۰۳، به همراه گروهی از نوازندگان مَرد شامل احسان بیرقدار، سهیل فقیه‌نصیری، امین طاهری و امیرعلی پیرنیا، در کانال یوتیوب خود ویدئویی بدون حجاب اجباری، از «کنسرت کاروانسرا» یا «کنسرت فرضی» را منتشر کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76476" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76475">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SjumfdM4UBpJJXZGucWLEBwbfl-6N8fH1DLTpt_a-LSpwOiWQvP6ZZmUkcrbS6EBMa0SNm-yk7CaItyFXfIz6oQyDoR4AR2ER9JfU29Fvi_q7Bk4Oek7rFNPKWFAbNGgt7x91CaefuxKsF3l45U7vgq8s_xhfRIbcQHV3AOhfM_OROz8-b4JVJB2b8ne1wAIMkEI9GLEPEvsIdRp_PrkqvcNAUXTAhCRcCTxlHSqWY2H4Lj-7va9oQrCvJKwMowb6JPx4kGhnkPvHZDjSApdtlKyj7b8umS9KoAZOR7FrQwQ_d5J-MLEHTg5ohknhw4s1QCP9ZeTqDtRpvsj3aFaxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت ۹ سال پیش ترامپ داره توجه می‌گیره:
ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76475" target="_blank">📅 05:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76474">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HMiZ-V9xs6leaVf0o_NeExjQKsXGMuqMTeVWHaUmsfmaMrS3UOLuHaHGhOGqjw4kPsbg1jxfGS-BQJ3tUhhpgWzXOG7TwRD5G9O9oxuTtjiE_rxcUZGNxJ68Hfx8dz2v3bfPSdiJYpXsW5Y0Iwsu7kIfrNERTgl-HF-ZV4cvW_uDKis4S9Hb2tK4f3PiinlxNNjX4V4tDgP4WB5oaP2uZqhuG3rMOF8fR4twfbySF65daugMRp1dKhq8njYDzt_iTenHTh-2dagwKdztMRlS1eyTJOS2bF8pEmuqsCfpN6QD6ARnL-M_K3IrIv2cTQzZvR3BAVcBpEq6QJrfzV1Ifg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درستش کردم
MahvashJebeli
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76474" target="_blank">📅 04:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76471">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iV-zxf7_Lfa9tPnJzOAHh7HmClfpmCmxNK_tXKl0J7W7m5iBcpjymVRIfSQwiLkXMN1oUnfNG9a866F8CelAOZIoWXOsFRT_-gia2oTRl03whTlB838VNHw0djjbeu8XVsCV2-s0SGYXhFTbnYko4Jb6qyH0buMSLLFWluZKqlXBma8oYVOvl7o29perZzI3-ku9zqQDJmZgP9EQEHYt_xOampC_QbOQvko4U52DrUNdu6Fy53waoHOTDuxzqHpdwxx6mB8B9koA7XbRclXMD8p49HRZ4J_uo_wbDgbqGjmNO55eQwuI3Fq8ue5eAdMTkqo1R84NONjIj7A2TwIlzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qyIiFjs4ybJ12KZ_S5UqdC3zwaGDFZadqRsFvnaTBKqOw5ZVj7rrVveAFzsgbsXbxnAm-i4ua8ucYlBpTHL50D8NUNM0elOP7TJ8PwAJWV8n2RilfphrZTfPkA8bRcbmfPHjhTfCHJYDM5O_1RfS4Ew5Z8zU_AqsOIg_50I1OfMOAfmvac151UD7ufQLZfPYDQG_RKFtbdUECkEyeQicacRSLzqCNY61Jl8XyvcSs5tLeJGgXYnxzNUH_AphG0pBzpPJ0YseKSl_zgMEbU70hAQhRY33-DZIXfW6nwGPnN-qUhXTw2WXc-MInua4Tytv3ye0S-hS0pP9qGrVyopG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a4K9lgIphqSRTkBgQlUakfBL1rz-CJCwsDvKM2QI1fBbhOZAy3qgWmJYMWABi7_EZLYTm8Zu8T-LKMhbOv3UaAhoObA89ITWYC6DofUAqUTDPoBASBY52eM9Nxj2iLAoq0aD5vpRZU4YXEp46icmH8cuE_GQm_tLnqgp4TfXlnzzBnHampxZd4FiMfJmIWASzrWXWiJFTVDawnVDoV2AG-5uC-S8kHBQvaf9Bvx2Ca_j68Q_X9rTAAxNWOQnosPi_LPjX34e5_Q2gw4IUztmyyCeDkC-cpWBn-jFsJ2zfLRzQ--nmUiKqomvoOZwcqRyPuP2XlMydiMvOD7efJBeGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امضای پزشکیان پس از
امضای ترامپ
تصاویر منتشر شده از سوی ایرنا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/76471" target="_blank">📅 03:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76470">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6a09c6ccc.mp4?token=HxSIDNigy3xTf0DPITi6CVTAC85sNHrPgSslqjoFxG3MKmOQ1d8H_7w_GCaB0wLXeJeULoAiOmqofHBPUf76myhHFZbF7nr9RGARpNliHxR8UMbKAxySQ67i0VdK4QezOdfksJRNSAt6IE3rynzvluaS9sXS8jLNrMB0BVv2vqAVhLIwNA3SsGXC9hUPyjKMx79nmYqQVqfCOtS-L7_y-dn8ZlVz58ZTPh8SVgU-xqzz4I96-yWL9lvKMrlYxFOA6O3PtuLSJJDUoHHzeBu0PJY4YgVBknC2CS7XOJI_XVzYBLD8azRq7-9Ib-ZP5FHhZPgskN95hxzzcrEi1yaf7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6a09c6ccc.mp4?token=HxSIDNigy3xTf0DPITi6CVTAC85sNHrPgSslqjoFxG3MKmOQ1d8H_7w_GCaB0wLXeJeULoAiOmqofHBPUf76myhHFZbF7nr9RGARpNliHxR8UMbKAxySQ67i0VdK4QezOdfksJRNSAt6IE3rynzvluaS9sXS8jLNrMB0BVv2vqAVhLIwNA3SsGXC9hUPyjKMx79nmYqQVqfCOtS-L7_y-dn8ZlVz58ZTPh8SVgU-xqzz4I96-yWL9lvKMrlYxFOA6O3PtuLSJJDUoHHzeBu0PJY4YgVBknC2CS7XOJI_XVzYBLD8azRq7-9Ib-ZP5FHhZPgskN95hxzzcrEi1yaf7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه امضای یادداشت تفاهم از سوی ترامپ
دونالد ترامپ، رئیس جمهور آمریکا که چهارشنبه شب در کاخ الیزه میهمان ضیافت شام با امانوئل مکرون بود نسخه نهایی و منتشر شده تفاهم‌نامه با جمهوری اسلامی ایران را امضاء کرده است. مسعود پزشکیان نیز این سند را امضاء کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 408K · <a href="https://t.me/VahidOnline/76470" target="_blank">📅 03:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76459">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10e61c88b0.mp4?token=BpyQ5TWk0cWg_lMVSIvp-9832r6F-GlK3UoYb3XeU3weK0y27v2Vv3A4g4hN1Uv7UndGpjsGZhiRHjNdn9eOtGzahgn2bnGIcFSiQ3T0LVBVBvDwSo6GsjWV1hZlrnqDm8XFoaWdRdLE8_ZRk0Xo7tV82nF3lUJG03qNdRPvGzHx9D6fUSa14tDIAiycz452MrAgphnAughivrpJpgogqYa2rO8CaK8Xhv_v0QlMsMMmRxEUClAAX9vzpULoosXd_Ym71QamO_bAIZ38mS03wJndOdxK1NwuK7WcUSRT92_SiaXR_tN3jzIrBX1SSQMTUGXmEJNyIcdQ_L1FfWyy9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10e61c88b0.mp4?token=BpyQ5TWk0cWg_lMVSIvp-9832r6F-GlK3UoYb3XeU3weK0y27v2Vv3A4g4hN1Uv7UndGpjsGZhiRHjNdn9eOtGzahgn2bnGIcFSiQ3T0LVBVBvDwSo6GsjWV1hZlrnqDm8XFoaWdRdLE8_ZRk0Xo7tV82nF3lUJG03qNdRPvGzHx9D6fUSa14tDIAiycz452MrAgphnAughivrpJpgogqYa2rO8CaK8Xhv_v0QlMsMMmRxEUClAAX9vzpULoosXd_Ym71QamO_bAIZ38mS03wJndOdxK1NwuK7WcUSRT92_SiaXR_tN3jzIrBX1SSQMTUGXmEJNyIcdQ_L1FfWyy9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">☄️
ترامپ و پزشکیان امضا کردند
دونالد ترامپ، در پاسخ به سوال خبرنگاران که آیا تفاهم‌نامه با جمهوری اسلامی را امضا کرده است پاسخ داد: «بله امضا کردم...در ورسای امضا کردم.»
@
VahidHeadline
پیش‌تر
:
بقایی: همین الان که با شما صحبت می‌کنم یعنی بامداد ۲۸ خرداد احتمالاً متن تفاهم نامه اسلام آباد به امضای روسای جمهور ایران و آمریکا رسیده باشد.
آپدیت:
توییت شهباز شریف نخست‌وزیر پاکستان
ترجمه ماشین:
باعث افتخار من است که اعلام کنم «یادداشت تفاهم تاریخی اسلام‌آباد» امروز به‌صورت الکترونیکی میان ایالات متحده آمریکا و جمهوری اسلامی ایران امضا شد. این یادداشت تفاهم به امضای رؤسای محترم هر دو کشور رسیده و من نیز به‌عنوان میانجی آن را تأیید کرده‌ام. امضای این توافق در بالاترین سطح دولت‌های مربوطه، نشان‌دهنده تعهد دو طرف به حل‌وفصل دیپلماتیک این مناقشه است. یادداشت تفاهم اسلام‌آباد با اثر فوری لازم‌الاجرا خواهد شد و در نخستین گام، جمهوری اسلامی ایران فوراً تنگه هرمز را بازگشایی خواهد کرد و ایالات متحده آمریکا نیز بلافاصله محاصره دریایی را لغو خواهد کرد.
پاکستان، با حمایت دولت قطر به‌عنوان میانجی مشترک، مراسم رسمی را طبق برنامه در تاریخ ۱۹ ژوئن ۲۰۲۶ در سوئیس میزبانی خواهد کرد تا این رویداد تاریخی گرامی داشته شود و گفت‌وگوهای فنی آغاز گردد.
صمیمانه‌ترین تبریکات و قدردانی خالصانه خود را به رئیس‌جمهور ایالات متحده، دونالد جی. ترامپ، تقدیم می‌کنم؛ کسی که تعهد استوارش به دیپلماسی و ترجیحش برای حل‌وفصل مسالمت‌آمیز، بار دیگر به پایان دادن به مناقشه‌ای کمک کرد که می‌توانست پیامدهای ویرانگری برای منطقه و فراتر از آن داشته باشد. همچنین از تلاش‌ها و کوشش‌های خستگی‌ناپذیر تیم مذاکره‌کننده ایالات متحده، از جمله جی.دی. ونس، استیو ویتکاف و جرد کوشنر، به‌خاطر نقش ارزشمندشان در این دستاورد تقدیر می‌کنم.
احترام و قدردانی عمیق خود را نسبت به حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای، رهبر عالی جمهوری اسلامی ایران، و رئیس‌جمهور مسعود پزشکیان ابراز می‌کنم؛ به‌خاطر خرد، دوراندیشی و دولتمردی آنان در پذیرش آرمان صلح. همچنین مایلم تلاش‌های تیم مذاکره‌کننده ایران، از جمله محمدباقر قالیباف، عباس عراقچی و اسکندر مؤمنی را به رسمیت بشناسم؛ کسانی که صبر، پایداری و تعهدشان به تعامل سازنده، در به ثمر رسیدن این توافق نقشی اساسی داشت.
مایلم به‌طور ویژه از تلاش‌های صادقانه و تعامل سازنده رهبری دولت قطر در کمک به رسیدن به این نقطه قدردانی کنم. همچنین از رهبری پادشاهی عربستان سعودی، جمهوری ترکیه و جمهوری عربی مصر به‌خاطر نقش ضروری و مشارکت‌های ارزشمندشان در این زمینه، بسیار تقدیر می‌کنم.
همچنین مایلم به‌طور ویژه از فیلد مارشال سید عاصم منیر یاد کنم؛ کسی که تلاش‌های خستگی‌ناپذیر، فداکاری بی‌چشمداشت و نقش کلیدی‌اش در تسهیل این پیشرفت و پیشبرد آرمان صلح و ثبات منطقه‌ای حیاتی بود.
باشد که این یادداشت تفاهم، بنیانی پایدار برای تفاهم بیشتر، احترام متقابل و رفاه مشترک در سراسر منطقه باشد.
CMShehbaz
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/76459" target="_blank">📅 00:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76458">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">"متن کامل یادداشت تفاهم اسلام‌آباد بین جمهوری اسلامی ایران و ایالات متحده آمریکا"
به نقل از ایرنا:
https://telegra.ph/mou-06-17-2
ترجمه متن منتشر شده از سوی آمریکا
@
VahidHeadline
مقایسه نسخه منتشر شده از سوی ایرنا با نسخه  نسخه آمریکایی که بی‌بی‌سی به آن دست یافته است، نشان می‌دهد دو نسخه از این توافق ۱۴ بندی تقریبا به طور کامل یکسانند.
تنها تفاوت جزئی در بند ششم دیده می‌شود؛ بندی که با این عبارت آغاز می‌شود:
«ایالات متحده آمریکا متعهد می‌شود با همکاری شرکای منطقه‌ای، یک برنامه نهایی مورد توافق طرفین با حداقل ۳۰۰ میلیارد دلار برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران تدوین کند. سازوکار اجرای این برنامه به عنوان بخشی از توافق نهایی، ظرف ۶۰ روز نهایی خواهد شد.»
آخرین جمله این بند در نسخه آمریکایی چنین است:
«تمام مجوزها، معافیت‌ها و اجازه‌های لازم برای انجام معاملات اولیه مرتبط، از سوی ایالات متحده آمریکا صادر خواهد شد.»
اما در نسخه منتشر شده توسط ایرنا، واژه «اولیه» از این جمله حذف شده است.
با این حال، به نظر نمی‌رسد این تفاوت جزئی تغییری اساسی در مفهوم یا محتوای توافق ایجاد کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/76458" target="_blank">📅 22:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76456">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCNoOoFAzl5v96cAI8McZhjRi1mQPbkPc6505HlQ827j8GMLf09gND7qZyAbibWJRfaiw0Bu5NhsKD5EtMwL9GOmFxRRHOagraqWdAoWvdpznWUZ4ZifR-IWGggBoMVtDrWvOlFt_YXCbWd0Sb9WbiEJnLRg8ocyzR0tCIXOcXsCz06VFic09Qd5X3uS5qgiv6S02hOGdB5MzNaqYsNlVy5BxrglCWwLTvZXw5BTFZz6feNI3iCke4RY1-9tS_7pqG1Kj4LR7_cK7vVTxrvgVZh-qRYNSsmitQ7zFgMQ4jcBWPcuO-MudjhrmXgKBOl4gY1Pcn4jX2ZBT0dgEYPKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه جمهوری اسلامی روز چهارشنبه از احتمال امضای توافق پایان جنگ توسط روسای جمهوری ایران و آمریکا خبر داد و گفت این مسئله «در حالی بررسی است».
به گزارش رسانه‌های نزدیک به حکومت ایران، اسماعیل بقائی درباره احتمال امضای یادداشت تفاهم از سوی مسعود پزشکیان و دونالد ترامپ اعلام کرد: «این ایده مطرح است و همچنان در حال بررسی است.»
پیش از این طرف‌های ایرانی و آمریکایی خبر داده بودند جی‌دی ونس، معاون رئیس‌جمهور آمریکا، و محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در سوئیس این تفاهم‌نامه را امضا خواهند کرد.
دولت سوئیس تأیید کرد مراسم امضای این تفاهم در اقامتگاه کوهستانی بورگن‌اشتوک برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/76456" target="_blank">📅 21:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76455">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کنفرانس خبری ترامپ
:‌
🔸
یکشنبه، ما به توافقی با ایران رسیدیم که همه چیزهایی را که قصد داشتیم به آن دست یابیم محقق می‌کند—همه چیز و حتی بیشتر.
🔸
اگر این توافق را انجام نمی‌دادیم، می‌توانستیم برای ۲ تا ۳-۴ هفته یا حتی ۲ سال بمب‌های بیشتری رها کنیم.
شما هرگز تنگه هرمز را باز نمی‌دیدید.
🔸
اگر من ژنرال سلیمانی را نکشته بودم، احتمالاً الان درباره این توافق صحبت نمی‌کردیم، چون او نابغه‌ای دیوانه بود.
آنها هرگز نتوانستند جایگزین او شوند.
🔸
رهبران جهان از اینکه ما به توافق رسیدیم بسیار خوشحالند، همه‌شان.
هیچ کشوری به ما نیامد و نگفت «لطفاً آقا، بمب‌ها را روی آن‌ها رها کن. لطفاً بمب‌ها را رها کن» — آدم‌های احمق این را می‌گویند.
🔸
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آنها بسیار کمتر رادیکال شده‌اند. فکر می‌کنم واقعاً کشورشان را دوست دارند. آنها خوب هستند.
🔸
نمی‌خواستم شاهد یک فاجعه اقتصادی باشم؛ اگر این روند ادامه پیدا می‌کرد، ممکن بود اتفاق بیفتد.
هر بار که درباره صلح صحبت می‌کردیم، بازار سهام بالا می‌رفت.
بازار سهام از هر کسی که آنجا هست، از جمله افرادی که روی این صحنه هستند—به جز من—باهوش‌تر است.
🔸
بازار سهام بسیار درخشان است. و هر بار که چیزی شگفت‌انگیز می‌گفتیم، مثل «ما قرار است توافق کنیم»، بازار بالا می‌رفت.
و هر بار، هر بار که چیزی منفی می‌گفتیم، مثل «ببین چی شده، ما نمی‌توانیم توافق کنیم»، بازار پایین می‌آمد — خیلی زیاد، خیلی، خیلی زیاد.
این به شما چیزی می‌گوید.
🔸
من نمی‌خواستم مثل هربرت هوور بزرگ دیر کنم. من آن را نمی‌خواستم.
[چت‌جی‌پی‌تی: هربرت هوور رئیس‌جمهور آمریکا در آغاز رکود بزرگ ۱۹۲۹ بود. در حافظه سیاسی آمریکا، هوور نماد رئیسی‌جمهوری است که بحران زیر دستش منفجر شد و بعد متهم شد که دیر، ناکافی و با احتیاط بیش از حد واکنش نشان داد. حتی محله‌های فقیرنشین دوران رکود را با تمسخر Hoovervilles می‌گفتند.
پس منظور ترامپ احتمالاً این است: نمی‌خواستم آن‌قدر صبر کنم تا بحران از کنترل خارج شود و بعد همه بگویند رئیس‌جمهور دیر جنبید.]
🔸
درباره کشتن قاسم سلیمانی:
این یک همکاری مشترک بود، همان‌طور که در کسب‌وکار املاک می‌گوییم. این یک همکاری مشترک بین اسرائیل و ما بود.
ما یک ماه آن را بررسی کردیم. تقریباً یک ماه قبل می‌دانستیم که او با کدام هواپیما سفر خواهد کرد.
او فقط با خطوط هوایی تجاری، آن‌های بزرگ و پرجمعیت سفر می‌کرد، چون می‌دانست ما او را سرنگون نمی‌کنیم. آن‌ها خیلی باهوش هستند.
اما ما می‌دانستیم که او در آن هواپیما خواهد بود، او را دنبال کردیم، و سپس اسرائیل به من اطلاع داد که آن‌ها این کار را انجام نخواهند داد. و من باید تصمیم می‌گرفتم.
و من به او گفتم، «خب، اگر اسرائیل این کار را نمی‌کند، ما همه آماده‌ایم. آیا انجامش می‌دهیم؟ دوست داری انجامش دهی یا نه؟» گفتم، «البته، اگر می‌خواهی انجامش دهی، ما می‌توانیم انجامش دهیم.»
🔸
درباره نتانیاهو: بیبی نتانیاهو مرد خوبی است. گاهی کمی هیجان‌زده می‌شود، اما اتفاقاً مرد بسیار خوبی است.
ما یک اختلاف کوچک درباره لبنان داشتیم — من گفتم، می‌توانی کمی ملایم‌تر باشی، بیبی، لازم نیست هر بار که کسی وارد می‌شود یک ساختمان را خراب کنی؛ این کار حزب‌الله است.
🔸
نتانیاهو به کشور آمد و از باراک حسین اوباما، رئیس‌جمهور، التماس کرد که برجام را انجام ندهد. او گفت این می‌تواند پایان اسرائیل باشد، و اگر من وارد ماجرا نمی‌شدم، همینطور می‌شد.
و اوباما به او گوش نداد.
بیبی واقعاً به کنگره رفت و از آنها التماس کرد، اما به جایی نرسید. و آنها این توافق وحشتناک را داشتند که برای اسرائیل فاجعه‌بار بود.
🔸
این یک یادداشت تفاهم است. اگر در ۶۰ روز انجام نشود، اشکالی ندارد، ما به بمباران بازمی‌گردیم.
می‌دانید، من نمی‌خواهم این کار را بکنم، چون خیلی خوب است، خیلی خوب.
اما، خب، ممکن است مجبور شویم، چون هرگز اجازه نمی‌دهیم آنها سلاح هسته‌ای داشته باشند.
🔸
توافقی که ما با ایران روز یکشنبه به آن رسیدیم، به زودی امضا خواهد شد، فردا، شاید روز بعد.
🔸
ترامپ درباره اسرائیل:
فکر می‌کنم آنها می‌توانند در مورد حزب‌الله بهتر عمل کنند. نمی‌گویم نباید از خودشان محافظت کنند، بلکه می‌گویم — وقتی دو پهپاد به بیابان شلیک می‌شوند و بی‌خطر سقوط می‌کنند، نیازی نیست ساختمان‌ها را در بیروت خراب کنند.
آنها می‌توانند بهتر رفتار کنند. و صادقانه بگویم، آنها می‌توانند کار بهتری انجام دهند — من آنها را دوست دارم، به عنوان یک شریک عالی بودند، اما می‌توانند در مورد حزب‌الله خیلی بهتر عمل کنند.
🔸
ترامپ درباره ایران:
خب، آنها به سرمایه‌گذاری نیاز دارند، چون ما یک و نیم تریلیون، شاید دو تریلیون دلار خسارت وارد کردیم.
پس کسی باید به آنها کمک کند — خب، هیچ تضمینی برای کمک به آنها وجود ندارد، و ممکن است همسایگانشان کمی به آنها کمک کنند، نمی‌دانم، اما این مقدار زیادی پول است.
تقریباً هیچ‌کس چنین پولی ندارد — این همان نوع خسارتی است که وارد شده است.
🔸
آنها از یک نظر فرهنگی ابتدایی دارند، اما این فرهنگ ابتدایی نابغه است، آنها مردم بسیار باهوش و مذاکره‌کنندگان بسیار خوبی هستند.
🔸
درباره موشک:
ما در حال کار روی یک تلاش موازی با کشورهای خلیج فارس برای رسیدگی به مسائل غیرهسته‌ای هستیم، مانند موشک‌های بالستیک متعارف، که درباره آن صحبت خواهیم کرد و حمایت خواهیم کرد.
منظورم این است که آنها باید مقداری داشته باشند، چون دیگران مقداری دارند، شما هم باید داشته باشید — کسی این را گفت، «نباید به آنها یکی بدهید»، و من آدم‌هایی دارم — بعضی از این آدم‌ها را دوست دارم، اما فکر نمی‌کنم این را، فکر نمی‌کنم آنها باهوش باشند.
«البته، نباید اجازه دهید هیچ موشکی داشته باشند» — من گفتم، خب، من چه کار کنم، آیا می‌خواهم به عربستان سعودی اجازه دهم موشک داشته باشد، اما آنها نداشته باشند؟ «بله، قربان.»
اینطور کار نمی‌کند، می‌دانید، اینطور کار نمی‌کند، و موشک‌ها مشکل نیستند — موشک‌ها به یک مکان کوچک برخورد می‌کنند، اما سیاره را منفجر نمی‌کنند.
🔸
اگر آنها به توافق احترام نگذارند، یا برخی موارد حتی در توافق ذکر نشده باشد — این یک یادداشت تفاهم است، اما ما درک مشترکی از برخی مسائل داریم بدون اینکه آن را مکتوب کنیم — و، اگر آنها به آن احترام نگذارند، احتمالاً دوباره به بمباران آنها باز خواهیم گشت تا زمانی که به آن احترام بگذارند.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کار می‌توانند بکنند.
🔸
مردم می‌خواهند من پل‌ها را بمباران کنم.
من قبلاً این کار را انجام دادم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگ‌ترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن در ایران.
اما ما آن پل را بمباران کردیم، شما دیدید.
🔸
می‌خواهم از چین، رئیس‌جمهور شی، تشکر کنم، من با او بودم و او کاملاً بی‌طرف ماند، کاملاً بی‌طرف، و من این را قدردانی می‌کنم.
و می‌خواهم از ولادیمیر پوتین تشکر کنم، او بسیار بی‌طرف بود.
🔸
خب، آزادسازی پول‌ها — پاسخ آسانی دارد.
ما مقدار زیادی از پول آن‌ها را گرفته‌ایم، و پول آن‌ها را از آن‌ها گرفته‌ایم.
وقتی پول ما نیست، پول آن‌هاست و ما در یک زمان مشخص آن را مسدود کردیم.
فکر می‌کنم باید آن را پس بدهیم، می‌دانید؟
اگر پس نمی‌دادیم، هیچ‌کس دیگر هرگز در دلار سرمایه‌گذاری نمی‌کرد.
🔸
گزارشگر: یک مرد دانا زمانی گفته بود، در ژانویه ۲۰۲۰، «ایران هرگز در جنگ پیروز نشده، اما هرگز در مذاکره شکست نخورده است.»
ترامپ: این را چه کسی گفته؟
گزارشگر: دونالد ترامپ.
ترامپ: اوه، فکر می‌کردم همین را می‌خواهی بگویی.
🔸
اگر آنها پرچم سفید تسلیم را بالا ببرند و بگویند «سپاس خداوند را که دونالد ترامپ بزرگ‌ترین رئیس‌جمهور تاریخ است»، نیویورک تایمز و سی‌ان‌ان خواهند گفت «ایران پیروزی بزرگی به دست آورد.»
🔸
راستی، محاصره تأثیرگذارتر از تمام حملات هوایی بود، جایی که ما بمب‌هایی به ارزش یک میلیارد دلار روی ایران ریختیم.
🔸
گزارشگر: چرا حالا برای شما قابل قبول است که آنها بخشی از توان موشکی خود را حفظ کنند؟
ترامپ: آنها چه چیزی را حفظ می‌کنند؟ آنها اکنون کمتر از دیگر کشورها دارند.
ما احتمالاً ۸۴، ۸۵ درصد از موشک‌هایشان را از کار انداختیم، بقیه زیر زمین هستند و حتی نمی‌توانند آنها را بیرون بیاورند.
🔸
ترامپ درباره ایران: آیا می‌خواهید اجازه دهید ۹۱ میلیون نفر از گرسنگی بمیرند؟
🔸
خبرنگار: آیا اکنون می‌توانید بگویید که آیا کسی در دولت شما بابت حمله به مدرسه‌ای که در اولین روز جنگ بیش از صد کودک را کشت، مسئول شناخته خواهد شد؟
ترامپ: اشتباهاتی رخ می‌دهد، جنگ چیز زشتی است، می‌دانم که در حال بررسی است.
من از پیت هگست سؤال می‌کنم چون آن‌ها در حال بررسی این موضوع هستند.
🔸
خبرنگار: چرا برای مراسم امضای توافق صلح ایران نمی‌مانید؟
ترامپ: ممکن است بمانم.
🔸
گزارشگر: آیا در این موضوع عنصری وجود دارد که شما معاون رئیس‌جمهور را بفرستید، اگر موفق شد که عالی است، شما به عنوان کسی که او را فرستاده نابغه به نظر می‌رسید. و اگر موفق نشد، تقصیر معاون رئیس‌جمهور است.
ترامپ: من این ایده را دوست دارم. خب، به این صورت، اگر موفق شد، من اعتبارش را می‌گیرم. اگر موفق نشد، تقصیر JD است.
بهتر است مراقب باشی، JD. او هواپیمایش را برمی‌گرداند و از اینجا فرار می‌کند.
بله، من این ایده را دوست دارم. فکر می‌کنم ایده خوبی است.
📡
@VahidOnline
بخش‌های بالا رو من انتخاب نکردم. هم‌زمان با حرف‌هاش از منابع خارجی با ترجمه ماشین گذاشتم.</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/76455" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76454">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOd67x9tTRMNbhoMI2CIfitJvI8IiI_c7MK8wnAvTflDHTX9IJfw-nDJp2dkW1q4jAa6H1ee23E3kswOMhjLBg8q82D4I0PcQvS7yx79M3plzkntJOF7PxJBLzSzlpaNOr-Xyf4L9_KcOYb7PDD7r1nwdKke8wD-AlIyu_8v2im08Ab7wp0zN54WppMMiKlU359MnQ3nl4wVKCVtdnZ4TPAXnIQ8xobrJfUvy4nuB4_dl3q-Yr9IQV0Wdyn-lSC_sg2ebTTgeJGOv8fO91YHt4epQmQF6xGR8WJHNlCAUOijGAN9llbOOtL_AnVru8wvGoKJGMoxRBBzmaVWkKfRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شورای هماهنگی بانک‌ها، روز چهارشنبه ۲۷خرداد ۱۴۰۵، اذعان کرد بخشی از خدمات چهار بانک ملی، تجارت، صادرات و توسعه صادرات پس از گذشت چهار روز همچنان با محدودیت روبه‌رو است.
این شورا پیشتر در ۲۳ خرداد از وقوع یک «حمله سایبری محدود» به این چهار بانک خبر داده و اعلام کرده بود که این حمله موجب اختلال در ارائه برخی خدمات بانکی شده است.
رسانه ایران آی‌تی گزارش داده است که بر اثر این اختلال چند روزه، میلیون‌ها کاربر همچنان به حساب‌های خود دسترسی ندارند. این رسانه با انتقاد از وضعیت پیش آمده نوشت بسیاری از فعالان بازار از انجام معاملات مهم در بورس، طلا و سایر دارایی‌ها بازمانده‌اند.
شبکه بانکی ایران در سال‌های اخیر بارها هدف حملات سایبری قرار گرفته و در مواردی نیز اطلاعات مشتریان برخی بانک‌ها در فضای مجازی منتشر یا خرید و فروش شده است.
با وجود این، شورای هماهنگی بانک‌ها تاکید کرده است که سپرده‌ها، تراکنش‌ها و اطلاعات مالی مشتریان این چهار بانک در «امنیت کامل» قرار دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76454" target="_blank">📅 19:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76453">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XeNI40--8KqCL2J9QgkETmtStin_FG0c44Niv2H542Y49MfMBGYKGqvPOwq0Mj_29WAUH52BIru8nOEASjGYTTpjj3rZq_vi0rS_lNS00zi9J-tja0dKBDFGYHjwwZXOfdZvFAy9cR54ADXJNnL6NIllo_F78KEHdmKCkHxtvb60Jli3fBNVfq3zrz8uXp16wxLONrBtenA9on5yYEIsARV0RSawRIAlwKHup7XtTGiNkk0h9Y-YJ4s4Xv3g1YG15bdOTtux3PJ8RclPHGJyRlekPzncb9uJ_dwAoQ0kBEKMKGobr1mE1--LNMSB6ynmRBrUnYinG0W6lTJEmnJG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم‌نامه ممکن است زودتر از نشست سوئیس امضا شود
آکسیوس، ترجمه ماشین:
آمریکا، ایران و میانجی‌ها در حال گفت‌وگو درباره برگزاری مراسم امضای یادداشت تفاهم هستند؛ مراسمی که در حال حاضر برای جمعه برنامه‌ریزی شده، اما به گفته یک دیپلمات از یکی از کشورهای میانجی و یک منبع دوم آگاه از گفت‌وگوها، ممکن است زودتر و حتی روز چهارشنبه برگزار شود.
چرا مهم است: اگر چنین اتفاقی بیفتد، یادداشت تفاهم به‌صورت الکترونیکی امضا خواهد شد، بخش‌های مربوط به تنگه هرمز در توافق اجرایی می‌شود و آمریکا ممکن است سرانجام متن توافق را منتشر کند.
منبع دیپلماتیک گفت گفت‌وگوها درباره جلو انداختن جدول زمانی با هدف باز کردن تنگه هرمز زودتر از جمعه انجام شده، چون هر دو طرف درباره این موضوع توافق داشتند.
عامل دیگر می‌تواند فشار سیاسی بر کاخ سفید برای انتشار متن یادداشت تفاهم باشد.
منبع آگاه از گفت‌وگوها مدعی شد این ایران بوده که خواسته متن تا زمان امضای رسمی منتشر نشود و رد کرد که کاخ سفید در واکنش به فشار سیاسی چنین تصمیمی گرفته باشد.
وضعیت فعلی: تا صبح چهارشنبه، هیچ تصمیم نهایی درباره تغییر زمان امضا گرفته نشده بود.
کاخ سفید از اظهارنظر خودداری کرد.
خبر اصلی: حتی اگر زمان امضا تغییر کند، نشست هیئت‌های آمریکایی و ایرانی، به ریاست معاون رئیس‌جمهور ونس و محمدباقر قالیباف، رئیس مجلس ایران، طبق برنامه روز جمعه در سوئیس برگزار خواهد شد؛ این را منابع گفتند.
انتظار می‌رود آنها درباره آغاز مذاکرات بر سر برنامه هسته‌ای ایران گفت‌وگو کنند.
نکته مبهم: یک مقام ارشد دولت به خبرنگاران گفت این توافق روز یکشنبه به‌صورت الکترونیکی از سوی رئیس‌جمهور ترامپ، ونس و قالیباف امضا شده است.
منبع دیپلماتیک مدعی شد چنین امضایی انجام نشده است.
منبع آگاه مدعی شد که این امضا انجام شده و امضای جدید یک «امضای دوم» خواهد بود. روشن نیست چرا دو امضا لازم بوده است.
چه چیزی را باید زیر نظر داشت: کاخ سفید از روز یکشنبه گفته است که باز شدن تنگه از سوی ایران و لغو محاصره آمریکا فقط از روز جمعه، پس از مراسم رسمی امضا، آغاز خواهد شد.
به گفته منبع دیپلماتیک، اگر توافق زودتر امضا شود، این روند هم جلو خواهد افتاد.
axios.com
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/76453" target="_blank">📅 19:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76452">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cc6738c570.mp4?token=qO8YkCUlvUZlGxzqzex3T6ioL9Ihd-z2HMQbwVqtI0Mfom3nZbnYO4F_bPg-QqgEJxO1VmMNCnfs-ifmWQNapYl5_sNDN5-_xvmrGdTvBkl21SnTICXdIiYRoUTKdP-9nani6kk8FMTsbV9y36xXn1Zh1QbL-O32o0d2PVfN7VgGCugS5C4pw2aWSB2p6RxOO7pbpLqsUWJZHoy7RJBAdPTO1PB6MvPeq-MR-eM9O3OIpdN3zLZDKi_1eS9Un5qyuw3wTrKq0ezYO7gIqFaiabWA6WP08Pq6im4IDIRLBkPZkio1NB_KiBO6VANS8oTN_voO6sKB6VuXwqXB2FESFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cc6738c570.mp4?token=qO8YkCUlvUZlGxzqzex3T6ioL9Ihd-z2HMQbwVqtI0Mfom3nZbnYO4F_bPg-QqgEJxO1VmMNCnfs-ifmWQNapYl5_sNDN5-_xvmrGdTvBkl21SnTICXdIiYRoUTKdP-9nani6kk8FMTsbV9y36xXn1Zh1QbL-O32o0d2PVfN7VgGCugS5C4pw2aWSB2p6RxOO7pbpLqsUWJZHoy7RJBAdPTO1PB6MvPeq-MR-eM9O3OIpdN3zLZDKi_1eS9Un5qyuw3wTrKq0ezYO7gIqFaiabWA6WP08Pq6im4IDIRLBkPZkio1NB_KiBO6VANS8oTN_voO6sKB6VuXwqXB2FESFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهوری آمریکا در دیدار با نخست وزیر هند در حاشیه نشست گروه هفت گفت: تغییرات جمهوری اسلامی با دستور من برای کشتن قاسم سلیمانی آغاز شد.
دونالد ترامپ افزود: جمهوری اسلامی رده اول و دوم رهبری خود را از دست داده و اکنون با توافق من هرگز به سلاح هسته‌ای دست پیدا نخواهند کرد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، گفت از حق اسرائیل برای دفاع از خود حمایت می‌کند، اما انتظار دارد این کشور در تصمیم‌گیری‌هایش «قضاوت درست» داشته باشد.
@
VahidOOnLine
ترامپ در پاسخ به پرسش خبرنگاری که از او پرسید «آیا برخورد گرم رهبران اروپایی نشان‌دهنده همسو شدن آن‌ها با جهان‌بینی شماست؟»، گفت: «فکر می‌کنم آن‌ها به این نتیجه رسیده‌اند که حق با من بود. یک‌جورهایی همیشه حق با من است و در نهایت، آن‌ها هم معتقدند که حق با من بود.»
رئیس‌جمهوری آمریکا که در کنار نارندرا مودی، نخست‌وزیر هند با خبرنگاران صحبت می‌کرد، با اشاره به تمایل ناگهانی دیگر کشورها برای ورود به فرآیند توافقات اخیر افزود: «حالا یک‌دفعه همه‌شان می‌خواهند وارد ماجرا شوند و مشارکت کنند؛ در حالی که کار دیگر تقریبا تمام شده است و اصلا دلیلی ندارد آن‌ها را مشارکت دهیم.»
@
VahidOOnLine
بقیه حرف‌هاش (بی‌ربط به ایران):
۲۰ دقیقه ۲۲۰ مگابایت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76452" target="_blank">📅 18:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76451">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJkK5_s6ZHeqP2t6Gfvh1Lt8eTSALo2EyQgL_nVMh4nhtM7yNChs4MfQpIPSYzUbmugZHCKfytVANTojx6T9P5W-MlLw5Ef8BtPrDcrewcL4nBnR_MrNmzeXakwexxNCE48DdruEBnFEfTcNF6PIKf04xnOknyXW_cd2MQfGCuf4Rj7RoLuYmvKOUiQvC9nIEDnZcibC4X4VQR1xjDeq9EkCfqLmc2KOMBUVGeqfpwj0RfDQ8L9hR3jG-jhAHDhPnEeZT--KMwLx1XVOTEXMoxaGZxaIHLrWOK8u9FMMopVaX85wfiv-PmtNuhuyEkaVnD9aqfjI8YysSgJX4PNDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من ۴۵ دقیقه دیگر از فرانسه یک کنفرانس خبری برگزار خواهم کرد. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه بازمی‌گردم!
این سفر موفقیتی بزرگ بود، اما چیزی که بیشتر از همه می‌خواستند درباره‌اش حرف بزنند، این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد.
در همه شاخص‌ها، ارقام مربوط به اقتصاد ایالات متحده عالی است؛ امروز شمار افرادی که مشغول به کار هستند از هر زمان دیگری بیشتر است. بیش از ۱۹.۱ تریلیون دلار در آمریکا سرمایه‌گذاری می‌شود، کارخانه‌ها و همه چیزهای دیگر در حال شکل‌گیری است؛ اما نکته مهم این است که ارقام اخیر بازار سهام به خاطر این توافق سر به فلک کشیده و به همین ترتیب، قیمت نفت هم به‌شدت در حال سقوط است!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/76451" target="_blank">📅 17:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76450">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RO4jgyTllRujQvGbDOF6eDLZhsrXCCbVbLn3j6PedJlhu1062iDrhFORyMRD-LuQsuMlbKiEz13W6y8tt6hFH15S-IcGxwDS1z2IvpiH-iJ_DIonhM80vMqWczWbqefJyw0rUsmV1stc-nKRfPKGDUHqGvQZG_deSUt_7plpS30VZ6nKivosyZDb8KOtyTaOZzuh8znT6JJksPdQPhZ8HBOUgjcgznFzOifpVs79N8sQiv0lMOGHHnfM2rRhrai0job1b24vg5KVU5u9NePWKxkE-itbYquO2mk374ywnXeqbOy5wL4p2nOaMwgATHNdULbSLbc6idcLSHDJYhIx-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری آمریکا، در گفتگو با برنامه صبحگاهی شبکه سی‌بی‌اس (CBS)، از سیاست‌های دولت دونالد ترامپ در قبال جمهوری اسلامی ایران دفاع کرد و به انتقاد از کسانی پرداخت که به گفته او، صرفا به دنبال تداوم درگیری نظامی هستند.
ونس با تفکیک میان «ابزار» و «هدف» در سیاست خارجی واشنگتن گفت: «رئیس‌جمهوری از دیپلماسی، اهرم‌های اقتصادی و فشار نظامی استفاده کرد تا مطمئن شود ایران به سلاح هسته‌ای دست پیدا نمی‌کند؛ هدف اصلی همواره همین بوده است». او با انتقاد از تندروها افزود: «بعضی‌ها فقط می‌خواهند بمباران‌ها ادامه داشته باشد، بدون اینکه توجه کنند آیا این کار اصلا دستاوردی برای مردم آمریکا دارد یا خیر».
معاون رئیس‌جمهوری آمریکا در پایان تاکید کرد که هدف ترامپ ایجاد بدبختی و رنج برای مردم ایران نیست، بلکه تمرکز اصلی دولت او، مهار برنامه‌های تسلیحاتی و جلوگیری از دستیابی تهران به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76450" target="_blank">📅 17:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76449">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MCIiJVwVLBJD6BGQ0JIKSDWejHA_FRYESKWwI5AGesCH7utK_RslF47avrFDSPxr6Jji1FgSBRB5PwW0Lo5XQhNoqx1McPopmuGSpabroTkoSx_aNeGwtYpP3qUiJ6_PJFjQUvRVqc2Itfp9w8lK4vYH4wYlHAQAKf4K3Nm_aeZAdvLHkTiCW4l35Ha4cGiwYQ__7T8X2rmrsOY8UmWJ-qnOJOsIz1frJdOZck1QhjG-a9NOI0MvJ4aan62Vb1Jqh3JRzLDisjva28Hb_bAhM1ooV3pb2VTr-XnNaLxkjeJnygE46A8Agz4SE9P1AE_L01o2rlaJ4-xpi_csTzeSRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76449" target="_blank">📅 17:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76448">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/790e3a4857.mp4?token=Qq3DZUW0JRWvWndiHlEt1Jrph2N6Fj5QLxHkQJ0CB7I1TPJeSkvW7vzND5OI-a9a0kBKJPTA6mChOuzglk-l0ubnH_7MYAkAJp4eM98Jhqjx457sLqV6NC9vNOC1_jvUrqMHcZYxXY2LX3Z82fnvR2nL8ymSJpmtn30K5jsNI9IYDrPYHqdKVJtjjUZB5lcrZp8M3hV45-0_EhU67OjkRaIL7AHcWJe-_cZwiG3zGP35bO1YDyxELDzUbPbzSyk1hsrOEPYU2iJN4boS0Ag_KWBWWiOpqtOXx-d9jWQzSOPtt6OJRcbD-NnYqiXQftK3Qa79itarX-M7eNpIX9kjXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/790e3a4857.mp4?token=Qq3DZUW0JRWvWndiHlEt1Jrph2N6Fj5QLxHkQJ0CB7I1TPJeSkvW7vzND5OI-a9a0kBKJPTA6mChOuzglk-l0ubnH_7MYAkAJp4eM98Jhqjx457sLqV6NC9vNOC1_jvUrqMHcZYxXY2LX3Z82fnvR2nL8ymSJpmtn30K5jsNI9IYDrPYHqdKVJtjjUZB5lcrZp8M3hV45-0_EhU67OjkRaIL7AHcWJe-_cZwiG3zGP35bO1YDyxELDzUbPbzSyk1hsrOEPYU2iJN4boS0Ag_KWBWWiOpqtOXx-d9jWQzSOPtt6OJRcbD-NnYqiXQftK3Qa79itarX-M7eNpIX9kjXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی: خامنه‌ای در «عراق» هم تشییع می‌شود
علیرضا زاکانی، شهردار تهران روز چهارشنبه ۲۷ خردادماه برای نخستین بار و برخلاف گفته‌های پیشین مقام‌های جمهوری اسلامی اعلام کرد که مراسم تشییع علی خامنه‌ای در عراق هم برگزار می‌شود.
زاکانی به خبرنگاران گفت پس از دو روز مراسم وداع، جسد علی خامنه‌ای در روز ۱۵ تیر در تهران، ۱۶ تیر در قم و ۱۷ تیر در عراق تشییع خواهد شد.
مقام‌های جمهوری اسلامی پیش از این اعلام کرده بودند که رهبر پیشین  در مشهد دفن خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76448" target="_blank">📅 16:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76447">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6d8cc30b9b.mp4?token=kzJIaf8HHBWxokFRkIGbhiEn33RQQpsvuFtyp3yoIbNJzzIcVHgLutJc1jnMqYJZoMK17P6A5v_6sGFAL8wr2NlNmkDDGta6ZjPFub232bJ-fTpCYhsICAARiMqB0WU8Sy8te1NER0TR3h9F5fmJtV1KLuWiTavv4NLr4SehcWNdD6mWpRzF6rogK03CXq2A288qUX51es16jiKnYq92QV3yP6ZixB5EAF9x_vu1xpKrTTtmPyNMImRyNGdwB1E2w0gn0LVHd9EPh6QNzrgIOAg8CO_RDf_lXIVyawk0yd3o6mcA39g-ilsGc2D6badXgyKsp4TS-anWWMiQkJ72IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6d8cc30b9b.mp4?token=kzJIaf8HHBWxokFRkIGbhiEn33RQQpsvuFtyp3yoIbNJzzIcVHgLutJc1jnMqYJZoMK17P6A5v_6sGFAL8wr2NlNmkDDGta6ZjPFub232bJ-fTpCYhsICAARiMqB0WU8Sy8te1NER0TR3h9F5fmJtV1KLuWiTavv4NLr4SehcWNdD6mWpRzF6rogK03CXq2A288qUX51es16jiKnYq92QV3yP6ZixB5EAF9x_vu1xpKrTTtmPyNMImRyNGdwB1E2w0gn0LVHd9EPh6QNzrgIOAg8CO_RDf_lXIVyawk0yd3o6mcA39g-ilsGc2D6badXgyKsp4TS-anWWMiQkJ72IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس جمهوری اسلامی و رییس هیات مذاکره‌کننده جمهوری اسلامی با آمریکا، درباره اهمیت روابط اقتصادی با چین گفت جمهوری اسلامی باید از مرحله تقابل عبور کند و بر توسعه اقتصادی متمرکز شود.
قالیباف در نشست همفکری نماینده ویژه در امور چین با اتاق بازرگانی ایران گفت: «باید سنگر را از بچه‌های لانچر تحویل بگیریم، مردم را از زیر فشار اقتصادی دربیاوریم و کشور را بسازیم.»
او با توصیف جایگاه چین به‌عنوان کشوری «منحصربه‌فرد» برای جمهوری اسلامی در حوزه تجارت، افزود پکن باید باور کند که تهران «شریکی به تمام معنا» برای چین است.
رییس مجلس جمهوری اسلامی گفت هر بلوکی که با حضور کشورهای ساحلی خلیج فارس شکل بگیرد، محوریت آن «حتما چین و جمهوری اسلامی» خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/76447" target="_blank">📅 16:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76445">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lXpvEW8SeEy5EsYn8KnnDasWyejGn0oUgukNl8ONA3F5ukia4HPsNKfysk5l3mwKPt3OB0wUx0ze6ECWLKYhryJ-sZxpj5Wmtnza8D8hSyzk7ruasHOA8IExqdNsVW-4IBcW5JxIGAfsCKDCSt1WlLrnIPIt1SNvrVXHlmfnPgZU7SXZtmL11Zc6lvtcxgcvBPA_AX7_rJoIgMS16oulsBziQT1ipaU-uF5HqahH-QMMFif9pDv5BTebnKPuKI_eo6JgGYecOoCTBSm-vBIZgOTsBuu76aHMj-oTm4HGf8S08-GGM-vJocQd1121u7uxHaEeoBKnhSHosCybDaXLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cda5339562.mp4?token=Cdi0NqZLsutwHQ7h-oV7lG-G3JTd8F4Xu-_vGxycsJNdwcdeb651VeyAwPiDH_TfqmA39x4DLSJHUZUzDLW_pXNFVuhdZU5Wr5Pu1gzLwkH5QQe4owS4z0GwfLaTLuyWatksD96Q63NygrRZChta7LfPBqH-I08CouIqbP0gC-WFap8N2M4H4f-vf78kR4Vo-3Pcg1Erm93g-ZVLgtWpdgjLeFLVJ7MwHmslkfkcfwTemOrJjlIxv0tCicYDw8-lNLUruwCgaqM7_4QhRzDrQJYRnXy5sWSE0IUQXck6eyvXQIM2GX7egyrJ6A8_NZgxrsEF6ZxPP-FHKMi00XVZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cda5339562.mp4?token=Cdi0NqZLsutwHQ7h-oV7lG-G3JTd8F4Xu-_vGxycsJNdwcdeb651VeyAwPiDH_TfqmA39x4DLSJHUZUzDLW_pXNFVuhdZU5Wr5Pu1gzLwkH5QQe4owS4z0GwfLaTLuyWatksD96Q63NygrRZChta7LfPBqH-I08CouIqbP0gC-WFap8N2M4H4f-vf78kR4Vo-3Pcg1Erm93g-ZVLgtWpdgjLeFLVJ7MwHmslkfkcfwTemOrJjlIxv0tCicYDw8-lNLUruwCgaqM7_4QhRzDrQJYRnXy5sWSE0IUQXck6eyvXQIM2GX7egyrJ6A8_NZgxrsEF6ZxPP-FHKMi00XVZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ می‌گوید اگر از توافق رضایت نداشته باشد و ایران رفتارش را اصلاح نکند، بار دیگر ایران را بمباران خواهد کرد.
رئیس‌جمهور آمریکا که روز چهارشنبه در نشستی خبری همراه با عبدالفتاح السیسی، رئیس‌جمهور مصر، در حاشیه نشست رهبران گروه ۷ در فرانسه صحبت می‌کرد، گفت: «این فقط یک یادداشت تفاهم است. اگر از آن راضی نباشم و رفتارشان را اصلاح نکنند، دوباره به سمت آن‌ها شلیک می‌کنیم و روی سرشان بمب می‌اندازیم.»
دونالد ترامپ همچنین گزارش‌ها دربارهٔ سرمایه‌گذاری ۳۰۰ میلیارد دلاری این کشور در ایران بر اساس تفاهم‌نامه را نادرست خواند، اما گفت که آمریکا مانع سرمایه‌گذاری دیگر کشورها در ایران نخواهد شد.
متن تفاهم‌نامه هنوز  منتشر نشده، اما بر اساس یکی از بندهای متنی که برخی رسانه‌های آمریکایی منتشر کرده‌اند، چنین ذکر شده که «ایالات متحده متعهد می‌شود همراه با شرکای منطقه‌ای خود، طرحی جامع و مورد توافق دو طرف برای بازسازی و توسعه اقتصادی جمهوری اسلامی تدوین کند و تأمین مالی دست‌کم ۳۰۰ میلیارد دلار را تضمین نماید. سازوکار اجرای این طرح، به عنوان بخشی از توافق نهایی، ظرف ۶۰ روز تدوین خواهد شد».
رئیس‌جمهور آمریکا همچنین گفت در متن تفاهم‌نامه گفته نشده است که آمریکا پولی به ایران پرداخت می‌کند و وجود بندی دربارهٔ رفع فوری تحریم‌های ایران در متن تفاهم‌نامه را نیز رد کرد.
در متن منتشرشده در رسانه‌های آمریکایی، که صحت آن هنوز مورد تأیید قرار نگرفته، آمده است که «ایالات متحده متعهد می‌شود بر اساس جدول زمانی مورد توافق در توافق نهایی، همهٔ انواع تحریم‌های اعمال‌شده علیه جمهوری اسلامی ایران را لغو کند؛ از جمله قطعنامه‌های شورای امنیت سازمان ملل و شورای حکام آژانس بین‌المللی انرژی اتمی و همچنین تمامی تحریم‌های یکجانبه آمریکا، اعم از اولیه و ثانویه».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/76445" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76444">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oZSwjz6aJ2qy7HPcimOI43n17BcmB-8DsZ84yuGCj_Rsp-rrN1BM1IBrG3HNVE_PGWDMp4fjH29B2FJzqtoLisFvAXKF51efxieJC-2CJvuaperokpKupTghJtRHfGhQyjrsCuk7XwBRl5Q9i62b3UftapkphryqdjZJnzFPuavWCK8zmuO63V0OiAzni2IaL5kkRp3fH5bsrerVDnuhUsqCYIt_oqcwDpn8pIZfSm6x8as92ZlaXxvBKjJRvB0hfPkLvrx_0Ay78vCbELXv1FZ77NSoJt45fLeSTTOF8A8SXI94S_G5Y015iTmy92tAmn7S-dxlmYqSfY_LFaMwAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی و سیاست خارجی مجلس جمهوری اسلامی، با انتقاد از یادداشت تفاهم میان جمهوری اسلامی و آمریکا، این توافق را «نامتوازن» توصیف کرد و گفت همه خطوط قرمز جمهوری اسلامی در آن رعایت نشد.
رضایی در یک گفت‌وگوی تلویزیونی افزود جنگ پایان نیافته و نباید تصور کرد شرایط از وضعیت تقابل خارج شده است. او گفت: «ما در یک جنگ ترکیبی تمام‌عیار هستیم و باید از فرصت ایجادشده برای قوی‌تر شدن استفاده کنیم.»
سخنگوی کمیسیون امنیت ملی مجلس جمهوری اسلامی همچنین از منتقدان یادداشت تفاهم دفاع کرد و گفت نباید مخالفان تفاهم را «تندرو» خواند. او افزود: «اگر این افراد نبودند، الان سربازان آمریکایی بالای سر ما بودند.»
رضایی پیش‌تر نیز در شبکه اجتماعی ایکس نسبت به نحوه دفاع حامیان توافق از این تفاهم‌نامه انتقاد کرد. او از مقام‌های جمهوری اسلامی خواست از منابع عمومی برای تبلیغ «توافق» استفاده نکنند، منتقدان را تحمل کنند و برای توجیه تصمیم‌گیری‌ها از رهبر جمهوری اسلامی هزینه نکنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/76444" target="_blank">📅 16:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76443">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z38qYMIDebmK5pg2Vg1pVRATdQ2Xtmer6o3tuv9W7108tBM0x72weBYCYiJPg2Cx7ZBlx4KAyPi6DLDKcKQDoWh5waNPMcxlEfQhU-T5Rv81cyLBqv_IFsofNMbSqQikkMNbDGgTfuk_w9UvX9ZW1i5AnfIamhULvdNpaiA69ypbG_42f3hPZ74UvTvP-XA_zNcw4ScUUxAkfJtTLUau6VErEyQ0Dc34uZXiuG0iq9DsbTsqllwZhVjoH7BebHsXrckKVUwBU_TuJGfza6VdmrvZRjP-mQlkGIdVKy1Y_sAYtbCGKddPtKIW9ZZesVAJ22nEEgkTQqjTG79dixfT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامهٔ روند کاهشی قیمت ارزهای خارجی در بازار آزاد ایران، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان رسید و قیمت سکه طلا هم در محدوده ۱۶۰ میلیون تومان اعلام شد.
قیمت دلار آمریکا که در مقطعی تا ۱۹۰ هزار تومان بالا رفته بود، تا کنون حدود ۲۰ درصد کاهش پیدا کرده است.
قیمت هر گرم طلای ۱۸ عیار نیز روز چهارشنبه به ۱۵ میلیون و ۷۶۷ هزار تومان و «سکه امامی» نیز به ۱۵۹ میلیون و ۵۰۰ هزار تومان کاهش یافت.
در مقابل، شاخص بازار سهام بورس تهران از زمان اعلام توافق رشد چشمگیری داشته و روز چهارشنبه با ثبت رکوردی تازه به بیش از ۵ میلیون و ۱۰۰ هزار واحد رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/76443" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76442">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py3YkAWdoW2X9PErpp0MThPjVMcnfG46icQw4wwbDbERFw5YZTSofqiwjqa5llaSeqRiM3OI9TmaThdzcUhzLhs_6pobzUsMMSM26uY3TYhWK745IZUe2JodzuC8barFbrH15z2ciATKWzq1725mqM9FI4q4j363x_Q89dHs-7VFS28mE7Q7SwbMQgd6Ob6VLVWCOQeqWWuGccl6eaWljk3UQtwUqZIrnfoRzS9DwhR21Di9u_72P93xfnORD1Dg_wt5MTgmj4LYRk9Sr2p1B-__KRePQy0bGftl49wnFqEH2OYQndj3s03dxEdkbyvLiag5ai06jGp3Ry8o6Xy_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سران هفت کشور صنعتی جهان (G7) در بیانیه پایانی نشست خود از توافق میان ایالات متحده و جمهوری اسلامی حمایت کردند و آن را فرصتی مهم برای جلوگیری از دستیابی حکومت ایران به سلاح هسته‌ای و محدود کردن فعالیت‌های موشکی و منطقه‌ای تهران دانستند.
رهبران آمریکا، کانادا، فرانسه، آلمان، ایتالیا، ژاپن و بریتانیا همچنین اعلام کردند آماده‌اند در روند اجرای این توافق مشارکت داشته باشند.
در بخش دیگری از این بیانیه، بر ضرورت حفظ آزادی کشتیرانی و عبور بدون مانع کشتی‌ها در آبراه‌های بین‌المللی تاکید شده و این موضوع یکی از ارکان اصلی تجارت جهانی توصیف شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 215K · <a href="https://t.me/VahidOnline/76442" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76441">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D-poUYkOPg-y5iaMx9KEmqgKKCOCGh8zV8QDk47uKM_H9ssqUrO9kJ-CKj3RqE97p94axIjcpLNcrRf-BIWnFlSXPH1g0sIHxJenPphUXwHj6xlgCUf4epkXctTClP9ZzbaD5FTjtfNTLFqxA939gJ1ORdloBoJU-YjqQ21H0GNzKM6WKqDbclXN7wsL05_RwD6G1BUtAROshu4sSL3syUsYV-ohNFH87vJNf5x8A4NSv46PV3GHAJU4chF-gCvV4mMXYE7dPnR_2oUnkSa_aQzUax3a9RefgKCiaPbEUdGt-WscxxTOu9bXS7jrKKXKCs0OJCfZmTotwBLugNEBww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مهری فرج‌زاده» ۳۶ ساله، ساکن کرج و مادر دو فرزند، روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در فردیس کرج هدف شلیک گلوله قرار گرفته و جان خود را از دست داده است.
به گفته منابع مطلع، گلوله به ناحیه جمجمه او اصابت کرده بود و مهری فرج‌زاده پیش از رسیدن به بیمارستان «به‌آفرین» فردیس جان باخته بود.
نزدیکان او می‌گویند پس از دو روز پیگیری، پیکر مهری فرج‌زاده را روز ۲۱ دی‌ماه از بهشت سکینه کرج تحویل گرفتند.
مهری فرج‌زاده خانه‌دار بود و دو فرزند داشت. دختری ۱۵ ساله و پسری ۱۰ ساله که با کشته شدن مادرشان با فقدانی جبران‌ناپذیر روبه‌رو شدند.
@
VahidHeadline
آپدیت:
پیام دریافتی: پسرعمه‌ی مهری، اکبر حسن‌پور هم ۱۹ دی تو گوهردشت کرج با گلوله کشته شد. اکبر دو دختر ۱۶ و ۱۸ ساله داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 220K · <a href="https://t.me/VahidOnline/76441" target="_blank">📅 15:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76440">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOnUeOGziP8o3U9stVWBLTVnDkAIdPdw58lTPUaT8yOihNx-aJ_K5jgDZW3a8PTAcgVw2i8M_yXDnnTyBloMGcrqvBz5HikbvZKfabiJDhOPr4nuNN0PzQPT-GS3t9W_9HZ4Xo4ts0vZjfK-_H5buPfqmO05oggvEC7vP8c7tNMXGsnPV4Cv3fjt27cWy1pgrPSwvFq8iP_oTtM7hiYkige23wIdlOKdf87jZtucpK8c_efQFdlkGZgYLOAVTQqUNz1AGW1pPNZEYEGcEaoQi-PW0CJlM0i13Yi6ZJmkGijFIIws1aTMLfThD4ZSwEQoSY2vNEp7m0pEn8mHp48S2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند از اول ژانویه ۲۰۲۶ تاکنون، ۷۴۶ مورد اعدام را در ایران مستند کرده است که تنها ۵۲ مورد آن از آغاز ژوئن ۲۰۲۶ به اجرا درآمده است.
‏
🔸
جمهوری اسلامی در سایه جنگ و در واکنش به اعتراضات سراسری دی ماه ۱۴۰۴ به اجرای اعدام‌های سیاسی شتاب بخشیده است. از ابتدای سال جاری میلادی تاکنون، دست‌کم ۴۵ معترض و زندانی سیاسی متهم به جرایم علیه امنیت ملی، از جمله جاسوسی، اعدام شده‌اند.
‏
🔸
گزارش‌های رسیده به بنیاد عبدالرحمن برومند نشان می‌دهد که مبنای حقوقی اصلی بسیاری از این احکام اعدام، «اعترافات» اجباری اخذ شده از زندانیان تحت فشارهای جسمی و روحی بوده است؛ امری که نقض آشکار حقوق اولیه دادرسی عادلانه و مصونیت‌های بین‌المللی در برابر شکنجه به شمار می‌رود.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76440" target="_blank">📅 15:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76439">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/649b79d41e.mp4?token=ujmu3fyb_kiWAZ7SbHmIfuBs1GHQq1vYyUUb6NUsOnh6HsIdYQ61dNCrmu1VdE4mkcAWeFasQHwvO3bM6l1l5aEUkltW-H-HTk3j8d5NnIDdk1mpDmi3eSnmwdZ7lBSVIOT5XKH-fzTtzeY7XfIMB9WOkxd2Jac5DEd-mUXc0g7jXQCWzbWUamnknCnzbxhB2zBZc2UTxvlQxT_wg37KTGohJNf_dpr8Zu8U7Gv35laCBEGHgw9-4lWuWfC1j30MEeo_qYz0X1_V62VBjyd--EDRsY7K94nyiUa7UKUg-ZWrFLOqcAVlrp9TwqYG8X79v6WfjwU5c91JGNk5lcbcig" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/649b79d41e.mp4?token=ujmu3fyb_kiWAZ7SbHmIfuBs1GHQq1vYyUUb6NUsOnh6HsIdYQ61dNCrmu1VdE4mkcAWeFasQHwvO3bM6l1l5aEUkltW-H-HTk3j8d5NnIDdk1mpDmi3eSnmwdZ7lBSVIOT5XKH-fzTtzeY7XfIMB9WOkxd2Jac5DEd-mUXc0g7jXQCWzbWUamnknCnzbxhB2zBZc2UTxvlQxT_wg37KTGohJNf_dpr8Zu8U7Gv35laCBEGHgw9-4lWuWfC1j30MEeo_qYz0X1_V62VBjyd--EDRsY7K94nyiUa7UKUg-ZWrFLOqcAVlrp9TwqYG8X79v6WfjwU5c91JGNk5lcbcig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک جت خصوصی تو یک اتوبان در تگزاس سقوط کرده، راننده‌ها رفتن کمک سرنشینها
J74wabx
یک نفر کشته شد؛ پنج نفر به دلیل استنشاق دود در بیمارستان بستری شدند.
AZ_Intel_
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76439" target="_blank">📅 09:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76438">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtYGgKVadH7q-tkDL0UpJybDN-b4CdFfCzLjqJPi2f1cLqHP6YbMY9LEjwQNDZCm8UAZXbDKQnclcrwS7Rrp_SUzAvOGS3OJTQeIaEln6Ow_rGiLDQEoD4TUewFWGg3S_ZvA1tt1l-FycwiFcN-YkvFzyuGEkGAJ-QiAjeTXc2YuduolzynloxoH2c__kfzedumB4GHfuk5VVHn4cEltbtcRWII2vG65EIQYTUnd0CMq2uurvptROYtVmSrCPVYvRy8aGyrtOF-HRUSIKQjP_Rmk5-mPJpbF1XAooZIqYLWpzPeDouhhms-xi6Z3lA89eqOOq4mFTDoociV6wjWNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخستین نفتکش‌های حامل نفت خام ایران از زمان آغاز محاصرۀ دریایی آمریکا، از تنگۀ هرمز خارج شدند. این موضوع را صبح چهارشنبه یکی از وب‌سایت‌های ردیابی کشتی‌ها اعلام کرد.
وبسایت «تنکر ترکِرز» (Tanker Trackers) که ذخیره و حمل‌ونقل محموله‌های نفتی را دنبال می‌کند، بر اساس داده‌های دیجیتال منطبق با تصاویر ماهواره‌ای، «اولین صادرات نفت خام ایران در دو ماه اخیر» را تأیید کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76438" target="_blank">📅 08:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76437">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KL_ZlO4xdNV2Xhn6v_2kh0AZCEr3SC_9ZcALcSPaFv5WkgjfWAgDvi2J0TvERX64tky1Xc2bsO1H0N_uqpM7Z3TIMpqAgqjiTHFGLmhlduxmBnvooiYmj0_Cu3oqenSFM0uiQHbPSJ7jIFlIAaWmScxUUx4m1BQVdRKpedKgOLbZ5gUwU5PCKvreAR584Tv4cD1iGjPP6IgcNMvDXDQ8FwKEcsDOiD8ZO5yQtfbr1qmhQolgHgyC0PyQ1-6yJkzYbneTbz6jAmV3UqvyMSJVpbnJztKc9-6jjhikXuTNkRpQzB6-ULk2oswC1q7r0u1O5nCEYdenlrAxckMDFt12EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ان‌بی‌سی، حکومت ایران پس از اعلام یادداشت تفاهم با آمریکا، همچنان تعداد «زیادی» پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است.
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی گزارش داده که سپاه پاسداران پهپادهایی پرتاب کرده که آمریکا توانسته آنها را پیش از آنکه تهدیدی برای شناورهای تجاری، کشتی‌های نظامی و خدمه حاضر در منطقه ایجاد کنند، رهگیری کند.
بر اساس این گزارش، سپاه پاسداران از زمان امضای «الکترونیکی» یادداشت تفاهم در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76437" target="_blank">📅 05:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76436">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/75a49fba40.mp4?token=nh9xGAROSc4r_CilKa9tUTPX5xYYzHH82ymzYFRH_pvS4Q-URel3c8AO0xRNUsP9KS7L4GR-3Va3S0qn1Q4eok8GUpShv2r2eq7XZVIHEpwEnAjPYVCrzBE4Ic8dPB6FkUzcBm1VVTwpMs8t26zlDAPM1_DgSYK2EN0YsfYoDn9loaphGMphc6Bp94E0c_t8dhDXH07Vwz6_VlRtHM_6XHx04wbz8aIw_9oJ3lXQknx2r8vHgPEDc_PjUBKDpMwZSkyc4pg5A6KWOPMUcWZ_-GZRRFd91eFAgNtiQCBiKDJ-t3gC4ZCJsMDhHI2o_WE5b7BaSVkXSwxjaAh3W4-Leg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/75a49fba40.mp4?token=nh9xGAROSc4r_CilKa9tUTPX5xYYzHH82ymzYFRH_pvS4Q-URel3c8AO0xRNUsP9KS7L4GR-3Va3S0qn1Q4eok8GUpShv2r2eq7XZVIHEpwEnAjPYVCrzBE4Ic8dPB6FkUzcBm1VVTwpMs8t26zlDAPM1_DgSYK2EN0YsfYoDn9loaphGMphc6Bp94E0c_t8dhDXH07Vwz6_VlRtHM_6XHx04wbz8aIw_9oJ3lXQknx2r8vHgPEDc_PjUBKDpMwZSkyc4pg5A6KWOPMUcWZ_-GZRRFd91eFAgNtiQCBiKDJ-t3gC4ZCJsMDhHI2o_WE5b7BaSVkXSwxjaAh3W4-Leg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون دونالد ترامپ که روز جمعه در سوئیس تفاهم‌نامه پایان جنگ با ایران را امضاء خواهد کرد، گفته مفاد این توافق اولیه در یک جمله چنین خلاصه می‌شود که اگر ایران به تعهدات خود در چارچوب این توافق عمل کند ایالات متحده آماده فراهم کردن زمینه برای بازگشت این کشور به صحنه اقتصاد جهانی است.
آقای ونس روز سه‌شنبه در گفت‌و‌گو شبکه رادیویی سیروس ایکس‌ام گفت: «دونالد ترامپ هرگز نگفت که هدف اقدامات او به قدرت رساندن رضا پهلوی در ایران است. آنچه گفت این بود که اگر مردم ایران بپا خواسته‌اند و مقابل حکومت خود ایستاده‌اند، خیلی هم خوب است اما آنچه او می‌خواهد اطمینان یافتن از فعالیت‌های هسته‌ای ایران است چه از طریق دیپلماتیک و چه از طریق جنگ که خب در نهایت راه دوم روی داد». 06:21
معاون رئیس جمهور آمریکا همچنین تصریح کرد که خواسته منتقدان آقای ترامپ مبنی بر ادامه جنگ با ایران با آن چه دونالد ترامپ به مردم آمریکا همیشه وعده داده و قصد اجرای آن را دارد، «همسو نبوده و نیست.»
آقای ونس در این مصاحبه چند بار تاکید کرد که آنچه به لحاظ اقتصادی ایران از آن منتفع خواهد شد «به هیچ وجه» از منابع و دارایی‌های آمریکا پرداخت نخواهد شد بلکه در صورت همکاری ایران و اجرای همه مفاد توافق، آمریکا با رفع تحریم‌ها به سرمایه‌گذاری در ایران «فرصت» خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76436" target="_blank">📅 03:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76435">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uDdALQ1HdDLnxxtemaRIJ2zzQ-W81I3eyWABs0NVWUrQzogBUfbymf1MskvLppNWnj0HWvp_YVOC90hvNKxA34rErpTiUc_bQM7BnihrECusPP7TnXNz-EH-3RpAyyE7Q1iIVXoWnOdIV15HXPM6tYcsVUEGdzzMkmxSfztACvldssJQSyE39HF0L2Xk6cuCP9zuUyNRlauPhePMDhjYvqbkhT3h0c-SqzNBRRmS3drDoeMWH3HR9t32lqvlRe2461sfqItcRMSe3Gj_ZAACHAvb9cq7ST6smGE39Q5A1qgPyDSMKeJ7eqphg-N4qtj5E9JR5p4MdR-7CFEq0M2_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری که در شبکه‌های اجتماعی
منتشر
شد، دارا خسروشاهی، مدیرعامل ایرانی‌-آمریکایی شرکت اوبر، را در استادیوم سوفای لس‌آنجلس و در جریان دیدار تیم‌های ایران و نیوزیلند در جام جهانی ۲۰۲۶ نشان می‌دهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76435" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76431">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZSjtM6cbzHjGDJKsjw82cvu4-sG6so3vqRH_Y1Lz3scaMXmqyqEMqxrxjiRJCKoXR5j2joJtBRp890KkzGMGid6_oFFYmmsLOqvHKWj6as8c2Xwi9wY-UehA7UWx3blXfAb5D7t7z7LK9mC_mlu70UQuJ8l1q_hIzWvWSSU1w3nSZjxYPHYvqkSEMMGsBkHjjpLDgGvZ07VxvRz4aah1If8DuKirrn3AvNW801M-FEtM3kJS56fNVhwE6mFnbrD37CJ9EMZbJLlieqpZ1lChoDMMk2P0KCigH7XVMMlBU4OoXhjfiEZsZcl5h0_C-7w6XO79cZ8JHhCzLQxi_Xf6Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tctHmXPMhKL_TYF68ZAMsZ2U1Amka06rqr482HhTP2g27D8cvcg3tJRNFZ9LnWkpG-tQkDmKmsaWbQ0nBcrzDzTn-oklpTiRKTkDaoZa1g9g5eIRBaXpYdbSNnZyiCBcazlgdGUyFKXb-XjTdTXxkJIWb_UW6hjL8z7s2VGrQS4pyBDK1UBgHrTb5TDgS23nknHsau1gRv5_lAMoK0X6rmx4Z8AEuC8slRimTvS7GBPqVPxef603L_8NG5dZQ3Mwr2OzucUpTMvF2rUFAznMuuIh5yTDJ0BeJWfWXuixJdAd6FdyZywny5Dv947G1ErWP8kML-dYUf5dTZHiEGSo-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NMvUV759BmCQOZ3zWWMmyao2sdv-AAxfitYf2n-KkBPpMMchcIV-V_cYyXhMOBnImobOE4dABZf4sf3eqHaVTKXMmYIkakem3o6OkJti2mRQ0Nm4anOx-JPsXn8di8_jz8H20lHkuXvNRET8ZTGdBeI5BD1FpnTLF-K5holw_boK4q2AGnEG8-3oBZWoyUprxzy-mJur3MawLTMk80HLk-9PYbZgT98RuVm5vgw40qWjY6-sSaVxuVTrv-ZzG_0VukcDTKbYbfSbkOS_m1-twXQvqhHEOM3SW_YsjI3q9q4L4U-9IvQOmkWNhxA_DSUY1kdqOaMSD44nEl1CSj2EmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/57a8c06d44.mp4?token=AZIgm9Wk_4-cKeKNHA2REFFPb0zWmD6Z0JgtwnNFuvKk3mkVMkf9NEr7pwT9vEeiI2ndEok6a4vgW6ztAQ4kEkB_v4ArTfwXd4BL7hvqwMaEJVNfuRHLCDRNm-5vn4vd_8G_cbHUCAlyW87If6Ot0j1Ob6V7e-lsENnfVKWATeF5Z8NIfpSfPBYg1y2mQJg3ApAFSDhM8N7esOWHYdl_CfxS9M5qTZP65y3-NQhvZA9GVfBTziGnQnuELvpIuuGIjhc6Wdib1hI1niDgZa6WtEqM2WVlx3HlRDGhGp1PV-0WFcNAkyIWqvp5BBVQfjaHGi8wrh2oSDczCDGIxCZlWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/57a8c06d44.mp4?token=AZIgm9Wk_4-cKeKNHA2REFFPb0zWmD6Z0JgtwnNFuvKk3mkVMkf9NEr7pwT9vEeiI2ndEok6a4vgW6ztAQ4kEkB_v4ArTfwXd4BL7hvqwMaEJVNfuRHLCDRNm-5vn4vd_8G_cbHUCAlyW87If6Ot0j1Ob6V7e-lsENnfVKWATeF5Z8NIfpSfPBYg1y2mQJg3ApAFSDhM8N7esOWHYdl_CfxS9M5qTZP65y3-NQhvZA9GVfBTziGnQnuELvpIuuGIjhc6Wdib1hI1niDgZa6WtEqM2WVlx3HlRDGhGp1PV-0WFcNAkyIWqvp5BBVQfjaHGi8wrh2oSDczCDGIxCZlWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکان جلسه امضای تفاهم‌نامه
ترجمه ماشین:
توافق چارچوبی میان آمریکا و ایران قرار است روز جمعه، ۱۹ ژوئن، در بورگن‌اشتوک امضا شود؛ نه آن‌طور که ابتدا تصور می‌شد، در ژنو.
این موضوع را وزارت امور خارجه فدرال سوئیس، در پاسخ به شبکه SRF تأیید کرده است.
وزارت خارجه سوئیس توضیح داد: «این مکان، یعنی بورگن‌اشتوک، از سوی میانجی‌ها، پاکستان و قطر، و همچنین آمریکا و ایران پیشنهاد شده است.»
به گفته این وزارتخانه، سوئیس زمینه گفت‌وگوها را فراهم می‌کند و شرایط دیپلماتیک لازم را ایجاد می‌کند تا این دیدار بتواند در سوئیس برگزار شود.
وزارت خارجه سوئیس درباره روند برگزاری و جزئیات امضای برنامه‌ریزی‌شده، اطلاعاتی ارائه نکرد.
srfnews
چت‌جی‌پی‌‌تی:
«بورگن‌اشتوک» به‌عنوان منطقه/کوه در سوئیس است، ولی مجموعه هتل‌ها و ریزورت بورگن‌اشتوک با قطر پیوند مستقیم دارد. Bürgenstock Resort Lake Lucerne بخشی از مجموعه هتل‌های لوکس سوئیس است که مالک آن شرکت/گروه هتل‌داری  Katara Hospitality مستقر در قطر است.
رستوران «Parisa – Persian Cuisine» در بورگن‌اشتوک نیز نخستین‌بار در سال ۲۰۱۲ در دوحه افتتاح شد و بعداً شعبه‌هایی در سوئیس، مراکش و نقاط دیگر پیدا کرد.
در ژوئن ۲۰۲۴ نیز بورگن‌اشتوک میزبان نشست صلح اوکراین با حضور ۹۲ کشور و ۸ سازمان بین‌المللی بود. در آن نشست هیأت‌هایی از اوکراین، آمریکا، فرانسه، آلمان و کانادا شرکت کردند، اما روسیه حضور نداشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76431" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76430">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mCujwkQopvbgqSXVnEEkj6Lr_cnWxbCtD37g8SimpmsYP3aMI6e0blH4edkhJbadjfMHxJAYA-bUZFCPwj9NXfQbLEdi7pR_HWAO64RByuKmICGINvnpgBaJ7iU6w0-c91a4et5NUlUIOxi4d2Z-s-eA1GHoE5iGcKceNYxTXIRy-C2bR9p0BQ41z-oRkSXme50qdopmO_wUUHVvS5Jo-BlrXa4T8sd8f91R_h7za1j5zAoDPMr3BCSWJI5E7efRoJqMMk6N9YBaOpj2LMzBoKq4y8UJwftF5klkVaacxOH7Kb3gMzdEddbCGvlLgZ7xC9xPLrykQFNeX7hcwV-QVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختصاصی رویترز: منبع آگاه می‌گوید توافق ایران شامل یک صندوق ۳۰۰ میلیارد دلاری است که بیش از نیمی از آن تاکنون تعهد شده است.
ترجمه ماشین:
دبی، ۱۶ ژوئن، رویترز — یک منبع آگاه مستقیم از جزئیات توافق به رویترز گفت در توافق چارچوبی آمریکا و ایران، یک صندوق خصوصی ۳۰۰ میلیارد دلاری برای تحریک سرمایه‌گذاری در ایران پیش‌بینی شده و بیش از نیمی از این مبلغ نیز هم‌اکنون تعهد شده است.
این منبع که به دلیل اعلام‌نشدن رسمی این طرح، در حالی که واشنگتن و تهران آماده امضا در روز جمعه می‌شوند، به شرط ناشناس‌ماندن سخن می‌گفت، گفت هدف این صندوق آن است که برای هر دو طرف انگیزه اقتصادی ایجاد کند تا به یک توافق نهایی برسند.
مقام‌های آمریکایی و ایرانی روز یکشنبه گفتند که بر سر چارچوبی برای پایان‌دادن به جنگ خود به توافق رسیده‌اند؛ جنگی که از ۲۸ فوریه، زمانی که نیروهای آمریکا و اسرائیل به ایران حمله کردند، آغاز شد. این چارچوب همچنین شامل توقف محاصره ایران از سوی آمریکا و بازگشایی تنگه هرمز، مسیر کلیدی تأمین نفت و گاز جهان، است.
این منبع گفت صندوق جدید، یک ابزار سرمایه‌گذاری خصوصی است، نه برنامه‌ای برای بازسازی یا پرداخت غرامت، و هیچ پول یا کمک بلاعوض دولتی در آن وجود نخواهد داشت. او افزود شرکت‌هایی مستقر در آمریکا، کشورهای عربی خلیج فارس، آسیا، آمریکای جنوبی و آفریقا با تأمین مالی آن موافقت کرده‌اند.
به گفته این منبع، سرمایه‌گذاری‌های تعهدشده حوزه‌هایی از جمله انرژی، لجستیک، تولید صنعتی و حمل‌ونقل را در بر می‌گیرد.
یک منبع ارشد ایرانی به رویترز گفت تهران در ابتدا خواستار ۴۰۰ میلیارد دلار غرامت بابت خسارت‌های جنگی از آمریکا شده بود، اما واشنگتن گفته بود چنین مبلغی را پرداخت نخواهد کرد.
پس از آن، ایده این صندوق که قرار است «صندوق بازسازی و توسعه» نامیده شود، مطرح شد.
منبع ایرانی گفت سازوکار پیش‌بینی‌شده شامل مشارکت کشورهای منطقه به شیوه‌های مختلف است. این شیوه‌ها شامل تضمین وام‌ها، ایجاد خطوط اعتباری یا تأمین مالی مستقیم بازسازی مکان‌های آسیب‌دیده در جنگ، از جمله تأسیساتی مانند مجتمع فولاد مبارکه، پالایشگاه‌ها، فرودگاه‌ها و به‌طور گسترده‌تر زیرساخت‌های آسیب‌دیده از درگیری، می‌شود.
ایران، به‌عنوان یکی از بزرگ‌ترین اقتصادهای خاورمیانه، در چهار دهه گذشته تقریباً هیچ سرمایه‌گذاری مستقیم خارجی قابل توجهی جذب نکرده و به دلیل موج‌های پیاپی تحریم‌های آمریکا و تحریم‌های بین‌المللی، از بازارهای جهانی سرمایه کنار گذاشته شده است.
این کشور دومین ذخایر اثبات‌شده بزرگ گاز طبیعی جهان و چهارمین ذخایر اثبات‌شده بزرگ نفت جهان را در اختیار دارد.
ایران همچنین جمعیتی جوان و تحصیل‌کرده با بیش از ۹۲ میلیون نفر، پایه صنعتی متنوع و ظرفیت‌های بکر قابل توجهی در بخش‌هایی از پتروشیمی و معدن گرفته تا گردشگری و کشاورزی دارد.
این منبع گفت صندوق سرمایه‌گذاری کاملاً جدا از مسیر موازی مذاکرات درباره رفع تحریم‌های آمریکا و آزادسازی دارایی‌های حاکمیتی ایران است که در خارج از کشور مسدود شده‌اند. او این دو را سازوکارهای مالی متمایز با اهداف و جدول زمانی متفاوت توصیف کرد.
این صندوق تا زمانی که یک توافق نهایی و رضایت‌بخش حاصل نشود، ایجاد نخواهد شد و عملیاتی هم نخواهد شد. تفاهم‌نامه، پس از امضا، قرار است روند را طی ۶۰ روز آینده ساختاربندی کند.
این منبع گفت: «این صندوق فقط زمانی ایجاد می‌شود که توافق نهایی امضا شده باشد. در طول این ۶۰ روز، مدیران صندوق با ایرانی‌ها و سرمایه‌گذاران کار خواهند کرد تا پروژه‌ها را برنامه‌ریزی و محدوده آنها را مشخص کنند.»
وزارت خارجه ایران و وزارت خارجه پاکستان، که به میانجی‌گری در توافق مربوط به صندوق سرمایه‌گذاری کمک کرده بود، بلافاصله به درخواست‌ها برای اظهار نظر پاسخ ندادند.
یک سخنگوی کاخ سفید به مصاحبه روز دوشنبه جی‌دی ونس، معاون رئیس‌جمهور، با شبکه سی‌بی‌اس اشاره کرد که در آن گفته بود ایران در صورت پایبندی به توافق با واشنگتن، از جمله برچیدن برنامه هسته‌ای خود، حذف ذخایر مواد غنی‌شده و پذیرش یک رژیم سخت‌گیرانه بازرسی و اجرای تعهدات، می‌تواند به یک صندوق بازسازی ۳۰۰ میلیارد دلاری با حمایت کشورهای خلیج فارس دسترسی پیدا کند.
این منبع نگفت که صندوق چگونه یا توسط چه کسی اداره خواهد شد و یادآور شد که جزئیات کلیدی هنوز باید نهایی شود.
این منبع از شرکت‌هایی از کره جنوبی، ژاپن، سنگاپور، مالزی و آمریکا به‌عنوان شرکت‌هایی نام برد که تعهداتی داده‌اند، اما از ارائه فهرست کامل خودداری کرد.
تفاهم‌نامه ۶۰ روزه یک چارچوب است، نه توافق نهایی، و انتظار می‌رود مذاکره‌کنندگان آمریکایی و ایرانی در این دوره روی مسیرهای متعددی کار کنند که مسائل هسته‌ای، تحریم‌ها و امنیت منطقه‌ای را در بر می‌گیرد.
reuters
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76430" target="_blank">📅 22:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76429">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dA2orLgntQN8h5WxHFlLE6YsdwFkBkVIb08qlA3GmBw4P0eOOZsKn9iN19qTwdz6mbhAXCwJoJQT80dhjjAVqn7Ub0bHWd7O2afFxL56XAuGEVr6Mgwst8y1OQ6KcRIoNX7cYtzdy94St08OOcpsELPc3JSPL9cXgiXimiJOdmOosWp2VqUat6BIrk5siyq-EOsJ7MfVUhSGj9w2FUsBnIg4222ggLvgxi5origH-y88q9J_1-i1Eq7C0lONCBeUPizQmo6Re3q1surNQQjjBEeQ-XDlEDPcK03u3mL_DmdAOZNHUNL6awzhdwqFSRiPKVbUdE4ZObgwvDPnk5i2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی حملات روز سه‌شنبه ارتش اسرائیل به جنوب لبنان که چهار کشته به جا گذاشت، قرارگاه مرکزی خاتم‌الانبیا تهدید به پاسخ کرد. این حملات بعد از اعلام توافق ایران و آمریکا انجام شد.
قرارگاه خاتم‌الانبیا که وظیفه هماهنگی میان نیروهای مسلح جمهوری اسلامی را برعهده دارد، در بیانیه‌ای اعلام کرد که اگر اسرائیل به حملات خود در جنوب لبنان پایان ندهد، باید منتظر «پاسخ سخت» نیروهای مسلح جمهوری اسلامی باشد.
در این بیانیه ادعا شده که در پی اعلام نهایی شدن تفاهم پایان جنگ توسط دونالد ترامپ، ارتش اسرائیل «۸۴ بار» آتش‌بس در جنوب لبنان را «نقض کرده است».
لبنان ساعتی پیش اعلام کرد که حملات اسرائیل در جنوب این کشور چهار کشته بر جای گذاشته است؛ این در حالی است که اسرائیل گفت چند راکت شلیک‌شده از سوی حزب‌الله را رهگیری کرده و حملاتی را نیز انجام داده است.
خبرگزاری رسمی لبنان گزارش داد که پهپادهای اسرائیلی دو خودرو را در شهر میفدون و یک خودروی دیگر را در شهرک نزدیک شقین، هر دو در منطقه نبطیه، هدف قرار دادند که «بر اساس آمار اولیه به کشته شدن چهار نفر» و زخمی شدن تعدادی دیگر منجر شد.
ارتش اسرائیل اعلام کرد که پس از آنکه «یک خودروی مشکوک» را در منطقه‌ای که نیروهایش در آن فعالیت می‌کردند شناسایی کرد، حمله‌ای را در جنوب لبنان انجام داد، اما محل دقیق این عملیات را مشخص نکرد.
ارتش همچنین گفت که نیروهایش چندین راکت شلیک‌شده به سمت نظامیان اسرائیلی در جنوب لبنان را رهگیری کرده‌اند و در پی آن، نیروی هوایی اسرائیل سکوی پرتاب این راکت‌ها را «هدف قرار داده و منهدم کرده است.»
@
VahidHeadline
📡
@VahidOnlinene</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76429" target="_blank">📅 22:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbwvNv3YSCZ_4UdEQgLoxOTTZlq3b3PYmLX8oP5RVUdcCoj9LWNuMbGtbmqa21DjHMWsCzWip9MOJC538q1krcxbw-q7P1jE-OGOdCTzyoQdfCz9x-sZTe0kmAydKssRCEZvcFMgd06oSXn84L_Q79JUiF9K91_OjJtwu7aAmkscG8I9mkGZOof-eqQBn_Vb4qrtafh2JS6pQcZ0TXTAWOyU89SfqWQCTAsLErTXaWcMzhdys4SDRE1zQ5WeSoSntnNAtG-PGoG455rnbbXsSxYzv7bNAAcn8hK_EaFO5nnV2CCrlS4lCg-qfeN21oniojwvYySdlVr270kobf75_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طیبه نظری مکی آبادی، مادر دادخواه مریم آروین و از بازداشت‌شدگان مراسم هفتم خسرو علیکردی در مشهد، از سوی دادگاه انقلاب این شهر به پنج سال زندان محکوم شد.
بر اساس حکمی که در تاریخ ۲۳ خرداد از سوی شعبه اول دادگاه انقلاب مشهد به ریاست قاضی غلامرضا اکبری مقدم صادر و به این شهروند ابلاغ شده، او بابت اتهام «اجتماع و تبانی علیه امنیت کشور» به چهار سال حبس و به اتهام «تبلیغ علیه نظام» به یک سال حبس محکوم شده است.
طیبه نظری، مادر وکیل جوان، مریم آروین است که در جریان اعتراضات «زن، زندگی، آزادی» در سال ۱۴۰۱ در سیرجان به دلیل دفاع حقوقی از بازداشت‌شدگان دستگیر و مدتی پس از آزادی موقت، به طرز مشکوکی جان باخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/76428" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76427">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR5x3LFRAM91T4O0OWJyji73DIPF-mo8ptNUgFn7TAyinkSfr7nD08nMYZk7aWi5DhDbbt37GuLTJ4eHC-p9BtAgjw1SaVFTPZaHLxfYtfE-9ZEYE6dnSYG8dSjK1Sl1cbsKKwSqUguzQvdb2lqAFPPMlxydG8UIREiZqDKBZWYaOanmY-lvYWyzGGSWmqJ_3qza5xeBoHY93eUoGb3Wrryyag_UNFefRcE963TtxGBn_ft1koDBZdXneG2iQsoOPYVQO_Wtv1oHdOoUig3Syf-aiazxW3-iUdM3Ez3QSlAMUDJRODP2QKezZlpSq2hE8k4Mc48oZcC3sdJ_iWZGwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت جورنال و خبرگزاری رویترز روز سه‌شنبه به شکل جداگانه و به نقل از منابع آگاه گزارش دادند که یادداشت تفاهمی که ایران و آمریکا به آن دست یافته‌اند، به ایران اجازه خواهد داد «بلافاصله» فروش نفت و دیگر فرآورده‌های نفتی خود را آغاز کند.
منابع این دو رسانه گفته‌اند مفاد مربوط به لغو تحریم‌های فروش نفت ایران پس از امضای توافق در همین هفته اجرایی خواهد شد و خدماتی از جمله بانکداری، حمل‌ونقل و بیمه را که برای تسهیل این فروش‌ها لازم هستند، در بر می‌گیرد.
وال‌استریت جورنال به نقل از این افراد گزارش داد که با اجرایی شدن این یادداشت تفاهم، موانع ناشی از تحریم‌ها بر صادرات نفت ایران و خدمات پشتیبان مرتبط با آن برداشته خواهد شد تا امکان انجام این معاملات فراهم شود.
یک مقام آمریکایی نیز در گفت‌وگو با رویترز تأکید کرد که این توافق دارای شروطی مشخص است.
او که به شرط ناشناس ماندن صحبت می‌کرد، گفت: «این یک توافق مبتنی بر عملکرد است. ایران تنها در صورتی می‌تواند از مزایای این یادداشت تفاهم بهره‌مند شود که به تمامی بندهایی که با آن‌ها موافقت کرده پایبند بماند؛ از جمله نداشتن سلاح هسته‌ای، خنثی‌سازی مواد غنی‌شده خود و عدم مداخله در جریان آزاد کشتیرانی در تنگه هرمز.»
یادداشت تفاهم ایران و آمریکا که ۲۴ خرداد به صورت الکترونیکی امضا شد، قرار است روز ۲۹ خرداد در سوئیس با حضور مقام‌های ارشد دو کشور به شکل حضوری نیز امضا شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76427" target="_blank">📅 20:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kp5DOVWn6qCWQ4ummxfLw_cBiRyaotclaT15zEVExvW7UEI9XsUpmy2yCmWQ7lAy8UwQ_xPcNC7RFNgbvFvY6RXnX-EQ7gVMCO-bhYBV6J9Adn1UqEShy5nLVlU5Id7cv4Zr_2lkWXTrYQWe9VZ_VIGvXi6AJ8MbYNDRL72cj0YyCDP6EAcb22Md_wamk-8LkqBGPmnss1jDFPda5EoutzXl7k3mHc9tzgr7yeBDw6MnU6q06DpUJz0TlS9oW7ks6sta2hc9FINDZkRY3OIDzOuKX6gscDBsCkMNsE15FsFiuSf3qSX8XNjd4WvpbH-VFySFqwSnwUQ_Jc7zZeLl8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی
آن گفته ترامپ
:
لیندزی گراهام، سناتور جمهوری‌خواه آمریکا، در شبکه ایکس نوشت گسترش توافق‌های ابراهیم و ایجاد ثبات و رفاه در خاورمیانه یکی از مهم‌ترین اهداف دونالد ترامپ است و این هدف زمانی محقق می‌شود که جمهوری اسلامی تضعیف شود یا رفتار خود را تغییر دهد.
او افزود که امیدوار است مذاکرات پیش رو برای پایان دادن به برنامه هسته‌ای ایران موفق باشد.
لیندزی گراهام اضافه کرد: «جمهوری اسلامی و نیروهای نیابتی آن به‌شدت تضعیف شده‌اند و توانایی آن‌ها برای رقم زدن رخدادی مشابه هفتم اکتبر دیگر وجود ندارد.»
او ادامه داد: «اگر درگیری با جمهوری اسلامی به گسترش توافق‌های ابراهیم، همگرایی منطقه‌ای و صلح پایدار منجر شود، این نتیجه یکی از موفق‌ترین عملیات‌های نظامی در تاریخ آمریکا خواهد بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76426" target="_blank">📅 18:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromﻣﺎﻧﺎ ﻧﻴﺴﺘﺎﻧﻲ Mana Neyestani</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/myOl8m9o4Lmsk8GYytEYG3ojLbcSRRJElMMBoZpLJJWLywOKI59AkdLdDwGs-64IU_OyMRaVuWY4YfNiuffGCsRqpLNm_5s4d8o2cSx5iHYcrlnM1tFCnuM5NiEZVaDUCgl5HngyfrKg2yEmdA9hQ205Pf4PXmmviwrEyF9j5alHRrs5ZFVq3nzUF-TClGbqv8SIfTVtnmoCI8PaP_WVMX7a3aCR1wzpYsBoNmKsKDiu1zaixE1DHqw0tznEFpYeV98xTdicupULB3vh-s-kKzn034rRYV5dt-6wFkMgtkxX1adHlkA8jGFyxlhdPMkDzlZdZoOZ5nnpm-cPB4aMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gs7njCBu_NOsQfck5XRm0sNi5HjKsKjFkAPrlHaaAXLmXFNnHECCpME_FK_FKMBUj-HMlco1-6pIVNOjTA8Lu0nCUFTh23lzoiwFGX3e_OiS-wwicNe3w5j5LkTxIL5-zpNSKcj3aj63HsGw0y0gW_eFu5dp-DDUZf3bVq_CCKtFODTst2_hrRtEaaLgk_TqpWiLXSGm1xdVikPuke7mwIxOXOaYxPBczw4Tt0A4iqkHYPaWmYkuYc5PsdKppXW-o3TDZe-CZkjGm-uhOTLQ7XfKunTOgJyGHM2uyBL0TH6fdekycqZTrx4XMWm2PQo01a1q5sX5Cb9vI9_tw9_OMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پهلوان سازش ناپذیر
@mananey
مانا نیستانی</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76424" target="_blank">📅 17:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tpESynp098MQbylzyNG7ePTIJMuArra_hAeOBRJVFJSt9Nah7ztxOiiVnHcJIUT8k5SpG-GaJvlnl97ItxK-xtwcVUF268Tw28FFAFafUp2VEyYHCqj4EzcBuxpEDBHBIMrgI7ByUM4ddiVwXLkJIvK_y9JJ0x0D9STMlXq5x_yaBIOhh_RgqdYqHTqq3-VutoOvxa2iX2bOQCe01UuMsZcUZFNO-jd_wSsfxa_B5aGqKvA6mhrDjtgoQLwUuxvdhOahfmtPb-2XwzHC31kBAHLqnJYqKzxEtSKFj5JLJTnUG5jOLnPr2NEuBuV6a00HaeX9k4q2GILjrTLMlB7iCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tnPq8zaOCA55LsdwdsU9ZfNFZYmIjsat4PB3ATi0SpkR6aT5rWBQ1-pKGWsg6J5iMT2gQb4tTkLFbwtgautRfE_LWDPbrxqmrZvXb3c67DjIrCFCifuIGFPnTu8_rcSoftqLox4UyXyhMspsPngn_ATKbyFQzj-cczUMsvESiWIVHv7Ge8-X9wxFH7FdaWcBawlpVK-WHEbqYwpLURKjVPJrQF0NtONyUTsVqCJhvEdhf10tF4wQ2Ok5d0BrE3yaaI3PFUX_0MRJC0_HLTpgT3nm-8MNb76sZr8ZZX9z3OYOzYlRjvgmYpsjpk-dpslp5bmnbnw3OyzJK7xDZkCb_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TX8ZIM7QKG8J4RZy0ROV5p2aJobUFSlFX6kdeCzTF-LeZ1AL_dp7WjlN_EjEJRoEGBm8XFHicBkn9EFGoGFyrHqAFosJ9BBNQCrMW_DJ5Ipa9xJ_NxHn8Ce0aGFE4XjLRsa1yig1uRi8cZUbLzIAupZ5mt1OF76kc54kCpWu6MeNqCXW4-qSxauD0oqZJz0G30Lw53fnZpescA2t265gu1nntxRiC_3EBaCZsRrNpYli9AscuV5KuSNXQgNkcLUv5KJvFucmACL4mRCYH8hOCgW0Th-ARy-dLoPFBM4PeWbsLkcbtvs6rjF1mFYtGLhXlYC9dkQaw53mCtNL3qjoig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faa23faa31.mp4?token=EFKg0J3uyfwiz-NIYZP_4i2kkba4oHSRNrKVAeK39ieIWGKngW8bpxVhK4CURP2nwrbxidA8gkXibruJXvGPDDifdQ4LSjBN8srlTUjjus5Wnzm5ajl8kqg1CVFSKxx2RceztRyISZQ5uShUKPqgcg6aHD6h7scP5RWCkkem3fs6TEpNC1bR8RUo5OfEZK45UThxp7ikPDigR7288CskLbNGoSuJ-8pbVMW8xi92kQJCoLEwQ6i1HUsqREF6tUs4Qqd6KsaI2eN9JMRlV2Bk8VyL8VOIwNUqISpKtYYortDcPJfjmGfxfmWLKsxW9yuZWNlJZpi4PiKbdNiOuIn_3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faa23faa31.mp4?token=EFKg0J3uyfwiz-NIYZP_4i2kkba4oHSRNrKVAeK39ieIWGKngW8bpxVhK4CURP2nwrbxidA8gkXibruJXvGPDDifdQ4LSjBN8srlTUjjus5Wnzm5ajl8kqg1CVFSKxx2RceztRyISZQ5uShUKPqgcg6aHD6h7scP5RWCkkem3fs6TEpNC1bR8RUo5OfEZK45UThxp7ikPDigR7288CskLbNGoSuJ-8pbVMW8xi92kQJCoLEwQ6i1HUsqREF6tUs4Qqd6KsaI2eN9JMRlV2Bk8VyL8VOIwNUqISpKtYYortDcPJfjmGfxfmWLKsxW9yuZWNlJZpi4PiKbdNiOuIn_3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ که پیش‌تر در پیام‌هایی خطاب به ایرانیان از «کمک در راه است» سخن گفته بود، اکنون در گفت‌وگو با مقام‌های قطر، کشته‌شدن معترضان را عمدتا به «گروه‌های قبلی» در جمهوری اسلامی نسبت می‌دهد و میان بخش‌های مختلف رژیم مرزبندی تازه‌ای می‌سازد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76416" target="_blank">📅 17:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76415">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0db862b726.mp4?token=fbhkaPu4CpXhx0sqSEqjvxKXzjLBJm2kuzlfbdKFzbxnmllA3HPB7qYTljFFw6-msfiz6bJO27PO631Cuqm2ZoREOjstnomZwk6XnuFNay8n9kDhxsCDuRCJf-nxH46YnuoBEsKHfvG2scnxslnBQwV3fOQoesM66iA4JxMyNzID9ndXYOJqXLe4w_t_E2_M2prL2q_BFOeDmAxfYlKq-Q9eFoPW1-ss30YsrFZyD2jhi33kbQWDmQddZ3AZBxjjMERJNDeAZw0rLlCTE59WGqN5cvVoutzxp2muo6BeAg9mLfgOU87e4-lyC35zsPb01-5TAdOm8JS9ALpFqapRfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0db862b726.mp4?token=fbhkaPu4CpXhx0sqSEqjvxKXzjLBJm2kuzlfbdKFzbxnmllA3HPB7qYTljFFw6-msfiz6bJO27PO631Cuqm2ZoREOjstnomZwk6XnuFNay8n9kDhxsCDuRCJf-nxH46YnuoBEsKHfvG2scnxslnBQwV3fOQoesM66iA4JxMyNzID9ndXYOJqXLe4w_t_E2_M2prL2q_BFOeDmAxfYlKq-Q9eFoPW1-ss30YsrFZyD2jhi33kbQWDmQddZ3AZBxjjMERJNDeAZw0rLlCTE59WGqN5cvVoutzxp2muo6BeAg9mLfgOU87e4-lyC35zsPb01-5TAdOm8JS9ALpFqapRfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در حاشیه نشست سران گروه هفت (G7) در اویان فرانسه و در دیدار با امیر قطر، از رویکرد نظامی بنیامین نتانیاهو در قبال لبنان انتقاد کرد.
ترامپ با اشاره به حمله هوایی اسرائیل به بیروت، درست دو ساعت پیش از امضای توافق آتش‌بس با جمهوری اسلامی ایران، آن را «کور و بی‌هدف» خواند و گفت: «به آن‌ها فهماندم که اصلا از این کار راضی نیستم. برای کشتن یک نفر لازم نیست یک آپارتمان را با خاک یکسان کنید؛ آدم‌های زیادی آنجا هستند که همه‌شان حزب‌الله نیستند.»
رئیس‌جمهوری آمریکا با بیان اینکه اسرائیل زمان زیادی است که با حزب‌الله می‌جنگد و افراد زیادی کشته می‌شوند، پیشنهاد داد که کنترل این گروه به سوریه واگذار شود.
ترامپ با تمجید از عملکرد احمد الشرع، رئیس‌جمهوری سوریه در ساماندهی سریع این کشور گفت: «او با مشارکت من و اردوغان روی کار آمد. او از حزب‌الله خوشش نمی‌آید و این کار را بهتر انجام می‌دهد؛ اگر اسرائیل نمی‌تواند بدون کشتن دیگران کار را تمام کند، سوریه این کار را خواهد کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76415" target="_blank">📅 16:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRbVRgcljRgDwN2NqH-oIH9ACIShGYpK9BW8sO5MI5qQ1jjqM7RL_rYpkAAQi6F5ZqZ3gboEHjWlOqsQvh1AlYYkdLv5KQEEOEUsffAizu2cW2CGB08l1hv8n871Xrc1Sx-XSmcisCyKUSs_0cdFqMpgimFMNEWBK2n4cTYJn0B58l6cqWWB_pqJYp_ddfeuGT8Jv0XrIIRl0EeQKLyhf7qf5mFuCCMkR0wLifJ5866bVOYtOoHtBPrI997iQPJmbmqIZR4__ipE13guBmpVqxCKrgc9PrqvY2bpRVm67ho2tlpCuoDv83bXD9ErydZbI9U1YzWP6rnT4xBEA8VkMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در پاسخ به پرسشی درباره متحدان او که نسبت به چارچوب تفاهم با جمهوری اسلامی تردید دارند، از جمله لیندزی گراهام، سناتور جمهوری‌خواه، با لحنی طنزآمیز گفت: «لیندزی تردید دارد؟ باید با او صحبت کنم؛ دچار دردسر بزرگی می‌شود.»
ترامپ سپس تلاش کرد نگرانی‌ها در میان هم‌حزبی‌های خود را کم‌اهمیت جلوه دهد و گفت گراهام «آدم خوبی» است و مشکلی با این توافق ندارد.
او افزود: «این توافق یک موضوع مهم را به‌خوبی پوشش می‌دهد. ما بابت آن هیچ پولی پرداخت نمی‌کنیم.»
رییس‌جمهوری آمریکا ادامه داد: «بازارها اکنون نسبت به زمانی که کار را آغاز کردیم در سطح بالاتری قرار دارند.»
ترامپ گفت: «اختلاف فقط بر سر یک موضوع است؛ این‌که ایران هرگز سلاح هسته‌ای نخواهد داشت؛ هرگز، هرگز و هرگز.» او افزود: «بقیه مسائل اهمیتی ندارند.»
@
VahidOOnLine
آپدیت:
توییت گراهام
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/76414" target="_blank">📅 16:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rTJTf8a1fyJ0sKYjChPpUJH9E9Nrc60jXEHD5EheaQlK90f13dqQ3kHz1DrPHxIsmRzdQsIbJ_0UGk7cdsD4qy-B1PXVe9fozCRRnHwTLnoeS2_JIPksHnoivpHM3cjayxARmC7hTO49bvsX0qjumFN7_BB7C0oaAwfDf0y-m6xwgMF0VRhZVtiuOJ2cxe4bVHKHJS9J1UxAlgQny9cOvpYxMuvLdlZ4Fx_fvKhR0o5-cZIMtyROA5Z5Zj9AqvVN82E1WU7eqDy_y9G4pW-xPwBPY3tI3oL2orj57LqeQqyJcxZTRZP4BdYkyUiNQuq1uoR_i8dJpszdmGRhbGrOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OHBZhdwCdcq42hcy2be1D3zln3tT5QPytIWK5NDE_tgT06x1nr9yFaxroUGBPfuD7zoq_QxQwAsbCofIEuu0COvaID1pg8e0-qyxBHLSuK0pJHS2tKohFSsWs1H7jYiZUsUA3VAcqErGDLXjmQxLNl1XV-CphOTne0qcSH-alAgxSTyl5On-3Dei1exBdM9OwJzed-3aXQPwYcnR4mJ8F1ajfBpN3QekEEjJFTPpfro2d9RZlx-Qm-aQTiaQqAXs4rSGMeDajFiQgfG0CwW_sgNKoxQYriAcVT9FWi2erxTj-ah-c0dCw9jgi3mE7wifHdryasZbOGV6Q3uxLL3VEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی درباره دو پست قبلی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/76412" target="_blank">📅 16:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76411">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDE9VujZ0OPIwZKL55bcszysYRQhMZmBwxMKcfz7LPj5jCCH07Y92Z-WXLyPMYgsQMGwbZYW_0FGRZiaLpahQxeFFL2k47Izm22gezOWGIfSzoupYXbSb5Q7XZ_cnAUvoVZvGvxLbEYSUb5XCKC1vXPV_IoK9wBuaIhd7OYUK-RiQP-rNTd6TGHLTJLZPlYdFKxfj1IECaqa7Zh0oN2bLtcIIycFDETtV1EFHIfR5-_PhZ6egHwQb-ux5ZrQa9Iyz-R7jtbnnY4U4BP1whTELvdelmDOsO9exSLhALfrrBpiXj3YE9HuNP04oSGWwRqhee2D8Dm1gqw8YtnNczqYcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور ایالات متحده، روز سه‌شنبه اعلام کرد توافق صلح با ایران را برای «بررسی» به کنگره آمریکا می‌فرستد.
او در جریان دیدار با محمد بن زاید آل نهیان، رئیس امارات متحده عربی، در حاشیه نشست گروه ۷ در فرانسه به خبرنگاران گفت: «هرگز به فرستادن آن فکر نکرده بودم، حتی یک بار هم به آن فکر نکرده بودم، اما این کار را خواهم کرد. آن را به کنگره می‌فرستم. از این ایده خوشم می‌آید.»
برخی قانون‌گذاران جمهوری‌خواه پیش‌تر خواستار بررسی متن این توافق شده بودند.
آقای ترامپ همچنین وعده داد که متن توافق با ایران را «ظرف یکی دو روز آینده» به‌صورت عمومی منتشر خواهد کرد و حتی این احتمال را مطرح کرد که کل سند را در برابر دوربین‌ها قرائت کند.
او گفت که منتظر فراهم شدن یک «فضای رسمی» برای انتشار عمومی این متن است.
رئیس‌جمهور آمریکا اعلام کرد: «دوست دارم ابتدا یک چارچوب رسمی برای این کار فراهم شود، اما هیچ مشکلی با انتشار آن ندارم؛ این یک سند عالی است.»
او در ادامه افزود: «محتوای آن این است: ایران هرگز سلاح هسته‌ای نخواهد داشت.»
ترامپ درباره مرحله بعدی مذاکرات با ایران که برای آن مهلتی ۶۰ روزه تعیین شده است، گفت: «فکر می‌کنم این روند خیلی سریع پیش خواهد رفت.»
او افزود: «ایران می‌خواهد این موضوع را نهایی کند. آن‌ها باید به فعالیت‌های عادی خود بازگردند و روابط اکنون عادی‌سازی شده است؛ بنابراین فکر می‌کنم این روند خیلی سریع پیش خواهد رفت.»
ترامپ در ادامه گفت: «ممکن است سریع‌تر پیش برود، ممکن است هم زمان بیشتری طول بکشد، اما می‌تواند خیلی سریع انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76411" target="_blank">📅 16:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Fnli9gzG0DO1AdHGGnlyj1eyZF0yMGSF1lOb2h-HgoT4_MOO_-zHKS9kqZ3m1dm3g-XHcHsgIlD03lFxk_7FfTz2EIq-LNs_mDHNgWlD1GHjfNoqjVoNZYhSv3lFXY9IBSh_g6KTQ_JBfG6_IcYcB0oC24u1IQ-NhugAVci0X0P89oKBZpM9dKujDxdzILfVuX6TpMCx-n21JpwyQE-E2HiwTkBnu9SPNabsQ_L9QCzGrGXZNSQtcGhX4WvyvkkhP85n-OoSExQq65m-cxFQsb87rI_qlFOUeUtqf-b1OHK8-P_lfC4mDM7iIMgg23L1Ry2ZSM-wOoUGp-SUlvyclA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد که روز سه‌شنبه ۲۶ خرداد دو نفر دیگر از معترضان دی‌ماه پارسال در شاهرود اعدام شدند.
خبرگزاری میزان، اسامی افراد اعدام‌شده را جواد زمانی و ابوالفضل ساعدی اعلام و گفته است که آن‌ها به اتهام «محاربه» و «افساد فی‌الارض» اعدام شدند.
این نخستین مورد از اعدام معترضان در ایران پس از اعلام توافق تهران و واشینگتن برای پایان دادن به جنگ ۴۰ روزه است.
در بیانیه رسمی قوه قضائیه، از قول محمدصادق اکبری رئیس دادگستری استان سمنان ادعا شده است که افراد اعدام‌شده «اقدام به تخریب و آتش‌زدن اموال عمومی و خصوصی، حمل و استفاده از سلاح سرد و گرم و اخلال در نظم و امنیت عمومی، اجتماع و تبانی علیه امنیت کشور و سایر اقدامات مجرمانه» در شهر شاهرود کردند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76410" target="_blank">📅 16:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76408">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RocklBllk5ccfR4Zf1-L6zfVHiyUkmmqghZUKzUNLCoXgOAbEoGRfBHD3Ckn0iNnK9yvR4izvn2qXSj1MjtikViEKo9tNAe27TVjiXcTbcQi7mBmMu_aPIdCEWJVDUToAZ_vBlZ4Zczz6gLQ8fUxhY7NdCFa9i-GY6Z2Q-IQtdqsGOZyGnqSpNYRLcOOxtpVVdUVPHCdajK7VOeOV5uyGYrQkzfwiSUYNDVd2vaCXboP3LZXLTK0uOLCAB4H4ZEqeQTTr5NxU4pWGw_LSDYYVj8b1pC3-QppU9GlZCjhdFWYgZra5FmJJIBZbsSSn4CJW_jfhANADuI0ALZiiFcD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XI2aPyRlnjctAmGSEsNnGsOqoPCZRtZECWhufAdLRSGp81ONA2Pn2xGS7l1dYeGeMqcvpiS-GQpCHQz6yn64-qe7Jpgnj2WFpHELJkqMk40CvDwX9GERU_XXlI_sATvvAVUgchK_1T6eH6f7FG52iczy_Vyo3I6WqBuGJup3l_0f6DfS_7mTtXoLAYlTLTwJmlNsPq4aoG9f36qMiSzTCe9qo2SfLTy9GbRlQDGlEBBOxSHpfEJvHFCUvjudVdQNpY6SbatqH9t8gOe9F-OhF0-dvyNS2QVn1WXRNdTLzEFOjRg98GdcxbVEdlC_mE0dIPsD3RAKYacQJPN_T0duuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مسابقه نخست تیم ایران در جام جهانی ۲۰۲۶ مقابل تیم نیوزیلند با نتیجه ۲-۲ پایان یافت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76408" target="_blank">📅 06:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76407">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6aa89bbb6.mp4?token=UkUEOuyF2Mi9zWKlrz1MX6Agp4AV7lKmreu11CmOpYRY43IyCSNBm6CCUi6jzVN46Yvx6Bkq0DVd6qDlYJru5fVkGFIdd7jAXOs2jwBKKZPUbk3qzMN1iIW9keSwEGhRN8CiAOUxETh4Ro8kc2lAdcKACpWQbc_6SyFqr8616m41fQXu-tO2jaxKaZCz0LL85bEYU1L0Ql3HrEcVKiDHEODc1ksNCvcn93glXamzhXyOud3poBvtHDkuUJL1joAQe9mXoUhGHsj0JWQRMWTB3yJnUlmv4pmUiVuUeaFtBcV3yE8l4UL0eYax086C612yp-0NGSJ7QtZKi7sWSQQ5lA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6aa89bbb6.mp4?token=UkUEOuyF2Mi9zWKlrz1MX6Agp4AV7lKmreu11CmOpYRY43IyCSNBm6CCUi6jzVN46Yvx6Bkq0DVd6qDlYJru5fVkGFIdd7jAXOs2jwBKKZPUbk3qzMN1iIW9keSwEGhRN8CiAOUxETh4Ro8kc2lAdcKACpWQbc_6SyFqr8616m41fQXu-tO2jaxKaZCz0LL85bEYU1L0Ql3HrEcVKiDHEODc1ksNCvcn93glXamzhXyOud3poBvtHDkuUJL1joAQe9mXoUhGHsj0JWQRMWTB3yJnUlmv4pmUiVuUeaFtBcV3yE8l4UL0eYax086C612yp-0NGSJ7QtZKi7sWSQQ5lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس معاون رئیس‌جمهور آمریکا ویدیویی منتشر کرده:
رئیس جمهور از روز اول صریحاً گفته است: ایران هرگز سلاح هسته‌ای نخواهد داشت.
بار دیگر، تلاش‌های رئیس جمهور ترامپ برای برقراری صلح، علیرغم تلاش‌های بی‌شمار افرادی که از آمریکا و رئیس جمهور ترامپ متنفرند، برای مردم آمریکا نتیجه داده است.
JDVance
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/76407" target="_blank">📅 03:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hpJVRz-Xe9kcdchQkRd0YJoCALn0lewSq5q4o2DyvRG1ckFydWLQ7O4M9m01V0_ccLVwse2BoC-cscwrv5E2gxyfSX2Behrh4ykoa8L7as12PE6gWv-jcBdWeBlsrsgUReBmy-SVdO34lJ2JsrYaZhRjKQ-jlkKgtuW432-6GP6h-SGznnQy4bpLtRPfJNlOtymhjTc6Lw6OzjrcGcSWAD19SlZLi2XQ2sqEwcazud_bbNX93jlAOHna5kFKGrZpAFR0dSplth6HYNS7VbW-H_an9Ckk0Mjk0zorLBZJavFUImK9efrov3w2eVQDTrb2vVVublYIk5YbZpU0MJNEVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه و توضیح ماشین:
ایران موافقت کرده است که هرگز سلاح هسته‌ای نداشته باشد! همچنین، داستانی که می‌گوید آمریکا ۳۰۰ میلیون دلار به ایران پرداخت می‌کند، خبر جعلی است که دموکرات‌های احمق منتشر کرده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
(عبارت «Dumocrats» ترکیبی تحقیرآمیز از
Dumb
و
Democrats
است؛ یعنی چیزی مثل «دموکرات‌های احمق»)
realDonaldTrump
البته حرف از سیصد «میلیارد» دلار بود نه میلیون. ترامپ هم پرداخت از سوی آمریکا رو تکذیب کرده ولی
ونس هم نگفته بود که آمریکا قراره بپردازه
.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/76406" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76405">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocnN716vhPQZ1HxYDNK06W-pwyCsC7hXc53YUXKFFnX7WlCS2PWFwEbo2_J8CpyoEin2NlouAKL92o2RRNZYMamyqAWuK-kxIpsKHVxWeQkfn481V-W1YdyGRwJYRbOWfksU0lvEaaBG7MqyuEeoQjdxz_3KGc0eMXUnjLDwME-6STcSsH69ruyllLZ5ZWtqRQc8U9QWjHo-jI9AmxDoqK4Olsof2cfKoFmt0_QfFdsLAltdnKcPREPtOUK3zsnJyvjuSqiOVwlNb0RYJfr1FfTMqm7C8lnFfshdaFex6fvqauk7NX4GpBlPaWCZeZmikZIhZPyJLYksnYK-8Twenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه منبع مطلع که با خبرنگار اکسیوس گفتگو کرده‌اند، می‌گویند: جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، به دونالد ترامپ و دیگر مقام‌های ارشد دولت گفته است اطلاعاتی که چند نهاد اطلاعاتی آمریکا جمع‌آوری کرده‌اند، درباره آمادگی ایران برای ارایه امتیازهایی که واشینگتن در یک توافق نهایی هسته‌ای میان دو کشور خواستار آن است، تردید‌های جدی ایجاد کرده است.
براساس این گزارش، رتکلیف تنها فردی نیست که در تیم ترامپ دچار تردید است. مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر جنگ، نیز در نشست‌های داخلی نگرانی‌ها و پرسش‌هایی درباره این توافق مطرح کرده‌اند.
در مقابل، جی‌دی ونس، معاون رئیس‌جمهوری، و استیو ویتکاف و جرد کوشنر، نمایندگان آمریکا، از توافق حمایت کرده‌اند.
به گفته دو منبع، ترامپ و تیمش اطلاعاتی را بررسی کردند که چند نهاد اطلاعاتی آمریکا جمع‌آوری کرده بودند و نشان می‌داد شیوه‌ای که مقام‌های جمهوری اسلامی در گفت‌وگوهای داخلی خود درباره توافق صحبت می‌کنند، با آنچه به میانجی‌ها و آمریکا گفته‌اند، همخوانی ندارد.
به گفته دو منبع، رتکلیف و روبیو اعلام کردند که بر اساس همین اطلاعات، نسبت به این‌که حکومت ایران با اقدام‌های هسته‌ای مورد نظر آمریکا موافقت کند، تردید دارند.
یکی از منابع مطلع گفت: «اطلاعات موجود نشان می‌دهد نیت‌های ایران با تعهداتی که در چارچوب توافق پذیرفته، همخوانی ندارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76405" target="_blank">📅 02:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76403">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/boaO8dnvK8J1pd6wCoME8Dz39JoOtS16XzJLSjuCV7s92PrDv2I2vIfAzDrqxnltCjvqzEwgKblGpQXuURfd5MHOkSKtjaH_dyxZuUN1V2DOVP1Tmf0psZUUmUWgK1YvkNa49msYPldW_24Agz1EGa3WHpldy8WgcOyO0xsJFE3FcLyqJwM5UgsH7XTLORVqmzyBHmqA7kauPhTcai6t8f8HJC7PDl4kKvh1-p7XbzmLWCxLYUp-UIFIiuQVIiDWMIAvlv2YZhAXTouW4DiR9S1rqCDlPmR8sr-4PBzJJ-xwiUAvtSN6ULhQ47IvTPdrADDJEU6Ihbd-J7iwWC4GHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lJM_97fxLlWAM0wQRqsODceYs8t-m1Q9XFlIUFqs5U3ZI6aX08JTtRhsCrda28JGIwncRvci8acxDLGP9_QrWLEIK-eqnV1DHSoOlnXdnPzXGNa2W4EiePB7k_YuRjXQSUDb0uxTv-Ozaa-59zqXuyqAk85r3-P1X1RhTQpBFaEnq-GMp7gXZYckc0WW3wIofnzP6CuzRe7MubTNyZCHWu32gXBy0OSIkjD3MO7ujm8XGH03PPJrjIh-x8MWs96bWn2mnr0GJ0A6AvQUmGll2sQhKbTHkHsQ_cKL7VKsNHeWy9_mFy-5WsBLhNzJKy_OGwLuW_PmC0EriGVKURg2lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهوری ایالات متحده، روز دوشنبه در گفتگو با «سی‌ان‌ان» اعلام کرد که یادداشت تفاهم میان آمریکا و ایران سندی بسیار کلی و در حدود «یک صفحه و نیم» است.
ونس با اشاره به اینکه این متن تنها یک چارچوب کلان را تعیین می‌کند، تاکید کرد که جزئیات مربوط به موضوعات مختلف باید در طول مرحله مذاکرات فنی آینده مشخص و حل‌وفصل شوند.
به گفته او، این تفاهم‌نامه ساختاری را ایجاد می‌کند که بر اساس آن، ایرانی‌ها در صورت پایبندی به تعهدات خود، از مزایای این توافق بهره‌مند خواهند شد.
معاون رئیس‌جمهوری آمریکا در بخش دیگری از این مصاحبه گفت که در همان «بند اول» این سند، انتظار واشنگتن مبنی بر تعهد ایران به «صلح و ثبات منطقه‌ای» به صراحت مطرح شده است.
او تصریح کرد که بر اساس این بند، همان‌طور که ایالات متحده به صلح متعهد است، تهران نیز متعهد می‌شود که تامین مالی سازمان‌های تروریستی خشن و دامن زدن به بی‌ثباتی در منطقه را به طور کامل متوقف کند.
@
VahidOOnLine
جی‌دی ونس، معاون رئیس‌جمهوری ایالات متحده، در گفتگو با «سی‌ان‌ان» ضمن تکذیب گزارش‌های مربوط به آزادسازی زودهنگام اموال ایران گفت: «تا این لحظه حتی یک دلار از دارایی‌های مسدود شده ایران آزاد نشده و هیچ‌گونه کاهش تحریمی از سوی ایالات متحده یا شرکای ما در خلیج‌فارس صورت نگرفته است.»
ونس با اشاره به گزارش‌های نادرست در این زمینه افزود: «تندروها و برخی عناصر در داخل ساختار سیاسی ایران، برای متقاعد کردن افکار عمومی خود، دستاوردهای تهران از این توافق را بزرگ‌نمایی می‌کنند، بدون اینکه به تعهداتی که ایران برای کسب این امتیازات باید به آن‌ها تن بدهد، اشاره‌ای کنند.»
معاون رئیس‌جمهوری آمریکا با تاکید بر اینکه این توافق در صورت اجرا شامل یک بسته کاهش تحریمی بسیار بزرگ برای مردم ایران خواهد بود، تصریح کرد: «این تفاهم‌نامه نحوه تعامل ایران با جهان و منطقه را به طور اساسی تغییر می‌دهد، اما تهران تنها زمانی از این مزایا بهره‌مند خواهد شد که به تمامی تعهدات خود عمل کند.»
او در پایان به مخاطبان توصیه کرد که نسبت به بیانیه‌های تبلیغاتی و پروپاگاندای حکومت ایران بدبین باشند و تاکید کرد که بهره‌مندی از این فرصت بزرگ، کاملا به پایبندی عملی ایران به وعده‌هایش بستگی دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76403" target="_blank">📅 01:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76402">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U2kxI3bzAEq98F5k_hz7mQDAil_FI_5ROcbg9vCBhkJcj3L1n2YM99DpFMUt4g0pu8CkBloCADa0t2DUZkPb4y4c56DzxNZ6UIkvb9XeuFpws4-luQ0GZYPF_YltfYUqlS2NivjFF0hEL6Xn4lDJMeYsSLgePTxwYRHJl9-rH5U09DPy5dqKJEKEHM6UjzfC_4S6pCXpf35tEVF6_e-4gddrPDJJXbqKGKGyjtNKtC_bz6f2PfBRgP4YSZyVcJdUeMWQRS4_rkfaal_dGeWUP51yHGP5Sf5bK1TfedeLgYe8EhAWkwBlNIWKMEJCL7VqBT6QFoV04u1VKgfKey_Reg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر:  منابع محلی از شنیده شدن صدای انفجارهایی در مناطق جنوبی جزیره قشم و تنگه هرمز خبر می‌دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/76402" target="_blank">📅 00:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76400">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/teqPJ58ygLmrwISN3ogz6BAWfD6j2AOcg9-A1_rxnEZJKiPmTVrc-0g37y15TUs5f-dIMNq6YHdSg4hkg3b2e6oy07NKaosvTPTokKbDmR4a4-ZdmxvJJdoFLgGfik6vnT0lF80sVYkucFqAUT25FTdLz_YBAtaiBxBj6l7x3UB5S26_gCJHTAwHpNmCuzjF6keH9y3IyDHGqwlBqk_WqranS7-du1asSbp1sDXLLYvoa9j21Gnx2WymijJ0XcixXmYaU_tO8I76kai37HN5TEQyPUrLeUnzVoTSBnAOLjwa_TtQSRAMUIhv7cWJUS8QdMR7hFAavu1Elwh5GSbc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DQo0TXzb4VbvaVq2uv3TuXcfnI7AdutNhDXDdmJdrAHMrb8I5130ZY-JdctChGD52-rIm_2dmeInOOySBpu6JHSc7Jtl0Av5rF52v-ELeCUPN68NZjkeJ14JE_IuncNiTHSQSPjvoxrymBtZdCFDPrN5fsJzo6tIOjluaylF6AVQFTTqhR_CDKCej0we4Zc2qEV-Q8bd_q-Y1wAylZ80V7aFyHre6CnVShURTXVWJVTbtDn3jVokobOvZdaFhgbX_Yt5hvCKFjRrVC5F1MeNP_lS_IOWIP9mY7HywRJVC-uqrX8PpVgsYR4h1NkCKHjHfZK3VsO0d_NN77SYXsz_qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت: رفع محاصره دریایی عملیاتی شد و ۳ نفتکش و ۲ کشتی حامل کالای اساسی جمهوری اسلامی از محاصره دریایی عبور کردند.
پیش‌تر ‌‌ارتش آمریکا در یک یادداشت هشدار اعلام کرد که محاصره بنادر ایران تا زمان تکمیل یک توافق آتش‌بس با این کشور که برای ۱۹ ژوئن (۲۹ خرداد) برنامه‌ریزی شده است، همچنان برقرار است.
@
VahidOOnLine
بر اساس گزارش فارس، دیگر خبرگزاری وابسته به سپاه، یک نفتکش غول‌پیکر ایرانی (VLCC) به همراه یک کشتی حامل نهاده‌های دامی با گذر از منطقه محاصره در آب‌های آزاد به سمت بنادر ایران حرکت کرده‌اند؛ هم‌زمان یک نفتکش دیگر نیز با عبور از دریای عمان و خط محاصره، مسیر خود را به سمت مقصد صادراتی پیش گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/76400" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76399">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌های دریافتی نیم‌ساعت پیش:
صدای انفجار سیریک ولی با فاصله تقریبا دور
سلام وحید
۲۳:۵۷ دوشنبه ۲۵ خرداد قشم
خودم یه انفجار و موج رو حس کردم، اما بچه‌ها میگفتن دوتا بوده و قبلش هم حس شده، جایی که من هستم نزدیک تنگه است، شاید از روی دریا بوده
۰۰:۰۴ سه‌شنبه ۲۶ خرداد
مجدد دوبار احساس شد
سلام وحید خوبی
ساعت ۱۲ و ۵ دقیقه سمت سیریک صدای انفجار از سمت دریا اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/76399" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76396">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hLc4rDFvHbFMccHl7dXOVwF--ftDonDrRP_mJlCP3ULP5c3M-0Tkm20yMJW3O4SJhERWymE7Kl9NRT6JhKWces642cb21nHDRJulhvAHwJMl4BG1io9MO9RMtvOTb4Ixjhx-hUQGkmTDxDzI8YRtbk5Ci8x2Y6ybO90U6cUkZK36Fm_KlOK9YP8xBt5kcHuGNWCRGdPh42_KFNrfVds4gxAsOHDDCFmgcWhSNfnKivuoJ6-__QD0c2qvLdQW6I-B-j3UQy0Skg3s7nS_JdopFwkBAiRGPI1ZoixCBgYaim7ICe3Lo7mnBIiqwzsWRQTAEyoL9Iu0nnuKifs-4CORiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/759110416d.mp4?token=UMQip_pCHso0hP1hGF6R45t_N5OIUWkNccd6YFZml7ykf_tfHtygmhaOCOfK6CW0fKStwAKRPEDbjDlAn1yq-KMBr91SSa9EOAT4JhsPCpG0fhildVDuXJhnP5q8PQ8D_iwo7amEA6HZNnX64jU5GHcGFp2ub2vqpZE0Iu6m5MoFSgN-A8QSvv6vNEsAe_O0Ry8XGoYOZAzVKdTL7FSVZ5SQjVtKMT12tDkH1SwzDXqmTBzgaAsWHpNVicB8LWuE33Uc3BRgODDW2jP_a_QxyjzgWUKP2G3bQBgjFxYUYq8W_wtgy6gx08H1GGAYQpcp8_YRm0pztwafwM31Lt_lfg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/759110416d.mp4?token=UMQip_pCHso0hP1hGF6R45t_N5OIUWkNccd6YFZml7ykf_tfHtygmhaOCOfK6CW0fKStwAKRPEDbjDlAn1yq-KMBr91SSa9EOAT4JhsPCpG0fhildVDuXJhnP5q8PQ8D_iwo7amEA6HZNnX64jU5GHcGFp2ub2vqpZE0Iu6m5MoFSgN-A8QSvv6vNEsAe_O0Ry8XGoYOZAzVKdTL7FSVZ5SQjVtKMT12tDkH1SwzDXqmTBzgaAsWHpNVicB8LWuE33Uc3BRgODDW2jP_a_QxyjzgWUKP2G3bQBgjFxYUYq8W_wtgy6gx08H1GGAYQpcp8_YRm0pztwafwM31Lt_lfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه نیروی هوایی ادواردز آمریکا اعلام کرد یک بمب‌افکن بی-۵۲ روز دوشنبه ۲۵ خردادماه در ایالت کالیفرنیا سقوط کرده است.
بر اساس بیانیه منتشرشده از سوی این پایگاه، هواپیما «اندکی پس از برخاستن» از باند فرودگاه پایگاه ادواردز و در ساعت ۱۱:۲۰ صبح به وقت محلی دچار سانحه شد.
در این بیانیه آمده است: «تیم‌های امدادی بلافاصله به محل حادثه اعزام شدند و عملیات امداد و بررسی همچنان ادامه دارد.»
مقام‌های آمریکایی تاکنون جزئیاتی درباره علت سقوط، سرنوشت خدمه یا میزان خسارات احتمالی منتشر نکرده‌اند.
«بی-۵۲ استراتوفورترس» یکی از مهم‌ترین بمب‌افکن‌های دوربرد نیروی هوایی آمریکا است که از دهه ۱۹۵۰ در خدمت ارتش این کشور قرار دارد و توانایی حمل تسلیحات متعارف و هسته‌ای را دارد.
@
VahidOOnLine
آپدیت:
هر هشت سرنشین آن جان باختند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/76396" target="_blank">📅 22:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76395">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/10d585b107.mp4?token=fwVUEBC262M9CrPxDy_JMwo5BgbhLqtxLWqtqcDnlJPPe3PyI8NvoIaA_2SvROQLbLXjqQXWuRCXJaWMU13zr4zvAeoDJh8e5Lwq7m34Yvw9u0ozZH63G4r1DTyDBvye976_iXqqR-GJPMOJyQ4oON5KV_LGwmAWqXd2Zbxliv8Ia8pSba36xjxwcfG0cz37to_2-zNbmairDKMyQ99mOpAv022X4RxtA7bKTITlOCScg-udoaULrUVjPR9AJh3YfPs6qGxgCBWnO1uVEMGnwXeBaNrNW74jycftTShoZpXKi2_5NrbQvKFMgOi-nR1XGpuSIK_WxnZmYxp3K0PLT7HrnjGHmfRONyoQJwyQJmc8kHo5WVBe9kOnNghphlnXf4CbQ4bzPatVc13O4QnJoLM-r-zBx8PLUYfXDrbxhaW11ovof5T4elsPRfPkstzKi42NBeGneFx5H3W2EqP-Gbu1nEzjl_lmOypCs9gbVjG-g68P_biWrjpe97--gfQHlzm-63CP1Phpd1RUyGyIJDDDHam0t2mOZiQP_Mv8AmMP8PaEe6c44cSH50jNpgOEA1Pg4EeuJ1MM6OVKtTtkQMpHZU6sWRLniXVgQTSgz8tZyRsDCk7KcHHrODsgrSYw6PAzAKNaBPvvk2LRoIILkeXjXms4P0wZJhkq8BdrcdU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/10d585b107.mp4?token=fwVUEBC262M9CrPxDy_JMwo5BgbhLqtxLWqtqcDnlJPPe3PyI8NvoIaA_2SvROQLbLXjqQXWuRCXJaWMU13zr4zvAeoDJh8e5Lwq7m34Yvw9u0ozZH63G4r1DTyDBvye976_iXqqR-GJPMOJyQ4oON5KV_LGwmAWqXd2Zbxliv8Ia8pSba36xjxwcfG0cz37to_2-zNbmairDKMyQ99mOpAv022X4RxtA7bKTITlOCScg-udoaULrUVjPR9AJh3YfPs6qGxgCBWnO1uVEMGnwXeBaNrNW74jycftTShoZpXKi2_5NrbQvKFMgOi-nR1XGpuSIK_WxnZmYxp3K0PLT7HrnjGHmfRONyoQJwyQJmc8kHo5WVBe9kOnNghphlnXf4CbQ4bzPatVc13O4QnJoLM-r-zBx8PLUYfXDrbxhaW11ovof5T4elsPRfPkstzKi42NBeGneFx5H3W2EqP-Gbu1nEzjl_lmOypCs9gbVjG-g68P_biWrjpe97--gfQHlzm-63CP1Phpd1RUyGyIJDDDHam0t2mOZiQP_Mv8AmMP8PaEe6c44cSH50jNpgOEA1Pg4EeuJ1MM6OVKtTtkQMpHZU6sWRLniXVgQTSgz8tZyRsDCk7KcHHrODsgrSYw6PAzAKNaBPvvk2LRoIILkeXjXms4P0wZJhkq8BdrcdU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"خون آقامون رو چند فروختید؟"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76395" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76394">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4de6c46b4e.mp4?token=AT5veYu8rm7Fq0Ffpu5pZCzEBhZHh3cSsWJVuq6jVBNL-7MizRKdrMxh8kkfkSAAonw6vOimioCchrWafJdlNnz4dxxtTuIZK_N-tP78WsWXmoVzjwhu5tC69Dp4mmRda0urdfw44H82b72FovJ0UndDwlBTgMW6FaHQgKrd7UE4w57Nigf1d1mN8e2zEp26gVV8-eiN0PkZWT79rvrcXffMxpL0zQ8BcR7DIuM58eO_n683lePp7pvnv9KJxtXMv56slJ-W2AhjEzub9DKR6Sce4t7WZ35e4iMcvMiq4ncBi-UlVvT5QWjpy0HGBMiy6uHEOey-ck3jqAp9Ug38Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4de6c46b4e.mp4?token=AT5veYu8rm7Fq0Ffpu5pZCzEBhZHh3cSsWJVuq6jVBNL-7MizRKdrMxh8kkfkSAAonw6vOimioCchrWafJdlNnz4dxxtTuIZK_N-tP78WsWXmoVzjwhu5tC69Dp4mmRda0urdfw44H82b72FovJ0UndDwlBTgMW6FaHQgKrd7UE4w57Nigf1d1mN8e2zEp26gVV8-eiN0PkZWT79rvrcXffMxpL0zQ8BcR7DIuM58eO_n683lePp7pvnv9KJxtXMv56slJ-W2AhjEzub9DKR6Sce4t7WZ35e4iMcvMiq4ncBi-UlVvT5QWjpy0HGBMiy6uHEOey-ck3jqAp9Ug38Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه ایران، روز دوشنبه ۲۵ خرداد به خبرنگاران گفت که قرار است روز جمعه در کشور سوئیس که محل دقیق آن مشخص خواهد شد، دیداری بین هیئت‌های دوطرف انجام شود.
او توضیح داد که در این دیدار، «قرار است روسای هیئت‌های دو طرف ابتدا این یادداشت تفاهم را امضا کنند و پس از آن اولین دور مذاکرات بعدی را داشته باشیم.»
@
VahidHeadline
محمدباقر قالیباف، رئیس مجلس شورای اسلامی نیز در واکنش به امضای تفاهم‌نامه توقف مخاصمه خطاب به مردم این کشور گفته است: «با مقاومت تاریخی شما و رشادت نیروهای مسلح دربرابر آنان که قصد جان این ملت و نابودی و تسلیم این مملکت را کرده بودند، ایران گامی بلند به سوی پیروزی نهایی برداشت. می‌خواستند و نتوانستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/76394" target="_blank">📅 22:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76392">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c3fdaedd66.mp4?token=SioC3pGS1fajV1Vxqts-ECXtbKFleKyip9s3nqq_Tdu47u_tu3PGW5h3NTeatIUkonFc8LBNGxBrAoAaZ3yM-VNEfn0Jt1cJpODvE0yZNF5M9a6FI8xkk9q2GokKwR-zktUzeYygSvzEuwfxfvp9i2znAqtVEHxVAM5Mht5lP-Xep7J-MYUSxNMBRR6ccuyAh2nu1KMiC8diS58feGxAnl-b4Jnmy1Xsg-KzbHwOXZrpn_Pf-K2g8AkdMZEeNQKGBX_iIKTlnNJxleJs9MwKo4a6DGOE6MccPxxoLPNu1lzlaiinf9CUN44CEIO7L4tiJPWij6nD9DpUjabViQI0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c3fdaedd66.mp4?token=SioC3pGS1fajV1Vxqts-ECXtbKFleKyip9s3nqq_Tdu47u_tu3PGW5h3NTeatIUkonFc8LBNGxBrAoAaZ3yM-VNEfn0Jt1cJpODvE0yZNF5M9a6FI8xkk9q2GokKwR-zktUzeYygSvzEuwfxfvp9i2znAqtVEHxVAM5Mht5lP-Xep7J-MYUSxNMBRR6ccuyAh2nu1KMiC8diS58feGxAnl-b4Jnmy1Xsg-KzbHwOXZrpn_Pf-K2g8AkdMZEeNQKGBX_iIKTlnNJxleJs9MwKo4a6DGOE6MccPxxoLPNu1lzlaiinf9CUN44CEIO7L4tiJPWij6nD9DpUjabViQI0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در گفتگو با شبکه سی‌بی‌اس اعلام کرد ایران در صورت پایبندی به تعهدات خود ممکن است به صندوقی برای بازسازی دسترسی پیدا کند که از سوی کشورهای حاشیه خلیج فارس تأمین مالی خواهد شد.
ونس با اشاره به مزایای احتمالی توافق برای تهران گفت ایران «ممکن است» حدود ۳۰۰ میلیارد دلار منابع مالی برای بازسازی از کشورهای خلیج فارس دریافت کند، اما تحقق این امر را منوط به اجرای کامل تعهدات جمهوری اسلامی دانست.
او افزود آمریکا با سرمایه‌گذاری کشورهای حاشیه خلیج فارس برای بازسازی ایران موافق است، اما این اتفاق تنها زمانی رخ خواهد داد که ایران به برنامه هسته‌ای خود پایان دهد، فعالیت‌های مربوط به مواد غنی‌شده را متوقف کند و با یک نظام بازرسی و نظارت گسترده موافقت کند.
معاون رئیس‌جمهور آمریکا همچنین تاکید کرد رسانه‌های نزدیک به حکومت ایران بر مزایای توافق تمرکز خواهند کرد، اما از امتیازاتی که تهران باید در مقابل واگذار کند کمتر سخن خواهند گفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 320K · <a href="https://t.me/VahidOnline/76392" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76390">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFactNameh | فکت‌نامه</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/agQQ87cD-tTYcIhfCqrMVS_0JKolwLH3HzPE2pf9K49oBzZwsetSQ08jeu6yEvn0e6mC9ht4rhDAPIJEOF6lt5DG3fIoe5pQ3rUOQ36G2MP2CJlxr-IFbB1G24cX1QFGfwpbJOd7fF8bzROHP_ZMq3NLeh_fqXHSerYwqXZQ5nOLcZ1sjfkPEYvtLNq4deMG7F7ilu6fTAAUo8O93t-gc8SqNCvrEikUT24OehS0Ve6QdHnq9LG6ceGjrzqxTQb5CzhoC95uvyJOfHYmP0F7M5_0oNa6LzNkhYEybKB0kV1zE25GUZtLBjP6MwVsNFTVR-8Zs-WyBmS1X-FezA1FkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k-BgJ0HIIFMZzj7OnQasIQuMe7GYm6b16OVfqZMTUi1P38YzwtHz473yc3BrR-94K--lI9q9h6Uu1sQca2SfcHINKFnnfnuZ-yOVhDdnbG5PlaOq4Lmb-ZNS16dEXcc5TnQKkgVwOCAxbdpqA9UD2U0tED4aMuuJt79Vrcbmu1tZMNaW1pZmZxztOiocqyBGdW0UdufHgr7HoXEeFIp7xRLVSPKHQFmbhhOp7XPABlF_HB2TEPwvuHR_mlm50P0IAVtO3Cx2nA8glsRAWr1VdDUFP9Vcstv_FlT3F9FgydPgrVI9Nx4JBiQ2tGM6mtks9v8p93R7x1hWQcWleM6DMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
ویدیوی قدیمی منتسب به تیراندازی به هواداران حکومت در تجمع شبانه
🔹
ویدیویی در شبکه‌های اجتماعی منتشر شده که ادعا می‌کند صحنه تیراندازی به مخالفان توافق با آمریکا در تجمعات شبانه هواداران حکومت ایران را نشان می‌دهد.
🔹
این ویدیو قدیمی است و ارتباطی به تجمعات شبانه هواداران حکومت در ایران ندارد.
🔹
ویدیو مربوط به دهم اسفند ۱۴۰۴ و برخورد پلیس عراق با هواداران جمهوری اسلامی است که سعی داشتند به سفارت آمریکا در بغداد نزدیک شوند.
🔹
گزارش‌هایی از تجمع مخالفان توافق جمهوری اسلامی با آمریکا منتشر شده اما خبر تیراندازی به آنها در هیچ منبع رسمی منتشر نشده است.
🔹
این ویدیو پیش‌تر نیز با ادعای نادرست دیگری به اعتراضات دی ۱۴۰۴ منتسب شده بود.
🔹
بنابراین فکت‌نامه به ادعای مطرح‌شده درباره این ویدیو نشان
«نادرست»
می‌دهد.
👈
در فکت‌نامه بخوانید
🌐
@Factnameh</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76390" target="_blank">📅 22:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76389">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccb668e4af.mp4?token=KMI1bxosUjWhpXmHB8chhoLOlE3rKEqWicjZruVfLxMzqG0KizTCqfX6CsaTPrhaoKr0aRFcvDvEqP5SS07D-eLMhYAKWnYmvpJ4ABD1Tk7d7iRADTeA4kWVwDdgvroaFX8npFn_X6eJv1hiBZrTiaHw7X6n0hhd-jsCXNtcQFFGx1-Frmqvzg2YumEdk1TxLOYvuYwJPBYEP7xE3svT-0PHxGt9cDjgfuA8FvIMCTuAzXTUY349lnojHwYPueUlVu7bY-iq2txeT18wCtSJxgfKGW_X17yRU135uRm3U6JHvUPYmFKuDJf5E8m35xF8mWouEAqAXjKlTsuvM6oy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccb668e4af.mp4?token=KMI1bxosUjWhpXmHB8chhoLOlE3rKEqWicjZruVfLxMzqG0KizTCqfX6CsaTPrhaoKr0aRFcvDvEqP5SS07D-eLMhYAKWnYmvpJ4ABD1Tk7d7iRADTeA4kWVwDdgvroaFX8npFn_X6eJv1hiBZrTiaHw7X6n0hhd-jsCXNtcQFFGx1-Frmqvzg2YumEdk1TxLOYvuYwJPBYEP7xE3svT-0PHxGt9cDjgfuA8FvIMCTuAzXTUY349lnojHwYPueUlVu7bY-iq2txeT18wCtSJxgfKGW_X17yRU135uRm3U6JHvUPYmFKuDJf5E8m35xF8mWouEAqAXjKlTsuvM6oy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، اعلام کرد نیروهای اسرائیلی در آنچه «مناطق امنیتی» در غزه، لبنان و سوریه خواند، تا زمانی که برای تأمین امنیت اسرائیل ضروری باشد، باقی خواهند ماند.
بنیامین نتانیاهو، نخست وزیر اسرائیل، روز دوشنبه در یک کنفرانس خبری تأکید کرد که به‌رغم امضای تفاهم‌نامه میان ایران و آمریکا، چالش کشور اسرائیل به پایان نرسیده و «ما باید گوش به‌زنگ بمانیم و در مواقع لزوم از خود دفاع کنیم».
به گفته دولت آمریکا، جمهوری اسلامی در قالب تفاهم‌نامه‌ای که روز یک‌شنبه امضا شد تعهد داده است که هرگز به دنبال سلاح هسته‌ای نرود.
نخست وزیر اسرائیل در ادامه سخنان خود تأکید کرد که «با یا بدون توافق، ایران هرگز به سلاح هسته‌ای دست نخواهد یافت».
نتانیاهو در نشست خبری خود همچنین گفت که حملات مشترک در کنار آمریکا به ایران خساراتی سنگین وارد کرده و به گفته او «بعضی معتقدند که خسارت اقتصادی به ایران یک تریلیون دلار بوده است».
او در ادامه گفت:
ما به مردم ایران قول دادیم که شرایطی را فراهم آوریم که رژیم آیت‌الله سرنگون شود، نمی‌دانم چه زمانی این اتفاق خواهد افتاد، ولی خواهد افتاد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/76389" target="_blank">📅 22:09 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
