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
<p>@persiana_Soccer • 👥 596K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 00:54:15</div>
<hr>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BCD0Xd8yhvxTAPvNwu4IZC_NmDEvmxSq8ecCdw7kEujYODtaeQ6zMRKygbQYIhu2L5i4lBjwe_85J4mv8pWR4W4w0emT1g-IzmWRjG0Oydua_OjYRzmtc0kQFPjCJgP7AVH2ITEz3s7gfE4327NgBapAvNecLSPq_u06iAK3nNz_eH8twTxzZ59RKh42baknxThyNvhcBBxrd3NgZJcnUie2RCsR7nTqfGryqg02SDpOkS5hJ5DkIoZAuMI0xTGn6WxL_1R06p0HEPFav4_IQYHpylbRr2d61dSgJsGS1C50USA6VWlYRG83rTR0UojSy70pN2ScArlE7wJRttmd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y84w1ypiH9bDgdGr7nZLa-5QoVo1kgfEyU5k5N5f_GpHy7bQNYwK9rN6fEqntxM6hiiljGgCDI3DD0z621_pPuAts4Bbz4oCPMVXjmnBSE8i_yi9rGtKXsCmlycZO3x67Xa9sz5DzheFQ_7EFPbQrNjbvc9ewL6bIs6EMNVdpI_fAK6k7qac81ARyE7VWClND53cjCGbTantTkfZolS0IO365PJzE1Rq1PunJPVXTBY6Ml2Ol5oa2v7ZCrPsC66jl06psS_TBo1lteixQNOg3b-4TKB93q6FrAZ5tWeoceoNNK4i_6EMvCtW9Y5CbRDxTSEkwYmNQOlZoN2Ah8v54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1tNPGw1lFqIqi4dHtxAVhY7hGhq5o2f-ZjkEJKsskvX27yjIt1uTAorD9GrMJhXE4BcNSZWbE-0kE6shLHBmiN-VIDsKQSBfMQZlAi9X894gYuu_lyMmBt2vP9np5cOcF17IGJ2iLPejdX_hqZix6m_OeE9Mxle52Z6pCEGjroYQG--DGiLU4aQrhG2fqDw4i0SiIRFhgO7KiRQfX3ckfVHUveExxo0SD0CS6xz7iBLGRNCYLhawTJdQIANLeGIDW1GKYwBAB5_uyf8o-1VYnT4NhcFXuvjOJDYBbiJwEiDHSpV9K-k33zfkmYaM15RZOqJuHUt654o-T0A_aUFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cThRrhtJfJZcDg6P-4T7xXjJHacK2GHjDP1XIWT_qmj4ejfpZch2hdhTjrN9E2_mw0rrEBTYmdOLZqLrPcgpTR_0_Zs2bAKg3LLQvZBJcE0FbVej2bjQnPQMQrkwS3qNKikbjZ8vZSKCA0-o3q19C6VGbPssnCxtatDoLT8M7IFNnVKO8y3T6SHjJ9-_5lyeY8UkyE-gDGY1PIXRguqDm7boiQHHUNlHgbdU7i8EygZq6jMNHuAKKsTI_mnu48DOd8DXQ0a8U0ZqFptbJtQBhNzh6pNxdkBzU_XqdR0vBIMFK2FUkma9iUGKNrCPDT_J58qPu8FKUg4aynQwlybEIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/persiana_Soccer/26580" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WERtbrd2RhFf6A9sDJHL0voPuVgtHSu1fCOM_q4174IqZI6M3rb-xlMJJUFybN1g1Ac82EvnOVSeS0zUnAWSzHvfgPigQLkwWctvRgqAF_LNzmEzGQnx2jMh_Upr1fcd5dajTS8cUrvgFZkNrxfg9H1_0pL3Xz0U1YubBMlWrXrO3Dhc5l-HX986hKogcyAMFe0utaRyRnh8FXf_EfoeXmQi6aWiKBmK2G31PH8yFdanze--01qdxXGcBrCs090PLDRCM6kDiW3MOUcVjqSuXZY1TdW4yu9nZ-zFxKGAMI7cLa6Jt0gv80pn6YN4GdMLeIGbKreORO_pawwloZbZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdD4-cWDITfS-FRe-AtfjsfEf5SVqxOOHGksCn7BGz6p-OQ-724LmOL7k07BrVnomp2LpGfE-yqOoPJZw_biIxFAS47uyNyr1a74_zX8urtHxdvzMxGdw7O8Z7TNrZ_pQE2Pbf7hALqFWoupl6k42jPXw-Pt4UqjptTK0PtndnA0AgngAwHc2pmJjtrTArHtGYRjiB9RYiV52DtdFWWKRyqlWM4__X8taDR0y1OqIyAqX9evsGwCdDprCIutU02WQ7F7y-f3dzRyTA2vrcDsT8bWNDo8GuSdOKtV04J9yr1w0qczOO4xAiT3ZRpIfQk-JI8tAQ_ovp4RrkhMxBzJKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26577">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKwevw1H-CkknGUWOqtfn-aQ5bT5s6fllVvhFAN11d0hzENx83OqTpTEmoa40E6X83oOdV9XkmjyN0Yp1Jqvxa5C000CMcfUkdd1ia3f9hzVOHf5FzyQGQ9w-LrGw4nsqSCzlDbiaxiob7sEfet6lZSUUCr9FFmWB1RByZIZXj3mt7F1w7lknkfEkAKRiL7_tfm3EzSSTtW38pAZtY-xgC2U7tqC1xV2E-93WgjVIGInI_nm0Ejgg3B3QVMvmhnVZfF0jFrZnKdWgED7Bs0rxTGIk0hmsP2aDS45836xE4AGuAdSk7ealfReHPcUn5IZasZjjqpUMvYc233D36d0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇮🇷
محمد قربانی ستاره ایرانی الوحده امارات: رقم‌رضایت‌نامه‌من 2 میلیون‌دلار تعیین شده. تا جایی که اطلاع‌دارم 3 باشگاه لیگ برتری به دنبال جذب من هستند. خودم‌علاقه دارم‌جایی‌برم‌که فرصت بازی بهم برسه. تکلیفم ظرف یک هفته اینده مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/persiana_Soccer/26577" target="_blank">📅 23:58 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dn5rHbb2iDJYtqEZsWL1Wi24oFbVUXj8w6pNjwpZaTUmnMCn0kZD9U7LDolPVgLL2r3MFkRRUQnD-pCij89W-4Mclktzq9O3hD-o8vU4fvcLnFryF_uoy9DTNd1jjTwT_utquwlNBUIfoBrTXGBBfCG9M6Ld0euvGnAGcjaW2FgzpFFK4B-tg-IinjkCztwIlyUSoJ5rUguP4XRyZJ4Dg86ccaGL0kaHK-J2b62qwQRYhzahYGcazQe6ajQ8bFRbVrabB1fzXP8BFUxBgr9oOnW0K2pdTLLm-0UNgUwnMwo7nzGeH2V2GrHc84LMp6jLaEyIl-yPfRPppR7aKe-rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhEHM7pxoBmg-k8u12Uxo3Uimsw-86XV_ZBKTriqzD14H-Z1vt55PT__RPpjIyYXcsc15ZUx2Ce185hoCo-yr8ThoK-Qnm0NGUbabarr6ycE_EwjsN1OlLRJGSCxGELOS9C2jKViheBO_bRkLl_MN3xEn1kXENngDC1xMCJw0rPVQC_aDi4kH2Oz3P8VOx10Bngo1xHVBaAhWzNelNTGFQmbRJ8Sm0fqMxUmZpETsX9PpQ4e7sOrq93DmodUT70dv5LN9Wtlg_Anf4voGF3rW1P5F81HtqkpAbjrNMLLG6qBosYBXVVWSxetknqTOCTKe1zPsJXexotglNCGOfQdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgcfWqFQGCeTroBY2gUDtGkBWlJI0hQgOoZwfGRLRpAMbaFsVSrvrdXaboRJTLimRutZLpAm43RFcmdX6kjWrcRRUtkjJtHJUnPv0fVupZ1RrTyu6sDXeg5Ey2FaZefNaUS638OKiFmfP6syWuWinxtAOGvy2uyiPK35bgllymWONJniperCCQQYxE8UkUlpJGUr6MOi_sBQm57Qso6O31NoD0p-I8REbxlSxTHImuL-wFTuOwylZBRqKl0XblJLy5U2Eb4ohuMLdM_eL2mCX_R-ItRS39HTr6VlO7ggFkGJ7Foe-ybvqNyJkXFr8J04IbqQTu_JTGrMgzzwvkxQtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMpThjY06ZQsizDoIW9lshH_4VfpygY7tJMqgUs21hZ5HQpRfIqEcod8fMlZQXgMhWBj0aGgiNfEGuJTGS19ZyR87hWmTPzpurxkU-6ycxdShA2bhRh2A-5ReJ-vKLDoOHR9_z3sNH3mlWtfVvdYXxbcp3H8RAxUCcfNB5_lr0cXUQ4gP0MsPFXG2mMhjCWCtIU9oJqy5Gk7JUqSm9SnLDlTbOzEkK7AwpUeH2lTa6N9sswNI7yfAtmFElJme6Oxr7sKCd1JKPgayKSyPESwX4RGbH5HBQNvMow4DCImMjJSsbK1ifmgA-AIjpOEnCibHOKsUUP-rlbdQXFR2YPy6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGc7AFT-iMdMsBazX232IouRdsNmL1eWG2X4yEMcXky3gB93wQPpCO6K2Dm0UwJ57RZYKgnHv0Fs2s7IDI0JAhiF3cORjhwyLx2m9dvH7sBKsdKHmFKKZiSMUs0n3MOvEAD2yva1-NIHqOxBDUvbUCUP_VGCVtur0HmMcdfNE5Zqc5MC0N3Hx5Z-6H7ne1qi5JVB4wa1glqSP-2oeNzpw3qa4BdKoSpnNNi0RE8W2F_NspKm7EaSCoZWpuv148qNI1lQ4hhAXJIHkLUHafTV9Z_1xxlpVSl7A3qIdgA35XTT0ZK91qC7YrVHtJl91Deuw8b8Nw-eYEKrsuaYiy-d-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFp6xTPwwDo9OQXlMymoCM0vT_d6hs-e8KHXXvZua4wG2X4s_lUizT1IJJTm0KZcFBUSw-4YLvlFTzgzSFKzpyrhYU8E3XjWIPMoYo6RS7hBwZGyIFYbwulC4p2RpqWkU6Xu1SZzt70KA8LbNVI0xSUvM03JUM5cJ2Om9GGo8f0Lx5BVhkObNQhxwN0PzuW58KFa8lfNhqXzRINczBDgGw7Gosrdh4Ld3pKs-rRESHKa6r1neOo2SPdTXsJv_VFqT3iQCk8UKd-tebAa1OMMeksqkHjzhdgdrVVwIO76dDmBfLX4UD7FaoFWIoQMcoHhumZ1CJR_o5CEmDmyy3_-vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDZFyFhLC7ZMyUfwXZl-QJhJTcgoz4tOGdOJX7WmAiLYSbzbr38eu96yRNvy6gWqyBA50VEKNp0Aa3SWkNZniohhqDUXIlXdk9H4VWvC0qJtX2nBms7qZCEwj76CiWfHwG-wuFIBvWLlg7I7QX-PI99rBFw0AvPj2RB106pPzVmExqp2euCmegUEJFuYLL5SuqyU31Puia22kk-ldPolwMvQWUoJMdEGTgslrkJaT6XNb63CMPL7vGLFZ7MZJ5p0tZvSfAep3Lt-lmu2X1O2_vTqlIHjrYRoW2MZJuKe3R5_MJy768hoScUGjrHUhHQFvvKE85IZgIut_yKbFzhHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKfARVaPzLqcYz9YwjHm-qpyiFyFp1xAenj9ZCscACUM2ua3AzGSu4IICvf002d5KhI3fmuZFrICbazASxLeREznPqvhEw50acdGRQYiADwAhjFxpDMgLEOId_c5MbExDoMQeMUBIu46Pa7FeUBUmtBPNDTxHsMoDoGB1wtwKHkLWVByHab_eXTgzsXVYGvxUjBQmkdt0kAPwdTVh0ytyHLEgBz-9xCqdOrX56RCDC-6WSKEHKaZ24VSIyYNR617ileSH2enPh9ir6eqe_7n1Mqw1xJ9kbgtVZtPNMreOawtiLvPpRbpqQlxdqlZlv6yEAmwvBWrixHhtTfUx-GVXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xhues1riFAtnITQlE0XVG_46o7jYLPUbzrXJv_Ya1K5vX3VWI8LPLznrQRlvDVrTgYk3sPv3Zu6_PiIa8LRMcjebhlBUQAtcxTk9a6xgarpTohTEFbCd08lZ59rrxhRHmrzOONg8fjs6CGjvF-M4JLihnlyoNrrKDbhC-cGfFCQPaSC6pkkfgot9G4IEJPtb654UCeoquP7XfXgYJxcakYjGt7DW1-WoY8QrRAwTGXvcG-1oO7rU8gOug5d2G_--laozCV-55tkYrSgzi417mo3OR57OulFdmhubXpHLXVeKewis0U5NuVtubIMtK5PQBdilPbs50U_-fqBTFYtUtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooS8sSfd_3a_gFTvVI33Z9OVKF9tXlDrnwSYVoeRSceCkFBfHoyT44KhGS6r3HDnViWfkGHxPVXofz-VorJ98jab1t5BsEctVzHzbPiHquqgAvjhp8wJE-lplrrjVli8yV_p1nM8zWoT4dXCiyVwq2kZYrCyop4GDSu0IGcAARNW6yMK6V6tD3NfVwHpT5qMq39XYSzPvZD32q7V0R8wUZY4tbHjLBypIPjhedkWf-r82HC_KVW0G5V1neLY0bYY8PbFF_7quh2OmB-XmBFXR0XMluZNt__Q4pyF7YSWCtDgx2aEw8vYxCewhnRajPoQN3mqKdD9z9-z_9XG2Cznlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=Prr34NRaDEQlZsXpAVf6w4QQMe7N05hshoHKZSKuy2EbLyfDjusFEOioANxjDo-g2jy4M6Yixje1UrpH9p5Vms3c5TxhR_9etmHDaeqh56tCntmSI0qnvu8MZ40w_UgxcjkccLRACYr3SryeowJ3V9bBIbfMxBhnPZ-fzEpp2yLu-q9nRlQbGmGQQqedCILNqtA_PfXZrwRD835vAo54mHjCYo62y8kDP-hi4CmfYPp2GfJGQNQW7HdCcBPi350dFRaxD1Fu2K7bPgd1IBQNWriCjL9RqLQIrYvtJSqzaMxQe5qHpZv4FDycq0mpqhZR8knoNiBNgNEZvmbffgpchw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=Prr34NRaDEQlZsXpAVf6w4QQMe7N05hshoHKZSKuy2EbLyfDjusFEOioANxjDo-g2jy4M6Yixje1UrpH9p5Vms3c5TxhR_9etmHDaeqh56tCntmSI0qnvu8MZ40w_UgxcjkccLRACYr3SryeowJ3V9bBIbfMxBhnPZ-fzEpp2yLu-q9nRlQbGmGQQqedCILNqtA_PfXZrwRD835vAo54mHjCYo62y8kDP-hi4CmfYPp2GfJGQNQW7HdCcBPi350dFRaxD1Fu2K7bPgd1IBQNWriCjL9RqLQIrYvtJSqzaMxQe5qHpZv4FDycq0mpqhZR8knoNiBNgNEZvmbffgpchw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiJCH_9-o_I-KfU8hMwx8RminURe5qgAq6RNNdCIaTyY-m4g-PitIBtZmR6hLRJvfycAV4Osf3If2QusbKfZRbvq3e99koFFdArUxf7euPGkP1jdEy64j-KFqkpVR-0xq3KDBKzlzRJmh45-F8awq5x97kehKtn6UP0CzVnQVwAAp9A2nmq8KgHIBWJWseQxi5mtGmkmeTiz0C2WvB8x3j0AD0td4hNWtXhWbaY2fkQv8Svjn5K8ItxBO_eTZhKxoFw3p9EqB8hQhEE6PnXgv8AYlqw3Lu9gwMmWx5HgSP2fDHGlk0fIv2pUVlxt4WMTdgXKLyqkTs_JV8ldxd7T8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzrnZc3PF2ZjbenaLwEfwRr0ifU95f-LXQUwROkdIGfgcy7x1tGhKqZE-qYJjQpNM_ZLNnjas-vP89S4Fdnp0Euw9Laf1VtGcBHshDSBq4__4Ij3RrK5kJvGypp640Bl-6VG1B4cTdw8G-G7l0IA8wzvZ42POH1exwv0tOJEDh7D4zoYgtk01iOrsEm0Rr5XRuaNdRSWgfbRTUclTfO5_4CbGkipFhUYw3QcchpC_7t7S4qEdgp9JvGlREQ8mmTHFjgkOBv4zaVYmVJEIk6Lja5vPBxvOvBCElkrg80AiMMxst5-diX3HfeiA0_h-MLjk8TDv2Pso1599KHsKnFVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjrIlwwzjYCy-iEpbXe1UdW51TGrbHy8uLuod6Xo9JhYlmBRPuZFNKReO8kl4uXt1ELceVv7vsrJ_sEQS4CfPpOyq0gFSqMmD5Ps0ia2XimAogI34cVEVylrou9Nfp5_-Uyxt1woCK9KOuWK53uhNGEipy1yLr0tPW2CFeNCtGfjP0ArEOk6q5WUsLzU2qIV5R_jx1tQtPPRR05uQfMkmALwB0fbkN2yl1-RqCIJ4ouGRW5TOZLrvUQ15EobCmqAt02E-nFhoKJi4NVwQNH6ET1syUsCm8F8h4-pJWWWgyWXgL07oC1A5xRFVy-nABLabASH5NFmsspUBT4pShCnHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2VW5LJvz0BUEUutl19NASI6Boupbja26bx5avyWVUEeXIRrVN6G8tVQCaX9aanxLeJ9_YOu6hFTlyofvG_gOM3gW3jWd3dZR0me7wx2f_lwp-LOEsA6DgCxqCfgmzrMh4V1wo-8tyMmXx5QWADxgJn6Vf0axmt11OJF8tPReH1D1nmWOu-9FuW-pBOHRCJPjeolWqlPWTKAmyvATvwFQ3EQVK28Ycnwq3DOjYZQbw6VI6JP0UcNM_7MWlRmXJp2TWiQiY9aIV-QBhfjWiNTjJXTD3yMQfsMN7LRxTs5A_YwlOwnvR0uvf3MyCA0Th-uaRh1nGVDvMD6xR6rujldPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_sbgI_3m5iiuF1qwdZCCWHQJDzRZydvEcz3-rQ_U37iX5Wqs88AaDA7ApNZbGxsZiWe_8iitLuQq0y_d2GCbTyiVMO66kG-mY2sZ1hCbyWpTB6pIoS_si6rMCBlPeElp1K_INKPjKLX6BQAW8SQBS7hyUSQgKtYZsCtqz7lwpNmzMXOL_WqpSsttvHBkzFBX8HN1OUIqB8XNjI2weCRQ0Ml8P9kXf3hPlR3czJ2AimEIyMKtvH3Jcaq4BxXwo1wqEJeQMpIyy06kpvmFUKVKZzvSST-QEFmrQyDr771N-KqkaNTI40WqNPVfL9BfsPIxjBYTWZVZZaGKHjSTzxceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26553">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spAe5Zw4JmryIT7TSxJ4faMuko2ehzuzV_gHzfI1eVeXEZgEkHAv5jRZ5lYH472lDzfXvMbe9YlBFV1vMeDC2g_0BpCiqgitkAYM6cP_CzG7zF-NX8CQ5tGW4MmuK8sHP2pX4GhV9Nvm485w8XxSFPUt1zNhjiQZlNO4oHFQvnIsKJbVPU8u8befCldC45RLnzfyVKqtnBZi4AYZFVGd8R86_duQOFbAs7LpdHcN5gpOlbwIMKlkFagQUa4QFB_3uCBfES4c6alZvj1DQu6tNswQp0IqFzTK5ZXHUx4BFA4qhUqqpWvcqP8kSzH1v_dNYxqSy63pKLMhmEYK2MwqsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26553" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=b-e_2oXw33rXDKWTFH_0ywAYWsd6WzP7Cr_95KNaKYzjpMcbbCP1UDphdQNy6lP7bnK_jp0Z5kFUh7qnUbiyedfrCOSdjb325gaFuMSAWkfSzIh99tj3JlAwIW8gpgUMgpdj4iWZs1Mm2o9G5G5nxxtGyrlV86LqZmZMbot_OqerwNTMjYBwwybu-zKsQTeyFIJSbxgm3xe-UYY9y3lneskU1kZ2QpUC4nJYindVzXHumi3iHs11mOE4ennCIu4lV9cUtZ7ZSl_YC-pDRffpoZ9wZrv0MW6j5PZO37ubwTmfNDlVu4TLyrNgX3OKutrim-I-QrlV9DCSRmb60ICAEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=b-e_2oXw33rXDKWTFH_0ywAYWsd6WzP7Cr_95KNaKYzjpMcbbCP1UDphdQNy6lP7bnK_jp0Z5kFUh7qnUbiyedfrCOSdjb325gaFuMSAWkfSzIh99tj3JlAwIW8gpgUMgpdj4iWZs1Mm2o9G5G5nxxtGyrlV86LqZmZMbot_OqerwNTMjYBwwybu-zKsQTeyFIJSbxgm3xe-UYY9y3lneskU1kZ2QpUC4nJYindVzXHumi3iHs11mOE4ennCIu4lV9cUtZ7ZSl_YC-pDRffpoZ9wZrv0MW6j5PZO37ubwTmfNDlVu4TLyrNgX3OKutrim-I-QrlV9DCSRmb60ICAEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26548">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a750ab04f2.mp4?token=r426Ngk6YBP4aWwxfc7G3T4ZAUB3mhdBd1NeFUhrUIPNdvkiCETj9eg5TMZHfLATP2DhfxQQO7SveQ2v-oB_vkTEn7TfFLcgiGlQKMo7QhKsDDKesSUewshMD5KxLX0Vd6AWqlwDtR7Nvkb8_LTy6df8MAA0U09Z_tcvWY4QVe2wNgIjVq6XFzd4FiCOsL0BRB2Ts3QQKHAqfOsmclN4z_S-KWb1GBRiLqe-Moppa0UUOk4xT0tlrMXjJE4s-ciWts7ufztLhzBbzqXhx4KzimgyWqOlkufFNdhjEc78rXi96f18tUJUM6UyvavgMPrCmwySj3LP98YEy8kRgKK-gXikM9jnSe9E4QUyVC-hwvhxgYp5gMtsN5OyyujBYLY3MRJ5oDtJtlJ7pKQVsMafwq7ZLGye7cPGH3XMjcgwo4lT1Ico6BVLrwjTpVkKN2mNZQiOWDn5UEjN_LlY9C27UIU_X77ihq3OVQzXYu1-UHOP7POpSL2JhhQSuC8om1lvWSh3T21i9iyO7105yJ-BLw2kFzz3IWDhUvAtHUp6f0La7OeIj1BPoyPWgl9nsBmo1USVG1xzgW6kD8x0SNXdt0ipzGGBCmD0k4tZ_l65tz7n19ua0eMqDr-9a_6hgc5plYzOL1K477-GXoexs-7DEwdKDdPxk8AVYhbC9vuoH5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
دقیقا 17 سال پیش در جولای 2009 باشگاه رئال‌مادرید درورزشگاه برنابئو رونالدو رو به 80 هزار هوادار معرفی کرد و دوران طلایی رونالدو آغاز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26548" target="_blank">📅 15:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26547">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjkJkh0qjA_6d4vkFa8nhklDpj6-vu5CknE__AK4VkZxn4et3YjOnLEwgNLDNecKj3CwHaHl4cinPKgFPQy_8ivDcZ9xA-60YNiwFLck6ZaMMgwmuVU5BPwzpbwpxI8QphSP3PEdm6yOcPtLJTjdHsZMeXQDOBpHik5N0FML-KOUUBTuFW_ctJLKmXTI3a0jKtbhjaxXGIgNquQNuh-qqoUCT3oAKx28rTMu-ZHrH9fxBm7UbCudMVbSt0sefxk3FvBJiRgM35Td48CBWNAL1vsAyUE7cZRPNGNyZ1DPb_eS4Zmqfoo0Z2VY1XMFFG9jvLyn9jWCFWKFWYQaZPlx2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بعد از چند هفته بالاخره، سهراب بختیاری‌زاده‌سرمربی‌‌‌استقلال‌دیروز درخواست تمدید قرارداد دیدیه اندونگ هافبک گابنی فصل گذشته این تیم روداشته. باشگاه استقلال ازفیفااستعلام گرفته و درصورتیکه پاسخ فیفا مثبت‌باشد قرارداد اندونگ به مدت دو فصل با باشگاه…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26547" target="_blank">📅 15:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26546">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWoPgrCrjqds4K2MQoABNBGV6ivdfKIznpVvNneZnNmdqve7YVYIt71shdCVRadwIa1VFsnQjGuxyK-7svyOHsn5YoRt_WYfLZcqdydZK6YwtPJglGwuitJWXN-iMBfXwMOHboDHtItBp6RecWPpZZpPrSDMLDUuBB2ODyU50_YjP39qVuF7VLKEt5BQ8TajfHXe28FyqaYxzWpu0diL55d2ljO8Czusx4QG6LQBHvix9sGM-qk0i42siYM6ezBqjSGJjodQzTYZqovw0jdOx2alVGYgRuIE-0Uno3MaIttj3PEGoYRx9C8IM9bL2Mf0vvwKKHL-qBth_mAM0DrKxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
👤
باشگاه پرسپولیس در دوپنجره قبلی بارها تلاش کرد تا مهدی طارمی رو جذب کنه و حتی به نماینده او گفته بود که در صورت موافقت طارمی رضایت‌نامه‌او پرداخت خواهند کرد اما طارمی پالس مثبت نشون‌نداد حالا باتوجه به‌اینکه در لیست مازاد قرار گرفته و ممکنه بزودی ار المپیاکوس…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26546" target="_blank">📅 15:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26545">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tN-ATWIqO7DTE6lumDKeW87TK-H2fW1q7z1dbyOFpP_J1-CLRY9pAvCfx_MvP0RkHjpprRvSdcZ2S5VqYXSh7pnuMzSe9CO9QKKwiraMOxTQJB0EZKNsFKqA7hERcKq-9Ns6OrkE_s5XteOq_E5sUO8PyNmwrK3EC1wLviPbHcdAPmKMd79l2PbpuFPssXQmbmiUN_eW25ZYeHYF5SUeUQi4Vw_rb3VgchjvJcb9SuWnUgIU63PxgC0hQsVVlxpLvd-BAg9PjeVO38BS5rdZX07xB4LJKAQMBhkbCCRh5Lt6JQmVFa-g67kRJsbd_ruubmBi_xSpjtLhVDBxX_Tcuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 22 ساله سابق دو باشگاه ذوب آهن و نساجی دقایقی قبل به‌شکل‌رسمی قرارداد داخلی خود را به مدت چهارسال باباشگاه پرسپولیس امضا کرد. پیمان حدادی به‌باشگاه نساجی قول‌داده فردا مبلغ رضایت نامه ایری رو به حساب قائمشهری ها…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26545" target="_blank">📅 15:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26544">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a35e208335.mp4?token=upprw1UNEd7HEEHlseFz4eG5UgxPhvph-iv8H2cZmmjW8SoNHJn74drm9ZQBnmtcg7Z8uIZSfir9-PU2yeRW4yS16wvZWpUzpgeTe58bwEF8P_skUdDCVJhsjnliU0PtSKk1jTp5jjuYbAChH8LfagDzD48OB1KaLoRmxwiiFaRL6JvrcWu9AN-8pGbK1qiLMmbt9c9xNecWI2B8PSQoK6Bh9ghmQ-2RA1lh5cxL6aRGPRmiOGFYAoGssXd6I4HfRnJbwu57xvTGRES8FhAHqxg3EcfAYaMPphxkM58YmIv2kou7weFeLMKZyeRsM4GUD7OuE5h4nzGiPTPIBpKPyRHoA69x_Dh2MxzeELOZ5AKYAmMwzLCWy4GkhWIrurWtF4MYRYmR9wHgcuY6GoYnvgYuXzAQbSgAcMrLnwhwJIZevzmEumHahECs_84I17Fz7WH-bYj5xArlw4iBERVzkPAgYz29mnnBuS0hlf0wlUUzvMqHKTBRcAdUnHsUyoUBw78JnyukxzTpugNgVmtlREsgFAzpOdtStciknwhMdjFDIdtC1vA3qq9oq6knDlA7peAJAV-P6dBlwDsozUovOCa4Iw5lr1FVV4PBu-vM5NIEDMOoC9ksXy5yp_hTWlP_g_80Lv1StfEDFlSLSt1pwQG7S0nyc3sRipJmzFCJEZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اشک‌های زنده اکبر عبدی برای مردم ایران درباره شرایط اسفناک اقتصادی مملکتمون و گرونی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26544" target="_blank">📅 15:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26543">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOVkt5oWbC11Gtq8YwTWAUq3XmCP1D8_VxYhNGsSIAEXYnuta6Dswv0QojwOqGqdw2gOoLkZCOLY6YSNGTKHOaDripBMiAGw87QfaMelVNghDWeZqqAZOFYwqGG3aHaQDUjiUDCCNalLdA6xeNPZtdHyCGlEU9yPfW-6imxMjjWHwmrtfIs3nbitxc45SGFUJ6kGLhdqovFW7fkkO0aPE4ST7plrAJkHO1Z9JMamDX1GuhxRt1Jh6r1mCqJpx_c6SRa5wEJUDahw1O2mpKLFLNthGyLESSAe0clTVtGjuGnAd9VW8jL3oSvG5z4J_HrqjP9i81NfYh1Wf7mnlMg6WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26543" target="_blank">📅 14:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26542">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g36of68ua5lMn12R2QEpJJfcdDOlHb4evFa_8L8iawR4te7QfV79cHW4ThVM25d60DeY1jT-m4_bOf6pQH9A3xjdTK1UIOHopF3R8FqTycxLR2bni3F8vOX5oyNB0nk4Eb99Q0QpqEEkV8BleoeLazOkdGWMvGTFBxbjnvZH-lCqeQpVHWI2sCOIEhzgnEoMQCa7NXZnvEuXi8eEM6NdXSLxRAYIZqtIRKoJPBTFgBZhcV43ikPvS94tXLnE9utRfu7MYtTlwgmS-qnsR7YjaTTKXFDU5afFcemGwcVscNq5jbXC5TyXLkOdefCO0AXaKodfqqAN-CmFwTN8rlbTpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26542" target="_blank">📅 14:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26541">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FASUWGNvYl_oCB02AJoVO2SqKjSkASIQiWOlXel2FcfeMAhViXL7YfZ3VYazBgE8LdpkWKXz5xIha7_JvY9BzEymRDv_3AOKrvzLs0eOuiijUtsdbnrdeyTdRUHC2bsmpDjaXVTCTiLu2fCqUUZQOiiJtd2acd_YZpFQgJRdOP1tsdML56OlctGe5gRilYKx5AfMtEb6JZMkwgLGT5Efr8kkok3SO_uYi8qCiz_yGnwJXR1CjwsdjCy_4Wxl8Q_OLMAXMFhkCzW69CHgETFE7u0YNmrkadUQDFO68DkkmIwXF0P7LZDba2Xom23RWpXD9HFk3pXhGSonbw8CKziF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌البانیایی‌تیم استقلال برای جلسه‌مهم با علی‌تاجرنیا رئیس هیات مدیره استقلال وارد ساختمان‌باشگاه‌شد. این جلسه مربوط به تمدید قرارداد این فوق ستاره آلبانیایی است و ممکن است همین امروز قرارداد آسانی سه ساله تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26541" target="_blank">📅 14:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26540">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpXz2VhYRwVLswKz5WCKkVjGJ9wthITakWLRs-dZ6qBZE3ZH1omwizDT2yCkWMgsew_EHE1s_WMFS7ge3qvhtVa3WQqPsFGvJrTqamZgIN9Y2OfNmmbbX7JS80iBpoeRdoDYbSgnJcX4WEjwmtir7HPjICFCDag1gFmBuLKs5uSrO5_hxdzgpa_LSYqgzmm-zZgI_XQw5Fd0w-NugxkFIqwD1RevQ02q_8eFdbDhKt2n-L19cwW4DCh-AzggziInRk0I6GTlaD0Zy8Al3Mkz_RiLSp6wzZ4JrWTjPdJIAet7RnbXd-kbrc-LcaUdjZTKzy9_jmW_GMRe6OFSSrvpRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق گفته رسانه‌های یونانی؛ مهدی طارمی مهاجم 34 ساله المپیاکوس در لیست مازاد این تیم قرار گرفته و باید تا میدون آزادی بدوعه برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26540" target="_blank">📅 13:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26539">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxgo050yNTgmG1S6slg__7ty9lhixPzR8lPW-Lpfsvs8PtwUv44tVPzzvFAvEy7Tpx1t8K5CWZK9jRqnyzBVboNZvqO-muQT2GwWvrZV-TvXJQ_SBRb07igaTXVhjLoNxUgu6sV62VMlc7A5gHiP4mDpi91ObObhwA7yje9k5-an-HaJKo0qCHiMG_dDiFTNYauxMvUva47sInY_UbgWsBjjya_gvEw3PflUX_yFCl8DrvLeMVYGqijazECWuM6OE4WzacjoLqdM65zdy-WOBf7vDWEuN2sj-i3TEq6VWCNg3JcE4WJCKGPGGJhaY6vIvor1Arp22F1N83OZ0G00bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مهدی طارمی: حالا که دیگه صعود نکردیم اصلا نباید سوار هواپیما بشیم و تا فرودگاه امام میدوییم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26539" target="_blank">📅 12:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26537">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=bNkWZGDh8tnQW33gMTIrrFlWVh7n7PrBMC6N9fVeApq60r_BszL1nAo1yRqSChuC0Y46j2R9T0sbqdVfBjs62Ide1D_v8p3v7K-X-0rLpufnkLS6PueFXBf2pC3acK-LQp8XiZY490nSLqLvFimD93Lkj39FkjKRbd0WUJ4-Q_WNzucCVyAUWpCnFKjygxd0JjSavvKQfqNikluwCHU87TJ5xvjSDL15tH4TsS1GPSFCrPMLmjPgInrWV0mxo44F25-gCpW3qI2kteSBkqax86NLqWhZZaRzcH-x_N517GmkOHOMzDVkHkwqII9PbljMul7PzO-Ob-_vfm_o6A0S6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f40399edf.mp4?token=bNkWZGDh8tnQW33gMTIrrFlWVh7n7PrBMC6N9fVeApq60r_BszL1nAo1yRqSChuC0Y46j2R9T0sbqdVfBjs62Ide1D_v8p3v7K-X-0rLpufnkLS6PueFXBf2pC3acK-LQp8XiZY490nSLqLvFimD93Lkj39FkjKRbd0WUJ4-Q_WNzucCVyAUWpCnFKjygxd0JjSavvKQfqNikluwCHU87TJ5xvjSDL15tH4TsS1GPSFCrPMLmjPgInrWV0mxo44F25-gCpW3qI2kteSBkqax86NLqWhZZaRzcH-x_N517GmkOHOMzDVkHkwqII9PbljMul7PzO-Ob-_vfm_o6A0S6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
فکر میکنی برگردون رونالدو جلو یوونتوس از برگردون تو بهتر بود؟ زلاتان ابراهیموویچ: اگه تو فاصله بیشتراز40متراز دروازه زده، آره بهتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26537" target="_blank">📅 12:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26536">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnDX84vwDsso9q1WwkOy9hJR6rtASMFRFE1qvrupKSXC3oG0qypg8TUMPSCfVb7Q_FOrbihW1oP1NsRmFBprfsDN_mKo0aXy9nHyDnIxs_2r63F01gBt0pxc0TqWchlZTd0XNOZM9H98FLYD_u0gC5AOYLoDMFMskN6K21B4d02Cune4KtC9gbH0v3j_T_5JVnzvj-KWJnMJPBAp8UxSTpE09ycmXP_DGCjNry9fyCrZFZi-ZaMySjXlPbc_pilWqsdxUKMEjtpMyFRoD1JjsTQ-lYBfgiFGLUr4QLvw0F9qgHtatxomrQxy_Of4dHh22n5DMtVmxo70EYUklCdoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26536" target="_blank">📅 11:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26535">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_XOQscwv4QJynUJ5kQN9d7YfSgsISGVMnm2DjXRpqTjxceXj0TbcsRNCkAN69obRRgEbk9s0qD71VEp0oXPNSnFqaoa-qsvz0cHU8PuquFoA-BmhLVKwTMvKddQ2KI6gL_nHxZm2vz3dJLb04il_eVowZ2qFKX9UbHNg5i2czmlsr9RvU71jvtflqsYKyx-Qb9jJoobAJl7U5wYrSG0AnLfUwYZgjpjpjTRMZJPRFyks0wEZYDnWrogyyzLYrla_TZOzJqOJce_HTrexaRWvV3w-uL2TadJoJOMbyq2b_SXv2df2UYfduWE0L2jU5Ajl3jlp0gaVhJYWqsP8cueDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سعید آقایی مدافع چپ 31 ساله سپاهان و پرسپولیس برای عقد قرارداد دو ساله با مدیریت تیم فجرسپاسی به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26535" target="_blank">📅 11:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCEaNw2mkb2UU-zNBhnfZMM1UQ9W5pdBndbNcvfZIZxFwtCfeOqo7zdjx3yBssoUt66sdMaUQ8F3A5npmu5OO_WkDXg-yrrLjzct7A-Ikz650yQGSb0cCm0R8OkkPcCgPMGpWmQVX3eXrWcGco3ShCoMLTmBFAiMH6UGGjF5gUAHqIwn4tQZd2mq_uoFF8CcZ8Adq4h2IYgKtHtLK3Z2SjG4H4mBrJz5O72PSy_mDUiObAxiIm6Saeg6NfCfc5i0y-IARZKVAJBjv5civOFehLrxuuOyl8MmBlh7dTyIf4CFHqPOfNZMlFM-02zZtmANU9afrSzhiwgUMiwe_UmBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مصوبات جدید سازمان لیگ فوتبال در مورد نقل و انتقالات در فصل آینده رقابت‌های لیگ‌برتر:
‼️
افزایش لیست بزرگسالان هر تیم‌لیگ‌برتری از 20 بازیکن به 21 بازیکن؛ افزایش لیست زیر 25 سال هر تیم از دو بازیکن به پنج بازیکن؛ افزایش سهیمه لیگ برتری هرتیم‌از 7 بازیکن…</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26533" target="_blank">📅 10:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26532">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKH5hc4u9TlKxbvD1eQvDvPthO-uJkqogOCQV068kfu6N-rvX-G7YdCIV0UrokG0jQ93kPyRm3aka8LJcf_0jKSr8e1XDnnsco0ZavOUuTFTjIZhJWhhRB6e-L7G3q0JWyGa2m7OWXvVgsN3JYr0GVLcK__mILG7Eeyj4nSMyGDyDDAvO8F5JSlpInLZdirjyeTwwZgETI7nV81Olhv1DQ9IWoGBIkSb9F4KvyjDwCW2yMGXkCDHw2H7vadqRkR0C9EXkVCvFkwQEUZDl2jR_QMPGC1P32Ru7uxR-sHkkAu3PlB-tET4CjbkJVYhE_fwqd9Iqbe55QigcT7rCuln4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26532" target="_blank">📅 10:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26531">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qp1ss1VZxRVZNZmRMol-BqURsEH4pp31zGU5Z5tvKaIMAGP-27FQLacCLR7YsDLTqqnXVDBK2LpW-GwWirveVlGbsmoQUhqGlJWJW3YTWXYJGmABQyo3GNbzQ0JBxvQ59-K58Q44agoQee_9jCxbgpaPiZ3NUVzHd1KPDNMoqlj2nk7l9xqHuyjHs60sB-i9QhmeTE7Od-iYjNrq_kA4KorV1HlsPdyOAVevivWNdX7CjUErIXDneRePOrL7Odey2MgyBB0S62iAUF21RET7-tTUS2OyJsbTPKjhGSby8Pn07p_xshzywnaIUHdHCuJCEqF1eOGpBb5kFkkGbi1frw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه‌بدونید بعداز زلزله ویرانگر بم، باشگاه رئال مادرید اونجایه‌مدرسه‌فوتبال‌تاسیس کرد، استادیوم و مجوعه ورزشی ساخت و درنهایت بخاطر فساد و پارتی‌بازی‌مسئولین و فرزندانشون داخل این مدرسه فوتبال، کلا منحل شد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26531" target="_blank">📅 09:40 · 04 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26529" target="_blank">📅 07:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4btXE90EuDpZHU5ktkrVlC0LcomaU5Bw-Cwnu8JNUTKCqkqjWY6zWm5mE7KYVLrHQ8oBrJLTotE6VY6DSMOc08nwzxdGH-otabZk2ncVv2rMZ5UW4MYzwc405P0tqORK0n81jU_nv0EOpodQQc331xOp24nUFeowOUXYloioExMUQxMEN1T5LxgIPXILGNkdbMxcJCVzgDfetEgW79EL1ItsWnAgZco9oYcxZMDX65-XYjqBsl8D_PVVAG644YkE8xypLznYbv-lBcV7pjW6b7GrjzFboChh41eh5fQzUShKXkMGbSUP4QQ08DSZYhwV7CYx2TWuvE_k6OYGxHGLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26528" target="_blank">📅 01:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26526">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txMyD6yeI7xlPsZWWn4cGZ4S_XnjENpsMNZ-gUWXo1UZP2M55bN29yyLBMSOQlptd6JWDCkiThH8c0PKym39mwZle6W4L5p15fYuXrFfhZBrCfRjNj-UuUwvIy9TlL_7nsxwBDd_WbCWCTHbpTKFpQxKMlLRhEGqBbleIdnq18a3aJWMQx75o0zqbhYdSFOK7E6y4m5_84rOVyTcYJLbCRo4o5CNNgmvDnNvSMnVEWroImzv0J5yvUs8Qkp9gykL9HJkeMrWaaMKvURKHil9nkGYu26i3Rg8kd5AQwNT7P5vBO61nqDlXtHo5C2wmSAN4l5CRHsMYuSaqvGQVFtzAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ جذاب دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی شاگردان آندونی ایرائولا برابر ساندرلند در آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26526" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26525">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fI9l2x4gJi389NcJo3xhYWlQQHmlnSWNt8ox6eiuKbz0Y95u8-GAx5WuQxtTdTTZZNmByNpY7k_s1GdiGQDmKYQ7qeSf5RpU65jDBgb-3OwlQyMp4TSiMmgc40ysjDYFHtd7lC5BPiff3TnOpoZCUZvEJvTlbks9VuuHdQLtO-UXcQHitPIH1qlRj2P94szIMg-biyWcGa93YewLdcauqJ8LZIUlTU71LS0466OutSzJtEZoNYVzpGSm7zn_YZUw6TjrqQOSN69DAulzq-iO5ZleInPHf8tbPQZapJKZKGptdA6u2KGvfuu3r-BqE_d9sD5lunOW9GJYOuCyLvYCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
توقف روسونری مقابل سلتیک و برتری‌ماخاچ‌قلعه‌درحضورکوتاه‌ حسین‌نژاد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26525" target="_blank">📅 01:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26524">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhN_Dya6V1EZ6HsAJbdi5S7GrxhWcIB8Rt0o3ze_k3FEPqutyfsn936T8g57sNFXJGOrT5zUZRQ1XLvXdkOf0OC5ZDd-iY5vnlM_qZjeRotvA27C3cdehRRYCTPIh8T7MbItygLOzFznHnjCGbujid1dwH386Lc2De4Gto11pWrjhdmdbivkAQjdTNHi_eKS-KWuLStDhpQpyBgusLXmpiZ5aXNwKfFOUvtaagmBEJ0Q8tZdcTjUi1T3HWtBTXhBcnk3GNnfMWvtQ0ZS3YtgwWzNUE0kCAvaKcUhdQFKdZAGei2eiKd3U2hzk3GC_fH557MZky8_Oal_hocXMNzoww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
#تکمیلی؛ محمد محبی هنوزآفر ارسالی باشگاه پرسپولیس روامضا نکرده و مدیریت باشگاه پرسپولیس نیز همچنان منتطر امضا قرارداد توسط ستاره سابق باشگاه سپاهانه. هرلحظه که امضا بشه سریعا توکانال پوشش میدیم. توافقات نهایی انجام شده و فقط امضای خودِ محبی باقی مونده…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26524" target="_blank">📅 01:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26523">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2hzERqIqbL0mhi4B_kbOW8-d6W3HfqAspRGPlOaVo4gBK7ostI5moxYjK6HtRyd-I0DYg9y2gB9PFsaaDhclMb98wtELvcygG3pzW8Uq1w3PvG0HSQSsUBex1CS6Q0jZwHSPjcbs32mieAtid8XbX_AoKZUJy98REeCcYXvupPNQOaGrWYDnZiOXK1BCgqrD4jKCZ8WtH6dhU_2e4b402hF6L1Qj3ofo3UWGkhk61EsbuqKfiFlvgfHq0rdrnmhxMRxZ2cbVBxyo2YPzXN6PulcehS_3KPxMNUH5LIus8MTUj7oR-5i08555qJJHOORgLc8huLMY6dMTYKB8XI0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
یکی‌از مسئولان سازمان لیگ؛ خبر فسخ قرار داد رامین رضاییان با باشگاه در سازمان لیگ رو تایید کرد. بدین ترتیب اگه پنجره باز نشود و رامین بخواهد قرارداد جدیدی با تیم استقلال امضا کند تا نیم فصل مجوز بازی برای آبی پوشان پایتخت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26523" target="_blank">📅 01:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26522">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvaORy2FjE85AByFwK67bXY7Hg7urmHoAVByg02Kgu88WtPz1jWm0oMtO2i-tgUdasJdHA3NoEuQlxRjtXVilHuc2pIg4jzYRpdtCsyrVO8xGTvAsF8AkpSRABdbwn-2qEd72hfUFG-GlQv2umMW9v_T9_5pbic_Dn7ZQdVlf6unJWUkvtvCZ3wADlnQRhAOcDWUKtILS9SwJkvFOkwy0stYAdWcasV1nVuwVuvTK-i41VTX8hSDgGGCKuUBlmXw-rGQU5JhA-ga2M8Md8zhzI3ug7g1BOwrnhjRiK8-pRGTjfWUG6hhQnmCOa09UF8GE87B4ckobgdtv-7HvxqCsA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=r46uyQDQmMEjkIG1apXpULgD5yF6azC_IwLV5YF0he-pWxIi01EnahmH-WLHhzOXOYwsSUnx3zJhHZ_gVPRc63117G0ucth0Iszpsyz0qoQD84BMMIwssFViGo_cNVhjvDcKNo_0yuA2Sc2J6cc1q3L-bHLr7Dfp2UCt-suvoM5hT9posNO3qyUEK0RUvKEw-c5KJ_buKpVaBK5G_Dz5U1t03g87T1owiujmvKlqOeNp-7c62IXp2lUze1grM2FXa5QpDeBnxKOK2tvmmTPyu8Qv8E_S6mbuJ21_sqoeHWyXpqNPWq7arw92sBjRkYv0flKI4BqIvLSI_9KR3rEYfjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34e9fb51c.mp4?token=r46uyQDQmMEjkIG1apXpULgD5yF6azC_IwLV5YF0he-pWxIi01EnahmH-WLHhzOXOYwsSUnx3zJhHZ_gVPRc63117G0ucth0Iszpsyz0qoQD84BMMIwssFViGo_cNVhjvDcKNo_0yuA2Sc2J6cc1q3L-bHLr7Dfp2UCt-suvoM5hT9posNO3qyUEK0RUvKEw-c5KJ_buKpVaBK5G_Dz5U1t03g87T1owiujmvKlqOeNp-7c62IXp2lUze1grM2FXa5QpDeBnxKOK2tvmmTPyu8Qv8E_S6mbuJ21_sqoeHWyXpqNPWq7arw92sBjRkYv0flKI4BqIvLSI_9KR3rEYfjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26521" target="_blank">📅 00:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXdzlAKI5i2LaW8vKv4sWd3CvPxYmLGnnpbNvcTDYYegKHzH3kGTDgRdhyUuA9AopTQnns0Zuh9XYK2h0-bqSGksdgZsWjefuryOCLikQUKgPC1rJfVrYKZ-jKSvSByP1ieCWd0KeDwIa4OoDn9sLtlSYryonL3W3uPYGw7UwOUnnPZ6wKgudzhcEi_q3Yi3bk3P3JNvsLl9kvcD-iLGk9ekqIrUBs2Z8DuG3zyyUpnztC7lwwjdAIcqvbv1YQGK-SRV80eDrbtEnEMtlOKSgwEx4iO5O8iZBvaYEhB_RqIK7kFXqwq1Y1LAH8M9-XNjwNvf9cTRtBMYZH4eD-ABZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛بعداز رونمایی‌از محمد خلیفه؛ اگر اتفاق‌خاصی‌ رخ ندهد باشگاه‌ استقلال کار های انتقال مهدی گودرزی ستاره جوان خیبر هم نهایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26519" target="_blank">📅 00:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26518">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3HB9C-cIMe9EMa4JjaSj4moyDUrLMcnEeMskad1W3cd91rqMfEf4RTunusnK5f5ktkRY2YWDITHGRju9_--wNMXN6S7QgPS0CnsuPwpjkzEcTfDmPtIp2VsdGGKwMwOUa_YBSp0lLjl2cuUARdMkr986fbRDbA2Du0PxSjXTLhFlyHyLbjwvBxYBM4juVdVQ1wEmS_YLL_aCWQwJJr-5VzCzdWRajBkzgNZI0602SpUtmgxKZbVKc-5bljOScwfD9Zlu__QRtpCG6et8GXGq0l-dn0EettEtAxl8F5u2KSxQB6C3mb0BjEW_KShDbsvG8OFI2dEsV4OcHIgUaBkWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
رونالدو و جورجینا هم به این‌شکل در تدارک گرفتن عروسیشون هستند؛ این چه سمی بود اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26518" target="_blank">📅 00:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26517">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqNdFACRk2BqePVapBzXmkFQl-Tvap_5tXNEX1JtQA0CkXG51wIpajorX19jvTBpf2YOLZGObWwff8WDyCpnSWCIXWyRoNC2qvWCR8nAK5p3Lkr1QUWnzDzsrIOirnD-4Wxa6I1JWuW_REk_LYNX1pX48gqTA6cqLw_w0Ix2sItqDf0MzbnaFsiu2ReiTLAYXfiPuRjTbAWKDSUKV8t60SPDIvcAejUWUBUdzAmUCoTaGjmPy0kpdFljELuAAbpGG3bIDfTutMdqJDFU180M7L8PhmQk4zylai57yKf1vYi3CcY4qbU7COOjuwnxmUKmO8WAI2LZb88F8c0GGM1rKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه‌پرسپولیس‌ازدقایقی‌قبل‌با مدیربرنامه محمد مهدی محبی و خودِ بازیکن تماس گرفته و در تلاشه که زودتر این بازیکن قرارداد رو امضا کند. به محض امضای محبی در کانال خواهیم گفت. دو تیم پرسپولیس و اتحاد کلبا بر سر این انتقال به توافق رسیده اند و فقط امضا محبی…</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/26517" target="_blank">📅 23:49 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHR98fgEgUoAqYS3DAP5MONwkV6IKXv6SUbhXGCf-cXqizPQ-GZUCMUFAZmRSpqSHtAoV2TxoxvETmb2gNAz8PMKYXBfzFhtFLFJREdpYoOGCNXD2BAK5kdue2F37ezODG3v-UiCeXJU-lhpoTkA9DCnh7zm8AJEXLNUSGFaEZBtmrbKi4mwTy0nTWRYmbF6GECmncWzp8KBafJLVMkcetS5THxjvYNXUicFelE1EBAi7qMH81dV2Z0R7_qtTZZg2IugrHLpGOynvZkWlW9IVTqMDl1aoohT4XKWr37up0S70Mt5vH_Qe-pH9S8nUw90XmlP-n1STGnrIrcoCOYWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26516" target="_blank">📅 23:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeGF5COYn9ffM7eIe402H2ahnzMZ1LdQszoemoD1P5cvpZtsMAWCJjtQaLRT3q-tfult9A3txNFTKAJ8NUHy-crNy74lT_GqZWtIkCjo6FqR8qmydt_OVEi86SuztatsClSh_tsx8NDf9CN33Tv2uFCWnqDHOE7AIstLikiKjNIlOXm27sIqJnK7hJURozEMgkL5I7GgIqtv09vsq81vUqvicqcM_bDrjIrIa2lsj67CFwRJWUdv3H3tCN9gTBa7B38uSKXcOl680AVt18OvAghW-QfcqbQPAGL8KG3ZylrvUsJ_o5ouEXzpcYEFLLINESsOvAaP6iPu3vzcv0F9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی:
باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26515" target="_blank">📅 23:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_UXIV8poS2W252Gj5edk14Qes4yNHzIPVWU6JxtHMv4O9QvvsjonyTgotAE82He1irTUBjv3jsugAaoDjeEWVKuZv-KVP3otMs34OOsu50rqs8EdUF6PzQhsrEFGJ0rtLCBvoKKujRcEf7WZpcAHrGZ6PCY93XKuAJC3gph2nMplrYEvl8AgYdm1TVdg-zittwDrsCQRrU0PKFpb1Nm8J0WEROMCQm_IEFFArF4GQOctFjMYlv3MRxpNcCI-1wUxwRb4u8cvZmROR76hoXI0reT40L_gW9a_SEXKvkmLtWCj1ZGC6yNjhkgFkWMfQxfNGY80j5fYxoha1R05uTO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#فوری؛ نشریه ESPN: یان دیومانده ستاره 19 ساله تیم لایپزیگ باعقدقراردادی شش ساله رسما به باشگاه رئال مادرید پیوست. باشگاه بزودی پوستر رونمایی از وینگر جدید خود را منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/26514" target="_blank">📅 22:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26513">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9F027Iepi2RNTJpK0qc6q138ALonp6ESVuUXLTrpTCPnOjr0bV6JKU8e7_4a21hF3lbEVslXVWUhh8OYm699ci34ajMILMPOOFwxhPKHJPiF_BNkcejQeG3BcYsWDLfQPXk-dkb5TrqTua01lkpy7Sqogh7CPaV96kMEGaijPAscBqYzi2y8ebibs6rRxp1JkbD6h8Yzu12AgGnGNQss51qduSygMfQF54knmAaLvpZN0eAYNzQrRzcpvq0gqm91AaUAUhi-d5taw6-bkfYaHw82p7ZJ3mTIl4bCaZCBWilLNe-0PGi5UCmVrPcLA_Io8M_jlF_twHPz2f5lbYo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین پیگیری‌ های پرشیانا؛ قراره که امشب حدود ساعت 23:00 محمد محبی قراردادش رو با پرسپولیس امضا کنه و رسما پرسپولیسی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/26513" target="_blank">📅 22:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0_GYOpjFcRucynTu_pYAx-BLO5oKqvDSaqIqLvE0etIjI5YghGFToU8T-yyD1qGbL-Dxnna_KuCMeSZFYnIZzNL3ucKcgJkEkAvcmugYExUVK_vgYWmX8ki7maseK7TcmqyP5wZoRjyhfYyoaKZ_xquXA2a9CS9Vw_pRKrj4Aj35t7Lmp9-JQW6F6APPdPScNT4MmJXPaVnJ07PnfpGbFHSTptw28CagjA7JrXsozj7kQ-Vyz8qaVjLKVGHS1HwwfF8ltXuooGWC19JGd86YGm32N1-7Os5ALpDdo_eazGa7o7ZG0bKvhzCWYBvwRWjHKIOE71AAfZSFKIcCE4EhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYaJcso49WgbPMtyd1sg0KQapUurDw0UtCX5fi4cb5oeR2-ChbiHGNg22UDbGHHzQ5DjciU7TM2Rdk_l8PRoEw6z7ZMtISbhG9BGlDlm3cVtTFVxHqgVj7SS22secUWOqOVsbzG2fQ7cl2ghekKmqJUYoex2h9A3exdxYdb5NEVpaRJMr_GgOkjUofYEviEGWyBiIIqXSbRArpnnBMv7nzmfl3qXnG-4hBdDa_F1GnDQgq9vGrW_IqWHdq5xp38KYZLbeafsaYgDBbZold0h-ZxkmHUwHx8PAg6FxGhEdXLfjAu8DX3XREQ09Qh5fQsZ_ZV3eAa9z4MbcwHQwQ8gdA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1aWXrbd44WceoXGidQDgrce5-IiKjyWSJ-P2v1nTrjcqMbtKr6UTkTMJCHRMz9UcJw5GQfADkqJH6_rOQ2kZL4tcBEvxK2899ElPVqNHPVMqylJvIouU1EcdeeZ3fDz0I9lJvy3y7Sm_sjoQ8wkZEliUalrFjzW8YuSwpelaxUutXE8WXs10LNFVPz5aorcIz07pPe6vT7PoEWfQJIbd_71Wp1VDBlhz67iFVcKNNr_853wPY_1yJH92z4dh0MAeIfmHW-zbDoY1ocD8ZvVBbyCvEE-dS7zpVQBp2PQLpbWGGLTbXyJ7yQw_wCvmjAFG3YT6uq9w5H__d1PTywTsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26509" target="_blank">📅 21:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_yceZg08YkEtBks6KD8Y-hybclobW5mnXzpxLZNUkhSu5AAW1FoC4Bt29E2F11lxH0UuVVelxUz3kDN8a7hzCnLVgBbqBw5UIXn7vckd-zy-AhK_DYQgfCN37iaW0Qb0-NmSh3Br_ajb90AfCVg0BA2Tb7RZMsF-ujDAxdts95_uXT_UUh7cxlWw3kJNzVldVnGYlZn5py_A6VKnT5PftCGlRIKfF8skV7N7vwTWqSkFl8yy9FtBq6GGaeD29pRPAsgvzAVmyAOOMgpdkQbMXyFHKXHylLCNgvCyYZeC_xaf2A91paJRzsGNp4t2mwJgqSiTC9gyLpU-R5NBEea6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX6SDqQ6ObJg4bN6d6XrjrASrV7Qitkfb3ikAhPiMoVtNAzr-gTJAV0BfZwUJHsTEgKEKL23CTE9sFjPTocSMR5tMeq6ig5BFOUEzl_XgfQf_6wibpdJuYUKpu1q_B5sBm0CnVItoHykG2TCXFfOZX42TkBpwuDOyaNKvxRWe_RRiENXk19UEeqICkRsAimg0RZ9-dfYlGT7_avz_N5IlBeKcnoLb8nSMxB-fT8C9Sw0yijmmeRbH6ZcRTolsehj75jYPE6l73b_D6g_ydMesWhgGGGaHKbZL9_TW_Dq1uRG3nxldrS7ltUUCgOmY3iX5GFZHfFW0HIpzWcr2yXMeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌اخرین‌شنیده‌های‌رسانه پرشیانا؛ مهدی تار تار سرمربی جدید تیم پرسپولیس یک فرصت به محمدجواد کاظمیان داده تاشایستگی‌های‌ خود را در تمرینات نشون‌بده در غیر این صورت او نیز همچون شکاری در لیست مازاد سرخ‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/persiana_Soccer/26505" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jl06lmVTsR_tqgrh4zC9mUMUEBWkfKVybrCKD9gYj-YsvpoUBHu765RshPXCB3cMWU904hws3lpjfyxG8nvQ0ONIML7WwA7Rdc9rFhVFRCKXDMbcpNeVLU5z6-tYbNbPjT4yONOdViOkNM3AVsvPeMGvXPnNbLQA1duBWEjsE9TFyiyMGNpXCAh1uk8b9iOYnmO_6euR0f3JUltnOTrVgn4b-Jmw1lndaC_qs0tyBNTTZCJTUnvnRi0ArGZyv9ppKBPM0e-nZvQXB-AQUYNo3G94KyBLj1N3Voh5ul-fTd66rCbWj5yjBoEwyrAu7Nz4lffNY9T0pokxAiQsqTbrZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/persiana_Soccer/26504" target="_blank">📅 20:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRwBrWdpGU4qSj4_f0bN_O0MJ27jp0S9-5TLa1ne35vbEqqjHR0Ble-zABUxZVZSQYudIvL_8HWkmEMTllAZz8FMC2um2dEdcwtXNozHW-yQOIEKbAT_hqj1Xel2lgz6VTlCczg4xGSPuFpKfEqxTnJDo1aNnWRuP2S3GY13halGqkrN9VuUEY38Pk48pmmR5jmUUqHYphO4jfQvPFBr-WIsPlA8hVmq2zDcYueyNFwxa7ik1JgsE9J8aM3eXNfg0V9GNDNGm95cfCNL0hv32HH0v73lYpbivsVSWHE3g42mSd9pg5epmR1pTajTvHG7H6h16iv6Uth1Nx2SUX8FTA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=OuAWvCDc7DcwaTMJZ9Ug29FsiGdrc1pjpF--pMUXt-irqALFJ80AkUsIn4fPnaieZ6ecD7fqTT9y2GdRKCVNdIGESILIv8wRK-cI5_JwCA56iosqsB-IpqlZKjqf2MSW9joV_2VAbK6VIJt8ubM5IJZdHIC-pf8ps1csJiyGHXVBJf99w4selGqn923YwlkinVNRm2ShpCkGC0MSIE8VegP2eQgdFu0ftlX2pQW_9AN7-JPMUXx88yKJX-wytvP24hDd6fw7YTs8jsnfaZymHKLe1F0_QwHNp1vOHuhk4644vflfF-yjlMFuCDa7WApHpveipFDC9m5noj4Ka2CShQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=OuAWvCDc7DcwaTMJZ9Ug29FsiGdrc1pjpF--pMUXt-irqALFJ80AkUsIn4fPnaieZ6ecD7fqTT9y2GdRKCVNdIGESILIv8wRK-cI5_JwCA56iosqsB-IpqlZKjqf2MSW9joV_2VAbK6VIJt8ubM5IJZdHIC-pf8ps1csJiyGHXVBJf99w4selGqn923YwlkinVNRm2ShpCkGC0MSIE8VegP2eQgdFu0ftlX2pQW_9AN7-JPMUXx88yKJX-wytvP24hDd6fw7YTs8jsnfaZymHKLe1F0_QwHNp1vOHuhk4644vflfF-yjlMFuCDa7WApHpveipFDC9m5noj4Ka2CShQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rDumj0xtVv3oO6e_ack1hjc_csYx9wXGIIfJyYB3zBW19tBtAGi_hScVBSFFRwKIe7V284eWcgpRFM9mS04rXaQSj1JwiZB53YqZ2TcwBDdZtwf3k6jGZVdCLVCleOKTv2h23PM10WexlB-o0seY0WFYzw9x4xZy-AIefJaj6gU78yLPP5kvtrt1xLCrM81qXxcBFZQM06WNoLgAdRknYtpZEEH5KIHi3sW_lxrV_TzMJuV_EZMxLLy3FypZgJPRighT0e_nuK_pUxd-j9mJAS9uV4drvrCJHxzLO1mLOvjHbNMIn-wbz2YoPzXBegUTY_LPt4GinPmH3QlL7Eh6Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ یاسر آسانی دقایقی قبل برای‌دریافت مطالباتش و مذاکره با آبی‌ها برای تمدید قراردادش وارد ساختمان این باشگاه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/26501" target="_blank">📅 19:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26499">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMfP21DXgtzfALWBW7k48lUax91IUhkcj10nZK9Ql1pHU0WWPtXYGxZ9hXApmrVpvF2Xl9Bur1FYlefBT73GFJyGcRKGofsMid8ndsoeQX4v3QaGuCPjtyADUYZ6Qp0KsYZ7zKaUL01xQk35hATPDUUUWWCbqebCeeTu4-W6jZZXFU-KUPSDiKJOa-ncdRtnG8hpAiWqrm_wR3c5aK2pd1xy3s6Vt4NsIWTto2EdNXHKJiuLyc1rLnN_pcFzTY6JR6aUcPa7-pdqiMmbO1i2viHyzpdhqF_s6ggRrN6tranCyVEM-rsFnjEP98obcGrszSwePaira-7u4xT3tjgLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛رونمایی از تنها آفر اروپایی‌فعلی محمد محبی ستاره تیم ملی ایران
🔵
باشگاه لخ پوزنان سه روز پیش آفری دو ساله به ارزش 1.8 میلیون‌دلار به محمدمحبی داده. رقمی که برای هر فصل 900 هزار دلار به‌ شمار می‌آید. باشگاه استقلال نیز آفری‌سه‌ساله…</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/26499" target="_blank">📅 19:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26498">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AozzFsu1IiHnTUcO06awbvXzmg9iGC0xOORn6pRlRqtSq35LiSfzdJcsx-AInX7Kd2eFWnQ7Io_PxzQvZ7Dh0HXnFEY5ST5xKDQX5VIT0WDEYUQePOH6eWoEdL8tcBku72Q6vPCYvli1UmIPukGIj8k1UgoQlPSrcbC-Pr4auIetMM6zKYLxw4X3HQV7TQ2MFG25RZtSr7x5GNVdF-KJtNiqoKTwg2UQ10QglonwTecQzM3og6OIkiD5Fkwh7fxbGTKAWhurljuhBowJUJ9m_5xPbwIiXrXTneYwsbIQn07z5W5z2E0MhxIJ7afok1OsUkPWRednEd0QFCaPlVkQFw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=tzLAhP5oJ_EWBjbnw-S1TVW5ovEW8Bjaiok-iFZNSxXbD4WIhLc33I-Y24BkOORChs_HHpv74Kqh-XsxObu5NaySpXOuf2SFuO5aa69J-y9oj9XIB_2xZlRmcnM275A7vSAHOZvWKEINNF8CURQ6iPZA4dSCq07J5kB5ZnI98EKv6dTTJSf6GzTEzsvQFNi6O0dBWRi-NgX8epQ7laZxw2T_l08KUBUEOtRoyTH9g6yKaDEbXoulc1EVMEpkN7xu5decSe8XmUhUeOm8F_j_ok-Kn1QtHdNVct8XjvIlA16RRIuXOHa6GD4eSi-w6Aes8ctPG9VL76Ef9CJR-_17dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca99cdbcf8.mp4?token=tzLAhP5oJ_EWBjbnw-S1TVW5ovEW8Bjaiok-iFZNSxXbD4WIhLc33I-Y24BkOORChs_HHpv74Kqh-XsxObu5NaySpXOuf2SFuO5aa69J-y9oj9XIB_2xZlRmcnM275A7vSAHOZvWKEINNF8CURQ6iPZA4dSCq07J5kB5ZnI98EKv6dTTJSf6GzTEzsvQFNi6O0dBWRi-NgX8epQ7laZxw2T_l08KUBUEOtRoyTH9g6yKaDEbXoulc1EVMEpkN7xu5decSe8XmUhUeOm8F_j_ok-Kn1QtHdNVct8XjvIlA16RRIuXOHa6GD4eSi-w6Aes8ctPG9VL76Ef9CJR-_17dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amUw0u5V1w-nxN1lD24iyjaiMqurWS0cpO2ddezLIcMyo_s5oP1-XixCWgStyRtH_0pnDae4WY5qx9lU4hZ0SUWEdlTfba3eK51bhvNbpg0XiWbFxV59Z_SGge03-oUp1_nmJ8mERn91rhNlkvQN-OITl9gz9UX0FUdduPV24B_rqtYyOC2I95HUEbXKfZe4E9pqQqH5IqiM_BkfhHDwTVQ5RhhqU0S4-3wlNCyWUGWMOmIZdnl2QTNUYF0x48-5hSy41gEG6ZeUo9SzIipZ2UrIIMWN_0RA0gmShG8pq292wenBOzKKmc47RZdJEmOGJ3Hs3jTxLiGNjZLQg8vLOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5dGSQ6jPnfxiuDU5UUAhIoMWEDOnLp1xSL4yM1aJ7NpxwJL0mNNOrDwxDpZ0Aeq6xYAU8wj0ZeNhjxhKWElrkRK6jZC-lW9U-jgOV3ajIWDgJYFXWut5kMFdFDvTywpbubJX4-5cGeiverPofJz6W_5j4I-ICKnI3_BmNaMFzzCACBdGNu-ugS-O7l0froMSsMa0qbTnhJHgkyzvEH8A2_JxWfFT22F9QBIWmqA5bh3870tXnOZZNrQjK5zbC3kvuotRCag490-pIV2LMRtftu4MVGUBweovg1pGBW5AxEe3wWOVMsUcq8f9xOplDBzFwemFwK0Y4qbsCe0kwDQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j8js3npe0dlU8un90Ba-YfbmPx-1mDhQZmGO-Wv-Tqh5PYdRdL1xjj1_eMKL2f40gN6aGAtSC52YPEFyEa3a4n1TVJYxNwyF4mtBYj0hyJLnyo5xHzSYkphcikaoO0ZZm8nXQNObCQ4k3XWOpw1w75JcCNwMDbEPHOoTSpA2Q6WKbQBTbkj4RZVfQsJP7UXzzIfdyvlDcumUO5MIJbRhzXB3bN5otcqJ3tjg23yEcYMYuIpbEK4Pxi-2yt42wLS6rPTETJX9iAFqUPf--xH4fsV9W2t1uyLEYmbFHQB_uOvRDY5y0A0ootFQYiVWpXPNSUMbSK4hD4gjazzyt-XAww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZh9yyoq1QUwGkB8_RTSYtfZ5zYBMzJxO7PPw0jb6YQ8H6bw1Lms2lVe_lfs-K19URggHfN9oqlIWZGwVU7Bx-klRmap_iSlsbuRe2E9YIZ4QJqrSalTp6QCIkea9D9LRLOH9lO9t35RkYUA4jXegIWAyCweYxExmrOPhTac2UH10gFZZTS5gnKcd6BwTNaD9tT0OkFzUcNjV1nRQEMP1HyBXaEhWdRwH4QzmnLc5w-ASiZFVoYARpZ3U4n2FLto6JsShaEoP9Y-A0JCNkjylT6yga_GVTbMmR2WC2zUIXwz1W7p5cidX4zTcnbgU7afn2Bck7sP6DfZdHWgolte_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_qDzCJTj9mTnWORoyBwuF-VoGlFzmNAnQcf5YOfoYSKqfq-GeeI1fyvdLx656GdR30tvGquBTY0BNPD5zwTlffxVeIR6DX-Iu3SEqhtuH0y7p0uLLkcehZ4Hm0Lj-RvePVPoRlzes6H1n8V29U7PyuETAiM73xzPgC2pUXoLJk8GrzOD26j1pC06L5ZmeCMK-4Y4pnwdqYaXZ6B6LJX_nF3hQi6-B_KWti4mbWX0x-33_g3dP1yj3OaPt0CCuJNyO2R8Tx8nN3nYJ2WYm_Ollebl2TEFtWbTqqquzTXP2MjP6H2a4kADLR_niUVIEcugDSN2gDnjTcB6oIt0mnzKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری: باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26490" target="_blank">📅 17:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26488">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ValAu3GLV1REL7N1pzxbOunL0qs-yxu9xfFzicdMNox6t3qj71kRiyGUkZeKKDuHwJjHIj0PkRG_a6qXtsIHXHQM7eMSftZrqFlfVM4kKaDXE0NAGKtCRZfHIv5umr-b5YypomI5WKeKFxkBFu1tANaZ430dVfnoD78nLZ_lRYQnZfQvz4JoEd_xkh-Pwu1-Auhwl27QbaHlUzzSPjw66cRPQX4LdnwWdFdDxzDGFFp7N_ZpkCWaMHXx8MzbChOzFhR0Fwabqe42g5NyglG0LdraqyfEUUAaMSBCDebZO3wn5zNlLDSE4HxqPr76pyYNTuML7ZmEJOcj5JZ3poA4FQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKvZfSzD5xQ7kx6RlJSHEPP3Xqc4tUm_Qfzvo32ldzmWjTIfWz_VIzloWOh69gMiouR3Ump6ysDLBpdCpmRiZcxYz8ym4iXT8YoQKsMfyPkJ1vEnxVY9qzibAwBlPMeN7_oQEVvDfdPssLRhcl1Rw7g0StLgidFFAREaukdyReUwjF2_Vz8x8cj5K0S7r7ai00gG5SZ8PZIEeZW0jccBTk3UPkoXShaE7pnn4XAnJ6SWYSV642QQqk0TeFJclAe8Qgp76BsSSoYKhcVIKhFR0y-GAPNhebAHEccdEM24eE6ebQR5GvehGg-_B8_0c1JhbA6wmK7hGTS73n2GkyG5Ew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=XCXJ1lZDaHRzut5nRhCqx52uWCiWCQoG5gnB8ECuvBscNME3qWE5q2HsmgFa6EfpgvFMbrbKt2pM_SiVmoKbgZD_m4Jr9fFDZUkxFDmdgrGztKxjYxcguXIx3iBE7CB2H01UtLlLfPTPTiV32v8EYv0avuIAGyIW8abnhs6Dt0AhpeULyNLaenEaoRR0dYSEodARVECJLgBUBW4Cf0V_Zdg2uie1cLm2_aeWMiD1zMKg1189RRvxFtq3S6JqAH8YCcd6w6YAAYVvJxmQOsjggb__Y3RhMUaAdGxViQ18yl6Ikwva8EOfCdsJXO9PY_Jdsgv__GtCHxgLCuLrnei0pq9MYZuY-0tH3IvGVMlGE_DbejdTPKVsze7J-4pMH-MCFNCbgKrHLClS8pm23Ee-w9IKCUcafUB3CrlziCYij1evAUDQe3sLVzoFvNfmUBSmZqYRipbS4pT7gZkEdwhZkQcdKbQ1GjQeU9YvJ4EdHsaNebag86QHj7C7xqdkC17cBujaa32M4mFoH4tdDT84Hapld0s35UIL3XK3wZdihmNRzA3ZXTW-zzAfZxoF1oh1ezQTImMDYc78Qu3BcJNT6PVNVfZnQJwYRxr2XL6dFyIrnGlaLSRAHHjCmgIicH2jAx5WjP77eiei9MBRQeN1ocrmuiSfyShCgLgtUh2wbqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edbaf35ae.mp4?token=XCXJ1lZDaHRzut5nRhCqx52uWCiWCQoG5gnB8ECuvBscNME3qWE5q2HsmgFa6EfpgvFMbrbKt2pM_SiVmoKbgZD_m4Jr9fFDZUkxFDmdgrGztKxjYxcguXIx3iBE7CB2H01UtLlLfPTPTiV32v8EYv0avuIAGyIW8abnhs6Dt0AhpeULyNLaenEaoRR0dYSEodARVECJLgBUBW4Cf0V_Zdg2uie1cLm2_aeWMiD1zMKg1189RRvxFtq3S6JqAH8YCcd6w6YAAYVvJxmQOsjggb__Y3RhMUaAdGxViQ18yl6Ikwva8EOfCdsJXO9PY_Jdsgv__GtCHxgLCuLrnei0pq9MYZuY-0tH3IvGVMlGE_DbejdTPKVsze7J-4pMH-MCFNCbgKrHLClS8pm23Ee-w9IKCUcafUB3CrlziCYij1evAUDQe3sLVzoFvNfmUBSmZqYRipbS4pT7gZkEdwhZkQcdKbQ1GjQeU9YvJ4EdHsaNebag86QHj7C7xqdkC17cBujaa32M4mFoH4tdDT84Hapld0s35UIL3XK3wZdihmNRzA3ZXTW-zzAfZxoF1oh1ezQTImMDYc78Qu3BcJNT6PVNVfZnQJwYRxr2XL6dFyIrnGlaLSRAHHjCmgIicH2jAx5WjP77eiei9MBRQeN1ocrmuiSfyShCgLgtUh2wbqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9FDGvNjfUOasgKctQgFdOCWMGu3HG6UlLZq_ri5a-WD5eG9nKsS0zJszooO5luplBSL7OViqsocjNL6P2uTsS2AFQ8hoJyzLAguIXNuCE33YS4UY2fE_C6kNT94gWPlYA5cj7MyXQ2abAIvbNg_GH07hlki5C1l4UiyFMJgE8q5N5pikAV5vGntUgoaFkQqTSOYdEZwaCYlyQ1yrDHgPeSbIa-H9GZDHnlWkYsg-MxXFmvp5nMqJTPRhL7bP8qEWlz9n_anYSBbnGvilCDXvhGR-f2HAmgfSpMvvBgkJdZFbS3rbUgX2bFUgl0AOuROluB_gRbdJb4g7B0bvkaJuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد زکی‌پور برای عقد قرارداد دو ساله با تیم تراکتور به توافق نهایی رسیده و بزودی از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26483" target="_blank">📅 15:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26482">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuPjXmjoLV6oVUf-muOEtMy4wa4hBXlfbuQPiEu6YuCgFHL_1pXmuHAtmL0_61mduPSbltOxqaxxFGhJbbcUPir2FXJybnahzyWsKVAIjfnuHs-ZRPtR6k5QEXP8K6AainWqO0MbK3I32AstvUeobhkb33gyQm-jTe26ojgTP6fU6e5-SimdMGuEa-NTjRXhVe-Qqc1ry6IWRRGPAYPF1qJx69YlIG0xnohjzkX_r8-_esRL8lOwoBoqCVGiOCvv7Vb3xpKocl2lFAUGcMvUULkSyS4ppu0YIkTVsd_996Rz-scIqO2fIR55gkS6I49e2VcpKGGjaChpzkJ8eomdxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یعنی نژاد پرست تر از سیاها نداریم. 99 درصد سیاهای پولدار فقط بادختر سفید تو رابطه میرن. اگه نژاد پرست نبودن این آمار باید نزدیک 50 درصد بود. نژادپرستی‌فقط‌واسه‌بقیه بده. واسه خودشون خوبه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/26482" target="_blank">📅 15:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26480">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kjzz9AOyOvRGKXH_9WvKHFNSnJEkA8ekuortq43FE8gPfBgWboJjf3kID5v3FlpKiNOWWCoHSYXQe0mfHo4TP6NuCJmZAnJ-K3uhclrMjuAUxMWLmejZLCoZCBQwkHJVqNwGswQSF_iYpVQK00_QwOc6tIPiwljSfgjRkp_wAJmnE7eSfAxh9f9bjx9LxyPVDq1HcWMEUVqZa-0kkB1-9a-3Pi2UJd37dK6EKjgTZ3q5e2aF0SQtL6KIxYrQ_R4cOIE4fWncEkiA9A4nF_ayRKr0xUa8fxTlyJvwVLG3G_kAa6ackB2SCplFFTL3g_RCryv9FYVhTa8Tycl6loC5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا و پس فردا هوای گرمتر از نرمال میشه و دیگه بعدش برای یه دوره طولانی کاهش محسوس دما و دمای خنک‌تر از نرمال برای اکثر نقاط کشور داریم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/26480" target="_blank">📅 15:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26478">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dORR9r5nTZ_Z00ssFakCj8ocj9E418wmLmz2byZtc2ZFRgY66L1z4QpKjMwNeR32-2jo_x_f-KcGbmxNDUJ63JChO8fNmSt7ff7Mk5xFeSDTfcq86nfkjUqCg8NDydZPq0Emf18LmhvCsSwP-wKKoGLjYZdj7f4rnVTqAkPe3eVHbseg7g4G4z3bQD9Gu-Kjrucu375gmWjLQrLXF34BEMvcpplI9pkG1jxXvT-TN-xHDpd1ggLg1KcdS7W_EhrOV0TmjqZl0ByxnWlC8Kdf9KRpteUM1d7koejAtLw1Kh3xL8C9PPuiXv7S-_ZdQ2UcioAOyDL3P8BAyBoZSgImWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRgPhNrpd2U0D_WjLTJM_tRB_ZfeBIEEBn12klIZWLN-mvZ9dDVikihq8Wru2QNgsxLffnkWqJa4RnIXIYn_7gLKCEy6IqO5MF68kwSoP8SnmTvZX5RJ6-D8gZEk8sDLX4s2ev6xEQZ2pxyioTrp6B-Eq28e9KNdWPx9pqFyl704E2LCNN2Wp0jEXaC-LS1w6Kg5VpVRVP_c_57jlzlJ_i3dvCKI3_hsSWThhfCXuFNs61QrMnxBdc2nlJquw4KBqeP2z6_COjsxpaaQnNlKl-Poz1AsYIpdiJ1_znIGVRA6VCT0-AYVNW3f2ShdlMUmewYXQ1rvtRuICVX2ZtW7pg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=Zh7kiF9ROEQHKcphCFFQ874YSsMpKxdL-eRupdvAKO2qJx7dCimCiqVozR8YeZsjDUmHf4BQyojfGdK2xT62TpPQHSlXVIKXRJ4b35wO0NQBDQD2MN3-KT437OXi6lmoXe1XgCHWggyK2yXOK_JuADVvVl_CGfCsCd66YOCChDj5vQTTeR9W3CpU1vDFYRsOUgDrUtRiyXL10urv1s8KhNpUW1JQ8_KlcRnDGJCW2ZfmgAmf19Ds89oKkBjgtoO6OJxvr1YMPHkxL6hV6ad7eiWvY4npBQQcfKXqol03-58G5d1JyaU721W67fez5iLi0uJifRymUMjeYQY50KCyrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a536e8783.mp4?token=Zh7kiF9ROEQHKcphCFFQ874YSsMpKxdL-eRupdvAKO2qJx7dCimCiqVozR8YeZsjDUmHf4BQyojfGdK2xT62TpPQHSlXVIKXRJ4b35wO0NQBDQD2MN3-KT437OXi6lmoXe1XgCHWggyK2yXOK_JuADVvVl_CGfCsCd66YOCChDj5vQTTeR9W3CpU1vDFYRsOUgDrUtRiyXL10urv1s8KhNpUW1JQ8_KlcRnDGJCW2ZfmgAmf19Ds89oKkBjgtoO6OJxvr1YMPHkxL6hV6ad7eiWvY4npBQQcfKXqol03-58G5d1JyaU721W67fez5iLi0uJifRymUMjeYQY50KCyrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به بچه هایی که توی اجرا جام جهانی‌ اش بودن قول‌داده‌که میبرشون مادرید باهاشون اجرا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26475" target="_blank">📅 14:25 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26474">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrL0isUDY54F6nHdPLMZRx9NiVdudL213CbJLQVHr3b9oatFSfKPZra9WlXN8By5bjbxSH182wKUKZYw2M7L9RU7jP1RRGErBTZ7FIe3XvmqZ4L1Tqv4db6X9Sycf3DkbRR3l4D247x-kNYp7izj5CA_DSm9-omCsmF29uXAi1RaR_HYD2fpcwAaCRjSPLEcn95owhu1bTO0cA4zV-vdoNjmVInOHzEPerXZ6naKfJMAXG4DuswEtqH2yczCKhTKxVg3HEloNYQsxol_aDIOamrM4QfarUycGkIPItvzSQi0qKN_2A1JFVWPirfgzikuG3DrncPVDrSJiIBmyRsHOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور و آرش رضاوند هر کدوم به ترتیب 20 و 15 میلیاردتومان‌به‌باشگاه‌سپاهان تخفیف دادند و در جمع طلایی پوشان زاینده رود موندگار شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26474" target="_blank">📅 14:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26473">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNdIgFz8gO_khUCcMdvi6DW6YsCGyVOrcTiV4C35brmoepwm10i-enWGd7ctC4DPOE-l_XjLYB7BVhq4E0FOFSzTMAuQWVPhmzPeNaOB4v3BiowybO4y-w_ok370gmh5Fjhl4SFk_lgQAbBS3KRJLpC21lMReMuuMbClwSJKs3nnlYHsABrD9qjD4yvXlj5_DoU4NxW9CBS1QRPRvrtkq7d4YfRJTu2emkSJZr3cJU0jC7k_YqzaufXEz5rtCElDRa4TDSd8U3_SWG9x68MRb4I1PHDePafk2XHLi5G2bUhoQyIbGHZsId-GxPKqwfaA7k59LA6SkEKbM7l08W63yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26473" target="_blank">📅 13:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26472">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJS7Qx2uL6u9oSNqZC9oX3EDg7sN6qUM2JZIi1eoeyPDxvcgi5tj--p7PVVdVOji_NXLdNqdhb7-ogr_vrXcskGAxWxvGZsoz-tCMDd7YTOpipygUTjxJ_10PQ4tHJqFzSTjuKol2eCF7Yta0oTQ9oTxwAgZz8hqIC2QHKoTUz2qUDs6clRG65-BK3swpO2S0w07qBNBNPziJC9wFMtvNxurxnT59xR4a73gJF_qQZrToc4ge3bTOaNCVr422Jin7HAA4jZHviCJMHNT6HR8wwoGWSVU0lBGWny4qwp4fY1yp_DrjH-tvA3xvmuSokjfqBvBFGjFiNZWEgS4DlsvMg.jpg" alt="photo" loading="lazy"/></div>
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
