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
<img src="https://cdn4.telesco.pe/file/TeaFlDBr9iMZtJwlfXAkB4mdSqBqlQDeegNHRORyBzKk0pmqORFoJqDcZwiIBNTm9Y8Y-PH_XeirzN091hjq5v-kIkJpmobzxgE2pHU7Quj8uWoGhouaKT01_F_ObRxhb8VTFgrzAfMDmM29ZChAs9RxyB96KMl7W-CbM_rIiUeUC6Om8EdJHOrvexPR9mBWxGrdVf-d7_V3JVNEuBhJC_G_ZnjEdz8JDjwSemC_i8d1zvEQtDLFdFttt8xvOiXdAHHYLSpo4k_poKbLMO0Nv-4eyyAc8a5-jilqUfgg4jfSwRDUZV3_5NFO-CbP2ANQsXdUZfF1xQyXWDLQhg1sQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 14:44:54</div>
<hr>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppdWci7ZnA-2IRuJiqgorxBppJ_u99YOeCWe5tic5pKks_PnaUuyrFvFu-Mfb4hhen-HF90IgXM0WevkchVe06wml_VbzvFM3Hj1vJXuwOsNpn9nLeWDMQhxtTVK7JuUDocUBCrZrC2t9SYDC8pz5FgnmLZFNqvUHSiOLVysmQrxctESXa3P1bk6Fwf0U0_zMVgJD4TGjwonnzGR1kL68ljQqAgZfpGYy_AWM3CPk1c1L50SHHBAvhXE59DeJNDJYiCB_z1oIupj3YCQFjATfnDaS83iV8p_aEGrPDSijCHkS_LXAggypfJApJeKzkWEaJx-veBbRZdaLBSqXjLFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQ3tLsZ77SCW2DlduN2szxNjUpC6DooT9CqCBimFk_exBgoneSYoKSibhtKANG3ibWjBleckrkGSOB2EskThq4yajApKW3Ty5YSrBmy3yDU-6gTgAhZe2WWwDShW7UUBOkdjUR0jDRRPQGqhLmPpN-xnzi7RjAuTwLjn_Lw8cgLbZXwZhRqP651nfkppkWD-t-wQtDfTgfeBNb1T3KTo193VZPc4dRUpIitNJEhBcsb-ak_v7hO9WAFeyStPNziRndjK2shbm9JO_PMZ2icymz2pDBGByedDYvwvJPXRhk3lSRtRUoX0XO5hojfriCrMn2JMk2tk-ZIfstbPpGXAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK3pISSKeb709ekPyaCs3xRd57_sR6AE09qWFpfB3zOkPXDPEJ10deQhA5jwPGGW-i8X-X3Gcxj49_L5DDebDggmg3WKDBNGOMMXDcbekL5tl5YhBAYwjg4sibAYByE-85p3loeKpCJ2S5YNrOFYsUMAtibwd57HBMEx-SZ6nK9l0b3R-M9-yrW_Qa8Kv-8J8IVU5VLOH_V1ikwNpbuiTXqKTN7X4St1VEwwPXdwKGzFUDF40M6Wm8--GYJD2DlIK2Djt5vyG6CODZF1mbEkahAW_BpKwR7Ozra6A1Ynx7sMaD3cpcJVy-iXA66EYjQDSWpdTdfhLaUQgVUnqtM4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F873Dd8hbgzzwogMZROePk5VNqAyQxOmaXa0wPpGX8MCNctDRvtCCqBxNQ0QBaIxWb-ls0H0v2cgJaqZTD_BKa2SSu7Eg4j5RBFEy46EYkr6vRZzas51QpzgoLNbouaQD30VHmXUOBv6-sLenEkcBa1qXWnu_N1WLw5W2E3S2ZZiA-yuuBFGW8Bao8rWnVdRAOT5C4FBLhX3dHzelPGdAFZqvZtxc7tZFuD3FblTyKgPn1Hz0x87-qvQ89CGPQNOwUIGBAOc1Ift9ZUipLLERwqAH89ZWHIWPJIXFpUJ0ixWmL8zsOr70wRTf-TwzHo9TCJMw3xhgw80ZcD8CJgrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iuygkne37eKpEPiEu0fgBw2tXEq5arRjgGWK2OUpiQNoD_NJQtgzZivRDqZbabzUTPLmMPKYiG1LA8AjmnO3RaHIi4EPA3uOmNnWD-5v8ZeJLKWdeiQv2WusTt6o_YIa9Y9l2cgLTgzQLZbapBldc2sum8VyB_j_O4dLcMHhQHxK4gBrdBOf08jveLhWQN6nTsW1zPRABDV9A_8wG7n76CUhSiP8NbAvXgQRpD-hHOwK4Jwy_fks8glTTawaPdI6TTW3lWnrvjSaYvgItHsubjTbBGlla7-vPqvt6_3RC0vAHgHNWs4fy8pPwj26hFP2mGLNjc2RL39yOkthCnAoFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYbIMjOmfnL4bpCbd7hgKO9RAhwcp2hHn7-rCA7iWcSVsCbutMeQe5DcjIEeV7PQv93hmkEZRJZRRJI0O7ah2G3jeLV-9AJ7RPR0E7uKaeeIrZqMNxnYSjnOkqqfJKd-XXAYpsmU7wmTnegB0iZPH5ttsiKbvX_3hrD3Zp2vAZ88NRBnmzD5D8A5ItOJJn2FeJOfdvmi_zrFETooP5k0bwDpGvWSAoSPIczCEtErMMkV-tBBXJTXqNFM2a6CHfArhp6TcyNy1JjLIMkaULUO8N_a7liWqZNtnGfy2O1sYqguuRijDLNJf0dooFGx0CJs3Rv9rmSNMBc6JwW2TgJfzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky7xm14Vok8rZRnCbKCq5kQEQqMPRedNfi0Pucj9AoyB4Gs0LBiLCawMbesjXW70n9bxdPWdkIYOzW8LIWs8D0Hkp2h40TxvaN4_UqQyIVfsoEvpPs7GdyGir8duomqWx1eDmnXvxq7eKmJ0A7iA6Wq4qjN25_PUg0biy67p5JUmrWaQWBMJpxtL2Nl5oHuE_Bt-txIAD02HKvJ8L2d_KFFlYl9lU2frMrfIdCvgpw7ntkOMwIacwe7EDD6nhhzZmavoF5Lq5NdsRlGQdTpq7cYG0jqfjhnjKCX8xsJobLZrDjiKYdKykg15bTUEQW1BdP8_5IBPXu11Q4lN5JJdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=MFBUoR4EcOcPlobWDIX4UL4v9n33EyR-5vnZxsD2aaRwCkEYAs937Y1jD4gX45YPA_Rt3dnwbnmXJB8le_Z5c73R84jBf3EqR62bE2jjtid2jt_BQSMpqrCCdvJA4rn2UOzQjGUQeKOv4qDmq9OWrRvJNBvqx2jNzVUfdci60LtckEkLU7JrBIR8bvXbFbVcuoiqCwjFHzenbKRiOyk6X01clkO0qE3EEr1l7noPcO0NL-GzWi0Pd8EUJeIJF3wCw5AKpFt46dl_JHo_94UC_K1VAGDJrqc4sIju2thFpo5W46o1iMLwz3Cj1en1yE2f8WXug887PTMVlG4hO-Kn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=MFBUoR4EcOcPlobWDIX4UL4v9n33EyR-5vnZxsD2aaRwCkEYAs937Y1jD4gX45YPA_Rt3dnwbnmXJB8le_Z5c73R84jBf3EqR62bE2jjtid2jt_BQSMpqrCCdvJA4rn2UOzQjGUQeKOv4qDmq9OWrRvJNBvqx2jNzVUfdci60LtckEkLU7JrBIR8bvXbFbVcuoiqCwjFHzenbKRiOyk6X01clkO0qE3EEr1l7noPcO0NL-GzWi0Pd8EUJeIJF3wCw5AKpFt46dl_JHo_94UC_K1VAGDJrqc4sIju2thFpo5W46o1iMLwz3Cj1en1yE2f8WXug887PTMVlG4hO-Kn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFQXfdYkxgTrGfyxJQ2d0u61ch6huSV43FVezH0B7bG6cJDExPthH6XTyo6czVONqbhMfdRz5DaMwXt_XTivrsj9gnv9gCgA3D0pv51baUM5JvAWHYoRxhDLmPceo2LJFEYC6ioIjyprFpCz1Etlz3kntaeJzIrwhyykHbt3ql7Iu7ub76NBW_F0gXfVIAoG7pSNVvyCP38Vn3IS_36xvig0dy_ofeILQg3ngIEdDxoBH0_woNWbKz5TRCElJIbThBPMRvM4_HbZAf2l1OJGyPcCUg_fUWlUiU30-MsQPymBoNE7Ve5_EychBWFidUIRGaxYLfBz4w3fsN8XJ5ehzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ID7qmwQtpeStPX02JQQemH7oQbNDrPxkvlBPo4gBg1rCJ_nT0j2rd_fdMGQuID8-B7CUgVQmZW2CpAtdYJeMMCqCm8IZ-GY9kjMZOSMRV428dDIlhXlizwoZT7BRzur_obP0MC9kcwBwlMr7v3zhvhb4n_Qj1KJ3eb4ToByANVUyjfYeJlAMyIjNS4r7mEMoypbT6vbq50aq3CLSw_yIPWJvEekwjiZdhckjbrdNhxuDSxL0ySHmjukvui9ivhofPvyTLu3ALVApKRTzpMBP4QWpFJkpriemjybWRW78aDhwkBXzTOJGDIzebx3rNc0_3-RTkkpPquHwimYkJffkPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ID7qmwQtpeStPX02JQQemH7oQbNDrPxkvlBPo4gBg1rCJ_nT0j2rd_fdMGQuID8-B7CUgVQmZW2CpAtdYJeMMCqCm8IZ-GY9kjMZOSMRV428dDIlhXlizwoZT7BRzur_obP0MC9kcwBwlMr7v3zhvhb4n_Qj1KJ3eb4ToByANVUyjfYeJlAMyIjNS4r7mEMoypbT6vbq50aq3CLSw_yIPWJvEekwjiZdhckjbrdNhxuDSxL0ySHmjukvui9ivhofPvyTLu3ALVApKRTzpMBP4QWpFJkpriemjybWRW78aDhwkBXzTOJGDIzebx3rNc0_3-RTkkpPquHwimYkJffkPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=XZQZZN4czX2ug5U8RifUqG4Oe-z4tmKE8PunMuwq-s6w1aDkCKmkWux6eXIUwr1ZHoeTl50Ag_vzNGtOPYJ1GHsaW6i3HdVmmmUj9PcWKgt-I9dWweXEUcAvJ7W70dlyRzmtXHWV8KwYiYtEev6SoKQJGjActNZFPicKbBAjAyj4HTIo6mmE653Yh1D505lmw421dbaxtBhrv9IEW8_wDQZpp4JJR0BGJheq-L9fUXKKODAM_AHHaJMRfM3UJJf21NiCEXKtdtAySamRMhCp-4XuHKc7p0b0VLvge3TAiFTecFMRxTsVUDb0_bN0EsloMm4FnXJnmeqzYsmq1Rq4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=XZQZZN4czX2ug5U8RifUqG4Oe-z4tmKE8PunMuwq-s6w1aDkCKmkWux6eXIUwr1ZHoeTl50Ag_vzNGtOPYJ1GHsaW6i3HdVmmmUj9PcWKgt-I9dWweXEUcAvJ7W70dlyRzmtXHWV8KwYiYtEev6SoKQJGjActNZFPicKbBAjAyj4HTIo6mmE653Yh1D505lmw421dbaxtBhrv9IEW8_wDQZpp4JJR0BGJheq-L9fUXKKODAM_AHHaJMRfM3UJJf21NiCEXKtdtAySamRMhCp-4XuHKc7p0b0VLvge3TAiFTecFMRxTsVUDb0_bN0EsloMm4FnXJnmeqzYsmq1Rq4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvJ-if4jPeOAWCfCGOS5T-vghyh2b9DmjI434UCdTfYW3pp3Uv4zsoMmkGJpWqq2E4vFQbanccF-8g9qT-20v4R1sJnd4-_tu2Aj3SQcafLhUMP8rnmKUz9Jb0v_iOcO0_qo-SZLiNjVRZZhjp63acx_ARNAYgEvp6GB59ueH4WJJr07QM_1yDObMWVBmQbn5ssgCSEDHq6DIIT4XeFn_OVPFVCPTgaLBb7Fnq93DOmAoP4iWrYCQqHDErwRTSOaJnbCkMMNsfwWtdtwWWX23Q5GF9CXOalcQg8p6nIjlCaiLpYZLUvFwU6GiKovmURF7XdH0iPVlubwW7v0_fgzqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQSlmtPWCo-ybncY6iRUlp8pkv8E9rF2oOuXgFQ04iz8UDj-D4c8Nf2Ui9gbIS0RFVDeO1KJjfJrBIv63rkiVYXaq3diYadkQDoBlIVrTuZhGj8-I5msJnAg-4URhV62mpbEY65PzjUO7Os05pkAoozAOFPwYfSZMkoyhfKq-N27Vd-nzifHXr9MYeGU5nWiNEwPapKRqiGj8a4F_oYJo6Tr-PCRFYqJwZMc55nd1ZaT75PUaFrouf-AmPg_OAJLo6_tL9c62AFHfws3b3O4AQlj0PaAU69adDKj-a5AaC3Yb2ns_r8V7HRxVL8PIbdRuqpjfIEC27To25xnLUr5Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=D_yNx_L8pvUml87CDeHbTm5vxd13k7Bo1vlMIgr19VuKOTqLiiMq4HnjYPx28IYX2CXwDto5XFyPOHLsTly2cuRZviz6gYwQlimIDZHQZxSUQYuuog1aB3Lu3gET1b7I9kY5iTURSqZr--XeiseEYQxvNc882xDgHB4RMbuCkI7VISqT1H5Iqd-7vcW_8i9_Paq48FDhcBTLrLqbNfILvBN4zgohUXp8kJDLmF0_kDJ2kfgmSz1_3-7-OGKBykrmcmrSpUO_Xx96nvKi-TTJ7-Yi0WVcCfmAl4rBmB_k9ejdL-sCEBVsA0TVUEhAIFXdkX_kVqoKn7K9ZBGikUCPDBUUD6jhFrKciiFhpToOtGv2VhWRJKd0LWhFAzLu1KVsbZ6Nv0EZ-eFcHrEi7K4IyuB8V1kLjQbJOt8N2XiDJh5TjgnfBclBflgzR8D70cfG8N2g7RyHGoHuvWDfWNuXE-j6tlJjmF0ZE69R6jY8rnCdlK3NzHj21J8LG7G4-YyWJS86XBdL65G2fDiSlpdbvLWBRjlyVHUA98QYcP6X6heJCGidKnMqvzmAOhEcgCHZ6eIMS0kHbgK85bwjsswP2nP3NiL62WZIkDMhtVh1F3wtJQjyRFcC_DbX9JEagMgyIpOwCQajvslXdrgblKahAcCYL8BjZKZerfDJqH82oug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=D_yNx_L8pvUml87CDeHbTm5vxd13k7Bo1vlMIgr19VuKOTqLiiMq4HnjYPx28IYX2CXwDto5XFyPOHLsTly2cuRZviz6gYwQlimIDZHQZxSUQYuuog1aB3Lu3gET1b7I9kY5iTURSqZr--XeiseEYQxvNc882xDgHB4RMbuCkI7VISqT1H5Iqd-7vcW_8i9_Paq48FDhcBTLrLqbNfILvBN4zgohUXp8kJDLmF0_kDJ2kfgmSz1_3-7-OGKBykrmcmrSpUO_Xx96nvKi-TTJ7-Yi0WVcCfmAl4rBmB_k9ejdL-sCEBVsA0TVUEhAIFXdkX_kVqoKn7K9ZBGikUCPDBUUD6jhFrKciiFhpToOtGv2VhWRJKd0LWhFAzLu1KVsbZ6Nv0EZ-eFcHrEi7K4IyuB8V1kLjQbJOt8N2XiDJh5TjgnfBclBflgzR8D70cfG8N2g7RyHGoHuvWDfWNuXE-j6tlJjmF0ZE69R6jY8rnCdlK3NzHj21J8LG7G4-YyWJS86XBdL65G2fDiSlpdbvLWBRjlyVHUA98QYcP6X6heJCGidKnMqvzmAOhEcgCHZ6eIMS0kHbgK85bwjsswP2nP3NiL62WZIkDMhtVh1F3wtJQjyRFcC_DbX9JEagMgyIpOwCQajvslXdrgblKahAcCYL8BjZKZerfDJqH82oug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLVlo51Q4i8CoVtya-16sFE1tSkVDs4wKOypfTjHXJkmEV4-ix1ve1tWL1QnilDGlLzo6SAELksoVf4l3n6us3B_IFWvBu3XKWEIVUm9_s8t1zTGtO0iyNTfnF-QhIZKAygyPbCjNT1Upa6wfHn38owq1rZoUMtT7HLOX8tZwc3q1peC3Ltv-P-9kfpYBQ5HXNV1ITGCuMukWqAxmDoiG7lSWow14sgGyQQefB2QNrTLlw_YKj8Oa9XvZWTWrhO_AKSD8lkdGQEI0LFGFvPxxVtbBM8zZGyOVOHz9mLIA-k7zljc9b8g_h6Abi3_xLpk6vL7ST4pGNRv8nRQiYmJCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=dreNFqFxZRMBM4_Q6ff5ioHlWmLZUA1kBx7kVhyw7S-YZoGpUzRWEQF2HUZC4rbM_tf2GR_ZqNQe7K1FxOKVHW_TIw26tCiKVf1dIrmE6aKPMTeG7qgZ4jftoHqDRcAW66qTuNV1C4t7D6IgkYtMkGv4LX7T1rIvGopKrMwYRHm33u0M6JL9CtMn9NvZFataBoGhQW1MwM11bhKnE07fCkf-mSv3i0B2iTSUHkyeV-ob6U2IlGnNl-aPOFT7y1Vt1l7QDBdZTFGZO9gSuqeN97lgY1LtI7L0S2X-Y3s9Ow4XBEFfaHWXDdTSk03pbs3MTCqahb5xuCWXegBerS0OMKvZrGREpRY_RY5DVAcWWS8u-abqbwDN9XgbfDHsjrJj6tsLi5ufo8RsXStgyqkdcQrpDmgzLN5I7X8yTJFuLaB14V5-aCi8RJOxWx7MalG3Xcu_MyTnYttjmoEsuarzYeQBb2HoUNK0jx83RdpHNPd4ezAKby4uks8WVlwS0_D8uQqs20bJOeGd4NAn_zD8bFjolr1UuSeFS2icNSZKXR0ps1Ot7I_5mLrP3U4cVcEbtV-gKStk5DdD4d_jVS8ZLsiQEYouAtDCnTtDCrO47d20uPNtItZKoe-iGNspF92li5pw4rCh29ruIXlfY1EMzzjO8Oo66YXEu-7_myH_nhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=dreNFqFxZRMBM4_Q6ff5ioHlWmLZUA1kBx7kVhyw7S-YZoGpUzRWEQF2HUZC4rbM_tf2GR_ZqNQe7K1FxOKVHW_TIw26tCiKVf1dIrmE6aKPMTeG7qgZ4jftoHqDRcAW66qTuNV1C4t7D6IgkYtMkGv4LX7T1rIvGopKrMwYRHm33u0M6JL9CtMn9NvZFataBoGhQW1MwM11bhKnE07fCkf-mSv3i0B2iTSUHkyeV-ob6U2IlGnNl-aPOFT7y1Vt1l7QDBdZTFGZO9gSuqeN97lgY1LtI7L0S2X-Y3s9Ow4XBEFfaHWXDdTSk03pbs3MTCqahb5xuCWXegBerS0OMKvZrGREpRY_RY5DVAcWWS8u-abqbwDN9XgbfDHsjrJj6tsLi5ufo8RsXStgyqkdcQrpDmgzLN5I7X8yTJFuLaB14V5-aCi8RJOxWx7MalG3Xcu_MyTnYttjmoEsuarzYeQBb2HoUNK0jx83RdpHNPd4ezAKby4uks8WVlwS0_D8uQqs20bJOeGd4NAn_zD8bFjolr1UuSeFS2icNSZKXR0ps1Ot7I_5mLrP3U4cVcEbtV-gKStk5DdD4d_jVS8ZLsiQEYouAtDCnTtDCrO47d20uPNtItZKoe-iGNspF92li5pw4rCh29ruIXlfY1EMzzjO8Oo66YXEu-7_myH_nhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5sllQm7Zyb_l9eCqxHn-hq0F9Tj3tWL9nMdWbk8_z78com7Mr3GAEnnkWCM4QwCKTgj6tdSZJb55XrII_Ygiy6Kz3SyHjn3KFV3gB46-3vinW4zA8WeK4FqP6kkN_jicW9IbVv8bMPWPnLO5kbDXDY2Diyv9V01FDOqQL6VdpBZLLX-xXYZepwCoHxYprZrBkO7SFJl-ye3euGiVo1ZB9RSMD2mVHPlDLGBLqg2MJdHsl7ZP8PDBu5fcX3KaC0ES1rzO9N31DvFTiJ6J9Mz0br4l_7M5ty7nDR_rUM-91pO6zVmXNDwxpo5gbQxzUh3jllOQ8sDHcjPFkcHzNyzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um-RA6o-EXhV1Ff4R0OzjPo7Hl2Dm5njwpWac7ZF2SK9R_4yIquOdIVKLZCEmdhO9eaEBEbwpC5kIzl1bqMth5XWoQf1PiX_TC1Fsu9s-ZS83KbmIC-gQ3VXjFTgmhaHnN3aF9EiTgc6Imz4QkyhJr6QOCEnC4fI1Ii3AexOKlWA7pxF0v0g7hJs5DbgwFsv1gaYqOWfPAyKxVq9WsMVNGLl1PhtG0HaBMjJ4G0LxcBLljALtJHJtmoqjD3Qx3Nwk4WTW-Mffo8hVfvniAuwQNGO1F26z5tjPaA1BOaUqvIf1qeDRNkFMZ_Nu2kPt6RIZh3ZKEr4QNLCNEv3WDBnmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scI7ESqHx4X71LbxmOFLi5O6-72rNUIJkuwdC7mjbB1mHtwCwS4scd0RqmUaaW7brhN86eyusbr_NEZ_Jc43BLYdGYHKqIILnJTSD4fmc96BvYgj0zT06XEFHa9z01LP_O-GijmsWRyM71xjha1zq-E7NI_lCT3A88l3_eVTrU5qhYSG532RYdJwhEAypKvOkDoc8Jsc7Xf_S-BJ18zcnEFSZVa8xfP6ceT8rA93pt2imscir_TLJ43wxzp9h0_i5SnGIRAOhg5KgQ-UlqGpu1L29kwE1l1R2yZdBIsRGvNLw3y_zzKuvl3ZHGYFRzb0X3K3d-Qb7oE5qo-p0suIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJP0RPr4R0lUUwslxuPo3w3kSRUobIBvPXRax4VSFKFhcf3V3OWVwckXdjknpnjLgya_gYubeHU1xRJ-40f7SuCbTXjQulUQteIxZ3bbXTRr3FDVRQwXaqK6kLVmB675r8axPv-IaybpsNiaZsHhWQ3fGmF8rGwd9EVtF8VTYBbmCYDQusfENXWOroFRGv97OGUkNidaBTszRms4CGi5gDazr1DDkPov1XiwYMtBdZHWDxPAmKxsU-a_xbBqwWw06TTEM55CzkQUJB5odTFWIQNZ3XMQik4GOU5KmkM1Iigcjx9EEM45tm50piHpCT3b6l-uWJiKBrEZx_B83likkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtMkJYiSlQ1_6LZooTTanXBZnYsSGpdMC-_6CdWMCCn5LDoVvbwDOLL8WVOWfNuGqD6Ggs0TJiaxZ0kOPlSuhDnxOKkho4q-dLYkZTllu6kyo7_WTKzrvPgqJ8bHsazV3mBBPvEV41Z6CM2Kzz5D8sUsMtehavwt-w45GVAXCnEnB6908N19aK8Vo0jtsYUCF7tPtL0CRNkth3QG04Jre2UheSGEghXjY75KBXw6_yoV0MZVEUzg7zP40wOuqUWIHPksqt9RDUMR-L8Peqs9sUkLCKwpTbTL1mmQpY5NcpnarHBmoh3o0BphHR47I7VvCrfAPJ_xyPe_nGj54OLF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SY8qOFU9AiEqGA1_1WjwjvFrIEicxCXxAW4H8LNBjcNvcf6xfzrEm69XmhXxU6WZ4KggBkdMz5hsM1EOqkxeXkRgYGUTQX00whfnrhr6UutNERJocc66_12c4zramzDLpLgRMamfFW6NG-gL1F9gm2WM9uXOkUPtw0EhfA8H7V82d2rc5SRs6WNX3ydDWgMtULh3IR_WCVke5zGkNNyRKizke4JayeRkYanjC1m5edWzPHGizG_5SRkPQt_XIdB8CIYctK_m0cf7CK4P-_40Ne5XuFEjy4kLnsCToqv6PA0gTUYCNIPj1pIQbhsmE8RlLTrBK3g27ydQK3Es4N60ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGZqzlnt9AXjA1BdsC95CsttFalopuGp_S_I5iaZTkf-aKczJkd2jCnRgMjBMo1oDKT-MDwa-GbcN8dAdZCWNr3gLC19usc5NPymRX34vG2fu8F17A7XKEq3PBsFO09iq2S29g8x5pyqyov7_dnavogL04X20vglbpj2LLwLhMQyamM3hUSym9obaPE_hryaidXzlxjzsmc9yc6sn58VbUc26bGiUQxLJNWTxDx2kVf9q62EiT5NVht5coSOjWKgEIaUUhNAqLseQsh7OAXjaRHYWIqqvew0YcoOIbzfMQJ1brMLpmaTXjkVHgZW00g0YAdg1I8_wMFWD-JkCIWpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HajVAk_sO7nMFqs2H8Bf7VHInMairGB2e-QW5vwSao6Zwe1FRBG3POOK0EiVIi2jk2YJI3gEg3wdmMTBwCGiDOaJ1iTot3_DA0ds9plFj3ZlLqDp1YCpZIp3x_SsTpgkEhcX6YzbQaT25SgG9V69r4HCvuFFrHhP08Rt0077hPuu7xiw7zTihEBu_qYUMM2f79Z5GhxwAFDeS_lTrdnsHj0jO6RnnTH59gMjaov8ZjZHD3JPmlxSB52EDp_en10qxiHyTeT6B_HNt8tuWAS-oCCaw9Xhfqc5RUSwsYi3WNPi4mY5qA9dctqokbFlR-JRxHTh8B3fISFmNnFqyUcLdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK2JsnnoVRNRTX03rXZA-s4vEPdOsby6Znw_PnYbFyqRyAsRtcHrhsPLKjVKzMfTI5ifY2gZwRJ5NlJFFqoQ644mtBzHLN-JPW6yhr_hpslQp8n9fsKb65NzfuoGniHML2dJ7K_d9ILl1IT6Nz_Uhi0u32ir0zn7b2uivx4YfsbtxmuEPot4dj4gvj_UtaGOIaAAOE0Gr1RZqmT45mGwnvIdFPImX6BJXqGpO_s5PORjueHNkbOb5JMtgkNIZhqimXmKnvT50zz8t_NCoeY3WURodbu4hbIPlKfO4703ImyAWxYUpw-FxLrm5Aa8pd63WQZgnxItHdtbCm8586T5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvCl4j33PDEVJBA451yLaDUXBKfF8YD79m3QfxmT6nVP8V-oIMRp-vPrDKGFMVhoajy-ji0xu6KFbqR5JNiUv7kBc26JBxeyav-10FoB4ukXQe8bJxqmiyKioKy3TFwstAHd2pcwlalA7oXeODln-e6zPMfUJvUPLT5apDbcAYJd82efh4-1X_FRBynDfHNqOiredxUJrMAQ9BeqXAWW2fXizkAHVT_-CiAk7_7mbYQVNMhLsp1dGcLnM47EwD5FxKjIS07MK1ej4PahJ7XtYD2tIWg-jPEfXzYNNWqEw6vgzK-2HChSf9yV6jl-49W8xEGn3JW_FKMxsFj749a0JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHIN--3FTd4la44ldnQAmfaCgjEnlmm4OGLUbTJu2Ql75PsqmjM0yI-mqEXMXIOZLR-pKYJaceZeS4nheIavRtvi7EkJYy1wNoMB57I0etueIxzJuFhTOvKuSd89uQEcp_S1W44da9meDDffWin7XathntiL-3_HEju_sDZONKhc0gWo5LHTaGEcuAoPyukGIxYs6_Xln8Isz5W62yHv91m-d6RHNmGrCU84-8Iy1e_kE0NuRsHmVmjKsUta48iPeXqscN1eLpR91mXE1TaUFC59wc3fMSTyKC1JmXAGQreK4N0yljGjZhzFL6z2lrgAjFFE4ZOzerMhMH9FDxP2zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLyn4LyDMYoiqfD9zycOn3yCWSYeEfz-6n9O8OfqOY6kLl-2fhERjp2-DU4XdW3eQQ07jH3F6pRbTJKFOzyQSflQhbMxnEGle0NAOIiOTP6zRbn3cRq7IXQXUi3fcFq8jRMef6dMcmjP6NCZu9SeDC7XJ-iwW6paELZq8oPyqGMfan3XxUY4GDv-E_18LAtee1kFEf2LYh--lVfn2bqSwLlAXC_8lDG-iXObdnJeXGfmwoR18gAu52nHd2grFtHb-dhoqxlD0sRcIrRYijsFOZKZDxCnyrT0ksreMjLYLPFtyh6mgYXq7cOvIfR75j79qiX6MkY8oiaM7ybnMb1S3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaZYodh350AiV2WiVDHuMXUPFec74sdq-kIF0LZt-H_jZekl9wdh6RO6w1Np3oWDdW9mxO3HOeAmmpv2IvvIOM0Rzv0X2dOoRPJ6h4SWgj3v0BgaoJ2HNlpiDDqkW4DqAVmKCYgwuDBpm-Z1PTnbvKoSL0naxZw7W7O_CyL-SNRk6hdYB27bGPvMhH_P5le6_W-6_XuDel8o7nHhRe1DXJUY1UTlDAuEPo_rvGYVn9TJPnDi0KorQyhdxlRcwvYkqkz2UYPhJ3m9mv6gSHsG8ajPjjQsbA4FLhAwbT6CKEdnfmERVy0SXZc9gqGvb0t1_dkG_wHkYNLSCze1akECWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnlaTy6YduknAq2djKf7VDVViU3OAgO4SZuL-bg1vAAj3t8zbEbwoDKSJd7-GqsUgz12xOUHqqqwkMl4moLTXvpw-2yPLsCT0EJYLc8aNFojhSJxC5aHQipJiIcjcMSgDujMYtG6XY5jzSMKSvBffgaFQtXeHPngxLvBJ15s4-HetoQuODl-JkvMsNv05-VPaA4W0vIc6ZLVB6vK08vnNxuU_1KgOHDO3vlmrUVE5KTQnbMHe7yvfjaNK_zIsWKnhwU-4gyKIuiLCw-fPDArkwg_3DvY05ETG5TrBdZWzPIQx0Z4F5ld1Y4GKpZOYP6SHH2NPg-FspwACRefA4DrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjGq_ygsMrHuVvDIcN6OIZ1D2BaaiZ8lNavE0ZFTV0O7pDC_4MG-7zmHpnHs5_SvujeqQeBRCO3ten9_HEUzdM7qC4NBHYkDwop9aB1s3sRQ7mq1aSKtfivLDYxatT-W1JVgdbarenSKVq4EhI_aRKUQw2p2RIQyOsKKHeykAaccm7ca9M1exjJk8Ot3UdgZzSHArIUArcVMmaOoujfJBMLpZIPAKUogN6IB8rYSSeSv_tvEUJkj5bUBmSMyYdilxLPvmg1qkfAQ-xmCIusgYWkUMFUPIJJuCDuiJvRBP27eY_fiNj_DK2k9prP_j6MUBWvjML9xRKO1Ro1TQDvtIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-lTgDZNyp_ELksQwGM8qe71QlUj6LgiAZ3F8TyL6dTF2bih9mLELAaCfvn4F6CYIgirDNFIXy0TCuIDKIj1O-oLF6roi2uPJCfldGTLCSeL1lYGT2DY7EfbOcAmo-OUPm0bxyvzPYBYSOaO24SM3lAEH4nCY-oG_gBZkyYTT5vKjOwLxjlfq6-WPoCGB_SA8yoM9XdXub0qeqDL55AQRXKTdbZXb3fW3fwzGoREYqiKoDAa7vaoiH40Z0zxnTOq7Y-XM9Lr_F4mc3wGTNBpuQv4hT3HAvFtGn6KesbirGWglpb1J304y7Kq_kBg6PypZxiAWaARbOfJS4BKgcH8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdUthnNo3uSaqTPZ7W53qbYte0KYR836AqgLqKArSyWLZeFm1lvqTtwWS_YAdjYO_c_sYXIBEeEL1L7Qmuz6ByS7wrmQDBuiZQooSTC9Rkc6YS2ZvJFsarISccaFb7LcqPqCLDSb052USxbS6E0GXO_XaTovyG-DxYxA_uNMK96YLe1vL71bXdQSeqO6SLH69sVJ29S9evM_c2ht-V92Fw1t0x8vHCIl1iA7zV-gh1E6A57qDur3Uzj5zIZmu8vuNnJF4w-Qv7NwBAYZTruOEzmsZKSjFKZqYePoyyvCVv_n7I7tX0avSWfS5qTS_UjELsAjdIAOtdJvDssfsxkk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzHwIcK4c5e1JI9VpfzU_NViRWBKHuX5GYNhiyAQhRdYxCFDm4HaVa8JZ5VCBRQrdQz0KBO2GQu0VnN3CwAlA02MdOP1lsTDoWybpZFxO1DBSYIgsfVYs4iQUSc3K0rQxEsgwCJ22NjVoZjAMwGHZo_OysER5eraf8_iQDG-1mHySMjJKq2S2wJo0lboiRFQXaUtcG6dCML8w8KBzPSDCi2tRCZ2NLiHGxVwL_KmM8YjYqTQrMF1HZsQowQeT7R7Je-Bi7hiAsOqlj2dCTcObnhkWPGxGiB0lZDHkNMR42oa2dGunsXfOx06Kk-Kq0rIJ6i-IPMIf0pq2XZOe8Psbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG3cXhq0HeZyP3VZtmCAIHcNZALkM0RQtNAABgf8hCgoYdtdWxgov4WxKjdycizS8xWQSTQUrIpln_c_lTETc_0aMK_lp9hiHWgpOVCDE45BUsm2NsF-DBRyP5vufLFxVYJ1P3z8YtEqZ6D8x6GvDGz135Xaow2-Q3cdzaL4IaimYVMuIqoXnhBHfCZ7OhaPzVzmMkQ3bmFdLOW28SSYc3YoAIdmbnwyCP3fXDzzbzKe8i6X5wsdDmiVc08MvSFNZaktcd00dT0jJL0jncPu3YUNJHvZiL9FPPp08Og3r78WGXNHhU3-r_DhsG-2mEwckDztXYoRgCID2p7E1MUo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuFP7Lbbrbiym3X94GTqz0vUnrI8nOWdVSPEasMym_slwZYavxaTQ6Vx0j4kWhgSTk987oohgGPpJO_PzFBDqpb_5_8QdjrAiDKoBd1JrOpo_fuSaDZQXJsrwSm9K5YWll-DR_o3-3iQPp4jaczcDs6EebKCWxB72LC8RJiVXybEfGaCmPaf9zfevOsSC_RRCwQLmyN3mqmAP-C1FQdcwbOPRWj1IZUKVDSx8r59kRJ0svfWPClPUfmU1qpokZa2EFPxUJ38k0ATzWYKskM0NZsAGWN14ivcG5hxF0W0t02N4hJxlHlgNgzZDTwG-_kXXC8RbBbiIX-RWMrd-yxt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFK4nzJ9_ETPlkoJBnvh9xTJ34NmhlDycAYe_vin9srvTRmL-d4atPrmxKn7Gg9eYmacuC0Jww1tisist9G3QvzDtGcUdETwM9gKHJrAzQTCogjNpQLsT4zgpUInN9G1fCx7bAzg6m7PsiBlmMRxYkrYELhkM6-5Mtk7j6LVj2sRPw7hn7uKxG48SIAS_OaovN4nIRkIvYp9dvKkAm1BsyCxeaNBeeOr1ouvwFnIsohu3OhuB634BpH1RBuA-Td4u-JICzpYJgb8Uzbt7LWY5w0-jni3D8H84K8RVE65Nt39-VmqWJp3na8rDyL8ap6L9XuTufGgQQ0DA8PYu0TLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coEdTsWFN93Z4ztvrKjuGTULTbPJci5hBzk7DBWjTaQzzPwoOMNT9lrhtEjY7JaN91a2jAhDFiUdxvji2JfLagsSZtIRQGnPNzcRuxbSXh1WXnlZp7ggeb8EQsKhSZbkJKez3hErLgLJjvwEP_POf4G9mILNfSufPdOfPnRrmHwAMufyqBlQ9xlwbyTbQJbF0z7OyCMDdY7i_BUngQbGnL-1Ns2nHw4TN3xCJrVOum_FH5mkTDaEQ8u5WLoAPRyXJHHhXn7VhGSaJ6-eZm_bVRbcxsWDVBy5QSo2QDaYJ6ZQNkOP0B9MDkzK7J5IdJ9bk9qBK2-qvYFcFLU34ECbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdXcL3vMUWdpSzEgLprN4ZHlM-eAh6G08A6B9yKQWrvTLqXZUiSryVkshsVuxN8Uz9bXp06Tg-16fsSadzsVZ7xLWXiaZLcawpKq9FhdkuVze91c2SOMq1gJ4cIFPe1LEL10CmnThJmgUMKkjItgdylFMR_IHi4Na40-YbFrRCsYilfhkjEv9s61Ctvu_A9yzNrxWUIbh-rbHrnHIeU6npDiVvZ3-Bu_WpQVpZ7ciPwMb_FyRKqZ7PEPZDmokQ3_LbhMgXp8DFpoiuDM6p3xO-b8nvPAyYmC30kguDDdfX3jshRf9kAXFs5zKOqzkvlNh5kfiYemZZTQSmh6Qd7Dbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1Uro2qb_mQ91bDqjQG7sb2FaoQx4YxHv-6iV0mhX3g6fTvOroIONNThqEpVzzHiRRLAVeenaJMxVMH68wrDEGXqaTwZghflevgoLGYfrEn9Mtc4x6zeRz5zSdy2W7xRMwvVnF8cn2rwTkg7EKnMxeRdS7wjKauAAmVDbwsu6gDKjBi2n9_2HAJ2ohPnPZ3Ri1BEtEb4OdpWKeJjXDfisTdMfBi7Z8z5ww3YS2BrOda759ve2Ohml5ckJFFnKeMANNn1g_C5TBtjkPRWxkErtGHdKUCaoVxd08sLaPgJWfpZuJ80jdEwsMohHkxfsnmB8G85-1wKCzDzcGwI5gvqtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHHlfAoV_mHssR5Y0WL3OCrSgyTIhVZZKl5t0a1nIyv392K-OYg6kQnIU5fBNSLbchUPkp-z0XoPnRdoQNorqHMPsojF6hn3_rwNZI3NrurR6-aw-vHrQkKE334mxMKN_nqWClI7RHDSbDDq51NXPAuMyTVN6gBqVIFZ5vYDF-HEF4PTKIIBtfrQxrnwLv9woSwB8P6HI9ty9svsyXAREC2nbUT0NpQokwGxaJY5tU7xIwMXrrkxDy5SyB6dpDQxj8bDF81MnpLNGGoP7SMEV6OBKFe0A2vUBs3_jDL7oDGFqmP7amC0XalaO_AWan52MEthw9F2CSji4WLpihfp_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKZL80kGjCemNCxEwPNTndqF1RrUiTnau4ZNFDGB7DouYK-9UXd0A1ZoxqOBfRu5fOt6J2ekzNFX7A8pNXLTI8-tZL-lVVJ3G3hgk9fAwcNjH1htihHr09niKztDVhliJtKC_s47n6GIET_rt7Ou5nfi04UCp02jKWVQPAVzYesslDmcgS4REjbULCIq_ZBScfCFZJhtWUUGLs03UPvtLqtwEFO5kIQvYqXypagzFIY_6knJBfmiCVQf_ENq6iO_h174xKCRjWXPFFN415pbYcTJpokEHDz9IYNo-F6P6qQ3rVXkKkB1RSr7vaeEKhrM4Ui86ja_MIKuHfPU3RVy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8oVq-FF7z0tERxojg1PfIzqGhd1E9xZWjzIb1Kx7iAPXb5n0uLShRFBgCs3MXJJwoNyFy7zKiZv2lDvzWDS5_pWNBYinXVt1KmXhMAWdbH-Ur-rmkVsXhPBFzkJWMKcuE5N1w4gTN0zFo4MCqvNeTLcAEwpmx4COWk2m6BjgiEiudFi8KPhkHImn2m14sfOpKVMAMxdb_wLPgQLBrFpYU1XNJcHDB3rJKanGWDFFY9S3sPoNXI7-6JbyaYixSQriaVvoJFp7nC4S16Hc78TMUteus9CbZuffRkKacK6s0XUurO5spTnWMqAHWdqi3EjBe8LYjneVeAvypnChcswOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVkn-62SJ0YSjbGpbHyWiG0VnvXZ7tY3Ed_219gxxasntzF6TMTBtUaJD7KThHp-6kNV2liHjSIeFD7O9TNrGGkJwevXQs5hXwL29KHrHIAgoGEALzLpz9Dnph0Zth-xjD_m26-ValK0d1zNJG3MjW8bVRYGbsDiPAXa6yZ8WcMtixs24hz5Cr0ZjcZFTi7u_E22GGNZj8KCrTiVz5CcuOQhR3-HQBHKcHzlGPg6uFI0WJPHCllqOrJEzJ83KaapFcL5aal3TNa5ZcVqb8jNSVbuzsVDLwkYoTmIqDznzjSkt4eQeiWTozW5bOaQ-P6Hvd-zq2bUTgYB9pKHbeij4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEgDhx8kMG4iQ-_G4_TAsUi1wBZi-DYzedbGsYEW3Rx0inZRxgLxDk4G0FnbB8XNCjx_WWAHcQhZOYlaQgk5-V_txx-pAi3kL07THyg2LFHUMqvJAPN7aKL-IKsMhZyznhx1RBqrrDgql2rxzO_TCkBT8tL-wii4YFuNDEFR4n2gwkSKje586zMwY-_DlxPNHk3E8SUr7-F3bBTrGOYiP0m-rq1tAZqmKMbeON4bktGf9DUW0H-cRVCuEC6QY9wSKEmKwj-SM5vO-3AIPp8boy21hfe5FbireXusVKb1lnLUOzdsInuMZFXI--doOpTetf_6J5HyVa8AcD--1BCCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVYdUZBIPfrYKtYwaJuheuYqPWVLwHfSbYA6jUP020etBeSCid_AV16EmJy2gKK2LHI7JZUH5wldTMe9zQtr0XR9BB6aooo7bJRNnUWCEG9b9bOJAlGGp8O0AbHiwP1YKwq5FleiT3uK8lPOeh6ENakB2jv_fDm5ZTSVimui4Tk06pBq_eWtGDhNwNTuJri21BqHhfhjpN53fprU6U0jSNrXcFBtDTKgQD6XMAAwLsykDQyHmkUQz3EpLeASRELe-IdILPkZatmz7IkraIkk7jaKVpWt5cSYJ38vmjri2ALSxSKMGJyVBeKq3v0Hzlvz-GUpkfG81uFn2fbuBaIuvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dl1LNJ_OMyLZWJePmremgpkbx-UhEMBUEFYFGQSZYA2whUwC0qBM43cr5niZT9eXxWsAm0dBqwSf_3pxBF0fE1UbNai0WXaUr_PkEXRHJif0KG2Gi6GjxFeSiLdpiZ24K7qcwE2U-nKSdhBNzE-8PQm1zdpQmeiynk1giH_ipJZouPhtNfBPHDFMuEM1OPk2rjyOHBxq2ziXSMKiMHGxkiYWWGvrUae3EZMBUSyNze68bG8lbaZMfRsbpZKJV7A0ZA9LBsQUp0RFNrCD-Zqw6grrkNzBC6mW3SA47OdPhhdf4Cs9e1nAmB5gG_RHHZTktzdaSMXaaTf9wS2X2riQJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hI7s3LJRMtyfRIaqU0VCVORwZY__dMHOGV5haqIzAMc22u_VteKoK83gJKvaIzyc5qyOraXJAdffrp-LNidr-ZQaL3_QhxmS3inmUHEXQ9ScA3FzPMDD8bqhfuRA9PS1CQoDpfeSC9tNydu2xqrSlROm7OzuSV2k-87-_c1AumrKnH7jI_YobWgU6xr5Y4IeejWwsSv4JwCHVXTnmRdxDgLeqifXFkmIZv0v9K1TK7HPdNDZB4chw-k0g_xOcbOYnrpdse-9MS8CiPuGruaHzfrYv2yxEqEVuRPABrjWr2f_apc7wGpcXk-mAhRmZAaQZSxxejmDZAT8a66dchqkIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEOQ97CdRbabV4bzATHiX6cuNm1ZMKTLCZx_ksfAd3U6Ix_D22I8PI4KLn-bvTUcxUUs8KB3OmUQE3S1EFB2H2PExnJh5_7cmOUFtsE3Mpz-iU_eQtX0n5orcc1FPrquiieWff6GiJ5rn3iyxNeKnb4g142ZXiaPrbYCZqUjqaCHLwszZ21mZBoDkNpzI9A0Ads07lQpsNt4WbVJrfs0hLZtlu0_oNxthvxTXMhzK0jhIk9EmCZxckYtVgnSoWX_LZvAWHZzPmkvwwjr9Vyq9vYlkjWj8qjyfof7FuhnOtLoKcYR0sgeYe-vbeulou6-moSu3fxwyHr9oJTetdDAgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmYrZN2D_ygz2kF3uqfxDpypUeEHwl3KwBm_tueKNw7mreth1p-nw7zzqxB5WE8i3O_K2ytkcROn5ukpMrSOugsrSvtpZs-SCNPpLMSC-oyUbsw0g-y4PVkZFVX5aSGl0-0puqXpVxe5BaNA-CbArjRbCayqdbcCie26kcsZcQi0rUuL-2Yv7QEGJHCPpBUtf0K5m_DK95wlEKdoUoXvbJm_4GRvt2uiL_N5jtE3SvBfN3V1J2IhZmClOb0bdBHHmkZrMDdoumkINgcNnGHnunoUTkDHhnOdRj_1MXeALFW3hXNECSbbJTYv37rVgmDKsRN2DZVAJSy_dok40xXL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=PbsUIOt0504Owiw4iy90ywRbrdc-JS36KeC3bNFCR73rybe1Ou4I_C9KL5_ot8wX-AKX1m6lfn_Icx5OJDoXdlpv-parlDT3mXTYX7xydtnIVMTY4pyIGFwW9cKhXtEQC_DpCsk8Cxo117LJ6RYQSGI1qyNh1lAL6Nxy2oihF5Q8addJriTOrUy9tSMJtz_xkG5eGe4eQPUkXHlScmD7Qm5-pgqSls61LCtS0AYb-6icV8Vm5dJ_b06HEE85b8stdfnGzzRAG-u2RXgMW-4qxZpuLDUDpwXG9tji_A_DUyCNzMkNei5bKwGOM1kxaOhPRjZTncn6JlUcFRPn7wNT4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=PbsUIOt0504Owiw4iy90ywRbrdc-JS36KeC3bNFCR73rybe1Ou4I_C9KL5_ot8wX-AKX1m6lfn_Icx5OJDoXdlpv-parlDT3mXTYX7xydtnIVMTY4pyIGFwW9cKhXtEQC_DpCsk8Cxo117LJ6RYQSGI1qyNh1lAL6Nxy2oihF5Q8addJriTOrUy9tSMJtz_xkG5eGe4eQPUkXHlScmD7Qm5-pgqSls61LCtS0AYb-6icV8Vm5dJ_b06HEE85b8stdfnGzzRAG-u2RXgMW-4qxZpuLDUDpwXG9tji_A_DUyCNzMkNei5bKwGOM1kxaOhPRjZTncn6JlUcFRPn7wNT4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhKcLaMvOJvywzBu0-CPhmupaY9QLg8CxTQBti2I--KIsYWMW8zAcoRzJCvHiH9I_BN5QL9DJHMyHvth8nDxRN8rNp-U4VKUD9KnqKaOC2cd4YmnxuCIAi8TLVhmZI-ga_mmvEn8IDUymRhC8PU8gXAUyb8u9Nb6zteIasrEA6C-bfkpoJWUHR1UacuzTDj-o0ugGNhSsaVNzeUw9pdhQvx7D7LeFzzJqANqulWHCEFe7jxF_gvUOrOjhbSFHkfIH46bzkLapNQjDytPsW6GDXHmlZqyk_bqi7ZeOt_tmE_mTfk2OzQk7xl7OR3Cj44q2pyXUOSu1vjjUf57bMdDWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=ohCS_iLmxQ8tnMAmEHmyzUh1g18iixxkuJ2h5hwH73oez4jTe1crKSm1eLh2xwZbU-9wAuK_myDkcSwJbdZYVQWKzAWmhXcf6ZdVI1xEBIsUwcyh4ysUXvEPKdQoYcTcBNaHWyMG51okodL12RSdmNaRYCYmpQMRc0NwnAv95jvFls_9hPmrgQHOo_KxUNcCsr1MAhHfcPV4syCiTukIPPRkhgq3-WTgWmhTbvuncdDNdq1OgFhJuiknq100gag-L9AqpsycX4l9dYSXy3RYMABFavKhgYOXV5ywkCWh3fihZSovkqDjAr0ikuZP7f9uT_IoJCoBjs7CeIYdCor0SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=ohCS_iLmxQ8tnMAmEHmyzUh1g18iixxkuJ2h5hwH73oez4jTe1crKSm1eLh2xwZbU-9wAuK_myDkcSwJbdZYVQWKzAWmhXcf6ZdVI1xEBIsUwcyh4ysUXvEPKdQoYcTcBNaHWyMG51okodL12RSdmNaRYCYmpQMRc0NwnAv95jvFls_9hPmrgQHOo_KxUNcCsr1MAhHfcPV4syCiTukIPPRkhgq3-WTgWmhTbvuncdDNdq1OgFhJuiknq100gag-L9AqpsycX4l9dYSXy3RYMABFavKhgYOXV5ywkCWh3fihZSovkqDjAr0ikuZP7f9uT_IoJCoBjs7CeIYdCor0SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSvLrjbc1oDhKcUiXDsT69MpTQMDh_AFn_l7BgAi8Szdaz5UZU2kltiAtc5ER_0MKers-UCErXWMm6Gn7wHUJOulAvva4N6HI1wOXM_6QLiauAeDhhdw9qUIHLDOX6lnGfU2jBwV8MKPKBpRFNA1OBRIbH8cupw53ictCerwN1xsviXFqCmvDxCkKeWuAq7xcIdMggnOeQ0hhlk9YaojaDup5Z-YX6JIHq1_Fy_W1cqeyuNV5TdMzXXNJiNdIHQCTAkGu7sbAxNmNuahMA1MgM7KZpO9-ZzCobC41jfk9yDdUthOeQjiqkrVVJKDiUZ0kiW5da4Ge82_Ns6fT3ogNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhJYG78fJGRjj_Z2G8UTk5i8yD3awjtjkCDt9DJr3inacVnFKHBVKbpTM9LFGGBxhlcdkeZgFxxly661xkFVFhdFGrw6Vyb4mGwGcuqzh6nwo27tXIcr56N2L51GjfFj5ju4c4qOYA-uW88RujvJDqCdi1aFHiOzZG23rCW-_UdGsdlascvrKGo0ibimQ7ocJyUxkizm2Suh8V5adZpCN5JZIn3zskDZdpcz-6NBW7H1lLRQROXpy3JAPwS4yBeoZiHR8E2of1KivltQLRVEgExpSbDVth02rIgQcTserkCiAMHR8LsJb6rFKmEwYXyzsnWOgKG1ht5GW4Ki6G-jHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=UrXpd2QeOauxjIoiwL9olwz9yiCSF4J9JCgMzXLMznxCKEr0WxFfl9zdvw53-SAyJF4STH9nqlr24tt6RAeo0ofTI9E7-DeAXa-WCpVH-mcaIg28ryY8EXWxChXwlsp2c4LSaH88yVYtIDCzB7YGpOfpnjN0hHbIEnEMAnnX_3qDi3rfxjpHbFGQnhJaQQ2V9tYCh71-RXqWXbju9LS5NuoTrnJp1G2KSF3K6ptw5kRQUtpOp_BUM-K92pgefWW8b6YiYMvhJMHB8key-aHDnzlg3ar63630wgaJtJLvGwUHzqLR-R7qY6zO8K9Vrln1eAUTPbR_mqfYyOlu9YleyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=UrXpd2QeOauxjIoiwL9olwz9yiCSF4J9JCgMzXLMznxCKEr0WxFfl9zdvw53-SAyJF4STH9nqlr24tt6RAeo0ofTI9E7-DeAXa-WCpVH-mcaIg28ryY8EXWxChXwlsp2c4LSaH88yVYtIDCzB7YGpOfpnjN0hHbIEnEMAnnX_3qDi3rfxjpHbFGQnhJaQQ2V9tYCh71-RXqWXbju9LS5NuoTrnJp1G2KSF3K6ptw5kRQUtpOp_BUM-K92pgefWW8b6YiYMvhJMHB8key-aHDnzlg3ar63630wgaJtJLvGwUHzqLR-R7qY6zO8K9Vrln1eAUTPbR_mqfYyOlu9YleyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYN6CJ1sXjOS_RJd36NHaBdkYnGMfYG8gG_d69j4M0snPV2v4og6s3F8G0I4FmOs7qxzn_Jza3GmUhvSJpI4EIEzsBDWRo2QmZxzFmp4NQGjroaaNPFH2g0jv7Zy37LSWusI-bn0_vLIt9GRVqkuDyNODVvj0OJa8-6iiQtxiPHCp_ZSx7X8-abpdlBEKuDjaSzXEZpsK2f49oWv3i2iBL_ozPUeDGGQoqqHgQnCEKtn59teZJlWktP1NbsDTbee5dWsoive_vWBniXSuJWHtRNDN6dfVyfnFPadyfbjFwEZsf4-ExXObFfoGmsNyB3fX10xoRuyBZzSSYbgGpN7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le_IkBVw7h3SX1fO2OdtzaMcXS8dxWFtqktMhfbXDLARa7DFvYrLbWHP2KS-zEEGQrSsc345eaCPhrUYqB6ILwDQAVH9uvR9BR1wDFZ2NS0jeS4km4hSrniM-zPhm_wEj6lBP7X-H8H4TxZWH2vGmYa-Yeg0m6tO2han4CBjQzlujN2gsbFx2N5UyiMIad2SiItBfrrztzQsKEsbyqyZrKZFB9oJTkSCSlljz4U8sQk4aUyBpl9gCDWwla88gNcanfMXbwOTr1ye_9TFxAL5FUhkMSm7LrTgXZ2ULGySMpF_QiqE2bAwjMmuzYfAs_PTu8kGpjVJywwmxz3MTW4LlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oL7ukSxvKQAzjNob1OwxLusQnX3oUF8SA_wAQBSG-xCBWSJ5yqH0NjatNDHE4wojKM6ozkCC8V1Yx1aDdALMMJ3r1DIWAtPNhm38ffdvdtILaj2SuAjGRbozRJcq_nTsPisTad6UuhaMS-HKhuL4pchOU3gzMAhWvA-At-SRSc2QtJdW6pXKc8YZeaRiT8FqTOPKAE-guiftNJ5z4_rdCDT9ox6Nph5yEe1LLFcGjCtRr6ufPdF9ihZTffJmPNzkLsZ-_8Ra_gy1F0X436XNYWnt6Dre5lkgGVHPcq9CKDByQI0M59qJ_vgW0ICH9awrydxh1VGH8XSII-3ciorkQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=bkUuHtroc2i6r22JGDvE_JeTZKF2XiMFRz8TrIB22SKxUV789GmvpiwVxNKIjKf3-kGfsVp0qhhkYNZZuQ03G8QC95OXVDNi9n766KTVD7-aRD-4O4YyZ1ujzdzjVeprDV26BbLu8WY4cKq29p7VaU-8-uM1rHbguwKLk1JAwSECbBlEuYanMn4EitmyRkuQ9CpG-WBsL4_WTabsUV5oUZJXKY4YsvTh7cPTtDgboBUy0lfgtz2_0du3rZk_HPNZ4t2thFd735fS2-0tEZYDRvUhT_g7gQqVOvT-abiwulkKOj3fSNgH1WwqbuZazp47rGXsvFB1Q2daUCP5P6zVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=bkUuHtroc2i6r22JGDvE_JeTZKF2XiMFRz8TrIB22SKxUV789GmvpiwVxNKIjKf3-kGfsVp0qhhkYNZZuQ03G8QC95OXVDNi9n766KTVD7-aRD-4O4YyZ1ujzdzjVeprDV26BbLu8WY4cKq29p7VaU-8-uM1rHbguwKLk1JAwSECbBlEuYanMn4EitmyRkuQ9CpG-WBsL4_WTabsUV5oUZJXKY4YsvTh7cPTtDgboBUy0lfgtz2_0du3rZk_HPNZ4t2thFd735fS2-0tEZYDRvUhT_g7gQqVOvT-abiwulkKOj3fSNgH1WwqbuZazp47rGXsvFB1Q2daUCP5P6zVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=kPKyS25nMWKDgNL6lZsRBzSJ1PlnVBgOz8x6gkHyvZtWhlZ5HRFWHGoXzx-SIyUMHWS0AoFNa0h8Qbn_DM5UVwlePvEZHN0sbXcpZ0fy_FOeF1UrulMFKOgzst0gQmOzrkOWFKPWHB7LPe670LtbwlqC_-qXNPu08vGsU67KZ0GfPK832e-8pzdysxIrNvHzITlRHRo-W2GYvE_wPSu3rVVzrkMjV5s1Gr7dtnNUTNvTBLrI6FCWVNpfFOeQ7TmxfYi_rbyEvUrXWfh5DCI7LnEIK7PXjzxhFisL5_Gx8s4RzjFAfi-Mr1lGAqwG5vyQhD12RJ4dPRPOyohV8pfhTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=kPKyS25nMWKDgNL6lZsRBzSJ1PlnVBgOz8x6gkHyvZtWhlZ5HRFWHGoXzx-SIyUMHWS0AoFNa0h8Qbn_DM5UVwlePvEZHN0sbXcpZ0fy_FOeF1UrulMFKOgzst0gQmOzrkOWFKPWHB7LPe670LtbwlqC_-qXNPu08vGsU67KZ0GfPK832e-8pzdysxIrNvHzITlRHRo-W2GYvE_wPSu3rVVzrkMjV5s1Gr7dtnNUTNvTBLrI6FCWVNpfFOeQ7TmxfYi_rbyEvUrXWfh5DCI7LnEIK7PXjzxhFisL5_Gx8s4RzjFAfi-Mr1lGAqwG5vyQhD12RJ4dPRPOyohV8pfhTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWX6WIG_RCSvV2EZh4W9vvKH7S55u1Sx91y9RyQzM-UkWtlLWRrj3kA3mq8XsLg1Akv4_LLmGruOKBezNQ3VHFLla74OpUyuwZJqmTDLiLeGU0XjpxaL--ClmM9P9wIygNaWKjVxZF7kmbv4XpMDKBV9PzECxEi7ojUcgtAzhdqwCn-RM3CU0Nt81_NOle8kNVfNzqafrMeiX6NaKJu_BnxFGWWf3gE8W87-cZX7mwkM7ws2-R-hUvBhv4CRLGezF70SuDp3xEmBwf-Nv3s9uR1wMCQJafODOnpSVZRCM8Alt6bQXHRRkL8FYRV4yACcoqTis-PjdaCjLGVDp2XTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMjbd_0p955mmR5q3PLogGGmk7TGuleGn3VF5T2kuX1sKcvtognbDA_6BwFu-6pWWUCZm2ZyjDWuDb_ksLAHU-e8tazEAib3BPSoltkB6xtUumkkblnDSS9sIH-1lmGM6RVwXi1XvL40ly39GUgA8bfrHM97_HS62hC7wzXt1o2VGrGGkv-gtNzgyI-19Af2UOh0LsRhDBRJDF_FZG56RgYpTHhR7u-tymkGsxi5zV-4eXPgni2b8D20OKWEVWL_BPNUog_5DeI2VqhK755tTE-8HabH6Y9viL5YFjKnvC7Ig1ne5VboK9qg9frMpTrefWaIXEY0U3Avt2y8rtkr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7o00GlpHn_Wmsgc_tyMQYpQVxozVrYYvXG2I954-JlFKUP_jhDvutgtsAdiIXjQ7keDbXVXBB96bQQh0Bv_xfyi-RDDYmAzfYvf7SWiT9WIPrnh6ieD4hD5Y0SlMhOTt_2sFdoG7VwZrgvIVzriNqVQfFnW8r39e-blirVCHiQfZagQiofTNW5u6jVCiBaXMK4D-BdAoMUgzWRbQq254skeIjTSfK-3480zfCGvEAx4230J4_SjjLsmKpM3VAsbsc7zEXQj9DKjAUzyQWSdg7WhqEA_CTUjjfLr22qJtuuU8DuXuUHQ0vI-p2y3W9iweulsY4WCikrOsUOnFt82WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eI0NLQrHlyJWJb2yuCGBMj3dKE1A8nUcO5-NAP4M1DDfjm5JzXEsHBM5KO67hcDVzdJAsWPdWcVFOm1YPskP3PWACSCog436ThM9ZjUafsBE-Qemeqgu7WOgZsA-k0q1gz1n4z3JqPI14wLU-COAzerpChXsyrDuVmITaEOYAOivREzmgTV74o5erNSE1LC5TYHOZjLmVK6jU4WxX7je3Crdm8qOje28VhtVcG2CaJmjrnHXI6YqcQ1VfIFJOGs3gfqlMlx_ky7ikL8yoqtUiSYtBqjxC2-NOuAsFnWMjkvBjRxPU5chCbVPJSyWbrkPGdPX3pWzA1mw4LPBoOzCRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uChVDEJ6pC9wFIgc7VXiRvPtJTKH1Bf2CqIsDu7HqTZeNX_SC6chvXFr0V6_gBVcX-WAgQym8tB2k38pvgvYqao4_g9PWp8q7SuBHmWDlBtifhSotll67Zyka5ywbWNbVfKTRFAEwoSliCduLxyJ0DMVlK1vtj16ceCxPxa-6U355RnpLGOv6jnbACaQYrIch28fyeW_5A-oEdBbIqDXui09dk8YckR6uOaf5ZQbOxsZOlZ86a_RggdZanQcyJk8jah2nqCOWMDEaXY35_KOBrpJL3rSeYL2zBjPbv_4W2jK6Pf7XO1joToCYTsUXrjx8cG9sOJGDqffpaeCAKsmjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpLKJ-JRgxL7d1hrymnmQLOuuKuzIcnviJC6ROvy59UJTCuNzzQX9F1tWBj5nN4Isv6sRH5Azq3Np95T3TBWm7iUsVDmvGOWaACRhrIk2IlvgLKCRjp8GFbh1g4oxPv5qMx_bK3r0hl-wu6LoucJ_E6S6OzWvJSfx_bjK0lJ0uwVuo4A9cqifZknExWGZ3JxJv76VxWn3i2JFa5DT7VZEE6JFW41jzoCwoS1U2qrkqtNcv1hZSeyRCANJcLSnaEEqOubWIbbdPkheqbLMcKUuDnNOim4rKUy3gmcjfeRicnqr-IW54FdFXHs4DIvLFdo02JbWsmpahEte0zmsae2zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lq21pF8jy-OgoNVrP8378FtcXvLtx1DhhJKJrQMKKiSUTZiftsFjetFiXPb4D_r-jxMV_Hk0g9_Ye_VQZQsMhfNcZVcoL2CRlLvdL5ogm17_eZfrHD_FiDa6u4vDbkTh9AcBHcmnkByi0IYcq1W0LrMgtkpg7LCql8cswyNh-x9uoFXCUDn8zrQmcxkLFjMeS_Ur7x1124Y_lWA6r8dfr6IRAlDf0TRGKRT6EFoAgYdNTjv4iNlc_hK9_lp4xT2v8xFjSvAcwweQYCBn63gAjQTVBYO37r8YMIPYidCnYP4Gp5qM0vaHSvbk7oNG4jJXzDdn3_pB6HBgtPtthVHElw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=R5qchZFIPrdnxYxubdTLTl2Z0v5UQBaQ50-wfZF2Ftjemre2V_b6qha-WixtPGJxbEZbp7jbcdN0bU7CY8-bOmijNS8MF5FRKykR9-MAqC_ZVe8h40HF_k5eNI1k7rcgVeOh6OmAlr7R3qzFXE7avQglunam-z_tOVhagUwfOAr9oZJSPWuaI5PuKzy4dQQCJddW1JO-TJAPoXzrgcov2xrOchfRebTBe-I7QVTpo9nYmnQTIablDchNf4Ii2Asx_2g0PhAgbEEmdrWHU_TLBU7IFdx2r2rTVZu7atmEucZDa4rDMXQUPCWFBEbSMYCJ_gTfx_ftwEb_JI7tGGdckw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=R5qchZFIPrdnxYxubdTLTl2Z0v5UQBaQ50-wfZF2Ftjemre2V_b6qha-WixtPGJxbEZbp7jbcdN0bU7CY8-bOmijNS8MF5FRKykR9-MAqC_ZVe8h40HF_k5eNI1k7rcgVeOh6OmAlr7R3qzFXE7avQglunam-z_tOVhagUwfOAr9oZJSPWuaI5PuKzy4dQQCJddW1JO-TJAPoXzrgcov2xrOchfRebTBe-I7QVTpo9nYmnQTIablDchNf4Ii2Asx_2g0PhAgbEEmdrWHU_TLBU7IFdx2r2rTVZu7atmEucZDa4rDMXQUPCWFBEbSMYCJ_gTfx_ftwEb_JI7tGGdckw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=ALDesw94uGTB6mkaBn1UmBfsSFuLRMPCAf9fa6vrYuHmANtTQgZ2zBLxilZk-m0VQpHqa1-AAJb7fL-udEu1xMgP_mxqnoTe1dZ679WUTB4M2fC1i5csRm5r6-NHP0N7kYz3Vf7l7uXjs67nJq86NY5LZjoUM3PMIHNHrYQ6nLBxqKkNl4eiyuygCcWiqshp5XHxGXf9tGU-PNpDsnbLVrdHi97O6eKKqBALOWjSONx6LbGACLc0dq1UKiFgDqZZBOr6R5VipiZUB1f0935rel7F0hb3GQZmIgs7-ZhTkpsVVd5HmKqhyMBXURWtCm8k2WxQC-JS0d3vLdF2-zYYWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=ALDesw94uGTB6mkaBn1UmBfsSFuLRMPCAf9fa6vrYuHmANtTQgZ2zBLxilZk-m0VQpHqa1-AAJb7fL-udEu1xMgP_mxqnoTe1dZ679WUTB4M2fC1i5csRm5r6-NHP0N7kYz3Vf7l7uXjs67nJq86NY5LZjoUM3PMIHNHrYQ6nLBxqKkNl4eiyuygCcWiqshp5XHxGXf9tGU-PNpDsnbLVrdHi97O6eKKqBALOWjSONx6LbGACLc0dq1UKiFgDqZZBOr6R5VipiZUB1f0935rel7F0hb3GQZmIgs7-ZhTkpsVVd5HmKqhyMBXURWtCm8k2WxQC-JS0d3vLdF2-zYYWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=XhEHHCZBDRb-EKhyPzmRkuOK5SnRsbGseKQa9SNw4-utQK4WY3rohxxCGS9vC5lgm78mKnXOQCeIYSQrqX5lyai0GVpUm1QboDM78ay_qenD3mLBzITnXFWGth3ynfXDJMGd8rPosMnV256CbgpMiNH89kUjC6GzxnoLqEBnVgECPFKJ3qca68gYsY6UXLYE5GIc46np5wyhF7-3wnf0Xp-YV9h63iyAS4-hyC-hSOUV7OZDXB2DuImLJI8i3I7pIZ4q_H74_JV1wvNtjLSNmOJeZwVsd_kdH-jGnBgl_OwjbQlehtMnm4qlsvhJFkdbY6GkuNyn0bO-vsbdhsBYgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=XhEHHCZBDRb-EKhyPzmRkuOK5SnRsbGseKQa9SNw4-utQK4WY3rohxxCGS9vC5lgm78mKnXOQCeIYSQrqX5lyai0GVpUm1QboDM78ay_qenD3mLBzITnXFWGth3ynfXDJMGd8rPosMnV256CbgpMiNH89kUjC6GzxnoLqEBnVgECPFKJ3qca68gYsY6UXLYE5GIc46np5wyhF7-3wnf0Xp-YV9h63iyAS4-hyC-hSOUV7OZDXB2DuImLJI8i3I7pIZ4q_H74_JV1wvNtjLSNmOJeZwVsd_kdH-jGnBgl_OwjbQlehtMnm4qlsvhJFkdbY6GkuNyn0bO-vsbdhsBYgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=vZkjbk2ZL-_5EZnHsZg9Mm6hBqZc6NousyRUFkS1qHObTnmBcGyvWfurhXb-R0Q-IQ8cHxGiV-K9M6VLiFz3sqaA4pWexlyFrI7nVlu-UGRxmFgqC9sT8kBQWNKRv0Fv42Jqo-U7MpKIYMb-SlB0mcnFesX2Wl_RQA4-AYl-hEShuhEQX-AsdNohHNdiX8c_QfJPr73JJ9pjO6IZS1OMbzyryAKCyqwxFTr4HWorGZF1AbHIwouO1DqeqzfiWNytpj-xc4ijHfRs-tFdgRhqBTAEtMxDjBK_L51pIFsyfLbZhxIf-SiGeW6a93IhPUPSlcVZfzK5myulBqYJhy9mhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=vZkjbk2ZL-_5EZnHsZg9Mm6hBqZc6NousyRUFkS1qHObTnmBcGyvWfurhXb-R0Q-IQ8cHxGiV-K9M6VLiFz3sqaA4pWexlyFrI7nVlu-UGRxmFgqC9sT8kBQWNKRv0Fv42Jqo-U7MpKIYMb-SlB0mcnFesX2Wl_RQA4-AYl-hEShuhEQX-AsdNohHNdiX8c_QfJPr73JJ9pjO6IZS1OMbzyryAKCyqwxFTr4HWorGZF1AbHIwouO1DqeqzfiWNytpj-xc4ijHfRs-tFdgRhqBTAEtMxDjBK_L51pIFsyfLbZhxIf-SiGeW6a93IhPUPSlcVZfzK5myulBqYJhy9mhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=kBdZC9LCuUHKZyD2fAj2WFozTzcfR78X8YzhQW033N4Lh4mT0_nGzWHSZz7TlTP8Rot4ZkLeMxL823VMGKkUlZj9Meg4hHUsxa2mnsi3WUD8qJzRnatfVXEuChOvmZrjeZidxt95TSO9mzNX8pEviuyyHB1oQ4w5ithlaBQcYL6yNQJ6KDGwZn3UeDgNYstX_AAP-CEjcI2F95jWWDjymVtd1xHziWusKpWchjmuqNprPYxEuosmdtOxBj_nfW1cRjpAouMdvn5fl4395kRMMth-18Jj_6aO7d4HwfYOWjsVwLkqKJLHCIbNxBSM_RfHqwQCd7pE2K03wVSq_VErRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=kBdZC9LCuUHKZyD2fAj2WFozTzcfR78X8YzhQW033N4Lh4mT0_nGzWHSZz7TlTP8Rot4ZkLeMxL823VMGKkUlZj9Meg4hHUsxa2mnsi3WUD8qJzRnatfVXEuChOvmZrjeZidxt95TSO9mzNX8pEviuyyHB1oQ4w5ithlaBQcYL6yNQJ6KDGwZn3UeDgNYstX_AAP-CEjcI2F95jWWDjymVtd1xHziWusKpWchjmuqNprPYxEuosmdtOxBj_nfW1cRjpAouMdvn5fl4395kRMMth-18Jj_6aO7d4HwfYOWjsVwLkqKJLHCIbNxBSM_RfHqwQCd7pE2K03wVSq_VErRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=aJ3vIrBUH08jLZMIrKAf932PBPP2_qJV1ZqK2SfbVpJ_-szcqDGmjVh-_QFMbPLrpMonIeTrl1kPaPAoq-KN_IhE_HsmBb6gqFEq3TOKzZkH6IMw9x8yeFdr3L7sVAKDo98ME_n_dY8i5dqFUIiLyojPidcIVUQ_PbLaMvwUgpn_LinhxnvNr1Wz9CGdC-kmIhB409JImqv4eQ9kZegQXa2-GKbDVi7yjnUedo7F6LqQnNqFXJk_2LNRr8Mhlc2t-_tSsKiXpRuwm0t6_1enpGZpuPAnKTBtxN2OvHIKpRjS7UnU44dhK6M2Uv0-Eg8NqMOh_NX8EsOWp333dYA1Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=aJ3vIrBUH08jLZMIrKAf932PBPP2_qJV1ZqK2SfbVpJ_-szcqDGmjVh-_QFMbPLrpMonIeTrl1kPaPAoq-KN_IhE_HsmBb6gqFEq3TOKzZkH6IMw9x8yeFdr3L7sVAKDo98ME_n_dY8i5dqFUIiLyojPidcIVUQ_PbLaMvwUgpn_LinhxnvNr1Wz9CGdC-kmIhB409JImqv4eQ9kZegQXa2-GKbDVi7yjnUedo7F6LqQnNqFXJk_2LNRr8Mhlc2t-_tSsKiXpRuwm0t6_1enpGZpuPAnKTBtxN2OvHIKpRjS7UnU44dhK6M2Uv0-Eg8NqMOh_NX8EsOWp333dYA1Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=HxGBNc1WOtXxvkxi8puYHHc8qhB9j999Db-bJjn0woxI7bkw4uKZI4bqXrv9gSIRTdQeG2OmKOSsXn3arl7x6eLGH98RTkqk0kOENAdB30Lr8sihFKaWLfdEzZL0zedUhCB4wgWSa1-RpRJ1kTdlGHC-XvAmu_8nCJtwfnU3Rxsrij71ExdPZiqZO1AkZU2qUINuyYIHa_TwClfT1_-ykDCkuroCO2DAu9CY3GJ_3qQ9GgdHBHY1ol4HOtU1qcyXW0fkozedhis4H0YL5HphflubsPZTA-nXA-9-IDGi3QH1HMYidohD2Bww2a3Hd9ZB2BkhLHq-q1mRfe2jmke68g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=HxGBNc1WOtXxvkxi8puYHHc8qhB9j999Db-bJjn0woxI7bkw4uKZI4bqXrv9gSIRTdQeG2OmKOSsXn3arl7x6eLGH98RTkqk0kOENAdB30Lr8sihFKaWLfdEzZL0zedUhCB4wgWSa1-RpRJ1kTdlGHC-XvAmu_8nCJtwfnU3Rxsrij71ExdPZiqZO1AkZU2qUINuyYIHa_TwClfT1_-ykDCkuroCO2DAu9CY3GJ_3qQ9GgdHBHY1ol4HOtU1qcyXW0fkozedhis4H0YL5HphflubsPZTA-nXA-9-IDGi3QH1HMYidohD2Bww2a3Hd9ZB2BkhLHq-q1mRfe2jmke68g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxWnjPojchN8KdH_4PB7NQYzBupccthR_uca0VeaGGLtci58L_3JBH8ycxbEPCJwq3kRwuZ82-YhUsjts1oWigSDOykIEMWAANnovpPuDo2iCIujRUI7OTGlZs9U-KcyXhC42xOdCFcn0w2oJ50VilFuNR89DA6-fZ9xwzSjaFKxcFCxxw8ny_aifGXEgdZsNN4sHkd735ilUux_6RbvxG5_kCuHY6hp5hVLA5TJIE9RKnaP8Pi5EzMifvLRHO7uHfGhX4iKapeOFQGBDvczg98OvYOifcveAnFncjertzXC2qLPYu2q-b9LdhmvENt8Eopds7zGeBLzrBl-FY44jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=VgEi4cs3m3sa66k8lPWCnUPfIS3UF8sA4WZlykyo-mJVFRqRzppueWqxmqQ9meN8l3NZ23MKqlp48dSrls6tWkRTqYL-96UQHpoR2znB-KHkABIfezK3f7tGR4LZj-CmgGpPi4UWZqCVQAFEBUA7x6C_nfxYXFqkk-uNM2oZ0N2CzIUKzc8SMvwDpPy3Ft34RYCTFKvxpaAeDpwXjq3lGfulPTe5XdTl5utwEuFSMZaSX1xbjGreFfWZ5Nop8j4Luql8S8AWaMR28Fz1eMjfRYM13trV4n8Gf0LYC1Y_kPnQzQxuA8UZ0aJZMAGV0jsqD-GrQzMVSFxLoRRnalMkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=VgEi4cs3m3sa66k8lPWCnUPfIS3UF8sA4WZlykyo-mJVFRqRzppueWqxmqQ9meN8l3NZ23MKqlp48dSrls6tWkRTqYL-96UQHpoR2znB-KHkABIfezK3f7tGR4LZj-CmgGpPi4UWZqCVQAFEBUA7x6C_nfxYXFqkk-uNM2oZ0N2CzIUKzc8SMvwDpPy3Ft34RYCTFKvxpaAeDpwXjq3lGfulPTe5XdTl5utwEuFSMZaSX1xbjGreFfWZ5Nop8j4Luql8S8AWaMR28Fz1eMjfRYM13trV4n8Gf0LYC1Y_kPnQzQxuA8UZ0aJZMAGV0jsqD-GrQzMVSFxLoRRnalMkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-1rgdi2zfDrbubMZTCVDrYVfXdfB-Pvt6w4gWv3DJOPJOY2-3eyIeyCDtN-g3e_vhQLBnj2hAFXQEuVtZxMNJ1tml2lQkwehDiDAq_foNNINL66uhuo9ts-pUqhCA5SJ4a2OpT07P_ntoggyRxxglpJTKGNNva3Hz52espmbLyCgo_yks-MSeTvMVNF4xd_KMj8hMk3dqlLbU6UxU9QCRCtNTe87gYyXjxs-wFJUHOYNiiPyiPb_wOQdyVZf_p6K3_8-SlKAZ55_uAQR_-oZLEaTAS0iamF6Urd58xFJ7yR-XLnCFIaFaJiFGbfvCdKV_pZUnN4cVwklsBknZI2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
