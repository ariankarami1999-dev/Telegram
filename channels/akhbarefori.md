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
<img src="https://cdn4.telesco.pe/file/qBBaAtJ09tqvVINbISTTwahx4ofkV1RKngVrJ9Eeste1H3iMP4chdLAZpmp60wnbsh_cAzFXkqo1vmsTBLRfqzSV2R0AEDvEiUln6FZDIixY5vqyDUSKjOUD7rFO0yetAuybAkzsPNsBwHp3KjDzzqG7YaOhUVqqX25Q94bFwvvbLt4ydZnFi-h8q403kyHPdENwSH54eQxKyfmaVE06bYz2Znw5ml0z75fIbF5QveBIVvv8pfxsALAMaClIArhJDQhGaP_x5EL0G29SVnd_fol_y03EB2dKd-ConnDkgY6CDthm389Ayv1LZai59yyvDtsR721VZKG_pwKn-DaFJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.45M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-09 00:47:45</div>
<hr>

<div class="tg-post" id="msg-685681">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn91uhpSZxenvibnhS8pfTh0Dh5PURu62NZo7VZmR_6HqyphV7LaFJguGIwFOu77IBo3Wf5Uqyq-U7HbpDBN-qaL7hddGDFXH8XTei9rMUROjSvMZz0COQeLSt00O61AG3gN4dPtP2LTerLzakoXKxpYniC53_N16gi1sP18qj3Mgh1hNU4Iy8z0OSBN0cfqHvKGBqJ25UTmd3MuhVIpJd9ZVoxRpSfdGT73UesTNnWP_aHKhpS1GC8LwQF2fSkCTzkzfCHn2bRVBi_eEADFNsdfYkspOnsfR5d36cv36lW8Q_kyzb6M46X26Jv8Yh8k39_59gWvbBha7hftohjZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آزمودن مجدد ارادۀ ما، تنها هزینۀ شکست‌های خفت‌بارتان را سنگین‌تر می‌کند.
🔹
بی‌تردید هیچ جنایتی، در هیچ سطحی بی‌پاسخ نمی‌ماند؛ پاسخی ویرانگر، دردناک‌تر و عبرت‌آموز که سلسله شکست‌هایتان را کامل خواهد کرد.
🔹
با ترس و وحشت منتظر باشید
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/akhbarefori/685681" target="_blank">📅 00:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685680">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8fa03f85.mp4?token=l4RqQj3irK0AXQiCYTT6RuTz-wWwLRRcSk6aoAVCP2mxTDTVIgR45BYKmCODW9tx9rlJiL-kNj8iufac4kbgQ9iJMN-aPsQlmQycxj04uOxsq10C0a4wNmcpUHa7xUD_pN36zf9Z5aeOIBcavlfEp8z_dmvXmZH89Qxb2pwSxU_1GcHdTxNjz3EDyFnprs4uNOTz_fUneWArhcBCARCySHY43A9AwQoohRq9mWR4TH9N7VM9KsyT17yOxLsuE0hzj2vYzudusSh1_vmOnDPgfCTorZ_WFDmGvJJ_UTq-EimRmHEyrCu5hXPFzw7b5LE0J6GliTjKulN48qOFBzk2JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8fa03f85.mp4?token=l4RqQj3irK0AXQiCYTT6RuTz-wWwLRRcSk6aoAVCP2mxTDTVIgR45BYKmCODW9tx9rlJiL-kNj8iufac4kbgQ9iJMN-aPsQlmQycxj04uOxsq10C0a4wNmcpUHa7xUD_pN36zf9Z5aeOIBcavlfEp8z_dmvXmZH89Qxb2pwSxU_1GcHdTxNjz3EDyFnprs4uNOTz_fUneWArhcBCARCySHY43A9AwQoohRq9mWR4TH9N7VM9KsyT17yOxLsuE0hzj2vYzudusSh1_vmOnDPgfCTorZ_WFDmGvJJ_UTq-EimRmHEyrCu5hXPFzw7b5LE0J6GliTjKulN48qOFBzk2JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو کودک کش: آنها از برنامه هسته‌ای دست نکشیده‌اند؛ ما آن را به عقب راندیم، اما آنها کاملا قصد دارند برنامه هسته‌ای خود را برای تولید بمب اتم از سر بگیرند
🔹
بنابراین تهدید از بین نرفته است. ما این سرطان، این غده سرطانی را ریشه‌کن کردیم. می‌دانید که…</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/685680" target="_blank">📅 00:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685679">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
به گفته برخی منابع از شنیده شدن صدای انفجار دوباره در جزیره لارک  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/685679" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685678">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز به ایران: اگر به کشورهای منطقه حمله کنید، تلفات سنگینی خواهید داد و بهای بسیار سنگینی خواهید پرداخت
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/685678" target="_blank">📅 00:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685677">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
نتانیاهو کودک کش: آنها از برنامه هسته‌ای دست نکشیده‌اند؛ ما آن را به عقب راندیم، اما آنها کاملا قصد دارند برنامه هسته‌ای خود را برای تولید بمب اتم از سر بگیرند
🔹
بنابراین تهدید از بین نرفته است. ما این سرطان، این غده سرطانی را ریشه‌کن کردیم. می‌دانید که اگر سرطان را ریشه‌کن نکنید، می‌میرید. این کاری است که ما انجام دادیم.
🔹
اما سرطان همچنین می‌تواند متاستاز داشته باشد و اگر متاستاز وجود داشته باشد، می‌تواند دوباره به یک تهدید جدید و بسیار واقعی تبدیل شود.
🔹
ایران می‌خواهد برنامه هسته‌ای خود را از سر بگیرد. و من این را می‌گویم - من قبلا یک بار مانع انجام این کار توسط آنها شدم و تا زمانی که نخست وزیر هستم، مانع انجام این کار توسط آنها خواهم شد.
#Demon
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/685677" target="_blank">📅 00:22 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685676">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
به
گفته برخی منابع از شنیده شدن صدای انفجار دوباره در جزیره لارک
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/685676" target="_blank">📅 00:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685675">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ushf9tJZyDENJqvyRd49T7GpqBH4QNs93MZ-g4lRm7SamYYlSzteIwnoTo8Mk2QuK8_WfwjqvPeegBX5fiL2TklHEPHTRemNujCGKog4MHUNzNtbYmqfB5a5KwaeVUR6suo5McT_V_xt8NjaE8SV_6EvPo9G52MdfNfnvde7UVLlKhULxbw1n_EBJBNobnwUNU4_NbxSnAuMP2wS5Q96TMAvz4Q8QKh7ZsknFeSj8kCEbFBGvASHbWdFjFvWOWIKT5iqa-ESEX5UGuR0CNLCXVDrnq07JHq8CPDCL78gVnb1JNi-Bbbp-PtS3xowJA5kJpZPdHdpz1BChYwYcyknSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تجاوز دشمن تروریست با تنبیه متجاوز همراه است  سخنگوی سپاه پاسداران انقلاب اسلامی در ایکس نوشت:
🔹
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/685675" target="_blank">📅 00:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685674">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ld6iHbWwmkFz3a4ycmESesS912z1jSj84a6wfk-nvyzSfxhN0BNB8V70rzR0laQeheF7tutSRBxQXpwpTV7nRTVuSnYSDvaxo1jKwuSxU6W-SNGvNcpectwT1x-6vj466tpQbSmeJTH9Pb9DvIehq-aN_NkCl_lJ5K3nLEtm6kicOx0ur15obWmfCaiJd6d3NGs_xjU6Dh9iXUUu1uY_ZOriEf7VKNIK3g_UMF5hJumZW7wWlm9mtHZItbnex_0HSOBWq3uxyzF2uZAkLDuDzFlsNRkEaimjYL4UcaqrYpbWfObwePE25lmYntAlCs4yW8HYu36N9omD_4msV9eBNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/685674" target="_blank">📅 00:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685673">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd8AcCtgVQ5diEgR0ouYEsZt5oMtu1QVYFwpHuSzUfL2SjY9u7aNaxjnYOwU-IzbQvJ-u7unj38EmpnIJOiwirCOc6O1JIOirJg72Ayh6xF9jsbtv_Ka-KbWFoQrJJ4UzWQ_0pqhm9ZjkJJYBI5kARr6sxCtgjEf1d5H_LZQoSm8JmUnwMJbkjRZR8aErj1tpI660wZgW9ff5eseuJ-2is_V_e_SfruYTaDUhixcntYn6RH3XuINDqFE856MfVu2SOayYmdSs2gq91Fc280bBuFzR7w1yxYPi3x7avbdUnxxiZvvEkRm1qZK_G4nfIVXQ57_g9xbJqxhlL6bdrCi_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سپاه: تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی:  بسم الله الرحمن الرحیم  انا من المجرمین منتقمون
🔹
دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/685673" target="_blank">📅 00:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685672">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
برخی منابع خبر شلیک موشک، از نواحی مرکزی ایران را دادند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/685672" target="_blank">📅 23:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685671">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
ادعای
کانال ۱۳ عبری: رژیم صهیونیستی برای سرنگونی جمهوری اسلامی ایران هزاران جدایی‌طلب را آموزش داده است
🔹
رژیم صهیونیستی به عنوان بخشی از تلاش خود برای سرنگونی جمهوری اسلامی ایران هزاران کرد جدایی‌طلب را به سرزمین‌های اشغالی برده و آموزش داده بوده است.
🔹
این رسانه مدعی شده سه روز پس از آغاز جنگ رمضان علیه ایران، پیامی از آمریکا به صهیونیست‌ها می‌رسد که طرح اجرا نشود.
جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news-3241556</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/685671" target="_blank">📅 23:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685670">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای
آکسیوس: ارتش آمریکا در خاورمیانه به حالت آماده باش درآمده است و برای پاسخ ایران آماده شده است
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/685670" target="_blank">📅 23:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685669">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
حمله آمریکا به جزیره لارک / ۲ موشک‌انداز سپاه هدف قرار گرفت
👇
khabarfoori.com/fa/tiny/news-3241579
🔹
درگذشت ناگهانی یک سخنران در تجمع شبانه/ ویدئو
👇
khabarfoori.com/fa/tiny/news-3241569
🔹
ماجرای مرموز فرار پسر نتانیاهو از آمریکا/ چه کسی دنبال ترور «یائیر نتانیاهو» است؟
👇
khabarfoori.com/fa/tiny/news-3241559
🔹
ماجرای اتهام جنسی به محسن نامجو چه بود؟ | شاکیان او چه کسانی بودند؟
👇
khabarfoori.com/fa/tiny/news-3241480
🔹
رونالدینیو: همه جام ها را بردم، اما یک حسرت هرگز رهایم نکرد
👇
khabarfoori.com/fa/tiny/news-3241450
🔹
همه خبرهای جنگ و مذاکره را اینجا مرور کنید
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/685669" target="_blank">📅 23:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685668">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HG2G9QUtdJHemeVueVcqKr_NXIbDRmDI4VPP2ort2SeYg9buGabfgyUZ5IkI_Vcfv550rCU5UCe_iwGnlQ98Qe_TmQx1dzDvlmR1ZG-ogLGqFi0O1SdyK1Hlc6KdnM7iMwQcnbPJaVr2cfwwrT36g8xDbEY0YAu8jx2GiJkSJy_4uZlmz0TdIuqzICLHK4qwOGyIS1yfyFVyJVbOhFBqSrCKWwhMdY4WsNvt1zUjpNziirali9HzvdVc0CSbWWLIVNzpzs9hh7YJ7HqAF5Q82gK_akmNe6YyJ29zBh53OnglaDAnf7yD-ZHTr6_a2oKCgQmOTlM92A155BaPzEGBIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توصیه‌ی مؤکّد و مکرّر این‌جانب به حکّام کشورهای اسلامی خصوصاً کشورهای منطقه غرب آسیا و حاشیه خلیج فارس این است که دشمن واقعی خود را بشناسید و نقشه‌اش را دریافته، با آن مقابله نمایید
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت | ۸/شهریور/۱۴۰۵
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/685668" target="_blank">📅 23:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685667">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4949575f84.mp4?token=Quf1KU87zCLftsgSi6ulQrYcYZgO6NplpJ-nP2iCtrvP5TuvDR2H-yJLn4hytVRVJzrtNERGrhdbDO3FUcflpz6noXi77d3Cua3OpN9_PNysYKyBE1MApB-N33I36Sv1qSbfE13z5aAew8XjR3vqJEcDYP9PL1oy6nFnQO2eRnE6F0fhVe67bILqytdXZHMLFapzRQhkQ-q_avvpHz3EHwOvqsePgb7keZ-xBsryd7D7xyhfYi-mzPXFn7kc6czVuzSbZpfoyfimcHcpl_xfbf-Nu2JUwQl2f6b9DAEYujdZ8QG-GyE1u_9ZrQ18vc_trW4T_MPniZvJ4c_V1s_dXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4949575f84.mp4?token=Quf1KU87zCLftsgSi6ulQrYcYZgO6NplpJ-nP2iCtrvP5TuvDR2H-yJLn4hytVRVJzrtNERGrhdbDO3FUcflpz6noXi77d3Cua3OpN9_PNysYKyBE1MApB-N33I36Sv1qSbfE13z5aAew8XjR3vqJEcDYP9PL1oy6nFnQO2eRnE6F0fhVe67bILqytdXZHMLFapzRQhkQ-q_avvpHz3EHwOvqsePgb7keZ-xBsryd7D7xyhfYi-mzPXFn7kc6czVuzSbZpfoyfimcHcpl_xfbf-Nu2JUwQl2f6b9DAEYujdZ8QG-GyE1u_9ZrQ18vc_trW4T_MPniZvJ4c_V1s_dXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امکان ضربۀ مستقیم به اقتصاد آمریکا و لزوم دریافت غرامت از کشورهایی که مبدأ حمله به ایران بودند از زبان کارشناس مسائل منطقه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/685667" target="_blank">📅 23:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685666">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYtsxx9R3Swp5Jl56fLGxP5aGGB7IAjWwPDyd9yjF8qG71Ep-wfJUAOInlBqi1YxlN9o1EJaecGhxcL8OdfriH8zCnieK2velFDRH_AiIvZicWvSvqN-HuMHUgpuyFM9abs-Sp1erWaqpXbPuIpqbiwY67FONFWV_sprGQE6Jr66oZzOdt4SOPp4uxN9g_eWwkVG7x90XpZZkGmfmtXeUASwp1QzYQkdJQjQRWXdQ6XDVvlXOc-wuk3P6Z2_QYgulhpK1AVG4rYguXTySl7wTx6e1hLxl12s8jnYNZga8EpetUTA5lpunlrtYTmxQfHumI-RlvCcawVddfFvd_wIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارش‌های اولیه از حمله دشمن آمریکایی به نقطه‌ای در لارک
🔹
بر اساس اطلاعات اولیه، ساعتی پیش حمله پهپادی دشمن به جزیره لارک در استان هرمزگان انجام شد.
🔹
برخی گزارش‌های اولیه غیررسمی حاکیست که بر اثر جنایت دشمن آمریکایی تاکنون ۲ نفر به شهادت رسیده و ۲ نفر…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/685666" target="_blank">📅 23:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685665">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e280c856b7.mp4?token=Mq1_9oK-jj-o7pxydOjDTIg4yO1a0wLiSndcgxOw3wJZdX096cdIW4FIzbBZj1vTaXDO0Y-z7P8Aagn22S6YMs0vkN2fIhnQsVj9awDs_3fyK2sjyzoPqGmp12uFKxwxGDxHDi0JWbsutSPrTCefDFXKaLNSTL1Zvcdou3A_P-GQchzA8FVq_cPUg493I_yN1H4qvpxfnjrSY-VaAWo_AFnciHNB7evdMslLDlKXmUyfyn6RQTFbwrdDXaq3Cqe264pEEeoiAUTZr3M4oldJmPQ5lhlp-u7y3k_rCoVn7F900UIb3NPHjkWJIGAzsKeMwayXuv-N9bNNFYCQ0JEZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e280c856b7.mp4?token=Mq1_9oK-jj-o7pxydOjDTIg4yO1a0wLiSndcgxOw3wJZdX096cdIW4FIzbBZj1vTaXDO0Y-z7P8Aagn22S6YMs0vkN2fIhnQsVj9awDs_3fyK2sjyzoPqGmp12uFKxwxGDxHDi0JWbsutSPrTCefDFXKaLNSTL1Zvcdou3A_P-GQchzA8FVq_cPUg493I_yN1H4qvpxfnjrSY-VaAWo_AFnciHNB7evdMslLDlKXmUyfyn6RQTFbwrdDXaq3Cqe264pEEeoiAUTZr3M4oldJmPQ5lhlp-u7y3k_rCoVn7F900UIb3NPHjkWJIGAzsKeMwayXuv-N9bNNFYCQ0JEZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دیشب در پرواز ایران به کوالالامپور بخاطر خم کردن صندلی میان چند مسافر درگیری به وجود امد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/685665" target="_blank">📅 23:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685664">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
انتقاد بی‌سابقه مشاور ولیعهد سعودی به رئیس امارات؛ القحطانی: بن‌زاید یک «رئیس باند» است تا رهبر یک کشور
سعود القحطانی، مشاور محمد بن سلمان:
🔹
ائتلاف ابوظبی با بنیامین نتانیاهو (که وی از او با لحنی تحقیرآمیز یاد کرد) با توهم تسلط بر غزه صورت گرفت، اما هیچ دستاوردی برای این کشور به همراه نداشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/685664" target="_blank">📅 23:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685663">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulki12YR2Vqg-tw_fCjURw47IrznqxxbGwfLaP_cXHfWhfY8EybQ-JhdfpGtFezWM7OqG0VdIpukLFm50th7xzjk5p09-S96q4-g2KVbfYICeiVxS-dAhThmo6vlkG6ZHqpA1rkeLj44ZEZSxoutqEPACuTPlczj3DDAvqC1vwXjZWhwJt9cLh-hbia-QtKVDCl82hoIcMLJJHTPXDb2vbMUb7LVHaZMEG04rBkUfTk5ZBAMgIRzi-SPjgSEvTCXHAFTLeat5op8HS4lhcw128AZhDebus0U35WS5tpXVTrLB5v2FgNZLDZljfNyqpysAoO79k6zomEn95sFFv-_8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرندی: رژیم ترامپ اشتباه بزرگی مرتکب شده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/685663" target="_blank">📅 23:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685662">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
شنیده‌شدن صدای انفجار در جزیره لارک
🔹
مردم محلی از شنیده‌شدن صدای انفجار در حوالی جزیره لارک خبر دادند.
🔹
هنوز محل دقیق و علت وقوع این انفجار مشخص نیست و پیگیری‌ها برای مشخص شدن جزئیات انفجار ادامه دارد./ فارس  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/685662" target="_blank">📅 23:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685661">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
یک نیروی امریکایی مدعی شد: نیروهای ما مین‌زدایی از خطوط کشتیرانی بین‌المللی در تنگه هرمز را به پایان رسانده‌اند
🔹
نیروهای ما از نزدیک منطقه را زیر نظر دارند و آماده‌اند تا از جریان آزاد تجارت از طریق تنگه هرمز محافظت کنند  جزئیات بیشتر
👇
khabarfoori.com/fa/tiny/news…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/akhbarefori/685661" target="_blank">📅 23:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685660">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zp1ws7bSTdaR5OsDDveOD8XLnrJpeDcB7HLa8ASACc4bElHOaCA_K1RITB3t6ENeBN3H8yxJzfwzU2lkzVDzlZx9wyYVPz5GOP2Ct7JE4Q6Ctgc8f1_CGytwRAs2AIUj_i5tyoSTNvPhPT5ntPPqcqDem1_D6iqbUuoSKng8DI4rbx7B85jSzerzyZori5mfTscj_v99JH9cj9A8eGJezw180Pf0Z56AUx8ubwqR9BSDdX0kkkBbX-wXxQm3LEn7lHSYGZhet-5sy2IQs67VH3HPTWIDI-q6TUOUdfjTkyA_BG71xs5Q_8VN0IYZNzAlJTrd-n_n3BfcPGwcY0qb0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهم: انقلابی در کسب درآمد با هوش مصنوعی
🚀
اپلیکیشن ایرانی‌ای رونمایی شد که تمام مسیر را از پیداکردن ایده تا جذب مشتری و فروش داخل یک سیستم انجام می‌دهد!
دیگر لازم نیست بین ده‌ها ابزار و آموزش مختلف سردرگم شوید؛ این اپلیکیشن با کمک هوش مصنوعی:
✅
مسیر درآمدی و پیشنهاد قابل‌فروش را می‌سازد
✅
محتوا و مسیر جذب مشتری را آماده می‌کند
✅
پیگیری مشتری و سیستم فروش را راه‌اندازی می‌کند
❌
بدون نیاز به مهارت یا کسب‌وکار قبلی
📱
قابل اجرا با گوشی یا لپ‌تاپ
💰
برای ساخت درآمدی واقعی و قابل‌رشد
🎉
هم‌زمان با رونمایی، آموزش اپلیکیشن و دسترسی به سیستم کامل آن در این نوبت داخل یک کارگاه آنلاین، کاملاً رایگان ارائه می‌شود!
همین الان ثبت نامت رو تکمیل کن
👇🏻
https://monetizeai.site/57
⚠️
ظرفیت محدود</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/685660" target="_blank">📅 23:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685659">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dc749d5ad.mp4?token=OG2K5RVGbL9QmgfB2wh6g-2zmvANDGSFCpdZ8_GqmQHcuqTLihKvMfiSvF0bfXg7y9IeQhtUAzwP4NgidXX4KwHha0853sLttg60vJO7Nlu2yZF2re31DtmBI58CVP_JGQbQA2A5LaBjlV3MVX1nhCmjzxiPHRsCiASqpUdlokANvkoj26HKmYB4vGYDHO2PvVgdaTZTZZC1Y9oni7rwwW-_mLVztxBQBWb_t0QvvzdMFEpg_0t7RGh_m3qZUVS8Y2I3MlTRxsx3sxhAFS_2FeYRVXTY7ezJuVNLzpD63gFyYRaLV746AAqRZ_6Jsk8B5aDEdEBzhDmavZE2mqya_TaRB1EZ29NazP1Q3JzW4I-n83d6VxJtsA1cPPYsSmk54x8CI1qLH1RgLMeLSIbfQsbkgc9eu1Gybh9jZIsaGoxG-kXLHQoD4zgCKVMeGC8ai6846ONxu0W9xX2glvoeeXgap2iHi9O93j_VCs9lCs1YEcOKXQKqzlfrKhwSM8Cs2Pq79emUIeqf9HEzXVOc9bxQlmJ2WtaMh1oJ0a0PXKGI7rty3cAFVPFTLwrbF3nc7luzb_zaI9fP8BXs0i_xylBeLnUCQmFZUeqR9lPps4Yre4wONOSApk-jMk5pkjFmnqyPv2S3CGrmtmetc9U74t8U0z1P_aNCsok_LLtDOpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dc749d5ad.mp4?token=OG2K5RVGbL9QmgfB2wh6g-2zmvANDGSFCpdZ8_GqmQHcuqTLihKvMfiSvF0bfXg7y9IeQhtUAzwP4NgidXX4KwHha0853sLttg60vJO7Nlu2yZF2re31DtmBI58CVP_JGQbQA2A5LaBjlV3MVX1nhCmjzxiPHRsCiASqpUdlokANvkoj26HKmYB4vGYDHO2PvVgdaTZTZZC1Y9oni7rwwW-_mLVztxBQBWb_t0QvvzdMFEpg_0t7RGh_m3qZUVS8Y2I3MlTRxsx3sxhAFS_2FeYRVXTY7ezJuVNLzpD63gFyYRaLV746AAqRZ_6Jsk8B5aDEdEBzhDmavZE2mqya_TaRB1EZ29NazP1Q3JzW4I-n83d6VxJtsA1cPPYsSmk54x8CI1qLH1RgLMeLSIbfQsbkgc9eu1Gybh9jZIsaGoxG-kXLHQoD4zgCKVMeGC8ai6846ONxu0W9xX2glvoeeXgap2iHi9O93j_VCs9lCs1YEcOKXQKqzlfrKhwSM8Cs2Pq79emUIeqf9HEzXVOc9bxQlmJ2WtaMh1oJ0a0PXKGI7rty3cAFVPFTLwrbF3nc7luzb_zaI9fP8BXs0i_xylBeLnUCQmFZUeqR9lPps4Yre4wONOSApk-jMk5pkjFmnqyPv2S3CGrmtmetc9U74t8U0z1P_aNCsok_LLtDOpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیست‌ونهمین نمایشگاه بین‌المللی الکامپ، فرصتی برای دیدار، گفت‌وگو و همراهی با تازه‌ترین جریان‌های فناوری و تجارت الکترونیک.
۹ تا ۱۲ شهریور
ساعت ۸ تا۱۶
https://t.me/ElecompOfficialNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/685659" target="_blank">📅 23:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685658">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حمله مجدد رژیم صهیونیستی به نبطیه الفوقا با بمب‌های ممنوعه فسفری
🔹
شبکه المیادین گزارش داد رژیم صهیونیستی، شهرک النبطیه الفوقا در جنوب لبنان را بمباران کرد.
🔹
این رسانه افزود اشغالگران صهیونیست در این حمله از بمب‌های ممنوعه فسفری استفاده کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/685658" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685657">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
ادعای الجزیره به نقل از مقام آمریکایی: دو موشک‌انداز سپاه پاسداران ایران در جزیره لارک را هدف قرار دادیم/ آن‌ها در حال آماده شدن برای شلیک موشک‌های حامل مین‌های دریایی به سمت تنگه هرمز بودند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/685657" target="_blank">📅 22:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685656">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ادعای نتانیاهو کودک کش: ایران می‌خواهد برنامه هسته‌ای خود را از سر بگیرد و بمب اتم تولید کند
#Demon
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/685656" target="_blank">📅 22:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685655">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای یک مقام آمریکایی: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/685655" target="_blank">📅 22:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685654">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ادعای یک مقام آمریکایی: نیروهای ما امروز دو سکوی پرتاب موشک سپاه پاسداران ایران را در جزیره لارک بمباران کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/685654" target="_blank">📅 22:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685652">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd1d589582.mp4?token=g8iOrz5qW0G41AV6y0IVTdSM3hFj6380qVYR-3wD3gC6K6w4vndauWXHUApIMYIuvlgpQSu3QlS2E3cJbgABnM6l--pK7hPkU4WkHlj0UUUqZ2hR9_KpYZdbjvSUC4F0stmwIGWhY17Pf0C08pmk1vqP9GJ3vSCF8K3FlDpC5Tq9TLc7GYqIcgx6BenRJp90GtfBYa_R4SibOl4m80GpT3BRa-DOx6zOfy1fJc-ZbD1MLAz_6rSPX81POHqK5RL6hPK5Zg84auHngpjrvNISh-J0hb_ma79sBj2S2upJIPAxAjnaIQj3xV7f4o-_hpDjhw57wV1rzBIBOL3Xl4PAjaqkYCFxprVoxNKm3CoiPzgigvndEGYXDwn3ZSBYJRyTG6pNOrA4LQYwsW_ZcNOJ21oiMxnGyUZoJMwTGn9FpU40eUnmQ0e9k4y0XPawNQNmnkF2PdB1WrqSkGcAoessCe34X0Gydh-c3ODXPAej6gQphOuEaJeer0ElBF-c2N7-Ct47pOXZzCzuovHgp-h7JOVe2jqD-ZPp4IE8xl9HSOOAr3q8YmankpXIdWz7-efQr1Odbuc08qicZwYrG4DgZ7hL7dInt6A3Di93fZn40hY6hqfmOwGhnI4gl2LeR4-D8SlIfvNIpIfmOlaxKMrmK-O4pMCuZR2k1WXyiZ_KISM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd1d589582.mp4?token=g8iOrz5qW0G41AV6y0IVTdSM3hFj6380qVYR-3wD3gC6K6w4vndauWXHUApIMYIuvlgpQSu3QlS2E3cJbgABnM6l--pK7hPkU4WkHlj0UUUqZ2hR9_KpYZdbjvSUC4F0stmwIGWhY17Pf0C08pmk1vqP9GJ3vSCF8K3FlDpC5Tq9TLc7GYqIcgx6BenRJp90GtfBYa_R4SibOl4m80GpT3BRa-DOx6zOfy1fJc-ZbD1MLAz_6rSPX81POHqK5RL6hPK5Zg84auHngpjrvNISh-J0hb_ma79sBj2S2upJIPAxAjnaIQj3xV7f4o-_hpDjhw57wV1rzBIBOL3Xl4PAjaqkYCFxprVoxNKm3CoiPzgigvndEGYXDwn3ZSBYJRyTG6pNOrA4LQYwsW_ZcNOJ21oiMxnGyUZoJMwTGn9FpU40eUnmQ0e9k4y0XPawNQNmnkF2PdB1WrqSkGcAoessCe34X0Gydh-c3ODXPAej6gQphOuEaJeer0ElBF-c2N7-Ct47pOXZzCzuovHgp-h7JOVe2jqD-ZPp4IE8xl9HSOOAr3q8YmankpXIdWz7-efQr1Odbuc08qicZwYrG4DgZ7hL7dInt6A3Di93fZn40hY6hqfmOwGhnI4gl2LeR4-D8SlIfvNIpIfmOlaxKMrmK-O4pMCuZR2k1WXyiZ_KISM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ازدواج زوج‌های «آدم و حوا» همزمان با میلاد پیامبر
🔹
همزمان با میلاد پیامبر اکرم(ص)، مراسم ازدواج چندین زوج جوان که آشنایی آن‌ها از طریق سامانه «آدم و حوا» شکل گرفته بود، به‌صورت زنده از شبکه دو برگزار شد.
🔹
این زوج‌ها مسیر آشنایی و انتخاب همسر را از طریق سامانه «آدم و حوا» طی کرده‌اند؛ سامانه‌ای که روند آشنایی را با محوریت خانواده‌ها و والدین پیش می‌برد تا آشنایی‌ها در چارچوبی خانوادگی و با هدف ازدواج شکل بگیرد.
🔹
در این مراسم، دکتر عزیزی نیز حضور داشت و در سخنانی بر ضرورت مهیا کردن شرایط و فضای مناسب برای ازدواج جوانان تأکید کرد و تشکیل خانواده را نیازمند فراهم شدن بسترهای فرهنگی و اجتماعی مناسب دانست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/685652" target="_blank">📅 22:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685651">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
وزیر راه و شهرسازی: پل‌هایی که در هرمزگان مورد تجاوز دشمن قرار گرفت طی یک ماه آینده بازسازی می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/685651" target="_blank">📅 22:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685650">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/587c8b5a56.mp4?token=sJ5TaOy2wJV_9883OW-z7n7sAdutu8Zg4EbZ1BKjGH5HchcZATd_r6M2tW4_gHX0CAcYTwJCfchP5Y8xCe_nsKBukO-r8pmTIzfmRg5lVb6zPiyKDpEHqwW1CncRyTGUe8n_Yi4Htbs1DetLSg-ULNd3IUcvIm-h7LyQlIj99ApbCKv17cmcXcOYv5y3oyNhaZR2mTkLuMubDovWLd-xzTM3XcxwojO8Q6YRHYVilHy1EfvPob_p025_wYi9SHtFNNAEatCX3sMt7thjzTFkTEk4DlJAOg4H-BoKnALnTQ8YZy3L1qyq1sImJgoBcnJRGrcYleBUuD9D-eyhf20_TTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/587c8b5a56.mp4?token=sJ5TaOy2wJV_9883OW-z7n7sAdutu8Zg4EbZ1BKjGH5HchcZATd_r6M2tW4_gHX0CAcYTwJCfchP5Y8xCe_nsKBukO-r8pmTIzfmRg5lVb6zPiyKDpEHqwW1CncRyTGUe8n_Yi4Htbs1DetLSg-ULNd3IUcvIm-h7LyQlIj99ApbCKv17cmcXcOYv5y3oyNhaZR2mTkLuMubDovWLd-xzTM3XcxwojO8Q6YRHYVilHy1EfvPob_p025_wYi9SHtFNNAEatCX3sMt7thjzTFkTEk4DlJAOg4H-BoKnALnTQ8YZy3L1qyq1sImJgoBcnJRGrcYleBUuD9D-eyhf20_TTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علائم کمبود ویتامین B12
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/685650" target="_blank">📅 22:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685649">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
رئیس کمیسیون اجتماعی مجلس: افزایش مبلغ کالابرگ به ۲ میلیون تومان در دستور کار است
رئیس کمیسیون اجتماعی مجلس شورای اسلامی:
🔹
افزایش اعتبار کالابرگ الکترونیکی از یک میلیون تومان به ۲ میلیون تومان در دستور کار دولت و مجلس قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/685649" target="_blank">📅 22:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685648">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
وزیر راه و شهرسازی: پل‌هایی که در هرمزگان مورد تجاوز دشمن قرار گرفت طی یک ماه آینده بازسازی می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/685648" target="_blank">📅 22:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685646">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0be860cf9c.mp4?token=k6ie-PspXb1PMueeLtUUjJbT4dCTz-gcdsTCixnECr7plib39W2uLA1c8BQUEdAXDHc5OeX-3RAiKi8_retgoMxO8Byah3If-rfJz3J_18EXpZ2oLbWzrtIwyr5dIJe1J-EVdfRShhwrrukrWjzg5vqJyDebBfhJeDYopWkBoQyZ5Nfnyil9lURXQenpFkeXIdQCv9QB-xF6jTsVriYg4Q9Y0j1nJeOu6Ea7HwcUtEuTUnvPdyE7nuUsCQ8hYG0fSorQ41LXW2Jet610Q0ABJPJLIiVKvhtBsT58ml_dlRve2Jxhk_jwlQ5_Yw7FzpkryDgO7P1ouJ_WPo4uD9jsmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0be860cf9c.mp4?token=k6ie-PspXb1PMueeLtUUjJbT4dCTz-gcdsTCixnECr7plib39W2uLA1c8BQUEdAXDHc5OeX-3RAiKi8_retgoMxO8Byah3If-rfJz3J_18EXpZ2oLbWzrtIwyr5dIJe1J-EVdfRShhwrrukrWjzg5vqJyDebBfhJeDYopWkBoQyZ5Nfnyil9lURXQenpFkeXIdQCv9QB-xF6jTsVriYg4Q9Y0j1nJeOu6Ea7HwcUtEuTUnvPdyE7nuUsCQ8hYG0fSorQ41LXW2Jet610Q0ABJPJLIiVKvhtBsT58ml_dlRve2Jxhk_jwlQ5_Yw7FzpkryDgO7P1ouJ_WPo4uD9jsmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روش کاربردی تا کردن کت برای گذاشتن در ساک و چمدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/685646" target="_blank">📅 22:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685645">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_1StuqwNH5X6mFEY9SF6URiLj13Llx_fj1-2HxsgtnJEU1ntNoQdIrtmzx-jcPNCzu0K1HeztOrdxWPLD9t8GnUJHEHivUH1BPqw1ouiHpL4al5dAzbdY7ITXBVbq7wZnw21VRAReB4EijTITvIq0xTFI7qfDPozcMwdIvqQtEZzKm6SRENwMcsx3cYTLqVxUH0Q3Bf9sWuhEBZFa21Ik3Kjks0Td782_RVOqVj6IEH-ataAFGf1izpBzVHB968vQxaRKdRGZQK0OtHJK7y94WUMzhohKs9DZpr-NijflovQNWKPohowSBfCpyMV_eiZ0MEfAZQmYLyYTyrZojtGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
علاج مشکلات امّت اسلامی، اتّحاد کلمه، دوستی و تعاون در مسیر خیر و نیکی است
🔹
بخشی از پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت | ۸/شهریور/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/685645" target="_blank">📅 22:14 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685643">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
حقوق نیروهای شرکتی از ماه آینده به موقع پرداخت می‌شود
رئیس سازمان اداری و استخدامی:
🔹
با تصویب طرح پرداخت به ذینفع نهایی، دریافتی نیروهای شرکتی از ماه آینده همانند رسمی، پیمانی در قالب سامانه‌ای تشکیل می‌شود که تحت نظارت سازمان اداری و استخدامی کشور است.
🔹
کسورات آن‌ها بدرستی کسر خواهد شد و حقوق آن‌ها نیز به موقع پرداخت خواهد شد و تفاوت‌های موجود در دریافتی این افراد برطرف خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/685643" target="_blank">📅 22:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685642">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UY58pNScTvsC335SRjALFS29NGxR62q-OFOfHvK91Ow7OLXFyjHMVs3eA0ZXaxBUaO_-ak71C7G6UgKb1Jd3IqdsLRbRbLnScrKImQygulkVJAm72ZznbQgpAuQFcBUwQu3x5k3DpTcT--gigF36EHDlud6lhLtM_9y5cTQsOeKQ2cMQj2K1CTU6mlebDmgDfygxVa2fhx-JF1KXpQCUvzne4b68CRAHV2ujbAqSeLF5pA2FvFy8L3pXFn-uCDo592PqfKDz-AkxrNIyV6-W-YCOtjRPtMwmHe90frB0dP2sBxmD4BrvGotPtWZPAs761yDu9wpO432LcA19QfpIuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف قرار گرفته شدن یک نفتکش در تنگه هرمز
🔹
سازمان عملیات دریایی انگلیس خبر داد که روز گذشته یک نفتکش در فاصله ۱۲  مایل دریایی شمال شهر خصب در کشور عمان مورد اصابت یک پرتابه قرار گرفت.
🔹
این نفتکش هنگام تردد از تنگه هرمز به سوی خلیج فارس مورد هدف پرتابه ناشناس…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/685642" target="_blank">📅 22:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685641">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwF9pT966o0w2YfZYNhJdA38s-r5nwBJEPXjC87dCMXj1b7oZOGvPtgsw8PWTUnF-lXwnWF_L8hgiMrgA-9B8AoRU6eEQsRMzz-ENizymYj8tgwAlpmsjzizaTMl2IM9ZVSqB6GfeXmHe9s4QKwHrLlv3NLhnAT50EcsmX_vUNEfl05TOSWYhStHjGLpnSICz__Ue1t1q4Lfsgy-h8zEGgXZfzERptEi_CpOAiYLGgfuDyqguNEiEO5CHVf9Lp7YK4pTt1aE9SET_9ldWdpE-zzkpyMzcz7HVgTx3UwNT3SbX18r1-PskNHvmj_BO6jurLvNi7mizguJsvlGiAIuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران نوین در مسیر تبدیل‌شدن به یک AI-Native Agency
کانون ایران نوین به‌عنوان حامی رسمی الکامپ ۲۹، امسال با رویکردی متفاوت در این نمایشگاه حضور خواهد داشت.
ایران نوین در حال توسعه یک Digital AI Ecosystem است؛ اکوسیستمی که با اتصال دانش، مهارت‌های تخصصی، تجربه کاربری و هوش مصنوعی، در نهایت به طراحی و توسعه AI Agentهای تخصصی در حوزه بازاریابی منتهی خواهد شد.
هدف نهایی این مسیر، حرکت از «استفاده از هوش مصنوعی در آژانس» به سمت ساخت یک AI-Native Agency است؛ جایی که AI نه یک ابزار جانبی، بلکه بخشی از معماری و فرآیندهای آژانس خواهد بود.
«آینده‌ی برند و بازاریابی، از اینجا آغاز می‌شود.»
📍
نمایشگاه بین‌المللی تهران | سالن‌های ۸ و ۹
📅
۹ تا ۱۲ شهریور ۱۴۰۵
⏰
۸ تا ۱۶</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/685641" target="_blank">📅 22:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685640">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRRGsDUXPQJKEzS2xdes7oNiaDz_uoBaqkOgQ2WbHpdeHAnRA1W45dz1phLd8uuoBJDLX2lWZnxXpb6BX954JEGiC-ZA02YQJXNX0Pz0DMYFVGMHkl4ZIbobazmNZJXfLsW2K7-cT0zBephFfR555BPjHmnki6Vdh2UNgI4lFMKTD5AozTM9f3P-SURiQ6sp_qSj9VmmEqyKe1AMnKyCmffzzkH2gyojB52_jfbTiXHWbcNrh3wRCY4TiAG5XZWFkyF_R4mGYbKTfMDCK-EMnBng9LO6C7TLldaAT9Yneh-pxX6bxmehYKec9_szw30a6-tV24qc7hHi609BSHRltA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه، به‌طور کامل بخشیده می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا 2میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/685640" target="_blank">📅 22:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685637">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1dyGh0VBViijdZk7R78EJeB_F8QeCp5nf6VZY2XySWajmHrZq-EfIphJqo7a16-ah7M65ueYKRbJy6ZT4qCZ1-lzuUPaMF3nqkjnrLO8PdEymCOTjlKuIlVuf-_ZU1GtpUSq4EkjV4atS7LvekKEO1dXdq1MlOJlX6AjICOVEhtTnB1ccaDmwWn_0QJDeFh7MmzGKLwvxXdM9JtTO_V4X12JdQcYI_ofTjXwCkeBTaPqTwIj3dmBfPx-Q3qIi0GiZW5m9AlQ5vR8Y0hpLME0uZNAJVnsjKxIQ3wu6DW7FCkK0NAqa-wJ3gwh2Ss_RvWVihuxkonw0CJZKwLDG6aJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوکیا ساده هم به ۸ میلیون تومن رسید
🔹
گوشی‌ای که سال‌ها نماد ارزونی تو بازار ایران بود، حالا به قیمت عجیب ۸ میلیون تومن رسیده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/685637" target="_blank">📅 21:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685636">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a490610f9.mp4?token=OdIfQLEOEi1gpq0AUglJ9SNkqnu0cm-rGwrSXhLcZNJFRdHqSU7n0FxZksvkjtU28UFlc_--mnCazOraq6ppYTRfEDNnZp_HM1HJzfGxaW7X9iN1E8QCtStoLD9c2djQ7cmvRGSWx2FomKiqhp7X3KxK0Km15YYTO4xEA5JJRiWaNATRF_ZJoucWDFBn1rxhVuauw8OMbRmFNcxQ2c6yA73nMfTssa9YxsYG1F3dQBRvGE0PJEbuxE73EsmSnesWP31BdoNpP8i6JOCM8V2EKb290Uc0hOVe0wUfabCF38aICHh24qMX59WsB1JCa-6ItBH7cV3EJfkUXsJXenEFOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a490610f9.mp4?token=OdIfQLEOEi1gpq0AUglJ9SNkqnu0cm-rGwrSXhLcZNJFRdHqSU7n0FxZksvkjtU28UFlc_--mnCazOraq6ppYTRfEDNnZp_HM1HJzfGxaW7X9iN1E8QCtStoLD9c2djQ7cmvRGSWx2FomKiqhp7X3KxK0Km15YYTO4xEA5JJRiWaNATRF_ZJoucWDFBn1rxhVuauw8OMbRmFNcxQ2c6yA73nMfTssa9YxsYG1F3dQBRvGE0PJEbuxE73EsmSnesWP31BdoNpP8i6JOCM8V2EKb290Uc0hOVe0wUfabCF38aICHh24qMX59WsB1JCa-6ItBH7cV3EJfkUXsJXenEFOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عملکرد جالب دستگاه فروش خودکار از موقع پرداخت تا تحویل کالا
#موشکافی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/685636" target="_blank">📅 21:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685635">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QahA3tbCtFNK6B2c3X5_hl1jI5OoKfCVpFyfqFJ_kyglC46Guhxup0o_YP7BgP1uBAB5KtN9vOq04Kx2-lmIyn66Ias5gwzB8uetu57qxI-vTthHFwSmXp0ToAq7DUFYnbxYJA-eQy9h7XPnfNGr0BwJFLQtEa8sq-RgV9PsmdCRSSDIl0E9Z3JKYw8Ah-uCdqLP7-Zco-Nrt7SdE2LJlpbK3Sv3qecWRW1UbpP9C1Auxi8WQwLWV2sNU9ahofZqWtgM54TJpat3GsPH65oDzSHyXNKT8z4ulgxl48yfMHBzy8rMczobSUgZZHvS9VbTJIIDSlPk-vBVHV6tL1RhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای مرموز فرار پسر نتانیاهو از آمریکا/ چه کسی دنبال ترور «یائیر نتانیاهو» است؟
🔹
چرا پسر نتانیاهو را به سرعت از آمریکا خارج کرده و به اراضی اشغالی بازگردانده اند؟ آیا واقعا قرار است گروهی نتانیاهو را ترور کنند؟ آیا نقشه ای برای دزدیدن پسر نتانیاهو کشیده شده است؟ آیا میان شایعات در رابطه با ترور پسر ترامپ و حوادث مربوط به پسر نتانیاهو ارتباطی وجود دارد؟
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3241559</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/685635" target="_blank">📅 21:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685634">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8fbf2e61.mp4?token=Na6QjscnvqawcxmhtusLoej6wPvXxvuJbYXnUIK7j66PbkMjMThpL5AIqgqxwG8rlmVRwaQBaW65TQtqCN4jWogakXanCz0hJ444GFHZhjmQwtaD3GX3uyNWwEQUym8alHy1aiLzTHxPG2jDY7RQoep7Frd0y4-er6XkzyXH3PcxL1-kO-Oa-ewCiVa5AJpARoZs3t4rGq99avNEWQcf21DUKeHWqM_LuYs-vRilTAKdxb4PKBsdx0hSbaYsxID1ea9WXUjJ9h0x59An_KLPMXUtr51JdiKlBYfY0C_NMji7LldAKXeuoceljvs9n3KGz36z4AKpJnm5Z61iIRncDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8fbf2e61.mp4?token=Na6QjscnvqawcxmhtusLoej6wPvXxvuJbYXnUIK7j66PbkMjMThpL5AIqgqxwG8rlmVRwaQBaW65TQtqCN4jWogakXanCz0hJ444GFHZhjmQwtaD3GX3uyNWwEQUym8alHy1aiLzTHxPG2jDY7RQoep7Frd0y4-er6XkzyXH3PcxL1-kO-Oa-ewCiVa5AJpARoZs3t4rGq99avNEWQcf21DUKeHWqM_LuYs-vRilTAKdxb4PKBsdx0hSbaYsxID1ea9WXUjJ9h0x59An_KLPMXUtr51JdiKlBYfY0C_NMji7LldAKXeuoceljvs9n3KGz36z4AKpJnm5Z61iIRncDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دبیرکل خانه پرستار: اگر کشور با کمبود پرستار مواجه است، پس چرا ۶۰ تا ۷۰ هزار پرستار خانه‌نشین هستند/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/685634" target="_blank">📅 21:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685633">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhHw5VXCVxg1q3YsyYXBR3f0LiFX0ufm4h4TNUY9x9pVBWSeFGrd1PAIVRJ-iA37y195XPV-xe_STDZK_FvQw_gTsSL4rbqJy69xwVgXVh-rMVGvUrQXdObUWq_6HJcclKmskMG3GZ-lAA7BUTtZsPeWsu0MTVdjSN44OQjH68gssz-7git-7-FC8Er_9wTPKnFITKM9Qj6k88T0NBkIMSXdFZKAivYme6ewiNnXqPymfcmFBV0raZbcRcA-DSsByuRX3rborKPrCIiTg0HbwTI-g7Kf8CXv6jElycmhBqwFLjAFOt5wyja-blGYDOdhQEzbf6H8x9gpniob0kmgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان اطلاعات سپاه: دشمنِ مستاصل از مقاومت ۲۰۰روزه ایرانیان، «فرسایش ثبات و تاب‌آوری ملی از مسیر جنگ روانی» را دنبال می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/685633" target="_blank">📅 21:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685632">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb9e28a81.mp4?token=DUx5o4IOk5oVgYzQvz4HakFiZgcEwfD-E4M1mmkEIg6MHSqjRFaCn9FTsKcxfLO3WK_nyBHmgkfCq1ekwVLZ7oVa8grIw6Dkwgj5dLmLlwSOaUpcajCNEkPC6u5FT9HuSDnYdOZ1YsgVOvYHUsbcIiLm2HCcx8nHKgNTaHzOXxTg5GJmdAiPrzlt2lvvIQqa3YAARxa4C06oxzuL5btzZviNSBufIO6Su4QsM0XgixFodt3CVITAx_eBdEv1V_nGzNF7RX_hcjNUrtswkHEtjPmFru6NNd4s3UlMMKTl2XDRgDbkmA5882rwZkOBMjomipwqATudoUshZNMtuygO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb9e28a81.mp4?token=DUx5o4IOk5oVgYzQvz4HakFiZgcEwfD-E4M1mmkEIg6MHSqjRFaCn9FTsKcxfLO3WK_nyBHmgkfCq1ekwVLZ7oVa8grIw6Dkwgj5dLmLlwSOaUpcajCNEkPC6u5FT9HuSDnYdOZ1YsgVOvYHUsbcIiLm2HCcx8nHKgNTaHzOXxTg5GJmdAiPrzlt2lvvIQqa3YAARxa4C06oxzuL5btzZviNSBufIO6Su4QsM0XgixFodt3CVITAx_eBdEv1V_nGzNF7RX_hcjNUrtswkHEtjPmFru6NNd4s3UlMMKTl2XDRgDbkmA5882rwZkOBMjomipwqATudoUshZNMtuygO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دزدگیر گاراژ بهانه‌ای برای یک دوستی شیرین؛ مردی که بازی کودک را جدی گرفت
🔹
مردی متوجه شد کودکی هر روز وارد گاراژ خانه‌اش می‌شود و دزدگیر را فعال می‌کند. اما به‌جای شکایت از خانواده‌اش، برای کودک مسیری نقاشی کرد تا بتواند همان‌جا بازی کند و بیشتر خوش بگذراند. هر بار که باران خط‌ها را می‌شست، دوباره آنها را برایش می‌کشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/685632" target="_blank">📅 21:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685631">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0BpiZxlYCMbvogg6WaIPTZOJE-CRxH8RSHzbDoHmv3T919_EHqsNmAkJngNO-4_Vreu_P4xtcRchDS9tTTlBCnZhqLwACjKRCJ0sALrmAg3VPTYAMyETbWTrONqIo1VKtb7A50nTBZlVIxTClBLi1szmgkxm09F9TPFxTGow_UV1hCcMX7q2T2QLLFW1_oyfbnr9RzDVUiM-pH_dtD3ud1CZCoMGO_YfRB28KQiec4rh1_p4U1FiO4fHbHA4j4-TA7y2PIDCG_KNQ7VYpO8X3NcE-nTW7_EaGLqgWhaaMrtcO424kJyEqSuHitCS8pBvatjRWGWpggls3HDjHvQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهمینه ها هنوز هستند،
تنها جامه شان عوض شده...
گراد، با حضور خود در دنیای زنان، به سراغ یک روایت اساطیری رفته است؛ نه برای بازسازی چهره‌ای از گذشته، بلکه برای بازخوانی معنایی که هنوز در زندگی زن امروز جاری‌ست.
زیرا زمانه تغییر می‌کند، شکل زندگی تغییر می‌کند و جامه‌ها نیز؛
اما بعضی ویژگی‌ها، همچنان بخشی از هویت ما باقی می‌مانند.
انتخاب. جسارت. خرد.
این‌بار، روایت این زنان را بر تنِ امروز می‌بینیم.
www.gerad.ir</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/685631" target="_blank">📅 21:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685629">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554cabedad.mp4?token=e2e9AuE0rF7MG0X5cMHLc046PfDqEp_qcmb6k2iM22kn4Nuh47HWXOKvPUoG3gyRk6tl12sHrd7EMtVBU5JO7VHR4YTpDdWlyB4M5A9pyfHYeEr4WNmPyiokzbRa9APt8fJE_-VDk986UZ55OJ3IzBLQLTodzVzSBU6p20m4rIP0ZZmKOHwiF8P0LUmY1ldXXrKXRvH2jBodyWH7JBdYjbkAFEH_0SRE0aCnhzKYKi1POyFJ2buVScXiUBmwqBoFP6_Xt1cVacQassDVdMWgiRS3q9rKGlGb6zY3POj7AAEcc1HCcEivD55kgIvZe4c3ak7WFqkHGtLh3wj2Bzxwcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554cabedad.mp4?token=e2e9AuE0rF7MG0X5cMHLc046PfDqEp_qcmb6k2iM22kn4Nuh47HWXOKvPUoG3gyRk6tl12sHrd7EMtVBU5JO7VHR4YTpDdWlyB4M5A9pyfHYeEr4WNmPyiokzbRa9APt8fJE_-VDk986UZ55OJ3IzBLQLTodzVzSBU6p20m4rIP0ZZmKOHwiF8P0LUmY1ldXXrKXRvH2jBodyWH7JBdYjbkAFEH_0SRE0aCnhzKYKi1POyFJ2buVScXiUBmwqBoFP6_Xt1cVacQassDVdMWgiRS3q9rKGlGb6zY3POj7AAEcc1HCcEivD55kgIvZe4c3ak7WFqkHGtLh3wj2Bzxwcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی تماشایی از رنگین‌کمان در پس‌زمینه کوه‌های یخ شناور در نزدیکی گرینلند که در شبکه‌های اجتماعی سراسر جهان پربازدید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/685629" target="_blank">📅 20:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685628">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13dc475bc0.mp4?token=VSCk_KMMWrlsNKHyib_0P7areIxQyTkFVnpgoDCS3s8ot72Nlgp1_C3UNs95Xs4UtT7OTxbfF4YvE1fu159G1MbLzwLB3wztdS5kWpkd0otMfS_I7f_hdQ9jM7h9kHL472iGattmIoOK4Ir133CZ8y_9UmjpXfcUMFpESv-QnYLeRVcfJhBWWOu75LMGwlIbzv4PcZUARqzpWyebCRyAjHRfRF133sf_P85_Y92LLsrHufC5LKGd_OsxVJiojAFgTmEb-d78hQw8stPqc0ybTjns_6q54s7YrgItjbnyu5m_j0Yy5gtNEnPuEuVUNu0_28z9saVDdcvlSzdsYRnHJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13dc475bc0.mp4?token=VSCk_KMMWrlsNKHyib_0P7areIxQyTkFVnpgoDCS3s8ot72Nlgp1_C3UNs95Xs4UtT7OTxbfF4YvE1fu159G1MbLzwLB3wztdS5kWpkd0otMfS_I7f_hdQ9jM7h9kHL472iGattmIoOK4Ir133CZ8y_9UmjpXfcUMFpESv-QnYLeRVcfJhBWWOu75LMGwlIbzv4PcZUARqzpWyebCRyAjHRfRF133sf_P85_Y92LLsrHufC5LKGd_OsxVJiojAFgTmEb-d78hQw8stPqc0ybTjns_6q54s7YrgItjbnyu5m_j0Yy5gtNEnPuEuVUNu0_28z9saVDdcvlSzdsYRnHJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین رباتی که رباط صلیبی پاره کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/685628" target="_blank">📅 20:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685627">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0P6ckGp-PfQiyUsKHzB6p-ArhpY3BgnuBk8b-DHabLGaHMVuRcgZ6qj1EURgzBkm5-ZQ_cxrGlOyRPfeRWiV26NGvZwPT5k4-41Ff13otfbLu44aMnH8qCFVTnV-A6wtTPn1qJQoF83tdNaMvJWml3CzIZp8IPgS7HAc4ct7OLFP5ljvQHhx78Le5pqBzE09hYlxEp_gejy2wuYbVLdSGM4RuUaDl6T29E15HflZb0-y_RFoCb605FGgKssWTM9LuZDYszIJRNumZUp1vjKptwT3X3dWtKJKr8qazG3QuVrtOa59yClsBHoANIpT3gSXx9tQ1eiGE3zO1aDCaD7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ راهکار کلیدی برای حل مشکل ناترازی بنزین
🔹
حل مسئله ناترازی بنزین در کشور نیازمند اقدامات هم‌زمان در بخش‌های زیرساختی، پالایشی و الگوی مصرف است.
🔹
از مهم‌ترین راهکارهای کلیدی می‌توان به توزیع عادلانه یارانه، افزایش ظرفیت پالایشگاهی و مهار قاچاق سوخت اشاره کرد.
🔹
کاهش مصرف خودروها، مشارکت بخش خصوصی و اصلاح کل زنجیره تولید تا مصرف از دیگر راهکارهای این حوزه هستند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/685627" target="_blank">📅 20:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHyoXkqWdKLlzJSD5vJ1E8ImafVegPW2WWgDdCPOzOOtALZm2XloG4Kn0Fx_q4CH-pov5Jqz2rLgCQa-1p_EaKcQilSmBMHz5oG_tCWFe2cicIe6so7HPJHa8z1rMCTnEQBSnxQHHDvbTxb5dYQVCZAd2Z-qx3ycNRowrUly_kvSCnbixpHHVBwONnK1marrkHe4zfZQRVWsYX_pmcLbVbB8Zm80MZWWJvRZBtTIYzskNR55TJE4bSoWuXzpvSYypIdaD4Cx_d1txuc1e5h8jPx0JO6hHGHNyNmx5VbcwYIxV5uZWn2UQWl91V6KpqrCM8uox6C0kWfMAZz7hL5gPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تانکر ترکرز: میانگین روزانه صادرات نفت خام از طریق تنگه هرمز طی هفت روز گذشته ۳.۸ میلیون بشکه در روز بوده است
🔹
در دوره اجرای تفاهم‌نامه (MoU) که عملاً تنها ۲۵ روز دوام داشت، این رقم ۹.۸ میلیون بشکه در روز بود.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/685624" target="_blank">📅 20:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
یک توقف کوتاه در یاسوکند؛ استاندار پای درد و دل یک مادر نشست
🔹
استاندار کردستان پای درد دل مادر سالمند ترک‌زبان نشست.
🔹
در جریان سفر آرش زره‌تن لهونی، استاندار کردستان، به شهر حسن‌آباد یاسوکند بیجار، وی هنگام مواجهه با یک مادر سالمند ترک‌زبان، از خودرو پیاده شد و پای صحبت‌های او نشست. این مادر برای بیان مشکل و خواسته خود به استاندار مراجعه کرده بود.
🔹
لهونی نیز پس از شنیدن صحبت‌های او، از همراهانش خواست موضوع را پیگیری و برای حل مشکل این شهروند اقدام کنند.
🔹
مسئولیت یعنی شنیدن.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/685623" target="_blank">📅 20:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هزینه بسته‌بندی کالا ۲۰۰ درصد افزایش یافت
بابک عابدین، رئیس اتحادیه چاپخانه‌داران و صحاف تهران در
#گفتگو
با خبرفوری:
🔹
حدود ۸۰ درصد هزینه بسته‌بندی کالا مربوط به بسترهای چاپی مانند کاغذ، مقوا و فیلم‌های انعطاف‌پذیر است و افزایش قیمت این مواد باعث شده هزینه بسته‌بندی حدود ۲۰۰ درصد بالا برود که در نهایت این افزایش قیمت مستقیماً به قیمت کالاهای داخلی و صادراتی منتقل می‌شود.
🔹
قیمت مقوا، یکی از پرمصرف‌ترین اقلام صنعت بسته‌بندی، از کیلویی ۷۰ هزار تومان در مهر سال گذشته و ۱۸۰ هزار تومان در بهمن، به ۳۶۰ هزار تومان رسیده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/685622" target="_blank">📅 20:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685611">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aVTBhhQGClf4BRKMJ5UI6PMJNFxRhFpASwWE_IARcrMZPLdOGvz46984ttg-mlKjTtPB2B-2r8NyL2U7QbmdzhCfJmf_QVuKW0qvwUKGJDkl8VBLgW9JQaUyh83Ho5R6kIOp94-2250K9CdH6DdPxHYQrvCGW_6qVw2lCMhAeGvazJUVfFCcnrDks6MvwF6C_y4RuoQyPPFmC0sb6fBn3oZz2J8wGuMVVwg11qHfRFRXauxFG5P5tmGZSWNcXcq2N5hX6L_FN9Ca7LEeg2odUWUnW91bfjrgsG_qt5Y18kT9iWGgh77ckU66N_X70MTa_wgrX42IauvFx4c7mcqUvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbzCPiVCUYl2A-0V4Ql0-SVKGvEFoMqVlt938UZofwzO5DYkFPTHwyW6TzVq4Z-C6SX3NJYjjhpynh3GyppMyK3-scNgnNDIWJ_6l-Tw3NULU5S2XOixJzxexbD8vO9iCtxcfqpjytmVh4KLAcLDb0Kr366H5SIpaRRHyV_hG0PJ6AtZUyniNkEhW488hToKqWX8BtRbTpOR_0m2jqW02kUDOc56j_yuuCeBqbBRHIsfrJuB6fH2olGPVg1ZA4FD56YMOL2RKmy1Yj2QPygfjPBgD2gQD2WcAUgkQZct3_cxwfH2-H68sN6J68Q1ZaURWLh0hb41Su8aMRIBcq0WuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ArPVtHyQ5nM_Oq9NdjTQ5GPZTLVG-wXQnicKS_CJTh14XB7bBc70lD19NUzmxekABV2s9Zl9KV5ZO8xr0oI6hNQJp31h_gy0Iekiq_hr3OxE_QXXZWZrQHw9ZOhK47lmfoH7PGXvaO8J3pu8hpLQUWTHqvyL4pGjhHoXryaIWR9Hojyzfh0wwnJqFDpgG1afJt1VlfYJ_7vUzRU9eJUcEhjjmKukuNEKcrS67Ty2Je4l1TUCYoU4VJf0_YXRTpCW6GfcRsZUd8ZkADrxB8X0KChfJvHwWw3u_a9O0XiiLaGRZdQJM0n2yF_qiW4WGcUo_yOtCJ2hBZfhorvS2bglww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FdUe1ZYumKqjWMscCCfBu5cSC0-1nir5tBz64jx-D3kUojUp2V1NIB16HcxqD5Anji8cMIzFKCa_8rDCj6v0f3SAy6oSrcbdMiULx_WcLE6v3t_0E7tcFo-V_FKpBBcuhAjPF6cqiFSg2W7v4261SxJzw97dYcQKOWQ30EbJ2xISh5ZMSRwO3fjQYEadwsmARUIlyKZxI4p7mzgAVUzdNBiQlne0XxHd4KHF3C-_lje89_CDm-f1Y_9-ef-kfqPwJrGZo1rGjq3Tj1mJOeiCEQkHZPC-OOoVLOjiBY0dBDwWKuZt0k7vpsdTQ9tBD8X9ATTCgKl5d93XUwzSZHEXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dA_5i5e5wWFbu0w_RcYQc20JUcvbr4C3N-h6doSFHq07tRM-9Dpqo7WrJ_01qY6l07tTjUmwcrtDjwmTrMv5py7N1PhLVf5mTYd_y73vbwWLbyq72IIo5qUulfTtCAxQhAdDKImGpfoxAhVGHh7uQzbpEPNgUMzW2pVxz6lm7VRt0sKwfAdPWMAeWHQaIClLs14KAwFXLZ0lQRygOGPSvz2FXdRST4RDxyGqzBJkgS9L27eyy5pQDU0L1f-kDY9vJ1tYfvdLeCpDf5Xds7XA4fHvPWn2rxJjxmOlPjrzuYSyW71bjzA8oQT_XDPrn_u5cpXW91FTbpM_QBm8qWzvww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8AUYG2Y2430a-8PcKFjtyGHTsYRsWMGkwPGv8PzdOzvDSz0e47xTCyWDQNnDqISZXUAetzcBFqpV5OoWGbtOXSSTwmNnAgb6TquSqwA9fb9i1A3SETzGFwp1FDviF6m6X_lEoN3Lnq_7XhNxG_Pz45qfeDURRZLXk2DMl97iQDrKK-W6aJB4Is2Qzul4kDQOIGSa0WGkMriojX2kKLgXnv_8RiPy9pENwvZRmZY2hDG2l7ddlCp_nJWs_DiDYDS_QBS_wSWiQOL7JgyAiJl69jKrTogbiU43UTqi3Y4uB2q770W42ThZvIvUqK2caumj1QyB53-aptRCKIkuY37hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pihTzxM_JkWQfDWxIuL-7hsFYGbbu_CfXPK-5_9TPUj3lCfri-3d7Z2EJ69aYVoHxzZZdw-yFkQqr8w3H-F431JVXs7UmZ-ZqShaTU0sAN-QWB5haMWxGppwQgKJ8GSVVdLFLH7dQXKiyNKd0kc2tkbd-_Eb5hsVszjwO2wh1zj3h7F_50IIDCI6Y5GH7zxJx3ntfx2naS9QZplLRyA-MIIbZpyzmlzdk1V0rUVPSwzroG8Oufx71Dz-xTqOp8YAki0iujzlb1x8GmcTLv6g-6KCAMNICS0IDC_OQc3un_EzwTTrVFTzuoMXKHuvHZB8eVzFa6d4C1OLBFg97cI--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpLs7pM3Qhwtu8Nss0Bl_cOar12avjEkG0Sy6f99eW4MvR8JGxhtewbMcK8qRmMX3kyjHX2QmZIe26wK-QscJoYE13I04VwH7FvEJAj_xWwfOOI2Ve20e39d5vReMcoZn5Cpr-Ly_7ATJW8UFKKHMaZ1lDVXujG8pG9iETW0iQSRjMTCzyhlTrlN1lnPFsM6CIEruf9swTG9o6pM9hR-zrd668aFlx1X7YIqzcRvvJLJ6-mnJxu0gSRjyapt1JRCnmu37Mp93xSRDLZiLO3gI4Q2r69Gg285I_aIpViRvmarGZ4o2I6JfQDpEOhD6Vpbyp3GQpR0ooBokb-YReqJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oBZfhHEP-_nRWnkGHgVeTN01I2htTwrjEa5BywwjNMXb7VkzhNSBTBZoPkwYslNLH15lclQpbbZRZWp36WnX3D5gK49qePQ0gUr77-s1iv9wRoXSI6VTDchDdiGtxAlS_fyux6vcR0syhTTDU8IGxFVApzW-4juwGSNhoRE0Wk-gCA8NA7kRkMTEk6OFkfp3W3sxuzTu2PxFvTM842FrRQruXpPl7xv-dNpx4kqi6fHFY_mS5XCNk3ITPauy2D3Ei6n_Z4fF3OSxOMAc_nGivHYsglQlNJ98EbrpJmlWpNppS2l4VDn0F-BJ6nH5bweBLxLlIBQ4RfCMbbzQMl_ZNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت قدم‌های خیر
💫
✨
هیچ قدم خیری کوچک نیست؛ وقتی مقصدش، گره‌گشایی از زندگی دیگری باشد.
🌱
#هیات_قرار
با همراهی شما مردم عزیز، هر روز با نذر و قربانی و توزیع گوشت قربانی، در مسیر حمایت از خانواده‌های کم‌برخوردار، قدمی برای همراهی بیشتر برمی‌دارد.
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇🏻
@Heyate_ghararr
شما نیز میتوانید در این کار خیر سهیم باشید
👇🏻
5029087002135690</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/685611" target="_blank">📅 20:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685610">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">08 Ane Manaee (1403-09-08) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/685610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه هشتم
حجت‌الاسلام امینی‌خواه:
🔹
از بود و نبود تا باید و نباید: مرز باریک تکوین و تشریع [3:18]
🔹
تشریع، راهنمای کاربری عالَم تکوین [10:18]
🔹
نقشه هستی و راهنمای عمل: خالقِ تکوین همان قانونگذارِ تشریع است [12:33]
🔹
ابلیس را راندند به خاطر تو، اما تو با او هم‌نشین شدی؟! [17:35]
🔹
صدای حق در جدال تاریخ؛ صاحب "سلونی قبل ان تفقدونی" در برابر نادان‌های سقیفه [23:58]
🔹
صف‌های طولانی برای حجاب در هلند؛ صف‌های کوتاه برای فهم در اینجا! [34:52]
🔹
وقتی خداوند آب را مامور می‌کند: داستان مادر حضرت موسی (علیه‌السلام) و گذاشتن ایشان در سبد [48:01]
🔹
کائنات، گوش به فرمانِ بنده‌ خدا [53:51]
🔹
صبر و تقوا در برابر گرفتاری‌ها: وعده پاداش از سوی خداوند [1:08:27]
🔹
حضرت زهرا (سلام‌الله‌علیها)؛ تنها دختر پیامبر (صل‌الله‌علیه‌وآله) و این همه سختی و مصیبت؟! [1:17:06]
🔹
شب اول زندگی مشترک حضرت زهرا و امیرالمؤمنین (علیهماالسلام): بشارت و روضه‌خوانی جبرئیل بر امام حسین (علیه‌السلام) [1:24:00]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/685610" target="_blank">📅 20:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685609">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mifAZ4WhZh_vjgAgu2N29MLs9fCFDmDQRQssDmuC5XdPOvs7wcWkJB8vb7zfxkt3z8YmNAOWDu6PI_NdxddEDcbX1D0xyTjWfyljxAFePGc0FPjKmVyHUsuqYZtA8bZI3YB36nqyMc3Y2J67WjoI4koJPqE_BJUyDoq0QV_2TLsHudDvNpq6t2Hl2q808yLOkhFU8_7gq_0-mTbqDPKO0Tr5BTUrCVXwGvpLs5q-uuuLHLXak7yUcKVlCTZVPIqOZ9iVpOoVG_NdGYpD0Fnuk5XyQ-j8stZCBY2-upA4NMI5LE1_BsSFj01TYz18slSHh6648uBRNqBfcjAAfS_sJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هدف قرار گرفته شدن یک نفتکش در تنگه هرمز
🔹
سازمان عملیات دریایی انگلیس خبر داد که روز گذشته یک نفتکش در فاصله ۱۲  مایل دریایی شمال شهر خصب در کشور عمان مورد اصابت یک پرتابه قرار گرفت.
🔹
این نفتکش هنگام تردد از تنگه هرمز به سوی خلیج فارس مورد هدف پرتابه ناشناس قرار گرفته و دچار آسیب شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/685609" target="_blank">📅 20:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685606">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتصویر بامداد</strong></div>
<div class="tg-text">🔹
تی
زر قسمت دوم مناظره «تصویر بامداد»
📣
خاکسترِ جنگ؛ ریشه‌های داغ جنگ‌های تحمیلی
👇
جنگ‌های تحمیلی علیه ایران از کجا آغاز شدند؟ چه زمینه‌ها و عواملی در شکل‌گیری آن‌ها نقش داشتند و قدرت‌های خارجی چه نقشی در این جنگ‌ها ایفا کردند؟
📽
در قسمت دوم «مناظره» تصویر بامداد،
دکتر ابراهیم متقی
و
دکتر مهدی ذاکریان
درباره ریشه‌های جنگ‌های تحمیلی، سیاست خارجی و نقش بازیگران منطقه‌ای و بین‌المللی گفت‌وگو می‌کنند.
🖼
این اپیزود را کامل ببینید:
📹
یوتیوب
🎧
کست‌باکس
💻
آپارات
☀️
@bamdad_org</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/685606" target="_blank">📅 20:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685604">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWDBB2wQdudcOXyS7n9jHIRMQcwDyH2cmjwjwe-bnzp0oEMarMKtFeONhy5quYnr3cBmqZobcuRPcY-uGNjDpp3AuQ5t6-QkzCF7wr8fh5uNWbiXYlgU7Lq3m3uwNzx6cYJuqg7wzgFYiC5WJGDpVhZAl2MYjhLKI8g82vButcAbsPKNidMFxoGQ8DKfCGIY1-M91JFRVcErQNRs2BSlo9JBc2GJxLpK93iGeMB2IkYRy9UsvL1baMQVUcZsoRsvfUi3VZ3vTRaFjHF_zty0dlGdkOw6RJAyMg8Za8fc7TjB1tjhdYq8CXA8vUPRTrwBsnyL5o3OH7UjqpY_Z1_xxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پولیتیکو: جنگ ایران قدرت آمریکا را کم و پنتاگون را تحت فشار قرار داد
پولیتیکو:
🔹
جنگ ایران توانایی پنتاگون برای نمایش و اعمال قدرت نظامی آمریکا در سایر مناطق جهان را تضعیف کرده است.
🔹
به گفته پنج مقام پیشین وزارت دفاع آمریکا و یک منبع مطلع از برنامه‌ریزی‌های پنتاگون، کاهش چشمگیر حضور نظامی آمریکا در اقیانوس آرام و اروپا همزمان با رویکرد آشتی‌جویانه دونالد ترامپ در قبال رقبای سنتی واشنگتن، از جمله روسیه و کره شمالی، نگرانی‌ها درباره کاهش نفوذ و قدرت بازدارندگی آمریکا در جهان را افزایش داده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/685604" target="_blank">📅 19:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685601">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
مسیرهای مخفی عبور نفت برای دور زدن تنگه هرمز
🔹
برخی‌ها مدعی‌اند که می‌توان تنگه هرمز را دور زد، اما این امر چقدر امکانپذیر است؟ از چه مسیرهایی می‌توان این‌کار را انجام داد؟
🔹
چرا نمی‌توان از تنگه هرمز چشم‌پوشی کرد و قدرتی برای ایران محسوب می‌شود؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/685601" target="_blank">📅 19:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685599">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما، مهم‌ترین عامل کاهش تعداد افراد بیمه‌شده چیست؟</h4>
<ul>
<li>✓ افزایش پیری جمعیت</li>
<li>✓ عدم پوشش بیمه‌ برای مشاغل آنلاین و دورکاری</li>
<li>✓ عدم تمایل نسل جدیدبه بیمه</li>
<li>✓ ناکارمدی بودن بیمه</li>
<li>✓ گسترش مشاغل غیررسمی</li>
<li>✓ عدم ثبت بیمه توسط کارفرمایان</li>
<li>✓ بازنشستگی پیش از موعد</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/685599" target="_blank">📅 19:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685596">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOrNrMpqAdabOckshfmV0u9APtVUu2Q92cd1f7RvSpP4_K3FsCWX6LLcD8Hn4fyyv4-CDg5iRgYnJZU3eH1i3XFLHy7U66_OlTE8MaI558nMlxS_MRGwxG2bHhImifv6QTQJRgSg3IB2RrsOCNxBLHG_rVwefssFR3yWY545_rOf7q4IjZByugmVI24o7eM-bEEUsQ37i4CYjGh2KJdqZQTsldwDBmV4LNBhCbIjiPuFsVB9l2zD7Qg5lhPLVtVQBL3mPGM0gqMtVYP8ORi8KH80b4grd9Svmlx-TMWIWO2WBjytPlqOEzL58-YiDi_FnQfv8Tu4ecjAj2J7BoQI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
🔻
مشاوره رایگان پزشکی برای متقاضیان کاهش وزن با آمپول‌های لاغری
🔹
با توجه به سیر صعودی مصرف خودسرانه آمپول های لاغری و با همکاری شرکت های دانش بنیان دوراپزشکی ، این امکان فراهم شده تا افرادی که قصد استفاده از آمپول های لاغری را دارند به صورت کاملا رایگان و آنلاین توسط پزشک ویزیت شوند.
🔸
کاربران در این سامانه با تکمیل فرم کوتاه ارزیابی، شرایط خود را از نظر BMI، سوابق بیماری و داروهای مصرفی بررسی کرده و سپس با مشاوره رایگان توسط پزشک از شرایط مصرف آمپول های لاغری با خبر می شوند.
👈
شروع ارزیابی
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/685596" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685595">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWBqTBkoKJujfntSjpJriwSkoQAea52w6iCUx4EU5HuXRLpKxx3vlgGaUzM6RtTtOJurLJ_0UCOlXrARYIzoLgc7SDCVrKvVkU4YX4WPBC9ub1LGmLUd9biN2nlA1FY3Bbtj6ZG2h0XBZZrqZ-kZvTTanGaY1dP4jW7T5ZHA0sGSgj0Gbj4Fa9zW5jVGXmh5yxBzU179IbIQaQ29F2AQq7-KvUJg6QwpNrGotVJfR-ANGcrg7dVEaQDC9yfDm1gOeRBVvFo6xZ6Rs49mRNDbwKlPRwualmlj_bWeS9e6n2TbSqZ-vnju07cy3AGC076sCX1bp6myxwppd71PlfKsag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📛
کانون ایران نوین در الکامپ ۲۹ از آینده صنعت بازاریابی و برند ایران رونمایی می‌کند
🔹
کانون ایران نوین در آستانه ۳۶ سالگی و  پس از یک سال و نیم تحقیق، توسعه و آزمون در محیط‌های واقعی از پلتفرمی رونمایی می‌کند که می‌تواند مسیر ورود هوش مصنوعی به صنعت بازاریابی و برند ایران را وارد مرحله ای تازه کند.
🔹
این محصول، حاصل یک سال و نیم توسعه مستمر است و سیستمی هوشمند که تلاش می‌کند دانش، هویت، استانداردها و فرآیندهای اختصاصی هر برند را با ظرفیت‌های هوش مصنوعی پیوند دهد و آن را از یک ابزار عمومی، به بخشی از زیرساخت بازاریابی سازمان تبدیل کند.
🔹
این سیستم پیش از رونمایی عمومی، در بیش از ۲۰ شرکت و هلدینگ و همچنین با ۱۰ برند فعال در بازار امارات مورد استفاده و ارزیابی قرار گرفته است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/685595" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685594">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
۳ میلیون سالمند هیچ پوشش حمایتی ندارند
🔹
آمارهای رسمی نشان می‌دهد از مجموع ۹ میلیون و ۸۸۱ هزار نفر جمعیت سالمندان کشور، نزدیک به ۳ میلیون نفر (معادل ۳۰ درصد) هیچ گونه پوشش بیمه‌ای یا حمایتی ندارند.
🔹
بر اساس داده‌های منتشر شده، سازمان تأمین اجتماعی با ۲ میلیون و ۹۱۵ هزار نفر، صندوق بازنشستگی کشوری با یک میلیون و ۱۸۰ هزار نفر، صندوق بیمه کشاورزان با ۱۹۴ هزار نفر، و سازمان‌های بهزیستی و کمیته امداد با ۲ میلیون و ۶۰۵ هزار نفر، در مجموع ۶۹.۷ درصد از سالمندان را تحت پوشش دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/685594" target="_blank">📅 19:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685591">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
واشنگتن‌پست: فرماندهان نظامی به هگست هشدار دادند که جنگ ایران را طولانی‌تر نکنید
واشنگتن‌پست:
🔹
چندین مقام ارشد نظامی آمریکا به پیت هگست، وزیر دفاع، درباره جنگ ایران هشدار داده‌اند. آنها گفتند که ادامه عملیات گسترده علیه ایران قابل تداوم نیست و خطر تضعیف توانایی ارتش آمریکا برای مقابله با تهدیدها در سایر مناطق، از جمله در داخل خاک آمریکا، را به همراه دارد.
🔹
این موضوع بر اساس اظهارات افرادی است که از یک ارزیابی اخیر تهیه‌شده برای رئیس پنتاگون اطلاع دارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/685591" target="_blank">📅 19:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685589">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU2Q4WzgdmQBRz1Kg0KOcp5GE6wV65ziKTobi8nEmGJhmyQFSJ4dzUz44Jw7QMIpXQ1NbTRBC9MLThpghEuBNUxVvqo80EpvU-v-c_GL9N5_KNDkI2scKpZm9sfUQpOLpaJj_ZK9Eyza9pVghlSURFtNu7D5CYRpyrykQ5xC_KcKvvqSoLu-q8z5cSyD6sfq2xdfl3unWvPkyP0_ISdsiemRrPVG8jyNqmX0FNgQTe0HOnVpJWjM8cl9l1KnJloHxUfEXioEbdhu9awEQD1CHVz5LnT5dnWEXtWJbhVXd-POUAIC5eMyXvLYQX-9rFh-869qkDojplzgZc1wK4Qcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایندیپندنت: همزمان با تلاش ترامپ برای انتقام از ناتو بابت عدم حمایتش از جنگ ایران، آمریکا ممکن است درباره ادعای انگلیس بر جزایر فالکلند «بازنگری» کند
🔹
ترامپ بارها به کی‌یر استارمر توهین کرده و او را به‌دلیل عدم تمایل به پیوستن به جنگ، «بزدل» خوانده است.…</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/685589" target="_blank">📅 18:47 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685588">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAzoh0-2jlwoDemBMs9I6RleqbuXIE8H8yWmGa8KKoC92nrMxV8t9nyL2S-0OT3gge0kop0iwgH559ncTk_wK1l6zHXeaoy3a3D8jHNkBiDnV3xZgoYLmAWqKzD8muoTEdNpBhes1GTlL33QMcGEf7D0dFEfTgiYR1GuWD7caD5jp8ky4FInr7vIVMIjKYvjUUcLERmEkGnoVJ9vZzQ6V4jULPnutOZUTOzCgSjyPlGp7JyOxazr_ujMI5OQ-i_I8ba3hRs6NVq93P08tFhc9INGmx0nPRIln3VU1AXsIEcp7La6SBBI4_ohuXYk5b2YH1JQuqst_1ypRY0HVSecwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیشترین تورم سالانه مربوط به کدام خوراکی ها بوده است؟/ تیتر تجارت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/685588" target="_blank">📅 18:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685587">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
کوچک‌ترها در بورس ترکاندند!
🔹
رالی پساجنگ بورس تهران فقط به کام غول‌های بازار نبوده، سهام کوچک و متوسط حتی از شاخص‌سازها هم جلو زده‌اند.
🔹
از زمان بازگشایی بازار پس از جنگ، شاخص کل ۷۱.۸ درصد رشد کرده، اما شاخص هم‌وزن با بازدهی ۸۸.۷ درصدی حدود ۱۷ واحد درصد پیشتاز بوده است.
🔹
این اختلاف نشان می‌دهد موج صعودی به بخش گسترده‌ای از بازار سرایت کرده و برخلاف رالی‌های متکی بر چند نماد بزرگ، این بار کوچک‌ترها در صف برندگان اصلی بورس ایستاده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/685587" target="_blank">📅 18:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685586">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJBGruagVohRaV0JIdesmOoPo0kxcVmGEL_QwBHyqrB9cGUdaI81IL1Hn7uAiolTSoOL333WMNlQQIduYdseeKSVBbm85rMB2T_-atFCAkRp9fRflG5X-nevzgAjHUsWEHWAlHEDAFrH8mC9n2DdQiUXAvdAhR7miUYByP5mVJ27RFloeslz_IhXcaNVMuXL7yaF3cgBEWTwgd_yfpwDBgfd-3-P-mL2lkLACkk5X_GVYYk0PbGpHEix4pykoHnbESiovMN5F871KKiGBl1Dm9AsVLUBd3I5H9rvuwYg8FQrQImdrDewLM45ps9O9RcuYA0HfdCGlrQYAjUwjXyl3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری این‌بار از نزدیک با شماست
✨
🔹
بیست‌ونهمین نمایشگاه بین‌المللی الکامپ، فرصتی برای دیدار، گفت‌وگو و همراهی با تازه‌ترین جریان‌های فناوری و تجارت الکترونیک.
🔹
در غرفه خبرفوری منتظر حضورتان هستیم...
سالن ۶، غرفه ۳۲
۹ تا ۱۲ شهریور
ساعت ۸ تا ۱۵
نمایشگاه بین‌المللی تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/685586" target="_blank">📅 18:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685582">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اتحادیه مرغداران: تخم‌مرغ الان ۷۰ هزار تومان ارزان‌تر فروخته می‌شود
حمیدرضا کاشانی، رئیس اتحادیه مرغداران میهن در
#گفتگو
با خبرفوری:
🔹
قیمت تمام‌شده پیشنهادی اتحادیه برای تخم‌مرغ ۲۶۸ هزار تومان به ازای هر کیلو درب مرغداری است اما در یک ماه گذشته میانگین قیمت فروش تخم‌مرغ توسط تولیدکنندگان به حدود ۱۹۰ هزار تومان رسیده است.
🔹
تخم‌مرغ اکنون حدود ۷۰ هزار تومان پایین‌تر از قیمت تمام‌شده پیشنهادی تولیدکنندگان در بازار عرضه می‌شود و این موضوع توان اقتصادی مرغداران را کاهش داده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/685582" target="_blank">📅 18:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685581">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">✨
شعری که آقای شهید، دو سال پیش در سالروز میلاد پیامبر اعظم(ص) خواندند...
#رهبر_شهید
میلاد
#پیامبر
@Heyate_gharar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/685581" target="_blank">📅 18:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685580">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290a466da7.mp4?token=R3Xe1zwnttXphEyn1K85bOEzBwPEst_J7OmcFayV1UeSQZUl8vVG4k62xUuTecfyOzhtU8p63hFNBNXuxgDhFly6jlV398pWk23LRc-vJBnoUGFEFuy7VXgLz3CFF8u6-sz49MMBXTeIMGpPlIqo5joBkbIiohesYynfWSdfL2Mw_9l5XJ3k0TC0EbgUZIGYQRxGgbYG7NHEixKDoJfF5hZE84AHBIO98uBNmMwAsUkjAi18JosVpkj0cf2OzAPj420L1RfAfE2ovtA9HpOZdJht1APUynomXVOrEAYmV8PNS0aPVP5STvKT0qUfDTtpEgRZ-xMtvrMJGrefvinKeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290a466da7.mp4?token=R3Xe1zwnttXphEyn1K85bOEzBwPEst_J7OmcFayV1UeSQZUl8vVG4k62xUuTecfyOzhtU8p63hFNBNXuxgDhFly6jlV398pWk23LRc-vJBnoUGFEFuy7VXgLz3CFF8u6-sz49MMBXTeIMGpPlIqo5joBkbIiohesYynfWSdfL2Mw_9l5XJ3k0TC0EbgUZIGYQRxGgbYG7NHEixKDoJfF5hZE84AHBIO98uBNmMwAsUkjAi18JosVpkj0cf2OzAPj420L1RfAfE2ovtA9HpOZdJht1APUynomXVOrEAYmV8PNS0aPVP5STvKT0qUfDTtpEgRZ-xMtvrMJGrefvinKeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میلیتاری تایمز: خسارت سنگین به پایگاه آمریکا در بحرین
🔹
حملات به پایگاه پشتیبانی دریایی آمریکا در بحرین خسارت گسترده‌ای بر جای گذاشته و توان عملیاتی یکی از مهم‌ترین مراکز نظامی آمریکا در منطقه را به‌شدت کاهش داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/685580" target="_blank">📅 17:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685578">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_VDk4u85w0ShmgMpc2QEdkpF1cgEIS4G9BYK-jI87oMeEGcOt8Pbhhz-D9jh8enjFGVq2ix2S-EdeF8XEQgAWNfOh0TTYWn7OOiah_cIFcLiEctEfluyAC1ggAtbGD0MwZ1wvcFDfZ6o0e2zB8C-x0AZtWmudUbp68v_q7VoeWllWA90lqVpEJPe_gNwfhQW4WH0NPavPAasJXlg3zXEX_-8wMP_I1hFFbRb3Au25xoUXCALs3MhlH6stxr5XxfRyicA57nkBJSnJG6UWrkH0rTp6u-y7T47Dwg2tCE3uZBYqkYxVrUsnh9xPrQrBgR70jzn2xfv5NSCzSRmNkZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لری جانسون تحلیلگر آمریکایی: راننده و محافظان شخصی نیکولاس مادورو در ازای پاداش میلیون دلاری با ایالات متحده آمریکا همکاری کردن اما بعد از پایان عملیات دستگیری مادورو، دونالد ترامپ از دادن پاداش نقدی به آنها خودداری کرد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/685578" target="_blank">📅 17:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685576">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
ترمز پول کشیده شد!
🔹
در عملیات بازار باز هفته گذشته، بانک مرکزی از ۴۲۰ همت تقاضای پول بانک‌ها، تنها ۷۰ همت را پاسخ داد.
🔹
در حالی که ۶۰ همت از توافق‌های بازخرید سررسید شده بود، یعنی عملاً ۱۰ همت خالص پول به بازار تزریق شد.
🔹
این موضوع نشان می‌دهد پاسخ بانک مرکزی فقط به حدود یک‌ششم تقاضای بانک‌ها بوده است.
🔹
اثر این سیاست در کاهش سرعت تورم ماهانه دیده می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/685576" target="_blank">📅 17:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685575">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sx6BoBNJt3LfYGGizqPR8Ly9Em_ck-vNpA0mTnxFOtysbEzaOk7S7gGWsq5OYmYxEpKAkujoxQCc3aAwFaJZZcp_Uy680d7UAUMICsRStbXRfaaVYmvVdhshCGKB4HRR9NvbxpUCpvdieEL99jm8riuxxLagayLtxrz9WI4wvGx8XhvAhvuiv4pv7bODC9GSNPLZE60VTEJ8siObO6mopwTZb9WjKCXltVd6tBEy-_MtOsUftmxpwAzoGh_Yo2zcsEt3_Zmsdss1QjqSGiBF6JzVVBZV1WCyk8QsxrkAnJzTbOFzYpP6RlEiak0ZtseGZGV-z65H9yxFVfHHYdqgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#همراه_اول
صدرنشین پوشش روستایی، جاده‌ای و توسعه 5G
🔹
تازه‌ترین گزارش
#رگولاتوری
در بهار ۱۴۰۵ نشان می‌دهد همراه اول در سه شاخص پوشش روستایی، پوشش جاده‌ای و تعداد سایت‌های
#نسل_پنجم
، بالاتر از سایر اپراتورها قرار گرفته است.
🔹
پوشش ۴۴ هزار و ۹۱۸ روستا
🔹
پوشش ۸۲ هزار و ۸۳۰ کیلومتر جاده
🔹
راه‌اندازی یک‌هزار و ۴۳۲ سایت 5G
🔹
براساس این آمار، همراه اول در این سه شاخص جایگاه نخست را در میان اپراتورهای تلفن همراه کشور به خود اختصاص داده است./ سیتنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/685575" target="_blank">📅 17:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685574">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چرا ترامپ از تهدید نظامی ایران عقب‌نشینی کرد؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/akhbarefori/685574" target="_blank">📅 17:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685573">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
لحظه شکار مزدوران سعودی توسط ارتش یمن
🔹
نیروهای مسلح یمن ویدئویی از حملات دقیق پهپادی علیه مزدوران سعودی در مناطق مختلف یمن منتشر کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/685573" target="_blank">📅 17:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685571">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e26c0994.mp4?token=t-D2vN9Tx9Cs0jaAbSAGu0YnkJ7Yk8gnzd72L9FOgRO7bGdh9TxSVNb43TZUIcM8CrIh18GAZSKHSatrT7lZ6LJNSnQdufr73OcgJ2IgbEXkdU-poFFio4bUOP2uni-LFX95fhhaNamrDJo2ZlVqyhUW_5l3YeBXPkYN0R7Q0_c0qs3snIFGX7JhXjsd8XsxVWpAKnLsxQzqAyQ8Ztzpl9w_TAM6zA4iFy9vAHs3GLpKAKgeHl8QS8HQu-rExC9YK9fUf4PXbOCLHZpkP-n9Awc4yhfowfixcd8dOknKJeSoNcnafjRYghOdKRzB9ZdEIGafDT2gaSgAoX82yrL-rIPiUNRB1EcyrHTqGdXhDSxcedMJiDqOoNIWc6caBvzNwsY2Mrf9nkvRF7xf7EemmlqOobGNcExq9E0Pd5l9_duRWV7TJWaAFSpdImcN6B8V7B2Bq2qC8c9qrDN3sISOI-Bfn7b-8Yhw-ZJ033aXkRNDeZvMpaxkcZc6twd4rRQ9zCmSf6UVMhUDiQuP5fsdvVBxcEGCAXhx_P26hs53o8FgHPJkj3FMblf9EEFnEsuGEJ_JrE2UE-Po-3w29GnhXSq7tBoFasSvIKgpPiwnPXYTeE9hbiqcsdHM5PuWZwhmTDUCDEnvXy0baI-Bs7qvS_5LkoUFn_fYPEFAUcAosdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e26c0994.mp4?token=t-D2vN9Tx9Cs0jaAbSAGu0YnkJ7Yk8gnzd72L9FOgRO7bGdh9TxSVNb43TZUIcM8CrIh18GAZSKHSatrT7lZ6LJNSnQdufr73OcgJ2IgbEXkdU-poFFio4bUOP2uni-LFX95fhhaNamrDJo2ZlVqyhUW_5l3YeBXPkYN0R7Q0_c0qs3snIFGX7JhXjsd8XsxVWpAKnLsxQzqAyQ8Ztzpl9w_TAM6zA4iFy9vAHs3GLpKAKgeHl8QS8HQu-rExC9YK9fUf4PXbOCLHZpkP-n9Awc4yhfowfixcd8dOknKJeSoNcnafjRYghOdKRzB9ZdEIGafDT2gaSgAoX82yrL-rIPiUNRB1EcyrHTqGdXhDSxcedMJiDqOoNIWc6caBvzNwsY2Mrf9nkvRF7xf7EemmlqOobGNcExq9E0Pd5l9_duRWV7TJWaAFSpdImcN6B8V7B2Bq2qC8c9qrDN3sISOI-Bfn7b-8Yhw-ZJ033aXkRNDeZvMpaxkcZc6twd4rRQ9zCmSf6UVMhUDiQuP5fsdvVBxcEGCAXhx_P26hs53o8FgHPJkj3FMblf9EEFnEsuGEJ_JrE2UE-Po-3w29GnhXSq7tBoFasSvIKgpPiwnPXYTeE9hbiqcsdHM5PuWZwhmTDUCDEnvXy0baI-Bs7qvS_5LkoUFn_fYPEFAUcAosdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش‌ها به پیام محسن نامجو به همسرش | آیا او به همسرش نگفته بود به ایران می‌رود؟ | نامجو یک هفته پیش از بازگشت ناپدید شده بود!
🔹
بازگشت ناگهانی محسن نامجو، خواننده و آهنگساز سرشناس به ایران پس از نزدیک به دو دهه مهاجرت، به یکی از داغ‌ترین سرخط‌های خبری…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/685571" target="_blank">📅 17:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685570">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nR_byhIsZXRpbJZ1bK6sCZ4rLxXMIQWWHWWkmb_AD4jrsA0x3up-rPFIo6A0qRa0hiLVyAlRae3YxlNYNruebSojszmHlZjMHjk1Rgm0Imyl2tWqOpWH6CDo3f5lGmbGRSm-X41QHgnWGzeQ7F748vOvxR8VJOdrscY0yXOooo-20FNmFTCPpyTnqzu3YJfjxieiXkLM6ra_x3JJfQlqsCtObtfiL6lMiEuIENXPJQkfUM6u1zHEzzXALmF7LR_nHAQgtr7X6bN3VvNiEX12egfHu6KaIjyp0-FIhnHjUR7stgbikZbA5r-osdZhlp5gPkbfUbCgLqgYB6e5LFPCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه CBS: ترامپ با خبر آتش‌بس با ایران، نوسان نفتی می‌گرفته است
🔹
حساب‌های سرمایه‌گذاری ترامپ در سه ماههٔ اول سال، حدود ۳۶۰۰ معاملهٔ سهام یا اوراق بهادار به ارزش کل بین ۲۱۲ تا ۶۹۵ میلیون دلار انجام داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/685570" target="_blank">📅 17:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685569">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUqiJy4FO3JqBop6mnNVeR2of58ZJ9beq3DHVl2SqciK2eSsLcIxUGotvxekqK-DmJtEGWeLI4u81zUG_Q_ojNm3EpeuEvDNfjh4_0BldkXB17QwvPpGKvsKwOgxz74FpNE86lPHcjMejI608HtY-njbvcSQgGeH-dMHpDlC2H71MLYFLIECkDfN3smepMp1RfU0XWaYmZ01HXZ3qboB15UY801DpOlzx_qdCdIAfhNL9ingg2CDaQDfn9RH9ErUZbmBwzNhXdAjh14tVNLoNjNrFRzYkUYO32UhDFRakcbztEO39XXn8KWmqE4cFDTkh4c3SLIOZzaHrZ5cstxPdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاربر اسپانیایی: ترامپ کاملاً دنیا رو بی‌ثبات کرده، دیگه قانون بین‌المللی وجود نداره؛ می‌تونی کلاهبردار مالیاتی، پدوفیل یا جنایتکار جنگی باشی و انتخابات رو ببری، رئیس یه کشور بشی و مثل هیتلر تو زمان خودش برات هورا بکشن. واقعیت وحشتناک جدید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/685569" target="_blank">📅 17:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685568">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEREh-oEH95dh2ccJvZd0wvjXCDgetBZdzskxciRLi1GXTKW9w2e5AEaihg8XUsS3z-fGOgwMRq4GnFA9HK-yUl31Tr4RF2L4zKz7HYslGIV8dhnTtuOtUDwbbhB7OQbXyDTvB0xtsWETXSvHnnKjkJquzHMQ9gbE436-WcmuNTzjdj564EUQE0VkKRN6EBnWWiuOowErQux05XOHrU7BLe70ldNDNQX0DXsGUWm6TYYYWX1a3rUHShcz6t43Tu0ubrHHI609QID1rmqilBknYbit-fE1-pwTfob8hQk-iyNO4ax7wDannylxwr2N3MvWI0btykl6wVMqBQVA2g7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روزنامه‌نگار و مفسر سیاسی کانادایی: دونالد ترامپ فکر می‌کند اگر مدام چیزهای احمقانه در رسانه‌های اجتماعی پست کند، ما فراموش خواهیم کرد که او با جفری اپستین به کودکان تجاوز کرده است
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/685568" target="_blank">📅 16:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685567">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227990e230.mp4?token=k9RFrzOTgLaDsY6hKRPJDIj0D79rZ60ivBPhY-yjVqnE8dMceafsGmWmTWWLBEvjzbfEw4cyjaTr-2OUpAOkd4RKU4uH8_L4gaVOOHoe4ZNtqoMaMNIz1kpD-wgTjH-F7JqbGrmRKN3l_G8ixemw2K08fpVYU3o_xpoFrRwK8MH7p72DQkYtDl7F8MP4ycJecqjfDBFDR99gIA7eG2sU4smfTJW_4QLaPvYhb_9i9R1s3WCLe2-7942a03TXCL9K8_lulqBr_Ol8VUdgtGxkCakN_iYD6lPoAWwd2k_PDILaQXZpNZVvbu1YloNuUzcoNnvKaoR7ctYDK405NA5WXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227990e230.mp4?token=k9RFrzOTgLaDsY6hKRPJDIj0D79rZ60ivBPhY-yjVqnE8dMceafsGmWmTWWLBEvjzbfEw4cyjaTr-2OUpAOkd4RKU4uH8_L4gaVOOHoe4ZNtqoMaMNIz1kpD-wgTjH-F7JqbGrmRKN3l_G8ixemw2K08fpVYU3o_xpoFrRwK8MH7p72DQkYtDl7F8MP4ycJecqjfDBFDR99gIA7eG2sU4smfTJW_4QLaPvYhb_9i9R1s3WCLe2-7942a03TXCL9K8_lulqBr_Ol8VUdgtGxkCakN_iYD6lPoAWwd2k_PDILaQXZpNZVvbu1YloNuUzcoNnvKaoR7ctYDK405NA5WXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تذکر مادر لیلی رشیدی به وضعیت نشستنش
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/685567" target="_blank">📅 16:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685566">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
خبرگزاری فرانسه: سران ایران، چین و روسیه با هم دیدار می‌کنند
خبرگزاری فرانسه:
🔹
پوتین، شی جین‌پینگ و پزشکیان، در یک نشست دو روزه در قرقیزستان با یکدیگر دیدار می‌کنند.
🔹
حدود ۱۲ رئیس دولت به بیشکک، سفر خواهند کرد تا بیست‌وپنجمین سالگرد تأسیس سازمان همکاری شانگهای (SCO) را گرامی بدارند.
🔹
این گروه شامل روسیه، چین، هند، پاکستان، ایران، چهار کشور آسیای مرکزی و بلاروس، متحد مسکو، است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/685566" target="_blank">📅 16:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685565">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd07QA7pTt8rwaU6Xvd73blCEtjEstXDhGHuJH1rZ9EP_LToMMOq-YeNRwiSrA4Xug01gF0i7z8vFoC3o_oR6XVI36L3u1SVqM9VO8Lkj7cg2QjUExS7i6yDmRIGoYBf9lY-YMCL8Hn0PI9fj14H0StDsH_3n7X_MZXPOikLps2Ffz9-f9WZj2FbmCmMddng83tx6ek7nTLnUJq7TS0WX6nDs4hKXos1_LbhFacJHw7ZiasgnUqzK9tuW0XP-nG9a_AjfwcHTiTrKRzHX682jJDjgo1_eHXAj0bHRgsWHD2JxPpXcj6--SJSHHKp_lQSj81yBXiMZ_ISWCYu_12yDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماجرای اتهام جنسی به محسن نامجو چه بود؟ | یک فایل صوتی جنجالی و میراث یک اتهام | شاکیان او چه کسانی بودند؟
🔹
شهریور ۱۳۹۹ و در جریان داغ شدن جنبش آزارهای جنسی عموما از سوی جامعه ایرانی به یکباره نام محسن نامجو مطرح شد. اما این پرونده به کجا رسید؟
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3241480</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/685565" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685562">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8L2md2br1gJcxiwIGDQKIfqdWWru_JwT-gbGkkUk6vNMEN92du-skFWv-FH8ttay4YwMeOM1A9fipkSGZIqEFtcZchd7H9tEwjVtluuG3z3CEnYfXQRQOO6NZPfJ3mjodGaNt2BaNEyR--EOJRwe3LFCs6byaSDAe-b6qoxYK6QDxwJqdxMMwKZLP4M2vgtrewpRcDvrhTqNPBRlp6mQxmnKlGacKdRujz7dHRs3iXzgVQVQ0BEalXGNH8I0V15NN211VgxZyN_vnKDtYFlk8jyHlsK46OVEyx5svCIjEL_1joGZRZhxsI0aE8eUO8mKSu0MzdVRcesi51gJUg-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان زمین‌شناسی آمریکا (USGS) امروز رسماً نام «دریاچه انتاریو» را در تمامی اسناد الکترونیکی این سازمان به «دریاچه آمریکا» تغییر داد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/685562" target="_blank">📅 16:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685557">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
سی‌بی‌اس: در آمریکا علیه ترامپ سند رو شد/ او از جنگ با ایران کاسبی کرد!
سی‌بی اس:
🔹
طبق اسناد افشای مالی، تا سه ماهه دوم سال ۲٠۲۶، حساب‌های سرمایه‌گذاری ترامپ در حالی که او بر جنگ آمریکا با ایران نظارت دارد، به خرید و فروش سهام در شرکت‌های نفت و گاز طبیعی ادامه داده‌اند.
🔹
طبق جدیدترین داده‌های موجود از دفتر اخلاق دولتی، ترامپ سهام نفت و گاز به ارزش صدها هزار دلار خرید و فروش کرده است.
🔹
ترامپ سبد سرمایه‌گذاری گسترده‌ای با دارایی‌هایی در هر ۱۱ بخش دارد و تحقیقات سی‌بی‌اس نیوز نشان داد که در سه ماه اول سال، حساب‌های او حدود ۳۶٠٠ معامله سهام یا اوراق بهادار انجام داده‌اند که ارزش کل آن بین ۲۱۲ میلیون دلار تا ۶۹۵ میلیون دلار بوده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/685557" target="_blank">📅 16:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685556">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751875e9d9.mp4?token=H9FNXICA7T0azqsA_A047Nm-AkRSOiedYBkKMC3ahR0DMKHrT-zjGc2uFzgQcIlXuyVxHnPJmwPET6_lSO7A5VwEqsF2LN7-WlFBWq5ZXDWBfMf7BiVf0ps_RF7MODgJ2t6jBLvK1ahP2m-YR7Lyc5ZWEwqX2yp1rMEiVKDfgai027dXQtTokoa0mjcrVm7KaP-ThzEan43ztsycfEKx8uDYLbBrwGH6sZvRaDKVgjGR7wAl11mW-j6Xp74CXEs805Kf5Z5rHw-vfLMpGjlxJl8obwOfuGnoIe5c9cAxU6ECVtbnu5BXIqwOh2sy1zupcaEChgbg3UoLcT0Vpl1VyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751875e9d9.mp4?token=H9FNXICA7T0azqsA_A047Nm-AkRSOiedYBkKMC3ahR0DMKHrT-zjGc2uFzgQcIlXuyVxHnPJmwPET6_lSO7A5VwEqsF2LN7-WlFBWq5ZXDWBfMf7BiVf0ps_RF7MODgJ2t6jBLvK1ahP2m-YR7Lyc5ZWEwqX2yp1rMEiVKDfgai027dXQtTokoa0mjcrVm7KaP-ThzEan43ztsycfEKx8uDYLbBrwGH6sZvRaDKVgjGR7wAl11mW-j6Xp74CXEs805Kf5Z5rHw-vfLMpGjlxJl8obwOfuGnoIe5c9cAxU6ECVtbnu5BXIqwOh2sy1zupcaEChgbg3UoLcT0Vpl1VyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران، سرزمینِ ماست؛ و ما، مردمِ این آب و خاکیم؛ ریشه‌دوانده در خاکش، با قلبی که برای نامش می‌تپد.
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/685556" target="_blank">📅 15:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685555">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ID0ZTkBbys0rZaPhGYXo8BGy9NcCSLfHosjdK3Vq9QzYzfyLLWXk7cUgK2zqWRZbZ-k2mClRZNZpBTaerjdHZBCgL8hf4Tt_yMnYGO2lM5dqRVsXbRWKfAAjfVmx5iu2ond-sujJ6Qzi4GDrLU3ajzl2Q9QopthBuBGApvPnykLKVFVE-GzfEXwELfssWrG77m32ZBFLHFXNEZxIqmkznzjFs_PYioFxEdWuEDi5h1yrJGEJOF48TRkMeZEuapJGPYh_tILds5kwfoGXCKhIDxQPgECW93KkfI5q5RfBvYhEHlAk5cDJDcj1UiX-X8xfvjcRp72sCdJnvhrAR5-1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستبرد ترامپ به ثروت ملی ونزوئلا؛ غارت ۶۵ میلیارد بشکه نفت
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا، در جدیدترین اقدام خود برای تاراج منابع کشورهای مستقل، مدعی دستیابی به توافقی با ونزوئلا شده است که از آن به عنوان «عظیم‌ترین معامله تاریخ جهان» یاد می‌کند.…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/685555" target="_blank">📅 15:36 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685553">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دستان پنهان در جیب مغازه‌داران؛ افزایش عجیب سرقت مواد غذایی
🔹
برای فروشنده‌ها، نگرانی فقط فروش و تأمین کالا نیست؛ امنیت مغازه هم به یکی از دغدغه‌های جدی تبدیل شده است.
🔹
سرقت، خسارتی است که گاهی جبران آن برای یک کسب‌وکار کوچک آسان نیست. نگرانی هر روزه صاحبان مغازه‌ها می‌گویند حالا علاوه بر گرانی و کاهش قدرت خرید، باید نگران امنیت فروشگاه خود هم باشند.
🔹
دغدغه‌ای که آرامش کسبه را تحت تأثیر قرار داده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/685553" target="_blank">📅 15:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685549">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
یونیوز: ایران در صورت گسترش جنگ، شمال اسرائیل را هدف قرار می‌دهد
یونیوز:
🔹
تهران هشدار داده در صورت گسترش عملیات اسرائیل در لبنان، فرودگاه‌ها و پادگان‌های شمال اسرائیل هدف حملات موشکی قرار خواهند گرفت و حمایت ایران از مقاومت ادامه خواهد داشت./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/685549" target="_blank">📅 15:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685548">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9acccbce2.mp4?token=na5D4k3I-oL-89-5lfevlx0AgyLhQ-2uhEUQkUMKNAFWL_UYIVFIlqcYkhkn9yJ1jFes7puAVyYetaJi7YB3w3o6q0mfDgjLYdt7B8BpXp2ZCLCx_ANN-cMrvXWD3kNF8d-Y2Wmy4si-suXHleAS_JH8-axOAShdWu98cOfwiDV_PSNpE7_CfTC7Wti-TNy71CtSIVBTVaD8tvPkVRFnCzFEWS4Eg5aTIL9mPLicq8Ledv_CI86N-rw2XioiMW93InbHRk0lda7-4NVhBQkEPABrc34-IS9sKabJPvR-oQt-ooxMO40KtTCJHot_l3p1MEoVXXGdr0hVWjQAGmp_pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9acccbce2.mp4?token=na5D4k3I-oL-89-5lfevlx0AgyLhQ-2uhEUQkUMKNAFWL_UYIVFIlqcYkhkn9yJ1jFes7puAVyYetaJi7YB3w3o6q0mfDgjLYdt7B8BpXp2ZCLCx_ANN-cMrvXWD3kNF8d-Y2Wmy4si-suXHleAS_JH8-axOAShdWu98cOfwiDV_PSNpE7_CfTC7Wti-TNy71CtSIVBTVaD8tvPkVRFnCzFEWS4Eg5aTIL9mPLicq8Ledv_CI86N-rw2XioiMW93InbHRk0lda7-4NVhBQkEPABrc34-IS9sKabJPvR-oQt-ooxMO40KtTCJHot_l3p1MEoVXXGdr0hVWjQAGmp_pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کردستان و هورامانات؛ جلوه‌ای بی‌نظیر از طبیعت و تمدن ایران‌زمین
🌱
😍
#اخبار_کردستان
در فضای مجازی
👇
@Akhbarkordestan</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/685548" target="_blank">📅 14:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685547">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_-THgpEoWs1cyQ_vcwOOkIrxgdBePgmO32FJ1DiUzYrCFw0z6HMt1nMgr2tA1LpAUFYzuAl9BaD_uuMYPBHApl0lxf7tVBdDe3GICe9yiC6ABgCHybnmkYp4XbYSlTZQA7fa3x18sVbdyENTuSG-U-EtuT1v_fPNdrQ0fCo3PgMe9tHGEhGwoLPpPXsDTiQ8BisCFe3hzZnlGHoeG_ks9DaWdAPtfHBzA0nNxvxNk9VnIhT92Lavpiu3WTkpLs_45LtAz7kLyeRoEcr6SgQWf2ZicRSu3PCmZOmsNsGw6tZRRDsFu-X_F34Lj-XWndnnkED2Od7wXgN6OG-9nTGCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای ناب ساغر مرادی در مسابقات قهرمانی آزاد زنان جهان
🔹
ساغر مرادی نماینده وزن ۶۷- کیلوگرم کشورمان با یک عملکرد تاریخی پس از پیروزی مقابل رقبایی از روسیه، چین، آمریکا، کرواسی و یونان بدون از دست دادن حتی یک راند در طول مسابقات صاحب نشان زرین طلا شد‌.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/685547" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685546">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
گرانی کالاها دو برابر خدمات؛ شکاف ۷۲ واحدی اقتصاد را تکان داد
🔹
داده‌های بانک مرکزی از تشدید شکاف تورمی میان کالا و خدمات حکایت دارد.
🔹
بر اساس این آمار، تورم نقطه‌به‌نقطه کالا به ۱۲۱.۵ درصد رسیده، در حالی که تورم نقطه‌به‌نقطه خدمات ۴۹.۳ درصد ثبت شده است؛ یعنی فاصله‌ای ۷۲.۲ واحد درصدی میان دو بخش.
🔹
این واگرایی می‌تواند نشانه‌ای از فشار همزمان تورم سمت عرضه و رکود تقاضا باشد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/685546" target="_blank">📅 14:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685545">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjwzQd-Gguj2eMy-916T9Vkri0GI0L0lPUUAO8Z5t--7wcgkKmbxO3aVMWXVBF_LRQt2tJ5id83vN9Daog4j6a90H3PfGgUCi9_OnF6cRYHyKAgMqT9_vK2nPlJwEVT7u5Ag9k0HHzJq6yEuVjOtaELA3yoBbUHbGacWupYRaX5ZFqDeTjNa7v2vLAd2i_zxQKR3V_lcSeCoHBCLiJgV_pjvXeCQQpJLJ2oEt_3PIrd7CvHUajWYn5ZJeFV_ufo8wXadDCTZ7HTwbnn_xD4F5vRsJl-TvRozbsoZmiEBx39nahnpyUJHXdoiSTk3xVf1kUiPgz6w-2IQNboa43hbpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ از کنترل آمریکا بر ۶۵ میلیارد بشکه نفت ونزوئلا خبر داد
🔸
دونالد ترامپ روز جمعه از توافق جدید نفتی ایالات متحده با «دلسی رودریگز»، رئیس‌جمهور موقت ونزوئلا خبر داد.
🔸
او اعلام کرد که بر اساس این توافق، آمریکا کنترل اکثریت ۶۵ میلیارد بشکه از ذخایر نفتی اثبات‌شده این کشور را در اختیار خواهد داشت.
@amarfact</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/685545" target="_blank">📅 14:33 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685544">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad1ca53df6.mp4?token=H1Cvfsc7dGgOdpqYJDf-rDnBDp7RHeny2I0V3_r4e3pL1B-fg3WCvBuLenJ73Rvb63M2256TALw8_3tOC7WFh_e4y-02HQePf7tvtHq9o58q_tCYFw1MX5JYQRCY1e6rANsy7xoEnnTgFoNCnKhTBXQOH0_-KZnf9Q8q1eTVjzOeqvNuFXgKX_OOvNOy3fqa9bLbPoyQjomy8cJ1SzWIX2tjbg1Lm8Bty51s_IxmnNK6T6l2_pNyeLvyPyL6-8rdmvx_yY6v3zYdeIUiwvxmLL984kseNUqy76ioCVB1ByE6ecaaS71Jzu-GmmaD4AL3mWen5CGCqk4NoxW8WBHjyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad1ca53df6.mp4?token=H1Cvfsc7dGgOdpqYJDf-rDnBDp7RHeny2I0V3_r4e3pL1B-fg3WCvBuLenJ73Rvb63M2256TALw8_3tOC7WFh_e4y-02HQePf7tvtHq9o58q_tCYFw1MX5JYQRCY1e6rANsy7xoEnnTgFoNCnKhTBXQOH0_-KZnf9Q8q1eTVjzOeqvNuFXgKX_OOvNOy3fqa9bLbPoyQjomy8cJ1SzWIX2tjbg1Lm8Bty51s_IxmnNK6T6l2_pNyeLvyPyL6-8rdmvx_yY6v3zYdeIUiwvxmLL984kseNUqy76ioCVB1ByE6ecaaS71Jzu-GmmaD4AL3mWen5CGCqk4NoxW8WBHjyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش جالب یک معلم؛ گاو نر تا زمانی که احساس خطر نکند، به جمعیت حمله نمی‌کند
🐂
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/685544" target="_blank">📅 14:28 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685539">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMFtFWA6Mz8CApAkfHjyvh1FfJxmiwRxzmq1BjCN62RljseYUFSVHLljm8WQQDmIe0kOVP4-_mKoxipQXj6FVa2PomJtb66_9OEgu4dPu-GrRuQfzOGYBjBl9p0vmBwLyiwyADcxkuCrei2XQr5Sm9WWJjaMmU83FBwjnM8x5ns-86IUKWEqfXIpH_RdGGeNTP-fPvWziQj1XYGH8BV1SZ3OcYqToWyLb8CbaVA7psJFCPn39L1PAF0sB2ymPRt5R-z-dqNEYrSyHBceB70KG_FPn0l4PofPtfJUolWN6tk0aqD9zEYY72707BrbBIXDj84rWHfc1obo8KcQ8ZYrMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlXdsBQjaA5p0wYIKegGqOc5jyMtRW48c4M-cGoi43Pncf4JiHsn-yfMaGwtiv0JedOdwk0zvru6KNwbn6ko7j8AJJy9IO3F_LqOQrBa_4mtomoRv0xCV8ml-eAFo6Yx6x4J30PA7D9_dL6YvVdv9iLaFxT9LFUirXMR4pG12hGVTPiVIt-fpS0S2cBZ1T8yEBmmfkuU-BqZcOkYOUdoC23qDvG2Bio-nACuHdM1UDwe1FlvQscL_wHWP54Qb0K7AOzEzBSR1KKMwpZO_kPcP-lt-a3Y4UA_DonECea-1bo-doMWFD5fgKYLLQr-ep_IkTWw9Ow1jXOmmir6IooaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QSvp0XAKPpn516U5Q_BxoiRv0Z_docamnroI0mNQLkYB0aHj4Q5tIIXxlBvkLybxXXDSy4DHlII7thGH6rP0N2-ri8nyrpQjs53DA8XDK1mjAKCNniJ4HnJlmGuP1cLrdy5BQSX_4msXmutJ36lcLyNypzaXXWnrY9wMsJUNYjh7uHh0_VDyGyyeGmNyBh7wLRkiAZbIDSbI8uis3bxeqFHyDAvhNQQUrotJ1xirrAGocJSOGTaLVWaWtOR78hcImTsou3xRvDneI_V8v84bCFMjE7EeT0zap3JRpcBsGYQy2iHR7P53xWnIvxSK8Mv0zLWf5W8jMufSFZPKIMRPjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انتشار دستخطی از فیش‌برداری شخصی شهید لاریجانی پیرامون مقام شهادت و شهید
🔹
حدیث اول:
رَسُولِ اَللَّهِ (صَلَّى‌اَللَّهُ‌عَلَيْهِ‌وَ آلِهِ): «مَا مِنْ قَطْرَةٍ أَحَبَّ إِلَى اَللَّهِ مِنْ قَطْرَةِ دَمٍ فِي سَبِيلِ اَللَّهِ.»
پیامبر (صلی‌الله‌علیه‌و‌آله‌وسلم): «هیچ قطره‌ای در مقیاس حقیقت و در نزد خداوند، از قطره خونی که در راه خدا و ریخته شود، بهتر نیست.»
🔹
حدیث دوم:
رَسُولِ اَللَّهِ (صَلَّى‌اَللَّهُ‌عَلَيْهِ‌وَ آلِهِ): «فَوْقَ كُلِّ ذِي بِرٍّ بَرٌّ حَتَّى يُقْتَلَ اَلرَّجُلُ فِي سَبِيلِ اَللَّهِ فَإِذَا قُتِلَ فِي سَبِيلِ اَللَّهِ فَلَيْسَ فَوْقَهُ بِرٌّ.»
رسول خدا (صلی‌الله‌علیه‌وآله‌وسلم): «بالا دست بر نیکوکاری، نیکوکاری دیگر است، تا آنگه که در راه خدا شهید شود، همینکه در راه خدا شهید شد، دیگر بالا دست ندارد.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/akhbarefori/685539" target="_blank">📅 14:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685538">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۳۰ تا ۴۰ درصد بازار کسب‌وکارهای مجازی از دسترس خارج شد
پشوتن پورپزشک، عضو هیئت مدیره اتحادیه کسب‌وکارهای مجازی در
#گفتگو
با خبرفوری:
🔹
برآوردها نشان می‌دهد بازار کسب‌وکارهای مجازی در سال ۱۴۰۴ پیش از قطعی‌های اینترنت حدود ۱۲۰ همت بوده است.
🔹
پس از قطعی‌های چندماهه اینترنت حدود ۳۰ تا ۴۰ درصد از این بازار از دسترس خارج شد و بخش قابل توجهی از کسب‌وکارها آسیب دیدند.
🔹
اگر دسترسی پایدار به پلتفرم‌ها ایجاد شود امکان ترمیم تدریجی این بازار وجود دارد اما رشد واقعی نیازمند ثبات در زیرساخت، اقتصاد و شرایط خرید مردم است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/685538" target="_blank">📅 14:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685537">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d31c32e4.mp4?token=XWlQr4K0KcBTrYQPDpuXUCBCixIz2sDmCmFvQHBdfGJ2bJGugL8Oadpf9BcUQUTRKJLP3tmE1Rajku3hxOdEihsdRtIcr0kQuHjmZs7_UVs1EhkkBZyzLmcV7UxxaN62TtyJOlNT0fPuQFzIyp-6rl3drxOLnTY7tlF5N2CzlNU6SGWoXEH_s4L44beEaNacO73mkngetIsYCrkoxQhDwl0kR3MfaH--C-ng_x5OtvmUgA5gwOMvCXWOVTYeB7Hu1IMoPofVFN4nJK4Zedq6UG48EtNJc5QhC3qQoRWadYRYRGurZxLS9XEvjM8ulwKG3RWjIrboUgcju_qLk3LRTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d31c32e4.mp4?token=XWlQr4K0KcBTrYQPDpuXUCBCixIz2sDmCmFvQHBdfGJ2bJGugL8Oadpf9BcUQUTRKJLP3tmE1Rajku3hxOdEihsdRtIcr0kQuHjmZs7_UVs1EhkkBZyzLmcV7UxxaN62TtyJOlNT0fPuQFzIyp-6rl3drxOLnTY7tlF5N2CzlNU6SGWoXEH_s4L44beEaNacO73mkngetIsYCrkoxQhDwl0kR3MfaH--C-ng_x5OtvmUgA5gwOMvCXWOVTYeB7Hu1IMoPofVFN4nJK4Zedq6UG48EtNJc5QhC3qQoRWadYRYRGurZxLS9XEvjM8ulwKG3RWjIrboUgcju_qLk3LRTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دارکوب خالدار بزرگ؛ استفاده هوشمندانه از درخت برای شکستن فندق
🐦
🌰
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/685537" target="_blank">📅 13:55 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685536">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c275b5876d.mp4?token=lZOuCXSKiCsJs7vmnQ3ClGcwijJ8DI8w-1ewIlEl0gfHO3-Igj4U5N00_giMlLzn-QzqYprUjU2K1mn5_f0hKPX4Hd-GUtvAfud8rvZlJ3mkgcinsLlyHx2yTLCUWEVljVJclaEVkHS9nhQ4zViy2gxqjFHl4jVkWYMFixUuOs1ZH1x8ZS-0Qi1WzfT3D2ySJClj6JCeeS08He38PLa0pncYE-4CjEnynlndiUyi3UBRIPUiV01UKYpZCh3pd3GZXkGnKBnE58gH_0-1QAffL5qmQe0k9eMijVcJnN-XlDOJla4KCITYNBdfeiDxDi3JtMjwgOA258R6frPlWrwLDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c275b5876d.mp4?token=lZOuCXSKiCsJs7vmnQ3ClGcwijJ8DI8w-1ewIlEl0gfHO3-Igj4U5N00_giMlLzn-QzqYprUjU2K1mn5_f0hKPX4Hd-GUtvAfud8rvZlJ3mkgcinsLlyHx2yTLCUWEVljVJclaEVkHS9nhQ4zViy2gxqjFHl4jVkWYMFixUuOs1ZH1x8ZS-0Qi1WzfT3D2ySJClj6JCeeS08He38PLa0pncYE-4CjEnynlndiUyi3UBRIPUiV01UKYpZCh3pd3GZXkGnKBnE58gH_0-1QAffL5qmQe0k9eMijVcJnN-XlDOJla4KCITYNBdfeiDxDi3JtMjwgOA258R6frPlWrwLDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری؛ چرخ زندگی
🔹
از خانه تا بازار؛ نگاهی به داستان‌های موفق کسب‌وکارهای کوچک که با تلاش و خلاقیت رشد کردند.
🔸
داستان موفقیت و تلاش شما در کسب‌وکارتان، انگیزه‌بخش مسیر دیگران است، در یک پیام صوتی ۳۰ ثانیه‌ای از چگونگی شروع کارتان بگویید و همراه با عکسی از محصول یا خدماتتان ارسال کنید. روایت‌های  شما در خبرفوری بازتاب داده می‌شود.
👇
#چرخ_زندگی
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/685536" target="_blank">📅 13:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685535">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فایننشال تایمز: دو بانک تحریمی ایران (صادرات-ملی) همچنان در امارات فعال هستند
.
🔹
یمن: سازمان‌های امدادی تحت فشار عربستان از ورود داروهای مورد نیاز مردم جلوگیری می‌کنند.
🔹
رئیس‌جمهور لبنان بر ادامه پیگیری پرونده ناپدیدشدن امام موسی صدر و کشف حقیقت سرنوشت او تأکید کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/685535" target="_blank">📅 13:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685534">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4592fb4ffd.mp4?token=ToIcHztstL__rOSgzEkif0cVANgQ2xaDZB0rz8Jxhs6aojdpg0V1Xp-8EiDRTe0LQzvF5xciaxY_9fZcQAl3FYSOltiR5RWKOFJgKxPNf9Eh49oOHP8TuUE0dXKfO0s34tm_PEWNDcW3mWwQk6Uw-V_5lM3vkk_8MRMFiMJXPK6vU5vY4qAElJ_kYzpo3IqAqBHeOtmVrJ4yg_A_zdld1NZrtNDNSoh1JlATdm22v9n7lxt-w-lEB_gFe2W1_8Bz7eBA-mxgdhqvtkl_t4ygKqyE_U9bUu13LtuStPDOyvAI5hzugl6Y9uRLT5b9rULMXY4xYqjMczrzHRVjSm1seA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4592fb4ffd.mp4?token=ToIcHztstL__rOSgzEkif0cVANgQ2xaDZB0rz8Jxhs6aojdpg0V1Xp-8EiDRTe0LQzvF5xciaxY_9fZcQAl3FYSOltiR5RWKOFJgKxPNf9Eh49oOHP8TuUE0dXKfO0s34tm_PEWNDcW3mWwQk6Uw-V_5lM3vkk_8MRMFiMJXPK6vU5vY4qAElJ_kYzpo3IqAqBHeOtmVrJ4yg_A_zdld1NZrtNDNSoh1JlATdm22v9n7lxt-w-lEB_gFe2W1_8Bz7eBA-mxgdhqvtkl_t4ygKqyE_U9bUu13LtuStPDOyvAI5hzugl6Y9uRLT5b9rULMXY4xYqjMczrzHRVjSm1seA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
السلام عليك يا سيدي يا رسول الله
🕊️
✨
💚
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/685534" target="_blank">📅 13:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-685533">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
الجزیره: آمریکا فعلاً از تحریم چین بابت خرید نفت ایران اجتناب می‌کند
🔹
به گفته یک مقام سابق امنیت ملی آمریکا، تحریم چین همچنان به‌عنوان گزینه ذخیره ترامپ باقی مانده و واشنگتن امیدوار است مجبور به استفاده از آن نشود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/685533" target="_blank">📅 13:41 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
