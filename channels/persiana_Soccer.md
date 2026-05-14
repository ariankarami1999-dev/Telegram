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
<img src="https://cdn4.telesco.pe/file/kDu9ufzvlI3rt3dje5IZJax-ydP6l6mp0esL0ePGkDNzkoFK4zmFaR31mEXu9qKFRbj4_3Sr9_QJgPumWmqv4VSfZRnwGz3ITnyieun4fo0ftnl7AtBs2OcjmhbuBIngYwzD4wAIOS13sG84XWQtp6ADwqY3N1PTPXEoytnjxJHRnXUWHButlkg1kM62vibdP6rg58B1mKc_83soObx8TttZYzW18PY1y62NcC4WHVKON3YA13fJKWcLQlwbxU0mtbbLOkoXABco-vB3EWj1NtWD67kxnUjm9lIq2usaxDulcMCY127On5AxWmnDkqYa46JVu0febvG6yauABw4ohQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 211K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 12:58:16</div>
<hr>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCdyUQ1YBOFLA4N6dfEO7SW_fZuWFcConm1oTJ46BUMO__yHA_Sf1oqLUDQtcW8EiAWnwIGdcZqy70R4-GbWMQLCbi8Yp03Ykwu0hMCqRLr1HfpbsVWdOwrpb4aqF488FpAnDnzJx9FHxgbVjlF8p4h9t9aBKVYW1kBowW0HCwFp1RVHhiCPKb2-mMC9uNHhy7EHEU9M3Wnboijaua3_bBj-ZMMzbmDerxt0fMOP3LZLcyR6mqsohIBexhtODx7X_lKbicoAnUvOaHzcAsa-4hj1S9Y-emSkcuc9yCgSnVMs9F10t-F1cGldykqfvZ5rMt2OACsWE0_weIzSc1OzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aj-veqmFkxbU7tgEThin7mBozcSogSB3LQXkTJ5icqIiQaMQINDwSOdm-tyEkAmGSPBct-bgcDS_41aWy4Z1gFyjMAe9w3JtIZfEpiaOafYeA79Goibog1MYKJUOoZrVLGgo2ivjzoFaFN08q8-l0c508p4HRfqovj9KX1BlG8HfzJo2t84zQt01qatm6H203C-5RXPcmKLHYNT5Ileo6bKnqbrNqwPw8OSuzxOURv3FPYKMu6dQ-M3D7tsv8i__t9roAhIEVQ-zNdQgnxA-xEWiMpX2f-o6IgKXPIWb-g0hPsE1xUjHXIdfC3S39KgVZu_HsDy69Oq-vURNY4uHRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFIapQtA5GAP-KNKA4Evm1J4iZD8mtpog9zGNtdQ1NPNnsT-800yHk3S9Ez4cx5u_jaflbRXz5OS9nYbbaW1A3DZAtkZwvWaiM8cPV0ncrfx235rg9P872fWzZsXqaYiqYzb30lrO_6r9U1WtGzVqKG3NBLAG1aeS-TspTYH9TqZmQZ-x2I0D0nuZTQZYNQ-k6uUGfnpGuoxmq2WbeGyGU6s7PMhBn8KqQGpn6jZSAQQ30ENyc6v0W3l9YhIjOdDIiFuhobFjjTa5RANvXBjQRifRoU08v035XNek5GVJweuGRQqO4oAUj0k1g5MoF5BiulfDIeDmPiMWIZyJghoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThjbyQeNHqMu79xJR43-BnU0P8nGmZ2EVQOmWeUROYnDnc9anhIqmwYY07A4Xv-YHrbnwOnQIc195FTdNAerCJ0PDDvpU5TcVekW8UP7Ph_LczDCsWk6IUqll1dTMAmLglcr7L2YGu0hiOqZ6ZbMmP4qQ89WAKXvN85qh6-6CeBM6C9JrE1nAOStakbH3VMUXqiowHcQ925FeiqVp_ZMlouj2ioHi60UsJoOy1EGsqD4ZN8neXorK-YtuwjHaA1hP4h56xTnqq6QLskj37KQ4Xp2QKEb2iHhyqmpMF72I6Vc4XltHoS6-2NfLUyx_HX65JyIzHeAuRD-TorGmcP-ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFSjT3XneP1bPb5dmETDnWqc63IixHhFLC9juaNCU-LmovqXwr5DtuZqav6dW0v0jIYDNcCKRwehe2n2Wp6_-h4qS5ttYquc9_JGI1h1VmMtdDbFH84vvqPsfgvpw1xrai0WVwH_h843-cemfbyEZDrIOgIajPikDBul_YYel7pS5DRqWiTZyxDXgyTSHmKq723LixhHbpzPKeD2IqtqOfbVGads1kqXsEE7BLcFW0VcVhstdSRqReOVZ3FTFRRIN9KkNZddqWjS2PjXgGdmMsG6TRDfbJtKnEt_KHN8eZI-UFs5T8zj21tG8VlhXxAFPq5_1j4eTJUdcAwadyL-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vr0PnkYnw6ozYfDw-hax7ZMyYTpCWAmjudQoCTZZ234poz_rZfIU0cetvhm0ayxbtRWAcqYlokn9id-5jBRkYz4Kvbs5duEWSAw2l2gxlacP0Zk2VA2RU6x85-ZxoveAl3QNsZDLR_YKTFaRKvMqkM51i65opFxOMbe9GN2qF2qpPhJntB-RALhybappT94P4EjcIForNvaX8L_2k_hkbmdYozgZZeRceruC3-ONhTvfiwTQRAjzApE7Ycz6DFllZL82Dbs_L49JLPcRbtSzXPVJo9DHmZVQlk8H-zrpHqp1EjT6t0MPvBQk6ORb6LZ_aZZjbyCsPyYEsANxrmtFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGUYJYCeg01_GrUdQ2c5nCK9HvC-pDiORrpwvhatRkzu4zwz3u6JZxXkQtHYwKOSlKcKPKXuXDWbZVBa8TLdu7AYOj_L0rxCapOY7aOHQjcVw8HlI1ro44Os2fVJ86ony9-6KFeUn_QNOXxI_a2SFjxZeS2MEvcFdbpj26M9UYz2yxREerAR-82HLhVN5QcGt1vPDe95HWS5Xe0v8SYk_kHH1oufabHXP0wqR60v3yjC124X8SIZkVlxsQlvtii3APihfJWP2mKPVu1Q6IyGa9y_O1NdCRWph4oUOfnrBqzqtj8Yzwo1j-84xt196Wr85QLzP4wWQ6_mg93UwwoTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKlcARNib46iBTfCqticAV5QV_CBxZjumzVuQ2t1KjZAn8bgcAx98Tf_oFBU7-88rVoabYBeKqShj-mjlSnwdFajGq6ud0G5MXOa-ds9X6LibCrTYJyvI9rToIoWbi0Wt4Y6fugB2ckk1m6pFCYP7JQUCDHmZE80iXRditjW6s0n3-wvCqG3U5wzy_z_kl4vgNZJLquOoHOEXs2y33hGz-VILTuSP104a9ZfUNuSRz3xo8HjZEAgYlhvYE0rtu9cSVejESjGi9-ayRVP6pwGscLqPj3Tj9BIVemrxUYbOvgdhZWaDapA0yGxfS99NEuzQShu6437n0c6iwdpq8rzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=YbZciyXD_KI3AnlF1D9ZCd9P0G4nYi6YzUV8n6dx1cNqTQmCcyKF9BNQVd26M5eIUtTjS9w3fwbJ8TrcztgdYMck0zH1Jx0zqfSohUybTZn_XadSRgUj7tUCAHnm8kRUT7hw4zHOaWSQawnKe5FbYrVgkG0vyooa9V2y91pYSczsXFMaX0_3a-Jyy0jiqATZ-5hgq4SUCtLq1Q3llgv2RPo3kEWbO9JOW6IaS32u7iGJDQGkZipXGIRati_96HdMwyxyh8vo3EWPyl24RUN36hpAEOS9D36BA0Xk4F1GlP5cobTegNcBZgySPk2dVDP_Sp4Ypx0XrKYCxlfnzUbNPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=YbZciyXD_KI3AnlF1D9ZCd9P0G4nYi6YzUV8n6dx1cNqTQmCcyKF9BNQVd26M5eIUtTjS9w3fwbJ8TrcztgdYMck0zH1Jx0zqfSohUybTZn_XadSRgUj7tUCAHnm8kRUT7hw4zHOaWSQawnKe5FbYrVgkG0vyooa9V2y91pYSczsXFMaX0_3a-Jyy0jiqATZ-5hgq4SUCtLq1Q3llgv2RPo3kEWbO9JOW6IaS32u7iGJDQGkZipXGIRati_96HdMwyxyh8vo3EWPyl24RUN36hpAEOS9D36BA0Xk4F1GlP5cobTegNcBZgySPk2dVDP_Sp4Ypx0XrKYCxlfnzUbNPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvP8q5LYLh3yqr6UqXHauWPrQ5dWvoX2yL7VGc17TecPjC3yQBq5ue6uDAGbZgG8N2phG2OnKJb3RfHevkNlWokeELtoozFo_1dLe9NTts5RpwUEwDF8y326-j9okYI8Q1B-4Qnmyp7kF77tP2HK8EjmIy5gw2vsK_KwYmWQtgDCbAQ4JBR2whyAd3PZHxsWse3rPUsEVsDSwyFINu463uPdPT3zNRVDDD1OoWfxFwMblOLbAlX0dhh7T6GLSE2dyahk3jBdUlI0m5OfftpJub-Bly2MNNHOoV3NlwM1S_RHA1JDlpMlovEorLXh4epxHzRYIv4nWhV5-_hKcGvXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xv4MxdOj2Zj2CCoIwW0UayljEpy1l_FIzkgvF1m8NMP9o2vWdoUfNMzqy3LW1LmK4CuvVBRh7vhJIQLM2tCfrXi4adUSEp_Mxcu6XmHkB5iojTn84tL--oxZHvrKUQ_8bo6ktiSAFYCDQsioPVGkqzUG-BfTqCaBmyUB0XFsW9xPSQw7oxLx3OJ3jHUzoWtovT8WC1BFlvfAItZOBblW20gGuY2j6nc0M8hU3BCtKTLrmEFSppntYUAYwrSpnkHTum8v7Jg3ufn1UZdn8GJi5UGhmHJkh5t9jcEFw53wa20JBs_G-bJYs2yylSW6RmZjXlNuZR55pCMJuO0g_DZPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=vrRSd5peITwrJyZCZhy02E7AwYNz0h1zwoQFLapDroSXz4rO-lrLJPz4Agrmo7hQTOUWhO1jsYIej1yG_K5oOITin_UlrCh2z0sMy57s3WTGkmINZmHf_ZXKcvj3h3eCkwgwiEFMNoXtfgv8-NFbW6ENF9Hng6gP88D6hAb70nTqC07dit9SiLBOnbgvtbMffdONkx4uBzaKCI2snTSkHZVggubD4mIWwVEJXSXvijSIjxlm9lRsdtaMOPfVKtfggQyhX4IHaVrzKSvV2VIxKJbSy3A0RJXiR1ZfrAgrrlMSKk2DEHCmRyg-jlV5VRt7Xq4xF24XWz69bt_fUYRkLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=vrRSd5peITwrJyZCZhy02E7AwYNz0h1zwoQFLapDroSXz4rO-lrLJPz4Agrmo7hQTOUWhO1jsYIej1yG_K5oOITin_UlrCh2z0sMy57s3WTGkmINZmHf_ZXKcvj3h3eCkwgwiEFMNoXtfgv8-NFbW6ENF9Hng6gP88D6hAb70nTqC07dit9SiLBOnbgvtbMffdONkx4uBzaKCI2snTSkHZVggubD4mIWwVEJXSXvijSIjxlm9lRsdtaMOPfVKtfggQyhX4IHaVrzKSvV2VIxKJbSy3A0RJXiR1ZfrAgrrlMSKk2DEHCmRyg-jlV5VRt7Xq4xF24XWz69bt_fUYRkLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npPOJgp7U5iCQFk8H-KIe7EhRjpoXTwL_c_V97zfpjGLRXrHO1tXpIvi9ht3HvX-00s-2fUCIaEnHV9VgTj3rqxuOSEGY1NsE13Wxg0FIspBtjGiZwOCVnKbWEKE0vR0Bd4mumXne8DK_avv6SHupq1oP2wi_X_eKBwlYQid3yU5bSF2tukBeObMAFw7OJLJAij07yht51330nX-wjwsH6NTsshIed5I3BpeiT8s2jnBSIY6opsX3sKwpfmVBU7SmYjwhjQ1YzcRG44pB09IKqT3T4rDjqJyPSDaaTot3SZOTUAigNBxl3Vqtf2CtLDr-v2_lWqnoCNYyBNYoF8YnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ggu2WqGtdXFGUlzxjOnEmGrpIuPYmINqMOcLnIQ6uKC2Usn0kzGqyrGY6ttnDS5-ssNCo53HHlxiThRWK66eSDZaLoq5ViNH2SP47qdNTAL9h06e0MQ9cTTrpCMuIQ1sSoRZT81EoED0Xk76Qu_xDZsiqXuXefQqvNVh1Z80RHbhzXddnQObASrjGMId64Ejp8u8f7etqzwSiwQcvghdfAXOjdP0G2PJFhj_aOoGJUX1mFOZnNlcvhHTWlG4CYf_2njZfsrwL9ArwXoYe-igo1OOhPhPxcg5z-PeItUP01EKJqO5Epg3dkIeIioax8_ilGoT50bUyyzlAqURH9TSog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niqCgpKWx_Iz6PXuKXCHlilV9JKYvT4yJPLxiigsdMANZPbxjWhfx8i4SYWWWFBQvBVSMkil22pT0a6Q099XeBNmk31_lTlBq2gD7MaGcYKuOaPsTtZWPxs3hvLzIOpQY6S0A9p7cSiVecN-EvLMHmfk4EoN9Iv3c3ZEdnYYPofejn49qOb0hQoq_j7CbCR-3-VHawGb2VvDFzPUCDPq9l6KJ7sQBV_sBTxPE1i2jxBLePUuzjEq-GpYkQhaZZQlYh-gBURMRN5exlMatzZmq6dxjl_W05h3WlM4pw1sZjha7ZAHuT8hLgu-Ey05ysnebQnRuLysKNbz2VX8lccYaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0wlq72lcwngfc4uyNmQ85WgSqOEX6-qqhYcUuR3HjZTIAjNX-RNXRJMOPlP8Zt3KPx0SrPwhaZjP_BXvzzJzCP8EQM1LkwfhLAJSa4_hjd98G30aJObMPrfWfVknSH0Z1kqFkK4iLuygpA5_NEizO506Esw2u_UXd4iqOZ-WH6fE7JqgiThNYE9AZLhInjRexssNdZfeyQJZODgGgYX3nFBNd7IrX0dM_9v0vzHIqlmvggDT1gKELs-a7stQ9MCtrOrtGOsdFoeuad5345H6SAn00m8logvKtvMsqzox6lqriGncNy9EfEWZubOKY8pVNTqrdzEXn8B-Xj_gukobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTMa7aY9rz_JRcdTs724gTdYzJv9J-f0hxExZtS6JAflWRjRx5QgEr2jECru2FprjW3vpqSoghhRMexLkk8PHwy2XitWpcALLTGJfaj2TdxpBwBqKfmjaH42RW2zjtsPFeJgG7FJj2wogeySySpFJaHDtfumLN3zUBxFFDo8SpVj9cNOWd0WFJSBK-f9tUEVat2otvzlwmlxRfvBS8raOFuD8uyst05mQ2mnC1K8_6ChTC19VXHjzUIvam2l_YGXLg37QhhT_lCA1JBeSuCj2XWzwqpZjJT2tPxs4fJ1rAdNFoXtOK_Ki9IVyXpSo9M-PBYEpQ51vW8tdp0duOavfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jpx9X4yYicz_rX7fcEtyCcq84rjAPlJbpZMsNKQmPBSXUGtU0o1dmj85EJZuEpebtKsdxiNuuEW86VpAOneA3tonlayh3cDBMwuEHSTvrGNU4i76Tabx9XhQeujs353IgKqx5FgJVnj09UjMPXk2jEorlkxQMGbcMHpyPrOBXFbNneBjO8OYDf49wND_eYIBeoQVrSxvnWeGbdyumnMeVwFX9adfVVkCuf82TLlfTyRuUVE3m2Mh5_NmzZTr2wscjF_8bJjp2k5uP5cRzggUg1QPVvLMgEiYmx2sNh8b4stkFUF191XpNzJ0l8YW7M8K3pYqUT245IuEyPV8hAtI4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaTy24xa8fBDvDA53jyhcaLkqD7VdLbLlP9uEybVVXwNLYyeCf6M1HUnyQVxQJp12pWBcWIqlEvjT5PIgQV-HfAIgwUqHeBu1LghGESl34TZV4S-CNg827e_Ra5ENgBxOCPaRBTSLysSJOleWxo7l_tb4hH-EcVMXX8QWN_4MIXkkZNF7nu7cJXlnJsCjuNKfcb8P6ROhI3J9XBixnzENAMXAf4jR2xY6Cis8hGQyYQEhj6vbSQuHaA1XV5RDk0WGe-0G-Ji_R07bGgUK9W8Fhl5li0EpQGPb_77JwxsoyoPDdjUP5vhPfsM0tjqbicdP5mxC80WwI4fGJzU84M88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sM4hV8dTpywf8jD9QG5CEpJHJF0-lzPvRW_6KvrAsdlTjONCGxri-yLzFZa9ZUh6vNX7BgSEtZVi1K7PYhjn8cgPR8VGXKO3mguPas3XRexOcepV6qy1sExav9C62eXA6sYhc0orphYTLKbgyYAsPvchbTeUWOJya5VekQw-KMSYK90UJTM68tOz-s68I5vO5xU9-7N6F2JxlKqzxz91lLwE0qT0zjK3_bbMc0hFmwQgfPyh3LWm2jFlk07vuEdZQ4u1-thoEtWIjPjtp6u6MmovZiLMMdOL2iqaWVVGWtF6ks4jlYSmFoHa9a3eLIh0gWLfLXPV43bhN0tDLBcr_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPpMKXEj1AVpZjliC0Y0HwIMZJJ-0GIEd8JKMBa13snWj3jgQNokFOvUEv7AEjwNXgwvmaWLsqIK5IsszicF5w4tUxbu7HDEH9VscBsOE4ax-TuPU4UPuOYm-tvNU4J1mpL_FXs_CIAN5qNNwfpyMbFRjCB3IZ85VKJcnypWb8bwC_SNC6pp4AjFgey7-0w0vp_d_CAunDSeS0Is3FNErpfG5OOJdlNOXDpWorUuhtXJaLbLwzVt-dT8lP8WYbMaCUHf7EvFcOP-3wsDuP71AwXSO8ZObLn2Qc5ISzINQXfETcBghb-kxOy91mhctb7uu0WkFKPYstG0BAN0r3ZZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2OlVeWlSFVJ2e6Z5cUlpR6EKCyBOIFGMRpiXkdbnNMKK9BMoz6OEFYkQZHFxi84ZuqbYDqhLt1IwhXpLJYZbgrv4bbWuCmj_enQPt9RAzDAMBaiWyTX-eRD4YJseyWNZ835qhos_UmABUyKeUCmW68UJoXU2twibhjMoXE1kjDMp1p4zCjliclCMsZ_WK4RDEGZML2BpXi4TgdIDGLKYJBK0_XFqNfu40PCUepTXlzHr0mmffanDvmaF1jq4Kz6CHizXRnJS7hfEkBFBYF3Drq1EKV7Rb-VO3UjaMGoDdU4TT74_okHYI6L17YhNqncaYVVYdvJXc5tGFc7UTTezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCbs2jLsXfq_oaRrHPaVN0GIW__CNdcd5mcxErZY-SDNVhkh-2wiD6Vyxx8PNBta3b-3ztJT1eH1dpa86bawn7zhfe-rytyXIIVoI9bBYzAKghMbA22_gisvbrvhZh_3ey5x0z00ZsvgLGOhaqiZDJ6myAfbPcSooAokNXCMNYYgzVCMXVOBQz1KVHoofEQpUbpx4rFBi8rd2Gma-0ldIvrXJ9KKyzCQo8PG7fVdaMqOZr6Lfvwp7QSoi8weXLz0nHSG4lwoh0vDOPAKGh3P8t4hYkbnRUj4gdmFyNTLh-rp6NRc-G9vctIVWOEkNIlazzH5_iq1Dt9Jbk-DaRtnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdMBGXQBlU2IC1JbVDliyBJKoE0S0mffoWSGrY22eRAnF4aP6Y4wn6bdrO6Fc4xKRDnggF7MR8-zks8yu4LbCaJAPRMl5nz7ibHmXjXZmTDPWcuubGdyt6gzjrLMDCkXsKJMYfevTSha6la5oOxz5mVhn8AKr1-zfcK8r2jLDgHLW-CRN1fJJBYBsh-BbINO9RsBE9nA-VBxT81NZjGYV_iDIZ9BInEhjj8w1ko_IbZh5-FDkDGQlJVPdD-MoVVKT76k3ctOuSDn9aAh4Qutp5OJ_5oOfBV8olrTNxzx-cRU4Wh9IZyDz4uFydU_FWrnI-7u0Lc2wJ_nzoPzO4Acbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbPMPpuHCH8WfBt8Mwt3YZzpOIEfEYkK3SC2KjIhw6XTOhGXd9PAkiwdMd4Mw2BUi-uY6ksWmqfTX4UZDeB3r4YOarCLwIcy5y2I4VXL3_j7ojMzVttPP03VVYpj4FbQIj0KRbmMAA4uoHCXb4vclpBJAkXPMTMinfFfWxeTOWevP_4skb6vQWk7Cy5g6O78Ai2SQL4RW_B2dCaSr2lXOJuHZRWKFf7QICTzYL5G4IJMCFhRfrDHBrt5zk4WixPtieQAnvFVRWDFNXN_RpJusGdmo_b1Fz-YzS9-sR4cTWeQ1u9kba9vLvcSWJwvkKPjxFa3pUu6cpvwo4lDHsMEPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0qmj9tANNvXJUFFiA8roB3NWE8p9qGD5A5aw_oPbSW3iw1seI5Mzi8fe2wgiNjUPrEoScnn2V_F-hLpGXKQzyxWYiLvAwGsazkzIrYUkLFEG0QY0xf3i8EZYmylxUdm-QY9P4JETN8raPygGwRIU1gTmhhxoqwcCZ9pf7Ym3VDfT3-PfnJY0ePZNE8NmqX5axobk_f1cLmbmGLJYh-AbQbmiP6gXiYKyth2sf46sraOLtqOiPT6x3fsfWLrbVL6r9XMVxbiaWsN6lHEeXbU5AQcGp4hzDP-nR7tXCxgsbnALueR7SnONUSInoFje1q4azKqnLM81VbgCrlVzTHeMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=qaic_-9YRXUMcdXmGcsUkng5CgIuahquXFcaCHXHg_jLcnDq0-wRwhOaVc68uQrX3AmicEavo8-T7t6VA_qgwNrATcDeyKbNAffeuYHD0A3EehbHk2hejoKoL1IERaxyZwEB9poT8YDrN3CQGTOy7ob8zbTcJTKBHm8KHUSmZLDgom7YAwNGBTp4O-XB4P6OWbFmHjAExfjnXoX_e-MJZ0GgvkQH-YIWMLJ8pBheD2g39gL0iOYmVNcbOi-7z1jRlVSRSZQEzpQhYrvlBcbh481jolIJGYII9MWzmysUJ6-Sw6MbMxOKn46OdxKB37COJSXkgw50hcH1t8PapArYrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=qaic_-9YRXUMcdXmGcsUkng5CgIuahquXFcaCHXHg_jLcnDq0-wRwhOaVc68uQrX3AmicEavo8-T7t6VA_qgwNrATcDeyKbNAffeuYHD0A3EehbHk2hejoKoL1IERaxyZwEB9poT8YDrN3CQGTOy7ob8zbTcJTKBHm8KHUSmZLDgom7YAwNGBTp4O-XB4P6OWbFmHjAExfjnXoX_e-MJZ0GgvkQH-YIWMLJ8pBheD2g39gL0iOYmVNcbOi-7z1jRlVSRSZQEzpQhYrvlBcbh481jolIJGYII9MWzmysUJ6-Sw6MbMxOKn46OdxKB37COJSXkgw50hcH1t8PapArYrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJfI6cct29Jvscwez-fPlM2ElVxMfs2fxmprJPutz_llGrkj4wXgDI99rkd7sRpoI3wghM1r5kx5ae48NfOGRG3VY8utTqigh8ViXOeZlMKpUH-F34SHc2FcmLyzEh_KYG7Bgv2rJ2I8kKYjqPb-gvpIG02-XMW8OGU_seLTHMrwVAFdinLFKKqJG0G31dgmHbTKg8XDI1lGmDddWj1CHiguuVT__uWKut07R4JMBxbhem_bhtERE4rB4lNWfqzPFpZlSea5_Vch4N0l95tEiV5wJTA2-2ileue1zuoItv0eSSFBJDnL9v_0B4Tv3ySrAp0X5JR9IZf6HMoK72EkeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBpeqDxd5Qd99vYgDyCyWus3RiawJsXvGQEsvnd_ki2hEQRF0zwt45nr58ocdrHZpJ4rzKX2Lrxjs7HFj0eT1mmVeVOmAkLdarSYN1X-uacmXY75kTwDpn575mlpalQPKemluLPIuZ9kcnMkPyOFknct3UOytLAdNVM4atULjw32HRU-7WtrAZh5IPKgz_3S5VqOQ8Lmeq_CJKoXN0-SuPhd-CT6LE6vF-L_mYZpdiGCZUzz7cm_yXQa7gTk_ueucfqRJl3Ps94RVNcv6l-Wn8nxDUC2ggfgWkwLWzeyuaqnxIyPhJNRv35kQNKyo5KLHgEWl17CBLqVktLWRLD9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIZkq0TaIce6bTJ793o8ONOdLDzgJOr4og5RLcgaNYCY-0W0dd2h2Db4ibJi3uygShLkx6k9nxcl70Szkxk3ce5ay0lEp1sGJhO-4WPagO7uUvFOb1zL6O3Qu6fQ5ep3wGt3icLDnzKKtBhmxAYQR82xatvjrgiV8qS5z0hluMxkqj29bTdWVSIyTLXNqbqcY4sZSpBj5rEMdDFn4zRPjbSkEAaMHQwgPl4jPaeHAciNjVc4mQc-YkKPJtorU1tUm3lumiNUsHYJ5P0t8e2hA7bdAEOd-lpf4d5VrmSFNtTy_K8wVJRnvzaaQ3AgRO6QLikA_O9gSjAupw08mvCNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNdSv9zSBBLx8BiPmvx1axs_YWH3tlK-oFuMMXXJaE4U7m5e45lKgks4N9lkvxnBP5X96UD0R_xaN_94PhEKXEIQDwOYrPLazPOGLDJPmaH78WokKRBFtp6-DGSPM_FHC7_mV29EFD1GSqxT6B3M_CBZ_Q6g7hepLjl3iiwZwuCt-sJ7XMxy3Z9m4xa-dIlkDaLDkLgud6ma-AfHh2fJTJGoSu2aXr56qvM45dTbcvVOsLmFo54ETZyaYjynZp7cvh4SNcYtufYrkmgE0jsMT-CQjTuGzCR4d2QUeDJdtVFVtWPoVNwH7cXeWSAdnaeB8iOnHAPRH8EQNgPtQehFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7dnmLVLPlOdEP3Md0VqXy5ECfYKG6OuFqtTaswoP-CkB0XjBaySikGWXfnQGOilGpovBuwTX3q_Zij3OegDphY9IRdn_m1z4isVe7NZYi1Ub1tN_Fw3JbfpZ5IYsfIdrcALjfEHDc3EpgHjoUnO3eerZev0uPMDIY6YWgR4jHJPCx4rVGEvFYrjcUFurzbDaPWfe2uXw4oSqx1ouo-fnvhIcjrB4Z-6i-QaTbtzLG1ZDWBF1-nCpoR95WhBLooXioZ2-mka4tpumN0CG1jvB3olamvzcqeJB7qgBmfRo6MXXOBuw9XFv-y52f9oWJN6HWjYJB4JuoEY8JyYS0FGrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYYC_ttINKqjkRgrvIrOl4DcrIArFs69dhCc0AsReC2TNGd1nQb7y4daYMveCzBc6eGD1D3Ntg1VLHv3054UkDFJGFDpvOtGsWb6OeWE-RO9hydO9VNEsMN19TCF33Ywwtiaj8oqWhuzNhVZAt6mhsbPtWDSgW02N8pFurksJ3ameT2X-tS5cgfxKSEOq5jUhl_zNe1SfWQiDHr65EK6WRlzHhAt6F5KC8QbQ4KEXgVE52zMxcdKGYXIK2r-eK5cWkRL9ryKARvPMggF-OYjHf2GQYRc8rb-Am4OtOC612cNF0db3L6iRFxUwMDkPX1YVCcJsztjkz1bu72QUVQ02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxAYAmrGuE7r9FTfH999zuNke87WOJhrkefe-P8XxDw7vq1M7xrDDacHH8eck8iP4yneXxDiveZHhyDCQp2K8yuGYHWgw87HaHu7Bw0OdzX3AM3F5pCBQsQvKDOWe_UNrv5vW89A4vO3RcZYefqhM_66xx2hTignt3J_EF4vbV75Y1ha0nBggadHT69SITPv7nP4vsdTqY-f5rvu1-CDPMK7soC9V5y3cbk01JlUvCCtwSSWdEVkn016CYyvnQvhpZ3aCsXajMFTUzrmSKc-H8BvtrR3vpRS3D_ebPBkNxH_dehYzOz7Lb5Cryp3sBA485-J66__RcxL0dapOu3cSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4RAS0jdaTyDqTZBI4Sf5dlAWifvlUqjxFcJBvQhGZ1NPy_nveYqtcdmo1N9QqawxjMwU0BQ2iO_K_zZGaIvLhHkioxCpir3TzZfVD6AnoiSlxZaUnYKzllrB9HTMJvZ-hp49aqbsz5rC7rvWnoBEF_stRmqHHhFylYe9rK49ADxNBnHCVPpYUyYf-LpYKqUlKtkXf9l5A_Hk-KdsP1GP7svaGyad4j0uOQ1Ayd-dGPgUbuxH96niCLTJXanUZZdfV8-hxIyT0lQ9AdxHburNszZ1PQgvegJWM6jd0O_zGIOs9D-S1W24QRh2xnVkae5UaLbZV-H6McKbAUaJRj74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFRnulzDia_LCF2TDwBsIKrZMxc3JDhQPMBx-LJcIJzVYOzhygNun2d9mYZ4fxnGVv9VKp0pXgeimO2s72MJ6tdaaMQ3XAubpLfijwx5mvFg8U2I7BXjE547eC_TRV17oJjW30XcIJz1RMhqXvkiM1jKexanqn9I3Z22a-as6gaKQfIttIYP-9b58JQnSO1YEZJP1WIESBFeXQnoojq5LO01W1-KpTrPh0HcqrM8QT0efEmfDgIH36jJX2G6ONvE4SpyxK-ZymCHV-2Xjk1xVWDTbE9lUYAKhMyKtOKxywo3jkNlDyyyt8cKg0PVx2e-wJqQsCoiMskXx6iOp6Y0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcoj5l5x6VrUgjVlvdNbxIEftZ2lcd5PJZYY8LeBSqECZhDIxyv7ONqscSuPnkXfr9mO1UYVqKeEtGs__ERzCvAf-GZPv0_G5v9MVXOs2sl8YENOmii50NBcPRP2B5ixychOo-ziKaS8Q9nk_dhv3pPXgbxrB2sYWmxATY_02Um9Kqtf5mGSvP11kO6P0BP1uJY9eg5x6386PpZtbCQ3Yrq8klTNcC3yQDgRHrOTVsGqdRJR75aoCL5InBb8-HHI7MXRfH4z94emaj1EqxsIgwQTo4nYEXDR7T5DNmWyCI5N5iaZ8W72oMl1i3ZOjwxmcRzXcQbLb3x-OuerfVqCdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byOx9J4xD1B_hq3HunXADQp0-wuCO6zh6FhwyLjwDGULuj13i4HzHo1zL15YeaiWahCziRIu7YNoL4AUIjPxnYPAsd8u3YNjntEaie9H1YIUydlqfuR_JLlyyu60dDLPHBE5QUfXDYk_ZKJCBr-XB3oixvrYxMBx8-8fwV12TxlWgzOeSpuTBiy7dMjZI7J5m8qFPwpudsn-tHNYqMLabxw5EuWEC3A1Sv1ZdmMjgrX7NPX7a7Yn3k7yfEph5Vs2iuROWUApo_m2x4wOwOWjQ2azN-TB1vpXtfauQLq1kHfoWiV9onjAc8qlSTaRGByuMvrdvuOiTzWGMIGsMcOv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvMjOXvgVyMczA_6TdAx-ZOF8LU5tIlQwQxPBFwB-vDD8S69_gfVVoVlqV1KiuSKnVgrg2yRb0Uicdt61ov-NoQq0SbI8Vygp4BUH76Su4osL_culqm-3-BXuvOXe6ykuxPuxcKoV1dJ3DWkSm9Md54-n1wuw6KRxksyUjq303-scgzKN1Q-HEPficbolf97HvIy2cMV0L4cLyopw-0Kj7S3mI03CRhANYLeHQC2TGbF-nprv37W7HO82lwiXqTcRtpGPR9vXisWis0O5ipamPPnG2QjYHwEZhQTYW2RTwb7i4_k3gJe4m7xQ6fH605AbI6gbdm_R925ytVbs7fUfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-RxMv6vrc4QreBAS7M410FfLaqquw-Us3Mx9d-qdiHOg5YrniFEjvAmJ4aRU9M_XYYFbZhj9XH1Px1vC2WTD-IJXVZRmbTqlW6qa3VY504UikNfhxETC4CIfRFe5EXg64H4NyPwMsfn8_g9GOT_3SgvH1PeahTcWdr0_uTVv33Vs0Vy2cWC_Iqs7cVkKuIR7ZxrqjbETOq7P98-BnbYx8vnluHnkmLG6fxZNm0VJ7GG0NTtksoMwsMdbgWO4e9XjBMywBbSEdG8RlBPvOi5-UJVzlkYpU_TT2MiO-1Q51DAustRsTCQw7By-ANKSdx7eBsSX4WkfXsJfBCK10ZOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUIPPspWWHnQSghHrluTSp58lQJYrkq1i-mGJFrcDoqEO_7197nW0XHEy6Vfsp-IlobPjXTbAzvCTlx8KvEbzvgU7HwUoF_oY8gEXVMoEgvG5pMUyf0JkilJoUK8xj35zMb7Sx9mT6E1i73KtmHfipynWAuBhbbzsYKSs-XFN304NS5ooQNN2qhlAu7GlOW8RL_aB_7Mfmko1aFDxDDtNGGrqD_OcA39DlrG33SL2wcP7-YqE6ZCFM2Otom9eqzgKNV54qUlF-cvvMb4MJOCowJNsmqKC-jXJBL9oUWH1F6MGGtq_sAnIC48n1h2yXEzZNJK25ppo-0ZPLDPRuZimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnoxqM89EAsjwaLGS3lScY29wRMTfmPlRGm7oEbCchrGn-rGbHzYMnYjs2MDbLAK62xPuvfhpC_Ye_NUVmawV9aMuCo9Ce_yF9z_gmA_93rNA4mWEwzjlCPyRuFQsesluripV880kUbEvLaQAHxKXyeLR9UlzRzAS4dATaGAN9jSRw0DhWH02UJUtwX2pSyTsMe8-HVdod0nejEW4K1Oap6o4nqJUOuK6ZK2JojvAt9-v18FtstXbHncI9zOCNmWSdS9TbHaD8MCyy3-jzLokgvtbRTL-uCi-mNrPQV_SP2awDkCftbvU8CFjzjm51Sn300Bo193yXMHDJOxbKFPug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CN-Nqt9rSugu3znDdoJCXkL1_VCUOnZ-s3MHQ_-ZibwfIj71_rRclrPmnleJgzkXhwLB_HehgvWTrdyI2UGjcqv_YO7o7WXn1eiBpdb0mAKWqOulLFHfcpRFI_4zTjHcHYVP0pYZEJod6DjZK61AXEAncY39tuRqcRzavq0dCbEn6nGcLYgj7eyEjVW02vCMUzo0AirAgDqmqZ_WHTaQ1ZBRQJjX4lm8wPs71d_cgqMBSF_k8cuXEKBqFC-9SL8agoioKKtld1xa-Dx7e_p0vISJt4XAyirPR7mb1Otng0Ubi_qs3LkJNb4tdMhe51ZUWetR7ppwxzipSjcv4P1WSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdZakNMNV-B1VVwr1LtkTKxa314iI0f4Zi6f3gkZHlJWApRYJv4J7aAmnd61Hki7RevJ9MgFXJOUl_5b_CLm5TU2rLQOfcKlNsFSmmLJBtJmREQMfWR8XcZQ-raprNCNWxH-Skh02FeC5NowlzQjpW65KTKtDUCP0O3KdbXx8yWRBr8YnDDRk1Xw_v8crBag0j9GCxNXkw629on9igFmzjr999Ggq-CvSpTWNtTrB-a_DtE70orsBieDFuw0rFrk4GCrdvbwCat1TTZ4FU-3tXIkWQKB4ZNLwanLTZ2KP6trrYW23q0AxzQR6LOZRkuXv1f0AF7vr5Q7XyyKhrnoFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnN__XXUvINOjjS2TFvqNlIYNEIKYiNAMTPFqyeXyQp55k2KeRKSEOLkKpSulalDpqysMaOAHXnVvQic5rqHwcVH5X_yIGO-VCXJerf8IFtbikg15TgeJFlQ9Mx8FoU21nPcyR-BWchjIz2T48goMfZJ9L9AXhQmvTciUr7Cnz0nvR_VRAoneq2ZgueFhRrAGDL31ISVrMmsFVVgF63CcS_42K-loHcK5f1PvzcBIXKG6pQ7MvmcSSAiMkgqiNsrElS_xaj_l6GTSkM7mimTCX7h6Ntv1JYGSoRi8uH-h62X3QtNGxVfBZXUB41xM9u9HcQGm475HDmgvsLLOrpZ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jc1pyDm-C_XfwRg6R6L0tZ-3naOHTX37K_1IW_4pHNIEeovSsu8_46RV0xuPBTpcehx6NvZCDVMYBVOBJBOxxOh8ixYD4V_McLHXMNXlRjdRQ9y73_pQBgsPvW-e6-2pgD0coh0Mi_EH1mSoJy57FEZsbngAXknizxYZthKXuY5bhmgjfxgwv_Pd4PngweeVVvGAEZJ48fCV3cl1M5SUvvhg-YvsTZAG9Of_fAyW47fR6sj0MZ_uMBWM7y-6I2fu2b_28SoT_s1oqBahl8SjSALaY6EZHWA07qKn1VcjwBCsI_p2MqhvW1C9UKV1D_8EL5S4wq9pFYqb_7P1wRorMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX3FCDwftO2TD1DXYAUxlDv313ak1B4hq13i99FlIzz6xXqcXdhFuQt8T7zy0Y6dTLS11REJdB7d5Qz338u39Wm6eewgLpk2Uh1wDyluE5dJsl8RCgCeTrLVdt6Or9on-jgXfp0GCmZ23yJGOifPKV12ZIbex0XpxRNsJJJ3qHis76Vk_YXNveVUVXf4SzfpZopPeV6LRb7IS5TWxvOI_XcaQHh1EpkLe1qVfJ0-AUD2r9PnDAp4IWz4uX0E6swOSAsP4cAo6fYwSlkTR1MzK1h2K3DEiR3SEIThz3Ip8uhC585uJx9zYroVoNA-P5KB9ZkMtOmtuEssEGuWXCOEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vsAFNI9Z37gGWGbwleufm7WKho4laffa_p7Ok_Evay4FyqztmD_u-HnNcYCl6xQwLJU8lPPNVlumGTMFJEGfIrD1sxUIQsCHy5JXvHV8uhI8H7lr2j0wYYjLj3skTjX0S_b7jKPNatuIfRCVtmfiMJYakqF33eZAOoNL-SkK7Pkh0Ute0IQg3IDlNlg7YKoNo3tC0yXGjJ_RBkX89erCXBfGnS5BnPZU3y6ymrLq4c3xg4F-GG3YYvyVq6rHgdkUZXFE7ADtfp-sUi9hAGvhB6PRV-kUExnCa1XTOqYT1cTm_f8ib3x7ISuwcrTGHkqn415-luz42QTdwGGbxbdAxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF6azFDgvs2gF5XgwtmHzjvByWppF9y3nt2uSYrCwzQJI4VHKwQ27VRW1t8ZWCx2oMUKr2fI1RLK5DQuFPsyOc_YNprHeIWtZLN5IjsJhiohmRU4TGbB3bmv63MdUD592TmtkYEPW7B949T6HXGFH9ccbwpV1faVxYgpAO0cQcIi_ul23qfTokfoW6kTNsgByIGSLOg0HXwnV-M4JgxS2bK9bbL8GcrnaD53UwWCfFtddn-WKrKwc8DEelrDE7Oa40Q01psWapGXiumMzwDtO87PDHj5YeRVHKYS6pC-7MMvAFqeMNRUbQ-zgEtSDniS0r1eKiytm4K9bZmBOyJdbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaB3NQxm7oWMqoCLfwcFWDk01Fpo67G52JSbds_HdQ_DesJHoZWMjLM8YDNiqX0n-tNlAjgXSmBTwrgDXrmjAbJPzl9I9o0HXSawOxa_CZVVNwhz-v4StVz6NoVpAslgIzOToihqgG5satRFY0ndIK3_JwJsucJx7eRUClyPH2nYQXJbbHfveWXwbFsd2fndIrM_wUY4qE2mtltdzeCpu7nhqyE7kjXEqkSVKdSIK-yaETzRgNJjmfgZeZWRPe64kjWvtMGwblD3JotPf7wtkc0SWYXzkWymwadIQFqmkWCM4gQFq94iGwgGHosk2uJs3BUr9bq0bdFbq2yyaZ601A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=v-vgpPZnJ1SQ38yGy1-UtVaDHO1tUb2ng7KU5qhArJO2-59Tz_KuivuV2bNC84fQSnCl4NBOC7pKfKxYKWnavfW22feK1SjaJnQNkASOI4gcmkPWN3LLJyNU3lqTMthyjWKdfXB00xg18yWwMxRNwrQ1gUEURsi9ywCwyvPqkXG1F1CoYHQ8rwG0q8YULn5EyawycERltEBMnhmaQGkAbCAVN9-jbhOheHTYEBFOhRRu-jcn8S_N8g00NZC31lxpg2a5ixTTzpf2XfYkRtzh01S5qPZTx5-37LpXQ_iWMj26gkK-VOJGo3myEryDgzRE1HCaWoDpYUYJBkkXFbq0EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=v-vgpPZnJ1SQ38yGy1-UtVaDHO1tUb2ng7KU5qhArJO2-59Tz_KuivuV2bNC84fQSnCl4NBOC7pKfKxYKWnavfW22feK1SjaJnQNkASOI4gcmkPWN3LLJyNU3lqTMthyjWKdfXB00xg18yWwMxRNwrQ1gUEURsi9ywCwyvPqkXG1F1CoYHQ8rwG0q8YULn5EyawycERltEBMnhmaQGkAbCAVN9-jbhOheHTYEBFOhRRu-jcn8S_N8g00NZC31lxpg2a5ixTTzpf2XfYkRtzh01S5qPZTx5-37LpXQ_iWMj26gkK-VOJGo3myEryDgzRE1HCaWoDpYUYJBkkXFbq0EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hjs-_K4OirLNvLlTJyzRvGIK-zeGsW8IaiNnxsFIaP4fwm7syKRRkcumKjvmvvxhQ3u3FR2CHVjQQ5A6TJyWDSzruPe3SLROUNltlKamGfh2KBGG7fPu19yANvQ1YBKH2pcPaPizp9-rmkEtp5BrcxNgfrs-GCy0DXM0vCB1CwC3PUGTEhhSWKDmS656HJAWGgAsMpdh6NW7sd_2nHDMJ-Q3xspOC4tB9juZdNUGHfwyVkW_u7OpMwf6GGEoWLwbcYVBNCsYSV8ak3Qg9r5Ew3Ap7vD4bGL2-HSiT1d81dHRfpxj0aRfzcXkGKw3o96P7RZ0DxRgPHq_OF978OngMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFXpI63QpAPYj-vKFEzKnwIOUvZ2DRMptMFxDt4sWPkee8pP_ypd9NtndDjgas69qukFE-NIgphMiSRCxsRtZzHHqm85CN3ESrXqz8j5sGmgZDzeQBHgGUc2G-19ymV1K0n1vzr6TYYtpYdCcfPulmKwrT5RVb6du_4gooJ5DxAQ8lgeLygch40PZU6YLGDkzLARIyXVKVU_LkZU2_gBQg6Lzga6Z7uUgs2lQUZ_16jWDqAQlsa1Sily2DUKJrbUO8qgNljb_14QkuovMfAYAcEB3BiMR_oQS8G9CKvUruUaqDhM1Y-HH97354atNiP6i_k8r0E8Xu5pyCRS5o5Fq_Yc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFXpI63QpAPYj-vKFEzKnwIOUvZ2DRMptMFxDt4sWPkee8pP_ypd9NtndDjgas69qukFE-NIgphMiSRCxsRtZzHHqm85CN3ESrXqz8j5sGmgZDzeQBHgGUc2G-19ymV1K0n1vzr6TYYtpYdCcfPulmKwrT5RVb6du_4gooJ5DxAQ8lgeLygch40PZU6YLGDkzLARIyXVKVU_LkZU2_gBQg6Lzga6Z7uUgs2lQUZ_16jWDqAQlsa1Sily2DUKJrbUO8qgNljb_14QkuovMfAYAcEB3BiMR_oQS8G9CKvUruUaqDhM1Y-HH97354atNiP6i_k8r0E8Xu5pyCRS5o5Fq_Yc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6CXvr8V1pobHLyqI5g42zFHyNy7adeNjCqG5rKUmmNQCqPdwQ6h1Nm6GAx07TKRkINUEJE9eKQPUSDl7fy_MD4E4Yo3l_ilguVftS8VO6crOsr2YIWgYH1lncUYHo_63vExzzl0g36VPwXPqeLOi6-Ymks2RPLEktuAzSpUAqn33v5iXfwCjSr_JjcHz4CumSaMf9vdIlFvbgAeRvsUtO1vxaJNIQJjk3HXl_U0vk8AvLLJTITiTe2F1EA50gotDkFMe0NBq-rCZzOTC1j4D3sBmjixIcnDN9bgmz08OGEDeb7GLOGaIGc25Zqf20zoFcF8Qy-pJko-DorIKdaLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paDSS37GNkGdf7XR82Lfb9DRDryCVYUF-04An06Nsk4GmbXG0pLa1nwy-jOX1FOzoWEX_VaogmOOLxT7BEzD9Y9t1Tr_Sw1pha9JuA2ajmU68j-rUgfVOIHQDZ04hCwVAl-oo3BRCTbCQ2yiAQgptOV_xzgIQ0Yk_xyxM5o7dE2DPlogLuw7a9rebKe8DFGLIsswQ728qbzh30Rlfk2-_PrvWkFA_5eRPPzj3At4HX0HHfVwTMfiaOB5IgPDwzMzDEC52WPN9AH0vdUNT15L20_Qw3CFtcGSp2uVMTk9F5OweuN-Qp8DSOgkjgSzb29m9CKDgdx00jEyPdMTwUNlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hhft4mJNtpvGYwLcvGU8Wu2fTttbRgy_syHKwEq8m8IP-onMn-aohrgX1JUKySVs7zWhHzE93lsCtqmwNgC5s6S2qcOgQi0cVHN6cM_FFgbbhOmfkl8e-8ozQyCMuMhJ6xxxc9BwdFHRABkRebSA9lBWp5i5p1BeGg0oQdbS4mOk9U5m8FTQT0a2O3l32mLASwIhae8kMv2UKhdbG2ZIpX9SNNLYRI4pkrTUgDwxSB9XWjAaCn-PPUOYRFYXSbd-XvXxU0islDZGz3wiPUzbfoIPxV7ne9QDN283BxUvwSIP_hcS5mEHiL92qjQ7hTVysIidBV0aW7u-x-JSjyWFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvlweunLVqbSEMWqTwTnJ0WrKx1VpefkvaFWJZmKJzLskMo5g4ZM3-FRqaFrSybcsDLn-UNYATmsrmrwqyEQo2X6GWzl1Ww1AgdFdkYj3B2obUshkpkSWcQWtZf6vogdccGAhkgHDldtuS12c2VyCokiY5UtQ5VwunW4QD5eDM3WSN32IutAYXFJuElTazmLYQVCZ5ZnPssZfoxvD4mt9_va5_BSl3ZKK3XHfQSevMVUchmrfcgxLWu9AGK82M25JGWGXYmntViBKWSorpxq0oH4x1GWMBAfDWYLoiDpWK9Fj2k5kFTofyimRKt0yyeYfY4tW83dRW1mYwjmZBPl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsO1vEsq6J26XSnGfc3GhuMHi6bHacCz68A8IzuuVsxxBQZJQwiy7T1RSqzdQqhS0pcBmkqe10EprwlVhuhg_4tuDiYOL5Zm1gRPz0vVy4P6cT5drZEgtVk0xILFcc8A6O27Rdm6ii8UWS9p6QnfWoepbDeJN0UzI-g8cS01P-E4YOYRssCV_HThRVbGoycE9yQknAmEeX33UlhJXspBdIs7sRMjG7VNL2YlxrmTD0IAG0-inFjWQ2UC8yZeJkFx82uLn7m8Eb_3ouQq3HtfY5NYdjngvWQ3ylNdQDJSTL7o2_HbsNV6nk8v-nlOW-DQXCyd-rWa14jzxqCceuAP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeRSDsGU_R0upP66vKShwn-IE9KwdHTuzUeIibRlIVmK3yzv92yHIVKOC-JMqx5uEFFYdD8Fb0ztrPj0hsyLVmEp05cf-VQOzkuYiLlkbyTfrPzugyCgxe_FsLC0MM_PaI2I7xjMtP3HcmNBK7sg5Lmvgd_J6LhZPJnjbWUl9yz9_rrAQ__-XU99ZWvwECTVf68ZvE05tflYGSlibyLDcl_2ZK2m3_nOQFl7XUIlq-G2Ec3wr_XeDZuSH29RY1juA7u1hJBl06xmdshMSehaY3amcQ3Q4FIvTf0EPtuUzXQh4MXPO7KmT4qSTBy3gJm0nX9gnaDy9KmjgPaQMo8aDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3yG8f-qr6Z2qSz7gwxJQpHPnceEaeohUUvD3omZB9TA-mJuZ3fWp_Rj1MDmcE2enfvDDvkJhyAL3zthvrMiWvrQ_9VYlx9cL_Pe8kZFMKTm4qfvm9uQyOVNrUSsZ4BJoNUtAfqeIEjUWMdOcaYKBrlsLqqg6G1qAmLoP6ivp61Se8QpxRoNkKx-pUWcWEngtoDET5bPqMGcepOGQvPenkfTGQYOCD4LmdEvpfYpaypNPZWSorIOQ1p2zTLiHb0oluBVFS9IehJpaEAMGAlAYKLEUGAFWwV3402Bk2j7g_-tWc3BPCQb3i4OyKpQJLQ43ZETYQELS13NWzt6_3w4qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nW8gd_wSK2SNCv_0zMLQvFJ81uY0p2eYfi2nJ-zCMLyMQ2JYGGZuwwu7c_5eM8YYg7tmLnRg0wPUYeIIZVa5kecJuJdycby_Myew5EsqxkYWrHUfNumEwI-1cVH47o_bb-9b1oMPcdaRkGJCLQS4rPreNGAfC9fJ-H0lJRsQ2w4A2Z5bFmtt2FPXkQdWrchlC6-8mssREB2MY5LLPNhX5ze6Om5fc9ryRYyKltTOYU2NWfDYivCP_NcVinXZ8H8Qr3BW2Lg9bdHYRJJ5DzJe34eO2eapZnopR3AYA6E8s70b24J8P3Me_JVDXBsKQnrREiMS6vgqWn-eIwHFDe8ZVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KR7UH9Iu46eX4FV5D8veM3SHERyypAzln1HshrpYPXqaAAyzcIfM8g2J9WJW4JOig4CDQNDbvGlwmD7dmyMQ_NwwKGVLtThOQJkydAiHvqq8T9LZ76edrrSp64paky_pEtpzuWp-ijmsQlwaStZJtGxUUEnp3mZqsJV7ImuvWftXDZPqy9FpZSdTjs2uemICZ4tSgNDRjd1nfeADCkq8fS3hhOYaJMmUmbBl3kLUzEXkCm5iQfwQ2Cf7xlmSnkKMU-cEmYck__KXxL3xGytFswkvq15z9h0hcvuN0A4JQrPjXfdg0Q83XmqekiUixPzCGw9HRk7MwdPs3YUbjxWx_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azCuFQyqUq6Y_phH8J5m1IRqU5ZhYMMruPcp2SNpzrrY7IQqrGeKXpTuR15wmkh2O0Pdt0m6WUiN0ke1JSxyCnHlkGbUieB0jb8ZUjRxJVohGcez04PXgMcrS90mlx5JeXNnybLsLxMk1fR_vF7ThFzI92ib3_682hhz_n6ob2eHXONENndvYegbsqs1Xjy3Jo6ZvZbHlRNMahv8HNkBVJTDb7m66RQyej3FKboPE8EiMrC4aIuMx7tdgPJDegYKy8XnH63RvkpZAk6bMCqnm1JyOy7ZSebACJw40pEHP9PiIPiSpNXmHlAF6LTz5J_-53SaZ6PQ9NLxWhnxIalBsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkh2-qjv51D3Gy38dfhlkitdUnWdOywHThpN7LMqInMGNEmjeXIb64df5348QdOaf9oztk-kDs4HJoEslLN74mLwxRWUXDxaYJe6TtqA5D2RUglXzBRcFzn2xTPUYF7iQrt1G8UtzodhM8acnPahmk_vqhNknoqP8vOmxuCmxxeXu6AhYyJnrHi7FYMgERP1ie0EddncBwjSZ0dDEDRdZDksYYy2USorQV_tbClSCJVUbWxXCW8B5YK55rpyvWiuzTXIqFiNj31WGP2fQ9f8o2raa-QBpW4NftxHmc89wpaOt-zYRWIWHcZa2c9PoCqPXahLGgFuYSyVi3PSpiOi5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=RYboCTq7xDqFl7VX9GvQbuQ34yJakmpzYG12bjaBXtX710ZkvJO0Xv6cTj76DTJTMjPAi5eCZ3Cnu65MJjHBq3IeFsPPiNrGtncT7WUpHVUWReTu4A2ROKfL1BRPLOaquj5H8Su8P-xU2EzA1kKBBBmPW4Hj2F_BfUAdsV55c9R1MJdr-BEVFiL3ssXLIzLVpPIZEkl5X-lBn-bg6qLm4Q9ORza0Mm-RSUaarUJMv1VUuDZ08h9XCAoD0BHc5j3g3MwIAC2YJmgQEWRU_6PUGFVMgIXlYGGzYCBxtJmVvaYg2G43FiNRN9OLZ0XR1aaVPs2YV00VR2RBUnc2PIjEXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=RYboCTq7xDqFl7VX9GvQbuQ34yJakmpzYG12bjaBXtX710ZkvJO0Xv6cTj76DTJTMjPAi5eCZ3Cnu65MJjHBq3IeFsPPiNrGtncT7WUpHVUWReTu4A2ROKfL1BRPLOaquj5H8Su8P-xU2EzA1kKBBBmPW4Hj2F_BfUAdsV55c9R1MJdr-BEVFiL3ssXLIzLVpPIZEkl5X-lBn-bg6qLm4Q9ORza0Mm-RSUaarUJMv1VUuDZ08h9XCAoD0BHc5j3g3MwIAC2YJmgQEWRU_6PUGFVMgIXlYGGzYCBxtJmVvaYg2G43FiNRN9OLZ0XR1aaVPs2YV00VR2RBUnc2PIjEXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btN_2xO9bQwurWXX1X85ceSFVPt21v3acY924Z3eaQ3PM8t51zd2i3O_GdYWgoms7rdnAfh6-7aDapRZROhDWsJaLJWRVDj2aDu9sKzDEfIjoi1Q9NkxWMniE-vel-lhIMKZW7j-Y_PoOvxOv7RyuxFmKxfJhd9zRVyy3Ip4KiinaGToM3t094alFrgDck3ygy5ikzYHTwZU_OxuQX8dYxpJ9ZpkH9Ysv4btcc6eaEQaw8UAGsJQ6DX9-XFPZkOKqBqw2vP1hmftwDFNR0BAIPFgBarNhnsxP-QmQmAcZYmTS0GFhfPHhuDoZ7nkf6VS_rAnaH44wi2wnjr0uuAeQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLRrcQb85esM-tqvuQ0puiaJYyZXgQkyD83cjrq5MGvMN5Da1YPsuFdul4jLc7Lsp3c1wdN_lrQRelIRVhPNcqA9ITQ3jK6LJUaKy7Cr3DgbmWP8-lkdjrM8Mk8HCcGmTEPnahg3mKe2Uuna8vNh2-yxwp9fCSSJmeuPyDG2poZs1hAzkmo2fsrUgiVMkhUgS2S7hDptS_QOS0e3urZ2YLZ9ZlOfV4SonW-8eCGiZDwXNUmek4Oye-Csr-lMdzG4iv9MYTlCvWdMiTiJ9QMroazBXBstQcB-2uJcuLB81Lqis7VLu0Q7wfFSGmbS4z6qWB_lu7D6v2cNasOWtjzxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-PyN4VpM5_nycoaQgTR4GLv3nisTRttq4qoeNO_F0MiVKxMDlNTZC0BoZ5pS_vxB5pMpO4D7kWJOjSpDSkubCirOREbD_V7EuZSDNpUoH24da51k1VgTVvaLXhhLDYywBW8Tlrk8BE_klwMQquI_zKxBh62oqiW7XVlIJJGASi7_FFkykUfBMhSTAlvOup54Pn7Rp4qe-2WA8AL5nzwp9K7OFpymQekLId0yKG3RZwD2u4dt_RM29YQhcd4C03MQ8vAy85tLStrXRo7rRUtKUd50i6JrkSANEYsZLg4ulYLktHHY3bYp5ZWWqRWew1hd-abXIZsksOqsixaWjgB7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xvmu7RJ-PpYysYHjOANt7mVBwBrhjjSOV7YNvW9ZFpcJ97_RN-w9BmRlc_zZZdZva10RoZ5qpUwwjwsQp9UnP8auelBj5de6CDhxrZAybcf3DnhVqz8aIyRtu6KLZyZhs_Vngms7XvK31ZE5t80wwvWIlcFy4aH18ULf4SuZZbWuglTscbG7w_8zYozSVbtsZT4UfYlsZuWJI23A1KDeprUEx8asyfsgtMglZGpBuHF9UABkN_tsp6YGVC9rZbqbKsM22RGPQdVNDSulTl5yWWVNP4ievcj2PbN8d5UpG1otxPq9oaB0N6Po76fLjw_iVmOat8c7q2NnOfmbqx1M6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-SuemUmbgDAjDNqPZUFw-o7EI-mMuod_j5EXG6EDRU1ytZUjLEv7RQmEl-s7NQIWvLcuwvrKfPjW7-z_wgkK_AD1N7-01ysfaVt6qe2e_92POBsKDIOytu8-62hGije5smtj9DlPFwwOx7fWtcqmgCJAdRd2VQHC8tBQJs6VxE_jYPLRGo0B_aV2YmZ4prnFMYBZ_wd91rmw59JMshy-6eHQrlp6ORdciJpU_RySHwu8zLD2Gqu3AsJW5Ig0wB08PWOLTonNL1j3gj10NLaieA_DWtrVNQbHdq5amHNH3OwF7qyNNsNQenPg-5CxGtSZ0VhttwBzzXHTeV6452GNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxnnB3MNnNV47RXZes42oFgW3dRVJKJQaz5YZFePoD3Mmfj5WFOWMmo02zrmdL1YWeT16qkNwHuW7uuW_rkz-OmnNBBpwzdVc0w_swIAbWYzJbfG3Wj2ZhMFcMwFvdRh2cmeO8yWO54S4QfQY_K0UQv2KiLwiobQtFt1dfKF4r1NIN8RsVRDC79jdDupzjujUv47S3k6-3jm98lcTmCDIVl_Wj7oldb-ltRZh3jpJvfrfM6yP_jiwfITfFAiGbqJlhhJGMUFTuCtMF_i8dvx0N2xtGBa6WXg2QzynfidwsaHPyDnvfoaf6S_47s1DX_GbJ7kudJqV_Kvy4DGyWmEJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tj_vJ56SN0sUkRcu9xXlIrgcPEOHCxHvs1uDSfMR84brhFm5-92e2eRk_gL87jjPSkE7NQybMBYRWWiojQlMgtIzqfHYAiiHm3GDgbDhPIvg-1ILHXoI5Vs_T3m1PXDgLNnO-G-RdBvpd9DnI0OHGOyF954I-uQRJr5HOuqoRYtDWr3rvDPKFkKsy-ii-NBMTrz0fxkcI9WSiFqXVIYpSFNQaS6sDAe9VVz9sFZObWEQtv6N89ay59-Pd3t3PFkOUpKCYp4LEDQIER6HwHnc8Cw91b5c46vZQiqsxYDeSlQsFvz_Fu3Xs_EBHqYuiTwmC85o8Mn8RahdKad_U2_fIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=lFNCrME3u2wK76aY1vvv3oCAyP5FXBWBOXAJB_BIhC234yUPPc2pUozxXObm3JaQeiI9CXShkkP0lPuxzmR3knCA00KRVZbPQzvdw983w1XHyaiI5jqt1uxXL66LcegyrJ2Vci_5Y2OfSKq34gXepQfHEQ-DZsNPUNNpIRV1d0pWakqMtKRQxBtp-RiXXdsmAVn60jRGgRN9yFvpgpDu4xp3lPplXTyVz-8G1NVHAVoVtq4qlp_oXgRPWgtaqgEEOUfBg3HPLvSTjE9vOz5_It2U0plBm_lfBpvEGRwG1Z0talsvjuyvR_jUVUBXObrkT-0lY-4qPT0H3o4O7rVSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=lFNCrME3u2wK76aY1vvv3oCAyP5FXBWBOXAJB_BIhC234yUPPc2pUozxXObm3JaQeiI9CXShkkP0lPuxzmR3knCA00KRVZbPQzvdw983w1XHyaiI5jqt1uxXL66LcegyrJ2Vci_5Y2OfSKq34gXepQfHEQ-DZsNPUNNpIRV1d0pWakqMtKRQxBtp-RiXXdsmAVn60jRGgRN9yFvpgpDu4xp3lPplXTyVz-8G1NVHAVoVtq4qlp_oXgRPWgtaqgEEOUfBg3HPLvSTjE9vOz5_It2U0plBm_lfBpvEGRwG1Z0talsvjuyvR_jUVUBXObrkT-0lY-4qPT0H3o4O7rVSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=k5KZ_Qq7HJpkbLOc5_3mQ0hEJtk8j5QOYhPzFI-eGOQAQlOTPVfyzemvaX3y6J64Y3_pfZm1FS1PjHr7BwgsvmqbzalfWgJzWUpR4b5_oatoF3jSLrgRnyf3deA6uGupero9mxRF20RrWFs4NJL9blBoS1wO88TS-1eFC_hzxHhsnhUrhUi8cIaIY-Ix8Rk6qVC383773vdHiFsQh6C790yIqPc8o2jECjinZv-L_zUB3_JNNbKHTjJNQ8G9IG9GwPHghqh-lxd4qLaplMRdSZFc5814D2vhckJkje3Pr3rn3tHMuadDiOHapChw78wxQ-6qIPOmXoGw10SDYiUYLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=k5KZ_Qq7HJpkbLOc5_3mQ0hEJtk8j5QOYhPzFI-eGOQAQlOTPVfyzemvaX3y6J64Y3_pfZm1FS1PjHr7BwgsvmqbzalfWgJzWUpR4b5_oatoF3jSLrgRnyf3deA6uGupero9mxRF20RrWFs4NJL9blBoS1wO88TS-1eFC_hzxHhsnhUrhUi8cIaIY-Ix8Rk6qVC383773vdHiFsQh6C790yIqPc8o2jECjinZv-L_zUB3_JNNbKHTjJNQ8G9IG9GwPHghqh-lxd4qLaplMRdSZFc5814D2vhckJkje3Pr3rn3tHMuadDiOHapChw78wxQ-6qIPOmXoGw10SDYiUYLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzvtXTRYiJwBVLaHjE8VKhW5i-AZOz-SCIVLNoRUI9XI-bQo-VYGGnsIkEsJYdF8dR8WUM6wO64swBSRFunys7pIV4aC0gWyz3JtZ6wmHsvC-XE-fiq2PhHrvkiLEKySTZ4e34D5YqdkClXAdrBwJiOkMgeptIxE3B1eMCvkyP2HPFvB_H4VmKKXAYxWpvtA3wwWKiwCpqWtHJ2G--IVH8yPEF9O4CFnHg7DLrFHgd0QQrI9ggSDYvSOI5YxQumbwbsBhsGpEHEJkLMj24uE1uShGXVcGiSfVufSZzMkAI5kFtSjTz2xHilHb8aLGCNnNx3t_I375cSt5AIEEOmGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOpoloTjuuNa7wwBuscF0wgherQTMjoUDDtsu4yLYIVlH6_H7r9DjggjjJxfsmQ03YFKI9ymIY7mRveINDe7zKtFreZ3mT_fezkUVP_A-uSyNQ_vufwgqQknCk04bMo27SoqPl28KEMA6ZhuUebly7qIPw1WOy2QL1KflwjnlZwwW9I2V_y5ezXe1BLAiZeDBG6FIq_8iXvb8Fm5APDXNYQB301fxUWimk8WAEeYygWCHbRlMnhuk6KWEdfxNryrl4nsThiGm18tpIUP3MKKr305XHwJFQScFeYo_cvRyOifAvqyGvtiUPhV9YklZVpHWbd02NWZJBdP6VCjuiVgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWigi-JSyKUVSaIioZqXCBDNWIwXw4LASbPQYGnXexvW_8jqejOZo4-cY7KPliC0DKHMGVxZ4ibRaOi55sAsVs5IBgvECkBOraJLaCO7M_-N57D26yKox8qtAClPT93ohHyJq8dwBqXQSc41j4g-aZN88WCXBxXpiaKdhYF9cg5qzPtULJbHSe3Gt-K1lghMrGYingea3Ef2TX9Kq5GtX7GCAxwWKMttJTg9qpl-VP1125sLVrTp_a4tWaeJ1g5tIx5YjLM-3XaZgKLFPMf6jow_FI1nhyBdqMSUSsJOaN5QRAa7GHS4iiZtR1BnXiVOAVbjtuPoXECLXal0D4QZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSfCc3RRARt59O5uFGiGwcjFQLJFdIpvtJuVngxZNRZZwUmnCAG6rIpi88PqZVfkWD8oIr3UFMFfND2y5Q1Soh2jnMX4FiNsEnIwo8QWHlOL3T1rLNwCPVGsCb8p18cyaFmS17M9FVwUIOUE3aTH0gYqylOTTqOaLoNCgEf1RE1kuoZJrnDorwsxklKES-voSS5icMO7zaOf945EsEwKK4e9JYdtbIuuh1JPNxQb8XmRvJHYcqT7KdGL7Eiv3BTgDfltlXX4-TB-V2uXmBJ-C-CkRsQJki2W_BU8IdwxQe5-s4hMyrRaP-VzkYXIOv_30JjDsDg-Q1wSRlLZlOdt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVDuRy2-16EngfOwaDPPG6nOesSg-7nZt4BgN8FU0NFRKN7tfmCMCi-dVdv1UNqPU5cFRgwTeVRU3bwinqbRUUgl26wvjZ9euxmZBIogoQ4RJ9T4jN7djSIBfada2asibJWyd2vcIFe0szAt-Ex8yjRK0k1WdXln4vLFogdx7ndIPs1DvvTPVQe28OfUV3MGphjvocpJr2URcyeFGAEQeAy2UynBd2m_sUe9dqji7JC-YqRghxUvg3TtfjOtrWYu-hduOjJGwwEiud4icwD3V74PbkplY7Rbk8FFGPvYWxoodBt1ftLTcvcdkhCK5K9s_J7_ZJjXuPf2uFrI_SdoMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apmZE7-oQD5M-tKWmdmIicEwWRQmESzU4O_1I6DvyHje16p0KY9e-8jeUTV-ZqF2duy2KlOLR44vNX-S6HjKXB9Z60yFfsOJe821JdcetCxrdDZv3hP18Lw5rOwz1X7lmd3WSPtwHC-3fFp07rK79alt6vT-eP3fPP9PvvOvGaYEtproSK15A-GT_NqR0TzuayWnF7Z9-yutLnxLWw4M2Nn7prtLS4zYebH-hlYktLDlT9NcZuV4SfOk__fh39gM43_lZrBoSkgWRMKLoo6yYUegt4CGaAUMyHEBBjlZlNHQovIjXIW79KRJvHHZ9Mh1z_YFNA6lfZAIzCwputS_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=Qvuosgr5aO-9DCy16T7nb7z3zV57nqNCSKzfs8QqnFOErr9Rl27S_7ESTOLnJqIHPM8fuGY2ABbZLw1QmbxOHhn_5P-k3dij3WX6GkewNQC3OeZBnB2xbpnwFuFtYQR2oaFmh_LF3zgtw4pN9H3w6rvXzI_zmaoigXYbVHg4YQ9rWbhPesgPO-WYBGi6FOEGYbrz6X9Kt1yhp0i9eHUtoaunrv7opXDdwFTw7mFENagGyA5TTZjwomDtDcSxhy5SvGzez3ikn9yZu9wI0JhVuEy0wTUzNDJnZQUvJd7cW_7kTKNXzi5uJK0HBqo14baYArhBqHFC1PI0zV2458qmwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=Qvuosgr5aO-9DCy16T7nb7z3zV57nqNCSKzfs8QqnFOErr9Rl27S_7ESTOLnJqIHPM8fuGY2ABbZLw1QmbxOHhn_5P-k3dij3WX6GkewNQC3OeZBnB2xbpnwFuFtYQR2oaFmh_LF3zgtw4pN9H3w6rvXzI_zmaoigXYbVHg4YQ9rWbhPesgPO-WYBGi6FOEGYbrz6X9Kt1yhp0i9eHUtoaunrv7opXDdwFTw7mFENagGyA5TTZjwomDtDcSxhy5SvGzez3ikn9yZu9wI0JhVuEy0wTUzNDJnZQUvJd7cW_7kTKNXzi5uJK0HBqo14baYArhBqHFC1PI0zV2458qmwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpvZX3QgSQmKn9zY4Efm4DsyafD7qDU3lEWcFhzXUdAjm78Ndmhny_DcHHnDIA-8E6Zhamf56qfVdLdpQxmK3HygmC51Pd9zWOLx6AfLNxRj9F4jpIV-iPTXR4kpva1edrB7LFq25ClxPvvsqoNGJaYh1mxsShBu9u6nFNh2yEerQliaKVUYM-gnD9NU8tuYRodmZ-JCWBJaSYr-xkNxjamGJaPea4FembOtYO0WydZ4aeDFN7E4fqhDb5ao630Vy5MK9jWJaBujzhFTbt1Wj0AI8eYCdYdS5SDSZeH3jbPy9DGq4-sXBtDWZdZpEK68OvSnvUO47W8ROvOwgawz7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتیجه‌دو مسابقه امشب ¼نهایی لیگ‌قهرمانان
🇩🇪
بایرن‌مونیخ
2️⃣
-
1️⃣
رئال‌مادرید
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
اسپورتینگ لیسبون
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ED8Rk93WWpufvXd11W3qiEIXu8-iY55ZAJoEtvd37438w5FixT5cZipfOkjs_Rx-AvJorh_nxy_vGV-5fR06Mq6l95eDFetQNUfeBY99klGKavX8zD-A-yc3RcbIPyhDUaaK1r-A6sP3bhNGZey_yV8gNTxudrK1U6yqO8vwRUu2qI2bIAvU26xubFtT48Xgk2LdNBaDArpzRe-q326KdgvL-4_XErZcTffZ1SG4JQEr559bAbn-HepHfTFcpEed5m7KV3I-IKrRC4uq_aFkBvXrA-AtUbhGLaGKB_0nmtdMgvyC8K2DLh4e9AwhBPVCrUI6N4x2ke7EzCJ2UR-rEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvDPLNSB3WlYx-M7UfloeiBMVyn_2GtfMZc8eVM7RnXaS92kOG_vDBKLNSZT5GQVZ_ubyXMqWFdCcrBzOziUhWQLR5GSEomKTj55T7oT5fsjiiH99Lr4yU8JnJvGZU_Cma8s2ITLVJu0lQ4t-w7tv4_-S2DQF68GBk7aTo6ETYZq8oZ2wSxD0y7M1hdj1zlpqYr2ROimcpYmH4gsyZTO1rPIHkxSazJ0RV27wUNVvzqjQ5pwj4kRrefgSJUiU0Z1a7tVJ6wqhJVm0bbCah8fWPMhHcRSJhjIkmzjGbfqyVz0_03fFCnk92VjtB_k47qYlGSNWpKTxvvM0a90Y-DkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX8Vgxn2yO4utkRR65crT42fkFyPInWEkhX9N3UTqWOlWWuYxiNDE5D7rBUCyHPEMyg-YA4M7VOhS9pf5IqD0YVYDfykEiep-HbNMPsUDbC6DMJD323QD3xYWNlOfhMCc2i5IwoDXk0OttDtr8vLcwLTWGi0rn8J20WBCtR2CneykrhmsXXpr_QXKcqxZpoUPLKfZ_NtJcWWpJ3lgQ-hyf0qrdmKJEvTdzJStlkYmCJU88b_8j6agrVAbWAhMfOnzeOF-0v9-dUkPr_CGXnebvP3cLg1C3x5-lxWiRIV24YQVtCc1FjQs4BlCcaWXTNpclEuYgsOgzklIN5kXoEdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA4plt24XBKeDkbRJldb-Joc01GwF3FmQXq2u5F-67a9urJ3LyrMNGpxG2SpTA1NyrVw9gITLAnyebLYWnKUBentOial_OxVBr1u6HtBB_q3NoLmKYF_Niou9qVtTexXfVJELffz00b5K5PSMq_GngL_Ni7Ain1PPFx2gCuhyPhVlrVZsFamwXFqCzhcms1-5GS28kgpJXbEIrazozoxg1N3zqGSkhSySE3h03bq29fjOnAZvjP3SYEh7mYYjI4K39V5-Md4OHTCxkqclSqKnwnLg6ofqUrwzoXrMkIlJH5L0sS8J7ZOEpSW0iai_AZ5EIcY4DKXvcAEnZoP3DgyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnBnThPdCwONHWK91QTiJZeZmM2V1bhu2yvLCRdB1KoFwQj0iF97vC6RRUtjmH_DzlLHNqrRq4527qqSR7pFllYb8U8AgF1PVFYR1FX_EiyPHMElaQvzkVDsC20dxIZOyQYcXoQKZ1HCUssE1mt_iYCYcm0vQ7fToxQhAZpK2PKTsVN3W2TY6WBi7l6ttXh9fdrAEzFY6k7NGmd2Dx3tT5Y-c9XTvjhSUVRtbg2X87d8X2fgILu43CZyh_Pgi-dHsTWWabx8Et6CuHr1xk8Mv1lziH12FQ0LhubVB2iY1eM_khheUoodE4yfn4zODFDYDzKPUslbJ6IzIx3d1cBhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URwlh2zZ0nSg7wHvgG_pVS-LAQndlqHc2W9Mg0HDdyQIkdY-saV7JC098IyxcyeEyPszr3gnb0tYFhorvgOpbDoTFHd_LZEqfRPRB2LOWYyCu9x1xO1s042SFJV1iKW36a34HwuBo_ISUJ5THZdRODThsDz2PrGAbkYl1IpTIlMSPgS1ORfWLBIZBQjnTEHtZXMCjn7UFC-11UIKLuLjn15Qiq9--dxu0ukIC6K36b4iYFQXwxQL9Qu6etVx3cnrpSKxqYTN_WXQELi_yxrDV5-SdNR7mZsUxsnPAwJbFPXkDDWZaupApo2DuJF0YJ7wx4iPVOf94BCzx0Te1cwEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGrCZjFLdAUYa6p0jnA3WshUwjqB-kBQ_AnJE-5TBxub9MEHBXpidgnONJuhRbGRobPDGhQ6RurgCz04eDfnGkj3wRLY-KNMMP7Xid5HZ6tk6_59Gxj1Q6a-6Y8QB_q7wJcDAq7vWGNytpW92D2uKEgfo8v93mORj4VzdBFLo_5SIOaaSvow6soSplIZRqW4cAw2EZw5gdGhP4aH784170-2_GDcTJrc2SI2oKO09e-GhwDrX8seH9S1MTBbxMvVPLer_6M7dLXCgyEOI_IRZMCyU2DUwopk40xpCS1eNNJQ__AJ3Ny5NYYvYJVT41SxE1jHzsMnZYLOdBFbD0NTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
​​سال ۲۰۱۶
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۰
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۲
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۳
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۴
: رئال مادرید من سیتی رو حذف کرد.
🇪🇸
​سال ۲۰۲۵
: رئال مادرید من سیتی رو حذف کرد.
⁉️
​سال ۲۰۲۶
: نوبت سیتیزن‌ها یا هتریک رئالی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/22009" target="_blank">📅 09:55 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22008">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNlZCfkRjTjFzBt_PzLWfBJ6NI0HweAJZvkfm-jitOfGD0IlounTolZLgJTsxxXzc-mETmfJ7d-TEy5ufwBeQDrBvf9B7TEDF5qxX5AZjKdXEAisa61t87diMqci-wuZf7vRFzNRsPJi5xNT7NnDQZs68346NA-Hn1TeVsHzAj3IlVGChYlXtmtFSFR_eBxm80AdFvfOm4O7CIlyajvltTFPeXstBXaR9zkcTHNXFX7ugAOCHCscJo4guaDSPv_27RLW0xYH19ykuDXpZN_1yjsEJP2J5hNbHJ4bdsbT2U5cKCSYM-PVMKnlcD5phiO0SQJ2Ln3dcjQA-znxdXOIzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Va0n6sh0eriFcS7l3d1H6y-DvYdOj-kIsWoPKa8pO-hac8taF3vNvwWeyiENMd6kGpK6zhizZOZDARG8nY65gs-wNB9PWPkf9b572Z_avE8WPiK0Eh6wqOKxjPPLPZIdx1_fjmo4Sd9KFaGoYcRbtq6f7v_QoMJU0Lw_F61MrTH8rxP4r0zh6fu7U4D5ofQp9dCbQylD9OHnjGAuKfFzkV4tup1o8_o16uhdUseOUiT0oBErMDpzZ-VQtPv66K6dqgomE0syZV4CCPxcoYCbq3LnieZQO6wU-mORNuSDwKL1Kzbp6p3pGY-t9hB098Yvfr-bi5Uma3xetQ6M74iCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرانکی دی‌یونگ کاپیتان هلندی بارسلونا به دلیل مصدومیت از ناحیه همسترینگ یک‌ماه دور از میادین خواهد بود. کیلیان‌امباپه ستاره فرانسوی رئال مادرید نیز به دلیل مصدومیت حدود 3 الی 4 هفته قادر به همراهی کهکشانی‌ها نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22007" target="_blank">📅 09:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=GtRZVOlein3aOnH6O6WjESwejsyUCPdtP_KfGOzy0fgT8D1NUAmD3_9XkZFjYQ_hzNAvHgPK7vtXP2tQdFga2jRCZ3pTHbUAsvBZgythZ-rgCN5ThQFAjZXV2eRetPxAf5IP6_FQUtZDaBU4grF4R9NBTUFo3xA3f_AtysCT_sAyufUDrCER-fNqjBDxZ7yvtG-ASqn-xWkmXAQ0x2Q2EyYDOCo6bHQf1Cg9eXPKSXWyIPBm-uWghNDYTa5aKfccV604r3nsS0SjiDRsQj6_fnLHPlN885ktBLVwb-QJ7Io890BwICzefXIKOdU0GL_LsOptQXQVUj_HL6Z_2MZe5K6qnQ_km6zXo0YeU079qa8CpIfiB_5rEGuqErVCzrIdKqosV0dTL2Rpoo8d293EdnJ2q9PvePa1UE9XDgchudvsIA4NPX9t1tJlfRdcyqU8qYMMG01k2-kKl-DHk5vVzCFwQGSGtVy4KKKFm2Dqav7OD8k9WkwOX-H1xR7xFFfe8pVRHPaNzu8X5JG74L3FlIPp9I1FKqN4cnypMNqx3BGtwN6MKSHIn85xwLSE_bROpEcK7yClHKCXc5shG9ILAwg0iZJrBZ3oM-ExGgLaPaqt7m3-4JoESyzU1sF8eIF_-GUuOKnmVEumuxK8inuMWxe9B-yHMpJOKw0xBQRPsVM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=GtRZVOlein3aOnH6O6WjESwejsyUCPdtP_KfGOzy0fgT8D1NUAmD3_9XkZFjYQ_hzNAvHgPK7vtXP2tQdFga2jRCZ3pTHbUAsvBZgythZ-rgCN5ThQFAjZXV2eRetPxAf5IP6_FQUtZDaBU4grF4R9NBTUFo3xA3f_AtysCT_sAyufUDrCER-fNqjBDxZ7yvtG-ASqn-xWkmXAQ0x2Q2EyYDOCo6bHQf1Cg9eXPKSXWyIPBm-uWghNDYTa5aKfccV604r3nsS0SjiDRsQj6_fnLHPlN885ktBLVwb-QJ7Io890BwICzefXIKOdU0GL_LsOptQXQVUj_HL6Z_2MZe5K6qnQ_km6zXo0YeU079qa8CpIfiB_5rEGuqErVCzrIdKqosV0dTL2Rpoo8d293EdnJ2q9PvePa1UE9XDgchudvsIA4NPX9t1tJlfRdcyqU8qYMMG01k2-kKl-DHk5vVzCFwQGSGtVy4KKKFm2Dqav7OD8k9WkwOX-H1xR7xFFfe8pVRHPaNzu8X5JG74L3FlIPp9I1FKqN4cnypMNqx3BGtwN6MKSHIn85xwLSE_bROpEcK7yClHKCXc5shG9ILAwg0iZJrBZ3oM-ExGgLaPaqt7m3-4JoESyzU1sF8eIF_-GUuOKnmVEumuxK8inuMWxe9B-yHMpJOKw0xBQRPsVM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
​​
مجموعه‌ای‌از بهترین‌کنترل‌توپ‌‌های سرمربیان در کنار زمین؛ دود از کنده بلند میشه و از این داستانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22006" target="_blank">📅 09:02 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22005">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPQdMXqzRE2d9Xq-sUhWsgl0rnJJwJ-iwrjD9c9UpWTWUhqrev9x0OPlwog8F5pkZJ2xZ5879beeUUcX0qfTkbaxqkXQEe1GqamhoFL4FdlzxLOjp6mxfwPLoIrljYZRsD8aIC64Ud62uLVfoz1qHrAojBd2CMKCb4kJC7djbIPObEt1yDHX2lrXuakMPvOWd90i-aooNZJTHY9yKeEbuOkPG922YOP9fDeaqpX22P3Rz0ZfeywPRwQ-ylRuc0BjodgocA8O8GE0wsCGxijhXAiWsPbgG_WjWjankMitvkRVjN4TgYjUXoBR6LT_3qRt7dUtV_YJFJnX1exWNhLLcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfMSVZuzuduHSOK0p_E-BAlogif51abwpgO9jMqmxRCUgGR9BF8nV5qP88R3ok7PiZy1RJFtgie0dBBVdtLzC3kCg-5J78gc0YVehegze3U6jgNyvvOzoxlpRYPSeTr8ZiQyKL4o0ur-iLhsLJ6saFR6s0I3rVV3t8HWtYpTGT3xtnKMuj__UZDZXL4hPivote9Ut7LVCw3EC0cIW1QzclFhxJl3jQVhLZrvDueAsYX2au0FJicTkzpoxsVB7_7ygRClVXcq_Bk0yXwRuWmYY9hPqB3a2JgnojkCBUalzdHJyzNS5H1czcpNO5vJm_xWosb35yRZBN_1VvLW1UO4jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRafxG43MB26JiQoqCT79YXTUeXPet1RWrWt4RRdBCzHpF9ZxP2RY0j7r-2BN0Dxih5nJMdBJNcKaWThJjC5jhrBd1JFGkbqG8qEoHT-YVaEx3I57p59rbRBNCRu9PpYlqt_zT0SBK9aJtaVzhb60IP4ZGVSTNXI5kJ9FTvq1tF9pF5_zYmptqLeAB1Rp5Ne-mjWuxEsdvQsbEMGpXH8bdZgilndiDjkDPavw18ylLI7PP0si0pIpn5NlQFaRL8gWzlvfZSBZSIq87EeGoS4Iyb-TUEOmETPWO63SXm40h_BbAi0bkLhsjNvbp-9V8PdQ-bO-e2EcPJonzqYs9HXMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyVOaF_aRp5JYMDRMiq6d9Fa22sX6XTwBxQoc3292p__PXLp79_X3twf2WckcfSwgE6JnrcGhhAXZ-515tU9AZ7KoPmdj1EhGVrVm0mrpHcyw9ksuJilSTCEnIZCcBLQZmHsp37Ooo_YGyCrEyBySkH61yFkIqipprTn0FIhoDqWNEqKksrLzMssTYt6nXqpGIqhTPJgse0uiUUG_Clk0vqdMDDYZ8-OGznE_0j3I072Y0C3-K7FGhvkH6XBWGvvSCqYgtSRUlE3dyTclrJuZSdDeHDBKlJuF0md9iAlB2Z_WdrzKMFI2341VHf19DZcoqSnvyXDvdXq_reD5OaQ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/22002" target="_blank">📅 23:57 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLOyRHjBmK4asTt1Di_vuBo34vKus_0A2EpfZafYiMPX4gjv5k1CKJlKgSZpMAYJ322Eo_0LskriE4vVbjbIW71q5eH2TeH6UE8X3Ne3FPs7zTyjoJmqBYngkx4P_B4rtwZ_XvspHfZXw3cEH69aLyS4X9sSw1tW7gn9Pkb0ggo5Gs4t7n_N3LSpv0MdQkHE4zhJ2zgdXPKwmDZwEopzPU6FEvIxmKMHlBVkHKcQFGV3G87uIRpa773XV4U624mcXs70h3cyz0aS5KzcQqOPPoWkRmNWtTCLB1WDzzhq1mIvxM9PUAWnaAERCtTGhSHwZP43jszhPgmqqZOdA-uNxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌اوسمار ویرا سرمربی‌پرسپولیس؛ سروش رفیعی و امین‌کاظمیان علی‌رغم‌حواشی‌اخیر به‌لیست این تیم در بازی فردا با ذوب آهن اضافه شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/22001" target="_blank">📅 23:44 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22000">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=ODhZni2GLNOuSwtNUTzCuSkjxjOTcYkWJdBp8ljkfIZ9_4OGMDlx66eF4guqhPE-3OTrJ_ALtbGzGpjXhdtqoLmUCDMV44q9G6TKdx3mYSNUW7HSBnDFVU9p416NtPs3QWyUNi9JFbRp5rl0xsH4QRUQl95-oduKEBSwmfei94T5rWyIIKmYX-EGQ6T3JdVVilJAqIVk7dPmNOhVugjeFL9RdJlocr15Gx73BpU192l2CJrQmo7-3w3EG7wTAx3jResvnAHXXv_Wo7ErKH-xt4YFqDp3z7-7FAls5QsfMzky7MwmYfXfxre1PqqAoFqG-L_9Ttlw0eATG2WS-Z1FfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=ODhZni2GLNOuSwtNUTzCuSkjxjOTcYkWJdBp8ljkfIZ9_4OGMDlx66eF4guqhPE-3OTrJ_ALtbGzGpjXhdtqoLmUCDMV44q9G6TKdx3mYSNUW7HSBnDFVU9p416NtPs3QWyUNi9JFbRp5rl0xsH4QRUQl95-oduKEBSwmfei94T5rWyIIKmYX-EGQ6T3JdVVilJAqIVk7dPmNOhVugjeFL9RdJlocr15Gx73BpU192l2CJrQmo7-3w3EG7wTAx3jResvnAHXXv_Wo7ErKH-xt4YFqDp3z7-7FAls5QsfMzky7MwmYfXfxre1PqqAoFqG-L_9Ttlw0eATG2WS-Z1FfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لیونل‌مسی بازیکن‌سابق و اسطوره تیم بارسلونا یه‌تایمی کاشته‌هاش حکم پنالتی رو داشتن و تیم‌ها به هر شکلی که شده میخواستن جلوشو بگیرن اما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/22000" target="_blank">📅 23:38 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avqhsOd_sk9JQPovRKpyJXqvQJ-QoVSMJ_ckf1g37qdPUe4DfiZhfI2I5v5ZkIz_RHN2ZMNNFXRYD3YPe3QECA2IC69B2YYFnsF4Ft1xdM9aGTyPP0EPDT13aFw2upLxj5-r8uhTen2GMJIRUrUj_kivvOW2s-dQzsttFZ0vB3ySFh6Q2I0Lkz_UgwOvHsKwgmXzvXgTpucAXwHCF1jxIufsArt0POj2pw8kS5Wx4KdCz1vW4ewwIg7Ag2iKrCZJSSgDNUEApkdLqUFpeiREIkdtEVd8wwN1sQxG9uXQZFfn2UYRUz2JQxPXYs-_wM6izaL-52itN6OMHTiXVHbAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
سعید مظفری زاده مدیرعامل تراکتور:
🔴
از سازمان‌نظام‌وظیفه استعلام گرفتیم که اعلام کردند علی رضا بیرانوند سرباز نیست اما باید تکلیف پایان‌نامه‌ دانشگاه‌اش راکامل مشخص‌کند و معافیت تحصیلی اش تمدید کند. او طبق قانون مشکلی برای همراهی تراکتور نخواهد داشت. تراکتور…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/21999" target="_blank">📅 23:05 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21998">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=V4OAvhj7pxOBO0ohXRFNWruZc9iZc1wY4nJq4jFr7VY9gD-T83UFKWuqKMBaoqIgVW71_MRggI_5gesMhCgoBHz-AzlKXrI9Ofotzd9Qz9gYsCcYA8WdBkvbesBzOVvCbv_HC15KgeAisuT5wqGYGkeBi3qXJWh4EsD1tHcJn4ni65hqIgklgrSpfnkSmcscGsm5JYmG7VOvP7WYFYusLlgBOO7bFsPYUXtsIQVkOKQMejfnQuiTVhmWsi4YkrtYMb9cg06WmJwzrs9K58z6UayVon3u2bXwYBHpIuPdO0wkOEmfhkOwL1feTFG-lFoyTdkSQjm00PvkRoNhzZNZFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=V4OAvhj7pxOBO0ohXRFNWruZc9iZc1wY4nJq4jFr7VY9gD-T83UFKWuqKMBaoqIgVW71_MRggI_5gesMhCgoBHz-AzlKXrI9Ofotzd9Qz9gYsCcYA8WdBkvbesBzOVvCbv_HC15KgeAisuT5wqGYGkeBi3qXJWh4EsD1tHcJn4ni65hqIgklgrSpfnkSmcscGsm5JYmG7VOvP7WYFYusLlgBOO7bFsPYUXtsIQVkOKQMejfnQuiTVhmWsi4YkrtYMb9cg06WmJwzrs9K58z6UayVon3u2bXwYBHpIuPdO0wkOEmfhkOwL1feTFG-lFoyTdkSQjm00PvkRoNhzZNZFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
مهدی شریفی مهاجم چارچوب شناس این فصل فجر سپاسی؛ استاد گلزنی به تیم‌های بزرگ ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/21998" target="_blank">📅 22:45 · 08 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
