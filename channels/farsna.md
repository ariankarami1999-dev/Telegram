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
<img src="https://cdn4.telesco.pe/file/PHTd81e0rJiS0rXjwkceDNqMOFRh0KxCOibq-MqnJoFX-brIVRgCYyqXhn8Libw4eWjvUyqsmoYV3O2GYZEseY7zxTJmf9voCtFPSKkJ3u1HJBkLGViPY4Lxgzd6520_7wjOB_dA12rW05s63cmjUM73YuE8bxgZZPdm-AFkGKpoGazUDU3XFvvZkK--H7g7A8-z6I83kNG7CmVoIF4U-wmtulQ_kbZhrE0xHJfTECf5KRu41OfZBNQqKr8TBE6HnHUkmLheEi_QodHGETRuhhsU6MxiOAjfIejsPjWimtLPvIN0vdcWYD_p7gow-F_6I_PZUI9rIg2eUBNWUWqj8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 17:59:56</div>
<hr>

<div class="tg-post" id="msg-444292">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_LM4cSrXQ2qWUJYJ3S4FryuFWTyhnqxloHqHAdYQoA3Cr_LTfF6DUJlbOdtSObOuhBROveBa1NywDZA0khrdcD0JGVr2D8YLmyu1tlvrWOeZZHGu-xRLGqrlzZI3deQ6gnZNXIBGbQJp0g0ZiS6034Dr9TxeNnfI__TTrhywb0bgLGZFuoUjIs75GdlnmSNAJ4UpqGAy9xUy9GPOAVZDMZfMZ-GEdenDlNwAUkS64pQ-hjWP2EvriItl5eyVsXuRfbld7lya5Iscu4-AlyaplV7j5OUpulZqH4SmePlaDe57a--7BLyUQ1tcv3V8dbBtX7GL38u-7I33a7__KqMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جریان سوخت‌گیری در پمپ‌بنزین‌های تهران عادی است
🔹
پس از اختلالات ایجادشده در شبکۀ بانکی و پرداخت موقت هزینۀ سوخت‌گیری به‌صورت نقدی، فرآیند عرضه بنزین در جایگاه‌های تهران به حالت عادی بازگشت. @Farsna - Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/444292" target="_blank">📅 18:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444291">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d0b10e2d.mp4?token=HjpQCgt5yYyoyZYWCjWzAmZ-9FixCtZeGmZoQC1-YERbP4ZZ9pjqFU2GMiWaTDkRDzUMI-VK5qo-fxlF8DrsUwT4Ezup-fWITMDoKsN9DcYulc7wTucTa4AKYef1k6YMcZRWyjxL4em4Wz9ihQF03QmxIqSh7tF0HaXh61D84M6VTLM-w_YShiOWxwnyXOHUma6OKJ2xc9RtvSMaDsmxCeJW246i-rS_8knC-ib6KUETm10XgUjgf9XEprYAgfGWNclSkOe026yCm2Q8I-KjHcbd4G9HXu21HwALlustnNqiTH702ngGjUaCvrRWoricKm9rd7UV0azykR-JYf_8vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d0b10e2d.mp4?token=HjpQCgt5yYyoyZYWCjWzAmZ-9FixCtZeGmZoQC1-YERbP4ZZ9pjqFU2GMiWaTDkRDzUMI-VK5qo-fxlF8DrsUwT4Ezup-fWITMDoKsN9DcYulc7wTucTa4AKYef1k6YMcZRWyjxL4em4Wz9ihQF03QmxIqSh7tF0HaXh61D84M6VTLM-w_YShiOWxwnyXOHUma6OKJ2xc9RtvSMaDsmxCeJW246i-rS_8knC-ib6KUETm10XgUjgf9XEprYAgfGWNclSkOe026yCm2Q8I-KjHcbd4G9HXu21HwALlustnNqiTH702ngGjUaCvrRWoricKm9rd7UV0azykR-JYf_8vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدرسهٔ میناب امروز به میعادگاه آزادگان جهان تبدیل شده است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 232 · <a href="https://t.me/farsna/444291" target="_blank">📅 18:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444286">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzi6xcjapTh0jYwBEKNkcv1m4yVxWSAqNjwENwQAMbVwxvZrY49fZKK0FPz1uqMIr4xjHK5DBBXXuBE92FyxswsOLWTF42Riv_30GZ2HKE5m5OF1izc36auenLJJlksPEU1nTRCDq1PnwHDiq4u_ItQYKSqTj7VbVDfylkoZ6bW-litVwnbz6s2eA7hPoXdUDzUKgHLGb6t9dYtUrdH0pqwS9SwpOPiI4JuoXKh1aTV844vkF15R4PFj9Z7Do5CSTgswtc7uzwwQCJoaZsRZTGrb-LE__50TUOkLUQtyo1qB_3f4a9k3L-We_IGQUWhphZx5FHjqA5jqokPlp1hyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4f1l5OOzQiGuXZTESCq6Tjpu5CBImPzpi2ytT3gSwh0V7eFgAK8_TCZD80xr490r-iY0j-NaFM3Xb6kkG4OvXOLGIvPw7j1sJFS9kYQt9diebvY_C_bHRdLmfD3cXLjLLSGwZcu6nSdIhUt3wWnnPeFIaH0DCZZymMt__BKi3DeO3UoLCHr0-ajQ7erfqgm99CPdhQO0nHxeqgTRMZKhqdz7I8f6tuyVOSkMp1ZMcrZmOcRcbnu4-84Zosl3-pVUwOihWTwarZNdenjhFs9c-pGbI8ubbdFbULeC20H4n0dFFol64G2pB8QopZCkXRER9S7Ju_c06rmi4uLsfpqEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivcri7QMOhlBKJInb0MZU5vg57KVHekE-p4S6uQh8uKzuNhq2ajyX3w8Q1BH3RXTbZr6WNp8MoLC5bCpIouObS40hbPO-KzWNSqhxVL2qKez4Og3cBNFLTMkWR5qeY21ikMWkj4vAGFabZ4kYaVnMahSfeW8TtwnbpiieSYcOIQIKVcuP4hJLgNWMazB2Rs0Qe0s3vo5ZNA1imNe4u4NyFhWC31s-joYKkdVeIGwCAPyRo1weWbeMt8JdCbocz-npTSw5Aw34As3DLl-zo0j7erpDJCnuSa9Xc1eK9WNqh4BdkPtf3ZNbadv3rObHSzUf0gaVIphvWInuhqHJzDJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QL2r7BLtNIs0uQSCWGsiGcfBaa8mooXdrDetjRFRbDh5IS_HQQCCAFbZtiNAAgXFMDs-hNQm6J3oyApL7i4ypP21PSHmMi6BMEKs7214RVMRaaZssoQS5cN5fJWRfkmoBq9kob_ziJSFMOMRfcTqiR9-C07yBE2QxIdfs8YvFi0n4qtuMuV8taZZxLpUX-JNeONqDOZZFxdcaloGSp5iyfnyU7t92NjADyDhp9LBZ0Pmkrb4XyOUZeXBZ8t4Ye4WxYzCgy8BgPX28h5YlY2fL8l2Hf6IJn7zamG0qmKXWax7FxzaSBEbnzDPm-Cu-AzucYGcifb5yhw010wvENOkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFzDQ0Dnmg6xGthK3UFgF9YheaU8zvh29RsZ1sFkV1nCHswJN44C5bgCU1_5CknulHscMARHbigXfhIQWKoK4fBje4ZvYsHHfuqBAF5nL3eIFTWW8q5bcdnfgdtud2euTqdptTf__X46p9XTkh1pMBQJzrl64Hub8Ig0pEKSAC2JpJpAsj_v2Bzk4aLAJC3GR_B4FoVz6y3KhArX5DR__FoSMJc5HnAoJEuM8pkAd1NaVb32ntMlqZYw-Sh82_kSIMLmbO7ss4SoM_7c9UzWIG4R9jhk0T3qgqlkYR7Zbgx3J3-mtDlXKkttTYIqW33jj8NOiiy0pUXs9oi72UGsxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دشت آزادگان غرق در عطر عباس(ع) شد
🔹
مراسم یوم‌العباس(ع) با حضور پرشور مردم دشت آزادگان، جلوه‌ای از ارادت دیرین خوزستانی‌ها به علمدار کربلا را به نمایش گذاشت.
عکس: میثم گمراوی
@Farsna</div>
<div class="tg-footer">👁️ 549 · <a href="https://t.me/farsna/444286" target="_blank">📅 17:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444285">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82297da050.mp4?token=tiQy5M5nk1weW0LSJkz-diH9or7ErY0wyQOrEHZYYlb6uMOW6wN2-z10kxR6Nt4JPs3wbczpVBh26SPk9wBArL1evUrOO32Ntza0gQvLefHksdlhFK5GZqz7MidWN4wOKol-2gNTIxO3p2WZDl2LQTjqDXzXH-fZQhEkFDdlsS5FUY8j2cm7x2WvLiQwoi5J7F-EGG-sWd5uh6mxIEXJFAhj9PAT7-JIT3NIre4Pcr3gHkI_a30wedGoBSeNHTguU6vFXdluE8WYnQJRZnrGNGH2_P4NoOCOxBwrtDcdP2WHJJgeE0qihYbCuIQPAk2CujeWEHoeL6wjsfeyr58Qcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82297da050.mp4?token=tiQy5M5nk1weW0LSJkz-diH9or7ErY0wyQOrEHZYYlb6uMOW6wN2-z10kxR6Nt4JPs3wbczpVBh26SPk9wBArL1evUrOO32Ntza0gQvLefHksdlhFK5GZqz7MidWN4wOKol-2gNTIxO3p2WZDl2LQTjqDXzXH-fZQhEkFDdlsS5FUY8j2cm7x2WvLiQwoi5J7F-EGG-sWd5uh6mxIEXJFAhj9PAT7-JIT3NIre4Pcr3gHkI_a30wedGoBSeNHTguU6vFXdluE8WYnQJRZnrGNGH2_P4NoOCOxBwrtDcdP2WHJJgeE0qihYbCuIQPAk2CujeWEHoeL6wjsfeyr58Qcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ اختلالات گسترده به بانک‌ها برگشت
🔹
در ادامهٔ اختلالات ایجادشده در شبکهٔ پرداخت کشور، امروز هم گزارش‌هایی از بروز مشکل در خدمات کارتی و موبایلی چند بانک بزرگ از جمله ملی، تجارت، صادرات و ملت از سوی مشتریان این بانک‌ها اعلام شده است.
🔹
پیگیری خبرنگار فارس…</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farsna/444285" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444284">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VbRNBzkf2qq3gdmIQQ7UaHcvgg9bWf_fENVKteZJhabf7zZTJumw3eD94BlyV4H7403o9ZvFNdc4SxyONID_odEEE61cplnbGQmz5Z1HvWae_eyC-SK034dIZf4VZALpA4Nxdt8w9oGmxcuiLvgy_XaKd5n59hC8hutyvkL74LaXPZo1PEZmpDiTXuQ1qnFGOgrAGGA0pfMETGDOo5Aewaw1cSt7gqCNKO9NAcYLRnEj0nQ5sPXPtjvhutJUfIyfQuXZsOvyAc0NPXURIRl4I1eSG4BDz29g7phLmFt_29J7Cce1RBdvsBv5ljk5jIhx8JMcT1qRDQyeEOpm4CDbrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرایط پیش‌فروش خودروی آریای سایپا اعلام شد
🔸
مبلغ پیش‌پرداخت: ۱ میلیارد و ۷۴ میلیون و ۷۸۷ هزار تومان
🔸
زمان تحویل: از تیر تا پایان مهر ۱۴۰۶
🔸
سود مشارکت: ۲۰.۵ درصد
🔹
ثبت‌نام از ساعت ۱۰ صبح روز یکشنبه ۷ تیرماه در سامانۀ
saipa.iranecar.com
آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/farsna/444284" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444283">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🎥
حسینیه‌ای در تهران که ۲ قرن چراغ روضه‌اش روشن مانده
🔸
حسینیهٔ سادات اخوی با قدمت حدود ۲۰۰ سال یکی از اولین و قدیمی‌ترین تکایای تهران است که توسط حاج سید ابراهیم تقوی معروف به «اخوی» در زمان فتحعلی شاه قاجار  احداث شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/farsna/444283" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444282">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رژیم صهیونیستی بار دیگر آتش‌بس لبنان را نقض کرد
🔹
یدیعوت آحارانوت به نقل از ارتش اسرائیل خبر داد که رژیم صهیونیستی امروز برای دومین بار آتش‌بس را نقض کرده است.
🔹
طبق این گزارش، سخنگوی ارتش اسرائیل اعلام کرد که نظامیان صهیونیست اقدام به تیراندازی علیه یک بولدوزر و یک موتورسیکلت در ارتفاعات علی الطاهر کرده‌اند.
🔸
ساعتی پیش ارتش اشغالگر از نقض مجدد آتش‌بس و تیراندازی در جنوب لبنان خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/farsna/444282" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444281">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-fnBf4I_MxtGimcIB3BCkptBZk8qsyZev5oycq12OrurLTkEteIvjt7fu4yPxGGu5Rs6vVrAit3Ab2kVmg1bSAb4aF5vcrn-bY5DDSfopJkqzOx8YElRSJpjZLELCMcziK10eK3beqExD2wWkhpDUl8f6J6AA1QBfw3QhaMlhFnCoQhFWOJqCX8FoZQTL4M1T16BujWJgYHxDk9U8QqGDw1e_kiE2mZ6cMqmxrT-aWeJZdl9RA4PLr1ocRuj4AOxfBo2PGASEBk7-wVJM4SyjoG21QHt00Qpw91Dos9cXUDnPePxnxbauZUAG0pGrtOfya9uvHJUUUa9nw-9xur0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ بازیکن تیم ملی در آستانهٔ محرومیت
🔹
احسان حاج صفی و سعید عزت‌اللهی به ترتیب مقابل نیوزیلند و بلژیک با کارت زرد داور مواجه شدند.
🔹
اگر این اتفاق برای آنها در بازی پیش‌رو تکرار شود و ایران به مرحلهٔ بعدی راه یابد، در بازی یک شانزدهم نهایی غایب خواهند بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/444281" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444280">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f3309b0c.mp4?token=NRcUUWBAUqz9v5Vw6XKPT69VU7X9rxyJTDlTqSUV5tagHANSWWJbshouaKHquwIqrYE1q_RkCIzVxopzFwb1hHGh7iIal4NAvfcwUGa7PqL6Q3W3Ysg9ihxJiNdCTx00y3yK9TtjuhkICjOpMkD5JasfBjb3-gokU7DQqlKLubcFTAGHrWEJojWOO-9_UNvZbxTAJKvnFASD12X6J7KJinRD37HYzKUjPT3vHPhwq02LSj1-vN-rWxYWKPm5z-9ks0psKfuubv-msyz5qBhvD_AAkertQ3sbbsVpnRALb7wVimmge1ybMNjx2M7Dh8m2fDqr3Qf4z1STKWFMqmFLdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f3309b0c.mp4?token=NRcUUWBAUqz9v5Vw6XKPT69VU7X9rxyJTDlTqSUV5tagHANSWWJbshouaKHquwIqrYE1q_RkCIzVxopzFwb1hHGh7iIal4NAvfcwUGa7PqL6Q3W3Ysg9ihxJiNdCTx00y3yK9TtjuhkICjOpMkD5JasfBjb3-gokU7DQqlKLubcFTAGHrWEJojWOO-9_UNvZbxTAJKvnFASD12X6J7KJinRD37HYzKUjPT3vHPhwq02LSj1-vN-rWxYWKPm5z-9ks0psKfuubv-msyz5qBhvD_AAkertQ3sbbsVpnRALb7wVimmge1ybMNjx2M7Dh8m2fDqr3Qf4z1STKWFMqmFLdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواپیمای پزشکیان با اسکورت ۶ جنگندۀ ارتش پاکستان به اسلام‌آباد رفت  @Farsna</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/farsna/444280" target="_blank">📅 17:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444279">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e10d465c1.mp4?token=CKkPkbkv6651Nctp8sFBOm6LOOUO0upgC6OwpfzQJFsb7X3sfffy8VnSM-MmT9DHyRhl63GXK8vyIUTrZ1-t7OvsP7Nw91lhw7zMEqmtb_k8M5CwiZHo0obm178zSmFeMWiqMvnha9H33eSCyYmGuL7LIOmRjlBcLJ8N-BGthJc3GXpQQrbX8IZXINkvhWfIhloKmBrIrxzqdo3WsTf90ZKe7XVMdQFBA2DTD7jMdmxpNOcBEbcyXaaBCA7ooBfDIs72fdsHjX1hBm7V_swW5IPEg-TQnGEbB6rAJgQ9chKu9A1rtzu1zt6zk60cjZs638fRRCpZHHcNP-FP6vq6Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e10d465c1.mp4?token=CKkPkbkv6651Nctp8sFBOm6LOOUO0upgC6OwpfzQJFsb7X3sfffy8VnSM-MmT9DHyRhl63GXK8vyIUTrZ1-t7OvsP7Nw91lhw7zMEqmtb_k8M5CwiZHo0obm178zSmFeMWiqMvnha9H33eSCyYmGuL7LIOmRjlBcLJ8N-BGthJc3GXpQQrbX8IZXINkvhWfIhloKmBrIrxzqdo3WsTf90ZKe7XVMdQFBA2DTD7jMdmxpNOcBEbcyXaaBCA7ooBfDIs72fdsHjX1hBm7V_swW5IPEg-TQnGEbB6rAJgQ9chKu9A1rtzu1zt6zk60cjZs638fRRCpZHHcNP-FP6vq6Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم باشکوه یوم‌العباس در زنجان
🔸
حسینیۀ اعظم زنجان در جریان جنگ اخیر هدف حملۀ آمریکا و رژیم صهیونیستی قرار گرفته بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/444279" target="_blank">📅 17:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444273">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHThmRnDHYdL8su-jPeEsqKKMAjO6YZPWGcBsFKhE-X9MA_mYYH8RQOcVbuYLKzcvUnY4EHUwTKmXgsC0vm-dD-eG1dbfJVlNNS_MTJuvpTzwRsZlUYxpv8Dv-SBOPURUFH7YwYa6dCyJn2bcXvsksXSxmi67FVf19t56f9_nz39V9SYROLHW1uH7m_8EYtDaXVli_gxf0_0h1B-rxH-sqMVsrbYKxmfaT1gwstY9YccTxsJ178orkOMIkEjnRYx0SLcURU74vD0bBcMdTIDAnkON76DQG6QjtPyHiQyPqpg7RNjSBZ8JrZhzJqh1TetPi5B7-Eg0Fjg16VWKIz3hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jayetwU7BDA54v9HeSB8eL-8Yy7HfGy1Un7kXDzMbVNPGs2k6JK2YNIhhPS__ORWhC5KcdOiEQLDjZ6ndROOFUo4D5IQiY0OyuzrXhSJy_pNERFc3NvBCnhBMGatN988YKQpqD4RWUic-Gp6SqmkLnNm0sHtfSADIfxjtHLCW5JRLh8jSxQgxDMAAoLX4XsySUHOQpMAJyi8_gSoFEvs1VHtP2SbvfL9rhrD_oqxsdvDPmZ-k_VruY7NHoZ7o8MpZufBLehqhN889ImnqYT86qf51sRY9aRKcL1MOcL1ttBdPOyx8-yNVSevujpAccHP_7e0YdK7ej-fhYaCDHjS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LhSUrM7NOJX8wljIYURBWQDtlX6uImdY56GnrbXXP94IE9jt93SQupYigidnLFSt_wTqa3MCsDymf7tHNq5O8U4wAaDdyvyZjqYPK8q6IUX2JYo1Gc3aplWPim7hAYa-b3wqeLMGqK-uu8haaBuVHTMXE23bDfqt8XGyINVIHfqlrjVgBDgy9Br_dE1I5yLprPA7K5C83AyaoStvvZkGHljSzqv8CtOTwW4b0GFtEWP-4oiQLQWFqZ8wpE3gOruFv06sgiVNqdkbkKtzNYQ4X0aNyTQnCDwY8cEdVnVmuKlLRRBw0MZpjbBk1ojiXmGdl2Jnq5SS1yOVTmnegR-OeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lwA_Hzn-9dls05H8bEyrjNxmab9udlxBL6GPMb6k6KeujRtLH3nfxi3cXB4mMTXSlwTPoUech0kVB0XSu3dSNgbjaRrYgPy2BqPkc5at-8Z4BoVRFpSofafgrhbLr3V1AVLganNA3aqoq79lHkQMxy1BhE3N3m3JMibK9pFB2nRbwe6OVsKHpxsCBu9-LjPk_w_L6PHEM4EH4Nf0JSEFvgqw6Ymz7QloSjL2j0Yb6cqqKSQWJSO3uauOmy959aSYIaIVxsOKpcWu_DQ0Gd3r1q-1XBgnk5twUAuB4xnC6OHec_sZfix6O8xm6lrCQv1bAlR7aZ8N0pYXXs4TYa-Thg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuNHZOqZphE1m4ipp_lQJF2mkdQnjX5IyAPw4kn_A-LuSF-KVt3Z4JFkFa5L6ZY7d-BHXnHoskiCfUKarCdPnNgbiP4jaeHtSRsleJJNn_sd_e3kXFr-vdQQdDntLPmR5aXLirx8xrmmkTBnEALhSM4BgH-pmX61IUNPYiWLyqhdNIDnfIUQUWXayOZECAB_D1HC9yHI0c7Royfcx-GKELRtcjwdwNP67Ar3Bci8HqcMVM3-OChsEoZxMnv23kG4zUy5H6_2L-jHmyqPOJsYdxDh0Mtut12OuYSEWwaf8GbADjmK0XihgPyYSPCjhoifjRnz4pQKJz6VQ28L0VbLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NK1-gYWFA4qRlLZq0NnKvduQxAjBHj52xyGNZVUxZSsviu2VG9dayMKmoKcrLAqlo6TLf38ucjgCKaIDYRuNDGa4_bNURV16aeXletBldz-5kGcnKBshbKE32z3S98XjZMcStAhNcnZSePYAc34tsTLLcxsn8Le-bFyfBXYGZvKkKdvae1qq292cLb6-Hp70A5SBmT7362mgDBQeC88GgrL8amkAU9pSGYHKzAi-n7VNiyRTBNsHzGoUXcyt_NagcLiZ15dv25wCWtu6BpuqmApC-Q1GCTkgGFiHO0Am_Gkz1lRwg5zABLUBKVxa-_J86coq3BAlgkjs_4Dqd0G73g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری زیر سقف‌های قاجاری
🔸
حسینیۀ امینی‌ها با بیش از ۱۸۰ سال قدمت، این روزها صحنۀ برگزاری آیین‌های سنتی محرم است.
عکس:
میثم ملکی
@Farsna</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/444273" target="_blank">📅 16:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444272">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس پلاس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJl3EkHhq-Iqw5M2DviQWAveO61h345RuxjHwS_FlUDD5S5LTbc2uzL33Fhqwp-aTdnhCTc5Cc4EryRgOpkxZaUOxBifwjJ1jrFfM49rg0rUbdyv43d0k1oV0XVsyhQ3eWmI773c_6njtuejZaFOrP2gb_s1iXUTaC-UFNTAmsHqcmsy-C0yvgv_CUXfitj656aL2AW2tPa9pjFKCSfqy51sSuhv0mHXnj81RYW_3BUaZmSKoypSkeCIwaoyhTUSP0ABfPyTvfeoLpg5qdUKvRQDajgDvbrh0anaLA2Zu-3RQ28u6o5s3Nj8PY5W32JohOJX9EwJe8ExGjF-9O0XeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تصویری از مشتِ گره‌کرده شهید تنگسیری در لحظه شهادت
استوری فرزند شهید تنگسیری در شب تاسوعای حسینی
@Fars_plus
-
Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/444272" target="_blank">📅 16:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444271">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrmYs1B-_YYcIFZ94r1nrH1x55WEnklqgYpM9E9nsl2Z-JpAcj5-LPcQLWYB772cM9nXAEpSWZqX9mwDTAXfN9MJh2mVUp4pfoJ5YWkc2xs87Q2VEO6zwTrSyRLx2i6mq9YWFOcZwl7Fo_ptjZ55BYfCNVmwLeLTpKf-Jq2wSqD_-7h8s0uaUJm9nQuxKI1m3NNmsHX3OOZRecMpsnlT-VsJgXi65LuX7C_pmJBKiVwjXLdPumUUV7jLsRRItuF8E-2EKxwK8VSI1Y7Y5L5Ug3BwpnoY0rWkYQ-ZYufhn2NfU9FFfS9xQWmJXrYi3VZ-UTdRZl_7uhhIRz9LC_HlRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران و مصر با سوت داور فینال جام جهانی
🔹
با اعلام فیفا، سیمون مارسینیاک لهستانی قضاوت دیدار ایران مقابل مصر در دور سوم مرحلهٔ گروهی جام جهانی ۲۰۲۶ را قضاوت خواهد کرد.
🔸
این داور فینال جام جهانی ۲۰۲۲ بین آرژانتین و فرانسه را سوت زده است‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/444271" target="_blank">📅 16:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444270">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcc9eacfb2.mp4?token=JauDC5JVqOt-2JE54saEiAAvwhR9MSiAPyOrbR28mV-1E8qDLzIliGsnKIvMMQgPJuD7Cjxu-iUoi25KNCaTM71lvn39DozEM2JyDscR8kkdYgtu0dkematMP9DHIZ3OZNe9pHHDbzmPvDGA1Ohp9Wo6g0t4BS3HZLzVHDY-cMu71yEDJsWuy4I802-XDNtkPFMPAlw7q48upyUtyva1jiFvS-UW6l_XEHnvjSLe5AW3CGgKh5Cgdw83MZ64OXqw4__EsQhINkRyVL7U1CMs6uIyVGIcgoboIo8Tecq4pFDxNsX6mUVmptUcHae4BibpXIyXYD1_iXcPYMbWc9oCSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcc9eacfb2.mp4?token=JauDC5JVqOt-2JE54saEiAAvwhR9MSiAPyOrbR28mV-1E8qDLzIliGsnKIvMMQgPJuD7Cjxu-iUoi25KNCaTM71lvn39DozEM2JyDscR8kkdYgtu0dkematMP9DHIZ3OZNe9pHHDbzmPvDGA1Ohp9Wo6g0t4BS3HZLzVHDY-cMu71yEDJsWuy4I802-XDNtkPFMPAlw7q48upyUtyva1jiFvS-UW6l_XEHnvjSLe5AW3CGgKh5Cgdw83MZ64OXqw4__EsQhINkRyVL7U1CMs6uIyVGIcgoboIo8Tecq4pFDxNsX6mUVmptUcHae4BibpXIyXYD1_iXcPYMbWc9oCSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در ارتفاعات «کوهمره سرخی» در شیراز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farsna/444270" target="_blank">📅 16:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444269">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🔴
انفجار در سلیمانیه عراق
🔹
منابع خبری گزارش دادند صدای چند انفجار در سلیمانیه عراق شنیده شده است.
🔹
هنوز علت انفجار ها مشخص نیست.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/444269" target="_blank">📅 16:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444268">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caecdbf25f.mp4?token=gsbn4Dg78ANEf3xbN0yL2ogL3HpDK5KE8gVqx9N3gWBbXj3EPVW3q4X-21bVORL2w3gs2oTeRKh-yOG8x9W_XDv2esdP68fU1YQ05g_-Rso9_KarYngs8SktwADvX5YCmL3MGMF1zjlFAYFaF4VRAtNhmrMUlo3GW7PxFOfkxzVrlyWd8VYDodF4nm1uBnvmUh14yMNcqkiBcnnL9Jj0uqT5I3pzKEnfodo6N9tajIqR37fzCQcwdR1zG41LQ1gP1BwEsCcMgLFKMUgTzJiA31V721X7vjh9U9_GBYuN1Lmx3TLQjPMEeniF8SGSY158Q3EvTV-SB9UzBbWuvLPPug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caecdbf25f.mp4?token=gsbn4Dg78ANEf3xbN0yL2ogL3HpDK5KE8gVqx9N3gWBbXj3EPVW3q4X-21bVORL2w3gs2oTeRKh-yOG8x9W_XDv2esdP68fU1YQ05g_-Rso9_KarYngs8SktwADvX5YCmL3MGMF1zjlFAYFaF4VRAtNhmrMUlo3GW7PxFOfkxzVrlyWd8VYDodF4nm1uBnvmUh14yMNcqkiBcnnL9Jj0uqT5I3pzKEnfodo6N9tajIqR37fzCQcwdR1zG41LQ1gP1BwEsCcMgLFKMUgTzJiA31V721X7vjh9U9_GBYuN1Lmx3TLQjPMEeniF8SGSY158Q3EvTV-SB9UzBbWuvLPPug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آزادراه شهید شوشتری چطور شرق تهران را از ترافیک نجات می‌دهد؟
🔹
رئیس کمیته عمران شورای شهر تهران: آزادراه شهید شوشتری که به بزرگراه شهید یاسینی منتهی می‌شود، می‌تواند حدود ۳۰ درصد از ترافیک بزرگراه بسیج و بخشی از بار ترافیکی شرق تهران را کاهش دهد.
🔹
پس‌از…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/444268" target="_blank">📅 16:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444267">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5af1d6630.mp4?token=PQlOw3S6QWWiWh236m5P003WI_BK9gXv250LG2Ey2Uia3CjfaFs4_r48vltGI23afWmN9DrDIiG8hZF3ZlR4Kf6Smr1bWZagS9GTWLARrHDAsSTedAi88PFm2QRIEk6oJ_YN77AXehyP6-FfGewrIxU4v8SSbM1NxPtBB16V-lAg618zhj64akhWxxeOqRCYax1r1n_NT2xlvvtsUrWrc_RE3xjime2ruThTIxaMkgPOa_GcorceNe_YpycEWnFRDy18oMg4U3ki72GIcRAwNELdPKgGkSi8A5lqEz2eXwuFIVljDC5IZ5wveM-D5NZkEUJaaqkxsrprC-aEZdM7cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5af1d6630.mp4?token=PQlOw3S6QWWiWh236m5P003WI_BK9gXv250LG2Ey2Uia3CjfaFs4_r48vltGI23afWmN9DrDIiG8hZF3ZlR4Kf6Smr1bWZagS9GTWLARrHDAsSTedAi88PFm2QRIEk6oJ_YN77AXehyP6-FfGewrIxU4v8SSbM1NxPtBB16V-lAg618zhj64akhWxxeOqRCYax1r1n_NT2xlvvtsUrWrc_RE3xjime2ruThTIxaMkgPOa_GcorceNe_YpycEWnFRDy18oMg4U3ki72GIcRAwNELdPKgGkSi8A5lqEz2eXwuFIVljDC5IZ5wveM-D5NZkEUJaaqkxsrprC-aEZdM7cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقایسۀ رفتار آمریکا با دنیا و ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/444267" target="_blank">📅 16:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444266">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfco_D_SfJnW-2AVNkpZun3YxPuXNRC9nfHWfoj5QLNmchUAPBZ5ryFeWtHHxcEoFIS9vCBO_sjX7DM0I1AqL5Gowxkyre5XJWNtQUPdBydqXm-z9s3HBe2GVsyKjPqmyYiN6eu5uylfgcy-UyI1JnmRsR22jp99T1IQsp4_zwQLpEpFrBEmpfZs_m3Pz-G43jlZUI61P_bq4ywApULh5HfhNWpvzmUTIngaXrh9Lltf4NX0YYT3YVzh6WvR8lHe8C2b7iOQux8pJA7On4TXhgBgZfcZ3bUecUemIhZLabnsHbTtQuDMnvWOMj56lkrvyzwkJDK96FL4v7WLJKy69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعاهای جدید ترامپ در مورد مذاکرات
🔹
ترامپ ادعا کرد که علی‌رغم تکذیبیه‌ها و بیانیه‌های رسمی، ایران به‌طور کامل با بالاترین سطح از بازرسی‌های هسته‌ای برای آینده‌ای نامحدود موافقت کرده است.
🔹
او مدعی شد که این تعهد، ضامن «صداقت هسته‌ای» ایران خواهد بود و درصورت عدم پذیرش آن، مذاکرات ادامه نمی‌یافت.
🔹
ترامپ در ادامهٔ اظهارات خود مدعی شد که براساس این امتیازات و دیگر توافقات، موافقت کرده است تا تنگه هرمز باز بماند و محاصرهٔ دریایی بیشتری اعمال نشود.
🔹
ترامپ همچنین مدعی شد دارایی‌هایی که آمریکا آزاد می‌کند، به یک حساب امانی تحت کنترل مطلق آمریکا واریز خواهد شد تا منحصراً برای خرید اقلام کشاورزی مانند ذرت، گندم و سویا از کشاورزان آمریکایی و تجهیزات پزشکی مصرف شود. سخنگوی وزارت خارجه و رئیس بانک مرکزی پیش از این صراحتاً این ادعا را تکذیب کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/444266" target="_blank">📅 16:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444265">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6739fc2cb5.mp4?token=Rdpsap4NJH-9rD7OoPqNHxMnITrAdJpXlbMQCDUnqao8Lg2AwtMF2c9T077tBGOKzX06InYTMsT1D4oEIfpT5V6lpZ7omf3TaWND0gor2NnhWYWHNFKBcFRsDIe7dGOnsf73jdHCxOTpoA8nu3WLLNN7nDmGPIiaXZd47gW852wC5oTypKurxBdv6YKctYQM4UftEBiC4Z0pxStd3YyvboBdD8OIz4NHSBMRTeo_l5U380xH-koDrwmpuca4q-0xdF2dqSQaTKEB_CwGCcjLHloKU0h3yDmSUP916dj5RKlbow7R2Lef3r_SR6T2T4en0dfePR9PhuLOYLYuaLrWVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6739fc2cb5.mp4?token=Rdpsap4NJH-9rD7OoPqNHxMnITrAdJpXlbMQCDUnqao8Lg2AwtMF2c9T077tBGOKzX06InYTMsT1D4oEIfpT5V6lpZ7omf3TaWND0gor2NnhWYWHNFKBcFRsDIe7dGOnsf73jdHCxOTpoA8nu3WLLNN7nDmGPIiaXZd47gW852wC5oTypKurxBdv6YKctYQM4UftEBiC4Z0pxStd3YyvboBdD8OIz4NHSBMRTeo_l5U380xH-koDrwmpuca4q-0xdF2dqSQaTKEB_CwGCcjLHloKU0h3yDmSUP916dj5RKlbow7R2Lef3r_SR6T2T4en0dfePR9PhuLOYLYuaLrWVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان وارد اسلام‌آباد شد
🔹
رئیس‌جمهور در بدو ورود با نخست‌وزیر پاکستان دیدار کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/444265" target="_blank">📅 15:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444264">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1nwFdJyo-_mn8waQdoH8BIwFeKztB7kiR624EZh9TOhNggHnrPld8V06f-IdtS8kRgub5S20Vluc5P2MuloiBWlffxZB13GE5lj8iAX557gRKRgzPjI172ekmV5WVkL8StE8wwiHhyB1iDof5cdQPnPqWBqb8juti-8mpIzZK2x91egaEVXi8bRAKLf8fd-8gOg58DITKqdFZX-Hb0Vh0x7HMAKkaOYShLLglewLfdhvXi8-Jd2xVpVqT0IrfxhPb4fRh-nXhPOQNCbYDZpdrSk6tzCphTKoSkrUBKTPBCtQh1s5DgW71DnPINm1Qi3_Cw3ATKMsFKcb28kFkp6mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اعلام تعطیلی چند استان در روزهای برگزاری مراسم وداع و تشییع رهبر شهید انقلاب
🔹
براساس اعلام معاون اول رئیس‌جمهور، استان تهران در روزهای ۱۳ و ۱۴ تیر و کل کشور در روز ۱۵ تیر تعطیل خواهد بود.
🔹
همچنین استان قم در ۱۶ تیر و استان خراسان رضوی در ۱۸ تیر تعطیل اعلام…</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/444264" target="_blank">📅 15:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444263">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
ادعای شهباز شریف درباره مذاکرات موشکی ایران و آمریکا ناشی از بی‌اطلاعی است
🔹
اظهارات امروز نخست‌وزیر پاکستان، درباره اینکه در دور آینده مذاکرات تهران-واشنگتن علاوه‌بر موضوع هسته‌ای، دربارۀ موشک‌های بالستیک نیز گفت‌وگو خواهد شد، کاملاً اشتباه و احتمالا ناشی…</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/444263" target="_blank">📅 15:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444262">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
ادعای شهباز شریف درباره مذاکرات موشکی ایران و آمریکا ناشی از بی‌اطلاعی است
🔹
اظهارات امروز نخست‌وزیر پاکستان، درباره اینکه در دور آینده مذاکرات تهران-واشنگتن علاوه‌بر موضوع هسته‌ای، دربارۀ موشک‌های بالستیک نیز گفت‌وگو خواهد شد، کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است.
🔹
بنا بر این گزارش، مسؤلان تیم مذاکره‌کننده ایرانی تأکید کرده‌اند که موضوع موشک‌ها اساساً در دستور کار مذاکرات قرار ندارد و متن منتشرشده یادداشت تفاهم‌‌ نیز به‌وضوح نشان می‌دهد که چنین محورهایی در دستور کار نیست.
🔹
شنیده‌های خبرنگار فارس حاکی از آن است که پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده، در حالی که در حال حاضر مؤثرترین نقش را قطر در این میان ایفا می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444262" target="_blank">📅 15:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444261">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
وزیر ارتباطات:  تا زمان عادی‌شدن کامل شرایط بانک‌ها، خدمات مشترکان تلفن همراه و ثابت به‌دلیل پرداخت‌نشدن قبوض، قطع نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/444261" target="_blank">📅 15:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444260">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
ایران و عمان توافق کردند گفت‌وگوهای خود را ادامه دهند تا دربارۀ نحوۀ ادارۀ آیندۀ کشتیرانی در تنگۀ هرمز، خدمات مرتبط و هزینه‌های آن، مطابق با استانداردهای بین‌المللی، به تفاهم برسند.
🔹
همچنین قرار شد در این زمینه با کشورهای ساحلی منطقه و سایر طرف‌های ذی‌ربط نیز رایزنی شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/444260" target="_blank">📅 15:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444259">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">منبع نظامی: فقط تعداد معینی از شناورها اجازۀ عبور از تنگه هرمز را دارند
🔹
یک منبع نظامی با اشاره به وضعیت تردد کشتی‌ها در تنگه هرمز، دربارۀ آخرین وضعیت ترددها به خبرنگار فارس گفت: براساس هماهنگی‌های انجام‌شده با نیروی دریایی سپاه، روزانه تنها تعداد معینی از شناورها مجاز به عبور از تنگه هرمز هستند.
🔹
این تعداد از شناورها به‌صورت روزانه و متناسب با شرایط، متغیر خواهد بود.
🔸
گفتنی است، در پی اقدامات خصمانۀ رژیم صهیونیستی و همچنین نقض تعهدات آمریکا در اجرای آتش‌بس، تنگه هرمز طی روزهای گذشته بسته شده بود و در این مدت هیچ‌گونه مجوزی برای عبور شناورها صادر نمی‌شد.
@Farsna
- L
ink</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/444259" target="_blank">📅 14:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444258">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4de625391c.mp4?token=dJPgVMFFV1qGnGJfEgyU7UtcpLRh3rCqp4gpi8erjSP8wu-j3t68WcwrnsE76DFs_V-D9ebKUl0Q1ibc8_l_ecePWChKLR2z1Kf0SyaHCD__3KGBGbnALftTTQRm1ZEFK6TerObFqTtBt_v7y2XinwQ8xrdv4kE8vhW23arkl3o9_RSWnFx7ByL3gGybbghVZMu90agkLxXdOF37ALoLyDtUz4_HnhYudLGtxyNzhfv-QBoaXzxPu57vgxslxQlVDoTtrZQ3Hn_H_Z5KdQlAX7RNAR4lft9fheXY3OokB1MUz8_feUklZlsf2HRkLR6xk_1oJmextET7wq--imVIkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4de625391c.mp4?token=dJPgVMFFV1qGnGJfEgyU7UtcpLRh3rCqp4gpi8erjSP8wu-j3t68WcwrnsE76DFs_V-D9ebKUl0Q1ibc8_l_ecePWChKLR2z1Kf0SyaHCD__3KGBGbnALftTTQRm1ZEFK6TerObFqTtBt_v7y2XinwQ8xrdv4kE8vhW23arkl3o9_RSWnFx7ByL3gGybbghVZMu90agkLxXdOF37ALoLyDtUz4_HnhYudLGtxyNzhfv-QBoaXzxPu57vgxslxQlVDoTtrZQ3Hn_H_Z5KdQlAX7RNAR4lft9fheXY3OokB1MUz8_feUklZlsf2HRkLR6xk_1oJmextET7wq--imVIkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار و رایزنی قالیباف با سلطان عمان در مسقط با دستور کار ترتیبات مدیریت جدید تنگۀ هرمز  @Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/444258" target="_blank">📅 14:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444257">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpPsfp4IF45dthA0ujE1_6SjCqx7fiDr2ohE7KWhQNnM-UJkHVxDgYSNbUbUBPK6JJ3b062I4OxRYH6gTDT06zwO96aWKFGH5NN2AIZK5OlDf1iCIPO_bCTyj5F4pN7qS4SHwVAE1zf2szi1wSWADeIG8SqcsLfoi_Qvx_jVim9fAV5AoCpXiPhZfHdRwzpRO3xNDTAq5CQmRa9AVTrv4Z4B_ktszzvoSEaF9cG-YarWLr4dmaJ5bMiHzXNlC72B_Ugeq7fpoMXA6sFiUKIBDRWDOPeMcomPbXCyNjw-Qz3wRRAqk8QCRUILDKhW4KKRXQ5Uh5_84Z-zw3YsAQBWNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر پوردستان: آمادهٔ عملیات پیش‌دستانه هستیم
🔹
رئیس مرکز تحقیقات راهبردی ارتش: در دکترین تهاجمی، عملیات پیش‌دستانه نیز تعریف شده است و چنانچه مصلحت نظام ایجاب کند، ممکن است با انجام عملیات‌های پیش‌دستانه در عرصه‌های ناشناخته، دشمن را به‌شدت غافلگیر کنیم.
🔹
نیروهای مسلح هنوز بخش مهمی از توانمندی‌های خود را عملیاتی نکرده‌اند و دشمن می‌داند که در صورت ارتکاب هرگونه خطایی، با پاسخی فراتر از مرزها و تنگهٔ هرمز مواجه خواهد شد.
🔹
در یک ‌ماه اخیر، ما چند نوبت تا پای جنگ با رژیم صهیونیستی رفتیم؛ لانچرها آماده و دست‌ها روی ماشه بود تا در صورت عدم عقب‌نشینی اسرائیل، جنگ آغاز شود.
🔹
تهدیدات قاطع ایران سبب شد تا آمریکا برای جلوگیری از گسترش جنگ، به رژیم صهیونیستی برای توقف تجاوزات به جنوب لبنان فشار بیاورد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/444257" target="_blank">📅 14:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444256">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc369d335.mp4?token=epkEnYiqkSPuT1kImdrmHlZOSMooLS-MyyzMbZjsltp65nEqFlQgxXdd03reMPxNgKEW4VUZQYM57jV5h0wDAtQHFraYq9ETLC4ToRaXmoFS7SuuUl03BYQ-wG2Z7O1Dvep889yo6vtT0mD8gd2KGgf_702RBXB8z_3p3qrA6e-2DlNLgQSkB8asqKjcApXbcX0Q8fnk7yLSVFx8ieWMHahIOcsgc_uskErk_LpGCC6D4Y-198rksY8FFCNg3eUcOL4LARQW-LlPeOVCISrdtk2GRQE5zB77GAiDKM5jl50HXUfG6-L7b8oEczIi4nfW9qqQuQCwnKDViqzjzcDwNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc369d335.mp4?token=epkEnYiqkSPuT1kImdrmHlZOSMooLS-MyyzMbZjsltp65nEqFlQgxXdd03reMPxNgKEW4VUZQYM57jV5h0wDAtQHFraYq9ETLC4ToRaXmoFS7SuuUl03BYQ-wG2Z7O1Dvep889yo6vtT0mD8gd2KGgf_702RBXB8z_3p3qrA6e-2DlNLgQSkB8asqKjcApXbcX0Q8fnk7yLSVFx8ieWMHahIOcsgc_uskErk_LpGCC6D4Y-198rksY8FFCNg3eUcOL4LARQW-LlPeOVCISrdtk2GRQE5zB77GAiDKM5jl50HXUfG6-L7b8oEczIi4nfW9qqQuQCwnKDViqzjzcDwNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر خارجۀ روسیه: باید شرمنده باشیم که نتوانسته‌ایم مسئله فلسطین را حل کنیم
🔹
نتانیاهو درباره «اسرائیل بزرگ‌» صحبت کرده. اگر این طرح‌ها به نتیجه برسند، تشکیل یک کشور فلسطینی یکپارچه و پیوسته از نظر جغرافیایی عملاً ناممکن خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/444256" target="_blank">📅 14:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444255">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3421a74a.mp4?token=HfFaVQvDFr5_PVDVWF387yrCwJbOUiXg3TsbhtN1ejOgqL6jyzZMmpVD8s6k0EqEyTDhMiLQszY_toO1R4EnmBBk529u7b6MdX43pj31ssxFrU1P7hxvp2GtI5JvD90GmVGcxUvUSFEQqG0DkS4CEOFisVAJNqV0YiVWgWXZc53cOfBtNvt81hHsKGIt54-WcblJqzQmkllJ0S1T9a-J3vLduZa2yi-spjPXhHYsMDGjUhNiDB-MnUonSwjhkAR8T5_UGcCJWEYkPJXXyg6DvaRCLPd9n-x1CiPBdgmxxw1tYz_gN1PNPbF8MsXxqkmepP-qfuvqnPF4M1OeYF0PHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3421a74a.mp4?token=HfFaVQvDFr5_PVDVWF387yrCwJbOUiXg3TsbhtN1ejOgqL6jyzZMmpVD8s6k0EqEyTDhMiLQszY_toO1R4EnmBBk529u7b6MdX43pj31ssxFrU1P7hxvp2GtI5JvD90GmVGcxUvUSFEQqG0DkS4CEOFisVAJNqV0YiVWgWXZc53cOfBtNvt81hHsKGIt54-WcblJqzQmkllJ0S1T9a-J3vLduZa2yi-spjPXhHYsMDGjUhNiDB-MnUonSwjhkAR8T5_UGcCJWEYkPJXXyg6DvaRCLPd9n-x1CiPBdgmxxw1tYz_gN1PNPbF8MsXxqkmepP-qfuvqnPF4M1OeYF0PHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ احتمال تعطیلی ۳ روزۀ تهران در روزهای تشییع رهبر شهید انقلاب
🔸
سردار حسن‌زاده: در خصوص تعطیلی ۳ روزۀ تهران در مراسم وداع و تشییع رهبر شهید انقلاب پیشنهادهایی ارائه دادیم و در صورت تصویب، موضوع رسما اعلام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/444255" target="_blank">📅 14:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444254">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI0_t0kgCdDs2_IG076Jdv1t_9oUBvMLbn2PFYZ0YSH5pR69HNvg9f7jTl3ys8nBkOF2txsv96WKyxnC59oh5mzJodeU8NwJisxOElZJ0LOpifxSVua0uQ3KnWH0LVmV-_SaHL5vHAMkI8DNz0Qy5Tbhgmit0VdQ8zNlArT__SVud7VgaB7C2niLOIHYTYVXtztkhPXLIFfu_3442pOub0yhEFiafTFCj91PYHqrUtb5L21cpUAMZiGk7L3v1NpSUo0mdrRHnZuJKcuzmwLSG_ymPriMY3aXxNlPQ_M1Jv34OyhJLMf-YytakrJy96NdWeAXJc4mZQGiBsGfXVpxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی پیش‌از ورود پزشکیان وارد پاکستان شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444254" target="_blank">📅 14:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444253">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiFn8V70wbmLLUAAcEdCrunzu4Zv4Lxw8xQpbv_u9XeqxAQbC4pQ71msRXbteU1_1pZxZ8HuzuqyvOGQPdCWfG5eiheF-4hwstKCD8ycDnhw1b5dmMynbUKNvKh33L_T2rak1HeBzWyX1chqsHUtlYZCQg63JYSH4LFSPR7MaLT62xox9y7wgpm65S3ydbsr9LAe1xyL1_RdcrCqf7x2AlBwOWl2a4RyhDzc63eN598DljIeFUq0Dnr0ECL_8IHTpOzqsqc3bCZfBzR14wTVEKgQ-oMpRNPYfegahOMj4EQl3wyRq3HfIDPfBi0ohTdmQvkP7Nc5BPt4q2wlH56kXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان راهی پاکستان شد
🔹
رئیس‌جمهور به‌منظور گرامیداشت یاد و خاطره شهدای جنگ تحمیلی اخیر، به‌ویژه ۱۶۸ دانش‌آموز شهید مدرسه میناب که در پی حملات آمریکا و رژیم صهیونیستی به شهادت رسیدند، با هواپیمای ویژه «میناب ۱۶۸» عازم پاکستان شد.
🔹
پزشکیان پیش از عزیمت به…</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/444253" target="_blank">📅 14:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444252">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3TNJsudsiPO0f0oHwomEG5RW5Rnj2xiakhSJn9XVMwaqRjbV3rQnph6hOv840k7ORsytpgVTrya2UVa-mkVWq-ymBkeG7pWch051OxdJHYm8HykNsRy3Jv1N7hIPmGT7OjxvTgcHN3X1yqzglp3lFcSwIs1pWgxYUjj-ZJmBh6_CXEP9PwNaE1rlxaQtwlUwMQ2I_nbtuH2xMaLTwnjFgYfm5rzsM2pzgOadluC98tKYqA7bFANnLKQ_BhDDyIs-7PxWo9e82vItwSREozYbrEdR0-SjAzK2aCxn-99J22wMahxznrq1WoWclCqTyc70MPQ9NvkNXsGnh13laF9kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المیادین: عراقچی یکشنبه به عراق می‌رود
🔸
عراقچی هم‌اکنون همراه قالیباف در عمان حضور دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/444252" target="_blank">📅 13:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444251">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌ توضیح بانک مرکزی درخصوص اختلال در عملیات ۴ بانک
🔹
بانک مرکزی: اختلال در خدمات ۴ بانک ملی، صادرات، تجارت و توسعه صادرات درپی یک حمله سایبری به زیرساخت‌های ارتباطی این بانک‌ها ایجاد شده است.
🔹
خدمات پایه مبتنی بر کارت با استفاده از روش‌های جایگزین دوباره در…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444251" target="_blank">📅 13:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444250">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
یک شهید و ۲ زخمی در تیراندازی نظامیان اسرائیلی به شهروندان لبنانی
🔹
سازمان امداد و نجات لبنان خبر داد که نظامیان اشغالگر اسرائیلی در محله «الدیر» در شهرک «النبطیه الفوقا» به‌سمت تعدادی از اهالی تیراندازی کرده‌اند که در این جنایت یکی از غیرنظامیان به شهادت رسیده و ۲ نفر دیگر مجروح شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444250" target="_blank">📅 13:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444249">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoDZ6HR4nX_rZZBSlwbn_-kj_NIDmXZ9RhC5k3vgR8dV0zf9ogi3HX08enePELsg8TGOQErH_S13K1km5KKiQLvpBzoThvPgllv5Um0GaeeXy1xzE7fKOl_DUdZYx7gBHh_ukIXSQz8vMoH_zg6f-7CjjenlVWeJWVqUIf14cRLuBilVbxfvKZ-C-v9vZ3g-eYMAqT9TO4vDsHPp3Aui8WF3FXYQuBpfxteQalJsQCnuYNgu8ECdsxK8MLgvhBFVzwBmc_WS2dLZ_Xotojcnrp8hTPiCqU-czM--MmZ3d2_Z7cBY-3Z7R9cY3OWF8gzO4o2Gj_KKsn39N3Asf36vNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از مجاهدین خلق تا اپوزیسیون امروز؛ یک خط ثابت در حاشیه جام جهانی
🔹
«هنوز مشخص نیست چرا سازمان مجاهدین خلق هزاران نفر از هواداران خود را به این مسابقه فرستاده بود.» این بخشی از گزارش میدل ایست درباره دیدار ایران و آمریکا در جام جهانی ۱۹۹۸ است.
🔹
فیفا در طول مسابقات حمل هرگونه نماد و پلاکارد سیاسی به ورزشگاه‌ها را ممنوع کرده بود و تماشاگران برای ورود باید از چندین ایست بازرسی عبور می‌کردند. با این حال، هواداران مجاهدین خلق موفق شدند برخی بنرها را مخفیانه وارد ورزشگاه کنند و پس از استقرار در جایگاه خود، با درآوردن کت‌هایشان، تی‌شرت‌هایی را که تصاویر رهبران این سازمان روی آن‌ها چاپ شده بود، به نمایش بگذارند.
🔹
اکنون و در رقابت‌های جام جهانی ۲۰۲۶ نیز  همان رویکرد همچنان ادامه دارد؛ رویکردی که به جای حمایت از تیم ملی در یک رویداد جهانی، تلاش می‌کند عرصه ورزش را به میدان تسویه‌حساب‌های سیاسی تبدیل کند.
🔹
تلاش جریان‌های مخالف جمهوری اسلامی برای استفاده از فضای جام جهانی سابقه‌ای چند دهه‌ای دارد، اما این تلاش‌ها عمدتاً در قالب اقداماتی نمادین و محدود باقی مانده است.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/444249" target="_blank">📅 12:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444248">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fd326b9a.mp4?token=Z0BolmmNuVwPxNSwIqTXmutfHAZYn9e2sTcmD9vSFYiigPlxkilN5Xa0zZ-JcNvOMxhMtOQOAumAWTbUos90mvNFYjW3cNj7FeBR9uP_UVMInu9R8pXCP0vwo5_OWPZ6niJCivnP7bvp_7CH8jqquYqykxn9DJaChojL0X23m38KB3AyXaznCnxvB5fgdBbUpEA1F1923zpwLTgWOjpd9bb4EiQaXT2CaFiIpr7ulx98ZeonsJZTRA8PUqBbwQJ3tsKz5x7w8blTdemGLnQRqyleRRC5UwpaqZcsje_Qyf55BAUaujGN0M1VtHOldpdThXLK0RoxZdW0R-Xy5sqh0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fd326b9a.mp4?token=Z0BolmmNuVwPxNSwIqTXmutfHAZYn9e2sTcmD9vSFYiigPlxkilN5Xa0zZ-JcNvOMxhMtOQOAumAWTbUos90mvNFYjW3cNj7FeBR9uP_UVMInu9R8pXCP0vwo5_OWPZ6niJCivnP7bvp_7CH8jqquYqykxn9DJaChojL0X23m38KB3AyXaznCnxvB5fgdBbUpEA1F1923zpwLTgWOjpd9bb4EiQaXT2CaFiIpr7ulx98ZeonsJZTRA8PUqBbwQJ3tsKz5x7w8blTdemGLnQRqyleRRC5UwpaqZcsje_Qyf55BAUaujGN0M1VtHOldpdThXLK0RoxZdW0R-Xy5sqh0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: قالیباف قرار است به چین سفر کند؛ زمان سفر هنوز مشخص نیست.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444248" target="_blank">📅 12:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444247">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_OflVkXJBAAKuaKM3qFtbjb99_0gKziv7RjyC9Z-QcW0jjP5V3jENtaqgSs7qlRyGjQYf8hYNrRNRk98zPBeh80JCFpT73Wt38PFJLMDdaT6pALhHcTGYWKgMrymD-iSn5-Y63etk5FwvtAlUUKQ3Dvo-g9nK0binbTAYT5Kzil3msov8yJSyNactmRZFWwyILYwXUslaVXiOp5P4Q_zLN8_CEx1z75DgEvvZgvL9GzlP5LqKHTb792PHbdU1qJ0LQQhyZRtXclTY8AUYWSk2knCv_0Ro7VBA1Qxu_oZlqrAyZoxMvuqhWvG3vdj999Puz_z-89T-1bWJQT29C56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با جهش ۸۸ هزار واحدی به ۵ میلیون و ۱۶۱ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444247" target="_blank">📅 12:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444246">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0qHXEyNqldFfSbdKe8HzzO-VJGldgN8ElfCzXGM1HlDpUraJ_nHWoJ_6NuqK3jd31NLgEwZ4Zva3ZVC5Ukdvj-kLkxnYTpYhm07YFGB6y_wP7y-zXb2KKpcmFKU09Oo_NzdE2sR2xVsIWbcjU_ACpoaQcLS4gBvfXCnDiby6oYMW1-bGWlaQXsQHQkmjNxP-yslUj3USPYDR7hUEtO9nkoKLL06--5PC4Xuvftjk99UR5dkYJs1Pl_9oWMbo6IYARrz6gG967Ji5Lzb7uLiGRXUGBaj5OYoWvoNNNEaxXvUE7aZob7j8rgjUuUBSY6zC6uOvF8SCoviArKBU0JULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این علامت‌ها خبر از سرطان رودهٔ بزرگ می دهند
🔹
سرطان رودهٔ بزرگ یکی از شایع‌ترین سرطان‌هاست که معمولا در مراحل اولیه بدون علامت است، اما برخی نشانه‌ها می‌توانند زنگ خطر باشند.
علائم هشداردهندهٔ این بیماری چیست؟
🔸
تغییر مداوم در اجابت مزاج
🔸
خون‌ریزی مقعدی
🔸
درد و نفخ شکم
🔸
احساس تخلیهٔ ناقص روده
🔸
ضعف یا خستگی مداوم
🔸
کاهش وزن ناخواسته
چطور پیشگیری کنیم؟
🔹
انجام غربال‌گری منظم از ۴۵ سالگی
🔹
تغذیهٔ سالم
🔹
فعالیت بدنی
🔹
کنترل وزن
🔹
پرهیز از دخانیات و الکل
🔹
تشخیص زودهنگام سرطان رودهٔ بزرگ می‌تواند شانس درمان را به‌میزان قابل‌توجهی افزایش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/444246" target="_blank">📅 12:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444245">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91a9021eb2.mp4?token=Nmnfco_7s5gJy4ZcyHA-m0mDvcvAQxJm-5CvL4jZciNtrOyPjP3ziWGQgQBuBmfOpQ1MZiAXWU_9EyegMTCfP2lMJdcN4PlNWq88wPP4XnVke9d5Pi2lEleUzDHhBfFMEcgZZEYzusZgehZLRGcpJV3LdB-lfRGczpnh3a0e5bdz0x2xneFwnA0atqlb3_mCVfPQri3M9biua5X2CUsOfNk4ZKkIlR8mC2WfnpNS48go06nIKSQwUK1G6r5w6ATiuSEjy281sTz-3RR2Hs2xKlGfadPqdLdNK-g8IKuJbWOYK-LalCm352JZLj1-zmkNVvD_Z7jMoYrrDuPxs7k2RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91a9021eb2.mp4?token=Nmnfco_7s5gJy4ZcyHA-m0mDvcvAQxJm-5CvL4jZciNtrOyPjP3ziWGQgQBuBmfOpQ1MZiAXWU_9EyegMTCfP2lMJdcN4PlNWq88wPP4XnVke9d5Pi2lEleUzDHhBfFMEcgZZEYzusZgehZLRGcpJV3LdB-lfRGczpnh3a0e5bdz0x2xneFwnA0atqlb3_mCVfPQri3M9biua5X2CUsOfNk4ZKkIlR8mC2WfnpNS48go06nIKSQwUK1G6r5w6ATiuSEjy281sTz-3RR2Hs2xKlGfadPqdLdNK-g8IKuJbWOYK-LalCm352JZLj1-zmkNVvD_Z7jMoYrrDuPxs7k2RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز جلسات ایران و عمان دربارۀ مدیریت جدید تنگۀ هرمز
🔹
هیئت مذاکره‌کنندۀ ایران پس از پایان مذاکرات سوئیس راهی عمان شد و گفت‌وگوها دربارۀ ترتیبات جدید تنگۀ هرمز را در مسقط آغاز کرد.
🔹
قالیباف، عراقچی و اعضای هیئت ایرانی همزمان با سلطان عمان دیدار کردند. تنگۀ…</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/444245" target="_blank">📅 12:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444238">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CH_ToTkFUjcdVDEhy3GbOHB_IdNKCcK_A_hyTrfZSSMa8qXXg6ZVzlpBrv488aI8bbeN5bCvHWNHiQZbwx_5fps3l2CdciReseIN_SuArFIfki0782Ds5aAdjv7kQ-JZrG8981Z5-SY_0UtG_n4AnOm4-9YS6nq6J8S24D75zDf4LPfCvHGKdZaqGBfu7GjN44ovhN1acH3A3AYzy2h0cDivOP8xhfAg-d3QbTI8L3WzirHX1Z6XzW4Yu45GseSh1jvJrqDKAwvbCMeTvQBh54BjBQGG-fVRoRfxiXg5jzfMs5Z5nZHBH1Jmo4qY-WEtHHvnr-wbDFEF6cl-2ApxrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z01RwB4xek_2cK4FIKEIQPMbD0sMo8a5-IN3LTRWbSjCw5WcSZJ-UHBWqjCFCj0EKajaoFZkrMsYFqeLFlksNx5Fg0lb1hT_ApzE5A24BOqoaBRFN18KEV0A0ZGT8d88yEhhfq0WfJREQfWUWIfp6SpU7LtTGv0vI2QUQ4vBaBu7qj-KpmNekd9WwLr1qJPT59XMw78a8EIQozU_isUmUYy9Vgqi1PUVHiZkLpAiJ7tyaZVwBpOjqM-ZatGUUzx--1sCUNw3a8mocUZw2UYX3G7DBev94ntAbFIKQO8BFz_fOkYHpugMte34e6fqqwYk38fAaXQKKRLP-Bi4ygFNKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sQnpqN9bbCAq320QdGXwptmJa0W7rTnvC5aLe1HpPv2yLw_2fPlU2EkpdiLLAYD1DtAUXmNNY_NgAtzpv6Y2ZM1YE5xAqoC-66bN-i9fraCnpUL24o6-dMoeD7KewsH8C85KW99HGIg9aMqL2dPKEwQ0vujHXe7EI4l-DoT8lsw6anubWRaCg92tIF8HaayoGWo3nvVkZC45x8-4vclHqpi1KkZSFSWnfCU0xOTFrtBYzxo5m8C4ByO6s5_T_yIR_wxkni3YaiHcB6ZLqTmd00BT_EvQHtEcZzYBIMPyIPK4XbVLfKKjCfApqvwP_JqCo3LHmi7gozT8_xgrDxfNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hso1i2iZ107T_SRoSRrjuRwRGtP9GSnyYmy5Kgm-TSzbcX_M-0q-yNknEzMw_a83Y_6pigquCv_YvMWsGYKDEeTS5SbeBPoA11ZJS1UBpMdDK0Cj2iAKXiZ7_b7o8wNE2whED0jqlzDixzL3twjnQev2BMsZMW6cPoVhBSv2Z5fZMqWF2nhM2tuIav4i2dnEwZIqdtNm5-7KZKFw6hTQNIVao4F3aKPOuNSmsF68fsw_oQ6SRjElF1Ux-vT_0ZmVHsgPsrPnIPkwsh84I-GxsfDY90BGQRoYlFOcZQ5WPAJ8gY4PgQsC6_GBIuXyayBuvKn0CRulDseZaas_ZzZrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BBulbmXLSTb8m7mxZrZ8zqDIdyj95UPhpSzpVhnQmId2aIUPe6KFXtbjqxRpUjCGdYIHEdhZmCo2xS4SATVoECp_926H7lP5XrBtAyZvoC56kMidqLsYgSwxu5xIBYGZW7TsUxm3V8yGLFxQAUJJKCpzATkdllIrojfh7dlvHZfwflo8rDTeDgpEZ3cCFZPYcQWQOAreZ0dNzqNtoZLeBzUtNuYR9zEOY_8SEX7IhQuBXJTmWlxubxceLKhhWafFrpPEx2Cd1lsjvWrA5pH9dH5HOVVUTphbwr82R-iMk7fVQICfP-DqKdUQuZXTO8UPaVmDt8nYG1_k4hIfW8XC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QePH2mTLG-gr_shZliwaZvoW-1hIhpLgkaCRZ1838Ek97wupdjDrYfGVP_kcl0SSEM-FbVtEGLHaYYW_l29Uw1x_LkrJazSxBwGvOdrkpq9bHdKr2mCVK0NyutDrGCoPDoR1H5slIDir4Xc458qkJQwdw-Wwn65tHxAZRcLC0OBjfoiSfDDCfwiBpo__GapmmWDOhWSPoDoGmQqNy0qLSBk_10n1vJigQLYGNp0PpYo49y7qWoyz5wks6COzmc70kxFE9ff2pW8x9YjHf8M0e0iIXz4YuuJnkUou5SwAlVPWczg5jYflQVdQti6IAgcZWj_PLEJi2BhyfFqwedXIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgReAsU1yy5UfSk3LA-JxSyxF_jFHSp0vbYs2_-6H0T1gJhkgtR38meDoNuNdtW0CyuwDd2hySYuYKvzzM9LIGuLv-cmLY25-n1ehZDhLdAFfT4Qn-J3O7c94FUmY5JLmet6LJHYUAsGAYcuDX5DgfkZge0tGomaxCiEF2JD-UF35IAStUEh9nn1kzNff5-Dn1TqKfTOE4s6CEgLW4qWMQcmGaR4nqPImZ_jWPPf-UIPNebeLTD_vqOr4I04fyy3Rmd61FUUgg6CVTWWWHI3sRoQWrWBSLed5DSnxJuh8TM-lZBwJZDyFCg1cONab_njU_L_jZLgo_szKzP0XJxt1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور شهردار تهران در خبرگزاری فارس
عکس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/444238" target="_blank">📅 11:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444237">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a13e62494.mp4?token=ql3qY5MfYvGZ668AzCBYUc5L8XnNQ0uOUzgfcNPXGS_h1GKlvqN4oPKK85fPxlnfC1JbaXSoDjeFbE05GDhfptoYI44_Wk0F8Ik1bOcmavWncAk89ytStVf03-WbpUiUO74V2FkpnrY-OOpk6HpfnJkrxURQfYZpPucFhupp7Ffy8a8aTYa4y1C69K7gTaPEGmHGOJb18xK5Su_TVvpFt3cF-ZhfuzuFirq5od4eAwYVd8kPQd_tuJT4fKGsbOuXgXypbmXHLKaNOV9rUNlwqj-346P1eOfQ6pzA-OyWLadu0mpJhsrxPatFfLjWHXXVLNTVji6wJRR0hcVF3OZnaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a13e62494.mp4?token=ql3qY5MfYvGZ668AzCBYUc5L8XnNQ0uOUzgfcNPXGS_h1GKlvqN4oPKK85fPxlnfC1JbaXSoDjeFbE05GDhfptoYI44_Wk0F8Ik1bOcmavWncAk89ytStVf03-WbpUiUO74V2FkpnrY-OOpk6HpfnJkrxURQfYZpPucFhupp7Ffy8a8aTYa4y1C69K7gTaPEGmHGOJb18xK5Su_TVvpFt3cF-ZhfuzuFirq5od4eAwYVd8kPQd_tuJT4fKGsbOuXgXypbmXHLKaNOV9rUNlwqj-346P1eOfQ6pzA-OyWLadu0mpJhsrxPatFfLjWHXXVLNTVji6wJRR0hcVF3OZnaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: برای ما مهم این است که به دارایی‌های مسدودشدهٔ ایرانیان دسترسی داشته باشیم؛ جزئیات آن به ما مربوط نیست و این جزو تعهدات آمریکاست.
🔹
خروج خبرنگاران از محل مذاکرات سوئیس به این دلیل بود که ما برای کار رسانه‌ای نرفته بودیم؛ ما برای مطالبهٔ حقوق‌مان رفته بودیم.
@Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/444237" target="_blank">📅 11:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444236">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d4781cf4.mp4?token=FTQnYZQjSGDAiTp4PAv9-FEZwqRVBumFJVi4P-arJuQl6j2kc82KiTY0ewHhvXzavoitCf1KzEvn06-EO8Mix-u0RZVQI0MEhnITYFBoVqO8mOQpHwWw8Y5sEcplXZsMcmUAHgK10V9MTAY45Y_de4gpgQ1Ig2CNr3O1IxLUrFKipCzrlgtT0GIX_DX6vMxM1r254sylMgenf-5_4A9o0gizzQRG-JiopTK0xOPt15U6sa4M3t3c4oj4-gCMNNPGIT9tjETIiyUv8zj6BEoPZgiaHs4_jcUr3qtdFM8evzw3dJH84M66b7TybTJDlR2FFfVnw2JTMsXZxYKLBvTYKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d4781cf4.mp4?token=FTQnYZQjSGDAiTp4PAv9-FEZwqRVBumFJVi4P-arJuQl6j2kc82KiTY0ewHhvXzavoitCf1KzEvn06-EO8Mix-u0RZVQI0MEhnITYFBoVqO8mOQpHwWw8Y5sEcplXZsMcmUAHgK10V9MTAY45Y_de4gpgQ1Ig2CNr3O1IxLUrFKipCzrlgtT0GIX_DX6vMxM1r254sylMgenf-5_4A9o0gizzQRG-JiopTK0xOPt15U6sa4M3t3c4oj4-gCMNNPGIT9tjETIiyUv8zj6BEoPZgiaHs4_jcUr3qtdFM8evzw3dJH84M66b7TybTJDlR2FFfVnw2JTMsXZxYKLBvTYKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: توانمندی دفاعی ایران مطلقاً موضوع هیچ گفت‌وگویی نبوده و نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/444236" target="_blank">📅 11:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444235">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502e49ac2f.mp4?token=qWr-KtCZ7NLFoEUWYlUkuHnBgm0z8fJNY4urssMjx_Lauxl1z1473CXPiiDBtWFGamzldilz9QtVfPGHSXSK6gANZdszZkxadfXCELrVXFDFLtl4mFhRmNKaOGmNLim0so4cWxOmyIrR4UfhvTcSmMpa_oKJHsuBDP1fMppptBER5biNYjOwdm9-u-TEIH-g3L4oERXisMq1UxV0WjeuaA4iGcICjAV1SUflpWNBTsZeFoFX43rTDEE8AQTAcYC5o9MXeFApFpiZBBgQmsvrPfnfZuZ2_NIma0CbSt6IfvYI3b2uVBcljaMg7g1__dWhF9tWBN7tk-hNURV18t88ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502e49ac2f.mp4?token=qWr-KtCZ7NLFoEUWYlUkuHnBgm0z8fJNY4urssMjx_Lauxl1z1473CXPiiDBtWFGamzldilz9QtVfPGHSXSK6gANZdszZkxadfXCELrVXFDFLtl4mFhRmNKaOGmNLim0so4cWxOmyIrR4UfhvTcSmMpa_oKJHsuBDP1fMppptBER5biNYjOwdm9-u-TEIH-g3L4oERXisMq1UxV0WjeuaA4iGcICjAV1SUflpWNBTsZeFoFX43rTDEE8AQTAcYC5o9MXeFApFpiZBBgQmsvrPfnfZuZ2_NIma0CbSt6IfvYI3b2uVBcljaMg7g1__dWhF9tWBN7tk-hNURV18t88ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
کمی تهدید وجود داشت، کمی هم گله و شکایت، اما در نهایت، مذاکرات ادامه پیدا کرد و ما به پیشرفت‌های بزرگی رسیدیم.</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/444235" target="_blank">📅 11:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444234">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9d4619ca.mp4?token=Wtx-_GhGa9TkTN37cH9TaN3V9CgqHid5ozLDZwipAPK0d32NXqvuLw9p7_LWg0zxwjxb_Zv2ZQHHkiTLMeymuiagF8WBisE2L9HK2WIIXbwPpXqdLiqeVfCMwSNz9mwRcTqhCS0ZENjlcYOOM7bZcjg32kPhGUZBJYpeNb_fZj7B0URBOD7vNQV3ZcRAQLRatshcIpHSX8CSL2l4w7LJVHIystkxEqtE2j012QjnAfIOaL_DzMl7BQmtR5A3YBqxQeEGhpUpwKeaIH-n6t8Uu5GprU4G1L344tUgO7IbGgl2d3FzWFUev874yBuKtHUFBdACbXrjXBGkqlfTsXOoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9d4619ca.mp4?token=Wtx-_GhGa9TkTN37cH9TaN3V9CgqHid5ozLDZwipAPK0d32NXqvuLw9p7_LWg0zxwjxb_Zv2ZQHHkiTLMeymuiagF8WBisE2L9HK2WIIXbwPpXqdLiqeVfCMwSNz9mwRcTqhCS0ZENjlcYOOM7bZcjg32kPhGUZBJYpeNb_fZj7B0URBOD7vNQV3ZcRAQLRatshcIpHSX8CSL2l4w7LJVHIystkxEqtE2j012QjnAfIOaL_DzMl7BQmtR5A3YBqxQeEGhpUpwKeaIH-n6t8Uu5GprU4G1L344tUgO7IbGgl2d3FzWFUev874yBuKtHUFBdACbXrjXBGkqlfTsXOoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون ترامپ: اگر هر کدام از دارایی‌های مسدودشدهٔ ایران آزاد شود، ما روی آن حق تأیید و نظارت داریم، قطری‌ها هم حق تأیید دارند
🔹
سپس آن پول عملاً صرف خرید سویا، ذرت و گندم آمریکایی خواهد شد.
🔹
آنچه به آن دست یافتیم، از نظر من یک توافق کلاسیکِ به سبک ترامپ…</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farsna/444234" target="_blank">📅 11:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444233">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfbfbc0c5.mp4?token=JKFLyYtLscPj6w776uJw0ES0R3C9PMKfJimH2vnmyNwZT9i3BtutZLW1bNh6DATX_zOM8nUkfEjtkmduqxZ9psSeQG8c4uT0l9af03msCnHuxd9lE_8dQNL5P3-hGk--HJcdf_xrChqZWwkDeMYuc-FWGlxqCCB-UpWIrrq9gCq3-7WJ9A7wCtVclKF68tsbiVa0rGCq29ZdyzNU9iFgkKQM91StH-8gfuVn5IaaxVuqsO4oPW2YaZRZ5vCm8Uk00ww3_ZAzLg7dSL8NFek2X2UnRWClClsnc0S_1Rp2pctZD3RK2QWJVrS89JuwXM9ZDB9hqDLgW9-nxKYVAb3mkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfbfbc0c5.mp4?token=JKFLyYtLscPj6w776uJw0ES0R3C9PMKfJimH2vnmyNwZT9i3BtutZLW1bNh6DATX_zOM8nUkfEjtkmduqxZ9psSeQG8c4uT0l9af03msCnHuxd9lE_8dQNL5P3-hGk--HJcdf_xrChqZWwkDeMYuc-FWGlxqCCB-UpWIrrq9gCq3-7WJ9A7wCtVclKF68tsbiVa0rGCq29ZdyzNU9iFgkKQM91StH-8gfuVn5IaaxVuqsO4oPW2YaZRZ5vCm8Uk00ww3_ZAzLg7dSL8NFek2X2UnRWClClsnc0S_1Rp2pctZD3RK2QWJVrS89JuwXM9ZDB9hqDLgW9-nxKYVAb3mkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ونس مدعی شد که «ایران بازگشت بازرسان آژانس بین‌المللی انرژی اتمی به این کشور را پذیرفته است».  @Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/444233" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444232">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh58wGa82UZZ0VHzd-T9_AmyNFbSiqM1LqD6YHXdhq0gvOuLVQ1eQY-MB-t_M4QnU22bsNXtTdJIec6pGUOlGcZkpDK77ry4vAWgyzwkE94RW6qmQuFBpz0hSaiQp54vzJ6BqJ_tR5-VDVof2cukkHszxKvgLIBVT4EYohbiz4uFzwg4_fxgEIIwLHEJ3N3ndHVgB8WegWypOb8fVhDfRMz58UxJD-NmA2QsskmMWmcaR6zvBMElKXaMWQGdkvjpC_WqSlHU8ja0-9KjrAIRMUbmHbuPi3w-ZqZvnUQN572LjCGLOAaO1k_DL_3u0MOsaHD5mXa4pd2hyw31WWjL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مرزبان در مریوان
🔹
دانیال نوریان از پرسنل مرزبانی مریوان، در حین پاسداری از مرزهای کشور در پاسگاه انجیران به درجهٔ رفیع شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/444232" target="_blank">📅 11:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444231">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia48Ch0681atVxRFbK48zVDRTS-aCyiFtlOFyRDAgOLoU3Rfn9psLj45QWqVMZsR9EqORXl9SM7OibSlsW4pSgi8F8HqoB439L9LBUjsq62s27ZAnLbBJkdRXmZ18btFMxGb65WYDDkHYMQ81vOeuLXLM3000t2wj9zSV7RJ3yCW-UjpzyiFsxX6PIOsnOSeteksBf6vU44yYgyxJIphacqGrTzmQWs3ZUT6KGkCBr0iLGoptjaHAs3UnjTf_1tgiLizVVoeSnfzKUfwYA0O4t6nolVXiQe5_50rram7vGET0rF6PqYUxbPho8q2tdjZNFzgkYAI91u3E4nJK_I4Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزادراه تهران-شمال یک‌طرفه شد
🔹
پلیس‌راه البرز: با توجه به شرایط ترافیک سنگین، تردد وسیلهٔ نقلیه از کرج و آزادراه تهران-شمال به‌سمت مازندران یک‌طرفه شده و تردد از مرزن‌آباد به‌سمت کرج و تهران ممنوع است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/444231" target="_blank">📅 11:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444230">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urcyV48D0gKMADZv4aJLBVAfbWcGIb16x-ODuVPBm96ZArZ4RyFrk09r9tyzT2M5qYOnYs1dBsTAF2DriCin3uNUs9iTz2Em5pIzfxAeTn8KfGitZ_J0AbIlrE-WvrVuUlYT3Zti5foF7ppNh_KG4Ax60757Et7ObdUbTsdX2yXgPNwUPOLlC1ushpgNb6RebLX65uN9Vbxtyh8TR6KxubN4IjmTrO0NZGRZDtgmvrt4q_e_IllKQqqv9XzWznldhQWoNMAZyBLmfV2dPBXLglOWYas2GOC8Y3wVvoBwQ18Vjg-amkeOvkzBDMu8RTRjbfN54BnVLl0tD9BVseANcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز جلسات ایران و عمان دربارۀ مدیریت جدید تنگۀ هرمز
🔹
هیئت مذاکره‌کنندۀ ایران پس از پایان مذاکرات سوئیس راهی عمان شد و گفت‌وگوها دربارۀ ترتیبات جدید تنگۀ هرمز را در مسقط آغاز کرد.
🔹
قالیباف، عراقچی و اعضای هیئت ایرانی همزمان با سلطان عمان دیدار کردند. تنگۀ هرمز و شرایط جدید حاکم بر این آبراه بین‌المللی از محورهای اصلی این رایزنی‌ها بود.
🔹
آنچه از روند مذاکرات برمی‌آید، تأکید طرف ایرانی بر این موضوع است که مدیریت تنگۀ هرمز و شرایط عبورومرور در آن به وضعیت پیش از تجاوز آمریکا و رژیم صهیونیستی بازنخواهد گشت و ترتیبات جدید در این زمینه در حال بررسی است.
🔹
تنها جمهوری اسلامی ایران و عمان به‌عنوان دو کشور دارای سواحل تنگۀ هرمز، مسئول تعیین و اجرای ترتیبات مربوط به عبور‌ومرور در این آبراه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/444230" target="_blank">📅 11:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444229">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">چادرملو در آستانۀ انصراف از بازی با پرسپولیس
🔹
باشگاه چادرملو هنوز تمرینات آماده‌سازی خود را آغاز نکرده و همین موضوع باعث شده تردیدهای جدی دربارۀ حضور این تیم در دیدار با پرسپولیس به‌وجود بیاید.
🔹
گمانه‌زنی‌ها از آن حکایت دارد که چادرملو تمایلی به حضور در…</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/444229" target="_blank">📅 10:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444222">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BTmQvSfatbnVLRlhG6NMVaa5JNXXuokbx4Udi_WNfk35vS0SrsRbLm3SuXcJyIg5x6Y4oOlMT0DUqrELo9Ee2-hmDt8nlEGV6JyEl4fCXRfWP2HCmlnio5iYg_jucFCDUDpaRQtQPYZTiWxTn2d2qkWvwmvNGabDBsOZt0mLXWJ0GiSs5bLMWPDZGOdIyFeUHWWXbOHMzJYn4_voAB3HOlqW49rWZsCWgLWOEamtDxzHER8FpK3h8Ayp8FE1EuDE8buU-5oVnCkP-nUSuPnDeo_tF6Wt6IlbcDr341s-Yrs2H3cEqR2XTmFuesvBrfh8Z_GQO_SV5bBirA_vyssNVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HAN7uYBc4ueYObuZtyF4SW5JK9265w1_-K8cygizfB4fQ07nKCN71hvt3rOwpPRsTQO_vbNjBS0XnZwB8erR8g6WK9mTHczAblihXC2KguGncYrhWNwtmN8qbb780Ynv-9Yg8gsnKCGm1rJoz6BZWMIP62uDggt97NHGeIk-kfX7yRK3nFOKMNDK3NMPLFDO1eCPu7vVMF7rAcjJUdkPjcgjywbtq92HsIY5TqwVPY1NU5ogGHsRVhhCTFaK20n-yq7ENKdygfOvUSpQdqJV6B49GEdGlHOTsq4-9s1F-3maZBPLcxBruYYIX2Ce64sS8z6fx5pTcb6HjbxLzWAfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMx1UDY8LT_F-8w7GYjbFTTGpXAc69YmtbxTgD5lokzU_Kb6pVr6odDWrGNsUwtiCP7_UR_KQnIh87l0TN01rCx4nX5DpP4xVgDfGhDRRVGI8ulGovqsJ4fH7CF9e8kaYhdjx_LtHuAfBXB8WdX3m24L8U2d72--RprvziHZ5ncLxIcRzCX0XQd9Et7JCSVtgjEAfpctX4k5RBeGCqQURKaEDrV6JBhJJg5EJkT2VnyMfakX2AatKtzJtLG5d9R3pb8iCYox3O2gSpZCcjnYfS05WfH-YA-DWQ1UD45M6rxcANeUnQ42ohvp3_WFYODFHKFH0ovP2QabtM4eUkbXvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJLujWf5QMpoID3onU17fa5V-ChZEftT7f21dVtFqd2Url06VTql6a1Ft1yf3dfrZl_UxViuW4C04fOs2i-UsT3OPy56gIaH22k03f-TjFUtK_OY6QpMj0takzvXHl_WbIvC7JDuedgzVm_xr_Pwvg3eMEn1YSZPE5B0DUPMPQgEGJGjoqi2dueJZ5Fb8LDh2PVm7ZBfBgoPbAFx9W92lC2XBcQ_ZtVPCaHeIX1_d7o6rPF9T7ru6g1RB9LghfUlc7hyaCJDwS-c5zmY3Hi8TJMIR7RYXsPcWxoEKXpKxhbThc78H-VYtVUdWf5k7AlLqKWZNljFUD9J9N3xFFzlwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lb_l_84ZBYhLWnbmPTv9a5vqkXzlh3WLuKEb89Zx4xRkcyUg0nfk3TlTtgj-LozgIKzoIejVT8CJwRZm8JA4skvj076aK6JO9Dp2XFG0GYslc-Mms4G77gjYez96v3JezgGgCs58z8TLsTaGL15GNeuVEcecZ-83gaanMQq5jl3nw9dlLtIT5vc7nyQ-2AQyGkKsMcOyPcbWSxY06Jh1ZwIwR_HDmqwfDOOF8jGXjgLwX2hn3XT-vKYGDG4Wm1fyvWrsowtMmBj16zKpGCDay9RFGgfOAwfK5VjYK0ngGgtKO7C3eRjp4Upt1MiPNvADL_2qFXn64rGSHuYpLQRCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CRCJFmOlzQteNt-o6obbFPfFVSH7D0kJoGNOHHOrR5WxrE8FiyFQFLklpZnmRT4eVRBcT7ixKo6xoFSLLl5vSMZj3QA3JcdwhdN6OvZeeh_UKtmuggRALyW_yZE0oa0W_n10LK9vIM2XuxqAWlm-YO-2vspzAo1APeNWbdUKAipmHdfaEMNZN1wi-dkPag3Ts13PM-cPrRGtORKwMMf0QqktVuxahRfysG3e3VE9RbSi2P3AKReZFsJTyO5xESx3Ihi6_fcgBCYKTQf8UlIZZ6z3ESU9bKO-S0MQXOEOdOkMp3utVp-DcyVkQ_RGh7HD376538aBOJHpxsNpFF-tcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YeC49fujz5q-P7Q1kp6QBO76yxCkCZD3JOPPHY0Ljl6B2lk03knsLgbiCvtj9KeV4TwK8Cq93w-U35ouskKyhdyjanK2DtNbx7eAxMv-tu4UhxSx6bIforbPayyEmNGO5kX7X5NUkKm_mnC_KRMV9LTG6fY2Jdo1YQpGqIkck_C-IxGulG5QuOex0P5uVAiTnaiH7FW03c_G0lQUzx8LDoygmctvDPhsalPzWFZMJbKjkKAE6seKLfr90HbkoUZvKLMlaHUwzvvz3XzMUvSz5o60HrIONyjadTkcQCvvd2Tm6D2fDMXokArWHPP7eKbEozswukbwJ_acVhQENeH5NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین «شاه حسین‌گویان» در باغ رضوان ارومیه
عکس:
محمدمهدی فتحی
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/444222" target="_blank">📅 10:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444221">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUW9fpvwJT8boHFn3zoyN4RMCWaVu5YXdkGugMnNyA_M4g7arhwTDRJPxZ5MLQB9fg6nTajBOepkcLj7kp7Pi4IJxWaKCedUVUFR7FfkvJLUbeaazMEDDRWHJX8ris59NiedewuULWrgmqhXOTRDPosd3kTkfGyLW03G7kP_l8pzGurRosfOv9XH7_bAIbILNFPmnK7nCn4lZOO-T9IxcA8re8mBVrFji_DkpTRyQouUUjok2w3qlP6spaDEGsXaBUq2lvIzcE6sXDZorVCDMr3c4aFdA_T7S8Rnqbone4qu5KgTlDTMci9VDtVyQR2GnNLZpU5QA5pddniRY6SJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ مدیرکل روابط عمومی دفتر ریاست‌جمهوری در گفت‌وگو با فارس: رئیس‌جمهور فردا به پاکستان سفر می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/444221" target="_blank">📅 10:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444220">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKYagInETz0oLE5l3_8e8qgLqdtgbOsZzYzxHCQhMoE2E9Cn31FKH-wleSwxqsO-PBgdCLgpNLMQ3f58NTABkeWS8zUvKyZumztsuaeFLgR0KRFdJsIRBCSHcTkDAzpFxX5TIpVocQz2zuTOXJoJdWbvKi29JAfFX_i5C3F8Sxj0HtDLGOJO5tReILAnWDIaHAnViAHA_bqwAPteb2SIj9KXf8VSAnQDjzhZFUu78ei7FYcu6_aA8Og1_SWf8Z-Mj57R0nTB_ep92NrolpcmXyO3an7Vn63q8ZdLrHza4RO-U36_wmpHutZWztWRKpcdw9l60sirIyp2OevITZKRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز نام‌نویسی در سی‌وسومین دورۀ آموزش‌های رسانه‌ای باشگاه توانا
🔹
زمان ثبت‌نام: یک تا ۲۰ تیر
🔹
هزینۀ دوره: با حمایت تشویقی و فرهنگی خبرگزاری فارس فقط ۵۰۰ هزار تومان
🔹
سامانۀ ثبت‌نام:
tavana.news
🔹
پشتیبانی و مشاوره کارشناس باشگاه توانا: ۰۲۱۴۲۰۸۲۹۴۳
@Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/444220" target="_blank">📅 10:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444218">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GqaEkkOgPcAVlfDFyNJh_cOYfpN-5HlgK2Wa5iPO6lI6Lp2pyQqBC9Ndh83OYuvny4eUnJY2kdltnNCK1Y4YtH_5vUH3NHkr_hsGqySsI8Xw0NrlWE0xsx4SnzjRFyN3GJ5RcKgceMfOt2gHHqLOXg_EkyzU0oUI5MfYtRpYusUCZA8cEK4cLep77IqeI2HaL88IcMoJY7Ezc4VcZexZqhDHtUFqop-asr1Jd09YGi893bYZSl5E1mKEHR-V04KHtum7g4EnTuxot6Cnl8ovW6CYMiW9T_nKx6nu_RjMhwQ8S4VBzVIbKWUpaEthjOt_rvJC0Fq1eLyVI0qhQ2Wbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efNh5mgoQQ_E0v8HGXNVTl9x5whuF2ohVzWxUZbSRcegLEidDEWF-HYcUbXWT-TpfEqpIiB6oIJ90rJnUl9Z2BTNX-okBxF7KMmEHTA0Uh5hJmsH7ZST6rzFooojOLBoel9Gy-oQR5qdDSMzmD2eUFh-q0FbtW88DoqBrQU4F__C1o5RlAgSOaE9HtpNVHJfEW6mQ4WVdDiOVSYxNdQKBs2ev8uL5L-oBncaqIVT-BVALLh-gtjJQYiGa2GpoSqizhDv3kwuW_kA21VKcL9fQLQqiSLatwZQyHYviIZirmjtsPYqQqqjjvPDGNQRIChyOpt5hekHrDgdnVZWoFCGMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۷ هزار دانش‌آموز خواستار تعویق امتحانات نهایی به بعد از اربعین شدند
🔹
کاربران فارس‌من در پویشی خواستار تعویق امتحانات نهایی به پس از ایام اربعین شده‌اند و گفتند: با توجه به حضور گسترده خانواده‌ها و دانش‌آموزان در مراسمات و پیاده‌روی اربعین، همزمانی امتحانات…</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/farsna/444218" target="_blank">📅 10:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444217">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5CvYzFDhXxi2WbQhMWUkpPreKOKr_glIemak7DDycfma3h3Gq9JziH5yu9s6f_8FyJ7X2Dk3FI07hBhIZLB8OqPDLV4UiA8ocnnONCjdWtk_iKGTzk3pIIlc7-qNgxCzON95K69zx6yrnhoaWANW2FzzA5_0i8JBimLAfIpntOFhnHQPq1uApxKuWiFimr04kmASGs38efOfNPtdtavQ-IkMozE-wIjFZwuMbDUkj3MHOcmg7WBu5oq1Jlb4iI1puXbWFIVc77M3CcE_oLNYfgFAzYHSkeMXhbq3MTcNsGQSggKUlc6o8MdB1xYVfzrpCqpsPZeUjeE-hNJoyursw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشت‌پردۀ کلاهبرداری با اراضی جنگلی به‌نام ایثارگران و جانبازان
🔹
در روزهای گذشته انتشار اخباری مبنی‌بر فروش غیرقانونی اراضی ملی در منطقۀ تکیش تنکابن موجی از نگرانی را در میان شهروندان ایجاد کرده.
🔹
این پرونده که به گفتۀ مسئولان توسط یک شبکۀ سازمان‌یافته در چندین استان کشور هدایت می‌شد با ورود قاطعانۀ دستگاه قضایی و ادارات منابع طبیعی وارد فاز تازه‌ای از رسیدگی شده است.
🔹
ماجرا از سال گذشته و با انتشار تبلیغات گسترده در فضای مجازی آغاز شد؛ جایی که افراد سودجو با سوءاستفاده از نام موقوفات (موقوفه آیت‌الله مرشدی) اقدام به فروش قطعاتی از اراضی جنگلی با قیمت‌های بسیار پایین کردند.
🔹
مدیرکل منابع طبیعی مازندران-نوشهر گفته این عرصه‌ها جزو طرح‌های جنگل‌کاری بوده و به‌هیچ‌وجه قابلیت وقف یا فروش ندارند، به محض اطلاع از این موضوع، پیگیری‌های قانونی را آغاز کردیم.
🔹
با ورود دادستان کل کشور و همکاری دستگاه‌های نظامی و انتظامی، دفاتر خرید و فروش این اراضی که با عناوین جعلی مانند ایثارگران و جانبازان در مازندران و سایر استان‌ها دایر شده بودند پلمب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/444217" target="_blank">📅 10:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444216">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">رئیس شورای‌شهر تهران: تصمیم داریم رایگان‌بودن بلیت مترو و اتوبوس تا بعد از تشییع رهبر شهید ادامه داشته باشد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/444216" target="_blank">📅 10:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444215">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f1b8581e9.mp4?token=k520yZfCVaGhvcPkPWZQkjLkMjr0dax5zEmosI6m4SIkOXKD87Vj6sG6eHHdAFlYJn49fQDlIjJzUI82wMioz4Ta7C6Fso2xB1ClaPsGZgtfeZlNVv9fM8Mg_wNmbOBTd1ExxsW9SDjVfGdFLjodUg9nqgCJVHUqDlkA1y8YB34NvClMBcC_kDKEAtcql_pxzF7DXfgYqgzBCk8qQaGq8-pj87LLdPO_kYCyAYI_sUBIekRRiuFtArjdqlyfCa9RPV7df-fECS1tdT6gspkB7va0dUmxCIb8P2JRAx6q852bcGVVJfk8fC9ituKghoZpOYgg6EXDUAbSldXvypTeIGkAAe2hF5dDSL9K4lF_cbdcS7KYp4esmAbTt49YydbEmKH45WkK5fIhOuYelxLOxojcEmc1oEq9GFrtnpJRgxEm9zZJl5TT4i5OBwcKNYO1hqHYF_VggWSKUSGloCnsS9bDvRzadwgAnAdSXXU0ZJy2OYGsZPLpZZb6nLSxS-PlcvvD6lW4S_am2586wsMzabeERebuRhscfOiI6B7NyQQJnhGa8JTAWVIMMi6uaxCQAnY-72wx5v4fqL27Mpb2cKVbnxSdGmKw3ho5uebCHRzDBoMBPJWiGQ0LRoOQs2Z7wMi3iswVh5S_VnKUbYZ_0_lQlgJ0-cY30r5FdICSsAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f1b8581e9.mp4?token=k520yZfCVaGhvcPkPWZQkjLkMjr0dax5zEmosI6m4SIkOXKD87Vj6sG6eHHdAFlYJn49fQDlIjJzUI82wMioz4Ta7C6Fso2xB1ClaPsGZgtfeZlNVv9fM8Mg_wNmbOBTd1ExxsW9SDjVfGdFLjodUg9nqgCJVHUqDlkA1y8YB34NvClMBcC_kDKEAtcql_pxzF7DXfgYqgzBCk8qQaGq8-pj87LLdPO_kYCyAYI_sUBIekRRiuFtArjdqlyfCa9RPV7df-fECS1tdT6gspkB7va0dUmxCIb8P2JRAx6q852bcGVVJfk8fC9ituKghoZpOYgg6EXDUAbSldXvypTeIGkAAe2hF5dDSL9K4lF_cbdcS7KYp4esmAbTt49YydbEmKH45WkK5fIhOuYelxLOxojcEmc1oEq9GFrtnpJRgxEm9zZJl5TT4i5OBwcKNYO1hqHYF_VggWSKUSGloCnsS9bDvRzadwgAnAdSXXU0ZJy2OYGsZPLpZZb6nLSxS-PlcvvD6lW4S_am2586wsMzabeERebuRhscfOiI6B7NyQQJnhGa8JTAWVIMMi6uaxCQAnY-72wx5v4fqL27Mpb2cKVbnxSdGmKw3ho5uebCHRzDBoMBPJWiGQ0LRoOQs2Z7wMi3iswVh5S_VnKUbYZ_0_lQlgJ0-cY30r5FdICSsAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ستون‌های عظیم دود آسمان هیوستون آمریکا را فرا گرفت
🔹
آتش‌سوزی در شهر هیوستون ایالت تگزاس موجب برخاستن ستون‌های بزرگ دود بر فراز این شهر شد. هنوز جزئیاتی دربارهٔ دلیل آغاز آتش‌سوزی، میزان خسارت احتمالی یا تلفات انسانی منتشر نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444215" target="_blank">📅 09:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444214">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تست سامانه‌های پدافندی در بوشهر
🔹
فرماندار شهرستان بوشهر: امروز از ساعت ۹ تا ۱۰ صبح در رأستای تست سامانه‌های پدافندی و دفاعی در محدودۀ نیروگاه اتمی بوشهر صداهایی شنیده خواهد شد و جای نگرانی وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/444214" target="_blank">📅 09:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444213">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPtLbxm2fqEFffym7aLSIv7LmTmLcBtN-4kp3XN3ImGGb1oORI3in5-dBjylogyQ9yp66UEo8Bl4PysxeND1mMUZDmXufwoHfmJXSeB1L_mDdkNUcK4WZelUnPFRVpkpwJUhhUSHgy4ZKA_hHeXi-xKAZOr6ujd8oryuEOp1Yk4oY1XVMc6Xi_1K_tMBG1qcjGTHZs3DL5KHbpQ3VNPfTqL_5ospseeD3OeyFTbRwNzhSAMq0xSRF57oEG4pBfT-5ysFWIBvfv-YkK3HqQ1-oYiXHW98QdQBR7H-i01imF7CXpU2FUMzlkdv2iaiMC0gSyBP2g-xr_gWZweKK8jkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرژانتین با ۲ گل مسی از سد اتریش گذشت
⚽️
آرژانتین ۲ - ۰ اتریش @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/444213" target="_blank">📅 08:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444212">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzYRTHGspq-o5KhkPHAHP0NG49JsnV8kI03FU-U_dHD6cWWeBr--ZI9x1oMjlDXzc3uLaB9C6W6aIHF7864gVReVGNCxoRRAl1TQ-ymwSrGlHF4lHfSsDiKLKM7KmV5l7rOkda7yrHDbGhFB7dzAj3iJCgo6Z7F5_3AQ_KC4F7xIezNnSLC9odiXv7UUnhc2_jBQKPuV_bD6VaFxrksocvFV07BW1RxwmQWlwaySZGxmbbeQp-TV-hxCIqDkqacyyJJJL6AT59bSOLhCobtq1A0O64DEdz5x2xS0m_j50W4W_DAEXtT1poBJuSKCbHe9WkjOrYEpFLc3D1NZRY9ZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گروسی پشت در بی‌اعتباری ماند
🔹
در حالی که برخی مقام‌های آمریکایی در روزهای اخیر مدعی شده‌اند ایران تعهداتی تازه دربارۀ همکاری با آژانس بین‌المللی انرژی اتمی پذیرفته است، مقامات ایرانی این ادعاها را صراحتاً رد کرده و بر تداوم رویکرد مستقل و مبتنی‌بر خطوط قرمز کشور تأکید کرده‌اند.
🔸
محمد مرندی کارشناس امور بین‌الملل طی توییتی نوشت: ایران قصد خرید کالاهای کشاورزی آمریکایی را ندارد و هیچ بحثی در مورد آمدن بازرسان آژانس بین‌المللی انرژی اتمی به ایران صورت نگرفت. تبلیغات غربی را نادیده بگیرید.
🔹
اسماعیل بقائی، سخنگوی وزارت امور خارجه نیز این ادعا را تکذیب کرد و گفت: تعامل ایران با آژانس بین‌المللی انرژی اتمی طبق روال جاری و منطبق با مصوبات قانونی ادامه می‌یابد.
🔸
ابراهیم رضایی، سخنگوی کمیسیون امنیت ملی مجلس هم در پیامی صراحتا نوشت: گروسی را به مذاکرات راه ندهید؛ او از سنتکام نیز وقیح‌تر است.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/444212" target="_blank">📅 08:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444211">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaY9DGnsODutXkVmVmbtByi9BrcRoAzuGknbRlpXq5bH6Ph5OM50_pllhG3NJWm8qdlIbYEedQy0s1c9lH9dWxaHVu4fgi5i74b8Aysm6cUaxChmrSUZrO8NG8QWGGcDHpNC56qQm-UVePhigwRY6iJgQfQdhu9ATsjJyBr8tPN2-BrUfgC7ofJcGG8Uzwd0HvIrICLhU93vewE-103WXf8JdUvwDNMNw2YVu1TN2qDd8oB2Zesuk7zY5Nh1aNJDotSe1rSP_tIihUSUgBnxiEPXVgOs84OS5jn3lQbKndvy10_ofI2uC3Odr-09-pHODgbWEMOsH4SPww6tSFk7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نان در تهران گران شد
🔹
طبق اعلام کارگروه آردونان اتاق اصناف ایران، قیمت جدید انواع نان در استان تهران به شرح زیر است:
🔸
نان لواش: ۲ هزار و ۷۰۰ تومان
🔹
نان بربری: ۱۰ هزار تومان
🔸
نان سنگک: ۱۵ هزار و ۵۰۰ تومان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/444211" target="_blank">📅 07:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444210">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0c191c12.mp4?token=o1um1AYpIFqMXsn31Gr9bB-5Mzj4s17BYfWUidex3zcmm30Ut1HHCwLpivC3_uuLIQw1nT0BzuKWguAMkXOFeyss_rMhEf_7cBYCxQ_TnI7JY_DV5GZrjMkfqf87KVrO5-L_QTG1oLe8f57YnxUMxYAKmdgWbrokjPzdt85XEzGM26UJ2b8PUV6EXP_vuxR1RaNAgCl48gTaQuIwZ7jECPDUeTlcUOUvWVmTBu83P9MuBLTCyoDmAppoOiXesHtmmP3FOsBuE6Px9uWv6aNbyEAP__vpu201PoNNL90eKCUMc5SbK9_Y-UhGirAXy7tEGneQ8emkS0x-5wD59GRAUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0c191c12.mp4?token=o1um1AYpIFqMXsn31Gr9bB-5Mzj4s17BYfWUidex3zcmm30Ut1HHCwLpivC3_uuLIQw1nT0BzuKWguAMkXOFeyss_rMhEf_7cBYCxQ_TnI7JY_DV5GZrjMkfqf87KVrO5-L_QTG1oLe8f57YnxUMxYAKmdgWbrokjPzdt85XEzGM26UJ2b8PUV6EXP_vuxR1RaNAgCl48gTaQuIwZ7jECPDUeTlcUOUvWVmTBu83P9MuBLTCyoDmAppoOiXesHtmmP3FOsBuE6Px9uWv6aNbyEAP__vpu201PoNNL90eKCUMc5SbK9_Y-UhGirAXy7tEGneQ8emkS0x-5wD59GRAUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گردباد هولناک در روسیه برق ۵ هزار خانه را قطع، و ۱۵ نفر را زخمی کرد
🔹
بر اثر وقوع یک گردباد عظیم در منطقۀ سوردلوفسک روسیه، ۱۵ نفر مصدوم شدند.
🔹
همچنین این حادثه قطع برق حدود ۵ هزار خانه را به‌همراه داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444210" target="_blank">📅 07:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444209">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNhDDwDYgBp0C1bIr64QH9Ck9nMSuYJwRqJG2y4vhKt9fcUzALyhpk6YOZNSynlPbmpTZVC_fAR9hP-OP7QlNu7fbzITSu5CsY8gCBtHKcIxy33zFsMm2BHvgOHA0uhiI-sDfiGm5i645y6F8krHoLAJB3vTN5EkfFqHZqBOK6sAdG5dvclSCEpzf5WpZNPxh712mBM9hO72-QsMmjzoHRFJHcAofj-WhmU7DMHYMbsVhqcd1ppXY15MdT3sxjEAn06YjEJuMY7aGhtsgolaMqp0VI8DEdTCADH1ESVSb0biI2CWcZixfrRbZazEob-jfGDyB_8XcEAC5irxCLlo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو هیئت‌رئیسۀ مجلس: صحن به زودی بازگشایی می‌شود
🔹
سلیمی، نمایندۀ تهران: با توجه به تغییر شرایط، آن دلیل ابتدایی که موجب می‌شد صحن تعطیل باشد، دیگر منتفی شده و ان‌شاءالله به زودی شاهد بازگشایی صحن خواهیم بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/444209" target="_blank">📅 07:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444207">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMPoE6WuZwHMQeFsKMxvs6_T5F8kxqEK3V7k1EB-W6CpVGH1DQGQnJE2N5syvnFMstmyiCk7t3RDYuv-IZ9NgWhrZ95GqF-LvS7VJ5QLEn2kdJ3KxR9a5vB-291jzZffsudhUTrILw5MRl-F3TWkQxgmkCZ21KvqwpgMwo6yumLeg0GFNG3QshdUw5ErX81nZCMFWiqZknTKMJo9vzkfOPP2ma1MRbxW3MPJqkPHeSa7a_TcE6GXfkq8vfXpyawxjRmewtlrxH4eR5KCdcHNABri-nqhAUbRYgC-FFTBWvsxzQJONkpSNk_-nw1rRBNfCI35WflDib_jR2JVCj2y4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تشنگی آغاز شد
🔹
روز هفتم محرم سال ۶۱ هجری، یکی از تلخ‌ترین مراحل واقعه کربلا آغاز شد؛ مرحله‌ای که آثار آن تا روز عاشورا بر اردوگاه امام حسین باقی ماند.
🔹
تا پیش از این روز، با وجود محاصره نظامی، یاران امام هنوز به آب فرات دسترسی داشتند. اما در کوفه، عبیدالله…</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/444207" target="_blank">📅 07:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444206">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nOdAdDZCUCLtAiTeX-mLkWbFIo_80I1lOFRugtBOW1A70SvvgxNGlNdtC7I7DXHQk6KUNYkEkidCy6gsbswzz1uP-6uvm3p-EnWwKFxS0415EDeiHJ2xxLfbZg1gnuFswfNfM1hfkC7I_poIcoTTLcZLMPJYd_HmxqvVGZ2LBj8vrHH0oGaMLo8wHBygKjlS3APfC8ldQT65pxhRHg49TC5tJFN2n5OEEI9B5qW_XZv5ba0BZE2_fR7-SBi9n5lr8aqs3OJrlJMUxIvRjhVW95kPQjodRHa3w9gEMdyuGNtzKp5Ur_0_9LPgV8bGVU02Y0sUYkCAvIo_0qoESiWkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول‌تیم‌هایی که تاکنون صعودشان به مرحلۀ حذفی قطعی شده است.
@Sportfars</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/444206" target="_blank">📅 07:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444205">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyTn0Et2_V_49yIRM0osdO3z32s8qIcdtbEIK10Zzr_bdNnsClkQlwGJ0OKLgPfApQiOpS3VDN6SlPAJg5tNA_Vj-ulJiyXHV0RQ5_72uwmwmvfcpmIPAi300utZ39J_9dpKEWHXQmOZo-L4Z90MoOJg3xQU6bXEp2q2DyYtNfRq_6BKT5-qUia5__TdlFoPzS7nsPtqRKVWE8BfAWBnAVf8TpjyyRjL4crqE5ncBO7XOb5dx0nsmqp_aIxK0Jm_ya1H0orYlItg_7K4KE1QeUYi2FCwedjTYopqvdQlfkg_0rSqZjr2mHPPJ-fBfx5-ZuV1PWNA2Z_N5pLTxZYGGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چادرملو در آستانۀ انصراف از بازی با پرسپولیس
🔹
باشگاه چادرملو هنوز تمرینات آماده‌سازی خود را آغاز نکرده و همین موضوع باعث شده تردیدهای جدی دربارۀ حضور این تیم در دیدار با پرسپولیس به‌وجود بیاید.
🔹
گمانه‌زنی‌ها از آن حکایت دارد که چادرملو تمایلی به حضور در این مسابقه ندارد و احتمال انصراف این تیم از بازی مقابل پرسپولیس دور از ذهن نیست. هرچند تاکنون هیچ مقام رسمی این موضوع را تأیید نکرده است.
🔸
این بازی برای تعیین حریف گل‌گهر سیرجان در مسیر انتخاب نمایندۀ سوم ایران در رقابت‌های آسیایی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/444205" target="_blank">📅 06:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444204">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8416b335.mp4?token=MEmxI2hX94QvYqGJh0WvdhUIzPwDP13QPvymXhSWbAaPlqtivbuSui6AXvC4F5sSTFcAq2krG0kzuqggcp0ZleBQ2oAkGn4yijxdutAY1JyGsF4-izX7f7zfPdudNeliGxmnyTbH1uOzv9ZOm-0LBsE5l9T4Sphk4ZRFpnz69fFZAFFiiKbZg-VlxTBt-6HzUZeUmnsNyjKUntMnM42J8YybOc1uREnLDKHjSVbJowhkrwLB8-UmpUwXY-Asi0-46i5aV9jYtu8hWSMix12BGQIX8eyemVNs9dhpIQMXIJqWDm7UgSROmJShBdPuaJIR4zjbPNR_zOuXfq2OfrgU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8416b335.mp4?token=MEmxI2hX94QvYqGJh0WvdhUIzPwDP13QPvymXhSWbAaPlqtivbuSui6AXvC4F5sSTFcAq2krG0kzuqggcp0ZleBQ2oAkGn4yijxdutAY1JyGsF4-izX7f7zfPdudNeliGxmnyTbH1uOzv9ZOm-0LBsE5l9T4Sphk4ZRFpnz69fFZAFFiiKbZg-VlxTBt-6HzUZeUmnsNyjKUntMnM42J8YybOc1uREnLDKHjSVbJowhkrwLB8-UmpUwXY-Asi0-46i5aV9jYtu8hWSMix12BGQIX8eyemVNs9dhpIQMXIJqWDm7UgSROmJShBdPuaJIR4zjbPNR_zOuXfq2OfrgU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی وایکینگی بازیکنان و هواداران نروژ پس از پیروزی ۳ بر ۲ مقابل سنگال، و صعود
@Farsna</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/444204" target="_blank">📅 06:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444197">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqPltEaefDyyhRQ0a2kWPtmBA_Fg9uDSQAEHjk2gfwDMBWmnby68OthhAkBIH1DZhor7AI2gxpwaQc2HXm-jLhgrNe3dqLAoylZGLFRp89choZtvzlvvXKFzd7I8lXihmcfYkw9Eb5U6FKCegI1ylhG96qLxsPB7ti7zYaqvKnXGrYF00qfSa-OSxpkfRojR9_1d0tR5zbY0ZUPrGTfc2go0pT3uYnzW911Ab-5xwP4RVY01oZhsLXxcuhyLkTBmRF2OHsiRxEvfzyghO24kHTckzNhxflbciyMhfFlh00NN9etm9nX3dQmPifk5bWQKKqBDWft2X9e5fnWbdCgiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9LhT1JGUFPxORnFCkGN-A9qgEFFYyiGgHYdcxmPIDlg0B6OavLUEcPgJRTak_Vse327lWDViTlExXK5hGa0R6mMK_96ruESctitjUHXUEaTLo2bVjOO22RkiL7Tp31hQQtT01sKzfeGKoX7c8lRsvn-17ebyqhnaGE8SdqdlYiHkVC1O7iQEI7V6m7Yk5tTDwbaC6DBwZNOX_A3rL5b0KMEAsNDBVZGBHzXaEdYOBzUeNV7pzFD1t21UdOHQDqZ08SD9MqDhwBOTGgeC3LYlDrrUxPi2oVELYGh2Dpir8GS3NLFA7HevrKKZ3J-wkLaVFKnrJZOBmLNPZP970gI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QsjORPd5aiUudovyvwoQ9adEbrRED7_0VrajRk04YasFpUnGSuRC1Q9kelTXb1JWJLgfGN-ZUEEqHb3_RZ81l_7MVoPpZDzFmOV1x1SD2GSI54zptwlIb5k8lmOjngjVJ32rSstBDA8_KMBkpOT6s9BUkqP6N2b3mAS62944pzCa77UpsG66jxVv9PDspz7VzryWz72ayh_JPLlfuIb5mWxANUEVzrXjNNa89VGdv2BNIR3bpCyYm0cU_V99uZtn3shUsfug1ZCwVVfF4JJW3byb4-kWJ6rs4hUdLHqOMSfqwiaevpH9gcD3WxUifi_mzNgZqA5di-uvK9lli9aFuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/seY6eu0clI4DmYR4QdMABOph8Y0swDpDJ5N9BzXpDYzxWkMgACQrOlbdWzSTvKE5CRLMPDP922lyhi7YEdkgjxAp-qmCj4EsVQQ127U8jFRHdRR1BAqLRjfCDSPkkCfclWSaYBJ70-OF5Ohwl2F58fO23S2p7nN5JSpa9wen-NTmbuXwMTFv2PQY3S7-aQAAFQhxFBpyMeQnMe2K05S3lZGwEVtpQj5C13xLE5fBHLGWwF1P9F1KtAXRVAYH4KJXTvFCDbTKFQwn1P8_jExEvF5TpbP823NSE9qL9K9bDfg-WBQ-j3L0hT6QMqa--lCXOW4x_y6kCGHBB5Da4cL8gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uiCbAS7QKLfXoQJOPe1yUulrYcG3cWmLdJISPYM6pL7TJCOh7OFk-XGuXxxiFhQXJOCHkBxLu9tVKO5kqJR6hYivhPzwaCsJfbLeVvu7wnmsOINxxEO8yfYzcoTgGqgdT5swkwVfcNcQk4dvYT2i6U9enCEIdokHiNVFcliO98k16Ycjp5iRCEId8cRpnXiMDT7mDuYBk7-0YnHT1aQB-iUtow4fthZCJnXN4uMjFRV2pfXyuTVKmPNPR6fJcvk8soNGolQZvQk_wyydPAGoMMINdp-4KeKeS3wNEnt9gHnIEdQbIYq5yjw6URRmBYS1ZyhC6aRg93gchpyErysHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SU3dkHFm1pQn88pLxyPGvTkOJMJyaZ5yxSR0kcX4K2r6IqsWeaTvp2Jtfpkc-OG8-XASt-m5KKAJV3mzyrwfR_FIsf_G4fcg4RAfPl96hj71tEWReT6WE5TzTuxQbswnqawUR1gZurO1R3TmupTjrYKjWjsZ0QDZP2HaBv9s9S0FxfaVFk1MM1xEfQ72ZdsbRCp61DK48sgRijggJBPQsx8sq_GW1fNAJOzR4oh_CzQB6xOQtdAlKypyO--4p5KMKhyJ1FvMxTfoVXJiZs7tGVfTsHc5dYQTeB6aw44EfVWj5z71UX4DRvstErhkIJT-s_r6Yu9k1jWOleHzOaD0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjBPrnSUdCCR35dvEmxJiwITSVdqVOe3IT5sXwEh8yHfCcDYEK7H9NKV4hmTijZEUz50By-qRT8_wmqIBcjryB15YDih8exo123c9J5hAPEHZydOzpOxLKukAVRNGBFbMQRZ8HxWBu001favXGFVM9aROOuEQyX47MQdZD-dXBPXTWumLB59oJRl6Fsk61EMRImXb9NbZlZzCdm3S_InibAz7Qp1GZ9iVmh7nG4A72l0UQDE0szRs2QTbpWcsRQhSJ2fxPmFwdTyJh99aj50YN9avjeg9VWpjRWKUjESWZejfns82mej8LmaLAwmFF3a1wXFWnjVMpt3r5ys_oLQ1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نذر حلیم خمره‌سفالی در بندرعباس
🔹
پخت حلیم در خُمره‌های سفالی سنتی، آیین اهالی فین بندرعباس است که محرم هرسال نذر امام حسین(ع) می‌کنند.
عکاس:
رهبر امامدادی
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444197" target="_blank">📅 06:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444196">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبر خوش برای دانشجویان دانشگاه آزاد
🔹
دانشگاه آزاد برای کاهش هزینه‌ها و جلوگیری از سفرهای بین‌شهری دانشجویان، امکان برگزاری امتحانات پایان‌ترم دانشجویان غیرپزشکی در واحدهای دانشگاهی محل سکونت را فراهم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/444196" target="_blank">📅 05:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444195">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBC85v-B2XUijtpkk4-MGkhVazya4uZONDndeyjYjAyexRIlXGM82ziwMt6PcAwhbs_bbESe32KL7OBcjy2UVXWl6kHmlat37jWuhPnXgl46xqfzBeWXNpjsE5e9jyF7bWmkbLlhvP8vuPRu60K8aYF_E0mWzczuzJhfclZdoq1x5t7oncC71HFeqLsrKllp7IbZ04i0mLgSIfpcgcfbR0jIZcp2shSmgT2x0PREsMUVjrN12mn66nyZ29zbhgtOwVpeksb0NsNOXTSIhuCp7a0f708y41DS_2Rfkz-kb3xIMrxMsZaEEL-XWQHuY1GztFfgM1jM7ZaCjd6CVM234g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهارمحال‌وبختیاری؛ بدون دریا، اما در صدر فهرست غرق‌شدگی!
🔹
در دو ماه ابتدایی سال ۱۴۰۵، ۱۱ نفر در آب‌های این استان جان باختند؛ رقمی که از کل آمار غرق‌شدگی سال گذشته بیشتر است. استانی که دریا ندارد، اما رودخانه‌ها و استخرهای کشاورزی‌اش قربانی می‌گیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/444195" target="_blank">📅 04:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444194">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha7pKrR7WKZMRS9nZswL4l4TjRriqNBYVf9fkWQJ4fRnPU1ADILn4SulwsDEcr9G_zt5wFSfzV3-T_X5PIvQPx9QjvIhB78aDzqB0ELcsu6kQOsf2FkGcxikKmZCERLA6_FKY_yT0OqrmvDlEr9G8Prs16b-Q2tRUgUCSR-nXOQgKjPWifQ7GcPh9_tO-0uYtnXvhuqnl6bo7eTpOJ1TfGok5kUZSTZYbkfoxmi3kwhcGrphwEDGZFQNpzCQ1pR-nNGfkPlBrqu_UmyUGjyFNC8evMGoks5Tbd-lERSzOMw6G0Vtf0EhdE0Ye7AxzK9unK6w1yIKWeXLcCjtIRVfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسوی‌ها با سه گل از سد عراق گذشتند
⚽️
فرانسه ۳ - ۰ عراق
@Farsna</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/444194" target="_blank">📅 04:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444193">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c7652da31.mp4?token=Me5p7zLK6y_k1h6YcvKW8jDtZhly36oPhW3DmL1GKzi9UZZBsEQJdAFOHJhCS0PKD-zSh4BvQpqCR2c55JjLCHjp9gmh_oQIumatzsc5Z_67T2r5c3HQqN48wgMHclWWtcicBACH4K_AHKZiWNNipv1MtOR7mJYwh7dUI_2l1vQBgm3qqyF6Z6-C8gCmZYdq4cP5aicpJVYu8bkIRvAJYUjFNFkgn0ltUkOCCnV03tkjj2m_nfiS_nPUnfMRfs6Qz4AbABj8BBVL8w1cD-_4uRGsSllIbtrXKRiHITal_RPUYPozX2Ahv0syW825H98R9WNGWG66SbGxOzt3Hen4xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c7652da31.mp4?token=Me5p7zLK6y_k1h6YcvKW8jDtZhly36oPhW3DmL1GKzi9UZZBsEQJdAFOHJhCS0PKD-zSh4BvQpqCR2c55JjLCHjp9gmh_oQIumatzsc5Z_67T2r5c3HQqN48wgMHclWWtcicBACH4K_AHKZiWNNipv1MtOR7mJYwh7dUI_2l1vQBgm3qqyF6Z6-C8gCmZYdq4cP5aicpJVYu8bkIRvAJYUjFNFkgn0ltUkOCCnV03tkjj2m_nfiS_nPUnfMRfs6Qz4AbABj8BBVL8w1cD-_4uRGsSllIbtrXKRiHITal_RPUYPozX2Ahv0syW825H98R9WNGWG66SbGxOzt3Hen4xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سوت‌ها را چه کسی خواهد نواخت؟
🔹
هوش مصنوعی، شگفتی بی‌نظیر تکنولوژی، حالا رسماً قدم به مستطیل سبز فوتبال گذاشته است. آیا سوت پایان داوریِ انسان‌ها به‌زودی توسط ربات‌ها نواخته خواهد شد؟
@FarsnaTech</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/444193" target="_blank">📅 04:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444192">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4df6f5ff3d.mp4?token=JdAUYmd1ZKD_ws0gzTPkMjf9Yz9RQX2XjBIY8kRp8k6OrxTz4DDO4oybQcsaWjym3aHuBIXc2hVrnTDTRzjpWpD-pjs_vgR8FkrLVUfunO5CfOFEFAx1TrN-ZwAkkvcZEmwRWPWcIYHlMQkUliU007jx2C9Q7ZHo0-NfD9DpZSPnEY9_W6v5uKmyGb3jGO--IgYZJAnB5JlIMrdS8cAyryhNR9axeCrqvio8-CVrOxj-0WXCCIItEuHupcaobuTeL7jrg-CJWFlO_z4_BHrQvGAoMo25JySplxuDmK2TS_wnvZVgePSRBHKfwk7TmaxfZohLGJtMBg3BRv9qcPIYoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4df6f5ff3d.mp4?token=JdAUYmd1ZKD_ws0gzTPkMjf9Yz9RQX2XjBIY8kRp8k6OrxTz4DDO4oybQcsaWjym3aHuBIXc2hVrnTDTRzjpWpD-pjs_vgR8FkrLVUfunO5CfOFEFAx1TrN-ZwAkkvcZEmwRWPWcIYHlMQkUliU007jx2C9Q7ZHo0-NfD9DpZSPnEY9_W6v5uKmyGb3jGO--IgYZJAnB5JlIMrdS8cAyryhNR9axeCrqvio8-CVrOxj-0WXCCIItEuHupcaobuTeL7jrg-CJWFlO_z4_BHrQvGAoMo25JySplxuDmK2TS_wnvZVgePSRBHKfwk7TmaxfZohLGJtMBg3BRv9qcPIYoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موتورشان روشن شد
⚽️
دمبله دقیقه ۶۶
فرانسه ۳ - ۰ عراق
@Sportfars</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/444192" target="_blank">📅 03:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444191">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3578b64959.mp4?token=AnRuHH9Xxx3T-MmRtMCNkOZq6WCVVZDX08f1oZC8CnRgWKIZX1PaU2QBk6IiKcTSn9giGThvSkhCUeLJZg7eOiqJBz9q7kMDSu1c8sztg4TjV9pJG0JwrNP6UTbHTtZG2dS7FcX8_B6ppD3DIZ_QUDBOJQYKUt60CCbNJkmPr-k2bmsXMqspN6zGXQzDvbhRopsXotLN7ZwGnwxGZrVjW1ZLYFCWAbC8OuG6YZxN80N5EfI8JN7BsdUoXNqa4ogoeGrh8Qazn_-m1-swzfF7KyHJ5ccO1ZBqLW6Zv2N4kJAlYR0sUm_eaGj1uu60x9g46bvzXwov65rXmwXn0tYO5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3578b64959.mp4?token=AnRuHH9Xxx3T-MmRtMCNkOZq6WCVVZDX08f1oZC8CnRgWKIZX1PaU2QBk6IiKcTSn9giGThvSkhCUeLJZg7eOiqJBz9q7kMDSu1c8sztg4TjV9pJG0JwrNP6UTbHTtZG2dS7FcX8_B6ppD3DIZ_QUDBOJQYKUt60CCbNJkmPr-k2bmsXMqspN6zGXQzDvbhRopsXotLN7ZwGnwxGZrVjW1ZLYFCWAbC8OuG6YZxN80N5EfI8JN7BsdUoXNqa4ogoeGrh8Qazn_-m1-swzfF7KyHJ5ccO1ZBqLW6Zv2N4kJAlYR0sUm_eaGj1uu60x9g46bvzXwov65rXmwXn0tYO5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رابیو، بازیکن فرانسه دروازۀ خالی را به بیرون زد.
@Farsna</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/farsna/444191" target="_blank">📅 03:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444190">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b0f3a5bb.mp4?token=WRGPKWVoE0jIsjgkYd_3eHhakr_oDXmo2pdMKJapH8lpPwCCcmyWB4Lt7tR4Q7dpiqXYlLqI9tlekx5jwVX-f1DDI4QlpWKlQIHjOT-fGceaAVE5K3DNso-gJNxVGyGeEVte3pU7n5_yMq_aQqR-ZqJM51HOqDelG0n2j209uZR7SnNPmxywr-xuqq1T1CEo1CvF8IbQlD70aCsaY4xibf1oNGF3KOllsUM_mRghSQgidRhLktubnMOs73oOOjKASkfsnT7s4h7rWJvlaCj1iSexmiA6HtEhamXrx9yZu1cp9Fhuon-4u2vbekAeepy9_hMCXLFYFBo31OqAsmls3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b0f3a5bb.mp4?token=WRGPKWVoE0jIsjgkYd_3eHhakr_oDXmo2pdMKJapH8lpPwCCcmyWB4Lt7tR4Q7dpiqXYlLqI9tlekx5jwVX-f1DDI4QlpWKlQIHjOT-fGceaAVE5K3DNso-gJNxVGyGeEVte3pU7n5_yMq_aQqR-ZqJM51HOqDelG0n2j209uZR7SnNPmxywr-xuqq1T1CEo1CvF8IbQlD70aCsaY4xibf1oNGF3KOllsUM_mRghSQgidRhLktubnMOs73oOOjKASkfsnT7s4h7rWJvlaCj1iSexmiA6HtEhamXrx9yZu1cp9Fhuon-4u2vbekAeepy9_hMCXLFYFBo31OqAsmls3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اشتباه عجیب مدافع عراق، گل دوم فرانسه را رقم زد.
⚽️
فرانسه ۲ - ۰ عراق
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/444190" target="_blank">📅 03:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444189">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfNyloQPv2Ompm6VtfAUB9iZO4SzYf2ZmcLsyt4ZD52V8rxB5X3pirEPPm2HgvQ52HHssDfZCUyzHJVtyY8fST9qcbG0h2JnGWJx3KK1c0CTI8xHqLv6XNOErjzL69SiCwpgHxIksxZJpA3VkTYW2ufNFfVSNtUhwooya9SGAwyRIe-ciPOYBiQd8Ek7IpUVHw3UoL6mWZDvyd7mQxyBQHDQwINiH6WoIrV0SRCjPjZjES8j0tC3VbE-jkb1YhpV47YJqdijpktqZlJ9hBxfFOThT-9wW7LwMIurMJAG1fO42BNp3SERYocdbTme8WqB4k6fZ0xrzvy53yK4fALhTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از تأخیرهای به‌وجود آمده
⚽️
نیمه دوم بازی عراق و فرانسه آغاز شد
@Sportfars</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/444189" target="_blank">📅 03:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444187">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
منابع خبری از بمباران و تیراندازی ارتش رژیم صهیونیستی به مناطقی از شهر خان‌یونس در جنوب نوار غزه گزارش دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/444187" target="_blank">📅 03:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444186">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMNaJTX8B-J3bTwxsUra7hAXjg08oZCRffyrg_-kRYEHGlfzZGzN2nUXLmnFO3-5FvM1Vr0zfrOU8O0LYWAiYHryh9pt_wAbFxAWJ_4yVMC6Xg_qLIgrZOxT_MQXHTp4JlBU16alNdUJn7t8OWghjqwXeoKT7zgQUfYCEhnaBEM0VGebtejTlVmu-_q3n81mylQzkf8tqoeCTu9mclPuh7UqdjEXZvOqUl13g9eeOopdHwtO6kpzvek0TuPPyq31VcA0S0c6uJrCSCufr1ZSuhIL6laXanW3kZFQz0Z2b_riM1aWdDgi3vMBPY-L24QhXWg3dGtETTWJPcN12dHCIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آغاز نیمۀدوم بازی فرانسه و عراق به ۵۰ دقیقۀ دیگر موکول شد. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/444186" target="_blank">📅 03:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444185">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYsHtpzH0M7KiRf-V7U3FyCK1sv-QLmqt5xa6wSqc18UI4pycdlKhATMiSe8SXvSF3KIAdtFooAMKBDVVuS9t5lH8kLGBdluq71OIJhI2Zpt6mR3rLrgrzwN89hUQRPozG-i1ukG8GyDR-9SZ1kH4ZdCj8K-6THI-5WNbPIwt-wfFXqRAcKB8g-THjm3Ym4daKSp8cfBLSDb62pZ-yrxirhPtqlyYOnsxeVzBnm9KfqUnzC8TbFtElttz9joQVyW1vU_vKq9sxwKuMbJQR0H7MPwwS0RSpCId7PzCRQC_u_GawsoCIXbHo3OoDCC73-Q_LPOGwAjs-dIacGbTTZVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
با اعلام داور، بازی عراق و فرانسه ساعت ۳:۲۰ دقیقه از سر گرفته می‌شود
@Sportfars</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/444185" target="_blank">📅 03:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444184">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚽️
آغاز نیمۀدوم بازی فرانسه و عراق به ۵۰ دقیقۀ دیگر موکول شد. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/444184" target="_blank">📅 02:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444183">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f49b38b9b2.mp4?token=eIe1m5fODk1tr-Bd6nO5Yx0yPpNwCB7v6rZlfCHtpz_oYizMlOw3MSN62pa3oMaG1CJ23v9tPYujr5ogWYGtAicLVn_5vGBB6EZVCucBr8lnI2O4sr1P434nL8ECsoFz-Lu2yWnpRkIU7upnBP7HbbaZOKsdPT9YXxEqk2ntJD0O_TodiCOmVEHLE8xRutCIaLQXZs3oRVKx2IpTSIaUp_9FDg52ACY1pnnHc5pyPTaqsSeapAWrDjCO0uimGczZzKJjHICxomlT1wVkMSP0WDd6A335Q5UbrPDtPeb_OxVIqlndU3GyqYZYJ6k75DQgAvTCICI6TFemeu-cCA2owqkaxUz98hqpdx8lBvmkTlz_m8AcVUoa6b9REFJd7i-KI_V7EAGZfYn87enp5sGuM0ie-GVA3vnPFe3y-DKjoydnnqA7OTP4rsFnpWTM1JX2udYiiZ480VRF7XS93HcCiyFeNdskDkLzVZ_OatedmkcpniINaL9bir6WtBMjdnIi-1ByK1uQqcvsO7o7jqL8qou5_lJnmriwtLV8Me-rif0OkNAWw-7ZtgJ2C4Us76jUptcYc7xJ5Lu1o490Dtv1av47Xo2ejBA0XR88TD2zIUFscbn027--qA1Ep-IXqB-GM7q6YbXkclEOEKlVaRu6Du87h7T3sOAJjssznmqf7XU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f49b38b9b2.mp4?token=eIe1m5fODk1tr-Bd6nO5Yx0yPpNwCB7v6rZlfCHtpz_oYizMlOw3MSN62pa3oMaG1CJ23v9tPYujr5ogWYGtAicLVn_5vGBB6EZVCucBr8lnI2O4sr1P434nL8ECsoFz-Lu2yWnpRkIU7upnBP7HbbaZOKsdPT9YXxEqk2ntJD0O_TodiCOmVEHLE8xRutCIaLQXZs3oRVKx2IpTSIaUp_9FDg52ACY1pnnHc5pyPTaqsSeapAWrDjCO0uimGczZzKJjHICxomlT1wVkMSP0WDd6A335Q5UbrPDtPeb_OxVIqlndU3GyqYZYJ6k75DQgAvTCICI6TFemeu-cCA2owqkaxUz98hqpdx8lBvmkTlz_m8AcVUoa6b9REFJd7i-KI_V7EAGZfYn87enp5sGuM0ie-GVA3vnPFe3y-DKjoydnnqA7OTP4rsFnpWTM1JX2udYiiZ480VRF7XS93HcCiyFeNdskDkLzVZ_OatedmkcpniINaL9bir6WtBMjdnIi-1ByK1uQqcvsO7o7jqL8qou5_lJnmriwtLV8Me-rif0OkNAWw-7ZtgJ2C4Us76jUptcYc7xJ5Lu1o490Dtv1av47Xo2ejBA0XR88TD2zIUFscbn027--qA1Ep-IXqB-GM7q6YbXkclEOEKlVaRu6Du87h7T3sOAJjssznmqf7XU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مداحی جدید محمود کریمی برای رهبر شهید انقلاب
مثل جد تشنه لب به آسمون رفت
روز عاشورای ماه رمضون رفت
یک جهان به مکتبت پناه آورده
خیلی‌ها رو خون تو به راه آورده
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/444183" target="_blank">📅 02:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444173">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUZ3rIMAZ6R6uMG8gOtyvUFk18L2DYqN8d4dcNzhAG3FnSluy9wtTnQaSgDEhxpW5j0mhoKXHKV8QvEyn9wRBVW42zpJJo9D8E_szH01yc6LlVpALLK1sNP4Fk3Hcu9G3uet9EEJMhKQqZ51za764ar7wOZJTR6MG8YpWgkE0e51R1kBHgrJOBwYlfk-cCMESCPqCbWa22oy6911x-G-D-yQYFQ4kITV43V5S1WkIYZ7U6DNri3oxra6eHy8cbDMhi1RldTrfYBG4PhIFbLL-mqWFq9mgFvhguoMhRdIDU6ib6nxLZ5MKKVHX4J6vE-vew1LHpmSv7GeiHA2MFNCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSPgUVJiJCacUN3evbU8fUKcG7BiCLCqHVXxaf869VdOHeh0KtC0NVfdr4p0UruNGYbidMYOpw6FD0IMRkfkwo8-LQJpRzvqXJMBxC3CzITYfGyPVL3tsw6Jcebiy3_928B8pA2q60S51WttjODpYCNOIdUxY-4Pz5UDDoEzJTrL3fdi2NXYpXhWGOsfBKitbKoKgiia3qn_Xo81bsdbj51Fc2pfYR0O6XAo-2o-IYATtl6uiRjhOFjga67kteVaIJirNqKMrVKHyPtiPYv2Ocuav-jclkVeB61KEN_vE4gby3Bz37fQdFDQZ5jI5fJz_rWoDb_nST8P--i2M2MwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bgbn6R7XbTORsTGegYyh6PHmJquXK1Vw6rNKC3JjZmmmnqgv-Ix9LFRomg1Cfvo7xtWfqd7L7f4xAnD1srVkQJRlznaZJNlYZdZhHtak7jaKm2-0cXKK3GGUXFe7TXoQ7pcla-vUBM5MuI1Xk-EHPb_o1_jMBoG7V46WIsZZemUu6ohAVHWIe-0jo3qM1Z3ajnvGGWxgjXSJw6QBk-5nxygyJpo6gWNuyHv0aJTw1u-u42Ch7gJncCpnn70wTkV6RXwoSMkDP0JwCnP1CJszmIShTpaxt0LNBRaSWxJ3nU024_nBOmxEAHanaXjiLfZFuSfH6oGI51T0YfzKox-aAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3g3o3ACtcgdLJd_K3FIcCH9qcSuNXLT6xUbca-VbIsiC6kGQaQMv3VV0Bk54CI7PV5bdBaiH_VBo3Mh8y5tyKnf-Xk6lCGf9lGgdrjdl5-dNktmT1JZm7R5DpO7uaVpiBhVRN5piu5PpKtG6SDgatgkN3C4DbOYX6bb5TzrxJqcGdBCfWKffuIgbYH8vCeYvuR7tDe3Q8bkQBAmLq5Zr0_M6Oj1bXk8bkD0QrDdRTX7oNWiKvKfG9RL62asO5caM31pVJzokMaiqKG5GC5Pqj2tLEx1DQq7Z494Th9eP5_E8Yvjszm5JDcQ3UNOQeg5KVWy7uiVOzHZtoQ2rIFgHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d8emCcJcdrQrV7YSqRgd6mQgDFxSXXogkD33J8XlCbP6hddLoEtb2aVv2OHPfsNrlSkNLu0O0X72R8qmwOx7kqJevINVXwleknPRExeEIMP9ZPgFqHlW2zqaIcC7z0b9Dq4Y1OZaGeThDLltySWU3q0C1_QhMcAjYvc7vFvW7rphDEIH3CjSjXIXFgNfGuBVdT4kwjrNYUmn4dwLoqASSuNtyimwfZIITbA1-PXjuNoKVdcrynYJcumncy0gtO_IIyb3G5aKVnvDL2tY-tYYaZD2oKCPVTeU6Kgxv239BujU0ASyd3kBeOSgz5kF14Ue8KK6Fh-EgxDhpQOZH5DUkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CvoZJC7yk2v_3MZoIVTGhRzblV45kqhEAX7P8Aw3ZS_SK4mwr9KiDDXEhvoxDn7S9I5assv4S91eJIXgroJcEM-vmgqTWsTo6l-EhpIngxWadJYVYpq1WQK0RY_ZpDbIkb6AajKORDY1f_vy9eFcIAZakL5slLI0cLzVyxlR94U22wy69CFLRHcTtHgewU2_kiSf5xcD7-hbbdYK5af5lgApokNynd3fCsIyfWe7WQ9Ant6O9WDPhNx5ZIDp6roP82tjS-AIgiDl5pE5wkVp7Dlw1Ar00TwKSJP9QUJ6Ewm3QDeqUKDtcQUXYipLcP7F-zfpOD69etSh1H6Pzyg5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjNKlMIokKo8aPEguaFxAwPMX1ce6GVYdkRjPlXslkV4Lz6amRFrN1dY2W_VAoe6Pz1yE30oJ0DMyAK_H1kaMj0QFs7p4KHN8HaIyKNpQRKay7ZCUl7jVvz5QFbRyUM0XRIhgUYnvgDTIoZeWL6f9E_WIvzc0I4G1hS2e8ywXpqzteeMYAvl1ay1-vDFxPM-RAXcr_B1Rnlb9WuLuultohRO6osma4_4Vj3S96YT4_MQmtd1kqv9-NKTuee61_MrnKsObNtQBNmtGZ8Rkn3mGfm3oEKeBKjQRldDfLA8MvRSLBlkwGMzx90gt_75BQ86MWp0GkjkGxwrzcp9ZhV98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IhYLZ0R8BWIToGUeoIfvIX96J75MCqRyuPIoW4ykp01XqiAuUHQvSOPMpc1gHNj7caHwUmxq6EOq_EKn3dGJtecmFg36r40WdIue1lurkhLVUY9dik3USLTqPQls-SE27EdZLn9uTHip5RSOCWXJSgpF01NMvCtvMXAHT3FQJqFITUbZlwp4XjSLeDQm9tKHHxsCZTglJ7W5Fv2LG83iOAFWNSj3s-XNaEVUOvSN_2wLsoVPPHadfGeC-5u-hxbFRaX85tWXCoHqj3Zm5opQIxmK3KAJjjqQOJMVatIHqrDDgCzDvegmRUGFhdaikX6MNY0d5fId_XYolZTkkPvDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2fzQFG-9nmEpr5y9TmJWLgvI71czsKgkhlvKpvU402vZiAU1sFFTzezFSi4h68sxRX8pwIvxCXVNcSs7FwlLzU-DqpKxqUIQOKIEUH1HUpfUK-VJVwNick3X56CC_Xxq5Sctl4Ad2zyYpcdpXrQD4kqCayyx4FCDvM2J-ChNcz3uYEaXNiF5NFt_bbJzpr24V86u4JT7k812MQthv06KdHBSzIjSpiIveS4K9JR5Y0mUfwbELv11de1EdG4B7wJeBgipIkBIgDKR8AAYxQUKOwhGHFDGaSxYD17yb2y0pQQbOfZfg4IcYdTuq4qruLJ0Ud9PclttV-AaXlU9d-sIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W5dLaPFrEbSRc1ls8_qKdz4LHYR3XMrpTGG4sm2Qhi1vTRgMTLV_Wr_h8kFfcJxi47rllRzYYOSyfqk4833GD3joUEJOIzFdV_Zq7I5FT6WtMtu0VfDaggyaC9ddPY83kRYcGxkVFxqZjzhUhQ9QXp1HfQPvAiK8CcCQeIeMAvWc2IIhO3U4Rq6pjD9Hs2og1tqBlyf2bW-PE2hKGGdomGbJYOkiftfNwTXXKNzv5Y37-IcEjztjZHg3pXf0EvZNzQvdIze2ipplzD1mwqJ-k3zyUh4TEExa5c03YDMScuOixJRiWHTmvGGgH9eMW9MOGcV2lDEqD6z3DlIGr4PvEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین مشعل‌گردانی نجفی‌های مقیم قم
عکاس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/444173" target="_blank">📅 02:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444168">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oux9xJtxxworpRKOqkO0IGH7h8aTCSkp0-V_wXtagI4O1wig8Zji00C10CG3M7NoCL-xPD51MVxnaviboM0iMb0AdhW9ievGM695fneAJwm0h48_IDDW6Q1QJ9SKhYiTvN0iQv_CYYUMHelTB9ldX5z5Cy-ktOg3-d4oevJNo4YzZnPX07Gd_LjyT3XcxwRJ_iarZYKtQXT93IxciPc5izRj3LZQ1ebZ6SB51-i2zaq3hzu0ZXRKClD12ZBbPbiTsSCLyIlGzaBC_MVrcndkOm2XOgJbeHNZvu_PCog-qGu-t4ybbTL38XpZH1X-m2B3Gbw93ag1UGRMBl0QznxQBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XnbL1_HvO8isuVuVs76Q7uljkArUMAhD6X204X_4ifNlhqU0a3hTjUAGc2LLPMrnOJBShYlEnrxo3o-IsRFowixd65Ro0VwPzADHMldW_2HN8xnNpRuK3MnZNM1UoLz8QNCRLEiKLRxi0uMDy6X3qa97cb-8bJToTV-y1cmX5TwdLVWnJ1cmtDsGNuz4b0XCdMPEPntp8q2u2UNvUxTvNYYTMVVpHqDK1jVqobEtHH-tCrljxAKM22D5aasHjDAu4bAK-8h6L3NOnw44kpU2KkfiTc0oP6PU_nJs4omr4u7q2W8-FI7XM-w6eKnHo_uNrvj1WkqKQw439PGHgim53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-xLgYPvBBqUtj3vZBYURpW7v9U1M7_W9v0VF2NX5AVCO2TupAGCavHu0ZHMbwqZzNLGcXKfYq9IH6phquSR_wbDafJHFPNHSYdN8tYM6GGwM9tfcFJXzzuzgUf7i6s-4R2Aou0fRootBjk5bvBODA-MLQ3GG5iRlM0F1pM1ubfS_QB4sZvMOYGTu3BdCyi1m_fLQ5Vn7le34U43xR0o_EBLoq4gl_ICCxqmBSxgvVpVebG0lWdSu5heOuKAjLwu1MELO8UDzLd1zgvTGV_Rmf6L_HIx3x8LXx3HosIWHyi8cFqgaO1yBu8RNaRkaZdIIb-KiLjoDq9CmRpqb-jONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K4sj2lJFLjDLDALIqjH8lHaPsLlZ_fSrC7uMI4jyIABDXT6tNejJEe_ETCCCRWHiUF4tizIKUE9tk7w7zCPv8lB5mEdFZUkVSLbtltEY4toB8K_9673vCxu84MlrqgzUlDDcP_MzGEI6B_JmRL0Tpu1HGVQPx7lqjXy57aZTnQefrz8IXUz-bbwtx8ut0j3gCen1nS6pHVF_tEZfOX99BhbnTGR5ZaiUVErHMCOfuRFSRJd01sOODLrahOSksOFSMNFPofE9pugIU3XiYU7aEtYCD6sKpbZJByI2kEGqPnhvnrzCt5H7UEyQdn-hv7RSp3BkSAW_zBcja38oPYAZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nVPJ2PqQHfuCVyzTv5xWlea6EwSqKmCZJ_74v6fInNICbiHd3qDhNwUh7RumEDw8LBR6apa1HNp-Hh3XbZ3StVCHF7CjVnV7X2zfnMzntyzWbvHZgV3JO3srw3AJQwY_fnTQaVxVyf4GONizASyROgTSposSaQZCaSWCbbgWjcld6wFG3HQOZ1pAyu8tJXLLC4Q8bboLu1S8WrZPwuc-72ZC9VzTd7i_dKmiNXf-GI_FFoWmVcdrBIWQpXSjly92Pzya82bJjafn_kakW0lerGZYFiaxgfJNKzD4KF-2u_XmIOW_5FpadMDpc12Efla15w8fKe7pggN6Zh-0q4s3Yg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/444168" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444158">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fr7C-3ooeudx2Zg9WSAwNTF6_r0nS4Sp8_nDv_rp347l8vJPs94A-lC43Sf731UsrOLwOQjluB0w4pac1GC_3AiWqRxsSKyBo5zaZ8Z_bNN349HtGzOX-wx4KJ8umhcGLKcN-2VL9usEyzSdte6YpxWmNdVatrLqOEnebESJ3w2KkqDTirZx1SGvltfCLz9EW9-SyYdZgl5ccpBjQ23S5PqrZ-p0co3bc8j45b6FQ_dhinWfCBPBAGi87fLrQnSmHOs9epuhSeZxRDKt48-RdsLXRj-aMrwkIE-pcSo3SQAinJw1hOh0bQ0tDT-SLBNmPsIhKJsKJu2bWaFdW-bYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlZhb-j7dKQLoZOmcU9lLl9ldvH-Fv_j_g_aJh2jJJymzPutmpG0LdWmaZBBqK2y3Q7yKE4EfHEU8CIjBdjoW3gxn4j1l34g7r67Yvskr_b5NdHHzT-8jH-mpz-BLaKnyA45QaoV-8_JphFODaGVGFAr3_2x7azBh1xXTvzU_TFFqYe1dPCOTiOPMaC1aE5HGMdMfDkaqSMQLUJf01kJFuZTDrcD7-tXsy4Y1jnomVcyL-TpqxJ8LbqbatSt3biX8Xy6fuFIMgplMWf5u8b1F1wEa9EtRfjw3bAsXq-M275-8Zh-oOiWkda2oSKEcdOVDp4oiKyitpjuh19JB6J0wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ohuy3xOLWPL_f2dDO1trCKJ6NIZAWUl0wc0ZL4mEEooqoZ2Da2wIjmjEqKXuDMBW7EEgJbH6xMJLLTmIq34Dv4GXVuUSIe7ptu8pFTuJLDzJn9KS6jhky94fignT8QOvxKgbS8DuArnFA-BKk-MZFC191Cxy6VKNW0poYOWVSFRU9IHaNHu0dFZmsdnAZvhqtKJAlTKotm_FFv94yqOjn9wrfDC0w4cHTRtmf5wP9piuFNbbI68-zUt4vPylIuSMl45tJZpeX27fQhapbdiAR9mWloZh7IvqzSQIjcovKUw-f8G2-igc2PYr94RajJSoQv4GBk4hc76JUSML_Sz9zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knuZKTED0OtG4NiJzDJNBUzcK-pGuopude2Vx2GAIo9U129cs39RfUDi4cZBtKJi05RbDaoIQZfjCXyUlQPpI4R3Nj6Pb7LOe1aMLLdplzzSVTZsDHY0GyXBLMjPx3cCPDR1wNn5ZkKShVlghsvgYokBSrNw_j3DQhLKrDzM3aFZWZaFwXIwwIIl413fCH9YHmbc6_r3BWOQNRiuu5JtaxZp00bPTS5-Z5p4NcVx7DkVWp_Bj9F4_KanwCDFJ0urn2x2NDNdC3GMI2i_7D7Y6Ldzn8pFsPkx7JC9Hvkv3ZpJxgSgb32kSKae2x7k7e5pTIftBkJRd_S1vI_Zma_NPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8dAbTlCcBaggRqNA86hZ2bySbOHpz4m9Nk8lQYnhMvRTaPWCx1b7DHhvgPW-BlpjlI387a2jSL-Z2aXTm1Dx__081Saaqktkqqlw2b0m4Fmi4HUypVmA_gIAQvrhwigh-6GbD6bvJ70JRFrMu9nbNZYKv7i6D4GxP_IbGyprj8Y-MJzHysLBBxl5ssRdsxOZlxENtZfG-Ppw2eyErT0nzrsFpSqb8ONBRwqb8L64Xe02I7cJy3BpmCVqxPwMnHkWYw_592P7ASyoURhNs_rNEp_-8DaxZ2s63pEEamvTsjrCiefLR7TsiuTVpn85d1S-0bS1FOpZZHOvxkVRRulbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8uKcGXSryejsvgQ62yS_-nZodbSj1NMVqGxLjz4v5BZ9VbmAki5nCfWYybOMmJvRlB0QjGXHWsqcRlkPbhdJU3xdgpFwn8RZEwhkiOq_7TzfnIvbGO9xQPaOFVizvGtDYbxmIfInMz3hZrZ72-oxdG_A1ghz48ney7YCbTx8wkXMK1GmgbWoMI63x5A2W0sScPZBO75QuyA7CeWdY8cF7a8NU5l3_5MVEGNgl1gX_JE6nUJ2-RVJsBE4JowZ_eHhfpg6VMW2P2_df4ok8u8FC4fzFOoDa3nNSvxgG49ftI_OKv-B7FYZa2bsoEyeXc5MdwlLnFCYdE6dJRPugIoPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cw_P9adgdbIuYFcS4PNiwUaAk2Z-u85gGY7PmlSDwg5wWXKjC-9t1ZzxVVoN7fs7Kx5C2Emcu51h0JaNSmHpnJo_THYcVDHOZE439HivO6_HtRiwEJA1wqWEhs9mYWhrqqOLYYQ4DVp9xfAG0pSAXfOssh_HrgrXs3cX5k8GBG4L-rW9odAS6PddwxdN9z7RaiaJ9vmycNdjCJgjFOnStiEvpBz7Ee-7uCAsNQLEh6sc5DVZzXQcTRy0xvGAdPLvSh0_ZJV-LgHe7kti5IHctLL-lUZXpcsICH8fjeLTSrovo9oVXUX93mAizab3SCNLs9hIbxWOPaYPhrunXxeUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdOTemeDyr0vaeJkKVlrK9IvtL5PEfcKIDiKzBNSrONOy5TBwMkmD8IKT5pezuie4WgkfbSPfG1jFtPtGT36OJ88mLe2YhASWHFlg_AnHK5mOv4bEUamac1-s9Ww2Pyn5Qu5mLIXC0jK2foXsGB0GETbBMuJooyAasyi6mWldPNwZPE6y1RjFVV6O4LKjlqUS8HWcHcNoqZWN80p_GgEYqzm_vOhLriOr6TL2NxI-8uRRwHaoDlZQkZ5lvfEGDWQgmDiMwNn8b8jXngr_0obDI1STgt9rkUL-EBMg8Lap2l7CVT1yN_PByW4L63xAx3Ccd-61fwMlO2nEtwHofF1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMrXkmADi33FQMsf_VE67rA3c5vOURRU3hJXD8her_TFohuskHNZsxQ7my6XE43pyXancjbNs9-zmktDQnVAz-78DiYZ_AZYH-4UK9TKh3MJ8CdwhIo4Ut4k6W9JQ58FU1r2n_AMncfLJhHj6CYXpaEaFRfkvpr_-No1rn7CZyOYiaDtlf2RWoCODRmRxV0hWe8Su-FU_3COhGVExhrDLMGxrxdrtku9zJfcO9IGVpHw7rQrMAxqvrrnJguQvLzmjl1MX2xWnt8i4HStwsbi8T6VPxa-7euxYWPU4Q0KYSZoV1oCHUKzQ7SGYoPBIXJ3sfazbhVXMruGBrI4pSw81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDlUS8QNjA6LFuXfTBGOJurFFIcdu-vWlIuoP_jVugTD-B_xHcTOcZnzWnlSgyCin3soFtrfjaV1IYI-1ybSRe_tImKzrjVo7y28qX1EyHKPfaWPFylinSbrCS1StRwycoUMp20xP436-mJLWFwAN7-qgWA7pSm4NMVJiuADKHwSmgAxs_xmObYzSszsY1VvouTkzhyP2yKEVyO93nLkAyx7zqbxmeLLj-lrl3iygThr9QjQilcVWrcJYerCzbLWwbM93Esc2PmgJoUGayD3U3icepAqccRgE-66HFyU78PMFJ9TXiDqqhMDFzTQqjQLI3lyXF5qjOX6hlWNAsNdUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/444158" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444157">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
وزارت خارجه از توافق دربارۀ ترتیبات مذاکرات آتی با آمریکا خبر داد
🔹
غریب‌آبادی، معاون وزارت خارجه و رئیس هیئت مذاکرات فنی ایران: قرار شد تفاهمات امضا شده درخصوص آزادی وجوه مسدود شده به مبلغ ۱۲ میلیارد دلار (دو مبلغ ۶ میلیارد دلاری)، بلافاصله وارد مرحلۀ اجرایی…</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/444157" target="_blank">📅 02:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444156">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZCZbMQLnDEK11XlJOr7_HhUDZobqC6mWfw6qh0joG9JZVzHTQjdgPA6YzoKhoNliyEXoLEGEP5t1894RrCK5KBSygyVUPRgdJO-Qw2je4K7hoi4f126ERCWX33I2k1ksVt4q5oE0PjsmRcHmnV31zKsvxmy0aO5rgyEyR1AaKzFd9GjM-y_2BKzq2KJUPtPVMXSystrmQYjFK8v84ZWTulE4Y-K743zqQEOrC04FBR7hebC3lb4dlN2Q750COlVIheqcNuKLpfIlOf18mHCDrm-TWgsE9QNgv1ZdlnGR84TnKfUMTPrmh1MtDxWHLLocp9LSoZ1f0b6wUCNai7Z_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه از توافق دربارۀ ترتیبات مذاکرات آتی با آمریکا خبر داد
🔹
غریب‌آبادی، معاون وزارت خارجه و رئیس هیئت مذاکرات فنی ایران: قرار شد تفاهمات امضا شده درخصوص آزادی وجوه مسدود شده به مبلغ ۱۲ میلیارد دلار (دو مبلغ ۶ میلیارد دلاری)، بلافاصله وارد مرحلۀ اجرایی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/farsna/444156" target="_blank">📅 02:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444151">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RvGNsYqBeqyLvfQvUH5yv7S_twESpvE5kadQCAERZXn3HR0wa_ZbFxlYbTRKyCsDhBdgH-naIw1b1ZOirxTh6J85BR-3AiYu6MNba4eZRgVJXPFd35QnPs3FXvMZ47uCO22P7r0iOnsGYHhNYVy55K9PfK7qLmbBz0ECQ7Ply8EaWRIsdyHfu-ZAk9MZ5COCD9wK17CsRo9CUPUzI-SsADLb0_12lI7D5QdwWDNpHZLPrhSXEg98KMx7w74PnXe2hQfWaPkwr3UtG-g4QQveA8qfd84_zSJXOHURhp8PRWyv5UGlo89eW72zP7YMIZaK0cbDdNk179lmcKnUfsYapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uylvHx8ouL1sDOm6gHtMRTQeFNjTdK7p9emLoypf3tV0XH-lfGUMax-6AiavbDzEdg81nuoMh69MVNqKadjZoFHyoiDvlPMeJ46GUFJ0E5cwVrHJQCbjjF3J1zK2kEJa9KoDwy1WtQJwBz7tlbMH0aMYQKM4pDGKueaAfj3kg3VHwHwlx7WAAsmN38Pgjig2mSj4Lf8SUn6sQVPVR9f3BoEgPWxN9gueNCvnU-h2u8K0ZUEZx__STo_D5v7xuQYNurO7i6VoDkj2ooLQ7s2BxoKbtJCdNUv93dWpPu_EzPPpUaizwugT3QOh9xCwH-kwYDbMOiOvp9QkXADhlz4VtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d5bvTRbmjAPWgSOIkeEx8fcILcFibCNTF1gXbdiToGI4qop8NunAjwsxMl1IBfvrOmB5Sefi3cLMHxfRC4wm4eZkzlbjFADPq_3wUbS6HJ0nyD62RxzCNGkTt4i6fH_H4cvI9Lfo2-bQAwVw7ZvRsEZ9HQ4_psOXvH73NDd-4vZ_-exnLmSylFNOZ69OEr68dKOHWdklvBlqTS_5v8RdDsNEdMAEjTM4X80oyLegetEeE-eCLc4ukNG_KTBy8MCPC4NEz8PKMld4T21ugqkamaHK01AV_aiX7dMiHicaQOipJYxUhqA7yRvS1PT7WZ_-yPwhwLtvplTO7CD7UTcVIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LHDe7LTjTJmgWfwxeu4bMz94B8-89LbLrtDTR26u9MIhByUUWoPrPFgNTAX4_MjHt9uqf8IwzB9me91ZlJSRG0PN3l7D5C8-JJvx9TIL3BMxN4-Nxt8x0GI3558A_2c2TgcmzmMEelzaTZN01oinBGmUgVn4OarBUwuFmm9IXCqfvhiWKk2HZFBmJcHylbmy0U8A5guzZWAriT9rJt9IdN0jkUAzaQSdugTpACQ67_nTIUbMBWbU3FssiVlOhGLShMMKW1AkbmvyX9UpAJHlCsq-q5eAjI1dsNtISd2aC232E4gOBbaZLJyrbQumoFshO04FZFu7nHkq9PZXf5GXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlV7hV3rEvxSJH_KBo5kWDHYX1l1k_Rb2BeHV7SpJ54vOUWrLROwnMVR22N-9SIrYF5Kt1xOLntsYx7ch5sw6egGwlxhx2jLwmwyk_2H1f8CLng0srA7slRd2MbQX0hTzP2j3B4mo84P7EirY5yZli2WscTdu8549bcFSZ_wbQOQMK3qlCQeab-k5yxi26-RtTcCx3mCiF9muVWS_7zmsi6iah0nAS832rD20XHGBaxRMKhNVlDVrR7-9-4imY05YfooBmc-61TbecV6RRLQkXhT1S124muhFR4xMUVMDTXd81Abot8dfsz3HOSymJYBGO0EvFsWtZbu1p85Sgb6hA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
استقبال وزیر خارجهٔ عمان از قالیباف در بدو ورود به مسقط  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/444151" target="_blank">📅 01:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444150">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b8757089.mp4?token=iPJg397P15_aaLZuJBeZTLXjRf3aTg0mM3j96ZmYcRcwLuZLV1v5QGT7oLFaEOfizePHcYmap6-u6ZYdTJ9YvrmBKSPRZpNHGL_De5qmteavSjJyM_kxkOGvGwNNnosBZgd2bW_uF2p6_69XAUqedyENoJsccKlfxDk_DWsIIK8tRaL_TdkXSRN7h3D3p-gmYm9DTJNOknVc4S1cbXLYJsiJnaQyGcA0hLb4v5iv2CHup5OxdlsxCQm_1BR54BglyJ3IFqZVfl-6_Aza4es3LqwazKrOPygvt_lCNmXxe-0M_BAGCiiMo87BLXxMC0QSdcKtMVn6g5cx5swUrxjuiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b8757089.mp4?token=iPJg397P15_aaLZuJBeZTLXjRf3aTg0mM3j96ZmYcRcwLuZLV1v5QGT7oLFaEOfizePHcYmap6-u6ZYdTJ9YvrmBKSPRZpNHGL_De5qmteavSjJyM_kxkOGvGwNNnosBZgd2bW_uF2p6_69XAUqedyENoJsccKlfxDk_DWsIIK8tRaL_TdkXSRN7h3D3p-gmYm9DTJNOknVc4S1cbXLYJsiJnaQyGcA0hLb4v5iv2CHup5OxdlsxCQm_1BR54BglyJ3IFqZVfl-6_Aza4es3LqwazKrOPygvt_lCNmXxe-0M_BAGCiiMo87BLXxMC0QSdcKtMVn6g5cx5swUrxjuiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
شرایط بد جوی و خطر رعدوبرق، شروع نیمۀ دوم دیدار فرانسه و عراق را حداقل ۱۵ دقیقه به تعویق انداخت.
🔹
از هواداران خواسته شده ورزشگاه را فعلا ترک کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/444150" target="_blank">📅 01:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444149">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۸</div>
</div>
<a href="https://t.me/farsna/444149" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۷ – کتاب آه</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/444149" target="_blank">📅 01:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444148">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJDazWypxhsNQ1VFgNU7WYWOywd_wTCgpV8oW23KP9iTtXKl5XDB6_ovu908j1P7Riq4KygDTyqt-E_DD6vWz08hqh9yAJXDDP71xvyF0-RUwBws3pm-d3UuJtb-Qg1bjq0KPwBiqJ4oPF-4un8YWFMGwxfd9MvbATaCI109-loQVN4AfI8XkQONX-kv3w_Gbb11VWM5C5hdAKr0nAUdeyIVL9Ju0u727hzoYwaXh0jPgUH7yMY4dtmt85nkaL1ds3WoTUPh6sIV4_O4pbGGxXmm7GOM_1hhugu-duJB6ydAsPp-B7A9ZvV0He1h7uo2BJEFRF7PBatSB7pgvSbqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شرایط بد جوی و خطر رعدوبرق، شروع نیمۀ دوم دیدار فرانسه و عراق را حداقل ۱۵ دقیقه به تعویق انداخت
.
🔹
از هواداران خواسته شده ورزشگاه را فعلا ترک کنند.
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/444148" target="_blank">📅 01:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444147">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b8d941003.mp4?token=JJ9hP2nzJC4HKgnlMZEj6kxGUNkIf-GiZcPZNb1tFJrbXJ5dh4HRTn4aqlEIqyf6Wt28aSOs2kPNtYup99DRIXcfRpLpFNATpwWruT_0Ddhwm5TCUSjQgnaGelXWgR2B5wRqgC5JhBi7KzoAyfT3x9WZtKSFVZ_7IIbKnchp0xpUM48bnuhWRq3WJUkX7inCH9d6MaGDP4MudZr-d0o75F-nocid2EdXSZpcagzg4Ngjxb8okdCCOMjUEmKCAIY1gVE7N5NcZ4Ajr7N1m9fSK9Zn30naRnffuT4E3XwwfT40EXmjnTecYbFuyHIeKjzmHURLh3s2FTNXjym3FvLzjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b8d941003.mp4?token=JJ9hP2nzJC4HKgnlMZEj6kxGUNkIf-GiZcPZNb1tFJrbXJ5dh4HRTn4aqlEIqyf6Wt28aSOs2kPNtYup99DRIXcfRpLpFNATpwWruT_0Ddhwm5TCUSjQgnaGelXWgR2B5wRqgC5JhBi7KzoAyfT3x9WZtKSFVZ_7IIbKnchp0xpUM48bnuhWRq3WJUkX7inCH9d6MaGDP4MudZr-d0o75F-nocid2EdXSZpcagzg4Ngjxb8okdCCOMjUEmKCAIY1gVE7N5NcZ4Ajr7N1m9fSK9Zn30naRnffuT4E3XwwfT40EXmjnTecYbFuyHIeKjzmHURLh3s2FTNXjym3FvLzjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پاسخ مبهم ترامپ به سوالی در مورد اشغالگری اسرائیل
🔸
خبرنگار: نتانیاهو امروز اعلام کرد که نیروهایش لبنان را ترک نخواهند کرد. این موضوع یکی از گره‌های اصلی و نقاط بن‌بست در مذاکرات است.
🔹
ترامپ: این حرف را به چه کسی گفت؟ به شما؟
🔸
خبرنگار: او این مسئله را به‌طور عمومی در اسرائیل مطرح کرد.
🔹
ترامپ: خب، ما قرار است نگاهی به این قضیه بیندازیم.
🔸
خبرنگار: خب، چه اقدامی انجام می‌کنید تا مطمئن شوید نتانیاهو اوضاع را بدتر نمی‌کند؟
🔹
ترامپ: قرار نیست به شما بگویم اما این موضوع حل می‌شود. من آدم حل‌کردن مشکلاتم؛ مسائل را خیلی سریع حل‌وفصل می‌کنم، از جمله مسائل مربوط به نتانیاهو را.
@Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/444147" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444146">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">بدر البوسعیدی: با قالیباف و عراقچی درباره تنگه هرمز صحبت کردم
🔹
وزیر خارجه عمان بامداد سه‌شنبه گفت که در دیدار با رئیس مجلس و وزیر خارجه جمهوری اسلامی ایران، بر تعهد به قوانین بین‌المللی و عبور بدون عوارض از تنگه هرمز تأکید کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/444146" target="_blank">📅 01:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444145">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3761e2cf7a.mp4?token=tVaTw1DaDji9XU-9nD8dSACpCWK0CWJJN9tJAmOul54eERs48qISszu9fCHVFVNaeFcIAVbMvQzqIjarWWktyr0lBfj3IrSsR7Lae2u_1TFdh4xMzRsMVG49anJkWYWGSQn0SIgmj32-sacZfBtTrdzNtVZZFndZTzjIAxs9q4mgt49Ad4-vfKU5nXpaUGe4U3-WUhF-1P4Pk6VEQbzfKcFZyiqFTyofP1ylpAbaTgSsiEgUryjLeDC59QL5n6RNEaGeBhP-DH7-EnC1W3pRlsIjLacq-vRl99tL8auX-m79vEAj9sppXi5m1qUjXeLLPAbPvOZ4kh37j8Kf1qpITYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3761e2cf7a.mp4?token=tVaTw1DaDji9XU-9nD8dSACpCWK0CWJJN9tJAmOul54eERs48qISszu9fCHVFVNaeFcIAVbMvQzqIjarWWktyr0lBfj3IrSsR7Lae2u_1TFdh4xMzRsMVG49anJkWYWGSQn0SIgmj32-sacZfBtTrdzNtVZZFndZTzjIAxs9q4mgt49Ad4-vfKU5nXpaUGe4U3-WUhF-1P4Pk6VEQbzfKcFZyiqFTyofP1ylpAbaTgSsiEgUryjLeDC59QL5n6RNEaGeBhP-DH7-EnC1W3pRlsIjLacq-vRl99tL8auX-m79vEAj9sppXi5m1qUjXeLLPAbPvOZ4kh37j8Kf1qpITYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بیش از ۱۰ میلیون رأی قضایی در معرض عموم قرار گرفت
🔹
اذعان می‌کنیم که هنوز به شفافیت مطلوب و مدنظر خود در قوۀقضاییه دست پیدا نکرده‌ایم، اما اقدامات قابل توجهی را در این زمینه انجام داده‌ایم.   @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/444145" target="_blank">📅 01:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444144">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
اژه‌ای: دیوان عدالت اداری حدود ۲۵ مصوبۀ دولت و شوراهای عالی که خلاف قانون تشخیص داده شده بود را ابطال کرد.
🔹
همچنین بیش از ۱۲۰ مورد از مصوبات شوراهای شهر و روستا که خلاف قانون بودند نیز باطل شدند.  @Farsna</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/444144" target="_blank">📅 01:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444143">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9296f446.mp4?token=WAx02Fn3r2Sda6LtYr9rsmI4ZUo354MSx8Fkte6ghvZFEifu0YmbIV_CAHL4OAoPeVmotfH_klr-1a-jOgXVQtDqV9he6vhpgwfTRBAt2N_M1D2nC0yHuQwlHS22Pj_dWMMPXANWNcN4d587hAUMkOL2l2bbnNBez178tNsD4fodls2GKHVX5yjh7TT4OO3YWFeje6zcu38fe7tArIIelmZ_cof6Savhd_Uk51fCMhUgd_5HJTrpr-57alFD_rxXrgcfVjZP65AzUXT6rdFqKCgLQlBgZuSPqO7HTB8jlOc9UBG4a2Bh-r9_6tggMExae34HngjvkARBmPIw_qlafWRMeveHAEvd88cOoqXFXf8FWqlZbKBKCI3MpjICbhdHj32vsHMSZHYT6A6ZTBzJe3XIg9CJcSiffcl_rc5ZMz0peIOCxUcyZr5nW_VZINj-1ApWOBlbVtgRxxdO68K2KzCssU8HbSPZvCPIhsvzpfFzHI_sHrDtzJ07TpX3cyh6Lzp0R08P2hWflyHOW4uwLUDkOQKi8T5R1CTvJ1vAHhGWbiuJROL8KTcR7PdJ7IyG1_hQQE8SVXk73BmyI395kmD3a4Sy73ZwV1jb23O5dq2b30VLrljLXS8HpWKuXcO2YXvsbNg2Gz3y3OkBHjlGN_riFRVQaGaE6wSk2yemb9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9296f446.mp4?token=WAx02Fn3r2Sda6LtYr9rsmI4ZUo354MSx8Fkte6ghvZFEifu0YmbIV_CAHL4OAoPeVmotfH_klr-1a-jOgXVQtDqV9he6vhpgwfTRBAt2N_M1D2nC0yHuQwlHS22Pj_dWMMPXANWNcN4d587hAUMkOL2l2bbnNBez178tNsD4fodls2GKHVX5yjh7TT4OO3YWFeje6zcu38fe7tArIIelmZ_cof6Savhd_Uk51fCMhUgd_5HJTrpr-57alFD_rxXrgcfVjZP65AzUXT6rdFqKCgLQlBgZuSPqO7HTB8jlOc9UBG4a2Bh-r9_6tggMExae34HngjvkARBmPIw_qlafWRMeveHAEvd88cOoqXFXf8FWqlZbKBKCI3MpjICbhdHj32vsHMSZHYT6A6ZTBzJe3XIg9CJcSiffcl_rc5ZMz0peIOCxUcyZr5nW_VZINj-1ApWOBlbVtgRxxdO68K2KzCssU8HbSPZvCPIhsvzpfFzHI_sHrDtzJ07TpX3cyh6Lzp0R08P2hWflyHOW4uwLUDkOQKi8T5R1CTvJ1vAHhGWbiuJROL8KTcR7PdJ7IyG1_hQQE8SVXk73BmyI395kmD3a4Sy73ZwV1jb23O5dq2b30VLrljLXS8HpWKuXcO2YXvsbNg2Gz3y3OkBHjlGN_riFRVQaGaE6wSk2yemb9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: معضلات ۴۰ تا ۱۰۰ ساله حوزه اسناد و اراضی حل شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/444143" target="_blank">📅 01:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444141">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3198d874de.mp4?token=Nb3unjZaCf8oqWumAksXhX2UVHd0sf5GXIKLn4ghmyojqHHZOwKf7u7gf16ZL9wBPZEgCrWm6I8ySZvdhH5RfKn7JuEdTXdCvjbvLdDPM6n3n3fjzlAjt2oZqiUZxl28lixkWnth90QAewe2ZS7cO5pVAOr5MjXXQabORKiiYPQL8x3y4KJNR47m3kbmumPif65JrxjC8bAXWTiUPJ0XnYaBd5SqVktSKqnPosAnP3iQgJoUFex-YWDiycNZbYjIIBhnSVWEeIBRgy-UHW-3VcuaFo05Z0RDXvmMCNwnmZpGibFNmc4g5IdY3KOXXrpS_jj0a0BeSvp_eqiOMjHz9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3198d874de.mp4?token=Nb3unjZaCf8oqWumAksXhX2UVHd0sf5GXIKLn4ghmyojqHHZOwKf7u7gf16ZL9wBPZEgCrWm6I8ySZvdhH5RfKn7JuEdTXdCvjbvLdDPM6n3n3fjzlAjt2oZqiUZxl28lixkWnth90QAewe2ZS7cO5pVAOr5MjXXQabORKiiYPQL8x3y4KJNR47m3kbmumPif65JrxjC8bAXWTiUPJ0XnYaBd5SqVktSKqnPosAnP3iQgJoUFex-YWDiycNZbYjIIBhnSVWEeIBRgy-UHW-3VcuaFo05Z0RDXvmMCNwnmZpGibFNmc4g5IdY3KOXXrpS_jj0a0BeSvp_eqiOMjHz9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: برخورد با محتکران متناسب با شرایط جنگی تشدید شده است.  @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/444141" target="_blank">📅 01:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444140">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🎥
اژه‌ای: دشمن با جنگ ترکیبی به‌دنبال ضربه به ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/farsna/444140" target="_blank">📅 01:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444139">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a7a3f7b60.mp4?token=oF8TYim_jQr3SgJ_6an5tmsF4VbhwclsWDdOtAv8-xbG_6nQl3qGmA9cwYW5GmNT80mBNMNHWrZs6XXmloNmoz0IUy5SCvPZmsc7yR8cj4M6QIUVbxGbUSHlLPkWebEl2jwSLQxRYvk-sf7L8NNuoxMi7aqTuguje8njxpeyu_9almp5FOJYBL7FQHUBrhaE8EhJlUojTv2eOFAfGBi6qYJeQc2ikY3F4HQ-nMzrYmH0tSgS9oRhSui9sY9vDMMHLdOr5um2JqImD7DiC1ZHaPZeZEoMQbFM6oNIoZKA4POj2wKTh0SydevlKoMPq67_fK4lwL4-IIbL74CcyXMNUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a7a3f7b60.mp4?token=oF8TYim_jQr3SgJ_6an5tmsF4VbhwclsWDdOtAv8-xbG_6nQl3qGmA9cwYW5GmNT80mBNMNHWrZs6XXmloNmoz0IUy5SCvPZmsc7yR8cj4M6QIUVbxGbUSHlLPkWebEl2jwSLQxRYvk-sf7L8NNuoxMi7aqTuguje8njxpeyu_9almp5FOJYBL7FQHUBrhaE8EhJlUojTv2eOFAfGBi6qYJeQc2ikY3F4HQ-nMzrYmH0tSgS9oRhSui9sY9vDMMHLdOr5um2JqImD7DiC1ZHaPZeZEoMQbFM6oNIoZKA4POj2wKTh0SydevlKoMPq67_fK4lwL4-IIbL74CcyXMNUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: با ورود قوه‌قضاییه به موضوع ارزهای صادراتی و تراستی‌ها  ۶.۵ میلیارد دلار سرمایه ملی به کشور بازگشت.  @Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/444139" target="_blank">📅 01:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444138">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdf51c89ef.mp4?token=vJ5fj85tALjjNuhsgh5b_Rg3vo8R3Kdp--6ymDq4ItkV2_HetmtBKjkA9tmx4JJp72ylP44WImQfQPVo1RQK2py4gTarAY3AjviWkvlMo0XySEWHtFdlEhG_zmLnrJMFdjnWtbBHhd239Gf7hwrIjhkJEcHfVho_QMQhg8qJe-8SXwhvld1aCpFag9P8PTEraq0Wx6RVYq_moh9OtWTEOHzdliEJXI8ZnY1-au9y7gETw3H_21MROVybriy3ik-50HZluIw3Ba84ktAjhwRM2ASqRB4LPZmifl8ZJiR3WdMz0KbRFQCa8S5OhGn3i9wlgjQrUbi_lBOh9YHQ_CEZKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdf51c89ef.mp4?token=vJ5fj85tALjjNuhsgh5b_Rg3vo8R3Kdp--6ymDq4ItkV2_HetmtBKjkA9tmx4JJp72ylP44WImQfQPVo1RQK2py4gTarAY3AjviWkvlMo0XySEWHtFdlEhG_zmLnrJMFdjnWtbBHhd239Gf7hwrIjhkJEcHfVho_QMQhg8qJe-8SXwhvld1aCpFag9P8PTEraq0Wx6RVYq_moh9OtWTEOHzdliEJXI8ZnY1-au9y7gETw3H_21MROVybriy3ik-50HZluIw3Ba84ktAjhwRM2ASqRB4LPZmifl8ZJiR3WdMz0KbRFQCa8S5OhGn3i9wlgjQrUbi_lBOh9YHQ_CEZKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس قوه‌قضائیه از تخریب بنای متعلق به دستگاه قضا برای آزادسازی حریم رودخانه  @Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/444138" target="_blank">📅 01:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444137">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv5E4JXGnyvIqie01dGQN3qpQxdvMQNWbMaxUumNMvcdaRhOKgURRfI0l4TOInpr9g9S6vVlHbShEdmRc6QSANfMWzUrCLRxYR7OB4Djh7GG2YgqKJXT357TY-4ssjHhW4weXy18-dhZoTgTCziERdOEPLYKu1aPDbK6Kns6_YW1BaMKlZIkJ4QOpGd45fR50NZxbdrFutm3WwE6QhL6iQY8fBerkbfldky9cLVgutdomNBL1lbAB-HZ6z3E4-GpwUid6rg1XRq0aT35UtTO2v8SC1KDkTLjlPeX4-rqKvrqUCoFI-cdYzNCY5EC1S3Vd2bx2tdTRRwtPmsTSkmvFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌الله: با هرگونه نقض آتش‌بس اسرائیل مقابله‌به‌مثل می‌کنیم
🔹
محمود قماطی، نائب‌رئیس شورای سیاسی حزب‌الله: مقاومت در برابر هرگونه نقض آتش‌بس از سوی رژیم صهیونیستی، متقابلاً پاسخ خواهد داد و به شرایط پیش از جنگ جاری بازنخواهد گشت.
🔹
چشم مقاومت باز است و انگشت آن روی ماشه قرار دارد تا در برابر هرگونه نقض از سوی رژیم صهیونیستی مقابله کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/444137" target="_blank">📅 01:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-444136">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb884a97d5.mp4?token=pmpdlspKxq6CnNIrv9wD-LhfzF6UY8fGbhaV0Dtfx2JWFbWYAZ_P_wO04NeqEGxrro5mPNwnh1SBfU5jfEqNwMWwfW3Iv4BpNp8XTizznbX4sZIxP5XoMVkuppFwc9onUvfo3tuP5Ym-1ayef4VJO6u04Yry5QCzK4EdsQs4MLFxVLNHOqGMvV-U-AhTBEy7tW_6nBTMexKg1-UcdLGvaB9a-yMuMTJldAynJXIHYNFASyvq0Ypsnkgp5R5024mZH5Z5fI1gFw_EusA9AC61QwKhVdbdhz0g-XD782KskFahtapq81AOOfZiwhDbAAVS7iGn-XTZQFm_jTNzun82qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb884a97d5.mp4?token=pmpdlspKxq6CnNIrv9wD-LhfzF6UY8fGbhaV0Dtfx2JWFbWYAZ_P_wO04NeqEGxrro5mPNwnh1SBfU5jfEqNwMWwfW3Iv4BpNp8XTizznbX4sZIxP5XoMVkuppFwc9onUvfo3tuP5Ym-1ayef4VJO6u04Yry5QCzK4EdsQs4MLFxVLNHOqGMvV-U-AhTBEy7tW_6nBTMexKg1-UcdLGvaB9a-yMuMTJldAynJXIHYNFASyvq0Ypsnkgp5R5024mZH5Z5fI1gFw_EusA9AC61QwKhVdbdhz0g-XD782KskFahtapq81AOOfZiwhDbAAVS7iGn-XTZQFm_jTNzun82qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: بیش از ۸۰ هزار پرونده مربوط به اغتشاشات ۱۴۰۱ مختومه شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/444136" target="_blank">📅 01:02 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
