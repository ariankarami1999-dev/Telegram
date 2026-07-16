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
<img src="https://cdn5.telesco.pe/file/i5kruk9pXJTOKeHAEy3brOdrH8Ko6UcvZYbY0nh2Xe4PZM17ji6NGz-NGR16jvEwAF2qFqK9fxkuYy7gFHjlN23TPdwdXckqFB-kMsl4yIZqlzuo1tn32cApPLsUK4jyCMM96UxQycpHOtmV0CI0EWHIo6ksNrfL7jrqLWgaFvuSTx0O8vqOka9bw4hB58HIKsknftNO3ph-T-rtDPzvoouKgi4gAlEoouX61kmXm-K07uZy6YBXK2CG-gKRdgOjzrMbm9Gp3J3Az1wXvafUkoUouBpJk8yaAv4U-K8N-jVy_lwD7A20K5ppOsjkX1uM-62FzTR3sPDp7i0A9VAp2g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 569K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 23:31:29</div>
<hr>

<div class="tg-post" id="msg-100558">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
تسنیم: شدت حملات در بندر عباس به قدری زیاد است که برق برخی مناطق بندر عباس قطع شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/Futball180TV/100558" target="_blank">📅 23:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100557">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kouHaaLcN5VPMoIfu7PlsOJtCnsxhgtel3rAq30x_pnjrcuKj0tMgRJqAQ3tnerVQWH4awD5fZdr3JzjfNZhv0OJA4S53PERkp7zMsKN-SZFO05fuvo0qYJVBsvWNfep1gy_h0s-M5TFNp_ZIuiYPkpVWR_jjAmycAPRhM7aGsP8j3cveXY7x0hYCAuvpkRhGBaoJ3kcQs4fsTRI5e_f2IRWE4mGkPSVMjzMOXuarMqHMc9sCeA9KNMHVZXrA8URa3jlkLNA9z5x6PXhPw6L0y34FSGa9MKQrFtOMMyITF67B5lB3-2nx2c4e6RZdbrQnMFBwV6YOcxszaZTi8xqWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
گزارش برگ ریزون RMC SPORT:
ویلیام سالیبا درحالی برای فرانسه 7 بازی انجام داد که دچار شکستگی در ناحیه کمر بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/Futball180TV/100557" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100556">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyfnjCviw0ZZTc9mD6mUPT1T_NIJ-Fx5MB6zYCu4CbvjlyQzTJ-okvJXrttH81ncwN9SlOFneteAYLDw6HaKc996VhrZe43wk1UBs30VFJNego9lH5ic9pppVzDtULJUsx9TNOfLpEJiypfwKP2BLpi2D3rZ5ehgdQAwcKacSsv1NsHH2mSxLwWivJB3bKNjlv2L9q-WcM5GuWK-5eWTNarDQ2uOEWCSqG2Lkfjeyp7jQM_XQy2ymmht78L19hiX2nA0AoxL5XbF1ZRantF6KymUsoqieYBT2xWHjYqXQvf-UCQEvy9n0OevQ2rlvJYeltOAbk25ZiJ7XLqnOtemCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🎙
انریکه سرایزو، رئیس باشگاه اتلتیکو مادرید:
خوان لاپورتا از قبل میداند که خولیان آلوارز در فصل آینده در کدام تیم بازی خواهد کرد.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/Futball180TV/100556" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100555">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=trFcvpXnQqVvx3E4MgGNUys6SCZArV0cyeYHjhsx298jTA1s6a87SBBrZ1Cec-1lZ6V-MVxF4tHl8SZi-1EDEJr_8HdRihSJaqIQUy1jCgs4Ibs2OptkTydPd9EXb4hj5zSsmZ0t5yNT018bDkCQ8llFBLLux5aYRSGy4nzBQXUitRr9Up_YEq8S7udztOcgSxs37RrbYhvwXlgP4UfSSWAcHQWotBa34dDvCgJudyM9Ig0b6dIyE2X5k3ZpjToe_bNwWM2RfkCjBqTWfBLN5l4MoFMXNji2ImKR5SZN7ZveCYfWwgqQEAUSf3qDEXp8me8n5i1_JM5E1PS-bpvzOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e16fb64d04.mp4?token=trFcvpXnQqVvx3E4MgGNUys6SCZArV0cyeYHjhsx298jTA1s6a87SBBrZ1Cec-1lZ6V-MVxF4tHl8SZi-1EDEJr_8HdRihSJaqIQUy1jCgs4Ibs2OptkTydPd9EXb4hj5zSsmZ0t5yNT018bDkCQ8llFBLLux5aYRSGy4nzBQXUitRr9Up_YEq8S7udztOcgSxs37RrbYhvwXlgP4UfSSWAcHQWotBa34dDvCgJudyM9Ig0b6dIyE2X5k3ZpjToe_bNwWM2RfkCjBqTWfBLN5l4MoFMXNji2ImKR5SZN7ZveCYfWwgqQEAUSf3qDEXp8me8n5i1_JM5E1PS-bpvzOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی و یامال تو فینال
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/100555" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100554">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBwJ1MEjZYhqhfcVp8PuNAHGJR1dEyEAyRZxSwFPISdROtDhYUUg4aOo_8xn_5Qjh8ub_Wsq9GqSm7S9ik2royYQsKELF2ZuXBClW2qDijDxK2kQUfqZqBkZ8MrKM2WIXRRR6zZnQXeF1YSTDO3OaL-nDCHM8XU2nyC0IC9URy4DNTFvU-fWfLGuDBQ0Skztk3tbSf4Cmg7d_SEu_FDpT8B86vGRUCSF3WIfeYvjUJQy_UNw7RyuSt7E_Rppj_P_vh7PPnwlzYrOiOAI6kQ8HTuc7I9X6Mm-PE9T9QHtw8wEThiMpAugD21FzvZ6JyCxdS00VImTmHKn4ubXA53PIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
برترین گلزنان تاریخ تیم ملی آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/100554" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100552">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVjippR3xz38UbuX-HiFI2rh4NKtpKZesiaUAqyi_Mo-HpmWiAU1Py6jnM-R5D_K6_PXT789eAVHRERnPOSZ5odtLVGhMQR7DSgBT550NIcsBNcpfuf0bjw--wR4lJD2OTD17r_kw0vTrr_lBxY7dm-ZPWltl9ti6cNxwXeS5_uAlgp_-JgJ3hGKvPJzmgLZqeLNUuCzD9DeDNH26oSGXTIQPsvMAP0nCfmdw8IYiygBNXWt5L_PTuEzYM6NeXh22OFhMBVBtecFJwbs20i5zszahXqNKudkwb-MkcjVmYV6sE13pVsEspYZCdEi37tmo2D11M8GciSrSQsbEOsEUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IISK3AL1vEq_m3ynI2TJez0RAJ8GbYevJZDp1O7D1vcEuA-4vC_nAgRKdJL9EyKK7y07Qk63IJPVKEBbJrx5QQX35oR0E9b26zt6xyKNdQZaUS5KKiPxQvywuDdYEQpliWXjzQbfppBLQe0pF1hRGPrpZC6v5tzrR-b-OAGAQpy-IxulnusEiWyr7vFnMHGW68ECxijoxWyqpeUubVw6VleA4Trm1lXDsmhHdjj3vw67EBkkFnHcn3sGZNdiEgx8wFi1WxM7bOTtteWK5es6tJFLv05vvxF3R8CjLqTHMbO0opo5OTMTh0XQY6r8ayXqi8YBNFP2gvjOHkQpXkhqKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تنها 2 بازیکن در جام جهانی 2026 بیش از 20 دریبل موفق ثبت کردن:
🔺
25 : لیونل مسی
🔺
22 : لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/Futball180TV/100552" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100551">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFNHHt71RmAla-b2kc7o5AS3dpsGvuy2VD63ls3u60P0FsWcnDnjEB-C9_q_F7WcsXVx351Z8xyFiL4ceDPL2JJw9EjaNA6py0s8WGBWeYCvZdPumPA-UvmcOgCGAWFr8VxRAbMdRiUy9220fXhej84nb2Uvz4iTcJnQhQxtQHbQjbJuS5RQxL34lv1ieYZxrVPpw-mt6KKeAnSMCW3XAScq_DlmF6IGI03LCQzzp6FKkKtwk_mGXOTjTlg0E-Ok3VzGUJ2EB96YMZIAyNTp5laEg7UErr3KtdC_CwY3wPJQHmmy0L5QQnNykSikGciVwd3EnZdFRtp3qZ8pFRI-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/Futball180TV/100551" target="_blank">📅 22:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100550">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UiJtO1h75nygjkaV1UCPBgnuWJqtRrcyymghxC0xGHmD0O0lX9R-VbfnVONbj90noCStYHwi8BWQ1mhhWR-wjckiM5ZtprGk3rKxZTpXx_DVlGhCAUrkHtF1uToZ0Qr4gap4fNiOwFxobye-8b0LRHDGp8zX-_nTMjslMiS0EIjDVnT1NVsTS7RCnQBtffjE76S_stZakf97XDPKN9RTw15Bxcm7Wv18JxY2fwFNSZSQ218wSbcDmabQTpFv6pCNgHLpXk2CfrFrBTZTcfCmHkYNFTlwGjMIADEbVphSqDsSWSKyPoovFc5Qkhf1nwslXzrMSc4cWAtRAzDPR0xnUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
فابیان رویز با پاری‌سن‌ژرمن برای تمدید ۲ ساله قراردادش به توافق رسید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/100550" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100549">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGj5895lr25rK21mjYXds9LkYOuWuF05-c9COGBllDyfLif_X4jjWj5djHXFCyWs6Py0Bk3Yw-NthZYz-_yY1BIGGXp7z08oEvw1bw3FHacKqRSuXDUvegliTiRpBzoziUOEMZF-nqxsej6t2zxe4go-Q4e2gBcIlyCucMXh31iPdvt-8zuggj9ecdvv0a988FGY93vzDT4DZbjOnxrXNsWA62eCbvtWhdS7KHeqqCQIYsF0FwqOoOvk86b_L53MpQHiT8FmwGYDrEmBdg3VehjaKOnZ0QGnMry6_-cqTcbiZg0NYkWVtrp2n-PyXelgdap9a5tRhzzUj2QOhUixzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام: حملات ما به جنوب ایران شروع شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/100549" target="_blank">📅 21:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100544">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQTiNbsGaK1joQfnMcGhtNUMnhKyDkEnlM35PEtcRE1DmJjMaMTg3krf87S05S8bRJj0Pe82BiKMWkvUTHg3vbbyVuPqpAsI2AbyvBez3YEYFDRxN2smAjEOu02PPrMgtvhP7SkCuOBVt73BuOvQ2P4e5lTzyOJfSoZCIghJ7GZdg3nJreJkU10xPsUEEehSUC9lui9CliNhrjgSXCXousX8SxouVX0vXKX5h9yiOG8CsqImhC2W0X5J7wsgBy-ODxlK6oGRA8qtN0LLNBvjgr5omBAB77KmtDU7QXFRRNEODYq_PyMGIHqPsr3MZ1QVa_jU8YWy8PfVcmge0xJ7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYYyOpwxqmD9XmOTvfcO8PibB_iBhR4n65Hes1ewXmry7vxvEsitZrr_Au5-h4PO1_esnJR1Tr3NE68pjj7ZU92X3F8RVg5NuvL-6Hdw6W0qEHQunkOYYWX-dfA5GcarPjFu5RG4nfz_sS8kGT5nWHtDyShYJzq7pZag2r4cpgSMHkNvI7_fZGyzBEexJ9YepXzAT362UjnHT2EpNhMk5soDn4OAUDq3PNXysq9R5wgs0fKjjKfABtqRDLSjx6hAMz0B9Ui6IfPTe4nyJLyWu3PzfqKJYuqMdkSpNk4dEPUJxWYE4CNgoctuBGIAnUrvqi8uTgGvvUeolCZha_32pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AZG1GpIP5yNp1ViB_UOUca9RwUMlexvOHP3d7gv1BUmXAWAfcLnVBT5r3Y2Lzk8HnidaMmmXbt8GMaWALB9L2suZTnPw37-9j19OAAkbI4nJtkQ3uLpuc3k4zaagCR0UmabPeqFrFQ8BKVkkjzuaPW6gketIbefre_-3c11BS-sA6WwB7VNhzNQUM17mUz0TscRhyqYkLKSa6fAuSMhfbAgC9kIsyjt-CZdKPbzzSxRCZ51C0U9qGQFiRU57NbN3yNj6T7t0Su5KEmgngAfJZi4WFAjZY8RWqxaxcGnq4ByLJss7h9kvn4My8DqkQPYzpAsRgbRvVX5i5Zv0d2SNjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KOgaJ9-WJHw1AlOTuvQoGMcj7YLvw3vy0fC7ectqr7xiEaDsJukNYeIjeYHdhoN3vO7K-QL_woI3DsTpjF58FbbMs-goWTB1Rto9PaiWsmpj5aHxtdAoGJw9FMZcbWXzxbquD4mvy1uYgX7vcvaiPjGBt_NJZEKljzsEREdZ6amJvCkdkAVOUk9d4j9ysl5eK6dU_9jxYPqtk21h5IBKU0p_4sJNM6BMzFvTRDj25hqR4yN66wh9NAspxgj7CiryuxvtAzjIUVRphMlOHuVMmjPMgFVRqyYdV8D8p8fmmDBNXEMHwPU2wdtk82fnDDKnCroZIwHcRtM266oWZDXtig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s7z1zp3UeMxFLufHIowzoRHOKuzJsnCM91oHWC4DCUVVffPBSGx7wm-g6TP2e87roqt9ns0ZYgtLn2t_tztJXWjx08B6UP4l0k4w_T1UlgL1mCeoYXRknrVa0H45H1COEQYAK3YSAiqKjQ-cxH_2bS2QAkWjiexLlFKjN285tMElOHwhcjSqnfXopV5YBQpI7YXePJnLSWGNXb8pjeQQFDEULTPOE6B9NqJCL4NUpmvXHHBDSqJhpSiPC8xrJdTt0rcEFgcmPo6U0dQ1WzZidiwUxddehYP9vmXQ7Vhqr8vAYgDmTK4jPAnQ6qA2AF4U7pBd4H6TvjMvF3M299DCCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پدر و پسران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/100544" target="_blank">📅 21:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100543">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWqP7m8JtSBTujbpXqgJxB8-r50fS364jV2jg1Al2qqjusGGFpHRhkEpK7O7B13MCRMO7f6pZz-k2vwUDxaBlZyp11MAa06y2d4EorHIi4pd5uu4cerlD5k9hKt7-bVXreaU2aCMW6-XoUmUR1tiiO6H687-NhkurbIf0axaxQS3U7-v0ANT7sQhTBIYZPbXXPxeZCASLJfDSpyXNIh-lpV6mxR2E4Z7N1l30a3rAfz2JU4bBgqFNMjSLbCtwvHK3Z7cZuzKpbOaU5JGgkJN5dqTmbrBv7D_nQo4VlmIi0QvovMZdLCGPNZLeAFIn9GFkLLkihDYxqAMmP_Q15KlNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
اولین بازی‌های زین‌الدین زیدان به عنوان سرمربی تیم ملی فرانسه:
😀
ترکیه
🆚
🇫🇷
فرانسه — ۲۵ سپتامبر ۲۰۲۶
😀
بلژیک
🆚
🇫🇷
فرانسه — ۲۸ سپتامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇮🇹
ایتالیا — ۲ اکتبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇧🇪
بلژیک — ۵ اکتبر ۲۰۲۶
🇮🇹
ایتالیا
🆚
🇫🇷
فرانسه — ۱۲ نوامبر ۲۰۲۶
🇫🇷
فرانسه
🆚
🇹🇷
ترکیه — ۱۵ نوامبر ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/100543" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100542">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTVW_ptTYArGisGTfecCaCx-ZrFhwOLM84ZDabMyt0FXG40xkl7MJBIhhS5U-8icRZ0cBuDYe9lJww_ZMlIj2eyGfaMBM-1AXX83WF1LsMUPDVl8oQqFnpnAGtQLbi3rz_rYJ2awqwYl0lt5TIK0KjOEHjvbvG1bqZdOEK06eKQHy7G2WQYRqX_EwAtteei0DMA-T-lBeE-NRXrF5EHGG9xEm13BgV-S1_8zCjv0pzIk4tQ3CaqW5nek3k9xtrcr_doO7a07E1wvzawhxx5oZqtq6tdjgtoS7qck9mxHNEvQ5X3vputsQ5mowUI7Ed6-uIzOBzro4BwB8oc5uVw1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
خبرنگار: چه تیمی قهرمان جام جهانی خواهد شد؟
🎙
گواردیولا: بنظرم آرژانتین قهرمان جام جهانی میشه چون حضور مسی در بالاترین سطح آمادگی، یک مزیت بزرگ برای اونا به حساب میاد؛ مسی همه چیز رو تغییر میده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/100542" target="_blank">📅 21:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100541">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=DBjs-n6yIBclHkYiY1CUDbu_8Qs86q_6pl7g15lhj7Y3nobZ6qNfL6vHS4To05ykohr4Lca0npo7rmoyEbmn54YOUlGj9v0lQPXeWRL4ZhzY4m36kXXg4vWweNBveLnzY3s_uTqfYRIg8CWXfK7EVkvzr8JObLcOejoAnNcYKYHH6SDgarrnqQiKU0Yh2KW8pXuUupt4Yd9XYU6OwqyjTZlEuA0fuOItUovaIy-WtMlaSJA9hF7FYrwiWmg34Pg78asfbTdXoinRX1GqAU-gB4CCr7coxBq_TTKewfYO6mr-JX9admGsJGYAJTMroF4o7pSqGYcgUPTlT8gE_nlRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0ffa0ac5.mp4?token=DBjs-n6yIBclHkYiY1CUDbu_8Qs86q_6pl7g15lhj7Y3nobZ6qNfL6vHS4To05ykohr4Lca0npo7rmoyEbmn54YOUlGj9v0lQPXeWRL4ZhzY4m36kXXg4vWweNBveLnzY3s_uTqfYRIg8CWXfK7EVkvzr8JObLcOejoAnNcYKYHH6SDgarrnqQiKU0Yh2KW8pXuUupt4Yd9XYU6OwqyjTZlEuA0fuOItUovaIy-WtMlaSJA9hF7FYrwiWmg34Pg78asfbTdXoinRX1GqAU-gB4CCr7coxBq_TTKewfYO6mr-JX9admGsJGYAJTMroF4o7pSqGYcgUPTlT8gE_nlRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد شریف روزگار
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/100541" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100540">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا رایگان میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی  @FutballFuckBet…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/100540" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100539">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avc2TuMfX7i_Om908cklYHbQHZGv5ZHhHDbOjHQadZKRVNmWXIgzTYcct3-3OOykarCf-KhtYo43BkihZPGVkuyefekumrDcmIMVjSDA4iV2Ev-TOX7vuaqyJaaa2VvNbXUICSYI0DUt8Iz1h7rpvffyeveAV0uAMhQsqrZz909xpWkboqrixVKMgD0kkdZLHS8PIB-Bbhgq_mTOvenjy8d5-zo_uFdYT7HxZW2VIo3vJ8nI5ZVNkLkD4w8AWj3hC063_Fyfds5F_rpowHlP9xAJ10IN71SDy_MXPYOyBF811rqdUR4esgDmfaipysNydunhQ99h_OxWamkti26DaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرم هایی که چنل های دیگه با اسم vip ماهیانه 2-3 میلیون به ممبراشون میفروشن رو شما بصورت کاملا
رایگان
میتونید تو فاک بت دریافت کنید
💸
🫶
فقط کافیه ۲۰۰ هزارتومن اکانتت رو شارژ کنی و با مدیریت درست فرم های یک روز فاک بت رو استفاده کنی تا نتیجش رو ببینی
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/100539" target="_blank">📅 21:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100538">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkJCsgwdyG5f-Y-ZbHn9HU9-yX0l7nF3ccSxco2jxH633mu8fiEIyh6a5LgL0JBRIhrQkVm-tHhVQzTDjNM8IiX2RGKisLoNYQEQbyhMdCG7aB8-hbgE7H1CNYVtCFJqubuwJ4qPLQDbc5ZM3e06eFHXKhgMoNSSBpey0jW8EDqGgFjAl6-aYPBDXuMvp7aIRmgCQ3YTjUxviCDlztdSZzohLuY9KwcQHHGnzkrYiCCHZn6Ww-hohssdl83dG2e0M_6vcfY-mAHer0e-R71X8-ykiHCz-Fguyrrhhd-vENDbrdMonqP6iT1iZRaJEzvYg50B0k6KZjQBNv19A6jASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇩🇪
#فوری
از اسکای‌اسپورت: اولیسه به بایرن‌مونیخ اطلاع داده که در این باشگاه قراره بمونه به رئال‌مادرید نمیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/100538" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100537">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CudcaN-6GvW1Botd5lOg7X888ZJxfL7WL2maOA9g7jrY0rUIHMS_poGOlV3Uqbamocupg_Kwez5Z2w3KbVSpOTJxoHe5rtG-Lt41hisUDh6_nNqs1O_XrWamfxx2IVtahuRqu_jHdwWXuSomXetIZ06JXaw24tjDZ38aGRsd7gx31Ko6V_GO2DBDhiAruVznnD9DawrNX1Km7KYX40ppAI_jH7eK7H6_RNDDUCPjyYx0_8cbWyk7K89G8FJS1UTAMBX0Ex1KELxAOMFmvrdYaTWe9Ko2a_pSAigax8pwjlv3teIXFGAZFvoLCD0uHPpht1T9hUUtGROhg2lxDHlvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
یه‌کم جمع و جور تر بشینید مهمون داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/100537" target="_blank">📅 21:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100536">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🏆
🇺🇸
سخنگوی کاخ‌سفید: دونالد ترامپ در فینال جام‌جهانی حضور دارد و به تیم قهرمان کاپ را اهدا می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/100536" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100535">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378abba176.mp4?token=fQTRQHmSGt7pTsLLsQuQcdClPKtHbB_lg01aG3sYk5nHVUdeoy-vi93TOuOsobrRaM3oeexCTzp7J-1Rr2CNg3JCX64JvK_jDyrYrANWouEXt6XrEFK4rD0Sz1jfvDCJ7NOjCYb9pdMMz8VSQqVp3WeYDColDieywm2B3Q3fQA_AZd-X2M81mqsjhFjF8iu9ywVmWznsoTzxeBwOgOcYIF2T33QPnpiCIOQRcJu3UnkZYLbW4tC9B2lt9YY_5uoZwmmcgMcY9N2meQY2iIL2bddwgAvGAAeRZBPPjaOz-w4wUEtAPgB90uYGpau313udsYzYHsf3b5_EvCU4AzHBYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378abba176.mp4?token=fQTRQHmSGt7pTsLLsQuQcdClPKtHbB_lg01aG3sYk5nHVUdeoy-vi93TOuOsobrRaM3oeexCTzp7J-1Rr2CNg3JCX64JvK_jDyrYrANWouEXt6XrEFK4rD0Sz1jfvDCJ7NOjCYb9pdMMz8VSQqVp3WeYDColDieywm2B3Q3fQA_AZd-X2M81mqsjhFjF8iu9ywVmWznsoTzxeBwOgOcYIF2T33QPnpiCIOQRcJu3UnkZYLbW4tC9B2lt9YY_5uoZwmmcgMcY9N2meQY2iIL2bddwgAvGAAeRZBPPjaOz-w4wUEtAPgB90uYGpau313udsYzYHsf3b5_EvCU4AzHBYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
فنونی زاده خطاب به جهانبخش: اگر تو ایران بودی یه تیم دسته چهارمی دنبالت میومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/100535" target="_blank">📅 21:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100534">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=oKRM__4feNIwo7uJ3RLNz3QSYPy-sPJYGbzagpBU0R9-fBzp6cKqCWe8KrRL7fY6I_PNAJbCrl5_e5hVcFJwxsEN0T6MPTxGBRBxrYzlCRXaDDS07oIvrGKZl2b7CKUEeaT7B2cnY2tBSvMuWb1fvgHLYsr2pyJnFkn5_zLVn8WwgQ3O79n8kK9L4SL_F89CM486bsnX-x53RTQQbHr1xZE0Pf6F0MStvgH-gW7L-Kpwm0waHs6sfxAeLnfQMUJOQwOSvrFMJjMCaztS74YwHQwYzEoR0UwknQ2x6WRzyUHwUEjrC519pJkWPMQEfAhGiwc6cfsPI3Vyt5vhAxWceg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fe3526bc.mp4?token=oKRM__4feNIwo7uJ3RLNz3QSYPy-sPJYGbzagpBU0R9-fBzp6cKqCWe8KrRL7fY6I_PNAJbCrl5_e5hVcFJwxsEN0T6MPTxGBRBxrYzlCRXaDDS07oIvrGKZl2b7CKUEeaT7B2cnY2tBSvMuWb1fvgHLYsr2pyJnFkn5_zLVn8WwgQ3O79n8kK9L4SL_F89CM486bsnX-x53RTQQbHr1xZE0Pf6F0MStvgH-gW7L-Kpwm0waHs6sfxAeLnfQMUJOQwOSvrFMJjMCaztS74YwHQwYzEoR0UwknQ2x6WRzyUHwUEjrC519pJkWPMQEfAhGiwc6cfsPI3Vyt5vhAxWceg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🏆
حضور تیم‌هایی از قاره‌های آمریکا جنوبی و اروپا، احتمال قضاوت علیرضا فغانی را در فینال افزایش می‌دهد؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/100534" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100533">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ChVirtynu9SG24l__Ou31zwn9rKO6wmb2LEEYZzW15glAvOS-d7gl3Cs0nMRqWou84-U6uHhMpUaxBtHaepKJOljoLkaeg_Cj0D616fR7m83jPg5mD10MgtQgyxvLWDJ2P8i5si0iyjppMtP_IGzVsEpQw5yhOhCM8TwUy16gKyt0eM10Ej91QP6c_abLYuDqwys1hI0FjLSDI5kOWhISOF8kztBPNlXg2Sd6j6LTtCeTNoziKNKLsANAUPvfWxjPXZa-Vgt6_7pxn2HcDWQBfM0hXtFv8lbF-77aTzkTVx_DxT0fst-WRMYevvcUKVfmwvoUBLaQnr_7ENLmooTWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/100533" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100532">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/735694936e.mp4?token=px0rgKq1lyIfm8E1_QcHlJ57_ykxWk6teAK4_GUnRjwyKYf5WXDTjqXIxpDSnBSVxQo4jRDtuYxN1JrxEoEWNHXPgQTVpZVD6Cv5nF-OioFKY6kmArZ3e3-jBk6rzQzl5DNzp06Vh8GqOhhRycwCYqfNr19gVMu1bJA8OfWiQ2d0Xx5FJXdWplCoJCb1vOv69bdHNzocdr7jq96w-Ub5KPG03xO18_qf6bC4-w0LqnQLkmFm7J4GXMWxvmh_qjg_Os9g-Xb77VoGPEJI5pMsHiUvMHqWzH9SSckCz1RC9bU9R3SyYEJXRX1xLu2azzoRjDj1iMvCiWoRtCe5v33aAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/735694936e.mp4?token=px0rgKq1lyIfm8E1_QcHlJ57_ykxWk6teAK4_GUnRjwyKYf5WXDTjqXIxpDSnBSVxQo4jRDtuYxN1JrxEoEWNHXPgQTVpZVD6Cv5nF-OioFKY6kmArZ3e3-jBk6rzQzl5DNzp06Vh8GqOhhRycwCYqfNr19gVMu1bJA8OfWiQ2d0Xx5FJXdWplCoJCb1vOv69bdHNzocdr7jq96w-Ub5KPG03xO18_qf6bC4-w0LqnQLkmFm7J4GXMWxvmh_qjg_Os9g-Xb77VoGPEJI5pMsHiUvMHqWzH9SSckCz1RC9bU9R3SyYEJXRX1xLu2azzoRjDj1iMvCiWoRtCe5v33aAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی وقته دنیا یه خوشحالی از ته دل مثل این صحنه به ما ایرانیا بدهکاره..
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/100532" target="_blank">📅 21:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100531">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BKsxqecPzWq0ff2ISlxm217bMDD-N1Stu7KHDK1Ibd10PQMExUbj6opnP5CR0RNrrKxPRg3ffRhy7XVPhW4tlqCk-wqkXc0DuoJXh5hAxa5prufg11ScX59DxLUIwoOQtKH5E8KZ7AECPqL8z0vgDU4YSWi0FlLFjZBhJ5H5jPbCGsHf2KNT5x8Mzr5V_Wz-NQrDolwVN_tHZpuHfPYzT2SD1c9WjZHEAWInmPf68ECLrTsGxg3NKq4kuD3fmHxay4AeBrnXqAQYO7B2iE6Xr2rubFtlgzyQcfnBT3pEemdA-RdEptkteDQXIiMQ13H8xdEPN-hrGcH3aLbliadz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فابریزیو رومانو
🚨
🚨
🚨
🔴
کریستوس تزولیس از کلوب بروژ با مبلغ ۴۰ میلیون یورو به آرسنال پیوست.
𝙃𝙀𝙍𝙀𝙀𝙀𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/100531" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100530">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6JDy3hkKY_gwM3i0OYMLca4mHZabkJJLcTNsCEzyyxyZwHXwEbAea3fZeymR40TN_Ov7mfzZxAAaFkkUp-I9vFayLLMqngBRN2gHrwM8zpo5cjehjSpaJGCDtqUTqtJRSRCPM4yYC98dm3o6gBk1dt1CZLjJ1Yx4KimNmo-0wDX_NqIzqchgZ0CQo7pM1ZF4-a84vDdzGtHcDNQSJniETUJeWJqOhHmipe-GA-hEbZV8IYAHKm2kwayHCvaKXOiDRCifDZJl0-sFJE5e9TK3OgywkMXmh3zjAY4_cb9wGAaaplb8iCWuBJzpm4ursNHJPswDMxoF5Le1UuTaUvmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
لیتان، رئیس باشگاه لیل:
🔻
ایوب بوعدی باید برای یک فصل دیگر در تیم بماند چون باشگاه لیل در لیگ قهرمانان اروپا شرکت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/100530" target="_blank">📅 20:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100529">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">لیگ ملت‌های والیبال
ایران
3⃣
➖
2⃣
آلمان
🇮🇷
25|26|18|25|15
🇩🇪
22|28|25|20|12
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/100529" target="_blank">📅 20:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100528">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=pd3PeXtxeIF7g2Xaul2SfGynMMFuWx-t9OQf36PwmzW287PGZ8ktS35oFf4KR_klOSLVtmUIB_9A5U-tCWbGhjplPmCtORi53FZktUiHPRAsG2KeMV6g8s00E8tYZJuoGnw-m-q5t3zUGTN9UVsPCTDKaWRn7tQi70ZIackf_HVzhoo4g8-R0S7Ipcacf7a6iyZIzZwLQlhvaj-NPbhwFAhZV6XCESb84EDiPFq77gSCCR6zniWxttakADxh70LpzaQsEeGMlgoz-w1FIW7tXSnU9sHePgbbPgB08Ohiowi0GeieKHiCJRi_kjnKHC6vu8Z-9kC_tSvsYAvaEjqiJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec19c4e50.mp4?token=pd3PeXtxeIF7g2Xaul2SfGynMMFuWx-t9OQf36PwmzW287PGZ8ktS35oFf4KR_klOSLVtmUIB_9A5U-tCWbGhjplPmCtORi53FZktUiHPRAsG2KeMV6g8s00E8tYZJuoGnw-m-q5t3zUGTN9UVsPCTDKaWRn7tQi70ZIackf_HVzhoo4g8-R0S7Ipcacf7a6iyZIzZwLQlhvaj-NPbhwFAhZV6XCESb84EDiPFq77gSCCR6zniWxttakADxh70LpzaQsEeGMlgoz-w1FIW7tXSnU9sHePgbbPgB08Ohiowi0GeieKHiCJRi_kjnKHC6vu8Z-9kC_tSvsYAvaEjqiJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلینگام، درباره بحث با مسی:
هیچ مشکلی نبود فقط داشتیم درباره صحنه خطا صحبت میکردیم، خیلی شلوغش کردن! بازی کردن جلوی مسی واقعا افتخاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/100528" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100527">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW0TXqvaWIK7YD1EQJhR2QNUN7eZhbkSEV9Rdj1HNyhSIrM7CYlBRI-maesoXh73Eqk4FLn5DVvTGWHMZNtHI__RTopQiRUv7egFHRY5lCRgEHMIjcn6FYvcurAtJbF6g6w5q2DpYJQ2sh1D7EIRFK1FwoaqJ7SdvxLC4YaE8EgG9n3NDgcKQMkqKf5EGke-Hd8frGMeGIKhdH1lA5LdIR4v_drEyOAJZRNsTuS9m7ur71Vq72SSvbPrgm5qjPdJBTu8tIZPRRDYpJU8drVMj0RM5tN2UrIk7ECm-LY7F_ASc5gY4GvS1I-lLSDdbNrul9X7OOWEdV_z04sAA9KurYkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f42b6ddc.mp4?token=G5zIT3nfk9jtnu6KsXyVLUDLN50jQMNhOprP-CYbadA-4ov4qzWdVBTCSk10u-oRzBkJOk-gDHtObLfJjYOQTL51xicEkc_NAMkLkRtRgKmOyAO9WfHAq4fbxAKA4dPen24FMYxmZFP5w-1aFAluIHuXnN-_uRQXeIp-z26hfou6ClCtITLhx_SCCkGVUHy3yTEE4SpdrUTYMNDcGv2f9Vdocx5l7UFr0msf6jb13B4_abcRLkN7JSEKE-uepAFoV2qWoTOU8yB8LR8AnIXNgzkH0FA-ANsnD2WbjdyothVHBKU4InrUMvov-ffwbAm1IVugK2_Ct7VB0DEFY0RYW0TXqvaWIK7YD1EQJhR2QNUN7eZhbkSEV9Rdj1HNyhSIrM7CYlBRI-maesoXh73Eqk4FLn5DVvTGWHMZNtHI__RTopQiRUv7egFHRY5lCRgEHMIjcn6FYvcurAtJbF6g6w5q2DpYJQ2sh1D7EIRFK1FwoaqJ7SdvxLC4YaE8EgG9n3NDgcKQMkqKf5EGke-Hd8frGMeGIKhdH1lA5LdIR4v_drEyOAJZRNsTuS9m7ur71Vq72SSvbPrgm5qjPdJBTu8tIZPRRDYpJU8drVMj0RM5tN2UrIk7ECm-LY7F_ASc5gY4GvS1I-lLSDdbNrul9X7OOWEdV_z04sAA9KurYkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی دایی: «ما شکست خوردیم، به چیزی که می‌خواستیم نرسیدیم.»
کریم باقری: «همه طلبکارانه صحبت می‌کنند، در حالی که هیچ دستاوردی نداشتند.»
عادل فردوسی‌پور: «چرا باید برایشان مجسمه بسازند؟ چرا باید درباره استقبال از تیم ملی، واقعیت را وارونه نشان بدهیم؟ ما هیچ دستاوردی نداشتیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100527" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100526">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFQjvSx_g1kJY5aSN5MLaeHM1SvxQL7Ztwg8LLqvdMJ--hSwL4VC11kaXWrkyQHpJyOYH27nOKVfEPieaRv1FDydqqPK42qHm8sKgvRFn0X2UI8Qjr1qzaoFeUIIlzU8PNswI-S_Ho69E_Pwuflr8k6Tz-uIXkfiI1T6ijb9YK5Rq0NZsK808X5i0R9XJ4CqXGpZ76CeLzVXEsniHihBFNK5IR9kCwC9z_thrTlB7c-JW2CXjDZkV_VyJjnFqW4KHtf4Rg0-UxNPs0XY0BZibzkYMqKEgdDadMxNGAkpI8lu7MbsKRMCHvHNLObx7smbduOzb2-3ExCpaDiBSkCvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">�
جدیدترین پیش‌بینی Polymarket برای قهرمان جام جهانی ۲۰۲۶
بعد از برد ارژانتين در برابر انگلستان
🇪🇸
اسپانیا:
۵۸.۱٪
🇦🇷
آرژانتین:
۴۱.۹٪
حالا نوبت توئه؛ از داده‌های بازار ایده بگیر و پیش‌بینی خودت رو در
Betegram
ثبت کن.
🎁
۱۰۰٪ بونوس رایگان اولین واریز
⚡
واریز و برداشت سریع
🏆
بهترین ضرایب بازار
👇
همین حالا ثبت‌نام کن:
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/100526" target="_blank">📅 20:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100525">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zetqpj2MR3DFGKyQ_rhFtzPdwvWiIs2B8e_FGOBCcZdK8qOH7BeoAarjjQk8qWCOKj2ROEix5SUxwHcSZFnQY_tiKnGxz7SYrDfWpNgbc-_nkxuh29gt_q4CziAWiiBkePDPyOzJuuhXicAxgUC4JgOR7ni0f-taUL-rJNYMxKl5qHKycWv5Ng9hF4ztmaeEcIX8FBY7lcuouOJjixh58eI47_0xSaSZy1fIZxe6RU9REWD6Svj3inSGGneXiiPYfp3K8C5uZBFjjaKeg-Lkvw-bFefy96q9jwZOA4aEAiuCsK9dGCrzAJhpJkPs79XPokWFFc0Fs3lorox8-HUjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عشقتون تو تمرین امروز تیم ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/100525" target="_blank">📅 20:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100524">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=D64OC4vwH0sevomgTLlRf6y2Bi8QTrzMEzosdNdDOe3kwp3v1FJzX6ogCJnSIVSQuYXWDraQT7zbCiAmoH8V1UMMJrg2Hnvqs1n4ickiqeQ6FylqFB7NAv69_-jveOXRjGMe4DWtR_NnhRIijLIcb1_nBid1JR_10s8zumGJzmjRz-DmF-r33YjNELq1qcMUdntigz0YeOe5eXldEmCcTI-CiG_Gzhen2DvMkZxTlFzQLe6USmYqQzSIe8sxzPZERL1kfS1oxX3eZ09hCX-f5SGq6c16Yl1Kb1Uj11mb9Srz0bLrqJO47eO-AsMN0bY6d4y0LxhU1kke9zdV0acmtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68c789aa9.mp4?token=D64OC4vwH0sevomgTLlRf6y2Bi8QTrzMEzosdNdDOe3kwp3v1FJzX6ogCJnSIVSQuYXWDraQT7zbCiAmoH8V1UMMJrg2Hnvqs1n4ickiqeQ6FylqFB7NAv69_-jveOXRjGMe4DWtR_NnhRIijLIcb1_nBid1JR_10s8zumGJzmjRz-DmF-r33YjNELq1qcMUdntigz0YeOe5eXldEmCcTI-CiG_Gzhen2DvMkZxTlFzQLe6USmYqQzSIe8sxzPZERL1kfS1oxX3eZ09hCX-f5SGq6c16Yl1Kb1Uj11mb9Srz0bLrqJO47eO-AsMN0bY6d4y0LxhU1kke9zdV0acmtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
❌
لامین یامال در تمرین گروهی اسپانیا حاضر نشده و روی ران پای چپش بانداژ دیده می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/100524" target="_blank">📅 20:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100523">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGA6hZxMJ4gCXPIX2Dw1YD1cxz2BauKCxbAM13joTc-ghNzNP-5nEYDVIXjH5XDq7Sq16rZwra4jtuvWuZQ2xrnjl4AKJ83uvBZm7xRkx1gWbO5FwVVECgETpQ9eeDAZ9EoOhbvdvswN0_5MWhowfJseyuLOGKh9vCzyrLDskD0HUrHh6w9KEvPOFSS-kdh_TADhTLReacJKwpOppDDZMeGC4tkybuGJax7H8qyHnLow4r3NUnmYWNU4hlMxGifR7RT9ZwfGJtHhYWEHc2XxcHdgmr4StvkY4yJjCzw97I-pwCOwWCma8ri3-XcwGLENOeQsnbd-OMDYMMaiHUVZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
#فوووووری
– گل
:
رتبه‌بندی ۵ بازیکن برتر برای توپ طلا تا به امروز:
1 - هری کین.
2 - اسطوره مسی.
3 - لامین یامال.
4 - مایکل اولیسه.
5 - کیلیان امباپه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/100523" target="_blank">📅 20:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100522">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2tZE_riwWByK8TkFDsLh5cEj1j83F86eJHwg01kla4BlGucp8JECexYkoYGOK6uoW1OT6RiZUDJ7wEfRKYA-TLVzWC5nNqwoSyzOvgoY_MuGNB3p_PqYs5PRCk1pxbFw59c5MjZvAsFZ8ICuR_O2HJbYnX45Z3rH_ybmzqxqDr0v8kmPL-J_LUIqc17C9AlnqQMTuhAZleC1ldC0h-v4Mi-7tmUKHuzUBiKtCqTmwuuMDQvFModH0wJTtT8QojpaNO2zxR0NSHcAUSHzX8gaSa9eYStXFknWU_07wm8Ol-Ap3nwLBQg1yMUO1QUgUeDFfqhq_QWthjASSW1mcFaMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
| مقایسه آمار لیونل مسی در جام جهانی 2026 و 2022
غیرقابل توقف
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/100522" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100521">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=doxBXeMA0J_JYJQBW--vrggDjle1Tw6iuDorJ6btCo1GMllyWI6_VLAu6ZjOoQoRWZU1s_X0HFLvLk2X2zoAAzSMktlWvnx66n6lFEQ9ciOk9GJFkklvklAjXyVw5CrH5jN228VrOzVLplB4cfN0s3b0GXutamao3bpXp_AL3lBD5jw_gpi24ddLWZiKw6iulZ3Hy3UFqs0O8Q_9hGdbdntH-GdXNIypMfVS3Mkjb8zgP8_3ud0vjTA988cpcj1So-90XfaZC0Sox9I96SMX-BKmb592YCW_pHpl1plswunfw6rxpW7cdrGW2ZB20X4J1xY7p9gR0QrN6d6um83vMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62c9ac7d18.mp4?token=doxBXeMA0J_JYJQBW--vrggDjle1Tw6iuDorJ6btCo1GMllyWI6_VLAu6ZjOoQoRWZU1s_X0HFLvLk2X2zoAAzSMktlWvnx66n6lFEQ9ciOk9GJFkklvklAjXyVw5CrH5jN228VrOzVLplB4cfN0s3b0GXutamao3bpXp_AL3lBD5jw_gpi24ddLWZiKw6iulZ3Hy3UFqs0O8Q_9hGdbdntH-GdXNIypMfVS3Mkjb8zgP8_3ud0vjTA988cpcj1So-90XfaZC0Sox9I96SMX-BKmb592YCW_pHpl1plswunfw6rxpW7cdrGW2ZB20X4J1xY7p9gR0QrN6d6um83vMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
کل‌کل بامزه دیشب عادل فردوسی‌پور و علی‌آقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100521" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100520">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtXtGya4m1eMWt0GAKhKJYQIqtTjJCdnjmuF9PAXDaXqQ_HIenKJz0RhQXBkaamdZlVIAVyI5vCHf54pZBKt9dXjq0DX27FcsSiVjJvnPFp0mHgxTnkM9jq-fx8EXAZizSYefPoar278oBxd_k-xPyJiz3yNH_MrRvYkiBSgIHYUDEGAethYv-ChfiyWc7V2ohBFy1xMYWg9J4K-pqumKZSOI4g8jham-OLXOZ5nL6y5CUDbwf68EHL09lQXs8YfXfaAXQIJqPULtoevafEP2ISScOvNoNJxIbuIyO2pKFlu_-BnaVbk1GLn2Gdse3tx5n90eVD2yL3O6_AzTZUkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فابرگاس و خانواده قبل بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100520" target="_blank">📅 19:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100519">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tikfnqILYDG7_iRclgxXy_MEk2HHsyxpH-XVNPnO_l2Ui074tG0sq_o3yc5X3WCFLE0vitIW1s4uXxrnhnwm3JNJMzVNMglxKfg55MOfU7VV2rUXBS9PfXodY-hvXgXCk9RxjDvIajwTiecHHZfnJhZGSao_BklEbR4oYWgGQyteilWuqxuxhwCAnvw2nJl3jTOjJDKNBcigUS4DwfjOZiKKjFew1n4Vqu51C1fbPkCo0iRG8bOfk0301I6TjCm8BgANvK-DrA-Zik8JHkAt6iBTUtohGOIogWYlLTUfjoZuhDIsBPNvOqZyWB-2iBiNovi0TIe9FpWQHiXXc_hqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت اول آتالانتا برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/100519" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100518">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcY61zCUdEp_9q9CrvIjhIsvEpNq30XUNdII92UOTnJG7iXmOQG2Pf4935clwtbvkxGyx0utwTUwpf6I5xTUFxJQZVtzZOZ2o8-tlzluogdgET1pCn6QH8orw1KRR3QfW4Yhf3L5NMoz3vPNW-Nvpe-730voD-xDtKp2F-0CEAHEoKjnDIHvrgPINDPbH8vWKQ9cJllmawoEdfSurDgv0DOYgUDwXWrV8p9A0KXmW79k0TLKvtfpa1ptJCSq0WsBMLJLl6hUW0tq_qRbZywCBijTFoWg_O6qaTjXoTkFo7PnwMEr7pp3JXS4NqGT_cn4bu9iUDk5pePhwZKLlS16Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/100518" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100517">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tfxpm_m-gN3F4BXnqx4gyR1r92cZqKIeH154NwPBJcCquIUfBbKAdwd5VWeWnjep_sTQjbWxxcBKtLNKm3o1yz7iSmQ-n9cCxa1p6mU7d0ug_6IBrCahw4QgVkgGG7wAPdnIr8kFMzPSekrluXWzzNufLQ4_kwFQCP3LUapM7PtyBxebaoEaY7jElmcQPkWIkbkJ09PhhDxZRxi5yji_OAhS01CYcKkILmUSUxGW92XMGjDeonZxX84TTh06uC7XzYFBXjQ152owmqsNZRwSCD6geDNpc2JLYqeCQAyxJZPcZrKIH1hHMd3Ks-Ub6Qz-gN5UEW6Hm0NKd8GVxAs45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
استوری رامین‌رضاییان که بنظر شاهد جدایی این بازیکن از استقلال خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/100517" target="_blank">📅 19:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100516">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhpMX2EmACN7MZ_wcp72EkPM2Hlz6lWjg3VS7xYGxnn4W_qXiDU23jHXMBN60VExTOIeBvpcURe6IbeAgSazTLeNrq2gEM-IrQ-PUFBwRnIo47aLdp70D5vukHahRitOHGzECOqZQDbVfqAlUmvpx9z485a_qQ6ZegTfOpFeKMMroXjLsFOmRaSHck8JGClSxYdBL_K3PNU27pTBvdhzGZKBaOqPRTH1pyI5l93xQovqIJfB05ogSeL5gQyH5YddVakpigLs_0tM-UtiTATbOC1co7t3d9pM9ZEe256vZneoerAuADg67TM89I0pRB4ODJIeryruUSyFVIZOtfb2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زین الدین زیدان برای یک انقلاب بزرگ در تیم ملی فرانسه آماده میشود.
زیدان قصد دارد یک کادر فنی بزرگ تشکیل دهد که ممکن است شامل بیش از 25 نفر باشد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100516" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100515">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=A05RuR6LYP0SXD7v1Sy3hyXCqZiH47WbS5Q8Q1mHZJUrrKwr10BAY--ZoHjsEf3PMASrL3lHCexNY8SJMy905UVnKjSEUYRPeRrDpRju55yeOVRSKUXu1e5NwwdyyZN_SvbXhU6VyODymRW18AYt-QH1gjOtHqASH488BpOMtRtkgBNeQTcU7H6K41Lvq7i6S_-UpcfkZn8mmSMqh4GtUuqJIfr-QZuZ6tj2izJsYPQe6J-LyMwm4_KfrFIMSHLPcK4a0GVLiwUT9otUh99rlhWStMFoMYWUQuveInVI78HhjmxtpEc6RQ2naRxwMstA57AoXSFJh54mwS74RCbKfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff7cbd247.mp4?token=A05RuR6LYP0SXD7v1Sy3hyXCqZiH47WbS5Q8Q1mHZJUrrKwr10BAY--ZoHjsEf3PMASrL3lHCexNY8SJMy905UVnKjSEUYRPeRrDpRju55yeOVRSKUXu1e5NwwdyyZN_SvbXhU6VyODymRW18AYt-QH1gjOtHqASH488BpOMtRtkgBNeQTcU7H6K41Lvq7i6S_-UpcfkZn8mmSMqh4GtUuqJIfr-QZuZ6tj2izJsYPQe6J-LyMwm4_KfrFIMSHLPcK4a0GVLiwUT9otUh99rlhWStMFoMYWUQuveInVI78HhjmxtpEc6RQ2naRxwMstA57AoXSFJh54mwS74RCbKfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«قاب رو ببینید... علی دایی و کریم باقری... خیلی سنگینه!»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/100515" target="_blank">📅 19:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100514">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6P8D88h1e_ywTuh4UbXQl0IfKxaOV3ICgNj9HZMNa6vUrtLgEvcWrA-4XKjikI95cSbIOI3UxhEo130W9H7sCxIHj1sS0nkabkVPi-XLWDYx4gwxLt6I0H_phj0YYP1w9mdgYgdy00oUeMbBg4Th1Gf6LvyQGciFGdEm1YIuFf1UcdBulm1GcMHEzv1X08i6epvFD8i7oOfIQnr0Edjony9FrCacSx0F9vMeEyKqupitevpO3xQMk_2JIjfhoFucUpiSJiqCveP4xFM5YM4TBuG5hahgVx2OGBl2SVcNRM859sg3d-0iKhXGSFWIaAL0PRMBuU65LZKgIoihoyMtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمعی از هواداران فرانسوی، طوماری را برای درخواست برگزاری مجدد مسابقه بین فرانسه و اسپانیا منتشر کردند. این اقدام در اعتراض به پنالتی‌ای است که به نفع لامین یامال گرفته شد، به این دلیل که ادعا شده بود قبل از ضربه، دست او به توپ برخورد کرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/100514" target="_blank">📅 18:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100513">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/121dde0263.mp4?token=SQ8_rWfQxEy_AK2o_Gzt9OUyZsVnQQN8-pZ2-Kj0xETT9KB_NV798nlUR5E34Zr5zx8JWlbmxX-To6I06BRkw2bpbhI0NAUfQc5QARuDbT3j1YA-ea6h_CwNmKYZuH1oZy8NOeWqyFKeEMO560HC6U_kgvHYOn1CrBPLNR3STOwndTFovDxbo6cnGdSopM3X6ZOmjs89nFpeXQpBVWsVht4asZITsUdd9HjV3nMpRUbUuHj8SuXyDbGf4HVg-omYTF2dzHTrbCOymP8dHudCzgBh6O2_gA36TxhL6UHElEO5ZMZpGg787bZT3syeYOIu1z3kEs7G-tKfqThNqxI7Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/121dde0263.mp4?token=SQ8_rWfQxEy_AK2o_Gzt9OUyZsVnQQN8-pZ2-Kj0xETT9KB_NV798nlUR5E34Zr5zx8JWlbmxX-To6I06BRkw2bpbhI0NAUfQc5QARuDbT3j1YA-ea6h_CwNmKYZuH1oZy8NOeWqyFKeEMO560HC6U_kgvHYOn1CrBPLNR3STOwndTFovDxbo6cnGdSopM3X6ZOmjs89nFpeXQpBVWsVht4asZITsUdd9HjV3nMpRUbUuHj8SuXyDbGf4HVg-omYTF2dzHTrbCOymP8dHudCzgBh6O2_gA36TxhL6UHElEO5ZMZpGg787bZT3syeYOIu1z3kEs7G-tKfqThNqxI7Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
تفریحات کارگردان استادیوم‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/100513" target="_blank">📅 18:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100512">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=n64Lu5fU7W98iSy5z29WnOJZLCRvJ8R_vRV52iJ6wSFgy05KOns6Mv3XCyTrxEl73F25qNCCsQE1oIuTwMtaP-EQRiIs7n69OA0FvspwZ3IBFafEMuTTWNStlhx0H89GFT7XeEx7rGrrjTxToEJ0RNripAGqpumrNezPM4rhPgJFiAoEE2uYuFWG4aoct0N3CcR_OFm7Tl5Y5y4o7YirTdo-lMdlj0bEizsv0wBnpbwaPEAwkBGyqcNp-j1x9KQqWbaBrQRQyzPYSZ2wzj2QzDA5LSdNlKMGdQSle1Fbwl3HneAGx5Fco0D-f3k4rH-_DUkcGcjL19h4sqy1JQ60DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c73b07447d.mp4?token=n64Lu5fU7W98iSy5z29WnOJZLCRvJ8R_vRV52iJ6wSFgy05KOns6Mv3XCyTrxEl73F25qNCCsQE1oIuTwMtaP-EQRiIs7n69OA0FvspwZ3IBFafEMuTTWNStlhx0H89GFT7XeEx7rGrrjTxToEJ0RNripAGqpumrNezPM4rhPgJFiAoEE2uYuFWG4aoct0N3CcR_OFm7Tl5Y5y4o7YirTdo-lMdlj0bEizsv0wBnpbwaPEAwkBGyqcNp-j1x9KQqWbaBrQRQyzPYSZ2wzj2QzDA5LSdNlKMGdQSle1Fbwl3HneAGx5Fco0D-f3k4rH-_DUkcGcjL19h4sqy1JQ60DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتخارات ایرانی‌ها تموم شدنی نیست :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100512" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100511">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f049197c85.mp4?token=dAqnQlXE0hPwDs1L-CGP2GdfmQ81lVY9bEzblqgYwIk2yT5hlqc69rbiLfmRqT4hARAwiCkHmm7cNg5pvh49BFEZIEPWHn2Cl4fz_ekc2PcpMJRwRBq2fnLjfGge457L2iM04LUWZ88oYhTkbRgpUcwPoPntYvlB_ffYoyJyAJUzpfC7Yuhk1sHlSQqYxo9ap0hjfSXyBN9zvWYNcehzzJK_Klu-fsvRBkIfeFVt7tLnG3bLRt6eOAKqsC750NTiZYmH4lcbazLQRB1fxY-jY8kf19vSkGXWxtZXPPOcrCrZVeEzBLw8TogOUjyCByGi7X_kllAfj7Ed-I_ZhYW6Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f049197c85.mp4?token=dAqnQlXE0hPwDs1L-CGP2GdfmQ81lVY9bEzblqgYwIk2yT5hlqc69rbiLfmRqT4hARAwiCkHmm7cNg5pvh49BFEZIEPWHn2Cl4fz_ekc2PcpMJRwRBq2fnLjfGge457L2iM04LUWZ88oYhTkbRgpUcwPoPntYvlB_ffYoyJyAJUzpfC7Yuhk1sHlSQqYxo9ap0hjfSXyBN9zvWYNcehzzJK_Klu-fsvRBkIfeFVt7tLnG3bLRt6eOAKqsC750NTiZYmH4lcbazLQRB1fxY-jY8kf19vSkGXWxtZXPPOcrCrZVeEzBLw8TogOUjyCByGi7X_kllAfj7Ed-I_ZhYW6Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتینی‌های دوست داشتنی خوشحال از پیروزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/100511" target="_blank">📅 18:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100510">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=ivLfOVrcbr81fbhXNHLsjB-qhYhiAGvmoMG9I1nqNuZf4P0_br2Zo68aPhYvk_jf16XP_H8cWOoMTIMG5NFoIV5Zg_8_Um6MCkgnqLhJpB24eDNjv2rIuPGllRqFM3fU8BGmMx8AvjoO0ZKJSFCkg6vWQ7-KlEAo5d0Zkb1adWMLt8lJLXrFJqfBDtuOH7xb7pMIq0hUOpKqhohQoiO1zt-S8QZMG-zLAjF7eMZeX-cyiWsMECjsISJ8zi879bMjH86k1D57k9X_O98lolfLHYlBVORxy7fy8pNhJ1RvMmr2x2uop4JVvj-7ggmHbwzs2av6Py_zNMNJqvhpVQGuiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4981bd9a51.mp4?token=ivLfOVrcbr81fbhXNHLsjB-qhYhiAGvmoMG9I1nqNuZf4P0_br2Zo68aPhYvk_jf16XP_H8cWOoMTIMG5NFoIV5Zg_8_Um6MCkgnqLhJpB24eDNjv2rIuPGllRqFM3fU8BGmMx8AvjoO0ZKJSFCkg6vWQ7-KlEAo5d0Zkb1adWMLt8lJLXrFJqfBDtuOH7xb7pMIq0hUOpKqhohQoiO1zt-S8QZMG-zLAjF7eMZeX-cyiWsMECjsISJ8zi879bMjH86k1D57k9X_O98lolfLHYlBVORxy7fy8pNhJ1RvMmr2x2uop4JVvj-7ggmHbwzs2av6Py_zNMNJqvhpVQGuiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از کجا به کجا رسیدیم واقعا...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100510" target="_blank">📅 18:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100509">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62564cea43.mp4?token=LFmNLIIS_elPTDB2KFC7ypwNrVoFSfGvNxxplEX_AgZAjECpLT4EjDjBrAvEhjOJ7qXj0rvRk81MoRJi7uHGIdRJ_ndQle3ROFSvD6upIrEpf0IpwQFSTcaBq73BXHEdL4S2SEhE_JfQ8uFhnlw4kaLzVExQbTWxjSVAFgvUM7WPZujQt9VwFegaw5fnZdl2_2Epo9JZtAyx_c374sWq5TrSYppGLO51Pyk1IoZ2XbzghLB3D3iHXlPA_q-6b0tbeuNxeUbEEEYmIHqjL5l6ZDWFYSi3VNmfd9__KKYziL_NAVuYwBfHIrVaY3ER6RfDn28fuJiElaY5rkrmy1O4bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو چندسال پیش گفت: ما تو الکلاسیکو مسی رو خیلی عصبانی نمی‌کردیم چون در این صورت عملکردش خیلی بهتر میشد و دیگه نمیتونستیم جلوشو بگیریم! درسی که جود بلینگام یاد نگرفت و باعث درخشش مسی شد!
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100509" target="_blank">📅 17:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2241a88830.mp4?token=aLoRFVRFEM4CX2pzUKLow79xP3m4OF85vC_Gf9f9qjUCpZhv8l7JOfvh95p6vqxoMiw7iaG6aGXmQJkQk9zdtMVuyHj-IHQA_jB9cCN7JDMVUMpajJL16jZKYdwNBUdz6YRNJaY5p8v7jEz64lWjUMeHsE8v0fJOh6G0fH5RZCXb7nh44rhLT8OA4UcKgJggZeugpmoTvayGl0AsO4VLKjDXMeXDxJsCXQHHDf5WeRKos5YUtSFzht1BRXZugYoT26Ma5Rd7PVz0mT8iPBX4H8Wyugk5I7th_VydT3iTyNfs4Av-s2BTRTtKQwOGvKzbu5mPExYbD8XWfYIQ1aIxTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2241a88830.mp4?token=aLoRFVRFEM4CX2pzUKLow79xP3m4OF85vC_Gf9f9qjUCpZhv8l7JOfvh95p6vqxoMiw7iaG6aGXmQJkQk9zdtMVuyHj-IHQA_jB9cCN7JDMVUMpajJL16jZKYdwNBUdz6YRNJaY5p8v7jEz64lWjUMeHsE8v0fJOh6G0fH5RZCXb7nh44rhLT8OA4UcKgJggZeugpmoTvayGl0AsO4VLKjDXMeXDxJsCXQHHDf5WeRKos5YUtSFzht1BRXZugYoT26Ma5Rd7PVz0mT8iPBX4H8Wyugk5I7th_VydT3iTyNfs4Av-s2BTRTtKQwOGvKzbu5mPExYbD8XWfYIQ1aIxTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چالش عادل فردوسی‌پور در تلفظ نام وریا
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100508" target="_blank">📅 17:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100507">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fb09b2935.mp4?token=pxZIHZ-mNIUdC9RWnEBbhyrkeEOW3O5FWovH_uTSNB68RXPEfAcQD8YcVpWgn85ycllsGkHO2-arpa9oFo7ASvGtkRlaS5t4J7OQ1pL-V2JhY4Ma80mZ7lZuRvWwWfDk15jgmkxgensxYyCaQKd0sXvZiKbOi1Omq87vrrfpmaFaA9NVqYayUYrufZXX8kRCfB8HmiZb68dzzAwuZALyNr25XqccQKOXf901aTYQ6_8c55qydoctW5AT5sisV_TJDrpOjDtNgF6MoRBGADDnvdU0eTYI070tdhWG9DN7gfwvDRJOQbY6uXhWoNHBqCoO4YmCB_YRBX6CgMhlMuIb95PVNI_piIiW9VkD8SRxgds02jxH3weCaumr9s8aE5x3NDS0IyuY1JNeVjmYAUPHjPRGo2mUa59gdR7_Set7TDgYIYaJuTVtynf6Kv4Bcx5C3CyMe2Ceh4AVtmBpvMSi2oL90u49k8X6v9ZzceT-1tpq1PUcMMj83xlDyXYCK84syTz5_Lz3fZ_z8g765RMFmLwksDhrsqNBTRnkG4Me3AJCuH1fK4-5gj-P1rd-98yoxUZovLZyRshDbGFAK9NrpXnH-3Nr3k7HG9AWDl0iJ6FQ6Fy-TN_hZkb2hbuaRy7VF5ruzI0jN2TiKxwn3vK4JSDxN9C8Yu-zuJcps_mK9vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپید:
دستم به دامنت یامال، تو رو به هرچی قبول داری قسمت میدم آرژانتین رو ببر و نذار مسی دوباره قهرمان جام جهانی بشه! اگه اون دوباره قهرمان بشه ما هوادارای رونالدو دیگه اصن چی داریم که بگیم؟!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/100507" target="_blank">📅 17:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100506">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I66BdoEzW2YZ8RXjTCZ1O8LIhTJ9cPlqcvIN49gv8ldUBDhWA4ZMe71jvzEBj3GJuBnZ-6W1dsrjFofNFvOsTgBW4a6vzCAfkkU0N5TKjbpbDjWeUJCq5lEw7zRhgyBsIr9qrqEFDwfWMNrasPat4AhpRm_ZO077Sfw-NuBgnc0FVxeJ17QzwxjNcD-m-VPMQzS6XNUkZVWbvj0fEtMc59_JSJBXId1bE_sRLaBpkNsk6i8V0qB5iQ2__XXQ_AnbQWxF5A5OtaVO9Dl5TkauTgA84GtXZGC968V4yfXAKhkI6Mi5-0GVfihxxjQNr-sZkwppIr0BPgQcjPbC_hhjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رامون آلواز:
رئال مادرید واسه فروش کاماوینگا مبلغ 80 میلیون یورو تعیین کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/100506" target="_blank">📅 17:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/901a48c5c7.mp4?token=TM8xcd59G0l0GRF3ZvklTaWQJrNlCAh89WFcTdAGslMys9OCnULhrNYW6317PwbhgHu2VBf6dU2p4a75lIl_ZBQkDZovCXFrgssPKHOQbVxNtM7y54j9eK4njHch9Z-_jV39gNiKzN4wG4R9AU_B7PkNjo-xxeTctOtDkqc8nQkSWjX91K8Aw5vVxIGblKNPO57bzQmT1BjdHZS44ZBIOyWEFSBKaG44mKD76P3z4HswBxCRz_7AZaPWf-svPAyyPpcHjl62eIoNOAP0f8aTTh4oaJkrMFy2EkrpMGUkGaRLqHAD8oPiOYHYrvGCJGP3Z6SRCXhxiGSl0jCWRguPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
🏆
تصور کنید توی اوج هیجان و استرس فینال جام جهانی بین آرژانتین و اسپانیا؛ نتیجه بازی 2-2 مساویه و بازیکن ها رفتن برای استراحت بین دو نیمه، همون لحظه بیژن مرتضوی وسط زمین:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100505" target="_blank">📅 17:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100504">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=WHhrJFOsTHyp3kw0i6tXJwd6X98o__ImTcdcrizkClEWNrqcfc3UNdEcmQqs4Jcbs6dkY1gfn-IWuRn8bOEnmA_y6yWljfEdzIoxZU_ODQkMZLV-iU9Pfg8Dr80AoYorvlXe75c7lapMxISN9UyWFkXqqb-Q-tJDCdPcEJdGMofbYND65oD2bv3MBv1EtTCXDboU1bE4b5mXNitsXi7YhIR5pGLyp3Pgn6Xa4CYj1vNwOkTrT_WKWG4rFNUjt1D3DaikxtIlzgKeFKoi2JzaV8DHzEpcIudII-HKmlw2ncenh0RFcD7VUpDWPFqMq9m3FNhVvSQfthwXhgqAc2ej6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5386b5fd.mp4?token=WHhrJFOsTHyp3kw0i6tXJwd6X98o__ImTcdcrizkClEWNrqcfc3UNdEcmQqs4Jcbs6dkY1gfn-IWuRn8bOEnmA_y6yWljfEdzIoxZU_ODQkMZLV-iU9Pfg8Dr80AoYorvlXe75c7lapMxISN9UyWFkXqqb-Q-tJDCdPcEJdGMofbYND65oD2bv3MBv1EtTCXDboU1bE4b5mXNitsXi7YhIR5pGLyp3Pgn6Xa4CYj1vNwOkTrT_WKWG4rFNUjt1D3DaikxtIlzgKeFKoi2JzaV8DHzEpcIudII-HKmlw2ncenh0RFcD7VUpDWPFqMq9m3FNhVvSQfthwXhgqAc2ej6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نحوه مخ‌زدن در استادیوم‌های جام‌جهانی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/100504" target="_blank">📅 17:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b77728c3bf.mp4?token=GPZbvyZAmuHH-FVaZCgABhjgsZwwPbCJ0F7-HQMai7ZxlcW9u7Bwsv4fqOcvLljES5SdO47BRJ7D5erGfFWVPf_YSMOi82pIQlJCtt_xmMa-eZWZmt3z6TBawQxCctDm-Dav0zvo0QY5PZv4k10FT0o0ze-K5UDND0Xe7qK4hDEsqVwGYrxnSsVyrILGfvuvVGw_ymQM7Tm0ECUv5t4QE2oUyt0oWBjzKBZiSdpJ4zgv1dWP39yChaz3TFc_WQ2zn3Hs3iExxSulwfEby-raicH6KBrbpowKDmE91u7PHwlIdD1gSfupQIE4PmlQINvnYL8FE4qvzXCHhnsllJ1cWzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
قیاسی: رگ گردن میذارم که هالند لره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/100502" target="_blank">📅 17:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100500">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlPUFoZLOGzXhPfEgL911uGYR2kTNrz72fM2LrXh1HjUuwYawbya9Zy3cwu3TqU4yQyw1hrrD_Vb6fIYhy0NgQSo92nw5G3tOImIVKzgTL1q8d9YibYKZ7iyd1VVrkN-FEquz9KHcLBhhFCLFwWajM2vIRCRMEfFB3H8Z3rfYZ_yVHwlxbvf2ypDWD-E2jqr9FBTW6auJcQKGGqLPep1mpQoUq35Qv6bMJuHP4IDkiAb-zqJCnYRb3pIm3TStVE5NBng40ATBrMtTL4Qh8fWIngqcroZdAY0P3F9N7jg974sCkcoPU1IcdutWk4MQPuD50L_kk683B-3lr8DvpfIQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oLgHvIcjW3v5cxBrPfeOEQbc1MubyAHwBEH0h3-eEbdBkbBiLjMnZK9uh3aLTB4EneklySr7DQRXll9lo9m30Fjb2Dkqo_3nVwu-oZ-ArAlzZKWHJzZ8qAmwlCty9UmE3Gpi5wkUow-Pbm8uOqE4Sq_pYBd4Q3Yjvo-Cli_68CjOQ166rgz6Dm4gpyR8nXta_iZz94upXci4A4pewMxg30_lX3N11P4fzpVOKWkolZjNz4kzipL3pdcU5y8QjMiSvaLOf-A2oqEFgr9Fm2Bb2Ane2ws9WkSbX6kYdxQZzkMzRB6kebP0zpEuxAAgvzZTEZZtr7WeIbLtGoshrwAz-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مینی تقابلی که قراره روی سکوها بین داداش یامال و پسر انزو فرناندز داشته باشیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/100500" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100499">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvD1o_L6-OC_3pt6tiNxH32dSMxcW83AjIz9HFTn1qeu1bxq6B3qDxy_4pa2WQ2-GlaYtrWhCMF47Xn_7ZklF4OAIXIt8rCA1Xb7DcGlIoHobzrGTpP546ufW9Q2TUoKz9hMogq23I4UxwrXX7PNBBkzd9dWqf-XZDr43e1lLbmre45fAD3JEfkxA-Gx5wsHUDjXKgQvM12ZsZ8B9sKnaTKhQYnGgSrbCeMaamuW43an8l3yfTtGUDynDidX0Y5-s0ELsVnIAYEe1bC5asW7tbciavaq1-OeZBrOIqVQk5XB37UEgSCQcBaPRaGGGCfu-RxQOR2jfQQk7yXN8mZzXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
الکسیس مک آلیستر بازیکنی است که بیشترین بازی را در تاریخ جام جهانی بدون باخت انجام داده است
11 برد، 2 تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/100499" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100498">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxErwStoKTi15Z9NPKM96b8ln3BuOsTtnyIQiK1MEuMGVPcpaLT4lAE0gM0AewfVhdda7-wUCpesGI_z_T1havWwoUbiSXh4ZJD_5a3fCmvD_VOycP5HPyxhRsgHTJlQbHF_nWt8yzw71HcgJIe9yZpb5x54X2b-f4uh8EQLuU_NCTtodVjBihjfB6cbcShOUsaP-_WlxKMJfPuyHTSXYmarozgh7I98vOl6qcTLxf_WdBu88cemokmdmEXsPR9pMZn-fWVMZJPTv0ssAJ8R3y_JF22T0DWJeGs8aPMaDYTJgIaE96KfwIMpsgykJvc3fDhT5b0fSAgtUr0hpeNE2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: سوبوسلای مجارستانی با لیورپول برای تمدید قرارداد تا ۲۰۳۱ به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/100498" target="_blank">📅 16:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100497">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=rpyqOBkqBbZQUyhuKr6x61ajl6L8yOM4e_0-URpd9zKOKF7c3w2yzfp-Fa3GLwER1UGxKdiv8zt_BnlsiM4tHy-OhGDYpvwwA586Nxh2dXPa1E8pvIF4D6p5t0Yj6PrLTyHr5-ioNkSc7XToNFLl0fHw1NliK6Jyi7SsKoiBX7yZN3klHbNNwS6jfRC9EI0M_epsCpIJNibkvOymqnTcPC47RFaOLTFNu0FiXpMSxlo0_eCCAS3A_7muFZwj8oyiA6jOmWg6xxmRRzYHXNHuhFOQ-fQSqJX7E_x9zOmyycU2FGttNdKtxzhJB9aNzXgHMuOcTf83DEuRtU16BAC3HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef12f755c5.mp4?token=rpyqOBkqBbZQUyhuKr6x61ajl6L8yOM4e_0-URpd9zKOKF7c3w2yzfp-Fa3GLwER1UGxKdiv8zt_BnlsiM4tHy-OhGDYpvwwA586Nxh2dXPa1E8pvIF4D6p5t0Yj6PrLTyHr5-ioNkSc7XToNFLl0fHw1NliK6Jyi7SsKoiBX7yZN3klHbNNwS6jfRC9EI0M_epsCpIJNibkvOymqnTcPC47RFaOLTFNu0FiXpMSxlo0_eCCAS3A_7muFZwj8oyiA6jOmWg6xxmRRzYHXNHuhFOQ-fQSqJX7E_x9zOmyycU2FGttNdKtxzhJB9aNzXgHMuOcTf83DEuRtU16BAC3HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این جام که نشد ایشالا جام‌جهانی بعدی بانو
🎈
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/100497" target="_blank">📅 16:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100496">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=TlVZ6BhAVK51WUCjKqgmc4TEWpDElXJLO36LikyVa60ij_4ZdF_MdN20szzcZN-xFD3CqVRgY3-LEB4A9M2_q8J7s9v1VQdBB9j-kBocsCadt_-ICZ9JeyF6Ftjswd5CUnvraJCacEtDvdhF4Qzwt_HA-ayeSIL4Mv3ffzB5mLf1uZRHBzzmw-8RJHQJFwSNzLgtyVlWw1TlkgnXL4haSZLD19uIb9iqzTzZ4vyVKVt3JH4MJnlYiXLZR_GWrQdXsNkKod00KfU2MKVBgGH4MXQYNq5kcgropbF18oI3KCrnYC0zZG4lNEoIJFU6e53sOaK7dJHHBrh7Li2G5mZcKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efcbbbb391.mp4?token=TlVZ6BhAVK51WUCjKqgmc4TEWpDElXJLO36LikyVa60ij_4ZdF_MdN20szzcZN-xFD3CqVRgY3-LEB4A9M2_q8J7s9v1VQdBB9j-kBocsCadt_-ICZ9JeyF6Ftjswd5CUnvraJCacEtDvdhF4Qzwt_HA-ayeSIL4Mv3ffzB5mLf1uZRHBzzmw-8RJHQJFwSNzLgtyVlWw1TlkgnXL4haSZLD19uIb9iqzTzZ4vyVKVt3JH4MJnlYiXLZR_GWrQdXsNkKod00KfU2MKVBgGH4MXQYNq5kcgropbF18oI3KCrnYC0zZG4lNEoIJFU6e53sOaK7dJHHBrh7Li2G5mZcKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
علی‌آقا دایی که میگه بخاطر مسی آرژانتینی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/100496" target="_blank">📅 16:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100495">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N92zQns_P9Ro-c8n1xGcyRTq7k6Eb6uxJ7jb9vdhnSaT8RrlgCAiFS36u0K3y1fkysM-evd5pj3MOGamQBZsP76g0AHdv3KP9laorkQ-HZZLLad-97O05RLl3dlZ0RseN72nEMHi0iCOxG9HE2TQte93FYYR2fSkllK96CYyaXXoQ2K3fBgd31ayntmwZs31fAEB3ojQA5g3tfUquFnW0M1YW3UJ1-ks8gFNUBvUTPUlS6H9GGVc8VHkjP5A6QvYE_uxI7Unpt167u5rqje3p8ylPDK6xwRlWa7-rVOU_qJSbdPY0RFLVNgsAn2ot_iJVVAc1PHzaNBYB4EPG4hTag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری دی پائول کنار مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/100495" target="_blank">📅 16:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100494">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8OpmFDA42-sIaMsPOEqr-DVcIF19ioMHlRTYwBVZPVlxNDZdF_qI2WPUXA4FJXOSlKv6OQa3DCx395Bw83-g-CkDh3zj8jnM6tSIwgyO5qMMV4t9jKEjBPYXpt-uV7DxNAno0zgTxWwSJ6dUg6-f8VaaY9M_elYwEDGdUgaW_0QPyulFeLKyDGQLTlCKLjpnPIMnDNCVUYWDVlP0exEaqxp13XUpw9VrGusGgFuAXf_qGg_gf03PdmmrjfFKotuuDcqYMVsIwrIg9xR6DAIUG9Jk7klqOhjIrJGebl5EXDZeD4lP6yBdc2_DLvf2gteqW0u0_ajGU5t9WVeuoLAa0vw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb2da8dfa.mp4?token=Bt8gYX8MHRqxo7ZXONIr6ARiSUH3QhQZkEBZozitJoNcTYg4XDKz89TNOSfYseH7umtiu6U1uqpnha3Yto4T_4tD_DZC4EFVxJ40boMMdgV2_mKi_lJmjMSipYE-ysi7KvgtU3YUOGUXEn1VqiZW7wz-Oh1kcNaB9q1PXHrfM1Xdst_La3ENlmlqrf1qArBKrMAN18DTGPtdTnAILC9Lf3V-3RtAiqgeLWTH_1d-8USURs9r31VuviIqqP-gAm6r1hFtc-l69XiX0DdEMZLcrCzXxEjdSKF0PGAcvAUn7-PkEgVzndN2T9YTwNVWhhmk9UA4JfmkLjSVkbXi-8M8OpmFDA42-sIaMsPOEqr-DVcIF19ioMHlRTYwBVZPVlxNDZdF_qI2WPUXA4FJXOSlKv6OQa3DCx395Bw83-g-CkDh3zj8jnM6tSIwgyO5qMMV4t9jKEjBPYXpt-uV7DxNAno0zgTxWwSJ6dUg6-f8VaaY9M_elYwEDGdUgaW_0QPyulFeLKyDGQLTlCKLjpnPIMnDNCVUYWDVlP0exEaqxp13XUpw9VrGusGgFuAXf_qGg_gf03PdmmrjfFKotuuDcqYMVsIwrIg9xR6DAIUG9Jk7klqOhjIrJGebl5EXDZeD4lP6yBdc2_DLvf2gteqW0u0_ajGU5t9WVeuoLAa0vw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
تسلط کامل فیروز کریمی روی زبان انگلیسی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100494" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100493">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=U2YK7CScNQjypeME8E0r4HGKbS3iFalF7FwPEygTbk2DJ6RwVXNDUlsJxNhH2-9_oBA4CEiHKKP3jOYn98wR0zs7HCh068T8CMYtcyRsg1lMeAqCS5cQhKa03nPffrMBDlZGN19KCO23j6cdWRBXDkbMD-XT7gSTOtMTfpklGvMAfKsBaWUiJuzwtu_9M6klXVRqxymedHzRdBHrhrV0iGelNtVL1XvkJa6FfLYkF6D6RzRk_qFyDJDNaURaYN2JoayChW7ymtyav3mbHfuuZfjJbeI6CmEMwBqinDVsWILnHgdlfr2poqFZtqqOytDAgRFQ7KzOtwA6j8DqoQUd5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8ceabea2a.mp4?token=U2YK7CScNQjypeME8E0r4HGKbS3iFalF7FwPEygTbk2DJ6RwVXNDUlsJxNhH2-9_oBA4CEiHKKP3jOYn98wR0zs7HCh068T8CMYtcyRsg1lMeAqCS5cQhKa03nPffrMBDlZGN19KCO23j6cdWRBXDkbMD-XT7gSTOtMTfpklGvMAfKsBaWUiJuzwtu_9M6klXVRqxymedHzRdBHrhrV0iGelNtVL1XvkJa6FfLYkF6D6RzRk_qFyDJDNaURaYN2JoayChW7ymtyav3mbHfuuZfjJbeI6CmEMwBqinDVsWILnHgdlfr2poqFZtqqOytDAgRFQ7KzOtwA6j8DqoQUd5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
آخر عاقبت گنده‌گوزی یه بچه‌سال برا اسطوره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100493" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100492">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=okkBWXPid_9NK7LNw36VdfkPnkgGvqKYlZ2oqPe9kuVh8z1BUlk0raDj6v8W1wxO4PCGi5Kos0XOC-Q2zQkCeO3ftuh6Zt5Ys1cCsvGvkF7Qixnq3-70WaPkVLEPR529chx0EeMmDjYZtqFh_LeK-3uzr_i_zH_mz7-ogkKprEzEenM-pG-a-XiJIQteV66IEF8UIIRh_teQ6V1dVmejFkXd_ZQJZCVzT1B5AlKftPh1oJBWM5sViDXBZaQBbbEGRzuqbLGg-7uhM8RWv-JdoxR-U6OdeMV57EsqXAohpWxENGTy_6G6SRloYwhJNYH0HCY2UkMJnhrrAv2smNktsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0505b98db1.mp4?token=okkBWXPid_9NK7LNw36VdfkPnkgGvqKYlZ2oqPe9kuVh8z1BUlk0raDj6v8W1wxO4PCGi5Kos0XOC-Q2zQkCeO3ftuh6Zt5Ys1cCsvGvkF7Qixnq3-70WaPkVLEPR529chx0EeMmDjYZtqFh_LeK-3uzr_i_zH_mz7-ogkKprEzEenM-pG-a-XiJIQteV66IEF8UIIRh_teQ6V1dVmejFkXd_ZQJZCVzT1B5AlKftPh1oJBWM5sViDXBZaQBbbEGRzuqbLGg-7uhM8RWv-JdoxR-U6OdeMV57EsqXAohpWxENGTy_6G6SRloYwhJNYH0HCY2UkMJnhrrAv2smNktsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای عمو ها اووعو اووعوو رو بخونید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100492" target="_blank">📅 15:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100491">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dd1G_fIKc3AuegYTEV5r8-mWnNaXj7LF459qAWhs4Gf28UVTpjwMM3FjFNeN51CjTv_INvYJ1dDy2qmi1D8C_QCrxZziPdBSJarxhLwMdMzAJMom42rxKWRnzDM63RUauuZhpq5ENc7oonyKNsURU0tv_z49fp11sPqEC-KWZx0xsa02xnp7uYAthHJ9C4FXYB2OoKL_UbCPkEpA0uReqZbqAgiw8rveDRN65WS3z60B0mTPRFzCA_Rm8GEuzKh3a1MDrisu_zrWtx5sgHn4Kb2eXG3cNM7bS_XiGVMegNSzFbMQe_GxiIkEsdIaxUtbngvTUL_kXL-xW1SSSPW0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
🇦🇷
آرژانتین در مراحل حذفی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/100491" target="_blank">📅 15:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100490">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZdyhRScUn2A513_RPvtabk8iZmhrNZJJwOjrfu5r4qhJ3eZhZh7bP9tNYQF5sDBstCiDcN_1aN4Ho3CddsOi1vo_3ZNCuE1c55YWzlb1XRLbLHJMPxZ7e2amdLkNwgTpI5TUqxrPAiRWIis2P9q4AZv_q7N4XTkFArZstx6h8yodhnyj6pjbnkAoFy0NzhOOtbaKXviuFS10E5hRWUenwwaZi3iupICNavDcxaDx7mSxiVIRZXcKuIMqHevRcqk0mOZbKW8YyUw7nYlOxVuRBw13OxtamgbxxVRRc0CohqihkB867IUnm6yRm0lCVGkFxOxaHgqa8R_MeJOo_ldZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🏆
با صعود به فینال جام‌جهانی، آرژانتین با عبور از اسپانیا صدرنشین رنکینگ فیفا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/100490" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100489">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYN5nsVCu8LBNJCHW5FzG-8cXpIVWAJEHtX20C7uGm3XsAqTodJiCkdzDqS3clvo7OQKqfMPGSblskCZ5xNyKgbygPlClEztDlNG39dndHLNPzDmaOO3X5f_mtRBAAB8ImyrNlgnXpBagU2ayVXhqKLs0VDleTH7hPl0qZFcFLmzHv435MS-xNbWaAf5RziRk8VUhZZLfWXeca9V3Yhw_BCXHRUOVSQRnjwtPYmfvHM-p9ya8JLtLKSlnYRrw21L6MhOMw0Pflh3e9Pta-P1UV31T3lzK4F_6_liDlVtdMUOZnykYaSg9A-PnPLQ8xPSiwU5eZ0OkQpIl6D-QQBPBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏆
مالکیت توپ دو تیم آرژانتین و انگلیس بعد گلی که گوردون زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/100489" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100488">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/100488" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/100488" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100487">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/100487" target="_blank">📅 15:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100486">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=HAzjOStv01Xhv9yaamfZnxJqXvj0K_DIXQc758jSAq26mAezYgszGMVtAdS3sPsHRaTM79rY-tIQfxe952m5Te9HDcXNxQT3Num25HEPeFrth8YDdx8JLJiBiBaf_ZeC2qK8xYlD3sfpBQT_CuGAuXRRxMx2tgIpbFNGXoPQhSTiihrNiDovJJbTygNIncu35QEmZWHwjRYvlLg3ZOO55whWKUWYW_uZEZQXcxXYIM6K2hkph3p-X8X6vmOwCF58vt7fVSiJTRv3g563xJrzHMNhkT4qGLKYRKW-L5u0_OLgQda82YvRwbpao8qxW-JW3PukNcYZFX6zfJKeWsFdvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9b7cbb4f.mp4?token=HAzjOStv01Xhv9yaamfZnxJqXvj0K_DIXQc758jSAq26mAezYgszGMVtAdS3sPsHRaTM79rY-tIQfxe952m5Te9HDcXNxQT3Num25HEPeFrth8YDdx8JLJiBiBaf_ZeC2qK8xYlD3sfpBQT_CuGAuXRRxMx2tgIpbFNGXoPQhSTiihrNiDovJJbTygNIncu35QEmZWHwjRYvlLg3ZOO55whWKUWYW_uZEZQXcxXYIM6K2hkph3p-X8X6vmOwCF58vt7fVSiJTRv3g563xJrzHMNhkT4qGLKYRKW-L5u0_OLgQda82YvRwbpao8qxW-JW3PukNcYZFX6zfJKeWsFdvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
لیونل‌مسی به فینال جام‌جهانی بازگشته‌است...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/100486" target="_blank">📅 15:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100485">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=SAqBBCWhn1Vx-CTQraAup8p22k_DtViis0bTFMp2gSJ5ja_0dX9hlA1-tPW_vW9TiMfuHXRkqZ3C5ES8eY2Z8buxV9GgS-FflJi9vQ_3pfyoBfHZrQ8WKGZHj62NDmEhGL9AhjyTTGCBbne25RZDLXYELrVfQrSbD4FzJvdNbVTY4GCZjED1A4dHgMHq_zgzrbI9ihwse71l2n8yFpMA_R7WBh9oVDzWtSr4w2p1nvfgBij__jPgHIUVddfWaBUz-FZuK3GH2DFigFmDixsZ67ScPuyQ65r7tPbTABFcvmmm0TX3AUe6GcYq-QnDBv26XBWhWtNBMey4RiePk71Hug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6732c2de4.mp4?token=SAqBBCWhn1Vx-CTQraAup8p22k_DtViis0bTFMp2gSJ5ja_0dX9hlA1-tPW_vW9TiMfuHXRkqZ3C5ES8eY2Z8buxV9GgS-FflJi9vQ_3pfyoBfHZrQ8WKGZHj62NDmEhGL9AhjyTTGCBbne25RZDLXYELrVfQrSbD4FzJvdNbVTY4GCZjED1A4dHgMHq_zgzrbI9ihwse71l2n8yFpMA_R7WBh9oVDzWtSr4w2p1nvfgBij__jPgHIUVddfWaBUz-FZuK3GH2DFigFmDixsZ67ScPuyQ65r7tPbTABFcvmmm0TX3AUe6GcYq-QnDBv26XBWhWtNBMey4RiePk71Hug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مردم لندن درحال تماشای حذف انگلیس از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/100485" target="_blank">📅 15:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100484">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=nLiUy_KQM5NIogGdJwkXHnYfHZpBIEOfId84ai-hqJM8YBHVv9OKSjhC5OjH8eJdzPEhzClCtkRwRvhvPqR3-_8pyannZiGvF26H5y6HMHg9bFchWNjX2FdBGUQZbY3mT5oksLY_Uh87DlqnCIOBqPonMzbjyHXtzK6wlK0mo3_-SVTXtYpjPnTQbQKoJfmZjP_fap9L4rx1V05FC25uRp2l-pBt0hOftSc09fCewvn4KgfMtXjkkNRisx8Yv6zO9wcisF55s3sfnOXhi1zTgBucSjG9xLaUeCooYIOisY6UGSkOdEHy1q03_AIg3lMlF_zoln6PChgs0ZmJUWrKqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0519f41eb2.mp4?token=nLiUy_KQM5NIogGdJwkXHnYfHZpBIEOfId84ai-hqJM8YBHVv9OKSjhC5OjH8eJdzPEhzClCtkRwRvhvPqR3-_8pyannZiGvF26H5y6HMHg9bFchWNjX2FdBGUQZbY3mT5oksLY_Uh87DlqnCIOBqPonMzbjyHXtzK6wlK0mo3_-SVTXtYpjPnTQbQKoJfmZjP_fap9L4rx1V05FC25uRp2l-pBt0hOftSc09fCewvn4KgfMtXjkkNRisx8Yv6zO9wcisF55s3sfnOXhi1zTgBucSjG9xLaUeCooYIOisY6UGSkOdEHy1q03_AIg3lMlF_zoln6PChgs0ZmJUWrKqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
جمعیت پشم‌ریزون در بوئنوس آیرس آرژانتین هنگام صعود این کشور به فینال جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/100484" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100483">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=PDsdpI33x70R9aY-Iy5T9iRXWt38zwUW9tR5ni_neNc2GiUU6O79v6iStkAvVcwXd8HAysTHCpAO0dqN2F-B5XHXAjxHAqPZngfyBNGqR3EScOBn3itpbuUR9yFD0--Tydm810GueldVVpWz8sofNUlsghx4-ac6fzdjshdoFac2JGRXvvCzn8C4JMut2QdWBpEA-qBRLmAkOCA_3IVaSrYkuyDeB7Ic1SacCMV-LkXm0QA0j1QyLbdRKNPmLS0_GYNb0_-2yqly9sazZS59TgkTtlQH2c0Hw84p3hiM7n5F96reot3g-tF6ngCKI7ngWUJijsoTPRvXWkjOcBGZww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b87eecf2d.mp4?token=PDsdpI33x70R9aY-Iy5T9iRXWt38zwUW9tR5ni_neNc2GiUU6O79v6iStkAvVcwXd8HAysTHCpAO0dqN2F-B5XHXAjxHAqPZngfyBNGqR3EScOBn3itpbuUR9yFD0--Tydm810GueldVVpWz8sofNUlsghx4-ac6fzdjshdoFac2JGRXvvCzn8C4JMut2QdWBpEA-qBRLmAkOCA_3IVaSrYkuyDeB7Ic1SacCMV-LkXm0QA0j1QyLbdRKNPmLS0_GYNb0_-2yqly9sazZS59TgkTtlQH2c0Hw84p3hiM7n5F96reot3g-tF6ngCKI7ngWUJijsoTPRvXWkjOcBGZww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
فریادهای رومرو بر سر بلینگهام بعد بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/100483" target="_blank">📅 14:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100482">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=dYZOoP-05gDdZcIUeoewLBr2UT-5_02qb6_TbGQO0xWhvf_z5GumjYcjTnP5ZQqY5IjXjrQh18_YvLMm26H4MYNqJa8kZiw_ehI4RTOKpQXVvpLGJ4qqlkDQAM9zFGFiwBO0_Mprp5mneKu-pDao8hFyS6rV2YcrSKxLRAdWbKD6_q8O8aubL6oG1yEAF7McJew0dUJmoyI3V_ZIuYg99xV2FCrV_2-uNLW91FNzwGe_nKGINNXHfEVkML5cNC1BFgAOh7rFnW0fqvpUZ4VU6zHHx42qJfFSMo2EGrp88JqbwA5kDl86Gh64oQQp1cqh5iRVHd8LVUYSANIcS5ZNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f72bbd0a4.mp4?token=dYZOoP-05gDdZcIUeoewLBr2UT-5_02qb6_TbGQO0xWhvf_z5GumjYcjTnP5ZQqY5IjXjrQh18_YvLMm26H4MYNqJa8kZiw_ehI4RTOKpQXVvpLGJ4qqlkDQAM9zFGFiwBO0_Mprp5mneKu-pDao8hFyS6rV2YcrSKxLRAdWbKD6_q8O8aubL6oG1yEAF7McJew0dUJmoyI3V_ZIuYg99xV2FCrV_2-uNLW91FNzwGe_nKGINNXHfEVkML5cNC1BFgAOh7rFnW0fqvpUZ4VU6zHHx42qJfFSMo2EGrp88JqbwA5kDl86Gh64oQQp1cqh5iRVHd8LVUYSANIcS5ZNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇦🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنچه در بازی دیشب اتفاق افتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/100482" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100481">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq-nQno1gJp2NuBSHZWrjDKMuRvEl97MEPhdPm4XeLds6v2xsLyqtwYy88wXFIEq1VC3Ifrad63JH91kHTkYezDa5UgPpymuAa0VQo688s7P1wgGv68ujCrQLSDDFIMU1nzBh2KsoZ_5Tjn9vCGGTL4pqNb7TSHWagZGamSKenA9C6sldZf8wcNC7b2aWYNPERPbtvbn-DXob-A9bBUZcG4kpbHlflwofSYDli58ZqH0o2ZWk43g8bAL6KrvsU2PK2ue9LuFPyVKgT8xwLr2g8K1ZDP24gPXndfyGnfCCWsAfdkRmyI1LynZiktTLfZI1xo7r5ledNGnEzd2DGFRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محمد مهدی زارع، مدافع میانی ۲۳ ساله احمدگروژنی روسیه، با قراردادی چهار ساله به پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/100481" target="_blank">📅 14:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100480">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇦🇷
سوپرگل انزو فرناندز مقابل انگلیس از از نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/100480" target="_blank">📅 13:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100479">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d71841ee.mp4?token=csknAfXpbgyizyY0aqG9zcsiKCwcBZY6GAlLspjIvsqt5Uj2_8OMjQR5YU3jS4gtgPNCz75jaNjn2yTiGLgxH3Qi4PRE63dK_YqsH2CHxWHE5cylDAyIl_Eb1MId24UxDMANB5mLkZ4T_qEX5LWqqQYJcDkNmJC1RxRRf-lWMgIqNjk3UrrlOtOAFyXFfoGTAdHt8SkiT-se14rufTegG3xZQAM6zY1m15xHmEAWGr5pntlQTd4QPel90TovVRmyfF5Do_xne8oG9oHgI_4oHlqVMiJlQ9l-FrRGYm-fR3d8qaC8xVs3nEgIVO7GkPg2KXpUrLIcdTkrZnM8Rm6UTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d71841ee.mp4?token=csknAfXpbgyizyY0aqG9zcsiKCwcBZY6GAlLspjIvsqt5Uj2_8OMjQR5YU3jS4gtgPNCz75jaNjn2yTiGLgxH3Qi4PRE63dK_YqsH2CHxWHE5cylDAyIl_Eb1MId24UxDMANB5mLkZ4T_qEX5LWqqQYJcDkNmJC1RxRRf-lWMgIqNjk3UrrlOtOAFyXFfoGTAdHt8SkiT-se14rufTegG3xZQAM6zY1m15xHmEAWGr5pntlQTd4QPel90TovVRmyfF5Do_xne8oG9oHgI_4oHlqVMiJlQ9l-FrRGYm-fR3d8qaC8xVs3nEgIVO7GkPg2KXpUrLIcdTkrZnM8Rm6UTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران جذاب تیم‌ملی آرژانتین
🔥
👀
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/100479" target="_blank">📅 13:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100478">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کریستین رومرو: امیدوارم وقتی بازنشسته میشوم مثل گری نویل احمق نباشم و از بازیکنان انتقاد نکنم
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/100478" target="_blank">📅 13:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100477">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJWAzEHa_6-UsX3rIpZd2Hc7_amQY_DN-uXONd6cGzGaiTyg3nFBD6NZwz-8-sYjl-Fh6ZlOCS5vWrr0nVY3-MMmXz4qZy0VZzPJVd0tnKICAk3_DHddb1fWOwthHU4r30gd3evtEvHHIHtZMg3dk9Uz95Zipz0KCzZoINLJ3EYxsVISJRacCH6un1xv3LF9P09RvL-Vx8O4ANeMARsFeo_8NTHORZ8nAP3afaWdZIDQg_yHJNupMcIRswNmc9gQjzYWK3sgll-VJ94oyimXEv_nLliEnTXLgOtauNzEV95Df3z8jYyEX7EKNdJqAnHC_Lw3amYxZzksyYwKneN_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
دو سال پیش در چنین روزی کیلیان امباپه به عنوان بازیکن جدید رئال مادرید معرفی شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/100477" target="_blank">📅 13:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100476">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3896b54423.mp4?token=kJXKbDh_mmPzJt5KwZJR89Gyfs7sWCWrRQ1rwQc-tfL8HnrTt2ThM9Y-l-F4XuHtjs6y3bqSaZRFqAUAN78hIHA-MpAUgdN2mpoIhBN9N78JwT_5OmyQ8ZqwWjQYYOzxmB9j0i7jZi29_MPy1Bqso2rpRBtLa8ydjJZdjX9HwGSpWs7CXHxSaHDa2zLHFpTG7bVmhgDWMaHSx1nOLXpcNFRxIyWe5KjKOf_ZxcDDW1kSQZc5DSwR6jMd2pDUOXplLfa79cmq0-vUaom4Y3RR224j6H7fToVFxG4PrGK67oyr4zUQdFOUWhfK1MFzymSKS9wchyCv2eNtezUuhf9VRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3896b54423.mp4?token=kJXKbDh_mmPzJt5KwZJR89Gyfs7sWCWrRQ1rwQc-tfL8HnrTt2ThM9Y-l-F4XuHtjs6y3bqSaZRFqAUAN78hIHA-MpAUgdN2mpoIhBN9N78JwT_5OmyQ8ZqwWjQYYOzxmB9j0i7jZi29_MPy1Bqso2rpRBtLa8ydjJZdjX9HwGSpWs7CXHxSaHDa2zLHFpTG7bVmhgDWMaHSx1nOLXpcNFRxIyWe5KjKOf_ZxcDDW1kSQZc5DSwR6jMd2pDUOXplLfa79cmq0-vUaom4Y3RR224j6H7fToVFxG4PrGK67oyr4zUQdFOUWhfK1MFzymSKS9wchyCv2eNtezUuhf9VRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
توصیف عادل فردوسی‌پور از کامبک آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100476" target="_blank">📅 13:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100475">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/876233c65c.mp4?token=mYK_TNPG7yHFa50OUfWoUASWpMNFLPbYYPEkwf9wL6ssTXxERy8yQIVYBaMI_lDuHGWYp8OjXKNauOFKV7bAUC6MJkvsmPQV1LvK_ugf-NdTBDqaylDAlsj3EmRgDn9WwT47VcziycYtj4CRLL5f4H2avLtorbvkUG2XHRgiIawR4G7dYKFcoDz8wxhp4DpqoFLcv-dHmSggSPM6313L8zky_o-RCzkTUhGqNZGOGNa-EqXCtj5YTTSSEb86vvBELGgCWxpF1wwxjrMDZOclWz14Emc5MgLNLBO7hs3JTPMBPpI5u1SRRBLnwzro7W3gGfyQozb-D6ZPjMmYklOgOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/876233c65c.mp4?token=mYK_TNPG7yHFa50OUfWoUASWpMNFLPbYYPEkwf9wL6ssTXxERy8yQIVYBaMI_lDuHGWYp8OjXKNauOFKV7bAUC6MJkvsmPQV1LvK_ugf-NdTBDqaylDAlsj3EmRgDn9WwT47VcziycYtj4CRLL5f4H2avLtorbvkUG2XHRgiIawR4G7dYKFcoDz8wxhp4DpqoFLcv-dHmSggSPM6313L8zky_o-RCzkTUhGqNZGOGNa-EqXCtj5YTTSSEb86vvBELGgCWxpF1wwxjrMDZOclWz14Emc5MgLNLBO7hs3JTPMBPpI5u1SRRBLnwzro7W3gGfyQozb-D6ZPjMmYklOgOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
گل‌دوم آرژانتینی‌ها از این زاویه جذاب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/100475" target="_blank">📅 12:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100474">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ade47d4d3.mp4?token=HnJbvXMCi5fJK1ub8Dw7Zd3ql7eA5OIgJFaf_dtaV9JxFlbEMHCq3R7_O-_J6On1NfGbpzjSzpP2yaq9yxknuSW5UlH4XIARinYbWLN-zU-kZly703HuSRad1QsJSKzAsuV0CD9Xe2i5a1MLRMX4Eld-aA_J9Qpgnj8kv1kVJDPfhygiMvDsUFxsfnymfYrqrewip5yehnG4tzTDsMpeyqp4E97v-X8VkCkjABw3iKba9jiO5YunJWhGO3vWOqeLtUC0HFZemmPC7AFLgHDzvDreAunfjtT72oYhdm8zkNqnMXpLLzPsetZNrGW2mJ3zICO0LWUrdB6jBX-Sbit3GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ade47d4d3.mp4?token=HnJbvXMCi5fJK1ub8Dw7Zd3ql7eA5OIgJFaf_dtaV9JxFlbEMHCq3R7_O-_J6On1NfGbpzjSzpP2yaq9yxknuSW5UlH4XIARinYbWLN-zU-kZly703HuSRad1QsJSKzAsuV0CD9Xe2i5a1MLRMX4Eld-aA_J9Qpgnj8kv1kVJDPfhygiMvDsUFxsfnymfYrqrewip5yehnG4tzTDsMpeyqp4E97v-X8VkCkjABw3iKba9jiO5YunJWhGO3vWOqeLtUC0HFZemmPC7AFLgHDzvDreAunfjtT72oYhdm8zkNqnMXpLLzPsetZNrGW2mJ3zICO0LWUrdB6jBX-Sbit3GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
پست جالب باشگاه اینتر برای لائوتارو
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/100474" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100473">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADscQV2kMR2aKCCPwZ4qebTkPB77dkyJPAb7i8zUN0LgoJHIofka3vGoZDpU7rGpZTWNwRclVPzvlNjR5tupg3dwgHmM7ck6Ke_g2epTwAQZZu2tcio5S52EebJVdYf0Lb8Dru80Hh3Bq_vpyqIg2UIrLNHq9bDKn1jTQYq97YDqOkSY2hQ2aJt4xihlrYsj7VCyJP24nmEenjkH306pWKmF7KhiQvcxV0JBojifG4jmsoWudL2uOC3t63STfhp9BCKG9aBdadAgicXN4mHbO282SNjMhiyHt8kwMxeiIQerJJt8kGBb-xOeVBb3qOaq8I1Bsw6ji2SkTqsk9U6nLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب نیمه‌نهایی جام‌جهانی؛ خط دفاع کاملا اسپانیایی و حمله آرژانتینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/100473" target="_blank">📅 12:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tCFnBSN0fkv-36Zt1Qx2RRoO60E6sgwgcWMcKKbRFbViBoCh-pz-7fwLuZTELu8o4bShb3FsXWI7m65NXEasM1Ixvi8J97UPxv69ynAMmFIh-poMYuIR69DDyZnbz-aqJc1kRRszfCPzVnpmvX6qVCLt0VSXvDPSByU93KIsTHW_y4LUZqX9N8C1FDr1N9ERfMXGIRI2DkPPsXk2wuVjWM68B3k8ReQmsoMroA-eRbMPdoAksTf3JPfjhjYfuy9uPaNoJEahS_KWSF7noPhEiU2FL54SgjmLVEMEkws-ccgLZP7z03CRN3uyKAZjXCAYMgfECqexkqEW9i0-9dRHig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fcku8vNIQlJx_dln20ecu2a3g5eOMhQ1zSofnYA-DK2h3e8Dmx6xnLFxhx06pw4-YK13KXzyl10RNKrjS2HOllx-DSrqYgltihPXdmT7W1QFlHN4VLaLDU4Jvw4r4hO7QR1Y0_XxVrsZeAlpDR3hdbhBHgnaOJilUyPQ8BRbRc9kkTjUDZajYzxc8OLfd-R7kSziyBdv6d-FNkmX1879jwEaIBFRwZdjAptBFTsYcIbkdsHY6MFeg5XBBa-FM2LC39tJm6cSt3a7FxtAw-nBubQaTwyjCpRvwx3URv3H1VivxgQoztKxCsePeefmCvAD_ulbGDjqqLmG3v_0QEx2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fl716EN2vsKaQuv5TWEz16qHTNlnrYInyAKOCJw2ZrZRuWGp49BWmvvGvBCmwux4U3A2Y-p6pelfb8NqcrpPx6q_pkcumjWUcFgBytQMJVU9aGhzMUh-UM9TwXz2L8dR_AGM_Za7xcqTOQAZVwSrM0rkGtZYAKQp-TyMThEovySm9Wm_O1WpkDG0jjSueRPWQugv_1FUvMJ0uEjLEQWHOGW8zAsDw6Dcdpr6pT8Eri7P9Q2PGRzdh-NdalyckJ58KSCPi91Eyv5G2NLV9tmfLTBmoSkXTH2XMTAxw-_j3irCHrE368JK71cdLmBmw9Zcoxc624gXuit-ugoVuNFSKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚠️
📊
مقایسه قدی سه‌بازیکن مدافع انگلیس در دقایق پایانی بازی‌دیشب با لائوتارو مارتینز که نشون میده قد دراز همیشه ملاک موفقیت در نبرد هوایی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100470" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100465">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pt-Ybj748mT26RIytsRf1bD4cDawiGps6AcSC-3RQys6xhaLxpUKl-3WQJ4PaMvTCBF4jMakNmUqB435rFIaX12s_0L6pYDwZfIexj859YTMQpKOZIUKelw2HScEnpVWMtoA9bW09gfcQSsrIVrFuUntXzucXGT_NpJmKbs2XSI1Ce4expwC6mxQDvLHuEDXEHRrpDK50sep0nTxHNhrjOue8jU47dy6Sysu_zlCzFSX4PQaMko0KyZc4Fr4VcJKxSKXosB1-OATsSQ7kSiRM2FiMSq8OS2VNfhcP_hzbn3XVBQmis-uKgquSySEhg5EdpG-qtbtMxocEJ_ch3ipcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bSxwf_KZ3VOeEwGQ3QDaMrgTpEvUmk7qBa3b-mqkYkLtODXiMf2axhz1djU8Gu5_wAmVuNRV0fAOp0I2bWvrSNff15226hqOj94l_XapV1AUPNZZdxOFWXwa2wHLRUb2sTrEt7bsSLEwfn9NYZz1H8fJwjw_t-Sl-iK8hiRIRRbiapzYP1XG4o51MLHYPLtTIojjhKO1gyBuGAWiq9yiuRJ2PAWIRRT_40jCZAQUK4T5ORSVuATVW43UVztVPHHG8WwEXRnJ7A4QDbtE5lKemc6uecEwSz__0gFoqQV3HeiNce-9Oelv3aEhdACvROutjQb7Q8jqRtEcksqFs8_6VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v_Uzy-YnJiP9dR8BaU-0ienlXvlcxC0mr7dFKDOsva8w6uKDp6fDQWQBn-sy1XR8eTD4i2X6zPiy_PD2EJcg8U6wa5tcZc-sEbpAXkbydzcRh6AahV5mC4E6Pe-yPnfivCE6t7zV0XIPRGsGEi8tL8YZXpvPjd6qiqOSVemCnhjgTK_17aydv1P9bBb0UPREMnnRO2ZeuhCvfMlw3fV_HyGQyiVqbAuYZW-UMgLOdSEx7cNLCyOO4nHfC_K4VfQE47CbOoIwsJzjEVn9waksAbT7lnqyClNN77zOT8eKXdUPHBVAMX2wj6qiPXZiuV9oHHVclW7PtdOwz4PAo_mfDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sxbUDOQ0_Mo2HbUAtXvWHZCzXn8236Jzj-3HfxRHSvBd457t2OEAil8XNqlM1ffRCMqtaDqEcOxdBrVN41j39Jr2iCC-Jy12OhJgOkt91GdUFOSMyNDjn6MMguFF0xo7UBsxwjUiZVAxYh3GKYHaOknXFhTeTJg7Z0zA-PhbaaC0WDTnOKFoB5-joi0U12MAUHq4d3WsVaOhB65U5Jq_Wx92ONII6LJaAdxYpQy7yFKJeUjEX6TvoH9QCG1o8TBc2YutWezx-OCHBa-jKaisLuYiKbXiOIVx6n-84khbgP1uNivD42LwvneCjVi8UNqTy1jiyQE5nR7kG5NA8TGiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMnixf0JmXFLFWnxomV1K3OBGI-KbtFLnX6uyzh6mZXu0GwU77jTpteE_LMxf7FAZgreNtfp0CKTGujx5vxN6fLQtm7kWCKVz67TiqmcB37FGOZmHKvzYEn1nmhfb3LD5O0heKA9scKj4IKTyT9INvuDpW2u09bWbJ4YRZsOJgqPsEMkJECO81zuYg6iQt3oiVdrlhMAeZCpKxXtGLdMZ0ME0gQfExUKgKYWeQ1D4JHOguII3JqdL0p6PqPnciEd_u-3kn4s9f82ejVLPaLK7cNVnKL0cz2UkNYqvdVoOg1aNz13P5jO4KoMnbS1AneknsTcDvlvJ8a1w2G4yyjfnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🙂
اگه یه روزی بعد دیدن این عکسا میگفتیم مسی قراره با همین بچهاا فینال جام‌جهانی بازی کنه بهمون میگفتن کسخل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/100465" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100464">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7cca92eed.mp4?token=p6KSHyQBL778Ry_ZD3xdoMgit2o5Y44hH28JT1A_V2hcwEdYnmGylBbEZjHrQda-khJTg72_KKPnhNoR7m08yg5jf_gn_3aWktc6wGLLGItj_uc6vn6tCO1m_nydbeBft3TUVbCK9moarUmrqOrOiiDi7kV6pR6AjKOanFkNUbEBJ5F2nr8TAL_-m0UqVCP7yQmIaQhp5uVRHZkcWpywoj7g6-etZ7m_7-F0eiZfHhTiaZEuPMgQbQFUpTZC8Tt5H1rX0535bqBjM5Tew3BPmjNIZLJW_lGAOeR0U_ZnSzKQM9w0hmcIoVtD7Kr2zGXCbKXUZJ1whgx1Aj8PmYNEdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7cca92eed.mp4?token=p6KSHyQBL778Ry_ZD3xdoMgit2o5Y44hH28JT1A_V2hcwEdYnmGylBbEZjHrQda-khJTg72_KKPnhNoR7m08yg5jf_gn_3aWktc6wGLLGItj_uc6vn6tCO1m_nydbeBft3TUVbCK9moarUmrqOrOiiDi7kV6pR6AjKOanFkNUbEBJ5F2nr8TAL_-m0UqVCP7yQmIaQhp5uVRHZkcWpywoj7g6-etZ7m_7-F0eiZfHhTiaZEuPMgQbQFUpTZC8Tt5H1rX0535bqBjM5Tew3BPmjNIZLJW_lGAOeR0U_ZnSzKQM9w0hmcIoVtD7Kr2zGXCbKXUZJ1whgx1Aj8PmYNEdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کنایه‌های فیروز کریمی به قلعه‌نویی: تا الان سه تا تیم تو جام‌جهانی نباختن که دوتاشون فینالیست شدن و یکیش ایران بود. این برای ما افتخار بزرگیه و باید جشن بگیریم
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/100464" target="_blank">📅 11:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100463">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ba5270ee.mp4?token=GagFaE8Qyq-Y9ClnjWeUJlUe4TlvHTwWd6aFXs67Cvk0aNHWWcaJ6PpC594hg1MAPCeCplpPBvT32FRf5xMgNsHbHYmQfMtMEF1YpFcAleHM_pX6VO0MtEJ6v3INI6VbqpxN6cfNlmqiCUiynDKF15aUYcFW5ZxtVc5pnKJ6jAdhKj62CMtlN_9CAWFIvTVKNOMUG-0C9Aq86_ZmlYDtwTh5OvUA0JluDm-3vso3ApsgJ0m43XIwRTSDGKCr77-96J_0KhYbWBlaAPpTlzUmjxH1HvZivjepUXsS-tmRit03-ovL0_IEBp6BiC2wL4oWY9_-7_xgJDeuko4GtrqhWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ba5270ee.mp4?token=GagFaE8Qyq-Y9ClnjWeUJlUe4TlvHTwWd6aFXs67Cvk0aNHWWcaJ6PpC594hg1MAPCeCplpPBvT32FRf5xMgNsHbHYmQfMtMEF1YpFcAleHM_pX6VO0MtEJ6v3INI6VbqpxN6cfNlmqiCUiynDKF15aUYcFW5ZxtVc5pnKJ6jAdhKj62CMtlN_9CAWFIvTVKNOMUG-0C9Aq86_ZmlYDtwTh5OvUA0JluDm-3vso3ApsgJ0m43XIwRTSDGKCr77-96J_0KhYbWBlaAPpTlzUmjxH1HvZivjepUXsS-tmRit03-ovL0_IEBp6BiC2wL4oWY9_-7_xgJDeuko4GtrqhWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇦🇷
😍
بغض و اشک‌های جولیانو سیمئونه‌ وقتی دیشب راجب لیونل‌مسی صحبت می‌کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/100463" target="_blank">📅 11:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100462">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d647b8c993.mp4?token=vQUWkUj9LnGeyTJ_i96dQJlegNmuENnQXnMEu0itbCPBpkfBVPVkPlvwII9L9qwZkuRaST1mlYXcpb2UXjFNJOK37rKaIEBdjprm1Pc_P1vGGGqLDRPF9FiBMLUD7ZJKQPSuth2PWniy9GjhkKYcXwUhbYPiu_aQGiWEAeyi7oXnCuLuiiAOnDvzXYfpOXQaP-BfcLALc1hp9VPiGFesgJrn1hqWJIY6Wp9q_TnORKGRepRPMvn6oIpQLJzbvY71MSQdPdOYp3WglLe2u0xPCYUdaaiseRW8lr1Lk94lflrRpH96jFK2P_jO1TMr59zXvtc9mE4glLsNnpVcupMfLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d647b8c993.mp4?token=vQUWkUj9LnGeyTJ_i96dQJlegNmuENnQXnMEu0itbCPBpkfBVPVkPlvwII9L9qwZkuRaST1mlYXcpb2UXjFNJOK37rKaIEBdjprm1Pc_P1vGGGqLDRPF9FiBMLUD7ZJKQPSuth2PWniy9GjhkKYcXwUhbYPiu_aQGiWEAeyi7oXnCuLuiiAOnDvzXYfpOXQaP-BfcLALc1hp9VPiGFesgJrn1hqWJIY6Wp9q_TnORKGRepRPMvn6oIpQLJzbvY71MSQdPdOYp3WglLe2u0xPCYUdaaiseRW8lr1Lk94lflrRpH96jFK2P_jO1TMr59zXvtc9mE4glLsNnpVcupMfLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
لیونل اسکالونی در تمجید از مسی: "اون دیگه چیکار باید می‌کرد تا ثابت کنه بهترین فوتبالیست تاریخه؟ واقعاً دیگه هیچ شک و تردیدی وجود نداره."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100462" target="_blank">📅 11:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100461">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45e92fe93.mp4?token=Aeq-s3KsfsyGTPaDKqFmRwHrflawrHJRQcnnjHC6k9ByraZzlisD5S2cwS_hI-D2f0MTM-F6kkyMl8Cm-K_2oGNe4WXoSuhP-CPjBtC60IcE_tkLmGZM18isFkzzn37xhRBCixxCmy7Ed9Tac4sk4O63ediTke64s3eegQRtEWgIjQeaoNcYHiVM3EWArM9db1phkDNPRBd_n6mwUA9MRYEXnwCf_08n79pA2WELbIjyfsTTpFIjW5LSEVsMAlcIcLjIkJ0vV-iO_iJX2SrjdMeeJ4qqgntPcIdHhnxNq1K5pc057dVYLzZvB3jXDtrMg20okJwdM9QaXa9CSwwuMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45e92fe93.mp4?token=Aeq-s3KsfsyGTPaDKqFmRwHrflawrHJRQcnnjHC6k9ByraZzlisD5S2cwS_hI-D2f0MTM-F6kkyMl8Cm-K_2oGNe4WXoSuhP-CPjBtC60IcE_tkLmGZM18isFkzzn37xhRBCixxCmy7Ed9Tac4sk4O63ediTke64s3eegQRtEWgIjQeaoNcYHiVM3EWArM9db1phkDNPRBd_n6mwUA9MRYEXnwCf_08n79pA2WELbIjyfsTTpFIjW5LSEVsMAlcIcLjIkJ0vV-iO_iJX2SrjdMeeJ4qqgntPcIdHhnxNq1K5pc057dVYLzZvB3jXDtrMg20okJwdM9QaXa9CSwwuMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
بطری تقلب پیکفورد که دیشب دست بازیکنای آرژانتین افتاد و حسابی سوژه خنده شد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/100461" target="_blank">📅 11:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100460">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔥
🇦🇷
جو فوق‌العاده رختکن آرژانتین که نشون میده با نهایت اتحاد و شایستگی فینالیست شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/100460" target="_blank">📅 11:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100459">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
‼️
⚠️
زد و خورد طرفداران انگلیس و آرژانتین بعد از بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/100459" target="_blank">📅 10:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100458">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3773c9a4c.mp4?token=u91ezT_gxJZg1ojx6f8x_eH6iXLSx8DSB5v6WFWC0IaTUXt7MG6Z-vszI15qTu142Bv8_X2sEjqhqutQf-ke-00Wi4kUNOHBbyGMf2Da-oRnE4eYptiDNNrSAFC6pRcBJyEBAmQglrjc2KdM2NLXtnyRj8p3MbBGW6Jtw2_rXTYX3deC6zVsSH57xO8WPaShkbFuqC6U-ys2Z4zWhqCifSrcOhU_HI-0C21eLLnYyCD79o6ajKFBmNl5pCXrzRWdB-6H25hvVHaeLAjH2XFRoemeGK2YMy2aVg7Ui_XwTZ14JmPLVwf_Kyyc5VGjXnAYBfIy_wdMx5d7PBVy3eiA9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3773c9a4c.mp4?token=u91ezT_gxJZg1ojx6f8x_eH6iXLSx8DSB5v6WFWC0IaTUXt7MG6Z-vszI15qTu142Bv8_X2sEjqhqutQf-ke-00Wi4kUNOHBbyGMf2Da-oRnE4eYptiDNNrSAFC6pRcBJyEBAmQglrjc2KdM2NLXtnyRj8p3MbBGW6Jtw2_rXTYX3deC6zVsSH57xO8WPaShkbFuqC6U-ys2Z4zWhqCifSrcOhU_HI-0C21eLLnYyCD79o6ajKFBmNl5pCXrzRWdB-6H25hvVHaeLAjH2XFRoemeGK2YMy2aVg7Ui_XwTZ14JmPLVwf_Kyyc5VGjXnAYBfIy_wdMx5d7PBVy3eiA9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
۲۰ سال و ۶ جام‌جهانی و افتخارآفرینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/100458" target="_blank">📅 10:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100457">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0ff21890.mp4?token=XX7KOzZPB6P5ikAIGd-wcAQ7EmHIgVARkJgBNIfP5OHopqQdBnyVa9xSClIV4pJfThvNwsjZSgrRJmvgQTBnykDSYcyYsBu6N5MteidLY2fMSeXEZNb4Tsh9Y5Rfq5dfP4u3FAC6Bfd2lJkJq0i3AimYdca-K924Y9THPxifLrXR2sgUtoP6czOz2SKd8fsmVRHCvvdO_V8StATINi4MQBTBUiRMHY0Vc8mhDPEyOMSN_isEB7uPp8IgvUHABrJHsMwSZe1ndgx_Skgpuk5K-eglekpotRMYA5Elhvoqn5RhXyvPMQFZBEGs5UOW1U4P6J4so0f9w0gc34ehIyQ0Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0ff21890.mp4?token=XX7KOzZPB6P5ikAIGd-wcAQ7EmHIgVARkJgBNIfP5OHopqQdBnyVa9xSClIV4pJfThvNwsjZSgrRJmvgQTBnykDSYcyYsBu6N5MteidLY2fMSeXEZNb4Tsh9Y5Rfq5dfP4u3FAC6Bfd2lJkJq0i3AimYdca-K924Y9THPxifLrXR2sgUtoP6czOz2SKd8fsmVRHCvvdO_V8StATINi4MQBTBUiRMHY0Vc8mhDPEyOMSN_isEB7uPp8IgvUHABrJHsMwSZe1ndgx_Skgpuk5K-eglekpotRMYA5Elhvoqn5RhXyvPMQFZBEGs5UOW1U4P6J4so0f9w0gc34ehIyQ0Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
پشمام از مردم آرژانتین بعد گل لائوتارو
🔥
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/100457" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100456">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f94f44a2a7.mp4?token=rhXEBb7rowIhKZjz-7GaQ1W4oiTgCtP241qEIOAhCQa1PqEjNSzu92bWszY2p-RowfrCwDS6Prq6tUQ8FjmAX2rIrhvopO_984FlX6ykoKjkyep393tEiOavrKVL841SdMDXYxF8LrW2OaCxMzIl1YUBuDnf7Ksg9reO_UMJ9zq1RwaqHyrxOg7g8ZrK_xwg36eomd6zytvQrZubJ7L1kF-40pB7RaR8zzAL2tk6CEFBIcGGEu_7VMdoHPW8yxRY7BNGaBGxD8-p_UVpKbgL7XwBnnwC1oEeOgcI2Cgu1OaN7_g7afhcg1VO2OospTwtcbIT8gWrYp9KDpMELc-RuRGJ6_5wwyqew_7nhQpPBirrkLDKK2YFivdYnf5ajlb5_LmxJ1XxRImqJXsBLw3Jvqe1BRMsGjTuGvjOx18mCpRiiYpUNSJ7q66JjlY2h4juWKvyyZiaLCsWUrP-_CsvXvUF1km3uq8Fly9knoyiKo6DGGNaNiZSGteNfqu9uQ0fW4N41-XD2bO61KhQsC0qRLMCaQ603YGrbGxREGfOAgSP51s5ITWu6cuPR4ndAQo38DEmc-nQ92YHqdHv0LKi97jre44j7PNcKOQOfsiSwNQPPl10O72lP3jz_HE4ccm9qnGG5ajRrrQitTZXHcf4nGo-cYCWYI6Y08IO0K0qvNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f94f44a2a7.mp4?token=rhXEBb7rowIhKZjz-7GaQ1W4oiTgCtP241qEIOAhCQa1PqEjNSzu92bWszY2p-RowfrCwDS6Prq6tUQ8FjmAX2rIrhvopO_984FlX6ykoKjkyep393tEiOavrKVL841SdMDXYxF8LrW2OaCxMzIl1YUBuDnf7Ksg9reO_UMJ9zq1RwaqHyrxOg7g8ZrK_xwg36eomd6zytvQrZubJ7L1kF-40pB7RaR8zzAL2tk6CEFBIcGGEu_7VMdoHPW8yxRY7BNGaBGxD8-p_UVpKbgL7XwBnnwC1oEeOgcI2Cgu1OaN7_g7afhcg1VO2OospTwtcbIT8gWrYp9KDpMELc-RuRGJ6_5wwyqew_7nhQpPBirrkLDKK2YFivdYnf5ajlb5_LmxJ1XxRImqJXsBLw3Jvqe1BRMsGjTuGvjOx18mCpRiiYpUNSJ7q66JjlY2h4juWKvyyZiaLCsWUrP-_CsvXvUF1km3uq8Fly9knoyiKo6DGGNaNiZSGteNfqu9uQ0fW4N41-XD2bO61KhQsC0qRLMCaQ603YGrbGxREGfOAgSP51s5ITWu6cuPR4ndAQo38DEmc-nQ92YHqdHv0LKi97jre44j7PNcKOQOfsiSwNQPPl10O72lP3jz_HE4ccm9qnGG5ajRrrQitTZXHcf4nGo-cYCWYI6Y08IO0K0qvNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کون پاره لب خندون مثل اسپید کسخل
😂
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/100456" target="_blank">📅 09:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100455">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKLOk5v_KXj7jTyeffCmv3z9gTgYjCFkJZ7Zsc7xN_tFRHfhVhK_VXlrw-3mysZtGTl-iqB8H7MyNEvZK_hCvBhpQZXgpVQbF0zRxpPN_EANIFPfr6dWKIt6w08bEAtQP40-AWN5tZCb0bM6Fn79_Iv-oMhJWlP4g9Smkrty1rf4mwzZG101jFkhUj1kIv960yHO36TFEi7Dz5isJ9r15BjB0coT6mX1lB2pf-9cdFwGpyIQpKeqneVzFv8DfDMrK2xYVoc4oGYXd3I7jSwwFwZPh45CFVFuV8gyx-4xN4kGst2B-EWRHR_AyPXDBvRyCBIlJjCID9eO8_LmNA29VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جود بِلینگهام: "برای من، بازی کردن در برابر لئو مسی فوق‌العاده است. عملکردی که او در جام جهانی ارائه می‌دهد، شگفت‌انگیز است. برای او در فینال آرزوی موفقیت دارم."
🤝
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/100455" target="_blank">📅 09:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100454">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f5b199b9.mp4?token=fV6_J0OroMSvpBzoeMPycPcS-WfptwuA8lMXALcuhHeZVZZsc7pcac2aBmB8S51GFFmzD9-EkWz5tfivG1Re5uicCQtbcJVUufwO-7rCgv-c8Vh82TQ9Br4uT9almYjgjmvqTwrkXynmQVP_jYSPqZztNKc011lIbJDbHPup9Fife1sfNleI9pbuDoPAOj5rlQjXaXXSPMPlCxYeEze0O3UIYAg_6A56PLYmeoLMtzDr_977amVS3qL2iBaNB1bKPpNHmChVeU4ykU76NxBv-eUqyDy9dNx6FO6oQ8-_DFr5utHrOeMtGMRu4h4tPyw9fM0tWr5PWwChKh1xhlJUgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f5b199b9.mp4?token=fV6_J0OroMSvpBzoeMPycPcS-WfptwuA8lMXALcuhHeZVZZsc7pcac2aBmB8S51GFFmzD9-EkWz5tfivG1Re5uicCQtbcJVUufwO-7rCgv-c8Vh82TQ9Br4uT9almYjgjmvqTwrkXynmQVP_jYSPqZztNKc011lIbJDbHPup9Fife1sfNleI9pbuDoPAOj5rlQjXaXXSPMPlCxYeEze0O3UIYAg_6A56PLYmeoLMtzDr_977amVS3qL2iBaNB1bKPpNHmChVeU4ykU76NxBv-eUqyDy9dNx6FO6oQ8-_DFr5utHrOeMtGMRu4h4tPyw9fM0tWr5PWwChKh1xhlJUgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی خودمونیم بدل هالند خیلی خوشکله
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/100454" target="_blank">📅 09:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100453">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBy4pf-7QS6BfZD7NMf6I8d-HkE19XMVqdXtvgiujV75lPsqOB_zTIMMGSAP-EIobdDkKST_FQyHrUUr-15fDnAflKdndyw3tfcTkrXwh_TmmGBJeXfd5gzZLtgBO_c-2EqxVbd914WRncOL0QeC55BHua3p9BAzC2ZwoWfUMUouF6Zu_6YG3zpEK7qZUTJsftYGCf3qwh6hVE3LqwJ4BAfypX8lL3yZ9UlWXYeaBHpu_HJ2_5LC-PN2mjr96FwN5IXYCHX49wxgSoZ8lVATWzQqCcKyuZCUbdf1qj71nHRU4d-LiInd-OMwoBLV8D_gdx7hm_CDsAStdiwpS7VPKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
| تعداد دریبل موفق بازیکنان آرژانتین (به جز مسی) + بازیکنان انگلیس در طول کل مسابقه: ۱۰ دریبل موفق
🥂
مسی ۳۹ ساله: ۱۰ دریبل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/100453" target="_blank">📅 06:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100452">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENYqwwtjhayDtZclRNzzZyw58okHW7bOytXVwyGmt52UBpAxtqNkkP06YKozKk0426CqETaHo_Bg42WhdlenQy48FxpXd4lOrDQCvq0455bTCrrmE5-AxymXyKfxnv8MbT2jY1MPzdEoIAP30xgg1uH7HjQPphmxyI4mVT-O1ytnzWGHBKzEg5NqZeHv2hOojrUkEBhiohltLfLqp2w-5XNr0wU1RHpx3f2NTjCnDxUxYUMlaOIYml5sVrAGGyChPACTx2M8b1mU1RtBFMwpN2ckLcfzZp0CQyY-4JDp1pGhVTlSZRTM67Z1yeSQbAKuUVVlzYErdBOV1A97VDMY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙️
لیونل مسی :
🔺
من خیلی از بازیکنان اسپانیا رو می‌شناسم. خیلی از اونا در بارسلونا بازی می‌کنند، تیمی که من عاشق آن هستم و هنوز هم اخبارشو دنبال می‌کنم. این مسابقه بین ما و اونا بسیار نزدیک خواهد بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/100452" target="_blank">📅 05:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100451">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de6a52447.mp4?token=URhzK44T3r-KY6AYN1IgQcv2YdbOE-P-mfe33S5iGlwCO_pScO78wnl4O8_3ASHsQi8AXAuaAB3n_C2RpgnG2EZsL6uD5gp6NIqVLkgDHo4WASZxPUVLm5uCzdS5xRnzJMsdL-a9AVfTUOfaVh5BGQf8zL8tAspvBng_vruiAkwyljExw5nlinTPolJMpD2yahf0fwzja8hjJ3f1p5HGqKyLkureHq_iD69S5PiHbS87TtHopUtcMWNnmRKsTNYbtQTxyU_b6aUthrm6GV2ibJYURRhfJkWebVosSeMb1YlDiOXjNWnY9W5dk-BvBmojvy2Jo3-84gGfAtNyOLoIQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de6a52447.mp4?token=URhzK44T3r-KY6AYN1IgQcv2YdbOE-P-mfe33S5iGlwCO_pScO78wnl4O8_3ASHsQi8AXAuaAB3n_C2RpgnG2EZsL6uD5gp6NIqVLkgDHo4WASZxPUVLm5uCzdS5xRnzJMsdL-a9AVfTUOfaVh5BGQf8zL8tAspvBng_vruiAkwyljExw5nlinTPolJMpD2yahf0fwzja8hjJ3f1p5HGqKyLkureHq_iD69S5PiHbS87TtHopUtcMWNnmRKsTNYbtQTxyU_b6aUthrm6GV2ibJYURRhfJkWebVosSeMb1YlDiOXjNWnY9W5dk-BvBmojvy2Jo3-84gGfAtNyOLoIQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فینال جام جهانی 2026: اسپانیا-آرژانتین.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/Futball180TV/100451" target="_blank">📅 03:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100450">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzXvsoSNYXU5VSCXZLF4M4nk8EE2iyv4K2xBfCatbHAAxx-FBqUewuCxPK7wTnG2OJaJ_uoapOBDHVzSbNZU3wh-DD4fiBlazErbs7HkWVnnZLOQtbyvRxK8Le0BRUyWDygdq7ZiDFtTa0f63aL2wsKdvlQueO7xGcsDDg3TKa0Ez5kmTodlExES8jnVuw8VE8eDwIbBY5GB7wh-7Xb16qkKa7YxcHL6rUUvNMzHkImec1Q1JtNcL4IfcfWHZ_Z8cyXNHlNnLYip6rTC3druLIOyX3huk6ni6NV12lRxvaBPzhHLZg2E9Va-6GR09nDf5bw3B-U7i3xwCH-Pxtghkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
📊
عملکرد لیونل‌مسی در جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/Futball180TV/100450" target="_blank">📅 03:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100448">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6FIZKr9d5uq0B9uww19Oo5Jv4jm8NMo8LBPSIZejXozhhUUTu5RNgWOG6gNtLuZwDzBRXYEcKR5-1RDdGnYj-ZqbhrrZmCqDwvlgX8SeswTmCb1STo--K16Yk1IyiFnDa8j10-GmMOTRcq0b59VrJKUErWB5yB5e6vCj1AZov0XnYGjpPUtkcRH3YC0knbjaBvzJxYC-mVN8uHB4IzdTfrJmeSlnlZjWRRBsHOonsIsT5RsZhCFdxG-WprnWCl09S03pZuw8YQgOaj8qSYoOJTY12Lw3qE6lsAXsUoHrO1vM159HCc8lRagYIkx7pdAlaD4vmFzLf0c0OAT9D83uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فیفا ممکن است تیم ملی آرژانتین را پس از برافراشتن بنری با عنوان جزایر مالویناس (فالکلند) متعلق به آرژانتین است جریمه کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/100448" target="_blank">📅 02:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc7a9f6c7.mp4?token=Mv7KkvslRlgDn9W0Cf1KVrpX4MtwI3JygiDleXbXYTeeUfN8wr5rouFBrTLJ8nJvuf5dZQ_dWpqnz1BTmyBx4iFSX-_0LAE2p1LncuXskgiDFSpAiI0Nt-ilpRsgbEeSXzm-c0MtZU0wnikohPsy3-SBub-4YLgjei8IBmVdqn6KMSvmZgneFv3rHPR-dTNhklzKCgeElZE6BGgYIIO_Sn6UW5isbb3ycvSeV0k8sgBVWT6vsa6-MT_UOy_qEumgYYOAgvscpZLbmEV7DUB2KhelYlNWyol-ouRPtLvORP6PMC4ML0DZ8bYec558A4R-z8RqxYJfG6vm48DSauA6HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc7a9f6c7.mp4?token=Mv7KkvslRlgDn9W0Cf1KVrpX4MtwI3JygiDleXbXYTeeUfN8wr5rouFBrTLJ8nJvuf5dZQ_dWpqnz1BTmyBx4iFSX-_0LAE2p1LncuXskgiDFSpAiI0Nt-ilpRsgbEeSXzm-c0MtZU0wnikohPsy3-SBub-4YLgjei8IBmVdqn6KMSvmZgneFv3rHPR-dTNhklzKCgeElZE6BGgYIIO_Sn6UW5isbb3ycvSeV0k8sgBVWT6vsa6-MT_UOy_qEumgYYOAgvscpZLbmEV7DUB2KhelYlNWyol-ouRPtLvORP6PMC4ML0DZ8bYec558A4R-z8RqxYJfG6vm48DSauA6HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ری اکت توخل و اسکالونی بعد از گل دوم آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/100447" target="_blank">📅 02:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100446">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a03939c70b.mp4?token=LreSxgSkbcXJkRlafI_AEzWVjO0KeVMuPIjcZDKpo3T8h5EW2OKqx2q2KxXVSL1TlIaYHy_KlpOSpyZ6wK9DZ1PrtxFwVfwFlFsAzXlvhkSvpp7DG5epZ0a5ciOUhqrwjhMc2BwT1lj2OyywXhNJZ4ci3IHLyIjsqE6ePBD43GubLd6q45M8edtflcfCc1eLvKdc7kfJ9L21ujOi0YVfUHFsNqxIzIyoTRTGTsKxSKzmcqaeZGztU6i8pN5xoiXVEvcRC9jdr9WMCj_s2f03_-5-y2PQvHAd7xUEt8Kuf4U7iZgmVWSCEH5f8_Iy9v0FEeC52ruF0Pdxnc-YDWlkcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a03939c70b.mp4?token=LreSxgSkbcXJkRlafI_AEzWVjO0KeVMuPIjcZDKpo3T8h5EW2OKqx2q2KxXVSL1TlIaYHy_KlpOSpyZ6wK9DZ1PrtxFwVfwFlFsAzXlvhkSvpp7DG5epZ0a5ciOUhqrwjhMc2BwT1lj2OyywXhNJZ4ci3IHLyIjsqE6ePBD43GubLd6q45M8edtflcfCc1eLvKdc7kfJ9L21ujOi0YVfUHFsNqxIzIyoTRTGTsKxSKzmcqaeZGztU6i8pN5xoiXVEvcRC9jdr9WMCj_s2f03_-5-y2PQvHAd7xUEt8Kuf4U7iZgmVWSCEH5f8_Iy9v0FEeC52ruF0Pdxnc-YDWlkcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کل کل مسی و بلینگهام
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/Futball180TV/100446" target="_blank">📅 02:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-100445">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fyl9yqZH3PZUdOCVjwMj9xZXNIMAn4zG4-K4mXIk41DaUMcsPjyAqYyiH9KBGqAcQjyYk_um_EJML0S-oDSgHIx70QQOcqD77jPYNuWbzMhe3w_XCp0bEIRJopmR1ffR33sJIAgrGquTPJSL-zPYAyYzgusNG_Qw3ixr_15vcxWMDeBkCTMI_Knvw4w_A3bwpSX_VWK-mEtDK2b1dCmE4_Xtp0m9zYj0WFbc47Z4-h53TuDiTyeCiD4NxJbvfE2YFMdDpV-GXdnyYbShZWRqdMwx4IR7dDGFcafDz1wmEiKP9Msx-yEXgRsDEAdacO1Zpge2uc1U3Xn08ZZwTdSWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لائوتارو پس از به ثمر رساندن گل، نام مسی را که روی پیراهن او نوشته شده بود، بوسید.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/Futball180TV/100445" target="_blank">📅 02:34 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
