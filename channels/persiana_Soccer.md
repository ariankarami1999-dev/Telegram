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
<img src="https://cdn4.telesco.pe/file/fKMnCr9Q6qCGF6vrgSyQ65ICG454TEJGbfmQT9z9-LFkyDsyxQ3YoHiaEUomy1vOduTewkxiR3eoPwgUv6JuWffdDRPw5BjoyOY1zk76UN9wAHHxkQo4O8p9iAKINl9tnAKMWCT4rZcJxInxY2f-t1epCRYtvk5rZo_LiXeNXkEQRQKIEG2oMWBVEORrh8ORYywZeiah5BcZ9Asu7ORfoyhHzJ2ZQ9ATTZk_A7s_cZzUEbyCzpDbymzAqgYLngMSoLuwApwzFfFkRgYejeeypBGRywRIdeF-SU-l2FU32N9BQuAhyZ7tRmhZ3nUgRyPWPjCl-ZfEIBCdcBbziccfsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 00:11:03</div>
<hr>

<div class="tg-post" id="msg-25246">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltTdaxveywEqDYQ9FoSJosNlgL1Rov0ecmzpwQ5zxXSnZunPgVuyXPmL36YJXWroaUvdsnEEkJUTYk5Ylt539jnBaxYYx_hbURborWR-jc0yhcM4FfnH8Q1Gs13dyQ_4ptdPDhjVtbhI8OXYVww44PT639IEcL4YY0zF2iVnFsWJswEoYPr-nvW9fsnYrtsrR9VMpYIASnuTjM5K0KFhfIkgrZmn_8xSF1Fm8FaS35aqL2C6mK-bjKOkxXD4Myzueu7xX2L1ZDMqZOCOoz4oej7pmvsXsYkQPum5ZH-YuqkHEkqALUkKqYf5hTpOt8h5ak-2OkGLMMM_r09T4g0Dvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دهوک عراق بعداز جذب سینا اسدبیگی؛ حالا محمدرضا سلیمانی مهاجم فصل گذشته فولاد خوزستان هم با قراردادی دو ساله جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/persiana_Soccer/25246" target="_blank">📅 00:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25245">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giTsCMWGMFEyDbLpDSEgqWcizz7z8pGhsJExIiBkhn68yh-fLPrjDUC50PmOtnS9jawHOsK0ap9wQVFUiI6K-r9NKYuujqUKmOymfmPWi98sJF8EjDlyGjL5Oiq0h_5nuwbCz8nSxiVJZWcYl9Uw6kPnalXyIgLU9MxgxfHcr5l0Kq-J9AKzaES3vZ0Z2TDWjqCA01W5CzYglJcehEBSzHRe1jxDrFpajL8IJdBIPQ1f4D84ir9W2M0rgMOxlSfehb-YogOgrmTCAZ_1KhRloXvktyOQqewdfjv4ShxxGW5hlxml8vATJ2uPy_8QRrsR-IqL6x4cJaRTcIUm_V5Q1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/25245" target="_blank">📅 23:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25244">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7YZaaVZeXVkVje5Fhu2eeZpKVy6hGrG_EpdS_aBHunvpp_5uKDOoloi0dB9eWwhwAPwKgqXgQylRnN24nuf-CdcBbeViRUcNpo-iZNm-X52gNYfpxXQbwEw7wBLPbP9nHOr4Xk44Pg_OGeNilMRzsZzde_CUJIhDO4VpZRngHgEYlVA3eb-CJYjJyOqOVBx1joXOLLWqkx0lXwOyCVdqVFgJlPyPczmd-CZhsIT8-z5zw2spwju13KydZkvYb0yapT1rXe4e9SsPUftkowDrWdePUNs-B6xe9kJRb3YUHss5VKBvjCq4n27zs3O2Y7ikfdohYZ6J1KgQ5zBQ_zzQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/25244" target="_blank">📅 23:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6DTFwFxhPVKJcBUAwxMA4AGbeBKlAidEVL8oe9O4GuS_jvd8wdwPOawdaDuNzN8yUOtPWq-GSPwMfJUiq--VMc19-puYC2zUEvW3wYCQeDMKIL0cwOEufnGuD46Y03cmkDW23xc7oTWdQeUw6mI7hLJ3Ols1ItFsWBw86yBsAqmi8m-MaDm4-vXP4D2JeydwkaVteteyR-2RoDktiuW0sCPjUOOaW1YxAPSS6Hes2VnAiqB3Uw1KZDMAf2z994FgP4YeL_bJEtby5RJzh_cUx4n_SxrkUZicqnxOeH4zm6N9rxn3IlRExt3HzlKZlwtrucGbXBi1Sif04ECDkobWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/25243" target="_blank">📅 22:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25241">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJnJDdJilWJwlkMVptV-D7qlSn_MKvHahZq7gB-LrM39rp2Aij_KuiidcznC3CwfzgdaaYXWjNuQL-rUDo7jC4Zli8Z_Logvk5d0PMq7Ou4TKVksJd9A-IrKNhk5yA5ySHw-gOzWPxV7dcQZnfsp2JjhzELql5xccCQ07V1rB1ZhfwDqe3Ouqmy-xTZtrfrr-0Ss-3t6BihQXCZX1rdd60mf-sCzSEpQmfAYC23wjV8kj1-2EJZaYvv-2GKqHyxzbZOPWmkIGe0tnapuU8045lj-6pMhBWTvlHlBf9MsVkmYZKlPY3k5496tQ4BHEYQd07nzWjN-RAy8J0mKacOQew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLGhTnG8L6nsMjydodK3gbmeuJePR-EgAifHmMnhOzze0hdf4VuIUMYcjCige5aWh66PaZG0J-rjAHQZ_3GAz8OPtGlnplBRV3Gsv1Trcmet9efyjK12dPF211DJFuoS9KBUiU0xLE0Qt8v3r4e5EVkdAVkFBJ0dBbJahUwUIV2XBnlN_2O6_QnMF3MEp1G4pV8WlqAdBhToTow8jXfoSfNxXNLKkRIU-SS-K9Bb5juA6xxciH3tWREFXiLvL8ozK4wYPDJd0GqEgM26dsnr1ySvxBsg_cdQMxqv0HIl-bRCI3z5GazgYjmFvjGqQp2nSoBliTYpAOSi8JYUO7J9xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🤩
مجری شبکه رسمی باشگاه رئال مادرید که مدعیه‌کار انتقال انزو فرناندز به این‌تیم تموم شده و بلافاصله بعدازاتمام‌جام‌جهانی2026 انزو کهکشانی میشود. گفته با انزو در ارتباطه و انزو گفته به زودی به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/25241" target="_blank">📅 22:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25240">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/25240" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25239">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRwe0_0WHGgZ_9VFWSd6lXfvUcd1832r9XrARtKonx22h7NfMX_8bjLUF8Qj8Q1lASNu_4SJlFx-4Ql48khCBO0Gglbpg4YfeqYOeaQin5TD-wm2bhJDzVS_oOW11roOUEmRTGtr6M4fj-7zBJHGM3xE7Zs6CtovTHPIsSStjVjDcwNajNMPw6a4SUMxlUXpRJEzPxpu4pkrkCBU7d06iIQxA3SBa4Q5gV8Z13hl-3be8dXhwucz2u4g5jaTcqNXIoBrwKmsWn0vpK9oeYTJpUnHmL2gSi08P0Y4qZYlj2RrNNb50M1zjv-oRsmBAM_qkiD9po9mvFgGcfY_sRjLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/25239" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25238">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/25238" target="_blank">📅 22:13 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25237">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LA8VH97SsP3pym9eLRs7DHzizsaNynU1UE12mWJJYMQZrN2WeMdvs0helplCVML1K7a-DJ-ZBu8OK4kIeKSB5SVYk1k3Yv6D-G2wktNd8BZFk72QSwB_7v05SqIOGOgB_zkc_ojsB3-IquDeFdQqoovJdseYJ3vCOUeXqMD8NkHybMnzVfPz_bragu1cSJ6i24_Mn3fgkBx0psxgIEeS8IMvRoqRmcQBj4XpEYYsHZNd2HG_pflqzOW9dpEEbJZngbl8EYZYoMObddRSsrxkyf4r0Y7460R0bp5aRa9RBGSaAya2dlJ_AJdAxppM4GvYxdzqnaJWrZc9Z7O5iD0Czg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشکارانیکه درحمایت‌از مردم از تیم ملی کناره‌ گیری کردند: یخچالی‌بسکتبال، محمد امینی بسکتبال، زهرا علی زاده فوتبال، موسی اسماعیل‌پور فیتنس و محمدرضا اورعی هندبال؛ بزودی شاهد خداحافظی جندین ستاره تیم ملی فوتبال نیز خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/25237" target="_blank">📅 21:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25236">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtODz4ZuWiCIREsTaJVb73aGgCjA1EgJujmC4eGC9-C3WgVl4gKl1OJ0C96wwMEr45sWXGvYYLbSiCNohIo6cq3KlucFidKA8pwOLbNYqKrl0qOVIokMErqYGwK7qP4b-xIcuhLkPeIrqz9IMO_A1tezd6IfKjmThKE9CBugBa7RcNAClTxrUeJfNv6ZKMXyVTqyr4xL7vhs7gpMs9sdqrCLgr8WC_Txhw0dz0xjxPMdMkAVlHljJSikl8WFYW1SgypnWf_EAi-lemJtb-Lwdjt7XaY576-nwa0cmC8BylsXgzsC30LjrieyBb_2__cjPezJSYckshaiQYsUHveCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🟡
بااعلام مدیریت باشگاه سپاهان؛ گابریل پین دستیار ایتالیایی محرم نویدکیو از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/25236" target="_blank">📅 21:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25235">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI_mTx9ahU6HEAXcF6f0dn0shyaBHmyrzxtwg-x5ENXYnsALH4ynIevsuZkhkvQyeVCJ-JIOB1BddumF7EdKP2MkHRMUnhT6whP3w1OLNQBfMi6-FGgm80wLwb1lSxg3rTg_4q-VXHZUXsdsX9Cro63V-Rfx5h8odc1bIYR3rWS1LiP8repImy43r5Ib0kbeH5AuASSCCRvj4rLpkXCvtbU0BVxCejU5VcHiEssvTtzo3Dtj9KRr0fUf5hbQrxx8SfN4eRXW7bujw2aRvezkvLMIOWzG-wud-taWdSnijG59_i6Uze1CwW8DRgW5MZPPBc5ehyO3aXFeD-RWodF6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌پرشیانا؛ مدیریت پرسپولیس پیش از انتخاب مهدی تارتار بعنوان سرمربی خود؛ با ایجنت هادی‌حبیبی‌نژاد مذاکرات‌مثبتی داشت و حالا درصورتیکه‌تارتار تاییدکنه هادی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25235" target="_blank">📅 21:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25234">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BP4q_76sVGT_ZoAZ1maLVECSgDr9_0zTVMdwnFaWpivMyxVuN4swUW055Kz_F5rd4k5R2wy-MbF2rl0T2ysGMlttDHLpPLk7dXxHUkgeZum3N5f5-qZ3DXaEZ1UpA5mlSKTVm_AF12QUnQl_ZE2AGeWfD_gq8P3c4TC0dafj_2y-2VOcusL4UxOZ6mkeOMruf05jUTey2qB07vRqaE4JlnSNRaXsMSX2bk_EKCnaM7mtmAtoMHJRM0f5I9GdKd5e78TwfkY4kVcyOR82ckf7kBrmS7SpOv8jEGnsh5dO-4sf2mhBpIwddJrIlwJxQqCJEWMTTEdeKPtaX2HfptX9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امیر قلعه نویی سرمربی تیم ایران:
کاش قدرتی داشتم که بعداز گل شجاع زمان رو متوقف میکردم تا شادی واسه همیشه رو صورت مردم ایران بمونه. باور کنید این تیم شایسته به مرحله حذفی صعود بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/25234" target="_blank">📅 21:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25233">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlIXDYc-EM-t8KD7BXJ4cAM5FsFCh_LQGsFUE2Ucbbppt6HwthmnxmXGsUMoYFf4WJmpFtZBUrR-3THhoFWOugzFG99ceXq2T2cQFiaqtzbQGJfW-2M2d_mjmd1TEF3k-qBB5QD_B-Zesk9jE6IuXb5-lWo2PkdXmizcP7N6ImvOlDaI1a6tjLTUDBaLV3MDatw8Z8UJl-A1BU6staUF16wNp1xSAGNo8XgNs1edUrOOHlTxcu6VFRrChtgR80rCKbURFfhSFIiTGtoxRRmkL90XewojZLwl6j5CN23w7UqzSb4CyqIdrjruP72_ZxZwjlVnd8dVpmWEoFtiGPF79Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/25233" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25232">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3RjaDhqtg8Wxu32_jJ2MEcsF2cTz9fLXBzyPdNG4mGOn0IB69MUE2jMZ_eqhx9S6w-T7ubZebmTI_-atRBrp-7PjJwTWBSds0Qf8w36cRvLS-9-PUXfBTTCCwBWgM1a8OQjbYvxrHEzgbsxaUQyWMGGj_FZ6K3VASdhgLXl6q_dlg13trpw97TvQXqlH-tzykvSBofJV3Q1n_-9yJtgzlXwD3x51atL4SQ-ekPf96u9cF7cgjo7TP-vetFREUY78S445QxC7qepdz38g4oVFc-gw8WklwzSlD1jwGAJd6P-No4uT1PJobVdNKes3rqC51TWBP-4haZ94IN-h5M7hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کنایه‌مربی‌مصربه‌مسی‌ولیگMLS؛ابراهیم حسن: فیفا میخواهد مسی توپ طلا را ببرد، در حالی که او درلیگی بازی میکندکه‌فقط 3 نفر آن را تماشا میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25232" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25231">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQEuqUrnLkAVOOBUuxJl03pMe8gTR95BU3qrRALI15uKYhCoF7Ej5zyOKopTSmmIIt5ky9taMk40PDzSshuO44L3S306lFfzwUfNaCqJxEzW92w0aNkVQMLemt30GMPAM3K-GWZoyljWaF2Yt67_2E9TZCcRc2A8bU7lTszimDaq5u7lUP1oaAVCEagAIpJhaXR0UYKExjdRon9rqp0WGII3SHzB6Y63Le7L7wIuJL32pYudBVauiQNayQl6bfDJl3HR3-2tOu57AIje86RrSUkCmGMLLhVFr2H1Uvus3_KVR4-s2gLFZ3k0iBZS8F-BBUqTG9HifQL-UEIWhSGXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/25231" target="_blank">📅 20:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25230">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv7-UOeWJA0yiz7x2kQLrm_yZ4xT69f70umKrUnpwnG1c6zeE3i0jcK6AZoyNiCTIyoakI0smZauYFB_K-etcG0e3--PuhYdQXkbRRejJ5peoKsVI_zhGjD1CedW43UyP0f6GKzB1kpqnta39mNzBfssz4Z3v2T8YNKKEUlR1ndXmn_0NjbLHezSon7UufzVVMbM91Fkmq8XMDxPY1Y9wZLx0A34mLj1J0TGTW-63XuXSGJJjf2mkIEevjqc22RswzZt-RnWRsaLlPhcNVvF8ERWm_Mg_ZT9M6DH5QixXupVrmFQqgEkB-Regf5OoN17EiQIajx2XxIYEUmkH0S8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25230" target="_blank">📅 19:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25229">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25229" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25228">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25228" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25227">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFgdaa2H-cf29WByl-aBmfAkGI4sqyuX4hqxp6p1ulpzWXdwSJY3WdLBWZDJqqFKIooUHyr558l-WkFcCmkwe4ncXdGwbl8dP-CGn6-fB83eq-zedBCX7KiG7V4eZjGNrqkJkdtDAFQg7mfwTR3aHwnnqdF4p7Xfcnhy1tMCjfk-0ZaWOWw998oNs0tjWmgwX_Hlda3lp0bx1Ge9ekCsljxwkmc5o4mRt7PtGs19AUZebULpYd3u-YgS-skWM1E6vxTUx7ZJW8Jb3FL1x5Ou2Lt8kkbLrkcd09N9cxZE1Hqz6CnnMfp9MO1IjYolfErrHzOzQQr1xbG8GKuof-iNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
تو این عکس لیونل مسی با نصفه بالایی صورتش داره گریه میکنه بانصفه‌پایینی داره میخنده، آلپاچینو نسخه عمودی‌این‌عکسوداره؛ لیونل مسی بعد از بازی: من گریه کردم، چون احساس کردم که هم تیمی‌هامو بخاطر پنالتی که خراب کردم ناامید کردم. اما خداوند برام سوپرایز داشت.…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25227" target="_blank">📅 18:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25226">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFu_i15RVbGem7uacHCSrGVxoNHbDWoG6wsFlmMhhZqjvrCLilWpwE_TPpoUSK4zjZcuh4JmHeLS0e8e1Ch4dg4JoKG5ITw9al3ng26zzjRbHTZkGLkuAYiaBrWlQk0ZSH0pv8gDVR52E06ANOnfgVGw8zNpLCfuT_bhGocYsgM1jGGaaDKiUfTO8mds0R3SjoyE3ddN4EaSACbRE0rRPqrJIlKaShXh_w22psmZZ4sG8dYWHewTU8_359gBGGC7D70FxHIWR7x1HJeUKGhDYcbveXIEaTrGzVJZCj_Pj-tYtuiLSaf1OD9N4FN_qftwkYKM1oAJgibh60zBXGpLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بمب اصلی پرسپولیس که امروز رسانه‌ها تازه دارند روش مانور میدهند سه روز پیش به عنوان اولین رسانه ازش‌ رونمایی‌ کردیم؛ بله مهدی ترابی بدنبال‌بازگشت‌به‌پرسپولیسه و صحبت‌هایی با مهدی تارتار سرمربی‌ سرخپوشان نیز انجام‌ داده. تارتار بعدِ اومدن به پرسپولیس‌بلافاصله‌نامه‌جذب…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25226" target="_blank">📅 17:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25224">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXQcSvENmcRPhUU5W6GIBgqZjSpPw4qlqUcKJD6Z6Nt2y-4xwDOwQVup0gTgurw9C86Q8juEmB2JpkaqzxayJNPUaZdXGI_r4-Il8jpNdCKfDhRcz1Mb9KhOGbEidyojrbwtqAhSvxZ7iwNh0rLaZ2XcjONvaD83sRGb_ew2LUok3zBzorzBxh5LeBrqCVoZwIw9mxTdmQG-CyZGQ4BxMSgezVzKlZO6rpWmwQRXUdjOgb7Z7CzwzRIYTRq9PWkGk0PdDzczShdahBsx_7c4AALEpOoittUQB3U1gXsjGoGICyMOsZgLIWWS2CTxSgLvc9x-wlCx51NZwxCbOt1raA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در‌اقدامی‌عجیب‌ازسوی‌فدراسیون‌فوتبال؛ درحالی که روز گذشته چادر ملو با برتری مقابل گل گهر جواز حضور در سطح دوم آسیا رو بدست آورد اما مدیران فدراسیون پیش‌تر نام گل گهر سیرجان رد بعنوان نماینده ایران در سطح دو آسیا معرفی کرده اند.
‼️
همون موقع‌ای که AFC خودش…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25224" target="_blank">📅 17:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25223">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmLEzLfq2Ffmo_v6i9vqP4YwALoqRb0NXmvdXVsd1rz7gFH9YyD7OJGu7W7qcRV5CFJXCTcBa2rtr3vN4eHjjbsZSBuCXq0Mwef2Bmgb8yamMVLcCApxsmtVkKj2q4JCUx1dAXTx_CAp04UEerL5YBq2aJ2gkujHjyPSM2OhfRwbbZAOheNvs4AF7dyOvDXHxCUkFnDAxovmsSiYgy1hE-b4zkeLdXi0mu64HCvzwBk9w8PixKvBMfiaOslLHLpvOg4FHTY0erfzyqhUjknRXNS47s74IafN8mo2IPJ_TUNxC7uLJ6mp5Qf-v2cPLEzGxga0xy8OMr08Z99TzOw8XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در صدر موثرترین بازیکنان هجومی مرحله ⅛ نهایی جام جهانی 2026 + توصیفات زیبای عباس قانع درباره لئو مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25223" target="_blank">📅 17:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25222">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opL4FweE67FhSd_0ASIVCf4Y0o-RYIOcVBHSLD4D10THtu7C1qnNQ1oppj9yZGfEuKEdSy11qkywJznQ6CoYmlj-lthyAQDJ6BB-IfooIQEk2TdBxRhasw_CwTlaA1uHtkp0w4Myo8CT5MZTObbxxT7j6aRKpQulOKlOQV3boJmt7mWyxICohY3fXZDsxECrrro_x2MqAc_smGm6Km1t6jb--IR9vP6Of_1V5vnKqNpkXfIWZAzh7NFqCqs7xpNE5f9ZK_NX8QyKMLzqodvQgxikjEh1q_EOqlM7SfP686MXMOVT46rSfpFepEFFkiVnC79zWPsfiC4WOdxnRoqi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس ساعتی‌قبل‌خواستارجذب مهدی ترابی و برگردون این بازیکن به پرسپولیس شده و از مدیریت باشگاه خواسته  با تراکتوری‌ها مذاکره کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25222" target="_blank">📅 17:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25221">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmjInWl0U_HS8zExJJOGOIgE2WGaYBuELAf2tGg1Z99peuGMQXGshMYnJX_ITIb-g-Xgtiw_BIgxOeHPetlcGpGdyXwmqVBHohta3dlQGS7mOHLm6jsuo34HfD-A2pvd-CBipCOOF9BlDaM7HNR3rPbgI5VFhFOQrkUg1HJPhMzPWNT7ipXrCJqWsoMthA67JkoAhq09kY3X8AnedVhCPbnrnAwoCDnFkK-K9HE9CNHkHl-v1LmAxh9WowEuzP4twNVgojxzszcG4_yXqka-aZz7XnirfIvn0pPmG-5_ISAn05xTmf2kkknmgc9LdswBltKe4JFDlezzOAX7jceKeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25221" target="_blank">📅 16:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25220">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZkvBkWaPWWxdiGyauG2Zs_XLwCTMT7ltxkI-9LeDGktwPD10AXpKeuodwc_FT29SpbLrfaDVbtVknCOlQUs345NNQPVxn_fUmTB23l1CfRtGJJc5CSfMXzeZ-5BDxR-IcD_i9FgyVFLe-d9DedP-M_mx_-yv7QonBLBV5ezwjFMW1tT3qTdtyUmrlpaHkzKo4k2TEBNam0lXxrowhLPfIoI4wPVkrfESFCM1FvXMymh37i_vg0ko7PaYRk_t2qRy4Rfq-ZE6UbSHSALcr20vLgXZoPovNrPri-2GVRxYc8Usoy0vFmslnjD_8nJbqKZoErHD0koowNkSNzFzQT56Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25220" target="_blank">📅 16:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25219">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkvqkPRVcfPcu4jacSI-mEU9yKdmmtHFgWTgZ4I1yvPKUbqUohVOjTiBoLFODZJW1cicm9IIBhfIzYptFf9uHYq_3IouLpdpSCE4ePqytTJFCEx-JevwlELvO1KP7-PFMnuakIvfhHFHYYPqdJkpZlXEkm98fNNLbNwYB2t0xNEUlEjfR4tI-QtO_kbCi39h46celOmRWochYGX_WogiJgav13AmusTlBWBkeR1QhP9upz8_V9b0mceGHAN0ICGNELvi5TE6bGes1KDnYNcHi_d8FJRkzKc7nTWvadpoSrGmfEKgAa-LGPlGve5FW6co_Q_4biQiKbDSN67xbp-abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25219" target="_blank">📅 16:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25218">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f158271b54.mp4?token=g14ujPBI-IXvzMboW_QWLOSnGVwssf-GH4kWV4R-JOvAXnIt7P-WJ78qQUM87GzBf7Gu2P-SSqKZZ_9pJ525PrF9mKgOTtp4DWa9UbAO3SkN3XVneQCdZ15UY7juNhpPbGywr5J4KZdz6m_shIK5s8fbBAqYdDOpoTHACfkk6WjwR_noqkWjuf3c6iVH6miyHPuhbMo2Du2imgKDyf6ZcynHpEZx_x3z3RdBk4DpC3Zjk8djOp3oVA6ZADsJjmwNqMqIgIUAHgsXxHm2SnwIXlaqnNTmtmMYHOrH6I7LTUJiO29gP7K47h9rpNhB-8uznk8JyB-sOA53cE8GgpA40Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f158271b54.mp4?token=g14ujPBI-IXvzMboW_QWLOSnGVwssf-GH4kWV4R-JOvAXnIt7P-WJ78qQUM87GzBf7Gu2P-SSqKZZ_9pJ525PrF9mKgOTtp4DWa9UbAO3SkN3XVneQCdZ15UY7juNhpPbGywr5J4KZdz6m_shIK5s8fbBAqYdDOpoTHACfkk6WjwR_noqkWjuf3c6iVH6miyHPuhbMo2Du2imgKDyf6ZcynHpEZx_x3z3RdBk4DpC3Zjk8djOp3oVA6ZADsJjmwNqMqIgIUAHgsXxHm2SnwIXlaqnNTmtmMYHOrH6I7LTUJiO29gP7K47h9rpNhB-8uznk8JyB-sOA53cE8GgpA40Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب‌مهران‌مدیری‌ازدرآمدفغانی؛
علیرضا فغانی سال ۹۹ وقتی‌ایران‌ بود: به من برای قضاوت هر بازی ۶۵۰ هزار میدادن که ۵۰ تومن هم مالیات می‌گرفتن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25218" target="_blank">📅 16:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25217">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c66hR58fdjduwckRwYlFi3xqIWhGgoIbID7dsb8Xlr557dEm3nbHgwamCEAh01GDxj0ISrVy4C-dc2vTL4k5clbsjzUihakgbsoKy-hfIbgEbdxTBb4ExI0IhYxrd8g8jzxpnfADIud3oUAQJGDxZe49CpETHW-SJg3Il1Gs9wCoPgZ0qkEJN5eO1L3vnVooGYZUuj0oO7XMI7763KJdDe136NvCqA7_80q0AD1zjZ3O5dWLX-q8fkCwA7uyD0uZudymVwQy0ycSwRdODu0wHWF08wqx0eKZ1fJ0jmi3Eea8xyjuHFHbcWR6X8lzFh86NUGSVP2ga-03gA_LtNWqQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌آخرین‌اخباردریافتی پرشیانا؛ علی رقم پیشنهاد خوبی که از لیگ برتر لهستان برای علیرضا کوشکی ستاره استقلالی‌ها اومده این بازیکن بعد از مشورت بااعضای خانواده‌اش به باشگاه اعلام کرده به توافقش با آبی‌ها متعهده و بزودی با حضور درساختمان باشگاه قراردادش…</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/persiana_Soccer/25217" target="_blank">📅 16:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25216">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGjqtOi4qHZxBvnpBI9dkxCzHD4knvcuWDSco-m4JDfAHBaY0drgJtHmpxCXJhS4p_A4HPprYvp1w4RBllp8-88df2IXztL6DcUVo9DQeRyXdMogN11m1p2qvog92jiRdDzZLI4e2spcCWMPldNGNa_qpxx6hPMuj6yZC2fdHVhDdCAqEkjwkGD8a1zoQ8JKi2UGp90ZGL0kG3iaGB7HMwLZawKG9sdW1gdszA4eu7Z3aP1qVnSjotwq5M23S6Q-AAnFBiSsOzdJi1EobauDc7HV96shjqwLamFHbwAAQ7WWVVItClIoj0AtRc1ehxJWTP04IWW8ZgF3s6_axnmzow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی #اختصاصی_پرشیانا؛پرسپولیسی‌ها به محمد قربانی پیشنهادی سه ساله با رقم‌فوق‌العاده بالا داده اند تا این بازیکن رو به هر شکلی‌ که شده در این پنجره جذب کند: سال‌اول80میلیارد تومان، سال دوم 110 میلیارد تومان، سال سوم 150 میلیارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/persiana_Soccer/25216" target="_blank">📅 16:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25215">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uilha7klNJH7sTUb_Txz6PG4DRXzHm0WXOxM1e8RXQYvdwmdJN7miS5qOtlhpNMUEeZYKuadYGCxLgJN7-ozdzMA-8RGV11R8URLAHF9mwiwt69ad-bmrQLE3YLxLcDY0N0rAD8Bx7n0PhITlIuOF913UvmEz4vkN4f31E0U_LDmw7I8m_yAfY_5jbAvQFJ40k3MYArS3OgD_VvLcMM6y0Qi76GeZr61iG39NczCbfA-y2V3wPJmHD0OlgC45y8Xmw2Lsti3f-ZjlR7z1pcNmjUaw3UD4dLrct-dHTF0j9d2_BglkGVgHlHYvDa4bnRmsF4oQi9wJTtmMLuR7vIejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ آرمان اکوان باانتشار این پست در اینستاگرام باهواداران‌گلگهر خداحافظی کرد و رسما ازاین تیم‌جداشد. همانطورکه‌گفتیم اکوان از سپاهان پرسپولیس و فولاد پیشنهاد دریافت کرده و ظرف 48 ساعت آینده از تیم جدید خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/persiana_Soccer/25215" target="_blank">📅 15:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Be6MpmNN4TqnRhIPTJYA0aEfykec-jL7LzUl2bzQQ6iSmSLNlsXIIRuzGfCGaU8Hq2i4AhtBOK1u8lWvWbyVoolqbT6mBrhJv0yVvm4RsiDXXMKWrEIcgr11GznfKHF03VJDUq9RnDS6-_QftDGP4nGyPlMQyljxiSz0PuS8B_byBxP4O6ieG4zwLCeUDyts8IY7U7SX8GtXpbKmnLq8n2Dg9TECED40vfYDcPeJKNhYZSrgOFr2mKKDAlZJgPFxQS_M_2JoXkFUmGmvJ0jKPpInsEzgZOW7vH0QgkggoMMG0wl1RUBLagKvS_hZm4p5sYrBe2JYjjdkWYVaKxuIzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25214" target="_blank">📅 15:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25213">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25213" target="_blank">📅 15:18 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCqQtgXx_8VWKtJRoEbuPKBHdNURkzmz1o9MSxUCFrH12zTOFrG68-W0NvtjTyt1kf03sM6NC32lnpBnG5xI6vajPy9SN2sXq3f6uPOKy_OMs4NOE_3F1e2pA2KAypJU1CsH-0C514zp0MIFxuUK0k-s2p2-dAXsDLXeCyECMYchWxsKJbZlwJVM3WHEsqRPNEanp8lFyZj48c9GTj4yuAIquGYodIcLs76UMqJkgeaKf0EC9vos8wMy6zgcGRkTTjeCxy95f-c1PF3EKDZs3E7BO3WKueBDAVeQbmkxUKJR3Id7HQ3n0gOLHZbtmKQWWxqHCcuZ16SxTIc91hhlbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«
وزینا»همبازی مسی میشود؟
براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25212" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOK2j00RNoVmR039uyz1caQsCTeMozk5tXhDHhFUQ_BPzK2WoWLPRkU2DXY5LTrATWoJY2AAWe2tQH9WWL6XlvBmk0DXClsOXs2vOF98jX4BgoJsSzTZ5nLb_qgNa6nQi41erUjQJmlaiaaMl3MOn37JecZKdtumIHE1e1_T3KDY8pGcYoSPrTFoHVTrAVWc8yalJq8plxzGV-a9pP4JMEXGBzcA3mjUkbzELBDQi1f4mCMIb0vs5SI4gsLEoiwZtFl-KI589OgyobAs6BcIRbL6iGyZiE-Tlyba9wejrR517zFbn05L9D47RcIUM8rVBfeqF_4wDaz7m_YrKCRTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون فوتبال کرواسی رسما جدایی زلاتکو دالیچ از سمت‌سرمربیگری‌این‌تیم رااعلام کرد. دالیچ سال 97 دریکقدمی‌پیوستن به استقلال قرار داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25211" target="_blank">📅 14:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXqdFlW1ukQPbxY8ntdc5mPsdqdN_qGBx6fdEjAr28VwvmJSBhbcGRW1gPFNF2sA-h8csyX64ZBI54CbIJQhCqgRkclGS0R40ehk-NEYvyJ-tTC_WvZx7tg7GsVi57J0Tp33KvWcGpzN4HmZscsacILzlLSzZSgGn2fNDVZkEKzrHiXPJkCDJka4rmU91UQJAZteOLeMrm-cg4TP-p3npqsSPoK8QT7UU3xDce4Zv6hXx2TrgKMjAG6DnEbQp1bS54lcnlB1-YGOQR0roOVtK3NIb43EEi6OSvRtpagjzUKJkjc_xCqGYu2CLOJV4POP9vFIH4lbryMd7RAnM3butw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل‌ جلالی بعداز امضای قرارداد خود با تیم پرسپولیس ساختمان این باشگاه رو ترک کرد؛ یه عده میگفتن تازه الان میخواد بره داخل ساختمان باشگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25210" target="_blank">📅 14:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25208">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25208" target="_blank">📅 14:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25206">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25206" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25205">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_uFvJxQHDgcyvfq_LcKoCkGsGwKnAKrjVRORUjfs16DmyWWX8C3epvTl9a2zOcC6e7RjWIPdvU_pJLIgfL4-u1eJDLIeeTSk0a0ZQrdxDCvxtiW6j6X2Ea_brGyD-xqqoeoRNqK551op4LmbkGBP5k5SEwMqobysuBbXdK6-uGtQ8gVfSayYvH72wCSNaABvQE_ntLbvqGt3Xql-IvI43OrAVfYEeOvNM53v-TwRyUZBlevva4k5saFSjm2WnVTB9pqDpsbhUre4QdfOBLeV13HzaybcI3os0psieIKZQtOREH096HBmUtcJlOYUK-KjpEwqFjLjlZq4W0LlC1ERQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25205" target="_blank">📅 13:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25204">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEsozZjNPsxJ9fNM4DfXPm3sVrETtbKb54F_WSCTs9mxf07l9PixaVRRof1efLnSv4PB7-q6iyaKOZlBWZ6twwMkZxW_gYUoT4HJyYe9BWk-RoUxIp0y3yIdax0X0kKaZDWBjebBQBRbUeMECdgCIqRadsEQHSCbXpB3t_7m9-uDPw2_h7gbK5Ibp5x52GVyYuPC3PgUDdrQJ9xbhO7oXYve218e3XayE6VHc6-O8NyIAJPF5OKE_jUEzPYD0ab9_g_EUrGr0ViipTvmA54ATjF7sDKtW-pyLBox29bhKkQZndEH1VlMJpxXaIZ7b7dIj9baxYhjYZ-4oOzyC0xCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25204" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25203">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=Nn8ESuE353xRuBzSx4ipg2AjaVIteRxp13j1C2-7613JAQn2Iwy6Vl974NGTN7aZ3Mohw-rJu5EP1r3i-sP5-kXevkdggFD9qsZ53H6DNy-RnpPadYboxuM1DtL6C8MGHSRHNsQvoIpsiz3X_J8gDo-ulq86XzSzgtuliTZF3mErukOL5iwCso_7Ka2iaFmER7f5IA67i2NbqJwmAD2Ract_QjVcO_ke3dAf3WFs3meq5s5YCXSdXYa0zR_KXCDnURuVBJhocVE5uznO0l5DfhvcIRC5rMH0R9NmJ0CMAKqlC0hhvjcqY_p6dbLLRvvEJTT9idTVXv3QJ9qnyMBWwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8123ef735.mp4?token=Nn8ESuE353xRuBzSx4ipg2AjaVIteRxp13j1C2-7613JAQn2Iwy6Vl974NGTN7aZ3Mohw-rJu5EP1r3i-sP5-kXevkdggFD9qsZ53H6DNy-RnpPadYboxuM1DtL6C8MGHSRHNsQvoIpsiz3X_J8gDo-ulq86XzSzgtuliTZF3mErukOL5iwCso_7Ka2iaFmER7f5IA67i2NbqJwmAD2Ract_QjVcO_ke3dAf3WFs3meq5s5YCXSdXYa0zR_KXCDnURuVBJhocVE5uznO0l5DfhvcIRC5rMH0R9NmJ0CMAKqlC0hhvjcqY_p6dbLLRvvEJTT9idTVXv3QJ9qnyMBWwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی‌قهرمانِ‌جهان‌شد، شادی نکرد، وقتی قهرمانِ کوپاآمریکاشد خوشحالی نکرد وقتی قهرمانِ دومین‌کوپاآمریکا شد خوشحالی نکرد، وقتی بهترین مربیِ سال شد خوشحالی نکرد، ولی وقتی مسی گلِ دوم رو به مصر زد روح از تنش کامل جدا شد. الحق که تمام لذت و هیجان فوتبال تو ساق پاهای مسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25203" target="_blank">📅 13:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25202">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=LPrYcNVyBg_gwaJW1ZAhSuxKLhdYGopPuD7NU4yV7gnxbtx0nAhblKCc-vFexd_K_8ldS_rf5bF-Tdn6RGO0SytP9uBKv06UBzCwminRCNXtOj1TpvC8fQFI94HcZbG7YFM6MQMtlP8RRm7vaXJxxxqGKerT1o5MQ678FwfDjjAXshg2p-m5zh6BfB9A9Vbo1QjEXZD_pzbPrJ1BczolqWgtI6GpNRu2CKDapZVcFOVDhPGaO8t8zw46ScyM_jb86A0DtDlBlErY5AOa5VAftF_xlv_zAmb3GDU0A9FnLaNqJLWVWiSjk2vLhoeosKJ78Urw1lg5YtaCShYblR3Mcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/867fd1f608.mp4?token=LPrYcNVyBg_gwaJW1ZAhSuxKLhdYGopPuD7NU4yV7gnxbtx0nAhblKCc-vFexd_K_8ldS_rf5bF-Tdn6RGO0SytP9uBKv06UBzCwminRCNXtOj1TpvC8fQFI94HcZbG7YFM6MQMtlP8RRm7vaXJxxxqGKerT1o5MQ678FwfDjjAXshg2p-m5zh6BfB9A9Vbo1QjEXZD_pzbPrJ1BczolqWgtI6GpNRu2CKDapZVcFOVDhPGaO8t8zw46ScyM_jb86A0DtDlBlErY5AOa5VAftF_xlv_zAmb3GDU0A9FnLaNqJLWVWiSjk2vLhoeosKJ78Urw1lg5YtaCShYblR3Mcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇬
محمد صلاح فوق ستاره 34 ساله مصر در پایان دیدار با آرژانتین از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25202" target="_blank">📅 13:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25201">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZxL542P2ZzerG37yRb5QdURcofh06CZiSAl-lFsA7DXkyWfM9RAI3J0HZiXxSi67gpspVQ7lWww_w5sSI33qoEQTVC5fQk6PRdHCCjG0p-f5e-B9dHIrRFrF1cSvfTFg3IR-VnRiJkn3AEcco1i0-B4e_zAFwSiBETloyTZXyC2e874I-aDiE5uKHPxW8V_IF2cjXlmSGSU8RSbbgiUYECScvWopP9KFr7XbdSgof8IcrfW-rJlye3gv_K3-NZqYFkJ44TlwAdwYU8A_QfakMrtBePwuUGFBI2SKNkjanr07K7_YFB-GYnMO3f0n43vY2ayBNGPaGn6DN8GVSEMEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
فدراسیون فوتبال برزیل ساعاتی پیش قرار داد کارلو آنجلوتی سرمریی ایتالیایی و کهنه کار خود را تا پایان جام جهانی 2030 رسما تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25201" target="_blank">📅 13:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25200">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEwDv0T2aKMSk6TqUnOkbQj9SrGNjOlU5zfJsp1kcWjbmozhx-i6030CBZB-bRdTfEFXueiepyNaDQJNsaoILHn8fQPn4bNNwhSGp-60CwOJo2o8bfMmg8QhiQtw90A_FOTyNcKdJ8dJoCVTl_lh1IaYslYl51MuXZqkDVhjYCalITPA_amgDQMn8vSmH3As-K9IIErrR11WGBb6SxOuY_4sRYTum8kEAo-AqRc441mmciiKTmiF4gNXoB0b11n7it9zc2bjzYUg1-LYbIOK8xwNeWk8w86l_PKm8e108Sh-uRbJGZEm0LLAZyvOQhcFTpAN5bZV_JvaFnC53AJSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25200" target="_blank">📅 12:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25199">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBI_fgcmYdkGQjCC84oaUaaX0GHXMJBV977ClBgXMobgi5itsPE2FGa3nuCZXBvwUnPcMVOsvO0h8vRE9B690efdfI_MMt9dE6fSt-pEa3T9RvMO4Omc4w448PXBzC-p-VlK2Cw97NvAkrz0WRzvLc0Xbi-rALqWXUcAyU7IXlDXbhKEs8mq7TigIZptteDk3fT2boW4wlJMqWTE9jODWVg2xoLzhElAPM-1eyuMjYFxA7mkQ46hgDcqbXmuBfpYvI94cPWBsT41OZUCzhkYGgAB5ovAyr5h9_taAEvZMSak7KOT20pOvfYUowtnnWwQlvdm4f0G-GfXk4qKjmn4_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛سیدابوالفضل‌جلالی شب گذشته به صالح حردانی گفته‌بود وقتی‌باشگاه هیچ تماسی برای تمدید قرار داد من نگرفته و کادر فنی هم هیچ تمایلی برای موندن من در استقلال نداره باشگاه پرسپولیس بشدت تمایل به جذب من دارند و فردا ظهرم قرارداد 2+1 ساله‌ام رو با این باشگاه…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25199" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25197">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=tLCz9Cdx3648pvDRS-JRnVuNE-gyp-tXiFFy0M9drwjvxn8ZrG5YJyl7XgFuhkgFhuKqFvamthMupGwY9CU3OIggGnZW9ubIcp1v8NABmQf5giQXhkGtLmfBVdCMztq5QfyCKDk4g_YNcY8Jvzo_IrwVOFLKUbC47FPGQVX2Rui9MHZC4T06Ti6Pnuklw5shnDoHqqMq-fyaCTRBu5ZMaMeJeToWbAlXXzHNgNXf73xX5vsjwiDT75ejjz8_ug7sdM7o-jY_4mWuM0bgyB-aR4yki3kzr_4Ly8nGhe5D3BTllfRbIDvmi8j3MJ2SqD-jpAPUModWqikVL6z7SKsDtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32700e30e8.mp4?token=tLCz9Cdx3648pvDRS-JRnVuNE-gyp-tXiFFy0M9drwjvxn8ZrG5YJyl7XgFuhkgFhuKqFvamthMupGwY9CU3OIggGnZW9ubIcp1v8NABmQf5giQXhkGtLmfBVdCMztq5QfyCKDk4g_YNcY8Jvzo_IrwVOFLKUbC47FPGQVX2Rui9MHZC4T06Ti6Pnuklw5shnDoHqqMq-fyaCTRBu5ZMaMeJeToWbAlXXzHNgNXf73xX5vsjwiDT75ejjz8_ug7sdM7o-jY_4mWuM0bgyB-aR4yki3kzr_4Ly8nGhe5D3BTllfRbIDvmi8j3MJ2SqD-jpAPUModWqikVL6z7SKsDtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
یکی‌اینطوری هم‌تیمیاش خوشحالن براش و بهس احترام میزارند. یکی‌بعدبازی از تیم رقیب میاد دلداری‌بده‌بهش. خلاصه که یارخوب تمام ماجراست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25197" target="_blank">📅 12:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25196">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=LLvWxgHRPEN5DmoDJ5Wu8qYfOX6JepDTaPMpkjl48q4ZGbDxK8Nq1FbhK9E0dzM6lfaoZIFPtGGvbwijS7qZCrCW15JxpC4gTd4nMGCcCWMZ13nL6wspCBbcHExZXTOCRoVc0yOR_tjjvLu535nJ5AA2P-c_KjVYNl0f-bNg3js_omQItrd6FjbX5qCTk1l7JSwXj53ssNduXuAaG2NvsinS6rJiFRuerYYabFeZa7so5QmSp2H9bP_S0R6xd4MIT2O8wLJvs5Epgb6-GNwPxALPC9s708cMrySI0FP0ldIfsPIxBcukSFQw05TqTuSzE7lq6fHa1ZWxMBzla62OZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9ab7b209.mp4?token=LLvWxgHRPEN5DmoDJ5Wu8qYfOX6JepDTaPMpkjl48q4ZGbDxK8Nq1FbhK9E0dzM6lfaoZIFPtGGvbwijS7qZCrCW15JxpC4gTd4nMGCcCWMZ13nL6wspCBbcHExZXTOCRoVc0yOR_tjjvLu535nJ5AA2P-c_KjVYNl0f-bNg3js_omQItrd6FjbX5qCTk1l7JSwXj53ssNduXuAaG2NvsinS6rJiFRuerYYabFeZa7so5QmSp2H9bP_S0R6xd4MIT2O8wLJvs5Epgb6-GNwPxALPC9s708cMrySI0FP0ldIfsPIxBcukSFQw05TqTuSzE7lq6fHa1ZWxMBzla62OZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای آلن شیرر:
یا هر دو این‌صحنه‌ها خطان یا هیچکدوم خطانیستن، نمیشه برای یک صحنه مشابه دوتصمیم‌متفاوت‌گرفت. مارک کلاتنبرگ هم گفته هر دو صحنه خطا بود و پنالتی رو صلاح گم شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25196" target="_blank">📅 12:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25195">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlV4ZK8q9ts71huhqkxVirnBpBOYMmdaq4AryPvvKfjzge-XEKwINWawOzPB9NcIteBUMyIjTIs_WX9HvwVO2MTOxJXcaTZOfMy0b6gKkzMpjLcQQt3BigSZssS7B7ABtE5YU-uqEaIzCVi7UDWXmGNqwABMfAsWlN8Z_uYyoSz2i2qusLIFUgW_7o1pKpBx9jRgIqJqGMc558P0pquUTGoiQm1A8qGZonmWqrhdWlUu4YNCDIUexynlFilZZL3jsCGefd2hMxsYMZ3J8eJjWOYYh5lhyt8kiU7HDtvpj3TpDF-4fBHeQYO1fEZWa-6YchPfedQlTagwsRkeRAdEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25195" target="_blank">📅 12:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25194">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAmzlzBJpL6vyuAatjIMnGYFY1Tv0cysTY9SKFyQMIn8r97hYpYno6HMryVMo3MmpGJ0-FYgjAWbbLKYFiOi2U0LhUatoG0Yco-hW6mK-MSuLZtrE-afOJBAmib501r6V0E3zvQG1o2jd1UMcwdyca7Rb_jgMQVtu9CTAE-5tSJ-8PIqQF7MPZsOQW8HlEjwCf3ISASm02FYJvRCS4hZmQBfckj7T-1DMjZhKU4ZDdN16r3xvVXwTIrPWG5MY4fjLGmad3tuGyWXZLY3Gm7caboxTABkzRBp2AmQqI36M5hYunBJ2IiqB7-P5EigWDbHUCq4c-g6nhYzyxb8BRrL6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛ ترامپ:
دیگر باایران توافق نمیکنیم، آنها فرصت خوبی داشتند ولی آن را هدر دادند. آتش بس بین ایران‌وآمریکا تموم و داستان به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25194" target="_blank">📅 11:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25193">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhCExSdtuZOazrFWZXPEMYCk_hCWV-MIAgqSzF0JXbS0AiILoE2EXfJ0VMn4h6--EntaTNqCUtfrMfaQ8CHLy6zY9-n2PEl44pnKGLPzaih6CIQCDi7kjuiop3uFFtPJhVgg6Yts5jq5Mt168046rvKvz4kYKo6Je5djspGISy8llybJ7uV97J-iJtvktfkibBJqPOUmgrhlX1jHR2KyU_s5mvXJ98NA_M0QBUsKOVw-o1iEALEVpFmjzer_3P-ZOvMdlFWFiO9khgnBC-JUcHlXHXaFsdVjzZMbHeusiwt-QHduSXdMuPb4lr37Rhw1Dal2tA7QXzdp_KZd06IPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ تابه‌این لحظه استقلال تماسی‌با ابوالفضل جلالی برای تمدید قراردادش نگرفته و به احتمال‌زیاد اگه اتفاق خاصی رخ ندهد جلالی فردا با حضور در ساختمان باشگاه پرسپولیس قرار دادی سه ساله امضا میکنه. آبی‌ها برای جانشینی جلالی بهرام گودرزی…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25193" target="_blank">📅 11:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25192">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3tVGpsaf1Y35o9_PYwzjVU9EdOprWnJFAaum1JZZPzFCkkwgOIRSfXMteCZ4U_pWbDojQ6aNahif9ES8XMkQ7XX661JI2S357TQhjdGnUUxnTQ1sh0f-WpmlAz-LasIJh1cr2MSsKuB7eLY9DFY6_EO_HL00PDZt4vkCKX0nyC4olQ5GN1bXxlGsfsqpuXt24Apf3FvgKM0UzsH9GD7EBroZfjfpGHKXuKl4x6oXsGadxY_PPl9UahW9O7Hkh6OavCixCYCQHVVDn_OMG4TEEuGHPELSisNGQieSzsxZC3lV6hyCSq76xl58NEPapODI4QVqksJyelUmQy6XautVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
#تکمیلی؛نشریه‌گاتزتا:سران‌باشگاه آث میلان به دنبال جذب فران گارسیا مدافع چپ رئال مادریدند که در لیست مازاد ژوزه مورینیو قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25192" target="_blank">📅 11:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25190">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8O7v9uct29S8qIrfOafUEV5UWYYNEwQ6TUe4adoP1yWmWfGh3vKLYbuLbnI4nIV9McSgZta8Oo2m4cIfuu6-Y_SaDU7EKSbWiepFpe4GyTyr2IMZHOp5DCq2gxXM1L4soFeDZ5do-jrrGv0inLLyfZ8gtShDOdW_8T8DJoS7fcU5rMaZtfHtwho2UkEfSmbqECQL1Y5e_AwZC_I1vy9_3jM7_YbnBHsmEa7P7p6AupA8uPEXwh3ZH8SDgTZRtYnKqfJdpG5M0gP4mVmAUi5zorPra10vYjg9jPW7OvYS4yc9muywje-0VkdyZ_8PavMkDM2bc3MKOocr_tc7gL_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25190" target="_blank">📅 11:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25189">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSJI2Jg4U5rkrMe9jPDqgBOnIz_1tfI1V99Ijs-QrAUB4a3ay1DQR752vRF1qC11_znoNXJ1vf8NLlSV7yujvZNTFpx6Q_DJbTbLBvFvVSTL5TODVLzQZmcvlIoccJI68MxBofiN-w_HQfRCUWEZDOKHT5ZnG43qYEvon94bXiUZuvsUm2Q3yy5jQkTOiTP971RgmopxrZWoxIkTNO8tE5T7tvguwxBszBGbsh1D278ZAE0-WY9kht7-2eoUkZgMVnFE3utOisWYrlyo2AfbloY--PAAaT9zB8UWkcIOUgfYT8z3W8lcmegWDU9bq5yvddUmRMj7redU0jheIbMSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25189" target="_blank">📅 10:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25188">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVHsNFDVoCF7IEKURNjbl9b20td5PwR7qYYJ7NHi5YzJM39IA80hOVptqMSqvdx13m883STcmXqaOacz7sWN4LRnq5DGJI3nB3hc_cBEvXxvLHvM1yAtemtXPsYwvgGHp8_7dSdSytGbI7nlaTMJ9ZeplC0pFBR2S5VP6rwJu6Bai_qzUG60cE3HC9fvAQl3YYl8tMI7vW6VRZEMaNlm3tKsoCHe1dizZkf1Tm7QeDSxJccKYruSiPbq_IQyoS5R-_prZPrFPpYiQbX1La2J-EMm6YgT-QWEKkKgUr5wpj0PnmOJIv2BPUi17WZy3R3x-PXCVsBDVFCyVbhEQRA2Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مونیر الحدادی ستاره مراکشی استقلال که قرار بود اواخرهفته‌پیش‌به‌تهران برگردد بدلیل شرایط بارداری خانومش و هماهنگی با مدیریت باشگاه استقلال روز دوشنبه هفته‌اینده همراه با همسرش به ایران می‌آید. منیر الحدادی دو فصل دیگر…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25188" target="_blank">📅 10:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25187">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ9dDns9EwI59Am6aQo0bKAmdouf6jzNmuOxN8Tgj5yk6aUTVqeuX752A9uW11v2yoJm2fOYJWNYYCOyEb_VW1blYestqhdbtB4bwXtTzQjOqnk0thNeEMfLq6wYChI28BWE6wwouctj61-3WNfnJKEBDdbEjfAPZoikTvcRfK7lbkcKptVZl5JNdothpo8EZgWR8rLSxmU9d7NaKX7mKwLqAvx0W2vl9_3WDMhsTFPMIY0NHP6UY7vf5wFF3y02G5STEJSo5MN70XdhSL4Nvdv5PoQY61C92kGy6ZCmpMoNQ-fuMFA0qWjOjAquU_DEfbCHJ7Bl4-AP4pkJpQNpKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
غلامرضا ثابت ایمانی هافبک‌میانی‌سابق ملوان با عقد قراردادی سه ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25187" target="_blank">📅 10:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25186">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=rfPSe5O8CXi48xG-eBKDBTb0Ut1Lyr6oIGcY9OqdArJO3zGIwlTcSQAibYVQRS9ytv5oc6twMVmOCt5kDHMtjzEVY_hkZHMUA58GahhGzQ8WBFILLH2x3I0GKfAA7ssxecew0N35EMNyZCzDz-lVlXOmLGVm4ToTWj2MtbKWXx7ibkpobXcP22bpHCHUltq2Cxf-zQf2_P8onXcy90BUEjtZTi5kjVqids1mY8ZtDSfzFeacXevHvINHn8kHlyg1fz0OFcgs1-0rwIuDfjjazI7QPVDfSll-qJhJI_OFvq2VTiurf5Q3pgL02zs7flW2xNhGxFIqQyvpzdFWZtR5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c548a97c.mp4?token=rfPSe5O8CXi48xG-eBKDBTb0Ut1Lyr6oIGcY9OqdArJO3zGIwlTcSQAibYVQRS9ytv5oc6twMVmOCt5kDHMtjzEVY_hkZHMUA58GahhGzQ8WBFILLH2x3I0GKfAA7ssxecew0N35EMNyZCzDz-lVlXOmLGVm4ToTWj2MtbKWXx7ibkpobXcP22bpHCHUltq2Cxf-zQf2_P8onXcy90BUEjtZTi5kjVqids1mY8ZtDSfzFeacXevHvINHn8kHlyg1fz0OFcgs1-0rwIuDfjjazI7QPVDfSll-qJhJI_OFvq2VTiurf5Q3pgL02zs7flW2xNhGxFIqQyvpzdFWZtR5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی‌از دیدارجذاب بامداد امروز دو تیم ملی کلمبیا
🆚
سوئیس در یک هشتم نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25186" target="_blank">📅 07:43 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25185">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=rfLwdHnL0ovxgwXVILRPTIrQOIXALExwugsDUWw2j0qdp6_jwireEnm09RiBOcpzdi0dQdGiRg8AOW5T28mSDl1IXuOcvaA7LhBr7YYvuyMHBrnQ5jGRTfklW1bKycDUYoo9VlktQ9MoRBM4kXG301Nn4w1fIOPPzffbJdQ3LofTVfw_CoBKKGkhLqRS4XQYCCOv7ABhlPN_-SIT7GiNdIHe-yt4Pi7tgu1eDMyNoQG-cOWqUUyuKGW5jDCBe8zzH7yBfLEbEgEKmMqqcFEdhdW0x1zdYfWsVCfhUzvlgxAHGbFV7_l3BBJSOmtBuXKB7oxQVh5s6yVtHcUCQ94BeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a83c29d01.mp4?token=rfLwdHnL0ovxgwXVILRPTIrQOIXALExwugsDUWw2j0qdp6_jwireEnm09RiBOcpzdi0dQdGiRg8AOW5T28mSDl1IXuOcvaA7LhBr7YYvuyMHBrnQ5jGRTfklW1bKycDUYoo9VlktQ9MoRBM4kXG301Nn4w1fIOPPzffbJdQ3LofTVfw_CoBKKGkhLqRS4XQYCCOv7ABhlPN_-SIT7GiNdIHe-yt4Pi7tgu1eDMyNoQG-cOWqUUyuKGW5jDCBe8zzH7yBfLEbEgEKmMqqcFEdhdW0x1zdYfWsVCfhUzvlgxAHGbFV7_l3BBJSOmtBuXKB7oxQVh5s6yVtHcUCQ94BeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هایلایتی از خلاصه بازی فوق العاده جذاب شب گذشته دو تیم آرژانتین
🆚
مصر در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25185" target="_blank">📅 07:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25184">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4Y1kUgwXh-QuRKkLKRudz0UEDrfJ6hY0jwEGTuwpY6vN-AcNR2q7qkLwyeqbna8eUliJ97ryJ_0-hPVWJzLC-xEY2qA1Ju83j5DFk5wor2r_jdp6zSunWTof3wtObPxMJy_ZeHsPmoLB3DI9aHbo821xivovF0Ih85mVu6E7lEnrH4gkquun3lFRPudGr7Me0oAFmv7Ec9ZZzPtflSDhwMrtadFqrg_VZXfX6gCowfZGpOj0g1w4HC7oM3LEsaE3Kh6g0UC9HDxg1WYcD4e8Ok4cNH8uy_lG_TiEJTmU2A6nKc_BGAA8kNS-s1BosZDSceut1GyXZZ13SO32h-laA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛ از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25184" target="_blank">📅 07:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25183">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQpZ0lGVHV8ViRu8IktuG6I7xhM8ksVmGBwgfNP_N4YG0IVZBjq4c05rTP_3TKgLUaEUZTTM6_Fk0cKzm21n2tQ6fWRaJFTMywuVwAkXa37Bu_kCWQVBrekKgrRhdia2oZzZkLpu0uJWha9xfVmybewQ4d91isGXu1ovtPoZphqMsJk_F-FeGhA5SsybQB6xpjOPhraPUw4nXobVevES0b9KJq15nXaCjjYo4fACs5QIf-liQ85HWDk5TXDqJsFpcEAGb8Mj0eAzrh8yH5FlZObhgdu6FKIp-Ke4N-S3c6W7A8ss5a1bb7cMnpWzOxxjutgLyUeYkxAV9eyAoZPCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌بازی‌های‌دیروز؛
از حذف‌یاران لوییز دیاز از جام‌جهانی تا کامبک تماشایی آلبی‌سلسته با درخشش مسی در پایان مسابقات مرحله یک‌هشتم نهایی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25183" target="_blank">📅 02:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25182">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a56858395.mp4?token=eCDlJvolCAYktCcRKTFjpHgYbgz-KxfGXA5hLLs0LFArsbBzBB2r9azErmGNJKQCQmRdRZ56s794DOCNGyEq-E3vehZmc6THDvPBDe8FoxFo5SBkOH8fudFR1LV4sf45FJHP1snTRPBiyiN3m_drFjlSVXppoUbd_wLj2KguykrF8Pp7t3OFtTUVRiU-TjV8Pt1Cq48We1vXIVEi1E6onEfdSlxtuTN4Ky1Ppi-RW2I_ozS8V5rtKX-1XdX-LXMH74upgTQGqOjFOQDY5r3SkKOI0ZKLGi-TpFdydef0aowRnvQO5fiPxSCuMY26SH_bJMweM63OMsLLuyH-57DmjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a56858395.mp4?token=eCDlJvolCAYktCcRKTFjpHgYbgz-KxfGXA5hLLs0LFArsbBzBB2r9azErmGNJKQCQmRdRZ56s794DOCNGyEq-E3vehZmc6THDvPBDe8FoxFo5SBkOH8fudFR1LV4sf45FJHP1snTRPBiyiN3m_drFjlSVXppoUbd_wLj2KguykrF8Pp7t3OFtTUVRiU-TjV8Pt1Cq48We1vXIVEi1E6onEfdSlxtuTN4Ky1Ppi-RW2I_ozS8V5rtKX-1XdX-LXMH74upgTQGqOjFOQDY5r3SkKOI0ZKLGi-TpFdydef0aowRnvQO5fiPxSCuMY26SH_bJMweM63OMsLLuyH-57DmjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دو ویدیو متفاوت و تامل برانگیز از کریستیانو رونالدو
🆚
لیونل مسی در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25182" target="_blank">📅 00:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25181">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOp6CtHwVHvZAOezZLVz2_XbY6QeUuh-zVyWismgQG79QYp5ifxh7vOULj3Iin_y9c_yKDNDjmCzA8WJBkGdnpPvPFF4anLXymmy7yAwODXUtdk_H3xyMI4pBRa1d7xVBkjoysuCSwWE6y0i1hEzis7sI-Wy7Ye9aOiQ-FZNsoKLgxiNAAxzCXx7w5FCw18ji3PG0jkPGzv641XaRzwww8PWvn0Wid9zH83ciZQR5_07XJ5uSAZpPNbp6A0bavEvtWgOpXC8TnOqwqpT5B46GfqXNslZ9saFLnq7OqU2GGbV044md-dSAE7ETesJv_Jcdl-hZ5NCAV6kT-ipD1SyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25181" target="_blank">📅 00:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25180">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXX1gagx65ajOwTlFa_7LmYlSY4K0LG_56_BXtqg4y1Fj3tjASNrvA5yG3RGJ0Mh454A2HPPbhuAIY7GL6T__uVkkWAabyFWnW4IvRYcp6SpSvejFzua6wxi99EZEhDB349aJzDQSP8Qi4S4gnuwU-Am93wDlSofs4Vh9ipD_CpQU2tdqYU22XdGI_XnWKkB05qY6OxA65NpSluh-fS-nakm6zJ53aAHDAGALOvdBvfAcFax1D85SLzM9IzmdMQp4zpQdNalsUdnbyxKgr8sRQ8rZTadJFzihkNAFLdjpUK0k5sc2TCqAX2N7aV8sb-2tckn4gNniIKKeZOnIjCvMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25180" target="_blank">📅 00:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25179">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggfCo6cSuJtrqR0I8PCCYo7lFycro6TM8wYWPr7DTErWZSUNErv-AS_AD3yhsTZZBn058VZHM5UFuJ5BvBv4bJPhxlCbKQQQ-21Y66M086vO5LlrRm78ZjpnfMxhHNs0ziGVx76xdWYdFDKdF-PXq7JI-maT1rSgkJhm1Iqh4GIR1rAIAMI5vSquHGy4x1V9aOtoT8BMJ9x8JayQGSaMfPyM5oN25Nj54KeHptmw58XiWv--YQC_4-5EW3Wx8UqEe58t91SMH7uLkWCI-UPggC8zCIetiTyEkdCsmf4v6Df7wnr8qBbal0MBX2fSl7wFvg5BvFrz2BNERUSaBkLWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای باور نکردنی باشگاه پرسپولیس: دراگان اسکوچیچ برای یک‌فصل سه میلیون دلار میخواست. حالا این رو داشته باشید بزودی اومد ایران رقمش با سند منتشر میکنیم اگه بیشتر از 1.2 میلیون دلار بود کانال رو پاک میکنیم. فعلا دارن باهم مذاکره میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25179" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25178">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYR8titTvL4Ibfdm3MSJAV47f2q36E6HobEo28I69x6w7E6R4vEKIl6AKC1XK7eCgWud0qrpvJrMZ-ibSmETzDt6FVkoi0pmPqr4-hXOaAnFB8CKqe-tul3BnWOFiqLgKcNh6GvOZsnV3ZtVDJB-eWnmneD4sJHaZS85jBMO3yNtS29nUznymm6gMnQDCZDIlqz1G0AkgIqWQx21RbP8RaLLk6pCDSLUbn0rBi6G29FVb-dxgxNo80doXlTL_5mxM5oSjmRNqx4ao-8XZmSndNFulLn7UYNrOxqjbE7H050THbC5MwKWDiu-UqzV6dqCuL2Kdrx6TatCv_DeoUeFPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25178" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25177">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtQLUrYamjyUn8Xul-BtSBIgwRmFXgt8BeZ1ySPxADo5AY8HsuJ6KBeteY3wJ90nfhhDO9zPsBJ2DaIo36o68CAictZxltMZYI72E-qu3dxYdDai4zFwurzlufkGCfKhQa-jEdT7aJmzgxeSpNwFMOS7C7Vxe09ndprOMfHhlVaN8I5m7_zTt1BxE_aQ8vQXUsLj6o9pctGqlCvsY5LLgJ7Vdg7vR14sJ0QqoIMNDVGklBBClNE3DeTSVEej5RAdluBiEKEtfV-r-6kAjdWGJITgeH5yqKFD3X6I3RBDexOSGwbq3YXvvZmZgI6-kO9DP1wH165cExjvjDQmVpBazQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25177" target="_blank">📅 00:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1vgZao1YvBPW1CGkRgcXXEsNPFUmeRYk0vPq9qJZOaxFssv8vSjq871TV8l1mNfFW5ISCN63FGhibwlnj98rMcMrXXiS7wO1J2559-PiGsnFZwlks9ShdEmicwn5KAYmeYi72ISPFgxXuT8k2g5CyfjZvZCs0cCnhaEC5ldqWpAA4fjelhoLMWpkw2dGMk95v6FcnxQRiw4aWpXJUg1EaA1Z0Io5kEZDb1OFZ1avITQeI2N_gct_3sWzeLwcbBygOJqbK3A401QLYdZKOlR5F095sOxchlRT1HI78zkmq1moCZkGwb7d7hGCkTzuL5SuyVYFtpXgq5jHkUTuaJ-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFSY4IamdapBlO78Yum4r27PvQ2n15YG7Vk3KCfjUd03tjeTL7tFHLE6l1HX6mbTrduEvYgh0gcpZcakpqMWI2tTCqTO3pqUaee1gQrydwMdE9KWjDflsX5xJYFduEpC1pXSvH53Um3YVrhfTgXfVg3G4oAhQVH8ydAMHBQ-s7AKZQhQgXmXqwYMFAuGc3TJaIFRzR74a9n5jDFs6I3muwdX-eBmDF-mgDqFd-DdVOiZniSLwca10ab7iCrMLx8CQfh4z2bINYmrdOUF8EUfgFn6QN6efYsw3ATvJRunPOOxT4p9wm07DjIvBeOK_hfwyrpsJoT_VQ3kxJXwCebWlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4Bk8CMbDkHmScHbA2qOsbUDysgAuUIGs6vpOU2pxBBztXy7Miv2nNVx180iRsmjt-doFLaQB-_WcHOxX4xJ7s3hmWZT71CyXH8AqedsfbWtJJt0s_J_ujJdjCz7V1upMPKW3Sq2rqJ2Pm77-1HFZUKB9Ro0U3J0jqFVFwWxYTLTgu0ytkZlTecJ3onpRkhW07wrk8oRDxK0B8tYOnC_ae7U2Z7WjH7V-cosdEeYQlO36PI4cyQ0sc2z1a3TkyjE-Ej_fCD6YCr3VI5dGlnFeMsDpTOmxfYPwYzd0OP7XAoRi4UQUbgUHec5Yj_OKxZTGXfk-wV68dRkyo7Jkw1K9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odvX8By756VBhOi6YIzdP_XTTgkPcVJ6RkrXYvlrDrr23Wva2wQAhHMYOuoshm8j_x4bVUZ-dhH6zIZogT4dakWAo6uO2k3MB9a0mH81kJ1wO8nEt8cT00dXI9PenAuq_3X9YHJHGqWGXsgvIXIQhMqg_nX52VmF1HTubIpjqU-WjXuI6YvpBz1W6xVMY4f4WML3p19a1IXr3uDAaqfAqDLAP3jmvh_Wdo-wGbATn9pHKew8Y84qFCyJLjiPdbgkctUkgMfJpJmr6AbTal8r7lY1doJ8rMgUo3DfWfVpyW3Je3THliejextwwnUQoyV9VcBAo0-1IS9Eo1cUzL0QUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdMhqoKrDZqrAw-xwilFm8klfN2wiympCUISRkOw3_emykIMc404g1BTgABOq6jOgkFlW15OdwP3G18tLeMh1UG9HlbMVz25hX7QU9jceQ3mCuXjD2mzyYWobsGAVm1tAX_LOluJrlPnLyca-sAxoJ7x0eCtumAp_K7x0fxXDxABSGJjj0-35pe1-KYTpdZsfTUMgl2LFRDCCNZhszqqj511GYGTfNPK5z5HQdtj-C9ojj4T6G28rFSxhm6l_YE5f9dG1SMhU46Vkjcbz5SkOOQZDOQbIn9OJTrneMJflg9x7pxNhH-N65mtxHnj2yWDEerrDk2uo_HhW3fuzeIrYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHyIOU6ykktdx4PL0CtfV1W1hoVE37anBCO9Pfcr2zCYZtIR1vmcfBBuekv5QRydSuv3YJ_2I-RvmpZ-Jd0fzFF3EDafKz4wWUq6j5qxdku2H-tu5DetU3nmrSEdjOHDFPDNSOlWZGhbD5brk-U0DO_BCYCTKKUn7tFGeU--l8_BHwNr6gumlcS3m0rRzYp0z4j70BlnexBxky_xDFvVNenD2wz3jZfjto2Vq2DLoOQEaItfh2JCi5Yhn_yf3Ikut8xfenPwdMegdAHv9PDCKT7OK8P89se4nkAdsz4xIoP7yTsuYg5wyj1NPuNmT_TXkolU913o-nlPQBdtynkCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRlJMzII7aS0NyvVMEoPQY7agNoZynWU1YXUDi6uWsYg48V5vPXlZ3hWYRJ9zZHP7ZympEF6W1VJdYgaKSCQ2Mo6QJCW-_BQUVF0ZJZN-lDc8zczgdhN8U2N6QmrAefAy4iWxX6tkQIF37Rj6LtMGZh5M6AnbGdUYoOIryrO7c6-zGrcmLq4eyZXYMefiIIU53qn3GqZdrmOTqEq2Yw9iKuNYlwcU_72aqYyxmGJnedm6gxg3llAygzdHiHg1erh1_BjyNZoPt2MBM2xLJAVe5vdJnjLbAVmeEE0uSNSI9YrphnjkU_C2h0t17GDmWj6pXTbvbdvdoTOGEAtfdbT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovSHtuyOyB4cfuEC4tT5pYGsjgkLb3brDcN3Ga2aBn689ZrWcm-__MaKz-pA093D8tPcT0hQNtP9p8PWb7yWn7Rdv1cDEqajPjTJbLlHUtQGu7sgTQsE6HW0e37MMTuBd9_7gR2HL4q9mAXgnX70WJvz25OkU9jI7JFdwy34OsbGMmtayZjgFOmm1t2PEYY5sVEbTSFQMa4BgkKpmb__HvJ32kp-xJGxKIBcBqqe8UlaV_G7tDJM7Wb54Z7UIQ0LyNUUFP2KOrlq7nr5u7DvGcgOXB3VK7ES46YtrkE4PRc5bi4ILqTCAWVirDfRlgVk84912W0C5Pd1gRdrzERTDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWYzy37_VGnfkUPF_MMDGK286ZSgNdO1S8JiKEUI7lRCuxNxFbQVCtKa-hVKBblyt7wMlY9VTmorxOlY9C5BN3EWjFM2pZCoiyz_L5xEE8-greeadQ2euzrWI4hG5C-zd1-a4qnnjUhDVySoR3lQfuS9lWvdR5Y3vJ1Wz_10X2JwfrH5Bve3V5-zy4LFCh9yNu5iPBTCNnP89pWMh3W1bBL4D-i_ezzvNGgTU1ZvWDVWV27yZpLyfHNATeHAH4LxD1I0u2ELY-Yk1U_UB5N9ROCv5tlB9N8sGRZprFZwCoEmnSVDPVUDtr4pygQm-zPM1aj0ea7e05_VS8_5sE3WAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTLBwRlCNzJSbKSVxD1IU_kzb5u-1I0rc0Ny1tMCZLR_d5dohF5T4i7wN0l2ljLKirX1u7JjUNKLsWtT-yL1_Ix2X3RQfvZuNT6O5uLmTWLcmwd56iYQ9BMqmyeuJ7Vgx6uJg-j1CQOYCOuf-uwXoF0PhUVzbO2fYyuev28Khdw2AZWiBE6yoWsqZycT1GqdZeMHFtErDPgmyDzDt89SazVCk7r-5vojEofsPrq3OXXKizb4-7sPwh131iocZORiNxwZDeyZfl8dYocuxLT75tJjftjQPd3_3Pt4DOxv8jY3XnJzjFpnLKBxnninazjeXMboYCzWaSeaTXoEaV816A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkyWvKyXZGJFyggSyABVkWNDNN_gGoF8AN7LcTDn6Azn7F8AEyhDRNfu3FF9wzvrKHt_uCF_nohBfjWPpnxxBOEGWmRlikzopM3vIhsOW3pkU4WWbEDwCNjt6bNkVOqZnFqtMjLUbyx9bd5lKwU8ApDs6R-qHfSFn_y1-BFc5fZgzEOgrn41mowddKWErtaywtdhDR3U8L_2lRVXQeW7BnbCReVrNx2_c_Isd69cYK0SicpL73qAmvkf9TnPurbmZG_Mn1s1Y71d2-lEX8nnEEFs8sCv0PvhJxZqKidFt64PySQjDN7ostIP4ql0tGTAZB8upEACclQ33kexLy0OJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpDvArr0blSNEZ9tq6wvOPv6TxcxFHPEyk72sHmPMA7z-UNKCoFjbdzv9Fm6xe4gvQoC_4-S6ZX4sA1ujT1-MMhSkTWSeyJH7sYM0BoTKFyQcEf9SEEGJ0673-7RkoODbkbL_3hD_OQaW6IPYCIxD_ZeHM5BjDJFVWQQxN_71dM4WAvDRlYGFd-J-_oJ6c0UwRhmSbBNA-aT8LyH0LmmAa6YMi_-f2smRVoYFk_CnXZxNXKaOVoLCB97splLB2csgTdlK0Qbxz2AxHZ75eC-MHx1IzPkaPfeECOR6j3wdf8cz7LqTrT_UhXfi8vVSvHs6iVYSKUWorj3TfHv-d8pFK14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=i-2_Acmx67A303wc1EzwGRGmngm2zKnKW2UbXiTmKu_pZUCZCfNkWVgyGuSljdWBcNpdQFOAOqUcIG9BuMKaPuqY5n4-FkoABKvwEdQlXiN1EILQ9GGMlxDOtEy2cVwubrHnMEBKQMuXjQU6uMmHi--1312quccgT1-5Dc8QZvZR14mrtWCRhpIgRurfoRNyhFNsGBCqi7ZehTHbVp-1AoN2YFPxtHkszssUBm2kk9LcoyKvy5dEn7yXZlVapmqb7WIATLvw8PleoU63MxnOmDA9srRAwzcZMm7KTtmYzjmcqn0htqJ6a23I8xP85fKczWeycD9Ebiixot0_N1CSpDvArr0blSNEZ9tq6wvOPv6TxcxFHPEyk72sHmPMA7z-UNKCoFjbdzv9Fm6xe4gvQoC_4-S6ZX4sA1ujT1-MMhSkTWSeyJH7sYM0BoTKFyQcEf9SEEGJ0673-7RkoODbkbL_3hD_OQaW6IPYCIxD_ZeHM5BjDJFVWQQxN_71dM4WAvDRlYGFd-J-_oJ6c0UwRhmSbBNA-aT8LyH0LmmAa6YMi_-f2smRVoYFk_CnXZxNXKaOVoLCB97splLB2csgTdlK0Qbxz2AxHZ75eC-MHx1IzPkaPfeECOR6j3wdf8cz7LqTrT_UhXfi8vVSvHs6iVYSKUWorj3TfHv-d8pFK14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfVdkb5RMhlVcY6vQqi_dcTYa-JmX6kqL7zSz-KUFOjTOTcfGNCJ5y8nUl2x1fqTFGVRtNI79Z1D7X5uX2InFNKrkCEQB5TQw7Rm4l-rXPOFZPuiNMavDcJg6KPOhg6ogruc4eg4jycUXdco-itEgRy7Q1CeDRO8Ar_AZLfz1uD-Y33C8SOJuEW20oZSKYND5ElP_Vn9Azo4W2SvmphW_qd0jwxbM6MV9G2KqnbXX_Rl87ahlcrQTpMdM7WpnFtqD5H1_fMuHZiStz0o6xKSWvT2HWEOfiIfHLKBbUYMIPHA5EO463nBvCjVrV-0wLtnluVr45cGjnQWtPKZaFA4NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxqJPiDzdSQmdaPEM6uiOcq2wXny98jLPNDwaxPM5JJ9JYgjtWivVMm4Zsi_IHvjMHyDpp6V-ZB0CTxLPEZC5uHl5kdDXhA60vOwP-IWBbUje_h7G91k-i1UEwrNhWbTxvQb0sIuIpMHm04gPmNKLBzWFvM73peR0nCJUwNFGUwS8pXY55kPpg4kQ7_jE9hARoPEgBEoyrJ3pwRqESs04-6FuVrmAQhmpA54D9_jp4WhbMuStPme2vLShNELgB0n-gGhC55Soj4VXqmHhAmNKgxqXB9tvFhwWC1go2oEcmHw9yPuMHcC5Xc69KrfNMEIUxwFWqUZejwgySVi_HwioQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBQsAn929pLAVApHRcWQboFKFc_q-VxCSH62GRkNhiXfskpBWDCPTPrUJBX35Blg2eX5_-KymrOJzvfF2p9MSn8C92LukONLrKPH5R4nfb9D_2my9jPQkff6jrplg3u8R49FzuUBNzXL2DFiVRgusyfHpPiJUXwGbLT6jOJITBD2ieKZBqtUhp3vyfYS6EA3zibivCPOcBmXULiKgt0lrhb7iDyqOSJYfPzsUU5zIOfw2If934XbWX5R-PqkRzuUNXJD46OVpkDLckxC7qLXNzG0Y9pWVZAInaEaImgcwLPM5oyijREUwwoQuvy14s3ChN_tZ6E0zkRiRac93gTbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=N7JbwXOFyx9Eb0_yhu5mcIithOGCsy7Ob-UK_GW79qbpbXa3_k0wsgpUNSWY5EmgMgfPk8Ev_gwvZsxF_TH1GaIxzzUQTKxDgRYk20NDRB6rljumRyJ9qVttdbTV_1HIPQ7wAOBTmRc15UgbZ5MRaajx6SoE8vH7-OX5Z081xKvG2B6zLYwrgI-eR7fR1b6uln78P5sDDic4dp9Rq7uBRbo3rQ9Z2kBU31C0jASxtTPG6Zr1vl3tXzRM1n1IBa2L_G-YlEfFLHaYuZbRmhyV-gzsBWbYNYdqPFY4sE7QI4SSnT03LzRC-_w-zPP_ktqvVBl0KKKbYHcUVvGJCtnToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=N7JbwXOFyx9Eb0_yhu5mcIithOGCsy7Ob-UK_GW79qbpbXa3_k0wsgpUNSWY5EmgMgfPk8Ev_gwvZsxF_TH1GaIxzzUQTKxDgRYk20NDRB6rljumRyJ9qVttdbTV_1HIPQ7wAOBTmRc15UgbZ5MRaajx6SoE8vH7-OX5Z081xKvG2B6zLYwrgI-eR7fR1b6uln78P5sDDic4dp9Rq7uBRbo3rQ9Z2kBU31C0jASxtTPG6Zr1vl3tXzRM1n1IBa2L_G-YlEfFLHaYuZbRmhyV-gzsBWbYNYdqPFY4sE7QI4SSnT03LzRC-_w-zPP_ktqvVBl0KKKbYHcUVvGJCtnToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=liQteunyCnWolI_QTP-frL1nVsxfxYFj3IzZ27A-56Og0zxe3JVdCC0IewhSbEPnrJudHxcm2N7a6ZBGXMALeu4fYYZ84TLCyzRT-752HVM2YRb_bXvR0trd8DdWB8JLQrRGaGRGOESKJO72iFhceU_9Awid_11uAfJeHR1TDiTqj5a3QsboSY-qpUdBU5L8LXmQTSCpjkYLaKXMY07l80I0NMluouU1Bp6Gvv2daqAySf7a1JtVg91H61ScZKxaFz34PuUQf4tONIkt4Gr-Ld17UmlopLBUHoy11Qg06mRgnjeoNM1eF00IWQ-7MPaY9ur-H9HvZhDFQDM1cfsRsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=liQteunyCnWolI_QTP-frL1nVsxfxYFj3IzZ27A-56Og0zxe3JVdCC0IewhSbEPnrJudHxcm2N7a6ZBGXMALeu4fYYZ84TLCyzRT-752HVM2YRb_bXvR0trd8DdWB8JLQrRGaGRGOESKJO72iFhceU_9Awid_11uAfJeHR1TDiTqj5a3QsboSY-qpUdBU5L8LXmQTSCpjkYLaKXMY07l80I0NMluouU1Bp6Gvv2daqAySf7a1JtVg91H61ScZKxaFz34PuUQf4tONIkt4Gr-Ld17UmlopLBUHoy11Qg06mRgnjeoNM1eF00IWQ-7MPaY9ur-H9HvZhDFQDM1cfsRsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cu2k0Andm_ApACEoyBdGArso2baVS41Gi4I4EOK8XCmzGZ5NG1549POsUi35W-HvQUBAE697JCU86D-6Yz4idXkH25EmaviXw8JdIDBE91mf90I-RY2GjV0luNwYu8pqdnDmL0nCOWah9-zfyXS9e6BfGiBQ_VroTNev-WAdHGU_HE5Y43OLLWsKfyEJ03iyVkVRCaOtO8krwdNJ6QPRX3pwQSC3ghhFCrQMoqSEwWTgjc2SmkJqXqAfyb_nUXT5gYP8h4k8S6VbUebxeoHO09zFxpkym8O9Xj_vQbWMsj0T1np3UJ6WMnDUJB4LsDOlAvCRwtwGf6RQwvK0X1bRtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b5aRJTQ6k-pBLcbH4CJquWcnsvE0oPWaa290_6oQv1BJ0zoBwMwpcIvZMBsB0vbWCKQNbEZciGaSQ6cGnmGF_vnxy8e6pKdLqMnN_YzA0S2cjQhpEytqe7Q9V-HY1s0gOXHHQaz9J3QF-i6cGvpd6PU0R3XPc4fmjzwzg4ae9xs72Om5Gr18YamGq4HlP1sBDggwNJsLdIMoNbSt4kjbd3RpKUJs8oKhpGTG4vesKfKmI8wGGFjumIb59wuFynFb4YbMaWVRyUHbr6YHtrKp3d2i25MCNwfz5hHygDmW4TQKrU_Q80i6idSbt6seKZoAk8MVvEb0pOGDR2uuYaS3oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC-MoLCxmxBb1roVKoAvjKzV6IM48CYmKnJUhWAss5dXTcGle83i7mfgBUgLnt_3pYs8H-cFrUUtHoUOVRzw0Verhvl9csBS6tIoShwOsLX-9lpdAQ4F0zZBamHigIGXeJN8FeJxk6h9n12TRyCu8KHd4oVPvpHmoMS03VxZJ2lvDmv_X6fU0dsYHUbDqtoSssqrx3at1rn77uJcu2o_2ttYNIPWjflVkCqxTotzeRlzDho3qXNDJDf1D2e01hh7u9M0z4zWUSSR-KshG07yFOG5qWJENhuHTD-TPiy4urrGopkU2jTLXZPmiGje0Y-oAO-m_6dzdBXWUTt0j75G-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxjg1xNRWjIE0jpWygHEUrftM_jn7T81QN3IN_qH5LpArr8qFg00BRM15lwlEMqf6TAgKtZGMAgmpcRLPfEEBsyefIdU5E-al99YxIDubXBV-V8TZ_IaPc7JevSMhphEIlF3je6O9V2Z8h_i-__tskMMEtJxEnUH4LWlfxfI1rZRmmJeEwZW-nT2NKj8cBI2qcsz_YaXdRk8Iv1B4zoPOYODKEqEw6qs2vYvS_f6COwbTkKD8jA1-D54MR42sR5QoMW1fNUG_54iX3bco6rsZrYlIJrQQOMxSdxpYGgVmE17AsdDwN4j4NsL6BdjXRzqx2nI7e3TA4jURXWR3q-8zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0zQE0mYTQV2Zeo_O8deCxe9Z4T9ICYcB3zXgSVQeMFLCiD24vkr1Bd65Hnw2XIlfnkPBP-9x0pGV7pWEIEG5ERDAOLmVEYzRbHwZjSbu6tEr0S9VJU2teRWrDWoro6MyGEBR97D8iez-99qGqtqRNcQyhrD7EQQ6dQZkPLZ8MjczMfgREH5ShIxBy-72oOtVq7fRFhg-nu5Ko9De-FofZa9iH_9_F-EAv5tftrHVynHRFnkv19fZRDGI0g_4Dhf5vhI7A2-aGsdjczr4ojOrN0mgvAq5WBSb10LtGkT7-c12P9k5ZOyjzhak02fP51SnqyZ8dYePBdO2rkBa3T2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WamnyQzgP3CXOuZs0oLiGLWeJl2AoSbRYLs-kn82HytmBokWlmjdV_XJguzyBXrGfFs-2wyWE3qqLb6x5SmTfrIKIxbdJ7aV_tH-hsEuZXJgNa23Y6L7im_2m5enK3Ws2lI1mexABVIkPJb6S1387qqspJdSYWy4D6pS5dHGRzPMK5Lg8goXglzRZrOOrX-uvCR87d7Qeb9nt0GCHg4lDIqQLJTDzVLMhNGyWgx3GE7YziHUEnsQqFnmInlniSOdkWbg0gbhn3YZQnkqYVdLik_0JaI-TIsgTu7ZADAYbGRmalw5xl9aapiOOLBILtxrT8jWiWrlSbarcm-FbOsnag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRn-7k-t3Qfhb_-pY9rTme_2Ayr7UV5BouEI_J8jOkoBZ1sdqt0JgEpMROYm55uHRPpijlqQRg9N9nY7NmfoHc6AStQ0fMTrjbcpFmWNOf4fmjC2QT2x2YCrl6Mafd1F1YHBsIHANztKtIzHeU0QmVKBye1M1pAMHLOQNbH0SIqjMUnhkHVcX70FRnT_BKXXk85R5TqEoL0W4PmjnqWWX30rzVoBu7QRCLcauyIsspi0ci5Iwmy4HcsNxfonVsFktnUypi-Nnc7-RKXi4JuNLjuqoBalVm6jr5E8LD-sqt3_3ocPz5krjGZPgC4aQ594OcIO11JObvYiWBm8HJUjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVR5zQq7AHXlKmIQJ65CcFuDcfHMNyzmlMnMUk6GgxfCZNajY6dMp_PjL3sng-LNdKH7OAlUjx12sbsCe2uSLPbrn05PUOtQ6ZAbJmPR8tmm5qe1hUesPnnqWr1SW3dS9mZsH3zxN3F0uthFsh9Y0pDsnpYbpbiZ2Pod-NP5ggfRb1mDMOSm3t65BEtxDplJ4dBEIjV2jMaw1OOz4-I64OosasCWkkjAWagj79YRlpfFdZLBUTPhKg1tjf6daX44vbY488gs9pA3bUrs8f9Kac9DJ486JiIyYirqsQxa3QuCT19tPEw1rlkFH-rJwpRDqqeceR6e_oyCkUH_LqtA3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0d21oNout_tRiOeJJqNS2UJbymsrKc6ubFMpEtlZNBRDin0lAHmTNRyX6iNdGwgCD3NyJXrosbqf6k0iEYMQ6WewftTsKAoMsd3ED00ZDBw-eCF3uY4VtnY2dJo52kaJmyP-pQgvuEJOgMp0aZ11XkaxlyOl9pChikqszw1SkWnDCB97F1tjLUN5hIPRrziTocUK-XH3udD8sGlZ7YwyvMyLBS3wM4lGxoqSZhH7Rj87LdnOS4smboKujo8i7IaKKVsIgG6vCtwrZzsPCvuRr0skD3eKP8TeRv3W0qCgGWHLKTHjKO3hFfE33YWAAIBuPM1afK48LQaIEBeAjXXbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AlCOwHMDVzeHzla6dsyt2P8vVb5NFcBYDmL1rBtMHrpeURgJ-57x27Gc7ymRN2E7oh3dc0MmBs8ICoTuteSm_BHs111colWOsfklYK6fkq33rg96TevlmungY10SUy2Tjx4j7cJUR9XHNP7hLU1z-_SudzsuFsXjC0csKfK6pyZ6e_vvbiO84uV6klR8EEpIkwF4izpGKaVs6OVbd3RW1kskqZPQJM2Dv_dTiNOqKKRc1FF_sMWQg-WqVlB4G-bzcgN1P8HwSLpActOPjdQFR_QFJKEh79LEY1Fm8sSvLCGTTHx1CvwoR7kTOqLHJ9YCd1nzNjRFGvKohHXxaBidaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7mwRfPLUdPCdENB6v-b7pf6Uc7QNJqXCZm_sZV3PG3Hf4LYc4MPSWXK2hW7wH6VpH1b31kCBYf5TxzImEr8vI3vJgGwereIbxHJQcDkclog5vXTtTONOlqq6FjG8nkfo43xssozqHWSHtTWHR6iZ-ZoYpheA5KcYPWYAB3cTCS6WYKF1NL9QvNclQfTzqq2d39TN3WKBIgTGNivNhv1xlYrrm7bS34k7CIju254Jisw_zeB4EgvmlyWeZh96l3YP8S_BJ9Z90spponGOaZTGP_ycs_Z6rTCwx6b_l8uNIF5vFlPsCUdwJ_3zmR-GjBYMZ6lmBW_y66RW5OUzjZK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsqQfUXQ84Fng2fEdVNis5Pn1839tti6HYrPXBAUnaMTLagE_Zo-KJauguQC3rscGOp4R9uMqYQLBwVnaGHaENpZaHfIoMv2UXzpOLjDfDTkEEQWgEM2_gN3zqItJkQDSw6Bm_0CYllLiSE3eSNKszmQ59VDjR62YZafbLkTSfU6ATK4jYHUQmhbyXHfNQ9kQdW5J-kpRko1bmZdQtorzYT83xQT_iY_WMBPE-pA1C3G8X7DcDXqEvUVJgVvd_N6J4WRDnbBfGCCw_HmL9ZhmvIKjSx-S8ziBLyJcv6TKTV6q9kl48_wbaGFy4z6auKNMfs91h4i6xAGj2wCVA2kTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkJm2Pc-4Of1YCFcX_EEgjPefxiRIXSxUDOjTkqT70H88rr7-OrMvWqyu9URssXfO6FwrbeYjj8VbBMnTQo61jb9QCnejvjtvXqDF6FCxfY_wwFuSpOMF5AA2EqPjLmcKn81Pds0_KzLRJAeSQkEyoWcZcnol2mKyGrAhYmdC5vgrUNOU7Q3UKkG40RPMEOFVObrm3z8Cd8obzk4CJZYcnQv6WeRuxwnmSiLoixbPHmXQQqaM6Hy66LknY6z4wnFBdSvLBiJtmQDJyEzq4UZXxndz7AV6dFzfQ-5bAx1b-otNrjXln8mFd_JEhne2c2cPhs-qL3nvHHbO6c6VAvDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpDxlqoqYp8SMAtbCTJsFdjFXKvse1Ww_oESCLyotfwnfNSr7AIaZ_6SEfQ7-KE75PH1A3zUVsXwOKyklr1bNRyWO-idZgby2-B73JWljyNQoPmz3PM_AZbDVYsfRbh6EdKcMJwX-McUX46ylDroTg_sMchpvFyVBIiv6DBIQyV_3et2vKIJI2mYAj8oerq-MF8NSuUXeTH-alh273gwC6r9D2yz7-r9BlZ1thIEyZL-M9ff62BoUcc7wopFUS6Z-6YdDETkdaztt0rQHPcLg4LMgf1ZDvceDQ6Yomn1qgFybi2JfglYsCyFx8iqRvJTnz4cJhz97ddS9rbVqLFiVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCg44guMIyLFnyoWeLP5nRhgeIR_6I4LGtrVZ0h3vk8bCWc0GcsTAX93lN4sR2STVVDwol0dSiIjImgc_6jjfM16Tl1yVD8izWQR5fxeyGN3qSxwKHvMzGGMmsffDtf35yU6wK9Ti5TA-lkVU2EJV8SuS752fPAliRGjACstB_RVvUhbygfFyI0brrhcKTgovHIftzOfZ5-mLpEjeDw2aK1ddmW_whBZ2uFLunnWV4nY-kIjdLTs4KEb0bV4hBEVOze1xSl-ndavEYYh1uY19RLtqBVZ5hypp1Js8Liue0SFRwMJKZq-I1o-FRn9FPFJuQTj9TE0yUn7-wJrgWpaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BATAnUL-MaUcddPaliYf_YlxlQf5XwuzAq3Cv5_yTEeJyKB579p59CZOWoHb9fLHTMODK0NQrJ_47s8pAcPcW3v1BWus4s0csVJPZca8fWx5Ub6HMnuLUKtnSXzN-oS8xnCRZ1xn05JOq3nvDY6qr-1uz7WfD5JN2mqhGFHoDwy2i1KmuXoU0KVVaI9wcP6vjNPgTivaHvoxhCpLDRVj3AV9Vmjl2nXAJfoIrgvxb1X4IwidFHRjeaErGH7OJeKorcBaluqS6bOq_hd0JkM-fVnUVOVhoqTQmdyWZ9VhhaHsI70_nKkthS8Wo7cN3U3E0YCaIynHmGrbhv1jfdA3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e52U4d33zQqvgrqByUeqGHEiyw8szEzOof07px9VT4uItN406gPsPI42Etrx2JeGg0GSP9fCigQH2GKlNbx2e6ZTPolr8U-LBGAlDIYATDOv7YEbSqxj6GpWly_5kKXuyqthQUT-L_U4zIeP9SK54gVZoz99GyNCQ5XbRscgRdHJwDLjhkU7552KbAblHCAzK5kPdjpjgFs_hGeH9LPT8Edt-9agciO08gxvol9NysMZUsTQ8ndrSwbnaOM9qzQy5g3lvUudEg1JyO5KjTVvyK6faOjPIorlxnw9qCva_fkifsBo3giBuY7X18NC72dMs_XlQGkbmGkBmA8Kb6YrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzlaLBkjk5REkmiND4FPULPFokPaFyyINJjyNl8r-nBOiGa0iBuFBAShSyldRqgIzfp-qDS1J9ItWkl8lO91ESdvldnZDk9H7lE_Qlo2Ym7C-1gC5cx60csBODKDUb5bhnI2bYvUic60mEC33p8M0ycP6uRzzx-Sz_XeGgNW7XA7COb99PCK47UvRLsSh4lxAp6tws-AFA_GK-fgRFm8JFdQIbYVNbUcWYgiKf1FtYrsCyfLY5jehkZIaRH-Ip59RwBMtLRa32KwTI72ytYJRgFsrZStvPKXzkeGwvfA21O4-cegKQpf0J3hwlYzvzcuTF2xPIb6x6aaf8fB7h06xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TPQ5RokOXfdAPXQhwVPFtrw-zZDzSO1L-Y5TBy831bc6KMRpLTBGY1LM66KDaXsSxG-0G_QtoRlWh534SeORSY7mvDxK9y4gvWFtchNkV23i5w_uPe3lNEO9S45B29vEcWhNSruxa8OqxfSPnLzRQIzS7cMealnHVMLcoAFpIScHLclt0-xduJqBOi8E-No3lJUAKgcVDFRenFZh285Lc-7yTALG9PgMw9nTddJd6GntclfEAuVHkVgxiycs5H2Am38EomSlMtXCl6jDmlD9G-oloKCmIyU7TyIyK_8cqGG5ZPWOWoMGr3BWWgxf9nrxWURayoXffCi9GsnX9ZUDfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaWY_xzex8qKCFCgE2u1sEGUBfzqCDX6eA2qacm02rG2dtkxkjm-R-WAIefMWeV9lN38qOToZc5y9F6HvCFD6AuvhyuxYup4muBIG2Xe_UT0l88tJ9IG_SDlZ1ywcqmdOp_kPLoODpHP1P1ALDAVAib_K70NyZYti_9ge6Kqx7M3UMPj6-k-1_ImHIC_3YL-yYs4HaEyu0mPTgKkb2oHCylBNE24W4FiQlS79VX1EupaXvuXxK-I7j-QFJypjM7g9T-xCNINYfzKH5KIjUWxOI1ABobEQfBWTIoGDFXYB5Bx0c1qoVVh1_MPTl9f3bJ2ybmSaKq8CeSNWmdZ93orjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
