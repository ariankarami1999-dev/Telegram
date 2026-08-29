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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 19:12:14</div>
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
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppdWci7ZnA-2IRuJiqgorxBppJ_u99YOeCWe5tic5pKks_PnaUuyrFvFu-Mfb4hhen-HF90IgXM0WevkchVe06wml_VbzvFM3Hj1vJXuwOsNpn9nLeWDMQhxtTVK7JuUDocUBCrZrC2t9SYDC8pz5FgnmLZFNqvUHSiOLVysmQrxctESXa3P1bk6Fwf0U0_zMVgJD4TGjwonnzGR1kL68ljQqAgZfpGYy_AWM3CPk1c1L50SHHBAvhXE59DeJNDJYiCB_z1oIupj3YCQFjATfnDaS83iV8p_aEGrPDSijCHkS_LXAggypfJApJeKzkWEaJx-veBbRZdaLBSqXjLFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK3pISSKeb709ekPyaCs3xRd57_sR6AE09qWFpfB3zOkPXDPEJ10deQhA5jwPGGW-i8X-X3Gcxj49_L5DDebDggmg3WKDBNGOMMXDcbekL5tl5YhBAYwjg4sibAYByE-85p3loeKpCJ2S5YNrOFYsUMAtibwd57HBMEx-SZ6nK9l0b3R-M9-yrW_Qa8Kv-8J8IVU5VLOH_V1ikwNpbuiTXqKTN7X4St1VEwwPXdwKGzFUDF40M6Wm8--GYJD2DlIK2Djt5vyG6CODZF1mbEkahAW_BpKwR7Ozra6A1Ynx7sMaD3cpcJVy-iXA66EYjQDSWpdTdfhLaUQgVUnqtM4Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F873Dd8hbgzzwogMZROePk5VNqAyQxOmaXa0wPpGX8MCNctDRvtCCqBxNQ0QBaIxWb-ls0H0v2cgJaqZTD_BKa2SSu7Eg4j5RBFEy46EYkr6vRZzas51QpzgoLNbouaQD30VHmXUOBv6-sLenEkcBa1qXWnu_N1WLw5W2E3S2ZZiA-yuuBFGW8Bao8rWnVdRAOT5C4FBLhX3dHzelPGdAFZqvZtxc7tZFuD3FblTyKgPn1Hz0x87-qvQ89CGPQNOwUIGBAOc1Ift9ZUipLLERwqAH89ZWHIWPJIXFpUJ0ixWmL8zsOr70wRTf-TwzHo9TCJMw3xhgw80ZcD8CJgrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iuygkne37eKpEPiEu0fgBw2tXEq5arRjgGWK2OUpiQNoD_NJQtgzZivRDqZbabzUTPLmMPKYiG1LA8AjmnO3RaHIi4EPA3uOmNnWD-5v8ZeJLKWdeiQv2WusTt6o_YIa9Y9l2cgLTgzQLZbapBldc2sum8VyB_j_O4dLcMHhQHxK4gBrdBOf08jveLhWQN6nTsW1zPRABDV9A_8wG7n76CUhSiP8NbAvXgQRpD-hHOwK4Jwy_fks8glTTawaPdI6TTW3lWnrvjSaYvgItHsubjTbBGlla7-vPqvt6_3RC0vAHgHNWs4fy8pPwj26hFP2mGLNjc2RL39yOkthCnAoFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYbIMjOmfnL4bpCbd7hgKO9RAhwcp2hHn7-rCA7iWcSVsCbutMeQe5DcjIEeV7PQv93hmkEZRJZRRJI0O7ah2G3jeLV-9AJ7RPR0E7uKaeeIrZqMNxnYSjnOkqqfJKd-XXAYpsmU7wmTnegB0iZPH5ttsiKbvX_3hrD3Zp2vAZ88NRBnmzD5D8A5ItOJJn2FeJOfdvmi_zrFETooP5k0bwDpGvWSAoSPIczCEtErMMkV-tBBXJTXqNFM2a6CHfArhp6TcyNy1JjLIMkaULUO8N_a7liWqZNtnGfy2O1sYqguuRijDLNJf0dooFGx0CJs3Rv9rmSNMBc6JwW2TgJfzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM16KEgGeB0kEieNc9w3iawjSudD4wQtVCYDfBLz98yaypR2TDGdv_-Xy4NoV0vxV36qYpwjt5jIod8wRvtwX9MiazCGXdeWa-04Wyts9bM1RELv7W6OtNlPON29768UMV8UkqEUwPO9Lzpq7qScGeUm7c9WyD06aWVlhODwEnNcX7IngBUKMYB1Ru8B22xJhqHDffbbfdYLYlzHHq3b6Jdwdxb6HP6tsvpBvI9Z1smb8V05P_AWiMHNR90Z19Vrmatd4BnnWQwNc3s58QFmjynnUFFsa8hKWf_LK87ax1JsLnDRH7GowZLWdohH7bW_wXk9MVunZ4xSadrwpW5OBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp2TYrzLxQTnJTGsKPEV4E_lhprpLh9UQhCqiVo1ZA59lU1XRjbE9oFifatVbu4aO0-dHm5BRLvYG8K4oLVsUdlharIhw8gRSdCYcGfSkThaaP_R7tg5A9wslXQrDlRkLRD6L4lE8RMoB8oGyBzXG2qA6Sh86rNoTGg5RYQ21OdWhpbstTQZrvsWQYtdlTbcBhcaGJvJPtXBmqa_t79Aj-zj2wcpUHFiRWR-Sd2zAYzl4nXDGVEDZ6EDdtoFnndcCYZ00skYxC6RvJgjTy7X1CTw6hhv5lgBf5nEzlpiHkQfGOqpgxti1DXcTZsm0UmNS_30AIwJQk2O2Dm5TPU-lQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=cXWCSDOATaHakyPAGhrnHq1ohKZY3YslLAxvADA5kSq81j0NtCJYaXPdp08QYIV1z0OFVigMjS3cSaZw73zQsEVE5lczm3zIW_zZJM8r4q_OILJw0YDqvQuybiWMD-XQcYn7tPNFMWEOFpBMfRq7UTyqTw2ZVcwESF_va2IRB6zcF1ivgtMaWXnDPMf314xa510GMfJ9zZO1p5IlrDtjiqVO7RUW1yNzFMB1P82Z3mz9AUb4dwhKP77LW_L4N8g0L21Bn0sPQmQuO6SJ0Wvbb43lf6_t9lC6QgWQhuG9vmR06hdxsxrWzAIMULGEO0qgGW9TDi1vHJLPKeJ-ge4GuJLjRwccF8tRslnzzpww4hMZ0iJK7foUJuTtx3gdfPu8bRkztJs5jSBOMeX-PmMXkjrUGnM0YmJsv8v8hWVXRTBPHWgfnvbZeQT1kn0x0__nMSV753ZhxypGsgOmyEZyhed94wNqfBCICSMGzDSCjaZT3GEtPpfXcuotx3TS7YO9CeebzVQYHT73OcHFRqOOkwA1BSo2wIqkWaupHO0oJRA4O7MW4T6QFIb2rxGPQKm6QDv0EXsu-0NVELbcLgbiCdRYWWAF6zLOkmW--19FkvP9YMtTSkuIMyVP41F0xXa-TnNpsrC6FEa5ysxZeLB65fGhVx6PS0RNOqRcfXEThC0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=cXWCSDOATaHakyPAGhrnHq1ohKZY3YslLAxvADA5kSq81j0NtCJYaXPdp08QYIV1z0OFVigMjS3cSaZw73zQsEVE5lczm3zIW_zZJM8r4q_OILJw0YDqvQuybiWMD-XQcYn7tPNFMWEOFpBMfRq7UTyqTw2ZVcwESF_va2IRB6zcF1ivgtMaWXnDPMf314xa510GMfJ9zZO1p5IlrDtjiqVO7RUW1yNzFMB1P82Z3mz9AUb4dwhKP77LW_L4N8g0L21Bn0sPQmQuO6SJ0Wvbb43lf6_t9lC6QgWQhuG9vmR06hdxsxrWzAIMULGEO0qgGW9TDi1vHJLPKeJ-ge4GuJLjRwccF8tRslnzzpww4hMZ0iJK7foUJuTtx3gdfPu8bRkztJs5jSBOMeX-PmMXkjrUGnM0YmJsv8v8hWVXRTBPHWgfnvbZeQT1kn0x0__nMSV753ZhxypGsgOmyEZyhed94wNqfBCICSMGzDSCjaZT3GEtPpfXcuotx3TS7YO9CeebzVQYHT73OcHFRqOOkwA1BSo2wIqkWaupHO0oJRA4O7MW4T6QFIb2rxGPQKm6QDv0EXsu-0NVELbcLgbiCdRYWWAF6zLOkmW--19FkvP9YMtTSkuIMyVP41F0xXa-TnNpsrC6FEa5ysxZeLB65fGhVx6PS0RNOqRcfXEThC0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcFO8nOhFgHqlOP3Q2L0umZOyyZqdNgD-Hl_HxHm5hpHv4A753UUZyXWw--QfocDdk2mmVSOI6v1c5EXfkH5AVUsAeAS1rUJSzHty21fsHKdwbO225E2Ut35-GmBYguED7wVSqkN86Lc4xs4Qficb-OdJC6GihcWgPiKzNOvO9kig8OC6IgqiiDgYVOt4pVCUAtkzkgyC4Gpk-CqYtJAR1TYwMrxFVj6WA8zxA9sVMbP4oJv0dFF26Wzrpg1cCbx35icE_lkXg4gNEmo50LSLQteI8xnNcD0raKIFO6p8GCmuz7jG8124VseAHuU_olKzkutcKnXRqcRNqrqadj8rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaQVaSipB47H0SXEr0znjAHIzF6K-Th3rD9PBc_aHP9pu7U3N_6xdEQuf9TwagFj7SLAjx_uJVLEcpyjmlutCNnXXDnsYL8Y4Vn6gKyKCDaNCQCI1biWt-0KZjLKsjiPCIuWCoKHvCSM4q72QCCLKFnhrg20077usaRNZoImCcAwL_MHWRgsNj9YFdCDN61TNcsXdyuBY0G1m3eFJOFrdVs9Pmhfw0LFlTEOQuPSHGmSTZ7dVqUQb7MbAf-fqpLUmiSpE_mop8CJbd-tUz4OVxtPpnbfYwlhrC5bvE3Mb8-VeRiia_K9R3f6Cnqb0xi6Pm45wQkP6blX2mdNGt1GWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKVEWN3F776orPW98XRaeooi3MyegwpvEdeS4iwxES6W0xsg0Op0b_lox4vV7n_HH4bcK6sC3DgqR4AUD15AbSAuWCldibk9xu7wYuwLtL9G2l42dLgArcyv2jQxlUuLLFyLYcpBl4zA0nJggEC_ICNmuqHvt4h_XhHL0W2I4O9Q06jzYtTDT1nKvstUNatQNBqu4nruQz0WlBn1sWS3R4DbSpx1qf-3-F45k8n_JkNNB7ED145DwQ3vwbJp3Mc2k70QItO1ZmEU0B9VnaSDD9GN40ZNZdsKosc5CsIqzvIUYjTLLwv6ALzMkg9ESrBW5tjImHdfYdUa41nvY7erQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czp6U4V2TlygBcPV2ThgpqKMq_YX-ptgNgwMMol8OntHqe_0YTKGHkEcO8tncfA7VpWSAKDit_gKE4LOTvdvsWDTbnnUolFSrJdcsTQCwE6DiIIk0Ty9gxQL_pXUU1QPWij-qdCnbXuktV250J11jxhtYgvl2aeexEelWAsFAi32m7uzRzCMulp-SiVPAVimdKuD0U1ESPJD5seOsXtXGvg6vm8r7qseqMi7Q9nFc4JmYxVUrNvnOEO-_Xs9_0-nshlbyWBPqcP0EXVnIzWd4JYXT1fnLZz8J8-lft5vWYJGW9aaeUwFp50GhhmJNOF9ofKmFF0oFxClZnc1Jgp9Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/royrKf8eMhrwTWxlElFlwUUEg_4ftJaFOe-EVQX9AxQjqjPeyuCbCfujRXlm2GHHN_wqbpb8vkvVmq3EzUX-C2STheDnY94Lq-Oby7cpbO7ydYtXvXRUPDwJd-QkHP6x99GIdj2Bgf12vkJTloBS4tJPQQOOpydAKS-UkhA6AmsM4DWriNyo4_WbeXzNFlk6uVokf3qCQI1eXk-Z7_aR2psqBwOJTDweFUmcuauH5Nmsdut6ktMPsCUD3WV6SiK9qz-aCQU-u9Pyiq9dW6IE4yv6rYwElKpliCMQNGEPuQO5hWHkhMTCRU-sg8rT7yqvTT-a6B1jtuV34EYzBYt8Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDwn6regSW5KUZ9VX4xRnZ6sKgzBWg33SQkjotw5rR2MOufConttHBKu3arsV30BBuB29q3hNaDBPHKyJrgW-XPLoQw4ZMW2nsx2HQhoACIxbvM7NSBEZcEeWDt437ldwu7NHPyVTvrsUjIITbfq_vffJXfRdcyKdB2aRVq_sbfXH5vco0kJN8ThGYQdevUGy6s_sALu1sJC51jiOMDXhQYdLUWOZK7oaQlMV-KyKM3GrbYs6yZYizeCF_d6ndDb1q5Z1fp-nI-NMmSmDVm40rgmq2HO0iCn-Rs0JCL1LCoqRt4cC9LV86zkVe-IO5oEm3SAT0Aebhiap_WLTchgPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBRMsTOzVW2LK40iwHwYPcCGFvgbf7hHw6jMQn4q6mWubRvaOg63SB8I01z1mOS7qs_e9iuxtqUPPwTbPnOB9VhhIgA89CY4bj1h8cVPv6yRpnWcJVYGP877O1-4ntCgxXf1yvuM59NMmiOKOpWkup1lt-G8XqS7c_f1VPRWHIO6ZkjQURspnnTd3vPNXjXQw9TwN-eO9PCtRcpu60rRnBUyhZRk9XOAtJPtwFYbvfvDTw4_X6WijTHK37cnkvn8uyrjbzhjjXQGaPfzlZiLqAogcAK_YMt4V4CY2gAb5Ze8KE52sbE_6PD3znkeAgu0S2ygTKqMy_Oh6xD-6fPZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZBatIORbRscCfgl8rrFAed9xsqXS7SVKSb-cUXqQAYK7G6tKlNe6jZWfxV1vZTEd3OLxLjhQBgxefk3tO4QNQRjhFTUFrmyLtp33_9bHYCMQ72n1ZEK9ZVNtBfgRdl-pYNwMmHTmy_uyZXvjvfdub0eq1KW14pzoxtXR68RV2fEwRqA1qM7lg4OZTP__lCjaFuKkD6bw6bC0TJKt3fcjZ-2q-sahHxsc18nieHha_odt35LT27BljAlDYHB8RxSljTZc1qzEWMLA0bHSp4KFgcW0ahTQr-fclJb4yfTrV78bbbkv3VQcuzaIhrJOhknJMML4EbKBgKmvEQKTRJFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEB4LfhZH3oVJLS6B1U665rslRX-K1rLy6kSWh68PNSfzADIOX-lgVobEAQ3iGYGZKOR7FjPZ3Tp5pu_oB695qt8A2R-vzOSjaL9zLFmyNBuQfqcA1OnOD_4m2MzXjpUx4Ck2LudXXCd9CKEAIxZW1wKpu8DZjboN54JjvFXBXQUwZeDz4UAVajA7UptbucUIZYlRAHkpDFiv9Un1VqjN2YvzaTwz8ozabpxYnAE-3riz95bXTazf807h8sDDJy9yrvLTELHnG--nbPLSJ9ehsJIRX7HVyZeJg_GjWCpG9WMCLkrocz5ALN8lnD-RLYZB5qk9CRBUkLIoNARqsljDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0aFY3Xuj93yw_G5qY7tti0I-BMZjJSpU7yfvR449SxSJkZC4JEfKxD7DLl9wzvAGjkchFfs1ICyY4S4gQgImcteQu2CQex124kIwIUQ2VhpVNfRkaioUoYEoTM2NkTw2Eq_kmwv391Bz9NHhJNScMHzwPLnJhZf4TPfJS4EpWBvcUmi8qfr6oGwAXlM_vGGuqQmReOu6WicNmAeGnb0y0TOOGwI-0mcFt79mHAHqO6_aiBDhtKA-gJKBZa--A3ZjxvG9iSh3tSCoXlVpreQJEyr-PhUdtiY_unaldKq61QhAuXLeNTYrMjoAFYYG7JZuX2sljxw2jrNnD5_X43XhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEaHR1ZrcBop-TEM-NKG5q0KWH6MG_rDNsxpYmMVwpY1NbMMEQZ_qObr1_felGGzz29rpsp3SudhEjVa9laHQyhPL7myLjxy5TRwkGoRYEC1Mqq73vGiLCSy0h7F7nR5514-H1OYrKQvUH8EfKHaPMiuPyktaVZAQMbZSurjmbg2-unASF_AhGWcaLNitQXQ_tK300Jo2yKbbxOr-cepOY24Xq9bbAawYJtEBefh6WlMYlAiFpwV1KdM-lWaA3wIJLUPS6g9qfD6td8MgPFDW5Nj9wOwo2fPZO71izYwG_exnXKcSMgmSwn0vs1IJXpjwCZdrMzQafCi_SSZuZsJnQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdyWlox1Ld3OzGbZzwG7cV8XGHpFGm-PcKWUpMTPDAc5qkCFkSuIWrzoXgxBTZS3JuCCQfpbOLcCZc7es3VDrou0aztJRGMw_Rsp00z-dy-Xr5p-jCDRzchdqNz9hGQGzMTWVfzROgovWmDGAxE2uCaiimfoekKuSJINlhEKHdC_f1vDrio0fSAIVNLsmGpGsFksbluIycmdj6wa7bJTIPYVUU4JTtX6RVGvsYHwUTGV8MCsZOlC2EfOjmkjQnbA7vaq7b9VPCGS40DxLFjghokBsTdSjSjI1IZldRyyoLypU9FCS3Wtm9XZ7zv-REbh5unDSJ6qZlBdoE6H8Bpjrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OlqBNjYRiRLtC3dxoUsAecWfFMYwXu0Gwin9rvUx7IqzVjOYTar3mHpdo6hLu-FrcfWVN8eO2llYQ18xp8RwnQaaXojAU0nAhPb8zARvS9PPbyqRCM0VqdN0j0KkOdLIwHF5KHSZyFKCrg-ryj9LDLeK2KDjcVjE1em94DoWpijT6OaC3W2nNNOdU3gXUvsZL55YX3KX8JROsOZSk1ShOu6_nGsK1jMH-WvVopbRqOnFBV0uENwZDb6Dbca5Zhj27UEb95AWDw3fsgefm88O_8Ni5xl6l6FeiTFCvPTZyHAvkTSgTDape2BHvc_geCKO_ID6JdbKFaLmN0j8LRyu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKRHB43uY0Swvggl16J_7fahwEQBy-gAsgvQG1FryomnZhD0wzfW-ZBIE_uNu2GTG8Bv9wVI5zfLu-tmHcJBeiwc2psycYcvfNp9Vb3Vr9waEfBenUdwsn7I8RoduLxzP_sGPj1d0BCzixA9cfUdsVbVfO0hG0QSCHD2eFM7WyshorPH1AeEX4qp7PVEL-0nj_iEEFJ9p-xE8fX0wZnUDsBEYj3mL0VqcAZUWdEq-kYtRtpmdp8C1pJAp3ysTAjpwQyCHj1Ni9GDdqI8y4-iF36iWMGO-Jsr1_EErKJVSNVgA7fEAMQxcoSczNfGPSpLm_HWiWpPxu14oOZ8zcbvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNXukZ70zbpG9rl1CBAXulBZ_24U33qzqVMVqjI6lEH5beyiCSzGQwbp6_CdCLHOHvLwixRqTHnkMd4eUI3RB_sg2_G-F6RrXuPVfSb7g_T0Q3orZXuvQIyTruZ2xUPNqEMTMRZ6FRlr4ORSDBoMdy8510HkkOk-tSVG4eBMUZXfERlaKkjfy-bvQoTVpIuelLiqE9FfFG5jaOsrmvCbNpLmvw098krxOV8E0Lds-TQdM8IF5FinNH028mshbTPqB1YpRA7_lR34NYQaGDoJIe5qgTx4whEo6cHRRFchD6a_JACaXkeL1sRPaCCuWn0iSwMnc98LuCnkKaWsYSipUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjaBSrjWLrjPMwGDXnCXKMgIt5p5P7PNQ6f0xpwElhoyfTWoG8Sudu_QIQQzGXq6BwGYbkcs7T_M_lJRzbhh7M-XsPDBhCsjJfJByyYC2rW84NHCrXnVp3JM1q8K2X8fiNriKBPPGfGV-RuuG7_Lu9I65YPlJR54-S6H_qPp2Wneun_E2vCl1vn5wzy5j4VeJ2QQjRZJnRX1yacyy-WZcMJgnWSqlKltZyJgDyW2EG9r4UeYoXje7Wm0ozih5j9K-BDGzCLQRHVvNyF8lD4JRLRi6nLfNWSQXFTsqIwj_x2t51YqjGhbl90JLu543ZFhJvezZQY5WAIsBAOcvwzXgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuCXR53L3-Cbbg9uYjtY60RKGjPspgxxCQOgoKLeM6ZjldWrQYyYQBvmGWKgRqFgM14tRMoHo-v4ZFpF-0geFebjq-0dS2nwncu48gAveFSxvd-3dSz83PEyk43UAXU5dVj0mEFor-0ZHK5XdN4qWiHQOLkyifQADT0UKMwhFjtTpgKAo7epnVhpquiKin5uH-eB965KlPuFMgnkt7HZIM-vxPVB9eo4nDNEjhSBH8Q6jE3Up4E092MIOg_3nyaA2rveH5BDCGwqxSErDYZjvoqT_8GlbAhzEIQDajPQpTzNRxFMbNhagVrTuULZWO6SWlM6D0m5FRrg9BIykx6UXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0HjEfjKUrbKZEBIblb3KwHfXfwa_R4V6IuIxcPQ4bbkF31Xir-ASU2DFO04GHpdL7QjRYYk9DB1AA3cHpt2fm-6RCOhNSp9LKIR-sRfzaBXaFbs94U45SMBatD3tTPplWfi3v-mJbBlWaCh2sjLAOlK2kawSNMB5Orn5l_rIw-rdnJSGzrklgjwkEPCItOwvLsQjgFXpHG4ZFtOOi8dhmgaumyT7fVPNEP55-wlNQOKOtpTorO3Q4NBxsGZgQ8O5Wx4NAe4esvvoJMzmR7mqBcwlswo7uPppQaw_2EaVqz0-qj4WNvhywEynfhqsry-lOJDUox7F8KPkOsRKGe3fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-PjO_nAXUMtN-4YmFGGq2mefOvtxvViN_9NGSgLT8BcqKuXbBX67Tj0C_TdoMZy4Sc9L8qJNwRQi3Ph79Q7lvWmvNyfghMWfSiR9MQGd-RDDix_czuBZU3hszMusczxq5xnYlivRHni1GwzW91kuXJPymlvMtuann-AX5xqQTsO23n3kgVFuOFGiaFloX2-68wmfTCA-TjnmFdjS3Hy4FI7sfuUR1oFssRUukJq6xRMtR0cjAfqYumz0INLQkJE_--N8gGa02y1nrgJQaWcqwEeIAGoRo5nRHTnKstyrRKZMVIpTNmYyDLQ0VRMzfQMdzP-PRRvxOsrlHPE_C3aBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qO7Xh5cDJQq01-t86oCzmShgG7EYetojvivr4kaCdvXA6TCb2jSvO0vXz9eeJGiFPU23TM4CB47JmTQz7sqFj2Yac2jJYfA7ge6yL5OpF4DYfS1r9yFd2y6G0FnjCYG_Mppsko5unew26QNeAyef9r111TmIKweHy1cvIkUKlAALLWNHsUEFNhnU2tBtfM8kgC9f0U1CN0PiriQI19kqIIJ4JOZEdFF7tupB-mRoSw0G1iiZd9pAM1koURu66vvPn7POgJZKrFqMzZI_AjqtcIyncXXfIv2O3L_ptr0cRml79zpg_yI_2Vm_3cwScZcRBt8vTwIlzsIJXOjZQJvuXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKo6MPytwkRKkA1dIWSYgGMbJ0E5zag_rOwLP6J_SS3aIP3MNH6p7XFhdxrQZ6u1x6SaHNa1_S-9_V_UjUN3Tf8X8xTzzR9KWBfhLCmcje9wR6jrlgX5fzgT5lNL0jZcRvNsgtU8B_NQuLx05JMV_LIssJ6TbmYvuz6Eq6bnCRbmc6-ADTwGYHbDUyqrJ-_ZXn2yZXSiWlUlNoAi2p_t-GApiIxnoa8Yb34h7T1V2LB47Yir6kYfhZ4-7Y7KizqLyWeC5YEk0kJXLYP2VnyjOhyE95KZJ_TJIzht6WcXdLd3MT7XZ5l4ZblslWXL6XPPe7vO76dIB1fOploqJaDKGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBWbl3w1l1yfAk2IJVq9IgbZW_QVIOJ1MOB9RzRRIzAM9Uj6KFgWTkYWb26yCXcTndnHGydki6DYDDTWw4BzGgJQEGzvT3JcWczXqUQBKb2sNnhpwwAUW-XjLuO8Qthm3B2JpxtLL_QTHR2YZG_d-fkqk_2oo40ybV4yCoS4HWsSx3puSBAZu4c2sAqvlWfjEtIyE4AzbTnvZFUfY_Q1XzE8U_Ior3fRuwBgOpBObyoYOBTLWO3uYmN5kD8zfZoyEO_8p_tWhYgV9RU7fMqptATStQSq_j1htBxnz9uvVE-tIeg8U0SBINwsXYlWdXFBxOKC0S8KcPB3KkomsctecA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1vjwoH_a2IIRWnScLD4xa3ykwF2jU5TrOUv0Qa0ZwJNKYf64HWN4UeN1SChpvBoaq8TASTwZa4CcdqUDAbtFipRGDJInhEm4Ifg0s5hprpjlTj6jhF0L1hfv33v4YWGuqpGrR-AyPWRgs-TdWhgtMCFQxY6KlTEA-Yjn1FjBmPiDolw-6OWyOlBvNagELMGbGu-1xhlOTOj-wc3vLXHB799CsEJqNiDmcYAzTb8nqeK_EvHcWKPDx-r4rSIIMl2eJ8NkH7C-uuHHwY61IKahffYKVlOrTSTL7CFRFZ-gwpZfXPo6XlZZz97DLJDBt9WWwW1KNHmEMAjeU2qPskRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQz8ykORiFojnmJ9R-jHwrqLKNcF99olZ4ZZjT1Qtic4XJmUAcpVmZ67hXaMyFO4l9kNx35GxqGPvU19J5u1wiibyYU4zp1jTxAnyB1Hnq2pyJzmMrN67tmNhaFbwevKln8_bh2LHbiDWqM9se3O61x6CCRMnV7JA0b6_VZu1813W-uLDbLl6zQhb2XJGZH4Wfu6vodomU8LFAynk8AD5aj8A4nHAGX1YJ36tv2uIQKiExm4VoeKxB9t62jWJpV9SXOzr_G9uVV0t9X8J_DkyUXankww9j66OaBlyJTS9qFfoZD65NpFJMcXXmaBXvU3EhsVwfQQT0sxIuoOJJtT0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7i_IniE28RmMG-FsmfXjBjEAZGYP5j7_9K1sxEpOUbZ-2EvBZ9LzoQvigrgEokX4APEX6ZPTgf_pyFSlUc95Gyt95ejKt4d-tQ96H-u7YmQn1tgQXjCJ9Pe0oVclFt753jI8bIEpsMQeUJH3rG5L1KNnyKyx7R7loCm3Rp9xncDMdFz0InHQjCBkDXgnz4vmuABU8Q97aOr-fP34z3VIngHaiKTqejLotwsbAOk5c-B08hMAqX30GSy5wZDe2LEUHgQb-nPQEGalTOHp2SRu4EIEDlRV6lFvgCdj_hhC54GoESgqZkucUx1G2CO8D1BzTN9BirJS4pNKP6CKHT2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpVQJskZu67ykvTjLukrNxP12p6e1fLGAN0JYXl8gpYs-Qy-tTLkPxRrriYl3wL3wA18n872LKsWJSdQgV_SDUHXkGsD0b_x06J_PgtWABaWtDb5wO7XqCpw-_cXJVjYl-5qIsMaYiZsIEtWs9xuTejgF6t49VnZnbbzUO7HEAKrXMaXizv6nw8sNA-PvHnAIqDKtP5hi1RF1ylOeiRw4KcL7M9W6uIFyMxJnzojuUuO5A-0uuaudVv_ziNCt2uTxgz5rUbSWl52RjcnWpUjaBJG3LmnCCgCrjOSY3kJauCT-SGCKtJMVENQufKOlw8uWXITNrOxDd0r3J_1eMXCKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXjqMX1JLShBK1qFELYC4jhNea2DXCgC1em5GxPGHXRAyeZn5SdaTHqprv2AfRdnd-UWejs74lAGacqiQO8v51Vae-r1eS__YeC2RQNSLIcFqaM0uYbWtcCXfcAUJQPLE0nQ-zSBzICmXgAea0q1X4pAdN57KlC6MvRe-L0MS13xAk7f79zbxv5RluF_G8ADEaYP4DEJv8L7hb0XYVv4UK3DohbKB26D4iK1ATLXZuJj2j49YXU3TmjdgyI8uDLy6ooKUXsMaapIYW8-9k94N9ZU6-V2wGHdYb469EYQOcCD_I61LBDpSghMYCYpUrF3VBk2LbrT9lMEs2oP0WUXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVzvegTL55tcxLEXTwecuWX9sB9CCTtkKMVFA-qbMDAmRH9PfjYhsqsVXkIHvMZHAh8DsKcj5IzhdibR-ZyT6hh21_bcG3l2h8D150Ii8Lnyg6LtOwgz3Xkxgs2S2yqwNFcPd2Z5o3WFyt89Kzi5zL80O9myEBvwkVxI6COMZ1PHrftW6ZRGvdAr4IEggaP8htmoSUW6xD4dKvaTibQTbSv3SOUvU12ldwd32ahCMVbTCzXQs_lWh1aGYJErKyN3rn510CRoAzTIhPZCv7P7OT-TzEROOiA0T0Ytj-YpGVTqgQE0WqZ1ghwPF9sSUM2xnt3yot28chzSYWR2NrbHtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX07TA9ru0jcR6EYtlI7kXOUPvhsgvXmN4Dd0iOQznqm9Br0olYyj-1Ht-ePAzXtWVrVpGEDNZqMRMo_cOAb-eEGCA4pqweI-60Z12vDOWixesyNOsAsFHt-pxl3mlRQNAHu1pab2_3oi3HsyzmMkCeDMCJn-0geq0Pm_quQHyCM-NBm37DdViHzAJJiJFeA2xnU7qan29j3J-2plxSxRYVdc0mKi_WxV_WrNY7WCCfSatoh54WLj1vDQVHJoje9-BDDT-7RO6j73tygUC6wKHgzvXuKpOLNezQc4fkgXXKL1mUVh2t5cROvDrV1qgDznrvQ8rGneoL9h9cWeJ2f3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXAIDIaYuri3kArqu_SiUdpTvRiZkC_aKvpUx-FwSAFdQ87qMtnW2dNzhwi9FU8vp417rd0bVAAVOwn8kd68ReBOKfrRqgbHk154C8h3Odbzw2UZofmze3n3ks0iEEOXQgmKBjRRPfXGvdntsYfHf67vMgEX-vJ5J8T1Y2BhiKilI2jnTlnQjEcMAWdppqtefIEiB8-gAnopz201C1aD0MBBlpNgPdUbvY4a2N4IhfP9lf-n1jJaczB5LFSZhF3QJKhMc_WGaRXBObQg3sbOKE-NLRlfXgnP68-WJrwDmMm3GS22tgBEc9O1ad8YvqWYsHsZ7OjWK42ZYV8gnSRAXQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scF5-AgNdyZc-L_eMfipNvhGgk_5R7kb0imewHK1yJg_Anh1cY-O5XjGuO_O-FAbmT8EgbnDfMFc3uRypGwow6LmZmzpL4n1zcGJiVPJ26SWHX7OgXy5J-s9O0JLBu_7xZW97m_32zQobnvlVK2LYSey5NE1_Z5XO7RVTnAc0YmNvbj_HizfqHzkZgGVCMhzosNw5tJnJQSLkWc9LSWTcQXKzppry4ccCFQn6XYLAjvLLFV5CpZTKzhlrb2H92qiLxVsCecDY_V6aaVJhuyPwwp036FuxAKao_bkTkR6eFMfeJicE46_FsWsrH56YDAGjRUhrWvm-zkigXVDK9YIWQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=jOonG_BXqwPqyuy2x5VLx-pfM5jM2Gu0b-gAwXR39kGd27EZHya9MuxS61vj1ycFEL-2CQyTBA8VIjguS9zk5dHZYhzUSkZe-6JXzAyS7MgdTLad-d-1J1LaEHwFP5LVTyrFgwbviLQprFtMhtFl8JP9R6vKfDN_yBqGazTaUY0DKBm0zwjKHLRUNsiVdOcDI3LcEo-YHZLsvkJ5ohawJGo6PEtOiBuX65f5dzxtac_M40jwom6Dyui9K6DiZkgF1-lZusG_fzC7NR4fJi6C3SDnSkUHi7i6sRtOCw9d6UpEzJyI7xTkjTU-dJLst_qwKzRdDt4W6OwpGRHjg-JCEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=jOonG_BXqwPqyuy2x5VLx-pfM5jM2Gu0b-gAwXR39kGd27EZHya9MuxS61vj1ycFEL-2CQyTBA8VIjguS9zk5dHZYhzUSkZe-6JXzAyS7MgdTLad-d-1J1LaEHwFP5LVTyrFgwbviLQprFtMhtFl8JP9R6vKfDN_yBqGazTaUY0DKBm0zwjKHLRUNsiVdOcDI3LcEo-YHZLsvkJ5ohawJGo6PEtOiBuX65f5dzxtac_M40jwom6Dyui9K6DiZkgF1-lZusG_fzC7NR4fJi6C3SDnSkUHi7i6sRtOCw9d6UpEzJyI7xTkjTU-dJLst_qwKzRdDt4W6OwpGRHjg-JCEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQ2Sv3pH9i2N1odM2kyXut36EuQB5as3YP-6NHD90FKtJRc10aP1l3AG_AOqXIxispO635AgeeUdOcOAPfqLM6ip7IW9ZiYGemslVtLTuPnjc-6iN2vqWeoi61yoTsuyWxNd28-P7Au3824Zp9ni5Spix-8pQ-U0lSKZGVwMXjMM8f_cYYoFjLACqCvczPLEOyxjC06CRBjvEHKhRy2LclK1o_IyGpEUc4ELZcmgGqMYP13Rv8fthInZgWR4JHfB4RK0GbQERzmKbM8oJZO5cVnElUc_TLm0rfH8RqsqJHa2OVPmoqLUPvGFgLC-zC3A6yVtpW_eMo7LDd_ndTH0Hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=lUk2g6UjDQeZec_1Bw7iyDAYKMfnANclVOYwweir291SNyjB2JwGCoAQhK3ULI_mcSSZEGDo-_H9bkqS9qkPwdVrFG1obQSbI3j3HWCtKOwp9FT2d8BB_JunBA6PuInRf2Naz96P9JI4JK6ld1pw2yjIpQNuRqA9jR_MkiHXd_g0mGW5jkq1s1rx1i3O7Q8ic7F3NiWlJloyWVpvo6dwV_cMJJIeCgklPONlEDYNPnuLAK2a0XhBBIdMo6dTMLSu_D3p-xU3O-iw8cuxxsX80c_vkqqemiPiwIoF5vX7s8iYom-2FILyrsMbmne0kydZFKk0Kc-43cq1PP4Dq14Sgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=lUk2g6UjDQeZec_1Bw7iyDAYKMfnANclVOYwweir291SNyjB2JwGCoAQhK3ULI_mcSSZEGDo-_H9bkqS9qkPwdVrFG1obQSbI3j3HWCtKOwp9FT2d8BB_JunBA6PuInRf2Naz96P9JI4JK6ld1pw2yjIpQNuRqA9jR_MkiHXd_g0mGW5jkq1s1rx1i3O7Q8ic7F3NiWlJloyWVpvo6dwV_cMJJIeCgklPONlEDYNPnuLAK2a0XhBBIdMo6dTMLSu_D3p-xU3O-iw8cuxxsX80c_vkqqemiPiwIoF5vX7s8iYom-2FILyrsMbmne0kydZFKk0Kc-43cq1PP4Dq14Sgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKgyXj8ePwO51UMdlZ5jjXuNFZhNNOhnFOdP_AzEsyMdyu84c_9xmvVwQ_qxHCz-zBWaKm0fvyV1GM340lp9gzX5ovlwy4XPCuU0Aegv6y2WAojb8Q8Xi7BI88OaInF1jnlW3CAXd-wq15SQzKbM7JxDpxOAPAN7tumETm5H4fFgDNk5nDosy0_5pciJ3HsX6EXc2xg9X1J9u5SilMiWdDb0YEz3CvMxQWVLIRS6TR9UPUqv3GQDeVto7S3A_UWZ_Y6uIR0mzl9S90qVaBsPfA7vgPKZ7h_aYlYfK73VHqdTtu3O0zUGQ6G9fcZPJpqdfMdRzhEONPdOz6Oa7T7zQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn3Y7bLm6nVAMRnpTtRUo9kvsw4FvH7xt7Q9SZkgFXhnTF9jQxIm6DbNMtCbb0sfOvmBp4E237D27xurSWeAPeAn6PyLE_bvLSaIiv_mfkfobQ0hdWlAr5fKfkbz3Rwj67HTzEpSo1UPDzV2f3QYUZqrnx-eQZAEelbWu1S0CSkxrJmQUmYeEQpqRfcGXZMlWigPe9gQOjB59RA15mqMCaKg5vEreSA0exf07P6Zpw8kr3awRsVv-Ru94ZJACJTXfuI2VEXqocp-n3NZrdFacHiveFgYuGCmDs_RDPu6VbrH1g4yWjayDPxoBOJIK0juzQW0RumA-ad4r235CBnRmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=qHWjQ6UzVLiMP-YHZ3f_QMOIm7DeMiDZy6b-9K002Mb7DK3Q_h3S8hCEpLfeZNgtzNVk7QCD90AS0kMX_Ls7fxQl9Jqza9Ma3mJSFHcjdwArfpvOQ7tPZymVMlrFFCkIlJaCuXGlSwZU362qnT3z6Rdzrf1mPxCMdUvr87eMK3hwfW3craECqHw0ucTMYf40OduK0dbnKTEtSeCKF6_9SB91tT4ozyMd6PXow4BI5O12XgnDNMNwwRdj4aUH60BH6j9_RpIhuCUR4zhDxPyHvk4-n_WN97vBTnkt49-Bp0CHAtrNN7W16VSkWiANQM51bYTzxXNfbx2kRTBem54Qww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=qHWjQ6UzVLiMP-YHZ3f_QMOIm7DeMiDZy6b-9K002Mb7DK3Q_h3S8hCEpLfeZNgtzNVk7QCD90AS0kMX_Ls7fxQl9Jqza9Ma3mJSFHcjdwArfpvOQ7tPZymVMlrFFCkIlJaCuXGlSwZU362qnT3z6Rdzrf1mPxCMdUvr87eMK3hwfW3craECqHw0ucTMYf40OduK0dbnKTEtSeCKF6_9SB91tT4ozyMd6PXow4BI5O12XgnDNMNwwRdj4aUH60BH6j9_RpIhuCUR4zhDxPyHvk4-n_WN97vBTnkt49-Bp0CHAtrNN7W16VSkWiANQM51bYTzxXNfbx2kRTBem54Qww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-Hi15pfIcJkNRSfLrw5Pw5Ssa3pxJsbWnN68iWW9dVelTXcdUz9mmC0BPhmT87DTC1hDjKlFZ132y3vlb94_Aqqbc0OZ4w54_17eeAwQZxJ_WDc_ETza2btvAcxQAGajGxDQ6wNyQVF2-UV0x70pR62Niz9ECIFMPXghVHhqA37EwpPhBquLYAdFNzH6O2CuajyO4hvtG5tfYDIbJZdyCYfmK4SQ_tXGaDyD9MXlcXy0gEtUjCUw6d_K_uOzfNn5THZtxyuRyTgTxV_7xZHsXLu_pqUnZjVbot1Y0kPbj5r57qSzerVdiE3Z5EJRsbncXanAap8YhdTqbPDe5rFVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeXHZsK7p4DivWPn55ipC4XFU-9YSxtBNWgB60t6S9YZFSW2oWlHEP2AJzFSelLQUz7mFNtJ2i_6QoIugIdFQo2NoS5ZKx9YLJag14lQEGvx5eTD_dt-qpAUB2-BTeUshBDulxZhrJApszwxGnDiOgjVBtWaHTyp0V5jVua1lr_S8CBCpPo9p69b13VpLCJ-tgbmbzNJ495z5vqor7a6eAgcyqdgN-QnnRFy4GC3-qY3W9MSpyI7j_IVTJ5zYMD_D0jGlR-leRxrwWTbV9KsqUJ6FhxJh8vIK_6rbH4A_lrvO2rjCtXWrfxX8OknTcaGNXlK1Y25FRyS38BPLKkT8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_49L9wQvv4gHbfxM2h2ewJCHBCoVXrqXDtxt5CNRfFLMke7aXcnhl3i_M3ZmQYyymRNugV5lQ4IDm5XLSuo2STKuXvvcUslHGCUORY5uBZ14-SwACtwtQGon4KjCdJmHdnMvk7MLRuS0wm63v_90fSkBEfFvqNFLI_ZXOohh0f6h3XZMRMuFxAogHZiNjH7_DebjkMfkdzOXcM0QNNEPc0Bkv2-HI3LKoC7A1mN_JlTSBAR0Xtnllc4z5G7bYbTrK7bHGgA3hcveJLvs18LFdPXgSDqJDy33yDR0d1WFZ25q_8f_YiJKvFbJEpXxTh_nnfbYakFmusAJY09rzseig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=vdSpFti_szzE1hX4jJrQPA1uLFm09_WuZ8a9cN6KeuCzi29Svn-OU7bPLGAV0obKrqu7NDurPqV-bYzrxCrX6FSKpvzHeYSlLzsfcw47uvYowCqvtKvcq_rBNowkULZYn3Y-qzXs1cuNJd75nm_oELfGuWNd8lzMhmsx9bdT6OEkT5s56a9bVoNu9CZFrZkvwNZoO6aqdSiAne1nIpPwsp65zn0gbWkwLLae1ydfS8hyeZfCL6IpEfDTkfPJDDcuBvTqnUbbCPLzrQkPFTeMjVhzKF7FaQ1wvXunCkr4iZ86O5XyFHuY2fdznaW0sE7Kmy2Sx7v8kCD4yw50zt1oxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=vdSpFti_szzE1hX4jJrQPA1uLFm09_WuZ8a9cN6KeuCzi29Svn-OU7bPLGAV0obKrqu7NDurPqV-bYzrxCrX6FSKpvzHeYSlLzsfcw47uvYowCqvtKvcq_rBNowkULZYn3Y-qzXs1cuNJd75nm_oELfGuWNd8lzMhmsx9bdT6OEkT5s56a9bVoNu9CZFrZkvwNZoO6aqdSiAne1nIpPwsp65zn0gbWkwLLae1ydfS8hyeZfCL6IpEfDTkfPJDDcuBvTqnUbbCPLzrQkPFTeMjVhzKF7FaQ1wvXunCkr4iZ86O5XyFHuY2fdznaW0sE7Kmy2Sx7v8kCD4yw50zt1oxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=FYOw5ZACnU--HfG03vlJI8bNc6mN_eyR6kzKOPZRBhj_sJk1OvV6QvcXkyIu9xNgzCes8Y-rHV2PazEDk9B_fTR0WU0PT0RQV0Ec6UQgs89_pHGDFZOXVJ7freUMeX9mFaVdCV2ffVJqZJZzBIpEUBL1andjbEmCfdH6rVDBF9a88OvWCrZw6R8Hn2_IexrId4DHYB3Le2uX8DnAGIg_K7FYuBQpuXDQPFdtdHFHumsj1WBl0RJqBa2WAOBhQYNE46J-V6t8UTb5-ytReru1sw1rQeBUsTjcOYLYBpT6AMZrOUlXqEVe11P9rjpF5_yyRo0QaWWR9pXQhMDMwebgmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=FYOw5ZACnU--HfG03vlJI8bNc6mN_eyR6kzKOPZRBhj_sJk1OvV6QvcXkyIu9xNgzCes8Y-rHV2PazEDk9B_fTR0WU0PT0RQV0Ec6UQgs89_pHGDFZOXVJ7freUMeX9mFaVdCV2ffVJqZJZzBIpEUBL1andjbEmCfdH6rVDBF9a88OvWCrZw6R8Hn2_IexrId4DHYB3Le2uX8DnAGIg_K7FYuBQpuXDQPFdtdHFHumsj1WBl0RJqBa2WAOBhQYNE46J-V6t8UTb5-ytReru1sw1rQeBUsTjcOYLYBpT6AMZrOUlXqEVe11P9rjpF5_yyRo0QaWWR9pXQhMDMwebgmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1STMdlo1O2emRC-Eh8n2Y_fvPWbXhI1prnQ0j6luaK361m4Qc2qF6HkP3MB33y5egVMSPOvxP32CwvVZ8p1vYzyvoiLm_6GKtSq4WQtT4EqaSjb3APQPY_htlTo310iT9ocuWBvbPommlz1ZQaBBw4ATd7qg18niLwnsPQZKxuyyR5_dhAEO0RvhFqyBO5QatSfE_VWdVaY_tTdRdX10amIsv611LEZFglbQjmas_eYMfCR-uZNUH9-Ni69aLKtACAZK3HgT0xpVFwyFn_Ot1dsBDBp5iaGnnIzo-r20LG4A_l-_W7HmTB-z4J9WqhsB77Zoe9SyVh61li8aBqpwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-A6C0AMioa-7rY_N-xjNlVnda5LJsdot6uH7CW5qp0xzbXNrUl36We4FmKbmEfbBA0WR9RG0_e0Z_G94mVqPBiCj3NA5Yejv33h7HISET2j6DKYFucVzwuMic7gcu-U8TiORiyiC62TDrguD5Z2qP1tsv2pPsBZYuh__t8Lfv9Faq_1co0wSo2tbx6nAfvbf79qLmzeFxaQhHaySqeYiz2ynn0KF5BuS6tINMJNqqoVtP2to7KpFz3pyE5PoBQk9FjMPoH8AWB8gdvcpTy6bMHNQqajeKsiIRYKvCS8M4ei4grOTtMNp47PBKFdxDWyzBytCqk7ylmOhICByKW_DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf4aBZ5_SICIsAPmE6dvKEMhfekrGOwNfKaxBXDfrX5fG5X2yJASmxy9sUmiB-zBHYNjNf-Row4UKP3FPVaeFlP1mT0XXI1k1xttyimLnxu9lcuYh72RXdpDbKz3qLfOXDshnza4xvEqDf6sN0vDaaGEongT9-htZZYe8I51rcyNxPJ8X5-V3LUyO_UwcM8Y4tEYVP0U3suGHSkrskeQWN0n8eTto4eifOUE62a0mMyzP7pNYbxK8AQqhzTVhrB9owZJSU5HmsQawIav-VUcw2q5zXqhaTWRt39CIZIu82IcBjNpqyMEQXu9fslrv4mayjlxPr7W3PtknUgddQ-wkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCrBtcBw0Mh9vZbbsonMBy67jOFVzyJx5wq9V7b8-6NqLWoemnyn61Mk316oeFHQzMf2Svim_HMzMStedx5uuQTK-pUOJP9usgAqLotgldoZaym-MuHSYzpmo1-yP1EN0FsYA47FGLc5agg_bEqNf3dvoWIQ04nhDje_QxnPittcKQrNXQfAwZdEGhTOxbDq-KVq6MUFJ6v-wg37cyXxxhjQJR6S-hLCcmyaakZwIs39HbRrRgwDEz69ALFhGERlK9CO6b30kMZXbxgOIt2YD8rgu273qLmMQ-_XJQXmQnNP5EeUFBrgbLnv_eVQLWev7gkwWIAIFXSBy_8_Qd4T4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SKyHnCmiVUFUNq3ZNczFfDUN3e2_FcT99zbIAfxoPOX_jvyIOWkGIM8OhrZDq4VkcuXm8mS-C1D67vK6Wy476nxoJ3RSRtS1s-7SwkuSgR7WufJM5Sof2-zBkGmZLuUIPjAdWvsczL6mIFcKXLypMNN141Jv9Is1tQ1q8qjWd0K3xnrSHglyt8ffOTG7k_eQcx8MPnd-WuuTm0hpujImPskVZTH-IgrcSKTVrpDpC6lMEhWKGkL4T_vjD-6QIj1rhEybfj7f9PcwetwGlKjnjqY95axDbzOWZVJYufFrk4yc6W2WICXYXHY7rNks4nz7ceuAq3N13LNQ_9JrkS-Xbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYaMsN7nzBSXa71ECG2eSWnLQHrs2OB0dRNVJRHlXIHgrdG0C5KsJViaL59celAPKwoqoyPeVZS5jQSITSMrhd00ehMLW-ydzlrpvEdoDhD_aqywrSuUjBjRot_9iSZ-nxhX0fTn8HtAXympfHqug07Q63G7sW3FLnxJoQ0DB5GTtxPn3Fvv1VjOcub0pHBUgnhe-MGKBE1iiRm80XUKyfBb1Kh_EBUP0Vd3RHobCvGfX8va5Uw0SBtylS77r1MOIgvoUuBGgCKdDV4yWMzPaYUIkYqHr1_Jf30pr3_g_Cj4L8YhIYyMmp6g4l0x_o4581ILPOlkloA3mAxvSXf_LQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT_97_3HAiM5DSL5XOqhgrNfBODQfLfdl-XRwPh66dXnEdq5P4yvM-ArFzWg-23wpg6s4KhdLlN89RudTIftmNmQNm4bBNoucAgbWcGX8p51cfviqZ0GUPGcgW7GBc0ZAONn7SlLQkiGDT3Lv0qAeYFK5sUhoRDyE4da81ZgMh8zcak5R_-nh9zlsvrSctF8W_boygfpqIUSo9farKqr2-EL2mpm4Zq0e7k2aTeu8lrBoAv9Asb8YarXCfUglDWevV0zbmorcxJ8gb09gmaZgtwPSlPGqMGeJPLG5rarLl1oFn1wSsqc-rqNEzwksRyhmZKaaDEofKoRbjpkH_gYGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=iQvrZsAQvpCnAZWT4oZrjfa1okwmCAXj5tIQA2K05Ha-Qmr3oAON_mpedbrRWFk3Np7f2XusTOIILZ3I21NQ8I5PKoXd86xt_l0gVkE6fW4Po6k_-h3YLsjwe0lMiEMBeUPl2Fccb13Z4dt05RXJ1ZvfCkMsC0_WFPLBYDJpcBMStID7FknTShtISswiaqIV-ZbC6gzlUCO9MOBT6OAivGnL5bhnSDgfKfj5cj0e826t-S3xzXk_9YiV25RqZ9gyMOUnN0qUzVJlkZ2o1uQdQ87KN8vIKCLjVrwXukqVXSA5c8emSFhY7QccwULeXYYXd3KVqXUhKt84uW305tY49A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=iQvrZsAQvpCnAZWT4oZrjfa1okwmCAXj5tIQA2K05Ha-Qmr3oAON_mpedbrRWFk3Np7f2XusTOIILZ3I21NQ8I5PKoXd86xt_l0gVkE6fW4Po6k_-h3YLsjwe0lMiEMBeUPl2Fccb13Z4dt05RXJ1ZvfCkMsC0_WFPLBYDJpcBMStID7FknTShtISswiaqIV-ZbC6gzlUCO9MOBT6OAivGnL5bhnSDgfKfj5cj0e826t-S3xzXk_9YiV25RqZ9gyMOUnN0qUzVJlkZ2o1uQdQ87KN8vIKCLjVrwXukqVXSA5c8emSFhY7QccwULeXYYXd3KVqXUhKt84uW305tY49A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=ksk7NEJfw4p5f6yilfKU9wQYt_acaOjpwwG6IlTCUjVbnbsRu6gGa9-NyzEM3yJtsgG0N5AEUlf-u_4S4Z45LjhqbIPfh_QGY9cKrbNTK3b1DYVeD_UCRRC0DDulZ_5IXoZocYcYlwX8rLjlNYgtDk1xn59KkOeZYNhrYRgfhMTtCAYmGW71PocNHbSJAGY7ho3DusFwlDQAaysdCBVHXZcpJP6ehbh80YP6el292wpfOmA6i8PP4aECNvmbWmTZBGfn0JAiQEBYwCaEZtG3GfzLVa8LQ75tCPoTCQDH_cYasQonKkJUgVhoyB2iBqtVAcDt35oDFTkghqu0TVlexQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=ksk7NEJfw4p5f6yilfKU9wQYt_acaOjpwwG6IlTCUjVbnbsRu6gGa9-NyzEM3yJtsgG0N5AEUlf-u_4S4Z45LjhqbIPfh_QGY9cKrbNTK3b1DYVeD_UCRRC0DDulZ_5IXoZocYcYlwX8rLjlNYgtDk1xn59KkOeZYNhrYRgfhMTtCAYmGW71PocNHbSJAGY7ho3DusFwlDQAaysdCBVHXZcpJP6ehbh80YP6el292wpfOmA6i8PP4aECNvmbWmTZBGfn0JAiQEBYwCaEZtG3GfzLVa8LQ75tCPoTCQDH_cYasQonKkJUgVhoyB2iBqtVAcDt35oDFTkghqu0TVlexQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=TvN94NvmA3LBHhrFoMz8BatlDOuUZlWnrOEj32geGoP8iiSVmn0VsSDGmf6nRzPVP-LSxqOqDL-0UyUKrldWg7LBWjrXeux4ws7gPzmUTLGCYJXMCF3ZvJIaAHZONjAbsIxN385HxbZuZJ97R6_iJpedZfWALEsMwsh-u6JSXZYMbzVOqYmNxixZqYYXG4_DvROTiWQW8_1psqovKctfqACtGNS_dm34C30lamJdpYViPxMJ2fi9DB5S0EkFRcV0FHy8E6WxgjRfKFQaOfQBckpDdL9EbtcRn9mx4rRsFMNCeT_Selxi33fviODCvPFqeLMxMlJfXA8bQxu7a94bXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=TvN94NvmA3LBHhrFoMz8BatlDOuUZlWnrOEj32geGoP8iiSVmn0VsSDGmf6nRzPVP-LSxqOqDL-0UyUKrldWg7LBWjrXeux4ws7gPzmUTLGCYJXMCF3ZvJIaAHZONjAbsIxN385HxbZuZJ97R6_iJpedZfWALEsMwsh-u6JSXZYMbzVOqYmNxixZqYYXG4_DvROTiWQW8_1psqovKctfqACtGNS_dm34C30lamJdpYViPxMJ2fi9DB5S0EkFRcV0FHy8E6WxgjRfKFQaOfQBckpDdL9EbtcRn9mx4rRsFMNCeT_Selxi33fviODCvPFqeLMxMlJfXA8bQxu7a94bXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=Q4tImKJxpJvm0F5j7geo3zbUg6eIcFqMZRZgIgRFpl6Q1gKZBxvX3QPzxwDfvqQqGdJsSe6Da2FQslP16mzfCgQwfYHM9DgurD1PAy3S2KDgzQkGcC5_2cqJKHLy-Mz54AOQi_7wVUoZzNCiEVOSLDDBpkKcWOtXE-SFO32EKWPJhp7F4J-5xu09VPcf1MNfBiEN_Xm2heWFXvSag7bCcKhOZVU5lgz5C24ErX9Ut29ZG7e3xrTyWFN17Zh6w-rHKcnlkYGoa_eB4t3xtI0MyDVzKkv0VPRngjHLkKdLEh_cZWsPFW0QPC2a7Z3_TAb5FuNrbVUHMJS1b-yyfd9qcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=Q4tImKJxpJvm0F5j7geo3zbUg6eIcFqMZRZgIgRFpl6Q1gKZBxvX3QPzxwDfvqQqGdJsSe6Da2FQslP16mzfCgQwfYHM9DgurD1PAy3S2KDgzQkGcC5_2cqJKHLy-Mz54AOQi_7wVUoZzNCiEVOSLDDBpkKcWOtXE-SFO32EKWPJhp7F4J-5xu09VPcf1MNfBiEN_Xm2heWFXvSag7bCcKhOZVU5lgz5C24ErX9Ut29ZG7e3xrTyWFN17Zh6w-rHKcnlkYGoa_eB4t3xtI0MyDVzKkv0VPRngjHLkKdLEh_cZWsPFW0QPC2a7Z3_TAb5FuNrbVUHMJS1b-yyfd9qcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=GQ8azilWskQpqNLmJKsH_lcQOFoO2_OGRP9GA9QRXaGvNE1cPBFZtXc2cRgFCjL8N5OB3EbhqkzOby8U9W41TQokPQbldaB6ci0INsEiSS3lAlQHi28HN8LIGaI8NBrZwnMI4_nUwwTpu-eLln7fnTTIrkoxWA2xbWmmG0kXCSx8a1v9TKXnb4dmiKz_-d0V0pp22F3MIdg-2P29bmbazyKBD4MOfZF_Pfj5Np21vN78cn8gMbjQ9sDaLyNsE15C4JgXhedn8ehIJRdDpoC2-6Kq3y5SuNUYhVeJEyq4v4oHTPx3Tuk-WPj8Vf2PbSLN0LrkbSSgWUwCt_2axKGqyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=GQ8azilWskQpqNLmJKsH_lcQOFoO2_OGRP9GA9QRXaGvNE1cPBFZtXc2cRgFCjL8N5OB3EbhqkzOby8U9W41TQokPQbldaB6ci0INsEiSS3lAlQHi28HN8LIGaI8NBrZwnMI4_nUwwTpu-eLln7fnTTIrkoxWA2xbWmmG0kXCSx8a1v9TKXnb4dmiKz_-d0V0pp22F3MIdg-2P29bmbazyKBD4MOfZF_Pfj5Np21vN78cn8gMbjQ9sDaLyNsE15C4JgXhedn8ehIJRdDpoC2-6Kq3y5SuNUYhVeJEyq4v4oHTPx3Tuk-WPj8Vf2PbSLN0LrkbSSgWUwCt_2axKGqyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=ZobTzTpVgi0kXAyJEbn0-uzjhw3I0ZDJIUr-IFxYEhcvx84Oo-Ym5CGIhcWioxcyDiLM1ZE3s6MV9HKoQA8mF6MRrPJzHxcaly3Y9niypovATdvF0uz4gW5kuxXf6VnQjyjgz5QsmPPSKbzsAkiYG0IMY85PDFNDbfzNFx4jdE5KzzMTuSmYhAl6qaUFSwbMTXE5Lj8SFuFr16sBoSTOUGuDzizhUjr-LE1GYgnQkU6FUnYjwsQPySB6Kcob9LIP3fXUPEcCXvpPeAvhR45OeVS39zfBdpY9bBCquwkWMbNZG17pLmnPGmelc9gr7f_sE-6NvIlP_GVj58hNfHrbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=ZobTzTpVgi0kXAyJEbn0-uzjhw3I0ZDJIUr-IFxYEhcvx84Oo-Ym5CGIhcWioxcyDiLM1ZE3s6MV9HKoQA8mF6MRrPJzHxcaly3Y9niypovATdvF0uz4gW5kuxXf6VnQjyjgz5QsmPPSKbzsAkiYG0IMY85PDFNDbfzNFx4jdE5KzzMTuSmYhAl6qaUFSwbMTXE5Lj8SFuFr16sBoSTOUGuDzizhUjr-LE1GYgnQkU6FUnYjwsQPySB6Kcob9LIP3fXUPEcCXvpPeAvhR45OeVS39zfBdpY9bBCquwkWMbNZG17pLmnPGmelc9gr7f_sE-6NvIlP_GVj58hNfHrbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=dES5fMfZZ5cMK-nov9QSzRMbDr0vnZgnqzWI23b_LPeHTxvoNoyizOk7SHxMyj9w1hVr2_wUmELfnnErFYTbQxSQaT48fnqIem0hQwdRJeLYhjiyI0iisGy0-5KiTutH0wfpGFRZ5f7gEVtRO33YZk0uUof0cz9a5d_3Et7Q3bl5q-fLRq33dKbmVMmm_HI2JUCipfisIqkNg2reVRpluPYsmZ_qBv-zXkXcG2QfPH-P1VOH92tb1k0mvMeQBfLuPiYdSZDRA395jZHrN6LHn-0C0yRaHOjK7heJgsmz54EQ4D64V3Kv0r2MAmv_QFF4TMAA61_lR1-b9P5BJm2VUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=dES5fMfZZ5cMK-nov9QSzRMbDr0vnZgnqzWI23b_LPeHTxvoNoyizOk7SHxMyj9w1hVr2_wUmELfnnErFYTbQxSQaT48fnqIem0hQwdRJeLYhjiyI0iisGy0-5KiTutH0wfpGFRZ5f7gEVtRO33YZk0uUof0cz9a5d_3Et7Q3bl5q-fLRq33dKbmVMmm_HI2JUCipfisIqkNg2reVRpluPYsmZ_qBv-zXkXcG2QfPH-P1VOH92tb1k0mvMeQBfLuPiYdSZDRA395jZHrN6LHn-0C0yRaHOjK7heJgsmz54EQ4D64V3Kv0r2MAmv_QFF4TMAA61_lR1-b9P5BJm2VUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FQAKAkvylyzsceSY_vIRsCq8esf64UDLKAXhCEKRf3H0X8yutaotfSqG7xPuGvq7Cr5m4ejHqOWYGIS-tzq7CAss7dg71IEPe1rEkyQQCMDRsFBzNeaFmT2E4S4KhX_Uu8F_n5PDleF9SNjLgzgWofKDL-eZNJFpOeRX5_noe61xPoLcenv1tW4XnpQIxgG3lkEfIh38tjxF8dZzLCD59I0UqLZLgWynsAm7PRYEy4n5fdHoA6_Sn5PeXHYKLr01ev0uYI04PGA6C33aiDG9adbrrCao2wsgJ6E8773B8HZHnStnziOoplgDXySRQeavQznUWFBRGb1kQyJ39brubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=Lp7m5nxzbTX1RUtILWJ0c1iheSGHamFOMaRhmTaDp2mMdDOg0CVkQ1LCCwe-qUd_bjC4kpFDHfQYSY_GWkusrG06RAoiav32DBIaYJlXp7drUYewPQcX34HMwd6u6fIzzaw-Owywoe536l9m95CPNJoOoeMA8V57c8kMjmrqPQfaviXa6FXeo83VEewG1j98hz77E1HAJQNHVn02UQrQZuyFIMe74kIJ_z8KK_VCM6_d87dQqm0mAgG82rGBHkw5QtL3LRSKUDnkwNlt-TIPPPu-t4Qfv7vOtVxLDSOrzv9o9J7bc5CrvrpNT8Ke7ALdBxPa28JY1ktyFE9Mq8X5_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=Lp7m5nxzbTX1RUtILWJ0c1iheSGHamFOMaRhmTaDp2mMdDOg0CVkQ1LCCwe-qUd_bjC4kpFDHfQYSY_GWkusrG06RAoiav32DBIaYJlXp7drUYewPQcX34HMwd6u6fIzzaw-Owywoe536l9m95CPNJoOoeMA8V57c8kMjmrqPQfaviXa6FXeo83VEewG1j98hz77E1HAJQNHVn02UQrQZuyFIMe74kIJ_z8KK_VCM6_d87dQqm0mAgG82rGBHkw5QtL3LRSKUDnkwNlt-TIPPPu-t4Qfv7vOtVxLDSOrzv9o9J7bc5CrvrpNT8Ke7ALdBxPa28JY1ktyFE9Mq8X5_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
