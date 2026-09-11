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
<img src="https://cdn1.telesco.pe/file/saKyz1vZE3_BN26axOTIYuC6kgbJog57axlfZSc3lb15_Cp5tkmC6RgJ3D3mbiY9NkZuw3i8CiClAx_N0cuo1cAph8B4ckHQ2_CTi5PBAfCfPWPelMVy_LwUskoMeueRquGesvytGf4OgrTWw-ZE4M4qBd6hZqm2sQfOLiOd3JhrCqMMnO1uFOUuvwRIZFpdXZWp9K3sgc3b1FbhzpKIS33zf_qqZ70aJSj39j7Tfdws71edf3hfjMvE4TRCPvhZ0KBLCrGmuq-Sv-4z8fXRnu7ZvCMVu9u0i3Ni2dj9DifReMeaU19M6Itwx9kt4hVC_mXvnzEMVg5MysjBQ-m0LQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 15:07:06</div>
<hr>

<div class="tg-post" id="msg-5221">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">متأسفانه من توی چنل نمی‌تونم به دلایل واضح چیزی بنویسم. توی این گزارش آنتروپیک، کلمه Iran رو سرچ کنید
https://www.anthropic.com/threat-intelligence-report-september-2026</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/MatinSenPaii/5221" target="_blank">📅 14:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5220">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=oujb5G3MVpSlPhSgewh-y5gTiAYxgTEq4uKhHIcpNh7V2wqHOkDgtvGUZOlMp9xYEhmGdrkD2MQJ3Swivgo7C2Yd4TM0yqPgrtO9zygBfSSm_FV7vi2-fFfdmlYsyTpGl54a8uLQb5VRES_GdE4Zvtxk0bduh28a54NHAIa6FAAAmp8hQXGmoIAyFDH_fNTJqIkDOE5ZooOl0Txy9nezkJEkemNGtS9UzgKvRVIhsnLqI2IpiA-ZqYOfTPtN3XOTDcWksz-5CB7CAUgXJsty-vRUWjIjLuKQOuqfszMfa7hFznJFgzfDY9q-HHw_26yXL0PtbvGe1bmztMgAKhVJDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c2915137b6.mp4?token=oujb5G3MVpSlPhSgewh-y5gTiAYxgTEq4uKhHIcpNh7V2wqHOkDgtvGUZOlMp9xYEhmGdrkD2MQJ3Swivgo7C2Yd4TM0yqPgrtO9zygBfSSm_FV7vi2-fFfdmlYsyTpGl54a8uLQb5VRES_GdE4Zvtxk0bduh28a54NHAIa6FAAAmp8hQXGmoIAyFDH_fNTJqIkDOE5ZooOl0Txy9nezkJEkemNGtS9UzgKvRVIhsnLqI2IpiA-ZqYOfTPtN3XOTDcWksz-5CB7CAUgXJsty-vRUWjIjLuKQOuqfszMfa7hFznJFgzfDY9q-HHw_26yXL0PtbvGe1bmztMgAKhVJDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایونت رونمایی از آیفون 18 توی قم
💀
💀
💀
بدون شرح</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/5220" target="_blank">📅 13:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5219">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-woGUZf8c0vYykYjYrMVSVPzPo0cpUWrrIfKxXCAVTEwxVUaJKhCcWMF174NVcxXIgXODJg0FbMGmdH3-5Zx_8O8U4FKPdShRORQtz4bD9-CHiP1EQjx0NmhRaWv0mz2XePFQPO5hhlk9KuuFq597amWesn3LyggSnh74u2CU03dXCEeakOG3CZ3usxZ3rlyY9_DYLKGaZw1s26o9O1sxn5HDYNZplydVOsXK-d7c4PZjR62lRAy2MOlfs18Chj3xXNkLOAEhZtSdvMqxBl2biZ5n8TfloA3aXEQvF4OVmwRlN2-GfHgd0-UdGVbyv-Kv8-bDo5skOQ2TRIcOThSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌تونید فید خودتون رو هم Tune کنید
که مثلا از فلان موضوع دوست دارم بهم مطلب نشون بدی،
یا از فلان موضوع دوست ندارم بهم چیزی نشون بدی</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/MatinSenPaii/5219" target="_blank">📅 12:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5217">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h4u68F0kNWso6ApHEcHBPxx9uDPrNpek3hmMGhFUUWb3PkAC7eti52ayz2UhwkcLP5Wc0yE5Afx5sG0vxIh7jYdKa0RR5XTZGMZE908i8GSGF7FQuH6Kr1I6rJZoz-BSmGCPej8EkndAm0AgvAdF2g3ULbqsPvUyE2rP5r8ApRNnyoZNqQLZXEvlio43JSLdCpo7pUjz50yz5HTImgWnDJ55D9pgtXSfqm9tRpthqRFDs9Qvnsi-kxP1Dtt8lW2bfk0HQbI_fHgxZKMUptT5GIFTqv8MeNkc7rRAXSuwewzgi1IyAr7Bxv3_0_lSh4jgrVC3lzeOezEiGz19lDW7LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MC8xOqHOSfaGlLKlypNX0YUCpvsG6QabAgiHnZcQA4KnG6KJ1VLzjOuhXjUjXxAAzJmu3Do2eD8Wb6uhqDeX1pCmqjGIWsoiIzoQn1hk4aFakgFYIJHRQz--Wdb5CihbQwTelWIfTsPUma7PRxzMJlPtAfyRvvxw_r1Wj0LGLzOqmKfHZ0aR53A_YNNovnLBtOYzD_HTVvEHiyMZ69nnv85TW0a4H3IOfkdMryxmKjv_GoeHtKx3ROETvZ6SoPvta5v01CkGOAKJXwSxkA5Nbd6GCuEBrC2aYL176k3NNA9Xfx-1EN9hSN2wbOdHDcvQ9cnAh_uQ03x9a6g6R6_GMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من نصبش کردم. باحاله و تمام اپ‌های گوگلم رو کانکت کرد. چند ساعت بعد واسم می‌چینه و بهتون نشون میدم</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/MatinSenPaii/5217" target="_blank">📅 12:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5215">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهوش مصنوعی | محمد زمانی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzm77phY6L3_AKZOLXNRbsT7DhHpKLP0eyfCm9w6V1jTfltsPQMbjFXtbPD8j-bSiRPbF5OYzFrMGN4hykxoYkyKrbk3cxqWz-twajKl0lA6GHspaVGiY6kqY3vekbYFmF07y1eq3IheWNj1ys_olDGRqefJF9GvXgd73gOzwAayUMJM829eNcPRzD1vQ49hdPbbbdvSBbYvRk77rLuqOL_FWdvIBEMsHiH35N-O9b7yop9Xtzk-4mH-0r_N-8C5nT4jCkWgIM9J0cSdsXJRjBWwjW9yXPC6zVlWO5PUKRNouly7Dmnk4DJlk9i29QOnB1Zo4wMhIFRC53bzA0fO3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkP-4-P6thsgdgStcKoPOqWriOHQU7S_Pfa4q30uZw0sQKeb2PQXKV4Mt2gQd_5amRB-sLfydmWur5zMdXWLWLK_fP0W7LOfbI4JjltvzHF_bkguwYt03LXLEa90TkNcNtlHB4rTuEaMFwG93_ItmcPyTcPHAEtjq9OBE2odbELjccjBqPszuWWgD_HRy1vdugbnIVD56BxXpqyS8cv2qrKxGUElSqTQxvXDpHiPqZ5GRZrpUE6MPWXRlWAH1hU-6eqB34ao-SvBuvnrSMdpBP4fJhhDneXYbXFxjiolk_eBRegxPnOXBLJWppYf0-dtBHZttn7rwbKh2p_DYeiENQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل لبز یه اپلیکیشن آزمایشی جدید به اسم Dreambeans ساخته که رویکردش کاملاً برعکس شبکه‌های اجتماعیه؛ یعنی به جای اینکه شما رو بکشونه توی چرخه اسکرولِ بی‌انتها و نویزهای تموم‌نشدنی، هر روز فقط یه مجموعه جمع‌وجور، حدود ۱۰ تا ۱۴ تا استوری یا همون Dreambean تحویلتون می‌ده که کاملاً متناسب با زندگی واقعی و شخصی خودتونه.
منطق اسمش هم جالبه؛ سیستم در طول شب داده‌هاتون رو سبک‌سنگین و اصطلاحاً پردازش و خواب‌دیدن (Dream) می‌کنه و صبح مثل یه فنجون قهوه تازه و غلیظ، خلاصه‌ای از نکات مفیدِ روز رو می‌ذاره جلوتون تا به چیزهایی وصل بشید که واقعاً براتون مهمن.
روش کارش این‌طوریه که با اجازه خودتون، از سیستم هوش مصنوعی گوگل (Personal Intelligence) استفاده می‌کنه تا اطلاعات رو از اپلیکیشن‌های مختلف‌تون بیرون بکشه و ترکیب کنه. می‌تونید اون رو به جیمیل، گوگل کلندر، گوگل فوتوز، یوتیوب، جست‌وجوی گوگل و اخیراً جمینای وصل کنید. برای راه افتادنش کافیه حداقل یکی از این‌ها رو متصل کنید و البته دست خودتونه که دسترسی کدوم‌ها باز باشه. این تنظیمات هم کاملاً مجزاست و تاثیری روی دسترسی‌های Personal Intelligence توی بخش‌های دیگه گوگل مثل خودِ جمینای نمی‌ذاره.
حالا این داستان‌ها دقیقاً چی هستن؟ هر دریم‌بین ترکیبی از ایده‌ها و نکته‌های روزمره‌ست؛ مثل معرفی جاهای دیدنی برای گشت‌وگذار، یادآوری قرارهای تقویم، پیشنهاد رستوران‌ها و تفریحاتی که ممکنه از دست بدید، یا ایده‌هایی متناسب با سرگرمی‌هاتون.
بخش جالب‌تر اینجاست که اگه دسترسی گوگل فوتوز رو باز کرده باشید، تصاویر این استوری‌ها با مدل هوش مصنوعی Nano Banana 2 شبیه نقاشی و اسکچ تولید می‌شن و جوری طراحی می‌شن که انگار خودتون و اطرافیانتون وسط اون ماجرا حضور دارید.
فضای این اپلیکیشن فقط تماشا کردن نیست؛ اگه روی هر داستان ضربه بزنید وارد جزییاتش می‌شید و می‌تونید اطلاعات وب، نقشه و راهنماهاش رو ببینید. امکان بوک‌مارک، اشتراک‌گذاری و بازخورد دادن هم هست؛ مثلاً می‌تونید بگید از این موضوع کمتر نشون بده یا «درباره این بیشتر بگو» تا سلیقه‌تون دستش بیاد.
در حال حاضر استفاده ازش کاملاً رایگانه و دیگه نیازی به اشتراک Google AI Ultra نداره، ولی فعلاً فقط برای کاربرهای بالای ۱۸ سال در آمریکا و روی دو سیستم‌عامل اندروید و iOS فعاله.
در واقع Dreambeans مثل نسخه جمع‌وجور، داستانی و تصویری از Google Now قدیم یا Google Discover جدیده؛ با این تفاوت که به جای پرتاب کردن خبرهای عمومی به سمت کاربر، مستقیماً از دلِ اتفاقات زندگی خودتون الهام می‌گیره تا هم به کارتون بیاد، هم به جای اعتیادآور بودن الهام‌بخش باشه.
▶️
Dreambeans
✈️
@mohammad_zammani
📱
Mohammad.zammani.offical</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/MatinSenPaii/5215" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5214">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/5214" target="_blank">📅 12:26 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5213">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BPGPrRbEv0uAdiWgUodCDgEcU6-JaZVtm4TzIvMqxjk_BXX2NRmo5jTsHUM6RGnU9tT67tGOJv1-ceDbECvc9TtZgnnNU76I0YoLViti-WTlAmZgui0hNocJ65QkhYpgYvyRishvqmP2qKNDA_8hE3aEHdFfaV1J5Pr5Nfh5HsX6fw923F4q_XhQpNs-MC6um0JlHGKDoMoHmoV1xbPfhp7cTHWrs1DldIYud0pJHB5agnkQyWFKj-Ro3jwOsUPh6jdm8RIO8ZQZKA0H5YqAs43AVkX6mQB1nmlXeldb_xeBeFXc8K97zLFspkyQOG8oHqVUhaFWm9H3ojvU0lywtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوپن دیزاین یه بنچمارک از Deepseek V4.1 Flash منتشر کرده که اگر نزدیک به واقعیت هم باشه فکر کنم آمریکا به زودی چین رو بمبارون کنه
😂</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5213" target="_blank">📅 09:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5212">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">توی این چهار روز کلی اتفاق افتاد. از معرفی GPT image 2.5 تا مدلهای جدید دیگه‌ای که معرفی شدن؛
اما چیزی که وقتی دیدمش برق از سرم پروند، حل معمای 90 ساله‌ی وجود و همواری سه‌بعدی ناویر استوکس توسط یه مدل قوی‌تر از Astra توی 88 ساعت بود که هنوز در حیرتم؛ چون خودم رشته‌ی تحصیلی دانشگاهیم علوم دریاییه.
ببینید معادلات واقعی ocean circulation معمولا ناویر استوکس خالصی که الان حل شده نیستن.
یعنی تفاوتی توی اصل حل معادلات شبیه‌سازی جریان پیش نمیاد.
حل این معادله بیشتر شبیه اینه که بعد از 90 سال، بالاخره قفل یه در رو باز کردیم و پشتش یه راهروی تازه‌ی پر از مسئله‌ی جدید پیدا کردیم و رفتیم لول بعد.
فردا راجبش بیشتر می‌نویسم.
خارق‌العادست</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5212" target="_blank">📅 03:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5211">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوستان من حالم خوبه
میام به زودی</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5211" target="_blank">📅 11:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5210">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/MatinSenPaii/5210" target="_blank">📅 00:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5209">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">توی تک کرانچ
یه مقاله نوشتن
راجب «
مشکل منوهای بی‌مزه‌ی ساخته‌شده با هوش مصنوعی
»
خیلی از رستوران‌ها با هوش مصنوعی عکس و توضیح منو می‌سازن ولی نتیجه‌ی همه‌شون شبیه هم از آب در میاد و مشتری هم سریع حس می‌کنه یه چیزی سر جاش نیست. مشکل همون یکسان شدن خروجی مدل‌ها هستش که تفاوت واقعی رو از بین می‌بره.
به نظر میرسه بالاخره داریم به اون نقطه‌ای میرسیم که خروجی‌های ai با یه ورودی عادی، یه‌شکل شده و کارفرماها برای نوآوریِ بیشتر پول میدن.
وقتشه دست به کار بشیم و از مخمون کار بکشیم
🙂‍↕️
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/MatinSenPaii/5209" target="_blank">📅 23:40 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5208">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvxfo-qyA_QwXinBZmPSM17EzpBCGvscZTFN7k7SPQE0IawvrTL7K_oJRaUJL03lng8FB6OfFjtwbGZSrH51SwDu24lTdTUoPWb3xLMqpebELHrjYe6I903Z1IR6AgB5cVb-bkrCPqDLL8ikC6oT7DzNaIOWx_Eh3VFTUuEmoE7Y_88googsZnrZxhYCNvqId0kheHFlrvzI7VMwtvaC2AztBLO-fNtmEUAZeHSXLs0u1bO0rHv1E_mMbKaNqTqajdxCk_36Ov9WCWQHlQu_48_MUajBOLJW2Dq5hFfb8hc1W5HlxqpXQk2XnwRLqoG7RImcTCUFqaa2OryhJJ8ftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواب من به هرکسی که فنی نیست و سختشه که پنل بسازه توی کلودفلر و... :
Defyx
👍
https://play.google.com/store/apps/details?id=de.unboundtech.defyxvpn
البته WhiteVPN هم از لحاظ راحتی و امکانات برابری می‌کنه و می‌تونید ساب خودتونو هم وارد کنید اما برای کسایی که یه کوچولو فنی‌تر باشن مثل جمعی که اینجا هستیم خوبه.
دیفیکس در حد سایفون راحته، با این فرق که واقعا وصل میشه
😂</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/MatinSenPaii/5208" target="_blank">📅 22:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5207">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گویا گوگل Mantis رو اوپن‌سورس کرده
فریم‌ورک ایجنتی مانتیس این شکلیه که کل چرخه‌ی آسیب‌پذیری رو خودکار می‌کنه. از پیدا کردن و تأیید، تا بازتولید و فیکس. فرقش با اسکنرهای معمولی اینه که با ایجنت‌های منتقد و بازبین و... و اجرای سندباکسی، گزارش‌های الکی و باگ‌های توهمی رو فیلتر می‌کنه و مصرف توکن رو هم تا ۸۵٪ پایین میاره. پیشنهاد می‌کنم بک‌اندکارا و امنیت‌کارا یه نگاهی بهش داشته باشن:
https://cloud.google.com/blog/products/identity-security/getting-started-with-the-mantis-harness-to-find-and-fix-bugs
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/5207" target="_blank">📅 21:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5206">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">چند تا کوهنورد تو آمریکا با جمنای برنامه چیدن و جمینای بهشون گفته خیلی کمتر آب و غذا ببرن. و به خاطر این مشورت اشتباه با جمنای گیر افتادن و آخرش گروه نجات مجبور شده بره دنبالشون. عاقبت سپردن عقل سلیم دست AI
خلاصه برای جونتون هیچ‌وقت فقط به چت‌بات اعتماد نکنید
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/MatinSenPaii/5206" target="_blank">📅 10:05 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5205">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JhQ0wcZO6Cb9g05iZxaAWv9OFObhrdrSHAG-eelh0beVP-gT0lvZwoDD9afejrlDbg2aSthFR7Kq6p8_m60oav6DO1cCfxtrfc1tk_Ut5yWikmKgJt7sQFfYHtaDoa3q29Nh0F-bAT2wd8LuhAFGpG3gTL3G37q9H4oZl3cmS9OJ4ac6UQowkLuIcO1PQy2AAPpMy0qdDWVwJBqK4pj6uaf6ZE5Yn5RmxYM1kYy35rFmy2KUHddqSZ0NsTIOjBWCjCDBhSyEriJWblDJmigrPF6dt4WyacItz6PkBSI0i3UcY6XFNdysMDlKEnaiBzLQneIuG-9OspybUZl9NOQ6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست
Pelican comparison
روی مدل‌های GPT به علاوه‌ی هزینه‌شون.
هزینه‌ی Astra تقریبا پنجاه برابر Lunaست</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/MatinSenPaii/5205" target="_blank">📅 00:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5204">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=hdCddTM03QT7bzaDqZzZQ9gtyg1jAtJbmnCSZv_blFrV_Ok8JaSQ7_76QGxTgvUCIwFobOQrwZyGeSF0wrl_rtWbaCUra7ko08kd9EyLR7HwNCxIAqZ5dPk3p7rVy3U9PGnMZtJUIytF5CfSxW0fR2OSZVVfBHLqwSVkS1oDhfQ8LQqt9Frll-rgtLRWKkGK0pTgy8BMHZEfUJLN14KGATvitz9NLZK9GFnDYtX98s8XN9Vl10afQZkxCTU6CsYeWO1tm1p59-BpBLjYAfgF6Fnce854q29rPtPz-i21DEK00nZm3B2EwDFPL4uBnwnIeDe6HJgeODsCaqNQ4ronUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48fb2366c8.mp4?token=hdCddTM03QT7bzaDqZzZQ9gtyg1jAtJbmnCSZv_blFrV_Ok8JaSQ7_76QGxTgvUCIwFobOQrwZyGeSF0wrl_rtWbaCUra7ko08kd9EyLR7HwNCxIAqZ5dPk3p7rVy3U9PGnMZtJUIytF5CfSxW0fR2OSZVVfBHLqwSVkS1oDhfQ8LQqt9Frll-rgtLRWKkGK0pTgy8BMHZEfUJLN14KGATvitz9NLZK9GFnDYtX98s8XN9Vl10afQZkxCTU6CsYeWO1tm1p59-BpBLjYAfgF6Fnce854q29rPtPz-i21DEK00nZm3B2EwDFPL4uBnwnIeDe6HJgeODsCaqNQ4ronUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نیرو : خبر خوش برای ملت شریف ایران، قطعی های برق برنامه ریزی شده برق تموم شد.</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/MatinSenPaii/5204" target="_blank">📅 21:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5203">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ELEPJBsu4F1rnNRMMdqSt9ZOVDxuyUjxsB2vNl3OSOUDlcd6aAcA-D_Q6c3Iw28ZGu-B_MWbcl5E5XB6gVZMNvjOYXbZm2iyN8tMKD238G44OdDftF_qERRgr-wl5hypF00cXd74l7F54wkZNIzOWM69Up_1Gfbl1pZOXkw8pV1UqAX110GZUx2LL0DXA0JNt5Vggs5dvpTYRtrG3_wipbs3rhp_TaiV6NnU2ijD8WPUIvJEAiy80JUvefs2WkdWAYu5UKnPlNuH6beWkd_Lj98VT4IxOp51xpP9yACwF0DhpJLdhnW5Yn5-o-ohiKllFRkweT8nRmAeK764FBkeEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اونجایی که کلاد و جی‌پی‌تی مدل جدید دادن... به زودی باید شاهد دستاوردهای برادران چینی باشیم</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/MatinSenPaii/5203" target="_blank">📅 20:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5202">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون  من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید. یکی از دوستانم دو ماهه و خودم هم…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5202" target="_blank">📅 19:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5201">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/geWkfgZ412ycg93H8xz12G2maPtXZU2JN10XVMD7xVKFj9VcVIfnQeHxKHO5a7gXs8tMi4Zg-vFbmqts2iWMd_tMwXh8KClgr7uyr9dY5iSk4c0-L5r0V96QWb4JCZBZryjtT5k5Aou-AwsCKTybHSHQgTWeB7U6OJasto21aiiXAbvUs8cm95JRTO5XJ1Vawzx1v8zcgsSImQBH0y6aj-B8sRys2zN9G3caj4gAi1OfGBgVLgomXXqwQPwK0flS7yDbAxLaJGcl-ABPCZWuLq5gQJ_ug-oA3gQ1F8VYHArzbu663zYipin4vgaIoi5YtyFKBP1ayc6dNvfr1RHgZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش خرید اشتراک Claude Pro با ویزاکارت شخصی و ایمیل خودتون
من امروز تجربه‌ام رو از خرید اشتراک کلاد پرو می‌خوام باهاتون در میون بذارم، که چطوری خیلی راحت و بدون نگرانی بتونید با پرداخت کریپتو روی ایمیل خودتون فعالش کنید.
یکی از دوستانم دو ماهه و خودم هم از دیشب خریدم اشتراک Claude رو و مشکلی نداشتیم. صرفا باید ریز به ریز کارهایی که می‌گم رو انجام بدید
قیمت اشتراکش روی لایسنس مارکت الان 5.700 هست ولی این شکلی اگر بخرید با تتر 228 تومنی در میاد 4.800 که خب یه تومن به نفعمونه حدودا.
حتی اگر بعدا به مشکل خورد یک وقتی(که فعلا با این روش نخورده)، مبلغ رو برمی‌گردونن به حساب Mpay که ساختیم و مثل سایت‌های ایرانی نمیگن برو بیست روز دیگه بیا
آموزش:
1- اول از همه، شما باید یه ویزاکارت مجازی داشته باشید. آموزش متنی ساخت ویزاکارت:
https://t.me/MatinSenPaii/4915
آموزش ویدئوییش:
https://t.me/MatinSenPaii/5091
2- حتما باید حسابتون رو توی Google Pay اد کنید با این روش که دو دقیقه وقت می‌بره نهایتا:
https://t.me/MatinSenPaii/5092
3- توی گوگل پلی گوشی اندرویدتون، با همون ایمیلی که کارت رو روش ثبت کردید وارد بشید و بالا سمت راست روی پروفایلتون بزنید.
توی قسمت Payments & Subscriptions که وارد بشید، باید بتونید اطلاعات کارتتون رو ببینید.
4- اپ اندروید Claude رو از گوگل پلی دانلود کنید، وارد حسابتون بشید، توی تنظیمات روی Upgrade بزنید، پلن مورد نظرتون رو انتخاب کنید و خودش هدایتتون می‌کنه به پرداخت با گوگل پلی.
و به راحتی پلن واسه‌تون فعال می‌شه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/MatinSenPaii/5201" target="_blank">📅 19:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5200">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKlwVxN3cpkqXZifisaASBPB-huI_QR1cOaf8YVa9oAop8rDeEbQmQtGRZ7-YGxmlDsFJtfUhAQTdeL2MVMRpxIgDSJ3ttlGDNG_DbeuzvqfhfCwbvIC4B21uhH8v-W1rCm7P99CCb-F7C9LF5O_gVmM3hgTIgPGiIgrYAcosHt9ycMxL-bHYLUrhBiG7yXMjIfL1ev0XasV3gENfREKo_4mIG-SDOw5ubgueQTcSHU5I1FYjl-nTUp-GxINVN3jlukq31-4SLAt9Ud4EzRNR54RE_pgruEWmgVKQPjxoFDdxHWUF9YDNtsVRlR2_x4Fac-LGIC05pHlWIrpw5uTOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📇
یکی از ابزارهایی که باید توی هر پروژه‌ای استفاده بشه، Codebase Memory هست.
https://deusdata.github.io/codebase-memory-mcp/
🟢
کاری که می‌کنه در ظاهر ساده‌ست: کل Codebase شما رو index می‌کنه و از ارتباط بین بخش‌های مختلف کد یک Knowledge Graph می‌سازه؛ از function و class و interface گرفته تا call chainها، dependencyها، routeها و حتی جریان داده بین functionها.
نتیجه اینه که Agent برای جواب دادن به سؤال‌هایی مثل:
«این function کجاها استفاده شده؟»
«اگه اینو تغییر بدم چه چیزهایی ممکنه بشکنه؟»
«این request از کجا وارد سیستم می‌شه و تا کجا می‌ره؟»
دیگه مجبور نیست هی grep بزنه، فایل باز کنه، دوباره سرچ کنه و نصف context window رو صرف پیدا کردن کدی کنه که اصلاً دنبالشه.
به‌جاش از طریق MCP مستقیماً روی گراف Codebase query می‌زنه.
✍️
تفاوتش هم فقط تئوری نیست.
توی مقاله‌ای که روی ۳۱ پروژه‌ی واقعی تستش کرده، Codebase Memory با حدود ۱۰ برابر توکن کمتر و ۲.۱ برابر tool call کمتر به 83٪ کیفیت پاسخ رسیده؛ در مقایسه با 92٪ برای Agentی که کدها رو به روش معمول file-by-file می‌خونه.
↗️
خود پروژه هم برای ۵ تا structural query مشخص benchmark گرفته: حدود ۳,۴۰۰ توکن با graph در مقابل ۴۱۲,۰۰۰ توکن با روش file-by-file. یعنی توی اون تست خاص چیزی حدود 120x مصرف توکن کمتر.
🔭
ایجنت از اول یک دید ساختاری نسبت به پروژه داره. می‌تونه call chain رو دنبال کنه، impact یک تغییر رو پیدا کنه، dead code رو تشخیص بده، architecture پروژه رو دربیاره و حتی ارتباط بین چند service رو دنبال کنه.
امکان Semantic Search هم داره؛ یعنی لازم نیست حتماً اسم دقیق function رو بدونید. مثلاً دنبال مفهوم send بگردید، می‌تونه چیزهایی مثل publish یا dispatch رو هم پیدا کنه.
ضمن اینکه همه‌ی indexing و queryها لوکال انجام می‌شن و کدتون برای ساخت این graph جایی آپلود نمی‌شه.
خلاصه اینکه به‌جای اینکه Agent هر بار پروژه رو از صفر «کشف» کنه، یک نقشه‌ی قابل سرچ از Codebase جلوش می‌ذارید.
مخصوصاً روی پروژه‌های بزرگ، تفاوتش خیلی محسوس‌تر می‌شه.
و بالاخره کمتر شاهد Agentی هستیم که برای پیدا کردن یک function شروع می‌کنه با grep و find و jq کل repository رو شخم زدن
🤢</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5200" target="_blank">📅 18:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5199">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تهران
💵
228,‌000</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/5199" target="_blank">📅 16:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5198">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">البته اگر می‌خواید برنامه‌نویس بشید توی ایران اول از همه بهتون تبریک میگم که با دلار ۲۲۵ هزار تومنی و بدبختی اینترنت و نامعلوم بودن آیندمون و جنگ و اقتصاد و فلاکت و بدبختی تصمیم گرفتید توی این حوزه قدم بذارید و شجاعت به خرج بدید</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/MatinSenPaii/5198" target="_blank">📅 16:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5197">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!  همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.  اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:  قرار نیست با اومدن AI، هنر برنامه‌نویسی،…</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/MatinSenPaii/5197" target="_blank">📅 15:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5196">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOnFpavr96Q6ooxC6Rj9pYSzBGS3hp9IxDsWo5kJm9zv1ZorL8PJyGQ3XzKayQIrSQomSzh_TJrC24TlkWiRtM3QDjflCb0luZrsFQo87wWmQzxZAk4JkeSkEpbdsAnHmpPtZzr6EhxPjDETdXpAyTS-bbj2IzWH7zfApodOcIOWKplCxF1yOT7TSivrVKday7GPDQRiXoc2_k0WLeKXW4xzoD9KzSFcWLdXABqfbp_uPuuyaQjKB1gz5pRCkD4_QX5fam0XIYT68noOsw99TWHVel-sGzee86D6rY0YheWoy6QxCM3ljjHIEXLgjarOeC5Sa_ba_w5gk8fvsZ7LUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5196" target="_blank">📅 15:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5194">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این 25 دلار توی حسابتون می‌مونه دوستان. یه سریا فکر کردن 25 دلار از سر راه آوردیم بدیم دست هتزنر
شما اگر که استفاده‌ت میشه طبیعتا پولش رو میدی. مثلا من عموما قدیم از هتزنر برای استقرار ربات‌های تلگرامم استفاده می‌کردم
هزینه‌اش نسبت به سایت‌های دیگه خیلی اوکی تره طبیعتا نسبت به منابعی که میده.</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5194" target="_blank">📅 03:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5193">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FJbt7_Ibt4R0kn9w_AJpmt68s4bfSBqUpOmsNivpqM0wswdGCDbA_HcDK9MbI8ehd85MYND1_2srmeR9dt20e7iZAIAeZa5jZ-CIJViQsC2yLNXkad92CSfrv0RKt0LIwMElV2se4JiK3zF8oHK3QkZ4HZlzHnOenouBCtJQdRefPDEmyXnnZF1WMAQZy6YXqpdcm7CqYb8BnsC617QV7LPcfUOxllbdrCu5KwyPxELCafiZE25dkn_XXL_OPNbmTa2io0oWnB6TvqtheZHtDLB_4npM3UL8P_bqiAqMqko0fXnzBc5_BLzO3iBlupnuQaLwovuhv_4f37GCAEGGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیمیتم رو پنج روز پیش تموم کردم. از کجا می‌فهمیدم می‌خوای مدل جدید بدی خب
🫪
(مدل Astra الان برای کاربرای پلاس بیست دلاری هم در دسترسه)</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5193" target="_blank">📅 03:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5192">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nkgDXzv5-bQL_MA_kjFC8tqRWKylvw4_pKC1OlKPONxwSB9qjkKCvmvQ790ArB3QKW6ch7n9SUFbf2d9Ww3WiyLVrWhzKismOZQ5nLF-5KjIeUv_G6LNYcikzymhu05MmkO7N3Kw_B2t3hTZ9v8-3_uDqDqAtTkn-MxNd3-82-YID6DvcilfXIZSy9QMPnNyfy1bDAeqs8etvfkP0IFEzrsCaPMcFoKicFeOaHucgJ_x0APesiGGbI51t0dUCyQp8v4YODBIHhpn1ZDZKtSZgVCh2I-095WDCSV-tfIXJstGN-dOjuGK976WIL863b8sYsbr8NYTe0TfQi60SVVe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5192" target="_blank">📅 01:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5191">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NlQFH881MEIcOSS7syBu9rB2OcyQte0j3BsKgdu_00eK6UOvEZ_J_n74VQ6DIJFqhh7vkMXn4uP4oea9GzUyEraqb12fDpFZyans-0vpppO61aPcCvSWUxJfuVRmOHIo_obZtwBmBwN_AjFkVR2wrQQu4LArE0vdfw4kqiOuFsPwDKA8KqauLvRARo8zrgrWe5rGlvX5f2Ws3fOuqpNRq1Xtvl1dXQfPtQx1mnKi8qigfrvt0P2jurHX_IJuyEUQ15T0gXK7ykNkgiy9NHDGqwbeaacAGQE_gnNlEKu63pyIJgBV1WiYXcDBc8_4mOcywGEvhBsPSnoBAw9TogYCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت Nara خودش از اوپن کد api میگرفته
😂
😂
😂
😂
عاقبت وایب کد کردن سایت Api هوش مصنوعی</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5191" target="_blank">📅 01:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5190">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">چقدر غمناک..</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5190" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5189">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Kavinsky – Nightcall</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5189" target="_blank">📅 23:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5188">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Nightcall</div>
  <div class="tg-doc-extra">Kavinsky</div>
</div>
<a href="https://t.me/MatinSenPaii/5188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این موزیک برای من، خاطره‌انگیزه. من رو یاد برهه‌ای از زندگیم میندازه که برای مهاجرت به ژاپن هدف داشتم، مانگای yofukashi no uta رو می‌خوندم و شبایی که 5 سال پیش توی ناامیدی و شرایط سخت، برای یوتوبم تلاش می‌کردم
کاوینسکی خدا بیامرز، توی این موزیک یه شخصیت خیالی ساخته: راننده‌ای که سال ۱۹۸۶ با فراری تصادف می‌کنه، می‌میره و به شکل زامبی برمی‌گرده.
یه جاده‌ی خلوت و تاریک، فقط نور بنفش و صورتی چراغ‌های نئون که از پشت شیشه‌ی فراری تستاروسا رد می‌شن. رادیو یه آهنگ قدیمی پخش می‌کنه، دستاش رو فرمونه، فکرش جای دیگه‌ست — پیش دختری که عاشقشه و همون شب قراره ببینتش. بعد، یهو همه‌چی به‌هم می‌ریزه: صدای جیغ لاستیک، نور چراغ‌های مقابل، فلز که مچاله می‌شه، و بعد… سکوت. سکوتی سنگین که انگار قراره آخر ماجرا باشه.
اما نیست.
قلبش دیگه نمی‌زنه، ولی چشماش... باز می‌شن. بدنش سرده، دستاش بی‌حس‌ان، ولی یه چیزی هنوز توی وجودش زنده‌ست — همون حسی که قبل از تصادف داشت: باید بره پیشش. باید بهش بگه.
همون شب، با همون لباس، با همون بوی بنزین‌سوخته و شیشه‌ی شکسته که روی شونه‌هاش نشسته، راه می‌افته سمت خونه‌ای که صدبار توی  خیابونش قدم زده بود باهاش. جاده‌ها خالی‌ان، فقط صدای پاش روی آسفالت میاد و صدای دوردست یه Synthesiser که انگار از یه دنیای دیگه پخش می‌شه.
می‌رسه دم در. مکث می‌کنه. دستش رو بالا می‌بره تا در بزنه، اما یه لحظه مکث می‌کنه — چون می‌دونه از این به بعد دیگه هیچی مثل قبل نمی‌شه.
در باز می‌شه. اول یه لحظه شادی توی چشماش می‌بینه، شناخت، همون نگاهی که دلش براش تنگ شده بود. اما بعد، نگاهش عوض می‌شه. یه چیزی توی چهره‌ش، توی رنگ پوستش، توی سردی دستاش، بهش می‌گه من دیگه همون آدم قبلی نیستم.
می‌خواد براش توضیح بده. می‌خواد بگه که هنوز همونیه که بود، فقط… عوض شده. که باید حرف بزنن، که هنوز وقت هست. اما پشت سر دختر، از توی خونه، یه زندگی تازه دیده می‌شه — نوری که مال یه شب دیگه‌ست، عکس‌های جدید روی دیوار، ردی از یه زندگی که بدون اون ساخته شده.
سال‌ها گذشته؛ و اون خبر نداشته.
دختر نگاهش می‌کنه، با بغض، با ترحم، با یه چیزی شبیه احساسی که هنوز کامل نمرده ولی دیگه راهی براش نمونده. و آروم، بدون داد و فریاد، در رو می‌بنده.
اون می‌مونه توی تاریکی، زیر نور کم‌جون چراغ خیابون، با این حقیقت که تصادف فقط بدنش رو نگرفته — بلکه اون زندگی، اون عشق، اون آدمی که بود رو هم برای همیشه ازش گرفته. برمی‌گرده سمت فراری، سوار می‌شه، و توی جاده‌ای که هیچ‌وقت به مقصدی نمی‌رسه گم می‌شه؛ بین چراغ‌های نئون و صدای سینت‌ویو، بین یادِ ۱۹۸۶ و واقعیتِ الآن.
Take care of yourselves
❤️</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5188" target="_blank">📅 23:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5185">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W-3No7AV9EKIwb6l0ruSEEpJuRuZhYNLi0caNhnTRnE_StehSHQw2pKpI-z9_ufZDjl0_MyQbnk8pmQ5N-YTm-ddFA79aVVh5WHK8WO2foGwgIXDjk7wzAevGT1GmxmwuYcguKZGzAGRqKrSAO2Bkm-IVt-1jglxTeTbMBPATR0n8gypcofqCaS-yXSPUYqzh8xMfQL8IBTbJ9nkYM6iT_pyq-GgWQS5t4hHcr9fudT-UtjAnl5qK-PTc8fM4mFRfJHNYtQrHF7M5cPGFkMr6qdCnTXOPCxl5RwimCnqCJl67K5OqmMk5BnsgEDZn4X-gynn7x1g-nygy_2dDz_oww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XEdCiKMma_AaOn_mO1s6xCB9YOdcWwrbLmtQNj291-KhjzUG9fPA6WbLctTlZ4e3z4ftByYBvpwC-ajsNObcgboBIm0SHpxUFKEY9CMqFatLUZMQc2D74_fPtrBLMaCJv2LFlEsWLGGZNmyxJhQlHDl7vFjpiacIPTejyr2MMDiRVV2AfhgHqGbceJzGC2W-yIneMle9eiU1bE-1j-uc_3qyjdqvZJ6CNsc4N__0k5EeWQMOOnyPpej-B7UstZTUN-yH0RVtMLGyIzQWxWtHVJ7QDfOBKa2j9i5KgPOAJvHnUXYEfuEXuGSpCjJepIL7YSt2haFxLV0BGXpJJny5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/j4T4xJ9F0tkZjAEPFcB4YnWPtxXqPBsPgqQgxPhHk0kl7LvXE3thPxcaArxMVFoIJPvdHIv3MHzNIxf_NxNlcdKHw4SUZTCCogSv4CO7sQS0IOvLugs-YvidHZqON4cx1R2Eaq979p8bpPbNzos5VzyUdTXY2xkUuOKG-E4EItwGsVwsQmeNiv789_2jwr_oMkkhFZthFheHralQqrARef9hC5TiQXTm-H0jsSounEOUj8yCYBydw6P7iXXkGp-7HIrYoXWoABKoTmqpy5KX-BsnTtA1U0hdj9uaej_YQ3kHa4WNQrry4RuOgVzno0z6TpBsIm0MccE5kJ6_PSL0nA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش احراز هویت در دیتاسنتر هتزنر و خرید VPS ارزان‌قیمت
وبسایت هتزنر رو احتمالا اکثرا کسایی که توی کار فروش VPN هستن میشناسن، یه سایت هست که به خاطر سرورهای ارزون قیمت(2 هسته CPU و 4 گیگ رم، 6 دلار) و قدرتمندش معروفه. که توی لوکیشن‌های آمریکا، آلمان، سنگاپور و فنلاند سرور میفروشه. اما علاوه بر سرور، شما می‌تونید از Object Storage و خدمات دیگه‌اش هم استفاده کنید.
ببینید تا الان، مشکل احراز هویت وجود داشت برای ایرانی‌ها چون مدارک هویتی و... می‌خواست تا آخرین باری که یادمه، اما دیشب که رفتم ثبت نام کنم، دیدم یه راه احراز هویت دیگه هم آورده: احراز هویت با کارت بانکی و پرداخت 25 دلاری
پرداختش هم به این شکله که شما هرچقدر بخواید استفاده میکنید(مثلا 200 دلار) و نیازی نیست حسابتون رو شارژ کنید، و آخر ماه باید فاکتور 200 دلاری پرداخت کنید.
سرورها هم هزینه‌اش ساعتی محاسبه میشه و حدودا ساعتی 0.001 دلار پایه برای پلن 6 دلاری که خیلی به صرفه‌ست. و هروقت نخواستید میتونید Terminate کنید و سرور جدید بگیرید.
1- اول از همه، شما نیاز به یه ویزاکارت مجازی دارید که حداقل 25 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- تشریف ببرید و توی
https://console.hetzner.com
ثبت نام کنید
3- اونجا از شما یه سری اطلاعات اگر خواست، اطلاعات فیک وارد کنید اما حتما با اسمی که روی کارت Mpay نوشتید ثبت نام کنید و خودم این کار رو با آدرس فیک آمریکا انجام دادم
4- به شما دو راه احراز هویت پیشنهاد میده. احراز با مدارک شناسایی، یا احراز با پرداخت. که شما احراز با پرداخت رو انتخاب می‌کنید و حداقل مبلغ(25 دلار) رو پرداخت می‌کنید و به راحتی حساب برای شما ساخته میشه.
دقت کنید که این متد همیشه ریسک خودش رو داره، اما دیشب که توی ردیت چرخیدم دیدم که 99 درصد مشکلی براشون پیش نیومده اما در هر حال، ریسک احتمالی اینکه ازتون مدارک هویتی بخواد بعدا رو توی ذهنتون داشته باشید. قوانین سایت‌ها هم ممکنه تغییر کنه اما فعلا مشکلی نداشتم سر این قضیه خودم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5185" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5184">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EMVm_CoNXDnQjMIQwYUA0DCO7yn9LXEEXobGQBWIP1FzDXhLlpJzcwSNugVdGx-rwtF3dRJCce5lWO06TF3jOZqVF06utzXmyLlOU3Sv2IWt50HILdotUxqYGFtU6bMj-G9dHJKbf4jCYTEUyuUrjsiX-HzRGZz9VgyBy0dXRC7WzUkEdrnTlCO7rpnc5dTIegaCwcDMUHyIgQem04In1DUrrI_ueUuRBTtwABPApuSB1JKfypsA66skrbEKi3S4Y6Lz5OBzSIYZzt_0XQx_PGCq2ft_LhJeVCWgQQXnQhVhWBfURTKvoVUG9WTkClDNjvPB0s_5Ewb4UvvGi0Zu6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت و مشخصات؟</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5184" target="_blank">📅 21:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5183">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه چیز بهتر از OVH پیدا کردم:) بذارید تست کنم ببینم اگه بن نکرد من رو، فردا معرفیش میکنم</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5183" target="_blank">📅 20:58 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5179">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=ViLc4MyTbJxlT3UTpgXoSqNujKL25SZ5gA8IulHfvW9KxdT3sSbG9Sdc7ErtR2MBFvIZdeHMDdUBwWHQckXxBfNAwP5G3P-YmeciD6Dd8J-0AnFZeKxdUYnVTZT18U5trt0xfcbjU2pGsBmyHqCkG_clus4WRdwmokPhigJi1UqPMr1xw8WI1VFowTNfQCRIS5W7PirfOPteiXcS-WlgZmwBzWJDq87og0Kw3ej5rr7eY6rt4zlBIDDLUURQOIv1_To618yDqIkSFrggpyf3yydFbcHWWT66v9-2knQmSw3minNyl6ybuwZBJIpAJdQDqXM0S2LgmFl8l21ase7e-w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c84957dbe3.mp4?token=ViLc4MyTbJxlT3UTpgXoSqNujKL25SZ5gA8IulHfvW9KxdT3sSbG9Sdc7ErtR2MBFvIZdeHMDdUBwWHQckXxBfNAwP5G3P-YmeciD6Dd8J-0AnFZeKxdUYnVTZT18U5trt0xfcbjU2pGsBmyHqCkG_clus4WRdwmokPhigJi1UqPMr1xw8WI1VFowTNfQCRIS5W7PirfOPteiXcS-WlgZmwBzWJDq87og0Kw3ej5rr7eY6rt4zlBIDDLUURQOIv1_To618yDqIkSFrggpyf3yydFbcHWWT66v9-2knQmSw3minNyl6ybuwZBJIpAJdQDqXM0S2LgmFl8l21ase7e-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل
GPT
-6 Astra بالاخره اومد
💻
بعد از چند هفته شایعه‌های مختلف، OpenAI دیشب مدل جدیدش رو با اسم Astra رونمایی کرد. گرگ براکمن رسماً گفته «فکر می‌کنم رسیدیم به AGI» که خب فکر کنم بیشتر منظورش AGI ِتنظیم بازار بوده
😂
1- چی فرق کرده؟ برخلاف نسل‌های قبل که بیشتر یه چت‌بات باهوش بودن، تمرکز اصلی Astra روی کار کردن مستقیم با کامپیوترته: پر کردن فرم، کار با اکسل، رزرو نوبت، جست‌وجوی شغل، حتی دموی ساخت یه صحنه توی Blender و بردنش به Unreal Engine. توی بنچمارک OSWorld 2.0 حدود ۷۲.۶٪ گرفته (Sol حدود ۶۵.۷٪ بود) و کارها رو تقریباً با نصف زمان قبل انجام می‌ده(حالا اینکه هزینه‌اش 2-3 برابر شده رو کاری نداریم مثلا)
😑
2- کجاها واقعاً می‌درخشه؟ توی کدنویسی و کارهای عاملی طولانی، ریاضی و علم (توی FrontierMath Tier 4 حدود ۹۸٪!) و امنیت سایبری که توی ExploitBench صد از صد شده. برای همین OpenAI قابلیت‌های تهاجمیش مثل ساخت اکسپلویت رو برای کاربر عادی قفل کرده و فقط توی برنامه‌ی Daybreak بازه(فکر کنم همین بود که رفته بود Hugging face رو هک کرده بود)
3- داستان اون ۹۹.۹٪ چیه؟ OpenAI گفته Astra توی ARC-AGI-3 نمره‌ی ۹۹.۹٪ گرفته که واقعاً وحشتناکه. ولی وقتی خود سازمان ARC Prize با harness استاندارد خودش و API خام تستش کرد، نمره افتاد روی ۶۲.۷٪. اون ۹۹.۹٪ فقط با یه harness اختصاصی خود OpenAI به دست اومده که حافظه‌ی استدلال مدل رو بین مرحله‌ها نگه می‌داره، و هزینه‌ی تستش هم حدود ۱۹ هزار دلار(4 میلیارد تومن) بوده. پس این عدد رو نمیشه مستقیم با بقیه‌ی مدل‌ها مقایسه کرد.
4- توی مقایسه با Claude چطوره؟ این‌جا قضیه واقعی‌تر می‌شه. توی بنچمارک‌های خود OpenAI (کار با کامپیوتر، ریاضی سخت و...) Astra جلوتره. ولی توی Artificial Analysis Intelligence Index که میانگین چندتا بنچمارک مستقله، Astra نمره‌ی ۶۱ گرفته؛ دقیقاً هم‌سطح Sol
😂
😂
، و پشت Claude Fable 5.1 که ۶۶ گرفته. توی Coding Agent Index هم ۶۷ در برابر ۷۰ برای Fable 5.1. یعنی توی خیلی از تسک‌های واقعی استدلال و کدنویسی، فعلاً کلاد جلوتره؛ عوضش Astra توکن کمتری مصرف می‌کنه و برای خیلی کارها ارزون‌تر تموم می‌شه. (حالا اینکه Input Cache اش چهار برابر Fable هزینش هست رو کاری نداریم)
5- قیمت و مشخصات؟ هر میلیون توکن ورودی ۱۰ دلار، خروجی ۵۰ دلار، کش ورودی هم 1 دلار و کش Writing هم 12.5 دلار؛ تقریباً هم‌قیمت Fable 5.1(به جز Cache که فیبل 0.25 دلاره) ولی ۲.۵ برابر گرون‌تر از Sol. پنجره‌ی زمینه حدود ۱.۰۵ میلیون توکن، خروجی حداکثر ۱۲۸ هزار، دانشش تا ۳۰ آوریل ۲۰۲۶ آپدیته. توی ChatGPT هم گفته می‌شه سهمیه‌ی پیام Astra روی پلن‌های پولی کمتر از Sol هست طبیعتا(بله AGI تنظیم بازار)
6- دسترسی؟ فعلاً فقط سازمان‌های محدود (برنامه‌ی Daybreak) بهش دسترسی دارن(مثلا ادای Mythos رو در میارن). توی روزهای آینده میاد روی ChatGPT Plus و Pro و Business و Enterprise، از طریق API با شناسه‌ی gpt-6-astra، و روی Azure و Bedrock هم در دسترس قرار میگیره که برای ما ایرانیا زیاد اهمیتی نداره. ما اونقدری پول نداریم که پول api بدیم خوشبختانه
حرف آخر: روی هوش عمومی و استدلال سخت هنوز از Fable 5.1 عقبه. گویا توی طراحی Front و سه بعدی خیلی بهتر عمل کرده اما خب، متأسفانه اون هم نمیشه اعتماد کرد. سر Kimi3 و Fable 5 هم همچین مقایسه‌هایی میکردن تهش گندش از آب در اومد که اینا پول گرفته بودن الکی قدرت Kimi رو خوب نشون بدن و خلاصه تا خودتون تست نکردید، یا عمومی نشده 7 سپتامبر، اعتماد نکنید.
منم هیتر GPT نیستم؛ صرفا واقع‌بینانه مقایسه میکنم. وگرنه همین الان اشتراک GPT رو دارم خودم و میدونم اگر روی هارنس درستی باشه، توانا هست اما خب، چه فایده وقتی Ox Alpha انقدر قوی‌تر بود ازش:) متأسفانه
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5179" target="_blank">📅 20:43 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5178">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">بچه‌ها من یه ده روز نیستم کلا و مسافرتم
بعدش قول میدم حتما استریم راجب دانشگاه و انتخاب رشته داشته باشیم و ادامه‌ی استریم‌های Rust
تا اون موقع مخصوصا بچه‌های کنکوری سعی کنید تحقیق کنید کامل. از بچه‌هایی که مسیری که شما می‌خواید برید رو قبلا رفتن، سؤال بپرسید.
دانشگاه دولتی رو بررسی کنید
دانشگاه آزاد
حتی پیام نور
ببینید هدفتون چیه؟
شاید دانشگاه نرفتن هم یه گزینه باشه
این وسط برای پسرا سربازی هست
و خیلی مسائل دیگه مثل خود کار پیدا کردن و ...</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5178" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5176">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/duiIuX0C28COqQLY9Fm1d0N88tMpx8jizgTk2TUjNujwg5ePcUerLoXLCnrBXqNPI5GhsRD6LrYWYkN4T64oVuNYAkXojxbIoFfa-EjDHVWgzjE6i3fbw4ld5_QAAy9hXVX5UMr9bu9PebEXUP1gSS3H96-p2JDstaFy6rHaEZziKqNfMMethEOAINJI_Nzn9GYDmlQqFfz8Eooi2iQWZ5Pby_de_JzF7tG_EwNWExFB8bLXIztyiXUx1UQKtaoQdJ5S7c8li9mTZQsxj_7fr9gSA1FL9i8iBY9XKodVt82iAkQKxerKUKifiF5G0cDffDXgb9G7dN880GhfSdCK8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام شما هم شده پر این تبلیغات کریپتویی و ترید یهو؟
حس میکنم سیستم نمایش تبلیغات تلگرام عوض شده چون 24/7 هر کانالی باز میکنم تبلیغ روشه. قبلا این شکلی نبود
الان حتی روی این کانال کوچولوی من
@MatinsDungeon
هم داره نشون میده</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5176" target="_blank">📅 14:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5175">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوستم دیشب بهم پیام داد و گفت متین، gpt 6 اومده
گفتم بذار بخوابیم فردا بنچمارکاش در بیاد
و الان باید بگم Wow!!</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5175" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5174">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">متاسفانه نشد
😫
فعلا بریم کردیت رایگان گوگل و آمازون رو استفاده کنیم ببینم چه میشه هرچند هنوز می‌تونید از سایت‌هایی مثل Aeza و Yottasrc و... خرید کنیدا صرفا OVH رو دوست داشتم بگیرم که نشد باز، اگر موفق شدم بهتون خبر میدم</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5174" target="_blank">📅 01:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5173">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8Semu4m3013oAU4QNhfLjZJZMrLJoJknR2DEzxe27EW4unwLgsFMEc-42R2DBJNnWdrPfjikjUzuS9F4vE4BchVtxLcIgr35Oj5FXhrWcQcDn2EUFv2nDujMtK1-mF9D0FkZbJFaFzVSw5kTadgV9EKJpPD26T8eBnJeEZwIH-y7h-9sW7AAsAzAQFJ00GK8NY7RijqpYI62Pok-L0KT7RwYb9Bi7Sgx2d8weu75FbSC6QvuWQDSXDxBlyohZNLVeRSZa--i2x1AWN9EGMTDMLwflIIQw3YBmcLvCyY49cGqMFX47Vw21L5FOHirkiY_ZNhhh3nBGQ0bgs7fuZgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5173" target="_blank">📅 00:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5172">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CjJM_MkwRyfqhe3SJojkQOR2gzDIeCFQYvst3KG-Jz6YufatlmXzD4joRiMKiVJTTPY0XyEi27-FxmMAiumkjh5F-JxKirxzsEy0ZLzWInciggNTm30oFj51kq-umnCo0gjirsHEkDjzUgPPf8Y2aY_C5s4Vjtkmk3d3J1geRV5b-YoeHuiZwIEZtipao2Yo348EnHIB7okTBzFM0kaigMJkUAqkaaWdVfNOD16XQZqdMImKGDLknLFzPX65PKuMqQHpXIM-tnWabKRAHLG7tWJ13Q-QZ0Y4Y5arfT9i65vLcnd3hqrc_QNWAL6pJ9OpGb5UOmweoYgjmVivLZNt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده. 2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://  سایتش گویا یه مقداری روی آیپی حساسه…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/MatinSenPaii/5172" target="_blank">📅 23:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5171">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wp29WnQXczCF-ZXekuBTWkLRWeoZUXq8hs73z-ZoBiTs2PtGSr3A9d_qFt7QnkdS9Oim4hQWetGo9iCdvWpcJ3ht_3rIbHINZ-yO9gF3lzO45w_BrYyTf1J00AOmDWnKjpBxgThRMjakAJUJCYQKXRZrx2MWDnSCp3N27CAG0kw8BfcFaaFPW0MAVHobbIU7ocgWpAhOKkjJ43eky9vdbMKQRt-rBidSS3wGOkXhYmm1IMEI_AtkHDz_OdXthKiq9DSqyruMQ3xyyInS4Nd0Ac95obPaqEt8hZSd3j7JP7F3T2oYsCiFQhD8SP303W-1kbDzqucOyoDDbHvt9gOSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرورهای OVH واقعا به صرفه‌ان از لحاظ قیمتی و اینکه ترافیکش نامحدوده.
2 هسته CPU و 4 گیگ رم، 4.5 دلار. با دلار 220 تومنی میشه 990 هزار تومن
اونوقت سایت‌های هم‌ وطنم پاره تنم دارن سرور 1 هسته و 1 گیگ رم میدن +1 میلیون تومن://
سایتش گویا یه مقداری روی آیپی حساسه
من میرم تلاش کنم ببینم میتونم ازش خرید کنم با Mpay یا نه</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5171" target="_blank">📅 23:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ud1xtEjddE375snOcVq7sA4yFty0mVndm-Y5AyhBtpvEgRZeGkAkk4-0DJMnOQE_AiVbUUxARHcHDvH7Y3o3Gt8kWtn1BWYb0QMtIJRibgT6QJaRnGrdH3CipQUuAk_kH2yoFjkOg9xS6gAGg6ye19UofBKVHQCevQNhlTW_4aYXbzH6NKhCYKDUEe5LVqwNrWluxA1ETvDOyKUdDLdmrKTbVtvqF7BULLSjm6aQuEiHwQ5__rJjUMml2PawuPyJDnXjRJe4pMQX-vurMo8kED5i6EL_4ujYFNFTGOc3tu3W5Bc95fPPkoH_AwT7kP67L8K9X3NfSoq4RA7FcvomLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LXJQr18vwa8AapSoky3AEuxluIR2PmsZAy-0DRGGmqLO82Kv0vmOmFfnEWxteLemPeB2vM58eYNcLhUyCcdoFNLs1rIEC5wyLa3GHKCHuei-WP9IipAy2WfICmgYoUxAyjTQKsYSs-b1RXEV7nA8BM1YbA9igzbE0TgYNzfDK2ePc9v3CWNrFs4A4A7vFZ0RytIyZsk2JO_yr5G1AlnnxsWBACkS8OzoMYWd1SqrahIyLiUS92jNEQOuHIRzoBxCR9vK8w5wrLTQUevRlQ8iuiDvTuCIkIDxC2aTsTt0PoJpysKZZ-1hCV94q_4Mnnc4c-GeXc1Sy8aZB2-iew4Hrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S4Dc-oLcIYT3w9PBn6gwMIZDu9I6BRFmC8oZXhbnAJv50l1zFqWYWJwQWcR9tWlNQtbIdyNfpr1txZ3I2ZI1jpoPp-9zz7lhuyxFlyzsBokdHhvywFQ35nOs-qiQoWCyz2SPQLmHluz15Pr1YS0uD2_06zgWBKnUtYqqbTMJFuC92Z2dZVeDXIVBGf2WHcdQ2RfOVKqzhBVKZ6kxS3QneEJqnu4rnp9yw9W_TKt4aHcFnjShWl00Zk_swTA7iaUwFi7ty_kHv1muFi9KUJZ8VKiy175DEjaMVnkwTSDaDPZt6AaMACaIbkTzFDJ8pWX2wrHYYQe9QumPH4U7ZvgGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/O0Ao6eW12mx-BwhBeKvM9Ql3YqeI6msdn1SwA58P0TjfmtJol38OKct_y_g9BiLLiOlEbbJ3oSPbq7du1_DTAOo-0orODf-6gJrOPrkxxTIDgdGdS20JPNK2tMuaWwvmlQVb_lmAkrZBI2KzO-6CFdTElvWsfOwoWBfNRbXRp1tIgLdwFRfOFSfoysQy900n7LfG-1Ic2Iv3VbxZZEdGJtn-7GBuARc9-HUZvuUhQ8rlxb0zgYnf22c-VyzLOV6F96Yr4_C0fTPFkH_6LD8XlEg6gIUnh3fH-ZWFbyILLvyOG1SAOquh-J1uuB1d8MjircsKbPBGiEFIe6e6pIQ9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kr9gtr4vkUf28PLrJj_7gsGQ9hUG6KvPS7s1CsHSnVt6lvweiFsSQm17Rqs21FvNh5a_ldiCQJVtWADIW_gOJK8ydudWwTOVWSjSgCswpwBfXOnigVvuf_1GO42m-xqBgq8xrK_jWmlBpB81hWwyXjUVCJWJTWqHurioDgRxXrOUEYRdmhcltaCDGIyBHckc8GC2Jt4Tz7nrD3O9ttpcM-DJBoIo9H9V6IxoXn0LjCCdcMi0mk7Og-9-MZipnfH0znFf-OFNo0kuZAGTYLJDv8lczQqdEyl_OUWDgq0HbqLR3WG1ar0wp3D-k2XrV8UrYXLx8h9LnZU-47p191St9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iV7LZ2mWS7NRTfYcOSOdgmtAKD43-DI3GOabd5LMKl9o6-1TOApf9VLXxwQ2mp7bPabZLdBJbcBUc8LMmh5zMHVtyHSYizgcg1ZAUMn9CaVxljhmh6T-NY-6UdfdzNU7xsDXTh3zi0WkMOikI5cGHfw5FxW9-SI4N_ni-hk7iul5YeM3q7wU-kNYqXNev6jfu_xz2ZhY9CBd3lHmkl8qlG2Ynlw3dgmsJK85DROkQAAt8JyIrjzLmnIBAUHzxkKFpTy73gYmTPbSfeE1lurOVJBXUo4yxpkCoR7RtpELluS-UmR_9dpUKG5lPGHM3Kdt48vCMleW5Ov3paGlfkCZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vEGheRspz45vmT8sBTbV242QDJCQTd1W_HWOKNoK9szu-PxsUmBIv0toF9oOkoqBAgVv8doSSfnKpfKGOXmkZ2mdZPMJggi7DZ61M0n7TGYK42Hw3lU0xsR4MB4pBou4XHynQrgHbRTar4uwDW5_q-x-Ya85MlJsT0CFw9uYB6UpUghUZpSMNzMyP0VmSwtg6tH8KUK-wBWbK46UdQe9hmg-9VlZAE3qaZpe4siMBoQHZGIQ-WACyTE4_6OLFtjonlH9D5hF95HJgfQlNdTrgROj7Q3v-KAnrS7hk1IrSvx8IONFAqzKxQ6oqb3X7SkF9Rd2_V1_4Una3jSiyOcNyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uAiKFOq-pH9XldcqqSotzwoNHgCw4sOc_Oqw3lxiWPjGHH4wL7u_zYPT4xhDA1v8izNN4pn1q9luJBJmLh19rgYbxdXmO5cUPvdg0pyNhZdulYVwIouDgb_-IfwPZ5r8f8aU6hKqoTNV2M8cgbiib5vOBxEnnRRTTrdtom6HMxTb2_uFrLrb1MqKYIZVNwTYk-ApOJnBigX7qDtV6L3qvnTMMMUX8s_FXbIu4WjkJFHbOSLLrNDrDBhYwcKgBBSJFqBxgSUlr28gPio4I8UclE_5-FmHIGoHWyKlAPNa5LjUwnGOBrkvIr1QM4fWsZy9EzG2qvi6h8Exy-QrTwT5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mq0EpbbszBVfOMH2mLWKdF45N2MG1DFBKa_sEvu2b9eiXGoO6wnM0Oohy7c-PDCROsTxyHgOpQOMeLnf0Xbs2eHa_dEcBQwhWEnQfKPSpm9OmKQh36h-NpJ3Fm6w0e7VbyumjoA0_5MgLYVZ3EBjSCz8RQLueg0mD2LKV9njfXlD4XjvOxBiKmJSd-SmD4l9eiXeRe3rxZci7o9a9HWaTSZFy7nGoZPlEtK0qA-6uwlhWlbD7R4t5UbGz3MCWvICPQVIt9qB4Y1qh58mhnZ9SMNZTyMGxas0iBIvmMATRHAr3sYiI53d7GlPCe3o26lbYBNUbOu2qNHl-G9hBVJwLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/daOBpkvkWkkI-4EblFWFssfod0BSHBrehsiTLDYCVn9qXWLiLE8vQYu9xFn7jIBd3EvLMP6oZFa2N-98Qs__ErxZ4BDAYG5mpmszNF0GTp2edZLs3tNypuNRsyvfu6Sdj7KCBD4eyqAerXfmOO9y_BURWkGaoSZVQNK6FrAtr-k-0VMhubWr9rRrke-EV8Pjzpc3_eju-zStRGVKmKIWMnDzcHpd5NPwQJqsnRAqzJ8PH_t-pZmk-tJeywmHRftHmNSX6XSYEQIQyh6aTexdRyPJ2M6enmJAI25owUwPpL__HJ-NWpPFjtcI_hVcvaIHDd20BAbEuIuHsSsVlhYYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JOl7kK4-YRy_Ju6cIaaTBATSoAVJ267LKjz2CbXbcZEzGQ0gTtirbl1XQSsQO9w3b5mNYymXodASHwV-Mv5yyftPXcO8blhUEbnHtKk1PmqQ2Y8Sy3_GDT4dqTgr1gy7NxLBhzi439jOmEJv7X1palCxRl3wIrRUh1OBBkaKPVwEUqvlzaI_3xIJw4lWK6IZd3JaB_fqbuaACe2Lddk4Z9I8yA0jEa_Q-1wHyUBPD30JFkmJHbpK9xZQqSb3KLaTC5xGIIaErSOuXgdwtmT358TosU24_sc4K74ur6q4ts1MtZQlymmjw2lTLh2dA5dReDwU9DiEbsIsfQVbLUDJZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cfWbyIAL4OnGAFG2mresm1xlgZ4-BnDJ2g8AGvsp79CwBC1e83vAnKDSoeWd75i_AIJEOdKn14c6FHu_rLeigqObS5zQscXgxkQxA0QMYqrHq2GbzTurghwY6iNGEEqAI_5Nfs1_smCVhaKYb_LNLd8dFCD2OlrfRX6aAd-ZyKcE5wbtSJRW1LlFHT_rgV0zaXjQL3_l-3BwiBa8M7S8tqbCk9gF2OHvggz7jllcrZd9t7WtN-Kx7i1ziP69VAZK9d2cY7XiEBPRUi_Wab1PDVCX6oueViclpi1Xun0cGE_9sS-HAUl61K5XVQYxWTwjjgpRcg9mnVFaynWf-pou1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WHNEhRYpZOdHQ5HrsDylV45aHm3ZTLe8-b1iPdUKH90n_h2rWg78otW5pd09xUJhVbfbRtbySRV6myugBywBXBcm0ehv3in5zGOOhXms2a1jTZUbd1sROo3JBnCUCZJ25iGgDqmALKjRUkoSVRBfYhszo0uOkJCuE0BgkUhdJ4WJnA4fIrRu9uJsTqm4fuho7PuOWEehDRpdVQvSFFGgOBcRfpo3T9LbZ_rIMERHFIH9YMlgFzrdb_MGpE_7xA9Z5owLqBRqADFz3aELGHKBtHmnhVRG609Lv1TdnXoPeU-nLIXr7KhTeDQohsglk3oIdAO5x4gs0rXZUNYhpgePLA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oKPq0fzXftLW4-oJs3EsrkbmMSRogV9ynlNf9KvxpuS7MdodFkiSKUQjXFbwvGSiAVz7kZntbL5bxOHCuQxiSTQi3y8FWRXMJvAx1posaT812qnrQAcRMvlnViJqob1-4-TVswfIVv7bwpbQGV-PrA9kh8lITNBIsJLzhT4cR2MGtQuBnGUDWQ3kD_b72xhLwjs2uROgQMaaWwOCkyD0W47qE8FWWUXwLfaq29kIPjkQRGvnfW5zC-_2MxmRKNxyJW-QLdk8Bir_ZILhM5bWbwMpE1KsKwZgq8wIyfpKmhVsiv0CXtXi-IId7eOynXhc4M1k7HKgFh0U5yPFLRR86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g2XYMD5VE_oVU84FDp70lDSBOq_Jqh264-xaoHcifhStt8PLgjXn_1B2MgK4B5QfJuMuYJ0gqFWd6f1D2Do0dZcd5AZqlc8wI9w30c9ggl0gQ4MXvlTkkwS8sp0KZkVJAN9k2ceigcuEUcN2XdHOnyj9bNY5NqT4IuvfITTH8WoD-_kq-sAmPnw6R0qzVENiC4bIZhWS_FxlL4FKOkMRrS3EsN0tUwVDwQd_DfcsN61X536u5XTsFbOFkJdAIEf8VHzpo29rxOaugvD5rxHMZPfa_7aDK8lxkJCuMxCx_izWTRminrdhI-85lrVZvNlTOGgUIZiD-lsHWzRLlCLg7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WfalqGGUSIOsHwhJvoTRnMM0ibBGvmefPLUZwI3AuKyBmZ-TueXf3t6U8BU8SjSEBJJ1cr1fYkfxhmlNuJXD1c_7VHfCO6CYF_V6T5c-CvVnM3TtJ9vqYc5MFnX5HDIi_AhyUHHo60NSxcDJk6l5cfK6ufhOnGrt3ppxUt1UAGaapow1BctK4Z4wV-J1gcfUdSBuZ8X8qKJeN32agCICKipAzRGqayvkp7vLEPz1tDgy7S2-ccds7D-QyN7mXZK4iPPL7H2KE06CDT_rUOiIxAzvw6ulB1Cc7PSay35VovqiEeP1n6yDnNrbIhr1BJo1d13nUZaKVCoh9-0DsrDOBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uYtuzqW-rTHFgS1hhCqqtjmF9YvmzQWsuvlej4qob8Hrtyykhk5BRqS9Ak8LyGLNvsiD8HQUcbCcU2wXCuGAvPFataLBJdNRA--0E7U836MaS0kEmghn_xR34rrJ9Mc-VdXw2FJn_sjT_5f8eSGggKaskXyFoD93AZN1MWE9X1KfVeiYjiks_WCKg98UUBtyvonSTSobz71KidFkpcghh4_uXQvWigDheqctqsmiJn3Wes2XKCkCJTL5A1FPQUEevSeHddNwPsI0NwOUWqtLIJ09oW9pXcKYROTN_24ykH0gGY1BPL5Bu1S7VQ4H__guFJB2_EgZmFT5CO6NIsjw1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v9-9GqvfJtVdrP7oj-d80KAnbZpnGBb20gqIpKmWXPCcerwijDw778Df4GawUGX_JrJ31yr1qRla8Oq4l-3UGHuGRYHZHsLEnxUJ_97rgL3oP8CLzz05vYtk7g--b76dN4MURNPbbO1WMMeP4HVNqqXLq6jExBFxt_7cIo1hdb7P8zQu29hd935q4W77sPBD2225-6N7tZtY_FB4e-DWYlOrdbNFMUNUqCd18mDbT8kFxU0ICpI0MLW5euBr3W6gVHJEdu5LHJMLSSVYCJSEXueQCvP6eiSCIJ-a1rd7RZXz_6DJ7_g8YLckXJ1V9Ltym5Sx4tgzkVn7Tk4nGzEywg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/teBrrlL_NmBui99IxEkikHnYLMujB_GE-mOna7iQnyhkiMQqwGPQ-CSbFfPQKWcfZmOMTwMt_8boF7-vYHrNJrDBHmGO1nbbDh06IWZzzFBNng4AYEYJeMSkc3fSSazdjXybr3ETc1n1QhTWUSE56Iz10Lpr7oFunRSpoiyqmr5OWlk3IZ8PZmwQ8VNkORQT-hjOnGMRhFrIJniSZXg0PRvS-Ds6_DjSJ51RVMr_HfFyF9w-9dnfnAnmq0tbjFP-24E2RfvVStUXGEZvPY5Dl21knA6Dah32JBd6iIKgzZqSB6jeCIlzxIlhn7oiRg38GK87iwOzWk4z-8V_h44pNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gT-o_808VWIakZ4PsI0sFlYNehtW8JtZW8_y5AVNuDFN_9bak5AriOpFI4kl7-KP0WkbXL2xT6vRwVVVgFey8PikPerdHLadjEnSgn8Pz-lrgSu1VwGQtWciRh1PygLLnITly2YSFtecEoPJ1THjfYppjSyGo01_zi24aEDrBMEv3v6SPIGzDRKKetpf7bKhmMBLLN_Tfwc7Gru1Z2-tYxJVCc2ttulHwDidn82U8xaiAiSP9yab6GCNJrQm-YsLLXChlfr_xYE9cAKple_EinLY-hdaMFQ21XymtRu3ed6g-hN_cIaYGKXRXrHKsHrr4oGxwH3BAofxzHtOVsTrkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q0iVaIJaf9P1tJit1D6qIemUS_0GQwO89iZ7Z-1FRYISDvvqNGUnjBaqwp-mdwqFOZZB9tSe_bogBT-twuP22EakwBzNSy8KrMa8f5eRgiDYuQk1gJTE4qScK32Ub1rRc1cUjqa0BvhoPTxhNk5DruiPhdBeTCUzegEePRChEIKUr_vxRTuMLgVT4JmFzJeDM3hDBAurAtJvkNVIqe2nysUTgOPxlnpLEAWZstX4nhLzW7XfDNGb3sNhSyXO1fDhdOhVz-eQgJSobCL5qiEg9yjpInkCNQWkFH_zt03vyzE6WFsxr-VCY3qU53FukL5zaGG21heKSwLsfjd-RJLlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RsKqkpaRvGlC9v0pHi-VdHAiK56oXcnEDvRKsz2HAYgPB4UgXWBvtjrMzbm4NvJSCliukAYXgrnl9Vz0_ACnd3mie0XDNBW4mKmM2OVSecVZs51rvMyipxxlvnV3poPkR61EX4Kb0Tjym800GCG_WsQ7rWy-9xfKJKG4Y2BITZbneDD8_uyK_q5a771nzWLA1YIvD5v7P_f7UFQDh2a9B9kBaBCCzhIFgsufVuJWFMpfQ6ibZdrygGX5Esc3P9sT_UV-p4n_fmsBK3D6gDr6EZvs7KIrElIIF6a822oEIpmHsn3nFre-2E286DYkgXSrJtK7LDgcd7MZjkH7GZS8Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RlFCK2AQwwP6iwrinSPMnIgW7jX6UkOtmIzsJU7cMETm_op1c7k5HnFkbgGhKBqeq6uarYObpedVFCBQ9KKPvjEkaNZdmY2682q76D3u0X1Wa06wyNbskRrjfI0eWuQhchnCOyQWsn3eIHtWim-qNaw6NHqoPzghPqDcHNvjjiD6LoFj49E1fMpOc_C1FxUoHmMV6tHrS4Z06Q23iyAyRDBfXELvS7m3cw4U6_HxewPfN5lG-gV3ohz6rhS1h9kE3MNlLIrXjtc7lZBxarLf-U5ja6fKKI0RAIX7VFDxz_3RUm6dTyICxgwXOn8POs8s8dEc08yOdsvGru-yvmJI8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fde87h3iUn7msN2X_e-xW1IHMVzGH_fUAMR3seztfqMIMgu3Yr-kNi3-U8Rc-fNa1UQEt8fKnxlHWfQ_y0ac22Q1SEtO-41CirjeoILbZefy0mVRfyUyazESid-sfLV_h9pDchJqGNAWxDtRkIUb7r-mkDtVUQ7Ujne_tsHhaF4OubdTDMZc1Al9_CUHl7lYdKzmwTj-9gnuDGOmcf7Xh1H_n9uD-qR4yph4BAThizlDZBAqx-pf2yboVqm_klqn18zcHAtLUMiOnjbxZ57G9ihiMLB60RxnYnCbo5ZZurDy-TPMwi7GmD04I2MiNO_iaiRz1rnHH9KMtMUi9sQkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QNb_u21E8Hf3OwmpKX03IZvKjK_IeVoEoeFSEbdUccV78nmOei0aAa5aQhMEZlMWkHwmr5gFUg68xdH1fZxFgSaAoCAH-MTpxThcrcQnC6cCNGs-mt2LPrAh5wYBjJ5ZPlJhd8HoGbOTE0a_SQEGOS8CewDm9fBxqVojnJc1SNVD4sv0awYTCAFTMlw1Z2daYAYSU4p0XoyQuxCiYDV_8k71A-ZypJQ8ss28uNYXwdHa29dgwl-Peu72UrIFME-fbdhvtJfYFU5FhQbbncG0duda2xLbvWfgHo9xzj9U0WI7xt71KEkN9YF4aI1NDa-8jNd6nMSEon5WiZBv5iMMcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S54yDLUK4-j5epeNym8Y0MiVgThMsgZNwgY5xQBMvVKsGoUARzlypRWW7HfFC0uJljSFB1uWzI43bp3KBNIVW7L7eQ3IHAoJYEBMvaggysi0CHcHb88345WNcA508dwOKzgQzWRAK8zaKRYpwdwJM7GqClvRbo5U51Aagzo4PLyKXMR7nYNPu4bs7VaEtoMUAnlmZToH1Z-0K8XcS6m6N2UqiJ9Wg27ImtQWLeivtlAhXPYvkwgbY9IDmgO2wGKIStpJMgjuw1tOmhldMHlcf529TjdlWvhDm7TeF_fw6kk57mDFMKXfI1XP2GPiMA_lmzccOsHEB-H9VrnhAKEHCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون
با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://aws.amazon.com/free/
میشید، و روی Create free account میزنید. بعدش سایت خودش شما رو هدایت میکنه به قسمت ثبت نام. VPN هم زیاد مهم نیست چی بزنید. من با کانفیگ‌های BPB رایگان رفتم که آموزش ساخت اون هم اینجاست:
https://www.youtube.com/watch?v=iAbYpjXyLpY
3- برای آدرس، یه آدرس فیک از سایت
https://www.fakexy.com
وارد کنید. شماره تلفن هم من گوگل ویس زدم اما نامبرلند و سایت‌های شماره مجازی، همه‌شون برای Amazon یه بخش مجزا دارن و زیاد هم نیست هزینه‌اش
4- یه ایمیل تأییدیه واستون میاد و تمام! 100 دلار کردیت رایگان میگیرید، بعدش هم با انجام دادن تسک‌های بخش Explore AWS که تصویرش رو گذاشتم، می‌تونید 5 تا 20 دلار دیگه بگیرید.
5- ممکنه محیط آمازون واستون گیج کننده باشه. نزدیک‌ترین بخش به یه VPS معمولی و راحت، توی محصولات قسمت Compute، بخش Lightsail هستش. چندتا نمونه قیمتی هم واستون گذاشتم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cb8CtVaO33uU9u3a2vr_Oey4WnwCTSeYJeyMEf34lIytg3DBQgviprorLQVF2B23hrBvrfr5xIbXqdhLwaGn67Gyb2nFlNrTgGrNbvmLjdg90JZuozBe85z05zWGy3y9M-0AGbFVTAFnxNVf49ZOcLDXUsm6mp1PYdSmE_HT4JD5jiEV6z8MNzi4TIoQWQXrKw4Kp61rnf3FxhH4ADFnNQ0c0bM4PSOtYRlYcoJvqh2iAq1YHYs0RdaptZ8mNVVtHJ62W06L9EbOWeY6dQ5T-TT4_4MZtAVBVqqNleSyvMKG3JVKi9iyHdM1Z7KSdYjvp22wxLT2um6rRwcjFousBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdlsN8bSH5s_sR3vih4N_HlSLu6QRNHUqUbWZG_uE3Fu4W3jSqEQ1P8cxywxlMbnOFOzniR6_gYTaMvNGJcjTDWW0VOn28l_JeoCqjM6cV8scLxDg5NfgkcXs8xf1fZMzUxvZLH884agk5pOXzWcNwaljgNLHPmI0-l1rbffxhp83wXvl45-SSOcmQIpJDlr-Ezo8QQVDlVTR_GZq8k279kp21DnuYRAHFedKttETfbais-n_1R_0rQuEXgsvtrWulQyy2jTv0AMHfa-iXxDq303FemE6sjs8itIQHq_huzNjkF9EvOpMIFIjS8UZqJbuU6igtLOLKl6xZmhqK8mQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDC1cIV0pL97TEies6J4WeJxU_bImu_KiuqfQygyk-kH_7tM8X8Bs7drmxRPlXg3j5NToPtAL9db_hSTxHp5rg6tXYJjsiMh34wX_cJ7y5NQsml54RTbIFaqr4_C_nLLxgj1KD00aPuZtJON42V33ye1Vulu73vw70xY7KP-XTYPWgRKNzNFIL4_NYhBdKuBjqJ3djmz37fWGmnjKoMPTiFbwuN6w6hsDizH7TnvyQbLYi9WWdGbfat1CzxRu6ATjNlT9ox-PvlAYmLCK-cZtYAoGJlxtAPEBoAw5M00gRkR1-JJrpKnpW3wtn6bVhtPFNRZ3jwGylLTXWDBqWAf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f5Zh9thiSz3VSPjyjKh2tqRNUX6Gc70bUt1J4cr74xt4O4-seugXvdkdYYhGsPE_qRnz9uBT7x3AsVnNi8TSsDXXJ3r73pv3mI0RDchltl7hvf8t2hDfbAFzKShROhU1pChKeBhsWfbIDszlXpPhvrQEtWaRohLfRqU5XT7bhqYkCMy_9nOPWxwln-8eeV7iZannxaq84awr_3aePCBhKqJtsg6LYXn9z0jC2cd3WgIrj5TTRQgdJohGZD6eUf7M_KZArQwsgW35lQM3LJ30QfunAx2sZXSSD_fi5NZBW0_W6Jed5brVcF1-jOSWf_ARnYJqEzfchzV0aoo4tT-y1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NLHdZc5zXdt9kowdaQ9DsyXMo3s-jU4ZumLyD8M9fQ_4HqW6eXZ-o4G3797pX4SyIZwnltBcXrZOb1L6Lyf5fldUkbdeazs3tgBKUS4hR25ehfScvCOKYScoLJuyrjG0v3ExUnwW0A8YS6xOENjx8rx6bMh7UE-QVATsCS7nO6cv8ff-FKXroDQjVppBOFjMK5Olqi-X11XEwzVM3nAwW9svM18inOzj-VSANw33hTUDeoieZWxUmONI8sXNkv1izrnXSpxx700vPx41uzQPu-JlEuHS17Yq-8ngNSUVMwYbo9Oe6S-somSNWcKI-t7yH2IqRydztdkD4Azgc81g7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N0_LTguX_FnFQBlfhEIzebfRadU3ixfctKtRo6nmoUXPjnUT7ErkoXpKd7Fqgy7flgiGJRvs44njbwhc16gCSdmPk4eku2JpLqzprw26CeiBdXS2T-36p-DgR3iRohOw-7WZ5qmnOzQiWjHshykXxB99DgcrI3muiXeTm71-RU36VpKtnfrSn6ojzPWt5o_tf_6iio-3uk6Vew9LHittVmYc_C5apgowlcHbs3u6T2murazfTlnS3RuiBP2P0C0z_oHKeYptTZkBRGyrwZqXpUoTCqk-h5PYqTPysFOlSWvtOrA4EEvc8IyPfRV4f2kkG24JEhQOD6kQvblDPjICDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OMOOE5oRrMqMXm-X9kBVCjfx8rK4joxgTJ5EguoTWscmZPDsgmv441wtWlvx9Bj58OQLjj3KHIZryksPZ8mi2GmpNaedfP8zZ7pGFPWkG5R_pN4RUa2kwhpWQyjgOZVmsN5s4nwiG8pn2HzOrXEDBYXkhv3S06tRNQ5yeBYPitaztrUIxtYrNkZiF2QziRD2O-dhm4VygH0-0QQQrOYlsQnITkihF3p67IfVa0uV_jSLrTEL3uodaRmMXUQSI1QLnXnB2dJbQzjoaMZ0BmUwScKjTrk2kVvTAJO6v2I-1ynizk7q-okrnMp5Gw31LRKLxlXj2XMGZMSukGkaB625Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fkgsteXEDYZ74zgFgNt1TiXxDA1XXcbeIgcu90NfWi88iSF30KGo5ZDwf9olBiN1UZtbXbtxMuXB-T9HrIHmHJ8Sz5sYydbbG6cRNtGmvp445nu_wmvvq2iVxzO8445wUI4KvocvVTCGGGDfE4aDtaWx6dRWKTV03falN824DDLDKMpxX-IiiJ1lub69A7LA0CI1hz-1_rzaa7PXTSOGvhiXuieKAUvuSw3ZlyD6K767SzzgnEuWRPGPy5s28tLnjCzYW-wGo_bP5pTb5acy2EuGUXCuJMPOjCfpPn1xCz9SmkofMscE-Am5R9xb2u6D6bTPkHmumheYO-SnY7EPvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nQ6h5vl-Vz6dwQuKhpYei35s2CjKzhtylA5o_dkQX1fpPkBRNt9NnS4mkzf-vfQqSyZZjCbJGTLFBO2i4HZ9_abiwg2zF1hEdWA33_OIj7MC4QKW-lX05mj7ScVGIdqATjVtxsR9Faf8LDn7LSU9ST4WOuHSAyBNmD3WeEYiJE4zsFDhuL30YUhJACpCxK_gTYmZHOREO9QgP1NCVTKSfae1veOjM4OhcGg6PKYsZx_yyAQknzaC3kWAnOF5dsbSc45KvuBe65mh2BKBrFfhp5d4Y2J6O6zbZSNsrHtfDCYk6r0dN4bg3sc6PBFbJ_OC0lb_E-nrR_rakq-7kDXpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gpb3zuHF4b6BMrkzXEA1emXP7VULZzPs6loo0BHlRfbZSoS6iXL_SKi_v2iitXfkNZEsXHEd-MyHtRPe5butFUsX1CVkwoXJb_sCeHc8aQRxIb080_VD_fEdNXVp0PkWgtY9ZSabL6B5rFjrO2qhODDR7-se0KcbAjCQlhC7lExKzwAjOcZiDWkHx_hBZOQxRGJL5BZ15iqXUDwiraMJLWbZZAx_eHTCkPXSeQjEFKBQfAlJxFYao4sU5tFLJlvjkdg9xt2nV3m2yCcHxKIdDCS3Gp3LD0UFZDxosMm-1sq6j_fHgQrdSa_QurtxgjcMQZTEQ65tSuIYVHlDSXK3YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/it_M2H5fq7fWDiliKJkRCkTG4ZaIr7k0aatyIE0WX2AI6IK1pC8dd0SafI2QS-Z3_BtF1HSdCNAjt84FtMSXKVIRPuFdhkRY6RQrCRGoXZflIHdIzzBJPpfONbDUR6SlMh8pFMUs7KzDz6xKw8QZhqcID_yHJkWFgnRJnsYQ22NSFtEPBLax7dmPPYztS8f0PR4-sv2UcTOM9wE51Y1jCkkPPC7ITOOe7Yx7_W3Tts35ZlP1_8cz6EWEatZZJvEnFSljZRSzhMKJuVWuFN2L4mJ20ztrxQ508BZ1ziIl6HpcPUlhUOiuRHvHEdvRFA7IKKqAdkl1WJRUH28iwuGKbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fxm4CGIAewOe3wh0L2vqtL11W4X3lE30CbSbMF-98HKGZle4BlCkklcI9EKiBjnpUeqib6QSe9___Pq69Ip2aJiYv9NZWJWfby8pY9qj6RTXURQ31jlvWHhOyGjHR0zREsz9qeMB-0JOxpNMT3hZDCTj69IRog6ssvCUwwJ3yTpBQFZHTe_DVUrmRf72u4gaqKpvMtejbNV0i2_gjIPwt0SpcjtqiFbzdXKlAe8HTk_XuYeHLQJYr-UTqUIhDVPBazD2KTReQfD68LSNx7rZwyid6kGDcD4BQH7Z11qFFm44wP_LAdHAqT4Dweaj_HZmyhXXZN3kU0g_M8wCfPX6Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟
توی این ویدئو، با
یزدان عزیز
در مورد این مسائل صحبت می‌کنیم:
1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور
2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن
3- تجربه شخصی خودم و شروع واقعی برنامه‌نویسی و مسیری که خودم رفتم(به علاوه چیزایی که به درد شما ممکنه بخوره)
4- تغییر قوانین بازار کار و حذف جونیورها
5- اضطراب، فومو و جو الکی شبکه‌های اجتماعی
6- درس‌های حباب دات‌کام برای هوش مصنوعی
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZstrDOT2TYGsV-CtBPxMY5sRI33YwHzqW-wlL4ZDH_KmDdkTGJkE5gdv5x_M60lCeFHjHc5oSXC3iB2hFPpy_yR6BDmjJkBZmk3p-mPO4j8UP4L2Xr0dpxqdllU_k2wS5sZxui_QohPIR5jo3ix_wVrxZ5HvswbhFT4Xbr-6EMeNDFYzah5Z6MoMB93IOB-xSZLpeO4UCITNR5Ixba4tYxgc10DI2gZ4CJCXsCYNtZJE8y4yu1jG7fnM9SZ7l0kW-4pKOpVKYywqrhPEEOmGJ0GQ8gJXD-0QwomwMlCcfGC6NgUgMffi8xxm_xzpFgNhs3YkcFZIXm3LEJg3-m4F8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fYym5alOrzUfAjVE1CW8FBgfHY6SeiGQFZ4yc2OrjJblFnVhxymDPdaC5BrunMgQ7E61Dn6bmJVOkHwpMc_rFmICTy3tiSS3L4FXJamTy9WZ2klupb75XEnc5S_ZaVIf52PdsmTbpsiLUXnwq0pQP2PdVvflh0fu1zq-ukhQNI_xmqx7p2FD67A7gRMcRgpoetW0FX2jIJ9iMNAcIv49z92WGLEHahcZEa65SO70isBuH98vqEvwIRoO8x6MinbVRzMjpyHEF16ryuM9WgOiBQWwd3xACAZXJ4t0e_y_qYSayfsDweB2_VAm14Sr2fi_dnznSUbNxtB3F8JXgrU1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CJ5gTyT2_h8vvcz_GiME4OXA3Ke3Im1js5eZixLks_uiKM6Z6al81m7aH44OfO__lkHcG9TNQnblAh1jCcBYkp6eElMrq_RfkbKVADyoVJ1ivBuUYTZb-Zt6BeuS9Qr70W3_R_iIMHoL9M01aIUSKR4Ko5aKQDKrQ8POFWWYoWAlYMiPYCZpdwTjQ_VcqSGwfipwzynMj9kl0dW_dj3j-9An0IaaPymyLw1uVMAGRu98riJoptRurYskGSYBSoYgZH1PkxSZeWLLqj1kDtFYKtPNvTxYUcOJAvrazsUMFlAN0Ol7rclV-xXgMlz4M17YxJgXTwOWVSXmw8vfxEGBiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:
با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.
1- خود 9Router رو
که اینجا آموزشش رو دادم
باز می‌کنید
2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline
3- این مدل رو از بخش Add Model، اد میکنید. دقیقا همین رو بنویسید: z-ai/glm-5.3-flash
4- می‌تونید چندین تا جیمیل اد کنید و استفاده کنید به راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
