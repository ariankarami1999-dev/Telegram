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
<img src="https://cdn4.telesco.pe/file/VodC7mPs4FrQXNI7816SdJh8oz1GJxa1vr6Qo63Hy4sSZ0Drh5plf5xmY9lEj6aY4UCtQLNcQzbxB99TAXB2qf2Wa1ra4Ka5NdmZi5S6dAwKE6OjMOiWkJgtyi7UHglsutJ2uc3YQZRLQbM4yD6hI63HLxwO1Afrrm5VVrhxh0LqRU9O7NY4_v03619P7ozwcAzfz01Az9MuhN_dZ5Q3BLgOEgxCoPYwdBY9XP4zztZDBLTL5dLe7NaGjg4H6t5sZSKnkQ6BsSYVUgOSv0hUZoPwVKE_6JlW7nICtdbQh-Eg6NocZEycvj09DYEJl0MYoHN-p_qHIro2Rf1FQ1hAnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 520K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 21:20:57</div>
<hr>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDGoEOhUoJSpSME0D2rdedMVqW87dMz7QwoFdsNUMY2U56RXVwkJMnXupD4dD1FvNx7RSGhqAVUzegooSl6r9FBW7p6H3UDR5cxbfsAndEelwvJPmSZxsD29NRqJvCh_QDOz2QhwMfR3LfN1kvnM8uc6iQ4b0N-vrzPZdzkPLXdoy9mvkFDLtxnDcjcFar3kwmynMTGTmQETBhOyTr8USH_MOunqwNTDSZsihooMkSTlGBNQClj7tFR2tG13zYE-h8UiLIUODi2Jw32ctYAbVh_KMLrD5B6PgDsCGGBStXm_NgHi6lkS5N1JczqSD4Aa1KsHP1LQMJNc31W5SAslYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=aYhi3Jr4-Ih6txcTRNPnMyv5koIprarESbuZ1ARiFaJjCLWwIw5zf8kjnFK_b37zZ2VgXASWt1UbXGaY2LetXdTZeboI6xM2za1IkmLSAm1cNA_LuYJtnvgYP9r0bhUHtGjkvhQJLHGPXXKjjHIOVFcWyVvuTl3x_4vcGluM6Tm80f1lIAN_LZM4k7gxBG__tWhQEP0F3Ebis0LSW0lvmctIFnSnWvV5RpFCt4p1hzOZC1LtrwJ8Hp919y06mbWw2M3jSPk-wi-H7LaQP8s8_410Aco4tyOwn3tWL7TxHgI4-WQ-KvprYeNr_7n-AF2Ps7n6sVadMpNgaJ-pRCtM6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=aYhi3Jr4-Ih6txcTRNPnMyv5koIprarESbuZ1ARiFaJjCLWwIw5zf8kjnFK_b37zZ2VgXASWt1UbXGaY2LetXdTZeboI6xM2za1IkmLSAm1cNA_LuYJtnvgYP9r0bhUHtGjkvhQJLHGPXXKjjHIOVFcWyVvuTl3x_4vcGluM6Tm80f1lIAN_LZM4k7gxBG__tWhQEP0F3Ebis0LSW0lvmctIFnSnWvV5RpFCt4p1hzOZC1LtrwJ8Hp919y06mbWw2M3jSPk-wi-H7LaQP8s8_410Aco4tyOwn3tWL7TxHgI4-WQ-KvprYeNr_7n-AF2Ps7n6sVadMpNgaJ-pRCtM6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQxExJs_l7fvykYjTNCGkFga7I-p5HeXWPA7XTgmVy_Loq3z6EkZ6SbDrIWaNpH_20KVz9xEZPqB7xVsfkmX7xPY5wRrjmXW3YggkhRS86mYIHF5CnkoeDmCf4C3cnk7DWly78e1UdM75zoLMJ_1dsYDCRh0ipXYn1CsiwfDa8t67qFfyHeQyDMc-UI4pzxxLorYfV8CBrkN1rCpxUOuH0EiQaE72331jrdfw1UjZelzew3La-zIwfRzmnFzAm2r6gIRRYpXVE3GUCP-He_6gMouzqKYSE51A3VODMWND5aNH5e9d3Oq9IO48UyCIAiPits5OukNQ4pdjTHEsvienw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pjmVbf8daZaPvG53aAWDKG4SjApJTHYBkcRlJKxno9iw5YcpS-RyscHTDyUuOzhENeN1VIB4lGc5vYPdW0QeTyitlBAPEBvZ0g2xwdd9mHF8WrKHHJkYl-d8Ax-Xc1rPCGw4J78mmaXCAdT6ilDuy1eNnD093oNZgwyp-hnbNT_yDxKSe0me1FU1gaUR0H0xQxT1cpDWdQ058iUtFT6be4qv4v-2tnJYOJ5ceZCxk7_5W_8KT8Pf6TWlFUtsfJVEPFkpopYRXtIZe-EPPKzA_w5YmNng6LkItWOQPbFYcf5heO9E1O3KAzqQT6478SV3ve_fFwAjTWcZuUj98jScWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnNForisJUhOT97zrMCx6oG6s2PkkmV6yWW0Y-7Klo7_boEoJbY1g3KmiYnAUzlw4X0qfWcb2V_zsBVi_Ec44921A0i-ak5sdp0jJy1NN2lhXq3mJPc2z382O9GEHtZY8tk3eAnSDFfGU5s7Z_NPiaqQDAWqSL0w5lsU7D_CJXfhyUl_8eW2-pdyRPk2wBJNnPXjykJvNf7fEdIusw-kUj2LXAVHQEj0JuF9HRRR_C_hhegtOf0CYPGJf8_Jc0IThQ7whjUGhieJvMV-LfwZsQFowsc18wxJhdhfBfe3uIIy3Tx5oORL_wC2PT6gMKj9hZaHxImiz-IysKU1LkLk2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG_CfQZZdGhQRrRAko_KQhxGfnz5T8hj3lRWy0gtcpTAEKaKSJPaZUEd9PPVtZ3BUVqbDGioA39QoSoZZ5_nrTR_4U_llnYOuHGz-c13YCVTxMXPy4wa2nEfadqUWnJLnbRJ6_l3ntg58kzCy-zihC-Ga3MJcrbm1EUWBktxz1oVMUdS92TpVhI461aQrX4nRIXfF8r1yJQg9zIL_5lYbKwouB7WwzZ3R0PBuTeZh26JPvxJH6ooqf31BztRckzgr1ff-nLtmHTCHI1icz2SfPFTv5cxIYljtXG4jCQOu8VF5ko514Yebp9iwjrN22HBblxutIgDS85DQYdT0c_3Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_QZM0YhUjDdVkpJWBLJNO_3VDNpfQtN-fAHdGvpF2QgIMYfeK9Kw_qs5DK7QuLFdc_fgaSz-0jD0lVKGhZfhG7PHk26qh1tbzDUTub2bqY_1-Wm0g4s7SzlqPXGIz46ML3SHKcfPTVWXYAqSdZelNmNd8cU9GCOK9m8mqPBsYKux1ZDn5WI3AWtWHd8EcR9PrsrbmS8M3FqFLIV9NzWg5VB2NQDNfFerA9sIe8GU3RT2trDzMpOWNsPv98ZMxYXeuFcwtFeskL-XkqWMBN9Y5IwDYMR1qn41JZ2JsDqOdxe7OgO1qgYHv_Usn-V5u4h9JGAeHW8LR_kWmUHKEgzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMVZdFKdARi07w1A9uHepQRT-JjXq_HwJXYajhSbWRv8xkHii8Pdwfngj9unaUzx7aqah5OpgHo4rXCpBaL7-uA3-S-sV9lig1cMw_BhvXQgraTU2Mu0QXsx2w5gTDsTXgmnWjZwtENis0NSMjpR18Vc1gaNV13N15WfM3_GNpUDzoMULcV8EfkIoev0i2JMAhPzEBmLVn79mQhuLeC9_om26C54ACVKNdCK3DaVYYyAtWjsPzkk4aR1F_K1JByxGslnG70Ye6C3V6822dDyRz5atdK5pRrJDu-1weghGX3792Vjx-AHCqlBxJ40JyUQAQG8GMP4fx-gVy__qVB51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlhteimBIhnON3duFv-NsFXpAwlgOHUBmpIPGCmgB8Y9qDRcZI9Ycg067BPUEzcO2T7fciJ_J2dodyHZB8rX8kJYLXKBIWsLP4KS-A4yKvN72fppMDWmss5hybI6RbOx7FZblHNZsFHX1oagkLDiN8CkZx29d8UWwkxb5zXOrQUOQNZLdYMtX0VUfpsqN0Vl_viU1vAMps6TOtvavVrbQVLUGQWnDkGXyjZ4htcwjGVHNHQ6RFRcvynm4CUhCliQVFGYbVXr-UZnXa5Ek9VLO2QDE1a02oNd3dwTQHxy6TEenf0h_YaK-M44MxyaD9Q2U-eN6brIr11m5ttu8fjguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26073">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFlit5GmicNI0LXSf1MNSG79SETdHdzF-vqtz1JbO-tDliuN8QshNi62FE4o_iImbdaJf2dbqcTqv1e-ckFGS4rhlGV01N_TKgD9tLJ9ZaECRsDA2F4HObCuPQQ0oKYMWVuk0G0uBwl1MDbLqRkDFc1GCGNJpOiBoAMt-L6pEH3Higec08IfaYxNW_2VdN2iyUTIDC0U53ypWVE1Km6Mt4Adje_fcQa43iKzCtJMrYzXp2dbWgwRKtWS7s8y8kcxuo3UsfLZ3PxQ7CAIMeU03Pqo-VojBvm3zU89k1JzvooFKK7J0O-wgzbz9mJaWNHvR88HKq1cbPc7uSHGpgsGNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین
🆚
🇪🇸
اسپانیا
📅
یکشنبه ۲۸ تیر ۱۴۰۵
🕥
ساعت ۲۲:۳۰
🎁
۷۰۰ دلار جایزه
به صورت
FreeBet
بین برندگان واجد شرایط تقسیم می‌شود.
📶
علاوه بر آن،
۱ گیگ اینترنت یک‌ماهه
نیز به برندگان واجد شرایط تعلق می‌گیرد.
✨
همین حالا پیش‌بینی خودت را ثبت کن و شانس خودت را برای کسب جایزه امتحان کن
https://t.me/betegram_bot?start=p10_r4EF37DCE</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/26073" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIJ_A7nIS7z_iyNiiGfV-zEPYijwYD9G0jImazrNbHLzPclkc0yGaHfoKZ3meiqhwCAT7csg0KloGXZT4wn0ISjzP_FPdW1aN4qkNFa4H6i3JgEh7mrYRwgDRg9IAGPrbK4k-9LMd1UQQPHE83AnyqOM6Ey65TNXW8NAhtksWY5NWmV1HgKPKGJeKgNdRvkGUukAR5-3_9HjzTAc7Hn0b9PQg2-Xfg8i411kvkc2WKZMOEm1UZfI4NolWchJAXDnu49Z3UO-QBUC43EgiH0ngQg4LRbF2z1tTUwd-vgAAmk9jNfaJWc78RjeHA28VH0OFYpSB-sgOrYuYdb_xvDJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCiShKAuVHvPnloWd7Qbc8XTLgt5qONMWoX_az4N44VTXOe4N5Y4el3OUf5kcSmE_w9BEMQ0-t8tcsDjj-7kVUiFU0mJ-aH_F29xnqYUlw4cjIcpFS3TqNqCJKjGMdnMM-X8Nk7-Z7t7HO37FOXt9k4dl4wAVGOQV96CS-fMhMq5LQBSTUP96hsSix7eu-iN8abErO4Zy1mhHzDkLcLt_qdgbkwfZuoX8p9PvNbXUk8jXyrkj4Q8ek6l_cIy6rt2naXlWPBE26LO8l9kCvIAW5U5mLh4HeT76IjaD3XSI9FaBotKv_nDIRgoESl4Q7vkzVH5RR6Zxa71U3S4VNws4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=XjgLeiBNg7QMFDZijG84OWZL_pyVR7F3JfVnykLM2K4fuDGPLL4QmCWHeBrygQDxwrscHxd2TnJtzkZfawZp8xN3iX9iBoeH6JXG2GVsKJEEUgR3TTMlMqVYyuUHhjCQdUSUGsx-CLudsWY8xjm-FEobckUr8TrvGJDs8So9tXSwLloye5xbFDEfc7lmJxL-ilB2_OhmyqzxT9EhiuY-QjwC_UEYjrjJ0MxBAPfx-BPnl60l8HysmNkZYWAmiaqw7uKDQCbfEA9GAyqp8YO85DyDj6nW8eNdFj3NA61-8D1oOwkMROJZgHjku_aAc2sQLVzssKT4wPWX1Xjr0HkDFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=XjgLeiBNg7QMFDZijG84OWZL_pyVR7F3JfVnykLM2K4fuDGPLL4QmCWHeBrygQDxwrscHxd2TnJtzkZfawZp8xN3iX9iBoeH6JXG2GVsKJEEUgR3TTMlMqVYyuUHhjCQdUSUGsx-CLudsWY8xjm-FEobckUr8TrvGJDs8So9tXSwLloye5xbFDEfc7lmJxL-ilB2_OhmyqzxT9EhiuY-QjwC_UEYjrjJ0MxBAPfx-BPnl60l8HysmNkZYWAmiaqw7uKDQCbfEA9GAyqp8YO85DyDj6nW8eNdFj3NA61-8D1oOwkMROJZgHjku_aAc2sQLVzssKT4wPWX1Xjr0HkDFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvyaANO9l_YlD7ax2Xol4fBvh-Kf78kxKZHI72c_bMjAERmCBroH9CoHvF5cBH2ns21TbpaF2dBEUnkgOuOPB_TxPyOzkLdXPu6FQcaEpX7w49i23jMST9B4F-Nexh2WHytgBsfF0awy8HQR2EtNVDLaD4imzcS0LoIHSLv3DyCth2ELQvIpjBBwQFMfrxfkR5HOEJcmiJicALh0QDgGpBDnEx7fKswXkbzvjpW82HjiDS3nVu4Tj6v4rXkARfZbJrkAQ7gFDICw4bWQGnd5yDeDO6BgOD2wnJpILV2Vdp0EqxqVnOyHT1u-E10Y9TvZNDCwkjxwH4FHH82Sufoo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsydjyRrEn_yIAZJvAmvneztY4liKv2cwALTg60oOQyk_Gv0yF8bz69Ic5a598WfTGjbAi45c3LREKPyEjvPt3kSP9gZnxYv1JqNvI2_mQAkNG5lrkcahBzn34qkmmemRkJjYXhZ72JwD7H5vPGNgY00uifNk9hiEacxmZnD8unAN4dxre4GGUfoqfA0xiBGMnmfa1A_HCnS3u0SDfXBFWfIDkoz2O0mJvI3msydd9HcoZaAOJZZG0BGQ0kZJVjvCyDBQGLh4Oz1tvdij-qdIW7S0bv5-SbrKMwsBtXmtUDaHQv8fCi_-7sAG0LzYk7nE7uHlnu9CPlMpjfJFFYipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7G54lNvPKACe2_uTWnLtGKcst4NW1eKPhSnSKrzf0S9ZoVES61_pDVcfxtlGPXlUJRruwUx78o1168sO0OACkzoSwKcczgv5TF31f7kGfm3kmu7tGlwzQgYCVFmmhQ7-U7i8f523tXXHtA10N-G-mVRXvmXdh_DMB3pSNGptKS3p2QKnqP6EYJ4qS9rr5ZOXPVwOK5ca1LkC8FT_XKrAbLxF8qkS_9SftvpFIW13umhNx7mIHCpwUJNmo7SZxpT8PMHEqHzUPgzplT1kUZlHNh509cUH3w3ignVbUOevxW_oUEBZeqwcgnamlPf4RqbguYVETKoQdbmbAsNwRzZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=lT0YDGn_xlfO1OZ36EUffmxWyZrlKpomz0m_Uk_sodQURdsShFfEhyGeQ42SX3j6d9QFdCW0MwOPknPQMBCwfoONKJ_jqZSSc046cZ8HmKWbFxFuBn5DeQ6lQEx0Y01M1_I4gYrioDfHHPGL3TSwPjxVN1KT5X7pbbmAWX5jpNBRcJPj_n9ZUFLfxHEPqAK9dPMX8tVL6Nl_z3z2DXzuMRiHUPt7s60l5ltCzHiOPGpJl2Hd-TLP8ZMM9tEFludgxWV7QWO9mCHjYF_R-5c6RSPy33NhkXXVjH9lOLrnnXY4pq9Ad_iY7ui4yCNdi4crSu6C18VPE2DXaokuQ0ai5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=lT0YDGn_xlfO1OZ36EUffmxWyZrlKpomz0m_Uk_sodQURdsShFfEhyGeQ42SX3j6d9QFdCW0MwOPknPQMBCwfoONKJ_jqZSSc046cZ8HmKWbFxFuBn5DeQ6lQEx0Y01M1_I4gYrioDfHHPGL3TSwPjxVN1KT5X7pbbmAWX5jpNBRcJPj_n9ZUFLfxHEPqAK9dPMX8tVL6Nl_z3z2DXzuMRiHUPt7s60l5ltCzHiOPGpJl2Hd-TLP8ZMM9tEFludgxWV7QWO9mCHjYF_R-5c6RSPy33NhkXXVjH9lOLrnnXY4pq9Ad_iY7ui4yCNdi4crSu6C18VPE2DXaokuQ0ai5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saNzXnbGmNQ1_FYjqjtJ0BqrujAO9h0E9P6obtW7Tuxmr9Y_93oJBqjBYIZqi5NYs4hukGzCVXDG7xyYXpBfJRvABknDaazsm7_FIdTc0vee6NMhPIZecGHC_Zhv_hZaGBb_wn-801WYfujSWoyn_JJ2gKRLtUSogXra0iPWbM5cJIifrIhJO1NYw4rnEty8m9FkBcHVCgVAP9tcnZuGZglsNCI7Ja_riVYR1UxxVDIkUISTpxzMLVD9CwBKxw8z-AxG6DX8r_ksKkAtLg9Qwb8g3qNDKTei-VnsKSmWLY8C0Iksx0RMb0bsXuiQkahdw3KJXKIDNyogcbHF6cIltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GgYX328VjNcyNHlso10Jrh2K5p_vNcqLHr9rQZkM2KpvKx1taGF8xouLHa7Q1vY3fU4urfL4inDhXdniVkO98EQysSmQzumvHf469RdwEmtJmVzFMB_yLf2ReeuuaQrj-q598mxyGcuj5wUtWzMUGND2qa1COA-HAtnlzCU8OiW_fj9bJD7Ra8VELIeHx0DvR3hPL64GNlqojdhG9UC_89xEMoMIGO-NtR3BL2h7jQJw0ER9QHDMoSVlBHNU9a0G3qCJ_Ano6P3MwbvT90Xex0KoELueO1q_J9ZCzltDIVWMkEZcraxvhd2gDzmR9YR7a25Ldt3yudIV12gjzJ833Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=GgYX328VjNcyNHlso10Jrh2K5p_vNcqLHr9rQZkM2KpvKx1taGF8xouLHa7Q1vY3fU4urfL4inDhXdniVkO98EQysSmQzumvHf469RdwEmtJmVzFMB_yLf2ReeuuaQrj-q598mxyGcuj5wUtWzMUGND2qa1COA-HAtnlzCU8OiW_fj9bJD7Ra8VELIeHx0DvR3hPL64GNlqojdhG9UC_89xEMoMIGO-NtR3BL2h7jQJw0ER9QHDMoSVlBHNU9a0G3qCJ_Ano6P3MwbvT90Xex0KoELueO1q_J9ZCzltDIVWMkEZcraxvhd2gDzmR9YR7a25Ldt3yudIV12gjzJ833Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbXs2GOh2ibErFv4_YS6Gykk5srqRZ9JMbdhVh-0Oh6l84R5Z3n-F7R2hfsUhsNnd418scIaSAAt4JWZZq4am2V13-ygX-fzBnF6XauTlPbcyEyCXRHcFf60vOJRjeYYP_YuKwETVfHovpXEPeLYswuoG0nUX9iDBvPLJpsF6CFsCJBcFAhLYuBijzQykF3rlisXBKxHxUogMA9w3UoyMyZlePgfcnKXTkZ6O-_dz8dL7rMHpJmD99Ar7zLP5sI5VDlkZ19niet1AWjX-jsYB378gQ7lwd0hDGAsc7bTBt3XfOSToathMAayzY8m56wczDD3eNc6sygu1EeDmY8lqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBPVkw31S_J18a8Caj4jal6VRc_krjCjDby2HLeQHiUgY16RvBdwM8iSmY_Gg2farZ3KH6irP69mbQOmcFs3pauzkrfUmr9oPpL_VRCa7RrlblJdYtsUwUkbx8CcbxNWirWrSpob-1SB7NrCr-ev7KqCx3d4mbUdHI4Y_2bcOnZo93hcIOfHAzKrSG0JKe1anfuL9T409a5QBcZhiX8xAT7VcHAHSw2JDOJXEWV35iCU-1vbMXXGnGUud3hH7jRW--2fI8kx_F7FgSgqjoxeni67AfabhWXhJwhxOLDxVrp5Cea9f-qk3IZSV82cnxyP_CnwblHX-CEoOTq3W1TzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVad5Z_WeYnMQaLn4zvEE13xYJt8pFaTUBOPQw6CEIMSfK9PArRyYjGdCjISHAou9lfF7HlVXfpubt6xxaRljMUbrVUC12CcXfFDkhQ2zNxoo-jO95ZCCXL7b-TFo9O_dkB3O4c--n_qZXCQFji1-FBj19sWC4wGjkT9PkKqB17AQXrYB4CAGYvp7Fvls7PEHL7E3ZxC1pMYgiDt4KrR3AWIhi0Z6wqyv6ew61p5HzqTsZDIx5XzTvsBS7F0L8Y54vFteWRcS6_7MfX0NpY1yiRWhdTzHNqzqo_BnwjnV_kgGSLrdRQUfbQoFTd9uF0SXg-ZeKcYzPdAwoSmXI1ujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=KsnVmmlDN7pefmXoO_DZUOIclmRKzIm0MvJMh9O4Wb-kRx9Co8o6ZFL_hpRV5fbb3DWRBVEh9In1PkwlMJh2TxJfIj0tzi8lckNV9ivTcQssYnBNpvfr1HBJBg5J1J2haPkNw-yBh_KLWOgKSHywi7qbIuKhI_utfAjbHzIi9VMuAEreKBxtC6jDZiXWWSLcuX3hD7T6FtdljYh8DVnLJ6X8npTfRcTU3w54zMpRFQwXMM6-bfy_2w9nygX5GdvCpdl2Gvi9Oz-3GJHTYHRnOnpS0dxOYbK23ZeAm68VJbneQGm0fYFACpgagHzhLNn5Jx99wpBUaF8HFL9tn96BVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=KsnVmmlDN7pefmXoO_DZUOIclmRKzIm0MvJMh9O4Wb-kRx9Co8o6ZFL_hpRV5fbb3DWRBVEh9In1PkwlMJh2TxJfIj0tzi8lckNV9ivTcQssYnBNpvfr1HBJBg5J1J2haPkNw-yBh_KLWOgKSHywi7qbIuKhI_utfAjbHzIi9VMuAEreKBxtC6jDZiXWWSLcuX3hD7T6FtdljYh8DVnLJ6X8npTfRcTU3w54zMpRFQwXMM6-bfy_2w9nygX5GdvCpdl2Gvi9Oz-3GJHTYHRnOnpS0dxOYbK23ZeAm68VJbneQGm0fYFACpgagHzhLNn5Jx99wpBUaF8HFL9tn96BVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsg4vBLwJ5e6BSn_QnbOQVUXyyvFSzsuEde9fMWhVvishV0AE7fSUpY0NGBBLH__uXVfKDSvQJ5rnYoQlZk-w0r2euyFNucx4fqdQ4l3hlvbpHnyOP05yG9cOvYOtI4u5F8JAFWvOeTRAXL8A1iSDE9zSJF43riJaAhRYO0WlQ3VRdH9irULGin_teD9SofD47iQWPiT9dtdhK6QAGiZ4jZRijEsc7vA-lS7qCLG4xOJEBiwV_yuL-WCKgBSNTs9DA45kIsjBcaOTyEx2AlRMsNuMGOope6xCE6KXPLuici7QpN1ynQyjEdFmuaXI6UYnCeHS7nx0XVBfzXMu_NuSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZ99USyvGhOYA53cANt1qJDNkOFRmNL2Ot-xEQiFVlnzuUXeSZvH5MJlOwU2-zTZFvUgldlznWJ2nbMldCizAzvuOuucaLVe8RBc5KmOOHi34jdK1vXKiWu27pdLeQ-LLeN6lEp2irA6IMQZ4utzqT7DvV8G1jXMTaM8pWbTGLbjs8eV_-NbeE7KP-wKwGac0aZC2eDXiSKyDgQBKPsyjrwWEVdqpUMNlQw0uDNEUlKPa1w_r3oThUmsxFtShR2qX06WynxsHSS9He8ubtPitcjAutPtE7hDiByeEzTYwupH7jUVcxJrN9Fz3dXU_0Kui0KMwK7Nf6z7lIFU8Tf3fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=BqRGnoqGZSi6Ie1mqy_t5dp3BV2HfaYlDo8vg9pNzGKEFTrKsUq2Cw2ppXYXXMxx6u2_2qGFK6uMSZwiyKFSDRJPholbc_V4J0IS7n5tLzJuvz3TS04F6d40d7K8hsLXATb7ldM5e6Ow0m_FOZlgNjg7gKzL7nNO1VOMHmLkfqfbAY8ENNxGSOe4OeCKk4bvFN9R4yzHrIIJvW1nyMxD17SpMmw-fmQU1nMp-TDw1ub30C-uKP7bp1ZnVFoPs-GgNojAWhyGvgZ6xlxiNCL6xjrEqUftsrpUWV9cHKhJLvdhuC--i0aeAoHvaQhsKrWnNwfLAbOXcHG5f2or8odcrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=BqRGnoqGZSi6Ie1mqy_t5dp3BV2HfaYlDo8vg9pNzGKEFTrKsUq2Cw2ppXYXXMxx6u2_2qGFK6uMSZwiyKFSDRJPholbc_V4J0IS7n5tLzJuvz3TS04F6d40d7K8hsLXATb7ldM5e6Ow0m_FOZlgNjg7gKzL7nNO1VOMHmLkfqfbAY8ENNxGSOe4OeCKk4bvFN9R4yzHrIIJvW1nyMxD17SpMmw-fmQU1nMp-TDw1ub30C-uKP7bp1ZnVFoPs-GgNojAWhyGvgZ6xlxiNCL6xjrEqUftsrpUWV9cHKhJLvdhuC--i0aeAoHvaQhsKrWnNwfLAbOXcHG5f2or8odcrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=RVC7KAltG8p05jvopIuBwXUZAUfMqxPGbnhgfQw8UTiTwkZ_bKsJ4BW_F5mOcqUFy0LvO2mmaeu1_xNqX3LBP6hrOoW1X2yyf71gjveVOSVPWSE37P8K7D-MP5J5DabeBBToDJeWoee0gBgweYHOeMj_FXVloBNNKrMx8zJhpQzlAelJgklmfK3qpN_Gm5dOqzP-fVHzypv06_yfa9r9pR6_cD4FqFPJ6wIh6-VtnPvughDdyQDYsUHpdEemsUxoeGrepUKXVToZ6kLkwG58Z_QQMAnz1LJ_JWC4Fgw5Sr1XvhkTSA9fwJuOx2_bqLYP4V0tsYOtzcyfJWCImeQFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=RVC7KAltG8p05jvopIuBwXUZAUfMqxPGbnhgfQw8UTiTwkZ_bKsJ4BW_F5mOcqUFy0LvO2mmaeu1_xNqX3LBP6hrOoW1X2yyf71gjveVOSVPWSE37P8K7D-MP5J5DabeBBToDJeWoee0gBgweYHOeMj_FXVloBNNKrMx8zJhpQzlAelJgklmfK3qpN_Gm5dOqzP-fVHzypv06_yfa9r9pR6_cD4FqFPJ6wIh6-VtnPvughDdyQDYsUHpdEemsUxoeGrepUKXVToZ6kLkwG58Z_QQMAnz1LJ_JWC4Fgw5Sr1XvhkTSA9fwJuOx2_bqLYP4V0tsYOtzcyfJWCImeQFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kKJxFdbnyJ6dupTscX09lgsmAFZEkA1_uD-_Z9x9jjQEdC7b_kZmSYz4eH4-3e7mcdxsfuBAeQKEzzxtk0SwULlZVOpX0K82IPwlrL1hkCZn45CaKp0Iofb12-xdLUjKGekom3KVSlI90c9DK065Mzcqxn6ze2ecE-Wctg4SFmV-9kMEJBFkzvxFbYbmqkpMajhoVfcWQNBAhErB011nRHzPcjP2uQP7H6VT_IW8C-D9-XDHf_xvOOS5029jawh7nsxvcrC82h7iITZ0Nw0n9b1fzqgMljt1H-DIS4-_d9dS5-ccAFDN-rEeWCAoBZfWThgSig0HiMDBTpKWh1elfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKSvU9_f7j-XSaEso_a6Lw2QIu1ksAm4AIIc3E13AEQ3QUWMA7sIavj_NvwYZPm9AnwlZ5yavOhjrL3FEVoacRCtGnnb6Ib-ikXzlP-EIOeXCnhpVn__fcgFWfU8pqBWskiembmExN4V98a4zm9nqvbcZwQCpqURgeWbPsuYCWtc_H_0suLIhCHPcCcdlRa3TcDAnaiv-aW6blESvKU6Usw6InwNSL0Koeoiy2mVz7T94xJOV8k-kND1LwU32Vd7ZZvlhVZQxx-nqSTR0xwu-yuChx-YvmHP_tlQlGMuQOL5eiA7T4xNbMvq7lnOMpfpEqHAn6yw0DrIB_4S4DUDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vq38ZDOVgkN3f8VwVkE8rOZX01pajxaN53NJ0tNwkwY3EMKu7eQPpSXQDNyMfHLCc8PtFK2WeiJhMBJMh5LrsjwhwMRtCJDGEimyQTqamNTGVvf7XLuQoAHw4yKjuGxhIveAg_i3qUwsQmBvmfznKc74f38iKyoeQwZT60X5YjEZZk6IFtJAhYrYEXIBSRX9_nLfVlicL-QLvaJnXQYWaZ641K2MIXa4s4kOWfrc3LyN8CUhEImRkJPG_z1VAyjrXtR3OaujuyGxsShCjCCQovQPrO1JomNyT3HhVOGJXzGzY8JOYEhL1zZlXgqnYTn8y0ivadxnYVYedwhuUCdknA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpNbmGRMPp9tbNVKh8MpMqJqKs0Rk1VE30SaHFIx_FqjpCrVQ_rYbI-gZG3WOjqKff7CUYKuxRSCRZ3-D9TyimMzULDBPVsPApxhRjFLxNt7a0yC1dMgMfiUqCq7PcqiVkuTaUiJ6ZF1EhAH4TcNmoVOkFUjT8LwVMHVIE1jetLemMuyGt9u2okDkU3WQN6qZaHp6vb77foKD_HUp99cu6mU8bus8MYQsr8ReXG5GKXMFlrWs3w2xUTso3-MAax3XybtTxmoYGv6O4w7fV7JnRYRpKdARpveL2X5_IEvBRI2SQuWdXJ3qu1_qYqf30049eg_VqiiVhMJ4dv5kTfDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwB29TmiLX5uvyVLK-QwKSpLlNdnaBbu1VI8I4HTI7zUCu8yw8w5Vqm3nyLzuibja99by4ZyUcaXDevhyEqPqfiMOIF5YGd5Sl8_BT0Dnn65qEZH6nToOmvX7mji0qFEFPDe7FwjyBkqmrltJXR86e5Dr2RGdVW0c2un7i-CHUbseXhIm6AZ4qET5MBx8yb4-ET9wT-P0M_EuUDys98bRQJ1xY8UizMacj6mfQ40Pbda2ghd6BXdhgZdwtJGcjiRUkS5FBW2ZZHaBmS4otttZUZpPdL9jiYoqzAC5Ev-SDkqqwosWZkMpv4WLaWs6JeMR4WtXjhZbR3NrWSoeuQHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2h1Tzb1kgSK72MLoVWFIpLMQ81uPwLRWsyx7lCUu3ka2urr8WCmoOH8dWVtlFFSTcyUdriwisLZT5wxY5Dyo1smPPteUGqmrJdGqiYQjp1FKYAdfbGAuFjYV_WV2zkPmUvPsQrCYOHE0OOBDIA3pMYmO3LYjcs2r5gopZas_VocuZgblwFW7Br2EdMTazRr5ncjbEH2fIQNEiiSAcm5Jh6Az-WleKOMNavxa7s0q1a2mytlgHMDMifjluJ5_MBB0OyZgoGg_Byt0SZ31eULY5shuN1PWRuMgaGbbl0N8brj_PHFLQtemilPFk4WL0FEA3yVbMUIomm-qOD5nOoKtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrUmBL0OI08C6JYdLdjE1p2ZTzItOdFZ68CHa0glmIuRsh0EewschSOAhk5Miv0aKTX9ZLlIt32ojsmpmzBgthXZygXzAQweeoFcSeeN3K-51FhP6IZd6TwngBT-UNHVtHhuEvO9vi3EYrS93hxBdOv7REConUjZZqOOt0voSqI4dr_Ba6zm8eUEbj_knWZVzRlvIgjMrR4g507vTlMv_SwwT4wKCYpVQgpWA--H9xEKtlY9Gxmj80MReg7lyyGCAZmlnv5ceIsX6S9q9XPJ0_7ozwmkNPPgvTPCRoGIqWBMLFvGMrm8koxl4RUvRYT2xafNcta2aT6FoAwLBIBusA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26047">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nApOFO_sYBbSFk_Pva2Q4q7gwvAAYI9OyV0x3qbYPJqgT8Ps6wT1lNSTQYg45fCXUSCz21s6MTYF80hPHEaA5f8vEMRUdqhwngRynlP8N0l9mn9UqI1jrdwsTG9zafDbQXhzhtEzaWTyoqfxJgjrNvwCr0MeV3kBXf89BJXjX8K76v0UOvONPOfGi-kdmKBKn_05jhuRU26p3zh_pxEoA8TM1hLQCPYzltZezoPrqoIyxNPgSgbWPNlSogriC7JoRXodoFi0bq4i3GUSlgsj-2DHMyicKlQE7dcsIpWUR6RFPwTVTMo4_WdgKRBwZQcuHy2lYZVuynQg5B2qPJhcLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26047" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYNoVGU2_YBIlp7PBA8RLt8p1lE26kXSsLAcywSRjA0luwxfprcjuWNM_-oCkqHN5LHiIvFMYLHyPjuA_uuHYTL6NCYQXZ_B7WTTjX_m7TIDcrBDW2bgUfFaPpyg5rDN_JZEeb_E1UMzhbyKyWDh4rDMIIno2VTEM971aOpDf4fdC8VWGhbivZbZEFmltNtjMabfoWSXF_3vaRc6HYL-CFRLxqVRw5wbQd0jvE83LD_rcidsXytUFV0zamTarnPq9Gh6PXYZ7E2uF3RZPekS6NN7KFYBXX-4RbbZUH5sZH5lf5pcUbnwKYCK98FEF15yVemaBrWXt-z9O1MzcO9MkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgFaoQX9ImNhn9TSi1O-GFrLWQK5hSqwSbOjps3a_J5aVUIE4tyq9SMrWQtHFDKUOA8E-L7NNAf75AA2TMNRcJZtrEL5KJIiFot8zS8LUQnoHzLlMrC0E5B2ei8A_obUpsce-kbdzXpkzgoR2jehYyIpcivKMYjSkRRpGOijoufasTxZXn27w21oQdigqDQMKy1WyhRmJ0mtP20of1wXWwB_PFTt52cfAi57i0X6OtlU_2Me4JOCelWl16ip87-7aM0LQmLpTgtR6MxhZ9nRhMOO5fcBB-dpTOGAIaNyWHX2Bq7atXw2xNVT_EOPcsg8n0tStSWNpWi5EaeOJlB89g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26043">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2k6inj52MHQE0E4qqpkQyDFXLTIMtc4Nb3AfM6YA2q1ztjgeLRQRcJ454zA7un74k_jAMULHpwDun6x-xmyVJg_4tMRl7EtWICnLF1vQxmmWwyAF7rESatGVIhI4vHBt5IX8Vu0uqKa2xX11faQSjbiAdxB_nCdoy2w8_0q-S7m0m8UXuLs8vwfQzOQjRogOJPI2ImILH61ni6Sx7Pr_A8pzZigaYdgRQHRzaP-eQt7OuUR5rRvd1omKp_iZ1Kjjb6ReowN9cgEul6k9gcP3DFy9gxRU0_NWruY7YlDb9lX7JcWkYIQUa47OnfjsKu91-ty1a5nw6ggKOLRAWs5Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
برای اولین بار در ایران ، فری بت
0️⃣
0️⃣
2️⃣
درصدی وینرو
🎁
💰
سوپر بونوس
وینرو
، پیشبینی بازی فینال جام جهانی با بیمه ی
200
درصدی
☄️
⚽️
اسپانیا
🇪🇸
✖️
🇦🇷
آرژانیتن
⏰
امشب ساعت 22:30
🚨
ورزشگاه مت لایف
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr28
📩
@winro_io</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26043" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=PVqA_9t-85aOVTFAk-YemeJBcGAWqIVpQYUZ17kKGAi5GP7aguVi6-U8Tz_-IwlzLnEQMn8ZdywgeKNYHm0qLUElWzPJiOwxDz0ff0-qArt8qLoi-l_cqj3CYIR9sjvMkgUGZh-Vxz9Gb9Mme2lYm12HjrAb8yB4pCEhzvhrW3t3HX0dSCXHmQuaBrbJdUYJnQ8FoUwTkntzYR7V4BBEqFdU2K44eL95hjSwDavRuLELEjV78xyU_rNMIsJE6zxukLstSZzUMbt9Al_aLeJMnJVUihMNGCELBtOHvgoq6wI710eQ45_Iy77XQDquTOgtARPEgoQkEX7_Ap4nyYtTqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=IgC5NHGSeHMOUQ-Eco8tg2D-YKvAWus2NaZWdudhcvvp931Z_ZeruWpAfbyw5nfzgxfSeq8Z1nALAJUncUpTSz8WWNnoQH85WRvqU3Tk3yNffFsX75tKieYzeum8PYOJwQyyD2upEjFhZ2_XWZ8LrgwVyXiyc7e24keqR_bC61Hl-TPA1Vgrqv7HzWwLylKHt6ih6Qzo94hmpJFsY0DkY69iHHJeOLmXNd4PNPRUowWyKNT64UdHC8IeeaWspIjtUgwzN5FoRO0uo25cfUFwFONuOBMwkqaJ9-fiNbudoCjoQZa8XSyxgpkmp2rEeRE4HqyCaEtNHTEelMRAhDTJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=IgC5NHGSeHMOUQ-Eco8tg2D-YKvAWus2NaZWdudhcvvp931Z_ZeruWpAfbyw5nfzgxfSeq8Z1nALAJUncUpTSz8WWNnoQH85WRvqU3Tk3yNffFsX75tKieYzeum8PYOJwQyyD2upEjFhZ2_XWZ8LrgwVyXiyc7e24keqR_bC61Hl-TPA1Vgrqv7HzWwLylKHt6ih6Qzo94hmpJFsY0DkY69iHHJeOLmXNd4PNPRUowWyKNT64UdHC8IeeaWspIjtUgwzN5FoRO0uo25cfUFwFONuOBMwkqaJ9-fiNbudoCjoQZa8XSyxgpkmp2rEeRE4HqyCaEtNHTEelMRAhDTJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XVxzpmbEY6mITACJAKa9qjIk_hVZVBmbbDMuxOTgVyugreOb8Fzrx6-wGQ7IrtwpR_kENLRbdg40JcNCLh6-tNyLtVgDUozGdVzKmHebP7wQ-HP3AtUcsT7QXDSO0l7lxpZuzns5Ilh6HhZSs67lZSakB9Jv_BUUuNJb1B-WIuAAzz8SZuCGiqa5iFu0gL3FShKHur7frnFPdHW34SLajFccUUO10jEv9l4wqhVvLdgwRxvIH2Ri3FuP5r_eAqFuFpCL1KlrRXne11tgiTkjVCOV7YHZHbcmtLdccIbkR1iyi8Ye3jAHkOk4CiTV2NKUGroVLDsm5U1_YtDSpcRDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNdrBDbm0Myt2ESeMUowGqqf6X92OFz1FUvAyLpot6yHthRC-qYjnaFx5qMcQgDkpbLByELA-wtFHUwdPhBTJ2ug_2TmjEN7KTj_JbMXIhCKtnTsKIYcMWeIHsTmiDwXzzxMdmSWAIoMXUOA_SONcEcyt9yiIJ_1qVmv_M2i4z4aVoR9w5cDZv0HZgAmcOlKpQL_lSJgN5y6iGd-QkEpJ4vg5Tc7VdKlmvNGt89WVxti1kdDpDPMrnB3IfG7TcSHJCBvxKtGgUUKDUNBl8yMD_ogDzbD3dBGaVH4oQ4axg2N_K4TkCZHuHJVfoLwHU5Ant5_Tvx9dMzUHAliS52nsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgJyzOhJPCcEm1IAbpWjEHATO4MNqJNHx8iuQxF3xNnVPeRiR2zKXXE_3ykwHVXBdcZkxJZOPed9HahITDYDVLCOdMri4LzZsVLNRxOMZUO6nIrRRjNM_4tpYUn5w39pB6tso_l7iQvczspig3AnCJvLwnX6ADDsjfBKkLF0PkV3kBsM3241Mzdq66ABu6RwlYNxF4x1QTj7y4m4OE2DwB1risllgzOMkfN0mp87ad2qUPd_eL1-D_Ts4xzLjWUOEuh5INHWeofAc0xJAp4EU8jLdSOhQWi2eqk9rjyNpvyRwAZc91oCgifUiuLmSpLCIZDJ9M5ABEnarBpOGtFhiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=YMhxq76v-KjlhNv4YlAZ83075_S9p16IPKbxOnvHzGhDSb5P0iL4_Xyyot2BjRcKa8rj1MJ5pAgyhimXqLL3AwYiDsA24tCaOLXoXmVbQqWcK0C9zw0oPqWRfnAjKs3pMtEYOrlfC70b2-tnnlAihO9L5BTA25yaKpyYQEPYBESsW2aHXb1yY_UFm17-jITOlszcUBE0prC2S4BVkfRNgzYdAKo7Hu9xCY7SB-0A-ysfSMotOjM7KAqgal12DqJehjEkNden9LeElsGqF_Ab1jtjcwhMAuUCVwRDz4dYCWeWPbrZ24nzdkea-g7epMPv2GYszy3szgOKYiXRR5MgZz5PclUl-tKdP6QHfih_-IIM340ZmzqaD-7Ccr6S32CwFUmtNE3LfFKE_CQXUH-iopVib7z3PXLI6PYb7jB-HFJIESbtbRd-WjYLvURDfmnPMiHvt8bWu0Nysi7_mK_B--BZBl4ykF--T8QIs4QCzWbuzY3dtssSliXJBUeoTJJnc5nr20J4bJ5oB70Ax4XYm7Pq7sVES6z1ie6jyNDPbI2WcCuRdfKdb6i2XoeP9yeLySdzT9UNdQ4lR7t0GvaIuFXD12rZ2hbP2ZS5eVd33Mn4lwRvZLG8_vHyEJ6mlFPr9Jigu8BVe3UqxXy0bKXz2pDuvTT2AAfL_MUtlzXxhJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=YMhxq76v-KjlhNv4YlAZ83075_S9p16IPKbxOnvHzGhDSb5P0iL4_Xyyot2BjRcKa8rj1MJ5pAgyhimXqLL3AwYiDsA24tCaOLXoXmVbQqWcK0C9zw0oPqWRfnAjKs3pMtEYOrlfC70b2-tnnlAihO9L5BTA25yaKpyYQEPYBESsW2aHXb1yY_UFm17-jITOlszcUBE0prC2S4BVkfRNgzYdAKo7Hu9xCY7SB-0A-ysfSMotOjM7KAqgal12DqJehjEkNden9LeElsGqF_Ab1jtjcwhMAuUCVwRDz4dYCWeWPbrZ24nzdkea-g7epMPv2GYszy3szgOKYiXRR5MgZz5PclUl-tKdP6QHfih_-IIM340ZmzqaD-7Ccr6S32CwFUmtNE3LfFKE_CQXUH-iopVib7z3PXLI6PYb7jB-HFJIESbtbRd-WjYLvURDfmnPMiHvt8bWu0Nysi7_mK_B--BZBl4ykF--T8QIs4QCzWbuzY3dtssSliXJBUeoTJJnc5nr20J4bJ5oB70Ax4XYm7Pq7sVES6z1ie6jyNDPbI2WcCuRdfKdb6i2XoeP9yeLySdzT9UNdQ4lR7t0GvaIuFXD12rZ2hbP2ZS5eVd33Mn4lwRvZLG8_vHyEJ6mlFPr9Jigu8BVe3UqxXy0bKXz2pDuvTT2AAfL_MUtlzXxhJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=HnhJ47KWZ1GWRcofuJd7K0uU8v-wPvBaAIV9MHDGEABk8aCVe53rl-wV_h5_D4O_oOaMLLbB2KbBiPGA4ZBN_fI4xLqRg6LHd8qZszlfgx3NPAlNnz7eLjkG_pCsCTJfM_26E70RvlhUjCX59ouBXN-UZtLRrYp2AU85Seb7LEysQuFGi-afeTfTlBGDqIFWOU28LNL4AjaNNJP7K-k0laK8XQewhfu6XhgW6lK9wfXpYzWsnCD9TtSrj0XzOfZaYP1LmjLa1_VhCJbGBF-eSH9g-ewQz3ALuQwjhswo_ln-b4f3RwY-_lzYHXaFW2nBurnBbq_wJX31yc1hYp_G8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=HnhJ47KWZ1GWRcofuJd7K0uU8v-wPvBaAIV9MHDGEABk8aCVe53rl-wV_h5_D4O_oOaMLLbB2KbBiPGA4ZBN_fI4xLqRg6LHd8qZszlfgx3NPAlNnz7eLjkG_pCsCTJfM_26E70RvlhUjCX59ouBXN-UZtLRrYp2AU85Seb7LEysQuFGi-afeTfTlBGDqIFWOU28LNL4AjaNNJP7K-k0laK8XQewhfu6XhgW6lK9wfXpYzWsnCD9TtSrj0XzOfZaYP1LmjLa1_VhCJbGBF-eSH9g-ewQz3ALuQwjhswo_ln-b4f3RwY-_lzYHXaFW2nBurnBbq_wJX31yc1hYp_G8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=sRyxfvaK1Ua-OABJsjTPHIrrMIpN6YbsCXNpbA_9AAx1aSkTAiKqXTSxIIddnTY9ad6ay4D7Yw3xNUsdwSRb5IL44s3gTNYHSmf74EpMJ53l5P_SgVJ2xEWLMZXPu6ic-YBiEFoQEkEU6y-LNLfIbFPEo1APysXUvZ-1qNwOwHqwie3Jio5RFtY3yan5MvxvYTb1l87hjPuUW4aU3oqoA2VIy3rhCXasDYyFJGW5CPx6LAD7YXV26ve2SJNILwLdHfOrjTnPMoChEnB6a0inwPG-sf6bOr9acsZbnYyZan3RU67byw7fR85WX5MKtTMr9CTF6DiXJR-_918BDL_D7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVi5gCsfOTBSvIleSm30YkG1Xf_kqNlD5xjxueOMIscP171ZT4ZpJbtvy1-BXYs0aa93PoTd5hlHNP0mgZdy-F8xxGPE8EVHSmK_4jwHva9jvEZjhkt9hc08qsgL67FXMeOLI-Zvz1BPoZhzOGUto9_Jq5Wy9_gXqGNNMld9mh69iyTfPlE50bvGlpiPEOyun04wERtNb25jLQJTKlzDm5CDLUS7U7NC37vN31OwWruPeoKogYURN-zZR_jR58Udhxs0XvaIe8ut5DSxgPuF2RWF0ARALIyQIh_g1qNl-6iIX7sZ_ttB9JxiwA4fn4tV3ft3kYsAWScK813hmRvQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=FLEBMTKiBoFnDFLR5_dQv_lXvL6ZdR05Lu_zbPEgKQhDELLxjFxwma89B3t4E_Go95k71a4rRZQsePNXZXfLB3_OA2n70agHdnqDWqcuVjF8F7KUbwQJk85mFFjbDyFi6qWfJ_T6cdjjB3wD8XsQkjvB6ctSYRPL1CW5_PcQR7v91xF4ak2TUNhD4F2UgCnQw2MOjWMl9-ZfVs8Gx_fk9sve66yp2GFKBJSJ5gyvc91Rmzf-IUfAKMTdslHHai3oHp4UTU0U38nhPmLPHbxIKlQpR93AXtv1ksimt0WbAZhN_10muCfUurTTZnPcGH7Awovawvt6cLRWT_yv2V6URQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=FLEBMTKiBoFnDFLR5_dQv_lXvL6ZdR05Lu_zbPEgKQhDELLxjFxwma89B3t4E_Go95k71a4rRZQsePNXZXfLB3_OA2n70agHdnqDWqcuVjF8F7KUbwQJk85mFFjbDyFi6qWfJ_T6cdjjB3wD8XsQkjvB6ctSYRPL1CW5_PcQR7v91xF4ak2TUNhD4F2UgCnQw2MOjWMl9-ZfVs8Gx_fk9sve66yp2GFKBJSJ5gyvc91Rmzf-IUfAKMTdslHHai3oHp4UTU0U38nhPmLPHbxIKlQpR93AXtv1ksimt0WbAZhN_10muCfUurTTZnPcGH7Awovawvt6cLRWT_yv2V6URQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCLvKdbfZwUKDusPr7KabTaG7FCufB0HQAA1_PlEri4c6JmoiUJzN4i5756N8lAc5WfWsS1L27kTiL304mfa70cj08eqPyl2pAjCPL-jQPyl8Vbsb83UpDlrsEjsZJeTFtjr1bGG1KyoEo0ZkP9wYRQeqhxFYS6N_LYT0ECgbpqlHOf7vfd28pc9I1obh7jZCAOb6zYJPRRkMS9wmxsjC0ZE-IzgC5UN_WYhrsjIwBD70j1M7y6JFl0-9LCJ2rI4obf2Ly_iTp8iyDmjCMG2JBYkJm4rj_G4RAB1jaGpx4o_hHB9vmMwwKl7U3_IjR3b-7fKHRgfvLXdogcE7ic8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGMxINoW77Udq6Ma3Gpa0lG-NNYDTIQyqn6QD1NCi2_KrR-9i2nWRO4G4XxEh5r4Uv7XpTAGDrOfaDf-IeelfoFnih-ZpzEhnTAq2VXg5vRPQQU9hvy0fpih_Xe98gCCMsXScEGKV8SwoOCEe7kNVqYFWtKU7BSTGVKYA9iWNbLTQ4HMnzgUHcSiC-FtN0yHXeHAlgHwb2LdXZhQUvf_62xoTfdK5PrLIREVdgat3E8uMVAaFVnUJB6zWAoP0iahY-13BGnAbb3UVP-4Ptrya4Y8Uhp_fCBg1uLyzAUXMHI0OYBuHJ1yz0AsUTQ2Ny4_ajODDNZMTfXuvONHIv97pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdibSXzCcL6I1HC-Zp69InIEkyt98oERSddhKn7Kbgf55GSOIJg-mMF-g1_kBAdSQ06Ot6lmM9RGLiqpdopJomsahTwxbOVExZdDj3yL4pElc2a8UtymblQGI4_-iT6SE_abJdHKpqg9YTD5hN6drNdRPsQrH3KjfBQAM0cRYoF9ja_ymrAQjsvRZp1rr1_R7bPdpm3dcqi8wOTLPVMfRL79Gz6rnWYquFaNq_GQvf_po9Kvra1slVqsK_0Pxu9grGR5PvgfhrojgO2vummGXJKslX4yGXXgwb9mWLo6IlSrB3hpLBnOmYnfUgkn2y8LTYJunVWsBcDZX-xOtfRwZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=dFnf-5u_ooNHYr7IjT_JB17U8ZqKDjCMLhtO3PuKqYZOTEnw1gSn6B4pKemn_c-cF_bHi6G_4K2tPyhkRnFpgIgDy-Tau2CwYOJhCjw75_MjgRByataT1XVSo53vH-W1nG0rFEpTZFZhY0JeOJRvPRQKuIYd9Xr5bXBuIdhg6LSXeW66B8ONkSs_12YKr3HEaRkTINspYJINE292CTVtVftQkJ1hOOuy_BoFasyl9KtPx9x2SY6wPOwr0YqxF8o6Z8b-bVr6q49dnjzlMpf8Xszup03TbnfEr3Y_8BP6L8M5XEXbBUdytbO1TgxBJX7_s9WLcffL1KPj_bdJfiOAnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=dFnf-5u_ooNHYr7IjT_JB17U8ZqKDjCMLhtO3PuKqYZOTEnw1gSn6B4pKemn_c-cF_bHi6G_4K2tPyhkRnFpgIgDy-Tau2CwYOJhCjw75_MjgRByataT1XVSo53vH-W1nG0rFEpTZFZhY0JeOJRvPRQKuIYd9Xr5bXBuIdhg6LSXeW66B8ONkSs_12YKr3HEaRkTINspYJINE292CTVtVftQkJ1hOOuy_BoFasyl9KtPx9x2SY6wPOwr0YqxF8o6Z8b-bVr6q49dnjzlMpf8Xszup03TbnfEr3Y_8BP6L8M5XEXbBUdytbO1TgxBJX7_s9WLcffL1KPj_bdJfiOAnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=bUBZixi0SF7NfQbDAcOErcr7r2yqVJtId48nFRlIwH58Li96SOXvH_lpVYJge6ei4DGtMt_gWGf6eYqC5QgwyeVAxHBuJo6ThVOgdDIM8rWr7NTcITFUCaLMeSmYf5fosx0LguRkqCRjO_n7RyHx_gcOo6TcXN14PDbNhAcy1Zxn7BFnMo2IggoOgvPWpOEpmPbuIw7sdOqBSVnCUEk4KOvUMgQQ9cup5bEhenqImLKCPd9CYb0mMx4XQeEI2TWs_vfMUJ2bDMO0ohVSsmqHiMEHVDuysT4hFRsivz7h9UMfUnMp7-5DUP55v6fFDdDTF1aqN8N429QMD8ul-ohhIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=bUBZixi0SF7NfQbDAcOErcr7r2yqVJtId48nFRlIwH58Li96SOXvH_lpVYJge6ei4DGtMt_gWGf6eYqC5QgwyeVAxHBuJo6ThVOgdDIM8rWr7NTcITFUCaLMeSmYf5fosx0LguRkqCRjO_n7RyHx_gcOo6TcXN14PDbNhAcy1Zxn7BFnMo2IggoOgvPWpOEpmPbuIw7sdOqBSVnCUEk4KOvUMgQQ9cup5bEhenqImLKCPd9CYb0mMx4XQeEI2TWs_vfMUJ2bDMO0ohVSsmqHiMEHVDuysT4hFRsivz7h9UMfUnMp7-5DUP55v6fFDdDTF1aqN8N429QMD8ul-ohhIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBvQZHhpIs4uCpV0NG1aaYXoj34h1Oa2uR7odFjXJr6cbBAxMuXCP42hulwvwseEq1ONhaHYm66fOiJTiBylXmhbjbjmyXf9uOvbEQ50LuB43oIAId7cxumvNZpsazVuD28DP8439Q-2CoSXXSVllPb3weW4iz6ED2VfY5qxkkptpKeKqeKZs79xN4BWudPYrTCr2Ku4WVS1UBqd8bHGDXePwXTDkYaTZJslHblb-Ivg71fClno7lz6KynV9oSNACLnxK_1uqArR1oTp3CPqg3_I-QlnIn7nbajh29fb3_74rx2d-dHWft7TEBBzlMqGqal5kJnAOdYez-lUPK7gsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26020">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxlyvypKQQaumHAmGm7j2Gv9YQHcpMlVuR-24XMzMmpKCV0hKlgAekMxaQqWe5VSpZE0g51lWOrDKnJ_WlcIR592sw1VsX81gUHcKW9JzgSkIl68S1oEepDUam2OI0AQGa15HRuqbrz9sx7p_2UwzQKaLsJNnzDM3JJdsZpgmBR-yQAiIFDU-HSsN_uCw9kGy-Cw2A8G6Ohm36m1vFVSLXXPrGzSWK5FAw5R-4nqwCXH1NuJZOB2_tH6JCOsdizuPjyJTL9A-w5WOvUUEgB2myd1uJpAVTPIku-q4t4IxJp0J-_mv3otl5jOVHA3H6_-p_z6BqjTDhtFvvwurKzOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQ8sK_maD_q6cOqpujbjx_24F_V62mwDfYnlvK1peBo0HwOAZ8Og6K7fwcPDUet7qPbfPbRDsfKGbw1tk28XkS9n7wKYnrR-Q2WoZoQxekn7Ks7blBSAXi3HsFSIhSc2Fim7xkXmhOcGEQY4OoOWbrsUdw3qwmFj32zlhMlUx821oCDq8Ozgo6jZ1ZZysH0V22vX-y1_bbu78GN-CMWGlcw7vRrr3I2fGmyVnQYdu2gTYVNyK_-eRHyWYJiRkglMyQSTaTIvPW3vWudxBJQq-eC-fxquUjHNz5MU1xCcRsvWI-enK9BJUNGGtGfYzfjXHUVTZ_3ABUVVntfYZqiCOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26020" target="_blank">📅 23:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26019">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmOoDxspwfPxKrjR_W8InU_KbPjrPMAiVia1RdW1HjomfAP1oo5i5WuPiqUz-UKIwsrZYT8igxUBYrBQxjqqe2Fu9Z9hkUSrCXV8K9X4etUbumBgDIx32DztdHkhRYAK0i9DS5OwyazoaPnqiKb7LusIVWvednFoXq6rELnWdThXC9iEB9pD4q1NO_bmVzK_yxPYKzHpIDsuWFsdH06e8-vAGIRRMv3INd1hFmi-QI4SYYAoFUjh1qXZ-5-3WGWzJigwGgRORYlfqciQ4ACmlxPZ5tOeyqqWFs5xb5ow6Mr6QmIVTzf1hBwIaVfBiwKdLs8A0otv12y_bC8zVefklQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26019" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26018">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOLNLrYcV2gUdH-X08J3zAyJOmmAM7a1vl94MtJ40Loa2LB_mKpz7GvW8Xa8mPhSM-3jt3Mi7iLMrM0dAqb3NEx9qf0RoV3wRDZnKBazXd0oicl3dKR21pG1k-3vu6uld7XqjpsRjpq4E7RIH88W8Xdlmlp24GBi_UNVne-IyfWkjPDugosiNuuvMstz5ahww7y6LGrmljh66m36F8sI90xSYlidUVvICL3G8H3sIiucbSJLDQdZTAWqPwkQRO8K5M2DpG4CwKnMoGgDIoW5r-CitUwllp5zilcc0OHg78Yg8eCeDQirGaIDF7MdK5Eh-rTgmaUJdyH-4qMSc0OmsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26018" target="_blank">📅 23:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26016">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇪🇸
🔴
هایلایتی‌از عمکرد آلن‌هلیلوویچ ستاره سابق بارسلونا که در آستانه عقد قرار داد با پرسپولیسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26016" target="_blank">📅 22:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26015">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5vaZBbfWElc-hqUkdfcNqFQjmA6AIgJ08omH3YSZAvXubz2Y4oaj9Q_dgSd5dyJ2k7CYVyD9SOUiAKEgbcMKsYFR3AVRTG-uDXWN_wg0Qi9WUGdtGrKrLNMvR7rqiLub8_C1nIo2HnpT5dKLSikhQv3x57eZTelHSBXjmft8A8ulcL9pEuCCH7kFMazzROV9BNx8sU7rJECGrLwnrjczcmSpjV0OY9aeaOuU1kVD31f_MNYH_kZSqU0LpNSLYMYaUrD5fEFYuGTqVG0BrJQhLY-dkiema-McNb33IlDQbfWhR2Clu5dg355lzt1deI-wiy0h7lM79YCSNpVo6XP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه‌پرسپولیس به‌درخواست شخص مهدی تارتار با یک‌مهاجم‌کرواسی که سابقه بازی در تیم‌های ملی پایه این کشور درکارنامه‌خود داره وارد مذاکره شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26015" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvNlJATMI1Z-aF9i4SA6gQl6icIAcid2QOEdER0FWX0PcscxaYdJACLySZ4rMnYfZGh5Urj2WsbDV9TstVHX3C1Rh85QNMarHyKVT7NSB1HdOtUaQJAtSY5qcjJbZe8coSvaQ2I0OlOSnISRPHCVQ3W9qJFHwQDplfgaI631fVQCVzOH2aabwrcD7JMOBQID1FNy8qTT3XDo30ecSLLxUelRaltIiq4xSzhOM3u1WCWYtR5df8Ws0K9ZCZaNLGphPbCrjLX7W88d2DEewIwwdqo-5XwW2Y3XBV0z-Ph8hFBwQi7QnLvXMMpJJfCum5zo1xQjr_IOrgVsqqp2oQt-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان تری اسطوره باشگاه چلسی انگلیس:
این سوال رو از من می‌پرسن که چطور می‌شه مسی رو متوقف‌کرد؟جوابش‌اینه:هیچجوره نمی‌شه! حتی اگه بخوای با بازی فیزیکی جلوش رو بگیری، فقط باعث بهتر شدن اون می‌شی. مسی فوق‌العاده قدرتمنده، از جنگیدن لذت می‌بره و واقعاً هر چی که فکرشو کنید داره. به نظر من که اون بهترین بازیکن تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26014" target="_blank">📅 22:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d9c8adea2.mp4?token=G15RIk4ganAoOdOcf2xDY-5co2Nfr61vg2EvO03ODhYJIvl8OCxt2-ryAFBs96dm_4jNcHB-4EjCMq8LfqG5tCuNPQjpbMlcp7YjLQnqOOLRZr4qfnNnowbdn0_NLLbU_OBvoH4mfEfuE6Fc_CKTDQC2LHiWXegSHQMT8G7qjm8Qw7Rp1gd4ozHuRCov7d77aLoM-C27j2z96nFlwhchNwGg8SsGoxhnmg1tpFrXiWYcv5rttiuizr7eAcVhtifBnF85hnJ3c3MjWfjPR2GsV1s60yITZ1Upq7YF1_lVZUbQv270vKgLezoKCk-sahmWSi7MZRG1QF8o-AOavQnJ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26013" target="_blank">📅 22:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPbiNjBg39MjDRd83Q0lacUdZLskoKotSCoBzkKmkzQR8_eJ-_ceQVSfWG96Z0t44z9kX_PXLexluNyX6B0e_n5MdXUOBqX0D28Y9yEE2QD4Cm7VWADEmzw-YR2P6fU4AdxjCCghDkK27e-XTGWSd2M2SgN5u_QKi-zp3XT57Cmadqo9F5_iA2qiiCuskR5rkyVowK7jxGX53M3dy4PrSU0V49O7rykfRXbsjvwTubvvclD1hUOPyqOmpBDvohVHlUZkqBsAOTZrLhD7PLoyaiPZGR6D7H3376YvB6R4Fi43Tzr1rtl5jyYLRKtON1Y-zc3sJ3NYXgo21LJL0ZUS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بعداز اورنشتاین؛ رومانو هم تایید کرد؛ مورگان راجرز ستاره آستون ویلا رسما به چلسی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26012" target="_blank">📅 22:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ty4iGxxo0Iyh0GPf5_wq0iZIcB3DC6KLENohGBEQejGaMScRaVFHM1F_yBjf9BM7ejkPa1WTX-eJimbnEb0g7rGOTHAVG-BmJfz5XHwQiiQy3HnHVw-cdub01p5QFZDrifX5MrKI6krzXjNNkDQIbzRngJ2VBh7lGtzStlY0GfPcuNnXG_Lzmx1G2F1WfqEnRS2xg8CWlIqKLuPBQeVmgenOmhW0Veivqaakcs8eGU_Sbzq-EBFIgMbyTUM9F5-2hfHWTTOBBc2H-vuwQWq3z-Zal1V2Zp2uSqFm9sKuafQRC0_ZyeKyAQVggyavJ6mdAVOJ3GevWiRNL3DkWvqNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🟢
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌باارسال‌نامه‌ای به‌باشگاه اخمت گروژنی خواستارجذب عثمان اندونگ مدافع‌میانی26ساله این تیم شد. اندونگ دو فصل پیش عملکرد خیره کننده‌ای درگلگهر داشت و با 500k€ به روسی‌ها فروخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26011" target="_blank">📅 21:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuYGC6r8X6DLZqnB56PMQt6AcJcZUYRilqLSTxKOPw3Qm99fayD-JmHxQfyzhY0pKucEC2P_fyMr0lY_vjd3pkHDL1VOFyenJIV1CNW_a9gKc3bCdQEebNZC4cvIBQi6nBYH94pUqhxpMZ_rQrottqMnD5a51_UbiTQDfH3FrnZQoVFdC1DmIUcOHqEYr4i1387_QpHXBBZYUY2b9EEXM0OpsRGr4ARJ21sRqhTcEU4klUxpYtKdwtwvOAST7ilL2vaOUzEgqhpU1IYUNpoyeaSKEfq7brmU38zlVO23YlrvjPvRjlAzeyPeVS6wE9N-n21UB7ylpAvyEknoUYaD8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتاین: آرسنال هایجک خورد؛ تیم چلسی با ارائه پیشنهادی 137 میلیون یورویی به آستون ویلا درآستانه عقدقرارداد پنج ساله با مورگان راجرز ستاره ملی پوش این باشگاه قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26010" target="_blank">📅 21:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26009">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZjgGP5Ed0_UfJljnKwYVevvcpLhHKiXsajJWfJ1weyKknNkId8Gom2m7t4tqFCkl3a1l8NDGNPQCTEGJWqDO3qEnYJ-0jm5oUvBXI8Q7WdGGhcjKwQz3i_sxwTwlwRuckv9YBDK6r5gkC5jjN3n8Wc-fVDbeybtd21BMh4Xu_dRxAqecbg7AbPnh_OB0qd5ylN-2niFHMJ0paFCGO2rT1tdIfvYQvW7GyvlHgVNcM85y4jxzCpN3uakJ7KalARtgM8CPijGVeIt5ZVPPQtLU0W4zoIoCqsGKLp__1UpZsbywt82qgUYAr0v3Cc0VgOR76qmyxSM3I8TEmCVfxc65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو؛ کریستوس زولیس وینگر 24 ساله کلوب بروژ با عقدقراردادی چهار ساله به آرسنال پیوست. زولیس یونانی فصل‌گذشته‌در36 مسابقه 17 گل و 23 پاس گل به ثبت رساند. همچنین توپچی‌ ها بدنبال عقد قرارداد فوری با مورگان راجرز ستاره تیم ملی انگلیسه…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26009" target="_blank">📅 21:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=pqmha0F91zRL5oW_ZlAoZxbIz4lKvTk57DAciOePKlLM819RePihnXrcpd3S_PGaFYvKq3kIAnImP29omCHZmpsBeaLtkh4Rfr1-p_thWgzz0bkw53ChtR3xCQGAjVmY0N3i6FuTo6ApIQ9OQXHdyaH3Hi46QKn6YOu_vkLlJj-G8mGKQz4RrLsJHh86eL2yYjqL6umBmdc8bbxIJodsntGQ7BDK9O2vDnJi-OIEqLeN2RYogtr5UkueE8oPFhMqINm18VyQJUOlIjeosXqw3yRHfXh1Tlk_tL5NIzjkl_uKJuMmPpJUN7ib_344ubuC2OAAzHtSNfQIc8pea16cKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3acdc0e3a.mp4?token=pqmha0F91zRL5oW_ZlAoZxbIz4lKvTk57DAciOePKlLM819RePihnXrcpd3S_PGaFYvKq3kIAnImP29omCHZmpsBeaLtkh4Rfr1-p_thWgzz0bkw53ChtR3xCQGAjVmY0N3i6FuTo6ApIQ9OQXHdyaH3Hi46QKn6YOu_vkLlJj-G8mGKQz4RrLsJHh86eL2yYjqL6umBmdc8bbxIJodsntGQ7BDK9O2vDnJi-OIEqLeN2RYogtr5UkueE8oPFhMqINm18VyQJUOlIjeosXqw3yRHfXh1Tlk_tL5NIzjkl_uKJuMmPpJUN7ib_344ubuC2OAAzHtSNfQIc8pea16cKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تو زندگی همه باید مثل علیرضا فغانی باشیم که حتی اگه داور فینال جام جهانی هم نشدیم از تلاش کردن تو زندگی ناامید نشیم. امید کلید پیروزیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26008" target="_blank">📅 20:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26007">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaBcO0FIRhL_Lnih-KaiHYMGKfFA7TAWmAF2bo2wPhc1LyURkENmJjK77b_CSoZstLHxiF0WqThh4suoXVMWgluetF5-HbXzKNAlfyjyLBgqXodKHSfU7yssOCRputOfZZ5BNAUinQdW6q6nobaSFzlUH3v-amA8HhCa4fjhGxPlnIfUhpLhKS1TXXOoV0XUxAC7ySX9NCxhYOCw9mMgNcqz5od6a0KYMhKq0pixckoUWbstqqLUn8HHGkcDNJq44sa5Vc0Zcs5pDit04seqySv7URA_D7TKtOYEZ5ceVkBwg7TxwmAO9QQ0IvuwQOMI5Ua-HdXE9SPLcx4VafJhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26007" target="_blank">📅 20:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPgzGRgPRCR-3TQLEofYYjBp45BTNQMybBkACzNsaDhWuGvk-yyPi_aCzNVDHI_OZvtIqMZrsfKg-aH3LGwLkyieKkKqWcNsrOc-R_qeJ-0vbW3bux7GBhDysGxh6FtAUKIZXOZf0YWA6HPIqwFz0mxOk1c0XxM2aDtPihN2ArZcze_GkSFujDROhIHU6CgaKOwXHvPmCmZS5RwYhTHrvMfUeO-JI2SgADI0dTc2p0RbXGCk4BroyTg9Iv21bGny7ULGjEiJbJ1kS7tQxSFUN4TQjdhmM9SmAPBf5m8a89pCa5tMPIOTfGVz6nSK5Dyw1Jbe_KnS7Kqp64fqPMHVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راجب خبر حسین نژاد هم‌پرسیدیم گفتن تا شب بهتون خبر میدیم که توافق استقلال با روسا صحت داره یا که خیر. وضعیت جلسه باشگاه پرسپولیس با نساجی برای جذب ایری و طاهری هم مشخص بشه قطعا تو کانال میزنیم. خبر رو بی سر و ته نمیزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26006" target="_blank">📅 20:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26005">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVxinkoqzQ7vnY3lZYbA6WFuBy5yPUveNKzIMm8PlbBRUT4RKlY1PmQMF-rWLGMg36NvP1S5Odmy-p23i6L0gb5ABURyQCH1yWzQUOTkSBBTn4bI59FUuuZuD1vww5lojS7zFe5lLXx9XGTz988dvg97L0UbFld_sfaU9N47Z9UN0JYOeD_r_adoYrUE-mI7uAbVE9HFRvwpggOYb8uVQoUikCDEcQijhMUJK4g1YnqG0H-fCcW0pvKkWV6ptLgcB_CM1tnv6e8J01oA807mjob3IEVi5XXWbx-aYfK0XEBSYGu10G5GwAiLJv_gfsjazULm1x1-_B0qNKIhQIJKcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وزارت‌ارتباطات‌شایعه‌قطع‌اینترنت پس از جام جهانی را تکذیب کرد.
علیرضا عبداللهی‌نژاد»، رئیس مرکز روابط‌عمومی و اطلاع‌رسانی وزارت ارتباطات و فناوری اطلاعات، شایعات مطرح شده در شبکه‌های اجتماعی مبنی بر قطع اینترنت پس از مسابقات جام جهانی را کاملاًبی‌اساس‌دانست. واقعا اونایی همچین شایعاتی پخش میکنن مریضن. سه ماه مردم ما نت نداشتن بسه دیگه کم دهن مردم رو سرویس کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26005" target="_blank">📅 19:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Heif9YGsIvhPhbLUH0ATVCHuksfNF4VDKEoTRCvJpkRjqQVTOPKw53yoB3YIqkF-XlloesPXYM4ALbYOkYpvw_efw6LQXGZ7qE_4W-IMmTc-Xh3Rb91Vxdy4zM5QjFJ-4TRM1JPxTtabN54aSKKsqDNA48_r3JZHto3YhHc5CtEWQBGft5YcGeXuqVcrmaRiWsLZMDil25uTaNjIt0cRTVgtSZ5xboXP7VnqaV3ZudIajoewb0VHetzLOhGIQeB4kMeTQd2uI0-4hukgqIU-2Kiudzm6kGFW6rUki2Prchooz3g6hjKp__4mqDAhVSMXUn98thIA3yRJUCflcLC6jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
آدیداس‌ازاستوک‌های مسی برای فینال جام جهانی رونمایی کرد که روش‌عبارت "آخرین رقص" حک شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26003" target="_blank">📅 19:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=fuCtXXmXdMJ-skUQ3XCb4USS1cjh_8ssK5E966_PENE0G197sEsjz9unf9n3xvbV1Qflz6d2EQjjCY5EWZbDBjyR7EAPeTR1cv2hPH_P62umagKAs-_3n2BLxqiKNnIFcYWhXzaZ_832Nlvui6fHinUVpUtgHwFd4pC-1yeuVpmQitLsSdo5W_TsWj4L2bqiJu6qr3OS4M_7Y0sN5vtTQDRfClbHqd_VN4BP5Oha3RW1B0T0DcEo3qoAZimx4SRKbMhAkU9DS_NL50VgUUjx0lA_4hj-EQXK2XxspMoy88u14wGHMZzmdULQ_umzoZUuYTTRhILXmNqeoS9y3-ItNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e60998a9e.mp4?token=fuCtXXmXdMJ-skUQ3XCb4USS1cjh_8ssK5E966_PENE0G197sEsjz9unf9n3xvbV1Qflz6d2EQjjCY5EWZbDBjyR7EAPeTR1cv2hPH_P62umagKAs-_3n2BLxqiKNnIFcYWhXzaZ_832Nlvui6fHinUVpUtgHwFd4pC-1yeuVpmQitLsSdo5W_TsWj4L2bqiJu6qr3OS4M_7Y0sN5vtTQDRfClbHqd_VN4BP5Oha3RW1B0T0DcEo3qoAZimx4SRKbMhAkU9DS_NL50VgUUjx0lA_4hj-EQXK2XxspMoy88u14wGHMZzmdULQ_umzoZUuYTTRhILXmNqeoS9y3-ItNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ درباره مسی: من‌از ورزش‌سر درمیارم، یه چیزایی هم از فوتبال می‌دونم. داشتم بازی مسی رو نگاه می‌کردم، دیدم مدافع‌ها حسابی چسبیده بودن بهش. ولی یهو دیدم غیبش زد و سر از سمت راست زمین درآورد. میفهمید‌ من چی میگم؟ همین خودش توجهم رو جلب کرد. هیچ‌کس هم درباره‌اش حرف نزد، ولی من خودم متوجهش شدم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26002" target="_blank">📅 18:47 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzuQBVg3Bna5rHcBkXETy2p8HH19jP4haVvEX7GkCh8faCA1Tuxh7aDmLXspVySS4GRae7h2JzhyWt2lu80R7FfWsfIAzrXI1dRhYX2d7YAmHMJ7lrpyj1EVDi4DFKgySMy0qQh81tqFWP1c_g5lCJ6AZiGLXfXNxm0SIK0jexlaSOy1tpD03hEXRMZH6jU67m1-gQZHM-0uMhzrGrPaowiRbzylU6r1EKxzGcxk4Bzg6KSnn-xs3jFUYRtVaUqOc0yjylG0HrUyLBJ9yaIDWk4lHjSy9q8vuKG1k07Vh09J3f2PuhPwhA910_ZpiFSncpXT1MSF-c5NY_x-t5N5vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خوان‌کاپدویلا دفاع‌سابق‌اسپانیا باسابقه قهرمانی جهان دست‌زن و بچه رو گرفته و بره آمریکا فینال رو تماشا کنه بهش ویزا ندادند. حالا چرا؟ چون 10 سال پیش برای بازی خیریه به ایران سفر کرده بود .
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26001" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7MQ44GfJekIkp5-17rbW-QVKxEKV8YKue_tsjCh2UleKnriu-oHiVfxPS0qbKflwVhMUOO1BKJxk4K0ydjrCYNmZaAPDRSKTTteKa6ckRVgzbsW6f564yWXfl_T5MciCDz9yWnMcK5-GWGfoMWiHOajYJjQY2entwLyj7v8bjReobyXnZFg2X-hr4-TGHJAjh-oyka57i4zM6xPeHoPI3WwOLMZKMcekzw6Cg0TYQUK9Y_qucB-MNbcAs8YEFkcqjO6_4Wjht5RPU9rmaLW1bLJm4ayzW3zDgM-5SEeaixOJSF1yTWHHomY4mu7zqUqphYVOyRCj8p5l9ZmQjm5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26000" target="_blank">📅 18:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25998">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UudmEXAQtvXgQYD_o0W8NxFeP1RVQMVvh4SdL61qTyy9fK5Y-MhE3e0j459GNApVCWG3Y_hzN2RuZkj0war-uxNQlBGaIrdpRAYKQj-dMGbvG1c_-mKxluXljJMnPVh3i9YKnDFx3Wl4VXl97GBfNNmHmmKgLOgXqqUgNb8azkAGsTp_FGuargPn1GU9tsD7yRlFZlG_fWqTOcgjLC7eOMvHXYZTc997Ez2l-aHHBb-jqgqBCFPqcv1qoTAPpc9EbixVj1en6ULGDHiuhPkLx_UqiR7UfKIaIQmxXPIWYPDWuMis1t21uWtfWZxbPhH8KDXxnq0Fl2MwFr5GyGJcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم اومده با استفاده از تکنولوژی آفساید درجام‌جهانی2026 باسنشو مورد بررسی قرار داده؛ افساید مهدی طارمی هم تقریبا همچین چیزی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25998" target="_blank">📅 18:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25997">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T537Y8NSzEnOYdlxazhhqxrRWoYrtdVJBhFjFdrSz6eLRyb6Wn6vkxd9pHyJsbf0SPwTwWAGY9YKBul8TSnTvvMWXXLxIrXKvOheul_s999mI3Oa42pzNJLT9gDfDVVrDLdnFF3pRCm6e43HEqCPruWDmvkUnRqnruOVLDlCpDJZHVipaasmtcjsbY047dNbIJJ614COo9KIod8hib-n0h5m-UXLW8xQ0tpRtXwQghkxWzhx2N76tYCa9ZiXEZFBgElfEElPtJ8pI2hV77aatizic6cq5MmS3pP587IO0MvVM6xemSrd2apwStis3xejaTrwsw-aRyJtVs9L5GJY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25997" target="_blank">📅 18:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25996">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAJWUfqH-Y96NNZAMvRlZd0Yk7uXdfkWVtU4GvedyWYmLnIWUI8yt92Di0TzAbYbubJVrwtezFFhR9Ft89-46kKAkV3raV4-gfn7WVd9mkjBOsnUVr3Sp429D6kqcMjSoYDdR00urYisEhg34Ncptpavo57u3vdL27MKx2DXgKXr7pNEiY-uMSFmfaGgGngy3K5SocTaRSOjjHABFFfibQb8K2sETWNCGNKY3GDcdb1HrfeusHe4f4lxgxDECoGACg8f903WldvNGZEvJroPVJjCC8-ba2I9VYFyzyWpWAfjdfkP73aBXzR98hykzaWT6kUD7auPKsiKTLp0A17yTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇵🇹
🤩
عملکرد استثنایی و محشر لیونل مسی و کریس رونالدو در کل دوران حرفه ایشون در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25996" target="_blank">📅 17:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25995">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=pIqixkx9QLYtJ5xUuOQXPEd8cuv7_RF3WDIv0vqShz0A7zO6ksVUg-Ia58S9EmvyVGBQYCb0cHEliZzlYwLXzkDyAF0M4-J0hkO59eABEwmqhArTQf0oCaqSLGSqo4hitLCNxNTreLm8NXHrw4IWxqUL-iqUsc6pglfxePB-jY2PZVFC1ID5YMAMb32VfCwlNLzExIvr_GmRM0FRh4plsYDLnbL2NO_2SiDXizioPf6iIkqiikVpI1t0EbQvTQ2nQFvyMWGJ2AJnOL-tURyeCCKi9ZA1CwpAj1cKELaKuH6ja6f-955MI90kb5larVmr-LCFQxeVoeReQy2Rj6Y9CR13FpkQcB6MR0iyGDoIq0BiHEvdfCqKpNEAJPXMj8FEdaHgQ9xco5HEOYqMrTq_bFK1avvZC4ZOTDHCHmobLOa54ZC6d8IBhsTO_0KouZkrM2A0P3gpNgrFcg7HcMsZJISZgPjO30Q8t4BlrM-wZ96WeSD4NurbrcXhVsg_1MeqS5K7vQ4BeRK0EyXQorV5eTGrnHSBBh-6_DMhL0IMw-G9Sa--yRHJ9-KMFfdWUGeFGijHpt4815Yt87nrgaq-5sH9d6Surtu7MrxT4ZaU0QYTl640WDAdKIq13BZl8WL181O8uJE55vduHKJfzHG4qF4zOz8isjeGcpvPgnzFtxU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf0ae4ecd3.mp4?token=pIqixkx9QLYtJ5xUuOQXPEd8cuv7_RF3WDIv0vqShz0A7zO6ksVUg-Ia58S9EmvyVGBQYCb0cHEliZzlYwLXzkDyAF0M4-J0hkO59eABEwmqhArTQf0oCaqSLGSqo4hitLCNxNTreLm8NXHrw4IWxqUL-iqUsc6pglfxePB-jY2PZVFC1ID5YMAMb32VfCwlNLzExIvr_GmRM0FRh4plsYDLnbL2NO_2SiDXizioPf6iIkqiikVpI1t0EbQvTQ2nQFvyMWGJ2AJnOL-tURyeCCKi9ZA1CwpAj1cKELaKuH6ja6f-955MI90kb5larVmr-LCFQxeVoeReQy2Rj6Y9CR13FpkQcB6MR0iyGDoIq0BiHEvdfCqKpNEAJPXMj8FEdaHgQ9xco5HEOYqMrTq_bFK1avvZC4ZOTDHCHmobLOa54ZC6d8IBhsTO_0KouZkrM2A0P3gpNgrFcg7HcMsZJISZgPjO30Q8t4BlrM-wZ96WeSD4NurbrcXhVsg_1MeqS5K7vQ4BeRK0EyXQorV5eTGrnHSBBh-6_DMhL0IMw-G9Sa--yRHJ9-KMFfdWUGeFGijHpt4815Yt87nrgaq-5sH9d6Surtu7MrxT4ZaU0QYTl640WDAdKIq13BZl8WL181O8uJE55vduHKJfzHG4qF4zOz8isjeGcpvPgnzFtxU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیو ساخته‌شده با هوش‌مصنوعیه که خود کریس هم لایکش کرده، انقدر قشنگ ساخته شده که قطعاًاحساسی‌ترین‌ویدیوییه‌که میتونید امروز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25995" target="_blank">📅 17:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=ZMVTIgOctn71Iug6uTZYlLjJ98ZMPF_9bD9XX3xf_5Hzpefk_OvIBpwSLinMDhYhQODkVgoqdB0Bq0GQ-PT5sXcK1agS_Dt67awBOEh7APizVZ_gfRpm4aUujAmQkvQJbDyKfbHYlSSw5yIM2MwiJ6QEatyFkU8LJoO4ZhAZ9JB3HadTIYre4jLO8M60ooHkKPoMvQ8su5ycAYNCmYKrxbgdVKxJYmsub141nusJ6dWPfXKg5ozEnb6V79OLO2oA4-OuCmQ6EgGnClHxC3f72gJ7V4KVepUT8WkZwg2BUFyo8bHalVsB7-_qfCSJ3dtRJVnGWahQL8IBqWS2bRxl-DMKDFoRDopD2J9IA0wa0sDll58q_X8xoQOsk2LXvKDX9NnZ-qnmURpOcAb4mXGdCi0Z3aN-vnHl0xueJl62blRO3rZvtS5rSCOKR4hAy72MzbT_drWz06JOdJZGtJs6xSxTUnI4SWdQadbOr0DiPslWtQ5qtotyOOJG7g12qQZXQRxzbYJWCLprdMSgrukESyJZtKtCjDbO9bjZVyzlEFgsGPS73ANXiHUsUY5FXd0IxKp6Bf7GuOKZFmGFzzu85ubPqjnb5RXW8y2aSMNJ32gN07lpmlV3XCk2FRBBSos6jIfQRYEZ3tPtYfSDloQuS0Kiu1IHpQvvXjj8c6VJVJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46f404ea6.mp4?token=ZMVTIgOctn71Iug6uTZYlLjJ98ZMPF_9bD9XX3xf_5Hzpefk_OvIBpwSLinMDhYhQODkVgoqdB0Bq0GQ-PT5sXcK1agS_Dt67awBOEh7APizVZ_gfRpm4aUujAmQkvQJbDyKfbHYlSSw5yIM2MwiJ6QEatyFkU8LJoO4ZhAZ9JB3HadTIYre4jLO8M60ooHkKPoMvQ8su5ycAYNCmYKrxbgdVKxJYmsub141nusJ6dWPfXKg5ozEnb6V79OLO2oA4-OuCmQ6EgGnClHxC3f72gJ7V4KVepUT8WkZwg2BUFyo8bHalVsB7-_qfCSJ3dtRJVnGWahQL8IBqWS2bRxl-DMKDFoRDopD2J9IA0wa0sDll58q_X8xoQOsk2LXvKDX9NnZ-qnmURpOcAb4mXGdCi0Z3aN-vnHl0xueJl62blRO3rZvtS5rSCOKR4hAy72MzbT_drWz06JOdJZGtJs6xSxTUnI4SWdQadbOr0DiPslWtQ5qtotyOOJG7g12qQZXQRxzbYJWCLprdMSgrukESyJZtKtCjDbO9bjZVyzlEFgsGPS73ANXiHUsUY5FXd0IxKp6Bf7GuOKZFmGFzzu85ubPqjnb5RXW8y2aSMNJ32gN07lpmlV3XCk2FRBBSos6jIfQRYEZ3tPtYfSDloQuS0Kiu1IHpQvvXjj8c6VJVJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌بدونید فدراسیون‌فوتبال‌اسپانیا به سر آشپز ایرانیه یک میلیون‌دلار داده که در آستانه دیدار فینال جام‌جهانی‌بهترین غذاها رو برای بازیکنان درست کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/25994" target="_blank">📅 17:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25993">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdJ2I0K8xiL5GbvnemB1PsocJ7_ftKwkLOKHJBcehIYoJLoKXtwZ3na2n9sSAYaKkhntvxG2-w510OB-rkI76-lI_YSgeII90qGv-iJoN2GvsnIinI1hDEUHfgc1svP3k-7qn3zpWkFDDvZutSBljvVBkRLTCGx2_nmX8ffwzKxsPPdrCim3KU8KYkoEDDBugNwkxXhARMm-VG8Dm09yEPVGVc84g905S6xvZeY8t2iF6NtHlRUo4X5c301IEKUTTSxE9IcxsxnFsF5sVua2O6ONC8XWCF2uBAh8o2624uRPZsuDfL1DvPS5-p_T2Re5AqWqK87sGZ_RKsB8-ofY3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز محمدامین کاظمیان؛ یاسین سلمانی وینگرجوان پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و از پرسپولیس جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25993" target="_blank">📅 16:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25992">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPeQ6OSxpk5iwR3MIwCbYE6X46wnArz2NiPvek0221uxUoZKWLOD4UQDGfJL6tsOjI9rOyo5Gs6aXdCb9pIJxwXEFAcJdHZL9xJdEQUE7E2YGliYtL4bqRwJd1HoomJrWmhJWhRtajX-aypaCB1HUYt4z1QNzPTZaHt6Gc576FpszueMFz_GsymszLMVdEsqKuxL937nrzOheLThSbHcgAo33hj6ocVRxaLoLMRVMkrRoqg_pXSDjg0MKMtL1wNClHFkssILL7XROSXwl_DBLOeihB0ajmoN08isj8DgOwM15DX_6bSwQketA0nrnYwdtqeuE_IXxLug7qdrGOgLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25992" target="_blank">📅 16:44 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25991">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAzhpIXvCjpn-n_LiR1TFbeqcW91n_TpzBo6DVaftLTGpVZxQ5JPFMxC6rCEF_-pleBL9QAbCqCQpZ9OPnTVSnBccEgKTNiBe-DtSYV2uU233NCiFaIS1Fi62PYP9QL2wyGZGfuQCN34M-NmnnXxkxEdrUluSSzkVhSqRHFsU9HaBLzEGFjaIoe8aEkaTlYpWyDezazQgC4swyftJ-awb0QykVD1mV_48gitGEOT1kECkcu_6CRKxP7-gwXJtCGkVCa03MESCebNSAzDJqOSmFnKr7khIaaBNNduEZmOa7Raafkw6ggEPRCB57xoDi_PE3o57A7Zhqhim5yG7BYhBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ از طریق نزدیکان خودِ محمد جواد حسین نژاد درحال‌پیگیری‌هستیم‌که ببینیم طبق گفته علی‌تاجرنیا باشگاه‌استقلال‌باباشگاه ماخاچ قلعه برای گرفتن‌رضایت‌نامه به توافق کامل رسیده یا که خیر!
🔵
تااینجاش روخبرداریم‌که استقلال با حسین نژاد به توافق شخصی رسیده…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25991" target="_blank">📅 16:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25990">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF2Z8k9D6O2vS9a6Otmvm4o3yofOQJfBwVnEF9ieBxF55aMO23tl61Tw-76kNH3o3EcaTh6Eo7oSSwhxtYsNKuylLwhNc84EpWKpLph1GDYHCZeerd7jxx47QG_BJo4I1RJPKrT9ltOuyJ8tOraLt0lSDXzABYuAKqbDsE6o7VKyA74MLVLqgbtENF2DrjdriLjt1F2T1TKdhVN3ODshu1nfPl0Avp7_5v6rvwmmvx1aowRzfE0e8iEqZXAIEffVAoveqkIHwWmomnF3k1vDyKSeHP3WDVXIG0WjL9SX76gdbJopgKJi0z2k2FOfxyc_p26yT2bIJx85fWeecsEPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
رفقای گل دیروزهم گفتیم باشگاه پرسپولیس هیچ مذاکره‌ای با علیرضا کوشکی ستاره تیم استقلال انجام نداده و هیچ‌برنامه‌ای هم برای.جذب این بازیکن 26 ساله نداره. بعنوان اولین‌رسانه گفتیم مهدی ترابی 32 ساله بمب اصلی مدیران باشگاه پرسپولیس است و امشب هم جلسه بسیار…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25990" target="_blank">📅 15:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25989">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAH9l58gLgEzATRxkxWorTP0R5wiA036um0k1ZfUPpRv7MOtDyjW-0_mZVSssmXAKa57d0Y1Hu_oVTA82REe1zu7vchJtrW_j14Gh1Bg4AqQmsWrqZl1u-PZTtY4WhlqasvN4wS_xD-yw4Mcq0Fi2HCeX4kZakEJFtWDFDugPvU_yRH8qkc-54Da__C6eNjZdaPZaHxYmEDDUNfYjBHj5lHDTkHDgKndJVsXWI3Vk3bve02MnZ2eWdoIOyuvCx4CdYmzynKleoFkezDEScWl6E5LYAqdCRLpDz8eSJfXEgK8slQVgJJp-J2fnCSW7waXMnfysIVoR--BIQfLFoOWAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25989" target="_blank">📅 15:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25988">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxbFDY6Hrz3kKb8cpfJMRhCPRr0c2_-r5pD6g7k9fP3dFchRN9fnENLwmNusmM1J1uB_DbOciZbaRhkkdBT8mxrXd3yCKplQPrOJqI2IWVyRB716ZDupLxRKkFSu2CvSDkuicTI3z5662rAu7eD30rWKUGaIoHhxDhdm3G9nCnGGoVo42js-7HULS94kdCbJ6gjgzi8tjqMqJFkfHc3yQnf-EVr7taMeONUgUCog4Fxn3dH58RamWAoP6WH1lisIqWNHhGCt60-v79tyL8-QDKvhSqh4sAhey6rrZ7kJ2OrKX2aZpDHFGybEtZovRzw8BWlwBLDkGqz6K-l5ECnxSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ یاسر آسانی برای فصل آینده حضور در استقلال 1.5 میلیون دلار خواسته و ازطریق‌مدیربرنامه‌خود به باشگاه استقلال گفته درصورتیکه بادرخواستش موافقت کنند حاضره قراردادش رو باآبی‌ها به‌مدت‌سه فصل تمدید کند اما در غیر این صورت ظرف 24…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/25988" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25987">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDPd5lFjzy9yiPNaFUzH1UvJc2P9yHbmgHdE7HWeocAYiYEJYL9KNidylOaO_o_Ad9Atqkw_7iOXxIfWjadiBy_V14a1n-DOBRB3FDHDjD8se6wqyjLFxNeeBOZb82uvuADPMdv_i6xFaOcfu_hj2ivU86S3z75G0XS2AlxCkJBgAhgdDFDUsEGP09fFfMko_ap8ckQAmhgUSr8H63Pn7B1U666-KSgt1fIXLeqYMZoxd6QTxk9rESCHpEAu8Ls6ust8jn7ccxCByF5UbhTTuFWYqQvK3DjchnzK9IwvpHfXEBfzNP78TtngNW79M3fiY5kRwaGS34_ToR47eFc0Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق جدید ترین شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ظرف همین‌هفته‌از تمدیدی‌های خود یعنی روزبه چشمی، علیرضا کوشکی و محمد حسین اسلامی رونمایی‌خواهدکرد. همانطور پیش‌ترنیز خبر دادیم تمام توافقات با این 3 نفر انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25987" target="_blank">📅 15:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25986">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXoIqps2z-CWsMDFcK2p77mi3ErfNKbrWjK3cRDriQao2GRlnTNgOxKWv5g3FZgon4-AFOJUh4zcfj_R7Tyah_V-2HAg9qaGPxVWpxR6cqun_nb3nfEqa5eDMcI1pFcBhW9nLpmzz69z7AV-1OCq8XsIIAJeVu4msJ-L-qGEdOKiQrbV8XFvic_wl-90AXNSC3wNgf3kO5ZMfDK2yWc-kyFPG-1tkx1IAmi9dtMocVRNwytSYWHFfVdyBZQaUNuGwSCQrd1FOwweCtZLDbV7kqV44HfLqLTGi8R899iKxQM7NEkAb3O3WmQAvges4yQPXN2I89NMSLEB1wiCeaKoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی؛ امروز حوالی ساعت پنج عصر جلسه مهم‌سرنوشت‌سازی‌بین‌مدیران دوتیم نساجی و پرسپولیس‌برای‌انتقال دانیال ایری و کسری طاهری به این تیم دارند. طبق شنیده‌های پرشیانا احتمال اینکه این دو انتقال انجام شود بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/25986" target="_blank">📅 14:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25985">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB-iR7NvqvwEvse93hUN07_Rl_-4SatB3E6NipHk-PSLyUfiN_K-o4Ju4BoBTyaU6_n0GIWydEwUcZti-dYC7gEIp0x608OY1-SRsAX8c9YvoCU3vw26HZSOLJ-mPeIId8OtqVYUPKLOTR-HsNkfRTHySylLlGRBWV--MUQRg7cRaNgGwR2UjTTTbadcjeTCYy00phMW7U1y2deY0EHkEYewjshDQG7vfptmXPoU7BPDWfe02z97LA3rSo-57gyx-P04bHUyOAEeRlWMXSIH0-x4eHp512El7grXAh5xhKqxAqWgOmAOYeNBwWqWz72S3rQOUZ5GHZ2ozGHb9ZuGGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه تراکتور برای عقد قرارداد سه ساله به ارزش 150 میلیارد تومان با محمد مهدی محبی به توافق کامل‌رسیده و بادریافت رضایت‌نامه‌از خرید جدید خود برای فصل‌اینده رقابت‌ها رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/persiana_Soccer/25985" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25984">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-bLXGpZguTVujC6HGTrZIgnGk3_AkXpA_RpgIEqeTzIG37bgOdmRH3nQQcvTgZBL9jtfvFQ9_L5Wtqzxe5DtaxaegH8Ainzc2h6MHESB9yVLAeOUIzuykHvLbxu5klgcRDpJxgylZr8gDmdc2I5C8ruoqCKANtyaTgqwAXnPwZOI7kkzWNjQBe3B5woM5W6hvesH6bqCi68hyN1lB6ufsqLxWf2QCKtDWHjCSxh1rXXlbaCvgJHG-l8P-8U0OC1_CMARSU2wFu6XnibNGpvDLRdQCTbcxUINrNfy7e_vd03_OJLysd9OoSkGDHlDax5lI9FlQcdFlB1BFLfimhkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◽️
🔴
👤
طبق اخبار دریافتی پرسپولیس؛ کسری طاهری از مدیران‌تیم‌نساجی‌خواسته‌ که کمک کنند در همین پنجره‌باقراردادی‌قرضی همراه بابند خرید دائمی به پرسپولیس بپیوندد. زندی مدیرعامل نساجی قول داده که همکاری کند این انتقال بزودی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/persiana_Soccer/25984" target="_blank">📅 14:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25983">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qP34JiExPVl4tRlPic7osRuVwnvUBvzxM9OvZSr3iZx51Tv6R05wNwGtnETmObsshoGRUQCfJpa1zEbJLh8l6TytL_7QPUiPS_5OCuGA77XWunw7r2q9G9LMFBBH5sj-IDnfIcmbzsgZTgReaqLP2haiJ6G_54bCB74adqo0hlGjjNNjMkP-UgoA6aJiDKZUinZ1yzjRRs6ElF9QiidzdzKyUuw35Ftf9mNV08JhXBqiO429CZ0TMPz_x-tpdPN2qKCFoHDQE3H7SPTlBxbwkFribxhVIzqUvdhvqmpsxiBbe59-B50kEhVefaPsWziV0LozvmcENwyg6WOunBQhiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ شهریار مغانلو به پیشنهاد مالی‌باشگاه‌تراکتور پاسخ مثبت داده و اگه اتفاق خاصی رخ ندهد شهریار مغانلو به زودی بعد از بازگشت به ایران قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/25983" target="_blank">📅 13:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25982">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II5VBhkTD_XlDgkKVWxtiaYEsK3b_C-CJfUbL5OvGzAJ4mVlCqEdW7dgHJy3Lr4TShVYHcefEnjYn31MuvwHMWtQwlawi9bIlVpnoIb4EfNvtqCtP3thjrVk13j0m_EugYnp3bEKIWBrpG3MOFMx1xvMIx4Qvi2dKFjdvZWH5LZXLizBLaq_RazmpYr3vvQnX6CaOF92_CZUnIulKrd9Al2zIO6Qy6Hm66CWtkt-z-Tg34s6YeXfZ27RQqvSNGF5HcN0NgbfvLU4WlLvtTPV2YM9gxEchA4CTiIFflkFEruWf1Q8Z1GjjRlJ0pLebVbUQ0L_HNA7rydhCqPnxf9UfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ تاجرنیا رئیس‌هیات‌مدیره استقلال: مابامحمدجواد حسین نژاد و باشگاه ماخاچ قلعه برای جذب این‌بازیکن به توافق کامل رسیده‌ایم و بزودی با حسین نژاد قراردادی چهار ساله امضا خواهیم کرد.
🔵
علی تاجرنیا نیز اعلام کرد که تکلیف نهایی پنجره نقل‌وانتقالاتی دوشنبه‌رسمامشخص…</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/persiana_Soccer/25982" target="_blank">📅 13:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25981">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hv819j6CIn1qJ2t_3Bs7L9HxgwEPW-bcusnqaWB_A-b7Nb1pBsqxtM3giQVK9o681qCHlnz2KULWt0EodzUyY1BTRAkrubRkqJSBupp2p0P73NpT3DLK5wdKxYHq81emcEdTJqnf80aSXoOkPYHbUMdd_9jhmhheFtidt4Mgi7uNCmljKDW1od5hNdIQeY1bo1DfBHQR9M2re7_zUUWCVFAhFIXXJdPDpmzkdXIT0jKL751pQc9qgvhxtXgaRvViWG33TfAq2jOOd29dgS7WsItXSGIjEc8B_8JI-pUf2ZacM7GisqxuJEO5BkK96b4HwX_PX-lxmJyrRQruvaZHRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/persiana_Soccer/25981" target="_blank">📅 13:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25980">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJgt5gbPv8PMGwbyjS966L3MX9SVeSVWR5hof_GgOd4LBpGoPLc4D7pxA1PHL8KJ6IiSUoy13uSIjFSOdjYosxrSpR0auhdF3QqoRRg8pn9bjsWLWlYRWmtVJcFTVonL6nK2uWLT1npAOoP44D5FFBLEYjJMvG93f0WODxwg-DhtOXAeU_gxtn3IhHLU8VReqz5h_EHXz2CD5Iolm2xAGp5CqwZAJPzJRYJEmvmg3xZXk6wO2wKI3-R3JV-BX2Iyz2hF_B3x2qToQjKNQVKXhrYVQNMrXu7VXZNZl4W96AlC3jXetxPBgD7f1hvxmzPUivbb6k6M39WgKUuymMECqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 84.6K · <a href="https://t.me/persiana_Soccer/25980" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25979">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlgbatIgi12TGQZCbx3MSe0Y7Qcd263aZJzOSWxfr_r36DIYpsg1YfepgoXs4DCuALLiFh-XfjYwKIRJ2tj-tAin8hi1mWpD3ZQEsO5xid4_l86pvWhCmEAswCspW7-oAGLsBLbgKIJGbjYzt7kg9weQigorYHaJD33jhS8s_rNXbUMdwidEytJdv9wEecBprj2wmn9uLpuZuYeHlIngXaaZwPuwcw2v7X511SQX_D97uFDVeTyWmVmamc0YyWYVG4I1z1FSnwRN-ZSsTjxfMTulch1HXOmVxXybeyf-_K8zQd2lwwUFzxOM2z5c4_FDWhAYdpNiWvcukHk1MKTIzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه تراکتور امروز پیشنهاد تمدید قرارداد سه ساله به مهدی هاشم نژاد ستاره جوان این‌تیم داده که رقم بسیار بالایی هم به او پیشنهادشده‌است. حالا دیگه‌باید صبر کرد و دید هاشم نژاد تمایل به ماندن دارد یا رفتن از تبریز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/persiana_Soccer/25979" target="_blank">📅 12:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25978">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_MriBxeWwy6bqS1981zdjBOEm0qU36SzQojJHfe8-sXZkruhYeZoxrzkwA7JyQOli0QWdm4dagowzRZjMSuBoNJyzfT_qmfVio1rOEWT8u_7qBEiI3zTyBm6EX0qAEOToi9nse-i2BqfFolRzdmoN7R9BhBRUHWDjuC1UpsZO-Hg7sRuiZ1zJde3j_iSkMwGZ2Z9oaleuVKtRzPmTHGhIiEqXwnU3EXbrTbb6f5g-edZYDfmMOkGlqgm5dfzV6N_9ljEr-YJey51FNKU3-3N-TL-I-CbRUFOtctk1kHi2YZAt0M245ka9cRT9KyLfevCVeNupUS0xgtFkrv5m2_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#اختصاصی‌_پرشیانا #فوری؛ مدیریت اتحاد کلبا ساعتی قبل پاسخ‌ نامه باشگاه پرسپولیس روداد. این باشگاه‌اماراتی طی ایمیلی به سرخپوشان رقم‌ رضایت‌ نامه سامان قدوس هافبک‌ بازی ساز 32 ساله خود را تنها 500 هزار دلار تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/persiana_Soccer/25978" target="_blank">📅 12:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25977">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlRklS6Y0fEYurxgBEfoXX6X1YTzv0jCzE9rRbRdoiKZPmmUy0kMKLGUcilsyrhljfMiNsSvQ90qk18n6wkN7fPM4tyN--ql37TgvV6bsRGo1nZ40LHZbhtQGro_KwfdndL7NzcZbO3QZpjqqWZWOmKwwUcioQW-qNBNKamXnKn0kpp06B48GUZNzZ8-E_hv88AC8ehDNRcz2seCUsBjSyUu67VhVocVndwvktrh3AAgR2vLKln0SwIYIvrxrD-0ViC5ii0-3fnMRKNqciNTB1_eINg0ERxh4nYF-mAQnosT0fzrj_SaPM-YUSQeK1RBYyXXQxl3Nmi4nd9paZoWCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ مهدی تارتار سرمربی پرسپولیس بامحمدرضا اخباری گلر 33 ساله سابق تیم‌ های گل‌گهر، تراکتور و سپاهان تماس گرفته و بهش گفته با پرسپولیس قرار داد امضا کنه. اخباری گفته میخوام درجایی باشم‌که فیکس بازی کنم. تارتار به اخباری گفته اگه‌شایستگی‌های…</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/persiana_Soccer/25977" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25976">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEHpL6yWjEfKG3R8Pcbg3vjUM4FzehsY9htm6NUKVbTOiUFqKAP7sggoD0-60ns6J1gLmp4w5fHwlXFcVimksbUuEeRwD-LoZ_tmRBoXK8-nhHe8XiyPciSkoKAuZuHwh2pXB8ICay2xV4v6o8ff928GAWKyKKiotswFwLMWWUlFFaaHPWtMZjSTxArIHp2igy19MA6v_VHGuwdgMhL2RSvXVS_G7WxbFsl67noK-6oceAXzjKyOieZmdu7hCgtcvZFGMSgHCPRDi_fPHgdaska0VTXSQ7KWisi-FBwxFh90YsW04yv10n2xS1NBFdTEPcEVgmdKeCTFzmLkhiO8hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیربرنامه‌های یاسر آسانی ستاره فصل قبل استقلال برای جلسه با علی تاجرنیا دقایقی قبل وارد باشگاه استقلال شد. هلدینگ خلیج فارس به مدیران استقلال اعلام‌کرده‌اندکه به هر شکلی که شده آسانی رو برای فصل بعد نگه دارند. ایجنت آسانی نیز اعلام کرده آسانی هنوز نامه…</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/persiana_Soccer/25976" target="_blank">📅 12:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25975">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMJublDdCQ9yWAvuzF8nJHLDW4KLrDd2HR_9p5f38ehvA5Lw4RTcKYrp7qI7AATWbsrlofGA4q8hmRhNdf06xFuTuMEF3JuSlHhERLai64e9ckc3FGRVJsubv6nnGehT71pySUKtXECCdYNkSQ7z22AKxrk_JgU3jHf96UdmY81f06_fkmEeZ2LBlr9zjgGdMVl2R_oyD_6xNWiS5DkhqjpaUkTV27xCO0tH2ppdcPQmBObv6SVWMbDIECeXyyNWpNpFlUa-VH_ssd9ZY4awiWWZkAEvepQvkBDtTlpiNtqAKr8laJFHY0ZsSZFQe9MCNSCMF01vaiHxZu4BEB8w6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/persiana_Soccer/25975" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25974">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iB0IQ4l2gg9I_2mSJOqD8AMeQthRAg4HAPPiF9jZZJT_oAtzOvOwuSAXADFHNcpQK07y8Xjm7XYK1CBbgN_X-TN_U1eKJp1tcV5CT90LO4pdDhzEB8xah33pLWKRsBqhimpuomN5Jfh_MtZ57CpwUmkUqV_djeIC9Sw8A3FEfF6mt1Btde0t9K7xzqPX1QE35BUIX4rtOIQz7WWRttyzs8jAQgTrE-eCZDKe-WmnGOsfYM_RhhbtjicWi6ELnYr3iXRWyz-eIiyE5h1Qa2tBgfjlWan8DIyoZ2CfGvFHKT2VZ6aZypAETTwUUt6_aj9nchyeiIGQ6JnY8fOewjKo-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ آفر مالی‌سران‌پرسپولیس به آسانی برای فصل اول1.5میلیون‌دلار بوده و برای فصل دوم 1.8 میلیون دلار بوده. آسانی فعلا هییییچ پاسخ سر راستی به مدیران باشگاه پرسپولیس نداده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25974" target="_blank">📅 11:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25973">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=hCZsqwfVCc9LSCr3867YQEW9OtoqBpY3127oUsNpCWrPFniJ6uqTP0a8z3n0EhJCJ2UPDaC5Hz7hqpjVCQfOhZQ_YTyJqnbRVeO3uXo43ehodRUocENnQf4iyCNPxrzYTU3bZap1YV7G-QlIozbDm5tnEHvxr8VLwx8jwqdHlcFxtGsm_37BVpGTuhLOZxr0BNlNC1J791hrNH-ZMun2Kd1A4TH0fKzMiws62mAa0Gcg1XNoAml_Ai1Np1tTp7jFKOn2G-okm0SR70QvwJW9xMUqw3WtFzN6zDfS-iOb9sWmCbzA-BGVr9ciVr3coC5S-th_zWUvLVTyg8XLjkWdWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ceab272ed.mp4?token=hCZsqwfVCc9LSCr3867YQEW9OtoqBpY3127oUsNpCWrPFniJ6uqTP0a8z3n0EhJCJ2UPDaC5Hz7hqpjVCQfOhZQ_YTyJqnbRVeO3uXo43ehodRUocENnQf4iyCNPxrzYTU3bZap1YV7G-QlIozbDm5tnEHvxr8VLwx8jwqdHlcFxtGsm_37BVpGTuhLOZxr0BNlNC1J791hrNH-ZMun2Kd1A4TH0fKzMiws62mAa0Gcg1XNoAml_Ai1Np1tTp7jFKOn2G-okm0SR70QvwJW9xMUqw3WtFzN6zDfS-iOb9sWmCbzA-BGVr9ciVr3coC5S-th_zWUvLVTyg8XLjkWdWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
🤩
انزو فرناندز ستاره تیم ملی آرژانتین:
بعضی‌وقت‌ها واقعا خودمون هم از خونسردی لیونل اسکالونی متعجب میشیم اما او میگه من یقین دارم که‌دوباره قهرمان میشیم. همدل شده‌ایم که قهرمان شیم و لیونل مسی هم نهمین توپ طلایش رو ببره. حقیقتا لیونل مسی رو بیشترازخودم دوست دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25973" target="_blank">📅 11:47 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
