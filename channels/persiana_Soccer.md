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
<img src="https://cdn4.telesco.pe/file/ByJo-9dl89Khdp4gk2KH5hMFuiT452PcrZi90zHfIs75IwHbZB6rYJgkT6DzNhuVUQoDv832gkclwpTzaX_cysIlIBR8AIPACTNcGXlJybR-IsGuR3Xe3ti0whTYux6uUjSzM_lIfb5wacgCk1lC7CbfBBSBG1aIXU4iPCbFZg9mwI3QifZAYkNM20cAViU1OOjuFS_VXvdHPPtJ0leyyzOWpPPBNcDr3DCxXfqRpYqcgJPFWZBhRBgnVBgF3RyNVTuOt9jCPuheSRZJeM3isMkzZeklhwwGCjVg5NVQfu2iuTiS-3XFjc08PfKdr-V7Cpv8labVVcMU1yaJz1p-Xg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 245K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 22:41:20</div>
<hr>

<div class="tg-post" id="msg-23464">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QO_-L-YpaDK-QWcwmXTQFcejECtsmMAPAvTk1CbBUXdCTxIqJP7ZNfkSUWL_GUI9JHx71UxKDPrHt8_tE_9Lc7ZjSfwQrhw2tbAFb9zSEBe-BUf-b7q_t0o9M6IlmNV1mjOu80Wlor8PGeEAeBGaSKeHDXjojTV1coFA4-Bfvae2uRjyoZKyPaW1OmmlT9_4mx9MU6YSY_SjqO_b-S5FdrQUEwIW80x3KfjJPFykoCcnxYePiplSBpoZXy3peqhv_pvGvDXbNZ7dPnk-347OgRqODz0orczIyuVFzEaVFlx2dx7p6sNjw61KneVZ9u9RUCT9qalyKfSWXSUGpSdSsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/persiana_Soccer/23464" target="_blank">📅 22:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_bVHfdUM2rypNlgEMX-NEvfVFZf00WuhDA7kELoFzxA8H4BTbFnGUKss71Lf_AAMw0IlSE1ilcFqrTDCGR2mesHFiiBx6xBjRaIy4H7vGuBk9mMY8MRlHrzzfdlHYHtxAnivvXnThXC6_g4p8NS2NUMqaFo3gLRCDVqqXkgvkoEZMZYRFlIx-FKCa-oW5vAA0XUO0LVqHseZjwexgCzLd882ON8V2c2A6yEuntncQb-K8e41ajSSJ0ck5zOuWpix2Ci4cCNM8kJZJ1Stz3Rx2RUZ6Fpd2-YnAv7f94NbYU5usFpuGtxyKRI3vJewBzADOEoo4fLqDbvoyUVmoEjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nw41JFDT7y69H6K7NI9MFzbjnkBgMV4J3vVdy-1DimgmXGNzzlr5G8csF3n5YtGIXpI2rtrdbzfzC2FZooX1wUb8UBdS2LPohb-seJTiOR991XhKIAhonar_tLydWCOfDozXWb77HD9bs0jY8-xbrhAWsa5CYRlnT48OOYxJbQOFzKdz-SN5_cGYqdZ5fMdeRz7JWlOQy52oXDDo8vwht63PoC3UReBJvPJQWZYMkkKgm3EW9nsccfBIVBZmCtIcYeGz2EKrDYylJCBtD6_30XeOHde0nXcKoA0jPKWj6AoN2AsYZRlvGolLCIdekB4-AuCwjV1VyE4NWA4lgsPnmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی
؛ شماتیک ترکیب دو تیم‌ملی‌هلند
🆚
ژاپن؛ساعت 23:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/persiana_Soccer/23462" target="_blank">📅 22:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4oaCp0L7ezMBTrKgdVDvcnf5PG2O3e9-EbuLGioRT5ZgzdbBq4uf2bNkhOYovqhhn5U13RJIgQyYKAvxXRxe_OKpEx7Y_TJt-ImhsNc1Fq1YxmjRS05mBLsqhED5A43gYub0R5fABI2tU0gxsNfV4y4vjV9SUKwyhjrBZeUf6rw3DXpDxfCB2BwbeE4wM66mJJkAwx78_SManRh5wA91D9ouFJ6fO8LO7UHbk4X-9XNa2buVyrxyGqkoMWNmDFikH-VYVTv3uY2LJrmZo60_oQleJn11xtuu1z_Eg6F8Xu0RTcSz-iDGXu9S802AoBT1CkkjR4gE73sn69gE1xcqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ محمد جواد حسین‌نژاد، محمدقربانی،احمد نوراللهی، کسری طاهری، رضا غندی پور، مهدی قایدی محمد محبی، محمد مهدی محبی بازیکنانین‌که‌احتمال به لیگ برتر برگردن بسیار زیاده. اللهیار صیادمنش هم آفر خوبی از اروپا نگیره احتمال بازگشت…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/23461" target="_blank">📅 21:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=iESBe4mTYHNyjKbAAwUUOLS2x5t1X33GsGAiZr0KL41A0OmASQcpeuR0vcOfhWjmMbnB97PzLR9H3BcHkaB0cfwvU9BIe1ZyA2aLDmPTCS1avV0PKEOPNlZuQyym-txXFJ36QEpL2yEMkZnEKBeD9F9rh-QqkrfBfGA7sQCElBGCt1FGbrP0wd635wEZO5IVk4IyVJ4f1R3PwhmI0K1nLE3r1mNBVdsuqHTdf0dhDhUoOfCIcbE2pC2HSNSI2iaU2QtBdqK2H_AGKla6U68-pyXKw6cHppmF-rA3VmZOnNiAHuePreca07BA8vGOHww7cppzuKYxETS0Cw3Cbq7aEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfc0bbc1b.mp4?token=iESBe4mTYHNyjKbAAwUUOLS2x5t1X33GsGAiZr0KL41A0OmASQcpeuR0vcOfhWjmMbnB97PzLR9H3BcHkaB0cfwvU9BIe1ZyA2aLDmPTCS1avV0PKEOPNlZuQyym-txXFJ36QEpL2yEMkZnEKBeD9F9rh-QqkrfBfGA7sQCElBGCt1FGbrP0wd635wEZO5IVk4IyVJ4f1R3PwhmI0K1nLE3r1mNBVdsuqHTdf0dhDhUoOfCIcbE2pC2HSNSI2iaU2QtBdqK2H_AGKla6U68-pyXKw6cHppmF-rA3VmZOnNiAHuePreca07BA8vGOHww7cppzuKYxETS0Cw3Cbq7aEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های ابوطالب‌حسینی به بعضی از مجری‌های بیهوده،دلقک و بی‌خاصیت صداوسیما فعلی مملکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23460" target="_blank">📅 21:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8GDHVyMSwB0WaxHyAe3A98BVZl8XsuMYSno4R8oWUJZrNAPTG-aZSU1hs_GnZKUArQ45HinPGz9meyUjVx9RDsZ2e1QSdA-Wnc-rGhtGtwFRW6-eeGQpP65AzdEFzgcTYc8W6f5LMywJtGL6-QSD7aGJk9XPqK6Jr38Z6VLdsdiI31MPXEYuMstCjKwZr0sCCVx_cVAhSdAhAMojV2DVhPjmbVsousvAN1knxc6sYJNEvU68banakZugdmebx1wFdp3XDrCfP2ATsjG_d0FRGwfioZZa7WVGPmAf2pomRrUJcqeU015f6X85Nuvm5LKcU6sf71JKqNIiIla9dcg5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلیل اصلی‌ اینکه اکثر بازیکنان ایرانی خارج از کشور علاقه دارند به لیگ برتر برگردن اینه که چون شرایط کشور خاصه و ممکنه در هر مقطع از فصل جنگ بشه و بازیکنان‌ خارجی تیم‌هاشون‌رو ولکنن برند لژیونرها قصد دارند با رقمی بسیار نجومی تر از دستمزد فعلیشون در باشگاه‌هاشون…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/23459" target="_blank">📅 21:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeXlkJvKbMl_KSpxzqHjbinfsmTO2LWnh8elmyd6a60twbbvOExWK8dmnD67Xo59gbqnq3uH5lhBZZLAgD2eJX1upDMgdvzkeClJxA2Gb-hZ3r9WXG_QtzRW7pdvNHcxSl04y8Uod3JjtdfVxJkj3ZHijJUW6zI9PPJkZdD1Gg58ujMFFHMuLlLyK778EmDu1m_PEwDA56-igZoYdk_jSBlJ_LwZQ-Ng0VU3N9rgEQM9vMlx8tFarpnvajsDNzhrGDV27kFFiedYVne_1CtDgDubXW0kget4PGTSN2mEau__sYJuF04KrUkBco5pUTTipHxohzsj5TEaqZmJUo4YPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ اولویت اول رضا غندی پور مهاجم 19 ساله الوحده امارات دراین‌تابستان پیوستن به باشگاه پرسپولیس است و درصورتیکه کادر فنی سرخپوشان روی این بازیکن نظر مثبت داشته باشد جذب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/23458" target="_blank">📅 21:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-9mrTb4rS8JGwe1eYAkWQYsJHodWhqqyQDb_TMn3crB9_qaNX7h-N3pSy7L97zfE5P5s07suH1_NxCi2JwxGEFBKGOilNMV9PgGjmni4PmWfmZLCHYrIrZV0kOOd4r0IKkR9jW4MUXvvil6bTcdJWytKvnTDq4IlOTTN6XzB8MwmntHGE2umgwZi2EASpf6ePmeYlMAC38phZbqdXKu1zdA8dfCmIwv4WXxNNTxH16vLtarA3A9ltf4NPtN0EjS3FqET8QEfNi6c9DFZs9Rrq-iQhG1P7OnSCiy4AdLWaUQGl-MA1B7y3coBgAxizMzfj4XwfOT99dHaLAaqHC-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/23457" target="_blank">📅 20:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvX9BJ7OjLLASqYWuqI4uYPEDyf5qHOM7IscyyL6QzqElCEzBAt-TRSxA0mNYR-QwhVVw2ZRhYyOTKIU3cHckrZYQ_R1cnbLGjJ-GNWwoX8RsFCn9LGKpI1Wobuk2Q2lscuc9V2Cv1a_E2WILnkKOmwkaN2uAgMhMGibIN_V9YNs_BMyr1bVQaxoTO_8nucZ2DST0yENj6rQPKPkBqOeVEtelI6TNymlntjwI-Kug5DkMpQKcI_MC9EvqdyA6IZwQt7xsUFjP3K0PovEF8cG9TbAee-_IhSSwxJzB52OCs5MkjLwQwjn93hb2d4mnUvHRZQT5Wxzy5dhbtAGeB5VOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چهار خرید باشگاه رئال مادرید در این پنجره تا اینجای کار؛پرزبرای جذب‌کوکوریا 50 میلیون یورو به تیم چلسی‌پرداخت‌کرد.درحالی کوکوریا جذب شد که اکثر رسانه ها خبر از اومدن کالافیوری میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/23456" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=kV6i-q5JqATGC0EGqHNCunlZF9NtThqVHazTGADyuExm0f8yEFosO_iFqdECUyV44mmAlesD5B6icky9Xj5zyCy1SlhvR3uvSo-ZqIPnp-1zkPaA9pF3qqPbg29e0kixZ_u7Gsz7H5CZQ0UoaWulJFKQjszDPBExYXXSsU__XJKLfe9kmkDuisJr2pg80NZCixGR8bDfMcOLHbeQxGy_ft5WaYLCIf3_mJEfMbBvZjxsOamfcPXOaR1Ve1OJE5kS6V23LRSpP7N8eV-iiH8hObXt57klTTsLwgW-IrsZaVJu-XaJ4UBTBLXDJJ8uYC8ao7FWv1qQc8qfQZn1T5t8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bd12ea167.mp4?token=kV6i-q5JqATGC0EGqHNCunlZF9NtThqVHazTGADyuExm0f8yEFosO_iFqdECUyV44mmAlesD5B6icky9Xj5zyCy1SlhvR3uvSo-ZqIPnp-1zkPaA9pF3qqPbg29e0kixZ_u7Gsz7H5CZQ0UoaWulJFKQjszDPBExYXXSsU__XJKLfe9kmkDuisJr2pg80NZCixGR8bDfMcOLHbeQxGy_ft5WaYLCIf3_mJEfMbBvZjxsOamfcPXOaR1Ve1OJE5kS6V23LRSpP7N8eV-iiH8hObXt57klTTsLwgW-IrsZaVJu-XaJ4UBTBLXDJJ8uYC8ao7FWv1qQc8qfQZn1T5t8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شهاب زاهدی درباره عینک خاص‌ش در برنامه عادل و عزیزم گفتن‌های عادل به شهاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/23455" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23454">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMsenNJOXQi16lOUTOH0rIG7tApGWIZ-N7kiPRZKfQUAI06clP8xiWKJz4qPVzxmEGjeRsB-vCoQtUsSYMyXfMNqm7sl0Agb5GXOuhmsKSFPg3NiVw0mBlgzQLQqmlwAYkE-geDj6hjZ6xolH1-h_lQKopn_LZHkSIVUsa0fBHNs9PVLY--8TXneana2P1fpe5qtD7WtVnpoPw2KXD6KZEXH-7zXPmRuAv4jiA3dBI_sgdmIiX9oGcD3ZIJBjLImNEBP-vUvOrDD2RWGPK06GSNsmiWqOhTN_glp9e8UJJ6w28Keyk6bXVgaRJlQZPJpOaV0DjqjZs7_VlVCb73wrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی های
#جام_جهانی
رو بدون استرس و کمترین ریسک ممکن پیش بینی کن.
⭕️
⚽
آلمان
🟢
کوراسائو
⭕️
⚽
هلند
🟢
ژاپن
💳
حسابتوبرای‌این‌بازی در
#رومابت
با ارز دیجیتال شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
24
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/23454" target="_blank">📅 20:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqUmJSjyb7lPvxyYQ1h5ooQmSBGr_2s8nP354ThiP65nNQiBpJgHxJ-shlzMHavSHSUM1GgkA_9YkpHJ60JAAsCY0PEujEQOyXBFvHeShaJ1frW863L52Rs0TTyI-aHGAO4D8aEeT62Htx2CcS6pXVQK-HM79uGR08LEjoanlnRbq5eOskE-FD8W5VxknHA2i2ZS_nElVRNs3z6FrSj-bWebdAlfRZivMrPqIa_ANnCZIYKM_9frH7Bf77DWozVmIWDflNaq83iGGSboEmf3Fbx78tgvVntsqsONB8SO7dNfm2dSKgDQLITWviwsFNl3sKaWp-YtNG0qLr_F8XdiUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏐
میانگین سنی تیم‌های حاضر درلیگ ملت‌های والیبال؛ ایرانِ مدل پیاتزا دومین تیم جوان این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/23453" target="_blank">📅 19:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23452">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyg-ANUpF4uk8wiV-UCKktRsRftZLjExTni_sYL2ww-bT1zpQAdanhQeaG8bpqtvC5dAqdBO-V4wqOc-UJZlkr_ygK1lCKnjkusMOUe6kXl1X3PMHX8mcO4FC_BeFYm9X9wduHeoLVbob8KZjS2hQI8OTvhcno_rwWXI08Ugppz1IyziMTii5aUVg1crdAqsb5hX4AnKlf71QgVjFg15QqIYjAadWD6LBMAZPCPgdwOxHO8Eh9QVkJeRKDZ4_WVb7hQRsFurcDL59NSDhtj0wBqSJN-gi-7IWl0nd1KYHFfHvJM94qvlC6MhEeK25pLkZ8iiILyyHRXvA6BtreAPPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خرید غافلگیر کننده کهکشانی‌ها؛ مارک کوکوریا مدافع چپ تیم ملی اسپانیا و باشگاه چلسی با عقد قرار دادی پنج ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/23452" target="_blank">📅 19:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u77ejBKK-aFHkMc4a2NzaUyJZzfyypEbmLt5AbdlcXUR3emeICktC50KZiepqkukf2A8k9EoRxNGpgigZOMG3C2fgQgymSizCgGrzH8rc3bPRNJeFv_aQivQPONoCThfsfy_9oT5TAPwwnH7Q60oF2N31SgaZRXnHsaH4_OqOYQrC-3YAxESNOO1eJIQ9mqx01d2zrmO-QWiMMPsXQFWZ7ddt4zoMXmS80RKfYqthDOV0KcGkjU-x17V6WzYaa9qge6895k4whRi3zCDNADdW8MsfMxGrpWEv1Hz2G-oLNlHW21vhirijuF-aWOlSQSVkpay4Ol-Hnhmlb-kvFSrpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/23451" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGlXIDj9e2ls1zwsFITN_AJ0JF4ywLtEDemxFakQ3V7pJle6R0D7ZvhU1nJWIl94TBiI9GOFOtY2VbOXTdhWN12_clzlsgc91o87NcSyI4b3BwJ7TkAkigQHWkHcd-veLXTc7Wn-muTM5XDV98ZX2WAlYBu_OF4oyHQFatLDzudtwiZFeNDXfPO-7btCYPRUVZo_XkjdaNcxdxRohACwoQhKK8v-0ta0GIcV1nAdDMiKi_ymSnUlFTGuu0zpCTqaKQlfwaQoSj5fCFAJv7U3MvKo_TWFNNkX_vwlGOmZI0Z4OLcFkxmU1iH97vOCTLcajRVZCxlzzA3o-XRHLaBbag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/23450" target="_blank">📅 19:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=g_rV7nU8NVUImbhZPrisGP_3mv9Yh2SI-31bBRjK5j5h0NLMzqb1nU7XxsjqPJahhquLWbzDFxG6wjJKqp0NnH7mSs3mhla0O0R04ZfknoupMCky5edbw522E967VFBG6KHtxXL3khdlKliFFFqpJgeK7JhUrLe1MF-Cbi7mN6QTW72FdUIJWQA6kGvZweO239rOy1pbejNjXI_0qjnR-K45xOZKlpzqNX3PtlqFt1ZT13fXCJfCQ8jluT8cTEKQyHezPM5GC88zhObxMPCkhYnTjdPJLR5ErHNGXeF1Ony4OHC5Y2e-aEbUxrQrV8SMSNMS-0Ktkrl2lxfQCQ_vTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/129e645eb1.mp4?token=g_rV7nU8NVUImbhZPrisGP_3mv9Yh2SI-31bBRjK5j5h0NLMzqb1nU7XxsjqPJahhquLWbzDFxG6wjJKqp0NnH7mSs3mhla0O0R04ZfknoupMCky5edbw522E967VFBG6KHtxXL3khdlKliFFFqpJgeK7JhUrLe1MF-Cbi7mN6QTW72FdUIJWQA6kGvZweO239rOy1pbejNjXI_0qjnR-K45xOZKlpzqNX3PtlqFt1ZT13fXCJfCQ8jluT8cTEKQyHezPM5GC88zhObxMPCkhYnTjdPJLR5ErHNGXeF1Ony4OHC5Y2e-aEbUxrQrV8SMSNMS-0Ktkrl2lxfQCQ_vTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/23448" target="_blank">📅 18:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23447">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntHa3ebWQVu7GrGUbZJqjto5ZQW6X0I-bcMozzb7dyn6RsN4bT8qy0QywiiIdLnpte7HRJpjrK79LcdQiKydwTWhKnKCmXvHHxFu_VSKgd_ii4A9AKFVcTovIR1kvgkiEpmMdji6PQgZVmowuHWE4q9uu8OtRb3yWcMtWQ_BxNUJKF1r7sASMLAWFjnDhk2iq9sLgpSc7WurgnsFvSs6m8Jt2YE7DOOwyJkCjv6ztVezLVwEi-m5AcP6XgLE8YM_SlfSAMRSe4w4z7PP6zfxufDG3VY5uqn6dRUb4g4_x9jZgFt-Nukz_Fci-4SDN7dIv7GSMo1magP33RzJU8UUPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/23447" target="_blank">📅 18:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23446">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔵
👤
هایلایتی‌کامل‌از عملکرد درخشان محمد جواد حسین نژاد درفصل‌گذشته‌رقابت‌های‌لیگ برتر روسیه؛ قطعا‌بازگشت محمدجواد حسین نژاد به لیگ‌برتر یکی از بزرگ‌‌ترین بمب‌های تاریخ فوتبال ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/23446" target="_blank">📅 18:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23445">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOpuwLucMeGfM7UnAebsBeWSs5w-fDOxkC0e8hVGCCXvfQCrshlLiuUWTXwoqCnJm2Kx5dL_DjjmbEp85Pxs_qKDtAcd3IyxWfjqf0m3QzBS6OJ9COZ3ESPFDFkv4HNXVKoZZYfCSICKcMOh5RgEf-Y6h_6J2LGSyqKU2b2X5s8Ag0S325CbenrbkJA7IsfQK9b7WbqMKxh3ZfQVKkoxjNWSPK353kGUu4jYzhJvHKSetBOCqXYTaU6F4Eu06ViVU0XGXXX9Btq1uRbwy1SONJYOh2ZfiHTDWtZyLzKy6Qb8W2qnwDqphS53paPlE9or16vKgwWMJ__hymbTuvmySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛
رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ ایران میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/23445" target="_blank">📅 18:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QFTV14vMzcjpl2tfzV54lzj8oNLV-KxGWGJvErTdorhdGssfxraDZifcPmlonJ24vzYcGqSXN671YqcjQUCpzU-6E53HVd-U9VN6RPY4mMgDLpwUpMOzfP13vL_JsXIiSrLz6icqUZfehUAZHkE91KwLB_wHjnZ7SYiOznkBPuQWM3VdgAR8Ydzhavfm-G1mGqDnoja9AQ7NBl_lvbkHZUxjmqzYB4ODkqrFeGnJPWblrmZ78fvEtlt_bLAejAAIvZ_8csl9wHBlvIEHHgDaIVJe6jvRpzPDm-ruMjQ4vpHYFjvOYwlfp6hqC3vTktsCYNP7tZHIkT2w5S0zQsrEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سایت اوپتا پیش‌از دیدار ایران و نیوزیلند، شانس پیروزی‌شاگردان‌قلعه‌نویی را ۵۳.۸ درصد اعلام‌کرد. در این آنالیز احتمال برد نیوزیلند ۲۰.۴ درصد اعلام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/23444" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=CHC-jvhmpGfhImjviKe9LSgh7jX8aYORPLFwzEpf_88OZD5w9Rg6bKoapQi0KE1jXXXqja_vP-3jKH8-rXAsUxkOxd1sLqv5IM7XJZROMwwQusB-Y2cHBZVexMMbqweSZtz85qoG1zdjwnivDobPpr-VTUEZuNVZmqURHYZ-bRxNQSP-HMXJlQ7FLupDQN4Jr993Jz6F_aaBhd4Y-IxjyZtCzQFS3KB2YcFsMbsVy30sheRN-y4z2skQ3s3fc27np7D8LgtbgN-zfzNSiz7QL3deHfFcTv1bRL3PTy7FG7lXHRid7VvdwXuaXkjFJvYfpvSqbjciFoHdJoDqqkJMjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d6eb70176.mp4?token=CHC-jvhmpGfhImjviKe9LSgh7jX8aYORPLFwzEpf_88OZD5w9Rg6bKoapQi0KE1jXXXqja_vP-3jKH8-rXAsUxkOxd1sLqv5IM7XJZROMwwQusB-Y2cHBZVexMMbqweSZtz85qoG1zdjwnivDobPpr-VTUEZuNVZmqURHYZ-bRxNQSP-HMXJlQ7FLupDQN4Jr993Jz6F_aaBhd4Y-IxjyZtCzQFS3KB2YcFsMbsVy30sheRN-y4z2skQ3s3fc27np7D8LgtbgN-zfzNSiz7QL3deHfFcTv1bRL3PTy7FG7lXHRid7VvdwXuaXkjFJvYfpvSqbjciFoHdJoDqqkJMjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
برخی از حواشی مثبت هیجده و جنجالی رقابت های جام جهانی 2026 آمریکا از زبان ابوطالب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/23443" target="_blank">📅 17:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1q5_tkr583yZlcmGNxW5hMW-71q1vvHhWsMjZf6RHv6Co9Hv8RSO0NlUUjUJ3_cogtu5vl-hhK6wCuJJEMV5JCOlTOUw3omxFEgZCCssiq8Y9S8VdW83S0cXfoxndHc9snljmeC_kjwCj4mWv0OSxVPi_FG80CS2BffoyBHH6DIN6pTltFlGmZi2LIIKKLsy8TA37bM463_R9juhASGriqAPepzWqNbV57As0H1KIKKftgqzyGoxwrU7TiLGxbSBOoBjC__irxFPv0XNDRottOZrWfErnvXLOJ-BoFEC_YfNvH-vP54E8A0JLKLRIMmVnhn2OLkk7KvIcIklEQjnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇶🇦
صندوق‌سرمایه‌گذاری قطر اعلام‌کرده که بوعلام خوخی پس‌از گلزنی‌مقابل سوئیس در جام جهانی 3 میلیون‌دلار و جدیدترین‌رولز رویس فانتوم به ارزش 550.000 هزار دلار رو دریافت خواهد کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23442" target="_blank">📅 16:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHcHKWeys1V4YFOenaLFIOe5PFhKWBJMXlbAJN34TlzQvbgmUQiWjBGcq7A1zYvD6iePEV1hpyvq9bQ4d66o3yfpbHT6C6Hy82bWIjIdGV7cZ6MKtQhnbgAqHfD7elEETE1fxj1i-WrobG8jzInr-_uE1UNiPE2apP4UqTsXHkLtCxVGYnbWjTJ7HInXfqR-_5Be7zof8kTocceOWkzqr9cwXneliOgfce8TMq30wQy5_m4K0csYaYZXN85WFxQ801YYlzAWqRO9UWlpyhQ8xK5hk1mRjh5oWlPn05g4nLfWr8W5gbP5pEMCReDW95v0Wrhdw7_iRxwiTU_xVUuDEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی قطر
🆚
سوئیس در هفته نخست رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/23441" target="_blank">📅 16:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_esjMMP8QUDEUsm3Y7iLbEuvHXALThsa4ik5lv5ff4jk6iG5LX7arGAmRF2kC6QNEX3x5Wb6voG4IOMBTs6u2MtNxeU6cehlc-HIGa9HMJSCo54vU0JbDQd0RlRH7V91D_osqB_uHKQ65sZkfN_jXMA3eh-aBqm376ACKXHWPP_Vx1uxBmmEaOJF9cVkt12Qww8t0adxQdJ9Bz0RVIkwvTAs50SoMEyJrBfwDJ62bgIZEYBgkIWyIUqLJ9Z1MNSGxUemnuFgp5wUvapkhYazAIwWy0zHsZdcA02XUIhnkvzUH4l81I96irs7C96almXQGaercaIVEyQK_jRJkOs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شبکه‌های‌رایگان‌که‌مسابقات لیگ ملت‌های والیبال رو باکیفیت‌بسیار بالا پخش میکنند. امروز حدود یک ساعت دیگ تیم ایران مقابل بلژیک بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23440" target="_blank">📅 16:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM31o9Uj2fDDwISryWCnjMniJ9SslwhCTwt5myfQv89a9TsWkU53QCAo__NC5LjOooMtHLkVk0kkoWj_I7xV4M0DHHGgKX2ALmNthjd_I7OxiuPawh--QpTyTAEWJEz2ibf8cGnPm-PNtm7GwSv3NL5sy1a-oYGY9XTTydaoyMx7k3IwoBSf_Zo-2mn4TEzEpU-UhQGykVMNkCo2aHXQ3-sVd6DgDQ7LIgY6fTsoK3nchSUVZjzqm9mXUtx8LQM2lJ6h7GWpx0l5nnnCGFBpoabydpdCWRfGaNcDay4sPCez_Xul2_YxSTBKsNv7SnKPH3DXJxslzW2BdaM3urzCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23439" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoEVJ6DHaeaam9CEoe8ajbVt59SB2KjUg1nlclRpHcHQ8CZKCpfYKeZB2nTuFn47aIT3Uxo7jX-5_VZiDgKFyUukIYvKmCOiqRBsTC2G9t3UbKHW9UBPdBFaYlTX6of1NV_ox5aqWBp4kSpb8fRHAEYgDTb8vUK_0Z5pZUBprNgeA_OActDl4Ie9vG2cfi-jfiR2T5yqu1ZynSMse4pdfNMl7tB4LjmsgeduOMLYa1J7__k1N09J7Ba8TFdB0qviOpJlZgoX4FCMD-31nxzOStUN_gF57DmzmeBjdrivdJGn_ivQ5w0bbSA3MoCtnzhhC-jKnODnU0KTddTL2v-c8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23438" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">▶️
قسمت‌‌‌سوم‌ویژه‌برنامه‌‌فان‌ جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید. شیت و محمد نصرتی مهمونای این قسمت بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23437" target="_blank">📅 14:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=k2Bsdo8smrptu0Y-g0GpEb0o_t2HQBvymG9RBuTEhzs3drd5Wh8_1PJozisfCQCZHH77Y6-aC897dv8LqT6K_lFM0wL356G2DP6bj2dF7QL4mwJEHN3p3jLXSWImZ8nTib9bhzbbKWOiYj0sDm1HqDt95iXlKYAjLOYigyEGfsuNHOX3rph5X3kY60kHjYpcXb2brfkguP6Ag4lGleRUVQBm37sZ2i48WEbte3Coex6yPMnxdzRixVoq23SZEkLOe6H5-7ZQMyYF17fqN4_dGQS5IiZi4haSQZAOhk3nGHQiYOINwOxQVWHkS1DmEJlTTwVVkC-bL98TQDfdpJchOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=k2Bsdo8smrptu0Y-g0GpEb0o_t2HQBvymG9RBuTEhzs3drd5Wh8_1PJozisfCQCZHH77Y6-aC897dv8LqT6K_lFM0wL356G2DP6bj2dF7QL4mwJEHN3p3jLXSWImZ8nTib9bhzbbKWOiYj0sDm1HqDt95iXlKYAjLOYigyEGfsuNHOX3rph5X3kY60kHjYpcXb2brfkguP6Ag4lGleRUVQBm37sZ2i48WEbte3Coex6yPMnxdzRixVoq23SZEkLOe6H5-7ZQMyYF17fqN4_dGQS5IiZi4haSQZAOhk3nGHQiYOINwOxQVWHkS1DmEJlTTwVVkC-bL98TQDfdpJchOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وکیل تتلو گفته‌تتلو واسه‌ماه‌محرم درخواست مرخصی کرده که بیاد داخل هیئت‌ها نوحه بخونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23436" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=s0JDDJqxRficgJO3xZBhBcCottRso1UG6Rb-wUgerqrEGHShduGPBIvGmxOahVhPioMhGEkfYhZ_BBRrl7eHUwbg_2ExSh8Vo51duObxbtAX5KV6AqlcU4S-losX3ZQfgrCZcOQ6GALaa2gec8ULfcxUC02QwuwG05gGQF_TyT7AP9q3w-1Nh0qdISKFRuhkumpMOn_NETGTkBvwTm4vrxcUW_ehYoep2CYJcjZXwUN65KZPFjUO6_h6qzT9YPEcwgbXvSmo2oRn3souqRwtfizHlm12JZyBh5O11v6qbiavDJOzUH9YEMnlWz_iSTp7a1ivG0yyN2Jtvb2OUx8FhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=s0JDDJqxRficgJO3xZBhBcCottRso1UG6Rb-wUgerqrEGHShduGPBIvGmxOahVhPioMhGEkfYhZ_BBRrl7eHUwbg_2ExSh8Vo51duObxbtAX5KV6AqlcU4S-losX3ZQfgrCZcOQ6GALaa2gec8ULfcxUC02QwuwG05gGQF_TyT7AP9q3w-1Nh0qdISKFRuhkumpMOn_NETGTkBvwTm4vrxcUW_ehYoep2CYJcjZXwUN65KZPFjUO6_h6qzT9YPEcwgbXvSmo2oRn3souqRwtfizHlm12JZyBh5O11v6qbiavDJOzUH9YEMnlWz_iSTp7a1ivG0yyN2Jtvb2OUx8FhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23435" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRQIB6I3ndMOGJviy42R3STn8axthljIEYzW5OCel8yKFE5Z6FGfQrsa8kL1gq4_9j5ID3Yu7NXjL3dXB61CMklVOEkzLSr6O-6bHboS3Eal-SgWQe2VGv7yc6IecSq0qVoxZ-dQIL32qG1vUb_whkMzh-CSOa8gLQaAVOjpc-85j64ZHNrfnyolykNgyGgbwx_UCJZFLtAUuTXp-z7rk4C50cOXQccFASc3RQPQDK4oY4tUDk-JYyR5J4dE1jBR3XFRjdzmbwdV4qZsnPJ2SEZgITCBBx8keGvXqe9cIvadqUkjQ7ovZ6RI1opIqXK8KSYfr62UpGNEy1vdx0QfMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
با اعلام فابریزیو رومانو؛ سران باشگاه آث میلان مذاکرات‌رسمی‌خود را با روبن‌آموریم سرمربی پرتغالی سابق منچستریونایتد آغاز کرده تا درصورت توافق نهایی بااین‌سرمربی جوان قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23434" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=OY1d0Gh7Qjqi5TOFoGcs_1-PBjE5JpOa4JG9bWEkpalTjk4rwa7TiNJUa-GdavhKv-5TYRLMrs-Q3OlQDxe5wlg891dbqS52t_dr8NmIfWFNwaDHYoe4qpdWhfUVd6ppMyrqDtkwfW1dNyKk0dQcJIwCncKWzzfkrfUcXVbqmZ0y8cuL6PQJK6M-CyjafcHYk_OanIEO_SxzudzfqYGELlAPJVAWAvaPcE9HdEFQ_53P8xvHhjEauS7oiopJae8ZXIRejvEvSC1AVQyuMVuDS6Q4r1Fo1AQHzeDSs0JvPqybk_K9JI_GI_2D7o-eiTcBi_uOzKJjkV-1sj4hAJY-Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=OY1d0Gh7Qjqi5TOFoGcs_1-PBjE5JpOa4JG9bWEkpalTjk4rwa7TiNJUa-GdavhKv-5TYRLMrs-Q3OlQDxe5wlg891dbqS52t_dr8NmIfWFNwaDHYoe4qpdWhfUVd6ppMyrqDtkwfW1dNyKk0dQcJIwCncKWzzfkrfUcXVbqmZ0y8cuL6PQJK6M-CyjafcHYk_OanIEO_SxzudzfqYGELlAPJVAWAvaPcE9HdEFQ_53P8xvHhjEauS7oiopJae8ZXIRejvEvSC1AVQyuMVuDS6Q4r1Fo1AQHzeDSs0JvPqybk_K9JI_GI_2D7o-eiTcBi_uOzKJjkV-1sj4hAJY-Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23433" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=ray57gYoKwP_ArzSBdyecYYpSLkSbMCRGPoMtlUard-HzeWIPD4TfZanTz9xaQq6DigZnfBvL7X1fclo6HEBYS1x9xoYDq4Ws9lMrFc6aB3n-fc3t-hkDJa0Ievg72kWeO8lwE6_XuQST3wrkBzItofNP-MJ-Q5zd9zQ0Jtz9tZw8G1lypm11A5iXlMrf-ZGJNE7d1YLSaqyxxBvcs8xU5MYgx6kK62g38kUemm5yupLZLkhpjHrM4zmLbgSJW5PK9gc_DNsmp2BolD__yFR7H4dm1ELFAIPHni63sMvsc3aDqqmvOcCqIm3ViW7fn8DuYBc6tn78FMhqcw8B_94fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=ray57gYoKwP_ArzSBdyecYYpSLkSbMCRGPoMtlUard-HzeWIPD4TfZanTz9xaQq6DigZnfBvL7X1fclo6HEBYS1x9xoYDq4Ws9lMrFc6aB3n-fc3t-hkDJa0Ievg72kWeO8lwE6_XuQST3wrkBzItofNP-MJ-Q5zd9zQ0Jtz9tZw8G1lypm11A5iXlMrf-ZGJNE7d1YLSaqyxxBvcs8xU5MYgx6kK62g38kUemm5yupLZLkhpjHrM4zmLbgSJW5PK9gc_DNsmp2BolD__yFR7H4dm1ELFAIPHni63sMvsc3aDqqmvOcCqIm3ViW7fn8DuYBc6tn78FMhqcw8B_94fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شهردار شهر سیاتل اعلام کرد که ورود پرچم‌های شیر و خورشید ایران برای بازی تیم ملی برابر مصر مجاز است و از ممنوعیت‌فیفا پیروی نخواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23432" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5WQkuNxwdXYpnhretV7b983HZ5buZhts59fcCx7hV7QtW63QKgTdl-s0Xa7H4FjmliV626Lc4XouKiLZIfJJwpwI8lE4WX9aayZGFOnVIir7ACmOJ_NxCIvgEUNKyDukT7JRWEkv-HApaJHakiKymbjQEurfX4C7MBWxYe2nvjdSdK7tgJkgVjQmOioZOzxlkWXDmcvx5hno62ezJfMZGMt4J6ftCIWpFAR2oWVZjNPwiEb8tsw3EEdxx-Zp5TMMHjhXdjI1NqjAKCV7B5o75SYwZUp_Cw-1DWSnAzNrdHAqpN60IIe43YLxoEivltdbG6AJ9KcNzxNtLVxtaMATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
حرکت‌ جالب‌ و زیبای فیفا برای جام جهانی؛
تیم‌هاییکه‌سابقه قهرمانی در جام جهانی دارن، لوگوی طلایی روی لباسشون‌دارن و تیم‌هایی‌که هنوز قهرمان نشدن با لوگوی ساده وارد زمین مسابقه میشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23431" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Muaqc-Xav0Jo1bWiuW5KyRblEo_tV3gsKu5pSw-q_FSwDwzmtGCLeUHNmMh98OO5kpFzr7ZvJgPcUJnNKbnX8Pg1zrOZEplmDtSotcMsjXI2ccWBtbP1d7UjytYm3yMsdRwGbj0URaI7Dx6AZMFzDg34ABjhaii2JrpF1el6pquVQO8rR7Xxt1b0qbuSPeTjFrs145g312q4WTc_orXisDPXnoVmU-Okr7e1k5RDnm0PTHmpDm12VOIIOvLeopQINA-gTcQ0HrXGFFqS9yhUVV422UOCwkgOy51G0Yc2tgPT7BNfC34Z9omRKDfQmyUedoQltB3B2OSxtHbY4UYZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23430" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=rL4pMbgkqsbwJ3feTrR-tn68UzYbfv1Iry-umz_-Pz_QMw8nvT-iTb41VviA1B0Qa7WIP4CFwyzQi3tCcsLjGVp60JujNL4cOaQK_Usc4ttFdQAn-1IHFs76ktxmXCrOUvYU5F18YntvglntJr1Bp9ye7oPKZI_MxP8Kwk1g9z7P4ESpB4R8AigXCQqT7HyzwrAMB-gKWk2QJBp9vdPbM6N5IEY8vwiky_nQ8uEMgqxlrqvUqoIsMJ1iIx_QvX_vxEzwkItWazQm-escHZl9qfToggNK7bVIKWsGY4EMmKX1KTNpYC57WhdI8morHO-yOAKpYNws4y_iec3EGo-qog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=rL4pMbgkqsbwJ3feTrR-tn68UzYbfv1Iry-umz_-Pz_QMw8nvT-iTb41VviA1B0Qa7WIP4CFwyzQi3tCcsLjGVp60JujNL4cOaQK_Usc4ttFdQAn-1IHFs76ktxmXCrOUvYU5F18YntvglntJr1Bp9ye7oPKZI_MxP8Kwk1g9z7P4ESpB4R8AigXCQqT7HyzwrAMB-gKWk2QJBp9vdPbM6N5IEY8vwiky_nQ8uEMgqxlrqvUqoIsMJ1iIx_QvX_vxEzwkItWazQm-escHZl9qfToggNK7bVIKWsGY4EMmKX1KTNpYC57WhdI8morHO-yOAKpYNws4y_iec3EGo-qog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های‌ابوطالب‌و‌قیاسی؛یک رولکس که قلعه نوعی بهش وصل‌شده؛ عروس‌دامادها میتونن با پول این شجاع خلیل زاده رو یک فصل داشته باشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23429" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmy4KMIBDv768T0BRzlg8ntc36mtrpvHhdxbnVi7vgT1JpK5ng5ELHtqv7d28HSGYKC_WJ0Hd7S-UCa54RiEVuLqEDL44EBS7mpqvMgEqTCpMk6_rNW9IRkeF12-VL6GAKtaH712sO9nlhE2-BtQzkKYModsT8SKOaEabCF2oJyxDNH2IrKjn4yEKJEm_X7-iYC3WjKzaQR7vqU_RQ_A8AqtLmOVxBdjTzs4uBYWWZ_2YfbA0EODGYnIBoqiSNdsn3WkdejNhj8ttsw7mZsoSfw2T4FNNi9cMrYKC12gNF3R70fi0JFd77GTbCpAolKnsTm4sj4DMjQLlTvJcm1WmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23428" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_gUUk1JzimEgyndns7_xWfgScWSIW9obQ2FKA13JSIDmTKogWpbTUGAvspJdxTDwA1bK3EmuJCsPhIb-NddFJS7uiIk4CURPTmPuAvIzFdvO-T2gqi6QYr4Q920YapsE51A_wu9D7PB9zpbuC9msGa6grME7PNbGdzOaOfPt-UfiO0gJOn8YcY-NbFPruLlZIvz7jP4s3oxPNYwZRkshX9LD0gokDqVYosbs_qr_8QV5oWcHSeL___jMk863TLgpETkQTzHyb-0YxxQ9zonR0upSlD9hkn3ZuVWJ5HDw1EKKaxaLCFY0pYZuaK4MiE-7-7h3Xig9hPyexKHXpVZaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇺
سرمربی‌تیم‌ملی‌استرالیا در حالی تو ترکیب تیمش مقابل‌ترکیه ۶ بازیکن با ۲۳ سال سن یا کمتر به زمین فرستاده‌که‌سرمربی‌ایران در لیست ۲۶ نفره‌اش فقط به ۲ بازیکن از این رنج سنی اعتماد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23427" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GILSA_pffcEB3E9joRzED0-jwZx3rltpoLyVjCuD4P12N6ogx8tI3Y_a44K-3n472pkbtvDs09S2CfLmu7V8khLi5S8x-TtQOty_zhRwIM8b_G_iyVIxvCe6iRAwmpJVEhLBvp8h25ppsKWMXQE8bGoJYmqifbFK1CmWQIEiFQW3Rm1QZlIwVRPDA93c7VgXCB1ZKwukgW4e4SLaqCCHtw_dbeulzR-bSxCKrG8cJM_YjCU4K26E42FjuRGVSwxtR53chCqI8M1d-aSfam_zkIBzqNWFLjKfm5vUiSmFEgK4sht9Wjwpl2CgTu9_TmQ0uJDjrS6o6Rx9gNz86EOQKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23426" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM11xQUHDJK_h6bxBu0gv1vA7o6amKVC_t6eBguUV5zU3oCJVx70szZu1jV1wzyHOe3OiWXQq0Erf9KePMs_hQ0aVZk2tbLSV6uVNcwG1eu3Q3-g8XgKv-HqFI4bZRXHWZK2sn_hYekCCEmrWKBdX71XJTVZb1IQXOdtZp8GAWCxQ7H6CntndQZ88oMrmeQsb4Dr3_ocgkwjXoDWOvPUBl280fqua9D4sND28Ci5UwiP17t9NnTssAanLEn-7UVu6tT_rWk5i4_UUNuueWfKbfdTGclFJRzin7zqxBwugXckfPJtr-qb6pTF5BHzwG42WMPuhHisrhlhT4IILsvmEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
⚫️
#تکمیلی؛ روبرتو مانچینی طلب 15 میلیون یورویی‌اش از السد قطر روبخشید و رسما قراردادش رو با این باشگاه فسخ کرد تا ایتالیا رو در یورو آینده به جایگاه‌اصلی‌اش برسونه. مانچینی در یورو 2020 ایتالیا به قهرمانی تاریخی این رقابت ها رسونده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23425" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PtZFRCYDQHJckfP58wjS5K5Hp4mpZypUDlO9dZpToYT1atQ6Af5AKby05tAIXQPGQ-VQUMealgsSsW3qAqzoI1cPpCraAEdn1eI6lXbFEMZppMLwXmDAFmlwxS2NghWl2cwRG2ZjXlTr9qIKV0uhe4I6JE7zR0vjuU0m2d_q7XHjrRSfdRv7hidlYpIxFrvu4PqQP4ANLJt1KrERefSnGWnTzIHZjmW4zGF6JS28y0Q2KGUXnS0RARv-NpKFh6WYurtVxfB8mKTIPJB1LygTeMLQfv5Wf2MFjquRxi7NXNgC3bA77C7FmcSDze0mE7WVV6u7Fiz3CG-1ldVUhtJneA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23424" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J7K9F0MU_nj5115ZUinWxupeenLDqXFOMJK6kthwZeywOVA8TfDZW2R7UdW9kNEQJ2KF8r0KsSrCwS3B9tZzbccSs5ec2_T-tc5A13OrIy3mKlWVUeajlrp-NDCDGKv5hZFvU5z0LWfNPuZZWoKY12wAQRTLcqksJAYg20AVKalWHzCUhwo9ZcShL0GyMBvn_lcwgnt-C2TjachburTZLltz4YtkLfuexTrtUJ-_Ni9GB8gsZG4FYmcpRSnXirD9wvafUoLZykaC8cJK8g8TqYQhkdNZBVbW-SZsWpIYFdm0Afqd3IJCA4iG1QIUyDF9RadO_WzjNRUsETFFfeLvcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MelBet | جایی برای پیش‌بینی‌های هوشمندانه
درجام‌جهانی 2026 هوشمندانه قدم بردارید و روی پلتفرمی با اعتبار جهانی پیش‌بینی کنید!
🔥
امکان شارژ کارت به کارت و هات ووچر
اسپانسر رسمی جام جهانی
پشتیبانی از زبان فارسی و کامل‌ترین برنامه موبایل
قرعه‌کشی و آفرهای ویژه جام جهانی
✅
حرفه‌ای،مطمئن و درکلاس جهانی پیشبینی کنید!
📌
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌ Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23423" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voWvZZjVfo8hCbfrxMooFtHcjVLylS3h5L2cbe4FbUMqwRvj8-G-EQ_Z8HXmuWtG-iG5-lBP350GWaLQ5JwXfm-r5Bzxx8tmJ5CmQxgHCtI-L39pe4aVrmRtz4Pan_EzmRH4bX8q1gm16YPbHckdEHgGqd8mbA0r4uGO1Is1VWTe1Box1rdcTSnPesTC7k80vcsQdi1StVZRW4wz_v6bvZeLUAT8D65DRQNyn0ulZvldfzLeqK65216e1wj3f0AA-2HygbGLw5WCVv5gEar3vR6DUIQdjiJo6dSeypYala_kwkvYopijIk_yMzvyMFYOsQn_VnzLmO_iNf1yxzNCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23422" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpkee0C1EO0PvvBz3O9mPT5ctHkfOFICfYFHC-hcKix-Hx7hk1hU3b8KuO1DjGT000Ns_9AUH4cnYaXFf098AjYaO9dQ4KvGZPFbH0FZPgKC80UJrernUZdISVLlADqRWJpCTF69pSy-4D3XWfnuPIoRXisOePuU1XSbLKkMhrjxSXSa4-EyiFWXYVAFJiLre3YuvEjaHSOq-QO9H5z48uK-QlLN6Hob_mIJTlVnt-LYT9MaiDHWHFxR7LUduqvvZpC1QGCnc5WEPoitgzkYqPYMrWphGJuuzra7B9NYMVUbdRsBzHrvxPM7wMdyY2C748UQxfAbqY31eiqpI_KtEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C و D رقابت های جام جهانی در پایان هفته نخست؛ استرالیا قاطع و دو هیچ ترکیه رو شکست داد. اسکاتلند هائیتی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23421" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KqMnkvUXZuLJSusl6doL5nuhjCZ9NEWG4cQsomgN_eXcL7XSgdxPJ9PfGFHmnWJVaZ5g7LQdkmya1PwdnJ0NZjIVdltUxTQ2JXAXZi1sbtjob5UD6ci5F8UhCQE0V0xVdITa6BC13zizbZ4iwe24Dq7Nj9o5ih-9wQLH01a78yUVwQWJnJZI5XZA5YFHUcu73wbIsrOUK9cl0xXRLoAyqxonDyFWpSnXmkln_ntpGeIvM7q6uTIUx8fFdz2It45hl_5mUGFm-e1rQgWe2gPLEBExcuFT5rZH2svYvuiyruQ0kT70xgaeSB-cMbwXg4lC_0NDbgp7dnxXWO37EQIWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q5sfpYaMGVkELUECrJiGlFNEYSc4t439NgtNteMj63xZFXmwO-GDbjntx5nXhaes_xOcXQVVJt-C17RpYVhDmbtkcXihlsev4EZiZk9PSdRgIMdxTruwfZTH-qWzJMynoVUP8l62VcVtIPedgVuaijoyeiuqpAfCiOoC97fuIdPzL03VojHElwEFA6ys3VOoCg1AEBpOS7mV1cI3NjW7-HjW8rP2byy4RsWjzlZh_PURWu7K2EvAYxVQY6B-L7tt3Wna_KX9NZJ4kucRCOjY_CF6FepKs5q4HV_F3iViL3QsbdfxVfPj9kXunD-5UwMs9B-BeEXR7XqVKkU3Kx_uQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی کاپیتان مراکش: اعتراف میکنم که در نیمه‌اول روی اون‌صحنه باید اخراج میشدم که شانس بامن‌یاربود و داور ندید. لیاقت‌پیروزی در این بازی رو داشتیم. هیچ موقعیتی به حریف ندادیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23419" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMTab4Xnyum3WSrrjVBignZ5tZWwUI_DOEQ-pFMYZVdulb2ksmFcn5RLC-fQMNc8Nho4FcCCMju4H8L7VcnG6ivRn3nGpN46SHVwaa6AyHAfrNDCeMqpjqnqad3zmvOe51GY1npRlPIwnvIqMbvsBHHqw0oYp_IFN8Y7cpndn99OuI2LhoXVRR2tLAFw0mpnYSoOtpKg8OKiJ3gg3mQUXPrRIt2LBE6Ehd7-WOStTmwbqrrBHO4_eZI96cQIE9W7UdBvozGLji8odb456Uami5y25Sve79WlQbGInhs790aXbWcuA2vI_32_uQ_-fHS-S_g5had-lLzxdPTal5tPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=F2OU3oGgpHfgd7DJ-ZZPqeBFOCinQ59cHmO3jdkh7r0LJFQ0SgiQEWZUgCWsmyhspimWXNB40p9Jk1coSn4Mwr4A-_tyDvmH0iFn5Y_xykr-_v7fFTN2_rFQyup7_vagS177WurTn35biiIEUvGg7DSppSlcEXSmRVS0PEKOYok2k2mKc7IVxqoQc-03FsIfkez5NjBi-A1fMIWXmtWMjDqv55y3rIMBJuANcT2MTxxRUHPsuUIMWuy6dI9vgl4n8HC0Mszmzivp3dYFmfyK6laqMGycAbkcFiKURqo9N-YTRaBCUDji5cZLsNy8z2o8UWAGFS4JH_QwDdP9HJ5SQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=F2OU3oGgpHfgd7DJ-ZZPqeBFOCinQ59cHmO3jdkh7r0LJFQ0SgiQEWZUgCWsmyhspimWXNB40p9Jk1coSn4Mwr4A-_tyDvmH0iFn5Y_xykr-_v7fFTN2_rFQyup7_vagS177WurTn35biiIEUvGg7DSppSlcEXSmRVS0PEKOYok2k2mKc7IVxqoQc-03FsIfkez5NjBi-A1fMIWXmtWMjDqv55y3rIMBJuANcT2MTxxRUHPsuUIMWuy6dI9vgl4n8HC0Mszmzivp3dYFmfyK6laqMGycAbkcFiKURqo9N-YTRaBCUDji5cZLsNy8z2o8UWAGFS4JH_QwDdP9HJ5SQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برونا بیانکاردی پارتنر فعلی نیمار جونیور و کارولین لیما اکس میلیتائو در ورزشگاه بازی دیشب برزیل
🆚
مراکش درهفته‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23417" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGtMrmzFarBV5QuFPEa74LnvZrKuhPa84R2IufgvMVDizr-7iBo0U6OoJCMRfg6rJpAAjxafnohtrYRTywyO3GNo2YCnGgf3OBGlTq6H7iaqHdOdN8sbU9B7S_W08EsE_Be_izBH0kbFfedNq_ITviejHALAiag9hfDpJ63kdKmo3-55pHtEM095h6gV0IycOE5AViHZDSBZmfKza9A6dsz8HN-N0QfTK3r7HbV6kuNkLWFohr-l27mrQx_0jzZ_j1SLrd2qq8z66oTnivxhSUDydIG3uqEltSa6f369dOh_TacHLfMRXHXJirPFXopPpQTI7BIzaISIRphg4pWRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ازکهکشان‌اومد زمین بی‌بال پرواز؛ مثل شهاب از اسمون اومد با یه راز؛ خرید اونو قصه‌مون شد آغاز، امیر10؛ ابر قهرمان جدید ایران و جهان
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23416" target="_blank">📅 09:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=UABNztAr840AMPZ1zAS1c9RAZY7w-1mGP9VNEhbpI9sGlU9YkfUzHThT2JnU5p1vRezAKqaffjncXlFMs8J4DrTVZQ0xI0LTHxNMFjbb5NVnASYCqpf5iCT6WbTkl-DiB7zH42-fCDft6NI4rOm0TiTpuktymXGBLyPRlkYVPyowfYAzVxQ8EsZxyFMDT8RpfnmgpFZTQeRuhwAWuFtCiEX0YKgywdTCtsIRoFhxReSzpR6HCZBmv40iczX0Bbw1bZCcbmVAS3D3iC27CBgwC7aBzbgtvgomEkYiYzosfOJyUF04ZyNUtiqxAwSm2Uw9AeC4J-eEHL7P7GTEhGUGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=UABNztAr840AMPZ1zAS1c9RAZY7w-1mGP9VNEhbpI9sGlU9YkfUzHThT2JnU5p1vRezAKqaffjncXlFMs8J4DrTVZQ0xI0LTHxNMFjbb5NVnASYCqpf5iCT6WbTkl-DiB7zH42-fCDft6NI4rOm0TiTpuktymXGBLyPRlkYVPyowfYAzVxQ8EsZxyFMDT8RpfnmgpFZTQeRuhwAWuFtCiEX0YKgywdTCtsIRoFhxReSzpR6HCZBmv40iczX0Bbw1bZCcbmVAS3D3iC27CBgwC7aBzbgtvgomEkYiYzosfOJyUF04ZyNUtiqxAwSm2Uw9AeC4J-eEHL7P7GTEhGUGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نگاه عجیب ویکتوریا همسر دیوید بکهام به تام کروز و حرکت عجیب‌ ترشون؛ درسته ما فرهنگمون خیلی متفاوته ولی‌همچین‌چیزایی دیگه مورد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23415" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uc6BxF-1-czbp6UoiJdUX-14WH6p0osTNU7iEpkzGD9guf4s1ZhVbDESQkhB4zzAqKE24o_kWizaztAA1n_St_b7BNg0S-cxtBt9Wt4pt9wRphzERyNh6ucdUQSD3CZO33goDqyvKK4Tnu-7uewnd9ZKi-3edngwk_6eDN5c1xqrs0VeZbHfNbm7S44kpy1RBl7PS4RxYeoFxuurKtG4rKW3UPvBwyPbDo4HbkZXgx51ItcYovY96yNABNCkWsdENzpHpnNe7BWGCKFF-ydQM4KRTYUJdJgeD3xfjcTidkSXDq9rlwqe4xrPIwKtv4qXlidKiF9RIincL6REj4TF9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
درحاشیه‌تمرینات‌دیروز؛ بازیکن‌کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه‌نفر از کادرفنی این‌تیم اومد گوشیشو ازش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23414" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da531b194d.mp4?token=suRTuNdn5-jJgFwipkgE76IK9mnDBStbq2k8cCUbwRNeRJ-2f0y4Huo_R21RyvNedRddHx2LyMR-n7M7IlZONJeGPv5vmyu7KecyA380YrtHcDZt5bQS2_1x5Y9i8_xnEBWTBa-FhpQFA-a_dFLpEbqBLHTVjb3W29J_yxTSktd4v6a39chE56TJKMmE_iERoLnfqboUUUC_-eO761ZCiIH__l0J2RVhPlMbKIE-4FpxIyLmX6tB1Dm6BN0FVDqPSCJEE_iOFidyqS6hGzgbhqjz_krqz6SgzMoLN8zeIHZ2C8Asui95S-wscJEsWfc2VndxIQ91FAhX-uo4EhGVrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da531b194d.mp4?token=suRTuNdn5-jJgFwipkgE76IK9mnDBStbq2k8cCUbwRNeRJ-2f0y4Huo_R21RyvNedRddHx2LyMR-n7M7IlZONJeGPv5vmyu7KecyA380YrtHcDZt5bQS2_1x5Y9i8_xnEBWTBa-FhpQFA-a_dFLpEbqBLHTVjb3W29J_yxTSktd4v6a39chE56TJKMmE_iERoLnfqboUUUC_-eO761ZCiIH__l0J2RVhPlMbKIE-4FpxIyLmX6tB1Dm6BN0FVDqPSCJEE_iOFidyqS6hGzgbhqjz_krqz6SgzMoLN8zeIHZ2C8Asui95S-wscJEsWfc2VndxIQ91FAhX-uo4EhGVrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23413" target="_blank">📅 04:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-CTviUeP6-XPZRwea-rYCtklshad5cSevZQHWgMOUwwXTXG2AnQF1xVyNQTBzXcxphieQVHyYGgavLuV9SxV_UcM0O-sq6_EHJ8_0qR4ehfMk0qNAeF60Vrq-rb5l850oE_DLWfsYUAtqWAx6fy8H76m3nRSPihWuyp_gunTnvdkTgz1QpjoEJi3rFdUetqGqGkJkTaf2KvScVbeZCicrhizFj_KF8p-Z7ONyixmeZyz9aG5YYO0tokFEX9Sl9rZb36EhpQaenDe2GNHnmrRCQ3h8Oc7hzXK2FQghVaO_wTe4JO6xupnEihauoy5amglOpB3xBBnkktomVcTpWFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23412" target="_blank">📅 03:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی برزیل - مراکش در هفته اول رقابت‌های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23411" target="_blank">📅 03:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23410" target="_blank">📅 03:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTYsrwzY16ytxATrKTz1nAhK4jHbnA1yP-_BCl8W3jbQtbTDsKnOnGa7qCpNeFaloMVFJv0AEdHyUJnwbmTk3MSutK1GmsxjWmVy1uAqcJjIspBY-GFTwc9X_lK5DY8wWbHP5gS_pseSXZt8dg3leBaTq2MkIe8Cf1pkKp9et8ke-bMZ9Ts1ncWU5UMaKiJbg-6_Dwiqm6cigsHutv033-2pH9wNreLV8myn0r2GwGL3X9LRhB01q7CfFbsy6HJvhTuRx7eDLs9iOqhzc-4peabh4KeewkGxAAoOqmvcSPkqplQfjz0akTLymqBwHdHJlIBfeykmCERh35h8MmpB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23409" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=hxSFu-jheN8v_4Zu7B3orU0Li4xqSb_rLbFPGq7MsFlrwBTthzzjRfyi5Yw6h3obe095hXhFi80tM20NQTddcMBu9j1Y4GdMTeWsX1xwF3dLk5kFV029bwzZMxklnFJUQykn4rHcNkxLqdAtyRK_YDJ4KJNMF_A7h1rSJ9GzzbxNiX9dz7xyuwu0iDQy7IrktjxfQ0SxI__PPJs0Gb2JC7wsc1mav1T286E1vt3HvHIVxEtk7_91el6qMp_IdEsXoWGPcopf79CNeVAZZ1ANkTILJIx2skJe_yGToD1_rGFtGTpLZrvGZqKMknUQn7ovNopwGstGX7gMtkTAyKw-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=hxSFu-jheN8v_4Zu7B3orU0Li4xqSb_rLbFPGq7MsFlrwBTthzzjRfyi5Yw6h3obe095hXhFi80tM20NQTddcMBu9j1Y4GdMTeWsX1xwF3dLk5kFV029bwzZMxklnFJUQykn4rHcNkxLqdAtyRK_YDJ4KJNMF_A7h1rSJ9GzzbxNiX9dz7xyuwu0iDQy7IrktjxfQ0SxI__PPJs0Gb2JC7wsc1mav1T286E1vt3HvHIVxEtk7_91el6qMp_IdEsXoWGPcopf79CNeVAZZ1ANkTILJIx2skJe_yGToD1_rGFtGTpLZrvGZqKMknUQn7ovNopwGstGX7gMtkTAyKw-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSCjwqcp7ilGAI_0VGBL7cdztKNc7IsWZ59t7nkSn6I5zMVfoFCzv879my0AIT0baVETrIoqLvuHZ6RVMMSV9KKenL1KSqI3yPO_ZaAFsZ34ryIAYlmBIzaL8dKiQjBFM0ZvYZCdFuw0QKDGjS6BtUNUnBYX9Z1PCW1H4hV3YxqKzvQ9OZCwiIvHlTlfE_5xz4Qs59xLEProgIG5vASQeLpKlhl2QIhVeUQHWXfcxR8YNDKvKVqXKpsw8hmjcQf2oAWHJzHKqItHPqZebU47hHmYpCRLw7r5vlX4ihspRMV6M5NJg7SIpZfb84LzBxtQw1aF9kkg9CzcCfwtlfX4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbCVv5KDxA6qmYbDx1zoyxOpXFQDVzM3j5rY6nKcagMN5rOrtLjD1apFt-ekYt6cxrTOvojtkUfZydH4pVTIIHLwKLrMz92ey0xyAGjJ2UGgtRnLY6347vHdBZXKQmrIjv0nChZaA2lf-KmkEi7-XoIullmIoRXPvd1mT4miFdkG74CzeC6yOq6GhD1Ug-aiAdlXAvzrwIveV7Xj_84i8oqg9dQscqrdxlR-9X4deRGhO5D0-t14gG6UU2qbNpIH71bQGUOxJCn-aqGz17Q3CsbaS9jIPLvW_DDRFOp8Za_GIqftibmAg2FnlbWaMMb0M24YXGUMSli7KnFbBWi3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7kAzgwKzinQn6ZW0_jf6tyTwuSG9oDd-ZqAQlgY9uPY_fEZ5mCG57U7JiSDt5kRLIR7SiV0ZggWwZBASlah6EEs_vkTk0OKs1HgOnP-JFCFGrJWx0jjgy-vdS17zTe21JIaP8Yt_Ya2wvstE_XPVhh24JIwXCIlPCfZe7sg8GdsNRQhMxFz2ls_8lChdOFC1W94ZrGFpA4ryjwKDFP_XkgE7sFnecgwZdAoWHT4XcO736EqczffCDbvif-bCkapeSbjR5E-1phlxh69Fhd9bwOjP70pJuJmLYYql9s2LSALe86s2fGGdUrV0zJ7-3iTZmPvk2TQtQlaHLEKNMVbXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=UQ_MfbNNS6XV8-X8pEtUyZIILJF9_yj8x5YshH9Q_2LWO7gD_OsFZ4zMuYtbYWQkJQRyBehv9qeph-NDY-iaYePcVZD-DYr6I1pVn9YeJr4LjbCNqlwRS8gK3krccgJlqXQuuClbhcnFgJqy4hyAU5vwjG1sw-MxlPURr-yOBwVoPLpKOKL-SeY0-YHfKtzhiCU24QXltzA0Qptp-cPJUIVKFj0W1ToPfmcnWk3YIRl0G3GHM8MhZ7b6d6iH5_so9WNOZRvmAn2d6Ttc4-dxoGtz0chGTFFMZH7UI-G52I3hHVnNamxcN1hanepUfjNQQjyVjJdZuaQtheyrZHnZQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=UQ_MfbNNS6XV8-X8pEtUyZIILJF9_yj8x5YshH9Q_2LWO7gD_OsFZ4zMuYtbYWQkJQRyBehv9qeph-NDY-iaYePcVZD-DYr6I1pVn9YeJr4LjbCNqlwRS8gK3krccgJlqXQuuClbhcnFgJqy4hyAU5vwjG1sw-MxlPURr-yOBwVoPLpKOKL-SeY0-YHfKtzhiCU24QXltzA0Qptp-cPJUIVKFj0W1ToPfmcnWk3YIRl0G3GHM8MhZ7b6d6iH5_so9WNOZRvmAn2d6Ttc4-dxoGtz0chGTFFMZH7UI-G52I3hHVnNamxcN1hanepUfjNQQjyVjJdZuaQtheyrZHnZQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MriEuC8WufkxHwoZsE1r_vRFvxayP8vFAR0p-6v-eAaZ5afEihUGchOZYtHAZrugoasl9tAeF5zb4e0hFvLpLhCFWVt9bEpz3bASx8zTlchi_u1vvyyYHVhtqt1L2DphjTcTmjl_yCi8nmAzW3H1vrmQ2hs-R3aCrWaGc51EKq_sLN-1tyD7Vla2fdzE-V0G-XcyxGpvjsTtq-S3xGJ6A0bB-ywYdxPR7Q0-1jhwnMynMK_SniPMWre_-k3JykPcGQVEP_uK0WbUWHDvXr2K8VIVQe7G6We6sdqkwzSB5mLv-g619Ma1jFnWR-AKrMZEG441B1ouVgIHCKf36-cWVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=LuVz0MhCJULA_2JiQSQPC35jGyISmOqXr4SAq3VzEs0pAnN97nLyv8CIoMO_vkjG5chNDGTvTq1gk-3HrdxEhn-gUjEOOwNvtrK-XC22AR2aaoKQZfGUBtxHlxrvJdhHXcqIOCC8dTKyZfMZ40M5u7XAg5vsHSslgmLLNYqGUktqVc_NmNhsvkeC5nd7h8-7L_IvGA-XUQ2lJMY5BSH7jnAq7tMk3uGBRyji6a_RnfNBVXgULMT_c_CR4WIsDOjCrXSemwHKdrgpULFwovHjkDVSQer62FtJELSFCr0LV18JC-yD_rVYaTFYe1rKwnPM3ijvC23ZQTWFtWojObyEsINlXLVbRBNQNNExehDgySuoFgm3ll_X-NU7RofQvsk0y-U5T_mp7Ah17hxCFQGjVS-GN-NkVHukVOwLbvNEx9YOuTLA8AAGajT3fI4is6ZQ_1p7OkeheFdz92Qa2MCOI6qlsNDz5Hd2vOuD87VH9Qvb1MrT33K8QuCaRusyZsT9sRlxKKgV8c7K1zW-Bbk92ac6taBk0Hl-fmB-lc0gruhA6lL1R2j25idd8-q0td4Q58wRpEhJjb4SIl6LHIG9E5r0DHIMS4mea_gmTgDVdSVVcQs8IuplNGTDmoEEhKoI95ITErRDUFC3hc9WxTspZHtwlPSLSjXJUe0Nb2EkFQc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=LuVz0MhCJULA_2JiQSQPC35jGyISmOqXr4SAq3VzEs0pAnN97nLyv8CIoMO_vkjG5chNDGTvTq1gk-3HrdxEhn-gUjEOOwNvtrK-XC22AR2aaoKQZfGUBtxHlxrvJdhHXcqIOCC8dTKyZfMZ40M5u7XAg5vsHSslgmLLNYqGUktqVc_NmNhsvkeC5nd7h8-7L_IvGA-XUQ2lJMY5BSH7jnAq7tMk3uGBRyji6a_RnfNBVXgULMT_c_CR4WIsDOjCrXSemwHKdrgpULFwovHjkDVSQer62FtJELSFCr0LV18JC-yD_rVYaTFYe1rKwnPM3ijvC23ZQTWFtWojObyEsINlXLVbRBNQNNExehDgySuoFgm3ll_X-NU7RofQvsk0y-U5T_mp7Ah17hxCFQGjVS-GN-NkVHukVOwLbvNEx9YOuTLA8AAGajT3fI4is6ZQ_1p7OkeheFdz92Qa2MCOI6qlsNDz5Hd2vOuD87VH9Qvb1MrT33K8QuCaRusyZsT9sRlxKKgV8c7K1zW-Bbk92ac6taBk0Hl-fmB-lc0gruhA6lL1R2j25idd8-q0td4Q58wRpEhJjb4SIl6LHIG9E5r0DHIMS4mea_gmTgDVdSVVcQs8IuplNGTDmoEEhKoI95ITErRDUFC3hc9WxTspZHtwlPSLSjXJUe0Nb2EkFQc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=rVSFjnwab2T8srHEQVERK8cf6bJ-0JWV_MqufLrpxx3oO8z96UA3w7fmeC6uBCRa87LEPhvB1BqgWRFifdxNwH53L9pA0aAgU19LBEXBIyuKuXj5-rLvYzpz8bSxF5vvWmzJ1wMQLqlDg_5ZMmwq5TY8rfadqBiJ7RgpsvFjBc5peNoxHa73DuhwerNWCz9sj9lxF_pPolzlJlOzxuvTziPyRiSc_UP80QUbXp9InWpgdjJT2OlNzqB3zxLZ2P-wmq6cuFDV34oj9oNSF9hyuM2r0-NtbdWTOzYK0yuM3tcx8MBnJ4rwKtRviB23ZRuok9wOTvHFzlIPRUCxCz_hWkIdvN-A4N6H-_4oWN22I34i66EUJZXOSUOpMuqdwMzjicCMciT6B06Y930h0nocVxKnecOuwJdIPtIh3yR0pq33w-OFZ-V4rYiSFR8acLMIhjzy4hmeCvDP_S3ZyFFTqj_lR3vd9QLczec-9XH3ccgXEbFuHuT6OLxoXT-6Z0oYbidX-0DT4UL-zKHTaUHdRvD0LXJXwXWDgnspzBl61QKOmlqsFvasUR92wyF46fDuC2FF3IOZEepJdDwMc_DctYxERB6Xz1XS4ROrG03Q-h8SEWvWM2xeuFaY19wPCdpcM_cVFP26iBGm6aWbwX7rEuBwgBENoltMqLKBGm0KN8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=rVSFjnwab2T8srHEQVERK8cf6bJ-0JWV_MqufLrpxx3oO8z96UA3w7fmeC6uBCRa87LEPhvB1BqgWRFifdxNwH53L9pA0aAgU19LBEXBIyuKuXj5-rLvYzpz8bSxF5vvWmzJ1wMQLqlDg_5ZMmwq5TY8rfadqBiJ7RgpsvFjBc5peNoxHa73DuhwerNWCz9sj9lxF_pPolzlJlOzxuvTziPyRiSc_UP80QUbXp9InWpgdjJT2OlNzqB3zxLZ2P-wmq6cuFDV34oj9oNSF9hyuM2r0-NtbdWTOzYK0yuM3tcx8MBnJ4rwKtRviB23ZRuok9wOTvHFzlIPRUCxCz_hWkIdvN-A4N6H-_4oWN22I34i66EUJZXOSUOpMuqdwMzjicCMciT6B06Y930h0nocVxKnecOuwJdIPtIh3yR0pq33w-OFZ-V4rYiSFR8acLMIhjzy4hmeCvDP_S3ZyFFTqj_lR3vd9QLczec-9XH3ccgXEbFuHuT6OLxoXT-6Z0oYbidX-0DT4UL-zKHTaUHdRvD0LXJXwXWDgnspzBl61QKOmlqsFvasUR92wyF46fDuC2FF3IOZEepJdDwMc_DctYxERB6Xz1XS4ROrG03Q-h8SEWvWM2xeuFaY19wPCdpcM_cVFP26iBGm6aWbwX7rEuBwgBENoltMqLKBGm0KN8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEWaQ1uR2M6dKsceRkD342jqtOdWo7nPOXCyRBXF-oBbeY4jZmCB0VUL4qfqF7SF7D_YpPb6OegNOYD6qCMAkzBkISpbCT7OWshMMECyJtdWiysfdmyOy0wAVPhSOaF0psQCm_xr16f13sM_kGS6EY8659wOORz-krfbIG1-jNCiV9GvfpyquK51e2MtkQm8gcsLDO53E-1nbmFG2qC7OkUGM9PiOcafBsEwhbY0YGfBoe2VA0WaZ9VqNs2lVDL6SElT_qEEK072c1LBe_z7X9gC9jKAD8W9wqqEJHlSmTZ8LvB4n1U_Q2tNSQ6enZJCNhQ8jFhP639E_dTGnPls7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki5Dfu2VJ_B_gUjrV2qXvhqZcf1f-7xWzQNf0-zxiuc1vfjxsU3BX9QrdAep_4Ie42Kc3I4nOBl065F4PB1qmsVe8sZoUc2kprdbrqOSsc17Wa0JesuSGjkCJxnQjBqwwXZ7XT3TZJBnqBWhyTew5XHxyPHA8Bo-Z3oM5nbRbmEwEdWADORSzoi5nQdotmHjBwdt_0c9uoMLtolx4QcUnqjGuKk2h7AXcMF-6yGaSR2biDleASXd2LO7Fje2vxw-H5V3dkFaqDK_In3ItHFIwNkHMTdNzoyFjR-fzDnBh0eLvSScHxF0ZX_30t_WpHf-aKiDduo0_elyV7qHbwiGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c1ZLvb3KDb2BRiFobDrUlNTihy6ivegKQAvkY_XuqGcKsoKHi2Q-LnMgBr88ftQ52l1XqaX8lKrpARI3mkklzsBPo_IBoryB6u1gFmrRnmFX5pff9hNYBcLrr8Zf2gBuWN31_CeKm--939oZHIA9H1tIGco6j19xuLkGFj-drD3DU9OinHuNaSPMUig5Nlp1-M-VK6iE_5rByY7XfGNBqZAG0Uc5e9FCrKVvEppefJNV3vjk8X9Vy7BvT0b4D47N_qIKfkc_zWgpyzMjLDxm2lRLc-TXLLpVF2B6xVgwDqhbO35OCDHTZg2MTnSzcge0X8swM6B_aLQ09-5I9-Jb8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0YIkmvczN6OCwng17NSBMtiGBPNDIzAvIZ1GD94gDP7l8JxtmJTattuAIOBUiq6_b5Np2T5H3klabCZaV6ddNQSpcztt2YsOXK__LteJnS33cH8WgVy3aXFCqzMzP3I70X5mwsdJgTJ8O4rjsF2xaw_Q8Vv1jKY1J6uhslT9KVwcjylOv2GnmUjLZkCCdbyfQ31HdMmu_ms5Nf_6b087XD7i2b5-My2eMg3QGsD8tyE34ZPbPFmomyIGshwZ6i1UkHMDKJNf33mgnH5DyOggU59BikEmnThMQ8m7eQ3WDYOvMISjxKYw86k1gUcKxNFGXD8zgZ3TOhHu6gpw1QzIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=VpSUi1mY7_IhplV_XjvHNhbD8WA13JAW8fWlMGDQaNTAxIx-fq8_2XJFWHc3uYy6_9T-mrRfV5iLyWPUB85psEBn7Gmj4NtihVpcrj6hsyuJNvb2u73mNUPQRekRxt0ph2wOfXMpYqzgtzhHwWX4re0oUPCiYKqoLAoxolCSqQTa2PYRl6dD7E1933ZAqCiLK9Pao_gA6pTXBxKp1hgU_R-VeH1Rtzu5qvF2kkAnzTcsteeGCxAC5dDpyFL5RLlwy02miuZTlq114mbgD0lzJPLHRCvi6nKYLYM8DvPWSuQbOWw_XJmSsdjdBLmdXfnQwhfJkYl5n4YRnCGUm-wQFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=VpSUi1mY7_IhplV_XjvHNhbD8WA13JAW8fWlMGDQaNTAxIx-fq8_2XJFWHc3uYy6_9T-mrRfV5iLyWPUB85psEBn7Gmj4NtihVpcrj6hsyuJNvb2u73mNUPQRekRxt0ph2wOfXMpYqzgtzhHwWX4re0oUPCiYKqoLAoxolCSqQTa2PYRl6dD7E1933ZAqCiLK9Pao_gA6pTXBxKp1hgU_R-VeH1Rtzu5qvF2kkAnzTcsteeGCxAC5dDpyFL5RLlwy02miuZTlq114mbgD0lzJPLHRCvi6nKYLYM8DvPWSuQbOWw_XJmSsdjdBLmdXfnQwhfJkYl5n4YRnCGUm-wQFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ7t2W0YtsAS7KzOuUK4PwOePxzDpWWpf5cCMc2k40HwBHpon1_fBzhFlnkxyNZXDFqEaRqwXlJtXD29Xyw-3VTsWzR14x9SRSWKn4vxjWF8M_3BaYbn9gRJ83OaaTDXSTlG043TXttI3OSN2Of-mOuoUzV4l7zqcCvIdFmlXvMmLB7q6OGWoTHTqPDeN5zEqdbSetMP-QZATxO9M_vbvnSHrM29jPdK9ubU60Jo1MlCxD6LG2M8s1-xjyjl2zxbhAiNElwxbnJfEULYPc86d07nO3G0I3TluRo3QzNkY02Zpkx59HsHQt4m_3kvN7u7FXd-jD8cI3HTymQVJvfsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h56S5aRpN3bhsl69Cdc9HsJAy44Q3It5hKQi_CywjlcDD9NYDkzZINdO_NgzaikADfcOd4MBhiqE8xdsc8yzY9v4iibCu3U2EccKB9BfinKqnNGyW_xJy72zsRYCWPIVZKxER-S8bMCE5S81j6RAWB9AFzA3_J7F09lEUmXnhONpHP7YTud4brZ3v-M2Vco4G_nnu9-9uXeGeJ7fsrq4rAMGVQbnaUH-Rm6Syg_mjdfktN4YYKqNz-VhdM3ngDjL3SBwn18cL-nKi5dv4b3HQ2pJB23XQFF78Z2oQNPUoJwuw6CENpT_edf24wfxKz37Y4nKhrO5LFNz_KmPkMFajg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJAwrhKy4oGgK1ippU56VN8lqH3_Iw5FtSxxur897inWpjFV7zUOsACzMV_0HfQoILZwN-9VlEsjRrFoI9CsYTDN4MM_Pl3ue2jWE6K5WeLKXocSbptWXh-LPDt_Q9tYLNKPXGrWtmNIzlqAmjGAQpZQxk9NA_kLZaFSsvJ8gSWRCFeaRkrKrx6IflsKRZR6mcKpapE82nPa9G5dlPwzH0qoo9U8OTqgM5zdRmC-OiGVQlea44WUDy7roDmuuYYJi9CWvj5r3eC9z5C1i5YI4oLyna2TaT6mM05UdhzMecq2rZTVJR8lqEBh7-y6PVj3ltrwIjGsaKArKxScPQ7wpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=us8CvwiKBNJMR6-I_BoTuBOZJP-yiQ9EtPWfU510aQLwdC7WzLOGoFnz-DUIRfajX61ZM2qAybcuqFYv-rohXOxApeWXbw0UHyGJGaZbx55sEJFbq3Mk8sTGpoV9d1ppmACojgIdlUBjr1Kk3phLeVQHyHkhR5QoHyqqi7fKQGwUVVilPlNkNCxYGulkjxJ8_3sKKOUAdNnMyW4pePAjCAKk-lD8_sRJu3gI-VAcXdzf05wkFByA0ZGrOLpGTEpirXfimu0j480WaPOcJUZHIYw8ul8RtpYG1SVZE2Fh1MOV1Jbx9QAegaJkcEaq9nRtWZmY3c3t4JLrgWkkvb0SzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=us8CvwiKBNJMR6-I_BoTuBOZJP-yiQ9EtPWfU510aQLwdC7WzLOGoFnz-DUIRfajX61ZM2qAybcuqFYv-rohXOxApeWXbw0UHyGJGaZbx55sEJFbq3Mk8sTGpoV9d1ppmACojgIdlUBjr1Kk3phLeVQHyHkhR5QoHyqqi7fKQGwUVVilPlNkNCxYGulkjxJ8_3sKKOUAdNnMyW4pePAjCAKk-lD8_sRJu3gI-VAcXdzf05wkFByA0ZGrOLpGTEpirXfimu0j480WaPOcJUZHIYw8ul8RtpYG1SVZE2Fh1MOV1Jbx9QAegaJkcEaq9nRtWZmY3c3t4JLrgWkkvb0SzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htdX6LuQzXUeRRpFe9Jx3kdGGAXAVOadIY0F08OXezsQF3ad_BbuzPSj22Dtd6VpaLIkXHfDCY4jFaKo4S7kB9M8g2Fom4A3acQIsw6KepuMEmQyyiG_s2WX3oo-H3j-nzv3J5e_PpfZSG0dmpfIipgoHhnLYG8GhMI56i5-_iu1gm8hnWa4LMN0i39-CdX25x2Yjd6hJol4aHNzn8VXqyrdw06_tOPz7YjFLZXNhpBmkblO48qdAY8zcH-t8gIXCE6dvveloGOR5RBnlmhm7hW6o6Mxu6r-iRaUandBvR3sJxPcqSlQNJgX-UQFe2Gs4E-Z8Ca5v9CEeiE_c-8x3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=m9UXW01nW27c-KAhjGOsOcYOXu6VFqnqdOkljMf8gDhNCSw_jzmBul6M__na6YwG9gGswJCpSwVZvVShTjsde7k2oCDxGDJp2itNzXty37gKKwE9mFaLsuKUS8KFH4X7sn_4MS_VCwCkP3QR_rU0w_h-Ekf5fpTCyRJ-_Z__xpk-n4iN-xj3hpZOHjtEiU-dc_JLpLGbIf4oHZfNPaqUPhT0mJL_CfipIIap5P9f6lPaH_dFgHI998SgIW5swF4GcoZi9vz_ooRU_vFQPpWf6JKmT6WmFc4rkgMPHxagKbHcxucpYUYa0FGg3EhVuQl7TsfVG7RD4olFSMlcwsvCe4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=m9UXW01nW27c-KAhjGOsOcYOXu6VFqnqdOkljMf8gDhNCSw_jzmBul6M__na6YwG9gGswJCpSwVZvVShTjsde7k2oCDxGDJp2itNzXty37gKKwE9mFaLsuKUS8KFH4X7sn_4MS_VCwCkP3QR_rU0w_h-Ekf5fpTCyRJ-_Z__xpk-n4iN-xj3hpZOHjtEiU-dc_JLpLGbIf4oHZfNPaqUPhT0mJL_CfipIIap5P9f6lPaH_dFgHI998SgIW5swF4GcoZi9vz_ooRU_vFQPpWf6JKmT6WmFc4rkgMPHxagKbHcxucpYUYa0FGg3EhVuQl7TsfVG7RD4olFSMlcwsvCe4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW2DTXxZEnJ9Yn1JTXX-wzCTmTnJB9NiUN8m62UoFsWDEzN1ntj08jhANdVukA6ClfpDyGWPd5sYWtrlxiWdSOTTSXrBqB9nBCihUcZqc6Sks1NknqeV6UtEKLp46rKpBf8GvNIhfvC7sARhdROSyaIs0LlFaJD-peQJeGUpljyDJLIn6MhxC492iBgdtblzOO8NkR7d2eZ5zQ6BT9Nfua6orvUexTVSND1PDjxhaK53Q2t08U3tVRG91CN0s1b1FNg1D6ydRcePsppM2ZmI0L_tRoa_fPopxs2Cfom2NVqSBwzlzBS0mmVyk73jNEW5XeXGlrtO2nu7FDO2Oy6FzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4DMtSlX0ZVhWhpTV13RHPQyxEE9ZdRavooGzIC858ESb4TVxCowMWusFDG7jmO7TXCLTtDrzWkGpK1fJyDvW45TANigyp1rQg717WJXaHO7HGght9x3UZQ4xNONI1r2YdLZyWHPrG0LF1vEjfMTRmFduw-Xk4w7zzmev97nkG3L-0rBWSlDwtD82AECbUGTVExczf53r6d45T_fNv6pt3EOEe8pCZJO5-vaPHcXTTA8JFhlmDTXa8mGSBhrHb4z-Dx5dfgw-HfyJJnc9jTuSyuFPculzhKuUGTYaIKxrC0_z9gepmRSGpoHy0lh8tcggxRVHpzPm_OVbbts4nqF8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=vIYM10E-J07l6-PaXk5Uszs9WcuZx2aZP57Pgow6X7r9Q35Q0Zzr0usgUn9nGXN2nMHouFVn0RdlRR9V-hEB8syprfKBtj_T2ZbkanweUDpDI_Yaa9lgrhVhcnMLdD3GYelovPyDoeYFmAkyuhvD7rXW0Wk32tosrwQRv-_c1Yxkn2SSZK6gjfksN7co3P3s48sOVqa4ceOSG2Gbkj_Imoq0sglrOypqoooFG4NQ17dgUJWvH5k2Ar1-st3dc_9_PCoIcxSKqTpDEV3HbrD5yIsG-3nHQyRuNOLz_We1QSTqztM4Utc8rTMnJo0hrG9CUiYqu8YM02qD_8p_icjPK5Bwfw5jI4uYbNM-agI0KgDBnJKEMdtyrTMC7nLgWhgoobOhKYDumlVwLnSsnROcUIzuu8HYU31W_NcMWBxDQz8RQuptBowgqIeLKPVhbXOf0mc2E4MYTWyEQKeokA6BDx7KEhxMQ3GJlp6KWJ7eHz-jICpYmRP2enlt9n3AbYVENKX5bGRWmfggqqonKKSKVzWNBcN9e3FzuDTD_qooK1IkcR5HDG75dvrSGq5Iv07jooXKfPDPkhbuv9wi9Vkz_KMKm3zLmO0fOlGKnP7rGs1wcJfhVI89r5VZIaeSnG9Jz8g8XCXMkS_i3fdNLdYTKeS9OrNj_-zimfxLnQ8h3kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=vIYM10E-J07l6-PaXk5Uszs9WcuZx2aZP57Pgow6X7r9Q35Q0Zzr0usgUn9nGXN2nMHouFVn0RdlRR9V-hEB8syprfKBtj_T2ZbkanweUDpDI_Yaa9lgrhVhcnMLdD3GYelovPyDoeYFmAkyuhvD7rXW0Wk32tosrwQRv-_c1Yxkn2SSZK6gjfksN7co3P3s48sOVqa4ceOSG2Gbkj_Imoq0sglrOypqoooFG4NQ17dgUJWvH5k2Ar1-st3dc_9_PCoIcxSKqTpDEV3HbrD5yIsG-3nHQyRuNOLz_We1QSTqztM4Utc8rTMnJo0hrG9CUiYqu8YM02qD_8p_icjPK5Bwfw5jI4uYbNM-agI0KgDBnJKEMdtyrTMC7nLgWhgoobOhKYDumlVwLnSsnROcUIzuu8HYU31W_NcMWBxDQz8RQuptBowgqIeLKPVhbXOf0mc2E4MYTWyEQKeokA6BDx7KEhxMQ3GJlp6KWJ7eHz-jICpYmRP2enlt9n3AbYVENKX5bGRWmfggqqonKKSKVzWNBcN9e3FzuDTD_qooK1IkcR5HDG75dvrSGq5Iv07jooXKfPDPkhbuv9wi9Vkz_KMKm3zLmO0fOlGKnP7rGs1wcJfhVI89r5VZIaeSnG9Jz8g8XCXMkS_i3fdNLdYTKeS9OrNj_-zimfxLnQ8h3kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anrINFYsyYa8fjePUAMQtaI9-FEEkMKT7Ec3Q5AxTqz-RIJ8CQnx6XCMKoetoAfH20OmJ3jX2QZXF9o_9fNpyf8tzK1T5VGXAEuiQd36ns8KTH-Cz0Ugmu9qAe60u_0PBdfaO6Edx9VEFseYleraKoOhmWI-u1u-8J79D3Bg1p-CPccdCYzeTmWTJ0LL4VkDz_7T4g5Fk--PnA2gPwpA04lio-AYPp0b8KPmdXQZpXfMgVGThwb36DgbKcmYxusLUsjHPYVQP1nf9QxarGghwOvjJWTuMSllq5Jcc6F2fYFijm9N4Xz0pqh5EhBPOMcw2pHAx7BCSO-anwLf2ywdnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWLkBo3jR7QtSMEcDGI42KeZXl3xjI1U3WfHv74tesL2KojlABenF66iuc8sfmUOSCExUQihcCUK_rMfhBZDAAWvx5Um-E_7yNY2m6uqaxUF2VixKRxQeTberYBIHM-DqnW7Dtp39GgJ0rypGyCPk0tZRwyudI5d8GQ8zKBE976Q5sp00vAH9Hj_xyAKxnzoEw4DkZYSJMw8s_a5WQDfX6hP8Uf4sR5imAzzJNfyKUc2TvyM3p0fqZhHr0-MPT91HVd3O4RWot5WATiNfBKl3Tc9C3TmODGOeSPZL-hzLB3HBH-WisUG-F1kfAn4RHRq2ppIwctnA_MajePe3v3f9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=CGDuwngrVJwzZMC5jitUGF7Fr7Dkx_4pePuiKS8761ZxjlkKBn_RdYD3V0qPTBQiVHOfcwf3aUjWWUy7k5bwPNRx83Z9LSokCGj8ZFYqEW4ihST0GiTkFlxLxpyTRhqZ3Z9QIkuF-a5Y9LgZWbiJsNqDJNgaUc2ZzW2BtA96h65TqUIZso7cnVKX4RLrV7rOZbnWEijBFkulth629d43IYJR7bIDoJBiy0QiktWdUrRUvPTUQHT6TwVNDd6hEJTvNu0M1oL2WbfDPpDnlgV7TbwbLDLlZPXbOSrrZ4d8rDDumNOods16i0wI73bTk1NxbvXU_lz0Nk0cUT6B0HXpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=CGDuwngrVJwzZMC5jitUGF7Fr7Dkx_4pePuiKS8761ZxjlkKBn_RdYD3V0qPTBQiVHOfcwf3aUjWWUy7k5bwPNRx83Z9LSokCGj8ZFYqEW4ihST0GiTkFlxLxpyTRhqZ3Z9QIkuF-a5Y9LgZWbiJsNqDJNgaUc2ZzW2BtA96h65TqUIZso7cnVKX4RLrV7rOZbnWEijBFkulth629d43IYJR7bIDoJBiy0QiktWdUrRUvPTUQHT6TwVNDd6hEJTvNu0M1oL2WbfDPpDnlgV7TbwbLDLlZPXbOSrrZ4d8rDDumNOods16i0wI73bTk1NxbvXU_lz0Nk0cUT6B0HXpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=GE4VNDaocXkKhddMroNxgVMjzoNn4d1bI3N6Bxr5BJ6Z8s_yia2kMGHxUQKMO0qpNBMko0AxwKoySOUIinKrdHO1kDgM9mUVNk36qdtWEymajvCzX45q6ilmcMBQVzUNX1bFRSmzMoVCnBGvUmdzQzzXvAQpeDNsZ1iaM1rauGH8XekAcKvqmoAu0DS3JuaFHo9sEZvOa5akKMvS-Lmr-9LX0OmsQ5tfbNJ6hdlwd6lCvyzVFPSCB1_D-CyFHP6KoOP_xhXJVho_hd_Mro0Q4rQ2HwXvZ74Rp7L6aIUycquOeZSWrtonsUFWUiVJE-2XqGB9vNE_T_ugOHNEFZax1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=GE4VNDaocXkKhddMroNxgVMjzoNn4d1bI3N6Bxr5BJ6Z8s_yia2kMGHxUQKMO0qpNBMko0AxwKoySOUIinKrdHO1kDgM9mUVNk36qdtWEymajvCzX45q6ilmcMBQVzUNX1bFRSmzMoVCnBGvUmdzQzzXvAQpeDNsZ1iaM1rauGH8XekAcKvqmoAu0DS3JuaFHo9sEZvOa5akKMvS-Lmr-9LX0OmsQ5tfbNJ6hdlwd6lCvyzVFPSCB1_D-CyFHP6KoOP_xhXJVho_hd_Mro0Q4rQ2HwXvZ74Rp7L6aIUycquOeZSWrtonsUFWUiVJE-2XqGB9vNE_T_ugOHNEFZax1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
هوادار تیم قطر آماده دیدار حساس امشب این تیم مقابل سوییس درهفته‌اول جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=VnTO4OYJQo5IbWylD8ypRdsJ5NyGZg8ZDfKldIZ_MGiAQYdRJeOtH_reiquSXf2mKltkOp-kkgbyGNKV_ViHQze_uFOqqtsJkEYZArjSKwGw-K-Pm__f6c4q6gDoBlPUklrAlf9Z3vP92rZj6iH6e0vWm8tst4DNoE8-uMWUlOEs6oQNZ8HZ9GORaJW2Ic4hsONhkBk4-1TvrQSFVLlzB5CT3nYI6aTBhp2tik3ZW_MU8o7YY1oiap74VZUiptppNL0hOL5Pfvvo5VvmkDSMpsOZ_b0s1yDgevJ9DLm9a5gZB9KTSkwGhFgXrgmh6XkZQrLRn611HkiazLd44A9srw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=VnTO4OYJQo5IbWylD8ypRdsJ5NyGZg8ZDfKldIZ_MGiAQYdRJeOtH_reiquSXf2mKltkOp-kkgbyGNKV_ViHQze_uFOqqtsJkEYZArjSKwGw-K-Pm__f6c4q6gDoBlPUklrAlf9Z3vP92rZj6iH6e0vWm8tst4DNoE8-uMWUlOEs6oQNZ8HZ9GORaJW2Ic4hsONhkBk4-1TvrQSFVLlzB5CT3nYI6aTBhp2tik3ZW_MU8o7YY1oiap74VZUiptppNL0hOL5Pfvvo5VvmkDSMpsOZ_b0s1yDgevJ9DLm9a5gZB9KTSkwGhFgXrgmh6XkZQrLRn611HkiazLd44A9srw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهمونای قسمت اول برنامه های جام جهانی
🔴
امیرحسین قیاسی: رامبد جوان
🔴
سایت ورزش سه: خیابانی و خداداد
🔴
عادل‌فردوسی‌پور: نکونام و کاوه رضایی و دیبالا
🔴
ابوطالب‌حسینی: علی‌پروین مادرقحبه برو دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=jRD1PROSb6ZH_v554YPWLpRvm3ttKJkJvoT1OfGGTMyD8XG1MQil8_OrX5O622aTcdQL88BzljWp1T_vqkm-E64Ozqsx6z4r3pz9sH18IB40b8hmYsQjWXT1qUKm8DUmPz0eLxg1tDOXmChhQYlCJHeZpRit6VwUHzVUg6i5pTKkPivqzaTZm1KLWnHIAG570XBvWQ2Z0mefrt6ZCrzcJEdQD2F0qRjanCVVcZW5a42DRYPq3MYeRUNb5I1DdzGMxd0-z7k0jw38NUECnBTvlK5e1KkMm1o0G65kxNnRK0OMY_wo1B_YALCuiNxq6UE-f5wX_n2RtxRXV3yAd3pKd3wcyCjcgGMQIZbEhJ3zEmFIQyO3rozuQ57Oo6EkYPGQe40TRBk9N3fqf8tC52Ap8rK4eFW0xi-jVZ-sleEd1NpcQJbjPYvOdzpH8FO-ohnTmaB_imCU_BA3SZJTXUMI6gWv0y6SkWxz2qbk7_Bv9VlT-Lufh5h2aBNBopy6VGaxtvsN3-9umdVb_HBUGyy6DNmSUtkX-CLDyI01XqBDTRSj42Tp4hbiuXTwSnzZrjsihewMkzoOMvaV83NsnQy-NEdh1GX5OoaT_YCAmCqV2RoQka3vAspc8P8wpsx9CObU20r-gz3szUToXTLum0eJa8OJVCzAv_ZFn7zCBfGLiRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=jRD1PROSb6ZH_v554YPWLpRvm3ttKJkJvoT1OfGGTMyD8XG1MQil8_OrX5O622aTcdQL88BzljWp1T_vqkm-E64Ozqsx6z4r3pz9sH18IB40b8hmYsQjWXT1qUKm8DUmPz0eLxg1tDOXmChhQYlCJHeZpRit6VwUHzVUg6i5pTKkPivqzaTZm1KLWnHIAG570XBvWQ2Z0mefrt6ZCrzcJEdQD2F0qRjanCVVcZW5a42DRYPq3MYeRUNb5I1DdzGMxd0-z7k0jw38NUECnBTvlK5e1KkMm1o0G65kxNnRK0OMY_wo1B_YALCuiNxq6UE-f5wX_n2RtxRXV3yAd3pKd3wcyCjcgGMQIZbEhJ3zEmFIQyO3rozuQ57Oo6EkYPGQe40TRBk9N3fqf8tC52Ap8rK4eFW0xi-jVZ-sleEd1NpcQJbjPYvOdzpH8FO-ohnTmaB_imCU_BA3SZJTXUMI6gWv0y6SkWxz2qbk7_Bv9VlT-Lufh5h2aBNBopy6VGaxtvsN3-9umdVb_HBUGyy6DNmSUtkX-CLDyI01XqBDTRSj42Tp4hbiuXTwSnzZrjsihewMkzoOMvaV83NsnQy-NEdh1GX5OoaT_YCAmCqV2RoQka3vAspc8P8wpsx9CObU20r-gz3szUToXTLum0eJa8OJVCzAv_ZFn7zCBfGLiRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LzZZptGIIqKLqcChYljzDPJIX6u7uJxsrIlHblfakMEXRiB6OHoRH4IJUq9_o4N_g1W3uV8xfqa7ArkbY7R12NgUcWCBjNUMTj611aWm1AZr4fAnJ0E_83Y_ye7CZfTVijHZXpQD7dOqFcCI11VGJ-n6QFh-4fPMUYYPGQS-D4KX30sOCX7-QSZhxWQ0ZNmsbfjIjL5FfTfP-r7PTySn9Il5d85PmSFm1i4W6pYzKCW_D4VhGdbQACd7yO56oxDdDY6Q6gPjx4BZftaq9fid_MYClm4hN6SAPOtEHQXiB4vfjdzygOhE0HGJv9AmtH8YjLJ8krziS4-2bUpvY8YVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NShd7WeK6LqLrLMXb80sCHgG2NowLtgNNOAj2dGkFItZTLdd1m37TLrL7LAL9nY6RtRRjqZMUlAg_5gDSPTAx8kEiFm4ayOKqD5vwOcNbQ9GozZ-KjOtkZ9bBtdsmh2ilWHqoC2rQ3vgOT_RnIRAKaRyPJ0aGkU5tvwIQC2rYk-10ZvOJIGPij-67uRbDzkuInWfroTLe1O8nQHAVx8q1BJme7eaY2Lp96AMPbU8pd4uASo2yqLEcO8GnyePgeFyzef4GA-ww2q-hAPowtTUobbKd3Ru2ujzSPlifQQoqBfaZZK9z60LSU5vPxnMpP7n_y_ySaqtCkkColm5u58t5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZLbR1CkWwK7_B0eZpBGDYV3eeVQQw1lN2q3PEDeKzW7IoA7KNmBhyeAdQSrnbOwjCvJYAM36zWiidizeVk0Y8MdGpveXPftHaC4t0mMZ_ULKC3ga-fWEHAfpIkgkXLE5iwUQbw5XRkOqTym72Nc_-Rp_O8l0WquKGaDsbPEuPgGQjrYkXU8ykqvhd0aDCF31ewqPj16Sd7PBPFpaOZqeyaeE8IqHKTalcq3vIAdMn8xCHfSFhGp7eGpClZZ-al-eesBgReLeTkHhWVvoEJWNk-wAw9pQdBlB6TnJp26Rwz_G02Hr8LoI-DefPbbnlZ3eq1LsUvpblVww-Ww50J-2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23370" target="_blank">📅 19:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh3V7vpmc1sruwhGXKLEB0_cyZWtgFfJYZAiTxvmhOSPX8NBMyKJzqFoWXsRT_9ieghkE_5ixezMoaKg_stoC2O-scD3h10LFmZSyoAavcZ3WZ_u5vcaZqSQ_9okpgKuojR6yLZXs8RJ7Sp-ypqLZa0zPKC-MV3STBScr-269aMy6Kc6x51wvgh2qZAME6z1l9vPCPXv-1Er7KN2MFDuKrhJMWOmzEPdfsOc1_ZjD_yHfLd1ZI8azxQE5Pto8EBwareJ3atRtcoAcM-Qy7j7WqbHgAd4qowhxvtcarkMkTwSdhl0LqGi36uWq9OV6cJzsT3e8Tg5eE2y46lJONrUhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23369" target="_blank">📅 18:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIcxmb01vMC4wejG9gZzGaeEMyB8-QV4X2HGNJLQcMKeOUDvBMI53Lq9xYb_dxm0FDjJ32yZkNtWSYivyEumKcQSRoBUTxaIaCt0LWCq_iK57_4FujM1cePdaxPnzydJe2d9WljUP9K9ET_kVq70Sr_artncd1sLi_WnAQWoLZLi5UWoh5uSTP1PO3btl4bNYoi-K7K24tkqFVqWXi5Utlcvv2hHxHZWsAVUgMVZcdzzAbEGFudJIQ8IXG8y0tgvV2ooRrNAJIgx5I6JI-6-JpjI2UUse6IOT4jfB_AQ0Fm1i2k1bjjXrYqqDt65gVRceddHwICC-lvW9J4Fdd1xdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LEbQn-Mk5x82QVMKpE-cW2oWmmvaJ8YPtYQ45P6OEfMmxmHfzDsJWsaJjk0ZXOAEis-VxgvgMEST85caMht8EiQTmoGRqdI_Oa-elxxhN1aGMG3xZSLWGhJaRUFGsDKoI3q5GK4FrUbW24a03BniBM0RY81NT1c6H_dj4waKK2AI_dFykq_EhjhPvL0iAXG3gMeWEohIbR3OSVP0AIV_-93hvpBdHm_pLnJMq8tEndZfVrDfnpCrWV_Bo1m8_s_S4n1sMXle6az2S0CjFn8bQMR-TRaoWWQW1UXS4E06zTfkcDKgsY-10OHaKS2gQDdDoAPRWC94Hou87C5MFmCqEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23367" target="_blank">📅 18:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaMv0SylISr1FQUHq_bfRQgTff9FurYA2MKgQocsNyoNxzmJWiBPtE9ZqpIxqzlcn9lVswurRpHzeTMfqkW1cZnRzGVsRKDyu7UyZeS6gTMYBB3DMijupjITtZqXjRbi-Lgan8f9RbnfoZX5ul7Q8gSAE8L6ol2NOLagvaXj82JHN5MGvDjKfAtrbBNoO1AiqnOEfHRZy1kVW4Nwv4NSEVscXzI5bcnsuy9aLpBVytrHJvi1RXiPP9FzMwuFAn2_w1twQp0JAfRI6bvFVxDW_6KkLhgIqolvHI7YEWm-hyCZ-A4Su8Fz2Jaymd8poa0sM-kGKm3XWR86YlC-FmWhkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23366" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=mOUVG_VzIEFe8slWo5Qvy1NtUDok-_4QEIHwSBGn73cAw9Janl5tYfAf9xHLywq5I5RI7OS7nH-lYJyaTfKsbyA1KR2pyPBFAMqk8dXPSEf3hnYzxK9ntIGxsAIgzfX3aGIf64Wtey0QKYYweFCgIdDaZwfuYq6ur8iwmOjKn1BCs9KF19PwjBKaX5wu-3Xox0S8rwLJwiApmqbERVKX2ujRZw_wxqOfOfy-SqzU6aahVGIK1SGSVo9u-KTBfyvIoenqlMF0MZYoDZsW01oU0hRxJNr7ClT8e7nXhzYpBb7lnlVVuExEsWiWUOH6fAYJcMHxZ4M65M_li9ouyeXd1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=mOUVG_VzIEFe8slWo5Qvy1NtUDok-_4QEIHwSBGn73cAw9Janl5tYfAf9xHLywq5I5RI7OS7nH-lYJyaTfKsbyA1KR2pyPBFAMqk8dXPSEf3hnYzxK9ntIGxsAIgzfX3aGIf64Wtey0QKYYweFCgIdDaZwfuYq6ur8iwmOjKn1BCs9KF19PwjBKaX5wu-3Xox0S8rwLJwiApmqbERVKX2ujRZw_wxqOfOfy-SqzU6aahVGIK1SGSVo9u-KTBfyvIoenqlMF0MZYoDZsW01oU0hRxJNr7ClT8e7nXhzYpBb7lnlVVuExEsWiWUOH6fAYJcMHxZ4M65M_li9ouyeXd1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23365" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzZVrb8KoQns6LpTaIszSMmWSADpB2KTnvdFmSZXdXAjHQea3qsVCFMROed5tc1AEKAyL0w3SZEzcUyceyo_TqRFx4dEm5xupoERmasuIXeix-E6r0wqXWqz8_aU2nnx66reSj5zzJSbYQdjgtmLRphb3z0FdZp7MJoHFt4glDz3xBUHJ20Hz7cZSouLSG8ShV9df4JnOuaJPlC1Lpor7jxoGFaaPA-lijTEmajTMKz5o2s5TAqFNC2jKyfWmUIXWr2Qf5fNo_kjJW5Mx-5x54igRjqmimYszhavI2zz6VfSrjDgWcs5ulkDiy7fiqmmPa6AMk0Arb8brDEbY79rNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23364" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meVzyqq89vFBL_YTGkzNG80JuEt8Ijnrv8tqYpQa2UdmL6CKdU-FkQ7H_9MuC5MTwOrWE-576jrK1Xq04bfJZKgUaoMmlsFUtvKIT_v8BRPNhABbm9pmfdRot8rCQP9uICKw9dgDD65CFdntLN6QWoouSQj1-D5HD5_7QEwAOT1e33vt1XcRsANBa6uzYr6vKI9q25jRsFJLWFPQ7R9mVRaWshP5JcBUUB5nCXp7K9xwi5l2dEn-rGUlNvFQZrCGuVaJIDa9bTwZ1allKPXdUlk7bjBoVR0YeF1iMRdJU571ybATJUFd0HkzwMzjvteNfdrR2EkCU0hMGazP6eGUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqGfTPtXQk4bTEeCRSMXqadCUar2kAZd9FGOj0i1hQT_8sIA3gN_cwKSiPEE7qDaj8s8jUYdwEIFu-BHsNgjq5zMZbTda9SIoTBw7_FYbb-PMMGCcqokei-GVpm8nEddiRm-X_BVWr9Mp2b71ipV5JiwLb2tIjWcU8WdEqNS9DE7Xme1IZnwLX5atvxjnRrdgyF3oXH9yGLBsHgNbzbEkBdzGxIF3_4Pzw0WZCJozvzS2MocRC3k-gsLW1jIjB1yOG44uc-WboWxd5mwcOr8wJrl33gkN6N6P4kUKvUY7meCWm713NvW_NTVgPBvZ1obCwo6GF2wRdKF9FBRoXpIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23361" target="_blank">📅 17:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQJbF0P1IfI9CVzFGLGnSSxO0waXtI-GGUqZ5hdFHsXT2eD2aSN0yU1MUxGeoYa3yJwlkpIb5WTKeJrLM6PSxIzLUnhk7je8pb_2RqBog5U-LDLgLo2LftfOJ9n9duJCphUlOBueYskb1DaUCEv9IOKZ_S5O3wr_f6CmkHHQeS2JF6jE_Hrv4mpEaZQXSx_bCF0DbsXSXCmGSdZkeySvOYrUYh__vW9l4Nx4_svkKFFhS79MOLgvHioAfmp5x99PfJ7m08NDNd2EKXO9vmKvw7omnTaa7iGarov1Ro0XVJe1blBRTQtC7j4kP6JRkqA7s8KZF4bc-PEYh27LpnKimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23360" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUig6PXncfYConlcbvE2lFx-PATBri_ah4JJP693x7Ve_1iyIXB7dq8LT944JIVOiia_VuHS_gHgLlZT28ZYDXpsy_wMXjeEjqVQOceY3yK3PF3M9QFxxhD57d1FJKJCphs4wrMArfpLgYSl_6chBGmbF7SYf37ArVIDFVLUaPv_YdTgey99qponN3O7yZRpeMeAnHNlN13yW2_Aq66r5XD202Q3BkoEmjNEfUf9EdaJwoW7PH2V3xq58ufI4-B2W-QSeFUY8ywieIm5MGpe2R6VfRJW-ktJhqYsXEqMzPrnnkv_LbCFmDEA1-vhTAPBbexQ4Mv_gQQjM0BFkSN-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcUytsCuw1n0f6jR0eKUzGqyFJbx8FQJu9RHhCAhsiYJbVJ3qU9KGHPpNJ-XgTO3zeqtcm90BCkrPEOyqPtFfDOAfdjfQR__mqeYmHOqfD588qMNUDHPJxMJ3uv6479Y-l7TitM_1wbDVVgnFbpI3TSbPx-T98U3PXJJx5jDTVRu6T9HXohAxXJsx3gudyOVs_8Zr-xso5NcFrFlIGP-DIi47wLb5yjKFKeYjbtd7xQ1k2slu9Hd6FNDtZqJWu-k2VnaJnNUU4zVjtx8XJ-EaXC1jW-ccn8d75zpGRyDo1P4B2BTX574SAOU6pol3sMzfoYkoZ-xFg3R7B81cROGGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دوست دختر پسر 15 ساله کریس رونالدو: من رابطه‌ ام با کریستیانو جونیور عالی است و شایعاتی که منتشر شده کذب محض است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23358" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRQ_43Mt0g-Pluq9kqtN6M_LLUy4jNOnX_Hu-lbnOhuwcRJOqWlNhepsUS9airUGPeu5T4fFS0x0FoWDieSZu8inzBOv5NtTlbzCL03Rf00EwGolAn7Ly24EW_xGVSdjhwhaenD3orn2_tgl7nBEZ2K9jCYN1l9yAxunGVdSO1YjYTN2fZxAABrDR8NgSL87vgqZ1ipHsymiLWo2VSCfhooqYJOj60aimnliN8U3ceibAMmFhEbZgW9d_OPJh3sxeGCnxtk2qPfUAk5gK1O4AIXw_wTVDOX1Ck1RvU30A-hidwunLHKW2HqT0lARWdVnKai7SKlfvrA5-D1e0uqnoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23357" target="_blank">📅 15:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23356">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVbmc_LCFtQ64BHzpl8eQWmgqY790HuAkjkVZJX3Vk3jZZf_x1CPiKS3wlIjhrhey2MS2JBjNQlVfJwB6n8Mg6BKoZeAVEyjoKAIL0s_hsvhfSyvqJ_BEtdGNKJTBySYgJS747FdeMEgs2fo8f10zhcJ1dAlBLK2UhzNZ-7XjhAQjz63kH0pZdH7hf1VtqmY4KVFCAZTq1698oKlxEN3kmLxCNkqWl7S54kxcezo9oviaDi2gMVzDKgyX9Yjm1p-I6MvbwKVOw_7pCKp0YOgvG2TdXEmqYenbBGeHEH9oZ8EHQlQJhrnhcISItebpxVKS-ohSjq5We8Ir_iyGR2zCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23356" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7YJ6WbY8d1JKGAYXeFCVQzBMuDbn8_FpVIdKhl-571Av2nrwkUFmCCU2GxMBUWyI40SF6e7Q2xDzi4gUp0ovHSoiblbVYxk0mz5gGOiozweBHjAe-qSL96Y8NiZkEtEYSv5nX4GvD9dV7JI9O2wKYjwNr9eOEfSrhTVDztCbAhIb-cc8tp96O0nXjnRpbVlwE3PlBcFKsabSFylDHAzhEpZn32AdEe5-AyYHBz4B_nVB3xHwOW_I2z0f-ACDaGmzxdwr9oWdJ_rdF5AO1MqPV9r4O1-wh9YMMgl69fG5tcbCHwb4aWxGk9HSxJ2fnBZsrwRGradAsOixt6ra_1akA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23355" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dr_panMmlXcGkzbvbQWKry2C98JedmMJx8f6SxODPHlz7D3ioMx6Xnj8rDZYO6rkDcr6Z8mAa4h9DkhgnpzYpik75SuZ2UsarZibJN2lnjY2-HuAzIMOr_v2vKob4kBBxwGAgBZ5y76iXbJNTY2Fd6ijc54RdRJLD1evzx44-jw5AsRnfYz5Ng8VPBhwFO39pwaS2jmDKOTWs0fo4mfAT1Fq6VpMhdQgTQJ9qgxugq1C4iAM3ak1i8AMUpxSupG6UXcsERyHV02ya5ETGeTDEdgsgam-9lNaz-XblB2rKpa7XK3lZYcXwe0e0sgLqv1ZRi9ppc-5CF_vonx3qGRwag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_1m5wzlAhu1zOzTSnvaJDMm6iSR9fRYCIkUEUvc23UQ7cWPX_fgBjAqqSy6yRwSH5QF8agHpcD-BOCeik-UO2BSZDKtu-zbK2-eOD9dH5alOmNGFhIc4IB5u8ktJTskG0D8jOmxzGFbMgXbR3Ji2KocVAYVHN_5t6siZCEi02NFAI1oaNYGRyikKqHssQmmAW_p3xD37IP3ghP2HC8aittLSqUn_6a5O8cGGlZKfrDX43U9r2RIt4yMJUjUn7KZ0hAzxxBUVFYsKoNF_iUjjG8-apl3mLGrqtYXarA1THbW2AVBCGFkxt95VurIsRW9tmWtNjvejDOFNRe90GBueA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نگاهی به کارنامه کریستیانو رونالدو و لیونل مسی در ادوار مختلف رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23353" target="_blank">📅 15:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMd8NMVY7xlLYAkIF8unzcCheKoLivWAytjRpzAkY8MiF5-Sl7kIka1Y0saCiM15zOmTxYygGJUl2skFQ4Bt3f4_aimmxANHGkjo0UT_msH05uqlVYjH3cg7A98qmWgqTkhC0o7nNxSlQkOqBldQr6AIU_UGZOd9PJ8q5edMIOgHafUcPO-ZJ4l5uaYt0-0GRCnZ6drRxrnevfNCgyqzEZn-JVqiswGemXT56EiIi2uNlHCUyIvZw53ZhWtIXJ1KJEA1qim_tpJPxBVI3swV6OwoGd29NntCmDmO-fyUvh93omzo3Zjw7vU7vY35m9DFbhKIp9zLff6k9iEe4tEWWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ‌ملت‌های‌والیبال؛ جلسه‌‌مهم پیاتزا با بازیکنان جواب داد؛ اولین پیروزی سروقامتان مقتدرانه بود.
🏐
ایران
3️⃣
-
0️⃣
آرژانتین
🇮🇷
25|25|25
🇦🇷
23|19|23  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23352" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23350">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqUFvPeErOGG9i4eCKuM-4fBHm161qEC4m6hM3kNBtiBeazzjCWWmR_mjGIzb_2N0RdOiJZzSL95ZtsuT1bGTdpiTywOUT5sd0ePb-qUROwoG7ukNR6WSDiFPXvbE9tmFFXCbVx234d7x2PELo58kKlK6TDdheLRG8q-_RWCgf6JwDp1NHtgoflCt_XoOYj-esEPTcjzCl3R-q89ZsTGsESmbTQPPCjJzz_rSkz_CnMToRrT9FoPR_AdDTaeDOsNPH85U9_Vu3yMTkBv6xRnDcUkdPWNgAAE2OmTmt0x4__2yFRXlq5JBm5gJDIDGdoGnQmWVcUVyETXcYA0DZRemQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/smaOPhvn6knhH3lCa36hyjNkhWGhMl5w1mbnQuYaPdDSyOgztWDqp2AEglCf2lAl-oY8IENwwsuMYoszsrEXo101IJNY55JBPAsp0v6BsoNh0glAh2WXmiNS91clp5rQoCvwvEAHtyqWGN9vGRvffSJfTcvtBoHD_gC4ebFMpgsov9WpfLOz8J3gjzXZbOT_aF6aRZ5dPX5XTi106uIGmcAw7qLASd2ZQC5eNc3TkIBHdvtUu0J7JLYEF4EDzHaySMCUcMF1qm1rFFEYvfNVVVOi4xBwvJn2da7e1iSNV-xC28iRZLgDgzsOZrRHmCNVChyjSrqKk0CkE5aj18t6jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
گزارشگر اختصاصی بازی‌های تیم ملی مصر در رقابت های‌جام‌جهانی 2026 ایشون هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23350" target="_blank">📅 14:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23349">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENTTr5siQkM1gTWTKUqejxQpTzq6IHnwGjJd1iGILPrAMdXiQeF8EehJAC4lsYuCLqWIQmcbIY5cGk3OGxTp6Z3k72pFdwhYXFnB1GvZZnDYQZFMhMyx_6RE-6BYvJFwrdG0noTewa2MU09QOraJ0iFQUdVf8b2SHD9iWbkKhccPZhVBvLxgNOob1pBbQWpydOgcI7F0AA8YrtLK50wkTxz9pMz_qlraA-xyfcQ8q1C1I6M50UoVyo0A3DRKOJB1M_ERNM5IXi_qmRfEgnlOABjxSpGQVf3DBUu4crZT9y5gvJoOs1ZzOTF-IHTLkHsRWSyuqX2s1Ka-t9AilPJEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23349" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23348">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=DMf5DPK0b-MV_ENXpXJ3Rzu6WY1N6H1MCj-2MjBt4jL27tVfDspR4nS9-aMf5yMW_DhOg9-6V1eqDIIYOAVRsvd-C5oEsavURqC9fzSzTlejABN_z5_HVkCcJOkqtvSKo1-0GrOOzkotlvcYyVTBgRpM8mmmHL5aGiSTKO3wVFSYCfmlwM8OljFg90hGeiLsL2zgRRNFZjZyehkvFfMzLX6-z_z-bFhZRic2EbckpIiruMvBSteaZbdWcn3GHV5wuDkDxlvpv4f9EzAAUTBAKKp0AN_vuMJXgFqy4hsfGms6yB1-zAWljwHB-rb6QRZojUK6Sz9fTVR9wByYK2J-0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=DMf5DPK0b-MV_ENXpXJ3Rzu6WY1N6H1MCj-2MjBt4jL27tVfDspR4nS9-aMf5yMW_DhOg9-6V1eqDIIYOAVRsvd-C5oEsavURqC9fzSzTlejABN_z5_HVkCcJOkqtvSKo1-0GrOOzkotlvcYyVTBgRpM8mmmHL5aGiSTKO3wVFSYCfmlwM8OljFg90hGeiLsL2zgRRNFZjZyehkvFfMzLX6-z_z-bFhZRic2EbckpIiruMvBSteaZbdWcn3GHV5wuDkDxlvpv4f9EzAAUTBAKKp0AN_vuMJXgFqy4hsfGms6yB1-zAWljwHB-rb6QRZojUK6Sz9fTVR9wByYK2J-0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
اسپید یوتیوبر معروف در حاشیه بازی بامداد امروز آمریکا میگه‌ رونالدووپرتغال قهرمان‌جام جهانی میشن؛ زلاتان هم این‌مدلی بدون هیچ‌حرفی بلافاصله میکروفون رو از دستش‌میگیره‌ومیگه برو بیرون بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23348" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23347">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qttmnIkp6rE6J1WhhgR1lh8Ne_gmL3o5A9vMyEic2pMDiOIAmGatpVYBUF0WdNP5G_aExJVijggyHLrV2QaDS-OAWJWsHmyRs6SVnpqDjqHksZFXTpESuZyx3vxXR_nq2jgpys-43v0xZDXtUt0U3vjBm0OzmwlSYh0rJkp_zqWPp6OgZJtxA-b-GZAhZkEZn9LNrrx1f0Mz-qIRBcpZ3AbIfEIYu0DS-oIY6DIF4SzSb4DHIcPoQObhsVihXQcdsnAKCy8-MWMDb7lIMaTgJDK5AqY4FqN5Nh75ePcoTHkXQBuh3CDuh5HGft3mNYxTSk4Iil-RxvVX2y-c5MIOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23347" target="_blank">📅 13:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23345">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gmgENC45DdKkx1GaTS0NC6FactQroH8SVwzIHH2mfYxRPxseQBp9UAoBBHHMuwGv6JvVhZRCi67ej_4P0t_Toh2ZugDqGdRzbb_Q_lAg9iDApPfGiOq186FPoTyTT4yaP0pDM__B7mmtfucAuvbk5wcNf2k0q-MnlCqprR9b6EEcc2diFLnUu64NqrupXdJC58V8KHPkkcCs1TYsLkvJCpdKeis6hUBi4WJ1kyFOFOPhS8jHQ11WfUa7QoDrGHOFnxnxCeYXvVH9kGB6UUMy8sdQ_Bd4__3i3lwvWngIjxI3SYml1_Z1nCRejcQOQCN6KT-2g-s4HDt6CYpFvG-t9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1A07MJ3_TAJCifwXWBVasarptp2IQTpCO4cUOqVqweqdts7boTk--geZb04LTT7OSmT3e354hlenxAlz2kGG3vMgobiM8xE8USoExUiPu7rwrexYQ5XYGNUzs5yTOaTlh41Rnu4afLNXW7SYueAqobM9aFeDJU5C5FgYpiOFTUafX8r05E9BH_6-ScYT6xxHvYJLtAn7iSmunIdL3dSlqkNJenz-0Vi7PXOQtZn5v47NLmdFXRxazCpDE-Bi312zc5N_PKlWkwPoXeQxWt3r2nd4OodtBRurt7SE0Lgj0iXLfCX0c8DkblNC5fs86UGqMsjP9ccVxlMlS1o8w5S4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرنگار معروف باشگاه شاختار: بازی دیشب بارسا و پاری‌سن ژرمن فوق العاده بود. انریکه یکی از بهترین سرمربیان حال حاضر دنیاست. همچنان معتقدم که باشگاه‌رئال‌مادرید قهرمان این فصل لیگ قهرمانان اروپا خواهد شد...!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23345" target="_blank">📅 13:09 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
