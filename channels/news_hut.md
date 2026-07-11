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
<img src="https://cdn4.telesco.pe/file/tqyPWGgS29dBqWB_cTpsyJeCKGnSmYnqJUY7dm68an3Yvw_gsguum4DbR6seRAcB7lMzB-eAiRQU7PgmyKfPLjo4oExLBH5KPKsFFCmhc-L1PK4-8O99kf4dxtHeTbaM7Px9FJ-RgjybB_7Et_oJsNmzGVaZqhhGn3qLpVWeFjGqfSn4rRTnDy9g_n25Hv1_xI5U_MNWrEnps7wo7QVEyBOu8-jOS6VzKhDpb2zgyKrqmHIksFyJ_1DAnqyYOSMpXPmmVe9GRW1yzbFppZS0nosustvNTnqRLNKJ7aUy0rwaLkZ2fyHWOFcwI_Ju4Lwoa-Bzc862PgU6vuVpPPmQUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 182K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 01:10:23</div>
<hr>

<div class="tg-post" id="msg-67815">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m2G5aJQs4QaiXU8alxvk9Iix16QFXcbj_Ueud_zKejfd6QKzTfNSR3EKfa5hBwK-OHyA6RjG1qzs4koqjzj5LLs3e2U-IzuiYXYpPGErgy6IMGXgzj1fwNpNuh8Cplo9qXKepE9I4eN8BOukm4sE0HXHqyIyjcfBuDUegDbAFRiyDeL-Zst-xGS68XpCdC3iq34VDON7AdOk3w6yBlYfhYmB8I9c85QdTg49qt_M8CC5PMas2k4AvZgeX0ZIqg8TUxvlKVzJZA6MYl1oykzQHUw9gv4N0yDwRqf4upSLcBAga7m_b10FaLcb6Jt3g1rrdUbgYIrLT-WUQtiaVWsNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTDRD5hbtc3zNuLXNIQ81luRd2GpWSl1DSC9s6Y4FNT-XotQuaSsOgMfU7KMs_LXzGYeR-DyKZjuBFcHLCxkiEdujQnfMqRkp6C5J_pGIdeUdnWqBHMG06BpmsEi358IUlN40AnN_-V-XtdJVzNSEuFJ8J9cKCbGcccALd3MqhO93gh8X6CA9TGqFgBJs2msd77zIcClOzlII4No8A94QOck-JsFM0ljKl2X3QS2E9Zry3D3K-5kxpLqU6fIGoa7FAfxqnhve9apCbFpMnxnzjzPaw8_WWxPRrsAm_7f5YcRz9ezZ312qkNzeICnTdh2Hlpnaa62ssGUO8PORLfdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVKeY4sg-BMnG02YajuWP7rt8xIVunozg9AtxXY9pgo7FXCWSAKtKbCzPM3w5t8I0y5FxFc-mk1YBxAJ6x5ZglCMUw4VKcdkbAZxPomPyVfq7ZHjvIBdRvj3SmaR0tAIuFt2W2PzKONqN_Q9kAgL9wuFYo2CzUAQakLNGTux_ynDvIlDvrHeyIQLmsOaipRrZN8ONk2mVfQSo8sHkvIXfFZLbS2AbKq3TV43ezIAOeZrUQ9frOZiqetl0WHsBkLRoxlhoJ3CWbdmSEoHbD374AtO4HYgkxw-LETie9ZOVmwCkcaLouFppflsdiUbVPixYidyyK7EXeXzRpi0LmKiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMfapwhErKQLP4ZuV79kj594HvL44AfID_Kh2Db4g0anGBf6Y3JLTM5oO6uKasq1wQUozLIPBsgevV3rkcWnbvtzqqBD2Wh05Ywzl9yfm7jUvmRh1s6HwrrDLk5EFC4rvpGifKpmqx9Zs_XBSxEhD3L0hsbiwf3SQmFAZLD6M8a6kmZ-_EGrBCLRIenIW5PlyVw_ah2B16k0XvYPZlYHrzTCc4w6sqL_iOaf3CECrJdG6eqKzx-ujdAcPaBKaIgrgJcaM7Eac0orJ1GFzzzgVIYzJJm8h4zWSLNwDIR6etpR45wGfr_MXLK_O2Q3SXa5npymA8B8Jj_vR9PoRmdknQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
هواپیماهای باری نظامی آمریکایی از نوع C-17 در سه پایگاه نظامی که توسط ایالات متحده در داخل اردن اداره می‌شوند، فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/news_hut/67815" target="_blank">📅 00:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67814">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=humdFprYduvy1vLGanHwNISfP30MoesgUBcPHAQeyh7JD2Yj_Ay7InJMlmDQohNRmcAynOkPyYaKyjpAIKWkqD3L2Zm2Bf2Thy4_IdYQuc6O24bMVjlh11cezP0Nht3SntdRa1wv4CbDEqRhkVLpvtVZp1ooYznszwQSZQoyBDWkVyuz2bv1G35KOenHrK2prPhPF5NispMJHuDqDV_W7i4hXHwsFtH06x_gVqAleCH3ElrD8NuITNG1_yN1xEHSh5iWkh-AuohvzvtJ6LcWcc5aNmQH2Okn3TbgCszPknTg31wNnqcnq8OlapSF6sCM9FamX7Rtc6xo2kYImVkfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=humdFprYduvy1vLGanHwNISfP30MoesgUBcPHAQeyh7JD2Yj_Ay7InJMlmDQohNRmcAynOkPyYaKyjpAIKWkqD3L2Zm2Bf2Thy4_IdYQuc6O24bMVjlh11cezP0Nht3SntdRa1wv4CbDEqRhkVLpvtVZp1ooYznszwQSZQoyBDWkVyuz2bv1G35KOenHrK2prPhPF5NispMJHuDqDV_W7i4hXHwsFtH06x_gVqAleCH3ElrD8NuITNG1_yN1xEHSh5iWkh-AuohvzvtJ6LcWcc5aNmQH2Okn3TbgCszPknTg31wNnqcnq8OlapSF6sCM9FamX7Rtc6xo2kYImVkfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک پسر هیجده ساله یه رولزرویس رو یک روز بعد از ترخیص شدنش از رو کفی دزدیده
یعنی رولزرویس رو تریلی ماشین‌بر بوده این با هیجده سال سن اومده دزدیدتش.
@News_Hut</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/news_hut/67814" target="_blank">📅 00:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67813">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTwwQCV3_97xVktyLNW26IMNq9JqI-FofyvrCtrmglRhuGnFav_8C_qUynClfyT0NEct5OsazdmEESCWapcNBzRa7bnVyFo3LKp1X7vr_8GvxOovt_nMwN_Vfl26m0E9wykGbRQ04DWOCYRfmNS3VspuoxJgNNyHO3vo__CcceqLgAHB1abXJNTlAqtc__t7y7kKnn-zDMh-PYW00SASW7-Q8G4gDmxMZ-XAVuvmQZVSxLb4GpR0NdL4hWaPL9-Xc_ObJiBHiB-O9Jt-sTfXRBF7b5acr_k8VFMdu2gfB_pOt9GKJpaxyLqG9OLxmbEIJ0Id95oDFiCn4fsd9zKseQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کانال 14 اسرائیل:
اعلامیهٔ مهلت ۲۴ ساعته دولت ترامپ، که روز جمعه، ۱۰ جولای، صادر شد و از ایران خواسته بود تا حملات در تنگه هرمز را متوقف کند و از آزادی تردد کشتی‌ها در این منطقه اطمینان حاصل کند، در ۳ ساعت آینده به پایان می‌رسد.
این توییت دو ساعت قبل زده شده و تقریبا یک ساعت دیگه مهلت یک روزه ترامپ تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/67813" target="_blank">📅 00:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67812">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
🇺🇸
مهلت اعلام‌ شده ترامپ تا پایان روز شنبه به‌وقت شرق آمریکا ادامه داره که میشه حدود ساعت ۷:۳۰ صبح روز یکشنبه به وقت تهران…
تا اون موقع به ایران فرصت داده ترامپ که اعلام بکنه که تنگه هرمز بازه…
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/67812" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67811">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSaeq9_lx3B74WbosOjnaZROFUFG3Wd8VwaIK8oY0sgELkMs6mVFQ2D8MVokOal1tv2sv9UaCcrQgHLsVGju3dOR3NfMsL-IO7703kbrih1IrdhBg5Zsf2l4jUeNkARFao8ARMOSSxCeCFl8HPxZ7nCVeMWMHR7nP-p_qMO7oJiWm15txI4DWB4hTmqLwnoaB1cwj9heRHl9JEjxiJHWLOOMo7XBC5SdGdVmIgU7E9bf3KsV8KcmJyi40aMHcm-Dmhj4C8Pemj1DseIBjfaZSm_gPB5fohqMK7XcmILKrJ1ZeMiEs4_r6HGgEeZx8REZL3TffJM5zx-s-lsvKW4I4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پویان مختاری گرداننده‌ی سایت های قمار که خودشو مخالف شاهزاده رضا پهلوی جلوه داده بود و معتقد بود عاشق جمهوری اسلامیه؛
امروز صبح ساعت ۶ با هواپیما به فرودگاه امام تهران اومد؛ که توسط وزارت اطلاعات بازداشت و راهی گونی و منتقل به طویله شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67811" target="_blank">📅 23:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67810">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6SQAYQEacjJIYewbt08DmeYsnXCPconFZFu4DaSj2WxAcuwlKJnwGaHhcRF3p-uhZmR6YNn1CSuL5IzMBNH2pnCAWBqhKhKel9jbLwW4D8Vk5zVsRuYQRQIWZWI4AnhIOfyIJQvKE4Lv3n_rWE9CWfew-Gj_36I2X6UV2SD3vE9eRPDJciU5GDhduyDBCGdkva2l4e7SebSAPr3LKCXBVC4DhRlxxUqPIjz586yyZ9YuFzSP7xQQRKeEESIbgIoK5UzM1S8tn_MqwwMQK2w9J8Qleataxjx3RH17nXSz86_l0yF7iSYKuyJFptSwFwCeXObtVySDBupuOV0RK4pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی قلهکی:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67810" target="_blank">📅 23:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67809">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
اکسیوس:
ایران نتوانست در این جلسه، موافقت عمان با این پیشنهاد را جلب کند و مجبور شد این پیشنهاد را برای بحث و بررسی داخلی در تهران مطرح کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67809" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67808">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHZbzYSGDz8f-9G5srP9cFpHBl0kBs9jVnTeE_Va4wJjyE9FqWS3UVPYiUMUA_VcpRuG8fvPHjbSfXA9xEELec193cseb37jxJyn9fyIAG0LoKPbjzQbtyyna-wv3Q0vTlnILu4-fh1FJZBlQ4MBYZm4K9HWcDGZHVWPCUl9XPzm3LFNqxVjxa1DrgHNJnx1i6KUXerEUcX2sidmTfavHPfewvGf31blWVS3icn5a6S6k_r_aC9WZcAQKfXzPbhLMdXI0AClY8HAvuoLRGSi4USIqRj34RuiEchm7Ksb6hPvoJnB9XR9f_B1oh671onzjjbGsjQwvi-haJVyeKQfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:عمان پیش نویسی را برای مدیریت کشتیرانی از طریق تنگه هرمز با استفاده از دو کریدور جداگانه کنترل شده تهیه کرده است.
بر اساس این پیشنهاد که هنوز نهایی نشده است، کریدور جنوبی از طریق آب‌های سرزمینی عمان برای کشتیرانی آزاد در شرایط پیش از جنگ باز می‌ماند.
کشتی‌هایی که از کریدور شمالی از طریق آب‌های سرزمینی ایران استفاده می‌کنند، به تایید قبلی تهران نیاز دارند، اگرچه ایران هزینه‌های ترانزیت را تحت ترتیب پیشنهادی اعمال نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67808" target="_blank">📅 22:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67807">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=OCOIYXEXZ1uii4GXh-5RxmTv3g9OqR0AbUrf9hfHSEOjsBkFEtOJDJ_Ew0lWrcRI03zGXAiyKtdPLnIzIf6kxSmOLg2ks5gO9OhrEe_duRUN6DKNHb8QUHPJqxjdXumt2M-7iA7hLWHBCW5lFU9feffh34NPFZn0iO01fN13yG1hii36wFNKnltOLSDNkNqgbZUUYhVWK7cv4QrRISURgabsKOxx3ZX8dHt64Q4tvsJuASOhQ4x7b2CDnDbOKueKtn47DImMvhUyPRPNNFvFDWMStJ4Q_jYuU70apR4HNW0pJRnI9lncmdp66CpU82RkSQRvMMd34BkPpQWzMeUpgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=OCOIYXEXZ1uii4GXh-5RxmTv3g9OqR0AbUrf9hfHSEOjsBkFEtOJDJ_Ew0lWrcRI03zGXAiyKtdPLnIzIf6kxSmOLg2ks5gO9OhrEe_duRUN6DKNHb8QUHPJqxjdXumt2M-7iA7hLWHBCW5lFU9feffh34NPFZn0iO01fN13yG1hii36wFNKnltOLSDNkNqgbZUUYhVWK7cv4QrRISURgabsKOxx3ZX8dHt64Q4tvsJuASOhQ4x7b2CDnDbOKueKtn47DImMvhUyPRPNNFvFDWMStJ4Q_jYuU70apR4HNW0pJRnI9lncmdp66CpU82RkSQRvMMd34BkPpQWzMeUpgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سی‌ان‌ان: برای نخستین بار جزئیاتی از حمله موشکی رژیم جمهوری اسلامی به ناو آبراهام لینکلن منتشر شد
.
شبکه سی‌ان‌ان در گزارشی به موضوع شلیک موشک‌های رژیم جمهوری اسلامی به ناو هواپیمابر یو اس اس آبراهام لینکلن پرداخت و جزئیات تازه‌ای از این رخداد را منتشر کرد.
این گزارش در حالی منتشر می‌شود که تنش‌های نظامی میان واشینگتن و تهران همچنان در سطح بالایی قرار دارد و موضوع امنیت ناوگان آمریکا در منطقه بار دیگر مورد توجه رسانه‌های بین‌المللی قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67807" target="_blank">📅 22:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67806">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
کانال 15 اسرائیلی:
ایالات متحده منتظر پاسخ ایران به درخواست‌هایش مبنی بر توقف حملات به کشتی‌ها در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67806" target="_blank">📅 21:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67804">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=DfTxbI6w8w7m86O-1VOcNeUUd0NXRMnlAk8Ua-Xvek3YQLLD9_XcFWfp-qT6NLxrZtf_qAdyYNq6Y4_-wHEINPUtJFiaEsHAB3-7RaCuuqZhunpVmdbEYtREd6w5JnwKzOG_ZpJNo_iGksz8f5eHZ_yO2-bb_i4laMj_17fE-SBDbR3trLoK8ygvHg4zREW-OC3yaQm3SoAh3uUz1utZm6FWq6Xs97nxgnpPyhh0XRiaFlIkCBPw0t-NWBmmKsIhvC3yvf2V0BIViC8bnm2w583HIcBizCcJSsYPLet7LsMtKVhThMFTnsm8SoRBNdPkF5bIMAYRtx6HMjlu2E6T5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=DfTxbI6w8w7m86O-1VOcNeUUd0NXRMnlAk8Ua-Xvek3YQLLD9_XcFWfp-qT6NLxrZtf_qAdyYNq6Y4_-wHEINPUtJFiaEsHAB3-7RaCuuqZhunpVmdbEYtREd6w5JnwKzOG_ZpJNo_iGksz8f5eHZ_yO2-bb_i4laMj_17fE-SBDbR3trLoK8ygvHg4zREW-OC3yaQm3SoAh3uUz1utZm6FWq6Xs97nxgnpPyhh0XRiaFlIkCBPw0t-NWBmmKsIhvC3yvf2V0BIViC8bnm2w583HIcBizCcJSsYPLet7LsMtKVhThMFTnsm8SoRBNdPkF5bIMAYRtx6HMjlu2E6T5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارتش دفاعی اسرائیل:تروریست‌های حزب‌الله در حال انتقال موشک‌های ضدتانک در داخل منطقه امنیتی در جنوب لبنان بودند.
این تروریست‌ها موشک‌های ضدتانک را به یک ساختمان در آن منطقه منتقل کردند، که نیروهای دفاعی اسرائیل (IDF) آن را از هوا هدف قرار دادند تا این تهدید را از بین ببرند.
پس از این حمله، انفجارهای ثانویه شناسایی شدند که نشان‌دهنده وجود سلاح در داخل ساختمان بود
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67804" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67803">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=qLKniKMiuujJzWRqIcoyi1IhTSj_XJcIIHvVmN19wKB0I7vBM3QfnbcRQlsAOZ4xrkr4qBLxfSxgrVKD_ZFCHQ_3aqMPSMo36bUi2g8bCHjzFqkc1i0sHEVKozHfhWYbW9EKLjm187wlVzLQFIjOhlCQS8LNN9248ohwCDNL3ZPtFpPdyllE0uABtN_KvjTQ7oc6IvENb020LoI87QgqaLtm7LT_VpYrKx9KsPAVB8tZYVAyps8iU006MVQLFZKFPGcBBF4vtEcR-KIz-NQnxW2f9jNVRz6vh0Jc6AMo9TyWmb-n2xDcnv6hm92WX_hwiQJVPAWImGj6aVO3EluKlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=qLKniKMiuujJzWRqIcoyi1IhTSj_XJcIIHvVmN19wKB0I7vBM3QfnbcRQlsAOZ4xrkr4qBLxfSxgrVKD_ZFCHQ_3aqMPSMo36bUi2g8bCHjzFqkc1i0sHEVKozHfhWYbW9EKLjm187wlVzLQFIjOhlCQS8LNN9248ohwCDNL3ZPtFpPdyllE0uABtN_KvjTQ7oc6IvENb020LoI87QgqaLtm7LT_VpYrKx9KsPAVB8tZYVAyps8iU006MVQLFZKFPGcBBF4vtEcR-KIz-NQnxW2f9jNVRz6vh0Jc6AMo9TyWmb-n2xDcnv6hm92WX_hwiQJVPAWImGj6aVO3EluKlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که رسانه جبهه پایداری از تغییر موضع ممد سامتینگ نسبت به مذاکره با آمریکا منتشر و وایرال کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67803" target="_blank">📅 20:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67801">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz47oX4HCwlfkPryYs7n9U5n7J2U5tT5z8Grm_ewaNuF5hMtmAl00JuZl2fxrciAXrnrAxMr_pKAU0psEUwj52obDXIJBFyAZAaloBY0M291PiwLDEHBlD1ym_k7WYaaGttDQwNN9Q11WJSHnGDGnpP3_fchB4LB_Ub0L08AsxZNnyj3MSamSX6FwacP4dNoxxFN58iNLpbaajet-R1cx_GZH-Tthue5ea8V4wzhTqzV_1pxUSXv_LIXrOqN1laRQ3qSxbuAAaNQJ_qXh4ryaSoT2V3xXPvf3iqQJtF6F_lwmk8NIp7QRbg-PcE6_TPCNjeRTGLYMjNdKceDUXu46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQg1odY-yEUCL-LYsgG9F8cquKXFPWK6_PuzMb0zDFsYCpz_xXeg-f6eeJImnXpWffpzKX7H3SQDVAVa3L3I07iT-H79akB-Zf017DsfAQAINwCgv85gXWCQU1bsY3apepDv0LMxY10CS5Xz2J4BEm3A46n33dV_eaEnD6VxsRUXg_LlODD4LpCwGaK6ZDSia0EoM-KtNamBQySeXaTRln6-Cs-Q1k9DkEB9bMvf-LJGt957yefaoBuFebaclFPbq8XiZRGrxDMVd9uEoewT_XdN7mc7JZiAhwiJpvVPHOqSu3FL2yhhss8-plMctu1XLIKt3MEn1UfwkAwsOzjcSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بسیاری از هواپیماهای تانکر سوخت‌رسان آمریکایی از پایگاه هوایی الامیر سلطان در عربستان سعودی خارج می‌شوند. این هواپیماها معمولاً پایگاه‌های خود را در منطقه ترک می‌کنند، زیرا نگران هدف قرار گرفتن توسط دشمن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67801" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67798">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM2TcBq79wEhytebcB7FQbq8WXShpBg9uRIhACJytvxYB_mFT4yNOccNBLQrF8X8A_XhiUlovw7kqkVVFs3GdnRZD2DRq_U7217v4MW7w4lhLtAJ3ZrctoISdWW9XzeGGsrRmsMlnWDv3RAkK2hhvgAGHaIHPQCJc7YhdzLzM16Lb5HShckTZV2zEkyVdsZhYGP-pFSBPglrMJmPx4DCyjjQe-cxewhD6YvKWU9jU7mTfM2vIrGxL8kY-fUS4MgWDyFHUvi0LXabeteImvWbkEt450Z057WCfZVRnYed1fXQSSbvL5VkCyAJul_e0cA5-uQcu6GJEsagrR5hxjNkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
پیش‌بینی نتیجه 2 بازی‌ باقیمانده 1/4 نهایی انجام و در کانال تلگراممون آپلود شده
⏳
🇳🇴
⚔️
‌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
󐁧󐁢󐁥󐁮󐁧󐁿
🇨🇭
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
بت جی‌جی</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67798" target="_blank">📅 19:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67795">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgD_8dv7aLb8S6xzrgq-OFTHueI9s9WVu6uwbWtMcguMQ5wFo7oizJSTq_-lnI_lF7vPGqsZXPlrZBorcGWvNCljQ-IUYFGhFChwsvDRSYXZ14wp-mheXV34YZlpwvGx7xBgrMSCv3rXci-J0h3DLW6we4uEf-kLRLrhbdkIgnaeeXb10dMfK_ra2BfbrNjcB0Wpg03NQZ0bfLaGdFiwYMTkTueyJcv0SjEeaY4bhXdROAhuHoFbvKCuTSPVDZPLvwUfTLV0e0NjiDYXuMJEf8ADzHx_mkEpfGojgPnWQIqI-HzwLmr8ssHRJimgbMRhIDocBFVa9B1sC5fG0xAVlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته یک دیپلمات مطلع، مقامات قطری در حال مشارکت در مذاکرات میان ایران و عمان در مسقط پیرامون تنگه هرمز
هستند.
یک منبع منطقه‌ای اعلام کرد که طرفین در حال گفتگو درباره بیانیه‌ای احتمالی برای بازگشایی کامل «مسیر میانی» در تنگه هرمز (که در آب‌های بین‌المللی واقع شده است) جهت تردد کامل و آزادانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67795" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریاست‌جمهوری core:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67794" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67793">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KySb-tBVe_lgLfk3Q-0xfTvWBdP8P8leVnsU7w-u3CbqrZlIKzDuiCQjF-8F-OGYGTcQ1MtNy62BmfDwVybsDEQ3AXtKtvMGGOESvl3oVhLC65lD-2YHO2HOIMd8A9i5XbapJgTGi9NfZZYK8rWS9mp1zcHeg4QmLQ6glHuonlmLn599BFSdi0aJ1CAemUv1kaTVv1YJhOPmA9tDQ2TCTkSLJ4hlNsuc6lxE0ttnAOpvzTsr_9gVJYq79FX3hAlkHTGSdwIUAjKsAcg-hYmoTN8PCb5PeEAhuOiiIgkfTMS5P91VdsTJV9SOaIJKT9HOyjGVBhp-NrKLbzScItrePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری مهر:
یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67793" target="_blank">📅 17:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67792">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJUvuQzhnslbkp4rMznMiIBNOvAETStYvkvPUQM9veLN0euFmhog0K6I17oR4lV56eC5giZvY-8cU8-uNthIZby3JIkiT0HRiRCFm7wL5z0g1Pb0Qsv9SpTWmptCSz7-m7Y0U0s9k_4Bgw3Xat9ce0wzclHdPRW2fV5FBfroRzjQHbnTO83cxboe5liifN2xsLG2iugynAhdhexaXzYNoxorDspeu5DOikZKjjGc_Jvi2hYTaKZbQIlZvxZcq4NeSSBaErUkR6f_K82eWRp8TGd9h5xFuNgYJSfq9hD2pIdh2ZaJ3iquCEIGtL6g9IXk75gJj3WEXSyUOAN5nRztmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستهای این توله‌سگ خمینی رو ببینید؛ مشخصه تا حالا حتی یک ساعت هم به سیاه و سفید دست نزده. یک عمر از خون و جیب مردم ایران مکیده و حالا هم نشسته میگه «جنگ جنگ تا پیروزی»!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67792" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67791">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=GFL2jq7Ag2Avgkvnq-4_pgdlbJtQJjl7uqVWDq9yEd2DYOcQ1Y6qWiO740bQ1F2QYF8PmmAPilU8xXBJzjvbTeVz2XLuzN2wPwDvWLpNysSnqJz3mFC9FTUj5svyqOeOuvHyOD1XiKvDB8eY1i_am-603uDAYHtx-cPTKVnS-shiMpFeibLHQSuitVkp4n-XurUNmW7cS3Dwxx_huP9ndUF5ufe1mcYRQGcEhQOSxlepAjmz70Vt-1chkexLBogEGPFl16TU4G2viB58tNG0ZwJArQb8eXLLZ2ab8s8WMxBFa6kqvfJHm0W2zZv2_Qbl8P_iD8DthDHV0_B1WOOnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=GFL2jq7Ag2Avgkvnq-4_pgdlbJtQJjl7uqVWDq9yEd2DYOcQ1Y6qWiO740bQ1F2QYF8PmmAPilU8xXBJzjvbTeVz2XLuzN2wPwDvWLpNysSnqJz3mFC9FTUj5svyqOeOuvHyOD1XiKvDB8eY1i_am-603uDAYHtx-cPTKVnS-shiMpFeibLHQSuitVkp4n-XurUNmW7cS3Dwxx_huP9ndUF5ufe1mcYRQGcEhQOSxlepAjmz70Vt-1chkexLBogEGPFl16TU4G2viB58tNG0ZwJArQb8eXLLZ2ab8s8WMxBFa6kqvfJHm0W2zZv2_Qbl8P_iD8DthDHV0_B1WOOnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کوچه پس کوچه های مملکت، یه دختر و پسر شروع کردن بوسه و مالیدن همدیگه، تا اینکه دختره دستشو برد روی شومبول پسره
👀
یکی از همسایه‌هام وقتی دید داره کار به جاهای باریک میکشه اومد و گفت جمع کنین بیست نفر دارن از پشت پنجره نگاتون میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67791" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67790">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‼️
ویدیو وایرال شده از بساط عرق خوری لات های کرج
😳
امیرعلی امیرعلی امیرعلی....
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67790" target="_blank">📅 16:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67788">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MgBw3TheJ3ib4Fw5_CVPkw9neAYRmLohZMpGlTEHASQenJO0OQyrEDk-hCdfWe9M5BGEH7y96je5GTjlqOfA7AyasDXBI0-Xs0XuJURsOwJg0Gn90uPvS7KG18lB26vOCArWWwoYgrHV4a8imJgQXexyCmg0DDO1kyqFI46SJixpuZcyBrGdATYGcdWGO4wKJN-0ZPvFtytrWn3VsPC0gZHCsFwHU1u2NHmncFg6-YhBH9WfvfDgCeCn9B5LK-tDcz9edsZW51szpEBjI4EKHDnT_7GeBbfOSuNKtveNoj2lls7nAwBq_GylOuhQwtK03nEGIz-WY3rygZP-jN-jTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=hZxnILR8SSS6nztueKT2NMJIeYCi_Vz4VnlAR96N9tifKEJXkLIodTPgTJVkHWYD0_xf6IRfcIibIVBOtVmg0YBy3ZUclHh_Wc2EI4t8pe2y145Jgs5lgkaawbE4jfJLMBlrR6GUpZROohFGMMEPcxpckJFYdzohZHNDXOEgAtHqKuAGHsAWEM_wVi0bO_AUVGLXyI1Yhj4Pge3zXur2WOKkRkVAb3-tT9E19eCnK3Cl4Fv4R5-A1lNPScIw0qB7pOW7VBab4ZluK0ofXAtd0rMTd62vGxcc-Fj1K0CZ9ma5VXfLE4b8QG7wA_uMcNArHvJfWPMHgZpNoj3gF6vaKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=hZxnILR8SSS6nztueKT2NMJIeYCi_Vz4VnlAR96N9tifKEJXkLIodTPgTJVkHWYD0_xf6IRfcIibIVBOtVmg0YBy3ZUclHh_Wc2EI4t8pe2y145Jgs5lgkaawbE4jfJLMBlrR6GUpZROohFGMMEPcxpckJFYdzohZHNDXOEgAtHqKuAGHsAWEM_wVi0bO_AUVGLXyI1Yhj4Pge3zXur2WOKkRkVAb3-tT9E19eCnK3Cl4Fv4R5-A1lNPScIw0qB7pOW7VBab4ZluK0ofXAtd0rMTd62vGxcc-Fj1K0CZ9ma5VXfLE4b8QG7wA_uMcNArHvJfWPMHgZpNoj3gF6vaKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات سنگین ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67788" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67787">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=OEZsxJon_7lc9kOSenL308nSepiVO16LyNtaF9mGLYkXuP65sj5Brp9gmLVWCGLDfAmLY85NCBoUvtxdaCi9zEGInHp6x60kNco57sVp6TOK0luYCq-G5ALOMgZ678JOBWAbKs3TOa6T9ZGZCxcnm-lAekoUzXup2EO7Nx2STKPJPMJiUcyJhBT_CiF6bWGD-A7JFxbNGDLvANKrqoVnQTdBY7gQawVwVaEgpttrceG_ZufioQfU-VbyMlB0brmmVPnVgRBuEDQTEykAfG6nzWh6sNroxd2d4Q19PJM2ji5Q33sPbJqJ44J5sjzKbwc7veDWhnmhPivjbuQi1fsAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=OEZsxJon_7lc9kOSenL308nSepiVO16LyNtaF9mGLYkXuP65sj5Brp9gmLVWCGLDfAmLY85NCBoUvtxdaCi9zEGInHp6x60kNco57sVp6TOK0luYCq-G5ALOMgZ678JOBWAbKs3TOa6T9ZGZCxcnm-lAekoUzXup2EO7Nx2STKPJPMJiUcyJhBT_CiF6bWGD-A7JFxbNGDLvANKrqoVnQTdBY7gQawVwVaEgpttrceG_ZufioQfU-VbyMlB0brmmVPnVgRBuEDQTEykAfG6nzWh6sNroxd2d4Q19PJM2ji5Q33sPbJqJ44J5sjzKbwc7veDWhnmhPivjbuQi1fsAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری فاکس نیوز:
رئیس‌جمهور می‌گوید ایران دوباره به میز مذاکره بازگشته است. آیا شما واقعاً معتقدید که ایران با نیتی صادقانه و با حسن نیت به میز مذاکره برگشته است؟
🔴
هارلی هیپ‌من، تحلیلگر سیاست خارجی:
قطعاً نه. البته دوست دارم این‌طور باشد. هیچ‌کس خواهان جنگ نیست، اما ایران کنترل تنگه هرمز را رها نخواهد کرد. آنها به اهرم راهبردی‌ای دست یافته‌اند که به‌گمان خودشان، شاید حتی از یک بمب هسته‌ای نیز برایشان ارزشمندتر باشد. همچنین قرار نیست از تسلیحات هسته‌ای خود دست بکشند. بنابراین، آنها به دنبال حل‌وفصل مسالمت‌آمیز این مناقشه نیستند.
احتمالاً این وضعیت تا ماه‌های اکتبر و نوامبر به شکل اقدام و واکنش متقابل ادامه خواهد یافت و پس از آن، ترامپ میداند که در آن مقطع چه اقدامی باید انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67787" target="_blank">📅 14:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67786">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای:   آنها باید بدانند که این امر، متوقّف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقّق خواهد شد و بزودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد.   @News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67786" target="_blank">📅 14:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67785">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:   عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد  @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67785" target="_blank">📅 14:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67784">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
انتقام خواست ملّت ما است و به‌طور حتمی باید صورت بگیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67784" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67783">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:
عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67783" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67782">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
پولیتیکو:
آمریکا انتظار داره جمهوری اسلامی در بیانیه‌ای که قراره امروز منتشر بشه، «به‌طور صریح یا ضمنی» قبول کنه که در حملات اخیر به کشتی‌رانی در تنگه هرمز مرتکب اشتباه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67782" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67781">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLEHfARz3jb64BoYFXOnUcV084qIXHXGWcKg4tPO48XhNmQk5JYl0KJH_0CyRuVQgI3UrbAtSYVtDJp_DR0HE-0xrVooRXaq2PIJkuD0HlYZJLiijWJ0yebAMSScNNDkXA1tK3RCx2-an17aAo7lrRsqieKcSoP-RHWxQpHvEe74obxekTRKp0tdU-lI5C56yRqlV_HVHF8rywgNbaDlTwDTB4GWJTvZkEyrF-2-Yix7dsx0RSURikTEB05brzwTj-ZgQ-IdxuT58U8uIQpTKDrzKplpCv80oqLJdYIo2mTAQL9j7hCOfYkDjM7NEUk73d9bEHnKzeuu2FuRWvfRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب رو باید تا صبح بیدار بمونیم که ديگه کم کم جام جهانی داره تموم میشه؛
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس vs نروژ
🇳🇴
| 00:30
🇦🇷
آرژانتین vs سوئیس
🇨🇭
| 04:30
🇮🇪
کانر vs هالووی
🇺🇸
| 02:30
[این فایت خیلی مقدمات داره و احتمالا ساعت 5 صبح شروع بشه]
🇮🇷
دانش آموز vs دین و زندگی
📚
| 07:00
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67781" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67780">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqNwnQvmoTCgFesfL9YIP2F0Dc0_YkpQQSPo_UXP1bzROD6Nbt6tDH6M8yzHAbax0KnGuUU8SSCf4BUy5MqcLd0W0iYNB4joJeIP204ZH2SIGJyrlNK7cl56mdU7j87onnaGHjK08hOeBEpIoATmb1Dozxt6UkXE3UKIIFE6Aq3bUAxizFalMe-WMwpPQtl9sGe4ePMh5bgmvSZl6KPwuHAAY0Ehw7zkqyCkF_OazGuxapXgTBqB2MbHVdmt5fTORA8zDKo1BRRuDxTTMwdnHEbfaYsEKFiGb90n9OhWcOJVvkfD4ajBeGepxCjxp4V04l-TUklQcMfnX9hKOZSA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/67780" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67779">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfcsfrOlAPPQ6_j26U9E8q1kZ6mJwWgh9GYmVfKlhq2MXSLQFcBJj6IBDvrv7TwFpwzwofe6Z9oQ0NYYY1eP_CZLvtZQtPxY8ax9b6tU-N8zmXw-Z2J5LrLDsrll0agjFAo5H3mDN9vX6xmkWE8N1G3uqXGnchIINeTxMYl_XUIDVYzGRqHGFPmEGnbC5bo1jZ2z5pYl3SLcrZNa2EjjNfVMFqni1gskGW2tzkTmWMDuotQWQF5xAdq_t0BTZRL_Pjl53XX0PM-a2Gfayj3cBkBNHJ5VUzWRJUyEIqPv8CTBZYNa3db5S02TaKsKe4_5WoCntMTQzjYPYxaqh5KYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67779" target="_blank">📅 13:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67778">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2gMhdm4QJlQte11G4BKVfP-iwldSbFoZvUccA2PP9h-tmaH6TyylAKaBrhA9oy_nQmakrEX8RECMamcmnNTipv4GVTSv8O1HyWUk_MIvU6s60BYihPVbyIkJ5Us5qDn7520HYyKzMNmxkOQue2zIyR8VvpUCAY6lsEALqqpgbCI8mdqbvd5fKZeiH7UY23d_o4QpEouuxG97t9c80gsRosNZZLBlQkfOzm7U697j7XLaR1gQyd5P4oasehFSNqWDaZwzTfkt87lzlwtLf1N3odU1OH8QGZmUBwj1orbYF2-az39nLsjsL8YjN7sy9uaVX3iBErZzGPb1zVbVUAw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67778" target="_blank">📅 13:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67777">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Sab8sSjKmXcGaZbO9K8VjYQ2UvyeTxGvC91t1tXe-dtx0Jq-WYgOqSnEZTeEiGZnj8vpXLguoQ43OBxrSui7FvIj9G3F6kBw82AOQUs4EcJ4mRjLvWUS1Bdy1Q7ugIDuI5KxXk4can04pVSlQRHjWh2W_xFIOjTQkZuekC6RzQ02TjaZ8sguxog21BvKQbkRwTHHN8en7L6fqWfLehygHo7aq-vCC3We9EIIZuFHyAT6hq9gM3B_B9cteV61S7j_KTc4oP4szlbkWHjYu2c4JBJIn5VgCchZHqqKMwHTDOflxyQJKqQiyoc5bmgDLJK_N1WPlg1GlZUvaQlfzEn6pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Sab8sSjKmXcGaZbO9K8VjYQ2UvyeTxGvC91t1tXe-dtx0Jq-WYgOqSnEZTeEiGZnj8vpXLguoQ43OBxrSui7FvIj9G3F6kBw82AOQUs4EcJ4mRjLvWUS1Bdy1Q7ugIDuI5KxXk4can04pVSlQRHjWh2W_xFIOjTQkZuekC6RzQ02TjaZ8sguxog21BvKQbkRwTHHN8en7L6fqWfLehygHo7aq-vCC3We9EIIZuFHyAT6hq9gM3B_B9cteV61S7j_KTc4oP4szlbkWHjYu2c4JBJIn5VgCchZHqqKMwHTDOflxyQJKqQiyoc5bmgDLJK_N1WPlg1GlZUvaQlfzEn6pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67777" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67776">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:   1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل…</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67776" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67775">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
ان‌بی‌سی نیوز به نقل از مقام آمریکایی:
اگر ایران امروز در بیانیه اعلام نکند که تنگه هرمز مانند قبل از جنگ باز است آن روز برایشان روز شادی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67775" target="_blank">📅 13:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67774">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
مجتبی خامنه‌ای  قرار است تا ساعاتی دیگر پیامی به مناسبت تشییع جنازه پدرش علی خامنه‌ای، منتشر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67774" target="_blank">📅 13:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67771">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=q1siNxInuXuiCaTXg6_4ZRbyt87NbYucMdo4Cnw2LLMne6Yj_AbA9AZQzcTTBMxK9Sx56KvHJ49809FEM9HafaE9AK52KLy4de2f2_aNsN1Z71n1HMnnUZjKjPcu8y3wGtUDH_-tagD6NbVFdfGiaXTSDKiTRs-Snlf3x6dcjDkz75i-Im2mRydoNFCZfuzTFh36PEDbyGF2J-5iMW15rLjZ4Sklnj6h4biUAYoKHPAKt3RFDD8Qee_rV7R3tNmublvtVYMKsS0BIEBz9o7LlSZOBwUEt0rxzydRcKixmUCiLPETWd7aTl-f6obZPggl3N8cmnyr-FOc9aQu0LtcTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=q1siNxInuXuiCaTXg6_4ZRbyt87NbYucMdo4Cnw2LLMne6Yj_AbA9AZQzcTTBMxK9Sx56KvHJ49809FEM9HafaE9AK52KLy4de2f2_aNsN1Z71n1HMnnUZjKjPcu8y3wGtUDH_-tagD6NbVFdfGiaXTSDKiTRs-Snlf3x6dcjDkz75i-Im2mRydoNFCZfuzTFh36PEDbyGF2J-5iMW15rLjZ4Sklnj6h4biUAYoKHPAKt3RFDD8Qee_rV7R3tNmublvtVYMKsS0BIEBz9o7LlSZOBwUEt0rxzydRcKixmUCiLPETWd7aTl-f6obZPggl3N8cmnyr-FOc9aQu0LtcTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از انتشار ویدیویی که توش یه فرد ماسک‌زده برای علی خامنه‌ای نماز میت می‌خونه حالا طرفداران حکومت مدعی شدن که اون مجتبی خامنه‌ای بوده و بصورت مخفی و بدون جلب توجه توی مراسم حاضر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67771" target="_blank">📅 12:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67770">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOOli3eL4X0Ixtq6p5_vF9B5fTt8sD5wN6p3yDB5oxx9RHG_KAZ8mw0daqYNr--3F19gun_t3aOA0uQHrGbPBD8X6chPfLTlPDg6GQ0o4xp3Mhfdp-KvYaVd4h-f6WTWmYsAppXlYSpBCsoffbliyLo23XUYdBn_wcfdlwmcKtpfb7ubavVC5Ql-VCb38-ljyXAhU8sWeBI-7bGmTozBioi6rykjvS9KsBfPmLPxh0PRvBty8C17aJaUYr0q7qDDYLCmSgtt3XEnRpTxOUByCU-iNfCqNJEHgV0FAnSd5nKFhFbNxPRpSBgBJVcEC75Z6QXat8LlVundBhv_RP7L3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد
دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل و قادر است، برای یک دوره یک‌ساله که قابل تمدید است، همه مناطق ایران را به طور کامل نابود و منهدم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67770" target="_blank">📅 11:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67769">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sn6N8MTa_GBRr7Ncoq7sf-2FkSLUvew9hT_3dxbxH8t6frjpvxASFRBj3BnmD8Hhf-8PmUnZeU3P1T8wVa22SpQws67YSmd-t8B_hGQn-2DWRmpbmZAgfxXLb7QbLFcvdNkVM1R9lRg0tSH01jxwxF2lVw0AzlnI7n4X7L5fBoN0iONWNPuaNWqxhFinqKiy3g5NudvoIaj21L8uDLk0-_UjEfM9WCIjY18f-wMSRX--fyTTuGxHVX5ncmYTk_6YAGHgOlEmFOkuhRKDDSPOlFpjAqQUa0fEsuN7p3H2nOtZI7ywI4vh9aQJTzRB9FPop7I7n9uQz88n6J-M-qjXkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تعویق یا تغییری در زمان‌بندی امتحانات نهایی دانش‌آموزان وجود ندارد
صادقی رئیس مرکز اطلاع‌رسانی و روابط‌عمومی آموزش و پرورش: آزمون‌های نهایی  بدون تغییر و بر اساس برنامه ابلاغی، از ۲۱ تیرماه آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67769" target="_blank">📅 10:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67768">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=DELjExlqY9BAsf1tNM0GvLxKAeCR1JxP8h7lDa7aL6arxiAE1Cn4pwFFass73yiA31Td5GfDnhDsATa0JPBFm2oV2A8VmR8kDwpc_XqIaj0okHuZuq1q2hibemRjz5S_IFMBfjO_6VYPAMDXT2BK9L2IcWghqrIE9EbO5SHIYfOLy1PVV9S39lBavks0F08Lp6Dz319_DbyBJF2RNS4D23zHzD28vhbfruoSGsH0Jc1919INGQFWQZjEfhOtXoapvmtAL0HDAzdehQXNx4y9qxBpLubk2AixJoyQ6K50i5nC39NGKkAEC3AeED640O-TdzrUGDvdVO8_Z_59TtfSAnCQLjZXihG8LQKjenv1wJz3jxOR2r21PUd_Z3UfJjRMb7nvEjTckRs2E_CfjgdZT_ehclmT4UpdMy1MlSRPFcT8bCgA2blSkGmiG1nu9mV1e3yKybT9vKMrYhPzWzPFOR3jkB9zME9I-qy7afuAVIg9U2XWYdX1qiyNlJB8rZdle2OXZBO-GtYOsuzYR2kNxdpnxorRAYlFGanyu70n7duOd6bLUFPBoUWgbxT5HeSovJzBIVaSeVf7MMZgcIBxdkBR44ocUVcMqNlEkM31KahVNcpoHk2rfo0XugpR4i9m4gzGJesIZndLf53y2OHnivnWhq29rEXA84KH5MQlwa8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d25ed65b27.mp4?token=DELjExlqY9BAsf1tNM0GvLxKAeCR1JxP8h7lDa7aL6arxiAE1Cn4pwFFass73yiA31Td5GfDnhDsATa0JPBFm2oV2A8VmR8kDwpc_XqIaj0okHuZuq1q2hibemRjz5S_IFMBfjO_6VYPAMDXT2BK9L2IcWghqrIE9EbO5SHIYfOLy1PVV9S39lBavks0F08Lp6Dz319_DbyBJF2RNS4D23zHzD28vhbfruoSGsH0Jc1919INGQFWQZjEfhOtXoapvmtAL0HDAzdehQXNx4y9qxBpLubk2AixJoyQ6K50i5nC39NGKkAEC3AeED640O-TdzrUGDvdVO8_Z_59TtfSAnCQLjZXihG8LQKjenv1wJz3jxOR2r21PUd_Z3UfJjRMb7nvEjTckRs2E_CfjgdZT_ehclmT4UpdMy1MlSRPFcT8bCgA2blSkGmiG1nu9mV1e3yKybT9vKMrYhPzWzPFOR3jkB9zME9I-qy7afuAVIg9U2XWYdX1qiyNlJB8rZdle2OXZBO-GtYOsuzYR2kNxdpnxorRAYlFGanyu70n7duOd6bLUFPBoUWgbxT5HeSovJzBIVaSeVf7MMZgcIBxdkBR44ocUVcMqNlEkM31KahVNcpoHk2rfo0XugpR4i9m4gzGJesIZndLf53y2OHnivnWhq29rEXA84KH5MQlwa8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی رحیمی (زاده ۱۳۰۰ تهران – درگذشته ۲۶ بهمن ۱۳۵۷ تهران) سپهبد نیروی زمینی شاهنشاهی، آخرین رئیس شهربانی و آخرین فرماندار نظامی تهران بعد از ارتشبد غلامعلی اویسی بود. وی از نخستین افرادی بود که پس از انقلاب ۱۳۵۷ ایران و در ۲۶ بهمن تیرباران شد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67768" target="_blank">📅 10:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67767">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=mGA4VfUjRAMWG7TCYDpyo8ZOWkDtlZwowHt3yxswmA5Hrspfwu-L6IyGpDqWb6fOA9nIJIoA35PuMjhp3dMU7omBKWan3xEJ9PFi0xxc3-CIKjGZQ5V6LRcUfISByue2i6vsamT3vtH2nj-yTpwJIM6jxKitEm79eUSE9GB3yGDUBf7FPgb_aZJeb-5BMqR3LTF40QIjzT7wSGDmoEKlhuAmMDRYLpU645lqdxC4i-oH9LlmJfPNI0SlFrMUNl6rJ_Amg3Z75WFhYUWx21JEh8RDYPArbPB6dn7gxeYGFpZ9zXnwqFird1mOdGK4k00OUXUE9LJGYozkRDNJyQkbzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=mGA4VfUjRAMWG7TCYDpyo8ZOWkDtlZwowHt3yxswmA5Hrspfwu-L6IyGpDqWb6fOA9nIJIoA35PuMjhp3dMU7omBKWan3xEJ9PFi0xxc3-CIKjGZQ5V6LRcUfISByue2i6vsamT3vtH2nj-yTpwJIM6jxKitEm79eUSE9GB3yGDUBf7FPgb_aZJeb-5BMqR3LTF40QIjzT7wSGDmoEKlhuAmMDRYLpU645lqdxC4i-oH9LlmJfPNI0SlFrMUNl6rJ_Amg3Z75WFhYUWx21JEh8RDYPArbPB6dn7gxeYGFpZ9zXnwqFird1mOdGK4k00OUXUE9LJGYozkRDNJyQkbzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
انفجارهای دقایقی‌پیش در مناطقی از تهران بدلیل خنثی‌سازی مهمات عمل‌نکرده بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67767" target="_blank">📅 10:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67766">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=FIid9s17v6pBsfpVGASBt5KUySuw8bOBfVJZrqymgUlyWkGO6LFaub6ANYuM3lN8B-ONn8qEmJPbC-UfJjRLqaMtSvdtoXkHX2USfYAxrcS7MGDIsdEsy918PsSaxr_KLKTT87qVNM7Ax7_EiQOd6FGERKSZTk-BB2mln161lzBdJ4L5MszYDLl7ua0ianJU6Nx7ElyntCyVnz6kdrN-Is2pRdsJUGqNj-CiZ3kq1KBu1_aHR5IyBWveQcBavAAb6dyaFftGq0SQ-bGMMQ69wer66lqaxbdMFEL3UxgkIjVJLqBccJMWPtwvq_KQbo7eauNh429_wcaU68TWAYdTuwcKGU6a6ruisq9eKS2uUixv_jxpNI9ohWRAcbVvIe2SExRFmUGQHM-Z-t1GkfmRYLkoqDMUDj2qNtr1rvuBhz8eKNyZxW1lZNytkxoOaJ3sm3ctYiTxEDZApc6YPNuvQe6bZ2U_is6mz9vkrjuiNVvt5IWToN1QBfyDFv2TFPztYv0NYCHvYfcNk4T5d0HkGifaD864Zp8UPBtRmNsbxlhWTf8HdFAKR7mMS2aXvAAW8XAlqcB-cJCF5zzP7PlfkYiqNBo5Hb9WegmeEap-hxoUizRempLQ6EOXLkdGrk0dzsfl8EQ5LBZh29hLZsGotq5szs3NPDP5WmS2C_Ev_cE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a14613e56.mp4?token=FIid9s17v6pBsfpVGASBt5KUySuw8bOBfVJZrqymgUlyWkGO6LFaub6ANYuM3lN8B-ONn8qEmJPbC-UfJjRLqaMtSvdtoXkHX2USfYAxrcS7MGDIsdEsy918PsSaxr_KLKTT87qVNM7Ax7_EiQOd6FGERKSZTk-BB2mln161lzBdJ4L5MszYDLl7ua0ianJU6Nx7ElyntCyVnz6kdrN-Is2pRdsJUGqNj-CiZ3kq1KBu1_aHR5IyBWveQcBavAAb6dyaFftGq0SQ-bGMMQ69wer66lqaxbdMFEL3UxgkIjVJLqBccJMWPtwvq_KQbo7eauNh429_wcaU68TWAYdTuwcKGU6a6ruisq9eKS2uUixv_jxpNI9ohWRAcbVvIe2SExRFmUGQHM-Z-t1GkfmRYLkoqDMUDj2qNtr1rvuBhz8eKNyZxW1lZNytkxoOaJ3sm3ctYiTxEDZApc6YPNuvQe6bZ2U_is6mz9vkrjuiNVvt5IWToN1QBfyDFv2TFPztYv0NYCHvYfcNk4T5d0HkGifaD864Zp8UPBtRmNsbxlhWTf8HdFAKR7mMS2aXvAAW8XAlqcB-cJCF5zzP7PlfkYiqNBo5Hb9WegmeEap-hxoUizRempLQ6EOXLkdGrk0dzsfl8EQ5LBZh29hLZsGotq5szs3NPDP5WmS2C_Ev_cE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سید علی خمینی، نوه خمینی:
«هر کسی که بخواهد برای دستیابی به صلح با آمریکا مذاکره کند، خائن است.
هر کسی که پیام‌های دوستی برای آن‌ها بفرستد، دهانی نجس دارد.
مشکل ما با آمریکا، مسئله امروز یا دیروز نیست؛ این مشکل دهه‌ها پیش شروع شد، زمانی که آن‌ها کودتا علیه ایران انجام دادند.
اما با آنچه اخیراً انجام دادند (ترور خامنه‌ای)، بذری از دشمنی کاشته‌اند که هرگز از بین نخواهد رفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67766" target="_blank">📅 10:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67765">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-0c4NjWv3onzgAPKcHn2L-aaSLejePPQua_lAJJiwutTzddOyTRzK0fRCO-MI9RDhyyGe0LLnULUqyk0U_xNzv5cxWYzyq4EkETnunLPe1noZPilZFI9C2Yrai9YCmva2vh0jDKLcaMZU8iwBrbiM8AlEZhpjE0N8XnRP2x9m8U-u0FpZhRrJcf5reUU8IM1Gf-Z8aZPWIWYqbjAQedTCRzhcg69WVW700swJtub6G-pUG694HTrIkGsQ2-w01l4EovqwI9xbijYXw-rKkKZatyKWxYKdHKI01tPkAd8WyqXdsP6aIYxqb9fYjD1EguLS6u9ZcfFp4e3Y2sv98FBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
فردی که «رهبر عالی» خوانده می‌شود، در حالی که رژیمش رو به فروپاشی است، در انزوا پنهان شده است.
وزارت خزانه‌داری همچنان از تمامی ابزارهای در دسترس خود برای منزوی کردن او و دیگر نخبگان رژیم از نظام مالی جهانی استفاده خواهد کرد.
ما این دارایی‌ها را برای مردم ایران حفظ خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67765" target="_blank">📅 09:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67764">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/news_hut/67764" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📱
اپلیکیشن اندروید بدون فیلتر لنز بت
🚀
🛡
ثبت نام آسان و سریع
✔️
📱
اپ
ل
یکیشن را روی موبایل اندروید خود
نصب کنید و بدون نیاز به
🔤
🔤
🔤
وارد سایت شوید
💬</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67764" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67763">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Wqck-uTnVKr1JCreDj_0AUmXlGvFjRkgybwdH-i6haXSReQvkRer6AZkoc5uWEGcRL6Evkf3oAZ4achfQB7QFDX6xiRqZTVw9BuHn1anBZcaUWVKttX_3QSlEaRQzXeIIS_TDthG_WPSOeicrLG542JF5MSfw8WK-mceaeErri-md8WWOJTbgVwBm23UxDxjvAMrT_prZEvA0p_GQHc3qNhjjNtkhRFhE_vTLa4H2bgLlfY4K7sJFmWdvrqqWEvvbfSDFalHHIoYy2aa5DiUF1xZWY1QmxKU3462M6EMwLN7u_i43BryCEeWTNB3JUCPh9RO8Fuw6XDrmDnRLvXYFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
قهرمان جام جهانی ۲۰۲۶ از نگاه شما کدام تیم است؟
✨
با پیشبینی قهرمان جام جهانی شانس چندین برابر شدن بردتو امتحان کن
🚀
💥
متنوع ترین آپشنهای پیشبینی در
لنزبت
😮
بونوس
🛍
0️⃣
0️⃣
2️⃣
خوش آمد گویی
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
برای هر واریز
💯
بونوس
🔤
0️⃣
0️⃣
1️⃣
کازینو
🏦
کد هدیه
0️⃣
2️⃣
🔤
🔤
بعد از واریز
🔣
0️⃣
3️⃣
کش بک هفتگی
📇
امتیاز وفاداری با انواع هدایای نقدی   روزانه مخصوص کاربران فعال لنزبت
💵
پشتیبانی از تمامی ارزهای دیجیتال و کارت به کارت آنلاین برای شارژ و برداشت
🔤
🔤
🔤
🔤
🔤
🔤
🔤
📱
@lenzbet_official
A19
📱
https://www.lenzbet1.living</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67763" target="_blank">📅 02:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67762">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZDNNgFoy4A_3CGopMjYjPjbIsiwShBOWJen8znfU6uaSzmlU1F--qENgTkPXIkNA-87C37zbAdIIC0ss0TW-0xZEzWxy54YEJkopZHiC1NlhI2xQTuYifBKebpfOXc3aMT9UB44C1rorWVHhzMrVR3t6cWTALAlvBaofkXfXm3ySOVobodb7I0ggwnuPzkr6Jrrx4x4So7iUZBXQE-SsLCt3BnTlNamGeIPC1c4_mXJXvBumW44S15a56SacWhE2_fWA-yrUvyuXBDQY7jM0aeGHpSgBrjUqema0BV1RhWdAXhOcAmCAOmxfOWGMbCcSFDrEVX3chXj-jRQ5HKoVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67762" target="_blank">📅 01:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67761">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
❌
یک مقام ارشد آمریکایی:
ایران‌ با عواقب وخیمی روبرو خواهند شد اگر از انتشار یک بیانیه عمومی فردا خودداری کنند که در آن اعلام شود تمام مسیرها در تنگه هرمز باز هستند.
اگر این موضع [آنها] فردا نباشد، روز خوبی برایشان نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67761" target="_blank">📅 00:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67760">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUIi_kmBwaWolF5_yqfFsBkqxZsC15p_OxNxra1TvEHveXjaQThQqtf6i4Q_Y16s8818F1dwiPqeI8dnWNgHIKpowY2qBxalVEGAegWZHgVzxNdBivYT3KVEnJ_KfcZbVm3v8tAO0IobQX-9oXavJiW_pQg1fVNjfNudSqUO1BLmUm9iAGpgi4Sz21iI5tlUVwjy37iMKr-V9UGInqAovdyFd_NrF9pfeA45oC7f7_GQgX8WsH4Fg3bqOmBp_YF8HuV2vpoJxXNtoFlPHg0BlqZc5TK5RXUQvi-78MnHQuQ3_hCy92MKXTWPw46GxMIEnJgQPo6Q-XfaeublYDhIRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته مقامات آمریکایی، ایالات متحده به ایران تا روز شنبه مهلت داده است تا حملات در تنگه هرمز را علناً محکوم کند و باز بودن این تنگه را اعلام نماید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67760" target="_blank">📅 00:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67759">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کشوری غنی، اما مردمی فقیر
💔
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67759" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67758">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:  ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.  فردا در جلسه ای در موردش تصمیم گیری می کنیم.  @News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67758" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67757">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
وزارت آموزش و پرورش:
ممکنه امتحانات نهایی به صورت داخلی برگزار بشه.
فردا در جلسه ای در موردش تصمیم گیری می کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67757" target="_blank">📅 00:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67756">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=kP-CCBIiSu6wriNVS66ZHX0I4j30KQltu92pNJ6RwwnEjnMumCSCPdphOmijTvL5lJrqVs8zuy43wk7ick5WqRY-u-VSKsPDSjcg9C1r0BSF0PDeCjsWNI_K8i7n7g22rXv2gxrFxjaNaw3SIIvhiJ6fF1IAfiFswaJ23VN6si42PwVfYqjSDh8y1TcZG4KkuFv5gwTblE9uJAcrGPrX_0ii8VV2mkvht3a4cXlzK-ON-hymfwDX9P3Ib1DX0x6qqKFSSVwqyDatyWXdw8dnNEXd0sZ-1wGbjVb8MhBrBYwhZrfnT3xjrzN4xqVzTirj86D1-oaEV4Dx6hon7ED7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024bc9f4e4.mp4?token=kP-CCBIiSu6wriNVS66ZHX0I4j30KQltu92pNJ6RwwnEjnMumCSCPdphOmijTvL5lJrqVs8zuy43wk7ick5WqRY-u-VSKsPDSjcg9C1r0BSF0PDeCjsWNI_K8i7n7g22rXv2gxrFxjaNaw3SIIvhiJ6fF1IAfiFswaJ23VN6si42PwVfYqjSDh8y1TcZG4KkuFv5gwTblE9uJAcrGPrX_0ii8VV2mkvht3a4cXlzK-ON-hymfwDX9P3Ib1DX0x6qqKFSSVwqyDatyWXdw8dnNEXd0sZ-1wGbjVb8MhBrBYwhZrfnT3xjrzN4xqVzTirj86D1-oaEV4Dx6hon7ED7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت امور خارجه:
ایران اجازه بازرسی از تأسیسات آسیب دیده در اثر حملات آمریکا و اسرائیل را نخواهد داد و قطعنامه 2231 شورای امنیت سازمان ملل عملاً اعتبار قانونی خود را از دست داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67756" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BiPAACJ5BjiPdiuHPyoJd9z4POe7SMF1v6O-5oMJKTFnwS6ZsFi_TQFuynZ7UQVMK2dzmu-8ovEDiuQ9MlBlNzOYbmOLeYz_rsw7pcKuXpn-p1-VnDztPniyZRobVAvlZF3AcjpAeMbQgZvYsykgUVcno-gCQ_va3PBU3MesPda-GMiSeqcpaLudstPushFtNs1BX_nIs_vXdMyLZzRdRSW7BoTAEtqw0raz96_X8sx0xU8Pd7lQsPm3BXCPB2AB0A7eBqfXF00wgrj1ha-9OOr6wd8R_mGhyWrkMUtmJRjwHAbLzEw1sXYN666hAx-l1F0W69a6Ae4JQVEQL7eYZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E_Xqj0eFkB-BdiuGU26dK4QWzUwr_oNbzc8yPIjvgzOQOeRpltFkhMYDMLaS6Owbz3yY7jWAcmiXj0BviZE0JP2i63c800_uZUeNm1u-JBm9JuPueL5ekCPSMyhVQ8WvFUF-8Iz1TO9g-BW2bKZueDWfr2_6-nZGfC-v1-fVICrscII5Ju1GP3k1lT7JAq2JXG2fO1fb202KtCiSP49HB09ZmdU1XdfIMJTR9vJd8LqkUqilhp6_j4yIUc9UJ-Vt1LWTkNXG0umMx9sRn4Yvv2sFXwGsP09GabFuR3coLpkjGVIKZ3N3f8wyUBLM2kw0ddyszvOMFR9nLsTREB_NCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5qVpXNvZp6S3UkYJQ3Ew3mBfZqFS0MRRX203i9j1EU0FJL67dh-zdR9D-ACUyS9x3NzTLBxK_kXtuhCT_qzt7T4h8rZagBJU3uBGUccdG-Ou38smD3EGvUejAVUQU0Uevdmvclny4511V1O-y2hYVM1GrIIZx4Kp4A5IP49h4fFLOAEPuluBQIwEANIZUGi3ME4-T9B3dRX08pLm8AuTGDsxS3CC9TjWw1lwZgtu-EMwuq2mtEgwOZzAT_pIKlmlL-qttJZE2ryjieavHfiUp4PrT-6pG4Y2XGC2sR37y-0uCTxU9hXFaYVVQuAClD7NvostWD2LQpMQjgZcSmvdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
شبکه خبری CNN تصاویر ماهواره ای  ادعایی را منتشر کرده که نشان می‌دهد ایران در تلاش است تا تاسیسات هسته‌ای واقع در پارکچین را بازسازی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67753" target="_blank">📅 23:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e999307d.mp4?token=dJ-YTcuEoLbT1vvWSV19XmHyB-5ZnigDtV67kBFC3Wc1CM5oKZ_V_a5l1M77QFnhqXPYQ4l2WZLt8Mk-0eGnzyfHlLMO8anuWSmLj6miErqAbBan7l0dT4t1qO8A6KfTpb-u5xJGinxB8ubZkk_ud9tBtsqDlVGlxdO__vCGEUMDK-k9hrHA_oCoBFCXZN4btwJpYnxHZr7n1Lg2R-_D_J7TO1xCN3vmaRG7osjtOKZZt1dCSFao4Si4VJoQua4bkx25byGiF8mkCGkw-bSFqY1-h7fzfSBtj3Cg4f5c6Q8D0hacHBJba27DqW8SxSo7Yj9OjLaYLAsUAt25-tLB6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e999307d.mp4?token=dJ-YTcuEoLbT1vvWSV19XmHyB-5ZnigDtV67kBFC3Wc1CM5oKZ_V_a5l1M77QFnhqXPYQ4l2WZLt8Mk-0eGnzyfHlLMO8anuWSmLj6miErqAbBan7l0dT4t1qO8A6KfTpb-u5xJGinxB8ubZkk_ud9tBtsqDlVGlxdO__vCGEUMDK-k9hrHA_oCoBFCXZN4btwJpYnxHZr7n1Lg2R-_D_J7TO1xCN3vmaRG7osjtOKZZt1dCSFao4Si4VJoQua4bkx25byGiF8mkCGkw-bSFqY1-h7fzfSBtj3Cg4f5c6Q8D0hacHBJba27DqW8SxSo7Yj9OjLaYLAsUAt25-tLB6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب ترامپ رو تو مشهد دار زدن بعدشم ماکتشو سوزوندن
گفتن خودشو که نمیتونیم بکشیم حداقل ماکتشو بکشیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67752" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqai4gQc2dU--E0TIcr7pIICNnADexaBmZCPRCLyGmCFMwF8l76NkeIa6r8iOcwMUoZ2-Y8YgjYGZOqsFSpkiynBMQ7hIcIB3v6upB2sQLoA68-Q6zSxfbbmw8YPfm_O9Cymt_qZT10645uI5izDxT97_Vlzr0AE15ClNtiUsJKT9KQErt6fzxuec8vjIjh_-3uz0rrkbB5vHw1Iy3XeGmFz2P3zyiMKL8Dgxf_Q5iBxncWd_72L4FMWOh9hleM3_HZvjbv-u5B9z7ZQV6jFmGtQ0oKob45zy4J-xVoa4oaU_zy7-2uNE9i1y7kaun5e8f3zmso2TkLRhL_NxEdYjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
در جریان مذاکرات، به معاون رئیس‌جمهور آمریکا توضیح دادم که ما به شما اصلاً اعتماد نداریم.
به نظر من، تنها کسانی می‌توانند با ایالات متحده مذاکره کنند که برای جنگ آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67751" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67750">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.  @bet_maxxx @bet_maxxx @bdt_maxxx</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67750" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnegin</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrlzdlFm8rhIqs41kbNlIN4pM0QKVDrLTLSa3KWP10-Jd-SuQmHSoaGZv8awAaHpY-Cfq5E2J3kwaCAolLNy-uIYqQAvJD4x45IhHPqakAk7rwmtHKE6zsawNqvk9m2teRwC-bxuv89URysRy_b1Ew7M3Kj0EMUWDInRESfj7eSnQG7u3o1iEdyfNqs8b34PnEQL8DL8TZwT4NTVCUI0kJPSM57pJo31a6Gp9ppkFWNjus9pWPqW6P6kI4aFZw5bqYMaG8omLZbbjb65n4uQIm5IhRO9YtwcIUBvNWZbkVJC2hkmH2ys6ScLD9--Qq-IHQHrdju97c96ky7d1gaBJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تحلیل دقیق مسابقات فوتبال
اگر به آمار، آنالیز و بررسی تخصصی بازی‌ها علاقه‌مندی، این کانال برای توست.
📊
تحلیل قبل از مسابقه
📈
بررسی آمار و عملکرد تیم‌ها
🎯
نکات و دیدگاه‌های تخصصی
همراه ما باش و مسابقات را حرفه‌ای‌تر دنبال کن.
@bet_maxxx
@bet_maxxx
@bdt_maxxx</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67749" target="_blank">📅 23:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=dKFFgd6zPwl3K5QRfbE8ivSggYPQ7kWO2LW4j4jTjnN5pUoB0Aiz9gnitH7vwsxIkBgBWqaWfqm69mNLdEUmxqG7rDW9Fd14ASAeJmcgCsHJh1axZQBY8rKdjobbTrOTPIrPWh0uaPddRnOEI-rWnkTPGzdrbsF96f66ZjBtUF181b5Ttb9iw3rZasajiT6zxG1E-8WgEJIGKrkzbcZrFwIcrML4dnCD54QIo63G35X3OcDODWsfKyb3tYjqrYA_9lrWYW8HHsXzJCUvNb4G6-2J_iG_-aaCd_BZjCAuo02GwcU0KB6TCEssLkEUyFQXysfu-Wsx0rX2oejY8uwGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=dKFFgd6zPwl3K5QRfbE8ivSggYPQ7kWO2LW4j4jTjnN5pUoB0Aiz9gnitH7vwsxIkBgBWqaWfqm69mNLdEUmxqG7rDW9Fd14ASAeJmcgCsHJh1axZQBY8rKdjobbTrOTPIrPWh0uaPddRnOEI-rWnkTPGzdrbsF96f66ZjBtUF181b5Ttb9iw3rZasajiT6zxG1E-8WgEJIGKrkzbcZrFwIcrML4dnCD54QIo63G35X3OcDODWsfKyb3tYjqrYA_9lrWYW8HHsXzJCUvNb4G6-2J_iG_-aaCd_BZjCAuo02GwcU0KB6TCEssLkEUyFQXysfu-Wsx0rX2oejY8uwGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالد ریگان چهلمین رئیس جمهور ایالات متحده آمریکا:
در این سخنرانی، ریگان با یک روایت طنزآمیز، دیدگاه خود درباره نقش دولت و مسئولیت فردی را بیان می‌کند؛ روایتی که سال‌هاست در مباحث سیاسی از آن یاد می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67748" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67747">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VccsGbitfgAg5JpgSg7B0mkA2eMLDeE6cjC81GNkjTWqjK0bnCaUuGfjOO-hG_kKRus37pXyIa8Py7YJCiBtNTsHuQJkoe4LyIhK4WWF7bGKVaZJmw8d-hRh_YX0Q6HDzTpJZCiEvCmQA66DJS7aThzPVw08G1Nsp01NIcZdQIZAI_m5dc_Kh5hpjF_UuUkXeCdDMSA9qaxCh5TtmK0YQWD99pbE_XAfq_B6Cp9WNCRU50tQ9sO7NbHLkeJ5j8h271UG58DtcwoIHboi3pe4E_RXI6u2sHUiyeZnaDmCbh4zlipiK5760pQo9TWLL7zZAD0mzLeBaQz-7tuYauHvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل هیوم: آمریکا و اسرائیل گزینه‌های براندازی جمهوری اسلامی را بررسی می‌کنند
روزنامه اسرائیل هیوم در گزارشی به نقل از منابع دیپلماتیک منطقه‌ای و غربی مدعی شد که ایالات متحده، اسرائیل و برخی کشورهای منطقه در حال بررسی راهکارهایی برای تضعیف و در نهایت براندازی جمهوری اسلامی هستند.
این گزارش همچنین ادعا می‌کند که در پی تشدید اختلافات داخلی در ایران، مسعود پزشکیان، رئیس‌جمهور، و عباس عراقچی، وزیر امور خارجه، با فشار فزاینده جریان‌های تندرو و فرماندهان سپاه پاسداران روبه‌رو شده‌اند و حتی احتمال کنار گذاشته شدن دولت پزشکیان مطرح شده است.
اسرائیل هیوم به نقل از منابع خود مدعی شده است که عباس عراقچی در تماس با میانجی‌ها اعلام کرده دولت ایران نتوانسته موافقت سپاه با مفاد تفاهم با آمریکا و توقف حملات به کشتی‌ها در تنگه هرمز را جلب کند.
این روزنامه همچنین مدعی است که یکی از گزینه‌های مورد بررسی واشینگتن و تل‌آویو، تشدید دوباره فشارهای اقتصادی و بازگرداندن کامل تحریم‌ها با هدف افزایش فشار بر رژیم ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67747" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67746">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKen5gqqrRyX0QSrxg6whhBD0g9LXEVig-iAerjhaqhflsQTCFwAOmhy5RlbQLxWk6oUCzKPQkHKNuWYH2Tf2vD2YH-0lGRYAiDIGlFojrFpAxnO8FBLVeI6H15Fp-laRtD8jPBTssbm-cL8pHwdArHPsHgfaP5zO2wYa4Ms3q8qmBbkQiWMbGnPLRRc3MpmPrcQqg7pDI1MA2KP_iz-JP9eW2f4DdfiUURGdjO5YxDhkkGhqJV6AguHr-6z_rQJwQLpEiKlcAljVrYFdNXF60PgsD2vI93NMgaUbCnFCqEKAJ8QaK8sf1Jvs-AIBFJsKw9mB5-djdWpOXMDGauABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باراک راوید:
بر اساس گفته‌های یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده، به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و تلاش کنند تا تنش‌ها را کاهش داده و شرایط را برای از سرگیری مذاکرات فراهم کنند.
این دیپلمات گفت که جلسات بین مقامات قطری و ایرانی در تهران همچنان در حال برگزاری است، "اما واضح است که هر دو طرف تمایل دارند به توافق‌نامه اولیه بازگردند."
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67746" target="_blank">📅 20:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoQChLLmORuQyPUhuXvJnRiNs68ESGR3JKQtbWK8RX3zWFx6nf7dSq5-3Zg8wrI_29wrflVvfGOOf3Vi62A4-5qvQ57FyUzy_ozkXxG4ygBItcp23AH3f4T3iN9XSMWuiLS7C-aBYB19VDl4TB_NlvpKsoOILDGp084O6JwX8drAkpGeH8ICO82zQvkBWN4Kn4txAAuBZqwg4KwUcqMULiMKm1py-_czCzAyfvC63WAuit_Tq4hBlUP21vV2Ko2HBazXtrPj9CsrloTaZHppOhtQCeGUqigFcfbSKUPhmRipKpR9uD880LL0-F_IgNQfN9T2zXNohJBrUld6zHRRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grTVM_NAjS4-WosYBQh_AFMOkb6YU7HY56KKlRYzwdD_U1RgY2y6N6sOJBu0-UjxxSjfhzLvsVqnk_Ur7P1Ysoe2i82zkHg0p5ThGsLbw_AtZouKskSlrw_picRyF0Rh2anhiUgxn0MUNYHWymJcSrw5HRI6S-qcaY9xp99AHVeHor3h8NyXpjOfr7bzSnoDxTDzK4iHoeSGNYIs8USESkydm-xExxc5LBG9Ex1i6wN7SA-awllbgb645T_MUlSjaKkJ-bIqoUxeTQVIUoWftr60lcC7K4yiCCpUJNRBk0A79bwI_JROdLk7UWh15lOljf8MBLBm8hAEJhDzwGkFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=XUM9w4hxg_esBMOdOjUxLT_mXExKEO33Wxk7aFfNGVA22KMIvZfit5qYyGTwAVm4x8Ns3Sz6qh66qnFqOU1XTjZegl5cdCK96c4m6Zk9vr3BA3-SzPnOhaTicPO48Z3zrnuvaeTz7ag2EJzrKotUSzncOTDIWGIa6wpBKEWCDwMpxVn01pN3ehWLbcb3KvS7XYwvyelvaLbIm61R9zz_ILV9-Pjqtrin6xM-Wl1_Qpcdx4whzmZef6mMMCiDPE7zMVu7EKZNBhRYWrhkZMadheF_U6xSKyMbmf9RGqaoeUl5KChjcm13rZYaUhkXuFEbHmL6rw2IIYAr-KOadxmJaA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=XUM9w4hxg_esBMOdOjUxLT_mXExKEO33Wxk7aFfNGVA22KMIvZfit5qYyGTwAVm4x8Ns3Sz6qh66qnFqOU1XTjZegl5cdCK96c4m6Zk9vr3BA3-SzPnOhaTicPO48Z3zrnuvaeTz7ag2EJzrKotUSzncOTDIWGIa6wpBKEWCDwMpxVn01pN3ehWLbcb3KvS7XYwvyelvaLbIm61R9zz_ILV9-Pjqtrin6xM-Wl1_Qpcdx4whzmZef6mMMCiDPE7zMVu7EKZNBhRYWrhkZMadheF_U6xSKyMbmf9RGqaoeUl5KChjcm13rZYaUhkXuFEbHmL6rw2IIYAr-KOadxmJaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2rG3GpBVPqObgO7bSc_voN6QVqbLgtNsaz-2KNPWYh9ghx555etmEgFSs7XpOVhdvcSgG8fNPfiw26LyEpwyM_ehhtje-VWGPRCQUQ8BxKwh4M43dfhp32CQXQhqYYg_KiNtaW5ku5zoVzHOJoPA17O5xnzcHMFf71B1CIy6mBjIzUMAaVne0J8u8IVuiEIRQ1WBm9jOn88HIUFZKTBNhgQHPzdu4Du_P0y4d2t0t21M7gUPI9IVnKl2mSYb4IwaEEsVrfi3EtUV0V6_AAt8rYboaQEj3OQ1RPOsGaaMKyK-pJU0TBgIldHZIwzPZiokJH3PFgw0E1yerqORfenfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owb7HrW_6adHhlTZnMuEQihfAEQI-P46k4gNG5YOvxrcKPcWtZw2GG7SrX_lRYQYuUACtJ5QdRIwhWJUTTqRT6KDVap_4g2vwhmXksF9glHzx0yGEpAUx_M4Ai6w10xlJ8g4aZz-xuBa6VoHfqt7w7aK0jG9pwRNeQwLWA3_CSGbZjj0Qbt3IYlPnvsg9FtzgjFwVm9VIbic-IeFRUWaiT3FoQgzM2_ggiBd39_VPY-D_3EGQNqNJhYO7OnvnK27v7vKQZah53nd4ovYs-ya4NBeshKBAl50kiTmTiiuiQ1wJrS1Eg9wchdl5SPCPhnQmj8e2RaEPdfrdiIuzBIm0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=nWNVYMDn3Bgo9Naw78APEB_Vo9RWFtkC7WIElzyu9BtWGczzbdhcoveQhq6k1FeWmpH5LQbPRXwA5o2C1zFtTGtHlilVrlmNZMEN5FzNjADQ-O6UkkNKUeWnf9k13cny9DcBonYGHLmx77wRHwh8EGX0dZRm0bNGdxiN0vWoCJh-0wcoeFAsw70tFQziJfa_IRwNT-Q8aAG4W5DVRI7wI5WHTddUgcmB-QF5vtI72GtXtwGKS-jZbVIVEpfx13MUZseKRZAoWrKnlMEl4dug3K7zRUyussOS0F0sD6QGBfQBYQMgVClTeL_CFFe4-UZ3dvThKEzLYikMFj4ejh7LIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=nWNVYMDn3Bgo9Naw78APEB_Vo9RWFtkC7WIElzyu9BtWGczzbdhcoveQhq6k1FeWmpH5LQbPRXwA5o2C1zFtTGtHlilVrlmNZMEN5FzNjADQ-O6UkkNKUeWnf9k13cny9DcBonYGHLmx77wRHwh8EGX0dZRm0bNGdxiN0vWoCJh-0wcoeFAsw70tFQziJfa_IRwNT-Q8aAG4W5DVRI7wI5WHTddUgcmB-QF5vtI72GtXtwGKS-jZbVIVEpfx13MUZseKRZAoWrKnlMEl4dug3K7zRUyussOS0F0sD6QGBfQBYQMgVClTeL_CFFe4-UZ3dvThKEzLYikMFj4ejh7LIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صداسیما:
اگه خمینی و خامنه‌ای، زمان امام‌ها بودن، امام حسین شهید نمیشد، امام علی حاکم میشد و امام حسن هم صلح نمی‌کرد.
پیامبر خودش گفته؛ من مشتاق دیدن اینا بودم و حسرت دیدار اینارو داشتم
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67739" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67738">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ppdfj-PKOzpO5BTi82s1afSCwLZ2EECN-Ap1CxZ_2keWujQwJ8ErRFNBDHW-SCrS0mLKC6lTne3qa3a0CF1tGRKgi5Y0Ll9VheJ95nfBTa9QVzXC60rr-OTXxerF2A3vb0MrdBCVteg-92RL_-REsaLnudy_S9lYOfjQHHFw-MCK0xXYrSYNSTjIu9L47tBsS1rGkcIjW57GN1RkhpNHvea1hyNoLudHULS_TpJZaWOZ0DBefjzVTLICmWaCP98rHKS47S6Dsd2ag_u-14sjmPLhGaZkiRtA8NRwv2KNtsj4x7G0eD7nah3wjjl-d8QcmjCxsYfYL98LURPLTmhhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_2v0u_zHtHX8b_UvylaPeWOQD6eFIe6CL5HpKKfQ9UI5gKCNs0loo6pcW-4lRpSz9kqpwQsdfikw5y2pBLa4WKitSGe19jhMry6SC22wHSi4MOTFS2idiSqRIPbmtA-s4OGxDa8AqBG4qX4vAva6bCaXepj5zgkvtjR0vjE2Oy7fBgpviDV4owhNIiA-9zlxaJxcY7ybksy-kiWn5BYbRnIYI5tPsA7mMwDZWjy6NiDR8MuPfZ5hM8nfkE8h23Uf6FePeJRlkX198-BLexHxFVeOMiGzp-GtYY9m_Hr1vwk-_bNxPLqPKCJJwXW0GrmycEI8GECYy7HCk2VGSW2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=m8r-KHJXJhlGKeZNjX8dAbNN3drVCY-zirwpD0QaYrlPv22NkqELLH4zlo65NK8PVq9SXHTFf8vKr_8LKNwvJIO78QH6TYPVWpCkpWpvh_9xgtPrGSRw9Dz6lt42beXiFD_iLDCILElyUSWt1jzoP-p_IA1IXFa--7fGP9_bTNgJc7TEvaK5p1oHrtKoW5vg7mttVoT4Fth7v5SmK_vGG1EuLJQn07OhhLpEjNOargyhDnBZiep0raX9-YOfHL485wezDuesTeLwANs1Vc55yDj0afuTQxSFTdm2BKHNxZwrw9EWtwDSa0HS9wqbAwHt-fUat26AUCzkr4ggnBn8RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=m8r-KHJXJhlGKeZNjX8dAbNN3drVCY-zirwpD0QaYrlPv22NkqELLH4zlo65NK8PVq9SXHTFf8vKr_8LKNwvJIO78QH6TYPVWpCkpWpvh_9xgtPrGSRw9Dz6lt42beXiFD_iLDCILElyUSWt1jzoP-p_IA1IXFa--7fGP9_bTNgJc7TEvaK5p1oHrtKoW5vg7mttVoT4Fth7v5SmK_vGG1EuLJQn07OhhLpEjNOargyhDnBZiep0raX9-YOfHL485wezDuesTeLwANs1Vc55yDj0afuTQxSFTdm2BKHNxZwrw9EWtwDSa0HS9wqbAwHt-fUat26AUCzkr4ggnBn8RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67735" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67734">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uwE758M2aFxDZDr6lzfaK_G6lbBsyiLWm3K3_FUtOYoHA7LxOQ4gxc27WtNicrFIPQwn0tSdsHdfhn0ZLObEWSsDumq4zTFd4_7Y2lxo0WbzrV4sqvMWE3VMAvFtR9rLcGWdhQH6bXYnxd2YFYT-Zy2cigStSDMNkbo9HPDGLbBs8_4EPGmzNsub6JGfNWojBrjaIZNkycjhp1PcKSVA4Fj9_4MrW5ejRpF7WtXFhc6mgKt3h_ZXu_xKuaqYIbzkgx31u4sZpC8fT4uQMEuanaY0z0PXKSN0zyi0FJmz1YhcZP60tBkhq835IjQ-uYgBCxkNuCR1mtIYfPf-Qi0bMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67734" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67733">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=OmygZ9pFKhpyr7qwtWMI5i56aQB5ybpHDxqVb5eQSqIVD9eXoTXZuP-r4nh1WfzuZg8kIN030aa57OKdV2AOzk6on1aVLGmqA43HPY-GajLk4oMTsAtFUWPtoc8_yRyy6qis44FhyOpoMbbCsG6gtJI4V8pqVxlkf8KB4SkrofqYZS3pQ6j4w-i8vf5gW-IYAdHijDkDi5Ys98qTdpf_JIZCK06xXk5deYa1rrJvx5piznS0ol_HfK8lECkWqAFdtmCZzzTMl6W8xrG_27d9P5pCXn96AUTT6NpFRMxEvo9GWyjfkJJ4hvuI93DLO9QHXeQkDuG7VGi3peioAXuvPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=OmygZ9pFKhpyr7qwtWMI5i56aQB5ybpHDxqVb5eQSqIVD9eXoTXZuP-r4nh1WfzuZg8kIN030aa57OKdV2AOzk6on1aVLGmqA43HPY-GajLk4oMTsAtFUWPtoc8_yRyy6qis44FhyOpoMbbCsG6gtJI4V8pqVxlkf8KB4SkrofqYZS3pQ6j4w-i8vf5gW-IYAdHijDkDi5Ys98qTdpf_JIZCK06xXk5deYa1rrJvx5piznS0ol_HfK8lECkWqAFdtmCZzzTMl6W8xrG_27d9P5pCXn96AUTT6NpFRMxEvo9GWyjfkJJ4hvuI93DLO9QHXeQkDuG7VGi3peioAXuvPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇷
علی خامنه‌ای،22مرداد1397:
به طور خلاصه در دو کلمه به ملت ایران
بگویم: جنگ نخواهد شد و مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67733" target="_blank">📅 17:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67732">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEHvbq0N-fwiWiK7xP4zsUOJPw7t2vbTxDxGX_e-kyoJEzH_Z3WdXZ1_DAeR8i-QJRPfomrbT1Ss1oFrpwdx66rW14Mb3tIBdTB3U9p-txxYZXC2bUviBOEKslkLe6L__mRE9kQRlvtDG00jXX-y5D8CxQfzcL7KuUbEJVhNvwmpREsGmoQ2IrUtLbP3OfoYMWPY8ArbhWuNuq2996X5E1i-RqN7q1Uirti1nY59TJniBqg1m7nVJxBDTRAYqXYMPGf67dMN8kXRWazxVrbLvJsrSj0MPWgzbzWWBEKN7l_z_7fapzv-DsCxu2g9T8gHHFnv60Y1rBua_tF8zbNtqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikirZfgEvO6tFbknoCub1Q-6K1XaRi5fgznfzOA8UiYZrMPSGJBsVma26oCcPkeMytt9rY59jzE395afRVIOB9W0NIeDanyIoOzNxkTB4w_wqV7mntrQdITIjTK5iQTBrjYJSUYC58lUkR5enqB7LNmtUObEcgbJ7x_nhvtR3J2JZMTwkxrCHUOVogQXzj9OSpDqRcAvTc6tqY5FfYmCfxv3jfQsE7wywrcOcrow3R4URDsY7iY6FVWB-Fi6Bho82WuqyIa5nkNXgBdnohPjpPJ3V2XPOeZE76x6kjoxsGFcO1yFVbg_Wxzf0aoMpTEJEooduafmDkhjfv3nJLvUFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=uP5HxSf7XMj66lpNjTeAv2z_Aqumnj62ahQfEO0yRvbx9bOlUM3iQneomYiqe5F-SnGIZGVEyAf2bOhZV6zGsW4ecrJXjWsPYpECq9H7lbfmWm8SKkQdH7sL2TQFoKjlJ9Qxlnh8IUTo_GcjM3VI4eWsz57GiRy2_q5iyQt0SgxPlKYf8Aqvzxmr7q-NhUh5BuivGhE2SPWDOAIsnxBkh7ouxUUCkpayLYkyeMvBpKZ9HfTvohnmuy1g3A7SQUFk9Wb4tud3ot72EqG9vn0hplruLpFjP9mzAoBqjZZFB3IaEpZ-S5d8PE63onMOvvPrnfGJteDd8qXypRewzHFRzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=uP5HxSf7XMj66lpNjTeAv2z_Aqumnj62ahQfEO0yRvbx9bOlUM3iQneomYiqe5F-SnGIZGVEyAf2bOhZV6zGsW4ecrJXjWsPYpECq9H7lbfmWm8SKkQdH7sL2TQFoKjlJ9Qxlnh8IUTo_GcjM3VI4eWsz57GiRy2_q5iyQt0SgxPlKYf8Aqvzxmr7q-NhUh5BuivGhE2SPWDOAIsnxBkh7ouxUUCkpayLYkyeMvBpKZ9HfTvohnmuy1g3A7SQUFk9Wb4tud3ot72EqG9vn0hplruLpFjP9mzAoBqjZZFB3IaEpZ-S5d8PE63onMOvvPrnfGJteDd8qXypRewzHFRzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpOwTWykr2lpbFvzi2uhcwA-m6IUfrsS7_BeW4iV3HGUwfg1Rqln6t5wl5Ah0exlkgfKI21-6KlsDmOfSSdqYm1wP8r5cM7y5vFMWwQ2McdRhAAIlXpoxfeFxkzDtCAoHUxjaW2zFlD8JDK8PuhxYJ1E0DSigGPXcUuMUxoq5PaLqz4BoIp9qFpioQxc4VAUy1n8qi4qKhV6qG_cIYlWmDFY5nsTH6CA_Na697IS9leaPlbtT6pbdJqClwYLBuh1BJ_cBuneu6w54Z3sSGMIR_Mu_UUApzczuYolZhjH8wrIiVMSemcXIxznUmTsImyzxz1wb77uDz5_dT5nG3JmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده(سنتکام):
❌
ادعا: رسانه‌های دولتی ایران ادعا می‌کنند که عبور از تنگه هرمز تنها از طریق مسیرهایی که توسط ایران تعیین شده‌اند، مجاز است.
✅
واقعیت: ایران کنترل تنگه هرمز را در دست ندارد. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از 800 کشتی تجاری و 380 میلیون بشکه نفت خام از طریق این مسیر حیاتی تجاری بین‌المللی کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67729" target="_blank">📅 14:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67728">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C_wybSaQyhW8Jwty8b9roOY94NhwRFo0EVWPIABfTkkbpGOaElr_kLcbCyqobKDg0hCzBK6kqgWlEVTDASAOmTbugoJAzg9LU1DapAyOw96wmaBoGNizqyrDIgJzFYSTBPPxos2BmLS1TyhEToXCh55CsJ5yJV3o-xv__mUHpOcKh2JuW1k-FKwS5dvUD3v9RfOZM1-zHZqnD7OpCVmroYM9NRaZ-kL1EHHqa8nkXmrrPvPQgLEcEl4DoV49X7Dq_0mg9oZI9Y1KE2fvSkyaa_kJ03wcDCL_P82IV1kNS8ObM8EJColKfX6Bc7wPOv9FMK76r-wsfzeFzOADdkvsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=Ca5v33SHSGwFQXutVh_SCNhdN_dh43a57eSf7zi_FsL6jXWGjf4kRusOwbtClO-hXR7U0Q7cMmj865zEV2MaJFw3IHi0K6pbCpiMr4HEzv-HnhimgaP00kjzcRQED6Bt8jpLsdWxc1iwFhbbByLSgTbzLYdBR-BOe4MpCQ-LDbI9DByJ6iZdCOqlIud6bcFspSR8VSe6XDjtyCi6MbYrod_eQ7Aez-acfsExYp0g9D1QMHNZo6nc3InQfcLr7HHFr1wm0lJVOUQIYtNuHJanxCP6vo56Bl7lpEPsUOjSagXMgtSTONQtqpwKL33hMJgP1LdMOYaGNPtLilqYM85Xsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=Ca5v33SHSGwFQXutVh_SCNhdN_dh43a57eSf7zi_FsL6jXWGjf4kRusOwbtClO-hXR7U0Q7cMmj865zEV2MaJFw3IHi0K6pbCpiMr4HEzv-HnhimgaP00kjzcRQED6Bt8jpLsdWxc1iwFhbbByLSgTbzLYdBR-BOe4MpCQ-LDbI9DByJ6iZdCOqlIud6bcFspSR8VSe6XDjtyCi6MbYrod_eQ7Aez-acfsExYp0g9D1QMHNZo6nc3InQfcLr7HHFr1wm0lJVOUQIYtNuHJanxCP6vo56Bl7lpEPsUOjSagXMgtSTONQtqpwKL33hMJgP1LdMOYaGNPtLilqYM85Xsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxgvdZop6FVj37lC_scIvFDCV06OcWzXDG7Ks2McG-Jd4W0rIYfrXEzJERY2_RBx5RCZb2KLn8hKG2P8lbESdukqAZ3JNhVJHACe1shkl60r5ON7JUxaaEkucFUAUPyT7JEgQhYB_m10yMOYeF9cdpbhEGApWjOU0VAnhp5BVLkZZnHGkp1ET9qEgwFShDKGtwqKCEG5Uory_qblzs2lC991Yl5o5oNvapffggZ9DqpN6B8mE6wcMAgF-TdlFp_ugBJ-FMG_B-MmHCP9y5Y7rFm83Vn00ezBsO40XB8TXAdRWnc8yhn9Vh5auAwunQSLRDRHp-SoSzsWdEBOVUDXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=BCzDnRZWrXvOIZMXoieEjEwDN9yDEHjzWt83Y4LRMUSHbh3aAJtV_J5V0nST1I-cJ4dYQdEw-FXcsbG8cU4k-rcslwhXKhe1KrM_pQhEF9lJhLRvWmGyd6fqX1t2efN62SRGz_9BHMtO8NNc1clDECrfO86qRGBCZNutitbvFrq7X-RmGarO8z-A5YbqHvUnHD9t817uqCoWKmsNKqtnQ1NFsJ1-9qGROazw-6o4ggPI43zZMOvShU5hcQsjQF8xIWCCtNufCGM8ZFnhyJ79w65RSfGQAgUavIXm5BtkJ-z4JdOIFnAjrOUIr-iY02gaEGoAd1cjhQbzPR-8g10aAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=BCzDnRZWrXvOIZMXoieEjEwDN9yDEHjzWt83Y4LRMUSHbh3aAJtV_J5V0nST1I-cJ4dYQdEw-FXcsbG8cU4k-rcslwhXKhe1KrM_pQhEF9lJhLRvWmGyd6fqX1t2efN62SRGz_9BHMtO8NNc1clDECrfO86qRGBCZNutitbvFrq7X-RmGarO8z-A5YbqHvUnHD9t817uqCoWKmsNKqtnQ1NFsJ1-9qGROazw-6o4ggPI43zZMOvShU5hcQsjQF8xIWCCtNufCGM8ZFnhyJ79w65RSfGQAgUavIXm5BtkJ-z4JdOIFnAjrOUIr-iY02gaEGoAd1cjhQbzPR-8g10aAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mRJFTmLK5b3KWvH3oSotQyZFGeWInIHZhIbZgAy1Bp16jlu2NQPIVVKJp_ZAajCPxIXkUj5maXvvdt06Vh9ovD7x5khTkrZiCMFs-usCYWhkcibUQ0DlRRF5o2abGKg6QDjxqQGNKNHU-wLNL54WEJ1CtSTAqqUPL28hnoCdS18fh4ESMPJP92C2SsHye_egpl9LEM5NnIKXvBvpxCWpTV0IpkEKy3oFoQauA87-n_C0i7Aea9Sa5kqtxqpVyfB18op7PecmgPs58wvUQ9sEJK5Ypk_-nJyfE0G6zOxqM2y5lKeBlVl6h0vrsJsaswG3WQ7rv3sn4Wx6DsEaNLlIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M21HeSp-GRI5RewVpRoWeOH4j2jleWQZOnlA0195Y7wuVvpE3qVimS9CfMazHn0Sa7KCZ_HrvlKIwu1FtwGH9rhzKbe0gPOwMWOBOLOVppRRBlWIkUDNry-NfrdaNa_XQGaQIuDf6Sa9qqF-hiWYp5vzHPSafbcfFPPFl3sojjSrRM-nStTUmM3OlLhWMiXAZ6kpfRvgvNf7oZzRr_n9HQrJHSjGVYJHkH3lhsx82n1ywCel9SkO613eLyC3y-lREUNrZBOUhRbvFfRzxvRmp14xSxEMPUKpFnjmGxUgU-LPfCaWjVtj1jXW1SUfkSQ-vFIjMOCH36tjHj-f_ZGPag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QxSjjOPPBHY515UZhwWCtT7lomRLfgRyRusAmEma9tz-KFEKyeDGQQ_-AZdgXY0t97t9t5vrwF_RTXpB1jvnKWGZ2KmD9qtqm14DiE6wxJ7PjWMhXj7m3nZZIegM5JFVwQ0C7JgNTHWVwoXVgPECccTsFX0JHzE7qOWnNK-W7Dq7L4fzkuqS3GnPIOxftcIvoQ-flU2T34potUE-w7S-YiX0J4elSeFZl0MOIhImWZ_fR8HOb7sFNMSaNpIcmbUfPLGZZXmHBo0qc-mWVDtWNRIweuYU1brmWCieZZazdVA6W-Udwj5q0lTGwECAraImOg88FOOu649G5eG7WFSwNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fF-aaqjN-wvpOacQ98fFEQYr3IZXmSkOawtAUYWF--pUS6m7Mf7JPwvst8ltn5f3weYkdMvsQbK9QeiL0lNYcbRk34FbOhKlsn2on7ZtzNBwuFk0m5AuoVkgcHNyUtt6ww0FGGPwwolPshFaEiIoddTQVaXFXFS8CXh05FoT9xr68COfwY0JkCTKPLD3JIlVmYcFYmVE7uCIdvoCz65VPDgCBTZXSU3NjzeSQ6vgF1xMH3IgtWX03EnWrSVizlUhgaJpjQtPoVUxvvPMirc0WrCVX5Y47abwUVMIvepd4D608VeWjMgEp9hpXTWr0E3KsoW68k3yByDQyXRArCV4wQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk2xVVCnZhcpb7cbjBg_rYzfLAJiCDGPLbQpiPgSMTYr4cVTbCGu6pQU_sBZe13V2Lg0HR3lxV8yU7fBJhm1y-ssD6_t11EnQaT7Ehmz69oYT_ZDgDqZVMrDdjEQ6SBOtLT-O-KjsupxKP4WyiQyjwvNOBgmsAl86QQfRAX6-Bay86HBzXpDXOM_MORHcRDp7Fg95tug_GYJsdaWjYJ2o2X9eq2q3i3ahRFeD4MxWa9vFaS0lrgAnW8YS6FfKw8j-eJsLUlxVmD4_vpPZ6Wy8WBzOtjCUVQ8G2Mz5EGIQtdz2gDtWMo6lGssiZ18T6ztEnP8IZiOS2WNcs-h0za8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHOeW2NDcVq6GGsucPxoSXoT1noVzyz-qliExbeD1x9SUM0iK-CP2fTXmcFwDJ3cOsP-5VP2wlbh8E1vo1kYAXOmKdxWbrld9S-Re4-ZDg3voeZdW40h_6WiGPApLoQpRKEsn7jBcX0XkdqqIc4tBXb1TXnuCOUiYZboTaoG1Tt-dylQr4JvDOKCR9Q-0YdpVneVExRAkpsn9XXnwaRUlGaMf_xgVzbsftdl5XxEipT9kUCRAIkohNgonVdUezITiDmw3590VLsZdIWtuXhVABwpqyUe5HvKi9qgKpm7U0NDskC3Wl5XU1euCLLFSm-GmWguZKyfratN__VyFHu7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=M2p8pyEDkYwJ6Cy-fmY73sSgPXwT9-iIwhP6trYIOfWcDKBAAqWSIif39N89P1BGQ6lWbWrSF7bSsQuB5dH5HkE1yE6M8oDoQnK2UlgBKha-JSaTJ6wiTJyFdfV3tdEFXXOVmUS-reGXZSVC4xw0LgLuWJwuxdi64IQD8FXZW8IuWSAJd170jggAM_VJYdWGAWP4p_k4BkcnHIRe3KOUbAIF3YAxzL3DmrCJ-uk-s3FL0KSaV4XBZ8vTC3HGluuyTS-Mb6GMB1IPf4pToUTZ-57zoPYT7e4Q2uGvrj0PIlFNE7-UsOJZMV8is4FXozYiDmkORTMX2ZuJhe6Z_R-DDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=M2p8pyEDkYwJ6Cy-fmY73sSgPXwT9-iIwhP6trYIOfWcDKBAAqWSIif39N89P1BGQ6lWbWrSF7bSsQuB5dH5HkE1yE6M8oDoQnK2UlgBKha-JSaTJ6wiTJyFdfV3tdEFXXOVmUS-reGXZSVC4xw0LgLuWJwuxdi64IQD8FXZW8IuWSAJd170jggAM_VJYdWGAWP4p_k4BkcnHIRe3KOUbAIF3YAxzL3DmrCJ-uk-s3FL0KSaV4XBZ8vTC3HGluuyTS-Mb6GMB1IPf4pToUTZ-57zoPYT7e4Q2uGvrj0PIlFNE7-UsOJZMV8is4FXozYiDmkORTMX2ZuJhe6Z_R-DDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQFnEuK4xX2ddlVkxBVG23jYGnnxpVm36nZ2FFbd8vb6lhdzeNFmnvOzilHYm7F6GmEkpzTBuYmGaj4B2FOffHz0h8FUAcPQWq6UoKpSqEpzmznpvS0m0ycwCsh7yw4eKSWtuxMz4KwRJXLMobchB6TDwT3ZUUzg727C58pgT6AyeF9zJqJ33bx2ewJeQ-GdlLnX5gY05d7DDJCB_adyOGpnp5VseO94NmCdvaHXkD5BnetoEtEwO2yWmRUEnnJ0FWB1DxTTFz_HOfJJBYjpDljbo-Wx5_1gwOdXrRqPy4d808ipnNzCCG3J9i5nu6nUa9n9CjuqIhwPbJ-QL0DpnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6EtyiofmiAXnQqVm7DP0os5gjwKFXT3AS8Qal_fP9GOB6dnQGv-V-w4n5XjYc5AgsLTYbrH_dUotpQq7OtxRvCJ8M_hGXEUVgzjYh-nriZXlgiTE8jp9Gs4nVi4AK3ruv_idOjmkoJpNf3u2mRamqpOK10fqWd6XQiXzvpFFp--d0wQchCT4MSLoS-MWAmEcywVLr3y84-GIKweVegxMSj248aV-b1dM40Vb966EKE825AwHgpaB-37yLsUvmAZrYCA1ztc2_Xn3lmCVzfK2OudAi3jaVzVgikSrLg-7_9G6O6a1T62ebeqM-4fV0z-nnfcGzExkk0M7_Eu1N0RnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOmAftCCXswoKXHf8x6oYl9eSsVnBB16FzAq917Jy4x4Ud-XY2es2jzkvVWSoZmdUY_r3M2mz-KGzEAy_MKHdtQ80BqjAZ8KN5br9ftCv1b8iSiBVCNFsimRFba6xNkKHOQQqEkOlLqSIOrlTbigmLYIvUH75y-C-_A47jkTOGXJRgsJUKT09K77owpAbpuxgWpsZtmDye_EkbCVaJYjHVQJhxHxIneDFYcuhc2tLfs7WH0xdFIeNSn08LL7KYy9EXxmVXJdd-Bk6VUjCjz5ONFxugpyLZEFH6zBg_eTaHto8Gf17UABr80hEBVKNLKHLsrkeeCEzWp0B8UbWTYQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
