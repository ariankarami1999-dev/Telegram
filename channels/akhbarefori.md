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
<img src="https://cdn4.telesco.pe/file/eoeNUCF0Uvh3RCp8aQpxbBrAIPMFCLpXN8oZ1WYxw916wnxdxdNUc573-oOesFzKZ4hoQiYb34mm7mYypWOL8e4kap6xSkkqYSIz-GPk3mZ6BlEEd5gd0uERoycWGVe1K5Pai4YkTT38LWR490jXOuorxj0UxVC5-iB6hfFjnYJLPcmwzngT-AMCObtmDYY4gtggwIOWZNwlWHlG8rwH_csz8ZzLAWCVctzkBbEYnf5f2yB-XTyBFQVilG7QilJ15GkqaaZk8Q4b2PxxvEsqHJyQGxWxJLNP72dEOfyhjWtohOD-HAEJqFj-YVMVrVSBgJnCz9iZmyIqi50u90dR5A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.34M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 11:38:34</div>
<hr>

<div class="tg-post" id="msg-693087">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
پروازهای ایران به چین، ویتنام و مالزی همچنان برقرار است و ایرلاین‌های ایرانی برای راه‌اندازی مسیرهای جدید هوایی مذاکره می‌کنند
/ فارس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/693087" target="_blank">📅 11:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693085">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
وال‌استریت ژورنال: ترامپ به توافق با ایران بدبین است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/akhbarefori/693085" target="_blank">📅 11:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693084">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89aad4192f.mp4?token=ZQ0k0x7YdXYEN4SBXO1us-nHWwWELsZMOK6Vw114PNWStKtsd5RU-HswiRKbKfGdHuuZLXep_5ddKQBh4Du6cEqPVeIiS6PcnM6LlkG1-rv7PhxMHrXVxy6u7aDweAWjNg3KiXdsHuNMXj6unN3odMteG70NcX439Z5SLfL2HQLmIH2UQXUA37DdBLpS8gn5MO6uzNq_f6B2WbXEm_SyRVyE6ANgorHfBiilsMDfOOuDG4bf4R7p5fheM4NNY7AoU9JQ1VQm8t39FysUQsq_CtTESD3kwfjZytYwiPoMWi77EnXIUNoDJFqMweFcDD0Pss9tRjGYm3BGqDRbvoFrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89aad4192f.mp4?token=ZQ0k0x7YdXYEN4SBXO1us-nHWwWELsZMOK6Vw114PNWStKtsd5RU-HswiRKbKfGdHuuZLXep_5ddKQBh4Du6cEqPVeIiS6PcnM6LlkG1-rv7PhxMHrXVxy6u7aDweAWjNg3KiXdsHuNMXj6unN3odMteG70NcX439Z5SLfL2HQLmIH2UQXUA37DdBLpS8gn5MO6uzNq_f6B2WbXEm_SyRVyE6ANgorHfBiilsMDfOOuDG4bf4R7p5fheM4NNY7AoU9JQ1VQm8t39FysUQsq_CtTESD3kwfjZytYwiPoMWi77EnXIUNoDJFqMweFcDD0Pss9tRjGYm3BGqDRbvoFrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هولناک از لحظه انفجار مواد آتش‌بازی در خودرویی در مکزیک
💥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/akhbarefori/693084" target="_blank">📅 11:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693083">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07403de48.mp4?token=I25jpzkSgjfFWZgrzRBzaYB6YZltAvJzKWWqY7Wjkc_fO8xOCtSrjyuZH3h_ji1xwc_lLt-aTL3FWM1EyxEQN2jfeApWHUUqrigo8Mk_ze_D_DNEM7ENBwBzUy8VH2LiIiFkmerUvK3kjgi_blpDGoTBdY9gier_rITafxqewr9aR1j9QFVdCmoQk5gDDyYTUaZKIwRO5nENyh_tIWFWrURPczcedk-xxwexyGMhWTzgH_9LxWJ4lXx8IIsc8NPVRjjAUSIcF6FkEKhSUCt_1l8ULjXCZtyWiFC7Yjo8khQhKdDgvKp3kRexLcdPV91BwecBpwpudj1WOFLaFvufKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07403de48.mp4?token=I25jpzkSgjfFWZgrzRBzaYB6YZltAvJzKWWqY7Wjkc_fO8xOCtSrjyuZH3h_ji1xwc_lLt-aTL3FWM1EyxEQN2jfeApWHUUqrigo8Mk_ze_D_DNEM7ENBwBzUy8VH2LiIiFkmerUvK3kjgi_blpDGoTBdY9gier_rITafxqewr9aR1j9QFVdCmoQk5gDDyYTUaZKIwRO5nENyh_tIWFWrURPczcedk-xxwexyGMhWTzgH_9LxWJ4lXx8IIsc8NPVRjjAUSIcF6FkEKhSUCt_1l8ULjXCZtyWiFC7Yjo8khQhKdDgvKp3kRexLcdPV91BwecBpwpudj1WOFLaFvufKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار فرمانده سنتکام از پاسخ به سوال خبرنگار در مورد میناب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/693083" target="_blank">📅 11:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693082">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نیویورک‌تایمز: عربستان سعودی ممکن است در حال حرکت به سوی ساخت سلاح هسته‌ای باشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/693082" target="_blank">📅 11:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693081">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454c9358d8.mp4?token=Im6O3tBDghKrR8rQY1D8zjtEurS1JHfn_YHaxoMKO6B1NURhWhUuUYhDkEvP6bY9abKgoXhbJteU9Ehtb3NKpx51pJ4yRGRCVWTIIKU7J2BP1yUa2BjxsGmlfyYnQ67NPjfPcsEv_7ppbiKJ2787RZgNc8cyQ6g-E3LOXU5A4qOtr9T2KwbTaEY_AxV2uhnEmknAJipEzrP66JgFT_12_LudNJgdSj60uX97zSs-OGEb_LrzPQZj0h3Wm6rzs-pLUBJ7LUQQ0XdTDydZwzweVB9A7O1WQKOura9dHhr64vM2wIdiRXydO6SVhUe1a7j4WExCXyeWPmsJZL2zWuyyPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454c9358d8.mp4?token=Im6O3tBDghKrR8rQY1D8zjtEurS1JHfn_YHaxoMKO6B1NURhWhUuUYhDkEvP6bY9abKgoXhbJteU9Ehtb3NKpx51pJ4yRGRCVWTIIKU7J2BP1yUa2BjxsGmlfyYnQ67NPjfPcsEv_7ppbiKJ2787RZgNc8cyQ6g-E3LOXU5A4qOtr9T2KwbTaEY_AxV2uhnEmknAJipEzrP66JgFT_12_LudNJgdSj60uX97zSs-OGEb_LrzPQZj0h3Wm6rzs-pLUBJ7LUQQ0XdTDydZwzweVB9A7O1WQKOura9dHhr64vM2wIdiRXydO6SVhUe1a7j4WExCXyeWPmsJZL2zWuyyPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: هیچ ضمانتی وجود ندارد که آمریکا و اسرائیل دست از ترورها بردارند/ آمریکا و اسرائیل هر کس که دلشان می‌خواهد ترور می‌کنند، بعد می‌گویند او تروریست بود/ دانش‌آموزان، دانشمندان و رهبر ما تروریست بودند؟
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/akhbarefori/693081" target="_blank">📅 11:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693071">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsBFCH0QTUIGVV1RN1VnLmIZvZmAucHzfa20c-sZqBlaLB-luRufEFtGQoU7AxCdavq_n47Ht7405KX5aPaaHFBBR5MDoDk-H1jFL48tjqw98Vbn6_P5YCs9ezRg5VHXcrkZ1I2j1wA2qy1EYwS-qspMbw-GjpLcKQXclmUPvyN5_f0BLg_OlzrZeedbC0oenJ5qVAMfs2Jzcyna9_EqiAkdhd4N9Nb0wI443zgKr_XJM7qzBzrH2oEGsAdGfEQrezIcwYdpY7nhBT69ZIO2RD1sqHIZNWwlCasCYdQaDZhm_L_1TtVhW7q29kMA27Jb_KS4k_exxAUdSyUoGpBZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yul5vecnKtmLAFPNo-Mtr0u6uUD7j5UgAdWXa6szwHBOGZK__ZWw9iHHzA8lUngiN8zQVTIkZDSVmyquwXlGzHTpX5NGds4qapZgQJiSDHxChx0DqgLebP2yIoPpgJOr6EPk0ZJa3FhpguD_Ueh9o1DtNErg3ixK2Ej0odFJTqCT9WRSD36YbIvgmx_fW-V-YyEEwx0hXHj02Tv4_86zmoRaMLEKvMkn39wFagoW8qxs-wK1GlUxNaq20fRYtJ75wfF1xPcZK-vYPJCz_xgq5DdFKpmGvQpee4Ub6O_W4tw9nn0GQcpPK5oz1J2Jd-xjPisOSvDwdFZFXUyy7JKNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCPrn3cVntozPfrOlCubZ7WxWdfexWXr37mxNRXCszSFiIkr9Nzi6MlP5zN94ssgazUDIJMbKYTyUEVpq080wZ3cTDad0VLrBpWEMtG2nhbE7QS5iVBmwBO7Z7dqcWZ1xvQhYGUuhjLM3Z2yu1HuKtMdPMCPntq_gqGCORJBdSB6AihEVnn7KLerCN8sJw6tjPMsE9wxizfN2j3aD5FPQdP6eAnOzeBFl3-LoWEzElYJu38FxBeILFNuMkEO7rVW10lI5VJUL6dXN0MNrVP_GFFtag9E6U2psiN33QBFFkrEa94-wANn3Tukc76Ofeh35yRaIiomLscjbSqmgz7zDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4z5hVNb6J1IoSyMaUd9IS_z7mxcxBG1ykkhBOw_wgYmfGeezmJ2r_EiEYujoVSiKVsw8LwJtbp0zmm3x31EV7eLtctQVnu8t-lew8j2e0KgMk8VzukTp-lO7YxFItDZjknjFEc0uK7cx5uA5iLryZ-HPNxGwfQ0OjL7VnqTURf4lya9uOG1gqdtS9mpk8oZGzdRzoKEKo-V0O6xuAlHLepej_3EwwoNPDWsuABrwGTJl2aDrcL7Q-RjLRyrtcjaInQH_2aN9yq3YrSwk8kMqDN-k4EZ2aYTFJ8qj77edf5sSpM83cBLNiNxKhi7nHYe_YQHHvh_rToz20WxYFiWcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M_hcp9shdoKGqh_vQjcDYyFHqZor6kRl5Mju3htsPz4oyJR9iGcp5pPkRrbHOWT7qwW3suHSeie7LblztqSuJPWjTL3Yb2SR_H6jXjPvNGphticfuBokNZNAd3yovcvVh42RNoF1ylK5b4BthyPCzEYpFCrZfCMSLS-Xk_4JRamqOv1T_8ztsA_B1zC_xjQ9gOF8a182me1zGCtcYhecLG_eB00HBZNRwRGzBEl4Df2q-lLxEehEAV8WNHUzQZy8DPMAqMNxlcoDlKtrOJIR60jJuE5qGgxIyVciaUSzZAtF9FB9_nJ9RsMYoxJuX8xEJ_ESQjXchZnt7JMtWNWD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IEc4sNiRbL_vV_RVEY6aHJWWzkW1GwhxtWxMLCnFDoDt-660LXf1Qyw2MuknbAufxkN0H4mbAdxzv9ovTtIekvg-WPE3WmW3kc2cLKoAfX9zdnChBICMGGcuONgcp5oXcoUUsTER1kCjIH5JIC4ecyiUfEzavt9xaGgFV2EnbD-eVMlw--_9AdfHfgpZlG3XNsD7RwgQhupRI2PgQ2ta6obm0EPZv-JtJdiMF1Sf4yNznk6_tBkdEkXGeefP43k75RbrDsRbcnfOraMOJ8nh0kuXDN_waUJhBXljT5-ptmvIlM44HVpw1FqWRNB2QTOI5MJn25AFUWSRP9oTzoKe3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnyisHGpDSoqDUhOSTlJNKHrdA6E0kFAdnp8L_y6IC7yYJs68RKxQQuf6dTac9H_jtw5lgBj2scltsTIYJOrl67_gIbhstGLaABH9DneaKE4dAGsjdEN86-OzRMHaJMJstzTi0ZYacKxBdu18B0LDnMQrf40LKOtUYLWKD6ACvr48wHqkhiRsWalR7zgJ1xAGkH4U5SXJ7SW2uC9aE9McA6YpCIN4gRskPCxwXZF5ZLR5tGprHfwcREfKhrJ7J64Fo8bFiaNH9odL1gHwlExLQSRWmTW5y3QQHs61dSWT7QZ5aOQJ3eg3z8V8Vbrz15pNo6HcZURpLfOgCr0_g8wRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMSo6xT9-vzW-J4vgS4wlNgvC-Vthkc0LyW661uRIqB_NYditYCfriYWE74aulr6XxYrQPrgdSvYL0jSp76rM6og1RJBMQJ5d0EfeVyF1eFIESn67cSEaNQe8juBt5E7_D9AoMuT3brFzoXoivLXi0XTJEwQtrM4IDVhCnq9mkJsfEY4HAiZ3qvodKCne4q1OzlQQAZRTpGjfacPdImQrUp5bAL6sK_nO3P9Ogu5xSAtL9tXGhMkxjCo7WnYjVgf6h6Ly0SpSsa1UecajHHAioReIgc9Mzh3kgOPAG-VrXqnXK8fx_IVHQZkJTIDTrj1Rce1NtbicUr7YvLkoGL1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VTrMFckhNSRbIwxOtVf2OMSp7uRZY62ooPv7Pv4pCGATl0QDJddvvhiI8rPJBE_zZjXar-wgZY9o6VbL7Mio8gKM_tkkPRw_agh-LtGyP9r5Yfmc4JR47rM09X1_uYF8IHb2JKooVKxayZE5SQaqk5dkpDZV_5-kZNWhv-KFQvP8-L77W7pzt1MYEEmRuGe2lfw1uYXK4j1roDX7kK-dfMV4J9BrDY2ZVODfGa2xzA__yg7jnyLOtKt2-mzYLWiDFp6lD1-AxqX97rbBR3lu2HtRrtTXvuATPViMWV0yxHgJL-sxG2QbzGJqQbDzYduJNt0VTUIL38UWDWRchvdtFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5aok55hOVgRc7KHW-zoZLe2bfn2kHrCehLy2Gd_LDTFxkEVqw_aStTrYIsOSLDI_7AzdP7qIjX_f6ugCe7l_ee7pE4567tA333RLdMPHW2R-h3SXOSC9V7eX42b047q7V9wb228OWNaYph-MiDznqdGP3PkcoUyv2v9ZVNZFy8sqqC8TXbbgU7ghnCVbUiQMjPUXdre1Ni-AyaM3eCLPSN9QTeKn84_5e_vneGL7MHkOEsKeNyswDpEn5BeiXc7TYIm3okmwR6UBEm1dRWMpgr3JU7X4NoMMqfCNr5zsHgImFtScQag1hN4wrJXLHH5oBrJidv1YD8b8qVGAXqUzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حماسه‌سازی از جنس امید؛ وقتی مهندسان و راهداران ایرانی، رویای دشمن را خاکستر کردند
🔹
دشمن به شریان‌های حیاتی و زیرساخت‌های جاده‌ای جنوب هجوم آورد تا با فرو ریختنِ پل‌ها و زخمی کردن تن جاده‌ها، نبض جابه‌جایی کالا در کشور از تپش بایستد.
🔹
پل‌ها را نشانه گرفت در حالی که اراده‌ ما را ندید، بتن و فولاد را ویران کرد، اما غیرت سازندگانِ این مرز و بوم را ندید.
🔹
امروز هرمزگان شاهرگ یک رستاخیز مهندسی است، چرا که در کمتر از ۵۵ روز هشت دستگاه پل آسیب‌دیده بهتر از گذشته بازسازی شد تا به نماد شکست استراتژی تحقیر دشمن تبدیل شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/693071" target="_blank">📅 11:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693069">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4395e833.mp4?token=obw1GOofAhtEH7FJ0y9kHlMe9FLzAf80LN6W5-5Ur6rb29mI58JHHEcgwqvmZBeS0nGNiY-gdHN0wkgJIc_-v5I6UnZ_5NhpK38PfTC6jXu2dlqZ8TFQs9CUpvdbB3tcUhqLiXhDvQz8YaG-mHge-I--2q_eHC68cOz4XkQlZMTW6KPN66pt2JuGudmOeWOOZy9Jfxf0jVS9P-sw_thZ4fgVB0ZwG9llDjNZsbP_r7E8aAq8g2DSCTxuty3SaLzCyMTgcSfKQpGeJt_Ca5V1tC3zNoYDU5HYP_RS4lP3OH5GBtW5dojq5cnURTBBUra7wkYZ_Iz1Mn1UG3Mz0d6MGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4395e833.mp4?token=obw1GOofAhtEH7FJ0y9kHlMe9FLzAf80LN6W5-5Ur6rb29mI58JHHEcgwqvmZBeS0nGNiY-gdHN0wkgJIc_-v5I6UnZ_5NhpK38PfTC6jXu2dlqZ8TFQs9CUpvdbB3tcUhqLiXhDvQz8YaG-mHge-I--2q_eHC68cOz4XkQlZMTW6KPN66pt2JuGudmOeWOOZy9Jfxf0jVS9P-sw_thZ4fgVB0ZwG9llDjNZsbP_r7E8aAq8g2DSCTxuty3SaLzCyMTgcSfKQpGeJt_Ca5V1tC3zNoYDU5HYP_RS4lP3OH5GBtW5dojq5cnURTBBUra7wkYZ_Iz1Mn1UG3Mz0d6MGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باید جو بی‌اعتمادی موجود بین ایران و آمریکا شکسته شود و به آنچه نوشته‌ایم پایبند باشیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/693069" target="_blank">📅 10:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693067">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تصاویر منتسب به مشاهده مخزن سوخت یک جنگنده آمریکایی-اسرائیلی در غرب کشور منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/akhbarefori/693067" target="_blank">📅 10:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693066">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
پزشکیان: آمریکا اگر یک ماه صبر می‌کرد تنگه هرمز باز می‌شد/ تعجیل آمریکایی‌ها کار را سخت کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/693066" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693065">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543dcdc581.mp4?token=Qr-GbGw5k4G6Orpo00jXKVfD7v2Sxzto_TbQhYON37K3T0GRwYgYL9qLJL8P35IaD-uObBJHL-LLm8-ofmVAqZmQjeh-QzSOc-A20VeBrYFQdLbR_Ma8BotzOlg9OqIfnTscYw4UObpVKQPRHx1HWkhomdNz_g4ttqY8w_Mz9dK66WOELdLdV9x8Sht5D6FZj84fbGDPzLqesPe_fNmsn9fLo7C2tXbPxrvnYCAk6SryUDmDx9vU9W6gphF3M3CUDJ9QL2mFEtc39urwuNh34FISr0hekCyF4hGp8hCyEzi3ULKIUMPubbqnjFzI-No1enxbJfTsPBcygk8pLRYbth6R9ddlqUcOtq-LmfCx72hEvcPsklQR1_GbFvi0RvDwc4Lfd-bcGYAtqbiNEI7Ra6zj5U38Z0K9kX3xJJDlN_qqEJ_kHYd8AEYvqMLYgnevTBZV-YmKLt_jnoNj-41-2MQjt92iK_rpxOCUUcIGWqwoGN80BzhBPyTz0knNUj4NqCPUMykCGvIHK3Mh6oQNP6hDhsLpcRKWA8y-ihb4DyPzLzQG-36gmzEMqGHEId7mRg1t_4AB3XwdnVCIprIG6EMGFqyOATz7EDICTnKb53ZNG68mqsPJoIY8mzRyTtRNySqoSMz2394p90Iy9ZD5qGbKh2WZ2wpLb3wAvEeqaaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543dcdc581.mp4?token=Qr-GbGw5k4G6Orpo00jXKVfD7v2Sxzto_TbQhYON37K3T0GRwYgYL9qLJL8P35IaD-uObBJHL-LLm8-ofmVAqZmQjeh-QzSOc-A20VeBrYFQdLbR_Ma8BotzOlg9OqIfnTscYw4UObpVKQPRHx1HWkhomdNz_g4ttqY8w_Mz9dK66WOELdLdV9x8Sht5D6FZj84fbGDPzLqesPe_fNmsn9fLo7C2tXbPxrvnYCAk6SryUDmDx9vU9W6gphF3M3CUDJ9QL2mFEtc39urwuNh34FISr0hekCyF4hGp8hCyEzi3ULKIUMPubbqnjFzI-No1enxbJfTsPBcygk8pLRYbth6R9ddlqUcOtq-LmfCx72hEvcPsklQR1_GbFvi0RvDwc4Lfd-bcGYAtqbiNEI7Ra6zj5U38Z0K9kX3xJJDlN_qqEJ_kHYd8AEYvqMLYgnevTBZV-YmKLt_jnoNj-41-2MQjt92iK_rpxOCUUcIGWqwoGN80BzhBPyTz0knNUj4NqCPUMykCGvIHK3Mh6oQNP6hDhsLpcRKWA8y-ihb4DyPzLzQG-36gmzEMqGHEId7mRg1t_4AB3XwdnVCIprIG6EMGFqyOATz7EDICTnKb53ZNG68mqsPJoIY8mzRyTtRNySqoSMz2394p90Iy9ZD5qGbKh2WZ2wpLb3wAvEeqaaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: آمریکا و اسرائیل مراکز هسته‌ای ما را که بیشترین نظارت روی آنها بود، بمباران کردند و آژانس بین‌المللی هسته‌ای سکوت کرد/ هر موقع آمریکا به تعهدات خود عمل کرد، می‌توانیم درباره بازرسی‌های هسته‌ای صحبت  کنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/akhbarefori/693065" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693064">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
شرط ایران برای آمریکا برای بازگشت به میز مذاکره و گفتگو  پزشکیان:
🔹
آمریکاست که راه ما را بسته؛ طبیعتا ایران هم راه را بسته است. راه‌ها باید دوطرفه باز شود تا بنشینیم و در میز مذاکره با هم گفت‌وگو کنیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/693064" target="_blank">📅 10:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693063">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf5dddbc36.mp4?token=WA6gG9cIdchESqcpiQjd0BzWNt-uQtn9JPMLWoiOn55CYMwm-0-uVjzZ_eIRuAlaSpwkLU_bwYPUQi8kplcibQsjc-p-h5G9qPBexJos69tAAkF6ZNtYlEbIVr6-CI25SNEHo3UIX7h42pS483yZMpXStIG2CM5hfcdEMdHO8-iJaQXx9LBEZLsZd42vEq1wLeivSxGF0Z2lcIIeI50YjxDVtozi5sCZt6_05iMFE4tJAURfXAvrAiFbVfjU7RVcFaOruhoQE7vbPiDuyAOReNEiUOVHZXqhIbQi6dZvdNUWxHxMmON8_fPj6b66cWQtnPkeADWW5j_u3EMYybcAOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf5dddbc36.mp4?token=WA6gG9cIdchESqcpiQjd0BzWNt-uQtn9JPMLWoiOn55CYMwm-0-uVjzZ_eIRuAlaSpwkLU_bwYPUQi8kplcibQsjc-p-h5G9qPBexJos69tAAkF6ZNtYlEbIVr6-CI25SNEHo3UIX7h42pS483yZMpXStIG2CM5hfcdEMdHO8-iJaQXx9LBEZLsZd42vEq1wLeivSxGF0Z2lcIIeI50YjxDVtozi5sCZt6_05iMFE4tJAURfXAvrAiFbVfjU7RVcFaOruhoQE7vbPiDuyAOReNEiUOVHZXqhIbQi6dZvdNUWxHxMmON8_fPj6b66cWQtnPkeADWW5j_u3EMYybcAOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: در دیدار با رهبر انقلاب ۷ ساعت روی زمین نشسته بودیم و گفت‌گو می‌کردیم  رئیس‌جمهور در گفت‌وگو با شبکۀ خبری سی‌بی‌اس:
🔹
۷ ساعتی که خدمت رهبر معظم انقلاب بودم، ایشان هیچ جراحتی نداشت. ما روی زمین نشسته بودیم و گفت‌گو می‌کردیم، ما چون عادت نداشتیم، دائم…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/693063" target="_blank">📅 10:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693062">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f6b017a903.mp4?token=S06cuKDOv8xnsnPb8QeCYDDzmJRrhLztFgXNFUIPZsz0KE47uK3hQ_NHPqNmpJQxG-30YAk2ElgcCe9Ipr4_y8kX0YSsCgkDRz1p9BiMHIIx1XEYR5wZPNIC2Umm_Kg_pKllJV2JosL_nHLWlt0wCT83Kt0-_Ydl0OJTuIZS1d9b_8Fn6ETWJhe-u_Kq2CpSxktkCGbMKPhKLotelp3KE-T0t258PosW6FZuRvzHhythkaMCcUra7Iz3wszVwpNcx6f71gScTfhsP-uF1XbWE3-GN7VVPWcz974R6A7EzMZuZ6pNzlqQx8WXl1PDKqcSPziWJHpOjlKFSQf5QVCWVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f6b017a903.mp4?token=S06cuKDOv8xnsnPb8QeCYDDzmJRrhLztFgXNFUIPZsz0KE47uK3hQ_NHPqNmpJQxG-30YAk2ElgcCe9Ipr4_y8kX0YSsCgkDRz1p9BiMHIIx1XEYR5wZPNIC2Umm_Kg_pKllJV2JosL_nHLWlt0wCT83Kt0-_Ydl0OJTuIZS1d9b_8Fn6ETWJhe-u_Kq2CpSxktkCGbMKPhKLotelp3KE-T0t258PosW6FZuRvzHhythkaMCcUra7Iz3wszVwpNcx6f71gScTfhsP-uF1XbWE3-GN7VVPWcz974R6A7EzMZuZ6pNzlqQx8WXl1PDKqcSPziWJHpOjlKFSQf5QVCWVTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جلوگیری از حشرات مزاحم خونه از زبون خودشون
🐛
🕸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/693062" target="_blank">📅 10:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693061">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-text">🔹
«روشنایی» از دل آوار و خرابی‌ها دوباره سر برآورد؛ پل‌ها و تونل‌های هرمزگان استوارتر از قبل، قد برافراشتند
🔹
در روزهایی که دشمن برای ویرانی زیرساخت‌های جاده‌ای کشورمان به خود می‌بالید و راه دسترسی مردم بندرعباس را می‌بست، مردان راهدار، در دل خطر ایستادند؛ تا هیچ بن‌بستی، پایان راه مردم نباشد.
🔹
و‌ دشمن چه غافل بود از آن‌که مردم جنوب سال‌هاست با ایستادگی مأنوس‌اند؛ و این‌گونه بود که از دلِ تاریکی و آوار، دوباره نور سر برآورد، پل‌ها قامت برافراشتند و جاده‌ها زندگی را از نو به جریان انداختند.
🔹
آنچه در ماه‌های اخیر بر هرمزگان گذشت، نشان داد که راه‌ تنها ترکیبی از آسفالت و بتن نبوده، بلکه تجلی اراده‌هایی است که می‌ایستند، می‌سازند و دوباره عبور را ممکن می‌سازند.
🔹
آنچه خواهید دید، روایت مهندسان و راهدارانی است که با عشق و غیرت، راه را به مردم بازگرداندند؛ قلب‌های تپنده جاده‌ها و مردان بی‌ادعای روزهای دشوار...
🇮🇷
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/693061" target="_blank">📅 10:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693059">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0ii4pVLOMdrm72hzUUiOD0iXgvDZ6XQKQ42Hk-MkGRUFdiZ1ztrIpkqcryKcka2dJRjuK7H_4Br1wQntsl1cN8-lUxncDHY6sR7f5hVVwGR0vWEPqzn0NdwkZM3lNk6uiFPdi08CIDODHi46-iKAKFdfOTmOsA9Enh8OqSxp1Mt84h84gMzTTC9RDteCk0y-XcS1ML7JCE0ucGj0ZfCpgFUoiGQDlfgHEctWa_30PdtLGLlCHWXXvRYOsIVRimUK_GsoCgABhWoWgaCsuh2GjfCC_o2NKI_i4V5GVw_Qk9nnrmgaYvn0lQsjmYjgw2e_8AhMrv87nMWUILRc7Swrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d5aa01c77.mp4?token=ryWk_Xuu0yzh7plhQvixDxD-7V_Uqbyx-ijAUaSIKA5ncav-I1m86ZdvB2QkR79_hPir5mXAPxtDUflcUqY4ahrUOiW2P1QQNFitlVx43obRlMiRQvq3ovEbrK4bzqzNS7-ijkak_6eTN7VIg3QMgW1mWCw_T8x4_TETZeJ7Q7scz8DPadOBRn0N5jg4y2Mb0BPw9qyUKZpd7MlTP59BPuHc3cqvZ_hnBPCjN8J-oxM0UahLoqZblcHqWiQANbIGfKoLgNKVf7Xjh7AAUPKvbeXkG2yRfx2ZeEwWdo6TcGbBfSsNDqRQFcoxrMxUlZeSE94eU6RN-u7KEHE61liE3Jlef7cn7JtA2OpcBjNOLRwXlJzCoQkyt9Nmy3dXALxjisuJbWaN38edPivRCYVlKfyz16CTjw_OkShPgSR7lLAt4dfLZY421fnWdJdC6a-9UjQla5NDlD5v_OB1ePHd-00rRggNy1TnZ_Pgr9dzuyOEsoy1bnyX66398dAd4tN8pCD_96B3t3V_s1mDXxEFyc5ePAWY4TksriOnYsmjW7Y4InYaruRGNkwkFJiKtzqvW3EG9Ocg7f7CxqR3IG-8ymGmqYgb4JJ3ASbNSXFu-CSAjKDoi-Nzoyi859ka6di68hJgEvEPQ-sc0G97mLMDoWyHGhKP_64OvG9EOQpzLQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d5aa01c77.mp4?token=ryWk_Xuu0yzh7plhQvixDxD-7V_Uqbyx-ijAUaSIKA5ncav-I1m86ZdvB2QkR79_hPir5mXAPxtDUflcUqY4ahrUOiW2P1QQNFitlVx43obRlMiRQvq3ovEbrK4bzqzNS7-ijkak_6eTN7VIg3QMgW1mWCw_T8x4_TETZeJ7Q7scz8DPadOBRn0N5jg4y2Mb0BPw9qyUKZpd7MlTP59BPuHc3cqvZ_hnBPCjN8J-oxM0UahLoqZblcHqWiQANbIGfKoLgNKVf7Xjh7AAUPKvbeXkG2yRfx2ZeEwWdo6TcGbBfSsNDqRQFcoxrMxUlZeSE94eU6RN-u7KEHE61liE3Jlef7cn7JtA2OpcBjNOLRwXlJzCoQkyt9Nmy3dXALxjisuJbWaN38edPivRCYVlKfyz16CTjw_OkShPgSR7lLAt4dfLZY421fnWdJdC6a-9UjQla5NDlD5v_OB1ePHd-00rRggNy1TnZ_Pgr9dzuyOEsoy1bnyX66398dAd4tN8pCD_96B3t3V_s1mDXxEFyc5ePAWY4TksriOnYsmjW7Y4InYaruRGNkwkFJiKtzqvW3EG9Ocg7f7CxqR3IG-8ymGmqYgb4JJ3ASbNSXFu-CSAjKDoi-Nzoyi859ka6di68hJgEvEPQ-sc0G97mLMDoWyHGhKP_64OvG9EOQpzLQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیژن مرتضوی، نوازنده و خواننده سرشناس ایرانی، جدیدترین آهنگ خود را برای کودکان شهید میناب خواند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/693059" target="_blank">📅 10:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693058">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2cac7c872.mp4?token=U8d1xtTUIW2S0-_trOmMUealb82fc95hH0QOnK-5AuWlA4BSu8-UYzMcAGFpChJ5NszkN2fwSrxlz_k0JDINm09J2xa8rNH8RYKOlcYSTopnUESGw2i--X1AFNG_NXAQRI6v3jQgrjN-UchKMQFeZuZBOsQuIbvTb_k8W2trDCWSJROKkpNEq4IrbRoEQ0a5NST5f-rqjo3JfGhHnZ9SdoAsNEe7XfkG7OOrgKFD1nxFs4Xaenz8L0FRQ9Se6ZUEnoTWPQb_5PeAM1jDswbdzB5SzgTa40EoPD8FHddGuHIDJHJgz1e_ehRpQ1S_C7bYu0ewKgiwS4uFBSmhEOAPvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2cac7c872.mp4?token=U8d1xtTUIW2S0-_trOmMUealb82fc95hH0QOnK-5AuWlA4BSu8-UYzMcAGFpChJ5NszkN2fwSrxlz_k0JDINm09J2xa8rNH8RYKOlcYSTopnUESGw2i--X1AFNG_NXAQRI6v3jQgrjN-UchKMQFeZuZBOsQuIbvTb_k8W2trDCWSJROKkpNEq4IrbRoEQ0a5NST5f-rqjo3JfGhHnZ9SdoAsNEe7XfkG7OOrgKFD1nxFs4Xaenz8L0FRQ9Se6ZUEnoTWPQb_5PeAM1jDswbdzB5SzgTa40EoPD8FHddGuHIDJHJgz1e_ehRpQ1S_C7bYu0ewKgiwS4uFBSmhEOAPvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این گرونی سوسیس و کالباس، خودت توی خونه کالباس لیونر خوشمزه و سالم درست کن
🥪
مواد لازم:
🔹
سینه مرغ ۵۰۰ گرم
🔹
روغن مایع ۱۰۰ گرم ( ۷ قاشق غذاخوری)
🔹
سفیده تخم مرغ ۱ عدد (۳۰ الی ۳۵ گرم)
🔹
نمک ۱۲ گرم (۱ قاشق غذاخوری)
🔹
سیر ۲ حبه
🔹
پوره یخ ۱۵۰ گرم (۳ چهارم لیوان)…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/693058" target="_blank">📅 10:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693057">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
پزشکیان در مصاحبه با سی‌بی‌اس: آمریکا برای باز شدن تنگه هرمز عجله کرد و باعث شد تفاهم‌نامه از بین برود/ آمریکا به مفاد تفاهم‌نامه درباره تنگه هرمز عمل نکرد و کار به درگیری کشید
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/693057" target="_blank">📅 10:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693056">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c79738457.mp4?token=hvtArveQpuFCZ7akPuv7-nsi4254dZE2TP8qSinpgvB7QaKtlHeeuLlQSWq93QssoADjSMNMgI6xgltqCYrlqAGDvHqlqQEUR9CYkLUNw3wji1YY7AYjjlBhjJNJ7AsuX1ypXNApPQedJJ8ojsqwL2Hi5Y09kuq_jccgpI_dKt6kBhrgFD1nxMIFrRVH216PHYnts9ncQB3aq9YuneePhd_0AZF2VWYEdQ8RpabazreBDYa5pjxEvfHmaHzwQz86I4aUbwZIF9UvEYnQhYZN0fjeNeQDThMf6qNVcCfO2dQzzbOSJrEUXnnISLAEEkHCHyCfrP8mPUxaIkJ-kjplhhtx-9W_7mWPn54GP1gM9xGw5pAxnEQlL1YSHGzFyzWtgaUJUo3xrZMspe9TCXkXBjjCqCriZLP8MUwzVGXVyDAzlidRnYzAgwyn3e1EjBZ6ziZZI8gZuRJowl_TowRk4CJfPNc8eIsbn_ca-a-anpEuxmkcwn_aB5MDT754VVCSKQlbzi4ETwppwyOIoDnTTS_itDMg6I1pUw3Tf2wCEbXsqNvfptYA9z_MLTiFL-c8VAcnbD2xLYLJUsglODGadi_TpkniawO3ISmm-L4qkJWa4qWV3XbTruGv5ztQdrhW2mdiyxPVCW3Q49EzFIAsTwCX0ihc1mabE_DcPkFM9K4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c79738457.mp4?token=hvtArveQpuFCZ7akPuv7-nsi4254dZE2TP8qSinpgvB7QaKtlHeeuLlQSWq93QssoADjSMNMgI6xgltqCYrlqAGDvHqlqQEUR9CYkLUNw3wji1YY7AYjjlBhjJNJ7AsuX1ypXNApPQedJJ8ojsqwL2Hi5Y09kuq_jccgpI_dKt6kBhrgFD1nxMIFrRVH216PHYnts9ncQB3aq9YuneePhd_0AZF2VWYEdQ8RpabazreBDYa5pjxEvfHmaHzwQz86I4aUbwZIF9UvEYnQhYZN0fjeNeQDThMf6qNVcCfO2dQzzbOSJrEUXnnISLAEEkHCHyCfrP8mPUxaIkJ-kjplhhtx-9W_7mWPn54GP1gM9xGw5pAxnEQlL1YSHGzFyzWtgaUJUo3xrZMspe9TCXkXBjjCqCriZLP8MUwzVGXVyDAzlidRnYzAgwyn3e1EjBZ6ziZZI8gZuRJowl_TowRk4CJfPNc8eIsbn_ca-a-anpEuxmkcwn_aB5MDT754VVCSKQlbzi4ETwppwyOIoDnTTS_itDMg6I1pUw3Tf2wCEbXsqNvfptYA9z_MLTiFL-c8VAcnbD2xLYLJUsglODGadi_TpkniawO3ISmm-L4qkJWa4qWV3XbTruGv5ztQdrhW2mdiyxPVCW3Q49EzFIAsTwCX0ihc1mabE_DcPkFM9K4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان در گفت‌وگو با شبکه خبری سی‌بی‌اس: آماده گفت‌وگو هستیم، اما قلدری و زور را نمی‌پذیریم  پزشکیان:
🔹
هر موقع آمریکا شرایط ما را بپذیرد، وارد مذاکره می‌شویم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/693056" target="_blank">📅 10:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693055">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
دبیرکل النجباء عراق: اگر پروازهای ایران از سر گرفته نشود، از مردم عراق، موکب‌ها و زائران می‌خواهیم برای اعتصاب در فرودگاه‌های عراق تا زمان لغو این تصمیم آماده شوند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/693055" target="_blank">📅 10:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693054">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
پزشکیان به سی‌بی‌اس نیوز : تیم ۶ نفره از نهادهای مختلف درباره سیاست خارجه تصمیم می گیرند/ بی‌اعتمادی میان ما و آمریکا مانع مهمی برای دیدار مستقیم با ترامپ است
🔹
اگر آمریکا جدیدترین پیشنهاد ایران برای بازگشایی تنگه هرمز را بپذیرد، تهران به تعهدات خود پایبند…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/693054" target="_blank">📅 10:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693053">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTa-B47LPFRuyo6hpT3GLm6PQPLjUFht0p5GG7C9hpH0yztuXGYOiiCAwdEhTQFhXU-qZlItkDvDn0diqZppMfplwgYPPLIqnf7CgrPfzcpwJCM4n_hGmzegkkR14xSn3VPlFiso359JsIYA2QmgnbBHkCzSTD-Ah1be_NrC1sjZiFyKVm4MetcaFVH-vxjq6nXn7YWpW1oLtdtyMOAR9NevBawxUbCk0zPKHsfHMLWFcVwiAMPnt9fz7wNHazxtHotG0CqdnYXPa2vKbzFSfekHeZNltrcZZOlLSuUTpcDr4NJU9fF1ivna1s1qNPI6xmu-T67p7NIJ72VKAPenqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این شماره‌ها و کدهای کاربردی می‌تونن خیلی از کارهاتون رو سریع‌تر راه بندازن
📱
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/693053" target="_blank">📅 09:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693052">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ایجنت‌های OpenAI خودمختار ۵۳ تصویر کاربران را در اینترنت منتشر کردند
🔹
شرکت OpenAI اعلام کرده ۵۳ تصویر متعلق به کاربران، بدون اطلاع شرکت توسط عامل‌های هوش مصنوعی در سایت‌های عمومی میزبانی تصاویر منتشر شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/693052" target="_blank">📅 09:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693051">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe8mOnvBGbOhg-G43eqWux_NlmpBEhXNFFniNMdl0vfQa--4VXp6v4YVgSuYtwDpOjI0lKKDfWLS2B6dpDjsZVt8nd7QPNWBCTFBUsfGhgPKhvOoMPOh7qJJWLrr11XTwCsYDl9KnanPRT5mdt4lmiWvEccwIl5uie3qw2RNCN5ZEVbNfy6IllURWVKMUmukaJvVZ0sAm9Lnmct5Z8VXkM7Z2nHBbQU4mG7yZpsIv3wLBwgkZ9VEax8ClxdUE_7iBhGXtbG9qlzzmkUQZtAAtjdUh0bzxDWmpJtTleK9au20Ear7KsfwVuPd4x6_lggv1PDb7vKdxVSv5wMQU99wXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۸ خوراکی مفید برای رشد و استحکام استخوان‌های کودکان
🦴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/693051" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693049">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
فردا یکشنبه ۵ مهر، کالابرگ سرپرستان خانوار با رقم انتهایی کد ملی ۷، ۸ و ۹ شارژ می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/693049" target="_blank">📅 09:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693048">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
جنگنده‌های سعودی در دو نوبت شهرستان قطابر در استان صعده یمن را هدف حمله هوایی قرار دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/693048" target="_blank">📅 09:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693045">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVduwS0c1GFnrgJGA3OXfstFN-4VM7-izUsOiC3iN0lj1twdDmzcLH5cqrsgyIljHal4WSSsCyglZnuDMigP4Bq1gY7LB03Pv2MtcGPAF1OO7e8AMUl95G9HPctRT0XDUA0Z2TpHZ9YAHrG8QM7xBzSsIRfvSAEwUg5-_ZSFtPskBAEbWd6b7MfbVTF4hix9dXODNWNrgyqoR6z9CWfxYngpQkSCCxsHPpRaYhXi5L9BAN-wF6uKvah9y8z2KZ8MS4X1B_DNx7qANQeGJj0KuNH1t0i6JT3WBeOJBpsgwjjnwBRpYtTUuTXNoqL8JYyjzJIMMVnaHhVeNZSwVX515Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f5aab4b20.mp4?token=FWW-iSqmNZwDtZ6yuDjiGbzn_GqGmvRiF_AASQ8JMNhj4BYci6adWFqi7ExvNqa6IfSEkLamYAZjEr1KejxgT1VMyyf_Lz3ZGY-AJ_hnLndMoCtfY63weiLkDcXU5SbZoPQ68VLISPnMOdnMrQuWcM-zgmUnFQc__-aSwn1WmOK-yuo6SNK5MXyG68p7QfiFpvP92u46NmE5mLlw9sA64a-o53oVoeYeLexSfWThfXQwJ1ec1Wc-B1GR3jUkW8gGRVr_SacZFNOJhDttCQMF-8q9fQi5gz6UOG3eP-6DpVHzTYdOOu4Ul7QxujA6ogWkfuITVUmxuvIh4eCuLmmGaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f5aab4b20.mp4?token=FWW-iSqmNZwDtZ6yuDjiGbzn_GqGmvRiF_AASQ8JMNhj4BYci6adWFqi7ExvNqa6IfSEkLamYAZjEr1KejxgT1VMyyf_Lz3ZGY-AJ_hnLndMoCtfY63weiLkDcXU5SbZoPQ68VLISPnMOdnMrQuWcM-zgmUnFQc__-aSwn1WmOK-yuo6SNK5MXyG68p7QfiFpvP92u46NmE5mLlw9sA64a-o53oVoeYeLexSfWThfXQwJ1ec1Wc-B1GR3jUkW8gGRVr_SacZFNOJhDttCQMF-8q9fQi5gz6UOG3eP-6DpVHzTYdOOu4Ul7QxujA6ogWkfuITVUmxuvIh4eCuLmmGaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پست جالب سفارت ایران در زیمبابوه و به سخره گرفتن سخنرانی نتانیاهو برای صندلی‌های خالی:
نتانیاهو هنوز در حال شمارش کسانی است که سالن را در زمان سخنرانی‌اش ترک کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/693045" target="_blank">📅 09:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693044">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
رئیس پلیس فتا پایتخت از شناسایی و دستگیری کلاهبردار اینستاگرامی پیش‌فروش آیفون ۱۸ که از بیش از ۲۰ نفر کلاهبرداری کرده بود، خبر داد
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/693044" target="_blank">📅 09:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693043">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBxMfevckiH1VCcqn7BEvafUsOw5fDnfsHRz0q53OPhla6qsXKgb_f0M284VFK0HFbvVCWIaSVt5171-m_wM18s-cql_OJowsoarkb63DVlCBjcAMrWVvi_Oge97MiO94cWCYxQ1jZDQJkQUBs0djONy7tiFwg5zzs5rheAlfZYsUKtRK0jKPrrIJhK7-seaKFqixhpEHqPT_C-JvH8bSzw8kKy02P5XAR9xvlIFDZ6v7588V6GJzN3imt3buspN3fIBd-xCI7Nq-RFMuGJjTY1A60TnYq210Qa9x8fNw7ZYEeHuiNdKCIzP1K4NTyXirJcNIt8wzr4NutasDuHtNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کلمبیا به طور رسمی روابط دیپلماتیک خود را با ایران قطع کرد
🔹
کلمبیا در این بیانیه ایران را به آنچه «ارتباط با گروه‌های تروریستی بین‌المللی» خوانده شده متهم کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/693043" target="_blank">📅 09:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693042">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbfQg6gFBpkbaUCGDoPi2mK2MTEpM6tWIc0TEEsQowmEP4LZrFPEMjljBP2pNJ5fLRmEDM0abn8k8G-7SWJpVZhZv1Rj-J-qmh0OfXXt3SB9RnVv8c64lyFC8dQyDlHpWZ8KI983YLc-urVzmDf6yrZWubxZOjfIUmcbLrg4UcQfZMhZYn-IYF0IRQlX-9Dbu_eNjTuDpZDKtezCtz_5XuDifEWgCenJk51DVdQNJLyz1LucRZJzEPr7qY0o2DVu5VassRBZy-yqPup21oUr40lu8yeAhgD88iK5d7pxnrV4Md9obdAsIXP-iF_XPsdP6HW1V7PDUUgvWnlyOA1_Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کانال ۱۴ اسرائیل: عربستان سعودی تمام‌وقت مشغول درخواست کمک اطلاعاتی از اسرائیل برای مقابله با حوثی‌هاست، اما در نهایت، هیئت نمایندگی‌اش هنگام سخنرانی نتانیاهو در مجمع عمومی سازمان ملل، سالن را ترک می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/693042" target="_blank">📅 09:10 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693041">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raz4zeRAnaeooeNunsb8EZceVI4_ZKtJlO3mvtl4hkgt6T1QnLLD0wvGEiIeGkOmhECLoxfoB9QAHo5iZEKh-UiePCE5PtoWDyNtn32oGHh685V3yZ2-9HzqM_JKGxfLGbEVKMHpX5inaXHCIuSgxlcswZGq7u0hv2j494BxAVukemms7ZTUeuiS5s9XxsqvL_JZsSsmAKplfxd3Q7eCdJnZPh2vhuATVu7nuDv_eb83XTrpKaSP4tCS_k81JpVLt4W3vQIyMVeSWLUzQR8eiJT_DUD1wTyxwHe6Ehrd2KCxZIiPi4w1yQxdR5bug6HuAfWccA7Czubm5Ci2AI0hCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
داروهای رایج برای مشکلات دهان و دندان
🦷
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/693041" target="_blank">📅 09:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693040">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">چله علم النور 4_ جلسه ششم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/693040" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
جلسه ششم؛ سرچشمه‌ قدرت
🔹
انسان‌ها از دیرباز به دلیل احساس ضعف و ترس در برابر حوادث جهان، یا به نیروهای تاریک و شیطانی پناه برده‌اند یا به ریسمان محکم الهی چنگ زده‌اند.
🔹
یادآوری مداوم نام‌های خداوند، شکرگزاری و هم‌نشینی با انسان‌های مؤمن و مثبت‌نگر، راهی مؤثر برای جلوگیری از فراموشی رحمت پروردگار و نجات از ناامیدی است.
🔹
انسان‌ها برای عبور از سختی‌ها و فتنه‌های روزگار، نیازمند تکیه بر دو نام مبارک
«الْقَوِيُّ»
و «
الْمَتِينُ»
هستند تا جسمی توانا و روانی استوار برای خدمت‌رسانی داشته باشند.
🔹
هرچه ظرف «باور و ایمان» انسان بزرگ‌تر باشد، دریافت او از قدرت و رحمت الهی بیشتر می‌شود.
🔹
متوقف کردن کار و تلاش به بهانه‌ی شرایط سخت، نشانه‌ای از ضعف روان است.
🔹
مؤمن واقعی کسی است که حتی در تاریک‌ترین روزها با دلی مطمئن می‌ایستد و جوانه امید می‌کارد.
#مدیتیشن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693040" target="_blank">📅 09:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693039">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
سخنگوی ائتلاف سعودی حمله موشکی و پهپادی یمنی‌ها به عربستان (به سمت خمیس مشیط) را تأیید کرد
🔹
بامداد امروز منابع غیررسمی از شنیده‌ شدن صدای انفجار در بخش‌هایی از پایتخت عربستان خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/693039" target="_blank">📅 08:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693038">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Paeeiz</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/akhbarefori/693038" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎼
پاییز
🎙
محسن چاووشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/693038" target="_blank">📅 08:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693037">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9c7f0ea6.mp4?token=Bk6NBi_OghKKQFYm9sDXsZEb_NlCTfmCfyob2XHRinR_gHBmPBqJscfZDy1uFMoIY7ruUtly1RJYXjtFUJAHkmUBjtgUmdZm8xPuedaVFiTS3aqirnMorIzgsv5wIuU44GJw5sLbdyeIS-BKUxlvjqlhqQJffMFkF682hTMzs8w2nkWIDI86UBzzRxnLi1qzrk8Kmz98lCkmIo8sIgRX3qrU-xsm_UTrU8wt2SyXCQBAF4tZ4F0BQ5WQKlnT5iNXOtzXBI16UpYN2RjYMO8eAyTnD73L1W3QHRFi4nku8B7tRh_986pIDYEu9xOLUemZt5D05wwaPuKWn1wDQdKErA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9c7f0ea6.mp4?token=Bk6NBi_OghKKQFYm9sDXsZEb_NlCTfmCfyob2XHRinR_gHBmPBqJscfZDy1uFMoIY7ruUtly1RJYXjtFUJAHkmUBjtgUmdZm8xPuedaVFiTS3aqirnMorIzgsv5wIuU44GJw5sLbdyeIS-BKUxlvjqlhqQJffMFkF682hTMzs8w2nkWIDI86UBzzRxnLi1qzrk8Kmz98lCkmIo8sIgRX3qrU-xsm_UTrU8wt2SyXCQBAF4tZ4F0BQ5WQKlnT5iNXOtzXBI16UpYN2RjYMO8eAyTnD73L1W3QHRFi4nku8B7tRh_986pIDYEu9xOLUemZt5D05wwaPuKWn1wDQdKErA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک: به وفوری فراتر از مصرف انسان می‌رسیم؛ ربات‌ها آنقدر گسترده می‌شوند که حتی اگر کسی قلعه بخواهد، برایش می‌سازند و تقاضای انسانی را کاملاً برآورده می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/693037" target="_blank">📅 08:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693036">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
کبدی بانوان نقره گرفت
🥈
🔹
تیم ملی کبدی بانوان ایران در دیدار نهایی بازی‌های آسیایی مقابل هند به میدان رفت و با قبول شکست ۳۷ بر ۳۴، از کسب عنوان قهرمانی باز ماند و به مدال نقره رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/693036" target="_blank">📅 08:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693034">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd16021757.mp4?token=hcppz4nEhdaRh6T4K8G0IIt7oLaTvJMqiJEf1c0sSn1qMglbRCKPqGHUEHnKUh_PjaJSXlShj-X3USVLYEa8f0dN6cu1DIGX7ZmAL7XtiME1DPc0VnqJiJKOqx_u3FjXZ1kHIFzbVT5ItJwy9cyN9Hnanxqh1Wgg5udHLaOxDhMr61OXt3dCVIADDxMXzVZokt_ROHLseNwMYxdxc7P_iUKPvfCkN8pcxo2_j1dw-GP1uf6AHY_0djwFkqCrh6VhTTVUKvQCRpaHzVRAUTsipode9TBoyIvJ2QEgFjzlyBdJ95rnYU4PFw8LjZPQRSPkLKSrooahDYw_Q36e7NevEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd16021757.mp4?token=hcppz4nEhdaRh6T4K8G0IIt7oLaTvJMqiJEf1c0sSn1qMglbRCKPqGHUEHnKUh_PjaJSXlShj-X3USVLYEa8f0dN6cu1DIGX7ZmAL7XtiME1DPc0VnqJiJKOqx_u3FjXZ1kHIFzbVT5ItJwy9cyN9Hnanxqh1Wgg5udHLaOxDhMr61OXt3dCVIADDxMXzVZokt_ROHLseNwMYxdxc7P_iUKPvfCkN8pcxo2_j1dw-GP1uf6AHY_0djwFkqCrh6VhTTVUKvQCRpaHzVRAUTsipode9TBoyIvJ2QEgFjzlyBdJ95rnYU4PFw8LjZPQRSPkLKSrooahDYw_Q36e7NevEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان در دیدار با دبیرکل سازمان ملل: پس از تجربه‌های گذشته اعتمادی به آمریکا نداریم
🔹
ایران میز مذاکره را ترک نکرده و خواهان صلح و امنیت در منطقه است اما اجازه نخواهد داد فشارهای خارجی این کشور را به تسلیم وادار کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/693034" target="_blank">📅 08:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693033">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKPI_Ib-nF5yDO2eMHI2pfy-rinI9cTMg2SfTaPi1ao--3B8Yw8zX1PRkIWm7OynGpsa7r_123qs9O0RaS0PCarCU-LclhshfKKckmigyO-JTtK0hrI2PwSO28w5W9xUJOl4rLSqveDTnU1ZlAafEOdQPM_V5lU4aQzbpQaDmLY5SYyWtkCZT2TtPkPFjhFS-RDaqsLH5rLqvctw-6U3z3_C2CUDdHaBAxtUdTNPUjQHnNugXCjjOtHCSo1Ih_lTGvUMWMZaU218l4TccYntAYSPHX1ZbY-Jop35oq56mPLrBxWcUQLisTCOPZbNXlVTAlsWnMrEppLEHyxXEnLl0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ با انتشار پستی در شبکه تروث سوشال بار دیگر تنگه هرمز را «تنگه ترامپ» نامید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/693033" target="_blank">📅 08:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693032">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/212062124a.mp4?token=gEXkKG67ntAzP9Dw-oHdfNucnui4SQYxft6L3tmq7onvqD3MtJVzFv5MHFpSzIn2rAM2AJTpgfEl8bDsfq-e1Njv8zsB8BlUY15vvolkcCkfjURceJc2wDsdnk88ar74SaP1XmDcq_0J8ksFQ6zw60PSTsvavboqaFPe9fpYxPTXiw-uJClB-1NjCBK84a2RlMK_KNCOyP7O2IxS8Vd3D_0je2pBkd99Q1qYd5Rvn1vrpDx9ZEE26-fouqCsERQumUv2uRrpOagRVjQb9dNTAcxJm1uFjIqXlgxh0dJFvvq-09ifhOf3Cswe1I1glMB8u7QcmNdsblI8TWyDjOde-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/212062124a.mp4?token=gEXkKG67ntAzP9Dw-oHdfNucnui4SQYxft6L3tmq7onvqD3MtJVzFv5MHFpSzIn2rAM2AJTpgfEl8bDsfq-e1Njv8zsB8BlUY15vvolkcCkfjURceJc2wDsdnk88ar74SaP1XmDcq_0J8ksFQ6zw60PSTsvavboqaFPe9fpYxPTXiw-uJClB-1NjCBK84a2RlMK_KNCOyP7O2IxS8Vd3D_0je2pBkd99Q1qYd5Rvn1vrpDx9ZEE26-fouqCsERQumUv2uRrpOagRVjQb9dNTAcxJm1uFjIqXlgxh0dJFvvq-09ifhOf3Cswe1I1glMB8u7QcmNdsblI8TWyDjOde-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر میگرن دارید، این ترفند ۳۰ ثانیه‌ای را از دست ندهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/693032" target="_blank">📅 08:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693031">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a09ecbf76.mp4?token=BlwXv6nWrim8vMzBXtDt8AT4er8yzn5Gh-mh6yOwVxvs3GaEbz_qO5BzhHM5LBGQJ3Q-veh8aDEigrNIy80v6jheL8JskcR9kFHp8C7A03d03cc3acj7USqlJ65_kp5Yyw-5gvMlyQneRnO1KFZGNyKCaXvgJTPUA9mle_3FEiHD03Os2XdE17OphknUQ4p18SHxcTmJXX6UR-KQ-4xdJU_ePJn_FefAFp3erm5qV_OH6Bbcf17lyWxvSnYuwHvNHnn0DOvoGHwF9Xhtq4S19fNhJA2lYR3X7vGjfYEu0TuT26kuWSZF4eQ2TIqjU27cRvYQWsyLceKSxkx_D442QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a09ecbf76.mp4?token=BlwXv6nWrim8vMzBXtDt8AT4er8yzn5Gh-mh6yOwVxvs3GaEbz_qO5BzhHM5LBGQJ3Q-veh8aDEigrNIy80v6jheL8JskcR9kFHp8C7A03d03cc3acj7USqlJ65_kp5Yyw-5gvMlyQneRnO1KFZGNyKCaXvgJTPUA9mle_3FEiHD03Os2XdE17OphknUQ4p18SHxcTmJXX6UR-KQ-4xdJU_ePJn_FefAFp3erm5qV_OH6Bbcf17lyWxvSnYuwHvNHnn0DOvoGHwF9Xhtq4S19fNhJA2lYR3X7vGjfYEu0TuT26kuWSZF4eQ2TIqjU27cRvYQWsyLceKSxkx_D442QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آبگرفتگی خیابان‌ها در پایتخت تایلند به دلیل بارش سنگین باران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/693031" target="_blank">📅 08:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693030">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEgLNQjPoXRQRpT-OncqoVmyuNDxKDbX1p_Fq7RWxoNL5NBFC0Eac3SPhp2O_iOnEwRQJApiX2vPMSpgpX79PZIzrYH9YPWleDGB8Hbt3rOy_dvMB5E3I9wit5PGQ4D4p0tIHNTWmRzgYn6GnKz3zIQf4Ixv4ZZTFuXY8_r_O96WMQKARGiE9OX4nkmrIg8ToApZ0LutI8Z1iPRJwq_4T2-j-UNKmE4URrs6GNw6-kQLSv0yFgHHS-B4wmAgUIy0Gs0iqc7giDaVtl0l70UAVBwia3FftdOV5ToTOe5o7SqKsuglR-6QZj9D7a3h9_PTrEQN7iaJ8XI46rSFj3J08Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نخست‌وزیر اسبق عراق: توقف پروازهای ایرانی، قربانی‌کردن منافع ملی عراق است
عادل عبدالمهدی:
🔹
بستن مرزهای هوایی عراق در برابر همسایه، متحد و دوست ما، اشتباهی بزرگ و چشم‌پوشی از حاکمیت ملی و قربانی‌کردن منافع ملی و آینده‌مان است. عقب‌نشینی بهتر از اصرار بر اشتباه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/693030" target="_blank">📅 08:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693029">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
به جرات می‌گویم مرجع عالیقدری که هم از دین، هم از سیاست و هم از رسانه سر در بیاورد، در دنیا به اندازه‌‌ انگشتان یک دست هم نداریم، و قطعا یکی از آن بزرگان، شهید والا مقام، آیت‌الله العظمی سید علی حسینی خامنه‌ای بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/693029" target="_blank">📅 08:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693027">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
واژگونی یک دستگاه اتوبوس در آزادراه ساوه همدان/ ۱۱ فوتی و ۱۷ مصدوم
🔹
این اتوبوس که از غرب کشور در حال حرکت به سمت تهران بود ساعتی قبل در آزادراه همدان به ساوه واژگون شد. علت حادثه هنوز اعلام نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/693027" target="_blank">📅 08:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693026">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای
وال‌استریت ژورنال به نقل از مقامات آمریکایی: ترامپ پیشنهاد ایران را رد کرد
🔹
آمریکا به ایران و میانجی‌ها اطلاع داد که قصد ندارد تحریم دریایی را لغو کند.
🔹
مواضع ترامپ ممکن است با ادامه جنگ تغییر کند و تحت تأثیر نتایج انتخابات میان‌دوره‌ای قرار گیرد.
🔹
ترامپ به دستیاران خود گفته است که انتظار دارد بمباران ایران پس از انتخابات میان‌دوره‌ای از سر گرفته شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/693026" target="_blank">📅 08:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693025">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
پزشکیان نیویورک را به مقصد تهران ترک کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/693025" target="_blank">📅 08:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693024">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1zp7jqF5imQUOeB-m1DrcrViHrrVU4Lh8pz4eSKgFQBjPBIlj6prC6ZwL3L8AHUj4ZgbSzH3-F6nc45AERulSRoSsbQYYhdQkyT0i24RyXHJPBzk1mSCWQs6NSIg1-sSSswxu_j8yEL66VD1dSWrCCPxK4HMjIIorBtGqEPHNsaOuNOIQhxsxvHUHLcPasRtTuH39BGyaU4frskYzRGo9FwYMhTgCuaR1qvdgkClbS_4g3QY9RbAOAbYX8dHMVmVoMMnx8qetQllBNef7qJJ9W5ZZphqrwwjBbTOKQnfknEKXzVHHefHC4zw6Vmc_oFDF48--LXtlTcOVo38Puktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۴ مهر ماه
۱۴ ربیع‌الثانی ‌۱۴۴۸
۲۶ سپتامبر ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/693024" target="_blank">📅 08:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693023">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ca1T29Ct3TKJTaVSMk9tXK2Cw8tI4nmte7GR8k3K5J9h_tMawZIOSob6PFtRb-fvxUgDZqKI-Pd4rjHtGMWsgZVzNeLHZv9yGu4AgTZgp1KWbAkyYpZhTRo8jNUZZBTaOysA0rrI7EtUQrGSDXajwVQyb6NZnqCbS7T3dfNiW3tYbODNEbzINYi2yV2GJWDA7VqFLL78pxu5AV4n8xWjRl8TSqy3M3etyXZnQg044PobpG7-dF73DAxnZ7Kr_ocvGU0z2b9Mzoh692R3lnnvasBKaF7UruHFlnO_r7iJMJmFrP6KIlbxfqi09efMgHsRwwBPBGS_pLME9DNTJRtw9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمپلنت کره ای دوازده قسط ۲/۵ تومنی
✅
با وام بدون سود و ضامن
✅
توسط متخصص
برای ثبت نام وارد لینک زیر شوید
👇🏻
👇🏻
👇🏻
👇🏻
https://t.me/arameshdental
https://t.me/arameshdental</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/693023" target="_blank">📅 00:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693022">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-A2TOd3QmoyNnEcb0q24gMFWh2HI7O7MCwAPAM9cyR7I5_kxMGiUCy4RHpdNXHWvhtXRJCDb-e2g-B6I-toO4VkKihJj1H3XtwbC2MwO9cGMts3H2lWhfA5RRjJRtvOFWT55q0YHiSCFge-aHhP4cSq9tbWjcsbuEqVheqS5vI48rqQwKb_N5KXgD-CFz004QQl85AuyPzevnRM6gXLOYEUpREeADEZttLXtDBSdmxL1w-7ODtCcjRoYzyIElVGuQuV4qHdYQnD4Hj8d3Wt5_zsCw7ei1Yxj5_CSRF-KX2PlbO3Ajqs0h4qRA5yi9mfW7JTOj-FILY6es0S2FFx5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ست راحتی مردانه سوییشرت شلوار مدل Mpower
✅
جنس پلی‌استر باکیفیت و سبک
✅
مناسب هوای خنک بهاری
✅
فری‌سایز (مناسب L و XL)
✅
تنخور راحت و خوش‌فرم
🔴
قیمت فقط برای امروز  1,198,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/fast/51861/180124/</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/akhbarefori/693022" target="_blank">📅 00:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693021">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
واشنگتن‌پست: پنتاگون با تأیید ۳۷ مورد جدید، مجموع مجروحان نظامی آمریکا در جنگ علیه ایران را به ۸۶۱ تن رساند. در لیست جدید، نام ۲۹ ملوان و ۸ تفنگدار دریایی ثبت شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/akhbarefori/693021" target="_blank">📅 00:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693020">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SteJSB4Ti03TJ1RdeZSsBDzIvDOVm238lIyU7ZtyFGjNqb_Y9Kz6U6u2ef_A4bAjh_YecpUhLfeHQh4FJBQALOWOn_lINfJOhndLtRX46S5pG4adMVXziEIweOG3SZ80vvQK7vEiXzCnmzb43mDKex5zTBOCrn6giocjOmVXpisE5n3u4W_fjTPRjaN-SbvhpQKOYXWy-HFdmJniAvpzbEMQEhNpENsW7lJnzyMHfGLjfoRbXjsYNTXyL3gRZj_QhfXLMcwHyL93g2gmzb9OtJL60boJRslOhONgchr5hDk3o08US_gkI1cQZqXqwjOCKtMuJtgT7gI5eOqLG5ucrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان جوشاندن تخم مرغ در مقابل نتایج به صورت تصویری، سیوش کن به کارت میاد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/693020" target="_blank">📅 00:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693017">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SB5WeLArt-LT6jOultZLddwoEPTSt4gZTwSKMZnvDBieEtgpfrP82RXDPww9zgHgOlTe2pgCcC8L6cGroLwGDQUNQdDUU1NcZvK2lK6SqZhaArgHig4VvFERsM5XnksfS4xi2h8y7c4dc0JDxE69YHWfEuZv7PFUqZsHMecpq2W6KkdVDAgsyGg5ObAUwpPdHeoIzesfHBjHFEkUdqvsDVnH2_vheLdvrdm1tsUlgDPp05llmYTQAWGifge0r3hfDBVbacjSuCvqVn5IT2UwmVCWqN4Yaa4zqEc9yl7gdqHzUy0LhulFhscumrkzJUtwM5cp4pjj-zsngjfrnfAqBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Atqdrt0U6vst7Ya2A3ap7uDVW5i1mRFEZCLZF4fG4yqtCx8WckQm-cOs202Uh6Nif7j-FYk6Mtf8mNHq5WA25NW55XG5OPDZVzTTlyvSTxwtzaRrngm-CSG1LM3GJnEhDpUQ4HYjVFdSshrmP_piYYIBAOabRrSgK6NrS9fNDkF1CRzTkNIjwChTUAblWFCXe4cZv6BDiYDposclt34KYx-_uaqra7oBy_mb9UZWg5UDVq_5t3YNJA-ftV-NBi57TIn4hwW2DOJN_PWsTJ4Zmi1gjDztPeXoNFriIQrzKcGqzocjiqAmrMKRuWxJwyVfaNIjyWjxHgtII_0Q56frsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AA_U4AlyHBmyvsS__lAm1JNbh9uahKGZcBDtKoI3WPJSYeE6Lw3mORNm61JfGF_CuwQia_lDvM7swbIhMepMV9cdWjsdT9DpDBsOCPqB5yrBcueqgLwOyF4WiWe-jMyxxhf0Zk4TkVIH_-RJ_M1dEi6eweu6SN6ci8IKZyrzsHOWknofFxA_bVstcM_LXFaRNTST3nKDARwJQhCxGIZt3BUxzopaJ-T7ERoS7hMd-zgMDTs4fPnPH7Evwkkv3x1ZozkrBlkzk8bWuHr3l5vX57kr4bZz_Yfp2GN3nPIxsGHIN-NqII0TL36lXHpEP5_tpaBdOMgyHkKYudfjOoejmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
صدای گراهام بل پس از ۱۴۸ سال پخش شد
🔹
این ضبط ۱۲۸ ساله روی دیسک موم، به دلیل شکنندگی بالا با روش‌های سنتی قابل پخش نبود؛ اما فناوری جدید بدون تماس فیزیکی، اطلاعات صوتی را از شیارهای قدیمی استخراج کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/693017" target="_blank">📅 00:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693016">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d44abee247.mp4?token=i-9T6ogYSmZSsjozNx3n-csdGphYb0oM4A13xnZFCkdmHSlQV0p8clMjYHDSd9XRfjvM2gu09YL_MI6yC4aamDvUAefy5XmSwnm_2hPPJ19T7VDDq8kvUMr3zOv4PZVaZIAKDAPqKdpDrp3siFHMCXthEE9x-MpXE5W7I5dcp-oz6L_94MJyX8bMT-aJ6rNrjm0aIt3QbnXBKLtHpnmOH7IE6v-MUHpvK16uSoAZQzLteq4CK2CGleVbGwxfCLKnjYwkSQVOuXT54pvpyF4z3_P-TqIWrtGMbmCzNySq-GridhEy_vOOBEy7mUKv6yP9UJkav9B7WzUDecQ1mBfn5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d44abee247.mp4?token=i-9T6ogYSmZSsjozNx3n-csdGphYb0oM4A13xnZFCkdmHSlQV0p8clMjYHDSd9XRfjvM2gu09YL_MI6yC4aamDvUAefy5XmSwnm_2hPPJ19T7VDDq8kvUMr3zOv4PZVaZIAKDAPqKdpDrp3siFHMCXthEE9x-MpXE5W7I5dcp-oz6L_94MJyX8bMT-aJ6rNrjm0aIt3QbnXBKLtHpnmOH7IE6v-MUHpvK16uSoAZQzLteq4CK2CGleVbGwxfCLKnjYwkSQVOuXT54pvpyF4z3_P-TqIWrtGMbmCzNySq-GridhEy_vOOBEy7mUKv6yP9UJkav9B7WzUDecQ1mBfn5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: مهلت هفت روزه به محض پذیرش پیشنهاد ما توسط آمریکا آغاز می‌شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/693016" target="_blank">📅 00:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693015">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751466ca36.mp4?token=lnd3d2XfqXTRPb4bfq24a0NrdV6KhTFGo2qPm82-BHg9JMB2C4hK4GN6wsYlXTaqkAv_JvgsJFMJztU2flt3D3crz1PXCJ2eHyQtnF9lDmiSz8FUjRtJpxvNoMaaKnwHvXjk4g-gKnvpNDwZHwJtKiSXa9a6vFVvm1TlYB5bS7KsNwTVh4c8DKwU76I1r29__dc3kUy71WIzB33tOaXlGW9OLlprkP1cvLmr_bmeryn30HopG-D3-qnHlIfA1Ulc_Km6RVfwUIjFeC-jSZtLAgEvBHhdPgtycq0CfmC5i4aT0who957r72xsog1iSOAjwhAcUv4c163eIqRHhtY2fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751466ca36.mp4?token=lnd3d2XfqXTRPb4bfq24a0NrdV6KhTFGo2qPm82-BHg9JMB2C4hK4GN6wsYlXTaqkAv_JvgsJFMJztU2flt3D3crz1PXCJ2eHyQtnF9lDmiSz8FUjRtJpxvNoMaaKnwHvXjk4g-gKnvpNDwZHwJtKiSXa9a6vFVvm1TlYB5bS7KsNwTVh4c8DKwU76I1r29__dc3kUy71WIzB33tOaXlGW9OLlprkP1cvLmr_bmeryn30HopG-D3-qnHlIfA1Ulc_Km6RVfwUIjFeC-jSZtLAgEvBHhdPgtycq0CfmC5i4aT0who957r72xsog1iSOAjwhAcUv4c163eIqRHhtY2fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سامسونگ قابلیت‌های جدیدی برای ساده‌تر شدن کار با گوشی معرفی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/akhbarefori/693015" target="_blank">📅 00:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693014">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
یک منبع ارشد امنیتی ایرانی به المیادین: خبرسازی رسانه‌های غربی در رابطه با مذاکرات کذب است
🔹
ایران شروط ۷گانه خود را به طرف امریکایی ابلاغ کرد و توپ در زمین آمریکا است.
🔹
دلیل بسته ماندن تنگه هرمز عدم اجرای تعهدات از سوی آمریکایی ها است و همانطور که پیش از این مشخص شده است تنگه هرمز با توییت،خبرسازی رسانه‌های نزدیک به کاخ سفید و فشار هرگز باز نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/693014" target="_blank">📅 00:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693013">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
پزشکیان در دیدار با دبیرکل سازمان ملل: پس از تجربه‌های گذشته اعتمادی به آمریکا نداریم
🔹
ایران میز مذاکره را ترک نکرده و خواهان صلح و امنیت در منطقه است اما اجازه نخواهد داد فشارهای خارجی این کشور را به تسلیم وادار کند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/693013" target="_blank">📅 00:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693012">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4921ce8ad.mp4?token=i6PNapm4IcoEm9f55riRVfPH33ty6aOUgQElYiIDG3_Cc-ErO50IqzTSuOZRSEJsaCJjRS0-iKf5PhmJ2CeOpiLC7l8K-uX6mw7p2MsffSY6mKT-m2QjDzprWU5FjlBhhVa6baLEAjIYJ2sEAFWeqvZjqdPCDT9mjf-cp_bK8gzdxbjnK2GdZzWlvIT0nawgbXUPdVZ4C7P1aG-UWh4BBJ_agesIjaUbQoLbWeVlV2f__LNMnuWzRSquE8LS5xZrFtUbDTQb57NVYVrXGOX-NeUOtSbWfuNLm7Q1w5OgvL3itLCqWOlFkUhVGiQxGc7l5NK5hcqJomS5IIXfl9wkcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4921ce8ad.mp4?token=i6PNapm4IcoEm9f55riRVfPH33ty6aOUgQElYiIDG3_Cc-ErO50IqzTSuOZRSEJsaCJjRS0-iKf5PhmJ2CeOpiLC7l8K-uX6mw7p2MsffSY6mKT-m2QjDzprWU5FjlBhhVa6baLEAjIYJ2sEAFWeqvZjqdPCDT9mjf-cp_bK8gzdxbjnK2GdZzWlvIT0nawgbXUPdVZ4C7P1aG-UWh4BBJ_agesIjaUbQoLbWeVlV2f__LNMnuWzRSquE8LS5xZrFtUbDTQb57NVYVrXGOX-NeUOtSbWfuNLm7Q1w5OgvL3itLCqWOlFkUhVGiQxGc7l5NK5hcqJomS5IIXfl9wkcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔧
دیگه برای هر کار کوچیکی دنبال تعمیرکار نگرد!
🔥
این دریل رو می‌خوای؟ قسطی هم می‌تونی بخری!
دریل و پیچ‌گوشتی شارژی ۴۷ تکه
؛ همه ابزارهای ضروری رو یکجا داشته باش!
💪
✅
موتور قدرتمند و شارژی/ مناسب باز و بسته کردن انواع پیچ
✅
ایده‌آل برای سوراخ‌کاری چوب، پلاستیک و فلزات سبک
✅
همراه با
۴۷ قطعه کاربردی
✅
سبک، خوش‌دست و قابل حمل
🔥
قیمت قبل:
۲,۲۹۸,۰۰۰ تومان
💥
قیمت ویژه: ۱,۹۹۸,۰۰۰ تومان
✅
امکان پرداخت قسطی با ترب پی
💳
پرداخت درب منزل
👇
برای سفارش و مشاهده جزئیات، روی لینک زیر کلیک کنید.
https://memarket24.ir/product/brief/46482/180124/</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/693012" target="_blank">📅 00:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693011">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7ec3c93e1.mp4?token=C0aeoM6SlOpqelSNIek_ofppIdZsAZEolWadg4q_-MOD_6ghK3spFRfXOIplVY_7172qxn_BrDnMTXEpvTzoZeAhbVe8l5PUeSCEeWqmSnp2r9CXpl_Ufj_hbKXWdp54KovOZ-4lhGyCOkfCGmNJyZABAWR8MdunvCuhH2gMNXctkcSQF4OU-mK_Xd9vHmtdpWlBjQq_obNs6mkyHmTGvno6sqIySYmlRn54KPKdfqklaxnheqzpbTpLLU-dT32OD_szpJin5eiKnToPDb1HIixr2Sshkw2WCd6VHUyw4EEc9pWAnnl_hj2QYx-f-A2c4e_NVPUZVlccJiQ4GJhnOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7ec3c93e1.mp4?token=C0aeoM6SlOpqelSNIek_ofppIdZsAZEolWadg4q_-MOD_6ghK3spFRfXOIplVY_7172qxn_BrDnMTXEpvTzoZeAhbVe8l5PUeSCEeWqmSnp2r9CXpl_Ufj_hbKXWdp54KovOZ-4lhGyCOkfCGmNJyZABAWR8MdunvCuhH2gMNXctkcSQF4OU-mK_Xd9vHmtdpWlBjQq_obNs6mkyHmTGvno6sqIySYmlRn54KPKdfqklaxnheqzpbTpLLU-dT32OD_szpJin5eiKnToPDb1HIixr2Sshkw2WCd6VHUyw4EEc9pWAnnl_hj2QYx-f-A2c4e_NVPUZVlccJiQ4GJhnOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با این قابلیت رایگان ChatGPT، هر دوره‌ای را با هوش مصنوعی یاد بگیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/akhbarefori/693011" target="_blank">📅 00:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693010">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toYfMR1Hj5g_KoTMT1dKhKxwGGZlnCz_jg4sAZ0Dwh_V-tNWqDD9pYBqz2OU33hTMpKHDTWA5xZCdOliB1WD616_GgZiZfL5SGySOwvU1SNW8dowKL6_h0gOC5ZOz-IFY6hFJXz3C6FwzP1w9vE0dEirEkwfPcFjVunNHUDCciiqWazappxct38l2YOBykQqtxM8pGyjPBxVV4BVupk5MycH2HQzdGlUFf-eCiflINqXhyhV6CQNi_IDJaJvjXvUZJfonkIykW1WBJvK0QnzaiPw0xK6ObJH3bOSuUZkLUz9CIXBLysp8ILKW0gR8ryb3y93ib5zZq5LBoWXMo7pzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/693010" target="_blank">📅 00:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693009">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
عراقچی: در نتیجه اقدامات آمریکا و رژیم صهیونیستی، بیش از ۵۰۰۰ نفر در ایران شهید شدند
🔹
اقدامات آمریکا و رژیم صهیونیستی علیه ایران، نقض آشکار حقوق بین‌الملل است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/693009" target="_blank">📅 23:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693008">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
عراقچی: در نتیجه اقدامات آمریکا و رژیم صهیونیستی، بیش از ۵۰۰۰ نفر در ایران شهید شدند
🔹
اقدامات آمریکا و رژیم صهیونیستی علیه ایران، نقض آشکار حقوق بین‌الملل است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/akhbarefori/693008" target="_blank">📅 23:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693007">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ki2W5CuV8KOhdXN0O9_hW9auspSZz0V_A4S_H8nlu2m-2yOrWWdvcg131vFh8nwMOMypOMOHKLFVKR40nXhHr-aBrNm2iJaOSTToq214F2PWfjM9ACh_vgQy77UVCZQYoVuhD87cAzzqqOijDQ55fDCWJsk87FLhfUQhGO44auKkMjqPUp2g9nSwI831vcOQesSM2SBDqD4r9IKXnZybj9_RmwTA8GrthUN0uGlrCfJ7fI6Dm-x05CMhqH1lABAB2Gie_M6viuo5gWVoOkTzTvFJ9xdnpZlq-6XQaLPY_rzDycWuAk4tsYBP5AH6WE-pV56PHt3_aOOZv5vLyxyixw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
♦️
سی بی اس نیوز نیز با پزشکیان مصاحبه کرد که جزئیات این مصاحبه بزودی منتشر خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/693007" target="_blank">📅 23:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693006">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c113eb8d81.mp4?token=C11hqzqHwawrD-OnJ9ddZJ2odPtUAA0VUuMBOGzJ9Y0MzVXCLOQ8UlaVcXxvdmAc_POl8QHh4yxZ5gLI5nGWi4oRBIhUlCMGCkVAXDBr9IF5ecS_rzDcn74ot0FMMs8K9vHKtuCt4CJ7aGy9hTyNlUDKXz8E6LuUjTm3QJmKPd6RG8BvlXb3CYjtKJ0o8IH9yLuSKtDxyxP_6z34qXV7diBTUmx6z2B9N2G5cVYPsHFfST52AbPZpiR2PLF87IQagBzVbKj4nwOaqyLFWvFlJS9FAiqbY9JDoo8Paw7PhiESOCqfyxORGo5UHasc1585p2TLpcTB6RP9_BTxcwcaNGDbEVC80wa5pEvpH_j77jev0s3V4WcvP78uHpipu_xsT5sIoLWYxL8H-HsEtX6VsulIa3z9Pd__bhydtBT-WynHigCYRt5JkWkyBi5TOaCvJbk_xOENb3eSqdcNtCjG0GzWdEJcA7INpq9QWvS0sMsQ2_eNtouQmG3z6FFhYaG7g1wczM9AREzLWL89tKOuxpEcz6HrMnjrblutCeSARklvrmHcq2PPU6t-UzETzKhqf1F4KHZCcyiPPtk53VDFs1MAqEIypSzFgL42uIEavapGAKcLM3DHHyqvmhCHZsPQVS2Zcobz5ID8Ld07Of7pZSlyQZFNKc0y0a3C3k1BFQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c113eb8d81.mp4?token=C11hqzqHwawrD-OnJ9ddZJ2odPtUAA0VUuMBOGzJ9Y0MzVXCLOQ8UlaVcXxvdmAc_POl8QHh4yxZ5gLI5nGWi4oRBIhUlCMGCkVAXDBr9IF5ecS_rzDcn74ot0FMMs8K9vHKtuCt4CJ7aGy9hTyNlUDKXz8E6LuUjTm3QJmKPd6RG8BvlXb3CYjtKJ0o8IH9yLuSKtDxyxP_6z34qXV7diBTUmx6z2B9N2G5cVYPsHFfST52AbPZpiR2PLF87IQagBzVbKj4nwOaqyLFWvFlJS9FAiqbY9JDoo8Paw7PhiESOCqfyxORGo5UHasc1585p2TLpcTB6RP9_BTxcwcaNGDbEVC80wa5pEvpH_j77jev0s3V4WcvP78uHpipu_xsT5sIoLWYxL8H-HsEtX6VsulIa3z9Pd__bhydtBT-WynHigCYRt5JkWkyBi5TOaCvJbk_xOENb3eSqdcNtCjG0GzWdEJcA7INpq9QWvS0sMsQ2_eNtouQmG3z6FFhYaG7g1wczM9AREzLWL89tKOuxpEcz6HrMnjrblutCeSARklvrmHcq2PPU6t-UzETzKhqf1F4KHZCcyiPPtk53VDFs1MAqEIypSzFgL42uIEavapGAKcLM3DHHyqvmhCHZsPQVS2Zcobz5ID8Ld07Of7pZSlyQZFNKc0y0a3C3k1BFQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ مدل سس سالاد متفاوت برای روزهایی که از سالاد تکراری خسته شدی
مواد لازم برای سس سالاد اول:
🥜
۱۰ عدد بادام زمینی
🫒
روغن زیتون ۲ قاشق
🍋
آب لیموی تازه یک عدد
🌱
شوید تازه
🍅
رب انار یا سس انار ۲ قاشق
🍇
سرکه بالزامیک ۲ قاشق
🧂
کنجد یه قاشق
🧂
🌶️
ادویه نمک و فلفل
🔹
مواد لازم برای سس سالاد دوم:
🧄
۳ حبه سیر تازه
🍾
سویا سس ۲ قاشق
🍇
سرکه بالزامیک۴-۵ قاشق
🍯
عسل یک قاشق
🧂
کنجد یک قاشق
🧂
نمک
🌶️
فلفل پاپریکا ۲ قاشق
🔹
مواد لازم برای سس سالاد سوم:
☘️
جعفری تازه
🌱
ریحون تازه
🧄
۲ حبه سیر تازه
🫒
۷-۸ عدد زیتون
🫒
دو قاشق روغن زیتون
🥛
۳ قاشق ماست پرو
🍋
آب لیموی تازه یک عدد
🍇
سرکه بالزامیک یک الی دو قاشق
🧂
🌶️
ادویه نمک و فلفل
﻿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/akhbarefori/693006" target="_blank">📅 23:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693005">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔹
از داغ‌ترین خبرهای امروز غافل نمانید
🔹
🔹
ماجرای اشیای نورانی در ایران ادامه دارد | آیا پای سلاح‌های لیزری آمریکا در میان است؟
👇
khabarfoori.com/fa/tiny/news-3247768
🔹
آمریکا و ایران به اتاق مذاکره بازگشتند؟ | خبرهای ضدونقیض درباره میانجی‌گری‌ها در نیویورک
👇
khabarfoori.com/fa/tiny/news-3247729
🔹
جنگ هوایی ایران و متحدان آمریکا / ایران به فرودگاه‌های کشورهای منطقه حمله می‌کند؟
👇
khabarfoori.com/fa/tiny/news-3247842
🔹
بن‌سلمان خواستار ادامه محاصره دریایی ایران شد | چرا کشورهای خلیج فارس از ترامپ می‌خواهند فشار بر ایران را حفظ کند؟
👇
khabarfoori.com/fa/tiny/news-3247829
🔹
گوشی ارزان شد، اما نه برای همه | بازار موبایل در دوراهی قیمت | پاییز متفاوت برای گوشی
👇
khabarfoori.com/fa/tiny/news-3247770
🔹
صفحه ویژه اخبار جنجالی خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/693005" target="_blank">📅 23:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693004">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
دیدار پزشکیان و دبیرکل سازمان ملل در نیویورک
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/693004" target="_blank">📅 23:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693003">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
سخنگوی سپاه: تا تحقق هفت شرط ایران، تنبیه آمریکا ادامه دارد
سخنگوی سپاه:
🔹
موشک‌های ما قادر به نابودی پدافندهای چندلایه آمریکا هستند. آمریکا با وجود بزرگترین نیروی دریایی جهان نتوانست حتی چند ساعت تنگه هرمز را باز نگه دارد و کنترل آن در دست نیروهای دریایی سپاه است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/693003" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693002">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f901180784.mp4?token=EU-avO-nhXDP3AgElZafwflPPqh5mvqrMQCONXc47UU-8oivC7XBIuwABHYKRcQbZME8T-fEp3N7nUH30unpQk79FxRI0FZLqVwCNK1PJRolYaHzuChyiQDKhCcWkhxhnU1Qdz50_0mRTnXW1W_B93KzllRBR-ifWcYFa_xB4QDVUUh1K0EkQIqjVTOA3O-9mSwfq9ndT-TED9cSDI-blZgksjwxMey3xj6AED2H-8fLlrSdtZ1t7DZ5QJOEBHo0oBjuTIYMwWeWSt_SZHi3shq2GpS8QhCZuxV7hRDNkbQRKssdGVkPxKRbkINAQ7_gDxQxCKRSsLX_-3t_KIBjGKnBM91jjMarLl6Rggwj-4hI4PkOjqX5r-TStPgYNnY9d_LKwuwaQiGHbf_4P1gfXxocjNXgOmJPSSr5cDzlbELAWoT-u_RHEThOXbWKNmJUVYPL_wwJxj_-0YWxQcHJvlD_qQNyG99eWKdGRh8qSxR3-Fanelg4KoG0zrb_bIPRka3rk_KPGREwIQT2B_tfoUbz-t9c8XacSZtyqDfGmj1P4suWYE8LYVDY_d8c1pCvJvfZ3_8khuiFgB3fhEGA1QRV9gYM9-JkBjAV5W64ab2liVTU1w4iSjRyaLrswdzEMg0GoBPV3VyYClby6Bm_otAaqNc2zqqC2RJJNTj2SmI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f901180784.mp4?token=EU-avO-nhXDP3AgElZafwflPPqh5mvqrMQCONXc47UU-8oivC7XBIuwABHYKRcQbZME8T-fEp3N7nUH30unpQk79FxRI0FZLqVwCNK1PJRolYaHzuChyiQDKhCcWkhxhnU1Qdz50_0mRTnXW1W_B93KzllRBR-ifWcYFa_xB4QDVUUh1K0EkQIqjVTOA3O-9mSwfq9ndT-TED9cSDI-blZgksjwxMey3xj6AED2H-8fLlrSdtZ1t7DZ5QJOEBHo0oBjuTIYMwWeWSt_SZHi3shq2GpS8QhCZuxV7hRDNkbQRKssdGVkPxKRbkINAQ7_gDxQxCKRSsLX_-3t_KIBjGKnBM91jjMarLl6Rggwj-4hI4PkOjqX5r-TStPgYNnY9d_LKwuwaQiGHbf_4P1gfXxocjNXgOmJPSSr5cDzlbELAWoT-u_RHEThOXbWKNmJUVYPL_wwJxj_-0YWxQcHJvlD_qQNyG99eWKdGRh8qSxR3-Fanelg4KoG0zrb_bIPRka3rk_KPGREwIQT2B_tfoUbz-t9c8XacSZtyqDfGmj1P4suWYE8LYVDY_d8c1pCvJvfZ3_8khuiFgB3fhEGA1QRV9gYM9-JkBjAV5W64ab2liVTU1w4iSjRyaLrswdzEMg0GoBPV3VyYClby6Bm_otAaqNc2zqqC2RJJNTj2SmI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روسیه انبار مک‌دونالد را در اطراف کی‌یف، پایتخت اوکراین بمباران کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/693002" target="_blank">📅 23:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693001">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
وزیر خارجه عراق: با آمریکا درباره مسئله تحریم‌ها گفت‌وگو خواهیم کرد تا امکان ارائه خدمات به پروازهای ایران فراهم شود
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/693001" target="_blank">📅 23:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692998">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCrUBLWEYnCzT6TqlTVZ6SHOKbqnetYN8-MnVh-IOv1B2zKv-5DHCfmLDVopzGHDHGhXEs9dL3ByYjiedI-OLZ7vW3NG4WhVKXoxtVOTxNVBxmnM3Ugk3_puopDFADU-2ZDgdcTtbiYbsRJNS-o4FHpQrr-kM6AS4gBUboDgRyepu3X6i_EhaNawWdcsTGruWWip-I2iDLkkfd98mHF8v-f70lBneiT72HNRnmOGfrrcKLz7_FkSooxMbH1dg9hXv0DI3On2wijxBwChrG5ZTBQVlP-YXDuk5JoVVteox64TvU5ywFIZQZ5vNbTWBio569LezMoVwtP6Aitolz7iqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YQ2YzfMek06Hs3VarbphES6jI2FejWCbc__-EZQMbbSQFn2GATEvyILffe6nj6-Prs4JH-RjsgPDLYR41RhLWwxwp0T4mwqmq1D3D47JMHfRCe_h33fhTLxQujJQSn-cO62jnvDPlDQ74yoG4unExv1VaEG846rePN-ZITAlqjW-Pk8ngUQ4pWkIyvKDbPQvSMe6J3raGqqaQf7WOlCfwTPIfsVF3GcLoeOUzKmN40pE1xqrwpwQot7f2HuHW8NnXLkxlmLo_q8pORBqGHcSAu1aXZ-CLsfiJcpYewXUWPFdBOIvBJmK1s2blxM_d9HvdMCuOFsmwX_G7LHdUAgH4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vF3r8JOiEGm54tyNx0xcIKE57FWahLE27wAUCUmX7dazHfi_sJaZvh7L2nk44MoB3_HqMQjp7kXsR5n0UrPwHXAkWIIHfKZZCgscKYjcx3QR6JSKyuabVxwz24r93XpaAZffy_uFbofF1G85Jlm075fxMQGFuiiqeVoLkyjC8-jz_R_Vh_klhffOiz6emhp97WVakcElBCRcpzPXH1X6q-IFkYbASUZ3IKVxE7M65t3xi4zEMXbNNSoSW8B-FIOiyIygrOdQXgGocyNn5urvjV5mDOPwJWB7uXTyalmoTlMRN98MsitA8NXVFxaPTngyAvMx0J_uc6Izc7BImfOCOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قالی قهری؛ فرشی که ناتمام ماند
🔹
«قالی قهری» اصطلاحی برای فرشی است که به هر دلیلی ناتمام مانده است. با شنیدن این مفهوم، این پرسش مطرح می‌شود که در هر محله از تهران چند «ساختمان قهری» وجود دارد؛ ساختمانی که سال‌ها و گاه دهه‌هاست ناتمام مانده و مانند زخمی باز در منظر محل باقی مانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/692998" target="_blank">📅 23:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692997">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">گذر از دجال-جلسه پنجم</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/692997" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
دوره‌‌ گذر از دجال
جلسه‌ پنجم: تفسیر زیارت وارث
🔹
امام حسین(ع) وارث فضایل و کمالات پیامبران و نیکان عالم هستند و هر سالکی می‌تواند با خواندن زیارت وارث با معرفت و حضور قلبی، از این میراث معنوی بهره‌مند شود.
🔹
صفات و معارف الهی با انتقال به دیگران کم نمی‌شوند، بلکه میراث معنوی می‌تواند در افراد مختلف گسترش پیدا کرده و حتی بیشتر جلوه کند.
🔹
زیارت وارث برای شناخت گنجینه‌های اهل‌بیت(ع) است که خواندن آن با توجه قلبی می‌تواند زمینه دریافت ایمان، عقل، معرفت و اخلاق الهی را فراهم کند.
🔹
زمان تحقق ظهور صاحب‌الزمان، با میزان ایمان، دعا، آمادگی و عمل مؤمنان ارتباط دارد.
🔹
فرصت توبه محدود بوده و همیشگی نیست، لذا انسان‌ها باید پیش از بسته‌شدن فرصت بازگشت، از خداوند طلب آمرزش کنند.
🔹
انسان باید از غرور، منفعت‌طلبی، وابستگی به مردم و ترس‌های بی‌اساس دور شود و با توکل به خدا، توبه، صداقت، ارتباط قلبی با اهل‌بیت و تلاش برای پاکی درون، خود را برای یاری حق و ظهور حضرت مهدی(عج) آماده کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/692997" target="_blank">📅 23:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692996">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
مدیر تعزیرات کهگیلویه‌وبویراحمد: محموله ۸ میلیون نخ سیگار و ۲۵۰۰ لیتر تنباکوی قاچاق در یاسوج توقیف شد. متهم به پرداخت ۱۰۹ میلیارد تومان محکوم شد.
#اخبارفوری_کهگیلویه‌وبویراحمد
در فضای مجازی
@akhbar_Kohgiluyevaboyerahmad</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/692996" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692995">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5b79d80fa.mp4?token=MypB6vmfZspXx6RY3x59yNC27q85h1yhZjAqXXcsr2hKrJHAe5baQCkTXj56JrdVq3UdpkJPFZJ0A9zfIh0o71iJnn_ri43t8uraypl1AXSPO4H1yCZn6w2IOUcHX0tz5MlfJWtiC25Eqcg2UCHojtlBFjqRGcaTUl6jtnvvVoQrsnBB4Zdekq6N2sQvpgejNrFPewbpRwPSIOI_kz5ywh6JP2MkdH8UOkwIKShA81JgI85RpvglmfkqgaYDZWUZColtbZjhl-STko_rJCzy5x3TyaLKCRrJSlDzDzmYAeODG7KcdzTC5WOASy2YzhUqNJ4sQ7WJZ9b7fZffu9idUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5b79d80fa.mp4?token=MypB6vmfZspXx6RY3x59yNC27q85h1yhZjAqXXcsr2hKrJHAe5baQCkTXj56JrdVq3UdpkJPFZJ0A9zfIh0o71iJnn_ri43t8uraypl1AXSPO4H1yCZn6w2IOUcHX0tz5MlfJWtiC25Eqcg2UCHojtlBFjqRGcaTUl6jtnvvVoQrsnBB4Zdekq6N2sQvpgejNrFPewbpRwPSIOI_kz5ywh6JP2MkdH8UOkwIKShA81JgI85RpvglmfkqgaYDZWUZColtbZjhl-STko_rJCzy5x3TyaLKCRrJSlDzDzmYAeODG7KcdzTC5WOASy2YzhUqNJ4sQ7WJZ9b7fZffu9idUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجوری سایز پاتو اندازه بگیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/692995" target="_blank">📅 22:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692994">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0yB4du_VZ9SYdtcrouq2Vxnu0oFYWLJFJJVLRQPFw4lZAMkxgPK5hXFnu0kZykIXq_BiFqETBU4BTUroEVNP4d1WDvVzpiTK_d47Hwif5jn2hICCjTsbngTl4QE5VLv_WvF0Y2XklmijM-quUMaNPBDnMasNJPTwutF-Had2X5Iu0pWCER_-xxLfnRLjH9VMbSFvWf199NLVVYAIhZoI7C0iZSss0RLOAz_RtHcfQDk7p5sRj-fledAjwD6rwaNDrQLedW3Cj9hQT4REiMysG6v8uHXaEJhu-yLUx0QveN6agnZeCbsfh88gxJVreyi2ROkWUWzWGK1RUqMIgwXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت مشاور فرمانده معظّم کل قوا خطاب به نخست وزیر عراق: مشروعیت از واشنگتن نمی آید، از خاک نجف و خون شهدا می آید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/692994" target="_blank">📅 22:51 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692993">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRGix58JnfYaTXNVlxAqU3yx2RY37tYWfVEDjXppwO41Yr7FQPacLHPj2WN9IkqI1XcVqeVvchQWGKwo4CCuIPI4hjbKqPKa-_cQNlkWqskLi_YAfNQHPsCzcu4zj34XIS-JSEFOt6ruv3KKb1RENheboHvyq87KoCQekRsErhpMRrwXFnMOsQ8IuqhgFK7GAU_a6nqUeQTKrmfoNyTKaZfWeAHHwlKm_5f3vWFfdAhmjOi0bEP5V36lmfFNogbrdl8d0NQd0XjdonRZ44xjtQr5w2wlDgCvdId0q8GVcF32uCP5Yb8IwCI-L5iY-No-_0epxWXhIn4sG0EPEXnGfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دبیرکل ناتو اعتراف می‌کند پنج هزار عملیات هوایی از خاک اروپا علیه ایران هدایت شده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/692993" target="_blank">📅 22:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692992">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8nU3IhGXtjM0RWNST4N5Wy5AQxMidcEQzAQCeGLi73EiWlbqEUkGpvQYF-5PNaX7KfxEFUlrYh3bMGwOMB1tpwl__AkJOhyJx7_cX0PSvOaVJDlzZ0wGLvJ_JQDW5Jv7GUcuxi7JnGJfCs-3CQ1_D62CmjAcrUcx_x0AZrSfv5kV29ygVs29rdzmGqgAjJ3liR4XdfQ2QcsRCwQqVvg1WiU0_hPof0GwHe8FtXtYskpadzXckpsBA2dB39WJgb07HLLVHQbmEM_DK8p6Vd_gB7tXEO3mmIwRGqvoUtDicMhplC_iD1byhYRtOXBYk5kK2jaSqmNzoZKvOYSyQb4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ هوایی ایران و متحدان آمریکا
ایران به فرودگاه‌های کشورهای منطقه حمله می‌کند؟
🔹
ایران در گذشته نشان داده که به تهدیدهای خود عمل می‌کند. در طول جنگ ۲۰۲۶، پس از حملات آمریکا و اسرائیل، ایران موشک و پهپاد به سمت قطر، عربستان، امارات، کویت، بحرین، عمان و اردن شلیک کرد که این امر منجر به بسته شدن کامل یا جزئی آسمان این کشورها شد. ایران همچنین توانایی خود را در هدف قرار دادن پایگاه‌های نظامی آمریکا در منطقه به نمایش گذاشته است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3247842</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/akhbarefori/692992" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692991">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxpBc9GRsELynpAOUJFQSIGh-1OKzBY3YXfncVACMciMOowUdYKFl6y0BMwhXziLrXNk-UrAwpITk6iJGwOQFuphp_oZzoG91VhqwiPi5ZuaFIzXFgBydYZnP9OGOYahtRlx_8lGTwkvMHfhE_MRTKbku-BbMv24hztHPTcj44_epLOpsWhRXR1dNVfgkFocVo-oqkb-BAldkNDZE2N9JKv4o85M-lk59dhD-EP6slufdfZJ5-SXJjEh47c0JiGWJRC8V7o5MgoaaLbyV29IT5WE5yBXOIOCavMjC_tp9a__q9OHhKM-6M9bObdicHC6mVS0zjyqWlwkMXuR0T0Bcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ایران بر بازگشت به تفاهم‌نامه اسلام‌آباد تأکید دارد
پزشکیان:
🔹
اشتراک‌نظر تهران و پکن در ضرورت احترام به حاکمیت کشورها، کاهش تنش و صیانت از صلح و ثبات منطقه‌ای، مبنایی مهم برای همکاری‌های سازنده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/692991" target="_blank">📅 22:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692990">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLSWIFda9P2eFppvrCTRnjzykyVDBxBnKRWL4NxZiGRXT3xz8VIW-UNfxZil2CFq_O_Z1lpVJJOm-FcU2NmF61zQyVzILc2lUg5M8iOlxaoh2MvbVLXQu2kMTW7mr8YpnW5ruBX2v6DxXySP55ng4-EZmMm4_i_w4qcIa03fhgsouCYqlENpXFz-KPIaM0Xn6FpRf8wRm8FNCkNPUieArpKZQzftMb11NaIBaPpdz-XDtB4u5neKuJbZFu99i6j-NSdG6Drf7OaWTpnXMLhbdM9tnt0TOoqZl7dX55ynIzukK5FGEfWOr7NIgJxr_5oXIToCRxJgXy9WUgnuI2plWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۰ نشانه‌ای که متخصصان مغز و اعصاب می‌گویند نباید نادیده بگیرید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/692990" target="_blank">📅 22:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692989">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN-vbfxQOt5BpgoiNXJalzkABlPoAf5yXfVOq2-CoBBGTt7S3WW5DCNLl5eORoH60AJbqdv_4Su8FpQrae5xNQ0lkMIzD3CVDDlijNSiq-ZjUZVLLlALL6sL8mSz9qnMv3noYfSgMws7HHuKYtT-GbuAZMWiz1vPKYLAeEpIYuQ2MiXI97_T8zXNdbBQoiJK5SJizY5Ps4FN4Ovn8my7SSOGBhR2Ecoe1U_tJcUopDpPzBl6iSm4Aj_cgHAgr7S5iEIKYzD8n7T5XSga-JMKFaeRNGdWQb8ygG1_YrAX8Lprlt2zQKaJOlcKorClcVrvKx-hFknKcdhlHKsMK_XLwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منبع آگاه: ادعای آکسیوس،فاکس نیوز و الجزیره دربارهٔ مذاکرات ایران و آمریکا کذب است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/692989" target="_blank">📅 22:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692988">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRVlW3jQBd35YeaJzcJpKT19SnHE0hrcON5q8kXIG7BoZ1uO79B5t6Z4COpo7IPPBeJdUSJEZF2fEyRkJrNekFlcR4YQUp5RYiY1xHhk_GW_jzqjtZxctDzGTgpSR3Hod0gYR2_K_jiJW5xoGBfpdZahs1rciSTlQ6DcBvXJKm6DWEu_Ulp3twVYH2dQvI5_js3j6OyhAXADLPdhz7AI4K23-IvQ-z2pzrOOtNhibezSaNZ5KF1oqINU2F4mKXUSMqLLwvfuakKab6CAEAovKSUX5WcpsvzfvwDhmaEmbx6o-vPCQBiNxkuRmPjOdpM_8ImcpeBpSM-URzUFpdqDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درگیری قریب الوقوع است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/692988" target="_blank">📅 22:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692987">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
کلمبیا به طور رسمی روابط دیپلماتیک خود را با ایران قطع کرد
🔹
کلمبیا در این بیانیه ایران را به آنچه «ارتباط با گروه‌های تروریستی بین‌المللی» خوانده شده متهم کرده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/akhbarefori/692987" target="_blank">📅 22:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692986">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQUJwMyZoHS-01412aTw73VffOm73cgH4flBtpdvYt9uALI18fztZp9m6MsgJagNco2zwoFEA9qOzlWtB36IMBO3m-jmlYETg1Ya7ICb1IL8u0mmc29Yp-cWYA92L3jNgf6UJFJaWm_M6Sk0mTOsVKb8eR2e9jFzFYiCExh8Pra2LdQ1UH0ynLqt7n1WnFj2S5WfkerSWiuh9D4z6uN7YtdpUj4tv9K1BHuuz5Psoav8scpF-g8Sp62frw0Vej5JpR3eHIbcy484gn2PNsTjTwupTdyV25945q23yj2KM_NMY3f2OdRXpj5MgVxDD6bKebVnHx6Yi5I0-4_Dd9HIPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کمبود ویتامین D؛ علائمی که نباید نادیده گرفت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/692986" target="_blank">📅 22:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692985">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
صحنه‌ای متفاوت از آغوش گرفتن در یک تئاتر که در فضای مجازی وایرال شده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/akhbarefori/692985" target="_blank">📅 22:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692984">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
دبیرکل النجباء عراق: اگر پروازهای ایران از سر گرفته نشود، از مردم عراق، موکب‌ها و زائران می‌خواهیم برای اعتصاب در فرودگاه‌های عراق تا زمان لغو این تصمیم آماده شوند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/692984" target="_blank">📅 22:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692983">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
الجزیره مدعی شد: مهم‌ترین مطالبات ایران در مذاکرات کنونی: رفع تحریم‌ها، لغو محدودیت‌های صادرات نفت و دسترسی به منابع مالی بلوکه‌شده
🔹
دو طرف همچنین درباره ترتیبات تنگه هرمز گفت‌وگو می‌کنند؛ از جمله امکان بازگشت به نوعی مدیریت مشترک تنگه توسط ایران و عمان…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/akhbarefori/692983" target="_blank">📅 21:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692982">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeDVZZiF4v8Guvs2t0hHTxeH-0IQ-o-CnlYfgwfBbDsxK8Svct_WPUm4-d2OQrXVzf1hOw9EPkaIGFSS8nPluhpag-V_Cz5BOVpn3JSWo6h2uIyf1T2uozObfAm1iCRo4xCdvyV8F_cT3FS5o4tVD06ZimnvF3KGMM3G33YqVsw5k6BBN2aMstPZr-kTDTttR51lPkPzlmkkDqPCt7Mq-vGWRwVgbP24JCBOnwRpdCsdYRVZdSXfmt2TwO1PMkYdeWpAX08xHXwATH2ZFDZPlnDp2PcgGRN9gR5A-xjjxVe906ogCVlAMT4rV1LERlNx1tAKuJDp8PVnNQ4AiBxL-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متن یادداشت پزشکیان در دفتر یادبود سازمان ملل
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/692982" target="_blank">📅 21:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692981">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28bae1d8c9.mp4?token=u1z5ixKJwHWP5fh20kZu9ckCc3zgLUdKrT65GYBcB9mrm2LpI7Ui9mRdZhCgXZX_1-XTDjQATDbiSvXDwkAJMnB0aV7wlrbyh5wzVHLVr2o9-FFRt6otq294yS2PfMxq_VSuK-tEakJjCGSsTcHw83rMlPKqUKmZVnI9WBYEODcVNR7IkwRwTKVvaWFQz6ko9v6dzJDId4mb-uQLQy0MFO7h6B4jK0GpJ0RPFuNwOBTpgSbK4SJ7J-btpbAYJKev_ziwaPeC43Bci2JZe_sK3VEDT3aogk00y21o55LJJna5gEeF5_r_oZRf0nxtCXKBD2jLqW4PE9E0gha1pkYh-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28bae1d8c9.mp4?token=u1z5ixKJwHWP5fh20kZu9ckCc3zgLUdKrT65GYBcB9mrm2LpI7Ui9mRdZhCgXZX_1-XTDjQATDbiSvXDwkAJMnB0aV7wlrbyh5wzVHLVr2o9-FFRt6otq294yS2PfMxq_VSuK-tEakJjCGSsTcHw83rMlPKqUKmZVnI9WBYEODcVNR7IkwRwTKVvaWFQz6ko9v6dzJDId4mb-uQLQy0MFO7h6B4jK0GpJ0RPFuNwOBTpgSbK4SJ7J-btpbAYJKev_ziwaPeC43Bci2JZe_sK3VEDT3aogk00y21o55LJJna5gEeF5_r_oZRf0nxtCXKBD2jLqW4PE9E0gha1pkYh-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت غلوآمیز شهباز شریف از نقش ترامپ در نجات صدها میلیون انسان از جنگ هسته‌ای!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/692981" target="_blank">📅 21:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692980">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59448866a1.mp4?token=LL7FC_eBbJuACGnFv0qPQEz4hUzSasY_LLlFblT3eBg7R5CMyuvhVjz4-MFkWaeztZSqqUbL24IP5NIQvK5-LscSeyiSQCox045AESAt9EMJGkoXxoE8uTqR12cfWQymvx8hfty4eHgXHXmox-Bogoitv4NCv06CnMab9TpPlUw5eJVnpbPOLqwdd7d2kqt6NiShHtNKPPG6sGFzieR3eEFQa0seLVc_bgweTjtdgZW6HWgJQ-aFXpVs980rPAT7LghsFM1geA3CPEpl8yMtR2q2zcfwqvs61yQb1FasJsWTlLqkj-wDMj1uqtZB9j3rtZZz8Lmqfo7lzT30LUALiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59448866a1.mp4?token=LL7FC_eBbJuACGnFv0qPQEz4hUzSasY_LLlFblT3eBg7R5CMyuvhVjz4-MFkWaeztZSqqUbL24IP5NIQvK5-LscSeyiSQCox045AESAt9EMJGkoXxoE8uTqR12cfWQymvx8hfty4eHgXHXmox-Bogoitv4NCv06CnMab9TpPlUw5eJVnpbPOLqwdd7d2kqt6NiShHtNKPPG6sGFzieR3eEFQa0seLVc_bgweTjtdgZW6HWgJQ-aFXpVs980rPAT7LghsFM1geA3CPEpl8yMtR2q2zcfwqvs61yQb1FasJsWTlLqkj-wDMj1uqtZB9j3rtZZz8Lmqfo7lzT30LUALiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از تجمع عده‌ای مقابل منزل حسن روحانی و درخواست محاکمه او!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/692980" target="_blank">📅 21:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692979">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
اختلال در چند مسیر ارتباطی اینترنت ایران ثبت شد
🔹
داده‌های پایش شبکه در روز جمعه سوم مهر ۱۴۰۵ از اختلال و افت کیفیت در چند مسیر ارتباطی اینترنت ایران خبر می‌دهد؛ هم‌زمان، اختلال اینترنت در استان‌های مازندران و مرکزی نیز در سامانه پایش مستقل آی‌اودی‌ای ثبت…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/692979" target="_blank">📅 21:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692978">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
پشت پرده تعلیق پروازهای ایران به نجف   یک منبع عراقی:
🔹
نخست‌وزیر عراق دستور تعلیق پروازهای ایرانی را به وزارت حمل‌ونقل این کشور داده تا این تصمیم به فرودگاه نجف ابلاغ شود؛ با این حال، تصمیم‌گیری درباره پروازهای فرودگاهی در اختیار سازمان هواپیمایی و وزارت…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/692978" target="_blank">📅 21:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692977">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/619837f067.mp4?token=dp5gdnligE9WDet4NCwAoSEA2XbPmCFM4p5EPiTh-FZto77bq2W9i3w6Fo4I6VDCBpbJuhe5eNP96M75vFK7xxuL19jujM-r9xcEV3gGznPZC7i4lZi2Mgn7uXv4M-RxSqShYx2-d8C1JZ9LBA-0xoEb8ywK3ymSRcZf7iyCKvtcs0Vfa_VggAHSrOjL6tDI6U0IjhWDzCy7gk0XZsRfi4zt3Rn_RsVhzXTj8d3m0ISzx6HCM7UPV_gDDKTErUX6c4f0Qu7b1iqHK3rEAoaB2QAllwrHsoD2STbonSaEqkfDe0pACXzOXVuLPse1H20dJNuSNkw4ZKwY6uCXYep6ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/619837f067.mp4?token=dp5gdnligE9WDet4NCwAoSEA2XbPmCFM4p5EPiTh-FZto77bq2W9i3w6Fo4I6VDCBpbJuhe5eNP96M75vFK7xxuL19jujM-r9xcEV3gGznPZC7i4lZi2Mgn7uXv4M-RxSqShYx2-d8C1JZ9LBA-0xoEb8ywK3ymSRcZf7iyCKvtcs0Vfa_VggAHSrOjL6tDI6U0IjhWDzCy7gk0XZsRfi4zt3Rn_RsVhzXTj8d3m0ISzx6HCM7UPV_gDDKTErUX6c4f0Qu7b1iqHK3rEAoaB2QAllwrHsoD2STbonSaEqkfDe0pACXzOXVuLPse1H20dJNuSNkw4ZKwY6uCXYep6ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ژاپنی‌ها قاشقی الکتریکی ساخته‌اند که بدون نمک، طعم شوری به غذا می‌دهد!/ دیجیاتو
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/692977" target="_blank">📅 21:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692976">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/749678b1ba.mp4?token=cJZ6xjfeWfX7zxRwnPiuFpDg9kPdEVJyd5O_6Rjd4FmsPEY-86sjhayUoCRtdgnw_p5GGopqEPQMzJp7puy9p1t9aGwAOqy53WnHa187Jx-GuBQEVbURbqWWETRCKoepvRHprxxdeJFyHbFUwV4NZ6-Cu8MnLJ74VcK9t0skVBJofXA7RY8VdbifgGfq6t8ou9ewA9OMqmGqV9EMI-G_WNQqKHjZJK6zykrcJs0Dw4YzzyXVWRLUcnNUvXnCmHiv-ZMM5lLCTmUA9BzMSEJXSMjtV0TRqL3c4Udx4jBHnnkVflW1FLRvjT0AXkOLnsLCDLaMkc-rNnoke53kFORcGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/749678b1ba.mp4?token=cJZ6xjfeWfX7zxRwnPiuFpDg9kPdEVJyd5O_6Rjd4FmsPEY-86sjhayUoCRtdgnw_p5GGopqEPQMzJp7puy9p1t9aGwAOqy53WnHa187Jx-GuBQEVbURbqWWETRCKoepvRHprxxdeJFyHbFUwV4NZ6-Cu8MnLJ74VcK9t0skVBJofXA7RY8VdbifgGfq6t8ou9ewA9OMqmGqV9EMI-G_WNQqKHjZJK6zykrcJs0Dw4YzzyXVWRLUcnNUvXnCmHiv-ZMM5lLCTmUA9BzMSEJXSMjtV0TRqL3c4Udx4jBHnnkVflW1FLRvjT0AXkOLnsLCDLaMkc-rNnoke53kFORcGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست‌وزیر پاکستان، شهباز شریف: تنگه هرمز و باب‌المندب شریان حیاتی اقتصاد جهان‌اند؛ باید باز بمانند و حامل رونق و پیشرفت باشند، نه میدان جنگ
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/692976" target="_blank">📅 21:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692975">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ادعای سنتکام: تاکنون مسیر ۱۲۲ کشتی تجاری به سمت ایران را تغییر دادیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/692975" target="_blank">📅 21:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692974">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVNREOT9fD0UVVk6CjHY3UGksH3MkEM1F8cFFHkkf0noDv51xVipgBLnby3aX3ZHlM5a8hH8qWkGDZTnI1bI4GTPcRaCSap9AJ7b_v3Ny6hKgy1mU5eu-PIacqOU91MD8ZNMrtinnvjfSytTerxbeGebork-EUqwLZ-oV-9xJir9fVHcrUw6T0gLTb92QTGe53n4D5nXMIb5dYUMjptQF8VQuwOe9IjA44Uv7L3gl3MI_PB_pbNjVqftpQ1bGgvLQNjRPk5dR7PaFhBXsWbjPj5XHDpAl7EzVOJ4aaiH35vFrXhGkyXebGTXB8QC3syrV-KNwIiR6WD76H7AflNHKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک کارگشایی نگهداری طلای میلی را منکر می‌شود؟/ میلی اسناد تحویل طلا را منتشر کرد
🔹
در پی انتشار مطالبی درباره محل نگهداری طلای کاربران میلی و این پرسش که چرا امکان تسویه دارایی برخی کاربران فراهم نشده است، امیرحسین صدقی، مدیر ارتباطات پلتفرم میلی، با انتشار توضیحاتی اعلام کرد که طلای کاربران به خزانه بانک کارگشایی تحویل شده است.
🔹
روابط عمومی میلی همچنین با اشاره به نگرانی کاربران درباره وضعیت دارایی‌هایشان اعلام کرده است که این پلتفرم خود را مسئول پیگیری تعیین تکلیف دارایی کاربران می‌داند و موضوع را از مسیرهای حقوقی و اجرایی دنبال خواهد کرد.
🔹
بر اساس توضیحات منتشرشده، میلی معتقد است میان اسناد تحویل طلا به خزانه بانک کارگشایی و پاسخ دریافت‌شده از این بانک، ابهامی وجود دارد که باید برای کاربران روشن شود.
🔹
رسیدهای تحویل و نگهداری طلای کاربران میلی در بانک کارگشایی نیز برای بررسی عمومی منتشر شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/692974" target="_blank">📅 21:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692973">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sP7b3-flL51M9JYTGAQaH5pJr3rFPENFfm9bmJhfPIEX2azhU0VkyJ4E72lmfqwBVHz1wsq7D2GmyDuniH6-5IZeIswHxP8NGORcMhpx7wR7syM0O3mxN_4ljS4LDrg7MpHAAfNWH8D0-huToxwD0wUR2puFm4BlgG6GvU6NzhlRgt3ZXqL8liEOHigCGutXCKThfz2098bj6oYASTnn5l5Giaq90x0tfLkDXCmivRV-my5YShWJB1vi-JkcEZNChDoWyO9_hsUz1V4msGil9hTH16kHXBDfCAETQS-Va0-n3VK8dTSiqBEem4DPbNEif9kuT4VGsYeWE7fsd7TGvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیدار پزشکیان و دبیرکل سازمان ملل در نیویورک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/692973" target="_blank">📅 21:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692972">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
جزئیات جدید از مذاکرات ایران و آمریکا به روایت مشاور محسن رضایی: آمریکا فعلا طرح ایران را نپذیرفته/ پیشرفت ملموسی در مذاکرات حاصل نشده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/692972" target="_blank">📅 21:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692971">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baf527f29.mp4?token=CS18gEmgVBTTIJCVhCI7iCIvpni7URKKtkqJ9olSr_9JRkzwRNWlADxyUt9bAtL8LDlBa8OOYHaUEX5irWQsrO0Dwvd5RTwH1wEJ7mpAHaUMNbpHJQEGGbO5DHlHyqoL9q_d8VIUTb-mGL7l1w9yXP2Y8gmzakEpsqCioH-1pacicxuUo6cBXVtNiTJ9NBliAOcIAOiT4XDpWisFUuZsVFK9oA361KH6FpY4Ky755SyQLc15k-dMfMmVH6tRtR1eI5HKvpYAYD6gSqGE_9pBAd7Ijg3DiLkJX8AiT0FEZIK41-GULRDJ1NRlgt9Xs4AzvrWbWLUfmH4lPRCh3srrVah8-dldhNhng8qdOVuHiZ7d5odlSJhFx3625vV3PzQcOHj5ywmY0zNIaOaohI9Mdf4bhrN09-zntVNJL-C3tEWn6L1VNGYSDylYaVtm6h0RZfguhmVt949svnRFPa2qNgnsu4HlwTj0Kism0ff4NxkK765XCGF7V6EXoaXKaJiWW-CbA5R_gYsd_XDDfHKayVZ9YKN7vHkHR4p6DCvyC-L1D5mKAdYogmaQXfDtUI2jWRjcNPfF-jXKmKfNqi2CK1GNvTCAWEQIFJsL_RGqJE1nHJ2VRk5rmjnhH8PhXkR5mdc2ktE9RK49Ks3szMzWOBNquAmf-nyvo5K1JYnyftE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baf527f29.mp4?token=CS18gEmgVBTTIJCVhCI7iCIvpni7URKKtkqJ9olSr_9JRkzwRNWlADxyUt9bAtL8LDlBa8OOYHaUEX5irWQsrO0Dwvd5RTwH1wEJ7mpAHaUMNbpHJQEGGbO5DHlHyqoL9q_d8VIUTb-mGL7l1w9yXP2Y8gmzakEpsqCioH-1pacicxuUo6cBXVtNiTJ9NBliAOcIAOiT4XDpWisFUuZsVFK9oA361KH6FpY4Ky755SyQLc15k-dMfMmVH6tRtR1eI5HKvpYAYD6gSqGE_9pBAd7Ijg3DiLkJX8AiT0FEZIK41-GULRDJ1NRlgt9Xs4AzvrWbWLUfmH4lPRCh3srrVah8-dldhNhng8qdOVuHiZ7d5odlSJhFx3625vV3PzQcOHj5ywmY0zNIaOaohI9Mdf4bhrN09-zntVNJL-C3tEWn6L1VNGYSDylYaVtm6h0RZfguhmVt949svnRFPa2qNgnsu4HlwTj0Kism0ff4NxkK765XCGF7V6EXoaXKaJiWW-CbA5R_gYsd_XDDfHKayVZ9YKN7vHkHR4p6DCvyC-L1D5mKAdYogmaQXfDtUI2jWRjcNPfF-jXKmKfNqi2CK1GNvTCAWEQIFJsL_RGqJE1nHJ2VRk5rmjnhH8PhXkR5mdc2ktE9RK49Ks3szMzWOBNquAmf-nyvo5K1JYnyftE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیشه‌های شفاف و مقاوم ساختمان‌ها چگونه ساخته می‌شوند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/akhbarefori/692971" target="_blank">📅 21:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692970">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBt0CZp-TrbmWxDyu2oQTuQCr9v6tTjprlW-B8bL_RMdh_5i93x2etFuRwYsEgBSCBpnjbhYhBjgACu7ASQtXaW1NuFIqORTIAcoi4VrS-njIo6cjK96GICMGdxP3YoHi0aG_qhkCsz_-KN0__Ak5VMwywpMmrpf_Og2tH34UaJZjvIKB_9SHYU33G3Oi86NQg_DgrBJMnv7QADjqZvdsk8f8Z_KoskuIXcjdDSowy3iLnnsl57kg3pjCnjV8FzbEu76NOSaFDpAg1qljL9RTCsn_sNSWiGN_UopddsjCzEa3TzT5cvvOGHcEoeZfYx8BFiKquVoOuJhcBRiG53PZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره مدعی شد: مهم‌ترین مطالبات ایران در مذاکرات کنونی: رفع تحریم‌ها، لغو محدودیت‌های صادرات نفت و دسترسی به منابع مالی بلوکه‌شده
🔹
دو طرف همچنین درباره ترتیبات تنگه هرمز گفت‌وگو می‌کنند؛ از جمله امکان بازگشت به نوعی مدیریت مشترک تنگه توسط ایران و عمان…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/692970" target="_blank">📅 20:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692969">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b2a67d87.mp4?token=cMHmJ-Dfgl2791mEDqelNLYFH-45k0s9MD0GfzT3i7YoWFOW_6eg4K2RWBcnhDgplQyk_hBYJvnZvzULwSRy7ctTOzefCJkftZEGFUTPv--Wh452oche3wJW7RLPxdTXPySU4_D8d0iwgN2vHP88Vz0bbj4fhKMuf088QCCmT9h3S2JgeWpp9pgLRzUI_7seju4wW7NFcn77m1xqeyZKSpNHeGRXPUtqhbI88x5Atyo9Kk-VZaBjzvp3bQmtqd6ZjRPqdbTgiplSvWWo5k3cly3Ag5nAEdH5hqjiCUfhx12PgJVHiHr9iUb_LH0J1ITmZaX55GiGOTvb1sg7ymuId4q4HJzxekGAoyRzg9uQK5FrTFXM8RoUMadNzNNNEU4bimi0oUfp8OEI83VLhJPS3HlyYoiE4V6-2QB4ZDwQtstZsco8If9B9sp8K7-L4_lqZxh8KwaLSOIwAEzCTGmIU3-RG_KXHkLZsrURLQ9Lf2qE9Vrr1-4mJdZ47mrsdD8AkSYIfIYqx93wAmP1NWdnjrPyoMyWUAQeIwsngtDP11qv04TIuowBNnyVEOuvZpP2VZ0YABZjVBX_bMOhxlOmDc0ziXGihM_HmCIV01LIDMx2Kg5FO2gIyHVX1FFsPiZWwV9WkqX3HR5bue-DuHDqKv2-IHOcK6_IeaGgh4B8ERA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b2a67d87.mp4?token=cMHmJ-Dfgl2791mEDqelNLYFH-45k0s9MD0GfzT3i7YoWFOW_6eg4K2RWBcnhDgplQyk_hBYJvnZvzULwSRy7ctTOzefCJkftZEGFUTPv--Wh452oche3wJW7RLPxdTXPySU4_D8d0iwgN2vHP88Vz0bbj4fhKMuf088QCCmT9h3S2JgeWpp9pgLRzUI_7seju4wW7NFcn77m1xqeyZKSpNHeGRXPUtqhbI88x5Atyo9Kk-VZaBjzvp3bQmtqd6ZjRPqdbTgiplSvWWo5k3cly3Ag5nAEdH5hqjiCUfhx12PgJVHiHr9iUb_LH0J1ITmZaX55GiGOTvb1sg7ymuId4q4HJzxekGAoyRzg9uQK5FrTFXM8RoUMadNzNNNEU4bimi0oUfp8OEI83VLhJPS3HlyYoiE4V6-2QB4ZDwQtstZsco8If9B9sp8K7-L4_lqZxh8KwaLSOIwAEzCTGmIU3-RG_KXHkLZsrURLQ9Lf2qE9Vrr1-4mJdZ47mrsdD8AkSYIfIYqx93wAmP1NWdnjrPyoMyWUAQeIwsngtDP11qv04TIuowBNnyVEOuvZpP2VZ0YABZjVBX_bMOhxlOmDc0ziXGihM_HmCIV01LIDMx2Kg5FO2gIyHVX1FFsPiZWwV9WkqX3HR5bue-DuHDqKv2-IHOcK6_IeaGgh4B8ERA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردمی‌ترین شرکت پول‌ساز دنیا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/692969" target="_blank">📅 20:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692968">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3ozC39XhtLzhKpLZ_0D_OsEVp5QsaTtTk_G84rrUVlcX8u75G05GQNPN3vP1hqdIe0sHYwWFH-g4w9KnGYKZYWtfOqwDPGN-1qGrT08Vk0iK3rqakf-tN-3pMAXOmoPJOwfZgiAIkWmo8tvIT7dK9Ym_PRteSUrlsGhPprmKZ1uw9z24zDZExkGOYSqbUOPl82qH0FWYKQznfrkGPtxGmgQZl3R6HyCOx1rs-45Z5gNTa6vg5RBm2ysGTW80D-9VKDduE2gz5oPS4ltvGKH46DgBFaI0vEfAScelRU8IbjDCEDgSebzkz423QJT4XkaXroK5pgIFHBdrUaFzmmvwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فروش کیف‌های اضطراری در آلمان از ترس حمله روسیه
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/692968" target="_blank">📅 20:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692967">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c17c8f0887.mp4?token=AS8D7hmfLnz71v1aePm4-ZMqTfZHn9XuopQrQgCoIScRplp-y_GslRzrYc4-CQGS20fBw61-VtEKEXbkLruO_2OQ2wZaIOgaeAG87nmzTXGvH1lVgNRop-lC3-nHPwcNEmC26J9AL3RCsP1Ys86pwfIWIUn2lmGnwoqTx3uyep92auRbO7c2Y9f6Fn0XQGQoESDAm7JvLDszjecvRFNipn-_iMkQmzcXIYi9rqhWKWWYdMOS5cweY18lkKEedx2otxnjkRqmhMQt-a0seP24cogu04Lt9i1vJEbNXh559F44BI9EYau8yr6HPOJUoB3SELvcdRgD2hxIc6SSHPgLL2LCvAPD9ssqzdC5Z5KCEMHiCJ6SJ_ZIgB8VdBDKjomgpjQK8Wu_kAW3m9nS_kCB3B9qaxz2gs3W6yYE5zVxhvGFOPCSnpbaY267_jJqVeAPMrdQpYIOqeEx5nGWxaGYlV8KthH9i49PPwkV_qvJ_3vdMR_DdFxq6duf8UCM68bjCfbFCxivJOURDFrq6UdVpkZTob4XU_cMXS0XfMID0gt7u_iPM0U5HBC7t9QvFU5p5iSJbM4bpNcQiGhE9dgkVnqYDrXRjH7GttTqG7IAv5AptFkKvWyLwz1t523P7uUTgS1YvNvEdJTRPOOxFPVbVrvyIv6EmAC10ECjdkxDe_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c17c8f0887.mp4?token=AS8D7hmfLnz71v1aePm4-ZMqTfZHn9XuopQrQgCoIScRplp-y_GslRzrYc4-CQGS20fBw61-VtEKEXbkLruO_2OQ2wZaIOgaeAG87nmzTXGvH1lVgNRop-lC3-nHPwcNEmC26J9AL3RCsP1Ys86pwfIWIUn2lmGnwoqTx3uyep92auRbO7c2Y9f6Fn0XQGQoESDAm7JvLDszjecvRFNipn-_iMkQmzcXIYi9rqhWKWWYdMOS5cweY18lkKEedx2otxnjkRqmhMQt-a0seP24cogu04Lt9i1vJEbNXh559F44BI9EYau8yr6HPOJUoB3SELvcdRgD2hxIc6SSHPgLL2LCvAPD9ssqzdC5Z5KCEMHiCJ6SJ_ZIgB8VdBDKjomgpjQK8Wu_kAW3m9nS_kCB3B9qaxz2gs3W6yYE5zVxhvGFOPCSnpbaY267_jJqVeAPMrdQpYIOqeEx5nGWxaGYlV8KthH9i49PPwkV_qvJ_3vdMR_DdFxq6duf8UCM68bjCfbFCxivJOURDFrq6UdVpkZTob4XU_cMXS0XfMID0gt7u_iPM0U5HBC7t9QvFU5p5iSJbM4bpNcQiGhE9dgkVnqYDrXRjH7GttTqG7IAv5AptFkKvWyLwz1t523P7uUTgS1YvNvEdJTRPOOxFPVbVrvyIv6EmAC10ECjdkxDe_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: ایران قربانی اقدامات غیرقانونی و تجاوزکارانه آمریکا و رژیم صهیونیستی شده است / هیچ‌یک از اهداف شوم متجاوزان محقق نشد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/692967" target="_blank">📅 20:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-692966">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
مقام ارشد ایرانی به رویترز: ایران در ازای بازگشایی تنگه هرمز هیچ امتیاز هسته‌ای نمی‌دهد
🔹
تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته باقی خواهد ماند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/692966" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
