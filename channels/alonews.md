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
<img src="https://cdn4.telesco.pe/file/Y_jSktuvsFhV0Kx2gy3l4stVQEtXuc8U1nJmK_n39L0iiCM6OkECDfhbjd8duQfzEutHONwagdvlGRaIVy6Kyb7PZcARhiQuPTUoIgc8ntH3_Sc9xA6f_zhlkZk0ginDi8HgcccLT595iRDylLUbQpuhUh9GNHF_hpNmRK6JOkpryD91GH6-OdgvxXh2iAcg5gSrPOfe-7zoG1Ku70mapjApS84Z6VmjI49rgtvVClX_AUvAYTiVL0GNPwKDI5JZ-8A9lRIgvpJWuigcuOlgZOmL4Hh1JnT9Ue9N-oM0aUq60uH5d6XLlXh8tTYxVa8x0vcnlV1jNutsYPOkaEk6vQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 971K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 16:19:20</div>
<hr>

<div class="tg-post" id="msg-125550">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e63a2b05.mp4?token=COjtLsQLZnv0zi4JSZ0u8Q-gz8o2GsCmnoaw4_zWlpZYoNQHW28eSx7GQvES72g2usEwPhgEOR7Yh2W7Ywjbh1vmSc7mpEwSAHt3UA95rWlWSkesD-6VsrtV0XKJQlYC4FvGAW_aGBE0hupLtlRxwYyvmrBGZv_7O9xy69yR56YNShxFDg32u_lei00PK_xXBO2DWx1lGxruYqoZDRi96eeBcyxgX8e1Z3Aa8hG-pHaZGuHZSpjmu1vdAh0qdRkP-dgPZ-sK6V6cOg4jFve5ntovYhvM4sjmV9X3tGdS1uET032jc2oJxUvlqGvxLmP5Mn5AP0r-dhYNH51rGflg9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e63a2b05.mp4?token=COjtLsQLZnv0zi4JSZ0u8Q-gz8o2GsCmnoaw4_zWlpZYoNQHW28eSx7GQvES72g2usEwPhgEOR7Yh2W7Ywjbh1vmSc7mpEwSAHt3UA95rWlWSkesD-6VsrtV0XKJQlYC4FvGAW_aGBE0hupLtlRxwYyvmrBGZv_7O9xy69yR56YNShxFDg32u_lei00PK_xXBO2DWx1lGxruYqoZDRi96eeBcyxgX8e1Z3Aa8hG-pHaZGuHZSpjmu1vdAh0qdRkP-dgPZ-sK6V6cOg4jFve5ntovYhvM4sjmV9X3tGdS1uET032jc2oJxUvlqGvxLmP5Mn5AP0r-dhYNH51rGflg9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روسیه در حال استقرار سامانه‌های پدافند هوایی Pantsir-SMD بر روی پشت‌بام ساختمان‌های بلند در مسکو با استفاده از هلیکوپترهای Mi-26 است، به عنوان بخشی از تلاش‌ها برای تقویت شبکه پدافند هوایی پایتخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/alonews/125550" target="_blank">📅 16:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125549">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا: تحریم‌هایی علیه شبکه‌های دخیل در قاچاق سوخت ایرانی. ما سیاست فشار حداکثری بر نظام ایران را ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/alonews/125549" target="_blank">📅 16:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125545">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aph_W4vCwxFej7kP9bcAmNFp5_AhGwcZMP_W3a7iJALTknln2KOfJTXsUuIJZAMpbrFCFKaDeQhJf6Po4mHQV3zQnpLSyN23uUxrkzWXJ0pl_vgiZtnvrh1-Ga_AXqz_3k5njel9RSg9XBL07tfpkG4VXmpDnt052nA19npY2DKiS6p8H0m4G1sQh3CKYd85pgq0pRM3FjHf0vJpeJSuCN9RjmW5_5s6FEc-7Ee6wGSstJEomVbZPebnuX_fYya6leiYnT9nqHCD0kqGTXdKdOnl4SfVkrnxJo36xEbQw7oqUhnknTX-3HB6f5EFWPh6dRu7kmDb4AtseNDbJ4dt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ukxogvXu03mnsi86GAT3zS8S7RsQDQ_XNDKxqyXlzrcUS1Wgao42NNRgvz5CqxjvNghmvS30VVNVb4Mve7yJDq5iDdcd0HSQe0TLY_rbE57FuwzVmANVtVEenkv_2XH1ALEnSJTxr0atRluNRlsHsGZ33c0qi5f5qxgHXEYpTteqhgfZWFVl_ylv3W1kMW3pvXwgn6Sp17_QMh5DJp1qbK1WkITX3mPw1-0BtZ0zZT6oBNRXopG5UiIBT66XEKX61svB7n9PjncdvHEY5GFmBaLq_HSQXmXlCXl7BuG7xbVbaNLjBIRYyhY-O5HD14g0vIFZNHXR-0waUy37FJRCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3gklu0Z659sp4l_Pd-BERyBebqhdyutSdaDc81M3y4JijfMXLVHhSQyracMQOBaKtImQvCVmGlqgZubEIUuYCQVGLUmbUIMoMqNj4IYZdyhfhi3MqqjGjr-JR1u7a4nTN4AVhirVYfIR2KTDXKe8BWKWVzLMseezwwai6JqVuPF63aBj8eEtNUfld26Uqb7z8dtU7UAzDQEN4mNph3wyTn9mtoFv5NqAjXRiOriCa_4hKvDqzHWlNRnzsnRCKw-eXSlpC1DvrF2m-SxdYJRseyieO9g5MbPQJYY-PQCd9Nf5GsEM-u5EKsx1jKmek4-J1aQNMShghiO4o35LvD-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJLGNtkHRDF90cL1g9PhZ4Md37TT5GUTtO04ual22Q8I0vtknssytVSUPQ55hrEk_uOxUM0GyXn1-CzvQJccXQtb5sVMgSXoskkYFsJ_dfnSvxrS50e-Wb_bh7j4UcYbmtSxzvz_fiV5mnXdlJULZ1rvd9KCrMQIX71T1dRDoyfRTutFQDmZLTo4TC2dSf0FOFb6yjS3d_EVRwxdcAtVWHLAGadpaHSHL56zPFFhnUCm7BTOUDrgltlAYCfmU757RXWL8eetXeLK7Y_EXsBU-fUYYGlhAXQe3kbeSQ4i9bZ8W6bvvGVUozr5Xxi0pwRoQH51FqPdIoazSPQxiy1TPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی در چند ساعت گذشته حملات هوایی را در سراسر جنوب لبنان انجام داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/alonews/125545" target="_blank">📅 16:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125540">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vNuiS5AFfW_iFH89Z7ixie9JF7Ediovlm1BLeFLh8SNEhDf5h-nyDr78STNWkculx5qGTe5stoneTJmyOrYXiFdRZhBuHt82PWlQ4NlZQhYftcJBmH1i0w8Or9fwewXB9CAjO15QBa4p_BKYqqtTI_plt7_FUmdZ7wgUEQkKzxwGTQRahk6C2r0oEnUuT-f5KcvM2yW37xcI7w7foWFxq6u269mMZPfgDd7AzgzlwUUTw78Jls2k6ifvzXCSNpmUorfLY2k3Xr5OoHmc-Pl-KjMlJ3M6V9-3inABm7cnqeiu2B3EEivTRCjlnN3n3K5JU5DiBdc9iDALip0jrYRBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kn9dlxyUCol9eyhU0z9x5ch0kDv5n7-x0vpNwLX5-bYMWWWjAdZXurs6Ttm2xmiXajOBARV1fgq8EJ83AqFOY3YBk8pM04XxeRendMA-dxYhq3II80POQG5NTFIbAOMn94SakpPu6TeEwVBTpiszXRH7D6GdMNSAd8qG-1EhxquR3r-e2pRdeNrymNn2SZgfUnGMJogAzxiUC8GYpW3-e9zIexkwfAHuLBkjm8gYsEtJwLHfWnY7O1XShLgj0CvS-96YNKSsqhXw9nLyp7FoJS2dkDDuaOK3ZoB120MZ8N1FWo2EZRVjSANy-Q71HyAlsLUWJlGmRJComzp2SEQEKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nb3d-npASTk_34aKBEGaMycquC6Re_utibdYiiqjDt4bkeZvZn0VFvzu5toNmvtpTgNBGDARZB-wcizGmSlZnuOdBJqpxDhaeul2DTlON-oicPzQfIjtcZGCyS8NrwtwSgCY6hmFOyf5sYNXqcNCwzPtB_IRAbHZsYk0cLaLe8Af3OPQcrtdJOuzcF8z2-Kuaje6uYS4p1Z5hKazsElXltdV7ShdhmsXCJUIhziDYkfuWfVBsYfY5ZBswmHAWfqXc38zSXIX-S7EhDVPBQOnjfvkUl-f4u3yoZB4-j9H4lOWYsemqRx9PwjZlrY-ijsFxRgIKGe4y1wUpqthDGAbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPTcs2CLeYewkBzdarwJzHQfTSwLplTKD66YH1f2oX8d1BdCO5KUFLfXVsdk_SQpEouakSVsyhyz_PLRBpSf0Iifkd0w4z7HXgDRVJt7YCWr7q7bLvLjM5Fa_c_ekA4gGjUfsUgoeC_-tDGlE1I1QKY9Oqm7orBNcl15e7JtfQIZrDNQtDbeLgOfCcCY_C1JMH69RuFYPIUUFtq_iwONyXb-N33tnKOkXBFeodr-vtKtYdW4H-ejP14TxBtPYF7WgYM5nRtdyeGAlGPpxAjVaZAdmCkUIP_lj-mzF36IfrkAuDf2tRyqBXLAhJOHRro6KOeQh-I9E9dhnYDh6C-hQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DCXhqUMNKOxSWPRichIZMEaexHjHFBOGt4xGs-_G7Me0yDVTvMOVmxnNqe_Dpv8HmwTRGHH6JpOatG4wXFxG6Z76Far43RD7sZlWo1r4WVgdpGmqv9irrkHaYvmvh-HevUF7sRFT54mRlP1dhy8wEjIn8fGUOJSvjgY1TokiDSKOMfNsREK49BEAfnjHyZHLr8v5tuYbZ-OHwtwr1Qnt1I4sdWOMBaYstjmyQkGu9ptMS9hcJNvmPm0fpr_vHbLghZCby8SmM9G28BmnTP4EQWuG8vROwuAqk6iMkdJeMgXOXzRKvnqGWusx2vtINXJUTdEMp6gwlfTz5JNknDbIPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کاخ‌ها و دروازه‌های تخت جمشید
۵۰۰ سال قبل از میلاد مسیح vs امروز...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/alonews/125540" target="_blank">📅 16:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125539">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGDJiEEihDVnGj2DJqHp3PlhmndUYQJYlCcdP7Zy8TlKxhxvZLB0T-4H3-QAM8j7TCKCnuDiTRfIC8QQtIc-Dv3t1TV_fYo_kTZTLPsWPnSJIqwrMuxpTbyOwfVaruKuerH3avlRqsQ2mzGEKHkS--3rQRWC20-dJxBl2X6X8FMN-B_ypzhvkoMaNw1nynqJC6Kns9M6wgmRNyhWcwp2jSrNd9i5DifIaGNPJc4NUbnthR7eu6E6gnr_CFyr5BBwyOx5P4uZJXwO1kSq3QG4csfBfyDGJZrYJtWE4fI1acJU-i4daSOrE4z6k02uVfUI0BF0lPWAQStH5FiZLKDdVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ : پیش‌تر هشدار داده می‌شد که بسته شدن تنگه هرمز یک فاجعه تمام‌عیار برای اقتصاد جهانی خواهد بود؛ اما اکنون مجموعه‌ای از راهکارهای جایگزین توانسته اثرات این بحران را خنثی کرده و مانع از عبور قیمت نفت خام از مرز ۱۰۰ دلار در هر بشکه شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/125539" target="_blank">📅 15:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125538">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSMfRatoZRerlYrCC45QPIMT5ZDw1U4SvYzS-PfAuCrYa-2GGVU7OyA8c1VggjNBmdZ_kkOer9-TfK6asQhZecVT0WQJzY6rdqvolwEOS3XuPKX_DopL1efCgYA5NAjhv0uQYFUW51DWCu8K6uC58h4vpES6zfZ8FQmllnKZDBDp9yNeyXqnN-di9AY01zyjJkurdcNSMlFPaS9W1mQxNyJqFyeZt_hDzmL5ITK_KiXcIv8p8XJ_optjjztgzVkBBKr0Z0mBkCfZrmXc-_-4wlESGhMoY_c-A5ysxERlHmRlvnD0D2iUdSPM3tKDuszio9_1cqwhgA8Lh3BwnkJyeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستاد کل ارتش کویت در بیانیه‌ای مدعی شد سامانه‌های دفاعی این کشور امروز موفق به رهگیری و مقابله با ۷ موشک بالستیک شلیک‌شده از سوی ایران شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/125538" target="_blank">📅 15:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125537">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
صدر اعظم آلمان مرز: آمار مهاجرت غیرقانونی در سال ۲۰۲۶ نسبت به سال ۲۰۲۵ به میزان ۵۰٪ کاهش یافته و نسبت به دو سال پیش بیش از ۶۰٪ کاهش داشته است.
🔴
ما این مشکلات را به روشی بسیار آرام اما بسیار مؤثر حل می‌کنیم
🔴
ما به افرادی که برای کار به آلمان می‌آیند تهمت نمی‌زنیم. ما از آن‌ها استقبال می‌کنیم.
🔴
ما می‌خواهیم آن‌ها اینجا کار کنند، اینجا زندگی کنند و در اینجا ادغام شوند.
🔴
این دیدگاه ما از یک کشور باز، لیبرال و آزاد است — نه انزوا، تبعیض و تحقیر شخصی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/125537" target="_blank">📅 15:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125536">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C28C5mje19vK1r630f0IdeLHxvwBHgZ23Kt-6V6-9c8GlJnrfsZxGmrasazmBCyIcm6PwZzt5dEiahW0MNQPGyyrzVWSRdBJ59jhNzbTSihoTRVpzJs7a5eMpZgj6oKkTr51M-44PjvxVowtTW4l0DkUe4e29ULgTUmEspdwmbAjxZvlUQjYr1Yd7ZB17VLIA4bx9DZfWqe1ZW5gYa6XZVVqU5bWVtyLFLf15lrBTt46OZDplzPkKrCXRJdxc4tQsRnK7r6Vq17xEUSY-jYNtOzHWSUT0oaBRELRTtqIwpCd6sQJVzlTRKNIs_MIeehJXAY7q9dE90HHT977JIGqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده فروش نظامی خارجی احتمالی به ارزش ۱.۵ میلیارد دلار به نیوزیلند را برای پنج فروند هلیکوپتر MH-60R Seahawk و تجهیزات مرتبط تأیید کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125536" target="_blank">📅 15:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125535">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=XvRpqLJTZGB8pY7081csxqFPThwib7mZhlPNSRz6nMOcB3WHFNMCIPr05JoJG76MAuY5kgDu78gfvkxpfh0wabJuGf61fjhmgZ0bf22LW1kJ6ZIAUZxE-ZlJ-Bl2NjLzY4__LjQlsU-0fXDGFBO6DPLNDTnRPkgtiJ0IUdOWTmD9ZZK7HC4PKks2_NBE7Xd6D1Jb_9Uwz5Ft4Rozhr3kh182eAWtg8K3Sx_HFB0bkDkgRPhCF3N_NKwXI7gqgbLbHBXNS7F2SgQ9K5i7-i5IO8dhtQK9ZVXl7cF9dqlu2ngpVmkr979tWongH4NUnOOz8uMasPvhN3pKw-fTIDY6Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=XvRpqLJTZGB8pY7081csxqFPThwib7mZhlPNSRz6nMOcB3WHFNMCIPr05JoJG76MAuY5kgDu78gfvkxpfh0wabJuGf61fjhmgZ0bf22LW1kJ6ZIAUZxE-ZlJ-Bl2NjLzY4__LjQlsU-0fXDGFBO6DPLNDTnRPkgtiJ0IUdOWTmD9ZZK7HC4PKks2_NBE7Xd6D1Jb_9Uwz5Ft4Rozhr3kh182eAWtg8K3Sx_HFB0bkDkgRPhCF3N_NKwXI7gqgbLbHBXNS7F2SgQ9K5i7-i5IO8dhtQK9ZVXl7cF9dqlu2ngpVmkr979tWongH4NUnOOz8uMasPvhN3pKw-fTIDY6Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اطلاع‌رسانی عجیب مجری صداوسیما: مرکز ناوگان پنجم دریای آمریکا مورد اصابت موشک قرار گرفت؛
نه ببخشید اشتباه شد
؛ صدای انفجار در جزیره خارک شنیده شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/125535" target="_blank">📅 15:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125534">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ    برای ۱۰۰ نفر اول و یک ربع بعد
😍
❤️
🔥
آتیش زدم به مالم به خاطر عیالم  بقیه هنوز VPN حجمی میفروشن اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
🫴
ویژه ۱۰۰ نفر اول
💥
بدون محدودیت…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/125534" target="_blank">📅 15:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125533">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RHvUz67QqPXuBEOympxb_88uVEzkKMceRbqxNxhVQ0eaSj4BkO1HuvkwNkfK_1q6T7INrL8QknPJL2pI1WsL2zvh-72kOb8o72ZuQQ_z4FjawptzmFb9dBdEFPqxpTaugdGcfn1cB3QdtCqSZuJ8okMc1yWzHaEhF2I3f_fFgXVXCc8UEAMobZQqorXKRW7DhPUrAfyc7fK_rmlY3N3UBt6ij8pG1Ds2YyQYPdq-N2mrYl5REjsjrTpvOlyxWRye4lUtb8Bvp7yUD8rJF2MGRuhKjfPBPK6mk7oV_H2H_CmzDEkkMxHotKir9siB9zVHxavI7DhJURdtiDNdjC3MEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با سابقه ۵ سال فعالیت مداوم
🛡
حتی بدون قطعی تو دوران جنگ
برای ۱۰۰ نفر اول و یک ربع بعد
😍
❤️
🔥
آتیش زدم به مالم به خاطر عیالم
بقیه هنوز VPN حجمی میفروشن
اونم با قیمتای نجومی
🚀
ما چی؟
💯
💥
VPN نامحدود واقعی فقط 190 تومن
🏷️
🫴
ویژه ۱۰۰ نفر اول
💥
بدون محدودیت حجم
@NetAazaadBot
@NetAazaadBot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/alonews/125533" target="_blank">📅 15:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125532">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFUWvuM43TKnQKETj2V9JjK0y4fq4ftc6L9aSEhMDJ3nSB_YesPN0NQFk3UZSg5MvsZ_LicOPtZT7F7WyksSdZon-rj1IC1vF0c4IeBPaI--Q7CnXjuflQvwP-4cVgdVND3i29H3hidi966TFCcv6Vc67lo-XWkslvY26RQeaxDKBPrrEakvIWgdiURZxt90zkEhVEHvRUfgQUkDX_CnTDXQaIcAiosG5MCxGqjZpFtI5LtCh6BY8t2khmCCbF5XzL2_ISGi6F8n-BbAvaHV8YdHDdjwaVBS89ZtU0oSQvBU1D8z6L67yjnVwPedXhS3LKjtaJxT-sGI-y0uHsO01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ : از ماه می ایران نتوانسته نفتی را از طریق تنگه هرمز صادر کند و ۸۰ میلیون بشکه نفت ایران پشت تنگه هرمز گیر افتاده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/125532" target="_blank">📅 15:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125531">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری / الجزیره به نقل از یک منبع پاکستانی: وزیر کشور پاکستان در سفر به تهران حامل نامه‌ای درمورد پیشنهادهایی برای بحث منابع ارزی مسدودشده ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/125531" target="_blank">📅 15:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125530">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
سازمان اورژانس : روزی حدود ۶۰۰ تا تماس مزاحم داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/125530" target="_blank">📅 15:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125529">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ459Y7cJP38PHx71VFI-JF7M_ZSIobV-t0IvxPk9g93ZCgbaH6IwyNfFVOxWoJSeGbwY9GIhV2upzDDl4GD58cKv3kGq_GVfEtAfPiZ9pwTyZgkjK_Cb_ysrycVkeQ5TY0LA7Yci8oEKavA4F-vKRi0HNy47vTtWz1kECg1QBFHn_dT8Pz1bJmV2HGsl5OvR06yB2dF_4w4nxd1m0ewEwExpxlUK4v5iqUQhqk-dE-3XcPfZhhmnEQgqJNLVs_Kg08_F-TQPex5CtBCzOragKpoVnU72IyNoWr9R7L1Gux-XKxpjyGIs_OA9CjSNyC0jzddE7-f_bShurr3V9Z1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امیرحسین قیاسی: سکوتم در جنگ اشتباه بود!
🔴
حتى در صورت سكوت هم معلومه كه من مقابل كسى هستم كه بدخواه كشورمه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/125529" target="_blank">📅 15:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125528">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbYGtnLWdkBaBtuGfoHi2ezVyrIy5BTT5aiSWvuTT8WCv-u41MjE5TxXb9E8B76xTrMYwSRm_QrItDZeuBdS4FFJTBbvMhRo6zEQUSVCOE-ooxc_yjGIAsDP0fZgTaHhyvPIHjApuljt3KYX9myOjwIBRC5h53uccDA5P7VQ3ZemkWWniywNZOO_2WYXPYiQU-l8fsoyIVyegtgIJgLbg9dkZJLFSVA2ulUjWuyLzsxzKlE7iuG3JjGxVwEJhtHEtLlbrapHVr3NRR7HoaTN9_QplQ5El-Iz7K1X77e52Q_91Demm4vyTN4q7kcVENPZE9ZUwhN6vD7xZEBFatp9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزرای کشور کشورهای عضو شورای همکاری خلیج فارس (GCC) جلسه اضطراری تشکیل می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125528" target="_blank">📅 15:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125527">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=fU50Hs6QBDgx7xorn-yLgg_imy3Nw9IVoJNMQRFMHw2IesPxAI9OlELuUEMktkYkTWdbJTVd1WRCwHE0C6meOKme1JKy_j9g7SJcgCC5ThIGCyEyGTbsVml0SZJ51LV3c8VSwK4xKgEbTvmWzcwg8l7YAjFo3yglRrzYDbtTlv2JFY1J1RoYcC1eQs87y_z2mc8x8ksfNQgNV_ThRhjpFNaTuUMCocJW_HB-hi0BcIKAWYZZrG2Np-qY_eJht0dai_wbkChqEltBr14nt910R21Y8-oQQUZs1HjjnJ763l9t-eqqC0OUUucCXy4PCPiYNr7C_azXulU1BctXf9bEag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f4e56d3b.mp4?token=fU50Hs6QBDgx7xorn-yLgg_imy3Nw9IVoJNMQRFMHw2IesPxAI9OlELuUEMktkYkTWdbJTVd1WRCwHE0C6meOKme1JKy_j9g7SJcgCC5ThIGCyEyGTbsVml0SZJ51LV3c8VSwK4xKgEbTvmWzcwg8l7YAjFo3yglRrzYDbtTlv2JFY1J1RoYcC1eQs87y_z2mc8x8ksfNQgNV_ThRhjpFNaTuUMCocJW_HB-hi0BcIKAWYZZrG2Np-qY_eJht0dai_wbkChqEltBr14nt910R21Y8-oQQUZs1HjjnJ763l9t-eqqC0OUUucCXy4PCPiYNr7C_azXulU1BctXf9bEag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فوران آخرالزمانی یک آتشفشان در هاوایی
🔴
طبق اعلام وزارت کشور آمریکا، فعالیت این آتشفشان در ایالت هاوایی همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125527" target="_blank">📅 15:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125525">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiVSr0dJkXYYHeifbGYzOTk8u_UTMXUBmp7aKFzQUrwxW_vBFVlaF8urgRri12qmcZvEHVjvnx7Mt4ph4SRMCKu9v_dxsRGdzaM7NFFjioCM3QW_AyC2gGK6_1LeriFhQCpquVcA-L293jDcwM_GEBQB-iFNZQFM6iKf_wFecCypGimItPeg81CABHP1yU_9zfDkOjo7aRK_nG8oBoxzxlBF2JLlY7Hrrp9zDu3z6xsQ5pvhW3Egq1LKItmGoiybC99mIsA5LIsAqHZZovU6y7KHmet6yBE_lkecqb6i00g-FsYxRR29-8mqLnBxIX8Sz0BhDVPziTws0gOzANbhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25126b98d.mp4?token=AYSrVuWR_kxz3Y3Dub6dyHioNUianu5UNxzlv7wXAB3kvH2njtZ74bZO6lksPnKQ1BCBbep_6fDDVlNvvVd0ldCLnGh3xa4vwBAlhTDGNV45rfKB1ZlaQDYsSQ7-d0qIBNNQs5lNjq61oytowdKwlA_5wg69CgEHi9jbDZiDEk-jUJHzWYTT5HjKvzGDP7_MGO-lzxTyITwrtSUjL_LeSoklcMRA6DG4PKPZKjImlMTvr6VT4loirBirV9X48NoDYiFeQYtJtkDYGQfCLyg2BkEYnQbLm_1Uxud4Ahqx4-YG6UG7BcxLzoBdb1TIRZG7zj6H2uU3ibMz7D9Xn0Czdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25126b98d.mp4?token=AYSrVuWR_kxz3Y3Dub6dyHioNUianu5UNxzlv7wXAB3kvH2njtZ74bZO6lksPnKQ1BCBbep_6fDDVlNvvVd0ldCLnGh3xa4vwBAlhTDGNV45rfKB1ZlaQDYsSQ7-d0qIBNNQs5lNjq61oytowdKwlA_5wg69CgEHi9jbDZiDEk-jUJHzWYTT5HjKvzGDP7_MGO-lzxTyITwrtSUjL_LeSoklcMRA6DG4PKPZKjImlMTvr6VT4loirBirV9X48NoDYiFeQYtJtkDYGQfCLyg2BkEYnQbLm_1Uxud4Ahqx4-YG6UG7BcxLzoBdb1TIRZG7zj6H2uU3ibMz7D9Xn0Czdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فیفا ایرانیان را از آوردن پرچم شیر و خورشید ایران به مسابقات جام جهانی منع کرده است.
🔴
یکی از راه‌حل‌های هوشمندانه‌ای که ایرانیان ارائه داده‌اند، ایجاد اپلیکیشنی است که به آنها امکان می‌دهد پرچم را به صورت دیجیتالی و گروهی نمایش دهند.
🔴
از ۴ نفر تا ۳۸۰ نفر
👑
https://www.iransync.com
#جام_جهانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/125525" target="_blank">📅 15:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125524">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزارت خارجه قطر: بر ضرورت دور نگه داشتن منطقه از پیامدهای حملات بی‌دلیل تأکید می‌کنیم و بر کاهش تنش برای بازگرداندن امنیت و ثبات تأکید داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125524" target="_blank">📅 15:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125523">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
الحدث به نقل از منابع ارشد پاکستانی:
وزیر کشور پاکستان پس از دیدار با نخست‌وزیر شهباز شریف و مقامات ارشد، امروز عازم تهران خواهد شد
🔴
نخست‌وزیر پاکستان دستورات ویژه‌ای به وزیر کشور خود درباره مذاکرات بین ایران و آمریکا داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125523" target="_blank">📅 14:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125522">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سرتیپ ویسام صبرا در حمله‌ای که صبح امروز در جاده خُردلی رخ داد، همراه با تعدادی از نیروهای نظامی کشته شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125522" target="_blank">📅 14:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125521">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
منابع رسانه‌ای و وزارت دفاع بحرین از وقوع چند انفجار درپی حملات موشکی و پهپادی به این کشور خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125521" target="_blank">📅 14:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125520">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
اینترنت  دیتاسنترها همچنان قطع است
کسب‌وکارهای اینترنتی کماکان با مشکل مواجه‌اند
مدیرعامل شرکت آسیاتک در گفت‌وگو با سیتنا:
🔴
برخلاف برخی اظهارنظرها مبنی بر بازگشت وضعیت  اینترنت  بین‌الملل به شرایط پیش از دی‌ماه سال گذشته، دسترسی مشتریان مراکز داده (دیتاسنترها) همچنان برقرار نشده و  کسب‌وکارهای اینترنتی کماکان با چالش مواجه‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/125520" target="_blank">📅 14:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125519">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سفیر چین در تهران: همه طرف ها باید به حقوق مشروع ایران در تنگه هرمز احترام بگذارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125519" target="_blank">📅 14:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125518">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5580004caa.mp4?token=rLT6CKVHCdt7rS9tf40vZ7yVyL2Fl0Ucl9tEjjmkak9te3-4xqOOOxSNM-N-Sy0XdaOSykrHhOzH9Xtk5S3EojTVqYNWyx7hOzrkPbsqSatUHykBKW35O3XiEOmvsuIUnrTcJyzlPmd032ulP3LNNlp7ljCPi9NPm1APso0CBfBFevEIXDd_VpQqLkBDdIWZrXp3unL3rmNPm6rboG6UMc__fbHVDl1LDBAp6jGNLntizO8Qn38AYIojBl8kkbjsWaEK2Vv0bGMEsudykv63pnlK-w960HKvKsoHqilxXrqWPo4VoWT7lxzu9ehv3r-tnRjjlrN57QyrpisMvt4xDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5580004caa.mp4?token=rLT6CKVHCdt7rS9tf40vZ7yVyL2Fl0Ucl9tEjjmkak9te3-4xqOOOxSNM-N-Sy0XdaOSykrHhOzH9Xtk5S3EojTVqYNWyx7hOzrkPbsqSatUHykBKW35O3XiEOmvsuIUnrTcJyzlPmd032ulP3LNNlp7ljCPi9NPm1APso0CBfBFevEIXDd_VpQqLkBDdIWZrXp3unL3rmNPm6rboG6UMc__fbHVDl1LDBAp6jGNLntizO8Qn38AYIojBl8kkbjsWaEK2Vv0bGMEsudykv63pnlK-w960HKvKsoHqilxXrqWPo4VoWT7lxzu9ehv3r-tnRjjlrN57QyrpisMvt4xDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی از احتمال بارش باران، رعدوبرق و تگرگ در نوار شمالی کشور خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125518" target="_blank">📅 14:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125517">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ به میانجی‌ها گفته ایران باید زود جواب بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125517" target="_blank">📅 14:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125516">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
غریب آبادی: موضوع رفع تحریم‌ها و مباحث مرتبط با مسائل هسته‌ای در مرحله دوم مذاکرات قرار دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125516" target="_blank">📅 14:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125515">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری / الجزیره: وزیر کشور پاکستان در سفر به ایران حامل پیامی برای رهبر ایران خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125515" target="_blank">📅 14:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125514">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجارهای کنترل شده در بندرعباس به مدت چهار روز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/125514" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125513">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxomYn7VVHEnudxlmqsn_n2pNgpHFHuDUKTrcSdt3jGvTQ5MCcJIyYb1OJBRiMFBxrE2F-o429U1bKcpenscHV9cCtcwbelwjQ9tvLtdbxu-TgydarfTlf0ub1AvzYGC47PHSmBvbGOu4LUQS_7b7epOotxzVVkwnmfL6QVYRn1MyIWd2eTOisjRno_B4FpDoQ0qFEVFpwCrqs6QHzl-QoLndEp90WgvUZmxWccbqcO2KasafFjA4z6isQvdxRkckEQEn9_tBthtnjZMt-d2DiTncWnkDzBzpegUd8tvMfXCMxjaD6xqZj-6ZBU1taN0MqVBN8JLwTNWsPF0ZMChFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الجزیره: نواف سلام، نخست وزیر لبنان با اشاره به اینکه مشکلات مردم جنوب، مشکلات تمام لبنانی ها است، خاطرنشان کرد تا زمانی که این منطقه در معرض تهدید باشد، کشور در ثبات نخواهد بود و دولت از حق لبنان در دفاع از حاکمیت و امنیت خود کوتاه نمی‌آید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125513" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125512">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
دبیر انجمن صنفی شرکت‌های حمل‌ونقل ریلی مسافری: ۳۰ درصد قطعات یدکی قطار وارداتی است و دستمزد نیز حدود ۵۸ درصد بالا رفته که افزایش هزینه‌ها را به دنبال دارد. قیمت بلیت قطار در همه مسیرها ۲۱ درصد افزایش داشته و از فردا اعمال می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/125512" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125509">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/999b104f0a.mp4?token=TYUG3K290Yq7GMWouQ3cpeb7OQ9tiiB6MkUlu4KSKQ2u7qR99F4DNVyCjrGTBh5okPJBfdh-tc1tNWckrJMuPqazMRU92-vewARFhcnzpluomz9Vl7qZ5_0cDGynjIWtoCEL9KRJ2iqAtn4BI_Q6EE3AWrO64kDplr2cLgiZgt9AF4-Tu1J_Tqvu30JkqTSgQemUpfeCwXCNvvyIFSx7AmnsypXTDzmQUuIvTZnjNzg8465iESB2ID1IweYNij4dSu57vh-4zycgnLzHDs6sSl_k7vWce0_tA69xHHfHOJ1rqmHq8VT0QzgGWxZWOOAabi5_774QoismcZ_7C8RKFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/999b104f0a.mp4?token=TYUG3K290Yq7GMWouQ3cpeb7OQ9tiiB6MkUlu4KSKQ2u7qR99F4DNVyCjrGTBh5okPJBfdh-tc1tNWckrJMuPqazMRU92-vewARFhcnzpluomz9Vl7qZ5_0cDGynjIWtoCEL9KRJ2iqAtn4BI_Q6EE3AWrO64kDplr2cLgiZgt9AF4-Tu1J_Tqvu30JkqTSgQemUpfeCwXCNvvyIFSx7AmnsypXTDzmQUuIvTZnjNzg8465iESB2ID1IweYNij4dSu57vh-4zycgnLzHDs6sSl_k7vWce0_tA69xHHfHOJ1rqmHq8VT0QzgGWxZWOOAabi5_774QoismcZ_7C8RKFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امروز هم در سراسر کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن و حتی جمعیت از سه شنبه هم بیشتره.
«خسرو پناه حیا کن، کنکوریو رها کن»
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125509" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125508">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJ697uIi4ilC2JYfY6EVdlZZqn2QrLuXvTrP5Y0jv-CpcjbDGYzYzcIxvffxv6PkN62pPxlO-f-rNgBKWyONZJLhq-nlHMQL0SrvxeVdryxX8TtMMEtahp1ijt6FWsQVNX5cl59J5vYbpj2mSsFu0p0L1FTEQ9Rjk7tcXXBmWblfMc20R9HYU_wLaBP2okjJyWKlAopKkF3FQdRr8yvmFIRPusqrEkhpOdEoxHYQ5Mq83WNEdICAxHdM6vsDY6PvnGAsg3IKjrGEF95EGN-BGyWTDliyhViSRTSnD2_vGNzTnYjPwGUUbNSXch-bqi0bTJruhytcYNPAG9t7W4BreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داخل امارات یه منطقه ای هست که جزو عمانه و داخل اون منطقه یه منطقه دیگه هست که برای اماراته!
🔴
خاورمیانه همینقدر عجیب غریبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/125508" target="_blank">📅 14:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125507">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3c6f0cb3e.mp4?token=vFy9rk8o0z8yUxgUDwopDOIebRQXuiG7oCBPb5VXyY_xv2NooSuUeILn8Vqr6sLjVU6kR9yuIT-8snY3Nqa_IcYv1xZ-28DGmyEMQnYCa5e8qRv9Ei_oBMrH8yaBPk4iMNMay-0KeRLDZ5SMlU0ebWC3UWxlJ-uFiAVSI2c4gQOnesORqaGtIY8M8HBuxJVP_Wft66ywDKF6DAFkI_EVH3VlZRCew953ztvwOMzk2fdtQ8p-oaVXaraDCi_XwRxC-3Zvw-FoOAu3QH_WeHEq2h9EzPwzrreuxL-WmwnpSdf-5S7NMI39bqqMamZS1L3o5OBibNkEUGQJJxdlul7EXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3c6f0cb3e.mp4?token=vFy9rk8o0z8yUxgUDwopDOIebRQXuiG7oCBPb5VXyY_xv2NooSuUeILn8Vqr6sLjVU6kR9yuIT-8snY3Nqa_IcYv1xZ-28DGmyEMQnYCa5e8qRv9Ei_oBMrH8yaBPk4iMNMay-0KeRLDZ5SMlU0ebWC3UWxlJ-uFiAVSI2c4gQOnesORqaGtIY8M8HBuxJVP_Wft66ywDKF6DAFkI_EVH3VlZRCew953ztvwOMzk2fdtQ8p-oaVXaraDCi_XwRxC-3Zvw-FoOAu3QH_WeHEq2h9EzPwzrreuxL-WmwnpSdf-5S7NMI39bqqMamZS1L3o5OBibNkEUGQJJxdlul7EXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
«هویت ایرانی» ما بر روح و‌جان ما حک شده! غیر قابل نابودی است!
🔴
ایران بر همه چیز الویت داره.
🤔
قابل توجه عرزشی حرام زاده که از تخم عرب های سوسمار خور عربستانه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/125507" target="_blank">📅 14:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125506">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=ojM8QB905N1YAKuM27PDIalD_TqwsCx3zWGwAEw4MWCSyq83_9cSUzSNuIHlyiipnBQSRcDcYjsnhThuLuoq2gJTKH-_TlSZKieGKLbThBkQ30LFc2klH75pbaHsUM3kYwFA9-G_db3nlhy-exyaKhVsDm_zXMseofTxWCI7SJK-plMaYLVk4DJWvod_g6nfLmpI9vL0zZvMT4wqYiYar2qJBz8A297e6Bb0HzN9zFr2AwBsQPZ6pIOY_oMbHhXBnpNsriwfmxoHdsGr2IhjdeVieAXENJGvGm1KpUi8aEtM8zvjJkpVnfeK3te7WFK08wsXOlNnkrW207lWcvH74w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97ae3c51ca.mp4?token=ojM8QB905N1YAKuM27PDIalD_TqwsCx3zWGwAEw4MWCSyq83_9cSUzSNuIHlyiipnBQSRcDcYjsnhThuLuoq2gJTKH-_TlSZKieGKLbThBkQ30LFc2klH75pbaHsUM3kYwFA9-G_db3nlhy-exyaKhVsDm_zXMseofTxWCI7SJK-plMaYLVk4DJWvod_g6nfLmpI9vL0zZvMT4wqYiYar2qJBz8A297e6Bb0HzN9zFr2AwBsQPZ6pIOY_oMbHhXBnpNsriwfmxoHdsGr2IhjdeVieAXENJGvGm1KpUi8aEtM8zvjJkpVnfeK3te7WFK08wsXOlNnkrW207lWcvH74w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: مرکز ناوگان پنجم دریای آمریکا مورد اصابت موشک قرار گرفت؛ نه ببخشید اشتباه شد؛ صدای انفجار در جزیره خارک شنیده شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/125506" target="_blank">📅 14:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125505">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy2fJHcdtrmdCdpkJDn-GuqgBO4b2M_vIx8aPdcBuckOzMrSLDtrpIG7Ur-Pi_PWvRij1FXxoEnXCmZNXD-A9uDKBA9TkhrAKh2HooIyy2sgmyz7t_43cyt7uEUBSL9a7JkAxwqVGX6rd6GWsDZGsn0l5awmeFjBf3P1phZek7goBYnQSj3lTOJXdkr2aWsSPzOTSv8QkAEyzGICuTXqz9mDlgnvSEdnRzxs1zGEZ9p0sDjoGOjBF8ZDswDqCnslztwf2By8jDZuHQ09a7ZehyN0YrbaJtX420j4Ru_PN4C5eGUu1dPOBkYunWjB2P-MS4lJYmT8HQZwbtasW0laKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چند روز پیش گروهی از اتحادیه معلمان مکزیک، ساختمان آموزش پرورش در مکزیکوسیتی را تصرف کردن و خواهان افزایش حقوق شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125505" target="_blank">📅 14:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125504">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزارت دفاع روسیه اعلام کرد که نیروهای ما بر منطقه «شوچنکو» در اطراف خارکیف تسلط پیدا کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125504" target="_blank">📅 14:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125503">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فارس: ۴۱۷ میلیون متر مکعب آب از افغانستان راهی شمال سیستان و بلوچستان شد؛ یعنی کمتر از نصف حقابه ایران که در سال‌های نرمال آبی پرداخت می‌شود
🔴
فارس نوشت: افغانستان یکی از پرباران‌ترین دوره‌های خود در قرن اخیر را پشت سر می‌گذارد اما تاکنون تنها نیمی از حقابه ایران از رودخانه هیرمند پرداخت شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/125503" target="_blank">📅 13:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125502">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
بحرین: ما مورد حمله ۳ موشک و چندین پهپاد قرار گرفتیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125502" target="_blank">📅 13:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125501">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وال استریت ژورنال: دادن پول به ایران برای ترامپ خیلی سخت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125501" target="_blank">📅 13:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125500">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: امتحانات پایه‌های یازدهم و دوازدهم نهایی و حضوری برگزار می‌شود
🔴
کاظمی: تلاش می‌کنیم امتحانات از ۱۳ تیر آغاز شود.
🔴
همه ملاحظات لازم برای کاهش نگرانی دانش آموزان و خانواده‌ها رعایت می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125500" target="_blank">📅 13:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125498">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P1v7b6y2yPML-tCXGPsl194EHvJHnkVbidjoOBhX8eT-mLrwgMCoMJLdzzSEHHwJLXM2-vaJZgvUY4IA8PtpGz-NJlGQibHEyMDLlXmntbG19nAlQiOufr1a0xzYtthvKzWPrgrBse7U_zFgzuic70kNJpxW7MF4LtSKjXllwVv5mMdx2U9U184f76i29SeV8Nbls6hVSEA89bkOAxpeaBfwyBonBOoMRcTMjDCR5h1NkkoZhVGuvA4kX-0uzuFmMgZQyXuJPO2AhLhQdV4xwMpqd2MH2L1EesXv93qXAenrk7q5Yu3WMD3IaBDMQOsQN6cDSYNYdtioOqbNmZl7nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFwNCLn5PA6RJPiVtTmjWnentoQTBQRyRxtA1sXjgXnD0dT234fMnW70th-MmGTqG84RRZpp2jkOeQh2IHdAkjZRSb-CoV5b6Elfpex8vfLnKgmB_6ZZxcmioiwY4RiaZYVMfkCD4dIRDrCFUzt0DpkaYP-ExAop9ILaJmOGmL4fUjxdMXqNVfZQcapL2fhHcV9LddrBYW80rXG_zYd4V_wXEMjC9DwhXnpmxYGs1rcbdXlJFLJj7SH3LEZ6--1TSyXBIf3o2jQ39rwzwqzYUYZ6a8J3QVVgmT9GR8KnElOv1TW46JIlaRd5bIq7ThWq9AVEdNvKo0Up90ihyefxzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آتش سوزی منتسب به اطراف پایگاه هوایی استان شیراز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125498" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125497">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ایرنا: وزیر کشور پاکستان امروز به تهران سفر می کند/وی در قرقیزستان طی روزهای پنجشنبه و جمعه، دو بار با اسکندر مؤمنی همتای ایرانی خود دیدار کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125497" target="_blank">📅 13:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125496">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125496" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125495">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزارت امور خارجه کویت : ما حملات مکرر ایران، که آخرین مورد آن امروز صبح رخ داد و نادیده گرفتن خواسته‌های بین‌المللی برای توقف تجاوز بود را محکوم می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125495" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125494">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
العربیه : پیام‌های بین آمریکا و ایران از طریق عراقچی و ویتکوف منتقل می‌شود.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/125494" target="_blank">📅 13:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125493">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1GSHD7co7eSYRIfA76y3LieS4X01GXh0JvEA3n1qUD-yAdGN03DimiPPtt7rWN8BJu-8rhCsnJOy7uUikRgaVtASaLz9tzKk082mNbrJAfVkzMZ3lxyOCQsml5Ps-NFL62eb6B5gDkTldRoWfHsNolSiEFrHjyiZ3nzls3kTSifNZc5TvzUG7lurlcz-w-ARuH9_PIGsqpOUEN8hXkfRykpQhiZk729P-hnzXvYFhQ7uKY5Qoew9TvhPxIaOvppkKMW__8bza7W4q6UFZIPi02ZxfCW6GbXLzKehZ9eM6s6QgqXDF17FiEWFKvOwyg8OnvbzTtQBs-ZFUId5oAekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه
:
پیام‌های بین آمریکا و ایران از طریق عراقچی و ویتکوف منتقل می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125493" target="_blank">📅 13:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125492">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">⚽️
🇺🇸
یک مقام آمریکایی در گفتگو با رسانه اتلتیک گفت:
🔻
ویزای ساعتی بازیکنان ایران و اعضای ضروری کادر فنی این تیم صادر شده است ولی ویزای افرادی که هیچ ارتباطی با ورزش ندارند برای آمریکا صادر نخواهد شد.
🇮🇷
اسامی افراد تیم فوتبال ایران که ایالت متحده آمریکا درخواست ویزایشان را رد کرده:
مهدی تاج - رئیس فدراسیون
مهدی محمدنبی - مدیر تیم
محسن معتمدکیا - مدیررسانه
مهدی خراطی - مدیراجرایی
مسعود اردشیر - عضو اجرایی
مهدی ملک آباد - رئیس حراست
سروش سلماسی- آنالیزور
مهرپویا اسدی - آنالیزور
رضا جاودان- تدارکات
حامد افضلی - بین الملل
سیامک قلیچ‌خانی - رسانه
امید جمالی - رئیس بین‌الملل
🔻
تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
@AloSport</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/125492" target="_blank">📅 13:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125491">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سازمان میادین میوه و تره بار شهرداری تهران: قیمت مرغ تازه در میادین و بازارهای میوه و تره بار، بسته‌بندی کیسه‌ای( پوشش کیسه نایلونی) کیلویی ۳۵۰ هزار تومان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125491" target="_blank">📅 13:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125490">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">😍
قبل خرید، رایگان تست کن  ما کیفیتو با حرف ثابت نمیکنیم
😉
با تست رایگان ثابت میکنیم
🔥
@Netaazaadbot  @NetAazaadBOT
🚀
VPN پرسرعت و پایدار
📩
برای دریافت تست داخل کانال عضو شو
😍</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/125490" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125489">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cOMzujEEtMxmaO4KOFySX-ktPQNmqLI7rPuWnDMdawyzFlDuCy-hD-ynqrPfBUcMnJ0jHNhRnw3u2TMn0ug93JFWn60zKveBDnSlRmQygYKM23w9qu-ev_Q9F4L-fmBPjsMh7Zr_JBvU5ARzO4VGOEC0R-7-qQoB_yreIOqE_PqSHqToExF7hOXJhNAwTceXFWtLBKVe-cnzu3zF65DOAbLxRxfRhJYsCWN5PbpBTrSFRBsI6r6OW7sF7rJg_Pm4joyYY135WB2Ky6YXee-95tNa26sgodpwXQKFqmCUD61O0RPWpmmTZgdj23304wWayRsBbYSDKYoBQPPHbClW8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
قبل خرید، رایگان تست کن
ما کیفیتو با حرف ثابت نمیکنیم
😉
با تست رایگان ثابت میکنیم
🔥
@Netaazaadbot
@NetAazaadBOT
🚀
VPN پرسرعت و پایدار
📩
برای دریافت تست داخل کانال عضو شو
😍</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/alonews/125489" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125488">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
ژوزف عون، رئیس‌جمهور لبنان: هدف قرار دادن یک گشتی از ارتش ما توسط اسرائیل، نقض حاکمیت علیرغم تلاش‌های ما در مذاکرات واشنگتن برای توقف تجاوزات است.
🔴
از جامعه بین‌المللی می‌خواهیم مسئولیت خود را انجام دهد و به تجاوزات اسرائیل پایان داده و احترام به قوانین بین‌المللی را تضمین کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125488" target="_blank">📅 12:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125485">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpSeacoCo2MIC_oTgb6K3S7qqmjjrzCFc1B2KNHx_fMbNse1S77FTXLUJ7wj2XFYCMhCCsbNjdAEiMAF3_ikBV8tLzNMWFuMYS3ZeumLEh8IBBNWsy9jjkwVT3nrRs6XrDfixWmUMCJVnjpAieIqRzOtE-3y9bhBTndi_4DYHIOpDfXtrssGpJlHA6l6n_RciiB5FdTMGrxNzG8eZIdZ4OHO6Mw0UswqJIVkcjkGas4J0UFk4eoFqnh8xUjLFqMHmFfX57gR0Nij5PdtBc1jKCpd035K2OcaSuIXVChODsutZm-EwxXbY9ffD8856NuFKSBQExasKsEGcuxlLqoXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DxDDiQWj5_KWow59Sugj_gHPz6_rcrBlcyJZYhHGEa68zgNFkELZ-0KdszJDHQT3mxv3FbNoS80vwXivPocY_fJ0PAwWESQ8spUifFHu3uZ-zM3L808WYR9HfGHHIVi9u1rrjsKxIAAyUPuaYL2wWFG73Uo8vXBAItATe4TER4cW3IqGQfa6F482LLvdCB-9k3l_8Ptmkx9gCDWnJ4Vloa4jh8SEZqu0s_6AydyuEfHGMKCgHuoYBdy2PC1RRNkCNVSdeLr8Y_b3VoQ7gArMtSDd1L3lDNO5LX-sdQOCLnFXGyiDTqJEpIbLzuDQ-60LSEidfD-0fGUgu4bBiVd9ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpuPeOMPq3fg3AhXVUcqUn1mu2iLKRtPvJ7n7nW6H4o7VBOX5oxjOtnQyZCbRUrYWbjbMk3vdvpV4n_4GQi_ATW2s0dh5wjOplRG6KLbUhLYVfZZC9efjUnEmhftOngTbenDw4hgvjX6TOpnTwqAo0bGenBq059smvldMu33fndLa-Or38hSDRt59pnSwwiv9YU5DxOlA5lkxpuG9YP7ybL3pk8qRyzHbsDhYp2tB0-nzc_plHT5tXXo_5y1W768SHkfa7hkYhubQilCKicKD4rsNCBC3qGvrNWJtzHKRBQzXsuxXTY9dM5Q6qeHZ5LH64NPeZgGEd01IjxNsYwaWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125485" target="_blank">📅 12:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125484">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نواف سلام، نخست‌وزیر لبنان: قلب‌های ما با جنوب است و دولت شما از حق لبنان در حاکمیت و امنیت خود دست نخواهد کشید.
🔴
درود بر تمام روستاهای جنوب و به آنان می‌گویم که رنج شما، رنج همه ماست.
🔴
تا زمانی که جنوب تهدید می‌شود، ثباتی در لبنان وجود نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125484" target="_blank">📅 12:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125483">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
غریب آبادی: آژانس نمی‌تواند از ایران هزینه سیاسی ناامنی ایجادشده توسط متجاوزان را بخواهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125483" target="_blank">📅 12:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125482">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJG1MH6AVQeB3vDTmZTaWLX5xH5ZBiA2cZgbslpQKZ7OfH1TgvhU9mMJGCxlJ5eghBBYGeYWmnjkspmrAuvDxM9BSI9Yw0hg5GxGzfurvjlcjrvn1pjeFKD9DSyTfuWS9FjO1T9MGygE9rCYQkN-x4NDyE__CIr04kkBon5JiKsRbwjrTMmrdxP0A7Ys1nSYSTWnf8ScBaI0_9mPJ_Brlb62ZiD_XaMZfTE6Ejr1IBnd2RJQgnJlYwVvQFeCbm7Z5570oYsSrhEfQRz7hojCaxOiCK0ROhUGxJZ639nY86pbpawPYOcMU5HIRYJCOnFENHf6x0smGNBsbsY8QpqHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری که به تازگی در فضای مجازی منتشر شده است/دادخواست مطالبه ۴۱۴ سکه مهریه دو روز بعد از ثبت ازدواج توسط زوجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125482" target="_blank">📅 12:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125481">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asIuvXUVtRhZ80Ny1LMdfdWS7HkoaQZVIgiqnD-sL5oPRpGgnIARJoPdniLg4VnhBpwKbGngt9OoNNqyvDRUe7oOctR9uvbX1T5eWaCbmuSI1cpnSggO6muWioZSSyKlBHnXcU30bL2O4BRBYGy3LwKCfw-SB6K2TN80yMfdqurA5Mq8dr5jhflkqB2cxXEyqC3qS99tpjfTzgqC5ETuWmzGHCKKby8ZwTbzsJUr154Gmqb8Kq2tG5asSGv6tI3pL2ssYzyrNHxFr1v7gR_5uB4639sTkq53KmfZp_JvF8DG8fosgHewKdBTJQySrPv5njytkOVR-Ah4so7zVv-eDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشکل جایگزینی پهپادهای منهدم شده آمریکا در جنگ علیه ایران
🔴
ناوگان MQ-9 نیروی هوایی از 165 فروند در آغاز سال 2026 به حدود 135 فروند در حال حاضر کاهش یافته است. طبق اعلام فرمانده سنتکام، این پهپاد در جنگ اخیر علیه ایران شاکله اصلی حملات علیه ایران بوده و بیش از 4 هزار عملیات شناسایی و رزمی انجام داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125481" target="_blank">📅 12:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125480">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PML-ui516RdBYhw71cP9omzIQLuGOqIRxyhuZDwPBzeawTugXceAtjPaeV8jZFLE8sCzUdbYkYCNJfKxKPoFL5vekLdBxicXi9s-Ib2u0n8f-hZzvOaBo8TQ1CZ_xazTVEKrq0p_bzaaY5V-3RR45t6g6G8ZkY8EQGfMTDLV3k8AVubBdP-TGUTc4jpNcXh71VjCvuAirPGKYTFSBN_x_80qearAaV1AnM8_81qzXd0-AS9UTzXBX-5cag6yDnMQeYUADM0cIaWaoUOma_1TnGbN87DLwTbsvbBHtjshHJNefxPnxThw-EIS4dSL3nf5zROeyT9Gyjhw3_GkTKJNmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۳۲ هزار واحدی شاخص بورس
🔴
شاخص کل بورس با رشد ۳۲ هزار واحدی در پایان معاملات امروز به ۴ میلیون و ۳۹۱ هزار واحد رسید.
🔴
شاخص کل (هم وزن): ۱۱ هزار واحد مثبت
🔴
ارزش معاملات: ۲۰۷۵۰۰ میلیارد تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/125480" target="_blank">📅 12:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125479">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/082a0108d0.mp4?token=m1mAwVaX3VoO6qnlqttHg7lCWJBUZdQGid7hul5CiGs4wE70_y8a74ySsf_VPmexDvKhsfFSDRn8L2XyuZ2MakZwCk1RhwTEdxYhWIbGFPYLcc0vw-IXVnSJsw80DPLVeRUAH4crnqaCt90BiKKOJecaIdXLFGVdUpEdCLS5vJw3w2O8bORG1_WjwOOZoy4p_rHuq3GLbSkxLUtUYERi4aKh_vVtfota8nRkmF3HCpQcuSZQMeLWANQ42gfzDd9_qMCazfh-y4YGFHUx_c_pdncdYZWB_mdtKGMsQ4nW5Us2rF3iCfhWoAQ2haN1zZCFbgVzhICBHX05jY_HTURLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/082a0108d0.mp4?token=m1mAwVaX3VoO6qnlqttHg7lCWJBUZdQGid7hul5CiGs4wE70_y8a74ySsf_VPmexDvKhsfFSDRn8L2XyuZ2MakZwCk1RhwTEdxYhWIbGFPYLcc0vw-IXVnSJsw80DPLVeRUAH4crnqaCt90BiKKOJecaIdXLFGVdUpEdCLS5vJw3w2O8bORG1_WjwOOZoy4p_rHuq3GLbSkxLUtUYERi4aKh_vVtfota8nRkmF3HCpQcuSZQMeLWANQ42gfzDd9_qMCazfh-y4YGFHUx_c_pdncdYZWB_mdtKGMsQ4nW5Us2rF3iCfhWoAQ2haN1zZCFbgVzhICBHX05jY_HTURLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
پیش بینی های درست تاریخ
🔴
نسل 57 چون زندگیشون تامین بود و نگران آیندشون نبودن ،دنبال یکی میگشتن که بگه بعد مرگتون من بهشت براتون می‌سازم.
🤔
یه مشت حرام زاده سکان کشور رو گرفتن که به این روز افتادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125479" target="_blank">📅 12:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125478">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر خارجه ایران :
آژانس اگه روی بعضی سایت‌های هسته‌ای نظارت نداره، به‌خاطر حملات نظامیه، نه اینکه ایران همکاری نکرده باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/125478" target="_blank">📅 12:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125477">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfNt_0hlczSSyxx3lRhFxfmzFa8mZSQz6igTWrrIV6z2izIARiqNZrWxhD9dZIhAPLGBa5uuezy1OdP-ngIaPuzz1juwxpOQsc1d3qMbVBfnL6GE6l9E5uKJL6kAUq7u8lFMKZWsyi8OTSVk6vfFAc2Jvpqsds9DAw3zi3uZ0PilcIbtL4tFAYuKyZcFeJux7EwUlI4Sv8Nw4FDH-CRLRXNeilvFb1afLsiNDw9h5GlEaYlgKdAkvjdGFn8bQrzXqTccZFDuG-W0soHcnEo1ariwFCm2xV7d5rJcIH1HvSalqKmqqyWB32zdDsWQN6ySNc8EZECHRr4hh4bLOqumYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل یک سرتیپ ارتش لبنان و دیگر پرسنل را در حمله‌ای ترور در جاده خاردالی-نبطیه هدف قرار داده است.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125477" target="_blank">📅 12:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125476">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ایرنا: وزیر کشور پاکستان امروز به تهران سفر می کند/وی در قرقیزستان طی روزهای پنجشنبه و جمعه، دو بار با اسکندر مؤمنی همتای ایرانی خود دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125476" target="_blank">📅 12:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125475">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
لاوروف، وزیر خارجه روسیه: روسیه ناگزیر حقوق روس‌زبانان در اوکراین را احیا خواهد کرد.
🔴
این یک پیش‌شرط برای راه‌حلی بلندمدت است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125475" target="_blank">📅 12:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125474">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
گروسی: ایران نسبت به ما تعهداتی دارد و باید دسترسی‌های لازم برای بازرسی‌های ما را فراهم کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125474" target="_blank">📅 12:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125473">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f714df4f8.mp4?token=PfK8UXjXH2-PuSuzxEXrrOf_ZgTjue0ENdJn-4hQkEjr_bQW3XT-OB6ghBMnRcURr6-dx6Gx37oE3DSk0E9XVb87VLcwLQd91YDIrLWiD1gcHSv6mjbwJejLxAWQ0rzVRM30LH4VT4RAbb1ifnFsMYrUQO5LjENHrowZkdy9lXZD9O1TqTMycON3qqeXRllXdfgNe2uI00nNBAWmhussja5RSF6YPrDIDn8c2qm1ZF6sDARSBiEzMIVhJ9sz1Qr35JGSnF-Nc_4kge2OUhRBYCeNaiVKw8QSDewd5mZjo-qvEF3rZSsgXKpinm-WqZvcmF04g3CmQLNrFPlSOgS7wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f714df4f8.mp4?token=PfK8UXjXH2-PuSuzxEXrrOf_ZgTjue0ENdJn-4hQkEjr_bQW3XT-OB6ghBMnRcURr6-dx6Gx37oE3DSk0E9XVb87VLcwLQd91YDIrLWiD1gcHSv6mjbwJejLxAWQ0rzVRM30LH4VT4RAbb1ifnFsMYrUQO5LjENHrowZkdy9lXZD9O1TqTMycON3qqeXRllXdfgNe2uI00nNBAWmhussja5RSF6YPrDIDn8c2qm1ZF6sDARSBiEzMIVhJ9sz1Qr35JGSnF-Nc_4kge2OUhRBYCeNaiVKw8QSDewd5mZjo-qvEF3rZSsgXKpinm-WqZvcmF04g3CmQLNrFPlSOgS7wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملهِ هوایی اسرائیل به شهر
السکسیا
تو جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/125473" target="_blank">📅 12:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125472">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
زلنسکی: این جنگ باید پایان یابد. اما رهبر روسیه می‌خواهد به جنگ ادامه دهد.
🔴
شب گذشته، پهپادهای ما حدود ۱۰۰۰ کیلومتر را تا منطقه سنت پترزبورگ پیمودند و انبارهای دریایی دشمن و پایگاه کرونشتات را هدف گرفتند.
🔴
قدرت ضربتی دوربرد ما همچنین حدود ۵۰۰ کیلومتر از منطقه کراسنودار را پوشش داد و یک انبار نفت را مورد اصابت قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/125472" target="_blank">📅 12:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125469">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=DaR_YauX4xcztQW7nmatgQMtF8uyD7AVjrurq6QvPjZrh1E8uhW-7bNrZj3r_AWSHZNLvfZuzvRO3rgd70vtoNZYsQ-v1cBXwBBD67RdWpgE5sbilW70TrvTbRjwWWMsSA1X1FKzbLIZ1Wru4WCM4xUTIVZX4b_ppsnfZ7M2_UE0cf1d6J6Mk2xM8Mie4iMlmBwDryMgRozGes6Fe1ij6NHgzvoMzgvCliAx3cvPixcxMLg1G7dnS5oxlGqANOi_r2vQfecVvDak3uoHdVjVNWcl19YzpdZZqsIMmBGySJ3UU13oAvL_ez5RUuNPPFXCxzTCoFXDtqM0CpnK-h4s9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d49e89d4ab.mp4?token=DaR_YauX4xcztQW7nmatgQMtF8uyD7AVjrurq6QvPjZrh1E8uhW-7bNrZj3r_AWSHZNLvfZuzvRO3rgd70vtoNZYsQ-v1cBXwBBD67RdWpgE5sbilW70TrvTbRjwWWMsSA1X1FKzbLIZ1Wru4WCM4xUTIVZX4b_ppsnfZ7M2_UE0cf1d6J6Mk2xM8Mie4iMlmBwDryMgRozGes6Fe1ij6NHgzvoMzgvCliAx3cvPixcxMLg1G7dnS5oxlGqANOi_r2vQfecVvDak3uoHdVjVNWcl19YzpdZZqsIMmBGySJ3UU13oAvL_ez5RUuNPPFXCxzTCoFXDtqM0CpnK-h4s9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز در کشور، دانش آموزا به تأثیر قطعی معدل یازدهم توی کنکور، دست به اعتراض زدن
🔴
«خسرو پناه حیا کن، کنکوریو رها کن»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125469" target="_blank">📅 12:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125468">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYyMWk7GBJWmkJsMP-9KoC4xwEGEILAfWXIMsDNa0yPAz-sNBHLpD3KNEBTFs3HxWIatL9wlGsCeDejBwoDz-46pnROLd9fuGG5T2QyOesFO-GEmYef_tlhRgF16Kn9JuNMLd9PLr-z4KcDlI5Sipu-owu82qQz_j48VfXh0x4vB1qe4YGh0EyM1ZaQ4rzUiW9Vlx802BXpZGd9EILnYESHSwevqNkwvQ1EUQ-UAiJrmZhDbyBzJW1J2vBICLMV9krW3KJRoFFFRPdJePZCQ5Op5RIta4kZxdLRiNEF810CYaVlwAlbfCfs5XWPM-PvyyHDDlHhXxmPsqRz-67Sh6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تریتا پارسی: به بازیکنان جام جهانی ایران ویزای ورود به ایالات متحده اعطا شده است. اما آنها شب را در ایالات متحده نخواهند ماند
🔴
آنها در مکزیک مستقر خواهند شد و سپس برای هر بازی به آنجا پرواز خواهند کرد.
🔴
این بدان معناست که آنها باید در همان روز بازی از طریق اداره مهاجرت ایالات متحده از مرز عبور کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/125468" target="_blank">📅 12:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125467">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
معاون وزیر بهداشت: بخاطر قطعی اینترنت یک رتبه علمی در جهان نزول کردیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/125467" target="_blank">📅 11:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125466">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmL_qYbC4V2fNX5dsrjTYzkyPjadMR5Y_PoHVnVzBlOjb_YNeg1RU7cwbHcMIZ4eBAUlgfxM6Qu0CxU2bfkGoKMfCfW4oBNmEoAROiw-FAi0r70-ONx4ypSofrP5oi-9_zH5D7H2MMDTJovPIGqDixPE2E8PJ_nC-azfk9nFD1Na8_QJVoz4h755QvzBnILE-z16w86Sz0hLo86WdQs6IfRecmAwyB_KY0fN6FMcjWjcvtbeMyRaSVPIHWwrdku9mDw63Xf4qeaeYoo80BMRSynDPtR71LAsXRbxcA1RujA5I9KBtpCBb74W6va7VneYV3PvJ1xpQiGl1XdyO3CJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت مردم پاکستان داره قطع میشه بدلیل اعتراضات مردمی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125466" target="_blank">📅 11:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125465">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
مشاور امنیت ملی عراق تاکید کرد که ایران پیشتر اعلام کرده که عراق از محدودیت‌های عبور از تنگه هرمز مستثنی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/125465" target="_blank">📅 11:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125464">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سازمان هواپیمایی کشوری کویت:
از سرگیری ناوبری هوایی پس از تعطیلی موقت دو ساعته.
🔴
تغییر مسیر ۱۱ پرواز به منظور حفظ ایمنی مسافران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125464" target="_blank">📅 11:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125463">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
تهدید جدی تاج: آمریکا ویزای همه را ندهد، به جام جهانی نمیرویم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125463" target="_blank">📅 11:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125462">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ادعای آسوشیتدپرس به نقل از مقامات آمریکایی:درخواست ویزای برخی از اعضای تیم ملی ایران به دلیل ارائه «اطلاعات گمراه‌کننده» رد شده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125462" target="_blank">📅 11:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125461">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رویترز به نقل از وزیر انرژی آمریکا: کاهش قیمت بنزین در گروی توافق با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125461" target="_blank">📅 11:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125460">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
الجزیره: ارتش لبنان اعلام کرده است که چندین سرباز، از جمله یک افسر ارشد، در حمله‌ای اسرائیلی به یک خودروی نظامی در نزدیکی نبطیه در جنوب لبنان امروز صبح ترور شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125460" target="_blank">📅 11:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125459">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
انفجارهای کنترل‌شده در جنوب اصفهان و بهارستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/125459" target="_blank">📅 11:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125458">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwihFGsciAQu7IIe7mfKH2BJZ6q-CUxQcyRkCp5HZCIVqqsxv72aOk5Th_ttQ0NhPiEXt6cXtyCb7QFkvO9hfAvQ_uD8sR7ZwQc3DMCpDNuS13I1Mil_xJHHzMuu3E8107uYeJfC9ynf0gSpA-d_e4JgUpqEOTfQ_x1dqghAllLbqXQgAbs50123Yg0VCTne-B9_80RPBbcxp5qXPnxSbDId040s5opgG774jJ7mXzOXrePg2a-gVGtbwwzHK3GheXLfCV-CZ732Aye7nJ7srQm-ABuEUAECkI1j_cJHp1vOJ3dgaXPFS0Bm8TCqzxB8p8aH59JBWeP4Hmr3yErj3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت بورس مملکت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125458" target="_blank">📅 10:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125454">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SADz6sfRQinaeSLvSLV4Ha8y-sPv_0py5nQ4Q1qUbyBXVWkHAd0-pDC1eWTjcKpVr1y55rUneSjQUGZ-nMUysQmsFee2kvNyAbHGHCvxBrjU5HBQBxYsyijWJe12lb3lIyLi-lUsaMqHLNGe4p1X8sJCE52yMyCD9naN_CnWBbuCPEjbbdzliWPgyYJ3fuJDa_lOyYFp4H9LpcTArqiktrtUfsG4z3NTnIi1DG7soeUOpoaHX_hB_57GOV9PLuAkEKlat49cQ6oY6frinTT9zpdBxWRNTpJVIxFlpcFMEdHiHd7yeih9ZCQqsCMVjZw3pL08NLtCmqHhxDp-UVOaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSFNs3mEHy57LTlwz5_--Twdy2H8jYc6euLbe5Tc1fcsfWPhbftwaoZgSIGGoquQ4GW_AyUmhep6DG8_WTJBZdIQ0XrWkHYUMxceD_faK2bnjOcOzULaA4Npf4ZWjL7bXHbsTc3U6Y5yv2GV4xO45z5uTnsiJbk6nWqa6H7k4NE8o7oUVN81QUNCWD3MZTeDIJ_zzBee3mVzdfVfzS2kI_I9N7gk19F-68Jnwazp8yhSurE5Ep8yZvoNB_4GHPQ_9qz6g6pWVezch0WRIkE44ZUHbU04aS9mfWE8d6DN8A0PFMNVXSDmCk2DMtS5IquTbqSvS6sZmFn3LGioRHIXxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s6Z80f0J68mMdEggb5LY2MTcd6h3z7ge2NtlPZi9cJh85-RFyzUUEHob_CB-oAdSvmvGf2NR1G0-EgYcK7565lzr_CetFe-orlo0IRk-bT0zxjD2LoN-mKUNVTrmrF25HbUy8-R175J8xnh_sR743U4AgQ0hB88nlu7Pc23ychQUnT6LMhIbtFagGZGRRrX-j3vIynJ_wneb7cPMcolDNqHr6Aj5AYTOEMy_ScXkjKjsRAJYVRqTSnFHnqXxMFxg-bF4_8pr0hbQvTvm9riizjQMPr4WfSbvGX1OODmo1zH4OJV4R3BlqUjWUxaAWWUObljfKStfKqVOkJwhb3ZZ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-8sqdclMylQVVapfxRlFr4DKPW3SnE9IrCvwuSKBC6K2j8ELfwBFlkL_Gd5yzoBMLGMc2zy8Q59sFl5dMCq0nik6chdWWvJouJRqLgF4e1ZedeOdOdJfrDH2g9FIBXbvae3HpT4DBDud4z55XuOxRbqwibqsjCvXcjAkx1DvDe8Dbk6ct-c6oqz35-FSTsvqgUC2YxFZzcabS-YBXjtJBOYpFwK0b8whIIxf-Af4sqiJoUuy5Tgy1_TMz2ThlTpBCw2zHeuNPG8QsYYxi0Zvd7EsoTUcVPTnTQG1fpAGTtMhndSX5J9FCvqaA5_uFGE9G9Ous5Sa-umrWhAXjmsww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دیدار فرمانده سنتکام با مقامات ارشد بحرین، قطر، کویت و اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125454" target="_blank">📅 10:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125453">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jo9h5wNXZlT7uwsKOU-yIwKbuvVXHdNvixM06qxEzVZF7qnbUQgt1L-qMxxn95pnB4bj2rNUjBVHEOVlHrtvvLmLOcuEsYOAMVjkLf_yjETaA-HuM6hsfSifUTHBgn-8VAHQUif6HVRS3YM7UwpDP3MOmM49o9clw1OKFtIkL1yHhnQqJf5B0V6xg4Jrl5N3xv1CuE6Ed6Ine3ht2pMxZMnkW2LXygjNisGRjZ8f_UHCSNkXKhUR8R3n_0lowrj7aL72T9p0uKWVWuW1zMQNCOgeAmlCKMJL7q5yJcobxo67wd6L8eU0_MMZ8jIpxhtsIferOPW8GePKlR-jEbBcsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بحرین حملات موشکی اخیر ایران علیه بحرین و کویت را محکوم کرد و اعلام نمود که هفت موشک بالستیک که به سمت این دو کشور شلیک شده بودند، با موفقیت رهگیری شدند.
🔴
بحرین از ایران خواست تا حملات خود را متوقف کند، تنگه هرمز را باز کند، در پاکسازی مین‌های دریایی همکاری نماید و عبور ایمن کشتی‌های تجاری را تضمین کند، و هشدار داد که برای دفاع از حاکمیت و امنیت خود، تمام اقدامات لازم را انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/125453" target="_blank">📅 10:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125452">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkEeN2iF0I7GOMFHbd5G1BFnb5OrCGrc39MGfYNzQ9fe8XurrO47GhDjGB3U-DbTHnRBoppeFQTOm1EiuXeDdWjeAx1PjNOANri16V_xIOZ32XP03dTyHUP7yDxqfeNeRvVyLrXrhy2_lzE_eIwyr6jXeTXOcVQ07li5sPwMgrlHMMc0q8yu73fu1hggyiRnry7di8jmk0mXb2-ni_Gv4aRVctLL0XQPpPpibWypEFGOScBcW7EUUXyJJ5dWXv97pVUhGULZbzUUC1Vbg5BDMbJCQ8y6XIHunFwK7c2NVrtsRapM_nnJKlvrqzxU1hSdB_FOe-pE0CdcZzbZCZFOEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس اتحادیه تعاونی‌های مسافری: با ابلاغ شورای عالی ترابری قیمت بلیت اتوبوس‌های برون شهری از امروز رسما ۲۱ درصد افزایش یافت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/125452" target="_blank">📅 10:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125451">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سازمان اورژانس: روزانه ۶۰۰ تماس مزاحمت برای اورژانس داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/125451" target="_blank">📅 10:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125450">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سنتکام: ۷ موشک بالستیک ایران به سمت کویت و بحرین شلیک شد
🔴
فرماندهی مرکزی ایالات متحده (CENTCOM) اعلام کرد ایران هفت موشک بالستیک به سمت کویت و بحرین شلیک کرده است.
🔴
بر اساس ادعای سنتکام، شش موشک توسط سامانه‌های دفاعی رهگیری و منهدم شده و موشک هفتم نیز به هدف مورد نظر خود نرسیده است. سنتکام همچنین اعلام کرد هیچ آسیبی به نیروهای آمریکایی وارد نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125450" target="_blank">📅 10:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125449">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N4REkdOJr7Uk5Zyj6jmy6GCVtBv7-EUK7_qTvS0ODtwr6K1Z2fVxivoGiKvnbB3xU3qUWbNfXu5dmPjVliPalgjvXb5L1TULdrQs3NNUi7nk1x5ewHxYlVhWaUnSIswNb_fBwdoHf6pWtnoh-n5o2aZC_oqCOx-KVkQrV4uozSyeY4NZVYnw7PfKKXF0qcq9rEJLwQ-75NJ19stxbirw0NlvopVXUWyTdiBvJr5iz5QM5mlUr-6KwjmCr7F5Pmo1Wca78l5BP8Kg5XDbgrOdMBSQPxBoOxXmmtSkkrIEk-s8wkPlX4j5CXSrYBOgNiYE2EcSfWffClOpD5INM2cr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل یک سرتیپ ارتش لبنان و دیگر پرسنل را در حمله‌ای ترور در جاده خاردالی-نبطیه هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125449" target="_blank">📅 10:29 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125448">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سفر رئیس سنتکام به بحرین، قطر، کویت و اردن
🔴
در حالی که پاسخ ایران به نقض آتش‌بس توسط آمریکا ادامه دارد، رئیس سنتکام «برد کوپر» با مقامات بحرین، قطر، کویت و اردن دیدار کرد.
🔴
فرماندهی مرکزی آمریکا در غرب آسیا در بیانیه خود اشاره دقیقی به زمان این سفر نکرد.
🔴
فرماندهی مرکزی آمریکا در غرب آسیا گفت: او (فرمانده سنتکام) همچنین با اعضای نیروهای مسلح ایالات متحده که در این منطقه مستقر بودند، دیدار و از (این) نیروهای استثنایی تقدیر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125448" target="_blank">📅 10:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125447">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgJni9F25_6lfsRAEhdfpmf100xpf2i_GKNvoTKoqQxqFfzbWCUUlfoXZK_0IlRF5ZZqfKNKcizJrK4sJSePImlk0qeMCbXKrgWkRsoy-omzvs6C3iXBcJNmVjQUlRWOPKxW1gPxbbhbA1IPcVBuezFusXHPBFF6wdB4zRDclGeP7jocuFm7PKEcT04HI17S2Z0dg4M5x_9t07lqg5Yslz22x38pmat8f0E9-vbK-c7GxSqg7zzQ7oVvaX_kML0Qu-nOrtLSaj8PU0JT4GTG-dgX3sM2RUAa86kgjnaAaUI5syvMygmLD-yUyzDDkVONFHennqJICM8PY4NNx1LoFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی میفدون-زوآت در جنوب لبنان را هدف قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125447" target="_blank">📅 10:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125446">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پولیتیکو: آمریکا به دلیل کاهش ذخایر موشکی در جنگ با ایران، توافق تاماهاوک با آلمان را لغو می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125446" target="_blank">📅 10:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125445">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd9a25e0f.mov?token=qk2kD_Qy-TgdmLTHVmJS-B1lOF7iURaENFM2uPrGVthUNolqEiF_O7dXG0uDBb6HsXaZSrkk-swmJPB0ukPfmk1FmdnexF_l4V9Px9ukOPx9ORtwtWkKuMt32HJV1B26SQM-8oaiWtCbLOHi-UbSAWRe1wkhQRC9AfqnUd8Od6pKSG4mG_siJLcnhXcbJoAAgPy8V8EFCGC6C4UzNISjRvDNtKCxMmVxKRer2yP87Y8Q01Hp_kb07YaaQm9JuuS2oDuTiu3CqhI5PftohEX9_bWe5aNVTSrtXPUilbvaOKsmyTJhGZtzKpaCX-2T2WeAqOG1a04ohDwBlJrPvwgKJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd9a25e0f.mov?token=qk2kD_Qy-TgdmLTHVmJS-B1lOF7iURaENFM2uPrGVthUNolqEiF_O7dXG0uDBb6HsXaZSrkk-swmJPB0ukPfmk1FmdnexF_l4V9Px9ukOPx9ORtwtWkKuMt32HJV1B26SQM-8oaiWtCbLOHi-UbSAWRe1wkhQRC9AfqnUd8Od6pKSG4mG_siJLcnhXcbJoAAgPy8V8EFCGC6C4UzNISjRvDNtKCxMmVxKRer2yP87Y8Q01Hp_kb07YaaQm9JuuS2oDuTiu3CqhI5PftohEX9_bWe5aNVTSrtXPUilbvaOKsmyTJhGZtzKpaCX-2T2WeAqOG1a04ohDwBlJrPvwgKJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دورهمی و میتینگ تینیجرهای تهرانی برای حمایت از تیم ملی در اکباتان!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/125445" target="_blank">📅 09:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125444">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b7b5a89e.mp4?token=pVWMjzXlxICoWiOnQPI9Q5WHn4P-IWnnHc9ESbxP0GOmgApBvEmOu6tiuXFWkYlOi8xdGSvD7-5DorzVEv5UaMliv2iBUy9shS8eeWBOkStzJ3zPdjxRB-w_RDWqXMiIfl7oci5xftZcVymbHSW97VWIkS4rdIKcO4_qeVK5uNNSsJvqAX7_qrX6rRbNMiHOazLQTdbneYt74MirdU2_Z8-UutNhLeQLls412XH3_NrSK-AAKThiS1BwyAVTwPnnH4YuavahEUbSvikG7fBN18WplvYiA7a6ZTqmZyke6QUj1sqpbzWez6WIepiZ8WT_OhDTxxPOBIjY0hYicOg3Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b7b5a89e.mp4?token=pVWMjzXlxICoWiOnQPI9Q5WHn4P-IWnnHc9ESbxP0GOmgApBvEmOu6tiuXFWkYlOi8xdGSvD7-5DorzVEv5UaMliv2iBUy9shS8eeWBOkStzJ3zPdjxRB-w_RDWqXMiIfl7oci5xftZcVymbHSW97VWIkS4rdIKcO4_qeVK5uNNSsJvqAX7_qrX6rRbNMiHOazLQTdbneYt74MirdU2_Z8-UutNhLeQLls412XH3_NrSK-AAKThiS1BwyAVTwPnnH4YuavahEUbSvikG7fBN18WplvYiA7a6ZTqmZyke6QUj1sqpbzWez6WIepiZ8WT_OhDTxxPOBIjY0hYicOg3Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فلاحت پیشه: امثال ثابتی حاضرند ایران غزه شود ولی توافقی با آمریکا امضا نشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125444" target="_blank">📅 09:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125443">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
ترامپ در گفتگو با ان‌بی‌سی: رهبران ایران هنوز برای پایان دادن به جنگ جاری با ایالات متحده به توافق نرسیده‌اند زیرا آن‌ها «قوی» و «مغرور» هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125443" target="_blank">📅 09:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125442">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTMZ-tjr4mHqKn94Mhkf_pqB-XmxFEIdMG3QtSHqnkSTAEue_wVekq709OwrsUQlTT-vhQerBv5_y5K2HykwkrqoFPX6pgtfcoiR2jqr1QiCpw6U0Lh3a0BFnM7pX-9F-6Hll9Q2caBk_iW8B3moJn9HA_H_xa1mgD_7UMudggeb2WsLy65JTDO5pVZFsZUEwN2GVgLjqQy-ENBaPCLsAKsB0CWLNEMOPc6pJK30UNc9lkAo-xZ3zfyqgYZWi0hwjYcYfMB9kYVZrhNKxUC0pFhe1Y4YhqmUlDqUiaPU6J_A_dM04mFzDrL8AyKfXFNW_iYZp2LB41tNDBGNwTh_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاسمین انصاری، نماینده کنگره آمریکا: دونالد ترامپ امروز در دفتر بیضی کاخ سفید، چند بار به خواب رفت، دوباره.
🔴
به همین دلیل من خواستار اجرای متمم ۲۵ قانون اساسی شده‌ام، و ده‌ها نفر از همکارانم هم همین کار را کرده‌اند. ترامپ بیمار است و باید از سمت خود برکنار شود، این یک بحران امنیت ملی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/125442" target="_blank">📅 09:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125441">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01c119656.mp4?token=fneMqpD18MiqWVmQk3vxjnSn6cjPRGtUJhrAqBwOGxHWr8qHKVVjJ2RlhnHagQLdGytSl09kS2rsGLz8TXmb3m7oVqv4XUzT4-7WKT0rxg3GACDfMnWt_0rRo48UGJIfIeMdF92elKp1kTZW0dzKganaOHMoCubJ7qM_9mG9z1cFcGuN3SgOVZqqGxOsWu208aZpS_tkckQdfZOZopspkEAUK9bo5TEceEHgcT2PeqBN_NC9mepGA33ScQh4R_u_dHBjDhIiXLyo_cILv6nwbMJ3Rgk4j1HkQ78Uv-i0NXPEfQOdXir4O1paoIrUtJ30KL9dxHoVciSJBAx_n5lX2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01c119656.mp4?token=fneMqpD18MiqWVmQk3vxjnSn6cjPRGtUJhrAqBwOGxHWr8qHKVVjJ2RlhnHagQLdGytSl09kS2rsGLz8TXmb3m7oVqv4XUzT4-7WKT0rxg3GACDfMnWt_0rRo48UGJIfIeMdF92elKp1kTZW0dzKganaOHMoCubJ7qM_9mG9z1cFcGuN3SgOVZqqGxOsWu208aZpS_tkckQdfZOZopspkEAUK9bo5TEceEHgcT2PeqBN_NC9mepGA33ScQh4R_u_dHBjDhIiXLyo_cILv6nwbMJ3Rgk4j1HkQ78Uv-i0NXPEfQOdXir4O1paoIrUtJ30KL9dxHoVciSJBAx_n5lX2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام ویدئوهای حمله به سایت‌های رادار ساحلی‌ایران در سیریک و جزیره قشم را منتشر و اعلام کرد حملات تلافی‌جویانه ایران به بحرین و کویت رهگیری شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125441" target="_blank">📅 09:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125440">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رئیس ستاد کل ارتش اسرائیل در دیدار با رؤسای شهرک‌های شمالی اعلام کرد:‌ «ما طرح‌هایی را برای گسترش عملیات‌های نظامی‌مان در لبنان به سطح سیاسی ارائه داده‌ایم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/125440" target="_blank">📅 09:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125439">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پنتاگون سطح تهدید ضدجاسوسی اسرائیل را به بالاترین حد خود افزایش داده است، در حالی که نگرانی‌هایی وجود دارد که اطلاعات اسرائیل تلاش‌های خود را برای جمع‌آوری اطلاعات درباره بحث‌ها و تصمیم‌گیری‌های داخلی دولت ترامپ در مورد درگیری‌ها در خاورمیانه تشدید می‌کند، گزارش NBC News.
🔴
ارزیابی اخیر آژانس اطلاعات دفاعی، توانایی‌های جاسوسی انسانی و جمع‌آوری اطلاعات فنی اسرائیل را در سطح «بحرانی» ارزیابی کرده و به چندین حادثه اشاره کرده است که نگرانی‌ها را افزایش داده‌اند.
🔴
در حالی که اشتراک‌گذاری اطلاعات بین دو کشور بدون تغییر باقی مانده است، مقامات گفته‌اند که انتظار می‌رود کارکنان آمریکایی هنگام سفر به اسرائیل یا ملاقات با همتایان اسرائیلی احتیاط‌های بیشتری را رعایت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/125439" target="_blank">📅 09:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125438">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm7ahI58io0M6qHyQ3VGRNzhvkyTPVIGm6w5Egxuqmd_zZ_jUWasBnKmaCxetWm0J_eNWTu4xkje54ICmpqB9oHSCnOkL83fyw6ehFrshuQcMRKkjpgTi1pxEwT2hcTYEfbE2R_wYpR2KbUI1erxmUcB62HuQgBPptsAfq6VcRsjXg-9n3KUBQLcnH6hJyImyCtA_ePdqYo20Mir2j93EIKHdThnE6_KqG2wxqtDvWdSSjw85IUPHWMf0VxkmGepxy9JE16pNQL8EJzSJwGyt__cjmcibgauGXactJ4Qa7mUX90A4hPMDarIre20lF1UOtafBSGV0OdapkgaMghGbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیش فروش بلیت‌ قطارهای مسافری برای بازه زمانی ۱۷ تا ۳۱ خرداد، از ساعت ۸:۳۰ امروز (شنبه، ۱۶ خرداد) آغاز شد.
🔴
پیش فروش بلیت در همه محورها از ساعت ۸:۳۰ تا ۱۱ صبح روز شنبه (۱۶ خرداد ماه) از طریق سکوهای مجاز فروش اینترنتی بلیت آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125438" target="_blank">📅 09:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125437">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6TDs-u6KNOXOvA6G5zRNj2AuxfrIt4iA1S0LweOYt8cdjiNrhZSMRNbQY-3Jcqkygvc_bmLtQ6VcxyqWjTTxHQQodhh4MOKcOQ6dSwmQkRFdFvFzCpWvvrnhUCHxWkF_y4j6YjwSogblKIQaNYyWd-80LM78kOgJuEbqbrVuGwiSvMk8k0km0a05r1Bkcobs5JAlZ_MY4G2Nv39sQxIZjpW_K8rDAenWOnxxBU31M4GaWRxX5PAOYGSUC0hhBwIEf_wy1wCHiyceFgnMjA3P5FhKOeavBgDrWB8j356tk3LPmUTLJuyjyENb3gZOH-B14o77ahDzaOpnlQpl7iR2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی به رئیس‌جمهور لبنان؛لبنان را از دست دشمن واقعی خود نجات دهید
🔴
براساس اظهارات آقای عون، ظاهرا این ایران است که یک پنجم خاک لبنان را اشغال کرده، یک چهارم لبنانی‌ها را آواره کرده و کشور او را روزانه بمباران می‌کند.
🔴
اگر لبنان برای ایران ابزار چانه‌زنی بود، ما مدت ها پیش به توافق رسیده بودیم.
🔴
لبنان را از دست دشمن واقعی خود نجات دهید، آقای رئیس‌جمهور!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/125437" target="_blank">📅 09:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125436">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پوتین: روسیه هیچ سلاحی به ایران تحویل نداده و تهران نیز درخواستی برای آن نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/125436" target="_blank">📅 08:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125434">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r1eo71UA3UedGVoCDnWGYToB4F_in_YMnxIGnal3Z-kTYX7ifpGwy-4s1YQvsmj1MRj2T85_2MLvA4gnsEe3KMgxr0J2susRuNPUKAcyCxu-AbQNmIkb_tbjte5Lhv_uRCiKnfIkFNCCHEfNedZKWZV1jBBe8o_o4Q0aK9icTVxULa8nyfwBDowAYtkonr9c-UTc5SMGjloCcwSg6kxPuJieCcnM-g-JsVFTpMxqX58BN_hbhEm0xp3BfhbLroj4q-qBb41_3ptL2_3fMXSzk40TpOvVUAkPU5e9RwH76bzbqC3NY_5G37514ik01QUfOk1ScBT9aWdskc5rtBkmNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ME04UGzazT4P2i3R8G7Crwdx334Pku-LF55kYXfRjmdSjLlToxvbgwi25wT73YeyNX5nfuNWI-YxcRLIBmAfKF4LD4Zwg9A0uER4eoHIlFuDR1cAdVjVrm_sGyE6a7ylxquCXLlA6PjcQCfjHo-RS2DqVRnL4oQNJNIpaq1NDFNoF3CGvCm4PgB4La4_BF_2hUiBkMtDQa5UeAi3VdmDJkX3EbeABLW-5mkEuL6HICXlxUOORSvn6PEL1J_Y7hPgSiLCW98RFEXqwtxHeyHSQLRTj6RlLT9FpObmcplwKZB3ziRZwPsPVYNwi5sjVrgUCSE5A4rgO5M-2zWcFpFr6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کیم جونگ اون و دخترش (جانشین آیندش) در آزمایش‌های دریایی ناوشکن کانگ گون
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/125434" target="_blank">📅 08:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125433">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
شبکه ان‌بی‌سی به نقل از مقامات آمریکایی گزارش داد که نگرانی‌هایی در داخل پنتاگون نسبت به تلاش‌های اسرائیل برای نظارت بر مقامات ارشد ایالات متحده وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/125433" target="_blank">📅 08:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-125432">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
چهار مقام ارشد آمریکایی به نیویورک‌تایمز اعلام کرده‌اند که درخواست ویزای تمام ۲۶ بازیکن تیم ملی ایران برای حضور در جام جهانی ۲۰۲۶ پذیرفته شده است.
🔴
بیش از ۱۲ نفر از اعضای کادر پشتیبانی (از جمله مربیان، آنالیزورها، پزشکان و فیزیوتراپ‌ها) و همچنین مقامات فدراسیون فوتبال ایران که قرار بود تیم را همراهی کنند، ویزایشان رد شده‌ است.
🔴
مهدی تاج رئیس فدراسیون فوتبال ایران موفق به دریافت ویزا نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/125432" target="_blank">📅 08:47 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
