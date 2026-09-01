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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 15:21:35</div>
<hr>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ILpoXPRH-X9WO8XMLjtVS78JerELGUt2--LOjDCcbWyd5JJJ5eF1rdxWetaP_CgwZjK72xo_ZuYsBCCHSi65ZpNonGah-Klswcr8RHY70EVbXmRTa69r_A7n0Qqko5P0zcW1pedKh-y_kgxXiVdXwxvi1eNdUuRqECebDDEwu7apjtoi8bz9QyUFWWHlp0SHe8oS0lGnbJmI8KVWQGI5k6kQ3FhidnBGGSrjLbjI316iIBC3OC5xgZD0ZrGOCX8mNmghlntuCXkKU916XbPM0iGREnCAXP1_AJ3aNxptP3UTGOTZiefMTlS9-BEl4I_ld1eLfxIAlQHypDta6k5Czw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q8N4UnGFiNZRx1CW2q3UE5JyXj9rgdl3ZeNKHasgJJ-So5mpl6n4785pc6W7zyYzlFFH_yEF5QQgaUVGohcUZOdC0n12v_siIrE_rswWdflZG4G1nMlkvNr9xnq847X9qej-QbOXqwU5zzKFyuWJvaUxVSq6aAaTbbgvQKqy-MZ2usfvt31WgKWQF0b6ID9uh7xuYwjembZOW2Fj3h6IkpoozPOEBMPhydv9YH_QXyj2JDW1E6D7sZRu54wFg86QqzYdEyIvivp_qjdnVsOKvFB-gqFjknmqHBstZ4Thp1lmSoZeZFaLRTLdKpVWPBEp99L_OCNlZRfr7AnZfdBt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FrLlL2F04-7j-bbtmjnVcSF1V4V954guqCD23NKMXhuytipaLZ0iwPnkX-Eu6ekJC84XPN03VbQnjUR8uOb4nOl5kIMsR8mhJSh91AUESbgV3gqBY9WMUuTBwldke6Jz4Sx6tZqxLCn-_Eye7lr8Q15GhLhScpyDcSpKwTNxRTYRs6aRdgFNoeragRhX77fV3QrWUC3fe6BVoD3pM3uxHkvBFu23P_PJ0v4ZSjCyKcTLcCfQ02nhhrMDKugQMECpIOVhYMCTG6YhuwgrPbPvpUcTh99Kb5-ALZlJ0CuFlMgvwnbiN1uBwH3OjqRqhiIqMO_pxhii0akrsQ6ryHTUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/noA09UQaWifbs1DRaLtCVxwGC0e77jkegQYWoFvDtjo86SZXf3TlJYHEIR-DZ2s6nHHgDt-WKl8HDyrL42O9hbWm1ZXxUfToe64D2ryQRR_JmNZM0mywnOJ4Gi7j24bPSf9cDbL2APrlV5_IB-lXhEGiyNCnIJ2TWYvkRqTRserPpyFEBJ5fx91tRGvN1rBEvxrUCyDSyrKTyRkzjRFpPkQUcg6fW0UNmFVYBzdFQPdH55rGrQBC2h391TpZV1kcfP2vUpD-3_iYdzPZsNyKJyiWNBQQER1ECkpS5nsFvoipOqrxW8yvZzuvfsB6XF-M8xGRoC4UZe6lIflwEgGwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dF7WRtpKH2ys9-dKrU4CA1X5kwTHDoOKl7xzZYBXgeic50cBK-mE0mraKYk_ZfQ5EwWDsuO1fhCb08al9qUdubbM_sKio3b3BAzmMTcMoAQy0P7utTTqGsJ3PZXO_F6-MgYbZ1Ynfs9qSzPBsQVogMF9JTC656hM6CrJbJYaTioyxvtAXCtMfckCQhQWq6ip5zW54dobOe4g5lnBmuZucKeJ32nc8FeP1rTfMsSn6qkebJXRxnkdclrCw_q26eq57rL6kRcaFKl0613-DaZescvj1oWPzS5gSyyfEuGKzJm631W78ZTm0WTq3LWxVVFse0x6eNPz4RNpPrL9j6lAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZcMPTcGHZH2VsLSA5qOsB4daylIuf2-jV9K3y_LS_Q5MiuCWKxMKxcsVk93If4SbrgZve9JQyWqcg0bz9msDxK7-NerBsr1bZxr_pm5XoA1WU8bWc7WCMk5FspQYVUdh8019Cnw8wymc3_by09WTnHUg3YD-lWi7-DhrqrYP4-1oLTAHQS4CEclh85r4XmBpn0u6kaCBeMstRiwTDm5Qk-IbSG0u-rDNJAojgCAuCE9OnVIf6Xft7P0B01HnE1oT4ypVgQe94pre9xLk-OqxJwpLLcblzawqNip1LlmxVHuI6edBRVnynAE7_a23sG5a6hzMkCmRHZ3DdPDPNgtEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Leh_LtKIPGHKbpufM1vKCwHf10uP7xSOxUsy4uFH1C2zya7IVlsht0rjfg1ovW0XDJ67-8fGnGGqnOeyRkdbNnyTtv3Xc-JuG0e-la59tez4_5nUCvGDhONGcxu1qbIXJXxIjmy80XZtypqfbCKAsE3dqiOBfWomhxSwTrus1fOTJ5QzZfaQxihAbgGN6C0uHlru3g7b-U1cDpgYLAfRCKFYVSz6sOxTFjEqOLZa7C0K8mFlHsO5v16h1kc1xgxAw12HNd2bNmcZtbU6DHE6uiYUnJmWRQ0DlVrCpIA3JYPJdwAKW3Oyy0J1fRQsr0Q9-PYxKcGH4kl2P44iasrxFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ve17BTE-Vwp3wkfU0xn8vO2Rz_6P7yNtdD1uixG0UXDe3E-016W9TSC9yrO7wDTnzsYLsURPfTpVUgpNiLoWFFIobWvM1zynolIQeq6r12U0sdXIo_p6TqhHhSrmuykxhdDo83ZSfIXrxPGSoLZBf4VRKek9Oi8Gbz2EOHhiCcEubn1-qkQY3M8loS7a_n0hGNpLBetzVfVA2WzStPoMUlrmiL_BeaPM0O1BoVsmWVDfV0Mo6AD9TTYJKZY0fT7HHI8ZnUELK64z_zlqTujHPLO6giHJ5RGcnOLpcJFvTBCysO3n0OTxpOs5EepkbR1Ap8yMJ5fLL-idgof9beq9Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sB8U_jY3f-vfyurl4NAXLzLqH4cZ05K8SzwGH1f7N7xv22BUoZddftGLqRhoMsCBEmlwrDz2ufFdc6HBP0DIAU1kV_GarShimOtMcQIwhfYOqkCNs3lXmQwoXMzaZuCFBfMYcUFbe3Q7xm-dwHjv7lfv3sIb78eDVDKKuj6CtCAx3qcRaZNQins7w1e9wIPOVXnI8O2lDfxYz3HUOAl36xjQ3XN5ztWqxarGyF7RGpljc2MY7GQQD927xB_-GCxUnENZ_AuWOY8HgAdWZmaZbvlWJ6SePxdU6-IqZc0B9Qn9RaejWhJ9S8p-8rW1_yr7aL0laAp4Nz1ujD4DFIEUAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AlDmmGvtcYqFCamLpwGP_uAt7s6XyOw9Bh49vM8u6ixmVE0EGqKlPoU4DcAv8m4V5VqYtQxc0ahWnK3vx6p6JyCq99EQKQAlUGV-Bs_oK8Gr0HRWvTNvUYt6yO50CznVodHTe1Dv7N69i1eTf1BXaXhBTC6cXaXZLlNK_tN4iOCuaO8IBmYC35E9LJ1qjRCrFn0oDgDYCIIvn6YgYUVIw5NiEhfRitntrfEomluvm2wCnWJaCREzdX29vxKAvHJwcHn76lEl4WFSz3yHvxx3RjW7ctzCDkDpMCmlqW5eBmH7LT_PXO1Tl1yR5W6GZUc_3CRn9tKD1zrzT2Gd6JhUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tQHsccmU1u4TqL-co-3YPpqaqMWgA8tBUUHg-FMyXyp3dghf7LzssktaJVlalE4biXAJNmVaF5JV7-SRq2J95A4OwP00q0nIusvYlUc84VXCU2G4YCoir8wULqLSMiJsPEDugNL-1OVuLxYtGkb8MYiKhpITj4zI_tUNwOHOl7k-V15RunBFzhK0axlZ5Y75yQgCjaFM5UIsAxPqKXD3kZMY4jHU4HfeG6aoqjbjSxUoYkyj5ti1vKerU_Sz_hGFu73d0i3bt5JOU-rGGldiN8Oj-44hyJ6FQEKm-g_upOZBeFBv5o7m08rpOBTOKGLufY4E-U2kPPUL_EjxEx6l5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qoOSQ5q132E-TaaU-bWCjvBSVLTV5ivnYCo6yt2qbGtpQBB_ZfMIytmCJUK1Z8OHIfco-BslQvfcHVJU28kqm-UID1ece_V7qEOIbyC8XrHRiuhhcvfhhdySKnpBn8UflCvPhTz2KVYX4ssZFL3O5S8AP0_ufdnqEbYAnpNbjXzgwt49K3TdJGMfSWHhnz5Z9A_KqpjooQ4khFwcNyACycjtSeGCzJjYlU4OU65nA5vrX-EyZ13kr0Pp47X7AU1s7I4K0EWpoyI8CWHTkqeqAfDWrfM26EOY9QPmCM_R7Han-0nxMXLjoo9B82rj9AJwXoSsrhF8XVHfFwKMU_jvrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FKYsK7Doa-YdDX9k1q0yN3AitsIieYzXKPSYvWbIaWUGkmOk-puQIZU3o3uNcki78fc1KieDG5RvRS3ItVGfWy2onKh2DtyF5UzJkmLwb2Lc_Qhz7tUqqG3Yyl65mSxj9Y8Y1OGGHNNxR6HKVJFKl_yQ5vFfFoVilI-KWZc5_IpMLrSUgoWCnCtQwl8ewaxl_0IMy4mosoOrE78T7WCgZfjDMbzDFsShvcDkCeCLsGEACAqCKvNll0AvPsiHi4ePXlCPdigmoVVNflI4CWqrxPDSjXqodJkxZVCUhpkmnRIj0gsYi6LCUr7P0uY9Wxywvu4xzAf1i-TRMcdwCWtM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sNh83_aFiwqXGmrJ_fRX5uYg34VegOHfUk8vsXg8p8rmK63tLBNibSOkLaHH5nqVWms0jY9ym4ndoDy52MNh6oORLG-WZmIY0Kja4y5pXH_P9fwdyz9DPkQe34gx69_ME08d9e28RxsvEfsbVZaA8IE-C-t-a72seqcQRg2FgUl-1R4Aiq-AM19E721V65ULz2-Ck9-cES6nX0PrEWTQpvPGi3GMkWve_ZlgcL99wXzvVzNQffS040As3m2bhgkYpOajW9a2E8JhNd_rZQ8_-0CeqwvCR86ZEKYjRYK4-lC8S8tz6exzrDkwoop-hVZeMx28_fuZmuNuCgANk1Yllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jY9c-PxvQyQrCykxGvJ__Lwh6_o4kMFkKj4isJlb14gSqcaJ6toXgo92EwmYmrsrSFSLOh0rP6bQ_rGvM3uJ3mnxnhp4Kgk4jhhtLCIFpUGVPi_mkIwJTKQjCjL_MtWxsnxY_2_O1Dqjq50ZvP1CV0u7VL9jiZvzXrzJeZZE1hdsGy5nERJ_D_v7Un36ZLwLLjfePtq-E0ISlbm-rzFXDxPD5Oh8DPWBsImdgm4DkmcDiiVYqSM9gM3DHaqMItCv86YGwZJAfbi-7CPyix6a3r1CZGK4sfr99aRQVY2JrLhpcw5nk5HiPEHnmqVt0i5B6UNqe0YeP4SCEW5zmgSG0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fWCOoC1E7gdKgj78MdFg8X-dgqsTu3bVoZGEikhLZdZ0hl4L7CmDwJq2Uggqo7lGaiT1W6kWcQcvBx8T15QL8qbijLmt3z6W2VHXQxPsW0VCQAYCiSNXjrPvkUNy_vwxoWrl5kuS2t2tesY6bVZ7VSQWfCKhQc-j-AXgtjGbIAgslq_GUtXAtZJw3JqxWRdXgbPEDtspN8gaSvNCs81scfxpeVdtF1MAijfzx09eDrgaMwRdQooAFhBxXOhb3HBhUsk0YFwdiBVJ1Z-FcQTZioMY1KBVMLu5tu4YNcpF08oWCL8jrTYB4v6q3_GpZc4xM9unaRRIhW5fml5866izEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gJGLOy-mH8bEfyZJjp0SC3GjkX1ALugVr1D38dvHCAy4PFNGzzFGayD5uEj2ONvNpnoZzB1I6zXK05FuU8emZhK1l8-DcoZqVTcrLLdk4D9V1ubOz6yfIqoiVrWuOgZE-JZMCq_jbG9SxCTIzG-D2AwOcBhh_DNAqfNXtPwfVmNDLj0vZbIf-WYHWTrlS_-xOP_Gx8cHay_yB_1Wj_So5DSLacNDlpPJrwscWELd2JP2yOR6ulzejPdmTQUXk0xYXbKE77Sj7wJFysbtUN3uKxQ_LgWbXoAHUPNS7tL6Eknvvto7gbcnw_LN18IZQ3-5RLYXgQSlvVTvsuECaQ3AFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UXSwEXpuhgvUM3YmXc7u0sWmvAPer9l1zt9C01ksYeeG_iWFGqtTDS4Zk632tmC0NKVInXBmH8YesFvtvmWpLRn6pkqUBVBjqDhqTFAig_FnnfHL1jg7JK5gjMJKCAFTZxnV3rQadWeqpgttX2Zq2884rLFCTiS4hu5ZyOJBUJ0fHQrsqBvoh5sq_4jNGy3xpb7knW8xXs_bUHFtG8gmDbQHTv-lXu-wLuf-5bLKAjwLxkdkw3POfC6z623ilqthToXaGJZQxFZg5xYRCmgNL3Xfpd69C01WySG9NWS1j6v7ewpVTWr6zhyrfsXQ157fMo1WgD5rpq0QJwtomz44BA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Dmnd01D09mHRFSwG1DSIdrhkFc585p_0HBxoHEPOF-FrIzliF1lK2zhfukMMaw4pxE4rUZ-FLicTiJYP1VHdzdShDK_OSeD6WXViTIVuk1CacHzsoDRmZB5ZfAU4NlWEwu6pDZQbls9b4wusPwKF0Jhw9QBSQG9plV7Ol8k2HEIjvRt2ndbPGOXIb5aaT8Uq-vLm7QK0Y-gWcMGi-LWazrYZdnI0QfUlVjt1Kw4pjS0EHnCaZ63dK22pS41EBw97GWuPcCmuqGZ9CkHPMf1gJ8DqWutAEKB1ephtmB4b4wYR53rhreaByQrBoHmw5hibv50iF_Q0nFPlk4rgY32kJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8qUwNFSaSxx8y6xpakkjfxfLPlkQUk5MA80HFGriy89AdjzhO9_GeJ2kbosilfS6NGTz6aBb2Va76Lf5DWTHE1PLdSoT1egM7nB3wfkqcuHwWpMasPKyDUOdKNdQHPCq7FU4Ug77SqSbw4aAxNKDM7i0xTbjCdTlfQwbKeB1UAlolt6PCdhR2m_m2wK11_K0LWxEU7owAejHoKiDXrT3NFYSioaa2hdNh2PFg_fNHnz_o-WsfT2XxPCOnDOZukoGuiKMx_h6bg52NiqwK_WbeikOsufhE9rj6SwraB29-rXh64lewN07atorTCOYJwJs01b5kR1K33pDfpuVXSk6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uf4NoqVuMWQRYb1uCOyGTYuGJOjJLje6tksfKMzWVJ6kbIJM8cNi0RKxmMdtFP1BwEVV7lgrcWDi5xo9N6VIy8zUyfmakso-ZAD3DBJxty7QY3tA5rslyC5Op-j7trYvGsR8vZt7ofzMPR6-zXhoX-DIADNr7x326hEc7xCsmKAJlq-g1ulsQYo4F3ODKzxgb5Ck3-KqlYgBDePHCxJ2NPWk3v6IcBIY-LovHMsf5y0BfQGlT7EbsmB-ZIO7QF7qXJ7bT5QosDBTN7irK6kfs2FSrgZvlgZyw2f9_vh4-dU3Tew9aSYi4hsiXxvElPOCLbOE0SwHnPbLFVoGLISnGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aQ0YOJRhKh8obo3L2otKaRmOZvsVi-oYJfuUxMSgabSgQSY-ENGuztLpzz68E_agR-FiB5Kw4nTCUas-0idj7-WHmnicSEF_911iffMlqpUilAyWYH2NdQrNdr1KSi0THiz-LqomiJ45OQ2P_FfKr-dHXmVGppqcLkRXxysXHkS0n-kg1o3G3tXq6Bx3-j8O9kpeTlJzVpocF0ooZ385mTaOXw318A59bduAifAxrzZbnscOQuO6GfYshwotl4d1SS1hN0EfgLmDBpFVr6NpKdVKCo8n0o2453ecPTpQVsTaz7Z17R9bCRQ49gzICZqbwqV_0p2N16yAxpE-g0Au7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gZYArKGpYGvBhJ0r1wQgqdpuXQNrzm2bkVDZ7lhBTw_QkLOQtyhDG6TgTo92q1mwcbRgNFXqX_hVgjW5n01CZS1uZcMnWZ4km5H0p-1nWZuNiqkFR2tcEaWU4htRvcM6xxVgO-Jkl607t1_cJCTb7ofOvOWG0AMH-2bVan26m76aT2MALBYUW5gobRChOtp_7yHFDcHOmpAje2ILvKkCCW1zg6tDNJji_k6k-6QvbIZgf82srv0bcqqFUo0JGuhnV7benKUKsnmRkpvx14GMTh4lzQawelfa8ENqz4VOmfwydJo2G0VlD-ErE6yquxXK-4LvWTrs31MrVIGf_ga1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=Jnyq2M2VEzZU-GeVSTzvau-stdh9zpt-Lrhr93WqJ8KNKXD0cP8ywqvFTN09LCCiMxx5xRdgWaLdv0I9jOtA4DAkV07Bg0bWvGHlotL4qggF7LLzSk5hCUbMz7I1CJZHa4R7XKvgBb5jUZnDymwWm1CpV_xUkqgqn9ybiMrZKX8OOezX2vAENNqsjvo423-zMhe1VZvJhsHXvGSLn6G-HTujIFdQCeoyBu10TqAj59dx2Ux75kHUOoPThtNnJunj75CM0eEflmrwUWzjSnnGp0fjb-1_wUfAMOLECVklzFgLZBvskNO7f90wmJu8iJll9Z4G_Hwvol77jJHHAFhJSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=Jnyq2M2VEzZU-GeVSTzvau-stdh9zpt-Lrhr93WqJ8KNKXD0cP8ywqvFTN09LCCiMxx5xRdgWaLdv0I9jOtA4DAkV07Bg0bWvGHlotL4qggF7LLzSk5hCUbMz7I1CJZHa4R7XKvgBb5jUZnDymwWm1CpV_xUkqgqn9ybiMrZKX8OOezX2vAENNqsjvo423-zMhe1VZvJhsHXvGSLn6G-HTujIFdQCeoyBu10TqAj59dx2Ux75kHUOoPThtNnJunj75CM0eEflmrwUWzjSnnGp0fjb-1_wUfAMOLECVklzFgLZBvskNO7f90wmJu8iJll9Z4G_Hwvol77jJHHAFhJSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0  مشخصات کلیدی:  1-مقدار ۷۷۰B پارامتر کل ولی فقط ۴۹B برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Mg0XnyBbsg9WmAJZ7C5kMtMJhS8tT1qKUA3Ai-AtvDNbSoTWgjvWLr90IddpI_IBuXiv5Y68IGzHeQ1Au5lQH-g8Pw8H-kEi9SNbHXr6xJOVqA0Nu-833qaYlUXB0qYU6KDIJk-pX7jhgZgvx7RJcEGs7vE1vU83vPYVxbh7e6GlBVRFmVQk-I3QW_FPW0K099vQ9QML_15-7VCqBTXrJpxwk_ywsbqLeN5nJocI9sUKjAxB-mLkTBWi6jwDA6ojJfhLIzuz3yiZj536alrDSZwdrXHU6NsD-6X6eXOT1MkUF-DVzPHHxbzlgWii3H86IfjHLZXdYz5nXVkHt7b2nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/svW5hmKziv7HCCpWx34WCah9Lp9QkDYchJ6nsjd4ObL9BBuNmr9-M54auepuro3i3filWC3OY9utzkPSvbno869vLdpqn-JYjUp7n4Kb6Koe9_4-vXAVyhK17JoPfEPpS8r9uFSIidWkEDTeYXbIVFmtuTeeoKxIzYuR1g1J-VgAnYF6bUYp-N02fw-IgKiDDTRS58-Q3r5TMCu8FaraV1z0QpR53YWpGMpzNWq_XyzcRsLFYZR8DBFcFeCzo6j5rMK92wYpX6zPcj5bzdhtmt80xz6Zuz241Tr2diOS1hw3Kl6AjY-625TUpB5Rj4sC2fM9N9m8Z038K11yzVHg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/LR-5G32FL6b4yYoimYShkkgtgXW_edONvGXSAqLI_CQm55XRbQ1j03W4YObre0b5zqho8ufnYqF0ByciPxNhlJTRZfX1ytXnvPisOEZrPVylOrmhaheySxlhtRrZ_ZP8KW9J-0w3QfVSWO0FpqPChsI_kp0PsFTQJPb_LIRBlziE8kbkjJ-CzQWjclwn2tHV7dvjBbRRfpceD3_591XRv-ahCKw2LOl1tRkoyaGtNjjSLg5UWqkPGnsXLTbspP2w8eg3W060RUwVTodd48shjROHWlQV3vUj_Jo_xT8UdNj2ynsbi5VyiH2m12l69Q4h2BQZvbs4AtyF-TmG8AHrwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r_vr_b5e0VmTu_Fcm7WoZVi1QMBhJYhB1t_9VQXf1GREU5SxdZCZYtqEGw5lbcBhGmZchZQ8kcrKY1PHJzNo6KPLMseTLpdIa00I1xtZ77Qbmf97bo-MyfU_2SE88VKBxxDXYTxrOpnmmWa6HMC8tkRTm-DeYYOzdjngzb07oHCxaP0PeLPR7jlBA19yITjvwyVzAGkZgino9xsfTLbPL9buaoj8gA1-QcPwBdcpTOd_eMsuSwa7BbaoSqU-kF5lpiXI1Rj0p3nmBtST630UInQMUSDJ8Vo6n9KC_um1Uq2T5ZknDK7IOBj-vDWXD9uYVbbRHHcuNKCcCOsJeDTwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iGM3QwH3ElkZd4LU7AsHNh3IJkvuvNn81DVyka7qa2buxKcGk-Czm6IBWckIoSR5cMelp69_sZYGFoUDKu8RaZUMA-mxlzFco_hq6LmtWoDvjfv-zd1DauSZ1aXgxhdaPOG7MFTZQ-hq54TJgGzaxFpylo8FhRsy0NH537CBZx-sqkuH5mtjh91wk0zhKmsoaKUhI-RQRkmDGGmb64MJjqSI1V06RmdTS7wUCoib2lHbewGnQrPGSif4gn0PQ0yEfQK2gr0H30Fb-Vs7b0RUiUTvdSIR9BS5D4rfWqZCaWERDVv-4oX0C46QBga5ZpUaWYEURzjOeITh9S4bDRst8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U7s1y5nwtgKdOg5gzELjQLiOa6IzEtCrGghhfa4Uiag-DO-RvSAQgtGd6ofs9b6RdWtlMcXF7XiqpSDid8AzfMIenBZTkgIZZKz6e1Ug7RKWtqdo8IsyyBHBAJWKYg6SsazxYEZ4fTzz2AygPij-6OO3mSaPfy_02qYCvR7s-qGTmTBwK_38iuSGF6j86I3Cu7j7Fb8BOv0BfvQpMT_re3L9ePPGIeXdsFcjNMfiUow53jeseopicFcINVGVC7UivPhdRJ7hBozPKdLY2J-L7uyJkt-S70NuLfEuhTCPR2Mw6lYEKJmwnca_LiHQ6XooLx9lDNF7TTQrlhd3k32VFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IWSrTsDY54Aaw4JOJD6-bsSN2fQlGt7UNSaprHl9QuOWemFcNusB1g-2l9TFcYdLfxKBIQqf1UAP97X7crO7D2YTqwTYEpGCi7f2a_HFt_VEcekVsIE20QXZoh7zwMtQJYN8rfA7QWDOfQL2ycz02yc2fA1AeB5RLQxU7vpQfZKNgPOpzZzJdeNvFlVEpVc8QDcMFSaPcSpERZeEVyllLt-9RcHSf2cOy5eBqiSXDgZ-lw65rOybp_IjeEngVbMDp2D5eL-ODItdu0hAxiqCOBWvPP_pGvSsDh9N6eFGE3HK22xLZ5O6VR3uk6g-xEj7_4VTDQC-QIAHsDb6U_X1sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eBC_I-MS_q9X607CjK4OUmKGPUSHVUtAsjiNoAmnFMIwcT1Hci05tKSEQPYX2SzEH2GKoZ5xTqlOxyLBe6st6oYDYUKF3cO2Da82GiZBX3PmMYFNrsljXFtt789eN4vokwLRC6fqOm-nCLD9nL5LmfSyIrsmyYOXwTzTnHicVYfr2XDwAFepFvFcXcTFOCoVQU4ixokxk8ouMD_WMNs5zuStS5EpfY3fBqoiGbwrs4pbPED0mKEGLWW4qs8u1Vp53nH0cgo0eoZdxyQ47cPo9Fw7hZwASha5Z6cRIvCAcXIP0fE9y-vDQuebCpBhlZMORkyHwPU_MjgXNZxt-aTxeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jp3Qa2DEShpvdm17twuIlyOeZuKpdFGGeIBMXtCXZEJIL_AEdyz4Gbpwv5kKxKsNhtgtAvdRgATENj7GYV5Tob3E78JV2xlRBwN0e9N_0Y70ncua4hyHXxWg5RYf75fjaQAQssys5Qn8K0thNmSAdJLrvkNPs4P07pfLsFENBjgamHDLIYxYe44jSzaNcvOgNKLLyBwMA4QCBGK9K5npr59iZn3qHHhOSJphI721t-yM5R3gg2jA9hYale8tl5JSDbtJA60LfgEpHHQfNGPCZDU5RLRflCVNwMOMM5tGNBha6FpTI5dFv5uMPqhcM2r83tFv8RdQb5ptC91dGxXecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=TsuCL6HB--Oqjx_Efz1odJM91iPyAKsdzkJ084TBJohkbdN9zNA16yYFUshXeq8gsGpg6BYMOVFfWzhPGBDK_O6untt82jWCDosqnmkVZyicrzwYV57bTqhpQSPmUJLbA2_cAktFYRfBmSW-Ymj1ntkfFNRvrFCSBw85DJW3mpRkCYmEsuSmYphOdlzmO-NNorfwhFWF696S7i6-VKEFn82qG5K2vNTwelUozQfxrq9L5qRSEiHUvwvFAB_o34CfSVm7HdCvWW6rPeongVDPNkHkgtPS_BqwhwCD_WXRGH7yFnt4_yHFIu93DgI6TrguL42xyiwBprpAC0EL6MimmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=TsuCL6HB--Oqjx_Efz1odJM91iPyAKsdzkJ084TBJohkbdN9zNA16yYFUshXeq8gsGpg6BYMOVFfWzhPGBDK_O6untt82jWCDosqnmkVZyicrzwYV57bTqhpQSPmUJLbA2_cAktFYRfBmSW-Ymj1ntkfFNRvrFCSBw85DJW3mpRkCYmEsuSmYphOdlzmO-NNorfwhFWF696S7i6-VKEFn82qG5K2vNTwelUozQfxrq9L5qRSEiHUvwvFAB_o34CfSVm7HdCvWW6rPeongVDPNkHkgtPS_BqwhwCD_WXRGH7yFnt4_yHFIu93DgI6TrguL42xyiwBprpAC0EL6MimmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DlGlzvsx-vwErm8M6wbPSsYMBu2Wpl8xmaPJZa-2X61HdfLMvXFbAgJrWd0b39v74LlSQthq0Y4Eu6I5dEeZP3qpEtI3QlCf-2nt1HIXqdRB7tt61jd9sgt8VZPy45QctO7pX9nmkSNpuzsFTDwUW3v3gjzykNU9wXuu7D4S_3XPaz_7HTdj2p0dkNtv_UZG-8QdJIL_mDgHLuwc90iF234itYQnxmz6JcubcFPhr_tmwP07Jgs7xIepGRvwVe1iLEmuCekFqR1Qkmd8SqjMMavdx4XSkjD7HPgGzOpcdGLKzGJPfGrsRZTSKZz69oTJ_RYmh5hyDGYyJ5aPxO_BeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jspNGV6H4KVTcDAHRm_dSLOBlDmTt4jotwcrF5Gc7yCROXjPdQGv7XJxbi0E8hDhxb9hnjUsRPYs8oYKXRRsnuKVD5Ve9ocd72hFbLiEIltcR-Mq2-rwSuuhm-qmyIeS2RpYfFWLymoOSVAD95gmP4LLD06-Cf6JryZmOOt04nUZuDgeIYCu6CAPni3tTppYAPtQgKQ5NxmWUsg8ik1X5ElwsNgTWPg5BlEwj9824Z6Qeqc6sqoJW6YUuVHnUfTkxBuWVOH6KujvkHr2THeNI65h_9czCPFAGqBWKc4LWtSQrmHXaXJ_NuNA8Q4VxS-DMPcjrte8C6yWrzIe6EopmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DqTvdnWfRe3bpv9ZkyLJWI7jiPEzpUeRj4gB_ahLtJY7IfwUtKb6ZxWv5ekK6ENzJ-rVbKFT-L-opZ04LkIq4C8rp3hGTay3sNa8-Wxct5wy1NfZ6CO2tLHhF8Y0QDNvYf6rayJfgObSrktLdslugq61au05stSrVmoxuOb0fjWXYim07EIFI8oZ3UbVqyeB2TSR1IlWNh42Zy2ZZpzhw0ZFG22VGn5qgNhEHGX3Uu3LGcB6NZQrnjcSbshOQy-vqe-VEltIZT4WPWqR4ksXHCf9oWfjTwrMxIOrZFJTOr3r6Sp1uGC6zxL9g8gcIY4BXmoxPnSBWin_BqvJA2ld9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hnAV4QPyoy7i9zn0ffwx9XoasfXdvj3R6qWbU6ZaE_Ms40MJnkWmOBduUA4JBcZAIHDSYJq7JwTrHyplc4KkplCY2iuvSx1_e1KkZ3DJZVCE9cTpamLfTjWAUENncEqLCySzvKMVcDWcpdmWXkjFkVkegiPAKxldHWxSAVJ2vr5aFiUm_dG5DvUGiH_uk-ita5PXV0zOhb5HPJ-NlZslPC7aexn4ChiGwi3xPVFA59gdqZ1ejKqYp3D8OsAB5s7s6XKVLfehHSRDVxjft4qPem_ma0BfwTSDGPYB2waJZySdGKsKuEghWOI0Ft4XP7aWe56VJj2jik3TvTz6KD0ysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RiAC1Hjq6SCBwMnjAqLpO5QzMk3DiIqNM3xyASQmvzUbQgHD7HiTnCO6ikXgVIDqH9AN12J_rUAYHxUgpgr-oZGUVi_aprsFtZpCE_zP9c5BFGmaPuhSBkLQTgvSIJyvRKeogE9b8E7xG7CsdyovBN50zZaLtCyfANER-3KmAHa6QI_z6NAY6qGni0YOj8sU2iQZ9lSvntuqAM51O7_pVcZzPb-4SimyI2IFtMWWO_qGz7TDx2TyVXKMv8GXCp3L8s2QreY9cQXdFw0ILQOAacZfOQF-Iztg8EzzD5fNRpzW7pQUWDpEFKqzG-4cRzH86y96k7Eoyl9Wl_W7KD9X1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ffDsfCeIJzScutv6q1Gpl561FWmlTIM4gxdqNLFE0QczDxJ8XW_PzVNr-shbCnSqmLCRMckDx2yvCHc4opL-WwAP00viAxNEar6_ONDAcZHtCoi68Pw-ycU57GabL6FNtD0huQOkRBV6a3UaMvz5W3vPLD9e4X5r9SaHJ4EUnMgbO2tH-jdFrGpyyrYSsMc5Nb4sS6asNBKvGZg_8_qsBQJjEUZkVwJ9FGyDxOMI2jwE5vuEt6mgEAJ8zXTikxB8bLREk6ucSyC1Cwv2ZkdntLV7n75-TL3ziLyM6H2F3jQLY3QcYOKOkuWlLbD_ibAyi_WGYyPiyfKEylMlTFQ7xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IsW7VquCnTZJD773AjAp-uqVAJXP2fQp4RDymSoEvFpopIT1DIA80VAnEJdd7c0OTfquOybAYvFKw05kpJQblyPoIsVkHAl2wBxh-dYwEmPv4qLjbkgNJq1Qbe23Ggk2BCveGF4dnJPIO04VIR2U1E287OT7EhMt9KfIAAw9xYunkm8ypmTxtdnGMAOvj1mBY4q1CwaJSXTv_TZCn_ug7JA4sRjWsHQBFRzhdjRhAfYYKw2KitShu7Zl7lOxcTjjlEM-ClePrDKpOOmQjsk1j_8fD_sg0cdyWd1vjupJ_2_F9UvtWLfwX5SkhxCkZoh6h3g6i37scijOFy2FXtN6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c8BptDlHruzqaY7ZLCyGV0NIbkFkIjSIpCCr7xC66KwYJHOpGR7haAZpr-vzXXJtqzc_1EK-2X62AT6j47y_E3eX5DTNSXhldBECJGe37iE4uM6LObserlePIQbePyME2sq9I_5etXhOwq-dQFM12En72YWR9ppt542Wr8eTw0AqQrj6V71X34HEBj4PSfmRdQ4EIf30KxGHSjGob8zvfIS9aqpKZxP0gBXFX_ND0WcSfJSLyezLw9yXvoyamViuuhvG9k5vafFQdE6eSoA_qnipRa5a0DyoMu-4zMUFIsM6W4DXXkkN0Gzcp7NOh7Ceu6VPLbdGKo_hnn3Gtoihqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cbjCHd8mSD3iQ66SMYiI0x5MkAeaSiU7VN4rGGQC4bv79mFcs0pOXwvEBcJNeYkyvCt3_Ro9tC075_vEYYK3WKTVTw3_YkihPtgtapqBY7_sQMGL5HM7-0hg7Lw_8kWY1jJucy3ypotgMmC5MOlMP4jC5hDAmnBrTYWPyQhPNp6Bc7yqtwLd4s1gGJxPnaTr5OE0ekyOzSvocnr1C-fx4m1ToOdD_WcyrmxF9ClMMD32mo3ZsNHCut6ruVcoMsvhFdow6dh1A8zExNbLORLgIUaUXBVS-t6b25hD5UItxJLcOEO-KLX1Lnl-ugqpyiJ6McwypSb-0phZF3AsoD-MZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/p-F_LHhuG-T6h8W5WIO0rv0Zh2qjeLcUB9GJbVFqhm1jDOax-pbUMx6xKoGI7JHCfkSUDkMvlc-eiiS8OamrH6P6k48z8Y5s0Ammiv1nQoD2GB3if6AqCg3wYOoeWN-g3v22k53w844nlMlVXX0WDHvYViIfaAXLXvpFIBsQa4EPa22w7s32rX6YkoKkS0newa-3ts9CXKMlVCjMNaWjbH8Quhi65OFLtWcBIUjbY6LL_4KvRaS3ZYugXut4r2oy-aiz5tdGRzc2QSy0GZdygI5ENcM_16TMFb4pAzsDmK-uhKF5Po1-82OSQ8368szTpgZgz4dYnLOvs5iuOvpZ0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/soSwl7d64g6BIxwsnSgvUsw-KvYGPetRguYWCbTNfxm-FUnn3jydMqH45DIDd95o17d0a9mzFp-vd0_mBZdOOHTho19E9Qf6VaY0GI_UO5Oxo-gReT3kg8q1gwoJxPZjBJxx-D7GAKg1l30O2T5ccwa8hyZe2HJImEsLZm7hH0Uuu20sBqao5Gav_OT5JKsr6kZEWGsJF-gzIaAB7sv-RPmJCt98QvjipRpVC9gTzeQAoxqlxGTzkwzJwtZPC6_eOzzfT6vIYM5d3XWHc9Ov_bN8p4RQNy32SKDZMxdgW-kMV1hdmVExnMS9lrSV1PBTt7UN5ORXhEYuIbv_x6XUQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K5EnAkzJHPBRTAQe-UAjtXKcA1ZZkVaPM2NUpC_duwbWWfeGSY2zSFxiLC8yMHOMpsSROSg2x2rFfuc5TvqFcst92EOD7YqlCcQRtfsXp16eIbC36JvZPnWkSzRjWMlfFCK63ZDBAk6k74cnpH-N_lZKHL0vUhCYL4aGRC2VyRXGYc2wKn3Qg2C_cTv6p5oSOiNDMzf00FO6PrZifaOLZQyCtQm4-lzazyZY5rvpoyaiLWXqH449fIeennopwmGf_1h0ftzj27L400_ypWwR3uGL410l8tNeJ_usKa3s-ZrLCsNW_UpCwaBBwbbRkEr8Yh4voy9gqmMC315jCAc6iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HZNv_7eJEa6WMgUS_Fzo3iiVlfdcRyUcMOZ7bYrSDpJ_Xtd2ZZOM3cePIyw33tzpjNfGcAI2lOqNFpkxHa_Eu0vARgYO8F-KahPUTzhTj1baU5_JJsC9p2io0_RgInWa2OpicZTVCRqHFNwso2dJSF4S8Hi2P0zwJ3a-fKuSYe1CqHWWKIs4ifEnMQxQ2BVEeiTbixPBXDHT2upKRhgHqQ7U9BYU51Z6z4Tjg-wA17h1rEUaNd5DAo60aR5znyR90eVDqJWC5ifeu1d5De9DTQULFeh69KDMlZrtKy_ueUxJ6-pVjtu_azGicEwErpZyn3y9H33NghuqaALI4XiBaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QUCY8tTdRvbTHpcB4gKgnFodQ79P_7GhlPlZifBX26lGkx0Dr304NfSzRur6cy498DOtRv39Q3vJf48gxjw4YahgKKSA3s5L1bUEmCc4hFDGT1PUeJFg7YdbukM1L6Q-KybN9GjgA2H8AX7TXYahVBCO2dkzLU0yi2Mv6Orao2BA2blcymGak9cikFUcVwfVhsq8Scuz0JhsiKnVZlBj_C2RvAB4QPYMQiQJICmUJXAfMehJncJYJj_ZogxRkS9Y-Dm1BxFyWc-Ic9N1NmwySbllq9K-nGzM6BT6Tsc33aMYwjTKmLXCEbzIy7n5StC-x6MTMP7c-xtoAZnBzzp8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bTdENQbz76a9EtM5T6Do7XRlv9zRG1aUXt4IV2347p8h9yNGUJKRJfrptjQKhXyLDGZGmV2AwnDutycxBAwVmwZPUlmcaiZoYnbzmCzeXHpWjPRP9NwY7roYxMjvp3EBTZBOe8oyQe1F463EPs2VQ2SAaQMmBWRpkz6nd7g_4vvgRLdQ6dI6Gtb1I15KTwtTohsLhfWCrrvCJ0YUmHfW7WcDch6RctCj4phxrSxL20lNrV6mbQ3xnQjzT-o0hHtQfpxdb-80TTSj3mINVfZopQIrdg6EphTK4JFQptSWJdHwpTYK3vjbDwOngwVVxE8CxzOP7ThtaeBh_ye6dhWtlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cykznz6-ucobRM2yk5dBjgJr1zr19w1c6zjhQLZQwrQcN5ih4gEwrvnzE0n4V4AwmP24uFpu1SBR72HdQF7HQ3MCqtb654t9nhJ3xpPu1-hoEv72xx2c3qtLt5vBnTN56KR0ROQSK8mIosQyE0wJAmMFGUaJA-AW6ikecdl_ZkMUUbCMacDJ8vcllctUiB6bV-lbtbuzxZs19fmS6u4s7s_iihUPLS5w1xhwgwnUQAR2TsuDM51GBjQZPk8zEWNyKXc-lsLDccDuKLP_GiIL43141I5iRLNLSk0UnD7FinyB3BMmi5fxy-3nZEx3MQuKw33Kl7tZbKGObWKCpLqxiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قدرتمندتر از Fable 5 ولی رایگان! مدل مرموز Ox Alpha
توی این ویدئو رفتیم سراغ مدل مرموز Ox Alpha و اون پروژه‌ای که توی ویدئوی قبلی زدیم رو ارتقا میدیم باهاش! این مدل، به تازگی اومده و یه مدل مرموزه که هنوز اعلام نشده مال کدوم شرکته، اما بررسی و تحلیل می‌کنیم که مال کجا می‌تونه باشه. و همینطور بهتون میگم که چطور می‌تونید رایگان ازش استفاده کنید و کد بزنید
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5049" target="_blank">📅 00:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوستان من کمی از لحاظ جسمی مشکل برام به وجود اومده بود. الان رو به راهم
سعی می‌کنم ویدئوی x alpha رو زودتر بذارم
❤️</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/MatinSenPaii/5048" target="_blank">📅 22:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">و خب من نظرم اینه که، Train بشه که بشه:)) مدل‌های قوی‌تر، ارزونتری که الان هستن و داریم ازشون استفاده می‌کنیم، بخشیش از همین طریق قدرتمندتر شدن
ولی خب شما باز اگر نگران «حریم خصوصی» هستید، دور چین و مدل رایگان و contributer رو خط بکشید</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5047" target="_blank">📅 11:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">به خاطر جالب بودن این پیشرفتش فرستادم. وگرنه به نظرم این نگرانی تا حدودی بی‌مورده.
زمانی که از مدل چینی/رایگان استفاده می‌کنیم، عملا داریم امضا میکنیم که از دیتامون استفاده بشه واسه‌ی Train کردن مدل.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/MatinSenPaii/5046" target="_blank">📅 11:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=SSgGPcU53aCD36MeoC8YAA3CkfezfsEPsip7U6GrOT2TQSepvAff1XorvwLAe3q4hWXeSvfdWiuch7Y4JvRrXgflbJkt40dXn-76Nl_pz_0aUGFw4BIFSUQgDuVYxM2aEIeaPDAkVAc9bPP5AkOZYBWLKFikwlVEzICO3Bav2FkkEmoZsflTUVgHAikCVyhwNoP4AVHK1Hz_Hgh8c6ZeNujz9cwEXrcobOvoAJs9w9PlVcctIpr_6cU-BSsXJ-vzmUbmbulyrsvAGA2xpTjasG9SLnYegPUbbhdVNxjNvtI9kke6PYkgGOxbwNW_a58niL5g1UFzRnK8lvIIx-P5vRxhJ6xS06ZaGVAfK1GrXSg3rjXSDsuSBuW3jfPq35sJzL_WaDvhyyywNf-OAE5HmQlHc3UCHcPMx7laiXMEQm8UzwHRhG2JhVInYgGlV4zIu_NZRyvvISZbDUPN6Fr5O3GnNF4T-ng8fy_K7i4CLlg2J2UCm-AhlNi8P7xG41_W1Ljkl2b7cbSDZWykTeAh8mJsXMm6tiC_CD7MvWJbsoRKoBHHDMpnRP5rQs-JA459cT-guIWqO72JDdA65NgeAGcwJoQgdcoQVzVU70H0efmTk1riJdZb31QB-Stsk-dIi2VKJq5VENvq0yNsiqi6ngsVUngP505p7w5nMGF88ko" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6f33bcf78a.mp4?token=SSgGPcU53aCD36MeoC8YAA3CkfezfsEPsip7U6GrOT2TQSepvAff1XorvwLAe3q4hWXeSvfdWiuch7Y4JvRrXgflbJkt40dXn-76Nl_pz_0aUGFw4BIFSUQgDuVYxM2aEIeaPDAkVAc9bPP5AkOZYBWLKFikwlVEzICO3Bav2FkkEmoZsflTUVgHAikCVyhwNoP4AVHK1Hz_Hgh8c6ZeNujz9cwEXrcobOvoAJs9w9PlVcctIpr_6cU-BSsXJ-vzmUbmbulyrsvAGA2xpTjasG9SLnYegPUbbhdVNxjNvtI9kke6PYkgGOxbwNW_a58niL5g1UFzRnK8lvIIx-P5vRxhJ6xS06ZaGVAfK1GrXSg3rjXSDsuSBuW3jfPq35sJzL_WaDvhyyywNf-OAE5HmQlHc3UCHcPMx7laiXMEQm8UzwHRhG2JhVInYgGlV4zIu_NZRyvvISZbDUPN6Fr5O3GnNF4T-ng8fy_K7i4CLlg2J2UCm-AhlNi8P7xG41_W1Ljkl2b7cbSDZWykTeAh8mJsXMm6tiC_CD7MvWJbsoRKoBHHDMpnRP5rQs-JA459cT-guIWqO72JDdA65NgeAGcwJoQgdcoQVzVU70H0efmTk1riJdZb31QB-Stsk-dIi2VKJq5VENvq0yNsiqi6ngsVUngP505p7w5nMGF88ko" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/MatinSenPaii/5045" target="_blank">📅 11:21 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/MatinSenPaii/5043" target="_blank">📅 22:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ما الان داریم دقیقا مسیر ونزوئلا رو میریم.</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/MatinSenPaii/5042" target="_blank">📅 20:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">راستی بچه‌ها پلن 5 دلاری OpenCode Go رو من با همین روش گرفتم. اگر که خواستید بگیرید میتونید به GLM 5.3 و اینها دسترسی داشته باشید به ارزش 60 دلار مجموعا: https://t.me/MatinSenPaii/4915</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/MatinSenPaii/5041" target="_blank">📅 19:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">روش پرداخت بین‌المللی و گرفتن Visa Card مجازی  خب دوستان، امروز می‌خوام بهتون یاد بدم چطوری می‌تونید با این وبسایت، برای خودتون ویزا کارت بگیرید: https://app.mpay.cards?startapp=ref_PzwXZ8 (لینک رفرال هست. می‌تونید آخرش رو پاک کنید اگر دوست نداشتید) 1- بعد…</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/MatinSenPaii/5040" target="_blank">📅 18:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/MatinSenPaii/5039" target="_blank">📅 18:19 · 02 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MMjCFqd6HraA0JPW8-1D2WzLkuF0vnpy8T_R2Hkoo_EWrOIpjwgBFgrrpG9H9PBy6VfL-UMR8MqRj3Kowy2JhmImaUCjR2__wyQKG5-lYlSfosNysqCWaimQBsjLB0taErg7U9AgT9Z-Rj7y6oWJ3mTfRum24yb0jG_yf5IPhFTmhvLA4T4R5cCI_2OA8R1YPjjIRJPBLYLzxIQbmFwbCCvK7Rd209U86JohOGbgFNJDH3sQHkguMUcob33h4l8tb-58c31PaPpOORTVljYm1mh4tQqkzVsK0uIbJlCSUpyCd-GRFD9WJ9MYMPTEX3bHzUF7rk1ymHE09Pd7yZM62w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
آموزش OpenCode، رقیب رایگان Claude Code
☀️
⭐️
توی این ویدئو: 1- با همدیگه OpenCode رو نصب می‌کنیم(کاملا رایگانه امکاناتش و اوپن سورسه) 2- طرز استفاده ازش رو یاد میگیریم و بهتون میگم کجاها خوبه ازش استفاده کنید 3- یه چیز مسخره با میمو می‌نویسیم(توی ویدئوی…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/MatinSenPaii/5037" target="_blank">📅 18:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tuZBOHVsaFxbsB9f98AkBlZzdHJvYKMOHILqATm5yF0tXPxE2b2E3L8WpY15rEa7S9ylh1Qtb__1jTkvB8RlR7uWyczbWaun7Dfw34ZGC8BvmnYEAhF9dii9RZjzG-LACLwNiJC_-GELZvFRpaHEOLXQ_5D0fgDWa4jpHPUw_PvV17KNtLi3wJIh8xGm7ugaXOzJDWnbaVYyYBtAUkn1n1xF8IPEWjR89xHFpY08fcncPfr2IHXPLfnzGLm0_1Dz2RVPqSmej4gwyuMuYGyqBu7cepOHjFoglYzEDCfGk5tYSvL4rhjrboKmWXsGboQVFZZh-OMPr57Qc7cFJ_De4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/MatinSenPaii/5036" target="_blank">📅 17:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5035" target="_blank">📅 17:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تموم نشو x alpha
💔</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/MatinSenPaii/5034" target="_blank">📅 17:09 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/MatinSenPaii/5032" target="_blank">📅 01:36 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یه ویدئو داریم واسه Open Code
داخلش یه پلنر ساده می‌نویسیم با Mimo
توی ویدئوی بعدی که پشت سرش میاد، میدم به X Alpha و اصلا یه چیز عجیب غریبی زد.
موندم که واقعا این مدل مال کیه</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/5031" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/MatinSenPaii/5030" target="_blank">📅 20:17 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دلار 200 رو هم رد کرد
ولی نکته‌ی دردناک اینجاست که هرچی جنس می‌خریدیم تا الان با دلار بالای 200 بوده قیمتش
الان قراره حتی بدتر هم بشه</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5029" target="_blank">📅 20:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7dqD1LGYds1EcazyxkaRG0E9InQPgE6uqHLnZQxasiHkBzEv2GX9uQUvXtVBUmgXs1O_zWVUb85psRsek2QlB4BBHGZV8GAlPIuotsDPO5vUbjiOonoBKrz-3yZ_dsG3hdGaY1_LLMjPj2-MsErm1gkRpy_Y1h0VEDyShbS23Q_iAE8vMYTj8Q7mLVTXrhR3ZW7sX2Fl9DGgOJx0srtbYlGa2lYE9tgAioRaq_ALMU1X6d6M6SPBFiWeKSYY9cp1LSwjsD1bxPXpeXyyE4f_4t9cOnBtIOYjV_BuFP50DnZ4RLLS-PFYO01LuQfpUdyqZVHeusgVrnmcwgyXKtKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسیدم ۲۰۰۰
تا الان ۳۰۰ هزارتا امتیاز
دو برابر بشه میفتیم زیر ۱۰۰۰
❤️</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5028" target="_blank">📅 19:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C-wIIU5GOmPm2E5_DDbEd3qcLpdCnILNNppbmS9xrjC04vJLikYYiD-H_MliiGLGF7oJ3AboLf3jk1NS9RbE0L6KWS9Z8Oe9tcNpp4ftMSMrR_DUmgTqGuB7haaFsgF7IcXK7fQw4F5YW5L9aFDB_eCZfwH3VHHvyhiITg-WKnLh7osoCw39UBmrp1c56lshC8dv118CnTWPMNMyQc265Gqh6roN6Z_RkxHDoWJnqK6NvYZzqAVqiA67s0CPPNFsPCkbtWDpVUirYi70VRnfXo7O88no3TTEY5n_zhiMkF02ts0IOoDyLK_3IVqPU6ca__3y76qY-p2kNitH_XcNTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DESdx7AkvPFuACjLMfyHEJeO1--UuvwZ3BvnDFgagZ7HDhuxwNsp5bdyN86iC95V7siFKFHXP0T_0CPQ7skmfqveJ09oQgzYESoJw25ZieUSrDXhLWq4n5pOjWWu2Qn4FqYln8F1FFG74xp5zP5Q0dvp6kLHWzwRdvmth2rYnsdBFtI0DPH3S7Hy11nFd51I9odaK5FeYI4Sq2XCjAYk6xrdUzVVeplDZt8NP1jiGxM2N7aHo5kWV-x7vp4VPQNbw7TktYRM_k96KffislCgLfdjrZpRXPfslUowMIO2jiSCtPQA7rbBX5q6_nfR6Mkg0QdH4GHJMO5WH2foD2yGVw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FPcIXTdl4-PaXqiAKTmjCP8VbQxXEJWGeBCtVwve6PSx1NTZkb33TEjiXAT9iGeg0pSoveuTgF8GKG2pmImjOFVK-d1wdB4dwcWjDzc8hG3hx-7UFl_pEkNAfYHt8pT-VqJbVtWegFzik7oHiNz-oRspgTJbr6Kn4j-5u0muDZhS1z11AOhbXh35cnCQjtPMnPp1-iwTN7xif64HFh_3m1CbBBGCArm3m-UEQ3ZfrmlIrKyTQdS9lbR76iYir6YeX6OKLTc-sFYvJLroQWDiawDQBO2-sVyiqJsPPdIZQI8ntTrgPHD52y8D_GsxaAqWhWo7IvJICM63y4ofk4W5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا چند ساعت خوابیدما دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5025" target="_blank">📅 16:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1357719d90.webm?token=QUl_Vs9xBhWG9ly-5Ki5BBd5hRWTacx4vL4NcrrJJUp3JkWAUIM0hi4ym-yMWEymT6KqNbm7V1ukm0Y8r9ZTA_pcXqxLF6g-_8_OR8PADXrgT_GIBkQKYkzUB5vIL9Mr7UAXTDCoW_VJjW5U5GCq0y724qW9GPgLxnOCM1MtWsoYKDIPLqxmCw-8qILE7D0FumeDcMU8SbX7BN9Pj-bAm9J9WxzlHYpUrqEiLafsujgVcd3OvyVOWuHetZfnGtgAi7XET4Uqyf-XJHI9fZbQy_hn2jCvk5rJJ8vFMgqcW39F8wSZIhcYQFKLH_hGmRpZg2A1BBHSluimlnrF8ePZoA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1357719d90.webm?token=QUl_Vs9xBhWG9ly-5Ki5BBd5hRWTacx4vL4NcrrJJUp3JkWAUIM0hi4ym-yMWEymT6KqNbm7V1ukm0Y8r9ZTA_pcXqxLF6g-_8_OR8PADXrgT_GIBkQKYkzUB5vIL9Mr7UAXTDCoW_VJjW5U5GCq0y724qW9GPgLxnOCM1MtWsoYKDIPLqxmCw-8qILE7D0FumeDcMU8SbX7BN9Pj-bAm9J9WxzlHYpUrqEiLafsujgVcd3OvyVOWuHetZfnGtgAi7XET4Uqyf-XJHI9fZbQy_hn2jCvk5rJJ8vFMgqcW39F8wSZIhcYQFKLH_hGmRpZg2A1BBHSluimlnrF8ePZoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5024" target="_blank">📅 16:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">به خدا چند ساعت خوابیدما
دلار کی شد ۱۹۷</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5023" target="_blank">📅 16:25 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
