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
<img src="https://cdn4.telesco.pe/file/AJ2XhDDThWmJuBJd-frbLfzyTFzGQY7w06R3rlkrgt5o1HFceCdeHzk_t1WEqU7VDYhMvDg2dk6iaq5McxQd0_fnWm-XpnLFLznzm6Ctlo9t3-FGUxNlFvdxHBaQ-IV_GZHvK27W0W7OLQ7bnyp3lY0W7HF5aRbNcbOD5YQNAv1gwq5jY5yjg1v5hjvf5HbmVRHiiJrGXh9E7T3Zp5KfINkFnez_J1zAz5CqaSQamhJ-dqFaOro5U9Q7vjwavNJAzF2isDttZemMgjaUJxndVByGkVVmyAS3Gvp5kKbd-3RbvaG27KXTJj69AllDNcnhigZGDf5Fip1021vRq7CSIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 269K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
<hr>

<div class="tg-post" id="msg-84829">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اینترنت پر سرعت اپراتور های مملکت قراره افزایش ۴۰ درصدی بخورن
تعرفه های اینترنت فیبر مخابرات هم کم کم دارن افزایش میخورن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/funhiphop/84829" target="_blank">📅 16:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84828">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c83uYHETy_ssVXkDj0IqxnoRA660ZfvwXRZ7aqfNxBmzOhvk2WWWWKmQWUfaxIl-IaSDx5CbKgaaySNngJ1oMnpm9f2TUbqTCjUpDDrqeGiYIf41_ScVWfKW2tW9pBT5EScmKkfGgMuOIDQIP1VhZPu7nwlx-SiFvdzEEl09qG3C95EIdQ9FPNMqv2XDu7B51j7_FY2Qcb0Bt4o-91ncZicRsKXh9pwNR8oZmEncrwzvFLfz2k9-KOJAeUFkTm6299pJPPqC-R7qnfpPa5DXlwhwwqwVTg7tTNX7CT11FCaXtysoiIJe8RLToyL2qz-5GWscpF-KQ_Q1YIVIi3qNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یه پست گذاشته خطاب به لمینا بازیکن گالاتاسرای و گفته، یعنی الان دیگه منو می‌شناسه؟  رافینیا و فرمین کامنت گذاشتن فکر کنم دیگه شناخته   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/funhiphop/84828" target="_blank">📅 16:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84827">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujFGuAFn80bzjMLB-HnNNG9Tsn-V7j-Zzfjhsi6k1Ch4ZxsObv9IKxGrjmG3-jQGyJ7zt4eHYRdAfprDw7FjP0MMyYa0zospWAPy2hYTN5NQrF4Te-kAsQxhLSof9u2iFNQaWm7-t7B1JimFIdjuCl6Rt4aNzXk_2DwE9LiiA45iiam_xfhrBwhY-Zmp_RTcUiMWToAH2WHgY7k0o4xJ7UALo5gleQtIC8dDOI7ghkePSBXmuR1YaAUHB18wNVQ8RNvhfswEr_A26GW9MW2wGc2-gCcenD5jPDOnJ9hO6NeIJWIxMrU_LbI-T1R5Deu28bbIBq_QY5729xffaV3w5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یه پست گذاشته خطاب به لمینا بازیکن گالاتاسرای و گفته، یعنی الان دیگه منو می‌شناسه؟
رافینیا و فرمین کامنت گذاشتن فکر کنم دیگه شناخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/funhiphop/84827" target="_blank">📅 16:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84826">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کیم جونگ اون رهبر کره شمالی خودکشی کردن رو ممنوع کرده و گفته هرکی تلاش کنه خودشو بکشه و زنده بمونه، اعدام می‌شه.
ممنون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/funhiphop/84826" target="_blank">📅 15:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84825">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">عمان:
مذاکرات با ایران درباره تنگه هرمز به پایان رسیده است
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/funhiphop/84825" target="_blank">📅 15:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84824">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPPKaiD94wlR3flCm0EaUwPuOl9H-m75z3c00CIu0DKfiRcqJ_gw93zL0zOSvYjUzgsnENWOtTfbyi2TLqSe02Z-MjkPBjqjrD5lkwRmiDIISP4WF2I3PthLCQMQbfy68GxIA-B8kaArjyuSUcNzoC4EnrpIjZk7Te80aHqtlTjWmB8lp2HT7BKhkm4Iyxc8yMz2fbNB0KwrUsnZd10yY8ExrVYCQQYYJKIuIvXSJywGg0tUEV5ghSVq8XLRrUcU_pyqmIvXurzYXMJQlV31n0gt9LKXiVDe9OgThsPRu4RJyyBjyL7VH0Jn3zvpfbfSba5gCEoxxKzpX8OYJSvlqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه اشباع شدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/84824" target="_blank">📅 13:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84823">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سلام فریب جان خوبی چخبرا  ذخیره کردی؟
سیریک صدای انفجار اومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/84823" target="_blank">📅 11:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84822">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(ChamanDarKhak)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK0lXfi2QyPnaVztObC8dXzAd7C-9FLkfpOHGj8296cGvUSZqx0ETwH3iO8cmaTuAoOYQy4yvGxxw-lQQhUq44p9oogZ4Jm1fWWSpEkgrFjdUInhyjEwvC4CVekisH5KkSELF1BQBq2QOP6VxkvK-Ujajbtp0tjZslaOIW10NrquVEF3mx6EgCsDUpyobDPtkduN6FO_judKZ9StIN2NqUf0lLspSaeedCEjXxIDR97GxgJE4proiNbDCBDU6h6lJ15CWBLnfPPckFfCl0CYycgE6ygz3R3bkrceru4ii5A0cMEvf78syGCl_fSjIdmUvTeoe__D1elKcVl7Jk9M7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NEWS
🗞
🔴
فیفتی سنت
به یک خبرنگار گفته که
Eminem
به دلیل اینکه داره رو آلبوم جدیدش کار میکنه نتونسته در ساندترک فیلم جدیدش حضور پیدا کنه، حضور خود
50Cent
در آلبوم
Eminem
هم قطعیه
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/84822" target="_blank">📅 10:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84821">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVCot7eDrTF5b1dh8ce3gLI1VMTvto5YZfyfe7vBsdRRdZMdkn-WFvs2p6_eo557JAEeK8xqChe8XH55QrEQdyajBSbS9Bti7VBnE5UpQvB4SL9v1aXreEJxiEVxWw5wodzhWgkQKdk2OC9Vhl7ikyH01KhEGsmsh82RA3432MKiCi7UYWwfi1gG_5eP-6mV3RJzeB66qTO---4-WfzFBK5IrDwlHz9JHmsumz1C_2TpI6cElTY2_rNZMjBmD6nzPrHHYyfmYlaE_Vtz6Gr4y3JwbX59TY7mo916KJNrclckr1NLNw8dForhGmt-u9E02nH3ABMDSopNsRmfL9bSHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرونده قتل توپاک بعد از ۳۰ سال بالاخره حل شد و قاتلش به ۴۰سال حبس محکوم شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84821" target="_blank">📅 10:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84820">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWiqAbicY-GCFxc2mK0MsObFo7sRJKS2kx7-Y0Br4C8xgqr9bp_G6VGJqKtzvxXTgGRtmmT0ByoaCZ3hzFpYj4z01uS30VP_lYxcebpYXdsWdqHXhGVD1WVk1B8iXVg4T0cE3J3sgG9kmVS9N-bYOI7Y9kRxffkcFXAnOlsVKLhRjNqRoy0mQ9KzM-jhVtfjvi4D4o27yRaDyCecSt4L1YmDAFcqnfj_iTZ0xsrkCpDquLBhbh_r2BQzTO86l7jqtfdnETToj-67S0sMN2uhR9gr22hyAedfbUs-JxL3-TYM0oeOW_egSL3WjevmV6orjdLCKrmIW-DpKoUP0h2_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
منچستر سیتی  - پاری سن ژرمن
🌎
ساعت ۲۲:۳۰
⚽️
آ اس رم  - رئال مادرید
🌎
ساعت ۲۲:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r22
🔗
https://leworkcihsa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84820" target="_blank">📅 10:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84819">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j17dW6qklu-W5Ih7ed6BZn8w_y6Yni4qBhSkGDLX2cs_vbB_9MDCtgF5cDGoCp5YK_t6keUUuC6sFB2d5OReRxBrJf2bTN1gYojyqiv2zAasozmUpF83v5AwmeI54lKxaFQVjw0Xx8k10vHQSDfS3SlivUXKW5s_pB_rC9M6NgMO7VIQg7Qh9n2-buBIRahiKRcnijfm-jDRujQwc9-OCTUfSiS_copZHAgI6bkwZg4jJnNdbpqPW7zgIihJxJilnkFdWVuaAPKYC3HNJwTwcnJce4hEebFPaJZ9ln9Sn3nUHtg_Y20HjlJuQ5jEKpo8A7Qhyz_3d8evxOLTgB2SvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب تو استرالیا یه دختر مسلمون برای ترویج دین اسلام رفته بوده توی خیابون نماز میخونده که یه راننده ندیدتش و از روش رد شد و دخترو کشت.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84819" target="_blank">📅 09:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84818">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=bRPgtHNRna5Mfrd-VXpg-KS9_K_owzyyz4OUR1VKzPQsvG2Sgxx8nAnC3JEmAJalXgbUZhfqqmgQZsbMFBzbiEaJSqV0JCtqaCx_UHlUZWKpPrd63MwBmPIMf89cUWv-cUZ4NMrYp_Vy3FIq3r4Yzopp5H-DfWjBaumVXsUVqNLtZYcW5ZCBMjHv879W8TCjYgfCEMB1Z6oQa28LxSIVo89kgYqIgcbz82m3eulbA9Q42cHJm8u3Rhbedopwx1h87bWNtcJ2PEX3wA8QPu2IFQni95_mgWWnDfGjpkXAXV98S9Ui1vF-tmS-I2wUx1VvPoD9qoKTiVKh4u1xSPmS_wFzp0SsBBrMVKL3RsFpqsBiZS4vaUfS-A8z4rL4ZjnJUQg3ks_VfC7FHlYBieAVPZACSjjFN9GFJkyZ8cszTsugsShSxTp-VFzJH9eDl-1yIkr2m36_g98uBFiQ9cs9gWOpxY5pPrUJPl4nnCnC_-WVY2l3x6wVW0Ace5HA7WXbXl_ZWrIubyusthTMQLraUlEpyroQ9JPZa2bVOukk2V52vUgTwTY5282bZ80GHS5nb0PnSnM7qGWTyKzxwiOvmsahIKAz-0kwmFeeVRaF0yZ_8xO3qpqpaG9-qr99Fz95J-GiN5lvxvOWzl9jr9B2Tj_MwevCnuNJf_0fhAk3Q9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=bRPgtHNRna5Mfrd-VXpg-KS9_K_owzyyz4OUR1VKzPQsvG2Sgxx8nAnC3JEmAJalXgbUZhfqqmgQZsbMFBzbiEaJSqV0JCtqaCx_UHlUZWKpPrd63MwBmPIMf89cUWv-cUZ4NMrYp_Vy3FIq3r4Yzopp5H-DfWjBaumVXsUVqNLtZYcW5ZCBMjHv879W8TCjYgfCEMB1Z6oQa28LxSIVo89kgYqIgcbz82m3eulbA9Q42cHJm8u3Rhbedopwx1h87bWNtcJ2PEX3wA8QPu2IFQni95_mgWWnDfGjpkXAXV98S9Ui1vF-tmS-I2wUx1VvPoD9qoKTiVKh4u1xSPmS_wFzp0SsBBrMVKL3RsFpqsBiZS4vaUfS-A8z4rL4ZjnJUQg3ks_VfC7FHlYBieAVPZACSjjFN9GFJkyZ8cszTsugsShSxTp-VFzJH9eDl-1yIkr2m36_g98uBFiQ9cs9gWOpxY5pPrUJPl4nnCnC_-WVY2l3x6wVW0Ace5HA7WXbXl_ZWrIubyusthTMQLraUlEpyroQ9JPZa2bVOukk2V52vUgTwTY5282bZ80GHS5nb0PnSnM7qGWTyKzxwiOvmsahIKAz-0kwmFeeVRaF0yZ_8xO3qpqpaG9-qr99Fz95J-GiN5lvxvOWzl9jr9B2Tj_MwevCnuNJf_0fhAk3Q9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به روح پاک پسر طبیعت قسم این دیگه صددر‌صد یعنی تعویق
ترامپ:
صبر کنید تا ببینید ما با ایران چه خواهیم کرد. ما کارهای بزرگی انجام خواهیم داد. صبر کنید تا ببینید. آنها فقط منتظر هستند.
صبر کنید تا ببینید ما با ایران چه خواهیم کرد، زیرا ما تا حدودی از این موضوع خسته شده‌ایم. می‌دانید، ما خسته شده‌ایم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84818" target="_blank">📅 05:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84817">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترک جدید سلطان بالاخره ریلیز شد و سلطان بالاخره رکورد گینس تعداد ترک ضبط شده با تلفن ثابت رو زد
🔥
🔥
🔥
🔥
YouTube  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84817" target="_blank">📅 05:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84815">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXQDCxEVXz2xgLrJHWYG8qO7-FDJp3Km1EOW9VePp4FHLNQlQ33Lytq2TB4KdNJAwZu9Ak-KMXKKB3zXb8sd5tNDul-jFhKMEn61ZUas2fNPYmcAilp-Avqj7ddmIO4zNARa6Nc-fq8kG7pwlJZlkrZ7u7tXsKjB1DLESp1Lany9WH55cGC9HcyBJ_EnAU4B89Vbq38PpvZpOU_1tC5gMHw0FFrI3-W5OtpTdvi9OU9ZXfYgbhuRawpeSZVGEehEE0tVxcv3CLDz0Aax1pwnpMsSHozDzhTnS0-FEOXgjyqL__r8d4zT5UZzGOBUCxsTP_O7h6zHZnRlQW3XXYpsxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سلطان بالاخره ریلیز شد و سلطان بالاخره رکورد گینس تعداد ترک ضبط شده با تلفن ثابت رو زد
🔥
🔥
🔥
🔥
YouTube
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84815" target="_blank">📅 05:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84814">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b06e11a2.mp4?token=CdRKu-8XVp6Uv4Is0CwtxpaIkizMx7quBxmskn8WZPJzFdtMyHKDjWNS6I3sjmmEgvK1a2ipra4s0G8kKCpp191993GiE2_R_X6FAYF8EVMvAANpiyGHqatuBfBuDg9DMU_0TiVZGyTSnrFSELQAVbsWFoUjYmXcOB3486_WnoEfwJbdha_6UgPsNVdTrkSGeLwVLO6KI5onAG9Z8ip4X2D-MpqFrxTiBHniJd_7ZhveDCSoSr4s86ZKPSGI2CmCfAHweYox4LQxmFAJvK5d_oXsQDIY4agztcABROdU3dqXtp3z-c7D6qi0tDlR3E4dYR3QQUFYCAojnumeIvSerA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b06e11a2.mp4?token=CdRKu-8XVp6Uv4Is0CwtxpaIkizMx7quBxmskn8WZPJzFdtMyHKDjWNS6I3sjmmEgvK1a2ipra4s0G8kKCpp191993GiE2_R_X6FAYF8EVMvAANpiyGHqatuBfBuDg9DMU_0TiVZGyTSnrFSELQAVbsWFoUjYmXcOB3486_WnoEfwJbdha_6UgPsNVdTrkSGeLwVLO6KI5onAG9Z8ip4X2D-MpqFrxTiBHniJd_7ZhveDCSoSr4s86ZKPSGI2CmCfAHweYox4LQxmFAJvK5d_oXsQDIY4agztcABROdU3dqXtp3z-c7D6qi0tDlR3E4dYR3QQUFYCAojnumeIvSerA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قهرمان فیزیک بن‌بست دسته‌ی مثبت 35 کیلوگرم، بعد از یه بحث بسیار پرتنش بین سه تا نورون باقی مونده‌ی مغزش، یه همچین تصمیمی گرفت.
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84814" target="_blank">📅 03:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84812">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">شمام خوان گارسیا رو میبینید یاد نویر میفتید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84812" target="_blank">📅 01:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84811">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5ukte5C8ShDcp8X4gWRCpX30aRu1gXM_Tk0YgKm6GmlDPlN1EHLledWMQo_aP-vxIX650JMDEMLqsn_Xrvz8jRKkOeBa8iGBQU1TJ-9jYV39jWpJ2LwCmPC13geZ5CADky0a8NbVower0Kgu7t0PUjq3Bz9ZXE6fNHjjuj6Fjs3BSlUlCvuX3mJxYP9DEAbQRUqdg7V8kWsSb8F4xUzbA83KX1klU5vPDvFJSjtP6ATrCVlwfF6rdNTGP8EgyCSH2owcssu6yjjEWN2HGZbTDc8Zm9CR9Vn-Vau7wxkwZpbIBDp0w8Nz96qvus1EzCOIvUU7_q0TuIN8hQr58XpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هی بگید منچستر قرمز نیست و آبیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84811" target="_blank">📅 01:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84810">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آمریکا اسرائیل و ایران، هر سه تاشون براوردشون اینه که میخوان غافلگیر شن و هر سه تاشون منتظرن اون یکی اول بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84810" target="_blank">📅 01:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84809">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65b19bec2.mp4?token=JhSWfSyMfIVmGrxvq_ZtQ7AIQo2ipUNPTYo1ZFc0nexfPaKrLI3AdLTVRn2rsSjJQ9UIsC6J5AjmtNFnWxssk9YCQ4ZWCA2sNxrYE2Feg0XpdGIVXxLtCcK-ZnkVMGT7jSNlkIT4KqpyzzjepJDu3k0rDC8araIezojQQPHi1yw2LA_eUJGsJPJ-UZ77Dz_PFu25r-3NzImkqJpjb9jd3QspH5h9NSEKL2wGMeBWS1swsrJeDdVzpM7WNjax23ih6ytrdENZQIX7PgtjwBNpGozKPwko0qakg0DT_s9mG3m_FjsEASNhjkqjNXe1qMuxGtMxqDuo9EZ3pv5828ba4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65b19bec2.mp4?token=JhSWfSyMfIVmGrxvq_ZtQ7AIQo2ipUNPTYo1ZFc0nexfPaKrLI3AdLTVRn2rsSjJQ9UIsC6J5AjmtNFnWxssk9YCQ4ZWCA2sNxrYE2Feg0XpdGIVXxLtCcK-ZnkVMGT7jSNlkIT4KqpyzzjepJDu3k0rDC8araIezojQQPHi1yw2LA_eUJGsJPJ-UZ77Dz_PFu25r-3NzImkqJpjb9jd3QspH5h9NSEKL2wGMeBWS1swsrJeDdVzpM7WNjax23ih6ytrdENZQIX7PgtjwBNpGozKPwko0qakg0DT_s9mG3m_FjsEASNhjkqjNXe1qMuxGtMxqDuo9EZ3pv5828ba4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا پر تناقضه این ویدیو، شاهی و بیگ شگی و محسن ای‌وی‌ایکس انگار از سه تا دنیای متفاوت ان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84809" target="_blank">📅 00:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84808">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بارسای هانسی فلیک واقعا بهترین تیم تاریخه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84808" target="_blank">📅 00:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84807">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یامال یه سانتر کرد توپ رفت جایی که غم نباشه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84807" target="_blank">📅 23:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84806">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTyzDeExR96PIS3saNAMaRTuC4T8hDo6RV4BaW2A6j6yUC9ncno-1Y-u1ZpWv-ISw8xMo-bLvZZ3XOLI4lhkYMX174OZKtOHs-UMaw_P190VPJj_z-F8um14D9AQIHhvPxoCtJ52gNVQzTVTwiQM5wfzMn7IDTikvUN90i06BvX6fgy2CM5mSxt6yfQgetMqdESbg0Eq_JXt3QiwSCP03jVZxSlK4RMIv08c5j37INnpnIAu4SRpiG3XITWSuql92m6cH-q9fQ6Ipijr6m9AOGvIWn6QT5O5iFr08uwNzIoRJefysB2nw4wnc3_goY-6fKBY-7PKhQSwRmdNfYVX2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپویل نکن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84806" target="_blank">📅 23:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84798">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8tJ-pLBy4Oapjxl8J_2_l6opcfbfl_zGRZyp2lbpXfl372QYbZSYlzcAkVRJ8NaoNF7HY-IV3_hwNa_DZ8jxBGJW-r3yaScGM7ZisRdBdj_-c0tzugY7rh5U0oiOguCr-7GzJvvfJAA9zxZGVd5aT6jzqlqJqnF-eXwWsW7awaQpkTSDO85CMNGJWjuonmGZ2fLx0laZGegNPaT3XAR74L6oFo-J5Jc2GubHGWFNy5BWMvX4_ncbJ7soW2C7PBhENIRuNFUMe7wPNKoxnhI-UWgmqxMf843ARq_7ijHsOovzBtaI6KUTuyy77BNWYULgyB4sKvt9qdf20DSl1pLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvr-RtfLc7MgkK3ss36oKhPze_EvP9YpRGzD4CNb6pCxIlV2vL9VckNuxuHoJJMPP_vAqNtAoUtjHxK7XmCIIG1Y0PoJyaO02LUgZ_tTTWVEjCJlNRz_rXZiyE2KF7OWkO8XqzgQjhp76F9ND_7pFzyoOvp0UhXHTeV8yWCo4DlUaGmrgERTxKKPYkrAry3486cCkcVX3ayuldV1XPMFNxJfLYS9yDuezROBr6av8r95Jy8XvaW504CHyXvlB38n3rL1P22Fsi3cs3KGXWPu-lS_EsYG56uXGmwEQ1A0XlN-WA2o22P-GIvNTypk1u_mSsprWlHS2zfkcfBV3Nb1Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی ترب دارن دم و دستگاه لوازمات جنسی مثل دیلدو و واژن مصنوعی و بات پلاگ رو میفروشن.
حتی صندلی و ابزار شکنجه ام موجوده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84798" target="_blank">📅 22:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84797">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941b0ce75a.mp4?token=Ra60EUfz-4QwfW0pPSxMZEOUtmQ0lhYEe7amij4P2-HFJf9OvOZAO-n1qHjCuBmpooXHo1UL2qwi-gqqBIkGDBoQ6Iz2vNe3y7YSF_DcfzxIekA10Q_b4r3VIWDyPOfyTX2MEszpIkXgpLcGFQnrxwWNSoB3__-t8Uy2g1phsDjaj8Tuq3C23uziR_ZpJeXn1yhz3LSPM8O3daDO53_QB9jG_dptVTP5wyJzJsGCAOm0okIGixwpfdI4K5qP5ZiT5czcQnRY8lVcros6-v-ELCu-xpo_CW_IoYclPdHyUOa2JahPh6pPJbg1xa815rS3ptn2VFCvbgml5v5y4CAIVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941b0ce75a.mp4?token=Ra60EUfz-4QwfW0pPSxMZEOUtmQ0lhYEe7amij4P2-HFJf9OvOZAO-n1qHjCuBmpooXHo1UL2qwi-gqqBIkGDBoQ6Iz2vNe3y7YSF_DcfzxIekA10Q_b4r3VIWDyPOfyTX2MEszpIkXgpLcGFQnrxwWNSoB3__-t8Uy2g1phsDjaj8Tuq3C23uziR_ZpJeXn1yhz3LSPM8O3daDO53_QB9jG_dptVTP5wyJzJsGCAOm0okIGixwpfdI4K5qP5ZiT5czcQnRY8lVcros6-v-ELCu-xpo_CW_IoYclPdHyUOa2JahPh6pPJbg1xa815rS3ptn2VFCvbgml5v5y4CAIVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین تی ام واسه خودش و دوست دخترش ۱۸ پرومکس خریده
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84797" target="_blank">📅 22:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84796">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/StxQQa5ezODoqZroeAKtK-oXcf9pQykmhgMb6vvEfPeFZcadTUVUVbR6swHPXcKz_NnjkAA1gA4qRDjtn0TO66CTVWKFndeolyaOa1dpvjmfi0-nLDm92MdxLoN7UU4wEZpZ7b21vq9pNOMXT735jv9vW3LuP7Ti-kKLMuCdBTO1exKg_Wvyw4omvUY-_or1ipbBfHPP1SekdBEJ4Uj1dZaXgOvQq4WmCIU1VEhVHTV2dizBU7IEiVdHhbPq9bL7ZzpiU1fUgAGj545Dnn9Mv3n5M3h6K8zXbz7awjXpBsJkSX1PND4IO2BHYHreBA2bkxotbVSkHdosK9D7JrhZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار همجنسگرای شهر مونشن‌گلادباخ المان با یک مرد ایرانی به اسم سیروس دبیر
ازدواج کرد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84796" target="_blank">📅 21:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84795">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">The Memory</div>
  <div class="tg-doc-extra">Creator (ft Alidanesh & Sahar)</div>
</div>
<a href="https://t.me/funhiphop/84795" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator ( Alidanesh و sahar ) بنام The Memory منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84795" target="_blank">📅 21:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84794">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp9iFEiAAIePekaxu6Z58r3hQGTuwMt_YMkOCCC2lmfsP8_K7zBg7r62vkzkfLpvlythfNLm7Pul5qfSAW3KxkYfref4HEpzX-6qMZX1kCZvdT4FgJM_iAijYeoW3V87ytlK5zW3npQ8RQLFXwBJfaSclA7ypPeS22cFE8QyvjFTuCSCHTrPp1pfnpEKuu2OgPU6uS_iktvQvdVUPaTtNnefeZT9P5zhqND_3enp3cLTWOaG-yOCNgDDMq1GvHJjGdRqM3JI_lrLsbN8mqSuQXtvFVDdR91UaKgvI2SC4SF4VJpjiSy6G_dfDZuyxHZBiMqhEQbOE_gEkcvDs5xcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator ( Alidanesh و sahar ) بنام The Memory منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84794" target="_blank">📅 21:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84793">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f013a68a.mp4?token=KURysiTUVSI9VP0Ha5QEPzmFXakd8zWpPBA0tXP__lBoMxjPKszvfZ7ovScGs0zh2Pe_usCP7NQb42i4GzGOnbf2AYRBH_D99hpe-qeEJHvaDgi4nn2xYEm2J-XAGTUEFmLyY7bd_65ckW-0lfPejzB-OubA-gzGjdH0IInwl9nA4M9oAhWXwES8igxxEgjQKySGuDSvyVGUJzJD9mNOLryruLL7cFZThoZWaiadw_H8QJw62ztxIFg7MiOb4E-ttcXSbvRxiOhsw2gggyIk7h_EyhxqUHp4p-5nLWUCG0FLxydalZswAO9_7On_Qp7S40e96v0jN_qQjW3hn1G52w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f013a68a.mp4?token=KURysiTUVSI9VP0Ha5QEPzmFXakd8zWpPBA0tXP__lBoMxjPKszvfZ7ovScGs0zh2Pe_usCP7NQb42i4GzGOnbf2AYRBH_D99hpe-qeEJHvaDgi4nn2xYEm2J-XAGTUEFmLyY7bd_65ckW-0lfPejzB-OubA-gzGjdH0IInwl9nA4M9oAhWXwES8igxxEgjQKySGuDSvyVGUJzJD9mNOLryruLL7cFZThoZWaiadw_H8QJw62ztxIFg7MiOb4E-ttcXSbvRxiOhsw2gggyIk7h_EyhxqUHp4p-5nLWUCG0FLxydalZswAO9_7On_Qp7S40e96v0jN_qQjW3hn1G52w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستان کرمانشاه: در بازرسی از یک تریلی در مرز پرویزخان، ۹۹ سلاح کمری، ۱۰ کلاشینکف، ۱۷۰۰ فشنگ و ۱۹۸ خشاب کمری کشف شد که در بخش‌های مختلف خودرو جاسازی شده بودند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84793" target="_blank">📅 20:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84791">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZqF_YmHSAlm6gY3Ksr_zhQZH8QzaquohGKPV-IMef_AjpvTricqP8BdrpszDfa-WQVb_tVsg2z9FODPiuzJmMymCtv2taI2xcAc6FpzbajGnOWt7FVm594ednleYA2UpXtwLs2hwvEEht4BG_RSvQ5BHn9q8HcPu6mza9FAYserAnqImCR179kqSLHXICF5z8MqMWWog6XeI0ROKqfUeMk6UFjVtr3DJcu75quyEu6NFXWIfaqe4oUbForK4ogcvCss6Fu-gvFATi6fATXuPUpQki2ILuR-1BDC4s0va3EMCu637hrpQlJTUOqplT45eMskkLZRsCBM7saKJvL9e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZjWUjOpka3a-Iz6mxzcByJBFigoPtsAIh-n7QuijWKFLP7RTuCzI3nYyodpz9coiKMsromBpSdd6PziXWuCwK5Me3xml9atQsz15nNBsqlmbLWZ32thlXEjMavE8LmpQPD_H6Up4WFfZEXrxjSiVNQKW4x3cINA-I-YeHmEbSPYkioM4wCO5ma7RqOMpZgK2F5MKBo5KyzxrCFsHqw-ajv1atMFiwb6-7ItCtvzXtnbbD4qNYEea89uKFvVbvc1CmtuoNra5jMltZwmsl-qSfn0S05UfiJyvv8ExWCV3uDAzAj4dj_fZktkznlrFChCv1PrVmnwL8X-bvMX10P4vKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بررسی تخصصی و کامل معنی “سیکتیر”
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84791" target="_blank">📅 20:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84789">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQLMFcCshk-uQee0DO7am1hK7ENVElQBOl8ytz62Cz2qPVDDXjLwajYioXSmAb59it9v60MyecM88YgwD3DDVFvX-ZvAM_I-zwDxuhDBTR0AA6xWnrewfK3BViD-GCJHhNTvsMbhKcFddr_nPx7k5mg49YadJk4qtX0RmpuwPN21dW4Vv6v7zz55e684rAliuwsTs3EKCznvDHKIXbIMtc2YZhhVwjRmjGpJbXFXdXqvH40H6RPKp4OzQWEcaHEQUnYr-wS1h9oiVIMBgN-789wZOUM4mhWmi6X0NwQlp_skLiN3EWiWrsDxLAx4TwEY8W28oJ7Z0RnxiNESExXPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11bb640d1.mp4?token=vp9zc__6LEZ4nbBN-EbnDn9vPMPDDPsG8_Xo9SLatE99dEbUHF0AW2yg9kUPgq6RZH8zRB6F--1BTk8IkVbj4dBehRJN1Rmf5oqb8MwtUhBUUn9gvV_JWeMfL_swcIyLg5edYqnir4CfFQXZRi5OpLi0u1uNKp3xcSiOTameh32WNycyxoiIumhIU6ZeK4WIw5G0VLj-dG8AAnhSaTsRJgZzlbOhqzNvsuMrU-YS7fjtJ1eNkV1kX-v9YbDdp4Sxfr2iWVheAn7HAl7mpqDZ8ZYXGk3_Laj8hXgHOkfueXNzcXVyvt8Mfb0NKKuF2C_JAUn3kavNyTlpn6wdmZTjFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11bb640d1.mp4?token=vp9zc__6LEZ4nbBN-EbnDn9vPMPDDPsG8_Xo9SLatE99dEbUHF0AW2yg9kUPgq6RZH8zRB6F--1BTk8IkVbj4dBehRJN1Rmf5oqb8MwtUhBUUn9gvV_JWeMfL_swcIyLg5edYqnir4CfFQXZRi5OpLi0u1uNKp3xcSiOTameh32WNycyxoiIumhIU6ZeK4WIw5G0VLj-dG8AAnhSaTsRJgZzlbOhqzNvsuMrU-YS7fjtJ1eNkV1kX-v9YbDdp4Sxfr2iWVheAn7HAl7mpqDZ8ZYXGk3_Laj8hXgHOkfueXNzcXVyvt8Mfb0NKKuF2C_JAUn3kavNyTlpn6wdmZTjFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بعد از اینکه «محمدرضا گلزار» به «رضا عطاران» تیکه انداخت که به خودش نمیرسه تا مردمی جلوه کنه؛ دیشب عطاران با این تیپ توی‌ جشنواره فیلم بوسان کره جنوبی ظاهر شد.
@FunHipHop
| Temsah</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84789" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84788">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/84788" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84787">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2z_c9cl51p02lScAU3-tP8F4B2kcSx0mHVA-61dxu9jorNlVAUpRQd4CHKOoEc8kzvriNlj59EOThZe_6D39YujvlZX1H5jnijEh-CBWjCQQaH4gaqM0ygadhROMsQkoFU0vB946fg9JTnzw5XlIHwFo-q2iUV29TgTudnxeUe6Bd3ZEszp0AHDH9EeDZKkmNavXjqCpGNMvdJJRRhs0uNbL2IOHoDgu_DviBn1TnL1hf7eTQukOmTKdBAgrTocbA3Zgv8nN264fCb2Y5XOmW-G4TF6TslVQVt54spXaeeJ86rEk29wI1rpWmKRzpLSxVVMReuwSFQOIixKBz6YMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G21
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84787" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84786">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:
بزودی درباره ایران تصمیم بزرگی‌ خواهم گرفت.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84786" target="_blank">📅 19:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84785">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d183db41bd.mp4?token=O27x2G_n-DA3-i3ZCBlWDAlyM5sb2VYePtIJn-ezTuDyAqUFEt1rmLGETUgXlEkMGw5UYg2PwF0z-e2hQIruezg2zS8ezBzLE3cx_LJdJfH9JvwSTWYhWpSl2sdRu3X_Z1FSdLzqJlGdhGLNDXo1mDiyiG135Mi1IqPNkhTM4kbo_gZjRiseFrBPSVAoewcvmeOjTqrujG2IrMzwu_QlMnn0YTP6MnuZspBhuaDkbcP4c77O-sfdSra99cI9U7F_tuVCDmOqFohmdqYi4_2HCEcsvHN_qnI2xX7c3ntJTXqfYB5qU8hiA9L8LShvMyOk5KSaZ14tgoRZW1wbKf_9aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d183db41bd.mp4?token=O27x2G_n-DA3-i3ZCBlWDAlyM5sb2VYePtIJn-ezTuDyAqUFEt1rmLGETUgXlEkMGw5UYg2PwF0z-e2hQIruezg2zS8ezBzLE3cx_LJdJfH9JvwSTWYhWpSl2sdRu3X_Z1FSdLzqJlGdhGLNDXo1mDiyiG135Mi1IqPNkhTM4kbo_gZjRiseFrBPSVAoewcvmeOjTqrujG2IrMzwu_QlMnn0YTP6MnuZspBhuaDkbcP4c77O-sfdSra99cI9U7F_tuVCDmOqFohmdqYi4_2HCEcsvHN_qnI2xX7c3ntJTXqfYB5qU8hiA9L8LShvMyOk5KSaZ14tgoRZW1wbKf_9aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهردار کرج:
همه ایرانی‌ها، کرجی هستن ولی خودشون خبر ندارن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84785" target="_blank">📅 18:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84784">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0c459f41.mp4?token=eQFYqfJlIMQ8d7BltFGReq5Az-v-KqEzcNHZ2yqzxiRhSOHdYTdnYzBmRrFMONe88GQtztSaVswoOSrfBPQNBAvM2VMIadbOTc1XqV7O6zFA5wlXkbB5DssO8FU7xp54EmKWOc0Ij4Dy3a78v0zFTkmKN2YI_JrAcrXMq5fHuOn-Of-CDnv2tK2vwrzvkXgczi8zo4_Ud6zMo9JM79XNxH3EJJMBAEli3Uupo4VH1IWdU5K9I-3MVLwYfe5Cpvz5Q3WbnIKookhLkLU0W4hTz5iSnO0H9PIO7Yo9AzXSmL0s9hqTckLU4iMFHxYkjNE05b59qX2uszouiXKmRVNFdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0c459f41.mp4?token=eQFYqfJlIMQ8d7BltFGReq5Az-v-KqEzcNHZ2yqzxiRhSOHdYTdnYzBmRrFMONe88GQtztSaVswoOSrfBPQNBAvM2VMIadbOTc1XqV7O6zFA5wlXkbB5DssO8FU7xp54EmKWOc0Ij4Dy3a78v0zFTkmKN2YI_JrAcrXMq5fHuOn-Of-CDnv2tK2vwrzvkXgczi8zo4_Ud6zMo9JM79XNxH3EJJMBAEli3Uupo4VH1IWdU5K9I-3MVLwYfe5Cpvz5Q3WbnIKookhLkLU0W4hTz5iSnO0H9PIO7Yo9AzXSmL0s9hqTckLU4iMFHxYkjNE05b59qX2uszouiXKmRVNFdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید سحری برا استقلال و یاسر آسانی کار زده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84784" target="_blank">📅 17:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84780">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/et9pK0m11ESd_7G0Q7d3p5KbF2CyDja_Jn3njj7Q_6JVukRxAKDTlAC85qxeJU6smxgh-pGm62XLkYNbqAsbWka6aSu0sVMNq6H4i4QNlavMVVRf9N5PIlpsYYQQ_QcloiOCG5q6W3WJzmIAJXYReAvSFEQFX0oMPKm7EQcgcVUlBjRlhAwEfVIn3m_PzktxaqfKjbSTuHSLaem8oa_teXZFa9CueZK2sybISTXN3W5VI374UZpVXhwNLm-7QtCXfJEJ8-rjGTtDIQDfGeeomFovbQ2cTFg2sgfsikAiHrmPnN2Uv9ypFiq99tICU3JafUdyVQlzvshpmOrYm1fdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWxTvnWuPt-qcosq_Pl0ttfpBdurF_sPOWoVZYbE0D80q128c9BRdoDkWCZjNTiD74xJNjdCMmsW5t4nvzLzhKTFNysToZcF8rE7bFbSi-phZcVkEbnPEGauHv0ogfULCs81QqtQDBQ0CAMZrjzaSUoHQMcISGnwdk4aO5uHXHwWZVRC9-ESLkZP2t-4JH1PdPPqEEk8iOi61DG3zYnGQMeh7JDPnuItohxsdJC2g033ZUQza8HqlWJxBa0M2t98OlsetmHq4K_vy7VP-XyX3Dl9AvMcANXPzZzakwxF-WzwNPkuUeM60Ft7G_KT02MjbB1yT3T-2R4CN59OBmGlQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjQr7Nwsmw5GHc2qGPtakvcXXc0vRv6sj0g2S1Ki7xioOgux7VOwj7pM1NH2eEVBieNgVifSE-Uxg2sum8Ms1badxPOTnYC6UPSIljd6AHKUf8yQDFdvbEbfPuNZLgM08UTRxhiVRUd5w8M3pqACqdUyHJFY654F31Tl1PZLjKnvaV3ULv5gKgPZ8dQbcdW0VUflU4jHhs75Jx7KGxqHzJ1iH5STbZD4Fcyt5ThvZoQ392ymD4AVk-THNNeHGAndj7HeqXlSQZHZzgipTEMuYGoiKSYrPTNV0UZyh0GaXkuI4ZA_7XD5R6adCudz545FG5d9zr-3Yk3IhyhH2ePsKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rHeK7yks9cP9AwDK6AQ9dYCoYYjR5bbdI3_ghlby3OTxR_AdP0McVEASn3k6puSwc1fdpScu9qsj8TV2sktcOPG5kHRk3hlK4nhYq25jOeWpwuXqV-g25ztGP5_GjEjpj4W3qsivq4ErUevJkfZJGT4FA4KTuSOuq6yCqw0toJz7Rd04FYwZXANgp1HisNw84h3HGMLaT0O6KHiPK0om7yP0rmPOEkjUc_h_qd1704bZHqFxcMhcQkp2kudmjekwtSFWwPz0fgkFDRQbfUZ5orRZvqqiR-nEZS8ZWyQNTQgf6PWeLv6orK7S78efkvUJzbQ93-y_K2n-1EwTUQOKiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز یه عکاس فرانسوی تونست از پدیده‌ی زیبای red sprite | رِد اسپرایت ، عکاسی کنه؛
رد اسپریت‌ها نورهای قرمز کوتاه‌مدتی هستن که گاهی بالای ابرهای تندری، تو آسمون دیده میشن.
اونا فقط چند لحظه (هزارم ثانیه) می‌درخشن و معمولاً بعد از رعدوبرق‌های خیلی قوی ظاهر میشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84780" target="_blank">📅 16:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84779">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=fzzJ72lYJxyAETQbmYb_pKInHijHUIa8E5Z5z3p9s0--HTtdcqtmNU2kK6kNSHwpjpiiOW3bTFvv7RPDH4ES_oK88sQqaqRRjnG1uJ1uYAXQ5Ws2E2D7i5tP_xYjMmLG0P6FtyXHPrsU09OrDjUQP5CeuOnt2qP2TxJ3SeKmJR0r89rk-BGqywQ5_ijaJwLEXE8_bELruysu2IY1rPHQ7ELYTX1J0_dIz_32FPqZp1xakJV2vYwYMTN-SGX9j6TlUezMbW09P2NDh3SInw-MLC79MkL-vk0-hiCNUI1r6iMjwM5d-jd9QdWsBGrT_TGVqC8sTOQZfroH35jfzxYYcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=fzzJ72lYJxyAETQbmYb_pKInHijHUIa8E5Z5z3p9s0--HTtdcqtmNU2kK6kNSHwpjpiiOW3bTFvv7RPDH4ES_oK88sQqaqRRjnG1uJ1uYAXQ5Ws2E2D7i5tP_xYjMmLG0P6FtyXHPrsU09OrDjUQP5CeuOnt2qP2TxJ3SeKmJR0r89rk-BGqywQ5_ijaJwLEXE8_bELruysu2IY1rPHQ7ELYTX1J0_dIz_32FPqZp1xakJV2vYwYMTN-SGX9j6TlUezMbW09P2NDh3SInw-MLC79MkL-vk0-hiCNUI1r6iMjwM5d-jd9QdWsBGrT_TGVqC8sTOQZfroH35jfzxYYcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست یه خانوم از اثار کتک خوردنش و 10 هزار کامنت این شکلی...
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84779" target="_blank">📅 15:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84778">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehdi</strong></div>
<div class="tg-text">بنظرت لیگ دانش آموزان بلاروس پخش زنده داره؟</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84778" target="_blank">📅 15:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84777">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مرگ دختر جوان در ژاپن بر اثر سقوط یک زن از طبقه یازدهم
زنی ۲۹ ساله که قصد خودکشی داشت، از طبقه یازدهم یک ساختمان به پایین پرید و روی دختری رهگذر سقوط کرد دختر جوان جان باخت، اما این زن زنده ماند؛ گفته می‌شود این زن به اعدام محکوم خواهد شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84777" target="_blank">📅 14:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84776">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کل مصاحبه گلزار فقط اونجاش که گفت اینایی که پولدارن ولی مثلا برا مردمی بودن به خودشون نمیرسن و درویشی زندگی میکنن کسخلن
تا خود صبح باهاش موافقم، کصکش پول زندگی خوب داری چته مثل کیرخر زندگی میکنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84776" target="_blank">📅 12:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84775">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=Bbs6sd8KiBXVYxggUNRPTlYOTZF-RszNL7U2p_OmQnUlNx-ihOs8-5x_mV_U2idwu77j5gfGwW7_RBzwzu6O9YGYQNwOZppG9sLHJuDgk1OWOj5SiOGM9Yn5VzLiDhlB2QC5CZLNJ3Xxezlxa6lJ_fRRc1Ub2xJAQTB3m7nYYv0RCMn_Fsi6_TH5yReUJqM1tQQakEUoyD0650aU5j2y0tM4NO4EXKY5_YyKX_ksyNxUIlH9Kz2bAjLglJNSFDo_YEDnprGnRyk3oKsQGr8fO_zayk-q8UWzHmmMsXWWMatIYljlz1ufAdoYIaMuOqgitkmlebQjjDiDnkm5z5b2Hm5C_VHVdsMgFdoDT8Q2Z26eK75M35Wgzn9jZn0Ukf-OlrqDuC7Misd77d1KSqaCSg_WBWwzsHKT5wNNXbhhZMY6qJrQ_FEa3niLEJSKWKyrVML6TzuBxRTLDJ17QWcVJJTCTm7lk5iTYwiSqRpoz3OUswkDsU9U-iP-HcMFeONgmQUoM4J2GmuT0m76tUvhv1_HhsFR5Lyt9wM61b6AWoN2OGIozJ1ROwvr6bs7j4N3-BWyPilRCeaWqW74x0HbxAxDYKuWKkGmANAouLrslu9UHKU0xKIIOJ7Qvcye2jDF92Lxo0IcNFMWmwP46IgFuQRZE2AJGxTMl0i1K6V7PZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=Bbs6sd8KiBXVYxggUNRPTlYOTZF-RszNL7U2p_OmQnUlNx-ihOs8-5x_mV_U2idwu77j5gfGwW7_RBzwzu6O9YGYQNwOZppG9sLHJuDgk1OWOj5SiOGM9Yn5VzLiDhlB2QC5CZLNJ3Xxezlxa6lJ_fRRc1Ub2xJAQTB3m7nYYv0RCMn_Fsi6_TH5yReUJqM1tQQakEUoyD0650aU5j2y0tM4NO4EXKY5_YyKX_ksyNxUIlH9Kz2bAjLglJNSFDo_YEDnprGnRyk3oKsQGr8fO_zayk-q8UWzHmmMsXWWMatIYljlz1ufAdoYIaMuOqgitkmlebQjjDiDnkm5z5b2Hm5C_VHVdsMgFdoDT8Q2Z26eK75M35Wgzn9jZn0Ukf-OlrqDuC7Misd77d1KSqaCSg_WBWwzsHKT5wNNXbhhZMY6qJrQ_FEa3niLEJSKWKyrVML6TzuBxRTLDJ17QWcVJJTCTm7lk5iTYwiSqRpoz3OUswkDsU9U-iP-HcMFeONgmQUoM4J2GmuT0m76tUvhv1_HhsFR5Lyt9wM61b6AWoN2OGIozJ1ROwvr6bs7j4N3-BWyPilRCeaWqW74x0HbxAxDYKuWKkGmANAouLrslu9UHKU0xKIIOJ7Qvcye2jDF92Lxo0IcNFMWmwP46IgFuQRZE2AJGxTMl0i1K6V7PZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فنای گالاتاسرای دیشب جلو هتل بارسا:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84775" target="_blank">📅 11:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84774">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یعنی هنوز ایرانی ای وجود داره که فیسبوک استفاده کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84774" target="_blank">📅 11:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84773">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗺𝗶𝗻</strong></div>
<div class="tg-text">ما سیاه پوستیم((((؛
همونایی که…
بغض نمیذاره حرف بزنم
حرف دلته؟
خب حمایت کن سیاه پوستا به حمایت نیاز دارن((((؛</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84773" target="_blank">📅 11:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84772">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">من دقت کردم از وقتی فوتبالیست های خوب دنیا سیاه پوستا شدن برکت از این ورزش رفته، چرا انقدر عمر حرفه ای ورزشتون تو فوتبال کوتاهه شما سیه چرده ها، ملت هنوز با مسی و رونالدویی که تو لیگای پرت دنیا بازی میکنن کری میخونن واسه هم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84772" target="_blank">📅 11:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84771">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=Gf1RZw09brtsKEsa1-eyLbMiOPu9t0X8kMbFi34Agr4VMYBBhNsyW3JdZFwKw15iA2I8Pk2rcooyuQRpmqT9RvSj9_U3jD7sEEOuFlVDdMWix51AprsBMNcOhkzKxS0X_K0v2dI4QnN0d8SUodzvfOdDKh7cOh7qNnfQjgtetHnGZRXQxWvIWVQKfvEUtDbX6FZa2lR5weXawd4sKeqeVRsTUeL0ZF5VQlG3Z8UkSbvgKVU0dS6asYDd1lOy6n0Kk8_7u9-ZyFBDCdPWj7nEkMGWte_gS6aZByVjVX_9HNnXr5u4XLwkdYm6YPaNQpFT0716SG2qu8UXSNEwDUFNGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=Gf1RZw09brtsKEsa1-eyLbMiOPu9t0X8kMbFi34Agr4VMYBBhNsyW3JdZFwKw15iA2I8Pk2rcooyuQRpmqT9RvSj9_U3jD7sEEOuFlVDdMWix51AprsBMNcOhkzKxS0X_K0v2dI4QnN0d8SUodzvfOdDKh7cOh7qNnfQjgtetHnGZRXQxWvIWVQKfvEUtDbX6FZa2lR5weXawd4sKeqeVRsTUeL0ZF5VQlG3Z8UkSbvgKVU0dS6asYDd1lOy6n0Kk8_7u9-ZyFBDCdPWj7nEkMGWte_gS6aZByVjVX_9HNnXr5u4XLwkdYm6YPaNQpFT0716SG2qu8UXSNEwDUFNGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شعار موردعلاقه‌ ام «گی‌ها حامی فلسطین هستند!» می‌دانید اگر گی باشید، تو فلسطین چه بلایی سرتان می‌آورند؟ شما را از بالای ساختمان به پایین پرت می‌کنند. شما را به بالای بلندترین ساختمانی که دارند می‌برند . البته ساختمان چندان بلندی هم ندارند ولی از آنجا به پایین پرتتان می‌کنند. با این‌ حال، مدام می‌بینم گی‌ها از فلسطین حمایت می‌کنند!»
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84771" target="_blank">📅 11:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84770">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8EoBxXSaKqO-nkdzaHtVoAhQfyKJBKbyTODkVScaw41LKceN6_dI0MFkBAjFeizbNqxSJK7H1170zKFnf7ovKtc83Jr5VbNwdmqetKUpiukh7fEDQOpiqKzlvFJ_qWnJAf60WgDVMHCaEjejomEyAX-5aex3i8eOcwxOCuP6EG1ZyTxpnV5giTfzJ43r6ZBeq701bNdhjU105-I9mM3XMhW9XMESbEsB_dE3FUz4xLTxIJCxJOYBIz6L7rmZs6oh-BBVoayXDGd9E1D57p3mUQUWbchRHmhD4U3A6-HtukUrzku0XFbbF3V3wOjX8yVpybDi7fQK27uPcnlOB38TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت دیوار پر شده از آگهی فروش سبدهای گل دخترهایی که به مناسبت روز دختر، جعبه گل هدیه گرفته‌اند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84770" target="_blank">📅 10:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84769">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84769" target="_blank">📅 10:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84768">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=kkywFw-4Gf81GCZlFo8vCUrWWH8baNIsoTLGkd0cWbPgkltOLqakPMv7pay5zEns_XQ35LVZNGXbioNfiMisdkUWJ4hTvHluF--E7uBfhrnAVtoOD-GCunSN1hAfZ9Ri-PPgWBndg0LNxptpFkkE4LF8eVsYG7RYKMRN_vqOxGV7t05_wWOiCJ0n-R3G7GKZR53jhlIGuHDAwstGMrj2whIKpz0zjdy5FKLsyaNFX8kflGjwhlpiMf62oLbkSPBZmqrewy-kxnGIRePKFGVTmiVsXvkEUhW6_3fAHcQ2qG6Ck-krP7XT1QnOoqmvNXqTN81-h2GR7LTSPOxBqT3DmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=kkywFw-4Gf81GCZlFo8vCUrWWH8baNIsoTLGkd0cWbPgkltOLqakPMv7pay5zEns_XQ35LVZNGXbioNfiMisdkUWJ4hTvHluF--E7uBfhrnAVtoOD-GCunSN1hAfZ9Ri-PPgWBndg0LNxptpFkkE4LF8eVsYG7RYKMRN_vqOxGV7t05_wWOiCJ0n-R3G7GKZR53jhlIGuHDAwstGMrj2whIKpz0zjdy5FKLsyaNFX8kflGjwhlpiMf62oLbkSPBZmqrewy-kxnGIRePKFGVTmiVsXvkEUhW6_3fAHcQ2qG6Ck-krP7XT1QnOoqmvNXqTN81-h2GR7LTSPOxBqT3DmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل مسی اسرائیلی نباشیم
☝️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84768" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84767">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UelL0Bj3Eqa7Y4iqtqYhWyKGvCecjt8BOj1Z7p8CcRWl0_PKuwzbzsEsq4vsEeO30djZFkKDvnBE-hQPN59cgxrfVEKJhNMLtbJrTVAcHuv6_-bOJuhm_USQ8VyjG98AdtbCX1IlUaAQ2p-FAg9q982vVeoLzxUk3t7zIEdGXhqn41Y7BCi91WBX8AXoJHdn6vdAeZnxb7hl2YxHIgoTJeY0G3Zi0dk497qfzS-dt6oNsjTXbEslxFJC4Dl1n_yxyhA4ZvxxffYrYDQdrIxhpPo5Q-xioPihbS4cb1vZCGSgHMJlMqO-O4vXoMrutJA5Rn_tYIxe8GFFTF60ZWoF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r21
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84767" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84766">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=Kh18jjdut0ChPfybI44-juQtLyYg9nONp88hOwe0KT4WTqAdAXwN7urbr7zhRHyL2EZEX7Qg3GenL9DjO4dlCMz8T8fCAcpT6JW1G-d2z_nbsxzAk6salWPRgv_Hkbqi27Wh9uyzBmBZ0PH5egARpLvjw8a4L5NG4HNNB7i8WLDo_P4x1lLONRvwLuaNpkg0bBqwfDgzhSJVP98bc_g94pcwiUkL4ANz9Jwl2TN8IEVWrGKvAYaIQfgT4-24vLgAfVvMml3mwZ5jEIsPYI9arnvd2ObDxcZA1rc6eDndY4Bf7-DwJt2EwTHFoiZoSDW6vb77YVFrjgotlQZvhJ04oH6u9wZglslbbtqNDfmcneV4HjCkspWatGu9BqGFJbfJyeJ5pBdgbM_n12rPZC3HMz0WeEYYY5I8FF40qdH9_UTPt2VXn2pw_2GZ7lnUIEBpIBBVoqlUNVkHUXVow-aHND1NzejM_wvLCT814TQgupMrdu9tWRTqXFI-3lbhqq5bRs4VqW0iEXmWsAZl4HUg_bQ17VRblfsdspqF3j2pbPaOGao4VXVaKKhESLNUFun2cTBFH5ZC0eARJany7ZVCATc9sQyABc-AHQ-GuKuBJWhZ6Xk2WfRczooRJvdjmHnP23lEZUYntfASMtB0qqSCkpPvL0VDmm8igXqW2qdq_ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=Kh18jjdut0ChPfybI44-juQtLyYg9nONp88hOwe0KT4WTqAdAXwN7urbr7zhRHyL2EZEX7Qg3GenL9DjO4dlCMz8T8fCAcpT6JW1G-d2z_nbsxzAk6salWPRgv_Hkbqi27Wh9uyzBmBZ0PH5egARpLvjw8a4L5NG4HNNB7i8WLDo_P4x1lLONRvwLuaNpkg0bBqwfDgzhSJVP98bc_g94pcwiUkL4ANz9Jwl2TN8IEVWrGKvAYaIQfgT4-24vLgAfVvMml3mwZ5jEIsPYI9arnvd2ObDxcZA1rc6eDndY4Bf7-DwJt2EwTHFoiZoSDW6vb77YVFrjgotlQZvhJ04oH6u9wZglslbbtqNDfmcneV4HjCkspWatGu9BqGFJbfJyeJ5pBdgbM_n12rPZC3HMz0WeEYYY5I8FF40qdH9_UTPt2VXn2pw_2GZ7lnUIEBpIBBVoqlUNVkHUXVow-aHND1NzejM_wvLCT814TQgupMrdu9tWRTqXFI-3lbhqq5bRs4VqW0iEXmWsAZl4HUg_bQ17VRblfsdspqF3j2pbPaOGao4VXVaKKhESLNUFun2cTBFH5ZC0eARJany7ZVCATc9sQyABc-AHQ-GuKuBJWhZ6Xk2WfRczooRJvdjmHnP23lEZUYntfASMtB0qqSCkpPvL0VDmm8igXqW2qdq_ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه بادیگاردا این یارو رپره میگفتن خلوت کنید آقای بولینه و نمیذاشتن طرف نزدیک بشه، دو هفته مغزمون گاییده نمیشد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84766" target="_blank">📅 08:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84764">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=L_f5qqZbixOjrt3T9gG8iVvJuSpx2h9PHn2DQLuiVJb5oDummFM9n_YoLi4ARulrw1VSya1UV8wlH4Y3brMITcPbmOYRkx4AuHALWTYLGb6HadVn0KCoHjsQ2nsseRqt8om8GvcHUUhqWRzyz5VkrlQWDXePoy6CztRfbjgVDTMt5scJheP81npsKN6ML_ywy65dYxC8xKu0w3xbmgSTy2pknqrRb4I2VXW-YzBuGc6ufz6HcXtDAdxaZ-bVDCFrZVtp83nKl5RcCH96Yo-RtyVaY6Tc9MPAnJNsB-TQ-wMd-l69qoA5wGqXPXKpjwkvSebdZQSIMOUOaInw8wYnDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=L_f5qqZbixOjrt3T9gG8iVvJuSpx2h9PHn2DQLuiVJb5oDummFM9n_YoLi4ARulrw1VSya1UV8wlH4Y3brMITcPbmOYRkx4AuHALWTYLGb6HadVn0KCoHjsQ2nsseRqt8om8GvcHUUhqWRzyz5VkrlQWDXePoy6CztRfbjgVDTMt5scJheP81npsKN6ML_ywy65dYxC8xKu0w3xbmgSTy2pknqrRb4I2VXW-YzBuGc6ufz6HcXtDAdxaZ-bVDCFrZVtp83nKl5RcCH96Yo-RtyVaY6Tc9MPAnJNsB-TQ-wMd-l69qoA5wGqXPXKpjwkvSebdZQSIMOUOaInw8wYnDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تورکا حسابی خایه کردن از بارسلونا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84764" target="_blank">📅 07:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84763">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=AN44lxXcsGZlTe0j3-zjfIq-w6mmWLm9VYOndI5hLJypE_e-SOr7LkpOIAXFDDu-dxJxavZd1tHwuidcUJ0ZfonwhFgIMRZh0ZHDWYGIq9nG2oBStoszzbRM6F3QJvQDeV58ju8Z7eMcTxx_t8fUFBKLSmjkuNIAEG7wtY-TLR1-V8rAz2leo87XPCUzbjZXdylWrEOjUhLGIrBtf2qRMW0H9zoHM5OyHI0ZB60Os8GONq2ske23kf3GPH-_gtkkSwtHXvqxV4o-IatWhCahvJknWyeZKKZ3xVK1GTUwfttHWrtAuVPabagsTQlviQEHssHcpqtvOk2h5Uo8n1jOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=AN44lxXcsGZlTe0j3-zjfIq-w6mmWLm9VYOndI5hLJypE_e-SOr7LkpOIAXFDDu-dxJxavZd1tHwuidcUJ0ZfonwhFgIMRZh0ZHDWYGIq9nG2oBStoszzbRM6F3QJvQDeV58ju8Z7eMcTxx_t8fUFBKLSmjkuNIAEG7wtY-TLR1-V8rAz2leo87XPCUzbjZXdylWrEOjUhLGIrBtf2qRMW0H9zoHM5OyHI0ZB60Os8GONq2ske23kf3GPH-_gtkkSwtHXvqxV4o-IatWhCahvJknWyeZKKZ3xVK1GTUwfttHWrtAuVPabagsTQlviQEHssHcpqtvOk2h5Uo8n1jOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثال عملی سخت کار نکن هوشمندانه کار کن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84763" target="_blank">📅 01:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84762">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_enscroyCy3oBSuC5Tjzl2wr4b3IXBesDpCOKVGDd3zqipNOG9QznrXZ6L9BvGBnKcej2ohfX6T3PO65Ge0ObQRRcWvELRXj1FxOxtkBXD5FVjqsBgFvXGANMhL-nXy80DNNTNtE5Uis42TxJpzBaFDxJvsvLWjCgFJrXDZAiMuM-VQS15pPlUTK436baXs0hYTPp7cT2o_ForfEduf15N1aOyXyk32ggwIG_pmIOrMEYS8ISqmeJBK7twuQFfb53LguP7tVcpu4nIogtZq4Uv7HEtkg8Sft9q9yxqGg17f32xuK8XZGjrltHuj79MjjgbUD4WDzPpNCACTiBMrtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84762" target="_blank">📅 00:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84761">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">خدابیامرز نقشش تو سریال اینطوری بود که اگه اون لحظه جلو آدم سبز میشد تیکه تیکه اش میکردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84761" target="_blank">📅 00:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84760">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSPoFRWUjxE4X_PDVHCXz78k1efawdSI0CsErTAxyO4qC1ZmnZS9KOyDuzQudZ0WVk18ugxtom8-nuec37D4MuRL-INl3lo2Mj6L2Tlvi2Xvdw3aTJ0NFd4QkfPCQjbGAdvedxkGluy_7bLrWpJgRenH5Ufg-uQ3qEgujX6OuWV8PwBrxETrw8GxXZXdhRfAPSLGj9iBA-5B52xNRzb5JAmBHlMQCQC-sR1tmYIWKLwuV-GHdnq_48w3vdoYTrR4zl87ip_q0KN6qKMUxdj8bRZdCifAE_nU5Npca8u3XOHD1lREGKFczqZ6U35cq7cqUZyuTmsAkaBSn6o0wpz1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84760" target="_blank">📅 00:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84757">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE43sj2dCCSxrwEGOUuB7N3NUf7umx9AuIX794usYSTSc7yBCuwNHfuwG4TefZ8ccoHW1hTeeBgjRJh9jstSS9-L6eGNGksdcYxKtkmopKMHll0V7STzuxI6yUQbgCrwKRzGv1CIDRke1LGPqqV75yKBC4k3xiHQJKREuQkyZrQMMxbL-iLs5_TG-N-dLi-snSDwbzY4SE9uweL7WXIAbt36Xcx0RRuZZu_ey5IY0N91cxZ2ntRTknF3DuN8WAfsjdKqMuvtcMY4qxgjY0u5CtGvikj0Z6Cvb7NIBarQI-dZm7h2kAnGIFnsayBg6ku7S5d4iRo-ZKxxdpN42m0xDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داشتم زیر استرس جون میدادم حاجی</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84757" target="_blank">📅 23:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84756">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swvvBQTvM69L2ymHF93sOTjDSkwAk2D6uFL-iS69jSnN6t80NsZniMOtVKzuKOpOHp8Uv1VXXaLBP4j9no-QyRa_0ML3I69izrMNiFLo268dTMRO2lzMRbvi00VURTfDobyJCGinnstoKfDToQhAwrdfqW0RSkRks-cOxzQGlaDUJ788D_n3ms1j4x69XWbLUTKhdOr3tF6WwlUg-pNfuC518beWBKgD2h-pLC_KrYNEVRCCLr1O5ZJ-M9ntDv7Bem6MoqP3yRv5vGonyUjzd0FzBt4hC28m3PJll6_l-9so5oXsQpTcCytoqjmk-lq0Mtx9bvP0X9iuSertHncXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید فدایی و شاپور و رفیقشون ارین بختیاری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84756" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84755">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حبیب کیرتو بخورم</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84755" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84754">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBsQ2oAulqNv9UoOpkGnvfZOiUF5wHP6Far0t5FkJ2ygSU1J9viwmgpjeFgejEfcBbfh9_g1QCMsVHOxjJuAMW4zl22ecTRHPuLNcLuZnB9x-5rzQZNa3FndI4Fj_EEsOaBVyhRpDrKvCD5ixtPlxgyDt_ute9_0vrVHopPMkCD90RV8W6351xUKnUq1mKnBrzlpJXJMtPRFMYbYqzodbdbCiGE91dyI6PFEwTcHn7nCw5QRYNT3X3_7sHDDxJ1GbPotowfZSHRnksBTn3ZueQA02rLg5UP47sllTLK3qrdy_0uvh9oyjAJ1TSqIeHcZaKlKF--aYfvaUA1CDKZHiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه رو
😂
😂</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84754" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84751">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">هنوزم نمیتونم درک کنم چرا هلدینگ دو میلیون دلار داد این سعید دالگخیزان رو بخره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84751" target="_blank">📅 23:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84750">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtfzKPAJD9jgGDY1ddt6cwQ30uSMzy7KMjAwMsXunyeQcPjFnt7nXKGQcZ173vJWUub25R-Lls-mwHhq3ndbBzxuvFxU9Psf2Eifz0ayXUl23WuLxcQ_-6MJGWhYMF-psyfLYXZ5eQvoso8wtkeNJa_CJckPjgfjcXlpCHN_oNNTLZLHDREakZRgQ0IujxmUX5aiynTUr5qMqADxsV_DmmPWWrE-ph3yY2C1whVM9cWl98LCUX091_LgX60pXVYu3EG9GkNswVtD_vhlu3FI3eqOM8ENBsjZRjgY73moywuuv5FzDu5-yNcbOdvTb8xocTzh_setKrJGryBGcVJo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84750" target="_blank">📅 22:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84749">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84749" target="_blank">📅 22:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84746">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940390f975.mp4?token=AG110l7XCEBfmdgitH7atTNlDSCp47K4Kf3mgIJ58piKheBbNsAyW4pFvCyU9weMdRb1zvoksU53V1nhBau86192uInycP0dxRefwM4SQdEnQ4Q8rGrjHigIxNZOSII6IzNpz1BXFDZcwG39Y1FkWKUrrUfd1HH7HcvOUB7iYBcPEOtgzi7qfC38rDZlt74wufv7ErcLgArzl0AB21Qz7y2gpa1o44LKP_4Ra4tlVm-kA12vur_sq85u_UPq692pOpTfv_TMOJQ2GsSgRhbqkMuvpq8zrl3PUXaEo0kWiyBlcu9jhTws73bKJvYA-lFhIq_bPr8Mx135VU77Th9s5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940390f975.mp4?token=AG110l7XCEBfmdgitH7atTNlDSCp47K4Kf3mgIJ58piKheBbNsAyW4pFvCyU9weMdRb1zvoksU53V1nhBau86192uInycP0dxRefwM4SQdEnQ4Q8rGrjHigIxNZOSII6IzNpz1BXFDZcwG39Y1FkWKUrrUfd1HH7HcvOUB7iYBcPEOtgzi7qfC38rDZlt74wufv7ErcLgArzl0AB21Qz7y2gpa1o44LKP_4Ra4tlVm-kA12vur_sq85u_UPq692pOpTfv_TMOJQ2GsSgRhbqkMuvpq8zrl3PUXaEo0kWiyBlcu9jhTws73bKJvYA-lFhIq_bPr8Mx135VU77Th9s5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84746" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84745">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=NcyhfaBNw9WIKMbuVdrEDn9Vzi5rK9CTWnIs7hHNN1NcRiuqPwQpQwooi-oueb2JTo12hIQMDVoDJgCkBk2YGLnjvOyi6eMjHr_FhOIeZoL_S1ySGYL1JeDRju3JYA4TXG_Hr3DExsVOCYfuVrw2A5KMm449qsh8q_LVfQ5SiwB6PQHVXj15kBtBqL5ybM256zrVg4NNoWBlJotoG99cJEYae3-P533AMAmwQYR5xi5VZSHi-Ro5OS_NoWCWI67rx1MdqFh5DjSHxUlzFikl9prKmhA_dOZ1pfXrlScoUtzgJER1fSKtDSlhhbKxT-doOdRyNtcWwOyU81r6Ry8b9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=NcyhfaBNw9WIKMbuVdrEDn9Vzi5rK9CTWnIs7hHNN1NcRiuqPwQpQwooi-oueb2JTo12hIQMDVoDJgCkBk2YGLnjvOyi6eMjHr_FhOIeZoL_S1ySGYL1JeDRju3JYA4TXG_Hr3DExsVOCYfuVrw2A5KMm449qsh8q_LVfQ5SiwB6PQHVXj15kBtBqL5ybM256zrVg4NNoWBlJotoG99cJEYae3-P533AMAmwQYR5xi5VZSHi-Ro5OS_NoWCWI67rx1MdqFh5DjSHxUlzFikl9prKmhA_dOZ1pfXrlScoUtzgJER1fSKtDSlhhbKxT-doOdRyNtcWwOyU81r6Ry8b9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر بخاطر آژیر خط امنیتی (احتمال حمله حوثی ها به ریاض) به تعویق افتاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84745" target="_blank">📅 22:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84744">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بازی پرسپولیس الهلال بخاطر حملات موشکی حوثی های یمن به عربستان لغو شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84744" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84743">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ناموسا آسانی حقش لیگ ایران نیست</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84743" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84740">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">استقلال یه بازیکن داره اسمش احمدی عه، یه بازی قبل دربی رفت سال پیش مصدوم شد، ساپینتو میگفت به دربی میرسه، یسال گذشته هنوز مصدومه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84740" target="_blank">📅 22:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84737">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آسانی نیست استقلال در سطح تیم سالن بچه محلای ما بازی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84737" target="_blank">📅 22:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84735">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بازی استقلال تو آسیا شروع شد...
گزارش لایو با چاقال اسپورت
🤣
🤣
👇
@Chaghalsport</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84735" target="_blank">📅 21:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84734">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJW3xAIooZbyd1uLFi3aw2HKVU15MGIdNM3dSp8arZcZOrMtrDxXoZUJPiV0qc5nf3ANjtu5o4LppQbMVYLfhFK8yQmjq4VcOaoPoV2uDX6y0QbucKoXjf-GYXAZVP8LXJdll-77oTbmES0fmXPqsxJ0GCX_IexQexW23gl85-_V9ShZ6Q9pLaEN8m5nBsdS7KRFV3PqCVFFwaNlV4Is2RT2NIpzHX2rJ03auiWO-svf4FRmqQ_4JotJ7bIEPBwPAYO-N6g4LhpiwtJ6YKes6x37PF56v1VI2CzyVBxsCokNQ4hf4YkJuTjmqGasVsERj-tpoG_3n9oI1giXobKS2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پرسپولیس برای بازی امشبش جلو النصر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84734" target="_blank">📅 21:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84733">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=qTZ1_jGbUZxR4PbbIAdhoiB-9qDftb4JsHRk3phLEbmf5X2g4f1k80hNbXWDzrS98JPgMI504LnYv7N_4GRyoOJ_JuE51VSVNTVO1x4or1k8G1qn0uoh7aNDFeHdgW6WZSw4_zC-79X3v590-NIevw1EwzfHqQgtvGFi4fa8bH7yPM9Q2mz9bqr6GFLEvpPN3ma-4aHCSvh5rjra629AF_FbPne_LSnOaAjFq3HMGPxTDbnAG3i53kSpEc95gZOEmoRwNHK2PajF22KzJ8ty0tbMWD3ZESwuoC1w-Hz6Vm37wfuI8xQz6k7NCowrFc2_PPeuab69UJIWfLuhSsGBiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=qTZ1_jGbUZxR4PbbIAdhoiB-9qDftb4JsHRk3phLEbmf5X2g4f1k80hNbXWDzrS98JPgMI504LnYv7N_4GRyoOJ_JuE51VSVNTVO1x4or1k8G1qn0uoh7aNDFeHdgW6WZSw4_zC-79X3v590-NIevw1EwzfHqQgtvGFi4fa8bH7yPM9Q2mz9bqr6GFLEvpPN3ma-4aHCSvh5rjra629AF_FbPne_LSnOaAjFq3HMGPxTDbnAG3i53kSpEc95gZOEmoRwNHK2PajF22KzJ8ty0tbMWD3ZESwuoC1w-Hz6Vm37wfuI8xQz6k7NCowrFc2_PPeuab69UJIWfLuhSsGBiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا چیکارش دارید خودش دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84733" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84732">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هالند راجب شایعات سقوط منچسترسیتی و جدا شدنش از سیتی: خب اگه سیتی سقوط کنه مسی باید نگران بشه، چون من برم چمپیونشیپ رکورد ۹۲ گل تو یسالش تو خطر میفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84732" target="_blank">📅 20:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84731">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ_d_WpBzTZV2XlZb5mMa9BX3IV2OsLw6Qy0jr0wvvUHniB1YjC0VptRMlnRycP5peeE_fwdCvSZ5uivUgszYFnUp3WJJ8XeOpQf6BaIA0vh0aD59dIFwck-Qi6FRRYTdr7LQSBQy7nPjNzdxHT-2pz6dTkl4Mxcjsmn0_cLKP_PtyPmQltpm-bGfa2xsNfxmkJ2tZHmv5pLTP-b_Rm0JZshlg2L-Lcl0jCkB7AlIiv995xX2fY7AWsDEEqUW8oz1qA2nu2hryfEOxzVmuqh1rP05hF2tSfzbfNpytiwcwpGmLZ8oi14yEemCy9YfeyVUY8oO1GsDN7SBYRoRXK5LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران رتبه ۴۵۹ بهترین شهرای جهان رو با کمال شایستگی کسب کرد‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84731" target="_blank">📅 20:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84730">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=okiQQiCcs089vnLOZavk-CRGrriv5OggkTUojXKceXl0eAgLWirloVbI6rX2ON_VsEpXJDmdt_oc_Nkn-QcXO8K4hzuU4DkrJLJuhHU1kdUOz7sNTk60kXoLzTWoP_p-JFIZULWwpsL6jmMuRBuxib7kNCZImrwOQPmQ0LAP1C7yFYvK0F8r1aKXnpyyNC4ViyngqEBPM9scL0cf3QwgqAoapqsRns65rOthk4u3m6Yyd6lWxGCkRVDkUoOsg538wBZ0MxWRjLREJN_9_SsJ0djPqQYwbH7dnAqq-OTteYMVwH71-Mqeu2VVDJuAW21p9Mwh9u4-PYlvqqhSI1KKTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=okiQQiCcs089vnLOZavk-CRGrriv5OggkTUojXKceXl0eAgLWirloVbI6rX2ON_VsEpXJDmdt_oc_Nkn-QcXO8K4hzuU4DkrJLJuhHU1kdUOz7sNTk60kXoLzTWoP_p-JFIZULWwpsL6jmMuRBuxib7kNCZImrwOQPmQ0LAP1C7yFYvK0F8r1aKXnpyyNC4ViyngqEBPM9scL0cf3QwgqAoapqsRns65rOthk4u3m6Yyd6lWxGCkRVDkUoOsg538wBZ0MxWRjLREJN_9_SsJ0djPqQYwbH7dnAqq-OTteYMVwH71-Mqeu2VVDJuAW21p9Mwh9u4-PYlvqqhSI1KKTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کن برا ۲۵ تومن حقوق مجبور باشی بری تو باغ وحش درس بدی، معلما واقعا بدبختن حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84730" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84729">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdCmnjVDWxx97xfGCvs_yp1Qq_c5K-fZEOgWKwwjdcq9HsvEQeuGcSPZStoDSieouZp3yjo6YOLrMjJDvXFcBTiAB51lOIuo1j10VmXc0DbBcclJSqL4boMtGGJBCCEc8yG6TF89WLTGLjeN4-VAycvVPJEwyU0jTk8KJcz9BRFVvIg1_3yvHwvaroEZMIKgjOCcX_YhvoT2Y5ZbJB_wbFs7FpIV6XK4kOtnj019G7ur_4Whf1uV4f9KTwh4mt_jaGHHvF9SHbxNlNePhDGI4-ZCKw6QjxUeXHtqxt7iRdYFbv3VtIiXYD-4cgrwUwGt6c6t1ERpTiCFfk0d4K1vew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G20
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84729" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84728">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شاهین نجفی میخواد بیاد استانبول، دسترسی بهش راحت تره لطفا با راکت بزنیدش</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84728" target="_blank">📅 19:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84727">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نخست‌وزیر بریتانیا: حمله به پایگاه RAF فیرفورد تقریبا به‌طور قطع به دستور سپاه پاسداران انجام شده است.
اندی برنهام اعلام کرد:
«می‌توانم تایید کنم که ارزیابی ما نشان می‌دهد این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریبا به‌طور قطع به دستور سپاه پاسداران انقلاب اسلامی انجام شده است.
ما چنین تهدیدهایی در خاک خود را تحمل نخواهیم کرد. با استفاده جمهوری اسلامی از شبکه‌های مجرمانه مقابله خواهیم کرد و از تمام اختیارات خود برای هدف قرار دادن این شبکه‌ها و منابع مالی آنها استفاده می‌کنیم.
تحریم‌های بیشتری اعمال خواهیم کرد تا توانایی جمهوری اسلامی و سپاه پاسداران برای آسیب رساندن به ما را محدود کنیم.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84727" target="_blank">📅 18:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84726">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">شین: پرتاب دو موشک بالستیک از یزد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84726" target="_blank">📅 17:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84724">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-1p8X5oJmsSNFl4C_4bYQ-D-v7cGgGWsNqu5TRD9yrCvDxeoxiVDW15wRhFn5Vb2GXFwcl8xjl-3qQDTx0OFzqrg-AkXgUHSzlS3ktB-cRmVyEcxTL9_bopg0QIQX4AOK5_nnYHr6HsfJss6xp8K6EPKwXfRfbH4R29ShrgkSbK31jsTkfvJa-5fUesMZFok8l7SI4zevvDMU91HE5GTm9K3A1FqsdIHZLko8DBN8XrXqZS-gxCFaWzYru1c1-5fzj2-024RS3TRs6eExoiNiGxEn3Z99Sf7yZ7jyMh7TLyjI_2K07Xkpo3Efb4pSLtOYWZDOCFWoAOrG5TC7q7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPEYaysGJUUnBUNdJFipioGfEGaPW-QlcqzQx_2daV_D-vXTmmkpKLazl_GV3aGY-QQqKArSMgVKjxw5x9mIX7dI9e9nQmesJ4Ofg_9LyeveEHmM0L55JaaRCnsFd4kocN0g4XzAT9q_DxKIGhUZPsvNBWEhvj6y2jGOOXTi7hY6O2OyDZFHFUMKFgKmhEaUiov1cgu_qmCIcUev4jSomcj4Su9KwYDF8Gl4lvd-QnPAgmLrcmSTu3sgISGUfJmHjotkKaxg4YMVi2hYo4jLwJeNZ-MMWsSSv1UnmJKt_OZosilwaOvJ6oIXuYRg6a4JFbrzZkquCck9IB7tRlx66w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84724" target="_blank">📅 16:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84723">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=LjAS72CVpPnQ5wDdibM5mw43pBa7F6OKcJ4keE0Zx37WlrrPqEbilSYBRTvFcVK0pZcDai_k-LXfZylAmpHvaIR6KrPILzOUSW0rID_9QSoTwOCIaX99LCc9QP-E-8HVOEZb9wpdEO_5Ro7Em-t1Yp7_JnL_v36M5pbRUB601y5Mt2DjtyhLwXzlNcIwH5Ydzk-BakShJXgevszTT50w4F0vjsVkbdOecmMpsRO7ymVw1Tg6NzR1b61nOJo64wQcxLyMOs4-AAfrqijnZJ8v2McstFMJ06TzGK-hGopQraPIjpfvz4p_eE2QKRtTvxBNrTy8LvT-PcSwTbIvkMjyRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=LjAS72CVpPnQ5wDdibM5mw43pBa7F6OKcJ4keE0Zx37WlrrPqEbilSYBRTvFcVK0pZcDai_k-LXfZylAmpHvaIR6KrPILzOUSW0rID_9QSoTwOCIaX99LCc9QP-E-8HVOEZb9wpdEO_5Ro7Em-t1Yp7_JnL_v36M5pbRUB601y5Mt2DjtyhLwXzlNcIwH5Ydzk-BakShJXgevszTT50w4F0vjsVkbdOecmMpsRO7ymVw1Tg6NzR1b61nOJo64wQcxLyMOs4-AAfrqijnZJ8v2McstFMJ06TzGK-hGopQraPIjpfvz4p_eE2QKRtTvxBNrTy8LvT-PcSwTbIvkMjyRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ی نفر تو ارومیه اومده واسه ی مسیر نزدیک اسنپ بگیره بعد اسنپ رفته بخاطر ۱۰۰ هزارتومن یه راننده از ساری فرستاده، راننده و مسافر هر دو پشماشون ریخته:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84723" target="_blank">📅 16:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84722">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdYg_CjpoJrZqMBwGzEz-tgVrIF-p6MvbqeJQh9Q3m-whT2IeGNG3S6pvQkv9cse4WjgLdoR4YpBIokNHQTm5irDPUDMAbo1MebA03ySd9mh9DvPWha3ICEFpxKEuq293hEZvI820LE0WGfVnNLiEvckk3Nd-EwMzI5mosJd4Y5SH2uHc15pv2tWpkqOcEOk1kqzj7g9z3bbgZHwa1cOmPCFz_gJSMcRoTbuI9ibps-HvGZ5BuT_FtTEh-Oid6v77xPULswyZW6Ypd2sZzJQTddw18kdFznmbaBrUA4tjVYgiJwsua3HL5ewsTjNnd3yvQqCheLANxDz2hjrwVPszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84722" target="_blank">📅 15:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84721">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=sNmO205UmPeHKvdFkh9MJfYbyqUt2wCvCt42YcdFTK56ymW9qkuhVOTbIRknFpE5d5eyQ6P_8D4-ES0lTi3-MpfDFoVYbfIKAnkONoWvJSGKfp16E2WZP9aJf5VT7ywUYYyeeUD5LMLaR9DOdDsqyVVE6mBz97RVhroNPaFqmimxqxJlZuJLNVTY8bw6lgm8gr5_BpG6xqns_fBmaURSEkhPT3lLYDcoy5iF16R-SPg0W4aDZCYf9U49B7GZAA722nw48X2POApBNt4rIRL_ilCfAtz-uyDqSrR-I45aca0_kcLgfVyfMgCXQBZBhKZqpqOwAFGSXpMMdCutwiwbCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=sNmO205UmPeHKvdFkh9MJfYbyqUt2wCvCt42YcdFTK56ymW9qkuhVOTbIRknFpE5d5eyQ6P_8D4-ES0lTi3-MpfDFoVYbfIKAnkONoWvJSGKfp16E2WZP9aJf5VT7ywUYYyeeUD5LMLaR9DOdDsqyVVE6mBz97RVhroNPaFqmimxqxJlZuJLNVTY8bw6lgm8gr5_BpG6xqns_fBmaURSEkhPT3lLYDcoy5iF16R-SPg0W4aDZCYf9U49B7GZAA722nw48X2POApBNt4rIRL_ilCfAtz-uyDqSrR-I45aca0_kcLgfVyfMgCXQBZBhKZqpqOwAFGSXpMMdCutwiwbCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرین حرفه ای کماندو ها و نوپو تو سنندج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84721" target="_blank">📅 13:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84720">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نظام‌وظیفه با درخواست کمیسیون پزشکی علیرضا بیرانوند مخالفت کرد و این بازیکن از اول آبان‌ماه باید به سربازی اعزام‌شود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84720" target="_blank">📅 12:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84719">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پزشکیان : داریم در تهران آب زیرزمینی را استفاده می‌کنیم و اگر تهران هم با همین روند رشد کند از کجا باید آب بیاوریم؟ باید برای حل این موضوعات چاره‌ اندیشی کنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84719" target="_blank">📅 11:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84718">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLCAt_HZsjNHo-thkTd6QzMlxu_f0IGJ-g1RSWPZGvTsotXbva9KtL9D9VaLcs89YzaRqNpdsqR37k7_zyQvfWEeEWL1kjLUl6f07u7M3C5u_AiYfVkLuTtRAqjGnUZweSWhmGR398IrP1j6z0eQPIK354PbbcU796-9oumhXbCXSbPa8R437n0kqirhnkt0rk9R6682tKVJBHeppxcvxPaTWQ8uYE9Gg4lRqHULEobiVynGA9GZ9muGVl5wFiIxYRkiFHr0LWo99xwy5v_ARHrGwX7lIFUZSUFADCuK4ImxTcr5qfzxaZ43mhJ-6kg4BOmQlULqafmgXnMcxeuRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84718" target="_blank">📅 11:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84717">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=smbKUaWgdzPxupVr1nX00HcpdzsFJr4C1TvLzQhJdm_bFQpotV_ZN-6PhlR2_GinMl96WAFgMdgA6ErA_g0DdGI-8496qR-uTE65caJSAEXstFHOcC-TsYoK0dkM77AMB0BW--NhrCVB6Izk1KXFmQcDAWZ5W8Fll1yVH-E2Q79F41UPvSTAv9pgJVbMVoVPB5-d5aGm7vuOGY-4g5FKC-otB_xwDlx-iof-nISdUZtGMGoNgp7aBAPkm26coH0lwth2qwAcfrbw5WpaoDaZLMtLVBOzh8ceN-Yc04ykiCkFAWnlXeK5kKGfhcYjV4ophzKr85aEBNVv4Rtmt0HW_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=smbKUaWgdzPxupVr1nX00HcpdzsFJr4C1TvLzQhJdm_bFQpotV_ZN-6PhlR2_GinMl96WAFgMdgA6ErA_g0DdGI-8496qR-uTE65caJSAEXstFHOcC-TsYoK0dkM77AMB0BW--NhrCVB6Izk1KXFmQcDAWZ5W8Fll1yVH-E2Q79F41UPvSTAv9pgJVbMVoVPB5-d5aGm7vuOGY-4g5FKC-otB_xwDlx-iof-nISdUZtGMGoNgp7aBAPkm26coH0lwth2qwAcfrbw5WpaoDaZLMtLVBOzh8ceN-Yc04ykiCkFAWnlXeK5kKGfhcYjV4ophzKr85aEBNVv4Rtmt0HW_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره دختر اومد تو اکسپلورم باورم نمیشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84717" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84715">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MunhVaa11HNyrzmxFwTumkdTQlcb-w4_ZB3pxuZQjJyZ51IRTKxqQN_JHXap3eA2MaOgvWHIVynhPdyUtPLPlD09kZls_Or5npk18v8Hadjg3y1Kek7wuv8VsGC86QRxvUr8bQLlWV6JXALMHzqb8rGqEuSNd8jXj4i1ZEANNt-DPehlJjlTu-vJ_q6wEEeeNCaToLkDu4Qmi8A8cvQN8NUpEqedYWI-614bzu-uuGAK0rhfGsVE6L4TsGt2ZpTqHQzybEP9AHADfPUq8HA8W39bxT2wV46QF3fOf8MjLvX2uoA8Eovx2KgTXDb8crpfW9TyacuqItKQMmqAlkt6pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r20
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84715" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84714">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=epXqXFLrt5tyWEGb4JpxYeLhlw_4VBF0b0mj7tATmMcjLwnJraOJ5hlJBeN8kBs5kd2zo-vMGIds1mJO-jc9a97wg_rtfFdlwiDGRCPhgcOmAfAvGHwonel5IqmOSwecPAg2Jvlqf4xq63YV8sWCmwbleaJcSx24WoctekRGnoZeOg50HDMwm2IoSje25o1MFYc5aiVkR-Sz8d8RvQKaKV9Y_6vBJ50qj-NplgqIfhhEY5v10HgwQMvJzT-y91FhUsUHDMSsR6eIWJwprGF5fECLxAQUDBKrERP6drTYHgl42FSPdwv0H6dHHD13iH-dlM5_Zw5Y24-MBtDfmDvuHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=epXqXFLrt5tyWEGb4JpxYeLhlw_4VBF0b0mj7tATmMcjLwnJraOJ5hlJBeN8kBs5kd2zo-vMGIds1mJO-jc9a97wg_rtfFdlwiDGRCPhgcOmAfAvGHwonel5IqmOSwecPAg2Jvlqf4xq63YV8sWCmwbleaJcSx24WoctekRGnoZeOg50HDMwm2IoSje25o1MFYc5aiVkR-Sz8d8RvQKaKV9Y_6vBJ50qj-NplgqIfhhEY5v10HgwQMvJzT-y91FhUsUHDMSsR6eIWJwprGF5fECLxAQUDBKrERP6drTYHgl42FSPdwv0H6dHHD13iH-dlM5_Zw5Y24-MBtDfmDvuHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار دعوای دخترای دهه نودی بخاطر یه پسر
انگار یه دختری به دوست پسر یه دختر خانوم دیگه تو اینستاگرام ریکوئست داده و همین باعث ناراحتیش شده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84714" target="_blank">📅 10:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84713">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">روسیه حرف ترامپو به چپشم نگرفت و به نیروگاه برق خارکیف اوکراین حمله کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84713" target="_blank">📅 01:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84712">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به رضا پیشرو ميگن: از مسافرت برامون چی آوردی؟ ميگه: تشريف.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/84712" target="_blank">📅 01:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84711">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/84711" target="_blank">📅 00:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84710">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دسسسسسخوش و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/84710" target="_blank">📅 23:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84709">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2nILajCe7BYGtm-HhuUiXb0FB3RKzoVUdma2_SdTHF89chQGTxAqXfCiBtnnGQ-qKcFknu8oyn2-3Ky-nxVEz2tsshuHaFO4VEsnrtea-9UWue-usKa_kNdFSq7ayJgm_FVkSgpXndilAIahEC-0jymbNBkkQFkBrZRVB5vS3GIc8_LVJCTEVTH4XenqZs1C4yLQ8-VeMvwMYG2RK7U65mqofBGXN_jvCWcOcBQypiLM1HNBwH0bVDHH24ubXIdhDzgCIw36l9WsRGGeemxEP4oMhev1o1U7gcUsjGIKppNbHnTQDsCBskXxI8_GEQJs0xjD_qybgbGbJWIQkyLrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان First blood از اینجا اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/84709" target="_blank">📅 23:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84708">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84708" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84707">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84707" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84706">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خاطرات وینی پرایم داره برا ارائوخو زنده میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/84706" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84705">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دوکو خداسسسسسسسسس</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84705" target="_blank">📅 20:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84704">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmisgQe8ULd_HKaud6xoP0R6pztWfD9Qz-jrVaO3qGfDbh8YrJ7SDJdRiqixTPveIuiAJJI_jCB4x-lqA3CLFYhBYgZTTDl6DCGWz6esKqH6QrVwr6tcslK-WqCYvBaESLqj4YP1PXbWyUhDVUYadfYPxySsrhxdyN7uWmKY8h_QQbzFTi3H5kJPqrUQ5h14vOuceXrUAs-8o0zwp3oJijk5h-T9vd4uDWWY7gtR3zpaQyo_PAbnloCktfR1Oz5vI1sS3-dUjFTpUC-bwSXZSO3jO4iCTSatIXgRheh93_gNwhe20TUGGlf0E8rLGkRLonNucYSz3CSBxCipjeNw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه سخنان شگفتی به زبان  می‌رانی، ای مرد؟
❌
چی کصشر میگی کصخل
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/84704" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84702">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnEi6HVkGJO6J01o-dkBgxLnf4LdP1N35WW41-ys6Sl5D--7r2mwUoEyqSCYbEsodcgKqhB_R8801P1ON7Ma97_IeRlLv-vJbV2OMz9ydkM2BBQ8aHlnSwIrf_zLFSLiVnAoc2AmwnglOuCGUjYhBYmHngt1CZ6SvVxeASIcRJ_eYU1dDsxScwRgK5vIPxpH5xvZG50D3-9QIpDCapqqaCtTP0Gd4xwR8hp-lM0Xsxt2hU_DkGB9KccLxHt5voYekOIszALzq5c1Qyu2mVqFlhXzxikoSpdypWb_84CWQQ_XfZPdShH0VEpVjIgaI8dER-IZglt5Qd7WTOyQYXJ9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بابلسر ی کافه افتتاح شده که با پستونک به مشتریا نوشیدنی میده :
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84702" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84700">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCwLkJGAIDkIqKLZcerQkuAQbi7sAjoxtwrAVUCxoiHvCS3Vtk7usPzWVdGrF7XG8FoTrWO1cPCKH9b2j211dJZe-Jbjq8c8mGrYlTJrlPPmUfQYe9fT8MdoFgikLHmIV2rPKwl1GkiDVbq1rcrb9dGUqeH4YHL1z7AgapyLxVEe5elIAQeqDioifIoaK7FOsBKIH9fQF5yRvqA5Wyd0Rev3HRZalguL7i_-OuA_A6OzWg21zufi0r34w5ZzUWvK3hvtsdgGHO3zfxGf9kleoZ37AAnqJaek44xdQiQPpKPHxOYftAmW782rFZkYdmCNuYaC-uUUdTPHGprd2YvfCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به طرفدارا لیورپول صبر بده، حضرت ایوب هم نمیتونست همزمان مونیوز و بارکولا رو تحمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84700" target="_blank">📅 18:04 · 19 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
