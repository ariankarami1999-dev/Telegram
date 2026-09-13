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
<img src="https://cdn4.telesco.pe/file/t39hrraEYRoNkc6VkKUwTQXS4VxA544xA_qd241Odc-9cxonTwCjHsJG9775harmsOHjYPkt28HRI5MDgdd6vFlA9oYLKhre0Bjsof5FAl5YJod8JJo5__MBNXdoevXXvIlprIcUKkisqmE5fog7UadyO94Jz4bD3bNheqAYBNa0FSeUimR2xbGXfBfn1TSAVRSgnSW9pG0Zkcx6JtR1B9WTXgVrR8as0TkagJxBkd0i7dAC_WCm8eoDktBAjok7SZriJu7RIRPXr18ohDJZoiqymR3Jk6BbYEYiUZXtx7KMry3fvIvd99xU3Nf08ihbFBDhLllrszxf8JYgvGD3qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 03:18:25</div>
<hr>

<div class="tg-post" id="msg-90441">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فشل كبير لمنظومة الباتريوت الأمريكية في صد وإعتراض الصواريخ اليمنية التي دكت مناطق جنوب السعودية.</div>
<div class="tg-footer">👁️ 37 · <a href="https://t.me/naya_foriraq/90441" target="_blank">📅 03:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90440">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تنفيذ عملية تأديبية واسعة من قبل رجال أبوجبريل على آل سعود</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/naya_foriraq/90440" target="_blank">📅 03:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90439">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">تنفيذ
عملية تأديبية واسعة من قبل رجال أبوجبريل على آل سعود</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/naya_foriraq/90439" target="_blank">📅 03:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90437">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FEANBpHmg8g14ez6p04fHWyZOw-oG9-cb7xmUkPA_4Gji45BrVKeitjHOQV1uEmrSAlBAr1_Jxdr_qz8_UKbvWqLSO74eIA_6_GzXtFM_HyOvY_hXghDC_9zkrhm0Y0tQ8jVkKbjnl0ruIaqAiF4JFBOZVQ7DkDUB5icCkOhorWrryav1X5Dz8g4xy73E-Y0ghTdQJdWsTB0mXI5hHJDaOcUbvG5MFw36tgPrpkWlsNDE5dH-j4CrLMYarVNCREoG3mQ2SIKRQPrfFbNzTBVCFqkk4XNuk1lmNYqmSKKcs6YhuOfyVyiO-ESGsR34chE5BlaMM0paed8_2Gnl-WSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLJRRip4VsDEIcCWYjJLe3W_43J3P6NfT4WkcR9lQJn3nH1h_hu7Iiuj1zM25qCgJf4cuDem2fqM9wZnZbHrApGJHy_4MlvW9H-emZv3-hDd6mpZqmFJbHVb6O3LiFYR4pELqGqMomQNvLgdotgllIq5mKX1C31iCzzi51qCj69ucega-OD4luE3Io_QU_-YmQuogCg8KrR0g3h8kvaKBqpQhqqKUXX1xKAO5FJX_7gBud4G8lUaSoW0sPaFDNoizBCPLuOZhE-2K5JX4_Q3ZxrO--scE-yBBXts6MtJs0XyRRoSjXyPILd5SxiSbNwTa-T11dhLVb6C4gZZluV_2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اصابات مباشرة في منشأة نفطية بجازان السعودية</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/naya_foriraq/90437" target="_blank">📅 03:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90436">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXWfrq-_CTRSubYeAyduYaXBmTr22U81yz2jBFw8LfV2kJIvqHLB5O1YgifypJwf9hHGTuNnsfyfVf41CfD97DfLd0JluonYEOFQnneQPqtev7foWwFEPHkhM2_lwO1BfD4Hw62wPbKYCJjx-wFVGmlX4WL87Xl0DBvdJAHW8_6REAbo_eO4AKHeAQ3Ctohf2bSzJdvpHEMDO9XZG5Dj4Y2dNUE7DZlBPeWCMcYScMIegtHvd_vJTWUyqxIU_MXH23t_8FmCq7kdbBsxJ23PotqeYdxC6ESB8auNhbfiEilS8EjK6JVrOhdep7el5wJVBRQpwgwqZKcjaqFXpYgpKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نجران اصابة مباشرة</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/naya_foriraq/90436" target="_blank">📅 03:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90435">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">موجة صاروخية جديدة تدك جازان ونجران جنوبي السعودية</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/naya_foriraq/90435" target="_blank">📅 03:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90434">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/naya_foriraq/90434" target="_blank">📅 03:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90433">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/naya_foriraq/90433" target="_blank">📅 03:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90432">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">موجة صاروخية جديدة تدك جازان ونجران جنوبي السعودية</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/naya_foriraq/90432" target="_blank">📅 03:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90431">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/naya_foriraq/90431" target="_blank">📅 03:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90430">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">موجة صاروخية جديدة تدك جازان ونجران جنوبي السعودية</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/naya_foriraq/90430" target="_blank">📅 03:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90429">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/naya_foriraq/90429" target="_blank">📅 03:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90428">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/naya_foriraq/90428" target="_blank">📅 03:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90427">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/naya_foriraq/90427" target="_blank">📅 02:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90426">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/naya_foriraq/90426" target="_blank">📅 02:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90425">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/naya_foriraq/90425" target="_blank">📅 02:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90424">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
ترامب: الكثير من كمية الديزل تأتي من روسيا.  تتعرض مصانع روسيا لقصف من قبل أوكرانيا.  لقد طلبت من زيلينسكي عدم قصف مصانع الديزل والمصافي.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/naya_foriraq/90424" target="_blank">📅 02:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90423">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تتمكن من دحر مرتزقة السعودية والسيطرة على منطقة كهبوب في باب المندب.</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/naya_foriraq/90423" target="_blank">📅 02:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90422">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e507f19a.mp4?token=b0vVNsx_KKKVihc-t9jg4zxdKa04Bpa5mtJBZQIRpExSfJGWGZW5IHDpKr-RXKTORc9ZwDOIq00jjwXd0NSl-rIe6v9YrJWzTlPu9vkN51RMFToyNqvRxWz6Zwmusv3nTAcgMxV7csIBLEbNf015a4YfqBdw8fAF09QEvhC543cP0HZ2e2MD2sqbgRsAPshnW6yJVyosCtDogDCPzorDnYwArtyqzJm6tONE5hAbpvQSbBrNFubPmjDKHr5WX-5cklOW1K9HRW49Ov5OVBIlSOnOj3IDmZhl1WH99jFfK-NesHgfw8bn6nFkWI0PMn8wt_QKz_ymURDUps49BCVqdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e507f19a.mp4?token=b0vVNsx_KKKVihc-t9jg4zxdKa04Bpa5mtJBZQIRpExSfJGWGZW5IHDpKr-RXKTORc9ZwDOIq00jjwXd0NSl-rIe6v9YrJWzTlPu9vkN51RMFToyNqvRxWz6Zwmusv3nTAcgMxV7csIBLEbNf015a4YfqBdw8fAF09QEvhC543cP0HZ2e2MD2sqbgRsAPshnW6yJVyosCtDogDCPzorDnYwArtyqzJm6tONE5hAbpvQSbBrNFubPmjDKHr5WX-5cklOW1K9HRW49Ov5OVBIlSOnOj3IDmZhl1WH99jFfK-NesHgfw8bn6nFkWI0PMn8wt_QKz_ymURDUps49BCVqdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
بعد ورود إتصالات من رقم أجنبي تطلب إخلاء مبنى..
إطلاق نار كثيف في حارة حريك بالضاحية الجنوبية لبيروت.</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/naya_foriraq/90422" target="_blank">📅 02:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90421">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">“
🇷🇺
🇮🇷
🇮🇶
🇸🇦
🇾🇪
The war involving Iran and Yemen is bringing Trump to his knees.”  This statement by Trump comes amid a rise in global oil prices, which have approached $110 per barrel. What is amusing is that Zelensky was carrying out U.S. and NATO orders in an…</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/naya_foriraq/90421" target="_blank">📅 02:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90420">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
المراسل:
قد تكون كيانات صينية قد زودت الإيرانيين بصور الأقمار الصناعية.
🇺🇸
ترامب:
هم في الأساس يفعلون ما نفعله. أعتقد أنه تصرف بشكل معقول، وقد تصرفنا نحن أيضًا بشكل معقول.</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/90420" target="_blank">📅 01:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90419">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWudg8gm2NC0dS1zBY-9XLTu6xaycpyCd1IwauKKJ0iuRTiCKBMtf4xF5HI20LLHuTXtbNZVB9SmsinSIyATh6YU_Lwu93r3ZnOif1MLoEEvvbGtSZsoxNvllXrI0z7-qXKtzqjvIXTtzNy3s0ZMydw2oG0dnVf6I7VTTkPdEl9ClsZMnDyS0dUvGFTidZiGzf8FT6rDR2fUpBLlCg7ibiQZoinApyCa2RgIgSE7H1Py6vbWdqbqsSHOvE7Pgw--1O30Moqeyg4p4BjU3h7KOBqbeV992HLwgLe4DvX40mUr0VA0HUqsJML-6TRE7JCN-2c1sHYm2AJvN0UaYdkf5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إرتفاع أسعار النفط العالمية حيث وصل سعر البرميل الواحد إلى 108 دولاراً.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/90419" target="_blank">📅 01:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90418">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔻
إشتباكات صاروخية في مضيق هرمز.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/90418" target="_blank">📅 01:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90417">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axZBXd0GRT5WtGaOj0XJljjiEIXo7HYIyPuntmrczpFOHKUm8rdzdx3kQFV53Srr-m6fjEEBMtGA_bN5ohIaE-sf0UBm7JCLwKGA_sV7-qwnX0tE-nwjluW49cEYLzsfwSkDuzNC1cXVNhDfOoCUgTwHWkcGTcbM7agX0uEC4tObycgBASB2nDUuxmmV32JaKh8f4NFFVwbCtnheKp6GHU1Yxy5FTpz7tot3a1ucACKyhibF-OlkdX3pIcDenu--k8NRql3vx1Iv5I9jGy1VwT2oW1fEUDOp178qABsWYZP-af6PbHQ_cSimzfIl7cvv2vkZWzFcCGk4My86_IkWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇺🇸
الأمن القومي الأمريكي يعتقل ضابطًا سابقًا رفيع المستوى في جهاز المخابرات العراقي رعد العنبكي، خلال فترة حكم نظام صدام حسين، في مدينة ديترويت الاميركية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/90417" target="_blank">📅 00:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90416">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66f7cf570d.mp4?token=Doq3IKdF7-dwqGysdXs_3kpMKbzLv_oGj7pK79n3_uJCVr7f_9GReYIQObEqzqrNHzTO_Nf8htyNwCw590Ngvw485f4xMD0eHPm7Sjwe8sTbKoeNJZT-3GwklIFDt1wa93YSzSR5kSkbHW96sekrjqv_dkHGEF7e3B-KffpkEyiW1UKZB-3lszjC1ddiKFnQZIt0BJgrDlIi3LMqKMjX-wVW0byUL6I203yI5vZ-dVR37F2JqdtAAp-yjr33syTF4AOdV-IbzrlMlwDyTnVCegJgQ8X_efPrYMX8kmVqFqwGpGrOKNTMOL4A4_yXo-LEi5Cq3M5rqLQ6lKzhTI3IAjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66f7cf570d.mp4?token=Doq3IKdF7-dwqGysdXs_3kpMKbzLv_oGj7pK79n3_uJCVr7f_9GReYIQObEqzqrNHzTO_Nf8htyNwCw590Ngvw485f4xMD0eHPm7Sjwe8sTbKoeNJZT-3GwklIFDt1wa93YSzSR5kSkbHW96sekrjqv_dkHGEF7e3B-KffpkEyiW1UKZB-3lszjC1ddiKFnQZIt0BJgrDlIi3LMqKMjX-wVW0byUL6I203yI5vZ-dVR37F2JqdtAAp-yjr33syTF4AOdV-IbzrlMlwDyTnVCegJgQ8X_efPrYMX8kmVqFqwGpGrOKNTMOL4A4_yXo-LEi5Cq3M5rqLQ6lKzhTI3IAjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المرشح الفرنسي للرئاسة:
الولايات المتحدة تستعد للحرب مع الصين، لن نشارك أبدًا في تلك الحرب.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90416" target="_blank">📅 00:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90415">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سماع دوي انفجار في سيريك</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90415" target="_blank">📅 23:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90414">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ba7c6492.mp4?token=fV-jkGbJAPqF_a6diIgqRQ5CVL3YoPDqNCXjfYpRNnpEaLZHl-4yb52Bt9q9VCnQxf94I0wMvm2ul69egfBIg8nofkxiIXvjceOy8R26XJQPXJubvPS1m4o_CE005fzDeWYEeQZV2UEk7jHGZR5uQUgxlYwbd6_bmBcF-E92MGD3TEEtoEryDmxY3VLg_wharqRIRfjeY1sozlaB30yNlq7P91lKiddhWW6tA5dTbQfd6fgjugn8do7EIT1i2MdHFZBMRLIU8Y48nzM5YBuO3bNyB2RJyDE7sOiYu3t-eQ1R0-0GFH69xNUC_bA6rRgATtK3iruV--93pj1HhbkXqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ba7c6492.mp4?token=fV-jkGbJAPqF_a6diIgqRQ5CVL3YoPDqNCXjfYpRNnpEaLZHl-4yb52Bt9q9VCnQxf94I0wMvm2ul69egfBIg8nofkxiIXvjceOy8R26XJQPXJubvPS1m4o_CE005fzDeWYEeQZV2UEk7jHGZR5uQUgxlYwbd6_bmBcF-E92MGD3TEEtoEryDmxY3VLg_wharqRIRfjeY1sozlaB30yNlq7P91lKiddhWW6tA5dTbQfd6fgjugn8do7EIT1i2MdHFZBMRLIU8Y48nzM5YBuO3bNyB2RJyDE7sOiYu3t-eQ1R0-0GFH69xNUC_bA6rRgATtK3iruV--93pj1HhbkXqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇸🇦
الشيخ همام حمودي
: العراق أكبر من أن يكون عضوا في اتفاقية مكة</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90414" target="_blank">📅 23:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90413">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سماع دوي انفجار في سيريك</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90413" target="_blank">📅 23:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90412">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B3WZoOS6nvS9LjewQzkP8MgTUVe707MMFbXi2u8BEL87gU4s9cQzZ3k3opzi6sy7DPpwE0bc8igBB-QRiV8awM2K-4dpg56jZENSE30OQLYDt2lDyBNzV9pL-XnWhG6MyctcwgplU5Dgh5yJayO8At-teOZjopDROAqO4vj0x8HvhVsIxjrfMRrK6aHav1UblGxyJZtrRCERL0Cf3Fv3RWuLqPVBxArr3dS_xIAmnSDMbMkQGWClRpYpIwlJv3cR8SZOsF6HU-xkepqFgyObA4_7D9G_DOghvRk99Avk-IRjsphwJ84vhnzkxR3N1d0thtCtUluRtif2H7j0PPzDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Coming soon inshalah</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90412" target="_blank">📅 23:08 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90411">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇶
السفارة العراقية بدمشق:
أعدنا ممتلكات في سوريا إلى أصحابها العراقيين.
😆
شارع بهمن حاليا</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90411" target="_blank">📅 22:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90410">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3bb77f66d.mp4?token=J0Svpa91h-axXiDYOS47cguXYwbe9yVXTZlG7A0kZ4NkuR4z94zSHQP8LsFMm9cgOWG03Yn-AVVLxtLzeXcC8ct2da-ntlMVeu7_Bjd9k62U62ldRvQCLAyL_POaWOojl9IO4qOj1wz-Z3pFnRC7eUAgM2csW_vtTiL44xM4jIGE_mGmYaBUKtIxAF4qPpN9sxK0WkqMafGNz8twbRbdL8rq4bckf3MUTk-DPv6DkpfAN_EKuw7__pziaFWZmPEjebEa0UFC4wLFFnAk675IgGH9xQxvYLgHtA1ho8DKYVxzLVVS7d_bYD9G4JinUAvqPdT-yLJ_QtVKhjFT3kJvpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3bb77f66d.mp4?token=J0Svpa91h-axXiDYOS47cguXYwbe9yVXTZlG7A0kZ4NkuR4z94zSHQP8LsFMm9cgOWG03Yn-AVVLxtLzeXcC8ct2da-ntlMVeu7_Bjd9k62U62ldRvQCLAyL_POaWOojl9IO4qOj1wz-Z3pFnRC7eUAgM2csW_vtTiL44xM4jIGE_mGmYaBUKtIxAF4qPpN9sxK0WkqMafGNz8twbRbdL8rq4bckf3MUTk-DPv6DkpfAN_EKuw7__pziaFWZmPEjebEa0UFC4wLFFnAk675IgGH9xQxvYLgHtA1ho8DKYVxzLVVS7d_bYD9G4JinUAvqPdT-yLJ_QtVKhjFT3kJvpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الصحفي: تقول إيران إن إحدى سفنها تعرضت للهجوم الليلة الماضية. هل كانت الولايات المتحدة هي التي قامت بذلك؟
ترامب: لا أريد أن أقول.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90410" target="_blank">📅 22:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90409">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387e122db7.mp4?token=eSBo1tu4iJ0lI5TFmmocwHDMODcVk1XOjJ1VmP2fcY826jzvszNC3V7drvTK-hn6lKI9vIp9FXU9Rtu9-4PGi83OvYIhqzsEqYxW1kNN_vEkEN8dDr_txbRdW9j-dSyUNnfHTqDrYD1Tq71g2nVUzF75WGnBhdduHehnh4No6G4J2UyWf2YxmbNpNOBWndmDNe1Ac_FMKsbhFtL3X97IEPnVzozynZiOmyAKC7921YztMZiS4Wtan_YLIC9MBuABjyKezwe0xawZTqeb0YJoWVYJWHCFopvqf5C63ju-gfeTMUWdcqUuPbZztbs3H9KaWCX5d3r57bHQVrwJdI6JWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387e122db7.mp4?token=eSBo1tu4iJ0lI5TFmmocwHDMODcVk1XOjJ1VmP2fcY826jzvszNC3V7drvTK-hn6lKI9vIp9FXU9Rtu9-4PGi83OvYIhqzsEqYxW1kNN_vEkEN8dDr_txbRdW9j-dSyUNnfHTqDrYD1Tq71g2nVUzF75WGnBhdduHehnh4No6G4J2UyWf2YxmbNpNOBWndmDNe1Ac_FMKsbhFtL3X97IEPnVzozynZiOmyAKC7921YztMZiS4Wtan_YLIC9MBuABjyKezwe0xawZTqeb0YJoWVYJWHCFopvqf5C63ju-gfeTMUWdcqUuPbZztbs3H9KaWCX5d3r57bHQVrwJdI6JWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
اعمال عنف وتخريب للممتلكات العامة في عدة محافظات السورية بعد قرار رفع سعر المحروقات رغم شحتها.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90409" target="_blank">📅 22:27 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90407">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99dac0b3e1.mp4?token=kutY2iFp8pVbN3hqJFWGeyxGgb3FKIUhG22Dega0MUxwefbF5uQtRsXAVREhPD_Jkq5xx9PMS6c1VTsdETUIOLIJjNb6fejvMm752-p9C-MGOTo10W3dBlgJAg1u2A4yoOpZH1t7r1qkQ1nw9KbWl02QENSBxMlo7-SrrkYJHvr7OGi5Wk2rzpV9ZoCPj1tpkjHv7OuvDMXVvy0QmnW2eBBkIw0VwfSRZawaCCblyPCMnt8XfdVM8mk5KvaNECsawKFsvap3dpDd_2ehF0_hUetTtM_cJGe836uvpWV5NQEHDw68sH8rpy3OPR9OORxgSYg7fsJ1lIVqXlHQgyguZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99dac0b3e1.mp4?token=kutY2iFp8pVbN3hqJFWGeyxGgb3FKIUhG22Dega0MUxwefbF5uQtRsXAVREhPD_Jkq5xx9PMS6c1VTsdETUIOLIJjNb6fejvMm752-p9C-MGOTo10W3dBlgJAg1u2A4yoOpZH1t7r1qkQ1nw9KbWl02QENSBxMlo7-SrrkYJHvr7OGi5Wk2rzpV9ZoCPj1tpkjHv7OuvDMXVvy0QmnW2eBBkIw0VwfSRZawaCCblyPCMnt8XfdVM8mk5KvaNECsawKFsvap3dpDd_2ehF0_hUetTtM_cJGe836uvpWV5NQEHDw68sH8rpy3OPR9OORxgSYg7fsJ1lIVqXlHQgyguZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
احتجاجات عارمة في محافظة إدلب السورية، على خلفية الانقطاع التام للمنتجات النفطية.
بدنا حرية
...</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90407" target="_blank">📅 22:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90406">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6901b9a141.mp4?token=FAH3eK0Jyu21NSQz-SJ2lP7keZmLDf-KtT2LzHjIRc_w4fvlTskXbydvoKCjZ3QoCW5KOBcOk72k5TDPLuSMaYFI-CjlPs109BlNEeNF4KOC5b5xJX90jsFt31xhnnH1DEMiuSutuDv9KHHVYrDBGBul052i22LVfyRbZrIoiFK9FaV-rAGE1Fkrebo30x4Ji69hcyH10xsfEp1uB4jCIv3NffK8tB53421K53Uryel62CwxcXrzc7qkn4uJwQGPHWicmnVVN5uCT4ZXzKOID6AE-oxTfbScYC1Zp7b5n4C4QIKBFDQrXocq1TSx06NOVdpMuD_zFTHCQSjTMWQmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6901b9a141.mp4?token=FAH3eK0Jyu21NSQz-SJ2lP7keZmLDf-KtT2LzHjIRc_w4fvlTskXbydvoKCjZ3QoCW5KOBcOk72k5TDPLuSMaYFI-CjlPs109BlNEeNF4KOC5b5xJX90jsFt31xhnnH1DEMiuSutuDv9KHHVYrDBGBul052i22LVfyRbZrIoiFK9FaV-rAGE1Fkrebo30x4Ji69hcyH10xsfEp1uB4jCIv3NffK8tB53421K53Uryel62CwxcXrzc7qkn4uJwQGPHWicmnVVN5uCT4ZXzKOID6AE-oxTfbScYC1Zp7b5n4C4QIKBFDQrXocq1TSx06NOVdpMuD_zFTHCQSjTMWQmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
رئيس مجلس النواب الأمريكي: الإيرانيون ليسوا شركاء موثوقين في المفاوضات. بالطبع، إنهم يكذبون كل يوم. يجلسون على المائدة، ويخبرونكم شيئًا، ثم يفعلون عكسه. بالنسبة لبعضهم، هذا جزء من دينهم.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90406" target="_blank">📅 22:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90405">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59a73e5d62.mp4?token=RCFEqnfLXxdGcf_r5XWPigvk-PC4IUHh7z94ORrvEx1jrXhsEvX2Ubv-i6MkKYNUx2Rpr4TsVsFOnbrVvg1caAWIGGybuBBAK_D-jrlBnV3eZBiCdm-AqYs39G5sdHcN9hg57NQgXzhmZdvKHsNFmwEWjyH3D2KOPNXXQA8UR6j04Enjeha_Hg9BPoArdeuO7KhODFmkzcu6YLhVnlX5d7OoFlYOMZtCzyQvH33i8l3Fdk5LdXAvPSxjIicvUDbeqVRk48OY1_BKCj1O0Te3YDyvMscjYup6FDp1JMY2Wr_0Gw1dVDShOxpbxIxkwUZgUV5qX47ilVcg3IYcj8aDkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59a73e5d62.mp4?token=RCFEqnfLXxdGcf_r5XWPigvk-PC4IUHh7z94ORrvEx1jrXhsEvX2Ubv-i6MkKYNUx2Rpr4TsVsFOnbrVvg1caAWIGGybuBBAK_D-jrlBnV3eZBiCdm-AqYs39G5sdHcN9hg57NQgXzhmZdvKHsNFmwEWjyH3D2KOPNXXQA8UR6j04Enjeha_Hg9BPoArdeuO7KhODFmkzcu6YLhVnlX5d7OoFlYOMZtCzyQvH33i8l3Fdk5LdXAvPSxjIicvUDbeqVRk48OY1_BKCj1O0Te3YDyvMscjYup6FDp1JMY2Wr_0Gw1dVDShOxpbxIxkwUZgUV5qX47ilVcg3IYcj8aDkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
رئيس مجلس النواب الأمريكي
: الإيرانيون ليسوا شركاء موثوقين في المفاوضات. بالطبع، إنهم يكذبون كل يوم. يجلسون على المائدة، ويخبرونكم شيئًا، ثم يفعلون عكسه.
بالنسبة لبعضهم، هذا جزء من دينهم.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90405" target="_blank">📅 22:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90404">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇶
حرب خفية امام أبواب مصطفى سند   الشركات الأمريكية والصينية والبريطانية تتصارع فيما بينها امام بوابة وزارة الاتصالات العراقية للحصول على فرص عمل..</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90404" target="_blank">📅 22:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90403">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a124353a22.mp4?token=fqv4eJvimqBmK68NH62LBJ3cvbRmQdNB2k2ygM1gxLTyiSL3jdyx4TIWNasVt_qEyD3tkoIzeXjMotat1lpALMyr0U-OlIUIK3zTSuSuYGnTNXx4EOJE9LS4Pz57w2xqhPC3GPzLccApuZp4w4GOGPzY1HtzwzHprvllpfmX_AVo1loIAqzTr-RW_zGI6tFA6ca2E46ETO85CrfC61HldSeRdOz5j345i_t8tYFxnGWitu7GyIzCTaCmGMlHpMweR9m0rpxxacax_RBMe_XB4wNNlfVh5AXMTUYmRwjANAlI3W-fUYavQmiqkpk4IZ5u55XoZli8Nxzc2xwt8E2ToQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a124353a22.mp4?token=fqv4eJvimqBmK68NH62LBJ3cvbRmQdNB2k2ygM1gxLTyiSL3jdyx4TIWNasVt_qEyD3tkoIzeXjMotat1lpALMyr0U-OlIUIK3zTSuSuYGnTNXx4EOJE9LS4Pz57w2xqhPC3GPzLccApuZp4w4GOGPzY1HtzwzHprvllpfmX_AVo1loIAqzTr-RW_zGI6tFA6ca2E46ETO85CrfC61HldSeRdOz5j345i_t8tYFxnGWitu7GyIzCTaCmGMlHpMweR9m0rpxxacax_RBMe_XB4wNNlfVh5AXMTUYmRwjANAlI3W-fUYavQmiqkpk4IZ5u55XoZli8Nxzc2xwt8E2ToQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
احتجاجات في البحرين مطالبين بالافراج عن معتقلين الشيعة الذي تم اخفائهم قسرا من قبل النظام البحريني.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90403" target="_blank">📅 22:00 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90402">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تستهدف تجمعات المليشيات الموالية للسعودية بالصواريخ الباليستية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90402" target="_blank">📅 21:46 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90401">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأميركية:
مجهزون جيدا ومستعدون لأي طارئ.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90401" target="_blank">📅 21:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90399">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgcZOFTPLoXseCrsMcM2c9atp1whVmJH4-b9lpyUmxZ1BE5ksavYKmDSS2hjGgE9q2IbfttCZ8K4ffRtiaK-y3uO5_q_2A1ZQpbptwufddXfhfttMNFYb71r4FAvOm5cxEd8GOcoguLc5t4TSwLJ5YGbjTyGrHXYqmOzeeI2aTh5XJSAx4-MuWFvO90b-MBzKYXpi1GmjnKFRPn6PSyu6qz513qwehPJ8WbbKT3hDGodD_KA4BfakHyB52Fjn71IXIHPNTeYhmiyVgiVaNDj33TComcY2GQeFgrYDX9tupl4IWCOrebK_FoBsFiTDK6rMxDMQK1X9N7QxQD2MdtrGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار عنيف في محافظة حماة السورية</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90399" target="_blank">📅 21:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90398">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HfurztzzeaZR-2GSDcNTRHRYgk6mRsY7rO74fciJ6m2qGee-AqaA0yfdP_7_xY9VK1uAmA1owgof93lxYJXmxVGW4-SJN5ddqOcDDy9-_hbjXaJ_bUk1ygnmp78SGX4pvJKZUcyG_oe-RQufyh9gSvzUYRdvWTxLLu0Cvq_l7svZ327GkJQ3OS0ZN4pRTv89Nqq-oorl99DVZe7JolWMZ84GgMslFw82S3_AMHBRCCCpcz1i4dTyvMOxdxMXtG-RdEMslcYk65KNlyhi3OlguEXyWdDnJ0XwnMS14ddb8mpLjDjXbejee9z9cN9AoEwmOpLQjMbPNECKr4Ju9uB7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
حرب خفية امام أبواب مصطفى سند
الشركات الأمريكية والصينية والبريطانية تتصارع فيما بينها امام بوابة وزارة الاتصالات العراقية للحصول على فرص عمل..</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90398" target="_blank">📅 21:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90397">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇺🇸
أفادت هيئة الإذاعة البريطانية (بي بي سي) يوم الأحد أنه تم تهريب أحد موظفي السفارة الأمريكية من المملكة المتحدة في أغسطس/آب الماضي بعد مزاعم بحيازته صوراً غير لائقة لأطفال .</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90397" target="_blank">📅 20:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90396">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">طيران العدو السعودي يستهدف سوق الخميس بمديرية خب الشعف بغارتين</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90396" target="_blank">📅 20:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90394">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzF1ft7EO_6a_Rfqm6_1aiWezPopdWTbIWp5NIwuRU7mcAjScYYAZv-LSLxF7LKcIbmbXDSjwMFIXpuuaps_XJo_YVSnRNfZVLxQbs5bw1U4UJ6zP0JOPh02XLFmQwZ-zw8TxPekCpMuj2WZr0EbQDJYnfkvdJ6SmLu2J3bec-U-CbJaMtE18jztKOiGxQlEOgpRmHGJAuYu4ytKvZQg0-eKf1ACLBNhsKIGTr-rTqSD7tXJWmwjFJRPCWyCdV9fpPND9O-kQcDSLXcnioJpiur5C9Cs1bT4kPTn72FbsUtqIaIfbw9K5yNNgMKXoaZX8t-IsU9Jnf-YyhU6L9N0yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MBkOre9xICeaBAw741D5PNkLiqGwZQ8uINvTSg8MtER-jz1KRf4cF5SaZGmrAZe18svBDhatC26e86T2DXUqVdXlNXDpAzemRcZRt5rEBTU2ha4Luzu45Rqqe2__w_FcxqfmQ_5XEsGWvcWj8z3PhfPmq0U2rhklBxI5URSSTSH73L1FBAjhVAkJBIdQK9SL0MuuEOSpuZLZbRanzfsSigC1erRYwHxg7Shn1CC4pX1csrUIxM9Bb7TJgv9uTFxQeHpVJoHad9A9t4AvgffpODtTpjLjoFlsOTiixEOYfe0UPc2B9_EzUYb8PfEf5UiEj-MUhw5t2GQRxQa740OV8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسالة أهل الثبات لقائد كتائب حزب الله، الحاج أبو حسين الحميداوي "ايده الله ونصره"</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90394" target="_blank">📅 20:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90393">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0be8bb0a.mp4?token=CJ1KrgM4BjLWh6cBfFs_I1lZELmpmz7obEWFKFa0ZVyIUNhXslkuBLLLGnKstEm3bvFzfT4oSoniwivZHOODjRWr80cqIFeOqTkB6DULLthQL7oHaAofYtfrCC7prc2FVg_yjYIYPosJ-RM5wMjnRQ5xgXqw1-o16Xabg1ARvcy2wwstbyCVKy4u8S6vMMrxewOLPbwdlxVfFxxv63f6qI5KxBVpiO0I_-Bm_tzPfruNl4DLhvj7HjNdPWkkIhAiDhtQ2_7hCYsetsPgXAIybtUGu9d5_xlqBD4ZuBZz1ldk87oeghTLhL4gwg0cxwsOw17HIGibNgoh_J-l3z4drA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0be8bb0a.mp4?token=CJ1KrgM4BjLWh6cBfFs_I1lZELmpmz7obEWFKFa0ZVyIUNhXslkuBLLLGnKstEm3bvFzfT4oSoniwivZHOODjRWr80cqIFeOqTkB6DULLthQL7oHaAofYtfrCC7prc2FVg_yjYIYPosJ-RM5wMjnRQ5xgXqw1-o16Xabg1ARvcy2wwstbyCVKy4u8S6vMMrxewOLPbwdlxVfFxxv63f6qI5KxBVpiO0I_-Bm_tzPfruNl4DLhvj7HjNdPWkkIhAiDhtQ2_7hCYsetsPgXAIybtUGu9d5_xlqBD4ZuBZz1ldk87oeghTLhL4gwg0cxwsOw17HIGibNgoh_J-l3z4drA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسجيل حالات اختناق بين عدد من موظفي معمل الأسمدة الجنوبية في خور الزبير جنوب البصرة نتيجة تسرب غاز الأمونيا داخل مصنع الشركة ونقل المصابين الى المستشفى لتلقي العلاج مع اخلاء الموظفين من موقع العمل.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90393" target="_blank">📅 20:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90392">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818a015df3.mp4?token=vK_IvgWPv09o0ltREfZZMtayAVc78xMu1gjhUIbuCU6TDMF1nBdrPRuVFljmleGybG0mFSn7zuSdKAgOsMkSXfD_Pq6y7bRhvlmtHhy-hNf3nQLqQX7-GAzOT2ObDysOHO3bL3g9H3Mqtb4KWFXNyGM7YE797SEI1bAYCeOti-x4eeDzvcHUd3JCreyTEfgzZbSZiLEuE11r1xmS0Xob2h-GyuzGMYZTHN88G4Ge8oS3sC1fpccfxt1bKKx_Ejqih0RtaRn7UxjWH68T8wKn0s6-Wjye0ihzXBYJyL4O2bYhHX5hxjjTu0ZvRRIEOTpCtJSGpKXgkJN9gt7y7lU7zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818a015df3.mp4?token=vK_IvgWPv09o0ltREfZZMtayAVc78xMu1gjhUIbuCU6TDMF1nBdrPRuVFljmleGybG0mFSn7zuSdKAgOsMkSXfD_Pq6y7bRhvlmtHhy-hNf3nQLqQX7-GAzOT2ObDysOHO3bL3g9H3Mqtb4KWFXNyGM7YE797SEI1bAYCeOti-x4eeDzvcHUd3JCreyTEfgzZbSZiLEuE11r1xmS0Xob2h-GyuzGMYZTHN88G4Ge8oS3sC1fpccfxt1bKKx_Ejqih0RtaRn7UxjWH68T8wKn0s6-Wjye0ihzXBYJyL4O2bYhHX5hxjjTu0ZvRRIEOTpCtJSGpKXgkJN9gt7y7lU7zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اخلاء معمل الأسمدة في محافظة البصرة جنوبي العراق بعد تسرب غاز الأمونيا.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90392" target="_blank">📅 19:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90390">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9UcIPMxNcxLj4TNETOk1B5Bkvqe7KdOyLcI3g8zayaMApmA_6U-5_fzLeo1w4UXwed2Krfl9RsJC7CjG6SzVVPcCjebmdf9pEA5m7k8_Dd4jtzjcXGCcastoSXuJHap5OkjUOc2UreINeoirh8uC9CkTkcCtTed-LF2uIbVY62k6zPE0pG5Ry4mJAMnQrBaKnlO_Y11Ab-qFAShZB-6Yu3HuCvsRgPimBNe5hIRO-iv7IncmFiQDoFPrBPN3oopAYS-0fUuAiFRN0bJ--A4mPrge8ZlDTrh6cIMsU1CHCP0QI9KtC89W7VuHFCNDN4zIuxglKkaQnaa8em-n4NxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZrPooIIin0Y9yyE94-X-oDf8W7EulecljVEYdCgNF8DQQdBFUPD7rCSCpuMDLoorLU59LIKdODcWc1ltl7JI0RJh_oi-7QoZ0R0yW_G1SjM6BeeFPT9ifN5Jtz9Feek1fhK_nq07sVu808U1x_vC5c5C1ozAyoHudzHkQBU8BFaB8PyHKO0Kmnq3Z3TD_V1JkL1ez_-nfwsO9wn-zGKrK0RUzE-_c6i_T0ScKw1S14gUvtIxDPPqojL2SMQc6us3P8qUQTREU5CMPVEQdRXHsjkfvcvU0l73wHbKVPNYCglSNVqhmA9u9Nh3FJj25E3cP-PojJoyF0EzfZXViL04Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارات تهز ينبع السعودية واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/90390" target="_blank">📅 19:18 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90389">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
اخلاء معمل الأسمدة في محافظة البصرة جنوبي العراق بعد تسرب غاز الأمونيا.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90389" target="_blank">📅 19:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90388">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">صواريخ باتجاه خميس مشيط وابها</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90388" target="_blank">📅 18:49 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90387">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90387" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/90387" target="_blank">📅 18:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90386">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90386" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90385">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رشقة يمنية زيدية نحو خميس مشيط</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90385" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90384">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90384" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90383">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90383" target="_blank">📅 18:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90382">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
🇺🇸
هل ادخلت ايران أسلحة بحرية جديدة ؟</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90382" target="_blank">📅 18:37 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90380">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نظام ال سعود يهرب من اليمن ويسحب معداته من مدينة حريب وبيحان باتجاه منفذ الوديعة السعودي</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90380" target="_blank">📅 17:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90379">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇸🇦
إندلاع حرائق هائلة ومجهولة في العمق السعودي بالمدينة المنورة</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90379" target="_blank">📅 17:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90378">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏ترامب في تصريح جديد: زيلينسكي يجب أن يفعل شيئًا واحدًا. يجب أن يوقف تعطيل إمدادات وقود الديزل في روسيا. إنه يتسبب في نقص في وقود الديزل.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/90378" target="_blank">📅 16:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90377">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a416e2d458.mp4?token=KYms1D1bhbnK0p5qprMaY9hrzHbOYNXT5l6W7gEpgL2sPoswVwxrrMISEtZ3kKt73sheFQUWD_xX_K6ODTGYZOtavbMKLt1c6afU9cC6R2yZwW3zXndPplBGtfy3sFzmQLBapG2AKAPBtXCTrTVy2wvag8wBH_q1NoeXISrMmlAZCWD-YQFpSbvCaFAzcYPrTUPPowJgWEWLUObC4FtBjOCmMIj3RFb3Pnd-YE9wKfUU2PGajMRxEdWHees5UjxNNk5yeB-PEJdcB3J-BzneDnaVzkSlw4DJ99ReT5JQoVrekTakkr-WzfMOTjSDQ_3H75EPn9r6FFA_m4vGOfAqU4IBFpLDJtlaH_RvVxdT-lgRtzDLnkPgdCHliVJDs0md0CU33DlYP5kZMoW9jl1utOMZqbRUT4fx9Fk6gQTjkE8BiZdNmKl7SRqHBDnc9mgbUg2oE5yOQpkPWuivKYuAypCxEDGjTG2rz03AQhYT0mGWPcxNdFJ3FULpqqaPPouMTGEkkt-CgMuxaO2-jihEPchkz1RiCdiYbBpZdQhtan-TP_4vA2IlkVF0OyOR5-n1oHarVAvHwGBj0Bvt_k97p1MlgftcN4yXR9MUguuQ44HwqlEPv0DEpieM0LqJHwUyw4UCcs7zWf_ClW1PJfE0gEnAWI_W2ZbRaVjJBGaOmvE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a416e2d458.mp4?token=KYms1D1bhbnK0p5qprMaY9hrzHbOYNXT5l6W7gEpgL2sPoswVwxrrMISEtZ3kKt73sheFQUWD_xX_K6ODTGYZOtavbMKLt1c6afU9cC6R2yZwW3zXndPplBGtfy3sFzmQLBapG2AKAPBtXCTrTVy2wvag8wBH_q1NoeXISrMmlAZCWD-YQFpSbvCaFAzcYPrTUPPowJgWEWLUObC4FtBjOCmMIj3RFb3Pnd-YE9wKfUU2PGajMRxEdWHees5UjxNNk5yeB-PEJdcB3J-BzneDnaVzkSlw4DJ99ReT5JQoVrekTakkr-WzfMOTjSDQ_3H75EPn9r6FFA_m4vGOfAqU4IBFpLDJtlaH_RvVxdT-lgRtzDLnkPgdCHliVJDs0md0CU33DlYP5kZMoW9jl1utOMZqbRUT4fx9Fk6gQTjkE8BiZdNmKl7SRqHBDnc9mgbUg2oE5yOQpkPWuivKYuAypCxEDGjTG2rz03AQhYT0mGWPcxNdFJ3FULpqqaPPouMTGEkkt-CgMuxaO2-jihEPchkz1RiCdiYbBpZdQhtan-TP_4vA2IlkVF0OyOR5-n1oHarVAvHwGBj0Bvt_k97p1MlgftcN4yXR9MUguuQ44HwqlEPv0DEpieM0LqJHwUyw4UCcs7zWf_ClW1PJfE0gEnAWI_W2ZbRaVjJBGaOmvE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بدأ كلمة جديدة لترامب وتسريبات من البيت الابيض لنايا:  - اغرقنا القوات البحرية الايرانية - دمرنا القوات الجوية الايرانية - ايران لن تحصل على نووي - ايران ترغب بشدة بالاتفاق</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90377" target="_blank">📅 16:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90376">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
بدأ كلمة جديدة لترامب وتسريبات من البيت الابيض لنايا:
- اغرقنا القوات البحرية الايرانية
- دمرنا القوات الجوية الايرانية
- ايران لن تحصل على نووي
- ايران ترغب بشدة بالاتفاق</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90376" target="_blank">📅 16:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90375">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e66be65.mp4?token=Gl6h3lTorvHzthZkLmCKE5-d06WSwj1n8kwS-vXQo6wW-F0bGwMEKDIGT5zrvk5PGEzp8pBht8Mr7zoqWdFjObgnBMx0t1hXRJQsKDImjKdM2KrtWV_Fg6WjGTKX6PAA_wMAYb7nZUhwdr9rz92lOlm8UQzEN11VvzIzv6nP7E5eCgF6SS893GToBq0YAd11uUO43QKa-Nk37497E2vcWfliiQsBXsNuaMX2blqC8Ce8QFU20ATnzWa0OfhSaWLTzc-1HrAhMnFUx0xgm7LvIjUf65bHACQu6t-50rUI8yGmi3YMaZR6Us1xvSD1MDO5kFQFcyHh9AB_6mccVIG5sVS8wCHwyDSz5WO29A2L4mAh6w-VjaQxsQCFjexXzdWsGRyb9Dr3_dAYxRF2F_vMElxPZGZ5pclJtrfZjstlSPiivdPwbAcyYD0rfs-ufkkpS804qTo8T8-WOrRO3yP8Xf5rYxsROO7ALbiUv9PD98U0XoLrRbarT0bzf-MJvebx514clV9Ja6odOYbHhwCrqcHoVbsxus3b2b6C_jGcJd05nr3D9vifUkp9MtCul-LI7Q2kthLFbxRLJ48GJjBAv_KlVrRvun7-s_VTk7Ber7D2s1pkTCmw54n6oH1dd3ExM1VSt5tsmzP9YSsTVg8AvfEYkKFeHcNdkaOCYOtFJ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e66be65.mp4?token=Gl6h3lTorvHzthZkLmCKE5-d06WSwj1n8kwS-vXQo6wW-F0bGwMEKDIGT5zrvk5PGEzp8pBht8Mr7zoqWdFjObgnBMx0t1hXRJQsKDImjKdM2KrtWV_Fg6WjGTKX6PAA_wMAYb7nZUhwdr9rz92lOlm8UQzEN11VvzIzv6nP7E5eCgF6SS893GToBq0YAd11uUO43QKa-Nk37497E2vcWfliiQsBXsNuaMX2blqC8Ce8QFU20ATnzWa0OfhSaWLTzc-1HrAhMnFUx0xgm7LvIjUf65bHACQu6t-50rUI8yGmi3YMaZR6Us1xvSD1MDO5kFQFcyHh9AB_6mccVIG5sVS8wCHwyDSz5WO29A2L4mAh6w-VjaQxsQCFjexXzdWsGRyb9Dr3_dAYxRF2F_vMElxPZGZ5pclJtrfZjstlSPiivdPwbAcyYD0rfs-ufkkpS804qTo8T8-WOrRO3yP8Xf5rYxsROO7ALbiUv9PD98U0XoLrRbarT0bzf-MJvebx514clV9Ja6odOYbHhwCrqcHoVbsxus3b2b6C_jGcJd05nr3D9vifUkp9MtCul-LI7Q2kthLFbxRLJ48GJjBAv_KlVrRvun7-s_VTk7Ber7D2s1pkTCmw54n6oH1dd3ExM1VSt5tsmzP9YSsTVg8AvfEYkKFeHcNdkaOCYOtFJ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احتجاجات وقطع للطرق في سوريا بسبب ارتفاع اسعار المحروقات على المواطنين</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/90375" target="_blank">📅 16:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90374">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">احتجاجات وقطع للطرق في سوريا بسبب ارتفاع اسعار المحروقات على المواطنين</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90374" target="_blank">📅 16:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90373">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UjIxnL0IUHgUWp7k8-bGeqS9IJhVvKRFIEhMkRuEXiqKQhj_CjYhNmi3eH-yiDuuW--W2gm3NiJ72dCzOVHY4F_N0e4QjlVUINuDSyBmGfwOaDxkwiqD7tIBlpjMFNTdHojr6px169bUoNLenBGZxiC85_CQZ42kZzkNnaUHZoqR-BVUzoTu4z_WQqtJ2PAEB7o-wB7TEjNciXWG9Fp6EY3b2cap-yhQhj4Vz6F9Sdsg2wVA0ei-Rz9wb0fsLPd5yImvKkzu69rwaRT9CJkkfZH3hXpvx6ireqHjWb5qxF-BAAIa6aMRrwdgEmmwYKNeWKnC8SYRZTVc3UG9LzGpTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🇮🇶
مديرية تربية محافظة واسط العراقية تصرف مبالغ عن طريق الخطأ وتطالب باعادة المبالغ.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90373" target="_blank">📅 16:28 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90372">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDhmGVievPHYX-40iUMsGCk4vj7_cthgFA17A-aAc5-0ELUJimfogOCYlPXQLeNf_YdL-e2GdazcECzB8eBXBxDgoIX_cwlpPdP8jKGandjNakkyYlc6mW2pwQDN8E1h_DsJYJ3CZrVjGUx09gF-EyZP73xujfn85LlflhByqbzE1eRAzmynC3DgWW1fjS7z9g898-nW2vT97fO5JI88qZaUw-_gE-9vpCD3ZYbvGPnGvJvyMzSvJ05SIh5fOGQNuiTrX5DAeVL8ajGGDC1o3CDXxzZnwD-UbALI5CjYCMz0pNH3WUchtp2uhTAB6QJHFONXzPaelAbn4z3Z3G8oSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكبسة ويانه غير
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90372" target="_blank">📅 16:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90371">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇷
الرئيس الايراني مسعود بزشكيان:
أجرينا حوارًا جيدًا مع ولي عهد أبوظبي، واتفقنا على تجاوز الماضي وبناء مستقبل أفضل.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90371" target="_blank">📅 16:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90370">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الاعلام الامريكي:
وقف خط أنابيب في المملكة العربية السعودية يهدد خسارة بنسبة 4% من توريدات النفط العالمية ما لم تبدأ الاستخراج مرة أخرى في الأيام القادمة</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90370" target="_blank">📅 15:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90369">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a08f0e1a58.mp4?token=qwN56tNdT3jFqLSNLycj0q5U-TBHMfzWRfErkAN1k7WAIRIPlsYIRsPdpZMI8PcgAWoVFEoZiq7gJ4Adg5eUdsRP22K_dYjo-w8ICmxOKO-tJeEY2VdZzUshEOUyq_4vzq44d51euQjlC56Q9IJ9bMWz-HmxZFKoWbtIzi97AE1zcLr3ZdMTOy46vrF_t9-NR8DaAddcIcF4kT_xztiM55ZoC6dtdbGBxyLzvAYyLGZwRodl5OJXv9XFwSHHZR9ptskzPWseM3TecOm9J9Og2h8gSWa3MWqH3jeB6_BwYlIMSkRISIDF3ZT7CQZw1061C9Dp-AvLMD9N6HGevBZl7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a08f0e1a58.mp4?token=qwN56tNdT3jFqLSNLycj0q5U-TBHMfzWRfErkAN1k7WAIRIPlsYIRsPdpZMI8PcgAWoVFEoZiq7gJ4Adg5eUdsRP22K_dYjo-w8ICmxOKO-tJeEY2VdZzUshEOUyq_4vzq44d51euQjlC56Q9IJ9bMWz-HmxZFKoWbtIzi97AE1zcLr3ZdMTOy46vrF_t9-NR8DaAddcIcF4kT_xztiM55ZoC6dtdbGBxyLzvAYyLGZwRodl5OJXv9XFwSHHZR9ptskzPWseM3TecOm9J9Og2h8gSWa3MWqH3jeB6_BwYlIMSkRISIDF3ZT7CQZw1061C9Dp-AvLMD9N6HGevBZl7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس الوزراء الباكستاني لمحمد بن سلمان: نؤكد دعم باكستان الكامل لأمن السعودية.
باكستان وتركيا:</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90369" target="_blank">📅 15:47 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90368">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27850023e2.mp4?token=rOyc1vOjLv47gaPJ9KOen3q2pKe5qyPcFd9thK81rKeY-fFAQnLDyHWNEOjQB3Dm6UK9iLBc6X6MDr0hRZUcM9U7Z05p2LPu4fbBjAfeEIReMLk5zxt8GOJ5ntrxZAyOYwXCkbS6qMVNLpbaczvsbUVjjbaIdu5MEgvc7X5_6bSb9-W0uMWbytQSui36dVZo7NsHHqtn2_pBEVQT0Dq98mBFJF8FQ7bRmIRZXvTvHsG0LGDlR5N-sRwNua0W30HGl4nu1Dawg8m6OfmL1w-CbfdVUP7IrdATLOTj9t1JY9HYw0MfiWZXdj8T4-rkpcAVOOQ4THG95AW2XPGCdprK9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27850023e2.mp4?token=rOyc1vOjLv47gaPJ9KOen3q2pKe5qyPcFd9thK81rKeY-fFAQnLDyHWNEOjQB3Dm6UK9iLBc6X6MDr0hRZUcM9U7Z05p2LPu4fbBjAfeEIReMLk5zxt8GOJ5ntrxZAyOYwXCkbS6qMVNLpbaczvsbUVjjbaIdu5MEgvc7X5_6bSb9-W0uMWbytQSui36dVZo7NsHHqtn2_pBEVQT0Dq98mBFJF8FQ7bRmIRZXvTvHsG0LGDlR5N-sRwNua0W30HGl4nu1Dawg8m6OfmL1w-CbfdVUP7IrdATLOTj9t1JY9HYw0MfiWZXdj8T4-rkpcAVOOQ4THG95AW2XPGCdprK9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇷
عدوان أمريكي يطال سفينة تجارية إيرانية بالقرب من جزيرة  قشم جنوبي إيران؛ إستشهاد مواطن وإصابة 3 أخرين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/90368" target="_blank">📅 15:40 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90367">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIwtuaLnh4lZPDlF5QyhqcfHWhQvL7TVhH0Yyx7eo6iVAKES-_KveUhAGvx7sU0Ntjj1C4ujLrDSnN1szqBl4sKEOwVWH7TCVM3vwiO0Ifm4Q5Zzh3lm_WswXsmqdtQIQUmuSs7pEUu9FbbU81SJo5qglo7-dcmjecouzRhxR4qfb2RE3Ts0x0MHBdF6XjvFPNaQfHfijviHDKPDQCIAoSAB467oXWroW0xYkE16CKfpjpeckTm02p25XpJMQkMco5zDoSDo--I-UFUpHi1K6sry7GalKv7SrjHoP9659bN42Wq2KcCT4DX8byADic-E19XRH380ujASHfDDhEyrPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
قصف إسرائيلي يستهدف محيط بلدة بيت جن جنوب غربي ريف دمشق.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90367" target="_blank">📅 14:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90366">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me4mVI-dLNCcbR9rfkxV6PYSk1rBmbCh32857g2rnbKWc7gwY3lZgF87_6aoGCY6d7jm0W8OLI4_KNOobvE4IHLyIr7oM2puN7Iin6evUSPNNu8HX2jvS17z6M7l8jY-z2Gv_3Uz9_ojfkpql-Hbv29CdG0OIC08vhK4IKKKLM3BCqhzdaCptIcT-wEYB6p_Ke0GRHXuVOWgwVt_X17boTgcgIeYJmIngOJBV3UyVGjNm6xFs-gb9Y-A80s_uhwmfgcfpTEL65WbRS3sj8Wmvunbfbh6npTLw5kcebDd1ITeQZsEMwRlytsGcyhrh0xDnAWY7E7mGH2n9Ye2VLRK0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز ينبع السعودية واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90366" target="_blank">📅 13:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90365">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇹🇷
🇮🇶
عدوان تركي يطال مقتربات قرية گلاله في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/90365" target="_blank">📅 12:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90363">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aH1RiuCy_cOFZOkATaufHhdidQcYP3_nqa5A8jUvf22-oWaYHQf_4VM9qnx1ssXEF14tXS3r9-0gthHGO2g-kJQ9t1JNs35GGY3-FTJrFGzJqMpqe27MSQhsX-eDEyJcM5oUnt_MVH0F-thq-Qce9jL8QmVVqTxabNUjQGLIfX4IXlUo_7zqSZty2y6fMdjAFoOnTycnL7jl5jMFz02ro3XLZk4TWtLSBjOKHNbA2b1T79pLO0CAZ1oBbvqMdTmFiwLeKbO-7UCGCG4RHpJ4A2SUxBnlmLaHRxrgoTrjQempU1wfgWMcOFEIooJSdXzCYUWss0ykMUnNwpdKUtqt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكبسة معنا غير
😆
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/90363" target="_blank">📅 09:35 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90362">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8041f170b.mp4?token=gHw03ZpOYoRFdszqhA2cBG8ssKhoBTBcGdGyCVQkyiz4yPKPU3-Gv7Ph5mpcK4YOUW50N6cBAbdlVUbs8snOTBAqB8jfkMfJokG70mOy7HO3nrpiJ3lze0H2rgSMbK1o_H-J60D_hTKhNVBGef9wEKLoe2U5H6FaNKCeifGj0iPNL3w3mSwVB7lP5PorAybxi8_gYfe83m0annzb114nvqAiI7YAMz8WEcYt-VkNMrT1ls9BrITuBNfAFtOnl3IqxjxP9Mbp0mfRX0LPZkZoPSerEs5No8OcmNj4xzsMLtIlFnrGlGNDP3fmcCEcwR22f7W_04Q_uK85OYxwaiiEcC5VRZxcrq0tmiKF-cGe_ktFTziAJZe17zQW-mRpEWCzaL19pqfMW1OWJ66TxqPix6109yZvpbCJkwNvvluGvpSJh1zesdbIxeklB8weohVas-zpOcEK4kBzJzVZzGVhWtkyAs9z7eZCpDuFd_dmCzhxQhZzLX604RVRbqKOK8NfWd037Ya4z-QxGCnCKHNjrPxw5g2kPFrggMf9e2x-SUwH4xv-IIuCyQXK_sEtcTalSdCA2aEBqnxUPzqSe5qiH5ls6PjzmkLr6VcLSa1v3HZpjI6TVlUfwpnGvVjunDsdVUn83qWY1M0Z0vohKOPqqKbvc0u_OJ-b30SHhNmdME4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8041f170b.mp4?token=gHw03ZpOYoRFdszqhA2cBG8ssKhoBTBcGdGyCVQkyiz4yPKPU3-Gv7Ph5mpcK4YOUW50N6cBAbdlVUbs8snOTBAqB8jfkMfJokG70mOy7HO3nrpiJ3lze0H2rgSMbK1o_H-J60D_hTKhNVBGef9wEKLoe2U5H6FaNKCeifGj0iPNL3w3mSwVB7lP5PorAybxi8_gYfe83m0annzb114nvqAiI7YAMz8WEcYt-VkNMrT1ls9BrITuBNfAFtOnl3IqxjxP9Mbp0mfRX0LPZkZoPSerEs5No8OcmNj4xzsMLtIlFnrGlGNDP3fmcCEcwR22f7W_04Q_uK85OYxwaiiEcC5VRZxcrq0tmiKF-cGe_ktFTziAJZe17zQW-mRpEWCzaL19pqfMW1OWJ66TxqPix6109yZvpbCJkwNvvluGvpSJh1zesdbIxeklB8weohVas-zpOcEK4kBzJzVZzGVhWtkyAs9z7eZCpDuFd_dmCzhxQhZzLX604RVRbqKOK8NfWd037Ya4z-QxGCnCKHNjrPxw5g2kPFrggMf9e2x-SUwH4xv-IIuCyQXK_sEtcTalSdCA2aEBqnxUPzqSe5qiH5ls6PjzmkLr6VcLSa1v3HZpjI6TVlUfwpnGvVjunDsdVUn83qWY1M0Z0vohKOPqqKbvc0u_OJ-b30SHhNmdME4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بحرية الحرس الثوري:  ادعى ترامب، في حملته الإعلامية، أن مضيق هرمز تحت سيطرة أمريكا؛ إذا كان الأمر كذلك، تقدموا وأرسلوا إحدى سفنكم إلى مسافة 100 كيلومتر.  الأمريكيون يعلمون أنه إذا اقتربت سفنهم، فسوف يواجهون ردًا من القوات الإيرانية، وقد حدث ذلك في الأيام…</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/90362" target="_blank">📅 09:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90361">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇶
الإعلام الأمني العراقي:
​1- استئناف دخول المسافرين من منافذي (الشيب والشلامجة) اعتباراً من فجر يوم الأحد 2026/9/13 الساعة السادسة صباحاً. ​2- استئناف التجارة في منفذ الشلامجة اعتباراً من يوم الاثنين المصادف 2026/9/14 الساعة السادسة صباحاً. ​3- استئناف التجارة في منفذ مندلي اعتباراً من يوم الثلاثاء المصادف 2026/9/15 الساعة السادسة صباحاً. ​4- استئناف التجارة في منفذ الشيب الحدودي يوم الخميس المصادف 2026/9/17 الساعة السادسة صباحاً. ​كما نؤكد أن حركة العبور والتجارة مع الجانب الإيراني لم تتوقف، ومستمرة بالعمل على مدار 24 ساعة في منفذي زرباطية والمنذرية.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/90361" target="_blank">📅 08:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90360">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇺🇸
🇮🇷
عدوان أمريكي يطال سفينة تجارية إيرانية بالقرب من جزيرة  قشم جنوبي إيران؛ إستشهاد مواطن وإصابة 3 أخرين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/90360" target="_blank">📅 08:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90359">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
بحرية الحرس الثوري:
ادعى ترامب، في حملته الإعلامية، أن مضيق هرمز تحت سيطرة أمريكا؛ إذا كان الأمر كذلك، تقدموا وأرسلوا إحدى سفنكم إلى مسافة 100 كيلومتر.
الأمريكيون يعلمون أنه إذا اقتربت سفنهم، فسوف يواجهون ردًا من القوات الإيرانية، وقد حدث ذلك في الأيام الأخيرة.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/90359" target="_blank">📅 07:29 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90358">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇾🇪
إسقاط مسيرة معادية في سماء محافظة الجوف اليمنية.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/90358" target="_blank">📅 04:33 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90357">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feda8091af.mp4?token=lIcM01BHDm5345rPj-tO26euv7RzaFetmSkoUJOCmrdVPfVqkl1MZ8fcVOdBT1HiSG_5ZVQhlCeo4F--zpFsvNjIFzpkFNsK7rcxRT8TvgKkPzGg9M-CiL4hbXyba87xL9NAavOrQIO7S_vtfR7owiVWZxnTlxf2noYRPcsVDn1nKfKJKALJWViu9lBPBithEGt-ZzpHERC0-MqMvPHAIQBEq2jdCt7giwLhNuCeQlIh_OEZN8t-4nJe6OF1E1AJF49mkWmV7Oz3YNl86L6IxnINeIvmBL36KHkQUJERcwrRaATiXRQT4RuTRCbJ3revsdEuRP3_B6AuDW4ePjlMTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feda8091af.mp4?token=lIcM01BHDm5345rPj-tO26euv7RzaFetmSkoUJOCmrdVPfVqkl1MZ8fcVOdBT1HiSG_5ZVQhlCeo4F--zpFsvNjIFzpkFNsK7rcxRT8TvgKkPzGg9M-CiL4hbXyba87xL9NAavOrQIO7S_vtfR7owiVWZxnTlxf2noYRPcsVDn1nKfKJKALJWViu9lBPBithEGt-ZzpHERC0-MqMvPHAIQBEq2jdCt7giwLhNuCeQlIh_OEZN8t-4nJe6OF1E1AJF49mkWmV7Oz3YNl86L6IxnINeIvmBL36KHkQUJERcwrRaATiXRQT4RuTRCbJ3revsdEuRP3_B6AuDW4ePjlMTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
الدفاعات الجوية اليمنية تتصدى للطيران الحربي السعودي.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/naya_foriraq/90357" target="_blank">📅 03:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90356">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WByN3FHdWeol4IlEo29RN3KhZ2lVwfCHr4F_DBAIOf2oLE1zrZncJa8xO9U_3OMReR5wwPfLih-InmhfEP0iKqIr8fUEQp1MFCCkFnXfesBvUh25yautr6WhPWG_iugc_s7tHoGum5KWsV0kmmBL6gZwRDJjcMhRY6KK3zKGA6C-dEJFUnQcP1CUp3pl2IxmvWAexnfiS8q--89XK8VgxHggidlzpf5toHvr22DAZG3aScxndNgkgIHXc8tBhyGdHPfmNXLsxGbTajqeMlhOaQe4vkuwwh3UZE8fuHpGwfQGXze9_ZoYNMdv-sbYFh01kfANgObeZDyKhTC4uMQFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد مخالفتها للأوامر الإيرانية..
إستهداف صاروخي من قبل بحرية الحرس الثوري يطال سفينة في مضيق هرمز، أدى إلى تعطلها عن العمل.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/90356" target="_blank">📅 03:09 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90355">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce949aeb8c.mp4?token=b7T4__EgxQquSFvRxISU_3tmZN2Q2mVCDNS38yih4saQ6alaIwm0dzzVOtkFbzR76YjC2mwE2qTKSaYGGyzhqWBsjszkc0PR12ukALE5U4IPOJHYCtyBcpMPHxPTaDQGi6Xjz32jPQAglqivbGLaP7F1FVI1cIAPMsb8k6sWPpaGxTbOw9fRJct8t9asFS2udKfiYsAkhmvUp9y0K-QSkRd5sr8jJWcEwzj_gx8CF284hSugE-bnLs5RwWEvOXJQuanIgYT59XM28jdG1ROyZwBad5N9VFM7HTSb5P3KwmRiaWq7mJF7D_cjRg5o9rl21W35Fnl6nbBP24DQN56mdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce949aeb8c.mp4?token=b7T4__EgxQquSFvRxISU_3tmZN2Q2mVCDNS38yih4saQ6alaIwm0dzzVOtkFbzR76YjC2mwE2qTKSaYGGyzhqWBsjszkc0PR12ukALE5U4IPOJHYCtyBcpMPHxPTaDQGi6Xjz32jPQAglqivbGLaP7F1FVI1cIAPMsb8k6sWPpaGxTbOw9fRJct8t9asFS2udKfiYsAkhmvUp9y0K-QSkRd5sr8jJWcEwzj_gx8CF284hSugE-bnLs5RwWEvOXJQuanIgYT59XM28jdG1ROyZwBad5N9VFM7HTSb5P3KwmRiaWq7mJF7D_cjRg5o9rl21W35Fnl6nbBP24DQN56mdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
حكومة إقليم كردستان العراق:
بعد اشتباكات عنيفة ألقت القبض القوات الامنية على وحدتين مسلحتين و21 عنصراً سرياً من تنظيم داعش في محافظة حلبجة، وصادرت كمية كبيرة من الأسلحة الثقيلة والمتوسطة والخفيفة.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/naya_foriraq/90355" target="_blank">📅 01:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90354">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
رداً على استمرار العدو السعودي المجرم في عدوانه على بلدنا نفذت القوات المسلحة اليمنية عملية عسكرية نوعية استهدفت من خلالها مخازن الأسلحة  وغرف القيادة والسيطرة التى تدير العدوان على بلدنا وشعبنا في القاعدة العسكرية بمنطقة شرورة السعودية.
وقد نفذت العملية بدفعة كبيرة من الصواريخ الباليستية والطائرات المسيرة وكانت الإصابة دقيقة ومباشرة بفضل الله وعونه.
نؤكد للعدو السعودي المجرم أن استمرار عدوانه على شعبنا سيقابل بعمليات أشد وأكبر فى عمق أراضيه وستكون عواقبها عليه وخيمة بإذن الله وقوته.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/90354" target="_blank">📅 00:59 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90353">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇸🇦
الاعلام الاجنبي:
‏أفادت تقارير بأن القوات المدعومة من السعودية في اليمن تضم بعض الكتائب التي تتألف من نحو 80% من "الجنود الوهميين"، وهم جنود مزيفون موجودون على الورق فقط لتحصيل رواتبهم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/90353" target="_blank">📅 00:36 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90352">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇷🇺
🇺🇦
الكرملين
: اجتماع بين فلاديمير بوتين و زيلينسكي في قمة مجموعة العشرين التي ستعقد في الولايات المتحدة أمر مستحيل.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/90352" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90351">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfe21f1049.mp4?token=gAvyQ--Mq-saSHkF05BZcZ5vHRd7M_VtfCTGFg52f6H5fQjiL_Z-99wlIL6dHM4kpXaaPCo1ejKIh-AfLMqwFl-kkbKp1l0-bdYzXhMwGK7UNx-nvCsH_KUOKIp6mQMQ91z7PAHsfUzUVh6FJ14lSRX66uNjhR-shTgzF65daT9OCYaM2IT9G3gTiDHp_4SSG5CNq4ngss13NUf9JVrrK1kyrwPEdPFvAwEuP6IOxhm1Al8HvnwiIFWeCnGl0I6u6DUG6mq3IqkZccANXWuEN7AxZLWzJ9JvCUfA-U9xcu_F8GP4EHZ5BN7pW34lh0JY29GI9lmxR-nS3QUIOJXguWDuo5vEro6VRLUTLUBRE-GYZuUk_JuGigmbtLdAzHCDGIitNYDROYLCVg9EUipvXH8NYI3Uja6deoLe89rfD3A1Be35NQopSwZAR2_46SxJXureaZ0hVarXxDwPp674bFVvoYyW4XwGd8Pf-gPuDJROIETZP7f56QVFDQPAQeOLIZmtjUxtl7mavY7-QPp_Keciv968IVfyS6Nok_FenDf1Gvq1vEVY0mPhZimfEqiCZuAeCgDqsluAj20L1Ww-IF2MhAuUhLyVxfdSBkV4IS-FlYiObGNqKkGd2jeL_MITipgqGupds_c1bCFerNxd977eXihIN9m9kqlDuzvip5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfe21f1049.mp4?token=gAvyQ--Mq-saSHkF05BZcZ5vHRd7M_VtfCTGFg52f6H5fQjiL_Z-99wlIL6dHM4kpXaaPCo1ejKIh-AfLMqwFl-kkbKp1l0-bdYzXhMwGK7UNx-nvCsH_KUOKIp6mQMQ91z7PAHsfUzUVh6FJ14lSRX66uNjhR-shTgzF65daT9OCYaM2IT9G3gTiDHp_4SSG5CNq4ngss13NUf9JVrrK1kyrwPEdPFvAwEuP6IOxhm1Al8HvnwiIFWeCnGl0I6u6DUG6mq3IqkZccANXWuEN7AxZLWzJ9JvCUfA-U9xcu_F8GP4EHZ5BN7pW34lh0JY29GI9lmxR-nS3QUIOJXguWDuo5vEro6VRLUTLUBRE-GYZuUk_JuGigmbtLdAzHCDGIitNYDROYLCVg9EUipvXH8NYI3Uja6deoLe89rfD3A1Be35NQopSwZAR2_46SxJXureaZ0hVarXxDwPp674bFVvoYyW4XwGd8Pf-gPuDJROIETZP7f56QVFDQPAQeOLIZmtjUxtl7mavY7-QPp_Keciv968IVfyS6Nok_FenDf1Gvq1vEVY0mPhZimfEqiCZuAeCgDqsluAj20L1Ww-IF2MhAuUhLyVxfdSBkV4IS-FlYiObGNqKkGd2jeL_MITipgqGupds_c1bCFerNxd977eXihIN9m9kqlDuzvip5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/90351" target="_blank">📅 00:26 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90350">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654afe11fd.mp4?token=SLoCtp0aWmbCqX09pUaLLToau5ahR-0YW7lwpwQa6UdjZPoL0bQr9Hf_YdFX4pYnXlt1-Kwl8izdsGRbZUBiREhQ8iwEXAh5F6NTh5D49NMqXqZ0rHHiZsm8g9wEulbq9tjbGFQB19NqXJTkPg-3fR_cNLOXWwfSVUr2Xtja8thI7uDbtU69a5ja00kW6KjtUA2j9sG8Kufw7KSpeQrpiASB86Tgb-n6kRxsvtOD1jvbHXLv3PS_OT36L48xWVRum6qNDxVjZHUeXrs_PVo90BHVICQ9dsJ20LfncX03_Px-14h6wuNvGL5OC_VOhuISG1K9gDwSBBj1p_I7JN52lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654afe11fd.mp4?token=SLoCtp0aWmbCqX09pUaLLToau5ahR-0YW7lwpwQa6UdjZPoL0bQr9Hf_YdFX4pYnXlt1-Kwl8izdsGRbZUBiREhQ8iwEXAh5F6NTh5D49NMqXqZ0rHHiZsm8g9wEulbq9tjbGFQB19NqXJTkPg-3fR_cNLOXWwfSVUr2Xtja8thI7uDbtU69a5ja00kW6KjtUA2j9sG8Kufw7KSpeQrpiASB86Tgb-n6kRxsvtOD1jvbHXLv3PS_OT36L48xWVRum6qNDxVjZHUeXrs_PVo90BHVICQ9dsJ20LfncX03_Px-14h6wuNvGL5OC_VOhuISG1K9gDwSBBj1p_I7JN52lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
توثيق من الجانب العراقي للطريق المؤدي إلى منفذ الشلامجة، حيث يظهر خاليًا تمامًا من حركة الوافدين والمغادرين عقب إغلاق المنفذ.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/90350" target="_blank">📅 00:07 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90349">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">كمين محكم على قوة مكونة من عشر آليات أثناء محاولة فرارها
عملية "والله أشدُ بأساً وأشدُ تنكيلاً"</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/90349" target="_blank">📅 23:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90348">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa40032226.mp4?token=gKhCFAOK-Kj2B2t1FRXuL8klPTc4Hc3QDsBhSunPYwDQnTo2Dn5XKR4H1j9q3I3CGog9m_1raMZ1LCqydErjSte1ps7A9UyOwFbeM34ObavdwAHuJBPOFrHod6ZCzyVm35lENHVOcnU6qqXqXF7iGZwh3r1hhjEf2l0FKuCXck_X-5AGES4i8zTdTfF-VRwkPm853OyAoKE5-mclxk8f3-Cyl0Q3Tn2iUFlLXxmOx4Ngirg6hK9yQ39HXicm09tZm-TUzoGpPk-VeVxH3ExK5O-DIoVN4QVid_ydk4Ohc9POdaY4HX-s2bvRPXNaCreQO-sT_eok-XSeiud8DTM8ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa40032226.mp4?token=gKhCFAOK-Kj2B2t1FRXuL8klPTc4Hc3QDsBhSunPYwDQnTo2Dn5XKR4H1j9q3I3CGog9m_1raMZ1LCqydErjSte1ps7A9UyOwFbeM34ObavdwAHuJBPOFrHod6ZCzyVm35lENHVOcnU6qqXqXF7iGZwh3r1hhjEf2l0FKuCXck_X-5AGES4i8zTdTfF-VRwkPm853OyAoKE5-mclxk8f3-Cyl0Q3Tn2iUFlLXxmOx4Ngirg6hK9yQ39HXicm09tZm-TUzoGpPk-VeVxH3ExK5O-DIoVN4QVid_ydk4Ohc9POdaY4HX-s2bvRPXNaCreQO-sT_eok-XSeiud8DTM8ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/90348" target="_blank">📅 23:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90347">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انباء اولية غير موكدة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/90347" target="_blank">📅 23:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90346">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/90346" target="_blank">📅 23:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90345">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
ضغط مكتب وزير الدفاع بيت هيغسيث من أجل ظهور اثنين من الطيارين الأمريكيين الذين تم إنقاذهم بعد إسقاط طائرتهم من طراز إف-15 فوق إيران في مقابلة مع برنامج "60 دقيقة" للحديث عن عملية الإنقاذ.
كان لدى الطيارين في البداية مخاوف بشأن المشاركة وكشف تفاصيل عسكرية حساسة. بعد التحدث مع هيغسيث، وافق أحدهما على إجراء المقابلة بينما رفض الآخر.
كما أعرب بعض المسؤولين العسكريين عن مخاوفهم من أن المقابلة قد تكشف معلومات سرية أو تستخدم لأغراض سياسية.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/90345" target="_blank">📅 22:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90344">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الله اكبر
سقوط مباشر في جيزان بالسعودية</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/90344" target="_blank">📅 22:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90343">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
تعرض ارهابي على نقطة تابعة للجيش العراقي في محافظة كركوك شمالي العراق</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/90343" target="_blank">📅 22:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90342">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/90342" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90341">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حدث امني في محافظة كركوك</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/90341" target="_blank">📅 22:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90340">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية
: متأهبون لعدم تكرار مثل هذه الاعتداءات على السعودية.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/90340" target="_blank">📅 21:58 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90339">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مشاهد أولية من عملية "والله أشدُ بأساً وأشدُ تنكيلاً" العسكرية النوعية الواسعة من عدة مسارات متزامنة - 12 سبتمبر 2026م</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/90339" target="_blank">📅 21:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90338">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇾🇪
مشاهد الإعلام الحربي من عملية "والله أشد بأسا وأشد تنكيلا" العسكرية النوعية تعرض عند الـ 9:00م بعد قليل</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/90338" target="_blank">📅 21:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90336">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجارات قوية في خميس مشيط</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/90336" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90335">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/90335" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90334">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجارات في سعودية</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/90334" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
