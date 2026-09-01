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
<img src="https://cdn1.telesco.pe/file/kgYyxjPkQQP0bZCGAF5-lFj9EW2zi5_x0LwTdpEu04BmXpbijoqgA7naC8c1ER2OP9bQWhMe6OooblGmuuedIahHOCDSj-Zni7Zd0rb8m7kvH0sV0GtvxvvqxC_S90e68yKSuFEamDpIyXXiDUC5b85nf-GrpIwX5FX5fVv6Fyv15WOZDOEgt8R8Sg3ZacwEw-tTAOlNy6J5JPCZA8yFM13qgt6ICx0Dfe0mKqK6MjCLpGPQN-Rn1xRcs8-WyfargxFBIi4IBg8yzjP-zaQ0WtWRir7ASc-iCQwHvC3eClHlWXM32449nveeadCcC0NuAX3hjVKl4BCPtig3sX8NHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 22:31:47</div>
<hr>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILpoXPRH-X9WO8XMLjtVS78JerELGUt2--LOjDCcbWyd5JJJ5eF1rdxWetaP_CgwZjK72xo_ZuYsBCCHSi65ZpNonGah-Klswcr8RHY70EVbXmRTa69r_A7n0Qqko5P0zcW1pedKh-y_kgxXiVdXwxvi1eNdUuRqECebDDEwu7apjtoi8bz9QyUFWWHlp0SHe8oS0lGnbJmI8KVWQGI5k6kQ3FhidnBGGSrjLbjI316iIBC3OC5xgZD0ZrGOCX8mNmghlntuCXkKU916XbPM0iGREnCAXP1_AJ3aNxptP3UTGOTZiefMTlS9-BEl4I_ld1eLfxIAlQHypDta6k5Czw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q8N4UnGFiNZRx1CW2q3UE5JyXj9rgdl3ZeNKHasgJJ-So5mpl6n4785pc6W7zyYzlFFH_yEF5QQgaUVGohcUZOdC0n12v_siIrE_rswWdflZG4G1nMlkvNr9xnq847X9qej-QbOXqwU5zzKFyuWJvaUxVSq6aAaTbbgvQKqy-MZ2usfvt31WgKWQF0b6ID9uh7xuYwjembZOW2Fj3h6IkpoozPOEBMPhydv9YH_QXyj2JDW1E6D7sZRu54wFg86QqzYdEyIvivp_qjdnVsOKvFB-gqFjknmqHBstZ4Thp1lmSoZeZFaLRTLdKpVWPBEp99L_OCNlZRfr7AnZfdBt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FrLlL2F04-7j-bbtmjnVcSF1V4V954guqCD23NKMXhuytipaLZ0iwPnkX-Eu6ekJC84XPN03VbQnjUR8uOb4nOl5kIMsR8mhJSh91AUESbgV3gqBY9WMUuTBwldke6Jz4Sx6tZqxLCn-_Eye7lr8Q15GhLhScpyDcSpKwTNxRTYRs6aRdgFNoeragRhX77fV3QrWUC3fe6BVoD3pM3uxHkvBFu23P_PJ0v4ZSjCyKcTLcCfQ02nhhrMDKugQMECpIOVhYMCTG6YhuwgrPbPvpUcTh99Kb5-ALZlJ0CuFlMgvwnbiN1uBwH3OjqRqhiIqMO_pxhii0akrsQ6ryHTUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/noA09UQaWifbs1DRaLtCVxwGC0e77jkegQYWoFvDtjo86SZXf3TlJYHEIR-DZ2s6nHHgDt-WKl8HDyrL42O9hbWm1ZXxUfToe64D2ryQRR_JmNZM0mywnOJ4Gi7j24bPSf9cDbL2APrlV5_IB-lXhEGiyNCnIJ2TWYvkRqTRserPpyFEBJ5fx91tRGvN1rBEvxrUCyDSyrKTyRkzjRFpPkQUcg6fW0UNmFVYBzdFQPdH55rGrQBC2h391TpZV1kcfP2vUpD-3_iYdzPZsNyKJyiWNBQQER1ECkpS5nsFvoipOqrxW8yvZzuvfsB6XF-M8xGRoC4UZe6lIflwEgGwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VcCV47Z0awGeyVT26gch3T_-rE9qBnmJ7tMgl8W2P66_GPPUiM0F2LVf_iLrK7AYdP1f3KaGQH9_SZbNbtQY-cgS9Ce-3PJ8YUvbVnZz2C5wlx80OwNmRG_Pk1WWXOJHIEAUblAK0eg1WQ2W_1z2m2JrKKqNJ3fxOQE3RaBEDQZK1zibPpwFskg2q5ll1i-Bj0BOOkfHM7tEQffqIFml1EOOIepr5iuvvbA2yGbUC1nBqGnh1lclgcn1flv2WuGTKwQlr4HOy2vkKLTrYGlZdPEMSXj9ElappPmtwhD-sF13wc-AV6WT7eO2rOR1CNcj2zMcD-2Cj-ibfKAWia8RkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UzFgMFjadFeQIo53w9PvV8Paup-UohVlDC0VIxiStjgZA-Y9bAZSAhKhAILEmI-Ym9R3csCjWuvi-oZZCgxxLlnwIisYl8kwmA0ZEl2atiVYFqgRelPurn6mjHnqfRP-IqTFEbzrxHf6Xli2Bxq07EUayTqa4Ea_9hfGD63CReNwLAmT2JHGjQvyHl7L0az4fhI9stCD9oNpws_BDc3aYYRt5TZI03m3LwzpEEdA-TUN8oEMqLqavYKrtFuwi6C0_JHCPZ6DqG_Nm9pjzavEbnVUEquoGEjoBxHHi1UYG8TAZ9vSwUxh5uZ2HjBYcdHmwQiUKmsZyWBtAMamknQUbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ErOBalGPMnjQe_V9DZTOwA3U6IeyBoHcq-gze09E0y4qTKzPo_YPE8EzLDfRJ_JmBbivQfC_-mNhQXu4ztjDGGKsjtXFPJYslLnLr3cNHFVmAGR_fuVc4cX4nKM9_VXtj8Ovd0mzVGJPKm6b7KJpu6IdcHUbG_O9t3Jc1WbDvGoBU3Qb0EpPMlvsw5iGcM-mTDdmjohDoom3gNKQkCxZN988g5gpfcXcw1MsuGrPY_HeJymO82szk2enX-POHwDhCKY_pvonPl0kPY38hn8oRdaPXqwnfubyDSKcR9dGAZE2D_zAWsiq-CGA3a3bFptqReehMYMTZGVel7BRfeg9sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QijLqPLgtLj30gO46WDXDnhGAHeIJmYPJ-92mGqdxAr2m0p2L8ISUGgOlLRz7DB0WXoQuHRA0pSR4xjXn6s37Td3v4EYkgQ9eod_W4Uk6BNqgY30lUGoOXt0XlTt_Liy50-6pZBscB8M5oqB3OP31dqrh1YaefA8aL4RHg_QA6oS09Q-Am0oM9QhCJg5is8yKm2aIp6-5EdDDS2aIl5EHD3KZHTQXWvmBwornYweLk9yEUWdJzbFxWDubytEUhoe3q6oO_rf-tASApa335Pu-uQMGIDp4TwbUzgjG8-rD1tplyAZe_uVnk3vyD4XwgNDOoYo1lgAgjO0h_Ig2BEVpA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dF7WRtpKH2ys9-dKrU4CA1X5kwTHDoOKl7xzZYBXgeic50cBK-mE0mraKYk_ZfQ5EwWDsuO1fhCb08al9qUdubbM_sKio3b3BAzmMTcMoAQy0P7utTTqGsJ3PZXO_F6-MgYbZ1Ynfs9qSzPBsQVogMF9JTC656hM6CrJbJYaTioyxvtAXCtMfckCQhQWq6ip5zW54dobOe4g5lnBmuZucKeJ32nc8FeP1rTfMsSn6qkebJXRxnkdclrCw_q26eq57rL6kRcaFKl0613-DaZescvj1oWPzS5gSyyfEuGKzJm631W78ZTm0WTq3LWxVVFse0x6eNPz4RNpPrL9j6lAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6M_t1BwyahsM4n1BBAZh8gJlk_O86g06JjvzEiWrPX3XtNBh0JTeh0wRm5shn5qxcSQc5iRkA3pP8yEkFi172c4rYQv5UQIOnfCpmLDVC02ZhIe1hnaArMjxgc3qXtoyYAWsTSSR4XRGowAzBWxA2KGfxPDqXNpeVb8SCrnvPfYlOOhmidYLW-pMvmjhP-0z3xrPJcHBU0hnJxFGkVCYGAeZdspVv08Kb30PPd9xcKUy1ry-NmwfUTe6B4v-mUwsZxCAQnbGyq7zb24-rpq25BrtfyggFzmHsfDl3FdvkV0dRCDL3LpdC7vel4GvcfEqQmr3Qz9h3JsvcxWA-9dpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGL5qn7MQLo7THDqS0HY-4DTU5WHfNlwKoxdcq7FRxXt6E8r1sCzoRFA0mLdMKNfKdzzVYn6RPpRf-IDWtOSXhEK0p_3ZhSaDNvaoi335OoBrQGB7BzZ0a_6oyGEuWJRLD-jkd4wtcfJYnVNraKF9RsH7P6X-W6D0lmpK3Cpg_DLEz5-GtSvwD8Gc25353plqafUYMcamQsQ7IondNIPRAppdE0nud8fPfCP9uONkJVcwVabVEXF03IGElkW9YaSm7rMyZvGXySw3TKs03KUHYo7zfJfcadqe9mNyBLv0X6o8qKBPUzNlD8rSbFg41pJVERp7zqqQwTw6Yb-yTCpPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ve17BTE-Vwp3wkfU0xn8vO2Rz_6P7yNtdD1uixG0UXDe3E-016W9TSC9yrO7wDTnzsYLsURPfTpVUgpNiLoWFFIobWvM1zynolIQeq6r12U0sdXIo_p6TqhHhSrmuykxhdDo83ZSfIXrxPGSoLZBf4VRKek9Oi8Gbz2EOHhiCcEubn1-qkQY3M8loS7a_n0hGNpLBetzVfVA2WzStPoMUlrmiL_BeaPM0O1BoVsmWVDfV0Mo6AD9TTYJKZY0fT7HHI8ZnUELK64z_zlqTujHPLO6giHJ5RGcnOLpcJFvTBCysO3n0OTxpOs5EepkbR1Ap8yMJ5fLL-idgof9beq9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mT5b_2Zrz1yW6tv4QOOYwbbf32lnuRDsfQyLvJyLd27HNSYH_BtHY17c5J4T-HKhvDrQNqKxa9k9nVKfIhW7N1mifqe6bvEm42nzcPYbZ_G085gHx9nwS742RypxVJkcyeWOV_mEeKgs9ABmXph2HNzWmSI4Hew4yfbykQMuJp9TG_ol-tTrJERAi7NySsVELcU5sBDEi6uce-wEvc3-u8ryoAE6OF0pm5N_SCN1mLA4zfbj8XcnUoZhRqxtgsIsvKVPToNAlKk69eIsTXxrsfEr-xRnJfV-67ywtlnAvwIt3x0huYi40rqb8_rAsKnAYim5OMtpJyLw4RsWZ8itBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hdmP-oAzFLo1LpL1h_TWKIt8IoPBFc-ORJdkaV8rJTu06TpkFeCmMTjTJtcX15I8HLoqgAg7KoSZe0Mu09RxvYl0lVQpXEtEu9vrXZyLrQk6YIoYzRD1-Pmzf2St437zMEiXzyFzpPgWXQkxk2AXRSuCjUsvhx4PELP9f46u9fBtveVv2eYwhGFnvkAeVQxmGheo0of-pFUijPS2rVMP_QS35tzCXXceXTGAGwuVGhEMwR6XCujb_ZzQijgGnlSXTZkJnIiaiAdiLKw0fIYxLZOqG8RKnshT2GCBr8dAn03UaHqx30D2idXVceQRjbh_EiB9JEhQZpA3h8Awyd3fTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ru-F9Cvow6RO1iWBwf-N_iuRZ3WuhWoUabf_ChWsv_PysCKN1q0jgoIiaIkvZiAEUQvvc0sFtgfIlyf0uk--7VIlWNaUG6dmZfYyFo0q1BIT0hiTPAiVEvmKpHEtKoo6EbCO00bjEPicwp7XdlqZsQXuxMXpxhDClZgkqHaHY5RLI-1avAvAmDSHG6gUQcoVTbwuWo2EBnjY-57Y7V_MPHA5Cv1HIiNzdwTQmW6ONnk859Xj78Ct6hs_M5Nctz1vmK9DRuTet63PjL1Fu989U5n03w6y2O9LyLfaFCz_MMeG-rmQCsbBgtKgXtkNQmNA3cUnnT9AXG9i0O7_crdOpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MmDBWCHsOzf0StG7hDmUkGmLJZJwEbnYVzk6RTvhlDecBxYBJH3bs9bmdFfJaZ92Vj0mec1HQMEbH_ENP-T8akrYevsm_dHXw6eOM1qaSP311ZF4r-XpOyFFMqWEW-ZraYx7Q4Le_-ApluNJZeEW9M55uY4bqojj7ZvM8TTfNX5vE0Q37Po6Yu2O0eZz5Gew1BFKAwL76HqHXfXQ3dlx3A_nNtExoMNCrlg5u2s8cqyCrcliPZcLN7K0TAIs32k54M9LRV13NhbEfQpQzb0dwFqIR0ICefK120Ox26exwyoLa1FVaXg5BQXhVKKZd0ncbUM2gbF6M9NdgFWDsQwR-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a62j1_HAwwVqhoxKZByfg_S2zWSd45fHaVXW48x3Rfs36sCTJ1UgcrHSgyf9GdXrmyg1XK16lf2eaKEBfi942cVn5rLgxzzF4eV41HN2aCZ_dp4StmfrV_G2FxTC77fhCGeYrvfGq8KBZ95UnknrRAb3BgTthIhWF6szzjg_g8Lw06zVdjgtZvOYAYk7K4SDkzOOcESlgG9gsHgSKAEmgL1kNwix1uN5XSxK8x4SqE8PFGGabAnia3giUnG1Gj8KslHeYcItOkJ0_4yhYu5LDJpE5lLBT8EuCvubnZ6feI_BmKiCrvnYIGe2hWh5yci2d5eF-y1VgfHtlZGYJ91pjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sM2uIdish4d9s24_onxobN4tQ-hn6Twnksct_0sAlBqztDwXsVatNaFm_rl2CbldchLX0ivE1TrWlBUC2Fa0H5iLsKPXeBJAk4UpqIohV7dVkaAQIBq-sv6M49EEm0tn-OFWqD_yHWjrF75c40JHR1p1O6u9sYbpZSoRkeW70U6Mv6BJbLkR4Gmk4Su4Ojb5n0xo7kV0hxWuvVRJ6JTR6c0lEf0KVuvPL0zSQzYAat80fPSQaqv-PSKR8bQ5uX5OoFbqPZK4Z22kcC1zMsQvY2hGvZKl8io-A7ybGVaiLZCmTZN0qEfgYT7uSDrTtf91ApoOUv98dcom7E5kE6Ci8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q7WdU92sk6IE-1OCJJ0ygOaHqcsTErxTaI8MWzZhsaVsblzZ187nJKap3n0HRqIoqy2bWwHA-_stc0XElcVXozvwxbIjZx-tbGQTI7nybwJAvwAStnOVpaEyPyEBidsRFsghlHfdmfTL8Hjq38VZ4yLJffKwXZzpUtSWd2ss3DPJF6esJoxBSxyCabsdiBwn7FHYUPHWpn9aU0bXTE61dil6Ja64cILN3GSuX9G6iEM3_f5IqQ9w4NRKJAmbLxnVzxA7Jcy13JJugjNtBJqrEVyIwsNLfWLmlf6W2WJWc6WFtxZyV_yn3QFFe_wbNsspdh7c1XYArCJiEmmfGimE-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eyUGjsmEnF3eIXM71JJh--V-pQjYGnXrweuc0b3AV46I_TnuM0qN7XiHzLzhzJxvUe8ROZtdha-zI1Up-z2yYmW7OsewLPTzJW0kIn8x1m8WT00LAAFnaMLx_O6_l9soUoRIhxhFBupKqt6XQ3GaZ_ggQb7RdKdbTuH7JBy4RtNFddK9pQdyXo_UY7YCNZwTu1OOWpStyxAQ-EBPxTo1PCovyMuNRYERI9loxxe9mLMXYIvgZl5Hi_xUh9I7zuiGpR9DrNt_aCc0XLu4IsMzmmyj-BcK-1_0xFxIpRd4OB0VdbtQqV1h_kXGdwPvW_QUsTLf0SlJcMp88Qx3rlaPdw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BbGrOusRF4U_RmnnBhOHa07FdHEbJLO1u3uw2-aT9882ZyMXKq9155wdrFejazk3kr7KfNV4-dgsFfzUUFYpt63K9xNurHsrFotpFgzajVqtsu-IgyGJqkyMruJleSkZ4ySdmZ7dogj6nY4h4n8rioGmVNPTmK1jTG0zl07Eav24jA2vbLaaIno48vqDjJsH-PEQ69MTSfi2EbG-rEi6HLaxL-s-kQ-oTxxwfJvt23UiqabSKD-Plizf0DRTLO5wpLh7kYUwgdPIvf-ctjDnk1gyNAurgZfJ6YDkZOqdvpSYWlrdRuEYlImOlg02lKUKrGihp5PV6hVdvlS8eGWXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DNhShDyZvcCbBRRT6gsHc-1zVCypYzjw543KSkI_qRZzcWVsknr69IKswT0kCLXna3b9TV0_c-VMzlWbKsi17gxmmmDmAWMHR7-ixeFsvQnzYkeJWGliX1s7YTokHhHRqaLr97BNFjBeBjH64EJU1QK_-AFb2hrbgGqzV59iEa1eX2Iujc4gN9OpFEkY5UWdR9yMKgjFihrP_z9FzzJ_TKSY-Wzai4ILoVtDSqyW5N7g71g8AKiTA4u3K0HmzvipV4T2LG9EAxqTjHKGC_PfXp3nzwIkpHnbwn25BNNW64KcXebAWIgEjxDHc-5XdGNnllV1Mi2qoALc1P0PbuSCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iPoVnfIbjrUg-HvC22-TNIExX7xk81TQtL07sBfOuVLf5B-QEO2hPRenYh_nLiAshJKZRCrC9dXX3JmaWTmEyHvJBH-GQJklpk_fw1ZTZBYkJXgMkLPdWA749hu7YddyA_94G1_sq95MDXLEpo8cdh3k3KxNwIfHKgJ5IB-bO_CM6HJUOmgQ9-ddjYpk9oH2J9_pM2hfZm9ER_wGNbhNAP9UJox_9PjI1Oq6vit3b7EU0yeB_X-QlGBUq12FjUhpdhQ001pnIYIfFHvAH9k8uQgmShgX-E3uvOCb_mf5z0SzloOh9lewk8XoeAwrT3uYI4Qnw4erMBCzQFhNcYHyrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FSDc21zv-kFSLQKsDFD7Z0tlVJtvR_LaQYTSlLueOTH9rzpLzv-AcSXrGURtYnk9hcKbX3bqMzEFf-TN02LaEfgV09jUrP3miut-EYcLc1afLwJFpjigiSenqYBqvliuP6jo_QgnGcyH02_yCSeBb_b6GcUhxwaKoCLNt4uNYfta5WW3gyCSQ8DNItzOvxp5tgHm_NqVx8aCX7Nfiy_D_GEp0rCBGsNGlVOVUYF-r42NQKgfYshaXcgIRf2IBsgJOdXeuZTqbChKBHgNu6b_OO6ABVx01-3uon714jJx-IqOgNf-IPOMAIIyq6LFEdR4m0PgsZa4hNJcm0d_HFAQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sku9yRw4XksuMEwOi9uujTpgJwy_PQ5QWPmDVZj7C0lC2fz29bN79g7-Cc3IKuF-3NzAceoRvYhxnvz8lvSd6HIFdlGBwfqlPFqL8Gplyg8F1l5M8K5dYx4ijgTJC4MSe9SzecllzrRkk5nGXaeKrgrszI1lWA20QUjKaoVWB8S3bH8NXptPnN0FvDLJXkiM4EV6Ez1D0sRqjevqoEWCdxVmtF2cqwA_R9jd986omKjo7yJfaOGzRslYZXPXR7eAf5_Wk_Lh7R6xHbX3RYPoB4y67rXh6phLo5dXvLUVPDrITgbA70z9BxwZrWoz5hkGt7me8bIMWbIcMe4ubEgr3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C_UWozCNeNrVf57Dzt7Mh3V-CLECZiOECk1e1Tmis9hKbPkIqtfMvrHcS9kwoT_2VGetsxaQFLUhrNaa_O4MA_DamElMjh7doevaQLxXPJqC4QUMkmV_LVv8FWQIrOUZGT2RgyAQ4GfAjz4DpWK2kLiRWk7wygo-nAKSO9aQINkcwuKjyF4TcwEPGTYjLz_UOubyGxaVlTSBui_K4eX7xfQdZI0CAa-yXuEE_C1pyXNtQZ5eDMdPFJmqwimK1bYFSqkWCxHI0AdGv2yEOf3A02cObEoxp5AB8GVyKmz-wlmQtuVFFph3b3jqM4w7b_dG_mi5XvQn59Sa4BXEVDpAFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ببینید من خیلی از نکات رو نمی‌تونستم توی ویدئو بگم به خاطر قوانین یوتوب. اما برای اینکه پرداخت موفق داشته باشید چندتا نکته هست که باید لحاظ کنید:
1- برای خیلی از جاها می‌تونید به راحتی از Google Pay استفاده کنید. یعنی میرید توی
https://pay.google.com
، کارت رو ثبت میکنید و تمام. اما نکته خیلی مهم: برای اتصال کارتتون به Google pay، بهتره که با آیپی آمریکا وارد بشید که با همون روشی که توی ویدئو گفتم من تونستم وارد بشم. اگر کانفیگ‌ها واستون پینگ نداد، کافیه که Chain کنید با یه دونه BPBای چیزی.
2- تمام چیزهایی که روی گوشیتون از گوگل پلی دانلود می‌کنید، می‌تونید این کارت رو بهش وصل کنید و خرید کنید. حواستون صرفا به اون آیپی آمریکا باشه
سؤال1: اگه یهو بدون آیپی امریکا رفتم بن میشم؟
جواب1: نه بابا. من دویست بار با آیپی آلمان و حتی ایران رفتم. صرفا ارور ممکنه بده یه وقتایی که ارور کانکشن میده و ایپی آمریکا که میزنید تازه درست میشه
سؤال2: آدرس و اینها که ازم می‌خواد و کد پستی و... رو چی بزنم؟
جواب2: خیلی راحت سرچ کنید Fake America Address و اطلاعات فیک وارد کنید اما سعی کنید همه جا همون رو وارد کنید. حتی یه جا از من کد مالیاتی و اینا خواست من الکی یه کد 8-9 رقمی زدم و گیر نداد دیگه.
سؤال3: کجاها نمیتونم پرداخت کنم؟
جواب3: ببینید یه سری سایت‌ها احراز هویت با Passport و... میخوان. مثل اکثر سایت‌هایی که کریپتو میفروشن با Debit card و اینها. فقط توی اونها من نتونستم پرداخت کنم. تا الان هرچیزی که خواستم رو گرفتم. که اکثرش هم توی همون گوگل پلی بوده</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/niABclIrrsedy4KX_Kjkic6Ei65NdkiGZT8kNlFY0DMKbduhjV8ex4K2j6knt2vFcNfSzPuVT4oqEncNchAM7it-W-4J1fIJLawNNu0jFygVCEmbjV94w36TgxDNyDRUvti_yIk8vA3wbVz6RFV-_RExcizAsNPLN2zTteyUpmIoWrsEQCHrpi0GxRKA7K2y0RGR0PJPwphJ-CDdq8pTsYJxE6rsw3HnxSoDAA44aInOHfOcwfXdaGQA-Xy72NRq3zgb5DGHS5Q6It4vQeQ_fXKUY2QyFqhfohGpQ1JNfbDedJ27auS-AusC2qc3sOuXd7Vtn3UgOxQt3K-o2nzopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت:
https://app.mpay.cards?startapp=ref_S4FPMh
ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر:
https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت برای گوگل پی و اینها:
https://t.me/MatinSenPaii/5092
⭐️
توی این ویدئو:
1- بهتون یاد میدم که چه شکلی می‌تونید توی اکثر سرویس‌های خارجی دنیا پرداخت دلاری داشته باشید که وصله به ایمیل خودتون با اسم خودتون
2- با کریپتو حسابتون رو شارژ کنید و از هرجایی خواستید خرید کنید
3- حتی بدون شارژ، کلی آفر رایگان بگیرید
4- و یه صرافی با کارمزد پایین معرفی می‌کنم که می‌تونید به راحتی ازش خرید کنید
5- سرور رایگان V2ray آمریکا بگیرید و ازش استفاده کنید برای پرداخت‌ها
6- اشتراک Command Code رو هم با همدیگه با همین کارت میخریم توی ویدئو
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bUpdo6qs_OQXwAgz378E81kGVpxwz1d0C4OKi_hln9WiY8aQ7NS3lg-rzp1eX5WfCC65bf-qslIg3k8HNdnaPL-lREJMkhe3HBoYyckpHYJvJ7Z4YZ-R1rm5ZQ5Oipb7qbVYo4uJPHlF3-riH3y8E2JY6FhjaWWK7tgec10nXm6lbtOBCAuS-1DPKbSFZUdKBETt-Sk4jQVkHPpofmU0h1pXpL2qSyDe2EGrWHcFBOAFzu69O8i7DsNI6DjRRPe_Yex7M1LL4kB8o-9zZt6qEpJA9yRH2ZV4Kf_APRrtC3xej0Qiy4gT1JL8IDfcvTLzWsjOKOliaM_LjZ5m5Kezrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=uhH96bSKMD1iyXO33PzbDd_f45AcIiw6Fbum33_5Ph7T5-tm9gWO1L7dW6SQ7aVmxQXVjHf0UXrwbhPz_Rpv2dxhfQMh2qp2YzKS8A7UHtZxVmkJGu8hf2nuEanOZ70TQwyKOriYDzcrscdG6iAtQZpIpDgjbUGAs__ImFPNUjT6KeYHMIzxq_P48URNJZHmCx8LjZMrFhqT46zqGhkDi_Fs9L9Rt2QU1BHm1RQfnAxBT57Gyelfk0MIBNBIQlP4UqEhrNkBWJl8lpCnm3gEcpNJKn6VZNYWiA__sz-4IatmqUnGpqEn2BAPNlOAcO5tz5qSxgbhoemjg1RHPY3Rqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=uhH96bSKMD1iyXO33PzbDd_f45AcIiw6Fbum33_5Ph7T5-tm9gWO1L7dW6SQ7aVmxQXVjHf0UXrwbhPz_Rpv2dxhfQMh2qp2YzKS8A7UHtZxVmkJGu8hf2nuEanOZ70TQwyKOriYDzcrscdG6iAtQZpIpDgjbUGAs__ImFPNUjT6KeYHMIzxq_P48URNJZHmCx8LjZMrFhqT46zqGhkDi_Fs9L9Rt2QU1BHm1RQfnAxBT57Gyelfk0MIBNBIQlP4UqEhrNkBWJl8lpCnm3gEcpNJKn6VZNYWiA__sz-4IatmqUnGpqEn2BAPNlOAcO5tz5qSxgbhoemjg1RHPY3Rqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0  مشخصات کلیدی:  1-مقدار ۷۷۰B پارامتر کل ولی فقط ۴۹B برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر…</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/av_CfJODgWvRycIog73jtnaHymipqEHMD4fttwDWgC77ivIIFUMxXw-6rjRaUGsmN_189pR__rrutzDkQ9WCuUF4mQmsoGwwL9UOmK7fo3aHXtuuUM4CYFIurM98FN6BfktpAWCfrBaQEKkcHqUAD4WmBtleSCNFOse4qhzoO4QXhYAV3kEywVWm8Y38_u2CjJdK_pIA_f0r1m8URB1blDVjTGLGQecB-rxUJ-wKeBeu2zb4LkS6c61KMII7lKqAm-O39Kiktc99p0nHmM0WuJYSHUKHnfMTHby5gYwNxL0uGuavj9RkgucfJhnrr2UXsh5Q0hCf80GTIcpE0qI8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/CdXFkjtEdHRyowAMMBayZLxdbMzfz123aUQydlPhWFOpE7btBj5Euuaqe7OB4JK-OdpcpO3SIbpeeWU1AqVNtFIETGJpjn4fb529IOk7GVQSYC1gXsNx4S83ejNNy6Cr5zyXl4RIV3ytduLXM-q5gSDZatczvJ4j8M7QCmGE92_LZIPbs-jiY3fsZsYYBH00g-3p-BZ0thzQY-NUFKu7TJieXD1kjQq_i8LKG0aQznHiBwDwrpB2gbE8x7syil3j1jjJfg0R-1XB-0eIZY2DAMfNIq1v_HW5rdxjjEvEX5Kv2_IoK2zcHEnBy0yXUZ3GYMvZB4mSkrfQlccdzgQPaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/rFV08qsPQftrTOIn-Z-KWosQ-lo_dQITijNssktx7Pgr75l0COR1tyqgURod6Si8DvAW4VE6vE_DQRsyLGMTgAZFVmrzBWg7_WhETEdv1_dUNRDC_60TpLdS-97D2dCWAMBz9uev0OA5Bu8O7AV6GxvH_0zJIU_zyRsNzYAsy_Wu7glrgcFQxcFqbl8X36v5hC6OMms60fGm5xZ9KEdmvtSxElyOhWgwwXBnbJY5rJymGzZLoMDbhOgSsD4-gFYmgz5olrw5Fb-tq-D26e6-kWrBqqRlceVW_KGtH6tXX24__TdaXuCzUBro2RU-RXlP7aTpS9fO4leewvweo7Ecuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n_vblasbSU3Pqv6aQk4k9LOctKqVi44ffaJk-nfjCuukitLfRUzSc-qy-wus16b_SOCe8gPVPqzDB0uyNQ4to9d0Wki_7PjYO99nb4dMGliZNnPMi0C1SIGFob5O8YKYOZ8rV_yHTHtzSyp5HaS_JdSKMAmi7FJDCXDp6v5yuRXMQ4XS1wl5fW3KEO9M7EO_FB4PqZ5wyekDHArOsTHx3mlzm1Mu0YAy45N5nd-Cc2dRA0mnNdNgTNYCEug16P9l6_BrOt4Mqk8ID-WxFx2LJFgZVge-Stqshea3Ea5pD5azGodvFC9eDldMVVcUraC7R5fcV2FdsRsgHEystFm11A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uJHqVRbDdj9qTzJcSVYLTC2aANggfqeDDcnetKFuxaOPl2Ja6N5UXQ81ybu0dfsyQPCcugSx0XqC266BRWOFAvglOhneo5eRvnpveRgkGKzaE6BWZinfAnqaeA1JA5DTbY7uoH2R2wAVpJOOqlTpRvqGZPl5rzBwDkbvRYVh-ltjDbZ2kc5X9dBzRvuzdJmqiN6_ACfUp7CnJT8u8nuliPCAWKZt77ZCjuBELtWdilxXWgOmnYJUmpuBF2HSc--KrqA6R04dQRh-riUArDudhpWQrcRak_8oJuCECdN8YqjukQjowJqyxKQDd6vgz4JsK9DS2IViOz-dPBG2MTu_JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dlr8pw66uBw1z6jldCDiLti07H9nhYQ6Un9NMuYWu46cZUco4he7o9YSJ422qiEnxnld4mEq_WASdjAiBv9xCylX04UuDlslmYXGGIRZaLIRHemxqhqCkFrNqDeDtomD_fyCbcU56mzXW3-2CcQ5-jeMppPSzieGJ7lECHAHBzLu4fefi_R9Cuv6ew9TUfJiv5wutRLngcSR13B6pYIwQNt0mUqYIC-txt7H4sCNTCrf5mEL5VjAYIauw7rA6zR3cDEnf_NDmeHBqYR9UQ2IHIpWLh7soypxdR9lLyBWmlTWhQ3yP9m4eYQ0uBXYVl8GxgRGYFtVSaxjxLYQT3g4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V4wiauO0DLLiaRUyvJ8Qg8SGtriz2IJEVTUUjkvbvsC1_y8fsLb3lR3UNehC6w2pzy86YbFMS5qomBpkVu-1r5dHLU8Lbk_U7WXt-CsX1pdmLeP0l1MsGlFQ3geqy0Ts17LyhK5E3-Rj2tGsnjXpqR_K6jM0CmIzWHsC-7_VRweRRJZThYdeVISIyOTOj-OhwRFjhjFQZATVhHFDvIFpWES6Ou08-bAYHgVDi2ewNiIgXqvsYQZobPik-M766pHkpP3atWXxIIKpBoPTE6gkZT1As7xzHIhagvdoKNiOEsFbfomGqAm5WphjaRcB9mxw8k-fnn7eccD3lFcsMhB4DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0
مشخصات کلیدی:
1-مقدار
۷۷۰B پارامتر کل
ولی فقط
۴۹B
برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر
2- روی بنچمارک
DeepSWE
از ۲۸ (Hy3) رفته روی
۶۴.۳
— تقریباً دو برابر
3- بنچمارک
Terminal-Bench 2.1
: نمره
۸۵.۴
— هم‌تراز GLM-5.3 و Claude Opus
4- بنچمارک
Code Arena WebDev
: رتبه
#5
با ۱۶۳۳ امتیاز — بین مدل‌های متن‌باز
#3
5- ارزیابی داخلی با
۱۶۳ متخصص
: Hy4 با
۲.۹۹/۴
بالاتر از Kimi K3 و GLM-5.3
قیمت API (خیلی رقابتی):
- Input:
$0.83
به ازای هر ۱ میلیون توکن
- Output:
$2.50
- Cached input:
$0.04
اما هنوز، رقابت رو به GLM 5.3 Flash باخته به نظرم</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mzd9rXgl7IscFyXmzuta7-vma28n8bUIGFuMebXCJCA_pMaf5yVMToCIepOLzgZVa0di5UHsVcHWroEQijyq8TMOUZBG7F-cz1Cwm8Znu3Ab6c_2HvCQI5tSjBPU4B2dWep9Dhbaa0OLnM_0LwCs7B_wu8rFpQHmAPSuYdr9_-G_5OGnr4gGsB4bzNZYnWALO_dRBPKaofdWv1j4Ybt56FfAb9C8HOGT2d3juyGduK4tA7qEslOorLHqJG-gq_EkxfXuCrDb4Auu34jSkOiravKdlaEtimaL7OuaWsUGxyUSKbzT1MQGbgPcef3QKzcEDcvMCP1q5otsNZ1Hi9BEfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qqqLxc8JeMy24syB0GU6Pn_bEEaXpLZwEH38cf-D0uclSs0yK8xnjcm_OuPjSGlBHvQETQsUMrE-qxjMpRsg9EZVYTPhpzR_9x4z4emPJ5kxScDK9na5-OkW4C7JwGCgaOPqfysVIelLxJ_6D0iZ_EfLKypc-uScpsu50ah-s8KJYAOwh9WHPE0dJ1ZuSEXukHmPUiXQnPCrv_EPxaKlxllG6i7kdzkn2Iny36aaQWjvYr13ZM74WW7CQF5Q8bTTSia57M2NiqIr143gHfaMum3LikYZjWdbZoOsQ2DKiKVoYGhHbcB3gewebWG-hKIEIe4LDSzx3ScKq9CrwcD9xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=ZuLDCwlcFmTqbj4vM6veDSG24wgtoKeJqKf8jPlo5P34CRMDzYyCMbFO9rluP3-lWu2yFczuQLxD6H_Z7lndJC8WmcoAgGiqDxvJ2g_Ma3yVdKE1WNrwyGsZFamfUKJ_XYdpKuvzIJo21JQnUKPxUxHeMjIGh9FIDluwRifaJWlCY1FFJ-HqDf_pFU_9GBSGxfuXU1-_E3jitMgX_rlOnsBQn3jo0N2WoIsviS0FFgzKmLElFd406d7p1tokPnXlVqeFP46XaRyq-RUdLk7bixXwOuyM6B_b8aXHTFigBBaZtKyYhwk2hX29eXn4O4YODJvMSbfyvamvny5wPRaP5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=ZuLDCwlcFmTqbj4vM6veDSG24wgtoKeJqKf8jPlo5P34CRMDzYyCMbFO9rluP3-lWu2yFczuQLxD6H_Z7lndJC8WmcoAgGiqDxvJ2g_Ma3yVdKE1WNrwyGsZFamfUKJ_XYdpKuvzIJo21JQnUKPxUxHeMjIGh9FIDluwRifaJWlCY1FFJ-HqDf_pFU_9GBSGxfuXU1-_E3jitMgX_rlOnsBQn3jo0N2WoIsviS0FFgzKmLElFd406d7p1tokPnXlVqeFP46XaRyq-RUdLk7bixXwOuyM6B_b8aXHTFigBBaZtKyYhwk2hX29eXn4O4YODJvMSbfyvamvny5wPRaP5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HsdaCs9UU90xFx15oODZE11IkheGylzobES6Cx6xFRJCzb0aCMjzWRYysnwRtoJYOL0XZeV0MGaE0atMXCHtBEJvSuDHNWNNEES-WTkLJrIC_MzmK0ZyHCS-adiCLc6ayJXbbdJJgUy4g0FPNPBKkEJjCQxB_teF0XRyi7jHEaaa6_Ifey7lo2YS8m_TG1TpnHN5XxS7PykSNL-7DBs3VqCgIO7lTxO35zA4zYvAC7XHcL8jH61TBgvffZqs_b6PO6i1Jo_6H6oFonlWY7SCtfbD7jutqe_xjzbHS3G5I0u2IwrH2FiSSgxKQ9SBW3Nc-hnKEyGB5d_WQwP3eNhbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kRkdL0k15-kCp8LIayXMV70cpTmNBDzXUm_wqqG5iKxcVjkcYTf4enpOTKAFHdMgUQ-hFgj5iTruud31LZ5x8eTTethMXKatCR99ZK9E_aFpwB_20dDoIc11i16FQ9QKLSS6JO0EIgElvBl7gn3J8cM3hHK5deteMzkIxIa77mJGwddOGqBKBQJEt6nyoPljP1KocCtlYTTkHpuQgnThSpe8fiVrOmVGElXXyopvTt4cD7o5RYq3CIyAUpGa3jB1fQ7SsheFqwATjFg4IenyyRFfr-8pZvOGkt6SvvGQBL7QMRpQlcNL8KyukgQoaoywXzNsrEt18_j4uw2dvaEIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b-CUXz6ucRc2eK2T88SHc9-ytQrua574TcmRfsXiE6EvK4xzVrWtNLPKQZxMPXkEs4hR_Yy1E0gggnBtvJmqy8JrNEUqkT-Drp-Hl-Tmp38RCKl1TsXgMqkyv7l4cM1fhKvNHO3bp-fY0mTMhua-beTHCvlOJCcQJT9cUnHi8e7sEE58Rv5jK4Jc8EH8wxwYBfykHfuv6L-3QlxoH9L1_Z4FhAKRh27lkaaCfypZkI7-_h97PaMGVji6Qigk3L264dpKqJU4ss-KdQncs-ySzvkMYQmrlD3e3SarEeOVSpRw9s3dnVxSoOxU9pJ_MEof_8Cnr3x4GHOLo7ZLBoiBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DCIP-OfWWqFHDgQ2fecdeq0ksw3KiHd7ETADEpJZ-LYg9xyOvFUlr9U8V0Kx3UFhkGMTYzoAmpXDk8oMP3dwV0guwkD9QI2Rssd4g4sZdZc6KijZCMtZ00HRPPihmeWA5pRY7C39JTBWykvpkaDvBhrmdoSSUXWXEMo9QyuD4lLpgzZDYrsZxF-Kui18Qih7zooOjLhHtJPkie4XU-MlRZ8quirgo1lAchpNluKC6CietEbA0pAxhx4QVR2SKgxIc0pMy4qVpPxspnvDJjnu6S9qcaOIvZbDZs0K5rBwVGRaR_gxmQrhp2tWHqI8Q056Ugkh0NHd1HB36ejS2YazOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YaeruJUPt5GxTsx4i2Wbx_C4VYCYBQtBoGoT5s4Onm0doYZOPkdq49Eyv4vUEOzDk85brojFR_nieHFZl8ByGGEoMltojrU3drHiAxx5di05nelqlQ1ZEY66VfRsaVxnhfqRfqe8e6q_QLuh1As8lsulL1kYRpAYeXGVpPX7XbaPmE5YdZDML203rm9wumr30DP7B8azdVt6SXEzXmvhI1wyRrQy6l1klqb1dV2GbQwFX5CQVZkT-BIDzY0mXsEAMiC6L_HXphNhMRnl7nZj-4DdyoQg-ZghT76SZduY02cjLDiLByl5Z-BxP-erRGeW42e2vSVAg5acoTG5SXLFEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iltDRSplNlA2QOswjCZr_ztkd5Rws0XlSghuNFFHja3zN-dfdBgXryvcD2bJTy1qx20mZfaRSPj6iW9phvY01oYgiEtpcSXLYjM8RMga1E0QdBFCNUMRR4IdB5HGBXXoeiR2KzJv-3xRRQNhkAXl0MoYSQuZ39YoLocriOhPiJb4PFPJg20IFp6TZ3RVaoA6itnfjpzx_iVWwvwraSVw15vJ1zexBax09vEvjvm5w7NN4PzcWi68wbZEqqfKHfH3BNhEunPc2YuA547LwtJkoosNLeXUxQs2y4Ran66vhLU1Oom2BLCOOBCA6km8RknIChHYttSOr2DQburP1Gy1FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fnyRmDtdi_DSbPqGpCthmbY5uaNhskFg9PrqIIIKhu6ML6T4mIwDO9Bka2-39Q_htO-8BHijzKERFZu39pO_opKcGabc3OzhHsCasSMNRJhrNW9c3gDQnqeF3d9CFQnmNzqu2Yfd6ImYKZr9e9jM6b_GX-r_Ovb-I0RDkvJCX8ysJCYaycCCb95t1K4-5Ktv4PYqNQSE3Agb9s4R8ScwiXdyZqRJTupTEEmIcfeyXZb9QC5wJAKAiQdh9gZUF62kPr4NzllnnqTWcNVlQJNn30hYPTo_YTVkxj7VGua2NitqoEqIR8zFdEdtSj74bqvCKd3UOI-giwKQru45wj0loQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UzvaraftRHeFvcljXc9vP23GJqb9BLcaxFECQOMXtEoneDXV6MTHYYVKb9KsQfEITvQEvksPp30_O1wq4NXjIRASMBhZSevtohgHM6i1iEO0_XOBxtHwz0-L_SfQVJCUoGVVGJ7uEv5A333B7Prawj6K0aMnFG_Sy70rcWnu0HX3s20HU9kiRiIxHGj2Wja1zUX9O_iHneCVYd5MUp5YM-eNtB1HbbOs31mo2T2mM5G0weVjPWM4vByw40cUGPbnT15EsBXCV8cf6VVUfUMpZOc6ZTG4Av15LlgSYsPOFT-_SpR10S0W3arHgY_ZdQziGFXogoSjbFtSsFM8esOZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YqnfSloB-3L9yBOLszx32WFrI9wks6J7-1kJYjwHe1S5Q9MKi6UO1qsjxR_PcTlgYeVusYMFdlN69NByZ0Mx8U5RE0jJdxltotGGqsK2BWAM_4RGR268Lzuu-NLdz0S97gzZ8_eZJYoBRxzxKXd_kEAfk20y6b2SGyPPpRLc54tbmLd_imR_VNTtmyL_90gx46sDffs7MJCNpUu-HDXO23GbJIPEIwRIZ9k7DNN4uLNEHAgMSj4T0TkvoAOshufLQSGfJ0uog4trjbAf0UkaXIEFqe2Q5gCk3ZxQA4DQJ8A_jt5BLdlIeqePHApqRFsdODg_FJCTML3435lZjMRyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fpa79aQKLZLm71c320q-MB1swACQw61MbgRHZX3H4nO4HUs7sqlnnW20rEaCys-pYPJIMzqPJ5jTOkK2g8Y-FA8kz20BdEppLSmDOsuO-Q0xb6W2uWpr3geZCd1L3eDgdPeOrn7i0o-LCllKJJNARsaneoNE6GOd1Ona_St-DeH4C43IQMTGQBUkTKctuuuiV3tjKc6TQLqk0vpRfshlfAofoyrCaFTMce8zQHT6RcWQAfvCw68z5tabd7uprfPr4CTeARszMZelay7GAWLdjmtBaXQ1kHFWxQ8DGrRsm6WjMJzL6TkR1RJzIz5n_uLnzX2Mk54kxAhSS4fR-cHd2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معرفی GLM-5.3-Flash و ماجرای Ox Alpha
شرکت چینی
Z.ai
بالاخره مدل GLM-5.3-Flash را رسماً معرفی کرد؛ مدلی با ۳۲۰ میلیارد پارامتر (معماری ۳۲۰B-A18B)، لایسنس کاملا متن‌باز MIT، کانتکست یک میلیون توکنی و قابلیت چندوجهی (multimodal)، که به‌طور کامل روی تراشه‌های هوش مصنوعی داخلی چین اجرا می‌شود.
نکته جالب ماجرا، پیشینه‌ی این مدل است. حدود یک هفته قبل از رونمایی رسمی، یک مدل ناشناس با نام Ox Alpha به‌صورت رایگان روی پلتفرم‌هایی مثل OpenRouter ظاهر شد و به‌سرعت بین توسعه‌دهندگان وایرال شد؛ در عرض چند روز، حجم مصرف توکن آن به رقم نجومی ۴۲ تریلیون توکن در شش روز رسید و صدر جدول‌های استفاده را قبضه کرد. جامعه‌ی فنی با تحلیل نشانه‌های تکنیکال (مثل نوع توکنایزر و کدهای خطای مشخص API) به این نتیجه رسیدند که Ox Alpha احتمالاً نسخه‌ی آزمایشی همین مدل GLM است، تا اینکه بلومبرگ گزارش داد
Z.ai
این حدس را تأیید کرده و وعده‌ی انتشار رسمی وزن‌های مدل را داد. جالب است که Ox Alpha پنجمین مدل ناشناسی بود که طی شش ماه اخیر همین الگو را تکرار کرد (قبلاً Pony Alpha از GLM-5 و Hunter Alpha از Xiaomi هم به همین شکل رونمایی شده بودند).
از نظر قیمت، GLM-5.3-Flash بسیار رقابتی است: ۰.۱۵ دلار برای هر یک‌میلیون توکن ورودی، ۰.۵۰ دلار برای خروجی و ۰.۰۳ دلار برای ورودی کش‌شده. روی بنچمارک کدنویسی واقعی (Code Bench) در همه‌ی سطوح تلاش از نسخه‌ی قبلی (GLM-5.2) بهتر عمل کرده و با Claude Opus 4.8 برابری می‌کند!
از نظر معماری هم ترکیبی از MoE، Sparse Attention، Linear Attention و لایه MTP به‌کار رفته که باعث شده حافظه KV-Cache به ازای هر لایه حدود ۴.۴۴ برابر و محاسبات attention به ازای هر توکن حدود ۳ برابر کاهش پیدا کند؛
خلاصه: هوش وحشتناک بیشتر با محاسبات بسیار کمتر.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZxA1mVL9eVfhrvGQsmtmRPBljwZ0Lo-5l3zn1s9vO0gI00yzf4hZjiIgRjzBSO3Hw0Ad7YW_dNqAWlDLfHLpTZPkHE4fxakZfFDhWZwA8PBPRH38xchx8Lc2RoMHxMrfpkAAgD-Y_f06q2wr7ib4rFQzH-XeaNypk73WN_o_5qozo7YL3gijAn6Nc0HYgCBtniHzBte4rDhoDx5odSlt3I3sqiszG8XpZIbk6D7IJO1A8oRD9OjlnxwGtzUPiHMehZ25LPce2yYwRpc60DeN6lWz5MuGE8wL9qGfe9JZB9vlH3Dx00rbkBxKvz9KLhfkVvYnuXdMKKbTIYuCY9NoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UEfyWA60D-Htc5P8pCPmf6Qty5Um3c1cL0dLzYFLyzGmVhidSbcrn4DE63MpgHor8vzpcqQhOG5l8KUW6pWg5AWERvvFHGaFAoIAnEYqPknGSrkdbBcto_Nb22uA4xo-LtC1MGKfKJmkHktX2qCSUEfMVqdzEcSnHfY5Dt_CMrSBMCbs8bBwo4JdfDvxwSsSQUkmY0CEL8r4zmbJbjaiDF6kwdLRxz8R8bK-4--1wNtxcJDi4SfmlOww5BJxfUsWn8DCSwsYBRqcVS0Hzw52ibGvwlb8HUNh4hR8crxxLeicKHvLuEl_XUkHxTQE2QSdljuTHq1AbEbttRNaTvoOng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uh06O8JiZKrZs1d8iz1rdL5Texjuk2NH5wG_4yE3DXxnBjB6sm2rei9ayIeKEoZ41MBmDU0e9nNqCIFXKpX_ypP8NKOebNsvAZQwGxhfAyyQ6kEQN3EAtbxb1ZtfgAjmWkyNmSKMd_mpaJBkAmZk7s9-8IJdAZSZfm-n7Hlp-jkYNtdDWYEpYzydY4GSVVRvveOy3s6ZucHkDHdRLZvmaTMo4sVEFAaIoJE7wJGQd00cbAIiFVrT8Db9BEniHRegZ890V51O60w8NIV62HZzCE29Q5z9Qf1epxYJIQ7xo81kMwps1HlZ5BXscSvsAJ9YO5c_7Wk9OeRHzgjOljMbxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BfAXhMgkY2A9huIfchdaZyg3ILLd677FJW9wAtHrPB3insRPq_v0c4mDq3YN4d9aBRL7X-oo4PfzKR0hqAqfpc1C3I1JePiGfcLEoKyv8fAHtxDCWQ48U6LIwjJRCqGA5Dx2eeUOjFCvcAV60xLeVGDRQzS4exTY0ticFR6TNmuowmlzsnNPKXHU7QHJYQQXuCkN4ts_niQhMAYM1xhbfKWD_WPHs8W40TJPI39b1uVVSqmGXoomXmUhqBrXVmereDriq8R5ykdjcxxdzh35OcqZgMA9IqSqEgY9MV3BE6bBctp6aR4eaOjF2eXpdMZRdbE36Sl_qoTGyJTyotOerw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bNyGqXcmkijebt9NUE2SqtyHmGVJvEbJ990sNdAjhIjONn2vdmhNM7hg9nWcjjLwAXD34gJr1hPncE4B2iD6Eby8B1JNdQu6IHhD2hgfJM5-_DQXbrttmr9ZEQAY7H588twOzzaYlZ37IhMhme9v-vC9Ha3eM5Wz5ile5BR7ICOO5kBIF89wugdYsK-tvL5MOnaBKxZ4AXb60VZNd5uDkFvcc2aLssA0YPcwPqqxNiiTxeJoDcVphyHh5EsD5x6o4grFpQ_L1JpfOkZ71kuIHEVQsRMfyzX3KSAbNdAP9B8PX0rGnSWmpLDq8DQHKjjWOIFFP9nm48jsT_v4Nx2bJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha
با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.
هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha:
https://youtu.be/FIhoccZtpZQ
برای شرکت در چالش:
1- ابزار یا پروژه‌ای که ساختید رو همراه با یه توضیح کوتاه و ترجیحاً عکس/ویدئو ازش توییت کنید.
2- من رو توی توییت تگ کنید:
@MatinSenPai
3- عضو کانال اسپانسر چالش، Lira Candles باشید:
https://t.me/liracandles
من پروژه‌هایی که برام جالب باشن رو ری‌توییت می‌کنم و در نهایت از بین شرکت‌کننده‌ها ۵ پروژه برتر رو انتخاب می‌کنم.
🔥
🎁
جایزه هرکدوم از ۵ برنده: یک
شمع صدف
و
توت‌فرنگی
از Lira
🕯️
🍓
معیار انتخابم بیشتر روی خلاقیت ایده، کاربردی بودن و کیفیت چیزی که با Ox Alpha ساختید خواهد بود.
تا فردا همین ساعت می‌تونید توی چالش شرکت کنید! چون احتمالا آخرین مهلت استفاده‌ی رایگان از مدل Ox Alpha خواهد بود طبق گفته‌ی OpenCode</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FOofO0xr1WZtmps3GuoHoYjagkRFGrlu7vv0J2z6VDn7FZ1sAPsm9lsiaarX5nPSP6sQv1B-y1xNPlcMFYH4baTBPFFx0wFX0riPuMfdEMYzM1x860J-IdI5cyn-K5LY0VGN5IiUFoolU1uIyrp-1Dot48DuMKfo5qLti0gcGKkw-3_xOuXh446JSEc2wsKf1iCgp8Z4cjmdEH-l42fdX3EnI9iuG7qHnu_pk2350_EdRqKMTWxSOcExYg6WuU-vABVem0vpN8-CmKd0lPwWyS9tNPZgri92mGH-Tzg_jdZ0Cu9oCWtx6T73XsifdCZesv-9aJGCMgsjUZ2e0K3OJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=CzW-0VZzG7sTKMXcmyzobb--GLEvy6zVxmBQhrS4NmtOtuw2OIkz3YCbCt-FKd4qr8PHMokuF2wwLPxRMWOIQ1YwPcr6boiP4X0FbepbXWcm8OZRpYerfTlFYFRAzxTQZF4P-Fu2waCIKp-FLgR_kLMi5I2olnOHY6MDL0_JZBF2Q-YbV2y-Kpyr8xo1qm1N3KCZdsin1R0KBuUKEgVO4n3Eggv-vz67za9n002P39k5SKstuIS7yILMEVDy_8Qvmf7eIvQlgxnStl95J2ljPoaUbir8M4CActZRO5DVfVRNj8g0a-aNb0VFc6h2z6m6vVMKnOYpdoSjr2tVQr8RVl9uH4jcILpTpoAM1HfE-A7WoNPouy8iZ6n2Xi7zWwIyUeg0cMGFYa3q0pOkDV58sUXxixWGk1_rEV5TTkz_gBvJeAaBKxBsK-eCM_dVXM3uuhm6_CF1anLfsxmkV5zvnSGngtq2UrVG6hNh9VEIE6W2FaAHU9eh_cgVYmOGa9tPikIcLxM3YGz6cj8UuPY0Aq9OkyrLdo0dazLHO8Vc3SPsSRo8-Xf8W4iwJWOptxnwKb9COix1QEUEmGnxKac8phN1PanqOGfgDGyiQRVD-LIRMqIw1eTDnMYe9EC02eQzw4ReQv7EHO-4T85saqLi1ZL2Y-T88PyrvYefag488-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=CzW-0VZzG7sTKMXcmyzobb--GLEvy6zVxmBQhrS4NmtOtuw2OIkz3YCbCt-FKd4qr8PHMokuF2wwLPxRMWOIQ1YwPcr6boiP4X0FbepbXWcm8OZRpYerfTlFYFRAzxTQZF4P-Fu2waCIKp-FLgR_kLMi5I2olnOHY6MDL0_JZBF2Q-YbV2y-Kpyr8xo1qm1N3KCZdsin1R0KBuUKEgVO4n3Eggv-vz67za9n002P39k5SKstuIS7yILMEVDy_8Qvmf7eIvQlgxnStl95J2ljPoaUbir8M4CActZRO5DVfVRNj8g0a-aNb0VFc6h2z6m6vVMKnOYpdoSjr2tVQr8RVl9uH4jcILpTpoAM1HfE-A7WoNPouy8iZ6n2Xi7zWwIyUeg0cMGFYa3q0pOkDV58sUXxixWGk1_rEV5TTkz_gBvJeAaBKxBsK-eCM_dVXM3uuhm6_CF1anLfsxmkV5zvnSGngtq2UrVG6hNh9VEIE6W2FaAHU9eh_cgVYmOGa9tPikIcLxM3YGz6cj8UuPY0Aq9OkyrLdo0dazLHO8Vc3SPsSRo8-Xf8W4iwJWOptxnwKb9COix1QEUEmGnxKac8phN1PanqOGfgDGyiQRVD-LIRMqIw1eTDnMYe9EC02eQzw4ReQv7EHO-4T85saqLi1ZL2Y-T88PyrvYefag488-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نکته عجیب در تست‌های اخیر کاربران از مدل Ox Alpha دیده شده که واقعاً سؤال‌برانگیز است.
همان پرامپت روز اول، بدون حتی یک کلمه تغییر، حالا خروجی بسیار دقیق‌تر و جزئی‌تری تولید می‌کند؛ مخصوصاً در مدل‌سازی سه‌بعدی موتور Raptor که اختلاف کیفیت با خروجی قبلی کاملاً محسوس است.
اما سؤال اصلی اینجاست:
اگر پرامپت همان است و آپدیت رسمی هم اعلام نشده، این جهش کیفیت دقیقاً از کجا آمده؟
آیا مدل در سکوت روی داده‌های جدید Fine-tune شده؟
آیا وزن‌های مدل یا پایپ‌لاین رندرینگ پشت صحنه تغییر کرده؟
یا Ox Alpha واقعاً نوعی یادگیری مداوم دارد؟
اگر این تغییرات بدون اطلاع‌رسانی رسمی در حال رخ دادن باشد، ما فقط با یک مدل بهتر طرف نیستیم؛ بلکه با مدلی مواجهیم که رفتار و توانایی‌هایش می‌تواند بدون انتشار نسخه جدید تغییر کند.
و این، از خودِ افزایش کیفیت جالب‌تر و البته نگران‌کننده‌تر است.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">راجب یه پادکست جالب شنیدم در مورد یه تیم نرم‌افزار نروژی که 4 ماه کامل از کلاد استفاده کردن و بعدش کلا بیخیال شدن برگشتن روی روش سنتی خودشون
فردا خلاصه‌اش رو واستون می‌ذارم</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5044" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5043">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نمیدونم واقعا چی بگم راجب اقتصاد
برق
...
می‌خواستم امشب استریم بذارم و بریم سراغ اخبار ai، برق رفت کلا تمرکز و انگیزه‌ام پودر شد.
کلا همیشه ترجیح میدم کمتر صحبت کنم راجب بدبختیامون چون همه جا میشنوید. و بیشتر تمرکز رو بذارم روی کار که کمی از این فضای حال به هم زن اقتصادی کشور دور بشیم...</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5038" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5037">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d-X4Gat6_B4CpRo5Bar6peXO3yrYhGHTO1myPQlwvYrXNZTme1313AhHWGvFxwuW7aMQ5ztxpakB2pFR5tq-r2IFLCFpXP0QTGm7jfVkgs9GFwjtLfXX5fJqiX7q-NX26-tyJ2nuyrsHqECcGReRFTnQb-CLXnUu1E60_tbxHl1oXoTMpUXDQFKkLnFXnvBy2jr8kmiRKxt9vqzsotA3rje7hHIjypeghDswFJM_GqY60D43V_Y79gF_bgGcnEK7cFjIOKuwLB29_c9MS8E5FAFXS_2q33vZFn_Kbhx_ydn8-qHgmuqHOfC2r2d0nNz00jY6g0T9kYyjaicMQkFI2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UBNtMM0S2gwezImGwwhMRH5OssEknCMKac-MgADGAzCP6wv3L62J8gVwajxstAwRIawiGwUf1bR_7rH1hTQ5CvhkvmPUiQdiyzY-YlkSu6HWjXmZJ5V3DCYUnFYmECQBmSeRAXDXnuKeXwGfWKU7tzBYuyH77QtydIjMqeY_7IIcPUGxycKOkbCfgw2FD4herUi8Pd54oNFdOZIKZ8uNli84SfmshED6MV5XQojCRuk_P1A1YjS1jntJ84MbUGhwWaRmT22MjpSb_XFAk6BEjQqOI9cpYZsLytvAyUHx89aIFz1uxO_xeYshfH1jIc_xefCtX2AkZtE-Hawwuk6Fcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو:
1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه)
2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید
3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی بعدی که پشت این میاد فردا، قراره حسابی ارتقاش بدیم)
4- آخر ویدئو هم توی ثانیه‌های آخر یه چیز جادویی هست. اولین نفر برید ببینیدش
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به هیچ دانش شبکه یا کامپیوتری نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5034" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آموزش مدل‌های AI روی کتاب‌های کپی‌رایت‌دار؛ قانونی یا نه؟
خبر:
اکثر نویسنده‌ها بدون اطلاع و رضایت خودشون عملاً توی ساخت همین ابزارهایی که شغلشون رو تهدید می‌کنه سهیم شدن. TechCrunch یه تحلیل مفصل نوشته که چرا قضیه از نظر حقوقی خیلی پیچیده‌تر از یه «دزدی!» ساده‌ست و Fair Use وسط این ماجراجویی نقش تعیین‌کننده‌ای داره
🔗
https://techcrunch.com/2026/08/23/is-it-legal-to-train-ai-models-on-copyrighted-books-its-complicated/
نظر من اینه که حتی کاری هم از دستشون بر بیاد که انجام بدن، دیگه به چه درد میخوره
😂
مثلا فکر کردن OpenAI یا علی‌بابا با Qwen که خودش دزدی و دیستیلیشن از کلاد هست(
🤣
) و... تره خورد می‌کنن واسشون؟ =)) یا مثلا میان بگن آقا بیا این قسمت از کتاب شما رو قیچی کردیم از LLM چند تریلیون پارامتریمون؟</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5033" target="_blank">📅 02:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب انگار قسمت نبود
👍</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5032" target="_blank">📅 01:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه ویدئو داریم واسه Open Code
داخلش یه پلنر ساده می‌نویسیم با Mimo
توی ویدئوی بعدی که پشت سرش میاد، میدم به X Alpha و اصلا یه چیز عجیب غریبی زد.
موندم که واقعا این مدل مال کیه</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5031" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/5030" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دلار 200 رو هم رد کرد
ولی نکته‌ی دردناک اینجاست که هرچی جنس می‌خریدیم تا الان با دلار بالای 200 بوده قیمتش
الان قراره حتی بدتر هم بشه</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5029" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VIjchXTv-yeAZmxePH0r4SIuzMAlU9ORqPQKiQtcLS7Dav_54Ye5fmkElnPDQUYNcJuKvez3DsJN9Lc2sjCc-GBAlNLS2gOQ82f5uDyW_OHnq1N5BHPpFbVWVlpusUKsJGMIQ4xmEqoQeCM02Es_etpYgC2JriY0EG13G0qP2rVu3Yznt3N_FbStuNMiE6G7w5zplnVzmwQ4EJwH4PvA0OXGJPJFiSb_MiS6AZ1tVf2_CmPWWIbtKHVUjVvdm5o767pGl0_nX3GAEgtOXNLlQprNRTkKzfnmvxhztHCaz9iznP4cMTlq2lAgsddO99ofpNELzoDTaX_SPNi-LMrrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسیدم ۲۰۰۰
تا الان ۳۰۰ هزارتا امتیاز
دو برابر بشه میفتیم زیر ۱۰۰۰
❤️</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/MatinSenPaii/5028" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nnVCAt1LYNRjc9_P32OBpIYWKObo4joy-UUgS-Fz-aKJDO3WYcLPFUthqUpMMo-2MPfaN6PI4pN4-kLCbTpNylhRjvuh6tvZeCov-kJ47Giw8eT0LQq2pTr-jdQL-va6-3faLi9Fv-upsQowb6BxnUV3ASzvaWnxBF3VMrjMvl96v6j-4cCchTTVQnE0YCta_MSM5oH-7bh8DCdQPKkgIFOxqNMJZ9CFkNqNM2fpbABBy1qDeOvI5zlpg4okNjyyjgNkGR3Kz2ymNIjSJGvWGc2swi1q_1xq00UOLaGwtYTyAQTQJp72ZvD39f705aNrZBWEMynpkUiFOMz_bGHcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jn-KzBKuLZBWZO02d-0ftq_bKEyIsn-ES6N6IYhFTnMSy0yzaij9xSMdmrW5kiRtH821WZDnf8SaPwEr8na8TXJh-XtmSpWg8fQYJRwsIWEK4a7ve2wAIbcSqndhFHr8ubtJxlaJoMcr96Gy2Clt_cO75BaQlHdfEe4nUL1xZIghzDDWdRAU1BnUm624Og251x-3-hVyz7AcemLak7KNA4k6icLfV9qzi12V6NVGqM68RsCpMSyRPUFL0A5LWx8Y_7u5CTOYAb3Tq3g2gBPNsyBpR44r86nLB8KoMwMZjNrrSjkNJ_CpHuNGDbri279kIQuRJgvgQDiUafUegFma8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یه چیزی دیدم تازگی ترند شده توی توییتر، یاد همستر افتادم
😂
😭
گویا اسمش ووچ(VOUCH) هست و طبق گفته‌ی دوستان کریپتویی، یه کمپین پولساز هستش و فقط هم یه روز ازش مونده.
اگر که تونستم جزو 1000 نفر اول بشم و جایزه‌اش رو بگیرم، یه اشتراک Claude Max میگیریم و روی استریم میریم میفتیم به جون ایده‌هایی که می‌دید. بازی سه بعدی چرت و پرت هم می‌سازیم
😂
فکر می‌کنم نهایتا 5-6 دقیقه زمان ببره انجام دادن این کارها واسه‌تون اما اگر که انجام دادید، هم به من ووچ میده هم به شما:
الف- برید توی سایت
commonsmade.com/vouch
و روی Claim With X بزنید
ب- جوین که شدید بعدش روی پروفایلتون رو بزنید. اینجا باید دوتا کار بکنید:
1- گیتهابتون رو وصل کنید
( گیتهاب ندارید هم راحت بزنید Continue with google )
2- مجددا توی همون بخش پروفایل، یه جای کد تخفیف داره به اسم gift code. کلیک میکنید روش و کد "love" رو میزنید، باعث میشه ضریب 2 بده بهتون.
بعدش بالا، سمت راست صفحه براتون 7 تا قلب ووچ میاد و میتونید به دیگران به شکل زیر ووچ بدید توی توییتر:
Hey @commonsmade, vouch @MatinSenPai
زیر این توییت من می‌تونید همین جمله بالا رو بنویسید:
https://x.com/MatinSenPai/status/2091522197537919325</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/5026" target="_blank">📅 17:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PH9dgfWB8jGoOqpejO8oIBZTjU8xjzacLtWTunfaVOKEXqrjHIwbJXjdztTHAWd7CXgTO7aTBUQpo5wPoZRAJqFpyrz8qvPLQ1OFbTQqG1RR71eA6N2ya8yxRCVvypoeerk94JFNF_ij9AC5cfG_XsZJmNE1INU-npo-3woPlrLrTNeP4nIGC43M31yBuLQKoGP61TFtzgWGW6KwM8_tBfyUBru9fdSuzU_dq12pR5yD4n5ASqXk0NOwwiaweZsMNnKS3uUXwqA9_PMTU1MZHByIqJWXfZnvU9OswVIM3ZrrD-6pVhLNUyMyYCd7AcVq9IxoHqx225V8g6xpHvlv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا چند ساعت خوابیدما دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5025" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1357719d90.webm?token=kNe5SvXaiYgb0UOagCd2ydf3eYIBWcZGn3gGajcn7ct2aZyuoSnpu1jRq8a7PfbwPk6R3qHc65wqbYWCaN6P3aSS3SGEelKADkETzqoU3pw7DALRQMzBmhmaBMqdaWKFGBPT9_26GH3XE9qokl1RQBNqZhLO1jb40sxvlmR8iZ1v2OhRsrjAT-WEK_0q2hataZcAAS0jJ_NeVsK_EQihO6b0LhEFwP1OkeAYgkLP5czcXCprrb2meNs_mYyoTC2v4mTG6MdLxisdeMUNuO882gPINdrOR5aRUaXiNeFS4JPu7eoHzTgEuwgbOVCPm0wBJlgMS3H366XDhYyzTR7LQA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1357719d90.webm?token=kNe5SvXaiYgb0UOagCd2ydf3eYIBWcZGn3gGajcn7ct2aZyuoSnpu1jRq8a7PfbwPk6R3qHc65wqbYWCaN6P3aSS3SGEelKADkETzqoU3pw7DALRQMzBmhmaBMqdaWKFGBPT9_26GH3XE9qokl1RQBNqZhLO1jb40sxvlmR8iZ1v2OhRsrjAT-WEK_0q2hataZcAAS0jJ_NeVsK_EQihO6b0LhEFwP1OkeAYgkLP5czcXCprrb2meNs_mYyoTC2v4mTG6MdLxisdeMUNuO882gPINdrOR5aRUaXiNeFS4JPu7eoHzTgEuwgbOVCPm0wBJlgMS3H366XDhYyzTR7LQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5024" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">به خدا چند ساعت خوابیدما
دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5023" target="_blank">📅 16:25 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
