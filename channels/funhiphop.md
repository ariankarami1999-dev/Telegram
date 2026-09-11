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
<img src="https://cdn4.telesco.pe/file/AM-IJkPaQRqobKmehRXEN4iTCP55gzYoEh4wK1hSDS3pzFLDxTx4WB2kfkcKocNlMNIgsiF5DSp9gE13v9HEKGPB0LrWpI1B95zo_vkCdkweH85xgD9TLizAtkMSEiAkJ6_eDPsGPNzUCyntQm1qrfM9nvG119Sq_-iVon33vFEPYfjBmfhwh_0aN5MnLav_3xBoNyCRsTiofp_zUlxMm20J5swIoiy4_Nd-lKbUz0YU-kV6ypcra7oOv5ZclwePk_HD9BERdIVOPnh8K0O0igGG9vrqPJaUA92g033Qm0sL1Z3aDWUl3KvlERz39dDf1WsgiDMJTGg3OpXMJEw15w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 15:07:06</div>
<hr>

<div class="tg-post" id="msg-83267">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cQ7UiFh36MVV9udLs2W_cFYgWo2cutNU6CbkH4jG_DngYx1azMhauHl0l9Vsrt-hd7XUvnRqysUbHUfBL2s0ISYMTuigBFzmrOsuprlTCECryuzPdtNB72lv_cm6SfLA6PZ99YOzdwp39rHch1XSmaUU4aW0vJhiQRdgC45vkFJWkVBJa2P22dJhK0Sa6DEzEE0qwYwUf38ZHAa_7NYmV7zoMmqGBhUz9fGIDmZfM82TIg9K5tvjqezYbkAbsYSNng5XLjXJeRq9hua9Qs18Yo7I3ps1vUULEp5wzcHTDpCSoRr-5j4hYBL0hn-RygKtSCmU7lg485aExIg36xVSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rblCe3wowVCjZaaM7ez_7JmqWqb56kxB6Eyc53SHmOlVpEu8MF-TIfojtmF68OB_i-zlzYbZ7CS38ZiExwbBK6-Lh9-o5XQR8PMS4Z1p9qCD9cCX378T49GOtQ-SdDpQ-wd3ogrzCeeT-nKJjY9azSH_XiLKGl3smhGTk1z8nVb0eE-aArT0tY3t1meI4sY4lHKHUfMW_w8nDpy8jczhRXC_YqNOJuqJBASTpBvewqay-vcmEEXglfzaGE3RXKWMIdYN4rBxnuwwYtEGXeNaIsYIHa6SiVG7xiDDAnKgIWaFMXIB2Ltkd8BKP3wBn7_ACZFFbdeHclc9YBtSK-w90g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همدردی مردم ایران با مردم آمریکا همزمان با حمله تروریستی القاعده به آمریکا 20 شهریور 1380
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/funhiphop/83267" target="_blank">📅 14:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83266">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=WRn8_iWSNo64o6wReQVjVA08k_MHgZYz95UbSnMLuz4viNc9RSqZo3CAqwf3cHzhCwRjYrr6ya74F1-_aFcy5ERacMp6yuI6K4W1tTwFgQ1Nc8QgPDsyi-FqRZD0cF43aaq8TRqgkGdT6KtbEvt902Tk4tngWECqQBereXeKVGUdJRkAwpzuAkztSYYolEDak36-JHYVqigfF70rntlwxg6Yj9dWwjByO7DOxDS5ZguZLH6ZIkiwAxrL-Gd_3gX4Seb9K9sYCbb6xRcnGABdL6DhcwWtMukdRVYfEZXIdt7RXu7w1ZnoPr8l8C9zTxfNjIVcBI25AeO53MClV_ujGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f56d26230e.mp4?token=WRn8_iWSNo64o6wReQVjVA08k_MHgZYz95UbSnMLuz4viNc9RSqZo3CAqwf3cHzhCwRjYrr6ya74F1-_aFcy5ERacMp6yuI6K4W1tTwFgQ1Nc8QgPDsyi-FqRZD0cF43aaq8TRqgkGdT6KtbEvt902Tk4tngWECqQBereXeKVGUdJRkAwpzuAkztSYYolEDak36-JHYVqigfF70rntlwxg6Yj9dWwjByO7DOxDS5ZguZLH6ZIkiwAxrL-Gd_3gX4Seb9K9sYCbb6xRcnGABdL6DhcwWtMukdRVYfEZXIdt7RXu7w1ZnoPr8l8C9zTxfNjIVcBI25AeO53MClV_ujGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت ۱۰۶دلار
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/funhiphop/83266" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83265">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دیشب نه در آمریکا، بلکه در یک کافه در قم از آیفون ۱۸ رونمایی شده، تو این ایونت همه حضور داشتن الا خود آیفون ۱۸</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/funhiphop/83265" target="_blank">📅 11:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83264">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8758825884.mp4?token=dr166vbRmfIKfPzz38hPulYw7vk0JaR3EdVhzuEG1Xv_KU9FYY5P4SjLLJP_e08JFaTgQBD3v4GyKgTyWoIUYgwtgBWbfN9qckWp4JelxjjVQOTlCY_pYUVHUivAZDLkUx8KeDmljD30Hf73fMEL4wztR08M-R_ClB4J1-5JO_-bLOEdbbKeKKqHGdC0uHYEOk2ozD_qwGFeukTQpVJ1xBuPvsc4Lfet_uFsum-4G-KVtGZ3JPWZLXiZLhlUVrs9ySDn-RnzsjTRtPDO9TCNviXJhb3NeymIMVf5lkajylUK5Ej4UGb0MC1W2xdgsr5eabMpcKdTCiKPdxh8AysHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8758825884.mp4?token=dr166vbRmfIKfPzz38hPulYw7vk0JaR3EdVhzuEG1Xv_KU9FYY5P4SjLLJP_e08JFaTgQBD3v4GyKgTyWoIUYgwtgBWbfN9qckWp4JelxjjVQOTlCY_pYUVHUivAZDLkUx8KeDmljD30Hf73fMEL4wztR08M-R_ClB4J1-5JO_-bLOEdbbKeKKqHGdC0uHYEOk2ozD_qwGFeukTQpVJ1xBuPvsc4Lfet_uFsum-4G-KVtGZ3JPWZLXiZLhlUVrs9ySDn-RnzsjTRtPDO9TCNviXJhb3NeymIMVf5lkajylUK5Ej4UGb0MC1W2xdgsr5eabMpcKdTCiKPdxh8AysHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو منهدم کردن تونل های در علی‌الطاهر که اسرائیل منتشر کرده
انفجار این تونل باعث شده یک زلزله ۴‌.۱ ریشتری بیاد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/83264" target="_blank">📅 11:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83263">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=MVEVTpboA1SMaHNRKSgdPD2iCSxYIOdQPu7ASpCwkYdmHhY4dt1aFgMNbokrp0LeWR62PF6yQGq4Egw25_g0EDBQ96RgIChelGXEx_M-JaQvm3_WIKiEVeUds3HvHHcgFi0a06BqlZQfb_yOXld-Y7IWXP0NHI3dKNf_VbD3kxqLJeHuhz3a3et8JVnX3Vq4cjKhQHSuVC3o6TOCaVki5dRctkfGt0GibNGd4QpgmrVVbvKWJIiqNkrPR1vdj9H6sRZY7qMQLt5VQuIQUkeneDtYhdCArDh8baV6WHSDFtUi7EuG9QDUEaaftKRiR6hCp-yOeZ5dkhr-6Ye4gePFpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe621a2e8.mp4?token=MVEVTpboA1SMaHNRKSgdPD2iCSxYIOdQPu7ASpCwkYdmHhY4dt1aFgMNbokrp0LeWR62PF6yQGq4Egw25_g0EDBQ96RgIChelGXEx_M-JaQvm3_WIKiEVeUds3HvHHcgFi0a06BqlZQfb_yOXld-Y7IWXP0NHI3dKNf_VbD3kxqLJeHuhz3a3et8JVnX3Vq4cjKhQHSuVC3o6TOCaVki5dRctkfGt0GibNGd4QpgmrVVbvKWJIiqNkrPR1vdj9H6sRZY7qMQLt5VQuIQUkeneDtYhdCArDh8baV6WHSDFtUi7EuG9QDUEaaftKRiR6hCp-yOeZ5dkhr-6Ye4gePFpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی پایدار کی منحل میشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/83263" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83262">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/funhiphop/83262" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83261">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJxe16V6KDQM4WAv8SJC85YZzuLduw1hyHSDL6ala0mXBu6N-9zBJdyaeSZ44yKPgplGeDjyI0QU1RiLkZED0C1QkY9zYEQVIpGKsDaraItQL2KlUnmh3aOeSV2a_N-pM-Iw_0UaV4OerrhG0tdO4QAmWj02FPJqkKOaR_Vv85koLfnabX0hAl9d99vKSK1T1zM7XivQD_fj7phcTPxsxBWOpWcer0B_DK8SwYKc9u_wjGTXp7Al3fqciJs-NbcxZkzcyVhW3OGInUGX657wn5zRmOwH9iRW2VqTxo7VV50l6_NhxH4dmzH3Xn56kCvweO4t1rndY5dcIabOsrqw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r20
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/funhiphop/83261" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83260">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امروز سالگرد حادثه ۱۱ سپتامبره، یه دژاوومون نشه؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/funhiphop/83260" target="_blank">📅 09:39 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83259">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/83259" target="_blank">📅 02:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83258">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0wkq0gyohSCK8HZx7A1msULhzOkWyprHVXT6yTLXecWuVyoHDZvnD3EQoMRO5FY-8JkuDx_cJt8XfMti03S4Hl9voVC1UWyOQzTw17ZDWj9RfYH7SWU7pXgFxMnLvZw8w6xjExZ1mr4-_LT3KplpobRZ-rOh5qn8BXuxqYTUtFja0Vg0iOVoAK3LCdEKZl8Oas-oYYzjFnXsko3xxX2qeF6_E3LcJDdOJdNxUbNkLlBO3H6l_OX2lKrKCBtGuTHbmGJo0Lt5CFDKwZghnuRKaPGqp_xMLS7jxTqg8jlJ8kqZlgMzFPnDb3bDCqfHfAo_QCq3Fjz2jmYd4q9VehPoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریایی بریتانیا اعلام کرد به دو نفتکش در ۷ کیلومتری عمان حمله شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/83258" target="_blank">📅 00:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83257">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شاهین نجفی الان برا زید جدیدش آهنگ عاشقانه هاشو میفرسته میگه لیلی بهونه بود اینارو برا تو خوندم، درحالی که اون موقع این اصلا بدنیا نیومده بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83257" target="_blank">📅 23:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83256">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmhKPpiwoo9_F-5Dn7YEvCdzqQRepx49KwXVvEIjSBLPXj65RIjWTWGaC5olDquj_c_LJBOFXbC0_5L6qKlzqBrVvIJRHGtWmiAI3Cv5ALbCCssqV3CyZf-h9cp5BpTV-ZWTOCsDqIAmwe29af0PebP-esp3uyooNEX3YW2ZSaPiU_W5Lt89IsAKCumGHf6JoKDK5KOq8kaHuG8SoVNoixAcA55fan75n5IP1NDKsxzdGdKPSiFVYBu9KyTJjXIVjaf0zYnMvgMtIhakPtpmISOMJ33vDOzwXx1svFImujjuhoDXVmGTY23ddoagDbVigeXCCtgezcaUphMcFZnQ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا یه باند میپیچه دور دستاش، با اون ۶۶ میلیون تهش اونو بدن بهتون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83256" target="_blank">📅 22:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83255">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=XJjC3wI7cq3wO8YxT67rqzSKe-_gSFbo0rrI3AWiWiXJ-dF8RSUuWB9mWxFU9_8jXdv2xUKwDW6O3Ys-LNc_nil1shGQT2-STOUSDfYyzSp9CDy0aNUpVnIBelSZcCHrdt2caW7bpMJwR561rb0KouoL2f_ahschCvjDeLBbAN10NWnUPlc6PR4KcZWnpWPe8ymlAJHk1ft_H8jfTp79JxVMUBdgryjLrlN5t8_G3wGz5XeMHsyFTUxh7W79hkkoMwTbOiFsdXzMDxlj8JaLkbTHfTLRGdtW9jgJ1NqwqbULH6GOQtKMX_V7DJ5AsjbnHjLbdTwSn_5eBhhk7s7zkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/774541b7ea.mp4?token=XJjC3wI7cq3wO8YxT67rqzSKe-_gSFbo0rrI3AWiWiXJ-dF8RSUuWB9mWxFU9_8jXdv2xUKwDW6O3Ys-LNc_nil1shGQT2-STOUSDfYyzSp9CDy0aNUpVnIBelSZcCHrdt2caW7bpMJwR561rb0KouoL2f_ahschCvjDeLBbAN10NWnUPlc6PR4KcZWnpWPe8ymlAJHk1ft_H8jfTp79JxVMUBdgryjLrlN5t8_G3wGz5XeMHsyFTUxh7W79hkkoMwTbOiFsdXzMDxlj8JaLkbTHfTLRGdtW9jgJ1NqwqbULH6GOQtKMX_V7DJ5AsjbnHjLbdTwSn_5eBhhk7s7zkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو انهدام پایگاه عماد ۴ حزب الله در تپه علی الطاهر توسط ارتش اسرائیل
پایگاه عماد ۴ بزرگ ترین پایگاه گروه حزب الله بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83255" target="_blank">📅 22:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83254">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83254" target="_blank">📅 22:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83253">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=K4KoFmKb8h_ucRVLy23H5_qAeYk-GKLzAYLtbSAqCMUP2ft49kweD_7Hx4Q89_3v7orm9DJFgaXB4eRldY7TSABUoHHS2KFQI7fwCOXy-6ciUb_nHiObwGBD8pm11s4wBvkkgqzn-70FGwKXepvL8wYtnnyHDCYFYvlw5i5qC7uj29qo_P8UkqWpnVkxBATfogvqFXGl3Sz_QgixsG4XVg5xQS8y_TxVtVE1olUdQ1o2Wczq3q1e1tYvxFUT_8G3f_keX8YaPtFcMUhAc5__t25NLIaqeXesQMCpMsFOIgYP-bXNQZgdWmwL_bmVlbTgkKPr1wP8sKQdhZYimzDaHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d72d98371.mp4?token=K4KoFmKb8h_ucRVLy23H5_qAeYk-GKLzAYLtbSAqCMUP2ft49kweD_7Hx4Q89_3v7orm9DJFgaXB4eRldY7TSABUoHHS2KFQI7fwCOXy-6ciUb_nHiObwGBD8pm11s4wBvkkgqzn-70FGwKXepvL8wYtnnyHDCYFYvlw5i5qC7uj29qo_P8UkqWpnVkxBATfogvqFXGl3Sz_QgixsG4XVg5xQS8y_TxVtVE1olUdQ1o2Wczq3q1e1tYvxFUT_8G3f_keX8YaPtFcMUhAc5__t25NLIaqeXesQMCpMsFOIgYP-bXNQZgdWmwL_bmVlbTgkKPr1wP8sKQdhZYimzDaHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاشو بودیم وقتی تاشو مود نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83253" target="_blank">📅 21:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83252">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAR6NTfhbbdhW1UE6xQPGvt4OUoaCtlVp0QWDFMgxEZgiMNRHZB3SSkVinPp_IauFkgUGdPaGeNI0XiGIz-1CqPYFw7HwFpiJb31db7eQXp0frCyBgJWAh0JZYKDc6yKxaQGsqhtLXOhCtahMFftFNUjH9f9ehe-nvE5ubU6Pk944xP1LpP7IeR7-5oDzxi75EWqELKNgWgWANs-sydCVgNJ4NNOhZjl1lNKk5_qTg0aRtrrVapDvu3Uy8q5XtsFGOZN4pBKAodhTniBB_Xsbb2maTk-7kqUVkh-TqmWleFiCdvRNeyLcgtW3ywwR8wR_iiz1dZ0IYS83i0cjRusFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا این کصخل که اشتباه جمع و تفریق کرده ولی جدای این ۲۶ تا میمونه، یه تورکم بوده گیشنیزارو خورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83252" target="_blank">📅 21:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83251">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPQp9Of5XwJhNasG9PbTdNvGRQ8_A4T30TMX0zMrWBEKfN3rfSga8ZWqWSOogZdfYOTKwFzqzQkNdwsrd92pLQIeV6sn5ymDvK9DH5CHsTSi_l6oN0CSRJVX-s4L0HbofBhUCGkGDOjsETBaFRVd8hUx9a3GBHf8kcDcEchHEvvLOYdUzprOUGP_wXfvDXQGZf48o2N2jDUyhilWglXz8lc_U5kh4KWpSX_ZteH3Q9t1gcScqbJbDZVVJvHbrHlGhXYRYXjUA-iREga0DNdIPZSl0PdNcBoGasle_bi43CdAGCsmuJCg41cvoG-_WuS0s6DVADaUW9w-OtMR6hJ2Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اقا مهراد هیدن که با اعضای گروهش فرق داره و بحثش جداست اومده ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83251" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83249">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hMdLcFwL14KNiSuOE7nD-p6Qc5Zn56PpsvOn41JDhfwHEjSBjhwEpmWzuqpfewztOy-pFA8-AisfQH244etk22F2cqfpCAU4JYXzH9Y9IdML9tDsfdtYpy4PVc2jDRFmlt1_W4-GT5HuApZALhhRRZNxkQi86BpxHdZrgU44wattTAVhCzJG7j-yAuDQVwgVjO5jL3yqVJzdLDleKplLET_tZ16Kwbizorgz4G7FBpxQvCuOju9I5rMbkbKZsdpBOoybh4RntZ0qtSpem5qdn5KjbSVXmpxg-GF-Y_XuQ4rTJq962j-1fX-c-HwQ-g9MyepSOeUXnHRnISahTabAfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aiikRwThpOBTyaoP9qpmfWnTxXwZ1Z_gY18Mf2W5C44bkt_Uzz342B2GVGM-WcDppRrOIqI6VqJKup4-9RWjSIOMM_jBHzOtwgR0VX2WIh4lXXaGnb4smDsv_yMmvvdswgKR6CUdpZQkdRZYseWSsAklQyZPmFBvkYbwKn2OPzP---y6-g8dj5YqFS9-CJHmfhyqHKictUgdWXBm3vZ79nNpz4ZpEye0Trqwn2avAv0NXciw6YdDx_DvE3V709kvIm6EX4avv7SvS3PUdddTnEuJf_d7kIwsrm5MApqjJGz_hYKRBjb9Mvfnioqrmg9aGunEVE44hgbXo73SWDJTyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آدیداس با انیمیشن ماشین ها همکاری کرده و کفش با طرح مک کویین و ماتر داده بیرون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83249" target="_blank">📅 19:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83248">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImVhJwBrO8NcKNyRNBb0wE1psy_jSE6BxwyNbtrizkQ-xNEc7yHz0erVwRFIS7jOuFQ77YLMadilzrj4fXgxdnYOW163z0jvm15QXrkhxwk_hIrR2ZqONWxjMawMd0A94xdfDWKPBSRla0hKeD3_5SXiIfFSdkh9GfDuo6Hbtizdh5lxj5Tn0aBKHCMAxVRpILoQt0Y6QPVtTiqg_6PYV3-PLe1_c5fpxzpHHH4QW5zC5SnW3xKq6bARjY5jm28-JH6k8AnOlpu9iCziaPdt0E8ae3zouUwQtSPWPuSwavazgyP1KUv9weFRoM7xGYceYwYcWycp6wvJU0LrlvA5pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم دیگه بگذره عکس کیر مهدیارم لیک میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83248" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83247">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsF3KayorZ2tB-cgR1xE6dp5YGonruPh10qhAVPoYxjiyWoR3GQdi7--ki8w5ZnhPtlJKR_RI2kXoakuntPH5zsxZFbvp1ZYP0igs3LXk5cicvWPFoKaoMDi0q7SXBlcIAtVHGrrqTQMHUJLDRG_cfA_cop9r3DXD2tsX3hgERfAMm8ByZbFMuXZq472XuEAtFnu4Whxti74GU6mDbzrHoNJUhGHQojaXS5OvHwPWh_zeC7-McYc2cZpGw_AkTuOehHEJSx_xuvwSFRrhDBU27-MVSM0GZkCdeMewXcpPv3cbRxi73pWmc8aDpkUsyWldhfBLcKKUB-3xV_eAIXE_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰٪ بونوس ورزشی برای هر واریز فقط در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
g19
🅰
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83247" target="_blank">📅 19:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83246">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8rp69QKkTxvDwHHUDwa1lRcagaPGFVfPbd7iUMmTLrDbX9Vk4xc06hpQpvXwoYL_WJGfog0fSFR1GipZHlmcDJaiqBheoL8d46hRcdxtWhfId0r267d-KpCTC_w9MFbq2OnZLsWsnbVyblr1LKuiLIuepvCXqZBhO8iplU6WRCy8wx5Z8sXDYQBSvgAZihd9ADoVjt-QyjHbZKPONL9m8oAwAiN7p8L6U5CACFdY7wiClprRAekApbqMjYfUiA7uhGWAKeax_OmNFhB5LQoiwjfrfo9WIvjS4L-d7lHzsBGyBl67Yspa0R_siVrmZSdzUH9xjC_GRz8ZDjtbCvl3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین مهاجم نوکای تاریخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83246" target="_blank">📅 17:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83245">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خلوت کنید آقای خمسه اومده</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83245" target="_blank">📅 17:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83244">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuQnHwhBnUTDFMg8Y1xv93PU-B-xgn6FDtp0JYPbXFUcI7Ug3Z8-3Wz11LDdkRX06rYVM-dyRJzKcXerNoEtJ-pRU7JSThFlIw39sPgYmZMMTKz-aI1qo4T6AkxLyEpXCAxZ6JpkmzXLcpq28zZVkTRrBor9AqCZ0dV7mO3iuxoK7ALH1Qky5tSrUXcDzu5f5rzRxHuUY8NTwlSysimxUSovTCmevq7nxm75iKKH_t-8hOZ6xwNYSV6d7JahqSS_o7O0U5yWqCOi7Y2GwFIEggcEztvj0mdbg4suV-wl-0gguPcaZTctogdyGapPzetj0ZIBwTLKntBfT2M0TW2X6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از عجایب رپفارسی اینه که کسی که به داداش حسین تی ام میشناسنش به سجاد شاهی میگه فید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83244" target="_blank">📅 16:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83240">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=VGhU9Y0XmteUBZwgPWdRZJAlnK5DDMcgqCsbJunvxzgdM2b42DT49DQg4DOTXX-tLH16b_gf5uZigbdLZgVPzAwRH9T7kQ1QaVmSSqcLQUotmdWSh05tlAO6NhS0imsqgF4WpjmAdkcBpGzejJ81cHEnO-QivEFGTsqAKYgXHre73-gS3lsbHa8-vl1OV77gN1mvsCY6aPQmbCboHrrtV5qpbfZL9LEiQ0SAqLSr9qb2QIeYBvxdIl6byEoxuDhzQTtK8_aGonNpTtEHpEEIFdri2SrBvKvjl2gRCnLmojRYItdTdm92yXNmslZEFboEVIGXBCcfs5sDlWLZVZb-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/483fabad8c.mp4?token=VGhU9Y0XmteUBZwgPWdRZJAlnK5DDMcgqCsbJunvxzgdM2b42DT49DQg4DOTXX-tLH16b_gf5uZigbdLZgVPzAwRH9T7kQ1QaVmSSqcLQUotmdWSh05tlAO6NhS0imsqgF4WpjmAdkcBpGzejJ81cHEnO-QivEFGTsqAKYgXHre73-gS3lsbHa8-vl1OV77gN1mvsCY6aPQmbCboHrrtV5qpbfZL9LEiQ0SAqLSr9qb2QIeYBvxdIl6byEoxuDhzQTtK8_aGonNpTtEHpEEIFdri2SrBvKvjl2gRCnLmojRYItdTdm92yXNmslZEFboEVIGXBCcfs5sDlWLZVZb-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: پاکستان و ترکیه تصمیم گرفتند نیروهای خود را به یمن نفرستند</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83240" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83239">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ولی خب طبیعتاً هیچوقت کسی که برا پول میجنگه نمیتونه حریف کسی برا اعتقاد میجنگه بشه، اسرائیلم سر همین جلو اینا دووم اورده و خیلیاشونو نابود کرده، چون اونام اعتقاد خودشونو دارن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83239" target="_blank">📅 14:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83238">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مگه نمیگقتید حوثی ها دارن بگا میرن</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83238" target="_blank">📅 14:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83237">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انصار الله و حوثی های یمن به نیروهای تحت حمایت عربستان و امارات کیر زدن و درحال پیشروی ان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83237" target="_blank">📅 14:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83236">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB-apvuN0GhypUAR4M3trpmaxhhzrEsQZdMjIy0ZcPyvmHhiIWSWJd65Hym2Q96rKgv0fNJCsVFXgQBfVmWr4PRlUZAJRDzqWcrR3y41MYUG0-vfhqgTuJ8x8vG7B5VBvvW74fmSwQ8XnIcdPKW3rLIM1G3eXUavgOn1Zy3f7tvJcm7K9wVc2hf6elHprXCCQ9_X-oVhcBUn9CIxzoAjziFza7WoGHt84DSFc95NunmnUsnWXVUBDai1ks5Q_a6vfCYDwf6vnhkobz9lB56H5ozbg6IHsHy6fAfSWWNikaaVAIXYLPJYn36iK1Z--Rj2KYP5CNakR2tc1gop7OoF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکم نظرم عوض شد ولی همچنان لیلی بهتره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83236" target="_blank">📅 14:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83234">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJDAfuUmu02YLRCpLaeGpAwN9lw3Y99jsl9kaUqt9ttC_NDE6KuBcxc5njJaW0wUnGCJ5SdfF3lBC-DSyxhL46FMGvZMyuJGVaday0JbcDcmPAIgmhcHM1gWBQIcatheFwJ7MNZe1XJGVObBnZ9nn1V42IrQC1sPewV30EGj_-3nxR9bZUR_bktneU3mgw4SQvf5az1G1wHwWdxvIZoM40fRPOVCfS7g1H6wLFTdoLp2vJOAOLZtiW3bSbHKHVGJk3dZ5SX9jv13UBAuLnNoNwJ1jUm32J5A0cTB4Z6momEb7GKsuXn8AsEXCJaR0K6oyUgYRG1Kj22NX2EjLTl2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kScCGGLjnnzwsMdmtWYvc4cP4N9QK-5WnV3yo3YSqjo1rcMP8zXZi7J_4fKevUoxSkB6MdYDHj7a9ts7TRAtGQG9kXA8m7LeqEg0PAUlEww0REVoE170elxlRNvnJINx-cRQscOw_80F4lRb1SzkOqPR4ycWWllF0PCge9y-xwzPPqv8y2zGnEtHGvu_QNAp2jKjwhipzMEH7M4gIbRy2AdoBoi98uaviDaN46CkhzC0ZwBGBaEfTVC_l2FpBmk-8dNuPxdL9feshDNEmBO85WkoH50UG63QuD9uW3Yj8_o66-Vxa8h7YbtjkyGze-m3sGrm5HOwlG2QpYn-PVlFOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">لیلی بازرگان بدون دست و پا اینو میزنه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83234" target="_blank">📅 14:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83233">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">الان لیلی بازرگان میاد توییت میزنه این کار شاهین نجفی رو به شاهزاده اطلاع دادم و منتظرم باهاش برخورد کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83233" target="_blank">📅 13:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83232">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83232" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83228">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmmX9_XYZYpGxKr6RBoccQEGEhCEnwL_avDNVBvjEZjSCKOjqf9VTd0mFmoNZQcLca9Cl450mqoWEfqY6ldic7A_mE9Ui21pmDr5hWpOulmFQETU6Ll2BiohrdbqH1wss5V1leGqAyUuH_xeHLOW6_cahCIrpUHbIdzRlGjbab8OSJGt4pTMgtH558YEA3fuVsfY4v3wvJ5UBxdQrlJo_yzwpdDFQ-E3D0mhbHSYpj_51hu2By4WsiuR0WQkdJkz-_7dWmBDDK7GQQzKB3ufDUIlrkJSGN_fUnHHVczO6faqKZxm4GnsUTYZRcNVLa_-xx7MVyZWcHtIiobk0Ex0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uAO0lD-3ows6sqtVodJjSGc8av_Wa0glNYMYINjQuhFAV9GQMxLzKX2nwbexVqixVxD2KI_SZ1imQwfdiIvfwjfg1A5me_6nOjWahhBacChsUYgT6doYahLswvb8oZehfmlZEGOe6YHNik7elLgDQrzO8MU6WkcFNGeoCSJ9yJxCYMXPNwvbK4MhfBtF6QPPxNuBupbiBhzT5m8H-i5Jd3U05j5dKdogeRc5VAmSaL2cpfFgEMu5jV1eNOpaU8F-QOsEbx-O5M9mXcMTHOm6XEZaYRJW58bSqLR32al595fBV_3ruImTKUizW2UiSgeb3QehMJeYxbZrpC6mS9fcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N1CxswJ9YhMFvy6jpHDNR3ypcTeHqgMgZHUfWsHMlXPcDxUjhF0piP0gCzouox1wRxHZiAeaWFwMfCYpiPBn9w8d5bfjknUK0sYH9IxraIHN5h5aVaddgye6c6IHdhW26X6sekFOO7E5G87le918SdEntqBdePtkwmiOZwzSlI-hw5I2QTWZwZXyvW2SpPtDp9B0zpGMPr3WD1pYJqbnQu7ncdbVQxYBwq2ypkJxrFOe5mkL3uzVgmwhySugfC7lmxdUQ6DHek-EZy-flCpT0w9lyxqlyUiv401iDl764XL5SSlNC8nel2NqrkX4LL3vTmW8gO8zSUONk4Sg__pDRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/scVT4C9tdyh3_0OM0lEA67UW37GZa4AIBBWiOB6VdL6EWKlJivw2pUgKvEzt9FH0FSnR-lPHvS1fBSFbgjk4tTWo9SPpXbMuYBEq3rSgVqnydhNqyqVf3V3PD22tZEcjZpzF7NtynRec0CirZwQ7rGpznSIql5MPkX7vdJb1wTTtvXcgsN2UoH3YNJpsQxsw9mZ02nJGf7qmQb3WPpo0MPbX1LCzO5dGlJCuSSF532Qz005C9lFTgDq1LSQooYY8xONlNhLZpTPTalqy5iTHe40tZt9-bBP9Ago91JzifrsD4DSU3V80p6GXIzG6fFb077IzOTCR6jOojZ4rbcSLgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاهین نجفی هم شوگر ددی شد و با یه دختر نهایتا ۲۰ ساله رفته تو رابطه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83228" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83227">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83227" target="_blank">📅 13:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83226">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تو مشهد ۱۰۰تن مرغ فاسد شده بوده، گفتن حیف نشه بردن سوسیسشون کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83226" target="_blank">📅 12:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83225">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الان دیگه هرکی عقل داره از قبل داشته</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83225" target="_blank">📅 11:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83224">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeCy-W19aD9xGMvco5fQNxiSbUe2O7XR3D8z1QFJp7T7Y3BFzU7FxZArr2xPHSoQc6AeQi1OEvIt_oULI2tP1kZoVB4AB6Q0vGnNUbjeKH7WrBQyptXd938NKl9KIcaghjikCHOCUFG5-WlU1bhiJraD3dLIDmj6HO3oVXqJ05GltMVVB782WY2uu3UPt8t96sxzlLqrRoGymaJ99Y9cT2pM_Y1zgv6KPezKI6qmjGnZ9vYGt1TVQryHWztsWld-M2Ul7Gn3THRlrFPBNU0OzJ2sqWGI_AuuEALS076ChMR_JM3_XXXLwyQBUp_Nf1QMbPSri5ZDO2bQKaq1b7XG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعید جوانمرد، افسر معترض ارتش، به ۸ سال حبس محکوم شد
جوانمرد، اهل الشتر در استان لرستان، پس از حضور در اعتراضات سراسری ۱۴۰۱ از ارتش اخراج شد و در پرونده‌ای مرتبط با فعالیت‌ها و مواضعش به سه سال زندان محکوم شد.
بر اساس این گزارش، جوانمرد که در مرخصی زندان به سر می‌برد، ۱۹ دی ۱۴۰۴ در منزلش بازداشت شد و در پرونده‌ای جدید با اتهام‌های «همکاری با دول متخاصم»، «اخلال در نظم» و «اقدام علیه امنیت ملی» به پنج سال  دیگر حبس محکوم شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83224" target="_blank">📅 11:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83223">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1ZlHoXNIOqdUcSoLih0NDNqayYIszDdRkYsNiurlYkb87_segOuPInwFo21aS-CuuHe8Bcyzr0JvHRYeZ806Qkhm5YTmKnDiFckWrVwB03Mumt54OaxsQeiK_2ouViu_Lnxh5f3_at1AZxgGO01MPqWLU0jluMmMRv3GPrOLihzr8jadmftDvNP525tv8KxhEJtXnZylYuVVP0iWguFbOdvGtGQIgwZbLiuPAoKhFunIwi25EABK1Xyl0_nNwFRTe02alcfI05RrzhHFPyq16YhfZzoCQSVOhNQ8Kx9X66Pf9VLan96L4u4Us_dTxjsZWfnGSbesfmgK1di34od4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا به خدا این کار همه جای دنیا رای خریدن حساب میشه، این آمریکا دیگه زیادی دموکراسی داره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83223" target="_blank">📅 10:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83222">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZhjjQXdc3-7J5S5TjB68_9tAjsn-YJWhP4ZyzT25QsTGakXZQ03HeW5wE_BmDdRLBjEn0J7KT38cIGUzsgtSrIqC-suGmx3eiLiD7LySntl5N8XGuByyJMKckDUFDi81WN3lIMwKbAohmWD_zpZNFzrseNBdPIQCz0s2dtNE8EsEVzPHVkjZ2JrNC5bDSiRU_pqItAmAAgxCai3IONADpXCUfUoc42kuemC0DbwoXnsnIFaUtIguKlwCB9ivh-AN2tnGSS7eDvQEpoOX3nDvBAYIkNIXE5ZmlugZsKKbDMESMDhWMGU4IdHaxogiW_8HRIG8JCKlYk-sAwMd1NU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بونوس ورزشی ویژه برای لیگ قهرمانان اروپا در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
🅰
19r
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83222" target="_blank">📅 10:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83221">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ:
ما شاهد فعالیت‌های مشکوک در کوه کلنگ هستیم، به آنها هشدار می‌دهم دست بردارند وگرنه مجبور به اقدام خواهیم شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83221" target="_blank">📅 10:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83220">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDfnRTthWov6Pdg6aLEH3l9Tihec0N9xCw8cDWplneR7g1wx2mwqvR3zqo4WPq9y4mLWTCtqcYqrPy-PYNXrhc-xI3S5gp9r9P6p7k4I8rh3_1Hp2AsSV9oZHKwrxxq3NYyNkD7tEFdXdyZgZoL9HtQ7wmclU_0vvNILNBWlLg5BIxfRYk0aiQf-tHELCHmrvCCu0KhMr5EfwSA30Z2eQS7bT9RNnMhmSvXx9WcrqATh9y5xwoHcStwAmGnxy05llwDunlTMQLqtoanQuIRTAwIhNKS-UlR2W-WDKEzSwoT_rTuYYi3wipdBDS9VXzdfn9l8udXFR3s9d3s1tk6m_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون متن ریز اون وسط رو من اضافه نکردم، خود عقب مونده‌ش فکر کرده خیلی خنده داره.
ولی به هرحال اینچیزا مهم نیست که، دوباره صبح زیباتون بخیر
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/83220" target="_blank">📅 10:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83219">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=FdNEgi1hC63s8Yu1Bt8H585YwCG7b2Sjw-CEBus5L1fUYzQ4uSCUxKU1iTVTeWEc181r1PBlHsPrNPhtO2uEBrmBtAZhX1IA8xKQBRIEhZiRkDrBgG_icQA-TxSYHdm-RQ_cvZR0pKOyVTKDIqyqtP3UcMnUvr7PCJSc6plyeXNC3OT8H9DDC9Stm-1RCoAfdHTjlWohkGBtq1zx4vpZKoEWgr07NSL2uRA8RGjTJvl5tMtuoo4ZByJ5o96GKfFEth4m0YYbRctRQzqvSFL5wOk0b5lpytM8ZZXLLAKwx1w76eFI-BdS64L4TQ41tRNwuNJFFX6qTJiCaoOV-MRCVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cfeb7c626.mp4?token=FdNEgi1hC63s8Yu1Bt8H585YwCG7b2Sjw-CEBus5L1fUYzQ4uSCUxKU1iTVTeWEc181r1PBlHsPrNPhtO2uEBrmBtAZhX1IA8xKQBRIEhZiRkDrBgG_icQA-TxSYHdm-RQ_cvZR0pKOyVTKDIqyqtP3UcMnUvr7PCJSc6plyeXNC3OT8H9DDC9Stm-1RCoAfdHTjlWohkGBtq1zx4vpZKoEWgr07NSL2uRA8RGjTJvl5tMtuoo4ZByJ5o96GKfFEth4m0YYbRctRQzqvSFL5wOk0b5lpytM8ZZXLLAKwx1w76eFI-BdS64L4TQ41tRNwuNJFFX6qTJiCaoOV-MRCVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکا اعلام کرده فیلم سینمایی نجات خلبان آمریکایی در خاک ایران هم دستور ساختشو صادر کردن و بزودی وارد پرده سینما میشه.
بزودی مردم آمریکا تو سینما:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83219" target="_blank">📅 09:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83218">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=cwHISR7hY1f_EDccUIJ60dc7jTKeYBki7EggwARhPj_l8pJrG8ENLOX-qI9uPcmPrpEsJ9IThEErs1kqy-DxFo_o_8uJXkg5rXjEDwKSVSD3xYu-nIxXdbjRBDGF6cewhNjxgevI2P4zgs1sOotwosZQXZa_tCvcgjbAaZxvlNJN1RlY_F6DwDmtQo8X6955PKz4rMpvLPtn2UUpK2wp8yJEf5FsUlDA_C_Mqox_u4uXmUvrpi8tFvbCmIKLubqjpTZM5HuLPeKo1ArjRNnGegHi2-6ny_5n4zSqzIrWlERf_lfR9hhJqDnZuuoYJ41EN5g-PT7Qb8SAc5NCbNbTXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4fcf7c48.mp4?token=cwHISR7hY1f_EDccUIJ60dc7jTKeYBki7EggwARhPj_l8pJrG8ENLOX-qI9uPcmPrpEsJ9IThEErs1kqy-DxFo_o_8uJXkg5rXjEDwKSVSD3xYu-nIxXdbjRBDGF6cewhNjxgevI2P4zgs1sOotwosZQXZa_tCvcgjbAaZxvlNJN1RlY_F6DwDmtQo8X6955PKz4rMpvLPtn2UUpK2wp8yJEf5FsUlDA_C_Mqox_u4uXmUvrpi8tFvbCmIKLubqjpTZM5HuLPeKo1ArjRNnGegHi2-6ny_5n4zSqzIrWlERf_lfR9hhJqDnZuuoYJ41EN5g-PT7Qb8SAc5NCbNbTXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون با تیک‌تاک فارسی بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83218" target="_blank">📅 08:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83217">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">قرمه سبزی جا افتاده از نظر پسرا و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83217" target="_blank">📅 02:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83216">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">۸ ماه گذشت.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83216" target="_blank">📅 00:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83214">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vasUost0gOVrZeRRiqh29Kdxlh3E_mvRsiz4igJOcfvoV-JSRQ2C4tqDBJsQZGC2SPb8HFXqT9gjvBkEtZT-juL5gB32HHTE7kdQiuIOFOtX2S04ZwcEK-L-TA9KquhHcaJAAJ1hJ_RbfepUZPH0bdPAA9DormDFCRI7Jlx3icz8FRHh3Vkciy_h6Tl_cQ4UqkIYxV_p_lzqEGYqDI691KbozW1EZO7qwWQBxIOtzdqKTN8l3LJ045xHxX2RxNvQ-agDduvDlIBZyLQpPbUqr4TUYHYh5dXkjaOPAn4qVm5obpAncUS8yD5FDyboBmfpNFvmKIA3JNgtm295Y9nTZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfvoAZns9v2m7JcQp-dHjfaNlRrAd-zS1KXaIxhWbhxW_lkBG9RppHwSZFk1WbIq28j9lJoRTzyqCkVmzW3S3ekU24F1JzCLtdjybNS9054DAJgdEl13kpo6uBBHkL8vfmlTdiu-ODMrG6XmivTEu9dMid_RZEy9QO58qB6R-BrTduHlopt3Q4o-SntrMafY7SQxNE3SuBH7QgzcSjScd0frWitz6qs13eSHcJASvL9XXfRVetc3dowgk5wrfpCli1EyofhLTS574PaBdj3_aBNcMMqp1aopba6C9p-Y82QwnRxkGL0X4sNlWLrdKJAiyjoIaOniqRsPV9VX_7XOGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت بت زدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83214" target="_blank">📅 22:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83213">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un4751cBqilTsnMgmaq4JJZoLxfzUzX9kXyQTBYZZuNafiqcoq0GrDF1Y37stHMS2QLrw6Q9AQCNmj2AmcYIZGrHXbLkH0oI94XY2avuxwztdjT0UZx1ujpQMeyuJJo9UdWxSRf1OwpG62U46n2B76PcSN4WXVBbdjoQXJ0tyzVCowNv9S3tKSIgINMpksbAHo1VzuOFdX_3z7is4awIaccIgi6NTwuFbyLF5B_IJRYrAow_s3euoJ_5kYnujeSSYWU0tEMXGYDiOq_gNh2WMA8RZQLnivlwq9iNkKI-hBT5oL6Ro2DCXOubzXUhNXMMJxW7zvDRVG7WBSkKQqgGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احساس میکنم بارسا منظوری داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83213" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83212">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDYZYfZhfb_TFbsrNd3-yrq0mooxQm3xudEtFoV6IIXdJT5Dy_CftiD47BX8ovO7XZ1-hVqWuiGTJ8u_Y0NBjbh3uOeoPTUwxexXIpACoUo4j60XGHKShOjkRLdneh59xBw0ODBfNYQ5vdQJc_5dNTsAx580c9hqezXZsImaZDNg2PLhRfa6nnYOXeTZPU4Xe2UjSbpxuvFxQZj6pZDGJ_DCy2DUjMVEnd-gxxo3nbFOR7C5NNga_uo8-H_lQx_MGgLNgoPLKN5R1UKCS27mzc9NbsD7F8em0FlZMQSJiR87hQGicL7D4qU4YoU3R5uSLkGbd3aaRTBg-mkbu56Iog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظ
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83212" target="_blank">📅 20:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83211">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کریم سوسکه چی موشکی ول داد</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83211" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83210">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">میثاقی وقتی خداداد تو پخش زنده از کلمه های "کصخل و کصکش" استفاده میکرد میخندید، الان اومده میگه کار خداداد زشت بود نباید فحش میداد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83210" target="_blank">📅 19:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83209">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=k5SMuQZqckjDxbJqcUbarPIhqqgiqwCTkEbtQu2yABrRhsRjDHsnM-zDWiEtrRELQ8lqcapsmKCrHeeIjNVyGgnJD491OBCShzmFNkQHkTxcIFoLfEiCzMJ7Xz2A_lxHqydbJoHoxQflfW9-q7x4jBv6l_tWlqmmaVWDi-wrVulZLho9YPFikUTW3Zb8q9IB_83Wswou8k8Re9MoDCUaTVhQ1hoi5xIayKgZI2E-F8z299P99HTn3QEKocAusaJfn6_lNTD24wbnq555XtgaVCOo72ODxtP1fksbR4z8tY7DSS_qE1HRjyfT1EiVgmEN7LPktRSIkOn9JZkBN8evrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab1a52ccfb.mp4?token=k5SMuQZqckjDxbJqcUbarPIhqqgiqwCTkEbtQu2yABrRhsRjDHsnM-zDWiEtrRELQ8lqcapsmKCrHeeIjNVyGgnJD491OBCShzmFNkQHkTxcIFoLfEiCzMJ7Xz2A_lxHqydbJoHoxQflfW9-q7x4jBv6l_tWlqmmaVWDi-wrVulZLho9YPFikUTW3Zb8q9IB_83Wswou8k8Re9MoDCUaTVhQ1hoi5xIayKgZI2E-F8z299P99HTn3QEKocAusaJfn6_lNTD24wbnq555XtgaVCOo72ODxtP1fksbR4z8tY7DSS_qE1HRjyfT1EiVgmEN7LPktRSIkOn9JZkBN8evrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبلیغ سیدنی سوئینی برا یه سایت شرط‌بندی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83209" target="_blank">📅 19:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=onO_Qoel26U5RrBUu8P94wjQgE4YXwYsgkQMsUPisjaC-hgGeDx7rdzEeazLyATo_XxhIuT5NMZy6letMcpeNhQM8LTt4Q9p_NxooJ583LIZv-Yhz0DDpfK1oAlrp6zM7fzcv0q0E4LZ6ytJU0zbj47DtdXKZStEidWkUV_aQbYTVEnoT97xlW0CYvzuyAptB3OiQng84PskOX-F2c2JdAEMTznRKHh1FZaZHOBkloyA9cpCdtELDbjoVbrErV-9YhP3crxpvL7bvuKfprlV0kI1u7FT4cA3iilWet3wPDTfbCq6FduLHnDjrU3ZjdNnJrUznOcJP4dSWDGagWxjSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc63a398d.mp4?token=onO_Qoel26U5RrBUu8P94wjQgE4YXwYsgkQMsUPisjaC-hgGeDx7rdzEeazLyATo_XxhIuT5NMZy6letMcpeNhQM8LTt4Q9p_NxooJ583LIZv-Yhz0DDpfK1oAlrp6zM7fzcv0q0E4LZ6ytJU0zbj47DtdXKZStEidWkUV_aQbYTVEnoT97xlW0CYvzuyAptB3OiQng84PskOX-F2c2JdAEMTznRKHh1FZaZHOBkloyA9cpCdtELDbjoVbrErV-9YhP3crxpvL7bvuKfprlV0kI1u7FT4cA3iilWet3wPDTfbCq6FduLHnDjrU3ZjdNnJrUznOcJP4dSWDGagWxjSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83208" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlkzOI-tiRSaoxU5KjWOCpksfVD8m_al8N6Axj_HZsLogypToVHWkm50xW2RLJQHvEDG2uiYuO4BZyyOhOxR4xuxqbNlFAJCmftKE-81wdUgZyuLtpFq4ZRswD7YGs8K8nTxJ-athhlmPKA1W7dmr3mbkY9SXJRi1WBBmjgUuAUlsfsUVSMKnEz_ZxPOnoZq7-FZbidHbxYF1GTq8yyt2Wrrf7yPQtZ-7RJ-gGO3hDvkNzkrkQfhj1OjzfIevuZUnDdBtgedaaRg81Q6vXKNB4UQCaoBYW17zmjj0m1y3qxM3BevBRyfdjA3o3uIoclkyJnr3C4AtMSg3iImjuQUSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بونوس ورزشی ویژه برای لیگ قهرمانان اروپا در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
🅰
18g
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83207" target="_blank">📅 19:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ7MujObMMc-W1qRnHtvqwtc4b5w7a9pGQZfLdqBLgLC8-aly74_WXwwH6-vVNI4rUz0okuxRRABq0Z1d8lEavKcS8Wr4UrTMGWI4HKf9V-nexxj4x2rKN2p-cO8KY2OzqxKgPDOgqIG8Tlw5PDalHgaHbmtmkSMmINg6pDpO1LX3gAxVDii2S_zkEAkUu5_ZYXhGiuLU_Gqkusx1ECvoIrv5YuQET_sAoNgmDvW0jQ7yXFNf49V9ge0uyl6peyKz2JcOsIBU_Rwz2dcl_TB2XrCJFD_PE7KnuQEmMRnitpL1jp3ji30GDXut-LsaCH3sWJ7tyLEd2RoBZ-MeUOO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درصورت هرگونه تحقیق، بنده‌ی حقیر به هیچ عنوان هیچگونه ارتباطی با عوامل این کانال و به خصوص این محتوا نداشته و ندارم و به صورت اجباری و تصادفی و به دلیل کمبود محتوا، در این کانال ادمین شده و دست به انتشار غیرعمدی و ناگهانی این توییت زده‌ام.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83206" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83205">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مثکه پاکستان میخواد پیمان مکه رو فعال کنه و حوثیا رو بزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83205" target="_blank">📅 18:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83204">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mip78tcBqCcHBCZEWCtthOrDHn1o7ZqQvdnXdU1RH6dYGU7pHV21OI1Ng5hM4it-_MMMQcQF7yQ0iFN7yEjv9uWPyI6D-L2l0uQk2bah32OVg9GLDMmqM8uT4St30UTxZ1BJN6BtMxT6vkrTCLARrZ-b73iWVYlax21tcxhHSb087BwX0KHYdckVithh8N9eN5R3vPhQYQLmyISHonij-WSV-sZ0lceIGca0ilqBKF7WZBNrV46NrpIGls3Iv9pmxiLBowI-my_h_NR73QXSERD_XCB01KhU49ZoVPZe60E0xUaZEC-HZyLI-rIwRbE87ScfACmLeD6M3QQMOmSrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به این حرکتا، همینکه تاحالا اتم نخوردیم یعنی هر جور حساب کنی خیلی تو سودیم پسر.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83204" target="_blank">📅 17:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83203">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565302292d.mp4?token=S2WMVYa_vl3tPZbF_YcYBoepbBjhfxckgoE6VLH5AxcHKjG_IY5EObaz0T5j_lxU8_yHzrMrx1ROb9t0LA9oGJWDpOSs2kz5x0IQnFLFAwkGtG0HcbPsA9rrgq9q9ewjsVtpSg8FV1GAzxGEeNlNiwhDSwoCpVmT39FEmbJnEyXLXe04v7WisDGG8mRz-LCbG0HCh0xiOrcC3V7HnNut9HP1mQaQ8ga75NS_WzVTq-_NjR1Mg0KdVsWJh6V25_FWPAYN-QupQANUQI5GhrqBPotjQVosNU2oH7riaKzqrnju_k29VEyacKWy6VhLB3wu2t6qBEMpzY7h2g_Z708RQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565302292d.mp4?token=S2WMVYa_vl3tPZbF_YcYBoepbBjhfxckgoE6VLH5AxcHKjG_IY5EObaz0T5j_lxU8_yHzrMrx1ROb9t0LA9oGJWDpOSs2kz5x0IQnFLFAwkGtG0HcbPsA9rrgq9q9ewjsVtpSg8FV1GAzxGEeNlNiwhDSwoCpVmT39FEmbJnEyXLXe04v7WisDGG8mRz-LCbG0HCh0xiOrcC3V7HnNut9HP1mQaQ8ga75NS_WzVTq-_NjR1Mg0KdVsWJh6V25_FWPAYN-QupQANUQI5GhrqBPotjQVosNU2oH7riaKzqrnju_k29VEyacKWy6VhLB3wu2t6qBEMpzY7h2g_Z708RQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فان‌هیپ‌هاپ در گذر زمان:
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83203" target="_blank">📅 17:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83202">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ارم نیوز: آمریکا در حال بررسی حضور تفنگداران دریایی خود در برخی جزایر خالی از سکنه ایران در اطراف تنگه هرمز است
در صورت اجرای این طرح، جنگنده‌های اف‌ـ۳۵بی مستقر در ناو تریپولی وظیفه پشتیبانی هوایی از تفنگداران را بر عهده خواهند داشت.
هدف این طرح، ایجاد نقاط دیده‌بانی و پایگاه‌های لجستیکی برای نظارت بر تنگه و حفاظت از کشتی‌های تجاری عنوان شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83202" target="_blank">📅 17:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83201">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=fazP5sox8Q3MyjG5rALz7k-rkBlU0I2uYMyAkXmMp_DfjaQ38wl-gEVzwW-aN638J4KRoc3jlfijrL1nu44Vn8zpELOL_Nau6Bozwd-vkj1QqUG4q-2cAQlFJ8O__ay6qgZMcLrHQ1DkweUKf7oYR7T-wndlgSeerfZL0jsm_Si7GLL2GeM5LAdlMsKxigEoPSu-XkQodh7tqy6gsvozRUyfE4wdfSbbfGmFYNfSZH7xs78v70kJQIK7yNgOByHaeJIrgSLJyMytOiSeQ6FmUOSCQEiKMUDm577z_pTx6PxoNh5UbIWqex1Bl3DTfaJdnQfv2gdmKOZ2aH5J3flq3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f275b2369.mp4?token=fazP5sox8Q3MyjG5rALz7k-rkBlU0I2uYMyAkXmMp_DfjaQ38wl-gEVzwW-aN638J4KRoc3jlfijrL1nu44Vn8zpELOL_Nau6Bozwd-vkj1QqUG4q-2cAQlFJ8O__ay6qgZMcLrHQ1DkweUKf7oYR7T-wndlgSeerfZL0jsm_Si7GLL2GeM5LAdlMsKxigEoPSu-XkQodh7tqy6gsvozRUyfE4wdfSbbfGmFYNfSZH7xs78v70kJQIK7yNgOByHaeJIrgSLJyMytOiSeQ6FmUOSCQEiKMUDm577z_pTx6PxoNh5UbIWqex1Bl3DTfaJdnQfv2gdmKOZ2aH5J3flq3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه ویدیو دیگه از عملکرد قوی سامانه پدافندی پاتریوت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/83201" target="_blank">📅 17:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83200">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_or6uTArdT2pYm-XKwNrdax8lBSI5XSqNYvDhBZgq-OWmJLPgefojNaW397O0mZphMBNQjMdUKdJA9sxWn-EHdIJ2OSKtGedcP8dk27rqigfcjN-tsFy5T1CpgUJdYmR0VgV0SpO_IT-PcP25elNEczIOSfzPDn6f_GFs33iDj28TPOIy12nlz-0jZYUsHBM7V9rHjGWw0b8MMiNbzRrUnG_TFRxOwnkkHHL-zQmHj1x5-jmUPjxKGevIS7tWSYZYjqpuGzuq8_7Hr1BHlUZdlGHhwN59JJV1MOWs4vx_SUmLGRsG8LRzcNnIE4n9qcxM2d4BLhYI3kNg2AmeQbuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جواد محجوب ۲۵ مهر ماه قراره با لویی سادرلند فایت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83200" target="_blank">📅 16:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83199">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83199" target="_blank">📅 16:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83197">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7_puVMGtb0yDQWwZHvi8EaJCa_b7sHcNQ0pHw-hYroZdcbI88-LMOlK54uAQzJVHkRFZg3_dZmTxpsOg_bMpvvZC4u9No94Qp56PikTjryY5930BdRjAEzX-6P3hTx5nYjVi6XJ3lv8YVg10MrWj6rbtz-q3hn-0t79f4RuaZBKdjF4hsAdCngzm2erpdkwzEaJeCwAZicjNWZMyECmEuV6dQ3_ufBDOaOvk-NDpUBaeCnmlwwKukp-cVwk4Q2lgbotRcOmAo_JE4wqfsqnDhHd1hr7gFL5rpdqWhFheMaRvU1saAIbgrDj3PNP84Pxd8MR9OUHTKtsLAN-HClCBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد به اسم Sweet one منتشر شد
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83197" target="_blank">📅 16:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83196">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoJdOQYJHnYB-xSVHjktBlH-4Ry4FeWXUPcFNYjAQjUnQYRin5Njt3zxGiPrv1wjlOmif21Vg0FurVOgD-0YH9zLjsBG9C2sQo3SZAneG3SlRwc3pytQ2S-9pSaH8j_LZHFsYGKieMFy3xlGdSEWQgDYxCbdzLCWaElEuOiITTdXm3pMuxvpC7D6jnR3I9nChQ_raunzp6GThVly-AK9gwoZHgy4iQ2nnkcrJSmqpx20_SPH069CFrTvaeCxzj8Ptl3ajo__LFIb3rwAeTtFwLD63PZOTniGWkses7HMhAwHyxr9052NePyNYqkueAg1RZpfKS-RTRyPCQf0dJuRNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83196" target="_blank">📅 16:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83195">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_x-0bf81v2ZqDGI5yHfpuO7xUrAtONE4FqB4bQsWrJxrzVvOv9nhpeSjd59l06PO39GfQta8rfE-EUiGkjnOvMOIKqOyRTlLLuTukaNGMwWj2jAGt815CX7sc9Bn4kq6hObjjNsLthe49XZ2gFQ4l_s-S5GqrBGnXjn2D9lX1foEiM_375hVx6g63gAT14SruC67wA4O1cIh_bcqal6OeRM8y0xQyQsnf-Gi514--7hZfjYOZBc-jZrbf6KG5xYl1y_lzkSYDC2vWmOPg91REpjYJjIRk5-lkqzuclmRfBMxtPPNKDv5rKKIf-l4SXTyik8tabyVwsmjAraX-p8iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رنگ های احتمالی آیفون ۱۸ که میتونید با حقوق ۳ روزتون بخرید اگه قاچاقچی اعضای بدن باشید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83195" target="_blank">📅 15:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83194">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4yYUlG25D9fv58KzPtbC2sd5LvSjBiMZE3MywWgGyFghu8lIGrIu0U-JLexmDygcwHyRM8i33QaQC2CNts3W9JGxyfg8573HP1w3W6sGSsD6tA_T7tHtZYIi_mTJ7UPQDWqM6Kg_ifHTRP8jzreorq2QpjdhIr5Sr1HaDWokCVnaE2f5gA6m5G9bmX8SGld7seOwKAaKKpPp6gwLusvWdXQQ4J069fnUUwgmJAUIDROaACGnFpRE0L4EiyDTw3IVWeR9JkgIsytiqLvKKytarPsJbanGq4xo59DLxWwumT45GwU_kRvKXMW4y690S-m4NRcaLtydx6nFOIqvH7blQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی وقتی دلار ی میلیارد و هفتصد و بیست میلیون تومن بود.
(اینو چند سال بعد بخونید)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83194" target="_blank">📅 15:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83193">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=jKIqTdeRvq3j1AgD9PDftMWb2-UF-Xg6fhGYrIr1EeFu9tgQmCvOXyD-UUkGOYNYB0b-mpIxYujeh73HDOTmrn6EeQbIOF3cDhvfYJT1Jzlr3ZgJgsytHMfEJtSfOjKZfgBKrHJg0SM6HcwyD4CB2feZeHlijeQXFnKHZjqgZEh4vb-TDpNU8gVMokOpc8KfK1-QaFdwbNtbWH_eNTKptIgW9ztr3Vs-wTcwbLQpAnNXILF6tvG77gcThcw8SCBW7FvayDexvfhNsPg363daHVVvP1SA03o7uzczSpPILXGNLb0wLyKq17IzJ5k0aQsgpMsQOqF8D2kE1dtO0w_XVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1bc2eba11.mp4?token=jKIqTdeRvq3j1AgD9PDftMWb2-UF-Xg6fhGYrIr1EeFu9tgQmCvOXyD-UUkGOYNYB0b-mpIxYujeh73HDOTmrn6EeQbIOF3cDhvfYJT1Jzlr3ZgJgsytHMfEJtSfOjKZfgBKrHJg0SM6HcwyD4CB2feZeHlijeQXFnKHZjqgZEh4vb-TDpNU8gVMokOpc8KfK1-QaFdwbNtbWH_eNTKptIgW9ztr3Vs-wTcwbLQpAnNXILF6tvG77gcThcw8SCBW7FvayDexvfhNsPg363daHVVvP1SA03o7uzczSpPILXGNLb0wLyKq17IzJ5k0aQsgpMsQOqF8D2kE1dtO0w_XVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس دانشگاه سمنان درمورد اتفاقات چند روز پیش و تعرض به یه دختر ایرانی توسط دانشجویان عراقی:
از همه دانشجویان عراقی‌ای که هیچ کار بدی نکرده بودن و یه دروغ بزرگ براشون بافتن عذر می‌خوام که چند تا دانشجو ایرانی که حالت طبیعی نداشتن سمت خوابگاهشون هجوم بردن، ما دستگیرشون کردیم و کاری کردیم که اعتراف کنن به کار بدی که کردن شما خیالتون راحت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83193" target="_blank">📅 14:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83192">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ما تو خیابون کسی با استایل دهه هشتاد میلادی ببینیم مسخره اش میکنیم، بعد شما میرید عکساتونو میدید هوش مصنوعی اون شکلی بکنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83192" target="_blank">📅 14:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83191">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">کیا مثل من نمی‌تونن تا شب صبر کنن تا مشخصات و قیمت گوشی آینده‌شون رو ببینن و پیش خرید کنن.
😍
بیاید بهتون قیمت و مشخصات احتمالی رو بدم تا از همین الان آماده باشید.
😉
این رو برای سیسی‌های ارزون هم که دنبال آیفون ۱۸ معمولی هستن بگم که آیفون ۱۸ عادی فعلا تا بهمن…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83191" target="_blank">📅 14:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83190">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDw5l0TsRHYs2DncfZJbjX6ozyzv6f-_M8H_rE4vZGuX7XihjwRMCjBwugFkg5BlQo16vorPkwoS9Xg9ybp1nPw2dDCzKAeOY60eHS5m-KKNUWU9s0av5mbps621I4PdwS71vY67N2fTSSWWkHXQ2mJOBW4UT1AH18gcYNXhxndZ6GomMyjct8UjroqXmh_oJ7AX1ksqHLWhBvSzSWm1ue2FKhqdRl7r57kpcL43jBRWORH0tpZgQYw7nBYwCpAEqq8q8ttfWmvbWRvEANQVPqtgfjM9Xui9r63UxZR2vQCHkZeDavDYekqw4xQOfbHUbkDJnMVZTpFNR_Okgj9sag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگرای ایرانی آماده باشید که عقب نمونید امشب از آیفون ۱۸ رونمایی میشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83190" target="_blank">📅 13:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83189">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">حاجی من از آیفون ۱۳ به بعد دیگه باورم نشد</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83189" target="_blank">📅 12:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83188">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دلار ۲۳۱
درهم ۶۳
طلا گرمی ۲۴
خدایی این وضعیت برای کشوری که میانگین آیکیو جهانیش تو رتبه چهارمه اصلا قابل قبول نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83188" target="_blank">📅 12:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83187">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">روبیو وزیر امورخارجه آمریکا:
از این پس هربار ایران تلاش کند به ناوگان امریکایی آسیب برساند چه موفق باشد چه ناموفق، تعدادی از ناوگان نفتکش‌های خود را از دست می‌دهد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83187" target="_blank">📅 11:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83186">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=gNJrr5-WLmnlXGbIsiBLvZMXrPRN55-nsrJUAwCt1S6omiuY8a3XP2tm6YpXDSpecSSbfOke9YwG6dCCiEW2f5fXX1WlL0psUxC27B4KemumefBvnq6O27-vCdcnEXOi4Cbyt6Cq0bCxyGs1UE2Td2hpAcP01e0_ZfWFwj1n2pLQPC_34jwRqPUwKlfrTBxsokKfAHTZeAthhqg6QyGW4jiVakOiVJStEjt4KWRbojLbYj76EHbLqr2qbRGbJk1V0fO1MRkYVJoPugyOiL6NKRLKRmUGa5ZXak7rl_BHjhuq4rYis_9f2J_QZ4Lm7BAfCYydZUdt8RG_SdwpIys04g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7f64e8a43.mp4?token=gNJrr5-WLmnlXGbIsiBLvZMXrPRN55-nsrJUAwCt1S6omiuY8a3XP2tm6YpXDSpecSSbfOke9YwG6dCCiEW2f5fXX1WlL0psUxC27B4KemumefBvnq6O27-vCdcnEXOi4Cbyt6Cq0bCxyGs1UE2Td2hpAcP01e0_ZfWFwj1n2pLQPC_34jwRqPUwKlfrTBxsokKfAHTZeAthhqg6QyGW4jiVakOiVJStEjt4KWRbojLbYj76EHbLqr2qbRGbJk1V0fO1MRkYVJoPugyOiL6NKRLKRmUGa5ZXak7rl_BHjhuq4rYis_9f2J_QZ4Lm7BAfCYydZUdt8RG_SdwpIys04g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83186" target="_blank">📅 11:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83185">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دالر ۲۳۰
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83185" target="_blank">📅 10:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83184">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX1nI23ouj9WZuCyJyRvjRONSsB1b_Tm34uXGF-TdyPIVGBKlcX0ffD8wS4X2sjrsAMEqteVkMDCCKmlWmYmdXuqYOUVcGsk3mKrZv5pGbLRRIxNn3E0AWbLP-mwC3KBvoivMtgXkgV6PrmyPHPFq8BTrNuEI5VMSmNTPDC_saFG2bpAQWGXY5VWyoSof0xFMFd0H54YD4nrU4Uh0R2_MpbIIeZbiYrV5jHhXj2SWFwrxZKEYzlWtfwi4LiIiT-5DL_G657N2Sk7yP1a_4xLCbGGhhBP0GYOxUXutpPiOurXw-W5jIe6TtN44EYV6ohlLwf_BL_IB8T0YjCmuoXNEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاگرای ایرانی آماده باشید که عقب نمونید امشب از آیفون ۱۸ رونمایی میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83184" target="_blank">📅 10:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83183">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b7d8831e3.mp4?token=ZxT7BxIrLf4T6RVw8XKEcqDXsFXlT4m2fq3Wxj4CRxc5awfHA8t51bfC9qvxO-b9UM7xb06i66nSu8Yc6BBvXtPqCpJMgZx-HMVYkqhyUclmYZtl-VAzzNgrIykBUpLBOTof3xGlTFUeI5OarabfLbNlpJv6lYzmwXWnEpQ0tpiCmrzqp78jtVN818orULv9GDyGt1rIuSln201e5vcoKyHcM042URMuqN4LqO6xJFmazc64ULZeIBV-46vaBTR6C0exnhePqdte3IjdHcivQVPH-i6YIrgtPvqulg0VlJ4LZoBBA65T1sVI2hYdrn8iCC7h62QC7ikzFXGXZbSHAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b7d8831e3.mp4?token=ZxT7BxIrLf4T6RVw8XKEcqDXsFXlT4m2fq3Wxj4CRxc5awfHA8t51bfC9qvxO-b9UM7xb06i66nSu8Yc6BBvXtPqCpJMgZx-HMVYkqhyUclmYZtl-VAzzNgrIykBUpLBOTof3xGlTFUeI5OarabfLbNlpJv6lYzmwXWnEpQ0tpiCmrzqp78jtVN818orULv9GDyGt1rIuSln201e5vcoKyHcM042URMuqN4LqO6xJFmazc64ULZeIBV-46vaBTR6C0exnhePqdte3IjdHcivQVPH-i6YIrgtPvqulg0VlJ4LZoBBA65T1sVI2hYdrn8iCC7h62QC7ikzFXGXZbSHAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب سپاه بزرگترین حمله موشکی اش بعد از ۱۷ فروردین انجام داده، این وسط هم پدافند پاتریوت آمریکایی اینجوری داشته موشک رهگیری میکرده در صورتی که اوکراین بدبخت بخاطر جنگ آمریکا با ایران دیگه ازش بی نصیبه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83183" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83182">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83182" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83182" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83181">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLXx1PuqwuzvxZMwNc3WQhBpxuZKpk7AAUm-wGFnN1SlqbarZopfcrQElOdgDyZpuU4PSSE2LMrq7S3QIeRox4vBlMv-nbqUbXSOoMT3aoqL1XWP7YTNegi1Z2APuj5GvXlC3CPDtFK7lbpwQ-q76DmEmV1RTU4VJxxhnGhd4XHKo7Q7mkW01Idk0iAcs0df0sxdHTI8yKknC5jHUW-89CRdnKG2WDWm4AIBBl3W47BTEKFmJRflsYZz5C_OOnZyUFT5CL895sqgU2ZBnhBrlPccj8PNcNI0PSbA7ZMCxHlbneVXzsTEL179FcJQNy7Fp5X6anuFVwgZptKyL0WL4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r18
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83181" target="_blank">📅 09:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83178">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdnlRQ2z8bY9RPp0xHNx_-dmrT_4VMdYdZe5BSx73bbDUxiTo0J-OYlvc0yHicOCfoh0RY5GwvKfeBdGn2MaDkRxLCBx6IUf7Jocaet_HUAVmMrO1yM7lp5XSM00p7SCrlbrFDZZHPEtUn1ExJ15fdNdsTBeAL0lbOAkKTGHsAEFDUZJNL5iz2Q9mmBA0oXtA-cWWw7RRPddv-8luri-h_htwhtjvl_7ogFycuAOxeyNCqMgLfFEJX8xOALcUUaq8UolcVjOoMIpeHZK-eid64egZcdirteBqMFela9gAZObNNGK5tipCaT-k7cyhk7rL1vFXJ2iFq8-PlGjd1vmyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیر تو جنگ بابا جنیفرلوپز ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83178" target="_blank">📅 02:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83177">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یکی از این موشکایی که میزنن اردن کسخل شه بره بخوره اسرائیل بخندیم</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83177" target="_blank">📅 01:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83176">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آمریکایی‌ها مثل نقل و نبات دارن پاتریوت شلیک می‌کنن
به زلنسکی که میرسه میگن نداریم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83176" target="_blank">📅 01:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83175">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">من حقیقتا دیگه بکیرمم نیست چی میشه، ما که بگا رفتیم چه کمتر چه بیشتر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/83175" target="_blank">📅 01:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83174">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">۵ تا نفتکش ایران رو تو جزیره خارگ و جاسک زده آمریکا.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/83174" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83173">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">۵ تا نفتکش ایران رو تو جزیره خارگ و جاسک زده آمریکا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83173" target="_blank">📅 01:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83172">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جمهوری اسلامی هرچی داره تلاششو میکنه قبل انتخابات آمریکا جنگ شروع بشه و هی حمله میکنه آمریکا هیچ اهمیتی به حملات نمیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/83172" target="_blank">📅 01:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83171">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pekrEHrQrbSZfjJdHYOOojeQQuOV-DI3pzEazu9zGzuJOr1MvjtdGmwFajCMF9L9tM_MYFH9ilz2zTJMafVpDkh5nNkG4SXypyXaKmtvQCOs1kmFR3vevMjw16ZIie41ggeSHUib7VnunItXMHkSl-w6r5OTrx2TWCFKnjAwsqJEGOWdEfeQ73KkBHYucOmRk8tx-sc4WryFwkDae1p-SCDm1fTLSmvS1Gl8cDCBNqPgfMrZvCh2I1mM5wv3BhgcQegjv50lKsEPh7y7p-djA3qIyGNjgiB5JuWW6fYhz8pjR-6MD0AHJJsA_6jEhnxn6TB0pKf67nDMFMuCOOCZew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منیره جان افتاده دنبال کون مردم از کل تهران فیلم گرفته، اگه قوانین کشور درست بود الان باید دادگاهی میشد بخاطر همین فیلما.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83171" target="_blank">📅 00:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83170">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار فرم های امروز:
🟢
2.675
🟢
2.104
🟢
1.696
🟢
1.77
🟢
3
🟢
2
🟢
1.26
🟢
1.56
🔄
1.9
🔴
1.62
🟢
1.616
🟢
1.416
🟢
1.4
🟢
2.4
🔴
8
🔴
1.5
🔴
1.3
🔴
1.6
🟢
6.7
🟢
1.856
🟢
1.57
🟢
1.74
🟢
1.495
🟢
1.28
🟢
1.2
🔴
1.52
🔴
1.736
🟢
1.925
🔴
4
🟢
1.43
🟢
1.89
🟢
2.485
۲۲ وین
۸ لوز(۲ تاش کاملا ریسکی بود)
یدونه برگشت
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83170" target="_blank">📅 00:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83169">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isveI28NaMUxRwGIG5Fd2x7gc4S45OGm_U0y6e32cobyl3LWK6-XVMvre8Qi-n_nKQhFPuhII4bUg3QyAzu_SpAf1IQoYRTlqzCa1yI5Q-EpLxZmXNkcVTAEK-n3py4e0Pi-s6Bg7Q-Cklx5d_peddHwHB0HjKq-OlLSwerQCMeBDG_15VJKDWMfedO1FoCnk0e4dfSolGm_uj6cW685zUV33rSFjxkWtVw0_CXK_s3KAkhiEsINR6rLYKM3reSjYgQwWbPwKHo-fJHKACA6wb-LDXFqvKP-_ayVW-9_pMQ9-v72zBgs2j2pRmw_BuDCmJJojELrcOXSVbuc7w8yKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایزی وین ترین فرم زندگیم</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83169" target="_blank">📅 00:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83168">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">از کی تاحالا پرس از بالای سنگین و استفاده از اشتباهات حریف شده حرامبال</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83168" target="_blank">📅 23:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83167">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وقتی آرسنال حرامبال بازی میکنه ریده تو فوتبال
وقتی رئال حرامبال بازی میکنه میشه کشنده، سریع و فرصت‌طلب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/83167" target="_blank">📅 23:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83166">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">من بشخصه فن هال سیتی ام، چون مالکش تورکه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83166" target="_blank">📅 22:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83165">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">واقعا فنای فوتبال عقب مونده ان، مخصوصا فنای بارسا و رئال، یکیشون جودیو مسخره میکنه که تو ۲۳ سالگی جزو بهترین هافبک شماره ده های جهانه، اون یکی پدری رو مسخره میکنه که تو ۲۳ سالگی بهترین هافبک ۸ جهانه، تهشم این دوتا که هیچ وجه اشتراکی ندارن رو مقایسه میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/83165" target="_blank">📅 22:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83164">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb4wtxuJ99C2-4Q38MhDMutmuWd09_EhmVfMkGO7mU1IOE7g_YsQKF0jVFne0rwO3SdGVrpy2SE65VMn7zW8VYNHmT2hcvrjEm4ob3UyNHSnb9_ysXZ7Lb9gKcFwqyv3ElmsJxmRjPu9xykkafUidiMUi4ar9arjT53Ixvbp9PRsCoRacHUFR0tdTXhf_jRjyHDGjUmpdU16NBSn6tbSFXMqhIlq4zd8Vpa1PRVMQFyeHRuMGn59cys1yJRKri_YPOEuHLnebu_I4v98TLilgjiPPAJYZdNaOt_TjzMdKbjtm8x6EGOo3e8RyE5fS89csc4E1xx4ZlirUCFRb3SeEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من فکر کردم بخاطر بارونه داشتم به خدا فحش میدادم، نگو باید به ارمنستان فحش میدادم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/83164" target="_blank">📅 21:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83162">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">به گفته بسنت ایران رسما از فردا ساعت ۳:۳۰ صبح محاصره هوایی میشه و دیگه هیچ کشوری حق نداره با شرکت های هواپیماییش کار کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/83162" target="_blank">📅 21:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83161">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کم کم داریم به فصل شاهکار هودی نزدیک میشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83161" target="_blank">📅 20:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83159">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کم کم از ارتشی که قاسم سلیمانی تو خاورمیانه ساخته بود داره یه خاطره میمونه، همرو زدن</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83159" target="_blank">📅 20:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83158">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWzmoQouQ7ZUFDmzB8FEzksW2-l6kFJJZTzcVoXffCVPGAtjrT5l2BgC15LLlUArnKUiIN2AgfuM4qzZSYIeZvotGwllCAvpOqiJ2hpu4269y2VwWlqmjeNIKcVY0cOThxo80-lU-4kEwQpIs1OyzrXbT7_5lGEpU2Eoj3BUtSOZStbJ6gy086vmFkRoP_B2gicCXOy1Yyww4jSNZUXGQYXW-W4AUH822o3xc-zxub7RP2ceM0CHiAewHYViMmtw2DG0wVF_dxb3njyUkwe1lcvMU6b6S8gNmQWzYpGKXvap50eHr2I1VuM8H2xxoRsKl6bsP9buG_I1NeyWL3G3yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بین نتانیاهو نزدیک انتخابات اسرائیل و محسن رضایی نزدیک انتخابات ایران تفاوت خاصی نمی‌بینم حقیقتا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/83158" target="_blank">📅 20:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83157">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCEO15D5LFTJ5ABPYv7keO7XgPZ-QVHKoh74EpUM1d5P7YD-A0AnEdDT5eL8r5DclX5gt90SsEl_FxEe6CAhCl8ASi6dlIEVjrD9zltXBjjaj-PTUGn01tQ76TDe2igq8GuoCC_tV58wFY6buWRGgyqQDv4Tzp81z2FqocjztLC1J80Dn9RBZWDZiWkWeTnCGUlVr1-m3S3BkM4HRP7XJyp8PBgmzD4oA635fT4YMSPHAB-ty9HWiTB4mh5IuuobH3JyEaZGeXdiMJEJydPRjBly6QCvQRCuMKDdxe_05CajvW-8gHN9c3cJdXHEP7tq2CRU_CfhYlEKU5KgxG7NbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین جان خیلی عذر می‌خوام ولی اسم این فن چیه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83157" target="_blank">📅 20:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83156">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">شنیدم رافینیا و فرمین و پدری کاندید توپ طلا نشدن، دارم میرم اونجا امیدوارم اشتباه شده باشه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83156" target="_blank">📅 20:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83155">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvkWyaXDpS-HS1FA7Gx087HGmgF3HBMMhk5lrWhCizmRbShbjKYqo0X_W_umRglPgWXZng1US-IR0sgYSvvb_xviLYRWMSa4WPZuIvbV5yNbWfhYkYC2wXmpvOvVJ7S-4whtVSDj1D-TIBm_8eIz94IS5fXAWPrZnuu88-I-O8wte5LCMechG9Yz06xHDi9ejJwFdhgB6CMX1XpT4qQy79N4PYHCTM4ekmHwNtG2NCb0A6X-PLoIUtPnguhtb8T7r2_fvduRa202jKRmsBedr76t_BdbPlRYKasYylFDjfHCZ-d30FN97vmyRWL0fmNFIVgCG8Mm3mCzHeQcTeB59g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین جان خیلی عذر می‌خوام ولی اسم این فن چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/83155" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83154">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حصین بنده خدا دلش خوش بود که یه دونه حوثی‌های یمن از محور مقاومت موندن که پانچ خفن ترک بعدیش رو با اونا بزنه؛
ولی متاسفانه خبر اومده احتمال داره عموهای یمنی هم تا چند روز آینده توسط دولت یمن و آمریکای جنایتکار با نوار مشکی به صورت جدول مندلیف برن رو بنر
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83154" target="_blank">📅 19:50 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
