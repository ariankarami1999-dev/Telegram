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
<img src="https://cdn4.telesco.pe/file/JSP0A1E8GkF8kgJUtifiL_10rbXFLkpqqGxrcC1NsshkjwlhXt5CsdIWcvhA2qnSUknBVgSIdcHB_cx78QF9ZAoV-SRLtMSc0w1ttdlyT9Qi92n_QJinReWIIx3MU2YW7IxlVAE8A0IfE47RRlsfYbuE1b5AfYdHvZ4H1LmcsO1pagbRp6ueJDIwfFHLgkGgqyW751GDWeGzYBaCHkyQDhjq_clVQ2MJb_42hmqO8D6kwMGMDVPvQBBqdDJ9gnSgA2Ro9cnOsHZE07jMFFiiei03pYHF-yW6J_VmzxodrngQXnQmGTKFPV9OAhnTrq-DkVud8bmH60ZuO6zvtHPnBQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 09:11:44</div>
<hr>

<div class="tg-post" id="msg-463345">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0ffc79845.mp4?token=FXIVxjd_r_d5nV06aQ7_3-Pe5p9xLUiZUJJ_fQotadvFq12Pu0Wy1HPIZtXHlzjw5BSMktHDjcp4y5UMcF15T20BBaPQLiQIvrYZti21Q4nyfSFqd0SuivR2kY6Mo5VdUIG6wK5QeQYxaGtTBBGJU3PtYVVMugfZul1iLcPwKQ2ET6JKkdr0ES0UNdR56NPEr8SR9rnb9IHWYNanl6GAmbU0-hAfGsRuxwDhReCS08ilCqoXvdhu9uNkQzBZ56qU_S9MA45PjhwzPs7h-yiCB3jkoG6Scap-felWObpXfdw_3p6iFtPyOVXD56FrUDPt5Ol-uo3-Ts00m_ZXFCirkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0ffc79845.mp4?token=FXIVxjd_r_d5nV06aQ7_3-Pe5p9xLUiZUJJ_fQotadvFq12Pu0Wy1HPIZtXHlzjw5BSMktHDjcp4y5UMcF15T20BBaPQLiQIvrYZti21Q4nyfSFqd0SuivR2kY6Mo5VdUIG6wK5QeQYxaGtTBBGJU3PtYVVMugfZul1iLcPwKQ2ET6JKkdr0ES0UNdR56NPEr8SR9rnb9IHWYNanl6GAmbU0-hAfGsRuxwDhReCS08ilCqoXvdhu9uNkQzBZ56qU_S9MA45PjhwzPs7h-yiCB3jkoG6Scap-felWObpXfdw_3p6iFtPyOVXD56FrUDPt5Ol-uo3-Ts00m_ZXFCirkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان خطاب به دانش‌آموزان: بچه‌ها سلام! می‌دانید که شما گوهر هستید!
🔹
می‌دانید من از یک خانوادۀ معمولی به اینجا رسیدم.
🔹
شما اگر ذهن‌‎ و فکرتان این باشد که بهترین شوید حتما می‌شوید. ما تلاش خواهیم کرد که شما بهترین شوید.  @Farsna</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/farsna/463345" target="_blank">📅 09:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463344">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cf94be4a9.mp4?token=ctnie4fkPuj5uxhpMJQHmk72GoH2KMQHR0etXrJVeyke0dhxOcwzsGQ2S2kWVhlqPTbjJxeg4RfXTIybUbstz7yq1Q5X1wLxQCqd1h8vErV9Koo-BAEam-pZGoSwexp8REs00UQfuZQ7PCClSC4WD7-PtclAJDQrAX0G2u6JE1bDTjcbZUbD86Vhv5-CNjTyvPngB3hWEyjgZvDL_7Rxg2w1u-FTIVvONirJXE01JJt663QfOuc-9G5mXVb8HL3nQyzdux56P1qH6WgFB4vEsa6eqrmxxwjCMCM5iB6ssvbvd6Z0Z5ibq1iDNSb5IWD_2S0q_1aR7lct51QtR4qBxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cf94be4a9.mp4?token=ctnie4fkPuj5uxhpMJQHmk72GoH2KMQHR0etXrJVeyke0dhxOcwzsGQ2S2kWVhlqPTbjJxeg4RfXTIybUbstz7yq1Q5X1wLxQCqd1h8vErV9Koo-BAEam-pZGoSwexp8REs00UQfuZQ7PCClSC4WD7-PtclAJDQrAX0G2u6JE1bDTjcbZUbD86Vhv5-CNjTyvPngB3hWEyjgZvDL_7Rxg2w1u-FTIVvONirJXE01JJt663QfOuc-9G5mXVb8HL3nQyzdux56P1qH6WgFB4vEsa6eqrmxxwjCMCM5iB6ssvbvd6Z0Z5ibq1iDNSb5IWD_2S0q_1aR7lct51QtR4qBxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظۀ نواخته‌شدن زنگ آغاز سال تحصیلی جدید توسط رئیس‌جمهور  @Farsna</div>
<div class="tg-footer">👁️ 1.68K · <a href="https://t.me/farsna/463344" target="_blank">📅 09:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463342">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGLnoCYalMGP11VIAxReKFZ9b9-DgbASiS9lFzIOZUZP0dnxNrkU3n5FiAf2b6UWNSGk5uQGXkOpI47a2ZQzvC7WqAOvh2DKR59sLeAi_TQ9-kDHSUrAmNONI6nKTLD61ugW8-MubBycI2gh54VDv05FNwjr9Zhg9iNwbvxUyX2rubnxRQxPBL7mMkT-0oO98KQ67A9guvyRuP8IXijSHM1hDgjAc8DKl-64MFMz8OxpENgTDT7Y9aF5Y9WZ0FsVDxoJ5szEIfoAWYjNRGb58KmDVT0VpM_HEX6HPw9bKAInK3CdRqqEJSeEFfjUMGhX_HgL7AcfxladfWNFgclzEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف ارتحال آیت‌الله شبیری‌زنجانی را تسلیت گفت
🔹
رحلت عالم ربانی، فقیه ژرف‌اندیش و مرجع عالی‌قدر جهان تشیع، حضرت آیت‌الله العظمی حاج سیدموسی شبیری زنجانی، ضایعه‌ای سنگین و جبران‌ناپذیر برای حوزه‌های علمیه، جامعه روحانیت و عموم ارادتمندان مکتب اهل‌بیت عصمت…</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/farsna/463342" target="_blank">📅 08:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463341">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌ سخنگوی سپاه: یمن، لبنان و حزب‌الله نیروی نیابتی ایران نیستند
🔹
برخی تصور می‌کنند مثلاً یمن، لبنان، و... نیروهای نیابتی ما هستند.
🔹
آن‌ها خودشان نسبت به تمامیت ارضی کشور خودشان عِرق دارند، خودشان سیاست دارند، خودشان تشخیص دارند، خودشان تصمیم می‌گیرند. گروه‌های…</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/farsna/463341" target="_blank">📅 08:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463340">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69d1407c5.mp4?token=ILDFsn0Id-KRIefvlszg3g7GNtZu5d_o7B4B71CRspZ7dupAcr6sG9iN5Seb-MJ2N4hWqrwX8G5Gq7gGw-D5mFu8Q2QGtVR96-3Lxmsq1PIKus7rtf0duL5djEMw6hzFSPApKz5SCAgWnDbjT1U17dSmwvLCv9zO0epZpupmCRl3GvpPBBn0DMplKaJKZHBrrZHeJPloGTui604RrANyEWJgQ0iGFoXGnC3VIxoA7JjwDBpKcGaTDMr6avfd0G-IWcipHwTViZPFt_AuDdpD50GX3zGQDUyXP3ugn5wvGqOH10QjenluKlIZtYmqXQ-NLvh7nECr48ZlsQ9MrW9QhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69d1407c5.mp4?token=ILDFsn0Id-KRIefvlszg3g7GNtZu5d_o7B4B71CRspZ7dupAcr6sG9iN5Seb-MJ2N4hWqrwX8G5Gq7gGw-D5mFu8Q2QGtVR96-3Lxmsq1PIKus7rtf0duL5djEMw6hzFSPApKz5SCAgWnDbjT1U17dSmwvLCv9zO0epZpupmCRl3GvpPBBn0DMplKaJKZHBrrZHeJPloGTui604RrANyEWJgQ0iGFoXGnC3VIxoA7JjwDBpKcGaTDMr6avfd0G-IWcipHwTViZPFt_AuDdpD50GX3zGQDUyXP3ugn5wvGqOH10QjenluKlIZtYmqXQ-NLvh7nECr48ZlsQ9MrW9QhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان در آیین آغاز سال تحصیلی جدید   @Farsna</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/farsna/463340" target="_blank">📅 08:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463339">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkeL9DsA_JzR4TXlwNkgkKkXxQxyrmJYCNuVdLlragI5n18uvCRLnzMsqp5K1-Urq8mX6AaEqTZd2jxS06VuN0nWXz1481F8ClXC1SyiJEp2TdsexDd6FipCrG8wQ66MVwrnHX45elTP62Zl2RkpFMtW-WOnx2EecOq3QG1w1B8Cb0z1f823NbMGVv6cuJAoj2KnrKMA4C0h7wp6YiFxhd6oRoeYGsvpP5s23D4IFKdqrwrUiD52jhhCECtvQO-koYwCeGI1i3cSEk_02_Z0Yy1u0ujdm9ri8zwk33Z8BP5Ma41JF9fI6qhR7Li0gWSig8aZkzAAUnweBxgmUSz_Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌آیت‌الله شبیری زنجانی دار فانی را وداع گفت
🔹
دفتر آیت‌الله شبیری زنجانی اعلام کرد: روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🔹
جزئیات مراسم تشییع و تدفین پیکر ایشان، متعاقبا اعلام می‌شود.…</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/farsna/463339" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463338">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‌ سخنگوی سپاه: اگر تهاجم جدیدی صورت بگیرد، قطعاً سلاح و جغرافیای جنگ را تغییر خواهیم داد
🔹
اگر تهاجم جدیدی صورت بگیرد قطعاً تغییرات قابل‌توجهی در دفاع ما و هجوم متقابل ما وجود خواهد داشت.
🔹
آن تغییرات، تغییر در جغرافیای جنگ، تغییر در سلاح‌ها و تجهیزات جنگی…</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/farsna/463338" target="_blank">📅 08:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463336">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b04ff241.mp4?token=QnJT91xQCowlxHCD2MQapL7yWVqX5VRIWEFhBbwFwvBtDyv8wXyNCXZzNt32QizC_u-qnFfoSNfpPVuSZ7Dn3Q2Ndu5bjCbnfX-K8CboIV__uKwKde2IquOFcDb9ehG7yS-4w6Qqh0BS4hafshwokr53gE6PU9oIaMRfoxZGcUce-gOXYnDieveMMbj--2_Aenu-XB-dvd_vVmTuGlz15thefbU_TlijQ8ZfYLVgrzunuXhJkzwU1UFHDlLJxL1Hzzg4_NYarS-OboZJkD0_UFaz2Kbo_x_5igklYuytRbX2EZSHPEPAItosb3MlO2ddjhkaeedUb_Zycf8s9r3s6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b04ff241.mp4?token=QnJT91xQCowlxHCD2MQapL7yWVqX5VRIWEFhBbwFwvBtDyv8wXyNCXZzNt32QizC_u-qnFfoSNfpPVuSZ7Dn3Q2Ndu5bjCbnfX-K8CboIV__uKwKde2IquOFcDb9ehG7yS-4w6Qqh0BS4hafshwokr53gE6PU9oIaMRfoxZGcUce-gOXYnDieveMMbj--2_Aenu-XB-dvd_vVmTuGlz15thefbU_TlijQ8ZfYLVgrzunuXhJkzwU1UFHDlLJxL1Hzzg4_NYarS-OboZJkD0_UFaz2Kbo_x_5igklYuytRbX2EZSHPEPAItosb3MlO2ddjhkaeedUb_Zycf8s9r3s6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پزشکیان در آیین آغاز سال تحصیلی جدید
@Farsna</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/farsna/463336" target="_blank">📅 08:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463335">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌ سخنگوی سپاه: سپاه وارد عرصۀ دیپلماسی نمی‌شود
🔹
سپاه پاسداران نه حالا و نه هیچ‌وقت دیگر هیچ ارتباط رسمی و غیررسمی با ایالات متحده نداشته و اصلاً ورود به دیپلماسی هم پیدا نمی‌کند.
🔹
سپاه بازوی دفاعی و نظامی ایران و اسلام است، و در وظیفۀ خودش کاملاً مجهز، مجرب…</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/farsna/463335" target="_blank">📅 08:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463334">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b690fb886e.mp4?token=iF--4tWJlbuzF30oufxMJtHCrCty-iDuCCMIvtEgdkbXRmqDEigVUY3eMT-IolPrPdUbxe9c7nkiNeC9Gt3SI8OsaX3Ec5XKWImSiyAqWslT04zHxL6XzE8FzFdjwoXnE_NDU2PkF6jlRk8byKCQODqmvkR9aS79y__z3-E4SpDNLQZ4XkaPUtKbK-EfUO9hS04j4CWO6SwtVkp94EkLk8hLminVmRnb3Rgt3f5OuVuGUsQEFSFQ4iCu__u1c04uEWd90JxO-v0N37i_A1D6b-HERrW6QmtNaQDcQ-N1qR4bZHXvu977KgnZrWc4p_NQCkrrnv4qx53zswIIv5a5Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b690fb886e.mp4?token=iF--4tWJlbuzF30oufxMJtHCrCty-iDuCCMIvtEgdkbXRmqDEigVUY3eMT-IolPrPdUbxe9c7nkiNeC9Gt3SI8OsaX3Ec5XKWImSiyAqWslT04zHxL6XzE8FzFdjwoXnE_NDU2PkF6jlRk8byKCQODqmvkR9aS79y__z3-E4SpDNLQZ4XkaPUtKbK-EfUO9hS04j4CWO6SwtVkp94EkLk8hLminVmRnb3Rgt3f5OuVuGUsQEFSFQ4iCu__u1c04uEWd90JxO-v0N37i_A1D6b-HERrW6QmtNaQDcQ-N1qR4bZHXvu977KgnZrWc4p_NQCkrrnv4qx53zswIIv5a5Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نشستن، سیگار جدید است!
@Farsna</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/463334" target="_blank">📅 08:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463333">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌ سخنگوی سپاه: برای یک جنگ طولانی آماده‌ایم
🔹
از نظر ما جنگ همان جنگ است، مقاطع مختلفی دارد، ولی جنگ همان جنگ است و جنگ هم تمام نشده و ادامه دارد.
🔹
سپاه پاسداران از قبل آماده بوده و الان آماده‌تر شده برای یک جنگ طولانی‌مدت.  @Farsna</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/463333" target="_blank">📅 08:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463332">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‌ سخنگوی سپاه: امروز ما هستیم که نظام جدید منطقه را مشخص می‌کنیم، نه آمریکا
🔹
آمریکا به خاطر بمباران مدرسۀ  میناب تمام حیثیت خودش را باخت؛ به خاطر بمباران و آزمایش سلاح جدید در لامرد، دنیا را از دست داد. به خاطر بمباران مراسم عروسی، کاپ اخلاقش را نابود کرد.…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/463332" target="_blank">📅 08:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463331">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‌‌ سخنگوی سپاه: تکنولوژی‌های آمریکا قادر به دفاع از خودش هم نیست، چه برسد به دفاع از هم‌پیمانانش
🔹
برخی تصور می‌کردند آمریکا از یک تکنولوژی بسیار بالا در حوزۀ جنگ‌افزارهای تهاجمی و دفاعی برخوردار است که این تکنولوژی غیرقابل‌دستیابی است.
🔹
اما در این جنگ همۀ…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/463331" target="_blank">📅 08:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463330">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjW2WHEGAaV9JgmzKmMV8I6XE1WEJsWEjMZO8KZ7l0r-nct23GaCEWKgwcC6i2470IuoFnPUlCyIAFlDKog9ZerEGKsgVcY5Oer6yfb3VBjuUeBtDQLaYVSrvLtJpX6bCm4v3GmtwiiZbjguG2hDjI0YuML3LKoYiyZzszo2ojINp8Tg0t8ZonVM281BxPAJQrKhQjb8eyPwUT-Z-qvbtggnJLqg2cSUmTJyNY7ggadZ5AACz9VLze6j-aRvN_HcTEOnCfLWN0zqDDFHhpd3Kwt_hepsmItH2Bo_0gY8k-6G32sIkSlABOR1biVQl04abX1PlSaPRyKfP6zwAH8S5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌آیت‌الله شبیری زنجانی دار فانی را وداع گفت
🔹
دفتر آیت‌الله شبیری زنجانی اعلام کرد: روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🔹
جزئیات مراسم تشییع و تدفین پیکر ایشان، متعاقبا اعلام می‌شود.…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/463330" target="_blank">📅 08:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌ سخنگوی سپاه: برخلاف تصویرسازی‌ها مراکز اطلاعاتی واشنگتن قابل‌دسترسی بود و مورد حملۀ ایران قرار گرفت
🔹
این‌گونه تصویرسازی شده بود که آمریکا یک نظام اطلاعاتی غیرقابل‌دسترس دارد.
🔹
اما وقتی این مراکز در حاشیۀ خلیج‌فارس و در شمال عراق مورد اصابت موشک‌های ایران…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/463329" target="_blank">📅 08:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دیشب که خواب بودید چه گذشت؟
🔸
آیت‌الله شبیری زنجانی، مرجع عالی‌قدر جهان تشیع دار فانی را وداع گفت.
🔹
سازمان هواپیمایی کشور، شایعۀ توقف پروازهای ایران و عراق را تکذیب کرد.
🔸
قیمت نفت در آغاز معاملات هفتۀ جدید میلادی صعودی شد، و به بالای ۱۰۴ دلار رسید.
🔹
ایران طلسم ۱۶سالۀ فینال شنای آسیا را شکست و هومر عباسی به فینال بازی‌های آسیایی ناگویا صعود کرد. امیر مطاعی نیز در مرحلۀ مقدماتی ۱۰۰ متر قورباغۀ مردان، به فینال صعود کرد.
🔸
یک پهپاد MQ-1 دیگر ارتش تروریست آمریکا در آسمان تنگۀ هرمز منهدم شد.
🔹
تیم ملی کبدی بانوان در اولین دیدار خود مقابل ژاپن، با نتیجۀ ۶۳ - ۲۰ به پیروزی رسید.
@Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/463328" target="_blank">📅 08:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌ سخنگوی سپاه: امروز پایگاه‌های آمریکا دیگر حتی توان محافظت از خودشان را هم ندارند
🔹
آمریکا طی ده‌ها سال، در منطقه، در کشورهای حاشیۀ خلیج‌فارس، کشورهای شرق و غرب ایران، پایگاه‌های متعددی ایجاد کرد تا بتواند در این منطقه سلطه‌گری کند.
🔹
اما تمام این پایگاه‌ها…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/463327" target="_blank">📅 08:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463326">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سخنگوی سپاه: آمریکا شجاعت اعتراف به شکست در جنگ را ندارد
🔹
سردار محبی: آمریکا در این جنگ شکست خورده و شکستش هم یک شکست تاریخی و مفتضحانه است، اما شجاعت اعتراف این شکست و پذیرش این شکست را ندارد.
🔹
شکست ایالات متحده و رژیم صهیونیستی شکستی است که همۀ آگاهان…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/463326" target="_blank">📅 08:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">سخنگوی سپاه: آمریکا شجاعت اعتراف به شکست در جنگ را ندارد
🔹
سردار محبی: آمریکا در این جنگ شکست خورده و شکستش هم یک شکست تاریخی و مفتضحانه است، اما شجاعت اعتراف این شکست و پذیرش این شکست را ندارد.
🔹
شکست ایالات متحده و رژیم صهیونیستی شکستی است که همۀ آگاهان نظامی و سیاسی، حتی در خود آمریکا، هم به این اعتراف دارند و می‌توانند با کمترین توجه این شکست را خوب ببینند، لمس کنند و حس کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/463325" target="_blank">📅 07:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">بازی‌های آسیایی ناگویا | برتری کبدی بانوان مقابل میزبان
🔹
تیم ملی کبدی بانوان در اولین دیدار خود مقابل ژاپن با نتیجه قاطع ۶۳ - ۲۰ به پیروزی رسید.
🔹
ملی‌پوشان کشورمان روزهای سه‌شنبه و چهارشنبه به ترتیب رو در روی بنگلادش و هند قرار می‌گیرند.
@Sportfars</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/463324" target="_blank">📅 07:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
انهدام یک پهپاد MQ-1 در آسمان تنگۀ هرمز
🔹
سپاه: لحظاتی قبل یک پهپاد MQ-1 دیگر ارتش تروریستی آمریکا توسط آتش پدافند پیشرفتۀ هوافضای سپاه در آسمان تنگۀ هرمز رهگیری و منهدم شد.
🔸
این مدل از پهپاد آمریکایی، چندسالی است از نیروی دریایی و هوایی ارتش تروریست این کشور کنار گذاشته شده و جای خود را به MQ-9 داده، اما حالا با توجه به انهدام بخش اعظمی از MQ-9ها، آمریکا دوباره مجبور به استفاده از این پهپاد شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/463323" target="_blank">📅 07:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YB-i5WWd91XWjkmO_m8jADJj6BYI1hLxoqJw7uckE0qYFOyM0XBSpML8Dx8BYpfaCYNjAGvWfJLmiXb01HStNZGL7SOZzj6tkoQEQjn4kyXAR14YFNyRzF7m6Mw0hhWxQMBrTa9b0-LweGRF1dCPnG5vJtDP2dRA3APlFPTFv7Jj2U1EGBJLSTSKKKqryhnTasAiSVcItmR_54x8wTFqxvRm5CPpEkg74zqJZ99kCXoSm3BHtYO82CfLJqKcdcCT4oeCX6oVjW6tGA-StDjvxi3vPMVD2wORq1uzE8ZY0VrtMBIzEo8pme1TD4uiNQsFWYWBiWxXOP9wND3xHKrkQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFxMfcSloa28VmqR-1lDXTV_aMHBtDJSg-yfh_Nm2J7dXxXhq2dUdlrKHhb-fj9pUdyuE-gfhERC2Pr2jsDMDB0T8C4t0qkrhj0OwINTG-Ydb6VFReO01GIS2kpDmNHzjLjDRQqt6kgfQCE2wyn_yFNj9bpMFBbZGaiT2_-dI7CXfTiWrLgrWyQqLR0mH66Jh8D1h1AjiTMwJdzxjJUHmMjzW8H-fH5dDnF_sG9DlciVbcgmLDkWQjLQ6UXxHwLlZkDpKbcEo8PnaY7Hf1aqBDxQ627P4Cw8otHpMweyXxT5jEjbeZu4IA0h-DdYDsNy5TEepUh5HFJ68TdkFTGibw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت امور خارجه جنایات ضد بشری رژیم صهیونیستی علیه فلسطینیان را محکوم کرد
🔹
رژیم اشغالگر صهیونیستی که طی ۳ سال گذشته با برخورداری از حمایت همه‌جانبۀ تسلیحاتی مالی و سیاسی-تبلیغاتی آمریکا و برخی از کشورهای مدعی حقوق انسان، مرتکب یکی از بزرگترین نسل‌کشی‌های تاریخ جهان در غزه شده است، همزمان به شنیع‌ترین شیوه‌ها از جمله ترور و شکنجه نظام‌مند و گستردۀ فلسطینیان در کرانۀ باختری و غزه برای پیشبرد طرح اهریمنی «محو استعماری فلسطین» متوسل شده است.
🔹
گروگانگیری زنان و کودکان فلسطینی که تعداد آن‌ها به بیش از ده‌هزار نفر رسیده است و شکنجۀ آن‌ها در زندانهای مخوف که منجر به شهادت ده‌ها نفر از آن‌ها و قطع عضو و معلولیت صدها نفر دیگر شده است، بدون تردید مصداق جنایت جنگی و جنایت علیه بشریت است.
🔸
جنایات بی‌سابقۀ رژیم صهیونیستی بدون تردید شدیدترین ضربات را به اعتبار و جایگاه سازمان ملل متحد و حقوق بین‌الملل وارد کرده است.
🔸
این واقعیت که رژیم صهیونیستی در صدر ناقضان قطعنامه‌های سازمان ملل متحد است و بیشترین تعداد وتوی قطعنامه‌های شورای امنیت، با هدف ممانعت از مقابله با قانون‌شکنی و جنایات اسرائیل صورت گرفته، به‌تنهایی گویای نقش این رژیم در فرسایش اعتبار و جایگاه سازمان ملل است.
@Farsna</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/463321" target="_blank">📅 07:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPPSp3OpJDgjW4zR8mCoSyNmIa-dtf7PNIkKKMy1Sbf_C3ezX9rsSlRwKuDZcJO2b3WUfR6GMJ6tsqS3DTnOo-A79jusmQW-QSVoGi_iAeqa7sr-UXG1P8Tk8wf2l9lL72VbZW5ZaWSZVOoiO5TNP5N5qZa5z6QYg5aFM1Cqto9RfWYfHu7lOXOBh6IWudj32p7dZxblioCf0Im0Pkr84lmj_7OmWrEeobAzUXeKRamO1yjSYSUxK1qNKr7nR0-pqNuEFw7W0rS7KKu0yo0tPHty5bf4bj1C49cpyNBede-Wwl3rnoBmZZhx5EqqmwtzTjiYYjzpyIqBEutNaSFJOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درآمد نفتی ایران به ۱۶ میلیارد دلار رسید؛ دست دولت برای حمایت‌های معیشتی بازتر شد
🔹
اطلاعات کسب شده نشان می‌دهد درآمد نفتی ایران در ۶ ماهۀ نخست امسال به حدود ۱۶ میلیارد دلار رسیده است.
🔹
در ۵ ماه ابتدایی سال بیش از ۱۳ میلیارد دلار از محل فروش نفت وارد کشور شده بود. حالا با احتساب درآمد وصولی شهریورماه، مجموع درآمد نفتی کشور در نیمۀ نخست سال از ۱۶ میلیارد دلار عبور کرده است.
🔸
درواقع این درآمد دست دولت را برای تقویت حمایت‌های معیشتی از جمله افزایش مبلغ کالابرگ بازتر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/463320" target="_blank">📅 07:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عامل حمله با قمه به مأمور پلیس‌راهور در شهرکرد دستگیر شد
🔹
دادستانی چهارمحال‌وبختیاری: عامل حمله به مأمور پلیس راهور در شهرکرد، پس از صدور دستور قضایی و با اقدام مأموران انتظامی شناسایی و دستگیر شد.
🔹
برای فرد مهاجم پروندۀ کیفری تشکیل شده و به‌صورت ویژه مورد رسیدگی قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/463319" target="_blank">📅 06:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463317">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4024a404b.mp4?token=a3-qQyfesQV5ZfuAGGKAzq9RIbhMcqO-oqUjSJnS4o38_WEBDWUMqTKrrPmS3in7nZp90ninHh9SDCob5yzNkyyHC3gUjDzUWFvaOb4WWjLComXm0BSLs7w6TLcenjejHXTITHLKs6tY0zGVF3CvxtEojwXp5brA6O052WnEQa_0SCH37n4AmT6MITzbihBdDgUei6GC6Oysm3EDgWTzZWrXkQWVylHGneVe3cra9G_k_V-XoBFyDAMUQEkcdiKbfgn8zoxPzmFQ0uWKtv1Vj76JbHqH4cYOSLlYa8kNl7X2o4rcKS5IvDSHkdUid9-RGfrWSpEzBs5ENZACEUcukQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4024a404b.mp4?token=a3-qQyfesQV5ZfuAGGKAzq9RIbhMcqO-oqUjSJnS4o38_WEBDWUMqTKrrPmS3in7nZp90ninHh9SDCob5yzNkyyHC3gUjDzUWFvaOb4WWjLComXm0BSLs7w6TLcenjejHXTITHLKs6tY0zGVF3CvxtEojwXp5brA6O052WnEQa_0SCH37n4AmT6MITzbihBdDgUei6GC6Oysm3EDgWTzZWrXkQWVylHGneVe3cra9G_k_V-XoBFyDAMUQEkcdiKbfgn8zoxPzmFQ0uWKtv1Vj76JbHqH4cYOSLlYa8kNl7X2o4rcKS5IvDSHkdUid9-RGfrWSpEzBs5ENZACEUcukQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در آستانۀ رحلت حضرت معصومه(س)، صحن‌وسرای حرم مطهر بانوی کرامت سیاه‌پوش شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/463317" target="_blank">📅 06:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463316">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">قانون جدید کالیفرنیا برای اینفلوئنسرها
🔹
کالیفرنیا با قانون جدید، اینفلوئنسرهایی را که در ازای دریافت پول محتوای سیاسی منتشر می‌کنند اما منافع مالی خود را اعلام نمی‌کنند، هدف گرفته است.
🔹
بر اساس این قانون، برای چنین تخلفاتی جریمه‌هایی تا ۵ هزار دلار در نظر گرفته شده و نهاد ناظر انتخاباتی ایالت اختیار بیشتری برای برخورد با متخلفان پیدا کرده است.
🔹
این قانون در شرایطی تصویب شده که کمپین‌های سیاسی بیش از گذشته از اینفلوئنسرها برای دسترسی به مخاطبان شبکه‌های اجتماعی استفاده می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/463316" target="_blank">📅 06:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463314">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd7d64ac1c.mp4?token=MMQNAWWLh-EnDRp5lUQV6wpi4qYtYb0hahHtgdXvxd-PTJrfaDM1qHaoCNuQalxPpH207YsfAclMM5HU_hlHMsnF6_Lm_GSGTgM0mHCZm6XYYPaFGC16nNlV_EzYVst5PlHM4fhvNRtbZ9gMxQX07erM7KXot9fEeWkzXdxnKFRxq4-O2Buyas2FEmOKDVwOXBB9QSKsD3-KhbJvTLJAclaIVJDq_8xS_Mn0iu8y5hSSpsQlO3Ka4E543Sz98gnOzCeLbIad1Ux2IJyn_BrFT_PuWoMurbgQl8tY0CJ0-JhZ8rT1BsfjATxKC7IXRGHbN_CpboF3ZIqedxl4rIuUqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd7d64ac1c.mp4?token=MMQNAWWLh-EnDRp5lUQV6wpi4qYtYb0hahHtgdXvxd-PTJrfaDM1qHaoCNuQalxPpH207YsfAclMM5HU_hlHMsnF6_Lm_GSGTgM0mHCZm6XYYPaFGC16nNlV_EzYVst5PlHM4fhvNRtbZ9gMxQX07erM7KXot9fEeWkzXdxnKFRxq4-O2Buyas2FEmOKDVwOXBB9QSKsD3-KhbJvTLJAclaIVJDq_8xS_Mn0iu8y5hSSpsQlO3Ka4E543Sz98gnOzCeLbIad1Ux2IJyn_BrFT_PuWoMurbgQl8tY0CJ0-JhZ8rT1BsfjATxKC7IXRGHbN_CpboF3ZIqedxl4rIuUqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌آیت‌الله شبیری زنجانی دار فانی را وداع گفت
🔹
دفتر آیت‌الله شبیری زنجانی اعلام کرد: روح مطهر فقیه اهل‌بیت عصمت و طهارت(ع) ومرجع عالی‌قدر جهان تشیع، آیت‌الله العظمی شبیری زنجانی به لقاءالله پیوست.
🔹
جزئیات مراسم تشییع و تدفین پیکر ایشان، متعاقبا اعلام می‌شود.…</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/463314" target="_blank">📅 05:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yo4ooykwyZQIVqNOd2CcCRrjz5hiCyPV52ujQbyaFs2OsA5Daho1XyYHKo8TYMtloy2Dy8_K9e5QSju4n66T0dXjo4w35lx_0yGw3VPsZRuFDP_XMwa52ZvNjRBXfb0g3V9qgluN3192YtairjBi0N5XWNgowXIWfPfJhl8ev7DubHFIsUzy5UUb437jGVZgT8l6GxQ8AgBiKTow5bmD_EJoSBI8buzwczFFwz208w3t68qXDnaE3mVK0Bx_gqk31lpHsBv9WOmIMeMokUrdpJHnN-aA8Q6X-Q2nWsNZY7BomF42xQbhxeq23xRVSQWzvptNaeHoiodlllml3xSQ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران طلسم ۱۶سالۀ فینال شنای آسیا را شکست
🔹
هومر عباسی در شنای پنجاه متر کرال پشت با ثبت رکورد ۲۵.۳۷ثانیه در رتبه ۹ قرار گرفت و به فینال صعود کرد.
🔸
امیر مطاعی نیز در مرحلۀ مقدماتی ۱۰۰ متر قورباغه مردان با ثبت زمان ۱ دقیقه و ۶۶ صدم‌ثانیه در جایگاه هشتم قرار گرفت و جواز حضور در فینال را به‌دست آورد.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/463312" target="_blank">📅 05:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463311">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حملۀ هوایی پاکستان به افغانستان
🔹
الجزیره: حملات هوایی جنگنده‌های پاکستانی به ولایت کونار در شرق افغانستان چند کشته و زخمی برجای گذاشت.
@Farsna</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/463311" target="_blank">📅 05:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463310">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtCYkxZidSayBI-AiGJQgJRJtAFgciGAUZXUXcbAbReL_nEpC4To1410pc6y4Rr5bOdGjjw85OgfIDBAyaPCYeuCtTcDKSjFP-9vUSH-5QYdu3CZWOBq8umfaq8ZYdlp523WHTOjtYBKtHckr-klrLcw1oqKTzPmUVa67wPJRgxkytvcZZaXoEUS0a7MDUynshRC9GEoB-FinsZd8Vf94DPTM7qdp4SoreliEIAMm0feCd7As-kJdue9bYUs8MixizNc3AotfiwvqAJ88rngpGEUewpuxnD_nbA1vvZge3yILIRg2l5VotQ8RchaU87yric7-9lupQ3aWBR99Rj_gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرهای خوبی که شاید امروز نشنیده باشید  آغاز پرداخت وام قرض‌الحسنه مسکن بهزیستی، و اختصاص ۱۵۰ میلیون کمک بلاعوض
🔸
سازمان بهزیستی کشور از اجرای بستۀ جدید حمایت مسکن مددجویان خبر داد که بر اساس آن خانوارهای واجد شرایط می‌توانند تا سقف ۴۰۰ میلیون تومان تسهیلات…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/463310" target="_blank">📅 05:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463309">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نفت برنت هفته را بالای ۱۰۴ دلار آغاز کرد
🔹
قیمت نفت در آغاز معاملات هفتۀ جدید میلادی صعودی شد و نفت برنت با رشد حدود ۸۰ سنتی به محدودۀ ۱۰۴.۷ دلار در هر بشکه رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/463309" target="_blank">📅 04:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463308">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287bdc0a73.mp4?token=nRC-G8dqdQ0cZJ8DJZ_69vSuaT1Gx8zyAsMcUiYA-k3BKsnMlJn_-Mzlg27T_BFtzJzWD5-k-OYt1uJHFFVEtstTPYo1HR3RjO9DKXd7CPao0h8ipz4yieEGX4hNuaLmaT_7UJw1ouD_ZEdwhadRY-D_RHYYtRL0uZW6IslQL_jcQvUE_pDiDPuUT8XGDyJ3TpQ3Q3rRj4PxELiVCB3rzdZagyedJ4RGqhtAHyrjjdBrQmQcXjxSUJcM-MR-h3OIA5lIbqcAzh2000d_xszEfr7SfQaq_oTHHAO4_KmYqIv2QSLQOFAB6C89qOwc8a1SvLmrQf2ZbFw7JQR5dkKHaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287bdc0a73.mp4?token=nRC-G8dqdQ0cZJ8DJZ_69vSuaT1Gx8zyAsMcUiYA-k3BKsnMlJn_-Mzlg27T_BFtzJzWD5-k-OYt1uJHFFVEtstTPYo1HR3RjO9DKXd7CPao0h8ipz4yieEGX4hNuaLmaT_7UJw1ouD_ZEdwhadRY-D_RHYYtRL0uZW6IslQL_jcQvUE_pDiDPuUT8XGDyJ3TpQ3Q3rRj4PxELiVCB3rzdZagyedJ4RGqhtAHyrjjdBrQmQcXjxSUJcM-MR-h3OIA5lIbqcAzh2000d_xszEfr7SfQaq_oTHHAO4_KmYqIv2QSLQOFAB6C89qOwc8a1SvLmrQf2ZbFw7JQR5dkKHaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسانه‌های عراقی از به هلاکت رسیدن تعدادی از عناصر داعش در منطقۀ دریاچۀ ثرثار، و کشف مقداری سلاح از یک قایق توسط نیروهای حشد شعبی خبر دادند.
🔹
تعدادی از عناصر باقی‌مانده نیز پس از تحمل تلفات، پا به فرار گذاشتند.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463308" target="_blank">📅 04:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463307">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/463307" target="_blank">📅 04:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463306">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57624d7066.mp4?token=DbvoCdIxmbeEH7ZIR5Z1W5EsVOMrcSWSG712BmMv2KpeagvNXpA8ZURNaJ8nsfeUUCo5NlgpH8hDqaMPRhgxVf4DyM1DA0pJuQVcd178eB6pxnc7mVnD9Y1YYyFRbL0oCfB05TuHmVoruJ8xKe0HaGKX5OU3oW7uAgOEtEUgPttMELVULclRRxlxg1pICpunA6-FDhvVYhQTVDXqM7dFr5yeh3WSn10cnsxHddi1oBrZarQ94Q6N93sKm2jon8vPBBNmr_pVp_rQd6larwhFW-q_DhJgZHF33dp5GZVFdAa4ljqS4dP_Q8kOYs-EQdyuvyk91V3PiVsxtqONwaEVCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57624d7066.mp4?token=DbvoCdIxmbeEH7ZIR5Z1W5EsVOMrcSWSG712BmMv2KpeagvNXpA8ZURNaJ8nsfeUUCo5NlgpH8hDqaMPRhgxVf4DyM1DA0pJuQVcd178eB6pxnc7mVnD9Y1YYyFRbL0oCfB05TuHmVoruJ8xKe0HaGKX5OU3oW7uAgOEtEUgPttMELVULclRRxlxg1pICpunA6-FDhvVYhQTVDXqM7dFr5yeh3WSn10cnsxHddi1oBrZarQ94Q6N93sKm2jon8vPBBNmr_pVp_rQd6larwhFW-q_DhJgZHF33dp5GZVFdAa4ljqS4dP_Q8kOYs-EQdyuvyk91V3PiVsxtqONwaEVCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امیرالمومنین(ع): اگر غصّهٔ گذشته را بخوری غافل از حال می‌شوی
🎙
حجت‌الاسلام رمضانی
#اندرز_مولا
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463306" target="_blank">📅 02:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463305">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">خانبان و لوسادا، ۲ دستیار جدید قلعه‌نویی در تیم ملی
🔹
پس از جدایی آندرانیک تیموریان و علی اصغر قربانعلی‌پور، به‌نظر می‌رسد نام ۲ دستیار جدید قلعه‌نویی قطعی شده است.
🔹
خانبان ۴۴ ساله که سابقه کار با کی‌روش و اسکوچیچ در تیم ملی را دارد؛ و لوسادای ۵۰ ساله که دارای مدرک پیشرفتۀ یوفا است، و از دانشگاه مادرید فارغ‌التحصیل شده؛ او در نساجی و پرسپولیس فعالیت کرده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463305" target="_blank">📅 02:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463303">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8838cd1132.mp4?token=KiPki1uRoZaCPySPd81Rs2a1PSgL5BaHTmvGAkmSi6CtNghU_wRICzWz-xAH3gsPSy8vQDyOMuLXbb5OobWoQkC59o1lOD4-898llFjbU4Z0p3TkN04nPINyAAD26QxknYOmAUa041NFXtkwAtIl0zUHKAfAbxU1fIBI9FdeJNlFDB_Ai3JKmHvgOR8a3hh00PoXoRxyTBq4acruzyEONiLDo9DzPAZbDBDn9iTTArWhEoMTmYwcyViBk-yk8MPsHZ9DCYca7gu3bsJ85A8FXhZ6ONLXDjeTOvb9YNw5FVEoM0J-dGaqV4ulVt0D09o8cISnbyjnp5p6ByOaTL4iaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8838cd1132.mp4?token=KiPki1uRoZaCPySPd81Rs2a1PSgL5BaHTmvGAkmSi6CtNghU_wRICzWz-xAH3gsPSy8vQDyOMuLXbb5OobWoQkC59o1lOD4-898llFjbU4Z0p3TkN04nPINyAAD26QxknYOmAUa041NFXtkwAtIl0zUHKAfAbxU1fIBI9FdeJNlFDB_Ai3JKmHvgOR8a3hh00PoXoRxyTBq4acruzyEONiLDo9DzPAZbDBDn9iTTArWhEoMTmYwcyViBk-yk8MPsHZ9DCYca7gu3bsJ85A8FXhZ6ONLXDjeTOvb9YNw5FVEoM0J-dGaqV4ulVt0D09o8cISnbyjnp5p6ByOaTL4iaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
منابع خبری از وقوع انفجار مهیب در یک انبار مهمات در استان حلب سوریه گزارش می‌دهند
.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/463303" target="_blank">📅 02:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463302">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBRvERaKTfbqj0V5omMio2mSRQPK6La0xBgZtiZYBIu8btp1aYaDVZ7F3E3PBNzHkKvleXfv6Nc-8Cgttuw1-iahzQgjr9N7uqPUL9YuW-4ltCHBYaScnQKct9nRsFbjbURMFqlIn5zAXGK5iH0w-q-d1MLltD_mtaK7C6isfBVqtAGdV_2chNRP2Uy1HRrSXtmqQq0U-kCqBI32W8jbQrsGPMyHZYEGIgYZoiUtcpO720d4oP5-A-lKdZ-1OpnGP20jUFdw8cq3VYn02sZTVc0W86yatO0cNcvsm0YILVK1oX0aR6mcAN5Rrxv94j-eXNwbSaG29sNOtYmLEaVCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقال سهمیۀ بنزین به کارت بانکی از مهر در ۵ استان اجرا می‌شود
🔹
سخنگوی کمیسیون انرژی مجلس: این طرح تاکنون ۲ مرتبه در چند جایگاه به اجرا درآمده و قرار است از ابتدای مهرماه، در پنج استان کشور به‌صورت آزمایشی آغاز شود.
🔹
طرح انتقال سهمیۀ بنزین به کارت بانکی به‌تدریج تا پایان سال در سراسر کشور اجرایی خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/463302" target="_blank">📅 01:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463299">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TWcnYKmxgcx-wcNE26rocWbU6bN23XZuhz2x3kFrkZ8Lw3xBz_xBl2_DRM0FOGNuVoz9Ufp3wlk_y14egJRdkt5hK08E-Qqq0-IAygZe8pPy0Mp_21_yr625KNkQlvd9KFw97_SGxQdefIx6KNnfDBNYimLwEVFjYJisL-uAUm69KIZtTblpDBwKw6bmXvZ_C8aH_DKZ16LkF9xz76n03SYPVzF7yBmD4qxwWpSKs6MPWVgWRcpMRSfljaXWdeOLqJUU4rxUgzPlDZSENDrK5cBppOay-Ic_epyGqxYlV_EdaxslLpKu9nbJoUx8g6iTP7EvVNjNJBbs353yXqnwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGCAsqU1ZC9QBZMzmTPv7Hmb_6guM1kXsfP8BcbuUOpIOmURiQPzt3p7EcI2UXsJmlct9IH8cNty905VmQynP3eFn5Mc-VNWNffAqFE7AJxvbiwUIDQXHsPgN3XCjWbJLo4tF_GBXXgPgaKqAMYW6mrZWnQe-bBfVR2R7dXoqmw1Ojp4YRI66J8jQtjFXA5pkjAwkCQKcbMwpXjy8Zqx_922nPICdgd5BHB2lc_w3XG2Bh4SSizawnS-urCLDqHfc99irCFwiy7psF6YveMkj22DHQjoj9idSxmkREXbhB4xvGewa7K4vVegbjsGunK6hQrB3ANQEg8PIPI-B6LLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gKljkSTS6PkEkqmCvnE29ymWhIx3LuJckmi7eBeH-0Ne7YsDmrzSGqEldip9NXrxoSAr6jcVykagqEU0XAwbg3-Vpxq5QUiIYyPAHh_fy6HHNoi0uAgYPywf7KMqmS-y1oY6uV0TV7F-SuB0zfT0Spt_w4G8pfYHzwB31CRfihpP_Vtp4v5da4Ieo8yBLCFlZYCX1_JOMOiWIMFNg8ZOZNPYcXfvx8XJ4KdYAHdTZc8kd1Kwygeb2ommCUc-fYaCGIH1dVi5kKhPLpGOa35uTDW3395nxdMUwCqc1zyGnGdSzSEDdsTtwJ2d8H-FUU73JnTmsH5hFHAaWhNxgxmXQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتایج اولیۀ انتخابات پارلمانی روسیه؛ حزب «روسیۀ متحد» پیشتاز است
🔹
بر اساس نتایج اولیۀ اعلام‌شده از سوی کمیسیون مرکزی انتخابات روسیه، حزب حاکم «روسیۀ متحد» با کسب ۵۷.۲۶ درصد آرا پیشتاز انتخابات پارلمانی این کشور است و پس از آن حزب کمونیست با ۱۳.۸۴ درصد در جایگاه دوم قرار دارد.
@FarsNewsInt
-
link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/463299" target="_blank">📅 01:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463298">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4cH-yfbbIf-raQqb70N8DyKSLlXPX00O2plZqGxofsKE9bjHx19KMD0Y20FO1UiQmo-HpKHgCjH-gxfYzRnuW3Pqo8-wSCR4a11-Fi37p1DnNb6C5cCKvgfBR40F6YePJd-PNmtKfuLT-g3t2zG1tIKUMv51ClFpZ1StPuGbCUpbWhbORGcN9qeyWhqoOI1Rpne-OlMBBud3cZbcYNT1HNOJjvOxIkoFk4tp8FbOYrrskzpRgQ11VXcNdegasOicsfELIfkLpPfNGAVb8wJ3kA0RIF_k1bTV2yKwcQP-f3z10MfyqpBLemX5ek5fvLQnkVA_MxQCMYJCUlFx_tFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات هوایی عربستان به استان الجوف یمن با ۷ شهید و زخمی
🔹
رسانه‌های یمنی از حملات هوایی عربستان سعودی به مناطقی در استان الجوف در شمال شرق یمن خبر دادند که در پی آن دست‌کم ۷ نفر شهید یا زخمی شده‌اند.
🔹
به گفتۀ سخنگوی نیروهای مسلح یمن، جنگنده‌های متجاوز سعودی از زمان آغاز تشدید تنش ۷۶۰ حملۀ هوایی علیه یمن و مردم این کشور انجام داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/463298" target="_blank">📅 01:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463292">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rwfq00TBKXANVSMyp2JqhIS-sZMugy2HKi7MLhS8j0jOVdjbtqpzM7bTvoSrGNuv5f76_muTk3kVebNHUt6EriBLlZ5DRmTjwnwTOge_79AxRfYnFmXhq6qUnj5CJ9md3i1WyzutYRnQFtKYN0C4K_S8hH8ixh9cUosnpOdkg0kYRKn0ZQ1wMY8Alcdl2uz7zXEGHVDcJEcCAi9N1oE-wP9R0GlksaFeUN9OnnCaSyiduHkcNbgoj2dDy7GDaYwOM8uADaeRtnBgKLE9s-VkOzGC5yf2PIkidDmu6cYA8SWwOrL4pvLoYEJZiZemkt7O9l7kA4Bg01QnGN6p50gcTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fViNsiDqa7pfkcSMlu5f72kzZK40K37BqXBJBgaT0911VFW4wb6aheO4_hbNw8cEamurfI52KJrEDnpCB3rH2cpRuuszJhXl4h5vs1YC4Fhg-sDt9emioV14Vn8f4Txjax0-aeTK1yARHh0MzhyG_hjBhc7clMkFbD0g49PT3Y3qOY4SgHVJrrUraueKaoolopi7GZY6Mi9l9Ky_vEzqThRldp3dCAOQmJU4lYsRcxgzUC-LdwTB644f_eVc4EiRu-VxIz95O7LWib20TPC-rytznYjtj5d5hL-3w7ydoAMjdgGQrXp-WPQazi57gr_n8YZXRC50Uy0nf7jMoFDEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXo8VIWxh_rufnURtaFCjoKKbirEJNYJuCVoMZMWH-x9bFvVFJBKxVn3QrXlhJ2qa_04zAtdiPlh8d9lU1kkMSQ5zA8AZ_iAwvLgUmRpsnJ8C_ljb32hbhpe9t4XEo2SjmlNBG5DWp3rkVZ2C2mISSP6Hlfl9ljp_HyB2raH8YxFtpTqnNu54E8C17dUMzOqeCmGSXa-qUgU1qGE4XMmzf4czZcqYUCPiYeeYS7jyIXlqMqPZeYrVqASIOct0Jiq8VJOHoJFiIUed7IOZIuOnMi2NYLeyaaN9ozoI6EnpY2UEe05FwzmD08nOIbWc2HpRDjTrTcBIuTYHo0GObYKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNe5dFLoNQHLPRXsulMM-A0sFymiq5nZHueRbb6pp2WH6eWG0cja4cYrWi4yXXEWXjTCpGYtJuRE9Zb7gR0sAFmnDGBKg12J9lhsUsqRUunEi1Eq2siWyBwXSvVd-zNnd3Yhh4Wq7ZHNYwo-u0aIpZhO0EyxqPybCcemO4GqDOGi0MKiMzMrVtC17iBsLXl7ZerAe_Dmou-k5ccwl6vXOfIKXQ3C9NDkpteU1KWUQw4jUGv1SUcOKxy5BGGUmbajQP5vEUtqmrp0jzO4m8BMUIled2FvdF-b0NHucnGkJuk9GXB95ZBQESyiXcnYLPqyJJomAs6fNmZizC37riaWNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeV4HnfYa4On1dstWhG4zkjhhHXkQCEhDQdWyhW1UcUYKn8MmdNCgWxVqjuSJ9uxbwxWZIdqHq4MIkSr0qlslrSyPDvO4U7pXT6glPtsY7T69dxqogTsJG5rTGjTHEtvER7JHg-SE9vnkBfP6dY_Meo_9qSohaU-DA6XrsoiM1H7HgR41mNhA7zoCCESqjWPkItKvGdUjElQ31AnxnxwOqPJix8VojtwXsXqvOTRDTZ2XzPFnF8wvpv6w6w_hkIL1gxlk3X1vZHJEQ-uAuZ0yQ5sIvMnS8yXBYdyHt8rYIhwEjVS3D_I4Xr2jFQfxbzy50y_Ha0ugHktDXVPzZOEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IxYlwmNSIUxVhJESlj_eXsMqxoztVBcdbmGaRPLDPh6kJoiNnosgbqvyD1dhSy7OwlbBepth8n4BqbWmLr3iS2KZ-U9qjMLITDaUT45lV6m18r10GNEeu9fOuusBJIhT_4bjaAEdFMbImvGfDyjr_1zcja1phoS7JP7aZum4NsoxgVzbxCa9Vb4ojk2755AjEYSOssRADjfhrQuGOBZ4D1dOFKsEahQgPZ4F0BFcXwNewuOavCsxbifUO6wOsu1r1l-mMFUMFz-rO5e6-S-2VdmhiGDyCQlOmOGzgjteqEp1e8MZcoBt9rP9-3I5-NfzItM0QViNcV4G7lsN5akiOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارتش ایران پهپاد اوربیتر دشمن را بر فراز تنگۀ هرمز منهدم کرد
🔹
روابط‌عمومی ارتش: ساعت ۱۸:۳۰ امروز، یک فروند پهپاد شناسایی پیشرفتهٔ اوربیتر با آتش سامانه‌های بومی نیروی پدافند هوایی ارتش بر فراز تنگهٔ هرمز هدف اصابت قرار گرفت و منهدم شد. @Farsna</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farsna/463292" target="_blank">📅 01:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463291">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y80Qvh-zAwSd5FAFDxWPfCgHUsKFCZNphISJ-QRPPSzSUm7N-IYJMu2sfq29lZMBE21xaNl01_K8e58BPeypHFb2Hsq3VoIMWvH64MwLsA3BGcUbSLXpfRuXiRHxEHPs77REdFCXk8h23cqZsPRgRvNoeHVtllLIIbIezuRHTcNkPFRD3AnwDxppXb6Yj18KFWA-EiAUpvNJgbS_dReze7vI-6MWfHhMtGDBj6IEt_7l_jwUPu4x_aTA4TvBRgJCfYz0KS3yJrH6ldzFscDfBwREhACD3JQdkfLeRm1I5ksAt5zjTuCmMVJKWzrrtnebiGqCMCo3J7jDlp4PVSNodw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله سیدموسی شبیری زنجانی به‌دلیل عارضۀ خونریزی معده در بخش مراقبت‌های ویژۀ بیمارستان بستری شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/463291" target="_blank">📅 00:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463290">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FB9Ujzatf_IjMcT-g0ZaI9d5Ce1r8hOQKKodJMUu3Lz1Clcj6gT_Y4rF_6QB0f14Oh7W8vJZRVrAopDSkQRzleE00m63Se5QlH9kqAixRJWCZcvKv1bTA3vQuXDwfO19oC0Juu5WIh1UqMaStcsEONBkyXRd9lQ8NPbJLpqIs0U7F94_1TH1GiAPvYjrkGiSfqFCwi9761eQrhC6Uvp7DD4Ba9qWTvY63GetjgaTHg0eWqopX1BU2xFsNgv6mI9zw-Daw5VvhaSeyUy7Zr96Opc_dqAU4vB_AQ2-1xIJe0NAiqo6oNCBRZo8hVODCW9H26OVsF9jwLLeFt9WmAgsnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای شایعهٔ حکم اعدام یک متهم در مشهد چیست؟
🔹
رسانه‌های ضد انقلاب با انتشار یک فایل صوتی منتسب به فردی به نام نجمه امینی مدعی شدند این صوت از داخل زندان مشهد از سوی این متهم منتشر شده و در این صوت، فرد مدعی است برای او حکم اعدام صادر شده است.
🔹
پیگیری‌های خبرنگار فارس از منابع آگاه حاکی است فردی به نام نجمه امینی به اتهام توهین به مقدسات و سب النبی در فضای مجازی و فعالیت علیه امنیت ملی در ایام اغتشاشات دی‌ماه مشهد بازداشت و به زندان مشهد منتقل شده است.
🔹
این منبع آگاه در پاسخ به سوالی درخصوص صحت ادعای صدور حکم اعدام برای این فرد تصریح کرد: هنوز هیچ حکم قطعی برای این متهم صادر نشده و هنوز دیوان درباره این پرونده اعلام نظر نکرده است. او هدف از انتشار این محتوا را تهییج دانشجویان در آستانه شروع سال تحصیلی جدید عنوان کرد.
🔹
این منبع آگاه دربارهٔ اصالت صوت منتشر شده نیز گفت:‌ هنوز اصالت صوت منتشر شده از سوی نهادهای ذی‌ربط تأیید نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farsna/463290" target="_blank">📅 00:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463289">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">توقف پروازهای ایران و عراق تکذیب شد
🔹
ساعاتی پیش خبری در فضای مجازی منتشر شد که دولت عراق تصمیم گرفته تمامی پروازهای ایران و عراق را از سه‌شنبۀ آینده متوقف کند.
🔸
حالا سخنگوی سازمان هواپیمایی کشور ضمن تکذیب این خبر گفت منابع داخلی و عراقی این موضوع را به‌طور کامل رد کرده، و پروازها میان دو کشور همسایه،‌ همچون گذشته برقرار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/463289" target="_blank">📅 00:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463288">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep6IEq6bGkNHmUma4kFUOxJfsCpJOYNOLJhfxADD7MQUhg-KkfNmbdGR2hVKhM-v6blzI6ApedF_qDpZWnImj6DOtpa6E5y4o8TqpeTwZdzZDsDqpjNVqQVi4chqNbREIR7dTZdr-DhODkud6AQ-tWygV_J9IkV0TclTOjLbfOdx7-mv773_j27cBcLHwMp0smI7NAE_352aZ2-M4OOC_4Kj0DYcZy6Egx8eUIS57ZtFZSsKKayaO0X4nl0_11hiNWThpUzPJ0XHy31AxZpcwmKn-vLx4QxrH0j8s0zn_f92ZmrRusq0g_jeXqDa3pvvtgDdT7OwRixSANFLOAmRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود دادستانی به حواشی آراز کاپ نوشهر
🔹
دادستان عمومی نوشهر: پس از اطلاع ضابطان قضایی از بروز برخی رفتارهای خارج از شئونات اخلاقی و شرعی در ساحل مجاور ساختمان هتل بین المللی آراز نوشهر، موضوع با قید فوریت مورد بررسی قرار گرفت.
🔹
با اخذ اظهارات شاهدان و بازبینی چندین ساعت از تصاویر دوربین‌های مداربسته مجموعه هتل آراز، مشخص شد این اتفاق پس از پایان مسابقات در رشته‌های بسکتبال سه‌نفره و تنیس ساحلی و در ساحل مجاور این مجموعه رخ داده است.
🔹
بررسی‌های اولیه نشان می‌دهد نحوه نظارت و هماهنگی دستگاه‌های مسئول و برگزارکنندگان مسابقات نیازمند بررسی دقیق است.
🔹
در صورت احراز قصور یا تخلف، با افراد حقیقی و حقوقی مسئول مطابق موازین قانونی برخورد خواهد شد و در اجرای قانون اغماضی صورت نمی‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farsna/463288" target="_blank">📅 23:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463287">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkQLtNBkY9n8ePu_vJdlQKWeVCGcqqBefOF4MnMJCyfPokperWhS3Oqj_GReESScQUIhaXhFflpxwqbcfFQXLxMPBDl5sb7Xhnl3V6hUxyb9ICv04jX0XD688n-4z5cHJP4i1NMY84bNGOsy49-JTdu-JJ90Kla4_iynkQTdcT9A9gDJzxeTe1soRri-12xnslwZjwq1r6442ResqawJFYj4RWBZa_qV6IzaG3WmoFFma4Mq_UQiIY697TfVeSPcg6amzINW2OpxbuPzGDckf4GnOy4tw0p2STZcYo4kYYEtO1WIzbAx0p7-LQHirfPxkqcPz6jLj6iZ5R3rRVVpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبل از فروش لپ‌تاپ، این چند قدم را فراموش نکنید
🔹
انگجت: لپ‌تاپ قدیمی فقط یک وسیله الکترونیکی بلااستفاده نیست؛ ممکن است هنوز حجم زیادی از اطلاعات شخصی، حساب‌های کاربری و فایل‌های خصوصی صاحب قبلی را در خود نگه داشته باشد.
🔹
به همین دلیل، فروش، اهدا یا بازیافت آن بدون پاک‌سازی کامل می‌تواند اطلاعات کاربر را در اختیار فرد دیگری قرار دهد.
🔹
اگر لپ‌تاپ همچنان قابل استفاده است، فروش یا واگذاری آن به فرد دیگر یکی از گزینه‌هاست و در صورت خرابی یا فرسودگی نیز باید برای بازیافت ایمن تحویل مراکز مربوط شود.
🔹
اما پیش از هر تصمیمی، نخستین مرحله تهیه نسخه پشتیبان از اطلاعات است. در رایانه‌های ویندوزی می‌توان از ابزار «ویندوز بک‌آپ» برای پشتیبان‌گیری استفاده کرد و در کنار آن، فایل‌های مهم را روی یک حافظه خارجی مانند هارد یا حافظه اس‌اس‌دی قابل حمل ذخیره کرد.
🔗
اما قبل از اینکه لپ‌تاپ قدیمی‌تان را بفروشید، آیا مطمئنید هیچ اطلاعاتی از شما روی آن باقی نمی‌ماند؟
راه درست پاک‌سازی لپ‌تاپ را در
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/463287" target="_blank">📅 23:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463286">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6XR5ylsNf4sb45iPx4CgWJLz2yImq8hxL5eQ1fMXVJP-nPllyvKbbMR7ftodox7qfvTT8KjCs9Ca2kjfxEJDEC7RY2Yr-eocwEVdt4WqTWhO4WwdLfgib0myHynkFX4h3eZQP4gYizkotWrkUcwI-yaNMk0groG2Af5kRBLv2LButfV2Lsw-saQnlErKMVxeWpwe6_7g4LBfQQ6MlmU0exwz5JezJX5Oxg59HUGa6nTmnDTuJc5IExHQHN5a9kTWskG0L4FmQgoQOT1h1lZ4n7FbgExNNTuVBcvk-gR6ZuP2tfv2ZlOz1Tru5tSUHNkNOGNEfwfcit_TcctTpQX0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن به نابودی اقتصاد عربستان تهدید کرد
🔹
وزیر دفاع و رئیس ستاد مشترک ارتش یمن در بیانیه‌ای مشترک نوشتند: حکومت عربستان سعودی و مزدورانش باید از این شکست‌ها درس بگیرند.
🔹
هرگونه حماقتی که مرتکب شوید، هزینه‌ای گزاف برایتان خواهد داشت.
🔹
موشک‌ها و پهپادهای ما می‌تواند به عمق خاک عربستان ضربه بزند، اقتصاد این کشور را نابود ‌کند و به هر مکانی که در آن مسئولان سعودی پناه گرفته‌ باشند برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/463286" target="_blank">📅 23:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463285">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ecdb9dd0d.mp4?token=tw0PPQtZo7RN2DX7WEi-It4wgvFNj2m6W8JstEt9NVUg5ZS1VuOF7KiLb0QjyirCR63fmddH0XBgOV3PuIDRGUF1DzYi94oDSxT39bcJ6fadtWH3FD0QLUET4rtHXJGfJpdsQsivhCV0A7CCLrkIU9zFKbouVeT9DlBBfmcDPEhUL6Z76sYfdsUnz8zWBdtFXyuiomU8r1f2Is4wIcYDGIusPiDYljmU7GCfq5S9fG7DTWck0_jbgOd9Llzh6O8AG-jm0SfevikWBETYpz5MXMUmWLO8dYPj0DP1nWwaiLprBZw6kTKndRSZUedA9yzXVPVEDvUDmlj4RUZHk6Kykg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ecdb9dd0d.mp4?token=tw0PPQtZo7RN2DX7WEi-It4wgvFNj2m6W8JstEt9NVUg5ZS1VuOF7KiLb0QjyirCR63fmddH0XBgOV3PuIDRGUF1DzYi94oDSxT39bcJ6fadtWH3FD0QLUET4rtHXJGfJpdsQsivhCV0A7CCLrkIU9zFKbouVeT9DlBBfmcDPEhUL6Z76sYfdsUnz8zWBdtFXyuiomU8r1f2Is4wIcYDGIusPiDYljmU7GCfq5S9fG7DTWck0_jbgOd9Llzh6O8AG-jm0SfevikWBETYpz5MXMUmWLO8dYPj0DP1nWwaiLprBZw6kTKndRSZUedA9yzXVPVEDvUDmlj4RUZHk6Kykg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۲۰۴ حماسهٔ خیابان بروجردی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463285" target="_blank">📅 23:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463284">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXCsDAaXcu1M2ney__J9lPYm0L_maVYba8LTNfpTJF-eBjUSr7H0IwFswIEm_gmB0ek-Ujk-AFXGpozNe4zC0SkTj1HmRW3jaI1DMQQLZeeI1vmHvLBZ3GVmdd_1vS_-jBp1MSWzaL-Zz4gUT7NBzB9PgnpNKsvDgqPKVww42PbbYhIzaVEPHup3IbTujXvbgkP0sPE3pIXmRceqzfEuDgPQT4U5YvtLph1-VYDPpo1GaRx4WY8ROHiBWvbhqIAG3SQzF1UcARLtmI-Gw49Pz8wT02Z5mp-6bFlbEug4ig1g1nYBGgTqG7x5PzpHf7dGZnnvFGH4M62__0VmQTvNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مغز ما چگونه تمیز می‌شود؟
🔹
شاید تصور کنیم تمیزکاری فقط مربوط به خانه، لباس یا وسایلی است که در طول روز استفاده می‌کنیم اما مغز ما هم به نوعی نیاز به پاک‌سازی دارد.
🔹
در طول روز فعالیت سلول‌های مغزی باعث تولید مواد زائدی می‌شود که باید از محیط مغز خارج شوند. بخش مهمی از این فرایند پاکسازی در زمان خواب، به‌ویژه در خواب عمیق، انجام می‌شود.
🔹
پروفسور ندرگارد کشف کرد که یک سری سلول به اسم گلیا در مغز وجود دارد که کار پاکسازی و تمیزکاری را در مغز انجام می‌دهند دقیقا شبیه کاری که سیستم لنف در بقیه قسمت‌های بدن انجام می‌دهد.
🔹
او اسم این سیستم تمیزکاری را گلیمفاتیک گذاشت بر وزن لنفاتیک. این کشف باعث شد به یافته‌های بسیار مهمی در مورد آلزایمر دست پیدا شود.
🔗
مغز دقیقاً چه زمانی و چگونه خودش را تمیز می‌کند؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/463284" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463283">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11908925a5.mp4?token=g3o5VzL26IqRLfFcyYyGnCSmWuRIYH_yJcdVwQTkpHhExzAWRINwo1Nx63QZe0Uz0ehnER1dhpgyX0i9Pl8RECL3O3FM6YTRkR6LXQP3vPuSCGkhEd15bmh1O05Qg-En7N3sQwTg78GJtx7XkZ7UacvbuRUYE5yfyquM9Zzs07N8CGUKh6uI1pWMkt6HWtbi0hjd9my7VlHFDHJTKw0W55ODQ8Wb8O8BYr64_-BsgTzq4ub6IvHEf6Y69hsG6klVfhYUz9Xi0xvXH085qZ0UznzuTHdl0hE2Kqi3g3qXUgzSjsEFrivOFLEyUj5fBizOR2d6RjXPb6I_YBVOX1xuB3I1Et4g_1FnD5IWZPp-vCCBO7q01qZO3xqYzMc66tMXzfWB_OYcXsBuHq9x4aHMF-o6f2FtQJUG6xJwJkF5mPtxy78oIELd_ZhmAD8-W9GNl7B9LUrw8Kmst_Ct98iIt4ageACcjOaSP5vWzHbRoIGICCd5siFe-79wMgiBVNxD4PP5YiPudlSokBktpbAPprH-DoZR29HVPmYOVsGVFf05yLt6MdS-iKqkyZIZ-DpL8d9rQ44Wj6OprPYHpEUyncudtqPPCRsk7fsTynFSlXVLvX9uI0gJ-VxG7Ha8WGxIw5uzif3x38VOSJh-uHpqVwPTaa-w64SIRiHhk0hxqH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11908925a5.mp4?token=g3o5VzL26IqRLfFcyYyGnCSmWuRIYH_yJcdVwQTkpHhExzAWRINwo1Nx63QZe0Uz0ehnER1dhpgyX0i9Pl8RECL3O3FM6YTRkR6LXQP3vPuSCGkhEd15bmh1O05Qg-En7N3sQwTg78GJtx7XkZ7UacvbuRUYE5yfyquM9Zzs07N8CGUKh6uI1pWMkt6HWtbi0hjd9my7VlHFDHJTKw0W55ODQ8Wb8O8BYr64_-BsgTzq4ub6IvHEf6Y69hsG6klVfhYUz9Xi0xvXH085qZ0UznzuTHdl0hE2Kqi3g3qXUgzSjsEFrivOFLEyUj5fBizOR2d6RjXPb6I_YBVOX1xuB3I1Et4g_1FnD5IWZPp-vCCBO7q01qZO3xqYzMc66tMXzfWB_OYcXsBuHq9x4aHMF-o6f2FtQJUG6xJwJkF5mPtxy78oIELd_ZhmAD8-W9GNl7B9LUrw8Kmst_Ct98iIt4ageACcjOaSP5vWzHbRoIGICCd5siFe-79wMgiBVNxD4PP5YiPudlSokBktpbAPprH-DoZR29HVPmYOVsGVFf05yLt6MdS-iKqkyZIZ-DpL8d9rQ44Wj6OprPYHpEUyncudtqPPCRsk7fsTynFSlXVLvX9uI0gJ-VxG7Ha8WGxIw5uzif3x38VOSJh-uHpqVwPTaa-w64SIRiHhk0hxqH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۲۰۴ مردم کرمان برای دفاع از وطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/463283" target="_blank">📅 23:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463282">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23196aff17.mp4?token=m-Fj9IOz87zrXw5ySkv3A1S5VWU50KWZLodo7qXzloznbMvZFOgLReVJzIYx3C4TyGNHg6gbPt6xHLgbMHZ0qq61TzUxyQl8-HCB32118n4CZS-fiKSjOwKGk3VKzCF6A_MPXI4dA38mkLL_0qmZCYu6eQa9D8eX-Y45pfYcY9Jobj7voKoqnJFWNfpTPGld-rRoImC33FZ7_t_4ST8Df00CbchWx5QxzXZ1sstcva_JiXTi4pgrNBScf6cchEXM9x4G91DudzzV6-qbxYCDzvZLvmf8zoOyQMCYndF6BHV8NQ26Q7sTupN6DRZXESBUpIsTl6iwnI3xedmZYjLKBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23196aff17.mp4?token=m-Fj9IOz87zrXw5ySkv3A1S5VWU50KWZLodo7qXzloznbMvZFOgLReVJzIYx3C4TyGNHg6gbPt6xHLgbMHZ0qq61TzUxyQl8-HCB32118n4CZS-fiKSjOwKGk3VKzCF6A_MPXI4dA38mkLL_0qmZCYu6eQa9D8eX-Y45pfYcY9Jobj7voKoqnJFWNfpTPGld-rRoImC33FZ7_t_4ST8Df00CbchWx5QxzXZ1sstcva_JiXTi4pgrNBScf6cchEXM9x4G91DudzzV6-qbxYCDzvZLvmf8zoOyQMCYndF6BHV8NQ26Q7sTupN6DRZXESBUpIsTl6iwnI3xedmZYjLKBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همدانی‌ها در شب ۲۰۴ همچنان پای قرار ایستادند
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/463282" target="_blank">📅 22:51 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463281">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8bfd542c.mp4?token=s79fI_YMltCIyM-DNqUUsToh_UtJWw3bAyk4OsPynqlWzJaFUnRGxCjInjCsimUkIisiUziqWFVmKPS4L9pBbVi22iD78GyxoM4u90cosrxS1iMx-pyCrsn3ewymM9vcoKXstYOeVufMdgu3bczSBBeO-qzmFjPcdbNM2Lc23TTY6oTE5ouaWYK6_PLjNcEI5PhFIOSQo9WqDcMA7X_nnfFF7dKfWqVzibp9MPjArOpial959uoOADKfVcvSnT7T9ZwYZ0dgqNLY6S2DEReSe0l63noZZv5uZYzD9-EoDj1vAY6w9pw8pkq8x0fnxwsaj_een6ReVS4M3HnXAwgIZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8bfd542c.mp4?token=s79fI_YMltCIyM-DNqUUsToh_UtJWw3bAyk4OsPynqlWzJaFUnRGxCjInjCsimUkIisiUziqWFVmKPS4L9pBbVi22iD78GyxoM4u90cosrxS1iMx-pyCrsn3ewymM9vcoKXstYOeVufMdgu3bczSBBeO-qzmFjPcdbNM2Lc23TTY6oTE5ouaWYK6_PLjNcEI5PhFIOSQo9WqDcMA7X_nnfFF7dKfWqVzibp9MPjArOpial959uoOADKfVcvSnT7T9ZwYZ0dgqNLY6S2DEReSe0l63noZZv5uZYzD9-EoDj1vAY6w9pw8pkq8x0fnxwsaj_een6ReVS4M3HnXAwgIZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله عاملی: همهٔ محاسبات می‌گفت شکست قطعی است، اما تاریخ نشان داده وقتی خدا با کسی باشد، معادلات تغییر می‌کند
🔹
روایتی از روزهای پیروزی انقلاب اسلامی؛ «همه چیز با ما بود، فقط خدا با خمینی بود»
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/463281" target="_blank">📅 22:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463280">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f823bb53f.mp4?token=UIuGC28rNlelG0JtA3s8mbgot9fQ0KHAwsQAa4VZOrl9GiBqxQDqC7MLRYuDKkyhCj6gmAOOqcUbguDnhb2Dx-GRDr0m2N9xKIQoBT_6LWpLLhZ_pFf55_7Ha-OoFY1LSWozfYR_zRRRUq-izNddI6PC_uYuZmT2Vgil-P2X32Ix8_5aksKVzb-nGkmzD-EKj3Z5-W9b4j0FwyoTClmtNYgvL9qt8PRzT7gVR6ObzC1b1CITr9eoHr1P6fzXwGzryVrD9OnZFg_5fQSRo4glYCRsqFD3mHQow8qflekCpNJ70qdacpcGSWf8d5ilWL0Fsxr_Py_4giYRhbcfkBW_5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f823bb53f.mp4?token=UIuGC28rNlelG0JtA3s8mbgot9fQ0KHAwsQAa4VZOrl9GiBqxQDqC7MLRYuDKkyhCj6gmAOOqcUbguDnhb2Dx-GRDr0m2N9xKIQoBT_6LWpLLhZ_pFf55_7Ha-OoFY1LSWozfYR_zRRRUq-izNddI6PC_uYuZmT2Vgil-P2X32Ix8_5aksKVzb-nGkmzD-EKj3Z5-W9b4j0FwyoTClmtNYgvL9qt8PRzT7gVR6ObzC1b1CITr9eoHr1P6fzXwGzryVrD9OnZFg_5fQSRo4glYCRsqFD3mHQow8qflekCpNJ70qdacpcGSWf8d5ilWL0Fsxr_Py_4giYRhbcfkBW_5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: قطعاً مدارس حضوری خواهد بود
🔹
ما تمام برنامه‌ریزی‌های لازم را برای حضوری‌شدن کامل مدارس انجام داده‌ایم.
🔹
اگر اتفاقی در نقاطی از کشور رخ بدهد، اختیاراتی به استانداران می‌دهیم و استانداران متناسب با آن شرایط، به‌صورت نقطه‌ای تصمیم‌گیری می‌کنند.…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/463280" target="_blank">📅 22:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463279">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYh4c63TzIMs5T8wKJRNkkjb9DCAY-q-rEWKTi6gm_kRfpOZbcZOf5nu_OaRBMLA3-RFmfNrDmUEdpX1V0kyJc00Bk8gB5Wgf7gX_X2oeqXSk2kMSxLqE5f_w-a4am0VbHznUr455EieE3nM6npEcHWOmho3QWZx7RsD4sjU2rjiVCQlTM-WZwzF33GtQXqizcID1Pvrc5ILaDqy8gvFOyXmrfUqIH8jxBBEMOn7El8ReQBrLQJEhoQGE0rFo3gVbhe3Uu62ouyN139931n3KIG4f6oYiuf2T2YEJc6MH6ez7-VSw6dZOJaLUYowOjBtRbO6CkVncwJVyKj2MFmwSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشاورزی به ازبکستان رفت
🔹
نوری، وزیر کشاورزی در راس هیئتی از تجار و بازرگانان با هدف افزایش روابط اقتصادی به تاشکند سفر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/463279" target="_blank">📅 22:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463278">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e283b14cd.mp4?token=abyfcxUljSXgbibntyjIZCf72iieixdvSx8FmtOSPKbl84ySmzQ2GKPJ7gmlAfmMr9o1jwF-s_VK9MpsXSb8zjP8dFEySMZ9SAb7F6W-xm-dV6fl6iou5YKImz001P4iRbhM63VWvbz31P3oIOBsRvpuW_RS-RsbmJNPZTtMF7ZIUcSNrRzFeTyb1j5_297Tj74P9iXKYs1LnKItrWBaPyqDf9pdn0jpLWdltUCyZdWPrv4vZy2fXe0gwm_FKaelt3jBNPTG8MZmSJs7W2rL5ymrTLKI8kKmCEqKShV26g42x_db0tqaxFYPEVvUozwrVp6G1zhZKUF7pKKqe_QUxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e283b14cd.mp4?token=abyfcxUljSXgbibntyjIZCf72iieixdvSx8FmtOSPKbl84ySmzQ2GKPJ7gmlAfmMr9o1jwF-s_VK9MpsXSb8zjP8dFEySMZ9SAb7F6W-xm-dV6fl6iou5YKImz001P4iRbhM63VWvbz31P3oIOBsRvpuW_RS-RsbmJNPZTtMF7ZIUcSNrRzFeTyb1j5_297Tj74P9iXKYs1LnKItrWBaPyqDf9pdn0jpLWdltUCyZdWPrv4vZy2fXe0gwm_FKaelt3jBNPTG8MZmSJs7W2rL5ymrTLKI8kKmCEqKShV26g42x_db0tqaxFYPEVvUozwrVp6G1zhZKUF7pKKqe_QUxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احساسی شدن شرکت‌کنندهٔ برنامهٔ سرآشپز شبکه ۳ به یاد مادرش
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/463278" target="_blank">📅 22:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463277">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b95879771.mp4?token=cVPSka-g2MGpVIRgf36ulKgKKq2LO4jF_fCcs0GGgxAB1ivSVOn2HD2DbQ1GoZfLIwTB1yha2py_7NU1PeXx22bcDw_Vrl1AfnnkVhoEmdol_yJsQCPxmTKC8cEp2k9DvIODHP94wlCFH4tJ00msNPlKAOwS8VZNINsiIGnHJU5wZNg6Cc4ILZGVaYKS2SQsJudCIsEUtlZ07jXGRmLl09dStk2SBz4EtgspMEpFdiKqxTRzcHWt6OujNSa_GEqFUrgg8yTDa_HrD-T2LJCCk-vUjB5A6ugf6nsgI28FjnSEBWHAqPBCtL8j5Ts3vSY0MYw5SA4BMJog4_QKt4rDlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b95879771.mp4?token=cVPSka-g2MGpVIRgf36ulKgKKq2LO4jF_fCcs0GGgxAB1ivSVOn2HD2DbQ1GoZfLIwTB1yha2py_7NU1PeXx22bcDw_Vrl1AfnnkVhoEmdol_yJsQCPxmTKC8cEp2k9DvIODHP94wlCFH4tJ00msNPlKAOwS8VZNINsiIGnHJU5wZNg6Cc4ILZGVaYKS2SQsJudCIsEUtlZ07jXGRmLl09dStk2SBz4EtgspMEpFdiKqxTRzcHWt6OujNSa_GEqFUrgg8yTDa_HrD-T2LJCCk-vUjB5A6ugf6nsgI28FjnSEBWHAqPBCtL8j5Ts3vSY0MYw5SA4BMJog4_QKt4rDlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: قطعاً مدارس حضوری خواهد بود
🔹
ما تمام برنامه‌ریزی‌های لازم را برای حضوری‌شدن کامل مدارس انجام داده‌ایم.
🔹
اگر اتفاقی در نقاطی از کشور رخ بدهد، اختیاراتی به استانداران می‌دهیم و استانداران متناسب با آن شرایط، به‌صورت نقطه‌ای تصمیم‌گیری می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463277" target="_blank">📅 22:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463276">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60af7456ed.mp4?token=c7un2vRaswGH0JKKhqhrHJe20N4LVDWEdmOQJq0xAl8Pm07BtpNPOnm3UZjJtJpCAFr-5MOiGYXkzcFpu5XPEsBzYLUdPGhpYkIaj4T9NyrIJXHset8LExmP7V7EOwM5xOkItVd7XEcQbEZQZy4lRCabdQnT9HCy0SybOD08CWvVvAozBB_yWs7i4TVKXLsFiXieTqup43tl9qbM3Uqazz-HYosj46MI6UD9zGnvYWiWdbT-n1PtqQ8Q_fZ0QMBrOzdenNc6pdNfyXS8pfIWgQbP9-Nf3ZbXt-nFaxx1NJ7u4BlwyvMS8f3eMjRfwki3pfqXI5xitQVZFnNIdbb5AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60af7456ed.mp4?token=c7un2vRaswGH0JKKhqhrHJe20N4LVDWEdmOQJq0xAl8Pm07BtpNPOnm3UZjJtJpCAFr-5MOiGYXkzcFpu5XPEsBzYLUdPGhpYkIaj4T9NyrIJXHset8LExmP7V7EOwM5xOkItVd7XEcQbEZQZy4lRCabdQnT9HCy0SybOD08CWvVvAozBB_yWs7i4TVKXLsFiXieTqup43tl9qbM3Uqazz-HYosj46MI6UD9zGnvYWiWdbT-n1PtqQ8Q_fZ0QMBrOzdenNc6pdNfyXS8pfIWgQbP9-Nf3ZbXt-nFaxx1NJ7u4BlwyvMS8f3eMjRfwki3pfqXI5xitQVZFnNIdbb5AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۰۴ شب قرار عاشقانه؛ گنابادی‌ها همچنان پای وطن ایستادند
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/463276" target="_blank">📅 22:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463275">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBD4Luc5MXiZi0qSaL8IDbX5AuXlRf3YOoMumC8xUoEHGIDnI1biYHttdoc-EuDjXSIjCI3lzcSzChBmMQ5KnzI6hmAFsmEbb6whlZouQvGCkWGweUK8AcQ8YgriQWCUrH7qX1e2RKngX76DFua9pS6fLxvSocDodwkGbYcz0bpTiU35K_JcQ8AwFSftwxdJ_Nr0cBuwwGvmojFPX89qSXBVpwBU6C0wOe--uSB-T18ys1nm8AIXU72S-Qmenj95OCBoyU8A6FlneWO6tfzXAVY1cgBojmMY1MZKi3xkLOhwxRAJKcVVhYGgVSQiqqUN06oG_XfxvWpQZxyYa0Kt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی برای شرکت در اجلاس سازمان ملل عازم نیویورک شد
🔹
وزیر خارجه در مسیر سفر به نیویورک توقف کوتاهی در دوحه دارد و دربارۀ آخرین تحولات منطقه رایزنی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/463275" target="_blank">📅 22:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463274">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
برای درمان دندان به دندانپزشکی مراجعه کردم؛ هزینه یک عکس ۳۵۰ هزار تومان، کشیدن دندان ۳ میلیون تومان و کشیدن با جراحی ۵ میلیون تومان اعلام شد. با این هزینه‌های سنگین،
بسیاری از مردم توان پرداخت هزینه‌های درمان دندان را ندارند
.
🔹
پس از بیش از سه دهه خدمت، بازنشستگی برای ما به‌جای آرامش، به دغدغه‌ای دائمی برای تأمین ابتدایی‌ترین نیازهای زندگی تبدیل شده است. با وجود سال‌ها خدمت صادقانه، امروز پرداخت اجاره مسکن، هزینه تحصیل فرزندان، مخارج روزمره و هزینه‌های درمان به دغدغه‌ای سنگین تبدیل شده است. ما انتظار زندگی تجملاتی نداریم؛ تنها می‌خواهیم حاصل سال‌ها خدمت، کفاف یک زندگی آبرومندانه را بدهد. از
مسئولان محترم صندوق بازنشستگی کشوری
، سازمان تعاون روستایی و سایر مسئولان مربوطه تقاضا داریم
صدای بازنشستگان را بشنوند
و برای رفع مشکلات معیشتی آنان اقدامی جدی و فوری انجام دهند.
🔹
لطفاً پیگیری کنید چرا
به برخی خودروهای نو شماره
، از جمله خودرویی که با زحمت و حقوق کارمندی خریداری کرده‌ایم،
بنزین یارانه‌ای تعلق نمی‌گیرد و مجبوریم
بنزین با نرخ ۱۰ هزار تومان
تهیه کنیم؟
🔹
لطفا پیگیر
دهک‌بندی‌های غیر عادلانه
باشید. من مستأجرم با یک ماشین ساینا با درآمد کم چرا باید دهک نه باشم؟
🔹
عوارض برخی آزادراه‌های کشور
به‌صورت دوربینی و با ثبت پلاک دریافت می‌شود و راننده باید ظرف هفت روز آن را پرداخت کند؛ در غیر این صورت به‌دلیل تأخیر چندین بار جریمه می‌شود. اولاً همه مردم از این قانون و مهلت پرداخت اطلاع ندارند چرا اطلاع‌رسانی درست و کافی انجام نمی‌شود؟ ثانیاً همه مردم سواد یا امکان پرداخت آنلاین ندارند، اما بدهی آن‌ها روزبه‌روز بیشتر می‌شود. ثالثاً بسیاری از افرادی که نحوه پرداخت را می‌دانند، پیامک‌های تبلیغاتی را در تلفن همراه خود مسدود کرده‌اند و در نتیجه
پیامک‌های هشدار پرداخت عوارض نیز به دستشان نمی‌رسد و مرتب جریمه می‌شوند
. حقیقتاً این شیوه درآمدزایی منصفانه نیست. فردی ممکن است هنگام فروش خودرو تازه متوجه شود مبلغ عجیب‌وغریبی بابت عوارض جاده‌ای بدهکار است.
🔹
در ارتباط با
سهمیۀ سوم سوخت در استان‌های کرمان و سیستان‌وبلوچستان
سؤال و مطالبه‌ای داریم. مسئولان آیا متوجه نیستند که مردم این استان‌ها به ‌دلیل مسافت‌های طولانی بین شهرهای مختلف و مرکز استان یا سایر استان‌ها، برای مراجعه به پزشک و انجام امور ضروری به مشقت می‌افتیم؟
با این مقدار سهمیه بنزین، نیاز مردم برطرف نمی‌شود
. مشهد که رفتیم در هیچ‌کدام از جایگاه‌ها به ما بنزین ندادند و با مشکل جدی مواجه شدیم. این سؤال هم برای مردم مطرح است که چرا باید با وجود چنین شرایطی، سهمیه سوخت این استان‌ها محدود باشد؟ آیا استاندار و مسئولان استانی واقعاً از مشکلات مردم در این زمینه اطلاع دارند؟
🔹
بنده نیروی رسمی آموزش‌وپرورش با ۱۳ سال سابقه خدمت هستم. یک سرباز معلم پس از دو سال حضور در آموزش و پرورش، کارت پایان خدمت خود را دریافت می‌کند، اما ما
نیروهای رسمی آموزش و پرورش
با وجود ۱۳ سال سابقه خدمت، هنوز
کارت پایان خدمت
‌مان صادر نشده است.
🔹
چطور واسطه‌ها خرمای کشاورزان را نمی‌خرند و بهانه می‌آورند که خریدار نیست، اما همین خرما وقتی به دست مصرف‌کننده می‌رسد با قیمت بالایی عرضه می‌شود؟ منِ مصرف‌کننده به‌دلیل گرانی خرما توان خرید ندارم. اگر واسطه‌ها خرما را از کشاورز با قیمت پایین خریداری می‌کنند، چرا محصول را با قیمت مناسب به مصرف‌کننده عرضه نمی‌کنند تا فروش بیشتری داشته باشد؟ آیا این انصاف است که زیاده‌خواهی واسطه‌ها هم کشاورز و هم مصرف‌کننده ضرر کنند به خاطر!
🔹
در شهرستان ورزقان استان آذربایجان‌شرقی و در مجموعه
معدن مس سونگون
، متأسفانه در شرکت‌های تابعه،
جذب و به‌کارگیری نیروی انسانی
بر اساس سفارش و روابط انجام می‌شود و این موضوع موجب ایجاد تبعیض و احساس بی‌عدالتی در میان بخشی از مردم منطقه شده است.
مردم بومی این منطقه
انتظار دارند فرصت‌های شغلی مجموعه سونگون به‌صورت شفاف و عادلانه در اختیار نیروهای واجد شرایط قرار گیرد.
🔹
من
راننده تاکسی
هستم. سهمیه بنزین ۳ هزار تومانی ما ابتدا ۴۵۰ لیتر بود بعد به ۲۲۸ لیتر کاهش پیدا کرد و پس از گرانی بنزین، سهمیه را به ۱۰۰ لیتر رساندند که همین امروز تمام شد. با توجه به اینکه تاکسی وسیله امرار معاش ماست،
این میزان سهمیه پاسخگوی نیاز رانندگان نیست
و هزینه سوخت فشار زیادی به ما وارد می‌کند.
شهرداری و تاکسیرانی
نیز تاکنون اقدامی برای حل این مشکل انجام نداده‌اند.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463274" target="_blank">📅 22:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463273">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b65d69a311.mp4?token=ElPz2BmJwSW8T2tRBMgxUUlqpZ-EmhAP32k8PTXP4Mdk0v2pv2m1MDqNgqpQU87igPiDZ-iN-9l2L0cx1YA18RZgGg3nNWu-Da-GBb-u3M-LM6-wg0rfd3ROqGwd1kb8AvIdvSmbTlnt52uo2KMV7GX_vWQxzb-RQfC5uFXT6Kml_SuHpQHTjIkkQ8hFZ-cJh_XmplYH-CPhdkRGoa48NPoxaknU0R_YbP56UQ-lAVWNxAzUJflYuMVAa7HUYtP_MIi9cw9aFdeTa7iQbRYyRvQT0nGZDObLVm2FA7EOVEg_hKIpyaEdpozwQ9cIzXFeN-QkRkEt0bKYGESg6k63zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b65d69a311.mp4?token=ElPz2BmJwSW8T2tRBMgxUUlqpZ-EmhAP32k8PTXP4Mdk0v2pv2m1MDqNgqpQU87igPiDZ-iN-9l2L0cx1YA18RZgGg3nNWu-Da-GBb-u3M-LM6-wg0rfd3ROqGwd1kb8AvIdvSmbTlnt52uo2KMV7GX_vWQxzb-RQfC5uFXT6Kml_SuHpQHTjIkkQ8hFZ-cJh_XmplYH-CPhdkRGoa48NPoxaknU0R_YbP56UQ-lAVWNxAzUJflYuMVAa7HUYtP_MIi9cw9aFdeTa7iQbRYyRvQT0nGZDObLVm2FA7EOVEg_hKIpyaEdpozwQ9cIzXFeN-QkRkEt0bKYGESg6k63zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از شب اول تا شب ۲۰۴؛ مردم هنوز در میدان‌اند
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/463273" target="_blank">📅 21:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463272">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320d035b7f.mp4?token=hM2HsAEYff2WWSnxdK47JwZjCZsQRUbmxZFoHjCP1omekzrMl5kda5TYUCe-XfBJoCdr82YsjrM9-hoz6pCsvrV8vqWsn7YBikVpKZpZscS1ok_oNl2nFUjVMxpedBlG-JgfI9UWZXp9t4jhofYyI-rIMdTkVum3h1mg-Snh2vs6N-FSyn1nQhXkSxjz2KzRmLQ_q0SBZleGnHblk-hmcf13Byj8HB0W9_Psfie4P7T3hjVu2F9yisg8NdzV02uz74mLziI4RIHyo-GU_ePr5Iqlr-N9SNPEt80w-X0JUr40Ve3S0sHCOoUsiUVW-gwUmsJFHLsFhMJykSzGn_CuuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320d035b7f.mp4?token=hM2HsAEYff2WWSnxdK47JwZjCZsQRUbmxZFoHjCP1omekzrMl5kda5TYUCe-XfBJoCdr82YsjrM9-hoz6pCsvrV8vqWsn7YBikVpKZpZscS1ok_oNl2nFUjVMxpedBlG-JgfI9UWZXp9t4jhofYyI-rIMdTkVum3h1mg-Snh2vs6N-FSyn1nQhXkSxjz2KzRmLQ_q0SBZleGnHblk-hmcf13Byj8HB0W9_Psfie4P7T3hjVu2F9yisg8NdzV02uz74mLziI4RIHyo-GU_ePr5Iqlr-N9SNPEt80w-X0JUr40Ve3S0sHCOoUsiUVW-gwUmsJFHLsFhMJykSzGn_CuuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ا
گر قرائی اسرائیلی بود بعد از ونیز سلب تابعیت می‌شد!
@Farsnart</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/463272" target="_blank">📅 21:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463269">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ti-wxrY5NfdVY_3QiQ45Glnq-b36CEeTYAcGwt6aeelKGEr9a-7hRgL14b-__-YBomRv946d29JxHsCPEMgYyzwJZtDEtNrV4uzVo1AMpdFgfwumC6PbeElrxBOjxTN_VS8XgU7TKBx8ZSODcZJRbUyS0NbkOEpJZ8dKYvJ9DUj9chJBrvl2ldE6QibaCutvADkNnBxge5aVrQRDEgQiZNee4NfEhAJzt1xFxYIaD6yvSfUEajtjXFXE8Ff6WIqh-V_SN5xifcD_op64IK2B36ma05rWABxU2jy3P2qFAO6anY0NmiHjfQpT-MREPjJQKj2D4aG_wT-is8RYxe9PGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPXj0EtnEGziS4mxJCU5RzQWb2dGsFyLk9bAOtAuexA0zteeRczXEPGPZvfnMcnq668Nw6Icb-gGLWl_y0ir21dbLhSCHz9DX1FYOixLw-1CE1vrEM6KUbKOdBJZw-wvnmIQFRZCpCK1gXCTRkc_rVr0uFWjqND3iZrjDUVsEF7v0Wvl2Mr3HyBc_YkaJX2yne3IaPYmuUFokbeUbQaw1waQlc_F48DpxyBLcBe5xzJ4cCm5qMTT7tzxpZhzNmN2J2o0zRbPI3COXPsudDwxohhWG2tjYIew01I4Xaj5EN8UykVWpOc2X6nO8zREYp_IqawmkoGHI3KSn63O7yEgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhMqk-7EYhaE_5RQFS935E0y_CcFGqMBaMr_HL5WdZrskk5axr82cNP2cHNA-NUD-nTF5BTyhh9mxKo8CGb0UgOVTx4AoqgwYvAjshtPnPfgFFPEjPCcKEKF1K9By66-OjreJtsE4c3D6ELhMQIpy7Hcj7nnLpC3i42jszllBZf39UsRRbI8JlapWL8WaZPQ2ObMwud12cHZo_zftT-Z6MvvLNgyXxvbF48konDucNL0T9kz5oTABvP2_FRn0MIIPJyDAK7lTJifHRpEOczgqGA6fSQc0gPQiVFMlqMNhON_-FV35EmYaPSQKeaUR-TyupQgVKIBXZ53MRnE6VGlPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نخستین تصاویر از ۱۷ اتوبوس آسیب دیده از حمله آمریکایی‌ها
🔹
سخنگوی شهرداری تهران: آمریکا با تعرض به کشتی حامل اتوبوس‌های دوکابین شهرداری تهران، به ۱۷ دستگاه آسیب جدی زد؛ اتوبوس‌هایی که برای خدمت به مردم در ناوگان حمل‌ونقل عمومی پایتخت عازم ایران بودند.
🔹
۳۱ دستگاه دیگر از محاصره عبور کرده و در گمرک منتظر ترخیص و انتقال به تهران‌اند.
🔹
جنایتکاران آمریکایی با زندگی روزمره مردم ایران در جنگند؛ این خباثت‌ها عزم ما را برای خدمت بیشتر، راسخ‌تر می‌کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/463269" target="_blank">📅 21:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463268">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45062f4ecb.mp4?token=MK-blKzvPxZfttkXKLG6iSHmhwILwA55SxIBskZpHabyMMqe7LFRcgE7ZwokuNYzFWMpfUI0ymDxcu9e4DyGyqjQv_9IaCJ8UUjNT-Q4wklIjasdN9iGzdJDbskDKn0yq1we7uwm0cDVtrjdOBoL6VbNdeXBnd35aOinGz1onw7BhMlz2OkdE-3g7zJp1sf4A2B4nmPe5EK52a3J44OVfcctFLoZy42DeHmuen_eol2n9pm-YA-veoA5Mqt3uOGXGECIJE0U_V6hJtqmiJ6E4nwpcLTf0NkACYeEtnZFE8djsYluNh1PZfpv0pTWZuYfOnOexTTbc_GAq6oTBoRsZSGRxTZqgFFB4UzjNvy1kjdGuxZi_LkdOYcaZIoLwQYsln-7zH-3OLrPNUAaeMFpau0m4hAy6BFw_5HI3uagmO3GzNaq2x2BJZsMmtHXxTtHZ9o_kYW_uKftgrlty3gTDS1GMa8N1ALM2KhoDfC_KY_kLnhzpbp2hINOqq6Z3Bco-S5LNcTT0CokzP_qzfQGO0hGQd8N3aB-AoXw_ZYYyMEn9vvTivCkEysGDWlrQdeRbOvfSOo2tSK-SoXVNDuU552jqVisegsB969Es7wMs-ykkTjlI_jeApmjE_Rbu2yYSwao48aL0YByJvex4MivQM9Lz7iBqj5CZ3zrhfznz8I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45062f4ecb.mp4?token=MK-blKzvPxZfttkXKLG6iSHmhwILwA55SxIBskZpHabyMMqe7LFRcgE7ZwokuNYzFWMpfUI0ymDxcu9e4DyGyqjQv_9IaCJ8UUjNT-Q4wklIjasdN9iGzdJDbskDKn0yq1we7uwm0cDVtrjdOBoL6VbNdeXBnd35aOinGz1onw7BhMlz2OkdE-3g7zJp1sf4A2B4nmPe5EK52a3J44OVfcctFLoZy42DeHmuen_eol2n9pm-YA-veoA5Mqt3uOGXGECIJE0U_V6hJtqmiJ6E4nwpcLTf0NkACYeEtnZFE8djsYluNh1PZfpv0pTWZuYfOnOexTTbc_GAq6oTBoRsZSGRxTZqgFFB4UzjNvy1kjdGuxZi_LkdOYcaZIoLwQYsln-7zH-3OLrPNUAaeMFpau0m4hAy6BFw_5HI3uagmO3GzNaq2x2BJZsMmtHXxTtHZ9o_kYW_uKftgrlty3gTDS1GMa8N1ALM2KhoDfC_KY_kLnhzpbp2hINOqq6Z3Bco-S5LNcTT0CokzP_qzfQGO0hGQd8N3aB-AoXw_ZYYyMEn9vvTivCkEysGDWlrQdeRbOvfSOo2tSK-SoXVNDuU552jqVisegsB969Es7wMs-ykkTjlI_jeApmjE_Rbu2yYSwao48aL0YByJvex4MivQM9Lz7iBqj5CZ3zrhfznz8I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این خیابان‌ها جای خالی ندارد
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463268" target="_blank">📅 21:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463267">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eb2a91cb8.mp4?token=EPqVFd3wr4hPwYG8TfHRbOFXxV0yW1c0RZjWZRRY31Nv1Wgcfnn93Pj1Kkhs_8wlg2TK5B1V3P8WD6hmalDrmkdrmWjBnj-MR1OeG_LmCJc_KIyTOR_lnCWuojzdnaNSDEkPL1bHAUzZ41qVEnMuhx0eqilnE7wk4MQbVt9H-clMidj4URjRudRAm46zjQQ0v1_x6GVttbK2Kg8dt9_UQ6egda8I0JsvxMFQ0Qh0QL73RPQB9Q7xEp-Y-69geySbMF8cFx5hR50Ql_TQFL_7XUOXqj5i4loHjQ3WrarPwY1dAYssiFMs6rkzD_du5chfiP0Rpo6QHAAabABLorKBFV_3JHkQXC6lSKOBS_sK7yPhqt7F9G2eP3Xucv8eJaSfdQOhK9CbCiLnZmxZXazfS5cptv2NBSfAvGgML8Ikkey2Ut3hbJ4-TYM7j5QnSY1QMMmWyNOVBAHcSquds6lNFhAkqLGvAM7NosJfZbhQ3xNNK-uqT80y3aeyvoU-Gl3UmL9SRPXVKI-7EyLm7buEVjIfeVTMVyNdYTkTIwbeilhHAo5SXhsUfB7N3nZEWikT4Maz6GK5UggiapD93GTYDqT8-voDk2VNKQP8Y6WmXzvgCfLfH76B7j7rVDP-n8kle3OHhr9DnHeW0OSaflDNQHhuUKJPUIuupEjkBKp8gT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eb2a91cb8.mp4?token=EPqVFd3wr4hPwYG8TfHRbOFXxV0yW1c0RZjWZRRY31Nv1Wgcfnn93Pj1Kkhs_8wlg2TK5B1V3P8WD6hmalDrmkdrmWjBnj-MR1OeG_LmCJc_KIyTOR_lnCWuojzdnaNSDEkPL1bHAUzZ41qVEnMuhx0eqilnE7wk4MQbVt9H-clMidj4URjRudRAm46zjQQ0v1_x6GVttbK2Kg8dt9_UQ6egda8I0JsvxMFQ0Qh0QL73RPQB9Q7xEp-Y-69geySbMF8cFx5hR50Ql_TQFL_7XUOXqj5i4loHjQ3WrarPwY1dAYssiFMs6rkzD_du5chfiP0Rpo6QHAAabABLorKBFV_3JHkQXC6lSKOBS_sK7yPhqt7F9G2eP3Xucv8eJaSfdQOhK9CbCiLnZmxZXazfS5cptv2NBSfAvGgML8Ikkey2Ut3hbJ4-TYM7j5QnSY1QMMmWyNOVBAHcSquds6lNFhAkqLGvAM7NosJfZbhQ3xNNK-uqT80y3aeyvoU-Gl3UmL9SRPXVKI-7EyLm7buEVjIfeVTMVyNdYTkTIwbeilhHAo5SXhsUfB7N3nZEWikT4Maz6GK5UggiapD93GTYDqT8-voDk2VNKQP8Y6WmXzvgCfLfH76B7j7rVDP-n8kle3OHhr9DnHeW0OSaflDNQHhuUKJPUIuupEjkBKp8gT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دنیا این‌گونه جلوی نفوذ ایستاده
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/463267" target="_blank">📅 21:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463266">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBJjsQWVl08kRXpclb8k4R71uegNGlfvdWntBzTENjNdWYyC2aleSdoRtHhlSg2sZgQ120An_y7N7ovN2cEdSO_Q8FEEXESbNU0D7PDUjTdTLaheyc2zx-De2VzTUvyomKEYtTDfGigWag4rnphDEU11CObQfev4fvndujnVkznNoY8nTxPeiStcQkAZZlatrqDjYTjWvZqDzEoQ2nIJ4hbcuBgoUeaUwMSXpQIcHdtsA2zfWzCBYVBCRaPz8BoSuyTW6ALlo6Eige12muBNGKBSRq-5WrY4a9mlTBlIcfxEyGlCnt-vjpifUID7XEkYwklNgjU96RBBKbXbqo4bAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: آمریکا برخلاف ظاهرش آسیب‌پذیر و در معرض خطر است
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/463266" target="_blank">📅 21:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463265">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXJI-u3ibWhc5Wg8LkQsgpevjDehvHe8Co-TrLJXYyEI1k1Jzxd9BUjQReJmlihYmaZ3ZUYdpHcHBUHZ2t5ft7SFmx7XJPEMDdnWQ4Qgaj0jdDuuXPe7rgw_AJNot_TffT5OIKsz3svcyQYnL0vPcv0CNUEKUlk2vur03xeB2VFf6kShSsV4HbggtZ0wN75PBqZ-eRefmI7XtmpAgaD1YIl-eG9l-4zbHoGCUpeo62KvAFZTU1moMGmM1kxoR8WvV2jXgvSibeRCVJg6djclMh32OVbOymGH6krMC1vv5YSuiownLPbY-fNvrElGSc6EOcEboMRhtO1IPtub03tt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر اقتصاد: ارائهٔ کالابرگ با مبالغ جدید به دهک‌های پایین از ۱۵ مهر آغاز می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463265" target="_blank">📅 21:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463264">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‌  رئیس شورای‌عالی سیاسی یمن: صلح با یمن کم‌هزینه‌ترین و کوتاه‌ترین راه است
🔹
المشاط: ما تأکید می‌کنیم که صلح واقعی و عادلانه همواره گزینۀ استراتژیک ما بوده و خواهد بود؛ همه باید درک کنند که گزینه صلح با یمن، کم‌هزینه‌ترین و کوتاه‌ترین راه است. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463264" target="_blank">📅 21:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463263">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‌  رئیس شورای‌عالی سیاسی یمن: باب‌المندب به‌جز سعودی برای همه امن است
🔹
المشاط: به جز کشتی‌های دشمن سعودی، تردد دریایی و تجارت بین‌المللی در دریای سرخ و تنگۀ باب‌المندب برای همه امن است و از سوی یمن هیچ خطری آن‌ها را تهدید نخواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/463263" target="_blank">📅 21:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463262">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbad9d4e68.mp4?token=laewQououLQXe-0o7En65QDYo1KTZb1zYrKsQ0xLxD378NBxACbg8OkEpw0IAaNo-oiXNc4Eje74ShweqNM08xPXZunyRg7INAzhL8laKgxnwCYDlAPWPgzQ-qXJJqMg7RbZ7KsFV8F7u7gN6Sd5XeLJZ8G7KeGPtEFxonNXQT3_yjENgPyA-SdLblB3HjhynLnyI0TBqzuRJodntsE8k9tTVtJiVHchMBi_HxpcZGdWZX4ZzBSdyfRDg_rKIEh-eo9H_Jtjg3OJ5sehcdlavZ-PZJvj4ye9hn6Q9qd6TaQJDpfqKZZPUTRctUiZChbUUSJBVN0ZRCQMrQYlnQsU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbad9d4e68.mp4?token=laewQououLQXe-0o7En65QDYo1KTZb1zYrKsQ0xLxD378NBxACbg8OkEpw0IAaNo-oiXNc4Eje74ShweqNM08xPXZunyRg7INAzhL8laKgxnwCYDlAPWPgzQ-qXJJqMg7RbZ7KsFV8F7u7gN6Sd5XeLJZ8G7KeGPtEFxonNXQT3_yjENgPyA-SdLblB3HjhynLnyI0TBqzuRJodntsE8k9tTVtJiVHchMBi_HxpcZGdWZX4ZzBSdyfRDg_rKIEh-eo9H_Jtjg3OJ5sehcdlavZ-PZJvj4ye9hn6Q9qd6TaQJDpfqKZZPUTRctUiZChbUUSJBVN0ZRCQMrQYlnQsU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوشت‌افزارهایی که با تخفیف، گران‌تر از بازار در ‌می‌آید!
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463262" target="_blank">📅 21:02 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3s8D49YPq5eDztc0e5gtT7kA1wSTbTrDejPdb_AJk_VDjeckdq-uz8eDG_kHHJ23t1VFdmcPJCfBCT3QI12tciBwg_YKqS_KaD7UM9Zrs26V7kcklHlFWvWeQvDJJGdKFCxlvKx1D4bRUzrayHEoGq2o54CTVLdHBX5637kEJKKEoVlX988J5IPnRQvs7uadVUgc9V5lm9Z6urz6EJGsL0MK5eU_b6S5r48OT30OA_dPr5ylupPcLmlrjg3gElzxtPZKRKOZ-swPsgWJw4vptcCqYi19MqNyTuA2hZQZMnUw7n3HupkmKfF0EN5w8fKnA5paD1PpusyC2vX8fwojA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TCjaxbW3UxF0vdfwAK9V1oFOdaKzqh9GFJgNxhERaORfIXlS7oqpZ6wQV7DTXb3zY-mkblVs9F05V2bPC51cxishFcMGZJoA1QZ4F_dHi8gIwVFkTzV5iPe1Xn6WyGD9aDwHJR-8xEGAvR4CkZp5ttGACyN9NTPFFnUstNaUb03DNV7eUdV0wdY6nCjOXfJmVPnUK7P1TrQSAxaon8WXQayr53oG5-v5D8KnccLdNyw3zIm8-gaiyBHJLLMcLYM9eJWOwSMDTTVwYMf6dmUWdF9j9ZAeZ2jjbRK9GBtLSoP1nbt3ptaG43hIEqNcW5gcgOrVH93jJQzSP5feRwNUFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف: آمریکا برخلاف ظاهرش آسیب‌پذیر و در معرض خطر است
🔹
در روزهای اخیر هلدینگ بانکداری جی‌پی‌مورگان گزارش هفتگی پیش‌بینی بازار نفت خود را با جمله‌ای غیرمنتظره آغاز کرد:
«برای نخستین بار از زمان آغاز درگیری با ایران، ما هیچ چشم‌انداز پایه‌ای (سناریوی مبنا) در اختیار نداریم. ما واقعاً نمی‌دانیم چگونه باید سرانجام این وضعیت را مدل‌سازی و پیش‌بینی کنیم.»
در واکنش به این موضع بی‌سابقهٔ تحلیلگران بزرگ بازارهای مالی، محمد باقر قالیباف در صفحه شخصی خود در شبکه ایکس نوشت:
📌
«این وضعیت دقیقاً شبیه پارادوکس شرودینگر است: امپراتوری آمریکا در حکم همان کابینت شرودینگر با بشقاب‌های در حال سقوط است؛ در ظاهر هژمونی و قدرت برتر خود را به نمایش می‌گذارد اما در واقعیت کاملاً آسیب‌پذیر و در معرض خطر است و تلاش می‌کند ایران را بدون هیچ پیامد و تاوانی خفه کند که این غیرممکن است.
📌
این بازی پایانی در هیچ مدلی قابل پیش‌بینی و شبیه‌سازی نیست. درِ این کابینت بالاخره باز خواهد شد، و از همین حالا دست ایران روی دستگیره در است و شرایط را کنترل می‌کند.»
📌
قالیباف در این توییت از میم (Meme) معروف اینترنتی بشقاب‌های شرودینگر استفاده کرد. تصویری که در آن بشقاب‌ها به ظاهر سالم‌ ولی هر لحظه در آستانه شکستن هستند! تصویری برای نشان دادن وضعیت در معرض آسیب و شکنندهٔ آمریکا در منطقه!
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/463260" target="_blank">📅 20:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‌  رئیس شورای‌عالی سیاسی یمن: از سعودی غرامت می‌گیریم
🔹
المشاط: دولت، ارتش و مردم ما در مسیر پایان دادن به تجاوز و محاصرۀ ظالمانۀ عربستان علیه کشورمان تا بازگشایی فرودگاه‌ها و بنادر، بازگرداندن ثروت‌های ملی و دریافت غرامت پیش خواهند رفت. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/463259" target="_blank">📅 20:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
رئیس شورای‌عالی سیاسی یمن: اعلام می‌کنم که نیروهای دشمن سعودی از تمام مناطق ساحلی غربی یمن اخراج شده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463258" target="_blank">📅 20:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge1nM6_QbUQi4cM1ywvMxv8fsAPTSgh5OncTRUuwyNsUPhEpstiHfh1wMAhPGp3gQeaHbDSEpaJ5HLQYp3n4ck7t3GnHZWa4dpaFGu1pOyYYi_r7_KgVF3h5U4298gofj3JKTKddJ6WMMnFxLTfmD9UarhCrOTElDzWuCt7IxJs6nEsSUkT8811Sfb2uVhJLKGq9Fbte1LJbeniYUG0Usp2AXttQy5dIV1wKubp6pEFTF-f4_L-F9ozB02B50R7Eye6Li4j9rXvmtShws0wI7IPA5tHB_TYS5qfsKsspgu4K2ejR1HNLo5Atg8bDy2wa0SBXrBrltLkPuO69v7KcVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رئیس شورای‌عالی سیاسی یمن: اعلام می‌کنم که نیروهای دشمن سعودی از تمام مناطق ساحلی غربی یمن اخراج شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463257" target="_blank">📅 20:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">حملات هوایی صهیونیست‌ها به جنوب لبنان
🔹
رسانه‌های لبنانی از حملات هوایی ارتش رژیم صهیونیستی به شهرک المنصوری و النبطیه الفوقا در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463256" target="_blank">📅 20:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463255">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2270aa5ea8.mp4?token=FQ2Z5ZMV4pGj5MRjJHZqtzWa5Zj29bU8iYgSKotGqa_yiAWt4uLD1D7gN4SQ87WYBM9t1VeRJgl2y_txWC28Q1hFbCYVkNTYHO3azbPBcMS9Re5LJ1bWV_o1iIWJF2AGkkJVPdkagJRzX6rrh2SgGfpIaVL08-cgg94wJH6aCrr4fmAkDlkbb1U2uhlY5TB8HNtN6ShSJllAPPB0poDOBEt8i1ROZ_YbxXwjZCrA-_g549t_g7kY-z7N_oivtmQpKUU3R65YDCWzYenat3xpp-7LI78iqizs90pDMUa-tHIXkdyUFRuH3xcwGx9k_X0tGI6BtWhybCsNExQ_jGWHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2270aa5ea8.mp4?token=FQ2Z5ZMV4pGj5MRjJHZqtzWa5Zj29bU8iYgSKotGqa_yiAWt4uLD1D7gN4SQ87WYBM9t1VeRJgl2y_txWC28Q1hFbCYVkNTYHO3azbPBcMS9Re5LJ1bWV_o1iIWJF2AGkkJVPdkagJRzX6rrh2SgGfpIaVL08-cgg94wJH6aCrr4fmAkDlkbb1U2uhlY5TB8HNtN6ShSJllAPPB0poDOBEt8i1ROZ_YbxXwjZCrA-_g549t_g7kY-z7N_oivtmQpKUU3R65YDCWzYenat3xpp-7LI78iqizs90pDMUa-tHIXkdyUFRuH3xcwGx9k_X0tGI6BtWhybCsNExQ_jGWHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لیلاز، اقتصاددان: وقتی طرف آمریکایی نمی‌خواهد مصالحه کند صحبت از مصالحه پالس ضعف است
🔹
به غیر از نیروهای مسلح، بقیۀ نهادهای کشور آرایش جنگی نگرفته‌اند.
🔹
نباید فراموش کنیم که بسیاری از مشکلات ما به جنگ مربوط نیست و برای قبل از جنگ است.
🔹
در ۳ ماه اول سال…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/463255" target="_blank">📅 20:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463254">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb07fb5b1.mp4?token=k77EZTS1BFtEPDTL27fLAsmW5Y0clPNk4Q0UzUrY59obilV-kvpwWRnDLqgQnlQ8Ltw83ckkW_UpIJlnW2TXexuFpig0qmeeewBGCcRULbw4_tnfDy1_IyQQkhtszqpCovLYdPAvOE7q6SpJxjecwDtRlb8g6hgkTxKfcm_mkmwUJhI7-0N-MV6043jd-7Mn7KmazO3yruerW2TJINh7dc5t6QDisdcNpFPCv1dTmQj25c8uIwKIivgQHfwCRwXhZtTCFNNuakAimeL_7bdFCmwwjURHOnghDSJoseJuUwYAWEpIaZtdbRgHQ3iWT-wQnad434NEK1li-krZ9C69vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb07fb5b1.mp4?token=k77EZTS1BFtEPDTL27fLAsmW5Y0clPNk4Q0UzUrY59obilV-kvpwWRnDLqgQnlQ8Ltw83ckkW_UpIJlnW2TXexuFpig0qmeeewBGCcRULbw4_tnfDy1_IyQQkhtszqpCovLYdPAvOE7q6SpJxjecwDtRlb8g6hgkTxKfcm_mkmwUJhI7-0N-MV6043jd-7Mn7KmazO3yruerW2TJINh7dc5t6QDisdcNpFPCv1dTmQj25c8uIwKIivgQHfwCRwXhZtTCFNNuakAimeL_7bdFCmwwjURHOnghDSJoseJuUwYAWEpIaZtdbRgHQ3iWT-wQnad434NEK1li-krZ9C69vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لیلاز، اقتصاددان: وقتی طرف آمریکایی نمی‌خواهد مصالحه کند صحبت از مصالحه پالس ضعف است
🔹
به غیر از نیروهای مسلح، بقیۀ نهادهای کشور آرایش جنگی نگرفته‌اند.
🔹
نباید فراموش کنیم که بسیاری از مشکلات ما به جنگ مربوط نیست و برای قبل از جنگ است.
🔹
در ۳ ماه اول سال ۱۴۰۴، بدون جنگ رشد اقتصادی منفی داشتیم اما ۳ ماه دوم ۱۴۰۴ یعنی پس‌از جنگ ۱۲روزه رشد اقتصادی مثبت بود.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/463254" target="_blank">📅 20:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ارتش ایران پهپاد اوربیتر دشمن را بر فراز تنگۀ هرمز منهدم کرد
🔹
روابط‌عمومی ارتش: ساعت ۱۸:۳۰ امروز، یک فروند پهپاد شناسایی پیشرفتهٔ اوربیتر با آتش سامانه‌های بومی نیروی پدافند هوایی ارتش بر فراز تنگهٔ هرمز هدف اصابت قرار گرفت و منهدم شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463253" target="_blank">📅 20:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs5Rf8R0IgMwjjp_cH8nbESvU3l3yulNUSs4hcuSmJf4TjqnMeTJpkzV3xVg6ljG3qWfNWuLRFBbvDDVrHDCYe3DrPkcfQkmokrj-S9lB05DT_J8sIzK3fAwtUNkuosKhapa_uM94p00h6NEkYXxSUM5UrMcuS00uMCtZB4xO3zGmOnRl9obxIF8oHR_IXQAtcLfbPYpECxfbzPceestrRIJJoikt2kSXmjz28g-GOcAlCKmv3DcU8cXstFSpwpSI4PynMiY7d5owcFp_motpEM4ncdfHIvo3tRglz4DPWqhMY26FvF3FzmzMDVBWtDL2HQdMHOyaKewa1mhEAV9-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش‌وپرورش: ۱۲۸۸ واحد آموزشی که در جنگ آسیب دیده بودند به چرخۀ آموزش برگشتند
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/463252" target="_blank">📅 20:18 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463251">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8b777fb5.mp4?token=vFa8H0MOMcniOMJ8MfoPsmqTK8Y7D45tItg6gmvUz84CKy73ibvWuIJtsndm766sFCYtxMEleuDI72XSiTbxcUcS1gPYEc8i1Xd8yabGCi_OIxXqGWMYiyndPje2nd3FBd9CBjJ7TheblsiwmX6xIVeyapsP2cYGHPL4XgBvzxJ3vNRCL711fmyb0pQnQQegLoRlEoeki0IN-A_wz133G_DojbjFjPxn-XEA6KxfuJipbYfZ3Nr64xbNBJuaJR-1FoY7Ns0Jkg2-eT1D2ZMBdZLtAEPPmQMUmU1G_cuae7uP5oA0sL1zCboIdq7m6hsHr9MoVI8tKEaPDEIfysTXSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8b777fb5.mp4?token=vFa8H0MOMcniOMJ8MfoPsmqTK8Y7D45tItg6gmvUz84CKy73ibvWuIJtsndm766sFCYtxMEleuDI72XSiTbxcUcS1gPYEc8i1Xd8yabGCi_OIxXqGWMYiyndPje2nd3FBd9CBjJ7TheblsiwmX6xIVeyapsP2cYGHPL4XgBvzxJ3vNRCL711fmyb0pQnQQegLoRlEoeki0IN-A_wz133G_DojbjFjPxn-XEA6KxfuJipbYfZ3Nr64xbNBJuaJR-1FoY7Ns0Jkg2-eT1D2ZMBdZLtAEPPmQMUmU1G_cuae7uP5oA0sL1zCboIdq7m6hsHr9MoVI8tKEaPDEIfysTXSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«چشم اسفندیار» آمریکا در منطقه چطور کور شد؟   @Farsna - Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/463251" target="_blank">📅 20:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463250">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anjmFbKf24boFr_5GMcpJCioW-XX1E8IEP34tYNgwy8IvMGXtW1EWejSGGJrrCSSgyxuehnj8ChQPo_OaHtCbqpAkOC233twUwdRGSlo1bSEOD4lEtQv5jf8pvLaz9xGjRL5FNlf6dzbxbaEzMJPhf9EJ0_mPVeMlhVOOPr9-tG-qnt5dCb_7qk-RRs0aBwgBn6ptCDA-T2Q8AK3PR-Qfh-dPftIBK35yW7gyr1wkrvQuw6haItYum9yVNkeF6n2KY7yrqSm_6zd41QN6Y59Dp-d-b6CCxYvF5TrVTd9AHUORcmx76eo87JsUeVuK17WSO5QalR8DzONaCcjmXB7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار یمن: تنش‌زایی عربستان را با حملات کوبنده‌تر پاسخ می‌دهیم
🔹
سخنگوی دولت یمن: زیاده‌روی ریاض در ارتکاب جنایات بیشتر علیه مردم یمن، صورت‌حساب میان عربستان و یمنی‌ها را سنگین‌تر خواهد کرد و سعودی بهای هرگونه تشدید تنش را خواهد پرداخت.
🔹
یمن برای جلوگیری…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/463250" target="_blank">📅 20:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463248">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEh2Dph2gmWLd5jm2-HEsxS1zEkOn8s8cC5oO7ym8zCzponrSShhOuLiryzjLPbY__ecl5UjVbO-7ZSrdJJ1tDsLyAwnJcKtemb4SjCvaJbXRiWzVOvbAWGUS6Bmmf8a1Ydhza3Rj9W-s8n0grUAf9MhSZmNoEzZmf4a4lW4LXPI1yomSedbMLYUkmcqc5aSrzQJyTmXp0cTt6Nw0NbOZOzt9rMFX2g2iYzFd7g0i2DgSc9TOBnmmk3JIyU9X0RiWuir-1GGb_8ySmu2ErnGSO4Rzjtjw90HvWk_uHRczUkFTcph0DZY9HT6LfMlqP8-OLS3CIx53bL-sExGcUdNsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورینیو اولین دربی فصل را باخت
⚽️
اتلتیکومادرید ۲ - ۱ رئال‌مادرید
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463248" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463247">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fai8kErVTD5sZ1eSZNyWlK8tdlUhpYsxIqdRo_EYORe8zWzGT5hULQL5q8u-xfeCPJxnZmwyPMQRuiu7B7wS2FL41h0O4sBk1djCQ8rFtWgypiLd613DMzc8iSyXK-25R_-7XBkz_ttnN8_TtewAJ68EbkrsALywGOwnOI8i_WAFAs4bBQSC9XjaD1ywYJE4pM7tF-y5VRWbAtpLOWiMscJ_UAQd0DNsdL2XcAjgFpgvPWP0GY59fbto-1bHeDikAc5p_n2nMs2fSvXN6x1MfqjFWdhmNf2DjSVRRZHIYlIGANWZ7BvRhVSztVR0PPI85xsivW_rzGCxEtli87CL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: به‌هیچ‌وجه نباید اجازه بدهیم تولید متوقف شود
🔹
همۀ ظرفیت‌های اجتماعی و نهادی کشور باید برای کمک به کاهش مصرف انرژی، حفظ اشتغال و تداوم فعالیت واحدهای تولیدی فعال شود.
🔹
در شرایط کنونی، همه بخش‌های کشور باید با هم‌افزایی و همکاری، برای حفظ جریان تولید، صیانت از اشتغال و استمرار فعالیت واحدهای تولیدی تلاش کنند.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/463247" target="_blank">📅 19:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463245">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxM3j-uMtVUhmezS7Px6SQdQ0sRMzv4nJTrsrJJqE-vuQwaDpg6fIRl7i-bJUm8ql3AqqJv0WgGEg5bKNMoHA7diXvskMQHDCSD8RzB-M-gKdGtzYQGvcF2LPAdulOwyq7HWcTjbZQYdeO48ZQLUxrLPgkIY5T5vGGrT58LAPas4XVhooYumCccLjyx-0HmcBG5qyTSahGtyDW2NRPKDtTaoAI98Heo4WurjGL9zHz_7_MXBJ04-N4V6NXTgcuZg3yjfR084j71scJPfT5Os2WrkBjW_GQFoUZg0MRnVZRjd4WoBhwBto27wtGqo9A6yx_YyMTXfULRJCjPJlpW0hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر سیاری: دشمن ما مجبور است منطقه را با ناکامی و آبروریزی ترک کند
🔹
معاون هماهنگ کننده ارتش: هر دشمن تجاوزگری، برای خود اهدافی تعیین می‌کند تا در نبرد، به آن دست پیدا کند، ناکامی در دست‌یابی به این اهداف به منزله شکست دشمن تجاوزگر است.
🔹
امروز دشمن ما نتوانسته به هیچ یک از اهداف خود از جمله ایراد آسیب به تمامیت ارضی ایران اسلامی و همچنین نظام مقدس جمهوری اسلامی ایران، دست پیدا کند و مجبور است با ناکامی و آبروریزی، منطقه را ترک کند.
عکس: اکبر توکلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463245" target="_blank">📅 19:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLNnfF6Z_INqfqCXJecqBO2Yhel7znhjRG0bhxIwozSAub4bUnwdl5trZhpMQlrUXSK_TO0Zd0YSwaYzRmT8wHZWu6O5mlJxIevFhFH0fO7WGmbNnfmNvQf44gU6pULmlDu2JA-2xGZpriimy64IyNolRKJ-T0iVAz1MxXoQsaMjw6OThClPIPvYWsIjfIqA04-RgrxyUskSjJ27x9Hf6HpRI3QKAiEzkwrjiD4BmAqSi_x8UAJLpFOwdlv48bHnKQ1eyOWm0aSNlRU34c1S-gl-G6TaxLC_h32mqAsyHTxmODdSvSrX7vjmYPijIKK_4SXiBc3rsBX2t4PftXbecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرود اضطراری ایرباس در مسیر استانبول-تهران در تبریز
🔹
مدیر روابط عمومی فرودگاه بین‌المللی تبریز:  یک فروند ایرباس A330 «هما» که از استانبول عازم فرودگاه امام خمینی(ره) بود، به‌دلیل نقص فنی اعلام وضعیت اضطراری کرد و در فرودگاه تبریز به‌سلامت فرود آمد.
🔹
تمامی مسافران در سلامت کامل هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/463244" target="_blank">📅 19:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCsO4r63qA2mN0hc-h1pPViXhKvRcMGOE09QJUJcb4PL19CJSq8UIJ6BlkgYodnGkyN_sn-miop7TTNWCxm1IPBmzY4w_4sjHnOTd55dHZwyFFkE4UuD9KFwW7Csnke-uTS8GUSuzzDbp8UhbDDy46HAB3F-c201du_W2fYtqpxp1IGxqG_0IoMpN0cv8-3GOxBdWWhAk5rtD-xPgjEdvyFXCS7zGdSZRRtqUM8aQjinmg5eV4RHYOX5zHXt4kdo4BqzAdqZlp0TCIliCrganNLrKWl_nieBUdsz3caZy6zFhV86iwyc88dlrnvkV88tEXe2ia_r0hUJn2ZleZp4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌  صهیونیست‌ها یک بیمارستان را در جنوب لبنان آتش زدند
🔹
رئیس کمیسیون پزشکی پارلمان لبنان: رژیم صهیونیستی با به آتش کشیدن بیمارستان دولتی ‌میس ‌جبل جنایتی جدید به کارنامه سیاه و متوحشانه خود اضافه کرد.
🔸
رژیم صهیونیستی با وجود امضای توافق آتش‌بس با دولت منفعل…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/463243" target="_blank">📅 19:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da305b137a.mp4?token=gmGOIPxeRPX8fZy3qA-yR4BI77fPka7HZnZkV7EKCdbeqXXVETVLJqFHduNXiRU6D0gHAMyOP43AiAXDkgwh7Eg2Wkwa9Icz7aTVlPSxhyQUwh3-ja04PpUTWeJv8kZKPqGik-JsWUTHx6F6o5ofv37pjepXxeMisNIPc_DQ1xuA7iPpROkcolNq3B4GhAkrFpVYonxDRaRsjUDtLqJ82nSIAKsR3SupHdfY96WPln9zOb5XJ4xGHlucdtAJSFO5rHysyOlFLomwy7ieF0sDRzB2J5v_F1kX3nIBF0MA6GtDUhUg-g57ax3VoLdBiqxF9pjM1xfMBdCwk9mPA97pDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da305b137a.mp4?token=gmGOIPxeRPX8fZy3qA-yR4BI77fPka7HZnZkV7EKCdbeqXXVETVLJqFHduNXiRU6D0gHAMyOP43AiAXDkgwh7Eg2Wkwa9Icz7aTVlPSxhyQUwh3-ja04PpUTWeJv8kZKPqGik-JsWUTHx6F6o5ofv37pjepXxeMisNIPc_DQ1xuA7iPpROkcolNq3B4GhAkrFpVYonxDRaRsjUDtLqJ82nSIAKsR3SupHdfY96WPln9zOb5XJ4xGHlucdtAJSFO5rHysyOlFLomwy7ieF0sDRzB2J5v_F1kX3nIBF0MA6GtDUhUg-g57ax3VoLdBiqxF9pjM1xfMBdCwk9mPA97pDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ژنرال بازنشسته آمریکایی: من به راهبرد امنیت ملی فکر می‌کنم که صریحاً گفته بود تمرکز ما قرار است روی امنیت داخلی و چین باشد. پس ما اساسا در ایران چه غلطی می‌کنیم؟
🔹
چرا دربارۀ خسارت‌هایی که در جنگ با ایران وارد شده، با مردم آمریکا صادق نیستیم؟ احتمالاً صدها میلیارد دلار به دارایی‌های ما در آنجا خسارت وارد شده و مردم آمریکا اصلاً از آن خبر ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/463242" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463241">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rV5lv4Qd859a3ALXtRk2HWaKJeS9EIj9AfjvEQT1pktl5XHQ5vTSwRocW7_68yk3_O-tH_tvNloGbRffsX2cuYgiTy0wm27kzbck8xu1XocVTxakA9rpIPh41fiOsCI2ZwAdf0J6z7dEn2DvGmVT8l20erUZ05rS8qqtWzPle8OcR4fcT1FSqmoV-QKiixMOPN3XhtvrbANKDYKM1gU1Vv8yQBkMGqBJCfdWiF-O4rrBmWFVs5bwC-quc6zrQGUdMYkEgYLw-Kl7d8VwXJrATyEsu9KwzfLWdnAfwMUWVaxqfiAy8RXPFZe3z7lpx7I5rMfGk5tJh3RGH144ehKd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور بازیگر کشف حجاب کرده در شبکه نمایش خانگی
🔹
حضور شبنم دادخواه، بازیگری که در سال‌های اخیر تصاویر بدون حجاب از او منتشر شده، در قسمت هفتم «اعتراف می‌کنم» فیلم‌نت، بار دیگر بحث درباره معیارهای انتخاب بازیگران در شبکه نمایش خانگی را مطرح کرده است.
🔹
هفتمین قسمت از مجموعه «اعتراف می‌کنم» با حضور شبنم دادخواه، بازیگر مهمان، در پلتفرم فیلم‌نت منتشر شد؛ بازیگری که پیش از این در چند فیلم کوتاه و برخی آثار سینمایی حضور داشته، اما بخشی از این آثار امکان اکران عمومی پیدا نکرده‌اند.
🔹
با این حال، حالا حضور او در یک محصول نمایش خانگی که از فیلم‌نت منتشر شده، بار دیگر این پرسش را درباره فرآیند انتخاب بازیگران و حدود نظارت بر چهره‌های حاضر در محصولات نمایش خانگی مطرح می‌کند.
🔹
«اعتراف می‌کنم» مجموعه‌ای اپیزودیک است که هر قسمت آن داستان و پرونده‌ای مستقل را روایت می‌کند و با حضور بازیگران مختلف ساخته شده است. این مجموعه از مردادماه ۱۴۰۵ به‌صورت اختصاصی در فیلم‌نت منتشر می‌شود.
@Farsnart
_
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/463241" target="_blank">📅 18:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463234">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lxUtV0vpPPNqDZdxrJjtm6gvTHSOCoESOewLfXxLOCK5lHDkzI3frsNtC40R0MwTW3K1ZPhM2-wOQFgiLvZW6NZ45UGWUnkjAswO4InqDhu9K5caSeAj4i0sxNEv9zBcQkOLX6jrvuFknxq2-K7sbnaEupngBdi9xfamiE9Om_MFPzJcuu_4Krmt0w05zA9O4NJSkjJWMaAwKeW17ia0W7LjgtZmCQxLN1pKnIeymdY12hKKWeBPnF0RbcGmm_oz_86B93j6ywkfc3GLHjoGcuVy5E80PTJljOOGbAI9a46TdW9IpspHqrcX97XYWcPYNoN-MMthFezW_TP-vNp1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bZRBSE5W6Un0V9kiT6kCOcGBAg4wUM1zECDrRrHsRawT-r8Pcvz9gwquXqEn53smVbweMNhACSYFdvvq4OunjR9uqtJ9E2IcBe7r_Vb-BYf_lChppFXwj7DdRubMRDbYY6KJB9h2zQG0kivdDpZ1m-wQ93PWpHKIEGKsp323X-tAHkS-jlLBhjHmvLXeaDGs8F3-9-3eRHa54oT1284VxMfQANyfaaci36t-xUyZLRIXCFmRHYnWCJ2l_T1IRuIadYldXf77MeohQTeV6XbXxMWj-awCD2eNS3-67LPOEH5_il2A8Lfa0Y5nFVErNNs2d8BehAvEQcf3kK4XS-FLXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRr8u8Q59drg4Wy0ZS82bIwG7kotAWslpW8Flx4OmUGnYksulJpIvcAWoYS36aBSUSQ9ti9Gq73kMkI1M03eG8nsGxYWR32CUtoAGoKWHWruQ-rpjw9o0vv3TYDFXvNtAAOo2O_Mpn6hu-uuOQ13FvUw-IF1iRJuh6n5UY3PbKrrJkuRDDbEGa3MNaSGtjDOIZXkOvb52SOealpQNDILEh4t__wmWyp-sE2PZ9l9Z3hcD27FPQKT_fN982LRPayBzyViO0WpAMlgkYtiWvg76af0e5IrBoucp0W9CWxLA6565kDhNBbohxKq3ai2T7Z39g8Ro_SuS8yKSXkeO20iuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pcBaMFOw6LMcKk8mWmrSWe-K3889zbCcl4NhFeR0lYQtXnTZSRF8KxZ0BKd4HpnVnbhG6LTJTZyh_ZCs5I3PyBOsPifaPZbjKzOytXugZ0WMhF4L8Cwe1OQpFSCIvPplblwAkFyIqtw6LHe6gVBprvBiuz00wqgx2UaRp_8ciWRXNftjqvxub1dMIfC5geL5z6uMcs0uuT3D6zQd5yPk4gquGo1NccJ8WepfpwvWGYAmouT9xcioSm4gdz9C1E3drPEiRerQ-scP00bcn5oFN2tBDwRIHVeIiPWDEyfjb7GLK60LzoJQm_uXptbbXacKXEmKdFvIsb45-ZyoOBC7Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MiwlzH4LrnUf5oHCR_fsBo4ilCWw6eQHpzZ3lb2_6sTOOtK7znxEFuQS3Un0pAQQr9c_KY6XUzldaKmS7oClR8a6fpjbckvihkxd8gniN4MSNZ45gawruFBjlbnbtSGqPoM_L-g7XS4Y4L3jcGBOvIvgRhnX93_wOrpHsOspzsclzAQdhC2c9or95u7CMiW3VvZdmtFLEoc5I_w-EwP9PyEHUWMMCDAwAMh-kHdMpVk73uGpMwr5Z8Dxc2gEKC8Jjj1LYUlgFF7rMjMMUuwMq7r_FyhOUXgSicbAx3ei5jmE-4PhDFNWLh4UJ32uDgyLBgRNyzuH6UGamWFycnQ-rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ABu9x85VLKxFYkkdnHSpxqPygvNitAvMt2dmZ4ecE3gTgMN0iBCTofKIZtagoLEp-3mLzOfMIcl0CrwhcksupEc7Cs6Qbx_A89eeVWFrglrTBt1QfNJNbctuS8wWeDY15c3u-48x8ozV5m1MW69sCQcTRX_C0wjs5GGiyPpLrlW6nd0ouLNu2zkIU3cRaiMO3Gmat6q1GuIGPh7OBgnpTGqA2GMe8SQm5Ht4pH9Xp8r0ToDSNt0qP4GoGltF9B4xSfc2f9VmbpeLH-_UvYOx9FQn9NCu-XeEtXnJd_FRwWZXlXs7VTeofREqIPn9ri0dQc3L3bwiVr2QBpSkXGA4Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pUsZ0rYhvMBqLyMDMA62cIWS7ctKJKYwxHVOsbD_35YBO7pnDmQNWWrtQuWRbCYh-2zeBGnH4WfU9CYC0WJdnc48V3r-IQcZX72VMjrKG0d4zMQIQm-Tturlz7EmulgW2Szk2CCUiu3IwqDBWk42EzGlVySgsUQLahasBomkDLoLgzpu9ecGy81WFQFfhS7wgN98KDQ7fMk3I6bq57sd81zUXMA_apwSoIEbbKc8ntnvit5eb4l_x1rXGBGcRH4-tzKYip83PFeeG4HAkkl7zl-j562zlu6k-Yd-0b-Ri28S-kDPowsCvknmbaFjBLJe14qrTkGOaAi9Y8quXdFBOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
اولین مدال کاروان ایران به‌نام بسکتبالیست‌ها
🔹
تیم ملی بسکتبال ایران در دیدار رده بندی بازی‌های آسیایی۲۰۲۶ ناگویا، برابر چین قدرتمند با نتیجه ۷۹-۷۰ پیروز شد و به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/463234" target="_blank">📅 18:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463233">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgMjpv4Y2vWejdwu0CGYVCZAS4CYA_ejEp-t-huX_5XRIQ5SmFmdjcFNIQgdbpBtPhaQ7Q-Rs_GTPROI2tHreuYtLl2DjwArHVMrLhNqEIdhS77sXqiG8w5xyCcMeRkstGlrtNJV3VuAZFrJp627ju7cwmH_0tMA0KxEGrwN8uhO0Y-Fuaj2eecDUgSsHslS46EcEeikZeY2qBlvyr8w0zndejDhSYeYQz1JXpnorq40AuxIoab4qXSTx7_ofzG0IbPYdpD3p6H0KTFLMb96OIErZ1Dy1DL9vHsZq_cz0CAHxaofRT7M6cueY-VhQnPbwuOn1XS-cmzp3lmM72Cf4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور کابل‌ها از تنگه هرمز منوط به مجوز ایران می‌شود
🔹
نایب‌رئیس کمیسیون امنیت ملی: مادۀ ۱۰ طرح راهبردی تأمین امنیت هرمز به زیر و بستر دریایی، ازجمله عبور کابل‌ها و تجهیزات انتقال داده‌ها اختصاص دارد.
🔹
این ماده در یک کمیتۀ ویژه باحضور مسئولانی از وزارت اطلاعات،…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/463233" target="_blank">📅 18:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463232">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsrlRF_XWCvVM2Voi56JDBvf0A6w908kQDgUtMrHTLNHh3JekGrVXVB4CagdcAup2zYnOaRhcnpH0G017kA9SIwprAHiZrb-nTZv867owbFC6i0AWG7e_Yw_wK4QXu31yE6v-1vGZw-oitof77TQQJESWyGtXj0ZpWA_sxlQhnai1jEXwwHYfqgQ9tum0jGW8Hp5MUb92OBnJs6H7zuwrHIGUdbdOlJuxrXAWSGmOE8j0Vo2bQb36Llimp09LrNuNKAK_7_5yk5adFyJ40gpVf1qgf-tZMejywedj4H-AqkYlzO9VKOa2eE0GDALAd2ES1vpD4tttqM-4H58RjBIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش قیمت موبایل شروع شد
🔹
بررسی‌های میدانی و اظهارات فعالان بازار موبایل نشان می‌دهد که با بازگشایی سامانهٔ ثبت‌سفارش، جرقه‌های کاهش قیمت در رده‌های مختلف قیمتی زده شده است، اما این آرامش، همچنان به یک متغیر کلیدی یعنی «تأمین ارز» گره خورده است.
🔹
بازرگانان اکنون برای ورود کالا به کشور، ملزم به استفاده از ارز «خود» یا «دیگران» هستند.
🔹
آغاز ثبت‌سفارش واردات موبایل و عملیاتی شدن واردات این کالا در قیمت بازار تأثیر داشته است و به گفته فعال این بازار می‌توان گفت که قیمت‌ها بین ۱۰ تا ۲۰ درصد در بازار کاهش داشته است؛
🔹
فعالان بازار پیش‌بینی می‌کنند که با تداوم روند کنونی و در صورت رفع چالش‌های تأمین ارز، نخستین محموله‌های جدید از اواخر مهرماه به ویترین فروشگاه‌ها برسند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/463232" target="_blank">📅 18:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463231">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/st5VHHyj6qi_u50w_hI7-aLk_zPlcQDAt9TZU9sKowqt_e2bp_osN0fLX3ShNM7X_sJKQh76z2KM97NCP9r-k3sz7mbZbGh6vAIAyjzR6LpZgKWR8P6v41XcSyb8U1dYpsmPiJInX5sowR4ME2tDls01KLtdhz3Tzn_Tep185S6eF9CB_tDMyiI3kVAOu0GRCJnUNNneAx5Vb7jkkMzhTqMW30_2moPFaNAjdPPAI40w9ljDF40q_Crbed1f0wUPgDc4gSQYI03m5soxQvymAbGYazkqBZF2YqzBfd_FQbCkJU5bEyp518BuSTpQNUyAQ9BHduRz1tV7GKce8DSMmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد حساب‌های بانکی‌تان را اینجا ببینید
🔹
تارنمای بانک‌مرکزی برای نمایش حساب‌های بانکی هر شخص حقیقی فعال شد. افراد می‌توانند با مراجعه به my.cbi.ir تعداد حساب‌های بانکی فعالشان را چک کنند.
🔹
طبق اعلام بانک‌مرکزی در آینده امکان غیرفعال‌کردن حساب‌های بانکی…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463231" target="_blank">📅 18:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463230">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea0fefff2.mp4?token=spBduvKb3nh1MoA8Mq2WTw5ApKpdPet4gwgTvFtZ6Bom8sF-GcyNZvnQ7bJhGuQ4H3IyhOqcsrroFeSo0aj3zBNINbXcbWOC66CZv4vRu1HGbnX_mrGELyNyE7AJRssdWYkILmLwRzyuxjoKRHA05VtoOeW1SttYscguBx1pWrZvtiEe7UGSdcpo19yf9o1V80B_0znaHekKhgxFwonYx4koeW7uLw-du_ME7tQtM1q7PKtafPX0MLR1NoMg8ieyT-AgCcILr8_7zJTQVCSo7i4Z10z8suhQTxdfAFGnHgMYg58p459XLMNRk1shwfhqzxJ35mjlmIA5AMIYB_gw_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea0fefff2.mp4?token=spBduvKb3nh1MoA8Mq2WTw5ApKpdPet4gwgTvFtZ6Bom8sF-GcyNZvnQ7bJhGuQ4H3IyhOqcsrroFeSo0aj3zBNINbXcbWOC66CZv4vRu1HGbnX_mrGELyNyE7AJRssdWYkILmLwRzyuxjoKRHA05VtoOeW1SttYscguBx1pWrZvtiEe7UGSdcpo19yf9o1V80B_0znaHekKhgxFwonYx4koeW7uLw-du_ME7tQtM1q7PKtafPX0MLR1NoMg8ieyT-AgCcILr8_7zJTQVCSo7i4Z10z8suhQTxdfAFGnHgMYg58p459XLMNRk1shwfhqzxJ35mjlmIA5AMIYB_gw_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع عربی: فرودگاه اربیل هدف یک پهپاد انتحاری قرار گرفت
🔹
لحظاتی قبل صدای چند انفجار دیگر از این منطقه شنیده‌شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/463230" target="_blank">📅 17:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463229">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNMDu8Nz56aIbXBHGiOMVIypgBPkJuNvIeHM7NL8m6Rlyf0ah0uAyt6X0YJY0xQKGSvbyFVtilU6jSuPlXOdxpEm0xlaLHQ-3cyU1eTRN2aVI1Qe2nkNtpVag4Y8ZHbIoLRHE_F6IhZf13kLa7wgnS3mPLpPYQDsk0UuwWgWMjvFY8AVYJT4oIsQSXmupSp_krPy2nj3vbbA90-t0C_yqtVJZagi9Kw_HOQAb5-GUuWnkC8W5bYgdmh-teRmFepKpTaqjUo6WUD48J4eb84hBWDm9sIuv8mG3WmN-TCQGk4zRGdvkiAmmlVQ8C52ajKu9n-QBScNjClu_kc85Kp3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل تراکتور: بیرانوند فعلا بازیکن ماست
🔹
حجت کریمی: اگر سازمان نظام وظیفه اعتقاد دارد بیرانوند سرباز است، در نامه‌ای این موضوع را رسماً به باشگاه تراکتور اعلام کند؛ در غیر این‌صورت بیرانوند بازیکن تراکتور است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/463229" target="_blank">📅 17:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463228">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbEdG8etxK77HbfbRjVBm8-ZVzIQE0rG6JOU_07nNEPCY713Wehyxzp_xcvk9G0siimO9aNgsjlyhVK1xgSWA6-9ZQBNKh9rJK86IqVz7UyDURdTg_-OJ2ZT5YT_XFZxXc79pZElUxJKfnnAa-MsOeWAD_U3B0_mOLjOUsw_BnXB5Jwd4rNdf0CciFdbCdt1awfJgzqsIkUgfiYd8xh8Hni1J-pkE15JaZ9zJc2yGSxm8mW2oO-UqYvhyKKemY-0wm9csW27KrfAJ5b_jFWIv7KQk2hZrHosbrhn2bBje3Ak_aVeE7qO0Us0oCeqfbqo-xTSvaN7NrS2fjKRabRAYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در منطقۀ اربیل عراق خبر می‌دهند؛ علت این انفجار هنوز مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/463228" target="_blank">📅 17:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463227">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75282217c2.mp4?token=hy5NqAbB8VWaQz7EO_1tiKBLLE0fw4crtVHAjE371HGgjjC306zgT2b0OAyJeQKBj7gZK26B2FttcHt7CLlzjiCl4ITABd3P_-0tRPaFc8vvztMGD1ltlDF9w8RldxRw82yGmOsGauTalkJ9V2KfBncFzHpA3AuWn2TKJddD32vxUkfXvwx9IfkOA1auVFWnAyxyfYYqTsJ_QKMROIX0vjPsDB584KTGnYjlXVQMAJNr2ytOFLQU7FnDRs8RLX3risX2X0SFaKY4s4c7xn4nwwA0V7qv-T3-FjbUkUpJh3rF1NZ-rWfCw7Uw3v993acgo05DMYzxJGQkxOPAkwhnSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75282217c2.mp4?token=hy5NqAbB8VWaQz7EO_1tiKBLLE0fw4crtVHAjE371HGgjjC306zgT2b0OAyJeQKBj7gZK26B2FttcHt7CLlzjiCl4ITABd3P_-0tRPaFc8vvztMGD1ltlDF9w8RldxRw82yGmOsGauTalkJ9V2KfBncFzHpA3AuWn2TKJddD32vxUkfXvwx9IfkOA1auVFWnAyxyfYYqTsJ_QKMROIX0vjPsDB584KTGnYjlXVQMAJNr2ytOFLQU7FnDRs8RLX3risX2X0SFaKY4s4c7xn4nwwA0V7qv-T3-FjbUkUpJh3rF1NZ-rWfCw7Uw3v993acgo05DMYzxJGQkxOPAkwhnSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاب‌های جدیدی از رواق کشوردوست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/463227" target="_blank">📅 17:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463226">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای انفجار در منطقۀ اربیل عراق خبر می‌دهند؛ علت این انفجار هنوز مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/463226" target="_blank">📅 17:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463225">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/601da1c19b.mp4?token=R2-Vbdv4H5trCXQi8cd4fcU3xtSvSX-K8Wl3Sw7wpqKQPEKusCH6_J4E17dTE8frxVVKVE3H6lsZOZT3JmKtTX2w02-gHTArBVCJmBcmP3c1C8vCivZYfvBiKmXwLge6xVH8Y-j34NUYFPzNHY1pRWWs4MapUfFAEKK9Q3zkLa4OjHKefxIB-43bdK49FwGbflG0LOzQGj8JRfGArfBeaGLOJ5u8gBYF1SgqLh6GD0NWrMy53G8pdIYq4o3IEbMDktuyL4Y4bDsXH0xmTgXtWRsqfG8Us5koo9db2apkhR2BdXfWWFl_X49-l4goIryGO0VxBqesPvuQD7aRYB2rbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/601da1c19b.mp4?token=R2-Vbdv4H5trCXQi8cd4fcU3xtSvSX-K8Wl3Sw7wpqKQPEKusCH6_J4E17dTE8frxVVKVE3H6lsZOZT3JmKtTX2w02-gHTArBVCJmBcmP3c1C8vCivZYfvBiKmXwLge6xVH8Y-j34NUYFPzNHY1pRWWs4MapUfFAEKK9Q3zkLa4OjHKefxIB-43bdK49FwGbflG0LOzQGj8JRfGArfBeaGLOJ5u8gBYF1SgqLh6GD0NWrMy53G8pdIYq4o3IEbMDktuyL4Y4bDsXH0xmTgXtWRsqfG8Us5koo9db2apkhR2BdXfWWFl_X49-l4goIryGO0VxBqesPvuQD7aRYB2rbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنگ پیش‌بینی‌ناپذیر برای آمریکایی‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/463225" target="_blank">📅 17:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463224">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq_GXdIdjB4Jjz4Xb2yatEz1d0E52AFjKG5-mRRgR3jygCqTjBrqSJVSmxZhh1TdNOt0OlxyqWo7LkyYf3RVtoFn3qLy2MxNoYJsh6-y3xOBlxvvPMGFYxhsvW0VnjwgCgIm8qzyVEvspBBTjrgrSFp3GkcXkfVm8gsjqCmA4eZ6zUH2VY9Ud0-1_bTc_gFVfCGWWtdNq5Xf0IYGB7MNGfCUYFohy64pdchLITIgUph5ai6I2LDoYrmOZd_k_VAFRc9NrOLDODYKd4Y4giAusXiKedYl4zxen74Qs1tDUrauv0dAVHTEUDf3TKZTUA6gBKVzC6TwvChvF-Otu8KAZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای مامور نفتی آمریکا در ایران به ونزوئلا باز شد
🔹
با قراردادی که میان دولت ونزوئلا و شرکت توتال امضا شده، قرار است که پروژه‌های انرژی این کشور به این شرکت فرانسوی بازگردانده شود.
🔹
توتال همان شرکتی‌ست که با خروج آمریکا از برجام، بدون هیچ تلاشی ایران را برای همیشه ترک کرد؛ شرکتی که آمریکایی‌ها در موردش گفته‌ بودند، «به توتال ماموریتی دادیم که 16 سال به خوبی انجام داد.»
🔹
سال‌ها پیش رئیس‌جمهور سابق ونزوئلا ،هوگو چاوز در مصاحبه‌ای گفته بود: «آمریکا نفت ونزوئلا را می‌خواهد، تاریخ این را ثابت می‌کند.»
🔹
در زمان او قانونی تصویب شد که منابع نفتی ونزوئلا در مالکیت دولت می‌ماند و شرکت‌های خارجی نمی‌توانستند به‌تنهایی مالک یک میدان نفتی باشند و در زمان مادورو هم ادامه یافت اما این قانون یک ماه بعد از ربایش مادورو تغییر داده شد.
🔹
حالا بلومبرگ می‌گوید که طرح ترامپ برای کنترل اکثریت بخش بزرگی از ثروت نفتی ونزوئلا منتقدانی دارد که می‌گویند ونزوئلا به یک «مستعمره منابع» مدرن، مانند «جمهوری‌های موز» تبدیل می‌شود.
🔸
جمهورهای موز، کشورهایی از آمریکای مرکزی و کارائیب در اواخر قرن نوزدهم و اوایل قرن بیستم بودند که شرکت‌های آمریکایی تولید و صادرات موز، تنها محصول مهم اقتصادشان را در دست گرفته بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/463224" target="_blank">📅 17:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463223">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">۱۰۰ هزار واحد مسکونی در صف وام ۸۵۰ میلیونی
🔹
مدیرکل پایش طرح‌های مسکن وزارت راه‌وشهرسازی: درخواست تسهیلات متمم ۸۵۰ میلیون تومانی برای بیش از ۱۰۰ هزار واحد در سامانه ثبت و متقاضیان به بانک معرفی شده‌اند.
🔹
حدود ۱۶۵۰۰  واحد نیز به دفترخانه معرفی شده‌اند و در فرایند پرداخت تسهیلات قرار گرفته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/463223" target="_blank">📅 17:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463222">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPLbl35WbJdZuML3fsH4WjdiHSsVupm9SrFz8zwv1kvCfBBVwfHzjgFYchuJAilyWKTJlkFVOX4e2Y4GDyfP4Mgfmk_MxIjDHlw1q0JGRIBbdC_YhAcsssCaOCy93HR9GtR6IgUngpKq9ZuTIqNaDactttlD7XXgNHaaoRsY6VqNzW3aQ1RBSQSp1OrwufrCUoFbc3HfsS5SBSWvM6TKK2pTuX8-tHzl9n7r69vxIDnRz0mBxK4sU4TCh8uTPgQVf4tS2J20KPGqAoNwVT52p_-T6d2WMH4-mSCCFeQ_X7V_LIqxlJ8IQnAVPFMRkEgensv3o4XrhDbOYvmIgOI8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری غیرعلنی عربستان با چین برای دورزدن دلار
🔹
عربستان اعلام کرده از پروژهٔ «ام‌بریج» چین، سامانهٔ پرداخت مبتنی‌بر بلاک‌چین برای کاهش وابستگی به دلار و شبکه‌هایی مانند سوئیفت، خارج شده است.
🔹
بانک مرکزی عربستان می‌گوید عضویت این کشور در ام‌بریج صرفاً برای انجام تحقیقات دربارهٔ ارزهای دیجیتال بوده و پس‌از پایان این مرحله، مشارکت آن به‌پایان رسیده است.
🔹
با این حال، فایننشال‌تایمز به‌نقل از یک منبع آگاه گزارش داده که ریاض با وجود خروج رسمی، همچنان به‌صورت محتاطانه و غیرعلنی با این پروژه همکاری دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/463222" target="_blank">📅 17:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-463221">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=qEGZVWsurcr43Df3gDd8ue8q8oAHPoL-7G005C28mGDOj6X9Dufi-hZUjTTM7n0ChKwv0iG7YbtQQ6B_fJGgQhssVKbXcJZziavzfkaOEza-stuUUzyxuhvEsRijUQCe6WikwU43I-iQUCbTQq6U_aQ6WL7cNygiW0iCTY8BiVQ9eVxjQdrqvjG_G2GYd9qiwezo3C3q8JI3Wji4zRg3w3dJQtxCDNhOrCMO3_1_GSz-3Nzvrt7w_Wp6id4OrP5Dk922sYYsVqHjLjwBRsJwpCzhPxy3NX240yAEegOgIebu-Ov5Fd_iidWsuzRbDFrXklzzyDkwR-oYWshKYVeVVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d8a658f3.mp4?token=qEGZVWsurcr43Df3gDd8ue8q8oAHPoL-7G005C28mGDOj6X9Dufi-hZUjTTM7n0ChKwv0iG7YbtQQ6B_fJGgQhssVKbXcJZziavzfkaOEza-stuUUzyxuhvEsRijUQCe6WikwU43I-iQUCbTQq6U_aQ6WL7cNygiW0iCTY8BiVQ9eVxjQdrqvjG_G2GYd9qiwezo3C3q8JI3Wji4zRg3w3dJQtxCDNhOrCMO3_1_GSz-3Nzvrt7w_Wp6id4OrP5Dk922sYYsVqHjLjwBRsJwpCzhPxy3NX240yAEegOgIebu-Ov5Fd_iidWsuzRbDFrXklzzyDkwR-oYWshKYVeVVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نویسندۀ آمریکایی: ما از منطقۀ غرب آسیا بیرون رانده شده‌ایم؛ به این معنا که پایگاه‌های ما دیگر کارایی ندارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/463221" target="_blank">📅 17:04 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
