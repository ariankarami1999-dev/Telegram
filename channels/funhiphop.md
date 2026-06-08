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
<img src="https://cdn4.telesco.pe/file/scMdUgBIEbdDAyvEY151G_O9QHCtWrU7SDOJ-2Hy1gM3JCVdmSsr9ibq77r7fwKnJoA55JEh2iY08xYzv1OIUBlo2c4BX3buftR-rzjZaxlbh0ZvBcBRnwHhM3wJQ4ft1WRvgGb96irZOBLQtU4LlhZT4UTgqH6Utk80luwb6Sssd3BxDi41YzmJvtZo0MIBLvInJSK44fCFzOZ2xbREJ0HLxeN_GSiTWG2Ea10qDaaEXzRfLKtK-9WXuULr_-Nam3vE1IqUWLbXXcDsjaNRZF7c7uTQLoVZdoVGJ9ov3YRx4YkDjnZOW7L3Zphaz347V5cI-54SPyZQP4CoTkkwrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 174K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/funhiphop/77297" target="_blank">📅 20:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/funhiphop/77296" target="_blank">📅 20:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پدافندا بیدار باشید باز ترامپ داره می‌ره بخوابه:
یک مقام ارشد امنیتی اسرائیل به کانال ۱۴ گفت که بازگشت به درگیری شدید با ایران ظرف زمان کوتاهی تقریبا قطعی است، احتمالاً در روزهای آینده.
هشدار بالا در هر دو جبهه دفاعی و تهاجمی تا اطلاع ثانوی حفظ می‌شود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/funhiphop/77295" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">می‌نویسم امضا می‌کنم آمریکا برف امسال رو نمی‌بینه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/77294" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERHjQuELyAy4kvUibcB5dQX-7sUbCknwQ-sjeEgeIPiX9cowzr9PkJ8MQ_eO4G2mZcUEexhdf_DnJ3wkInHYymsI5AiT1baymHPuF-UVmM6ZtgcMhXRW66XS24SBZQtbeOVxRwDzx6kKiAgpcreHxwTOv49gIFetx9vk9nnxF4U5IVsZvx4tAI3sTPvYP_fTRyQClx0QcKitqPPgnWMAW9YnzpJUY7bGAmzILs7_Za0D5z-TGA6d5tGobIaPt03D6rd5y3hb7Da_-HwmX6zp3t9zXr9VZtrxdqB03qeLuSvd6hMi7gBBIs787R6Y5Q0ZKrmf9CZa9pJReKYWdXbyjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان عجیب پروفسور بقائی، سخنگوی وزارت خارجه:
تحقیر نهایی آن‌ها زمانی فرا می‌رسد که درمی‌یابند سلاحی که برای تسلط بر دیگران ساخته‌اند، از بند رها شده و اکنون اراده‌ای مستقل دارد.
در آن بیداری تلخ، فقر واقعی قدرت آن‌ها نهفته است — و آغاز سقوط اجتناب‌ناپذیرشان...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/77293" target="_blank">📅 20:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند.
این حمله گسترده با فشار ترامپ لغو شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/funhiphop/77292" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ:
حاجی نمی‌خوام چیز کنما ولی انگار یه احساسی درونم داره می‌گه ایالات متحده و ایران به توافقی نزدیک می‌شوند که راه را برای مذاکرات بلندمدت هموار می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/funhiphop/77291" target="_blank">📅 19:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFpD6CobCfm2J07X3gnxby5djBw1ovudkk_zuKykQ8ZMkcskeFzj1NbSi0omuCicnQGex1rSAEYbBBQZn4CtA8EhFo2V0aPHfSEPWgaiOK9LgVB_tJXcrhRGJmsNlZtTq2gf4as_tFh93206C8TH6WclTOMi5BiI8hPu4bqthb4tI5lvDR_GTuGO67qs3Oq4baNwlMcGY7NYmUmfEbMw6ftkwudGqNpDeRS7Lpx9BNZdmxFipqrRx6_xT-Ybm5LzqwGi0h2EsUOASMkAvqsxHVr4lRGDCJHTUNWCCJIRJD6pNbfa10VJrOBFZYUTuuvP11TbWN5rlvmBIvy-eTT8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/funhiphop/77290" target="_blank">📅 18:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">انگلیس از شهروندان خودش خواست به اسرائیل سفر نکنن
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/funhiphop/77289" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foFpfmOdD8N2PzD0mDJzLDly85s8ccXM1sj3ZosYlYAo-CUpQlWBsOXuEpX2yG7M_5hpE5pyGniFxc99kdcqi-sST8cUx53XqbwIj41HJAnzO9h6u4MrMDuEdSx3JWvRGqrUgt67K1X55mliyn3zLj4FI_lKLgFYjN_MfK7Ajy3Pfqnf-5N-XX_571pzRtufOKVxVbc4tvinH31qqI6VlW1zglNPd1j2Ch_DXW3fbqJKRRoUROmCIYkbbiShRd4wNu0CNEszJwDzE6MjvWQs_ILDqe77YT0lC8creL-OWdJy4c_pNEXPtubzibQwdzGzdWmemRg9KUABlwvdnIl5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب لبنان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/77288" target="_blank">📅 17:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm_fHoc7a9tIBweNTKeupo-BTtBboWh1e9Qxf9e6zt3_smUs2rmiaZRTT00D7i6IuI6sX0acXWUu9IAV3UbUwZN0QAt1B4VaXgYTLRzdiS217nEFbdsqq8eR0cxhzxcxwWflG_E3qLJYwKPK2ufmagN57tiQdhTVYJx2Uv2Lhp5xRIizJQLVFCOHVUrZ79CchUVT0hGengm6fyvNHexkSUoZyCe709ttbxR_cEJYR__ZjcVpH1eyObI4GoEwtMP_q2998dlubEsanlkWHMw2QBd2uxmC8LFkU_AwcCGN6ggBr8SB9G1Ax_9KpixXB751hXibeGKr3zdgnLe5lPJ3qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7Uv0g7dHaMBafHFpGiKt2Of8C08KIFGczU8i3TaAM00LvbHcXoNApelFQYex3bJ7WZ7k5uUlAs6MP4QGUom7DgZSPyY5PGb5epcvKAowdg-027AaheKSO83ksHI1qLaFd_alhWx33nDVcpI27ISpCLg7dW5SO5Na4Kms_t2asGaBYitOvungETp4yyZYcwClf9IgeyFkLgQuoQAhp4k3EqDJBmEyaw6WX8axC5tvOH7N7P7RzrFpJNkH7JcnuBDO6F7HxdnbdrPnkoWM58pqfNb9JTemSErMiJArHcOwoTWRUYcN_t3OC-AGEiqU_ymYcSFv__GPkxn9D6UAo2BNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعمتی که از دیدنش 10 سال محروم بودیم
🫠
🥲
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/77286" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/77285" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🔹
ثبت نام آسان و سریع
✔️
🔹
نصب و راه اندازی تنها با چند کلیک
🖥
🔹
اپیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/funhiphop/77285" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/eGGaWnPeXVRNe6ntSCoTZylyXtdWYxVGm9kPSTMBFiFIuHL1CuNwxEgG3ED5NRGRP74peJY5Eavvy2R3jfz98Jmw96ABpe3rPyPQSj6joC52dQpXwwbxFGl4VsPPu-Fp6n_1rHwbBY4vrBEy_ce4HWCtIJ8CFlnijZvURiiMQg98Yf0dC7U75hzdC_uziQr4DQauCacCpdkoRL1VdQVcjd-6dyF-fy4Sdc4lL_Hc2iKpMOaE6WfMKkkAeSxY83kZufsJ4E9MBbhlguS6pFTHt3B7N4g0AwoB-XCv-8Rpl-nteQUZy6lqIiFmMNatF0w6xennC-qYHJTMt_l0ic01PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎊
با لنزبت، دنیای واقعی پیش‌بینی رو تجربه کن!
💳
شارژ فوری با کارت بانکی و درگاه امن VIP
💰
برداشت لحظه‌ای تا سقف 10,000 دلار
💯
بونوس
🔣
0️⃣
0️⃣
1️⃣
برای هر واریز
🎁
جوایز هفتگی مخصوص کاربران فعال
💵
پشتیبانی از تمام رمز‌ارزها برای شارژ و برداشت
🪩
امنیت جهانی و بیمه شرط برای حرفه‌ای‌ها
🔤
🔤
🔤
🔤
🔤
🔤
🔤
G18
🅰
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/funhiphop/77284" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXFMYmLmFoNl-Vq0rpImmPaO3xvA8YOIA9f_pua1yGUNj871fU5Qc8KH9nuKJli5C4soXtKo0f1R_wel7-0_-bGIvCQ9DNVz3pUFrJjPJQf0eVACx8X9ryevL-m5aiEoPNWtQQEs2mcLDP14_lKoDWoOSJHB0k_9onibWagn8AntXtX1xpYp3rl9BhhUk0MaX_xYNDWCRS03CwT61n5qF_yvzHLub2a_mex300Dz2vcoHJFvUU-x_L2YFCoDe-8zonP9sN6E0TrsWWsevGPkD7SWUgN9dxSCRwV-6_Nk6ZFvETfKLuFwUfagOB7zP5WWK-zn3tUidKf1dz5KvNDCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصدم این بود برخط باشم، دستم خورد رو زبان ترکی تازالیخدا بیردایمیش شدم
@FunHipHip
| Constantine</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/77283" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGvTOqmr60hZ9Jxm8fQnGAgtHCwoBWAReOFqxIi9gUoOmFCkL-DhZ9itJNi9HZ1n-0rxYpBOO9AHJqz52jsF-NxzDhKuCC3VkYcrMr4E1UePV6wLQHAU5iwLbZ3vKyD6Ls10wJ_oFNwimXi2Z0_0UzjnDY6JRQn0qUem8tsRVhSwwPUEJYwMX9-U-8kNn_r_yO1bpV-y5H1IL0-uzj1oGHPwwWOskE-j2quPtotcpzUPGdreMJdc1YuR1AtldkBzBCTkjLamYgfGRlhMxpe6tJriJnN5at1D2AfWLfsVcss0LdeYhikicNJ1LS4Vxj5NHaX8aue4e4X6dIM3X2VNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهلاک کمرم هزینه بردار بود
آب هدر می‌رفت چون بعدش باید دستمو میشستم و از مایع استفاده میکردم
هزینه ی عمل دیسک + ۱۵۰ میلیونه
و برا همین خم نشدم که بردارمش
فروپاشی اقتصاد ایران به روایت فان هیپ هاپ.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/funhiphop/77282" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بچه هایی که خارج از ایرانید شبا که گرمتون میشه پاهاتونو از پتو ندید بیرون چون ممکنه ی موجودی به نام سروش ولی زاده برای اینکه خنکتون کنه بیاد پاهاتونو بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/77281" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siRpoq_Ayn0YfgJVsNSuVyejhaKIYctBZbiBIgV_c_8G3VwMGh9DMsSU1vFJZMicT_gbOHes7y4mtTl4dCFMCXkphRjyiVuHqWNHQAZHnWXHz3FrE-FVUrv-EHsf6N4DRxR6Pll40eGvSJHffFK6dNyawJJId-fdZxxMFiZ5K1s56YyOmtDqc6bwmyql5HqbuDcQmGKYkJfpe59TUVeUPSmowuOg9C6WmPAWceqLiytUj9bd3YsQBXKVmz878P8Zke5wWM4hQtxqIH_vOzw6j1QN72OrSKQupa92a-fGdd5edM5_kiq6ozrsQ0yZaqoTkVP1WYp5mc2-CRLZlU4zCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان حاجی پاکستان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/funhiphop/77280" target="_blank">📅 16:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77279">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الان ملت چجوری به کانفیگ فروشا توضیح بدن مودی نیستن شرایط و تغییر میکنه فقط</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77279" target="_blank">📅 16:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrHmVtpI0n8mTUwVngTgXQPHNRqjNd0tzLixMagwkTlFglRSy9_FXwdOMO9JT7ZEhaWJsTPsxGuiV2EqBvK7vpsss5CMlMIc-tzaS9Njcavv98V_Ya5wwnv44DTrvh3NwyOOH2moEPAH5x-6ENcMtZ1z4F3xN4U_WhzmRB4QwJzUjudqifjbEtiQhv4IRj6bkDUp9sH-5We2ToaVekJZHjyjnnk81K2ieGcbUyBSxKnN1gm-Aj6vEG6Ztfo252RU_r1_z35hymG0S6YHEVlWCXFLArF4jr5rgnwfr6GcZOPWDPejJ3bm5i1Uk4rBwzpgekr70DpsolZtxZWL30g21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید کوروش به اسم
تهران 2585
ریلیز شد.
YouTube
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77278" target="_blank">📅 15:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77276">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اسرائیل
⬅️
لبنان
ایران
⬅️
اسرائیل
ایران
➡️
اسرائیل
ایران
⬅️
اسرائیل
فردا از اول بخون همینو
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77276" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77275">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwYqNnh35qSjHRdrNsR8en3-kQS-c3LoxUNFTAGkqHIJMcmQ7lMOhRrZGK8yB3CUlW8EnfNMjXZXOm_f8X1mklRYJkjzDHmQ0GjRowo2elKCsXFGryOpiF6FDcpGXUf12p090SjWLMHxvVKklOqnUicEGGvi-VDlpq8GFfeQeyTOIv6IDk5R1o46W3q7psL1EhfgYffxnXMKBFiXvJTLNW8Q45lVITszAKJfJFtVIx_wOJRafQE0KVMvzExpcu_lmlfM0zyWDCbqZtwCXDpIvM2o0lXoDUn3VNW6o_JN8Dalv2fidrAXKB5X8K1KIRYe-vs1Rnwf9wHvQKND44rtZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم الانبیا: از این به بعد درصورت هرگونه حمله اسرائیل به لبنان (حتی اگه به بیروت نزنه)، ما خودمون موشک می‌زنیم تو اسرائیل.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77275" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDKvyHosTQVeflPok2olFjFSE_gEcpncErferR2Nd7yKHNQbURy4rfMjfupJyewq2YsOS3kb1DwDXtkr5v-2JruSVpA-vnnMzI5XjIzCcGN07914ucx0NFPVArZIkYzen8oTCzfcqVpI5jqQp3FA5XaXadEkuKoIV5L5GXOO74xhZGhRlMRo6hXtk7NOmVC9MyLcu6u1DOphyWKJXJgegrwacVSEniPU4hYqNs7sY5Vi2hHi_uQq-gdWoBKWBgNOCWVXEXV5_M1DSNBFioMAnksydm6EQze0k5urCKv8oeb_LUtDgZ6a3DBdjjJrLs4wBfEtvc3guDopn1uZ0rd4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت پزشکیان:
اولویت ما امنیت ملی و آرامش مردم‌مان است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/funhiphop/77274" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77273">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77273" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77272">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسرائیل هیوم:
اسرائیل و ایالات متحده پیامی به ایران ارسال کرده‌اند که نشان می‌دهد اگر ایران از شلیک مجدد خودداری کند، حملات بیشتری صورت نخواهد گرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77272" target="_blank">📅 15:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77271">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77271" target="_blank">📅 15:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77269" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">من کسخل‌تر شدم یا پزشکیان واقعا داره چهره ی محبوب جمهوری اسلامی از دید عوام میشه؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77268" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">میگن پیت هگزت به مناسبت این جنگ نصف روزه ۵۰ تا شنا سوئدی رفته
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77267" target="_blank">📅 15:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77266" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:  نگران نباشید نتو قطع نمیکنیم  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77265" target="_blank">📅 14:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگران نباشید نتو قطع نمیکنیم
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77264" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnGIeUuRG4nueT1ql2u6y_xwNYhh71MPfcwGW1ESACHE_bisx-fndN1wFc1o6gG3fsPotO_Rl0SK2ViWdjKwlODrJRIw0VNJ1vSMu2QON-YMeFG_ZR1Mu8i-Fgcq29B7QZHzEJN9pAs9_ckzIqg_Vfsz_4UIw50COskiEiQ8HpSiX-JDO4CH0V0GWTpsrUoWdcgZSxsRHcLIzuWXIyl4steIXq933pOMnxQWW5rWoE0OGEBomLFbLrrGuOpk3buCeoc1X_lbLxodVVzQBIjJYKgWoMS8GAWcrgSVas-K4-2HIbJl4uFOXPn9z0h818IObPiAz3U18pQ66MQTgKmcTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:‌ هر دو طرف، اسرائیل و ایران، به دنبال آتش‌بس فوری هستند! مذاکرات نهایی درباره «صلح» در جریان است، مشروط بر اینکه نادانی یا حماقت مانع آن نشود. محاصره تا رسیدن به «توافق نهایی» برقرار و به طور کامل اجرا خواهد شد. امور باید به سرعت پیش برود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77263" target="_blank">📅 14:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">منتظرم جنگ امروز تموم شه بتونم بگم این جنگ عین کاگان بود، کوتاه و کصشر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77262" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0ztyVmpPM9-aW-r_wPXJ5OtPLLjK7wqGoiyLOwt-ov51Tb3a3MW77boSacEqev3wQfUB8YbNnx_KSbYf00zLJVYtpnP-TvPeYSC-3U9bMBRhfXmAHA-AbambVcKxeaW7bSHB6skvDB_OxAg2qwavO2FGCZoRRXHUdYTCR3wPIutd4XUgI6D3-Qme3NvErpbRpW1YqBDxLoblYogZTZMpyPN-Utde9_G4kPTgkIUVE5htT3LuSCiPl5rijfMZyFPQrCUTTsr6_W-SmTkFX-ZiF9r5FkbCe9m-xclcV9GVgAHBQMw4NzBa4H9fwXOKeVECMygqCnXOTbwJ_oX-08H1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرا امروز خداست
😂
شهربانو و الهه منصوریان چون الهه تو مسابقات انتخابی تیم ملی باخته حمله کردن به خانه ووشو و الهه منصوریان با چاقو میوه خوری خودزنی کرده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77260" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آموزش پرورش :
جنگ تموم نشه نهاییو مجازی میگیریم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77259" target="_blank">📅 13:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9BJOS5pPpdFhPAWf4N3tUCNOJYjf73W0ZdxUQd0XqCuWpvZaacHOIvAvM5QY1Q1dDe_9Of2rkmahT1Ll3b8bawI19UxSeH4_pREtDqwzD8Gfm2yubWlJXvkJW3L4CCQgUa0GINjuhuIN2YfeMWv2ZtnY8r_y1V1-EA0M-Pk7YzBnIB3NuLdHtv3S0vKFOatZ20Yt-yQ46nqWi3029YwGa-GXQNPk5YPxCZUB0ao9h0u7Lk0lNBhDD0bLx5TKC8TnU125SRVJoXDOj7j7LqqxLriYoBsOcrnAUcsIAvjDXD2_93f6IqE0eTHg_sfGTaU5XzoiGsF5DCiOllgwDnwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8d5Hqwlufsf5oEtM26lcla2MiwG4fSj1RZDly6tFrT3sQOtxgmKeTggC-8f9U7SlCXDF4IO4OIXuFO5el3pJsFgN32LdKdIsv7XREhFqyvRSeqFV7MychVJJ-XXYkM7_pLYAg8Vf3Q12rf4t64q6pnfvjzTYPKKROsh3F4frxZvI7TFWk8Cltwtw4ssgzAH-rN5wOrM1bTyScWFnWOJ9qhPydmBkdYWbdgWF4f_uYkNipAislClI_lRhibbVqLcTqwHVQcOT9bKFoR_HR2uTTHp-Z3agfdPVuXqZHt1kMw_u-DyYhdjRXnC6r_ZHVqPZWX3jc6g6pqE5LnLil6Plg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارن فضای جق زدن هم تو اپلیکیشن های ایرانی براتون میسازن دیگه چی میخوایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77257" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77254">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خاتم الانبیاء :
زدیم دهنشونو گاییدیم اگه باز بزنن میزنیم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77254" target="_blank">📅 13:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77253">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اگه میخواید بفهمید کی ترور شده کافیه ببینید تسنیم میخواد از طرف کی بیانیه منتشر کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77253" target="_blank">📅 13:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Gashtam Shab</div>
  <div class="tg-doc-extra">Alireza Roozegar</div>
</div>
<a href="https://t.me/funhiphop/77252" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آهنگ مناسبتی برا کانفیگ فروشا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77252" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اینکه نتارو قطع نکردن مشکوکه، میترسم بیان گوشیامونو بگیرن ایندفه
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77251" target="_blank">📅 13:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ :
ایران و اسرائیل باید هرچه سریعتر جلوی شلیک رو بگیرن
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77250" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=TIgu_G4BMqUGOHh7nIpZYu8PM55Fd278kxiEUjrfWf-jDyBYpf0oyuxaSBlmKHwTGxCF6VbepaKqEuolDbOjNpXSouuFmWsCzClL4tYqUuiBh3TL9WTGXt1INFrdBAVEwktH_qUCg7OFX4eHFADMR0-eahCizNTM28hmh1E-RrzhD5qNGHrr6EbTh_XgLYrAFn1KpiV1zSdji5Tp4Q6-60KemDpAXU9uF0JyzSgTDfeYyheNy9SvgPL6tCbhWShxfjSOzYTzI8TkUHS-_qAgko1HEUTqhehQXmzasXVs6-z8P2BPJNTHJQCiacPMa0OfaPXpfiwRL9FIUkO9eLfY2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=TIgu_G4BMqUGOHh7nIpZYu8PM55Fd278kxiEUjrfWf-jDyBYpf0oyuxaSBlmKHwTGxCF6VbepaKqEuolDbOjNpXSouuFmWsCzClL4tYqUuiBh3TL9WTGXt1INFrdBAVEwktH_qUCg7OFX4eHFADMR0-eahCizNTM28hmh1E-RrzhD5qNGHrr6EbTh_XgLYrAFn1KpiV1zSdji5Tp4Q6-60KemDpAXU9uF0JyzSgTDfeYyheNy9SvgPL6tCbhWShxfjSOzYTzI8TkUHS-_qAgko1HEUTqhehQXmzasXVs6-z8P2BPJNTHJQCiacPMa0OfaPXpfiwRL9FIUkO9eLfY2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دوربین مداربسته از حمله خواهران منصوریان به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77249" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ بیداره و واکنشی نشون نداده فعلا به ایران و اسرائیل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77248" target="_blank">📅 13:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بیایید برید از این کانال پروکسی انبار کنید که اوضاع خیته:
https://t.me/+IJWzPBxj-zJiY2E0</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77247" target="_blank">📅 12:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رسانه های اسرائیلی خبر از ترور سردار سپاه، احمد وحیدی میدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77246" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">رسانه i24 news:
ارتش اسرائیل تصمیم گرفته عملیات «غرش شیران» رو از همون جایی که متوقف شده بود ادامه بده، به‌جای اینکه عملیات جدیدی رو آغاز کنه. ارتش این رو روز ۴۲ عملیات «غرش شیران» محسوب می‌کنه، اونم بعد از یه وقفه بیش از دوماهه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77245" target="_blank">📅 12:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77242">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3dNjTr32OMmDXloi4D-cxAyI9A7oBAoIJgGn2F6uEoOESgXQuN_NAy2X3D03yGQ-Vng8SMcrkm8tYbLgZOeut089TFii-DICLZsTQQLCwEzqeiz6cTyiZf8_jtKyix-rDxCn34YnqRAPj0xCxPUF1BLOVCkgZ6p4iJOrjxxPXEugxxNkLoEPAL7KARrDxLBtS5Isbuoty8Bq3wKYEdxowzUpfvfuUd2qjzfctugaARwpyQCFK37KZhBq1Xj_zUlLyyaYzc_IhLFnP5IXEWs5ARif58EIydqYMN1RR2Mu8AFUSoTalM-gkuVq8ZS3ITY-JJJMn80_6qdGvx6QFnKnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rtI80DVcGVX2XHQJREzv3lT5t4o_ekekvI_Ck-VAoT8RZ0tbvWYH0X2yqk9u5jRU1JSYaZiw4H1_c7jy0sLvudEKS2E39F0r2z07-RJ_h5INm_4tUKEHrf0QEKq7AMhEeCxfdlqVBcdDuupZT0_g7t1fC_bUXbAiYQGbCUMha1ql2Sox9x9Eg3lDA876YjMXCR3Vcj6tqQuPoM9BHcGuMlVfcenu3ioMC_7T9vH5zZ5myyN3cQ4q6Ohns-VgRJ3uzW42-NxBBORKSPL_oIVciTKmCMeyXtsZP45Ybm0OMkD9XOxv1qscJjc_VYQDZtxB7MKc0LLIp0_rDxOWdZ5z5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQVFxhqAJPWcK26-wAp9YRFP67d4oYWAiSWivu1GCYqk0GINvcmQWTvsYtiWebl6r9zeDsg3hAbabDtTd65AHJlxcTdw0248xlw6zJCMgcRJXVMcAfZ4EnBw6QeYu7lTL5F55GQHWMb5G36ABfQAGgI9YGBxD1Y8yPMEERuIbIz1hC4AY3wBm2s07eN-nhCJqqhvEItgQOLqyPbbR3D42ReYjbqP9euCHHZcM1spFJfYk8150KVDzh4Xra2g7m3v0_8ZxrR0aNlCTmPZZSbEEtwICMcPk-Ufdk4RoAxpvF-f2YPtfEtfW8o5wbRpxfNTlsiK4EAooYwomO_DgNJ3oQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط که اسرائیل داشت ایرانو میزدن، خواهران منصوریان فرصت رو غنیمت شمردن و اتک زدن به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77242" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77241">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل برای حداقل چند روز درگیری با ایران و احتمال یک کمپین طولانی‌مدت آماده می‌شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77241" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77240">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سازمان ملل:
we are nigga run
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77240" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پارکینگ های زیر سطحی به عنوان پناهگاه برای شهروندان تهرانی در صورت تشدید تنش ها در دسترس قرار خواهد گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77239" target="_blank">📅 12:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77238">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صابرین‌نیوز: خبر ترور و شهادت فرماندهان سپاه کذبه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77238" target="_blank">📅 12:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77237">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سفارت هند در تهران خواستار ترک فوری شهروندان هندی از ایران شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77237" target="_blank">📅 12:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77235">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بنیامین نتانیاهو با کابینش جلسه امنیتی گذاشته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77235" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77234">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پتروشیمی کارون خوزستان دوباره مورد حمله قرار گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77234" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77233">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تیپ 10 "سیدالشهدا" سپاه پاسداران در کرج، هدف حملات ارتش اسرائیل قرار گرفت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77233" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ کونی رئیس جمهور هم مگه انقد میخوابه، پاشو دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77232" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دانشگاه هوافضای عاشورا رو هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77230" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سگ زرد چجوری الان آتش بسه؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77229" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لشکر 8 زرهی اصفهانو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77226" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تسنیم میگه تست پدافنده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77225" target="_blank">📅 11:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فرید جان سلام ما کرجیم صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77219" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=cDNFe5re1hsM9dCX5a54pFF-_LHKgOTNVCBbb9Xc1203SaF7c2zqOYxscAIoF0cIKFv_h8qW3jrZIwKSWjuMbK53Ck2TY2YB64w6GhBaXo7alBl8tYStR01iAtx4TqudHT44O2csx_dn2XZOfln8GHNx1Yeq0y0eLsfM0KgFhyybjqge5yrx0j7y0iLVeGFV2EiFrjuSQe8F1VPWClaH2jRc51CZWrbQwdaK0N5aFq9rmCHc7ygzzD1IJtLEU8qare6uC6dp2t6UW5b3cHOQf0-VZ8KH1Z41L7ZI9pParmecbqjELUkRluCJsY1KEkm6FsvvuDB9EHLeMs554YBpIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=cDNFe5re1hsM9dCX5a54pFF-_LHKgOTNVCBbb9Xc1203SaF7c2zqOYxscAIoF0cIKFv_h8qW3jrZIwKSWjuMbK53Ck2TY2YB64w6GhBaXo7alBl8tYStR01iAtx4TqudHT44O2csx_dn2XZOfln8GHNx1Yeq0y0eLsfM0KgFhyybjqge5yrx0j7y0iLVeGFV2EiFrjuSQe8F1VPWClaH2jRc51CZWrbQwdaK0N5aFq9rmCHc7ygzzD1IJtLEU8qare6uC6dp2t6UW5b3cHOQf0-VZ8KH1Z41L7ZI9pParmecbqjELUkRluCJsY1KEkm6FsvvuDB9EHLeMs554YBpIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی بیدار میشه میبینه نتانیاهو دیشب گفته بود نه بابا کاری ندارم هرچی تو بگی ارباب ولی همین که خوابیده شروع کرده به زدن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77218" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صدای انفجار در غرب تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77216" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d92631652.mp4?token=MkU8JylsH8-Thc4C97ElrM9IAT6jRfQGHRNkDPasqjGulEyLCihX6AwEgXrhylP-OH34fcVh0uBigsnAqEg8Nuo3IRcW6Dbw4jB04xP6NPMehV24rQD8zW4WGAvtKsAlBuQIyzycyEYyG1ne8Om0kWlzk7jkWDgZ9S2UjuxD9CuoCA5ozqzlzyJ7YC9E0hbjLcL9BX0L3UMy4UWwbcHB6SeHCyTn3jmv8GjdfxZIoKLncYpU9XZYGGPztw8lq1d0NTWGiPivcP_XQgPM3lBrJcmIOmR86r21fGbWqCKZMApxwM0rrOnk2XA9H6_ynvOwd4jRlT7eKmcil-420ZyzsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d92631652.mp4?token=MkU8JylsH8-Thc4C97ElrM9IAT6jRfQGHRNkDPasqjGulEyLCihX6AwEgXrhylP-OH34fcVh0uBigsnAqEg8Nuo3IRcW6Dbw4jB04xP6NPMehV24rQD8zW4WGAvtKsAlBuQIyzycyEYyG1ne8Om0kWlzk7jkWDgZ9S2UjuxD9CuoCA5ozqzlzyJ7YC9E0hbjLcL9BX0L3UMy4UWwbcHB6SeHCyTn3jmv8GjdfxZIoKLncYpU9XZYGGPztw8lq1d0NTWGiPivcP_XQgPM3lBrJcmIOmR86r21fGbWqCKZMApxwM0rrOnk2XA9H6_ynvOwd4jRlT7eKmcil-420ZyzsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77215" target="_blank">📅 11:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به حمله به یک پتروشیمی در ایران، چندی پیش به یک پتروشیمی مشابه در اسرائیل حمله کردیم.
اخطار می کنیم؛ دشمن صهیونیستی با اقدام علیه اهداف غیر نظامی و هدف قرار دادن صنایع نفتی، بازی خطرناکی را شروع کرد، که دامنه آن کلیه اهداف انرژی منطقه را در بر خواهد گرفت و عواقب آن برای اقتصاد جهانی، بر عهده آتش افروز اصلی این میدان، آمریکا می باشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77211" target="_blank">📅 11:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نیروی موساد و آمان انقد بدبخته که با یه نت بستن شما نتونه به اسرائیل اطلاعات ارسال کنه اخه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77210" target="_blank">📅 11:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrRNexR66SJ0sXVOA09hu0j66sGk2MgQCZW7YbOmiu14T0WSMjopluGuKGwhEpRGkjASNfKewwjNZryNmZaKWwy4ed6mCcCDKxSTT0zInh08q4XwnJJioergDkScw0v-iJnTsGKxPd17iB2Zdy259wWTeGHKPlz-IgxCp52QatJPhIxQJS94879x3iDcGY-jmYqUq6VOb4D-KzyYOAhj0glB0easv8zqzn-q4AqE7lZWt242HBu4878VEDd60k1j6Ls9u_DnnHqkqWlZnL1qsEzPxXhtBctpcVbsVJaKk_sxZDyArJNz5MlyxiUNMvXhn8bc5oAjUy5y7_MlIEsC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا نمی‌فهمم منظورش چیه ولی از اونجایی که چند ماه پیش به یه بنده خدایی گفته بود زهی خیال باطل احساس می‌کنم خیلی حالیشه و در آینده خواهیم دید چه خواهد شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77209" target="_blank">📅 10:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سخنگوی وزارت خارجه:
آتش بس نقض نشده ولی اگر اتفاق دیگه ای بیافته که بشه، ما آمریکا رو مقصر میدونیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77207" target="_blank">📅 10:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">۴۸ ساعت پیش ترامپ: در آن قسمت دنیا آتش بس یعنی کمتر بهم ضربه بزنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77205" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObbS3HrXQTP12rVQ6DoiDndA5epqbFwWTQbbevnxLd_2Aq9GJIx2oPhCvdlOXXyyt5zmQtOUPD-7dDxbjN1jQohI085DJBtPW9tk10uJVrKcASYFDIhFMwUtD7ulsaJOtNLsTHVOs8JjmUXGz1CFiAmHo43xZULvZLEhG8EshNSMOqhi4x0ZZiYG6plWnBuXEg9RRlgMusWp7_uZquOxEsoulKHbcVdGmCwtD8wyMxWVQlU4-4Bi2f1w1xiLrmLjhqF_AJUL0ULKf_JTBmCWlPR6or9NLs_OaEYgoZDzi-XJYMEX6FhV6Kh52w7MJ6lZqPe7RJ4ZHms020868hxV_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا:
پدر عشق است لطفا جنگ نکنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77204" target="_blank">📅 10:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77202">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تا اینجای کار کشتی فرنگی بود، هروقت آزاد شد آتش بس نقض میشه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77202" target="_blank">📅 10:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77201">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نگفته بودن آتش بس زنگ تفریح هم داره</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77201" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77200">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZAO0qUZMLmM2WGIjR11GVBhAhVZKNIaXaJaO2yoNt1tqZAIzO4daJGdTgPXH8vPsPpeaW_GAiBcgWGK51dEFMTIHdjobDzRW0tnYXyhFxU7yFNj1tb-uj7dXXYxiV7I6OYCPGuBrvy-SY5zRR_4ZFkXticwW3vcLOx0SjOcV2J5jODuCw-o6K5Zdn07hN0tE46Cf3-8f77S4KgnZCxjriulzb5q1hfz2MRG4kUGke-53Fmx4kCHTLFzO4UwNz34QVGYOdEmegGuKiQdfpbZAg8xX69BfS7edFRIszSc2HviT6sy2BYHLDUdqwssTzcuWBKpqG6RHtkQ1599YhbqpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
خو اومد زد، آتش بس رو ادامه بدیم بازم میزنه خب یکی بگه ما چیکار کنیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77200" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77199">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اوه اوه جالب شد، انصرالله یمن اعلام کرد تنگه باب المندب بصورت کامل به روی اسرائیل بسته شد.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77199" target="_blank">📅 09:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77198">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0472fc5f3c.mp4?token=hmoMnqGrcKxyPD6Q3IWD1H7BNkeFrCLG4LTkoO87hDWG_cmT7yjKUamirZcwjfcdJgbeNP3Jdh7FNOLqV-wmQQE7j8xK4L7kD0-tBcaWrBs-xm7ubktCZcD_A91N_OFCCEHWI8L4cIrs3je_kg9X87cHpP8vS0ysmn37natDhgHQCds3G2dKXsMdYL6T5D2jpDBqIwKVk14KZKkqlT-mk7M5WH5o4AEbZu0kOyELfZNYq0mpx2ElULVnJEYMYeGBMtXuJQOx7k7g3u-A-WcrqfQbgZyoUtATyAqN3Do_Z6MztWQ1A9JkDSHFrkn5eW4No-e7TIBZfN5HMTO6cxj6lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0472fc5f3c.mp4?token=hmoMnqGrcKxyPD6Q3IWD1H7BNkeFrCLG4LTkoO87hDWG_cmT7yjKUamirZcwjfcdJgbeNP3Jdh7FNOLqV-wmQQE7j8xK4L7kD0-tBcaWrBs-xm7ubktCZcD_A91N_OFCCEHWI8L4cIrs3je_kg9X87cHpP8vS0ysmn37natDhgHQCds3G2dKXsMdYL6T5D2jpDBqIwKVk14KZKkqlT-mk7M5WH5o4AEbZu0kOyELfZNYq0mpx2ElULVnJEYMYeGBMtXuJQOx7k7g3u-A-WcrqfQbgZyoUtATyAqN3Do_Z6MztWQ1A9JkDSHFrkn5eW4No-e7TIBZfN5HMTO6cxj6lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به عاصم منیر وقتی میفهمه دارن همو میزنن :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77198" target="_blank">📅 09:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77197">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شما رو نمیدونم ولی من یکی خبرای جنگ و این که کی کیو زد بکیرمه</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77197" target="_blank">📅 09:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77196">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ug2azl_wWanL80lymPT_hG7x52Ejyfxq-llW7P8Yo5DEzKrYGDWBMemWHbEbKDpsjqXhrgC5MrFP-2I2vb4DK-7D3BD0zORsxhkDrMefNJ7rdCD14Bee3iU7CYc2Go_uEngFWX0KUhKq528hXRBvcIvKsulg3CE5t4llqXwwevLr01WbzH_E0YLeALeAvqHOGeBuLKnGA_2qinj7oWimr77VauI-35FMrsTJRFyYre7YNL6Rlfz1iqF2Mk4Ef0GUbViY83bNz8m2bbf70sz_Ev340-eEVWNTqxUDPrP21l-Rtlwm1f4xuyHJgVGbR8Lt4hLj6t11mzjjFBHl41khpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید جان گرم کن بازی تازه داره هارد میشه
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77196" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77195">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2iipe15QW98bmfYAAJz4Fm6R386NcfLZnCcuuJci2hgUjT5RCy_Je5ls6TtYTm3Dr7S_6UeSMYZk3aT-XZ3cQDQIPF4I2-co-owKiMGPqK0HzKxhabn5oSbqOjJRoFmyd78D9NmxV9VSCElC8g01HXQp5m1BBe3p_pfsPAeJRI8Hb97a8clAFmwQ70MkmvCfr5qsI5vh5izKbGyXdpt6S9xgljSluCy87jEdodFGVr-O90piIOwOtXDWfwLlsCw9gFrSh4ZSnmdpylkYHO64sfczjJi42LfV2B7JuyDUf__0SzQewAMqh6d4E5iq1bBCByQ0MwidE-jayOPT6bbEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
فرانسه - ایرلند شمالی
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
دوشنبه ساعت ۲۲:۴۰
🏟
ورزشگاه پیر مائوروی
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
فرانسه در
۱۰
دیدار اخیر خود،
هشت
برد و
یک
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
ایرلند شمالی در
۱۰
دیدار اخیر خود،
پنچ
برد و
یک
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر فرانسه
۳.۲
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر ایرلند شمالی
۱
.
۹
گل در هر بازی بوده است.
🧠
شرط ممکن است ناموفق شود اما مدیریت بودجه‌تان هرگز نباید شکست بخورد.
👍
ورود به سایت با فیلترشکن
R18
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77195" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77194">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اسرائیل هیوم: حملات صبح امروز اسرائیل به ایران با هماهنگی آمریکا انجام شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77194" target="_blank">📅 08:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77192">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تایید نشده  گزارش‌ها از حمله اسرائیل و انفجار تو مجتمع پتروشیمی کارون خوزستان.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77192" target="_blank">📅 08:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77191">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تایید نشده
گزارش‌ها از حمله اسرائیل و انفجار تو مجتمع پتروشیمی کارون خوزستان.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77191" target="_blank">📅 07:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77190">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">موشک ها به سمت تل آویو شلیک شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77190" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77189">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ایران داره جواب حمله هارو میده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77189" target="_blank">📅 07:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77188">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سید مجید نقطه زن سریع دیس بکو ارسال بکن
منابع عبری: انتظار می‌ره ایران بزودی حمله موشکی کنه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77188" target="_blank">📅 05:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77187">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوستان بخوابید خبری نیست</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77187" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77186">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ارتش دفاعی اسرائیل: نیروی هوایی، با هدایت اطلاعات نظامی، مدتی پیش اهداف نظامی ایران را در غرب و مرکز ایران مورد حمله قرار داد. جزئیات تکمیلی متعاقباً اعلام خواهد شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77186" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77184">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کانال ۱۲ اسرائیل: جنگنده‌های اسرائیلی درحال حمله به اهدافی تو ایرانن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77184" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77183">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تایید شد
اسرائیل به ایران حمله تلافی‌جویانه کرد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77183" target="_blank">📅 04:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77182">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">گزارش اومده فرودگاه مهراباد رو زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77182" target="_blank">📅 04:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77181">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اصفهان
تبریز
تهران
رو زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77181" target="_blank">📅 04:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77180">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">جدی جدی زدن</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77180" target="_blank">📅 04:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77178">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ در ادامه گفت اگر مذاکرات با ایران شکست بخورد احتمالا یک حمله‌ی کماندویی با سربازان آمریکا در خاک ایران انجام خواهد داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77178" target="_blank">📅 01:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77177">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این بزرگوار در ادامه: نتانیاهو چاره‌ای جز قبول توافق من با ایران نخواهد داشت، من تصمیم‌گیرنده‌ام، من همه تصمیم‌ها را می‌گیرم، بیبی این‌طور نیست.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77177" target="_blank">📅 01:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77176">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یه مادر خوش تکنیک رندوم: حملات ایران هدف من در تکمیل مذاکرات آمریکا و ایران را تغییر نداد.   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77176" target="_blank">📅 01:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77175">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یه مادر خوش تکنیک رندوم:
حملات ایران هدف من در تکمیل مذاکرات آمریکا و ایران را تغییر نداد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77175" target="_blank">📅 01:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77174">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آقا به به امام زمان آنلاین شد  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77174" target="_blank">📅 01:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77172">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تماس تلفنی ترامپ و نتانیاهو(صدا کم):
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/77172" target="_blank">📅 01:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77171">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کانال ۱۱ اسرائیل:
ایران از طریق واسطه‌ها پیامی به اسرائیل فرستاده است که تهران حملات خود به اسرائیل را به پایان رسانده و حملات بیشتری انجام نخواهد داد مگر اینکه اسرائیل تلافی کند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77171" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77170">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یدیعوت آحارونوت:
بر اساس گزارش‌های دریافتی، در گفتگویی که کمی پیش به پایان رسید، نتانیاهو به ترامپ اطلاع داد که
قصد حمله‌ای گسترده به ایران
را دارد.
رئیس‌جمهور آمریکا روشن کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77170" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77168">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فووووووری اسراییل لیست ترور جدید پخش کرد
😐
😐
😐
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77168" target="_blank">📅 00:59 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
