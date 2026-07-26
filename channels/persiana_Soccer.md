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
<img src="https://cdn4.telesco.pe/file/ndtSLrz1COmALWAWEzqQRhSu4IPiVLMHp8zBgunBsh2FfAhH4YdIx5Fw2wUZr4JWQdw_zFXm_Ypvv-VbTmoczi-9PwEQoJ-2j43sk-tdvKdzdA6ysEkDDt8QJR7G9GGJt8DnjpyGHXrDbeWrV5eDEx0SeChFqg6_a9b55KyndRg3TyLYbubHfINyIlrkpzmvKu680ssIWZnumsCbasDiYBw2C2PVhGAz6tQ4mEUZd-dVATMe2WKoaTNEENsNwmojsCSgg9ixByxOBDKzNXZJOvCQEf3078KsjCfF2wEoe_qj9uRMQSLFzVfJd2GoBZX2M6BX-tl7K2WDZf7FENsFkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 598K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 01:57:18</div>
<hr>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCD0Xd8yhvxTAPvNwu4IZC_NmDEvmxSq8ecCdw7kEujYODtaeQ6zMRKygbQYIhu2L5i4lBjwe_85J4mv8pWR4W4w0emT1g-IzmWRjG0Oydua_OjYRzmtc0kQFPjCJgP7AVH2ITEz3s7gfE4327NgBapAvNecLSPq_u06iAK3nNz_eH8twTxzZ59RKh42baknxThyNvhcBBxrd3NgZJcnUie2RCsR7nTqfGryqg02SDpOkS5hJ5DkIoZAuMI0xTGn6WxL_1R06p0HEPFav4_IQYHpylbRr2d61dSgJsGS1C50USA6VWlYRG83rTR0UojSy70pN2ScArlE7wJRttmd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y84w1ypiH9bDgdGr7nZLa-5QoVo1kgfEyU5k5N5f_GpHy7bQNYwK9rN6fEqntxM6hiiljGgCDI3DD0z621_pPuAts4Bbz4oCPMVXjmnBSE8i_yi9rGtKXsCmlycZO3x67Xa9sz5DzheFQ_7EFPbQrNjbvc9ewL6bIs6EMNVdpI_fAK6k7qac81ARyE7VWClND53cjCGbTantTkfZolS0IO365PJzE1Rq1PunJPVXTBY6Ml2Ol5oa2v7ZCrPsC66jl06psS_TBo1lteixQNOg3b-4TKB93q6FrAZ5tWeoceoNNK4i_6EMvCtW9Y5CbRDxTSEkwYmNQOlZoN2Ah8v54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1tNPGw1lFqIqi4dHtxAVhY7hGhq5o2f-ZjkEJKsskvX27yjIt1uTAorD9GrMJhXE4BcNSZWbE-0kE6shLHBmiN-VIDsKQSBfMQZlAi9X894gYuu_lyMmBt2vP9np5cOcF17IGJ2iLPejdX_hqZix6m_OeE9Mxle52Z6pCEGjroYQG--DGiLU4aQrhG2fqDw4i0SiIRFhgO7KiRQfX3ckfVHUveExxo0SD0CS6xz7iBLGRNCYLhawTJdQIANLeGIDW1GKYwBAB5_uyf8o-1VYnT4NhcFXuvjOJDYBbiJwEiDHSpV9K-k33zfkmYaM15RZOqJuHUt654o-T0A_aUFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cThRrhtJfJZcDg6P-4T7xXjJHacK2GHjDP1XIWT_qmj4ejfpZch2hdhTjrN9E2_mw0rrEBTYmdOLZqLrPcgpTR_0_Zs2bAKg3LLQvZBJcE0FbVej2bjQnPQMQrkwS3qNKikbjZ8vZSKCA0-o3q19C6VGbPssnCxtatDoLT8M7IFNnVKO8y3T6SHjJ9-_5lyeY8UkyE-gDGY1PIXRguqDm7boiQHHUNlHgbdU7i8EygZq6jMNHuAKKsTI_mnu48DOd8DXQ0a8U0ZqFptbJtQBhNzh6pNxdkBzU_XqdR0vBIMFK2FUkma9iUGKNrCPDT_J58qPu8FKUg4aynQwlybEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26580">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GIZpK8O5ThmFdH4WA1uQ-BggyV1qXEL5pv1mPys0Y16UxBEEEAHoyITmgDbMFJyyIVjR3eMDMbnlmMtn5vdXxKNqvotA-Mv0z4NBR5vvgHnejO9_g7mUAx4MkXt5srpqt0MePQaMw4AkWKDcQmOxKFBpBCbqYVYcsQCLbrmgjkLd2drInrfOhV-vaRT77WdUzjcMHm7q65wV_vJyTDwdke_PXUZl8pqenpVPOKXbifN20Z0Xm-4-T1vXuZDWR1UN9CM4OubdUgEfUeDoga7nY7kODIJu0a6TEr7C_6Ii0UXPHG4EzpMk2HJPb8bFu2oL-1i_yjUHfXY1-0yK5LkPng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی‌بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/26580" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WERtbrd2RhFf6A9sDJHL0voPuVgtHSu1fCOM_q4174IqZI6M3rb-xlMJJUFybN1g1Ac82EvnOVSeS0zUnAWSzHvfgPigQLkwWctvRgqAF_LNzmEzGQnx2jMh_Upr1fcd5dajTS8cUrvgFZkNrxfg9H1_0pL3Xz0U1YubBMlWrXrO3Dhc5l-HX986hKogcyAMFe0utaRyRnh8FXf_EfoeXmQi6aWiKBmK2G31PH8yFdanze--01qdxXGcBrCs090PLDRCM6kDiW3MOUcVjqSuXZY1TdW4yu9nZ-zFxKGAMI7cLa6Jt0gv80pn6YN4GdMLeIGbKreORO_pawwloZbZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdD4-cWDITfS-FRe-AtfjsfEf5SVqxOOHGksCn7BGz6p-OQ-724LmOL7k07BrVnomp2LpGfE-yqOoPJZw_biIxFAS47uyNyr1a74_zX8urtHxdvzMxGdw7O8Z7TNrZ_pQE2Pbf7hALqFWoupl6k42jPXw-Pt4UqjptTK0PtndnA0AgngAwHc2pmJjtrTArHtGYRjiB9RYiV52DtdFWWKRyqlWM4__X8taDR0y1OqIyAqX9evsGwCdDprCIutU02WQ7F7y-f3dzRyTA2vrcDsT8bWNDo8GuSdOKtV04J9yr1w0qczOO4xAiT3ZRpIfQk-JI8tAQ_ovp4RrkhMxBzJKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26577">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKwevw1H-CkknGUWOqtfn-aQ5bT5s6fllVvhFAN11d0hzENx83OqTpTEmoa40E6X83oOdV9XkmjyN0Yp1Jqvxa5C000CMcfUkdd1ia3f9hzVOHf5FzyQGQ9w-LrGw4nsqSCzlDbiaxiob7sEfet6lZSUUCr9FFmWB1RByZIZXj3mt7F1w7lknkfEkAKRiL7_tfm3EzSSTtW38pAZtY-xgC2U7tqC1xV2E-93WgjVIGInI_nm0Ejgg3B3QVMvmhnVZfF0jFrZnKdWgED7Bs0rxTGIk0hmsP2aDS45836xE4AGuAdSk7ealfReHPcUn5IZasZjjqpUMvYc233D36d0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇮🇷
محمد قربانی ستاره ایرانی الوحده امارات: رقم‌رضایت‌نامه‌من 2 میلیون‌دلار تعیین شده. تا جایی که اطلاع‌دارم 3 باشگاه لیگ برتری به دنبال جذب من هستند. خودم‌علاقه دارم‌جایی‌برم‌که فرصت بازی بهم برسه. تکلیفم ظرف یک هفته اینده مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/26577" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26576">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=ge755alZYJgBb5OHgyVcNKs-1Dgg5NUEEhhNm568qPFzMmDusXloeQGZcVg13nBcuxsVbMFV-yBSdGYR6F2dNJMb7n_PUr29k51Bma780s0D-np1XS-a2wmDMDh94iRYF7wRlDraW7Cite3ot-T-sB0s9q4uzsYDVKrY8j3qqDbFObZ8kc6pfFRqW1a8icmKEapI_gSlVQZ97u1g7pZwtrLMXBKA-ZTUYL7oEXfQG_ttGhjC_c-wyfK9jjTJb2nTzXz9YBWalVcFeYRd-lzwHCkrrjAja6rcxaXNUZZ5U4rPhyPKe1tiI6fBTYAteu3OPWaLqyqpU-gvxwGrmHMJFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=ge755alZYJgBb5OHgyVcNKs-1Dgg5NUEEhhNm568qPFzMmDusXloeQGZcVg13nBcuxsVbMFV-yBSdGYR6F2dNJMb7n_PUr29k51Bma780s0D-np1XS-a2wmDMDh94iRYF7wRlDraW7Cite3ot-T-sB0s9q4uzsYDVKrY8j3qqDbFObZ8kc6pfFRqW1a8icmKEapI_gSlVQZ97u1g7pZwtrLMXBKA-ZTUYL7oEXfQG_ttGhjC_c-wyfK9jjTJb2nTzXz9YBWalVcFeYRd-lzwHCkrrjAja6rcxaXNUZZ5U4rPhyPKe1tiI6fBTYAteu3OPWaLqyqpU-gvxwGrmHMJFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه نزنی ما احمد گوهری رو میاریم به جات!</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn5rHbb2iDJYtqEZsWL1Wi24oFbVUXj8w6pNjwpZaTUmnMCn0kZD9U7LDolPVgLL2r3MFkRRUQnD-pCij89W-4Mclktzq9O3hD-o8vU4fvcLnFryF_uoy9DTNd1jjTwT_utquwlNBUIfoBrTXGBBfCG9M6Ld0euvGnAGcjaW2FgzpFFK4B-tg-IinjkCztwIlyUSoJ5rUguP4XRyZJ4Dg86ccaGL0kaHK-J2b62qwQRYhzahYGcazQe6ajQ8bFRbVrabB1fzXP8BFUxBgr9oOnW0K2pdTLLm-0UNgUwnMwo7nzGeH2V2GrHc84LMp6jLaEyIl-yPfRPppR7aKe-rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhEHM7pxoBmg-k8u12Uxo3Uimsw-86XV_ZBKTriqzD14H-Z1vt55PT__RPpjIyYXcsc15ZUx2Ce185hoCo-yr8ThoK-Qnm0NGUbabarr6ycE_EwjsN1OlLRJGSCxGELOS9C2jKViheBO_bRkLl_MN3xEn1kXENngDC1xMCJw0rPVQC_aDi4kH2Oz3P8VOx10Bngo1xHVBaAhWzNelNTGFQmbRJ8Sm0fqMxUmZpETsX9PpQ4e7sOrq93DmodUT70dv5LN9Wtlg_Anf4voGF3rW1P5F81HtqkpAbjrNMLLG6qBosYBXVVWSxetknqTOCTKe1zPsJXexotglNCGOfQdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgcfWqFQGCeTroBY2gUDtGkBWlJI0hQgOoZwfGRLRpAMbaFsVSrvrdXaboRJTLimRutZLpAm43RFcmdX6kjWrcRRUtkjJtHJUnPv0fVupZ1RrTyu6sDXeg5Ey2FaZefNaUS638OKiFmfP6syWuWinxtAOGvy2uyiPK35bgllymWONJniperCCQQYxE8UkUlpJGUr6MOi_sBQm57Qso6O31NoD0p-I8REbxlSxTHImuL-wFTuOwylZBRqKl0XblJLy5U2Eb4ohuMLdM_eL2mCX_R-ItRS39HTr6VlO7ggFkGJ7Foe-ybvqNyJkXFr8J04IbqQTu_JTGrMgzzwvkxQtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMpThjY06ZQsizDoIW9lshH_4VfpygY7tJMqgUs21hZ5HQpRfIqEcod8fMlZQXgMhWBj0aGgiNfEGuJTGS19ZyR87hWmTPzpurxkU-6ycxdShA2bhRh2A-5ReJ-vKLDoOHR9_z3sNH3mlWtfVvdYXxbcp3H8RAxUCcfNB5_lr0cXUQ4gP0MsPFXG2mMhjCWCtIU9oJqy5Gk7JUqSm9SnLDlTbOzEkK7AwpUeH2lTa6N9sswNI7yfAtmFElJme6Oxr7sKCd1JKPgayKSyPESwX4RGbH5HBQNvMow4DCImMjJSsbK1ifmgA-AIjpOEnCibHOKsUUP-rlbdQXFR2YPy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGc7AFT-iMdMsBazX232IouRdsNmL1eWG2X4yEMcXky3gB93wQPpCO6K2Dm0UwJ57RZYKgnHv0Fs2s7IDI0JAhiF3cORjhwyLx2m9dvH7sBKsdKHmFKKZiSMUs0n3MOvEAD2yva1-NIHqOxBDUvbUCUP_VGCVtur0HmMcdfNE5Zqc5MC0N3Hx5Z-6H7ne1qi5JVB4wa1glqSP-2oeNzpw3qa4BdKoSpnNNi0RE8W2F_NspKm7EaSCoZWpuv148qNI1lQ4hhAXJIHkLUHafTV9Z_1xxlpVSl7A3qIdgA35XTT0ZK91qC7YrVHtJl91Deuw8b8Nw-eYEKrsuaYiy-d-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFp6xTPwwDo9OQXlMymoCM0vT_d6hs-e8KHXXvZua4wG2X4s_lUizT1IJJTm0KZcFBUSw-4YLvlFTzgzSFKzpyrhYU8E3XjWIPMoYo6RS7hBwZGyIFYbwulC4p2RpqWkU6Xu1SZzt70KA8LbNVI0xSUvM03JUM5cJ2Om9GGo8f0Lx5BVhkObNQhxwN0PzuW58KFa8lfNhqXzRINczBDgGw7Gosrdh4Ld3pKs-rRESHKa6r1neOo2SPdTXsJv_VFqT3iQCk8UKd-tebAa1OMMeksqkHjzhdgdrVVwIO76dDmBfLX4UD7FaoFWIoQMcoHhumZ1CJR_o5CEmDmyy3_-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDZFyFhLC7ZMyUfwXZl-QJhJTcgoz4tOGdOJX7WmAiLYSbzbr38eu96yRNvy6gWqyBA50VEKNp0Aa3SWkNZniohhqDUXIlXdk9H4VWvC0qJtX2nBms7qZCEwj76CiWfHwG-wuFIBvWLlg7I7QX-PI99rBFw0AvPj2RB106pPzVmExqp2euCmegUEJFuYLL5SuqyU31Puia22kk-ldPolwMvQWUoJMdEGTgslrkJaT6XNb63CMPL7vGLFZ7MZJ5p0tZvSfAep3Lt-lmu2X1O2_vTqlIHjrYRoW2MZJuKe3R5_MJy768hoScUGjrHUhHQFvvKE85IZgIut_yKbFzhHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKfARVaPzLqcYz9YwjHm-qpyiFyFp1xAenj9ZCscACUM2ua3AzGSu4IICvf002d5KhI3fmuZFrICbazASxLeREznPqvhEw50acdGRQYiADwAhjFxpDMgLEOId_c5MbExDoMQeMUBIu46Pa7FeUBUmtBPNDTxHsMoDoGB1wtwKHkLWVByHab_eXTgzsXVYGvxUjBQmkdt0kAPwdTVh0ytyHLEgBz-9xCqdOrX56RCDC-6WSKEHKaZ24VSIyYNR617ileSH2enPh9ir6eqe_7n1Mqw1xJ9kbgtVZtPNMreOawtiLvPpRbpqQlxdqlZlv6yEAmwvBWrixHhtTfUx-GVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xhues1riFAtnITQlE0XVG_46o7jYLPUbzrXJv_Ya1K5vX3VWI8LPLznrQRlvDVrTgYk3sPv3Zu6_PiIa8LRMcjebhlBUQAtcxTk9a6xgarpTohTEFbCd08lZ59rrxhRHmrzOONg8fjs6CGjvF-M4JLihnlyoNrrKDbhC-cGfFCQPaSC6pkkfgot9G4IEJPtb654UCeoquP7XfXgYJxcakYjGt7DW1-WoY8QrRAwTGXvcG-1oO7rU8gOug5d2G_--laozCV-55tkYrSgzi417mo3OR57OulFdmhubXpHLXVeKewis0U5NuVtubIMtK5PQBdilPbs50U_-fqBTFYtUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26564">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TV3Uyn81n5NHSkuLu8bNggPjn4xfoTO6dBzPHSHqnZj9xb9ZMxK_SX1qCn5GcoZKHB3-f-9hsAdTXPDt1cmzMumxEh5mm0128eHwQEGcMbcSKlXvFs_oWfyEn03_5hZnyTNjezJ-194sra1m_FcWUwFDGBygUkJw_LgTTrxQ9xMd9Fr-oJ5wmuBfvdcBpFzXCPPACuVS6lEIf6PSpeehCMC0krf96uyfv5f8fi8dTQCh28wNKStEdbqgbxqNMewe3M9EVpMDfF4YoklDBoOd5sOuAdvM1eA-K69VUYqSYYu503RVaLkejkDElYgyP_1MhTBWYKyj6JADJScXrCQ29Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26563">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=hucH-4UszKCQDzeNK6sl85PN3ijoVwh53UvAbHpaUW8Vh-JPfBvtY0cdrpOACNXbpGEcXhSi5aOwKbqarEQdQ6cAWsJAU8sStOcDFSNiJ07mdp1oU0a2xRH-1IbSdy6j5OSaa7_Nr6ACPs4Nl8WwSkZDSWpPTIz26htFrCjpKj2z3pZeSwI-t3pydhfT3R9-45NPlXZ9mbRVomxSeHQMRm2F8JVM2_iEpUMEqRKVIryUVhUS_tcWFGRvDxn_2Aa0sWJTi0o7kOPCdTYXKOiypV0WIloOyoZ83wSiL-Wvlu95Ti4h2f5QnA8-JccbU0FKVY6lmvN7v9rFFary8EBtZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=hucH-4UszKCQDzeNK6sl85PN3ijoVwh53UvAbHpaUW8Vh-JPfBvtY0cdrpOACNXbpGEcXhSi5aOwKbqarEQdQ6cAWsJAU8sStOcDFSNiJ07mdp1oU0a2xRH-1IbSdy6j5OSaa7_Nr6ACPs4Nl8WwSkZDSWpPTIz26htFrCjpKj2z3pZeSwI-t3pydhfT3R9-45NPlXZ9mbRVomxSeHQMRm2F8JVM2_iEpUMEqRKVIryUVhUS_tcWFGRvDxn_2Aa0sWJTi0o7kOPCdTYXKOiypV0WIloOyoZ83wSiL-Wvlu95Ti4h2f5QnA8-JccbU0FKVY6lmvN7v9rFFary8EBtZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIjINTQBQjJTcWh62LJdei1jxcbPsWs1fRRK6SflT-_EXxfu-D1uJFd1LnEP7KwcLVn_F8Ys7J2hmJV1zuUjoxMcpMSwXPlWvrHw2ExqoSRDqacKTHHUKxJCiDjVwjBg87u3v3fpAnekup1B8ovJdpfthqdvfG3L6zz4BiDkusx2p5_Xvrdw7NT95vPon5X6ugkSjAii_p8fZg451hIAymOyO0co5ADppxV_rN4yjA95fQJuuMqIO-uD-qFb0iQNt3sCU7-l-cRE05iRMmVSVAcxtSLMCpMUfIekwgTpIAnVbZzMcsZ6h0CODXJ_9JtVdaL7YmSgfIp0Rzx7FTrZHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=o_4dbTG2jSZTvdfSAfi8aJVUAKc2OpApNei4G21aFR39TiuewLtyoMusQjdzoCf459b5jgEO3YfyokL3IzP7VbWtLW-dHk988WGCZT74bXujL1N2Gh6JyoEyjEVhMoBSHQDaneAFWoA-9iO__lhOFtBM-sUAwo5LJnLAvhfUxZvZ3TGb-afkFK_HUz-fno7AsvotSGGVvY2xX1I8lHiuEnbIMmOWUJ-BkRanRxdakh8VspvXZrc9TyUIwFlnlhEA2MQFgAMzBNtOtn_u2oH-rsV9x-UIsou4Wv7yYa8aR3uil-JnAEmDV0d9yXR1xwAHKKx1QyiSQafXimM-9C0xFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=o_4dbTG2jSZTvdfSAfi8aJVUAKc2OpApNei4G21aFR39TiuewLtyoMusQjdzoCf459b5jgEO3YfyokL3IzP7VbWtLW-dHk988WGCZT74bXujL1N2Gh6JyoEyjEVhMoBSHQDaneAFWoA-9iO__lhOFtBM-sUAwo5LJnLAvhfUxZvZ3TGb-afkFK_HUz-fno7AsvotSGGVvY2xX1I8lHiuEnbIMmOWUJ-BkRanRxdakh8VspvXZrc9TyUIwFlnlhEA2MQFgAMzBNtOtn_u2oH-rsV9x-UIsou4Wv7yYa8aR3uil-JnAEmDV0d9yXR1xwAHKKx1QyiSQafXimM-9C0xFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZ5q-OBssMIk14qEsij7giOftjlapu_bvptZpzQyWxJKar14qKLxNQ25dzARyRlWKDYrj61KnIvBYXSnnjwZc3dhsrD6Y5docVHDpqfzXWHUcjfn6wdxkTPv5Jc5iYgknmH3Gl6a1mdueWfsJ-q0nIgHlp97s51GqYzEOqK8pmMjCAn_u-NYY1bhwy2MJSNF1JBaByZpcszBRmovKl4wCDwDDDK6kLKx38bhQ8IzYemAV8SanuF970qpPrz8SI95nd1WLYytjRg5nQXnq8ozcq02AwGRHXT2Hv7C2yTxRWlCAcCyKQ1apPyj3ZO9ucxfwNQxH6QPEOffJjqX1oCAFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPNk5Ge0KmV2gkQJtH8s63uT7XdInYOjAAdyW0ex_gxFHq01C70xMkSyq2_SoSqvoKCYjVr5YxNHpJS8KMjUO9ELOXWnZa2lFeawLlozoszqVCmGLgEP66_ABLsRLwi6DtaSeEqd1PxB0K2Yteg7VjXhraqMzU6FA_si4qD80HgCiiRZlldsVon5lplqx67DuuauBxGTdOv70UlCu2rkrJo14woB9TUuSQ44N0l-m3bA3MVXekzZhUkFB6NQ7Xh7lY80pYlAzBOgYD8rs-aPOoMBlMDOzjqcTOy5k3Hs_EXRt1AXcEeibiyhfS5433mDmmuBSZNn9oeMpju0xbjNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26558">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKq4T1vZSP1je--aJiVhKfRaQfQR7DEhhrRZPmchhLHIs8VRwCuJIpeSbAntHFaEt1tk0ruB6GXh-h10gXetHvmA0ovMzo96dRhPpUthpssIqfm7i8d57d5Oz-INpKiokqUBHVop_sgDt15GUTjj_dPZ2o7v5kZ1cu6gcxKQvtWVgOFEEFYjDgqNQ9YfZhcp4B7lf6tOuX0yPuKO64DNqImDm4yhSlqF2GEmCRgkAOxQDJNDzAU5QYzbGQ4LL72qiDYkn1O3Ke0QRklaNG6ISLZAWn_uc5uQ7P1ursGPGRVdCUop1dnoVZMGqfbOa97QKajG6kTkLT9-N1QHdRwN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛طبق آخرین پیگیری‌ های رسانه پرشیانا؛ محمدرضا اخباری گلر 33 ساله سابق تراکتور و سپاهان تا ساعات آینده قرار داد ارسالی‌ باشگاه‌پرسپولیس روالکترونیکی‌ امضا خواهد کرد و رسما به جمع شاگردان تارتار اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjrIlwwzjYCy-iEpbXe1UdW51TGrbHy8uLuod6Xo9JhYlmBRPuZFNKReO8kl4uXt1ELceVv7vsrJ_sEQS4CfPpOyq0gFSqMmD5Ps0ia2XimAogI34cVEVylrou9Nfp5_-Uyxt1woCK9KOuWK53uhNGEipy1yLr0tPW2CFeNCtGfjP0ArEOk6q5WUsLzU2qIV5R_jx1tQtPPRR05uQfMkmALwB0fbkN2yl1-RqCIJ4ouGRW5TOZLrvUQ15EobCmqAt02E-nFhoKJi4NVwQNH6ET1syUsCm8F8h4-pJWWWgyWXgL07oC1A5xRFVy-nABLabASH5NFmsspUBT4pShCnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3e3fcjhnCGvriMP9oFyKOXiGS7Mb_Ky4GKp4ZwtjfD2jJNbNea48RBHZfjtsKZnHphBISxt1wMYNdg3ZanNcjHcSaXDOepQbGD3chVP74SFZIV9W0D4KOVf_9HH-IE2Nuc-Ifjfu3A0Mc1qIqxfxIyCo8nLA5PvJif4gI-S3vfa0Xpt3JwtT-ZQUXp0HPoxkUqtGr6qJF0mKK0KQ8J9WOIzw2TOyXNnFqKmDO3DLDDx_XozTz3EWIcYZdENiv7kTWoV7y5y_CRnjLx7dhRqt1X-_F2M_6X59oUyQH0YuFnoEfHZoAm8nflG-h8605Ui7jYTpURxL7WCNtPyY3_-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGrNVAs8FENF-rva6rFczpsobnywonCnxrV2Q9-V3ZMBAwCoiD2ZOcx1G7xhPY2bP-OaAvEJUCA6s5g4s3Ixq2N1j3nBHkc5rU6d7nozFe1a_Bpa5tUF6XbKpLN1MKIYx41IIBn4QJoKwhMAHVcLKGWyL5zyBwxIhUxO79iYHPekmRlixJ2hUToH5IIM_0kHxyEiniCIitiz3myYVxtLvcZHzOgcGjxjl0xDEbtXMJL9mi4olFqncW7cCo9rCg2atCp-MY0jjBfuIb_e3AvBLEX_v3EkKdaZ6HX7PhGVbs1sEZs8mNstnMBxjP8GywpTTsLvavJ3J42EutYVuRkGTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26553">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxQjWMrI6nZD_D2A_orbQUb1T_SBl7akAS-c1gkGdM9KGgJjuJFMqjKQRBfsXb4nZBoqTk6dnHZj4h7zG_WCXWrJ2UIGgcrlJmTwh6uV63gySiXpYpmkNba205yGT-zt1ldckUfY3yH1tZCpH6uVN9JR7vAhUlVM7CzhZuRa7mDmcfJmEG4YYCYhy-dK07G2_OgIHcMv-YWliqHhBNO5aINK-hnigj1g971H7JFXTLAkX02ELquvuZ3n49pN2JscYly_Gf9W06UnvyBqby56FxIlGsNPb_oiwxwRZQ15TAVbEad8jQi9_PNMin2aGwC863E77Dg-R8e68tfS6StLlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛همراه‌شب‌های‌فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26553" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=HiTg12Ms2bV4zUYSu9DEaM8mE5cewgMUo6P_t6ZKLhz0DrUE19fUqonbv98Hw649qhfrn_B9kQ3kZBPAqhvxHgOx4yoTaDNBxnY2UJO_EEk-YCuDQeox6tzwNI0M53e7oujWfS4ZqYeSizOyWw6MaQ4rBIBcK-Lb0AXKJuTB_2_JY03uYQfptUYhlrYJ2uUPdLjuEfJXmXBqjai_MJFk65KV7FC2CIPwGCWcW1HXb5XfQ8ov3Jjr1_rNvwZckNt6hMsEc8Bk-pj4GW3cWa-7etIfJcLbJ1sanrYezo-M7pwuED9fTl08rzX1eSR2p5eNLcDD9YCAuzbyk6ItXH4ELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=bk6nzX8olL0Zw-SILvunWVhMQEXdhCHsfL90rZVeS1-6YuvE_oKG9cf1JiNxw_Ed8T2a9fhon4e-DaxnSl53OgI_OjYON48bXc4EOTNyOePVtfWDGfvGMNAKwqLJtVUYXErpsc8DQcMuahA7DFfHdFAKCeBjz8vz3Mb07w_3duUM8bBaK_Tl9ajVBX_W-isC-RpWn9OAhDVAfOeRUb7-LaO8s69RZKrstzLoEwxab7NkHTXNLgU4H0l-iEdHRmxa9HJdrh-D_YBmNgyb9Bd3135hBQvELz1pu18fnjB9PEeI20ZM0umJK-ilHEjYhFFaPlWWWrnhHiQTsCWEhEVwwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=bk6nzX8olL0Zw-SILvunWVhMQEXdhCHsfL90rZVeS1-6YuvE_oKG9cf1JiNxw_Ed8T2a9fhon4e-DaxnSl53OgI_OjYON48bXc4EOTNyOePVtfWDGfvGMNAKwqLJtVUYXErpsc8DQcMuahA7DFfHdFAKCeBjz8vz3Mb07w_3duUM8bBaK_Tl9ajVBX_W-isC-RpWn9OAhDVAfOeRUb7-LaO8s69RZKrstzLoEwxab7NkHTXNLgU4H0l-iEdHRmxa9HJdrh-D_YBmNgyb9Bd3135hBQvELz1pu18fnjB9PEeI20ZM0umJK-ilHEjYhFFaPlWWWrnhHiQTsCWEhEVwwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFyIg9yz0mLAbJarvskX-v6b0-vGO8fs74pidC0m9FfjRMcbS3PGev05929daig8YJUsFFMnKPmbboHp4TvHGhphGbNNP7DIuPoasoSak-LfpYu07GjCAWAmwn2ug1Vmjxebm6enRy55SEsCitBaMnXbglLqic6nsNwMnd8IPlZyTvpPtfI8ehEpMY5xwmUtBTd_lKBEwsb-hKHnirNhZOwPfTnBrtwSDMm5C4WsjsEVAbsJhkFPY8GgkvDgjFV7f8i0l0vG7FycBLYoZ2_lFYbXPxlhakwNaJnX2ZUHYUyhfZ8xQj4EFrZQ-Bge94iRKfHIo3Jxf3FJpKp6LTG15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=Qo5AGNrZIFUMBSFKSKYkusIB9_WibuDgrtdF7iOvHvW8HIa0sIf3Aiu6gYW-ias3qgxw5eVUjxwzCxAPqXvcOZryTkN6UYfRvKkU7Ys1w6OvqfrOsOekuQ-ta6hBp5YCuJIKg59oN_KTizNe8IAheN03QfRgA0486gFumMCjGWeCXq3f4EJERX-aF-NN9VICZYqdVRx4HPBgCi0jOW7X2mv1F-wDFDmXRzR3a1QcydiQtrr1fA4hLTjiuhp2uFgysKy0HMUHtNSHgjiRDsl3zTnL_VYl_zlpqVoKYvEs8_-i7XY1k56lH25OsdAcjSPm8sm1e3DsAYkGimjYBlu5koSM3846y6g4B6p33Zwy18uA-5Q-FIsiZMv0ln6Z-MbW3VeuCEoxbFYQ35wwlEWwlSVBjaFyevES_72Qxz4Ma10NE7i5TM1wsC5NWVvHGqsYbSJ4OdyRr_muezEwQ0_STapp29kbQ9W-o4dg_VEoqNVqiEGulPUg3yZ1GjesZ1kAvGYS_oLJpEe-pZN7oc6qbJ9lryGl4aJKwUrWHUsypWgDj6zXvMpKaXZb25XAJekPifryAyCtHj4gjRTVPJywk_O7i_nDDgRqw6jk1JrjXr74TgNOwURghUMniFCdbaVJ3IzQtPk_BSiy9ALaZeR_z0t4n69Uwaj503n6ok0hdcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=Qo5AGNrZIFUMBSFKSKYkusIB9_WibuDgrtdF7iOvHvW8HIa0sIf3Aiu6gYW-ias3qgxw5eVUjxwzCxAPqXvcOZryTkN6UYfRvKkU7Ys1w6OvqfrOsOekuQ-ta6hBp5YCuJIKg59oN_KTizNe8IAheN03QfRgA0486gFumMCjGWeCXq3f4EJERX-aF-NN9VICZYqdVRx4HPBgCi0jOW7X2mv1F-wDFDmXRzR3a1QcydiQtrr1fA4hLTjiuhp2uFgysKy0HMUHtNSHgjiRDsl3zTnL_VYl_zlpqVoKYvEs8_-i7XY1k56lH25OsdAcjSPm8sm1e3DsAYkGimjYBlu5koSM3846y6g4B6p33Zwy18uA-5Q-FIsiZMv0ln6Z-MbW3VeuCEoxbFYQ35wwlEWwlSVBjaFyevES_72Qxz4Ma10NE7i5TM1wsC5NWVvHGqsYbSJ4OdyRr_muezEwQ0_STapp29kbQ9W-o4dg_VEoqNVqiEGulPUg3yZ1GjesZ1kAvGYS_oLJpEe-pZN7oc6qbJ9lryGl4aJKwUrWHUsypWgDj6zXvMpKaXZb25XAJekPifryAyCtHj4gjRTVPJywk_O7i_nDDgRqw6jk1JrjXr74TgNOwURghUMniFCdbaVJ3IzQtPk_BSiy9ALaZeR_z0t4n69Uwaj503n6ok0hdcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTDJgcWbUfBqFtbo6X8xLc0VVmEIa9_2whzFD6pZTwKRmZC1zJlKncIDb2H-4UaEyYiFPI40EMQQ6_KIqAWU3XOwxmAzwsW6QQbkECBg-8Tkz7HTWHVuPeN4Cty9qtnD1oFfPJHL7adJyGMFIcjmFJxguziEoFsReNI4ygiuwq1Ah9dnl3gC1DONkUNiAnyXbHOJSHZj4RE1W-F4mmy13vdTcY4hZsJvdVFWP6VY7ZRmPKGnv3VYkMyOzz3LpE-zy3q82w1EefzzuMgOiROBBYNAdW9ZMGJrIOvGIqwyeFhYZk9Fw-iKAf7rjOl5obD_-_VrW0J_0qPEUI_ESG7NTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcw6BKT1RTHBG0LNnZrLWG0UYhxr0cjriJOcJQIueE1fJ0-LWhCala6A4XWHof01V-dSXO78YurJET6ekShlK7FskEqbhETeV-69m2sxH4epiFO6mUuuN3We1LHShGUvnDc69OWajNJ6IQVeq6zSo2H2BMtqHkt34Fbco4xqHX3XD30eBg6L-k9juRgzVdvBvkX-98P9lM2a7TPiqRYlBJFe6laiLd8Z3d-ig_zaSn6Fx-6_jQd8uNXdP4snK7pPxeL9-skIRoJlMh-5JGFhTfwpxueiCFECGKLrhCO0t1VGTyMsYw4H_HL1wgl6CW3bMiYZQ8AsKRJFWapFeVPZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yd4mpt0ASJyOx8DWuVbiZmWzIV374QWc0Ntyux1RNSE-ivdl27ulBcs6emz8aL-eJ-mDBYrxod5j981sppPplbA6bHUYvHqV-QJ2yuxb3sgp-FVBrkinqL_zeH8qh129ZT13xlp51nNp9WByStbYq57VFCdyxjZEGAylJ-5X0F4VvjR0oKF1zv7zJzl-YwOUd53wbb8ybs1djU2ZEaH9PtbrnUWuRNP4yBC0dZsTOVCcBplRij7kTfzyAkYn6X83Sc_dNUaf309pJ-WEySZLKl0NKjQtaC482Frc-bk2BIrSUaQeTpOBH3A_6NwwDHHa7s8zu96zd0lp0x74BQru0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=Y5Q4PDmWSf3q7Bua6dNY0Ci4aiiBD64nC7svIjfr3ETwXKjF3lHIeNp1orsdJ4-54-Y_Ii5W2hk9MARQRJo3J01LvDnPlBTpa4v4BPSufHmZqxnLWgbwCgr-peYFcX-MxAPbPtuLpHnJkLalMiWd8szmySyIy-HmzSTqkYffdgUx-AFBjTHa4KNFy2csqBgNNAoIc0t2G6wa7oAbb4yxKk28Do-YomZlzZgrLAu-O7I_JYlAU_oDdBpVstcrYadEAlCluxMqnA0j1N2TR6d0mCdqCBZNYmFpqmIZMOijSBsBLhc5aAz_jUqbv_t7fBVqSy9eW5ljJambv9KBr5qnBCvCklBVFTD2SpKQ0RTjj_EME27oHS9jWnjEja4EzRH-vpVKR8IhrJLqtNy_Zfz0_TQ690aBcf3FwskYxSIhjq5m2mEUl7YasnK6dFl0mnvcF9QQxrK7hFpJh_FdREdQAkSG_Gkbb1CN_KYXR1T8Ic-0yDracaa0BvaFdBERgEUuvBoXbBcVFdDUpRvVmqhjPG55mNfKVrWeeCjv6N73AlwQ78mp13CDK2dJNAQS6QD2-mS_9FPhU8M5mcaBLfRiVm6RPN6CtrrQYqq94-uKbPMviyfY5F3FxNxtGM3z8UpbbbS4oQN2GDoiEZY6sj-zvMWRmtHAl6mWmJzhLFps508" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=Y5Q4PDmWSf3q7Bua6dNY0Ci4aiiBD64nC7svIjfr3ETwXKjF3lHIeNp1orsdJ4-54-Y_Ii5W2hk9MARQRJo3J01LvDnPlBTpa4v4BPSufHmZqxnLWgbwCgr-peYFcX-MxAPbPtuLpHnJkLalMiWd8szmySyIy-HmzSTqkYffdgUx-AFBjTHa4KNFy2csqBgNNAoIc0t2G6wa7oAbb4yxKk28Do-YomZlzZgrLAu-O7I_JYlAU_oDdBpVstcrYadEAlCluxMqnA0j1N2TR6d0mCdqCBZNYmFpqmIZMOijSBsBLhc5aAz_jUqbv_t7fBVqSy9eW5ljJambv9KBr5qnBCvCklBVFTD2SpKQ0RTjj_EME27oHS9jWnjEja4EzRH-vpVKR8IhrJLqtNy_Zfz0_TQ690aBcf3FwskYxSIhjq5m2mEUl7YasnK6dFl0mnvcF9QQxrK7hFpJh_FdREdQAkSG_Gkbb1CN_KYXR1T8Ic-0yDracaa0BvaFdBERgEUuvBoXbBcVFdDUpRvVmqhjPG55mNfKVrWeeCjv6N73AlwQ78mp13CDK2dJNAQS6QD2-mS_9FPhU8M5mcaBLfRiVm6RPN6CtrrQYqq94-uKbPMviyfY5F3FxNxtGM3z8UpbbbS4oQN2GDoiEZY6sj-zvMWRmtHAl6mWmJzhLFps508" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOVkt5oWbC11Gtq8YwTWAUq3XmCP1D8_VxYhNGsSIAEXYnuta6Dswv0QojwOqGqdw2gOoLkZCOLY6YSNGTKHOaDripBMiAGw87QfaMelVNghDWeZqqAZOFYwqGG3aHaQDUjiUDCCNalLdA6xeNPZtdHyCGlEU9yPfW-6imxMjjWHwmrtfIs3nbitxc45SGFUJ6kGLhdqovFW7fkkO0aPE4ST7plrAJkHO1Z9JMamDX1GuhxRt1Jh6r1mCqJpx_c6SRa5wEJUDahw1O2mpKLFLNthGyLESSAe0clTVtGjuGnAd9VW8jL3oSvG5z4J_HrqjP9i81NfYh1Wf7mnlMg6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g36of68ua5lMn12R2QEpJJfcdDOlHb4evFa_8L8iawR4te7QfV79cHW4ThVM25d60DeY1jT-m4_bOf6pQH9A3xjdTK1UIOHopF3R8FqTycxLR2bni3F8vOX5oyNB0nk4Eb99Q0QpqEEkV8BleoeLazOkdGWMvGTFBxbjnvZH-lCqeQpVHWI2sCOIEhzgnEoMQCa7NXZnvEuXi8eEM6NdXSLxRAYIZqtIRKoJPBTFgBZhcV43ikPvS94tXLnE9utRfu7MYtTlwgmS-qnsR7YjaTTKXFDU5afFcemGwcVscNq5jbXC5TyXLkOdefCO0AXaKodfqqAN-CmFwTN8rlbTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FASUWGNvYl_oCB02AJoVO2SqKjSkASIQiWOlXel2FcfeMAhViXL7YfZ3VYazBgE8LdpkWKXz5xIha7_JvY9BzEymRDv_3AOKrvzLs0eOuiijUtsdbnrdeyTdRUHC2bsmpDjaXVTCTiLu2fCqUUZQOiiJtd2acd_YZpFQgJRdOP1tsdML56OlctGe5gRilYKx5AfMtEb6JZMkwgLGT5Efr8kkok3SO_uYi8qCiz_yGnwJXR1CjwsdjCy_4Wxl8Q_OLMAXMFhkCzW69CHgETFE7u0YNmrkadUQDFO68DkkmIwXF0P7LZDba2Xom23RWpXD9HFk3pXhGSonbw8CKziF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBr28o7kgKdCWDDcZs_yMqV9yt6XFdFI8Ry9WCmhvcA5jcNw1s1dcdsd0BJBnJmrUprKwps3u_lxfJS1CwcCyOI5vjSHTu9NiexWy5Vr0S-u9OMOoZ8y_R_4D62EfaQmb9S_eQtOkboDDmK4dFEJkvsd15_tGOjuH59IIbw8GY-8CzygQwX159HXMK59Ja9skVqjMcn51xBvV_jDovaelENj7aNhHJq5MOrZ7KLrMRyCWNvgVM6WQfX0jC9XMFBC3IAXY9GB45TxNuseA9R-drjmdMhkz_nKBkZRcsCY57PLCq-Y1vqltDxMOPYycCgz3D2GgDLgKWn93efN5TlRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD6H5fweSRqw8ig08WKxO8yX3GhEY5meoxM2nTTDfg0AWGRczQHDytiENNlz4pzI8yW1NY8_OuKoO79p7H29AWGw93tkkoFDvh0TiHw8K0v_gXL08E6q4j1tbeAINdUMRItzuhApETOplERsxa7mb_3arWeR_BvVGKQhX-8q6gck9OaL9rN8lA8De4NR-lSrsPi4O-uHmxhGpTUpt6m0FVKqR_R26YNi_7hiZgmLcxpAMBPKbjf8rNRJ3TiHrqlBIIuE_44H1XLj7mabcdgLT8KMYHBNc8D8P5RDAXhRHWncsrX0Jel2ExzqEGqxSPT67bS9Mlsnec36U7ejt0nH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=aeqaDjsROW32SmLZIWM7NsoNKhju20hc2E5rj7UBuEa482SkG8rIMPMwou5ap9kbJtnSNw9gyf5bH76SY8tlsXuR5j12Pjd-WpvOG2esHGJo3rKw61Y10ABY3iO6Tp24heDC6EazTz6iErN-8WDBLL-ftRB9ExwpNg7u_tdB3V8m9VdQHZcE05anB_IafV2wgH6P2npC-knnQTShx2AFXg9lH1M_DqroaR1x-XGSL-jQPJs6TUcSGpj2fbw0d9Lk1U6f5OShwUcRt0sBViSJsyNWJlF1h0V55XskQdrAhi0M_eB5ttG8GRvLK4hDmFPpHmUtV1ga7WHS0t2tEKOsZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=aeqaDjsROW32SmLZIWM7NsoNKhju20hc2E5rj7UBuEa482SkG8rIMPMwou5ap9kbJtnSNw9gyf5bH76SY8tlsXuR5j12Pjd-WpvOG2esHGJo3rKw61Y10ABY3iO6Tp24heDC6EazTz6iErN-8WDBLL-ftRB9ExwpNg7u_tdB3V8m9VdQHZcE05anB_IafV2wgH6P2npC-knnQTShx2AFXg9lH1M_DqroaR1x-XGSL-jQPJs6TUcSGpj2fbw0d9Lk1U6f5OShwUcRt0sBViSJsyNWJlF1h0V55XskQdrAhi0M_eB5ttG8GRvLK4hDmFPpHmUtV1ga7WHS0t2tEKOsZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnDX84vwDsso9q1WwkOy9hJR6rtASMFRFE1qvrupKSXC3oG0qypg8TUMPSCfVb7Q_FOrbihW1oP1NsRmFBprfsDN_mKo0aXy9nHyDnIxs_2r63F01gBt0pxc0TqWchlZTd0XNOZM9H98FLYD_u0gC5AOYLoDMFMskN6K21B4d02Cune4KtC9gbH0v3j_T_5JVnzvj-KWJnMJPBAp8UxSTpE09ycmXP_DGCjNry9fyCrZFZi-ZaMySjXlPbc_pilWqsdxUKMEjtpMyFRoD1JjsTQ-lYBfgiFGLUr4QLvw0F9qgHtatxomrQxy_Of4dHh22n5DMtVmxo70EYUklCdoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fimZGywaYBeVmJSYYxwDmS-5KVrbCc6NP8CuqR2QfdulsbPfgVE6PBaH0cYZJZwFFTZcT4Yb8SPnbsy4M-jzb7S1oXgQe2qwY3F1UIhtv4DN3-b3MNFQGb5wSoyeKlKIkTCNPFJwants2kClLnat37pGESdNShfPGwwnYbng0v9ZjsvwzFMX24MQ-MyHFMTXbWEyqSXvT40uM5Pp-RPWwGAo1WKCkQD_ePL22hqFoKFk-MEFpblao4QwZ8DScgUjLc2p6kPVsHHolZpEZNjh6NyVubXaG-XcgBfaaXE39S88mD0GuxcPxc6Aa56mGL8lwg_jLanjTkVk34mwFsORPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEJliDLH1HvAL7qxeiFxQ7BFE5BWw8l_UUVPuzbRSt0gn2xB4bmpDiXjDmkVo8yJooiZzEppk7jIwJX0ioXfgeCFoqCYG-GwG420j3WLHHfA_KRSM3wfRiTRRa9FwtyK7VylqrAQccj9b5xuYDaaF0BuBbuUv5LXgf_suGFHt_pEo8b_dxF5ZF3Htu9aq9AbMN8yyGZl65e078mVYQtjneltCWvHCdlVekLUV0Tvj6PBRpd5Vx4i4CgWmvIDWRV8cZqIhezVvIsLcbf6T6r11us4utfGAGhiP1O8nReA8uUFtUYqNYa6N3KpSPzKDHRKzk2mFmLU5jsOo0aWSM6I8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKH5hc4u9TlKxbvD1eQvDvPthO-uJkqogOCQV068kfu6N-rvX-G7YdCIV0UrokG0jQ93kPyRm3aka8LJcf_0jKSr8e1XDnnsco0ZavOUuTFTjIZhJWhhRB6e-L7G3q0JWyGa2m7OWXvVgsN3JYr0GVLcK__mILG7Eeyj4nSMyGDyDDAvO8F5JSlpInLZdirjyeTwwZgETI7nV81Olhv1DQ9IWoGBIkSb9F4KvyjDwCW2yMGXkCDHw2H7vadqRkR0C9EXkVCvFkwQEUZDl2jR_QMPGC1P32Ru7uxR-sHkkAu3PlB-tET4CjbkJVYhE_fwqd9Iqbe55QigcT7rCuln4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc2s4IvulcrwCZ4rL5BS91jUEdRRGWFFoHx9mXvQTUnSKPgSzxObX5DnuC_28DQVSg0eIJNKVApy_NFonXBy73RHngJ4g9TTQOt2q9yQOBeEClj8sLzTdS5P0uqxcj1s3xKovJ_b8iSz2zMdwH8HezLAC-Gx8dEsFwtfg_rtB1oozMLP9SzrVSscwuvGnVMNFs6BmydDd5PWkMFUPUrVC_3sLV5fDFHcw2snYsN0wmasUmSaoFLv-BPiRXj8wA2aTZzvlifjdMV7KoztLzU9yNamV94QDSKe4Tb_IyrN7KCWsbR2uCKppTTZpR0tNlmgPjht28vEW7LT5_n3zxzMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26529">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=dhj-bGVFD1D0K949pK34LbAi3GyiZmEZ6oyV7M0irBj6cVbWRILqrbaLN9Tzo6WjEE_DOItK6UCuDGhsJJyxv8QWyWRreOcbO7Feb9H_jrU7MERt6QMQBBxyQPzTtW6Q_3FtKMAqi_gUSlTa1k_ljCmhXO3e1eq5l33TAS03ZuVvXixpxBjT29mDxeJY8gETQLRxnnOL9c9WlZd-Ywzff6JRgqbX74Ls4omqvGackZE5U3OOnsw01qye1WAq_pQA7FBnYp0GXiHGAiA2TgEQ9o1LBRgBMeu8RZHSVCMPkk7ZEtr-r1opwxs_SpFKtQFIFSPFsLH2NNw0J4vygiyrEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84e71d5985.mp4?token=dhj-bGVFD1D0K949pK34LbAi3GyiZmEZ6oyV7M0irBj6cVbWRILqrbaLN9Tzo6WjEE_DOItK6UCuDGhsJJyxv8QWyWRreOcbO7Feb9H_jrU7MERt6QMQBBxyQPzTtW6Q_3FtKMAqi_gUSlTa1k_ljCmhXO3e1eq5l33TAS03ZuVvXixpxBjT29mDxeJY8gETQLRxnnOL9c9WlZd-Ywzff6JRgqbX74Ls4omqvGackZE5U3OOnsw01qye1WAq_pQA7FBnYp0GXiHGAiA2TgEQ9o1LBRgBMeu8RZHSVCMPkk7ZEtr-r1opwxs_SpFKtQFIFSPFsLH2NNw0J4vygiyrEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
ویدیویی نوستالژی و خاطره انگیز از تقابل جذاب نیمار نوجوان مقابل رونالدینیو در لیگ سری‌آ برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2k0d0u_8xnPsQtj8j5ymsTuPHdcxJbYqby_fqwwB7rYJj2GffnLK0RD1YzubzBuFAPOp2KS7CHFS9RaTQYOvvZIDLdsHSymBy8iT9EuswGJW3nQhZZvzTNSZqsm6nOn9syfz6FkntNM9ZQ1r8PDgyhPRcjuYmjuGM1GJ37LRR4PZ_m1-nFwVQZWGh0DqWdMYXhvCgCaVwLffLQccg797QkDUHyWyL6s8IkxJlDF_4B6_OZyIHhv91CZMSuC-bj38bf02wsF1o8Dc2ORtyc3wHQ6RO8cg2RoeHv0oJCmR_zLDSMPjG6t1wHhCKAS-KZ0on1JcrVAowmGCdiGYm3tkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOqeba4tFUYKau4GIucCJzHekW5FoTGWtg2Ou3MYR62OFAHs2MdrHG7OHSsAcyrNi9Y0vqu4-UJ2aFWH4B8oRWj_32Lp5O8xTaHiUHcmuLfs2ILu6VMjD41EIH7Oy8NB7DggrchQQWoma1x9poifxbxb4RRrDvWuHzHNYpXGPwf2OW7lCqGuSob9EKy8VnziDvyHKTVPF--wZmmnp4nUhifW-69VmEm5KEaDk7hGjh2POEnmrVVGIwYG_tziFXredH9LQHqrmKNlPUICfZORjcCWKm_MtPas5r57QH3uNu3GdlA1fUrjWB30CYwNopAz-w5EpdDBt16FNzSZP6Wklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKOVBV6YbHWadaZrSAXKTEssfcoxLXYEyPgY0HQf8jEmA5u8YoJIjDvtZZxZyd2x8Cdd-32Pp9gfLsUbVDhql9Fwegj3skUzV2aflLHWAmOgL6mRAr0bt3crmPjXf5h_G4b3-Bcql-FwIMvDbNDlJzPS36GEORX71IRjMqKLWIYUQ2HL84XAINr45iDmECmEfu4pZzuOdbUD1s6q9P6D-kdlQ0i_FwXM6tsdK2mD5EdePPx5M-cKuW8fXrHyS4z873lycJW__6rcQFq7yFQsM6aiywLaeMFomEcfBDlF4Q7vsWjhkt4qWlYdHCpgHmjv0u1bAWQqdRsZdZMzJrnydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAhonrla3S6IsDdn6s0og4f_45C_YC7Z7089Lq_p3abNZrSzNGQMmpVZVCiVLm6sPxdkP3MipxPFSgoto0D5wsKU8jJxRrTVFyxwu6C7o95rnhosjP5D1_EeENlIM6NVY5ZDBXYE5rh9H2B4EMhhU1Ubl9dWLYO9-g8Kv-12YO2OaApgbRz_07lkDOaHEElQxkZMYEON3tomxrVzXdT_FzDX3_Z_MIFUOrQj1hZkfRxez5rQanP9ef2ckXCb-UOIPg-DaB9oSjDBaXy1KaaYPap_7N01ABN3NCfot1M2oabds6fIBn7loZsoum-IvsKeZHWOiV1LfRf9ZX5ho3xY9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP1VToeLwrPtZSwUD14yI9Ooil0tiLxrc5yxdMP_KaOT1zNS3AukAmi3t-xbDfRVXHWvsf28GnJlhJl93FUx-Adguxlqi_8sJCG7NK8TlD-VHR7P9tXhu6HAIVZe1199udnAXFrAw0p90jlv0hZGNnuGVh6Uq9P7Qk557EaYTsVo9iVoSuCyfk9c6zSPFUgMhcUSAlh_TBC-nAQUp2ODRs0ybhBVnu5_37XNYyihtZo18VdPrL7i9ipU8R8cswKs0Xtu4g-ruKg4Uh4O2ssqecIKDQ8fw3Sb-01ckUy9QpdltZTdsbffC0dnnX41lT0vOrdx5rYvi5K4eipLJ-c1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYPanTD9XQFliC7UJZuqDYaT64FMwg0Fe3G02hFEX-rKKZdEpFxDnIf6ikI9brdKo0VQYCzqv1FxI35xFPxU61flGd_qpcMH5OBmcXmOtCWkNZP4dDZ2DaOYDz_2nb8DL_RmvEByhreLnLd5A83JCAQG51SpNanO5NFnXJ6VhyoknTLdxDyiZtLYUazA8B99AEXfEupGR-4ZDbojQGMo_VrQigRlFXooVtPgUirZ9I9SyXQWBvlhdit6OOgbQXG9CcZ2FNA6H-ioXQFfSXaGrcE7-iFhApBvs8oimS7QOovFD__9VhiX9xoKf_v4GUYVoT370abGtR1z9z1_7-PWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26521">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=leFzX670bFXjoMMLp0v0D2J_B6TytywjgnVFabvDEBZrwNHk2zNfOk9a0wYTqeDY2OyLUtyi_nrVcfxWQnXfZBskjyzcjZT3KCfyO52VD6zxbv1jxrwzMs1712O7HgJ0XdCxPdgtX1nYbElDPB13SB2E7jSMnHqfRcA1Hd_SsLGpoJMSyoSwOtX-iGeuXu-KD47ZG0IYhQYYrqFDfgwt-P16mUi9iPfjrDSL-RrlZHezrAKJmOMxY3BHRk6nTS9aXocEHSci82mT8KRLGwvGzVP7Tkk6oqFKmSUpgZGGVG6ANbKC4WaJFNl0PmI76V5fr6C7b52mtpX4lww4SEZbjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=leFzX670bFXjoMMLp0v0D2J_B6TytywjgnVFabvDEBZrwNHk2zNfOk9a0wYTqeDY2OyLUtyi_nrVcfxWQnXfZBskjyzcjZT3KCfyO52VD6zxbv1jxrwzMs1712O7HgJ0XdCxPdgtX1nYbElDPB13SB2E7jSMnHqfRcA1Hd_SsLGpoJMSyoSwOtX-iGeuXu-KD47ZG0IYhQYYrqFDfgwt-P16mUi9iPfjrDSL-RrlZHezrAKJmOMxY3BHRk6nTS9aXocEHSci82mT8KRLGwvGzVP7Tkk6oqFKmSUpgZGGVG6ANbKC4WaJFNl0PmI76V5fr6C7b52mtpX4lww4SEZbjzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvVM2QSpqTUYMGjwroGR7ac_EFsfrPpI3e3QRMq48wnuzBFY7sYfndYAot-KJ-cGzDqZi6eJnOkiuHzVAv2HBGVEdsGVOQWpF5slxh_KPBN-eeikOKeUumgHsPvOMMD-oWGHzaOf-nVelK2QLqp_QelYgLACQIb1WxRszRAyVd_43q50yySzbhgh2eNTDJMAKjuKHuDUtgbgWi5JYIYJb1TMiSSvxUBqbA-tCTou8iiS9hE4fFrLr2Qnx8eaOZItOct92OHxo4InCItG4VpCqydCQFqFN6FOqAeiRKWjOkYz1BCECXDe8he5qGZQ1Vku7Dt2eqzWB-rrgk9C39n1jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j32mWN7a9F2uI3CYbC3hWScIC_y-jKLUJwPYyjByhTei9JZsXQ9aIAON_-8Tvo2gguue8ZwO8gjLJ2qG1GCu0fKrq0nfKSGgq8z4IY4xnVSH--CZ8ZdmtFP_EAyhgdgMDHGGbctMZt-D3G9OGIYa1L_c5x8FKpQSpJqJ2Ci40LMVJMNDhQV4Fqyx_Mk5GkKo4-r5lZm9tEejUrUthyB1-ilxxn5_k9S65CI1PDZcd87JK8so078R5nnObKPaP955YoT7DKaDc8yasZwW92fEoplYKSq8mkO3X4dy_oy2yeBfy8wEOHMb2UwMG-kYQMQaFIJ6I6Xn7ARJnM7DjydpUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaUGJLvAQDSHLb_sR8bQRNRYcj8nGvhBM7zFNY1igy0PE1UYMbEIOPBWjkOp-3i6_N-g88JirCL787gO3hCMjjyg4LgTLqS-DQ4iL25E9MBDwScn6T4f0p2pPKxxJeiqtcsiSa16MRD4ZtEqkzTP6phBQx4OWpn55tXwwgcCUzgP2VSwAmjHcyexlKt-R1x12hpV4qvKtsLQD2KgbactT9er5g6mM6RdhPuAUZaboQQ9_Xuw-e5K9IZdLoH6ejxRrqimb6ZjcHTWPVvmx-i9_qXoDR8-ROeya-SCmuWBBznDFmhSZHhUgpEFWm2B7dASkTqYIfXpeqL1_iwbCWOwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5ryixxKZmCmg2fRkuEhl9PODMKifo6zUhPNUhc5rFuH7ej5gRSvpN2wEWPti6nnqnPSidGfihabdANSxC5F1AaqDNrHEoxDVgPkcTXTgv2ir4qmLzBoHN8_A6_10J6y6ax_dcfOgalnk_1a8wwuuCaN9Vq8-pHRvHVRLpAsGjRzI2LrEWOnehpbDUqenDy2OuQHmzR6yJ4qmU2Z4RobWvE4cfleEzZ_92H4tesMpGt64pPQsFTgfejhjnhdXtoMaOx024GpPcsjcu75xD4xlxYlzM9OBrO3ohcTeoBKLC0tNjWz6QtFOf_q_09evt7nf33L4DSBxnDyUEE7_NzKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0kIcPXXSoPtAC6jLXVwOl0oNpAZuFKiwNEjv9OtrhdHCeLl9OkWFAmqaDR0rjfIlN-lHUOM0apEdDcGhUfKxym4uw8GsBGzbAHtg-TxWhWhRgPqc5LK-vWtOyfoaQVwCwqPD-IvrPY-XOjkT2btbxKMkx5Zsis73dfkN_IAj_pM2_-UuNUiFyH5ebUGzqErT9hbjcXLyyjOKAQbDlz7P3wEYtJtDy43Kc6DEpZH_Ox2HB09aTEcwq6CtJZh_Jm-8NNxGVg75os-JDnYR79aNIsQgETVX7A1mmmBXIKzdtCSa4r7S3UB7RPqieK3nUxHkVsi3e8O528gZB-inXs2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toDtANMTcewoy1PaJDhakoI9aIcTYmSSALzBFXTHCPaRdsN7lUHgerZEytHgabXIxe1qhZ1hGecpE4HPCUL1zMsln2uingJOVHIiIsaQD_AzJxvxIDykYhC7wdC655POdAgqAmgILX8P-jZGPf-CRoPIWgrioBsjW5Y3bUgh0nf_WgTqDlg09C3aIhP9eczHM-MLInzaGLTRvazqfC9BGieRmVF14J0d33T1OddBBBQ2y9oClomyw7WrigWz2T48BIFB6tMX0RJ1rVGAAcOBTRKRSBot9wa4xlhxmMCez-ajmGQQDTeZIUno-B-Oc4t9zKVe96C6j7y_YNtHrSyiFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh995WZge_1aC_vAVUtZgJ6Ib4CQrhLsNbEYYkPZI7CQGtEvhhoPTiURNKjjzwSJBxOcXt-aqMZ58aUnyZ81nAx_uX1zb4Syc0wW6TLaGaGhUbw-cgUxazAIUKnfeGJTY9ol91T_Vdv1H4tAVzMqzI7_afvAcXQQXdzAU5F9sOMGlY6F94cFoqxhN6Rngb8Qp2w43iilR7k7X-nRaUSNou0oM55q83pRu-CR1HEgQNQRCgHxpZHyVWKEw0YtU6kF5cuck7aA8aeeLsLt59b3RLtbzLQAePURU4Bz84fqqi2ly2YLG9iwI0PAUYajY64t_VSJ-0RXELFBPWGsvYci6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiWE1GcFowb8rJGjBSEMb8MVdPZO6zlrz8-J89MCJNyeah87eZsFcdY0rdhHgheNrjfnFsGi2lFRHz7sSTjx_NBOisl89zzgK_7_i2Ln3RO56Rit-VRmN0i2X-lh0iHOs5C6q6qfllATEGD9xaTszKqG0G2d_yQioVjKWne4nYHa1QymWZeGhCSfLw5HMr0-bUeina1_bRFVIC3iSLDPRm6c8X9mwq8Hsy1gbtD4dwX3AiPE9madGGQSFvXLNsjv7Ru9bZ7ZZKraOHvj0GMJSEZHYmw4F73AUf9BvmJrSoF0vhsk-JIr_Zb2pd_YtScVuoZtSE4Oe5zwHCOvxD1ftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxjc9vv1FXB4dBXW3O7G4yDvpxjajCLTc5Om3lmTBwHt8G4jsKpgKU5pYwtG5Pb1e0d_mAcQPLAzj7Kxz0VIsJ9oQRwblTBDVktpDf9Lc1Ze3DFbUPB-sW-j6Lt5dYAdu_kSnpo-03O01ylKsTYk4SxbH5ugPyt9n3q7liCQjWwoeZXLJMM1GkiL0C-viMZs7rkFKEgIdP3foKfTDjGG5dT_IFavU_TPGWHEhe8bwXBwrbPQmvSg3a99b3g3Z7Jrkdf4K0NxDfr71rrHIi2xU8WRF00lVHi8we2rJejd1f1QdsIbgSRSYy_IJMZqfGFXO-dO0qwnnnGXcgKGntH3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJmcT2L1A8M5EjQHQxHoI3XoU6o74CECmrt9jwhAtka3Q-MygFhg3i4ZL_DWF_o2wZgFQAjUg1nhrMMgbx41cmQhSsObadgN0wYzj2bwLkv7DEYgkoQYGHzoc8FP5ZkX5idATRgfO1oIH8IIE9vFcKRSaHAGTmsRTpq-zENZBfTYZZ1NmJLJvA3eGoCmILzxVgIllwrTG8H_GJWZhj5RDTY9lkxwvwPW8MBmafxEUavDGcIdU52QgkWUHD5Z2o-JhJonymgLwwS8DoPCsthCVFdX8EeDNjM3-MIVoP2b-8nhm_egnAILPkqYbFSBUL1IKHduFQWv9oMnNw7w2fgeMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ou5fRl0Vhqi-Tj7yI19MTRnu23WZlcCDDxVhf9oKAWCjilrWNpOL7s5s36obz-8VIKnC8m73qmJFU1RZ4_sp2iWZnE3DprYoOZi_FNt4_PeoNCpqHgx_rjUnSc-eUZcPiCDs6nMzxK1sh0G_Aa_prx1rWQq-gDeg20k3foHBUCWNmHZ75PX4TjDkqcLnaIt-2fIFVjY-H00KPY07lvByETXOkqMerDH6cOTVm-g_9N3cVbQ2pXG61oRWobEKxncOy1QsVlZHeMR1enGNemi9jN7FyEFyh0qH-76kkoAtaeQvvDdMPKyJxVVnQ0_mqc4lrtmsTaJTO273-7h26ik5Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhKG2hn5MSVcj3EV5oCZZ6Sj_1sF3Ta9ZiwjbqlLkCIL-rL83SqJmDSK852D-nXspNK8crDodtzy2ldfhDlg3zIVtvdRCEuacRoupZwgmZQwW-FyUneDEK9FQyG-t4EuM64ckulaSn4qODVkEUR3Qd5XKru6ZkSTsQ_sQt8cB3ZyCk8aWIBamEa-RWWyF3Jr2o5JjdUbSmSOpgvpSa5x7p8Lq-xOWaofOnNq1UXXy_atmDq4jWUGL2s-grcvGcuTwpkZbRXnyvdqm5poX6UsluAnzEJzHy9xTtvGn2NKDiwClGUMjG46jsap5eAsOI8Po2P4JrxOR39pJVFNiUs_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DP19JW6Ao43vqYvn4pASanFWUB6iOYt5oeOmlFRycpDbYLkiUS3LRN7UEO0ug4rTgrgHvb5pgcPZbx5gaXPmuCQjI0rOgXvQstKozc3I00Eg5cldQPqdCTtOWOLzsh020ZYagFQ3vrY7sDYK7TBuEYbRuAsXOpSg-yRlc2uxZAX5QlxiStGq-r3mJeYw-sD5n7LqfOcY35ffc0FNa5fKjueCsn3Xm6L6wt1dZKOD3-cD8Mg4KaQnYrMCd4H-5OC_0dS0Lw8imtNOGSCa4X6D_G0XbHkIHq28AYhEd3ok2OCxC77wGAVvcf5h7DQYJTCAwK0UnRWfDBhF-L9HR7gp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqPJq9XY40vYxII8U97FUNn4SG31abjLwLvmkPSnojkSSVjuJhLDXHt0yxit9epyRFeypnY-evpPXp5RTZrn4uF7lhpMXRwUasIiNgVAX50ZKXurYpoUC1Vl8UOI0w196zIqwlmAy7JMhHcj5khX6u-wCQGt59xEqdXZ2iMr88-wmp1-WxwC04zpnYnL2Hyyqdc7W0nFSJGReBKVMhUWtcHo8xZcszWlNIDIEn68jCKU2SOLebsvNdX6YkoXv3n6glPx4tGWC7PE1tvVZ0vn28qUQSeJ-RB8rhLm6j0SCUyfL9TlJjeWi-PPkanHSDiMQV4LHxM-TuhfQpfUFHjv1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQfmB7-uXZjiaCPwUndf4Mi9SO-eRiC0jfWjarvpVSGdzadkhmrUmvK4xuTQ1gh7Kj-bFWQBVARuevQOUEYIqX9pUgwOwMlPrDCea0AthgG7LJ5ksnTYWzRueTU3pfYY1Fs75Ox6AOs9KgGDjxKsPH6GfdjY9SfaeKV81ZBrCOkwCqWc8ceJYEQNQFWXX8818ZLhtD228lQe9anUoJSDcrGKmMIVK8J-ol1QKe8Kvz79CT9yKA35BKGQaZtFvvjLlfNBGliHsEQzQUYsXeYMWx9mHBSwqCGlnIbXzMPXccBIlL-R03glXg2biknnjuq5afP_1E_P8YNJhl5l5_sKXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7WX1Tslnxs8jMuAZTJrdA638-1XCPUhRzhHlwTyB6QlfZ1r59QdNGjdrifY6ejeTC49aMpJ3ErLb0biUW-z7rrOJ8QzE8aE5VU_TdjMWBRdpDjNGQ9MxHu9KslOVl0hsS8vQUj5BQ7Hv1bFouV9P6o45IjGQEzrwKLOkGHub44tSN9G2n2U-oyMuxkLwdApZs_ZqUVB2ivFYT_v0KqvAd9WmWzruwSIC8XzRc7ni8W-Ys03lzTb8rUERwbKtBO1zHIneqaLz9Z7DWu4GvPvsOVvmWlpASYkTYRUCikrjl1k_Oc4z0AwatN9Yz9S-mihnJ9N65g1cniujAswfwXEaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMb1OTXRow6EYq_UTiQ7whuwsJxvY-kdWuj_PZFCleuns2oUyvlKLtMNF3lQ24H8K3rRLRyAEJQntFZGIIpQs0QZQNz5OL3KpTEXy5_6aZFI2JU2L9ZfSVq0sGsUUJDGZjvJKJk3l3aktptaddrOmnW3h7IYIeKtMgNAd1xcUZplK30mcMmI75cCHvwkmNX7QtA8KV4HLkNLcobBdMNYB8pH7YFTaPobjTIVZ-sWcN2Sjk8QIeySGjL7DiLZB7Cmpwu3_bV5PebdBZJv3NqSJufi5-Q_MpTOedHuOzgZQXvHBg8olAW29MSsG-06a-KyNQYov9FklQYJdYUmRro9mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=a5mVxlKsa1m1GXKOXfgFHa7o00UC1S0JWjpB8vT4vPD5QEk77iDbRMHPCFPAKbAXVUmXsNhpiHkoO-UPPS0h3fuoU3V3CSB7dZH5gzg7cnYSjIq7v6u2jXKoXbdSU-FuxFsfPJk_e0qupypasdrq8CkmfhXD0DSEHQ_M5XrHlr0K7CaUDogL-H_3BIW3EefyhQsYshWhPgysx9BJL1e4f2KgBKkhiDrLa-pwaMShkvCDVbXAuubufvmDagQ5N_b4RStdj_t9GLsISCOIQRZ31QUhWYh_iC9eZgpk8-DxS9pmdRAFRrEGDGp29cdDh4q8-9z71-xd3d1NBx3efGpsug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=a5mVxlKsa1m1GXKOXfgFHa7o00UC1S0JWjpB8vT4vPD5QEk77iDbRMHPCFPAKbAXVUmXsNhpiHkoO-UPPS0h3fuoU3V3CSB7dZH5gzg7cnYSjIq7v6u2jXKoXbdSU-FuxFsfPJk_e0qupypasdrq8CkmfhXD0DSEHQ_M5XrHlr0K7CaUDogL-H_3BIW3EefyhQsYshWhPgysx9BJL1e4f2KgBKkhiDrLa-pwaMShkvCDVbXAuubufvmDagQ5N_b4RStdj_t9GLsISCOIQRZ31QUhWYh_iC9eZgpk8-DxS9pmdRAFRrEGDGp29cdDh4q8-9z71-xd3d1NBx3efGpsug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnPcHiHEOyawbvhvJa-i0qFLniTOUlC1M-Ly1toPtwOX3aief5Ew3Quc2j2ZvnZIofsLBxPsX-vqM-cq7G9uP38WpIWt6XANzj8sVEOSHHbk7s91YaQCYqhWLUcsVBO7Lo1KRCfoyEYFD9G_Bo0yvA1lyirPl0nfnpXc-4-fv5qz77xXA5sYVlPqOV_mtUbYHpNsz4bLUn79jaXKEpx16xYGYFuuSQiA71ZfNZVjAYo3JMHuAHPKqz7xDIbCeZstXKHWkgDGtShxH2ooUNTQS1DMOYPkhSaPNXZ2SOzJaAX15xCrJjBY5IXj8rrc8WJdxcAjLdZCg5KO0f-G6Uyyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tz8t1Wo8glWQLsRvu7rOYnMjbllGdKoGr7b7nYKNj7Qxd3pAP2JIHbbUQiH8a3ho0l5Px_bfFDcXxB2CIOjtB35P6lfpaoFu6hxnwmdd9TIYzjLtq-uked_3NeGVXUA94TP2M6RLu-0cJKRxO1KfBvyuMrtEIFCpdeeWBHuJcUDpuLvL8cMw1gdGzRGyQhpal6E0zmpKc8R_pJXBZlzjQUhzxr9v364kaJQsvlUKjBKqNk2S-CyhVo-tDXz0cQYlyh7FO8TicfUUAw_k8fZxwx70jpHiIbpS8dzx_Wnxy_fQp43FOez7MeAtMXp56gHbQvzRLR-fWz3utiulQc-xJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNDNYcIXcdCAnHa527cgxZVzUczjRA86_9IIkrWab8NxaxjYPKxubb5mcypDjlYdy0lLeGFYiQgC8IMOxhMwMBVJHLobUzQpzIBqDobZfCjT5x3H4gjBYrWwQAISDNW8BcOO0ZQIiJzRe6Ou4zJixua_an5wmmhDM4Ec-TejcMCr2KFnL9Wc3r_WIm27DebHwbCDmsb1ZzlKtVsDeAkQPTZn1VPRZnAoBui7C3vZCg0l2JqbdNA_1CeemOIFsuxlaPYNNh4nRZEOoNkC5QJb18ybjR2wMp137ym5x-_aDz-RoNKRWLIPE9nSC37FAkjvecJHIiJP2tV7FVnmGHEAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26497">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=Mq6chxpiJ7Ck01aHD6CipqoNAmidOlewT5x7iAOz713sFBORnVOljyW9bvkBrGJWedAG4YwqEIKorSA_cLj3uzkcHe8rwZ1cUYQIxhtRpTYSVMWTJMG2nlB_-r22NkTR7VJW8CGZPmRph9A2y8FoOpGvqRQ9P-SGx0UgvHIy6jmKYsB-HwLD5trlN8V8kVuzdkGjU4mScxHcSmM-5nDsYkF_z89790U-kHVjit3mZYk8myK5VNSOpSONTU0i8Qh05BlCAHsOX3OPStRbdEwm_WGCVKMIqN0lJokLM8AZdKJGbgLWVBx9_3K9n2MvWgJrXE-rQ8sFTOrtM_gp4UeXdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=Mq6chxpiJ7Ck01aHD6CipqoNAmidOlewT5x7iAOz713sFBORnVOljyW9bvkBrGJWedAG4YwqEIKorSA_cLj3uzkcHe8rwZ1cUYQIxhtRpTYSVMWTJMG2nlB_-r22NkTR7VJW8CGZPmRph9A2y8FoOpGvqRQ9P-SGx0UgvHIy6jmKYsB-HwLD5trlN8V8kVuzdkGjU4mScxHcSmM-5nDsYkF_z89790U-kHVjit3mZYk8myK5VNSOpSONTU0i8Qh05BlCAHsOX3OPStRbdEwm_WGCVKMIqN0lJokLM8AZdKJGbgLWVBx9_3K9n2MvWgJrXE-rQ8sFTOrtM_gp4UeXdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام سانتی آئونا فردا باشگاه رئال مادرید انتقال یان دیومانده 19 ساله رو نهایی خواهد کرد و هفته اینده نیز به شکل رسمی از او رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2bqdAVuQZcUNhISyAx-PYSoQDcXrOcuvCpIuzmJtrEpoaY8gsN_B-VC-QsxuiNV7Uz87CyGq-y_XuyUo2mq3_jSY2ynqEqLc0LclrZWWV8p9oVqPI1bVnGEKiWkB-2uhnh_mIaMWJ7Aw5D5YCAB_-VUycs3aAP471_rxO0W-aDJYQwssj5ORrnXOfjig41rjxY-flhy4o48pHROwgbf1AObpv_DhYPSbWATin8NJQGXvpZNN4aRbwyHxXoXC38b3jkjqKiq4eKux9YJtmiDIyVB70yWRs-mpYpaVg1mhfLQwd-ou0lcRyKfoCJPA-KsHJiDo9Rpg5IhAf6nh5rZpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26495">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50d8219701.mp4?token=V7u_pGDtZT47JiFWnwhFU2u32tWQhX4C85-0tR2UYvllmGB7rlz2-mgxzRVyBJQOwvbyKX5zqXw8pgGvR-F3p7SKRbHxIcmQGEexPVi8Ug07hEfftYvkKRY048KzJsFaXTBHYWdPBCu7FrxVJzwtIOcTF595rwzUoSl-17mv4LDSM_Xse_hz2Ma0QWw6f2MjsXsLlzpjMWGn_vobdr3uApfzHRiJ2OYAwn5Zk5jLNMedsMpVQcD8iAVkX3Pv7LC0S8xaRcx6KxAgjbTpeYnhf3qh5xR6RZzxLnbLSH6VEiIkr8wFZG5fUAKqScDwqu2ubIP-NGhlDQ8juQSjhjIwRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50d8219701.mp4?token=V7u_pGDtZT47JiFWnwhFU2u32tWQhX4C85-0tR2UYvllmGB7rlz2-mgxzRVyBJQOwvbyKX5zqXw8pgGvR-F3p7SKRbHxIcmQGEexPVi8Ug07hEfftYvkKRY048KzJsFaXTBHYWdPBCu7FrxVJzwtIOcTF595rwzUoSl-17mv4LDSM_Xse_hz2Ma0QWw6f2MjsXsLlzpjMWGn_vobdr3uApfzHRiJ2OYAwn5Zk5jLNMedsMpVQcD8iAVkX3Pv7LC0S8xaRcx6KxAgjbTpeYnhf3qh5xR6RZzxLnbLSH6VEiIkr8wFZG5fUAKqScDwqu2ubIP-NGhlDQ8juQSjhjIwRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqdjdAHU2Smf8mE_Ei-6JpJBm5tTQgC2rBkVY9DPoa-_6RDIdzBXiueALoPkie8icCtLAG0_DVXh8172hYfdCIz8Vd92chYRhZ2tvHviHb_vBL_OvUaGRGnS23pCtG7ynKnP5HGlXJFrrzESFwft0ngg0nTXUWbj6Xva6iT7owmSjwnG2Yk5W9sU3TxtraFYHtj5PRX1yBOMn0jj0b4_zRWnzu-XUiu4GigSo9tOTu_2i6bJ3zxO9Pk8XKgsErxxo7flnV7QiQmlEyss0XMo-VDbB3YV3PNmlSLlMP8sbGEjZoz5CJ065eDDJ8hWkQIkXJ7HVXVy0W-jcn4E_zfZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utThEyFkBiFZz-HHS5JyFwlriyycNyK69QcAMEpz_sa5C5c7UzGvOAI6D_g357Heqvc2YIZpZkrUxN514xrN5yjUOZqXvZuT02AkkccuZr0E-VEJviLvmnYXpPdA4glweaovFrANjmMMv0xlN2RkaIo_jE_QGInZysOfATpL3XFQkVuZq9sz4vOSzI8_Q0wAKwY8V3sL_qoMEcqEiEuc1S1Cm1QXqakDp8VF05N0iWc2YXiF7UlcG_gE8xMC4xqmkzUBXV6Cykk-rrtVr0Dbf6rVCL7uFt8X6WHvGfKOiAxroUCH9c_G_VEAH-Qoy04Dn8pkx-HJxzN45ys7N_PlkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jyev_p51u6PJE5vNVg5PIiQKYJhNJ6amP3t-W6JROyg9961TUIb757fFNjhb5FRrLWGYu8L8c885_3e2d-QDNHNIxXCqDKvjKP-1qTQTy4pDV7cfc5P6NFSxL92PTxez06VsTzphuHxTRgaTySixVTyTd3sadBEhGU-QiTm2L7nm1W65QlZGHTgoi6vKgQ30t361zpU0iuySUSxlzdOD-lxSbBpSbiLLn-aX94g-5O1rVpUKFGnjNAvSt5ijZSd2Nc2R-5RpnP3AXVSKc4JLcXS5PPrV3ByoKLIvsRMcSSM0kPwNOR8UFsOYPWdoUS3s2dwIZSIukW0ggXfhtp60Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6T6S3jwVukCJfXNIzF_hKNAwdE1MQesMFMU__hNCmSLi7rmg1hoHFTZIwcR76LhAiaR3-mlh1unk7i7YZf1m3Geo7L0-EDdHshbm0nmczhvjqtHVSiBgkQks9RMviUtSezRBehVk__AqIATtfm7vUuF5xzxjXGdw7JATUM3DGt79RKg43BuqEA6i9WETZsENzWqSGqDriYHkCHNZZE1ysByNLyQntzKqmaBYB9xfGTFfrLhcu9objN8EbM1vqJELYEvBMJEvseyEyroDIbRCIrwN9bOI6pQdJ2yK1gtL1ZXZTXv2mAvWnUSkDrEsZUhoZKJfAeVHjmK90C7edfEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUSjGUevlybB1s9U7hW0csx3aOlZC1nFuYd_MQJXcMQtV2MVgFqRaV6xvYHga54zTPX2GoY6FBNsW1dLs0VJ7a9Y2UPljYbyqymx9mEfPXsLZUExvz7PaXAuAPQ-OihXIggWlzRxqcF7dGCltTClgvoj8hnOZLLLL_wr9R3i_XZANIDwWNQhD-N3pOLNeLuC-18cqp9u2JF9HDVxsLWzs9qsZwUgtyeLMbYQvAnctgW0w_WmkTSfl_mYBothCuurdMhBLnGGKnyC9wgLAL9bljbPZzyhuSg5GXRK7uKBwSrr4Zc3WYQ7GnyU8_alhZeOEWRcggQp5OqJDvghCKck0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXOgP6eumtNOhOgiCkcJUJhbPLWzEVaSWzqQZALhXJPz57kNjWh4RC46AZG1l98wpl9H83AtokxmJZTFTSKV-Q7QF0jKDzZ_lJJBGZIW4d7gNfNKLqv7xa19pvE3ht8a5_tPFSxDtlOKWJkaOiJXsh68-SDlfZXu6dG6wtl1A8JtXFc_ymA1TZKn2iq1Y8r2ScGEwaepDHM6-cEJIwrq-d-KGBtP_Y1ra2cEMktOvxkgv0IWaOCEPn9Hy_qZphwOTRjvE_JIc_bp1_y2feGvnkzOmC9LcKv_HARJ1RnVJs9CL1PDd5Nt0vd1DxT01dFFWt1qZ5sogTvOopyOcrcMeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwaPhsrr_zDhqA8H4uaCfO1q4E_LAgnhEXLuQ5tKuHsF1p9jPnCBXQIsSo7NgACUQrbqBGXPpHVleF9hEbGACnbi4VmdtXbhItPiiWlb55Uj9NUH5kX4MgthIF9_yqllKzPZnzIRRk8Ejr92fS8sJQ2bwUtW7ZintJanP2GSn--FqCc3cVEZ7q7Vxo_eUG2Losfg4ILvu_gH4WI0oqYb6jFjQWSRXerMxVm6zlqq32h9FIDN817GH3TB3kQ8WBBoGq5G4LUEouJdI0rCRE9A2M96wQmH7DZznR8lFomeP8btbW6bdesUaxCpxyuYvE1mNyyXMNFFJ__epHzak52oxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26485">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHPDSuwmXS6wQTL0HBCurcjTHArP3Pa5NfRTe9ZmTaEy2irZeCVCHKhw_Jacpd8sAgjAjQCKgwnAX0yDT1Z_BIZvq2lSEx75yemb12npt30BjKh0yvpGhllF595K052mrV4n59pFbyiZoQwi2jdUwBG00BX4IcTes1tcgh6nG8sdN7aS7zPydC67IjbX9tNM0c0g256jBdkOXf2yO1FAAc6AQNfwzOF0-vR1rrG-no2XPdw1CeqYBEarzEkn2OByJm_m94igQsFv402macOlLkQx7RGLkm1QzSU3s2N99Yhw7wA58foKCyBu9mA4LuDJ4I62MK_eHzJEawN-iYilCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚪️
🇨🇮
بعد از علاقه یان دیومانده به پیوستن به رئال مادرید و مثبت‌پیش‌رفتن مذاکرات بین طرفین؛ باشگاه‌پاریسن‌ژرمن از خرید این فوق ستاره پیشمون شد. بزودی کارهای‌انتقال‌رسمی دیومانده 19 ساله به برنابئو توسط مدیریت رئالی ها انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=rFFtxM4Azj789i3-Pcp_b5k3so6PH94oj6roJ96fo8UN13WBskO9uVnANBUdeChqskiD6IvPzG3tuBlwoUyzwb_LTg0hS6ufThcgQmwcZVpcwMjUxGOs4x-edXOVOzLGtLEE_D_odVySh67yatLMbMEb7nu2QWpac52PWlTgoqcRb9WTds0XcJGpGd6hnnvqV18CkWD4-hRd-dh4LgzomyidDLXq8_Ej25NJuyouLNAvWfk7xpR997PYBFZ4O1UhrulFhnpKkT61LJ-Qvfg7W06s9ia8en45sLhnnaWnKomlfW55l_mH7yY5xWGP4PHktGXTjbBx1pEG5P_Qva-yIVWlgETBPHOK25Rhb5czLuTDF_HUbvEhz8VnwEpVIsswU4xVmLaaQnB1_LeDjDcLUcEWxyPDcoy8DsCCSDRrsi2xqv1tvvxCcxol7pZ3jwTKXHdKFaMsxkhDKKEKr_EnM4RVLsL7rSz8EJErKsDze4bC7yW84n3Ncy163UZmc2gRtbjRcueELFXlOyFdDHwftK9WMdxZuua-30uiz9D7R5NNLAc5--VYM9NWufiWrzEyJxCxu9zTiHrlD9GA_3aEP7bAFME2Jxds_hZwkn9-xbTc52EsNqOpGsBlrES0m7CpGa3euo_2DNdzarHOzYGXaPMz2lhQndHMP085lAZXg4U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=rFFtxM4Azj789i3-Pcp_b5k3so6PH94oj6roJ96fo8UN13WBskO9uVnANBUdeChqskiD6IvPzG3tuBlwoUyzwb_LTg0hS6ufThcgQmwcZVpcwMjUxGOs4x-edXOVOzLGtLEE_D_odVySh67yatLMbMEb7nu2QWpac52PWlTgoqcRb9WTds0XcJGpGd6hnnvqV18CkWD4-hRd-dh4LgzomyidDLXq8_Ej25NJuyouLNAvWfk7xpR997PYBFZ4O1UhrulFhnpKkT61LJ-Qvfg7W06s9ia8en45sLhnnaWnKomlfW55l_mH7yY5xWGP4PHktGXTjbBx1pEG5P_Qva-yIVWlgETBPHOK25Rhb5czLuTDF_HUbvEhz8VnwEpVIsswU4xVmLaaQnB1_LeDjDcLUcEWxyPDcoy8DsCCSDRrsi2xqv1tvvxCcxol7pZ3jwTKXHdKFaMsxkhDKKEKr_EnM4RVLsL7rSz8EJErKsDze4bC7yW84n3Ncy163UZmc2gRtbjRcueELFXlOyFdDHwftK9WMdxZuua-30uiz9D7R5NNLAc5--VYM9NWufiWrzEyJxCxu9zTiHrlD9GA_3aEP7bAFME2Jxds_hZwkn9-xbTc52EsNqOpGsBlrES0m7CpGa3euo_2DNdzarHOzYGXaPMz2lhQndHMP085lAZXg4U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ43hr8sU0VqGaI0n_lBdfBolvq0tuCP5tO3vw0OUCX4Hj8v9E2BnmykS1gQVfdWhAEp8vf-UqlHLte70NYrU7vdOQ1869n4qX2KmAGmKZuPCMWmtPXcFHpduXsYj0pyjWIW7vsssaO6PjuLiZ9AgYR9RxrmihhqME8o8z6C1C8TRKEfNCZjwBtoClRDK2A69SnN71TmsnEmlgRQhTwtYNzfppQBNqS1TPpgU1FcIGg04nnO_OJbSr5wSogagPxCUQU-lwZEsCSLWPLXnPUUXRF374GuoFRNyz6WwcRbTsmBqEzAs1l0gxOC8iw4pvTFwaNbeEaj7AVe5EZsiinNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDsovhLzM3Vvk6Gm9KYiwHQ2s0aPkFliRiFj8oHzVXp9jTjLZMiNYI1x_h9JCYjuIiuVb3YOcWg9LEtRvmBXzqVmfHs_ypm088YC0pn6M6eK7q2-mKxMplC6paWsD3el02a1YnNygmOicq4Vy1G300zHJ9RXIYHtJN4dfv83_SqUP4gl6RjGKiCF7CDbCN22K5u0nPfqDxAMzg2x-_FTmkXsA0arfiHY8yXtUZeACuqTJ0yY6RrI85hFjVASswbGzG65Ni6oOfOOlwzXDsd-iWEhR0InMNsA76T-lHcYV0mPs56bFnZEz8_6oF2qDh3r4pucFDqvb7DO9rwORTXJqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olGmhnoHl8mQAzlk6ITc3KGGVkuc4X5CX7BQwAXUDd7OOWJVBuiTxPJ927Rem-9RuCg_dWOJLZaFFnZrRHA0F9bk13vJHRRW2OrUQxkgHlnzmFXJQDXoQyBxzl0rCGuCM3TsY3Uodp1hmi8NBfHHSH1oWvctM45fUf5K-5rfV7hVoYWffLr4x0nj7-YARJginwYR4pDazdpB9hYhVtbl13vSCCAD-LhA0S3e3LRKzbolhUqns3qveQH2Tr_3YC1rzSpc4TGPgxRQWAqlVQgl_UdwdLBzvzbmJUp6lxf7_z8vR2zV8jp2489OyW787Wdxd_mNJkJFedJG56I_fxRn_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzSSlnRR2SZIR5U_uWEgGe--0dxkri6CiDZ8QWNdHoqcpPCIxlis-yRl-P694WDMIwgrx5CDBoHT2wt_GeNa47KUfKnR0xSV9SfFEMfQn7kI0Hg1DOXZGbISpzZQAbYRnyI4MlBqXZPfXXp62ITVPJZAySBbcpo_4gZ4n_7ZcJbAI22aQlF5JGBHzSzan10fj8acID5yGz3Gf_ICzeYs3JW7Lsu1nrQZF8uKfbalo79tEcfu_9YoLV_BolW_la8UhNmSJlclOFw6la1G8XpQaxQtLgMA8dQc9yEqAwhn6pHF3FIer57mAs46PyC39H9aUHBWg5fZ1b0Au0zIn8xVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNC8vtjDkz0nBeoCsMdG6cDO-NvWfJfXMrJSpgohTh_vllV05isrCQcB01oQ2zk69B-wagMLiPJgw5iThG6b_AP2HGUBTKPV8wYPh-5XSiWZ0yNLeeyQmZZUgA3tyNUrjE2yb2CAn06JTcG_DdspluF0oBbuvT1A7Nnb6sgpDJuxBdoZN_WDqv3Gqses2y0rVIrjyletVQKKdxpiaR9L94d1TcX6PasH8-NyRSS-QQinedFJuQX-cc5o8FjncW2p7hq09XFBr91fZQNd84DXqQ4VaHaS3jMdqmiZDKuuaqOI5KI8_c__PC7wEPZmW4ZPEAAI7_ghrQMAkAvM2Efwcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzOIXm6DGIajiWHNA9c4NqlO_NhAODWU7EskgWC7rFkS6mnHV3NgxWZVS5DgsqGCQsiKypj5q4fUs1Lcjz0q_shByOLDNPwGaGGCvkBCdoCJDtMng8c8b589XmKPX502ODpI3b6wWWhxpVSyc31c1gVRye7XXO-jGWUrsQaxHT5cLGa-OGh_uQvDmPy5IwwhF4e-CTorgPv2Uj99g2IdHjfhJnO1uV5Q6Ew16H8oX7OvEXEOS_aO6PC2GdZUzQSiZVfwZhCEx7SM9dJJlbfVQ2-3QF49TCZexFMgT2ysvZMImOOYrqQc1bRmeHeJLJlggArJwYfxVtIQVAKb5kypRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26475">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=R6Mauuumuzd3BdGB-OsuuQ7RpEmmd9JuU7P1RDxyTlA1zIN66IGdyGdqKxSTkmv8kHYQiDbXgu56Njqy-S15ofAUgeQf8itjz2BALlPT6dx3mSLFZ4kR7AaITHCNvF3QgBMupqFygIoI_RIsL8R7_F4BsQF5sH3wYim524-eXEZRIUEe6loTokHPLICHjDnb-h8LxdtNvq5DX-qRLqcoO_TWjceacCVTPbH9h4VPZuBm6xS5W8R06pFcw39tT4avb9OHMksm2FplTHnGqfBWZgWZ_enU5WUa_hl2MIJ8Nq70tyXcVteT5im5mDalb5NP6NP9OMQR22zBG96xvgmsDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=R6Mauuumuzd3BdGB-OsuuQ7RpEmmd9JuU7P1RDxyTlA1zIN66IGdyGdqKxSTkmv8kHYQiDbXgu56Njqy-S15ofAUgeQf8itjz2BALlPT6dx3mSLFZ4kR7AaITHCNvF3QgBMupqFygIoI_RIsL8R7_F4BsQF5sH3wYim524-eXEZRIUEe6loTokHPLICHjDnb-h8LxdtNvq5DX-qRLqcoO_TWjceacCVTPbH9h4VPZuBm6xS5W8R06pFcw39tT4avb9OHMksm2FplTHnGqfBWZgWZ_enU5WUa_hl2MIJ8Nq70tyXcVteT5im5mDalb5NP6NP9OMQR22zBG96xvgmsDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cD1gERdS0A6iZC9WtpBU1qoRg6MqSUJlHamLrieSd2cK7BvTG0aD_JwrikoWN8Wls1gqqwgJgS_WaKYz0iiF12WbcFiQ4jgX83rYa5vuJL8ByKOC3Ab_MiXxawk-Kj5O7wI-yOl9eHEmiUWAF2x4YlXrvX9WtJNqMgCCKnEHCnhy6wPEtC6GkPYmgpezDEbwuw2tlwneLL0_Hz-Kt8vALn42_E8Fu0UVNBWabUdxMjFzhjNSOvdTDG-2U1LYjjP0-wd9jtcqYNH697llyX9Xo7QDfCoZ9l_K-cscYlPesvpgh-75N6n6rxJKMLniJ1U5mIjNWtv0m8gAKr-_0l0BYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7TN4N9ZyfZTEyfhGaBkLJZK7_YzmBM4_43DX8swDRGjhodW1VrIhytpC75f49xU1fVe0eIysSdYd5JBgx7zMExof-_9GvOtkqaopxCJPxnv_uOc91wc9vP2DGrUyJ7RQSm7z-PyvtqIYKX1TkTmp4EfX3rwRGkcduxgyZ53cZ3UnmJoapNUMA3oZ-jlfyfW0v2w8MSGFjcyjrj7_tpX9qjTaG0MIh1r8FOWssxG7QfuktUpzqatEMQYLiozl8Ehd7e60Fm_kOhBdl9yLTaZsml6rS3LGpOJni70Vf_ppjgHTK06DDpnPDbiFbgh7v2JU49PZCuYyFelemzWTgXq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPrpZdgyXsYgE2s_C_xwTgqCFCuL6Ghu3I18_iKeuF2wyp9u2r5yaCWUeaRWbxmJ-MkEgqmBzBOER1T3bt9kq0Fx7Qv6LI1qeKoEt2rLpEqOeGJoejj0FBAgmCisxXqwLZBKeNm-caSicP2ObTY3ms4X4OJeRmWQ2BikR-VYJ-iARNytw_kZVF9bJnuGgXXTt33cl8C1ZwfhfL-spIzRtByNmD6hf6Hm8t-uwJWF4-zzoDuBN9mcX6Cu4Xb3sta2TUls8UcP2nehjko6JoEZhRXE5qGIhHm0j9Ro7rGG-GUwNfQzOPbGgXZe3Bxeqpc3ubrxH7BxRqeNsYEqVgsf0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
