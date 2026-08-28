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
<img src="https://cdn4.telesco.pe/file/Kya4ABReYZsIwWi-6zRoTsVVDH8_sFEWn6hRHp4U7eITzwr1PrQupzNWKMRqCgVp5i6StUi9TFg3VE-xic1TD7l65ez-NIwRp6gMAF8Q0OrkiO6o0xJf7kwZEBREjuCrmMuOChkcy7lSJF-BEuU5eQ5WRUOenKZadkffkIQ1TvQkKsXhZ1pqKb5gvW1oPiE8GcC8QLQ23GTYcwk21WYIBiltOHiVU8tz5q7xg_VOjVflzgr5MzxMn8xhyVm9L2Z6v1RkTaUpdK_g3uka7RIhMix5aG3tKTnq7TD1VXnZbszwcbSRPIH9H29USydH_26m81JEZCTLBwhgBJHGPqTtHA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 02:49:00</div>
<hr>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_Q98O9pnHv1ov642DEwoJZYqVoCOkr10PfaAAVh98z26-3TbzVXUdOCuabokUwoGUMMP8NjNaZLXs2ZWmHx1dX73OZFvhG4ymeMUmyConsnzfHZy--ipzOUYYMODHi60RJ424KmwxgyCwnVPOC6qtjB4Sm5yFJTNxJ5qAVWGSJ-EHb_42QBqw5tY6QWVX5LGXmtfCboS_RDvTSyAZhFritnHJ-9gaQC5IGvgdexLy52ZwVNKnPw4GbQudRs0u45h8TMAilkR2nNSh0BTwvjXLyl9dDCBkftcZKnBGh7OomOQWr_KDLDKz8e9NVVvNTs81eh2cHREyRYZFrBJM55Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZduC-KD8JriO1xUY_5tEO-9HAp5CMQddPg_JFJOaKUPtJ-BIDo2IwJpHLv07h-ubQZyikFeZhQ1-7Rglru-buWEo2VpiWZCkq1GS27utBcY3s8Yov2r6D-uk0la6cJhYPu06zRNI0Ga2Mw6I4l_vnoqZEdziXFyUhYvFratv0LzQVvyRZCJx-SH1QuqW-dc0cqbmVT_xaJv6Z5Md6l-rluZXPW5fUr4rjEEaOLaPxXu4FdE79Vya2Dj1Qp_oMD8kFhZ8emiL6g46rzjY1eJ1nve__KIw6avFYGf1aeH_RsVsd0tczqsA85lW-KKjY9_4_IwtQNLIWWmqBE0OXkq75g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDc6gHm4uRp9DV4BHCwmkcsOKqvRPuNeP_zdZla0OrIVFSsr0dhceyweVPiaDxBMD2BHJY1Qs1zFc09wW5YkyIjuCg6DqUBlgKz1whRJoZpJcwhnOJJJkU_NGjUivQrjet_5aaGBeuQDTUmOpquqygEaNXpeaHkvUXo1aMUQZ_N3CQ4ziAoqwWC2N5P2UPtKfYG9WNajraeyAPj0jV4C4LWGnd74TjJDItADrlPitVz8jmISyQhCVHibkATKhXvjrXaIrztnohbgYyW2odWvedggGbFfW_EQDZm7tKtobgOzDfyMxuGFavOBFovTrRoVpmdluwiXcfqsczKDP38VvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkIQJPm5PxIz0bwAfioqq0r2nhYZGKLwTobwrFzcKdhGr6do_2N3tUd8z9KieBwhh8Rh_r7raNulAbHmqkfNBovMd5FawyTskBy6NC6t8B5YldhQ7q1qopdfTFJM9VxMsxG4senE7PHxwAp8Ky0M-sr4i1scXOfM5Y_dm9HN1__P0609E5vyiG_oExZkwzXK4bNrPxIbuctMphazE3mOP_UNjPy2dMUJsjRXEUb_9ML8DnNSkxq70WnGqnGZnCJfAjDqo_fhzVuJm6A1XSn18JNNuL776Nin-YOK0MsSoCElK1PDtxYSnE8PEhiId1P4QIKkLFIHy4ws9yi4GDcZVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK7fsiDDyZuj_zGcIv4kiI4VuhOWuJW_DKtJPHHGjNX428ZpMkfXhExBRfqiLrpQJ-K901DoyR9crN-eB_KSqW8jWeQ_EbC_y7av8PN9gEy5or8_HA2mQKHKqdBjtg-icI8ygWVnOmTS2LRuR2xZ7x4qUIjjoPFLDO-GFliMQXQgKk9eaKQFw344Qq1FvSeo9iml1bWSdlfGy8c4yKtqQh0grNEro2B2vFs7_PDqkjsnrhm6HKazXg1N2HXqYfozA5uiz4ogYTXGSLOjO55qTh2YFR3zSYxzhHLa10InI13XuhM8UzoEqWFGAlUY42QIBJaPFNHRnaEDbdqNxx-cgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=MFBUoR4EcOcPlobWDIX4UL4v9n33EyR-5vnZxsD2aaRwCkEYAs937Y1jD4gX45YPA_Rt3dnwbnmXJB8le_Z5c73R84jBf3EqR62bE2jjtid2jt_BQSMpqrCCdvJA4rn2UOzQjGUQeKOv4qDmq9OWrRvJNBvqx2jNzVUfdci60LtckEkLU7JrBIR8bvXbFbVcuoiqCwjFHzenbKRiOyk6X01clkO0qE3EEr1l7noPcO0NL-GzWi0Pd8EUJeIJF3wCw5AKpFt46dl_JHo_94UC_K1VAGDJrqc4sIju2thFpo5W46o1iMLwz3Cj1en1yE2f8WXug887PTMVlG4hO-Kn-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=MFBUoR4EcOcPlobWDIX4UL4v9n33EyR-5vnZxsD2aaRwCkEYAs937Y1jD4gX45YPA_Rt3dnwbnmXJB8le_Z5c73R84jBf3EqR62bE2jjtid2jt_BQSMpqrCCdvJA4rn2UOzQjGUQeKOv4qDmq9OWrRvJNBvqx2jNzVUfdci60LtckEkLU7JrBIR8bvXbFbVcuoiqCwjFHzenbKRiOyk6X01clkO0qE3EEr1l7noPcO0NL-GzWi0Pd8EUJeIJF3wCw5AKpFt46dl_JHo_94UC_K1VAGDJrqc4sIju2thFpo5W46o1iMLwz3Cj1en1yE2f8WXug887PTMVlG4hO-Kn-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFQXfdYkxgTrGfyxJQ2d0u61ch6huSV43FVezH0B7bG6cJDExPthH6XTyo6czVONqbhMfdRz5DaMwXt_XTivrsj9gnv9gCgA3D0pv51baUM5JvAWHYoRxhDLmPceo2LJFEYC6ioIjyprFpCz1Etlz3kntaeJzIrwhyykHbt3ql7Iu7ub76NBW_F0gXfVIAoG7pSNVvyCP38Vn3IS_36xvig0dy_ofeILQg3ngIEdDxoBH0_woNWbKz5TRCElJIbThBPMRvM4_HbZAf2l1OJGyPcCUg_fUWlUiU30-MsQPymBoNE7Ve5_EychBWFidUIRGaxYLfBz4w3fsN8XJ5ehzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ID7qmwQtpeStPX02JQQemH7oQbNDrPxkvlBPo4gBg1rCJ_nT0j2rd_fdMGQuID8-B7CUgVQmZW2CpAtdYJeMMCqCm8IZ-GY9kjMZOSMRV428dDIlhXlizwoZT7BRzur_obP0MC9kcwBwlMr7v3zhvhb4n_Qj1KJ3eb4ToByANVUyjfYeJlAMyIjNS4r7mEMoypbT6vbq50aq3CLSw_yIPWJvEekwjiZdhckjbrdNhxuDSxL0ySHmjukvui9ivhofPvyTLu3ALVApKRTzpMBP4QWpFJkpriemjybWRW78aDhwkBXzTOJGDIzebx3rNc0_3-RTkkpPquHwimYkJffkPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=ID7qmwQtpeStPX02JQQemH7oQbNDrPxkvlBPo4gBg1rCJ_nT0j2rd_fdMGQuID8-B7CUgVQmZW2CpAtdYJeMMCqCm8IZ-GY9kjMZOSMRV428dDIlhXlizwoZT7BRzur_obP0MC9kcwBwlMr7v3zhvhb4n_Qj1KJ3eb4ToByANVUyjfYeJlAMyIjNS4r7mEMoypbT6vbq50aq3CLSw_yIPWJvEekwjiZdhckjbrdNhxuDSxL0ySHmjukvui9ivhofPvyTLu3ALVApKRTzpMBP4QWpFJkpriemjybWRW78aDhwkBXzTOJGDIzebx3rNc0_3-RTkkpPquHwimYkJffkPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=jg-A3RSlKjJ5mGNUOOGVxIxRjXV9UOW83Ll6Q5HycptUm6oVUJrNt8-0xdsztBY5U9YIoEv7hMyalxWBG9Hb_pm899ALHuVaAwZe_hbVlT61yPtSOYt9iT_iEE62_Wjysr8kYxP0X8LkzOyeN5m83PktVjyvOu53Y1neZQBxj-KQRPk0kuf2XScrZtfJYgZBop-RpjIF9dxupi3aPXH9BwcZgfs2nTWyC5QacFZoggdDpCCrVGgyCX0s_RmeNp6uIPqShL_6qX17_BSABCuGzxMq5R_7AbTPr9NK71UsjakC2byKlrkbOp0BN0G2ypvhd5DbxMcavwxUXyc3AcUHMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=jg-A3RSlKjJ5mGNUOOGVxIxRjXV9UOW83Ll6Q5HycptUm6oVUJrNt8-0xdsztBY5U9YIoEv7hMyalxWBG9Hb_pm899ALHuVaAwZe_hbVlT61yPtSOYt9iT_iEE62_Wjysr8kYxP0X8LkzOyeN5m83PktVjyvOu53Y1neZQBxj-KQRPk0kuf2XScrZtfJYgZBop-RpjIF9dxupi3aPXH9BwcZgfs2nTWyC5QacFZoggdDpCCrVGgyCX0s_RmeNp6uIPqShL_6qX17_BSABCuGzxMq5R_7AbTPr9NK71UsjakC2byKlrkbOp0BN0G2ypvhd5DbxMcavwxUXyc3AcUHMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-KcQfgi1E8wgKCYwPQ5Kqhz6QBTiIlFdONhQGgKnPpDVpmIWk_czvbmD2LYjEQIm76P9EQSBU4EPXLTY-_jS-oUHJaZx53O0t5YE-WWavSH3HWWe3_-7LF8C6sh42oXH-jkaeaGB5nWharZdz_BPgGnJ5BzeCpHYjPsPnAteSSt1zyJQDM8GwWkKxAlr2usMlYLjZFXuelsU6eslq-Fs-Fmm7r_GouFB7u-TYS2uCjeuylZhHTfYJbjWJYtmnOawix58WFjTSGnvooJL_pU-3wJirCkxy1DBkpno2T7vlfL2uQbSbjSB1W1vuBNuwazUgEnejA-Dlf8BL4wTCaoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8J8sxLtgGao6qrffvT1yHlpIbjS-1Qywkh4gANFda2GfgpuCLStV_VSQUQoynyW8Dy8D7t-Bo94gn8ex4ofYNs31k-ZfMeU_d6ZJO-ShaUZyOorAvekCZxO9oc7ytBSWFvkfXdZV5y_neyRBPJbDekkruXhxhpHbXKrsa6vrJKUA9GvHhegD4dqhmo94YWWSqth3PGDgSEtkm9eQVy33n_qg6dcFJUgWdj8-h_JJB-GpVFyHMN0K3ur2nZQbhZW2pT8W0rSkTmdXEAZGagE5sj5aaA6nFxMXbLQCLuUp37kukz0KYCI9oiTRlFCV5_YhFQCTbpUkQQWxFmS-a2AbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=EdsRmrhvcMhh3R5E14ZnozsLHkzHaXpVlnMSAjZCCvBN6L0cWR5SSgHv5BYApe396EdZUr3TESyPBaG8IfKoshSKCTeUY-8_fDFu2OaKbS_02uhWwSCtN7haor90uu8IEwcPEjTv132BhBYVKrJ0EsYoPR7d-O_SICJniulDHJjgWMKVF_KbBA6_calQ-DwmkTkQXUVFWDlF1fHn3asoH288Ovzo66uGunfwgQic79hiJX5JRdg6hbqoYp_vMc0HhGe2UTfUm8j5-dh5RDD682jJAW3M5OlCTs_1aMITKKqQX53oIo40nVx4TpeZWo8UHLsKvgqx3YQIxmEQK_cgUxkQ_ExWB2S9BZ2JiHDG3QAHsWckQtzwhVeYPb006mzmkEHMXiuZtlSk-YeyuTMOmnOLtOg5SXFEycVuZ5gnQNfBLZG-R0u2DQwlQ7t2QMyBBoBI-gIkObzaT8ZYv7p2jW5KJoJDky4LqsGEMKSoztcMNh8FMOG6YHWVegMGU78nUiKjtMSWj54PKhctb0WR5VWRT2bbBXh_zj0tAKRiRwldeSErbdk2BmfBaf6uko3KIBrW59RBAgY0fu3dDCGvyNXY_xSGSijGJCZw2A0bvkKQyLix4UzYZRwfJ2ihuNfdtFgUkdLOmMF6flHaQGpoeNpg3Va6g9FbcB1-XZSkCdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=EdsRmrhvcMhh3R5E14ZnozsLHkzHaXpVlnMSAjZCCvBN6L0cWR5SSgHv5BYApe396EdZUr3TESyPBaG8IfKoshSKCTeUY-8_fDFu2OaKbS_02uhWwSCtN7haor90uu8IEwcPEjTv132BhBYVKrJ0EsYoPR7d-O_SICJniulDHJjgWMKVF_KbBA6_calQ-DwmkTkQXUVFWDlF1fHn3asoH288Ovzo66uGunfwgQic79hiJX5JRdg6hbqoYp_vMc0HhGe2UTfUm8j5-dh5RDD682jJAW3M5OlCTs_1aMITKKqQX53oIo40nVx4TpeZWo8UHLsKvgqx3YQIxmEQK_cgUxkQ_ExWB2S9BZ2JiHDG3QAHsWckQtzwhVeYPb006mzmkEHMXiuZtlSk-YeyuTMOmnOLtOg5SXFEycVuZ5gnQNfBLZG-R0u2DQwlQ7t2QMyBBoBI-gIkObzaT8ZYv7p2jW5KJoJDky4LqsGEMKSoztcMNh8FMOG6YHWVegMGU78nUiKjtMSWj54PKhctb0WR5VWRT2bbBXh_zj0tAKRiRwldeSErbdk2BmfBaf6uko3KIBrW59RBAgY0fu3dDCGvyNXY_xSGSijGJCZw2A0bvkKQyLix4UzYZRwfJ2ihuNfdtFgUkdLOmMF6flHaQGpoeNpg3Va6g9FbcB1-XZSkCdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK5u6XB_T_eV24in1yBq2CTND7aF8p-ukEt56pSkoYIUhFV9iZ1EPMyzhKVI9fkihm362Qzw1m0fljxMKW-dsUm04Ji-EpDbFCYLJyIj31d8HqWNYonPloTV9UQl-SbAE6zETvFODQA_u3vXQRS_yjQVrpG1qTPZd8856RD4fvHtwnB7rUBCp8APWy8a3YllMoLGezlWOYU_2h5nw-_qoDZ29cdV7RO9EOqnG5kRY4t8Erb-_zbqDjQvo8k9TVapJwuhvycVt6I_VTj8ltDQlMKPLFQdThwKjbEzkDckta6K3zYk0Da59NYsV0nkcEoYr3FM4Nvsu9a8CBCkBiNGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=VPIRC-tswRP2rH1jvo2JZ00QwJXWZ17hITWDPRM0eMnfrot9oKJDmbnLqR00obC_XcGoVvihNTMC6C1iJW4_TxrySDc1HpomoVsQUtsRfjRygDqnY4FmP3Gl4FGgCMhpyNJY6oUp1YXj_LYBDwuBYT8WwhqTRC4itFkBvCJKBtvxBeqDaoZvU2fXOVmYKbJ30Y3hd7icUFw3SUspTqi01CZmMf4DXiGs3S4_mdcr_rvrT9dS39XLUzS0fkPpDUF54J-kSZpS7Gd_vr5fdyerpww-oB746Vvd6vdgoxFBSXzMvP_0YY4oSBCR3fDWdoN7JUjoiwTRDyYi5WLGfvJkyi0izkTarN8jCfyn_2l7UiJc5mbcRpYSlx5doy0jqxebGb-sd6ukvTLbCZKQe1rnClEqRDeNA4qIMqQgI-rJKUqGdTGI0wExs_zaEsPrahEQ4hpVtT73Glyshi9cqJ4OgQY54rLJqw3XgIQYQp7xruoqCYzLauLX49DOt4CVCXZiPbvwNIiI2uKBe9MNWY4lpemgOyrTTqWc3w8QrIVkze1x67DvGzkvE-o4AIh-3V0rsE_kdzBTKhtF_ie0BBravsg_zYTAxJTCV0wZqSofpJiY0OBlw3Bo0efHAJvuWurJ8DIepdIk1-4py4OLllQmAiwF7ZgmhnYmyYUMvC04hsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=VPIRC-tswRP2rH1jvo2JZ00QwJXWZ17hITWDPRM0eMnfrot9oKJDmbnLqR00obC_XcGoVvihNTMC6C1iJW4_TxrySDc1HpomoVsQUtsRfjRygDqnY4FmP3Gl4FGgCMhpyNJY6oUp1YXj_LYBDwuBYT8WwhqTRC4itFkBvCJKBtvxBeqDaoZvU2fXOVmYKbJ30Y3hd7icUFw3SUspTqi01CZmMf4DXiGs3S4_mdcr_rvrT9dS39XLUzS0fkPpDUF54J-kSZpS7Gd_vr5fdyerpww-oB746Vvd6vdgoxFBSXzMvP_0YY4oSBCR3fDWdoN7JUjoiwTRDyYi5WLGfvJkyi0izkTarN8jCfyn_2l7UiJc5mbcRpYSlx5doy0jqxebGb-sd6ukvTLbCZKQe1rnClEqRDeNA4qIMqQgI-rJKUqGdTGI0wExs_zaEsPrahEQ4hpVtT73Glyshi9cqJ4OgQY54rLJqw3XgIQYQp7xruoqCYzLauLX49DOt4CVCXZiPbvwNIiI2uKBe9MNWY4lpemgOyrTTqWc3w8QrIVkze1x67DvGzkvE-o4AIh-3V0rsE_kdzBTKhtF_ie0BBravsg_zYTAxJTCV0wZqSofpJiY0OBlw3Bo0efHAJvuWurJ8DIepdIk1-4py4OLllQmAiwF7ZgmhnYmyYUMvC04hsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5sllQm7Zyb_l9eCqxHn-hq0F9Tj3tWL9nMdWbk8_z78com7Mr3GAEnnkWCM4QwCKTgj6tdSZJb55XrII_Ygiy6Kz3SyHjn3KFV3gB46-3vinW4zA8WeK4FqP6kkN_jicW9IbVv8bMPWPnLO5kbDXDY2Diyv9V01FDOqQL6VdpBZLLX-xXYZepwCoHxYprZrBkO7SFJl-ye3euGiVo1ZB9RSMD2mVHPlDLGBLqg2MJdHsl7ZP8PDBu5fcX3KaC0ES1rzO9N31DvFTiJ6J9Mz0br4l_7M5ty7nDR_rUM-91pO6zVmXNDwxpo5gbQxzUh3jllOQ8sDHcjPFkcHzNyzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QjxIrkljdC4ARfaFuAS5K2ljbLIgQeKd_jkli5Q2iXOSh0_NpIjuceWKzyBo78T2ieF8zBF3_S_M-ylHKGgko5CuL_KXJHzaO7TKZMOYYC1IMAc7XgZpwHW4ogg8r6WjKNEQL1Aqhb4bJnQMIpbeRwOpY1TiYRU6yGnv-KgXG05kqMUBfWG7EpPxaCCzFRdxw8lqz823u5IHm2_wwbji-HE19enDpw__mpbv3rV9eOwmcfWTs84b_vu9kIMcWiAL68uQbtNGPqUafnq9lB8B75Juqq2vGeK__nqX-zvirklf7fVDt_eNgQ_N4s3seeuAiKL0DjwJVkZpKoiqGc__pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scI7ESqHx4X71LbxmOFLi5O6-72rNUIJkuwdC7mjbB1mHtwCwS4scd0RqmUaaW7brhN86eyusbr_NEZ_Jc43BLYdGYHKqIILnJTSD4fmc96BvYgj0zT06XEFHa9z01LP_O-GijmsWRyM71xjha1zq-E7NI_lCT3A88l3_eVTrU5qhYSG532RYdJwhEAypKvOkDoc8Jsc7Xf_S-BJ18zcnEFSZVa8xfP6ceT8rA93pt2imscir_TLJ43wxzp9h0_i5SnGIRAOhg5KgQ-UlqGpu1L29kwE1l1R2yZdBIsRGvNLw3y_zzKuvl3ZHGYFRzb0X3K3d-Qb7oE5qo-p0suIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJP0RPr4R0lUUwslxuPo3w3kSRUobIBvPXRax4VSFKFhcf3V3OWVwckXdjknpnjLgya_gYubeHU1xRJ-40f7SuCbTXjQulUQteIxZ3bbXTRr3FDVRQwXaqK6kLVmB675r8axPv-IaybpsNiaZsHhWQ3fGmF8rGwd9EVtF8VTYBbmCYDQusfENXWOroFRGv97OGUkNidaBTszRms4CGi5gDazr1DDkPov1XiwYMtBdZHWDxPAmKxsU-a_xbBqwWw06TTEM55CzkQUJB5odTFWIQNZ3XMQik4GOU5KmkM1Iigcjx9EEM45tm50piHpCT3b6l-uWJiKBrEZx_B83likkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtMkJYiSlQ1_6LZooTTanXBZnYsSGpdMC-_6CdWMCCn5LDoVvbwDOLL8WVOWfNuGqD6Ggs0TJiaxZ0kOPlSuhDnxOKkho4q-dLYkZTllu6kyo7_WTKzrvPgqJ8bHsazV3mBBPvEV41Z6CM2Kzz5D8sUsMtehavwt-w45GVAXCnEnB6908N19aK8Vo0jtsYUCF7tPtL0CRNkth3QG04Jre2UheSGEghXjY75KBXw6_yoV0MZVEUzg7zP40wOuqUWIHPksqt9RDUMR-L8Peqs9sUkLCKwpTbTL1mmQpY5NcpnarHBmoh3o0BphHR47I7VvCrfAPJ_xyPe_nGj54OLF9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dN4UEfLyBdvjARUce7VvnsKSCLaAnfUVtVV38ZMtrKQET4fvXqZV8eQjXqrGRAv0nUXaJnOs5Z6HCJF7n6eMI-jAxIzhMTQpLZm1Gs1PX27xmuYRzU0I8oTqkBP5-pbGWpyIu4UKAUgSm3ioLNGc02w06FGqe6rfE1Snf7ixGhl0ulFUgyayciGH3MsKnVzEUhOCAbCaRCJhAiboBXQPT6B--NOYlfQD_CiCMNSRUs6hpai-CkSO43D2cYIc1npwGonOSS-Aa23JWdTE5Q3_aSg_PLqCtJRWTlGf_yuUl4g_n2s-SWlTK4lWUUhKf7L_s-XTDVRJvDJby0xq1TFTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGZqzlnt9AXjA1BdsC95CsttFalopuGp_S_I5iaZTkf-aKczJkd2jCnRgMjBMo1oDKT-MDwa-GbcN8dAdZCWNr3gLC19usc5NPymRX34vG2fu8F17A7XKEq3PBsFO09iq2S29g8x5pyqyov7_dnavogL04X20vglbpj2LLwLhMQyamM3hUSym9obaPE_hryaidXzlxjzsmc9yc6sn58VbUc26bGiUQxLJNWTxDx2kVf9q62EiT5NVht5coSOjWKgEIaUUhNAqLseQsh7OAXjaRHYWIqqvew0YcoOIbzfMQJ1brMLpmaTXjkVHgZW00g0YAdg1I8_wMFWD-JkCIWpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HajVAk_sO7nMFqs2H8Bf7VHInMairGB2e-QW5vwSao6Zwe1FRBG3POOK0EiVIi2jk2YJI3gEg3wdmMTBwCGiDOaJ1iTot3_DA0ds9plFj3ZlLqDp1YCpZIp3x_SsTpgkEhcX6YzbQaT25SgG9V69r4HCvuFFrHhP08Rt0077hPuu7xiw7zTihEBu_qYUMM2f79Z5GhxwAFDeS_lTrdnsHj0jO6RnnTH59gMjaov8ZjZHD3JPmlxSB52EDp_en10qxiHyTeT6B_HNt8tuWAS-oCCaw9Xhfqc5RUSwsYi3WNPi4mY5qA9dctqokbFlR-JRxHTh8B3fISFmNnFqyUcLdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK2JsnnoVRNRTX03rXZA-s4vEPdOsby6Znw_PnYbFyqRyAsRtcHrhsPLKjVKzMfTI5ifY2gZwRJ5NlJFFqoQ644mtBzHLN-JPW6yhr_hpslQp8n9fsKb65NzfuoGniHML2dJ7K_d9ILl1IT6Nz_Uhi0u32ir0zn7b2uivx4YfsbtxmuEPot4dj4gvj_UtaGOIaAAOE0Gr1RZqmT45mGwnvIdFPImX6BJXqGpO_s5PORjueHNkbOb5JMtgkNIZhqimXmKnvT50zz8t_NCoeY3WURodbu4hbIPlKfO4703ImyAWxYUpw-FxLrm5Aa8pd63WQZgnxItHdtbCm8586T5gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMJ_pFSh1hgCSOlKyEj23Doyy9TRng8IUnLm8cLCYfkbYOGB79X8lOUwTi7J7CXOOZZVkPEWXLCcI7jmc8B3SFwJSE9p0YHWfUojo10wMA3dmiAZ7Nsx2su4X0L7wz3tWTLGaKsss54UDfWugfojJivgG4cIiGAYMl6yA79O11HtMY0vHVyPPoX5MR4IdicwXv1B5HtY9IPE5BCEUCELn8Y6CkCxxs2SoWcf3u958VEPZrCMfqlaB-mDwxGq7u3mFHmGMHy8LYVQSf0xcqY7McDEZI7nDjEzMYRapjPNiDDJcdavsRyJpBTz0KXXL7uOJCqGKRpy1k3IhtPM5rIm5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHIN--3FTd4la44ldnQAmfaCgjEnlmm4OGLUbTJu2Ql75PsqmjM0yI-mqEXMXIOZLR-pKYJaceZeS4nheIavRtvi7EkJYy1wNoMB57I0etueIxzJuFhTOvKuSd89uQEcp_S1W44da9meDDffWin7XathntiL-3_HEju_sDZONKhc0gWo5LHTaGEcuAoPyukGIxYs6_Xln8Isz5W62yHv91m-d6RHNmGrCU84-8Iy1e_kE0NuRsHmVmjKsUta48iPeXqscN1eLpR91mXE1TaUFC59wc3fMSTyKC1JmXAGQreK4N0yljGjZhzFL6z2lrgAjFFE4ZOzerMhMH9FDxP2zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zafdy3jP7t86qNNZ1hrkK-HU04Q4QbaB7abEC1c2VEL9Pf3uXsp7icGxKFiFScJziTaEgcn_dUWj8aH2u2Y5BfyHMCXbkQSAUxk8hnbytn1dwEflv8NFMybVp67MNhaGNW7TgyZnDL9mpfWWUFPvPZjy6mOvrN3HZ5vbVhytGjOkhoW_OG5fg-bbb7kW6YA4fr1A6NeGUy4FsygO00tE6LRkv51eCkvrucVzESbr2CVWD4fdsXufPnKAL_E4M9UeGNFIm9TcmLOA8pGElLScddcdrkOv8GkUS4blwSyhBfU4L-IWa_uXFcTbgyix3SCtJw-j4EsNj9xUI-Fa67MdjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO7msTBNEFAy_rpAiVMp3gyBSdhdCWRhbpkreZbVurPG3U8cta-tevladwc7m_7uzbzdSgjZXXRDLdYOV8v6J14C7yoayIc99G1-7EennufU_6JbzX5rxOcNGm00im5M-UwGxUXvUB_Bf_s6w0X8dUDVlwYslOpmtWxTWpvpbw52wrqjPhaKPQjWWUShqv_pRp02uX3t9eGFOqpsK_cV2BImfDu1gEvL6771wfzR7L2EOxfaxlQGajYjUjeUgiL-A8f8gU7TbGkYMs9m23_o6hJPjjJdwG6dqxl13QSdMSpKkmRpy-FUnmIm90wFKkvaA6ZjVioYw7CIMG1KFpK04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diDjibOjPzKVj5rI8JCFvvItM4OTPEae3XTJaY00BjZm2EK60ctXSfA4g49dknvOCJk6BZJJaHDk30gtzbIbTDSohpLtqWVXvWa839QVpO8ePnQpvCeFqVr1r8e5k-3IHHr54E0RxZMuQQEuLUfAO8H29tZNZ4EDwrP-XxxtALojPiXmZJNVLThAuC1wPze1aLzmGm2cXiMEyGBHI2lrgTndkGiCzWSVguBwevR9CdAPaO8vmI8adwVv_lPWLm-3TMNT7kyE4Bu0jAUSOlKc3Xf-CY-GxEH6CbgE6l3jjOoi0_QS-xW6ItVpSMBP65WijxaKuXOvHVGvPrdTzenJaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X80c1hoZSkGRfWRS4bj6Iz-pfabwG8Cv98C2YQCCcSfiyEKx84sTeVKsuoJGX21aIux9FpOfs6pYsS8AoKMy-tjzQcQoKiI-DvrADxUM7YUd-UivDuyFq1hxUcwSDM_I6y-W3dDmBAEBzp0LSq6qcak4P0cAqi0qhwA-p7cgM05TbwJojFO2b6ZfZFTY_JvMaqDTDBy4EkT0GdTTgxDNHds6ZxIkhxhXa3SmMBhmC5Jcw27DPh5XBUzT7IqAuvGNd-cdb_Jn7niEIMkEynOsA18utieE_GG3_kYFnXl54mTyVMG5tHs2-OXrovQj-rlb8-SNM1nYsYGlewg3EvceOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r0ZKzuckjYh6Pz_RiuZ1-Q3s1e5Ek5C5xDkOg1QQLqjNzNQq_xhDSonggG01vGqjjKdDDrd9HM1ESojyXSD_CLtGT3DuNvdPfFDWPApzZqLmHq9ekxy0OrZG80tm-Q_-jObUxjxSbQakyJk0X0aQ8vfFshsyc5kzlJO-iEJfIFXNZBFDWDR10-Gvi9SCBz9XaJwwEi67p2Sw0omyJVYGBLI9N-D6e-yYJCGOD8uwlubXjlG48kl-q5Un3wBTMvJlJ7qoRGVRjHPxSk2K80YQrFNT-bi42X3xAObdEI-doM9CivsSYkhfuTt0ULf5HmiNuye6W4LRePbl1njuRoRSig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtImohMDHmjljWzcmC7WbTLLdUBD1GDkeEzsVCL1XTeeY9Wl_y4pnEZxsy7nU1RExiB6gmoPn58sL0t50UzaEdQ3ER15xGSVNfcsxQvsbo8tqwZkxlBbJB_YLU-3nuExfQ_DZAkAai7r9zO117aLYnvQLXg0e8hu2FI-3KFNDucAFFREDyvfxqa6tgOOdwzlNik9gfxe6sM-sy4wVCZ9GvjCj3PUBa3aPcW0Uw8IL0vYSE5Js0G6bG7z4uNTC5FyDfEqLg5vs2xSqn9NTQxYrNpPRsH_fyzXwZN495oh5yLZ6RJmc87j0QYzGfIgH7m2PVP6VKS6yceDmWjdBmR0_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG3cXhq0HeZyP3VZtmCAIHcNZALkM0RQtNAABgf8hCgoYdtdWxgov4WxKjdycizS8xWQSTQUrIpln_c_lTETc_0aMK_lp9hiHWgpOVCDE45BUsm2NsF-DBRyP5vufLFxVYJ1P3z8YtEqZ6D8x6GvDGz135Xaow2-Q3cdzaL4IaimYVMuIqoXnhBHfCZ7OhaPzVzmMkQ3bmFdLOW28SSYc3YoAIdmbnwyCP3fXDzzbzKe8i6X5wsdDmiVc08MvSFNZaktcd00dT0jJL0jncPu3YUNJHvZiL9FPPp08Og3r78WGXNHhU3-r_DhsG-2mEwckDztXYoRgCID2p7E1MUo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQTJ_wb2Gl_umOsvMTwekXKARLa_kFy6PLIyeC5_rvXjgnq77MyItTu8e-GO4A0k7y5GD3VodkkzYiXFU23GvqidYN9f1mjeO2uqdXZBMFL60dJgC4XAf2RF_2Df9wIq--SF7ewSMMwtAnd9Nm7f4yPhQJpt-gLuUc52TXHdNd5xUQ1ISPjtDpiDSAWrIYbDuwizTPApqTK1D64dJMHYP2_k_uzYH8M2nJyhkCB4LPnC178RM1oCNb3joXwCDQPWL8D0P-X-s25l6_vc09-pCsk_CZ5KinMR9mCmK5JZBVAFm5MvLEdjsHQlsH3uN5dyRWXs00G_L6elt-79vkub1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFK4nzJ9_ETPlkoJBnvh9xTJ34NmhlDycAYe_vin9srvTRmL-d4atPrmxKn7Gg9eYmacuC0Jww1tisist9G3QvzDtGcUdETwM9gKHJrAzQTCogjNpQLsT4zgpUInN9G1fCx7bAzg6m7PsiBlmMRxYkrYELhkM6-5Mtk7j6LVj2sRPw7hn7uKxG48SIAS_OaovN4nIRkIvYp9dvKkAm1BsyCxeaNBeeOr1ouvwFnIsohu3OhuB634BpH1RBuA-Td4u-JICzpYJgb8Uzbt7LWY5w0-jni3D8H84K8RVE65Nt39-VmqWJp3na8rDyL8ap6L9XuTufGgQQ0DA8PYu0TLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coEdTsWFN93Z4ztvrKjuGTULTbPJci5hBzk7DBWjTaQzzPwoOMNT9lrhtEjY7JaN91a2jAhDFiUdxvji2JfLagsSZtIRQGnPNzcRuxbSXh1WXnlZp7ggeb8EQsKhSZbkJKez3hErLgLJjvwEP_POf4G9mILNfSufPdOfPnRrmHwAMufyqBlQ9xlwbyTbQJbF0z7OyCMDdY7i_BUngQbGnL-1Ns2nHw4TN3xCJrVOum_FH5mkTDaEQ8u5WLoAPRyXJHHhXn7VhGSaJ6-eZm_bVRbcxsWDVBy5QSo2QDaYJ6ZQNkOP0B9MDkzK7J5IdJ9bk9qBK2-qvYFcFLU34ECbYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGHMwL-CVaQL0-O9QPGGwMWk4MDkngFngKTRALKH_aWNfzCD2rwCi52-duRau1rdea1ZugIe8B6w9NOlvomAAhsICbQHZSkhHK95pgrzhR-jDG1-0LMcRNDlIbwmLK9q2IY4wiFpA3kzRT6U41dTjfdhmI8YIVWOgqmwfVjLxxPRLqhLj3xKyX0vYcD6wmniU833HfnNht5NXEDRuBdWxdD1XeN9UdkuqA-caiNX32RJ2uKzKt1d6ulkq9uN52Z7dnRaYQCm39H6M_RMzvxWntTQ4jACaBYrItiCbZlBPY7zpgJj6UDXe6GXhghfLjSwb9AzIX7UhtP0-q8hn0YqRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOF7aMr_i0HDCPEC1pYNboIAz8UE1Hiq68pKEfIY4zVSj2mY1AfePqPKNrbQnnr7aGW3amgUKMmotpA9IOOT5ohhTYp4Z21702wv-6_SClcWJUCBTonW-cj7sGF2_NZZwWHxqahIPyi3lcP9JDwvYjncgrmsZvuZLjnV4zc4RJX06YcTf6GavDPMXpUbupB4ElMEmz58kworLyi01hPXma1Rl6jRGRq67H7z0WKV5Gk4QgmkiuhLMT3Yer7XpAtRrB1AIflM8ge0iZlfWO12v_BGnU244gifQ5qHrbG5yBxDvAB-Va4skH1YcE3t-3xajTUgE04fxJiY7rieaBThaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5McWECrSaYhmsbRXxEWgLbHw-VtdvD4AQcGf6k5VBlGrJg_2YLxa4qGdqYeT2CxBvvCMsS62nZYMtc10Ot2jrQApI8NiK0ymuLajKVgL4yAQdMCuZX_WQ9q2qGfDDcr1MXnSHYEcUXpsCJca0INGcNbnEH_DAIAOyZtgQ6XilMzi8o7ExnZzE9gSI5E0kd3W01-wB_af7_kteyBuhB7X85FIJPpqDqZATHH9Znvhww66d3_V4HaiNzbir3o-Rfiw6tr0AtH7-VPVPK9I0wG6S-Red-2QoR6Acn-YJDMLZkQEWYcmNRYN9SNPH0rGabs867EsV2qaKXrZDt3dDGdOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKZL80kGjCemNCxEwPNTndqF1RrUiTnau4ZNFDGB7DouYK-9UXd0A1ZoxqOBfRu5fOt6J2ekzNFX7A8pNXLTI8-tZL-lVVJ3G3hgk9fAwcNjH1htihHr09niKztDVhliJtKC_s47n6GIET_rt7Ou5nfi04UCp02jKWVQPAVzYesslDmcgS4REjbULCIq_ZBScfCFZJhtWUUGLs03UPvtLqtwEFO5kIQvYqXypagzFIY_6knJBfmiCVQf_ENq6iO_h174xKCRjWXPFFN415pbYcTJpokEHDz9IYNo-F6P6qQ3rVXkKkB1RSr7vaeEKhrM4Ui86ja_MIKuHfPU3RVy5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHK2XF6w8X172REbUSz2sJJTLUNHebsVysogXv2l-84ZBB9IcinI8TcrtE4U8FWCD24T_IF1J743cQ1n1OKdXEkX0FaqZNLer7yySogrnwFSF7L61J0bf-z2GDMr5QB-k3xDxMriEd1ss-PWqiUuwDHkeAuFxTG9FN6dAMduk_dcQ6AZ7y6IySNUnxGyEFlSKd1eCGuEHe5VtUVGJGWpOFW4f6JwxwBRcBrVNhu4GYCbvnt_y7_rZaExvjPz3ZykZ3mXzC4wB9rczQWvQNGv0z3h1Y03dPbfTAtyVNLAVrqLNgciLwTDFkzf6dNFlrn9pZz8GlGXRijdAVd-F7u1Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmCZVhQ6HVHJzDZQi0cKEhiDLCFeKDaX4e438QAm06GGD1t_tWwJv_w5eDtMaASPmgiceQbhi2zgPJIkxLET1hSy4az7Jg32VXBzVxOI6dzzkO2KJmOJ1rF9PGy7T8JmsupNaU0YhGG96I9w2vimigKJdnPyndI0tEQuSBAYSYiXBHP95X6GhjWSBu8YehhlWqm4bAYNpKubjkWAswvxh5Gw9cn9M1dz7UTQ-XkwduKVBYzxJSS8vY4QevGC_iIWxFSdcFAlakTBLsRdr00prY81JlGVyz8RuGwe88Q5Uh1DHdlrjwd8-lIR5YG1I5GVO3QYmLglsQrABQcS1sRKSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEgDhx8kMG4iQ-_G4_TAsUi1wBZi-DYzedbGsYEW3Rx0inZRxgLxDk4G0FnbB8XNCjx_WWAHcQhZOYlaQgk5-V_txx-pAi3kL07THyg2LFHUMqvJAPN7aKL-IKsMhZyznhx1RBqrrDgql2rxzO_TCkBT8tL-wii4YFuNDEFR4n2gwkSKje586zMwY-_DlxPNHk3E8SUr7-F3bBTrGOYiP0m-rq1tAZqmKMbeON4bktGf9DUW0H-cRVCuEC6QY9wSKEmKwj-SM5vO-3AIPp8boy21hfe5FbireXusVKb1lnLUOzdsInuMZFXI--doOpTetf_6J5HyVa8AcD--1BCCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVYdUZBIPfrYKtYwaJuheuYqPWVLwHfSbYA6jUP020etBeSCid_AV16EmJy2gKK2LHI7JZUH5wldTMe9zQtr0XR9BB6aooo7bJRNnUWCEG9b9bOJAlGGp8O0AbHiwP1YKwq5FleiT3uK8lPOeh6ENakB2jv_fDm5ZTSVimui4Tk06pBq_eWtGDhNwNTuJri21BqHhfhjpN53fprU6U0jSNrXcFBtDTKgQD6XMAAwLsykDQyHmkUQz3EpLeASRELe-IdILPkZatmz7IkraIkk7jaKVpWt5cSYJ38vmjri2ALSxSKMGJyVBeKq3v0Hzlvz-GUpkfG81uFn2fbuBaIuvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVHWfRDj057TmmWx--1diqEAYBf_trxF3rFwfuJLQ2PHBGnLgDc6pDDyV9NEsuZKzBzr9jHn1gXKiv-Y6gPW963zNkfarLeOKVEMOcLO0XXX0LFF41iYbgEOi0yK0Gu0d63MbJjek3pX9uZYPtXoOm0r8FdceEhNpKFttBV5gF-CbaqBh5ptjaPL_3d_xSHFz_JWGc9IAM8BENEm9YBuLmujj0a7ro6A-ucZ1tVk9QtHOu8jls3QVXCnWAGgnnJZsuqN-VdAozeVESOhubgGrOFlmpPfS0-BZ5fMo1LPxbnFY4byw9cSQL1qSfGEgynGAjRb61vTR5fNDhOUK-OcxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJW5gboEZrCFl1Pp2xOM-EwzCEOIFvzDv0wyOanekFtBy5qosSoSsYYjBt8zHZ_V_2lF52-6x_dgpULG7Ckbz-D_HfpXx6DgxzrsS9zOwgTpjLBXwqkPA-TrT_RkXy0hs2LGfJ5PewNCn95J4x5zhE8I2vMa1cvQRJtKlaj5lcceoQpvcc-xRsXjW-bgXpEpR79RgP_EqNo2YFMkCeJCgfzNtmyem5K4NCkOxVrcUJMN-w4jQQwzvysi79UElECp_dSVL4yS7ACUAqe2b3E4FTErt7j9EbAfX8DTwH7_sOMlhkZ0WW2fjEhxJt6-APGRHarrJz8r2y5xTae_Yuj6JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #43</div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cmHyc6xCW97mlbnM76DGHApzQ3jF3Q3g0E7nOPLMHK-2VAfEoFQf9QEWbBeNVg_rBTxCkeyBqK_naH152MiidiEtKEZ28olgb5g4Ozku7xtRKaXaBR6-xfiHxCJSEShf8AfKVTvKkxkuMWvDI-d8jlEHZQ_mDnxTb8lraAXMzP5_k566-JXYgGdJLfQxex9CjpTIKNhNHDSOTVqDUw_TdpKzTmNZ4UzWVYOfN5aHT8UNeH2-0r3diceN1VQxlkA7MIu3_kTYvRgyH9OnkqhagyaBrmhzRzpJy4CDP8i-zsdQQyhkEy0XFOXpSf9oWUgcHrq2LiYhtCWSwDoDGUKL3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=jxh57L-9c_k8iGVbP8qEIONwyFhsQrMKbLeLO8Yr5Ln85B8wHQTCvEvyNS-B0YgvQ2Doi-OgbpLEKkrh71yM8hjl3ncoRtvDgLTJDfKUJY9LK_FVTcgrqs4mezu66RgGdMvCyPd0Dn6x4f3YRgrl9i5UWjHaopS6uw8_Oa-GMnbUl6vgxFgLrJlx57INgi26GhletDQu5uR9_dT3XAgXWxhzjrKQrxZGegDI-Pd385EALgpHZBLTe5gSLGT4IMXFihiNxomMSp1Iyfrgcxy1RpDWFS-QTqu9ZMyhBFYZt_LyhuIxADzjqVps0mxcojlX4ovA62GByh4XO-InV1qbKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=jxh57L-9c_k8iGVbP8qEIONwyFhsQrMKbLeLO8Yr5Ln85B8wHQTCvEvyNS-B0YgvQ2Doi-OgbpLEKkrh71yM8hjl3ncoRtvDgLTJDfKUJY9LK_FVTcgrqs4mezu66RgGdMvCyPd0Dn6x4f3YRgrl9i5UWjHaopS6uw8_Oa-GMnbUl6vgxFgLrJlx57INgi26GhletDQu5uR9_dT3XAgXWxhzjrKQrxZGegDI-Pd385EALgpHZBLTe5gSLGT4IMXFihiNxomMSp1Iyfrgcxy1RpDWFS-QTqu9ZMyhBFYZt_LyhuIxADzjqVps0mxcojlX4ovA62GByh4XO-InV1qbKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGFyM25nkSvA1hkjljwEpGU3G-rmZEe-cRlwygS9krLsXB81wv9nQVyS6o-tr-4bjrxSdbGtBHgxi-LyiQSdZBwedCS7S-rDaE9ju36x9GhaVc_e929cccJ3q9_YDd0JrTQ2hBnoDUOXuYIdAPwuSDJBjPokLfIkbp3SyalCrArUOlz30gq3d-Nj6g692uHaiDmYDzgRbvRcLjL7EovA9VnHvRC7FtBWpSF8-bo9L6CjktsDz2Rvv7vQGybkftOmIVadi1wlrRwfEuTZ_ILl0trNixiDOPeMPzS59OWFDLRJSvxAFIKV9rR4Kdg2aqtOXG8ExEGtB_hJeEEWyfKx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=BRaRHeoO-PJbQ1KwSuxBqpqRZWLvgKqC3gako_mM6R6kkA9K8qMraCcLd-agtuA2L8f9aKN05SUVKm8V_0SW-zmncBSTR-LA0LCh6tMS8XYE4GpF7jgFVKIp_ubzXlGqD8uQ7xEeNI2GGqTDoeH-11fo9M9lZV6EqvVqIHJzP3YXu9jhtRvakTwktxi-PiScH7ybp3Yhi_ujWaqFudXAJjnwhY0j8Ve_AFnCD2HeMRx4MGbXUscQwsVpJ5l51GnBV_n8qPzhXCmaPFVp_YSS1IY5NO-zi4yvCYsM3SgIoi5JeBlQBooV_M9j9RK-JcnherhOPJnuntUw1QDIRUtxEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=BRaRHeoO-PJbQ1KwSuxBqpqRZWLvgKqC3gako_mM6R6kkA9K8qMraCcLd-agtuA2L8f9aKN05SUVKm8V_0SW-zmncBSTR-LA0LCh6tMS8XYE4GpF7jgFVKIp_ubzXlGqD8uQ7xEeNI2GGqTDoeH-11fo9M9lZV6EqvVqIHJzP3YXu9jhtRvakTwktxi-PiScH7ybp3Yhi_ujWaqFudXAJjnwhY0j8Ve_AFnCD2HeMRx4MGbXUscQwsVpJ5l51GnBV_n8qPzhXCmaPFVp_YSS1IY5NO-zi4yvCYsM3SgIoi5JeBlQBooV_M9j9RK-JcnherhOPJnuntUw1QDIRUtxEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6iBHKAbQDT5hk8k7-eWs7AydOVnnUFDqhaJaJ0Cu6Wq6_NRERKR14xCjzJcUpZ5JLBMQ2z7IJdMjQtn8Cmsr2zmR1LgnUBSh19nIKzisSR5ikW1z4SsmO0l3_mHJ4_OlOoWU9EP4JUibqJ4R7gBh5mMI2zBELMnoEyX0GC7cUJ41XK5uem8Jnl3rbk95cfRGWLaSKi5qgn9Zw3NItaKYo4BCf1Xfd0sidk61fJWvfkTqpggGQbT13rWOkEG8TVVM1WD4-9X4QE99wSKP6gPZ477n3tI4QL7SXH5I93jhlt920o4NaoNCCOLhvhrS-F3o6gefhtcgf0J_841p_5DBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfmWl_2VqumuTkOFjpHj5pRq8gnQJX4_Aseom8jd698Pvrg_zpcXHXYxeSKvZ9ENWd9BOXaO2fIV87LE0RrJnJRNyb5v4RzmDeNk051UdIGxdSNnak7Lr4z0iQ543tJA8kr-tpW7sNV1Abfb06O9HCI_hMn1kEmUTAcKD6pYVNtOEcqM20BQZ2molRCNi99-4wXF7Za-_224px4FvGjDP0R8mQBin9CYEs-D-bclq_DUDseFMBnYPLk5oQ4qrzaUcStJK6S5W1maY870YeKFyseGCIuIyEiheIXOy8SIVcmJfC8vxohmPyCoKRW9JBRIMpmCyQw06-YPvN-lmQYrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=Yss2KWGosAnxNKdj9aX-2s2IN77guA-F21ssn2OkrRrsluiZQa0cjGS0JZDMNLfYBlx9yhdMkDsYBxpuqcD1gxAIVZ_O4PmAUOZR999pbXcCdhC874QbU4396aJ0Exgg4lib_1OyltlhaRTfmIGqJiECVy7AsAw_2X2rsZbffxY7Sbbv-COxBteX6tUhzKkDXi8nCS1y4Jb9fQn_f2_8-JtiRRJuQvCzGgJvM5c6qvfzXthKprrWd5ZjeiLj-hTkdV_cVBhikK-NbmjvZjqQT1FEy1MVzmz7xDBNb5VmC3KUPeDlEtVY10CMxkSPrL69wNEobFKqduUTASjjHCqNAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=Yss2KWGosAnxNKdj9aX-2s2IN77guA-F21ssn2OkrRrsluiZQa0cjGS0JZDMNLfYBlx9yhdMkDsYBxpuqcD1gxAIVZ_O4PmAUOZR999pbXcCdhC874QbU4396aJ0Exgg4lib_1OyltlhaRTfmIGqJiECVy7AsAw_2X2rsZbffxY7Sbbv-COxBteX6tUhzKkDXi8nCS1y4Jb9fQn_f2_8-JtiRRJuQvCzGgJvM5c6qvfzXthKprrWd5ZjeiLj-hTkdV_cVBhikK-NbmjvZjqQT1FEy1MVzmz7xDBNb5VmC3KUPeDlEtVY10CMxkSPrL69wNEobFKqduUTASjjHCqNAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkKYMAo8LXre6bQP99fTElez5yM5GjUMUVnvLxkEY97szbI89fq2R0OsUBwoj1WCJFRvd9_QaumyrN2zzFWoLlrl0uK1kNsrh-MWQEKVoN5LVO9tdni3iPWX58b508Ymtu4_Ul_OCcog5DAUo88oVu-z0WI9SJq0PXdUTyFwRZGEs0PMxeAHLCAz2Wt05ca6pdecZ48N0SDa__1ghBC1EoBE180tYhsqteT-qgTSylVAx2E0kHNXzInSLcg9UDBiD3ZFO2FOc2DWtVSicj2vJOKGM3vjQlu3yX1MoZuWBjTdxnCegtNbuU1JL5eYdCHlUeSOFQ8P6D2GekuxVDc0Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5IT1qCLAnQO6hCU7j0RTJJtPLcRYTw4TuGO3OXbCmA4nq0tLGh8ZxN1ZMqZCgWMQRqSop6jAlwatTgs4J9PRk_h1xqDnwi0BFfRKHXYZt1dd-O7lvpcKLt0X7NMFMFGWjA3L_xS7lOeM3TB4ZZC_PFYvm--mfcLiU3Gt47KMGsV8OvzmajSNarewY1ERusTpY_LEw_vB2libGHRRfhvpcqqDrTDxcANKcNdJ_zLIn4iQcqyyQWBncOp7mdcD02cM9Pu6WnPin4ScoSmvms3cbB6_OoCYeQvOJjcHlUHcpg5tSIwjgWaPpP-_c0itEfUI2AWWLdGUGuMzhpsHhFSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stdtackegb-zIdFP4LNHJ0fz-5d1CSZb2ds3y1q4iaCKj3nvRHo4D4lCGIGcD8faOYo0scjguORJ55TTQ80oJeAC9qBGsqFxAo6rBF3m--krcamU5Io1aHwJwayQLSo8Oog-XBkS0NJpoZzNP81TkBv_IQJDW8q3cfwhlMqk2RQQEMeQlqE6oiWQYvn55XUBicBuH2zkIkmWTzGVYwPMbt9pyiGSc2j2h0Y3Jlr9HhgqbUH7yF5i2kQ2aG5rsXjoqVDQaB26lbuCdiP7C1_vopPwRh4eYC1hOAIW20k4i2Fn7jEIF6IguggI29XzyE-Rb6w8oDpWz0eryjIc4KVIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=Rl2Ck0WGCOeWOfN4d7jampAuUZOfD2D9SqiesyoUehBAUarE0AdtFmKkWqxl0M_r1Cmcln7ATi8tFfZKQtAYHEllKFgcIks8XIlm-yC1YL6h8F6NNaZqMAfDPdD3pMehOWlMobDk12iEbDphYcNXvKbRmMSMPSbrR1asNSGfGo3-JGQlNpdd1iBLA0gqChcDS3suU9MzLpa-TeMa9Klcwwqqj4SDC5rzJDlQqIqrYasGLdfjcKzQyF8EsNfn21i_17a4BrtZCUFhVRmAV4W7Fruyenlq2PJFgkxouAOPJSKNVq0evtjn7LWLLNFwmk2wLjllNVAzsMTHsB6cC2rGzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=Rl2Ck0WGCOeWOfN4d7jampAuUZOfD2D9SqiesyoUehBAUarE0AdtFmKkWqxl0M_r1Cmcln7ATi8tFfZKQtAYHEllKFgcIks8XIlm-yC1YL6h8F6NNaZqMAfDPdD3pMehOWlMobDk12iEbDphYcNXvKbRmMSMPSbrR1asNSGfGo3-JGQlNpdd1iBLA0gqChcDS3suU9MzLpa-TeMa9Klcwwqqj4SDC5rzJDlQqIqrYasGLdfjcKzQyF8EsNfn21i_17a4BrtZCUFhVRmAV4W7Fruyenlq2PJFgkxouAOPJSKNVq0evtjn7LWLLNFwmk2wLjllNVAzsMTHsB6cC2rGzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=F8js3jo_PHHfM3mQR2u2F7ZQ33U3xTHk9F8A8mGeS1QDcHsYlQAizvXu7MPeHfZOcpQrf80a2o5ANiIij9LXgCwYJaoGcz3YtJemLwuLq39rCHftnrm5fGCljSXAI4R8mW6XOsfr7CC1CtWftW0vnCL36igult2ErSUMrefgkusTgZflvJD7vpO03qDbZs8KVaL7ZwSjo8X71Fq2RAg9Dglx7MEdtVLrcGJJZCgOSZ3VyeWPgPZtBz4iMa515GQSOMXzKLfED1TSEGCF9osbeG8wOXq_PF3jF244PTC9CG51X50Akxddbj0dLGQPJDZ_Gp42_a6P6XqLe9a_nFEX0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=F8js3jo_PHHfM3mQR2u2F7ZQ33U3xTHk9F8A8mGeS1QDcHsYlQAizvXu7MPeHfZOcpQrf80a2o5ANiIij9LXgCwYJaoGcz3YtJemLwuLq39rCHftnrm5fGCljSXAI4R8mW6XOsfr7CC1CtWftW0vnCL36igult2ErSUMrefgkusTgZflvJD7vpO03qDbZs8KVaL7ZwSjo8X71Fq2RAg9Dglx7MEdtVLrcGJJZCgOSZ3VyeWPgPZtBz4iMa515GQSOMXzKLfED1TSEGCF9osbeG8wOXq_PF3jF244PTC9CG51X50Akxddbj0dLGQPJDZ_Gp42_a6P6XqLe9a_nFEX0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZpMEYg-S2gZg9VIXUmHNc5Vlcc6hdIg7pRhJOYtwPSaNdz5Z_nHdpOu1X6-zt1DYaCP5tEfEz0YpLu_te0Tjwfeans2enV6Xlk9vab5jFeCa0UgijcbHcvA7w06ebIdaGqvA0YT1IgK7XBc_VgINLT9Txi4eJfQnJpfMD8Mkl4bt7G1pe1mnwC997hriZk8Mpzb1XU50Ug4CYkvgmh5TMS4qhxIeHXPVf2R3BEpeo-uLGBKSUFmeXus1w1gvwkKquQoGjnOUpI4GoyUtegs8w9WuSCi7wCd8tgb6qcF5aFqkvp0P_BePPRoNsoPUQWyCXOilSxE_9FeQJI9eXa-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAXPfFJpgWBSCcpl5deb7DP1moX6q1T3pwQDpQ-YaVLuO8z0utTffy1TAM_hvEQAXZmu4u59NrJetESYFfofPbEjsWXf_Wn4XXkog2Tme-ygK7r4vv1hDL-jDEFWqkXW-_MWgBH1acaiH8V-u_xcPwcBRajnLND5vDA4gAxtysl4VXtRxJVJbRKAvyJeqrK4vlW6nhMHh-hxpCFZFHeJ1khjWXjmcLlN-74jlkxzEEHK17Lkmbzd4lUB9bXqlLogbazUcp0VcB5XO7DvELMqB9KQkUFl1gwMGhvvRc13shu66fUBYUwkbiBWxp5Dq5uTG37Ji33givKY_8cmOgNpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgydp5FT096SuQHcIGfRVTDeYNB1UoLlDQk3EVgUmDHOq4z1SK7teyNluYKFj7wozlF3FcWTXmMKHuTdyg37xIms8dzzodvoS6ANiJR3G83CFh_h4HHMGKzCqqU6PH5TLzNnX-gbu8OrI3SdrzE--i0XzJooWEHBI9QoZeqihbetIP-x0DvZX2_GOJxnlzxE9efPuk4TuByqhfrLFGUCdy8VGb39WsIr7QecpEW4ak_qql77fafjZWx39kYsQg_Zf7SlmjToL5XCBtieMpYLVaRVp0-xtHRhzFuFkZ-Moebff0NvpsznJi6OMJdRBo0QwnrdXwkwVBfY1E76t-BDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEDZo7DCvv_7-u8MA8rh6hOT2AOEtxDS8VNeHGiSRC235MlbFHlZFnVkrRiN0Ls4pfoadWkjZOWbx9y5sFhNWCs5NjkwlVA7pkhNTxhhECvR6lG6uR5ZEmEie1ZawGnmmr47iWjGPF_nRu_VTwhUUQwzU5DkrckZ6yYsw9Jf6pe_tUMi4RmoiIyWmfaa-4v3vGysEcVSrXvlI1W30xq24XCPkcf-AwGVTXy7RKedCxWLm6dMo7yLbi-EJJV9KdqAdeTByrCDRZAJuX8JVhhrkOJXTXyJSj-Gjsq07mN3nA0ns_DvRWTwusWRc8Xq8X8QcfoeIMu_5E0p0vnbUNKJNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEsi9c8fkf9kSxfnR11RYHGDxy8oC97hT922qEStoUIILx5FuKOlkjKvv70kPlJWYJKbBx6N7aeh1d9JkOClZdjZVXA2Ss0t3N3L1eT_i8t4tPaeyPgtPcDyEKSscgFMtjVYZb2ZsQt7bDI4Xf9aOwGSUWbbYYfWgX463dM_SyViU5teV8BQj2vCvmvfU_oNDlVBB6x43BH1l79_nDAwkotb3XZlmIB0cADRKbTemHwho0Xv3op5fxEaX7cg0-pDaYAho7aSU1P7W3Z-x-KNbc5nejezp8PBzWtRzhEBLmweJf6qqrLifD97uiYl8jFyr8UL2DjxzZU5xBFTCD1Gmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pflHJopqineDEdjd5z38ycM-RcRUEw5y213P9LbUjHy3s_PaBhj7OQm2tx30NnQlLzx1LhxEjQsX2aeZ-5_Hd6-YXzM91bfgC_wo-oJkCxccEhPQZruie9PChWuTXvGk3LK-EwlwEuDylpVWRkaRP50Y0JZTXAJpWmj9K2iQYahM3o2tIKchBhu12r7vN4DcqER9hCQlbDD62PYRKPAK4I09Qzg4LTyuPrUOe-9pkvVhkwxC5DlUFxTgb_e9XIL_lgEhCZWAW9BlU1zUpbjzzIMFmA-eClEpOHG75jKwp42ie5Enz5wlZgnKKtayX5lNTCmqMmdXX0HvhZ0I_w1rCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubHNFDQ_5KfFvQ1nfRTCXzJXXCoTr1LYfMpkdYWCIBidw03zRH9DjfHu45qCKdV6e0o-I0Wt2EEz0CBv3ZWv3n3ihLLIylfzcXtKQE57tK_9G_I7axbSFXZNHo8A8m6RjVs982whaowF4e_HLo5cK53LV6CUf9MHLElojVwexI4SZrpE4QbTDWQ8jkfW2lkRxN9ujk-kdfJ3renA3YWNIqAVA74G565oU6zZWOlwR00QESrTyvBL17GApSuUh53X3ryz3O1izWCHGa6WFcZcxFvi18TcYBD4woqoYx6HO_YwjsQ4N8TbpeNRglQGZb2qFBrhYoL8X7TnbfkdQsDlbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=tDpkIBesYkxPbisuRAf-rrwGWAqt-iXpj5-FJYhS72dPikAF9L6INEkh7lC7kX_fDMAD5t7p-lizIlZ5JCG1xRtzRAT3iXD_0ICumuk_1FGeKu0FM52dFIjXv3jLImTGM3xTuXArhJ-zq5yxv0awKnzn943OVDZSVuQMKHBwrCzoj76rD-nz_Ip__mriSIpa_2gO0e8m9CmunDMu0VhE23CsnwLIP1R1TOaIAHqcPzQ0wMWBMhUrF-x05c6Vml3IYfs4NizcUmOM5t9aGcUqXPeCFzvnMW10PwMNdc-ToVhT7JHNS9wHw9DbUx714wjOWqaiEup12CjjHh_ZDqoIQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=tDpkIBesYkxPbisuRAf-rrwGWAqt-iXpj5-FJYhS72dPikAF9L6INEkh7lC7kX_fDMAD5t7p-lizIlZ5JCG1xRtzRAT3iXD_0ICumuk_1FGeKu0FM52dFIjXv3jLImTGM3xTuXArhJ-zq5yxv0awKnzn943OVDZSVuQMKHBwrCzoj76rD-nz_Ip__mriSIpa_2gO0e8m9CmunDMu0VhE23CsnwLIP1R1TOaIAHqcPzQ0wMWBMhUrF-x05c6Vml3IYfs4NizcUmOM5t9aGcUqXPeCFzvnMW10PwMNdc-ToVhT7JHNS9wHw9DbUx714wjOWqaiEup12CjjHh_ZDqoIQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=TnWhnwBeRqHQatjA_2rRfNUsJxX1-a_u8VNux4QmOJSDv4z5wBtOF_PhShe1Y1RZanv3laxIO-2I8b_FF_3HvZSHnkp2zWsxW2fXxPdjWaTzDA7E-DMf2LL_7UHSsUB8IwHB2V0Wu8dezx1vKu4xi6W0hDImXy9fR_eTKFG6dXvwSREuha3ojZVBGSxCzpT-qVgkW8fwgTMYWJnqTPnhKJlpT2aoGVGmfX-6UV5MRzLJsFQFTzLrlzROaGdLksj_jmurax6cO8f8koPTQLsrYWEYZWjKh66b9AmNlFvTucUnZzMd2KMyea_V-rSLEPdm1aI5QD7VJLGOxSvWpIYWwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=TnWhnwBeRqHQatjA_2rRfNUsJxX1-a_u8VNux4QmOJSDv4z5wBtOF_PhShe1Y1RZanv3laxIO-2I8b_FF_3HvZSHnkp2zWsxW2fXxPdjWaTzDA7E-DMf2LL_7UHSsUB8IwHB2V0Wu8dezx1vKu4xi6W0hDImXy9fR_eTKFG6dXvwSREuha3ojZVBGSxCzpT-qVgkW8fwgTMYWJnqTPnhKJlpT2aoGVGmfX-6UV5MRzLJsFQFTzLrlzROaGdLksj_jmurax6cO8f8koPTQLsrYWEYZWjKh66b9AmNlFvTucUnZzMd2KMyea_V-rSLEPdm1aI5QD7VJLGOxSvWpIYWwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=dOJF4K7JVgD0Ys4xnw9Jc_42iaBXwXrtsnlqPvOFzTuAltevXuc_snszszPDD9vkVpbpc_z2KutMa6QYbFBhKBD4zKwE-o-riitS-2_QvkYSTw-Je-6YLg5iQQIzKPAOyIog9-M5XuPSkNIuZRuYvTWAI8zolLsRKSSObTeqjPID_TfEY06FXuldQmyMcCTFFQeRAg2cvOv0skPn-1rU8xVzj15CSzWJrBxN-Y7g9Zk-Ewxz2KmtsJKbxLyZenBkThG8mlJPnCdnvwfUXeh7BENXXnLwlFIubHQwFNkt9POzY8EW-H6BrGuNkbP13wGVCdDc39ey9lM-lw9g-1demA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=dOJF4K7JVgD0Ys4xnw9Jc_42iaBXwXrtsnlqPvOFzTuAltevXuc_snszszPDD9vkVpbpc_z2KutMa6QYbFBhKBD4zKwE-o-riitS-2_QvkYSTw-Je-6YLg5iQQIzKPAOyIog9-M5XuPSkNIuZRuYvTWAI8zolLsRKSSObTeqjPID_TfEY06FXuldQmyMcCTFFQeRAg2cvOv0skPn-1rU8xVzj15CSzWJrBxN-Y7g9Zk-Ewxz2KmtsJKbxLyZenBkThG8mlJPnCdnvwfUXeh7BENXXnLwlFIubHQwFNkt9POzY8EW-H6BrGuNkbP13wGVCdDc39ey9lM-lw9g-1demA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=Ze7tD4fCnqMTFFh1gzqSmPbtHtMLM-PgfhwT_UQ2VJseUzPEB70q9Ls2Cg80SRHp8KtgptE-GGJBFvItmHHRVFwmwSo3ZIu8EoqtnSvNI2vZelNcHpVzIG7eHMoLSn2E4D8kJGk_16Zf1B1odDEKQrLfXXHEcb_6BxxiKnqVlzkxdA6uoFvRZsclZuI0UWY56mbP7YTbaF_uk-E5BCEzbPJeYyvVy1AyJ2SkEKCGKVcvmhroLU3tUfogYqCGdaX-22NGKaO6rJKNYi7JW5yFCbiy1Rjm_Zlq9yP35WghC2jY383-NMUDZFvrweAGYxGX6pAUnCoePoPwCjESZcNeXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=Ze7tD4fCnqMTFFh1gzqSmPbtHtMLM-PgfhwT_UQ2VJseUzPEB70q9Ls2Cg80SRHp8KtgptE-GGJBFvItmHHRVFwmwSo3ZIu8EoqtnSvNI2vZelNcHpVzIG7eHMoLSn2E4D8kJGk_16Zf1B1odDEKQrLfXXHEcb_6BxxiKnqVlzkxdA6uoFvRZsclZuI0UWY56mbP7YTbaF_uk-E5BCEzbPJeYyvVy1AyJ2SkEKCGKVcvmhroLU3tUfogYqCGdaX-22NGKaO6rJKNYi7JW5yFCbiy1Rjm_Zlq9yP35WghC2jY383-NMUDZFvrweAGYxGX6pAUnCoePoPwCjESZcNeXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=NJV46TbsFEvmCD6gDosSjYVQvH4eD5NzjySXHcwDU0I7WXNdAl7f43IN01Kx__L3281bks0Ii5i7qj1cDkKhQWVQYHAYmSJfMMWYEFlkXYVHW2mdW20RFsoWGfacOPVcbGQNCn9CLWnFpr2Al6CngWWmXL89p8lPUnq_AJ-b1hoqGaKtlMJmIXNhhI_e5bbfjz59SpB1ZyDB0qgRHZcVZNCkVC64RfJzaLQyYoqgZ5KujQeFwJZvVU8y5qqBurmZ7bCfHWJTVHTqXM-uvjXnbXSjvRcQuN77FoGp5t21byTBoVt2AzsJQIKMNbu5sJtls5gIM8xwmCmt4fJry6pSNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=NJV46TbsFEvmCD6gDosSjYVQvH4eD5NzjySXHcwDU0I7WXNdAl7f43IN01Kx__L3281bks0Ii5i7qj1cDkKhQWVQYHAYmSJfMMWYEFlkXYVHW2mdW20RFsoWGfacOPVcbGQNCn9CLWnFpr2Al6CngWWmXL89p8lPUnq_AJ-b1hoqGaKtlMJmIXNhhI_e5bbfjz59SpB1ZyDB0qgRHZcVZNCkVC64RfJzaLQyYoqgZ5KujQeFwJZvVU8y5qqBurmZ7bCfHWJTVHTqXM-uvjXnbXSjvRcQuN77FoGp5t21byTBoVt2AzsJQIKMNbu5sJtls5gIM8xwmCmt4fJry6pSNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=BkdRZIRYGoGurVnySF4lRWvm7g0518ECwTEzeIhy5-50lnouLk84pCPsMtj_kO_oLMkHqiYgiah7sc5sXm3LbVgqEkIphVvZPrMXLoUmGCXzp317pWcsQy-1np35Nn9Id7iAfXcE09qAm6vZydvxJz0XtlatL2jZbEIF6DQWM03_2TkOGO--I3WuJfT4E8gnUW6pOtBMUp8zABXBa6VWG_pSrA5xXei-QrvoFA9g9n4JtN1_D5mnUnIofMq551vLo6YJy9GvNf1H-8-V1E_ocgLV3ZG41uuFGNMXG81_72J5ZW_Ls_I05iAUuhSEZ_Nqu5mz0BCs1-vH-jUuDQh6aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=BkdRZIRYGoGurVnySF4lRWvm7g0518ECwTEzeIhy5-50lnouLk84pCPsMtj_kO_oLMkHqiYgiah7sc5sXm3LbVgqEkIphVvZPrMXLoUmGCXzp317pWcsQy-1np35Nn9Id7iAfXcE09qAm6vZydvxJz0XtlatL2jZbEIF6DQWM03_2TkOGO--I3WuJfT4E8gnUW6pOtBMUp8zABXBa6VWG_pSrA5xXei-QrvoFA9g9n4JtN1_D5mnUnIofMq551vLo6YJy9GvNf1H-8-V1E_ocgLV3ZG41uuFGNMXG81_72J5ZW_Ls_I05iAUuhSEZ_Nqu5mz0BCs1-vH-jUuDQh6aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XclCWxkdos5FGNaW8WsxGlAZT3Mu5WZXI25LDBnsZLULrp1D6q6gAKUu2DQSL9oDW1jG3wAiwXp-kFjznlHnXc_MJ2hkIJVvDdN--eDiHzxzEo1TSeCiLxRTdZzm7NEOpZ8R1ichRbsRrl1EzxuMWgDtFB7NTQzmUoLPsz4JIZF6chsJS3xI7q5m3K0KFTs81PALoQfh0tCAo1mgrqXAUutCOY57nqn_AjWc3QyfbZB8gFkqh8Zp3zsWLCPiSsetdahwskYPGBPn8tbUTd_MW6kDzQbstbcdMlmkizK6G2SgCGJpVDjHEec_3l499W3RXJrAwAcHV7Nov3Ta4cWJHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=L9azNKgILXzRnNeiF6AOTGVJtlS86rYD0Jmj5IXFlCQt8MKYqnUMSOj2uYh18495NDtah3eFUX1D88Vfd7ehuIBXvBHA9IgYADyXWDTuw1KklMn5HIkK23285K99iBhtm9eA7sOfjm1chNUoxFuJOOBfarzorAWEAYHcouEnAVTUSP37dXs9tf1zFR5CR62eesywk0KdxpeU9cgnBe6NxewYq75qchPjo1LkABfD8K0UpjGVS6ensb8gCKNkABGp0ijvyk2QZg70xYkUge3ORImsn8R0VJ26XAP5pgtq9YLeYFXyUC2pWOe3bajbuJI4eLNmdv-bxLqCo9SAxuUZUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=L9azNKgILXzRnNeiF6AOTGVJtlS86rYD0Jmj5IXFlCQt8MKYqnUMSOj2uYh18495NDtah3eFUX1D88Vfd7ehuIBXvBHA9IgYADyXWDTuw1KklMn5HIkK23285K99iBhtm9eA7sOfjm1chNUoxFuJOOBfarzorAWEAYHcouEnAVTUSP37dXs9tf1zFR5CR62eesywk0KdxpeU9cgnBe6NxewYq75qchPjo1LkABfD8K0UpjGVS6ensb8gCKNkABGp0ijvyk2QZg70xYkUge3ORImsn8R0VJ26XAP5pgtq9YLeYFXyUC2pWOe3bajbuJI4eLNmdv-bxLqCo9SAxuUZUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-1rgdi2zfDrbubMZTCVDrYVfXdfB-Pvt6w4gWv3DJOPJOY2-3eyIeyCDtN-g3e_vhQLBnj2hAFXQEuVtZxMNJ1tml2lQkwehDiDAq_foNNINL66uhuo9ts-pUqhCA5SJ4a2OpT07P_ntoggyRxxglpJTKGNNva3Hz52espmbLyCgo_yks-MSeTvMVNF4xd_KMj8hMk3dqlLbU6UxU9QCRCtNTe87gYyXjxs-wFJUHOYNiiPyiPb_wOQdyVZf_p6K3_8-SlKAZ55_uAQR_-oZLEaTAS0iamF6Urd58xFJ7yR-XLnCFIaFaJiFGbfvCdKV_pZUnN4cVwklsBknZI2OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
