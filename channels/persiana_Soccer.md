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
<p>@persiana_Soccer • 👥 602K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 08:33:32</div>
<hr>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCD0Xd8yhvxTAPvNwu4IZC_NmDEvmxSq8ecCdw7kEujYODtaeQ6zMRKygbQYIhu2L5i4lBjwe_85J4mv8pWR4W4w0emT1g-IzmWRjG0Oydua_OjYRzmtc0kQFPjCJgP7AVH2ITEz3s7gfE4327NgBapAvNecLSPq_u06iAK3nNz_eH8twTxzZ59RKh42baknxThyNvhcBBxrd3NgZJcnUie2RCsR7nTqfGryqg02SDpOkS5hJ5DkIoZAuMI0xTGn6WxL_1R06p0HEPFav4_IQYHpylbRr2d61dSgJsGS1C50USA6VWlYRG83rTR0UojSy70pN2ScArlE7wJRttmd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y84w1ypiH9bDgdGr7nZLa-5QoVo1kgfEyU5k5N5f_GpHy7bQNYwK9rN6fEqntxM6hiiljGgCDI3DD0z621_pPuAts4Bbz4oCPMVXjmnBSE8i_yi9rGtKXsCmlycZO3x67Xa9sz5DzheFQ_7EFPbQrNjbvc9ewL6bIs6EMNVdpI_fAK6k7qac81ARyE7VWClND53cjCGbTantTkfZolS0IO365PJzE1Rq1PunJPVXTBY6Ml2Ol5oa2v7ZCrPsC66jl06psS_TBo1lteixQNOg3b-4TKB93q6FrAZ5tWeoceoNNK4i_6EMvCtW9Y5CbRDxTSEkwYmNQOlZoN2Ah8v54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1tNPGw1lFqIqi4dHtxAVhY7hGhq5o2f-ZjkEJKsskvX27yjIt1uTAorD9GrMJhXE4BcNSZWbE-0kE6shLHBmiN-VIDsKQSBfMQZlAi9X894gYuu_lyMmBt2vP9np5cOcF17IGJ2iLPejdX_hqZix6m_OeE9Mxle52Z6pCEGjroYQG--DGiLU4aQrhG2fqDw4i0SiIRFhgO7KiRQfX3ckfVHUveExxo0SD0CS6xz7iBLGRNCYLhawTJdQIANLeGIDW1GKYwBAB5_uyf8o-1VYnT4NhcFXuvjOJDYBbiJwEiDHSpV9K-k33zfkmYaM15RZOqJuHUt654o-T0A_aUFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cThRrhtJfJZcDg6P-4T7xXjJHacK2GHjDP1XIWT_qmj4ejfpZch2hdhTjrN9E2_mw0rrEBTYmdOLZqLrPcgpTR_0_Zs2bAKg3LLQvZBJcE0FbVej2bjQnPQMQrkwS3qNKikbjZ8vZSKCA0-o3q19C6VGbPssnCxtatDoLT8M7IFNnVKO8y3T6SHjJ9-_5lyeY8UkyE-gDGY1PIXRguqDm7boiQHHUNlHgbdU7i8EygZq6jMNHuAKKsTI_mnu48DOd8DXQ0a8U0ZqFptbJtQBhNzh6pNxdkBzU_XqdR0vBIMFK2FUkma9iUGKNrCPDT_J58qPu8FKUg4aynQwlybEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/26580" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WERtbrd2RhFf6A9sDJHL0voPuVgtHSu1fCOM_q4174IqZI6M3rb-xlMJJUFybN1g1Ac82EvnOVSeS0zUnAWSzHvfgPigQLkwWctvRgqAF_LNzmEzGQnx2jMh_Upr1fcd5dajTS8cUrvgFZkNrxfg9H1_0pL3Xz0U1YubBMlWrXrO3Dhc5l-HX986hKogcyAMFe0utaRyRnh8FXf_EfoeXmQi6aWiKBmK2G31PH8yFdanze--01qdxXGcBrCs090PLDRCM6kDiW3MOUcVjqSuXZY1TdW4yu9nZ-zFxKGAMI7cLa6Jt0gv80pn6YN4GdMLeIGbKreORO_pawwloZbZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdD4-cWDITfS-FRe-AtfjsfEf5SVqxOOHGksCn7BGz6p-OQ-724LmOL7k07BrVnomp2LpGfE-yqOoPJZw_biIxFAS47uyNyr1a74_zX8urtHxdvzMxGdw7O8Z7TNrZ_pQE2Pbf7hALqFWoupl6k42jPXw-Pt4UqjptTK0PtndnA0AgngAwHc2pmJjtrTArHtGYRjiB9RYiV52DtdFWWKRyqlWM4__X8taDR0y1OqIyAqX9evsGwCdDprCIutU02WQ7F7y-f3dzRyTA2vrcDsT8bWNDo8GuSdOKtV04J9yr1w0qczOO4xAiT3ZRpIfQk-JI8tAQ_ovp4RrkhMxBzJKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26577">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKwevw1H-CkknGUWOqtfn-aQ5bT5s6fllVvhFAN11d0hzENx83OqTpTEmoa40E6X83oOdV9XkmjyN0Yp1Jqvxa5C000CMcfUkdd1ia3f9hzVOHf5FzyQGQ9w-LrGw4nsqSCzlDbiaxiob7sEfet6lZSUUCr9FFmWB1RByZIZXj3mt7F1w7lknkfEkAKRiL7_tfm3EzSSTtW38pAZtY-xgC2U7tqC1xV2E-93WgjVIGInI_nm0Ejgg3B3QVMvmhnVZfF0jFrZnKdWgED7Bs0rxTGIk0hmsP2aDS45836xE4AGuAdSk7ealfReHPcUn5IZasZjjqpUMvYc233D36d0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇮🇷
محمد قربانی ستاره ایرانی الوحده امارات: رقم‌رضایت‌نامه‌من 2 میلیون‌دلار تعیین شده. تا جایی که اطلاع‌دارم 3 باشگاه لیگ برتری به دنبال جذب من هستند. خودم‌علاقه دارم‌جایی‌برم‌که فرصت بازی بهم برسه. تکلیفم ظرف یک هفته اینده مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/26577" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn5rHbb2iDJYtqEZsWL1Wi24oFbVUXj8w6pNjwpZaTUmnMCn0kZD9U7LDolPVgLL2r3MFkRRUQnD-pCij89W-4Mclktzq9O3hD-o8vU4fvcLnFryF_uoy9DTNd1jjTwT_utquwlNBUIfoBrTXGBBfCG9M6Ld0euvGnAGcjaW2FgzpFFK4B-tg-IinjkCztwIlyUSoJ5rUguP4XRyZJ4Dg86ccaGL0kaHK-J2b62qwQRYhzahYGcazQe6ajQ8bFRbVrabB1fzXP8BFUxBgr9oOnW0K2pdTLLm-0UNgUwnMwo7nzGeH2V2GrHc84LMp6jLaEyIl-yPfRPppR7aKe-rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhEHM7pxoBmg-k8u12Uxo3Uimsw-86XV_ZBKTriqzD14H-Z1vt55PT__RPpjIyYXcsc15ZUx2Ce185hoCo-yr8ThoK-Qnm0NGUbabarr6ycE_EwjsN1OlLRJGSCxGELOS9C2jKViheBO_bRkLl_MN3xEn1kXENngDC1xMCJw0rPVQC_aDi4kH2Oz3P8VOx10Bngo1xHVBaAhWzNelNTGFQmbRJ8Sm0fqMxUmZpETsX9PpQ4e7sOrq93DmodUT70dv5LN9Wtlg_Anf4voGF3rW1P5F81HtqkpAbjrNMLLG6qBosYBXVVWSxetknqTOCTKe1zPsJXexotglNCGOfQdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgcfWqFQGCeTroBY2gUDtGkBWlJI0hQgOoZwfGRLRpAMbaFsVSrvrdXaboRJTLimRutZLpAm43RFcmdX6kjWrcRRUtkjJtHJUnPv0fVupZ1RrTyu6sDXeg5Ey2FaZefNaUS638OKiFmfP6syWuWinxtAOGvy2uyiPK35bgllymWONJniperCCQQYxE8UkUlpJGUr6MOi_sBQm57Qso6O31NoD0p-I8REbxlSxTHImuL-wFTuOwylZBRqKl0XblJLy5U2Eb4ohuMLdM_eL2mCX_R-ItRS39HTr6VlO7ggFkGJ7Foe-ybvqNyJkXFr8J04IbqQTu_JTGrMgzzwvkxQtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMpThjY06ZQsizDoIW9lshH_4VfpygY7tJMqgUs21hZ5HQpRfIqEcod8fMlZQXgMhWBj0aGgiNfEGuJTGS19ZyR87hWmTPzpurxkU-6ycxdShA2bhRh2A-5ReJ-vKLDoOHR9_z3sNH3mlWtfVvdYXxbcp3H8RAxUCcfNB5_lr0cXUQ4gP0MsPFXG2mMhjCWCtIU9oJqy5Gk7JUqSm9SnLDlTbOzEkK7AwpUeH2lTa6N9sswNI7yfAtmFElJme6Oxr7sKCd1JKPgayKSyPESwX4RGbH5HBQNvMow4DCImMjJSsbK1ifmgA-AIjpOEnCibHOKsUUP-rlbdQXFR2YPy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGc7AFT-iMdMsBazX232IouRdsNmL1eWG2X4yEMcXky3gB93wQPpCO6K2Dm0UwJ57RZYKgnHv0Fs2s7IDI0JAhiF3cORjhwyLx2m9dvH7sBKsdKHmFKKZiSMUs0n3MOvEAD2yva1-NIHqOxBDUvbUCUP_VGCVtur0HmMcdfNE5Zqc5MC0N3Hx5Z-6H7ne1qi5JVB4wa1glqSP-2oeNzpw3qa4BdKoSpnNNi0RE8W2F_NspKm7EaSCoZWpuv148qNI1lQ4hhAXJIHkLUHafTV9Z_1xxlpVSl7A3qIdgA35XTT0ZK91qC7YrVHtJl91Deuw8b8Nw-eYEKrsuaYiy-d-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFp6xTPwwDo9OQXlMymoCM0vT_d6hs-e8KHXXvZua4wG2X4s_lUizT1IJJTm0KZcFBUSw-4YLvlFTzgzSFKzpyrhYU8E3XjWIPMoYo6RS7hBwZGyIFYbwulC4p2RpqWkU6Xu1SZzt70KA8LbNVI0xSUvM03JUM5cJ2Om9GGo8f0Lx5BVhkObNQhxwN0PzuW58KFa8lfNhqXzRINczBDgGw7Gosrdh4Ld3pKs-rRESHKa6r1neOo2SPdTXsJv_VFqT3iQCk8UKd-tebAa1OMMeksqkHjzhdgdrVVwIO76dDmBfLX4UD7FaoFWIoQMcoHhumZ1CJR_o5CEmDmyy3_-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDZFyFhLC7ZMyUfwXZl-QJhJTcgoz4tOGdOJX7WmAiLYSbzbr38eu96yRNvy6gWqyBA50VEKNp0Aa3SWkNZniohhqDUXIlXdk9H4VWvC0qJtX2nBms7qZCEwj76CiWfHwG-wuFIBvWLlg7I7QX-PI99rBFw0AvPj2RB106pPzVmExqp2euCmegUEJFuYLL5SuqyU31Puia22kk-ldPolwMvQWUoJMdEGTgslrkJaT6XNb63CMPL7vGLFZ7MZJ5p0tZvSfAep3Lt-lmu2X1O2_vTqlIHjrYRoW2MZJuKe3R5_MJy768hoScUGjrHUhHQFvvKE85IZgIut_yKbFzhHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKfARVaPzLqcYz9YwjHm-qpyiFyFp1xAenj9ZCscACUM2ua3AzGSu4IICvf002d5KhI3fmuZFrICbazASxLeREznPqvhEw50acdGRQYiADwAhjFxpDMgLEOId_c5MbExDoMQeMUBIu46Pa7FeUBUmtBPNDTxHsMoDoGB1wtwKHkLWVByHab_eXTgzsXVYGvxUjBQmkdt0kAPwdTVh0ytyHLEgBz-9xCqdOrX56RCDC-6WSKEHKaZ24VSIyYNR617ileSH2enPh9ir6eqe_7n1Mqw1xJ9kbgtVZtPNMreOawtiLvPpRbpqQlxdqlZlv6yEAmwvBWrixHhtTfUx-GVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xhues1riFAtnITQlE0XVG_46o7jYLPUbzrXJv_Ya1K5vX3VWI8LPLznrQRlvDVrTgYk3sPv3Zu6_PiIa8LRMcjebhlBUQAtcxTk9a6xgarpTohTEFbCd08lZ59rrxhRHmrzOONg8fjs6CGjvF-M4JLihnlyoNrrKDbhC-cGfFCQPaSC6pkkfgot9G4IEJPtb654UCeoquP7XfXgYJxcakYjGt7DW1-WoY8QrRAwTGXvcG-1oO7rU8gOug5d2G_--laozCV-55tkYrSgzi417mo3OR57OulFdmhubXpHLXVeKewis0U5NuVtubIMtK5PQBdilPbs50U_-fqBTFYtUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEuAfOg5MKzv7QalYRtzyNc16V1xiCHo-8ApO3E8EoFO5Tvz3ug6qnpxnb0--cVv2khd2BSxNTpK86IOhMRBDxDHwAJOmJPt4Py8JKMzx5gGjcKTyYpa5CPhx7P8Tb_D0IrYql7Vb-EzcCDTZlMI7caF_wNC414IkTurV0HxFPlFn1_3ZTvtjmitzIPdBJcClnmKfEHqVrfloEfRQFJ2vv_VVZi052jJnNjXmRU43Aons35OJ7zMwIOn0Cg8QWO1-ngnAobwhy5ZE2D3HODVQnNIyFQrRLqGr0VOYDknI55yuzS_gWrUpW0OBo2xa_BNeu9zwpsxAsKrolF-xXEXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTQIBySLtKGt6iYDGMBqG3dYTpkwP7fqrpE1rYHbeM-cSsM50X7SwCxAJgyRkOCO-olCWLZw40PPIakRqbpEWv7YBveMwk1WIjGp6neEn1KzFR8epgqTmQmJxSpLzDOqFrRGwOiOcyPn_WOmlZcV-GZP2p5zGR8imAevoWckxe2narAogfkDbwt6hac4qvaAR1TbCnoNNRQo85P15RhAk11cphrI2U0QU4_ehGIW1E2ezR9KYsm4AlGEH13guoQQVrG5bqDZuXEksVoQa0iwGHdwRnRv_SxkrId_oNSAzWU0oTZpVHrolV51iwoDTZ98jkw4tMcJS_zwhwbWObdnCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOh5lExYPNCAAPvowgerH5iXCOxAByzqIH8HvC5UaOfr9LsmQ9DTDkGelEdSoAKn0ikl1KXJYk3M0Y3OWMHkeTe0_z2-pUbQ91JHRjngwNLQa0qgyKtLwKfjcDZOGxfs_9bkvY71nHnUx7h1lQwEcnBownvtG1_GVaKwcxauGgvs2i_x8TBrjginfRnbimo_tfy7Rkw-2EmddwdAXlEzpKI8pJq-eLJI_LxIW5HxPh4VDRbJa26_VjEikN3UGAgAfudBFD6JJamuhmkF7YfM4T6FNJR9qUKuMmSZC_aa5pGuKnJWXi1jVGQKzzGgBv_dCLlEJ4LtEBtW5aaEqUeW5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjrIlwwzjYCy-iEpbXe1UdW51TGrbHy8uLuod6Xo9JhYlmBRPuZFNKReO8kl4uXt1ELceVv7vsrJ_sEQS4CfPpOyq0gFSqMmD5Ps0ia2XimAogI34cVEVylrou9Nfp5_-Uyxt1woCK9KOuWK53uhNGEipy1yLr0tPW2CFeNCtGfjP0ArEOk6q5WUsLzU2qIV5R_jx1tQtPPRR05uQfMkmALwB0fbkN2yl1-RqCIJ4ouGRW5TOZLrvUQ15EobCmqAt02E-nFhoKJi4NVwQNH6ET1syUsCm8F8h4-pJWWWgyWXgL07oC1A5xRFVy-nABLabASH5NFmsspUBT4pShCnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c3e3fcjhnCGvriMP9oFyKOXiGS7Mb_Ky4GKp4ZwtjfD2jJNbNea48RBHZfjtsKZnHphBISxt1wMYNdg3ZanNcjHcSaXDOepQbGD3chVP74SFZIV9W0D4KOVf_9HH-IE2Nuc-Ifjfu3A0Mc1qIqxfxIyCo8nLA5PvJif4gI-S3vfa0Xpt3JwtT-ZQUXp0HPoxkUqtGr6qJF0mKK0KQ8J9WOIzw2TOyXNnFqKmDO3DLDDx_XozTz3EWIcYZdENiv7kTWoV7y5y_CRnjLx7dhRqt1X-_F2M_6X59oUyQH0YuFnoEfHZoAm8nflG-h8605Ui7jYTpURxL7WCNtPyY3_-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQGsHC253wZrTQwezPFXx4qT2k6OQvXp4mVfJ2w6RZHQqtTC1Lk9R1BZewEPrU0ao3TEo2V6tYz0zZSydlUDkV1j_isefkuvMniw1d4L8LIatEBGtnxwOrF8XXuvWgExPEaXi370oz_cthE5VtlCgbwzA1oKG0uRyyQ3nYejkadHl1nIY6LluV5gqZC7KNzhfCEBRqTZqQhInIKPX1eAuDkBXA7nNPeVKprft-5wQfa7QlitqICMHlKj5wK4prDjtYaj3UDDUvdjp_EUuy5g01sLF93MhCVcoFA6pzuF85P6nOdLMvKDenPL1rDanYsb55fkVWznzKCnU9kmc7A1bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26553">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_4zOQM8tReULMPQjIVJlbl0QdPaeCVdJJTRgcxo5wcEcG_9nMrQ7CqIMQu5JgI-XqKPWhMvt4VvUHM7Pdw2yA6MOwGQz69yrJJz5S87dt-hmQtRcCd6_CRxGixqcUA2saGsUox43bvJjE0GyEnWpA28KC0ArZ6q6VX_dnvJmv-_toWeZFfFG9FUurBdJfPWaYgoAAS6hbbcUEWO2YmyyAVpJam88FTPWkBSCFKH0teq_wsCG-HLnKIb08WpPVMpzBTp8vq26HPvVTu6owWVMgs_1iKH2iSakr4CKQj2toa__2dcSKJDTFPV45M51peW6ES4tP2KYishbvXEsapBow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26553" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=EW77Yf3-hYPFnBFV3hQTQXhaCbzpooZMchHdaRHzVq2lnGfRJD0tEESX1V_PAGPGY_o3sOz9Z9PNxiEdhqyt29H_5MNccDqUUqw7Y7pwcP8UL_4-r6vOiquKKjV-UGe3Ryqk_rlts75J_UMPzzrtaZIHi17XiRsC413o6S9YZI2lylzdvjnHOkCdxTUVi5XaKswD6TuXQz0hFamQYxEUk4At5vwmO8VOOTwDHUD-FufQEpQMEgz7FFfhb5tjmJOZeyTn9XoclNOA_D1qXZYmDZ13mpfFeEqJqQtbJLprlA788LFqDGyfgMgPYPcaEURoJggyLXu8AB2Rll6k44ikp7sHC41xjonJev8L6V7lct8t8tK77ksidB4QViffOu3KNRfdiHv4xq4QFI6klh4UaE4FvNpurC8ZTiLESd4ec5U0Fh0-A0gXh53W8S229ANRGhf4S_ja6KClacSfjAAqW1qzwTpGG6S23qI3DCyCqH8rGkUAmXq5I_bwfC0JsdIXnrEq8GgPJdGwAsXDQrdMO655wja6cPU2b1mg8QMnz-eMw03HypGzcwgLsmAkZuOwBDdgBVA7EA0TloY5_pu6NawKc4G9rnqlxbn00QL4l7W6iTzER6ymEKWbseFdMKgGTCu-3827oaHii9sFLA_hlhoE6OSq7bx5MEOO-C_AA2U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=EW77Yf3-hYPFnBFV3hQTQXhaCbzpooZMchHdaRHzVq2lnGfRJD0tEESX1V_PAGPGY_o3sOz9Z9PNxiEdhqyt29H_5MNccDqUUqw7Y7pwcP8UL_4-r6vOiquKKjV-UGe3Ryqk_rlts75J_UMPzzrtaZIHi17XiRsC413o6S9YZI2lylzdvjnHOkCdxTUVi5XaKswD6TuXQz0hFamQYxEUk4At5vwmO8VOOTwDHUD-FufQEpQMEgz7FFfhb5tjmJOZeyTn9XoclNOA_D1qXZYmDZ13mpfFeEqJqQtbJLprlA788LFqDGyfgMgPYPcaEURoJggyLXu8AB2Rll6k44ikp7sHC41xjonJev8L6V7lct8t8tK77ksidB4QViffOu3KNRfdiHv4xq4QFI6klh4UaE4FvNpurC8ZTiLESd4ec5U0Fh0-A0gXh53W8S229ANRGhf4S_ja6KClacSfjAAqW1qzwTpGG6S23qI3DCyCqH8rGkUAmXq5I_bwfC0JsdIXnrEq8GgPJdGwAsXDQrdMO655wja6cPU2b1mg8QMnz-eMw03HypGzcwgLsmAkZuOwBDdgBVA7EA0TloY5_pu6NawKc4G9rnqlxbn00QL4l7W6iTzER6ymEKWbseFdMKgGTCu-3827oaHii9sFLA_hlhoE6OSq7bx5MEOO-C_AA2U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo2SeUbtkq4Nzi284cs3rukjY_SEGp-vUxwRgN2TSLdZ89aj_Vc82poJ8FEr3msTXJAVS1UpkGtf4Hpf7sE0NX3VZduaH9Uau4LwNSBuNBumKymBkrzKYnsOVP3p-MIx-F91cwO1L6Sb7aicmQ0W2o1M8d17wHDRxl68qYhdxq9rGW7YaZYpZg6lUxKmlecEq1tbY8xR_ih4PJBrT-dE0X2PwM854LFYVw5jozUmTB80mH5kU_ATK8I4h_DAHXB8MUuzGbGaXnnw77EjpqygZicK0aCm3-b3DGiE6fnYY0KP4QZrV5hhKh_wTFsLAAJLkIzI_MrPyEbGdND5XlEorA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcw6BKT1RTHBG0LNnZrLWG0UYhxr0cjriJOcJQIueE1fJ0-LWhCala6A4XWHof01V-dSXO78YurJET6ekShlK7FskEqbhETeV-69m2sxH4epiFO6mUuuN3We1LHShGUvnDc69OWajNJ6IQVeq6zSo2H2BMtqHkt34Fbco4xqHX3XD30eBg6L-k9juRgzVdvBvkX-98P9lM2a7TPiqRYlBJFe6laiLd8Z3d-ig_zaSn6Fx-6_jQd8uNXdP4snK7pPxeL9-skIRoJlMh-5JGFhTfwpxueiCFECGKLrhCO0t1VGTyMsYw4H_HL1wgl6CW3bMiYZQ8AsKRJFWapFeVPZvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPH0PJhTpbhepvH05NNe69AsgfPhh4aJrCH-7s0mAgwlgn0mn3r9Z5wBGXz8alXCLxVP4ZbkmaY8KEO4N_B_z_VI-98G3XThsk7TgoI0YD2uQhN9FgEh0rl1e8xkamIqVwLz70NQDU_Lf0Ov2Orny5G1vpJ7jJAYX8y9ZoAHD5pUgLTa0QT9q4b3ATebFhAe10P7Wa9eBuz0NvFlapQyHlvMAa_zbnAAfjIvFnHpQJygTY5p6ccXb2SKC7kJUc01VowPxiHmcL-N6zXPXQghjQoEbdk3Bo5PqzwVB_DB87kJd3_g04bZO6sgSPqfb3vjYS1EucxX6hw9J1UEMzn7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=gD_y5rMOKHK52Wd7eC5OUB-iBOFbq8mkCG9FePqWjnMuIoLBnBKtlmfnlZKhVm7NcCNZin1MT-HQZMsz7RIpIPDwYxjPbr_XQgWByEvd1K77o-WAnCmvPxTqNZiUnhDfYDsWg-TSwU58WkWNpBINVKql6iKu_CgeZwEqSTb4mffzSMgyIN3AOB_jofvGmiPDEQ-a-SelwrxRtefJE8id58gL2AoyySSJrJUZiyH_NXl41Slzhh9re3jAXXWM8CpaphilgcjRB5J76wN4jVqrTf71o7urx7Ye9CpEF6h5gokcdpb8uiQyt7xcLArPOGrKXT3v1ddcCqWEY-ndsFUCcI6o7aE1j2feOxXRVrxkvp5Wy3mQs8n4hYXwAPF6jSKlyGg3qGVPE7R3n0ndnMxmkZZqbJTlJ4c6BI-nF0qtf2kDeatZ2YodFq0qykcdXJJJnT_oKlyN2g4a7dsNQ55vYuVYicY0NDVlhPoKBUo6s_tYHHp9TKa2HUjsgzOrz2LEeDFJKBBirg5uAD3UuJaBkNeZB1uNAK7UUU3OqV21So_-9Y0MXlsk7LzipADTrL4jBUXAsyjTwyQm8RzbGxrtpCiKWD585YUWTspW3dSUEQKL_qzwiuJt8_qtwm3LIe5zGOFI6q8RKeMH8hOx0mPpa1hrcfxGZ8r1s0jA4oIpeI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=gD_y5rMOKHK52Wd7eC5OUB-iBOFbq8mkCG9FePqWjnMuIoLBnBKtlmfnlZKhVm7NcCNZin1MT-HQZMsz7RIpIPDwYxjPbr_XQgWByEvd1K77o-WAnCmvPxTqNZiUnhDfYDsWg-TSwU58WkWNpBINVKql6iKu_CgeZwEqSTb4mffzSMgyIN3AOB_jofvGmiPDEQ-a-SelwrxRtefJE8id58gL2AoyySSJrJUZiyH_NXl41Slzhh9re3jAXXWM8CpaphilgcjRB5J76wN4jVqrTf71o7urx7Ye9CpEF6h5gokcdpb8uiQyt7xcLArPOGrKXT3v1ddcCqWEY-ndsFUCcI6o7aE1j2feOxXRVrxkvp5Wy3mQs8n4hYXwAPF6jSKlyGg3qGVPE7R3n0ndnMxmkZZqbJTlJ4c6BI-nF0qtf2kDeatZ2YodFq0qykcdXJJJnT_oKlyN2g4a7dsNQ55vYuVYicY0NDVlhPoKBUo6s_tYHHp9TKa2HUjsgzOrz2LEeDFJKBBirg5uAD3UuJaBkNeZB1uNAK7UUU3OqV21So_-9Y0MXlsk7LzipADTrL4jBUXAsyjTwyQm8RzbGxrtpCiKWD585YUWTspW3dSUEQKL_qzwiuJt8_qtwm3LIe5zGOFI6q8RKeMH8hOx0mPpa1hrcfxGZ8r1s0jA4oIpeI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOVkt5oWbC11Gtq8YwTWAUq3XmCP1D8_VxYhNGsSIAEXYnuta6Dswv0QojwOqGqdw2gOoLkZCOLY6YSNGTKHOaDripBMiAGw87QfaMelVNghDWeZqqAZOFYwqGG3aHaQDUjiUDCCNalLdA6xeNPZtdHyCGlEU9yPfW-6imxMjjWHwmrtfIs3nbitxc45SGFUJ6kGLhdqovFW7fkkO0aPE4ST7plrAJkHO1Z9JMamDX1GuhxRt1Jh6r1mCqJpx_c6SRa5wEJUDahw1O2mpKLFLNthGyLESSAe0clTVtGjuGnAd9VW8jL3oSvG5z4J_HrqjP9i81NfYh1Wf7mnlMg6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g36of68ua5lMn12R2QEpJJfcdDOlHb4evFa_8L8iawR4te7QfV79cHW4ThVM25d60DeY1jT-m4_bOf6pQH9A3xjdTK1UIOHopF3R8FqTycxLR2bni3F8vOX5oyNB0nk4Eb99Q0QpqEEkV8BleoeLazOkdGWMvGTFBxbjnvZH-lCqeQpVHWI2sCOIEhzgnEoMQCa7NXZnvEuXi8eEM6NdXSLxRAYIZqtIRKoJPBTFgBZhcV43ikPvS94tXLnE9utRfu7MYtTlwgmS-qnsR7YjaTTKXFDU5afFcemGwcVscNq5jbXC5TyXLkOdefCO0AXaKodfqqAN-CmFwTN8rlbTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FASUWGNvYl_oCB02AJoVO2SqKjSkASIQiWOlXel2FcfeMAhViXL7YfZ3VYazBgE8LdpkWKXz5xIha7_JvY9BzEymRDv_3AOKrvzLs0eOuiijUtsdbnrdeyTdRUHC2bsmpDjaXVTCTiLu2fCqUUZQOiiJtd2acd_YZpFQgJRdOP1tsdML56OlctGe5gRilYKx5AfMtEb6JZMkwgLGT5Efr8kkok3SO_uYi8qCiz_yGnwJXR1CjwsdjCy_4Wxl8Q_OLMAXMFhkCzW69CHgETFE7u0YNmrkadUQDFO68DkkmIwXF0P7LZDba2Xom23RWpXD9HFk3pXhGSonbw8CKziF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBr28o7kgKdCWDDcZs_yMqV9yt6XFdFI8Ry9WCmhvcA5jcNw1s1dcdsd0BJBnJmrUprKwps3u_lxfJS1CwcCyOI5vjSHTu9NiexWy5Vr0S-u9OMOoZ8y_R_4D62EfaQmb9S_eQtOkboDDmK4dFEJkvsd15_tGOjuH59IIbw8GY-8CzygQwX159HXMK59Ja9skVqjMcn51xBvV_jDovaelENj7aNhHJq5MOrZ7KLrMRyCWNvgVM6WQfX0jC9XMFBC3IAXY9GB45TxNuseA9R-drjmdMhkz_nKBkZRcsCY57PLCq-Y1vqltDxMOPYycCgz3D2GgDLgKWn93efN5TlRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD6H5fweSRqw8ig08WKxO8yX3GhEY5meoxM2nTTDfg0AWGRczQHDytiENNlz4pzI8yW1NY8_OuKoO79p7H29AWGw93tkkoFDvh0TiHw8K0v_gXL08E6q4j1tbeAINdUMRItzuhApETOplERsxa7mb_3arWeR_BvVGKQhX-8q6gck9OaL9rN8lA8De4NR-lSrsPi4O-uHmxhGpTUpt6m0FVKqR_R26YNi_7hiZgmLcxpAMBPKbjf8rNRJ3TiHrqlBIIuE_44H1XLj7mabcdgLT8KMYHBNc8D8P5RDAXhRHWncsrX0Jel2ExzqEGqxSPT67bS9Mlsnec36U7ejt0nH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=ijFhRMz7IiTlwaVKpSSaaFfEUQZ-LortwINd7UAk10Ip6u-HjTc8pJM_cean2YwdqYdABEvlAnYhdAW1xY1rrcNNDEKS06oOlSDv-TWsEU38C7C6wZ3LkFXrMDGmRsXOgpaY2hn78GfznI18509bbX5-PZ5AKs2X_S415aZUTE_oHh8zEMn47NcdeQlzr3GyPeSdPAeXX_APR1jG0l2j1fysnCF6eE5xf9W8twilj0rHswMtOoV2A0xErolc28_WK12JByNqvwiyRPRMBi417rcN3zt4aMUqwv4XdUHnAv1xLhyR0wFafEOcGLVBqLV8zTD44u42ua5uaOMmZM43-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=ijFhRMz7IiTlwaVKpSSaaFfEUQZ-LortwINd7UAk10Ip6u-HjTc8pJM_cean2YwdqYdABEvlAnYhdAW1xY1rrcNNDEKS06oOlSDv-TWsEU38C7C6wZ3LkFXrMDGmRsXOgpaY2hn78GfznI18509bbX5-PZ5AKs2X_S415aZUTE_oHh8zEMn47NcdeQlzr3GyPeSdPAeXX_APR1jG0l2j1fysnCF6eE5xf9W8twilj0rHswMtOoV2A0xErolc28_WK12JByNqvwiyRPRMBi417rcN3zt4aMUqwv4XdUHnAv1xLhyR0wFafEOcGLVBqLV8zTD44u42ua5uaOMmZM43-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnDX84vwDsso9q1WwkOy9hJR6rtASMFRFE1qvrupKSXC3oG0qypg8TUMPSCfVb7Q_FOrbihW1oP1NsRmFBprfsDN_mKo0aXy9nHyDnIxs_2r63F01gBt0pxc0TqWchlZTd0XNOZM9H98FLYD_u0gC5AOYLoDMFMskN6K21B4d02Cune4KtC9gbH0v3j_T_5JVnzvj-KWJnMJPBAp8UxSTpE09ycmXP_DGCjNry9fyCrZFZi-ZaMySjXlPbc_pilWqsdxUKMEjtpMyFRoD1JjsTQ-lYBfgiFGLUr4QLvw0F9qgHtatxomrQxy_Of4dHh22n5DMtVmxo70EYUklCdoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fimZGywaYBeVmJSYYxwDmS-5KVrbCc6NP8CuqR2QfdulsbPfgVE6PBaH0cYZJZwFFTZcT4Yb8SPnbsy4M-jzb7S1oXgQe2qwY3F1UIhtv4DN3-b3MNFQGb5wSoyeKlKIkTCNPFJwants2kClLnat37pGESdNShfPGwwnYbng0v9ZjsvwzFMX24MQ-MyHFMTXbWEyqSXvT40uM5Pp-RPWwGAo1WKCkQD_ePL22hqFoKFk-MEFpblao4QwZ8DScgUjLc2p6kPVsHHolZpEZNjh6NyVubXaG-XcgBfaaXE39S88mD0GuxcPxc6Aa56mGL8lwg_jLanjTkVk34mwFsORPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEJliDLH1HvAL7qxeiFxQ7BFE5BWw8l_UUVPuzbRSt0gn2xB4bmpDiXjDmkVo8yJooiZzEppk7jIwJX0ioXfgeCFoqCYG-GwG420j3WLHHfA_KRSM3wfRiTRRa9FwtyK7VylqrAQccj9b5xuYDaaF0BuBbuUv5LXgf_suGFHt_pEo8b_dxF5ZF3Htu9aq9AbMN8yyGZl65e078mVYQtjneltCWvHCdlVekLUV0Tvj6PBRpd5Vx4i4CgWmvIDWRV8cZqIhezVvIsLcbf6T6r11us4utfGAGhiP1O8nReA8uUFtUYqNYa6N3KpSPzKDHRKzk2mFmLU5jsOo0aWSM6I8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKH5hc4u9TlKxbvD1eQvDvPthO-uJkqogOCQV068kfu6N-rvX-G7YdCIV0UrokG0jQ93kPyRm3aka8LJcf_0jKSr8e1XDnnsco0ZavOUuTFTjIZhJWhhRB6e-L7G3q0JWyGa2m7OWXvVgsN3JYr0GVLcK__mILG7Eeyj4nSMyGDyDDAvO8F5JSlpInLZdirjyeTwwZgETI7nV81Olhv1DQ9IWoGBIkSb9F4KvyjDwCW2yMGXkCDHw2H7vadqRkR0C9EXkVCvFkwQEUZDl2jR_QMPGC1P32Ru7uxR-sHkkAu3PlB-tET4CjbkJVYhE_fwqd9Iqbe55QigcT7rCuln4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc2s4IvulcrwCZ4rL5BS91jUEdRRGWFFoHx9mXvQTUnSKPgSzxObX5DnuC_28DQVSg0eIJNKVApy_NFonXBy73RHngJ4g9TTQOt2q9yQOBeEClj8sLzTdS5P0uqxcj1s3xKovJ_b8iSz2zMdwH8HezLAC-Gx8dEsFwtfg_rtB1oozMLP9SzrVSscwuvGnVMNFs6BmydDd5PWkMFUPUrVC_3sLV5fDFHcw2snYsN0wmasUmSaoFLv-BPiRXj8wA2aTZzvlifjdMV7KoztLzU9yNamV94QDSKe4Tb_IyrN7KCWsbR2uCKppTTZpR0tNlmgPjht28vEW7LT5_n3zxzMlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQLbgABPD_kuAwPHoaSpMYb2QowFiGePH2t90r9ILzHH22Ak07F47LV_yFk6McRTc8Nr-xZd0IkwVz6-JwN8lLK5HL21GFxxwEM5sCHr9fPsZv-zy1IfIbHhRnW14z5KnKT09HAIxJOd7PKJ5x_JQrpPbV1W6rhzHl3yYyfhQa2gWKPAPIxrJ2HM01bdrHeKWC9YlqnjHsD68-_RbF7BCWeMoyxOzxk8zh2KobGHKlVPcdKuBMUaqVdRAn0vr06WQNKLSlK0nurUQ4jt4TGaPWsRKUncx1kKEFOnI-ToXpHc7NyBCdVEvNn_PIFxV7yTxASgXwAOnEByERwX8rKRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOqeba4tFUYKau4GIucCJzHekW5FoTGWtg2Ou3MYR62OFAHs2MdrHG7OHSsAcyrNi9Y0vqu4-UJ2aFWH4B8oRWj_32Lp5O8xTaHiUHcmuLfs2ILu6VMjD41EIH7Oy8NB7DggrchQQWoma1x9poifxbxb4RRrDvWuHzHNYpXGPwf2OW7lCqGuSob9EKy8VnziDvyHKTVPF--wZmmnp4nUhifW-69VmEm5KEaDk7hGjh2POEnmrVVGIwYG_tziFXredH9LQHqrmKNlPUICfZORjcCWKm_MtPas5r57QH3uNu3GdlA1fUrjWB30CYwNopAz-w5EpdDBt16FNzSZP6Wklg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvRSnZhGu48rbOd_jAXUFhHRnLUhchAUkRRrR6KUQtZR0UvH6U06Puhmbhafl3j_IP5nhLo4hi_q2o3unYpysAlxogHFZRkYxbXuD_7NdkFpa0LKrd_OnWKO2UT9qYWX0eQ38cA0dXGvAMITykT-y02Ijy_XtgEnEjkmBaDD3aI7D3jSdoRvcXb-XSN3Y4tZIMiHkSm81VOerd9fwfnw2Eo1k6Cj2wYmH9fAqoJYznOV1KVdW_V6XXD7zHaAjbjFs52uBuZagoapxAQEHev9XITq4F2iGxY4FVgxsnmwD_VIkzp-07Vm_tfMjY7SP1aP1F3hzfySCB_w51q8cxmgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcI6M8fsONPOIifkU5TDhea5TLKvny0_ZhcyEoVQNWjtsRjUuy6qv_chTfMEWanAXyNWJ_suIAPxpsbjI4FZYtTD8jj4sP3IEQD7ndL9uzhOzdvkfN38-KMPGIlnNszplNzsOuQ7kEjrPnuY6TZA51LMiPXeiBnjTc0GJa5IjlHH8wRquioQXgvEm-CImtLb48ROOOjsNDrxn_LHXU7s8myeY7f_VblvFxw8HqiP4CExlhBReAPOne9QGkdQfm57tP6L0HeYM7Y5St_PRWLsuW8_XLV9tx2GqCzPpLAOGpuFL7J_0Q0j8if-c3NwOpGrYRRwFPwLDqXNS8Pl60CdBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHmty51O5cGFBk1JYlQxQy4tzEt5FiYWKqRGl9mCqiSrkqT1vk8MqxNFywjnYKRBGG-p6b1pFqj6WMjoydCOLUx3vKIgUsSvBorF6x9NYbWhO5X0GCcrz7fFdx1GIpLfRuZIWcaS40jF8jUp8jmp5ne85ahZXobdMlv99P5Q4iDfObhfbPVFrLq2ko9BVZTEwYYSCplcG4IhwXKqEil9sxxaBchapNSEm7s83_Q5mK45W4fqiSuDzaJTvrszQTuLfZTKW3m_x8FFrGBfsW5ekbk4bE5DXi2VSqWjGmm_5Wt2yhYpF6dFDXjohjujyiljIMhrYX5sX9vSOq8eAIPVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYPanTD9XQFliC7UJZuqDYaT64FMwg0Fe3G02hFEX-rKKZdEpFxDnIf6ikI9brdKo0VQYCzqv1FxI35xFPxU61flGd_qpcMH5OBmcXmOtCWkNZP4dDZ2DaOYDz_2nb8DL_RmvEByhreLnLd5A83JCAQG51SpNanO5NFnXJ6VhyoknTLdxDyiZtLYUazA8B99AEXfEupGR-4ZDbojQGMo_VrQigRlFXooVtPgUirZ9I9SyXQWBvlhdit6OOgbQXG9CcZ2FNA6H-ioXQFfSXaGrcE7-iFhApBvs8oimS7QOovFD__9VhiX9xoKf_v4GUYVoT370abGtR1z9z1_7-PWow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26522" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJqkjy4GPjc4Dz4G6ntPiP8MIfIDr3Pxgt7di7Ln-lb2nQjDdgeADixB0sG3_dFNJAbWzVku3pUTaoIRyV79lxmlrffcRV-kL9CYC24L1403WwB6RUk3O2Heex_tSBuUqCYGeVVP6sEO0QLU43SmHrFdBckVzjCWyKL7Q-xd5HhKLBImYiM04hvgjSq9tLEdTFo4uFfB6hJ76MCALk2liClFmyWArEOmh9M3yXLX43O04bZ-5vH6vl78ClLsIm97avTFlSXXJqfViBcfkjBODQLKZRCxJApTi_6gFmADwiPt2bPoRAlrvmk42ruKoJZR-rcF-UbQuUu1TpShsyzs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j32mWN7a9F2uI3CYbC3hWScIC_y-jKLUJwPYyjByhTei9JZsXQ9aIAON_-8Tvo2gguue8ZwO8gjLJ2qG1GCu0fKrq0nfKSGgq8z4IY4xnVSH--CZ8ZdmtFP_EAyhgdgMDHGGbctMZt-D3G9OGIYa1L_c5x8FKpQSpJqJ2Ci40LMVJMNDhQV4Fqyx_Mk5GkKo4-r5lZm9tEejUrUthyB1-ilxxn5_k9S65CI1PDZcd87JK8so078R5nnObKPaP955YoT7DKaDc8yasZwW92fEoplYKSq8mkO3X4dy_oy2yeBfy8wEOHMb2UwMG-kYQMQaFIJ6I6Xn7ARJnM7DjydpUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaUGJLvAQDSHLb_sR8bQRNRYcj8nGvhBM7zFNY1igy0PE1UYMbEIOPBWjkOp-3i6_N-g88JirCL787gO3hCMjjyg4LgTLqS-DQ4iL25E9MBDwScn6T4f0p2pPKxxJeiqtcsiSa16MRD4ZtEqkzTP6phBQx4OWpn55tXwwgcCUzgP2VSwAmjHcyexlKt-R1x12hpV4qvKtsLQD2KgbactT9er5g6mM6RdhPuAUZaboQQ9_Xuw-e5K9IZdLoH6ejxRrqimb6ZjcHTWPVvmx-i9_qXoDR8-ROeya-SCmuWBBznDFmhSZHhUgpEFWm2B7dASkTqYIfXpeqL1_iwbCWOwOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nilf6qQKVjzFWBizXI2g5cgtRPCteWPQY_RD3dA3f-8BejxZ-PppXnVlb4rMr_YlFo7F5vbmL7LpHvpJSswtTshrUSes1ylGfADxz4d1XI4gC980db5UMURr65gUgg2d4vJ8Nac86Pqq9Fuobbd0c5cLMNtpsMW6yNJluJzGThNw0AQRUylJ856MiKHVXi8GqjKjDOJsy79dmd9FkDpGccYaoGR-8BL_9dK_2PA8bU1T3bRoX0Xt1UYhovzXAuEDCTegF7dYLIbpyhyyW-7vk8n6GZnHn0pOC90UeMBci4JrTw0XdpJJderl8h8GgQY3mX8H0ESl8lgRjb8RYpBMEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0kIcPXXSoPtAC6jLXVwOl0oNpAZuFKiwNEjv9OtrhdHCeLl9OkWFAmqaDR0rjfIlN-lHUOM0apEdDcGhUfKxym4uw8GsBGzbAHtg-TxWhWhRgPqc5LK-vWtOyfoaQVwCwqPD-IvrPY-XOjkT2btbxKMkx5Zsis73dfkN_IAj_pM2_-UuNUiFyH5ebUGzqErT9hbjcXLyyjOKAQbDlz7P3wEYtJtDy43Kc6DEpZH_Ox2HB09aTEcwq6CtJZh_Jm-8NNxGVg75os-JDnYR79aNIsQgETVX7A1mmmBXIKzdtCSa4r7S3UB7RPqieK3nUxHkVsi3e8O528gZB-inXs2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdwHbYRm3s6M_H6KNN5v06-XRvEqF7xNG4nbgG-FzoFR9AkHdYCoZjI-6C_SUD-BJ6DBYCQBWAOxRIPdYkL-AE_h7UtouFvxw6PryYZg4EggH4rFaghQRwGDO5v8AiCVLaGn53WCX8pLrTG220iHl0cVzhuIDTy-cQ_J4R_P3eDwgXLxnRDxWXLQUFm6EZ0RACXK9cdZZA_LtDy7q5JG5Wp0TUVvf9A35zqGgWrHdRN7pTKbdNBac5X6cJhcF4i1U_IC5bJ4umclMOEzFwnvRlAO4W-Gt5_0ecv85HPZRdS141tHh7WRDJDjGr3Tw7GaQi4j8P7RNsOo2wUV7e57uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zh995WZge_1aC_vAVUtZgJ6Ib4CQrhLsNbEYYkPZI7CQGtEvhhoPTiURNKjjzwSJBxOcXt-aqMZ58aUnyZ81nAx_uX1zb4Syc0wW6TLaGaGhUbw-cgUxazAIUKnfeGJTY9ol91T_Vdv1H4tAVzMqzI7_afvAcXQQXdzAU5F9sOMGlY6F94cFoqxhN6Rngb8Qp2w43iilR7k7X-nRaUSNou0oM55q83pRu-CR1HEgQNQRCgHxpZHyVWKEw0YtU6kF5cuck7aA8aeeLsLt59b3RLtbzLQAePURU4Bz84fqqi2ly2YLG9iwI0PAUYajY64t_VSJ-0RXELFBPWGsvYci6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiWE1GcFowb8rJGjBSEMb8MVdPZO6zlrz8-J89MCJNyeah87eZsFcdY0rdhHgheNrjfnFsGi2lFRHz7sSTjx_NBOisl89zzgK_7_i2Ln3RO56Rit-VRmN0i2X-lh0iHOs5C6q6qfllATEGD9xaTszKqG0G2d_yQioVjKWne4nYHa1QymWZeGhCSfLw5HMr0-bUeina1_bRFVIC3iSLDPRm6c8X9mwq8Hsy1gbtD4dwX3AiPE9madGGQSFvXLNsjv7Ru9bZ7ZZKraOHvj0GMJSEZHYmw4F73AUf9BvmJrSoF0vhsk-JIr_Zb2pd_YtScVuoZtSE4Oe5zwHCOvxD1ftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران عالیه؛ مدیریت گل گهر ساعت 2 با جواد نکونام جلسه داشتند، ساعت پنج به سید مهدی رحمتی زنگ زدندکه‌بیاد داخل جلسه، چند دیقه پیش هم خبرش‌اومدکه‌با رحمتی 3 ساله بستن تموم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/persiana_Soccer/26512" target="_blank">📅 22:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxjc9vv1FXB4dBXW3O7G4yDvpxjajCLTc5Om3lmTBwHt8G4jsKpgKU5pYwtG5Pb1e0d_mAcQPLAzj7Kxz0VIsJ9oQRwblTBDVktpDf9Lc1Ze3DFbUPB-sW-j6Lt5dYAdu_kSnpo-03O01ylKsTYk4SxbH5ugPyt9n3q7liCQjWwoeZXLJMM1GkiL0C-viMZs7rkFKEgIdP3foKfTDjGG5dT_IFavU_TPGWHEhe8bwXBwrbPQmvSg3a99b3g3Z7Jrkdf4K0NxDfr71rrHIi2xU8WRF00lVHi8we2rJejd1f1QdsIbgSRSYy_IJMZqfGFXO-dO0qwnnnGXcgKGntH3Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛عجب‌روزگاری‌شده؛ دوست دختر لامین یامال برای اینکه نامزد سابقش رو فشاری کنه این ویدیو از خودش و یامال منتشر کرده است. چه دل‌خوشی داره که فکر میکنه یامال پاش میمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/persiana_Soccer/26511" target="_blank">📅 21:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26510">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLLPwrIPZliSZc1WxB9ihDqBwMnOtxrw2kb-pZuQONLWC1dcOZb0l5OgSVnkIIIrw3K_27MI4i3_z57tE1rHEzUb9l9cibpakBJw-8rNz5k7VCpskA7lYRNkDVhz5e1SwHKOd0PztrGs-4UT8LYPHzwI98MTQzTHIatVDmuSdMsWvLa5Zfce3Dx7QQ_N4sW7H2Gy-88nqXBJ8SiDKylnC2QS-nEIlfxn_DEMkSpaUoZANJVEL6PywhmoDzN_cW2ShSiMkecQsGZNha0BI-KeP80BzKREfnEzPcSGtmf5vsK4ahKfu-z40IV43abncOez0fpIdHSvhZtzbjZ5aifqsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26510" target="_blank">📅 21:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFiMQmbZ7lq8eXjCAzS6p6Xi6_rWQYAosjeLezqsry3WBf6vK6_SdlTsiFsCUD1UXitLLWYwjzuWIPIBBGs1A4v57tRbSgVh9rfuu8aiSs0fMYVXhLlz2TKc8AEQYcCKGCMmWI-y8-uVKMQRWrzkfyRd4oIfocpxxJb1Q1fVGFc6S45iok6SwaQWyl2DoHSJatcF2iofQv_HmAF0O5a_ot_dGuS4cnvNvPeYHgx1QT7HL_qLztZbiklUmpQWpVpMocveom_bWpqWFD1H6yzr6Z4GzU_zzcaWQFVRi2Gs5aiUSeYi9zF-KBoGlc6h2uQyPoXXXqoXw3n63MJaOD6bsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QhKG2hn5MSVcj3EV5oCZZ6Sj_1sF3Ta9ZiwjbqlLkCIL-rL83SqJmDSK852D-nXspNK8crDodtzy2ldfhDlg3zIVtvdRCEuacRoupZwgmZQwW-FyUneDEK9FQyG-t4EuM64ckulaSn4qODVkEUR3Qd5XKru6ZkSTsQ_sQt8cB3ZyCk8aWIBamEa-RWWyF3Jr2o5JjdUbSmSOpgvpSa5x7p8Lq-xOWaofOnNq1UXXy_atmDq4jWUGL2s-grcvGcuTwpkZbRXnyvdqm5poX6UsluAnzEJzHy9xTtvGn2NKDiwClGUMjG46jsap5eAsOI8Po2P4JrxOR39pJVFNiUs_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/persiana_Soccer/26508" target="_blank">📅 21:20 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DP19JW6Ao43vqYvn4pASanFWUB6iOYt5oeOmlFRycpDbYLkiUS3LRN7UEO0ug4rTgrgHvb5pgcPZbx5gaXPmuCQjI0rOgXvQstKozc3I00Eg5cldQPqdCTtOWOLzsh020ZYagFQ3vrY7sDYK7TBuEYbRuAsXOpSg-yRlc2uxZAX5QlxiStGq-r3mJeYw-sD5n7LqfOcY35ffc0FNa5fKjueCsn3Xm6L6wt1dZKOD3-cD8Mg4KaQnYrMCd4H-5OC_0dS0Lw8imtNOGSCa4X6D_G0XbHkIHq28AYhEd3ok2OCxC77wGAVvcf5h7DQYJTCAwK0UnRWfDBhF-L9HR7gp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخ آغاز رقابت‌های فصل‌جدید پنج لیگ معتبر اروپایی؛ تنها سه هفته تا شروع لالیگای اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26507" target="_blank">📅 21:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqPJq9XY40vYxII8U97FUNn4SG31abjLwLvmkPSnojkSSVjuJhLDXHt0yxit9epyRFeypnY-evpPXp5RTZrn4uF7lhpMXRwUasIiNgVAX50ZKXurYpoUC1Vl8UOI0w196zIqwlmAy7JMhHcj5khX6u-wCQGt59xEqdXZ2iMr88-wmp1-WxwC04zpnYnL2Hyyqdc7W0nFSJGReBKVMhUWtcHo8xZcszWlNIDIEn68jCKU2SOLebsvNdX6YkoXv3n6glPx4tGWC7PE1tvVZ0vn28qUQSeJ-RB8rhLm6j0SCUyfL9TlJjeWi-PPkanHSDiMQV4LHxM-TuhfQpfUFHjv1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسکای‌اسپورت: کارانتقال یان دیومانده به رئال مادرید نهایی شده و طی ساعات آینده کهکشانی‌ ها 115 میلیون یورو به تیم لایپزیگ پرداخت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26506" target="_blank">📅 20:57 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQfmB7-uXZjiaCPwUndf4Mi9SO-eRiC0jfWjarvpVSGdzadkhmrUmvK4xuTQ1gh7Kj-bFWQBVARuevQOUEYIqX9pUgwOwMlPrDCea0AthgG7LJ5ksnTYWzRueTU3pfYY1Fs75Ox6AOs9KgGDjxKsPH6GfdjY9SfaeKV81ZBrCOkwCqWc8ceJYEQNQFWXX8818ZLhtD228lQe9anUoJSDcrGKmMIVK8J-ol1QKe8Kvz79CT9yKA35BKGQaZtFvvjLlfNBGliHsEQzQUYsXeYMWx9mHBSwqCGlnIbXzMPXccBIlL-R03glXg2biknnjuq5afP_1E_P8YNJhl5l5_sKXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hczPjIC0NQQ8ggGN3DZ98NwJgrfbIonABfmuwDFav2euhC4kNBMIwIEmLofu-yk_A-QJBg3IqnQnarlIFncsFR0BHNEbo8Wy1bDN_0F1o5GFDn9nJlrTFDjZNX_CItMqVEftWVIpiActpwkXYaTx8Je4SDvPfPaGkeMFj5k0WRrAzuR1MkqyZusZG0tm8VaxBze22AqYxqkaH8JrbecP-AXSxfRNDtEjW0o0ZAOWWov6gl4JfjpY79yXvs2hiZVwleE6QCOUPugHNabdactL-VmyXhsiKQyfvm43F35NqlBD_iSJKQIkvRjrncNJH8KmeGy2q1V4VKsOkYULx4xaXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMb1OTXRow6EYq_UTiQ7whuwsJxvY-kdWuj_PZFCleuns2oUyvlKLtMNF3lQ24H8K3rRLRyAEJQntFZGIIpQs0QZQNz5OL3KpTEXy5_6aZFI2JU2L9ZfSVq0sGsUUJDGZjvJKJk3l3aktptaddrOmnW3h7IYIeKtMgNAd1xcUZplK30mcMmI75cCHvwkmNX7QtA8KV4HLkNLcobBdMNYB8pH7YFTaPobjTIVZ-sWcN2Sjk8QIeySGjL7DiLZB7Cmpwu3_bV5PebdBZJv3NqSJufi5-Q_MpTOedHuOzgZQXvHBg8olAW29MSsG-06a-KyNQYov9FklQYJdYUmRro9mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/persiana_Soccer/26503" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=tNky9uxpjLHtq9wX9GeYXK7rXyaw7il6T7kO1RV33DjE1nIMvXMJuR3M3XZlG1G_KuIJwGhj3udzebd4up44AZoKNE7fAmrGNcTA89gosp1jvJZnEIUULZzdxPR0QZZGIxYejAHIx6iQ760YL9b9UeyCt04mln9HjZJ4Dzm8a59X5bdY-rItHJx7jhyujlUpWSeDAW8u9IRbpRmGVHc0JRl8ShevFrbCpwjU8kaaMGOGqG5lWgAvOTojIpGXezou9sCOMBteD4OS5l0x-ko69wBkRIbWEZtCyF1tuBscWkkP9k03bx6X96YBQlMox8MdSFyK8H9AE8rqa1ZCFOOzJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=tNky9uxpjLHtq9wX9GeYXK7rXyaw7il6T7kO1RV33DjE1nIMvXMJuR3M3XZlG1G_KuIJwGhj3udzebd4up44AZoKNE7fAmrGNcTA89gosp1jvJZnEIUULZzdxPR0QZZGIxYejAHIx6iQ760YL9b9UeyCt04mln9HjZJ4Dzm8a59X5bdY-rItHJx7jhyujlUpWSeDAW8u9IRbpRmGVHc0JRl8ShevFrbCpwjU8kaaMGOGqG5lWgAvOTojIpGXezou9sCOMBteD4OS5l0x-ko69wBkRIbWEZtCyF1tuBscWkkP9k03bx6X96YBQlMox8MdSFyK8H9AE8rqa1ZCFOOzJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی‌سابق تیم فجرسپاسی باعقد قراردادی دو ساله سالانه به ارزش 60 میلیارد تومان بعنوان سرمربی جدید آلومینیوم انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26502" target="_blank">📅 20:22 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnPcHiHEOyawbvhvJa-i0qFLniTOUlC1M-Ly1toPtwOX3aief5Ew3Quc2j2ZvnZIofsLBxPsX-vqM-cq7G9uP38WpIWt6XANzj8sVEOSHHbk7s91YaQCYqhWLUcsVBO7Lo1KRCfoyEYFD9G_Bo0yvA1lyirPl0nfnpXc-4-fv5qz77xXA5sYVlPqOV_mtUbYHpNsz4bLUn79jaXKEpx16xYGYFuuSQiA71ZfNZVjAYo3JMHuAHPKqz7xDIbCeZstXKHWkgDGtShxH2ooUNTQS1DMOYPkhSaPNXZ2SOzJaAX15xCrJjBY5IXj8rrc8WJdxcAjLdZCg5KO0f-G6Uyyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUtE5U9_zHX09FX-26RpPj9KUGwhfiIGmeCEC3gl1zOjCxct9RvUT0GB_V90j9aiW33q1v2xNm16PPqyZo4fw-bdcgpkmh-SSCitC4ijyNLl9zuNsowDd-SlHx0jSKBqiEm5FSsRyh1tpW-UriMRYgTmhJSljPB2p4v4i4kq0y-gY3jcBPvcdPqwpvSmJcaIadzEqs6CJ8ziRxf83yypDq1FiSoxGUue7h67arHhhyaZ-_vE6elK4Eq2MDEczr1d7Xn9xxETZ1Me5ma3QCp0jHTv5rbZraxoHoJ8FtPybxvlRtti_A6LRY8mKqAn0flvJscerztZmfdX9oB9Fnuumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNDNYcIXcdCAnHa527cgxZVzUczjRA86_9IIkrWab8NxaxjYPKxubb5mcypDjlYdy0lLeGFYiQgC8IMOxhMwMBVJHLobUzQpzIBqDobZfCjT5x3H4gjBYrWwQAISDNW8BcOO0ZQIiJzRe6Ou4zJixua_an5wmmhDM4Ec-TejcMCr2KFnL9Wc3r_WIm27DebHwbCDmsb1ZzlKtVsDeAkQPTZn1VPRZnAoBui7C3vZCg0l2JqbdNA_1CeemOIFsuxlaPYNNh4nRZEOoNkC5QJb18ybjR2wMp137ym5x-_aDz-RoNKRWLIPE9nSC37FAkjvecJHIiJP2tV7FVnmGHEAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/persiana_Soccer/26498" target="_blank">📅 18:53 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/persiana_Soccer/26497" target="_blank">📅 18:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26496">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUtFAU6jTFqlxuy3h1TWTYqThCwzn3WA896XBVB1gd_KmG8Cgfw-KQD3BReYE8gDCatP-1XQuTE-_Lv0aFyvstCN28hD8B7vCnNveKwVJkvgrlK5aFPzIAmFZDY29p1VEV4dPnvU3x-yZuodz-tFV7XGNFBoGQPJ-pdD1Jn9goPb-2noTxSbQErX3CypuXC3FE-mF6rGFy1YnSAT2qrraqeDUiIBNcjexgCVqmUI1giBnNbOExLnze1AxhQ6fdU-Ti-i8iYUxmKwtXrBcvnctyms5skiHVx7OjKqnPnNV2fUNTMWUpoNor1V5N9cC3UJIoLewTziNrfgd9xfSpx1kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛اگر اتفاق عجیب و غریبی رخ ندهد؛ محمد مهدی محبی تاساعات آینده قرارداد سه ساله اش رو با باشگاه پرسپولیس امضا خواهد کرد. لطیفی فر هم صبح رضایت نامه‌اش صادر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/persiana_Soccer/26496" target="_blank">📅 18:13 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/persiana_Soccer/26495" target="_blank">📅 18:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZqdjdAHU2Smf8mE_Ei-6JpJBm5tTQgC2rBkVY9DPoa-_6RDIdzBXiueALoPkie8icCtLAG0_DVXh8172hYfdCIz8Vd92chYRhZ2tvHviHb_vBL_OvUaGRGnS23pCtG7ynKnP5HGlXJFrrzESFwft0ngg0nTXUWbj6Xva6iT7owmSjwnG2Yk5W9sU3TxtraFYHtj5PRX1yBOMn0jj0b4_zRWnzu-XUiu4GigSo9tOTu_2i6bJ3zxO9Pk8XKgsErxxo7flnV7QiQmlEyss0XMo-VDbB3YV3PNmlSLlMP8sbGEjZoz5CJ065eDDJ8hWkQIkXJ7HVXVy0W-jcn4E_zfZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V49_7TuwfYCqq-iIW-XkK1HBdacf1JBL9pZLDUeZl4jl3fP9FoHIOjWhIk0Pq9cHptf0UIKRNC-9-XNRRhJ3ylvNq_tSIvXCfPrw874XR7yGOg5f_ZQi9c9VcVsrSeNkZF6BCcCJFmOKUAeHgIHCtCT1MNtVwaxoATkF7JH0RS_gT3ZVheHdCzJpa_vNbAtCzz3keWpbmpQQNdJcoe6_2DaIv9UEr5JmKobx6jG4nHTDWbOLwdY0aGOHvp5Q5TAg1Fo-nNkQJunpRp8HVkQkYMxHVXCb6VauTKUnZ6Pt2cpQtDk0qdZRIbZTFEdhqoebjn4Rwt4v7_RzP8qiZXadaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال درسن خیلی کم اولین جام جهانی دوران حرفه‌ای‌اش را تجربه کرده است و اگر همه‌چیز خوب پیش برود، این شانس را دارد که در شش جام جهانی دیگر هم بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26493" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jyev_p51u6PJE5vNVg5PIiQKYJhNJ6amP3t-W6JROyg9961TUIb757fFNjhb5FRrLWGYu8L8c885_3e2d-QDNHNIxXCqDKvjKP-1qTQTy4pDV7cfc5P6NFSxL92PTxez06VsTzphuHxTRgaTySixVTyTd3sadBEhGU-QiTm2L7nm1W65QlZGHTgoi6vKgQ30t361zpU0iuySUSxlzdOD-lxSbBpSbiLLn-aX94g-5O1rVpUKFGnjNAvSt5ijZSd2Nc2R-5RpnP3AXVSKc4JLcXS5PPrV3ByoKLIvsRMcSSM0kPwNOR8UFsOYPWdoUS3s2dwIZSIukW0ggXfhtp60Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فوری؛ طبق‌شنیده‌های‌رسانه پرشیانا؛ یاسر آسانی شب‌گذشته‌با منیر الحدادی ستاره‌فصل گذشته استقلال ویدیوکال گرفته و ازشرایط آروم ایران برای او توضیح داده. منیر به یاسر آسانی گفته دو پیشنهاد دریافت کرده و اگه با یکی از این دو باشگاه به توافق نهایی نرسه احتمال…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26492" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26491" target="_blank">📅 18:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUSjGUevlybB1s9U7hW0csx3aOlZC1nFuYd_MQJXcMQtV2MVgFqRaV6xvYHga54zTPX2GoY6FBNsW1dLs0VJ7a9Y2UPljYbyqymx9mEfPXsLZUExvz7PaXAuAPQ-OihXIggWlzRxqcF7dGCltTClgvoj8hnOZLLLL_wr9R3i_XZANIDwWNQhD-N3pOLNeLuC-18cqp9u2JF9HDVxsLWzs9qsZwUgtyeLMbYQvAnctgW0w_WmkTSfl_mYBothCuurdMhBLnGGKnyC9wgLAL9bljbPZzyhuSg5GXRK7uKBwSrr4Zc3WYQ7GnyU8_alhZeOEWRcggQp5OqJDvghCKck0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXOgP6eumtNOhOgiCkcJUJhbPLWzEVaSWzqQZALhXJPz57kNjWh4RC46AZG1l98wpl9H83AtokxmJZTFTSKV-Q7QF0jKDzZ_lJJBGZIW4d7gNfNKLqv7xa19pvE3ht8a5_tPFSxDtlOKWJkaOiJXsh68-SDlfZXu6dG6wtl1A8JtXFc_ymA1TZKn2iq1Y8r2ScGEwaepDHM6-cEJIwrq-d-KGBtP_Y1ra2cEMktOvxkgv0IWaOCEPn9Hy_qZphwOTRjvE_JIc_bp1_y2feGvnkzOmC9LcKv_HARJ1RnVJs9CL1PDd5Nt0vd1DxT01dFFWt1qZ5sogTvOopyOcrcMeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی پرشیانا به عنوان اولین رسانه؛ یاسرآسانی‌بجای‌سوپرلیگ‌ترکیه به پرمیرلیگ ایران‌برگشت؛ بااعلام‌باشگاه استقلال ستاره آلبانیایی آبی ها دقایقی قبل‌رسما وارد تهران شد و از فردا در تمرینات آبی پوشان پایتخت حاضر خواهد شد.  پ.ن: یه بنده خدایی رفته…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26488" target="_blank">📅 17:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26487">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26487" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26486">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwaPhsrr_zDhqA8H4uaCfO1q4E_LAgnhEXLuQ5tKuHsF1p9jPnCBXQIsSo7NgACUQrbqBGXPpHVleF9hEbGACnbi4VmdtXbhItPiiWlb55Uj9NUH5kX4MgthIF9_yqllKzPZnzIRRk8Ejr92fS8sJQ2bwUtW7ZintJanP2GSn--FqCc3cVEZ7q7Vxo_eUG2Losfg4ILvu_gH4WI0oqYb6jFjQWSRXerMxVm6zlqq32h9FIDN817GH3TB3kQ8WBBoGq5G4LUEouJdI0rCRE9A2M96wQmH7DZznR8lFomeP8btbW6bdesUaxCpxyuYvE1mNyyXMNFFJ__epHzak52oxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26486" target="_blank">📅 16:34 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26485" target="_blank">📅 16:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26484">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=vZKHQtxPfSPprTnPhoBv20cPY2Xy9RH1p29hllwMWq9OEnknHdQVzjfVn0DSjxzgeO-ZRGILBuUXASJ-O8RpodCmaD5KIdcmMmdE9vGo-fH76YHT8xMy5CE77dky7fGk7mIngBqDt71D4liaQLsuaXfw4RjVOClDxieWZ2PZLiHcHCJPwkYl8ow_L0U08tPX-f8-rvMSDNAvw0DQzEh-E1m1cLByaNazzgcSaasr9SEUNlXQjIShVBtsuSpOHsimUlz-E5fdyoqMIPZyt7K8Jr22p44e42d72uDEWoGvOrmD1AHihMBzcXPMk5NDRZJLlXd3FzMCbyDUmo9pHrNyoEV0QQtnwsMmYyokCRltTLkA822CHsKvHSwfYkEfzWz5xvy6XzPF7lNEcsQZJkPNvfVbfCdlpJkNJO2Qm-kzjLlXmMXcPUhfEwBoSTbyLpGyUSqECYTzL58f0KszohFdckoTjr05eKcKmWtd6jCEumvPPhgcBjvo4ytzZUweqhV5UpiwWzCHmSrfCD1DxaWSJEbnQ7DP5oIuxmQNrNreQk4jLRf2nP6Rm1KIF5mVGB_mipZEmO5R3FBxTE-K2itOi_9ftSx5pVRWssTBwb0zP77sAKRZKxgrRARBr5b5chhsiOpH4o7_55ZkYy7pfZbXP7jEGmeJSJVXjKuuvLbSxto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=vZKHQtxPfSPprTnPhoBv20cPY2Xy9RH1p29hllwMWq9OEnknHdQVzjfVn0DSjxzgeO-ZRGILBuUXASJ-O8RpodCmaD5KIdcmMmdE9vGo-fH76YHT8xMy5CE77dky7fGk7mIngBqDt71D4liaQLsuaXfw4RjVOClDxieWZ2PZLiHcHCJPwkYl8ow_L0U08tPX-f8-rvMSDNAvw0DQzEh-E1m1cLByaNazzgcSaasr9SEUNlXQjIShVBtsuSpOHsimUlz-E5fdyoqMIPZyt7K8Jr22p44e42d72uDEWoGvOrmD1AHihMBzcXPMk5NDRZJLlXd3FzMCbyDUmo9pHrNyoEV0QQtnwsMmYyokCRltTLkA822CHsKvHSwfYkEfzWz5xvy6XzPF7lNEcsQZJkPNvfVbfCdlpJkNJO2Qm-kzjLlXmMXcPUhfEwBoSTbyLpGyUSqECYTzL58f0KszohFdckoTjr05eKcKmWtd6jCEumvPPhgcBjvo4ytzZUweqhV5UpiwWzCHmSrfCD1DxaWSJEbnQ7DP5oIuxmQNrNreQk4jLRf2nP6Rm1KIF5mVGB_mipZEmO5R3FBxTE-K2itOi_9ftSx5pVRWssTBwb0zP77sAKRZKxgrRARBr5b5chhsiOpH4o7_55ZkYy7pfZbXP7jEGmeJSJVXjKuuvLbSxto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇮🇹
ویدیویی زیبا از مراسم ازدواج جانلوئیجی دوناروما‌ در منطقه توریستی لوکوروتوندوی ایتالیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26484" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26483">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZ43hr8sU0VqGaI0n_lBdfBolvq0tuCP5tO3vw0OUCX4Hj8v9E2BnmykS1gQVfdWhAEp8vf-UqlHLte70NYrU7vdOQ1869n4qX2KmAGmKZuPCMWmtPXcFHpduXsYj0pyjWIW7vsssaO6PjuLiZ9AgYR9RxrmihhqME8o8z6C1C8TRKEfNCZjwBtoClRDK2A69SnN71TmsnEmlgRQhTwtYNzfppQBNqS1TPpgU1FcIGg04nnO_OJbSr5wSogagPxCUQU-lwZEsCSLWPLXnPUUXRF374GuoFRNyz6WwcRbTsmBqEzAs1l0gxOC8iw4pvTFwaNbeEaj7AVe5EZsiinNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNKdFnZ__DI6p84h1DYsfKfKCrhaXn-FM1DjyCA_ZYKHarFq-nL46JAZaXbo1_oU-f4qlOak_4EUtc1Uhi5zmfGn5-_YmfSu-ayH9RWX60gicp1HAPjsymirM880lfX3Vuw-rBrP8m4L7gmgED6JObP6soW5SvUx-KVwJgFPbIiuRs5SYNDqsnLWPm5Pl7NpsnhS2VuS47nv_6KKvc8B7kxgdV_ZdcjLi2Rbc1vLe7sC0oL9A6jRHU0zLUPSVftVw50a6-bNCpx7xLZU-hMtSkfYi32JMkldPKfUk4OCU8Yg0cWOn5L33nYVttmbju_g-nTFkUYpov9ci-fT9H-Kvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWgo6wdeQBOEDqklxnZQWwo6c6Zr9nS6tt58A0PK-4-x-Isqy-_rJmoknMmaM97st9TB9soCfX9Nzb4eXuoRxpyE31VpZSUYvpc0CpPD6VxD_M9SvvvaublApmuCVp5g2osw0otlRDl9ZEKCWjt7kyHC_nbdDu7UfsoVLtZoSpjW8WGrpc5te85LechEEA05myMXKKCLmXAzGcvVk1Own8ODiVems_Xn-roP2HBGKlVUvwb7lLGIzZbW7mvVGKvnpDN1X0bcbsFx_YyE0Xr5UsIyR-jZL5waA2bJ4fv2gDsaspwa0mUCzXhLuYSiOVGiBp_pA91vRU-WDlFTJWuz7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7L6TgdDOEGXft9fyCeFtfczwRE2Inb4TqTfnemfm67nxJIl9rKPNQ0xJ-RJzJbFBZUK8VXhi4LAy1whVVC0YROn282ePPBcHAmnJpppCH6DsOsKHJd5GRV9eVzzGaChubnX93wcri9eo3VrOTKTonBLZAyMRH2klzGf0JmFOpN0_Lkwq7akbe6lvH0QdMzMRXWoqNxBwx31SedKCeXI7mHfNf3qJqVtQuOsgRh6tyxcZTq2gUg8gyEIAd6Q4G49sJFhMyeaWwxrYF5ql7IhwxXVwUn6qwfpziqy9BzIpMQMDouaddbQX62NpLTJuiVUS4zaV7yRRbHcnz-YeQfsiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇨🇮
#فوری؛ خوزه‌فلیکس دیاز: باشگاه رئال مادرید بزودی باپرداخت115میلیون‌یورو به لایپزیگ یان دیومانده ستاره19ساله این‌تیم رو جذب خواهد کرد. تمام توافقان بین سه طرف انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26478" target="_blank">📅 14:58 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26477">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNC8vtjDkz0nBeoCsMdG6cDO-NvWfJfXMrJSpgohTh_vllV05isrCQcB01oQ2zk69B-wagMLiPJgw5iThG6b_AP2HGUBTKPV8wYPh-5XSiWZ0yNLeeyQmZZUgA3tyNUrjE2yb2CAn06JTcG_DdspluF0oBbuvT1A7Nnb6sgpDJuxBdoZN_WDqv3Gqses2y0rVIrjyletVQKKdxpiaR9L94d1TcX6PasH8-NyRSS-QQinedFJuQX-cc5o8FjncW2p7hq09XFBr91fZQNd84DXqQ4VaHaS3jMdqmiZDKuuaqOI5KI8_c__PC7wEPZmW4ZPEAAI7_ghrQMAkAvM2Efwcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26477" target="_blank">📅 14:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26476">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzOIXm6DGIajiWHNA9c4NqlO_NhAODWU7EskgWC7rFkS6mnHV3NgxWZVS5DgsqGCQsiKypj5q4fUs1Lcjz0q_shByOLDNPwGaGGCvkBCdoCJDtMng8c8b589XmKPX502ODpI3b6wWWhxpVSyc31c1gVRye7XXO-jGWUrsQaxHT5cLGa-OGh_uQvDmPy5IwwhF4e-CTorgPv2Uj99g2IdHjfhJnO1uV5Q6Ew16H8oX7OvEXEOS_aO6PC2GdZUzQSiZVfwZhCEx7SM9dJJlbfVQ2-3QF49TCZexFMgT2ysvZMImOOYrqQc1bRmeHeJLJlggArJwYfxVtIQVAKb5kypRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ میلاد زکی پور صبح امروز با حضور در سازمان لیگ قراردادش رو با باشگاه سپاهان اصفهان فسخ کرده کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26476" target="_blank">📅 14:34 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3UdgpbQvax6tWpy9n7OSw5GiarlWk_SZ-FvXn2m1fAMbJkFGX0sdc5pSEWx-21RgfOWUUB0FWqv79pjgFhO7CPJE3SjXlP-TZ9Sn1SaMkQL2peBPxxg98RL5S2NixffIDdnF3EVeEWMIlFV3B5ahgRCXKdh7u2ARvibNsR_0mJgtV0VRhyLrAx1rulsuzdtkNLAfsUhegWe2MH35bT1QUnkjvAgj4JhTx-ay9CQTam5ty7I-FgMtz3I8732JAQk8i9zk_KN55KxBSj_o-BW83p2qDIOCpx8b3uC61sCsYvgB9gWqkQYn8XbncFvehDwouulySHNowgf5PjCpMP4Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7TN4N9ZyfZTEyfhGaBkLJZK7_YzmBM4_43DX8swDRGjhodW1VrIhytpC75f49xU1fVe0eIysSdYd5JBgx7zMExof-_9GvOtkqaopxCJPxnv_uOc91wc9vP2DGrUyJ7RQSm7z-PyvtqIYKX1TkTmp4EfX3rwRGkcduxgyZ53cZ3UnmJoapNUMA3oZ-jlfyfW0v2w8MSGFjcyjrj7_tpX9qjTaG0MIh1r8FOWssxG7QfuktUpzqatEMQYLiozl8Ehd7e60Fm_kOhBdl9yLTaZsml6rS3LGpOJni70Vf_ppjgHTK06DDpnPDbiFbgh7v2JU49PZCuYyFelemzWTgXq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPrpZdgyXsYgE2s_C_xwTgqCFCuL6Ghu3I18_iKeuF2wyp9u2r5yaCWUeaRWbxmJ-MkEgqmBzBOER1T3bt9kq0Fx7Qv6LI1qeKoEt2rLpEqOeGJoejj0FBAgmCisxXqwLZBKeNm-caSicP2ObTY3ms4X4OJeRmWQ2BikR-VYJ-iARNytw_kZVF9bJnuGgXXTt33cl8C1ZwfhfL-spIzRtByNmD6hf6Hm8t-uwJWF4-zzoDuBN9mcX6Cu4Xb3sta2TUls8UcP2nehjko6JoEZhRXE5qGIhHm0j9Ro7rGG-GUwNfQzOPbGgXZe3Bxeqpc3ubrxH7BxRqeNsYEqVgsf0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
فلورین‌پلتنبرگ: یان دیومانده به‌سران باشگاه لایپزیگ فشاراورده و میخواد دراین پنجره راهی رئال مادرید بشه. مورینیو هم اوکی نهایی رو برای پیوستن ستاره 19 ساله تیم ملی ساحل عاج داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26472" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
