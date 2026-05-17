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
<img src="https://cdn4.telesco.pe/file/uLiHrKmQFDwRAfoSbjxhO_8raEwUasQgOerVISzeMq7oSTKEWbPy2KmpYEw1WJv5hQZZDS2OdsYhyXLAUbe2e0hKcFtq7mId3E8tX__hqxzu4kgoAMGY4RABJBHDaE0nHoQmLfqdXaHB6xdh33L6Uh6kGkWyyWLyYS-l40l7j8_kkSiV6LjrcrIQkSyhpp9eZ5zj_mC0HwOvUybj1CHsw2SblQhCEDHc1w2ACrEK_JRKp6vpWjRvnslTjuTIaztklNA2-nllcGz2sSkZVDZs7211rE52bOEU30dC_smyLKuYroJSUtZwLZGaNbQsfmuC_yedHDfjccwjXGJbQrjxeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.02M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 11:55:20</div>
<hr>

<div class="tg-post" id="msg-652619">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbvRDp9ZO_8dKVUMePeqKvwMzEfP05mkiPw7pa--BHI7FCsvLjXJnUUCa813no4W1gAXFD96T5CPvCYmQ0FfmCAZupzNCCZD5sfPx7esnSgk_zPz-MCuBoLax_4hNGU3GIeNHXMeFId7G7TUVQXluZwb47HoqjZ-WKulIwVsvVsAZ4_LcoKFxhvWMJFOaOHs1ZlevyTgA1OX6tqVQT80krgJ_iZWuOUmRvfAz6FWRDm8S8m90mork0-zrGl8CRrlIsLq2hsfAhU9cpritlfQ-EmMMjCSoGx4p2HYsf8iTKwX3-HxjBUiP3PpJnP1AEifoe5BzNEfZ9R24-I-NPqkKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به نصف سال نرسیده؛ بودجه ارتش اسرائیل ته کشید
🔹
وضعیت نیروی انسانی و بودجه نظامی ارتش اسرائیل روز به روز در حال وخیم‌تر شدن است؛ ولی با وجود این، مسئولان صهیونیستی بر طبل ادامه جنگ می‌کوبند.
🔹
روزنامه صهیونیستی «اسرائیل هیوم» امروز با انتشار گزارشی، از وضعیت وخیم اقتصادی و نیروی انسانی ارتش رژیم به شدت انتقاد کرد.
🔹
این روزنامه می‌گوید که «هنوز به نیمه سال ۲۰۲۶ نرسیده‌ایم، اما بودجه ارتش اسرائیل (۱۱۱ میلیارد شِکِل) به پایان رسیده است».
🔹
بنا بر این گزارش، ته کشیدن بودجه یعنی اینکه ده‌ها تانک آسیب دیده ارتش اسرائیل، تعمیر نخواهند شد و به آموزش‌ها و توانمندی‌های عملیاتی و ساخت مواضع آسیب وارد خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/akhbarefori/652619" target="_blank">📅 11:31 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652618">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
پاسخ ارتش پاکستان به هند: تهدید همسایه هسته‌ای دیوانگی است
🔹
روابط عمومی ارتش پاکستان: تهدید یک همسایه هسته‌ای مستقل با حذف از جغرافیا، یک اقدام استراتژیک یا ریسک‌پذیر نیست، بلکه از بین رفتن محض ظرفیت‌های شناختی، دیوانگی و جنگ‌طلبی با وجود دانستن این واقعیت است که چنین حذف جغرافیایی قطعاً متقابل و جامع خواهد بود.
🔹
فرمانده ارتش هند بیانیه‌ای تحریک‌آمیز مبنی بر اینکه پاکستان باید تصمیم بگیرد که آیا می‌خواهد بخشی از جغرافیا و تاریخ باشد یا خیر صادر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/akhbarefori/652618" target="_blank">📅 11:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652617">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZF7eXJ3Cwp7On1aNAHb73x501Jrcv97f3gWGQdIHFXUjTrwALHhJ6aOzrqraMImN6e49vfEwnRELUOJhgAwzlDinLoZRsEz4LpETQe7bCxtK1vuaMcMFL_IPt9WUCx2s8ooQkhMvIDJtc3TXm_5pNU8LKLuULKNkEIeNs4GOb65lkCwexOecCTE2Whn-RF_-vocSl9yzn6zV__nAbNZNjIFcK1LCdjcfHEoaeIYrvAKX3NTG7vO_PJpCU6s0JFaKUa8ojk6reHnVFTQnoKyLI4xdfv7kHQuOHNfGiSnrnEtvsBa1BIZ3d8zaFdMo8YvttzRgrK4qGXLinc6l-0J6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حاجی‌بابایی: مجلس موافق افزایش اعتبار کالابرگ الکترونیکی است
🔹
نایب رئیس مجلس: مجلس حتما با پیشنهاد افزایش اعتبار کالابرگ الکترونیکی موافق است و از دولت در اجرای سیاست‌های حمایتی، تقویت و پشتیبانی خواهد کرد.
🔹
دولت باید از هر ظرفیتی برای افزایش رضایت عمومی مردم استفاده کند و در این راستا از تمامی ابزارهایش همچون تقویت کالابرگ، تشدید نظارت‌ها و کنترل بازار استفاده کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/akhbarefori/652617" target="_blank">📅 11:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652616">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664ae9f9bd.mp4?token=plgOaCYUPyR7XUvblFhRNOtB72AMekmiy4UPVM_oIU8eX5OJUMxVL0jwXQpdKkO6nTBMW1ioiBeSZZN4wLnojkyCyrAzDhH2iDFn2p_SwEEEjR1KLpgaxXaWRUkaGzOGNg7jbArAhClq0eMwCdpt76_ptIbbjTtBKnmefjNQHf8bFP6gJDTeEaxRH6d7kel2TjlBvE6U9oVhQbf-Y__pT1ZSu3tDlLHl9rDTyrZNnprTbkJHQ1tZcvKkUeVrSMgMj-mNFwp8pM3uLXkqtbI1TyyvlXX7-yojpTUbzSoNnSiJ251g-MvzFIZmmIWEXtRQZMOYTIhSrwSpcQduK3kdxgIwPk_K1mt563ElYsD6QzxbYE-VWYceLbBDhDavdSAcrUjMjKPyKJ1Ax5qBEMbJzpL2RVPBE-_9oSsNA4-wxt5t7rYBylXYGG3zMq7u4zSn4SRLNbZFxOtlQDyu8xm2JNSqIgGj4iVAPanj5gPezZshbV3OII6WQFqsBWgUn3oHOeUFDBrtykS4eaIvc79iA-XvyPCPKvmxAedy-J2SIyRj6sPjFrQ_d4SqcOk9yrjSF7UAzW2UnxYe-_zazJKK56b33FiBHgX8zUzGHoWPeza3NGupVpoMIYakBgWze78Ewbb8L2kMYtr8MSy7bZ5Wgw8dUtbZQShzvcWtmlHCi40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664ae9f9bd.mp4?token=plgOaCYUPyR7XUvblFhRNOtB72AMekmiy4UPVM_oIU8eX5OJUMxVL0jwXQpdKkO6nTBMW1ioiBeSZZN4wLnojkyCyrAzDhH2iDFn2p_SwEEEjR1KLpgaxXaWRUkaGzOGNg7jbArAhClq0eMwCdpt76_ptIbbjTtBKnmefjNQHf8bFP6gJDTeEaxRH6d7kel2TjlBvE6U9oVhQbf-Y__pT1ZSu3tDlLHl9rDTyrZNnprTbkJHQ1tZcvKkUeVrSMgMj-mNFwp8pM3uLXkqtbI1TyyvlXX7-yojpTUbzSoNnSiJ251g-MvzFIZmmIWEXtRQZMOYTIhSrwSpcQduK3kdxgIwPk_K1mt563ElYsD6QzxbYE-VWYceLbBDhDavdSAcrUjMjKPyKJ1Ax5qBEMbJzpL2RVPBE-_9oSsNA4-wxt5t7rYBylXYGG3zMq7u4zSn4SRLNbZFxOtlQDyu8xm2JNSqIgGj4iVAPanj5gPezZshbV3OII6WQFqsBWgUn3oHOeUFDBrtykS4eaIvc79iA-XvyPCPKvmxAedy-J2SIyRj6sPjFrQ_d4SqcOk9yrjSF7UAzW2UnxYe-_zazJKK56b33FiBHgX8zUzGHoWPeza3NGupVpoMIYakBgWze78Ewbb8L2kMYtr8MSy7bZ5Wgw8dUtbZQShzvcWtmlHCi40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی مطهری: رهبر شهید بابت رد صلاحیت من اعتراض کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/akhbarefori/652616" target="_blank">📅 11:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652615">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9def2c56fb.mp4?token=StHawe__PWs6cjE1FOP2P_KIr3jDxCQC8kgDlkb4bsLT3iSe-ZmpOe2Os2iq_kdPn1Pcd31cSvt0-2xlIDnegKrKrBYS9kiCD-f4LRRBysEr22K8vqbpNEKZ4XsOC-Vcyh47LsvxwaNHUuXm7wQsw_P9NNSApRReskASJjcwpcm7wfgLvA_khWMzpGW4HGcc0ZWTviD4aNcP1X7RAub_w7DvQiu2f1ngQGHWAN6mxUcomqU_Tqr7xdPL8vmUoJZgo0eQZ6lZfXmidorNX0ezbtORrMgC8OW1lsv1TCuFJdIz1n6gFEe9SxqZserg9EmP-qP6DN-G14ETmQrdE0T3lIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9def2c56fb.mp4?token=StHawe__PWs6cjE1FOP2P_KIr3jDxCQC8kgDlkb4bsLT3iSe-ZmpOe2Os2iq_kdPn1Pcd31cSvt0-2xlIDnegKrKrBYS9kiCD-f4LRRBysEr22K8vqbpNEKZ4XsOC-Vcyh47LsvxwaNHUuXm7wQsw_P9NNSApRReskASJjcwpcm7wfgLvA_khWMzpGW4HGcc0ZWTviD4aNcP1X7RAub_w7DvQiu2f1ngQGHWAN6mxUcomqU_Tqr7xdPL8vmUoJZgo0eQZ6lZfXmidorNX0ezbtORrMgC8OW1lsv1TCuFJdIz1n6gFEe9SxqZserg9EmP-qP6DN-G14ETmQrdE0T3lIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماری از آسیب‌های دشمن آمریکایی صهیونی به میراث فرهنگی کشورمان
🔹
قائم مقام وزیر میراث فرهنگی: ۵۴ موزه در کشور طی حملات دشمن در جنگ اخیر آسیب دیده‌ است.
🔹
همچنین ۷ بافت تاریخی و ۵ اثر ثبت جهانی در ۱۸ استان خسارت دیده‌اند.
🔹
در تهران ۷۰ اثر، در اصفهان ۲۷ اثر، در کردستان ۱۳ اثر، در خوزستان ۱۲ اثر، کرمانشاه ۵ اثر، در لرستان ۴ اثر، در قم ۳ اثر و بوشهر ۲ اثر خسارت دیده‌اند.
🔹
بیش از ۱۷ مکاتبه با نهادهای بین‌المللی از جمله یونسکو، میراث‌جهانی و... انجام شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/akhbarefori/652615" target="_blank">📅 11:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN8nF9IMM5TOmsDTlyJ_MShJao1sK-JnSHfvcMXUgLw7uAEPlXLlQMcqydj_7q6ndQ5GOZ1eoSkwKM4_WGPaFXAcNGoVftRkBwUBHCkxviGi1oRMV2H6ER28-pcP6Bz773Qt_PdLnZCa1_tkVVFP_apPPWQf2GkRP-LoGzHfhCsf_fwHliRmND-gzvLGOehxpb-5EymWY1JggOJwEnmRkNPRq2TB6xfevxdEfmMUEbYwM4XfMTMYt2S589xxU1Wu-8sCwfuFsfB4lx4TEL2FYBgvdvJqlLUALhLbyBUtR5MGC4Ivqmj58LVLwOZFJnWj9wc6eXUCgFeehGWRCc5xBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دادگستری قم: آپارتمان‌های مهدی نصیری و وابستگانش به‌دلیل خیانت به وطن توقیف شد
🔹
رئیس‌کل دادگستری استان قم: با گزارش اطلاعات سپاه و پیگیری دادسرای مرکز استان مشخص شد که «مهدی نصیری للردی فرزند گل‌محمد» دارای سوابق مالکیت ثبت‌شده غیرمنقول در حوزه ثبتی استان قم است که براساس مستندات، این اموال شامل ۳ واحد آپارتمان متعلق به او و وابستگانش بود که در راستای حفظ حقوق عامه با دستورات قضایی توقیف شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/akhbarefori/652614" target="_blank">📅 10:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652613">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3FgLMC-Mnjbva7J38FFyQNILPXop87H5VYXI7yew_46OocUqZ_hanXU263s9cVpimo-9TTfM_5SeXBM1VyfZJVylVlPzvqlkZGMBlkehFYM-czRzQxC8Uo8U77pVZ3OiuGCsL2r0hL0H21G_zoagxidR_wkt-V_uGBstL1FsAhgzD_nymfx6uWrW7B1jgBHFRhO2NXvMMFf-yKA66AzMqjzSNZGRuoWdyzTojmwYfWCVOr-z301TKCMgCo94z154uNzTFohGiOmGuQlf7XWjt1sd_LOD_mWsqSvbhBszLTTVlKgkiaoJKtOUUo3AfGG89v1SY9sqSEokS6VSrAHxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حق هسته‌ای ما به آمریکا ربطی ندارد؛ از حاکمیت بر تنگه هرمز نمی‌گذریم
🔹
علاءالدین بروجردی عضو کمیسیون امنیت ملی مجلس با بیان اینکه مذاکره بدون پذیرش شروط ایران بی‌معناست، گفت: جمهوری اسلامی ایران از حقوق خود در تنگه هرمز و همچنین مسائل هسته‌ای کوتاه نمی‌آید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/akhbarefori/652613" target="_blank">📅 10:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652612">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a1745ced0.mp4?token=nD9vR_ZQyYA7f-l5SK8wfGAffQXWNNROs9iNRQ2kW6gD5dTtOCIv_NDpHPICBAHA5l6LpcTobxmS9rVJqLPdPEiCGeo4ocolRPi3wrVLR0B4GU0SnqhsT-xrvm70wcvMQnS9vd7TM5G7CLQ_TNs-l1s5jsxpqbsgyV64U5PxqKhJ-28VXM8oIM5KI_v3ZkbMHBQrQSWiksaAdpExSjp1tdSsG--4PmBq-k-QSkZ3zMoTpS3YqmgG2P0VxGqgZIO2pexhlMjOOFbOKxXtgCr3kk3Ihr4PfO-gCxFHFkx95yZFut332NMnFV7AGd-5zxaZhKqXjbUrYoV9rihofpsWfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a1745ced0.mp4?token=nD9vR_ZQyYA7f-l5SK8wfGAffQXWNNROs9iNRQ2kW6gD5dTtOCIv_NDpHPICBAHA5l6LpcTobxmS9rVJqLPdPEiCGeo4ocolRPi3wrVLR0B4GU0SnqhsT-xrvm70wcvMQnS9vd7TM5G7CLQ_TNs-l1s5jsxpqbsgyV64U5PxqKhJ-28VXM8oIM5KI_v3ZkbMHBQrQSWiksaAdpExSjp1tdSsG--4PmBq-k-QSkZ3zMoTpS3YqmgG2P0VxGqgZIO2pexhlMjOOFbOKxXtgCr3kk3Ihr4PfO-gCxFHFkx95yZFut332NMnFV7AGd-5zxaZhKqXjbUrYoV9rihofpsWfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر مجدداً مورد تجاوز دشمن قرار بگیریم ضربه‌ پشیمان‌کننده‌ای به آن‌ها می‌زنیم
🔹
زینی‌وند، معاون سیاسی وزارت کشور: ما به‌دنبال جنگ نیستیم، اما همه ارکان کشور، مسئولین و استان‌ها آمادگی کامل دارند.
🔹
اگر مجدداً مورد تجاوز و تهدید دشمن قرار بگیریم، کار اداره کشور را توفنده‌تر از گذشته و با آمادگی بیشتر ادامه می‌دهیم و ضربه‌ پشیمان‌کننده‌ای نیز به آن‌ها می‌زنیم.
🔹
اکنون شاخص‌های امنیتی نسبت به اوضاع غیر از جنگ بهتر شده‌اند که دلیل آن همراهی، انسجام و حفاظت مردم از کشور است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/akhbarefori/652612" target="_blank">📅 10:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652611">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87d6e980d.mp4?token=Wp56IM0lufoKOnUw0RHq4xN8YvT-1WAyxkhk_dBtU8N7TuytrR0GrJpz1Bhr1JIDrOQFhu44bYijlfC3srGiEGgHw6lr6-LzUUBvrekAGZHFB8vaFNAwHwQPK-yK6IMa9SaNgWw9OOR--6L4TjJ3cMtXOJPo3uMDBmYmxnkSqreik5-om8lj3w9EzzxALVBNDvHLM2ZV9rIGKJ57uYAPl3wRyc5Tofbv3Pg47NI3i6wzOpjpV0vixjkFJ9AbYzJgZvSRAEJhGBwiwqdqus-qY83NkzIRxIVgvqpfWpGm_O2NA40DXpcdhD8j4C9Ocpd4NvERnkiiU7ZS05xOPn32ZyAziLwJg7AYwa1HNQsLCTQLP4LmSrbkDQJ1zLsbDCzr2WcyjMkP01Q_U9dU5g2aTlHDtKS4M5ll2ZK2-zeP3mZG9wiH0BGtQUtbiVMEZYjr0tc202CHlg8S_9Ay23c7kGZqp6-XzKqDbq0XW0_Jl0bMlot4DhxomjsKDrE8pkRr2_5xiZW-Xu7YngEZVRI7z9KTP9VvW2zAN7iZN_yZzMyFJaGywX8bRILPbk7z18SZkoF0G6w4VGz6MN1xGqlUmd62xQHY7eEH-6xQRYV-TRugiMtySZuQQcv_3eI8yQiV6_t-Sn0cgdUITIXeqfMtPL0Ic0aMMcfHtFrcSvC_LbE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87d6e980d.mp4?token=Wp56IM0lufoKOnUw0RHq4xN8YvT-1WAyxkhk_dBtU8N7TuytrR0GrJpz1Bhr1JIDrOQFhu44bYijlfC3srGiEGgHw6lr6-LzUUBvrekAGZHFB8vaFNAwHwQPK-yK6IMa9SaNgWw9OOR--6L4TjJ3cMtXOJPo3uMDBmYmxnkSqreik5-om8lj3w9EzzxALVBNDvHLM2ZV9rIGKJ57uYAPl3wRyc5Tofbv3Pg47NI3i6wzOpjpV0vixjkFJ9AbYzJgZvSRAEJhGBwiwqdqus-qY83NkzIRxIVgvqpfWpGm_O2NA40DXpcdhD8j4C9Ocpd4NvERnkiiU7ZS05xOPn32ZyAziLwJg7AYwa1HNQsLCTQLP4LmSrbkDQJ1zLsbDCzr2WcyjMkP01Q_U9dU5g2aTlHDtKS4M5ll2ZK2-zeP3mZG9wiH0BGtQUtbiVMEZYjr0tc202CHlg8S_9Ay23c7kGZqp6-XzKqDbq0XW0_Jl0bMlot4DhxomjsKDrE8pkRr2_5xiZW-Xu7YngEZVRI7z9KTP9VvW2zAN7iZN_yZzMyFJaGywX8bRILPbk7z18SZkoF0G6w4VGz6MN1xGqlUmd62xQHY7eEH-6xQRYV-TRugiMtySZuQQcv_3eI8yQiV6_t-Sn0cgdUITIXeqfMtPL0Ic0aMMcfHtFrcSvC_LbE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آغاز پرداخت تسهیلات  ۵۰۰ میلیون تومانی مسکن روستایی تا ۱۰ روز آینده
🔹
جودی معاون بازسازی بنیاد مسکن: تسهیلات ۵۰۰ میلیون تومانی مسکن روستایی نهايت تا پایان هفته و یا ۱۰ روز آینده توسط بانک‌ها پرداخت شده و امسال متقاضیان دهک‌های یک تا ۴ در کلان‌شهر‌ها هم می توانند از این تسهیلات بهره‌مند شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/akhbarefori/652611" target="_blank">📅 10:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652610">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecJlwL8pC75Re_Jc_5K_ZHtggc7LDZG5XFR8V9G4otXI3azIfOh5TSAE3PLAKlvpwcNO2268B1L2ohiaaSYj5oU3uK4c6NrKGHpd5vtj3Ys_5HXXBNeUuQbbKq2yJkDx7m5XNYDaGBptRB1fCxMcIAftfpJXJ81b87CfanTCqiYvQXenB-fmztIAXTnF4KgKBM2sMTrrMo8BMc4YetdmBHqcUn5FACctSzQLxNoSI3GKHJwGmVMJhnsGKwldL08LKqdRW2E-iDmBjwqDbBuTbMNVICC4b-PaYgZotzlMhewsNTNepaW9mrCNlyPO80rnUN6p3oJ-Py6tn1iD5DvrIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاریو: ارتش اسرائیل در حال تجربه فروپاشی نیروی انسانی است
🔹
رسانه‌های عبری با استناد به گفته‌های رئیس ستاد ارتش رژیم صهیونیستی، گزارش دادند که ارتش این رژیم در مرحله فروپاشی در بخش نیروی انسانی قرار دارد و این در حالی است که افکار عمومی از عمق و گستردگی این مشکل بی‌خبر است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/akhbarefori/652610" target="_blank">📅 10:05 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652609">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6379e24.mp4?token=Nx1HJIvROGxyu8OnnIamCGiYp6yH5zp7Pnu-m4TiRUwDTdsQDqM4bbnKDQeWpeitzQJ2ooG9EFH6huBXzFT8f2VLEAfuLf3kMkpcsOiJETA0xbnfeSB9z28pvSucucxx0UpQlK6duDDK1P_9qLQ0sES49JdP8hKcBxLyDc4K_ILtooFZk1jJzgN_g69xCWF8Jb2KgneZfx52gM3RJ__Q44qPbu43RPWPC65bGesisMohI0h-cleQE-J-Lppbs_jOtqSmTj1XPXI9Qb1tr7ik4fUINCMXE0V3xyC11D1RR_B_Dpb7-4b9YHvlH-apmvpahzbdEXB0fzcnF8KZyQA_rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6379e24.mp4?token=Nx1HJIvROGxyu8OnnIamCGiYp6yH5zp7Pnu-m4TiRUwDTdsQDqM4bbnKDQeWpeitzQJ2ooG9EFH6huBXzFT8f2VLEAfuLf3kMkpcsOiJETA0xbnfeSB9z28pvSucucxx0UpQlK6duDDK1P_9qLQ0sES49JdP8hKcBxLyDc4K_ILtooFZk1jJzgN_g69xCWF8Jb2KgneZfx52gM3RJ__Q44qPbu43RPWPC65bGesisMohI0h-cleQE-J-Lppbs_jOtqSmTj1XPXI9Qb1tr7ik4fUINCMXE0V3xyC11D1RR_B_Dpb7-4b9YHvlH-apmvpahzbdEXB0fzcnF8KZyQA_rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکس امام شهید و رهبر انقلاب در کشتی توقیف شدۀ دشمن!
🔹
تصاویری از داخل کشتی توقیف‌شده در آب‌های خلیج‌فارس، توسط دریاداران جمهوری اسلامی ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/akhbarefori/652609" target="_blank">📅 10:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652608">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
تکرار جنگ جدید علیه ایران پرهزینه است
🔹
احتمال بروز جنگ اسرائیل و آمریکا علیه ایران در زمانی نه چندان دور وجود دارد.
🔹
باقی ماندن شرایطی که وقوع دو جنگ قبلی را در پی داشت، احتمال شکل‌گیری جنگ جدید را توجیه می‌کند.
🔹
در عین حال عواملی که سبب شکست دشمنان مهاجم در دو جنگ قبلی شده همچنان پابرجاست.
🔹
همین موضوع تکرار جنگ را برای دشمنان پرهزینه و دشوار می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/akhbarefori/652608" target="_blank">📅 09:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652607">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB55e8kkqq7L_XFi5fA52SgEx2PBcspZw9Hq5yNDANfVvpQgyu30Jmq_9VlAzF2IsJhdk9LM4MsAtyT2QKiG3-0g-LHq87HUCimIsGzyrTu-1xdH-R8pAGnGL60t8JCjEBl2tYyMYtFTJKBRcSCDRL1RV8tUiWPwn2mnmXYIoO0P-YuGbmojRpjfo_ggN1F59HaoU6C3T8NBnv5TKJ7totgAd4HdJ4-0OwzllJyj8YW5sHtBxpeo1czd8Iku1m91mq6NIJsnoLSAzgDYUHnsuqescgyZzfzMK5nJpfalQy-mtG56Hi6mLviqlPkFLnn_bmLU2n4LZhCdIJCtdUgerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهر بررسی کرد؛‌
🔹
جنگ معادلات در لبنان؛ از راهبرد «زمین سوخته» تا نبرد فرسایشی حزب‌الله
🔹
جنوب لبنان عرصه درگیری های سنتی نیست که نتایج جنگ با مقایسه خسارت‌ها و تلفات سنجیده شود، بلکه به میدانی فراگیر برای جنگ فرسایشی هوشمند منطقه ای تبدیل شده است که در آن آتش بارها همراه با پیام‌های سیاسی و تاکتیک جنگ روانی در هم می‌آمیزند.
🔹
همانطور که راهبرد نظامی رژیم صهیونیستی جبهه‌های نبرد در منطقه از ایران گرفته تا عراق و یمن و لبنان و فلسطین را مجزا از یکدیگر نمی‌داند، اجزای محور مقاومت نیز باید در تصمیم سازی‌های خود این نکته مهم را مد نظر قرار داده و راهبرد «وحدت جبهه‌ها» را مانند گذشته تقویت کنند.
🔹
رسانه‌های صهیونیستی اذعان کردند که تهران با وجود ادعای مکرر سران تل آویو مبنی بر اینکه ایران و لبنان «دو جبهه جداگانه» هستند، در برقراری راهبرد وحدت جبه ها موفق عمل کرده و این موضوع در مذاکرات اخیر نیز کاملا ملموس بود.
🔹
سرتیپ مجیب شمسان سخنگوی ارشد نظامی یمن در این رابطه تاکید کرد که «جنگ چهل روزه» در حال تثبیت یک معادله بازدارندگی جدید است که بر اساس درهم تنیدگی جبهه‌ها بنا شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/akhbarefori/652607" target="_blank">📅 09:38 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652606">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0683cf1ee6.mp4?token=XFHTlWHm1aDK2kgsSMieOlv34CrzKwYr5EJVu0-6-tRjiloK-YoKY9aWxL5eEChf22AA33a-hihT6UlYkURcjpwyhNLXU-pJ2wb2dEcmaxgOcHkV-bkWixS_1p-O1uou79-IA18uHlxO5I34soIrC64KtryqBUHwCmHZupsNOgflreLqjGgFq3HFzf4j07q5sXruWPZwQj7XZYtzglgfhcU6x1bI0BlEJyZWgogHf83tn5GoW33s_pmBb0L5yIhB74EGU48A4UlxXNZqcexwBNWHpQ3Cu4-7KTMkDqhX8yX-etg4X2RXA0LvrCzn0rgyTQUfIJ4uNWUlYd_OW1Y0PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0683cf1ee6.mp4?token=XFHTlWHm1aDK2kgsSMieOlv34CrzKwYr5EJVu0-6-tRjiloK-YoKY9aWxL5eEChf22AA33a-hihT6UlYkURcjpwyhNLXU-pJ2wb2dEcmaxgOcHkV-bkWixS_1p-O1uou79-IA18uHlxO5I34soIrC64KtryqBUHwCmHZupsNOgflreLqjGgFq3HFzf4j07q5sXruWPZwQj7XZYtzglgfhcU6x1bI0BlEJyZWgogHf83tn5GoW33s_pmBb0L5yIhB74EGU48A4UlxXNZqcexwBNWHpQ3Cu4-7KTMkDqhX8yX-etg4X2RXA0LvrCzn0rgyTQUfIJ4uNWUlYd_OW1Y0PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون| کشتی‌هایی که پشت دروازه‌ «تنگه هرمز» ایستاده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/akhbarefori/652606" target="_blank">📅 09:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652605">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOtSXr0C6pgbkMU053Xi8wjDsbtNKDHu9Axdlmd9ab-4i163Jcd3MitdWu-DERtNzLYvbl9fOamfG_-BZipNUF0s1EoLUFIjXqAyyASdtszb8PGKOHspBv8UvZ-v_OsfGwdrLUNor8FjUWix9srAnYhFAIEewNsH_gd6kRkKcQYFAolbANjk17stUA-Op-u3PZxYouGMGrQlCQFctEAHuJ0ldw_KOhmGI2DaU3xvNH-Y-aRifB2BXCzqdeBT0SThdufiUoi-tTrJNuoXt1AfZ1ZZBkUgY3XcOOrFwbybg6jc2yoMMi71zFeN06JUv62pGwVSkSLNgaEj_sUIJ6DKpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اذعان مقام سازمان ملل به تجاوزات تل آویو علیه فلسطینی‌ها
🔹
خالد خیاری معاون دبیرکل سازمان ملل در امور خاورمیانه تاکید کرد، رژیم صهیونیستی بیش از ۴۰ هزار آواره فلسطینی را مجبور به ترک اردوگاه های شمال کرانه باختری کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/akhbarefori/652605" target="_blank">📅 08:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652604">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0541e6886.mp4?token=j7nwdF_sqRkFghkqw8PFcS33iCoUDCfj3NUig7xo4obrMivrJH5sRE-jspqKiwTWpjftV5YG6JpqE1Gvb53n8p5yxxPzkUZQLj1Jiq-39XsYTiRBRlBIGdD3ugYU5VpeWazs5BM_5hvSpMK7wB_7SN1c6hGUSfYmd33LePcXcKBuZsLygqrSrhKPsuv4-swyT6holsckMBu_4TfmHvqSnZMW7FIcZwq5O09wdohDdBt0hceNITdJinXUaoNQawmsqkUe_OIvm2lpIaznRwXmgopYYUisrkGuWiD06SmtQjsoo5YJ6wXV92jOMOEXZAVjjl2rSyhBxNzg5aZrnkanRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0541e6886.mp4?token=j7nwdF_sqRkFghkqw8PFcS33iCoUDCfj3NUig7xo4obrMivrJH5sRE-jspqKiwTWpjftV5YG6JpqE1Gvb53n8p5yxxPzkUZQLj1Jiq-39XsYTiRBRlBIGdD3ugYU5VpeWazs5BM_5hvSpMK7wB_7SN1c6hGUSfYmd33LePcXcKBuZsLygqrSrhKPsuv4-swyT6holsckMBu_4TfmHvqSnZMW7FIcZwq5O09wdohDdBt0hceNITdJinXUaoNQawmsqkUe_OIvm2lpIaznRwXmgopYYUisrkGuWiD06SmtQjsoo5YJ6wXV92jOMOEXZAVjjl2rSyhBxNzg5aZrnkanRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردی که نامش با عدالت در تاریخ گره خورد
قسمت بیست‌ویکم پادکست کافئین منتشر شد
☕️
روایتی از زندگی خسرو اول ساسانی، انوشیروان عادل
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/cyoMCF_5vUc?si=evsHZ1zKo2U21n1d
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/akhbarefori/652604" target="_blank">📅 07:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652603">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین - قسمت بیست و یکم</div>
  <div class="tg-doc-extra">انوشیروان عادل</div>
</div>
<a href="https://t.me/akhbarefori/652603" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
انوشیروان عادل
🗓
این قسمت روایت یکی از مهم‌ترین چهره‌های تاریخ ایران است. پادشاهی که با اصلاحات بزرگ، قدرت ساسانیان را به اوج رساند و نامش در فرهنگ و ادبیات ایران به نماد عدالت بدل شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/akhbarefori/652603" target="_blank">📅 07:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652602">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg2k0_HtgSDQzTED8tSV_3GGv1Gt-AqiSq1mWV7ZQSxphz--TlAlfYwtHQ9o3D3RuaA-8Ghypo2a5I4UzXuC1sl0Z2-RpXKzMWJAJs8lL4byCQUEaDCeuic-W3ffOeyllihbxHh5uUx60G_ox14JVh6Vc8qWpO57mA1fEkaHPQIizu3I9Sm-uZABQzixZxa7dzFZZamA43T4YHu1DS5NI7LRn8TlvcWwq2um5x3ioeXkLG5sQq4CdL-wjTQdZzhdfljLLRMCYCz4p2bRdmJoC0H0qIZoaFrAYA9iC_kcj2D3g7E9KYB8lexnKardOnoNoSac5gZIiZ-sTTz9WrohTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۲۷ اردیبهشت ماه
۲۹ ذی‌القعدة ۱۴۴۷
۱۷ می ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/akhbarefori/652602" target="_blank">📅 06:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652596">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDQGpSmFx9rLQ0pQ8-BCRdDkWdvaQgwKfxYE2J1Die8QJW0-yZY2kbQ9Uj4Fe04bzQGHRa2V3z_KMvcLAlpRnFcbkFsioP8tgrE8LOWi3Up3yeoYB97esbXUzADjsbBwFhL_e-jP288IoEM0HqScxxHiQ-Ky9lXvc6oUtvd8OhWts7NWBuxKBNqfSLfSWCsKK1uq74cYQHVBiKlsbL4K5tZkt2CFkMLyC43znTAJm49R9CGXQBcQp18lQNxcoIJAbBd-6Jwg-ei-PRWbMEH3m5mjJNfxN-69TSuvcxy_CQqtgowD1L5c0x9i5XDXH4f8PRA1NMH_vOB3Pn-HGBK2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BrOH-o6i1XFrML0-5SfKQ0bwGmqliJiPhed403l31_rFTuR7GRQ14EzeQCcVxPb8q7vHnQnxagdak9_cs2xkkX2KISgifzzYwAYW0Vhfi5bhrK1Gbz3440fgoTAdjKjU5NljXDKRjxw_kDE40dM_tK2WtndDGD7VmFmozYiSzMaTL_kQhXxgHJqIk9W38IUoOQoneJopIkKIyWM1xtThthFiwuysWoSqV6fl47lzrIxjByrL8h3E2dy7jRIbDlho15zbel6A2hjCVBmVxPHBKL0oAMGxOw235ClpLMcgndB0oha2PuSQT10YbncH2vCa3lV9qZ1vkCyOT0SnYPu9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKuPeZTHi5bz8IwfTTMWYBtq46mbUe3VVE0UH0LGem8WlOPw9IM2WNEGDp5pxymI0w9xIpJ90bEJgDuLUi9Az3Ao-7wrDa8SS_6Dc4M9MMn_ixpqSjeHe3rKel44-vZD-Ic7udiBf0PxAKTfLegM2o51170O6zAyT6TTb_arqgTcA57DpLYzPr2yjUW7CVbCzQZLOmyM7-Dhm9CicqR9KWX8sQoshWAy7uuMKFJ-dKih0tOkx9-ZSEwBm3kK3QXtpcDvroUbeXYcRup3MNGDs8kq8KxaGK5Y-beG0gc1hh-xOjzGpuv7iYGLcrDG9GO7Drq5rOKUC2Utn410CXXv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LeYcQZ4Qh6DF0tdfOdi71zRmbv8P0CeSRGNoSz1NWCuVbRHdkSC0Bsz7g6NIawBUhKSAYef_0L2i06H5_bAzSN7VauQ_BYn2xssgIKDVh2EVKPiRHJW-IiPQCtA4V5CwFNHA6fLks4evcuUxb-6sP5AvXxITUWH1gZkUl_fHDhF8c5mlvOq5pax1pqT_w2jAhPdUwTuSrPD5bDjvjwqWP6d1k6dFvL_fT7YLU0oSaOhfP4m4OwQG5kTWiT-cULG2_6KgCH2JgNfWHfKjSebL3e-cKVtsJf5iHB2lfPVc9zrY1jqd761hmDIEnrdekF3Pwd1ZhR9YM38e54BaucWLbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUwVnrfnlh8_WzPNrCd66Wnd565IbrGifLaDN85aJMqfRtnWT5uzl21DXSXoIWjnCxUAnHCxK4Km2JxN-nrd8uWCCd4xWgOhE5lHwo-KPk_NAFFsYuAQrn-bOhmW8RQPwE7PoYX7UU8JwH0kXRN1LV3fWCdZT8NUvAbcrW2gdzW_uJBlB3cvql0OElKu1YgUs3a41oMc1j39nyPeftY_73BEDm9deazEVfiwYPHpn88JcGXwQ--Kv3asawJhfjUtVOp69guGqY3EkOFTS-8CTsi8jNQDKepH871GNa8f6CXK-weNISWhBY4RGcZoLuRoMJf-ISu5O4q3sY80HmZJOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gEx_mNgPboBoDQsUPTHLLcuFD_yfUjknmA3bn06pOvHdpsOWaOFIelS3CXrAVs2CqxSxed1wiTOGHUkS1Vnb2aeSJxmpnW6y_4i53V1D55KcSOw6bBGbEvAhggjl9-fooXBB0o-LyxWSPpix5YMdaj_IcdfKy0JbSoGt8NfYqbVOTSsDq05LbzySw_1OhiZ6PYuIrkpXgkusb8bFmk5WYK-yI4xcWizCgErneVn0jNvo2R3CvTCBJbh85mKDuiDgE8vQbTRXRkQcELqxEdqpjwBZbHm3RPtAjtPV2BhJFWFxIpYzVQNFIVf7ZjUMppOKqpDZwhPT9qQXHZzVHPxrag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تظاهرات ضد جنگ امروز هامبورگ آلمان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/akhbarefori/652596" target="_blank">📅 06:58 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652595">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aa48d6eb3.mp4?token=tz3qU0U-ee7z22BHhGv9YoLU7lmaU8g9gPj2DFiyNo1q7m9piLtxyWA0bPK37jlZBi5Bb12j1oL3opZzlMgk35bugnQwMs40YA3rTqvMyswnGhMUDhO2QG3oTMRna-YICwzry3H8VkW4ijCDR2hxM93jht__V8JPaRkfiWudng0QbE5si4U8kETw4kAz7SVJQEkBFdl4OzEAo1xa7preC0BZT1DPYpSQrDYYrG4djKcWRiOtklPoqNGhPDSIUNQGnxIE8iwkKXn8PaoawDd_9MgFH5kkFpd6FfyWcuM30MS24zYXE2UTBRq1yQlHb_6qYmtrVIoOuFQekhFvICibBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aa48d6eb3.mp4?token=tz3qU0U-ee7z22BHhGv9YoLU7lmaU8g9gPj2DFiyNo1q7m9piLtxyWA0bPK37jlZBi5Bb12j1oL3opZzlMgk35bugnQwMs40YA3rTqvMyswnGhMUDhO2QG3oTMRna-YICwzry3H8VkW4ijCDR2hxM93jht__V8JPaRkfiWudng0QbE5si4U8kETw4kAz7SVJQEkBFdl4OzEAo1xa7preC0BZT1DPYpSQrDYYrG4djKcWRiOtklPoqNGhPDSIUNQGnxIE8iwkKXn8PaoawDd_9MgFH5kkFpd6FfyWcuM30MS24zYXE2UTBRq1yQlHb_6qYmtrVIoOuFQekhFvICibBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئویی که سرباز اسرائیلی از جنایتشان منتشر کرد
🔹
‏روژ گذشته، یک سرباز اسرائیلی ویدیویی را در حساب خصوصی اینستاگرام خود منتشر کرد که تعقیب دو کودک فلسطینی با یک پهپاد کوادکوپتر در نوار غزه را نشان می‌دهد.
🔹
دو کودک غیرمسلح از حمله اول جان سالم به در بردند، اما تعقیب و گریز ادامه داشت و از سرنوشت آنها اطلاعی در دست نیست‌.
🔹
این سرباز متعلق به تیپ کفیر اسرائیل است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/akhbarefori/652595" target="_blank">📅 05:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652594">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
شهادت سه فلسطینی در حمله هوایی رژیم اسرائیل به غزه
🔹
در حمله هوایی رژیم اسرائیل به یک خودرو غیرنظامی در محله النصر در غرب شهر غزه و اردوگاه پناهندگان جبالیا در شمال نوار غزه، سه فلسطینی شهید و تعدادی دیگر زخمی شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/akhbarefori/652594" target="_blank">📅 05:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652593">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOd6ixZxYm294Zss0fy4-l4Cmfy3Zk_jxFxk68bTDS2lsPY-wlBbGoKFvSBc7vTXPvPH23QImRClKxFhisdEhlLXrqLW_smJ8lQrLoxZOBNcKo4SEQdy5MTREfrB8trxPSYjVagrVDdCRIArHt0hPdTVjXvTOUuE_154N1DHQzjpFlvv2cJmHp9z-9xaSl-fz8_VmqfWsSBIoSc6sT80pyIf1yeyBIOmn_Le_q6q_LhCCgt6_0MB91-G8mFkGQAd_tvvQYlTNDhas4oZcGyYNNSVoRDZg5p-aIwwtQgdkA6hWiwIdsInq626L2DQduLbfSjgYLjeZjES9gj8zzRphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نماینده روسیه در سازمان‌های بین‌المللی: اگر آمریکا و اسرائیل حمله به ایران را از سر بگیرند، نشان می‌دهد که از اشتباهات راهبردی گذشته خود هیچ درسی نگرفته‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/akhbarefori/652593" target="_blank">📅 04:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652592">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
ایران ترور فرمانده کل گردان‌های قسام را به شدت محکوم کرد
🔹
وزارت امور خارجه جمهوری اسلامی ایران با انتشار بیانیه ای اقدام تروریستی رژیم سفاک صهیونیستی در ترور «عزالدین حداد» فرمانده کل گردان‌های قسام را به شدت محکوم کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/652592" target="_blank">📅 03:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652591">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
گردان‌های القسام: ترور فرماندهان بزرگ، مسیر مقاومت را متوقف نخواهد کرد
🔹
گردان های القسام شهادت فرمانده شجاع خود توسط رژیم اسرائیل را تسلیت گفت و تاکید کرد: دشمن جنایتکار صهیونیستی اگر فکر کند ترور فرماندهان بزرگ، مسیر مقاومت را متوقف می‌کند؛ دچار توهم است، چرا که این خون‌های پاک هدر نخواهد رفت و فرماندهان دیگری جایگزین آنها خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/652591" target="_blank">📅 02:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652590">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
«افت شدید توان رزمی» دلیل عدم مشارکت انگلیس در جنگ علیه ایران
🔹
شبکۀ فاکس‌نیوز با استناد به دو گزارش رسمی از اندیشکده‌های نظامی و پارلمان بریتانیا فاش کرد، دلیل اصلی عدم مشارکت لندن در حملات تهاجمی علیه ایران، «افت شدید توان رزمی و خالی بودن انبارهای تسلیحاتی» این کشور بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/akhbarefori/652590" target="_blank">📅 02:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652589">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
شبکه «کان»: به هیچ وجه امکان ندارد انفجاری که در «بیت شمش» رخ داد، یک انفجار کنترل‌شده بوده باشد؛ آن‌ها قطعا دارند چیزی را پنهان می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/akhbarefori/652589" target="_blank">📅 02:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652588">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9JfmagcpWoaX8HzmYx1nI9BrsRHhUheymix3VfsnYDOfJJhEFZslf2F444wpc7AVd_H17g2LEwtmjyBzlTXLePM3sAku0VomLSilEL_JGazoJpIL0vVRKbNfG69z6vYpFd6IfAWoq7fCDRsURO7G8diFZCo-Ua7lZqErkyo-DEkjfxBhkpfsZZCPTXroH5QrW2XkhjpSmebQhlUGxxDkT4Gvq14SmOJ4aAZN0k13EnVpU4i-IfXBh4aDcWB5bpZIvu09246Oi7kVYoXHVw1gjyunBxq9bCiBxfBvhN_LuQhjPOhr3ta9Cxe7RKvVYfNhU6Ho0UsB6n0StRHr4KUww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیۀ وزارت امور خارجه دربارۀ ترور فرماندۀ کل گردان‌های قسام در فلسطین اشغالی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/652588" target="_blank">📅 01:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652587">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvCWpOSkzWLCzYqxGi61Kx2SnL_ZPx0FfG1IWK-kh-iWaO81kn77Qso1iBcbNTMkYoWCwGJD5p14V5ieo4JQmtR24BKztZbcr0tir5m8qbXln3Oh2U9T4Mm-Lsk2fEm7eq4C5qmH4h9VFFJGDSQVcaF8d2L5NJyQvaTYPBFiYjmaBaEXl_-hTqq-c7tAh6_2DKJATX1kQaMPbEgrFChCjvNLE7tl7sOTRkMjBfDIR5JPLp_yKl2HQHupSjrqmfScwpxIjEHGlKJgQIG8FqrAeia0IY_KXCGQksTpyYcQJKGdkZDrI1i51t9wnpE17JrQYeAtytvddGoTOAkhufSQGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات تکمیلی دستگیری فردی که رسانه های معاند اورا کشته اعلام کرده بود
🔹
فرمانده انتظامی شیروان گفت: یکی از عوامل اصلی اغتشاشات دی‌ماه ۱۴۰۴ این شهرستان که با انتشار اخبار جعلی، سناریوی کشته‌سازی را دنبال می‌کرد، در استان البرز شناسایی و دستگیر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/652587" target="_blank">📅 00:59 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652586">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°(منتظر شهادت)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15ca8c681.mp4?token=NAXlVYpPN6f0fJfg354iZoOamlcU1hoNL0MKzg3Mx8S_JgRtIUqsrV4yeiQf6XOD7oEVTVimkkCD8l-3-t02PeICtTgb5u99OwFdg_jsvqEVgNe8ScrI0X_x3_AGkkihcUlVsjiks6eMEtqW4PHSuLoTvC_pOObH5TE9g1umm2Ctb88w7FYGSv2P-j3bXkmx0aVLeMXpCnpzJi4j4033McLRFYFlSVP3GnuwO-Nk0qskowLyXPU9VHnwBAaRJQhCpKZ6P9BOxcPkr68M5EsZRr221OeVyIYgw46VKrOu3mwrMW_V9Q0ok_jr7mj4mK86uREGbpf201rvzCmeLZvRiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15ca8c681.mp4?token=NAXlVYpPN6f0fJfg354iZoOamlcU1hoNL0MKzg3Mx8S_JgRtIUqsrV4yeiQf6XOD7oEVTVimkkCD8l-3-t02PeICtTgb5u99OwFdg_jsvqEVgNe8ScrI0X_x3_AGkkihcUlVsjiks6eMEtqW4PHSuLoTvC_pOObH5TE9g1umm2Ctb88w7FYGSv2P-j3bXkmx0aVLeMXpCnpzJi4j4033McLRFYFlSVP3GnuwO-Nk0qskowLyXPU9VHnwBAaRJQhCpKZ6P9BOxcPkr68M5EsZRr221OeVyIYgw46VKrOu3mwrMW_V9Q0ok_jr7mj4mK86uREGbpf201rvzCmeLZvRiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجات دنیایی را از امام جواد(ع) بخواهیم</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/652586" target="_blank">📅 00:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652585">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ادعای شبکه «کان» رژیم‌ صهیونیستی: انفجار در«بیت شمش» داخل یک شرکت موشکی رخ داد
🔹
شبکه «کان» رژيم صهیونیستی ادعا کرد: انفجاری که در منطقه «بیت شمش» رخ داد، در داخل شرکت «تومر» بوده است؛ شرکتی که در زمینه توسعه و ساخت موشک‌های پدافندی و تهاجمی فعالیت می‌کند.
🔹
رسانه های صهیونیستی پیش از این از وقوع انفجار مهیب در منطقه بیت شمش در غرب قدس اشغالی خبر داده بودند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/652585" target="_blank">📅 00:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652584">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAyz5D74pEr8wRWo3dJqVDcbg591VDObeUlmwFIvIIhoap1jRu6e8CtPVDG6F8-xoPJqjDwtdUbMDD2Psp4ayamAh0dMLvK10Md8NrHWB55-l4l8cFF2Xc8RTu3bgO85jXXV5OROiRU0sANqiOtwvP8rUeWd_cYQQiKe2htA--5KiD-GS3teWA8566ROdd3GXv0HKxk7ylIyuwSQNj1aSakClUOTq3Dcgp9_lgl-khqssPtlVDWkDSGidmob1-d8eEMFny0C--wQs8JzdWCDQePw6n4PKx2_wOUifIMP1JV2mpo3ZyO8ECIlJ_x_hyY-_Nxy4Izp8ZVM3gdDRGi7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اهمیت منطقه محل انفجار در فلسطین اشغالی
🔹
شهر بیت‌شمش واقع در غرب بیت‌المقدس که محل وقوع انفجاری مرموز است محل استقرار کلاهک‌های هسته‌ای رژیم صهیونیستی است.
🔹
پیش از این برخی از فعالان رسانه‌ای گفته‌اند که احتمال می‌رود کلاهک‌های هسته‌ای رژیم در پایگاه هوایی «سدوت میشا» که در شهر بیت‌شمش قرار دارد مخفی شده باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/652584" target="_blank">📅 00:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652583">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4922b5c6f.mp4?token=k8CgXKU4yxUENl2T7ajCQfPMZ3y4OpQs4_IuFmtambe3z_P0jTGsFV5Hhc1m6CPYTRPyr4AbpdH-x75i68nqMHFlC7TdPSMYk26SWKMx3IXUtOBtm6nPXtYggSfNXsjnaIat3JGgndvz4bT-Mirc4_to6Itdmy3OR1B0JrCaz8ffZ1oW_A0ej9ue2GidflEtaDhpwv8yX36CgSf-GzDmGpnF3h3QR7sYRLfpyT4oh2kcAGnvddMLGvITqfcBKWtOxooNkS3CYubU0NkBMrGeQLIi_hdrpmC5VxJ-iq251GWjoqWSKa_DUkxkabfzOBSzwfPa1ROwYn8qTRAUCeqoGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4922b5c6f.mp4?token=k8CgXKU4yxUENl2T7ajCQfPMZ3y4OpQs4_IuFmtambe3z_P0jTGsFV5Hhc1m6CPYTRPyr4AbpdH-x75i68nqMHFlC7TdPSMYk26SWKMx3IXUtOBtm6nPXtYggSfNXsjnaIat3JGgndvz4bT-Mirc4_to6Itdmy3OR1B0JrCaz8ffZ1oW_A0ej9ue2GidflEtaDhpwv8yX36CgSf-GzDmGpnF3h3QR7sYRLfpyT4oh2kcAGnvddMLGvITqfcBKWtOxooNkS3CYubU0NkBMrGeQLIi_hdrpmC5VxJ-iq251GWjoqWSKa_DUkxkabfzOBSzwfPa1ROwYn8qTRAUCeqoGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در نتیجه انفجار سهمگین در بیت‌شمش آتش همچنان شعله می‌کشد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/652583" target="_blank">📅 23:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652582">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
از داغ‌ترین خبرهای امروز غافل نمانید
🔹
خبرهای لحظه‌ای درباره احتمال آغاز حمله دوباره آمریکا | جزئیات طرح اشغال جزیره لاوان توسط ارتش امارات!
👇
khabarfoori.com/fa/tiny/news-3215239
🔹
اگر آمریکا به ایران حمله کند، ایران چه‌خواهد کرد؟ + ۷ واکنش احتمالی
👇
khabarfoori.com/fa/tiny/news-3215311
🔹
پشت‌پرده سفر وزیر پاکستانی به تهران فاش شد | پاکستان حامل چه پیامی است؟
👇
khabarfoori.com/fa/tiny/news-3215448
🔹
بزرگترین سورپرایز ایران برای آمریکا در جنگ احتمالی پیش‌رو چیست؟
👇
khabarfoori.com/fa/tiny/news-3215463
🔹
مقام اسرائیلی: جنگ با ایران ازسرگرفته می‌شود | ظرف حدود ۲۴ ساعت، وضعیت روشن خواهد شد
👇
khabarfoori.com/fa/tiny/news-3215371
🔻
ویدئوهای جذاب امروز را در آپارات بخوانید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/652582" target="_blank">📅 23:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652581">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz2JUegGKCWx4Semy_5PS3MnoCvWbUDDlG63XmPILt0o-mtyU_aOrcoCbmQFZ7d9mrYdP6tl_DdTIB5NYztiYd8qo-tkHpu2wY3lui1aRdT7h19aVvws1jnWv0Y1GqzSCNcNQKJ0HWQEsHudSY6FP2o63ks2wgSQqwWDerbdRCvqpYXPy92kW4ilyLIOLUWjv3DPInUYhx04IfiJZWhejiAZycmZgJcKru2q7metPmAOa42Eoud55DoRa0Bs2qfaS1oVfAGjaB7HuO7Qt4kd4KYmcXokTSmLWCil-nfVBsqTsZMeD-mG2KjuRkl7-SdEu-QqZGpV6_Zxn2-Bum7p-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حماس: در صورت تداوم تجاوزات اسرائیل، واکنش نشان می‌دهیم
🔹
عضو ارشد حماس تصریح کرد اگر رژیم صهیونیستی به تجاوزات خود ادامه دهند، با واکنش فلسطینی و واکنش بزرگتر در منطقه مواجه خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652581" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652580">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7948ef75ed.mp4?token=Dx1utB3828RpPZwuJlQnygc4NQVcBnbpuR7TNJV53VqpWwqV2lOoAfDwzjKVjBnb5Gjukwg4tUzg2RV7H0eRr497LxRnIMxOMmtWM_D1nauam7TnqqoEITP_IerTohwJcsSyp3iemaw1AAvcZqLiEiwdSy9vtYLU1R10-4EBv4qZfp7KEb_WZlCRcfKL1dLOLftWRaIo_sT4I9OcsfsJC5QT7daEeny31nN-NAZvE9yIJG5FIrPfTiW6vAFiziqSwYY1RzU3mrvVMmUEhlZlCnkBJ47fJ8yAcj0MWXUW3n9YALTsCXaI4YZCXoySOmG3zUiktWRvEV0vUoN-unfsNj2R0GmEKFkuq773j84C6a8wouU9Dhwabi1bAJjEBcAwCr6ZDk8RRGGj6KNU8Ej7iM8-KwxUjpk8k1bkZiOKSzVLQSbCSgj0tVRjbB6ywENIh4_4CLZzbGMXbAg8BI_OC2ZJkJ5IdgC8KcsYIDRnr7RPgQ3X0qQcWoJ-3TT4VfnDhEaNvHwkSyDRxWYNgD9iSOldUhEg-B6FbZUsJr3p4ybVoUQj1Fo5WErFoWkMMQloF-EpNyfFHQy4c5pfKRM2r7bRmCxHKt_65Wvk4UNlXAv_0x1bzO_85etkFIWoiE_GBgxzeK1mFwuVVL8dnOc8ATC6ZnhE9JPQYwN1e7L_Z6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7948ef75ed.mp4?token=Dx1utB3828RpPZwuJlQnygc4NQVcBnbpuR7TNJV53VqpWwqV2lOoAfDwzjKVjBnb5Gjukwg4tUzg2RV7H0eRr497LxRnIMxOMmtWM_D1nauam7TnqqoEITP_IerTohwJcsSyp3iemaw1AAvcZqLiEiwdSy9vtYLU1R10-4EBv4qZfp7KEb_WZlCRcfKL1dLOLftWRaIo_sT4I9OcsfsJC5QT7daEeny31nN-NAZvE9yIJG5FIrPfTiW6vAFiziqSwYY1RzU3mrvVMmUEhlZlCnkBJ47fJ8yAcj0MWXUW3n9YALTsCXaI4YZCXoySOmG3zUiktWRvEV0vUoN-unfsNj2R0GmEKFkuq773j84C6a8wouU9Dhwabi1bAJjEBcAwCr6ZDk8RRGGj6KNU8Ej7iM8-KwxUjpk8k1bkZiOKSzVLQSbCSgj0tVRjbB6ywENIh4_4CLZzbGMXbAg8BI_OC2ZJkJ5IdgC8KcsYIDRnr7RPgQ3X0qQcWoJ-3TT4VfnDhEaNvHwkSyDRxWYNgD9iSOldUhEg-B6FbZUsJr3p4ybVoUQj1Fo5WErFoWkMMQloF-EpNyfFHQy4c5pfKRM2r7bRmCxHKt_65Wvk4UNlXAv_0x1bzO_85etkFIWoiE_GBgxzeK1mFwuVVL8dnOc8ATC6ZnhE9JPQYwN1e7L_Z6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آنا گاسپاریان، مجری مشهور آمریکایی فاش کرد رسانه‌های اسرائیلی خودشان اعتراف کرده‌اند اعتراضات مسلحانه‌ای که برای توجیه جنگ علیه ایران استفاده شد، پروژه‌ای طراحی ‌شده توسط اسرائیل بوده است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/akhbarefori/652580" target="_blank">📅 23:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652579">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
«مکان–رویداد بمباران مدرسه شجره طیبه میناب»
🔹
این مکان-رویداد اسفند ۱۴۰۴ در فهرست آثار ملی ایران ثبت شد؛ اقدامی که با هدف ثبت و ماندگار کردن روایت حمله به این فضای آموزشی، شهادت ۱۶۸ دانش‌آموز بی‌گناه و بازتاب ابعاد این فاجعه در حافظه تاریخی و افکار عمومی جهان انجام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/akhbarefori/652579" target="_blank">📅 23:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652577">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5105ee0640.mp4?token=j5fpoT1uRsToF3_-JKdKGotiBz5AUDdn5N9lr3NkoH-QBkNACzKgS-fxHFkKybJwq6f8eSmH5_RXAgM7HTvF9Czy2SN8rTjZkyT-rjBCQwgHimNGFEC4A_8uGkPsBCeyh5c15XM67Yg1pxOpmYRo_KvHB5u_Fl9sp3uZB1Sw2EJxaF73r4xc1DAROFCPZaBUZttJ1iX6on73wzo64C7WF0k8ZOJXCtchPbrVCgYb5UQigXTTvPy-DjqMTJNsGTCj5-IzodV-4Nmgx6aWXsCuLw7FEBogXGXQ_fkaFNE5PRHjaS24oPZvCmz41fTK4S8DIq3Sf8513gj_I_er92Dsiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5105ee0640.mp4?token=j5fpoT1uRsToF3_-JKdKGotiBz5AUDdn5N9lr3NkoH-QBkNACzKgS-fxHFkKybJwq6f8eSmH5_RXAgM7HTvF9Czy2SN8rTjZkyT-rjBCQwgHimNGFEC4A_8uGkPsBCeyh5c15XM67Yg1pxOpmYRo_KvHB5u_Fl9sp3uZB1Sw2EJxaF73r4xc1DAROFCPZaBUZttJ1iX6on73wzo64C7WF0k8ZOJXCtchPbrVCgYb5UQigXTTvPy-DjqMTJNsGTCj5-IzodV-4Nmgx6aWXsCuLw7FEBogXGXQ_fkaFNE5PRHjaS24oPZvCmz41fTK4S8DIq3Sf8513gj_I_er92Dsiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار بزرگ در بیت‌شمش در قدس اشغالی
🔹
رسانه‌های عبری از وقوع انفجاری بسیار بزرگ در بیت‌شمش واقع در غرب قدس اشغالی خبر می‌دهند.
🔹
این رسانه‌ها با بیان اینکه ارتش مانع از ورود خودروهای امدادی به محل حادثه می‌شود، تصریح کردند این انفجار احتمالاً در تأسیساتی حساس رخ داده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/akhbarefori/652577" target="_blank">📅 23:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652576">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg8hAMG-smO73WGrFreHSoUxlDDGClHHflGQGVrRrC1hgLMmURABFub8oxiRPzp1fJfi0cJN7ZFS2pJcz6z0OSdXf0Ypo-UHfe-uwu7d_sR_wF0YUUmRniJYjPKot5WYIXogatkh5tteOyQ1soxwGiHMoCsFyJiK0XGyt0yb9orJ78rXhhQ8kQswJPREHZ1HVhAG7IioSaaw_GzPes-ISeDB87Q0OHksxN4MdTbtNSnLkLmvvFazvwAdu8dr74CDaLB1jxt7NkBwLB8jgwD1zda5dtxQUFYe0zER5TBPgZ31gOQYaKRU28HzPgDTPPiO7NaHuf9mOt5Pknwo6I771A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکرار تهدید کاخ سفید با انتشار تصویری از ترامپ در اتاق جنگ
🔹
کاخ سفید پیامی تهدیدآمیز از رئیس جمهوری آمریکا با عنوان «شوخی نداریم» همراه با تصویری از حضور او در اتاق جنگ منتشر کرد.
🔹
در پیام کاخ سفید آمده است: «اگر به آمریکایی‌ها آسیب بزنید، یا برای آسیب‌زدن به آمریکایی‌ها توطئه و طرح‌ریزی کنید، ما شما را خواهیم یافت.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/652576" target="_blank">📅 23:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652575">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyqYK2sVL4c4L5tpNuNLwTZQ3gfwL-eiPeGJU7z48xL00WNX5q4_BEi8wcmaKeh-LouMfULMvavxHBRrGcayCRzTzAq_Agd1CWHtD9MqLoD4f1iH5SLFmyTxDnBcUikqZGEAkBmjDZzCafxFiF30vX8abi2-mv1XNg9d-LOyohmHtiwlWWbMtuMUWOBg7z4Q4yp-e7XnFf4HBxFR-9MJBObYLr63p8V23C9W4c-ZXF2_U2dYmKacWRP3SeQg4TsLcfPWINFZOnTVkUCHkyT1de0tJ5PqNHgYFc1DDvidLuJae9cz5zOdO7fAOnuAA--sh6PmKeMj69JquxviR_R2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بزرگترین سورپرایز ایران برای آمریکا در جنگ احتمالی پیش‌رو
🔹
ایران در جنگ ۴۰ روزه با بستن تنگه هرمز، بزرگترین ضربه را به ارتش آمریکا زد. این اتفاق ممکن است در جنگ احتمالی پیش رو نیز تکرار شود، اما این بار در تنگه باب المندب و توسط متحد منطقه ای ایران یعنی یمن.
گزارش خبرفوری را بخوانید و در بحث داغ مخاطبان شرکت کنید
👇
khabarfoori.com/fa/tiny/news-3215463</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652575" target="_blank">📅 23:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652573">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d9f9f757.mp4?token=KMeCkY7hbxYGl5Ks8Zp7B6DzKLoQ7taw_Tsfs1kBlmcXi1mLuVtlFBTjio3QEV0A-qq6wU5h5z0Wr5h0y49-1a13nx0_ZgSfRkHL5uyY98sl6P2VjM-JKAd6UJvwsx1iQ_1XOIuKnbWXs4_QlfDVGYxcj1fX3wGAaHCZujBdvgA1EytNP7xcA3xpkxWKvYjypjadPcrEkc9RuFhviiPOsxGGj_9FNyn81V2dxag8NLjoxTCjhH9XtRBzv6_yWCqGh2Ejzy13QUPmbunMuN6CI_L2TZn6NGMVv0hARis_dWy2EGsdBexRqGnbP-y5cAnlXf1fuvaypgNKXtKBz4gpYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d9f9f757.mp4?token=KMeCkY7hbxYGl5Ks8Zp7B6DzKLoQ7taw_Tsfs1kBlmcXi1mLuVtlFBTjio3QEV0A-qq6wU5h5z0Wr5h0y49-1a13nx0_ZgSfRkHL5uyY98sl6P2VjM-JKAd6UJvwsx1iQ_1XOIuKnbWXs4_QlfDVGYxcj1fX3wGAaHCZujBdvgA1EytNP7xcA3xpkxWKvYjypjadPcrEkc9RuFhviiPOsxGGj_9FNyn81V2dxag8NLjoxTCjhH9XtRBzv6_yWCqGh2Ejzy13QUPmbunMuN6CI_L2TZn6NGMVv0hARis_dWy2EGsdBexRqGnbP-y5cAnlXf1fuvaypgNKXtKBz4gpYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دفاع مدیرعامل جی‌پی مورگان از حمله نظامی به ایران: باید سال‌ها پیش سراغ سرِ مار می‌رفتیم!
🔹
نیروهای نظامی می‌توانند برای باز کردن تنگه هرمز؛ ۴۰ سال برنامه داشته باشند. آنها طرح‌هایی دارند. نمی‌دانم آن طرح‌ها چیست. امیدوارم کار کند.
🔹
جیمی دایمون، مدیرعامل جی‌پی مورگان؛
🔹
جی‌پی مورگان (JPMorgan Chase & Co.) یکی از بزرگترین و قدیمی‌ترین بانک‌های سرمایه‌گذاری و خدمات مالی در جهان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652573" target="_blank">📅 23:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652572">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
بلومبرگ: آمریکا معافیت فروش نفت روسیه را متوقف کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/652572" target="_blank">📅 23:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652571">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
آمریکا معافیت تحریم نفت روسیه را تمدید نکرد
🔹
این معافیت قبلاً به مدت یک ماه تمدید شده بود تا کمبود عرضه نفت و قیمت‌های بالا ناشی از بسته شدن تنگه هرمز توسط ایران کاهش یابد.
🔹
اسکات بسنت، وزیر خزانه‌داری آمریکا پیشتر گفته بود که مجوز خرید نفت روسیه ذخیره‌شده روی تانکرها را تمدید نخواهد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/akhbarefori/652571" target="_blank">📅 22:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652570">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkVn1E2UaQltUpesPCX6k507kDq7RNHUpmsVvCibwHkdriO3aODBA2i1jULMdZdT6k9lD7lRgNr2kbwxBh7QYgMH_gwQDM9ILPIWG448einUGWLIro6VlJIhjmlVJHd2g31skPGz7NT_ct9YatPCCPcNdMOJDf5Kcq2ouDiuxv1l82-HwbtsTh58nSRr_rL9g15_vnA-DpoIBlX3tm5fLyvi8aqB-nHxUgNA6NJB7rypB8x2C8-36rp64ZI3HfzpbNt7qyWjmt6teRr768ywKgrU1USc9VdgAYH0JPTvS5RceUdhCgKDoOj2l5Mh1S-g7xKkezB2X7BvagecgD4mtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: مقاومت ملت ایران، تحول جهان را سرعت بخشید؛ آینده از آن جنوب جهانی است
🔹
رئیس مجلس: جهان در آستانهٔ نظمی نوین قرار دارد.
🔹
چنان‌که رئیس‌جمهور شی گفت: «تحولی که در یک قرن دیده نشده، در سراسر جهان با شتاب در حال پیشروی است»، و من تأکید می‌کنم که مقاومت ۷۰ روزهٔ ملت ایران این تحول را شتاب بخشیده است.
🔹
آینده از آنِ جنوب جهانی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/akhbarefori/652570" target="_blank">📅 22:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652569">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8fSGClsCVfsI-jbojIQao-sAVbfzzfFtr0hr_4ttkViaZ7OmIt_KQVuu1GbG_MmY5tTS_1Z9Mo4alXsDQfFLizP07aQIaytXI_reJPxVzW-cwP6ntZxFtfaJ8bdueTwWDX2vw_37p-X9aDvQ2f4rUyI0naacUCKkjG9D2EDMgGwolJIyZgWEniTMrsIuNzRtlvXTkvH-M2O32L09meB0GmFdWcHenpqf2urDAiuY_Ep-kfL3vXDyt39AslVTGXnry1tYCc9JyLHzvMmsgjPGOfBGTH6t8F_vi9nuwNmxjgfrwZDyhu0wuNH4tEhCRHc9xoQtVteH7UmrdRoX2QZ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سوخت سخت
🔹
در پی جنگ تحمیلی سوم و محدودیت‌های تأمین سوخت، صف‌های طولانی در پمپ‌بنزین‌ها شکل گرفته است. این شرایط بحرانی نیازمند همراهی و مصرف مسئولانه مردم است؛ استفاده از حمل‌ونقل عمومی و پرهیز از سفرهای غیرضروری می‌تواند کشور را عبور دهد. اما نکته کلیدی آن است که مسئولان تصمیم‌گیر پیش از این باید تدابیر لازم را می‌اندیشیدند. موضوع خودروهای بی‌کیفیت که اکنون قیمت‌های نجومی یافته و نیز انبوه خودروهای فرسوده، باید یک‌بار برای همیشه حل شود. تا ریشه‌های این بحران ساختاری مدیریت نشود، هرگونه کاهش مقطعی مصرف صرفاً مسکنی موقتی خواهد بود. همکاری مردم در کنار تصمیم‌های درست و اصولی مسئولان، تنها راه برون‌رفت پایدار است.
🔹
هفتصدوپنجاه‌ویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/652569" target="_blank">📅 22:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652568">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991a0ca5bf.mp4?token=vTCHSitNG85uL1NkCJxq2wKYF8yyg5UQ_golrYHe5QO35djabuuso8C8dMkU7GI-ZcZqg0YHn9GmShWGq8_0U1Agv-OGVAP9qTyWi2DrJHGS4VmoGQaaXYBwqWRSeLBmc5Wak2rSLyWR5ZQtRt4K-FHCGrMn0v2dsn6vyu4dRfA1nx5RMRrKbFT25XGhB1KP3HQrdqZ50tcvfeGOzeUNVc2xR8LnA4OTD38GsUtgPCbMCY6axA8XEMwuH8C1kmaZE_71dkqzH0zmjyjjgO0zw_tbm9M2Ni0WX3Uk8RyyixFv8dQ8-JHEqVvYJEf6ALEVo-2zJsaA5ikoWvfTB5LbRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991a0ca5bf.mp4?token=vTCHSitNG85uL1NkCJxq2wKYF8yyg5UQ_golrYHe5QO35djabuuso8C8dMkU7GI-ZcZqg0YHn9GmShWGq8_0U1Agv-OGVAP9qTyWi2DrJHGS4VmoGQaaXYBwqWRSeLBmc5Wak2rSLyWR5ZQtRt4K-FHCGrMn0v2dsn6vyu4dRfA1nx5RMRrKbFT25XGhB1KP3HQrdqZ50tcvfeGOzeUNVc2xR8LnA4OTD38GsUtgPCbMCY6axA8XEMwuH8C1kmaZE_71dkqzH0zmjyjjgO0zw_tbm9M2Ni0WX3Uk8RyyixFv8dQ8-JHEqVvYJEf6ALEVo-2zJsaA5ikoWvfTB5LbRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای عجیب ترامپ: ایران در گذشته بارها تنگه هرمز را بسته است!
🔹
ترامپ در ادعای جدیدی گفت: ایران سال‌هاست که با استفاده از تنگه هرمز، جهان را تحت فشار گذاشته است.
🔹
ایران از انسداد تنگه هرمز بارها و بارها بهره برداری کرده! (بارها تنگه را بسته است)
🔹
آنها در گذشته تنگه را بسته‌اند. از آن به عنوان یک سلاح استفاده کردند!
🔹
اما الان نمی‌توانند از آن به عنوان سلاح علیه من استفاده ‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/652568" target="_blank">📅 22:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652567">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519197d026.mp4?token=BoKx-hnhZDfEnYBbwqLCiuh69doEKW-K55vygybK8_EXFE05WcYhFhrXnjRChHmAKeqrLz60vGBYeHsvz-N70api6elBycVgY9K3ajolYwRgtDKWGttLZ0clCh0tB6b5pC6bHuTu5vu3XYCTa3lH2Z88sTbTCiz2fN7IpTwAKnBxF6DExV8R4ZFcOmM_PuwW6w__6bAg3S-EJ_Ia-J79g6USaKNU7M0Vj-xSlFxuHPPac4L_8vqwPdo5wg6xJV_udys26ksmfUuw8Fam6Deq6dmMnlgvM0LVNESYkuXFbssWumUVolO4_4tChyAdeEGmxPSjC6dMDLwqKYDun3-G8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519197d026.mp4?token=BoKx-hnhZDfEnYBbwqLCiuh69doEKW-K55vygybK8_EXFE05WcYhFhrXnjRChHmAKeqrLz60vGBYeHsvz-N70api6elBycVgY9K3ajolYwRgtDKWGttLZ0clCh0tB6b5pC6bHuTu5vu3XYCTa3lH2Z88sTbTCiz2fN7IpTwAKnBxF6DExV8R4ZFcOmM_PuwW6w__6bAg3S-EJ_Ia-J79g6USaKNU7M0Vj-xSlFxuHPPac4L_8vqwPdo5wg6xJV_udys26ksmfUuw8Fam6Deq6dmMnlgvM0LVNESYkuXFbssWumUVolO4_4tChyAdeEGmxPSjC6dMDLwqKYDun3-G8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله‌ی پلیس برلین به تظاهرات ضد جنگ ایران و فلسطین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/akhbarefori/652567" target="_blank">📅 22:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652566">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh76L96moPWwsqWm9sAL3UiCbIskiP3nsTC2BnxUvIHl_D4XPk4ZIEdFp4TabmjC9L1HFRKT1ukF9w9MvP36lYba5TV2GGg_RylExxNI1cv8CieeM_B4FON6VUNJWolurVoxrGxhZFQKZIVf9i7Lzmi4ap_HGBYGtswMg3ZyW9HzQ4LmyqKsF2FFh6rqRBNQTZKFOrQKkZHShl45TMwZ42HPReCk_v7kUpXFGY3H7wdDzZMUJpIIzOXpdRJ__TVcrm7rUwO8nwCOsvcJExbLDJtG2PVsH-QX3eMB7bYrc9V6pkXxwjv4Y-pvOZdT4LZPmCFP1DL7cNlP9lRiEeqn8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کوثری: هر تعرضی با پاسخ کوبنده مواجه خواهد شد
🔹
عضو کمیسیون امنیت ملی مجلس: اگر آمریکا یا رژیم صهیونیستی کوچکترین تعرضی انجام دهند، مردم ما، چه زن و چه مرد، در صحنه حاضر هستند.
🔹
دشمن هر توانی داشت در ۴۰ روز گذشته انجام داد، آنها نمی‌توانند به راحتی بمب‌ها و موشک‌های از دست رفته خود را جایگزین کنند، اما ما به راحتی میتوانیم جبران کنیم.
🔹
آنها در هر نقطه‌ای که حضور پیدا کنند، رزمندگان و مردم چنان ضربه‌ای میزنند که جز ذلت و خواری نصیبشان نشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/akhbarefori/652566" target="_blank">📅 22:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652565">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaM-YKpp2iIPM4_8T6iwMPFDsNNXuhixT0ot_GBIpXZxVUuWR9iAGIJf1dBftygWVCmlI4oQUwW2B2pEKt1YCVoR_D_w3cz4iEFZHA9McSxRf_b9L61B_Ob4BUYWIB8UYUKXZBFYTa2tISVuErb2U7khG6KEJqF98jD0gB621lUbMKMGaoL4dOJq6OrF-cJ-QK-DGQfmZBsqt2kAnuFZAoIdPXHSlX_gt--Hd4Wl6PehjhQdnelzgbM0a8gj7b_VkWIBWPhoph4tackruJHYwEETyHjNDsex3woV3cjJezZOQf_D5h27Ecq50iV5QPhuqVe84jkgub5XDDBRmvQijw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حزب‌الله شهادت فرمانده قسام را تسلیت گفت
🔹
حزب‌الله لبنان در بیانیه‌ای به شدت جنایت شنیع صهیونیست‌ها در غزه و به شهادت رساندن عزالدین الحداد، فرمانده گردان‌های قسام به همراه همسر، دختر و چندین غیرنظامی فلسطینی طی حمله هوایی جنایتکارانه را محکوم کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/akhbarefori/652565" target="_blank">📅 22:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652564">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agL7IgXFhJHsx_GSHkql968-Jfmn-q8083uwwRZL8zXWxK5EecmkyDZVhQESe4v-0tUnwkUtKVYtgEhtgbE624H7VAl9-WQdd_kG-rx8yX-lgpyofgzhPpwiK2hja1XWsaF_VR67fC883BpcIcEU-LmCcgs1bImHowiiivQntNvo2MKyzt5O1GQSXCsdMm3xEKUM6c8fj2bOO3pCJH5gmM19r9ufsAMy9uvSAvZ7aXbkCRUM6QrxtDfYXllJzil9ajhpL0Prtft4k-jkZIag32HRWk53N4JGDZhDAaHN_x_JxSGE-7XdZ0vztuoOfIGL21YeFhE2kSDy50WlctmOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هلاکت یک نظامی صهیونیست در جنوب لبنان
🔹
ارتش رژیم صهیونیستی از هلاکت «یسرائیل ریکانتی»، از عناصر تیپ گولانی در نتیجه اصابت مستقیم پهپاد انفجاری حزب‌الله در جنوب لبنان خبر داد.
🔹
ارتش اسرائیل با وجود سانسور بسیار شدید تلفات و خسارات این رژیم در جنگ، اذعان کرد که شمار نظامیان کُشته شده در جنوب لبنان از زمان جنگ جاری به ۲۰ نفر افزایش یافته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/akhbarefori/652564" target="_blank">📅 22:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652563">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318b3eb231.mp4?token=gra054Kuvb1gDn95IFzfJPDhSkFpiDvuhUhGUx63qy-9IjZvAxGlbiwHu47VQwZSFJZnEEPzrSBVcS9oiIbhl1EMCb9glKAZoAg_85y9zQpDMOJeEzlMjN0-y-NdNjW8bTslfJqs3Z-OEv54hT9OW_69mKRkfvX_yQIFrFYbPaLsxkzSYS_cmbOm2EQEAm6QdKKzCycMF_PntUjg4IaPYJ2xKAosrdi5RnIOhSrnV1lA6jVv1emkfgJEafktZZy3q9GozjNjsTOP0C31HDFo1uEbMdD5bIwCsh8dYqzYzNmgX-sIFpgnH7XRVHUchXpkC3-YxalaHqXpu0CCzZH2hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318b3eb231.mp4?token=gra054Kuvb1gDn95IFzfJPDhSkFpiDvuhUhGUx63qy-9IjZvAxGlbiwHu47VQwZSFJZnEEPzrSBVcS9oiIbhl1EMCb9glKAZoAg_85y9zQpDMOJeEzlMjN0-y-NdNjW8bTslfJqs3Z-OEv54hT9OW_69mKRkfvX_yQIFrFYbPaLsxkzSYS_cmbOm2EQEAm6QdKKzCycMF_PntUjg4IaPYJ2xKAosrdi5RnIOhSrnV1lA6jVv1emkfgJEafktZZy3q9GozjNjsTOP0C31HDFo1uEbMdD5bIwCsh8dYqzYzNmgX-sIFpgnH7XRVHUchXpkC3-YxalaHqXpu0CCzZH2hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئيس كانون كارگران بازنشسته تامين اجتماعی تهران: پرداخت حقوق و احکام جدید بازنشستگان از خرداد ماه اعمال خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/652563" target="_blank">📅 22:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652562">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-text">✨
بخش دوم | ادامه‌ی مسیر همدلی در روستاهای مرزی زابل
💫
به رسم  پربرکت دهه کرامت، با همراهی خیرین عزیز و هیأت‌قرار، اقلام معیشتی میان خانواده‌های شریف روستاهای مرزی شهرستان زابل توزیع شد؛ تا سهمی کوچک در لبخندهای بزرگشان داشته باشیم.
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/akhbarefori/652562" target="_blank">📅 22:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652561">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8h1TueJTQ32UDKFImSQv4AiMiE3hg1XlXA7NYKSC2LGCdPZMcvNFwHtIB0FdJ2QmhifgujgAwkQXBwNXvmFqrL-KYu6PZIj_22UNoOU3ht9iUuLCrwveHIqcAlKiEAve58cHfp3GK5gmv_LOAmLewu1vUkaeuU4__dmct3A3s95AfQv1mmsPqDinJGDaeBURu0KIYETgoBjkU1b5KcMh7_UpHsyFgGTyQNIkiSVQqmcwz8ljWAXopy8mUUOiHPyqGnXKZ3rkLJ_XkTVRJE47cOtjoPoM0Rax53TvT7osKpUh9dr2CqONm92nUO9o7yolVk8jVrfol0f5UVApw6YGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاکستان جای خالی امارات را برای ایران پر کرد
🔹
پاکستان با کاهش تعرفه‌های بندر گوادر خود و پذیرش اولین کشتی تغییر مسیرداده ایران، تلاش دارد انحصار امارات بر ترانزیت ایران را برای همیشه بشکند.
🔹
این تصمیم درحالی عملی می‌شود که مسیرهای مرسوم واردات و صادرات ایران از طریق امارات با اختلال مواجه شده است.
🔹
پاکستان علاوه‌بر تخفیف ۳۱ تا ۴۰ درصدی در تعرفه‌های بندری خود، یک ماه انبارداری رایگان هم برای کشتی‌ها درنظر گرفته.
🔹
کارشناسان معتقدند که اگر این روند ادامه یابد، وابستگی تاریخی ایران به بندر جبل‌علی امارات که تاکنون سهم اصلی ترانزیت ایران را در دست داشته، برای همیشه پایان می‌یابد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/652561" target="_blank">📅 21:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652560">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3-aaoy0nfH6ebKsihgp3-3DqUiHU4VvJ34R4s-Cq127zUKmaHj6363ayo9YRyQlTqfMoC7FB7ISW1p18B6BV9XnskT9u00I5vlBtgYEAQZVQX9Qil7cMXlFU5rkXShL68kyZM5iNRMHRN3LgDHgcdFnMHAnaMzjsK4b0gPkkhVrO5e-HOkZGrhOQgcR8F_G8KjnqTHhE5QvYQo7x7UmjQj-_jZVLwjc3POornwtLFXvuRpTGN1jeOrL5G5DJ4zg81kWyw1QIg72kj7dIfprmyptfN3oy8EoK0vi-7XgTcqfXpSG93eqXNndc7bz9dXSuaWGKbRHnJVkbu0IqC7wtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان بحران، سرعت خبر برای افراد مهمتر است یا دقت آن؟
🔹
در این نظرسنجی بیش از ۳۶ هزار نفر شرکت کردند که سهم روبیکا ۶۲٪، بله ۳۶.۶٪ و تلگرام ۱.۴٪ بوده است.
🔹
بیش از ۴۳٪ شرکت‌کنندگان در زمان انتشار اخبار مهم نظامی، ترجیح می‌دهند کمی صبر کنند تا گزارش‌های جامع و تأیید شده را بخوانند.
🔹
حدود ۲۴٪ هم اخبار فوری و کوتاه را حتی بدون تأیید نهایی ترجیح می‌دهند.
@amarfact</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/akhbarefori/652560" target="_blank">📅 21:41 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652559">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bec27ace.mp4?token=taQ2bf4vTVHfD6MtupNoK9X8Ao4AoXjEUmAI_DCCbD9Rf0HzLPFARILghxcVdbBUcjdtPm8CTbGwvTRvk8uAS5lDitk58rA0ieEAVVgM7cMFoipa-YNTw3ZksCSyra_lwP8_E3VtYyb7GE10K8D-NUuBlTAZfGm2dgmGWOvtGe7K_Xj3hPvKlLZXwLgjGFIHZlZ4UbRx6GEFyOetZrT4PLTrlMsY0gH0-b5lypndKaPHvracNQQp2gtJ-RUkp_ae4veoUYPnk_PO7BpopIeo2k-_jl63g82hQVZ10c5V2re9isJWn_M3xTvcxaO_Yb77igcYlGFMAp2KqpXameeK9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bec27ace.mp4?token=taQ2bf4vTVHfD6MtupNoK9X8Ao4AoXjEUmAI_DCCbD9Rf0HzLPFARILghxcVdbBUcjdtPm8CTbGwvTRvk8uAS5lDitk58rA0ieEAVVgM7cMFoipa-YNTw3ZksCSyra_lwP8_E3VtYyb7GE10K8D-NUuBlTAZfGm2dgmGWOvtGe7K_Xj3hPvKlLZXwLgjGFIHZlZ4UbRx6GEFyOetZrT4PLTrlMsY0gH0-b5lypndKaPHvracNQQp2gtJ-RUkp_ae4veoUYPnk_PO7BpopIeo2k-_jl63g82hQVZ10c5V2re9isJWn_M3xTvcxaO_Yb77igcYlGFMAp2KqpXameeK9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیگیری وضعیت دارو، کمبودها و قیمت‌ها
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/652559" target="_blank">📅 21:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652558">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YdWlj-cJQHgFko3F4Dtd5X4-vfxFRIERIk8I9pkBzslz-D9DFQu9c6_PlvexkZZGp8U7zrMyn4AOJEa4ISwxZQb2y85uvraVNvuLZsrCOYI6tifxC0fwpfgCs8u06oJJuCr2IngYm9XHEhRRuuJ5mwxR_w5gzHsdn7FW0r6ABy7mGAfS5JcPRFP1a-uqLwmOeSEkqcBo6OqkZET9NXpugv0WLP9TfSaaVr6eEG7dm7N6WuKWmOXltrJzMed2F_nG1PccEtS4GpKM9VRzDUHQWD6amdU38AIzuFmAC61Ipib_-548H7t-3j2mjzsxQ4f3JZx_OK0Ic0-CC6OMjj0NgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گالانت، وزیر جنگ سابق اسرائیل: به وضوح می‌گویم که هیچ‌کدام از اهداف راهبردی جنگ درباره ایران محقق نشده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/652558" target="_blank">📅 20:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652557">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044a1cdda5.mp4?token=WoacJ1RnzAqCYC1AX_GVYH0qubDIOB95m8vUVMxpeqxhfmhSNGiBdPzwBDqv2JxTyfKapVY4nhegPlyIlkmWVEmtZXRVNMb7ZcCV0FwiL8iOU0rsgSl0OV-2yaT-lsNkykmFdqvrwvdZykQRqcSX90SuwTmS-LEeaAisuJsEUPn8SQskKSQcXngDr6F2v-49wBbhCPQM63-TxQ39xa1Qx7HPPjVSbv8yrdJKwllyA2oemKm1gcUH8bihhXejZ0LG1Hvt0uX8ZvpyeCBaPhi5YHeBZFLCIHAApsu24_G4vohp7NcF2m6md2rVw9tcBmZ8xIRax_KIkhdg5pxxfoW9GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044a1cdda5.mp4?token=WoacJ1RnzAqCYC1AX_GVYH0qubDIOB95m8vUVMxpeqxhfmhSNGiBdPzwBDqv2JxTyfKapVY4nhegPlyIlkmWVEmtZXRVNMb7ZcCV0FwiL8iOU0rsgSl0OV-2yaT-lsNkykmFdqvrwvdZykQRqcSX90SuwTmS-LEeaAisuJsEUPn8SQskKSQcXngDr6F2v-49wBbhCPQM63-TxQ39xa1Qx7HPPjVSbv8yrdJKwllyA2oemKm1gcUH8bihhXejZ0LG1Hvt0uX8ZvpyeCBaPhi5YHeBZFLCIHAApsu24_G4vohp7NcF2m6md2rVw9tcBmZ8xIRax_KIkhdg5pxxfoW9GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معاون اول رئیس‌جمهور: دیگر اجازهٔ عبور تجهیزات نظامی دشمن از تنگهٔ هرمز را نخواهیم داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/652557" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652556">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640a18d638.mp4?token=mZkDg7Dt93-K8cSIcdFu3BmcVOk7dWDFy75irjM2ufqYXJ8mGMAKZ8OINbaGcQAOhvRWDjafr8l5OVcC-9e2AykoDqWwQgRP7AmJ1dDVDkkEGGhF-UswsdgVAipK0_3c_Gjyn-K5kJLaWfBiyQr03SHN5TjtfrT3cXBrjZJmDPMxqGwvnMGvfXbB7CyjwYpDJkjI2GGO5_gLDEpW6HeAlIFor9GQ6wAFogJfomwTLRAQ2Czk2Y4uZWujo2HhVr6IZ1_QzK4A7-EENFXhVilQ-aPb5Ucmh3FvStRMHbNiExUCzhlfh9MJgdesgcmkbLL3bomVf53poeSizYIBN20USA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640a18d638.mp4?token=mZkDg7Dt93-K8cSIcdFu3BmcVOk7dWDFy75irjM2ufqYXJ8mGMAKZ8OINbaGcQAOhvRWDjafr8l5OVcC-9e2AykoDqWwQgRP7AmJ1dDVDkkEGGhF-UswsdgVAipK0_3c_Gjyn-K5kJLaWfBiyQr03SHN5TjtfrT3cXBrjZJmDPMxqGwvnMGvfXbB7CyjwYpDJkjI2GGO5_gLDEpW6HeAlIFor9GQ6wAFogJfomwTLRAQ2Czk2Y4uZWujo2HhVr6IZ1_QzK4A7-EENFXhVilQ-aPb5Ucmh3FvStRMHbNiExUCzhlfh9MJgdesgcmkbLL3bomVf53poeSizYIBN20USA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی نفسگیر از انتقال امن بمب عمل نکرده دشمن متجاوز آمریکایی توسط یگان چک و خنثی فراجا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/652556" target="_blank">📅 20:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652555">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a182fe40.mp4?token=j-8_6MfIkKIUR33Zi2hUihvls23JTJCDO5B9C2Xcg4Nkr1xpqTEDaIxDmITwSbGBLkD4_1MKsfaAV-IXNcnVDy0GM7oT_xivryMah119OWSKwWO3Y1pF78JMl0pv7NvkyxszPpcJnDr9gumHjk2K-yHELIRJh-h0ThyIiNhZidApDtzgEWOWq_5l_kqLhtwPpHjDYDyB1HhXIaKJggdiwjEt7Ou1TL96kWOrorftcou1Fbxi0woUURmCbHkyb3d3q5jvym4dt2vzJniQoL16yIGT3MrcBZrmMADBj5IGQ_uRMyL-kRgFBjbxD6Fs0OqSxaNY_VphswMbGyLxuw5WPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a182fe40.mp4?token=j-8_6MfIkKIUR33Zi2hUihvls23JTJCDO5B9C2Xcg4Nkr1xpqTEDaIxDmITwSbGBLkD4_1MKsfaAV-IXNcnVDy0GM7oT_xivryMah119OWSKwWO3Y1pF78JMl0pv7NvkyxszPpcJnDr9gumHjk2K-yHELIRJh-h0ThyIiNhZidApDtzgEWOWq_5l_kqLhtwPpHjDYDyB1HhXIaKJggdiwjEt7Ou1TL96kWOrorftcou1Fbxi0woUURmCbHkyb3d3q5jvym4dt2vzJniQoL16yIGT3MrcBZrmMADBj5IGQ_uRMyL-kRgFBjbxD6Fs0OqSxaNY_VphswMbGyLxuw5WPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عذرخواهی تفنگدار سابق امریکایی از مردم ایران: از طرف کشوری که بدنیا آمدم بخاطر حمله به شما وکشتن کودکان میناب عذر میخواهم
🔹
کن اوکیف در میان تجمع خیابانی در مشهد: شما با شیاطین در جنگ هستید.
🔹
من در وسط جنگ درخواست دادم بیام ایران تا مثل شما باشم و دفاع کنم مقابل شیاطین.
🔹
کشورتان(ایران) و شما مردم فقط جرات داشتید جلوی این قدرت ها بایستید هیچ کشوری این جرات را نداشته پاسخ جنگی از طرف اسرائیل وآمریکا را بدهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/652555" target="_blank">📅 20:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652554">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsxPWdkaxhcl2f61yZQ3rmm3wSWeamKuf6M726MicpxwuQo-1hh3tA3lo_xL5Adc2jNJZ3StiOzsV7W6TmmvuqGfoWM8EHOC_tlBY-yzR24TzuXglKDm3dpsb1LoolSQ16HKAaRrt21q7_irXI0SWZyRcDInfJjskIcHTh_BCFM2aC45fwaqJkTU8lSb4kk0NhrrX8ZDcqJqnog_1PmQTU1O9gjRNJFQ0A5CS52V_YZLhGh8abWiYOuBgB-U3fwCFMIBfFZvWcVo7ZBcF7C-rkMPDtVt23G6z9vnFRczw3W-7MZ-xtL_59Whz9rJCJZsnKam7YQ_5uVLmLqwXWl5Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ژاپن تایمز: با تداوم جنگ ایران، کاخ سفید برای کاهش قیمت بنزین به تقلا افتاده است
🔹
مقامات دولت آمریکا در حال بررسی داده‌های بازار هستند تا ارزیابی کنند آیا میانگین قیمت ملی می‌تواند به ۵ دلار در هر گالن برسد یا خیر، در حالی که داده‌ها نشان می‌دهند که هفت ایالت از این مرز عبور کرده‌اند.
🔹
دغدغه‌های دولت با جهش صادرات نفت و سوخت آمریکا به سطوح بی‌سابقه عمیق‌تر شده است، امری که توسط خریداران آسیایی و اروپایی برای تأمین منابع مورد نیاز هدایت می‌شود ولی ذخایر داخلی آمریکا را کاهش داده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/akhbarefori/652554" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652553">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH0GcfA8Eyju1B84bGEgwdcAuJ5Bts3FqbYHrNdkuCe7z3WRSGfYDeKoiSVlGvy0mtfvNxKsfRoPS_dH6lHmrI43vZOpL15SS6cTbpXXIgfXPXsyf6uWoxHcXG-CYjcwoUYRgRXhNHQB11WYSFb6TPxLsN50Cupo0mJ0yH4pbTt4BgKh57i18Ml6AI0emwxZ47l-ap_1F6sp1PXHObPVPj1SIUC9vmZ29RGAqvg0SXTANh6JeE-OfdPzo0ryrEkQdlf-ir_dTgWosI2v-tB3S1E63P80rNL_K2LgrPxbsZCRgcns65OmZmiArE27hgGHMeWQRBL-SjrqT8482p6RfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دولت ترامپ در حال تشویق امارات برای تصرف یکی از جزایر ایران
🔹
تلگراف در گزارش خود نوشت که مقامات دولت ترامپ، امارات متحده عربی را تشویق می‌کنند که نقش مستقیم‌تری در جنگ با ایران، از جمله با تصرف یکی از جزایر ایرانی در خلیج فارس ایفا کند.
🔹
امارات متحده عربی یکی از ستون‌های اصلی حملات آمریکا و رژیم صهیونیستی به ایران در جریان جنگ رمضان بوده است. این کشورک حاشیه خلیج فارس ضمن همکاری کامل با نیروهای مسلح آمریکا و رژیم صهیونیستی، دو بار نیز به طور مستقیم حملاتی را به ایران انجام داده است.
🔹
طبق گزارش تلگراف، یک مقام ارشد سابق امنیتی دولت ترامپ گفته است که برخی از افراد نزدیک به ترامپ پیشنهاد داده‌اند امارات باید جزیره لاوان را — که در اوایل آوریل هدف حملات پنهان امارات قرار گرفته بود — تصرف کند و به جای آنکه نیروهای آمریکایی این جزیره را در اختیار بگیرند، نیروهای اماراتی آن را به تصرف خود در آورند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/652553" target="_blank">📅 19:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652552">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
شبکهٔ ۱۴ اسرائیل از شنیده‌شدن ۲ انفجار در الجلیل غربی خبر داد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/akhbarefori/652552" target="_blank">📅 19:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652551">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_057i3Cs0MjDFXk-dqlIM_HN8PoOs79ySJ-CieMLdiDoKUjquCQ7lHVKOZGGYVzXzKQTHnrcnJU1RjjC6hGni3U1BROveOAx9ajjx5ggnvyRnBsIMfi7V95WagBLSMlQBoQoT7fiOlbrgTFp1aD-MzPMSk6V0pXvVEwynLdCL7wgAKcotBMA7mU4Wl5eUu1-tdG8IfRINP8v83GGO8vUj-xlqtFJ1nT1L1bZDWNMFipwl9JOMmWp4rrfhTIrsssDZgNzqMetSh_hFqPyQizM-f_wxmVr9OshEg0hfVKFXZ_Law7jClz4NU_pB0esnb3FDO8KMj1nYiZ2SrgMUXMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان ملل به نامه نسل زدی‌های ایران پاسخ داد
🔹
دفتر امور جوانان سازمان ملل متحد به نامه ۳۰۰ هزار نسل زدی ایرانی محکومیت حملات ایالات متحده و رژیم صهیونیستی پاسخ داد؛
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/akhbarefori/652551" target="_blank">📅 19:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652550">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
۲۵ درصد ایرانی‌ها فشارخون دارند
🔹
معاون بهداشت دانشگاه علوم پزشکی تهران: آمار و ارقام نشان می‌دهد که ۲۵ درصد جامعه فشار خون دارد و همچنین ۱۱ درصد مردم و ۱۴ درصد افراد بالای ۳۰ سال به دیابت مبتلا هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/akhbarefori/652550" target="_blank">📅 19:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652549">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bhz0gk2UZHILyrj9U2b5vRmxjssKrmxqJJTKK86-A4EyZFN31cJQpocMwPsCbYpwJPcvp7ZddIOYKjFDxKST0_ogKoLvzqzy_I0x23_d9OTVcrGWeDoce7SahfNSeZlfh3YMWQ9J8DDeT_6YJ6sL06eGR0-X_kzvx7EFLniorYNRiMumBvSWH6IRysDoVap2HIgW4kPb1T9ladOMSK8XImDYM_cJiimqamCqfX5YOAnCSk0h1a9o8hTIFqNuDnvGMD7Dmi_MRUB8ec1PLhCdNmW5eoE9QEwKGGLZggccBuNzFywGSIJXFnMcpnUFktp7qn-d5qPW1wHafRIoKNms9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهدی میرزایی فعال مجازی: ناهماهنگی بین نهاد های مسئول عامل اصلی انتشار اینترنت پرو برای افراد عادی!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/akhbarefori/652549" target="_blank">📅 19:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652548">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at_4ms9FoKvJ6ceWNWOUlfp0Dm1IymCxh1r4a4Mrjs-o4zzxzUrt-pW3hIwh1NeR7_aPH7vUWnx3ZjLsUm-CTCgS1UEXDuJjwsnxeOsxqI8z0KO7CCe9M-Yz-8H0rxpcRknKH2RWhzdFojHNm8YlljlXhZvajqLDWCJdX3oIAMFwIdwwJFKBrEzWcOOIcvfdjkuf5W_MinBkBceV1Z2iQ1oJ3wwd-bLqTHz1vb1V6bxQIAL749Dn8soVLLU65O5sZ4ZnjwYJCJJQ1hHX9iYyW2a-LhR9wzx2V8AkXp9UqAyN-dhwYQr_esshgLzJSZXExzEq8MsHQfD1ONMHH5Lezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصناف و اتحادیه ها تخلف میکنند، اپراتور ها توبیخ میشوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/akhbarefori/652548" target="_blank">📅 19:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652547">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
بازآفرینی یک عملیات؛ نابودی پایگاه آمریکایی در کویت
🔹
این ویدئو لحظه‌ای را بازآفرینی می‌کند که خلبانان جنگنده ایرانی با نادیده گرفتن همه احتمالات و تنها با دو جت کوچک اف-۵، در حمله‌ای جسورانه و ماهرانه، یک پایگاه به شدت مستحکم آمریکایی را در کویت نابود می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/akhbarefori/652547" target="_blank">📅 18:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652546">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4ffc8c09c.mp4?token=vC0I2LwicMdJGDZE_eQWn-9dEIlcluzFH-85y90O2u29z2yhV22yyXnC0T4WrU2Hce_eAgdrpitwW3IlEM3TdvoqW6ix-2ZVPQwpz_Hw_y48qGlQ632ctJ8Nv35RRWyAB2_39wKhfwBmmg2r7OxQOcRS-yogK9Y9-MFnu_RIdC2J_FsjtoZIH5aaS8ivKAUBerdUMEEODSiBEO6a4RVKpHfRf9-_pYCEOe5HRj2pgNLE1StYeOJiB-croU10GYHiHkwPS6kR-VkpOd3Aghbu_ePdnEQ0HKiiC5vqYJCGT8zX5XFJdtqyFHn9F07GQehZ-aznE864VwPdX5DfXgQzxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4ffc8c09c.mp4?token=vC0I2LwicMdJGDZE_eQWn-9dEIlcluzFH-85y90O2u29z2yhV22yyXnC0T4WrU2Hce_eAgdrpitwW3IlEM3TdvoqW6ix-2ZVPQwpz_Hw_y48qGlQ632ctJ8Nv35RRWyAB2_39wKhfwBmmg2r7OxQOcRS-yogK9Y9-MFnu_RIdC2J_FsjtoZIH5aaS8ivKAUBerdUMEEODSiBEO6a4RVKpHfRf9-_pYCEOe5HRj2pgNLE1StYeOJiB-croU10GYHiHkwPS6kR-VkpOd3Aghbu_ePdnEQ0HKiiC5vqYJCGT8zX5XFJdtqyFHn9F07GQehZ-aznE864VwPdX5DfXgQzxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما عزادار دل خون جوادیم همه
با دل خون شده مجنون جوادیم همه
عرش را غربت او یکسره غمناک کند
رخت مشکی به تن پهنه افلاک کند
🔹
شهادت امام جواد(ع) تسلیت باد
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/652546" target="_blank">📅 18:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652545">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
اعتراف تکان‌دهنده مراکز فکری آمریکا در جنگ با ایران
🔹
اندیشکده‌های آمریکایی از یک غافلگیری بزرگ در این کشور خبر می‌دهند. غافلگیری که محاسبات را به هم زده است.
🔹
در اتاق فکرهای آمریکا درباره ایران چه می‌گویند؟
در این ویدئو ببینید.
@TV_Fori</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/akhbarefori/652545" target="_blank">📅 18:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652544">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5nwijxR0Nh9Tx1OtlvjOs5Z-pGgDdhq0jXTAl38kCIaQ0cTn6PlsH1KOjXf7aJ7oZ7agNh0AZnlNrXyUjTxLIwTgWPHZwVPq9qMY4gfSwFTqlU7Kf12cEiTtzMQvWXWh2wii_U5AIdK0wdUqhAYs5lGJnR3Um0Fe3NPPWG49mzmq3XTHQsIFHNtyusnLwSEx6xDKB__CNRCkG5CiYATHzHEqTBcVEPnR-4wXyBUeYOu7WjEdKdh2bZ-M9DkiUem8khWa5uX2tNrFxk1g_aMqPB9TTBhkShDpZvOEULr8ZPVA6RMLtaEO98WEGo-rNam-ai6oU0bLZHJuiqkTM_-wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن پالیسی: جنگ یک جرم بین‌المللی است، اما چرا بدون مجازات باقی می‌ماند؟
🔹
دولت ترامپ با انجام حملات هوایی علیه هشت کشور تنها در یک سال، اعتنایی به اصول منشور ملل متحد یا هنجارهای بین‌المللی نمی‌کند. ترامپ حتی صراحتاً ادعا کرده نیازی به حقوق بین‌الملل ندارد.
🔹
او گفته است که گرینلند را به هر طریقی به دست خواهد آورد، کنترل سیاسی ونزوئلا را در دست خواهد گرفت و همچنین تهدید به نابودی کامل تمدن ایران کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/652544" target="_blank">📅 18:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652543">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
کپیتال اکونومیست: درگیری طولانی با ایران، قیمت نفت را به ۱۵۰ دلار خواهد رساند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/akhbarefori/652543" target="_blank">📅 18:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652542">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
صدور دستور توقیف اموال ۱۲۹ عامل دشمن در آذربایجان‌غربی
🔹
رئیس دادگستری آذربایجان‌غربی: دستور توقیف اموال ۱۲۹ نفر از عوامل دشمن به‌دلیل اقدامات ضدامنیتی و همکاری با کشورهای متخاصم صادر شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/akhbarefori/652542" target="_blank">📅 18:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652541">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK04OukWJo6rN7YxTaXerEqIvky__aS7sMCNOYRgWIjmlUn7Hr_RArW3M8WUo5vD3ZUqZAvhDWp4e4DJbgz9JBMBpw_ciI8uXeFDudMVt-2MdqC3uFn7zxa9BpaJLiHW5A8CIspNJ87l5SGVq8fSwwkyj_IbgaZwMdWzIdCgvDJYblUsfoOBE7M3g5BL5CibrCjqcQC1XTouIBPog7AIXFPA_B9FLvAoh-bgH5kMvLG3UsOP7h2NOqDEP7k5PiIroY7okX3HvsJgfW0nJK5a6F5V06oH_u3H55A9-tkPJplyu16ULQq6YPGtO9TiXXTuStV_J4awWvx99_2JwE3X_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: کنگره مهلت مهار ترامپ در جنگ ایران را از دست داد
🔹
به تحلیل روزنامه آمریکایی نیویورک تایمز، جمهوری‌خواهان کنگره فرصت حیاتی را برای ایفای نقش در خصوص عملیات نظامی آمریکا در ایران از دست داده‌اند و این قانونگذاران که ماه‌ها اختیار جنگ را به ترامپ سپرده بودند، حالا به‌خاطر همان کوتاهی، دیگر نمی‌توانند در برابر تلاش‌های دولت او برای دور زدن نظارت کنگره یا گرفتن مجوز از آن کاری انجام دهند.
🔹
از زمانی که ترامپ جنگ علیه ایران را آغاز کرد، جمهوری‌خواهان همواره تلاش‌های دموکرات‌ها برای توقف درگیری‌ها و وادار کردن رئیس‌جمهور آمریکا به کسب مجوز از کنگره را مسدود کرده و استدلال کرده‌اند که چنین اقدامی ترامپ را در جنگ تضعیف می‌کند.
🔹
با افزایش تردید در میان برخی قانون‌گذاران جمهوری‌خواه درباره جنگ در هفته‌های اخیر، آن‌ها بررسی مجوزی را مدنظر قرار داده‌اند که اهداف و معیارهای محدودی برای خروج نهایی تعیین کند، اما پنجره ۳۰ روزه پس از آغاز جنگ برای بررسی سریع چنین لایحه‌ای دیگر بسته شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/652541" target="_blank">📅 18:09 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652540">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3NQBZDdvFSrDeyNW6g7LaJ5yTHiy_dSlDfaaoCF2ThR1gXAUclVprlTuWjyBZEUTRV2N6vwK3QelfJoi4BAqVgwrp016UdOhM7ZVqr3I1gkYJ0x0l8EoNZXPaDv7Z4OK-mLz-a9r2eHCGf2w1LjhnUGoDceDQpaf_8KJM2YrMyLjoExjyFr5D2X8MwesW4-3NI3RmWqguoVXD66PgepZKWgmu8DqhMDDWMCPgdUtKUDwEBOVdV-RCG0iM_5PbtXKLlIfa3-m2KXig6tjnkIe8lXP8Dpdaqrzr290WkwPdEg6x0X6AfY-jyQfhYWS0vaNd1aHEzkM685K28-IXP43Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار بسیج؛ سرلشکر شهید غلامرضا سلیمانی، معمار تحول و مردمی‌سازی
🔹
سردار سرلشکر غلامرضا سلیمانی، رئیس سازمان بسیج مستضعفین بود که از سال‌های دفاع مقدس تا عرصه محرومیت‌زدایی و فناوری، حضوری ماندگار در ساختار انقلابی ایران داشت.
🔹
این سردار سرافراز در ۲۶ اسفند…</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/652540" target="_blank">📅 18:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652539">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
رئیس مرکز وکلای قوه قضائیه: آماده اخذ وکالت ۹۰میلیون نفری از مردم ایران به خون خواهی رهبر شیهدمان هستیم
🔹
حسن عبدلیان پور:
🔹
وکلای ما در عرصه حقوق بین‌الملل به صورت ویژه با تشکیل کارگروه های تخصصی به طرفیت از خانواده شهدا و جانبازان بحث طرح دعوی را در محاکم داخلی و بین المللی دنبال می کنند.
🔹
در دادخواست‌های خود علاوه بر کشورهای متخاصم و حامی آنها، شرکت‌های مختلفی که در تجهیز نظامی دشمنان فعالیت داشتند، طرف دعوی قرار داده‌ایم و مطالبه خسارات وارده را از آنها خواهیم گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/akhbarefori/652539" target="_blank">📅 17:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652538">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un6-cTEHeszgzrnGrGnrUFqHzD8dJNYV9yN2aGzvbWCTt6xuWMIjHfvOXmioD1hT7IqVhzzba4SHngeFBUEXo6RweKEUDoHjgE4LV5L5a_C-LxN2pAKyl-DhFc5t3-02onC8mWko_9bnFPr97-hUpYQ_llVrzMnOFXMWlynBhAsP43hg5dahzHs2KZ4toFMfemJle_c53XYn_zOmtOO2RiRSU-YrT-uqFKQRZAjh0GZAlDJd3hPLFZO2jxQKrqk9KDcaryUGzyZTfGNJKub1P0i6HWzUYpuAL3fmzgTikD1J7kFsbms1rIOI_t9-SUuFB_xHv4tCswhekBaAbrWs7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرگردانی ۲۰ هزار ملوان در تنگهٔ هرمز
🔹
حدود ۲۰۰۰ کشتی با ۲۰ هزار ملوان همچنان در تنگهٔ هرمز سرگردان هستند. از زمان شروع جنگ رمضان، ایران کنترل کامل این آبراه استراتژیک را در دست گرفته و قوانین جدیدی برای تردد کشتی‌ها وضع کرده است.
🔹
برخی از این ملوانان حتی وضعیت قانونی خود را از دست داده‌اند. شرکت‌های کشتیرانی پوشش بیمهٔ آنها را لغو کرده‌اند و حالا دیگر نمی‌توانند وارد هیچ بندری در جهان شوند.
🔹
جکلین اسمیت، هماهنگ‌کنندهٔ دریایی اتحادیهٔ بین‌المللی حمل‌ونقل، وضعیت ملوانان را با دوران کرونا مقایسه می‌کند. او می‌گوید: «در کرونا ملوانان ماه‌ها در کشتی‌ها گیر کرده بودند چون اجازهٔ پیاده‌شدن نداشتند. حالا دوباره همان وضعیت تکرار شده است.»
🔹
این درحالی‌ست که سازمان بنادر و دریانوردی ایران اخیرا با صدور پیامی علام کرده تمامی کشتی‌های درحال تردد در آب‌های منطقه، به‌ویژه شناورهای مستقر در آب‌های سرزمینی و لنگرگاه‌های ایران، می‌توانند در صورت نیاز از خدماتی نظیر تأمین آذوقه، سوخت، خدمات بهداشتی و پزشکی و همچنین اقلام مجاز مورد نیاز تعمیراتی بهره‌مند شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/akhbarefori/652538" target="_blank">📅 17:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652537">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huTaZnwkGIyzJgNc6izXOeZYTuXEH1nIA-YIgCDw-KVQ5U_-rt7miJOGD9PFrEZEDke9IDOMUmKCdnACDT2Hmj3hII-0TzvKA1szXPIfL-RhqWCNpkwD7YqOfI-MZFKSrl42SMGjx5wXClWSfqjylkTAysFe2qytqu36eM1C-9LplJWLyu8wDH0GBX0DJNlaD6Ju066pPLlPbdtEcwO0O_vdd0gIZjYwTpbqXwjVk3tECTET1EuuWU3GZKLm9Fn-8fSQmedS1kgTNxmH_VXMlchK3jAb1Od9k_S9SmzD4BEpZISGr0615sR13tPRSVsu4vPN8lGLLa-pqACB5dtN5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی حماس، شهادت «عزالدین حداد» را تسلیت گفت
🔹
سخنگوی حماس شهادت عزالدین حداد، فرمانده کل گردان‌های قسام، شاخه نظامی این جنبش را تسلیت و تعزیت گفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/akhbarefori/652537" target="_blank">📅 17:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652536">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbWi2cMsrtVMLYXJE9HbWrL9Lrouy3D38Gqy_49x-3Ltn3Hf17E_xllJIU4UEhlQJa0ckH43J64fHNnbih5buDsRypH8wcoChti5l1-BqAmWrk3J_KldpaqqNlmUlI5msUtzX-uZkeexShv1lq5WWqYQKxbuzRy74JB_J5BnPQ-B56n3jaTm6krzcbsPnV0rrh9gQ0v6eWWu6vnco5gRkN2EK84kj0ZBI3Id-3HxeQjeOjcKtTIPorYQLYL2mvOkGqR3v7PkxutffW1Sa4IGlmy3p6NVyDUbXq3G8rUU5d6VaGGwOKYvBt5jVBvhUSpe_XhEJC9YEhuBrAWosyDqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرگردانی ۲۰ هزار ملوان در تنگهٔ هرمز
🔹
بیش از ۲۰ هزار ملوان از کشورهای مختلف، اکنون بیش از ۲ ماه است که در آب‌های خلیج فارس در کشتی‌های خود سرگردان‌اند.
🔹
روزنامهٔ فایننشال‌تایمز در گزارشی به زندگی عجیب ملوانان سرگردان پرداخته و می‌نویسد که ملوانان برای فرار از ترس و فشار روانی، آخر هفته‌ها روی عرشهٔ کشتی‌های به گل نشسته کباب راه می‌اندازند؛ بعضی شب‌ها دور هم جمع می‌شوند و آواز می‌خوانند.
🔹
با طولانی‌شدن حبس در دریا، ذخیرهٔ مواد غذایی روی کشتی‌ها درحال اتمام است؛ برخی ملوانان مجبور شده‌اند سهمیهٔ غذای روزانهٔ خود را کاهش دهند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/652536" target="_blank">📅 17:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652535">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKF4JUBxBm6ikXn7UwfsvKuYlMzXWhFkr_O0bnxkYzXUCrJSlj7LdULPFfBeWGqVkXCKmr1RRlX9ISEiuCZQLiM16quniC5OImsFcHtrF_itr9nL6LBQ4SmjiB9vKzqlnpIov5p0r32Dh3uRQhguXMIZvu5UH2crktyv5Otockn8NQEgUhYe40xQ2YquQ_18HpM53neUkACFE2FU8rb5UEEKo13aar8sXzmBMmOnwsnlozGv3Wl_HNspt67Nkuw--pKus0CPzAAjbE5rx3orLuAdRd7zxUdYzObdhMwqZO_cmZEAUsgH37W6l__rwyaM4GDEa_JMIDKLaks_meukFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاریخ اکتشاف نفت در کشورهای منطقه
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/akhbarefori/652535" target="_blank">📅 17:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652534">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f74d66ef34.mp4?token=ApBqakvLynTeFvYgDw2ssb5oAU53I0Y7-tnAwlHFTIrK0SyWqbplDL_zsfge_qnfsVBjJbEvYgNLBCZRhaxlOp9rFVg0VxRmjEOBy9gAyCGNEHjj3X9qZYtCMZBUNBXoi524MIRawOuPIr9HHMn_O2r-Rb-zHkljy7_5qifD0Vo4JHGNhpMz0B8xloB1JUr6C1GP0yyV7ZKZ46dWN8qPvDjUHJACf3i5OZZE60OFABoOme2vWFWWTmUHPJC9VagsyjlRINjQ17HPkPIA_vuGCAXYf6Dh9jTlq6Vmf3vFVOoomB54YC5vms6cvxs9Sqon92RQVo4VLOr8uwk1KPTIIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f74d66ef34.mp4?token=ApBqakvLynTeFvYgDw2ssb5oAU53I0Y7-tnAwlHFTIrK0SyWqbplDL_zsfge_qnfsVBjJbEvYgNLBCZRhaxlOp9rFVg0VxRmjEOBy9gAyCGNEHjj3X9qZYtCMZBUNBXoi524MIRawOuPIr9HHMn_O2r-Rb-zHkljy7_5qifD0Vo4JHGNhpMz0B8xloB1JUr6C1GP0yyV7ZKZ46dWN8qPvDjUHJACf3i5OZZE60OFABoOme2vWFWWTmUHPJC9VagsyjlRINjQ17HPkPIA_vuGCAXYf6Dh9jTlq6Vmf3vFVOoomB54YC5vms6cvxs9Sqon92RQVo4VLOr8uwk1KPTIIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت : وام بازنشستگان کشوری از ۲۴ اردیبهشت و در ده نوبت پرداخت خواهد شد میزان کارمزد ۴ درصد و بازپرداخت آن ۳۶ ماهه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/akhbarefori/652534" target="_blank">📅 17:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652533">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJyZTRiwNh0bzfwiig_mOYGkSg3vbM3wEyH_7g1qtlvpFqGgW8UP_PdDplAIOiOj5myJFkGmfzogs1zpXQXWxPVjR7ggKY9zBXjyE64KfEXhBLoCmT-x5ThL0MKCrDnvc3Lrk0aCzY5Fu_qTMwz6kAXJ-NnNf7iBk3M_X4HFuw-vYPqSBkN1nxzskuc38ROIhw8WPfmHUG0DMXUwdoDDgcsPWgBb5amE1l7bx9s_NVxERuO6xoneBNvCdE35-bcfMePiZOPB8lUSpoI5MFnCNUy4Wp7yqTTtlB3kPVxGSQW0vJd6TgspKuvUCOqqoOhbGgZtwQvBiy1BaBcdXHcy-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لوموند: روایت پیروزی قاطع آمریکا با گزارش‌ها از بازسازی زرادخانه موشک‌های بالستیک ایران همخوانی ندارد
🔹
حملات آمریکا و اسرائیل به تأسیسات موشکی ایران آسیب وارد کرد، اما برنامه موشکی ایران از بین نرفت. ایران توانست با استفاده از شبکه تولید داخلی و تأسیسات زیرزمینی، بخش مهمی از زرادخانه بالستیک خود را دوباره بازسازی کند و تولید موشک را از سر بگیرد.
🔹
برآوردها نشان می‌دهد ظرفیت بازدارندگی موشکی ایران همچنان حفظ شده و ادعای نابودی کامل این توان نظامی اغراق‌آمیز بوده است.
🔹
سرعت بازسازی همچنین نشان داد که در جنگ‌های جدید، توان صنعتی و امکان جایگزینی سریع تجهیزات نقش تعیین‌کننده‌ای دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/akhbarefori/652533" target="_blank">📅 17:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652532">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB1iPCSssMYiP9SMFUHwcqJ7pw1F6jDHKcoC2trxLCidpbDNSaKFlFj7LIU1q3ZcrcReWf6Y2PFaADf6vEK9bX0COkPqi1Qkd9Jcz4i5d8CYX3zxYAmTg9agvwVA97XjnhbYG4Nx8wTql0qTLFwdCpsP2Fv82BYW-9sp9jmpdiqE_BZI3jDaMdB4dSU2o3MWHoWF7O2el_0OViHQkZagIDZfwoe9_6NpHukTPswjMFCopAAonHJKpobm0SdNBO_I4QimZlVftT2c3RnphVjvZ8LqK67gii_spnkdVQxpo0F-hpP2e2k5dcR0NplDDxia77IHLwYFhenAImWU65njMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قهوه بیرون‌بر، بدون پلاستیک
🔹
هر لیوان قابل استفاده یعنی صدها لیوان کمتر در طبیعت  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/akhbarefori/652532" target="_blank">📅 17:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652531">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نثاری: فرودگاه مهرآباد هرشب مورد هدف دشمن قرار می‌گرفت
علیرضا نثاری، عضو کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
بر اساس یک گزارش موثق، در طول ۴۰ شب جنگ، فرودگاه مهرآباد هر شب هدف حمله دشمن قرار گرفت که به گفته منابع، نشان‌دهنده استیصال طرف مقابل بوده است.
🔹
همچنین با توجه به وسعت جغرافیایی کشور، امکان استقرار هواپیماها در نقاط مختلف وجود دارد و هرگونه جابه‌جایی احتمالی در آینده امری طبیعی خواهد بود.
🔹
آمریکا هواپیماهای جنگی و باربری در پایگاه‌های این کشور در حاشیه خلیج‌فارس مستقر کرده است.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/akhbarefori/652531" target="_blank">📅 17:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652530">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYSRqlpJGZvUGhJT2GixwpjmdyGfz87BQFys3GslBy-mZJMExK3_Q7Wgfni4hcP9xP_0ybRbpHMnot-OcyqmmY7L0V2RbQeXXhI32pVmpQ3fpJg5Lm6pIqor2rCYTc6DaPfLcz5EUvaiakTHpGqquPsX-FPUVhl0Hltz_yjjf0pCbxxDSCCRxFzPld7PcbW8Fkj_o1k69kelzQ1U-5BdMxhXnhC6eWrJ8nUzUHShNJmGq1sHRWogmEvzmWtD1BRbkVLvc0vufaoz2mL6O7g8BekE-LmQ6LCeo3nsuSiroL84fEpLApH23IhuH9gl4W7sZP550JXGkojWJQcRU9szZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار لوازم خانگی در شوک گرانی‌های پی‌درپی
🔹
بازار لوازم خانگی در ماه‌های اخیر با موج تازه‌ای از افزایش قیمت‌ها مواجه شده است؛ به‌طوری‌که قیمت برخی کالاها در فاصله چند ماه تا ۲ برابر افزایش یافته و فعالان بازار از بلاتکلیفی قیمت‌ها و سردرگمی خریداران خبر می‌دهند.
🔹
بر اساس مشاهدات میدانی، قیمت جاروبرقی که زمستان سال گذشته بین ۱۲ تا ۲۰ میلیون تومان بود، اکنون به حدود ۳۵ تا ۴۰ میلیون تومان رسیده است.
🔹
قیمت ماشین لباسشویی در بازار حدود ۸۰ تا ۹۰ میلیون تومان اعلام می‌شود؛ در حالی که همین کالا در اسفند ماه سال گذشته بین ۳۰ تا ۴۰ میلیون تومان قیمت داشت.
🔹
فروشندگان بازار لوازم خانگی از شرایط فعلی بازار به شدت گلایه دارند و می‌گویند نه خریداران و نه فروشندگان چشم‌انداز روشنی از قیمت‌ها ندارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/akhbarefori/652530" target="_blank">📅 17:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652529">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14f603aa86.mp4?token=Lr4hyY8ZgdJsf5vWlIOUYXwifqeLaoUxbJjQ3NbwCX2XDgLESMNJ0bL9TsupqsOZebvzxOu4vFcnAouPz8LaiEo2XcVQ-7HBwq7hwu3uloQcm8axeBy_6hsNjl5lc2YBQ2vIHaig-GQONRYnlpH87Tx7FTWKi8KxB7tIhnkJZiNFYyrL_Xm3T_i86Mfbzct_aoGzUvCO5CXizVPslZOsSIQP7JI1LLlSmcf1E9opbPKOeSRmpsNbyCJ4ZBJ0TWOzeOOwcYmzByOmeTSKd7nrYVErum_aXnxcWfe6gieOzjP2acsHSSWlvCqOfjom6uSAl70ir-ZLWG7ql5-6Heb27Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14f603aa86.mp4?token=Lr4hyY8ZgdJsf5vWlIOUYXwifqeLaoUxbJjQ3NbwCX2XDgLESMNJ0bL9TsupqsOZebvzxOu4vFcnAouPz8LaiEo2XcVQ-7HBwq7hwu3uloQcm8axeBy_6hsNjl5lc2YBQ2vIHaig-GQONRYnlpH87Tx7FTWKi8KxB7tIhnkJZiNFYyrL_Xm3T_i86Mfbzct_aoGzUvCO5CXizVPslZOsSIQP7JI1LLlSmcf1E9opbPKOeSRmpsNbyCJ4ZBJ0TWOzeOOwcYmzByOmeTSKd7nrYVErum_aXnxcWfe6gieOzjP2acsHSSWlvCqOfjom6uSAl70ir-ZLWG7ql5-6Heb27Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از توقیف نفت‌کش متخلف که قصد داشت با جعل نام واقعی خود، ۴۵۰ هزار بشکه نفت را تنگه هرمز خارج کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/652529" target="_blank">📅 16:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652528">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ایران برق اضافه خود را به پاکستان می‌دهد
پاکستان‌تودی:
🔹
سازمان ملی تنظیم مقررات برق پاکستان (نپرا) واردات برق اضافی از ایران برای تأمین نیاز ایالت بلوچستان را تأیید کرده است.
🔹
بر اساس این تصمیم، در صورت باقی ماندن قیمت نفت زیر ۱۰۰ دلار، بهای هر واحد برق ۹.۲ سنت و در صورت عبور قیمت نفت از ۱۰۰ دلار، ۱۱ سنت محاسبه می‌شود. این درخواست برای تأمین ۱۰۴ مگاوات برق به‌ همراه ۱۰۰ مگاوات برق اضافی از شرکت توانیر ایران ارائه شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/akhbarefori/652528" target="_blank">📅 16:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652518">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ta6RkeebiNVSp0ThwN51OcvvduGrH1IpPM_x1qnR1iWpbe-zufsaVGEMq2cMq_nNio5v65KtspzhQn-vBf7oQV_k7GQSETikea7pmJLvflv6DtnSrw3xVEOzflEG702Udl45Ww1wnocHYbg-rK-6J3mYHILB5Gh7c_J1bqGKP-34pxAeCbWxsnAMRr4xuLl3RNMRB-H54MDDrr8Tqh3hg-EOSpPwnMKtvjSI-rWS_zHDmsEHNr8lgTtTpcFe4QF8smo4dmlJ4KX1HGqhiviYqZj9ai2IwMWb-lkSJROeOd75DtqyFoYYXADaT1vG_sDBUlIfG28m7L0z-pHhXsrAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XkaYXTHtUp3D2viWxUL-E9rNODjIjbRR99X5Ef8VLWzxfeTN5TcaLopYpnHhUT77uPs5LlsxjmznDHeweoixrvd_vOZI5MYOmWsXfjazZEi808Y3McprpND37B4sdO-1AEIitKStwOGrn6fYZD8Bo8__qXqPjP9ry8CP1qWajud5XTT2uSHkQenZ5CV5BY5rdKx7RccMLzJWyBlUoTYTgjgVbrASl_slXjwqeGXtcHuwjzr5wn0ZD57-n0p1WGC5H11pyW09Ogk70OvpJI6ytK5JemUzlKbD53NInELRw9fOYS-1q9q3WZsAILXwOU5I4vcxxh3kg4wl7Hj3itw07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/haZ-Z8VJIcYoRiACH0DorEG959lcrvapq_88-thrDbk-3smUukO2XHPnjTjF9rsX0M8fQErovOjpd0jYDPk98UVA9WbZ03q4HpgyEem2AwbxIjZLQigfBNGqg5iTQvuQzAbEiBX85bM_uZHxIKuGyhGQmlCor3rULUF3hQBs2pqeOMf8aLTOMGATBPrH9Reui87i4kKCufeg3VOzF2hsHDX8S3cOYooWCWpD7BvV2x7BbEYiDh9gA5fzsHcjZT7hILbABt4T_Q7l364t7ncYnSf19z3g5AcfLKhefkwg6xYCMCCj5URtjIa95Sv1DnPSUbo6wJsvMoVLLDMW4WsZLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e6xM21HXNcclnWvijmjVv1In1YaXkKr4-_ZSGOZje0ldfnPbLSDbkFBn7jg5fuey_SeDuiAV_pRX1eKuodGnwJ8150Yb-cmdtkct5_QYdcZsW_OwZnz_eth6SU4EvQwl7gLFEk_Kt9XInBc9zWKt7JFDCtMf1S1lKwb2vLmJ6FTazSFIEtA5XBJ7ahH-LgZi6dpaj55dU7ps1CgoO1zCQp7cT_FMTBLVHldLerUbuFZcshnLLzHz7v46W8JiKYCkJgO7rOoKmzKgw6lKp6jdPmTUULw-mMjCmukBYVTC67_n1ooLOOEzy1MPm2My2Hc1XnPg0ECblgo1GQhiG7PQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1PrNnSdsbcznBPujdR5LUCiaajtHq_OEwy67eUbjRXGPggCCAgNxv2xjSdvSP1CNs7l9Z2dbozNbRsTieugbl8svXTtO_ggAvHHLYe9iEqLOWI1rWUDamsNyx_5SsVL9VxukZKFhEf-mKcnWai5Fuo9YzsHvt5YWCPvh-Z_akP4UJrnTxel2aTebBvqaVtUw31X_ylQ4e0VmlDFcdN9f6Y2F1OLJBsFUilUs3URv7UkIUgdpsaiQLS8Z7SUWvKFJiu-4goRfjspMor8Sxn24hFazyNjOs_uGXM33yBa3TmfiiS_9ZmhyTZ5Rjsxt6YCyzg4jES9-faxzxGWrcSBKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HB9U75v4j1KfcnKvfPKjYNe1FF7jQF1Om5rD_6BGhb-B240BpBW3CDcoPFOudVXrP2pHV3YM3XEb4g5LBamYPAHrc0fCmyj4FGVQsAGDybu1v7Jq601m0GZQ6VKdTJNocP93NZMW17qbbfdv1N4fd-iFTDb5E1gKErET5KIZqhNo66WeHXC3TVnvog9bt_E1QWOVYmsAjCi_-Hb_o3lJNE6qB2EhKZZhZIasZAeLg42E1CK2mocIHXRM13nXrG5AmSt4Y15qDatdBjcUjU7xotLHL1Yiyb1jEaKCTBkbF6bS03D0ylI7cjPW1Sf71W_5ssYLi2_T3PbLJsyeDzgvTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VcM9ODZH5UmLnQmgXKnWbzYqa2NtGCRx6__2KhNhcPEAsqK9DCVBo7UNaCZar_5LS5PJvjI4YTbW4xb484S7s6jlmU-4Clxi769xiyTRa6Xc1ZKAs4E7I-gbwgoYBybnyvlk91MrcP3TWMB2j9HGXwlu7cZduyFEh5PfqWQ-JSiQvEZ6hejAx9ApnlPhVKvNaNwGT22zxhhnldBnduvUFkHl0UEyh6FChuJSyY-xKlFC9qP8plZAhYVzNYt1RfVefb8NnqQos5vWV5OPNWRNv5u3AqzlzjpIAGe81WwI-sQl1XFxZDLhE7mfA1NWmsTgce5Wev6DhJb6dG4GO1kBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O300G3EbA6GoKkqddYkabh0AiOCUNW7ACi6qc_p4u8DVP5Y8fmrUSWeOoTPcijTWPAGB4sR-T30d1KNTU8tQKL7Vw6G_oSv83-18AGU9j4aRCmwISwKvgTXQPlcMx4FbpdoR_Fak2IZz5SRbkd3OJhLVrWazy5vLl6Wjy3ZhZoW5OkWFxj7MdM9PUVQU2LcWFRJOftWLg1jl_grurMfKaf7mlyxYODaT9mfIDcgsxDZuiyD70PaL6_FdStOPEog8uZL2QGc8vATfo1Ui6DO3WoTc7Msz11JDp3WJZdG9ezHKhN-XfAyeZY72NZTfEpzmY6n-1OjkANQ2XrqoF--XEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_bzD79FumrFjda7kF9tmknky9WUGon1zZWPMBGXJZP6D57lsSwfEx3QaF_9xpcQw2VUvFeOLGLkTIPKYJVtltkqyl8TLRK9TeOZWR8hWJxNpvxaUEjP8-XE5yHcau9Y0MTvEEsSE3nquDqRS-zQjtPn0AiaBoJCeXY46sZrDqnvoJ_OWJr7LIuC5zffG_meGDNfVr9Zy6tCnHHSDhx4mSkHE5sGy-lYlpqz4G0Np2axaBy_dWu26vxQ2XOIex4T8fEOenRlgWBWKs2wIPeNXlm1X-Qrt-nazYvyDDSBCRn5NlNIDfP9sYpduhjH7SuNBciKBr8RTqDAnwD-5dFF4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ot3rb7tn9OAbRzGlsaPFikIOmme183_gyC1EBajq47A9l4v_NqzxQI_ekVA1F7IyTAFqaupDu6lwfmHXX33Yu7bol85oVagKMh2YWxOE4UhCQgSTE1-miAsLCNuHXxXPkpRKfT4fOfn7CL61h97tjcRFNtPWC18-gJV51_HkL_c7rY96ekv3zyFSyvKmu7lrL6ihGZRP_l1svB2rmpyH3E2RocgrbUfTqEtDGRGOBnrHjhMgnaky_2HdBNq-0fWQN6cqKVlpIlGfBX8hD5yr4dSpL27znhcuRHWftLuuGYNBS4kTKodZAtZltRclzaGVrURJ0wg8ihlDCj3anpqnUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت همدلیِ واقعی
💫
✨
#همدلی
اینجا یک شعار نیست… یک جریان واقعی است.
#هیات_قرار
با همراهی شما مردم عزیز، ۳ رأس گوسفند را قربانی کرده و گوشت آن را  در راستای حمایت از خانواده‌های ایرانی میان خانواده‌های حائز صلاحیت توزیع می‌کند.
این جریان، با شما زنده است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_gharar
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/akhbarefori/652518" target="_blank">📅 16:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652517">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حداقل جهیزیه چند؟
🔹
قرار بود یک سری بزنیم ببینیم یک جهیزیه حداقلی چند در میاد. در نهایت شد یک چرخیدن حسرت‌بار در راهروهای فروشگاه! لیبل قیمت‌ها برامون شد یک ماجراجویی پراسترس.
🔹
این ویدئو را ببیند تا با هم بریم در یک تور قیمتی!
@TV_Fori</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/652517" target="_blank">📅 16:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652516">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ro8adBTuOJ5k3eIYtGt3D-rD06favVP3gP-r3Ppz7pxkHR6D7A5ML-ES2fd6GdjeZwI4ybMQUaK79ZlUzp8PXJorqd3xHeoWM8Euk0aeEQ7ldgWFf7u9BUihnmaj1obDoXneB5XxCE-OQ2x_zuvuYj8ns_EvHQPr2rKW96SoFpUYI-AfMErQVvFkqXn2hTQ5qBO3DBnaE_bKMIXxpWx5Yj0XEuPRZXJPNOAxBfdxV45fXL7_uxLbq7xtTAYkxowp3_vFf_wmtAtyuKcKgSqODiRYsYpAKiaFyYqM02BehtIbgoSHN0e87zKwzRL1uUCT-0u17HZCtRT__QAS5T6sxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه MS NOW: دولت ترامپ احتمالاً هزینه جنگ با ایران را «کمتر از حد واقعی تخمین زده است»
🔹
مقامات نظامی آمریکا در کنگره شهادت دادند که برآوردهای قبلی آنها از هزینه‌های درگیری با ایران، ابعاد واقعی پیچیدگی منطقه را در نظر نگرفته است.
🔹
علاوه بر مخارج نظامی، اختلال در بازار انرژی هزینه‌های سنگینی بر اقتصاد آمریکا تحمیل می‌کند. برآوردهای فعلی بدون در نظر گرفتن جنگ‌های فرسایشی فاقد اعتبارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/akhbarefori/652516" target="_blank">📅 16:33 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652515">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f98522fdb.mp4?token=oP_IAKVGferZvoiJDv1WyQnFIw6sivSz7uRpRAKz57W0CaIG8QGqCUfKnyWprS9z7mqzb6iZ3Xabg0cRmpn-LjwtYazCokfsC6qVygBrPOG8BGZOH8ht7nlum-3UrHgkgsthvlFlxA3ItWdulahW4HSrpvNhMnPLyJ9dro_19pUkipgQuDC6JF-JFq3AJHJzNSM8_2DaDYva6yZPlrzoFG9PXVHuxD8Z4FMAL5OmQxM204Qk9V1ZgnabHd4lIrojfXcAWWuf-vYBFdwRmtrRfOYkqcJS2Pg81U02knVoyqeqyuUBSL2kqaUgMCsiAJVRzlNWDfN2XduQS-1kwod2RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f98522fdb.mp4?token=oP_IAKVGferZvoiJDv1WyQnFIw6sivSz7uRpRAKz57W0CaIG8QGqCUfKnyWprS9z7mqzb6iZ3Xabg0cRmpn-LjwtYazCokfsC6qVygBrPOG8BGZOH8ht7nlum-3UrHgkgsthvlFlxA3ItWdulahW4HSrpvNhMnPLyJ9dro_19pUkipgQuDC6JF-JFq3AJHJzNSM8_2DaDYva6yZPlrzoFG9PXVHuxD8Z4FMAL5OmQxM204Qk9V1ZgnabHd4lIrojfXcAWWuf-vYBFdwRmtrRfOYkqcJS2Pg81U02knVoyqeqyuUBSL2kqaUgMCsiAJVRzlNWDfN2XduQS-1kwod2RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم رصد هوشمند در پهنه خلیج فارس و بازگردانی و فروش نفتی که قرار بود در نظام اقتصادی اخلال ایجاد کند
🔹
در تنگه هرمز دقیقا چه خبر است؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/652515" target="_blank">📅 16:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652514">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiFaGB4ruD2zJ-EImpbSR50kGEa7TT7I1Q9ta3Q6zhAForkgoG_F5u8J0sEFAb_eQ9jvxSMv3mdqiqwpia2kj6W5eGQfeVChW48xqALpGsNdxwDL0qSrK4TjIQBYWPAKjfpFvvmBwMmCS9AlMOgTeAixuA9cUDgaOha08t5F8qp28hq8V0mkIvME4AvO8WpZRlcMBso5NdzAhwTr0Ggfx9CN1nR3UYJX2CqcYlhBbnbUb_m_QoI-bEa82DOh4-yIQkSVFaD8PRa4wpzVhuWzNIyoEH_aG4yMyQmM1pdPYztApPFRAMRUAgqS3TngdWaA-YTRqslFuC6-AAumOeZ7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زوج‌های جوان در سال جدید نیز از بانک‌ها روی خوش ندیدند
🔹
از صف وام ازدواج سال گذشته حدود ۵۴۰ هزار نفر وام خود را نگرفته و به امسال منتقل شده‌اند.
🔹
با این حال پیگیری‌ها نشان می‌دهد بانک‌ها تاکنون به‌صورت جدی پرداخت وام ازدواج را شروع نکرده‌اند.
🔹
پیگیری از چندین بانک نشان می‌دهد که اغلب بانک‌ها با وجود گذشت ۲ ماه از سال یا پرداخت وام ازدواج را شروع نکرده‌اند، یا اگر شروع کرده‌اند بسیار کند این وام را پرداخت می‌کنند.
🔹
یکی از بانک‌ها در پاسخ در مورد تعداد افراد در صف می‌گوید: «سیستم ما آمار در صف را نشان نمی‌دهد فقط بانک مرکزی می‌تواند آمار را ببیند.»
🔹
در صورتی که پرداخت وام ازدواج به همین روال پیش برود نه تنها افراد در صف موفق به دریافت وام نمی‌شوند بلکه تعداد بیشتری به سال بعد منتقل خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/akhbarefori/652514" target="_blank">📅 16:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652513">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4d0b9089.mp4?token=dCsQdINKfMf8wW3zF1HCPuKlcW8Yc22NYO9RgH94PvBVwEVkAAXwBAitwe5CKAaNF9HC-SQdP190sXGCtM8Ep1e244v2N_34Q1avypbPglH7_ASBF_CsBBiqgvxyaUDspGbN_f0FA4QB4h5UbgINuVDk9pW5lshG8E1v7NX3lbVyP14hdnH8tue0ZCcUXutML8DE4sSrTNz2Z6o-Zv0xNC0ps33FAGu2fmUlil5p-MDQJ_UXB6PZMlBjTc78ROq4K_cwYTbFMca4dKveh6fUXZlbElh4Gg8gPBTrJQWcCfb4t1f84ZjwdGb_3k787Sc1EB1OtmUpt1eozV-hUzD0yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4d0b9089.mp4?token=dCsQdINKfMf8wW3zF1HCPuKlcW8Yc22NYO9RgH94PvBVwEVkAAXwBAitwe5CKAaNF9HC-SQdP190sXGCtM8Ep1e244v2N_34Q1avypbPglH7_ASBF_CsBBiqgvxyaUDspGbN_f0FA4QB4h5UbgINuVDk9pW5lshG8E1v7NX3lbVyP14hdnH8tue0ZCcUXutML8DE4sSrTNz2Z6o-Zv0xNC0ps33FAGu2fmUlil5p-MDQJ_UXB6PZMlBjTc78ROq4K_cwYTbFMca4dKveh6fUXZlbElh4Gg8gPBTrJQWcCfb4t1f84ZjwdGb_3k787Sc1EB1OtmUpt1eozV-hUzD0yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عارف: ما از حق حاکمیت خود در تنگه هرمز گذشته بودیم و اجازه دادیم از تنگه‌ای که متعلق به ایران است تجهیزات نظامی که قرار بود علیه ما استفاده کنند، عبور دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/652513" target="_blank">📅 16:21 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652512">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بدهی همه زندانیان غیرعمد ۲۰۰ همت اعلام شد
سید اسدالله جولایی، رییس هیئت امنای ستاد دیه کشور در
#گفتگو
با خبرفوری:
🔹
مجموعه بدهی همه زندانیان غیرعمد موجود در کل کشور ۲۰۰ همت است. هم اکنون در کل کشور ۲۰ هزار و ۳۶۵ زندانی غیرعمد داریم که از این زندانیان ۱۵۶ نفر بدهکار دیه، ۱۶ هزار و ۳۵۸ نفر محکومان مالی و ۳ هزار و ۸۵۱ نفر زندانیان ناشی از تعهدات مهریه و نفقه هستند.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/652512" target="_blank">📅 16:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652511">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
بارش باران در تهران ۴۰٪ کمتر از حد نرمال و وضعیت آب تهران وخیم است
احد وظیفه، رئیس مرکز ملی اقلیم و مدیریت بحران خشکسالی:
🔹
سطح بارش کشور در سال جاری نسبت به ۳۰ سال گذشته نرمال است، اما بحران خشکسالی حل نشده؛ بارش در استان‌هایی نظیر تهران، قزوین، البرز، مرکزی، سمنان و گیلان ۲۰ تا ۴۰ درصد کمتر از حد نرمال بوده و وضعیت آب کم‌تر از سال‌های گذشته وخیم‌تر خواهد شد.
🔹
پرآب شدن سدهایی مانند لتیان در تهران به معنای حل بحران نیست؛ خروجی آب صرفاً برای تولید برق و ذخیره‌سازی کنترل‌شده برای تابستان بوده است./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/akhbarefori/652511" target="_blank">📅 16:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652510">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4ddbxcxmAFXRGDoeOxrzE-TzaBOQG3fTy49tD-WPkK4rhG6DnAae6aLgltS8e3atkddX-GXPpMAFCE0uW5AGmAAPLLYmyZcX7wQfb9TtqNkjOhh4MFCr_NQ9DH09a5KE3zIP_8A_rcm2BP03C3eGlqzPnnxtVH_rkE5-U1yn8aqGxDOgqyEZ9FW9ia_L6G5PgTaAtei-TQib27mkzb7RaWYmJC5QiE0sCIOrr8BMRnj4TvIPwATgqWb3PV6qNPAfuJefkhuHcindcc0nNHunUHMWS4-DVTvCzB-9GFn6nOaZyh9agzVaa2Kf5GfxkYhWSeTd31PJkJkg5gnhCFG5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنجال دستیار بلوند و مرموز ترامپ که تلفن رئیس جمهور دست اوست | ناتالی هارپ کیست؟
🔹
ناتالی هارپ، دستیار ویژه و بسیار نزدیک دونالد ترامپ، به یکی از تأثیرگذارترین چهره‌ها در پشت پرده فعالیت‌های شبانه رئیس‌جمهور آمریکا در شبکه اجتماعی تروث سوشال تبدیل شده است؛ نقشی که در عین حال باعث نارضایتی برخی مقام‌های کاخ سفید شده است.
گزارش خبرفوری درباره او را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3215167</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/akhbarefori/652510" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652509">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQ4Tq600yHcja-wN0wnIkHVEN7fAKl-2YC-f8uL75kCwVsX8lWbru9BmrtzIPxan7rQ3HSOzxAQpkvS0V_GtbHFhurvEVsNA-QGzK2UqlM0q1ILquHDgSr_8TH4mXAdKD0rF4ulNhl_brI4VlQC-GBJ1vHXaqiyntfOTOhcA7V8LTnXMfEd2LKRgow8w_RvEJEnngz2d3LDESUSIqeWoEDYp5GAe0izE_o47z5HKpUhq0OOCSXv0Lzpn0t2qqYTo_BwLhupTSa6Q01uluIIk5BI5X8QYkzufvtyIXbQH2FOzn4DWJuI7B-QjE0K3mUxZ0VdI6srS5SDkIHfGWIVo8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چطور طلای واقعی را از تقلبی تشخیص دهیم؟
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/akhbarefori/652509" target="_blank">📅 15:49 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652508">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76ed043b8.mp4?token=Y0zusJ1ieb1Oi5A9V3d2q6uoSdcWnrW69ez3tRD_wzQ7y04uAqDj6-u9lQWJrb2paMU6JH5q_L5kkEtzlWm7H_YhxqLeSqKZGXvmKtIAIYvuqt_wzfbRaJ8e7fvjT-wF1VVvgxkh8Mb_J8P8hoSHFgZdAHPeivWGc9nb3u9kqk7yklp_ccH7Y_IIAw3N9CWsmQh29bGemDRKRURIfvhNVNAekz3q_vElTwrtC-XhviKwBJf0qYu_NGIs2U3jJ1BxVqGsRFQXZ-_CtplZMXXnP0E-KXSImzxMFLKaysXaH568xkpeacaoToZP9NVzdv-e2GSJV2oz37gp3rCixQSwhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76ed043b8.mp4?token=Y0zusJ1ieb1Oi5A9V3d2q6uoSdcWnrW69ez3tRD_wzQ7y04uAqDj6-u9lQWJrb2paMU6JH5q_L5kkEtzlWm7H_YhxqLeSqKZGXvmKtIAIYvuqt_wzfbRaJ8e7fvjT-wF1VVvgxkh8Mb_J8P8hoSHFgZdAHPeivWGc9nb3u9kqk7yklp_ccH7Y_IIAw3N9CWsmQh29bGemDRKRURIfvhNVNAekz3q_vElTwrtC-XhviKwBJf0qYu_NGIs2U3jJ1BxVqGsRFQXZ-_CtplZMXXnP0E-KXSImzxMFLKaysXaH568xkpeacaoToZP9NVzdv-e2GSJV2oz37gp3rCixQSwhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
«خیبر، خیبر، ای یهودیان... گردان‌های قسام در حال بازگشت هستند!»
🔹
شعارهای جمعیت شرکت‌کننده در مراسم تشییع جنازه عزالدین الحداد از فرماندهان نظامی حماس در غزه.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/akhbarefori/652508" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652507">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daJrx9i3TpEbn5ZxtsdX9-Q1dq53hoaTSoeDtx8KOIrYq6IkvPEDMmhbOC6ANwcprxT2ouFJQ__4DYDnmthXlgI7C1jYdTCciKtX5MPT0A9auHPL3K1RMhwvTLQU655aXrQAdG0qVp2rXlSywr5rCiuD03-jJilaQ3pCWFeMA9mDNDbtotgvvhlhDcYf4U3sReg8xXx88UL9djiq43y1StQTH_ZtnhF3XNcBV8yrfnE_80WmUv0J1ZXM037ejrVYRw6d7514nTvU0k75LBt6R71zyE__ooGxT3dml8Uem7ySDaNPF_LOGfUPq0KVvcL7qMFs6os1-1vKN6_zkIl2DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلاش امارات برای ورود عربستان و قطر به جنگ با ایران
بلومبرگ:
🔹
امارات پس از آغاز حملات آمریکا و اسرائیل به ایران تلاش کرد کشورهای عربی حاشیه خلیج فارس از جمله عربستان و قطر را برای یک پاسخ نظامی هماهنگ علیه ایران همراه کند.
🔹
رهبران برخی کشورهای منطقه، به‌ویژه عربستان، تمایلی به ورود مستقیم به جنگ نداشتند و این درگیری را «جنگ خودشان» نمی‌دانستند. همین مسئله باعث شد اختلافات پنهان میان ابوظبی و ریاض بیشتر شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/652507" target="_blank">📅 15:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652505">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRakXSUS5gw1X8-jHAegKMQ3Z-1S60Hr-IOg70jspkSB5a7KbmBtMWZgVPM-CP1ILbLC3oP7ejTa69BB4PY4YOZhMqFMWXKPwl3eLGLnFjzhOWYIgWUfhPJJu2Rfqa_HC78ZK1_ud6_URDz7uxJRHizDPhCFZmnGuc6-pGIZbKhGvwou-dXhKVXy-vQ3OfWJ881yB12aJl2xoIFRJLzuMH5haxeJ5KGOn1mh1c5i773P2D50HVypEKKW5gVft7i3YD-ktUmwJp3rUEb-6d4uL9PJnOxOh2wGomh21BdJdQNApkWSuBxWX1hJxqH4VJgqRfClDt11_JigSCUR4SRLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند خبر کوتاه از دنیای تکنولوژی
#نبض_تکنولوژی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/akhbarefori/652505" target="_blank">📅 15:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652504">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3761ea2642.mp4?token=fzHkaNYlPu_QWjIE83Vvm55HxmLKpZ_g4dOctgDz4pgDe-aogdtzyG_ybZxp5u6ozMx2exUEVrRz0Fkb5DTTG9B_soOWdY9LuPBi-H8XYCU9DJuSQ-bVMhIzvaFu2Zz_t0-UMbM13udcbrjHtn1TqK8bQWpPNqggbRTeyXQpM_PM0c1lDqsGOlmjwI8BBF3G1jQaODqGfzwSKJBJLBYqRuvM7i3HIBO0Ub-MkdFujxUbYxHNgRdaYIXUmh7N-7V73SiKoGwnTiB6U1HqRF2M6HuennfgxJcoLL1zYOVwv_fKvZcUWG82f7uTsxqMt2C2ebDjLVdVCa-SCm-TogsYzkbFYPH4AIVtBX0XZhggLoel0-PoUfUbH4T_9oQ6YHRYzlZgdlQ6KSwx2pi1L2X4Nkg_0M5CPVoepoQ62Vu2DCmILgcQdP0fn6CMGMO2dvYjZYE2QrtqioVj0uZV2TqZJe57Dv5qGWZEJFku-s7oJ1Am9hjJIHWNcfD7kJ55htFjo_xDRko-_GYlYFuceE71n-ii9gVBdr14yz8oNXyhmzxG7vuhNKpftU_MiTPP4LulfW8KKAdFkC-OocqEM5QR0bBr1fUxmuCk9wCqVF1ntA4TnhCwLK6S1LHzs8KJEBCLzVdBP-ME3Cyo6puRP7t6jROkR2ql4UbiYncSD3QYSlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3761ea2642.mp4?token=fzHkaNYlPu_QWjIE83Vvm55HxmLKpZ_g4dOctgDz4pgDe-aogdtzyG_ybZxp5u6ozMx2exUEVrRz0Fkb5DTTG9B_soOWdY9LuPBi-H8XYCU9DJuSQ-bVMhIzvaFu2Zz_t0-UMbM13udcbrjHtn1TqK8bQWpPNqggbRTeyXQpM_PM0c1lDqsGOlmjwI8BBF3G1jQaODqGfzwSKJBJLBYqRuvM7i3HIBO0Ub-MkdFujxUbYxHNgRdaYIXUmh7N-7V73SiKoGwnTiB6U1HqRF2M6HuennfgxJcoLL1zYOVwv_fKvZcUWG82f7uTsxqMt2C2ebDjLVdVCa-SCm-TogsYzkbFYPH4AIVtBX0XZhggLoel0-PoUfUbH4T_9oQ6YHRYzlZgdlQ6KSwx2pi1L2X4Nkg_0M5CPVoepoQ62Vu2DCmILgcQdP0fn6CMGMO2dvYjZYE2QrtqioVj0uZV2TqZJe57Dv5qGWZEJFku-s7oJ1Am9hjJIHWNcfD7kJ55htFjo_xDRko-_GYlYFuceE71n-ii9gVBdr14yz8oNXyhmzxG7vuhNKpftU_MiTPP4LulfW8KKAdFkC-OocqEM5QR0bBr1fUxmuCk9wCqVF1ntA4TnhCwLK6S1LHzs8KJEBCLzVdBP-ME3Cyo6puRP7t6jROkR2ql4UbiYncSD3QYSlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قوانین جدید خرید و فروش ارز
🔹
دستورالعمل جدید معاملات ارزی «تأمین نیازهای ضروری» و «مصارف خرد» ابلاغ شد.
@TV_Fori</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/akhbarefori/652504" target="_blank">📅 15:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652503">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buPLUMs1K2Hf5TzzKzjcuVCKdVuQlDj_Vu7RCfHNzQ3sx0KiIqTmZtEKtyok_yF4WnSDfZu1kxySm6HIGeLmNZbhNlxqUM7r0qV2Uw7zZyd8svz3-xDF6Qp2r39xPvZcdivFD0ncKrjKoYoc6xgmxAajV7keaGCMMNi0YkvS1ETPK2a6VtFBPDe42ndN3kRZybUUCHU4IMuIZd60UR__2fsvr374EUR9x1SjRLC8wkzmCPA35FjWZxpl9YXr4xUCEy1ha7sH1n56HCFsueUOfdQT65oFkFv5zgC_7eh6Hd9ByOcKmxBbVCXAw_UwdgiiSnPmaeZTqKZO2tya3C1Q1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت فرمانده گردان‌های قسام رسماً تایید شد
🔹
گردان‌های عزالدین قسام، شاخه نظامی جنبش حماس رسماً شهادت عزالدین الحداد، فرمانده این گردان‌ها در حمله رژیم صهیونیستی را تایید کرد.
🔹
گردان‌های قسام تصریح کرد که شهید عزالدین الحداد به همراه همسر و دخترش و تعدادی از مردمان فلسطین به شهادت رسید.
🔹
قسام عنوان داشت که این فرمانده بزرگ در پی یک عملیات ترور بزدلانه توسط دشمن صهیونیستی در مرکز شهر غزه به شهادت رسید که این حمله نقض فاحش توافق آتش بس است.
🔹
گردان‌های قسام تاکید کرد این اتفاق بزرگ تنها انگیزه بیشتری خواهد شد که مردم پایدار فلسطین و مقاومت سلحشور آن را به ادامه مسیر مبارزه و مقاومت سوق می‌دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/akhbarefori/652503" target="_blank">📅 15:13 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
