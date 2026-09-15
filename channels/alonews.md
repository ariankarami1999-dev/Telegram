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
<img src="https://cdn4.telesco.pe/file/PoTRiaYtNAYva8iG6vrNBT9ZG6y0o533YDXQ6LZXV6Dg3V2B64eOFqL5IoiyDGKh6MwKJItW_23UIP0txMRuLntZaZfhp2SO-pZmdPlXwpMM4MpfwHUOf-1b9rEA7BYMdUaXES7efRcbH5VbZECi4jj8FNi_5jewXeZmFIP0VP7m_4du4K_kiyT7F1d5O-hSDuGikcvRJA1Tiqpf3u4J7gh9dOEawZQ-6wGp66x19ztHqjIJuocLEWqUpLS_D_DuKobMCb6iaBFjiRa3XmUdo-j-aotVoS0IEIql-XtRXgTsJIa4H77b5etyZByd8bvWF582g3HQPb85Q1LGpV-VHg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 910K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 04:34:56</div>
<hr>

<div class="tg-post" id="msg-147490">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاکوپینگ | EcoPing</strong></div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/147490" target="_blank">📅 01:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147489">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
جمعی از نمایندگان مجلس در بیانیه‌ای خواستار تجدید نظر عضویت ایران در npt شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/147489" target="_blank">📅 01:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147488">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0M9nnA2nXryb-nd1dUwt_s1Zmi2Nh92rhWcM8isZGuzgtvL5iexax0VACQwH6-yYNTBJCVESduR1ayekCYc00m1DrrX9oVGP2LA4SbGdMs19pKjyVIfIDqwMiYEwNxXWO1egdxfpFueOMAcdaQRJSqen6_u6S2zOqkqSpSCgr2zbZjRDSJuwleeLxSNeBpXZxUlXY82pDyiQpYS_ngBEUbcQrboLoylxzLrroRkTIicEeHsIOxeedCIM0xmHCzbPgcWPDyVsijy-NE0dTW7swF4BQSfPdvcvswqlvbuAlfX_zkKNEv7t-OemIRP4BDtx52AmHVKoswwLT26niKnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صمصامی، نماینده مجلس: 56میلیون بشکه نفت تو کشور گم شده و کسی گردن‌نمیگیره
🔴
پ.ن: حدود 6میلیارد دلار یا
1,410,000,000,000,000تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/alonews/147488" target="_blank">📅 01:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147487">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
گزارش‌هایی مبنی بر شلیک توپ‌ها در منطقه المنصوری، در جنوب لبنان، دریافت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/alonews/147487" target="_blank">📅 01:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147486">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/147486" target="_blank">📅 01:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147485">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI_e25j8aVFdDf7XYF2n0oGDFF2uwwCemfhHfPSi16oyhvbwj6-lcLUVuOYaNecSWSJK-glBNAMrzRrGsA8Er7i9eEc1dzZlEUrjUf0D7sZzDKzMeLSeIDA0XXq1Js1kNNDELt151Nc_R9gF5Q_3DNgQozYn6jLIQMXdwnrntAFtupkE0T2YmZBGFvZfJT8tfJQO5fIchh6eVCNb_u5ygm_STKUjMrA0e5vxpcSmYO7O9UlW_wJWQg_rQBi6diT48tbFwm8spt9McRUKFQbxIj7FhhiIK2trM_M7gkKbEHp2DY36TyYE9OV6jRFd-f_dRxktZkSeGe_A1jJak3rQMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن رضایی: تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود. تمام.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/alonews/147485" target="_blank">📅 00:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147484">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
بنیامین نتانیاهو میگه جمهوری اسلامی به آخر خط رسیده و شرایط برای سقوطش فراهمه. گفته هفته دیگه تو سازمان ملل درباره ایران حرف میزنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/147484" target="_blank">📅 00:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147483">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
۲روزه تو سوریه شدیدا اعتراضاته اما فعلا کسی کشته نشده، عوامل موساد فعلا نرسیدن اونجا و تو راهن
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/alonews/147483" target="_blank">📅 00:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147482">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnEZPrd4v2I1G5wJhcIwc3zC7d5Gbxdvco4fE2kZuDQhazcbB_xdxv3Uqqvhi6zfFf495JHuJA8VIBqlu0_IKm2tkyOnnJFMCZznz6_OOAb1xZZAfZzjolfqzW5JSxParvl5rfN1JWUn-t7LAoXlq_iyYFchsf-lZELM5uQehlpvFKcqb_5hrgWxEliGNdvPOO58pEc9QhQ3-KW-PJ9staGPEeXjj0uGRfLYgsBAacNaBweRbj3KB953OwqHDC14CviPHpB1OeiSkVgcOohFIk3jm-XdIqg5B6ONN5KtJly29uUtLrvoMDj5aQi8Rwj-vhnW0Qz94U7gqfAxSsdvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید ترامپ:
من متخصص افشای حقه‌ها هستم و همین الان دارم یک حقه دیگه رو هم افشا می‌کنم؛ اینکه هوش مصنوعی قراره دنیا رو در اختیار بگیره، همه‌چیز رو ببلعه و نابودش کنه و ربات‌ها قراره وارد شهرهامون بشن و همه ما رو از بین ببرن.این حتی از ماجرای «روسیه، روسیه، روسیه» یا حقه تغییرات اقلیمی هم عجیب‌تره.ممنون که به این موضوع توجه کردید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/147482" target="_blank">📅 00:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147481">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoP3Kqw6p40nD7F5R8SB-nlTo-WxF-5LVkB8iUHTM2AUZ9J6nAnVjjV9CkONpbM9Yfg_MG_4pEV9ItMmQDRen8qaUt8pIkb1CjbXtXTh5HTmSRmBaZHl-aA8xYyGeUCVZW6-1ASEeUrfp9O0825jS8SRO_k6hy6x2ENrsmUiGhK4izWQEb9wD82oNtk4gduRP1KaMqrKPtd7EuD1Fujfhc6LxZ6zOjl-M5vI-TyxO_iw0dUX22d3SFDSjYLUMM7oigoXmPVt2fyW5Yx4Y15_tz0tD4LGNw_w1xGwzvkm8AcsAYocE8yWZ7AG_62p0GU0M18ADjPfjdT6litat3-MSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همینجوری گذاشتیم تا حرص بدیم بعضیا
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/147481" target="_blank">📅 00:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147480">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534f93c783.mp4?token=Sh6yPQlIGoPsHJdq62eDJxRhewBiMByyQccTNIzcSmJk8ucw_CauD0m1rIfHCt8L-8nw2HNVKt9rhVchIpxP3JDbSN0KNuEHg4WRHytfAcdrO9IZJodXlFExwm_BLXIbpnPRjQ3cTLNmBH1tHV1Sep__5l5DmCSBpJ8vqlyWzDiiAnnCnHBtXAieBQ8lPEbusH1Za_UleNHRbi4OdUNhu8m6ev51qOaF1O2ZJMya4gNQ8xIm0tFWqBh1i1rhkczu1rMwt4MTW7x3sKhkmuSKKGs2TyP77wOCOcd_JnyQbZ5x1Y1UiHDHLlTL6dyWXF-j51mdvEeXoDbDK_9IpCgFZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534f93c783.mp4?token=Sh6yPQlIGoPsHJdq62eDJxRhewBiMByyQccTNIzcSmJk8ucw_CauD0m1rIfHCt8L-8nw2HNVKt9rhVchIpxP3JDbSN0KNuEHg4WRHytfAcdrO9IZJodXlFExwm_BLXIbpnPRjQ3cTLNmBH1tHV1Sep__5l5DmCSBpJ8vqlyWzDiiAnnCnHBtXAieBQ8lPEbusH1Za_UleNHRbi4OdUNhu8m6ev51qOaF1O2ZJMya4gNQ8xIm0tFWqBh1i1rhkczu1rMwt4MTW7x3sKhkmuSKKGs2TyP77wOCOcd_JnyQbZ5x1Y1UiHDHLlTL6dyWXF-j51mdvEeXoDbDK_9IpCgFZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یادی کنیم از این کلیپ تاریخی که چند نفر میخواستن با برنو، سوخت رسان و جنگنده بزنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/147480" target="_blank">📅 00:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147478">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2qS21tU2uCrWcjBAsDvejV-PrObsKeAcGkrLgXvV-hwrxE_lAQK1hE6dWwDvVkm6PdvbiLfa6xrLNRs0717HEfeBbh5p1V1SiKgHIOD3RoUO0PtjkylKxXThf9qA_nSPJdU40V8fYqcQzzrnXY6dAcizpJVBlIBuiqr7Zwb9AYxKpnUHSTdnmuhQhh_6viwmNL18AsOyVOzUPRyXU8M_sAbt-lw4yvilQFDwkRqekLVeoaP_0gpeCeGTiAbvmZCambxM9wJ88WuctB5ZPK98mrphRDaxqzlo5h0-EmHmC-7P-5TcbTdBOOIM9Zhc37ohzjkEcEh_CTdebtfuyyRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سریال خاطره انگیز قصه‌های مجید به دلیل اسم بی بی دیگر پخش نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/147478" target="_blank">📅 23:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147477">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lw88TTilUvP3DTWDZ5HrbU8ETKx6F-0grbaYqeyDfpvoYQfse-TiiGdRBkF_E8_gG3qjw8pb6_Zzo8tRFqhEgOqifrnSfAM8Ak23uGtqX2crdKrMT1qyGHLt4cMmwJqk8GcD0XFKXg3v0dg28orbDleJluic7fEPDRP6YzfkE29YxTSs2jAxFcw1NkTt9SMayQYY8cr4YR814dWCAjPkpYI8EEC1ojbO1uaqgxkzcOhQeEYRYxnFwKGDtFX5flnEmUyqnTBPasCl2LqImRRd1PKI94YoFo0WKzTUnJ0JRqi1mrwl_bTO4b46j1EFWJDNzOggFf0Mwjq02fH-e1-VpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هویت ۳پاسداری که در بمباران آمریکا کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/147477" target="_blank">📅 23:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147475">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⚽️
🇶🇦
| خلاصه بازی استقلال و السد  @AloSport</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/147475" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147474">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPZesO48SlL3-z3tUhbDhxDaM_vceDZjs5mvR_sXCmy2PWZEX-6DuTzeV9sU2DX5hWAKTQMrhtrQqxrNSjIdTPMi0vhmrABlTww6fpnnB51DxJ5Y8eEmZfzL8dCcFn0EGyLWLmcX4xeqeqN8dx4BzDpQRZZUZaHzQQz9UjOTEZnVLUo5HNfaJ76kwFQUPG6oE2Ea_gxVm4o1TJEIw3Xkp9XJsnCzIIr87L1CtruZWLm7c_ikx0rFN2mL_9QRQILC6PRMmlz35xq0zIaR3fdLIWI9PQTe7zNEAJ3fsG7C4lOswh1dYkq755xzn7c6EwL8Bw7-FtsraIzgRJzfjad5yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط، فصل جدید همستر هم شروع شده
+اونایی که از دفعه قبلی جا موندن پیشنهاد میشه که حتما این بار برن انگشتش کنن که آخرش یه کیر چیز ببخشید یه پول بزرگی میزاره کف دستتون.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/147474" target="_blank">📅 23:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147473">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">💢
بیا اینجا بهت میگه دلار و طلا رو کی بخری و بفروشی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/147473" target="_blank">📅 23:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147472">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOHhm1UNwYBO7Q7dxmdKNXL-5BRFyOe_5ir2MONGVPCKOvPja6spTj6AFAjEwYrHrp3ZoBIXFxVU4SZha8weU7edE3igNlO8YdS1BHquyCanIRyLatjZHubdzPTmtQy9nqznsf2ZgSSMId_UOFwckObxhsj5mC5WtAlv7lXHvmlBZ_SGpWOE2Kloi9VA6r_CAJWsT7i13UM_APNJ-kJIPlWUDfYfV4vh4yW2O5t7sUHzV8wRk9YnYBlVGpajQL-jRmle62XrSIRuDje0ZyVyE59JwGm3e6KIsY281O0Ze83gP-oM9WIrrqxSxAoc2sNHaZ4B8oO7BwbAe_So2RJjHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
کشتی نفت‌کش "ال گایا" که پرچم پاناما را یدک می‌کشد، ماه گذشته مورد اصابت یک موشک ایرانی قرار گرفت و از کار افتاد.
🔴
این آخر هفته، ایران بار دیگر با استفاده از یک پهپاد به این کشتی حمله کرد، در حالی که کشتی در آب‌های ساحل عمان قرار داشت. در حال حاضر، این کشتی توسط یک شریک منطقه‌ای به کمک یدک‌کش کشیده می‌شود.
🔴
ادعای نادرست سپاه پاسداران، نمونه‌ای دیگر از دروغ‌ها و تلاش‌های آن‌ها برای ایجاد ترس و ارعاب است، در حالی که آن‌ها سعی می‌کنند تردد کشتی‌های تجاری را در تنگه [هرمز] مختل کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/147472" target="_blank">📅 23:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147471">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پزشکیان: نمی‌توانیم تصمیمی برای مذاکرات با آمریکا بگیریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/147471" target="_blank">📅 23:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147470">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWtrEV0IbsyJShYlwMpDOceiv8XaAND0ANJYFr-ck3cO6Lc_qrtUQXxXBayksjEYZ4S2Tq7vu6ibIidTQKyzdwK-J2ftKwgs9zrGwBZ-xlBNDQbx1RUzu9BuVjr-BuoiWVr8335_C82c7RZ3tMQWoIodSInJxS2vBP6KEthdFzTdHf5Llw3OsRe4w-Ux7ZDLJ621ViS6piCds8fTBLdX7A1k0JwKb7r4rEc2PdWwj5zQKqNStEeb78DKiNNV2Gc9qg8u6jT7P47mABcDujaBpFGUDCvCrKfcPD0ia2ehs5Tm3ZUh55Fvijg3m7yXTyUMXZIT7tMtkvbsnWzmXsLsGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظرسنجی کان: ائتلاف نتانیاهو و مخالفان هر کدام ۵۲ کرسی!
🔴
بر اساس نظرسنجی شبکه کان اسرائیل، ائتلاف نتانیاهو و احزاب مخالف هر کدام ۵۲ کرسی به دست می‌آورند.
🔴
احزاب عرب ۱۲ کرسی و فهرست هندل و زولخا نیز ۴ کرسی کسب می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/147470" target="_blank">📅 23:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147469">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
تا انتخابات میان دوره‌ای آمریکا ۵۰ روز باقی مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/147469" target="_blank">📅 23:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147468">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT73UCN7_rxkLJSNErKdIVZvW7lfzpBExkhJQw8pltpriqy5-10-vSTboA9Dz9ZindQahhe78HbjARkZ653QLSiXWi6WNXp1XPMkxkVpg4hi0pFEDv2g42qbhjAGJ6CGrXYpDN2c1ZzvoMqydPACB0S0SzHzfmllkkdU6x-PESNmwcUfvh9iKVES6s7Z0_nsdRJ-NU6ZgKRyrwxSU_FNJ-hgyUxk4zxxSVRcbXiF4vPOVkZpnPovenMPslwTag89-VLWg3Ak3Xby7qlzglItqnYW6bDDLnql9YW49cjlwVO2fjGSLbg3zW1f_taBiLQhP66JQPJ51PLQMVxip0o6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور: اصلاح طلب‌ها یهودی هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/147468" target="_blank">📅 23:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147467">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‏
👈
فرود اضطراری بوئینگ ۷۳۷ سپهران در مشهد
‏
🔴
یک فروند بوئینگ ۷۳۷ شرکت سپهران در پرواز مشهد ـ کرمانشاه، پس از برخاستن با مشکل در یکی از لاستیک‌ها و احتمال آسیب به موتور مواجه شد.
‏
🔴
خلبان با اعلام وضعیت اضطراری، هواپیما را به فرودگاه مشهد بازگرداند و هواپیما به سلامت فرود آمد.
‏
🔴
در پی این حادثه ، باند ۳۱ چپ فرودگاه مشهد موقتاً بسته شده و احتمال تأخیر یا تغییر در برنامه برخی پروازهای ورودی و خروجی وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/147467" target="_blank">📅 23:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147466">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
پزشکیان: آمادگی داریم در چابهار با هند مشارکت اقتصادی کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/147466" target="_blank">📅 23:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147465">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
گزارش فعالیت پدافند هوایی عربستان سعودی درپی حملات یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/147465" target="_blank">📅 23:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147464">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پزشکیان: آمریکا راه غذا و دارو رو بسته. آخه آمریکا هم انسانه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/147464" target="_blank">📅 22:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147463">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پزشکیان: با عربستان جنگی نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/147463" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147462">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
پزشکیان: آمریکا چون نمی‌تواند رهبر ما را پیدا کند، درباره سلامتی او شایعه می‌سازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/147462" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147461">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YM3JQzUJ5fS2cffSxkuxjdfHCjgGmlIaPLuWNaQop1Jg0gv4XDkrklXtnPUx2kJ7IOlDEF4sc8_obXG08HT1_FFU2cbv7_LHqQ0XluVmY8cg75Sn2AUWV229wRcM5olfUe9UqIZi2aWlc6It_6v28cbtxy4qJ__Py8vyzOj2Yhqytfvxta95Pxx3pPBKVOAnbeT2MXRTFfVQU3rT_pdWPOYmqACWyru441gDzPrcwsAirBlzX0xzDbqn7DtS3Wn_x-R93Y7IJWYbHSXQV227xsZm0CbaVOIHSXth_CvsKDqwKhuv5Wxt6zsvfuxR8-Q3WPWpTItuHe2BT0uKagk2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انتشار جهت حرصی کردن بعضیا
#افتخار
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/147461" target="_blank">📅 22:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147460">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zj682yRoWqjoeORma2ANEnk7hdf2fKihxToFJ3OziRadtyf6E3V18_Nsh48X3TGtDVktFICrZpj3GM4zZ1PWrDDTTF4N5416TdDvmZLOLfjI84D06ZRacVf4K22Pvi3Ob5cKvnsrtpwiHhIG7Mvd_Hzl8qTicdS-aoGl8bvwKSZbSNyHcnLD5ZG4IaXE6wcG9zS8xNsPSfGdeky318xTFs7NWyL8eXSEemW38FX19FXB_0OWikSkrtPMpu4CUw2m8_omohzqx8P3VIQxIh3aBEJ3mTG0FqvPdzu4pyO83czIi1aD7iykVRh3A2lupBzF7TDP0XDZnks-DYjSzgAUrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوپر نفتکش «الگایا» به شماره دریانوردی 9325336 که قصد عبور از منطقهء ممنوعه در جنوب تنگه هرمز را داشت،بر اثر برخورد با مین های دریایی منفجر شد؛ تلاش برای مهار آتش بی نتیجه بوده و کل نفتکش در شعله های آتش گرفتار شده است پیش از این نسبت به خطرناک بودن معبر غیر قانونی هشدار داده شده بود، نیروی دریایی سپاه با قاطعیت اعلام می کند تنگه هرمز مسدود و همچنان تحت کنترل هوشمند ما می باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/147460" target="_blank">📅 22:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147459">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
پزشکیان: مشکلی با امارات و هیچکدام از کشورهای منطقه نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/147459" target="_blank">📅 22:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147458">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bx0nHfTUPYCVzEKEesmEuYmkOLJcYxDCGF-LjVOsxsmNieJ31spTlratrukztlXdMDfhQ_2T4K4eX0BxQ3GI3-9DCdyENIAgHEBLanWM2HUT-uauTbh1Ar_4gV80lVU-j35bz40HZUaeFv1igLOJ-dKmDlppWHFjSNTV32VMr4SfOzB_L6vF1GHqoeta-ZTFVs7y3suetuKyNDoUsznsxQ70a4GsxgLbxlOTx422a9OAwfoqI0SUNlJsW23JSMOnBs7X6cMkEFyiiD50VojgB7D67w1iyQ6I8RAIE6uib7wSIZuaPRlrWEJWlb6qj0Pst9drBMrweR1X0B9zWCYyXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شماره ناشناس تلگرام ۹۰۰ میلیون تومن
🔴
شماره ناشناس تلگرام تو ایران حسابی گرون شده. الان هر کدوم حدود ۹۰۰ میلیون تومن. سال ۲۰۲۲ میشد با ۲۰۰ هزار تومن خریدشون.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147458" target="_blank">📅 22:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147457">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بچه‌ها این گردونه صراف رو چک کنید، من الان شانسی زدم ۵ دلار بهم داد
😐
😂
انگار اصلاً پوچ نداره و به همه یه چیزی میده.
برید بچرخونید ببینید شانس شما چیه
👇
https://r.saraf.app/s/agrd277</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/147457" target="_blank">📅 22:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147456">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
به گزارش نشریه فایننشال تایمز: اعلامیه دونالد ترامپ، رئیس‌جمهور آمریکا، مبنی بر برقراری آتش‌بس در حوزه انرژی بین اوکراین و روسیه، مقامات کی‌یف را غافلگیر کرد، زیرا مسکو هیچ تضمین معتبری ارائه نکرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/147456" target="_blank">📅 22:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147455">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: هدف قرار دادن بانک VTB روسیه در نتیجه دست داشتن این بانک در دور زدن تحریم‌های اعمال‌شده علیه ایران صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/147455" target="_blank">📅 22:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147454">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
بلومبرگ: نخست‌وزیر بریتانیا، در حال بررسی درخواست‌های عربستان برای حمایت نظامی در برابر حوثی‌ها است
🔴
این درخواست‌ها شامل کمک برای دفاع از زیرساخت‌های نفتی و جلوگیری از پیشروی حوثی‌ها به سمت تنگه باب‌المندب است
🔴
فعلا برنهام با اعزام مشاوران نظامی بریتانیا به عربستان موافقت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/147454" target="_blank">📅 21:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147453">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=GbzCVwNE9BBioNUICP5pQXccWUumspMpeHWfGBG9bn48RaoK0TZUhytbRvS2I6nk2vq0ZNZNTsvoJm1cR8p4ZXdqcV8QhLlDT6rOGk9KQHUB-0cZI7fHoU4SviFSgv1-Q5X7GIZ9iumEo4KRfACNXlbyZ9qJX2p8dxxxU85oMkngyQv8fhn7fssZEckrnJ_a4mZBFgjilrlZ7BqUSU0YTh0GiKHtNucUl5IB2jXtsfZ94J9kozWqVAZb0EJ5wcf2H7l7ttKx4MsR01R94cgAxqCQ9_TO0vA_71aRDCZdgWs4Bbh-O2p88HtWZR63OxvWTzAinND4kVhEpLsjYxmvIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=GbzCVwNE9BBioNUICP5pQXccWUumspMpeHWfGBG9bn48RaoK0TZUhytbRvS2I6nk2vq0ZNZNTsvoJm1cR8p4ZXdqcV8QhLlDT6rOGk9KQHUB-0cZI7fHoU4SviFSgv1-Q5X7GIZ9iumEo4KRfACNXlbyZ9qJX2p8dxxxU85oMkngyQv8fhn7fssZEckrnJ_a4mZBFgjilrlZ7BqUSU0YTh0GiKHtNucUl5IB2jXtsfZ94J9kozWqVAZb0EJ5wcf2H7l7ttKx4MsR01R94cgAxqCQ9_TO0vA_71aRDCZdgWs4Bbh-O2p88HtWZR63OxvWTzAinND4kVhEpLsjYxmvIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوش‌چشم، کارشناس فوق‌ارشد صداوسیما:
در عرض ۴ ماه موشکی ساختیم که هنوز اندیشکده‌ها و رسانه‌های غربی حیرانند سیستمش چیست
🔴
موشکی که بدون نیاز به ماهواره، ناو در حال حرکت را پیدا می‌کند و دنبالش می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/147453" target="_blank">📅 21:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147452">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نیکزاد، معاون مجلس : آمریکایی‌ها برای خلبان نیومده بودن،اومده بودن اورانیوم ببرن که شکست خوردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/147452" target="_blank">📅 21:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147451">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری/ گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/147451" target="_blank">📅 21:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147450">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری/ گاردین: طبق گزارش ها نخست وزیر بریتانیا در حال بررسی اعزام ناو های جنگی برای حمله به حوثی ها در کمک به عربستان سعودی می‌باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147450" target="_blank">📅 21:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147449">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhOMrgsovJ0naA8MOu9V98aXKwptd5Sy43J_VxXZdwWq8vTGN3CHH2pwtkDhN0Z7eMHLY54BLQAzsxMhEIGrTtu0LvS7VNxOgXnC61p9SF5Hi2Dq4dlzzAupn78tc5ZeHyWMvmaNmFe1wGz6aznBKirwINaeldWW6QjMSClrc6GzKpbcKYGRVBZjZYB3B91gcJGdXysL42HlQL2tOn0xfhnpTSXV-CtsI52QjWVyS1gp8pkrcwJxNSzjJnLf2oXrpK-0vr8V7eB6QC9VNLCuXzwd_nUn7v8D4-ZDVIA8OXc08BzpmBAJAtswebCyLquBoDc72fttVA08ZkNLtdUnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: در مورد هوش مصنوعی، در تاریخ کسب‌وکار، کیست که رهبران یک صنعت را دید که برای مقررات‌گذاری فراخوان دهند که اگر به شدت اجرا شود، آن‌ها را به فراموشی و ورشکستگی خواهد کشاند؟
🔴
هوش مصنوعی که دنیا را تسخیر می‌کند، بشریت را ویران می‌کند و همه چیزهای بد دیگر، یک دروغ است؛ تفاوتی با «روسیه، روسیه، روسیه»، «اوکراین، اوکراین، اوکراین»، دروغ استیضاح شماره ۱، دروغ استیضاح شماره ۲ و همه دروغ‌ها و کلاهبرداری‌های دیگر ندارد که آمریکا مجبور بود از طریق بازی‌های کثیف و رفتار غیرقانونی ویرانگرها و منحرف‌ها تحمل کند.
🔴
رئیس‌جمهور شی از چین تازه اعلام کرد که چین هیچ کاری برای جلوگیری از هوش مصنوعی یا آینده آن انجام نخواهد داد.
🔴
گوگل اخیراً اعلام کرده است که می‌خواهد یک کارخانه عظیم در فنلاند بسازد، فقط به این دلیل که دریافت مجوز در ایالات متحده را بسیار دشوار می‌یابد.
🔴
من از این موضوع خوشحال نیستم و می‌خواهم آن‌ها فکر خود را تغییر دهند. هوش مصنوعی و مراکز داده، بزرگ‌ترین موتور توسعه اقتصادی در تاریخ خواهند بود — بزرگ‌تر از نفت، طلا، الماس یا حتی اینترنت. این روند توسط نیروهای ویرانگر که به شیوه‌ای درخشان اداره می‌شوند، در طول دوره ریاست جمهوری دونالد جی. ترامپ متوقف نخواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/147449" target="_blank">📅 21:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147448">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
یمن: حملات امروز سعودی‌ها را بی‌پاسخ نمی‌گذاریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147448" target="_blank">📅 21:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147447">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
فوری / شنیده شدن صدای انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147447" target="_blank">📅 21:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147446">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
امام جمعه سنی مسجد محمد رسول الله زاهدان به ضرب گلوله کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/147446" target="_blank">📅 21:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147445">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8571b00e3.mp4?token=BBSLpled0H_dQX6ixmv7z4SKoAXrmDcr9l-HIie9qU-F6Yu6OFOoHrrUhf3hqs2l_UINfFWL5XsGuSQUDhVbXiFl0rhX88sa4E9sY02kAikuyZe0dW3aTtaH6aGaPeN9cFG7cARSbreI7z0hm6rF15P-CTWra88dea6P_7wTct7zgTbONPBUnGQFQivsEuNhcK4QaWl8Q5CcGdcdICQOZ6sBAvtywHK6w95caWQTzlw15BZW4me16jSO0SOaynNzHcIsuJwL2nbLKgiCbFE6RAEUOmswthCYoXscs5-WSrYmtielBKCY3jyZernA7E79IiRwBjbC7og87Yh-mEHlkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8571b00e3.mp4?token=BBSLpled0H_dQX6ixmv7z4SKoAXrmDcr9l-HIie9qU-F6Yu6OFOoHrrUhf3hqs2l_UINfFWL5XsGuSQUDhVbXiFl0rhX88sa4E9sY02kAikuyZe0dW3aTtaH6aGaPeN9cFG7cARSbreI7z0hm6rF15P-CTWra88dea6P_7wTct7zgTbONPBUnGQFQivsEuNhcK4QaWl8Q5CcGdcdICQOZ6sBAvtywHK6w95caWQTzlw15BZW4me16jSO0SOaynNzHcIsuJwL2nbLKgiCbFE6RAEUOmswthCYoXscs5-WSrYmtielBKCY3jyZernA7E79IiRwBjbC7og87Yh-mEHlkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور، جی.دی. ونس:
اگر شما اطمینان ندارید که دولت فدرال از پول شما محافظت خواهد کرد، چرا اصلاً مالیات پرداخت می‌کنید؟
🔴
ما تلاش می‌کنیم تا دوباره اعتماد مردم آمریکا را به دولتشان جلب کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/147445" target="_blank">📅 21:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147444">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سی‌بی‌اس: در پی تعویق مذاکرات ایران و عمان درباره تنگه هرمز، قیمت نفت به بالاترین سطح خود در چهار ماه اخیر نزدیک می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/147444" target="_blank">📅 20:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147443">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sigVSY6nwCPdf0PalxmyMVsgOTLdTl-LufW0cIBeWdEHWCROy44Fvi_7cavxrTHsOIXP4sh8ZG7LIWLm2I7IuuRZvUPylXnF047OreZKeNpdOI_VaNmaCPtj8HdGt5X2zTZqg6ZMnFgvRC-0zlCoT1JuFNJIagKCxfBRyED5pR778f0FM7f36RDns4MRKhMZbfL3ll_YCPaFbIHHOKbVNFRMd39-7J2kI8AqQdpeetrOw3bDa0ZqvGQ-7UtZ2Ke4dXvxSbCCdzj3piRL_h8NsfctKhW309S6rTq3b9J8wZhRwwdwZO1TW84lPaEpie567aI2uAAzMK4KZe02WPC5yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیامکی که داره برای جانفدا ها ارسال میشه، از فردا رسما جانفداها برای شرکت در دوره‌های نظامی و امدادی، اعزام میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/147443" target="_blank">📅 20:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147442">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/percFomUt960uQLuKavRNess5jw-r8r-YcWgKswfQomeXPvcsYJ5CFmKI2aRb-qxHnVIJ4AQjltWGz-N6mhaTSXi5d_o1sPPkQPrQ3gxPewZvabplfO6Ws6EQ6zPCI_00tlqhrxSaRCpxktgI1gK9O2921Spwn1D-NZxQjx3JvnFac3GoL37nHLCC96NHa9Ue_3oITbO5Jgl8H7EM6-R_dKN2Ob5jc3VQ6KA6cUc14H4rhCF2dEyJfcL_qSElPtsX5iRHmFFV0ix5XU1hS5PqtLMN9bGv-YZODm9dOdYtjsAM5OdSlSYZyOBn440ZWIZkVU6xAJpndoHy3UksUbdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ذخایر استراتژیک نفت ایالات متحده به ۲۸۵ میلیون بشکه کاهش یافته است، که کمترین میزان از نوامبر سال ۱۹۸۲ و تقریباً ۴۰ درصد از ظرفیت کل آن است.
🔴
این ذخایر در طول چهار سال گذشته، دو بار به میزان قابل توجهی کاهش یافته‌اند: حدود ۱۸۰ میلیون بشکه نفت در دوران ریاست‌جمهوری بایدن، پس از حمله روسیه به اوکراین، آزاد شد، در حالی که ۱۷۲ میلیون بشکه دیگر در دوران ریاست‌جمهوری ترامپ، پس از ایجاد اختلال در جریان نفت از طریق تنگه هرمز به دلیل جنگ با ایران، مجوز برداشت گرفتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/147442" target="_blank">📅 20:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147441">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLedfrLm7OTxaXIbWmV_cu9PbvpuD1zqDAq_TaWj1rTLPoV38obpm1dGSd3rlrJlRtNuWiwOvSC7fvNvLfJK0Vocpax0U6cQ2eKAj8xnO_NeKqveEP1j4NdE9C7Wgqyx_dDXdrP0SSarGUTTHQ35Y67mNE8FT2yYJsr70D2IgfKShZkCHy1FEjG4DCUfIdYGGON31795uE3YwIV7sJXNIiy0awrvzkHxbFjW_JEcf68TgqXvRrzhYJkGIzj4jLvatZj-zDzctEk7TA8F9RymMX3FlOskLSgGfr3mgRFxUneDb3YsaIDdp_m0KNgl66A2kDCWEaJm0QXPLZS8-WFD7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی الزیدی، نخست‌وزیر عراق، گفت که عراق به «پایگاه پرتاب حملات» علیه همسایگانش تبدیل نخواهد شد و می‌تواند به «کاهش تنش‌ها و گشودن راه‌های گفت‌وگو» کمک کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/147441" target="_blank">📅 20:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147440">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
منبع پاکستانی: آمریکا به‌دنبال توافق مرحله‌ای با ایران است
🔴
یک منبع پاکستانی آگاه از روند رایزنی‌های دیپلماتیک برای پایان جنگ آمریکا و ایران، از احتمال حرکت واشنگتن به سمت توافقی «مرحله‌ای» با تهران خبر داد.
🔴
این منبع در گفت‌وگو با «ارم‌نیوز» گفت اظهارات اخیر دونالد ترامپ درباره احتمال پایان جنگ پیش یا پس از انتخابات میان‌دوره‌ای آمریکا، لزوما به معنای نزدیک بودن یک توافق جامع با ایران نیست، بلکه نشان‌دهنده محاسبات سیاسی و نظامی واشنگتن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/147440" target="_blank">📅 20:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147439">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 250 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/147439" target="_blank">📅 20:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147438">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTK1A0FDP8NGK6OJuVywV4ehO2Xy-9NF5u3YR3rsnVg6hxoA0mXD-ZOQtDPNZIWOpfNfVxALyArJgx_iC2Kz7L_SaitN5wEB44jNGd-AYFD3uNpC5SUfm6T-vsxZXGbFiErIGD9MacjebGC1KiC3JRTmb3tR0XzJIoYgi-xOrAwofiWb7nEwSEAPmlZG8mZ2qW3ssgZ3adDUebUn0T7lRpkmliaAMKAiArlWryAeepy1WRSAcVgvTott2voH3hPgAM5L7upX-WUV9t6W2npPbszrJViArJ7-zttmogTQdyOvdAv4fNUX4_dtKlWN578FoQ5B_yEB3CBPitcUr8mSuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان سعودی در تلاش است تا حجم صادرات نفت خود را از طریق تنگه هرمز افزایش دهد. این اقدام پس از آن صورت می‌گیرد که حملات پهپادی باعث توقف فعالیت خط لوله مهم شرق-غرب این کشور شد. این خط لوله، مسیر اصلی صادرات نفت خام این کشور در طول جنگ با ایران بود، به گزارش بلومبرگ.
🔴
این کشور پیش از این، در ۱۰ روز اول ماه سپتامبر، حجم صادرات خود از طریق تنگه هرمز را نسبت به ماه آگوست افزایش داده بود و اکنون به دنبال افزایش بیشتر این حجم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/147438" target="_blank">📅 20:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147437">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeC5UlauWAXGhsr6w8mOrI7aOCbtxoGjrgAenN14YaoLryOF6i6cBHZgo80wnA-OGp321xjkuYTPg6j4090vC1Btqni1z8HPRfbUsYqEuQ3JTfxdn0fvT7lBQJcUw7yscbBIdatBs2sVHgKcgpq39hctYQ0vzFxLJ45HVLQlHJmOW1FYatprhEQRa08fXN2jRO3Y1jKFxhffFyFL44v9jJ29iyuTbVqlR7y34-QpTor5X7mheMWqGAPowXHzRRFqnCR_czhXJyA3V5QEpGX6a9jPBKycRQy5GthpAoWaBL7et2Fbdso_t2KQKDFlAen_1rzheCEs7Ol7FMF-Fcpo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : امیدوارم همه متوجه شوند که افزایش قیمت‌ها در سراسر آمریکا ناشی از جو بایدن و دولت او بود، نه از "ترامپ".
🔴
حتی قیمت نفت در دوران بایدن بالاتر از قیمت فعلی بود، و ما مانع از دستیابی ایران به سلاح هسته‌ای شدیم!
🔴
با استثنای موقت نفت، قیمت‌ها به شدت در حال کاهش هستند، و به محض پایان درگیری نظامی با ایران، قیمت نفت نیز به شدت کاهش خواهد یافت، و این اتفاق به زودی رخ خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/147437" target="_blank">📅 20:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147436">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUVCB1s2S7-ySBoSsfK4dR6f19b7CWNAW05_z1kHXH4rvlYgsqdHG7TvKAXbmPfyais6PNk4ext4R-FGqfb8zU05I75NFoLxyfXPcU4BHPFKiVEDtEKtf057ULcWzjiZwpq6ayBvPgcfh3upHG3pEIXlAPWsHSbQX7Z9X_KXM2jXY2r22BkmCjbQfnH7IrKaU0fGgcfeqponipl2uk3aOAz2q-WutT5mxeaPtup61dJzibMMHEA9KP924lXVCCwEgqWXNGQY1gGPX2qN8SQhpnpIxzZ29Mf19sD1QowWd829OIkpZdRwFWTg7z1s8lvxaVtnysyXVARlkliJyRjAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کشورهای جهان باید هزینه اقدامات آمریکا در تنگه هرمز را بازپرداخت کنند
🔴
دونالد ترامپ گفت: «نفت از تنگه هرمز در حال عبور است. کشورهای جهان که هیچ کمکی به ما نکرده‌اند، باید و در نهایت هزینه‌های ایالات متحده آمریکا را پس از پایان این درگیری بازپرداخت کنند.»
🔴
او افزود: «ما این کار را بسیار بیشتر برای دیگران انجام می‌دهیم تا برای خودمان؛ کاری که نسل‌هاست انجام داده‌ایم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147436" target="_blank">📅 20:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147435">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ: بیشتر از هر زمان در تاریخ سلاح تولید می‌کنیم و این سلاح‌ها به طور روزانه به نیروهای ما در خاورمیانه تحویل داده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/147435" target="_blank">📅 20:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147434">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKzVE5vTpuVpFqlCe_xVemc2pmDIP8FCrFAZZBlkSM4kgV2mBzHjpk2-g1E_g4yhmPmI2DbycAhCs5imPYOvrp_h2xfmZhZRW_57bj8pHKXE3seDT1PpilLAugTwvKWe_zpXGMDaWbheIIqf6ncGa5djyOvFOSHdZ50m5GoOY7394zLqxB5Lb6rAgd4BDqsaxu2IUPY5Nqjz78GHj4MYXIxfD_gpcf2Aa3bx69GdCShmRruq86AGY1V2l2PIkKDKrC7EelYRvzpQO1bSmogCiXvyQsHQEqaraSNjXCMZdDxyPjLXAXzhHPAKQkGpklzSfeS7Wv-2qfm4vuSc5H3zrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : من به تازگی گزارشی دریافت کرده‌ام که نشان می‌دهد ایالات متحده در حال تولید سلاح‌های فوق‌العاده و پیشرفته‌تری است تا هر زمان دیگری در طول تاریخ خود.
🔴
این سلاح‌ها به طور روزانه به نیروهای ما در خاورمیانه و سایر مناطق تحویل داده می‌شوند. کارخانه‌های شرکت‌های دفاعی ما به صورت شبانه‌روزی در حال فعالیت هستند، در حالی که به طور متوسط، 4 تا 5 کارخانه کاملاً جدید و بزرگ در حال ساخت هستند.
🔴
تمرکز اصلی این تولید، سامانه‌های پاتریوت، سیستم‌های THAAD، موشک‌های تاماهاوک و سایر سامانه‌های موشکی استاندارد است، که ما از قبل تعداد زیادی از آن‌ها را در انبار داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/147434" target="_blank">📅 19:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147433">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
رویترز: داده‌های اولیه رهگیری حرکت کشتی‌ها نشان می‌دهد شمار کشتی‌های باری عبوری از تنگه هرمز در تعطیلات آخر هفته به رقمی تک‌رقمی در روز کاهش یافته است؛ رقمی که به‌مراتب کمتر از میانگین ۱۴ کشتی در روز طی ۱۰ روز گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/147433" target="_blank">📅 19:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147432">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
نتانیاهو: ماموریتی پیش رو داریم و آن را به زودی انجام خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/147432" target="_blank">📅 19:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147431">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
دلار میریزه یا بالا میره
⁉️
🔴
تحلیل ترسناک هوش مصنوعی
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/147431" target="_blank">📅 19:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147430">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
عراق توافق‌نامه‌ای با فرانسه برای خرید سامانه‌های پدافند هوایی امضا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147430" target="_blank">📅 19:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147428">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCYAxBMuJldv8mGCJHnMpOn7FdE1RnhY3Fqh-zYJnjTfpuTgDJFA6D3EJs4cVOMj16wFdzw1CMck7yeVOu85HRdQm9k9ZTezptWdQQ3wBxzhmwwZvh0O2XPXuY6nX0h4ZJVAPEaM1kd43EG4ydnIyLMgKx5-lSk315ow9qDpE72U1ErWHKaxa_K1_-YJS75BU0Pyuf2-nnKleKd3aGnlIbe44XNd1GJMZyBxOVjPcjinzaR9SufDqVJ5BP7co3B07gI2oR9MWn6ceZPKX0p6RR78bxKZ4_K0mFzcmA6uuqBUQmYxWoBYhtAY6ErcEkeVhHEBIe1o5uOnMOzE6jUYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری رویترز گزارش می‌دهد که پالایشگاه‌های آسیایی خود را برای کاهش عرضه و افزایش قیمت نفت خام با گوگرد بالا آماده می‌کنند، چرا که منتظر شفاف‌سازی از سوی عربستان سعودی هستند. این اقدام پس از توقف خط لوله شرق-غرب، در پی حملات روز جمعه، انجام می‌شود.
🔴
قیمت نفت روز دوشنبه حدود 3 درصد افزایش یافت، در حالی که شرکت سعودی آرامکو هنوز اطلاعات به‌روز شده‌ای در مورد تخصیص‌ها و برنامه‌های حمل و نقل به مشتریان ارائه نکرده است.
🔴
برخی از پالایشگاه‌ها از احتمال تاخیر در بارگیری نفت از بندر یانبو در دریای سرخ مطلع شده‌اند، اگرچه تاریخ‌های جدیدی اعلام نشده است. سایرین نیز انتظار تأخیر را دارند، زیرا خریداران برای به دست آوردن مقادیر محدود نفت خام با گوگرد بالا از عراق، امارات متحده عربی و سایر مناطق رقابت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/147428" target="_blank">📅 19:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147427">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3tT7NzTPRycadHhOE3cPm3BUQQySumegp2V--zo_0VwNbSos_uBH5fHuxO6p-lvHeHNlub_Ueb332okuxilLC8AeudDgQ-h4q6CENIhPDwQUMOQroS5sVQd2RP5q-fD4JRXbdeNTPRhq1Ke-mjoAZudlis7_a_sYD97rUCBwN6vCNtkbNJJEu8pM9e50WefBITv-sfIeNvn6dNy3aSRIKpzAWlVkyhYmcqYLmqd5fOXjsdJ_-2f3rJhUZKdGLR1BLh8T6-Uir-T7zGYp9x4RIgnB1hf8euNyg1cit9026Qfxe6mwgqwbHBL6_Kf8uA58YKYdkhQCadQ6OskSXzXUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بورس مسکو در پی بیانیه ترامپ صعودی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/147427" target="_blank">📅 19:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147426">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a9fa4d5d.mp4?token=e0HF_boYLtz9bR4cFpG4asmsAhkbPofx8yUxeEeJl9qBXTIOBFv4C5x0qKGLdxq0kBU8CxcXNwWCbIqRFsRB8fRIw9wAEM6K07Xrz8Con2RT4OzTYUQ4FliwxnyLjPPyicr-MfGi4QdBtqf12VoFu_MghOPmuPaIjklYcQjKqxGF0762NwJaO2IXU1vfGcJ7-oIqmi88UhudHW7tIWig274li1dxGqLGFj-ZxMbhHu6uiOkOuFqsDtRwVwOMuH4B7dVpi3zcuorQCScDzFwMANLpS55TKH5FJrFsEFzq6iNBYWILF1F3FWeZztQ7D5ukn01GvF3I74m0j0PJZ9SB7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a9fa4d5d.mp4?token=e0HF_boYLtz9bR4cFpG4asmsAhkbPofx8yUxeEeJl9qBXTIOBFv4C5x0qKGLdxq0kBU8CxcXNwWCbIqRFsRB8fRIw9wAEM6K07Xrz8Con2RT4OzTYUQ4FliwxnyLjPPyicr-MfGi4QdBtqf12VoFu_MghOPmuPaIjklYcQjKqxGF0762NwJaO2IXU1vfGcJ7-oIqmi88UhudHW7tIWig274li1dxGqLGFj-ZxMbhHu6uiOkOuFqsDtRwVwOMuH4B7dVpi3zcuorQCScDzFwMANLpS55TKH5FJrFsEFzq6iNBYWILF1F3FWeZztQ7D5ukn01GvF3I74m0j0PJZ9SB7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرسش: آیا آرزوی تصدی پست نخست‌وزیر اسرائیل را دارید؟
🔴
بن‌گویر: من معتقدم، بله - به امید خدا که به آنجا برسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/147426" target="_blank">📅 19:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147425">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
بحرین: عبور از تنگه هرمز باید رایگان باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/147425" target="_blank">📅 19:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147424">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
حمله هوایی عربستان سعودی به المخا یمن
🔴
منابع خبری از حمله هوایی تجاوزکارانه سعودی به شهرستان المخا در یمن گزارش می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/147424" target="_blank">📅 19:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147423">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
رهبران اسکاتلند، ولز و ایرلند شمالی در کاردیف دیدار کرده و بیانیه‌ای مشترک را با هدف دستیابی به استقلال از پادشاهی متحد بریتانیا امضا کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/147423" target="_blank">📅 19:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147422">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
نتانیاهو: ما در حال مبارزه با تحریکات یهودی‌ستیزی جهانی هستیم، اما وقتی این تحریکات از درون خود ما سرچشمه می‌گیرد، غیرقابل‌تحمل است.
🔴
اکنون، دو کارگردان اسرائیلی، ارتش اسرائیل را به عنوان جنایتکاران جنگی معرفی می‌کنند و جوایزی را در جشنواره فیلم ونیز به دست می‌آورند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/147422" target="_blank">📅 19:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147421">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzpkhrvN-rnJiVMsVhUIRH6DQnvOoMs29pAkDiNYKRYNzk-sZs1Lmxk1V-PpfX5_D_BLmjALefR4iiiHN9yy7jvNiocmOH0wydt8WQ9_EwT6VNlK8rWvAbdL64mD0uIdRf9wHDQYPDpp0LndKVljY0IzAraALTnpoRLrYQm03cQHBzHa_sqxhG4tP7hC3qKqBhJT8RIL4-jER1YOD7wOg2wtr15IS9qLVEN0Rvnufhxz9gbl01MRiBQijeTow5inY0iYny4zEO4pERZ4sdmhTUdSdWoqP2yXHIvobACuFy01takKf5GFdmEXSnoIKG07MtknmwRA-crZ4GLEa1FMsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال:
«دولتِ در حال شکستِ [رژیم] ایران می‌خواهد خیلی سریع و به‌شدت به توافق برسد.
🔴
من تعیین خواهم کرد که آیا ایالات متحده آمریکا تصمیم می‌گیرد وارد مذاکره/تعامل شود یا نه — مفهومی که ما نسبت به آن گشوده هستیم.
از توجه شما به این موضوع سپاسگزارم!»
🔴
پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/147421" target="_blank">📅 19:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147420">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpLpq6BgWXBxiJhHI5liFBGKiUwKuXpChQuX4IXjBoX8m1AO8MzZy0i4kCjY54RYGPaAs2N_VdODWrb_TYHSkxLHDMzZGme5C4XKmLU-LPBNrq01bY0aswObslF09VaHFa8NkoHgOl36-yOXJ8UJaGTXHOUw0FFH5zctvHsxWyhm3lfE2fY0mceUjePAROdB_TNQbvzJ0eLM9mMUKN6OJpSecW0gCkq01paLGNjBKH_Pjw4MTlp0unhkEdlchz5dKLQ891_JNU4KN1zdamXYoFovjoEYfb_AzXfRw6Qw6w-_QFFnfxjtHnt6bbZpEbZkUfOm2HoBfzg4CXSHwlhTPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت وزیر خزانه داری آمریکا:
وزارت خزانه‌داری، عملیات "منزوی اقتصادی" را آغاز کرده است تا تمام منابع مالی را از رژیم ایران و کسانی که از آن حمایت می‌کنند، قطع کند.
🔴
به همین دلیل، من بار دیگر از افرادی که اطلاعاتی در مورد کسانی دارند که به فعالیت‌های تروریستی ایران کمک می‌کنند، خواستار افشاگری شدم.
🔴
به هر کسی در سراسر جهان که اطلاعاتی در مورد این منابع مالی دارد: این فرصت شماست. اگر اطلاعاتی دارید که برای وزارت خزانه‌داری مفید باشد، ممکن است واجد شرایط دریافت جایزه باشید، مهم نیست کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند.
🔴
اگر چیزی مشاهده می‌کنید، آن را گزارش دهید.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/147420" target="_blank">📅 19:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147419">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1HrFH-0uUHj-ugN_tChh0VotK-AwAvsslzS2a0aRdOYak9DFKUSA2cnNK5ki606-NlS1LDJftz2VrHtDBwPNKH-ZPFoOYNfPzvGpktnCvOdEXvi5-hFNNMS0gY3kmgz_MhjJ5CJXFHlevlKII7OfPggg93jgSxdDqHbvyokFpZRJNHCS8NdP-bw69SswEJ0NJAwS1VPz9md9j0kwNpy3ANKuBIcdkJtxR7scX6s5HAJRbcA0KrAvTGLikIH8jOOCA9ta_VuVk_q1PkCVWYrFIeZrXGcDdW2QhRGX5IZqQojJ-MIP5GvbEwdhphkuxM0XQ6GAxjKbqemPhR2q-nEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سریال خاطره انگیز قصه‌های مجید به دلیل اسم بی بی دیگر پخش نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147419" target="_blank">📅 18:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147418">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkO7gPeDpcSrK06h3uZlS3xu9TuUhaesxk0ca7jyZClLsnVakQOW4nARYMm4EvdY9rXl23lvVh0BRu7BvdV89NnQiT5pENgyyr6mTpFEodl7tZI5djFxs2N68-jXGubcVfFQjBlmzTw4-1NILtO6iw-HBRaH_dIwlkA8nQnBn_To74SCzObETDSFSIoNlyvZoMWunnbXjITJy9V90VtCBzHhSsKw590_SIaoZWfGdEKqzDPb_AHZjm-BM4P2DbShWwSHNwYrxFUNtAFTUpH6bKantCRMqFfQhxjirQ6Fe0Gh-OdtaI2j883dR0MQ9jYXno4CbW5dxTvZHMYhU3nVDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اوکراین و روسیه موافقت کردند حمله به زیرساخت‌های یکدیگر را متوقف کنند
🔴
افزایش قیمت گازوئیل بیشتر ناشی از جنگ روسیه و اوکراین است نه ایران.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/147418" target="_blank">📅 18:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147417">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
طبق گزارش ها عربستان سعودی برای اولین بار چندین موشک بالستیک ساخت چین را به سمت مواضع حوثی ها در یمن شلیک کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/147417" target="_blank">📅 18:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147416">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da4fb06f0a.mp4?token=K8XrVUPPrLqxqSFCbVlADE0HhArx-1Jr_YCBCwzFDOiRvvl9tM0rhxU1z6yKLGzlvMNNiR-qfrkZJ5LfVCFIDh2mAnekLBpqY50euX96mtGkw4B8cUxnWE3Idy20Tv-ftwcLgvytxphh02JhMuS5nvYuWgiep019eUGJi9xb0UuB5Off4j8R144s-LCPWn4GUOe8CF_LsiTphdMtkySaFYegrFtIT5OhGmMbRv8YpWTOdh5GPuYRfqa54kZyWQOCJlDQAhcZeTOphADTg5gGZ6OhriObQ6qS_syqU8MuU7jnogE271JvA_B3YJuHxaLnPDSnE4FsJutnhs0lMbe3fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da4fb06f0a.mp4?token=K8XrVUPPrLqxqSFCbVlADE0HhArx-1Jr_YCBCwzFDOiRvvl9tM0rhxU1z6yKLGzlvMNNiR-qfrkZJ5LfVCFIDh2mAnekLBpqY50euX96mtGkw4B8cUxnWE3Idy20Tv-ftwcLgvytxphh02JhMuS5nvYuWgiep019eUGJi9xb0UuB5Off4j8R144s-LCPWn4GUOe8CF_LsiTphdMtkySaFYegrFtIT5OhGmMbRv8YpWTOdh5GPuYRfqa54kZyWQOCJlDQAhcZeTOphADTg5gGZ6OhriObQ6qS_syqU8MuU7jnogE271JvA_B3YJuHxaLnPDSnE4FsJutnhs0lMbe3fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو خیابون شریعتی تهران، یه خانوم با یه پیرمرد سر رانندگی بحثشون میشه و زنگ میزنه به شوهرش که بیاد.
🔴
شوهره هم به این صورت میاد و با زانو حمله می‌کنه به پیرمرده و درجا میکشتش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/147416" target="_blank">📅 18:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147415">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">تلخ
‼️
تله‌کابین نمک‌آبرود نفری یک میلیون و صد
خانواده‌های ایرانی اغلب با دیدن قیمت
منصرف میشدن و میرفتن
تا چشم کار می‌کرد توریست عراقی بود
توی صف
ایرانی‌ها توی پارکینگ با کاردیاک
عراقی‌ها سلفی می‌گرفتن
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147415" target="_blank">📅 18:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147414">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b48e7d1d.mp4?token=lEv54ewNxwF3DwF3aSNt2FaHphLxypDCTHh__mouPQTp5o2S46ZiJxlEKJOuTSlCA6Uj68BZCOXGngC9NuYa4zJj00E5EomA9yIdy6X-k9T7_uhTlh7YlpI54ZJTApjEyxfJoI5-BQjZ2USxf72Q2eQhSX6nTFywkYWpw80GH-JCcSVkT9jMqwAxrPfdmIiuYqMsEZm4S4pDDIeC54IXhZf-WWVC5EhZts-cTwLp4jOE7-5jxPPpYhBRgJp2GY-lz46aXmhlSTXrpnCkzsoejqf6ZunYEOsMILYRMMBsvntvGbXnoh5PJa_KSd6rmuec93rAQggx7ZT1mHwTyYxroA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b48e7d1d.mp4?token=lEv54ewNxwF3DwF3aSNt2FaHphLxypDCTHh__mouPQTp5o2S46ZiJxlEKJOuTSlCA6Uj68BZCOXGngC9NuYa4zJj00E5EomA9yIdy6X-k9T7_uhTlh7YlpI54ZJTApjEyxfJoI5-BQjZ2USxf72Q2eQhSX6nTFywkYWpw80GH-JCcSVkT9jMqwAxrPfdmIiuYqMsEZm4S4pDDIeC54IXhZf-WWVC5EhZts-cTwLp4jOE7-5jxPPpYhBRgJp2GY-lz46aXmhlSTXrpnCkzsoejqf6ZunYEOsMILYRMMBsvntvGbXnoh5PJa_KSd6rmuec93rAQggx7ZT1mHwTyYxroA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرید، برادر زن سابق مجتبی خامنه‌ای : یه روز با مجتبی تو یه جمع فامیلی نشسته بودیم، یدفعه موبایل یکی زنگ خورد ، بهش گفتم این چه موسیقی هس گذاشتی ، بعدش دیدیم آقا مجتبی وارد بحث شد و گفت این موسیقی رو نمیشناسی؟ این موسیقی فیلمه کریستوفر نولان هس ، اونجا بود که همه پشماشون ریخت از حجم اطلاعات و سواد آقا مجتبی
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/147414" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147413">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e22382ecd.mp4?token=a7IIElZuImXVoZz2_1flVk9cpOdAwzuLig3O7hqGCOHaOZHugEk9OPQ4Oa-zCppw2sRGoZWdkxFrR7auyx6kA-SgM5jPzySZNNaHrGNxxKroAfRoP-8ZamFenYS3ikrw00TmL-A62uNYzqdrzPuNZaHbE5qMDb8unG_se-ehxtYv_lhhYdv_2kUTyciuyKH01236sT5jJUUAHBjhINXF6cZuhfJFd_6_fInG9UcoDLbDOgOGIwmtqhDNo0EG4RlgjtQ7Fhfg7kleiVeUF31C8JRMM-HYfLldVE87eTi--LEi78UgZxfsLSqVdA_D8OGW_zKPNuegO_1RBMbp06htsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e22382ecd.mp4?token=a7IIElZuImXVoZz2_1flVk9cpOdAwzuLig3O7hqGCOHaOZHugEk9OPQ4Oa-zCppw2sRGoZWdkxFrR7auyx6kA-SgM5jPzySZNNaHrGNxxKroAfRoP-8ZamFenYS3ikrw00TmL-A62uNYzqdrzPuNZaHbE5qMDb8unG_se-ehxtYv_lhhYdv_2kUTyciuyKH01236sT5jJUUAHBjhINXF6cZuhfJFd_6_fInG9UcoDLbDOgOGIwmtqhDNo0EG4RlgjtQ7Fhfg7kleiVeUF31C8JRMM-HYfLldVE87eTi--LEi78UgZxfsLSqVdA_D8OGW_zKPNuegO_1RBMbp06htsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک بیمار سرطانی: شب‌ها که پرچم تکون میدید اصلا حواستون هست که ما دارو نداریم و داریم میمیریم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/147413" target="_blank">📅 18:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147412">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7f9d91bae.mp4?token=TWaaytfJ5sTyJa5SnR6gp7O2v0tFArTLw6xrT9PLk0iLjsZefDNqo_N5J9E2GjpWS8Vnd86Vgm-EclAxV3OT1aOCVut7WLvKw4tmd-waL8bXXn0fiGo0nRRRwaj4FxMSeH1zCONnIDT0UE_opz9GSYiRuuLHKawfJX-ngkicRrhfWhWxVmTAGSEDh3XDX-U-QLoxfQ6oYwMqkq2uo7gnQRAOTKsJPdss9eQLV5CKFqyoReNtRCCHIRtGcfCZcs7wOVwLY1EZoIYNHTxPmSSLGH0U4-PtCWjPkHrsWMqtfqloti7hEBE5AfFHFbdznkKOau6Nx-G9OKYFSOVBe2P24g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7f9d91bae.mp4?token=TWaaytfJ5sTyJa5SnR6gp7O2v0tFArTLw6xrT9PLk0iLjsZefDNqo_N5J9E2GjpWS8Vnd86Vgm-EclAxV3OT1aOCVut7WLvKw4tmd-waL8bXXn0fiGo0nRRRwaj4FxMSeH1zCONnIDT0UE_opz9GSYiRuuLHKawfJX-ngkicRrhfWhWxVmTAGSEDh3XDX-U-QLoxfQ6oYwMqkq2uo7gnQRAOTKsJPdss9eQLV5CKFqyoReNtRCCHIRtGcfCZcs7wOVwLY1EZoIYNHTxPmSSLGH0U4-PtCWjPkHrsWMqtfqloti7hEBE5AfFHFbdznkKOau6Nx-G9OKYFSOVBe2P24g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
باجناق برای سرقت طلاهای خواهرزنش، دو سارق اجیر کرد!
🔴
در تهران، مردی که از وجود طلاهای خواهرزنش خبر داشت، برای سرقت از خانه او دو سارق اجیر کرد.
🔴
سارقان پس از ورود به خانه، دست‌وپای فرزندان خواهرزن را بستند و طلاها را برداشتند؛ اما در همان لحظه، صاحبخانه به خانه رسید و سارقان گرفتار شدند.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/147412" target="_blank">📅 17:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147411">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
زکریایی، کارشناس حکومتی: حکومت امیرالمومنین هم فاسد بود پس انقدر به ما گیر ندید
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/147411" target="_blank">📅 17:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147410">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
انفجار در تنگه هرمز بر اثر شلیک موشک
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/147410" target="_blank">📅 17:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147409">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b278137e.mp4?token=QVVfvbiooAgKN49X57VzDFrGpduugqsGTgdL-BP9l5PWBHtvLucQpeArz74fDpvCK4ODrRcCwMcDorMTOMr3DZZobXWana3nM3WCetaG-IvBEisFVMQiqIY5dsIXCuh1BlvvKs8JxtdExuDbjWCBLHpdqjAs0HMZ2U4eFd0JU4x-7xYAnIjEMtCgbpvJa-qSAZKTSmOSRbxhObTFuUTsbKYR_jeUd9_qEcKvW0Vx8OhgVtZ-SN4LrRI2EEjDBqAR9WIo-VhFvmxN8grjTQzjSnBF6c9J42LR8ZjXckJy7UgvV_dzSetrokI7znPJMHZAt35wOlCde7doGZM2UG6XzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b278137e.mp4?token=QVVfvbiooAgKN49X57VzDFrGpduugqsGTgdL-BP9l5PWBHtvLucQpeArz74fDpvCK4ODrRcCwMcDorMTOMr3DZZobXWana3nM3WCetaG-IvBEisFVMQiqIY5dsIXCuh1BlvvKs8JxtdExuDbjWCBLHpdqjAs0HMZ2U4eFd0JU4x-7xYAnIjEMtCgbpvJa-qSAZKTSmOSRbxhObTFuUTsbKYR_jeUd9_qEcKvW0Vx8OhgVtZ-SN4LrRI2EEjDBqAR9WIo-VhFvmxN8grjTQzjSnBF6c9J42LR8ZjXckJy7UgvV_dzSetrokI7znPJMHZAt35wOlCde7doGZM2UG6XzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سردار کرمی:
نیروهای دلتا فورس پس از هلی‌برن در اصفهان از ما ترسیدن و فرار کردن
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/147409" target="_blank">📅 17:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147408">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9132eb650.mp4?token=njaxi3r5SDn0v_R-acwZsSTI4EJPq1yKIhWTWBFxPps3i_cq9RTHrL6MFiS8nNDUHuXpnWbb7rXE9CH7BPGFLhqWTvVG3KWPos0OxemPM1f2VMf1zkF1eaIDpKtRfyZTsm-dKA8kpq2dW1XlkzjfcGuLATovaW4uYbdJvJRwmNyoZ6cwxE3Kr3yFcLofwSLvhc-jlFyvDlKHHgMq6jhsNyP3VtoW-zeFiCIxRtsj3PrOsIvwjlxdb1rZeKTE48FQ6jaAGIO-3QzHs7ZXb_CdL7Qhnwt853pMf47QFcMNfgRLRpzr5cAMJrp1TaRxDK0tNi01e0mkG8VllSRFHw_seg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9132eb650.mp4?token=njaxi3r5SDn0v_R-acwZsSTI4EJPq1yKIhWTWBFxPps3i_cq9RTHrL6MFiS8nNDUHuXpnWbb7rXE9CH7BPGFLhqWTvVG3KWPos0OxemPM1f2VMf1zkF1eaIDpKtRfyZTsm-dKA8kpq2dW1XlkzjfcGuLATovaW4uYbdJvJRwmNyoZ6cwxE3Kr3yFcLofwSLvhc-jlFyvDlKHHgMq6jhsNyP3VtoW-zeFiCIxRtsj3PrOsIvwjlxdb1rZeKTE48FQ6jaAGIO-3QzHs7ZXb_CdL7Qhnwt853pMf47QFcMNfgRLRpzr5cAMJrp1TaRxDK0tNi01e0mkG8VllSRFHw_seg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پروازهای مکرر و گسترده هواپیماهای جنگی سعودی بر فراز شهر طائف.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/147408" target="_blank">📅 17:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147407">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🤫
اگه توام دنبال کد تخفیف
🆓
📌
دیجی کالا و اسنپ و ..... هستی بیا
👇
🛍
https://t.me/off_khooneh
🛍
https://t.me/off_khooneh</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/147407" target="_blank">📅 17:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147406">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
خبرگزاری معتبر فارس: لاریجانی زندس
😂
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/147406" target="_blank">📅 17:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147405">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckWfRYSLHmPmDtLa4JYI-Su06MU5HoHTMJoQIEHHcHLpmWJ_lLnVdjCogP4dps1gD4_leSyh9Ufb1PD8iQc5-CcKmnLyFYhM7SRDTwJQjgQitizAL0nP8eHbz0oH-HVgEzip9bkk9kdpCzYWVeyFupkm6EYOrhwzyMQOjsKgXQAOBG2Cyf8UZYkTUcrtXHeaDN_wmyXeGewZKmsSJCv5Y3Mx7Vr-N3cBI-r_bV0W2P6yyxo2fGphi0431ldY9tkCCMaTse0xgMIVM881FB-xg6BHwSr8wtf6HE-MKesGSsQgW_8QDvGUde85Cz7zHj7-VmoYQbunwHVdi-YGcKgZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری معتبر فارس:
روایت آمریکا جعلی است و هیچ خلبانی نجات پیدا نکرده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/147405" target="_blank">📅 17:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147404">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55f910667.mp4?token=QcxqvzlospsY6Wvvi_chHUOPv6SV5MQ3nGTcViuD4SK23gQxUJq6doETLRNk1KUBN2bD01YALvhGzIN2U5HsxSMuNtT_x34oCIb4rWCMkc-h52rUaePdko9iQJlCqWyK-uoj2kupzp3_GFbN5vieWlQwp8z2qD1DTlVSGu2SKhqRqQR55lBIhTVDJPERI_GBglTUGSIl9wEhYmW1Psx7nRDjXs5NVdG1lVVLuFxK0HJ2lYfCEvl6es6yFuk4iYcaL_aovW6w8bxI81_eSso-iHtXLI1DKdmZ9KofbaT4o5rE4RQBAIQjdgTkasYBNpUETUsIFylN_K09P-kt7GHyQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55f910667.mp4?token=QcxqvzlospsY6Wvvi_chHUOPv6SV5MQ3nGTcViuD4SK23gQxUJq6doETLRNk1KUBN2bD01YALvhGzIN2U5HsxSMuNtT_x34oCIb4rWCMkc-h52rUaePdko9iQJlCqWyK-uoj2kupzp3_GFbN5vieWlQwp8z2qD1DTlVSGu2SKhqRqQR55lBIhTVDJPERI_GBglTUGSIl9wEhYmW1Psx7nRDjXs5NVdG1lVVLuFxK0HJ2lYfCEvl6es6yFuk4iYcaL_aovW6w8bxI81_eSso-iHtXLI1DKdmZ9KofbaT4o5rE4RQBAIQjdgTkasYBNpUETUsIFylN_K09P-kt7GHyQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسئولین طبق معمول دروغ گفتند
‼️
🔴
نیکزاد، معاون مجلس،مدتی قبل: آمریکایی‌ها برای خلبان نیومده بودن،اومده بودن اورانیوم ببرن که بازم شکستشون دادیم
🔴
اما دیشب ایالات متحده فیلم نجات خلبان رو منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/147404" target="_blank">📅 17:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147403">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری / لحظاتی پیش دفتر نتانیاهو اعلام کرد:
نتانیاهو هفته آینده به آمریکا سفر خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/147403" target="_blank">📅 16:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147402">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a2436eef8.mp4?token=JvaBMaKa0NgMh8gdnWrx-u9K9BlO9ykxWVSaNWVPPP2CWLIK4JolRjfxSP7FbV2zKN8gLh5eLiTpi20ikQ5HBx1obe8K-mojqNDoVfnQv8H_J12NvYhtBxLm9nAhk-721cgpazDG65bWIxW3qeX3d-8Cl0XMPdL_Sji56hWkhkmyh7a-I8mLD5ghq4UenbyroHDMQkOcPMgSzUC29PF7xaQvC9fLjL1I38tOD3fwN3GPCN45wr1fMkucXc-Tmlq97F7uWh2XYJ0kpqQ7Flz1Z2LiqYUHtp5TeSBZ5oInEdvjQDt4r1UfOYyJmnPUNXgfR1aoLLa406ubH2OtCSR7N4b7avcmciVC5bxiHhqUk56rpvGLdls1Q6cSDTnCaXt7DtBDtEbb7bHwR6JIR45G2cqvH7DxRO6GN_ZEcMtJKdZdy0r1955OIqm0ZGElMi2MvkZ0EB6OTdL3HqUcJsKlsdhOxxnoLTGDrK0HUCMcUZ8g6Q2o5UqNEWe2FDk2sMLrXOA-LeyRkykR5Vk0Ie2Ln3M-OLaKUyaJZpAUTeLJZ3jaA27MAeeyWSDOJSrE6k7lUAKgz6XP-uzTa2Agl3EJcrvSVw1cUQTYteFmFD5APPwcchmzewLBF4_y5fakuV7NSnNsxEngBDd6unGTZCjZUi_woKshngrvpbb9WFnkUVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a2436eef8.mp4?token=JvaBMaKa0NgMh8gdnWrx-u9K9BlO9ykxWVSaNWVPPP2CWLIK4JolRjfxSP7FbV2zKN8gLh5eLiTpi20ikQ5HBx1obe8K-mojqNDoVfnQv8H_J12NvYhtBxLm9nAhk-721cgpazDG65bWIxW3qeX3d-8Cl0XMPdL_Sji56hWkhkmyh7a-I8mLD5ghq4UenbyroHDMQkOcPMgSzUC29PF7xaQvC9fLjL1I38tOD3fwN3GPCN45wr1fMkucXc-Tmlq97F7uWh2XYJ0kpqQ7Flz1Z2LiqYUHtp5TeSBZ5oInEdvjQDt4r1UfOYyJmnPUNXgfR1aoLLa406ubH2OtCSR7N4b7avcmciVC5bxiHhqUk56rpvGLdls1Q6cSDTnCaXt7DtBDtEbb7bHwR6JIR45G2cqvH7DxRO6GN_ZEcMtJKdZdy0r1955OIqm0ZGElMi2MvkZ0EB6OTdL3HqUcJsKlsdhOxxnoLTGDrK0HUCMcUZ8g6Q2o5UqNEWe2FDk2sMLrXOA-LeyRkykR5Vk0Ie2Ln3M-OLaKUyaJZpAUTeLJZ3jaA27MAeeyWSDOJSrE6k7lUAKgz6XP-uzTa2Agl3EJcrvSVw1cUQTYteFmFD5APPwcchmzewLBF4_y5fakuV7NSnNsxEngBDd6unGTZCjZUi_woKshngrvpbb9WFnkUVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریس رایت، وزیر انرژی آمریکا: هیچ برنامه‌ای برای غنی‌سازی اورانیوم در عربستان سعودی وجود ندارد.
🔴
او گفت توافق همکاری میان آمریکا و عربستان بر ایجاد صنعت تجاری انرژی هسته‌ای در عربستان متمرکز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/147402" target="_blank">📅 16:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147401">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=BNQNII2OacvRiMO-uBX0LeocXZbVmugasjdnzlP7OgZfgevISmMX9dGn68V_rwguAIhBD9XsNz8x6WhqOziCJWf221u0R7QwPUOWaPcvO9nSv8tsj0yl7VZWGf3FtOwJc-kzF35RwEp4oGUOaxn5_j7iCzlZDWymYSS_J8zNk3LiZhsTR24AvEdrNHeY12IRo1ru2I_oT1ntF1g-HD1P0ygpU4KRvdkVuTMrhKpNOuPEOL-YJ2dR62n6EZ8RiEZ79PR2wBQxNmxWwXpc2XiQGnXy-Wh4zdVaMboRJI79ndW12_2BgXJimyYjiZA6ZQIeRhG7xzV_5Acco7uBl9VtqyDAg1_Srxj_xEPcyHdMZFpVOg0zY3UzKidEujy6jQXW7acYcTZq8ALusivw9w1Sg1s_REFDoU_PIqPEB1IC8_OLqDCtpT6VdYO-nKlzmfBscvQPTGwWiwZZxT0hwdx1uYr4WjKCu7zZ7lMAvCgqEOy1J7CKI6ZJRQZzsPoQ3l7_Ip-m214_5qeKUbR3-OoJr-5gzHjHXBXvq1wbCGHsd8U5UWZ30o2PeNIA3MPxdAdhnTicHNi101XbPqLJmR0VoEjOsdJbY5ZHyDNS-umHaDEQCs4CMfZZx1rs9SOmuGpQdRBCGxHRUPdkY93PrA7Vtw-w-Q-f9gcG4Ld03VBqSLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=BNQNII2OacvRiMO-uBX0LeocXZbVmugasjdnzlP7OgZfgevISmMX9dGn68V_rwguAIhBD9XsNz8x6WhqOziCJWf221u0R7QwPUOWaPcvO9nSv8tsj0yl7VZWGf3FtOwJc-kzF35RwEp4oGUOaxn5_j7iCzlZDWymYSS_J8zNk3LiZhsTR24AvEdrNHeY12IRo1ru2I_oT1ntF1g-HD1P0ygpU4KRvdkVuTMrhKpNOuPEOL-YJ2dR62n6EZ8RiEZ79PR2wBQxNmxWwXpc2XiQGnXy-Wh4zdVaMboRJI79ndW12_2BgXJimyYjiZA6ZQIeRhG7xzV_5Acco7uBl9VtqyDAg1_Srxj_xEPcyHdMZFpVOg0zY3UzKidEujy6jQXW7acYcTZq8ALusivw9w1Sg1s_REFDoU_PIqPEB1IC8_OLqDCtpT6VdYO-nKlzmfBscvQPTGwWiwZZxT0hwdx1uYr4WjKCu7zZ7lMAvCgqEOy1J7CKI6ZJRQZzsPoQ3l7_Ip-m214_5qeKUbR3-OoJr-5gzHjHXBXvq1wbCGHsd8U5UWZ30o2PeNIA3MPxdAdhnTicHNi101XbPqLJmR0VoEjOsdJbY5ZHyDNS-umHaDEQCs4CMfZZx1rs9SOmuGpQdRBCGxHRUPdkY93PrA7Vtw-w-Q-f9gcG4Ld03VBqSLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: ایران می‌گوید آمریکا در جلوگیری از حضور محمد اسلامی، رئیس سازمان انرژی اتمی ایران، در کنفرانس عمومی نقش داشته است.
🔴
کریس رایت، وزیر انرژی آمریکا: او یک فرد تحت تحریم است و ما نمی‌خواهیم افراد تحریم‌شده از تحریم‌ها فرار کنند. او درخواست معافیت از تحریم‌ها را مطرح کرد، اما این درخواست رد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/147401" target="_blank">📅 16:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147400">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a38918bdab.mp4?token=AkEBjw4-oiUzXEicmkYvi9ko_sXLc9cS8zBNb6uKcBvKbH3bW6IDvuSH_awIzsAinfKf5c8SSVpRBm7wy4S7WxppU5I14g89Bt8oU50jI48lHQZefQoXMh9CN5d43DNtZ9SqPb2ZoXfM8wraveShWIIKKDBHqCKxU5BV7sruQndY57oXjJJ2vvwgYbJHojbgIjrltFWFcVes2yxMDwyDKrDSbszOBD1_3JGmVP9LsVZWwayv7qfJjer7cRIJZQTkHh2Wmad4JOKaweoQrON48QT9lXng0RIqD_XsjDHdLKq2WGFuVptvVTJ0LxVvvyodAeiGAOCB-d-Jfv97_7Z8wEsBsrrxy4bcbwEtPJVq6E-3H9OxwdZ2VC6MuG0xkhBV-yYrTm8NiRhlrzKnrYojQET7aDj2VUr7T7IZHSWMngcARl1ZDL26WN0RpbSRi0YYZNJEe5uPpy_E-QJjrYhr-cFY-1PEHDivUA8AjIR5Bw5eo4t1mLh8OqaHxhFaiWHv2IUhP5JwIhwYU5eDA9z4pJ6JGAlaOlqhL48UgJtGPdH48f3sG3C_yNFVr-VYDgGqV1XhMHBS7ODYESVgy8yiDQDrTV6iO6jmB_rf8__ZAtNeGANR6IXnOGuUrUbjP4HOyvLShJbVqLPQGnAWqVoTtl68OaXSBXX472Eofkq42us" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a38918bdab.mp4?token=AkEBjw4-oiUzXEicmkYvi9ko_sXLc9cS8zBNb6uKcBvKbH3bW6IDvuSH_awIzsAinfKf5c8SSVpRBm7wy4S7WxppU5I14g89Bt8oU50jI48lHQZefQoXMh9CN5d43DNtZ9SqPb2ZoXfM8wraveShWIIKKDBHqCKxU5BV7sruQndY57oXjJJ2vvwgYbJHojbgIjrltFWFcVes2yxMDwyDKrDSbszOBD1_3JGmVP9LsVZWwayv7qfJjer7cRIJZQTkHh2Wmad4JOKaweoQrON48QT9lXng0RIqD_XsjDHdLKq2WGFuVptvVTJ0LxVvvyodAeiGAOCB-d-Jfv97_7Z8wEsBsrrxy4bcbwEtPJVq6E-3H9OxwdZ2VC6MuG0xkhBV-yYrTm8NiRhlrzKnrYojQET7aDj2VUr7T7IZHSWMngcARl1ZDL26WN0RpbSRi0YYZNJEe5uPpy_E-QJjrYhr-cFY-1PEHDivUA8AjIR5Bw5eo4t1mLh8OqaHxhFaiWHv2IUhP5JwIhwYU5eDA9z4pJ6JGAlaOlqhL48UgJtGPdH48f3sG3C_yNFVr-VYDgGqV1XhMHBS7ODYESVgy8yiDQDrTV6iO6jmB_rf8__ZAtNeGANR6IXnOGuUrUbjP4HOyvLShJbVqLPQGnAWqVoTtl68OaXSBXX472Eofkq42us" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوالات عجیب خوش چشم در آنتن زنده بعد از ممنوع التصویری: بلبل دارین اینجا؟ مگه باغه؟ صدای بلبل میاد!
🔴
چرا روکش صندلی نو رو نکندین؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/147400" target="_blank">📅 16:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147399">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxnuPCob0dhzuCa4Pdnbl34LPl03y78uOdhpBMTJ56wYB8vgHPp_BWpqpM_GmOid1-aUDdpaWa2ZjIUH9_zxur9gY4xIJt_RtyLLiyXDWqhN7ac2-0YK-Yf0_mtkhdZHhloOk3HZqpJFkqrPNyMszquR0NPXrNV166OLa-1L9-QazMmxNa3J7sxBQ3_FswVxGJarLO3RQxin0eTkj-_zUX9p2hntHyP0LY-xWRnmiiGzjbrqPR_jDVcbNXnS18HWKXJ-srwOSfQJjcN77m90oWXtUN5gfiUuVZYyo8jiGg3laTIG80BKjgoh4pMlPo_QjdwqmF8QraCM0GReSrPXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو تهران (ونک) یه غذاخوری افتتاح شده به اسم کتلت بی بی که فقط تخصصش  کتلت درست کردنه
🔴
حالا قراره به دلایل نامعلوم پلمپ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/147399" target="_blank">📅 16:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147398">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22435ecca9.mp4?token=hKLnKMSBT7VYgFQ2j0L8waRWJKYD4NCHBJR6mb9rLGEO7HcCcGh3btpY-4xZn9O-VHJzAuuWgx0IRRKJeTHqeJWeCN-ODb2Cao6yyejy1VyqGaOT-KEBl4MOVJvDW3YaRXCw0p00J0op3dOAKVqhMYhwcLJKhfFDdoBCQNYULIdyS3gEVtSmaLLsZuaeZy8tBnql2zKKe7G5Mqaw38OnjH-dS1uWPCeXcs9YxOCTt1I-xd5fF2j0OEAc7YglGHmYDcuVERBruD3kVeJoVCHSzYEcu8aPofa8s2rQ6q6b0XH3rAwcOxFNm9eb4-0Qd_nSx9H7Mxw0cTWmh160Tlerfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22435ecca9.mp4?token=hKLnKMSBT7VYgFQ2j0L8waRWJKYD4NCHBJR6mb9rLGEO7HcCcGh3btpY-4xZn9O-VHJzAuuWgx0IRRKJeTHqeJWeCN-ODb2Cao6yyejy1VyqGaOT-KEBl4MOVJvDW3YaRXCw0p00J0op3dOAKVqhMYhwcLJKhfFDdoBCQNYULIdyS3gEVtSmaLLsZuaeZy8tBnql2zKKe7G5Mqaw38OnjH-dS1uWPCeXcs9YxOCTt1I-xd5fF2j0OEAc7YglGHmYDcuVERBruD3kVeJoVCHSzYEcu8aPofa8s2rQ6q6b0XH3rAwcOxFNm9eb4-0Qd_nSx9H7Mxw0cTWmh160Tlerfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بالگردهای آپاچی عربستان سعودی مواضع و تجمع نیروهای حوثی‌ها را در نزدیکی باب‌المندب هدف قرار دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/147398" target="_blank">📅 16:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147397">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ماهواره چینی که در فضا به ایران داده ارسال میکرد، به دلایل نامعلوم(آمریکا) منفجر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/147397" target="_blank">📅 16:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147396">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=lZ3YHhAYr193k1fQ5UM2y4GNQmJ2PmmGIGRaat-PKGzdvPMv0gzdb3eUhClbXFY0SOfu7_5_ZLg11gVvs9c3NRJzryq9-vlFqd0yGcsLODaWAkz_DsGTtgMglLoUf-wLd9rvMy7qa-sum0eeRDgf7XSxTrgTrtUKC4UHCWlPga7ehPQUzQK4MBxioEU00ocMfTpIumg28zA2kwizH7tTd7yKhdIQ-Q7gHRHldypHf5DkFEt5D4oy3KT4thnBzQaMkge3jgxdEfFUfMdoSwbMApmuqDB0GV8zi1GEPvlIdWMqPwln3fc3zKCm6l4RCgvIAuPVCm_frTKrNLrYT9bdSWqcQQr9XIgswo78hUf_HtO4ZOq9HUiKoTMbS-NLk7Y0NEr0LSCNAU_qTX_CAG_ZNG_LiBfY0vpbSjzSDgjHPFWFzCBKYHDhhPCPvWyvzZlDZAhdvzFfAGNvdgvYDW7rgxwV9d51MhWcpTyZ5yVrOFLfNs-ysRiGA3sjH0WVXoEGz8kW03gKwWKHENLoyCGun4uGFisUHZUG9aVhYe8qdxRXh1Dwg2yQ3jwWNXCk2rtHZ5ufsDyB0secuWVGHTcEBa70Isrp2Bl1a3P8Z9HsswlVPRIxTAueAaBNfjxYadGSSayHbQ_EoDJuXN30lgmAyWFXiQicK7mo7keizgff5vM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c79848ffa6.mp4?token=lZ3YHhAYr193k1fQ5UM2y4GNQmJ2PmmGIGRaat-PKGzdvPMv0gzdb3eUhClbXFY0SOfu7_5_ZLg11gVvs9c3NRJzryq9-vlFqd0yGcsLODaWAkz_DsGTtgMglLoUf-wLd9rvMy7qa-sum0eeRDgf7XSxTrgTrtUKC4UHCWlPga7ehPQUzQK4MBxioEU00ocMfTpIumg28zA2kwizH7tTd7yKhdIQ-Q7gHRHldypHf5DkFEt5D4oy3KT4thnBzQaMkge3jgxdEfFUfMdoSwbMApmuqDB0GV8zi1GEPvlIdWMqPwln3fc3zKCm6l4RCgvIAuPVCm_frTKrNLrYT9bdSWqcQQr9XIgswo78hUf_HtO4ZOq9HUiKoTMbS-NLk7Y0NEr0LSCNAU_qTX_CAG_ZNG_LiBfY0vpbSjzSDgjHPFWFzCBKYHDhhPCPvWyvzZlDZAhdvzFfAGNvdgvYDW7rgxwV9d51MhWcpTyZ5yVrOFLfNs-ysRiGA3sjH0WVXoEGz8kW03gKwWKHENLoyCGun4uGFisUHZUG9aVhYe8qdxRXh1Dwg2yQ3jwWNXCk2rtHZ5ufsDyB0secuWVGHTcEBa70Isrp2Bl1a3P8Z9HsswlVPRIxTAueAaBNfjxYadGSSayHbQ_EoDJuXN30lgmAyWFXiQicK7mo7keizgff5vM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ایران اعلام کرده که ایالات متحده در جلوگیری از حضور آقای اسلامی، رئیس سازمان انرژی اتمی، در کنفرانس عمومی دخالت داشته است.
🔴
دبیر ویراایت: ایشان فردی هستند که تحت تحریم قرار دارند، و ما نمی‌خواهیم افرادی که تحت تحریم هستند، از این تحریم‌ها فرار کنند. ایشان درخواست معافیت از تحریم‌ها را ارائه دادند، اما این درخواست رد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/147396" target="_blank">📅 16:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147395">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce9a0183a.mp4?token=K1GAkqNp3mo_TfzeWQGbN_ELKOrrYhXUcGQObHjR5i88DLyD8evn5aVPy-njTFLCajMgwFFg6cXOsy18Y7_xB1PG5n-YaxXm-xe5ROhBrRVJgCC5IcHGB5ck21Hho5BKBR51QKaPRyD53kZI5rCb8z_kSy1ptF7pcGOd2VOOghYSzuYYVSOXDwSjl_1vcCEz3dupVXfYEYgWe9kH52elRrIaocgb26bhFGbc2ZMKpJwe0fJC_L_WHi31UNupl6oVnuep_8Vm6ZLTMfKJSbH0ofBbrL1RyrsQPnw6RvVnsc4ihk-vZaeWX1Nf4vsUPJv2ZE_JmZuqQgBMm15--22T04RgYhbtWRJlxbqgk6TNgyCMmiMSI-DYUtKAU8rAKQiYkRydCWLgEdU9KSf2BJlwH_kLkjcR8nw8u3XQ80BMqO-Q3RbrfnAYuJg_zb-C2k3JPdnSL_Uw73ObXB_wm3rc9ePXUmw1vl-8q5GE537y2H_Fji5iKSbgWv5-XvfDkV3do9LaNJ8RATU1V6_bKu1FgJS_kwC9lPb4kvswk0TG0NiJD8cliZbgmR6tmFBcEGPpTQPCX4gQhZGPBdyDiNROfYDnfVCdRrvUWynanl7iAcNKPhm3lKsKU05U3aAa80Z0q6dT9COrpURn6JuUtC2GfiF_E6wKJlXNIN3ck2pw_NM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce9a0183a.mp4?token=K1GAkqNp3mo_TfzeWQGbN_ELKOrrYhXUcGQObHjR5i88DLyD8evn5aVPy-njTFLCajMgwFFg6cXOsy18Y7_xB1PG5n-YaxXm-xe5ROhBrRVJgCC5IcHGB5ck21Hho5BKBR51QKaPRyD53kZI5rCb8z_kSy1ptF7pcGOd2VOOghYSzuYYVSOXDwSjl_1vcCEz3dupVXfYEYgWe9kH52elRrIaocgb26bhFGbc2ZMKpJwe0fJC_L_WHi31UNupl6oVnuep_8Vm6ZLTMfKJSbH0ofBbrL1RyrsQPnw6RvVnsc4ihk-vZaeWX1Nf4vsUPJv2ZE_JmZuqQgBMm15--22T04RgYhbtWRJlxbqgk6TNgyCMmiMSI-DYUtKAU8rAKQiYkRydCWLgEdU9KSf2BJlwH_kLkjcR8nw8u3XQ80BMqO-Q3RbrfnAYuJg_zb-C2k3JPdnSL_Uw73ObXB_wm3rc9ePXUmw1vl-8q5GE537y2H_Fji5iKSbgWv5-XvfDkV3do9LaNJ8RATU1V6_bKu1FgJS_kwC9lPb4kvswk0TG0NiJD8cliZbgmR6tmFBcEGPpTQPCX4gQhZGPBdyDiNROfYDnfVCdRrvUWynanl7iAcNKPhm3lKsKU05U3aAa80Z0q6dT9COrpURn6JuUtC2GfiF_E6wKJlXNIN3ck2pw_NM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر انرژی ایالات متحده، درباره ایران:
امروز، میزان متوسط نفت و فرآورده‌های نفتی که از طریق تنگه هرمز به دریا منتقل می‌شوند، تا 10 میلیون بشکه در روز است.
🔴
شما خواهید دید که این رقم در هفته‌های آینده افزایش خواهد یافت. و اگر جریان نفت از خطوط لوله فرعی را هم به آن اضافه کنیم، میزان انتقال انرژی از این منطقه به 13، 14 یا 15 میلیون بشکه در روز می‌رسد.
🔴
بنابراین، بخش قابل توجهی از میزان انتقال نفت قبل از درگیری، که هنوز به طور کامل به حالت قبل بازنگشته است، همچنان با پیشرفت بسیار خوبی ادامه دارد و ما به این روند ادامه خواهیم داد.
🔴
حالا نوبت ایران است که صلح را به این منطقه بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/147395" target="_blank">📅 16:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147394">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dfbb346a9.mp4?token=mMQjEuPlKsZFLONFWrgyHRGLQfePJ5bO6METLmbZl5mTk0tYowaD3gi2cMCZb9WcxoRJ_9XP4RI9wq5mUSY5gDbs0-7X3NimCXgxBYxuBI0k1-WIDkPYXp4iqE_ctqZ9kIYeOZBVavA-aOg8M36LmTATDadSZstNRBaflLoZJL0iOIAMUQXbJeyZQ8gtf38VJ6o4OnbCl0sE90QUpjUUXZRb-GVzq8FUdtLH1gT_VbWmAYh2OntVlIQb61i0zDN4DGrQLsEbEUmeIEbU-Te5QtAMZ0Vo8TQEWGtxStuvVgh_VOH-ziqOxE8GejMo5BozWP6cLVW7WS723zczQdIoAocse-mCBFpKJQFUEsjgY6_-75hnGITL6aePoenjsKV7gOoAMJJy3dH5EXwMGq82wwyoZ3S36uipC3P4xdAmKOFuH8UgC0OhlamWUDRzuVhZUzbCc47VfT14wTTUfMFiTxRGGLxUi717bDzJitjsje_1EUxP9KQGQhJADuPCK0sV-tj71HlMvsnbcpHL3RvjcKoy0vBfP_tkcr7snWCOJQAtzt43xl53VaFqc-53UuRKbnmNC195UafRlnY9wV6D2ofvhHnTfxD3ZG_bGhCRw-RfeH3fVZK1zluMUnJdN80Hp_5_wADjW27Ilae_2efKR8P1AqnzTufGIPCNqqvEBAE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dfbb346a9.mp4?token=mMQjEuPlKsZFLONFWrgyHRGLQfePJ5bO6METLmbZl5mTk0tYowaD3gi2cMCZb9WcxoRJ_9XP4RI9wq5mUSY5gDbs0-7X3NimCXgxBYxuBI0k1-WIDkPYXp4iqE_ctqZ9kIYeOZBVavA-aOg8M36LmTATDadSZstNRBaflLoZJL0iOIAMUQXbJeyZQ8gtf38VJ6o4OnbCl0sE90QUpjUUXZRb-GVzq8FUdtLH1gT_VbWmAYh2OntVlIQb61i0zDN4DGrQLsEbEUmeIEbU-Te5QtAMZ0Vo8TQEWGtxStuvVgh_VOH-ziqOxE8GejMo5BozWP6cLVW7WS723zczQdIoAocse-mCBFpKJQFUEsjgY6_-75hnGITL6aePoenjsKV7gOoAMJJy3dH5EXwMGq82wwyoZ3S36uipC3P4xdAmKOFuH8UgC0OhlamWUDRzuVhZUzbCc47VfT14wTTUfMFiTxRGGLxUi717bDzJitjsje_1EUxP9KQGQhJADuPCK0sV-tj71HlMvsnbcpHL3RvjcKoy0vBfP_tkcr7snWCOJQAtzt43xl53VaFqc-53UuRKbnmNC195UafRlnY9wV6D2ofvhHnTfxD3ZG_bGhCRw-RfeH3fVZK1zluMUnJdN80Hp_5_wADjW27Ilae_2efKR8P1AqnzTufGIPCNqqvEBAE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریستوفر رایت، وزیر انرژی ایالات متحده، درباره ایران: ایران یک انتخاب دارد. آن‌ها یک انتخاب دارند.
🔴
آن‌ها می‌توانند به جامعه بین‌المللی بازگردند و صلح، فرصت و شانس رونق را برای ۹۰ میلیون شهروند خود به ارمغان آورند، رشد اقتصادی و رونق را به منطقه بیاورند.
🔴
یا اینکه می‌توانند به تلاش‌های فریبکارانه، پنهان و شوم خود برای توسعه سلاح‌های هسته‌ای ادامه دهند، که در نهایت موفق نخواهند بود
🔴
آن‌ها در طول دهه‌ها، با این اقدامات، آشوب اقتصادی، مرگ و ویرانی بزرگی را به منطقه وارد کرده‌اند
🔴
اکنون زمان آن است که ایران انتخابی داشته باشد. آن‌ها کارت‌های زیادی در دست ندارند، و ایالات متحده پیشرفت‌های چشمگیری داشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/147394" target="_blank">📅 16:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147393">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزیر آموزش و پرورش: با تصمیم دولت، وزارت آموزش و پرورش مرجع تصمیم گیری درباره تعطیلی مدارس شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/147393" target="_blank">📅 16:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147392">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) چندین خانه را در منطقه طیری در مسیر حداثا در جنوب لبنان به آتش کشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/147392" target="_blank">📅 16:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147391">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر انرژی عمان : احتمالا بزودی تنگه هرمز باز خواهد شد و وضعیت فعلی کوتاه‌مدت خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/147391" target="_blank">📅 15:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147390">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a18fd106d.mp4?token=YuWiBromjCkkN2I-eY3G64SiW0AHDgzlgKBelMz8ysLOn6QkpWDw4isgHvh7YYp2xGCSkNdb1z3-1oVi6jg3FxAbQ09itt60AtjqDrdxa95YnSgcbpO5uVaeFQ7BAYXn0gdBonoePgPOK-AvypyQU0rgP1wCEgT_m5H017tbrnmpWogkK92jkZoRDYfRuA-2_1q0TgaQpQDC0doWFRv29xZqzn-geB5KCYz9jxwY8yQO3EcqRSmRveYMtNsoqsUxUgyquGZn0xpatMDcyGg3HCtZJTK9PI6j85BrJTasKvZ4oaH1CwpVQcaveKcrEcLsCv-sXCUgzyWInJV_XRFwije3YkS5toq3XyupKH6oou2CblyE8JJRIMH8IHEM87Wf6RgVZZCm49L7AY_nrmHCNv0eBlnw-Skm4dez3VhrP1-gTBePyneSzYF3PhnKR78R4liV7IF1zDOb1izyfEwM56so0IdPQGZxkW51HKGFeRXnkL7EVHCjY0-mLkqRBUkDgjEJ3lgCTSsfq7oGyMQOUy1ESk89HOVjqfcCtG59AsJOFIQPeoU4pB5y3w2hvnhSAR7NkZhuRMMOpnVj6VKT2EXH7gX70ct-AcdbZ6SJGvvUm_blq5Mi-rvIw12IpOHRZ8T7oB40gpBbrnbExMahyt4cfyrorPs8d9YitGhzWEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a18fd106d.mp4?token=YuWiBromjCkkN2I-eY3G64SiW0AHDgzlgKBelMz8ysLOn6QkpWDw4isgHvh7YYp2xGCSkNdb1z3-1oVi6jg3FxAbQ09itt60AtjqDrdxa95YnSgcbpO5uVaeFQ7BAYXn0gdBonoePgPOK-AvypyQU0rgP1wCEgT_m5H017tbrnmpWogkK92jkZoRDYfRuA-2_1q0TgaQpQDC0doWFRv29xZqzn-geB5KCYz9jxwY8yQO3EcqRSmRveYMtNsoqsUxUgyquGZn0xpatMDcyGg3HCtZJTK9PI6j85BrJTasKvZ4oaH1CwpVQcaveKcrEcLsCv-sXCUgzyWInJV_XRFwije3YkS5toq3XyupKH6oou2CblyE8JJRIMH8IHEM87Wf6RgVZZCm49L7AY_nrmHCNv0eBlnw-Skm4dez3VhrP1-gTBePyneSzYF3PhnKR78R4liV7IF1zDOb1izyfEwM56so0IdPQGZxkW51HKGFeRXnkL7EVHCjY0-mLkqRBUkDgjEJ3lgCTSsfq7oGyMQOUy1ESk89HOVjqfcCtG59AsJOFIQPeoU4pB5y3w2hvnhSAR7NkZhuRMMOpnVj6VKT2EXH7gX70ct-AcdbZ6SJGvvUm_blq5Mi-rvIw12IpOHRZ8T7oB40gpBbrnbExMahyt4cfyrorPs8d9YitGhzWEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارک کارنی، نخست‌وزیر کانادا: ما قصد نداریم که عضو اتحادیه اروپا شویم.
🔴
آنچه ما به دنبال آن هستیم—و بحث‌هایی را در این زمینه آغاز خواهیم کرد—یک ائتلاف منحصربه‌فرد با اتحادیه اروپا است، ائتلافی بین کانادا و اتحادیه اروپا
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/147390" target="_blank">📅 15:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147389">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9gaLh-8VmNa3aiU-AOHGz2UvdA-2WQD8I8X6kLtfFQGX-XCYMV-Uz8ZvKWvgJFdvXxFNhbYdmhc-c3CWncHBt-0bkuTv6AE9XXPSJdfDfb6-KmgsB3WhdluGy28OU9xUOsqDnG1C34O3kUKNt-JIT5YGix6olPj4GejR0eAlmCwux0wAng2l9CfXK9YPu0K3nYsf0-CSk57dSWbks-K0vRtIOmZSie1vx2YymG0Aa1nEgbPfYZ1YPif-o8LjRJEaLgaEp_-f4WiSqrCzk0XZE3_LvScsXDSYUbW69eK3bDh7j7u10ifZOBJUfFG3Y3WyNphc9hO_dO1Ley9dCSFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو انفجار در منطقه مجدل زون در جنوب لبنان، متعلق به اسرائیل، مشاهده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/147389" target="_blank">📅 15:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147388">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7B__gd8j8tAIjTcL91GAMxLwJHIVB5mTSphEZsynekKrAHB6xWLlDUwBRGuCxHPgJl4K5Ihyeoq08rp-qQaYduz6_x2F03P0EOW6i9OMxbmUVvuhz9O3g6v_Ju3VVjPW62xVsCJR-9y8xwrcq_tb4DOP2rGjcxi8dCzMfCRdNbgw19GmpGEhWRC1CQS0MnQz8tkN1q2f_cfJ8Xf7BdecZ8CjmP_H4XSqdv2sZaPk730Avt33CF1DonnFvViIkXTo6L8PkEhnUCBt1wJ90dMU18Va-vt4GgddMd7d4INbHnPFMdO3lDeqPYTC6YFgsN456dTXQNw33KNwr870UUGaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیل، منطقه کفر تبنیت در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/147388" target="_blank">📅 15:46 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
