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
<img src="https://cdn5.telesco.pe/file/hUEp8XfCtW9Z6zlJulYiyVgtsTiHF-ATVrStROt45Au4lncQBrxpxkxE7MvsHaoE6Zzypv5CecIUaIn9aYTa55D7qhKNd2Vngcow0IOj6Umwcwd4b-edKrosf-w1w425pidIkYSQV3Qdb7y4ZL2MrwEUyVKmuPjcVKW111328VUdbsaei5kQxiNrTjUSLn4JeCOXsUqvsKrI9lzosuOI6nBw6JBlGS3gM_Sz6SXo0_e2SKkn-e25XQe4MakN7q-C4pq7pVTW1eKe_F5Az6keGmkQ58VWRcVod2aEOO1fLVT-udjXUOk75JkbwNwi3UguNq6Que5AjQA_57XW3YpmiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 645K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 08:31:44</div>
<hr>

<div class="tg-post" id="msg-98129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXtwgLKf0bR3uxyj48I9G9ZCdhs02BUKKQLFw8wpinMflQ53xAVsI0viyxvShUaY3XHYHWG5L7oeaSPdaxghNI8ar2lHhV11oBklGZ0BvubsBFcTTiDJ65wfwGwR5BcjoEs_8S_3Ku_Fiav0xHLmUIVK5r9nDumv8SXXCTDMhNQhlcWYtRf4yAKHMFO4nWq2vpoBhd8GOl-1-S-BWGlkDqzs1zDFdA-aS0Spuoj0BnM8wJ2H4rP3ZzSc3niQsAP8lxrv9oqMHSQLZAG_9_-t0Ki5xekD_oC5lbn7iwtnh6DEYPKP7EpeSHYwuextEQTW_C7PpWOL24mJTAdvlBszyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
ولی چه کیری خورد این بشر؛ تو چند ساعت هم تیم ملی کشورش از جام‌جهانی حذف شد هم جادو جنبلاش اشتباه در اومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/98129" target="_blank">📅 08:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98127">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeKjbdKiPdjEKW3BXL9ZNZJZ_acxvSRcfgSaACqog_uc_lAQLAspbf5CrTiLcFvlPePr76I-_yiHNsnzYp7peU04J2lzZUMSIgDyC9CJWU9wK9eeOM2pjh9eC1iE3z05C383iBajYHAAI7NgC2m8g_vUumipO-A16yyHs2jh_he1rX21kXHcDTDBMrQeyEpjiW-_2-MkO1wfY78GUwo2fByEadMF4WL5304M1FV3CcgL6PL7sXnuQ9AsBNaorUAzfixNgUR4vsocLRw7ahe0_H2-oFWrmP0DWR2sbNtUCYMPHQfl0GtZ6c-Mbxu76yykm77yNuhep8ZXz8i5MGQaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه مسابقات ⅛نهایی جام‌جهانی
🇨🇦
کانادا
🆚
مراکش
🇲🇦
🗓
شنبه ۱۳ تیر ساعت 20:30
🇫🇷
فرانسه
🆚
پاراگوئه
🇵🇾
🗓
يکشنبه
۱۴ تیر ساعت
00:30
🇳🇴
نروژ
🆚
برزیل
🇧🇷
🗓
يکشنبه
۱۴ تیر ساعت 23
:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
مکزیک
🇲🇽
🗓
دوشنبه
۱۵ تیر ساعت
03:30 بامداد
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
🗓
دوشنبه 15 تیر ساعت 22
:30
🇧🇪
بلژیک
🆚
آمریکا
🇺🇸
🗓
سه‌شنبه 16 تیر ساعت 03:30
🇦🇷
آرژانتین
🆚
مصر
🇪🇬
🗓
سه‌شنبه 16 تیر ساعت 19
:30
🇨🇴
کلمبیا
🆚
سوئیس
🇨🇭
🗓
سه‌شنبه 16 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/Futball180TV/98127" target="_blank">📅 07:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98126">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUpPqx-8FFpRHvfQPN3iZZcssZY81ei_-h7zhk54fj08B_F2fNH-cF7crN8b4sqck2KT9xUWsnzKqStGjMRQCSIN509YmGod8MpeViIAH671aeCEfEO9dvnn5vqfjfxAR2QvIwGFgykeXkmD64NzTqTs-mAkHks7tLYZsRz-bAcV9KveBdgGxjkmCt4idaZNBIlZId6eZp5oyw0zsvb_HiaMfA7FzOn7CGav5f7BI7f98zi9Z08br3Kp-0c1AkWs2hfSTI0-VV2TeMlVrDBI3TwCkZiflLCe9CW7JGiRbGV01VhTEq1TwReME1_AaakM-SmT3HJwrnwGReSXOoLZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید
❌</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/98126" target="_blank">📅 06:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98125">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کیروش کون سفید پشت هم داره از کون میاره</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/98125" target="_blank">📅 06:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98124">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آفساید
❌</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/98124" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98123">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کلمبیا دومییییییییی</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/98123" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98122">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/Futball180TV/98122" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98121">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDPA0PXkllNvSgdW0fyuYBNb9DCpVohcyNYGHzCV9i4dHxrGcGUVx_II3w_A9hTh8u940fQ6WKyMXbN3WGG74gKknC8ezv2RlU19-whAXpvQcGjSPHQi-arfQkQ6rY6OLI3nMI401YRxz20lFRAXlYXRvQW5PJ63IPdRPPBg2G1DKoHbtQooHXQoEFHxl9rUzhDkUSOJ4Ah37Q7-R9IEGhOtJFh_T49ga9GL2ouW1h7GA9rNyj0N3xwxLDhreAGmgiNuibIzvoTk1sycpRUJuLZX7_D8vdPJ1zvHUVbrCyBJD4MGjZ6c_X5Yd0a_uxY9Y_k0qPFlQr2BN6qJC7QFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار دریبل‌های موفق این بزرگوار: 2 از 2
🔹
نیمار: 0 دریبل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/98121" target="_blank">📅 06:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98120">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djfXPEZNV7rC-cGnECHs4rzewtlAzaBbUScfbfqef0SDWRyhJmgtS016fz80jYW1bGu9o-aHHWniLiCD801ruXtVKSwhKtCrn3QAcplkBHx-HAEUjtQUQfY2rZQKoUEmYexJtZWqDUW8dRYFzQHXGXA1evhu86WgEbEhLWSwIFkaItJM3oZdb2IdyYDPJ6Px_jc2_e3EjpBCEJHQxZGhGYpX6fONCQ7XF8sFPcLKqjrG-KCS6i8Z093E-h4di9NMAOgD6i9lnbYVV3mn_57GzCHKYVUobu7y1KZ3EBhjBCcOErgWH33jJPtJtjznpUAxVFkLqII8G7JNenvrv9dVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خامس مصدوم شد و بین دو نیمه تعویض شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/Futball180TV/98120" target="_blank">📅 06:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98119">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/Futball180TV/98119" target="_blank">📅 06:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98118">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇨🇴
گلللل اول کلمبیا به غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/98118" target="_blank">📅 05:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98117">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8Xp8_eIqU6Ez9TqHDo5lV9pVNYdGixDCaG8-ZnhTfwYYFxDipxUizpuKPD_DlXnBZpxWpC72qpjbb-JV8Tds39yTIcWdA8auvGOn5gfz9VGyoPrw7WpCliwKMESosJTIRf7PyzhOD95rk46A3ji3RTwdYuXQeriS6YREROg0lRN4g42wI0Rtdri5JirhV5j908nTxzl18NK_PwQ2BzbGzreUWV2Mm-aRCYAciIbWXutKLRcmFn5aEGUlywd5i-heS0ZJBEkqqWCBIncLOo5TXBobSbpL4K2mawk0EBFTWvdIISstuOxnSUaK5MmSN5hGNFPTJiCD15w1IF_8johPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدترین بازیکن آرژانتین در جام جهانی خولیان آلوارز هستش که در کنار مرحوم لائوتارو مارتینز رسما آرژانتین رو بدون نوکِ قدر کردن.
این درحالیه که مهاجم نوک اکثر تیم‌های مدعی مثل انگلیس، فرانسه و پرتغال نقطه قوتششون هستش
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/Futball180TV/98117" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98116">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3mkYJWJ0SOIbz8WF--QlsXNkY7C-SPdTawd094pIWV2d-PwjcxBLhV9UYKeV0TOuH-07YHyb6bXfa1jEzuUYJnZyetbTTlFwT8EvmyA7mCQ5FEAetp_wgUGhNGC3OlPNWOv4DSE3PswKpR7RL0i_4fNqOvpYYXLedLv9H3XnFlUSQupTBQEfa-58IaJdfCoOyFOw6NhhR0QActcVYWC_C7EkX_Gas02IfqJ_xzgMePANB5KVmf4XBkwrgcbsrIy0DOa6Ob2tEZrsek3jndJiiKuMpZAvexRLM4JHU5UNeTxojnsrtM3-BL_TG62vZqTFFSij9rvFiIjGJT5f7_aIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتونلا هم اومده بود ورزشگاه که شوهرشو تشویق کنه
🥰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/98116" target="_blank">📅 05:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98115">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16e1357ef6.mp4?token=rRAa88fFljloSYpwZSJHfE9BImcWqd6bLVT3aCoE6nnY-buv-OYYW_iwsBCpFeGvDXjgwvRqHEQx1Qe9YVamGWQh-2-WvOmbGIlf0Xf2ISCZ-WfN45JxNNZhPvqZF7J5cV2oqq2QzFEqzwsYU7XjfHT94fbG82Sc2MsLA5Z1hp3_TItyqPoUmYj_0JNzh5zxpeAGx2g0dsIUx_g0d2Zn6_EzjHOqYxGySUKBnYhLzLk0SRVYa_vtbvrTWgz-po7viXLKCZQQl6i6em99fu1KuMv_Nyzyrbq5btzFKmv-SqPEgoZX0RNZRrHTGfiCtIzpwj3PpMzbrBF03tkTbITwUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16e1357ef6.mp4?token=rRAa88fFljloSYpwZSJHfE9BImcWqd6bLVT3aCoE6nnY-buv-OYYW_iwsBCpFeGvDXjgwvRqHEQx1Qe9YVamGWQh-2-WvOmbGIlf0Xf2ISCZ-WfN45JxNNZhPvqZF7J5cV2oqq2QzFEqzwsYU7XjfHT94fbG82Sc2MsLA5Z1hp3_TItyqPoUmYj_0JNzh5zxpeAGx2g0dsIUx_g0d2Zn6_EzjHOqYxGySUKBnYhLzLk0SRVYa_vtbvrTWgz-po7viXLKCZQQl6i6em99fu1KuMv_Nyzyrbq5btzFKmv-SqPEgoZX0RNZRrHTGfiCtIzpwj3PpMzbrBF03tkTbITwUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
گلللل اول کلمبیا به غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/Futball180TV/98115" target="_blank">📅 05:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98114">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کلمبیا اولیو فرو کردددددددد</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/Futball180TV/98114" target="_blank">📅 05:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98113">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شروع بازی کلمبیا - غنا
🔥</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/98113" target="_blank">📅 05:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98112">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsdwKZwid9UAKF4THbvKsgbmbmMjb1q3k1j2Lxt58qwWPaQEmtJwm91UrnpNqLKBOQ11G24gKkPjcNjIcHj23NXcNZouV0biFAzvwaHsheM9x25-tvekDaixYSd8NQcY2m-S681JCylp2cSK67ikCAOr0Qqnl3h7WQuGyD2j6uL7Oi4Gvs-FubKmayT41CTupKK3hnQxmmTBMVPaJFX3DUyoCwaCjW37dX08o-kuRRJ52fUCawGNCuFfTfE9oe4FXqY6qpfZ_oS5z416t4C9uHjAJUh2CrFd41TdkopB_fksr_IyqkNNWJI4gFxaypmMiANuD3aYwfrdAhDN6G2HyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🔥
🏆
لیونل مسی، اسطوره فوتبال، اولین بازیکنی است که در تاریخ جام جهانی، مقابل 14 کشور مختلف گلزنی کرده است.
‏ـــــ کیپ ورد
🇨🇻
‏ـــــ اردن
🇯🇴
‏ـــــ اتریش
🇦🇹
‏ـــــ الجزایر
🇩🇿
‏ـــــ فرانسه
🇫🇷
‏ـــــ کرواسی
🇭🇷
‏ـــــ هلند
🇳🇱
‏ـــــ استرالیا
🇦🇺
‏ـــــ مکزیک
🇲🇽
‏ـــــ عربستان سعودی
🇸🇦
‏ـــــ نیجریه
🇳🇬
‏ـــــ ایران
🇮🇷
‏ـــــ بوسنی و هرزگوین
🇧🇦
‏ـــــ صربستان
🇷🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/98112" target="_blank">📅 04:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98111">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOrl_CP3s9DOscrupUbELT1hSaR6f8HP_5su5M2_vxilrm_Evgm1TxjEh8YJIRB3HEWb2oplmdU_Pq3pNiTsuKTzQjsI-v5eOTAMbsMVYIGAfjCS5asNClBNDzQJkwnAUOiFaCxomtvqLbWCYwrbLLHcFpQiALPLqRH0RQxcynSzkn28zWma2YnpUZCwm1T1qdqe1x_p_1Z3i9wmBMQiT7LY9sHdiiO9hKmw48D0_Pdh5-qq_qa8Yn61p3ExM63DNA2pNxspeRV9dUjqUUI-pC107VjBRl3cMZgaD-oeysaBGiwOijU6ybdI8Nrnr3dUNP1LrQqloopcrDiCxTawDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📱
مسی همین الان گل زد. فکر نمی‌کنم تو بتونی کفش طلایی رو ببری، رفیق.
هالند پاسخ داد: "درسته"
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/98111" target="_blank">📅 04:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98110">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBrWkqfz37EFI5FhWvghwb5ovQKWE_jg-M5NJvnGkDctqJ4hu8gFZwY3EQngIX-f4VRHHtQuuoOvHToHzpWN07xYFHDwtl2i1ROxXgt5vzXrt3djKeY_JRnMl-H2_bRGaLZrCedHyZfUn-BwuJNwwJMzLH2r66k6TkZrB1LfC2khWtB-B717t4RGfwRFn-S8_sf2-eMhIwqCfqxa8CgyJqc3tXZ0FXh84MloGRnTfzwpAlAL-3yt3awuOH1bxpSZpXZdif5h1BVAgCnx7GBvCHWVZ1H7Kq0X2kMoWG7acH_1m_AbXi4IY-huh2ee1FywDc8NPgjNGDN0WZYhgIWnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
🚨
🇦🇷
🇨🇻
🎙
لیونل مسی:  ‏ ما دیدیم که تیم کیپ ورد در برابر اسپانیا و اروگوئه چه عملکردی داشت.  ‏می‌دانستیم که این مسابقه سخت خواهد بود، هیچ حریفی در مراحل حذفی آسان نیست.  ‏گاهی اوقات مردم ارزش بعضی از تیم‌ها را دست‌کم می‌گیرند، اما ما مطمئن بودیم که این مسابقه…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/98110" target="_blank">📅 04:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98109">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgKQWoeA2lHs5F_5_Au0izl21_V1VELg4iV0mg5NDhCto_hGvrY2g7sp1387KZhBwHGjn4wi8cjWeP8qupG-f4DsP7SmfDgozoKmc7X_rxImBdF8p593NFaVTkXPdmfDjuv5pCRZaufe-ZP89yHjSllJQdoB9KfKEsRh23j5XatYiOy6rUFQVTX061Ej87hudv2Fa9p8emDlwFH5w56uH1v7lkH1bDSnaJgu5K10up8B1VWdLWhCrv2_JoCRAHYRWTCUBLAQNGRhJOaoJiz3dCP_HCWa4LWg3v1ruyUC_1J1BrgzF6bfRUKoJyAW4uzLZ0p9Vvfljkgph_-upicX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
لیونل‌مسی برای چهاردهمین بار جایزه بهترین بازیکن زمین جام‌جهانی را کسب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/98109" target="_blank">📅 04:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98108">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMvO5GVjrIp_Ln1Xw7MmMRkCjaAJJY6wizLzzuW8_RctyDeBRHE6bCcJlKQ_ZIK1C1krIuO1TPfEd5ZDg6hLeXcCa6fta60pN6ExTbmlERsGJLId8yj5KBJirWaqkLWyqFVI9lS73cJew59TdaFhJW9tMSQ0mVvA9kuUr7_GEQubucn9ewpFqUVCaiSYmrBaCMW5gvQnlwfodXZ4FCQnVlHN0aOWvPutuv1DxNReUBFRmUurVMJjAY_XGuZPidgd1-JbBb4QC7XZ6QVzF0jDzhGLYJsj6qLTSn9_NXKL0EEw4SjrhsMVAVJSUz9wzhi53GtE_D7Siw-e_fBSn-QkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇦🇷
آرژانتین
🆚
مصر
🇪🇬
🗓
سه‌شنبه 16 تیر ساعت 19:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/98108" target="_blank">📅 04:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98107">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfwDc8GzQhDFX-A2sk6vhyRZXZdo-RSTLkU2Qbd3FDWI_VvZ0NpdoBOazq5lVBsWtfSp6rWknwWGjZq_S8fcN4lymtjMz7_OoHwi1aZClX0UgIXGfv4GxvuYbCkm28HMqB37UEFaP_0niNEFYQJfYaoPXTtQTF8lQux8X-WcpYp8rDBKoTOTAnm1NYzVE70dY5K0jxmNv3E1SJk7PrEK0RPpxRx78BBe6ImxhamUC3FfNpUE_LTO-0XUy4nX2yM2TdolGh2YkahDGBZBJJbVk4pmQgOl_nEojvZvelGbEXdPwWfcSm_jC4qdV2aS9UAjXQPOm3UnYmuqmDXGj1jJjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاتوووووووووووو
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/98107" target="_blank">📅 04:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98106">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhL5QKPpgmcCSzyQLpH2gambaLVK7xP4Ipeyju8ORd2b4yughgGtaoz_1FbTDZKIQg_RhUfnFPOqbE2xtzcAhJpLRRLwS3tQYzNmCiBEte3r6g0tsQ_hFugKgZgsy-jptq8QmiFkromwJhj9uN-V5SV3C9Ouri3kef6xE2Jd68tAENIOkv71UUbvt_WG5LswHQQKxqQyc3245VS9u12pj-rZaskVarNmFLcHTqlKUufAgLjGwe9UkxrXPt-zd0pgwbLoyHIhCh1FUkuPEKTD8abBadvYe7l245Y8ip4zLAV5_rJ7yaopJB_gKJV5Yxlx_vIeZr_8Ml1T0dQ8gVxigQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار خلقت در ۳۹ سالگی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/98106" target="_blank">📅 04:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98105">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🎙
🇦🇷
🇨🇻
لیونل اسکالونی:
«می‌خواهم به حریف خود تبریک بگویم، آن‌ها امروز ثابت کردند که یک تیم بزرگ هستند. وقتی می‌گوییم که در جام جهانی بازی‌های آسانی وجود ندارد، این واقعیت دارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/98105" target="_blank">📅 04:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98104">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPzHPiI8HNGSTeBHLkBxHxGA8bllAtaGpOXUrOihAk3sALiF_hl32aivKoGKWm8tm_M5jWHwzn7XwUThYmv6ImzWULs7sgDl_GMXNrVuwgZuFf7xFQdUo7tprzWuf_pmOi5mxHxNZKrxv6-ZZInoU56QQqaFSjtAXCFsb6NhptLAq4MScLkadzCVkyOHvKF-RYnNFv0ifV7SoAOvlrZ3TqOUoBu0aVvKl3izGDKUSD7ubWMe6FnD0GXF3P06bAQ8kJBy12H2tKors_pZ3_9Kjxr3IKP96Z8wshPqmX5khjV-d9Eq8cXGS1B8qk0vEu1o-JQGDwaSu7mgSFCldYaUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/98104" target="_blank">📅 04:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98103">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTAnSbrxUj-NABfceo3i9xAZizEnVN8qLI8Fe6xBaTkMCp-pKfx4SO2mH5rIkZcd3IDCa-RilTZqqqKg8O5NIbsthdKAEbDdj-uOZvDjllkxdgKa5-lrF5q-8onXpiTSUyaZefm5ywwDGxfit_FXjPp8vMRKOXMFnnaMsunQwOi2PEVJejiwTfH1wTsysNBziLj0L68IJG7LMxsjTWrXDJrGe18cwl_qn6S4DhynYuCop5t18EO2j3GATF7uLODOKYFRqVQdBUxyzs_cKJ9qjRCiWW0nqJikebTz_H9VZIe6YaBprDjk024p8VtOcVMkz0vUy5UclNy-rI_sU20-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🇦🇷
#فکت
؛ آرژانتین (از جمله در ضربات پنالتی) در ۱۰ از ۱۲ مسابقه‌ای که در جام جهانی به وقت‌های اضافه کشیده شد، پیروز شد (۴ برد مستقیم و ۶ برد در ضربات پنالتی).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/98103" target="_blank">📅 04:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98102">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWIZsjDzRmotjMsgoXnhCDc0G3rX_7R2qR4WgSTqeNpYO0jga0o8URV_xWNGbcz5kRaC5-hVTVYfuMt-RmPzweCz7_w6-VxdDBNIw_1f5AXuou7Dk8OIIn5wpeI08UnxryG70nqa3GeSZi5yzCAL1FcQ7B-eVMxRBHeHKmCAFbQuSQWGeYvxvVLMdtXpVRYKt_9QPIND_h_pLulqKwdO-MfGfRzFgXPIJ1DLZ1xiJ4pwButKIYGNOoifmqfQl7xavlp4YZv0n9Ty2lGK-QMb0UcsaxoLXbDZ867Isu3zxeTmsio6tudJ-uYcEQCPJnh0S3-XnhRpR2HZ3qkiReKK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
گلر کیپ‌ورد مقابل آرژانتین
🇦🇷
|
✅
— 8 دفع توپ
✅
— 5 دفع توپ از داخل محوطه جریمه
✅
— 3 دفع توپ خارج از محوطه جریمه
✅
— 1 دریبل موفق
✅
— 8 پاس بلند موفق
✅
— امتیاز 8.4 از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98102" target="_blank">📅 04:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98099">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNDX-vm_3q1qYLQenxpclrb2mhKo4MmeRxuehIvDdcNBuJUipgSJOxseCMhDYEOjMahw1XpOPUxkQZaTtkM3LHYHnB-rBJ-UeY6z_sx0im7BLhO6Z3tnZ1bmil-ZFmyTRIxqOWafuuWelPiAmRZil8D8fgtHgW6aH7MhvoBRQBNDAmvOOsVRDsGZxVCfrGpgbeiDYR3Lfa9LXDY1j8JOIyIDsxsKjDjU70pew6_PpM-jlGQHQgHGYg4jfw_u9VKQWB-_InNppSgGQTRQV1iK3_AL9HNivK9HNTclACM-V-mgbjMTnCq03w6ohzvFiiQREdmO5OomhF1rc9Oa7UBCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
📊
مسی در مقابل تیم کیپ ورد
✅
— 1 گل
✅
— 4 پاس منجر به موقعیت گلزنی
✅
— 1 پاس منجر به گل قطعی
✅
— 6 شوت به سمت دروازه
✅
— 2 دریبل موفق
✅
— 8 نبرد موفق
✅
— 5 بار دریافت خطا
✅
— 33 پاس موفق
✅
— امتیاز 9.5 از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98099" target="_blank">📅 04:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98098">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خوب اقای وزینای عزیز الان ما بخوابیم یا سر کار بریم
کیرم
دهنت تموم برنامه هامو بهم زدی</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/98098" target="_blank">📅 04:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98097">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuXlTmx_CJ3BOtQFvDfaeaxCy610jU0a-QSGwoZegXCx2LhOCv8LEvvtZ2itGboQRCv2G-9xx8wiC8iEII6Rx0XBvt62lANZNR9maK8eQ-qmKjKBbYRgBWdRTxc3wzIPlSCaoywlXoOebnVKWsU6g_LTRkblZl1pBdvPJ6ImXdVMhdo9eYg5TAxkKM2DKAmxAKjakxfIYkhQHcbsEYkwVCf37K07Px-Zi8RPkCsVOzH8z5Vx63DRh8CYmTtli5uQmSZkJx8LhF_ZrXzH3kaQAzBkL-xezkWh2ZHwOaXak1r6YM5buPvtEvk4TzmTufDrKjiTeOgA9g0do2G_pdYEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک‌های لیونل مسی بعد از برد مقابل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98097" target="_blank">📅 04:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98096">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLqdeChgKj4KCnqEu3NNSWhnRY6vn3d8GCg_Z-Obd7nprJ8ZEQmOB-RGufKUwS0X3i6mStJGx7thiSSf_PmFK8CuROBM97rYIsyYAIpegJ5T0HB1I0iT1a80bYYh_lyW0B3DHR82Vde0zOdep2zbh22Mj-7POnvdUIGEN_D5suaYBRZmdJ1SwkMmtq-fvFr1n9XGIn126Q1chUj15f6x-UyL7zSi5DVx7iiJBIG3w7zzj_wT34z2I_INFrW6y74XCm_Uo9ON_2mW8C57MZ_WjUv01FEDrwYL1licxToz_gaI_lAoXUMz-QQUMWjysK81CqWWEfw48tBuOtcxISXhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیپ‌ورد سربلند ترین بازنده جام‌جهانی...
تا لحظه آخر جلوی مدعیای قهرمانی تو 90 دقیقه باخت ندادن و تو اولین دوره حضورشون در جام‌جهانی شگفتی ساز شدن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/98096" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98095">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98095" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98094">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vutdl29VRNxiGmERJBSWRL7EwdhVUkDKmTFA8su3iMG0HVZ5fjXHhhh3IzpGK5vaGovp_D27jNzd0VC2nz1DRH7JvvK2oxsEc6-DKv0WSYswMKHhxTazJtY_ct0mondsbUerq32DU1g7uS0GSXnYed_jzROJ3HA0eXL_vLkT5SZGaGsCbQXVlUyXInhS3wDj8jFnHA7q-FUUrXBij-TWcI2VHl6g4M4KPjgB_8IoNDdBDLKBoTt9ILc5GANCKPBsArFq2xvApHcXETA3YX0ODegr5GUTYBV1qEJM-s1TxxgDQ4Vu07lfsVl_lIyIboFZXF_vqEHfwHw1YTied4vKrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/98094" target="_blank">📅 04:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98093">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MW1KDzBrGtQzL8uQojaKXS-IdYhWkQ-hKYuewtuAlfXRxmQUS6wlDuoCx3hahBeJqPTTb6gauDe7bptQLGiz78BJe6CVGXu_1Wc5muUr114jQawKrDm4JTWZGNl2a70Vq3g1q47_L9YqdOSkV2hTaaNq1f7fJjHAsh8XBbpXY3Jwcdn7JTBVaC0hdt4VyPfGwLFw887MALZX5uOzLLDYP1wJMxWC26_0VXnGdqKkLkyfGGyn9hBTUp8jlFGSqq6ejklBpYIrd2-Aiq69oWu7Zj1zTC2oAXjgIdRYA1J1Zu6bN1lkJbni3cDJMnz2L1GxbmQ63IVqmX7MFMkT9E7wdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/98093" target="_blank">📅 04:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98092">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انگار این بازی خدا میخواست مسی رو بکنه
😂</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98092" target="_blank">📅 04:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98091">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaGiHuVSfpRiBSTuQlpu4ywgupMCzQCIY-mBvqn6YxwrzMHVn7Dvu9SCtMf25TVw4AFEyoTTSWmq_rbgykiokpIn-azenDN0zX5YYqDqLMIJZJ7u6jYX01p05LDbKSw_wobso_zTMDODOXGYOWq6qh8RtM1zsCos5LxVt9zytd9YH6N_QfijkWGNn2teqBn_xFCIyj0ozjaPS3HCrP3RsdM4nMh7zdGwIfuS5eNI-3wCqHwnl0rfmMhpAx48n01RRCez0N23FFjbv1AiYrJBS_GVY8Wp9GCJbcBr1ZQ_8QX2JrULIKFMM4ywkJ3_r2-fScgWC6b-NU3WxBqbssy4uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/98091" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98090">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">با اختلاااااااااف بهترین بازی جام جهانی ۲۰۲۶ رو دیدیم و یک دقیقه سکوت برای اونایکه خوابیدن و گفتن ارژانتین به راحتی صعود میکنه</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98090" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98089">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
🚨
🚨
عصام‌شوالی گزارشگر بین‌اسپورت: از مدیر شبکه میخوام هفت روز بهم استراحت بده تا این بازیو هضم کنم</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/98089" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98084">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6c46fd63d.mp4?token=o4Fw7Htu85Q1iqOwyrp9pIrMk7vyjkehYNbA0KEtbqoIEOCjXffjs-wEjP9TuGXcKtSIP8ChmIIyL9aFuM34NAeaa_j06BnQCQ5DWNDyg9KsSap8Z08MochINYGwIWOgYYAvxsFnghU1n3GgMfGpFyjH93LmfcHP_3mVdutqxO4JFF4zVgtX7ziFGaUlQxHVS1n4OssKwjyyB2PqwsA4rhts_j-gRepaC5RJ7lDEYE2pGimniOyCLKVW3F5eeGkd0CT7HAJHnrz5AjbXhTPPrXqy99nYGAHYJa1udi3pgCGzV7ktKmIFWkCndllchwTbgAHUdQgk7Ta1Hw23lTo83w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6c46fd63d.mp4?token=o4Fw7Htu85Q1iqOwyrp9pIrMk7vyjkehYNbA0KEtbqoIEOCjXffjs-wEjP9TuGXcKtSIP8ChmIIyL9aFuM34NAeaa_j06BnQCQ5DWNDyg9KsSap8Z08MochINYGwIWOgYYAvxsFnghU1n3GgMfGpFyjH93LmfcHP_3mVdutqxO4JFF4zVgtX7ziFGaUlQxHVS1n4OssKwjyyB2PqwsA4rhts_j-gRepaC5RJ7lDEYE2pGimniOyCLKVW3F5eeGkd0CT7HAJHnrz5AjbXhTPPrXqy99nYGAHYJa1udi3pgCGzV7ktKmIFWkCndllchwTbgAHUdQgk7Ta1Hw23lTo83w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل رومرو به کیپ‌ورد با پاس گل لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/98084" target="_blank">📅 04:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کیپ‌ورد خیمه زدهههههه
😐</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/98082" target="_blank">📅 04:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98080">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/98080" target="_blank">📅 04:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98079">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmDx6itbVz_0uFxPfSl-Vg1oZYjF1FmDOZ6RghuCF28HTYAYPraPvy9qkuEgJDR8T0Cr_JZBkrCmz4U4-qFBtwo0QGLrRV6BYcBX3ESZw-tTVHVd-4BGiA-r8nirpbCttQ-ss0gk3pZ3PjzO3igkJGd9uBep50XxwdtdTPFpixSFC7as33VgN0dcy_-zNf_B8BA6PU9nVvSAkdvHrhqQAwXx7IkLNgLlSyIhovaTbb4Hjd62tsr4abifYYIrq0JJ_urFxiYf9b36b6eB7V76KkYwMV6L8-zhm97YKe93AS9gRRxmxhuY1HqrgY1La7nCXMIytEpxE2TeDlKtQVTkMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
• لیونل مسی، اسطوره فوتبال، با ثبت آمار جدید، عنوان "بازیکن با بیشترین پاس گل در تاریخ جام جهانی" را به دست آورد و از مارادونا پیشی گرفت.  • اسطوره فوتبال، 9 پاس گل ثبت کرده است.
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
👑
👑
👑
👑
👑
👑
👑
👑
👑
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98079" target="_blank">📅 04:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98078">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مارتینزززززز چی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98078" target="_blank">📅 04:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98075">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF0YXcuwueKYhIt4uEvKmxwM4mYc9cOXHheUEEoIASixzTtxWumnpvRMhA4VgYTF1fSrEveaqZ9zVGKDhJe7ykD5Mo73xu1B3wsEy2GwlmFBJLMK6eNld9pUCe2X2YYgf0LGaaRrIprEJYlzuROEF8cm_OL75_Lighv6dGxbom1zcVQWxeQqYwP4v7h6G5qW2BBjWtMtg8By9GTff8ZnllDui7HYSBdvudRzdhy2q8I4PRcwlmznhXu8BaZ0L45rseknLXz4HPDzSFAMPqMqRMWfJQKlD7tcG_V5L0bSa-nWhLkUCmfN4iXpyUCAYo55bDPiBfVd1LfZ_-TitlD0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
• لیونل مسی، اسطوره فوتبال، با ثبت آمار جدید، عنوان "بازیکن با بیشترین پاس گل در تاریخ جام جهانی" را به دست آورد و از مارادونا پیشی گرفت.
• اسطوره فوتبال، 9 پاس گل ثبت کرده است.
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
👑
👑
👑
👑
👑
👑
👑
👑
👑
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98075" target="_blank">📅 04:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98074">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اسکالونی داشت گریه میکرد
😐
😐
😐
😂</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/98074" target="_blank">📅 04:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98073">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پاس‌گل از اسطوووووووره
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/98073" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98071">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سوووووووم آرژانتینننننننننننن</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98071" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98070">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رومرو زد
🔥
🔥</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/98070" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98069">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگگلگلگلگلگلگلگلگلگلگلگللل</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98069" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98067">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رومرروووووووو
🔥
🔥
🔥
🔥
🔥
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/98067" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98066">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جاننننننننننن</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/98066" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/98064" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e6e57be9.mp4?token=q7HT9gwgsmdeKGDh7eTOakWIFnzxkE97TaWQl4E02pbBmixS6ucVvN-6rH4QdeoaEedHEk4L_pkRgsoFVn8rvA923sk0ifEIcmWyP62hlS5ptMnfSJh_e_aJ7tI7rftaxF-S0E0-UakgYqw5FVI27kc1d52lz1IR4Evn2vO4eqwN2wy0tMpqKQylO50zPrTrsIaf1XggVkPpk_JP0Xy1cnqzwhmzgEIkRf32FeITX0JCsoTdcJ03Ij1yWbh2VHZ9Tj6TRuTAJspDeXM3mMZJ1RYr23CMi75MP8S-ddNhsq-IjdjH4ZumoNMkZvykZO9MsPYESKrLOCFn81UvymW7SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e6e57be9.mp4?token=q7HT9gwgsmdeKGDh7eTOakWIFnzxkE97TaWQl4E02pbBmixS6ucVvN-6rH4QdeoaEedHEk4L_pkRgsoFVn8rvA923sk0ifEIcmWyP62hlS5ptMnfSJh_e_aJ7tI7rftaxF-S0E0-UakgYqw5FVI27kc1d52lz1IR4Evn2vO4eqwN2wy0tMpqKQylO50zPrTrsIaf1XggVkPpk_JP0Xy1cnqzwhmzgEIkRf32FeITX0JCsoTdcJ03Ij1yWbh2VHZ9Tj6TRuTAJspDeXM3mMZJ1RYr23CMi75MP8S-ddNhsq-IjdjH4ZumoNMkZvykZO9MsPYESKrLOCFn81UvymW7SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش اسپید لاشی به سوپر گل کیپ‌ورد خداست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98063" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_C99qTf-VEtM2GmzJaesbOps2RfRatOdKB71wk9Sn87vQMcRqLC1pN1x5gdA7_efAl6kgK_g2IONGm2OL96Bdfi9nWOV__a6NX8ce9p_6oFmHOtYK4CHd3adh9sPt1yfGgeZ2_qRhCqyIYggUw0CQeXKWig3_YlUrQCvmQ12FGdARCzr7P5eSNlmiGMF-_MgB_c9i1VSc51Yz5TMvMtoZOqMRdC0ocHe7oKGedtM2xo-tWHxcT_klqwItET5GQMUPdh4oiadIxwHybrkaKRuOoCFm7xy1RE80fv3kAYXZ5APPWheSc8YsAS8GsPgd2uxUTe7j7HP48syMvlBKnexw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرررررررررررررررح</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/98062" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98056">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سرمربی کیپ‌ورد رو بیاریم جای قلعه‌نویی</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98056" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98055">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اینجوری که بازیکنای کیپ‌ورد جلو آرژانتین پاسکاری میکنن تو خود بازی فیفا هم نمیشه
😐</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/98055" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98054">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">وقت اضافه اول تموم</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/98054" target="_blank">📅 03:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98048">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/182721537d.mp4?token=Y7pKp-GY06xtZJmikRhd3LYLz9iN5KkFhoNonaLzY7xGXjwCpOpzSuMvTS4Ysp01LVMqacHJY8xQTaeOz_6-Ru14UGSNwAPy568qmvveFl_I2r-2P5oyFZP-lZ12mgV3Rk2o19zx8nBW1gxySGb49kSSN-edWO-92Bs4R2Owr-v27QUZ8iRi9iYU_8UitHUql0Yktwrhs-Cs14nOil1Pxx7pKKiumFsR4EGrJzgVzXRh5sNgYHa5kklEVinigAPoVF_pQAsFMtZESWq6aFyZgtRt6ZkmxRxwyDe7aixlUbRvlEJNxZbRaTt9fABleiYw1sQvTTkWkLIM0vYKyKwQDXMckZfQWpJneS-ePzughH6eyBGi4GjEgcs-K8jjoJ-7B4onfyeT_VKAKC81HjxWchJB8lY9BWE_PJ496wU3h3gPDQoOIj90LHc9LsUy4hd9qwa2t_eMXDnMxAj0bO8WyV8UU363BqBveo90G8xTp9sNRWbtZsYyB8z_nfXSM40eSiwp6xU_0PK85ZAQUeE5c0YhX-xPkFk3o-ccojYrtij3mrWQjMoNL_D_bbccbpOVmec02-UtpB42ExhRUY3rlgxYxI6KWfqUJNwxct_I4c8L4HA2A146GIgHmTyZsq510b8s_2YWUCsaSTAyZAhEM2bWAl7dL8c1HRbnxeGsg0E" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/182721537d.mp4?token=Y7pKp-GY06xtZJmikRhd3LYLz9iN5KkFhoNonaLzY7xGXjwCpOpzSuMvTS4Ysp01LVMqacHJY8xQTaeOz_6-Ru14UGSNwAPy568qmvveFl_I2r-2P5oyFZP-lZ12mgV3Rk2o19zx8nBW1gxySGb49kSSN-edWO-92Bs4R2Owr-v27QUZ8iRi9iYU_8UitHUql0Yktwrhs-Cs14nOil1Pxx7pKKiumFsR4EGrJzgVzXRh5sNgYHa5kklEVinigAPoVF_pQAsFMtZESWq6aFyZgtRt6ZkmxRxwyDe7aixlUbRvlEJNxZbRaTt9fABleiYw1sQvTTkWkLIM0vYKyKwQDXMckZfQWpJneS-ePzughH6eyBGi4GjEgcs-K8jjoJ-7B4onfyeT_VKAKC81HjxWchJB8lY9BWE_PJ496wU3h3gPDQoOIj90LHc9LsUy4hd9qwa2t_eMXDnMxAj0bO8WyV8UU363BqBveo90G8xTp9sNRWbtZsYyB8z_nfXSM40eSiwp6xU_0PK85ZAQUeE5c0YhX-xPkFk3o-ccojYrtij3mrWQjMoNL_D_bbccbpOVmec02-UtpB42ExhRUY3rlgxYxI6KWfqUJNwxct_I4c8L4HA2A146GIgHmTyZsq510b8s_2YWUCsaSTAyZAhEM2bWAl7dL8c1HRbnxeGsg0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
سوپرگل استثنایی کیپ‌ورد به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/98048" target="_blank">📅 03:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98042">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پشماش ریخته از گل خودش</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98042" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98041">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">چه گلی زدن
😐</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/98041" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98040">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/98040" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98039">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وااای</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/98039" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98038">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کیپ ورد زد پشمام
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98038" target="_blank">📅 03:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98036">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/98036" target="_blank">📅 03:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98034">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nI_NdazkLMTI8UHXO9SIcZ9-4l43monWxLaNTcIo2Gz_1tleKwY-YB0p570VeT43XGVyY3Zc8rShw6jnZvxJD91_iIWqSQrZw4HxVY1V-7QDT5m0z7VN_y53YBtCy9k004qwuNYb7uTx_EVekJ4K_whPSlnwhOSAzJhzRGKS3za311aFbSYdrzFA9u0Gb5ipG5H0-fivjkMLckTX2OXrE078VvWf5YLNnacx4wU2Dv9lNuRskjHC5JNWvX-7oB-g4-xL80cmyho-keEf_auMp8hGT1fIFMkiv2rssXJfjUwUA42lybTpvQFl5aMZsOSDN1moRTioxwSQjJe9m0wa8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jA5Dt4m0zwfEsA6PAe5tXRIbqoMK0tPbnR9l_8yA9XOEvn-Kg9FIaTJZWjl647rvEjg2vuObz-4dRZjUY0v9G9KaOsD-zGIzZLqvDJttdPbR6PpYH4FbLQpwNCHL32KdoqMDxeyF3E8MdJxHqxAFnSXaKachwJIL3RVHvSJzrfbZduPttZgELjdzdbIPKo0CfZLPKYbtWshunDMEeJhFjhFX6Gwo9L1OrsOc_mJiNMtuOQFYz2rBr0g9fBkQZQKqMCo7imUdvqqu0xkZTS78UKV31TFl1P09PIzQ8kxeywAMXGQN4W1Z7uy98x3QeC-ufiGRv_IIvTD3qxKRq3Ry1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇴
🇬🇭
ترکیب رسمی کلمبیا
⚽️
غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98034" target="_blank">📅 03:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98033">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بازم خطری شدن</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/98033" target="_blank">📅 03:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98032">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/78229061b8.mp4?token=HrYyAxU4K79-J_BYV9lfz20EhDqtJ0yNVw-Vrnb0GheF6cYhCbDPNrsd5VAeVg5xgDizw0FhgiwQP-xPHubmlgitBTOFI_uIcIHY7nqg9suE3C_Fbf9AV-BozTTYeTk9LJiUgWhMc8iWPT36xMzO173nViAoISkU54VwCp4u6Uj3do0Xj9-1DoCYkeBPFae9yxWoTnvWHHpkpUQko-T92AGUhq5ZzbZmwzM1XPerGyl-8P3MxDQV-87Q3VmmpxnXm3Y5HIifaSGQEQWIAd8L-yiY2Z96mK7MBjVkx9koREkIn8e6s0OUvg8sCfba3wjUSsN-mGCCBGjQNzJYd_JCbQivx0N-mUvqCy7hGKgK39sWi4eN1i9nQXvDNuyzKAPXBy3ySgCLLJ6Hv-xSFb-oMBuAMl6AGn8Pf0LyAqnXeAn92u9vSjYeiZEQV6ZOaQdrzvKDBhhyOqEoe33MsybntGJhcEznNnaIu3kLdJ4QePZlsiBf8H5VIcBdl5HOvVglwu5VoJOAWQEcsncR4yNWcvWETat-NXMual_y4fdf9S2agNC_4URqqkvad6TubGhN1eXqImRWWtwIYfTUU4iWLIUP-HWLFTrJBddcCsh-HXZdn8zsqVcf8LVkhJ98GlkkIQ0si0vGQgCihTx31osukT5r-KnHpXg2XVicbD9BleE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/78229061b8.mp4?token=HrYyAxU4K79-J_BYV9lfz20EhDqtJ0yNVw-Vrnb0GheF6cYhCbDPNrsd5VAeVg5xgDizw0FhgiwQP-xPHubmlgitBTOFI_uIcIHY7nqg9suE3C_Fbf9AV-BozTTYeTk9LJiUgWhMc8iWPT36xMzO173nViAoISkU54VwCp4u6Uj3do0Xj9-1DoCYkeBPFae9yxWoTnvWHHpkpUQko-T92AGUhq5ZzbZmwzM1XPerGyl-8P3MxDQV-87Q3VmmpxnXm3Y5HIifaSGQEQWIAd8L-yiY2Z96mK7MBjVkx9koREkIn8e6s0OUvg8sCfba3wjUSsN-mGCCBGjQNzJYd_JCbQivx0N-mUvqCy7hGKgK39sWi4eN1i9nQXvDNuyzKAPXBy3ySgCLLJ6Hv-xSFb-oMBuAMl6AGn8Pf0LyAqnXeAn92u9vSjYeiZEQV6ZOaQdrzvKDBhhyOqEoe33MsybntGJhcEznNnaIu3kLdJ4QePZlsiBf8H5VIcBdl5HOvVglwu5VoJOAWQEcsncR4yNWcvWETat-NXMual_y4fdf9S2agNC_4URqqkvad6TubGhN1eXqImRWWtwIYfTUU4iWLIUP-HWLFTrJBddcCsh-HXZdn8zsqVcf8LVkhJ98GlkkIQ0si0vGQgCihTx31osukT5r-KnHpXg2XVicbD9BleE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
گل‌دوم آرژانتین توسط لیساندرو مارتینز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/98032" target="_blank">📅 03:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98031">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گگگگگگگل صحیحههههههه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/98031" target="_blank">📅 03:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98030">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvZeQnjy0oPahidpIeH4jjbM6BApOpabm8_2_gM1xG6u6bHQFhNjQHwmRVmYMcZB42q7WKAnOrQzRo8GmiG_uhsJ9LNonmZ9TLtOwXTZDb3nGt-JsyuIHX5kMvUmk42fNElHIgOuSxmkwGJywHc00VUcMjU8FYL06D09L67BiDxtvTbPw8NfpxA5Um6Q_PcUJsbJQFFsY3STT1HgFiodXNrIJ8P9eTUGQuYHF3a5XxrmzFyBqdlMszdCjICLHRA4TUpPVVrhv9GRI7uNd7d6_rPxJk1b2aUTxApTOlmNXSA485bslkmbLc0I-ub58NUfehvHmtHkCh63_CtN-BrQ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حروم زاده فالوورتو گرفتی حالا صیکتو بزن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/98030" target="_blank">📅 03:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98029">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کس مادر جادوگرررررررر غنایییبیبییییی
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/98029" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98028">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">لیساندرووووووووو ویزینا میزینا نگاییییییددددددددددد</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/98028" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98027">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">لیساندرو مارتینزززززز
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/98027" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98026">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الللللهههههه اکبرررررر</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98026" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98025">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گگگگلگلگلگگلگلگلگلگلگلگلگلگلگلگللگل</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/98025" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98024">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIMw09l-I5OJaMQ5AZwrmQXjsVAXAIBDoY8iEJX_aMy73g8pfzFNLMaXN0IbqZXoRM-oGRi88w6IeKGqlmW_Tv7eWNZ7EWSN5ZbR0jOi9hjUpFAtZLJzY3jopHOuJ0LSHSDTY0BLjP0ixss-SZC3d5Z1tqC76auw3s2MSJGrYfrOq_XmqrQpouIV3F1Pj5hZPZSvThsqj4Ppi8ZxAuDopWi7OOCgV1S4zP5qkla7Tzgo9jHUKveWvfgxD5AFepWd5dGVH86w1mCky_1ELQ0iRWaiDdnj84WFGB8cSbq0vta1MyzT9fpZLLsOE1wN1A4Jq09LOsJDqm-4Mt4-4-2n3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همینجوری داره فالووراش میره بالا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/98024" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98023">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلگلگگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/98023" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98022">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گللللللللللللل</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/98022" target="_blank">📅 03:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98021">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آغاز نیمه‌اول وقت اضافه</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/98021" target="_blank">📅 03:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98020">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq45OuwGj0j_niyvxKxwcEVejaKbqrtTuef7RBOyp-BLkmbSW_EkuxqZblYKx0UbVFaJaDjrk2LmuG_J5Ol0Ug3UX1PWIHXPejbrgSYHU13iZKhAMMzVjpc5mhizM5QylKjiVarCP_uPtSCXS8akVvxQc1smtoPN-hAZmnP4SQoio0MicKtovkh4zTiFtntw5SBaWVpMdjZNCA827JJxFx3QcpjL0SGkWBYrOcuDIW3Nivh4jfGHtDxYD1FuY2wTfhHxIq3AHVhg-7P5Si52vs9A7YO_BJl8jS0NapYuTi4QKHddeZKAqhBOFszLe8_NbUUSsDoPcvnEr3348Dvwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
نمره گلر کیپ‌ورد در بازی
😐</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/98020" target="_blank">📅 03:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98019">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اسکالونی رو نیمکت ریده به خودش</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/98019" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98018">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
😐
پایان بازی در وقت قانونی</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98018" target="_blank">📅 03:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98017">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">یک دقیقه مونده</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/98017" target="_blank">📅 03:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98016">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گلر کیپ ورد چی گرفتتتتتتت
😐
😐
😐</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/98016" target="_blank">📅 03:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98015">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/98015" target="_blank">📅 03:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98014">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vh7sFPTczOoshM8Ab2v4XuE9raa1gW6owugMJE5J9D1V-33d8Q-gsaZLH4R8zMCCigR0DKRHVw1S9M7wd_uaKabdu7eJ43GxcEtCQsM9TgVvWjPRIJ2FLG6TEypNEyMYxkdiJk1IE4qvzO6ZpaFHNglSkCHUZTNO6pcUzhYDjhieIxIToDHZvqkAFqLZRqWR71bcnN-TiUMGMGe8JGvFLGwJtpo6UdqAyiq1ReqK-ZckR_bC44OI-shS-P4eWRkF3Wbz3sxM4ijPVR-5u-nuOXya2TUV1-88n0DMZJZzQrlZXXUiOw_rmn1DGHbjMmgz4FeBUlj3l9j59HXPcyVMMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکالونی پشماش از وضعیت آرژانتین ریخته
😐</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/98014" target="_blank">📅 03:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98012">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
جادوگر غنایی لایو گذاشته میگه کار مسی امشب تمومه و حذف میشن
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/98012" target="_blank">📅 03:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98011">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
جادوگر غنایی لایو گذاشته میگه کار مسی امشب تمومه و حذف میشن
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98011" target="_blank">📅 03:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98010">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
جادوگر غنایی لایو گذاشته میگه کار مسی امشب تمومه و حذف میشن
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/98010" target="_blank">📅 03:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98009">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oh6KWjsd9dN8qZjiCFg8mRNPiqBfvY5OYP1CAxsmrWnBmt6hT1h7pISWKbr4cKrhVQaeFc_BfwSYlw-Afe18WY9Bk6X1lgxvb_9SXOAULvJHy0zuBBrXOV5UBpJBCx9IH7I5twZGqC2YeXlDTJtCX-CrQHD34SFTaXdlM8Q7E8UFnC2KRE-FynD4R53xPfcAqCK6gEj1Ix3UMMp5V-ynePFp5cd0p_dj5Tohv3ZU9Kkb8kWihDpFBRy-c8O0Qnt74oU1VCunBGmpCM6cA_35hF42hMLYLZqdeJP9BPXcCDH5Rp4EtSbmlk9h48nORY2vOF-0QSRjd_T9dqcqdc03fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گللل کیپ‌ورد به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/98009" target="_blank">📅 03:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98008">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab8afcddb9.mp4?token=PG0jfoNNXUEKRN2mCfae0PqBzS1Q6qIcEPPNMjEMdcM4T47BRgXaOJxyo7JHPpybir-NUcG4Gxr3lBDZQhyhWOtWgjJLEGoyQ99SWTtiBQKvtLlY0vmfaZ1VYjrI7Obf9rfuo_YpMhHZF_tgRWy6nNxGZyMjeDTUkizhNPAitjY6lMFhneGJuz-Kpzeavlhuh6dsC1aR53-gbFuGMKNKEaSmaGph1HSVGIld-olLMsFzAXAil-AOEAZERlX8AK_8nLhVS5EFKXaDXmJmiSopMcSIJay34MmX0MrplIEkb5Oe9C4iNY43okBmDngPTU2_cI8sjGNFCSMWUCQtGQumfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab8afcddb9.mp4?token=PG0jfoNNXUEKRN2mCfae0PqBzS1Q6qIcEPPNMjEMdcM4T47BRgXaOJxyo7JHPpybir-NUcG4Gxr3lBDZQhyhWOtWgjJLEGoyQ99SWTtiBQKvtLlY0vmfaZ1VYjrI7Obf9rfuo_YpMhHZF_tgRWy6nNxGZyMjeDTUkizhNPAitjY6lMFhneGJuz-Kpzeavlhuh6dsC1aR53-gbFuGMKNKEaSmaGph1HSVGIld-olLMsFzAXAil-AOEAZERlX8AK_8nLhVS5EFKXaDXmJmiSopMcSIJay34MmX0MrplIEkb5Oe9C4iNY43okBmDngPTU2_cI8sjGNFCSMWUCQtGQumfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گللل کیپ‌ورد به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/98008" target="_blank">📅 02:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98007">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmS0qThwCYyAdP0gcg8c2CMHf4P4-zC8cvVrbGEJIbFYGntIG6ntFuVo8nDH6-TxfJUNkQciHwKP552cj5b1AEfE7ug2-QFhpDlDr8Vjix-oQLWA2QiGz5Zi2CZRDkc7w2_IPa5wf9DeKsyO_-jfj9OdWacB1T3n6-JToFDo2Xy842qV-TcFlP3vwfxcE8jyFm9mNXptj3MoxbMH4Tl9q8zkSvzy4SpptMRncDvK3PHY6oQCl_KhFzgDCmIAs4OpgKFkkr2kzSVrboC13Yq6qaMvecTvfmtUIZCBTkDgUsc_EnzZQVtBVcTK1WY0aC06JLk1QhZ_7PEWTc7sgPsd8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت مسی بعد گل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/98007" target="_blank">📅 02:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98006">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">جادوگر غنا کامبک زد.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/98006" target="_blank">📅 02:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98005">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شل کردن چرا یهو
😐</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98005" target="_blank">📅 02:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98004">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کیپ ورد گلللللللللل</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/98004" target="_blank">📅 02:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98003">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شروع نیمه دوم بازی
🔥</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/98003" target="_blank">📅 02:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98002">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrRyrJngwQRC2ioHguEuN6E7gqqyDA1_n9gR8A1IJ0N7ig92KHfsLheFgzjwGCpBV76hkw6VRmH14CnUPwoYFaGTGAaJbEXE53g9Jdc8OOt4Ch21y0otNwzyukLuMiwD6LzF7Sh8iHibwBg-W9L4mx0Q3sXYaHuK42WGsV1T4f13vPd2U4Vc5Wf4xfZagJeQEUVB3WSDSXk3k0_ewOQL4N9d-7VmzSOheFnpQ_TH1NoijmhiNHIT-ymUCAkY7aDZrSQB324qHtYUSBqto62hFzubwOs0kdcDoKZBhTf96gOTWG2v2atiOiE339drZQOYnxgH8xAGJLjgpaNlRsJkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🏆
| لیونل مسی، اولین بازیکنی در تاریخ شد که در تمام مراحل جام جهانی گلزنی کرده است:
‏مرحله گروهی
‏مرحله یک‌شانزدهم نهایی
‏مرحله یک‌هشتم نهایی
‏مرحله یک‌چهارم نهایی
‏مرحله نیمه‌نهایی
‏مرحله فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/98002" target="_blank">📅 02:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98001">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GR9YbySOYOoRx0s-gvYZWumtMJTI8bg7tg_Gc1UCD_g-XYOEMCykEdBCToU346sToBzT07ROA3KwxOAcosM3a0VtvBqpE8nXNbk8KFFULynPZISPcQbkd17jODKW3r6qDu4Y_hCdjN_CNrJufA4UxthbltknOj4yO5uXi01Eo9hnyy9kJvh6U4GBUaUYHLftI4u-dTEeX-kM6JC1Ga87QYbG2GPM1mJfVfdxuoMU5oef16NGRn5cXaQUrsvDkUQHSxXoDPRN9FrwlY-xpUhEQm0l-4JA2oZXF-HhOvHCOC3OTi4eQX5CNv_AN_8nNPqM1X9bvgDeKjx04LSU-c8rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا جناب مسی آرایشگر حلال خوری داره
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98001" target="_blank">📅 02:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98000">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojpV1H_ul8kefekpeD60_uFB891X6BA66XLPUeCxT3c5SbxWFziA9rSnITHp_qaJ7mhsht1ISt5fhBVTWn3ZaeVsB9LIhI64cuAeTbMHZ6EaJtp4ugfAhqii99ZNqwqUbIHN9vuf2lmMxu9dy79IeYWppe7ayPwHVmrT78m1jhBw8e7ttLR7aqXrmjojVi6y8ZrQhYom1M0iKdUh_lI27tfhdKyL_icO_CIxJR_9-PX--ShyEYzgJwvAeTixpMmBC42YWfiqNo5WAIy027jyqQvQCpOUzyRjKCllNTpv0L4MBUtkoJC_sjiE-aJoSNpGZxFbVvK3XzgNDeMEO8p12w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🏆
| بیشترین مشارکت در گلزنی در تاریخ جام‌جهانی:
‏
🔴
لیونل مسی: 28 گل و پاس گل
🔴
کیلیان امباپه: 22 مشارکت در گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/98000" target="_blank">📅 02:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97999">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پایان نیمه اول بازی</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/97999" target="_blank">📅 02:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97998">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QUbd9P1HXhgjI3UGVYnEvJrvQDNLG68EF_JLRRyG7w4MWoxqIiWoijweanxp0QKCA_WNsf7M_MKW-FTVyG438IuRARy0xgKZ4yfvQfVOpUmKic-CQapuBvMto_WgwNiUTAxgG-ZaQ7GVgRVL07HawrtG3z77VPPs84KtslWeeI9dQPNdQ8IvysV_DN3yN77cdXuUC862jBHojqG7z8GPYbOv3chjRQDqatcAr3l9NLtE-aoqWj3gws-b-MKgFqvuZRrOE_wxEyFwlFAy7va5SHi-x3LeqC5WS7P98bbv6YN3XAj8IPfbdhnV_bXJ11iBgy1Bi77aKqSYYz2RgbuM-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97998" target="_blank">📅 02:17 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
