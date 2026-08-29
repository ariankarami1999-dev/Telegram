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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 01:20:26</div>
<hr>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=rNo0xs4gGWzGryPgjMywJGGn22SRNvSmRo86fsfZx5QH1GtDjq7EfxpvzbBJNpfQgjZbu4Vaw2Ln9UYCq0ztVIxD6piDMbeuFgDw7rc54Q8WpMnB1C9g3uXhii4TWtWDIF2qHGnq6_thASoTdiEieICJLQuu3Wi4P8wD2ritFVSiWyFPaEaeuHh9Eid00WEvHE_PeusY4dzhF5x8xJCJwGbMmvUvCLRKqF9vDO5NaC4h20ds_SZ50FZMuRY5InPS3P8ku-JX55PClTDvUdetuz1c4GRMg_SwcaHKC-bOlMRAS83jtOApItEA5vLGUCRyQFnHUY5tO4GrmI-MOlPHYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=rNo0xs4gGWzGryPgjMywJGGn22SRNvSmRo86fsfZx5QH1GtDjq7EfxpvzbBJNpfQgjZbu4Vaw2Ln9UYCq0ztVIxD6piDMbeuFgDw7rc54Q8WpMnB1C9g3uXhii4TWtWDIF2qHGnq6_thASoTdiEieICJLQuu3Wi4P8wD2ritFVSiWyFPaEaeuHh9Eid00WEvHE_PeusY4dzhF5x8xJCJwGbMmvUvCLRKqF9vDO5NaC4h20ds_SZ50FZMuRY5InPS3P8ku-JX55PClTDvUdetuz1c4GRMg_SwcaHKC-bOlMRAS83jtOApItEA5vLGUCRyQFnHUY5tO4GrmI-MOlPHYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvOB1IeD3SUtPGb19zePxNyYV_jJe7h9FCegjKKDeNtWsy2qEGK28kBoO_tH-Yi6c7ooELBtGC6hY4jgyJVsg5QkhRjWu30b2KI5VHIKppHm6TG1ysBv7RLymgjLTtD_aJ3FU2OHbwsnllNowkqHQ-Kw8ten9Aur40RH0mX3vfoPfwWrRFs2NxNVpdpdsR3GmlMOrP9Q3bnsMvemM_4-KPHoOoE_db7CfiIFikVIsFNLNpQzvBao6jE_1U6Amt1meLfh9ZSg30SQ1mm_c-4v2RC-FZvakCbvynxFTzG9uacYfOgkPuEQnZ8dwf4RdZQtoe0PCc6RcFGzNF3O5HzHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppdWci7ZnA-2IRuJiqgorxBppJ_u99YOeCWe5tic5pKks_PnaUuyrFvFu-Mfb4hhen-HF90IgXM0WevkchVe06wml_VbzvFM3Hj1vJXuwOsNpn9nLeWDMQhxtTVK7JuUDocUBCrZrC2t9SYDC8pz5FgnmLZFNqvUHSiOLVysmQrxctESXa3P1bk6Fwf0U0_zMVgJD4TGjwonnzGR1kL68ljQqAgZfpGYy_AWM3CPk1c1L50SHHBAvhXE59DeJNDJYiCB_z1oIupj3YCQFjATfnDaS83iV8p_aEGrPDSijCHkS_LXAggypfJApJeKzkWEaJx-veBbRZdaLBSqXjLFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHugfv0kSBOsWiUvMHMvkbVhWUqXemM0MrU5lYWO9tA8YoLnzK28on8ciJD7kWWc-xXcSgZ_SZ6fsCrPbLC75Pj1692RW_RgN14T7TFVWiNUtt1g-Q-pTzR_C_lan6hzCq1tAQkjEUDTZnSz5vdj7QEv5qm-_Mr73IfAmKe8gouo1WICGe3F3YEz6NqUzITRg65RfigKtXPB4XRdU4KIsJgB795iJ9AVCow7AVzzosKucb8YKjkSOPOYCAgquEmZvlZYwNf1aMmWaq5wNb5U1nTnrQvzJp3lh5vfo7F_gBkWm6Lt5k3EODPI9jhRFDEuR_fAjnDhHOQ2OGjnTZQDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK3pISSKeb709ekPyaCs3xRd57_sR6AE09qWFpfB3zOkPXDPEJ10deQhA5jwPGGW-i8X-X3Gcxj49_L5DDebDggmg3WKDBNGOMMXDcbekL5tl5YhBAYwjg4sibAYByE-85p3loeKpCJ2S5YNrOFYsUMAtibwd57HBMEx-SZ6nK9l0b3R-M9-yrW_Qa8Kv-8J8IVU5VLOH_V1ikwNpbuiTXqKTN7X4St1VEwwPXdwKGzFUDF40M6Wm8--GYJD2DlIK2Djt5vyG6CODZF1mbEkahAW_BpKwR7Ozra6A1Ynx7sMaD3cpcJVy-iXA66EYjQDSWpdTdfhLaUQgVUnqtM4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F873Dd8hbgzzwogMZROePk5VNqAyQxOmaXa0wPpGX8MCNctDRvtCCqBxNQ0QBaIxWb-ls0H0v2cgJaqZTD_BKa2SSu7Eg4j5RBFEy46EYkr6vRZzas51QpzgoLNbouaQD30VHmXUOBv6-sLenEkcBa1qXWnu_N1WLw5W2E3S2ZZiA-yuuBFGW8Bao8rWnVdRAOT5C4FBLhX3dHzelPGdAFZqvZtxc7tZFuD3FblTyKgPn1Hz0x87-qvQ89CGPQNOwUIGBAOc1Ift9ZUipLLERwqAH89ZWHIWPJIXFpUJ0ixWmL8zsOr70wRTf-TwzHo9TCJMw3xhgw80ZcD8CJgrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iuygkne37eKpEPiEu0fgBw2tXEq5arRjgGWK2OUpiQNoD_NJQtgzZivRDqZbabzUTPLmMPKYiG1LA8AjmnO3RaHIi4EPA3uOmNnWD-5v8ZeJLKWdeiQv2WusTt6o_YIa9Y9l2cgLTgzQLZbapBldc2sum8VyB_j_O4dLcMHhQHxK4gBrdBOf08jveLhWQN6nTsW1zPRABDV9A_8wG7n76CUhSiP8NbAvXgQRpD-hHOwK4Jwy_fks8glTTawaPdI6TTW3lWnrvjSaYvgItHsubjTbBGlla7-vPqvt6_3RC0vAHgHNWs4fy8pPwj26hFP2mGLNjc2RL39yOkthCnAoFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYbIMjOmfnL4bpCbd7hgKO9RAhwcp2hHn7-rCA7iWcSVsCbutMeQe5DcjIEeV7PQv93hmkEZRJZRRJI0O7ah2G3jeLV-9AJ7RPR0E7uKaeeIrZqMNxnYSjnOkqqfJKd-XXAYpsmU7wmTnegB0iZPH5ttsiKbvX_3hrD3Zp2vAZ88NRBnmzD5D8A5ItOJJn2FeJOfdvmi_zrFETooP5k0bwDpGvWSAoSPIczCEtErMMkV-tBBXJTXqNFM2a6CHfArhp6TcyNy1JjLIMkaULUO8N_a7liWqZNtnGfy2O1sYqguuRijDLNJf0dooFGx0CJs3Rv9rmSNMBc6JwW2TgJfzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky7xm14Vok8rZRnCbKCq5kQEQqMPRedNfi0Pucj9AoyB4Gs0LBiLCawMbesjXW70n9bxdPWdkIYOzW8LIWs8D0Hkp2h40TxvaN4_UqQyIVfsoEvpPs7GdyGir8duomqWx1eDmnXvxq7eKmJ0A7iA6Wq4qjN25_PUg0biy67p5JUmrWaQWBMJpxtL2Nl5oHuE_Bt-txIAD02HKvJ8L2d_KFFlYl9lU2frMrfIdCvgpw7ntkOMwIacwe7EDD6nhhzZmavoF5Lq5NdsRlGQdTpq7cYG0jqfjhnjKCX8xsJobLZrDjiKYdKykg15bTUEQW1BdP8_5IBPXu11Q4lN5JJdwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=PmQaGNdQYi4AIuXxDI9f04IfA04X_5yOs7riHKrvztTACYxqd8A9bzcbmSb9vMj-ecQtE8JdpspG4Icj-vnz1DLjKFEya22TVEZy15lM_nPpKUUXqq56CXxWu6AMmO0WCfqnn0nR8qh4LSl4amjb4iZOvBSb8Cic8wSwWmGPtU3my5XjDzq-P20YY7psSNyuTBZ7nteRJiQMCfHRSM2rdAneILFoHoIm4pW7IpYMdb5ADMuDFgp54uBnHh1ZkqrqWqhaNFIqBIn_qTfNrjx1I57KIQ8hQCLPaqi1_RH8zcHoM_JqXwvdGBGlm8CiG4ds2KguKk4OQ_UZ6UxivEyX0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=PmQaGNdQYi4AIuXxDI9f04IfA04X_5yOs7riHKrvztTACYxqd8A9bzcbmSb9vMj-ecQtE8JdpspG4Icj-vnz1DLjKFEya22TVEZy15lM_nPpKUUXqq56CXxWu6AMmO0WCfqnn0nR8qh4LSl4amjb4iZOvBSb8Cic8wSwWmGPtU3my5XjDzq-P20YY7psSNyuTBZ7nteRJiQMCfHRSM2rdAneILFoHoIm4pW7IpYMdb5ADMuDFgp54uBnHh1ZkqrqWqhaNFIqBIn_qTfNrjx1I57KIQ8hQCLPaqi1_RH8zcHoM_JqXwvdGBGlm8CiG4ds2KguKk4OQ_UZ6UxivEyX0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM16KEgGeB0kEieNc9w3iawjSudD4wQtVCYDfBLz98yaypR2TDGdv_-Xy4NoV0vxV36qYpwjt5jIod8wRvtwX9MiazCGXdeWa-04Wyts9bM1RELv7W6OtNlPON29768UMV8UkqEUwPO9Lzpq7qScGeUm7c9WyD06aWVlhODwEnNcX7IngBUKMYB1Ru8B22xJhqHDffbbfdYLYlzHHq3b6Jdwdxb6HP6tsvpBvI9Z1smb8V05P_AWiMHNR90Z19Vrmatd4BnnWQwNc3s58QFmjynnUFFsa8hKWf_LK87ax1JsLnDRH7GowZLWdohH7bW_wXk9MVunZ4xSadrwpW5OBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=H4llj79WkX7vTV7QaSDCNInGm-nn_m2eSuejW4o4phfekM765pXKdZTKWrUHw4gNlsJMqMcMz8hPDQ5_gJXwqRddYPYpbAJZ59RGaiFP6H7lRk0TAZyW2My-dxDCbESGBT4cZPHOaVE58j_XA7ZWrDN8abZT4bm9PNAeaIrHRGxUZo5EX7_n82mNaOjqRgpstXWhk0zp5ML5ajLuSmV2_PNew8TnR42PLwCceZqrWAH8Hi0wxuqH2yJvJffEevebNxnBaiHYHXUdtvzOPrC2YtlcU1JpbZfIuXaiW5Z9armnH5dgEx1DEz4RsXl4itewATLkw4f_Yhkyvgy9peQhnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=H4llj79WkX7vTV7QaSDCNInGm-nn_m2eSuejW4o4phfekM765pXKdZTKWrUHw4gNlsJMqMcMz8hPDQ5_gJXwqRddYPYpbAJZ59RGaiFP6H7lRk0TAZyW2My-dxDCbESGBT4cZPHOaVE58j_XA7ZWrDN8abZT4bm9PNAeaIrHRGxUZo5EX7_n82mNaOjqRgpstXWhk0zp5ML5ajLuSmV2_PNew8TnR42PLwCceZqrWAH8Hi0wxuqH2yJvJffEevebNxnBaiHYHXUdtvzOPrC2YtlcU1JpbZfIuXaiW5Z9armnH5dgEx1DEz4RsXl4itewATLkw4f_Yhkyvgy9peQhnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=XZQZZN4czX2ug5U8RifUqG4Oe-z4tmKE8PunMuwq-s6w1aDkCKmkWux6eXIUwr1ZHoeTl50Ag_vzNGtOPYJ1GHsaW6i3HdVmmmUj9PcWKgt-I9dWweXEUcAvJ7W70dlyRzmtXHWV8KwYiYtEev6SoKQJGjActNZFPicKbBAjAyj4HTIo6mmE653Yh1D505lmw421dbaxtBhrv9IEW8_wDQZpp4JJR0BGJheq-L9fUXKKODAM_AHHaJMRfM3UJJf21NiCEXKtdtAySamRMhCp-4XuHKc7p0b0VLvge3TAiFTecFMRxTsVUDb0_bN0EsloMm4FnXJnmeqzYsmq1Rq4vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=XZQZZN4czX2ug5U8RifUqG4Oe-z4tmKE8PunMuwq-s6w1aDkCKmkWux6eXIUwr1ZHoeTl50Ag_vzNGtOPYJ1GHsaW6i3HdVmmmUj9PcWKgt-I9dWweXEUcAvJ7W70dlyRzmtXHWV8KwYiYtEev6SoKQJGjActNZFPicKbBAjAyj4HTIo6mmE653Yh1D505lmw421dbaxtBhrv9IEW8_wDQZpp4JJR0BGJheq-L9fUXKKODAM_AHHaJMRfM3UJJf21NiCEXKtdtAySamRMhCp-4XuHKc7p0b0VLvge3TAiFTecFMRxTsVUDb0_bN0EsloMm4FnXJnmeqzYsmq1Rq4vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvJ-if4jPeOAWCfCGOS5T-vghyh2b9DmjI434UCdTfYW3pp3Uv4zsoMmkGJpWqq2E4vFQbanccF-8g9qT-20v4R1sJnd4-_tu2Aj3SQcafLhUMP8rnmKUz9Jb0v_iOcO0_qo-SZLiNjVRZZhjp63acx_ARNAYgEvp6GB59ueH4WJJr07QM_1yDObMWVBmQbn5ssgCSEDHq6DIIT4XeFn_OVPFVCPTgaLBb7Fnq93DOmAoP4iWrYCQqHDErwRTSOaJnbCkMMNsfwWtdtwWWX23Q5GF9CXOalcQg8p6nIjlCaiLpYZLUvFwU6GiKovmURF7XdH0iPVlubwW7v0_fgzqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTJK_0JW7UG_-Ts6eMpfUSm-4uPbuKn2KnRtY00p2U9BIZyZoCYJYVu_rQHwr6oRR7dbNKGnIR3OFbN74xR2VXtvGiwR40jgfJq3scNqyrpGgn9hYm_UOuLoywOGqk22SbLt8oOqGStzW20-nz6ctCUdJMGcDflNiw_IjWGkcLJ8Bccc3VUbIZnJPoRkwz2zfw_AcICo3wsbRMSomLcHq8SIJ82jReN9F1BDD0j0xcjTPnJAj0O0BGt_BM55zZ3xMFK0QNSqrv9g6rsXbPydQ5bCwAfEgg1S0ae2vKTNfQGKsKAKfAdA6WcCDNTg4rciL03KwuPgCX9bnq7G9KL_Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=IIWLWaWGvSUcvgi0ZIA1YVy6FO0EgT7cT9qbXzm2_-4Dgom6A-lSkr0EVIapOk0Q7bbgJsY1HOp5kvb6EKhD2aR7Yck7hr0zZKAgA5asbXpaFe_bo9DuK6dyZXsBwSdTmPVbXBcj7nY5KqkNGG8IQpHuZF5_Uqfic70iKukJmdk5-vbdJzQ9y610-LwWLMJd3eQ4h4K866hMei8UoOWEqU2hm1YmNDMSZ3W38Fm-K93rpfyMXuGJXiG50AXk-woveITT7ExFMjUHwe2AD6U2yVmR5MnfPfaU-d-jlUvf2tD7FCnnFQ1oOMcP_JEgM5M7ScnbUoTqx24xBa9N7w_dux2rz5bmyFbsnkry7LjtuKGt3cjzeM1aHsx_dmEiFxlQkWdwq3GInIO5S5pVX4lwus-XWI6SFZzVhbGsL2lWZTtvpV23wYVYPIaNQ1dlKsdyBR1OeP2sz-iiZSjhtO19VEvjkZRijlhlyflbPIfp_GiMGgliOzc6bdguNTZEK5Wvxm1F9_UrSxGMTvOCt26jtUfuEZUaP4-L5OlDGmHq7jio2mU_ykDIXQZOJwetLYx2DShc_VWeajtgw-NBFwq_jgL_-B4FQ_1GfDooyREbcwm8bxgljYqVaH_njTKHVI7ImB_DlBjxVx8f-QiCu7pGMMakbGvzMeg0J5DG4O18HL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=IIWLWaWGvSUcvgi0ZIA1YVy6FO0EgT7cT9qbXzm2_-4Dgom6A-lSkr0EVIapOk0Q7bbgJsY1HOp5kvb6EKhD2aR7Yck7hr0zZKAgA5asbXpaFe_bo9DuK6dyZXsBwSdTmPVbXBcj7nY5KqkNGG8IQpHuZF5_Uqfic70iKukJmdk5-vbdJzQ9y610-LwWLMJd3eQ4h4K866hMei8UoOWEqU2hm1YmNDMSZ3W38Fm-K93rpfyMXuGJXiG50AXk-woveITT7ExFMjUHwe2AD6U2yVmR5MnfPfaU-d-jlUvf2tD7FCnnFQ1oOMcP_JEgM5M7ScnbUoTqx24xBa9N7w_dux2rz5bmyFbsnkry7LjtuKGt3cjzeM1aHsx_dmEiFxlQkWdwq3GInIO5S5pVX4lwus-XWI6SFZzVhbGsL2lWZTtvpV23wYVYPIaNQ1dlKsdyBR1OeP2sz-iiZSjhtO19VEvjkZRijlhlyflbPIfp_GiMGgliOzc6bdguNTZEK5Wvxm1F9_UrSxGMTvOCt26jtUfuEZUaP4-L5OlDGmHq7jio2mU_ykDIXQZOJwetLYx2DShc_VWeajtgw-NBFwq_jgL_-B4FQ_1GfDooyREbcwm8bxgljYqVaH_njTKHVI7ImB_DlBjxVx8f-QiCu7pGMMakbGvzMeg0J5DG4O18HL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfxfibbjEleMVjc4uXFCSuAiDCNCNlAHUmaEs5nvHqVsmi6s-ZfMahRIjhKr-cDI8g0_r7JETbZxw4TP1LCZy6Q6vzdyr1QIkt7AxkmiglFCOtaMdrqQ3zqvb6K-8xsfVuM6X-MzPRWSkqz4KG3Sr6aIrm7ozZetCBFgaw4seAK8dKJOy71GM_JBwJ66dyXPxQtui7PlHlGeQGN0_hUFe8ZP80ouGlJDnk_WGNOG_wyGuQn5lBcLZMwnIYyS59F4Gz_l8CGg9Pt7CZlnVRKYoegbr_AA3q75fEmjbewl0RrbLEEGqLuhAJ4wtKzZAhBvqptDpObffrlvyt2WMecxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGOI_vO-HFodMQiAlcoh_48qkjqUzPAGIfNfR0tNNFdKL_3m2nHssE3uYRuo215wmG7Ft0LA5Px3mPTHpkNi7-YUB8EyZj3GkjrezKBkj7F-tobya7PFtknckf6Wa-2i_uv5tHIJJYX4kUoPCLOUw9L_-2af_fUTX4Aisnq4ot2q3E3jddimMLc2uqjyTM6hYaSPQ_ioeCdH8z4i6fNM-IwD6VjUwle3VgV0u07DohkhE3OQAwI2ZEfWSPZ7nGAqYyARVQWBbml-npUjp2rb8oJ0Ki971pw1BsnGEfuQQ9ia_Kj2wHFXb7Lm5CzrnAQ3u_kcydRVkrYcidbhijpJGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCrDQC-sI95pWc2PgusDqHHWvAcdoYbqGQVj-GtYIx_mJbFNUoJPb8iz-JunkxjNal6YkeytDeMmQfk8P6UBYk6oSoqnU5BAcdnjd_padC2NZ9rLzbAAKSmPy89iVl6mFW9_vdLkYjaeOgcFUfLrvpv_TtOJg481w4HWGDmx9ho3XU_1e-eWBD17MIyIBj1CZS-n0D9hgZn7M2JNZDbAWHkSIJUxHSBzzf-bHuoAQeSPlfKQqCHTqKbhGxulHhKMP2zshtG-_d-Vf2QcIfcT5nmljeKxYYgPWBYF83XPR7acVJGa6qFPk59bdDpHS5KFgwFir7Up4W-cz8rGzw5uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRIgoaUjZSEQYw8k2P1w0RgZMMtCEv3JT5w9fvD_wS3h3spaAEHYzuSWikp7WDtNTfPichQ0iveV8ZI4ytC39E3niwYS819eFxz6bh4axMCTXJ2BrwGXgldzytzjbhafWP2RDu0zFjy7d9fOqXgshxSpUNAdo5u58QFuQWr3JjnNY1Iq8vAL3VCMI9ruiu3KoSBrUnIK57OZE5UJTL8YrjPbV5jQd-COIcFgNRRwrflpJZDAnb0dijKx8ic7V5FG_Cya2oKGFbpgQuIfmnFU5r3vIXM6zSlzw9aIHNopXUDFEoLu0wSktcFgW1NRuZzqg5gzMSTMwmqoG307ukUz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeJmIx8frarJEV5_RQ63ftbyl7hySAY0sLfdV9dKf_HwR0Vs8Lks44vvcsYFZbp4O3YDlvd6XN0E2W06IEFqtLw0_b-UuGUysf77fZIOy6hMW6IhCkmriCRxZR18sCPCFf_LPt3QqyO3MntsiPAcM8rY8xDAPUkObZ9ufNzSgqIYxFzn3thYD3hYeMHovZvjSpZBajUTKHouxRbsIcDSDir43btN01T-E0eg0A8B5HExEENKT1nm37bWO5imS4-r4Hp8w-axfFDmU7b4Na5a6DwrPW-Wbd5g19shLROmZ21EwZZgzoT6nAmAjhQSHyAv9sfxfH8RCVKwV7vUHy0qEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gpe65NaT8PVtBDMcZhTr7Nqs4e6lljAZwp2J_Ziujong4IskQyL-whYKrbHnQU6bnNtUH-_wR8itTCQlf014PtUP7JTzGRPcJL2XiHBZN6yM-ZZCmz6q4f1yyHaXQP1iitIeo7U8KT568j8Nh1SxFLf5O703mqaM73Ia3Y41bg0k34g-AbgXAuN_OdswccS57ZH-ovBTizSevNYuTUl2RORv8ME7tstyjm6mzssOvWIffz4yCTUj94_ibW2D-JakvfLdhdZAezsHrVZb8fTjbr1ZZOlCtF4p_K00ZURclN1sasCqUM6JNj7joCALbMxIPVCluA0t6xehea26lrAxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcxdQ93vJMoXVtMebdnHwMloVG4IktKDPc-sdcxi8c49w6zveX6EeIZ1ddmlyc19EnCc3EV3SEyy0sjAgfaBMFC2ch8HkQPTjyye6Z7YhhZn6itCiJBnqpPTV1SVcmcwW4WdLw42WTOodw4bnkQg1vysL30b-2PKYOb2fkfON88aSHgwdRObwXLdl3X3098-u-Bjv_AhwhJidav3lnUza_f1GrrFtPytIu7ykAz-4xkikLctrx6BfZ14wgK25fD9yQa6clsdx7Ak07SsolLjEBGKidjH_L8vM9yWVk3f6takSejdvRabJh3FU18hLYqrNBl9x3E_yEOktK7RqO1IWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6hL8hjmpyeH47r_rRN3NjZKZiwRlj1RWO42JR9X1X_F90LX82He_vN0AzI9o9AYftOgDNYHJigs3mdHGOFZ2U6vnH9mS8c29ZLMl7qfOYECy_BIjkCy8rxqsIJKxtoUIbtcpO905LBnKq4KhLrJ16TQxTNW-WZVsOyqjW3JKLWrULxoDFCeVU0ppLMwDEgbViIqoinP7hQkOrVuXE3hKBIF0m4CWhgn5V_o3Ew6M61QN71VjJuUhF12DrwQHVYBl0sEfZ7qAbpD36NEY-ocHJfV3rz8WfeghjDyfxmqJjxyKi-bL0OsS2m-DoklRAPvE0kLll3jqX1f4WGH5RGyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2nW5gCr4C7QsBqrs4PptbQQcVDlkAacbRgeQ1qLCT1E_L4t3yA7ClkrztTMOd3G36qioguIuB7jmN7qZr-uu_gmywsVAgod9hDlIdiViIxVCjxD7IcRICoyvfUVtbnc3dWshsTsSqDb0QLyacfjrV34Mqxur9O5cdSm_3HtC52ItoVSN16vTe45sHkLZT9r4nqboZKJWxGMWHCQRPADNrBDp3NqnIKLshc8q4BdSvjWRSRhhpheKgZXYhBGlXilRoSQVpvJ4aTjATB4yzwr5aAkTmHhVcQEExCgmycQqU8B0CR8uaZEGlgG_cUZhIoTAYaz7jrobSXI_DjXAmaKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7xrUwOk5vcyJQfNPO7-6wHjXS66sBi8LZwKxTdgzgLq32bicpM4uSLD6lXZb8EaksvXdnykWZR-36RxZJkD6k9upJh4Doi3Hh4mtft7r3t50Dt9QHqU__smCJg156ZmdCoR7PTlDYziOkXv9HfCPok8MuIhVMmZAYYE2xqdXrlrqVCuc9JRi68Bag6hXQyqHlRbu57ryYKR-GKJTOyoXWX2lSsjdifurysSF2FDT89FL68uQCJQrNMbgHNoPoJZt-pjmckjMZJUfcsgiNTd6majXcskOZy91OmEQekX-BfQ4f14U_P4jlIyU-tquEEXmdJum9numaLWAVElMwT9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZDu_icODeNHKfb0wUGB4pCprTlZOQ1YAOTjazcjgCUr6VwjRSE4Vabn3eyCn42LD495bCrVHXholVeOXNXQDTT-9cYXad_vhvfzgEAHi5V4M00OO2O52mZsylRDFXhW6nUZu4Aqvzu7MEuH6AAoUkmiOxzyn88xUkbkZF4Y8KHbEvgM9FsoQxBLRoQdX1pPWYGP2EBdUsQIe7yEjiuQrqknagK6KTUD_61q61K_LeiVvBWRzFWfV-rwW3t3iHnYnE9Cnk_i8EjRYNHhN_88Sg3sAakm01bhomRwQ3Ix_jMLSNacPkKJU8V9cyXj8WG28s1mjdinHPdm0tmkCQrsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYR3v2q410ctEOS-vORrCNNgffOuEE7TbIGbnG7jj3b_NdYM5aDt5T7iLIWWODVMSJVD3EUciEu25y_S4hnEta6J3jsqgfyIs45opjYEPkG_uzsiewEOWFNNhWXud0t14ptG_0wGcLVycCMdroRiloaQMtwxDw_OlA6SNv9dDZxfbyFuPWDc-e_sxqoVHbcEhywDwfDth2Napkg3aTl7DCkf4H_-kwtjsyumXyM5m5AxR36L5Rh4sa-PCjp6fyRSyruBLwAcVWTD3YbYB8UBP5h_Elhr7wLXgCWS_05oLIJwVnPaqmt3zQ_AUOdIEZTQ2tc5tI7Cm5DtAh74YF0o6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVbKx4WhEqZ1xLFxngj3z7TciiyYeY-46e5heAOkHfBJPftsgYR_jqEZSCNrPNaBuTZbNlsuBNLN6xF1MFi5wyveEq8PWBiqsYAQT41hPOE7JfuXfBrdrsQHnIZlRYmJ1OzaAIPv6Iw5xzbxBcBhAI-TYtoR17rXT_9d3_hUxir8RCiWuOpgXLAFKQj5QXvjC3kYWvnrHDzBxBQcQ6J17GQcwYUBhTkv0zU5ipOxldlCcNY8xbolUVaJy8PeHmgo34T50G2xHpPVGNCmwk581nOhuNjrdfj1pJ2u5JMTdnP5qERKxpBl9sBNefeRUuu2lZ1kYULgQe-QqLosGC9__w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJTPocax3x1Mtdj4efk-aMrCuGMAHXNlGc39joPmEqrrmH2AWgbcWmz4O054pHjK37nnFevn00FaQnwsh3Xbgfhxt5HYzFFbfAoJ9FKT2UbanHZV4ckKSYO6miNDq4pNq6ciS64jc3Xgu75c4Y2meoPny0qKDQdWZxqCeEJxJeoqDe2JZvgq1Q_C_KZRmtn-vTwPieIEUV87pbw4y8_k8IGciYtGRXGjf3YYcxb3XgaiOMNGsq7jSFs5k3Wk48uCgupiOv9nltYjFw6U7379nLNsuKVp9d83kpyie7P4fc_AKGh1YscedTC5RtcGKG6bQbkhcuVHb6xxNfxbghOgaQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xc_yi1PcQ9g9dNVI-noxzKJ78XFxJH0khs_FtHWqyWb1q0QjxGNp9eTCjc12_wb2JiHnGqtoPC4qcMya4YY8Gvt5hKcykJ5A44Gn3G335VXco9nt7Mx01PawgDP3lgCpY14JM9-eOJe1azAo1-9tfVGVsjzaxTSLhS0iX4gL3Zp7cwW_fJdSRzbt5-68A-PowgEI4S1IWKgmHvZ-3b3MNKOmGBN_YiXdnXWLsLVbvDWw3JoPPsYk0SmkJIpX-VeS_Yz1Pxwiy2ew64DzdB6z5K1Wec6TCIlbMUoTaxACIhygLv4e4zBWQ8MvqVFz15qtF_RO84_hACbjw5FhjzonRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5tP0HjpKENAq4GNX_WD03cW3mXEdJoKd2Ha2ETTDxjYyC_AA3bzO6kSqsN3pdIqsvbvOPTMvNsyly8CTuy2Ft66dcSy0-uRdGQaBaRep683sE8LkibawUoO1kEy4E2Mcqz6ywoZzafO5fVdipV-yYvSgDjAALfEu9a7Gk0bTDUpJd2gP_QFMJ63d-ykGWynb6TAb9CEyXVWul8LzDwXiUFlDi8lGgDSmIntIDAGExI7uvSIhhlshBm9GMGdyZIyj_XUFTWkx8wCAxJRcvBZsfkV0fdxtG_9xW1EcdlURzCEuCHKsG9VlHjT91X8Yw2ajrYz4_zYZIh3ujAHbojGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAsl40RdbH5V7PqVlpRQnDNFB7ePzFgBxtpHfgRkEhyUQQn8FgVRCoxPrDkrflrrdzNwGlZdYG2GbWoYKUF8CmXsJ2MdrnHr2NOzc5dkmh9jWOGh8TnIaQ6UQgVisBdn6qxQHCMszIyBK1pI2i9dJWcKiKAHHuxkNyGSJrCbUY37hhNbtpXPW3twVdKZtoqh711AQZOzqi8z_SwesQK3plMdvidxEKs3Dz7edKH2Ut3DpCuSETuqaPHRoKrKh5wvfNJI7ySav_baltYlNabGvfVYnYC9Md8QPbzifwRGbZgmrMEs_7fbP64GghEKdboUZOzoLtwsIsNlBA1XTFt4GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7hNmHb8-Qw68c8oNTfm8NiMHfaiLC-3QljKnwmTGXdyESbEO9p6LIsEyv8ZENI1cq5m2-uTfOmB41_ynrFUJSF2LJOxi9kYYDGC1ZWuyEXrYZ3qak99GbUxjVwO7sqLEkrTBT66yOW7F7krc8rwz-n85XhiW3_IjcpAUf-MZtAP22s4ao8BB6HxxFELS1JklIKO2davYxhVyOUMK9wgQE8lNJ8h1pmRewEIV7amXiuPfRYvcI1q6l0Swb17r6c-skmGxbAvb3F_w9IWjs3lhTGLtScpvWRCchTFhcQObBj8jFkqdwaviy0cvGTptRgEKLQSPYG6jQ9g2Encp_-JLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebhVV9Cns_Zdn_mL5_ix7tevYZ_c1eAsbjXpOTgsdidufSeiw9r106hvBJM556r8U6hQhMbO6SOForhWENrf_9qxqJ0qDH3Q5n6077rgVty0BCpm6khVzGH2_zOFLSV4JPw_OK42dwRrt87EpIBpbVH1J7TSl3AEA-qmAFbPxpPj4utM_66xYDbvzzU77XvHTzeaEvKiKf6dwMkui7XCplvQbEjmp9uvERIuq4_9sG_FdFryA1EQmpvCu206uVgBYPxbEE_ECD3EMTLKIo_U4j4K5vvAYCjCN6AUjl5E4fWvgJcUy6KmWPY2uUDBzEF3jT3XbV6uxVinBuG5PcIp3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrX8HjYkhWWF0LUQV3L_l8zr6S5R9sXWN90sS-1YstxnrZwLFGSlmDHs4sZxLs-YvNSIMCq3WXuTKIuCA7BYzAqgEpdi53oI2k1DNl6a89GI9Pa7Hc0hpOcO5-rYvnQkW_5RkGQqklFxPOpOYROGocn5IyNpMdW9fuWh3s5lob5hRGO1K5toYLJAB7JZEocJFd167B1RQ-ExIpd7kuAPonR07aaeskjtmgXrOwOUNvlEgZ_OjRXQARubqzm0vNY0VO_Nl5YZanL5T7wfFpf_H_P-l9Bd_FqBH9G69MwAZVRnpcf7HRA_mGBogoi94lysnhkNCSMweJWYKjQ9L_qR1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJFdPr70s-eSenPxK-QvtAzKtKT882bTVA9wkNgehRrujx7R7TxLpXBXcZRuR_69OPppGIFiN7RHd-NPqgCeTX--BkpX9VO7XEyjzsPzsTDp0lTii_grOJqQU1Ox5FZdIa2W615FD160-D4CCIvcSZ5ld-2ParTUoW1Hu43kUf0ZsnOWXVfNRaSrx0k7tZCZ4yjQ52tsfZ26kLzXVhRWFutjM0Wq8fdzTErJO08wFelWWAmXWlxo66bHz04O0OD-XLLee1llwJwQ1nAQYSnjVdXgb6L8369MWS9nPNu737l7XRZhRyems5Ox8XlP-xdqkIF2_85506f0LHALRKzpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daWCaHOVTbBuat-ktdlg9Yku5slEKpMEntbnMjv7KvQwKKvMGeCFTTDdKUhNTjodSgf3WM5mE0VIo9ey0NXB7gH4PNP4QGWNRw6kdj52U68Lf2rs0sPGKddFTtULdS6sHfgNr_lTa8Nq-4pIAZzRNY1FpqexWxkAonRH8q9M_cRPXTb5VgCJUvVbN2qNoqfpfUQyps7E0UwHo58gpxoPlhPRfKRFGnudMcoQNMa-_XbsOenia5s9s9ROYnhX04iuAaz9iYVmtkbs43SZX5-S3vS_bK4pEslVh_qb50O37mH-wtbxlzQHuDlCBNjxBsFFfCVLadwTPWCu5oWL6XMMNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V6eRDRkIofsTp0NFtUJ89NbwVATnSBbOnmxzhFE0ZRKJYlDKjM2gjhhmTSn0xRt5xNIUKWB6i_fwRiOwS4Q2BHntv3zvuA1icIntbO2VZla-Wez7RQ-m8jT5mqLw05P0Tm9l0LL8482JSMVjJCFcCpv2_UVkP7bFAEd5c5Bwy6F1v_HQ3q6OTAc03luqlgHvjzHyQhy3Z0wKJdFWY7gcV9mYN-Ho4FUT0ypwVaRGwHeA69COjNCo3cJkXPtnX3-FEm4H4Ee7tFzEsadctM_uNLgSMcnc8oA3bJhaTcww99BOFcqOYdkvdzy0FX8GjM_i4sLcSdt4jGYPPKcCsA2T-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VnhWhlzYjxGN6XLN2VhqFc-tmhhtl-XbMeJs-FykwH_f2e5bCWrUJOpe12KBEKf_iprHePJZWPgyGzbjXYc2sIjfRKtO2rS0Uvt0AIRfqthYMGqFesn7YzuCEFtyXtTeaSl2JpjcYuwA5yFjEcOM21NztKMKVQeu69alQFFAbuJvIDA0nbDeyN4r1gcl1lNNLD4-F4B3CFIsVI7WmN7msNPVKCERAlOjNQEglDbEzEd42_jLPZvJ9X4lIC9dyR436iDF9dahVlosHDDt3uKr0XJAsq-zNn7FcIf68jb2SHgNsLNOeqhYkmVLghcoOn2ObVUKtoMoNLLq6UqNGZDNcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5-_2X14pfoZiwbjpJUEW1iqYoleTPJcqVBBMYO-CfUvtFqc22S9HaYRh7b-AAVZMXVlTzZSN4_DnJ8-Dsr28de_BKJtJYSljsIUgx_UHTHWQaRv8g50GyPhpMqqLqXwB8Ggmn1Dyh8fIxD1C9FsP_EbLU7uffnlSlXMuM3ztr6TjJfm1JidWa0JT8_fXrtKOewgkkFBSId2P5FZPJtffVM2yCkocciy8Q9-GKqPyQe2ShlCarNCGdcq7OznlAqVkftiFj5meAfVQQ4naG-8DQjBpQLIQ8lQtI1bMhDrREorn0PCO65QtuQMFd_e7ntgj8H5RJGJzcTMni9DDjJ5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx7XxfadqDwRmQdXRD6pffUm3WSOiqgrf_oTX-yjeRjKq0LH30fiZn3QHllOybUoCVr08RIX-KIX8aHEfwT2XuezcP6Q_Ic4lUlFWs5q6fzAYjikw8sU4Cmh_l1HsqTjiu4aEB8uQu07Ryr-efoqJDYLnt8-J_fWPz_rAjnGsVFTcjvSLuLlpzVv252EQyUi3knZb42QPBdtV0tHnxJYxm5vzflKS8j2O9apUKAQg6P9U567qGe6K7o2CsXzeUdFEka0T81cfc94BFFvpF1xRiHNZECcRUb5VvGY2s9D6-Q7KY1DJwIy1EWatq1EFM2lXAVSYojDF0fKg60z-jljhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tcu05S85UyqMXmpw79RAW6kHmlCTakVQfXI7NZBjlYJdlGt6cTz45rm7FIS18fE0WVjEtudxgFjJmvUgH6768WJrpjpFeDamFt_Ayu2eRe33BNLNI95HPwB5D5fwnqFLUFLSzVQQ3B8HzKuXMYvSE7-2-p6T_hL7YUUZ4gydoBDs9lN0RCngASVDKuBcjki64wMmeQvx7sGvP2VdrDN7eS3PPsFKvS6EXRTRa3jBY742-RrcXZpJG5v1zCf5ep3vLTMJqocS-87xD_Q48kgpCPqB0Nee0M3MEHCk-X2vpvifsdRoyizg3Ozfps0_4ClY_Wd9q2hsYAGgnEeWHpx4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWqwmR8GTO0KbTFsiKhbBESqmc3MrPrX60wI-8fMxgoZ0FuZS8ZPtySJHV_Hn7947Oh92Zt3i9Ax-LN-vAaC_tM3gbfWLCSaVtV1T_McVgVAVhH0bJuq-zkqLsyCp5sPLEic2m0ob08qjF1OVvTgHdvvQee5P4DWs0_iZt9r0TOmtyC3wmQ1er78O43ORuU8z1owgTR1ic_c42E5Vc7EFCFhHcfq6yvqV2QJ1KFUYnbRxwEZUqeD8h-kv_FxClC3V7kZL2XSPcj19419cB1pMIqdb5KtqDqPFElY7dEctc6i111vJL05G9XG5eLVAflMh_wxn5SHHcO4GTuIyqWGPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoYLvLr0bt1nYMIoMwh-fd6w_tV9d45nDgrKvfuD6AH6wpYd0ppDCYBewS7vaj-jH-1-7FqO2csPyGA-Il1gEXG7sZ4qd7-QLrVjIFvMU8OUqP5gyd3bSRvsSgNlUnbFAoJqKgnFavvNMpGysOiC5t6ZnjadijDbAi7wT_Pb6DP6TB2U7lDD5f1riyYgZLjgLEG43vFa3hX7dhyud6aAiElj7gwKj90RRn7Gy6I-71rY_3shjrMdIXwQKsHPtNj1Fn99VZCcEsbNQ0MVOTfYPen6l_JP_Sa8apnrCXVoJI3SrnpfwwKzdrvn5IucKuZfs4jnVKooEQMTgj5e31nPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhACKraawfECN8paP_1k-EF-x1DPSW4r9Ipw_AeS7oy-JPA4tbcj8HoLcv6-X1b9_9ARtxbttOALoNd5SdHC2YDEXsfZEGS5aMnKVjcqoV93iTBYNdU60z5Onx4lw52LNnf_D-DrOTecXkNV_EXP2lbFzcA-fpo1JrsplyC8_E2IHSFP7C-amA_PklLJzthQXWootc-yhVqxedQq-a2X-7MaoL3PLnVolesOE1W1iii61jbs5GoGiHg7NVMrsM-1snPnluMMetDQS8aX-Ns7lqkCWX4RxXS__np8tZrwm1VIcAQ7UJukYo8nRi1WPHvkAMzCLkpObJCfkpEmassJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okABEeUvq2Kk1XqiOZNVmXmBUMiltIsIrod8EXyIvToPErfXd8l5Vf3ljApU8QfDQPMTCpeybthlok8x2-kndIfcqiQEHi4ccTp8_rrqycdQzAKVuu654R7IXfkc2cDTrdlH2I7SMh229VCts8bUdVu2hhim_ebIHzKhaOq-xjWwhqK6hhUqkkKe0r4STcZGZnF2lKoi5QJruy4pbLBR8oz6oxqwTMc7PgIooBCxH_JSVY0ZAN5323l35JwaH7V1nA-VUI03id5N2GASPaK9p6ZFGJ3zqdIg3gn1p2pPJq0zKg09Fgf-dVMjyiYGNz_TTVdbeuBUmEHw9E_ksHG35w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ok_8UT5cA0m9x4jdrUzYhDG6LrD0kjVFN-t2_IK_bfC4pKIKJCTHnmAOh2JV1HMpaOiez37Z_9NmgYpx12DaQkUxaHjdVqPZw0ZvMXXv2sEzRr9kOf7jih-PP42Fdw0gD2iYJG_xECccHfYmdotuK1_nIptN9nlnvMGEqThJ-U4afrqR4U00ddxyanMKG1qhNfylsiSWNm7yjO5lwicToAVKDrjxekSlyOGtjNIfauGPs8eAgLYBvOzEVXOdB1QlL5mQ3u94BWpJ-Z5FKJO9EMl-X8m8n5ujGd2modaVuUL0z-DZJOrQSLVIQOlgyvps13AqkGEhKCqd95EpgMaPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-zPUr6UVf2uRoO6pmyqBJbreXHxph_fHXa3NVf20-Dt3_D064G7THA_E7RTeDaGAfqqw5hIjxohd_vRzrKjFHuLeo5B7gZeiX_yVuwk2CyHy4dWK1DNrLaD-n2CwuDqjiSRwxfuq8vZTsAIBKQZwiSh-6NqChBGoiQGzZhSJAEu0H40zbUofaOl85b-E4H9_ocU0ueAs6IGUi0ozKENaY2LZFT2tdXbbpBrv44rxPHKHRUN8HIBQcGGtr9ibdkGH-TISHaZeedCNL9EC_l3R7TRTPDzKlsMhJSYTHNsKBE9zat3lTglZpvyHBqGqHmpgL3erSJxlwS226NqcT8Hsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOxhw5TS0nKbUw0_1ugYfJ64N-lvnLgmYnSwtAySsgC5WeTyIcDBj9b0is2GEsDQfcQWTAEk8sHK4BpHTQGrhTv0POwN9DYy3QoVrB-sv8lNIH_85Eb13wGPrV7hZUIUzLeKknbchZTcsEodw-qpGjtqUu72z7GPzz37AXl_PKXQkxPf3PfOMtEFlxdjSbygMK9AFYbHPjLKsQU-uo24I-RHm2J_3M5MXt3y6wOtkm3_D-icKgueSe0nPECaSzz12cxIs35ZFXo3OX_fux6vxDhpTYpZb4eaS1vH7dO53QXz0taS_d2f5NhMBlcftUMl5xEtBY9Z9zfnynrXlFMgBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=eCGCBIyLBTjcTsTemfVx0PnfhP6nLLiY6mggGk2o-SWhT2TAoml9YayHFZARKh3Y1yh8eddxByf-8lVLg-kh0nqZ-CQP-6pkqwMFxPHm8IFAIoQf8g_B_-8eRNxHhKxeNzWsm0pv2s4BWv48CBLlBk2d_ZMhFJ35IBB2woRthTloL20ng07FKygzk073P6igphfRUQYSXecGubc13p3xUuysHIc2s8XF5rURNkSbYjBNjbHvLmoHJZ6ASBSY6X4QIm4hVOd_zc9gsTAKtN41sJuNAe6oRLLTS5TPqrv8yJv3EW3cR-UtwhgQYF9FmSEQ9thTwKt1zlhFzwUR5rBZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=eCGCBIyLBTjcTsTemfVx0PnfhP6nLLiY6mggGk2o-SWhT2TAoml9YayHFZARKh3Y1yh8eddxByf-8lVLg-kh0nqZ-CQP-6pkqwMFxPHm8IFAIoQf8g_B_-8eRNxHhKxeNzWsm0pv2s4BWv48CBLlBk2d_ZMhFJ35IBB2woRthTloL20ng07FKygzk073P6igphfRUQYSXecGubc13p3xUuysHIc2s8XF5rURNkSbYjBNjbHvLmoHJZ6ASBSY6X4QIm4hVOd_zc9gsTAKtN41sJuNAe6oRLLTS5TPqrv8yJv3EW3cR-UtwhgQYF9FmSEQ9thTwKt1zlhFzwUR5rBZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6NA3t8oB6q6-FsbqSv38-_M1C6odbAO9IpavSW6M7DmIVFXeq2-u_KnYu04gTh4pAS9H_UcCcQupykzIxhmpGr0NtfX_ezO-k59dx9MSMkaj9LMvN6FrYKLOZxgFGPlkXmW4CH7sTXQMVEMKb-7-WGHui1tU3f2wWyf4Nlwglzp1iMFdLGIPZxmrUqctALPQJznWVl572WeZtB6n-A3hTlxCUaLVNPPppTgYMZUlRswrELI6of_4OHE1Bt8EQkpLukNoA2bwsYbaQ_6mWfpOl6feHu3dggJchUACgITXSTfh7KLjhpxyRJC-B0rTDcCkqEJCfLRESTrTl-msc2TqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=n_CEGTo2rTdxDbR1X70ZFfRzNtMhkQvFfOdSZaUSUQbl77mewt3VD-uvgiXSkvnTrgoxmcvluJWjRInDNzG3mM8UMYDqmAxKrcZsQZVMwVQXHCpdbKJN_mju8_pXdcS5kIBQzOEU2SeDa0AlCQWIOzRAVJWegTD3f3sIqfszoDJpZX4KwmsoaGokBVpfwX6XReUrNH7nuX6dVFMKddMgneI0XqQ3dXSh7xQkaayR55-x3-3qevNzlJRWCCTaNBvACxsZagBYoWUFVFuKphqB4PN5HLB1BwaiRGNiucxpWsuksIq4kjy9r5bVt3eoejeGaIXpPNt77u5H85enEQ5mog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=n_CEGTo2rTdxDbR1X70ZFfRzNtMhkQvFfOdSZaUSUQbl77mewt3VD-uvgiXSkvnTrgoxmcvluJWjRInDNzG3mM8UMYDqmAxKrcZsQZVMwVQXHCpdbKJN_mju8_pXdcS5kIBQzOEU2SeDa0AlCQWIOzRAVJWegTD3f3sIqfszoDJpZX4KwmsoaGokBVpfwX6XReUrNH7nuX6dVFMKddMgneI0XqQ3dXSh7xQkaayR55-x3-3qevNzlJRWCCTaNBvACxsZagBYoWUFVFuKphqB4PN5HLB1BwaiRGNiucxpWsuksIq4kjy9r5bVt3eoejeGaIXpPNt77u5H85enEQ5mog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqSalw-wcU-Uc7DzSGpNlCkcmlZMBiXgMS3pXQfu1EqILdv66fs6LryQ1LMJ1jJGJg0b9rV3lRGlouQHXwlUT58Xv0JvAkvM9wCUkV_TyuGOBEjq-ms09GRnGiVdiOKE8DR-TDgNxZ5pur-p4bezMXhUE3OGOg_5lAN3_4CXVMGCMkG60Nt3DrwkxbfbOV8i8q5dGpTCLcrjkOrJSMIyuhKwnIlUhN8QrXeHVl5Oli-83pDTr_Vs9yr5jxrbjxM3EWo7-WEwvIviT-3CCWAhrQT-_kthxV-ptPWv4v7oD_eIrTbuYVCN8F6g1MEDEBib_d752BzDq5PknK4zqlBvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbZX0Ia9LFkNT9TxNfSpJFWGyHdRLjg4nxLGDxWMqXlofaxA2XERLffqfyW3waXTeAugJ5KmSvprInqFRRZSyYF-BeecKxff-0mFAxewFW1vmFYCIlxA-rpKdmq9MNRDcMJSOsuKgU_E4j-wsOyqWMuP1K57FAmknww7rLvKdtRWbccqL9TdVa2sqFcpdjNd_omTYuUwhzvMUASY09nBsTXZMC_abcgjewvLYgDQwgzP_Pb0sUc-WAUrIWZyFbxh0PGPTpktPQ_VND3y6KaUiUFO1DpVl1oH8xwPWDeXQEkgr68opsDtOzrE2aY3j95mLbCk9BkVydaWOkgfixC4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=IAnMETGX3xnJCBGuUskjh53EsrQrKbFqFIzW9mcXbRXgSWfQmRfzHKGx6_KZYdm2iYW8mNaeMH0uYKKpjlBz8M_5ojEpi5qxVOn1d5GqTqSn-LgGdjs-ny1-0HJvT5eK2VXiIDhFvJJUeIrSw9w4vtAJArB7gX5FR8NtYRlePXMxvt4lT2GwBO77K5KicYx2ptM2ly4U7ORfhx3pKAzYpX-A-p7awkTZSJukrvcCaAqn9OPJeziEKqev_sM93StGx8mKQggWWEbKy5I9nSCocmf99YHWWdKsrzj_mlTE4KP5xAxypCqUQDWDjp__uTKj6Ihu8vZpuDzygzAHhSkT_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=IAnMETGX3xnJCBGuUskjh53EsrQrKbFqFIzW9mcXbRXgSWfQmRfzHKGx6_KZYdm2iYW8mNaeMH0uYKKpjlBz8M_5ojEpi5qxVOn1d5GqTqSn-LgGdjs-ny1-0HJvT5eK2VXiIDhFvJJUeIrSw9w4vtAJArB7gX5FR8NtYRlePXMxvt4lT2GwBO77K5KicYx2ptM2ly4U7ORfhx3pKAzYpX-A-p7awkTZSJukrvcCaAqn9OPJeziEKqev_sM93StGx8mKQggWWEbKy5I9nSCocmf99YHWWdKsrzj_mlTE4KP5xAxypCqUQDWDjp__uTKj6Ihu8vZpuDzygzAHhSkT_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSVcj4IMZN-sT1vrLIyR_cOjLj4iOiYvAqrKnwLby2xLuEN6l15X_pGZa9K2LEsLJ-2A0CPBiL2Bg8dxHmmUJmv6Gad2wL3sgV01vqC0D2jIIeJ9eyJ1UdGKyksdKxe4pKUlce0cDGqvaETqX1pV_00WpY04daEq3L3G8TthPdWjszYkyhCThF8IbnUwgbgEq8t3tA30PJZn88EV7vn2MBC9DLK0ULELLZwSgmNDDFYMMBQMjcdtdsU3j5z1wXtyZnmbR7VzDABmQ57X_wifYkonRIt_jBJWRzSwhKmLntuQ10dyTQLjAv8lVeWkD8Mg5mBA792bUQAf86G2wBR5Rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pE06p2b9KlcdebPmeLWi2kC61s4a8iZ9MRWkX1PYU2r2UYlZRGsCm9n0fuuOSWX0gBJTBdx2bmVsJ7VSEMxqa4PHNSs4egHPOxn3rjuQzflZdXHjj3jB6Zz1CBMUCFaouwSd1lg6bGqmrmabWbWxH8TLoklZG_9DsqrIk1eQtzlPGGBhU-0Nnng3Cel3IrXZhfKER8IV2PQE9LiAiEs26PT2tNE30Q9A0eTVmxvEwsso9Ki75-Rhef3WmWStuwH1zz5S0l2e_Nv2o2hsYo2ciIdWuy-UVoHijjyZkaVTS2iIh6u4XagM8gWk7NiduZNpw29_lWeB7ymeLUdNYe394Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq3w1GQpVbAK3sKYjgPOHkzJKJ2QdKPDma2WnTNq6USSvDYifHxFfAbQ_x-ljFaO_MiAj62aFrpcAyuPOE0rBCwoK8qVxQkobBXy1tHqAIbD9RnqyTwivNmMKIzTyjWPwkajrM6qXrSMuldkgKuY5ikhHUJ9IOVquVTSvNpaaOBimd8pPUKbx0lueD55_Df_UqO8bSZC_zpu-xOLjhXwpUR9pA7hinrh99oR0G6BxTqMCzT4mELzYqm9l9LOdYpV8VUaHJ31tiXQyK5irmSDQBs2TeeAmKCodRVym_K3q28cUGjh5q3BT2yokFObsZWgyi6eEFYT8xV479433s2l4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=FpfjIatJSm4qioEV8IhgSuXm3Xn028s1exKxeH-IpzxGnByisM1-cggllwGhJysSDz6bQsSDX2Um-CIWuMrv3_l_RpWscoiL1hcwfHkRCSwiNuIOG3dWvJ7Fn_Sev9sKRNV-dJn2biiYgnE_OzyHV52sbFLXsPft5-15UforX-dOaxXrRI5g2Fcs1ARJi0BFXzJQRqvTmhDfMHixx0KwyGrdHCsi6xUSfibHu88zGuYh7yNixxWqkwwiRrxrGEb9BfylutLdw-y9i738ieStaTLyvO1-BmolbnYdxHi0Hs0XOZZ2NG5xF2ODJ8jbjI4FfPlzwj0dsM6N2esQY6jx5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=FpfjIatJSm4qioEV8IhgSuXm3Xn028s1exKxeH-IpzxGnByisM1-cggllwGhJysSDz6bQsSDX2Um-CIWuMrv3_l_RpWscoiL1hcwfHkRCSwiNuIOG3dWvJ7Fn_Sev9sKRNV-dJn2biiYgnE_OzyHV52sbFLXsPft5-15UforX-dOaxXrRI5g2Fcs1ARJi0BFXzJQRqvTmhDfMHixx0KwyGrdHCsi6xUSfibHu88zGuYh7yNixxWqkwwiRrxrGEb9BfylutLdw-y9i738ieStaTLyvO1-BmolbnYdxHi0Hs0XOZZ2NG5xF2ODJ8jbjI4FfPlzwj0dsM6N2esQY6jx5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=lWPfODcjgDo2lOdzwKnYMuyttCj2Q9pk7539zaIQXiHfloHjVOtwM6cz9j_HXC6LFQ8YUTdAj4Inn2K3eraKyZxctmflMzedirOhR_D9qieD99g2TO9UrKvWTzsD32pWcptCAKmCxLiHoYtEQnESDa9-jFRdbRPfPCKKuu7Uz77kTcWs65LJge7STP-HzqKvh6mlMZlGFUfgNM9siYW40JJ6Xc-yq0rCY1b1FTkgmkVYfYtblI_lkvCFMp42FCVNaYazbO_Co6ujiUBolsH9raZBL1r9q5Jn9YL_zyAnUVdUN49lOkrx1HUDjuI7QWHD7Nz4e8RCY5SZsATw7gsv6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=lWPfODcjgDo2lOdzwKnYMuyttCj2Q9pk7539zaIQXiHfloHjVOtwM6cz9j_HXC6LFQ8YUTdAj4Inn2K3eraKyZxctmflMzedirOhR_D9qieD99g2TO9UrKvWTzsD32pWcptCAKmCxLiHoYtEQnESDa9-jFRdbRPfPCKKuu7Uz77kTcWs65LJge7STP-HzqKvh6mlMZlGFUfgNM9siYW40JJ6Xc-yq0rCY1b1FTkgmkVYfYtblI_lkvCFMp42FCVNaYazbO_Co6ujiUBolsH9raZBL1r9q5Jn9YL_zyAnUVdUN49lOkrx1HUDjuI7QWHD7Nz4e8RCY5SZsATw7gsv6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hqsv3pvpPPYNrJZcXZhwHyHtx0VxsIwv6-SttNhGcaRQYx7s9FkAqmfdg_xbG3PCES86vSz6JGl5SgaWKmujnMGTV7NABQ9VuMKcvrYnYlTERWNHKniEVTq55IST4vmpTOlizb7uso3iE2wKtQILYv1kUEMkCXDpC_T5g5lr9UzEEyWf6QjgV5ZXe2Zow6HjFWiKiVNg674Y4RPHlQtNQEeR-DkOknlM2_WwYz2Ce4JIESTb6ungNx3zOGDgJugFikXs_sp0HJ-Qk6UilSIYZOLk2OcTTCNbzvvD90aaEcb10hy0bK41dOeVUmE2FxxuHS5G-Vf3v8HlRAgvQvEWCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPHSfKY3bba0sNFe8MBngxyrgVc4-H9EYIE-Uj7PaN4XwotN8iM83irXns7XxXrhrCOLzIl0NowheUL4_Blmp4jb2olI220qli6FzkbZOttozcBFFlVoM7n5n87Fz-_RvgNJH3gD36yIMy579zq44dJAyeMKGPAZ4YIwxD_0d2zyB5AQTHU3e2_Fd6QZtkqe2i6_ag7bgncsZfYJc2BXumnVWh9UfSoGTZFQDoRyCSadxCwdSqLNj7jwi3bjJMF1tvtBU1EBUyrsJccAnK8nscJvoSpiDbB6mh6eiUSn7usc2bxKJiKgoWrlR-fWS3uGe1nhe_1SAkNHw1RBjudHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMC75Krg96r0vAPlm-C_EiLQY5Cd0mxCWVcJXHSBMqHEmfvWfbmhi3fS_G65bQyPZyG5vbe9C8h1yRudq2FHQ6-R0XWpxOroI_7RrvlzSaEdGGOW9Nbk5RyMBjB8kTuU9xnniYzhYmztv5-sQxZ2kkek5VBZEr0H4pwPA83XmtLEBcB1edDsGDUWk26ch42FUsSJkPgVotswjzP7AFUh6cSSUc4Bpu4IHSDCFdccaeWI4-EmHB6-m4v-bZTUTjeFDyOilWgF0Xo_rQPdg0Rd6nsrtws5mH5YUqNND4lZkNrVg3tuFO5inMy7bT5dig-2vIfH_EsHZYDBaFxIUp-Pvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_w9skx2fyY7MArfDsABswhrjwczD-ihonpo3-U-MP8QgZB2Hbmb5ZHnLp3d5M334yWRBVviUHz25vxkkWhRtas5CTqUy2e1XtapbYxhq5Tz9vULEa5WhA7u_WuNNPsLMMb62dGm5In4rh5QPD80mNgNjDOVM5ll7JVvqsRLvI9UjvLRwGOY_VHu8URTQPiUAelxl8fe9zmCR4zq7l3_4rxBQAArumM0flq6YCKEMKCYll54E4sG8RA_tpmSYbRI1iFTa7euxcVwbtI_go_U5CjE-5Hhs6alY_MRUtOomdjmMC1Qv43NrVIvTIkZeYVpofNZa6kNZrTUhYRhsdl5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmbLK4r92OjplEXdeuMNfjTmLfxgyGpp6rGZ9A8OR56B0uarvmDP4OcY_FdXLGcIkheHLoYNHyH__OFKYE3rFAjfKgKndBcet5APpOiclJ-Gy5_FjXhMydlFtHMoVW0pXeXWkI3Wvug9Ygbfg-jzEJPt-Z5x8ZRQQxMzc_4gRw-FABA_W6IKBUhJRFW-Pp0MFk7dv9BT4TZipirPq6daKiYVhV5vbmaf8jFJ7VK3RDTiw_-cCPeVmdSOzW-DvazyNp1VwnyIorB5GYUUujt5DVpkfL0H1qvlqtIVhbqZYIUHwK6Pv6AGjjoMXuwnorP0bW8AJ40aoJrytxDJ8-Ro1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIXDaeABT3FU1AD2EUQoIWTCfdNr92nnGDkJPPv-xMcSSnNiX3_5wDLTG3v8oKMPwGCEgmWPNZeWqimD6a7kQeVpDGnS_HOq6dCAfcoyLcH5vS0ypMrsXIIEvy2ZPnouO7AxglQtAFY8oagX-g1-OsEOhCFepJhHVbHFEBz659YHxFJrxYlFiwgO9RxddPQtstvNIjxXF_IDXlfystRrGvUqYF99dvgclkjPcqYLkdcRuwky5Xq1yZJW6sM8ICYOTGV4vxaCY7VrR-ksnAl4syKIs_3yjx0Dn43s5HkW0FALp6Jp8nQTdxSMFNycwIV_XZQ4cf7ad8-PjPjfq35-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzTYxTp8v_9MqiV34wvZ6neoKqt2kcV0_x68XkSKQTJ0BVagqGytYUJwW33hSlBGY5g9WNMAhX88Ra5NuNBBl6Br2eatc00Bj06NzQiQ__zHA21fbxKZhRb7-jFnEY8mP9KfviD_QLr3NusmbHIoWX_vTk4VX9JPovhdkmLtT6uock9Ch-04uFmM53MU6xfyiwzaS6CZUUFSVsA6yWw8wLpiJEFbM08J1vVj0gSHPn5oQJ9YI_6YvlzccyPsxCSPC6o3fS9ligNWboam_V7S-ADKLml8lx7WhkXNPsP7mKwBQEpokuD8wr1VFWR3xd0GF70_hqx3i_dptQ15_p2wFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=OeuONnHu_fHzxKlBGprskr4GTjiyVXggPYx73xi4aTzbdLbDg9CgWvTtu4Qe6ioMdckI4Gs_Io9pvIilOFOGO8HUmOb2ZGTAUF42z1xdaUrr0ucmnNk_EFlx981XYrJVMtKPKNlthk-r1KRIdLzqQ3axTHhmUFh1uwykgvoPHD9HGZKMqFhAHKf3dTqyquCpm655qiUuLqSKL4m-N-cO6_4FCJ8T0Kmd2rge2Ntf-YGX4YU8XDeSHECbmuTH2-_MG2fWxwqV3P0T_TI-zweda-V6KtA221HYnwLSPRR2rtQhODLgvBNFkaPSRUNJ1dtV_4I5JSiTUU4NxBJcQ8n8pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=OeuONnHu_fHzxKlBGprskr4GTjiyVXggPYx73xi4aTzbdLbDg9CgWvTtu4Qe6ioMdckI4Gs_Io9pvIilOFOGO8HUmOb2ZGTAUF42z1xdaUrr0ucmnNk_EFlx981XYrJVMtKPKNlthk-r1KRIdLzqQ3axTHhmUFh1uwykgvoPHD9HGZKMqFhAHKf3dTqyquCpm655qiUuLqSKL4m-N-cO6_4FCJ8T0Kmd2rge2Ntf-YGX4YU8XDeSHECbmuTH2-_MG2fWxwqV3P0T_TI-zweda-V6KtA221HYnwLSPRR2rtQhODLgvBNFkaPSRUNJ1dtV_4I5JSiTUU4NxBJcQ8n8pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=N-UfxeReVS9WXhXgDITnLpzAnHK4HghcVmy9imIF8aAaqxJKUlnoY1A4xVeIlnd9rU7dK8WlCse_7x1npQ3nZy8YtLVVFeCAsq2L5JFDUWicKV_YTC-_iy-G3O1-sN7TcxXgxg0meCBBvERLlP0DqCfwFKEEhiXrDVbP7gK7J6KEfC8WOfNUN89rAKnz9eo9nHlzxq1Cv2G2PsUwzqUgAKPyAHBi2VU8X6oIWVHYKeQwWZNK_BkhlM9h_74Y0SDKRHgCi_D1P7ewktoFXt-zvRAW79QFT5BUsaAOfROqqRf4HStChYlSUDqCN2Po5l7BCQS3mMA8-A9H9lK8Q36I5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=N-UfxeReVS9WXhXgDITnLpzAnHK4HghcVmy9imIF8aAaqxJKUlnoY1A4xVeIlnd9rU7dK8WlCse_7x1npQ3nZy8YtLVVFeCAsq2L5JFDUWicKV_YTC-_iy-G3O1-sN7TcxXgxg0meCBBvERLlP0DqCfwFKEEhiXrDVbP7gK7J6KEfC8WOfNUN89rAKnz9eo9nHlzxq1Cv2G2PsUwzqUgAKPyAHBi2VU8X6oIWVHYKeQwWZNK_BkhlM9h_74Y0SDKRHgCi_D1P7ewktoFXt-zvRAW79QFT5BUsaAOfROqqRf4HStChYlSUDqCN2Po5l7BCQS3mMA8-A9H9lK8Q36I5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=lJGMmowHtjcQlbunyEhFVo8CvHUTwRYjVxN7PjIbcFFsEqqo0RFXtyo6kqe68jFDmP_DG3ykbK4Alee7yQjbBvlI_cJXfyzx2ik-m1dVEMi1i03QMz6mHoJwqnWEX6KcTBnS8ebHAsCtAJBgGxQzGyohdRR1Cu5YxVIRzj_rL-K2Ttrsnz4P0ao2z335P2ieS6t7Gdv3wiBG38z6KFlfUvYJEZ9lnnWn-pbsI6-ZG4pWDA5fe019HTYbM1pXW7ETLWHHhMJJV-GTJt2a6qifURasyHxc6PTDYLMgo1UJEM-S9CVT7ZCzFI7OP2kd5LGeD87jJi44KO5RKIB7LfIKMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=lJGMmowHtjcQlbunyEhFVo8CvHUTwRYjVxN7PjIbcFFsEqqo0RFXtyo6kqe68jFDmP_DG3ykbK4Alee7yQjbBvlI_cJXfyzx2ik-m1dVEMi1i03QMz6mHoJwqnWEX6KcTBnS8ebHAsCtAJBgGxQzGyohdRR1Cu5YxVIRzj_rL-K2Ttrsnz4P0ao2z335P2ieS6t7Gdv3wiBG38z6KFlfUvYJEZ9lnnWn-pbsI6-ZG4pWDA5fe019HTYbM1pXW7ETLWHHhMJJV-GTJt2a6qifURasyHxc6PTDYLMgo1UJEM-S9CVT7ZCzFI7OP2kd5LGeD87jJi44KO5RKIB7LfIKMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=v63hUcvZ0JYm1Kc0sctgALLXr40QB5gJx2xpSG2lDNPFac4afEtj01YpEtRSjnx_dGBnEipEzI9hO_e7Dg6CouyRrgtnCrhDnkUCFtbLQsuFQNabd6cN3fFa6t9cH8oK-IYvkdxL7baZWgjVlEeWEslDxECfn-70X0aDIelQ9CCTaRWvyW3OdVmxqdfAr_HYTSaiA1sC2HeCZtiELwrYEyy_J4W47fQkVJgviztT3JgwM1GsNsPKPGQraHcJrB-tLbuWzOPUUYYrbDbaoYoE8jrvLzL2PfqQ3-fLT7bMzYv38tl5mfCMlIWRaoc1Ri4SPH3QzSTHzBfE8UVhJvtLtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=v63hUcvZ0JYm1Kc0sctgALLXr40QB5gJx2xpSG2lDNPFac4afEtj01YpEtRSjnx_dGBnEipEzI9hO_e7Dg6CouyRrgtnCrhDnkUCFtbLQsuFQNabd6cN3fFa6t9cH8oK-IYvkdxL7baZWgjVlEeWEslDxECfn-70X0aDIelQ9CCTaRWvyW3OdVmxqdfAr_HYTSaiA1sC2HeCZtiELwrYEyy_J4W47fQkVJgviztT3JgwM1GsNsPKPGQraHcJrB-tLbuWzOPUUYYrbDbaoYoE8jrvLzL2PfqQ3-fLT7bMzYv38tl5mfCMlIWRaoc1Ri4SPH3QzSTHzBfE8UVhJvtLtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=uHxV-eBeDiVf2A34TRUZ-z3BO8Xj4P9b7kGJLzq4KIN2czi0Q-7qawSfnUCI29l9qYs24y5TiZr32d1zZQATsniOdGW8lw_0OG0649Adyrdkn_NKp0gINwKfeyiJ8-xSLI_PVYaf1CyJvZ0ptnarELH-JKFD4iFhXoGrw97q8CgLxdEeLDN2kBA7vnGwJf3NrCq8B3vFavqRDkVqYNFQg0p6yezO_HyOZDIQStCYHZdK1uIrzeV5P4wbeYj1KBOEZiqySIachFr4951J7td7DZWWHw8whzjniCyJop-plTlDYm7kN-XBzz3sojSPzjejV0HRPmCcfNNwUuuePPlqww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=uHxV-eBeDiVf2A34TRUZ-z3BO8Xj4P9b7kGJLzq4KIN2czi0Q-7qawSfnUCI29l9qYs24y5TiZr32d1zZQATsniOdGW8lw_0OG0649Adyrdkn_NKp0gINwKfeyiJ8-xSLI_PVYaf1CyJvZ0ptnarELH-JKFD4iFhXoGrw97q8CgLxdEeLDN2kBA7vnGwJf3NrCq8B3vFavqRDkVqYNFQg0p6yezO_HyOZDIQStCYHZdK1uIrzeV5P4wbeYj1KBOEZiqySIachFr4951J7td7DZWWHw8whzjniCyJop-plTlDYm7kN-XBzz3sojSPzjejV0HRPmCcfNNwUuuePPlqww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=pryb5eWgfPNTAbzlvTsbeb883ohkQ-TrvWuAYpZ2EAaYsocdnt9vJRnyp4ce2-4mGEc8sx9lIJv8SaiBubdytEoQlOi4TxgJXrw0_9ChNWUm5MeBIhFf_XZ11axiFhJUZUaYvtKK5xgcM8DiMTRJkYWzFMuVumgKfO1DB55YTYCXPdZ1rsoXuau4YU991kLyQCE6XzWkTG0M35V23lOV2JENopO9s761cLmxwLezfgAfBIOSYNmxEHozkMtWFPg47IM258daa--NNM_36_gsPA-y5S7hm2d3v_9DGVUgmC-7IA4ZLE5haG6oUHbSxeysayZkH4asX2EqBQ6TVaCyIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=pryb5eWgfPNTAbzlvTsbeb883ohkQ-TrvWuAYpZ2EAaYsocdnt9vJRnyp4ce2-4mGEc8sx9lIJv8SaiBubdytEoQlOi4TxgJXrw0_9ChNWUm5MeBIhFf_XZ11axiFhJUZUaYvtKK5xgcM8DiMTRJkYWzFMuVumgKfO1DB55YTYCXPdZ1rsoXuau4YU991kLyQCE6XzWkTG0M35V23lOV2JENopO9s761cLmxwLezfgAfBIOSYNmxEHozkMtWFPg47IM258daa--NNM_36_gsPA-y5S7hm2d3v_9DGVUgmC-7IA4ZLE5haG6oUHbSxeysayZkH4asX2EqBQ6TVaCyIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=ByffXj2DMh4AjLxNXIRiXGxpDmTbXLFF2-x1a0i-KX-MlBRi-C2qw5JllnktTAYrH8P4mJruKFyPiM_M7RyoGZaJMS_H_BpjzHLlAH1SfhQ-YZMgSG5gWb-RU9wipkOyYSm3TiXK2sJSldjnMZntBw_G0eySx2tTGHmKo635nBjggjWuVnySbBbZSvJiM03TBD31uFxiYsV0djvAp6ux76QlKIyY8Nt7KW0zfE0okG8ae5jpYz6AlHTXyFXKnzoWGKZVRHEOOsAahDM8h27x0pjlGXeyp7PTKhHReTp6uC5KHqrJnpMFv81ALoZ97UVcpoRuCGW59ik_LDcRbju4vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=ByffXj2DMh4AjLxNXIRiXGxpDmTbXLFF2-x1a0i-KX-MlBRi-C2qw5JllnktTAYrH8P4mJruKFyPiM_M7RyoGZaJMS_H_BpjzHLlAH1SfhQ-YZMgSG5gWb-RU9wipkOyYSm3TiXK2sJSldjnMZntBw_G0eySx2tTGHmKo635nBjggjWuVnySbBbZSvJiM03TBD31uFxiYsV0djvAp6ux76QlKIyY8Nt7KW0zfE0okG8ae5jpYz6AlHTXyFXKnzoWGKZVRHEOOsAahDM8h27x0pjlGXeyp7PTKhHReTp6uC5KHqrJnpMFv81ALoZ97UVcpoRuCGW59ik_LDcRbju4vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT3IPN5PmjM6gyCAFtSLEMnKLlGi4hEQCWnT6R7nv6YHa7QjNHwKZidiAO7j0T8b7asPvUBLR-GBBbhdhSxhKNlQ5chqHoVMZsHS9jITraOhCnwpYB78NDDkaq_n6-tLC96WfzZOB4ZAKcB0oL9abFv43ChHIWMT-4MnTFL7hFQBHtm8Pl2pDuJ_0A7_cMG1kzQtHKhOmFoC1qPiV6ADswqvjDIZKHac--zgnImzMKfPdLiavGlCtzd5L5CG17bYcc69Tl4lvHdS-4ih9xtsqSBFHkj2dIDtyts3VeHXM6t_qTULSb80OiC-3KXBdnCXp2fO1DUixz7rc08hJMDxtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=nKmippdljqtIZF4Db5j9vGTxivYb6JV_e2L_GeDEhOlbs7PtmNtVy6I9SgZ7Ocvbb9MKVdlzYkrwd7_pOEp1qNkQFMLwTVmXYa4xyosUpL4Ze2S2VTmeMDNEfMK-M_ejrmLKLcTkglyOGC-kcLbhye8xMFbZCjEBZ8zrzW2bIWdMDZX15uM9IHsiyMgRyMLP5yQ5RPS80QvkXfJid0DRzhTRquN6dSKOcsD6dQ7Bbz4uW5tNT2-wEAE3Am5rCIz3tfkATY97LEoK9UMiVc3q2PYR9ADAHUjVcGNtCZYkpdNkYsq9A6vH3ut94ZrRxDKl24QfMqVdDhbtRSIOJ839Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=nKmippdljqtIZF4Db5j9vGTxivYb6JV_e2L_GeDEhOlbs7PtmNtVy6I9SgZ7Ocvbb9MKVdlzYkrwd7_pOEp1qNkQFMLwTVmXYa4xyosUpL4Ze2S2VTmeMDNEfMK-M_ejrmLKLcTkglyOGC-kcLbhye8xMFbZCjEBZ8zrzW2bIWdMDZX15uM9IHsiyMgRyMLP5yQ5RPS80QvkXfJid0DRzhTRquN6dSKOcsD6dQ7Bbz4uW5tNT2-wEAE3Am5rCIz3tfkATY97LEoK9UMiVc3q2PYR9ADAHUjVcGNtCZYkpdNkYsq9A6vH3ut94ZrRxDKl24QfMqVdDhbtRSIOJ839Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
