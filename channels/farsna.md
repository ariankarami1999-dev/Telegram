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
<img src="https://cdn4.telesco.pe/file/EU0qUAghnO4Nz-5Bwf5oc6xFADnAG4o0k5BqW9-n-DUKMU7oYf8y_rbC0uH7okxaUCkKGgfbkOF5h6WBXCcanQRUXstxcc9OXFyxer2KegUlMcRcvYGUoH43KjNp8a5kY8xQ1ULpvP0m2TbWHA7cRcIRoWbS4rXF4ymE-5odQHLKz96J06n6lGb3G2uyvbOE4QX7MYppOsFCA-IS0_gfEqv6tvHA8cUaSAwQKbnY9BC8LgX_n1Omw2YZeTtTb9e7ZrC2gl2SUvCj88cNj6V136eXdgm8OEql3ZItgmwFU081C-mt7PNDQbB-oQ50_J59SCB4qopMYxvBFXMoefjKJQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 03:29:18</div>
<hr>

<div class="tg-post" id="msg-435505">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsT9uVp933U1FyTkmd1gGW5RANM4EFdyqVFFvKDuvpOehjUF53Rfd8cYRHfKYVfThi_4QvhcXLBbf5zESYiZsI2D0jV4bBsQLigTIYzJ7gN4E2yzcvPyFh6lxpd4AOoXQ7EhQr5RaL1XYGPhmIjHPSJ1QSdRCOPYJTVAAFbE4wfEQSPmuNqmYxl0u74ENciaENtOixeLR1fMllPxwUeWMXgbxXSZzCDKv-HsOosZnxbZYO50EJosnEWALBAKcfr4QNbEpGuZGS_QfwnJb-ewry3lTkTM-VnKZqerbNsO2CO6r-bchmE7QIc_DbqeqPaJfVhLqkIwaNPWPHBWJJ5iOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحریم آمریکا تبدیل به پوستر استخدام شد
🔹
استارت‌آپ چینی «مایزارویژن» که در حوزۀ تحلیل تصاویر ماهواره‌ای و اطلاعات متن‌باز فعالیت می‌کند، پس از قرار گرفتن در فهرست تحریم‌های آمریکا به‌دلیل انتشار تصاویر و تحلیل‌هایی از تحرکات نظامی آمریکا در غرب آسیا، واکنشی متفاوت نشان داد.
🔹
این مجموعه طی ماه‌های گذشته چندین گزارش و تصویر از تحرکات نظامی آمریکا در جنگ علیه ایران منتشر کرده بود. پس به‌جای عقب‌نشینی، تصویر اطلاعیۀ رسمی تحریم واشنگتن را کنار آگهی استخدام خود منتشر کرد؛ اقدامی که توجه رسانه‌ها را جلب کرده است.
🔹
این شرکت در پیام منتشرشده خود اعلام کرد فشارهای خارجی مانع ادامۀ مسیرش نخواهد شد و از افرادی که توانایی کار در پروژه‌های فنی پیچیده و شرایط پرفشار را دارند دعوت کرد تا به تیم آن بپیوندند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 768 · <a href="https://t.me/farsna/435505" target="_blank">📅 03:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435504">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پلیس راهور: اگر در ایام جنگ کارت خودرویتان را‌ تحویل نگرفتید، دوباره ارسال می‌کنیم
🔹
در جریان جنگ تحمیلی رمضان، برخی شهروندان محل سکونت خود را ترک کرده و موفق به دریافت کارت خودروی خود نشدند.
🔹
حالا رئیس مرکز شماره‌گذاری پلیس راهور اعلام کرده که کارت خودروها، دوباره و در بازۀ زمانی ۱ تا ۱۵ خردادماه به نشانی ثبت شدۀ شهروندان ارسال خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/farsna/435504" target="_blank">📅 02:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435503">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
عهد دوبارۀ کرمانی‌ها در هفتادوچهارمین شب اقتدار
@Farsna</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/farsna/435503" target="_blank">📅 02:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435502">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKE6yryfo1fuadeDn95-eiYBffZbZGiq22NzB68JUJiOGXGQcJjx54CQmGgDKSBQx0-L8BSqAGkDiywL_iQPLM7PNJthjyJUK601GE4K6nXzDhYM9F7otstpS6feGn1TWoPdFjDgYIbLMKy0ZNrMPhpxIDFf1jLCJrHx0s3CZSmDwpZj9E_YcQhmyhxcH1ghrfrZ2PS4mAwAbL_SPuoymRLeH1V2eblYtlLI0yQwLnmXC0cXbA4acrgeRQo5TYnWCHrGNYJAZomlFayWxjxZA32XrcBUDvsTDawWP7UoqmYuFdqLs-WwvMG4lcpEBxxzu-r-9j3RacJl5wuqs29nUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روبیو: چین نقش فعال‌تری در موضوع ایران ایفا کند
🔹
وزیر خارجۀ آمریکا: هیأت آمریکایی از چین می‌خواهد تا از نفوذ خود برای کمک به حل بحران در غرب آسیا و تنگۀ هرمز استفاده کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/farsna/435502" target="_blank">📅 02:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435495">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sf0s6XZAuEGsgFC2PYrB_2IGWmKSiP6o1HQxfOBOGvxmVxLPm9Ss64zOlvMUVSLLBLSn2v6-uBv30TDOFVJAbPKpm5QQnNgWYY2GtD_CG5baa-znNH3lPFjJJder70y6BidgGXbldONccJlhFKhJVUf6towH0SnlGwPZPp51mNXhO_8JLuvoqKscQRAe5iwgLOhUsH4j9Vd-lDJD-ks9GeH_6kkAg7i8AQPFdOhiCQMDSYNPcpuFUjesFlIHMQ36qUmEHYCcFoV99UuszFTnUPjPW9nkqxyLSd5_R6WadZnykTytTzjPO4O4QUGXeMasrqVZDt7PYH_BZceHV_5CUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KysFwEw3Dl-JkEws5xF8toknlcPmhDRmFcIIva0NmHp3V-yGPFVDfHauWMObh50mIX3PxlLR8MPJRrkC8rry5jp46sgI8x7nQml2BOT7-6C3toWmUDb_7uuneNAb83OefzshYgs6ZT86YvFkvK67gYpDRdEvu-S6urQ6T9FwpburleMioBao1cL6KmqvosQx3Ptdax7TVrfLVcB9qd-QFBJ1MoAPlYU994rqmmYa5BRwlyT7cqu4bTCMtYdTKD0wS28C_jeaPpjPi_ZC2fdq4Whfu7-TPUOuz6c1bI9C-Za2n_EUG1b9XrTcketT-01yxrWbnJlfbIdNx1BBKFY1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbFd5dEvkzVj0eBPf7WQzkNCD2idRaAgZviglYBVJMRrYXQsuJbTUzZZSl8hDXROcN30BrE9hTL3NkrfUw6Z-cieowCBSKUiUjHQO7DToLr2a1JDncsycHMh0MHbO6kyw3Y-ap5dFd_61rRYqKZ6Y6rOroDoeB1kJyrsrgLNGgsYcHvK_mXt7ShSWXaQYLPXlwZxNDycMOJjuG_xGrUTagRkWngDliCT56A65bSjllb789DlzomlftRmfFId2Aa-l77qnHfzLkkhvEiAeAgE16upkoVyGl1_rAwkXA7rSWQBxneKnw1Z9gu4N8eQ09Yi49teGTiFrJKzNO1_ppNDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qICNsO_IePSaWZZhUiSSAXBi8QKIw_OCBhcxpre-pYDffcMPQ1pX00-yEbp1wdw6LKThE959vZdrNeC-3OG4o3AQUDT11u2hsVwEfDRZ92mKuuS0Mn4YKLiIOw_0tOs2QEksalrL5HBXN8Uk-Nssekik7xQNh4o2NlOkaOsWxNOc7a9C3TAIw7VPsI9ArXzq3nWSNW58QQjr4MoArdj2TipD5DmKIs8kuR2nLx2SfqieG3lc5citn09RUSt9zXKcTx-Exx_acHipzL8bcARl88kAyMlIWRAtsZ4bubaIFWCJX9kvCyXi2FpDxEMs01LIMxicdKrom9f0J4jeTkhyFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ST8BPUTI0J0qL_0tsNU_eFJCdEpaVlPATb6kwGQocIyZwrtieba86kez3Bv8kR3nr6p6FdV1KLZexEZBJeOXzw4gJ_RCX12j6VIySdpiy3HEDu8teNFObVEDUO9M0xfc62zO01GN97xJ54dogRdz-B9Nd2ZHe4seiPd-_X2ia1f92ihNJBAKyc7r08VQUf4I6LgYsfkaIrKK2Ar4DpOi6qflIdaZU9uJ3KHWC-Kjka0sT96v4CwyRGOXFAvKmlTSco8R9DiuGXurtqbyVmPkIoGJDLX8NlBEwJyGgJJLYs4CKZWbX6nkYpepJY2eyUTFdjBPKhA6i11NjyVzE7mbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRJnn9FzbI-IkvFi6ZjV81RYDDJuls8GWRqKw6y_sPG3vAbveCcAp8fbtMn4zd9DdzkuQRfbg8NOuc8nI8tTSHFXxUDQq-gDWUL0RU4njuQgksxZmKbsAyuFeqXkA2genaK4EM-sghbBI-CZQVTfuLkrQdy6U0D_RuES48K22rv9UW0m6J9xBw94qgDGap2ZYsgGigGo99aZtwxzIf9uwKwt5Lv8zbD-0RvagYe2YZAXySqoHvMeYoKSNHEy-k0zQI_6hSykkqmb-wmFt3AukGMY5QSwcUaF8V50AJzLDeCVB0QZkNf0xoT_EXCFZYGheYdZho0JyeFDKoPX_RFFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H3Gux31W1Jmsy0jyX8MW7eQlODrqby0OAViA_kVhPc3p-8Mgdsa2lrfuyYm7DtcBw49f07SN3LSFOl4LZE_jcP6K89q0txCOYPlhm1MOFpvUqu_efld989bsX3k8AN-ZKz2gA0lIRegAnANPanPqapsI5c5ApKIkJ41zed5Z6BjvSyE-Kl7WacL8RU_-tEyqN_MX85z91C4GHH0jrhLgFhsWZjEunY1L1LWnOu2gUtgFoD_Ucl2gEvJTQz_-oqWhJFdn-7nmLNiWlH1q413M0RAdLR_I6S-Nb7HK_--yPNAKk_jljsf4O3AjUINCAaFTv4fgrPBUzzOSTJALR8-4qA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بدرقۀ تیم ملی فوتبال به جام جهانی ۲۰۲۶ آمریکا، در میدان انقلاب
عکاس:
صادق نیک‌گستر
@Farsna</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/435495" target="_blank">📅 02:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435494">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sggJu0l9Jjw3oCAXz-ULr19X4qpAf1TFt0hQmflrMG-XErK1k_R96Z4KhWEP9NDIrDoirt5WGKc9K9Fi02ZJS7D0tQKmw63qRS-2yRGpYzEf9VDOOxcGxkixLEvof7lItFXtcgv_eN6n6TrwUzm8u4kr_2IMYyJX9tGB_UC_7MjwrJInObIAB5ml0KuuSBLAnBwBBo9HwP9MK_tOui0D6bntge33O73mXqeR-GQNFucg2qLqPRC2tT7WTzMXOT77YBen4A5u02hwm_SAkYlGmwrWy6bcYRS_2zG-Apj1a9d--Z6X1npbACYCP-uD0BZbHwxwJLgwJmPqB2T62t80nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحرانی که ترامپ پنهان می‌کند
🔹
ترامپ می‌گوید عجله‌ای در مورد مشخص شدن مذاکره با ایران ندارد. اما آمارها دیروز فاش کرد که آمریکا بزرگ‌ترین آزادسازی هفتگی ذخایر راهبردی نفت خود را هفتۀ پیش انجام داده؛ آزادسازی از محل ذخایری که ترامپ همیشه بایدن را به خاطر این اقدام در جنگ اوکراین نقد می‌کرد.
🔹
ذخایر راهبردی کشورها به ویژه آمریکا با هدف خاموش کردن بحران‌های نفتی شکل گرفتند اما حالا کارشناسان می‌گویند که این ذخایر دیگر کارایی ندارند و وارد مرحلۀ «تنش عملیاتی» ذخایر شده‌ایم؛ حتی مدیرعامل آرامکو هم می‌گوید، تعادل بازار نفت با باز شدن همین امروز تنگۀ هرمز چند ماه زمان می‌خواهد، چه برسد به چند هفته بیشتر، که یک سال دیگر هم باید صبر کرد.
🔹
با این حال وزیر خزانه‌داری آمریکا هنوز در مصاحبه‌هایش می‌گوید، عرضه را کنترل کرده و اهرم‌های زیادی برای کنترل بازار نفت دارند. اما مدیرعامل شورون، یکی از بزرگ‌ترین شرکت نفتی آمریکا معتقد است که به لحظۀ کمبود نفت در جهان نزدیک می‌شویم و آمریکا توانایی جبران آن را ندارد.
🔹
تحلیلگران اندیشکده بروکینگز نیز معتقدند که بازار انرژی جهانی به‌شدت به ثبات غرب آسیا وابسته است و طولانی شدن تنش، بیشترین هزینۀ اقتصادی را برای آمریکا و غرب ایجاد می‌کند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 2.71K · <a href="https://t.me/farsna/435494" target="_blank">📅 01:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435493">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a0fba85b2.mp4?token=N_Jv1bhyg8ha64qQ_ASyv7QFvvBsMPfJrbUrTaAaIRnvCyYqxEaMT-Zdsw9hT175N62sgrlAANbtfFQkvSIwsM7pq9Nqg-hny6jTnlt9lV7ufemEKVui0OZ18_WUjrqdXQIvzNvfAaV7Oy3GGd72jTQ8iaYMHlUtLq0g9ORQsrJEmC_Yjo5YAYvtjAOvbVww5nZridSiCBtqpgcKCbJqEXDq35EgEcjoHQlPRgs94N1aK33TkEivrs8mk58NFvV7UybJzUkjxKy4uSsCi7-tUDWL0DFhwZH58ou91QjeC1bshSKUBguE-aGvVg0R1cFfNebMzrzZ8p7JGEqE0l0Plw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a0fba85b2.mp4?token=N_Jv1bhyg8ha64qQ_ASyv7QFvvBsMPfJrbUrTaAaIRnvCyYqxEaMT-Zdsw9hT175N62sgrlAANbtfFQkvSIwsM7pq9Nqg-hny6jTnlt9lV7ufemEKVui0OZ18_WUjrqdXQIvzNvfAaV7Oy3GGd72jTQ8iaYMHlUtLq0g9ORQsrJEmC_Yjo5YAYvtjAOvbVww5nZridSiCBtqpgcKCbJqEXDq35EgEcjoHQlPRgs94N1aK33TkEivrs8mk58NFvV7UybJzUkjxKy4uSsCi7-tUDWL0DFhwZH58ou91QjeC1bshSKUBguE-aGvVg0R1cFfNebMzrzZ8p7JGEqE0l0Plw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تهرانی‌ها در بدرقۀ تیم ملی در میدان انقلاب: دست خدا، دست علی یارتان
@Farsna</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/farsna/435493" target="_blank">📅 01:26 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435492">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMo_6cmNQ20Hir8urTK-_4xWooUEu_dQzY5HpUJ6EzVxFB66aTTlFoCFM3p-Ii0jztEQ-KYHU7-2Uq8IK1Hzp_Q6w5pvDZ9MUUyWhIFTBU-ENZcTuUlXcxhXI0yM2UzY1owk3d0iGEtSZJCXIHF3uVrLVuOB3Q5DCERLyWkccf2gANMhhdKnchm7GcbVRnAsnhifdVnmFPrdBWwEGEHnWn7WELBm8s9gWcX8QbcovftQqbZdnaYUgmPoB6bKukTU1lrjUBENZVMRdPQ7FbABYENVVbFI9Z8HHSTzklq6gWAYA4euu6WGwNN3Qvbzb8YxalSb8LclzMsuOKAV9zp7MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات سفر نتانیاهو را تکذیب کرد
🔹
دولت امارات عربی متحده بامداد پنجشنبه سفر مخفیانه مقامات رژیم صهیونیستی به این کشور در زمان جنگ تحمیلی علیه ایران را تکذیب کرد.
🔹
این در حالی است که دفتر نخست‌وزیری رژیم صهیونیستی نیز تایید کرده بود که نتانیاهو در این سفر…</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/435492" target="_blank">📅 01:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435491">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLYfye42g9CvfEzmD1EvMLWS5O52zboNAFlgiAuGEWOtSSVYU494IOCetSYSBM0Ygc2EODLbpWAbXFWItq9kYGs8SS7CcAziCXse_e5QyFN4QDFpH5kfW2Li_zKAP4Fr6B88rC8gBLhuDzlHer9Olw8map9CVDq0M80hrBdMXQj7n8GjoEzg_neBWb_Gz1IGdk2APTtgPVqPpmIvTGG-Dv-478AHl_y1fKJ6SkFfWT3NZ6Dawp77KhxQS4lhso3a2iP9xYqooSbTpfz67FYoUqky0DcMCM_u1OiAGJMJ2GHaYJ5Vs2uRyfQwo6xAs44cU6kxRFCQABdZQuYUl5Sdlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای خبر گرانی پیامک چیست؟
🔹
بررسی‌های فارس نشان می‌دهد خبر افزایش تعرفۀ پیامک که امروز دوباره در فضای رسانه‌ای و شبکه‌های اجتماعی مورد توجه قرار گرفت، مربوط به مصوبۀ جدیدی نیست و پیش از این اجرا شده است.
🔹
این تغییرات ۲۹ مهرماه سال گذشته تصویب و از
۲۳ آذرماه ۱۴۰۴ اعمال شده بود
؛ مصوبه‌ای که بر اساس آن تعرفۀ پیامک اپراتورهای تلفن همراه افزایش یافت.
🔹
طبق این مصوبه، هزینۀ هر پیامک فارسی برای سیم‌کارت‌های دائمی ۱۱۶ ریال و پیامک انگلیسی ۲۸۹ ریال تعیین شده و تعرفۀ پیامک در سیم‌کارت‌های اعتباری نیز ۲۰ درصد بیشتر از دائمی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/farsna/435491" target="_blank">📅 00:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435490">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2edb2a1af5.mp4?token=KEeIg0L3ofgcfBF5F5LdtinBJw7QTy-4a3OVFCByEm3S_uZQrqjv6RvuK5njZZlkWwTu-FUmZqwJ4Bfj9q-yQv59AKJUeSDkV23jfEYjCx40mMYllVmwxgEftjO43R90WL5vo-Be2jprKxIpjkcx4r3Cbb74C0uSDM6mnXVEOI9c6pX3jpb48GQ-6JBEWH_bkHTlm6pVCr9Bx1_aHu971evSY68FfMEyJzIQsed2MD22eN5GjUbU0UfMCaDJv0lXRcT-y7IZQnyQIQUESyPHNOwX3cUgVn8JMbNmxGbvGDBHkEAqx377r9kW3OHBIl5z584QO0DTOD2AWBueCZJhAxHFRzGxjy6iRKe_n87cqtC9GOZOn3trow13GEB5p7DBfMfGywSzMVTy14TrdkLKtQHQra21dKh0O_UIUq6e7hgSNdPp1Jl10V3mDpSM8FEis9xXVdOo_cSgTfoWJYKfzvd0la64DVODt2ryzjH645ioDVluT98M6ytjt5t8fdjUw6hMNTWZ6RtPiZvM2tIUeDbuDfsaLUQTBFcTBDdbo1vUF2JDHrnUFE5c5yzVLe72C4FJhXT_g9lj96Q7rWARt7TYmAwwjKLIZSHaTzdbITOjalHVO_zg4t5yKtjxnW8hMkhpVODBZdRRhN5_GfXyvJbCCBr0fSQ1Fp_BR9ocEhE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2edb2a1af5.mp4?token=KEeIg0L3ofgcfBF5F5LdtinBJw7QTy-4a3OVFCByEm3S_uZQrqjv6RvuK5njZZlkWwTu-FUmZqwJ4Bfj9q-yQv59AKJUeSDkV23jfEYjCx40mMYllVmwxgEftjO43R90WL5vo-Be2jprKxIpjkcx4r3Cbb74C0uSDM6mnXVEOI9c6pX3jpb48GQ-6JBEWH_bkHTlm6pVCr9Bx1_aHu971evSY68FfMEyJzIQsed2MD22eN5GjUbU0UfMCaDJv0lXRcT-y7IZQnyQIQUESyPHNOwX3cUgVn8JMbNmxGbvGDBHkEAqx377r9kW3OHBIl5z584QO0DTOD2AWBueCZJhAxHFRzGxjy6iRKe_n87cqtC9GOZOn3trow13GEB5p7DBfMfGywSzMVTy14TrdkLKtQHQra21dKh0O_UIUq6e7hgSNdPp1Jl10V3mDpSM8FEis9xXVdOo_cSgTfoWJYKfzvd0la64DVODt2ryzjH645ioDVluT98M6ytjt5t8fdjUw6hMNTWZ6RtPiZvM2tIUeDbuDfsaLUQTBFcTBDdbo1vUF2JDHrnUFE5c5yzVLe72C4FJhXT_g9lj96Q7rWARt7TYmAwwjKLIZSHaTzdbITOjalHVO_zg4t5yKtjxnW8hMkhpVODBZdRRhN5_GfXyvJbCCBr0fSQ1Fp_BR9ocEhE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپادهای صورتی و آبی شاهد ۱۳۶، میهمان اجتماع امشب پیشوایی‌ها شدند
@Farsna</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/435490" target="_blank">📅 00:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435486">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DiPigpZuVM51_zBLVQsQgVtuuBTL_XPlRP5zT0Y9FEAJ68pGeSthOLmRXnVMKn6pZgWsEbPrd4P6il3_I08D67Y6d-826-najmRXYkxNCwiGIITtm032rc7hgYz8QKVFtWSdouF3Mpdjsj-sOvnDG29bcUNV-kRyiJ6lGnmdThmaJMxVY4y5DEQgR7mvLWp5j87wIEAp21KX8xed7LfDCgRQ26xUeUUCBQjbpwxRirvB206MWujS5ZJJFLcgG9tq3OjI2nNScvetOb2g6q1PW5myU1KChjbhd64Pdvb0hFa0cr1gzn0ObqXeUjN-0ZIX66Oz0hWsaa8n4mAIWsj5Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ckdoDT7D7riBuMey1Ij11O1OF4Amef6a997hdbVv9LrmaZuSuXFKAIZtAaaIci4r3itQufxZZja_NtVrUy_UDIQ0LZYEJN9bCii2GxmXUzHyq8ohzJlXNInvp75P2w9A0YdBDpJfKtOU-EguNjbtVTQXW2jF4nBlY9IuuLS5mmdlbSve8jIepEePTg5iMMIyfIgfB3oybn7jI-pyzzUFBZIoyOxZIi1_PdFhgfsZe_EzHweMu26Oy5wIT8xn4GNUOcyuicMwWNxLV3n2y4joKAXQDrmSVIzHfbJTfPjGKgx4t7xbNNdbE3MicwS1IebYDY2vTz7Yo4vtMXeZxIlt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kfQBJ_yok5c508nkTOjEe-3_jzKF09CsAhGiXBSEFvwqlIxcv_7zBXvGQp8vRV58baLhFe1_Z-7FW1npRPOOKeFPBpjcNvYfWuEnqqqEfHlMbCArThuymCrcuR1TAoRG-RnVTU-7m42JbJuS_ht3UKvphAOu2YKXp-jpJrdszyhcn4pI9q8S_ZfS7K8n4EYZdluHM2wpmlmhOkGW-QmSxhVC3_uTtnzeCVgYPQ2De5qK4S_Slt1O2Q3OpkzBeT4QwjEQ6qtsRQpLOFs2BgSMay9r7t0tpl0f_5ulx7_8K1joghpAPSokffjPjo1vIMgf_XEmd0e4fv-qQzESqaFopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Poqsx8wcfW58nV0GGzmlADSa9H5d-K6xlTvYXAWffKwverXQ762nLofjtBUeKbz33iZL0tKDmC1jkTKgapO7qhgcjHPjdn5skQ93sqQCLS-W93i2R9QOlrT_7DjO1zoegQelPyXWMdzBCihTP1Oq-srtGhyP4JItowPJPJ49qV7Y30SuQKPvBrJq8zyanjHZ6ZR2e-gfrNJIK5dGuSRY2WfkYMg7ZxWwFV53sJGzpo3rXwJY7nuweopjY_I-TMRJPwIk6SrKXpD5YpVGXGoRu-cW5TzbxrEtNrqVrp-JvPJlpy_6KvEbD7krpRtCWNtVfIe3bDDWkRPEP7cMtq3log.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۲۴ اردیبهشت ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/farsna/435486" target="_blank">📅 00:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435476">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spNzSMoJDyj3cgJVCoD2PIH81iPDd98oMiWojg3huR5deLoqEouYgmSdic0TIzlnEkHc1SJ1lSYvtFsEqTPY-cSU40JsD3HK5hOODmJWTYzjjwwn2hxOdJmec09S1khDCuGHqEfggmOcG-MdPHkxracswSZ5bqvWTwh2ld0Ouz9UAnmC0Y4-29Ta1EFKmKxjyUT404g2LWITVTpfSHOFnW0mxsAUSmzaiEpzlY4DjwIebq9MESCjwDbt4vixmFdK8GhXAQByVJ05VfBnYAJB5p2h7Zwe2dogESyblSpl-ICa96Ws50CcOrffahCPtc9fksZrOW04auqSdslPPDtOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3y1Uzy6MCnLAoxsal6SlnmV8wf4RA7cN9FIhjL036-MepM-11cdhcIVzOkyum8tzum3zkFOGn2gRmiC81V63zITcDyh6WQ0UEvi062hyuiD2gQlK6lbQ4S1ypstbWhBTqMUefmPDAHQre9LymjenqWkkqS5faLaZDi8IAamVB807JGIJ9xJpf5Xz8k2vbebaQjL7uTV-PzDFvl9BcPt6diJt0qJQlGFJnN8o5sizaLm7R7JXNMS9hDNNtJP3hTW_GZTry1MlZqPMSsDYtIIiHdaUpm9yzecUdM8Dt8So7MUaRSWr4vNEsdvG8m2YY9XBT4gp81ynIe0trwWcU02Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESYjXn5dWXQE8BeYfns_q1RG_JNxU3gcVOCcxcE3oi_f9TaddkPN2CaqBzVUcHliaS-jJdNLcvux3QqNJbKMpdbPgCobWTDgNRHqEDp6OkWHnP0A1gg6FIGQmZ0wf4aOa2So9CT92WurxnHQ0IdpB9sEelXw7OSGeDVL_SuWJMBo6JwS-eIR9UVzKwqMryBiafRI68MeVb2Tuu8HaaUkf4xC-jonWFQz9fmzOQ4u_3TgB4UGJ_WeQCh0oS-QMFr6T8dhB7Rfgc5HU2SXfPHUjh0JNHhTdyu-Rou5P6NqRvZdamLXGNmIeoOLAaA02upS7yjdDTVKMegNkoCarzp0IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMrXHfiEU844wgGmde3TvXdm5ERt0lrI8qSqdebBIfmXgR7Fw7-XgFUYGV6iE2DK0lBY2s2jsd24UOfVsLbTytzOIS6UL6uMaQleZMYvntAMFZZpOvaHVdgZ2F-IVgMq_-0_MZDlhSaxqor4TkJ0DMuCvhzriTEt7SstKY1qBJ5uorc6YjCThTw1VIaaMbMlgs1ehEkCZ5PBL2YX0tphIxeutYx-zcs-xBjoJryByFXmbLQHealyKkrFbS6prR4APjEvV_lR-T7_osktYKDpHMEFTaLbBWe2s69FT8BWVQsvpxSIv7cASxPqjgMUZg9MFeQsBBA1xVGhdI9d28Zk7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHYDSizgWyNFv5Arz4UDWawzP99ldceXjIjuqZipks0If7cAffX6JrYfB96y2uYR44EvZ-YtB1BdBPtAjxuJOnFMDizmOYn5vZNj6LOgyP59tFkH6y7GnE8OsVM9H30jrb_iPAGdRNQzTmziNLyN_F4gsJ9WTd-4EEQkQr4GNednOX7c9ayl6mno0IV_M57iEfw6HjZ6HuBONou8DOfuuERxaGz7BUC8SbF3R_96MQVx5_ESkdroWPI8_BAZ0L8N993ydDfKC-YZtJUU9XSebVo12gcBLxZEZ76EHtLAGVL2lUIW_rkwSSDhNP7lTfSpSqYCWfkIf_Duvr7fNx9bdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQrZaBB7Tor1ifYwEGRAqhHcZy7mM1ZtaCVURxS_fuq2Hk_jt0145elxMQDT7er0FIr0lT8tx56U0G0Y5khZIcfevVsoHrfsvNb0LRxl8POwhCKdS4U-IyZRkO8Tkth5-st_MJQTFPFIcMSeoQYtCdbkHRnwjAF_13Rn0i97hJA4x0otytfrR4hehxLE_yu53hk6Gz6m4T-YOaRxCG1C9UvCAd3_-53Y6qN-L6_6ZBBkmbIqfjGBX1W8Kzj3rPgM5dzOyOLXyqOLRVpomIiC9De-l0i4Pn_xjRr56nPuTnjVTG96-2f2qg8LohRCEhmygmq41Lrz5dPyQJyFByp5vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k2BYibI9rQukKJSQi2JpZnHIsstJeU43RM3kSlSsQ8UQyGCfrd6BV6uag4AHpJLmt5I659_MqsEIxR5dO6xXBZKyf4PPpQK-_qzejb62Q83UA_uRtJWcOlIymYFkOMLtU6TTxI_huWzcM1WHPLWUmhtUeIU4BXv38rgi8LZHOPN3JFqVXfWaJXwKWHv5wAv2_kxCE-RtJsd6C6W8FBja2-QJnGyR8VTNm_Bcu_N0e2ClslTvv0zuAjImdrhcNS-a42qDTYZj_N0yrGTUgDZ4jppmghQVnVPRTE1S1JidLKtOp1Rqmk-VXJEEQBIm7vsSpzaipZu4iYricjCq8hNQVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FiICjXlcMc0WSlgwVtWh8tQsOpr2jV0OQ0GtJZ0yHSCGTsA4bZQdXJLtdeXbFDNGSXvRMz_m4O3lv0yNjCxO0MyATMPO6fQz5FM4Ec9DqcRT-1rxFV-x0wrERjK4qH4v_MBWHR2qf8WMw0cOZz6yvAl6UzG6M5EUgJABjcQOTZcy5cFPUp0SJo-APGzGOHHxjc41ePqOxgHIxr40haBDlfc-RoTIcL6EyDRZBltB1_ixMSelrAtvY5MSh01zp7TvxEUfvpBYMYbmQlRJDGBg5GGEzg0-wgRlpANk6loHzkJ8Krqud3M-ns4EJRy662pPzZo9w3kuGHBrZq6fDNewzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6yRq_RfU8Q182hy3HmEWCg_vODl-MyEGukNnLfgcSfG3VzbXWYlSKJC6VUy-mDsUGUSDC8OksQjXCO4tBmQ3Fk3CryrapaNP19XerfGO9jJtznJP2_v_IsZlITzfVpiehvkiJdJznSH_bywdBC8WrpV5jGjs5Kd2p8OYy7QyXmyjO9LzdeeZrth1jlIji-lnEP9HASouUw1Bpdbkk4C5MXXBUJVa5y2XA4UDRg3vDU8wTZ33gWsVh3SIsp_eSukeXVwu7OR_fJSrQnvnBKGXu45moyr1Fx565eLLalHCl1DxzQ2ry1TASoA2fYzt4pnniF3o71RaFWh4htqbx32aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lB2a-yRyP_3tD3WkWM2-EymL7-2PtMDN5jLww0BnAskYnh8S31o5FilbhpCFThnM70Kqh3UdNqRqbqcgsYsT0Q-RgDpKAvmanOOyIjjjhxGPLU1f6R-a3CzdiOmTM6DoksHG5mL8uRRxmjzKkH5KfG8I8BKpgmjQjlPAif4Yhw9YzmRdXNtSbPsgs13_vlAswEbDSYPyGuODQmbQ3SC8pet_bOMgqgNau7mFKMxIXm-p1japeLYVORc0JQk7-AP31CvgTeXpy9fItOMWqyEz8DQLWH6KtdBV5niQReuiBuvkekWAPlI08sl43TZyMfA1w-tp0NWOI9ME7nXyTfa9jg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/435476" target="_blank">📅 00:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435475">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">امارات سفر نتانیاهو را تکذیب کرد
🔹
دولت امارات عربی متحده بامداد پنجشنبه سفر مخفیانه مقامات رژیم صهیونیستی به این کشور در زمان جنگ تحمیلی علیه ایران را تکذیب کرد.
🔹
این در حالی است که دفتر نخست‌وزیری رژیم صهیونیستی نیز تایید کرده بود که نتانیاهو در این سفر مخفیانه، با «محمد بن زائد» رئیس امارات دیدار داشته است.
@FarsNewsInt
- Link</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/farsna/435475" target="_blank">📅 00:30 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435474">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎥
حماسه‌سازی مازنی‌ها در قرار شبانۀ دفاع ملی
@Farsna</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/farsna/435474" target="_blank">📅 00:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435473">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BY6aKY1CEFskNbFA_VfnJmyvhA0tGvuAVZfLYqo_RZq7u09U1CiBIjGnctRveeJqcLK48eY5rGkekOUD4-wPvQKvpCMYEVJL3SolD-cW7Q6yp4zRQSYm1u0tVKuYnZtPScm9M8Tgo1cSK0nLZ7LcVJudGne4hqPMfn1l3VsVWMTT7a_czPxE8R1dEDB4i2Ap4sJZPUI_gzqtPyvp3x_AQ12dqxh8AowDVPqTAnDAkG1AePGEAk2C6d08GAbCReXHHUkvCfeomGME-Un8S-JhEixvqA8i6iz8_LQSjAtf1vCHHBi9l03IbWfkJz_bAMGVl2_TFYCfwdR5cLZN3rrGZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: دشمنی با ملت بزرگ ایران، قماری احمقانه‌ است
🔹
نتانیاهو اکنون به‌صورت علنی آنچه را که نهادهای امنیتی ایران مدت‌ها قبل به رهبری ما منتقل کرده بودند، افشا کرده است.
🔹
دشمنی با ملت بزرگ ایران، قماری احمقانه‌ است؛ و همکاری و همدستی با اسرائیل در این مسیر، غیرقابل بخشش است.
🔹
کسانی که در همدستی با اسرائیل برای ایجاد تفرقه نقش دارند، باید پاسخگو باشند.
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/435473" target="_blank">📅 00:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oc1aD2aVLBq-ETrJGdaqUgtJPHHmirm7ND1aNxZIq4PvaEhQcGMUq4qvmsajQeiTzWxrzNU_-A0jmOmT7nOCgVZdAeAxozn02frvIoaXDTAwt9cYlG-9Uvde6HT6_Z98Zt7tzquxxrhFGg2oh-itd1jGO56gJeBQOj5X8bRFXGFgHiRwiFL43iAzIDuRInCd5HFY2QSQYe9g5vEa97SdrkWMtSWXJ4rSdxz6Ox8IgohmbJlXHl8n_SLVa16u0yzMSdMt2nWdrmj-QCQuzc36bCF3Z6j8lfeyXrFkvMNj7GMnYVdOKGwwr0gs1Tp7CVoFw_XqtXDmB2Yp4Gq8kTz_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QHTQOp2q2JLEbDoGZqZ32YnXooh-gME9RY868Os4GgEFJkRJ2-RBLIT1g8DJXAlEO8Iv3CYpnDJYCHeH9bRfEdugfMVxhfW0T6wTQ5OOnX07F6v2VFogVZN1fXoVmJXAmX3_2iXJ53w7tjVC3G9KPcJxmSoFPP8NU4DshBnJv74VceEzwBK2Trx1tGi6HXfsRrpYrS5kZbed6tBKc5ypj6SA4Vq3bEFpnjYhLvQ6QEYdXCsfUq52OcQLW9v6zXdVg1lymx6uSWr_zs1XnooFY0hszfw1TIrSN2XXG4n6HpQETT-ScKVoQoaIIiZrHz_bcBFnCeA0z4abP2GFQPax3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AalKREjS-ZR1bopfpHnVNHvBkU_XuarKg3A2tnCxmURbnQGROesAIc53H2fi0S6jyXlgG4-eaOW96NHWRgRD6bfDifZo1HAQbwN1Ev1BtKU8M3lodZ14VEk6aLcUO1i0VyEYNRyGqklLJNMRgMHSUXquiVg3kuOhip1rm1bPxTS8yj8kt3zIxeOV7wRI7LrGNnmFRm17wxOkGWuzt9q-rWVCjh9elmc7O4tG1XYRd7Ys0U9D7v2MATpLbYmYiMOjXhmzZLyhjBSBEZO5XvIeBnPiSWG8MXqgP2w8ttIOT7QyC_P0xdfkYlplJOI5xuQ-NViGXX6HGRA7Wn84nJ5WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lTshZELkCR6pXi47CXWi5lnShu3F2GfH23bdOAAQbRfhNsF_vNjUZxOGDw05psq5uKeJGHJuzDyZV6seawYZsHcmfFWawy7ak4gKYmV_qwvcbDqc2d5-A64vXhDPO8-kigbD5jppSiQAU3cxlKC9p4GHeQZhjYNGy-vj-B7yx4kSYM0v1f8VXQ5yumVEgbm90onxsFmaxpZU1rpkz9ES6tF2_JvQE-VozANkCiWBagJ9AXibyqiolMZxJD8oF_gXRqtcBbjEx45qheghOAwALGZI8OdYPcFKaPPOGEsEqZKXXDFWIDxdf4iHSSlAtll_WU7-bhYGV9Rw2Q4CLtt63A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YzniWBQWTcdjo2tL_WiqoIDitc2q6cPTpXt1HNkgf_AokrrVDXH7Zrpq9kc6U999WPVBY62ThCC-g-R0CbcuGk59PpOWbOvZRNODxtZRP8ZNvYvkaSDHrjIljCgnAn8BkQP2U2q2q5k8yTWtN5VmLHQAIXL5VgJPgU7EpiuL3CIdQF8rT0_SRoI-2rrLarN99HTSKUOLp7Ts8wiBKRhAasUx9Jbfp7V5s6qou4D9ejEgrb2hN3Tfbb-gJhDQsVI8dCXkqKCJJnYtY9iHfq-T9BC0T9DlNXLG_lv4p2r1KdVakjqKYub78_5N_kKZaUExgoS92MF6NENsI4r2kB02vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAQYGeV1awKB-fLRRDEfCyq2Kdm5naxvLz3hhhjSnc4QlyIlf_JiIzykyFb-_6cI9kZnuGw_5lL7YKMp3oPRLl2gAHJYqetVE8c6v5RTX-L_HjqFT0YOMDw2FheJGRTjBdeKuo8PTEapah0vffL5SzXOXYMc1HLtItGx-lC-fzpNLxEpt3micS4IyXYylvmMcUrIIUd2PxCc3lrEXYEq7NzrmLdgzxpDWmB19fwoLazHKfGP1EzmJg-Q8nf3Qw1yJt6QGTC8HdtZ1BYGIz8NYOY5QFBNE6vPZ-wGVyWvSQlOB9h_VbX64iVcNY2TqN8lXO9RdgA0Ne_LzS4KfrcZqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nd8gtFgsF5cqUHDREGTp90eNJLEfl1HxMUypC_v9glDrddg1uV7iHEzuM8S4gYsVEIEv3El1BYTaWc38M-CV7v_JkiKyE7i7I1fWxs7qmpKQlxBcWId875cpZlGjsyMVYJIVQBMGGG_VlXy6shld4lSYld4fruP7cuCquX4CWGs6fpVl1lbZPGIGv-GewaTCx4EZjw_hOd-dgKTGlEIXAYB5EwY_kxu5P_YgMHWKcR37Xtm0ikyTfCB4WkcTwIJFv-G2qqnW7OthA05lFAlVMsHyWo0f2TpQ2lJaC6TkNve9aBXMP6LrD6FpM78gHxFvc8Jul5chVjCLTXXdIjMovg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رویداد لِبران (اجتماع همدلی و همراهی ایران و حزب الله لبنان)
عکس:
زینب حمزه لویی
@Farsna</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/farsna/435466" target="_blank">📅 23:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ebed97b1.mp4?token=JNpGrzgy7eHs8uDkyKrBpgu9nZkleVzPCwDn7b6-BZQimtwhD6pxrzE_u4JgwmWZnBrztT4h6i4qWCqrhKVmUOK3s-9YWDfBTgqHrCBMii6Jv3JZqfR0045QXioi55flIihyEKY4mviDO4d8x32ruQRoRVK5FXpisBL-1eZGhxUSD80spKg5a1lu4F_O2xqr1Sh9B_BBSB2-cJSInWCWSmtTLiFgDvvk9aHhK4TDXDTv-ylcMOTR060lZDVEO7WQxj7670U6CdDILVNIN7f1XXSK5vnz30sbUiDq_5QsEF9oZt3AjdlliKN-q5C25TBidTvC2x_FMMtteWVG8ST8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ebed97b1.mp4?token=JNpGrzgy7eHs8uDkyKrBpgu9nZkleVzPCwDn7b6-BZQimtwhD6pxrzE_u4JgwmWZnBrztT4h6i4qWCqrhKVmUOK3s-9YWDfBTgqHrCBMii6Jv3JZqfR0045QXioi55flIihyEKY4mviDO4d8x32ruQRoRVK5FXpisBL-1eZGhxUSD80spKg5a1lu4F_O2xqr1Sh9B_BBSB2-cJSInWCWSmtTLiFgDvvk9aHhK4TDXDTv-ylcMOTR060lZDVEO7WQxj7670U6CdDILVNIN7f1XXSK5vnz30sbUiDq_5QsEF9oZt3AjdlliKN-q5C25TBidTvC2x_FMMtteWVG8ST8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت حضور خرم‌‌آبادی‌ها در ۷۴ شب حضور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/435465" target="_blank">📅 23:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f969c9ff.mp4?token=Mq4m5Qqk-Eit3jpZFoD4QVYv-kDpjwyEoY-hUpSt85X7TdUs_lErCe670zLHQ-Lzp9eTAlntnftErf052fygpd-Wo6Hy3dQj7HUYxSlc7czF5Vy9VzlEvBjIpyWA8SMwApLyko1IIudfJ0p6dm1iynsHH2r7qH3jbuhzUHt5Dsz9lwyT4pXBiBjN05_FlRwbmrZ7HCDOEenhKjhoOCqGMMJlvzsDsmffJGs1n_WH1AdgiXbzWGKOVOzfF5KlWoO2FdEwI3kXfNpwwm1zGb6jEP484JSI5Z-vWJjv8KC3Gxt6BZKDMo2e2FhZoX94B2VfQrxVjPCt42yyA3dhijUrlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f969c9ff.mp4?token=Mq4m5Qqk-Eit3jpZFoD4QVYv-kDpjwyEoY-hUpSt85X7TdUs_lErCe670zLHQ-Lzp9eTAlntnftErf052fygpd-Wo6Hy3dQj7HUYxSlc7czF5Vy9VzlEvBjIpyWA8SMwApLyko1IIudfJ0p6dm1iynsHH2r7qH3jbuhzUHt5Dsz9lwyT4pXBiBjN05_FlRwbmrZ7HCDOEenhKjhoOCqGMMJlvzsDsmffJGs1n_WH1AdgiXbzWGKOVOzfF5KlWoO2FdEwI3kXfNpwwm1zGb6jEP484JSI5Z-vWJjv8KC3Gxt6BZKDMo2e2FhZoX94B2VfQrxVjPCt42yyA3dhijUrlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری سی‌ان‌‌ان‌: براساس آن‌چه به ما گفته شده بود تا الان ایرانی باید تسلیم می‌شدند و محاصره آن‌ها را پای میز مذاکره می‌آورد اما نه‌تنها این اتفاق نیفتاده بلکه آن‌ها توانمندی‌های موشکی خود را بازسازی کردند و مواد هسته‌ای نیز در اختیارشان است.
@Farsna</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/435464" target="_blank">📅 23:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/916ff1848f.mp4?token=i68lA8tw2a6o3lyo48WPIR4d8sxsfE8s3lPZA4SdQY0koo7ZCb0Wb5fERmcPByJa0BOXPRilEzsMuNZP-FO_mNkUTjI1sIb0Ah347SzCDapMxH3NtZ-6MinnetOYs7Fn7W4GY-Y4O2hLRo79sQpMPdV0_ISSpj76ayGrxWduWSaInWwWBxkhh9IjlN8ik5Pjbo0-nisLDa36wZD78Yp8waCjiC3iaNEpj3tHvqC7tNMwWnddn7cagqiV-A8WBTXvghZMKCEvOQ-RDB4YhcvPWoIpFQ-Fn9P_VcqJ4tVpjY4xSqmE5QpHqftK7DkqpVBCO1oAl_cimsEii2Hy5e1bqa_due-o3NWc-HhxOQwN-gI-Y9KiaG0AX3Z4kLZ7tYTEasnORPlDlL3HeALEbt0us10pzdbIkIhlTUjGtcSVY9YrAaiCN3mMP69XLUDdIPM7MkTD-cI1mVSyTf9Fwpv3ndUrYfLw8JH3WuK1AgmQWoU7uWW88-wTEv_IbnSTrqAZBYk5tSm5Za6DbYKUnSMvkwvIPJFs3sTEWVp1BwIz2rsC9ZEV8eY-zPRSMkVoyrbDymkTcOTD_tP6xFAH3hFYWxdxnLjD_W4ANEUkR7Dt9PzN0FeWYDJ-4gyTn3Mo_rVhF25y8XkpEsdAUzSQIBbr4o4gDeiiqWLr72XqJlNUmFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/916ff1848f.mp4?token=i68lA8tw2a6o3lyo48WPIR4d8sxsfE8s3lPZA4SdQY0koo7ZCb0Wb5fERmcPByJa0BOXPRilEzsMuNZP-FO_mNkUTjI1sIb0Ah347SzCDapMxH3NtZ-6MinnetOYs7Fn7W4GY-Y4O2hLRo79sQpMPdV0_ISSpj76ayGrxWduWSaInWwWBxkhh9IjlN8ik5Pjbo0-nisLDa36wZD78Yp8waCjiC3iaNEpj3tHvqC7tNMwWnddn7cagqiV-A8WBTXvghZMKCEvOQ-RDB4YhcvPWoIpFQ-Fn9P_VcqJ4tVpjY4xSqmE5QpHqftK7DkqpVBCO1oAl_cimsEii2Hy5e1bqa_due-o3NWc-HhxOQwN-gI-Y9KiaG0AX3Z4kLZ7tYTEasnORPlDlL3HeALEbt0us10pzdbIkIhlTUjGtcSVY9YrAaiCN3mMP69XLUDdIPM7MkTD-cI1mVSyTf9Fwpv3ndUrYfLw8JH3WuK1AgmQWoU7uWW88-wTEv_IbnSTrqAZBYk5tSm5Za6DbYKUnSMvkwvIPJFs3sTEWVp1BwIz2rsC9ZEV8eY-zPRSMkVoyrbDymkTcOTD_tP6xFAH3hFYWxdxnLjD_W4ANEUkR7Dt9PzN0FeWYDJ-4gyTn3Mo_rVhF25y8XkpEsdAUzSQIBbr4o4gDeiiqWLr72XqJlNUmFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غرق زخمیم ولی قامت ما خم نشده
🔹
رجزخوانی فرزند شهید لطفی‌ندائی از شهدای ناوشکن دنا در رشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/farsna/435463" target="_blank">📅 23:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
روایت شهید سپهبد موسوی از پدری که دختر یک سال و نیمه او در خرمشهر جا ماند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/farsna/435462" target="_blank">📅 23:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7fffaad4e.mp4?token=hHBbkMlRJ26-DwzIEeEurK_s1hjZzqgE4BYsw7-KAr5H6-9FAICBxwqb4C8t0FtVy9vJkJXYbgJjkw9LOlxnQ1tcZZqLGuqiZBYXv7DldIbpU733yFSdxaoYbdA0FIt97OIeDjFp2EsmnAZzhgfx9b066zc0Tft_R52maUO4yBDsiOhEemtFDlKwRbYqlYDysHDo6aK3-v2elF8qHGeuGPOEJigfHSscUACwTTj2g1zbB3cP9oGfu-4Ye5EWX4ov-xfrW1skqN_jeMdpDV6rHJwfjLXzMT02yWKe1pnoqXdOk6LiAtpOki5XlQeuShC1AL6_mRfHgM9SHeSu4vnFkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7fffaad4e.mp4?token=hHBbkMlRJ26-DwzIEeEurK_s1hjZzqgE4BYsw7-KAr5H6-9FAICBxwqb4C8t0FtVy9vJkJXYbgJjkw9LOlxnQ1tcZZqLGuqiZBYXv7DldIbpU733yFSdxaoYbdA0FIt97OIeDjFp2EsmnAZzhgfx9b066zc0Tft_R52maUO4yBDsiOhEemtFDlKwRbYqlYDysHDo6aK3-v2elF8qHGeuGPOEJigfHSscUACwTTj2g1zbB3cP9oGfu-4Ye5EWX4ov-xfrW1skqN_jeMdpDV6rHJwfjLXzMT02yWKe1pnoqXdOk6LiAtpOki5XlQeuShC1AL6_mRfHgM9SHeSu4vnFkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاینده نام نامی ایران
🔹
از سرود رسمی تیم ملی برای جام جهانی با صدای پرواز همای رونمایی شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/435461" target="_blank">📅 23:32 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
اجتماع شبانهٔ مردم اندیشه در شب ۷۴
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/farsna/435460" target="_blank">📅 23:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTVNdYBMu42XU4wiMZKNXS3o2imI48UQjgl-I_fDykCJR9YOi1zaaEpnjhOP8PNT3yo1_TLVdBmRWijS4uBxM3NQMYty2bD4uycNZrX2TGIHJQ4wMPXD2uYk3zUNgBq0MY8QMkXr0y6qSvewujs6OT5RDvttetcDra9AulDyC95xsmDcJwAenVBHPyhsY-8BLFJVzrhnHSJ_qdTrcVMIn0brZKgZ4p6PWQcSnVidL3kxDiS21FwLUPJRWmI-bx0gTIyD_HHYP6iZDT7iOcAfYCUYSVcBiM-2PioRKfOQ8UHcsLvv6opEiusaSzQjsm9TXTXdUYkLHBK8XQ7dwhql0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرر هفتگی ۶۰ میلیون دلاری شرکت آلمانی از بحران هرمز
🔹
مدیرعامل شرکت آلمانی «هاپاگ‌لوید»: تداوم بحران در تنگه هرمز بین ۵۰ تا ۶۰ میلیون دلار هزینه اضافی هفتگی به ما تحمیل کرده است.
🔹
حتی در صورت کاهش تنش‌ها بازگشت کامل حمل‌ونقل دریایی به شرایط عادی به چندین هفته زمان نیاز دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/435459" target="_blank">📅 23:27 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435458">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎥
۷۴ شب حضور میدانی مردم زاهدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/435458" target="_blank">📅 23:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435457">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">فرودگاه امام ۴۰ پروازه شد
🔹
مدیرعامل شهر فرودگاهی امام خمینی(ره): روزانه بین ۳۵ تا ۴۰ پرواز از فرودگاه انجام می‌شود.
🔹
در حال حاضر ۲۰ مسیر پروازی فعال وجود دارد که پرتکرارترین آن‌ها به مقاصد استانبول، مسقط، نجف، شانگهای، گوآنجو، بغداد و مدینه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/farsna/435457" target="_blank">📅 23:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435456">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
منابع عراقی از شنیده‌شدن صدای چندین انفجار در اربیل خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/farsna/435456" target="_blank">📅 23:11 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435455">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🎥
رجزخوانی یاسوجی ها با فریاد حیدر حیدر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/435455" target="_blank">📅 23:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435454">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09bba4b1ee.mp4?token=Wbu3CmBTZCuGpq04olNPxzLaaRPjIQhQBBXH6tYCmxcedZMEi2ATReZYtthUTsDIdcgy89VrM43TfTVyrseF_KHze6YbGLzt-tImWDT1RufwN5mWVas-g1xGSBsZ2qpIGPhjP2IfOzGMZ_6X02ug0mrDcU-hQpgamz-3974HF179XnEfejXLENTOT07ySCg0m2MIdQRjA-5asfsKAnli6eMOAUyYYbLq3GbbH94qoi9LUQZYynT8EJ4FHq_boBPC8vj8IeTq95yPoEES9sWV5l1KE2GAdb7d74TNeglloZ53zBHR-bALcu4Xp9HCKYGT0wcUCo7dl5E_a4ehzSLm7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09bba4b1ee.mp4?token=Wbu3CmBTZCuGpq04olNPxzLaaRPjIQhQBBXH6tYCmxcedZMEi2ATReZYtthUTsDIdcgy89VrM43TfTVyrseF_KHze6YbGLzt-tImWDT1RufwN5mWVas-g1xGSBsZ2qpIGPhjP2IfOzGMZ_6X02ug0mrDcU-hQpgamz-3974HF179XnEfejXLENTOT07ySCg0m2MIdQRjA-5asfsKAnli6eMOAUyYYbLq3GbbH94qoi9LUQZYynT8EJ4FHq_boBPC8vj8IeTq95yPoEES9sWV5l1KE2GAdb7d74TNeglloZ53zBHR-bALcu4Xp9HCKYGT0wcUCo7dl5E_a4ehzSLm7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم ملی‌پوشان را راهی جام جهانی کردند
@Sportfars</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/435454" target="_blank">📅 22:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435453">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
امشب موج ۷۴ بروجردی‌ها همچنان در میدان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/435453" target="_blank">📅 22:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435452">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">معاون دفتر رئیس‌جمهور: پزشکیان گروه‌های مقاومت را از ایران جدا نمی‌داند
@farspolitics
-
Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/435452" target="_blank">📅 22:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435451">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bc347445e.mp4?token=F66z1grCUYFdsjpcOYfoiP5yoHcl55kxQya2Rz4fOHSZ9sWG5ylxc7iKHcSjjwBCbZdAOsOcFrNQzVWjwTdz66cA7NBj-EsurvN_QQaoZKHXxs-bL393FmPAgk9jQzhyqi7TiWeJOg5EAOw1LXlvKYdDBxvWjfY0UwMp3-wh5UkYZZ0UGbPCotFmtF1R4cwEWmmezDJtyuUPDm6lk5KwQFGuy6vjYUOFLGfQLZ9MH4CzozbGNJ7WH4x0j2t9buoWcUqdwLw_X3aJTCcdfD6eFZGcmpYuLr1drneEMvM6xNFNO68pnNH3lvej-i2a2rt5BGJocNKePmKvcU2agqtfyjfa0MTPKrJMbWGkGFt8AWWq6rHHlYHXbmbVAGxYjZOcGYpPGY75rPd5mFFOmyHVT2Q29aXU3L288VDpEd64oASQeImkjE2RFdRvR-CC_M2NjcD52K7XI3nzFYOOwB0mYE-g6dPvbTnHtuS161Oy8qthqW5VNtHBKIbNzJx72jHcjWVi7P19JG3GZHxeKCx5YU2POX94UQxBJyLE5B4IF0ldSt_1GM1NKRy9J4exA2xW4SSQOdginmR6PqeAKlOSBFwOSDIMMQOGs61AWRxkqpyBPLIhKTkO4zmLnE6pu5KG6NHyg1HWCp8oQv_qcSlweqX8IamrUi02sEQT7Cckh5Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bc347445e.mp4?token=F66z1grCUYFdsjpcOYfoiP5yoHcl55kxQya2Rz4fOHSZ9sWG5ylxc7iKHcSjjwBCbZdAOsOcFrNQzVWjwTdz66cA7NBj-EsurvN_QQaoZKHXxs-bL393FmPAgk9jQzhyqi7TiWeJOg5EAOw1LXlvKYdDBxvWjfY0UwMp3-wh5UkYZZ0UGbPCotFmtF1R4cwEWmmezDJtyuUPDm6lk5KwQFGuy6vjYUOFLGfQLZ9MH4CzozbGNJ7WH4x0j2t9buoWcUqdwLw_X3aJTCcdfD6eFZGcmpYuLr1drneEMvM6xNFNO68pnNH3lvej-i2a2rt5BGJocNKePmKvcU2agqtfyjfa0MTPKrJMbWGkGFt8AWWq6rHHlYHXbmbVAGxYjZOcGYpPGY75rPd5mFFOmyHVT2Q29aXU3L288VDpEd64oASQeImkjE2RFdRvR-CC_M2NjcD52K7XI3nzFYOOwB0mYE-g6dPvbTnHtuS161Oy8qthqW5VNtHBKIbNzJx72jHcjWVi7P19JG3GZHxeKCx5YU2POX94UQxBJyLE5B4IF0ldSt_1GM1NKRy9J4exA2xW4SSQOdginmR6PqeAKlOSBFwOSDIMMQOGs61AWRxkqpyBPLIhKTkO4zmLnE6pu5KG6NHyg1HWCp8oQv_qcSlweqX8IamrUi02sEQT7Cckh5Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرائت میثاق‌نامهٔ تیم ملی توسط احسان حاج صفی
@Farsna</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/435451" target="_blank">📅 22:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435450">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🎥
طنین شعار مرگ بر اسرائیل در اجتماع شب ۷۴ شهرقدس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/farsna/435450" target="_blank">📅 22:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435449">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80a9a739b9.mp4?token=IkhkmTf7KoOZ5Snt222l3JiI0GfVlUR9wuxBWiZM_N_K4iflZxZfFWJknBmcgLJlgm5Dhkhm2omIf3ywKnKGwvMj3gsi8JK_cFij2gg_haPzMVynat7xtXTHRuwH0a5f2rpnvfYEr8Y3NiEGlfZ5d7tqSpJ8OPoZlxzp4p904gsh__oSuN2YuK02z0EsgDGYgJfpOysMB40sS_LHvs8n41pKwyo2JZWJ456tgxoKPk6fi69KclG6g-QhvPDbdaC7D6czIdTDXTWmjqIfzTSogF1vaPYFnYoq4PCIuq-sSoCq7NEu_pl-9izD3AVc39LKK9npDjvq-3CzSmVwBWzq7Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80a9a739b9.mp4?token=IkhkmTf7KoOZ5Snt222l3JiI0GfVlUR9wuxBWiZM_N_K4iflZxZfFWJknBmcgLJlgm5Dhkhm2omIf3ywKnKGwvMj3gsi8JK_cFij2gg_haPzMVynat7xtXTHRuwH0a5f2rpnvfYEr8Y3NiEGlfZ5d7tqSpJ8OPoZlxzp4p904gsh__oSuN2YuK02z0EsgDGYgJfpOysMB40sS_LHvs8n41pKwyo2JZWJ456tgxoKPk6fi69KclG6g-QhvPDbdaC7D6czIdTDXTWmjqIfzTSogF1vaPYFnYoq4PCIuq-sSoCq7NEu_pl-9izD3AVc39LKK9npDjvq-3CzSmVwBWzq7Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چی این چمدون رو سنگین کرده؟
@Farsna</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/435449" target="_blank">📅 22:24 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435447">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎥
۷۴ شب همدلی و عشق به ایران در خیابان‌های گرگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/435447" target="_blank">📅 22:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435446">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USy_SOHMr0bohkhah-8Qv1y35OGAwnX4RnJl5EbnFXVobLnMRQYLiy8QBk1H4krZ8owHCy5c22-OoqRiIkM7P5B_yRMc7uGDnRACucQ7LfSk7stwK-ay7IO2H6YyiB638UkB7hGoaaE7LqZ8OCN3zrJ4BK0vejiC0dJXHAF8cMYrDo_37axQmfhqN_arx_No_DjGm3dzQ4YjNC9ajiHjZ34PMPJre9yl5mOsSt9VkMbIn8cnUMX-GHME5_v2bruFlkEvgXAJK0AePorrAv_PHnuVAI0PrYvAfsPjoCrgD-4XB9rgviZdZTJd_6Y-Wgjl8sQSqbkfyjMUNqHZo7zFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر شهید دهقانی: منتظر مجازات قاتلان فرزندم هستم
🔹
جلسه نخست رسیدگی به پرونده متهمان شهادت سرهنگ شاهین دهقانی‌نیا در شهرستان ملارد برگزار شد.
🔸
سرهنگ دهقانی‌نیا ۱۷ دی در شهرستان ملارد و درحالی‌که هیچ سلاحی همراه نداشت هدف حمله اغتشاشگران تروریست قرار گرفت…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/435446" target="_blank">📅 22:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435445">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/708ad1605f.mp4?token=iuTlh0f1_lgtz4Exn9hxy22gyMD8_NiG-tzhwVc5AyQ8xdeE-UzWBjJH0Xm-PLmv6s1MBPVlMEpDhU0XyHnlQMqQgMNZxO39MlLv69bve4uqn7oEogAmPIe_59hHFQ_Q1pHN1t3c1215pvAtcH2aMX76dIXWtN_I7sKuVA9_tyUO9-cNKOP8edzNKoXIFt81nF_HOr6uRRgr41_Mf62eHAgvBKNpDjrub9-kvj53dmctN__emkUEdmn7Q4y5DhvWsnxz4og6zuM3lRF3oDKedG-gsZP0fkorq2QytMHejmkJovg5WAKbx1U8IvGgvihV-lXu6ceoRxpsCMYFqZpv36n3qzMWupaiQ9I9vnY_wgMGZ8-38o2YfEOOPJb2zFjPy_DWer05a7pjja8F8RlRMzAEnpHa26yU7CiS7Uj54gc4H2zFZvxq_W2oklx_zukh2Rqnc0eJAj41NhnVpSb5oXTPpKnfcNY8PsdJWoHJV0m8au-2txYHz8HHHxg-uzcd4YK_pI5XU0vHf8inz2EK7FpFiFMDLKlzdwPnm9XsEk06RU9zTVN15QOfc9iHc1IIRAY0cnoMBXmWaHwdgfFQ8U07ceCBpBOi4baKgaksjJ_DeCCbKuHsFVa9Pfm947qKjWwtuuzXBObYMUUc_UWkpvmnVWSIyWmot6Cbh19f52A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/708ad1605f.mp4?token=iuTlh0f1_lgtz4Exn9hxy22gyMD8_NiG-tzhwVc5AyQ8xdeE-UzWBjJH0Xm-PLmv6s1MBPVlMEpDhU0XyHnlQMqQgMNZxO39MlLv69bve4uqn7oEogAmPIe_59hHFQ_Q1pHN1t3c1215pvAtcH2aMX76dIXWtN_I7sKuVA9_tyUO9-cNKOP8edzNKoXIFt81nF_HOr6uRRgr41_Mf62eHAgvBKNpDjrub9-kvj53dmctN__emkUEdmn7Q4y5DhvWsnxz4og6zuM3lRF3oDKedG-gsZP0fkorq2QytMHejmkJovg5WAKbx1U8IvGgvihV-lXu6ceoRxpsCMYFqZpv36n3qzMWupaiQ9I9vnY_wgMGZ8-38o2YfEOOPJb2zFjPy_DWer05a7pjja8F8RlRMzAEnpHa26yU7CiS7Uj54gc4H2zFZvxq_W2oklx_zukh2Rqnc0eJAj41NhnVpSb5oXTPpKnfcNY8PsdJWoHJV0m8au-2txYHz8HHHxg-uzcd4YK_pI5XU0vHf8inz2EK7FpFiFMDLKlzdwPnm9XsEk06RU9zTVN15QOfc9iHc1IIRAY0cnoMBXmWaHwdgfFQ8U07ceCBpBOi4baKgaksjJ_DeCCbKuHsFVa9Pfm947qKjWwtuuzXBObYMUUc_UWkpvmnVWSIyWmot6Cbh19f52A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع شکوهمند امشب بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/farsna/435445" target="_blank">📅 22:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435444">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVV3WWeLcemOR6oJVbQWeSu1b2TGWgRkgVL3ljlNOyhqFBYWzZhwq1YQHPGwJ-upWCSMLN6V1Obl3m1V7gFIT50GLJVT7B24miEW9fpWJyJstDs1e7uw-OWnqrhucVZh_SaCqqTzF88JwuzjQ8rAMGPxejUDCM7thKC9xsUegmp1vAGM6zhGhSt2kw47yxyDbIoUmiKqji70ygAqDE60mSs4DKkPaUxkzvkmKO4OVy-ewWC93eDaI4T2i5YrqVin1XxIhOuJu6Rk1NdEY9fvkwAicDzEWEG_Sy7O-Ym5OD0W-jxm70VJBoYjgHiOMDsSSGGHeFRuONwtZno1m5MFkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوش‌چهره، اقتصاددان: در کشور و جامعه در قبال جنگ جدید دشمن آرایش جنگی ایجاد نشده است
🔹
درک درستی از تهدیدات وجود ندارد و بعضا شاهد ساده‌انگاری هستیم.
🔹
نابرابری میان تهدیدها و مدیریت تهدیدات در کشور وجود دارد.
🔹
باید قرارگاه جنگ اقتصادی با افراد امین، علیم و دلسوز تشکیل شود.
🔹
در درجهٔ نخست، نیازمند اقدامات آنی و کوتاه‌مدت برای کم‌اثرسازی برنامهٔ تورمی دشمن هستیم.
🔹
مقابله با لیدرهای تورم، ضرورتی اجتناب‌ناپذیر است.
🔹
در تاریخ جنگ‌های جهان، دولت‌های موفق در شرایط جنگی بیشترین سطح  مداخلات را در بازارها داشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/435444" target="_blank">📅 22:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435443">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHnwPLJU9eT_FEpksX6ymigD1Wy4jo7czfL4pWPGUeBxopVCDcpUqHHZJSySqyabgGCoIHIt-hixTgRYrDRxxvU4X1jq2LyOBVPxFgJxf9lC62sUjX4G-9OZyuBtiJU-a8FjujIZUahe_oehw5fkNLsWLpGZIO_VpHouuRho1hWVjz7-zVnP2wFzXBCE10J9IAUzt1XUgEHAzCGab03SyryKPoQUfEL41TivceR-ipuqoy9afyX1wBKiH1Ew6ZGk4qUQzjpmKenK6BTOosBhn1sCLfIMuuWbJOvSgTBmPvf_ta9rUQCSKlATbaPN2NvKKnpXESO7gJ3nS1m_pwV-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردهای تهران با شروط ۵گانه ایران برای پایان جنگ بروز شد
🔹
شروط ایران شامل رفع تمامی تحریم‌ها، پرداخت غرامت جنگ توسط دشمن، تثبیت حکمرانی ایران بر تنگه هرمز، آزادسازی پول‌های بلوکه شده و پایان جنگ در تمام جبهه‌ها اعلام شده است‌.
@Farsna</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/farsna/435443" target="_blank">📅 22:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435442">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhkzNv1ZV7SryiF4QgKQ0Z4jWgfVoUejsyleu7frrcga-eOnpP77a_WJGkqQ7KntWqm8F0dfGQ2v1FGxIADOsY27b7dAjIFEJ3u6AcqkQTV0Le9gqTGA-GAiZKt0BIg1IODBTOYtA4-EyaG6UpxbDLG_RHPpOdArrs_iH0h9qzPn3yTNGpufhQ19kRb_evL8yt9lhkd9I2sjjKWUo1vCtHKMXY7Bu2qBPsdWXCB8jtCiJbpirMkA_vdV7looJN6a4e6Ue5yeXVvji9smo5d-XsQe0GH3iLpMLlxd8cLgfuF6f2gXbqAcCX4LyKacTEw1UPg1xurpzy7bZuNQT26Pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای همراهی و شرکت در پویش هنر برای زندگی
لازم نیست هنرمند باشید.
هرچی دلت می‌خواد بفرست:
نقاشی، دل‌نوشته، عکس… حتی یه خط ساده.
چون هنر راهی برای آروم شدن دل
و کم کردن اضطراب و
خستگی‌هاست.
آثارت رو به پویش هنر برای زندگی بفرست
تا با هم، با هنر،
از سختی‌های زندگی عبور کنیم
شما می‌توانید آثار خود را
اینجا
ارسال کنید</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/farsna/435442" target="_blank">📅 22:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435441">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/435441" target="_blank">📅 22:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مارکو روبیو: واشنگتن پیش‌نویس قطعنامه‌ای را در شورای امنیت برای دفاع از آزادی ناوبری در تنگه هرمز پیشنهاد خواهد داد
🔹
پیش‌نویس قطعنامه در شورای امنیت با همکاری عربستان سعودی، قطر، امارات متحده عربی، کویت و بحرین تهیه شده است.
🔹
پیش‌نویس قطعنامه خواستار توقف…</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/farsna/435440" target="_blank">📅 22:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435439">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03ccf47277.mp4?token=KQHYcfAEWQzY7GjFBfcoXuTYzGRRs4KyWYkrUmJ4mgCSfWdVi19LSnihmuCvuO2TAuC7gHMQOJYUW9igs9LzcHpWUrsqomHv3mquSAcE6LLjppTzP5BVt6rXMJRQmBpL674h7VBBHOIId0NVec_VCtycWsdZOAZ0-qZs6NkjdMUlGOiXyX_4kEwujgQ0S0ske_ECdZaWkAO6q2Z66YGpueyoZddrwTNOIH8PSwExiQVEyb2GImRbxHz5cuRbzZ-7o5Lun7J9Q9QfoUITVf1vLEpRTKqJS3KGUOzcBQ87g4PZbXnjOQMioOo6sI3ZMF1xPKwgxZF12WVhwhHPPv7Shg5t_Fvt5rawAxYdCsm90vieENONtKEnMSB7I_YUCkQvL72ZZPV_uuybs52gc6OBDQRn4TyxO8XVzbS1kpjBLvzaRocO7gqZ0ngWIUQ5zU7EG2Whocf-Tv8Af4163KFOXLpYB1G-gNmYdOBLt-n6xeJuUCQ1n97l9xJ8zdK8tovAay6dZP6qxVGPU7tmzoPhv-7-mv3uOt32-IaFrLMphLWe55wYQmUdloPoFq-_aL_q3eG4EZ-nzcYHb7hzumWsiJ8hTDqkgcnRIkg9OELbzLXwjAeVi2xg5Ux5cOKJB-c8F4q2bbl8BEWdlgGf3gfjKicyiI0knUyVtTga-kD84NM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03ccf47277.mp4?token=KQHYcfAEWQzY7GjFBfcoXuTYzGRRs4KyWYkrUmJ4mgCSfWdVi19LSnihmuCvuO2TAuC7gHMQOJYUW9igs9LzcHpWUrsqomHv3mquSAcE6LLjppTzP5BVt6rXMJRQmBpL674h7VBBHOIId0NVec_VCtycWsdZOAZ0-qZs6NkjdMUlGOiXyX_4kEwujgQ0S0ske_ECdZaWkAO6q2Z66YGpueyoZddrwTNOIH8PSwExiQVEyb2GImRbxHz5cuRbzZ-7o5Lun7J9Q9QfoUITVf1vLEpRTKqJS3KGUOzcBQ87g4PZbXnjOQMioOo6sI3ZMF1xPKwgxZF12WVhwhHPPv7Shg5t_Fvt5rawAxYdCsm90vieENONtKEnMSB7I_YUCkQvL72ZZPV_uuybs52gc6OBDQRn4TyxO8XVzbS1kpjBLvzaRocO7gqZ0ngWIUQ5zU7EG2Whocf-Tv8Af4163KFOXLpYB1G-gNmYdOBLt-n6xeJuUCQ1n97l9xJ8zdK8tovAay6dZP6qxVGPU7tmzoPhv-7-mv3uOt32-IaFrLMphLWe55wYQmUdloPoFq-_aL_q3eG4EZ-nzcYHb7hzumWsiJ8hTDqkgcnRIkg9OELbzLXwjAeVi2xg5Ux5cOKJB-c8F4q2bbl8BEWdlgGf3gfjKicyiI0knUyVtTga-kD84NM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پیراهن تیم ملی در جام جهانی رونمایی شد  @Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/435439" target="_blank">📅 21:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435438">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/farsna/435438" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">«پرواز همای» خوانندهٔ رسمی ترانه‌های تیم ملی فوتبال در جام جهانی ۲۰۲۶ شد.  @Farsna</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/farsna/435438" target="_blank">📅 21:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435436">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea2800611.mp4?token=n9sM5Y_mjw0EsbwsPHzMACqAXycPGuyA8Uz100jNJoKvzAZaotOFp6hi_uBP7BGPRYgckt_FPg9gPglHXDfaq9Qpfrlebqbz6Y7E-EmCmZRKVkJrRlNLbkXS2gMO-mE8wK8fc8hnv4fyoDjeCIxzeqqUnigKLWfwCANJX4iHA6c1yV-3svNJlNST-Z7Rt56m6rWlpNHsqpHQU_-qXXDLZjUb_TLyh2_InTjQDISc0MNBwGY7llszPUKVwNU5cRUlRJSohCSgu2jXTFnB7RDZe2NRuaTsK4r3yhxyNelqxpwx42endfDtZjj-b-HgNzSBKzVkHr_BBfGHTZoduXgneIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea2800611.mp4?token=n9sM5Y_mjw0EsbwsPHzMACqAXycPGuyA8Uz100jNJoKvzAZaotOFp6hi_uBP7BGPRYgckt_FPg9gPglHXDfaq9Qpfrlebqbz6Y7E-EmCmZRKVkJrRlNLbkXS2gMO-mE8wK8fc8hnv4fyoDjeCIxzeqqUnigKLWfwCANJX4iHA6c1yV-3svNJlNST-Z7Rt56m6rWlpNHsqpHQU_-qXXDLZjUb_TLyh2_InTjQDISc0MNBwGY7llszPUKVwNU5cRUlRJSohCSgu2jXTFnB7RDZe2NRuaTsK4r3yhxyNelqxpwx42endfDtZjj-b-HgNzSBKzVkHr_BBfGHTZoduXgneIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از پیراهن تیم ملی در جام جهانی رونمایی شد
@Farsna</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/435436" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435434">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IingY6SMc2ZtUlavvxS3CluvVY5FERA2z72EdspZ3KSxAu6T6r0Tj3uRsiZq18N7OCYU1iwrddX9dmoghxtmkFPAr7DZ67NrvbZLFvuG7SpFzYVCIfj-P4YWdsGWJki4011UHM8JlfQLBqkwlnVmfcbBWUPXA8hlShPaazJ4RHbluo79LoKPOQ1npoZlo0axuJ6plspypIRwZtfCJKH3MCD3YjrMk4KVTRIcvEJkQMO7AYAAiCSaoGzf60pOcY_DFW2y43JW9atiS0VLqoCtj-8dZNmrKkElj-tgMdKSyKelInlL6l_0l8HegawqCU9leLYZYatG7WuRRyYWWbIZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
عراقی‌ها به کنسولگری کویت در بصره حمله کردند
🔹
به‌تازگی از خاک کویت به سمت عراق موشک شلیک شده و عراقی‌ها به‌شدت از این موضوع عصبانی هستند. @Farsna</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/farsna/435434" target="_blank">📅 21:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435427">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A0ZMK1mwRVEae3K_3cGKO86Pmje5NNf7pPe4ssr-IJFWTDuotpHwwRTSH2MSKdSx6RR3r2ErR9Nab_kCuTHkoPDLAegJXk_4RS8AWAZOJWSc_3ECn8-WW3zQ5SshIBqyAcE2elhERuvsWt8fHIoVu3X3fmIRGptpTrWxOTaDY_cjAIqzJffeRaLhgqXOLj-0l55-NePQud1Oe7pe-M_q2B9kgjFk_DLYYiwABZknJaHzYfFbIjY_oP44K1LJtSefZKXAJufxQlz4j5jXn0VdQz9nVBwLXykVx6EW5Bg6x5EMvJxFDaeCUG5d6hEwV4mb8JtyeCUErSMvdnE-RvSR4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awY9Xq7eaXVdM1BcLpiTKvDTTZRLRH_sQFC3cTIrApHHJWMwrgzYKdwjP3Uv6mcJf-ZlsJUOFZay5BnQxnd0hsUdnexB9Wp-wbaBBeMbpPhkM_hhDFfx2I4v5kDNG-uPfMlrByMq5_jN9ZD-P8XCNm3goqS4acq2kXqect0F10Z3GZ8jNCmq21ci_ZzPzN0ltoGtrAyeugpop878CjXr8Q5JkfWSylbeQI_8NArynqh-vHHe84FYb7ew8MyU8wbdevOIpwftgjHqRVwIAKuwq-66zSvsVtE2SrFHsAfJg3AJ7_1pSY7f88NBlSYViSnQ6vXJmfnYcoAlyIUhLl1nUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcSdMQsktH_dJUCKXYN4x3iOt9buipS4iw9wrOQjGAZi9m-FV0lV_q_Jyq9ZC2-16GjwarrXkywpIPGl7N5yyvzmDun0D6yRCMKI9PEZ7JwsEW8zz3cJBHaEkgUX0aoDGg69yIqkyf0mJN09fiReF-wUvwRcj4dGwt9HQMglK58eDlUmVnaboO7GlSv3JvHD_b6F4gMWUsowSbhci2lQ7It9JfRMrX82mySwxOtbZPIoIYhHnpKAz81HqzHPqKshI1Hu-mIxE56fkJ8jVKp1D8p8_9GxxufBdezzjzIbwPH6tqgLWGQuAbXO-eiwqt8UBgfBgmX-8X2fKNsEvcd3Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v39GHaQyDcf-Ar-zKD1Xa0b6oAZ-o_hdvTn4JTwaqGCTP3ch21Rb11PRSCa0bx55Lr-FH1l0FzgLQs0jRtTxewCCwz5G3LMYtZ2jiaB-47mwrN2O8myQ0oylYzYgAaDYQ_ia4UqEBp5F9y81RTQo4bjTHfaKaz6GWwMJyoH2AtBrs3448OeaXcfp-juf_u59vp2KtNHY2SL48kAdzgPitwHmWmdWw-Qq1V3phobewjgpNZLFmNv5N4dXT6fjkFIooLnx8qIsEK24dpxIUrNzweOt1A3jHcvuuV0gu9Dg4Kf0AtSJ-WIrhS1RaUIauShiopgRH3ZET1FgX3wTLsxeWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1Jpl3SP3QDX7f0p_D3UbGBIJASfOWFfAKjhYSCUQE4ErFjRVTyJJmFxyHJ8E3tQVfjMvP1RHCYNAESn8j1DP2owUDHqTSeYul4Hm9jhJ3nW_ca842t7tjyjVl6Id1XyHw-nrx_TIxihsG4QIP_9CgtVt0tKIWYwSDO6wLUjkU_7_-5iQA9PPAyDM7UmZUBoQNEovZhw0awITdUpnR0QHEHMd2kXpyjT9838xLRsDCtUxn9u_ugQjAnWS1UFeYTTtf5rjsUJyBtnPCQOSbzhYGyTkCfNAb3FXV3z2E5NGqU_x0vyKisfeGVtX3lAIRlvp4B7IGAXT3taSNSMdCPxCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGrOcPx0TQC8_emWEyaSGond4BcoRsiyodIIgq2iM6zaXvwsUsIoPxCNQykzBHAxwtyma2o5zYDk1BovLv84Dk8HH_Lf9D691Om-bnZoOrwgrHKviC8QPK5mOkTIcKvwzCBeJwe7wP2HmJo8F1hFljvVhosqrCKQHrS8eKscc5ZL-0bFYiJtvOPhPPT6YIBOQ0B-h17A-eMJr9i8ewlYE-HbNTc3IaugnAHX2feGRFY2muUIEwrsJLqGq0iwH3sJf0x6Jg1iFqlr_UaPKLRx2qj2zQg2F5_j-qPy9WAWwisPsj4h080rKVYepgtkYTkNT1GXRjr5D6TH8tKAoU7QFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jezo6aEYZAp5AYIpPIbyszF3xb_44QWePSYDKC-53O7iAZQl8or4iUtg1i8QXEV_Ntt5Wg1Qk-7LKF7-BG8I9Dky3spe1L3QzcmQMOfo241Snc1H-3r_bwX2f64LVNHlWWqBavHeayDA5Sn-ihYNu1aQ_f5YhvMUCyXQPX6aWZVM3-pLs-xLIwXpVcJP_fJlQgGVE2Jpgh4orKckKCKCg4BGSxLTALF5KR0IMZk9QErjAqk4RlB3HHlz84_3e3Kci702S_Q5y2JIlxPaZEwCNqg2T2NYaa_KDfRuhHc50uC_ZbwnPRCzBoN-C7pNcpAAFicaf8M-nZ6PYAeIQ1lErg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
چهلمین روز شهادت امیر سپهبد شهید سیدعبدالرحیم موسوی در آستان شاهچراغ(ع)
عکس:
احمدرضا مداح
@Farsna</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/435427" target="_blank">📅 21:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435426">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5de6b3208.mp4?token=G-5AZMlLQP0ykt14EKnCcE31wylCJ9mCNSOPHG53xX7Tu7dzOfPSLPKoNMxtlL8eRGRoZ-8CVh_X1F_oRbVRBHltcTW2FgSgDzgmOyYPHmbvpFj_qHhUcpWZlazGQgDuYtPW_0zIgz_x85H2vNw-hMTXnmqs7vZWl6yn4koZ3ngZWQ9wV9LtuRVy9OT3JZ49aFkPEsWdgSo73x_vrpoqtPAjlvr4Ro4REdZcsqkqysHfKwbU8pV2fo5LVANn9S1YVrBWXAeRflxzHhiAJ1ZttMdbqqj0DVgycf5PMBWQqERL8eISaYr41zXtrXMzsVVRbcpeYXICuEa5oNEsGFPciQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5de6b3208.mp4?token=G-5AZMlLQP0ykt14EKnCcE31wylCJ9mCNSOPHG53xX7Tu7dzOfPSLPKoNMxtlL8eRGRoZ-8CVh_X1F_oRbVRBHltcTW2FgSgDzgmOyYPHmbvpFj_qHhUcpWZlazGQgDuYtPW_0zIgz_x85H2vNw-hMTXnmqs7vZWl6yn4koZ3ngZWQ9wV9LtuRVy9OT3JZ49aFkPEsWdgSo73x_vrpoqtPAjlvr4Ro4REdZcsqkqysHfKwbU8pV2fo5LVANn9S1YVrBWXAeRflxzHhiAJ1ZttMdbqqj0DVgycf5PMBWQqERL8eISaYr41zXtrXMzsVVRbcpeYXICuEa5oNEsGFPciQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم ملی فوتبال از میدان انقلاب به جام جهانی بدرقه می‌شود
🔹
معاون امنیتی استانداری تهران: در حمایت از تیم ملی فوتبال کشورمان برای حضور در بازی‌های جام جهانی، آیین بدرقه چهارشنبه‌شب ۲۳ اردیبهشت همزمان با اجتماع ملت غیور ایران در میدان انقلاب اسلامی برگزار خواهد…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/435426" target="_blank">📅 21:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjryeLcJmlsC8CxUuNEgK6VTm8UmXA_KqRW6fjSws_9746Fv_AG9VSpi1t4Vh_tcq8wL0g2DyuZO-I4zwA_g2_ffT3N9sRHmht511aaWecY5vHDU2LQBf1Qw1SUX2Gvm9wh7XQDC8ZjDGrhfAdtojW34PxlSuIPFq56nnhAGl6uusvyJEaV1WC-ARCy-IXhdY5i1v2zh5sdor-xaHiMGY1CUCu5MOzJ3wgFpo-Uf3opm51Y4jzytYZ-LU5AVwSW_9oaj6d5PrkD-EwQSdFt-cxtD9JG_nme-o-JCLm4xHMCnbll4xzWLbXqWbu54Q0HeQos6Zi5KzWZ5EfZVdz2u6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعمیق روابط ایران و چین در سایه بحران‌ها
🔹
روابط ایران و چین در بحران‌های متعدد غرب‌ساخته سال‌های اخیر از جنگ اقتصادی و نیابتی تا تقابل مستقیم، همواره تعمیق شده و کارشناسان چشم‌انداز آن را مثبت ارزیابی می‌کنند.
🔸
«به چین اعتماد داریم»؛ این اظهارنظر وزیر امور خارجه ایران در سفر هفته پیش به پکن، پس از دیدار با همتای چینی است. سید عباس عراقچی در این دیدار ابراز امیدواری کرد که چین بر نقش فعال خود در پیشبرد صلح و پایان دادن به درگیری‌ها ادامه دهد و از شکل‌گیری چارچوبی جدید برای دوران پس از جنگ در منطقه حمایت کند.
🔸
در مقابل، وزیر خارجه چین ضمن نامشروع خواندن جنگ آمریکا و رژیم صهیونیستی علیه ایران، برقراری آتش‌بس کامل را امری ضروری و اجتناب‌ناپذیر خواند و بر تماس‌های مستقیم بین دو کشور در مقطع حساس کنونی تأکید کرد. به گفته وانگ یی، منطقه در حال عبور از یک پیچ سرنوشت‌ساز است و هماهنگی تهران و پکن می‌تواند نقشی تعیین‌کننده ایفا کند.
🔹
گزارش کامل در این‌باره را
اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/435425" target="_blank">📅 21:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435424">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cdd6667ba.mp4?token=sEGCFChGqsFj4RhKKpsrEjScyHn5iFuNqXlakt60hcQAYjhEvUkNC0x7T47upW5IUwDTs90F6-YYEYE8CIV9RTS87wpYTRbCP1KWtAaZBmruYBLLEBkQUP2SQTszzUdMeWLLU2mS-wGXtuhfwjgRcypDUTn9pmDKuNnRBaM8M_bSO_QoEoHHQrIKKtQZdNEVHXijZXrmUTxJxqd0aWhLHqE-7Qv0Ty6CtizUIdS_0T1HAAeeRsz8cDszbRWMu8jq7dDaSEgWmWy-9OVl113OMLS4kR4hMJOy9UXja0tF8udAj-niLyiTvBBSUBwlgLJxdGSb7OmDl--HQ4YO-pGzKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cdd6667ba.mp4?token=sEGCFChGqsFj4RhKKpsrEjScyHn5iFuNqXlakt60hcQAYjhEvUkNC0x7T47upW5IUwDTs90F6-YYEYE8CIV9RTS87wpYTRbCP1KWtAaZBmruYBLLEBkQUP2SQTszzUdMeWLLU2mS-wGXtuhfwjgRcypDUTn9pmDKuNnRBaM8M_bSO_QoEoHHQrIKKtQZdNEVHXijZXrmUTxJxqd0aWhLHqE-7Qv0Ty6CtizUIdS_0T1HAAeeRsz8cDszbRWMu8jq7dDaSEgWmWy-9OVl113OMLS4kR4hMJOy9UXja0tF8udAj-niLyiTvBBSUBwlgLJxdGSb7OmDl--HQ4YO-pGzKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برخی شرکت‌ها دوباره فروش اجباری کالاها را راه انداخته‌اند
@Farsna</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/farsna/435424" target="_blank">📅 21:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435423">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5577cb4ce0.mp4?token=iJosQP7_us6nhvCozS8Axg2h9oK8m1dPnE-3_Op6c7okIeDuOOQiAN0pQDq3IuPD79ZlfdvL5EFQD1XamZL0HKAXXI1onYYa3ux7qci87LefOJUfAhuiaejhGvCfXa_z6ivlySgFXjrxf3W8NkLEc2c7RB8AELSNinxu83i5YJOu-UjwU_hxddu94g8Rl2cIyWGzFO5P6pQDiQV7OuPAWdADUnEXQr9y6DHyRArVXwH82DvNe5r2lbR3f8Zyv_4PWQiAlKScy_59qWLKzz-MmE4iGT-5CPiqLuEIM-eItT3uQ9wiEcIZy2hqMuXNnYDBZjo68r5dQlp4nMRcmR66KTQSQ3vgUUWDfYqdSvilWrR7vEamK0U7whxQQJ-ER3uwbiy2W6yy35sL4rzXafI8ZNT1qGo0B-Fl5wgllKs0wCVNsG4Jii2iubcn1gYIkxCrYrhaXDV1zt_YRG-7GWFZh9dms0mLIAAt4224if0GfHCKWyaFNhUAQqNnETL12ksAF7JmocG4PWj4zK3YiqaUBsom_Pj4_Veqqbw_nuNwnKiwsLKN0D4Vplx2rDfEpOpN_ygdnYonvpF9FHfyBGYQfw_whqVeY28QOMTYRh3m86YtnigdrWIpzd8_1OEcD2eck_tzch1joxFovIAOOOelKpOPTwZFSX8p_Xdqp1wnNOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5577cb4ce0.mp4?token=iJosQP7_us6nhvCozS8Axg2h9oK8m1dPnE-3_Op6c7okIeDuOOQiAN0pQDq3IuPD79ZlfdvL5EFQD1XamZL0HKAXXI1onYYa3ux7qci87LefOJUfAhuiaejhGvCfXa_z6ivlySgFXjrxf3W8NkLEc2c7RB8AELSNinxu83i5YJOu-UjwU_hxddu94g8Rl2cIyWGzFO5P6pQDiQV7OuPAWdADUnEXQr9y6DHyRArVXwH82DvNe5r2lbR3f8Zyv_4PWQiAlKScy_59qWLKzz-MmE4iGT-5CPiqLuEIM-eItT3uQ9wiEcIZy2hqMuXNnYDBZjo68r5dQlp4nMRcmR66KTQSQ3vgUUWDfYqdSvilWrR7vEamK0U7whxQQJ-ER3uwbiy2W6yy35sL4rzXafI8ZNT1qGo0B-Fl5wgllKs0wCVNsG4Jii2iubcn1gYIkxCrYrhaXDV1zt_YRG-7GWFZh9dms0mLIAAt4224if0GfHCKWyaFNhUAQqNnETL12ksAF7JmocG4PWj4zK3YiqaUBsom_Pj4_Veqqbw_nuNwnKiwsLKN0D4Vplx2rDfEpOpN_ygdnYonvpF9FHfyBGYQfw_whqVeY28QOMTYRh3m86YtnigdrWIpzd8_1OEcD2eck_tzch1joxFovIAOOOelKpOPTwZFSX8p_Xdqp1wnNOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرانجام این جاسوس موساد اعدام بود
@Farsna</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/farsna/435423" target="_blank">📅 21:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435422">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8034f918.mp4?token=IxtXdF2XR7BOlFv-g-oQNkfo4JCZdgHTT9ZSFHeHQchx73qhWDS9fKUllzHt_Fq80DAzDHTzGU5o2ntaHvFCpq3i17XqcXkLvxptf66imcylZBJFVHto94yOvxxT9xvvvBgC6Omue8rf6jD_Qs0f2U5nSpuYNgyE44hZBZU3RvDt_Ap1pfmkQa_JyA_WEtxP6HgdWOXzfJ48CAzR3cXbkn18NUS-vn2geqkqRZf-tK5Wa2Xc7cBzy2nPoOAqfC4DGBsaL3rnVPPUey9ZuZHiv7htWzmavljvcY0e5_v69D9GEtohqogYNAkvquUP_exl-IUbTFEMdYnlAhF3CZGAVoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8034f918.mp4?token=IxtXdF2XR7BOlFv-g-oQNkfo4JCZdgHTT9ZSFHeHQchx73qhWDS9fKUllzHt_Fq80DAzDHTzGU5o2ntaHvFCpq3i17XqcXkLvxptf66imcylZBJFVHto94yOvxxT9xvvvBgC6Omue8rf6jD_Qs0f2U5nSpuYNgyE44hZBZU3RvDt_Ap1pfmkQa_JyA_WEtxP6HgdWOXzfJ48CAzR3cXbkn18NUS-vn2geqkqRZf-tK5Wa2Xc7cBzy2nPoOAqfC4DGBsaL3rnVPPUey9ZuZHiv7htWzmavljvcY0e5_v69D9GEtohqogYNAkvquUP_exl-IUbTFEMdYnlAhF3CZGAVoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر ورزش شمارهٔ ۱۲ تیم ملی فوتبال را به پزشکیان اهدا کرد  @Farsna</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/435422" target="_blank">📅 21:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435413">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_Mdyvmjq5RzzuYocUH_Zu-X3bvlxj6_KDm2h_OU8WnJ_QXpa1rgHXtvDkjAov9XpTMpflSsyd8f4ToKhmPIkgxv5QeYF5qtjSwTaQmeTEUTqnes4KTqf3DrDyEL9YDIYO6M42Z5hHiGhDl4f-G5iER6K-PpLsj1JFgLmGCcPC1vsf44Cgs-yep1CH_CQdrT9HgnIoDaoFg_tssnZSTGS0yQrRlMQxpwxCUJy74C22tO_FPNY4v2hvk6tZ9NbFcUpTk7rJtRvnPaBpOcPn9eey8L172Nu67-EF7I_rX2oSNmID8UxW2szdcKrbZEafzaMs-sjXR0VQq5zi7zJiYEhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای احتمال مرگ یا کشته‌شدنش نامه نوشته است
🔹
درحالی‌که ترامپ، در بحبوحهٔ تهدیدات امنیتی فزاینده سفر دیپلماتیک خود به چین را آغاز کرده است، افشای وجود یک نامهٔ محرمانه در کاخ سفید توجه رسانه‌ها را به خود جلب کرد.
🔹
سباستین گورکا، از مقامات ارشد ضدتروریسم کاخ سفید، فاش کرد که ترامپ نامه‌ای خطاب به معاون خود، «جی‌دی ونس» نوشته که در کشوی میزش در کاخ سفید نگه‌داشته می‌شود تا در صورت مرگ یا ترور احتمالی او، استفاده شود.
🔹
این افشاگری در زمانی صورت می‌گیرد که ترامپ در آستانهٔ ۸۰ سالگی قرار دارد و موضوع سن و سلامت جسمانی او به یکی از مباحث داغ سیاسی تبدیل شده است.
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/435413" target="_blank">📅 20:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435411">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkkiagilIhCnq6FR2jc5FgfySS9TuCYj01Fj0_-it48afqraF4RfuxMVTnv1x7bemqX--z69eiN3sTpDZhR749UIcSqSb3y4-NzmU6yU4z2mygTwc_QuUvAmjUuAYcJMbjgT-NrGOw1rxaueOLajPvu3xowgd0RqcAjzXJEa_t6hZ862ZFbvTdPhuES0-Me5O7hD632aY6HcKB9sRikpKomOuROBRpCQnWYiWX61UQvsJ00eQns-jmpvKCnYoTZAD32xvyM_V9Dly18Ct-mQbb-uWbUL90j9PaEE6qSS4RjhgbsFYHhW4bOIRzeoYK19Q5GpJiTWlbwtrz15oHsxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: اسرائیل علاوه بر گنبد آهنین، پدافندهای دیگری هم به امارات ارسال کرده است
🔹
فایننشال‌تایمز نوشت: «اسرائیل سامانه‌های تسلیحاتی دفاعی از جمله یک لیزر پیشرفته را به امارات ارسال کرده است تا به پادشاهی امارات در برابر هجوم سهمگین موشک‌ها و پهپادهای…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/435411" target="_blank">📅 20:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435410">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854ea55cf4.mp4?token=CTAfR8xRENrHk-6zIIgAMKRwQXt5BdkTHIFeCqKiNHu5KEUDryB11Ci1dZ2_Ey54XykqfmucfAn0APS1XLyVjD0hCQocRenLWwykXptyshFxAHK1XgxlJsjXWrhwQm0ZyEwVFMWvYII8jN_Z8f2GGsRFAnQqf9xmqtvbLRTtIEtVZPf75tfk8lNURQCOmDRzAyF6FS981cCwLvGy11hUpVN0lQrbdqTtsVqhdB6OiZa5kHxacqDlt9mh1ans_mRVFGgJDSNylrKZYlXnirpR6U0QgXPgA1wgaDjTyxht1mDKJhAIhbEmWY4_xPnlyfnsssKmykYQ7XInILuegd_qmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854ea55cf4.mp4?token=CTAfR8xRENrHk-6zIIgAMKRwQXt5BdkTHIFeCqKiNHu5KEUDryB11Ci1dZ2_Ey54XykqfmucfAn0APS1XLyVjD0hCQocRenLWwykXptyshFxAHK1XgxlJsjXWrhwQm0ZyEwVFMWvYII8jN_Z8f2GGsRFAnQqf9xmqtvbLRTtIEtVZPf75tfk8lNURQCOmDRzAyF6FS981cCwLvGy11hUpVN0lQrbdqTtsVqhdB6OiZa5kHxacqDlt9mh1ans_mRVFGgJDSNylrKZYlXnirpR6U0QgXPgA1wgaDjTyxht1mDKJhAIhbEmWY4_xPnlyfnsssKmykYQ7XInILuegd_qmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاج: تیم ملی فوتبال ایرانِ در حال جنگ است و باید این وقار را حفظ کرد
🔹
صحبت‌های امروز رئیس‌جمهور به دل همه بچه‌ها نشست.
@Sportfars</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/435410" target="_blank">📅 20:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435408">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZ4WYeOvJzTh2vdLO-a0Hg5sRXZN7R1X7lUpDZiMGExS86Anixj3JSQ_6wK94c99vYmFPySEEtdACq-4WmVkAifxjP_SJVgUZ6D-dpt3tYArdyj1KWcrCuvSlc5a71D1PW25xt9xZQ_LyQZ4_z7Lxk8SYalttB14lli8dmJwM-YaV3bYRhl553_3xCwr2G91vCUOl_fZruTCJ-F1qQCwr1mNamLhc-cxDBJIuoydqCu3mVvgLPNkqyzpWuXki9_A8ooUDwcKrD8b-fQfxQ7KNVbljQ-hvzyzUlbGBBLD5t2FRilOKL0vEBOYddFFFJ4i1JOvOKP0hC9fuSMdNf32Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام سردار سید مجید موسوی در بدرقه تیم ملی فوتبال ایران به جام جهانی
@Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/435408" target="_blank">📅 20:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435407">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مجلس سنا در توقف ماشین جنگی آمریکا علیه ایران ناکام ماند
🔹
مجلس سنای آمریکا برای ششمین‌بار قطعنامه‌ای که خواستار توقف جنگ علیه ایران است را ناکام گذاشت.
🔹
این قطعنامه اختیارات جنگی که قصد داشت درگیری را تا زمان تأیید اقدامات نظامی بیشتر توسط کنگره محدود کند،…</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/435407" target="_blank">📅 20:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435406">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc555bbe09.mp4?token=WS5dzyqW5nRayjUFCs9e8jVoYm30ZPTisAigPqHwq9e7zhoJuy5qNGfO16gzbFx8tGlqF7lnzDV8igLkraGDZWnVHnWoEws9G-PLxme5bs6tcDp27uq5tMuuGuYxGMvmOjn7s0h0ne30CSYTbqJSn5l4z__vf9fsgx2MftzhDgSWJwRwY3TWqxPLV3KOWreRwOl0XhyaNRaQ1lqDWranbGLttu8LsqWdBRNu8EPjy09yNcljAteCuOpk4GG6hOekiNdUa-wnCX7bdtNcOYGmoj-IwsMgS9XJi-_sRmgJJDmZfIxUdIOJt7Fwe6VFtgwhgk7ljnqPy184h6yvwZ6rrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc555bbe09.mp4?token=WS5dzyqW5nRayjUFCs9e8jVoYm30ZPTisAigPqHwq9e7zhoJuy5qNGfO16gzbFx8tGlqF7lnzDV8igLkraGDZWnVHnWoEws9G-PLxme5bs6tcDp27uq5tMuuGuYxGMvmOjn7s0h0ne30CSYTbqJSn5l4z__vf9fsgx2MftzhDgSWJwRwY3TWqxPLV3KOWreRwOl0XhyaNRaQ1lqDWranbGLttu8LsqWdBRNu8EPjy09yNcljAteCuOpk4GG6hOekiNdUa-wnCX7bdtNcOYGmoj-IwsMgS9XJi-_sRmgJJDmZfIxUdIOJt7Fwe6VFtgwhgk7ljnqPy184h6yvwZ6rrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اصابت موشک حزب‌الله به محل حضور سربازان صهیونیست
@Farsna</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/435406" target="_blank">📅 20:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435405">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p573izjdRFOzhClmXQiYsv-0DGw4MYG-Xljm5Oph1cbXlMlXzpxvbTX41YOBx0NnftddZUlFNrdvm_W7j5Fb1sHs_eqsRW17J5V8QAo6XcA5t7n1s6wU9HN8-uHjVuP-TRAwzUFzTSCSHEPuMLrbp3lvY2L-0p0TBJ1JDILlgWiKzhV3obw25io5CU6TkxEi9lUWu5hrdi6s4ERT2pzPNGvFC5ZkTGZUzst3L5UWG69POdrMAaVRl4nlgv2Se5WlmsJqCNGg01q5Nk252a9Ox7e7kD4xn4m5IVux_Sy7e0wup61RJxdWf2KK_M5hGkfBnO_afSKHdCNP5yTRbVCVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزارت خارجه ادعای کویت دربارۀ ۴ شهروند ایرانی را رد کرد
🔹
وزارت امورخارجه: اقدام ناشایست دولت کویت در بازداشت ۴ مامور ایرانی که براساس اختلال در ناوبری وارد آب‌های سرزمینی کویت شده بودند را محکوم می‌کنیم.
🔹
اتباع ایرانی بازداشت‌شده باید مطابق قوانین بین‌المللی…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/435405" target="_blank">📅 20:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435403">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e9154898.mp4?token=rJqDkC8tV57Q09-yoKb9lFMVSsVvKQfArtW1EL3h6_57b3wDGY6xyniKdKtHO842mMxfsFwreoPZ9S5OEj-OaNu6R9Z2KqQANQxH4jfmT5Bdz8zaAc_Wl3JDK29U22z6qSEYeJpONrKvroWU2hDDatf9oDUzIRkEgrNxnsseG3CazzuVDOXJBcEOVgy81NkOQxn8Lcuq9A5xTB8yu3AoKdM2--Sk5R23hXxjD20w-VxEendriwlWsB0os6RiY7NkYR-p1F7hI6QZpteU0xMloEOSq18BY0LUuZl6np_s1326B8ssDWq5SQ9uot73m5zMmoDYZWBq_6ggyOtwnDmpC3Ef8uebUV5geep-xKVoZ2_gGP5LLqQSOI6OVC5aKuwFp6QYcNUvaiPmFA9qbJ28SM3YQ0f4ScK6GIJDKzmn7hxOw9NBnB6wqeukLF1teWQgWI5pDec4mZA9_Z4D_OtNSKtf1ku6Np9OUcYsPQPiR2jXGC5VWI30PZXhnzlW06yjcueH9QOMmNoa77vOngLKjsm9ku_FWa09jFe13nCuUeBisvPAd1QWPAMeahoMPSLIV7FGqcoAzRl28KHn2oJMh8qZzt-C00O8CniSidAb9FuIqf5EmB9r3O9Js8wSDcmSyhrys9Io4eHR1TwodHveoFdVFoc4sreCgSNL0QigcFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e9154898.mp4?token=rJqDkC8tV57Q09-yoKb9lFMVSsVvKQfArtW1EL3h6_57b3wDGY6xyniKdKtHO842mMxfsFwreoPZ9S5OEj-OaNu6R9Z2KqQANQxH4jfmT5Bdz8zaAc_Wl3JDK29U22z6qSEYeJpONrKvroWU2hDDatf9oDUzIRkEgrNxnsseG3CazzuVDOXJBcEOVgy81NkOQxn8Lcuq9A5xTB8yu3AoKdM2--Sk5R23hXxjD20w-VxEendriwlWsB0os6RiY7NkYR-p1F7hI6QZpteU0xMloEOSq18BY0LUuZl6np_s1326B8ssDWq5SQ9uot73m5zMmoDYZWBq_6ggyOtwnDmpC3Ef8uebUV5geep-xKVoZ2_gGP5LLqQSOI6OVC5aKuwFp6QYcNUvaiPmFA9qbJ28SM3YQ0f4ScK6GIJDKzmn7hxOw9NBnB6wqeukLF1teWQgWI5pDec4mZA9_Z4D_OtNSKtf1ku6Np9OUcYsPQPiR2jXGC5VWI30PZXhnzlW06yjcueH9QOMmNoa77vOngLKjsm9ku_FWa09jFe13nCuUeBisvPAd1QWPAMeahoMPSLIV7FGqcoAzRl28KHn2oJMh8qZzt-C00O8CniSidAb9FuIqf5EmB9r3O9Js8wSDcmSyhrys9Io4eHR1TwodHveoFdVFoc4sreCgSNL0QigcFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
آیین ملی شاهنامه و هویت ایرانی  عکس: زینب حمزه لویی @Farsna</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/435403" target="_blank">📅 20:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435402">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
امتحانات حضوری دبستان‌های استان تهران لغو شد
🔹
مدیرکل آموزش‌وپرورش شهرستان‌های تهران: ارزشیابی نهایی حضوری برای دانش‌آموزان دبستانی منتفی است و نمرۀ نهایی براساس عملکرد مستمر کلاسی توسط معلم و تأیید مدیر مدرسه اعلام می‌‎شود.
@Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/435402" target="_blank">📅 20:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435401">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0098b7a4ad.mp4?token=XtNpdMVU30sL1a8CSFTm-F8mMAtQcnXvLIR3uAwTizJFjGZtf6S6HiAEcNLL1WKfNMrUZ9yd2jQKpkkIBGY_uTRTSn2WPpqKh4_xzsmF6ERuLnh-A-Nr5O6a9NzvQ8F8oWsUTBjGDOoXkp7jWcTyJu7n7QzKrXanfP4CmbMEtDXNRO1BLVK5f5GehNemaf4F7ToGYvC3TmemxmIAlf_he_dD1ny8dZvhuQIZWFXy4K8W_rKrvsPkrXqaJrbUwCnfziavwEBb9UFKK8jr4X40eSk4UhsIXxCLMsia5ks6oQAcRrcxJJZQeS2VIMNmPXu_oRfGxt6OzB_Wqnjp2esiLk8YVPLAS2tFXNyi9cLD9xQC1D0R10ZJsx63AJpLrUwVZ4OWVjgHatFNzrO6kQjqNHQ3ioNa529Ru9cMiiq_lzJr53tc3AN_n3yLddt_b9gRCybhwhMLpKc9Ol-PXToKdf3mUsqo8DyFsptHhn-NGJkZuIO96jWUgNSMGQnkp7cSayI-QxOLFV_oP-6Y3BRMacs4bac1iTSJPQ4KaOEAblBvmkb34HjK9XjnwGmpMs52R87vGODJIlayt3V3XAkGSNteos63BC68LoKqxczW8RHcYosXeXl15ffHre5cC5Lv2JzE7mZ4cpdHF1ioM7P9H3YMcrPUM550rfPtWpHvwug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0098b7a4ad.mp4?token=XtNpdMVU30sL1a8CSFTm-F8mMAtQcnXvLIR3uAwTizJFjGZtf6S6HiAEcNLL1WKfNMrUZ9yd2jQKpkkIBGY_uTRTSn2WPpqKh4_xzsmF6ERuLnh-A-Nr5O6a9NzvQ8F8oWsUTBjGDOoXkp7jWcTyJu7n7QzKrXanfP4CmbMEtDXNRO1BLVK5f5GehNemaf4F7ToGYvC3TmemxmIAlf_he_dD1ny8dZvhuQIZWFXy4K8W_rKrvsPkrXqaJrbUwCnfziavwEBb9UFKK8jr4X40eSk4UhsIXxCLMsia5ks6oQAcRrcxJJZQeS2VIMNmPXu_oRfGxt6OzB_Wqnjp2esiLk8YVPLAS2tFXNyi9cLD9xQC1D0R10ZJsx63AJpLrUwVZ4OWVjgHatFNzrO6kQjqNHQ3ioNa529Ru9cMiiq_lzJr53tc3AN_n3yLddt_b9gRCybhwhMLpKc9Ol-PXToKdf3mUsqo8DyFsptHhn-NGJkZuIO96jWUgNSMGQnkp7cSayI-QxOLFV_oP-6Y3BRMacs4bac1iTSJPQ4KaOEAblBvmkb34HjK9XjnwGmpMs52R87vGODJIlayt3V3XAkGSNteos63BC68LoKqxczW8RHcYosXeXl15ffHre5cC5Lv2JzE7mZ4cpdHF1ioM7P9H3YMcrPUM550rfPtWpHvwug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن تکلیف فرشته‌های کوار فارس در اجتماع شبانه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/435401" target="_blank">📅 19:59 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435400">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حزب‌الله: سربازان صهیونیست‌ را در کمین گرفتار کردیم
🔹
رزمندگان مقاومت موفق شدند با استفاده از تسلیحات مناسب، خودروی زرهی دشمن را به‌صورت مستقیم مورد اصابت قرار دهند و آن را منهدم کنند.
🔹
پس از انهدام خودروی پیش‌رو، یک لودر نظامی که درحال بازگشایی مسیر بود، هدف قرار گرفت که منجر به توقف کامل تحرکات دشمن در این محور شد.
🔹
درپی این درگیری، نیروی هوایی دشمن تلاش کرد با اعزام بالگردهای امدادی و پهپادهای مسلح، مجروحان خود را تخلیه و از عقب‌نشینی نیروهای تحت محاصره پشتیبانی کند، اما با آتش پدافندی مقاومت مواجه شد.
@Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/435400" target="_blank">📅 19:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435399">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b211685ea.mp4?token=XsDdJr32f1I_XhbtnGTV8N9XlaWXncqkVGleEmysyjo0YwkT_9_wUOSYkYGf1piJeSnNf7KuFKPVaMbV3xGird_ZbpVSSOIS5Xro4K84BVarUlO-Iutembh2hmsKWorLfbw7hXaWQUQ1j8C1Oq2U6AAMnq-8KU_41Eqhq-3xCLFgLssc7jDRs7hAYjZq0L7LAY6Bhp_tep-RpdkdTJG7p2XYCBhtTduYB_15DeAW5Ral0ZldmOeW0GbXYbdnVJ7lABb0XzqR3LjLTHv7bcaV76uWgQ1ndXsnkQXq8h53-sxGY14y8rqTZ3T2rN1CJ4t222I4Cfh7s1yVzdXMgpYlkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b211685ea.mp4?token=XsDdJr32f1I_XhbtnGTV8N9XlaWXncqkVGleEmysyjo0YwkT_9_wUOSYkYGf1piJeSnNf7KuFKPVaMbV3xGird_ZbpVSSOIS5Xro4K84BVarUlO-Iutembh2hmsKWorLfbw7hXaWQUQ1j8C1Oq2U6AAMnq-8KU_41Eqhq-3xCLFgLssc7jDRs7hAYjZq0L7LAY6Bhp_tep-RpdkdTJG7p2XYCBhtTduYB_15DeAW5Ral0ZldmOeW0GbXYbdnVJ7lABb0XzqR3LjLTHv7bcaV76uWgQ1ndXsnkQXq8h53-sxGY14y8rqTZ3T2rN1CJ4t222I4Cfh7s1yVzdXMgpYlkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی در مخازن نفت شهر «مرسین» ترکیه
🔹
این آتش‌سوزی تاکنون یک کشته داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/farsna/435399" target="_blank">📅 19:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435398">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad1ca7b77d.mov?token=oEvsBCrNTUTkPk6Qd2i2tFtZiMREqofL7-ncfqOs_RvJW6L2OenV2ZC6oy0twati7kjgqswTP2dscBtd6bV_mlM64InC0ky4AvBcVmvOumiTir17PSq9P7qmM6s8hEM-UdhyJ4Rn57YvsJv_LQOOxw-VWwlK1ADvGRn8Ga8ijXE13e1V8c3zbMnM6tT_im26Zndr90SCT7LnJ43480fC0as4hKgKfBqnsP7zkvumER-EUL1HCumsl21Ivz1WJeCnjSU5WsTlbaKGqla_dr_zMNrZjjOxJ7AEed5HsCkiluUjHPJ37Zio0X2Aw1TsEA8JyzmKEfc6dJ3rhL_6qNtRqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad1ca7b77d.mov?token=oEvsBCrNTUTkPk6Qd2i2tFtZiMREqofL7-ncfqOs_RvJW6L2OenV2ZC6oy0twati7kjgqswTP2dscBtd6bV_mlM64InC0ky4AvBcVmvOumiTir17PSq9P7qmM6s8hEM-UdhyJ4Rn57YvsJv_LQOOxw-VWwlK1ADvGRn8Ga8ijXE13e1V8c3zbMnM6tT_im26Zndr90SCT7LnJ43480fC0as4hKgKfBqnsP7zkvumER-EUL1HCumsl21Ivz1WJeCnjSU5WsTlbaKGqla_dr_zMNrZjjOxJ7AEed5HsCkiluUjHPJ37Zio0X2Aw1TsEA8JyzmKEfc6dJ3rhL_6qNtRqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی برای شرکت در نشست وزرای خارجهٔ کشورهای بریکس راهی هند شد.  @Farsna</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/farsna/435398" target="_blank">📅 19:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435397">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
آشنا: سوییس که به ظاهر آرام‌ترین کشور جهان است، قوی‌ترین پناهگاه‌های اتمی را دارد
🔹
ما بعد از جنگ ۸ساله نباید پناهگاه‌ها را از دست می‌دادیم و باید آن‌ها را توسعه می‌دادیم. @Farsna</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/farsna/435397" target="_blank">📅 19:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435390">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LVSR9xcokH8XtIHWVu3ROWG6J7Er1h0x2yRfhYtTinz5_R31j4qaEo6SUWsRuydXevkYG21rQH75faNGoEoxHcWB4qs41Nc0jlFSMPm0fqSNsK4CjtsNEZuGWE-7ORUplF5YPE6ng7quA7EvkJGJ3842Ln3umbZose_tr0UVxhlcGjSi6HAA9LmGYlZ7Q86tShyN9k8hArlJZNNWDNlEnKuRaf4GUfr4JzbkudWQ_Xv9s8cnPkJCvNFNqFyqJ-KDADsq0QigM8hDrGtyxh08z5NIfX3R3ECvrWH8DMht0mfryD5x9YSJFp4LjZaSOmPxjkSn101rYgdaWtoCLODLtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzF2_cPGIC79LcehKDQrvaugF-urgy5oJ9Fr3w6J1i0826GOvEV6mV-ITpW6WG44-uYWcSSU7aox0IK8cG5ItVs_iqNhkxY0sNrbRwaXofuBsbjz0jAeu0-E9fXn69_kM2HYD2aCH8tUvwQ2pY3RE_HI69UR35TTE4RRcIvokr0fQOtOqZBgfgn4FXkQMks8sVdnVM0ZZM0uu4_R9kWtRDos0RZSs5g00K5CRHfdt3oiFeXXvJlnzr95t9XXCsrLX_g_-YSHuwG2tHfAS-l6PKHF5arqAmsQN0h24liUqZusCkoOlA-MDnqCiv9MYoy6fVNiT500Q1l8GGLAWCuZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N4fDYPvWd52bJE3NdVEqWz1ZC5dwgZZJCJ0T6_oJ8pa-NfyXj80JrEptO7F2QHPX9IGSE2G_rANf1HyIiRQshEjqzX5Dn8xIbodxvyFa60HhEviZz7sQqaM2_ewu1wwgNSpUtfp8f1I3mdGFUbii5Cn9hPrLED8RBJafZq8yNYvHcN0hnMjBYMqE12A5FMtCDr5qkiyrFzeZDO9zgV8a6jzJSXFdvJT81lPct7YVciXy9ZgbmKtN72U0Z_PoDUD0Qh9DPQ4psmjlIMFRQ3VLZ2FiJXP06EtSeuz4npMfNLlBBKJ0eL6UEXUL4fdJGFfCY7vIh3IFBbN35zmRl0236w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UDtl-maz2WOXxj5yFLIhN2OwwVyQZlznR1E8T-Ol_IZVgEbw72VA2o_XpmWL7hcTtedlkXrIRzJ1roWZnD_qUrIlJWmPotytMDwPEIdDieU961_B1lHpmSpYeq1vOo6QaSDgKLrC6qBxNEpoTlL_cO0HRmT83QXrXEMkI5cybicKzFFdyZ5KQIhFEo9T62qhV7uG85RqRT3udzxppEIffwcGOV0TeC07I1KOBY_7Gp5f6Hveb72_GQBL-rlThX50FJfwk5qViIEgCSKSiixSzTLBmf0T2NcwvzTwgxAAo9zWrZAWrmAwkMgTDIx09AvKBoCNIUqlG14iJBooWhzqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOjx-NW5S6aoZvW5htelhk4edIKNWZA32Ilj2IJhyR4iKPmaTanFeBj7WXSuOQFSfUz9lEBs4tOOwCWdB1JSGaSOyMNUxoPXKrMnBWTeqftPOLFJkUQgfxaym2Ak7AbVOLnmEdXPACa3FDYsS83asPJiM_H48rlR6wchmmdusKskNmfA1DJrx_qcuxJ_taen5pJUONr0zfaQTKekbXK3n9Qiy_Ya1xxgle_kLE0u9s9ACfyLr64TtxzpfOLnsen1mBaTkyQdk_xJamxZ18cXkRjAMKjTxcosKP9qMpUSjOHvUx3rHmf6upYyfH58zWht3LdGEPf2_wQ5a1izF5yKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVjfAtBMajmHvh0zyMMV2Yl7DePJ-vi5ndo_yXibJXEio1Oz73HcSsDZbMa-A3F2j0DOTzz5jMMNRhMES9Y9PELIgefCU1Cpgq8ZxAa3Nnsf1kViguIR8b0jrU3-w7cUz5Rv46qPRyEp_hQ-9jOR0XH3hEZolTvl7Qfvf_6K8ho3vt1v-pJvgp354m2TDLXr_A9P08pqbC1KVdykQPCpEjfC5tS2Jz4fEOVMY2rhGbtEznZDiswbB4569D414SvbDYfgI3n3wwRn2BAlky1-u0__o3SibGV5G3VQiwFV3TM33n51aLBvd0XZ2YSgPtRn-lu7MmiWJHwUMElMWOX-fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUw4FU6iVQmwQBEBEEnT9O62wCwgi8fYz2n8H5Y6E0JsSmcb_gsGrzd029_EVyLY8Pqliqu6ch6IQv2AwxJ-y0Er4fb5WpcX247C8JDPIoAkdSssX2MFndZLwKg8uDFcbfpK1tmSVVeOE8OSS0ANhx-9yX1yaXx8kQrxgcQiKL_sRT8-Nd90Grb2zJfn5DbPKZSLn1XL_ndxxXQ8RiwNcGk7saIUxUa-ibf2rv6uFPAzSLYpFur7-1RK-mZ42bSR7p3V-1_5dIR2ocQMVvlBXDLHp5hUVw-2c2szjjGgI4TIli6ccmJPfS4fC4iSZeHNIwXA81zJJ5DuLhEwaEzFNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین ملی شاهنامه و هویت ایرانی
عکس:
زینب حمزه لویی
@Farsna</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/435390" target="_blank">📅 19:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435389">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwN5xsPt-OKyO0mfx5QldbtS0wI7581ODZuQVfaXpagFX9GcBAR3RXo2zPUH_yaDXddSwGM1NXeWEqtzd9hKODWkA4pD0iDYUG5Dsc9uysoGw3VaMmzpWD-F3wDhZL8-5gsevluOHiPDWfxzM1vTZilNTt8-h40BKrCR3tki9417iRg8kP6bn0dIvR4oEt2quIA5UMG2xlGEfk4Qf3p9A5qy5yOB2gvUBjuWKEPYsY1bA-1dOaB-Wf6DJ5wNnDfepokqmySgpoHQSTH-rQ88BD8jxSpYg33q5qU0OTPAbki1qxQ14_3tREUcqSuUuViFm9l5mAsgkrS_jvj-h76zYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیپلمات آمریکایی: اعراب بین ایران و اسرائیل یکی را انتخاب کنند
🔹
سفیر آمریکا در اراضی اشغالی خطاب به کشورهای عربی حاشیه خلیج فارس گفته میان اسرائیل و ایران «یک طرف را انتخاب کنید. کدام طرف را انتخاب می‌کنید؟»
🔹
مایک هاکبی ادعا کرده که اسرائیل «دشمن طبیعی» آن‌ها نیست و حتی مدعی شد که اسرائیل قصد نابودی آن‌ها را ندارد و «نمی‌خواهد سرزمینشان» را تصاحب کند.
🔹
این در حالی است که بسیاری از سیاستمداران صهیونیستی به طرح رژیم برای اشغالگری‌های بیشتر و پیگیری پروژه «اسرائیل بزرگ» اذعان کرده‌اند،‌ طرحی که شامل چندین کشور عربی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/farsna/435389" target="_blank">📅 19:44 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435388">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884ab33e4c.mp4?token=mmT5hNlDDx1b_s1ai-x3R2jdD5zFmM5ALGx-8FX0vZ5aKHnSCKxwkkBYU2Mfalv0ui6eoGLc57Nt31JatIv2J9lzeJrlBe10DrQFwaES_NpaOPn8ezZR8EGsSnzZFatirEA8d_c-63vlxsh-61ZcLxCOS5URELOf2uOza0kXFUGmj5gaYjMChwtAFHZfAxFg002fDQU2njTVABqr805_JopajAR77Q3jJY2HxJLvlhGVd9wzp6bRykMPYdEV-uEodzblIdxGmyAauU8DIP533CT7D33LvYV87PJz7o06119lqItCZj0sP_oQt_3qjk9XG-bx-fB8qyAUMB2Wvegd3wpFn83INl-8KB9EUk5JUqhglQw4u9PCfk7rxdwj2qbeCfLr-79WNZwRFMW4VDM-Gn8VG_FufNHqBUnsx4pW9hil_5tRmihmuPdUXAbTQC6xYOj69tgGwxe6CIQMPkexAbFLBEEKNzoddHD2o0rd1aP8Akthg8AyhxmYOiqA2YEwaIenOy2KbCCRz_RBJ-UnBDBj1Gcyb-C5MlR3O3EnTmsKcPERbAhltV8h7zfAhFYHuXXvODl0dr61bHiove5HTuiKh12NI6icNPwkZRAYpJrzVfVTVhOxZqxPET8EbSEjvNeJuLMM-6KtwmT8wcgzvQKAcHvVvPK2DWL9Iri41IU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884ab33e4c.mp4?token=mmT5hNlDDx1b_s1ai-x3R2jdD5zFmM5ALGx-8FX0vZ5aKHnSCKxwkkBYU2Mfalv0ui6eoGLc57Nt31JatIv2J9lzeJrlBe10DrQFwaES_NpaOPn8ezZR8EGsSnzZFatirEA8d_c-63vlxsh-61ZcLxCOS5URELOf2uOza0kXFUGmj5gaYjMChwtAFHZfAxFg002fDQU2njTVABqr805_JopajAR77Q3jJY2HxJLvlhGVd9wzp6bRykMPYdEV-uEodzblIdxGmyAauU8DIP533CT7D33LvYV87PJz7o06119lqItCZj0sP_oQt_3qjk9XG-bx-fB8qyAUMB2Wvegd3wpFn83INl-8KB9EUk5JUqhglQw4u9PCfk7rxdwj2qbeCfLr-79WNZwRFMW4VDM-Gn8VG_FufNHqBUnsx4pW9hil_5tRmihmuPdUXAbTQC6xYOj69tgGwxe6CIQMPkexAbFLBEEKNzoddHD2o0rd1aP8Akthg8AyhxmYOiqA2YEwaIenOy2KbCCRz_RBJ-UnBDBj1Gcyb-C5MlR3O3EnTmsKcPERbAhltV8h7zfAhFYHuXXvODl0dr61bHiove5HTuiKh12NI6icNPwkZRAYpJrzVfVTVhOxZqxPET8EbSEjvNeJuLMM-6KtwmT8wcgzvQKAcHvVvPK2DWL9Iri41IU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دنیا به ترامپ می‌خندد
🔸
وقتی ترامپ می‌گوید «ایرانی‌ها دیگر نمی‌خندند»؛ اصفهانی‌ها جواب او را این چنین می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/435388" target="_blank">📅 19:38 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435387">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357902fec0.mp4?token=DkDA5j6HMd1E16jOf_ruI47D84zu6dZrrY4nykBpP7wAJFBQWJk6RyYO2Ag57Gfq9SCtNjVPCpaQK5glvLe7yG16l9DtAmpZRYH6bseaIngNOzreACXNAIiPdsrWzSGIWpOQQxnlDQu2lUVoTmtVuwTnpkNsYinHUfpcizQ92Pm0NUfCqLpiSgGQy_CYcUBWqbwj2RqhUJXKy5nUmjG29oKbrJ4I1jtnHZ6XKf9oAadAVefugkQstrIH-2iLDzXhrtr72aICADQ46z7yzczutmzTe8RNDlvUbkAKOj8qwOdIsSk-msGr4SSGFKmEmuiwvKrV-Bwuh78Dr2DdSyocLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357902fec0.mp4?token=DkDA5j6HMd1E16jOf_ruI47D84zu6dZrrY4nykBpP7wAJFBQWJk6RyYO2Ag57Gfq9SCtNjVPCpaQK5glvLe7yG16l9DtAmpZRYH6bseaIngNOzreACXNAIiPdsrWzSGIWpOQQxnlDQu2lUVoTmtVuwTnpkNsYinHUfpcizQ92Pm0NUfCqLpiSgGQy_CYcUBWqbwj2RqhUJXKy5nUmjG29oKbrJ4I1jtnHZ6XKf9oAadAVefugkQstrIH-2iLDzXhrtr72aICADQ46z7yzczutmzTe8RNDlvUbkAKOj8qwOdIsSk-msGr4SSGFKmEmuiwvKrV-Bwuh78Dr2DdSyocLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آشنا: در جنگ ایرانی‌ها فهمیدند عجب چیزهایی دارند
🔹
وقتی پل B1 را زدند ناگهان ایرانی‌ها توجه کردند که ما چه پُلی داریم.
🔹
وقتی مدرسۀ میناب را زدند متوجه می‌شوید که در مینابی که ته ایران است هم مدرسۀ کپری نداریم.
🔹
در جنگ است که شما می‌بینید شبکۀ برق‌تان را…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/435387" target="_blank">📅 19:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435386">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86a5b68eb.mp4?token=eferSD8bKm_252u625C4-GPx2BmHFf29b2dhw3IzQQ4-3haaMTeTInJj7Zr1w63vgxU8Zy559M_dZJAE5TxbaYI_SzRvCdBnwaYyn0S7Ev_kK4v0sEPRmk4djTtj2PwXlVFnXm1whKraBjpdZIuvfTqCCuv1L0wwlJBK9-i789Tw0wHSHR7U5xpi5aggZ68mDfZfMIyvtvMksKdx7QX2kLcBdq-EwmfJzyqgQ0Cjg36cCZpjcELk1R2qdeKx4lXjzKJWhljdOmTV0fVIL8pDvF8JJsNMC_znh6zhOJoYm71HHH8TXTKjbhVNXUrSck8KssnVSQ4bUY-TWX-_Jx6aSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86a5b68eb.mp4?token=eferSD8bKm_252u625C4-GPx2BmHFf29b2dhw3IzQQ4-3haaMTeTInJj7Zr1w63vgxU8Zy559M_dZJAE5TxbaYI_SzRvCdBnwaYyn0S7Ev_kK4v0sEPRmk4djTtj2PwXlVFnXm1whKraBjpdZIuvfTqCCuv1L0wwlJBK9-i789Tw0wHSHR7U5xpi5aggZ68mDfZfMIyvtvMksKdx7QX2kLcBdq-EwmfJzyqgQ0Cjg36cCZpjcELk1R2qdeKx4lXjzKJWhljdOmTV0fVIL8pDvF8JJsNMC_znh6zhOJoYm71HHH8TXTKjbhVNXUrSck8KssnVSQ4bUY-TWX-_Jx6aSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بزرگترین اتاق فرار دنیا کجاست؟
@Farsna</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/farsna/435386" target="_blank">📅 19:30 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435385">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c03f1b81d.mp4?token=XypNkQwAsPaUG6iw4lRcbvvGrnPaFVl4bLRrXEr2Q5f_psfkJLYiRAkQSr3_OmFjSafNbRXwbhrDAN36zmllqe0DzkAMez3hV1BvYaxOePtsTxveC9jyrHTu-WlJIudoBac82STjDLpSJAuVx0zW6HdRoxUp9dbhwqGwRMgNLOIAydFn4t1TWkM23lhO9Xx3-RfHiFeWm6XH6FVISJBuMH3SXcMeZc3GR7ObThiQkbImeFW7y4Zevk5-1HFJ8HS1XSCYsN3bZt0c5b8yGYTzkAZjC9i7YE1WDMC03_QP9x3eLGYbwZ_Res3mASTeQe0PDbGm07zPcgriHMUYWh2u5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c03f1b81d.mp4?token=XypNkQwAsPaUG6iw4lRcbvvGrnPaFVl4bLRrXEr2Q5f_psfkJLYiRAkQSr3_OmFjSafNbRXwbhrDAN36zmllqe0DzkAMez3hV1BvYaxOePtsTxveC9jyrHTu-WlJIudoBac82STjDLpSJAuVx0zW6HdRoxUp9dbhwqGwRMgNLOIAydFn4t1TWkM23lhO9Xx3-RfHiFeWm6XH6FVISJBuMH3SXcMeZc3GR7ObThiQkbImeFW7y4Zevk5-1HFJ8HS1XSCYsN3bZt0c5b8yGYTzkAZjC9i7YE1WDMC03_QP9x3eLGYbwZ_Res3mASTeQe0PDbGm07zPcgriHMUYWh2u5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیوارنگاره میدان انقلاب با تصویری از ملی‌پوشان فوتبال
@Sportfars</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/farsna/435385" target="_blank">📅 19:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435384">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375e2c0d3d.mp4?token=n2tznFyQXI2NcUfoA-g7FW08jOvvsGm5CLKKC2PLKel0cajp23AkAnCGacUQSnc9SSmAua8pLBw3mTEUiyt-umIIFoQMOp7S0jphktFTBCbK05520Vr133DWHsKgiGwgxYW_nrth0PMQHsJkxhOTVU9nTaY_mFQQAajUCGtnnGkAC1Ewvl4lzwlqrN4G8WZi9j8cDuXr9pgb2zkEFlHdpgJZ10Rpz-EN9zMivhRYy4r_SU6QUotgvf3jN1Jk4FscwAX2GNXZBfeFqPTgcwntvz8TUPNEtuF7Zk4zrKUqLEB53JYMkXz7qRcOqhIkKd3EBH3N3E-v_KWqGN_qZYRzPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375e2c0d3d.mp4?token=n2tznFyQXI2NcUfoA-g7FW08jOvvsGm5CLKKC2PLKel0cajp23AkAnCGacUQSnc9SSmAua8pLBw3mTEUiyt-umIIFoQMOp7S0jphktFTBCbK05520Vr133DWHsKgiGwgxYW_nrth0PMQHsJkxhOTVU9nTaY_mFQQAajUCGtnnGkAC1Ewvl4lzwlqrN4G8WZi9j8cDuXr9pgb2zkEFlHdpgJZ10Rpz-EN9zMivhRYy4r_SU6QUotgvf3jN1Jk4FscwAX2GNXZBfeFqPTgcwntvz8TUPNEtuF7Zk4zrKUqLEB53JYMkXz7qRcOqhIkKd3EBH3N3E-v_KWqGN_qZYRzPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آشنا: الگوی توسعۀ ایران کاملا نشان می‌دهد دولت همواره نسبت به گسترش خدمات عمومی به دورترین و محروم‌ترین نقاط توجه ویژه داشته است
🔹
ایران تقریبا به تعداد تمام استان‌هایش فرودگاه دارد. اگر الگوی توسعۀ ایران چیز دیگر بود می‌گفت تمام پول این فرودگاه‌ها را در…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/farsna/435384" target="_blank">📅 19:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435383">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDBwS9sXbCuTvH4KGR8yE7PHOYVvnFq8Pt08k6RiTngZvQzxWG7sSYc-0je7DAPwS1zNWcIsYxq2mYKKO42jc_cdbXbyU_Po-igAX_O3r9Rh4g1oxqFbgHNQ2-5Pwe-JrhkkbHfKpGL2gAtG1r32Ee2w0M--7Ts8kYHN7-OHgXbTp_zF9xqqnzprT1wKAACAFxkQDMyGVR3r2G3WDQ7zTGFmdiUgJYjkiwYxD6SBjjmTZr4Z5ltIVFeS6ByI7RSXqMLu9xdI4j1InVIWijoBOeTQZey5RNnmSL35ipT6Pf1O1u11XguDviZTq1e3wmBjoXZGPEm4vKX7F6g7hfykew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: تابستان خاموشی نخواهیم داشت
🔹
عباس علی‌آبادی وزیر نیرو: با همکاری مردم و افزایش ظرفیت تولید، وضعیت امسال از سال گذشته به مراتب بهتر خواهد بود و امید است تابستان بدون خاموشی سپری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/farsna/435383" target="_blank">📅 19:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435382">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/966f423d72.mp4?token=LUqHBuy1-OA33T6j14zIAkAXvbk3hTy-uJ3HsBVYsc7mQrr_ECkTH_4531tBsQQf-xV_56xkM-jhYgKrByZiRE3xZ2ltCXlX3Gu5x3W4loOI0Wdv_wSoGNJ00cDrl2KpzTmKRgrPcv6wPBoBkEGnq0gTCaEuLYNCEng5tCrWadZKtuCBEt-OpF3ARMd4v6caKIJzmfA0k5kwiR6EF2-5EuGBI41loMkf7MjBUV76NTjXD7vEbMdWt7zjkoaXx-5VkzygB1N0OKGrJ2lvDtF0apVm0z5_0k_CCq5tf5zo-3Wxh_pLwxZtpOrBET6NjPje1JlEUxSUNKj8ur64sN4dYhkL5xqnZq7ABhoUFRlmLWhb3GG8sLz_AwugK38Grqwx5uB1ZxxzZZYRdUBL3k2wCR3ROkAsjpr0vZ-u_SoZ8de4BgAHv_7yxxOAiTirs0VpzRCXW-4Fs-ZaMEU6VN4mqBZsyknpO75wOLtH5GyMqGnuq127-hq_4Vxgh1PV0aAWuRmq8Z_y68K5DkvaxEgPxeyVbMtAh_KC6ormvCC0EmJVv_1sO7O53xJqGI2PlGUnpQhdtLWYOkjif6jhwF6H7CQetoMC8_WuYeroGX697q9xnQd9ritsr0o9IKwQvzqvQALP3VDxzCZZdCZinMidNSy5-5ntjvJiJj_6sA8aDeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/966f423d72.mp4?token=LUqHBuy1-OA33T6j14zIAkAXvbk3hTy-uJ3HsBVYsc7mQrr_ECkTH_4531tBsQQf-xV_56xkM-jhYgKrByZiRE3xZ2ltCXlX3Gu5x3W4loOI0Wdv_wSoGNJ00cDrl2KpzTmKRgrPcv6wPBoBkEGnq0gTCaEuLYNCEng5tCrWadZKtuCBEt-OpF3ARMd4v6caKIJzmfA0k5kwiR6EF2-5EuGBI41loMkf7MjBUV76NTjXD7vEbMdWt7zjkoaXx-5VkzygB1N0OKGrJ2lvDtF0apVm0z5_0k_CCq5tf5zo-3Wxh_pLwxZtpOrBET6NjPje1JlEUxSUNKj8ur64sN4dYhkL5xqnZq7ABhoUFRlmLWhb3GG8sLz_AwugK38Grqwx5uB1ZxxzZZYRdUBL3k2wCR3ROkAsjpr0vZ-u_SoZ8de4BgAHv_7yxxOAiTirs0VpzRCXW-4Fs-ZaMEU6VN4mqBZsyknpO75wOLtH5GyMqGnuq127-hq_4Vxgh1PV0aAWuRmq8Z_y68K5DkvaxEgPxeyVbMtAh_KC6ormvCC0EmJVv_1sO7O53xJqGI2PlGUnpQhdtLWYOkjif6jhwF6H7CQetoMC8_WuYeroGX697q9xnQd9ritsr0o9IKwQvzqvQALP3VDxzCZZdCZinMidNSy5-5ntjvJiJj_6sA8aDeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آشنا: ایران هنوز شگفتی‌هایی برای دشمن دارد
🔹
ایران ظرفیت عبور از چالش فعلی را دارد. برای توان نظامی ایران، ۴۷ سال زحمت کشیده شده است. به‌نظر من هیچ‌کس نمی‌داند ایران چقدر قدرت دارد.
🔹
اگر قرار است مستقل باشیم آخرش اسلحه‌ها حرف می‌زنند. @Farsna</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/435382" target="_blank">📅 19:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435381">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1b50003c3.mp4?token=vJuV8-La7nAKuVcfXF1-BHL1jzTrMmoRNm2aDaIxeXFR12nDuaD68W8Wy7buOWEcGBgr_EqfUF5EwGMNOpEidEBFtPV3H8jkPr321mXOSCYovOfjrDs8e_gOsMUY5q_oUJpKzB2gFPJuEspt121W7bpkt8KvJfIrDXbNeCRY0qU_8iGcRrNSix3IV5LeSXe5LdAR1LeBqCuE0IgRD5EQqm6KztyTzDD0FAHNABKXz7XRYcHXlZ91P0Zo-n9yeGoSrk5dJXW5xk8FqB0XxvqY9PaasHG3cphVSEbbHlZzuUMjV_j2lqzOWAy1YnPYGfkJK6Dl9I0lvatDd_7eW-rMtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1b50003c3.mp4?token=vJuV8-La7nAKuVcfXF1-BHL1jzTrMmoRNm2aDaIxeXFR12nDuaD68W8Wy7buOWEcGBgr_EqfUF5EwGMNOpEidEBFtPV3H8jkPr321mXOSCYovOfjrDs8e_gOsMUY5q_oUJpKzB2gFPJuEspt121W7bpkt8KvJfIrDXbNeCRY0qU_8iGcRrNSix3IV5LeSXe5LdAR1LeBqCuE0IgRD5EQqm6KztyTzDD0FAHNABKXz7XRYcHXlZ91P0Zo-n9yeGoSrk5dJXW5xk8FqB0XxvqY9PaasHG3cphVSEbbHlZzuUMjV_j2lqzOWAy1YnPYGfkJK6Dl9I0lvatDd_7eW-rMtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
فنجان اول اسپرسو با آشنا  گفت‌و‌گو با حسام‌الدین آشنا را هم‌اکنون در سایت، ایتا، روبیکا و تلگرام فارس ببینید. @Farsna</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/435381" target="_blank">📅 18:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435380">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">Live stream finished (4 seconds)</div>
<div class="tg-footer"><a href="https://t.me/farsna/435380" target="_blank">📅 18:54 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435377">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOI-R_HJfqXW2SZysTCHfqs-QIUQpRrsZfKWrkffuOX_bbouyXtbemEVT_rYOBuh_IPt1xMzGKfAC7JXI0nzqAFR3LnrLD_NBXg74HkOI1rfbbcWhyAl1qtAyaBRSl0LGkQjLK9a6jq1u7V6VyKNI6paH-tjIm-Qjbx7cYf_C-b1BzStUG1gKHVPZjZkex_nCMFeUbGUPyKrMKjgNy7_O3ranA6bYwxoEQTOKMewRHi7BBbWJ30f26hWUEV7jvHSYgTgbmM3ztOHVV2Qilj0gCjsVxszbpPGxXJXVRacVSLap8mZKWsNk_TR8ba-3u0K9QjoHoj61GpVUzujCdKPmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان به تیم ملی فوتبال: برای نام ایران بجنگید
🔹
رئیس‌جمهور در جمع اعضای تیم ملی فوتبال: آنچه برای ما اهمیت دارد، مجاهدت صادقانه، تلاش مسئولانه و به‌کارگیری همه ظرفیت‌ها برای سربلندی ایران عزیز است.
🔹
نتیجه، محصول اراده، تدبیر، تلاش و البته مشیت الهی خواهد…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/435377" target="_blank">📅 18:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435376">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR4NV2ABFagMJbnt06TsibSJtJz2M2_UtqNKn71-nbvOuWsD_YI6EtFIsyXLsB2maO3Esgh7tqLkJVYnBKvzJZW30EB8oPMfIT6MOmf8zVf0Z7wKxHDBud17Kl9eqH40zIqT8vwbKmVXbpnzvhkUS-IMxvp_6mo4942BLOkIKgDTPvNMrTZP1cybEnvDvB8e_jLqbza6wIjnVfGCHL6QCEtnD5GtkbpS0x6ram-swtCzxbcJMnBQRr00Ghx6GFfBiR_s7E-CuIAQDBKfGoPq_WQfSSSVIOJwp4f5aMEdVq8FpE3Tf9pBHj-Z4R9XzfRqeVa-rRVq3_GWZGQDR7nq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان به تیم ملی فوتبال: برای نام ایران بجنگید
🔹
رئیس‌جمهور در جمع اعضای تیم ملی فوتبال: آنچه برای ما اهمیت دارد، مجاهدت صادقانه، تلاش مسئولانه و به‌کارگیری همه ظرفیت‌ها برای سربلندی ایران عزیز است.
🔹
نتیجه، محصول اراده، تدبیر، تلاش و البته مشیت الهی خواهد بود؛ اما آنچه ملت ایران از فرزندان خود انتظار دارد، ایستادن شرافتمندانه و جنگیدن با همه توان در میدان رقابت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/435376" target="_blank">📅 18:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435375">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jv3kZBASh6Ppz_c7kyG6Vi1he58Bflrkd82Ip71SSJqxxZrGAf8m59DhC-k4t-Ab7DcnAvt_Qm3IF7nGveTAMPoLlO39MTxKow-zWqCfwnylerF6PuMTncA-1xYLkQpiSwsYwtkUJ_TPMerPG644k3mgUJ-N4DBL4-xaS4Ak-w3-hIqxHEpvWQVi0GcVuxJc5w6MEe256J_y9Ojz-w0FmwNUbizd4l2gt51Cl1QZ_VGcIyufK7AKK9NdpKtZXmmkmb52Texp5Sq98jfBf1-lbHfChtlaQDf98vBGoJGdViXKmeO4jlfR-UhZHrqdA5ghirY0IXm5QmGVGX2u1MSaZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
فنجان اول اسپرسو با آشنا
گفت‌و‌گو با حسام‌الدین آشنا را هم‌اکنون در
سایت
،
ایتا
،
روبیکا
و
تلگرام
فارس ببینید.
@Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/435375" target="_blank">📅 18:34 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435374">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-34.pdf</div>
  <div class="tg-doc-extra">2.3 MB</div>
</div>
<a href="https://t.me/farsna/435374" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۳۳.pdf</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/farsna/435374" target="_blank">📅 18:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435373">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JftG4Z9lf5WPnCr7ZUyWkk-9KiyTpdjYfoQJoNQxzhmfHwUTxewg8wXohfGQXDAZmdBdwMIVydTE9iCPwDqHIuVoWS2IrcbL_XZE8DPzsV7WCuDBlClY-UQfvWO5DsxyoYhnyPMpYtVG76mxHnvY2sGiNWFjY3SC6A5Dn1moAd20szTcTU3hirEJ_CGJ2Det9exwmpVncbpsJl0MVKdd-5Y7xkxiM5qnMW1ddunG32TJ2F7xOwaIsnRuTsouzUUaukvbw6RAf2XsPkbB8RUWQl-igEMfCfE2pXfgm4o4imJQT-r6CYSVK-7TWpT1_AGtxrfdd_zC4ayZDf0xvoCW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پهپاد حزب‌الله یک سرباز صهیونیست را شکار کرد  @Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/435373" target="_blank">📅 18:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435372">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">Live stream started</div>
<div class="tg-footer"><a href="https://t.me/farsna/435372" target="_blank">📅 18:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435369">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9Zl-zm9Z2jcXY_P1YSpNS53zcVOEn-FmHl59D6Ki2jY88m_d4E2HaG_1dg5TDs1bv-Jj7dqGT7tX8EL2Sn1DylS4v9z0XR0QzJFFRUQgnJzqLGqDVFuDc7dbbJlo-t-0pWRC2RH-dYr7Ap-WtL4DQrISurSMxjfCx8nVXrvbmcFpb-1ybR1dbP3bOME0mi3vcUbZ_o7klMxgHuyshvU0Sz8ztJP4xDroVJM0M9296ic9YBEtmcGw_zxu6YE_-c0u5dWuQcSy8QpTJjzymE-UZJsPYNk5trSks2krF-wZDxiNsxX32QdB_gb2RIk-TMcRjGl_Nstfze-EPC02yQZVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایننشال‌تایمز: تأثیر جنگ ایران، برای صنعت هوایی در ابعاد بحران کروناست
🔹
اندرو لوبنبرگ، تحلیلگر خطوط هوایی در بارکلیز، می‌گوید: گرانی سرسام‌آور سوخت جت فشار زیادی به شرکت‌های هواپیمایی وارد کرده است. بحران فعلی مانند «کوویدِ بعدی» است. ورشکستگی‌ها، ادغام‌ شرکت‌‌ها و بازنشستگی سریع‌ هواپیماهای قدیمی در راه است.
🔹
احتمالاً دوران سفرهای هوایی ارزان‌قیمت درحال نزدیک‌شدن به پایان خود است. بسیاری در این صنعت اکنون در این فکر هستند که پس از تعطیلی شرکت هواپیمایی «اسپیریت» آمریکا، کدام شرکت ممکن است بعدی باشد.
@Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/435369" target="_blank">📅 17:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435368">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUIKVEVScLBb3IFaGiGLmZ3n2arovLfhsyi-WXA2MCEHMTBQptUfkc0yrBWpcMJ4aoeZ56L_nDbOo6djvXFdeMQEApki2iead5wCsmsR6jkYNbFVuJHIL6GfBkb7A7ZJXdMMpnO98jEeGawPRXOMhS-zY20eKUoFP8CPwaYBleVHtUVk43XAyE-7BwZUHNi7QEU7qqDfhcW_AryKx2GVvSFNiriWFMzzoTjujj0VmCMJTt6rIPzPNnare11gGxBEYxFCRD8FSWzy-NwBgpxcAqPhcMdQMgkrGy18Yhg_8HBskNO-nWknTwj5qHTMLpn88sn_zzQ_q5Bxr5QG4ajlyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت خود را از بازار برق بیرون می‌کشد
🔹
سندی به رویت خبرنگار فارس رسیده که مشخص می‌کند، مشترکان برق با مصرف بالای ۱۵۰ کیلووات شامل بخش‌های خانگی، صنعتی و کشاورزی از تاریخ ۲۲ تیر باید برق خود را به جای دولت از بورس انرژی خریداری کنند.
🔹
پیشتر برنامه هفتم توسعه دولت را مکلف به خروج از بازار برق کرده بود؛ از سال آینده دامنه خرید و فروش برق در بورس برای مشترکان بالای ۳۰ کیلووات نیز برقرار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/farsna/435368" target="_blank">📅 17:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435366">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6b553572d.mp4?token=fxPeANqfBnrVsEMEYS1qWKhUXBIP2oMgIohucw1GmbtYLDmPUjtNywUMjF_RSGVtdbEDzjAPmFNus8jvb1i3ClPY7DA3IjufCCZc3YBQieQjD6dfuDDhFOPefGj6IDniJMIGiybIhQfCtqYnvHSNa59iQQUFKvetHwB4Et15_kZbCyRz5Q1MOUP0nOZy7J2-uMbIkMnwpu_TnQj-km13eDbDy7R-uCsfKCPxYTge-Cf0XkhueN7gaQ0BuSQMWXgLJEXvM7rF-8zSJ1XMRZ2lF5M-353VZZ_tQv0hha1j5dcxZZw73zmaIW_wIQeMllLKleWSGqDSGTbQssa_wFwJvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6b553572d.mp4?token=fxPeANqfBnrVsEMEYS1qWKhUXBIP2oMgIohucw1GmbtYLDmPUjtNywUMjF_RSGVtdbEDzjAPmFNus8jvb1i3ClPY7DA3IjufCCZc3YBQieQjD6dfuDDhFOPefGj6IDniJMIGiybIhQfCtqYnvHSNa59iQQUFKvetHwB4Et15_kZbCyRz5Q1MOUP0nOZy7J2-uMbIkMnwpu_TnQj-km13eDbDy7R-uCsfKCPxYTge-Cf0XkhueN7gaQ0BuSQMWXgLJEXvM7rF-8zSJ1XMRZ2lF5M-353VZZ_tQv0hha1j5dcxZZw73zmaIW_wIQeMllLKleWSGqDSGTbQssa_wFwJvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام عابدینی در برنامه سمت خدا:  آمریکایی‌ها می‌گویند ما می‌دانیم ایرانی‌ها چه تجهیزاتی دارند و راه مقابله با آن را هم می‌دانیم اما بازهم نمی‌توانیم در مقابل ایران مقاومت کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/435366" target="_blank">📅 17:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435365">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bfe83fff2.mp4?token=SPWX8FSzRJ9eQAeqMqQNjacPSELJ9ZaS_7Kv_7MjSxeeOFkUZXmyMGz9cDxtixVpU6iJ0eJMt5phkLxiXpo8Td07M6RLmwTFnrftTTU1sz9PtfWzNhjJB_UzuhWd9_E3xpfaetd0Xk-QAeYorr-TSl34bmvXAoleqVCqzjzzj1Gl9pWqCpyT_K2Ok3lsfa_Pp2-9pEHopTTWBzZhqp-P8eIR5APejktO8SdY8BFj0XyKUv6hJetJJPHFXVQKjo4YiCmDpmXDNNLlsgpHiDxxvIqZqqtj7FBuVOYQyG4TkrFKh1iy1X9IUCGk2XCd9thDx9mL9RU68rIbJVcvwzWh7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bfe83fff2.mp4?token=SPWX8FSzRJ9eQAeqMqQNjacPSELJ9ZaS_7Kv_7MjSxeeOFkUZXmyMGz9cDxtixVpU6iJ0eJMt5phkLxiXpo8Td07M6RLmwTFnrftTTU1sz9PtfWzNhjJB_UzuhWd9_E3xpfaetd0Xk-QAeYorr-TSl34bmvXAoleqVCqzjzzj1Gl9pWqCpyT_K2Ok3lsfa_Pp2-9pEHopTTWBzZhqp-P8eIR5APejktO8SdY8BFj0XyKUv6hJetJJPHFXVQKjo4YiCmDpmXDNNLlsgpHiDxxvIqZqqtj7FBuVOYQyG4TkrFKh1iy1X9IUCGk2XCd9thDx9mL9RU68rIbJVcvwzWh7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپاد حزب‌الله یک سرباز صهیونیست را شکار کرد
@Farsna</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/435365" target="_blank">📅 17:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435364">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef4869e61.mp4?token=Sgqg26lMZKJDki617Of4ytai1WsdQecer932goZhBEpumhLUJ4E2Vg9MLFkgufoLaFZIw-L1PDY1bXpPxJLjCDwtVJgOr1hVoSf7HVubO1V_-wiQ4BIB0skiVk6u073xuu3GXsK6z3h7IEX_cBl73KmXNYVjcgOef-uFhmbhETBNwG1uQG-bsJztIVTJPhgxV53UxZt9VSZ4XgMMpHivpUsb_b6kGnDmATEOaJvHpgf9ewqWjGkkj7Sfcx0JD-YV66Mxj4MzGJCZKsudwJitGMjZF9LZ6c4YSC6pl6ImS1iNGbdPoxDuQhvkNNTmQ5unMBN23XdRxLCRtqekepCshA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef4869e61.mp4?token=Sgqg26lMZKJDki617Of4ytai1WsdQecer932goZhBEpumhLUJ4E2Vg9MLFkgufoLaFZIw-L1PDY1bXpPxJLjCDwtVJgOr1hVoSf7HVubO1V_-wiQ4BIB0skiVk6u073xuu3GXsK6z3h7IEX_cBl73KmXNYVjcgOef-uFhmbhETBNwG1uQG-bsJztIVTJPhgxV53UxZt9VSZ4XgMMpHivpUsb_b6kGnDmATEOaJvHpgf9ewqWjGkkj7Sfcx0JD-YV66Mxj4MzGJCZKsudwJitGMjZF9LZ6c4YSC6pl6ImS1iNGbdPoxDuQhvkNNTmQ5unMBN23XdRxLCRtqekepCshA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چهرهٔ رسانه‌ای پرنفوذ اروپا: با افتخار صهیونیست‌ غیریهودی هستم
🔹
ماتیاس دوپنر، مالک پایگاه‌های خبری پولیتیکو و بیزنس اینسایدر، عضو هیئت‌مدیره نتفلیکس و عضو کمیتهٔ اجرایی کنفرانس بیلدربرگ: صهیونیسم نژادپرستی نیست، بلکه ضدیت با صهیونیسم نژادپرستی است.
🔹
من با تمام وجود، از روی اعتقاد و با اشتیاق، یک صهیونیست غیریهودی هستم. اسرائیل تنها دموکراسی منطقه و سرپل ارزش‌های غربی است.
🔹
اسرائیل با وجود همه مسائل، سرزمین آزادی و مدارا، و سرزمین دفاع مقتدرانه و موفقیت‌آمیز از ارزش‌های ماست.
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/435364" target="_blank">📅 17:31 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435363">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4812709ce3.mp4?token=Rb7QqJC3Tca7BJLR6cVO6NV2tts8jw2RzE-xqbA8eSU-_wudALMTgP7WrGQgwRKLx93vFUW8KbSVSm2EA6LUbZC4beYsBGOdw_Eb5eTIIITMQMYHzmtVUDL3ecL8lhHGcmJZuP-0HXcCbU3VyOo_hvUtGtWgclXBpyA_Z1w-U0ilkZReIu9hw9SqkKlGAGKF7ShcLZzZeZ6yT3Rn7x8KPQu8Il-Gz2VZu345QA5M7zXER3i82yQTaSx3pj9WyGbMPTyWsaQbRGOYWhZjLZdtx0I6QXcdVUU6P9zkkQBdT4Ip-wRIaDyinAFOWXtz2saMEvnsCuAUADuYFWKNDfY48Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4812709ce3.mp4?token=Rb7QqJC3Tca7BJLR6cVO6NV2tts8jw2RzE-xqbA8eSU-_wudALMTgP7WrGQgwRKLx93vFUW8KbSVSm2EA6LUbZC4beYsBGOdw_Eb5eTIIITMQMYHzmtVUDL3ecL8lhHGcmJZuP-0HXcCbU3VyOo_hvUtGtWgclXBpyA_Z1w-U0ilkZReIu9hw9SqkKlGAGKF7ShcLZzZeZ6yT3Rn7x8KPQu8Il-Gz2VZu345QA5M7zXER3i82yQTaSx3pj9WyGbMPTyWsaQbRGOYWhZjLZdtx0I6QXcdVUU6P9zkkQBdT4Ip-wRIaDyinAFOWXtz2saMEvnsCuAUADuYFWKNDfY48Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره همرزم فرمانده شهید یگان فاتحین از آخرین دیدار با شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/farsna/435363" target="_blank">📅 17:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435356">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnsfQ-21nQGx4oVqdRRAgtfbKdt-wJRkYXNOkvUyGHfVQpxWqnR7p8IeinHqDYn4vkoKQnXfQMhfTsNA2Jv0Jk4ivBBqWlLbIk6_c_LxPSZa-ehK2R264Q5trnjOVypLmWeqi7O2b4cn9KfdxWFKxT-WVEPBR4TSOZJKEZAUgzlP772hzS2UJ-A_jPtAlTtoDCq2R-EQHn05W0-f55TPS6SbKSQhfalLQhrSMzuAP_8cgpM3AtUaHICoOXaqR2Ejt8g7Z7vAP1JxAgaFpVUisCvRXPzBoReFHmvk_o_WcgEX9JkZQf4kRSEdBDwkMtvCB5xrUVDcJpgmKgaBfJ5fHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dO3IRCWe0mpl_7-M-UfmPL0F_6ccfAOVTligy1cEamW_-RyX59Vf0ZLG55-zXpqniySbD8RKm5nqR76BwJ7fw-WjB4s7_2VZ0N3WkSXw-p2w6WxcFB6RcumXOz1-QQ_yhfu764BF3PiYN4A_AL6a4tfg5bZC0SE1mdcSjMMa9nnTGHemNAFRsF0cTnrwjlnfLXqfH3pSa1Ot01_mM7Ig2YkwZCWam0P_PmDpfok-A1WqiEJwrm-j1Qhzdh3lIlIQOhjNE0wVu2UPzt1WNVDOx4sHgkckxdQoR4v7-LiPSCDimgHToXeZ3NB6HGE53agNXXsyIrmx-b8ijrKoIOtong.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmQe3xul7Vk87gXQtjxbX4UJsiU--IizsTRwfmnSLW7C-8BX1Z5pYR3B6y7abajYo0KD8hyHdO1BOUfy5R-MQiTCHl2Lijb3RR2pAc7W7Jv0tz35Thxa2q3OhNRK8xncWpsbWYu3SazTFkNbABUXWSOeplHuXE8lYSwvzbwVtNsWKslpaqP3EKHCx1L5Mea7X-Weru_CsSMSOgQqSFSYNAYufOZIt-76mq1HcZ__4IxO6H7GV0fSW1dhP_M31zxCF6m7k1-bZcN1rvx8lSuJgIj-C-w7z-bLi6e4Ivw_zJsIWJjrMi28u1DvwYw_kfCfG_Z0CyRBYWRIArcVxeo9Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AelfQai14Ze5c9lZCBDY5p6p0OSgLyvTtsiWI-ceq5cLg1Se4YaiTkre52n1HhUTtHgoF9oIC6UN_CeTN5I5Nz0d76gwYJ5f7ewSNg6g6hD26I6hxjQFnlWJFN2nsPjJ8oxQX3GuNg3LLSDIuU5vEbzJH6Hm3bpUnmNGIrEAMmyqEnuCu4Lad3h_91u00Vc4x-mIe6ElUK_b9QST91vCWJaXt6bMZr_MDIoo1mdccoEgM1e-DZyG7mej_b89f86HNWXrm4pWqtbBOpPK-KfZu2Mcjp71bneUuUficYJ2DYSIHmFgXPoaNxYLzLvp8KcPgR32wUWO3UqLjOn0CyY-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9lt9lzDCZizHgrcpLOJPp9-qlCP5YcFNwSTEHkmBWJuLXTQyxR5KkAklBz03xJVwj2H7YH8EWSuf37CB3xKKd-3VA1rwXuXrcJPGWagdIdDf-oQtlkiepkSrEI5y1xceaposRj1M2U--4hpnm2C-x9DX-_3RKuedSob8SzvoTqAb2pd-pXud_UWvILTaJ16FjmlHIjC_B8oCpUVnOSvDyKhlWDKZTrEMeD3u7Idb-LAOUb_bmx02NZJUIjnj1GfLn5w6C7JRjIxRPV0eHd8iz7bV6Xo6cboDsN-e1IOdkDwZb24ll2P6rLO0l1NVgakawvd4btd5Dvg7sLWTyOx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vvrKA4vxYoZfz-ArRrsGsXYu3KmXWKPzDQJBN23MS0JMVBZWrwd8bUpETJbRVKbs5nAtZkHZHvCJYdQAimiPwhtuzoTEEeh8pV_KNQ9H6JYPH4XVjfSYDemmalNAX5dXqh_H9--AIze13AtAgMd8KANfLQDaaqUp-xpy_O7mjUWmbFal3MzRKh9WOOGUIj-lYai5x7NALArkeAztb8ZO4_a4EJsaHqk0_FrQpBy7ii6rQsQsA4k24z3TBfGXY9lu06EBRhxD1DLgqXoFGfG5mVMv9lQUWwWFS7c-X_lbg9-2N_oDdAJrv6Jj6sv29Nw5b8r2TWgFhz77Tkm0UMPHLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk9nS7-f1HKkQjR7f5re_i5GNiBEzwqixnmMt_BnVbe47kqeZMTygwaUI_B88Cyy5OZ-U2u-dC53D_bme2hIoPqnivUmpy9iqni8UA_cch2tcUrDrrBebprR_9hJSkCxqI30DSFfkQ7mbcBR9FUhx0VW8hgxh3lsNBwPvouougc-bjQ49PJNLUl0yl05xrjY7-iIatzDsdgCSIa0iHOjg6hEuEx5yna0jdykQHJH4I0WUCsdDSVh28Izct0BpweDFUBdy5QpimY8PbCtN-HT0mWDzmR9u3ug6L3X3b6YmrH6R9P7fq2QmZiLXsoOtu8IwERJ5dzN0yF24o-_QCQM6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
سلام شهید؛ آئین گرامیداشت شهدای جنگ رمضان
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/farsna/435356" target="_blank">📅 17:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435355">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYJSudKGM_psCpMmW9308MDIqOgkLeC1JR_eAu9AmdQe_wHsmVVws18_XieJUsWbchNGW1CSIuW50nI6Slva4QhoDLa3ZuqmcOcNtbIwSrtZ6niQd3PS5EJNZ9ML4YHA5Sk-nZps_YJSYE6YXtdrYd4frWLIYx740YbzSBic5RmynDNCIbqpqvX1UBVdKjITuzQy4GdKNJDiyTY4W3A29Sw7ZCk-pFd0Fa2NTXv_I5QVFzl9olCDiLBnJ9IHSjg80J8rcyxEDAm1253pJ4yr5dLS4PGv9ONQuwaoSmV5DiK3-i3NYX6XQV82Ok_7uN9nmvsHxW5O4ZBqpwSa-3QUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذخایر آب سدهای کشور به ۶۵ درصد رسید
🔹
طبق جدیدترین آمارهای وزارت نیرو، میزان پر شدگی سدهای کشور در حال حاضر به ۶۵ درصد رسیده و حجم آب موجود سدها نسبت به سال گذشته ۲۴ درصد افزایش دارد.
🔹
با این حال در مناطق پرجمعیت مانند تهران، البرز، مشهد، خراسان‌شمالی و مرکزی همچنان باید رعایت مدیریت آب و صرفه‌جویی در دستور کار قرار گیرد تا از شرایط کم‌آبی در تابستان بتوانیم به سلامت عبور کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/435355" target="_blank">📅 17:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435354">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7JwZTSRdVxAhsImnB8UPyPdASfnu2i7EHB03FNkbjEm7qQcCU3OsS8E8Hf7szbkYB-HbqtpLCfQfi69-I7ZGxz9fIeUv8Tx2h7raLuSarW95n3uP-AARVtA_DQm8XiG1vaOtlFAD5YBPGadYwwxkTYq11qb5N4i0TXISivLwGZgRMRl4i-IN-kKHJoJYvaRjUtNufXLlclxZU-ag6WP6n54FvPeJIQCMNQZHpBNsIOffyGaIDSmWBMirL40jk5ZXuYGmXuH-nh4cWz4hxetVfrbxwsMvS30Hs-_s_beMuRbG_LjLIgPORZ40zM5igMO1Schq0k41tqPwhzJtMo2pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمزگانی‌ها روزانه به ۱۵ کشتی در تنگهٔ هرمز خدمات می‌دهند
🔹
به گفتهٔ مسئولان بنادر و دریانوردی هرمزگان با همکاری مردم محلی روزانه به ۱۰ تا ۱۵ کشتی معطل‌مانده در تنگهٔ هرمز خدمات‌رسانی متنوع می‌شود.
🔹
این خدمات شامل تامین آب، سوخت، نیازهای درمانی و دارویی، نیازهای فنی و تعمیراتی سیار و... است.
🔹
۴ لنگرگاه در منطقهٔ پیرامونی بندرعباس و قشم وجود دارد که زیر نظر سازمان بنادر و دریانوردی قرار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/farsna/435354" target="_blank">📅 17:06 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435353">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/331e0b7936.mp4?token=CAxlv0fqr6nC7xl60bv2boyyutl3jIyCrdRIq2foINJw1RFt7shA0J3PoUQiltLJbOQR5ol9STBDdILRJ6j9YKSIPB_g-Yhy0vgU4fZTBqNSCZrKA-nhw6srsJNFY4VXvk2uK14hBOi4xP579s2YgvfZJCv2kZnmvnIbP2G3ZE2MUYosVG8NSWFdYZSI_PSFGLbTb2cN1dou5s-D9cJv2clgiIHHBr1V4Zy8skwqhcncJHwE6HoR3VuHgluNiw8OxWO6SdKU7g8UF_qHlOGAm9V-OyD-qBXoOv2Gkdew2k1aUXBmXRl4kbDoKlaWRcbX1K549WkTdGwrE4-Esd8CbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/331e0b7936.mp4?token=CAxlv0fqr6nC7xl60bv2boyyutl3jIyCrdRIq2foINJw1RFt7shA0J3PoUQiltLJbOQR5ol9STBDdILRJ6j9YKSIPB_g-Yhy0vgU4fZTBqNSCZrKA-nhw6srsJNFY4VXvk2uK14hBOi4xP579s2YgvfZJCv2kZnmvnIbP2G3ZE2MUYosVG8NSWFdYZSI_PSFGLbTb2cN1dou5s-D9cJv2clgiIHHBr1V4Zy8skwqhcncJHwE6HoR3VuHgluNiw8OxWO6SdKU7g8UF_qHlOGAm9V-OyD-qBXoOv2Gkdew2k1aUXBmXRl4kbDoKlaWRcbX1K549WkTdGwrE4-Esd8CbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تشخیص پیکرهای تکه‌تکه‌شدهٔ کودکان میناب توسط مادرانشان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/435353" target="_blank">📅 16:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435346">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJOYjoN48jZWtyS0qJ4cCQCvlzGS71E1zgwMDtF1zRxMHpnWZT8_mtsS2wBwzZOnkMcoQNmH_ZSnzZT74PzSc8DwxvZ7ayknwYv6UDmtl6O5CGQ7K5pBjWIlcTekfwC6sm9bAjFR9uFMDSjiWiqOdogIT8iovieytwZVxdPvPJoweJTo4gYuM5GJpP8Ra3nInL_QLGoYOU9F97MGVoWvi2b5lRqcD1AOvysAdIB7RCYKX3EjCmeY4c34uSKfNaOPZ0Qn3fXGEHqmlZKmfo6az-IOmQNhIzsNS6blaMV-MX5-KD7gqLOiWXkowfVQ7GxFxs4eRpdvMzftCMKj_sB9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TgBdRXFc_UebOQS6nC0sVRPN54Yq0STNTeNKA1r5CDqHjKQFRDjot5KetIQFqTrLboXS7js0qFLWugvI6ENMSdMWzx-A7Br_Q1DeIfkIB5PVgz6K5ZyEAxgVrlVm_tM8HsBzC69m8Rk1nIxE21JiTqehllawlCEgF0VYjq_4k3i7l-Deow67Kom0ZLTfbSTTqBESZMFKgeKyBUCnr8vD2MRciyRjEseIjlBy8XET6rOjN3FXDmqWK1baLmHTTRlv9Q8ng7Pa8VO40hc6uHzUckLTBdeiWid9LLfKduruOfgty2j2wSjiJoihdJzZI4BM5iOmP-oj3w4kVZ4oadEgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q9r9oPNCIbt2PXeDB1c7-MvHO7eOnf-67UZhJY6FCo2rF9eTzSwf4Y_4OfRs7jKN9IJPv_5Ne9pbb3u9qBGIHWmCar1Fvqdg56bQjlS4Tzf9axQIM7TAm4c1TFQOyuRAXYxrjjvxg21I7c05Puu7gH0C2DKF6Sr3SAH2dUzoMRPKVNVXNkFA8AWlQdiY-qMtCzQkHfgAv6SL_KH_1LdGJv0hp0R683Va6CfYu1VC3F65nEVTzGT3guKp_hGOtDs9bXznYl5tUgiukia83ra-OFd0me8Izlj6cVhedy5Xobpc0zIEICwUb-4RzQAZ02qkG0QL1XZDiolJ2OQbU5AzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqk_0Lmzs-J1PunKEqzySKGZdvoBFFexOkwdNTBglhhixg6AtdTwxB7HfPOwjgjCvNxrJmeNvHqge8QZ7CFOzpAHIyZ7aFBC4ProP1E1XoJJP-euwx5iSyobxiVIGCjvfvnh2kzQsiSexJf1T79izKluLVdKoz_utmW-87vZdoCQhrlyHKAqt4XlQTrmY5EsAnR9Z5GKpo1_zw--FHum6V-a7wo8WUmsjvYHzIE5zSvpVjUlgL0mn45WbPDbNvwkjjTc0rXAD4Fr0bTtllgbFcic-KC6-1BUllQiBPq9y5xb-XWVf83kSR3PuwgafThw2Mr0ddIX90Glj1EKpFn-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDhomIRnu3ovdOeQPs60TEfgQyPctlVsg6rJsPlUzS2895wFZcWPVS8c6c9pY81npIbQW16E-Y1CVWwqI9JrEM5MzeVgjOXix4VosCmxQPyTiSiQHuI_q8YevIXzGMkAunP82DqsZbGMB85j4DvBOm79dB3XpAGBknjOYLopzL3bI0dJal60GBDJSZoQgwkp8RSJkvFLKzvuiOK2kEXo6ib1gHnUZp09JB-4AtcoXY80X506-lND19tFzkxY7Vx0eqA0d9RTMCeDuKEU8tsQYRGxFnUNl6b-_0pPgm0QVoT_P9hUCRkN4uH5GJ2PV75QVAExrP-atFCm-DD06oiV2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/subLx05rcjrmASf-WWDj4EWg9ufpQusnkyXUniLdgs5bLOQRmpr8AfB6wD1XD_WwnFsBxxWFvgi9uB4G8CQjJboGz3iHXoiBgkC_TDu7iTAxUpcZseDEJ-bT43zE-usy-5vnjK_etNwrnTJ6Zz3UEqWC_hi-816FIstzO23W4MoaydvpQTrxGc0WFGk0ckBz2D8ZG1vXg-FMZSCdtPrXap2w60DMg-zwv6WPvTfwonlPekMFKeTirVv-9kpZxeBJELcDbBryb6_Y0xV_vc8dNCPLYI-Hxy6IZ-Cm1RHDg5Zy2_pfGFAjtqO9o2-Fu3n1b5yqMLCHGFPIu6opypFEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r23x5l8GWwVjM22moy-I-tRMgcUGKjVz4_43HGXjdxoU5_jKK6jxcY-lHZArXiUUgdBD8d80INOOlEubF_bp7V7m-1enJtsJzrwLnXPQ1Yre5MPvhNzbxfz0M1GbvyT7Nzr3dagqPTK8BWKbmTZJpW6b5SBztlDrNmI1wPDGpGCqZGtgm1y9xkv7B3Eb4c6Iaf-1vkXLJU4mIRnlOhgNpBHWH-4faADjIghBeGQhGI9svua-acdhOtzywmlDXkkTp_7Vt-lRzOe-rW0LoJlfiKOkpKuOgRyRKaxYImLffn-MxNQPmgF1bPeMRXhCAkVL-aijGZ6BnlyYr2qClbb2NQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست خبری هفتمین نمایشگاه مجازی کتاب تهران
🔹
نشست خبری هفتمین دوره نمایشگاه مجازی کتاب تهران امروز با حضور قائم‌مقام نمایشگاه کتاب تهران در خانه کتاب برگزار شد.
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/435346" target="_blank">📅 16:53 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435345">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9393913bb.mp4?token=R12u27Y-bTiGVpHuc3LAXDUfoQ2qJLbDYmJwNbklf3ft_hwLhfmm-haITaf1KgpvUahQM5GcI4AtQ46hsVHCbwvzlEcNEPbO6mQ7N1fx08g7iL6-ouRl87ba8moboamyhj89yxumeY6HFVQPS0YDMQk3qWnKlL-Bzcm8C1QdAJVRMfmVUgwnG6qw3IDQ2Wg7KCPjgMHYaNd1CDxTLoItP4olnB4Qmg-B00Iw2OjqhouQ5i_knH3vGLmKnnCcEwqtfDlF3QhpfanVUz9WmXZrhQv4VRUNx5PtGbwMZadAq1y0ecjWC5vBfL3YxIYYc8sdCOZ_lFxFBzBNdxNQcdTiqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9393913bb.mp4?token=R12u27Y-bTiGVpHuc3LAXDUfoQ2qJLbDYmJwNbklf3ft_hwLhfmm-haITaf1KgpvUahQM5GcI4AtQ46hsVHCbwvzlEcNEPbO6mQ7N1fx08g7iL6-ouRl87ba8moboamyhj89yxumeY6HFVQPS0YDMQk3qWnKlL-Bzcm8C1QdAJVRMfmVUgwnG6qw3IDQ2Wg7KCPjgMHYaNd1CDxTLoItP4olnB4Qmg-B00Iw2OjqhouQ5i_knH3vGLmKnnCcEwqtfDlF3QhpfanVUz9WmXZrhQv4VRUNx5PtGbwMZadAq1y0ecjWC5vBfL3YxIYYc8sdCOZ_lFxFBzBNdxNQcdTiqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ سلاح مهم شیطان که با آن بر مردم مسلط می‌شود
صحبت‌های شنیدنی حجت‌الاسلام رفیعی در برنامه سمت خدا
@Farsna</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/435345" target="_blank">📅 16:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435344">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SV3rEMz4P8eZTf0Qzp84oOjecNJeAHLGZMF9nNn_JX2C_xgGKtfdnEOFCsCYIZa8UQJ5ET_dznPZnVgOyl4azX3JFH2cq-4OPivK_i3n_0uPEE8X-W4qFzGuNVLskytNkm3fwrNDSYl-wcP1YUZOsII-PrgTApL_AHynAgRxoctI-r8xTK3_iIFcS_Qz7cZl0wslSTFHoIKZphGCO_q6QnEkljnfVtxKBRX__lNmRvKF_T0Gk3flryY38b6PpXFhxa5KD4OywX_tM9ej-HSARQFPvhCE3GAfW4UIsIU8yAEe24MBMg3Wgo3rCwgJRvAhBxEaap4uFA2XcqyPnFrpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییر نقشه انتخاباتی؛ حربه جمهوری‌خواهان برای فرار از شکست
🔹
جنگ ایران، جمهوری‌خواهان را در شرایط بسیار دشواری قرار داده و احتمال پیروزی آن‌ها در انتخابات میان‌دوره کنگره را کاهش داده است. اکنون آن‌ها در صدد هستند تا با «بازطراحی نقشه انتخاباتی»، ضعف کاهش محبوبیت در میان مردم آمریکا را پوشش دهند و بر دموکرات‌ها پیروز شوند.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/435344" target="_blank">📅 16:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435343">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما از ایران سپاسگزاریم که به‌خاطر حمایت از حقوق ما در خاک، عزت و کرامت، سختی‌های بسیاری را به جان خریده است. @Farsna</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/farsna/435343" target="_blank">📅 16:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435342">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: دشمن صهیونیست راهی جز ناامیدی، توقف تجاوز، عقب‌نشینی از خاک اشغال‌شدهٔ لبنان، آزادی اسرا و دست‌کشیدن از بهانه‌جویی برای جنگ نخواهد داشت.
🔸
دشمن با تجاوز و جنایت‌هایش نه به ثبات می‌رسد و نه آینده‌ای خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/farsna/435342" target="_blank">📅 16:39 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435340">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dae014c5c.mp4?token=C2WmbQpItF8rLtcCXexeFfnbtZEku6X_2LG6VSP_AfMEXJzOO83ctNkXSxj8-eRxRzgoOlvdnjeDVHuJDfmDDFq5rA4wjxEt7TU_21Spvmd4lwWi1hRwb1URcz0pqDKj7I9nRdVFwDlJL-s9uVriM5c9-vhNbbkUswlGSZWKJlyqhyOxK151xQ2n1KyCZUlJwhl0tJ6hnroeWyddYOVWoWT9R61l6l40bSZQmdlP4_9I1Yv2TPcKQ5fFltO4OREowgNu9SIZLXtvKC3bQkhQxVzsR_BwVjL9PJv5DnJoK6i68qFVer67xf8LvOWLYNQah1A-HMfGq9ugI3ttguoERg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dae014c5c.mp4?token=C2WmbQpItF8rLtcCXexeFfnbtZEku6X_2LG6VSP_AfMEXJzOO83ctNkXSxj8-eRxRzgoOlvdnjeDVHuJDfmDDFq5rA4wjxEt7TU_21Spvmd4lwWi1hRwb1URcz0pqDKj7I9nRdVFwDlJL-s9uVriM5c9-vhNbbkUswlGSZWKJlyqhyOxK151xQ2n1KyCZUlJwhl0tJ6hnroeWyddYOVWoWT9R61l6l40bSZQmdlP4_9I1Yv2TPcKQ5fFltO4OREowgNu9SIZLXtvKC3bQkhQxVzsR_BwVjL9PJv5DnJoK6i68qFVer67xf8LvOWLYNQah1A-HMfGq9ugI3ttguoERg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تیراندازی در سنای فیلیپین
🔹
همزمان با تشدید تنش‌ها بر سر دستگیری یک سناتور ارشد، صدای تیراندازی در داخل سنای فیلیپین شنیده شد.
🔹
شاهدان عینی از شنیده شدن صدای تیراندازی‌های متعدد خبر دادند که باعث شد روزنامه‌نگاران و دیگران به دنبال پناهگاه بگردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/435340" target="_blank">📅 16:37 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435339">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
دبیرکل حزب‌الله: دشمن صهیونیست راهی جز ناامیدی، توقف تجاوز، عقب‌نشینی از خاک اشغال‌شدهٔ لبنان، آزادی اسرا و دست‌کشیدن از بهانه‌جویی برای جنگ نخواهد داشت.
🔸
دشمن با تجاوز و جنایت‌هایش نه به ثبات می‌رسد و نه آینده‌ای خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/farsna/435339" target="_blank">📅 16:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-435338">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_zHvZrm_WrYTYkPwFLsWgjWWMK75kWH0Ib1oNNKWEci54lbqC_W8K1uI4z-RV7IhCJqyLtaokZABSUgeDr_JHsnxeCD84Y7_vU_Ddhk6D6cYc27q2r2qRjDAeuERPTzV3Oaubj6-XlSPyqWpGy2IV1hRqG99txBIyaZ-zKnsJ4-WtSuRrINnSYyfhmiVLwWFHbcoqVfS1wfqS6aZvBsu86EVf5zS5_vI5kC8OjL8u-k7LbNb8ya5Yt5Eo0OTV3K-_yrNQg6LVScK86VTLXLbyWHnvUGBRsFp2YwAmao4jkt-CNAmmsrok6XzVsgzfqEW1z-MG2qLsLiesED6X5BEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور حکم توقیف اموال باشگاه استقلال
🔹
ساعدی‌فر، مالک برند پوشاک ورزشی «مجید» به‌دلیل دریافت‌نکردن مطالبات خود از استقلال در زمان تولید لباس‌های این باشگاه، از آبی‌ها شکایت کرده و علاوه‌بر دریافت حکم دادگاه، دستور توقیف اموال را هم گرفته است.
🔹
همچنین طبق شنیده‌ها دسترسی به حساب‌های رسمی باشگاه با مشکل مواجه شده و مشخص نیست تراکنش مالی استقلال دقیقا از چه مسیری انجام می‌شود.
🔹
آخرین پیگیری‌ها نشان می‌دهد که باشگاه استقلال هنوز اقدامی برای پرداخت بدهی خود انجام نداده و همین موضوع باعث شده تا هر ماه حدود ۷۰۰ میلیون تومان جریمه به مطالبات ساعدی‌فر اضافه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/435338" target="_blank">📅 16:28 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
