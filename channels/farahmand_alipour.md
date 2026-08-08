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
<img src="https://cdn4.telesco.pe/file/BvNpfs0_zs1ssolnJwKnplUdvs0VGtLGYLby6CmST1Rf1ZWN24aOUvpJerHPcGbp7cGFlRcIkEmfnCgs-TXyL9kWMSj6d9qjPvvKMev-kgupeLjIuzw1aUVX6ZltsSEuxwipzas9yDsyBRMhzvMQcN1rikfmhusfMOT7Mi-Gd3CGk4POk-0DGJlDwu0Q9NwmrxjsrHmF0E8UbqquAcPSWM_gA-5TGEOjY97vT_QjGicx71bEsDzOrbXQzlbOtOdwKu5v4HnY6U_RaKy1KUtPsSdV2lcc5N-nECT3j7HKv5eEz9OVAIvvk3JEYFo8Ln_bXED8a6Knz60UcI4ekndJ9Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 18:25:47</div>
<hr>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=XL8kSSkJ_7NNq_r0BNSOqCRa7z_vvPcX_mcMRUeQxqIamNPNm7XdbDtVTaPaKm4irCaRnlDrY1MKKrxINNMCCU7JSoPj0jenLwVLA3SqbDTEIFzEip6HenTmQnn6hgMGwhSfnzl-XqZv7AqNuSosZAyk5-x4RNofgxQN05PnxEgnHD3EtOsSEkgrLyFT1WgFj_bf8jh6iAdJzokFOZVtu3Y-ljxcuM2qD7eFL7eVCPn8oAu6-z3qSk45Zzm8It5e9DqpvVqhTcinVn2k_N57Qq9VB7aPfWUoVc0rmvLB1M8gv5HjSB9A8sXozIFJY5vtFH1djO2y9dq6qoTOekAKMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=XL8kSSkJ_7NNq_r0BNSOqCRa7z_vvPcX_mcMRUeQxqIamNPNm7XdbDtVTaPaKm4irCaRnlDrY1MKKrxINNMCCU7JSoPj0jenLwVLA3SqbDTEIFzEip6HenTmQnn6hgMGwhSfnzl-XqZv7AqNuSosZAyk5-x4RNofgxQN05PnxEgnHD3EtOsSEkgrLyFT1WgFj_bf8jh6iAdJzokFOZVtu3Y-ljxcuM2qD7eFL7eVCPn8oAu6-z3qSk45Zzm8It5e9DqpvVqhTcinVn2k_N57Qq9VB7aPfWUoVc0rmvLB1M8gv5HjSB9A8sXozIFJY5vtFH1djO2y9dq6qoTOekAKMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=gJj1Dcnh0yUYOP_vezG2WYmanvBCxXx0xxb3VJMyqSXlpYMJf7hT0jU8smjDmm_pFSgK64iXHX2c9V2fbg8VaFv5f--A_HCOC7_nldVB72D5otKfEu4SS-9JF3MxPsvJL7cjDM8OFnPqSePmfwKCYhnF8OOLKGukNvq_GTHoYXh-M64IzulrQhAed--g4Tc5BaTJ7ErVqyayyUCcnZjU62y0mcv4WBn8jR_rbYf1n89-sbANC5_iSjtcKYEZzOaRIpePD4c9-Finjguo-AS9yY6FitFHIP448RGGMuyZwk-V09cApV9Y-FzxDbu717Jcqww2uvHshLyexAXBv_xx6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=gJj1Dcnh0yUYOP_vezG2WYmanvBCxXx0xxb3VJMyqSXlpYMJf7hT0jU8smjDmm_pFSgK64iXHX2c9V2fbg8VaFv5f--A_HCOC7_nldVB72D5otKfEu4SS-9JF3MxPsvJL7cjDM8OFnPqSePmfwKCYhnF8OOLKGukNvq_GTHoYXh-M64IzulrQhAed--g4Tc5BaTJ7ErVqyayyUCcnZjU62y0mcv4WBn8jR_rbYf1n89-sbANC5_iSjtcKYEZzOaRIpePD4c9-Finjguo-AS9yY6FitFHIP448RGGMuyZwk-V09cApV9Y-FzxDbu717Jcqww2uvHshLyexAXBv_xx6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdLyvCNXFdS_bIc1IbVNaHQqTc82LpMCSxuu6n4VQlJWhSHT0CeDZUCreJx9V2e_4Qh2_6XDoZCyQuz6FZwaoQj3CXxBI01u0yZPIAFJV9wMH4MMZVuDyA4R1-yg0Sohj9x6KSMX6b7oPx5oiiQIqk3TjYZHIPW0T_jrPcLgaxo__tMMNOeVQYrhjM-TTP26VUKZAK-rxRD9xrvdEx2CY1x6rnPq59O2ksprYB1R-tF5sh_hAEW3pfiHMvQ0qQG-EQ3DP1pE1-OMgi6aUuoT01zx6Lg6Te8MFR8BgoGzo1zDEMnFU_O4ZpQR-8SzQ0BLHoHIRWfj2YFr0wNHmKAxeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcbbydzNeN4jwXJ2fjoAsabw7z2k_kq6p7E-nEsucVLrNjRr-GZohQ3g84WNHGPC80rSHNdkN3ZOyoPQx6olvGqKcMvahSk_oDupm7PVb7gG8XbVnwUpkoXOU-ZdnjZPYf5WoNJX9pkYFz10oC_W77RGVufL0d0otnHWMR-8IZU0dXQQRWDSKp-By9P3eTOO2aWDXyifrDPAInIdWX37bt4GGd9Do3SvKcrjzD8naE2pF9knFA9k_tWNMzsnqY3nUscTPoeV8KMP6z_n3TMLeQoCiSQVlyoyG3MFhBa_pkxchDiTmRcrsefg3RPvJzjy3o40yjNlLjSZStoPf-JSMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hV7gLqBKZrfjByVY7QaIUccjb1JgxWcjW22_h0R68A-p3rPPdY8y8zX1IQgjt_B_hvqeSelhS1u-zActSoi-fxRQU7nOFNyUivM0od1-ctampvOwVYtgmBZeu4y736c2TZyAE3RHGFSNC_5lt7j5H54Q_jdA0avHP919h3lKBQGTr7xJbBoGEsUCGwn9UAakOwBFOkPY3m_UoE8sz_OXesa-EiuAeNUiuLWCBgbFBa-wwxIpcJ5NBgxtBFvntobc9rNSMsGRgyU0cMtuwswnPiFysiQFDAUUu6ez88BKopyaXrphjqh7Beo2rNSsMJ4CDUr89j0sTuuIq3f11da1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgmoePoLnsAuEMEASaLv8YGMFsP8RD51CFedu4c-7jBVbSnRFyzGZk0VhqOJKX9kVXG9t7VFMfiB3B2QGBeOKoe3_oKRiH3cw2w9inKnsCQwsEIXPIAEgtlEUR58JxjsKt8lIlLpPdtldN3giFwIdrmLkx9kMD0cGiXAGhkzT-aZ9hsy0A_OaBzQYEMnapklF7z7y1xeZvHNQragUcIi99gSzVKZ3KHjSXKf1YUU608mpeq7sMPeSy2nMnp-VYl5nV4CrisDHZbjXaBrhdD-dvJVTSIspejLYJEWQPekoHKIBO-MGurmxYg3MJVH-xUx884I-dgz0R6tRE2STNPrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTj6t-LGZT-Mo2KAEny8cfPaEOyk2dFXSAboKYA9pHsZTMAvy7kQGWz3lP4pY4QdFKIavvQ1C2eEQeMBAIK63VJJ8xvckzIgx751AFQreD_9_9F_39dgqxjhMmIlVz7Ua7PQl3C3vev78vpvtZ5xcH1TP8j7F2F1tRy4ZgSi89oDGEqLNGYywu5rfBoKqyYnft1JseOZJEx5FKJW_TBV4Dk4AB4gR82KiAnTvUzWnr9lBxFcmpdTEkYGb1UJnGQ7AX1jUHJ_4EN62DnTa7QxrmJCqckmOp_f27o8ksONFBTvZQdXHrmei---HdovkwffZjSDYSvGPBnXv6ybjR43sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKoVmZbRp6SyGX1wNeA132sy9Km0qm9s_-TcVTygDq3mr0mgFNM0LOIYi5p62H6L2dsdpG1m1xspBtDb05HJPbAF6E6sl_0fugg-EtfvWs365A6e8SSRliLH18CaP3-EGECSNoCee3Zx6KkUzBpLAnhlCAMef8NV_-7auo7CkqFUyOFqBHkzZ4jjpf5WteGutXWTvlhDf0sKdopXHb_Y-dDW4Js3sg4re6IwTGguatr0BAFMIAFRmFd3gbrGlfDlqmMZ0rrT0tC-UPIzf63lUWQxa6YnC2D_MuNcSYIxByvCD1DItcvXTdbUM7DZ8CcBSdAuumUoqjOO_zGY_UsKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twDU2JwCGxxrM7vJYM0L9jFR3ygrVeSQkAH6nNyEamEckbbyCZMbrbHSY3Qxn03FHKHbAL1i5O716ojyqNn_wTcAk6XiKw7cdndUnNZMRTreBM7qaO_yKrF92Ajt2Xt4vDHwNDPVaD0fz-zbNhv6JXyf4kIMUQ2fLHPEMgUAK-pE7YcKNwMnKsCzTK8rPHfiSZyr6PlbYVBU-tmEUUmrHp0ZDW9ueolzpnVxQHu0V58N02KdXd5Ju7ZxDlsir2TqRU_plFWPMVX_QmEZuB0b5OgajpO3Ppqr9ZAGvmscadHTgME_PWvVfP50nxy3eQZ57tZHajNg_HBUa6oBCrTbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pZZ5xqcAK9C6syyZLvz47xQ2Psf7hsjNNo6mJTya7BsDpOGRL9_B6wE5wnGLQsIKBJxXqTEXBiaWT9FuZDJ5WswDD8Gnec9wGQJplKK_5rR7ko-Dq_ct9vVMB6dZ2iB0TRG2xLcvPur5Xbksbnso25IFZ3sQgiri1iQaWLN5H9bdrZHL1U5jWGPLNc74vOXvHY7_mCR7yEI5U4-ibzreEhVJYTPmM3_xheKPrvTOC1_uvatq-L8wZrSmdV0iyfZwmVsWVT2rB8kmF3UKJ0y_avxjTRq8jERiEyAXtm-oC0gOfOEQuVVFxjAZYt5n8LQ39o2qcsUqETPdGO8fGYWymQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yu9QD79cZ8HX9mJncqkTJ_nbaPERLjKvGT3xvEujykKcMR18Am60YEmm0cYysluTiug3-owIuq0sHSnWFC-JlOGcTs5VCrcgB10FOzS6CExiXr3hkrpXqn4koy1Q5OMIy2QKixnLdJMlsDGnNd6rxhTA4sMlzp4IDfmc46pH9azimWy1h6ScskGi1AkoFyuTLJ5O8cTeU0VFs7zapbbE05CwR_M4PvDSwiR_owmGgHLuF-AD9eviuEAS_lFsy5hGs7vahodCDg74quenbfX1AUaeYeZxBgHwSWJpHvBbb9u201KlHpSt5urtAWHSw-QtMwu1RnIFf7Ncm7LbXqv5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=IdN6cm-LP2e32QdzQQOrZnmPw5zA4wnlIbKD8jLYWqU1L_7ylluZVxIdq_gdkw0etEITMo0_FLJQNjd4dwQL918XGYi-JK_0goNnrUi6sFvkSFXoadQMPzRGLlLzE-hIUZneEZY_dFj8QobOJISu8gVPT0GDk4xEt9IeHzoM7kZr98IswtIzsdeJ1HD3cZ8cDIW2OylL3UjmLnRfYEVcTABGQ9z2wOeeVnknCJpSMlu1lmostM3tMYYTt47-TKoW95HOXxI7GK3kY9fzWaDhaL0wpAkF5MQjotnc9XqRE6pwF3VFF0dLbw44_Dyohgqn7SCkJVasYs3d6b6ioSxnvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=IdN6cm-LP2e32QdzQQOrZnmPw5zA4wnlIbKD8jLYWqU1L_7ylluZVxIdq_gdkw0etEITMo0_FLJQNjd4dwQL918XGYi-JK_0goNnrUi6sFvkSFXoadQMPzRGLlLzE-hIUZneEZY_dFj8QobOJISu8gVPT0GDk4xEt9IeHzoM7kZr98IswtIzsdeJ1HD3cZ8cDIW2OylL3UjmLnRfYEVcTABGQ9z2wOeeVnknCJpSMlu1lmostM3tMYYTt47-TKoW95HOXxI7GK3kY9fzWaDhaL0wpAkF5MQjotnc9XqRE6pwF3VFF0dLbw44_Dyohgqn7SCkJVasYs3d6b6ioSxnvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDY4yjNhWEVIXqHcYivW6UchJSqoA-WUSpcyRzdljJmf3HHN0IZFpRKWfyLTxPkmFTOQflc6MotNArF_j-Lp1N9jXZ0FFVDn9IUFziGosE9PN8agg8QgeemLCe_gsHAwjunCetzkhluY8DAw6DWbXLeo8atWUGM4M9NlH8b-1ahLDWt8gcMH57FB4XZ-G1nilaYFQi_y8kL13fIo96vRNY_TVO8EoQuxMq-p5RfhOBPKOKiifVRPZ2IDSNF_340n9Xn3ffNBI56GmA5ilM_qZHgv5cbaQ9CwWZ3Awij2xbXh0YovQglKsrOVZK3fNWp5wCd0CH0STIeZRimixlJgkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK4GAvnZj6a5AYe9HXxoYp0VaKj36lAm7uV5FLTa2cjE9eDPUIjzCxkSpdGZDAfYxswCWJscl4N3-uPxsb4zSqoCUNfa_zYDOxp07gQD_ZlFyXI1t2_LGnfet1oycBjebqEVreRNvCjH__FcMHqVB6AyIx5AA8u1r9chmYnrkmcc79IG2TEb10iEjvHPL0Rd-8jXQBYHGxb9QO2F8_nfhTH7vyULeXZUOafnRpf9Oumyd0RzqihijcsYu_PbRIBa_GEIyhvehCNo1Gnk3b1MI7aNc7EIZ6inUjgUD_PUsEbbekFhPqCPzKgZJ857KtTe5cBkdvy3CriUpwJfup_y2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5453Runc4wcSFdIsjdVea6x3O6TCEcaAVJinB8sm5gUcZlDYGqP5gQh5OfYqw7DKK3OEehWwZsQ4gXaTdSdPVg2s8svtFhL2Ntq2TBv5yIc0fqN3uhh7ovk6CDKQqJ_qoxP9aUn80wm_YV05VTnNuxbCj9iDo22H8qu2XMqvEkUJSATokArftGcNu6eQC5lzfKKRjfANQcGJTjUvO0R0LWOmHM7sUyvOokWcsXY7QJqeOlydmKPPkAiEA0ZLx3tquTxiJEZZNH-pPCWG8V5oMm-DbSDW-7UZqIcxRY3qZiFG7uB1pUeFAZg5-mFbsmfkTUHfv_HBLzfXr81KP3crQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXbT93BjmAGa8Kc_2pr3MNiakSpQw2RjuIlsWkt-gCzsIJCumN9M0PvK-EL5k82wfh5t_U_IwNTFTjOyRIIlf1kM0L3xUhzCoUGoRVUoGbxk-CQK5IKwi6MqiujM8UW0sfuIbUDz6iVuIzEAiY-mV4kO5SfMF0-MqweF9PnRzhev1Ih2YXohmGXCjdMs-MHPDFH77yZyJBCJwYjCxTeCXYMDhW71thAJ4gZO3Xh8YTl_YDz0zaN24VkFCOfwk7aooYkgOjSOAvKJ16xaDmHDTJU5AVGkfvnGb-KLD-wNjm3_38OTDQiiU2rLWL-JvZNRWp9so2AFusmA_MLBimZzcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8oIwF5pbaY0Hy4jyJyW8qsXX5e9Ac8LvW2IJB83NCJiTzB9XCdzJlyGWqxHcC4GvwgAvT8Uy1Via0DQouCraTg0lI6Yy9_3DMHu4Z8rqjB8OsmM6MpNdWc-iHDG-u4f23cTSnBk7wwZwiiqKA_m3mNdjeAsWWHsbeQiPdzS0oeVb7k1ZkiekfRW_ccbjaGE-pHDkKGhg0GaZs6mCvoNdu0E1z-zrQE7HDsw4BlBX3vB1y6Vjl2CAI7AArfqtfy-8KQMZ-2L3U9LtObM4I6Kcef1z3o08OsnI-cVK6pXLf9HOJG2MFuYn_8KLH2JJ-qjtZmyvxzWfacP0jbnuTGnPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VRA7gZDaiIAYneZTMclLFJYovGYejjyOqkXdW2o0qxn0ATmRrHk4wsZK9hXporL9yt30QUFxEu4RUOvs3mumJejdFrhkMa0RqDF_ORYEJ53A64Cho8PIQD28dna2iOWwEiDhlGSss6VCjDu_Y36S-kfYVzLjAh4ZyQHlGdtV-dDWm91ZwJurTzbdPgjIKJMqjgJBBFW50hriE4C3TZECyRMzqapg2TwbVydAatJhYB8OUGtSHUY3Rz6wRzjUY_NK32Sy0x8TscgQU2MOcUa7pAQF1Eym48RtzuoR1FLxMRq-rU3dqqCPLyOhW-8F2kAI7MVaaoBhDXDqx3c1p_CqEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7zql6YxTM_3I_ZmYTR6twBPrhxFFN2bMxSBUNbTVQ7AlzpQxJmpBzNcmCSdDzUh2-NIrnF8WYENW0PayKphRk9XdxqCoFP2Ff6NDXy1zb8ksLOvIpN8cSTgqSvMQsG7yQk_y79MFRv3KdbNWplSzfPUiljzYOGrCDWNSzA6prNXdC_QU6weA5Fz1Oz9mVFkyLhVNeorgvkgw7QdqoTxM8BIAFFbI0yWmqz12iFSI9U03wmsNaq8bVRjkm4A5Q85Mjy4YtfT6_5lKAqIDOe4uxok6oK0Iet_2ux3-D-Qv4S7fooCUcEc0kC3zbhCvK4YnyFfqQsbnZ8R4VuJ46ZuYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=BxMfZdXD_BdVfgaF5HDrVEhcsW87h0i69wqXdjiHXQO3ObmvhHHfLc5JzPBX6Yjo4k2jGTCp9K6KmHuMQVlehCSXcDVS3vJ94ggTuxVXIJk16yYzHczpluUvD0SPQ-cQcVsy0IjuQ7crzaHdqC3LzCzwwVXsyVHhwBmuuA3UMutQf1VhADmFcEQYf3cUiQaouVCEc1YMOBEFUMpphvw9Wgk00s4RyrprkK6uNOAscbWU8BBJJ3q2vq40zSwQXqIraAoCwtX8RgMn5xKDrLsHQN6__5vk11Sv4HPX8VZUTtyqCuT5wTpCsd4g-eT4AvltxH8p_UChkFWZRVQPALUs8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=BxMfZdXD_BdVfgaF5HDrVEhcsW87h0i69wqXdjiHXQO3ObmvhHHfLc5JzPBX6Yjo4k2jGTCp9K6KmHuMQVlehCSXcDVS3vJ94ggTuxVXIJk16yYzHczpluUvD0SPQ-cQcVsy0IjuQ7crzaHdqC3LzCzwwVXsyVHhwBmuuA3UMutQf1VhADmFcEQYf3cUiQaouVCEc1YMOBEFUMpphvw9Wgk00s4RyrprkK6uNOAscbWU8BBJJ3q2vq40zSwQXqIraAoCwtX8RgMn5xKDrLsHQN6__5vk11Sv4HPX8VZUTtyqCuT5wTpCsd4g-eT4AvltxH8p_UChkFWZRVQPALUs8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=f8JkjwVgRy1QN2T0eE1eZ3KZMPDwHbzliH8-OwvkR2W0bt2I1q8ROmZo-KRAl0O6KYlOh9Jdo3-OpSKqn8rmv1t_iI36mYHt3Xl3i-V8oj2bY2zWgnzKIb9AQ7VHiQTCAxjdErv5pKbu4A8RVP77YSDcaz7bl5D_m-07AlUGC373QXn0io2OwaqMvgnwlApIWxDQO-RFo8j09FuiPxVEK0qjtyI-zM_HvfdxEp5FTArxCclvguq1WKMQondEIQY5B94VLPTO6rhYJ2L-xZ4rbVyD0yKgbZW6X7I99qnHOF69R3-Mzbun9z-uNbdgOzjIz3_bR4Dut_aXF-PstSy63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=f8JkjwVgRy1QN2T0eE1eZ3KZMPDwHbzliH8-OwvkR2W0bt2I1q8ROmZo-KRAl0O6KYlOh9Jdo3-OpSKqn8rmv1t_iI36mYHt3Xl3i-V8oj2bY2zWgnzKIb9AQ7VHiQTCAxjdErv5pKbu4A8RVP77YSDcaz7bl5D_m-07AlUGC373QXn0io2OwaqMvgnwlApIWxDQO-RFo8j09FuiPxVEK0qjtyI-zM_HvfdxEp5FTArxCclvguq1WKMQondEIQY5B94VLPTO6rhYJ2L-xZ4rbVyD0yKgbZW6X7I99qnHOF69R3-Mzbun9z-uNbdgOzjIz3_bR4Dut_aXF-PstSy63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBpczV5I7EaLMt1nAEi0Pj_tImjDwsgpHpB0OgD2cV0-eRUPIpQ04X5muc9ukh8FIE3yXkOgMr2IjaQc6d-o2b_Vv9wSj66lahNuhvTaFP0hGOWX3XFO_cI6k6TpgqWM9ugNN2MYe7yUEnyhwpar6NC_X3Ipid5yZWIrZZDq_WUQlt4bH5O4A8nDwhUFfYIebGoeMFXXeHmk4zfL9rSllZ6aqPmgMNp_RoDpnoxIfkY_R05N_iIoW7oS9DbX7WiOTveI9ut4iuN_Bpoqyl6QfID5ovDaZlvfPUJkCZ_QxXsXAIc_2Igmw8OC_HwbD-T1mmyiAhpfT105jj9i0lXM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF_Zkmhk5MoJZbcu5nf4sOZ2Gjmt1P1c8s5LLH2NMPoTatUSR9qnKA2FI4Na8jOCA35VclC1Sf8Jbwmb85-ykZq3qSiCYWhhQp7e685YqQir5a3TPsnCkV7WUWMt_hAGMRi_uqBJC-CQxjZOLiTWIFmvz69SMLXuhefzg1P3Pm7q_AgBYzUNBatpODgx-koSPHEg9SNVZOlFEmlp7cqC_6izF0bou9-47qTpPa3yDlaKZBy7U-q6oR5ndVADvlhnQ4P2DG7XPHT2xPzgu2kjSUZIppvmpxfw9_BPWrGLVbwm7Wr_WuLlxnht5BkC8nA7vaErZLdZjMCKjSE1-ZkNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=UZ8blXWnRbE1gxSdS3iyFWH8-h3PMmNJHP3q0LLn5-WaFYaFekjID_tnBXrfTuG4EbQ2f7707dCbladT3zelDx3qTAop9Mvpjv7YOceZu_4kh0CEJcwiFbV6bPXeDP8oQCId-X1exPP8Kx1Ch69UfE8NUEbg6phI6ozOFs-k3bwrOMy260OXssDVz0qEBuvrzyLEOFBJc4NEK7SaWQ7qd5lmAU1n8zJHHKpYIzBpzLK1pFDWd3nh__a2QnDCVKHPQZTq1ngL65kdR7zsznz7PHcEEfMwI7W0uSbMAIum8FSLYUi0IlBDMx-x27f4r-Y38hG36rEMkhR2Sm0OhVDzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=UZ8blXWnRbE1gxSdS3iyFWH8-h3PMmNJHP3q0LLn5-WaFYaFekjID_tnBXrfTuG4EbQ2f7707dCbladT3zelDx3qTAop9Mvpjv7YOceZu_4kh0CEJcwiFbV6bPXeDP8oQCId-X1exPP8Kx1Ch69UfE8NUEbg6phI6ozOFs-k3bwrOMy260OXssDVz0qEBuvrzyLEOFBJc4NEK7SaWQ7qd5lmAU1n8zJHHKpYIzBpzLK1pFDWd3nh__a2QnDCVKHPQZTq1ngL65kdR7zsznz7PHcEEfMwI7W0uSbMAIum8FSLYUi0IlBDMx-x27f4r-Y38hG36rEMkhR2Sm0OhVDzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOT_ufxXlnbEEJQMl2fwPCEc4LpA3k1ErcQaV2E4nBBoqzGUIOnpQ7Pbg5CFOzk3IX-ZHsMXhxRd4KXvbi6e0qWEoWTM0ylRBmX71GLIaXD_5QMPHgedT8MDQPbeCJztf5sk7HROqUNXePIIM25XmId1XtkG57SXvan4fgzD1xHk7PN5IaNpplBQcruOElFgphPFE9KgvSgNPL4hZ3vHq9K6QL34GmpK7Qry7cKhvvIigwr6FaJETR6CrTCq7blrI9G4vHFhmXiOvWJmGDdw248MFiHl-r31qwJomYr-AGs4YbegXVveDMorzdCiUn_SpXoJpe3pyNLM1JLH-n8BHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBgrS-xb9tlW3TqPsezmCPcDQnbhrnj5k-SAC3XVEX1ea3pMrl1CJeexz4r1PQMeStYd8MK8pZ8fIsJNZbhmmRz3YMovU2aEP5d5mi7xwSIuaVYgp3WMGPqL5qhYWEurTwUpRprvBeaHL1nOOpYpjkMPO5rdBlq2iD5zvI81TDPU3BdzbXkorVn7TfvnOq2KyqrJsCj_iqLOFJhf3XyX17-0GsQepDoz8NsZVh-ScrADoMyo80sDjITL58MWeaHybzaqWsMia-37I_BEgQbrC3wfSWfnNs8HRGKehku7yjJ5CE1ko15Pa3_yxx1FmsZxmCsdX4ZhahhB1UcMF-6LUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=UmCcpNqRqN7qazP9VMkZ84XRx__6Ru_U4B1vM_fM2iiQfIO3GIprUvrPXqmcC0mpUMb2oYRQPdElssTwNSTbFmRHQUm-UL4Fai6TYtpRTYISWmITmAiSoxqerMcw2Dbz21G4FlQBE1gpqL5oqbSXdsaPiHFZckdMNOSpAGlDR-AK0k0dMGpsOAPpfQ4PkPoPKRzVzE46PZ8qOVZR-ljYYbQi2_WKg37t1P1kL6qCFzz1JO0i4tNJ_h9LFqg8-nZvd9lRfbzS0uCK3QmAcL7BvjuA2O94FXmiV5QPXQfwWAcn1qBLc5gaUIXwNgoN_0LugnffKz7NHec1EDStxGrT3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=UmCcpNqRqN7qazP9VMkZ84XRx__6Ru_U4B1vM_fM2iiQfIO3GIprUvrPXqmcC0mpUMb2oYRQPdElssTwNSTbFmRHQUm-UL4Fai6TYtpRTYISWmITmAiSoxqerMcw2Dbz21G4FlQBE1gpqL5oqbSXdsaPiHFZckdMNOSpAGlDR-AK0k0dMGpsOAPpfQ4PkPoPKRzVzE46PZ8qOVZR-ljYYbQi2_WKg37t1P1kL6qCFzz1JO0i4tNJ_h9LFqg8-nZvd9lRfbzS0uCK3QmAcL7BvjuA2O94FXmiV5QPXQfwWAcn1qBLc5gaUIXwNgoN_0LugnffKz7NHec1EDStxGrT3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=be88oRG635V7brcYoIhA6he8h6Mjg7LF_sTGIRzyMVg8aB1USXZBhj_ACKEiDAwc64d0nEhe7Jji7hC7eHmANNy6nPuAw_-RLlCmqjVfMSt_IS-pvs05PbwiW24iFsDXHqj2mI9FzAilbTJfr34bmqEg_kjzeRFPjGm3Y1JLlHE2HoCTFvYOtJFsOLJkoZvtAiXtO-RhmN5yZnOOreiLNT1cVUI8u8ScW9rDXaFE77CRq8B9N6MdhtUeEsUpzLqVeJN17tB7t9vh_RfqaWeC9C_kc7cSL-6xQ2cK7PGSWupIBiPQTTFZHZjg_MTH8yBmEtz4J8-7pYzsxEZMMJUBgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=be88oRG635V7brcYoIhA6he8h6Mjg7LF_sTGIRzyMVg8aB1USXZBhj_ACKEiDAwc64d0nEhe7Jji7hC7eHmANNy6nPuAw_-RLlCmqjVfMSt_IS-pvs05PbwiW24iFsDXHqj2mI9FzAilbTJfr34bmqEg_kjzeRFPjGm3Y1JLlHE2HoCTFvYOtJFsOLJkoZvtAiXtO-RhmN5yZnOOreiLNT1cVUI8u8ScW9rDXaFE77CRq8B9N6MdhtUeEsUpzLqVeJN17tB7t9vh_RfqaWeC9C_kc7cSL-6xQ2cK7PGSWupIBiPQTTFZHZjg_MTH8yBmEtz4J8-7pYzsxEZMMJUBgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=V_z2bkA9dwbFD3_dpGTu2bCMbFyzmSGHv2pDv3CQUyztPlnqXuoMDJwlHb2bqtSXsoJz--GTRcwrZqsZXf0Q2Lb4xS2MwxZtU5yhFSlD-E8nsxnJW3-Tx1LFEX56t68LecqvcX13SA54ycxcutke2uifqLTRIEXcAQwiU0btp39wUomeN0u0WwL6lUBKEWHDdVDikGa78eJmiNqmBoufHKNd2YLDTsrxN-1c5CwH_hFk2zUDRumGletXuYO__z4JVOlXzSfZnLmp7oPp_nx0b72qoxBVkhR5nwJSSSM1TYguAP3McwOqs4JvvSFRcR4dDwLCMNMabtVA4sY5xBBSBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=V_z2bkA9dwbFD3_dpGTu2bCMbFyzmSGHv2pDv3CQUyztPlnqXuoMDJwlHb2bqtSXsoJz--GTRcwrZqsZXf0Q2Lb4xS2MwxZtU5yhFSlD-E8nsxnJW3-Tx1LFEX56t68LecqvcX13SA54ycxcutke2uifqLTRIEXcAQwiU0btp39wUomeN0u0WwL6lUBKEWHDdVDikGa78eJmiNqmBoufHKNd2YLDTsrxN-1c5CwH_hFk2zUDRumGletXuYO__z4JVOlXzSfZnLmp7oPp_nx0b72qoxBVkhR5nwJSSSM1TYguAP3McwOqs4JvvSFRcR4dDwLCMNMabtVA4sY5xBBSBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNPy6QHWPaSVKiAi7x6Qp_D51ZrA8WU8_MRw25heY_2gmF70z2z_re7Mwaq-Stv6dR6_gqizZiw_QVwzduckZ5PmR7XC-WsJqd1J4Xp2hpt9bScERrmKC9xszZpKdR1A7rnN_h988RcSFVcQnV_FU8qmmbqSp7z3hh4g1XHnjLb4E9NSx_6o3dKH-xSrvBB_D51MhYiDFmwR9gWX4YZ8-4ANdJeGYTdL7VJbmN4Xo9voMTL1n7HUpAjF2JbRd2gTGK8RBgwEYbsLWFHs8XonMyVncUET2wQVlMyuGuheuw4Lp04-1SNflKX-oifLjXYJeplDJZoCyrkFS4MiSM068A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEBD1RO36NsaG_77J6KdKzVSZB9NrfhDrCvjkeIsnvTupMLnVRF444QPJqGgINyYdlPhz1Mgy-mRZNH0pFbO6pBBue1Ifatge6mriXt5hLhXiq0Toy00uQJQAQbNms2pLcpJdabAhav6niPoemRK3nthTRTNbGEZIFNhQowHrpjbKtbwXtVjmr-7UQ4LYNiQC_6RhZ-F13FwNe_0r7Fx7I7aH7O7AGh8k-efd6o_vqlP-sWUTlhtF5ODo3fxXIs6un37PgX4_rdJvGEEsl7ukRxjYksfmWbpVkN--jMPyqEuxzfkOLW4pX9NU9Pq4Z4zZMVcIIp_aAJm4_AKqocg2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quMFuySZ2TNKnd0-s30K4idT-yZ342IhlY0TqAPFkfaEbd28VBUvUUUfWO2O27Yb3tMuSI1gBVEebiIaGbt_nhQNlxrEkpBYTc6FBwSpiaEHGp3UvRR58m-A7X_USpCUF3WYlxYIDQ76A861gOccgOPh0paSv6hUADdaooZkFfE4AFWevK9XaVadbJtAvqHxzG7y2L7uh9kOSAorPgED2A0_3mzDzg9hwBgOcAHUlQXujAGt4r_mAZaeKEnYaKrbfzbxZuILG9CbWDZHHbLkUVXoh1Ycp7uZ01o361Py80s3ShW7XtdibaCnzvbpkrZY1D7Z2qZYG_vQu9BLH0jUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=K4xk1GRi5fEKJob-SQEQVD3gpB-kYEbp_Yrk6Vu561qTIIMHfEjXt0SADwLQP4trMR718i-ax0b0iCXiC5K62AcHi7t4qBaAIifC1DZfTtxxyDC5SnQbm7MFU4pFlv1b7MsMrSmYkVNa5YMhtZhv-kOXNpJ9IZvH_wKo3bg4BN71V8tNW4XBJz5s5r8cdVJep9FiVueOf6MwGr_0IYyXkx2B-GLOHBIoAM90UtPHk29l4OJr9m4eFNxD4wS8fpGiyqB_P4f-GSx7i2ebY2kWK8r_gZx8og58HGrgbdqC_fgzN-BnoB3WYEfT6-i6bc_RahJhphfHnsDBPyfagDTcMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=K4xk1GRi5fEKJob-SQEQVD3gpB-kYEbp_Yrk6Vu561qTIIMHfEjXt0SADwLQP4trMR718i-ax0b0iCXiC5K62AcHi7t4qBaAIifC1DZfTtxxyDC5SnQbm7MFU4pFlv1b7MsMrSmYkVNa5YMhtZhv-kOXNpJ9IZvH_wKo3bg4BN71V8tNW4XBJz5s5r8cdVJep9FiVueOf6MwGr_0IYyXkx2B-GLOHBIoAM90UtPHk29l4OJr9m4eFNxD4wS8fpGiyqB_P4f-GSx7i2ebY2kWK8r_gZx8og58HGrgbdqC_fgzN-BnoB3WYEfT6-i6bc_RahJhphfHnsDBPyfagDTcMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=n93s2znwCgSxQbjaybvi-zYXtXbWnJWSB2T1Oo45yMtjDEqfTlAveLYgsmtcwQqL7cm-s3aZkq4lAcCM3P3knl9lL7GoPLpe23adJ-Ty3JQ8KMGfdjCsa6eW6VGGy79hla88dxD1TXu5Q9kak0hBkzCE7HW6ERtoPb52LAnV2m2I53uYoiqny-1qTcjSkmR8mMx5l4popgZMXL87BQmy_UssSX6d6BSzwqYZbhse4Dbj43lbRu2nWNHDVS1kP39AiEAPrcPnYM0O6AQ5iwLcuKtkTBRFLTRwteW_3QMhSeiWEe6V-rokFBH9bGbL41jfTzP0eIPGMJlmQEmt1W00zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=n93s2znwCgSxQbjaybvi-zYXtXbWnJWSB2T1Oo45yMtjDEqfTlAveLYgsmtcwQqL7cm-s3aZkq4lAcCM3P3knl9lL7GoPLpe23adJ-Ty3JQ8KMGfdjCsa6eW6VGGy79hla88dxD1TXu5Q9kak0hBkzCE7HW6ERtoPb52LAnV2m2I53uYoiqny-1qTcjSkmR8mMx5l4popgZMXL87BQmy_UssSX6d6BSzwqYZbhse4Dbj43lbRu2nWNHDVS1kP39AiEAPrcPnYM0O6AQ5iwLcuKtkTBRFLTRwteW_3QMhSeiWEe6V-rokFBH9bGbL41jfTzP0eIPGMJlmQEmt1W00zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=uU-LbPHeUC3LwtK8XAetj9ZD4qKlcoJhxsTHKEN4Yvxy1U_--qWwxgRC9UA2QITEfhnsMtKkfGQC-arLCIHbiERY7j1yj8TTJ2NQ81WiWI4-c5NeAl0jQR5v0aFvqgwBd-6C01ZqX3Yv8ytUpHHiMLwyKAqciJczEAtDs4xQjSVBs-xbqr5f-QvKUyOa0j8f6zdVqE7Hn-Lc3uGGncZkAkROcVX_is05R4swK7brqVj-dRwwZ1aHKzNPuJP92Oz_h6vZ6K7IskdEGjDZhNFQRxnhFEesbMjzpW18AmCVW0KV6uy2Fdyis8paOAjXKOV6bmIcdBG516NPxyZJBRjOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=uU-LbPHeUC3LwtK8XAetj9ZD4qKlcoJhxsTHKEN4Yvxy1U_--qWwxgRC9UA2QITEfhnsMtKkfGQC-arLCIHbiERY7j1yj8TTJ2NQ81WiWI4-c5NeAl0jQR5v0aFvqgwBd-6C01ZqX3Yv8ytUpHHiMLwyKAqciJczEAtDs4xQjSVBs-xbqr5f-QvKUyOa0j8f6zdVqE7Hn-Lc3uGGncZkAkROcVX_is05R4swK7brqVj-dRwwZ1aHKzNPuJP92Oz_h6vZ6K7IskdEGjDZhNFQRxnhFEesbMjzpW18AmCVW0KV6uy2Fdyis8paOAjXKOV6bmIcdBG516NPxyZJBRjOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=CBvb69SyJB9UhMcp9RSqxCb5PFAk-CCVe97URkJR3aOvKnzZp89FhvPS0Yv15XNkYo5dHJeGCegM88bbfkFs_gi5yWKDOo3SagKT_uALJTKYQmwbcVC84ONeLywjkaaRBVdkSPuvFOZuXgUNaZGkJ4ub9EBRi3I4cXpowZCkaNHOt2pg21E-XEQFhpq_fxV0f7GtcQ8AQPoXJ2vE_oj6EHmmVwzoaRpcHp_R01AEvlTza8u18UCTpCyIcOaCNl2gqwHtHdCmTYhcVt2E2fuNsl8Sm_cc11zqGPtIWQAmftt4MJLLBWykVlP9LBWod0KvoS_LJjikQ0MnLHke12fd2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=CBvb69SyJB9UhMcp9RSqxCb5PFAk-CCVe97URkJR3aOvKnzZp89FhvPS0Yv15XNkYo5dHJeGCegM88bbfkFs_gi5yWKDOo3SagKT_uALJTKYQmwbcVC84ONeLywjkaaRBVdkSPuvFOZuXgUNaZGkJ4ub9EBRi3I4cXpowZCkaNHOt2pg21E-XEQFhpq_fxV0f7GtcQ8AQPoXJ2vE_oj6EHmmVwzoaRpcHp_R01AEvlTza8u18UCTpCyIcOaCNl2gqwHtHdCmTYhcVt2E2fuNsl8Sm_cc11zqGPtIWQAmftt4MJLLBWykVlP9LBWod0KvoS_LJjikQ0MnLHke12fd2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkrbXLisOSGJbyUp1_2yEawjOskJLjvxMP5mwb74yi_ummT_O0t_zHWw1pyIO2FZPuiIpwX0cPZ_7niKqHzrLRGwyZWc21HdCKy3lQGyR5NlvKnEMBN6LXItdfx6q1nkd-uvoSZtOfwdQ4GGO3g3bGcnB6b0uFvs-Vv28X-OjIqg018wwm_eeRNP8elwOSZj7F_wzexqGe18-oW2adp2YLChvmnbX4T2Ioppn6898oQ9lGFKZRbbz34iv3fZTS3i0gBXWJ7xTicPupClQu0qZr0eiMvNABLBzxqVdm1N8tCCxsfiRgsgRgzYc3SHq4bLFv959NrZZBvFDPF0MPyLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7Ct-C7n76KOWUVaelTyDDgu46hJEDaD5BaaVPnn0PmTUUGvXzJTn1FPsrQZ0CsBoV2_0dB7DZxgXgPdmKVhNkM2AIDyM0roFVvtheaMVKUaJXUN7sSIrhZ9tHu8ygGLST61GCHXqIM3ORijOefLm89P7SgcGou8nZzS4xmhuwSEqCtXoUJYRGan_FXnN75KuQ9hVKMwPLydAAAoChFERZJG0xsnkq0XASERzDasl-7LHuSBkSi2HkMQMyf4W27uAXOi8Xscp4u4yBYEP_e7eB_mev88oTPZtL_bu-6OsCE36QEZIzOryUHtsZ8OAfd3GiAz5GOvhzQKpQboJX8txw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CLXn9LMSg9NZ7J1K8yEgiVgtKq9TpvQZXk-ExWBjG7SPFXPVgCCk1fbG1zXUeqe7KZgOvZKE8rbyttbMl8njNO-5YxosMPP_nSXOvq9ZLylcXEhl1f9iJ-jX-PLznSO8sGSfGz-hQv4GX_pt2a1DvJ41D8F_DpitUDJq7sSRGyrmyuk3SUdZiGhW3FbuvvCTDaTkvVT70RiCyF5zdqrRECB4KWcNeUd9tG9fPK4dHGv9XKG5toTHpJsAgthi1IJCTonaAndc_V1CE62pv71RyIO96KTz-TjeCyxdyBBljyKpkdZgJrLi7hZpzMyAd2z_uJa79pL9FTm__o1jiFthQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iobh8D0uCnbZN-ygyilI4FiKZAg0kyR6FwnIJqFSUTr3OKNgai71uunyy58eajRaBqY2nlxUgo1FKV4thh_KsrdGtNN192oVkuU56_vyvuiffX0QlBpz55U2oQGa5vf90d6MtsWETOnkQPHlaD4VvdN2sIUs93Qs9sd386VYpHWaS3Msqc49VmItIV-w8REuP4Tl8YRkWyu1ZRTFSaVtR02PfIygkUUxpxeSKXulCVDTtxIZgpAegNpceGKkA39DkyF-v0dPT4gLCCcVMq0K5o9QW-Qd7lVRWArGpRZGQJ2VGDvcm1zH_I_0KPJHGA8bt86vMqkYlO_FEbAV3eW37Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l4dzzUBfS1I1F3dcvAUbfGwNAeHBZyls9r-l_QtCyeAWg5NA8UOOYQUM-MV6_Zl7PVCmHn_LfYLChzWpOpX-QX-2iwoLjc6vOPUncOgq9KpXRflm9adQYLL22YuInueiHOw0GePh9RhIHvV1E0C8oba39ccPRL8lkHSn_LQ_6bTlv_EC2uN7aZWy6NFwYC7qi35R0-15ynp3Htuu87Ip7POLwL5-5Y2X8VwVRW6wYRs0x_o1sE2xyNZ2EHkOTzOTf1WY0T1AX3Q2Y-_vDR_kgIGEk2njFwcIBYCvSavPdBGdtDblkvt9_5sKgK50j_vItP_ZX78vp1KU2OXb4QBw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRsLT3NYbO3RvX4J8FBLbMe7mnoBmo1c9g81q1_jrZH9UMZVjAcsmLNjPO7rpTqlIMmkh8SGmr8Yk3PgN5omgfhulhoOkmOwVFT4O5SKyBe4JsH-sDT7Ww_ANrxAItoPEPXWifrbmtJCZBYSbNRrDz-yUwt-ZR-hOkDODnipXyqbNBN9bqgcoZ751xSKRyJwo5lWC98za2HkevrnZeJflfmO7WvNYNIDDxYm9NvQDPlreaPSwlLMeHsXXJYDGWp6kvAh5XbiEpXVzcqImQtMAbyxyZXzvO49tS1W8vkEhQ4GQlsuHlQWUsEnCZY9nWbgrEBd3rknO5JdFX_qA38RTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfX9cIHzRjnn23OGKu3OoqxdONDbqJ7UkRk1dsumFF1Uj65GkjWpE93olvPXdjGJSaKWXVA_cS2mhni--cp-Tg_fqw6Bw-90HrPuJ9CDaBk9K_3hZEW271DcUsb625olw7xL-Obof-GABSrty_MFgACz5_j_IePDpkaslOkpmZkVEdi9or-a6HtaIqjclZVckH3vX8_PesPP3W02rCtElQYhsttXoYU8WjyDJwuV5mWfJhZVeCc6A3q9D468rPQGiMntKrj4vg9vwWdf6YtXkIMDiXJvQOWXd2P4BopgbCvU3Tvq9RQGKV0GDcHCtGPTWnRSbv1n5iHZvf7iV7txgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxY1Kylp3yAaC-UnKZ-13QMYyeFCJDfqHlUW0l6H8nalmRgJ_W3daUSqfJon7lQuG4-JgVCMoujvMubmoOEASjKbn3GaEELoE9_3ANmtCw4wTLdBoY5BwSEJW0Pk5Qf6eJXViyeWoy8ZX8TmuoxqwE6196tA_AzED3XJF4Hd_ltypzdzquuFPxQNqYtM1zXxr-Ygwd98hRcZ9rC_8n5ugCWPFHMGXtGVI-KYYL_F9kHIxXudfi9GYcScU0wsaNdMSWswC5GBcayQYkuy7_2t7z1fOYa6fCXThpyHa9BuixuHVb73-jg0PhFCTIEZMvQn7rabcz5zqKu8Y1dKaLHrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGjeGz7tmUPdIRfSbvvofRslDF2IwfpCm9DDBl4jNihJ0HEC_nMzkdkfYiiBhWHTibvtbZ-mnYKQWIvqpIvH3AlhcGmGwLTJsLWlrQRgKFRzJ2W8qqebFPcGDs6rdmH3BCKAMYWDMIGS_DFGPo22Y4n7qtSg3wBLmaBYTiQaO3tSHHaboKz4GWh19ELVNj0K1hdNe6L26CnfH2nDCD5DFyusOxksmCbHDfV8qrsjOQ0lqJkRQdNxUWwGQN-cf3PY7rU2hhld8gcW5YP0_nREYNLBoDB_ymodzBUqfaBKG2wWxBp0tGB0cawBElPGFPXtaWMbkNmqU7ysM9zxmdcWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mcc2dvVBY5z_i06duLlUL-6AdvWMl9tz2OlheM9NEPAnwfNri7kkMaVmehPg53nApLmkNRWW2t8jtYnUsuY4aMl6jkSJy9zarstzeBGBrmrFkHF3D2qWyHUMdUdTWiz7IR5khHyvU5U4dqBECE8L-oR6c1F5cEEPCTKHToE6ViLueVEDHtoAqkw90668DSk_IgXry4oC7BIrCAhEEEg-ip947VHoIqVBqeNBQSMaplfylmNI4HRZxuQu9k0ooVWe0YPpGvXt1F3jke6myHEl4cSSTLpdDGxxzrPgf7TzyCFF5Wceacc92znCtmRL9I0IUiy4uwVgdC6wzqSUtiNRhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxANlB_j1X5addyDh4_gn74AoH27ZvFDmVgpSwdp-j3ne3spYc8k8IyW8hLHuAqqYgZb2dFnoqwnNEOLwPRYcjNS8GbzaX0WcQPWKl31zPtB9ecZ2B1yBVr70hI1xt52Th76zBOT8diC0zitvMIbOrI8NFsPYWWBpujDihMeAEIZiA89gb2mo4iEIvd-DMVits2142pyz3YjDNElrKkt3lh02VmGH7rrRehLHJsGmmL0atQBn29tNu0LDdCUbuw07RejYd2TJhrAUi2fnbQImu4_TW5Tj06a2QFj6mLhDfXBHbfLkaBdP345gXAo3wWKU_bK0lE4bSBZDM9UbQjkQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPCNUL7ondckHH-1uipAIOSKMxvJshtzxpaPH5pS7Spc1_LjzIxfaUzltX0TYzQhsUBWv3YDrkfS2j9qg13RcQ_J4FmtHpAMk4oV_ZE7p6KwDg8wzYJc12iL7RVbItud1_9wvm9F_KZyohLJE9C_F4qhpqca0rM7NFchDBxP4PnKAAPhCw8IUqrAdhMcfS1GhFr9Cb-ICGTlgO9jf_pBl5H4zzmc_vV4rz_H7IVPcq956pu8mqs8kncfHQfPIeqpNraqsnZDdZT15UYa5GilRhQzmF-3HLkK6msHLtmKHYGPJr0UY0CuvkeLsSLDJKI9oHLucVVVM3IJEMZKUTfx4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLkurSXByCjcfsPVuOAKtqcv9IxeMdBd4XRJBM86eBuTcsIHlbQVTBl8w1Il5X38MP1HSE_9z1bheZvg7W72Ld6f_Ce9YmnYIFg3f8Ib4tAl0RCix1_Gtux3N3Uk_5JIRia3NwgL5xbORG05GTK9Ek6oCJzY4kfazoPzTAKrB3ETHNh_MQ2wu82-5dIyuFbfN01AqgMgiCh267dZgKrVdSl2Azg2J3BhOvXSCXgr4kX0mevo854HRWyO6ijD19hnXPZ-0HULaYQVVmIGYIZXkchdVAdP__Hu43k23Q785WodyLUoAOyPIlALqZPv2l6_dgY3BM0X8CO6qeinZ5WxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBk_HHj214dbPGGtKjW-TJd2aqLXahNMt-Jv_-smrCsDLPsyScIUJAGcpyVkU1p9K0_E-lA-r00opc1imz9-BBxCs-3kDs2GA0XYATPzEsyXkxbnc_5Stx1uk7z1fMWfOpif_Su7Cv1Vg2vu5lH2o2nOzAHEna7hnFAaaGjmsH57lgMWpDP4SkL0kgDWg9HS9cE-AkL8kQDBOG3GEaabAWhMfXtNztcLpUyTEHLcXKo2pFaZK99I3C0cNm8hBaaR5E1Wo4C8iOMhKVSjQi6dban8V6Jr8xm5y0AeQD6uJwUdH_Pu0QBiQoGgAFFovxNAgsIy3DQKS8gSlpHiSC6MQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=bjVlOFTnb6ZAV4l4nB_myJ-Wex9VIG0_HTz-PgLderWB3wA9uOw0xYpwY1hMyePkYlOrKfiNlVy5rfrrBPy7zBGsJyJ8Bmw7kO0esBwTQF955Zq13gCqK3b1s25E8alwDhlB7rHY8axiVaNRU_dJ7ql7PJc54YbmSR4YdzavGHoOK3aqgY5S3mPAYkCfnQBxjTl_Ei3n9V2SJjB6GxolALiHmbRcIblr9NnQJ9SygY7Hz4wQobwlqsd2lG9OAUY9VcFU9JZlD-A7ZFaSokv0VWECcGV4KNVE01ZgK9iO53WaUxTYCt7imyBzu80MgqV9wErX1uGEiFhltgB_NRIKTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=bjVlOFTnb6ZAV4l4nB_myJ-Wex9VIG0_HTz-PgLderWB3wA9uOw0xYpwY1hMyePkYlOrKfiNlVy5rfrrBPy7zBGsJyJ8Bmw7kO0esBwTQF955Zq13gCqK3b1s25E8alwDhlB7rHY8axiVaNRU_dJ7ql7PJc54YbmSR4YdzavGHoOK3aqgY5S3mPAYkCfnQBxjTl_Ei3n9V2SJjB6GxolALiHmbRcIblr9NnQJ9SygY7Hz4wQobwlqsd2lG9OAUY9VcFU9JZlD-A7ZFaSokv0VWECcGV4KNVE01ZgK9iO53WaUxTYCt7imyBzu80MgqV9wErX1uGEiFhltgB_NRIKTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psn2nb9szcgeO38OZEcb0vuOcNS5LszQPwESUWfPdNWMMtYwdZl1IMzFezSc4eaJSuYE4ckIV8ryfTSQP6tNC2MvqYPotBycg04do_aeZoMP79Ix4kR7jODBXNSK_FBITExuXVz_dUoHLOUFj7cJHqW_QRgSkDdHoExrMapi8Z_dC6r03mAQesXQbGKpPGEVi6hNK7z3Ny5QvWdtfOydoa_bXlPPE0Q7x0xaET8e42KeKPkyLyhNji9ljadVB28LSyWHAttkWz3parK1E9_EyNaM6DUZCGjtO9jgI2YaKeXmwbxcN_hG7K6cYcYR2mglIxTkzX2_Acm0TbVF67rdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE9hsxpGtDZ8G18mn91qWHtWFW9CWjnXsCiG696d0JeZkb9vCI1ppWXBPQWD4GpokYG8Rc1ncwyPZFCb08t8WC5F4OiEYU7GC98OOoCQzmaxXdK0PKUWPqco77rjKchsZoo5QhmJwVPa8EEyVTNCXnjtEwCSm4EkvjaOwhSgdpcAcA2lTxWjDZb0f1vchkrjO58QRhHCoeKMsbBnEFp-OCvGjq4cRDkIGDCVzYSVooUa0_PscoGVxsiIcNXfCqDPESQCQ_8BuY-GijhUd5r0Jo1CnZIxj68Va6-fntYpJ78AYQIH0zLFSG5hBxkFTtZbzdX_VLiV9ozhfXbbqIaL9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEMas4cOD_zlUsbqDhHKRif6kZkPGWnmr3JBt0cTXNpd3pIEAzgVHu3lsek4rI6GFga1jItwkbi_sT2vbagXXPRximau0tfi5vePissvqt2n5zGsJwFPc0ikW3Mq5YSNjLnF1uZ6mlZ-1wcrOmuxaC3OPog-7eNFYzvm0IdpM8CejUKRiCcBPULLU6x0WvO9w8TzVl8rE0v9dh5qezbxsN5yIYKDOPSRpwSXTgH9h8GYXHIpF5oaR6akELTZfdW8ZYQQ59u0r9Hzmrtrre1pBRfbvWmU5mW4XBjrY4hwDR8G9YADG0rWWEytH-fKw2AeVdlVn5S4WWB_14jmuzwWvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjmfbX3t9ZOLvxrrdMVKf3YzPKHFbbZ_O81xSlIFenKbcFuveNvCxK8lmD706dlgIcXJdzpFcAtmuejOaBWGwk4ghT5i4qeD_FQy0_DLh_ZKQeIyphlxwWPa3ZM4yUCuuQALohA0ihujHY4Dzx4cWoVlCnfptRrlWeO8zNLUSW1JhzPVTBtHM1MZ6qJBhmUHRdgOUkYpzdGpjCy9Llr4M-sjupK3xZljJsVhOY3rSSp3Xh6F92ZSeLOwbfrkDOHdNWPVwvCokb0Vm77U7lz2t11pIKiEa4OjcPYAb9jl8h7dH5cMTUhfYZGZ2x5JR20ADq98z79ss2CCi1BHT7xQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYc39lncWdcx1s8CJb4tQM7qyIe1GBzffuFT-9VEp78mcTny3T0tit5Sg0ev34zspSRcjE7qhBPs_SCQ82Vs21QGfeD1NAbh1c7vFg7Crx3qkSoc81IiQmYheY1oKeA1RQ2mjMxGcSVYxJlLe7jzEK5jnDSgyG-zdO007jA91FnjNivttQYLd2ryNGfSWaK2baykZrzbUUP_S_2GFNIvqSwOpfIhGa_i_dV0b2K2EC4697Mw0MD59Bn3PdDmClQxSEJuMNkSuq7BgAZbG52iBtuG0jBnEHSu4FcsP108eGtrTv5EWzrHU0AOih1fTXoZ9g8bfXrcfqPoAahYrCM7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gog4kQldlh88CJqEU9JPl1ypkrBL_SNMSv1rwd6I1SiiEyKitExXN6tIUGPecdujKBTCqylh7iN6ZUrZ89AN-ao3PBTgGuThMjTp7jYr8WK76yj09ffmAsIvrkfKO9LUeKwraotkutDF4lBijxuDV9dDfg5umyEFEOV_iFIl_1R4sBrRLlMFTttDwT6y6kWalVeZEzMf1ChaO9j-sp2KaqRwH6AKusEMqrrFih-MHnmammUGMA3OimGDlVRHM0jPY94eHxs5eUiGio7U3dorsowQopdJXCc2HuC-MwhYI4DaRpckUUcrKSFkvF8vKPmHvfbUz4lqLJwLwrLHFSpSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-yXlVcnEU38bM1SSPnijOpnCLWSUF8ASHmDQMH0MjtaZUJnqSfnOr1-U10SPeixIuIsiSiOeM_8uaipiSP6qc0a5bHog6W8IRGvro25Ju7sW7pik79M6hw3tqaFVFIJkT5shJNOZsWxnNsjlU8pJTi_Xtp4xAxubRel4CWin4gHqGqwC-IgpyUyG2RsLHI20OIDU5bxL-PYSWh_qFu_9gmWyYtaiHT1OiogvU8UnlyP0p5lt1eT-uk9iNCG6HwTNkoMYEMK-hXA_kZo4tvWbSw_Lb_20u7UbcIcgeOt1ghltM57J_ujuFbAXdk5NV5FZeu3e5I8UykARB3rEjmGDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB5SS8cLAtrvlk2b3h7K7a7klW2qI-NvAeNr94nmLiN8tQcRKMk3CTrx7mje8qZbzijHFN9Mxxr2cAMj50Aimkw4uEn9erpx5vYaYSQ09OuknHHHqP4UtkbQefcmferqHkFmxWMALSS2H7AhJqmVWinTrsttVtBsJr9AH2JZ8wb9KedzTrEIG-zd0DLiVz4UQ9MPBcG9LEYqSWjsBhXUrDXnaKrqJL3G8x8FaPfAcUZ5K2aYoaOjdLKg4bGdzL4lBe4PxDfDQMa9OZFuo2AYkuBPI4cbfO_w-iYUQH1vjOpNtjV6AvRkpApkbyxflrJzfA9Oe3-9g-srI30G1UOAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=ZLTANMZjLXDWzAfFM5_fzDLIyj2qMiWxXKKTudMjPSpzn8M5dHWWVJZofy2rn2FdcrZgV7FtmgTRJx3rWT2GT92UspuYChoEgYYqo6Eii5cFfmZaT4_2o6vCz6c1eeV9ZmDE7LsN8HfHP4SArYp08bhAI7ltNJ7h0t8Hfdw1ut79pdogsPBBa5is8481Vczs-egYFasmUdjxnoUF-Vjvj9NMLjWo_ZirkO3X4O-dTeFPQf9NKFF7geNHL_uJk9Tkp_aHrohMOdtVLA277psEmQ8GMlstDBUjWEtRjHG_PQPytQbYM2pAEhBetnJwzpAXoT7WWudhJwkqTM_5LXuijQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=ZLTANMZjLXDWzAfFM5_fzDLIyj2qMiWxXKKTudMjPSpzn8M5dHWWVJZofy2rn2FdcrZgV7FtmgTRJx3rWT2GT92UspuYChoEgYYqo6Eii5cFfmZaT4_2o6vCz6c1eeV9ZmDE7LsN8HfHP4SArYp08bhAI7ltNJ7h0t8Hfdw1ut79pdogsPBBa5is8481Vczs-egYFasmUdjxnoUF-Vjvj9NMLjWo_ZirkO3X4O-dTeFPQf9NKFF7geNHL_uJk9Tkp_aHrohMOdtVLA277psEmQ8GMlstDBUjWEtRjHG_PQPytQbYM2pAEhBetnJwzpAXoT7WWudhJwkqTM_5LXuijQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvSTIwDn-suDfwrnUo9CbZmXC29yKDSHtt2eFjg-D7o35Wj5kL1gUklgKnfmiJrrb1wG_huJ4Vfe8tbh3OEkarufWTkCJsDVI4a9TNNyzsOqKb8PQzV0emsFywDTCIgJfLYb3gkWkFvJc-7_o956WW3mmsjwrnrMkGeDwbwuQAeg7O_lCY47rPHgjcs5-gje_A-Le5k061fCu4RJkUKhkramjGqzjG0B7KjBTYH0xsuogB0e-YJdPUiu-jeQ8rNSyHjkwlebZaPWR5uI9PelgnHUcvKVeA12emXSyifOxunNsGNxICGaL09J3uIKGxlWTrmBC_tiP0DvUA9j1xss6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpB0Llm8qYu-CjO2Y9HXYHGdYW5Df77x81BswdrattGfWMlrM9FU0BahtkNhEBkw-pHvpAhRwzxgsFgDSx-0mxMaF4TYAp5_ifafxa3A6p-S5JXBwfkWMgTS7npu7icot-1iwox0yglr59rT6z7ZeWjhXeUUe7XouX6ad8Rue6Zm8XodPsEgEQRcrvLYfgdak9jIWixRCW2G9m1fgOQ3wYIy1yF10Gx3zSLAXcQqjarG-uBYSYXR3nSfiA5LE11k8mpMZ4RhkG9HlMirNiLKjUJiEKGL3HnyBw7adcGAnBUZfXwKI2X6M2WGzdxwHosCSJ5oeG-CG4gHcv5wx16h2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcwwNktW-OY1H99pAy1KONg5sAeprq9g0sEyjhOecBhQ6PvfyPCM18woIojWTfdDGTXEVvS3ClLay0iG26EoucV6qzvdWApd2MinbmKM5PtliZQ3r8QbCn4YiSVkTWJk2V5br-uukkEuXyZzeJZYmYf8Y61rvv_azXYEFfIZidj2aAXEFiTzXFvU_bByY4qGCBoQNL7qFj39b3KfLaskfZgaWMReBOQIxypjxvRdxenUd7xTpZGUl9vXc-QJLnCGckpsS8-wJrKpWDLflhwNgIBnVlIqBl4b9CyvhlQRR73CvR-BiEvKpwVVbOeucN0olruFIO_1cByw0XJVKsnN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdiY9W1dpVIGcTrD37A9WGwm7e5FCFXOH0FoMnD43I3DPoprU4mbvwQ9StQrgAmBFkveq15p4JqEBf9nN8vQSlwq43VL-qKIO7rqdTvbqs715of82Ja-PRGfVNAxNoFFLtK6ycjf4BwoaNPD_Nb5C3cJ4fQgt8oivwdkcDul_phyZdHkS9feJ36DK-uXYd-G1c70kghZSYYXAAUVNY6504X93jcHl_Tr460YQYnKA6Vf2wWG-6N4Ks7Pkx1eYi7dDPsjQS5vOBfcWsjWssn_tYVmHhx7yTqEtkH7-TA3hEEKN8W9ZVh9zmE2izGvVCIAgRZS6d_cFQ6cnECYtA0a5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGm_NQL2JPXDigTPZwGLqoHV6t0HxG0O5gGXgYSMwKUnqC_PQQyaora5Ax6h7snrmGo65FVYI-spdSColtuLz6QLq7jWZUGJuAjzY4gQi6IqXrUAM4oWYC43_jBS9UkjUEyjDs4BgVHXCSqQMh_N5548QikRMkqXWBFMkp4pLFbTvEaOgVhd48JLbAlkGYAanv9k5bZn-xExAyjlEopoC0i6ecxaGe7YH_77TZ6mmozaxbGSPBt2_xbwD53nAQz7ypFiMDsKvjqmAw_vrc_DCdeP3LuVXfTBtF5HrWvIbLMVzDOXEfKxStADZiWZanozHzI5EFpOSk-cG0gMI_029Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8oVmMp8CHF4tglvonrIV0Pi5dXVkbp3LZtDve9IpptYA7aFEP7_578Z5Tv4ONg5OpKDQrGAZwmJLrKFE0VxhZ0f2sQnY1qtTxgnwd8rnDgJRp3ekSMGZ1uFRcKSblGYBcmdVbBmgU-mbjsDMSuFMfSBsUh1XrmhFcznXYir4DpjONIcF2u1ermYE6R2oooZ-SiFpNtMLvr6vKiRLlDhaM__bXQX0ZTAbcPC8m6dxtmgbJFCwl8ZGgi0mKHLJUMUJH-rEmEiaLS_wI3hgCnenzX2k9SFYlCU46QzO0fa6nBt2Xo1d2qoVpYqqCO7elK2MwBp5H7FAVhb5ppfrdPQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TD1VC1aCB4RwcpyesMSiYZQB54B29dMG4Li-GCwrv_6zi2Qoeycepewuud8UhipJlq1ZTyE0K7Xxr0fa0dxgJ61Zo835Fmj2QsFr8ROeazQWt7Vxo6nOyZ7ScZSVCoY4F7jW4lmsZk-yud54CSma8CIZfReNobOAnzcvWZ-C4BUeQC6qf6vnP-UqTc0Xex1-9LnhE4C8qQfy8khAQ6JmmdVcFjy5w8Ej1cCUFqct9G5Xe_Lc6NHuSVUD5QGYxT6aJbkQ0cdqafrk9VSkQXMF3QxoBkUEEJzzjAE83jeB5tdeUY8vQD5AjfH4dAnjl33f_apfbb3KY-tVeiYOo1rVLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=sS00cjnkSo8Y9xm65s-C1TM1RrWKfdMcAc6DwfpiGZTv1cUKHr0UCjtB1KBTBuqaJ0izS4sNyHImOFfRNW0BC87x6NDPKW-sHspK78O5GfPEk46zqnqwlAEgH7vI1EKPFTbRkeHIFenY-6CQcnqXHSTInxvM3pA1EZn51nicfm992Pim6gR_0d8Y6l2WHgmddWelOmK1YyHQzTZHL4uBOtybLNUrAZEhSaEaS9mWxVxw44BJdV6wJnZelaV-9SNKjI375nvoExGFVn7L6LecZhxjto4-CipJXWD7ce3TwSShF1-3r7qsykugp_fyD0-kzKEr5e3drsmfvkIaVwZiQCpXUlhvHCtAzOI33eg6HPH4TY6oMWKJVNfo611hKhPDsppNKNLANxRxJw78XV1A8QpE95QGiFKoVsREzgpCDm7vd7h-2ohzt-DwtYjqogKENy9NJ-Ykx-hn-5hmUi2jHQn5tuty9YqQNLz481V7FBsGlSFXNUSIWPq37omRXcjyL7XtkQaqdWkocOOKb115nOC9ASVGTfKT4XsaeV2CIUBMY0fiaPqbHD6Koj-roASI-Oczb4f-S7R-_uOxMudrHZAMauRFQ2YHEAJ6YZtBinPZC2HtS46dG3EeQehA7WM5JkE6mS5uzP3kUFPhxPYyUcKrj5NK9WyMQEHBGbQe6aM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=sS00cjnkSo8Y9xm65s-C1TM1RrWKfdMcAc6DwfpiGZTv1cUKHr0UCjtB1KBTBuqaJ0izS4sNyHImOFfRNW0BC87x6NDPKW-sHspK78O5GfPEk46zqnqwlAEgH7vI1EKPFTbRkeHIFenY-6CQcnqXHSTInxvM3pA1EZn51nicfm992Pim6gR_0d8Y6l2WHgmddWelOmK1YyHQzTZHL4uBOtybLNUrAZEhSaEaS9mWxVxw44BJdV6wJnZelaV-9SNKjI375nvoExGFVn7L6LecZhxjto4-CipJXWD7ce3TwSShF1-3r7qsykugp_fyD0-kzKEr5e3drsmfvkIaVwZiQCpXUlhvHCtAzOI33eg6HPH4TY6oMWKJVNfo611hKhPDsppNKNLANxRxJw78XV1A8QpE95QGiFKoVsREzgpCDm7vd7h-2ohzt-DwtYjqogKENy9NJ-Ykx-hn-5hmUi2jHQn5tuty9YqQNLz481V7FBsGlSFXNUSIWPq37omRXcjyL7XtkQaqdWkocOOKb115nOC9ASVGTfKT4XsaeV2CIUBMY0fiaPqbHD6Koj-roASI-Oczb4f-S7R-_uOxMudrHZAMauRFQ2YHEAJ6YZtBinPZC2HtS46dG3EeQehA7WM5JkE6mS5uzP3kUFPhxPYyUcKrj5NK9WyMQEHBGbQe6aM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=HodWhs58zOaZTyjgjvpl6JJkRNcWLB_R4lMIgkFyojziERHKbuzsIuQ8evrsdyO7Or8GtvIbt9f8Np6VleULZOrrPM6rpt4fjqSJ8u2rXVU4TUmq4bOgPugDowpHKh2sLa5VZ_wR6lSH9hM0vsxGtQ4d4jUM4bkwjTLZC6Ndm45GgJ81_RyymZnthjWB_A-XNoCMnSjJrfUKuY170UgUNsbDr0y75GVD8FLfD2hwP0K_u5zhd4452zaD2_h_zdfN2YgPk3eOhBB2HibaBq4BeTnf6tc7d5q_Zh0shD9-FWtn5rQAJnkLS0AC-NBtQgruuUalafzn15jfLNsQN24mLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=HodWhs58zOaZTyjgjvpl6JJkRNcWLB_R4lMIgkFyojziERHKbuzsIuQ8evrsdyO7Or8GtvIbt9f8Np6VleULZOrrPM6rpt4fjqSJ8u2rXVU4TUmq4bOgPugDowpHKh2sLa5VZ_wR6lSH9hM0vsxGtQ4d4jUM4bkwjTLZC6Ndm45GgJ81_RyymZnthjWB_A-XNoCMnSjJrfUKuY170UgUNsbDr0y75GVD8FLfD2hwP0K_u5zhd4452zaD2_h_zdfN2YgPk3eOhBB2HibaBq4BeTnf6tc7d5q_Zh0shD9-FWtn5rQAJnkLS0AC-NBtQgruuUalafzn15jfLNsQN24mLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEXXvywd6Grvs6ulj2o7VrZxkJ41iHX72QFkchIFjXYmZ8MNsr6nEORenkFdfGI0lD-KuiRTZsoXWaMVfS7oj_8lDZp1AjcVmgkNsl68OIQTb2kcAXttGJgp6M6WYrLOUY4Hijox7GpRSZn5nBULEefJGVceU64mgR5sqvIw7yXP2xJv3aJbElTw4viMNPjW9wDGviYnhBihcQOqa6L_NbGdA6SOFg1rUcdtGIkUlqYgo4Gs7HlnFyuouzzhjSm5YPVVFCVN5B6q7wUW-G63pBcjch5sAh6BmuhgSm3kKxgudTvfSf3nXP_ovDt7t9TSKz-Mf3kQG6gLuANw6vcPJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJSxIlDdRMXz1VrmAARz1ULEb6f9iC1S8yAXFa1Z4mrkyDcKwNOeYodbmxbeZKgNscdEi54rIniktGqzIccYZIUssUZPlDxZgBfOUVixAsW3zV_CS78xIV65ULIwu10Ne_ImFQvqcuWaqeqjgFmJgs9Qgs1s6eNxu6YzDFVL7mGhe_H0PCnKDf2FIEtX87gVOeLeFgjptsHWYCLg_zolWcJi3D3A7Ls9D2QLRafPXGjISr8QOsDnr-vSbryU7ODokj-NCfyUZ_2ke4FPwyncAcWCccbEGSVKLS9Y1YB28OjlLj7SvZS21BD1QXmIQewv6Xo0g1hfXLCNepS1WL2gew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=WjUxasjlhJHpj1e7TCzTa-dT7SU_CqJmFO6ZfRxY7uSJo0TZZB6Uk-rwCAUn1f_45le8c6hy1JTfyVJiAn8zHXYGH__Ccf-WHaBX7vUlRlsEmEE0t4GnJKxUJdH_yxuNQnTd2o67L1w_rJjDshgu7kbytkLmlyBWIfMqBxlSUjrTMlzjhR-AAHuass9RihPrwcS6utUH3trMyms44J-gpNNA4AXPyCBHbgLZ8608CUcthqUjRAkemzz0chRkv5IrCx7d08_Yh5VyNXOjNLuDAKKTcPKqlTcRywHH5IaqELq3Yt_GTNa-wSjNM9c_gmejnwKwdG7jPQzwuN5J8IS4GYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=WjUxasjlhJHpj1e7TCzTa-dT7SU_CqJmFO6ZfRxY7uSJo0TZZB6Uk-rwCAUn1f_45le8c6hy1JTfyVJiAn8zHXYGH__Ccf-WHaBX7vUlRlsEmEE0t4GnJKxUJdH_yxuNQnTd2o67L1w_rJjDshgu7kbytkLmlyBWIfMqBxlSUjrTMlzjhR-AAHuass9RihPrwcS6utUH3trMyms44J-gpNNA4AXPyCBHbgLZ8608CUcthqUjRAkemzz0chRkv5IrCx7d08_Yh5VyNXOjNLuDAKKTcPKqlTcRywHH5IaqELq3Yt_GTNa-wSjNM9c_gmejnwKwdG7jPQzwuN5J8IS4GYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbkP98p9iy_0hVCcCLcBJhqppBBG9qSsNlOzbUMNE0NI9JC5v5cSEV4RJUw53lFn9j-5caTmj1-5kZSLNn8dLspfNu4wM-Kzdi9ZvRp92v3TCHCfTghWNYb9qE_1ogb0Rb5QW91TLJ8jfISEqx3P0sfTJp1XKhwKU7HDb3bjewcr91HMwgSbdiDWVYFvcLYS8XJhGTyvGqFjb4u41STH7W0gIYfCTOo2cpX6iGpmcW7xsclnMsknTIpNUrZKwH-iDK_xGf3WnjBD3UTEVPxgC8JDA5bJLtChFy7kRwxjDfu4-EBg0EmNydAzJErDr1lAkUHnEWn-Dh4FO6nXtwaW9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orDi6gGxofkVcAP982B8JSGx9Vej5hVYFElbS01tX5PV_VarCnfBwmkjpqvFk7lYaiBIirMq_omqOE19GFUpKBbS45PXFMX1DgEfjDxi3_nfHK2hvc074koIVBMT4_CrobLL-P5D-i4q_HNI8PQdJB7lZdhOh0vQ4u6nfMF8i1HEmK-I8vmAxJpJOGU7eLZUh9jAIpghUyzj9t7XbJYAsGmDgKTOpvJDqh_sB9o_5zu0YIBM7wJNxNvhzO3ZhjC-fzgoDd_7avmvJtd9CbKnseVMtk_b-2351ENC2FYD0BnaJUZc-vlClVDhIDNOTPl0i5VzRoq-SKaq7Dds_Hrn9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHX2J3NPIt0YImDrVrZsxrlTlsERWkIRGop8Ri71FtRJNkq0Z7YV08MFpXDcV2aKHehQMfdSmUj3aOJ8jZDS--_LO3LDsTdPWYdv3Uv_BVfRkhc5iQRJ06R0-VhaUT6AmU3GBW0vK_-sIfq9gtkbq6YQLwaj3vDl-2HCJjdtHUKjXH22Z6kGP3Yfxe_0WHCEUBP4YQgP6KRa9bkxq0tMSc4RxNx603Fp5dIw6IphwLroCX80yDBJPIVJdzq8fTsR5u0I4TczdRTUZtyVreTCU6AdE-o_xJenwDUZLbnfs14wmyY7-xrZNHInou_s-A9FrgmPTaQ4XnzRaghuTfqYBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-MewYvVT-3a2c_d3LgbhIWPUHKbCzPgcFkza_rgJRwJXq0V7rOvgUijLaahGVXWDIz-HU3YxpuUsbAUv_cR2kX0IvpaiSuauF-Gf__m63LH8AhLc3Mo5YeVTW6Clf72UJ9OXRA7DYooiiO1BEl-r0i6zi7Giushs_xIgtRubBnCTYOrAqXRy8Hgik_aXNBJmobY5P5RI5z1837E9XBL0J3cIyGRRbfMzaDmdmGhc8fD-JXN9Lowbf3_7dkmxOmfGlyOPTbuN7IChgNB6X6t2IbsAYoGVVfQZokwj4AzcHHp8CfbOtiaGDy3qh-mKRqo3KwZ6xv3UlPR4nZSwayj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k72cYwx_V_gwFlE3h0QlALOqhpO4JnZaAWFw51oNBp3MsWkONaQFvQJKxfaIbRcES3TPIqJ9l8Owhnq2eDMZgp-nmYyAR7QpoHXsoD41h6wqfBDJy7yfymvMGWt_mIGGzHHMTf0UlrrjGMts_KCotNd1HILsdrkWdHqo27d5HfWL94kuDiwo-3KXY0ZC54aeKuYREsUlhGe5xpDt0VcaC8svejsWtglNaIH4WCayLH6xRph6U4Ds-YjTcc9sejrkIuDuE1SANtNdhGUFhxsU9KKjusNxDzsRwJJnLmpyZkaNTtuHhsd64hT60OepKbVb2kQNQGN-eFk2Z8_n5KJJeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJXRF6RrDUHFrvsAomG9ADO3kZzCSCSRr0roN_XDv7_7GJ8u3VEUdJpq6I7ckq9CLBOx00fWWP8vRLBLNFC0bgbRUq1KTKx2ATRHMK_k9O01qI3d8TidGGV4SX8iApd8FKJUp6PQVPyAU72ebEq2esAva_GAjIkMBAP-c_uBbWkLm35SbKTem-HpcgX3-uHabSuo72fRbX8NIJm-PQyhqnXHdVaFRcx3LWzpy9kKWsE0jRbkvJmeMEwZYoRalgdfA0M62DULrbLBfwM8R5YM6JOcj2PfwHpgrHRzlJyYJg3dxNnjQiJlJChKQWLP_Bqz4hVEdd9vUSwcEx8I0GRt96LU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJXRF6RrDUHFrvsAomG9ADO3kZzCSCSRr0roN_XDv7_7GJ8u3VEUdJpq6I7ckq9CLBOx00fWWP8vRLBLNFC0bgbRUq1KTKx2ATRHMK_k9O01qI3d8TidGGV4SX8iApd8FKJUp6PQVPyAU72ebEq2esAva_GAjIkMBAP-c_uBbWkLm35SbKTem-HpcgX3-uHabSuo72fRbX8NIJm-PQyhqnXHdVaFRcx3LWzpy9kKWsE0jRbkvJmeMEwZYoRalgdfA0M62DULrbLBfwM8R5YM6JOcj2PfwHpgrHRzlJyYJg3dxNnjQiJlJChKQWLP_Bqz4hVEdd9vUSwcEx8I0GRt96LU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6437">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnL7dbCUGmMRIXg9xdj-RMs83Jd7i7soVKE0s86R36p_cGFZgQViWhJ-04XmmNd4sAqGBlamjXf4dHMLLwb_2OAFJy-RPFYvthuk0yVbt_qFhHrmf53ElIKDe4XfF4hs4Xlh_IRryV6_3iqiS_5xLID9sScMV1i604QC18khB2553O83zl8w6MBXJi5zdQwuCtK9IOAyMdR9NvzMlqL0lHbY0-w74AdEURv7CfWSBX2KEw8KPlMc09WrXJSXQLGl7wFjmzVuqiuk46imE3Fv7qRQM4byPd9_fju-phyIa2PhWnGc_3NY7rYX6eIyxeZmNXBSYWtoSnEVj1Wtkv4LKSY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/127d794f5e.mp4?token=cfEFSZqkFD-tpSe0yArs7edwi8rs30Vuor-FA9ObipI1_BUfei9lmZhW1BOrMihp_9gu1jQ_eDs0GtBwEuwAeTwP23yJOvf9v1aYzytGyNM_FCoGyAcLNprFjQL1mUg6Jghd9ihsrM-yzNhURQpVHxy6-fnmjj4-uTkoQbPE8r8ECFxuO8iJrwA2DKQ8WXxlVzzDghD3akgkk9_qtZvcUB27SJShSYhmNo8bLMrrb7teoX2CMcK87SHzywENDkjqgWy19qk9DInALTYRp5_Te4T4HVTAsk2rsKt9KgxH5YmdqrLGNMrKyOTqi4_Szke2z2gzwdHkZTKK_N7JBOPCnL7dbCUGmMRIXg9xdj-RMs83Jd7i7soVKE0s86R36p_cGFZgQViWhJ-04XmmNd4sAqGBlamjXf4dHMLLwb_2OAFJy-RPFYvthuk0yVbt_qFhHrmf53ElIKDe4XfF4hs4Xlh_IRryV6_3iqiS_5xLID9sScMV1i604QC18khB2553O83zl8w6MBXJi5zdQwuCtK9IOAyMdR9NvzMlqL0lHbY0-w74AdEURv7CfWSBX2KEw8KPlMc09WrXJSXQLGl7wFjmzVuqiuk46imE3Fv7qRQM4byPd9_fju-phyIa2PhWnGc_3NY7rYX6eIyxeZmNXBSYWtoSnEVj1Wtkv4LKSY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا
خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6437" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6436">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=H0xrVzqqAkxPje8SU8oS6hqu0FZooW8KrRkqQOoXKxGtZZN6NpXDYrpFVc6tLTbSQyn8--QkW5TdXsiYADhkWXgLe1XWAqpbPMZdQcKGho3ZqpZnBuKeaBTLaf3AVUcUtMmDC5OOU3xEtEVuG2wR8QvQU19WoBWXUpKkWI_HOZLj389kJnjxGMZ2gdEQN-xJstfNUKZYW_W-xoYSxeBPp6BuH2ixH4_BTctHZVubDSyOi9sXeuP-W-XUTCUxcwWXMBF1C7F52VqIIY17NpAOFDqapE1Pbu4gpTArivP659frq2QCjdMcDOPVVCPM77C9QUQxFd6yHxnYVTkYACLI7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a175d481ad.mp4?token=H0xrVzqqAkxPje8SU8oS6hqu0FZooW8KrRkqQOoXKxGtZZN6NpXDYrpFVc6tLTbSQyn8--QkW5TdXsiYADhkWXgLe1XWAqpbPMZdQcKGho3ZqpZnBuKeaBTLaf3AVUcUtMmDC5OOU3xEtEVuG2wR8QvQU19WoBWXUpKkWI_HOZLj389kJnjxGMZ2gdEQN-xJstfNUKZYW_W-xoYSxeBPp6BuH2ixH4_BTctHZVubDSyOi9sXeuP-W-XUTCUxcwWXMBF1C7F52VqIIY17NpAOFDqapE1Pbu4gpTArivP659frq2QCjdMcDOPVVCPM77C9QUQxFd6yHxnYVTkYACLI7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساکنان سئوتا تجمع اعتراضی برگزار کرده‌اند و دولت چپگرای پدرو سانچز را «فاسد» و «خائن» توصیف کردند.  سانچز شخصا فردا به سئوتا می‌رود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6436" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6435">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UC7RGOUsSrk1hfw7cVfCDrI0aaTousDvuUvYj7aNj-Nf9gjgoH_ioPbKg6EJ_W1e-4RSe6Omc6Y9J4PyGwQZ0pqxmvphSbufItsupM17DGCib51TfDTZ84xm-OC3q-MsG8wul18qwK2a9tgiAxXAA49OF5q8c4BOD3bLfUBXN6mPjEfBMhV81GWndtBjaNbSS3KUMVXtVxiXq7UUYio7HGgjSw-Is0Zd9z7xh5WuFueOnTWeeZq3QPZcqdNVgPmgidNJ-y_PF-lJWErTbBmSesuXFaekvcU_dsJZYU_Cqza_f4fp0YO2-LcMoDgo-4xkbWSFDJFWqq_1hxm3Elk2UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی امضا کرد و خلع سلاح رو پذیرفت!
نتیجه عملیات ۷ اکتبر که خامنه‌ای میگفت :
« تاریخ ساز» و «ضربه فنی جبران ناپذیر» ، شد نابودی غزه و کشته شدن ده‌ها هزار نفر و از دست دادن ۷۰٪ خاک غزه و حالا هم امضا کردن خلع سلاح شدیم!
کی به این گروه تروریستی پول و سلاح میداد و برای این برنامه ها تشویقشون می‌کرد؟</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6435" target="_blank">📅 08:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6434">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPnFNSkCuaAHnhB0SNhf1MPYdGhNu0tTXe6VSZYdleu4NhZ2DldGRH81T0GI_mUV2U9PR2XN2m9RHO9OkmFBCihL6l7ESfmraGGZnOWO5SSn-KR_KTiL3swqjdGKd0BaeEKtRMZKzGo4db0Zg9xHT4b9uT9Ab8ZOvG-v0rXn9wSFWy8kF_CK4UUp7DYCpG6cybHHCFBnpBdorrrzUz_FLt7Vsn1ikmRI8JCCZT-OCqUYqzWOyYD6x0Hihl9MZ1uHQpxu_Vglp7CygMH-lubv-miXfb8pD3Y6uXMaMUqgNM8Coi7cKjUBHd0W3ELVmBoWpAlU6Vl7vXMXYlJuDSZEwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوون‌های مراکشی رو اینطوری میارن کنار  مرز اسپانیا
🔺
در یک موضع شدید انتقادی نسبت به رویکرد دولت چپگرای پدرو سانچز، دولت ایتالیا خواستار تعلیق امتیاز شینگن برای اسپانیا شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6434" target="_blank">📅 01:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6433">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=WCkj-ae8t7deVq5uWQ5Id8yQQNMZ4XEMVIMsRCthSLkUhYYAVXDM075Q7Frww6D1QSG-VAVmBkcZ5h3I5qAT10TRW5C8LyZbd1M9EqmOd5S7emdSJXh0Q9qWNDtnk4PZYyS-40o2FEN6iSsX7ZQ20wV5-GZ48dkRosyQPrYLc4bSO8m5GPHziaI9hRWXnLfrZe5h7FfqOK7cbRn8gOEA4oCOKgyDC8WWN5l7mXWFChdP4Q9GV72X5YlzR6z7gajtkICVyA-ZSFAIg_VMb9COFuGmWrjtFUcp9n9NbxePjvhkYEiM31xYEJGk4NBA36K9tVUENTeu3NWJs2ZY0_RnhWCQ0H_lCAIZmx80E-8LXpIwFj6mRnT1PGA4OCWD5-86Sy15srPiLP4eeG3waWaRxpvChZzu7im4yz-Ltio-1OP9bblbPLKDuoYXZ7hcEx7e0VzBGVqY4zgFDJAZW-whkkf9H1UnRowZw6StUUIFyEYzaZIR6uPyf14oysEr6haT6QKGVnv24x53qp_1xilSe0uI1hLgyqdeDxumNVQVNigZ7h2gMFMMSR6i6XQv4wqSudOlP-Z1Vbc7qsPbObVhFY_46vNtY-MBGWIDKS8hbz0k19VqlXY_L26Y9Z_vz9E4AGcAW6mhYvvs1X3ORsGCzxJe52Um72vJ47CYINgvQtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cceceaa5a9.mp4?token=WCkj-ae8t7deVq5uWQ5Id8yQQNMZ4XEMVIMsRCthSLkUhYYAVXDM075Q7Frww6D1QSG-VAVmBkcZ5h3I5qAT10TRW5C8LyZbd1M9EqmOd5S7emdSJXh0Q9qWNDtnk4PZYyS-40o2FEN6iSsX7ZQ20wV5-GZ48dkRosyQPrYLc4bSO8m5GPHziaI9hRWXnLfrZe5h7FfqOK7cbRn8gOEA4oCOKgyDC8WWN5l7mXWFChdP4Q9GV72X5YlzR6z7gajtkICVyA-ZSFAIg_VMb9COFuGmWrjtFUcp9n9NbxePjvhkYEiM31xYEJGk4NBA36K9tVUENTeu3NWJs2ZY0_RnhWCQ0H_lCAIZmx80E-8LXpIwFj6mRnT1PGA4OCWD5-86Sy15srPiLP4eeG3waWaRxpvChZzu7im4yz-Ltio-1OP9bblbPLKDuoYXZ7hcEx7e0VzBGVqY4zgFDJAZW-whkkf9H1UnRowZw6StUUIFyEYzaZIR6uPyf14oysEr6haT6QKGVnv24x53qp_1xilSe0uI1hLgyqdeDxumNVQVNigZ7h2gMFMMSR6i6XQv4wqSudOlP-Z1Vbc7qsPbObVhFY_46vNtY-MBGWIDKS8hbz0k19VqlXY_L26Y9Z_vz9E4AGcAW6mhYvvs1X3ORsGCzxJe52Um72vJ47CYINgvQtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تداوم ورود هزاران نفر به خاک اسپانیا  اغلب این افراد مردان جوان و نوجوان هستند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6433" target="_blank">📅 01:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6432">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=aYhcBfCbWsKJFfMfDrGSPgoKS7IlwoqtnxTAiqA96336AjreypKVidmOh_9wZVMN20X6NqbRRVUeXJpnI8rpibf43DV-igrymczH-vChrHH9f5LDF2BZxLvSBDVefyOyplS_bbLfxyyrajN2saa7sGNWUIjYjK_DswMdp1-bkipx8X0W17nRahoceOTh54LILefT4jJyE6s1afRaMhNMtGXa1DOaxhUENSLLQ_50htgLvkFnFgN_AFxkO-DdKkbokkH51lEzDEh1Tq3XvIQKnPf50hLnCPuZ3JKxeFtBHPsmesKBGj3WYkalwjUQO7RaC2RP3_T5k2pUTNk-WQsqfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c72fd0437.mp4?token=aYhcBfCbWsKJFfMfDrGSPgoKS7IlwoqtnxTAiqA96336AjreypKVidmOh_9wZVMN20X6NqbRRVUeXJpnI8rpibf43DV-igrymczH-vChrHH9f5LDF2BZxLvSBDVefyOyplS_bbLfxyyrajN2saa7sGNWUIjYjK_DswMdp1-bkipx8X0W17nRahoceOTh54LILefT4jJyE6s1afRaMhNMtGXa1DOaxhUENSLLQ_50htgLvkFnFgN_AFxkO-DdKkbokkH51lEzDEh1Tq3XvIQKnPf50hLnCPuZ3JKxeFtBHPsmesKBGj3WYkalwjUQO7RaC2RP3_T5k2pUTNk-WQsqfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حدود دو هفته پیش دادگاه عالی اسپانیا حکمی داد که افرادی که از طریق دریا وارد خاک اسپانیا میشن، نباید فورا دستگیر بشن و عودت داده بشن. اما اگه از موانع مرزی عبور کنن، پلیس باید اونها رو دستگیر کنه. این چند روز عده‌‌‌ای جوان از مراکش و از طریق دریا وارد اسپانیا…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6432" target="_blank">📅 01:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6431">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا چسبیده به خاک مراکشه.  خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند در Ceuta</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6431" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6430">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js345ElFf-7qJa-sk97LIsDCnHLoVfG5508Gq2wS-gC3v_B3Puw0MzmLGjAe_lL7PTmKRTFxZlRWGSeIMv5cBy_dzdDYxQr8mOdfF4i_nDiu-COqHCT31620qGuwT9wa2fbDCDfncNYof_2AiKNsKgpy67CD5FtIdrPKyhBG9BlY4OLaNzASEP2UgVI5A4bWTBSDKSv09f6vToJ7zU28n_UGe1VSHRgQAYISxY-KLbi0od9dwXCmOu9tLGC5UKjFNDbxfuvSMRKKhkylde5cTzoASHJx8Slw6jC4uXkU3pldD8OryozDK25RRXlKKYMxlxhj5HC2jVAv0LkKBhZt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکنون ۱۳ کشور اسلامی
به درخواست عربستان لبیک گفتن!
برای حمله به گروه تروریستی حوثی‌ها در یمن،
از جمله : پاکستان!!
مصر و ترکیه !</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6430" target="_blank">📅 21:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6428">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsbeacPhrupEp28ubrcEHkXuwALM5U0osBxAw1ROB835eN5HqEpF5NeU8dpiducZsWGp_4NLUAeuHfCXF1aIPBTV4CMQD8gUgXeGWGQzTkH_JiKvLgCTHvSBHFygki8n-hYeiOepttIeqicXvSGm_ldHZ0SM9OLLOo_fcKD6RWVMKsNalbr5akTY6K4ToygfOkohVnBV0J07SuHhaediq2nWRkvfbUDoy57sfrG2W3Vf3LtawBqefHh0vM34xwCaV8D1PbFC1nSIeMv-P9FTOMCTZn8kBpka2GRAMlpK1fUMpGTLcbkiaUGnIpFz93d7hgCqMAdXAH8t0-mYjlTAeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjIFsjJVgKnnoejj0XDN902DAwCIE_0a5iOE_pEFqT9bozKQBZfpViMy_NxzD3k27uD7PSMNNmNti_RFvjbgJ3AOOoUAIwPyp9tmi4-PMb5MrB-RIgIHJMXAMXrGo-5JAAkw0X5FJSrTN6iOODzROEHBunQD_u-59eeEplN1ID5ov2gQOFNhFXOTR0dB7_LRUnMNDF2YzJ3McwbVltrq18c2gGhTeRWMs6r3wtG9l7oheQ1gX06xVVpYw8AYXgSQ2hEGgHjtRu0pMXpgYpEcWmyRJXYtuoEeIHyo-jsDGh0IIOluo7Qp4MMf1fTexGTHA65qRt7rdxYMu0VviB1cHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو نقطه بسیار کوچک از خاک اسپانیا
چسبیده به خاک مراکشه.
خیلی کوچیکه اندازه یک پنجم جزیره کیش ایران. اینها در واقع از خاک مراکش فرار کردن و وارد این نقطه کوچیک از خاک اسپانیا شدند
در Ceuta</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6428" target="_blank">📅 18:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6427">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39130dc900.mp4?token=jP6dTbhfZTcbYBcbsoZ1yGy0ZTZPQ47aUJeMo02Rr_LpIokqOaxqH9ESJFklbWUBC0PJzsEBWkVCh2x6yCT-V26Uynkx8VyA0pnFFErH5pf6KkPR7i4zXYWAWDLr6HUAC9KgU_C-2MlpuQw0opqsUBcy79qKMh9eB3y8YfRGo-A0wAHow-ZaC6naQ8fSZbx8zq_gm8WdkNQQotB4IfPY1j3zYjc3aqycDIyos_mNMnuP2HV-cCLxSewpJeskXjALxC0nrUc4KMraEmevXwnCcQ9VIJn7Astv65kMyJB6XurgcPuFAcywAybdOnoqyEEMIVFjN-0sux7w6c1cPUm5RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39130dc900.mp4?token=jP6dTbhfZTcbYBcbsoZ1yGy0ZTZPQ47aUJeMo02Rr_LpIokqOaxqH9ESJFklbWUBC0PJzsEBWkVCh2x6yCT-V26Uynkx8VyA0pnFFErH5pf6KkPR7i4zXYWAWDLr6HUAC9KgU_C-2MlpuQw0opqsUBcy79qKMh9eB3y8YfRGo-A0wAHow-ZaC6naQ8fSZbx8zq_gm8WdkNQQotB4IfPY1j3zYjc3aqycDIyos_mNMnuP2HV-cCLxSewpJeskXjALxC0nrUc4KMraEmevXwnCcQ9VIJn7Astv65kMyJB6XurgcPuFAcywAybdOnoqyEEMIVFjN-0sux7w6c1cPUm5RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرار صدها نفر از مراکش و ورود به اسپانیا</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6427" target="_blank">📅 18:02 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
