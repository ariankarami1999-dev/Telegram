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
<img src="https://cdn4.telesco.pe/file/HmsxHDhPuocH5cLFOPCvFIc55pEw_CRRkdzsNxfnSnEqjy7OpHOSuwlEsUBkh67PqGqU5hDTkl4rB5Q9vxXvKMKLv6LqdcxscMulP84h2KNLgXkBhII4fIHBEoz1bHjLxN3jKjFok8KYAgJ6DswJpwAQGuE3X456q8qNPTr0fEp0qPuZfRDvp5K1fvhL7yCj8ht_EGzmLjZWHAXstADl1wzS8KH97mDIk2QsXWZsT0CW8vECZLYrFntijYp8NVViu7BZlklop2DsL_fMfifldgiuXCH8VacErZ9jHEUREpL9LIwK6Ynzkau5UXtsHtGw8p86lEidJ4WEpuw6G_WKZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.61M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 21:22:53</div>
<hr>

<div class="tg-post" id="msg-658127">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای اکسیوس: ترامپ احتمالاً اواخر ماه گذشته می‌توانست یک توافق اولیه با ایران به دست آورد، اگر شرایطی را که فرستادگانش مذاکره کرده بودند می‌پذیرفت ‌
🔹
در عوض، او پس از جلسه‌ اتاق وضعیت در ۲۹ مه تصمیم گرفت درخواست دو اصلاحیه در پیش‌نویس تفاهم‌نامه را به ایرانی‌ها…</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/akhbarefori/658127" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658126">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای اکسیوس: ترامپ احتمالاً اواخر ماه گذشته می‌توانست یک توافق اولیه با ایران به دست آورد، اگر شرایطی را که فرستادگانش مذاکره کرده بودند می‌پذیرفت
‌
🔹
در عوض، او پس از جلسه‌ اتاق وضعیت در ۲۹ مه تصمیم گرفت درخواست دو اصلاحیه در پیش‌نویس تفاهم‌نامه را به ایرانی‌ها ارسال کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/akhbarefori/658126" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658125">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5d-zZP3fEQ09rnqNLH2_hATky0Qc2DqwRRRk_NnXg46M96L2PIrHvqd9RyBkLlLt4zqKVj_-j6BgET0iefcfg2ShCwXG23Fj9gvg4n1g-58HZU8YlyK1J4j_4t08DqgwlKGgJqWa7q3w5XazZ5Xacx6vxN21snkHSbt9pEgwCTH1OLNvsUUuPp0wZgPw7pW7dqdpIUqDuTyJvs4YDNnHHNQ-P0UEgudWHzkdKDkVpIV9qx6ih7_ALF4pclfKC5ZlxfEHgQ_fRt-t4S_NA_4joAVQDkjrGsrmP-tGO72wlIUtHGRbdyTDs-c32WPBkCu7K6BFEwTxaebNaLdtRn1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ در مسیر جیمی کارتر
فایننشال‌تایمز:
🔹
آمریکا امروز بیش‌از همیشه در مهار نتانیاهو ناتوان به‌نظر می‌رسد، این اتفاق موجب شده تا ایران نیز تمایلی به مذاکره نداشته باشد و آمریکا تعیین‌کننده پایان جنگ نباشد.
🔹
ترامپ برای خروج از این وضعیت، سه راه دارد: تهدید اسرائیل به قطع کمک، جدیت در مذاکرات و ثابت‌قدمی؛ که با توجه به سیاست‌ها و شخصیت ترامپ، محتمل به‌نظر نمی‌رسند و حالا، او که از تکرار تجربه کارتر و افتادن در چرخه تلفات نظامی می‌ترسید، بیش از همیشه گرفتار آن شده است./ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/658125" target="_blank">📅 21:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658120">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tNNg_DaPXt3fwfozbEPcc7F-2MFLqrgjY-MMMedgOoMQNPQxprSGr5N7pZpC5rh-dFpcFuBpmZlOCs0Nwz3mb9qlYqIzKRN0rlN3_F419p-iaj5lchq1ED353JHIFxpBHfedW_6e6D2RGyOE98uQDvLV4izT2VofnpiAz7Gu5_RORU4VtIWBENnd9uSI5bAPZyY139t0z5D_Atje5EqLrM5Ob05sqvDF_-DIWF23zybxR2wGV5kup7yW3q7LjDhQfKbATG1NrE-FPD6v25ok8OXvmOrlZwfxsHDhCo4SMMQDrTRFUroSsk_hVNQD_CrGB_BhFYfepDbSxRr2Te_D6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fFN--TRcIb4sxFCn5eNbv04tzeAfnt_42n2PFo5_rCKTFMl9v6-eP0nuqA52deGETpocZBoX6UGaXX2Y8Gf0w0Q6kCYnsd5itMqn1plougva6yQwIYWcsmxJVe3ieCQJDs61xSgBY_GoTWU272BMF437QlulH0uvqqW50dpD5XAj24kTZ92LyNWUDb7OuhKKYHgFLOcCXN6iYnkn1StsMoE961q6nfA8cvyJK2LvZkVHh5WpgQEHzh8J1zhBDAtVfODW9Zft9nuYFRmeabPSWjwR9hG0Su0UZiCLpa169ABWT5y1KtHJlLY7tVanCBlrfM5eGBskMPbIde_UOLUKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UA9tIkx3swi05VTfAOCemW7K3agS2mNdagus7ej9kFVEwrknq0ZYWTLOwbrN_5wIwQgE2YECaKahIswr1VtNg8qfQfW2r-7D3EowvVVsfAdguYOKqn1egikL2UC2QljhiW1YWUHszabaaWYYpRfqhqKGrLNOfl7wzD4wxuqeAgmRJh88Y7LhLSe4M2kbjMa53DXNRrHUNexBwv5La-P7HiFdcJPYG0wdpIp6K2h3DdeA54jt1Ui63rOhmOUnUuMNZYd8eku566LUgX8LefaxRn9qUdmlI19HTCdib4osBaFk3KbQIN_XA5cOegAaboJ6t47aExz3jGKkssKRiDgUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAp3YBVNgNMX6Oq8U3quYA6C9ussugWSdWhuhh5vPtae7zz2TLquGYhEOwTJ6lVKw0tIrLePjObL-iQhm3z3dFHV2LUwN_YtfLJmInuqlq_OsTu7VzlrETJb6rQTabiMlLLTYueDEYGVurrvrrR-x-XDjv8d8VR80PBzJs_Q8WULDAbrMq3oUoe3DWfdO-VKptV-jmWvebg8U85mzNCaPWLoETQ2TxJ7555tmXnhFNs3FhQ_gJiHXAUPlRQMyonSpU4VG9_TKKiIeOOz-560p6ErFyJCWSX848wAF2mPWApw4YZ8F5FqmELw9h2cqbb9yM4iEKMKRXM0raI-co5UXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55a7594099.mp4?token=eVPtOI_Li0uMysKTrLSXxkqnqluUClsdgvckCD_4DUyii95KF4Gx-Ned-N-2YgNw-5n0aENKDgsPPmLLEOuBfVmDVEclTXPBSDQN_NohvO34UD9u5NPtJrHQVGlKnnV4wqhYlwMMM8Xs6mk4udCvnLD8-Azfu5F9xkGD_K2xs-w2dR8Oo_BppDBuSMgkyIAjNCwr1dIAH44IIhEJ3f5O9ONjZrQ965IduzAFkz3N5UVdL7vXG69ktcsVgLIlu2T2h0VH0l5e9TWadENXgy4Xl42BlQ0LXeBjYLVmwpMaTha2ucObRMYYuhHERN31zwFNIXqArwpHt1Z4_rQ1CEpM-iEE6guOOfJ--3vm_Lt2OYIJFKB42HMKyppMwE7Yt-8V48rCx_ka3b8BAfa6MjPsWy3MFSzxA2IKjxL7bgVzdsmrulVlpdS0e_Cm9P1EFP7S_ZlJ9RpRUPgd8jFKx74mH465UnBchlUupX8sVjKVJ9WOjIWrkUb0qxXvhlBmQYg6P5LFCuwu7DSBexnNAVl2lpRIURgtAsCCk69OXLNbYsu56Hl44nxY3y6EaV0UDk24hHnq9soD3O5J11j8nyu8Jp_cEPM1GAy4MYUECOmY_Bu-VKgjQmcddS0eyvatllrW5XA5aeHvnTz5iFFflitBxj_Pkf_B_vmdRI8rIYwTlU8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55a7594099.mp4?token=eVPtOI_Li0uMysKTrLSXxkqnqluUClsdgvckCD_4DUyii95KF4Gx-Ned-N-2YgNw-5n0aENKDgsPPmLLEOuBfVmDVEclTXPBSDQN_NohvO34UD9u5NPtJrHQVGlKnnV4wqhYlwMMM8Xs6mk4udCvnLD8-Azfu5F9xkGD_K2xs-w2dR8Oo_BppDBuSMgkyIAjNCwr1dIAH44IIhEJ3f5O9ONjZrQ965IduzAFkz3N5UVdL7vXG69ktcsVgLIlu2T2h0VH0l5e9TWadENXgy4Xl42BlQ0LXeBjYLVmwpMaTha2ucObRMYYuhHERN31zwFNIXqArwpHt1Z4_rQ1CEpM-iEE6guOOfJ--3vm_Lt2OYIJFKB42HMKyppMwE7Yt-8V48rCx_ka3b8BAfa6MjPsWy3MFSzxA2IKjxL7bgVzdsmrulVlpdS0e_Cm9P1EFP7S_ZlJ9RpRUPgd8jFKx74mH465UnBchlUupX8sVjKVJ9WOjIWrkUb0qxXvhlBmQYg6P5LFCuwu7DSBexnNAVl2lpRIURgtAsCCk69OXLNbYsu56Hl44nxY3y6EaV0UDk24hHnq9soD3O5J11j8nyu8Jp_cEPM1GAy4MYUECOmY_Bu-VKgjQmcddS0eyvatllrW5XA5aeHvnTz5iFFflitBxj_Pkf_B_vmdRI8rIYwTlU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش اولیه از حریق یک انبار در میدان قیام از زبان سخنگوی آتش نشانی تهران  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/akhbarefori/658120" target="_blank">📅 21:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658119">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nRaL67LHR_H4HBWkHDcvJnIRnSFxfFRYQSW7xZzy0-Cke-Cf8vaCB7xIfBePp4PdrAx8wXbvDnJ4vUZdD97NErrh6ZHB8t9R-nxbOLkcwAwgVRNaSOmGwdelbZRIrn7af1oLh7NDgUBrILI0iQbEaD7pJq6roXpOCA2NFjw3WCyreARUb7-Kl_Vvu58Ah0tywRVcGdXawejFNWeOGNwNngAhXwfPizo6K7yIk18q1s3f6gjYMQDQU73I5qy0VgiuaKwIJva9LFiyR-vy5f4Q1q_CobaYemrPTcnXU3M7w2OLF1mwLXyCVXrCsI6b9HS76nuUebIKsDwAWWXltYVNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مشهورترین پیراهن‌های تاریخ جام جهانی
/ خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/658119" target="_blank">📅 21:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658118">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111fb7a2d5.mp4?token=FZ2wBzrhz9t5ws6wg9HdbL-fiRBX0QXx3nt752Bpz1zpBx_HXUK0jnn_58LjMNKt8kTuLb33k7uoFPLdDgQyWtM8kEw1RclogBHT96F3DsaGYlx9cdj41CcOQnSYtp_8EsuMtcwDCQVBPmEbgUzXVdeNMSM0e7CChyP1z4-2fdNl2nwFYMCQTuR7j5AYWxZV4wvXU9Mux4vW9tgnlzgd4FbjebtiiNL-eElpH9YYDErcfRaA9xOnxqd3PXp-Y3ejPhQ5UnjjdYP63cA0yuZMXXGGKI8bQEBnxfVdPFm2N0liUIY4_qH3QAhj2GoC7fcblcXJio5BTSvHnDEESEpxww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111fb7a2d5.mp4?token=FZ2wBzrhz9t5ws6wg9HdbL-fiRBX0QXx3nt752Bpz1zpBx_HXUK0jnn_58LjMNKt8kTuLb33k7uoFPLdDgQyWtM8kEw1RclogBHT96F3DsaGYlx9cdj41CcOQnSYtp_8EsuMtcwDCQVBPmEbgUzXVdeNMSM0e7CChyP1z4-2fdNl2nwFYMCQTuR7j5AYWxZV4wvXU9Mux4vW9tgnlzgd4FbjebtiiNL-eElpH9YYDErcfRaA9xOnxqd3PXp-Y3ejPhQ5UnjjdYP63cA0yuZMXXGGKI8bQEBnxfVdPFm2N0liUIY4_qH3QAhj2GoC7fcblcXJio5BTSvHnDEESEpxww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیازی به توافق با ایران نیست، فقط از این جنگ خارج شوید
‌
معاون ستاد انتخاباتی ترامپ در سال ۲۰۲۴:
🔹
من هم خوشحالم که خلبانان ما سالم هستند، اما سوالات زیادی دارم از سرنگونی اولین سوخت‌رسان‌های کی‌سی-۱۳۵ آمریکا در نبرد.
‌
🔹
همچنین درباره خلبانان اف-۱۵ که بالای ایران سقوط کردند و هنوز ندیده‌ایم‌شان. فضانوردان به کاخ سفید آمدند، اما خبری از آن خلبانان نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/658118" target="_blank">📅 21:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658117">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRsVn2P-bEEv4lBDCrSAtceGTwYAsoVzPyEIOc7ow25oTXtsPtoAwS4BqTnCXwVfo7hQJ97AAug9VYtORuqM1hrIJ_0WXL9-8thTq4WH6lRXztWgxnju6P0PBDt9Zq4vG8LSoN_KWrgqpBgMIOQkd8QQ96ceWH1Z7uD7Xdki4-VO5bHXzgc9TXgslgE_YezuGeFcvDZbTmqDl5PS39GJpAHfCoq-9XcOcDcXEIjoCMyghGWKdagn38zQyEaYavRmOCbbKbfVAAP1-FFFDVYKQXmYU8JiYtS0mkpr6V38TskPdEIUzeOTP5Qy82G8nXa6cOpIE-yY4sFp30FF6TLyNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قاتل‌ِ آپاچی
🔹
از شب گذشته، دونالد ترامپ و برخی مقام‌های آمریکایی مدعی شده‌اند که جمهوری اسلامی ایران یک بالگرد آمریکایی از نوع «آپاچی» را منهدم کرده است و تلاش می‌کنند با برجسته کردن این ادعا فضای تهدید و تنش نظامی علیه ایران را تشدید کنند.
🔹
آپاچی‌کُش‌های باسابقه، حالا ژست عصبانی گرفته اند و با سیاست های رادیکالی که تا به امروز بارها شکست خورده، دوباره در پی آزمودن بخت خود در خلیج فارس هستند.
🔹
فارغ از چگونگی انهدام این بالگرد، ترامپ و تیم آمریکایی نمی‌خواهند از اشتباهات گذشته‌ خود درس بگیرند.
از پاره کردن برجام تا امروز، از حضور در ویتنام تا امروز، از کشتن آپاچی‌های بومی آمریکا تا امروز!
🔹
هفتصدوهفتادویکمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/658117" target="_blank">📅 20:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658116">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0992445ad.mp4?token=ABN6-V0o9c-PN-WIFU23fh2BYrjzate6kQYO9_pqZ9SP6nmcvBkb9tCPfLaO1nA_yI72-dX6aRbL-GPmPML0dw0wyM4aovNA3so69mGKbhy2XQCr2fhSFMey3kLiRi9LoZirbeAlVsM1LwMxuQNIovvqlMa2ZKmr8HVhdlLnua5cZBZkTQEarAjdVhlgK6w8tfONJcOJ-YNC2eWZz775T04UuOZepJj5M3Efr2qgR9rnwwQrLDd9ecII71Qrek9GpcJ2yaYx4Xn5rRS825aHkl-arv-1JFwdqI5Rt0STnkaMoMANzCiU2P9MIYQr5-xIis9tsBIpiJz2QpCHaq2xtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0992445ad.mp4?token=ABN6-V0o9c-PN-WIFU23fh2BYrjzate6kQYO9_pqZ9SP6nmcvBkb9tCPfLaO1nA_yI72-dX6aRbL-GPmPML0dw0wyM4aovNA3so69mGKbhy2XQCr2fhSFMey3kLiRi9LoZirbeAlVsM1LwMxuQNIovvqlMa2ZKmr8HVhdlLnua5cZBZkTQEarAjdVhlgK6w8tfONJcOJ-YNC2eWZz775T04UuOZepJj5M3Efr2qgR9rnwwQrLDd9ecII71Qrek9GpcJ2yaYx4Xn5rRS825aHkl-arv-1JFwdqI5Rt0STnkaMoMANzCiU2P9MIYQr5-xIis9tsBIpiJz2QpCHaq2xtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است  #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658116" target="_blank">📅 20:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658115">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ترامپ: بدون من، اسرائیلی وجود نداشت
🔹
رئیس دولت تروریستی آمریکا در گفت‌وگویی با سازمان رادیو و تلویزیون رژیم صهیونیستی گفته است بدون من، اسرائیل وجود نداشت
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/658115" target="_blank">📅 20:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658114">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cz0YlV4dj473aB36xCGDiyCMz2xeSCEDO_WvaRu-2ODDEAk0kdF2k0hHhdt9qPtfXeX_mzh54n9vvyNEeJhlmSzr5d5z57xQJWfRYWLvx95FoQhGRPgIcpAgnjkHORlsun4KQcSREv4j_YKUk2O_ek717FPI-NjkSSpfZFN-22kFwockBPdbC6D_ZovfBnmpzMNc-_A7FRzrrz7bIsa0m2MLNziS_2F39Sp8pRRdoY5lVLPneti-AEZUAZpUUBQwQ5ugoLqaOHuWcdlpjd8mmIb_etHZLIkpipIph8oK9z8Ehg4Eo1bf3jwIuxe7dEL3fP6b36D7C1-HTIAT9wa3Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور بانک سینا در جمع ۵ بانک برتر کشور برای دومین سال پیاپی
🔹
بانک سینا در ارزیابی بانک‌ها و مؤسسات اعتباری از سوی بانک مرکزی در چارچوب شاخص CAMELS، برای دومین سال پیاپی در میان ۵ بانک برتر کشور قرار گرفت.
🔹
بر اساس گزارش خبرگزاری وابسته به بانک مرکزی، در ارزیابی انجام‌شده برای شش‌ماهه نخست سال ۱۴۰۴، وضعیت بانک‌ها بر پایه پنج نسبت مالی کلیدی شامل نسبت کفایت سرمایه، نسبت بدهی به حقوق صاحبان سهام، بازده حقوق صاحبان سهام، نسبت کفایت سرمایه لایه یک و نسبت مالکانه مورد بررسی قرار گرفته که بانک سینا در این ارزیابی، برای دومین سال پیاپی در جمع ۵ بانک برتر کشور قرار گرفته است.
این شاخص‌ها از مهم‌ترین معیارهای تحلیل مالی بانک‌ها به شمار می‌روند و در سنجش توان مالی، ساختار سرمایه، سودآوری و میزان ریسک‌پذیری نقش تعیین‌کننده‌ای دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/658114" target="_blank">📅 20:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658113">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9195af6679.mp4?token=ee3vn7D2ql98Rrp4EPB4UU694CSGa5XLLUIW-T9IOfAYJke9NCmlUrRkKm9U5j4VZIi_1HAbWKWI6pzmjIStWbUcC2McQYGNIpzNlvg8NiGZ2np8TxpTUp2yy_3EqKWsJO1H-LSF2yBoJNJYbkzCOkxvOJz5NHDM7GlevR7-CD8Yr7FVmQ6Utk4ZYd69Nw0_-j1m0ta7Ar5yyIouO7GOnGKxlFkvEYIXIRg2XksW1WXOt0Tt9MmPFgjD2pr79u5xV3_Tqs8qPLxv3pTFKloChonsBYmvCp2DhmFIIqD0eqnjzSZ-Ck-gqUrGVMBXiViI2RDRltJ384_H2rkJVJlgIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9195af6679.mp4?token=ee3vn7D2ql98Rrp4EPB4UU694CSGa5XLLUIW-T9IOfAYJke9NCmlUrRkKm9U5j4VZIi_1HAbWKWI6pzmjIStWbUcC2McQYGNIpzNlvg8NiGZ2np8TxpTUp2yy_3EqKWsJO1H-LSF2yBoJNJYbkzCOkxvOJz5NHDM7GlevR7-CD8Yr7FVmQ6Utk4ZYd69Nw0_-j1m0ta7Ar5yyIouO7GOnGKxlFkvEYIXIRg2XksW1WXOt0Tt9MmPFgjD2pr79u5xV3_Tqs8qPLxv3pTFKloChonsBYmvCp2DhmFIIqD0eqnjzSZ-Ck-gqUrGVMBXiViI2RDRltJ384_H2rkJVJlgIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: کشورهای عربی میانجی‌گر بدانند ما زمانی اتمام جنگ را می‌پذیریم که جنگ در تمام جبهه‌ مقاومت به پایان برسد/ صهیونیست‌ها بدانند مسیر اتمام جنگ اینگونه است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/akhbarefori/658113" target="_blank">📅 20:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658112">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ادعای عبدالخالق عبدالله مشاور سابق بن زاید: امارات در حال هموار کردن راه برای کاهش تنش با ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/658112" target="_blank">📅 20:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658111">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🎬
#تماشا_کنید
↗️
✅
تحولی در مسیر اعتماد؛ گزارش دستاوردهای بانک تجارت در دوماه ابتدایی سال ۱۴۰۵
‌
🙏
بانک تجارت در ۲ ماه نخست سال جاری، با تکیه بر سرمایه اعتماد مشتریان و اتخاذ رویکردی مدرن، گام‌های بلندی در جهت توسعه و پایداری برداشت.
🌐
گزارش ویژه
👉
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/658111" target="_blank">📅 20:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658110">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
از دلیل عدم اجازه ورود به نور تا ماجرای عذاب قهر با پدر و مادر
🔹
00:12:50 تاریکی مطلق و حضور دو موجود وحشتناک
🔹
00:29:50 عدم اجازه ورود به نور
🔹
00:35:50 پیغام پدری برای فرزندانش که ۱۵ سال با یکدیگر قهر بودند
🔹
00:52:30 ماجرای شنیدنی از وابستگی و دلتنگی همسرم به من
🔹
00:58:50 فضای مملو از مه گل‌آلود
🔹
01:01:10 عذابی که در جهت قهر با پدر و مادر متحمل شدم
🔹
01:14:30  رؤیت علت مرگ و جایگاه ۵ نفر از اطرافیانم
🔹
قسمت یازدهم (صدای سخن عشق)، فصل چهارم
🔹
#تجربه‌گر
: مسعود نبی چنانی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/658110" target="_blank">📅 20:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658109">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
وزارت خزانه‌داری آمریکا چند فرد و نهاد ایرانی و چینی را به فهرست تحریم‌های خود علیه ایران افزود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/658109" target="_blank">📅 20:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658107">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
هشدار حنظله به نیروهای آمریکایی‌: آمریکایی‌ها درصورت هر اقدام علیه ایران باید جنازه سربازان خود را از مخفی‌ترین پایگاه‌های خود خارج کنند‌
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/658107" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658106">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usYDmbHA77vNArlBxG9o4hkG_xu3dj1eDRxkn5fdYnc37moKH_KnvjoeRoUEB505vg4VUh5QU90I_obqGNCNU0DiE1WkigHovGs3UVM9oxbHBtHz3gWRDglLZFaHW2M-biuiCQKoLh0ELuxwkmD40jBVJKXtZgvPJ3GIjBSXRF1fv0UWWJiqs995Ux5enjCpcolkH1oDgnZSuVTx56zcDFkQxAqFv5D3Cjs5ay9d9Wnwjc40tgPt1yzac2MTcVvODSFubKxw6FBV_oj276EMj8masu5XZ40lQJz_h4ItgWsQlrq9i0oHR6qxcm-QdzqpIc4ar0RkxjUk2q7-3M_COg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: زیرساخت‌های حیاتی، شریان‌های زندگی مردم‌اند
رئیس‌جمهور:
🔹
زیرساخت‌های حیاتی، شریان‌های زندگی مردم‌اند. تهدید به هدف قرار دادن آنها از شبکه‌های حمل و نقل تا صنعت برق و آب نه نمایش قدرت بلکه نشانه استیصال در برابر اراده یک ملت است.
🔹
ایران با تکیه بر دانش و توان متخصصان، وحدت ملی و همبستگی، در برابر هر فشار و تهدیدی استوار خواهد ماند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/658106" target="_blank">📅 20:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658105">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52cdfb59be.mp4?token=bY8nyUxTfqy3Wo0iS6sX5R8kkpU8R4CyIuQR76JnnACSRSxJMLRFbuKRImZeztHA8HI8mz1hmz0GDN_OqD8XradVItW4V40_5RNxiZGxnUQWDqfUIplwRlJsuMrEzr7nLlh498DYD6zRJovwYbfYbcftUyB0Sar75ghAyDaPlX5GtB4Ic8173Zk8SVdVzwdn80iALqTyAYIN09gLiLN31NHuXKegM7TZ5tTorI15YPpf8wPHfWJ5bZVBstojxE7qmwY0gsKhf36E7mBWkLjmX3a1TbFs-MijtlBOs6AvxDs08h-8NEdw-wi5Cg9J4ivNgAkvDRTPBdLQ4zXhIkcgQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52cdfb59be.mp4?token=bY8nyUxTfqy3Wo0iS6sX5R8kkpU8R4CyIuQR76JnnACSRSxJMLRFbuKRImZeztHA8HI8mz1hmz0GDN_OqD8XradVItW4V40_5RNxiZGxnUQWDqfUIplwRlJsuMrEzr7nLlh498DYD6zRJovwYbfYbcftUyB0Sar75ghAyDaPlX5GtB4Ic8173Zk8SVdVzwdn80iALqTyAYIN09gLiLN31NHuXKegM7TZ5tTorI15YPpf8wPHfWJ5bZVBstojxE7qmwY0gsKhf36E7mBWkLjmX3a1TbFs-MijtlBOs6AvxDs08h-8NEdw-wi5Cg9J4ivNgAkvDRTPBdLQ4zXhIkcgQ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: براساس اطلاعات دقیق و میدانی، تعداد کشته‌های ارتش آمریکا تا به امروز ۵۰۰ نفر بوده است/ آمار منتشر شده از سوی ارتش آمریکا مضحک و خنده‌دار است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/658105" target="_blank">📅 20:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658103">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bL722eldOba1tZwbpYhKbdg-HiPpFY5bOKXShKu35ZscFL5c_7ZlxlF1u7Emrf0UXUpPqBKmGE543pUrhDAdm8sp1mBhoafdR6KtUzGWki84PP3_AudY-iO5k-Yeg8aLrmNi1tfHlGUg2YWl1KXVV9WKoMikZ5gcPkPwdGWb3ST6wI77J6kt2zO_UYqYhaQhngo_QoeKX8KdwMPoiU1eupgY2msoBZVgjqVfyX5ruxxAbH8G9D76Ja3kGJTuveeLsd_9VC4nOcEW5Dy__qh2WY45rWHkbEAATgZA_AheHzD-7biDF0Y1nN391nplBVQLe_hgY7GAGUHF27FkgPX_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnIYrs9MZfG_OSG_qemAr5IoaTXiDmT30rvbKO0Y6O569YNDbnV0lNK1agkhTY7csnOiOxUAmJCBlNcYBxjeXsUWfxHLurd-b0hxR-VQlTLqrTnNbCrJroMjzbZMOTnk0xWDk-ItuOnszbWVrbocF4c5KpW59i2pX2Kef27zrNK9WIZCcJQ85g3XmboJmC1rMutCrxXqUKUggjSclHGPlrJjU6xoB95Jgjw4-C2qAypOI-oFvFxbTq3VgcGCdt7dj0UXSlKDUkbVhcaAOE5WYWzG7PKT-X6MDUb1tkOej8hoP3v_rAGvV7pcMxq2rCIZqKJ8IpC_Uuv_8Z52vuaahA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: نازنین
🖋
نویسنده: فئودور داستایوفسکی
🔹
«نازنین» داستانی کوتاه اما عمیق درباره عشق، سوءظن، تنهایی و خودفریبی است؛ جایی که راویِ نامطمئن، حقیقت رابطه و فاجعه‌ای پنهان را لایه‌به‌لایه آشکار می‌کند. اثری رازآلود و تأثیرگذار.
🔹
مطالعه این کتاب به کسانی که به واکاوی ذهن انسان و روابط پیچیده انسانی علاقه دارند، توصیه می‌شود.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/658103" target="_blank">📅 20:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658102">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سخنگوی آتش‌نشانی تهران: ستون دود سیاه رنگ در جنوب تهران مربوط به آتش‌سوزی انباری در میدان قیام است
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/658102" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658101">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام: روز سه‌شنبه یک نفتکش را در خلیج عمان پس از آنکه درحال نقض محاصرۀ دریایی ایران بود، از کار انداختیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/658101" target="_blank">📅 20:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658100">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYmUM0Zq7J_fVW4AJZkCHXQWVgXcV9h4v6mSoTFHV29j1MuEQSpZEwmwxvWf7dNKuAS_UtBkhb8H6HK_5FCYoPPQc_ZCGNIdF6Ws8D0RcUR7TlCghh2mkkHB_XPNGRVQNEIsWnT4ucYhnBj3FSTdgWTcNEeFdBUT4KrAwxMwiB7rBWOwWZbapYYXkA7TSeKT521aOvjCe8NcswZVSzmsj9-usnGi18eWEM95YUJ8vfImvrzHjVIueCrnU-4wN2c9-UPJRcR3m51gNDhEYomaYnxPoBWTDG57MBV4RX57uGoTKTDPIDtdzJgG1rEzXhRzzozVl83ypXVdOnoPAryTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون سازمان زیباسازی: شهرآرا؛ خانه ای برای رسم نوآورانه در شهر
🔹
حمید عسکری عاون فنی و عمرانی سازمان زیباسازی شهر تهران در آیین گشایش «عمارت شهرآرا؛ خانه طراحی شهری و مرمت بناهای تاریخی تهران» گفت: این مجموعه بستری برای تبادل تجربه، گفت‌وگوهای تخصصی و شکل‌گیری و رسم ایده‌های نو در حوزه طراحی شهری خواهد بود.
🔹
وی افزود: فضای مناسبی برای نمایش دانش، دستاوردها و تولیدات حوزه طراحی، مبلمان و تجهیزات شهری ایجاد شده و محصولاتی همچون پایه‌چراغ‌های هوشمند، نمایشگرهای دیجیتال تبلیغاتی، نیمکت‌های چندمنظوره و دکوراتیو، تجهیزات نورپردازی و سایر عناصر طراحی شهری در آن ارائه خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/658100" target="_blank">📅 20:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658099">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سازمان تروریستی سنتکام: روز سه‌شنبه یک نفتکش را در خلیج عمان پس از آنکه درحال نقض محاصرۀ دریایی ایران بود، از کار انداختیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/658099" target="_blank">📅 19:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658098">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
قطعی آب سیریک پس از حمله آمریکا در ‌‌۱۲ ساعت وصل شد
مدیرعامل شرکت آب و فاضلاب هرمزگان:
🔹
در پی حملات بامدادی آمریکا، خسارت فراوانی ‌به مخازن ذخیره آب ۵۰۰ و ۲۰۰۰ مترمکعبی شهر کوهستک و بخش بمانی شهرستان سیریک وارد شد.
🔹
از صبح امروز ‌تیم‌های کارشناسی، نیروی عملیاتی، رانندگان ماشین‌آلات و عوامل پشتیبانی با استفاده از اتصالات، لوله‌ها و ماشین‌آلات مورد نیاز عملیات جایگزینی تأسیسات آسیب‌دیده و ایجاد خط انتقال جدید آب را آغاز کردند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/658098" target="_blank">📅 19:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658097">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/723629509e.mp4?token=kx14xjcFACdNek50YAMC-6R8sIq2pzuZHJBBaY7C0MIbPiX7f5NTc18sLhFbPySCKy6bEUw7hoXQbTqTPltFp9KI2TrhnOwS3fJaln4fjY8tHdnLk5ucSXMDhzj82gFGnHn9ANDvV2L93cLL9rym_83XMqyoIip59wDw7E2pelkxc6JcEQO91SUHiNEMmhhOwCNpWwFxpfqLFIaoXGP6Cpy-lS_ji6Qq5ckkodgQC5Du7Vl9jgxm037jS6Jadhl-h8KFV_jxPY3v0hAgrCu2yp0Irfgzw7KuQAjjc2x2ysSwKd6aWipx_g5tobM1CTX6WrdvlUq1Vh7cDNoGdKLBww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/723629509e.mp4?token=kx14xjcFACdNek50YAMC-6R8sIq2pzuZHJBBaY7C0MIbPiX7f5NTc18sLhFbPySCKy6bEUw7hoXQbTqTPltFp9KI2TrhnOwS3fJaln4fjY8tHdnLk5ucSXMDhzj82gFGnHn9ANDvV2L93cLL9rym_83XMqyoIip59wDw7E2pelkxc6JcEQO91SUHiNEMmhhOwCNpWwFxpfqLFIaoXGP6Cpy-lS_ji6Qq5ckkodgQC5Du7Vl9jgxm037jS6Jadhl-h8KFV_jxPY3v0hAgrCu2yp0Irfgzw7KuQAjjc2x2ysSwKd6aWipx_g5tobM1CTX6WrdvlUq1Vh7cDNoGdKLBww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: وقتی جنگ تمام شود، تورم مثل سنگ [از صخره] پایین خواهد آمد ‌
🔹
میلیون‌ها بشکه نفت را [از تنگه] خارج کرده‌ایم، که امروز برای اولین بار اعلام می‌کنم، اما ما مدت‌هاست میلیون‌ها بشکه نفت را خارج می‌کردیم. هر شب نفت را خارج می‌کردیم. ‌
🔹
اما حالا به…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/658097" target="_blank">📅 19:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658096">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
ترامپ بازهم پایین آمدن نرخ تورم در آمریکا را منوط به پایان جنگ با ایران کرد! #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/658096" target="_blank">📅 19:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658095">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f245a6dbef.mp4?token=ONAz8UDtoUqCNCdTPQ8XA1lUMDKvlncMknhl07EMuy-PiiXgjz5EekObh9TmkZD0xB7xuDt23LqmKv2ALkb5O9yPqiig9XJeGbomzYh1oF2ffEZpk2nvnfDqPdlJVu8_ObdMWz5xIf6uHv4iofUPpvAXsLoND5PAXIzW377Z7ThOb97EoTkfjkYhQcmvzkXEZdphfKfg7Xd_NRpJSfUg0-Q_ZsuUGryqcTD1d6bdNVv4OfGU6oLQK-_S00RCHOAfehhNwnA_LtaUy3MHEvJXCL2Sla86yFXMZgVK17xsXId1EYVCopoDh5NPF8qZ-9Sh6OL-AYyLUBuDBa6WNTDOBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f245a6dbef.mp4?token=ONAz8UDtoUqCNCdTPQ8XA1lUMDKvlncMknhl07EMuy-PiiXgjz5EekObh9TmkZD0xB7xuDt23LqmKv2ALkb5O9yPqiig9XJeGbomzYh1oF2ffEZpk2nvnfDqPdlJVu8_ObdMWz5xIf6uHv4iofUPpvAXsLoND5PAXIzW377Z7ThOb97EoTkfjkYhQcmvzkXEZdphfKfg7Xd_NRpJSfUg0-Q_ZsuUGryqcTD1d6bdNVv4OfGU6oLQK-_S00RCHOAfehhNwnA_LtaUy3MHEvJXCL2Sla86yFXMZgVK17xsXId1EYVCopoDh5NPF8qZ-9Sh6OL-AYyLUBuDBa6WNTDOBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ مدعی شد: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و ما آنجا قدم زدیم/ تنها کاری که ایران باید انجام دهد این است که امضای سند توافق را آغاز کند؛ این توافق به طور کامل مذاکره شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/658095" target="_blank">📅 19:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658094">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
ترامپ مدعی شد: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و ما آنجا قدم زدیم/ تنها کاری که ایران باید انجام دهد این است که امضای سند توافق را آغاز کند؛ این توافق به طور کامل مذاکره شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/658094" target="_blank">📅 19:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658093">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
ترامپ قمارباز: ما میلیون‌ها بشکه نفت را توقیف کرده‌ایم
🔹
هیچ‌کس از این موضوع خبر ندارد. می‌دانید چه کسی از آن بی‌خبر است؟ ایران؛ تا همین لحظه.
🔹
ما چند شب پیش، در دل شب و بدون روشن کردن چراغ‌ها، ۲۲ کشتی را توقیف کردیم؛ چرا که آن‌ها [کشتی‌ها] رادار ندارند.…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/658093" target="_blank">📅 19:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658092">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
ترامپ متوهم: ایران مدام ما را احمق جلوه می‌دهد #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/658092" target="_blank">📅 19:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658091">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1fed6b11.mp4?token=SOZ0shL5oj9PciFW9uj-rdMb5c5EtrdkzKM05WqhQKB70hKYRa0bYsFTuEWBd5g2ueXW43evSNY4HjOXoqYyjK90Lh2PMCDC3S4HE8Fynm94OzZWcm1zfClOYCHVdmA19OYgzQKeY2gV7E2Kuf82UgMjMAsMN0i2iLvBwz_jBkAB0tiCmFlFZY4Il4_JhFL6HOFH-edWhVqSgKx5vxdMtzFBZpCm2EHTanpjAQ1csSeVbcV_JqdNjEjWCef7hZcaGsUjExlibxLkG9nrZe8l3xmTGKsmRsDZ5pMH-2PA6iEWgslbFfoG4ioyJ8wKbtG6TGS2611Iu0r0QJPoGb1IWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1fed6b11.mp4?token=SOZ0shL5oj9PciFW9uj-rdMb5c5EtrdkzKM05WqhQKB70hKYRa0bYsFTuEWBd5g2ueXW43evSNY4HjOXoqYyjK90Lh2PMCDC3S4HE8Fynm94OzZWcm1zfClOYCHVdmA19OYgzQKeY2gV7E2Kuf82UgMjMAsMN0i2iLvBwz_jBkAB0tiCmFlFZY4Il4_JhFL6HOFH-edWhVqSgKx5vxdMtzFBZpCm2EHTanpjAQ1csSeVbcV_JqdNjEjWCef7hZcaGsUjExlibxLkG9nrZe8l3xmTGKsmRsDZ5pMH-2PA6iEWgslbFfoG4ioyJ8wKbtG6TGS2611Iu0r0QJPoGb1IWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای سگ‌زرد: دیشب به آنها حمله کردیم، امروز حمله سنگینی به ایران خواهیم کرد #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/658091" target="_blank">📅 19:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658090">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYx4hvdFPjbnzxnyD1kByWcYIUDNppFUboC0CRie614ElFstZ-4O4htgQZ_VHKXHGrGAdfoJgW_IWXjSsINgcJbyimb9u3FivseCAIm-muf3HLSDx5VqK0SaSCoabE7_FcRWZtCB0JQ10JRt71uHVJjwQjkw6-9OcUR3RPST9RVVRbkqtaJN9vEcLQ-6oWfYRS2wUPM26zX8O4pej9X06qY8hu2ZW3gggY3DpjfYhB69-S8OuiQk-xHlXh7Bq-NCbjtvN9IiIzFr07nEAX2uscWTZQqxowsPFNrCIyAaXnDhVOj1wXD7OslLsmC8psA0es_UnMMJaKkGwXJq6pQG6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقتی فوتبال لباس می‌پوشد | داستان محبوب‌ترین پیراهن‌های تاریخ جام جهانی | سفر به نوستالژی جام جهانی
🔹
برخی می‌گویند زندگی را می‌توان با جام‌های جهانی اندازه گرفت؛ نشانه‌هایی چهار ساله در خط زمان زندگی، از دوران کودکی تا نوجوانی و بزرگسالی. مجموعه‌ای از خاطرات فوتبالی؛ تیم‌هایی که دوست داشتید، قهرمان‌هایی که تحسین می‌کردید و پیراهن‌هایی که به نماد آن دوران تبدیل شدند. موضوع دقیقا همین پیراهن‌هاست؛ لباس‌هایی که داستان تعریف می‌کنند و به آثار ماندگار تبدیل می‌شوند. اما چه چیزی باعث می‌شود میراث یک لباس فوتبالی تا این اندازه پایدار بماند؟
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3221763</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/658090" target="_blank">📅 19:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658089">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4FOK6ayOlvMNnz-ma62Z4lSCFjcHzh9uR3kBJOamrUSvyZtNjK4RtpleXh7StHsYg1waJZMxqTRdjHgFbJ7qs_FSIihqINyNjKLHAjRazYFvI9FUtIDkkwTPKsMJm4XbMC4fH2m1L5KgwkarO5Sr9XjWunwY6wjdn_qa8aXV2Vdy12ZyTRVC4LhVuxCnk5LtgLZEIfTNxopwiHKA6hFVGu12B-CkX9XfKt494zOKAB5wgd7IlMtiHYhqD2srlk3RhqdJef4YSb3mCm_ERaycq1r9eIGRiiecMKdZgpWrYuRBfmNsGVGxEdI-04WxzZXJA77lqBCTheYmmVhjk6C7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/658089" target="_blank">📅 19:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658088">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: من چندین ماه است که با ایران در حال کار و مذاکره بوده‌ام و آن‌ها باید این توافق را امضا کنند. این توافق، توافق خوبی است
🔹
پاکستان همچنان در تلاش است تا برای دستیابی به یک توافق با ایران کار کند.  #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/658088" target="_blank">📅 19:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658087">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
گزافه گویی ترامپ: واشنگتن ممکن است بار دیگر با قدرت و قساوت به ایران حمله کند؛ یا با ایران به راه حلی می‌رسیم یا آن‌ها را نابود می‌کنیم #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/658087" target="_blank">📅 19:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6475ac6ebc.mp4?token=WfGutBDpud_cZnq7CDGfSDutQhF-dtFeXv6ZZH6nwuuW5IUb6MQ0rx9H-EkFknaCj8CB72VVLC7NI1FRumWgkhQlGNQLjFfqL15fVE2tudbUteBvKpEGhmrYwBtda9H8zEtjDS2albPLRMx3HAP8eXdGMpr-EUZnfbA7UHCFayM2uJOnV43rf5YWnIIzr0A_EYNJkLWbNzQ9jS-4hshV68MxKypfkMySEIuYYblITvrBpIRcIXINoScgdD2op9nv6ehZe81lZW2KeZd33uAy5yd4FoJVq_qK3z5ajPI5rdNoTxJ_8uhadCVzohRz68fDPuUE3G6O0ek_NIwYVzkBIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6475ac6ebc.mp4?token=WfGutBDpud_cZnq7CDGfSDutQhF-dtFeXv6ZZH6nwuuW5IUb6MQ0rx9H-EkFknaCj8CB72VVLC7NI1FRumWgkhQlGNQLjFfqL15fVE2tudbUteBvKpEGhmrYwBtda9H8zEtjDS2albPLRMx3HAP8eXdGMpr-EUZnfbA7UHCFayM2uJOnV43rf5YWnIIzr0A_EYNJkLWbNzQ9jS-4hshV68MxKypfkMySEIuYYblITvrBpIRcIXINoScgdD2op9nv6ehZe81lZW2KeZd33uAy5yd4FoJVq_qK3z5ajPI5rdNoTxJ_8uhadCVzohRz68fDPuUE3G6O0ek_NIwYVzkBIoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه گویی ترامپ: واشنگتن ممکن است بار دیگر با قدرت و قساوت به ایران حمله کند؛ یا با ایران به راه حلی می‌رسیم یا آن‌ها را نابود می‌کنیم
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/658086" target="_blank">📅 19:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaR4yU6ONpmjdejX1k5kw9aS3rgJ1AZAjmTFaSqf5dWffuDfRctt_eyfhLwoGHypH50KaMCaFax7xiPf6Ae6s8_JMhPo6Qbal0IEr11fKOvs7nEuC-7HeciQ5d05Xmqu8EDq1WgpOreTSgfOErykm7NNZZWnPcvTykRyn9r4Pg37bUcyiLRnK98McSC2OkhvQOXi5dtQfgvy_lK-iaofmszMVk8OiDjlMqyxwGb--nqDDX_72ATTMvHGGkNlQHtSqLe393N7O_SETUuBhcr3DbcQ3NamVhMudv6qh-zHc2ieZIJl7mcFVHDDqMMkOr-WK9K3N4Cv6f37IncBqyI2OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت سفارت ایران در ارمنستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/658085" target="_blank">📅 19:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
نماینده مجلس: افزایش ۴۰ تا ۶۰ درصدی حقوق بازنشستگان تأمین اجتماعی/ زمان واریز حقوق مشخص نیست
جعفری آذر، عضو کمیسیون اجتماعی مجلس شورای اسلامی:
🔹
افزایش حقوق بازنشستگان صندوق‌های کشوری و لشکری بدون تأخیر اجرا شده و بازنشستگان کشوری از ابتدای سال افزایش ۲۰ درصدی حقوق خود را دریافت کرده‌اند.
🔹
احکام افزایش حقوق بازنشستگان تأمین اجتماعی نیز صادر شده است؛ به‌طوری که حداقل‌بگیران حدود ۶۰ درصد و سایر سطوح بیش از ۴۰ درصد به همراه مبالغ ثابت مصوب، افزایش حقوق خواهند داشت.
🔹
هر زمان پرداخت‌ها بر اساس احکام جدید انجام شود، معوقات ماه‌های گذشته نیز به بازنشستگان پرداخت خواهد شد./ جریان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/658084" target="_blank">📅 19:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc7752550.mp4?token=OgpkF2qUXXHicevAPpb7VtwbqoqApZTgQdw0O-u30a90QRt3ayINgRZoRP2LcN2jEU291FJYmTnJqOkCTfefAQ1pHUjexyV9uVYOSecytjWYLyqH3ioMvSRvBoksvA8oowwJHMIDShERnMwGm2IttK7wiAthYKeb31qbNdbqgA2uaT_4rLqtcTaiflHh7-ucUzDZFqJGgPJhTaLLDa2liYssRjhqN7k9Khm6_futIj5YU4L91bBa-9IfDYua9Ikd28SAh-Fb2eNU2E_umRgvzgk_8AZRMpkGrHaY74uADKtNGML0J930TFbnjRf5LoqiBKYe6GYvU_0LD5K4MIcSbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc7752550.mp4?token=OgpkF2qUXXHicevAPpb7VtwbqoqApZTgQdw0O-u30a90QRt3ayINgRZoRP2LcN2jEU291FJYmTnJqOkCTfefAQ1pHUjexyV9uVYOSecytjWYLyqH3ioMvSRvBoksvA8oowwJHMIDShERnMwGm2IttK7wiAthYKeb31qbNdbqgA2uaT_4rLqtcTaiflHh7-ucUzDZFqJGgPJhTaLLDa2liYssRjhqN7k9Khm6_futIj5YU4L91bBa-9IfDYua9Ikd28SAh-Fb2eNU2E_umRgvzgk_8AZRMpkGrHaY74uADKtNGML0J930TFbnjRf5LoqiBKYe6GYvU_0LD5K4MIcSbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری جدید از جنایت آمریکا در مناطق مسکونی تهران
🔹
حاوی تصاویر دلخراش
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/658083" target="_blank">📅 19:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
عضو کمیسیون امنیت ملی: طرح تنگهٔ هرمز آماده است
کوثری:
🔹
همهٔ اقدامات و بررسی‌های لازم دربارهٔ تنگهٔ هرمز انجام شده و کمیسیون امنیت ملی مجلس نیز کارهای تخصصی مربوط به آن را به سرانجام رسانده است.
🔹
این طرح پس از آغاز به کار مجلس، در دستورکار قرار خواهد گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/658082" target="_blank">📅 18:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658081">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
قبل از خرید و فروش سکه پارسیان؛ بخوانید
یوسف تقی زادگان، رئیس اتحادیه طلا و جواهر مشهد:
🔹
فروش پلاک طلای پارسیان دارای بسته بندی را برای تولید کننده‌ها ممنوع کردیم که از پک‌ها خارج کرده و به صورت فله در اختیار مردم قرار دهند. هر کسی که پلاک پارسیان را به واحد صنفی می‌برد، باید از پک خارج کرده وزن کنند و چنانچه وزن آن مغایرت داشته باشد مشتری را راهنمایی کنند که به واحد خریداری شده مراجعه کند اگر فروشنده پذیرفت که پول را دریافت می‌کند اگر قبول نکرد به اتحادیه مراجعه و طرح شکایت کند ما پیگیری می‌کنیم./ اخبارمشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/658081" target="_blank">📅 18:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658080">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGIElUtmRy6qUjuZssjb8BqADZmZ9P2Y_AfdFgb7l_E21B23DiLh_FD6rkOb55X_3vx5Qcy1O6JK6H0fPKM8lYNRcXyFLmP76QZERm_iCED7zNxiyImkATABLzp9gE3h-Q7uF2hJhYOuN7tXUv9b7vGNjaT4nJCz90kmBpwfTEmuvNqpTvj80Z0zgBUwDqcYRmUQLoQdT93CPi9lJeRhqfMYsfY8lMpgF8-1AtQsu_adhxJKscRDQih0XbHCRgGjBg73yE8MWjCrTFVB1Lew7Hu2WUng57atmmnfV9SnH0dBuahVzHfBo4_cmIMv3s2Fzvv_fGqNltKgbMRPPejffA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/658080" target="_blank">📅 18:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658079">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICOx2V3zXT-1ISsOcxFS4D9x_3mql9dgof2DX8_59WOLR12Ub3HWBeHaqNstjEA-wyXdhVykgjusgDtaSUvXwI72hcoqMuORl-P4UEZqwG4Dyt-sJZi4caJsAnq-QtGXJ8YlRK9uHHAG3cQZFFSjCPMe0jmfWgXzRtY1FF4UPcVIZx1BV7tLozl6XZhHep1-oBirXXTtMB2zo5n3ssEm4bjPBvC-gO1bfHNbVlRVa63pnTQKrmXJPmplgxFg0pAMnZQUv0cuVLWtUyV9uXP4oZ-6DKxuAZBfz2tc37cMDfvlryIHCB4XRmWY1bQ7Hq1Wzo3VWWcB47VaryElJ0-IaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طارمی: سیاست‌ ویزایی آمریکا باعث تنش در جام جهانی است
مهاجم تیم ملی ایران در مصاحبه با ESPN:
🔹
اقدامات دولت آمریکا در رد برخی درخواست‌های ویزا و جلوگیری از ورود یک داور سومالیایی، به وجههٔ این کشور آسیب‌زده و باعث ایجاد «تنش زیادی» در فضای جام جهانی ۲۰۲۶ شده است.
🔹
در ۳ جام جهانی قبلی که حضور داشتم، همیشه وقتی وارد کشور میزبان می‌شدیم، حس صمیمیت و جهانی بودن فوتبال را احساس می‌کردیم. اما متأسفانه اکنون چنین حسی ندارم.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/658079" target="_blank">📅 18:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658078">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
احد عظیم زاده، مالک لاکچری‌ترین فرش دنیا را بشناسید!
🔹
روز ملی فرش گرامی باد
#فرزند_ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/658078" target="_blank">📅 18:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658077">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
یک زخمی و دو مفقودی در پی آتش‌سوزی نفتکش  سازمان تجارت دریایی انگلیس:
🔹
در پی آتش‌سوزی در اتاق موتور یک نفتکش، یک نفر زخمی و دو نفر از خدمه مفقود شده‌اند؛ این نهاد، هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است./ خبرفوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/658077" target="_blank">📅 18:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658076">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jINc4OsV0f-eDPqgWAcuKhBLswKOvx9BNPkhSHKLeSIJZE94idAzyv6wwkqAohPVN0IIB-qXjQ-w_qyhv6jPNlEdm_QaYDcCK0cgzsNBMdsvAVPzOmq_5-qddPeGAoMvS_GHRhq-zdW7pu03B3vkcsy4o8INfAfloeguI1XHU4mXoUnPLPDnEaTMCEflZr6EQJg_A5tYyhH37op7cEaF6jhCeYzqppTiQCcMNJrLF0-ihZaXmCv-jADOEzdvKwGIrApJ3PapSu4qKO45ZiO3OfSdP839WaKf8fmY7WiS92fIZ3JR7dT9qzHS6cNlEnL-mFdr5ICMNpBGsvrSHHzJfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابوزید بلخی، نابغه عصر سامانی و نخستین روانشناس
🔹
او از نخستین اندیشمندانی بود که میان بیماری‌های جسم و روان تمایز گذاشت و برای درمان اضطراب، اندوه و وسواس راهکارهایی ارائه کرد. او در جغرافیا نیز پیشگام بود و تصویری دقیق از جهان زمان خود به جا گذاشت. اندیشه‌هایش…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/658076" target="_blank">📅 18:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658075">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
۵ کشتی حامل ال‌پی‌جی از محاصره دریایی آمریکا عبور کردند
🔹
بر اساس پایش هوش مصنوعی دریایی «ویندوارد»، پنج کشتی حامل ال‌پی‌جی که با ایران تجارت می‌کنند از محاصره دریایی آمریکا عبور کرده‌اند.
🔹
در حالی که ترامپ مدعی شده بود «هیچ چیز» بدون اجازه آمریکا عبور نمی‌کند، داده‌های ماهواره‌ای کپلر نشان می‌دهد چهار کشتی محموله خود را در هند و یک کشتی در پاکستان تخلیه کرده‌اند و صادرات ال‌پی‌جی ایران ادامه دارد./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/658075" target="_blank">📅 18:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658074">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
سردار شکارچی: هر تهدید ترامپ را با تودهنی پاسخ داده‌ایم
سخنگوی ارشد نیروهای مسلح:
🔹
به‌هیچ‌عنوان در مقابل نظام سلطهٔ جهانی و شیاطین عالم، به‌ویژه ترامپ و نتانیاهوی خبیث، کوتاه نخواهیم آمد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/658074" target="_blank">📅 18:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658073">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1df010c4d4.mp4?token=nQuqdtqyI_giwI1cmL-8g6ffFkKWjN-I-K_QHvATuTGY7ZuvWD90cC5T-IltKEUhFUxTV1WaeaBh0iAmk3Y_0lxlw2qWe3UH7KOPcMrwhYZXgDvIg5VYeg2y9N8Zkilf8HVVNBideVzvhfh-UW_sdeCVrT8EbMW8RDj3plUTx6MDO1NO78y84gZImbg-yrEOSET6F7XDlnT7HDBmrGBkwLF69KcbP8KElbgVSaqiwBw6Phv1SNkFffZKfEJPPCvOmjOwA8YifSn4AWqcgYa2s0CS1mfOH9wBb4f2R4-4RaJY5yjZrNa3WulgreTXbD5WJyjXCP1b8SO0Oc7is_k_6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1df010c4d4.mp4?token=nQuqdtqyI_giwI1cmL-8g6ffFkKWjN-I-K_QHvATuTGY7ZuvWD90cC5T-IltKEUhFUxTV1WaeaBh0iAmk3Y_0lxlw2qWe3UH7KOPcMrwhYZXgDvIg5VYeg2y9N8Zkilf8HVVNBideVzvhfh-UW_sdeCVrT8EbMW8RDj3plUTx6MDO1NO78y84gZImbg-yrEOSET6F7XDlnT7HDBmrGBkwLF69KcbP8KElbgVSaqiwBw6Phv1SNkFffZKfEJPPCvOmjOwA8YifSn4AWqcgYa2s0CS1mfOH9wBb4f2R4-4RaJY5yjZrNa3WulgreTXbD5WJyjXCP1b8SO0Oc7is_k_6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو وایرال شده از نجات معجزه‌آسای یک مرد در تصادف زنجیره‌ای ۷ خودرو در آذربایجان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/658073" target="_blank">📅 18:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658072">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
تصویب قطعنامه علیه ایران در شورای حکام؛ تهران: پاسخ می‌دهیم  نمایندگی ایران در وین:
🔹
شورای حکام آژانس با رأیی ضعیف قطعنامه‌ای سیاسی درباره فعالیت‌های هسته‌ای ایران تصویب کرده است.
🔹
ایران از حقوق مسلم خود کوتاه نخواهد آمد و به این قطعنامه پاسخ خواهد داد.…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/658072" target="_blank">📅 18:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658071">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUJWAUuDyWrjXggUA2O3qz5UzIPFZqmyojNHiAxFFqx3Vd_7jMBdfDODM32bjxVefEyqBy-Ia_DZiM0tQEcOjPnrucROn01ALaQYCbwK-kQcHTZyCM6VZrjiYqFdrDu5x5llmG2m7XBMZ0bVp4ghyEYPeg1ByjIgJk8bNilYK4nl-0PjCEm0612cDkWz0DPeWQ4pWdJkgl7fG9quAfyYg-lQwzMluQdIGlyfAd-2a38Qfq8A5k1jdBkS2NW_uwtmbSt_cevfExCC2XBZqO4xMfyZ2GXEoeu6S4Y2SHhLMgc_OhnrhycW2EYKAHO-kmizbebT8SY3NETpIU0VvPTLyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی 2026 در راهه؛ تو آماده‌ای؟
هنوز سوت آغاز مسابقات زده نشده، اما هیجان در «همراه من» به اوج خودش رسیده!
فرصت رو از دست نده و از همین الان، جایگاهت رو در زمینِ بازی «همراه من» محکم کن.
⚽️
🎁
۵ گیگ اینترنت رایگان بدون قرعه کشی
🎮
هر روز یک PS5
💵
۱ میلیارد تومان اعتبار کیف پول در روزهای مسابقه
📱
قرعه‌کشی بزرگ S26 Ultra به همراه سیم‌کارت ۰۹۱۲ برای سه نفر برتر
✨
۳ کمک‌ هزینه سفر به عتبات عالیات در هر بازی تیم ملی
قبل از سوت آغاز، قهرمانِ پیش‌بینی باش!
👇
🔗
https://www.mci.ir/-4S0XAJB</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/658071" target="_blank">📅 18:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658070">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AINTvgvswRHasVBHL7hHQRglAXaVCw8J_A3yiObhaVt_XBosZJgyMQ6IlTAlhRAPhnDC6_W9uRWRZKi3-1FmM5ESLU3nxELsuS4LwizbhIkFjZPBy0H-jLNASUQyqlM2kehjbhZ3wX1iwgVm8l5z3U67GMXn-uC4qdAPpf3Tg-Vx4LzBkL8mkUJbt61hGqZBakBi30Swx97_lCnR0migQghqS9vSAmvb-vVysPNAt97O-C_lHpLvgQkTE4F1u1hYGT3zMzmOkPd6Gi5J57yzATYfXlBMfPAB5uI-pwUJ1FmjM91SLjc81Ua5eafc-_dPzkUpULEUFItb-9mhe0Cw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویب قطعنامه علیه ایران در شورای حکام؛ تهران: پاسخ می‌دهیم
نمایندگی ایران در وین:
🔹
شورای حکام آژانس با رأیی ضعیف قطعنامه‌ای سیاسی درباره فعالیت‌های هسته‌ای ایران تصویب کرده است.
🔹
ایران از حقوق مسلم خود کوتاه نخواهد آمد و به این قطعنامه پاسخ خواهد داد.
🔹
این قطعنامه که با ۲۱ رأی موافق، ۱۰ رأی ممتنع و ۳ رأی مخالف به تصویب رسید، از ایران می‌خواهد سرنوشت تأسیسات هسته‌ای بمباران‌شده و اورانیوم غنی‌شده‌ای را که در این تأسیسات نگهداری می‌شد، به آژانس اطلاع دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/658070" target="_blank">📅 18:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658069">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
ترامپ امشب سخنرانی اضطراری برگزار می‌کند
دونالد ترامپ:
🔹
امروز ساعت ۵:۳۰ عصر به وقت ساحل شرقی آمریکا یک سخنرانی اضطراری ارائه خواهم کرد./ خبرفوری
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658069" target="_blank">📅 17:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658068">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1RLa3dMZwhfg5Wkvr4IW7gj4aryyi_v_Un2j21BFUPIXaKEZKluGZhzr3YIWHD87D3J_LJmajE8-Dax4Sz8lwDselceO4Fq8Wigoq8_pK0YBvjkjAJtP584cWR0irHMGIAE6C-W-qJ3I6bvRDeoK85f1nW4pXbpk-8EbRZvi2ovG3gLx5Qfpzx_S0r0JIWaHQrPIBlqHRV1sw6l2NvNivOd5z3R1viiBxU-qfBhBa-rkBVmDnAtGQu84F6mjc3Gy9CLcaqVCdJS-z9GjRwutTfCQ0TJlQ9J7aUE_FLoG1DuLJ8zH0BX3sjzrC_8ObtLAyvGnpQm5WfZaK0m-Ipn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایتان لوینز، روزنامه‌نگار آمریکایی: ایران در تمام طول جنگ یک دانش آموز را هم نکشت
🔹
ایالات متحده ۱۵۰ دانش آموز ایرانی را در ۱۰ دقیقه کشت. ایران در تمام طول جنگ یک دانش آموز را هم نکشت. چرا ایران به‌عنوان «طرف شرور» تصویر می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658068" target="_blank">📅 17:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658067">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حمله تند کارشناس شبکه افق به صادق زیباکلام: زیباکلام لعنتی بیشترین نفع را از ساختار جمهوری اسلامی برده است ولی به رهبر شهید توهین می‌کند/ رهبر شهید ما هنوز دفن نشده است ولی زیباکلام به ایشان اهانت می‌کند و می‌گوید آن که مزاحم همه بود دیگر نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/658067" target="_blank">📅 17:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658066">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-text">🔸
روایت مخاطبان خبرفوری از بازار مسکن
🔹
ارسالی از البرز:
سلام وقتتون بخیر توروخدا صدای ما مستأجران روبه گوش مسئولین برسونید واقعا کم آوردیم هرساله چقدر اجاره بها افزایش پیدا می‌کنه مگه مامستاجرا آدم نیستیم که ی زندگی خیلی ساده برامون بشه آرزو.
🔹
ارسالی از مشهد:
با سلام از مشهد هستم شمارو به امام رضا به داد ما برسید اجازه خانه‌ها و رهن خیلی بالایی مگه چقدر حقوق میگیریم خرج خونه.پول برق گاز آب تخلیه چاه به خدا موندیم با دوتا بچه چکار کنیم تورو خدا یه فکری برای صاحبان خانه بکنین لاقل اجارهارو بیارند پایین که شرمنده بچه هامون نشیم
🔹
ارسالی از کرمان:
سلام تشکر می‌کنم بابت این کانال اطلاع رسانی فقط خواستم بگم به داد ما مستاجر ها برسید خواهش میکنم متاسفانه صاحب خونه ها خیلی بی انصاف شدن تواین شرایط که خودشون دارن می‌بینند.  آخه این انصاف نیست نمی‌تونیم هیچی بخوریم هر چی داریم باید بدیم صاحب خونه تو رو قرآن به داد ما برسید.
🔹
ارسالی از شیراز:
سلام خدا قوت.اصلا نظارتی روی قیمت اجاره خانه نیست مالک میگه میخاید این قیمت نمیخای خوش آمدید ، یه سامانه ای باید راه اندازی بشه که راه دور زدن املاک یا مالکان گرفته بشه ، مثلا اگر بیشتر از یه مبلغی بخان اجاره بگیرن ۱۰ درصد میاد روی مالیاتشون یه همچین چیزی،  لطفا شما که زبان رسانه رو بلدید این متن منو با یه اصلاحاتی که بلدید به عنوان یه پیشنهاد مطرح کنید . ممنون
🙏🏽
🔹
ارسالی از پرند:
سلام وقتتون بخیر  تو شهر پرند کسی نیست نظارتی کنه هر جور دلشون می خواد خونه رو میدن اجاره کسی هم نیست جلوشون بگیره ما تو چهار جنوب زندگی میکنیم سال پیش ۲۵۰  رهن نشستم الان املاکی به صاحب خونه گفته ۲۵۰ رهن اجاره بها ۱۶ ملیون مگه من کارگر ساختمانی چقدر در آمد دارم که ماهیانه هم کرایه خونه بدم هم خرج خونه خدا از املاکیای بی انصاف نگذره که رحم ندارن فقط به فکر جیب خودشونن  اگه قانونی باشه   درست وحسابی املاکی  حساب دستش بیاد ما مستا جرا اینقدر تو استرس واضط اب نیستیم میگن ۲۵ پر صد اضافه بشه به قرارداد ولی املاکی ۲۵۰ در صد میزاره روخومه ها ما شکایتمو به کی کنیم
🔹
ارسالی از اصفهان:
سلام وقت بخیرمن ازاصفهان هستم واقعاکسی نیست که به دادمامستاجرین برسه شوهرم بازنشسته است مستاجرهستیم مگه چقدره حقوق یه بازنشسته اضافه میکنن که اینقدر هم اجناس راگران میکنن وهم مبلغ رهن واجاره همراه خداکم آوردیم زیربار گرانی ورهن واجاره له شدیم آیاکسی صدای مارامی شنود مادرکشوری هستیم که همیشه ازهمه دنیاجلوتربودیم پس چی شده که حالااین همه بدبخت شدیم ممنون که پاسخگوباشید
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/658066" target="_blank">📅 17:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658065">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfvwxfXbTW3wIWwijilcaaLL34GWBY6k7OCRY-V1Sxx337OMdVNkxIj9xSg-LwwVSks46eq-ECh6g4Iy5c5EJ3VC0r1NjTr0-qt2L90sNJU1a9612ntQMzAV3NjpSYn0ouL53mz8YZiqb1j1IVSevIdpBa_i0Og08rh8qpU1CigpIJq9kkuH6MJclTPwOIfuCXodT7DqEdiJrw0p5T4u3SZzEinUjYXMZUMqcOivshTjvy6Bp_vR48t_NKfxwyEFVJ7KkGQcN68FhuEniCl7L2kRIVtp8qHixW9TndOeQya13j7OkEVf80BzBfE1SF_iCEyZ0rqz7uv1EC59s_PncQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ساحل فیتوپلانکتون، چابهار
🇮🇷
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/658065" target="_blank">📅 17:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658064">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
بقائی: آمریکا با پیام‌های متناقض به روند دیپلماتیک آسیب می‌زند
سخنگوی وزارت خارجه:
🔹
آمریکا با ارسال پیام‌های متناقض، تغییر مکرر مواضع و نقض‌های پی‌درپی آتش‌بس به روند دیپلماتیک آسیب می‌زند؛ ایران هرجا لازم باشد از دیپلماسی و در صورت اقتضا از توان نظامی برای دفاع از کشور استفاده می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/658064" target="_blank">📅 17:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658063">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
تأیید خسارت در پایگاه نظامی «رامات دیوید» در پی حملات اخیر ایران
ارتش رژیم صهیونیستی:
🔹
در جریان حملات اخیر جمهوری اسلامی ایران، پایگاه هوایی «رامات دیوید» مورد اصابت قرار گرفته و دچار خسارت شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/658063" target="_blank">📅 16:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658062">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ارتش عراق: پرونده انحصار سلاح وارد مرحله اجرایی شده است
🔹
ارتش عراق از آغاز مرحله اجرایی الزام‌آور طرح ساماندهی گروه‌های مسلح و انحصار سلاح در دست دولت خبر داد./ ایرنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/658062" target="_blank">📅 16:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658061">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
«خانه صانعی» جان گرفت
🔹
عمارت شهرآرا، به عنوان خانه طراحی شهری و مرمت بناهای تاریخی شهر تهران، به کانونی برای گفت‌وگوی میان طراحان صنعتی، معماران، مرمت‌گران و شهروندان تبدیل خواهد شد.
این مجموعه علاوه بر اجرای پروژه‌های مرمتی، طراح و مجری پروژه‌های بزرگ در حوزه مرمت، مبلمان شهری، نورپردازی‌های شهری، طراحی فضاهای شهری، پلازاها، فضاهای مکث و همچنین المان‌های شهری در سطح شهر تهران است.
استقرار این مجموعه در خانه تاریخی صانعی، عملاً این عمارت را به یک پایگاه زنده برای تولید تجربه، آموزش و تبادل دانش در حوزه مرمت و طراحی شهری تبدیل کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/658061" target="_blank">📅 16:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658060">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
افزایش اعتبار کارتکس گواهینامه از دو به چهار سال
پلیس:
🔹
از ابتدای تیرماه مدت اعتبار کارتکس آموزش و آزمون رانندگی از دو سال به چهار سال افزایش می‌یابد تا متقاضیان فرصت بیشتری برای تکمیل مراحل دریافت گواهینامه داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/658060" target="_blank">📅 16:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658059">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJfIC_NI8xtYdLuQn5Gf07blU-_Z7jP97lOkKhQUypDD1h4_n3vVNom1DyVzt5WYr-tvr6BjxIxX8vzAkbY_XWwGu74VtNAFhCjkejcQp0y5GukLhXpuc_N1oJfKKntaxmeKfURXzHAjMqPRHPSA0TCncwRhsHLlnzNgzT3BHeKOQr9vNQNrZDcBYOkDC0KQXBUDqmXwRboFiDeSZ1xX4IwGhcFkY9PYzUxaBhQWpUIJMmIYD9h6le3tL8MwZYYIkQh5q2ZyD-R1hXWAYChU7PBQ_lVaYvdpVaK0G39yRjErplSyJf3y5BrIr62pEdXrR4DWWs05If4QpF9ODZobMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلای جهانی در یک روز ۱۲۰ دلار ریزش کرد
🔹
قیمت جهانی هر اونس طلا در معاملات امروز با ریزش ۱۲۳ دلاری حدود ۳ درصد کاهش پیدا کرد و به ۴۱۳۴ دلار رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/658059" target="_blank">📅 16:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658058">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
بقائی: جام جهانی نباید بهانه‌ای برای آزار تیم‌ها شود
سخنگوی وزارت خارجه با اشاره به برخوردهای نامناسب با برخی بازیکنان و کادر فنی برخی کشورهای حاضر در تورنمنت در مبادی ورودی آمریکا:
🔹
فوتبال باید زمینه رقابت سالم و نزدیکی ملت‌ها باشد و جام جهانی نباید به فرصتی برای تحقیر و تبعیض تبدیل شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/658058" target="_blank">📅 16:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658057">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
سفر هیات قطری به تهران
🔹
هیاتی از قطر برای رایزنی درباره روابط دوجانبه و رویدادهای منطقه‌، وارد تهران شد.
🔹
قرار است در این سفر، افزون بر بررسی روابط دوجانبه و تحولات منطقه، درباره آخرین تحولات مرتبط با روند دیپلماتیک برای خاتمه جنگ تحمیلی آمریکا هم گفتگو و تبادل نظر شود./ صداوسیما
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/658057" target="_blank">📅 16:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658055">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQZWJspkyirDvQ6kdiobwP5XUVff-zcLwjKZwncnrHMW5fHeQTEIvUoeqGzgM8jFmwIKBX5j6NSmbAC_mAxoScgsaxdvTXPySxKO49GcOcTmiqUUCGXBajEXTfw53qcH0iAgxEpElv38RMiJzeCP6gdWIImaXgXN5XqdAW2WhE8DbBPfV_nJ9crL4f4rUc2y1eFo7V41Z1h_lghYFyRzoES34LIDoRJc_aaolkpHiYS9ni5JfNmC-ehLasCnupJk2SGyQWf8jwNsLL1XEK1ZALdXFeouVbZv83nJZ_q9-pF_8xYPaQqzB6lBEmGo_sPstDgDo-6OfEmA4FshpBJxVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سد منجیل پر از آب شد
🔹
به لطف بارش های گسترده اخیر سد منجیل نسبت به پارسال پر آب شده است.
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/658055" target="_blank">📅 16:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658053">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
قطعنامه ضدایرانی آمریکا امروز در شورای حکام به رأی گذاشته می‌شود
🔹
پیش‌نویس قطعنامه ضدایرانی آمریکا با حمایت انگلیس، فرانسه و آلمان امروز در شورای حکام آژانس بین‌المللی انرژی اتمی به رأی گذاشته می‌شود.
🔹
در این قطعنامه از ایران خواسته شده درباره تأسیسات هسته‌ای…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/658053" target="_blank">📅 16:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658052">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b7d6fc75.mp4?token=aRj_mNko-r_l-cKrVBY-UBhL8153u-s0EQnM5BTNM4kbGRZ4wa1W3ZU0e1GCi4zf5nf9Gjh00nrTjNkZH8QXFdQ27ilK7iBmpIOh0iTGk0SAW-OVqCsuj7Fr3TrG235Q-5KrskulKgkQS7hXnIryS0Psr7ivYVzgGt4U8G4FphguQgVsQMaQ8ou2lxvl_E7pZFZpO_GplcEr86--dgn7O4AGcbdXdfWghaBAb1OTQ_aEuvUxUmjlSEOOLrkameVu6MKLHeJTCoiXFLq3IDJ0uy6PSPNsKCIiiX4-tFyd1ZkE_oLoIDRbf1lr7EhMa827JwSXDXEeF0o5X4OWg64GmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b7d6fc75.mp4?token=aRj_mNko-r_l-cKrVBY-UBhL8153u-s0EQnM5BTNM4kbGRZ4wa1W3ZU0e1GCi4zf5nf9Gjh00nrTjNkZH8QXFdQ27ilK7iBmpIOh0iTGk0SAW-OVqCsuj7Fr3TrG235Q-5KrskulKgkQS7hXnIryS0Psr7ivYVzgGt4U8G4FphguQgVsQMaQ8ou2lxvl_E7pZFZpO_GplcEr86--dgn7O4AGcbdXdfWghaBAb1OTQ_aEuvUxUmjlSEOOLrkameVu6MKLHeJTCoiXFLq3IDJ0uy6PSPNsKCIiiX4-tFyd1ZkE_oLoIDRbf1lr7EhMa827JwSXDXEeF0o5X4OWg64GmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راهنمای کامل خرید طلای آب‌شده  #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/658052" target="_blank">📅 16:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658051">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-text">🕊️
هر روز ما به مدح علی می‌شود شروع
هوهوی صبح باد صبا مدح حیدر است
▫️
جلوه‌ای از حضور پرشور و دل‌نشین مردم در مهمانی بزرگ عید غدیر در برنامه «پناه غدیر» مشهد مقدس
💚
▫️
این اجتماع باشکوه، به همت هیئت قرار و مجتمع فرهنگی امیرالمؤمنین برگزار شد
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/658051" target="_blank">📅 16:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658050">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Age3bKP-5qQkuCpMn9hvh2bk1KZ88aACYv86UvyCUZit4OUGF56VHtgHOYdQ0BeyOoRwrw6HfcpoOoMIS5i8c2YK_Y9iJgGD8F4adbPcFXamlO1_fJmLjc9V1RI-nnJVAEc2VVzGc_oyiM2PiFnv1XMjSj_TqVAv4BqoY42VVplALNdT_A8FBJj7wrptflM7OJn0zblP4DOPzE1fNB2bIJZjKwEZqefKFp1n6oJwSZjzjO13NtPaBLZuO_lI3FmUmkBJMB2eR88EbFvN1ESQ4MybEoY2DTA1wnyB-zomKNUPxSc6bdE20fRj6i4LTzPfC7FAf7wOnh28d1_A29x98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط اعتماد اروپایی‌ها به آمریکا؛ فقط ۱۱ درصد، واشنگتن را متحد واقعی اروپا می‌دانند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/658050" target="_blank">📅 16:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658049">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
جزئیات جدید از حملۀ پهپادهای ارتش به پایگاه آمریکا در بحرین
یک منبع آگاه نظامی:
🔹
بامداد امروز پایگاه هوایی شیخ عیسی و یک سایت راداری آمریکا در بحرین با پهپادهای جدید ارتش هدف قرار گرفتند.
🔹
در حملات اخیر به پایگاه‌های آمریکا در بحرین، کویت و اردن، حدود ۷۰٪ اهداف با موفقیت مورد اصابت قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/658049" target="_blank">📅 16:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658048">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
واکنش نتانیاهو به سخنان اردوغان: در جایگاهی نیست که بخواهد به اسرائیل درس اخلاق بدهد
🔹
نتانیاهو، رئیس‌جمهور ترکیه را «دیکتاتوری یهودستیز» خواند و مدعی شد که او علیه کردها مرتکب نسل‌کشی شده و مخالفان سیاسی خود را زندانی می‌کند، بنابراین در جایگاهی نیست که بخواهد به اسرائیل درس اخلاق بدهد.
🔹
نخست‌وزیر اسرائیل در ادامه مدعی شد که ارتش اسرائیل «اخلاقی‌ترین ارتش جهان» است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/658048" target="_blank">📅 16:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658047">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
یک نشانه نگران‌کننده برای اقتصاد؛ شامخ به کف ۸ ساله رسید
🔹
شاخص مدیران خرید (شامخ) در فروردین‌ماه با ثبت عدد ۳۸.۵ برای کل اقتصاد و ۳۷.۴ برای صنعت، به یکی از پایین‌ترین سطوح ۸ سال اخیر رسید؛ رقمی که نشان‌دهنده رکود شدید اقتصادی است.
🔹
افت تولید، فروش و سفارشات جدید و همچنین افزایش تعدیل نیرو در صنعت از مهم‌ترین نشانه‌های این وضعیت است.
🔹
کارشناسان اختلال اینترنت، کمبود مواد اولیه، جهش نرخ ارز، محدودیت‌های ارزی و نااطمینانی ناشی از جنگ را عوامل اصلی این افت می‌دانند./خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/658047" target="_blank">📅 16:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658045">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/973ea2928b.mp4?token=Bi1oWDxwnSa9u3aI0bX7hLHtyJsS1c-sZQEy1yOL5z8a5jdYusHYf6i1cjqHUuU3FBK4-m39ryFEO94vXoqjYF3zPO1OhWctb0mBr34Ndr9gZvTdr2oK8lRzKwzPrBfjrKvrobUjaDU9s4tmYFb4Y-DQGDBn5MEDwvcG_8uscIO8cEQE9fiN-44sjWGXi-p-vhP34tVxDgnqtzj8BpgdnLcfP7CTtvoftNxxkgsp5U6nbGLhvt4XO6iV9KGKKLnNjxnIKexeujrnxpcHHZfrrWTGpypVVyOIxA9T4arwnncVoM4di5vblGTXVQUsiVY9LSGOxiQVl-QRZg2_4E5QmBO_a8wH0rmfISUJfAcpstvuTNXuvLwoyewJQSewgk196ycFsdqG_OqAVqhFVYcqbW1afUblh7bsigb9-1bQEroT4Mk6I5xtGuQIlAPqZcJZ-xnLV00xeX7jQ4EG2qsQpo631Cl_s9dhomHE9ZHzuKZESG_odhkAHcXdNI4_gJuFdapkqlcbFZMlHCyPR9lywJyHYuZnInb-6JCadL5jAlGwH6ZSTr7cXOGyHyxQSSVTtrebMlrXZR3WH7WJBi81tclu7iQzPA1ml6X1_SnHKTgV3w1ZGGlsnBxMYgQKbIJ03jSFIZWsUMigVIcUy0sqs3h4eN-5XdQizR1iXvzdF0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/973ea2928b.mp4?token=Bi1oWDxwnSa9u3aI0bX7hLHtyJsS1c-sZQEy1yOL5z8a5jdYusHYf6i1cjqHUuU3FBK4-m39ryFEO94vXoqjYF3zPO1OhWctb0mBr34Ndr9gZvTdr2oK8lRzKwzPrBfjrKvrobUjaDU9s4tmYFb4Y-DQGDBn5MEDwvcG_8uscIO8cEQE9fiN-44sjWGXi-p-vhP34tVxDgnqtzj8BpgdnLcfP7CTtvoftNxxkgsp5U6nbGLhvt4XO6iV9KGKKLnNjxnIKexeujrnxpcHHZfrrWTGpypVVyOIxA9T4arwnncVoM4di5vblGTXVQUsiVY9LSGOxiQVl-QRZg2_4E5QmBO_a8wH0rmfISUJfAcpstvuTNXuvLwoyewJQSewgk196ycFsdqG_OqAVqhFVYcqbW1afUblh7bsigb9-1bQEroT4Mk6I5xtGuQIlAPqZcJZ-xnLV00xeX7jQ4EG2qsQpo631Cl_s9dhomHE9ZHzuKZESG_odhkAHcXdNI4_gJuFdapkqlcbFZMlHCyPR9lywJyHYuZnInb-6JCadL5jAlGwH6ZSTr7cXOGyHyxQSSVTtrebMlrXZR3WH7WJBi81tclu7iQzPA1ml6X1_SnHKTgV3w1ZGGlsnBxMYgQKbIJ03jSFIZWsUMigVIcUy0sqs3h4eN-5XdQizR1iXvzdF0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جاده بهشتی الموت به تنکابن
#ایران_زیبا
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/658045" target="_blank">📅 15:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658044">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
اعلام جرم جدید دادستانی تهران علیه زیباکلام؛ قرار نظارت قضایی زیباکلام تشدید شد
🔹
با وجود اعلام دادستانی تهران مبنی بر قرار نظارت قضایی زیباکلام مبنی بر ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی به مدت سه‌ ماه، این فرد با نقض این قرار،…</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/658044" target="_blank">📅 15:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658043">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18337c03b1.mp4?token=grhgCOn07S6nC3UVSn4NsBKjFdi-is9iEvciVt8ge0XW7VAoWaKczOZK9e0iFP-YpsmNjl-xFthOksOaWfp3F1ZVAkALzKlywrr-Lh6ySpHuzvznwGsJTf-IT0bmFDdVJ1fQg37_m6-rd9vJbtvZ8VeFoU408NuCJVTutcBKA0ONsNjS18promM5Ng7HlG_TFMTeCD8yr3mBPy6iFAqw3_Z5Tl-GXppWR4YWnfEFWunqe4GsP9blGR6D5_brfOfRUcYGjxE1ujIE3vrbZ5tiy4RNGzmNd9xnpL3siEQCjBCFDntAnT7V_6K3dx0pFW9GnGWk0bzBiUmqtWqhSlw-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18337c03b1.mp4?token=grhgCOn07S6nC3UVSn4NsBKjFdi-is9iEvciVt8ge0XW7VAoWaKczOZK9e0iFP-YpsmNjl-xFthOksOaWfp3F1ZVAkALzKlywrr-Lh6ySpHuzvznwGsJTf-IT0bmFDdVJ1fQg37_m6-rd9vJbtvZ8VeFoU408NuCJVTutcBKA0ONsNjS18promM5Ng7HlG_TFMTeCD8yr3mBPy6iFAqw3_Z5Tl-GXppWR4YWnfEFWunqe4GsP9blGR6D5_brfOfRUcYGjxE1ujIE3vrbZ5tiy4RNGzmNd9xnpL3siEQCjBCFDntAnT7V_6K3dx0pFW9GnGWk0bzBiUmqtWqhSlw-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط بالگرد ارتش پاکستان در کشمیر
🔹
ارتش پاکستان امروز اعلام کرد که درپی سقوط یک بالگرد نظامی در منطقه کشمیر (تحت کنترل دولت اسلام‌آباد) همه سرنشینان آن کشته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/658043" target="_blank">📅 15:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658042">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9247a5c8de.mp4?token=ZsKry5ShhHgL4T3N9k8lMR2k7GtniYoFpec9pHZCW3TvEcjJXU8Fg6_0VKShKvFb7HJslu4VCiYUFKZ2MZkYMFX9W6PMDRzp5p3MuMeGiVxFvTkpjct7Lg9zoVJ0Ulx5Q3jpWRbQA4ufEVfpnElMsISBFqEuoz1rfEbi3GB_3rQEGHbAh0MA4FJbYSqrfMVb9G6fk_U4Cyea2wC9IcP6ll-5a8Jg44nh-797ztPLzzUm7Vdcn1MF-ycVuxbBA6e-GJ8cfK1yx3_ScBg9unhQQLuRyc9Bw0pBLQ3gNz-VORu7_VoEE1XhGK0IKh2tC9IghK0oHUE5NmAr29ck0p5AUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9247a5c8de.mp4?token=ZsKry5ShhHgL4T3N9k8lMR2k7GtniYoFpec9pHZCW3TvEcjJXU8Fg6_0VKShKvFb7HJslu4VCiYUFKZ2MZkYMFX9W6PMDRzp5p3MuMeGiVxFvTkpjct7Lg9zoVJ0Ulx5Q3jpWRbQA4ufEVfpnElMsISBFqEuoz1rfEbi3GB_3rQEGHbAh0MA4FJbYSqrfMVb9G6fk_U4Cyea2wC9IcP6ll-5a8Jg44nh-797ztPLzzUm7Vdcn1MF-ycVuxbBA6e-GJ8cfK1yx3_ScBg9unhQQLuRyc9Bw0pBLQ3gNz-VORu7_VoEE1XhGK0IKh2tC9IghK0oHUE5NmAr29ck0p5AUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلاغی که آرایشگر گراز شد
🔹
در پریمورسکی روسیه، یک کلاغ و گراز با هم همکاری می کنند. ویدیو نشان می‌دهد که کلاغ با آرامش روی کمر گراز نشسته و دارد با دقت تمام پشم او را می‌کند. این کار گراز را از شر پشم های اضافی در این تابستان گرم رها می کند و برای کلاغ هم مصالح ساختن آشیانه راحت فراهم می شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/658042" target="_blank">📅 15:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658041">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
پزشکیان: مدیری که تصور کند برای حل مسائل تنها یک راه‌حل وجود دارد، در واقع شکست را پذیرفته است
🔹
بنده شکست را نخواهم پذیرفت و معتقدیم برای عبور از چالش‌های کشور راه‌های متعدد و ظرفیت‌های فراوانی وجود دارد و دانشگاهیان و نخبگان می‌توانند در شناسایی و به‌کارگیری این راهکارها نقش مؤثری ایفا کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/658041" target="_blank">📅 15:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658040">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دادستان کل کشور: توقیف اموال اشخاص بیش از میزان محکوم‌به یا خواسته خلاف قانون است.
🔹
عارف، معاون اول رئیس جمهور: دولت به دنبال افزایش مبلغ کالابرگ است
.
🔹
اتحادیه اروپا: از دیپلماسی برای حل پایدار موضوع هسته‌ای ایران حمایت می‌کنیم.
🔹
محیط زیست بوشهر: ۲۵ آهوی جزیره خارک قربانی بمباران آمریکا و اسراییل شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/658040" target="_blank">📅 15:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658039">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
طناب زدن با آهنگ تمام قومیت‌های ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/658039" target="_blank">📅 15:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658038">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
کشف کلاهبرداری ۳۸۰۰ میلیارد ریالی در کاشان و قاچاق‌های کلان در اصفهان
🔹
فرمانده انتظامی استان اصفهان از کشف کلاهبرداری سه هزار و ۸۰۰ میلیارد ریالی در کاشان، دستگاه گنج‌یاب پنج میلیارد ریالی در فریدن، ۱۲ هزار لیتر سوخت قاچاق در نایین و چهار تن چوب قاچاق در شاهین‌شهر خبر داد.
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/658038" target="_blank">📅 15:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658037">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBcviq9dsAmohcDGLM-exE9mtg_eiN01WIW2_jJSLFnSuzA46AT2EPW0VkdqOiu8ToL8Kq200PgTn4dduE1Lk1C14tw2N4X5xQPDilxMTSUCm6O8FfNQwlc1TjGlvzE0l-K0Ukg5DE-bLDN3UYnZ58az7KZ9yHyHXTGfACPnxmn9xHGm8XYF8fAeilwCQqKV4LMgYcXjxnxFH7QOnehF3kVBgxG6SC9aw9HQ6tKTAuTiCYWhqH9xJa8UM2Qj-KepXuKjPQ8cNJe9jLvYEvPBQfYKrdFAtShPjWY-KKC_X4YIGjRyX2PIKle8C1qK2pvCQUSOKi1JbRODezB6xsP2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سفیر ایران به حمله دیشب آمریکابه سیریک: مغولها هم در حمله به شهرها، به منابع آبی آسیب نمی‌زدند
کاظم جلالی، سفیر جمهوری اسلامی ایران:
🔹
‏جامعه جهانی مقابل حملات عامدانه آمریکا و رژیم صهیونیستی علیه زیرساخت‌های شهری و مدنی ایران سکوت نخواهد کرد.‌
🔹
حمله به مخازن آب و تأسیسات خدماتی علاوه بر آنکه نقض فاحش قوانین بشردوستانه بین‌المللی است، جنایت علیه غیرنظامیان است که با هدف مختل کردن زندگی آنها در آستانه فصل گرما انجام می‌شود.
🔹
وحشیگری کنونی، در تاریخ بی سابقه است، مغولها هم در حمله به شهرها، به منابع آبی آسیب نمی‌زدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/658037" target="_blank">📅 15:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658036">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu7Oxc6VSgrNZzq469abF0nnxWKUBIwEm2VJgg6MB96PrPxfdeHDVaHmyqTdgsgK1TMGGjh5b6HOT4CWj2LT4of0kp1RrNAIK4sfWddZ0vJvf9e5f_quK5k9l56reICXBF1Na15h5aAjMZskPk0rmlWxfW8xBrJQ-7AzwL1ZDLzjeeQe6uIl0WOo0JbVBrsQR9_c9YJvQ8Iv2S_i1DJ78A2QugRYdwobLiPl6dXP0CZfSZIFtsVrCihQU9mFVOJaUSmeru8C3pzIL3LDaYzihkdCyHxVpTghUyS8wYjCtoNOCh5-pZFLqUdqogaa9tY_lCw9db1Pnqzsp2Q53AcPxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لیکود نامزدی نتانیاهو برای انتخابات آینده را اعلام کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658036" target="_blank">📅 15:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658035">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5301cd06f2.mp4?token=rJ8JsfLkHI4pm2fe3cdc-hImgRJ5lljkfqcLcyMwg2gWGvujJV7JI9ucnVRwUMkwZU_Eg2pCAXnox2ErNYV1ELxCl4brpY2x1u3UoQJwbARyxmXYmuXEuEG9a7oHw2RUb-sH53E_oFdHEOF13Z2xC6ZanmYhD8DST5DX0tzMjm1Ln5nXhJI_u_pIxE_zOWOEK3X61TgguDMffcCA9ZbLyf5My6mK95gdXWGgDgNY0s4BaM-svjEg2M8nXM-uDWvNnQBScxNeqayh6Zq0rE30VVdecC3H3ABddIkPC5vlrR_bpZaibWZDsBd2IPhvNh8TiKGArgYbB-RvayWz0VYKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5301cd06f2.mp4?token=rJ8JsfLkHI4pm2fe3cdc-hImgRJ5lljkfqcLcyMwg2gWGvujJV7JI9ucnVRwUMkwZU_Eg2pCAXnox2ErNYV1ELxCl4brpY2x1u3UoQJwbARyxmXYmuXEuEG9a7oHw2RUb-sH53E_oFdHEOF13Z2xC6ZanmYhD8DST5DX0tzMjm1Ln5nXhJI_u_pIxE_zOWOEK3X61TgguDMffcCA9ZbLyf5My6mK95gdXWGgDgNY0s4BaM-svjEg2M8nXM-uDWvNnQBScxNeqayh6Zq0rE30VVdecC3H3ABddIkPC5vlrR_bpZaibWZDsBd2IPhvNh8TiKGArgYbB-RvayWz0VYKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی به صیدا و شهادت دو شهروند لبنانی
🔹
منابع لبنانی گزارش دادند که در حمله پهپادی رژیم صهیونیستی به خودرویی در شهر صیدا در جنوب لبنان دو شهروند لبنانی به شهادت رسیدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/658035" target="_blank">📅 15:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658034">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
کشف ۱۶۳ هزار لیتر گازوئیل قاچاق در سواحل میناب
فرماندۀ پایگاه دریابانی میناب:
🔹
۳ مشک ماری حاوی ۱۶۳ هزار لیتر گازوئیل قاچاق در سواحل این شهرستان کشف شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozga</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/658034" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658033">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
تکذیب ادعای وزیر ارتباطات درباره مصوبه ۳۲ بندی
🔹
اطلاعیه روابط عمومی مرکز ملی فضای مجازی: روز گذشته وزیر ارتباطات در نشست خبری اعلام کرده بود که مسئولیت اجرای مصوبه تسهیل دسترسی به سکوهای خارجی و ارتقای حکمرانی قانون‌مند که به عنوان مصوبه ۳۲ بندی شناخته می‌شود بر عهده مرکز ملی فضای مجازی است که این ادعا از اساس غلط است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/658033" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658032">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-U4-y3UghaERR1Z3TrS3ZkbarozzSlYej_uQngMJsOqTvYsSF1daeCxkLKrllaabBj7Z_dIfyEtwPu_yKsExK2XzuR0QMpfaew8WIohKQ58JZGikLx9CnpiFxrpPY5XsBkzfsuC1imDAUlC8I7wviZ8p_AyXnVvd-013b7dOXmyB4R-yAZE0zgqIuWN4vPePMz3XqedqTAshVTKdMYVMmSByJVMMzTTnDwtyTtWLgvo6EwIG0Kalb4I5h3vYxXzuyY508GX7fQu81X9OalNrzZZdORoVUd2dFszWDGfX3m1L9HjAOdJsE5E4_FZIQAFJtsPoSvVqj-qkmYuoKEBOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خواب نما شدن ترامپ: ایران حقوق نظامیانش را نمی‌پردازد
رئیس جمهور دروغگو آمریکا:
🔹
رسانه‌های خبری جعلی از گزارش دادن دربارهٔ اثربخشی محاصرهٔ دریایی ایالات متحده خودداری می‌کنند، موفق‌ترین محاصره در تاریخ جنگ‌های دریایی. هیچ چیزی عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است!
🔹
ایران هیچ کسب‌وکاری ندارد، حقوق نظامیانش را نمی‌پردازد و هیچ یک از صورتحساب‌هایش را، و به سرعت در حال تبدیل شدن به یک کشور شکست‌خورده است! مقدار زیادی نفت خارج می‌شود. سپاس خداوند! رئیس‌جمهور دونالد ج. ترامپ
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658032" target="_blank">📅 15:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658031">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
قطعنامه ضدایرانی آمریکا امروز در شورای حکام به رأی گذاشته می‌شود
🔹
پیش‌نویس قطعنامه ضدایرانی آمریکا با حمایت انگلیس، فرانسه و آلمان امروز در شورای حکام آژانس بین‌المللی انرژی اتمی به رأی گذاشته می‌شود.
🔹
در این قطعنامه از ایران خواسته شده درباره تأسیسات هسته‌ای بمباران‌شده و اورانیوم غنی‌شده آن‌ها توضیح دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658031" target="_blank">📅 15:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658030">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91330768c7.mp4?token=DnWJ8Vu1JDmkycfTnMSGypqpV_2peXcRAaA3-OFuWyymb5yVrsj1NmMIecf0vwItm0tAZ59WkYlDy3htHZuJ6DGwsepxghd7m7Z5rlM9wu49VZIfjLJ1k-JzNpiNBddw26ZSx1N93-LzzgQ7ATm_fK23k74vj0kCSaEgN7bQPlpzK6eGoLH8JnmLPtqhe2YiB7_m6nJBSqpIzWXj_L5G0MQuE95UT04qt6I0rnq4zQ_xCCYprW7mlhkmZMCQkpsJTh1o0eq1S-bsgrNK5nCxWs68I1-ec18-8V3DSytYelqDxni27bvHkQXbo8GqMuAjRl5I-3k3l4lLQjsqzbSbSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91330768c7.mp4?token=DnWJ8Vu1JDmkycfTnMSGypqpV_2peXcRAaA3-OFuWyymb5yVrsj1NmMIecf0vwItm0tAZ59WkYlDy3htHZuJ6DGwsepxghd7m7Z5rlM9wu49VZIfjLJ1k-JzNpiNBddw26ZSx1N93-LzzgQ7ATm_fK23k74vj0kCSaEgN7bQPlpzK6eGoLH8JnmLPtqhe2YiB7_m6nJBSqpIzWXj_L5G0MQuE95UT04qt6I0rnq4zQ_xCCYprW7mlhkmZMCQkpsJTh1o0eq1S-bsgrNK5nCxWs68I1-ec18-8V3DSytYelqDxni27bvHkQXbo8GqMuAjRl5I-3k3l4lLQjsqzbSbSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌بازی ضدچینی تایوان با موشک‌های آمریکایی
🔹
تایوان برای اولین‌بار با سامانه‌های موشکی توپخانه‌ای هایمارس ساخت آمریکا شلیک واقعی انجام داد و حملات دقیق فرامنطقه‌ای را شبیه‌سازی کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/658030" target="_blank">📅 15:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658029">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db1b80511c.mp4?token=d9Su_Es5PerFfTm08krOkxceyqpF4u9Z29swmfrCBK3Slg2DAtNFq3Aiaa-Y41f3ppOQLkbjk1cwooS3KeKeo-boKSEN5L7o2Elz45JfzllMX4M-piJsxlld_5gP7hCLcbbecP51LLMQP7syC3BDmTwqT4NwZ5NgtO1N_HPyrutUVfOxTZWeflMXpIMGGHYF-eK6_iBmQdkHLqQEUj-Z1juZwlCo9poOEOxvh9DF3nO-P_9E0o5CP0tewPeS65ajUfMkkUEltDQUfFO9B5A6AwINo6-fW_f1sYGjP8fSU2-VxnYwQrqcSiL4l6NDOKX98H3SoGdGnca5opDI6zulkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db1b80511c.mp4?token=d9Su_Es5PerFfTm08krOkxceyqpF4u9Z29swmfrCBK3Slg2DAtNFq3Aiaa-Y41f3ppOQLkbjk1cwooS3KeKeo-boKSEN5L7o2Elz45JfzllMX4M-piJsxlld_5gP7hCLcbbecP51LLMQP7syC3BDmTwqT4NwZ5NgtO1N_HPyrutUVfOxTZWeflMXpIMGGHYF-eK6_iBmQdkHLqQEUj-Z1juZwlCo9poOEOxvh9DF3nO-P_9E0o5CP0tewPeS65ajUfMkkUEltDQUfFO9B5A6AwINo6-fW_f1sYGjP8fSU2-VxnYwQrqcSiL4l6NDOKX98H3SoGdGnca5opDI6zulkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: بررسی‌های جمهوری اسلامی مبنی بر همکاری اردن با متجاوزین به کشور ما، تنبیه اردن را در پی داشت/ این رویه شامل کشورهای هم‌دست خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658029" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658028">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
ترامپ باز هم پل‌ها و نیروگاه‌های ایران را تهدید کرد
🔹
دونالد ترامپ در مصاحبه با فاکس‌نیوز گفت که در آستانه صدور دستوری برای انجام حملات جدید به نیروگاه‌ها و پل‌ها در ایران است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/658028" target="_blank">📅 15:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658027">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933efea1c1.mp4?token=eIl0xCx-k9_qNM0-wM-QaSkhDqjLrjvPGSuEK_kz6IMKG4DQ6yJ2pUBfwob650z2SqeuUsei8OY5Z4QFsxmH_OXRmD6x5UeQG9DQUchtc3nnXJfmT3Z-GqocB7K8A3lUR-Xeq9VNjkiUFOkPxqfGcOAK8HNSQHRB9t0y82IkHIv-AgWvuf58w2LEUre884IgKvSi6f6oCBizfZzAK7cR7MuZ4WE8IXpAHA9-k9V7kLxbHwG5XJV-f7MMt3Nx5LWzwwTxs-F0BMsrGl9u-TwadC4AmI976nzECX93H2-AFD7IFDTs6XW2CRYn6IQJeSeCorTzmMrILx3z5vWJrI9uZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933efea1c1.mp4?token=eIl0xCx-k9_qNM0-wM-QaSkhDqjLrjvPGSuEK_kz6IMKG4DQ6yJ2pUBfwob650z2SqeuUsei8OY5Z4QFsxmH_OXRmD6x5UeQG9DQUchtc3nnXJfmT3Z-GqocB7K8A3lUR-Xeq9VNjkiUFOkPxqfGcOAK8HNSQHRB9t0y82IkHIv-AgWvuf58w2LEUre884IgKvSi6f6oCBizfZzAK7cR7MuZ4WE8IXpAHA9-k9V7kLxbHwG5XJV-f7MMt3Nx5LWzwwTxs-F0BMsrGl9u-TwadC4AmI976nzECX93H2-AFD7IFDTs6XW2CRYn6IQJeSeCorTzmMrILx3z5vWJrI9uZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله حزب‌الله به تجمع خودروها و نظامیان رژیم صهیونیستی با موشک منحصر به فرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/658027" target="_blank">📅 15:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658026">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بحران در بیمه تکمیلی؛ ۷۰ درصد پرداختی‌ها عقب افتاد!
فضل‌الله رنجبر، سخنگوی کمیسیون اجتماعی مجلس در
#گفتگو
با خبرفوری:
🔹
بیمه‌هایی که توانسته‌اند تقریبا به روز شوند درصدشان خیلی کمتر است؛ حدود ۳۰ تا ۴۰ درصد، اما اکثریت نتوانسته‌اند به روز باشند. یکی از دلایل این موضوع همین شرایط تورمی و گرانی‌هایی است
🔹
اخیرا هم که مدیر بیمه مرکزی منصوب شده، خواهان این شده‌ایم که گزارش تکمیلی را بیمه مرکزی به ما بدهد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658026" target="_blank">📅 15:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658025">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
رویترز: هیئتی قطری امروز راهی تهران شده است
🔹
خبرگزاری رویترز به‌نقل از منابع آگاه مدعی شده که «هیئت مذاکره‌کنندهٔ قطری صبح امروز پس‌از رایزنی با آمریکا، راهی تهران شده تا در زمینهٔ نهایی‌سازی یک توافق گفتگو کند».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658025" target="_blank">📅 15:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658024">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6oXXDz-Xs_kHC2pdFLGcAck-MzNdIBSh7NvZQvutRc11wK1kM4_VVbDeDzJOT3afB0MHfWM1kxaANDklUs7e5wKm7IQpnsVEtUfjZW-b108S44Qm-EXti1ubXXkN7hgJafCn3fdndcsuDQB-gYNyYfKzy5JDeC9n8ONbA9CoP61Uq-dnV0Oae0mszmzVtJp41KpXqWm2fy2wyHvo3SEY_Y1_zQUmF8rPDIidKQz7z8wD--xzJuXJAEzlezTxB_ORMyxOG82GWwiIo0KUZeVbcrgrY1QJgfujeSLmzvX7iu_xppuf4NVFWpRIV0MpckAx6jxwlXHegTGmd1GuoA_Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط بالگرد ارتش پاکستان در کشمیر
🔹
ارتش پاکستان امروز اعلام کرد که درپی سقوط یک بالگرد نظامی در منطقه کشمیر (تحت کنترل دولت اسلام‌آباد) همه سرنشینان آن کشته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/658024" target="_blank">📅 14:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658023">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36692261c5.mp4?token=gwonyYIqRlWXxzxosP0Nmy_4dYfu7p3WNIFrIPrm7n5EPLOzvZuloIuF5RsW_ylRkVgULTupLGhG1K5kvrpeYNUl6AMVziwsDhOgtxgkwozLJF8ukVuItFSRQjlu8itC1pR8HllQS7eU-xHV4ga0v8iHfxJqh7LmMfRXWC_wEZuZneQB296rD_eGyQva0sinYaOWfFTg6BQ6XNGT6sG6VBuifz5aD5cBHVF0moylw16YXTK-4mU9I5jRoYtrfWOh1uUF2wJAj7i50vcY6dP16f1xe3545vRSAP1k50kwN9rmw9NoN9VU0AzmkjS7a-hBqAXNekMvp3_kiuvvEa6Z6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36692261c5.mp4?token=gwonyYIqRlWXxzxosP0Nmy_4dYfu7p3WNIFrIPrm7n5EPLOzvZuloIuF5RsW_ylRkVgULTupLGhG1K5kvrpeYNUl6AMVziwsDhOgtxgkwozLJF8ukVuItFSRQjlu8itC1pR8HllQS7eU-xHV4ga0v8iHfxJqh7LmMfRXWC_wEZuZneQB296rD_eGyQva0sinYaOWfFTg6BQ6XNGT6sG6VBuifz5aD5cBHVF0moylw16YXTK-4mU9I5jRoYtrfWOh1uUF2wJAj7i50vcY6dP16f1xe3545vRSAP1k50kwN9rmw9NoN9VU0AzmkjS7a-hBqAXNekMvp3_kiuvvEa6Z6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پالایشگاه بزرگ روسیه هدف قرار گرفت
🔹
پالایشگاه نفت در استان سامارا پس از حملۀ پهپادی اوکراین دچار آتش‌سوزی شد. این پالایشگاه یکی از بزرگترین تأسیسات صنعت نفت در منطقه و بخشی از شرکت دولتی روس‌نفت است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/658023" target="_blank">📅 14:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658022">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
معاون امور زنان ریاست جمهوری: احتمالا صدور گواهینامه موتورسواری زنان از یکماه آینده آغاز می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/658022" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658021">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mEyVpnYsvWVCazsjZJ_jsLnggyPUj5zmDkTQDXQ5ZfJk39MJaOa80CoGMoKTCyTBp6V4JvD3QGVYROvLp5EnxNsR3dsVr3Q4FW3l4Wrl61yybs_vRIrjQiurvNOWTtlMF9l8IPm4X9BUnEA6Q_Q8y1kJGFKuW--HnmMUkku76GWo5sU3kX-1rK5p9ntcPsA73I8ynLV-8LxiuO8KBmuju5zeVrCHo8imuZaEauKv2eHIDVKtlsVSAjM_KYxWH52k3IjMVx4I6Hv5neC8-S3eM4AcTTv6Gd9hem7QJpkAh5P2AjDcH9EYLTF5AwrA8QK8k50XAPFh78WKELzrqs9dtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از کشف تجهیزات پشتیبان هدایت جنگنده‌های صهیونیستی در لواسان
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/658021" target="_blank">📅 14:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658020">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZK7g1uLf27oO9Ll4G9Zlbl3BxfRxJ82V1JoaMs1JpZWGUWXt3VvSMUYBCytsYBI3DV2K2WTakunjz8IEuWq0LuZEa4Ov8LBTPsuTVIT_tWjgPUNetOSOThMK5u4GEteLXnC0_Ec90_lr2V0xhOa4LbMTckm-MtWXFlQCk6A8pMuK0-QsefQbAmxYD3awGfuVFdkSsXu5NTCj9D9Qn5pUeoqhkvqLzIL9WOY0Jug63t22Cz4nuyDsOZ-iGtv1_Md0An8V1o7NVx2B5bku7vijPm8VDVpDBWNufZZKRQlKMoxAelWWdYqLMzSFK2nci03VCmFYnVTnmytiy34Sa0Agg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای جدید ترامپ درباره مذاکرات و توافق با ایران
رئیس‌جمهور آمریکا:
🔹
ارتش ایران کاملاً آشفته و بهم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و هوایی آنها، دیگر حتی وجود ندارد - آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و هیچ عملی انجام نمی‌دهد. آنها برای مذاکره در مورد توافقی که برایشان عالی بود، خیلی وقت صرف کردند، حالا باید هزینه آن را بپردازند!
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/658020" target="_blank">📅 14:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-658019">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce354e84e.mp4?token=g_Hy6icmtfJgHzr1U07nVOzukNgibdpr6SKoaIlxpzij1otvnpfYw2kRlugnH9rnNdTtf6pH52j4JbLJksKE92CcACd0zCoIhKtTVJU91jGRrsvCt8MtbERZHaZrvAugddA7mG-IEQyiznVTtfv2ODHD070dDrMKNVn2LgTQ4UveIl0AercYGjqy_xM4T-4JwjjoS7rryq2Ol45JuMMipymyiy3h70zIxKUPbWNhy_4b3FivAAnXvwRVC0xcUE_Nm-Y6QIizuNy8pRsdAPnaEjTBuEh1YqWiQyyGdT0MCv3kZIeR2vwGnP1rAue1T2q3Yka-u7TPjskvnCkIB9Sy5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce354e84e.mp4?token=g_Hy6icmtfJgHzr1U07nVOzukNgibdpr6SKoaIlxpzij1otvnpfYw2kRlugnH9rnNdTtf6pH52j4JbLJksKE92CcACd0zCoIhKtTVJU91jGRrsvCt8MtbERZHaZrvAugddA7mG-IEQyiznVTtfv2ODHD070dDrMKNVn2LgTQ4UveIl0AercYGjqy_xM4T-4JwjjoS7rryq2Ol45JuMMipymyiy3h70zIxKUPbWNhy_4b3FivAAnXvwRVC0xcUE_Nm-Y6QIizuNy8pRsdAPnaEjTBuEh1YqWiQyyGdT0MCv3kZIeR2vwGnP1rAue1T2q3Yka-u7TPjskvnCkIB9Sy5oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: اسرائیل اگر خط‌ قرمز ایران را در لبنان رعایت نکند مورد هدف قرار می‌گیرد/ حضور مردم در خیابان دلگرمی رزمندگان در میدان جنگ است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/658019" target="_blank">📅 14:40 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
