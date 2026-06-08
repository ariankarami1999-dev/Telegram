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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 18:24:47</div>
<hr>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFpD6CobCfm2J07X3gnxby5djBw1ovudkk_zuKykQ8ZMkcskeFzj1NbSi0omuCicnQGex1rSAEYbBBQZn4CtA8EhFo2V0aPHfSEPWgaiOK9LgVB_tJXcrhRGJmsNlZtTq2gf4as_tFh93206C8TH6WclTOMi5BiI8hPu4bqthb4tI5lvDR_GTuGO67qs3Oq4baNwlMcGY7NYmUmfEbMw6ftkwudGqNpDeRS7Lpx9BNZdmxFipqrRx6_xT-Ybm5LzqwGi0h2EsUOASMkAvqsxHVr4lRGDCJHTUNWCCJIRJD6pNbfa10VJrOBFZYUTuuvP11TbWN5rlvmBIvy-eTT8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/funhiphop/77290" target="_blank">📅 18:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انگلیس از شهروندان خودش خواست به اسرائیل سفر نکنن
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/funhiphop/77289" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foFpfmOdD8N2PzD0mDJzLDly85s8ccXM1sj3ZosYlYAo-CUpQlWBsOXuEpX2yG7M_5hpE5pyGniFxc99kdcqi-sST8cUx53XqbwIj41HJAnzO9h6u4MrMDuEdSx3JWvRGqrUgt67K1X55mliyn3zLj4FI_lKLgFYjN_MfK7Ajy3Pfqnf-5N-XX_571pzRtufOKVxVbc4tvinH31qqI6VlW1zglNPd1j2Ch_DXW3fbqJKRRoUROmCIYkbbiShRd4wNu0CNEszJwDzE6MjvWQs_ILDqe77YT0lC8creL-OWdJy4c_pNEXPtubzibQwdzGzdWmemRg9KUABlwvdnIl5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنوب لبنان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/funhiphop/77288" target="_blank">📅 17:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hm_fHoc7a9tIBweNTKeupo-BTtBboWh1e9Qxf9e6zt3_smUs2rmiaZRTT00D7i6IuI6sX0acXWUu9IAV3UbUwZN0QAt1B4VaXgYTLRzdiS217nEFbdsqq8eR0cxhzxcxwWflG_E3qLJYwKPK2ufmagN57tiQdhTVYJx2Uv2Lhp5xRIizJQLVFCOHVUrZ79CchUVT0hGengm6fyvNHexkSUoZyCe709ttbxR_cEJYR__ZjcVpH1eyObI4GoEwtMP_q2998dlubEsanlkWHMw2QBd2uxmC8LFkU_AwcCGN6ggBr8SB9G1Ax_9KpixXB751hXibeGKr3zdgnLe5lPJ3qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v7Uv0g7dHaMBafHFpGiKt2Of8C08KIFGczU8i3TaAM00LvbHcXoNApelFQYex3bJ7WZ7k5uUlAs6MP4QGUom7DgZSPyY5PGb5epcvKAowdg-027AaheKSO83ksHI1qLaFd_alhWx33nDVcpI27ISpCLg7dW5SO5Na4Kms_t2asGaBYitOvungETp4yyZYcwClf9IgeyFkLgQuoQAhp4k3EqDJBmEyaw6WX8axC5tvOH7N7P7RzrFpJNkH7JcnuBDO6F7HxdnbdrPnkoWM58pqfNb9JTemSErMiJArHcOwoTWRUYcN_t3OC-AGEiqU_ymYcSFv__GPkxn9D6UAo2BNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعمتی که از دیدنش 10 سال محروم بودیم
🫠
🥲
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/77286" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/funhiphop/77285" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/funhiphop/77284" target="_blank">📅 17:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXFMYmLmFoNl-Vq0rpImmPaO3xvA8YOIA9f_pua1yGUNj871fU5Qc8KH9nuKJli5C4soXtKo0f1R_wel7-0_-bGIvCQ9DNVz3pUFrJjPJQf0eVACx8X9ryevL-m5aiEoPNWtQQEs2mcLDP14_lKoDWoOSJHB0k_9onibWagn8AntXtX1xpYp3rl9BhhUk0MaX_xYNDWCRS03CwT61n5qF_yvzHLub2a_mex300Dz2vcoHJFvUU-x_L2YFCoDe-8zonP9sN6E0TrsWWsevGPkD7SWUgN9dxSCRwV-6_Nk6ZFvETfKLuFwUfagOB7zP5WWK-zn3tUidKf1dz5KvNDCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قصدم این بود برخط باشم، دستم خورد رو زبان ترکی تازالیخدا بیردایمیش شدم
@FunHipHip
| Constantine</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/77283" target="_blank">📅 16:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tGvTOqmr60hZ9Jxm8fQnGAgtHCwoBWAReOFqxIi9gUoOmFCkL-DhZ9itJNi9HZ1n-0rxYpBOO9AHJqz52jsF-NxzDhKuCC3VkYcrMr4E1UePV6wLQHAU5iwLbZ3vKyD6Ls10wJ_oFNwimXi2Z0_0UzjnDY6JRQn0qUem8tsRVhSwwPUEJYwMX9-U-8kNn_r_yO1bpV-y5H1IL0-uzj1oGHPwwWOskE-j2quPtotcpzUPGdreMJdc1YuR1AtldkBzBCTkjLamYgfGRlhMxpe6tJriJnN5at1D2AfWLfsVcss0LdeYhikicNJ1LS4Vxj5NHaX8aue4e4X6dIM3X2VNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهلاک کمرم هزینه بردار بود
آب هدر می‌رفت چون بعدش باید دستمو میشستم و از مایع استفاده میکردم
هزینه ی عمل دیسک + ۱۵۰ میلیونه
و برا همین خم نشدم که بردارمش
فروپاشی اقتصاد ایران به روایت فان هیپ هاپ.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/funhiphop/77282" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بچه هایی که خارج از ایرانید شبا که گرمتون میشه پاهاتونو از پتو ندید بیرون چون ممکنه ی موجودی به نام سروش ولی زاده برای اینکه خنکتون کنه بیاد پاهاتونو بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/funhiphop/77281" target="_blank">📅 16:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siRpoq_Ayn0YfgJVsNSuVyejhaKIYctBZbiBIgV_c_8G3VwMGh9DMsSU1vFJZMicT_gbOHes7y4mtTl4dCFMCXkphRjyiVuHqWNHQAZHnWXHz3FrE-FVUrv-EHsf6N4DRxR6Pll40eGvSJHffFK6dNyawJJId-fdZxxMFiZ5K1s56YyOmtDqc6bwmyql5HqbuDcQmGKYkJfpe59TUVeUPSmowuOg9C6WmPAWceqLiytUj9bd3YsQBXKVmz878P8Zke5wWM4hQtxqIH_vOzw6j1QN72OrSKQupa92a-fGdd5edM5_kiq6ozrsQ0yZaqoTkVP1WYp5mc2-CRLZlU4zCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاکستان حاجی پاکستان
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/funhiphop/77280" target="_blank">📅 16:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77279">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الان ملت چجوری به کانفیگ فروشا توضیح بدن مودی نیستن شرایط و تغییر میکنه فقط</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/funhiphop/77279" target="_blank">📅 16:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrHmVtpI0n8mTUwVngTgXQPHNRqjNd0tzLixMagwkTlFglRSy9_FXwdOMO9JT7ZEhaWJsTPsxGuiV2EqBvK7vpsss5CMlMIc-tzaS9Njcavv98V_Ya5wwnv44DTrvh3NwyOOH2moEPAH5x-6ENcMtZ1z4F3xN4U_WhzmRB4QwJzUjudqifjbEtiQhv4IRj6bkDUp9sH-5We2ToaVekJZHjyjnnk81K2ieGcbUyBSxKnN1gm-Aj6vEG6Ztfo252RU_r1_z35hymG0S6YHEVlWCXFLArF4jr5rgnwfr6GcZOPWDPejJ3bm5i1Uk4rBwzpgekr70DpsolZtxZWL30g21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید کوروش به اسم
تهران 2585
ریلیز شد.
YouTube
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/funhiphop/77278" target="_blank">📅 15:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77276">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/funhiphop/77276" target="_blank">📅 15:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77275">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwYqNnh35qSjHRdrNsR8en3-kQS-c3LoxUNFTAGkqHIJMcmQ7lMOhRrZGK8yB3CUlW8EnfNMjXZXOm_f8X1mklRYJkjzDHmQ0GjRowo2elKCsXFGryOpiF6FDcpGXUf12p090SjWLMHxvVKklOqnUicEGGvi-VDlpq8GFfeQeyTOIv6IDk5R1o46W3q7psL1EhfgYffxnXMKBFiXvJTLNW8Q45lVITszAKJfJFtVIx_wOJRafQE0KVMvzExpcu_lmlfM0zyWDCbqZtwCXDpIvM2o0lXoDUn3VNW6o_JN8Dalv2fidrAXKB5X8K1KIRYe-vs1Rnwf9wHvQKND44rtZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه خاتم الانبیا: از این به بعد درصورت هرگونه حمله اسرائیل به لبنان (حتی اگه به بیروت نزنه)، ما خودمون موشک می‌زنیم تو اسرائیل.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/77275" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDKvyHosTQVeflPok2olFjFSE_gEcpncErferR2Nd7yKHNQbURy4rfMjfupJyewq2YsOS3kb1DwDXtkr5v-2JruSVpA-vnnMzI5XjIzCcGN07914ucx0NFPVArZIkYzen8oTCzfcqVpI5jqQp3FA5XaXadEkuKoIV5L5GXOO74xhZGhRlMRo6hXtk7NOmVC9MyLcu6u1DOphyWKJXJgegrwacVSEniPU4hYqNs7sY5Vi2hHi_uQq-gdWoBKWBgNOCWVXEXV5_M1DSNBFioMAnksydm6EQze0k5urCKv8oeb_LUtDgZ6a3DBdjjJrLs4wBfEtvc3guDopn1uZ0rd4iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت پزشکیان:
اولویت ما امنیت ملی و آرامش مردم‌مان است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/funhiphop/77274" target="_blank">📅 15:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77273">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/funhiphop/77273" target="_blank">📅 15:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77272">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسرائیل هیوم:
اسرائیل و ایالات متحده پیامی به ایران ارسال کرده‌اند که نشان می‌دهد اگر ایران از شلیک مجدد خودداری کند، حملات بیشتری صورت نخواهد گرفت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/77272" target="_blank">📅 15:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77271">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/77271" target="_blank">📅 15:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ولی واقعا جواب دندون شکنی به یهودیا دادیم، بخصوص اون بخشش که مقر پلانکتون تو بیکنی باتم و خونه خانواده سندی تو جنگل رو زدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77269" target="_blank">📅 15:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">من کسخل‌تر شدم یا پزشکیان واقعا داره چهره ی محبوب جمهوری اسلامی از دید عوام میشه؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77268" target="_blank">📅 15:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">میگن پیت هگزت به مناسبت این جنگ نصف روزه ۵۰ تا شنا سوئدی رفته
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77267" target="_blank">📅 15:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">قرارگاه خاتم‌الانبیا: فعلا عملیات متوقف میشه اما به جان مادرم اسرائیل دوباره بلند پروازی کنه یدونه موشک میزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77266" target="_blank">📅 14:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:  نگران نباشید نتو قطع نمیکنیم  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77265" target="_blank">📅 14:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">معاونت ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
نگران نباشید نتو قطع نمیکنیم
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77264" target="_blank">📅 14:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxi-thRIRWLkIIK3wosEQCZCH3wDdWkUcQCo2FJBRJT1-tzgdCo_J10QmwGqJu7o7rlG6ftUEfRDPDmERRok0QJrmnuPQWr-c4UjVCICuF6CE9AyThjM7ouNKFPLxcqWC-xXq_CkMYcubqgPKWHZYMcK4vR-MKCa32B-8hRPo7AiFonPT6y4wst8ls42VC6cm_dyoPiLB7VG0oGNIyz7JpPClin26dUCl-IYmfkjTcBFtoN4Av55wfVqUgb_hdS_WWlgQR_ttDJivYN0IB5kpROHzqoO1_5qfHLGUKJ2TixWq0AFHdOigN4FpJ0lUE4AQKtwxsr5PI-L_v9Ksa4mqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:‌ هر دو طرف، اسرائیل و ایران، به دنبال آتش‌بس فوری هستند! مذاکرات نهایی درباره «صلح» در جریان است، مشروط بر اینکه نادانی یا حماقت مانع آن نشود. محاصره تا رسیدن به «توافق نهایی» برقرار و به طور کامل اجرا خواهد شد. امور باید به سرعت پیش برود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77263" target="_blank">📅 14:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">منتظرم جنگ امروز تموم شه بتونم بگم این جنگ عین کاگان بود، کوتاه و کصشر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77262" target="_blank">📅 14:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0ztyVmpPM9-aW-r_wPXJ5OtPLLjK7wqGoiyLOwt-ov51Tb3a3MW77boSacEqev3wQfUB8YbNnx_KSbYf00zLJVYtpnP-TvPeYSC-3U9bMBRhfXmAHA-AbambVcKxeaW7bSHB6skvDB_OxAg2qwavO2FGCZoRRXHUdYTCR3wPIutd4XUgI6D3-Qme3NvErpbRpW1YqBDxLoblYogZTZMpyPN-Utde9_G4kPTgkIUVE5htT3LuSCiPl5rijfMZyFPQrCUTTsr6_W-SmTkFX-ZiF9r5FkbCe9m-xclcV9GVgAHBQMw4NzBa4H9fwXOKeVECMygqCnXOTbwJ_oX-08H1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرا امروز خداست
😂
شهربانو و الهه منصوریان چون الهه تو مسابقات انتخابی تیم ملی باخته حمله کردن به خانه ووشو و الهه منصوریان با چاقو میوه خوری خودزنی کرده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77260" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آموزش پرورش :
جنگ تموم نشه نهاییو مجازی میگیریم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77259" target="_blank">📅 13:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwhdej8JtgyAcllaS55PYoYHITLVChvOuM7MRkU_YWpvjCacRDHhVWVzTA22LBGyZG1x0FJ0c7q-2vmVqQ_paMCjaQXUuu1IDNfkPFaLBUgdyglrz00_DcVx-ZloQydScA7ugta-F9W6K-BYm00lc8vd5CqhXnprK467RqdEj90PEoFGDYWhZtKTA0qColvy5LCPIjY9cyjtk9IfKoXCKgRKX2dGuYdd9D7qmSMh3IYJ0MOK8Jai0tDwOFyzQVgdC_9EnQL2XfAOsGIOBhhPw13jjgAwp11zPDnImwJIowcrFaQnLvvZkNcNe_j_nawq36SXFKl-Ac0zdDF5HhzRQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8d5Hqwlufsf5oEtM26lcla2MiwG4fSj1RZDly6tFrT3sQOtxgmKeTggC-8f9U7SlCXDF4IO4OIXuFO5el3pJsFgN32LdKdIsv7XREhFqyvRSeqFV7MychVJJ-XXYkM7_pLYAg8Vf3Q12rf4t64q6pnfvjzTYPKKROsh3F4frxZvI7TFWk8Cltwtw4ssgzAH-rN5wOrM1bTyScWFnWOJ9qhPydmBkdYWbdgWF4f_uYkNipAislClI_lRhibbVqLcTqwHVQcOT9bKFoR_HR2uTTHp-Z3agfdPVuXqZHt1kMw_u-DyYhdjRXnC6r_ZHVqPZWX3jc6g6pqE5LnLil6Plg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارن فضای جق زدن هم تو اپلیکیشن های ایرانی براتون میسازن دیگه چی میخوایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77257" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77254">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خاتم الانبیاء :
زدیم دهنشونو گاییدیم اگه باز بزنن میزنیم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77254" target="_blank">📅 13:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77253">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اگه میخواید بفهمید کی ترور شده کافیه ببینید تسنیم میخواد از طرف کی بیانیه منتشر کنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77253" target="_blank">📅 13:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77252" target="_blank">📅 13:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اینکه نتارو قطع نکردن مشکوکه، میترسم بیان گوشیامونو بگیرن ایندفه
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77251" target="_blank">📅 13:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ :
ایران و اسرائیل باید هرچه سریعتر جلوی شلیک رو بگیرن
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77250" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=RN6xElz4vgLpIeHxLI9eUkAx2n-1J7qZZmp1qWb5sALCSWWDVEPU7GN2aTBvcy5TvsGE92atVcEtuet3gcqx8KgrMbshMx-UrMuh5mgLEbs3FudbcUnCXTYj4WSwGW6gFn_goqIYDAymw4FVQZGQMZ_1KTYg7_Er8oy3B20qhX6ynDt5dysvenHtPrjsn5KkTEUZFRP6d-OWSUk0wWFQZ_MS8AntekowyI1h7NFnDsof-f16mFPMGO9fEJAdF5T3K2rrHxJa9yzcNUmt9KuqR0eoP1SK8ZP8_cc2rKCkVyxJF7vksQ6zkxdw6gVjfftaZ7wX0bHXkD2msO5uGN8PHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e98d055a5.mp4?token=RN6xElz4vgLpIeHxLI9eUkAx2n-1J7qZZmp1qWb5sALCSWWDVEPU7GN2aTBvcy5TvsGE92atVcEtuet3gcqx8KgrMbshMx-UrMuh5mgLEbs3FudbcUnCXTYj4WSwGW6gFn_goqIYDAymw4FVQZGQMZ_1KTYg7_Er8oy3B20qhX6ynDt5dysvenHtPrjsn5KkTEUZFRP6d-OWSUk0wWFQZ_MS8AntekowyI1h7NFnDsof-f16mFPMGO9fEJAdF5T3K2rrHxJa9yzcNUmt9KuqR0eoP1SK8ZP8_cc2rKCkVyxJF7vksQ6zkxdw6gVjfftaZ7wX0bHXkD2msO5uGN8PHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو دوربین مداربسته از حمله خواهران منصوریان به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77249" target="_blank">📅 13:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ بیداره و واکنشی نشون نداده فعلا به ایران و اسرائیل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77248" target="_blank">📅 13:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بیایید برید از این کانال پروکسی انبار کنید که اوضاع خیته:
https://t.me/+IJWzPBxj-zJiY2E0</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77247" target="_blank">📅 12:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رسانه های اسرائیلی خبر از ترور سردار سپاه، احمد وحیدی میدن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77246" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">رسانه i24 news:
ارتش اسرائیل تصمیم گرفته عملیات «غرش شیران» رو از همون جایی که متوقف شده بود ادامه بده، به‌جای اینکه عملیات جدیدی رو آغاز کنه. ارتش این رو روز ۴۲ عملیات «غرش شیران» محسوب می‌کنه، اونم بعد از یه وقفه بیش از دوماهه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77245" target="_blank">📅 12:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz5qgr3DqGV9oTJCmpgY1v8EO1Q5-N0Vj7ViyVgITLUbM5UnpXkl7rNZXv3WuAqI7ufHlyC5VESCFedJi-dcG3pUsz6P-xXt7ExYRoXs2Z5t6dO6vAOX99WKDO6vRg8FHv0N1phnHnm4dXOD5f1FhC5HXY5tPX-S08IDcLtz8rUm0VpUlQ7EJL0JMdl1Jha1gCB_PAoJp36mdxilLpbFKVNxbgcq0SoZ4448Bgursf0Akw1z68oQx_n-aE9GWoAa4K0uVX4CLLgK4gle8HNM8ObZZXUmgxaoDn5nFGCKkKc1hNRmiAwXoxJkxrRMVKBWWjb6lEybcqPwbNpUKMVUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTSahkJLET6A3B4urWKIJNxBMmM9H3ibINiwGuQinUrTr4CoL5Rv67_KD3uSZO_0Byv4Kddt_uvUZQpDBoP0dHk-X8QS7-qb4LcrZr1QVdtb6uFdk8ytpW0-FPEKsmZoCzVSJAuhjA2X0l1pBLFlLV_YnnHaQkercdmRFZ6fyuPlgTA_KLO8OYMLf6Zxnsl9jsoNdYh_hF4fPKRlZ0XTg_KGd07BHTEOMtJEXFu2sbQhUc-oEGdHjd29raHCPUBXjd7Kf8Ja6hX2__WGWEqHfjtyBk4YIFA5h9HQ9PAPcH9bcR2LefrdN_djlilrPwWR-2uBs3TFW5ba85IcBCzkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1JD-MjR4qAd66dASk43QuyUtrlHnTZoGYOnCmKFuBVxVbxk8idMaS6dyYyFqkhw5iSZKhgtec7jJR0frt43tmWfOZL33t17joU4CENKVpw6jmaSxEUcmvt6xrPZJ8Bfc3N7gahCHLTwyXzAkbkyiJH-hXIR_4SUyulMqLnm_M4_TT8Ou8bjZQewJuqGNORrMhx5lvNeX-ADU6Vr6roBx7DxIGjVhT3yTxEkeY2q0ER0flSkjX66AnQkPJvOWePa_0JEmBbgOsaCUSS7COiZv9AUqK7QsUV9kDw7SdxZ5T2cV8nvNAFtSDXbtBwuVwNAhPH0MPsLKbvMcyVAX617XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این وسط که اسرائیل داشت ایرانو میزدن، خواهران منصوریان فرصت رو غنیمت شمردن و اتک زدن به دفتر ووشو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77242" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رادیو ارتش اسرائیل:
ارتش اسرائیل برای حداقل چند روز درگیری با ایران و احتمال یک کمپین طولانی‌مدت آماده می‌شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77241" target="_blank">📅 12:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77240">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سازمان ملل:
we are nigga run
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77240" target="_blank">📅 12:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پارکینگ های زیر سطحی به عنوان پناهگاه برای شهروندان تهرانی در صورت تشدید تنش ها در دسترس قرار خواهد گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77239" target="_blank">📅 12:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77238">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صابرین‌نیوز: خبر ترور و شهادت فرماندهان سپاه کذبه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77238" target="_blank">📅 12:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77237">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سفارت هند در تهران خواستار ترک فوری شهروندان هندی از ایران شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77237" target="_blank">📅 12:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77235">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بنیامین نتانیاهو با کابینش جلسه امنیتی گذاشته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77235" target="_blank">📅 12:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77234">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پتروشیمی کارون خوزستان دوباره مورد حمله قرار گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77234" target="_blank">📅 12:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77233">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تیپ 10 "سیدالشهدا" سپاه پاسداران در کرج، هدف حملات ارتش اسرائیل قرار گرفت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77233" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ کونی رئیس جمهور هم مگه انقد میخوابه، پاشو دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77232" target="_blank">📅 12:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دانشگاه هوافضای عاشورا رو هم زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77230" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سگ زرد چجوری الان آتش بسه؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77229" target="_blank">📅 11:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">لشکر 8 زرهی اصفهانو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77226" target="_blank">📅 11:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تسنیم میگه تست پدافنده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77225" target="_blank">📅 11:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77219">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فرید جان سلام ما کرجیم صدای انفجار اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77219" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77218">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=OdDR9STF_cmeWMIKmRQ8eDeUVAI3UrInI6-TS6tbcEgVg_I1Xm-h5QAlhiNI-5Mo371WFHYvVRwevdq-plciKdaLh7sLPLk-c9taftAps86ODgBK7Ccjc_2ns653CFX0XTzDcEDrg31U1-_3dG7uEIstK98rMi9KrKVMZMMPBAG23yGXN4LCYp8BWloQhF_uAoR4W-HCRawu5mnrGex4OtWUdHJPoguUW8PucCavfbuNoMHloydoJAwk8ywxQ1fxVs4CEhS7s3VSyiLLbNGCRNP67R4OuSXYC1SjTFt-q_ou4cN5o4ATJQHvLH-ltelUL6XHXxMQlqET6bI0x2k8BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e1f36b08d.mp4?token=OdDR9STF_cmeWMIKmRQ8eDeUVAI3UrInI6-TS6tbcEgVg_I1Xm-h5QAlhiNI-5Mo371WFHYvVRwevdq-plciKdaLh7sLPLk-c9taftAps86ODgBK7Ccjc_2ns653CFX0XTzDcEDrg31U1-_3dG7uEIstK98rMi9KrKVMZMMPBAG23yGXN4LCYp8BWloQhF_uAoR4W-HCRawu5mnrGex4OtWUdHJPoguUW8PucCavfbuNoMHloydoJAwk8ywxQ1fxVs4CEhS7s3VSyiLLbNGCRNP67R4OuSXYC1SjTFt-q_ou4cN5o4ATJQHvLH-ltelUL6XHXxMQlqET6bI0x2k8BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی بیدار میشه میبینه نتانیاهو دیشب گفته بود نه بابا کاری ندارم هرچی تو بگی ارباب ولی همین که خوابیده شروع کرده به زدن:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77218" target="_blank">📅 11:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77216">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صدای انفجار در غرب تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77216" target="_blank">📅 11:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77215">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d92631652.mp4?token=pmdAeQI9hjZbaXB2rEWvzFgYH6dRuPUwH3LUKOf5t6LHue7ifnYXqZkTG-8JTGhuTlStSbOV1JNXaoK92lArPdGwHMUxOG4G1q4Ehefbv_mFcA8udYHijPH_nnbLCdL5ZFiLyX1ja6yZH_nxbew2SPb-hDRG20aXL1iMaXMFOATnEFZnnaL691dK7KQCvSmpw6Wnc9fd_EohRd-FiFZ2PrmHIssOl6U3xESnfXjQ9mz4lbCJOnINxLvBEDSEMzUOvkaWyWjIVfHGuKvzMi6-sZajTzykCKl7onf1YeMhVjafseIYXVGQ7XnTq6iGHxgoDWR93LGOIMhvIIU7SfyTsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d92631652.mp4?token=pmdAeQI9hjZbaXB2rEWvzFgYH6dRuPUwH3LUKOf5t6LHue7ifnYXqZkTG-8JTGhuTlStSbOV1JNXaoK92lArPdGwHMUxOG4G1q4Ehefbv_mFcA8udYHijPH_nnbLCdL5ZFiLyX1ja6yZH_nxbew2SPb-hDRG20aXL1iMaXMFOATnEFZnnaL691dK7KQCvSmpw6Wnc9fd_EohRd-FiFZ2PrmHIssOl6U3xESnfXjQ9mz4lbCJOnINxLvBEDSEMzUOvkaWyWjIVfHGuKvzMi6-sZajTzykCKl7onf1YeMhVjafseIYXVGQ7XnTq6iGHxgoDWR93LGOIMhvIIU7SfyTsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77215" target="_blank">📅 11:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77211">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اطلاعیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
در پاسخ به حمله به یک پتروشیمی در ایران، چندی پیش به یک پتروشیمی مشابه در اسرائیل حمله کردیم.
اخطار می کنیم؛ دشمن صهیونیستی با اقدام علیه اهداف غیر نظامی و هدف قرار دادن صنایع نفتی، بازی خطرناکی را شروع کرد، که دامنه آن کلیه اهداف انرژی منطقه را در بر خواهد گرفت و عواقب آن برای اقتصاد جهانی، بر عهده آتش افروز اصلی این میدان، آمریکا می باشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77211" target="_blank">📅 11:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77210">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیروی موساد و آمان انقد بدبخته که با یه نت بستن شما نتونه به اسرائیل اطلاعات ارسال کنه اخه؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77210" target="_blank">📅 11:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77209">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqNOx1HsialzIE1yqUgHA_p7_2nVvB_7iGGkNEVmkyEvfNSrLg-b2QAYUU54IjxBGOgY3nIp--KDm5sYNL-sAn2lQNAvZcqh7O8WGEyr652xV2Sy2mwYu7tV3j_VzdqjPSKj0G--2PbjlnAI0I_Dw13kkkCK2w9Ao5kGghk-5DjQ3qsjiIB45lNRxELk9Zi7SNDc1phyjegMDk8_c1GNuDVXahzajUfAg37TretKxQmy-Zrnc-PS-jrszcDP6E9O8XQv9Gaaxz7ZQlfDTYxMdJ_d11zMv2MSjOHARdr4hmKnUASfeCPNeZ3rM5vIB5FWI0EpJzb1g_HNQd_AfNInbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا نمی‌فهمم منظورش چیه ولی از اونجایی که چند ماه پیش به یه بنده خدایی گفته بود زهی خیال باطل احساس می‌کنم خیلی حالیشه و در آینده خواهیم دید چه خواهد شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77209" target="_blank">📅 10:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77207">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سخنگوی وزارت خارجه:
آتش بس نقض نشده ولی اگر اتفاق دیگه ای بیافته که بشه، ما آمریکا رو مقصر میدونیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77207" target="_blank">📅 10:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77205">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">۴۸ ساعت پیش ترامپ: در آن قسمت دنیا آتش بس یعنی کمتر بهم ضربه بزنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77205" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77204">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Erg2JtD-LKPufR6ABNqXMQztcOv3nnwHFTpYmfjXic5jPerZK0tLZhJsqGAZWTIK_Ip1hff5bt-wkIPmH8trhxa0wmGaTw1BKQF93PRIebDqW4GiX71V88WTc415hUPv5Itjn6tEqs68EBFkOKKoEpooqFwMN1f5Bg_BUYc_yGuFFewfmiiZe0xcBK2l8AyuG0k5IfNGutmBMdGkgd7BRFfUkkzsLtvLUEu5DV9fMKSpX04q7fiiKlJBN7vWM_3ZAEK944hPSvqVXgoq0rBxp3oEHvNt76zVfav6LuOm2W1YDbVk21BQQxduVHUu-Yh7uxECtA0dmn7rUyIDbkRgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا:
پدر عشق است لطفا جنگ نکنید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77204" target="_blank">📅 10:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77202">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تا اینجای کار کشتی فرنگی بود، هروقت آزاد شد آتش بس نقض میشه</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77202" target="_blank">📅 10:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77201">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نگفته بودن آتش بس زنگ تفریح هم داره</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77201" target="_blank">📅 10:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77200">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMCInw41ynHsfz13gl3nPdlFV4ONWq-uGdgt-AcHcUK8wF3FbY7i_Iv_trb0847j1o6w-IAfydgPcR7_RcZNXbrrbIuwTAD-vFKLYvMeJo6erebWLpLIahi39Zsm7wAaUsMpQLhkFt8FE_GK8lr7mHczutwFqSgOqUvYQPZwq9BmJ0LEnEfauT4A06eM1ugUvoZhTxssFYlEYuVWjLp-faWHkeOCZv3wACbPNDYg0w4yw7P3S5viUN3HDv7EQ6rfy3u7uhJpxPq9Go8JiJfmdkbB5nu4g1xMEfPqKh0pCcu6x8bWTWbDwMRPVmeyn4RxKthG6ByjvEq1xP6-riBBtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
خو اومد زد، آتش بس رو ادامه بدیم بازم میزنه خب یکی بگه ما چیکار کنیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77200" target="_blank">📅 10:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77199">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اوه اوه جالب شد، انصرالله یمن اعلام کرد تنگه باب المندب بصورت کامل به روی اسرائیل بسته شد.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77199" target="_blank">📅 09:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77198">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0472fc5f3c.mp4?token=ayLnXQFofTOFjdMgy5I6GvsREYn6xbEJ2E73FTFkDSdKtGFhfrX5E1dSV62Th4qXZ4Lq0IHgIJQxUKW96WCK6_MbXPQa3m33rL41z5dy6qiqobt895XlrZqnHg-JtLOdg39GddcQCmHUkhFrWyt7p-LYtg7Oat2iGesuVjGW5G9m7g1LfZ22NUaJ6NfXLFjn0wMAgJZyK-QqG9aYEhWUftGdVWAv7pE5gLmsfb76lqKRrkKXObg7vRfxgGvbXq4o_dTSE3kEVdKyAuqagXHvrG7TPJiXYFy2a_wxZ-vq_hGAin0IhNIsUwxr4M32GAR8vSwymC1RViYuEzEsTHL1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0472fc5f3c.mp4?token=ayLnXQFofTOFjdMgy5I6GvsREYn6xbEJ2E73FTFkDSdKtGFhfrX5E1dSV62Th4qXZ4Lq0IHgIJQxUKW96WCK6_MbXPQa3m33rL41z5dy6qiqobt895XlrZqnHg-JtLOdg39GddcQCmHUkhFrWyt7p-LYtg7Oat2iGesuVjGW5G9m7g1LfZ22NUaJ6NfXLFjn0wMAgJZyK-QqG9aYEhWUftGdVWAv7pE5gLmsfb76lqKRrkKXObg7vRfxgGvbXq4o_dTSE3kEVdKyAuqagXHvrG7TPJiXYFy2a_wxZ-vq_hGAin0IhNIsUwxr4M32GAR8vSwymC1RViYuEzEsTHL1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به عاصم منیر وقتی میفهمه دارن همو میزنن :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77198" target="_blank">📅 09:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77197">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شما رو نمیدونم ولی من یکی خبرای جنگ و این که کی کیو زد بکیرمه</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77197" target="_blank">📅 09:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77196">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oe8xwdXdLZWj1F03mFuB7QXrNkIlqZnVqzUtK8B1VCbEo_wPh81i-TTwOrn14xENHdWDvtMKlv9iLL8mKZ6s4aQ0yO80hQxvdcandjQNr_jxo6t6EjoQdPyBuisCyGIpYJNE6FGk2__dmQKvZRLzDLSFmdKKan9ZsJbH39lZfRcGhK5TMg3ZBWS-WJoW42gEAwckj1Vjb0Z_yRb8S3oVXfutjKuKMwGq_x-hS7t0x2wgEzrKG2w4av3tn0659P_-1kMlvvW3CRldqrZY9NP1GMLET6T6oNJY6VVNx7iDLQ9TtmgTIjS1fFKoYfq3eIUqKMiM1pkIJP3JuHKvtk54RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید جان گرم کن بازی تازه داره هارد میشه
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77196" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77195">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ng-8cN7_EqXrMOKUj5EPDsGR8e7rqRHC8EHYaqwrWDz6iNF3hsc0vvr1lM7k0p913Qx2SDgVsOdQHEim10b1MmajxQchqDzZS5vDg-BX3ITRLJZS_uiHIhLe4OKuGSSlVd73ZFSv_-O3i5VdXPRHPnbsyBwu9SS71utV99-xEWBSpTvT47FMtkYyUTCBKnSzDeJOZ5gZ4p-sNR_LgJK5tLn-YGYkOxVsOj2rx2TxcHAuU56A90XfQRgLsQf7yoMYOOwGEoL7mxCxGsd9Vwvxl8_XPC5MkujjRMPtmKYWlBevCUBSnZmuGgk-52MV5R5uE3B6A7_qhMHZ3QSjvsHZQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77195" target="_blank">📅 09:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77194">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اسرائیل هیوم: حملات صبح امروز اسرائیل به ایران با هماهنگی آمریکا انجام شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77194" target="_blank">📅 08:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77192">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تایید نشده  گزارش‌ها از حمله اسرائیل و انفجار تو مجتمع پتروشیمی کارون خوزستان.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77192" target="_blank">📅 08:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77191">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تایید نشده
گزارش‌ها از حمله اسرائیل و انفجار تو مجتمع پتروشیمی کارون خوزستان.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77191" target="_blank">📅 07:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77190">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">موشک ها به سمت تل آویو شلیک شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77190" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77189">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ایران داره جواب حمله هارو میده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77189" target="_blank">📅 07:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77188">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سید مجید نقطه زن سریع دیس بکو ارسال بکن
منابع عبری: انتظار می‌ره ایران بزودی حمله موشکی کنه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77188" target="_blank">📅 05:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77187">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دوستان بخوابید خبری نیست</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77187" target="_blank">📅 05:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77186">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ارتش دفاعی اسرائیل: نیروی هوایی، با هدایت اطلاعات نظامی، مدتی پیش اهداف نظامی ایران را در غرب و مرکز ایران مورد حمله قرار داد. جزئیات تکمیلی متعاقباً اعلام خواهد شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77186" target="_blank">📅 05:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77184">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانال ۱۲ اسرائیل: جنگنده‌های اسرائیلی درحال حمله به اهدافی تو ایرانن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77184" target="_blank">📅 04:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77183">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تایید شد
اسرائیل به ایران حمله تلافی‌جویانه کرد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77183" target="_blank">📅 04:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77182">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش اومده فرودگاه مهراباد رو زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/77182" target="_blank">📅 04:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77181">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اصفهان
تبریز
تهران
رو زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77181" target="_blank">📅 04:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77180">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جدی جدی زدن</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/77180" target="_blank">📅 04:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77178">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ در ادامه گفت اگر مذاکرات با ایران شکست بخورد احتمالا یک حمله‌ی کماندویی با سربازان آمریکا در خاک ایران انجام خواهد داد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77178" target="_blank">📅 01:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77177">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این بزرگوار در ادامه: نتانیاهو چاره‌ای جز قبول توافق من با ایران نخواهد داشت، من تصمیم‌گیرنده‌ام، من همه تصمیم‌ها را می‌گیرم، بیبی این‌طور نیست.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77177" target="_blank">📅 01:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77176">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یه مادر خوش تکنیک رندوم: حملات ایران هدف من در تکمیل مذاکرات آمریکا و ایران را تغییر نداد.   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77176" target="_blank">📅 01:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77175">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه مادر خوش تکنیک رندوم:
حملات ایران هدف من در تکمیل مذاکرات آمریکا و ایران را تغییر نداد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77175" target="_blank">📅 01:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77174">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آقا به به امام زمان آنلاین شد  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77174" target="_blank">📅 01:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77172">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تماس تلفنی ترامپ و نتانیاهو(صدا کم):
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/77172" target="_blank">📅 01:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77171">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کانال ۱۱ اسرائیل:
ایران از طریق واسطه‌ها پیامی به اسرائیل فرستاده است که تهران حملات خود به اسرائیل را به پایان رسانده و حملات بیشتری انجام نخواهد داد مگر اینکه اسرائیل تلافی کند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77171" target="_blank">📅 01:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77170">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یدیعوت آحارونوت:
بر اساس گزارش‌های دریافتی، در گفتگویی که کمی پیش به پایان رسید، نتانیاهو به ترامپ اطلاع داد که
قصد حمله‌ای گسترده به ایران
را دارد.
رئیس‌جمهور آمریکا روشن کرد که اگر چنین حمله‌ای انجام شود، آمریکایی‌ها در آن شرکت نخواهند کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77170" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77168">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فووووووری اسراییل لیست ترور جدید پخش کرد
😐
😐
😐
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77168" target="_blank">📅 00:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77167">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پروازهای فرودگاه امام تا اطلاع ثانوی لغو شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77167" target="_blank">📅 00:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77166">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سفارت آمریکا در اورشلیم از همه شهروندان آمریکایی می‌خواهد به دنبال نزدیک ترین پناهگاه برای خطرات احتمالی باشند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77166" target="_blank">📅 00:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77165">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبرنگار وای نت:
ایالات متحده پیامی به اسرائیل فرستاد که بهتر است چند روز صبر کند تا ببیند آیا می‌توان با ایران به توافق رسید یا نه.
و اگر نه، ما طبق برنامه به اقدام مشترک بمباران گسترده همراه با غافلگیری را از سر خواهیم گرفت و ارزش ندارد این موضوع را با درگیر شدن در تبادل محدود ضربات هدر داد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77165" target="_blank">📅 00:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77164">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سفارت آمریکا در اورشلیم اسرائیل از همه شهروندان آمریکایی اسرائیل خواسته است که نزدیک پناهگاه بمانند یا در پناهگاه پناه بگیرند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77164" target="_blank">📅 00:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77163">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">چند دقیقه پیش تماس تلفنی حرامز و نتانیاهو آغاز شد.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77163" target="_blank">📅 00:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77162">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اسرائیل لبنانو زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77162" target="_blank">📅 00:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77161">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۴ اسرائیل: امشب فقط موشک‌ها و جت‌ها نیستند که بین آسمان و زمین در نوسان هستند، بلکه سرنوشت سیاسی نتانیاهو نیز همین گونه است.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77161" target="_blank">📅 00:22 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
