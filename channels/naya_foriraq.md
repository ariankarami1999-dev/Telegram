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
<img src="https://cdn4.telesco.pe/file/icCNSxjqXFHbjb90WxFkENkdciUGF6n14bruKQIh-ADRadc9br5gJI9xJeY-5ixbLiJdChnu1KXQOtlWiR-4S3ko1H9hy4S7YK1WHpUwCMrIoDzLJCLLfs8lizEbxhOuGZ6ez4g5UdM7W4rFByAXeG2OMl-y1kW4Z11I-js0LO8ALnD2BC9QB65VqEM6ZkLH7GMrwpDZE21sG6kIwru8KMNamocwFnYwJ84GQD9HLjm4aInteB958rU0_Xa2Fm7R4tDY0qH3VhWJtHYwWL7PFCPlMb14PVcN27Q3E-y0d2ZuAB0gTvClmk2T4vnuC96JUIcJJS1vTIFIlwn07rcouQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 273K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-22 01:06:13</div>
<hr>

<div class="tg-post" id="msg-87662">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا...
انتشار أمني واسع على طول شارع مطار بغداد بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/naya_foriraq/87662" target="_blank">📅 00:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87661">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556bb53c10.mp4?token=A9MORXb0v_cv5MuFfpuZ6UjjTVyBa8b1YikWwjjRQOXY9l-ULJ41OYDew87Zm8JHl3Yd85NWoC4mtnnweMvUBBKkl2xKArVU_DXkQE3Olt_sRy9J8Gm3l5BaJTSvz1iMcYnzSkupUV4s8Y_FQSNyDtTIIRJaJRNIdwE2RTrv1W3f33_g4kMp1puIydEPGEg5eFoPIO9-USQ9Y0ceEfUBOq44Aemrt4aWcZ76i9li1RWa23PrYp_iNpqeqEu0YzZoXWFk2H5tCEbUgkQWxzvlAuPaq70aVeCHhm8Ux-ZG6hUgG7DQjSdQSJqkMztHVb3po0gBQ0Q9vs1qSm2dNjv8-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556bb53c10.mp4?token=A9MORXb0v_cv5MuFfpuZ6UjjTVyBa8b1YikWwjjRQOXY9l-ULJ41OYDew87Zm8JHl3Yd85NWoC4mtnnweMvUBBKkl2xKArVU_DXkQE3Olt_sRy9J8Gm3l5BaJTSvz1iMcYnzSkupUV4s8Y_FQSNyDtTIIRJaJRNIdwE2RTrv1W3f33_g4kMp1puIydEPGEg5eFoPIO9-USQ9Y0ceEfUBOq44Aemrt4aWcZ76i9li1RWa23PrYp_iNpqeqEu0YzZoXWFk2H5tCEbUgkQWxzvlAuPaq70aVeCHhm8Ux-ZG6hUgG7DQjSdQSJqkMztHVb3po0gBQ0Q9vs1qSm2dNjv8-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
اندلاع حريق واسع جراء تحطم مروحية عسكرية في تكساس مما اسفر عن مقتل جنديين في الطيران الاميركي.</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/naya_foriraq/87661" target="_blank">📅 23:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87660">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">طائرة من طراز بوينغ 737 تابعة للأسطول الملكي الإماراتي A6-RJA تحلق من أبو ظبي إلى طهران  ‏هل ستتجه المزيد من الجزية الإماراتية إلى إيران، أم أن مسؤولاً إماراتياً رفيع المستوى يقوم بزيارة؟</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/87660" target="_blank">📅 23:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87659">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFHl0brrzXq_saSS8lNqi0vTWnQawZKodLxxj7P3S7Zk7au3RS1u5FCEnrYzx2Bzy2LCDXUUyQOaOYB0LQXlMb3gjqaR6X_yxmdbqzH7xBdX0s2Nz8_YVEu79VHjkZJAg5mLAOCRsQFZjCT9VNq_RAd5qX9hxa7_NmotLqGneHpMciHm2ypNnzMFtHUt-nOBrl1UY0VXyEoi1pfF0-tS-NKIcvrNSxFnUZekVPeSvaMZDf-8JU2N78X9Xwe0n3qxxXPyiILz2jPa43FBqulF9tzX7KRAxH7cEF4YrwWPjJrKQAatwEx0gT5_W4vyweCeZHmZ4wFtq_p9PAtRFfQzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏ترمب: المتحدثة باسم البيت الأبيض كارولين ليفيت ستغادر منصبها نهاية أغسطس.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/87659" target="_blank">📅 23:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87658">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbKa2zZqoaqIKpH6_UtZHiXhjHI5l2Yje_PSNuFUDfXf02J9FPd7znZCBVt4p2fJz0OCCKiLyNHxCsJGolaF6CWK7EElSV4Z2CqdoTJXr1i96wI8FY8Lmk0B2dCXRuEsWITGtijy_w19R1iDPaMMXvHlg8C9M8LMErbOai3Orj4_5PlhrqwUdp1gfY3y99U-hbKTmGO7KXHugG931czc6FMwOvqZ3YyLmAXgB8g-VxaDEn9K6v8XDfeuM5TwzK0IBj9DyIwUxLmZfs_L8UlPNiJsd0AOCl-cwMW2QAUTaURKb2OWupOvy71Tf88FEpApZmHNYRScgjzUUQiB5v6Adw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترمب
: المتحدثة باسم البيت الأبيض كارولين ليفيت ستغادر منصبها نهاية أغسطس.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/87658" target="_blank">📅 23:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87657">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a260e9217.mp4?token=q6X6LFDLa-8qZLZkeMS-g0ClPZbKrNz0F2n82AbUVD5hfFhBNEpwYEF4_L3ERjypLZCxY4EjVUV9dHL4fEstodyScngNHJBz43zKThycHuxldk-q3YNIEt-BBNtFO_sKkQUT1njxETIMKagCU8y2EM90x5q7KbgOzaCTe6klB4WgEzo0oDVlvWiEntHEKTeYb0u1stVtnZaBsEtP75I34o5ubdYdNa3S5I4Ely5UnF4TnJa_Z4L0EC632WW1KrKYFwnFIAY1IeMW7d04sVAAxB-M0cXHs2hDuLiplTUgeuCLv19UfDLBiPRDE8mV0a9Agt6f9kTvadYMehgM5iK2Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a260e9217.mp4?token=q6X6LFDLa-8qZLZkeMS-g0ClPZbKrNz0F2n82AbUVD5hfFhBNEpwYEF4_L3ERjypLZCxY4EjVUV9dHL4fEstodyScngNHJBz43zKThycHuxldk-q3YNIEt-BBNtFO_sKkQUT1njxETIMKagCU8y2EM90x5q7KbgOzaCTe6klB4WgEzo0oDVlvWiEntHEKTeYb0u1stVtnZaBsEtP75I34o5ubdYdNa3S5I4Ely5UnF4TnJa_Z4L0EC632WW1KrKYFwnFIAY1IeMW7d04sVAAxB-M0cXHs2hDuLiplTUgeuCLv19UfDLBiPRDE8mV0a9Agt6f9kTvadYMehgM5iK2Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
على الرغم من الارتفاع المهول في أسعار البنزين في إقليم كوردستان فإن جودته لا تتناسب حتى مع دينار واحد من سعره، إذ يتم خلط مادة الثنر والماء مع كمية قليلة جداً من البنزين.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/87657" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87656">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/87656" target="_blank">📅 22:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87655">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/87655" target="_blank">📅 22:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87654">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKN-Ohq7VCVOzfYmD7BYNvI05Y0Tw5EH8om7fGUPbbx4PQAIC8ADOOqaBojE36XguxZCzcDoF9EyNPtiij6XnRGcvRJmbzcl4aj1EBlCtGma8F02_spN8gm6yODLJOQ1ypiNMWgfKXdDIZEyImyK_GNYQIVmljOGiPh1zSCNFaY4fRnRxc5y6hajDPsNCttYMUZjkKhPHsmOjDk4TvYBnE15BYlJFqfjUyqm0PRq3qOG1wRK-pZEL6T_EtXyeKiuXmIjK3EJY16r5RS8lkwFqttL8nzMjSzjryjmJFOeRKaPGVpYY58KXj8fLXwdnvx3r8dPCeng8oNcFdkDZd44hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هيئة الممرات المائية في الخليج الفارسي:
إن الادعاءات والمنشورات المتكررة من قبل المسؤولين الأمريكيين بأن مضيق هرمز لم يعد مغلقاً لا تغير الواقع: فمضيق هرمز لا يزال مغلقاً ولن يُعاد فتحه حتى يتم قبول شروط إيران.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/87654" target="_blank">📅 22:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87653">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec836d6d11.mp4?token=i5U-Id33KO2-pXccv2x97hdaIbvMYdEJlsii8e2-VakopXEfMGt-ayCQeb1uhZGqdUEWHaJONf1R3LUyZ7iiAap_Yxa20mUKCF_nhHHt4C3sQgbxviguNNUSj5y30bLJb22spobGtrjHtZo81jy60M2s465YrarVSdjLqMV3UgHMCDEEHzpv5MEJG14-kTWm87RziI7imLsQdBvIOyB326X1vIR_p2RrIGRXVywYabxt3H73FWVBRSIdwjmwVxRfLw4vpM48qWp6nHDcNGfnpEtK0Ho8XdFBc8hYpplhyRZAidqlAS053gG8YPiEIKl2JGpg46UT4ySmiiJ366HHHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec836d6d11.mp4?token=i5U-Id33KO2-pXccv2x97hdaIbvMYdEJlsii8e2-VakopXEfMGt-ayCQeb1uhZGqdUEWHaJONf1R3LUyZ7iiAap_Yxa20mUKCF_nhHHt4C3sQgbxviguNNUSj5y30bLJb22spobGtrjHtZo81jy60M2s465YrarVSdjLqMV3UgHMCDEEHzpv5MEJG14-kTWm87RziI7imLsQdBvIOyB326X1vIR_p2RrIGRXVywYabxt3H73FWVBRSIdwjmwVxRfLw4vpM48qWp6nHDcNGfnpEtK0Ho8XdFBc8hYpplhyRZAidqlAS053gG8YPiEIKl2JGpg46UT4ySmiiJ366HHHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
من حادثة الهركية ومحاربة مدينة كاملة بسبب اختلافها السياسي، إلى حادثة فندق لالازار والرعب الذي عاشته السليمانية جراء الهجمات بالمسيرات ومختلف أنواع الأسلحة، يأتي بارزاني رئيس اقليم كوردستان اليوم ليصرّح بأن فصائل المقاومة ستجعل العراق في عزلة دولية اذا لم تسلم سلاحها.
هل العالم بأسعار النفط الحالية قادر على فقدان أربعة مليون برميل ؟!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/87653" target="_blank">📅 21:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nox_3M2t8riZK_pv_a8ZTtrpC6cRLCHMkBKYwVKgzsHkF4tMMt-_YxMnaDW7iAshd0UVfoTFfebgXGspViyxrxo7DvsEfvxynz9iJmO1gbqg_J9E8CFi8LkKtzVmybGwv4fgG8uJlVwC7t9wvXB_650DAxN1aSssO0DbCe3O1BKdFcGd66nA187ZCbBxRrt9cx2lTCUsHnLRUrJoqRL5JmJwOf3NXVqNV_onYPbozod-KdhPzXZuA-Tp0ND8YyMuP6jpDlODu2N9FvaINHB9y9V1RqRw4vFfdsscX1gxS7kD8wk6L8j7iwNPxYHqRuD0NJlN7SAzfiLqMEcygyQY_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vuV5FI-vBWz-A7vQURvjtUWvum23r93ej95B9j1SgBJ5yEA0TvIdy4T_lDIH2KZDU0nuMG28eeB-ETfrkmnrbgwXco-R3RBR1IKqs3S_j2Arde5oVPA4Hg4G2G9ji-zTsyRt0PyhD-fqbwoC618sVrmCXI6rdDEvrg-4tgx-1vZ_b1nZcResXy-fFL6eaRLFdv9UwD3oDA1cm31mrYCJbrIm-TlLSr1nEFSCZ9Op_oZ1bxvK_vYIAvXkOL0E4_onQsMT-UuHj1-YLNyeF1mKHS_L2tdYvocDh15wuBGMSscKSha5HrxzhjXlUE8j-X9RGRcqg_zNtvGywCX3nSb5hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇭
سلطات البحرين تستمر في اجرائاتها التعسفية من اعتقالات وغياب قسري في حق الطائفة الشيعية التي تشكل غالبية سكان في البحرين.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87651" target="_blank">📅 19:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
🌟
‏ترامب:  الولايات المتحدة تسيطر سيطرة كاملة على مضيق هرمز. أعتقد أننا سنحافظ عليه! يُطلق الجميع على حصارنا البحري اسم "جدار من فولاذ"، ولا تستطيع إيران فعل أي شيء حياله. ليس لديهم أسطول بحري، ولا سلاح جو، وجنودهم المتبقون لا يتقاضون رواتبهم، والحرس الثوري…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/87650" target="_blank">📅 19:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇶
المجلس الوزاري العراقي للأمن الوطني: قرار انتهاء مهمة التحالف الدولي في العراق في 30 أيلول المقبل هو  توقيت نهائي لا عودة عنه.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87649" target="_blank">📅 19:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87648">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇺🇸
‏رفع دعوى قضائية ضد ترامب بسبب بيع حق الوصول إلى منشورات Truth Social.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/87648" target="_blank">📅 19:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87647">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBpDVWhpIPbszAswz-9JXTaUYIUAAP1gnEE1qXpikOdlwFuUxhMV6WHWPWJThs5Ir0zEAG86huciA2rZHc6nsnMvoxcREfRyPTUbrUoEqUkecd6WVQtxLti_BwSLiA74aep46-Yk1Corr9sazWTZvEep44Qd8h6p_Ont-ldJvuI4rGlK9q9kPyWqOBNi4VCWSqYPQxVl3ltdewYLsUzBhywU70Gl8juTO2kfrKLVa37rGZKpWd7eQqkkeYhP6c8Ds1zkEvmsHXfTHYiEGTaftoysai5cstPLqMshiFgkmwAsqScuY_h9CD5dUQ6FZ_O4uWJQopbV4WFgVuacD9QeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
‏تتجه ناقلات النفط السعودية حول رأس الرجاء الصالح لتجنب انصار الله في اليمن، فيما تتوقف معظم الناقلات في البحر الأحمر عن العمل، وتتجه أكثر من 12 ناقلة فارغة نحو موانئ عُمان والإمارات.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/87647" target="_blank">📅 18:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87646">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">تذبذب عدد من خدمات الاتصالات بالمنطقة الغربية في ليبيا بسبب تعرض الغرفة الرئيسية لاستهداف بمسيرات.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/87646" target="_blank">📅 18:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87645">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">The bully of the world no longer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/87645" target="_blank">📅 18:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87644">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
المجلس الوزاري العراقي للأمن الوطني:
قرار انتهاء مهمة التحالف الدولي في العراق في 30 أيلول المقبل هو  توقيت نهائي لا عودة عنه.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87644" target="_blank">📅 18:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87643">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇺🇸
وزارة الخارجية الأمريكية تطلب من سفاراتها في منطقة الشرق الأوسط خططا للعمل بعدد محدود من الموظفين.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/87643" target="_blank">📅 18:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87642">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrnPnc_k3Ipne9j6lZxgHyBY-eQc87vd_U-W0bsHYmNNYPYo0lYgE6SWPtS6Yvuu1d5tzd-g2PGlAvrJlFhkrJxRVa2v6EGCMpw-aTFVgdD1tlJqKyxlzH4-DUgB-auNj_w_sb9OqQNUrdxLERbGj9KFKj-yIeGRkZnrRw4eqnYL1Tdp-QRx3HL_HT4Cpmc-v_HZpPSyRHCn5C8ie7ShwlY0aCXg8EBlTE-fhkHXfRjykP7R0U5HLSRHqhqtNq-IrSGxWMB8bIZpAxWGmMoQ2I8cuKskT7IbyhZ4J0wORrp8ArL47iyggW9KWwKBE-S7mkXAzDyAdqslBS36H4mlhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">The bully of the world no longer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/87642" target="_blank">📅 18:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87641">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1ydzolvdGx6afw0iuEfkiKDAmcxF2mNV5Xhb4ykmMyHXKOCoOioy_9uwgeQ74XOo1xOpcjpAVtMdpRfBzNdFktURP-gJi1C5TdYjYA0W47A0iCQma29y79XDVQlrPFkXSsjXXkKr292-R8BpWcHeuFdJQwFN7Nrc-hVpmc93t3XWAfyKjh8O7qQvnyYwrgcDMyjL7dcF39xkRhA8sL4OGkvHq4x6G93DBM3ybXJ13JBh059PhERRRTYiWne8B8JMz6Q4VqYNS9EoYBhDAwfWvSUMxjXpfqiVgfQNKo7_F6k4BGO5UQcuuEX2idLxJWd5oT1jTOMZJshKH4j2nV3Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
الولايات المتحدة تسيطر سيطرة كاملة على مضيق هرمز. أعتقد أننا سنحافظ عليه! يُطلق الجميع على حصارنا البحري اسم "جدار من فولاذ"، ولا تستطيع إيران فعل أي شيء حياله. ليس لديهم أسطول بحري، ولا سلاح جو، وجنودهم المتبقون لا يتقاضون رواتبهم، والحرس الثوري الإيراني مُنهك ويهرب، وقيادتهم غير مستقرة، في أحسن الأحوال! ليس لديهم مال - بلادهم في حالة يرثى لها. كل ما لديهم هو أخبار كاذبة وتضخم بنسبة 300%، والوضع يزداد سوءًا! إيران مجرد كلام بلا فعل، لم تعد مُستبدة الشرق الأوسط. الحمد لله!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/87641" target="_blank">📅 18:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87640">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
نيويورك تايمز:
يقول صيادون إكوادوريون إن رجالاً غامضين يتحدثون الإنجليزية ويرتدون شارات عليها علم الولايات المتحدة هاجموا قواربهم بطائرات مسيرة مفخخة ما أسفر عن مقتل أو فقدان عدد منهم.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/87640" target="_blank">📅 17:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87639">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6HAMoUyl3-LUH0SWJIfVe9HhAe3lYIWxkd90_Lx-jZzGHLm1UA4eOB4f6h2rLcLFrfvYnZz2XCLza1L8qvbBrJbyFm2jpxMuJgBDu7CYf4GwNMaM5CpiGVaA6rszK2oqBuUcY49ZxVC8SvVH-sgnGBNRHgf_u1UiKJA60EIitjklzYusSbpFZyC-3YAFpPihgH8Aj1RWenCowVc4aurgmPMPG7rX2CuhOdRedi8MM28d9yLeRIdBUB_g-RyJJwBt885V14scc_TaCV1iqkJU-TkE1VqNe9UhUEukvVas5SSzJKv8yblzB5LunZ4H-sTnseesKiR0fwIiAnjzGBPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
النائب حيدر المطيري:
يا وزارة الكهرباء العراقية حقيقة أم حلم أم خطأ مطبعي. 801 ضعف بين المبلغ التخميني (900 مليون) وبين مبلغ التعاقد (721 مليار) لشراء 4 آليات، هذا ما كشفته اليوم لدى مراجعة تقرير ديوان الرقابة المالية الاتحادي.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/87639" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87638">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
🇾🇪
انصار الله:
السعودية تخفي خسائرها لا سيما عدد القتلى وحالياً نستهدف البنى العسكرية فقط. ننصح أبناء اليمن في المعسكرات السعودية بالانسحاب منها للحفاظ على أرواحهم وسنقدّم لهم مكافآت</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/87638" target="_blank">📅 17:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87637">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d416ce65.mp4?token=otv3Xmu7Mh6B5Bnt6BU1iumzZIrN5YS3u_9T3Xc9cQQK275KTQG6wfR2sW0o4rQfdBVdaQXdCDg7U9K99AC9vuE8SWjfuTd430LVKRUD2dTQDvhFeC-w6Dh__VSPhn-QUMF9pUC5QGcld8Au2GLitk_H57laucwioRQvEWgSUaioh-Yf5Wgd9AHEtiM_jSDcQpzV0Lu40_ojzGkiVKjOqqXzfQ8QeQPhhNFGrW1OTodSrLPqKJFIvnrzGHcV6ySVQW24m1oA0mCmoSxJ68YALTSeSflaJYd9sk5p9gyu4neX7XXLlFajXqSWO2K4g2WlpTXwrnFW_LW86xfeWgFu8V8mPQtfWyQjazD-6TCLgWhvqLEPZSuQeZOSDd5SJeNU68UP-xa9SE8MIDNwwOZnsjh_Aw-jND_GBjtfMoavZ-HV0kVqg50SFyW6ZycURDDdSMekNA8v7YXwfAziHslZjhbiCv06ZCInf6RcbSbNavyjcHyMO-6HSyKDqsZtTrIw9k_s67DFMgyOWSxYP9lOE8-679ktVU_-1giF0-kxiMNhJ1v0b32xSQ6Lw8m-ZzCbHGJdrncJKe2b1hC4DpMDggT_6kWaZu84PkmDpGv6vU2q9Bbkw1F1YBWlZ0407Upf1unmzEIkJuIhDX6dCvtD9W8gPWlWBQ__JPs1brrNuzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d416ce65.mp4?token=otv3Xmu7Mh6B5Bnt6BU1iumzZIrN5YS3u_9T3Xc9cQQK275KTQG6wfR2sW0o4rQfdBVdaQXdCDg7U9K99AC9vuE8SWjfuTd430LVKRUD2dTQDvhFeC-w6Dh__VSPhn-QUMF9pUC5QGcld8Au2GLitk_H57laucwioRQvEWgSUaioh-Yf5Wgd9AHEtiM_jSDcQpzV0Lu40_ojzGkiVKjOqqXzfQ8QeQPhhNFGrW1OTodSrLPqKJFIvnrzGHcV6ySVQW24m1oA0mCmoSxJ68YALTSeSflaJYd9sk5p9gyu4neX7XXLlFajXqSWO2K4g2WlpTXwrnFW_LW86xfeWgFu8V8mPQtfWyQjazD-6TCLgWhvqLEPZSuQeZOSDd5SJeNU68UP-xa9SE8MIDNwwOZnsjh_Aw-jND_GBjtfMoavZ-HV0kVqg50SFyW6ZycURDDdSMekNA8v7YXwfAziHslZjhbiCv06ZCInf6RcbSbNavyjcHyMO-6HSyKDqsZtTrIw9k_s67DFMgyOWSxYP9lOE8-679ktVU_-1giF0-kxiMNhJ1v0b32xSQ6Lw8m-ZzCbHGJdrncJKe2b1hC4DpMDggT_6kWaZu84PkmDpGv6vU2q9Bbkw1F1YBWlZ0407Upf1unmzEIkJuIhDX6dCvtD9W8gPWlWBQ__JPs1brrNuzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي عن ادارة ترامب: هؤلاء الأشخاص لا يعملون من أجل مصلحة الإنسانية، بل لا يعملون حتى من أجل أمريكا. إنهم يعملون من أجل مصالحهم الخاصة. بمجرد إغلاق سوق الأوراق المالية، يبدأون الأعمال العدائية، وعندما يفتح السوق،…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/87637" target="_blank">📅 17:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87636">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي: حتى لو استمرت هذه الحرب لسنوات، وحتى اليوم الأخير، ستُطلق صواريخ إيران. إذا جاء يوم لا يتبقى لدى إيران أي صواريخ، عندها سنكون أكثر خطورة على أمريكا. تمتلك أمريكا آلاف المصالح الاقتصادية في جميع أنحاء العالم،…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/87636" target="_blank">📅 17:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87635">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي: يجب علينا تحقيق الردع بحيث لا يجرؤ العدو أبدًا على مهاجمتنا، حتى نتمكن من العيش بأمان. إحدى الطرق هي إطالة أمد هذه الحرب حتى نصل إلى الفترة الرئاسية الامريكية القادمة، والتسبب في استنزاف العدو، بحيث إذا أراد…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/87635" target="_blank">📅 17:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87634">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e9534074.mp4?token=fcAr6dGGWzpLfn7nsqPPzhZJGNwRBm1Qz3MseMTBYv4etksg_pAXQYs9X8pl_hYobib_7FG4VPXueJn00v4UC2rlx_iAiQSnRjuycQwt0Gjsj6BQEpVph2LbIeH8XC_3drbA0XUxIhg3UAwv2RSvo0B4Kep24bJ1XgKMPW0k6kEFR3YAU7SJDhCErOpEJ9Kki0gSQFJirBTKsbhvrPLCtkan0CXNNU2tqxkNS_OwexuuxsHozV0LYFKi829nCME2yfBTltzKMfIyaFZ8F24EFIOox8i9OATHB-EzOfEStlUMzGKe8DH6U3Hh_BxxdmAe6QvFFdjr7lfptZpLpUuYgrnDbzrmIXzhGxaXMvt9SYWzz1884iCles2YREWVLxOdb508zt_ak0USyPQyYOi2Zs0G8XvR96LyWzr339zLW784_DtLEtLxoXb9Xmnhri9WkTxYkhd1YVMJ1vi_Manv6LBRb2Urah0yfFTe7235mmsCJzvH_Cu1y8rlLYAWu93GzlTqLhcy9kLRFk5QK23SM0p7EwdThira0phvXyv3DimSLdi1-fLnzade1WeqL2B5ISTaqXe2M_k_42zryRcV40My7NeZRNJd7CBa7k_HYjGTRZ5RvkHNHrpBLxCVHT9Ft0nwaOES1YavhfEGfXChQ0mawGuHq_4oDX9-fwhLVuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e9534074.mp4?token=fcAr6dGGWzpLfn7nsqPPzhZJGNwRBm1Qz3MseMTBYv4etksg_pAXQYs9X8pl_hYobib_7FG4VPXueJn00v4UC2rlx_iAiQSnRjuycQwt0Gjsj6BQEpVph2LbIeH8XC_3drbA0XUxIhg3UAwv2RSvo0B4Kep24bJ1XgKMPW0k6kEFR3YAU7SJDhCErOpEJ9Kki0gSQFJirBTKsbhvrPLCtkan0CXNNU2tqxkNS_OwexuuxsHozV0LYFKi829nCME2yfBTltzKMfIyaFZ8F24EFIOox8i9OATHB-EzOfEStlUMzGKe8DH6U3Hh_BxxdmAe6QvFFdjr7lfptZpLpUuYgrnDbzrmIXzhGxaXMvt9SYWzz1884iCles2YREWVLxOdb508zt_ak0USyPQyYOi2Zs0G8XvR96LyWzr339zLW784_DtLEtLxoXb9Xmnhri9WkTxYkhd1YVMJ1vi_Manv6LBRb2Urah0yfFTe7235mmsCJzvH_Cu1y8rlLYAWu93GzlTqLhcy9kLRFk5QK23SM0p7EwdThira0phvXyv3DimSLdi1-fLnzade1WeqL2B5ISTaqXe2M_k_42zryRcV40My7NeZRNJd7CBa7k_HYjGTRZ5RvkHNHrpBLxCVHT9Ft0nwaOES1YavhfEGfXChQ0mawGuHq_4oDX9-fwhLVuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المستشار الأعلى لقائد حرس الثورة اللواء محمد نقدي:
يجب علينا تحقيق الردع بحيث لا يجرؤ العدو أبدًا على مهاجمتنا، حتى نتمكن من العيش بأمان. إحدى الطرق هي إطالة أمد هذه الحرب حتى نصل إلى الفترة الرئاسية الامريكية القادمة، والتسبب في استنزاف العدو، بحيث إذا أراد أي شخص آخر مهاجمة إيران، فسوف يعرف أن هناك ثمنًا لذلك.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/87634" target="_blank">📅 17:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87632">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وزارة ‏الداخلية الكويتية تزعم: الموقوف تلقي تدريبات تتعلق بصناعة المتفجرات والطائرات المسيّرة لاستخدامها في تنفيذ مخططه الإرهابي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/87632" target="_blank">📅 17:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87631">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌‏وزارة الداخلية الكويتية تزعم: جهاز أمن الدولة يحبط مخططًا إرهابيًا داعشيا كان يستهدف إحدى المنشآت الحيوية في البلاد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/87631" target="_blank">📅 16:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87630">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‌‏
وزارة الداخلية الكويتية تزعم:
جهاز أمن الدولة يحبط مخططًا إرهابيًا داعشيا كان يستهدف إحدى المنشآت الحيوية في البلاد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87630" target="_blank">📅 16:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87629">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
‏
البيت الأبيض:
على إيران التوقيع على الاتفاق وهي تعرف ما سيحدث لها إذا رفضت.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/87629" target="_blank">📅 16:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87628">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57727b7186.mp4?token=BYmtrRRNdLD8FQJ_O1MMcvN08Ngt61jTwC7KlTylBBvIwo3BR6lMMi_rdGqF6Fr_ENKhqexvUxYIQDRSrcEpiH1Bh-CY4LSMRaZsGraUWOtLAZsSqr1vdpefglhSY0L84GPI7uj-_u302hr-LZTpHVwLD2yxZogZ17SwnDYScEOBidJfNAgmxNewsqPmtqUOthsPWmSVQr4RqRR5QfsQTRF7pb_qcspaQjxD1ahgunLBXZd_LjZBbXaCDWRuUS0GvkdYK604A_Wxf3geumtmne84Tro1yEEftkhbPL_f7VWcFSz0el3cmrGFqLeQ_d2CgyUjGazP6abwZTZO58g0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57727b7186.mp4?token=BYmtrRRNdLD8FQJ_O1MMcvN08Ngt61jTwC7KlTylBBvIwo3BR6lMMi_rdGqF6Fr_ENKhqexvUxYIQDRSrcEpiH1Bh-CY4LSMRaZsGraUWOtLAZsSqr1vdpefglhSY0L84GPI7uj-_u302hr-LZTpHVwLD2yxZogZ17SwnDYScEOBidJfNAgmxNewsqPmtqUOthsPWmSVQr4RqRR5QfsQTRF7pb_qcspaQjxD1ahgunLBXZd_LjZBbXaCDWRuUS0GvkdYK604A_Wxf3geumtmne84Tro1yEEftkhbPL_f7VWcFSz0el3cmrGFqLeQ_d2CgyUjGazP6abwZTZO58g0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">التقى ببشار الاسد بعد اسبوعين سقط  تحالف وية باكستان، باكستان دخلت بحرب وية الهند وانفجارات الارهاب كل اسبوع  تحالف وية تركيا، مباشرة سقطت طائرة F16 لهم وبدون سبب  الدرس من ذلك: لا تتعاون مع بن سلمان فگر ابن فگر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/87628" target="_blank">📅 16:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87627">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGeR3W4fcNWfM2yDrlTLfLghwCtKMN7xWnCRxtj6GgpLGbKg9nGDDxU7PRVOKanwN0y8pWcSZSB8sDibMTWkL_s03uJk6PUfGWL4dQrdrKV-cd2qW_FfO_3kGeGNtfMGphcHf8xFyOmLLVAZvSRrq3ANCQcIidkP3t0RRJ0H-xlC0vammXINxnis7V-90jw_h5qbfo6Fy120EQSnrTaiIVPIchq7Rd0_7ksYATMK3zdFT-dqeH5E_I6j-n70n1eeBnGduultwWe-N23tnHudZFchet_SjkNNCmjgqQoaZc2Bc121uCWml_Lkx3z2Fbi7l55D5PXNdqfqgnjqs5wjUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
تحطم طائرة عسكرية من طراز إف-16 في محافظة يالوفا التركية خلال رحلة تدريبية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/87627" target="_blank">📅 16:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87626">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06d02b8565.mp4?token=RD6TdtTdS-fruhENaxcLwYDtcl28WSLkcnb54itADaj9V4ZvtUfD5faGMbnO9D3QwyTYjA7cTVKmjvIt8pnjPR1t7WRY-Z_8uW161PxGdj4BikewBH-yZcc04sU7eOmwh5wkimHQvsVx-wUmnRSgS9g9UlQ1IDlq2ioJYA8RnyanFrlUGkjp6ai4bAM09MorghGtROjUZSG6vzEHklNcuwgjWdC6kZfcrzexfH8xsLXTXKOvswI66S9826va28gRia5E54sveEmfpXjqgd9QNFwkUgEIlqxdADWu6FoFqra90tuRGfTnLclMn6-KR0mRRm_5KR1kMdC9aS5RNo_6tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06d02b8565.mp4?token=RD6TdtTdS-fruhENaxcLwYDtcl28WSLkcnb54itADaj9V4ZvtUfD5faGMbnO9D3QwyTYjA7cTVKmjvIt8pnjPR1t7WRY-Z_8uW161PxGdj4BikewBH-yZcc04sU7eOmwh5wkimHQvsVx-wUmnRSgS9g9UlQ1IDlq2ioJYA8RnyanFrlUGkjp6ai4bAM09MorghGtROjUZSG6vzEHklNcuwgjWdC6kZfcrzexfH8xsLXTXKOvswI66S9826va28gRia5E54sveEmfpXjqgd9QNFwkUgEIlqxdADWu6FoFqra90tuRGfTnLclMn6-KR0mRRm_5KR1kMdC9aS5RNo_6tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تحطم طائرة عسكرية من طراز إف-16 في محافظة يالوفا التركية خلال رحلة تدريبية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/87626" target="_blank">📅 16:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87624">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇸🇦
🇮🇶
إعلام سعودي: وفد أمني عراقي رفيع يزور السعودية غدا.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/87624" target="_blank">📅 16:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87623">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بيانات تتبع السفن:
السعودية تقوم بعمليات تحميل النفط في البحر الأحمر مع إيقاف تتبع السفن بسبب هجمات انصار الله في اليمن.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/87623" target="_blank">📅 15:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87622">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇲🇦
وزارة ‏الداخلية المغربية:
منشورات عبر مواقع التواصل تحرض على العبور الجماعي نحو سبتة ومليلية يوم 15 أغسطس.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/87622" target="_blank">📅 15:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87621">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇱
🇮🇷
اعلام العدو:
بعد اختفاء مواطنتين إسرائيليتين في النمسا يوم الجمعة الماضي، يحقق الموساد في القضية، وسط شكوك باختطافهما من قِبل جهات إيرانية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/87621" target="_blank">📅 15:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87620">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">منظمة أوبك تخفض توقعاتها لنمو الطلب العالمي على النفط لعام 2026 إلى 580 ألف برميل يومياً (التوقعات السابقة 780 ألف برميل يومياً) وترفع توقعاتها لنمو الطلب العالمي على النفط لعام 2027 إلى 2.16 مليون برميل يومياً (التوقعات السابقة 1.94 مليون برميل يومياً).</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/87620" target="_blank">📅 15:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqeqkyF2nu2yP4v5P6A0CKqmAohFYru30qH5mGUH25mnUlMXAyCS_OT8Xoh3kUOud-oBlyZv2G5UqKuRO0B5escV0ugQ5qxO-KKw7ncuCLznQ08jlrhpxe9xCOyNs3bO1wKS4jhtr5b2HRK2YwjYN9-_-pxPa9BW7SGpMPKIBWUhEXLMGnH528jN-20P5WULnEdZB0rwLDW7ygwMfTvMOyhH_7Mn4CVPxBD2wYttVBHED9XWq2tnoIM-xTHeHCwARTraXR9E0So0BI0lI5NUKRPvTyhu93rzrcS9f_hXQdV05oEEyHX1rY8923op3oMrk_q8VePxHhT0n4_oQuap4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
كانت داخل شاحنة اردنية..
كمارك طريبيل العراقية تحبط تهريب سحبة أركيلة إلكترونية متكاملة و(390) قطعة كارتج و(310) قطع كارتج إضافة إلى (12) حبة مخدرة فضلاً عن قطعتين من مادة الحشيشة بوزن إجمالي (5) غرامات كانت مخبأة داخل الشاحنة بقصد التهريب.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87619" target="_blank">📅 15:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">عدوان سعودي مدفعي يستهدف منطقة بني معين غربي محافظة صعدة اليمنية</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/87618" target="_blank">📅 15:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇸
فايننشال تايمز:
اوكرانيا توقف هجماتها على الناقلات في البحر الأسود عقب طلب مباشر من جي دي فانس نائب ترامب بعد ان اكد أن هذه الغارات ألحقت أضرارًا بمصالح الشركات الأمريكية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/87617" target="_blank">📅 15:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇩
وزير الدفاع الإندونيسي:
لن نسمح بإنشاء قاعدة عسكرية أمريكية في البلاد، التعاون مع واشنطن يقتصر على التدريب العسكري فقط ويجب احترام سيادة إندونيسيا.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/87616" target="_blank">📅 15:06 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87615">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔻
رويترز عن مصدر إيراني كبير:
لا موعد لوقف إطلاق النار ولا شيء هناك لتمديده.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87615" target="_blank">📅 14:23 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇸🇦
🇮🇶
إعلام سعودي:
وفد أمني عراقي رفيع يزور السعودية غدا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87614" target="_blank">📅 14:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87613">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇶
وزير التجارة العراقي يبشر:
الدين الداخلي للعراق كبير جدا وتجاوز الـ200 تريليون دينار واصبح عبئا ثقيلا على الدولة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87613" target="_blank">📅 13:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87612">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇷🇺
🇺🇦
إنفجارات تهز العاصمة الاوكرانية كييف بعد هجوم روسي كبير صاروخي ومسير.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87612" target="_blank">📅 13:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feafd64b6c.mp4?token=fVwJFa7NFlcLlrc_vtcHtB9RiTq04R2dFApGN5PCbvJG-s7FiXK0rJbTw0QjM-9w-XTCJcE--UZNAqPu5jcMbTrCg-XU6aGnRUH7SwGkUFwFQ7mC5L2meDYaqz6BF0D4yfJ5z5zkdHyVyHT7w764-HaOk3V3wC1FQ4fLYhuSelqbdgs85-nB-RdF9CVfzE2DJWWg7XiLCuRBCimLQiitsM4F4m1IP91d2Emo4CDudeGBy_nnhg5ydzEiiXQhtErJ577V3YGtA-Go8CfozamJbODX57xlvQhiHbV7Tv80IYgB4g4YqUuWVbdr0A8UKHQ0RRGWFKbnxDgROSC3Z-ERDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feafd64b6c.mp4?token=fVwJFa7NFlcLlrc_vtcHtB9RiTq04R2dFApGN5PCbvJG-s7FiXK0rJbTw0QjM-9w-XTCJcE--UZNAqPu5jcMbTrCg-XU6aGnRUH7SwGkUFwFQ7mC5L2meDYaqz6BF0D4yfJ5z5zkdHyVyHT7w764-HaOk3V3wC1FQ4fLYhuSelqbdgs85-nB-RdF9CVfzE2DJWWg7XiLCuRBCimLQiitsM4F4m1IP91d2Emo4CDudeGBy_nnhg5ydzEiiXQhtErJ577V3YGtA-Go8CfozamJbODX57xlvQhiHbV7Tv80IYgB4g4YqUuWVbdr0A8UKHQ0RRGWFKbnxDgROSC3Z-ERDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحليق طيران مروحي مكثف في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87611" target="_blank">📅 13:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87610">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجارات تهز ميناء المخا في اليمن</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/87610" target="_blank">📅 13:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87609">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇴🇲
‏
المنظمة البحرية الدولية:
تسرب نفطي من ناقلة انجرفت شمال شرقي جزيرة القبلية العمانية ومن المتوقع وصول تسريب النفط من الناقلة كارولين بيزنجي إلى عُمان.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87609" target="_blank">📅 12:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87608">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجارات تهز ميناء المخا في اليمن</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87608" target="_blank">📅 12:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87607">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏بيانات ملاحية: تراجع حركة الملاحة في مضيق هرمز إلى أدنى مستوى لها هذا الأسبوع</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/87607" target="_blank">📅 11:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87606">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📰
بلومبرغ: مخزونات النفط العالمية ستنخفض هذا الربع بأكثر من ضعف المعدل الذي تم تقديره سابقاً مع تجدد الحرب مع إيران</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87606" target="_blank">📅 11:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87605">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇵🇰
الخارجية الباكستانية: لم نغلق ملف الوساطة بين واشنطن وطهران ويمكن تمديد فترة 60 يوما في مذكرة التفاهم</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87605" target="_blank">📅 11:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87604">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd6eb0f77f.mp4?token=SqThEWifJYxRBhl831yrJ5eEIVeaJeCDmkPe1KGTuZtnD42E7zugRstVpZUhm8Z9J8b9PptC84t3DxG41lhNT7sb6S-ulMWFsk-__yqz6hd0plqz9rl_JH4QC5dtbSyNxXudSrgtFuFDr9yIIGujwaBcjP68u1EzlNuOIdNcrmrZGAGBcvPAOakYSIXR-Vk3UHXR63qlZeaFMOJ45trewkh3fwPzSiupf9Az6eVk72sTiWRcDHJJAMkE--OSO0f0fd3YKXnnlQxClnK7mSNWuohYXTxvzKt5ie8xzr4ZpOpbQ-Y3lQQXHsEo1_hj0E3Oeqjj_JZAvp7T2JTwUn4e4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd6eb0f77f.mp4?token=SqThEWifJYxRBhl831yrJ5eEIVeaJeCDmkPe1KGTuZtnD42E7zugRstVpZUhm8Z9J8b9PptC84t3DxG41lhNT7sb6S-ulMWFsk-__yqz6hd0plqz9rl_JH4QC5dtbSyNxXudSrgtFuFDr9yIIGujwaBcjP68u1EzlNuOIdNcrmrZGAGBcvPAOakYSIXR-Vk3UHXR63qlZeaFMOJ45trewkh3fwPzSiupf9Az6eVk72sTiWRcDHJJAMkE--OSO0f0fd3YKXnnlQxClnK7mSNWuohYXTxvzKt5ie8xzr4ZpOpbQ-Y3lQQXHsEo1_hj0E3Oeqjj_JZAvp7T2JTwUn4e4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تحليق طيران مروحي مكثف في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/87604" target="_blank">📅 10:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87603">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36e86b5f40.mp4?token=bN6DY_nO0U6IV7DAn4IyEi0jD3zMD7A09K3zv0j-j4XTCODjYCU_EOceSjTOdA1xPlbwORFnXRQUufpQjQHzcoU-LyWtfMUwu95a88bBDNcBzNFSJPoqI7kmQg1VjAzuUc4UKkR8pgyfuLuM2FvjUnKzWzKAPBRvCgC_ny1Z6Dnr8zKfqJzhH0CrT_DLdq7lwbifebY4P0sezgt_BvxFwvv_oiI9zKDV6Nerl_l0G__Ktb9WUMrPDcoAWrYzR1dk04Hi35FsRjrlrwZnReCpTt1D1cfrRusMyCkCtAKA3s6OvcwxvxZ6gdtqPDXT8FK6WpLPKDiw4uT0W4gHENFraA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36e86b5f40.mp4?token=bN6DY_nO0U6IV7DAn4IyEi0jD3zMD7A09K3zv0j-j4XTCODjYCU_EOceSjTOdA1xPlbwORFnXRQUufpQjQHzcoU-LyWtfMUwu95a88bBDNcBzNFSJPoqI7kmQg1VjAzuUc4UKkR8pgyfuLuM2FvjUnKzWzKAPBRvCgC_ny1Z6Dnr8zKfqJzhH0CrT_DLdq7lwbifebY4P0sezgt_BvxFwvv_oiI9zKDV6Nerl_l0G__Ktb9WUMrPDcoAWrYzR1dk04Hi35FsRjrlrwZnReCpTt1D1cfrRusMyCkCtAKA3s6OvcwxvxZ6gdtqPDXT8FK6WpLPKDiw4uT0W4gHENFraA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بالطائرات المسيرة الإنتحارية.. إستهداف مقر تابع للإنفصاليين الأكراد في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87603" target="_blank">📅 09:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87601">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏بيانات ملاحية: تراجع حركة الملاحة في مضيق هرمز إلى أدنى مستوى لها هذا الأسبوع</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87601" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87598">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb4c8ae875.mp4?token=RE6fpl8-WYB9krfXqtYxgKG54WIZUrUhaX_FVFthcV15SnqHlp6jrwMjtWFnfw-V2Nd75YyfRYVfZrVQUGEJSwB7H4E3PtStOyhY9891o3UA5GORvkm2s3n9_grLDBBS5ddTDOUiPGXS0u05_8e6Ra-1pBjyng0sKmN2DbQWCkXte8WXFNVB6-1zyQhdEoRXo0HQXP49RFT1_VbYe8E5MlkAia6OWGiBBCFGIbr0PYZCCvF3tCJMuuEWzp0TOdlvrd9uISfquO-pnpTX93EtcgShr392n174xw5DthU2VXpiZKVhmbDjaO42-Jvj8F4ANy0g7K636O7poIVeh80g_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb4c8ae875.mp4?token=RE6fpl8-WYB9krfXqtYxgKG54WIZUrUhaX_FVFthcV15SnqHlp6jrwMjtWFnfw-V2Nd75YyfRYVfZrVQUGEJSwB7H4E3PtStOyhY9891o3UA5GORvkm2s3n9_grLDBBS5ddTDOUiPGXS0u05_8e6Ra-1pBjyng0sKmN2DbQWCkXte8WXFNVB6-1zyQhdEoRXo0HQXP49RFT1_VbYe8E5MlkAia6OWGiBBCFGIbr0PYZCCvF3tCJMuuEWzp0TOdlvrd9uISfquO-pnpTX93EtcgShr392n174xw5DthU2VXpiZKVhmbDjaO42-Jvj8F4ANy0g7K636O7poIVeh80g_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بالطائرات المسيرة الإنتحارية.. إستهداف مقر تابع للإنفصاليين الأكراد في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87598" target="_blank">📅 05:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87597">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a0d0bf3.mp4?token=tcr_Fj-2cnCJH22qu4Jj1L5WRLkUi6tmltTB5vLe7FREsqBB9ANMVaR4CtQv9_d9Hr0ttnwIy_0tECT5IAtWGeQ0jKr5BigeNZ98lkWSfqgFloOJYapvqFJeC7fOufL4yhxLKhnRVq5lnPCkYvih_hFhP9_Ky9Dvu9vT6i8qPi-Ry5WbM2EaL93IgYrm3dPZmoXWhZLBfqBmYa8TS8O0IDr-8tAQfLpG8fJuCrQesyXVxcBX3zIbuArhDx7GgmsadcLziVO3wZQoauRu1KO_HCKWChWadDPpk0GjALryV1csCGodl4SDkTreqllFSLFuj2DJvA9CTMUzsHd5zphJ2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a0d0bf3.mp4?token=tcr_Fj-2cnCJH22qu4Jj1L5WRLkUi6tmltTB5vLe7FREsqBB9ANMVaR4CtQv9_d9Hr0ttnwIy_0tECT5IAtWGeQ0jKr5BigeNZ98lkWSfqgFloOJYapvqFJeC7fOufL4yhxLKhnRVq5lnPCkYvih_hFhP9_Ky9Dvu9vT6i8qPi-Ry5WbM2EaL93IgYrm3dPZmoXWhZLBfqBmYa8TS8O0IDr-8tAQfLpG8fJuCrQesyXVxcBX3zIbuArhDx7GgmsadcLziVO3wZQoauRu1KO_HCKWChWadDPpk0GjALryV1csCGodl4SDkTreqllFSLFuj2DJvA9CTMUzsHd5zphJ2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بالطائرات المسيرة الإنتحارية..
إستهداف مقر تابع للإنفصاليين الأكراد في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87597" target="_blank">📅 05:39 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87596">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
ترامب حول تغيير الطائرة في أنقرة: الأمر متروك فقط لخدمة المخابرات السرية. أنا فقط أتبع ما يرغبون في القيام به. لذلك، أتبع تعليمات خدمة المخابرات السرية والجيش.  لقد طلبوا مني السفر على متن طائرة مختلفة، ولكنها توفر نفس مستوى الأمان، ولكنهم أرادوا مني فعل…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87596" target="_blank">📅 04:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87595">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5aec64b6d.mp4?token=ha49lu47kLtg6skClMqDsvMEYWntNVad4tiPQ4EmK_uk3O04LQi6YrmF8wMGuVBdcbEASJhcV0Ib67TcQeOsqEohDjdabh6WVLpBMrUwvEpOY7W8PIxzEkQLYfEjvW6xFcR0SaOVDbTNRaeVy06XS4uBX606qoM5-wjMmZAOsIo8JB6ToKrTpkeKCT95tqROhhKjQaX_KTWlN54nivBnl1X75aQNBXsksm-U0a5maAWDhuYI_-p11krktV_Spv18TmPd06iH1gwZGuWDxd6Su8HbeZfaQIBmc97gMr7gM7EHBEP2h0VY9H___uF82MX7WZBUiddZnFl-buMGdwDm8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5aec64b6d.mp4?token=ha49lu47kLtg6skClMqDsvMEYWntNVad4tiPQ4EmK_uk3O04LQi6YrmF8wMGuVBdcbEASJhcV0Ib67TcQeOsqEohDjdabh6WVLpBMrUwvEpOY7W8PIxzEkQLYfEjvW6xFcR0SaOVDbTNRaeVy06XS4uBX606qoM5-wjMmZAOsIo8JB6ToKrTpkeKCT95tqROhhKjQaX_KTWlN54nivBnl1X75aQNBXsksm-U0a5maAWDhuYI_-p11krktV_Spv18TmPd06iH1gwZGuWDxd6Su8HbeZfaQIBmc97gMr7gM7EHBEP2h0VY9H___uF82MX7WZBUiddZnFl-buMGdwDm8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب حول تغيير الطائرة في أنقرة: الأمر متروك فقط لخدمة المخابرات السرية. أنا فقط أتبع ما يرغبون في القيام به. لذلك، أتبع تعليمات خدمة المخابرات السرية والجيش.  لقد طلبوا مني السفر على متن طائرة مختلفة، ولكنها توفر نفس مستوى الأمان، ولكنهم أرادوا مني فعل…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87595" target="_blank">📅 04:43 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87594">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995c12d41.mp4?token=e8OjsFGt1WrVuVvNuyPCL8n_PZdHvulF18gNMAZwz56Uc5Ta8nDe_-KdGwEWQZsCEVPF68tqyqqiVHRWX9dDhMMeEmJCri-TfJfdu0FNwXebghXisfdVKpZEMSroe2l5UTqAnggrzJgJlUh8YORVMmDht4TyXI0YgY0580IN3eFxffhvoE1kf-LPO6VEZjV6tvjGLodL0UXF_dSA1RAPWgrKDjxCS-kBW88UXS6ECoOW97tVYHOVhlClYSPu63y7Y9kpeIMvb4UIu_PFks-trWGkJdiRWOEipBCFlwxJZUqtm5XcTJDwvg3Pwgad7ajZhcHki2qcZipOezuspWC8TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995c12d41.mp4?token=e8OjsFGt1WrVuVvNuyPCL8n_PZdHvulF18gNMAZwz56Uc5Ta8nDe_-KdGwEWQZsCEVPF68tqyqqiVHRWX9dDhMMeEmJCri-TfJfdu0FNwXebghXisfdVKpZEMSroe2l5UTqAnggrzJgJlUh8YORVMmDht4TyXI0YgY0580IN3eFxffhvoE1kf-LPO6VEZjV6tvjGLodL0UXF_dSA1RAPWgrKDjxCS-kBW88UXS6ECoOW97tVYHOVhlClYSPu63y7Y9kpeIMvb4UIu_PFks-trWGkJdiRWOEipBCFlwxJZUqtm5XcTJDwvg3Pwgad7ajZhcHki2qcZipOezuspWC8TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  انا لا أثق بإيران ونحن نسيطر على مضيق هرمز.  إيران كذبت في العديد من المرات وأنا آخر شخص أثق بهم.  ‏إيران لن تصبح المتنمر في الشرق الأوسط.  إيران قد تتخذ إجراء بشأن مضيق هرمز وتتعرض لضربة قوية لكننا في موقف جيد للغاية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87594" target="_blank">📅 04:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87593">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9de36f951.mp4?token=ODN2b4G4GibvpaHZ5BIkVSmhmNqVtM6sNYmC4eJVHBjHL9T6rh5pBhcOhJsk-LcjRjM_Bx10rxERTTIQ9_BzKMJXLs80a7-NRZd7BALtuchoDXIIK9pqjHcn5FLaQufTTA-kywEkibn7xsRdkQ1-NPMZiS1ATMgXkONinYz56mff1Vrk-OQWvKfjYA3CurtQPaBUJx7zNAiARJsnE93jEHPrqpv5l2aP8uVzg2ErKKL_xy6dDrA-5V4sW_G-4p4RtqhcPQrVZpxMkmHIxW8kdOGDo8hb4looXG4LYUmt7WWYCZ53dT2_O-zosfUbOKZ-U3ZAsb0YbYY_sp3oVVRlsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9de36f951.mp4?token=ODN2b4G4GibvpaHZ5BIkVSmhmNqVtM6sNYmC4eJVHBjHL9T6rh5pBhcOhJsk-LcjRjM_Bx10rxERTTIQ9_BzKMJXLs80a7-NRZd7BALtuchoDXIIK9pqjHcn5FLaQufTTA-kywEkibn7xsRdkQ1-NPMZiS1ATMgXkONinYz56mff1Vrk-OQWvKfjYA3CurtQPaBUJx7zNAiARJsnE93jEHPrqpv5l2aP8uVzg2ErKKL_xy6dDrA-5V4sW_G-4p4RtqhcPQrVZpxMkmHIxW8kdOGDo8hb4looXG4LYUmt7WWYCZ53dT2_O-zosfUbOKZ-U3ZAsb0YbYY_sp3oVVRlsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:
انا لا أثق بإيران ونحن نسيطر على مضيق هرمز.
إيران كذبت في العديد من المرات وأنا آخر شخص أثق بهم.
‏إيران لن تصبح المتنمر في الشرق الأوسط.
إيران قد تتخذ إجراء بشأن مضيق هرمز وتتعرض لضربة قوية لكننا في موقف جيد للغاية.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87593" target="_blank">📅 04:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87592">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0b4cce9c8.mp4?token=TamIVm-zpy7YbX0luR_mFiXK2Jxqgvkqu3zejGbsRX4ceqncWB23dVLot4wr_knPWJp19Jr6XRdwqSc47Q-MPPMYOxMuveI46xC0sFTvMSF_895JIyeTRUKZNR6AzG90AlkiTn20DeA1gemDN7DrMMcztZ1UrbbToMX9NZiqOKmIcKLKdoogDipsm8yLJr12RQD9V-YDVOyca-4xuJgmxqU8c_2ypKTG9FByy1cc82SRk2UZE0mqoWzsj4TU_MCXo9eIfyX5lOJlwVlMlWlNMJrEF2lCW6M7IRIHkc9NQe5kAk3ENhyBtMhyOOXX0DDIMO6RwoYUdls1BYAKud7U37pV4zRQBUqdRA3G-oPdb_cK8nGhu2Ay37MMaXAbPg_QjcWmVrMqqDa5psYsR6DsQDmuugvqL9pWxHvB2W2aOw1SKH-XY4SAGopcS1HsDfVVS71XbdCgIivlR4m37CgTHDtxBDqw2IWjkZzcubrmGsXnpPIocCiFtyNJxmB-z05NfcMZkVzqEoRfmAVOZ3UVQLvh81l6CeX_IuOjwfz9FtQJy7tQ8hC1LxTUVkWBkxq9zzcamdYC_WvHdQjZasjPIsO_6l6R9hEoePFJSgSzwoB4Ptb0_oOJCj30uhCP2s-5-AW9P4j4ddFUnKD-nwnFfSBRXzh0H1Fn0boNqTANdkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0b4cce9c8.mp4?token=TamIVm-zpy7YbX0luR_mFiXK2Jxqgvkqu3zejGbsRX4ceqncWB23dVLot4wr_knPWJp19Jr6XRdwqSc47Q-MPPMYOxMuveI46xC0sFTvMSF_895JIyeTRUKZNR6AzG90AlkiTn20DeA1gemDN7DrMMcztZ1UrbbToMX9NZiqOKmIcKLKdoogDipsm8yLJr12RQD9V-YDVOyca-4xuJgmxqU8c_2ypKTG9FByy1cc82SRk2UZE0mqoWzsj4TU_MCXo9eIfyX5lOJlwVlMlWlNMJrEF2lCW6M7IRIHkc9NQe5kAk3ENhyBtMhyOOXX0DDIMO6RwoYUdls1BYAKud7U37pV4zRQBUqdRA3G-oPdb_cK8nGhu2Ay37MMaXAbPg_QjcWmVrMqqDa5psYsR6DsQDmuugvqL9pWxHvB2W2aOw1SKH-XY4SAGopcS1HsDfVVS71XbdCgIivlR4m37CgTHDtxBDqw2IWjkZzcubrmGsXnpPIocCiFtyNJxmB-z05NfcMZkVzqEoRfmAVOZ3UVQLvh81l6CeX_IuOjwfz9FtQJy7tQ8hC1LxTUVkWBkxq9zzcamdYC_WvHdQjZasjPIsO_6l6R9hEoePFJSgSzwoB4Ptb0_oOJCj30uhCP2s-5-AW9P4j4ddFUnKD-nwnFfSBRXzh0H1Fn0boNqTANdkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربات متتالية تطال مصفاة الزاوية في ليبيا.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87592" target="_blank">📅 03:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87591">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
أُطلق صاروخ اعتراضي نحو هدف تم تحديده لاحقًا على أنه نيران من قواتنا في المنطقة الأمنية جنوب لبنان.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87591" target="_blank">📅 02:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87590">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da38748ac5.mp4?token=L1mgnRY2IoLs__sugu_n_Ff1F0uO6GLMoojTGJH-CKpCvKR8PqU-192Scxz5IzkmDbtzcq7YdQiuzSjwfaPDlOgJ49NUK1ozNEGLwsp4Nj2QeQ8fsXGBzUmDdRI2YLt-F_voIKNMY64YNYOhKpRDbUIcetblHKU2pXPcHdFlAQ7fPx8W3SHMQggxOPwWZoIVixPFFR81IHBSohdy_ocY7I4Fksv_17ber7lRWagj44FtTO9ujTv8WFbja2lVTlpa9Sc2uLesPLeemEh1v1aB4I2Ep0_e8Q-QQ3qRHOg4_btD6xy2nUdoAl0HSROGgkYW109BUgezdQBwlnlTRg2GPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da38748ac5.mp4?token=L1mgnRY2IoLs__sugu_n_Ff1F0uO6GLMoojTGJH-CKpCvKR8PqU-192Scxz5IzkmDbtzcq7YdQiuzSjwfaPDlOgJ49NUK1ozNEGLwsp4Nj2QeQ8fsXGBzUmDdRI2YLt-F_voIKNMY64YNYOhKpRDbUIcetblHKU2pXPcHdFlAQ7fPx8W3SHMQggxOPwWZoIVixPFFR81IHBSohdy_ocY7I4Fksv_17ber7lRWagj44FtTO9ujTv8WFbja2lVTlpa9Sc2uLesPLeemEh1v1aB4I2Ep0_e8Q-QQ3qRHOg4_btD6xy2nUdoAl0HSROGgkYW109BUgezdQBwlnlTRg2GPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد من مسافة قريبة للحريق الكبير الذي اندلع وسط محافظة أربيل شمالي العراق والأنباء تتحدث عن حادث إنقلاب صهريج محمل بالوقود ماأدى إلى إشتعال النيران فيه.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87590" target="_blank">📅 01:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87588">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c98ac4fb.mp4?token=aY7WIxH6ODoML2hhbQdEILRMs7x2DzpmOexTiazmoXkbgTkngUDLddEbo85CGMAJ23UwXjUpQ2EVIY3hw248WLo0UV3jGA39tqPAU5JwMup6sO932r6-oh_dJiUSTvHjlYY5P07Yaum4J8eBA2dlHmgoQnQRwleawn0jNYrTnVwGsaAqgW6hd9ObV6S5gzw5nunIeoNXXOj61amtUBv5kA9g6w1Y46WT7s_NojnaHBxkJWymAplK3YaLUtsyr7vSN97JkmTt9cK6-_Iy8qJTJ3_Mu0B3dRGGxqt-ZENYIJwVSN42CBXGP7vSVCo-C2TmHfVS8YopkaoGeZlaI5l3cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c98ac4fb.mp4?token=aY7WIxH6ODoML2hhbQdEILRMs7x2DzpmOexTiazmoXkbgTkngUDLddEbo85CGMAJ23UwXjUpQ2EVIY3hw248WLo0UV3jGA39tqPAU5JwMup6sO932r6-oh_dJiUSTvHjlYY5P07Yaum4J8eBA2dlHmgoQnQRwleawn0jNYrTnVwGsaAqgW6hd9ObV6S5gzw5nunIeoNXXOj61amtUBv5kA9g6w1Y46WT7s_NojnaHBxkJWymAplK3YaLUtsyr7vSN97JkmTt9cK6-_Iy8qJTJ3_Mu0B3dRGGxqt-ZENYIJwVSN42CBXGP7vSVCo-C2TmHfVS8YopkaoGeZlaI5l3cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الحريق الكبير في محافظة أربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/87588" target="_blank">📅 01:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87587">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9acaf5a0.mp4?token=iksy9hAxXr5_XCjNkH-0Hjv9f0rSit_087e3_WWIlr3Rt6dKuLys49TPBizOmNoWkwRDUHxoJeh8A6DJMz9GSdOl-lQXFvp9KDQxIt5pTb6dCosXe1oxJVZXqAnzNB6V1SzTWYmfn38bzlHONn_6hpxPx5ox5ZULpNOyOJ-HdozaCRgGKajyz59g28dV0VkOagjC_yePBRRwCJF4eDpafoq9NBIU0e-BiJyD7orHORvOPqrQ8bRoLIiW3vJs2cprLhPSICmgEv3_YdQ5y__Izc_0cfvJBSv6cvdr22pH9VYXyGQqvWcIxXfFaMfveTWevFrudgaQI2ptUp_Q0VCJfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9acaf5a0.mp4?token=iksy9hAxXr5_XCjNkH-0Hjv9f0rSit_087e3_WWIlr3Rt6dKuLys49TPBizOmNoWkwRDUHxoJeh8A6DJMz9GSdOl-lQXFvp9KDQxIt5pTb6dCosXe1oxJVZXqAnzNB6V1SzTWYmfn38bzlHONn_6hpxPx5ox5ZULpNOyOJ-HdozaCRgGKajyz59g28dV0VkOagjC_yePBRRwCJF4eDpafoq9NBIU0e-BiJyD7orHORvOPqrQ8bRoLIiW3vJs2cprLhPSICmgEv3_YdQ5y__Izc_0cfvJBSv6cvdr22pH9VYXyGQqvWcIxXfFaMfveTWevFrudgaQI2ptUp_Q0VCJfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق ضخم جداً واعمدة دخان واسعة تغطي سماء محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87587" target="_blank">📅 01:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87586">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57fce359f9.mp4?token=sCK7N3JUxp43YenWhpKD5zuCAudDuwTPnwkBlVx1Z7I9S4UHdUsIEGBw0W6-2c1NJVwWqq9_aEUeVc6J5N3fLdTYRDCWFrS6ENIuv1AzsSEc3_Wd0AQwRPfMHRKoTow8pUFn0Nl_WATb31cO1ctk2gUcj5QUBDIcQPzFDztQ-zvhYBRKXw-VDzQZECGsewliheuZpmz7OpTaaj9F8HlZxCJQZwp3DiN4_lKB4h2XMaSGqtxk-S6i7fzxUL5Jh8Nu40EtYB4Lmk12FBbUARN6cciNOc2UMI1W-FgoJgiEFQWRaWw0Q6XLTxgyk_4LdbfOOOKx-3UA0gixWEY0UzK5gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57fce359f9.mp4?token=sCK7N3JUxp43YenWhpKD5zuCAudDuwTPnwkBlVx1Z7I9S4UHdUsIEGBw0W6-2c1NJVwWqq9_aEUeVc6J5N3fLdTYRDCWFrS6ENIuv1AzsSEc3_Wd0AQwRPfMHRKoTow8pUFn0Nl_WATb31cO1ctk2gUcj5QUBDIcQPzFDztQ-zvhYBRKXw-VDzQZECGsewliheuZpmz7OpTaaj9F8HlZxCJQZwp3DiN4_lKB4h2XMaSGqtxk-S6i7fzxUL5Jh8Nu40EtYB4Lmk12FBbUARN6cciNOc2UMI1W-FgoJgiEFQWRaWw0Q6XLTxgyk_4LdbfOOOKx-3UA0gixWEY0UzK5gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إندلاع حريق كبير في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87586" target="_blank">📅 01:32 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87585">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38bb20ca7d.mp4?token=p7GMHDTL_Wr_YHPHcx_P156vZNKIvZDWzyE0vIHUhCumAw6hbKG4D2U6Tp0mLkdreC1wULgaSLjwzrZt4axfIDpZNug9dAJJaum_vyCv_mqsrqaTHMHX2Pim40cXwIbBjXSbzmV23v2EVO-ekxFeq3yDsa1ycia_11YnGnMKrA-A8jAAv6XMGF32gCWjlqbUAgdimEhw8KUAyjTaXMcCQWzDM9JQgyQU_tC80PDHxG1CnXeF3RG5zMnxcdDk_Gx8yk5eoRwPZ3KZngIJYymDq01U_hnSaBylLKethQGgz1g-bGo134rTa6rBwanxAH5NKjyXPDZxvr8yZfVnW53oxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38bb20ca7d.mp4?token=p7GMHDTL_Wr_YHPHcx_P156vZNKIvZDWzyE0vIHUhCumAw6hbKG4D2U6Tp0mLkdreC1wULgaSLjwzrZt4axfIDpZNug9dAJJaum_vyCv_mqsrqaTHMHX2Pim40cXwIbBjXSbzmV23v2EVO-ekxFeq3yDsa1ycia_11YnGnMKrA-A8jAAv6XMGF32gCWjlqbUAgdimEhw8KUAyjTaXMcCQWzDM9JQgyQU_tC80PDHxG1CnXeF3RG5zMnxcdDk_Gx8yk5eoRwPZ3KZngIJYymDq01U_hnSaBylLKethQGgz1g-bGo134rTa6rBwanxAH5NKjyXPDZxvr8yZfVnW53oxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إندلاع حريق كبير في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87585" target="_blank">📅 01:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87584">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
أصوات إنفجارات مجهولة في سماء منطقة السيدة زينب بالعاصمة السورية دمشق.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/87584" target="_blank">📅 00:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87583">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtVaZDW94LXjqgUMoRYPUn7edJTYDRJX5VLi9VBY8tRHUx-Ko1aZU-qEMw6UKdlRvIyQzdyKDoeXvkSGfM3DrENYqO1V_91U5yCI-I1FFIVKn5-uZ09K8RT49fa37WCyN9qx7bajIF3IRwBHfLiixHha5dXc-YTacPt5mwzXBo_OIeMQ3o18V1RZT_8nJXqIhrxdMyC5YySDzvSVmJRclAvnGXrdFcdG8nPCXQ0PO-ewk9QZOv4rCwTgxJ6BJhVK0Re0YF5hWQSEn5PKjjfrXuzUYSrw7JafiAUDGw5qtidc4eMdNX-UqWOgPITFlEuATLlrMnpmyDY7A4AY-ImklA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
الأدميرال علي عظمايي
قائد القوة البحرية للحرس الثوري؛ رجل الخطوط الأمامية في المواجهة مع الولايات المتحدة</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87583" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87582">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي منشغل بازمة الصواريخ الاميركية:
أطلقت القوات الأمريكية حوالي 50 صاروخًا من نوع "باتريوت" لاعتراض الصواريخ في يوم واحد، خلال الهجمات الإيرانية التي استهدفت القواعد في الأردن في الشهر الماضي. ويقدر التكلفة الإجمالية لهذه الصواريخ بحوالي 200 مليون دولار في يوم واحد، حيث تبلغ تكلفة كل صاروخ حوالي 4 ملايين دولار.
استخدمت إيران صواريخ ذات مسارات قابلة للتعديل لإجبار الولايات المتحدة على إنفاق مبالغ كبيرة وتقليل مخزونها المحدود من صواريخ "باتريوت".</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87582" target="_blank">📅 23:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87581">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
في خبر مفرح للشعب العراقي
الأنواء الجوية:
انخفاض تدريجي بدرجات الحرارة بعد منتصف آب واندفاع كتلة هوائية معتدلة نحو العراق.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/87581" target="_blank">📅 23:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87577">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RFb0n9T-bTWELtV64sb7HQx2p75GM-1WBJ33hI-MqpTrPGFBwfc-NWgB4OrDHYtmDJQ7OcFbBEFarmFvbBJK1nRUziprqEP3-4gzAw-HHdlRrDjvPvWeIW5WPJxy_RmZrtYXXFMjr8N4rf9gfLx8kfTAGiqk_EwNrwQ57sAzxpbzo5ekOZyJuRIuU4vNTYmt0yAvQREJBf34v7lJPypkdgEAVsWiJ4G-68U-hdxaeQ2gHf3Y2E2bNONsYo-UJK7uceM6y4Cx9D1zcXZpOmLSZiZLjCogroG9oo8TkKWzc_YXdbpXA6MhpFln60Sfh8RJlhsVEWZaHIwUryT0_WziWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MAaOZViDHaY852El_77PVQfdYXSljgjBtv-1zEWPh9cx6TETsZOmxCjmG2ppkdMpoUklu0uRvaLx5GvXbSvqUB_7py7n57nk4I_vZQogr7YgW9NguuqtQS3icjunleirKc_qwjHQuvmrewhrKrUMZFZGiaF7bIG-SyGmxWmqcE9R10BIqjmBfD3GTFt58qvksxipfreQpW2-EjwlRpdVBsLS-u6bYpLrFMTyEIYpS8AdjveVfXI5IHjiBHQJAyCTigbe972YVK7vE4YGJbO7OtbBKmLLW4XP1LOy9aPqi8V09rtUPnHqWWwtx8V89xyXf0lf1Lfk3PGjbuLzOAsbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ow0dlG7apzcPOYlDfc0DE_bPV5Yw67DOjQIzbWiwB1usT4xf9VGD0QK5vZITn0DWNaPRCIEDxV_bnGFhRDxXry32MS6jbuyqzhJmaAWPcV8s9Kbm4X9Fie4U0F-mxzVO-ww3Bp6wMdnEvNjdzJpY-cQ5WKfUw-9KCYUSPC5vgTXL-R8DHBNdpR7RhYeG68Uqwc33fHEg8mGx4qBuqIGoaXQWvt8SXELkKAJOuDWlSRQZ4mz4SYbXPE5qxJsr_18eha_u9PE4TBKNzADF0wGqRnjhiKwdBjZHsUnO7z23qABWasaGBt5JYViBeoAeGzeSuh60L3WspWjdQ_B06eKcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Anu1WERRRESWgr_s1VJk4XEcb4rRfic2TJpkU8AVYroW8tAYWXgrSOXOjeRrGSE_VsOTbPLiuERRfqxr8gvG3mpNsr0DBois9Vzj_Q8dql0i3xFkuE5Yg3uN_o39-qAAw4tFHrr4vJIA1dlxUiglv8RRxj0-AMv-Dnxlnmm0tmyFvUoI4VL5FewgV3OftU8nIcS9ErnTukqBaFgqFU7lpNR4x7sJ4dsW0xWDbRJnuQ8CChFLHoAdRLfvBA-oQNR8_zHXApQL79Qyc-fQ3e99L9A4XxclunIBDpZCgF5941AWLPHgT-CH3UjFSlPWAw44SjpX37p7XlbqsGsaM05Jfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
استهدفت القوات المسلحة اليمنية سفينة نقل معدات عسكرية سعودية في باب المندب.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/87577" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87576">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇾🇪
المتحدث الرسمي للقوات المسلحة اليمنية
:
تمكنت القوات المسلحة اليمنية بعون الله من استهداف تحشيدات العدو السعودي ومخازن أسلحته ومقار قياداته في منطقة المخا و معسكر تداوين في محافظة مأرب وذلك بعدد كبير من الصواريخ الباليستية والطائرات المسيرة وكانت الإصابات دقيقة بفضل الله وخلفت عشرات القتلى والجرحى بينهم سعوديون.
إن القوات المسلحة ستواصل عملياتها في استهداف كافة التحشيدات السعودية التي تسعى من خلالها للتصعيد والسيطرة على بلدنا العزيز.
تجدد القوات المسلحة تحذيرها لكافة المخدوعين والمغرر بهم من أبناء بلدنا إلى مغادرة مربع العمالة والخيانة قبل فوات الأوان.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/87576" target="_blank">📅 22:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي يوجه بإعداد مشروع قانون لحصر السلاح بيد الدولة وفقاً للسياقات الدستورية.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87575" target="_blank">📅 21:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇾🇪
استهدفت القوات المسلحة اليمنية سفينة نقل معدات عسكرية سعودية في باب المندب.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87574" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇾🇪
سماع دوي انفجارين متتاليين في مأرب.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87573" target="_blank">📅 20:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87572">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfIcEvg2P9M6hjv8ssOd4B5u1IRMHrHk2cHmOiu1Qxc7aiWxNnaL2xgw63aga9Tz-XdIMogM3oKrquzFll6oA01TW94TccSPM2eExUdeOJiLnBo9_HcNerhW15jV2w3_y96Kwd2hKOUudfPtOzuO9WkaLBqQL5vNNhvW1IfbC_idtxAZJ8DmU2Z03Cn1LaKz09IUGJn3fVgbMXmhsu9plzNm0a3ZnlE3AL-NZbXJTpxz5WOsyCFH1HCUJFd8UtRrgubuoXMUEVzxVpn6bG6qsI27m7OfXIvg1qNCvYAejOHvJhHy5_pLpFv5KOVtJ8qtcaUvPnr5V8rRC6I-r5h_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربات متتالية تطال مصفاة الزاوية في ليبيا.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/87572" target="_blank">📅 20:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87571">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtC-y_jwaPDyNGUK0A9ctKKETmXiJaRanJCBcxFCii7fo1XOL2gNnBTwYMI46jmuCVrU5lCi_5udhdo1tSjpX-AXDSllWSc6FhNkP2xktZnqbL0wVBQMKOT9Tpudb7V2us8Ezjz9mTk_kmxiZOkbe-o7piHBwcuajf3vpa4VJN1wcHqvXbYfGscNPIRvloAuWe-wuDVaqWiqQFlR5PqvEi_6DYLhIqmqXfa3r-umMYQJi8c2Dxeb1TDMBL_ZTJrCL52XQ8t6NSycaNebv2HD33Kl8TeoslCbnB9e2hlqPIJ8dUjQkE53E7LU1uTB4VGNpch-xfLEPaR4viWS1bMxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
‏دميتري ميدفيديف: أفرجت روسيا عن الجندي السابق في مشاة البحرية الأمريكية روبرت جيلمان من الحجز لأسباب إنسانية. وهو الآن على متن طائرة أمريكية تنقله من روسيا إلى مطار واشنطن دالاس الدولي.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87571" target="_blank">📅 19:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87570">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏ترامب: "ستصبح دولة جهادية. انظروا ماذا يحدث في ميشيغان..."</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/87570" target="_blank">📅 19:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87569">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">المركز الأوروبي المتوسطي للرصد الجوي:
"أفاد شهود عيان بحدوث هزات أرضية في كولومبيا قبل 5 دقائق"</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/87569" target="_blank">📅 19:27 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87568">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EANCxKG8YFX8IWdfcmKrtYOhtDGBJIj9HD2ZyfOg6iUc_fPF20yewCtozZHujmIHRvIH1UOTXH5epX4yO29slXEh40GCD6a1cvvqAjOwHg1c1KQIAOhK13A7rmIC6DFqQFIiU2UmcIr1QYnMj_aa62Ci3u0TCrLgWCOAfoOMzOyM6DCplEkz0Dkd34o1ZzZvk-mrj2gHyjhgTpLYMRxh09W19K-Vuq0qvXE4i0PvWoQ4Yt1_93JPtZS2M4GdmG3QUkJSEqAwjKQbKiQbXiXIfDUw_3qw6uDBTvlA1uPgQEn5P2074xDuQHSRwHxx4spPw-SVHhCTk3i1xis1C9SZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
تكلف ضريبة الشقق الصغيرة في مدينة نيويورك مدينة نيويورك وولايتها ثروة طائلة، حيث أن الأموال التي سيتم الحصول عليها في نهاية المطاف ضئيلة للغاية مقارنة بالضرائب التي يدفعها عشرات الآلاف من الأشخاص الذين يفرون من المدينة، ولن يعودوا أبدًا. فلوريدا وتكساس والعديد من الولايات الأخرى تجني ثروة طائلة! هذه "التجربة" السياسية الخطيرة في نيويورك ستدمر ما كان يومًا مدينة وولاية عظيمتين. إنها ساعة هواة بحتة، ومن الصعب، كرئيس للولايات المتحدة الأمريكية، أن أجلس مكتوف الأيدي وأشاهدها تحدث، خاصة في مكان أحببته يومًا ما. الخراب المالي، ثم الاجتماعي، أمر مؤكد بنسبة 100٪ - ثم يفرض الجهاديون اليساريون المتطرفون رسوم الازدحام فوق كل شيء آخر. هذا لا ينجح في أمريكا، ويجب إيقافه، الآن! أبحث لمعرفة ما إذا كان للحكومة الفيدرالية أي حق قانوني في تجنب هذه الكارثة، قبل فوات الأوان، من أجل ملايين الأشخاص الذين يعشقون نيويورك ويرغبون في رؤيتها مزدهرة، بدلاً من أن تصبح مكانًا قذرًا، مليئًا بالجريمة، ومتهالكًا، ومثارًا للسخرية والازدراء. لنجعل أمريكا عظيمة مرة أخرى! الرئيس.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87568" target="_blank">📅 19:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87566">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
انصار الله شنو اليوم هجمات متتالية بـ10 صواريخ و4 مسيرات على مواقع في الساحل الغربي بمواقع تمركز مرتزقة السعودية.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87566" target="_blank">📅 18:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87565">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgupGiE-Vn8Jr7IJASuwygdDG1oGvg2IhPiUlJj2_Jjl4k9d0ZBQN1HnztRGSXe7FQPZXiHJJcY0_tDTV0gbPG77HV55mwY1trocV6C03YT2Viuckw42KM4G48C2Ke09UZVGplYBpRZ6jQ_B3Lw_icoca9z1839cKVWDd7Pb0aQn-JbHRjRJcaqAyed585YSGnAf7cDfIjIk9P_tezpMBQeKbksArRqgHDjwe7aCv3l98S2bNsO4WvWpKhTlJnq_MDIvctLpySVjQn2_b0rAufl9cKusJie8FXzxhjOOcW1WO1LRp3M3pfwYarTm4gplwt9gwbC_ASmdPS-D0RWrsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
‏
نتنياهو
: الجولان أرضنا وستظل دائما لإسرائيل.
🇸🇾
رد الجولاني: حكم على بشار الاسد بالاعدام
.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/87565" target="_blank">📅 18:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87564">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇶
انفجار عبوة ناسفة بالدجيل جنوب صلاح الدين ؛ اثنان شهداء كحصيلة اولية</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/87564" target="_blank">📅 18:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87563">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇷🇺
‏
دميتري ميدفيديف:
أفرجت روسيا عن الجندي السابق في مشاة البحرية الأمريكية روبرت جيلمان من الحجز لأسباب إنسانية. وهو الآن على متن طائرة أمريكية تنقله من روسيا إلى مطار واشنطن دالاس الدولي.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/87563" target="_blank">📅 18:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87562">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
شرطة البيئة العراقية تكتشف كهفاً في صحراء الأنبار، بداخله نهرٌ يحتوي على أسماكٍ نادرةٍ جداً عمياء بلا عيون.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/87562" target="_blank">📅 17:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87561">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇷🇺
روسيا:
القواعد الروسية في سوريا سوف توفر مركزًا لتأمين العمليات في إفريقيا.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/87561" target="_blank">📅 17:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87560">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اصابة 14 راكب خلال رحلة قادمة من جزيرة فوكيت على متن رحلة الخطوط الجوية الهندية بسبب تعاطي قائد الطائرة للمخدرات مما ادى لانخفاض مفاجئ في ارتفاع الطائرة بمقدار 300 قدم</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/87560" target="_blank">📅 17:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87559">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامب: يتحدثون عن نقص الذخائر. السبب في انخفاضها ليس حربي مع ايران بل هو أن بايدن قدم ما قيمته 300 مليار دولار لأوكرانيا ‏عندما غادرت، كانت الخزائن ممتلئة. قام هو بإفراغها ولم يعيدها.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/87559" target="_blank">📅 17:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87558">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامب: سعر النفط أقل مما كان عليه خلال إدارة بايدن، وقد منعت إيران من امتلاك سلاح نووي لأنه لو لم أفعل ما فعلته، لكانوا يمتلكون الآن سلاحاً نووياً، وكنت ستخاطبهم بـ'سيدي'.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87558" target="_blank">📅 17:12 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87557">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/296520615b.mp4?token=qU6VEGIfamQUyZ8bud2R1nU-9Iivsw-Z2WXTrqR1MHvIQnszga2R1WPZCywLHeFNrdPZfiiy6JjkT5XZP1vEpaT22dbbhLblfh1-oOHtQ1CJG1L60N99MVXoGqpj0k9uT9bSX8cElwUvaXLSyDQTKXUjT7hoc5Q0xoJN1k8kx30P8dut0mup1YEtZQDcAdLfLxr_Gdg3YbnG1wu-HkzfudN8LwFgU7RqxwGPqj9j6HBZF63zibE528CLab8lFoBUd8t-y1F_7fsH4vaKOXQrkFojk15jjMlk9ad0de-p6emaxdyk255UwDwSoJ4L1mD8XTWFlz65J6SvBmmndlgSXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/296520615b.mp4?token=qU6VEGIfamQUyZ8bud2R1nU-9Iivsw-Z2WXTrqR1MHvIQnszga2R1WPZCywLHeFNrdPZfiiy6JjkT5XZP1vEpaT22dbbhLblfh1-oOHtQ1CJG1L60N99MVXoGqpj0k9uT9bSX8cElwUvaXLSyDQTKXUjT7hoc5Q0xoJN1k8kx30P8dut0mup1YEtZQDcAdLfLxr_Gdg3YbnG1wu-HkzfudN8LwFgU7RqxwGPqj9j6HBZF63zibE528CLab8lFoBUd8t-y1F_7fsH4vaKOXQrkFojk15jjMlk9ad0de-p6emaxdyk255UwDwSoJ4L1mD8XTWFlz65J6SvBmmndlgSXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مجهول يحلق في اجواء محافظة كربلاء المقدسة وعدد من المحافظات العراقية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/87557" target="_blank">📅 17:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87556">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2516bb44f8.mp4?token=sa18il-R05s00rLVBewjX0ViSoEcMgkbJMgnt7q3IGLPqVNIiJHSqMCkL8WdLxj6oy-XcwU9TxHRtE4Kg81LZndbWH6axjf8LK-ZoWVMm9VSFBkolsRI4irt9AsoU_5kDL02rMxzc9hEpjgYBKUBW6R0PF709TBlQw6GiqHY1-VuzfLbOse1y05U5H5_r8XX2-UTB_vZ4yi8XY4eAOa3udPVd2XtxCGUKS3FL4VNVT4lxQzYbheLQSRn17xuCqQMmgaZ-MQQ6zVRi8ftMkVHGGdpKuTqtXtrAP7tfBr2W-PKu6ytfUEaHlttC882vs4ERhQE_fuBXIvQ9PPHIOlRmZfDo45yGX4V155dX6LdpppZ_wWF-dsVuTtQxEhDRU-9sIugs0W1UA5zNfg398Lru0hpJI01PiIe43bXMFD_sxlybffLT5rEWrCRcpjK00JWMWTk2yvAOH3rnrCq8BXCb9nof7fjdcIY2oaiMpSyM-mx3-7BVBDT_w6SPGk9g07eX_po9xvqhPCglj4uAm7LlGI9hWThmVA-pKcQ3_edu9yRfVLFD4SokMU08osD7r3Z2KXHyJ353TgYKoKEbPrdFiAowloLLa6cs6E4CO9zrs3k9a5y52r1HYooCCvZntvcCPDWnihwR-9hohEqwk85Dz0QpSSQ7YyS20yXYGozGi8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2516bb44f8.mp4?token=sa18il-R05s00rLVBewjX0ViSoEcMgkbJMgnt7q3IGLPqVNIiJHSqMCkL8WdLxj6oy-XcwU9TxHRtE4Kg81LZndbWH6axjf8LK-ZoWVMm9VSFBkolsRI4irt9AsoU_5kDL02rMxzc9hEpjgYBKUBW6R0PF709TBlQw6GiqHY1-VuzfLbOse1y05U5H5_r8XX2-UTB_vZ4yi8XY4eAOa3udPVd2XtxCGUKS3FL4VNVT4lxQzYbheLQSRn17xuCqQMmgaZ-MQQ6zVRi8ftMkVHGGdpKuTqtXtrAP7tfBr2W-PKu6ytfUEaHlttC882vs4ERhQE_fuBXIvQ9PPHIOlRmZfDo45yGX4V155dX6LdpppZ_wWF-dsVuTtQxEhDRU-9sIugs0W1UA5zNfg398Lru0hpJI01PiIe43bXMFD_sxlybffLT5rEWrCRcpjK00JWMWTk2yvAOH3rnrCq8BXCb9nof7fjdcIY2oaiMpSyM-mx3-7BVBDT_w6SPGk9g07eX_po9xvqhPCglj4uAm7LlGI9hWThmVA-pKcQ3_edu9yRfVLFD4SokMU08osD7r3Z2KXHyJ353TgYKoKEbPrdFiAowloLLa6cs6E4CO9zrs3k9a5y52r1HYooCCvZntvcCPDWnihwR-9hohEqwk85Dz0QpSSQ7YyS20yXYGozGi8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: سعر النفط أقل مما كان عليه خلال إدارة بايدن، وقد منعت إيران من امتلاك سلاح نووي لأنه لو لم أفعل ما فعلته، لكانوا يمتلكون الآن سلاحاً نووياً، وكنت ستخاطبهم بـ'سيدي'.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/87556" target="_blank">📅 17:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87553">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794bf9e946.mp4?token=op-mn9gmgAKV4JH3RtzMBGVyf_d50JhF9RnYMmf40EaSJ9V7MGIOejRBl6HrUYXbmGWqPhp8WMVGQBfY-wO0GMWjB5bowTjLa_iL49hDHs-qQslPR_RmbSujdofAd6bxfdZ_BFx8PAWAAnIFQb5bAu1MZ5vLXJC6_B1p5gZnoQvitrTKYgGhreH4Dr93uE9mfr4KUIjqDVzURDeB8JXsHfn3UYgejribB9BwrP_ErtAR7gs16Vmo8i721vxKRFf_6S2hvucMAKJcZI4jV9-aNJOsZoxibVlT1n_kd08LNv1yBuXXVDBs-k98qZrp9c92DhCgSK5uIliifyaPdfqMdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794bf9e946.mp4?token=op-mn9gmgAKV4JH3RtzMBGVyf_d50JhF9RnYMmf40EaSJ9V7MGIOejRBl6HrUYXbmGWqPhp8WMVGQBfY-wO0GMWjB5bowTjLa_iL49hDHs-qQslPR_RmbSujdofAd6bxfdZ_BFx8PAWAAnIFQb5bAu1MZ5vLXJC6_B1p5gZnoQvitrTKYgGhreH4Dr93uE9mfr4KUIjqDVzURDeB8JXsHfn3UYgejribB9BwrP_ErtAR7gs16Vmo8i721vxKRFf_6S2hvucMAKJcZI4jV9-aNJOsZoxibVlT1n_kd08LNv1yBuXXVDBs-k98qZrp9c92DhCgSK5uIliifyaPdfqMdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مناشدة انسانية عبر بوت نايا
بعد منعهم من الدخول بريا خلال زيارة الاربعين من قبل السلطات الايرانية لاتاحة الفرصة للزائرين الايرانيين.. مشاهد من محافظة ميسان لاعداد كبيرة من الزائرين الافغان والباكستانيين الذي بدأوا بالدخول الى العراق من الحدود الايرانية لزيارة العتبات المقدسة ويعانون من شحة وجود المياه والمواكب على الحدود بالتزامن مع ارتفاع درجات الحرارة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87553" target="_blank">📅 17:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">طيران مجهول يحلق في اجواء محافظة كربلاء المقدسة وعدد من المحافظات العراقية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87552" target="_blank">📅 16:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87551">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
العثور على رفات 12 مقاتل عراقي في مدينة الفلوجة ضمن محافظة الانبار غربي العراق قتلوا على يد تنظيم داعش عام 2014 وفقدت جثثهم.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/87551" target="_blank">📅 16:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87550">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مرتزقة السعودية في اليمن:
مقتل 4 بحارة وإصابة 4 في هجوم لانصار الله استهدف سفينة في باب المندب.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87550" target="_blank">📅 16:41 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
