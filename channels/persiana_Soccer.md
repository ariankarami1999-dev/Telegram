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
<img src="https://cdn4.telesco.pe/file/Z78h1wQn5tDrchqtg4Yz0Bkx-wMdPgIuOTETZtTWt11oMJ0Kufl9pM7lg3uGAxuswBPeWK6vFvVNZmQQQ9V7DM2omv_27kdRwiraMHI2scF1WFLxZjakyrdxiboz5fDOlexAF7dDp_m7R0vAaIw3y_fQAJk_Hpw9SWH1p40huxq6HMBtrBmYCisBZ-II7FCBpdMnacDA3AKnt55Nubbw4QLC3FkI33fiP9raoVOVZszdC2pV1nPcYKW9DJKZERnyGG5tWyl5g-_6tdOxsD7uXfjLIf0QrDIEQWlmZEevWAQx-56cVjgymZRJELk_A3tQUJiB_NUHCHhkx_HFxUfocA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 22:46:24</div>
<hr>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6DTFwFxhPVKJcBUAwxMA4AGbeBKlAidEVL8oe9O4GuS_jvd8wdwPOawdaDuNzN8yUOtPWq-GSPwMfJUiq--VMc19-puYC2zUEvW3wYCQeDMKIL0cwOEufnGuD46Y03cmkDW23xc7oTWdQeUw6mI7hLJ3Ols1ItFsWBw86yBsAqmi8m-MaDm4-vXP4D2JeydwkaVteteyR-2RoDktiuW0sCPjUOOaW1YxAPSS6Hes2VnAiqB3Uw1KZDMAf2z994FgP4YeL_bJEtby5RJzh_cUx4n_SxrkUZicqnxOeH4zm6N9rxn3IlRExt3HzlKZlwtrucGbXBi1Sif04ECDkobWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJnJDdJilWJwlkMVptV-D7qlSn_MKvHahZq7gB-LrM39rp2Aij_KuiidcznC3CwfzgdaaYXWjNuQL-rUDo7jC4Zli8Z_Logvk5d0PMq7Ou4TKVksJd9A-IrKNhk5yA5ySHw-gOzWPxV7dcQZnfsp2JjhzELql5xccCQ07V1rB1ZhfwDqe3Ouqmy-xTZtrfrr-0Ss-3t6BihQXCZX1rdd60mf-sCzSEpQmfAYC23wjV8kj1-2EJZaYvv-2GKqHyxzbZOPWmkIGe0tnapuU8045lj-6pMhBWTvlHlBf9MsVkmYZKlPY3k5496tQ4BHEYQd07nzWjN-RAy8J0mKacOQew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLGhTnG8L6nsMjydodK3gbmeuJePR-EgAifHmMnhOzze0hdf4VuIUMYcjCige5aWh66PaZG0J-rjAHQZ_3GAz8OPtGlnplBRV3Gsv1Trcmet9efyjK12dPF211DJFuoS9KBUiU0xLE0Qt8v3r4e5EVkdAVkFBJ0dBbJahUwUIV2XBnlN_2O6_QnMF3MEp1G4pV8WlqAdBhToTow8jXfoSfNxXNLKkRIU-SS-K9Bb5juA6xxciH3tWREFXiLvL8ozK4wYPDJd0GqEgM26dsnr1ySvxBsg_cdQMxqv0HIl-bRCI3z5GazgYjmFvjGqQp2nSoBliTYpAOSi8JYUO7J9xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=nVasLUnDnQA_BLFq0hcsG0uHnk70Y1KPsBPrIVwn_Wudpl01R3dSmOyC6JJp1GnMnA9xeRCVLU3zBuFJ2GZUcMmuWrnnmPKjfVatdv39bApIZ3ECYmD1fFA2VzrR8UoavSu6yZs5aFbq2q83dWUoKSiaDk4phJ2-mckPjI95Lq6ta73z0ESnAdziH4s6IpeLeCir3_W-I6i1qLuBcmD2N7b3SwZR_xbEe7-VUqirizbohiUNMAsKiVPbuMsl9CNLbh_tdTe0_GekC8Zt7ZPJttsYRWyqFZa8ttMdE8hLaZ2Dm-fv_FfGo2dD29JxGCDW5CH-zVFW2dU1IGI3BzP8Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d23ff97317.mp4?token=nVasLUnDnQA_BLFq0hcsG0uHnk70Y1KPsBPrIVwn_Wudpl01R3dSmOyC6JJp1GnMnA9xeRCVLU3zBuFJ2GZUcMmuWrnnmPKjfVatdv39bApIZ3ECYmD1fFA2VzrR8UoavSu6yZs5aFbq2q83dWUoKSiaDk4phJ2-mckPjI95Lq6ta73z0ESnAdziH4s6IpeLeCir3_W-I6i1qLuBcmD2N7b3SwZR_xbEe7-VUqirizbohiUNMAsKiVPbuMsl9CNLbh_tdTe0_GekC8Zt7ZPJttsYRWyqFZa8ttMdE8hLaZ2Dm-fv_FfGo2dD29JxGCDW5CH-zVFW2dU1IGI3BzP8Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران: کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRwe0_0WHGgZ_9VFWSd6lXfvUcd1832r9XrARtKonx22h7NfMX_8bjLUF8Qj8Q1lASNu_4SJlFx-4Ql48khCBO0Gglbpg4YfeqYOeaQin5TD-wm2bhJDzVS_oOW11roOUEmRTGtr6M4fj-7zBJHGM3xE7Zs6CtovTHPIsSStjVjDcwNajNMPw6a4SUMxlUXpRJEzPxpu4pkrkCBU7d06iIQxA3SBa4Q5gV8Z13hl-3be8dXhwucz2u4g5jaTcqNXIoBrwKmsWn0vpK9oeYTJpUnHmL2gSi08P0Y4qZYlj2RrNNb50M1zjv-oRsmBAM_qkiD9po9mvFgGcfY_sRjLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25238">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=Od3OLf0ZTl9ivqinJbXOQfUnc-CpCtBAr1lCXmSYytETjVDb9lyv_dK8Qj6Gl8oW4wzAw5VGJ6ADKq4KsIN_wpgFZJiA2ZBw7zyJjpTjcQBGqbMbguX65CZdKM5a9aHa55DfVIku7Ixx7Zcjd-S6d6Grc1wBcW7ycOi76Mrl6pgD5syrrYeeoNdR-EiM5KfgciVPg6osRcmqJ9Km1pz_pWQfuIDy94-Pb_dMyPyq0cq4yPHL8E9kTsoXx6ycPX1U8_1rDlXpxInH5CiLudRf6mr6oM5nlb5fnmU2AeuDsnycv6ICGuyqJIqXuxMR44USI6cx4koaEePXKuWuL6djMgqwhkrq7UxScuAZrvA98ACPGLOdh-cuqa5Rpad_gA76xNNLZuPKzwhJsDlv1F8TC0VpjcvaCI9FMeu608XZy8U1gPBi7m-3uebgW7a-kfVc3_7-D8zVIVCqF-2nw615mn_c1W8Ovsalgo4ocBMY7AIuSl6uDoHedSoByiCNolAiQJu-cnZRtJ_S-oINj_-sUZQ_vQnH9unlTRXxTu75e4EOq63d1yj3Itrb-bvA6x80sJOjcZ1KIWCUQSSjOTJuLpAuKbDzSUT0WsHRVmrWKqjBYkrEXB5_LRrwzVoLab4L5CyyoVRVmlpWngpQ139acqL7uJMwuZw3XM0kzPcwcAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb7b4dbfc.mp4?token=Od3OLf0ZTl9ivqinJbXOQfUnc-CpCtBAr1lCXmSYytETjVDb9lyv_dK8Qj6Gl8oW4wzAw5VGJ6ADKq4KsIN_wpgFZJiA2ZBw7zyJjpTjcQBGqbMbguX65CZdKM5a9aHa55DfVIku7Ixx7Zcjd-S6d6Grc1wBcW7ycOi76Mrl6pgD5syrrYeeoNdR-EiM5KfgciVPg6osRcmqJ9Km1pz_pWQfuIDy94-Pb_dMyPyq0cq4yPHL8E9kTsoXx6ycPX1U8_1rDlXpxInH5CiLudRf6mr6oM5nlb5fnmU2AeuDsnycv6ICGuyqJIqXuxMR44USI6cx4koaEePXKuWuL6djMgqwhkrq7UxScuAZrvA98ACPGLOdh-cuqa5Rpad_gA76xNNLZuPKzwhJsDlv1F8TC0VpjcvaCI9FMeu608XZy8U1gPBi7m-3uebgW7a-kfVc3_7-D8zVIVCqF-2nw615mn_c1W8Ovsalgo4ocBMY7AIuSl6uDoHedSoByiCNolAiQJu-cnZRtJ_S-oINj_-sUZQ_vQnH9unlTRXxTu75e4EOq63d1yj3Itrb-bvA6x80sJOjcZ1KIWCUQSSjOTJuLpAuKbDzSUT0WsHRVmrWKqjBYkrEXB5_LRrwzVoLab4L5CyyoVRVmlpWngpQ139acqL7uJMwuZw3XM0kzPcwcAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۲۰۰ میلیون تومان درآمد در ماه از معرفی دوستان خود امکان پذیره ؟
بله.
شما ميتونيد براساس مراحل آموزش داده شده در ویدیو از معرفی دوستان خود کسب درآمد کنید.
عجله كنيد، ممكنه دوستت زودتر از تو دوست مشتركتون رو دعوت كنه
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/25238" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA8VH97SsP3pym9eLRs7DHzizsaNynU1UE12mWJJYMQZrN2WeMdvs0helplCVML1K7a-DJ-ZBu8OK4kIeKSB5SVYk1k3Yv6D-G2wktNd8BZFk72QSwB_7v05SqIOGOgB_zkc_ojsB3-IquDeFdQqoovJdseYJ3vCOUeXqMD8NkHybMnzVfPz_bragu1cSJ6i24_Mn3fgkBx0psxgIEeS8IMvRoqRmcQBj4XpEYYsHZNd2HG_pflqzOW9dpEEbJZngbl8EYZYoMObddRSsrxkyf4r0Y7460R0bp5aRa9RBGSaAya2dlJ_AJdAxppM4GvYxdzqnaJWrZc9Z7O5iD0Czg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtODz4ZuWiCIREsTaJVb73aGgCjA1EgJujmC4eGC9-C3WgVl4gKl1OJ0C96wwMEr45sWXGvYYLbSiCNohIo6cq3KlucFidKA8pwOLbNYqKrl0qOVIokMErqYGwK7qP4b-xIcuhLkPeIrqz9IMO_A1tezd6IfKjmThKE9CBugBa7RcNAClTxrUeJfNv6ZKMXyVTqyr4xL7vhs7gpMs9sdqrCLgr8WC_Txhw0dz0xjxPMdMkAVlHljJSikl8WFYW1SgypnWf_EAi-lemJtb-Lwdjt7XaY576-nwa0cmC8BylsXgzsC30LjrieyBb_2__cjPezJSYckshaiQYsUHveCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI_mTx9ahU6HEAXcF6f0dn0shyaBHmyrzxtwg-x5ENXYnsALH4ynIevsuZkhkvQyeVCJ-JIOB1BddumF7EdKP2MkHRMUnhT6whP3w1OLNQBfMi6-FGgm80wLwb1lSxg3rTg_4q-VXHZUXsdsX9Cro63V-Rfx5h8odc1bIYR3rWS1LiP8repImy43r5Ib0kbeH5AuASSCCRvj4rLpkXCvtbU0BVxCejU5VcHiEssvTtzo3Dtj9KRr0fUf5hbQrxx8SfN4eRXW7bujw2aRvezkvLMIOWzG-wud-taWdSnijG59_i6Uze1CwW8DRgW5MZPPBc5ehyO3aXFeD-RWodF6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP4q_76sVGT_ZoAZ1maLVECSgDr9_0zTVMdwnFaWpivMyxVuN4swUW055Kz_F5rd4k5R2wy-MbF2rl0T2ysGMlttDHLpPLk7dXxHUkgeZum3N5f5-qZ3DXaEZ1UpA5mlSKTVm_AF12QUnQl_ZE2AGeWfD_gq8P3c4TC0dafj_2y-2VOcusL4UxOZ6mkeOMruf05jUTey2qB07vRqaE4JlnSNRaXsMSX2bk_EKCnaM7mtmAtoMHJRM0f5I9GdKd5e78TwfkY4kVcyOR82ckf7kBrmS7SpOv8jEGnsh5dO-4sf2mhBpIwddJrIlwJxQqCJEWMTTEdeKPtaX2HfptX9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlIXDYc-EM-t8KD7BXJ4cAM5FsFCh_LQGsFUE2Ucbbppt6HwthmnxmXGsUMoYFf4WJmpFtZBUrR-3THhoFWOugzFG99ceXq2T2cQFiaqtzbQGJfW-2M2d_mjmd1TEF3k-qBB5QD_B-Zesk9jE6IuXb5-lWo2PkdXmizcP7N6ImvOlDaI1a6tjLTUDBaLV3MDatw8Z8UJl-A1BU6staUF16wNp1xSAGNo8XgNs1edUrOOHlTxcu6VFRrChtgR80rCKbURFfhSFIiTGtoxRRmkL90XewojZLwl6j5CN23w7UqzSb4CyqIdrjruP72_ZxZwjlVnd8dVpmWEoFtiGPF79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3RjaDhqtg8Wxu32_jJ2MEcsF2cTz9fLXBzyPdNG4mGOn0IB69MUE2jMZ_eqhx9S6w-T7ubZebmTI_-atRBrp-7PjJwTWBSds0Qf8w36cRvLS-9-PUXfBTTCCwBWgM1a8OQjbYvxrHEzgbsxaUQyWMGGj_FZ6K3VASdhgLXl6q_dlg13trpw97TvQXqlH-tzykvSBofJV3Q1n_-9yJtgzlXwD3x51atL4SQ-ekPf96u9cF7cgjo7TP-vetFREUY78S445QxC7qepdz38g4oVFc-gw8WklwzSlD1jwGAJd6P-No4uT1PJobVdNKes3rqC51TWBP-4haZ94IN-h5M7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQEuqUrnLkAVOOBUuxJl03pMe8gTR95BU3qrRALI15uKYhCoF7Ej5zyOKopTSmmIIt5ky9taMk40PDzSshuO44L3S306lFfzwUfNaCqJxEzW92w0aNkVQMLemt30GMPAM3K-GWZoyljWaF2Yt67_2E9TZCcRc2A8bU7lTszimDaq5u7lUP1oaAVCEagAIpJhaXR0UYKExjdRon9rqp0WGII3SHzB6Y63Le7L7wIuJL32pYudBVauiQNayQl6bfDJl3HR3-2tOu57AIje86RrSUkCmGMLLhVFr2H1Uvus3_KVR4-s2gLFZ3k0iBZS8F-BBUqTG9HifQL-UEIWhSGXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv7-UOeWJA0yiz7x2kQLrm_yZ4xT69f70umKrUnpwnG1c6zeE3i0jcK6AZoyNiCTIyoakI0smZauYFB_K-etcG0e3--PuhYdQXkbRRejJ5peoKsVI_zhGjD1CedW43UyP0f6GKzB1kpqnta39mNzBfssz4Z3v2T8YNKKEUlR1ndXmn_0NjbLHezSon7UufzVVMbM91Fkmq8XMDxPY1Y9wZLx0A34mLj1J0TGTW-63XuXSGJJjf2mkIEevjqc22RswzZt-RnWRsaLlPhcNVvF8ERWm_Mg_ZT9M6DH5QixXupVrmFQqgEkB-Regf5OoN17EiQIajx2XxIYEUmkH0S8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btYw0NczwZYUmkYN74TbDUNn1kX4Mbb5DZjxSqjTpurx-e20-2yFgl6kssbV3BY2tcga5ULwlaxmP8r-gMyqjgy_aVGJ3qU1cGJnEBWJLOXLbyZtthZ0Za25HbBXlZlzKB-o4p26PuDLoxtctH4-8St1XmwPWM8R9km_DlO9MsjRdO8yvMUe2Hz4l9YYFA3B5sO1tE0tR7L6g151YVKdemRlsdnhCBRsMQazaUA3wtn7YLcoYmz9JVGgx6oOV2Fuy9GsvOIbBLtKUsLLZVHZMb8WL-sPDbd-e7-UKka4Vw7TwrBSnYs-mqHduQYlf5VcZRqKJX0lAlUm88wiCqMj3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا
#فوری
؛
مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=ZO5zo1KwRBtdlYhdExzP63eoJLekGmejR5P4TJhIj_gMOI-o0PJa6UZ1Lr7Lg0DmXexy07_UPo9GW3kP9v05dTGNUA0GPGFlMhj30hXm_UBzciFe_iB3KkuAyPEQ10MmVgrgfPkZRKvI-KKyoaqCppTmh5jgOixAug6uYmECgHGxW7eQvZRCQbzscyTLCP7U-E6j_PEzwodVgas50BIKkDik1E-wbKfDLqVeyFUlM7VKbMXvSZLG9x1UUSq3o3Y5ZfgM88t_T_k3sfFt51LRR-afKsuEF2T46dvyEZi43p2e9-PVmQKv1_uM4dTs7otrLhaV66b1CPk9gC0XeT7Sfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7acbde92f2.mp4?token=ZO5zo1KwRBtdlYhdExzP63eoJLekGmejR5P4TJhIj_gMOI-o0PJa6UZ1Lr7Lg0DmXexy07_UPo9GW3kP9v05dTGNUA0GPGFlMhj30hXm_UBzciFe_iB3KkuAyPEQ10MmVgrgfPkZRKvI-KKyoaqCppTmh5jgOixAug6uYmECgHGxW7eQvZRCQbzscyTLCP7U-E6j_PEzwodVgas50BIKkDik1E-wbKfDLqVeyFUlM7VKbMXvSZLG9x1UUSq3o3Y5ZfgM88t_T_k3sfFt51LRR-afKsuEF2T46dvyEZi43p2e9-PVmQKv1_uM4dTs7otrLhaV66b1CPk9gC0XeT7Sfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFgdaa2H-cf29WByl-aBmfAkGI4sqyuX4hqxp6p1ulpzWXdwSJY3WdLBWZDJqqFKIooUHyr558l-WkFcCmkwe4ncXdGwbl8dP-CGn6-fB83eq-zedBCX7KiG7V4eZjGNrqkJkdtDAFQg7mfwTR3aHwnnqdF4p7Xfcnhy1tMCjfk-0ZaWOWw998oNs0tjWmgwX_Hlda3lp0bx1Ge9ekCsljxwkmc5o4mRt7PtGs19AUZebULpYd3u-YgS-skWM1E6vxTUx7ZJW8Jb3FL1x5Ou2Lt8kkbLrkcd09N9cxZE1Hqz6CnnMfp9MO1IjYolfErrHzOzQQr1xbG8GKuof-iNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFu_i15RVbGem7uacHCSrGVxoNHbDWoG6wsFlmMhhZqjvrCLilWpwE_TPpoUSK4zjZcuh4JmHeLS0e8e1Ch4dg4JoKG5ITw9al3ng26zzjRbHTZkGLkuAYiaBrWlQk0ZSH0pv8gDVR52E06ANOnfgVGw8zNpLCfuT_bhGocYsgM1jGGaaDKiUfTO8mds0R3SjoyE3ddN4EaSACbRE0rRPqrJIlKaShXh_w22psmZZ4sG8dYWHewTU8_359gBGGC7D70FxHIWR7x1HJeUKGhDYcbveXIEaTrGzVJZCj_Pj-tYtuiLSaf1OD9N4FN_qftwkYKM1oAJgibh60zBXGpLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXQcSvENmcRPhUU5W6GIBgqZjSpPw4qlqUcKJD6Z6Nt2y-4xwDOwQVup0gTgurw9C86Q8juEmB2JpkaqzxayJNPUaZdXGI_r4-Il8jpNdCKfDhRcz1Mb9KhOGbEidyojrbwtqAhSvxZ7iwNh0rLaZ2XcjONvaD83sRGb_ew2LUok3zBzorzBxh5LeBrqCVoZwIw9mxTdmQG-CyZGQ4BxMSgezVzKlZO6rpWmwQRXUdjOgb7Z7CzwzRIYTRq9PWkGk0PdDzczShdahBsx_7c4AALEpOoittUQB3U1gXsjGoGICyMOsZgLIWWS2CTxSgLvc9x-wlCx51NZwxCbOt1raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmLEzLfq2Ffmo_v6i9vqP4YwALoqRb0NXmvdXVsd1rz7gFH9YyD7OJGu7W7qcRV5CFJXCTcBa2rtr3vN4eHjjbsZSBuCXq0Mwef2Bmgb8yamMVLcCApxsmtVkKj2q4JCUx1dAXTx_CAp04UEerL5YBq2aJ2gkujHjyPSM2OhfRwbbZAOheNvs4AF7dyOvDXHxCUkFnDAxovmsSiYgy1hE-b4zkeLdXi0mu64HCvzwBk9w8PixKvBMfiaOslLHLpvOg4FHTY0erfzyqhUjknRXNS47s74IafN8mo2IPJ_TUNxC7uLJ6mp5Qf-v2cPLEzGxga0xy8OMr08Z99TzOw8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opL4FweE67FhSd_0ASIVCf4Y0o-RYIOcVBHSLD4D10THtu7C1qnNQ1oppj9yZGfEuKEdSy11qkywJznQ6CoYmlj-lthyAQDJ6BB-IfooIQEk2TdBxRhasw_CwTlaA1uHtkp0w4Myo8CT5MZTObbxxT7j6aRKpQulOKlOQV3boJmt7mWyxICohY3fXZDsxECrrro_x2MqAc_smGm6Km1t6jb--IR9vP6Of_1V5vnKqNpkXfIWZAzh7NFqCqs7xpNE5f9ZK_NX8QyKMLzqodvQgxikjEh1q_EOqlM7SfP686MXMOVT46rSfpFepEFFkiVnC79zWPsfiC4WOdxnRoqi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASoU7LVcxUUnkYHU4fIdcQSVpbsuUr8SUpaQIUi5cQMrunjmcm3x19owsI01gOrHdaouH_reyZoTlalN45bDLziVy5O1jVub04MbT8NRELWDtulN9X7x9EI5Y2l1ksskp6g4xGYzG2uYwKgjYB8gjTEBiunwTOr-G1JYd_oUbqQ2uGM8WBabd_7iJqQ-85dYBF6z-iJn1JggXMD_BeHa07-vnPLBob3QcTIl0xOJqL6xO85hgs5mrr6xAwjcV5B1oUiHDnEluWUnhDJNQ9fnaP5_M0Ud-LR19BdQJM_WL8suP0sZCc5DdqNpEGoP7BuW2LWyCj0M3EmsuSWzDqABgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p9DIiwd0svz27YWzjkKRgQvQaseeU0v6xxjntDqr5XUtD-Y_1Yk8t5RvNxvpw72ARiqsZ4Nx6VDu-opeV6JivaN70GjUs4_uelvsX9JaUqy35iTlE-GS7VNdLIFGKID5k4LjJUqmzPElLj6tbQgcf8AarDkFfSOcp4jboV2gKmgEOaZzgKPc8nSGR-wvkhEr2oKUiy32R9LG-Y5j4ut8LIxohX_7P9IV6M8Luo2eBKT90NGc2WI8iAnXp2urUekgxymL4GaJy_X04BjJxFZowW5vAvVRPLxjyzqbpOmPdrazVL03RoB5J9scIKITDgQWtXj-Gi3FrYRgVMarm48K0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkvqkPRVcfPcu4jacSI-mEU9yKdmmtHFgWTgZ4I1yvPKUbqUohVOjTiBoLFODZJW1cicm9IIBhfIzYptFf9uHYq_3IouLpdpSCE4ePqytTJFCEx-JevwlELvO1KP7-PFMnuakIvfhHFHYYPqdJkpZlXEkm98fNNLbNwYB2t0xNEUlEjfR4tI-QtO_kbCi39h46celOmRWochYGX_WogiJgav13AmusTlBWBkeR1QhP9upz8_V9b0mceGHAN0ICGNELvi5TE6bGes1KDnYNcHi_d8FJRkzKc7nTWvadpoSrGmfEKgAa-LGPlGve5FW6co_Q_4biQiKbDSN67xbp-abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f158271b54.mp4?token=acknQVN2SXWCgRnHnWJBkxxhnHPA0qLGyZjHP8hB5plGzCZfCX-iMfpv9i3HdxRwsU4VzV87wMflWrhBxm_5AKczXk75oEAgkcEwvdAy0U3LbUetwDrlKWF3ztJ2SZbMKr7-fggK_1U2gQ1uJzjq0vE5kP_Z6BseLVZN-0aXSmYhNpsucxle1iwoQknB2QXZnOhJZ50CDsuvk-PSzh6nOBbhg0rip-Fu5eWPvHQoBnaX2UR1jpFtRMiPvuk6CfXa-WsbPCtKhNnBENKBA8MkbsFKECrz7D6cp1ycbw-k703ERTznSa-I1zl-rtZPOUMtofX-2l4zxbDsULP0nUHGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f158271b54.mp4?token=acknQVN2SXWCgRnHnWJBkxxhnHPA0qLGyZjHP8hB5plGzCZfCX-iMfpv9i3HdxRwsU4VzV87wMflWrhBxm_5AKczXk75oEAgkcEwvdAy0U3LbUetwDrlKWF3ztJ2SZbMKr7-fggK_1U2gQ1uJzjq0vE5kP_Z6BseLVZN-0aXSmYhNpsucxle1iwoQknB2QXZnOhJZ50CDsuvk-PSzh6nOBbhg0rip-Fu5eWPvHQoBnaX2UR1jpFtRMiPvuk6CfXa-WsbPCtKhNnBENKBA8MkbsFKECrz7D6cp1ycbw-k703ERTznSa-I1zl-rtZPOUMtofX-2l4zxbDsULP0nUHGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب‌مهران‌مدیری‌ازدرآمدفغانی؛
علیرضا فغانی سال ۹۹ وقتی‌ایران‌ بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1V2opBIAWxDbcJ4g3EJYZS8QkMzxKDp1MQNH-EzUFPoK2r3rHDqtzPpbrkP3iLj7Uuvrrx7lgF8VQG3bMEgB219UpFWbQZtKiH794SygQEUkky-fH-qjelayq1h9TblVicTL9MhSdDIgd2RIjVA8AfFzbr94dpYKxkc73fhB2l00c-dqXqO3BLKx9Cl24BpNVQzemMfrFWEh3eJRP6rl6nfFr-KC0-BxbYrG86S_IqYtN4YeVvWJUQQUKk1Eac6UQ0kr7jznXL82XOwWhzsAAXLdIT2RmD9q02RT_p1uBvZZUmPMhu8w1dskhdMxm4mqzhraU5KI4vl-9K78WvVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEr0yR4aeKeOQURdfOiMGUokdIVCwaEsPryvsSKXU3TTG5RJ677R4szkTzJwQBn2cHojRJERvrY922Rpx427yKuMGOSbHT09kytSUFNEkBp7kBklGizEygHFcHEWJgM5Kg0EzNa3w92aVk_LIIXlyARNXXkVQ54ck_7ucY3aw8_LvEAuMiXGx3b4ZAgbvCYQaDwvBsAWN5P7UHGgDAIfVHgtXCfrZVoAmQwiKI7nW36fCe7kLYLOSh441UVNCrKfZHGPBs9FgTTP4d_ZqEnLnlq1yc7X13-0PFIa_KQGPRwSsAoYg2SDWc3bmxH5FHCEd3RxVchMAF5TApq92EHw1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaLAh3IiAILndiyJe7PwEbDpE94c_J2XLsZCvdIzPQNEHPXtrH7fiU1Q07qk43mCOam_ylQOUzyAYr1azB8PMt1H7yNtACJT5z-WDnZQkWwD-CgPlHAz6Pu_nARwKGkCBUrpYrVsDNZk_yy02zC4jTULpAz-J7NFyvXOc3wG0r_AjpZvk7XZ-r73h1--9iFPkSojYszoARzewpbeKo3hyfylRsAmynxOkl8WvvUxaZf8XEAR8kJSYiCSGCekQW0dX0T_fVg3_0TYjbcONd9hu5sW4SvxeaYCQgUjJWj64QTaGFsTMXIYXscBLUyW3r02vIl7ht1ynWEwQezwf1W8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0Bda7Hl8nl-sQFy3N62aHzVjlBhVgys9nzN7GGXbRljVM9n5nTJ22pFU-kLgDCs8e_A7bEI5b5ZVfEixg_p1S4g4Wd3aI8B_FTESbdfbriy2zaU2LqkJJsBwbQTtOIeKyRl2xiil0AdgAoWkT4I3b8Qeq2F3z35WZZq9GDBiDyq5GOj11SUe00PSzwpjbGuQeFAZ1ppPNNcUnox0IJeq0ESP5XJqr2bsIB0t11fQ_E-2mnWOL-Hecjyzgn89ySFi2sadbbCkdJaKZ1AvZDwAjzxzV6t7kfJb7N8_nMGCYdHFSaSHHi9X7OKsGMy0xdZTgaXs02oxd4iDc-bsGUTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=WuzpmhGVwALG53aMhU10QideSYmanOdqPaZOiDCDU3X5th1XcJkS6fBJPWHIQkjqPnsDxbw2eP-a-WYklTQWK_IN--0FGN-rNbwDHVr8xx_4sF-d9t9lwqFb8uSb1LosflK1tENyIRNcRbthNimMf-r5faUvQ2_clxycxR7sOCv2BGyGnLCmQKbQaPoorZeuwZl2ZdZFHXGQo0Rw1pWsa6H6cvs_tKoxcOI9wkgcrIovHbIBttoLaEhnXBLy1N-fUQN6ShcctccbEgC-Z7C6qg2FYz96rVzp1z98dJmO-QtL8ip6L_x-xcsrz_F5FUwAeauBxMR0409qQZEF_V4dQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e22c0f699.mp4?token=WuzpmhGVwALG53aMhU10QideSYmanOdqPaZOiDCDU3X5th1XcJkS6fBJPWHIQkjqPnsDxbw2eP-a-WYklTQWK_IN--0FGN-rNbwDHVr8xx_4sF-d9t9lwqFb8uSb1LosflK1tENyIRNcRbthNimMf-r5faUvQ2_clxycxR7sOCv2BGyGnLCmQKbQaPoorZeuwZl2ZdZFHXGQo0Rw1pWsa6H6cvs_tKoxcOI9wkgcrIovHbIBttoLaEhnXBLy1N-fUQN6ShcctccbEgC-Z7C6qg2FYz96rVzp1z98dJmO-QtL8ip6L_x-xcsrz_F5FUwAeauBxMR0409qQZEF_V4dQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCqQtgXx_8VWKtJRoEbuPKBHdNURkzmz1o9MSxUCFrH12zTOFrG68-W0NvtjTyt1kf03sM6NC32lnpBnG5xI6vajPy9SN2sXq3f6uPOKy_OMs4NOE_3F1e2pA2KAypJU1CsH-0C514zp0MIFxuUK0k-s2p2-dAXsDLXeCyECMYchWxsKJbZlwJVM3WHEsqRPNEanp8lFyZj48c9GTj4yuAIquGYodIcLs76UMqJkgeaKf0EC9vos8wMy6zgcGRkTTjeCxy95f-c1PF3EKDZs3E7BO3WKueBDAVeQbmkxUKJR3Id7HQ3n0gOLHZbtmKQWWxqHCcuZ16SxTIc91hhlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CflROHh8yk50lUIQpeWZ7eSVcU7WN9XbHeFzvTKj_POWXCo4GxY-iriwiMPkpDsQ2no-0nxOYc-KtLxn5IQfz4b_e82fwqi8kL6eFIcivYYyp9cXZ5KHpWqEh2ktdexTwt0nWYfriKV9lMD6lF7WQq1Bp7QQoyYxXaWTpf5-BPILQ4nWI63dqu6IbNJxt_sh0e6zCcQGCrg44jAxXHO8y9cgFIUo-IY3RSQhVk7xYoj_3IM87XHXcibPn5r_XoX9cQLKflCMkxcTzdTgJEjD3aoBbRtoVJrKPaeSp6kNHqsYRGSX4U7_HvlBjaa1Wijy59YfGIzpojP9vaWO2NAucQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXqdFlW1ukQPbxY8ntdc5mPsdqdN_qGBx6fdEjAr28VwvmJSBhbcGRW1gPFNF2sA-h8csyX64ZBI54CbIJQhCqgRkclGS0R40ehk-NEYvyJ-tTC_WvZx7tg7GsVi57J0Tp33KvWcGpzN4HmZscsacILzlLSzZSgGn2fNDVZkEKzrHiXPJkCDJka4rmU91UQJAZteOLeMrm-cg4TP-p3npqsSPoK8QT7UU3xDce4Zv6hXx2TrgKMjAG6DnEbQp1bS54lcnlB1-YGOQR0roOVtK3NIb43EEi6OSvRtpagjzUKJkjc_xCqGYu2CLOJV4POP9vFIH4lbryMd7RAnM3butw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JN9R3x0_XmLkjkoN8z5a1sjEdSgBqS5SM8RkZDv8SSNLYk7AbQZ9pjnHa0sLWGi5P4KqMEKtdXoQmB55jAtYKuLPW0F4W8zzlzeaw8tA_IgGsO1cUMFHeQR3HkuvcsBzbzWz9xe3oLpOuIYk62pI_4SfPPJEg1D64OtgU41uH-733lgZp2r8yKJ8tXDQgsmq33LLMlr92JZ8Ch-OhQOKjk7_lUEfu3VDSSvMpy3V4QBns-Kcf2uish5cS2xJIpXXpGteub42lX-NYOkSCQP4hWD-MtWeqlpZoTcToFqA1Oen_V-KDz6pE-UrCv4YPrfjpz5moG4lf06kME_2pcYXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=JIkHPUwS6WkQyxFphQNkracnKzqEiar-7nRWwU7ky0bqcBmKe9UDW7ThF0pNBaeC3lQR9p596YgCgWNDHnp4XCF22be_x1LXA4cU3YuEYivXkB6gRvZlXflLB8nCpdL1PbTcPsXcPDRpHTGjx9zv5wOTL6TNAkzxyQJ_9GaEcn25SJ_OSDvQJ5jL3zV3WHtsUmqUnVSC-XPc3RBdHecJ18s1R5bIe6My9_dl-MZ6mn1_VrPqFo2L1HCM-69IOApoP9FA1nH58RNWQUttdH0uInxRJHYvsvt0tFgQOAIAhMsMHKD9A2IZjQ2-dv9t6Y4qyAHRT1uLOf8v9PX9pL_YoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbd67803a1.mp4?token=JIkHPUwS6WkQyxFphQNkracnKzqEiar-7nRWwU7ky0bqcBmKe9UDW7ThF0pNBaeC3lQR9p596YgCgWNDHnp4XCF22be_x1LXA4cU3YuEYivXkB6gRvZlXflLB8nCpdL1PbTcPsXcPDRpHTGjx9zv5wOTL6TNAkzxyQJ_9GaEcn25SJ_OSDvQJ5jL3zV3WHtsUmqUnVSC-XPc3RBdHecJ18s1R5bIe6My9_dl-MZ6mn1_VrPqFo2L1HCM-69IOApoP9FA1nH58RNWQUttdH0uInxRJHYvsvt0tFgQOAIAhMsMHKD9A2IZjQ2-dv9t6Y4qyAHRT1uLOf8v9PX9pL_YoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=gEQDmsv4CNz4GE6SSG9AaMyD4qDVHEZ-9Z8ljN1X9_s-gkrRW-bI5tZ6QqfOW-p3tO3Wz5WmvxD7eGmW_9PQBWA_uksTerSMzIwZOsEm9ilSJT74GI4rBT11Gyb_5NjaqRHS9haNhCWIiL-up6W5oId3JtsX2D-RdCU_Vfly09qE2s_cEtBEB6VIkW2FubElQ1A-7BTXjgsjVUomyvoAMMdV4Vj6nRCKvO1zinCmGKg8FyJOGoV3FAvjhUsadL4OGJFqBPFKr3H8fUQNzx8SHB6pBIzcSHaoNkKDtoo4OiafmBHpUuV2CYIofeUrkkUtiBKQGl4IdfcNXoPzDrMp3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e403b418.mp4?token=gEQDmsv4CNz4GE6SSG9AaMyD4qDVHEZ-9Z8ljN1X9_s-gkrRW-bI5tZ6QqfOW-p3tO3Wz5WmvxD7eGmW_9PQBWA_uksTerSMzIwZOsEm9ilSJT74GI4rBT11Gyb_5NjaqRHS9haNhCWIiL-up6W5oId3JtsX2D-RdCU_Vfly09qE2s_cEtBEB6VIkW2FubElQ1A-7BTXjgsjVUomyvoAMMdV4Vj6nRCKvO1zinCmGKg8FyJOGoV3FAvjhUsadL4OGJFqBPFKr3H8fUQNzx8SHB6pBIzcSHaoNkKDtoo4OiafmBHpUuV2CYIofeUrkkUtiBKQGl4IdfcNXoPzDrMp3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#فوری؛ابوالفضل‌جلالی مدافع‌سابق استقلال برای عقدقرارداد با باشگاه پرسپولیس وارد ساختمان این باشگاه شد. قرارداد 2+1 ساله توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iewWcOqTFhH2_8-eWw_78rStPRB9CSQoUdUGCKnc1cbLWuZLKX80puC6ajeYOIPzkaIYyvBcJB0TJcGtYP1MGDkADL7sPO769ZG5upnWN0GsueWvoik8SAhX6_ZFSGyM7RdcKag-lqibJBcZtf3jkint0d_NAcoQ1di2AkGa3zJ6KjpmrJqcLRsS6UEkzouE6D3CHe5HqTpyosYSLyNUPWJO32miNQUmtfWbq2CNvDRhzw9_5nzcM9Iz9u_KQ4gYIaOGufT_-iL8GMcLqgbjGMd5BH8cr1Hurl4Md6R3NZMLLvw3Z7j2-UhlJ1PUe36Ndac5ec_WNUPdXslcjVkmqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtF6s-5LoplNOhL7tAYie8mrx9qIJnvdP-dfZZzNytPv8APWP44VTMJK8KMxTD7dioGPcWLhOfbops5AZ4-KdrC8XHGeiW0KRYHqsmWM6Jq77V-xrraLD2dhQN2PxHDHzg1MdqpPLMn5Zl6l3FA7Tub4hxvlU7BL8jDknAWTVCj3I8xDGyJxRfQeIfk5p9gMx6XtgFkap0YtKY6oTF2wt9Lbj3yuGJi3w3lwsTnDGE5EqPiz2sw_vJY8YiayI9mhqz9mYUw1RmZshHq70N7coJHnYbaG31rsapD3AbiXI37E7IK6FnKsM9FdbFc1RsFzaelJfNOiuAyzy1BdKgHhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=NOLPkKixYOmLvaoNk31szb53XBRYSWddsvEXLqFxHEJPumVOt2ju8k41C8i2zJ7CSpD1ad4A4B64sVe60VtU9U8XQrXq5_Edz3RASgO16EBQaQ8EOhIllwzgXAQVEmhnj464AXE6DWRUS-LPFajaA9GcNJT5K3UQYfQYMtgqpTf3AtbuIfVwOYBMBMm-aLtmUb72uuoUm2dN_kqYaEdn_b5QB6IcmQn6usxk8tY0iL26yv1CR4YPp6NZQmDuAKTiQEmlhV9CoGTYGdfwjHWq6im6n6LSPGJRS_c0H4dM-kQKOqUj6PzCbp4g_DDj_pMznmhp4ky-rfDJzmM1BXd8zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=NOLPkKixYOmLvaoNk31szb53XBRYSWddsvEXLqFxHEJPumVOt2ju8k41C8i2zJ7CSpD1ad4A4B64sVe60VtU9U8XQrXq5_Edz3RASgO16EBQaQ8EOhIllwzgXAQVEmhnj464AXE6DWRUS-LPFajaA9GcNJT5K3UQYfQYMtgqpTf3AtbuIfVwOYBMBMm-aLtmUb72uuoUm2dN_kqYaEdn_b5QB6IcmQn6usxk8tY0iL26yv1CR4YPp6NZQmDuAKTiQEmlhV9CoGTYGdfwjHWq6im6n6LSPGJRS_c0H4dM-kQKOqUj6PzCbp4g_DDj_pMznmhp4ky-rfDJzmM1BXd8zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=B5pFa77c-FXHjhj5RdYAkJgbpQXj5JXMs78RDE6OQRzPLSkH2ATGftIeuR1_dw8ns3ihLSLS-4nRA0hvRCZOiKBD3Q3_pjNv20y1L_7-LILp3fyo-2Q5q2pdCC2Wqa8QpplHn6SPO0FIN9ztB1mD_VmKK64e64WuC-zPHtvXBaQgEgFSPKV3XWM33vP_1i1NVwhlPAx5chIdsoyO2bQWSm8Psmoxo95Uy2efFsowyhQKK-o2eLvdHR59xzNu161kZ1UYsHUJZdz69xT_BaUyXJWAKrkT1FLjJCXd1cCGRPlwl0tV2JyzseDA0kzyjg21m-wz5xwbn4PIyDUVZY769A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=B5pFa77c-FXHjhj5RdYAkJgbpQXj5JXMs78RDE6OQRzPLSkH2ATGftIeuR1_dw8ns3ihLSLS-4nRA0hvRCZOiKBD3Q3_pjNv20y1L_7-LILp3fyo-2Q5q2pdCC2Wqa8QpplHn6SPO0FIN9ztB1mD_VmKK64e64WuC-zPHtvXBaQgEgFSPKV3XWM33vP_1i1NVwhlPAx5chIdsoyO2bQWSm8Psmoxo95Uy2efFsowyhQKK-o2eLvdHR59xzNu161kZ1UYsHUJZdz69xT_BaUyXJWAKrkT1FLjJCXd1cCGRPlwl0tV2JyzseDA0kzyjg21m-wz5xwbn4PIyDUVZY769A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsjke6TbdKyJqrAEfqhmXy5iEbg0qCW-fLi1GXXywRwrr54nAgrW6AKr0UrP5FMCdBeG_znmPwZcQxMu74eZstqM_MbsMkn7-GoFsM8WbFbiuVlEJLr2gknE8JitdCAZH1dbuKo0oDjGXsIDnXRajltASSp0F9sAwNy9FpEwOE4UbnCRvja-goxibU1U-grmwQMKRdujNr_aIBiyUGusj9jwbWOV5OxTZudCD08UffXHR3clxTmq-o1eW8Nb9K8NfCL7ezyNEvxNxnPw4eKKRSAr2wl0dBiM0kP8V1JVFgZEtevnks-_YzVgsUSAj5hoS-xt22EWSl5Lp9yd3i0Q4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEwDv0T2aKMSk6TqUnOkbQj9SrGNjOlU5zfJsp1kcWjbmozhx-i6030CBZB-bRdTfEFXueiepyNaDQJNsaoILHn8fQPn4bNNwhSGp-60CwOJo2o8bfMmg8QhiQtw90A_FOTyNcKdJ8dJoCVTl_lh1IaYslYl51MuXZqkDVhjYCalITPA_amgDQMn8vSmH3As-K9IIErrR11WGBb6SxOuY_4sRYTum8kEAo-AqRc441mmciiKTmiF4gNXoB0b11n7it9zc2bjzYUg1-LYbIOK8xwNeWk8w86l_PKm8e108Sh-uRbJGZEm0LLAZyvOQhcFTpAN5bZV_JvaFnC53AJSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHDFH0PvptHyIoa5NpfFl2EmEcqUlJeDoEZxWxxvLvT1xdX1oKbvKzCV3VrSB2W8qJgYtFaIfnEnUBA6j0AnOv0oY5e03Z-lLLGyep9rU9bdFvEjOHOJr1synt6Wrm68rokATyXxg9qOudPgnl15euyly0iezSEGf32wzsUBcIXzfZ-iNIkQLtis5v17Eb8SnZ6FCdltUJrZ3aHfWGOBJ5FQAhkS-qkzSMe7lG3D2Bvt2-P0M5rvnu80z5g-vnqbJV_wk15zsNt97qlBbChCk3Jc4oZaEn_vBgSe8f2Fpz9Dhvr0Mt0SNZ5Xr1zL-g_0fzDzbuqArx41vIF69-CLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=Y-LSFAq_spOyieY8BP24-2WtpeE6P9xPrFWo_hvWk1SYe8s9qYTQ0IhxzmwsJcOqn4d0g0XGLZUCIsR1RhoyNvp3C-CTmtMlNUvT7Qjr89NIt9jBZ5DET11zRVu6mKVxT-vjlvqfdHPzQtNx-XDxlpAXuK9AZ9dQ_jG5N5omySNny7wIR_ZVQUmGPc0mar8YX_LHJARc6Rf9d_xZI-faaBXUOlj8Kml6P1OSebRDhpja7foadgZp3wDjV8d0Uof6CHF3X8In4fkf3u71yKE0gZp9Z8wbnGNSmp3fqEcSAr4IiyENXo-LwtGJoQ4P9bZyjZoCapblVJuL8U5W7RoiXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=Y-LSFAq_spOyieY8BP24-2WtpeE6P9xPrFWo_hvWk1SYe8s9qYTQ0IhxzmwsJcOqn4d0g0XGLZUCIsR1RhoyNvp3C-CTmtMlNUvT7Qjr89NIt9jBZ5DET11zRVu6mKVxT-vjlvqfdHPzQtNx-XDxlpAXuK9AZ9dQ_jG5N5omySNny7wIR_ZVQUmGPc0mar8YX_LHJARc6Rf9d_xZI-faaBXUOlj8Kml6P1OSebRDhpja7foadgZp3wDjV8d0Uof6CHF3X8In4fkf3u71yKE0gZp9Z8wbnGNSmp3fqEcSAr4IiyENXo-LwtGJoQ4P9bZyjZoCapblVJuL8U5W7RoiXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=CTK9YcVleR7k7a_o-KGWYsQ7ZhriuJF5SVcnBmJVRnj7uNRCTf_w6ANWljjgrLBL1M76Jy_F09O6gLiVsZIHAKEn2V498OSE0fZEFWQaO8u-A1SHpKQLaQ9bZPEvHaIhhyYOj2ytTmFZH6MTf4nMKZwK_1rx1A6PGSO00hiOeaChw78Ymo5ax-LK0Y9Q9neWxdloucBbHVnLZq-9TFCgys3h1BuQZvqn-GCRYRZuV7IO0FVb3rkUHPecTseHFaDPmrZWNuvATUI3Jo2oUjWK6Qv_wrxB96M098J-sfEX_H0sOZPzbpRjX0L0kPy85V4ounsxHoPetDyZydr58ZMFJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=CTK9YcVleR7k7a_o-KGWYsQ7ZhriuJF5SVcnBmJVRnj7uNRCTf_w6ANWljjgrLBL1M76Jy_F09O6gLiVsZIHAKEn2V498OSE0fZEFWQaO8u-A1SHpKQLaQ9bZPEvHaIhhyYOj2ytTmFZH6MTf4nMKZwK_1rx1A6PGSO00hiOeaChw78Ymo5ax-LK0Y9Q9neWxdloucBbHVnLZq-9TFCgys3h1BuQZvqn-GCRYRZuV7IO0FVb3rkUHPecTseHFaDPmrZWNuvATUI3Jo2oUjWK6Qv_wrxB96M098J-sfEX_H0sOZPzbpRjX0L0kPy85V4ounsxHoPetDyZydr58ZMFJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای آلن شیرر:
یا هر دو این‌صحنه‌ها خطان یا هیچکدوم خطانیستن، نمیشه برای یک صحنه مشابه دوتصمیم‌متفاوت‌گرفت. مارک کلاتنبرگ هم گفته هر دو صحنه خطا بود و پنالتی رو صلاح گم شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9Y-QTIPT9BXLY_QCWBTyxtNKcBdDRP_cloc_rz8B4yAYEqs1MTO9AfVnaQM_mypi-pWJCpeJ479FdpOWfWhasQmVVkAlhWaMZ-CPluxy3RUHnI0H28GsD71mNY3N83NpxqkiDXlz72ZWaz5A5IU0w6sDIbH_ES3awJ-4el63u07O6KsXgklhYdvBd0xlqfbm6RXiKI02ORBviAme5iSmDIG1sAeOSSustepOoS-Kj5Fa9d-dEt8Y14xNtvK03yz2NRbOF7J1ElNYNilYq_igZFmCeA9096Fln2DesPu0-qQs0eUNqG7t5hNMjtkS0iqukWnBHU5Z6seN2wmhcNT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbK22P6IqSYXt-_5JoYPCmn1eRbphNr8Q9cMpLmMsDe87NxfKYc8oYLanhIzjor1ahYiNHh9AhmcyJlasSgUz468FPxOl23c6TrGX1ymT1yg9ag-XjSefhYUzeHwPFyO7Jj62uRQ9eYRy3yrdVdX3Nv-GVtKQ85B15R6ZhoKaeLKjuWNR_b3ydnZ1zL3Lm9-kQFaUTeahdJvx21fvZjRwUZI4CUzlR3PN6zBYjCXpOvWvNms6dphrMOQhBvGDvJQYks_s5kvz9YhXKB6SgpavvJAcJGli3M4a6fzKIJJErt5h3Zy-Opjb2njmbkvWq3nTQgrSeBMq40cBMajbCkn-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aq8HPIv6gygymcqR2FJx_VwZT0CZDWQwEGAQmPxpIhYOQXRX9sO-bpLP_VRYXpu37OUw044FiFPfzcBAiCA0-lWL8YfpGYPgBPCynvFGD3jVfGaSzPJgbgolajwZ7YRwdT696x2VFzgv1VsR6KVCdpc4RqQF4_TdWValQdXdG1LtlCBzECML4PWRMIKvii5V8VMEKC-HKuOkslgkslLIovrFtsFD4oi3KLb54IjzjErRNfCI6XBkNVZ0Myvi8x7hS39xEYOpa9ruEHsZYxdMGe98lAaCNRLIQsQxNjZ0WW9qYAzO2H_Ei8FgLiWybu3FpqgQZLCUL-4yqZLl8TFDrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dobZT2uUyVq5MD4ZfpKcLBtsr0kGefJq_crj8lyR_PD-HCntFBY5X7SwKGZvUHoMEFq1rotpJQzFPr5d2Xk-LQmlnlaoXd6eC6v1LzLvnM7MWKCyyBSgtx1JpDQQMxc1iRjTebMA_fT0-ANbMe5WUqolYl4GKtH8qj8QBEHTtezEEOzWkXBY9A7Rp392YHpWWXjPN4-jJTilXxQpfgzlbqqtUrgLn_gWFhGeMMUNawns_CvXE7AR-RR-xmt9tlMj8-WK9yI5Va8kentmsCZSLaAKUgWsiopeMqF1IkwfRIFdyDrB6uwL9gAetYOWoVVNu4uFWpu_TYhgXsZBDTzGoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoeQKfc3qKdT0oAlzYbRV9k8w9ew5GcrDn9YDFsyeGMdZ7RHVbnbxNtqv9q-bsRXzbGkU-HpjkkLU-rNvs9yDFa1GsNwugN4BcO7uAyo0MtCpUveIX7mdYheIhAagjmXyQh3xZ2R-ByXlImb_MJP8L3RPyFn_6_cDWAItxicUgAU5-8_JHLig284Sv8ku2xDNJxCHV2cgTFQIt5AHkrGqcpPWFqXYuOn5eL9C8C44DgxMAiUy2B4iYVyiURY4MRH4ByrQ_UpZgXlueEg5oEXrZR-m5eXJbOeYF8DHqTWw_vVrbcK2NzgiZE10mHCKNzhZJvA4cLRLMErELXo3VmCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfSoaUFne5S3l3Z_0ltUW50tlOE_j5FAf-EWoZZETeV2ICd2he6P2L7rfLRI9Oufr0eFBLaaDqqWB9tTCpbv3BsUtXXIEs_AbipxTy9w5q0g5H2P29_hIshjS8iBXDvKzRBjRZT5kK_cYPdKJT145JOTVQLSLe0SbCojCdq9Wbcv1LlgsFS-m4pLQskT8d068QZCv-uZtOGZmWnIdI0oWt8N-SkPVtelxG27HGOhe-AhmW6ynMf8c5x-8B4CVoBBQaaHajLOiRbYvwrz8_0yeeDMgjvnnV3z7Ghnce_nt44qxVRwolVEBjUzhfHZB-A2JLvcUOYsC6iFA1UnGpp44Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isXtOE8r90os13ZNaW8SKnYg432zVonynuqes4sc8LaDyqdXzGSERfoiViy-XPn0zxbuCEVm1gNgniwu5560XHHyqgNvvN_Eo7UECfiLSCMVYexCMW6uJtH48ZJ2oW_gu4Ic0AIOxUA4tWM_lNeIIyIP29MKrqozBKtocOckYDoHycdUAWAYBzS79O2-NJlzhP9TFmIvsbG1i20f4v041V5--BdeO_2orcyuTNDU3BYSXIRa_YP3oKkLjTAkjFkHXruRK87ocXt4iOcGK8X7WSHEpv2-AAvMm4d8e8UqkuKeOP8EhIRDipS55PudiJSHnK-6Zb6LwavlEYGyqxK_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBKsF1M_rECrGj2hgFXI0uWKtiZuncc4xA7Ad_kUmcWbRzKvagfbc64pl0mvJXFCLBvQsFNWsYVPTVf6XehW3lkF3riynXWGcdIMAU2iMkZ4dfRd0ufn6IIzZ7Cj4MUbxlql5-HsvQUWxVbsdamlZNWK3yFpb1SO7MU1vMmvkOsLT0I3Pgep1RjpYurXo5iCgVjMYo74Rs5bdK_Ua_5cVqTL5Buaq-5PAWofqoDX0xIJFTI1S1MQ2OwFrYyP08oXKo1ioJ1xxqtPFWzIkOSnrdlHypa7edjHZc-TZpvjCfus6llbcFWeNKfcoLYyJH7TY2gik1t3xxeA7GFkiN7OBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=KjRDeLjKEnQ8kxNifQOwuv5CpZKacNd7tMUkN4e2GQv00bQci4x1Vr17XspW2cIEdJ4jF05ND-NvkK6HEimhi4fZMU1qElp1rPpPcRouz2kEreGzpT2atN-PduAyAjp9CwcSdOA3fnHyIL9hMs3H0cYbbieQwZMXZhkZFpyiqXYt2veNN3krg3xvD6xL0hBwP0tNfrU8I8acBgsA29xWqw-E-2rgroCgtJUcOzkLeDk2CGAS1PkoRDQvYlDM20ujrO1ISL_J2493wQiNmgJ0gsFeKo6N4YS5yZaklG1bsMgiJz7m2DEXlGCuC8CnKZ4BibyAf_55EsIby9XdhZeukA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=KjRDeLjKEnQ8kxNifQOwuv5CpZKacNd7tMUkN4e2GQv00bQci4x1Vr17XspW2cIEdJ4jF05ND-NvkK6HEimhi4fZMU1qElp1rPpPcRouz2kEreGzpT2atN-PduAyAjp9CwcSdOA3fnHyIL9hMs3H0cYbbieQwZMXZhkZFpyiqXYt2veNN3krg3xvD6xL0hBwP0tNfrU8I8acBgsA29xWqw-E-2rgroCgtJUcOzkLeDk2CGAS1PkoRDQvYlDM20ujrO1ISL_J2493wQiNmgJ0gsFeKo6N4YS5yZaklG1bsMgiJz7m2DEXlGCuC8CnKZ4BibyAf_55EsIby9XdhZeukA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی‌از دیدارجذاب بامداد امروز دو تیم ملی کلمبیا
🆚
سوئیس در یک هشتم نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=nKtx46LZgcEn7bb5djfLvF4KANAK93IkuyVh-HpPvIzZxFtub7BhkiLIKv0eqtpFzsqDvhOKwW9MyyPvpFWkft9qO9A2RfATzJ0Ngp7e-jJqETlrKKBl78R8SodhQl2kPNDD5DSDqe_L_BSwVSpEJsOGWyytP_4-fC_rI3n86jGXHIPWpE4mb2e7SiyGcCsphaGSgNLUbcnu3L6_QAGVrfmeWspt2Z39rXVQkguoLRUbwU6QqqV74c5MRxnVjWwGqI1Iaol9LyAoW_r3SsQiB9kaNF9-6EDgfld-od1j1OsRrKlk-3XTQDpIP1qvU5z_Jn-zaj0UMuhFbimO_Itlww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=nKtx46LZgcEn7bb5djfLvF4KANAK93IkuyVh-HpPvIzZxFtub7BhkiLIKv0eqtpFzsqDvhOKwW9MyyPvpFWkft9qO9A2RfATzJ0Ngp7e-jJqETlrKKBl78R8SodhQl2kPNDD5DSDqe_L_BSwVSpEJsOGWyytP_4-fC_rI3n86jGXHIPWpE4mb2e7SiyGcCsphaGSgNLUbcnu3L6_QAGVrfmeWspt2Z39rXVQkguoLRUbwU6QqqV74c5MRxnVjWwGqI1Iaol9LyAoW_r3SsQiB9kaNF9-6EDgfld-od1j1OsRrKlk-3XTQDpIP1qvU5z_Jn-zaj0UMuhFbimO_Itlww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی از خلاصه بازی فوق العاده جذاب شب گذشته دو تیم آرژانتین
🆚
مصر در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-iJUhC2Enpt64ecA8x6YneAXaWr9S25t6sofx9mIgyHVEpF19HAb0HRfY1OkoT6oYi_NySNiNcrCgUs_VmCddTl_S5O6RIlOWeRsOUubSW1PPdJRrm9lccoHmLU1On9NBPHFMvyi6vgsXWfQkHyXuoxPAbo9q8AkaWXeikVrWwbVf_j-sljGuxD9rOUYg31LhRK_PwsJgVjijcjKEu2X5daKlVE12_zwsejcc7zk4D1Fsy545sLLj4hK1088ra8IQ3ZTTcw4S1cX4UaABi7033LoGS5ISOGtqKb5ZhaR06Nwlr9TwmZObTPulKdnbXrU761tY2GQl06XsYd4h-m-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQCpaqP9LwATIMh0KIZgHrRnywYAVT3uHdLJ_PxQq2-VFmMqg66wbLk0IJ0ZtwBGgvJ7_ibUbi_7a4j1EPAcdSNCiLslOm4xkMnby6KmsdYxwefo_ZW68jM-B2n1GSaNvOWRo1lCGVZsPW3-4ZEE5YtAHtEHn-FxH3a4i3P6ThNhwMzYGuOGriIR7fF-LSO76J_0WMnPO1pK4pEtk748rbk2pbmjcq1M4oqhcyu1XOgICfrhpiYy44BMTiIwnrRGgpYwfv72CH1zM9lyAZgVxl_FIKi4H6qu99va3To9FftezsmdMPsQIjLgXbM46_pjvgOaQ86g8If6fs9-95tjfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a56858395.mp4?token=jLeWi2q-ID396JTz2JJlh9iebr5hTxOpuFITJhpEbLk_C_oSak59XdfOfqppTE47JWD62hTBpJS-4f-p3a9t7C6SpVeoQEAiWpWUBeaD0eKQ6oLN9gtHmTNgoqAeyyKg8FsEYSws7ZM-WNTijItafLf54ODCTBcUslVPZDR0fVFRlgtT4G3YQiPzDJjGtQk-pTIP93aG9UzTvLRRLbSSz5QUMVidep8gnc25WsPpkFxadTcz8cOfMf6kqmyqI2SMmjJs4_kv1x1Sghxoxy9H2yeYBRnazVoy-HVLnBIN2BbUSKazgcHAG0HhI7mBO_PBpSgRT9TBvOC-GRlZ9uzh0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a56858395.mp4?token=jLeWi2q-ID396JTz2JJlh9iebr5hTxOpuFITJhpEbLk_C_oSak59XdfOfqppTE47JWD62hTBpJS-4f-p3a9t7C6SpVeoQEAiWpWUBeaD0eKQ6oLN9gtHmTNgoqAeyyKg8FsEYSws7ZM-WNTijItafLf54ODCTBcUslVPZDR0fVFRlgtT4G3YQiPzDJjGtQk-pTIP93aG9UzTvLRRLbSSz5QUMVidep8gnc25WsPpkFxadTcz8cOfMf6kqmyqI2SMmjJs4_kv1x1Sghxoxy9H2yeYBRnazVoy-HVLnBIN2BbUSKazgcHAG0HhI7mBO_PBpSgRT9TBvOC-GRlZ9uzh0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دو ویدیو متفاوت و تامل برانگیز از کریستیانو رونالدو
🆚
لیونل مسی در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE6DKOJKUc_eB8NDgXhLKdj3xWjL1UaG0MuHbXLaMwe-h-t7YtuQtMIp724Ozr8s6mWag9NPR7IVZz4Oywvb0Txtl5N-8VRCnDyK0XhQrD42UziMHuhH1daITBkTk_VFVmmyPw-vBDmnu-p31c6c_gM_bpD4WJtNj9nPoO4nmIMqjve8U9xCrU2PBR3B5QOQz0F-sT0tr9_3Z4qlFs8MAonP9wCey2U9dTFLuA2P2ZWkoZ8IvDNd6O6FwkAA4vh21zprKK3i9DLOmw0SWemhBsFI6bhcn8xF6jmWZ015mKNnc0_0QkeaMv0NxOX_g6j9DyQ1OHufwGgh4IQwefa34A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF_oekErGYdLxfzR9t8PWp1Y4LbspdSTgRTfXisyc7VYNZiky-7UA-59Da2tNLwwLYCSSZvk-LiVlJ2BV4Ic-urXuJ1g99VlnIg0-bZ1OqoBk5QS8PuyUubyQfh5rXaIy7TdSjKvoHqgmHVNmqVO3DZecIjW1_pDXfy6VloRoEOJRyOL7ZJsSV0-uXmBJJiSMFqqxWFqx0NrUlaxlw4PP05jYYX1Cma2n6JMAg2vi693Lw-BGpP14bXMFBuhXHqi4kNPFvz6lzi0mGYZursnPBpQXLJFGVgLWpi7K8SF8eZFR1qxQKyF0-KliEIEmblfSpbe3SFvAB47dL_SGb62Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjYv87ubn8IIhfXFZAMU1N_PS6iiPHhhBuFzIuHvL7OK0otBMvXyxK_iFUsUd_GZPCX8KDXBQPhH68GZ1fmH-kGV7VJZc7X6UvEPxqVjLsH9u6HKhkBEIZ1Bt189PG_lhjihFNmXD1nWHorLkgZrLNSKUD6TrKFRaB_A8Vj8OBmFBT3S2kRYc9CV0Mcd5EYRCn0hf10pL8KNr2l4gyoG-sioBS08ZIiBBHGONvBrCO59NRG4_dLBThdvt6dR4es79316y-z6KAZq8-66zecm4b8KjJUNVrOpcCWQrck510SZtGxQzxidcHnZi70kISJctpEg64PwNLb6Aw6ulmD23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSLP1t_yZCy3vlSCdsJFKbClPaqnlOXVTmCNwxsgQbdNOToxYAywkLK917NWzU3WLmr-yJi2hWwFvs-qCSb0JRedNCbv9bE6xeqIcVqKvixO5W0UZuZrs8a8SmnuFLJiJoDFPIdZ5P_9Rr7fo6HoWTM-I5IdDspD3bepfNFbwkiD0jmq3fpWlL9IvKN0Fzjx7r_B4UHXuhnu_j4Gyca7-p-9ELdVmlKkcyAv1_vv5i4lkh_cLrYW2wpAgW5XrSISUhhyze1LjlwDI_DJAhqEvB8b1_mLdphcpgx-nPmYzqNndIMkw9fuhP6UhjBBMpGZmKLW4SmyvADXLR5hh3rYFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOJhZ5jXXzmWrmoCLnZ3qQbhpzbvaFT3b0vCiG7CJAg_5rkFpXXF375Z4UQxtARPJq97N8jbIizgXlt_KmCORNwz0wGK3AURMy6zZR7VNkO-q4NEr_Nm4E7lVRerc0nIWanIWPJLY7OznLgFZ59YgwE82_rNvsR_fas5M363jgvzZuRVQG6vvw-VyT-gOkvb_PI_aZOaDQZR7e9I1eFrjhAcW9m5SW4wn8pM-sUR98Am88wdY-7odwT5ddiCpAvo7UpFVY4dhBWZzgPGs2wQGkSUAYPW2Phus7HHGRxpZJQ9Ci1_WOXnHO3pNcOda4InINNomS3GvIYMtpQqdQLITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25177" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEFvWWuLESE0l8Ear-m4IdOBIBVFg2fRkMqRgDHk17yIQQOov09i0g6gSIpjduNW9PdiNuivlcPAv5LeJwcq_pIY-nv6n3d7J2ljCrw_ywpaPXF_83QXeJHxSlUExvzuTW_fA0WvWoke3ZiK5yO079dC1y9KQjBkfuqa7xGkOAWKJxgbS9RHaUAhs26Fsx_4KagPtSX-GGlcU32p8l2wJ_9eoMJsj05PduUbIOo2WpknWnbmwyy1q4RVlyOZqc1YwKdcJNCh8kEEvs725hzzIY68i7ercb3AJcWFJckumcKALHmJ0Hno__trozE5xSiL2WeSh8-yfcadjRToZ-wpmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPUtLHexq9hE3UPCADEFZPJsisiKeOvYFi4pwpYkcl00jVu6x-LLFZTtni4bxnbfmyZWmWdDwMzjrlWxslwqvnSUW63uHmtwjj85M4Az69NxQvTnk5lL5jGn3l-J5SManplAyskOpQ03f7YxO3fV0TJ_EutUpdn60EXDJC6loI9voiQt6huurMLfx5qB8e8YIJwP-CI6BQ6zR7bw9jHrAAyUCpnC_0ypxF3CBEa3Qr6w4mOoP9QvybDDYJH1O2ONGrX0SSIGH-sX-h52Ey7CMw6MgHT85BFd06_Y9nEm9R3YGzQ0sNBHLbGpThLRmEpt66fILJzdpR_jQsuQXfJ1Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s30-LaP84TSmBNAQ_ubcexG1nfShzfjz18Cg1e3KNq0eESS4DB6iKtiPppAYjR2i1bYFYmfWu-xpjAdtTGIko60Q__Sdw0lI_TITqC68lruRa5aUKW5-QS4qLpg_ctL4iOkYtHwWrkDkiYBQEht5mvsdSEJ6eHbn9lSU8NyJu93A6ryDXSaQKRRh1XJfDfhAVrJ-5ASfCVwYuHiHlszZPtETdl-ObWyOFIpTAsuzyEEFEqhWW2eewY5Xee1PPpGDi9JfhIBqyZLv_tyc8QWm74MIxDZs8iByUoc7UUNsUOH9FbvliOnLXy6a3yVv-9mCQ5TWRDLLYK5rd7__GHGoBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otGilmgVQSBcTZL8u5YQmzKELnn6z1GVrNFyTlkJHWaMBcYPUorE4NEV2VSwAklqqklb7WNJTk2m9F3A1Nb-LSz6lp82w33018xER0yaaccfD7WIqkE3B8cxEPXEp3W45PsInsH0hxZqT6xyB4H-IFpw9UIm6RTkzGTRDUCVb1nA6SLlf5vABxuStwe18AHEmGPKU2jv6EpPqlX_-vZDg5a-aUQq_iW7dhsTSUdR8R5g-zpoSSgdkMObBuCu9r-Na_e-gGsGfaeNEShyUCV6x5GoG7jACFM8t0nZ-JqS1wW8DEa-gu1Q54wcYg3w_Cf0jpRWY_7SUSFPJ_BOyDFR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo68qJV493Ixcq4F6RClsYGznloD3YY5BXt0iA_i6BL7qojAuD3XfiLZm1n3zIGG2l7ovrv5EiALZcA_76pM4X1UWAZbBHIPuyRTirrxerWzrQh2AljogFrF_alCDrop4p-hnTNFO1wFuIrew53-Q0TcQpyNuBg3WDz3HISFx2Nv2cacpEBPnggJFQ0aW_FAnbv6NgRZ4kMUVZEAeC_9OlmizdQg9luD_0VDWZeSIWzf1Y1idSo1Zk0m07fvb8Hxek0qQrBJGwGW6W0LREaHno_6QB0Jxs5XW3AMF_82QPg4sdXmW0QrYZEA4PAbN4kUIXlqEeUdVigIY-1tnobRIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe_RoU28NV6WUWbwUyeJCF8JDQ4v2O_RReD3yQpD1C6By_7lPxklCMiCDcTWkjf58Dxlv7eLzPhBZKJuD-NHzpYyqvfic5ehSCVCla_JYlEc4Sj9whmxAeAEplu60Qbive2G5WZTUwuTaQQNTnqNYTLv-osCD2iEibzRdmCl7_3NDY2NlkqLy2HQlII98_92dl8O9yMxh1ye-S0SQmdI8zHeoYD_g4hVIEuswUMIR4omLzyP_UNsuWI9joF4jEP6Q-ysMrsp2sqH0OoyOg2EZKgpFUcOeGzCezbHP-m1e4HWZP2jpsT_F3lAarwfINnWYsBmOq3Zg6tVrtQcaR3qiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsMqlgn5ESJ5Ce3NlteDlGv0Daw0dNHyBbEsMARpr8CQDzqBg7lY3-FejTcKqzANM3MgP-Zb7BmJ4narp_HkuUeSq9xXidELN8wMf9-dG524y7kyEZJbjNzodKtkoUg509Jy-2NQJZYQUzVfd73QK7PgSMftHIOxUKHTd1WXziXt3CQDyjOt7hFf-z6O16MwYOZCc2wi79Q_8deOZaDdzpvf62FmUZy89HvNy6ipgSidwsJWegqy5eIvEtIPaeEwGsh456RkRj4GRbSNHOFbB4AVRJOwe0gXQSUiHbFYZftcjawpV3LlG7pxPw_RTXRDyk7WSmg8ETK6A66lkamlFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNsgOlQjr8GxJQL3JKwHaz-9zu_1lsqSw2Aio-LYcUDJR4e9798kt4e14FsrIdq3W_rQFikMR8a-OHDsX8qUlusLEJIH4OfVaHtdglU-8T2PSPzpsOkqvxCOihQnVto4O_RKB21f0PKpmldppEDptncfnAAIY6hfumlZ0gapSjrHS7KfdsmuBNPrEJXg6Su6PVoACy4hafmpFQvRqI3poct-0S2QHO5FGBf7EU6Fs3M835Y07c8Uv1CgU1wiT59YDgS3lNnzORL_2jLjTZWTKHEdpWlYekyvz5BIyGH0ml6uGgGgVx52XCYfcDXgzRcuyKaZM0uBq4h8zpUY3yIokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUMLCMmdcolKweT9KW2-s_x9hbBTOTd3BAxdiC2yCFymgChWH22RyX9SbEC0wNOBho8TrRcYJc4GE6zXi57K0TFwdi9J9GSXShfj7K7W4dqjzVaO1Iieng4kiK7KMcL57KZbJresy7nuvLoynBpj-5RT0qM3mBkgHGeONoFRCrOJAYgMY0nvXIISjvNkaREp53OJq7M0zoDl4xPYVwdjT75-LUTPgTvlBCsArECjHQsqmQxnZXDNdp03heqrk_jOarhGVDpWINRCWp-JkYkWbusahJ0my4bOg-dZ012BGrfreXlFhWCjfnjDKHQ2arXf30ZjBvnlW4oms7vl6jGhuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP7b8sgYS00FJnEyovve0H5R1Yac8QS0Lk6uxat10mWMQG-JKH1j8NYaIVRUbawvVpTUrffpYfUA3Uz1Ohot8o7HYJqgSmBIME2dvnE4NMCD5PjQpwP7MR16TVLZhuthlavcH3Lrh0GMejKFKalIk6vvUERdfxGE6Sd_k4lHSQCUaWBW_Tgyga9kY85WgMTdwp88oS5071atSbca3q5k1JKT-nCmk0Ekqtasnd3rk6_FCC8BxxmUpFXF2JIjybPLUPN5ue8d_3g4jQNPfzuOm89n3-m5nH94rrGHvxbvGbgWQDLayQTI5oq3AEP76nvX3Rd8WTHqop6jtVDQmBtXxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIRXz6W9QVShEVBx7ro0H3rzgohjoEg5gXmF22Mifp3g5Jp-P08NlWgY6Cr0Xa2b7UJMalAPzQ1RgTttaYtI7RblgO183kd3hbQ4PK2RWYUZfmBHCclJp4avcGQWgyoK4YTxa3rHwtothkGzsYOlp-O_CytGj90Q66ll2OmMVNUXM7Lf5x__RS36IMGp5GPb18Kllxf2XP1CfCA4WqlL1npkEw9Kq3PaFRzgFH72jw79c97F1Ap7YtWOtPN9CO_OBTvrUNtguLdNgesEzwUNDOGnnvYN4afn23hTTJo95MbPCXwxZEc1OZvPt3CFnGiGr6yb_xYJ7aRlP7yzd0uf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4H8QYOqdhc_TjavPUK5vwVet9rNLUTy8NHF2QgD4CiYipmlgWivcTufFINE9XyQlQ7vgxgmxSgZyEWn86pCMS8IniAgjKklo_ipQnzX0Umh3MT921rVdGffA04a-9c9hfqz_QpX9ZFU7ARC9dt0ednoAom0l9TYJChapvqwgHNu1MBb5y6TpWbIux0dquYCnXhjCFPfan4JmFelKVz-6_D4R5xSwf41HohqQdGFPUre5gkxFtgTaGJekuYhnzyJhq4I3XzhNF4ieL1DBKbnrzqVNA8bJzsygjhdersx3-VvMzX_0PQCmsCPTeQKfQgQOAUia9anjG79VenIDX6163i0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4H8QYOqdhc_TjavPUK5vwVet9rNLUTy8NHF2QgD4CiYipmlgWivcTufFINE9XyQlQ7vgxgmxSgZyEWn86pCMS8IniAgjKklo_ipQnzX0Umh3MT921rVdGffA04a-9c9hfqz_QpX9ZFU7ARC9dt0ednoAom0l9TYJChapvqwgHNu1MBb5y6TpWbIux0dquYCnXhjCFPfan4JmFelKVz-6_D4R5xSwf41HohqQdGFPUre5gkxFtgTaGJekuYhnzyJhq4I3XzhNF4ieL1DBKbnrzqVNA8bJzsygjhdersx3-VvMzX_0PQCmsCPTeQKfQgQOAUia9anjG79VenIDX6163i0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1Pgj5n1rzQXJcxDJVvSWaF0d5LHGX1Wwx0vKCE3n0y0B5OFB8tvs-rtW7t13KYd9sinOJrvzZA5MEjhZ9e9M7zNEVxiTQy6WwGhfUeybXwAxdNF13o35b2LatXdQo0--8veTy88j292q3Up30hyphF92z7nJv5lMskgebNjouIkhUQvn-OV4pSm1XNoriBrKt10eFjR6YqT1vDH8Tl3UE1AhfjoCXi5-1gzBpVa8fnQA132doGbf0ucTaE4XJXSwFCcoWHOi9Y-xhpw7xvmWOVB1ASo7GqdtQv0HLIku9KB7aJMQy1hJCcEpynLUJEuLaZ_QSbF7dPfhWERdpWw-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfU9W5Xugwfk3rZP800W2-g4KSyThrfj-gWuqQ93nsOPXubIObRoPlwtfEkKss_NX3TQtnr6z77oA6gIbgjxTC-sRfSlg6APy2RHtzUfk_Oedx-ML11iHX6cJcY76qdbgFiPyuLbeqUmzELKDKnL_n-ct28ON7WcjOpk1Pv6pHJWvEiddOtwhWpKNDOCX-Re66pajRORn7mRFzWmjX0nM0NUAKuzNHN7jF9KKzpAX0hewpEx5fWiASgA7YVDEpbU_8fpJbUKkyVX16577VV1V5mBDZb3caYn15k2H_0XoOc0AbZ2HP8x3iKD9DRvoxuTa2Te-2SADL6EvH_HhrVgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfCZD_OilL-KyrnuewAcEvG7HtG9XsJpwtPWa6-fcNbEP5umP1pEYdf4D8LrmmH-AlzTl-w8oRN2dBvTjMCHSZVfTIRfVmY96yna6zdCre_sa7HLewejcorRupFVUl7Pgvz7mh_buE6r8UVAHIjBlpEJ69uiM_iK-dZIRz315-VuILCyzAKeGGGZYfdu0tSUogkajYgR2TU9L00WOeDSdFrpOHDdDvqBzIkuzLHAStm0rM3mjAkMD2zCdkzO-dsY33JBcRTEysUqL8AiV3ai7GvFHvJGYlAfjw_oFLur_p1gaszz0Cp5aDlHE2CFPeVrs6iG_vKLLtXzHSMCt2t67Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=SNN24m260kRygp-H8LxO7iydKQPH1v4aqHA1JFw1SA4EzH2gQheEX7ItGHmoysSL_aqzkL_Uzc0qbXHVlKFIfqAsUAGLbQR0T6yRN_yx8y-TSRW3DGpmnlY5E-jJHZpJMnVdnyUnCizNfyfaUsklYSE0dgXK6UI14AP40EqnfAnWIK8KjT9_ahSQqHCQyEMv9SBpmg4icj1JzPVc0ph6lIF-tJ2xev5qpQIgdt47POztqtaajKC557Ol8avfx1imAd25LvjUQHTNJjeJlZXqGEZr38RjiESxLocQjwVcIvrBCdsamN237kGwpyKyaighD_rXhQOCx-udMWWM6XKD1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=SNN24m260kRygp-H8LxO7iydKQPH1v4aqHA1JFw1SA4EzH2gQheEX7ItGHmoysSL_aqzkL_Uzc0qbXHVlKFIfqAsUAGLbQR0T6yRN_yx8y-TSRW3DGpmnlY5E-jJHZpJMnVdnyUnCizNfyfaUsklYSE0dgXK6UI14AP40EqnfAnWIK8KjT9_ahSQqHCQyEMv9SBpmg4icj1JzPVc0ph6lIF-tJ2xev5qpQIgdt47POztqtaajKC557Ol8avfx1imAd25LvjUQHTNJjeJlZXqGEZr38RjiESxLocQjwVcIvrBCdsamN237kGwpyKyaighD_rXhQOCx-udMWWM6XKD1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=ccGKWpajV8QS46KDLbK4OYOGPrmKpmfU3zJ5Pb2tuKQ9agu2Oxf8FezmogAySmvQxSKW4lkMXHJ45XSPeUx8BOPSlwrJDgGl5jmdJiOmhgISmWhELPLRTj09wahSugk19j0MNScflbpu0gnkN15Mnhpnq3aTjQNtBsB06taubHIdKsEshtCsW4DRi5R88pfpW9iVQNEyWo2-4IBj9tO1DrpQb79ZT3J0hqeBWaFvrIZ1iK4MTmPy-gHBXleYpG6noLeqO76aKjj935gQdvRmVcIr79byYf8S6yCycrMUcKuEiq1G1PozWZEEoYGForTDRHDvg0R9FE29Flv8fr5mzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=ccGKWpajV8QS46KDLbK4OYOGPrmKpmfU3zJ5Pb2tuKQ9agu2Oxf8FezmogAySmvQxSKW4lkMXHJ45XSPeUx8BOPSlwrJDgGl5jmdJiOmhgISmWhELPLRTj09wahSugk19j0MNScflbpu0gnkN15Mnhpnq3aTjQNtBsB06taubHIdKsEshtCsW4DRi5R88pfpW9iVQNEyWo2-4IBj9tO1DrpQb79ZT3J0hqeBWaFvrIZ1iK4MTmPy-gHBXleYpG6noLeqO76aKjj935gQdvRmVcIr79byYf8S6yCycrMUcKuEiq1G1PozWZEEoYGForTDRHDvg0R9FE29Flv8fr5mzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWuKZvYuJ2lkJp5iiOR1FxErKS9HHxPgF1SWXkQkIzXK4K8O1mizCCyho1cQ_d46CnlKoBM926mzWsf2Wou1fJILtAE36shtNhUnRJufhU00mcAuaITH8MigCP4nG5R00vJnV_rBqJ_6TJNjF061NRVJW6rcdtxyhxL_uK4m1xTeXfbMbh_3njT_xfV32odyZTyUpUs1RIANX_T5rr44UpB5vv8rDqQIz1IR9MxMyn6YHtId3bjbXaw1mM05S19FvTvJVB6ndUKnKcMQX_X1rPf9ULONJdJJf4zqHD2nzxnr2nWUG9nahGds5YjO3y9nx8WudhSz5H_WrUXfUfUt_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V0jWPhNClU2-beSOLkjPqUAW7cM4Vlq_VZEpWrJOKcfA01aBH4T5Fr8WZwkmE1T_RdG9pXH6l42_9G5bQ3Nhsf1jId9HlEVuMmKVbCwrc6Jc4FfqAFtfOMo66J3LBAQjWErpuK4WpwJ_sJx_AajQQy2gpR2IiHZrMxQRvqt01X8Ts84ErtFMTQA9v6or5vDdGhN5lt8soOxbb4ZZmIhkCkcFaQT7OSacVGqwRzMp7rLvS-Cx39hz98WKGxWy9HPrGxmCSW0jz7AXJqDlZ1ujJIokdOlvCsuyb8fk-SeBvOVw5PGD0475bN68dNloeHVKCLJnzlMZNZt0iULhH6Xm4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz90ZgfCM5t7py6FMYcnCDNlvEjK5opgkAjsEDEBjgndyxisVGvMrnXQKJ33jAsPFLAZBmX6O9st2FmXm4c7WNnO5I9MhS8qrXT3ZZJGGJG4f3u43lHOhsvDxtWDuFUemydzsCUitCvOj7BVNuDIE4AKei0REcNp7LclT-5TGa1emV4V6LD73btP5mkmzlNyzSh97lTnYkkFt6Mj2yt9c-hAqxmVugVcZ1kdqqObdvNUqtXHypL_e3tSiZHn0JrJW0C3b1asd5bJdA9_US9ab7hSLcylT_JZEioWPRT58ETt2kId10oMqXqTOXswMkxWLQ76Rx-sojkSP46MtUD5iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1wPDOHSxFoudnku7NmgKdWMNENv2CTEe8uwj2mlflE2p3uZcgubbHY9falmlsO6433gVDG7NyHsl9H_auXSQQZrotvt0p82EVuU99sSBVnHmzjysjTMSpMCoMYpiksEA9yRplEr8aXavtPvO0TD5fUjyTQrAfi5XBzm22Jvo0kBKYWHe0s_-w5-1D4QJnK3Gf3_2yxW0zGLCaSrUqzU2bXoJb_3Dj32ENya5eiDyUGa2-70xFj0C64I74qZIp2rjPfjR8XiUnWggzb4hEe1KPE4h_yRWGC9JQ-G4XwcyN9u3ka2HBtcSrwlMgUvAYEjA0bxVFJiOHbuCkX-lCheKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nj_-MuXaTYPy_daKnajgUwrrSNtm1VwpYfhB3o6kgN_rSR_W-vya3csNjRNKEi2iYUCK1CLO4DvZH1h-lqVixwKmiBbYlghjjGGBzbWVdxRPXm8uNxx2f2w0Grbs0f2sYmrFzJ_1-y0RbXKSa6NmEcK35ysYVaQefxinirdLe1f1hs4vXQzj5Ca9l7xEJzWae-mXKEyb12F7Z7dlyKAXxGOI-XU_SsjQyIISphxQWPll_76pnj47DMxhocEXQvP7MO7lLd52KkkzQl1o_mn2eW4TQjk1Z6W-h7_y35enpehd0B6Es1i-F4dwimCip5TRgQQYII-oFJ0njiEmBKXovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCqDgC4Kquler-zMJafxcrWNP3Q2CbnP9O7qjFsicBzW0gRH7GqHkg_dUgvuZccbBaA-OONvP8Cv4wvatsUfQvRfBVVknkZRwP_yMVcFAZ1X9lF3TxFyi4Qs9aE7eE7dRSi_6AFAw3TrYrdDGNgUxWKY7X0kE5ivbNYmUJ-C32KItAEDxdupUilxuwjHADUSZVDqKZN7pN3c0DF5YA6mMfeavg4l_ioFewy8_hGV5J7r6wcav5r34GGUuON-JX-HfYY5_vrFyQBGlTQflm3I1JS12BBSxiErEKt5hNoPV5NNIhBK5ZVQtPYn2e_ks6C5FigzHzRPAqpmznhYbNW3Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP6Q6wm6tncTL5UT4XjKDiVrGHa_qIbNa1HhdyldWitPVNuqmkeLssF48Win5qQbs-yGgXBAjDPAADVldm6gqFUUujlhqXW4FXkbkcO4EYa95Bp6aSKOvkL_W60tLuMA5SMtIte-Kg3hbiSR_cljD6WQQ3viaPvZUAwLw_ZSuNlaFlpC0xNDW-Fepv8CC-ggY09LvrZmNRAM61WYuIZ3OKKxeMs8zTB5g4dqMbrxshJoMMS-9Am7-vlcIbfbNBNRO-8H3miT7SUBMkbQP09wNXQwaKMJ0K7vx2GioBoDC0gP8_PZ-NzrAwotcG4p2Mk4nuJIRJBR0Vgfo6ffFaWIeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLNHEii5BtE4hQItUIFTcQdclqj23KW8wyHtEIe-3qxfcRIRdEovT_v5_b4UqLxG5Irn6T3LwTCO4GgZ6LAwzNX6zpDtCsh596NLxvjKJQsaWwhIm4L4_rZHLE8rWZpKj46eYJT_YFBcaaBaVohOcPD49CLtO2d0XDMEBo_5qGZif2LYq9-iH9tKdI4aI1EOszo5ctJkThEvybWd7KOR62IiKtD3SdJ1yFi8UuPbVLwpKyMlDtvukmuPYVrf8j0lZLRYKDd9pI9P2tpVJbz0ImRvZwhRWVwzxrBkE1bGoMoIQZI0xKzIgEJEivwcwCvRkS-xfFJERMLJssfNgaHtOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-sOpww9p3nljlnA91ahcjKnipL1So6zpr_tkcObFpwYZQywmHuzQhm4nMDKtosHV0pTwjOSypw4GhDXFwHXH3d4lM3TNOJlG8ke5UOysqEBCJiNxXq6ZRwFIFTbl8sJSkhAC0digxGixi4FDAsExxDzUMECx5HGN6vsBUgBpBPLs-9PSYm9JsrbR-o-rQEFC-Zq3K2U_AMeWRQ1F1XkFAh-vLrG-3m0Wd2TOopStZLtW9PjrKsfWuGwXv8kqwYoBXq50vsyHWBTxJAFSzD1zFK0B1EJrcJCwao3O3bpMN65qidVIPQl3gMCwHlLFPKdmEyyBXeoF3GZUKWV4Zv9Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPcpWrJLM4564kdjLyF0IiiDOrpEfHdFdkWlbv1CTonUFr7vp__AKCF4_dl-SttUQ2xOseKCFvM0CuVoWyHpmRd1Co2D-LoKlxdIGMsk8aeLuXU-PsRUb34oOB1LtR1QJWLX2ZBVZ76JtwZyQhSQurA_VWla3WkRYxpIrXPm4-qkf4rjsUDSY31x5hQXjEqalyCixXTXe0EBUpZXXLYHXh3vFPv4tXYLBpG9OZEn6pGH0a8wfRDu6aWhmO9rz_mNMN0Hl5k3cSlY2N2b4VqpDWjpz9H4GY-zuDu-z4kRFzhqOuhnUO0CV8B7egT56sPhBGt1rYHiB-5H7-Yz-PlXhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTPDstPMsM5SwYKHlDxLJBg5jlAgjWE--p5t2bMEoyBAqOMGGs7bgCNsp60RKw-xq4QjyqyxChLJed3mWIL_b2W1bTzKV_mHIGyZFYDOdlXOaA43Bz6HB6M6Xno8pYiiaV2YiLDizviQq2dl8hu_2Gbsi0MxOgE4N1wD059ffzxe9_1jcYHEJmHlFQKompVHUWh-Tho00d60OkpKUcPwV3trXq7FfPIpw7gzcQHCLea7hr0NnamczymytMXGXxahC6PcHgHfU_P95mo5K0h1GdsotUg1eWoyMnmVzQZyWOlu7fNeeRcSo-87z6h57hnfTWK19kGMjayO_x-3xA-Z9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1Jk1CTIseHSJ6rPqrYKiZt_tlQLMNciRSyxEmVhoKCkq7t0K7E73G06gMKBKxzIcr4t_U2-AjYYn2_lz0mMp9j9M9HEERKRLpc2Q3-HUe6f2jTYwe2z-jXMoerpq1sPqPkZFzz0yz6l3qYa8V3k9ATtA1p1mz6y40MO9nES1E67Fr0r41dlm16LkRJ8Y2_XP1htal-pwcBpVs2sZkditZsvg6p16XRuyzBpvwBCKWzojW_6vUTJ8q_PJAJgitCbkECu6kEQufaOp8EUFnx6jCTVnqOA_GCmWCS5mXukGwexlSxb3QNQxBIw2eKsuWYLiWH6DvqIGWjVgUe2I7VgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcnSjIgG0FWlU6TdHNu1hXb9vIYYxKzdy4TNVeKwHtg4zCprVYqT6P4dsPKkUbyYmbyDdj2xwbo0JHLosOLssZMBRoF0GaCK6VLn4Hhm0-Q0CIciAJ7WTEBXflwbHjWzJIxLpTAfJ0dK86G5L5Af81n6bPEVVbd4587ju1a8L_BLAYspOGGlPynKtKoD_2RZik3ikJK_VCRLyAlWpLH3vrDIstcHpfTUOTBwMLXS0mAXFoghEwNlfU6p6g5qbQN02TMaznhyqC07PuSLsrp-dWDI0uwxeU6a5F6XavG63U6V5jiZMLKV5OhR1eVUGuE3cOKsR_LyDXt0le-Mvhb9fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfHw0VBPL3JX_uvCs8PjhEZ9CQ6IHU-MxG55pvMzSWD9zvkAhmTw7Ezi_UKV4vRkiMd_L9zgoxzN6wjgfiRe78jlvoHtvCmEb2Ftv5VAm9eVZH4gSS2FZHdXID58whSVGdoJLwBQhOhtxCHmV2Tkh8qwT73O3-_GQoKVkzpeEiqGQC_HP0BGXfTeLYYvdOi3tErAkP27RzRwyiBKcj1Ag6fvyTKnMN0HRm2ThEk0OmvYGjVpvwTRjwreIKjlvaRIYZqrMfnqtxbaSpLLvIwsoS10jsX88b4yaSL0NFrQ5ZpiHlETQSuI4twaSciKIU7IN8lW62j7OSwGkPQdoZ-4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fD2WV6LKOyBiQXNBDkapgT6dvUoxWjiSK9VIkerfNXedzj1eEsY6ugjt3yIHVT5Fo72hsW9GSHdhXcQqKRyBaRI8tzA2T93ijEwx7F7sM__AFIAjhzkSFLdZRfKzJr4ihU15Nh_LIW5Gctb9f1PLjsldjCC_pNghQ4PglBft6qt9364b-MbPG7h39nTQm0K-PuRQo_oiTECV33cIO1DR9XDRcSt4r-3Gw23AO96DL0zPNxMqcspiUsqd2HesL3X5U2iWHe10FxvP-aVplO00uG1rNwWC1kNxdKrGx6hpVgjknFV1vdD8N_UlIsrd5ZrX1V74mvfPSbHm_vFefl9tJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWNgDqInDi6wRtIx0_rqBOT26cEhV_0FOlq5OHTy7Y_hwyZF8HBNqYPzev8-ixlHKT0qA8T35x16azxHIHZLtVDM1uCBEuyqk36uDyHEA9QXyPXlXGM3CH7JIshVNMor1Ktjso2fryWRP4WPSTc6FwHx0b2jX9XkCoUyS1jVG_hXhfQF54rVDY-Q6rfB574xbtrpOLdyN3offmkfHioQLffDburzZHt83G24UeX8QFRQbaA_6NSLBM_BP7ozWc3MdTXde2P2PwRBepCmE82yx5L1ja2U3hhW7UiQJG-f4LMz9yyu2-pSTpnSK_Ydas9t_Q5cTUXHk3UHfr28UfL7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRqlYfFfGyYvLgfXZgCvRrMsVFEfCtNNdJPwWYfd3JkfbrqHf9R6YnBC8MeqBICofJ9EcsVOR5nOsDW11am14akovWpRz31lZf7y4e2-NUxH8yD8AEWF4Hsd2MBwjnTCD1mHzNefMFm7MJw-j6H1XW3RBEzuBpJKfFFDu7lb25LPy5GP41uSe9NvLkV_5sKLe7hSehm60np3UDF1IILzRBS16PcynPU4cFy_JJw0e1dFgovFaz8k_FAOHXga8F6yfcRsUFc2gx_2t4x4XCYlA0y9yRd2zMr_RJtEt1TFzjCCyCeJEG7SukMhRCiDAQRmNswQDW9nSB9IX8shZh0gSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PUc8cLS_-B0uIvYI4bS1gAElVPLjNsW-ziVs3Fk8FEIJCXy3Kha8gsTBlNY2GR6SaWVElyHesttuGZrQ5TmIjHaOCnATHcoWkduecbqfjWD-jo-VlQTR0yoG4nmMjZChhbIzq2s5nocvdCHtAIcqp8vz8WQr6CUXEJJjnycGBabGcCO0LntTwLV1dFcil2SoNYneZtnDjpuIEXQ6PJ6f5tueJNkx_zasSkQIjZDkmwryVth-u9Csx_p7k8YAJGZTTGHspbAhoVNWHGzy_JrVgLmYym4-KhPEInUiiC_FJqKvW0KTZbzMJt3u9QCVJ9iTY01Q20gMXKqI0JmmLc36VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KpS4lo5qT4f79jkCZhXjfVkwuR0M7V6ZXz0wT7TdrFbgpzrQ8qALULukGVuRH4XKIVT027XDMeKLQAWbNkaNth3gwLheO7sR2MLPGEwurx9D5aMXebyVmyCBkoP-0hAVb34gIT1AnXtLf2hZqe5gg2K9sWs8NBkDlcMn226NOajFS4C0jqdtJZpLPl6R8zeZD7pg7NDwmkxHBZFgzUkoFw1v0A5W4imYY-ODrm-dgId15oeY7WquGEnv6mDiDX5ylvc0bYFJRyMdWMJE8Yt8N9WqFxYiVR-OutngrNavLzNbnmd8vKLfVrBlICXZYxhauJRwyXQTEq2z9bCr2CfxQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvK29zkQ7ylKH8n8ytzMUZIHWBGUSC7EChZeY5JcO2_69kMjTVAWndZx2jvnNub_Z3Bvcoxz7cUCzN952tCOjbEu_Odx0nSJ46C_3xyETZZuSY8Fkh0UL3gD0Fy8KDB6xbSxHVNN3nkat_fjxQuhPou3zsYhaWmcFXWSvRIs3zoLvSc9WE-aBKJMJHyEqMCLDiZeK3ydGpTIPbDCLZPowg3zxlO86y8jmTihz8MXJCVk_LVj5SBFHSaM2EA3_jnw015su4XkWVryuu78tXqt-rHJLSmCTiqqfUKOQvvtiK8XUj2d51c94ISYoCqppQJ7K_3X8IQKbfliDVSo0cUmSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZSmjSzHKm5iF72WArsuaV9z62j2M0lOEThB4iKPP_EEBQaWlOfUGnOJoacrGp6zlb_JDz-3wp_HD3PQxhVFB8nY6N6BX_Vo9XF7KBv_WQ0luhQtj1PJ2wAtSrTy3phaltC-Odl0AJW1ZO6_FLeSiespBVSy9wHyia-_kN6tUk2gFm8jmgXfdsg55EHg_OGXNuuO17GL4XaW54zFO8Qx-LSSm5VwU47aLd1xIx_rr7xH8G4qMNKoIcUoAy5UaFyEUEKDMFzmRmu2dtv08gyNG_V7WmHSQX3ouisTieH27RIyZiHLyVyQ5pLBJ1IDMnC77pbweddQETOB7UzSKN1Z1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=WoRhQnkolig6BfTZpCg2xJYmNdbgpupqtCueed2Ch2m5sqJnbEPx0NH7mydPZRTrAiB6_835PBuY_R6aeziezBf69Hd4FbOOVzISKR5xSyS3OlvVok30zeuO9J74JdyresKoDhVGXmldHL0EHMK36NdRbHnqf4pkBOKoagye0xXkum-7Idv4meOGPk_NOkRdI-RQAMEDmkwpl8claQDpqs9kBOcMrVADycWYO2FaBq99MYQVbhTA2VHXFv9bAGpbHUkNlG9N6kzKE9Nhprqz2SEeCVeDcdpPYfypdOKkpB02chWZIHL1AlmTfsdvaY5bYiIsb7kP_HTcr_gYGoFa9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=WoRhQnkolig6BfTZpCg2xJYmNdbgpupqtCueed2Ch2m5sqJnbEPx0NH7mydPZRTrAiB6_835PBuY_R6aeziezBf69Hd4FbOOVzISKR5xSyS3OlvVok30zeuO9J74JdyresKoDhVGXmldHL0EHMK36NdRbHnqf4pkBOKoagye0xXkum-7Idv4meOGPk_NOkRdI-RQAMEDmkwpl8claQDpqs9kBOcMrVADycWYO2FaBq99MYQVbhTA2VHXFv9bAGpbHUkNlG9N6kzKE9Nhprqz2SEeCVeDcdpPYfypdOKkpB02chWZIHL1AlmTfsdvaY5bYiIsb7kP_HTcr_gYGoFa9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhqrrqz7kant-p8NMhjtbBrzPbPiSs_RI7abUlE2HSUfjDUDiClaFIdL3izA2jhE3Nesd0zc0XsacCCiQVad1XXVS8-NPcgSTDuPonMLVSPvQUuue8IqEKhS6zfFt_iiwwET6H_ccZxORgtP6_09-u8-1XQZWFDmxLRuXzIOaIMXtDA-aitkzy3_UEyYOUHClRrP_sKBHNaT3EkDqaSFxdQ7ZEtjdcqhiyPMV-htJNp3XaPC51RB2STX07KQknIx3aI8GlfIZxDi-CslFwkH3uXAHxMCL8w7qWYKovDeOjbppyqKWGcnD_6VG5xKHogG0PX0q3Zb4amfzTfIlg6QaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-BYC2-5WjgSzFzVFXqgGDmE5rIf-_aHdarvrbpcUSzxDk-chNTVhfcfa9lzFd1AFq6ncTjYUYti_X_Jva7bntYzkNP03mM9YrW9KdjakKD4OT9ht8ZXTOIg8w1vbkiSmn8KWfuAAIv8BpPN31k7tstU0xlpeHpmt_Ow-bF_gJOxh7Xn6VVzWJtFxYJ5wxhycPI5ZhsY8fQspwM6PXkTJPzhYKBiymYQcflWPFY0B74sCFBjcdPXgI2qVg8zM2AzF5GzmxK55p0OjrvUnNB3mHk9vjXc14NPER2XgfBcIGg1B06qB9lqx04YySmcYiDUY4jpvydbQh7bp7MpJZasrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
