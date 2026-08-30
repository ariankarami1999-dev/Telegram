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
<img src="https://cdn4.telesco.pe/file/gXis_16m0au0RuGBYO4IcdNp0Ho763qEt4zIz6wAG5tR6KaltplcwEB-eI8DpG3tpBfYpZ1nU6skjaSqII1N4K_Ruhp2blD88a0hWtn2DLDgNy-K1G23eJFyU8r_aA7IQuECaD9zDwSnzUmB-0p-BimhxgP15AzGXKfq_EmNx4i9WYTHp0ncPHQ2MIZj_MXLfvkV0DVYN0rCyW3vfSjkRBWkiU5wBRzUwqOXgQndDGmPpHuaCSIMYDKB7cH41ZECOiVOmw0EC95K_szY--nfjL1YYBn8alg3_heNBVcGdko6nSesIJZkCTp1gSCpD4utXs-zf_eAF32Ooha9fSBDMg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 12:13:41</div>
<hr>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=rNo0xs4gGWzGryPgjMywJGGn22SRNvSmRo86fsfZx5QH1GtDjq7EfxpvzbBJNpfQgjZbu4Vaw2Ln9UYCq0ztVIxD6piDMbeuFgDw7rc54Q8WpMnB1C9g3uXhii4TWtWDIF2qHGnq6_thASoTdiEieICJLQuu3Wi4P8wD2ritFVSiWyFPaEaeuHh9Eid00WEvHE_PeusY4dzhF5x8xJCJwGbMmvUvCLRKqF9vDO5NaC4h20ds_SZ50FZMuRY5InPS3P8ku-JX55PClTDvUdetuz1c4GRMg_SwcaHKC-bOlMRAS83jtOApItEA5vLGUCRyQFnHUY5tO4GrmI-MOlPHYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=rNo0xs4gGWzGryPgjMywJGGn22SRNvSmRo86fsfZx5QH1GtDjq7EfxpvzbBJNpfQgjZbu4Vaw2Ln9UYCq0ztVIxD6piDMbeuFgDw7rc54Q8WpMnB1C9g3uXhii4TWtWDIF2qHGnq6_thASoTdiEieICJLQuu3Wi4P8wD2ritFVSiWyFPaEaeuHh9Eid00WEvHE_PeusY4dzhF5x8xJCJwGbMmvUvCLRKqF9vDO5NaC4h20ds_SZ50FZMuRY5InPS3P8ku-JX55PClTDvUdetuz1c4GRMg_SwcaHKC-bOlMRAS83jtOApItEA5vLGUCRyQFnHUY5tO4GrmI-MOlPHYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eqvy-PGp_3T0ng4Ysbljglx-XuBh55zHziuSUGYSLmUclugNZz0idfXEIHbhzSns7RyhJTIYbXgVpqh0hCHX8-7tiqGRkeH-Q1FUDszFp9ZE2W0E2PIa7PqSL1GgtHaCEkFy8cFdz5tQfuL8cPPkCWD7FXgPG9jn_y9HhjwdFaguEa-95Ap4UF6hhKrCkaaA9fNIZJhZDRDkQXNDZ5Uk7sh8dVM9oEY9h-5AR11QtWDw1q4BST8ILPyMCeP3fRLQrOLRfZH3UrSHixaQ6O3zpp3k3FWJUKqXRLDA4B6BofqnkT7dKwP9XmfUoyW_YX4dFdqMhby7w0Y0cjI9WEyFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY5nFjIGwk0H5z8yYdx6FYEKTr1VuCx3amOE066Ra8w5QBHHZvNbQKCnpGKIy8qiBHsEYpZq_G6gK0xy1ZFkUCjJScdwEOlF7ljEHaZsbGCcv-Atsb3QrZDLkjDihXURD4TCDTjOuhwzDo2RreEjmwUWUm8r9tSxlHlmIlUfon3nXoM-W74IJT0H13etPY_-3nn3A1gnJUIKjxoERWgWmLrQpG1H0rXvUhH1aDJRgx2hQbPO9_iR-ytrUrmTx1NDM9Z3f0H1MarUPH-Fbb3IwCENjW7krsdSj0uNCTtavViO2Drx50I45geuT23i5IJL3vKDfKx0S3TQRFiVv6YLng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlSMxyf9YurJ6f4tvYTCEimgCeREawnR_1El8SbJ6lZox9rAFjOZSWwYh2Z8Z5EZ0DR1j_bd4whLz-xLtRc2fbw8zs4YXJFy5pX_eho6PjMzP76ToQkMRN_GNKr7s044QhOjkWO1caaQ1mSkWSoLf6AeVxrP_CZfu78P0T14szFxSF0k96-qvA3OVnKWBTupcPet3hu3ix_gvxYD96Ve3xzZtDehz_8UxqzL0bcfEq7ss-wkIgFTgbYHzMF30fDzkjn4AQYOMfRljgCLMdx9vU4llhYwwC5S9xhTXZrpoVIfS3xBln3KO2vNz-2UuFKOWJa9caNpZdGo8u_xQsj4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqHft56kVzqcBvVktxflgsppdUAXn16bTm07CaSPcnY7Ucz_hqnEVpPC9LgIBThjiE6NgSzc4KRrvAok06BxdAhqq6cSz9n-RR-9oR6f7l2PzXXlxQnqhEkGU7IRiapMzqjlfFiN5POAZFbKeLZzi_fuZlHVtJNY0F5cIzByCUKHxKCb_jo0uYWixMY4lfnxqe9PON2IdB09ixm0fWJPxxVcjltW0CA7Trd7SMGmKnvZtxr5wCYyldybcxui-QjiuYNSo7gcfQ1vIH4U8oZNYEs-3Hf80Fn-FvG9OCIomWck2OtXrcZFswy5OF9z9NoVNJt7aw8EbI4k2ro8AuobPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stL33D372NHb7IB-Ybq_2300QymPj6TTyMecz4EPqxWxgDxFg2ofh5XH1wo56feP4CiRidYLwy1KGp8F90idbrZtwciY2L08HeaJdn2cHSansyrMWy3U8kiOD37fzJBINi7rji63FgjVVK2JifWe_9M-YjXd8MHI47sZZ7uDcoLsLNSTtgMwo67qwvHqto9LDpGlzai_zhSr2na9DVnxKh_6AuGeiaQ1NmyEEhsbBRqSgW6pcwLVp6krJTyehK-agJV20sJOulZUxsPrh8gY4ZK1OILZIhauWYZqMwgsE9uOBSXP8CbVTULCwzhnMHA723j5Xk5DaUzTzawlA02lSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fq90r0xb51cHTMMMxAlLFuaufFkdT7FjjU7ATHyAaifn01_WnA_pTBjyv2OXCmuA8GLKdvTxTb0kxiof2YqLYXovbAW-Ndk8l2yAB3yqKz1xzr5YmmEbexwDgNyeLH80hN3Op-45rCG3xrJPIOrc_ju6--On0mcKtEO_PbvItIEXT03owyFlyB2yYotKY82sEScgjhvGf096DGOtwozWytKyH8ubtarPH82DXQy6T9gW8jBcZRU5oyZsS5a0yp8z9rxZkmZENl8d3oeLqs0jDbUIavS21YFVxiupVyCWpxORHC9MnXLXe3zpjbmDqLlDdmLwe1BGqtv60NznP6S-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=PmQaGNdQYi4AIuXxDI9f04IfA04X_5yOs7riHKrvztTACYxqd8A9bzcbmSb9vMj-ecQtE8JdpspG4Icj-vnz1DLjKFEya22TVEZy15lM_nPpKUUXqq56CXxWu6AMmO0WCfqnn0nR8qh4LSl4amjb4iZOvBSb8Cic8wSwWmGPtU3my5XjDzq-P20YY7psSNyuTBZ7nteRJiQMCfHRSM2rdAneILFoHoIm4pW7IpYMdb5ADMuDFgp54uBnHh1ZkqrqWqhaNFIqBIn_qTfNrjx1I57KIQ8hQCLPaqi1_RH8zcHoM_JqXwvdGBGlm8CiG4ds2KguKk4OQ_UZ6UxivEyX0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=PmQaGNdQYi4AIuXxDI9f04IfA04X_5yOs7riHKrvztTACYxqd8A9bzcbmSb9vMj-ecQtE8JdpspG4Icj-vnz1DLjKFEya22TVEZy15lM_nPpKUUXqq56CXxWu6AMmO0WCfqnn0nR8qh4LSl4amjb4iZOvBSb8Cic8wSwWmGPtU3my5XjDzq-P20YY7psSNyuTBZ7nteRJiQMCfHRSM2rdAneILFoHoIm4pW7IpYMdb5ADMuDFgp54uBnHh1ZkqrqWqhaNFIqBIn_qTfNrjx1I57KIQ8hQCLPaqi1_RH8zcHoM_JqXwvdGBGlm8CiG4ds2KguKk4OQ_UZ6UxivEyX0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM16KEgGeB0kEieNc9w3iawjSudD4wQtVCYDfBLz98yaypR2TDGdv_-Xy4NoV0vxV36qYpwjt5jIod8wRvtwX9MiazCGXdeWa-04Wyts9bM1RELv7W6OtNlPON29768UMV8UkqEUwPO9Lzpq7qScGeUm7c9WyD06aWVlhODwEnNcX7IngBUKMYB1Ru8B22xJhqHDffbbfdYLYlzHHq3b6Jdwdxb6HP6tsvpBvI9Z1smb8V05P_AWiMHNR90Z19Vrmatd4BnnWQwNc3s58QFmjynnUFFsa8hKWf_LK87ax1JsLnDRH7GowZLWdohH7bW_wXk9MVunZ4xSadrwpW5OBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=H4llj79WkX7vTV7QaSDCNInGm-nn_m2eSuejW4o4phfekM765pXKdZTKWrUHw4gNlsJMqMcMz8hPDQ5_gJXwqRddYPYpbAJZ59RGaiFP6H7lRk0TAZyW2My-dxDCbESGBT4cZPHOaVE58j_XA7ZWrDN8abZT4bm9PNAeaIrHRGxUZo5EX7_n82mNaOjqRgpstXWhk0zp5ML5ajLuSmV2_PNew8TnR42PLwCceZqrWAH8Hi0wxuqH2yJvJffEevebNxnBaiHYHXUdtvzOPrC2YtlcU1JpbZfIuXaiW5Z9armnH5dgEx1DEz4RsXl4itewATLkw4f_Yhkyvgy9peQhnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=H4llj79WkX7vTV7QaSDCNInGm-nn_m2eSuejW4o4phfekM765pXKdZTKWrUHw4gNlsJMqMcMz8hPDQ5_gJXwqRddYPYpbAJZ59RGaiFP6H7lRk0TAZyW2My-dxDCbESGBT4cZPHOaVE58j_XA7ZWrDN8abZT4bm9PNAeaIrHRGxUZo5EX7_n82mNaOjqRgpstXWhk0zp5ML5ajLuSmV2_PNew8TnR42PLwCceZqrWAH8Hi0wxuqH2yJvJffEevebNxnBaiHYHXUdtvzOPrC2YtlcU1JpbZfIuXaiW5Z9armnH5dgEx1DEz4RsXl4itewATLkw4f_Yhkyvgy9peQhnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=Nn4B8fFsCwTiwz5QVkXLq_-1m7z71Ewik5Zgpwhhf69n9NfdB0XH4yQ3JGeBwkdAiwwisAl8jRTsK9yOhcySAoq_6hwZ0mGqzG9Dlfdd5fLuMLbJPCzLB7N4XcbyWQCsRQdqIzVoN6vy26jrrzGFBuUJe8N7EVpg8eHiLbWLYnqMqnimvLhIzmfFVczWmKuLDjmHN_rjaqSb8kLfVp1BqB--N9UC9xyX9yAUElEotkmQhx9GOI64S7CthPGdd822xWr285T8dJXGfxijL0Bdo-1MkRPtPRN--GaV0eP_vwFSE_SLSQjSqUo7aRBm2snzCRMU0lF9rHzUxN5nH4eQfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=Nn4B8fFsCwTiwz5QVkXLq_-1m7z71Ewik5Zgpwhhf69n9NfdB0XH4yQ3JGeBwkdAiwwisAl8jRTsK9yOhcySAoq_6hwZ0mGqzG9Dlfdd5fLuMLbJPCzLB7N4XcbyWQCsRQdqIzVoN6vy26jrrzGFBuUJe8N7EVpg8eHiLbWLYnqMqnimvLhIzmfFVczWmKuLDjmHN_rjaqSb8kLfVp1BqB--N9UC9xyX9yAUElEotkmQhx9GOI64S7CthPGdd822xWr285T8dJXGfxijL0Bdo-1MkRPtPRN--GaV0eP_vwFSE_SLSQjSqUo7aRBm2snzCRMU0lF9rHzUxN5nH4eQfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6V8Qrsvd9-8sVtDHofAePe2DYsZsFHqeS4_hMGlMvmTMQ4WX4xWX2iTXAz7OCmo5xP-sS6BBSyamW8FjLZFMTzWMHvmVm0Z76P4QfzeErlCCXzB_MsfiQ4TzUXCgNamxEZo2tZTLSTdu026VYK7YKPZU_4GKvbQY3qDTAm4hFz_MiU9HHo7991MBk1eSl0DOpYj-At8qXqlTwjciNn4kEtqVzuxYeB6J2PixFODBjuVwRM5POTcjl0fkmueISve2nbojUOCzgtVvWl34sRVVqlIF23Yq12BQOVA4mUXYZimsAdLHFrg5jVFrLqC3BObgbgL1cSdmhmwUzcVZR5MSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=c1asgIIBbWcf5Smd_6EWZk0ac9VhDIdRawxasA4oROzSZm4Rt9qu08oPMIR6jI3CTNhntgGqrcFyiERrHIsyRsRuNgspBxv21WNpEt8d5q61BQEPjL6cHJLyMfkSsZX1nhv54O-eKHXAQcFU3hvOIz_Tw1WubNmFCRqwmlA5qIQY42jpEND9KYmTOBwOpjpPjHg91qrXCpks9XFl1XJU6YxPhpjtojvJfiJw1QCeL1U9IU84OBrh-jo5yvwvI12dOZBspk9JUfg3H6Tdf5GMP0lm7Pbev5i3ZKFMZJPJXLTxngMM5H1NnKRx0YyzM-ekA9XZknESOWln16Tc3E5DjIoZRl2_cG0m6TyCMTFKMSNw28jcwkfR_zp5wPZUrh8GkBQ_N_U8OM6H4UWX5pn57rzCbdi55xJdHzjCW_eOGk6oRoUwEiifrAUJ8LRT1mBV4YG1CQxUF42ABgjdIbxIA4n-b5FTw_z5-4wXQ5PjV1w1hx8Unt2YrRRlJN5MYj_11SDyrVTEQRdBABoNcj6JJxwnoHKK1niwnHPJuACe-xX1MKBYGdw6iLjCNBFRmUK1oQNSYRkQQNoO41jmdZyfU_Iz_xOagsxCoPagJyXczL1IntZQwxBKdyu1aw_5UIz4hcfadu_hGx1Can0ZfedcLXT-O2BmfT7ftfmkDuPCgd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=c1asgIIBbWcf5Smd_6EWZk0ac9VhDIdRawxasA4oROzSZm4Rt9qu08oPMIR6jI3CTNhntgGqrcFyiERrHIsyRsRuNgspBxv21WNpEt8d5q61BQEPjL6cHJLyMfkSsZX1nhv54O-eKHXAQcFU3hvOIz_Tw1WubNmFCRqwmlA5qIQY42jpEND9KYmTOBwOpjpPjHg91qrXCpks9XFl1XJU6YxPhpjtojvJfiJw1QCeL1U9IU84OBrh-jo5yvwvI12dOZBspk9JUfg3H6Tdf5GMP0lm7Pbev5i3ZKFMZJPJXLTxngMM5H1NnKRx0YyzM-ekA9XZknESOWln16Tc3E5DjIoZRl2_cG0m6TyCMTFKMSNw28jcwkfR_zp5wPZUrh8GkBQ_N_U8OM6H4UWX5pn57rzCbdi55xJdHzjCW_eOGk6oRoUwEiifrAUJ8LRT1mBV4YG1CQxUF42ABgjdIbxIA4n-b5FTw_z5-4wXQ5PjV1w1hx8Unt2YrRRlJN5MYj_11SDyrVTEQRdBABoNcj6JJxwnoHKK1niwnHPJuACe-xX1MKBYGdw6iLjCNBFRmUK1oQNSYRkQQNoO41jmdZyfU_Iz_xOagsxCoPagJyXczL1IntZQwxBKdyu1aw_5UIz4hcfadu_hGx1Can0ZfedcLXT-O2BmfT7ftfmkDuPCgd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=IIWLWaWGvSUcvgi0ZIA1YVy6FO0EgT7cT9qbXzm2_-4Dgom6A-lSkr0EVIapOk0Q7bbgJsY1HOp5kvb6EKhD2aR7Yck7hr0zZKAgA5asbXpaFe_bo9DuK6dyZXsBwSdTmPVbXBcj7nY5KqkNGG8IQpHuZF5_Uqfic70iKukJmdk5-vbdJzQ9y610-LwWLMJd3eQ4h4K866hMei8UoOWEqU2hm1YmNDMSZ3W38Fm-K93rpfyMXuGJXiG50AXk-woveITT7ExFMjUHwe2AD6U2yVmR5MnfPfaU-d-jlUvf2tD7FCnnFQ1oOMcP_JEgM5M7ScnbUoTqx24xBa9N7w_dux2rz5bmyFbsnkry7LjtuKGt3cjzeM1aHsx_dmEiFxlQkWdwq3GInIO5S5pVX4lwus-XWI6SFZzVhbGsL2lWZTtvpV23wYVYPIaNQ1dlKsdyBR1OeP2sz-iiZSjhtO19VEvjkZRijlhlyflbPIfp_GiMGgliOzc6bdguNTZEK5Wvxm1F9_UrSxGMTvOCt26jtUfuEZUaP4-L5OlDGmHq7jio2mU_ykDIXQZOJwetLYx2DShc_VWeajtgw-NBFwq_jgL_-B4FQ_1GfDooyREbcwm8bxgljYqVaH_njTKHVI7ImB_DlBjxVx8f-QiCu7pGMMakbGvzMeg0J5DG4O18HL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=IIWLWaWGvSUcvgi0ZIA1YVy6FO0EgT7cT9qbXzm2_-4Dgom6A-lSkr0EVIapOk0Q7bbgJsY1HOp5kvb6EKhD2aR7Yck7hr0zZKAgA5asbXpaFe_bo9DuK6dyZXsBwSdTmPVbXBcj7nY5KqkNGG8IQpHuZF5_Uqfic70iKukJmdk5-vbdJzQ9y610-LwWLMJd3eQ4h4K866hMei8UoOWEqU2hm1YmNDMSZ3W38Fm-K93rpfyMXuGJXiG50AXk-woveITT7ExFMjUHwe2AD6U2yVmR5MnfPfaU-d-jlUvf2tD7FCnnFQ1oOMcP_JEgM5M7ScnbUoTqx24xBa9N7w_dux2rz5bmyFbsnkry7LjtuKGt3cjzeM1aHsx_dmEiFxlQkWdwq3GInIO5S5pVX4lwus-XWI6SFZzVhbGsL2lWZTtvpV23wYVYPIaNQ1dlKsdyBR1OeP2sz-iiZSjhtO19VEvjkZRijlhlyflbPIfp_GiMGgliOzc6bdguNTZEK5Wvxm1F9_UrSxGMTvOCt26jtUfuEZUaP4-L5OlDGmHq7jio2mU_ykDIXQZOJwetLYx2DShc_VWeajtgw-NBFwq_jgL_-B4FQ_1GfDooyREbcwm8bxgljYqVaH_njTKHVI7ImB_DlBjxVx8f-QiCu7pGMMakbGvzMeg0J5DG4O18HL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfxfibbjEleMVjc4uXFCSuAiDCNCNlAHUmaEs5nvHqVsmi6s-ZfMahRIjhKr-cDI8g0_r7JETbZxw4TP1LCZy6Q6vzdyr1QIkt7AxkmiglFCOtaMdrqQ3zqvb6K-8xsfVuM6X-MzPRWSkqz4KG3Sr6aIrm7ozZetCBFgaw4seAK8dKJOy71GM_JBwJ66dyXPxQtui7PlHlGeQGN0_hUFe8ZP80ouGlJDnk_WGNOG_wyGuQn5lBcLZMwnIYyS59F4Gz_l8CGg9Pt7CZlnVRKYoegbr_AA3q75fEmjbewl0RrbLEEGqLuhAJ4wtKzZAhBvqptDpObffrlvyt2WMecxhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBhV7vqROfsVCwTkFisT2cS7TrKT98YtUuAHuQ093HGAHolxZW0kc2ner3-qYRgPDIBAJevniYyUFzsXctve1MrlINk773Flaz3HB28MbjMuRZM9EQUml0mXKx0ZCqEUGQAINU9SnU9xwVKiDny74fHDq6SHVWq3SGrSRzWErLHHQjQE3VaI7sEt-YBkkaF20YAOTjFzCRKcnB2EUBvfhgEF0MIhFGzFgZFCpgYjL0qPWhsVetkOBtdzgUlCLArWMYyLjMBUUGSyymrCAzmxvmjhux-b9ESuw-cUDGTQSYVE6me_pb6naUYnc7w8_UZXVrXAm8dSbpm9lpMOYU0VOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCrDQC-sI95pWc2PgusDqHHWvAcdoYbqGQVj-GtYIx_mJbFNUoJPb8iz-JunkxjNal6YkeytDeMmQfk8P6UBYk6oSoqnU5BAcdnjd_padC2NZ9rLzbAAKSmPy89iVl6mFW9_vdLkYjaeOgcFUfLrvpv_TtOJg481w4HWGDmx9ho3XU_1e-eWBD17MIyIBj1CZS-n0D9hgZn7M2JNZDbAWHkSIJUxHSBzzf-bHuoAQeSPlfKQqCHTqKbhGxulHhKMP2zshtG-_d-Vf2QcIfcT5nmljeKxYYgPWBYF83XPR7acVJGa6qFPk59bdDpHS5KFgwFir7Up4W-cz8rGzw5uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRIgoaUjZSEQYw8k2P1w0RgZMMtCEv3JT5w9fvD_wS3h3spaAEHYzuSWikp7WDtNTfPichQ0iveV8ZI4ytC39E3niwYS819eFxz6bh4axMCTXJ2BrwGXgldzytzjbhafWP2RDu0zFjy7d9fOqXgshxSpUNAdo5u58QFuQWr3JjnNY1Iq8vAL3VCMI9ruiu3KoSBrUnIK57OZE5UJTL8YrjPbV5jQd-COIcFgNRRwrflpJZDAnb0dijKx8ic7V5FG_Cya2oKGFbpgQuIfmnFU5r3vIXM6zSlzw9aIHNopXUDFEoLu0wSktcFgW1NRuZzqg5gzMSTMwmqoG307ukUz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeJmIx8frarJEV5_RQ63ftbyl7hySAY0sLfdV9dKf_HwR0Vs8Lks44vvcsYFZbp4O3YDlvd6XN0E2W06IEFqtLw0_b-UuGUysf77fZIOy6hMW6IhCkmriCRxZR18sCPCFf_LPt3QqyO3MntsiPAcM8rY8xDAPUkObZ9ufNzSgqIYxFzn3thYD3hYeMHovZvjSpZBajUTKHouxRbsIcDSDir43btN01T-E0eg0A8B5HExEENKT1nm37bWO5imS4-r4Hp8w-axfFDmU7b4Na5a6DwrPW-Wbd5g19shLROmZ21EwZZgzoT6nAmAjhQSHyAv9sfxfH8RCVKwV7vUHy0qEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gpe65NaT8PVtBDMcZhTr7Nqs4e6lljAZwp2J_Ziujong4IskQyL-whYKrbHnQU6bnNtUH-_wR8itTCQlf014PtUP7JTzGRPcJL2XiHBZN6yM-ZZCmz6q4f1yyHaXQP1iitIeo7U8KT568j8Nh1SxFLf5O703mqaM73Ia3Y41bg0k34g-AbgXAuN_OdswccS57ZH-ovBTizSevNYuTUl2RORv8ME7tstyjm6mzssOvWIffz4yCTUj94_ibW2D-JakvfLdhdZAezsHrVZb8fTjbr1ZZOlCtF4p_K00ZURclN1sasCqUM6JNj7joCALbMxIPVCluA0t6xehea26lrAxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcxdQ93vJMoXVtMebdnHwMloVG4IktKDPc-sdcxi8c49w6zveX6EeIZ1ddmlyc19EnCc3EV3SEyy0sjAgfaBMFC2ch8HkQPTjyye6Z7YhhZn6itCiJBnqpPTV1SVcmcwW4WdLw42WTOodw4bnkQg1vysL30b-2PKYOb2fkfON88aSHgwdRObwXLdl3X3098-u-Bjv_AhwhJidav3lnUza_f1GrrFtPytIu7ykAz-4xkikLctrx6BfZ14wgK25fD9yQa6clsdx7Ak07SsolLjEBGKidjH_L8vM9yWVk3f6takSejdvRabJh3FU18hLYqrNBl9x3E_yEOktK7RqO1IWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6hL8hjmpyeH47r_rRN3NjZKZiwRlj1RWO42JR9X1X_F90LX82He_vN0AzI9o9AYftOgDNYHJigs3mdHGOFZ2U6vnH9mS8c29ZLMl7qfOYECy_BIjkCy8rxqsIJKxtoUIbtcpO905LBnKq4KhLrJ16TQxTNW-WZVsOyqjW3JKLWrULxoDFCeVU0ppLMwDEgbViIqoinP7hQkOrVuXE3hKBIF0m4CWhgn5V_o3Ew6M61QN71VjJuUhF12DrwQHVYBl0sEfZ7qAbpD36NEY-ocHJfV3rz8WfeghjDyfxmqJjxyKi-bL0OsS2m-DoklRAPvE0kLll3jqX1f4WGH5RGyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2nW5gCr4C7QsBqrs4PptbQQcVDlkAacbRgeQ1qLCT1E_L4t3yA7ClkrztTMOd3G36qioguIuB7jmN7qZr-uu_gmywsVAgod9hDlIdiViIxVCjxD7IcRICoyvfUVtbnc3dWshsTsSqDb0QLyacfjrV34Mqxur9O5cdSm_3HtC52ItoVSN16vTe45sHkLZT9r4nqboZKJWxGMWHCQRPADNrBDp3NqnIKLshc8q4BdSvjWRSRhhpheKgZXYhBGlXilRoSQVpvJ4aTjATB4yzwr5aAkTmHhVcQEExCgmycQqU8B0CR8uaZEGlgG_cUZhIoTAYaz7jrobSXI_DjXAmaKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7xrUwOk5vcyJQfNPO7-6wHjXS66sBi8LZwKxTdgzgLq32bicpM4uSLD6lXZb8EaksvXdnykWZR-36RxZJkD6k9upJh4Doi3Hh4mtft7r3t50Dt9QHqU__smCJg156ZmdCoR7PTlDYziOkXv9HfCPok8MuIhVMmZAYYE2xqdXrlrqVCuc9JRi68Bag6hXQyqHlRbu57ryYKR-GKJTOyoXWX2lSsjdifurysSF2FDT89FL68uQCJQrNMbgHNoPoJZt-pjmckjMZJUfcsgiNTd6majXcskOZy91OmEQekX-BfQ4f14U_P4jlIyU-tquEEXmdJum9numaLWAVElMwT9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZDu_icODeNHKfb0wUGB4pCprTlZOQ1YAOTjazcjgCUr6VwjRSE4Vabn3eyCn42LD495bCrVHXholVeOXNXQDTT-9cYXad_vhvfzgEAHi5V4M00OO2O52mZsylRDFXhW6nUZu4Aqvzu7MEuH6AAoUkmiOxzyn88xUkbkZF4Y8KHbEvgM9FsoQxBLRoQdX1pPWYGP2EBdUsQIe7yEjiuQrqknagK6KTUD_61q61K_LeiVvBWRzFWfV-rwW3t3iHnYnE9Cnk_i8EjRYNHhN_88Sg3sAakm01bhomRwQ3Ix_jMLSNacPkKJU8V9cyXj8WG28s1mjdinHPdm0tmkCQrsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ_fUOhZ-pNksTwtTyE6CXcykW9JxoM2LbW0yF3Gso7e2gnqd-ksHPoJsuKFMh_EuqDxHWS3Usl8cNEsFLlFuvV7aKLNouZkge58PoseXwAGWu_FgVlwCIS50qiNd1vzqpwC_ldW-4lC5v40uErKeYkwTzxez9fSQ1ghJ2Ky4HrUGKwV3ut2djqXRnXJyGlvAQyFrsAJlLNslmnJycudy-Ct3dVeuiNv0KZQ_Jzn8ynwUPMwJH4oBooK89mqDa5PNT4ZzkbQVXA1C0yRNw6rC7wBYCzAunlWk7MnzGW3HVGr_P9J1U01lVJPnfFwI_hKFquhtMBnIUn-Yx2PQqr8GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0AaaUvdkHwWnBw3ftLMxiTg9xx73inn_y4J2T-kPKxrebTld6MFP8F_nIGNPK_VxZbbaqei35y-GhWoxkuJItphZwb2MA3DnlwfUf9tCpMuVHYS-W_iJMyVQc5LmB0fqkXY7owD_9MBADVS26qcbzgOXJJKuV2VZLpdWQzjq0GVFTVK3wj1ArYq8vwXSYR48ZmT1G73cruw4Xn0jHVyarRdZEExy4K29mWfw9tlTc25lA8JasW_wAqAnH9kaCpFsZpZIu4dqMLpkki5YEi_G4iRfKVbUm0ythacg73P_kGQG_N9U_ciLbn7iyf6YwyJzcfp3Ef_poof080-JaTX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYsaUKB1EiGWvFDaUFATmJBvscWdMkWuJZgVmdTucKDhOz4HZE8KRZGMcv9H9CrHPTF7EOoB5P4PJ-CjdeyXM0cAcyy5SMcVz9fWvtlKy_D0CuCfFjij9o3IU2GOtVnBxyhXTaq9TUBClvQrMyufuZrk00HboLzVQKCOK5spJfbGTPaEjOgjplefQqerSeCVfrUr8zSb4DYy3ODMicHKR26HyIHxi2qoDf0Wl6qcqC-0a1vjb7_tUViCt7jCSfvu4dGWPG51lKXzpvUVQzNVNo445gQ-RajTbPEUSUnuQ5SFF8yr2_WYBqYtlXiLc-jMV1WKZ_9mdQWpYxXy7oUDCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCC_wx-bVohldgyh5s6p10bkj1SgAaOXiriBB7vwRy9eSGsoH5jFCXLCt4vvap91ZL_1Kc8uHf_OjSOc0WdMWHSinJL7Ufei1YkuNvyBXITQZX8UKUJTklKBFqRv-vTpQpi_PF0xeAEsezOzaw1FfqP4dg5IH6POWp5IqNWCrPGlbcpbGlKLO6L2i37BriJitgJ17EkN1KxGD4BzRl1RtJWgIZMbYp8HYOsc89kMPWk_iG0QF1cCY8li7kSVRksaJw-kNQqACUV_nHAIYejrrdyh-Iv4GQO2PritRwSuPQvNs4gczp3qLalJQaz2CFcVLqXD41HCsJ6bfV_Bly646Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6-f6q2IgIukiiqvYQKMg5nLJe6BnOAmIT9L3VGUo0_RW5TrbRR5Didbsz20bk3IE_7lpF2sDJGPCZ3394K-PpHllFgx_uwb38DzAFuvRcIvRtIbdrcOSiGE1QRNZtHw9Nr5keheEV1qmXO_pSPsRLfUyBKbelemiv-EFRcjj7yoZs99yQRR-4p0aEm4Nn_vkgh7fntWjv3hxwKdZBjQbBqAFjh6Yk3nbttQOCWgpywddWMtSd06ES2_5x4PJrMutbsOO3Ij7mYAjjE17Xn7e6suFMVKBgYYY6wsNQOvDYf9nF_Kyr4ctWUC6N5rEnDNF-gbbhQEX-CYl7rSPiyInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRSptrVTHnZFGtu0-s4JNrBzEXUscSY9bJYV26oO9hRiAunxaIXKjNRqq0yvXQ-tiPDeJsq4jaIQye_Wkx--kO2cmyOaIsHkuKk5hfkmlO1YccWUrXA0dzzGJbCdMU4opdGKe2acu-p1jtBz5Jx7Grc88xsMLQyu6d8YIoOEkQD5zIdIGGsLPrvVggrtaEjv7RigtUYgS0sal4xd3vDbB-MCFy6WaDl5rB4w2b0tHmVV7lryhTyH5R7frB1LmyItfb8AOMEd-oHoxEP9_ZI7JuNaLBN-emwOzyB6V4_l0apuReeJi7iSG_wNIi1GKDCSs1_o6aLnxzxIccqwwc6hEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VSaJY8HML3HGST2nCoonHYGjRlBdacI8htloOLjfRRUCe9J5SEdbag6avscYi-5BrWlbZPuPXypbLpNIglC4I9ZD8LaeKDpalpLD6ShvCGmAWx4poWu_pM-F3NEio1XIM7xBObqINJYLgIJ07tnh3deDeUWPRwvRpgtVcMbPUZNNgfauJ7p7IrWM_oX4bmz9yr9ybt34oNty799I6x5TxuMxCoDkCxRf0e4mWzYVdw965wRQk1EEOaBQ9G0TRLbxpFo6aoN2mGv3bYMbLijl0gvBjjOP4fBoYU5hDAP5kDj3gKksobEZLZM5fMtckEoBojCcaxcyDUKANP9lz5pIJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPmOmygjwTzrCu0b_bUSbvSfRUL_Ddw5fUPZeWzm6zsyy0AgLKM1W5oN8nt01ArnKNsiLrNaCeu7IV4s6cEMPK9kDwmRkHNuoyVrqw2lUu3IrKMNunYDIe5sLNVzKQl-tLimS22Xydaie7NV7EIzT9xPqLOGX0SeSGGhZnHikkfrzcU-W533YId0Cjp9dJ2_Kv532CbIm8PuJd4Vbd4-G5_X2z2vI7Qq7lCDIQ711otnJ8tZXBkdiHKNkSk2bpxGmneuZKQccNWMXc7P0d0anwDXagCEsLcEKvGa7GG5Nv1DUmb_SIIT6uN9dWno1YkwFFpkAdWK0tTRI0XUOtU_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLQQwV0YAI2juxaustoDpFAlVDOIGIOsCcjjgeyOpCbGisSdKtlOJsRL2Q8L4GXbuCXcNeUrOi4Yi1OyXj4UXke2von5d3j6JzT4k7_QsYwBdY-WfwTT9fdVADx25gLECL_YNq6LdBRy5DTTgp19T3jo8v-CXdo0h97lhCjTugwHT3ag1UWjTDMEq6DKiHCVaSIwUuJgEVBCLEKTMaaukDHp-WaRKSiJ96XylE1gk8qgbTzZj24a6aGyWZBYToiZ25v1R8CNvteQzuOKYhwxZQd2s1QEhUuVWQ9nYgxEt8gOtzSBWZA5-TYXdxZEgl8zm2DQ_-hpIqv6P37sy0GrHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJFdPr70s-eSenPxK-QvtAzKtKT882bTVA9wkNgehRrujx7R7TxLpXBXcZRuR_69OPppGIFiN7RHd-NPqgCeTX--BkpX9VO7XEyjzsPzsTDp0lTii_grOJqQU1Ox5FZdIa2W615FD160-D4CCIvcSZ5ld-2ParTUoW1Hu43kUf0ZsnOWXVfNRaSrx0k7tZCZ4yjQ52tsfZ26kLzXVhRWFutjM0Wq8fdzTErJO08wFelWWAmXWlxo66bHz04O0OD-XLLee1llwJwQ1nAQYSnjVdXgb6L8369MWS9nPNu737l7XRZhRyems5Ox8XlP-xdqkIF2_85506f0LHALRKzpjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daWCaHOVTbBuat-ktdlg9Yku5slEKpMEntbnMjv7KvQwKKvMGeCFTTDdKUhNTjodSgf3WM5mE0VIo9ey0NXB7gH4PNP4QGWNRw6kdj52U68Lf2rs0sPGKddFTtULdS6sHfgNr_lTa8Nq-4pIAZzRNY1FpqexWxkAonRH8q9M_cRPXTb5VgCJUvVbN2qNoqfpfUQyps7E0UwHo58gpxoPlhPRfKRFGnudMcoQNMa-_XbsOenia5s9s9ROYnhX04iuAaz9iYVmtkbs43SZX5-S3vS_bK4pEslVh_qb50O37mH-wtbxlzQHuDlCBNjxBsFFfCVLadwTPWCu5oWL6XMMNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WWwjWqIEFm9MCnozROA2PEimICwfgLpIs3mJG0aqHJxYTPrhk5AgLNHG-TF6butXyngb0DCMqcvGuhgD-R-lBxE64CJRU99HGRgMlCZfznu9wXwHUNBxn9ZYigS1un9x4mDaqmSgT8ssZbrIHmnMjs_CGmvJZvCLaqBuEV3FdExmMK0tdtohyDburlye1SCQF0mdTCVgMOhlbnaRoZWSg88JK3bpYCEzb10xWpKXhSLSUZsXmAMo_UhdvHWZ-HVn6uifYpVQwVqpexTnq43azUz6sRJLG7j4ejZJv2slg6cBtURMadBbNjC7wMBmDLpq4BtOvn1Oehon9D7pOzYxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGL8DpWXb6X545x52yGA3QayFtw67_9m2nYPOfsirzHmyINE5PCR97Yp7ogHdVi0Cwh5kANwg6RgwD_WcLxocuozQBVjQnjoyX33UxTHnLz9rnWuy-ugeBMSzh3K8EqI4PAf-PUJqzWoH0PadRoT4mZdlgI8Fx5DzhKC63TH2G79lVWv_rggEXjeZDF5B-TzenkVXEbWhB2toWTbBDaeIraYQZgJOVlGXMIqO8aumqeqf_ed-myfONr9WvtefmHS_J40iR68YwqgeF4QrFxzNEQ5Ov9v4eC2rH8y5ST2dM0NWhVxlQd-7mD2F-ztd0jH0R4D5KB1IjqpI7_rayPwZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PW6Je2pt5OLgs6eUg7ozw_4MVi2nyf8i7rXholf55eJy2Pfi2sm83gBVrqEtro76h38v7Z-GPktP1HOxAOyMiEjRfHiap9-KyNRhwc_nhp9VXFd0OgbfBJfvGXXVsCGDH10FjXSVvHR7pb6wXly6rAF_kntsN5CtOKESI_fomkP3sv6WpjFkcxRCM3RMrf9UbeiSKR2ta0vWZQfjZr-8GpX1GN0aSvfC2Lo0lBlGsahvpACRWVkUM36NXzvJxgUnIl52tCxxtrTp7Q9_zHOXV7djWLDo2PR5jc8VqbYI35Zvyh7qfrSXOo7DY8UhsiCPiC1XwBfnB0yXAQntfOQ02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx7XxfadqDwRmQdXRD6pffUm3WSOiqgrf_oTX-yjeRjKq0LH30fiZn3QHllOybUoCVr08RIX-KIX8aHEfwT2XuezcP6Q_Ic4lUlFWs5q6fzAYjikw8sU4Cmh_l1HsqTjiu4aEB8uQu07Ryr-efoqJDYLnt8-J_fWPz_rAjnGsVFTcjvSLuLlpzVv252EQyUi3knZb42QPBdtV0tHnxJYxm5vzflKS8j2O9apUKAQg6P9U567qGe6K7o2CsXzeUdFEka0T81cfc94BFFvpF1xRiHNZECcRUb5VvGY2s9D6-Q7KY1DJwIy1EWatq1EFM2lXAVSYojDF0fKg60z-jljhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSY1nwefCaRSer9d1OiKjYS6DQgYbi1movMfJMZ88Sx70rtwnxjVfDJw3YMSsS8SgXO5H6eGCn_ZWfs9i1pa5BEbzf-BWF-sofRgzd7MkJJkNZqVMB2ed6GB4o2jIOEYAmCH7FoJd9lg_azbXI012UAEEjKE19kzHPRGEOkSSmwzOsYBfYCpScy_sLq8VikdJ8DGqwQH0pa2d7WAoy9XU2QNlNmLDqo3FVjC-InW35tbMbb1J-s-QesxP7Fs_2HbBXescxhm1DGlAl6Mq-sovMEsebP4YUFhZs5luQNfrouFMZc9LAoGYcgeh5fT4Jy6Ofyj4PDogiWL3lnEOOdTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bur8DVSScN1RwLGHXhVvSd3KMxLJZNWXxbdigS3tuaf0ylR--I2lqSklNfmXwXbInBKYSFUVI2e79NFPGPg8nvhFx0x6zP1AHIxWS9KpBbVg2MG2nGTXk0LLwvKfuliuY1_QQXLx5to9Qs6dNqqHxC7AX9CPYljhOZIL6z66gMOJaE31obNMKiXJEtPQscGZ-2rtRgTEr0niQABY6K2_F1A2jMqhh-a6mpdSfa43QIiRpbXAnVUEbcAtdkC2D87pbnbutHyiH1mwvIU_gykr08Bunn61Kp5JuNmU9RVFyVu3IW4SUAgrrt4TarDa0S_rLK7cnjwIrYIXFOpPNSdUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoYLvLr0bt1nYMIoMwh-fd6w_tV9d45nDgrKvfuD6AH6wpYd0ppDCYBewS7vaj-jH-1-7FqO2csPyGA-Il1gEXG7sZ4qd7-QLrVjIFvMU8OUqP5gyd3bSRvsSgNlUnbFAoJqKgnFavvNMpGysOiC5t6ZnjadijDbAi7wT_Pb6DP6TB2U7lDD5f1riyYgZLjgLEG43vFa3hX7dhyud6aAiElj7gwKj90RRn7Gy6I-71rY_3shjrMdIXwQKsHPtNj1Fn99VZCcEsbNQ0MVOTfYPen6l_JP_Sa8apnrCXVoJI3SrnpfwwKzdrvn5IucKuZfs4jnVKooEQMTgj5e31nPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jabdP7qx_AhHHsTuqOQFy9Bqnof19O_RArijIGWwxA-UWqpUBmom_Wc0TPaJnfxc7YbAcsYV27A_mdi09XGHKxdACNggeazSNJlMSGXK_n0lWIUTjk6s5R_CELA_oE1KyYhVvzBeu2UT07P-AmGtHxobSl9XgBiP_6euwYIALXdz_zvlpcR6WT0sJJdvN1TgJ3o427WgRGv3UVEYEyWA6ibVvvGQ6WbqIqS6wOvQyRmBbB_-a34nAipBJV6KukUuqA0eavy7HFmc5S_3p1HVJBYrD77JXCjpI9_NSAA1GZgwM7sh4H8Ue3jYA01rQ-qeL_xs2N0MBJDXnF2Du-friw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9QwpdEWXedKdNokB4uvxTGF_OT3ahjSW49ByTw1mfVmuX6eevBkHxYoUh8X5q5EG0Xdwuu78EY8ZJCR9ufXbsl__3eSNRuqNXIzc_7gRkdldQ4RUJDmX71yh1ppRUQKDP5iA7rXEPZjrMKLjSYvwkhmebj-kI9ChTmqtMmST9B382yje88tZ0fJplw7iC2ubZwi7FVaJBDDVpVEn0NIzskEbkPvLIy3pxKKcg4fCz7W2HidIqffKdpTcy89J_GbQeDXmRcoPZi34mgNiwCyNeb95dYSeyuxQ2IbFz2M2PHARD3UH1JP6Wq_JIXfvCUFVQv-Oof-wlEXCcIa_F7Mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_CvXDoD2Uem9xuqSLEghcRyGGm67HhaJ5b8YNiyN2O1a47rubTUo4O62vGXhx2EW3DcxIrCWpS95YjvmMunXefcIcN-Gn6CCXtsUQcUhljeysEVM4MSPNPY0uJ9wbVHGposYxrgRpfpvlQorO5eNQLbKn8f_sFEOOah7F90RPsZIj3DMMquDPLFlPI6wOK3LqFjOUkf2ZZbEdqyFlaijLRtvLqbr9j7X7ZbW7m1b8zJ1qD_EIUyYH04TRKRdblq7Bfw2VAqHY5CT-Zve_O79VD7FVWYwtcEEj5Q1A1LWw3WgGHJi385qGXQsKsBT5lN6lDtpxJfMrPp97PdCcf1Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRw6rin4TC_xgncN2BFvpyjK7iYtdzq7DkcMYpmJqdAtRasvWpF0fWDDwDlTCB7MzEkwveppwXAloLPO9sbrD8opyidufFozlb4_CVjW7Ufthz3BmrfSa4YYvtX9etxNetEW1aKO5aEwscBq1MpOGDCjipPpFKDdhzdrIUIBSwwt95wwMNPtTnIMlWJKaNJfbLXJ-igC9V2dyjNkby2s9paTMQzGXK6MdGkjv6wrlwJiinyLD7Uc5pdNRFBca4BdhKx8yPdULGrlybDmmC1m40rDvJ9JqNwAlsqmWYaBMbvTmKhAEcnSz_HYeXwcuhVXJn0G_izQgjwJMChtK4900g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fybgnZ-DbT_3yMa387eVbRDEz0uHPi3-KaolnkuaJSUaMfZOdRUUcgp2a_p5HOSJIZuPCHX-DpOVj81kbWzC9EBmGZM_aMmTiH9m7ZxaR8_ZOy3D3TGwdZdqdYh81HH8b1qjVedZgPA-Aq0NM-cE31ud2sMG6SnpyWg3_wBOrz2JkZRBdJelsxekgycyzhc6HbzG5bfveQDRCOyWMivYWViQUN1Z0KHBnSmdEXypZVYn-EI5WrspH4H0UjuxDJd-DOSBzZmtF8rPvFtWhUFTo2gaMI3LN8kiqiyedCcV6fFBID5CNkZ6hrYN48_NjcakXWOj6sfxCuBpzJ77q9i5Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=n_CEGTo2rTdxDbR1X70ZFfRzNtMhkQvFfOdSZaUSUQbl77mewt3VD-uvgiXSkvnTrgoxmcvluJWjRInDNzG3mM8UMYDqmAxKrcZsQZVMwVQXHCpdbKJN_mju8_pXdcS5kIBQzOEU2SeDa0AlCQWIOzRAVJWegTD3f3sIqfszoDJpZX4KwmsoaGokBVpfwX6XReUrNH7nuX6dVFMKddMgneI0XqQ3dXSh7xQkaayR55-x3-3qevNzlJRWCCTaNBvACxsZagBYoWUFVFuKphqB4PN5HLB1BwaiRGNiucxpWsuksIq4kjy9r5bVt3eoejeGaIXpPNt77u5H85enEQ5mog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=n_CEGTo2rTdxDbR1X70ZFfRzNtMhkQvFfOdSZaUSUQbl77mewt3VD-uvgiXSkvnTrgoxmcvluJWjRInDNzG3mM8UMYDqmAxKrcZsQZVMwVQXHCpdbKJN_mju8_pXdcS5kIBQzOEU2SeDa0AlCQWIOzRAVJWegTD3f3sIqfszoDJpZX4KwmsoaGokBVpfwX6XReUrNH7nuX6dVFMKddMgneI0XqQ3dXSh7xQkaayR55-x3-3qevNzlJRWCCTaNBvACxsZagBYoWUFVFuKphqB4PN5HLB1BwaiRGNiucxpWsuksIq4kjy9r5bVt3eoejeGaIXpPNt77u5H85enEQ5mog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5kLwxIs0X1r_wJtZ3v5alrBdZbLQQE_E_8tMaGO48LU8bkaOD0fT2YtuxLsrqnTaQgGfeYdAHcHQvJfe-do9OHXaou9ZWSiqICUMkSRk5PS-hvuZO5T1e8v77EbPzNLF9QUvbhYjL6KCq9Z7YpldI2PbYm-kzT_zLKB3nGMGZHsqt0jb_dZZtnj0ovgH9BvAJ3DiKhydR-qM9eMODanTkmB25Z7pFK5IGAYXrnICV1fMxoKJTdWzzJmoO2pRwt-XJduDZeicWT2Ovxa6Bt0fFYAWtTRKsezMv_TgNf1Jkil6MPkGXODCrR7PDk0uFsnXmzh-rgcXy6jIQnMZjpSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BttgLYy51UC4oUzUp_XGgXL2FmCkg3sDqz0LXAEevOpUpokLy8oMwOWUgQ4XabGUn0BEZ28gKaAprUBD_N3elQyzXXh2BG7TkgqLuYznfdjepCIxi0fkq8XF6Xs0OtVBPC5seHdWogBkmvh9INh4T1ZtN484D18j5ZVBfPCyC5lTCKaQqVtr9WYF7lO9enT0SkNw1M1a7K75XdWz8wUMk6baSlb3wJC9elnWsdBAqYzPv7PIMomZCtRoXfYJYB5BtXZLET7IEYqurWMclZKWQhKaJLyO7OjYOO0yeHYnZbY30DVBUwJQ3UoiF7wLSXuEm8aVzow0qDrOoYJx5LyXkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=E7z5-n_XB12NvSXZqp_A22pF530ouSSItgvxukqQJMoXAaxfRDDDWvmYz1iNH0d0NkQIcUTq5lYd9TcpbG6r5sx7HudO77HhL7WHCKFM-9RYc6Ypvvie5FkK5rQJrokN1x8XO8m6aXnkZPu9vCS6ke5cktSQ1xlSKf6pavJq2JgMOpJVOnrY8Yo1U7vt_lgQysFTMXainbEUghswhAP6VZpGr0upOiD669NTxBdugnElzdFaci0f97HNV-VXwXPHdDCDGN07XF8mDVkb4ZYjo07s9aGRX_j94igE9AgFR1BPpRSE2eqnBYa818nzEIpxahTR6zhxXq2BJchSWbMzow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=E7z5-n_XB12NvSXZqp_A22pF530ouSSItgvxukqQJMoXAaxfRDDDWvmYz1iNH0d0NkQIcUTq5lYd9TcpbG6r5sx7HudO77HhL7WHCKFM-9RYc6Ypvvie5FkK5rQJrokN1x8XO8m6aXnkZPu9vCS6ke5cktSQ1xlSKf6pavJq2JgMOpJVOnrY8Yo1U7vt_lgQysFTMXainbEUghswhAP6VZpGr0upOiD669NTxBdugnElzdFaci0f97HNV-VXwXPHdDCDGN07XF8mDVkb4ZYjo07s9aGRX_j94igE9AgFR1BPpRSE2eqnBYa818nzEIpxahTR6zhxXq2BJchSWbMzow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NN7kuRzoyUBdDnEiGqfXEZVL4d5ekMaJNe-HK6NN1vaacRVv5gDBISmQeZUU76eVRdlSDEbnxjrIU_398xnPCfCOAc93ef-5xRsCgvEzuAjVV4eSzw9ORPj32V4p1tN_-nzdng1sI0sWAA-FF9pXcmvFkWbkRiF_GdZJc7kNIPsfKruVdNP5HgxgJtjxFuh2QsemqflebBtnvIgizUyAPklCwPdZVTAC7u1No8qihn_kIOGtWJ_ZYWhtfsh_WXzAR1iM1HKRgpILq1exh-mccN4Evt3FxtBYyD9TOZkIKrLBhZXyZyJ6jD1Z9iuFXosAl6Z3X5PICW3_ZnCtrJOTLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk-jysy63iOdnQdkgqZtMHyZ-623AYuMwy4PET-qg84p17oul3F57Th0GK10ZIMCogoiLBomDtPX2lRrIND-qRJ1Ic9M3ldPmrtZ2NNmD30ng1voPAMFc4DujvDFgGYJDHjb70gtcFe3IOV2XNH-jPfgwST1Uwm7zlidXVYxgEN3u-KlxCAr-hyuE5q-W9bnZ1QbODnpRP0za67bFKuKsgbFRsfhQ2z2UZW2lH49xopFfuLB7HvMr2EQDG7RfUiRAb6QM8wOIGIYO7tzfABJA8h_q_10pr_CEwkU4HvgehGY0q_KXHjsLyoyQ6OL8Ncqqj9zvmlowfHwQXfZtMTA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6Yle2PeZwq68_9NlfQ09ggKAliwNqpw6p9ip2Y6JUAkhVsisbdJC7LiDMe1PCR5tvZZE2-k1vRAvgIyF7pxNh2FJ7dMFawCZJKoBtKe-nlRmMxwxK5mrvva6D1zrZruUQW34q41r1OSj7UB4WuZGSOHha_f7MirL9y7ahlEXKseiNGCZIt0SvUcQDWqbS4WacuG08cOQZIoGUayOS3JFAsLTttvq1A8JcLvfSE4YxlecjIgiBAHJbSldUdQdG4SGyJGVk8zpELRXVErB7t2E2JHL7nPJnz_ewK2YyxGi4fmlNQBY_QnAckatay9k-R4_8nnPMLtgxG0KkEy8Se0bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=oNqnz-Giv9mrsuX14ndry-oG6LOCM2mU6N_BRkLyBxUvotT-j8HeHEErFkSM1IT5wOUmnx_EdXDzD9ii9F3amhbcG5gfRagwBXbYbNM52Hy8bQgn8qQ9mD_9xWxJdSt7g_-CWcxGI3pJdirCRytCng1f6YqaH1C4X3NGHeFqrYoEzcCuvUdLJqeGjSCzNhaVWiR2F_xjH8uL0VHUkyEAt9udxbB-lYaAxhMvIdm8LUsc42fZ2VqQOy9zy1GUfCFS-lOm_pjUXrhVfn_gqspFpCDLi1NMgr1HwMR_djwkl4omIgXkQU0sqC5ijj_0judimVuJIWSwEZzm1xmFQyzxfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=oNqnz-Giv9mrsuX14ndry-oG6LOCM2mU6N_BRkLyBxUvotT-j8HeHEErFkSM1IT5wOUmnx_EdXDzD9ii9F3amhbcG5gfRagwBXbYbNM52Hy8bQgn8qQ9mD_9xWxJdSt7g_-CWcxGI3pJdirCRytCng1f6YqaH1C4X3NGHeFqrYoEzcCuvUdLJqeGjSCzNhaVWiR2F_xjH8uL0VHUkyEAt9udxbB-lYaAxhMvIdm8LUsc42fZ2VqQOy9zy1GUfCFS-lOm_pjUXrhVfn_gqspFpCDLi1NMgr1HwMR_djwkl4omIgXkQU0sqC5ijj_0judimVuJIWSwEZzm1xmFQyzxfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=WEsJZEdhmPU-TjchNe0dDl1tYaP82joVnyQb9cd6Ui6WOtm5X6fRmWFvo8fv3SrdjtUWB-U8su_Ed5_qPyJ8k84IL6BH4DXMAehah8Nk-xKskOjxSNr_SpHVowLO1s_bka9Dp1xg-FwY6MhPbq5Hj-HHxW7dcyoAjJ-qX2C9bvxJPZoWW7w6K2reWJNkIqsdUcJziluy3FVaOFqQ6CbjtZbMI9Kh2E2aunRlKzhHR8IC5hsYbWeXdSyx5XLPLM2XawgJCfa_xVrvx-INN7qxhAXlM35TMFfydYrckTEPdVe7C_CP4qDV5KY0zutCm2_cUr5GRRvg5N1yhg9-k6t1dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=WEsJZEdhmPU-TjchNe0dDl1tYaP82joVnyQb9cd6Ui6WOtm5X6fRmWFvo8fv3SrdjtUWB-U8su_Ed5_qPyJ8k84IL6BH4DXMAehah8Nk-xKskOjxSNr_SpHVowLO1s_bka9Dp1xg-FwY6MhPbq5Hj-HHxW7dcyoAjJ-qX2C9bvxJPZoWW7w6K2reWJNkIqsdUcJziluy3FVaOFqQ6CbjtZbMI9Kh2E2aunRlKzhHR8IC5hsYbWeXdSyx5XLPLM2XawgJCfa_xVrvx-INN7qxhAXlM35TMFfydYrckTEPdVe7C_CP4qDV5KY0zutCm2_cUr5GRRvg5N1yhg9-k6t1dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT092vZuCOVJbHFsWemmCTpKfeGx0EkKUGW8_xvK9epusqOk8OsBicL0SyS78bOuMeBnMsGAxFdZukNabLFin2KFHiL4zIRz7w5Hxm7dOTLbQHFT7HNuzAC-D2b9hGC2CQv57CSzBiI2xzRaQTgySWrbadrWDE5jQOHcKixqcc8SzgOYFzs1fRu3QPkyvxef45E0jhYlomuwWOGHS2BcLEPbMNVwPeeRcHVgsqn8ZXU8t8ND7QHAeVEVvHqB9Tg4qu7XE9KvIMa8EX2DSyCIPbe-Y1SFAfR3-l_fg6r9d0AsG85mEFT45ssWwGtQh_QjFb_BxDtlWvVeizQMi1pT7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNhmH9yUPiENoo6yxkfK96-lnpa6Il5gfrklI2iWuwbWUzmwHbtl5svf6MFIBdOJTa8mSKKwhNSV777lzwrOErM88dbiL2C43PYecNn549BoBOZFSyKtUl7RILCFKZ-vauEl-d71P-Fg4CCPfJ1BmYu2NLiLTwsZc6og5NAnJ7-oytkQlagaKcOdyTZ3qobhe8q7_wj71PeLFsiAPQWfIHr8O_L71oAqrmVYKNfdJjrzMxQHrsqQh89kdnCIsJl3nVjYouy6jcsQ4DPQvVVFprwVN3NF5DeXQa1KlpXe5HUd0C1bI6eWUAVfsbQc-PTKSwPIt9F5BKzgOp5RC3mwmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMC75Krg96r0vAPlm-C_EiLQY5Cd0mxCWVcJXHSBMqHEmfvWfbmhi3fS_G65bQyPZyG5vbe9C8h1yRudq2FHQ6-R0XWpxOroI_7RrvlzSaEdGGOW9Nbk5RyMBjB8kTuU9xnniYzhYmztv5-sQxZ2kkek5VBZEr0H4pwPA83XmtLEBcB1edDsGDUWk26ch42FUsSJkPgVotswjzP7AFUh6cSSUc4Bpu4IHSDCFdccaeWI4-EmHB6-m4v-bZTUTjeFDyOilWgF0Xo_rQPdg0Rd6nsrtws5mH5YUqNND4lZkNrVg3tuFO5inMy7bT5dig-2vIfH_EsHZYDBaFxIUp-Pvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZhccruG9gCDH4x-vi1rO2RhWuRdWwRi4y_YhJ2matOWV2KOdTOAmrzJ_GvtchGRL6vVQtPtzo3bf9LGO1LbJtgTD4hry3uHLNjZlKIHPPA3YnXQ8Jrhh3e4DTDufnMWj4hMJgG9TIVRPanh6kJX63jNxnaF7DlWgs3F4mdgIo9AwjCOlsKRIiJYl9REt9XyeuA3_uXo22NbSQt-eDWPnw6emtuCWzKEN8ul1Yncdv1pDWlEcWJ8DP4PjuCG5HNLhFok8u6pC3iEXzJLiWiytbFZ8wzGDwN-fOE1tvvZ8xAntGWRN7BcfzwLbSI7ncIchhIi1EpJ_cfgGwrqrOHxxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adQR8LTe1J6CxI_Ca7fGA8s_nUgqCVTIsjlE_aQx5haaaDiASrrsMThIz7BLhmDnGvJIogjwtaUwKcUGoxYatEjcT7ooVbAGL9rUrC9kWtfeH347ZKDgopxNmP7js19FyWkaUdFQ_PazhTBYJ2TTVMOvQxNvaGLTcGirWu7I2INOdDB_Luu3FfnjH7fY8lHKxsE6XYxJkh8RDUtj9s0daQLMe9x4wjZqgPa7XQYOOCWyLBXe0gh7fF5j8s3WnzZLB7oS9Nnw8NJEKEeXyrIjR8BYCLf1U4QgUzsYs_xyxUMlM4CKl1IrHUHFP6oTAXBhB6ags8iq14oSGcdrKw7gyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzRnDTOsV6SDl9GxnhyEodtJwbL4VGgMt8bhBtVPk5NiglC54Aqejtb3jMsyFJwTCOAphjbd81v-Cl3dTTc6GzfMLvFTZxIPfZo-PE4sfAGy0iUvTJ7h3yKhPXQUM5Ox7wfAN6ojaeLyQvb8CaieQ7PZPc-Knp-w7V05D4RCV0VX7Tb29NjnSG05pkZywSTX-TIcQTvWqNKom2hh7G3Ix1YfGOiguBikNfQ8gzaoZQrkulrnkVKhiqwtz7gW4_sCkZ9IUKEFqhe2wdYd9k5J47XXJmNkCDLj0OuqzFiuv9kj_Me_DzXE_uY_SIwvyW7ly2BO53A_G8Sx3BLuUBErVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWxTBNRHs66QN_O0M1Ta4uvXUtpLCLil2MNffJUkwf6EbX_3KCKSAs2kAT9ozkwRScTzvWHuo-VYVSEOsN7LJ3pSKbRD9JTFdEYzUjDSr-flgBIBz0crQcfW0IoknkgxQtcbYcD_Ab7WeEPQBvrbpKCk38yDNPjtPQF6CyTilZAWphFqOn6haUMbEyjsIV7bkGCx8K9MkEjFn0LL14U5eOtoAYvKKqnaQX3790zYEJjGOhe1mIiVUh5uxQXu0lP7Xb5elAEP8eigAmOw5OY8WzT_6f8_OCRFqs-YbbL4dlVJ5u3r3JXjYcS2GIadZG4UGy3Iv5psHCBxn2EJGrrCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=nyCgO6CBrhGiC53fINtlB2QxXcoMZdQrmdlhqlubCZOB4A3j5J4ApZaq6xlHXwfrybABwz-XMHQNPXHz4Lcq4ugfBEpzqHRNeaIIGdpyQ85uEhCA60E-xbrZn22mQcBzGDIf_wpfdYtQm3Yx849btaw54tZpbq59Dx7ZIAdVbeNw-lnus3Qgd1UJPY-gXbQHs7MwYW56q9LWLebRD3JMI6d2g0rE5cAjKVZE0V_HGFDlLCPthdTl1SH8YG18xWichmS5mSIGDLta4QPCQU_D8TBjq1tHPyO5YDD8SuB3V20OHEU9eSdT0pCFJmvpkO5Fsyo_GJPP903vGXn8lwSItw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=nyCgO6CBrhGiC53fINtlB2QxXcoMZdQrmdlhqlubCZOB4A3j5J4ApZaq6xlHXwfrybABwz-XMHQNPXHz4Lcq4ugfBEpzqHRNeaIIGdpyQ85uEhCA60E-xbrZn22mQcBzGDIf_wpfdYtQm3Yx849btaw54tZpbq59Dx7ZIAdVbeNw-lnus3Qgd1UJPY-gXbQHs7MwYW56q9LWLebRD3JMI6d2g0rE5cAjKVZE0V_HGFDlLCPthdTl1SH8YG18xWichmS5mSIGDLta4QPCQU_D8TBjq1tHPyO5YDD8SuB3V20OHEU9eSdT0pCFJmvpkO5Fsyo_GJPP903vGXn8lwSItw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=kMOTsojHQH97o8XpZGKYnwfVaGbTmlMqtfBDQcaKxTNWOykAqbwml0k3EpGpKtB0XEIrrEZYOGudoCSHZqHrmvd9-r4RzCAKAg1z1b65LMeVHj36UaK6vGT_AAneRK5QvktgQjTxE_fiaylwDBkPhh8VkjNKCk6mknqtao3Q_qCD7Cbug3IwxP_xpx4ibGE3lMYIVZoT3MidbRYirEqXs6M8vkxuKlu93E5XVz5HPqb_AzgoU0MgfT0w0Mh1frn0tWBlh6AQA1BNM7W2SpGEGrs1XLuAYlnLa8BBFSY_jw33GYXJOSHqIlgKvLkmizB2wSlU3i1IQe7BMB99Wc_KTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=kMOTsojHQH97o8XpZGKYnwfVaGbTmlMqtfBDQcaKxTNWOykAqbwml0k3EpGpKtB0XEIrrEZYOGudoCSHZqHrmvd9-r4RzCAKAg1z1b65LMeVHj36UaK6vGT_AAneRK5QvktgQjTxE_fiaylwDBkPhh8VkjNKCk6mknqtao3Q_qCD7Cbug3IwxP_xpx4ibGE3lMYIVZoT3MidbRYirEqXs6M8vkxuKlu93E5XVz5HPqb_AzgoU0MgfT0w0Mh1frn0tWBlh6AQA1BNM7W2SpGEGrs1XLuAYlnLa8BBFSY_jw33GYXJOSHqIlgKvLkmizB2wSlU3i1IQe7BMB99Wc_KTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=F_obAa9wB0W6Ccs6iyZjfYMd1ZAT6ToWWZIInou56mADx5HKkvPfcxfZMpABCXmNYp10TCTVkTHRV6fxkHYisDOLuw71e0c1qfxlBNoWNPz5sTMvQ32-YNczfaXtTBxXqYxqol9JxaI0RmPq3_YWhacj0NXZE6oRRkaHik9xNdk8x2aN0mE4nmFVyb9bPjtSoL1ICFbBTiSsdbaf_g7TjyocmoXD9ESXiaeIRZnOq226SJ3ATjBCdB22vImhgb1m3DAZqv1Pj9vuZBks17jlQDpHc6aZ-QrjtcwHV7EuxgKqbwgIbIm1rwtaIl3ZjXqwWuZ4sz-t90pdwbRTk0tNmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=F_obAa9wB0W6Ccs6iyZjfYMd1ZAT6ToWWZIInou56mADx5HKkvPfcxfZMpABCXmNYp10TCTVkTHRV6fxkHYisDOLuw71e0c1qfxlBNoWNPz5sTMvQ32-YNczfaXtTBxXqYxqol9JxaI0RmPq3_YWhacj0NXZE6oRRkaHik9xNdk8x2aN0mE4nmFVyb9bPjtSoL1ICFbBTiSsdbaf_g7TjyocmoXD9ESXiaeIRZnOq226SJ3ATjBCdB22vImhgb1m3DAZqv1Pj9vuZBks17jlQDpHc6aZ-QrjtcwHV7EuxgKqbwgIbIm1rwtaIl3ZjXqwWuZ4sz-t90pdwbRTk0tNmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=Ou3dOyNy98ULrSRUTtwWEfEMa-4n885S1nh0YRXmQnUL3gzQi9F6uikR2_WhMD69ACoqOq_gY62R6CzX4QWqtQCm7HHpgNecaZgkuxpNb3_8pa8hvzDzO8uDLaOyELbSbd1DbsAX_-NqBbhbZifSDKKcG6nj8QTYMysEMGfdEt_wLDTgkdre4ljk6NCo72eCqFnXwzEtHwxeZp7C0ePXD0rXW3SIfNrZ4eqzzYrkMOy70HF7rVIssen3Ip5MiwLcbu-g3ehfK8YLKxq5eUWIdQqsXQeaurVX0jNDRUxbtcLt5e697c9xrovjtEhFAzFFAkWat-dxdXQA-Glvhcm2dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=Ou3dOyNy98ULrSRUTtwWEfEMa-4n885S1nh0YRXmQnUL3gzQi9F6uikR2_WhMD69ACoqOq_gY62R6CzX4QWqtQCm7HHpgNecaZgkuxpNb3_8pa8hvzDzO8uDLaOyELbSbd1DbsAX_-NqBbhbZifSDKKcG6nj8QTYMysEMGfdEt_wLDTgkdre4ljk6NCo72eCqFnXwzEtHwxeZp7C0ePXD0rXW3SIfNrZ4eqzzYrkMOy70HF7rVIssen3Ip5MiwLcbu-g3ehfK8YLKxq5eUWIdQqsXQeaurVX0jNDRUxbtcLt5e697c9xrovjtEhFAzFFAkWat-dxdXQA-Glvhcm2dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=WogxpvMTpPt2SV9BRiaCnTTIre7FvCdVSPuqP3z5kNWvjTb6rqIIdNQXRheZuUWJe_uxOWKbP97Ep7mE74v-lrEt3ylD05ude9ebtiFULuFkkZjCblLPLaZEnDs27U-3PA5R8W1lEVb7Z3w7_S7BxOAcrpQDJPN-184E7cVJfFDkGnPAsBXr5NdDeMVMYiuLpKbY0lrIMpirQnkMvryMIA1u08Hcb5oYAGlxREw2cyhCcGWkd4n32vFfH9zQWXCLIBYg-MMsPrazT20Ph5hQJqSdDcaxD2eGvLNg1BIysqsJk7-KZSYDqSAAz3VmYoPbBkqGMYiGMTHC6MLsOrTCHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=WogxpvMTpPt2SV9BRiaCnTTIre7FvCdVSPuqP3z5kNWvjTb6rqIIdNQXRheZuUWJe_uxOWKbP97Ep7mE74v-lrEt3ylD05ude9ebtiFULuFkkZjCblLPLaZEnDs27U-3PA5R8W1lEVb7Z3w7_S7BxOAcrpQDJPN-184E7cVJfFDkGnPAsBXr5NdDeMVMYiuLpKbY0lrIMpirQnkMvryMIA1u08Hcb5oYAGlxREw2cyhCcGWkd4n32vFfH9zQWXCLIBYg-MMsPrazT20Ph5hQJqSdDcaxD2eGvLNg1BIysqsJk7-KZSYDqSAAz3VmYoPbBkqGMYiGMTHC6MLsOrTCHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #2</div>
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
<div class="tg-post-header">📌 پیام #1</div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
