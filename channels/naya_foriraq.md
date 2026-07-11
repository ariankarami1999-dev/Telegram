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
<img src="https://cdn4.telesco.pe/file/dHthEfFWksno0o_TM7PVuUHgiOpOIm7wO6UDOBQUjSMO4GkUaItginkC0bNzAmFNBWJbzLcyuJCRJtzLJeERG2vWKrU4dF0tpZevyBuOj0ba-1AZmGAy1McXaCbUeP3YzBh299w0T1c5P5639JC_DYGEms8jGU2HaSF55abXSyzf8vAsJ8WxhA0LI6MdZ0umrhBdqz3Y1GNo450WWB5JtENHod2_jjeoysrKOuT3_1b2piTs-gMxhJWJzKaq-2T5R6QAx_-_bUH5rCWATuOemQfmzL3Wz2V4SiMh5RQI1WDW57hw8acQe8dFUatb83J6wIiYm5VztcwDT2-OCAqSzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 259K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 17:52:09</div>
<hr>

<div class="tg-post" id="msg-82376">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⭐️
دوي انفجار مجهول في محافظة السليمانية بالقرب من الحدود العراقية الإيرانية.</div>
<div class="tg-footer">👁️ 732 · <a href="https://t.me/naya_foriraq/82376" target="_blank">📅 17:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82375">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🌟
إعلام العدو:
عملية إطلاق نار في شارع القدس بمنطقة يافا ضمن تل أبيب المحتلة؛ إصابة خطيرة كحصيلة أولية.</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/naya_foriraq/82375" target="_blank">📅 17:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82374">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a715d83e0.mp4?token=WzIDcExvpTBirsPiR7q6xea3jL91C__AbVkt9vmBH7VaBxldtDtE35wh1XKBp886mVZpqujXwv033lEyY7LBRru8Yqg1kAvCo2iBQedojV6gI34NEB_FVTE2ofVbcK3iUq18Fi788edFInUGoO3yGiIk3ua2BgzsYcijJbWpdOtvgEUuMxYi9kMw8BQraMtfcC3lDZjkxXAsAbiOFquCb8XKYbymFREQUgbEqjTGKSf771bLx_E9rZWanQ5wjMwW2OAiD7DA28i3M33Figcy8DrRr6LL8SpqtaIBEk-vxeuTXDvhtZQXKDNgepK9Ir-v6GhZhfFz-s0H5MbYNOa-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a715d83e0.mp4?token=WzIDcExvpTBirsPiR7q6xea3jL91C__AbVkt9vmBH7VaBxldtDtE35wh1XKBp886mVZpqujXwv033lEyY7LBRru8Yqg1kAvCo2iBQedojV6gI34NEB_FVTE2ofVbcK3iUq18Fi788edFInUGoO3yGiIk3ua2BgzsYcijJbWpdOtvgEUuMxYi9kMw8BQraMtfcC3lDZjkxXAsAbiOFquCb8XKYbymFREQUgbEqjTGKSf771bLx_E9rZWanQ5wjMwW2OAiD7DA28i3M33Figcy8DrRr6LL8SpqtaIBEk-vxeuTXDvhtZQXKDNgepK9Ir-v6GhZhfFz-s0H5MbYNOa-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إندلاع حريق وتصاعد أعمدة الدخان في مخازن السكك بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/naya_foriraq/82374" target="_blank">📅 17:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82373">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15f4c182d.mp4?token=bEfRcsLff0Tgg6tIpN-X15bnpDU2kSwLidwlK0g7Hds6HhcLIBglOZNKsi6L_KrWLfXRykXiK_18aWPDOSoVLmJ3uKXdXrUIr8xQU98SY_37wY103C96T-6PPJSmj_16j6smGkYKaUG33z0p0uzYNssaJ4Aafo_VpRi8YRXDGUscgizWD4MQD05MUATKC62rCA9cXOkwWNO5IsgVbVU1ySHJl3dc6XG65ZvcMCjQS6zEwL1-UDFb8GTqAhGFisaYUbp4qOiArxtgUu19uCJSWAnfQSirxGURbVikUtwpnpjS20FFjaCT0MEduf560-ZmbjAIm1wvNHYyu3Uoqubi2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15f4c182d.mp4?token=bEfRcsLff0Tgg6tIpN-X15bnpDU2kSwLidwlK0g7Hds6HhcLIBglOZNKsi6L_KrWLfXRykXiK_18aWPDOSoVLmJ3uKXdXrUIr8xQU98SY_37wY103C96T-6PPJSmj_16j6smGkYKaUG33z0p0uzYNssaJ4Aafo_VpRi8YRXDGUscgizWD4MQD05MUATKC62rCA9cXOkwWNO5IsgVbVU1ySHJl3dc6XG65ZvcMCjQS6zEwL1-UDFb8GTqAhGFisaYUbp4qOiArxtgUu19uCJSWAnfQSirxGURbVikUtwpnpjS20FFjaCT0MEduf560-ZmbjAIm1wvNHYyu3Uoqubi2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🔳
قطاعات ‏الجيش العراقي تنتشر في محيط القنصلية الكويتية بمحافظة البصرة لتأمينها وسط تصاعد التوترات والاحتجاجات على خلفية استشهاد صياد عراقي على يد خفر السواحل الكويتي.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/naya_foriraq/82373" target="_blank">📅 17:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82372">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇮🇶
النائب سعود الساعدي يطالب وزارتي الخارجية والعدل بإنهاء الصمت الدبلوماسي وتقديم شكوى واستدعاء السفير وإجبار الكويت على الاعتذار والتعويض عن جريمة قتل الصياد العراقي</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/naya_foriraq/82372" target="_blank">📅 16:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82371">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895e96c42f.mp4?token=S2ijzTv-VPmdOCR9z4n0GhrXC3816OqMNzjTDyAkYIPPME27LK2BU7j1FkZ28kIivh8UrltEXPv_6sArvDat8KkCA-jmiyteZKLytFUo8D8Qzl4PBJsQbrOsS0w7zcvUn_6-02PpwIxjwaLHXKv-xYKHIObfER7MiSztK8pcdAg7UNnyqcKwSB5QXzW_Uj9z6wt58sZES-5w8t6uJi5XfPtqAJWVeB7nzRPdoNRk1F9Zu4dLp_NcNGm_63_rZcNY5Mm72kElyzfXn3wah5SYSBW8wduEljmzcw9tc3mPIjbcwmHEP6cPQYweXoPJJamMA9eygv4xVUgqjjydFkEaWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895e96c42f.mp4?token=S2ijzTv-VPmdOCR9z4n0GhrXC3816OqMNzjTDyAkYIPPME27LK2BU7j1FkZ28kIivh8UrltEXPv_6sArvDat8KkCA-jmiyteZKLytFUo8D8Qzl4PBJsQbrOsS0w7zcvUn_6-02PpwIxjwaLHXKv-xYKHIObfER7MiSztK8pcdAg7UNnyqcKwSB5QXzW_Uj9z6wt58sZES-5w8t6uJi5XfPtqAJWVeB7nzRPdoNRk1F9Zu4dLp_NcNGm_63_rZcNY5Mm72kElyzfXn3wah5SYSBW8wduEljmzcw9tc3mPIjbcwmHEP6cPQYweXoPJJamMA9eygv4xVUgqjjydFkEaWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🏴‍☠️
استهدفت مقذوفات "جيران 4 " الروسية، والمزودة بأنظمة توجيه كهروبصرية، مستودع نفط تابع لشركة "بي آر إس إم-نافتا" في مدينة بيريا سلاف، الواقعة في منطقة كييف. زيلينسكي أعلن اليوم ان بلاده نفذت منها صواريخ الباترويت الأمريكية.</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/naya_foriraq/82371" target="_blank">📅 16:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82370">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكتائب سيد الشهداء</strong></div>
<div class="tg-text">شعبٌ يُقاوِم الاحتلال لن يخون الشهداء.
شكراً يا عراق الوفاء، شكراً يا أشرف شعوب الأمة.</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/naya_foriraq/82370" target="_blank">📅 16:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82368">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36cdfd7d02.mp4?token=Zxtr7Z33QM6yRdE2F9k1I741ZwMqDofYTyqp5vvZjx3CmPRvs3V4-tjakjwBn4BrTLeqm-8rxymhK_2PYv4HUcDRl1xHlVYQgNpWqh8Aydd0LAnlcVMsl7YUFL3YIO68ag7rWrYCQV9RVfZ3JRrhx6_7fz1ZgdsjU2_BnPnIfGp6CFMRblqoGtQCKm7qU7CM0c1g9Y4kSBMoIBUbMeUN6983qD_MzAFXWK3biWLhH2_AW5wxmfmGCoBhVXH1hCqCw-OyvvBYeATMm0a4KA8bFBgpgO1axkE_51Pi1HeiVGx0dDnadyVQFmdHx1ypyvMpe8jcvIyEMtgwEFOObzszWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36cdfd7d02.mp4?token=Zxtr7Z33QM6yRdE2F9k1I741ZwMqDofYTyqp5vvZjx3CmPRvs3V4-tjakjwBn4BrTLeqm-8rxymhK_2PYv4HUcDRl1xHlVYQgNpWqh8Aydd0LAnlcVMsl7YUFL3YIO68ag7rWrYCQV9RVfZ3JRrhx6_7fz1ZgdsjU2_BnPnIfGp6CFMRblqoGtQCKm7qU7CM0c1g9Y4kSBMoIBUbMeUN6983qD_MzAFXWK3biWLhH2_AW5wxmfmGCoBhVXH1hCqCw-OyvvBYeATMm0a4KA8bFBgpgO1axkE_51Pi1HeiVGx0dDnadyVQFmdHx1ypyvMpe8jcvIyEMtgwEFOObzszWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات البرزاني ترسل تعزيزات عسكرية الى قضاء خبات في محافظة اربيل بالتزامن مع تحركات لقبيلة الهركية</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/82368" target="_blank">📅 15:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82367">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇺🇸
نيويورك تايمز عن مسؤولين أمريكيين:
إذا لم تصدر إيران بيانا تقر فيه بفتح الممرات في مضيق هرمز فإن العواقب ليست في صالحها</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/82367" target="_blank">📅 14:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82366">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">AUDIO-2026-03-17-02-59-01</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/82366" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/naya_foriraq/82366" target="_blank">📅 14:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82365">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">"سيتحقق هذا الأمر، وسينفذ قريبًا أحرار من جميع أنحاء العالم جزءًا من هذه المهمة الإلهية"</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/82365" target="_blank">📅 14:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82364">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">14050418_پیام_رهبر_معظم_انقلاب_اسلامی_به‌مناسبت_تشییع_و_تدفین_آقای.pdf</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/82364" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82363">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">14050418_پیام_رهبر_معظم_انقلاب_اسلامی_به‌مناسبت_تشییع_و_تدفین_آقای.pdf</div>
  <div class="tg-doc-extra">150.4 KB</div>
</div>
<a href="https://t.me/naya_foriraq/82363" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇮🇷
البيان الكامل لقائد الثورة الاسلامية سماحة السيد مجتبى الحسيني الخامنئي.
بسم الله الرحمن الرحيم
السَّلامُ عليكَ يا ثارَ اللهِ وابنَ ثارِه، والوترَ الموتور. السَّلامُ عليكَ وعلى جدِّكَ وأبيكَ وأمِّكَ وأخيكَ والمعصومين من وُلدِكَ.
🔸
سلامٌ على الإمام الذي امتدّ نداءُ نهضته الذي يبث الحياة، صدىً عظيمًا مدوّيًا للبعثة النبوية، إلى أعماق التاريخ البعيدة، فانبثقت من أثره الثورة الإسلامية في إيران؛ تلك الثورة التي كانت حسينيةً من أساسها، وبُنيت وارتقت بشعار الحسين (ع) ونهجه. لقد نشأ شهيدُ إيران أيضًا على هذا النهج؛ فكان حسينيًا، وفكّر حسينيًا، وتحرّك حسينيًا، وجاهد وقاوم حسينيًا، وعاش حسينيًا، وبذلَ دمه حسينيًا في سبيل مدرسة الحسين، فنال الشهادة.
▪️
من بين الحسينيين رجالٌ، حين تُسفَكُ دماؤهم مظلومين في سبيل الحسين، ومن أجل مدرسته ونهجه (عليه السلام)، تنهض الأمة الإسلامية، فيتصل ذلك الزمان بعاشوراء، وذلك المكان بكربلاء. واليوم، الملحمة الحسينية ذاتها قد بعثت شعبنا، وأضفت على مدرسة الإمام الخميني الكبير والإمام الخامنئي الشهيد تجلّيًا جديدًا. هذه هي تلك الملحمة التي تبث الحياة، وهي الصدى لنداء مظلومية الحسين (عليه السلام)، ونداء: «هل من ناصرٍ ينصرني؟» في إيران، ثم في العراق وسائر البلدان، فتُزلزل الباطل.
⏺️
كما يجدر، في هذه المناسبة، أن أتقدّم بخالص الشكر والتقدير إلى عشرات الملايين من الناس الذين سجّلوا حضورًا مذهلًا، كاسرًا للأعداء، وتاريخيًا، في مدن إيران والعراق وقراهما، ولا سيما في طهران وقم والنجف وكربلاء ومشهد.
شعبنا يُنادي بالثأر لدماء الحسين (ع)؛ فلقد قدّم هذا الشعب العظيم، على مدى السّنين، أبناءه فداءً في سبيل الحسين (ع)، وفي الحرب ضد أعداء الحسين والغيرة الحسينية، وهو يطالب اليوم أيضًا بالثأر لدمائه ولدماء حسينيّي هذا الزمان.
🔻
والآن، أخاطب إمامنا الشهيد فأقول:
أيها القتيل المظلوم، أيها المظلوم الشامخ، أيها العبد الصالح لله، فيما نحن نودّع جثمانك بعيون دامعة وقلوب مكسورة، نعاهدك أن نصون مدرستك، وأن نسلك بثبات ذلك الصراط المستقيم الذي رسمته، وألّا نهاب مشقّات هذا الطريق، وأن نعقد القلوب، كما فعلت، على البشارات والوعود الإلهية.
⏺️
ونعاهدك أن نثأر لدمك الطاهر، ولدماء شهداء هاتين الحربين جميعهم، من القتلة المجرمين المَخزيين. فهذا الثأر مطلب شعبنا، ولا بدّ أن يتحقق حتمًا. إنّ هؤلاء المجرمين، الذين توجد قائمة كاملة بأسمائهم من أوّلهم إلى آخرهم، سيحملون معهم إلى قبورهم أمنيةَ أن يموتوا موتًا هانئًا على فراشهم. وعليهم أن يعلموا أنّ هذا الأمر لا يتوقف على وجودي أنا أو وجود سائر المسؤولين؛ فنحن، سواء أكنّا موجودين أم لم نكن، سيتحقق هذا الأمر، وقريبًا سيؤدي أفرادٌ من أحرار العالم، كلٌّ منهم، جزءًا من هذه المهمة الإلهية.
▪️
يا أبا الأمّة الشهيد، هنيئًا لك ارتشاف شهد الشهادة الذي كنت تتمناه عمرًا طويلًا. ومبارك عليك ارتداء ثوب الشهادة ببدن يحمل علامات من أمّك الزهراء الطهرى وجدّك أبي عبد الله الحسين وأبي الفضل العباس (عليهم السلام). وأنتم يا رفاقه المظلومين الذين تعرضتم لهجوم مباغت من العدو ونلتم الشهادة، طوبى لكم، إذ تحلّون الآن ضيوفًا على ذلك المولى الذي ربما تلمّستم رأفته ولطفه مرارًا وتكرارًا. إن ذلك السيد الذي يمثل باب الرحمة الإلهية للجميع، ولا سيما لأهل هذه الديار، هو المستضيف لكم الآن، وقد غدا جواره الآمن منزلًا لكم.
⏺️
أيها المولى العالي المقام، أيها الجليل، أيها الإمام الرؤوف، يا أبا الحسن الرضا المرتضى، عليك أفضل صلوات الله، يوارى الآن في هذا الثرى الطاهر الجثمانُ المقطع لخادم من خدّام حضرتك والعترة الطاهرة، بعد سنوات من الجد والجهد والجهاد الدؤوب، ومعه أبدان شهداء من عائلته، يُذكّر كل منهم بشهيد من شهداء صحراء كربلاء، ليرقدوا هنا إلى ذلك اليوم الذي يخرج فيه، بأمر الله، بقية الله (عج) الشَّمس الساطعة من خلف غيوم الغيبة، ليفيض بنور الرحمة الإلهية على أهل المعمورة. وفي ذلك اليوم الذي نرجو أن يكون قريبًا جدًا، سترافقه - عج - نجومٌ من الصدّيقين والشهداء والأولياء، ونأمل أن يكون سيدنا الشهيد أحد هؤلاء، ليعيد مجددًا رسم مشاهد واعدة وخالصة من الجهاد والوفاء بعهد «ألست»، ولعل هؤلاء المرافقين يصحبونه في ذلك اليوم أيضًا.
▪️
يا مولاي الرؤوف، إننا نستودعك سيّدَنا الذي بذل ما يملكه كله في سبيلكم، ومعه رفاقه الشهداء، ليتشرفوا بلطفكم وعنايتكم، وكما كانوا ينعمون بفيض لطفكم في حياتهم الدنيا، فليحظوا به من الآن فصاعدًا على نحو أكمل وأسمى بكثير.
وفي الختام، نتقدم مجددًا بالعزاء لسيدنا بقية الله (عج)، ونبتهل إلى ذلك المولى الرحيم أن يشمل بدعائه الزاكي سيد شهداء إيران ورفاقه الشهداء والشهداء كلهم، وأن يسأل الحق (جل وعلا) علو الدرجات للشهداء جميعهم، والصبر والأجر لذويهم، والفتح والنصر الحاسم والقريب للشعب الإيراني المظلوم، إن شاء الله.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/82363" target="_blank">📅 14:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82362">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">قائد الثورة: أقول لراعينا الشهيد: يا قتيلًا مظلومًا! يا مظلومًا منتصرًا! يا عبدًا صالحًا لله! الآن، ونحن نودع جسدك بعيون دامعة وقلوب حزينة، نعهد إليك بأن نحافظ على مذهبك، وأن نسير بثبات على الطريق المستقيم الذي رسمته، وأن لا نخشى الصعاب في هذا الطريق، وأن…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/82362" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82361">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قائد الثورة السيد مجتبى الخامنئي: نَعِدُ بأن ننتقم لدم القائد الشهيد ودم جميع الشهداء في الحربين من القتلة المجرمين عديمي الشرف.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/82361" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82360">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قائد الثورة السيد مجتبى الخامنئي: أود أن أعرب عن خالص تقديري لحضور الملايين، وهذا الحضور المذهل والملهم الذي يحطم أعداء الثورة، في مدن وقرى إيران والعراق، وخاصة طهران، قم، النجف، كربلاء، ومشهد.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/82360" target="_blank">📅 14:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82359">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قائد الثورة السيد مجتبى الخامنئي:
أود أن أعرب عن خالص تقديري لحضور الملايين، وهذا الحضور المذهل والملهم الذي يحطم أعداء الثورة، في مدن وقرى إيران والعراق، وخاصة طهران، قم، النجف، كربلاء، ومشهد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/82359" target="_blank">📅 14:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82358">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئيس الوزراء العراقي يوجه وزارة الخارجية ورئاسة أركان الجيش والجهات الأمنية المعنية ميدانياً في محافظة البصرة بمتابعة تفاصيل حادثة مقتل الصياد العراقي نجم عبد الله واتخاذ الإجراءات القانونية التي تمنع تكرار مثل هذه الحوادث</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/82358" target="_blank">📅 13:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82357">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🏴‍☠️
أوكرانيا تنشر مشاهد من بحر آزوف تدعي فيه إصابة 28 سفينة روسية تابعة لـ "الأسطول الظل" خلال الليلة الماضية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/82357" target="_blank">📅 12:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82356">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ff607673.mp4?token=NoFm0_p_CfXhzLRm8AumPcfQXbeXJLMwi0dYiJjn_vPHtcS381o-zeOgyKdeFiPhGyNwYClieCqd8cUlrckAac5mLHj7n7WAAf8gohbLSKVhQMlKVgGJOtXpfrLNqggxe53oJg9jg_f918nSlS9MYZIrxFr_2NwdNJGzLLHjchv3LKfgkVp3LGhvcfb4tBi3yBT2KIABIqBBI8d8Z1GkD84tCyWQy-u9kJoX8bFElDAtxWHmYhpkxlhHV32Wvh_411wMmdkiCPYPPI0XGLyw3S3rKuw9LN1C-bSY0p0Q5SwUEQeb62nEKcOP1QHa2msbvjS1wqIi07KsR4q2jZl9Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ff607673.mp4?token=NoFm0_p_CfXhzLRm8AumPcfQXbeXJLMwi0dYiJjn_vPHtcS381o-zeOgyKdeFiPhGyNwYClieCqd8cUlrckAac5mLHj7n7WAAf8gohbLSKVhQMlKVgGJOtXpfrLNqggxe53oJg9jg_f918nSlS9MYZIrxFr_2NwdNJGzLLHjchv3LKfgkVp3LGhvcfb4tBi3yBT2KIABIqBBI8d8Z1GkD84tCyWQy-u9kJoX8bFElDAtxWHmYhpkxlhHV32Wvh_411wMmdkiCPYPPI0XGLyw3S3rKuw9LN1C-bSY0p0Q5SwUEQeb62nEKcOP1QHa2msbvjS1wqIi07KsR4q2jZl9Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الكويت لم تكتفي بقتل الصياد العراقي.. اعتداء جديد يوثقه أحد الصيادين العراقيين لخفر السواحل الكويتي أثناء مطاردته لهم في مياه خور عبد الله العراقية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82356" target="_blank">📅 11:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82354">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇸🇾
دوي انفجارات تهز السخنة بريف حمص السورية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/82354" target="_blank">📅 11:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82353">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇸🇾
دوي انفجارات تهز السخنة بريف حمص السورية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/82353" target="_blank">📅 11:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82352">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwt8ZFyW5F26npsBmY5g9kr3ZdFsrYGJ5PmDPJxgFMo2spQAkeM6bU7A6fPK53Y0eEHB1R1jb26asImMx6YPHJhmviwbypHcScRerpsSW1dIZ2IRtAIGxNH4THndT9NVwsWO2-nngk-D2_0vXP9kccc3kmn387ZkI78U5ssD97hPFU_PGRaOTGaa3o4-M3LmaCziyCeHPsBGM6N3OUBJoOW_WhL0j4mJtyjomp8n0rbwr_TyEylXwaFPpqhQvzE8otH6bybFllAkqwj2E8H01JiL65wMYpCLTOQJ1dkAX2Jiqs5cZBQn6kjKF4BknKlrl4yIBDs5iMYuTPpfuACyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
إدارة ترامب تصدر مذكرات استدعاء لصحفيي صحيفة نيويورك تايمز الذين كتبوا تقارير حول مخاوف أمنية تتعلق بطائرة "إير فورس وان" التي تبرعت بها قطر لترامب.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/82352" target="_blank">📅 10:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82351">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">أنباء عن سماع انفجارات في مدينتي باكداشت وقيام دشت شرق محافظة طهران.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82351" target="_blank">📅 09:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82349">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=C1zmi3QSPhuHUwbJJisOx5Z2zk9PLgH8jRGsdMGoVaGgQfmQjVl4jSo6itvFEoDsv9Lp0n3rF26PL_ji8Kmop9Wo9wEqkUT5ferGksUqy0pUbIBBi4D2VSuA-90u9BZchz8RUyQ1mkWm_BkOQ1R2XLzcU4275laas90L0mnxOxTb-9tySfiIHvj19ekmgBlg5pleFqGgUWK8m6kfQFDjBqfk9RiSgfgXcwmuvsVIenzbkgpmKl8fckQNRr0byD7i2H9N0inu06wjvMuKtci_kL5cEKJafEW0sQqmfemhHwW3bfUe71j2v06WdmVXq4u46iMu97SIdVDbfJFgEH5amg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95215f1b5f.mp4?token=C1zmi3QSPhuHUwbJJisOx5Z2zk9PLgH8jRGsdMGoVaGgQfmQjVl4jSo6itvFEoDsv9Lp0n3rF26PL_ji8Kmop9Wo9wEqkUT5ferGksUqy0pUbIBBi4D2VSuA-90u9BZchz8RUyQ1mkWm_BkOQ1R2XLzcU4275laas90L0mnxOxTb-9tySfiIHvj19ekmgBlg5pleFqGgUWK8m6kfQFDjBqfk9RiSgfgXcwmuvsVIenzbkgpmKl8fckQNRr0byD7i2H9N0inu06wjvMuKtci_kL5cEKJafEW0sQqmfemhHwW3bfUe71j2v06WdmVXq4u46iMu97SIdVDbfJFgEH5amg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أنباء عن سماع انفجارات في مدينتي باكداشت وقيام دشت شرق محافظة طهران.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/82349" target="_blank">📅 09:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82348">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">أنباء عن سماع انفجارات في مدينتي باكداشت وقيام دشت شرق محافظة طهران.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/82348" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82347">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEWmQPm19GyBwafl5dYbd2aXDpnaFTjdwMhueGVjJSYaTnkcayCtyaH8grQ1_Hw1tfYKUtixknBD8vElHz91iMb3vUHH9llXdFn4b4nyILq8QEIVAKpTK8oy0Vi7dy4cPZSdlpBR4d95uJxSXpsg3IPyy3kMcLqRZtOsw9pWvd36dvF1Vc5ri_sJ7OnqnUZM0tQ_LoPQd7_psfquifGacVeJG18cUYnZSIr1m_Vmeo5jsx4L79R7UZtSyDie4fdNVSUyGhBM8stt9Aw6LAwW-Jy607Sdq0SxQwWTzViWn0RlZOJEm0Xl6xzmVZMR660707ocec3awNyERAEGv2-V3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
طائرة وزير الخارجية الإيراني عراقجي تهبط في مسقط عمان</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/82347" target="_blank">📅 08:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82346">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knOHQZ-i_kU6qYnQmQa8XT3ity6IU-LCp7aMcfCDXEx_T7QaKgqfTvSK27o5g6Xc2tj6OWzFjHwgjAx9Fgq6RniIZG541dG437-G4hve5NfFLWnPq4cnd4ZT2m2apW1n1xa8kZnvYfJq5qoldIMhs76vLY9TV45OKJg3BzWug4rjANwpc-GGkqkbT0Ze5nkJT9zAy8F-nd4XALXXvlXVS5oFfv8DZainF8p6MfdhJRu5GUCv6QdnD5Oq9VSsVBes8nwsiwxf7h-S_cTwNH9r4F4OTRdwgZdb4fcX4h-UVdkUkt4qer-ivMaFZ4PPSEHYOz5JR3L2SV0Xmfgai4r1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇮🇷
شركة شحن صينية عالقة بمضيق هرمز تسير بتباطؤ حاد حيث تتراوح سرعتها الحالية بين 0.1 إلى 0.4 عقدة بحرية فقط (شبه متوقفة) تشير المعلومات أنها قد تكون تعرضت لهجوم إيراني. لأنها مرت بالممر الأمريكي</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/82346" target="_blank">📅 08:42 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82345">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sh47EP-A-dsfjf5-5s73EKrkjZIHyRKjd8__iPjEp6NpNtd5pLN0V79J4jVZfNQrTrlYwvxmbWp4exMpBNR615izjDkKL1q1rzdM4tqKfLG8SoiGpVJKxWbd7tPRyjYgG_ah2BYeNYfanH3MEK5Dl_lzVoeB9fF0HK_4eeR7tMAPMbX7Dxp3d0SOoE-qyblaa5lgFlD3sSxVdtL2hYCVM5Cej-WGvOI2lEYNQLIyF7RjVI0AO9yewVl9dCI9GJo5U3eiVbH8vipHnFFk0rRmJVgd2dvsM_eCU7hquCCiprBrjHGuM860DO3QUDIOa0kxgzc5KJEC2NENi5Bg-axI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🔻
🇺🇸
قناة نيوز ماكس :
تم إيقاف تشغيل مؤقتًا حاملة الطائرات "يو. دي. كي. بوكسر" ومجموعة المشاة البحرية رقم 11 (MEU) التي كانت على متنها، في الأسابيع الأولى من الصراع مع إيران، بسبب عطل في نظام تبريد محركات السفينة، مما اضطر سفينة الإنزال إلى تغيير مسارها والتوجه إلى جزيرة دييغو غارسيا لإجراء الإصلاحات.
ويُذكر أن هذه المشكلة غير المتوقعة في الصيانة أدت إلى حرمان الولايات المتحدة  من قدرة استجابة سريعة مهمة، في الوقت الذي كان فيه البنتاغون يفرض حصارًا بحريًا على إيران ويدرس خيارات عسكرية إضافية.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82345" target="_blank">📅 08:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82344">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">📰
وول ستريت جورنال عن مسؤولين أمريكيين: إدارة ترمب ترى أن احتمالات التوصل لاتفاق نووي مع إيران تتضاءل</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/82344" target="_blank">📅 02:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82343">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
مالم تستطيع أمريكا أن تخفيه للوجهه القبيح لتنظيم النصرة الإرهابي
🔻
الصحفية الألمانية إيفا ماريا ميشلمان التي تم اعتقالها في سجون الجولاني في سوريا لمدة 6 أشهر تروي ما تعرضت له بمؤتمر صحفي في ألمانيا حيث حذرت المجتمع الأوروبي من حكومة الجولاني قائلة: "أرجوكم لا تصدقوا أن نظام هيئة تحرير الشام ديمقراطي بأي شكل من الأشكال".</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/82343" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82342">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الانفجارات في بلدتي الفوعة وكفريا حيث مكان تواجد الفصائل الإرهابية من الجنسيات الأجنبية</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/82342" target="_blank">📅 00:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82341">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📰
رويترز عن مسؤولون أمريكيون كبار: ‏إذا لم نحصل على الغبار النووي، فلن يكون لدينا اتفاق مع إيران.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/82341" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82340">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوي انفجارات تهز محافظة إدلب السورية</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/82340" target="_blank">📅 00:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82339">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوي انفجارات تهز محافظة إدلب السورية</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/82339" target="_blank">📅 00:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82338">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSDudGkYCIkuaiQFAOQcJkqkC0IuLGZbWo8yFWECc0__jpEtqEHslRuGBDx3QuYKCzi4PlyLS3iuwaw47hOSaj6SaHQQ3zA23x7JNJDW7lGQWL53Lj-mp5oPnz8_4s7kGzOdrUJZrO5HscSs0tpmDfVZzNm--yjSGb_9-SPcj884ZT1E3fc4MEIvD9jF0irtPJwS5v8yh484vif80Be2iHUf2E7FsXCbz_ePO-GAn0Xh0rEKq6uwklPOVvZPOWAIY_k78sM2p02OxPQf8MO8nwDuSOG6dtZ10kIdgtRKTLVcc93E5iH_6H6Y6cGQWHjLamP3ITheJs96aJzFF-6zIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/i/status/2075679676492558827</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/82338" target="_blank">📅 00:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82337">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-pK6KDLVKucKPOf7z3IauoL4RF2F9PIx384iTM4UUjs3Jqo1JYsjvjsF8mQ2hR8rY_FsOT-xrxti9Ce7qaqPMeOJRuessXWEElzNYwERB9CdsqwDKCSeg_RO9Bzv_zzHMZ2-80wILFdgop8HFUyNkyF1jaVcp0DVnhZKdRtBhSO64bRZM8gZA0f4MRJ72xiS2vW0CPknIHbiCKf2wEi_4I10nFWZneZF-41N0PnyxNcRWniw8pNd9_R00IwajKfvSAePw0zz87hFlz7q43ezj0NvRbplUIg6K1-C4glRSMoF2Kx7IYe52UzdmmkcFD0ppjfLrub7qbPKBMADpAxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم ﴿مِنَ الْمُؤْمِنِينَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَيْهِ فَمِنْهُمْ مَنْ قَضَى نَحْبَهُ وَمِنْهُمْ مَنْ يَنْتَظِرُ وَمَا بَدَّلُوا تَبْدِيلاً﴾ في محطة تاريخية استثنائية تجلت فيها أسمى معاني الوفاء وتجديد العهد، سطرتم —أيها…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/82337" target="_blank">📅 23:53 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82336">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔻
مراقبون لنايا  البيان قد يتضمن ثلاثة محاور ابرزها شكر الشعب العراقي بالتشيع و أيضا يتضمن رؤية المقاومة عن السلاح و  يبدو أن التنسيقية لم تعد موجودة حيث أن البيانات باتت تصدر بأسم المقاومة الإسلامية في العراق.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/82336" target="_blank">📅 23:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82335">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
مراقبون لنايا  البيان قد يتضمن ثلاثة محاور ابرزها شكر الشعب العراقي بالتشيع و أيضا يتضمن رؤية المقاومة عن السلاح و  يبدو أن التنسيقية لم تعد موجودة حيث أن البيانات باتت تصدر بأسم المقاومة الإسلامية في العراق.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/82335" target="_blank">📅 23:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82333">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pf_P0rP_yNqM7iUc-GoR5NsMONxtK4yoPiKK8Y-MYoZu2TaB_EoDEdKd-Grt2AgLBHmxUt-ieRK7gIDeRjvXHIaw0URX0Lqo46-kD8hhm0G4tnmkSykHNzCf2xvGb1xLNDnWTIyzyeeF8JRCztGr8Lt7ZdM1jb_kFAuB8oU0FPBWJ6yFeYMwdFZKm9nncFfgzahaV2Mhr37K8EMk15agxbH_7I9ACfg_FJ-Qa09b-eHBT8jhu2q8Wvx_RJH15FIUIDSv88PbBvZvlcOv-Iw4Wz0zixjMg1UcBh-jOmVHffVYO9DExNe0Z9sqZwuj9aPDQljhGfEyYE8g2RdXJUlqhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
﴿مِنَ الْمُؤْمِنِينَ رِجَالٌ صَدَقُوا مَا عَاهَدُوا اللَّهَ عَلَيْهِ فَمِنْهُمْ مَنْ قَضَى نَحْبَهُ وَمِنْهُمْ مَنْ يَنْتَظِرُ وَمَا بَدَّلُوا تَبْدِيلاً﴾
في محطة تاريخية استثنائية تجلت فيها أسمى معاني الوفاء وتجديد العهد، سطرتم —أيها الشعب العراقي الأبي— ملحمة تليق بعظمة سند المستضعفين الإمام الشهيد السيد علي الخامنئي (رضوان الله تعالى عليه)، وبحضوركم المليوني لتشييع جثمانه الطاهر في النجف الأشرف وكربلاء المقدسة؛ برهنتم أن الشعب العراقي الأصيل سيبقى متمسكًا بخطه المقاوم، ومكملاً لنهجه الجهادي في مقاومة الاستكبار العالمي.
إننا من أرض المقدسات نعلنها مجدداً ولتسمعها قوى الشر: إننا ثابتون، ومتمسكون بنهج المقاومة، وليعلم الأعداء أن قوى محور الحق كالجسد الواحد وفق الأطر الجهادية التي خطها لنا قائدنا الشهيد، ولن تثنينا الخطوب، ولن تزيدنا إلا إصراراً على مواصلة نهجنا لنصرة المستضعفين، وطرد المحتلين من العراق والمنطقة.
إن سلاحنا الذي تزينت به سواعد رجالنا في الميادين لم يكن يوماً خياراً للمساومة، بل هو عقيدة وعهد في أعناقنا، وأمانة الإمام المنتظر صاحب الأمر (عجل الله فرجه الشريف) ونائبه المفدى؛ وبه سنمضي لنكسر قيود الهيمنة، ونكبح جماح المستكبرين، فإما نصر عزيز تقر به أعين الصالحين، وإما شهادة تلحقنا بركب الأنبياء والصديقين.
وعليه، فإننا نؤكد للقاصي والداني أننا لن نقف عند حدود ما وصلنا إليه، بل سنعمل —بكل ما أوتينا من عزم وقوة— على تطوير قدراتنا العسكرية والأمنية كماً ونوعاً، ورفع الجاهزية بما يتناسب وحجم التحديات والتهديدات المتصاعدة التي يشكلها العدو الصهيوأمريكي؛ ولن يهدأ لنا بال، ولن تغمض لنا عين، حتى نبدد أوهام الطغاة، ونصون الكرامة، ونحفظ السيادة.
المقاومة الإسلامية في العراق</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82333" target="_blank">📅 23:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82332">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بسبب الحر او الفگر وسط بغداد
اندلاع اشتباكات بمنطقة السنك وسط العاصمة بغداد ٥ جرحى كحصيلة أولية..</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/82332" target="_blank">📅 23:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82331">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">حصري لمكتب النائب حسين الدراجي
....................................
زيارة الصيادين العراقيين بعد عودتهم من أسر الكويت
((تم استهدافنا لأننا شيعة واتهمونا بأننا من الحششد الششعبي))</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82331" target="_blank">📅 23:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82330">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اندلاع حريق في قاعدة دبلن قرب مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/82330" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82329">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حدث أمني في العاصمة بغداد</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82329" target="_blank">📅 23:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82328">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حدث أمني في العاصمة بغداد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/82328" target="_blank">📅 23:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82327">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
تنويه:   المقاومة الإسلامية في العراق ستصدر بعد قليل بيان هام.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82327" target="_blank">📅 23:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82326">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
تنويه:
المقاومة الإسلامية في العراق ستصدر بعد قليل بيان هام.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/82326" target="_blank">📅 23:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82324">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71b2c4bd96.mp4?token=VQK9TD8iJ0BL4Nnhu7QklxnymLWT6Iu3UMOHy3Kf5P1uKlh1nrOunPzlEcjHX0E3iirSxM7E3frTKZIGVhmzLJEAnD7XbTSm_1IEtos3lc1Uh489jP6KeIjYekqJT5npIUNmsb0UxMW14iiTjQfvbUIHq6_UQ2R-JHDCNGs5k1TO8jmqRaThu0hfS4PZFVClKtD38_cGEO4oRx5M6lfgACxS5_Qb7lCB2OndR-vb3tkhmq0pfsfJ_2j4xGPsgaJusuWZbz_qfBGkmcEe7PIFEbJ6Q5GUdU5hqsE5SF3kNJJESkL6-tnnbwWI3ORA3k4ZTZ5cylJKx6mwBU7XA7eK9TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71b2c4bd96.mp4?token=VQK9TD8iJ0BL4Nnhu7QklxnymLWT6Iu3UMOHy3Kf5P1uKlh1nrOunPzlEcjHX0E3iirSxM7E3frTKZIGVhmzLJEAnD7XbTSm_1IEtos3lc1Uh489jP6KeIjYekqJT5npIUNmsb0UxMW14iiTjQfvbUIHq6_UQ2R-JHDCNGs5k1TO8jmqRaThu0hfS4PZFVClKtD38_cGEO4oRx5M6lfgACxS5_Qb7lCB2OndR-vb3tkhmq0pfsfJ_2j4xGPsgaJusuWZbz_qfBGkmcEe7PIFEbJ6Q5GUdU5hqsE5SF3kNJJESkL6-tnnbwWI3ORA3k4ZTZ5cylJKx6mwBU7XA7eK9TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شيّع العراقيون بالملايين جثمان الشهيد المعظّم آية الله العظمى السيد علي الحسيني الخامنئي (قدس سره)، في مشهدٍ مهيبٍ جسّد أسمى معاني الوفاء، واختلطت فيه دموع الحزن بمشاعر الوداع، فيما اعتصرت القلوب ألماً وهي تودّع قامةً تركت أثراً كبيراً في وجدان الأمة.
#قوموا_لله
#باید_برخاست
#KHAMENEI</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/82324" target="_blank">📅 22:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82323">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d532f551d.mp4?token=pOIKXbfZKhT3exbyHWXIkoeKhMZuY0oEIPr8lo_800s7ESw3sHRXxfIw2HTujSXrR0abMg42d4TPSoqQQwHbYpzBBQsynD_85FHn6I4xciQHll6yhLZ6aWYXQgdGaJis5vA6pDzQ6nppE7AMLDOHQtwf5oIwRmRnS3TvkYnrTtKpaRgHNKxZ9hhWQqi2His-vWG_val8pff3qPQUq05Onm2lbWpzpLGAF1Q855ouTXZvxV3pTJ8v85mjyUroGAuWiSp9Sxg54IeLp80EHSahXtk37aX1zrPTNxszlI0m7y5swECdOKZZG9HMHzZCv2T4vyRwcPFE_8oOiGGY-Aa1DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d532f551d.mp4?token=pOIKXbfZKhT3exbyHWXIkoeKhMZuY0oEIPr8lo_800s7ESw3sHRXxfIw2HTujSXrR0abMg42d4TPSoqQQwHbYpzBBQsynD_85FHn6I4xciQHll6yhLZ6aWYXQgdGaJis5vA6pDzQ6nppE7AMLDOHQtwf5oIwRmRnS3TvkYnrTtKpaRgHNKxZ9hhWQqi2His-vWG_val8pff3qPQUq05Onm2lbWpzpLGAF1Q855ouTXZvxV3pTJ8v85mjyUroGAuWiSp9Sxg54IeLp80EHSahXtk37aX1zrPTNxszlI0m7y5swECdOKZZG9HMHzZCv2T4vyRwcPFE_8oOiGGY-Aa1DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترمب: بإمكان سوريا المساعدة في مجابهة حزب الله  ‏سأرفع سوريا من قائمة الدول الراعية للإرهاب</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82323" target="_blank">📅 22:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82321">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الأخوة الكرام في الفديو يظهر رجل امرأة عراقية اثناء تشيع السيد القائد  هل لديكم اي تفاصيل او إمكانية الوصول اليهم او عنوانهم لغرض التكريم ؟!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82321" target="_blank">📅 22:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82320">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇺🇸
‏وزير الخزانة الأميركي:
سنواصل استخدام كل الوسائل لعزل نخبة النظام الإيراني
سنحافظ على الأصول المحتجزة لصالح الشعب الإيراني
عقوبات على "علي أنصاري" أبرز ممولي مكتب المرشد الإيراني
استهدفنا شركات صرافة إيرانية تساعد على نقل مليارات الدولارات سنويا
أنصاري كون شبكة في دول عدة بعد اختلاسه أموالا لصالح مسؤولين إيرانيين</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/82320" target="_blank">📅 22:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82319">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇮🇶
الأمين العام لكتائب حزب الله الحاج أبو حسين الحميداوي: بسم الله الرحمن الرحيم (وَلَا يَزَالُونَ يُقَاتِلُونَكُمْ حَتَّىٰ يَرُدُّوكُمْ عَن دِينِكُمْ إِنِ اسْتَطَاعُوا ۚ وَمَن يَرْتَدِدْ مِنكُمْ عَن دِينِهِ فَيَمُتْ وَهُوَ كَافِرٌ فَأُولَٰئِكَ حَبِطَتْ أَعْمَالُهُمْ…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/82319" target="_blank">📅 21:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82318">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
الأمين العام لكتائب حزب الله الحاج أبو حسين الحميداوي:
بسم الله الرحمن الرحيم
(وَلَا يَزَالُونَ يُقَاتِلُونَكُمْ حَتَّىٰ يَرُدُّوكُمْ عَن دِينِكُمْ إِنِ اسْتَطَاعُوا ۚ وَمَن يَرْتَدِدْ مِنكُمْ عَن دِينِهِ فَيَمُتْ وَهُوَ كَافِرٌ فَأُولَٰئِكَ حَبِطَتْ أَعْمَالُهُمْ فِي الدُّنْيَا وَالْآخِرَةِ ۖ وَأُولَٰئِكَ أَصْحَابُ النَّارِ ۖ هُمْ فِيهَا خَالِدُونَ)
ألا فليعلم الطغاة المستكبرون، أنه ليعز على قلوبنا أن نرى إمامنا الخامنئي، قائد الأحرار وناصر المستضعفين في العالم، مسجى بدم الشهادة، في وقت يتبجح فيه قاتلوه بجريمتهم، ويتمتعون بالملذات في غفلة من العذاب والطيش، وسيعلم الذين ظلموا أي منقلب ينقلبون.
الحمد لله الذي منّ علينا بنعمة السير تحت راية إمامنا الخامنئي طيلة ثلاثة عقود ونصف، متمسكين بنهجه، ومستنيرين بفكره؛ فما بخلنا يوما بالغالي والنفيس، بل سيّرنا قوافل من الشهداء الأبرار، الذين خطت دماؤهم الزكية أولى معالم هذا الدرب؛ ابتداء من قاماتنا الأولى: الشهيد الشيخ فاضل العمشاني، والشهيد القائد علي الفريجي، والشهيد القائد عباس فتح الله، مرورا بالقائد الشهيد أبي حسن الفريجي، وكل من التحق بركبهم الطاهر ممن ذابوا في عشق الولي، وظلوا أوفياء للعهد، حتى نالوا شرف إحدى الحسنيين: نصر مؤزر أو شهادة في سبيل الله.
وقد خضنا تحت رايته (رضوان الله عليه) غمار النزالات، واقتحمنا ساحات المعارك؛ ابتداء من مقارعة طغيان نظام البعث البائد، صعودا إلى مجابهة الاحتلال الأمريكي وسائر قوى الشرك المتحالفة معه منذ وطأت أقدامهم أرض العراق عام 2003، وكسرنا شوكة التنظيمات الإجرامية من القاعدة وداعش في سوريا والعراق، ودككنا حصون الاستكبار في معركة طوفان الأقصى، وحربي الاثني عشر والأربعين يوما؛ رجال لا تلين لهم عزيمة، ولا يزحزحهم وعيد الأعداء.
لقد تأسست كتائب حزب الله على يد شهيد الأمة وبقرار منه، فكان رجالها وما زالوا يوالون هذا الخط والنهج المبارك؛ وها نحن اليوم، نقف بثبات لا يتزعزع، معاهدين إمامنا الشهيد (رضوان الله عليه) وخليفته المفدى، أن نبقى على العهد جندا أوفياء، ودروعا حصينة للعقيدة والمقاومة، ولم نبدل تبديلا.
لقد أثبت الشعب العراقي الأبي في يوم التشييع التاريخي المهيب لقائد محور الخير والمقاومة، وبما لا يدع مجالا للشك، أنه شعب مقاومة وجهاد؛ فكان ذلك الزحف بمثابة استفتاء شعبي مليوني حاسم، جدد فيه العراقيون الأصلاء دعمهم وتمسكهم بالمقاومة الإسلامية وسلاحها المقدس، وهو ما يوجب علينا اليوم، انطلاقا من هذه الأمانة الشعبية، أن نجدد العهد والبيعة لحامل الراية، على الثبات في هذا النهج المقاوم لهيمنة المستكبرين والظلمة، وعلى رأسهم أمريكا؛ فرعون العصر والشيطان الأكبر. عهدا نذود عنه بالأرواح، ليحق الحق، ويزهق الباطل، إن الباطل كان زهوقا.
وفي هذا المنعطف التاريخي، نلفت أنظار القادة السياسيين، والمسؤولين الحكوميين، إلى وجوب الانصياع لإرادة الشعب العراقي الأبي—شعب المقاومة والجهاد—والحذر الشديد من الانجراف في ركاب المشاريع الاستكبارية، أو التماهي مع أجنداتها الخبيثة. ونحذرهم بأن شعبنا سيقول كلمته وقراره إذا ما انحرفت البوصلة؛ وحينها.. ولات حين مندم.
(سَلَامٌ قَوْلًا مِّن رَّبٍّ رَّحِيمٍ)
الأمين العام لكتائب حزب الله
الحاج أبو حسين الحميداوي</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/82318" target="_blank">📅 21:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82317">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇶
🇺🇸
السفارة الامريكية في بغداد: ندعم رؤية حكومة العراقية بنزع السلاح ونتطلع إلى التنفيذ الكامل والشامل والسريع.  لا يابة لا ايران تتدخل بالعراق</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82317" target="_blank">📅 21:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82316">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMgYI8g-KufL09_XE8x9YMFHQk7FRa2KjxRYvnzKe9I6av_EYntVIFsGnuvz4rH5p7K8VXnkWGsRM1ZlP6Rs2bswGHgfvAI3uSpsNcRSvt7sq9omDCzdjGzVWP0cepkzO75IdIb_PLeQUQzgU34eaN6jS4HCiPgULZJws55hRgnDjaLqnkeVHz6AjqrT6zdmc130QJqOGu7pcTGkIOo0OuUO-vhdHB1uAYi8VBdRABluumSG1j2ky8TiZWDD3PmRhkUceckw4k--Dg8fd6Kr08Z3MqxTzEH5zefZee5sf7_-5FoE1wtOes--dB_2WGmzuZ4eqOTXvHh7c16KnRc40w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الأخوة الكرام في الفديو يظهر رجل امرأة عراقية اثناء تشيع السيد القائد  هل لديكم اي تفاصيل او إمكانية الوصول اليهم او عنوانهم لغرض التكريم ؟!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82316" target="_blank">📅 21:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82315">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نايا - NAYA
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/82315" target="_blank">📅 21:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82314">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02f1693de4.mp4?token=XuzBBObCFmjFADJ5UQIflmQvBJKqEFv6h_UsF-QEV3D8QVS60_RkaJjXKiDTjZ230-6f-h6dezTWZ6JaW_74ahIDw6W23b3D0xbK9BtFAklRbV33r_Tz_GrFXxntsj3ruU18fqe5Ws5lidrLJIQMejaVYAyohUKtdzmyiDQKK_IR7tD9QfUjhwhIcyAa7H25v0V0Cn9vuK11nkmNXtriXxrmDaudHZElyutjraAzQcp7Hna9NjGfzinPlMcnBZs2gx6_ssxLNCw3p2o68e2JtaJr7ZPyKll7Il-vNxbcC6xYDAdZaPIxbg3UTOdRW3cVsECr4KCEO4Z6hMVVZrtR5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02f1693de4.mp4?token=XuzBBObCFmjFADJ5UQIflmQvBJKqEFv6h_UsF-QEV3D8QVS60_RkaJjXKiDTjZ230-6f-h6dezTWZ6JaW_74ahIDw6W23b3D0xbK9BtFAklRbV33r_Tz_GrFXxntsj3ruU18fqe5Ws5lidrLJIQMejaVYAyohUKtdzmyiDQKK_IR7tD9QfUjhwhIcyAa7H25v0V0Cn9vuK11nkmNXtriXxrmDaudHZElyutjraAzQcp7Hna9NjGfzinPlMcnBZs2gx6_ssxLNCw3p2o68e2JtaJr7ZPyKll7Il-vNxbcC6xYDAdZaPIxbg3UTOdRW3cVsECr4KCEO4Z6hMVVZrtR5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الأخوة الكرام في الفديو يظهر رجل امرأة عراقية اثناء تشيع السيد القائد
هل لديكم اي تفاصيل او إمكانية الوصول اليهم او عنوانهم لغرض التكريم ؟!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/82314" target="_blank">📅 21:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82313">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">😆
ما يسمى ‏مجلس القيادة اليمني المقيم في السعودية :
رحلة "ماهان" الإيرانية لصنعاء انتهاك لسيادة اليمن والقانون الدولي</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/82313" target="_blank">📅 21:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82312">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsQSsfN358mJp1dCVy2EUVl2hMCzNYjLM2YxF_eTvFW1Pge9IIqEF_ikYdib0KyVjD9lwGWw45e4fECGdTwHwsRVQTXk3lgjB26uunHPDi1Yg1UFoI0PCSw7_2mWg84u_QB-2ARsSt5gv0Ioy-MTLTa6XDS1nG9RKIRCO3lOIP-lU6T1Uq2hjjCFZ95Kz23h6N4SxYwhAo7enCcYM26ofBBcYHyVMYWD4ltaE70PTSRaUvTN85UHGJQLaB1p9Xjw6GZ8jnkGcREt0ZzjHxl7GGIyDUpI2ArLeRBHCOIIMHyk3ksmGARo6bMjZMiwSSimHz0pzd-gLY1tgrCUxXsuQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🔵
تغيرات دبلوماسية روسية كبرى بالشرق الأوسط قطر وسوريا والعراق قريبا
هل ستنجح روسيا ام سيستمر الأداء الخجول المتواضع ؟!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82312" target="_blank">📅 20:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82311">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
🇺🇸
السفارة الامريكية في بغداد:
ندعم رؤية حكومة العراقية بنزع السلاح ونتطلع إلى التنفيذ الكامل والشامل والسريع.
لا يابة لا ايران تتدخل بالعراق</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/82311" target="_blank">📅 20:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82310">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
🌟
فارس
:
نفي ادعاءات قناة العربية وفوكس نيوز بشأن مفاوضات الأسبوع المقبل بين إيران والولايات المتحدة
في أعقاب نشر أخبار من قبل قناة العربية وفوكس نيوز حول عقد جولة جديدة من المفاوضات بين إيران والولايات المتحدة في الأسبوع المقبل، كشف مصدر مطلع قريب من فريق التفاوض الإيراني، في تصريحات لمراسل وكالة فارس، أن هذه الادعاءات غير صحيحة.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/82310" target="_blank">📅 19:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82309">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9458162b3e.mp4?token=B1wRapQSRMyFjc1Y10CdvEEISP1o_fgAytpO0_dWNnNpwmG42Izj81WC7fiq49vsdXATeD5YN2RYEoMTvoblDPREmSCJcIoS5KydzXFZatatl9CLvLeVtc5eRWfmec62zRJxo83EmusvIIGM4bRVNyNL8dVuXq7fswL0B--yhHBpayB6bPym4n_ooUP-sT5fy6LQs5wqSZ8fY0FqAwsY2CPtHuNzutjdbEVmb6OeqxI0bqc7yQARjiRsZeHzzeR1y0adq97A173Pu1wCSZU2EKRPLyzPxVZRVOWs8V10DJQWXSs8xXp3IjPVclvMlWdsYKf-BzvrwM1Vgnn5bh4-kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9458162b3e.mp4?token=B1wRapQSRMyFjc1Y10CdvEEISP1o_fgAytpO0_dWNnNpwmG42Izj81WC7fiq49vsdXATeD5YN2RYEoMTvoblDPREmSCJcIoS5KydzXFZatatl9CLvLeVtc5eRWfmec62zRJxo83EmusvIIGM4bRVNyNL8dVuXq7fswL0B--yhHBpayB6bPym4n_ooUP-sT5fy6LQs5wqSZ8fY0FqAwsY2CPtHuNzutjdbEVmb6OeqxI0bqc7yQARjiRsZeHzzeR1y0adq97A173Pu1wCSZU2EKRPLyzPxVZRVOWs8V10DJQWXSs8xXp3IjPVclvMlWdsYKf-BzvrwM1Vgnn5bh4-kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
بعد تصاعد الخلافات بين عناصر الجولاني ولاسيما بين المتشددين ومن يُوصفون بأنهم أكثر ميلاً إلى السلطة والمال ؛ هكذا بدأت حكومة الجولاني بتصفية بعض المتطرفين من عناصرها مع إرجاع أسباب وفاتهم إلى حوادث سير وجلطات دماغية ومرض العضال.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/82309" target="_blank">📅 19:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82308">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvLWcXB-lH18bs0U6PHtyW7Sv2flqYo_0yLB0ppy-yuE4GZEnK3-LpPsBowk855OXzt5F073CftcqX1Da3B9hIaw8QWMs5Ib3TdvTu-KM4KIeqWiBPt-0L6YxJjHiuUa-O9IRkoEnaGNKvW798pmHOiI7rl7w4WCnA2I3lUX0HzdOq2kn4WfTnUJkHGmw2rcACUGj-j6zEnM3TCtQYyrimxRLZIGb9p_yY9KGxLuzckkTQBv1dL2zwRndwKyNKjNpL1-JRl06uRzLiFRPt5qCfbVs9Z7Anll2CAv9oJYRmnT78yJ-ngjPg76NLqIfocVNfE0I96rT7zSoq-Ctogozw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
رئيس المجلس السياسي لحركة النجباء:
على الحكومة ان تضع حدا للاستهتار الكويتي، وإلا، فإن للشعب قولة وصولة !!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82308" target="_blank">📅 19:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82307">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
‏ترامب:  «طلبت منا الجمهورية الإسلامية الإيرانية مواصلة "المحادثات". وقد وافقنا على ذلك، لكن الولايات المتحدة أوضحت لهم، بعبارات لا لبس فيها، أن وقف إطلاق النار قد انتهى! شكرًا لاهتمامكم بهذا الأمر. الرئيس دونالد جيه. ترامب».</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/82307" target="_blank">📅 18:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82306">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTT1J5ya6hBSDln6XeDOBh3ryMyvS7nxXzoMkZN_3Qep5Ot5aOjR56gTGDoWv8NJ2P_n1g8CcGXskiLXynbgwTjhdGGEyj7oNjGV_mGPhQKQfRHOo4fwhudNxs_z5npSGumxpkd50h1egJhHKv_vhHQvTqWqz9wW8XLhffZVuIOJquF-p1dVttS1x8yc37p5Qr4V95SukRdZlHLnsFLjsZ5NcdhPB-R4FNEInBU2iVhGkXLK74IqxLLFtZoAtx7hRcZPDtnEesY6Lh_tdj6HhL1OLNfHBYSkEQrMP0N_Y0v4WwanqJ4L6ZovY8egp6uHuqBL9y3D2Xg-iWbMSnlrtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
‏
ترامب
:
«طلبت منا الجمهورية الإسلامية الإيرانية مواصلة "المحادثات". وقد وافقنا على ذلك، لكن الولايات المتحدة أوضحت لهم، بعبارات لا لبس فيها، أن وقف إطلاق النار قد انتهى! شكرًا لاهتمامكم بهذا الأمر. الرئيس دونالد جيه. ترامب».</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/82306" target="_blank">📅 18:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82305">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇷
‏جلسة لمجلس الأمن بشأن النووي الإيراني</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/82305" target="_blank">📅 17:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82304">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
‏جلسة لمجلس الأمن بشأن النووي الإيراني</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/82304" target="_blank">📅 17:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82303">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b551c66b.mp4?token=pA0nJsQLhdCNzvx5fHBb_o1a1f9t0-A9wIauQgHh0Llu6BP_4Hnv4sF-XPVAZU8cfkrUSB_D-ixK4meslqXNWnQAc7jV8Jhv9F06eLKl8u2Z3qK-TQzr-7qTaloGiYxjt4m8LS7ECFU2ce1_PUqYFDVSq6N_a57BF1R0u7SAtcUwvj4eD-MG0NAs-mqUwf8XpaCvVb5xHt7AR--DPFA4GVLPuNXzqm8xvoYy662LR8DDztw-XcKnPJx6e-MRXtJMZHFMgKmvgg-6jsrr-yE2SluPj8pnlWj0iY4psDYU1jfQJ4iJKDcpH-C7f4WgMRD-UK6YD8Q2ufMxxF03n-2xrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b551c66b.mp4?token=pA0nJsQLhdCNzvx5fHBb_o1a1f9t0-A9wIauQgHh0Llu6BP_4Hnv4sF-XPVAZU8cfkrUSB_D-ixK4meslqXNWnQAc7jV8Jhv9F06eLKl8u2Z3qK-TQzr-7qTaloGiYxjt4m8LS7ECFU2ce1_PUqYFDVSq6N_a57BF1R0u7SAtcUwvj4eD-MG0NAs-mqUwf8XpaCvVb5xHt7AR--DPFA4GVLPuNXzqm8xvoYy662LR8DDztw-XcKnPJx6e-MRXtJMZHFMgKmvgg-6jsrr-yE2SluPj8pnlWj0iY4psDYU1jfQJ4iJKDcpH-C7f4WgMRD-UK6YD8Q2ufMxxF03n-2xrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
IRGC now</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82303" target="_blank">📅 17:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82301">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BcnyWNNPaNTii0-Q_u76S63qFZTUaPPqz0IzpGaob-t59psPYE4laePNntp9BiOdGMRKEbCHDXfkO_Xz_sp6MVGZO87nnwjBgsc91YMiay0WiVj4Mtp5i_YsxYT2DFuECAfOpGlKB6SKL9gxu_ARBZFqhPpyfxwhN4ys_yif5OR315A6swPrTh2RrXR4hV3M5cehlyrKpuRXlalEyYbVNL155IVYPSk1rg8ft2awh-WcnWoL7hqFzQZiKsHTbKp0fmSgKdYYqTnbg7HIuPtW4pwpRDVQyFS4oMOf6XeQcKlHv29EXyChRauFAdNqRSzPTfCz8QiWvveHc18us5N_-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tC2OPpfF37_5lrlOKE37eQo37I9VM0uEPpbOqNdTOwwKRxsJloflumlyA1nuc6K2XwcD9wkaU478WZXvCOd90TH0zin8ra9IKQ2xcszpXdfj8lSHh2JE7fAzv-O4gBOdrKrDQzxn0-1OxGHaMfRpgA3am-NKGUQZNOCcPaMl-spQU9Ht_6vhUcoYIhRJkYRnponDDQsZywj2O_U5slemfrEYEpDYS-4bQJeSliLmcSUSq0WQF-W5M_oJi23ce_DY3yWlqXDtHWozq2WTxnaPZInOlG3ag84i8e1g3OiVWTowZzLwwFX2F5eFIJ-2WsL8dOn5p-tdDDjd306ksgLExg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇺🇸
مواقع التتبع: رصدت حاملة الطائرات الأمريكية "يو إس إس أبراهام لينكولن" في صور الأقمار الصناعية "سنتينل-2" بتاريخ 10/07/2026 تبحر الحاملة حاليًا شمالًا في خليج عُمان، وتقترب بشكل خطير من نطاق صواريخ إيران، دون وجود أي مرافقة مرئية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82301" target="_blank">📅 17:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82300">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏴‍☠️
زيلينسكي : لم تعد مصفى في روسيا اسلحتنا لا تستطيع الوصول إليها ؛ استهدفنا مصافي روسية على عمق ٢٥٠٠ كم في سيبيريا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/82300" target="_blank">📅 17:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82299">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
🔵
🇮🇶
بسبب عدم فعالية منظومة الباتريوت
وزارة الدفاع الألمانية : تقرر تقليص عدد قواتها من ٥٠٠ إلى ٣٠ عسكري في محافظة اربيل شمالي العراق وابلغت حكومة الإقليم بهذا القرار بعد ان كان مقرر بقائهم حتى منتصف عام ٢٠٢٧.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82299" target="_blank">📅 16:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82298">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇺🇸
القيادة المركزية الأمريكية:
مروحية من طراز CH-53 سوبر ستاليون تابعة لسلاح مشاة البحرية الأمريكية تقوم بتوصيل الإمدادات إلى سفينة تابعة للبحرية الأمريكية في بحر العرب.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/82298" target="_blank">📅 16:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82296">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hm0UAAQ2FzYvbcGVkM0b7C1VAVBSzTzWkcRvgiJ9g3PQEe0LM4cOvUJGxM6_XE4O_ZUBvR0FRIdBhZ3Xl8Qp2455du2WFo83G-OytsbMrJfACTIq-DlTzzDQhZz5Pr6YxD5VmbVh8cKpwu2E8ORZ7t4blWPky9ELXcvy5INSt4xH3xGcm7FXgjE4jHSXLf6zjh3nxw_DJre23CcwWGDBouowqAzNJen-giKKqH4I9Sl-xuBT1wzuVermQVxx1nc9kt6-LU36y0NRe7RGozuIYs-XEHj8iZg9emKMngXbaBC-uLA7Lyh1XgJjfJCvDciv3PblWz4ciBCVZWapggNZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i4A8A8OJBZB_DIDqdAxa1MLCK18EXwa_d3okuBBkrcS7aOBS6nWJO7Go49xyZTfxVyHm928zF_n4HShNlpadGix5ZmcGy2A9R7Z6HcFR4R3Z6cb3heGD8k-vCLMxvROXH5XIDkcqY7fMwSIq6jW7FaYO_kbpWeQfcaULTv1-AWF5glq_8zTUkDQyjPxBaBo21trriB5Bo2RZC3HKfcTx2kHHyWAD66vYUB8SInku-UQTf0Hdo73rQjEDFlAghfXKV6V_ikDUfImzHIq2CXcgTIhdOhq6BbBTrau8tNkQDFRBEwPTounzeaqZUhlVi9CgiQ3aZX09y6Ga6aYOs9_Jjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇺🇸
مواقع التتبع:
رصدت حاملة الطائرات الأمريكية "يو إس إس أبراهام لينكولن" في صور الأقمار الصناعية "سنتينل-2" بتاريخ 10/07/2026 تبحر الحاملة حاليًا شمالًا في خليج عُمان، وتقترب بشكل خطير من نطاق صواريخ إيران، دون وجود أي مرافقة مرئية.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/82296" target="_blank">📅 16:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82295">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nzto440WcpzO1ZneQNWX67buS2HlFYq21aurQ-3IqhQvSpS1nFwxJmIqu-EiN0s48SVvwNR-I3D3GRYNDU4YorzQK4W2sYx3GZ6PqIN9Jv-JBbMki8gEAYWxzVIG-fdNR3fPCn57RSPICrcNQ6uiDvs213qBO-40bgB1fhfs1u7zVU21_INYr5NQBl9qjli3ZFGo9yyGYGaMZ4Ek8DZbebMuJZI3sQ_mGUdlkzQPK6cKcgbI8gc1FUog8qvCWYYKXSIwlRadT8CFx_LSgGeY5-5JUuq9pnt6XcpP6zuG1TAZ0UXIean8occzZ0A2rvV2BLJPsMJo2jTVfdC6cgjjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
لن أوقع على مشروع قانون الإسكان الذي وافق عليه الكونغرس بالكامل وأُرسل إلى البيت الأبيض احتجاجًا على حقيقة أن مجلس الشيوخ الأمريكي غير قادر على تمرير قانون إنقاذ أمريكا، الذي يحظى بتأييد 97% من الحزب الجمهوري، ونسبة عالية جدًا من الديمقراطيين غير السياسيين.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82295" target="_blank">📅 16:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82294">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
غضب شعبي واسع في محافظة البصرة وعموم العراق وإضراب شامل يدخل حيز التنفيذ في مراسي بيع الأسماك مع تظاهرات مرتقبة للصيادين عصر اليوم احتجاجًا على قيام خفر السواحل الكويتي بقتل صياد عراقي ودعوات للحكومة العراقية لاتخاذ موقف حازم إزاء الجريمة الكويتية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/82294" target="_blank">📅 16:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82293">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇮🇷
نائب الرئيس الايراني:
العراق كان لسنوات تحت الاحتلال والنفوذ الأمريكي. الحضور الواسع للشعب في النجف وكربلاء أغضب ترامب، وأظهر أن النفوذ الروحي للقائد الشهيد يتجاوز حدود إيران.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82293" target="_blank">📅 16:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82292">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">📰
مصادر لـCNN:
ادارة ترامب لا تريد مشاركة اسرائيل في الهجمات على ايران.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/82292" target="_blank">📅 16:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82291">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
🔹
غروسي مدير الوكالة الدولية للطاقة الذرية:
نحن نراقب الوضع في محطة بوشهر للطاقة النووية في إيران ونحث جميع الأطراف على ضبط النفس.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/82291" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82290">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇶
فيلق بدر يرصد هتافات الملايين.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/82290" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82289">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇷🇺
🇮🇷
وصول اول 6 موظفين من شركة روس آتوم الروسية الى محطة بوشهر النووية</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/82289" target="_blank">📅 15:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82288">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
بيان لرئيس هيئة الحشد الشعبي
:
بعد اختتام مراسم تشييع المرجع المعظم الشهيد السيد علي الخامنئي (رضوان الله تعالى عليه)، التي شهدت حضوراً جماهيرياً تاريخياً جسّد عمق الوفاء الذي يكنّه الشعب العراقي لرموزه وقادته، نتوجه بخالص الشكر والتقدير إلى جميع الجهات التي أسهمت في إنجاح هذه المناسبة الوطنية والإنسانية الخالدة.
ونتقدم أولاً بجزيل الشكر إلى الحكومة العراقية والعتبات المقدسة لما وفرته من دعم ورعاية وتنسيق عالٍ أسهم في نجاح المراسم، كما نعرب عن بالغ تقديرنا إلى قواتنا الأمنية التي أدت واجبها بكفاءة ومسؤولية عالية، وأسهمت في حفظ الأمن وتأمين انسيابية مراسم التشييع.
ونخص بالشكر أبناءنا في هيئة الحشد الشعبي، وفي مقدمتهم الأخ رئيس أركان الهيئة، وجميع القادة والمجاهدين والمنتسبين، الذين بذلوا جهوداً استثنائية في التنظيم والخدمة والتأمين، مؤكدين روح الانضباط والإخلاص في أداء الواجب.
كما نتقدم بخالص الامتنان إلى المواكب والهيئات الحسينية، والمتطوعين والخدّام، وإلى الأسرة الإعلامية والثقافية، والنخب الفكرية، ومنظمات المجتمع المدني، وكل من أسهم في خدمة المشيعين ونقل صورة هذا الحدث التاريخي إلى العالم.
ونعبر عن عميق تقديرنا لعائلة المرجع الشهيد، على ثقتها بالشعب العراقي، كما نقف بإجلال أمام أبناء شعبنا العزيز الذين صنعوا بحضورهم ووفائهم ملحمةً ستبقى خالدة في ذاكرة العراق.
نسأل الله تعالى أن يتغمد الشهيد الجليل بواسع رحمته، وأن يجزي جميع من أسهم في إنجاح هذه المناسبة خير الجزاء، وأن يحفظ العراق وشعبه، ويديم عليه نعمة الأمن والوحدة والعزة.
رئيس هيئة الحشد الشعبي
فالح الفياض</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/82288" target="_blank">📅 15:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82287">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔻
رئيس أركان الحشد الشعبي عبد العزيز المحمداوي:
بسم الله الرحمن الرحيم
لقد أقدم أبناءُ العراق الأوفياءُ والغيارى، مرةً أخرى، على تعريف العالم بمواقف الكبرياء، وفاضت فيهم مكارمُ الرجولة والشهامة والبطولة وكرم الضيافة والمواساة وأداء واجب العزاء.
فكانوا جديرين باستقبال وتشييع وتوديع السيد الزائر لجدّه أمير المؤمنين (عليه السلام)، والشهيد الوافد على جدّه سيد الشهداء (عليه السلام).
وكأنّه أراد أن يقول: (أوفيتَ يا ابنَ رسولِ الله).
عظّم الله أجوركم،
وأحسن الله لكم العزاء،
وشكر الله سعيكم.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/82287" target="_blank">📅 15:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82286">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
🇮🇷
مشاهد تنشر لأول مرة
جانب من مجلس العزاء النسائي في النجف الاشرف لتوديع جثامين العائلة المباركة للامام الشهيد
#قوموا_لله
🏴</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82286" target="_blank">📅 15:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82285">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6c1048520.mp4?token=YkclLSnZ0QeNhNmVjS1yuc_cqKHAYG8sktvzHHGmAcuU2ccLjQUe9134awealGx7qfsy8B4izKSNXE1yXF5DkWwq1RvGnE7uVlNbqZ-WV7ozQrnwGRw0EyC0qE0VG3Iq_4gnrsafZmu4_Kd5WUBwxx8bq2eYlJJo1Cd9AoASmke10RrWeeomxiV6vkwsphPeRR3Xnwfpb5P0oWQ0Kku7jhh383pGEYaO-cjnh5pcssfS8A_BG0xVCpqbWLlUMS0Lja3D2jKbTN_m9nAk51_s4Gtl0PSFq6xq_GApvDI-TVuLnqR6VAckGKPa1IXKlJM6KmwyzBxyal3Q6f4S0IW9Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6c1048520.mp4?token=YkclLSnZ0QeNhNmVjS1yuc_cqKHAYG8sktvzHHGmAcuU2ccLjQUe9134awealGx7qfsy8B4izKSNXE1yXF5DkWwq1RvGnE7uVlNbqZ-WV7ozQrnwGRw0EyC0qE0VG3Iq_4gnrsafZmu4_Kd5WUBwxx8bq2eYlJJo1Cd9AoASmke10RrWeeomxiV6vkwsphPeRR3Xnwfpb5P0oWQ0Kku7jhh383pGEYaO-cjnh5pcssfS8A_BG0xVCpqbWLlUMS0Lja3D2jKbTN_m9nAk51_s4Gtl0PSFq6xq_GApvDI-TVuLnqR6VAckGKPa1IXKlJM6KmwyzBxyal3Q6f4S0IW9Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اندلاع حريق كبير وغامض بالقرب من مطار اربيل الدولي شمالي العراق
🚨
🔥
، قرب المطار توجد قاعدة للجيش الأمريكي!
🇺🇸
✈️</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/82285" target="_blank">📅 14:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82284">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
اندلاع حريق كبير وغامض بالقرب من مطار اربيل الدولي شمالي العراق
🚨
🔥
، قرب المطار توجد قاعدة للجيش الأمريكي!
🇺🇸
✈️</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/82284" target="_blank">📅 14:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82283">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
مجلس القضاء الاعلى في العراق يصدر بيان بخصوص "سرقة القرن":  موجز هذه الجريمة يتلخص بان الشركات الأجنبية العاملة في العراق تودع لدى الهيئة العامة للضرا ئب امانات  بقيمة 5% من قيمة المشروع لضمان انجازه وبعد انتهاء عمل الشركة من حقها تسحب هذا المبلغ خلال خمسة…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/82283" target="_blank">📅 14:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82282">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇶
مجلس القضاء الاعلى في العراق يصدر بيان بخصوص "سرقة القرن":
موجز هذه الجريمة يتلخص بان الشركات الأجنبية العاملة في العراق تودع لدى الهيئة العامة للضرا ئب امانات  بقيمة 5% من قيمة المشروع لضمان انجازه وبعد انتهاء عمل الشركة من حقها تسحب هذا المبلغ خلال خمسة سنوات ولكن شركات التعقيب ومنها شركتي المحكوم نور زهير القانت والمبدعون اتبعت اجراءات غير اصًولية في عملية سحب هذه الامانات  لهذا تم اتخاذ الاجراءات القانونية بحق جميع المتورطين بهذه الجريمة من اصحاب تلك الشركات والموظفين اللذين ساعدوهم في عملية السحب الغير أصولية.
ثانيا
تم الاتفاق بين رئيس مجلس القضاء ورئيس مجلس الوزراء السابق  وبعد الحصول على موافقة القاضي المختص بالتحقيق في تلك القضية على اطلاق سراح المتهم الأساسي فيها المدعو نور زهير بكفالة ضامنة لاعادة تلك الاموال المسحوبة وعلى شكل دفعات مقابل تخفيف العقوبة عنه في حينه وفعلا تم اعادة مبلغ قدره ٣٦٥ مليار دينار من اصل مجموع المبلغ المترتب بذمة الشركتين  التابعة له القانت والمبدعون وقدره (١,٦١٨,٣٧٠,٨٨٢,٠٠٠) ترليون دينار وهذا المبلغ هو جزء من مجموع المبلغ الكلي المسحوب من مصرف الرافدين من قبل جميع شركات السحب والبالغ قدره ( ٣،٨٣١،٣٧٠،٨٨٢،٠٠٠) ثلاثة ترليون وثمنمائة وواحد وثلاثين مليار وثلثمائة وسبعين مليون وثمنمائة واثنين وثمانون الف دينار عراقي
ثم سافر المتهم المذكور خارج العراق  وتوقفت عملية التسديد لهذا تم احالته على محكمة جنايات  مكافحة الفساد المركزية وصدر حكم غيابي بحقه بالسجن لمدة عشر سنوات مع تنظيم ملف استرداد ومخاطبة مديرية الشرطة العربية والدولية لاعادته إلى العراق
بعد صدور قانون تعديل قانون العفو قدم محامي المحكوم المذكور طلب بشمول موكله بالقانون مقابل اكمال  عملية تسديد بقية المبلغ المترتب بذمته  وفعلا تم مخاطبة وزارة المالية لبيان الرأي بخصوص هذا الطلب باعتبارها الجهة المتضررة ويجب استحصال موافقة الوزير على الية تسديد المبالغ المترتبة بذمة المحكوم بحسب قانون تعديل قانون العفو ولم ترد إلى المحكمة اي اجابة بخصوص ذلك لذا بقي موضوع شمول المحكوم المذكور بقانون العفو معلق لحين الاتفاق مع وزارة المالية على الية تسديد المبالغ مع المحكوم او وكيله المحامي
وفي نفس الوقت صدرت احكام حضورية بالسجن بحق  ١٢ موظف بعناوين مختلفة في الهيئة العامة للضرائب ممن ساعد المحكوم في عملية سحب المبالغ  بمعاملات خلاف السياقات المتبعة وحاليا هم في السجن يقضون مدة محكوميتهم مع ملاحظة  إمكانية  شمولهم بقانون تعديل قانون العفو النافذ لكن بعد تسديد قيمة التعويض الذي تحدده وزارة المالية ويدفع من قبلهم
كذلك صدرت احكام غيابية بالسجن  بحق مدير مكتب رئيس الوزراء في حينه وعدد من المستشارين مع تنظيم ملفات استردادهم من الدول التي يقيمون فيها كذلك مذكرات قبض بحق اخرين  مع ملاحظة ايضا ان جميع هولاء ممكن شمولهم بقانون تعديل قانون العفو في حال تسديد ما ترتب بذمتهم من مبالغ
وصدرت احكام حضورية بالسجن بحق اشخاص من غير الموظفين استغلو علاقاتهم مع وزير المالية في حينه وساهمو في تسهيل سحب اموال هذه الشركات .وتمت مصادرة اموالهم المنقولة وغير المنقولة
وتم اجراء التحقيق مع رئيس الوزراء الذي حصلت خلال فترة حكومته هذه الجريمة وتم غلق التحقيق بحقه لعدم كفاية الادلة
كذلك تم مصادرة عقارات واموال منقوله في العراق ودولة الكويت عائدة لقسم من المحكومين الموجودين حاليا في السجن
ثالثا
اما بخصوص قضية شركة مصافي الشمال والمتهم الموقوف عدنان الجميلي وعدد من اعضاء مجلس النواب سوف يتم اتباع نفس الاجراءات المشار اليها فيما تقدم في حال كون جريمة اي منهم مرتكبة قبل تاريخ نفاذ قانون تعديل قانون العفو و يسدد ما بذمته من أموال إلى الوزارة المتضررة
اما إذا كانت الجريمة مرتكبة بعد نفاذ  قانون العفو سوف يتم التعامل مع المتهمين بسياقات واجراءات مختلفة كون جريمتهم غير مشمولة بقانون العفو .لدا يجري البحث حاليا و بالاتفاق   مع السيد رئيس الوزراء  لوضع خارطة طريق تتفق مع الآليات الدستورية و القانونية لتحقيق الهدفين المنوه عنهما في اعادة اموال الدولة مقابل تخفيف الاجراءات القانونية بحق من يعيد تلك الاموال طوعا.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/82282" target="_blank">📅 13:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82281">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇬🇧
‏ هيئة بحرية بريطانية: التهديد الأمني في مضيق هرمز لا يزال مرتفع</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82281" target="_blank">📅 13:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82280">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇶
رئيس جمعية الصيادين العراقيين بدران التميمي يروي تفاصيل استشهاد الصياد برصاص خفر السواحل الكويتي</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/82280" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82279">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇷🇺
الكرملين:
سنوسع المنطقة الأمنية داخل أوكرانيا.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/82279" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82278">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇶
غضب شعبي واسع في محافظة البصرة وعموم العراق وإضراب شامل يدخل حيز التنفيذ في مراسي بيع الأسماك مع تظاهرات مرتقبة للصيادين عصر اليوم احتجاجًا على قيام خفر السواحل الكويتي بقتل صياد عراقي ودعوات للحكومة العراقية لاتخاذ موقف حازم إزاء الجريمة الكويتية.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/82278" target="_blank">📅 13:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82277">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
غضب شعبي واسع في محافظة البصرة وعموم العراق وإضراب شامل يدخل حيز التنفيذ في مراسي بيع الأسماك مع تظاهرات مرتقبة للصيادين عصر اليوم احتجاجًا على قيام خفر السواحل الكويتي بقتل صياد عراقي ودعوات للحكومة العراقية لاتخاذ موقف حازم إزاء الجريمة الكويتية.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/82277" target="_blank">📅 13:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82276">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تبعات حرب إيران
🇮🇷
⚔️
‏
الطاقة الدولية:
نتوقع عجزا في المعروض العالمي للنفط بـ 860 ألف برميل يوميا في 2026
🛢️
📉
.
إمدادات النفط العالمية ستنخفض بمقدار 3.7 مليون برميل يوميا في عام 2026
🛢️
📉
.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/naya_foriraq/82276" target="_blank">📅 11:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82275">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
🇮🇷
مسؤول أمريكي حول إيران:
الوضع متغير وقد تستأنف الضربات إذا لزم الأمر.
قائد حاملة الطائرات لينكن ببحر العرب أبلغ أفراد طاقمها بالحفاظ على جاهزيتهم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/naya_foriraq/82275" target="_blank">📅 10:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82274">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXvuGMcLj20yOgAP-nxx9sYwTS4vCQz4qctrjcimdBNUqqI0joQtkD2IoqjPoK1ZkdVkleVlQINqRImB66R6kkJMYhTJp-V7YHcbg4HtfXpMgInzjnUuXDDyr1BAPqepGKQn9lyGEU4ukGN1jlTLKimwkVcUEbHnnPclHX63IW43Sb57hLZMwmu6B3UUlxZNhET6DPNACr119TH8VjOX-QYDf6VKmDJoPEbb7HlqN60YVk-UaYCqSNC0q2qPJIR9LAwFn8O5RhTDXZRGH2eM4nsvqWt3P34mZokWInlcKvIY6sILdrXSGq-RiGLAG-C2gy28ukCBxitQen9boEZX_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
الرئيس الإيراني مسعود بزشكيان يوجه رسالة شكر إلى العراق وشعبه والمراجع العظام على مراسيم التشييع المهيبة التي جرت في العراق.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/naya_foriraq/82274" target="_blank">📅 06:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82273">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
مسؤولين أمريكيين:
التقرير الإسرائيلي عن مخطط إيراني لاغتيال ترمب قد يكون محاولة لدفعه نحو التصعيد.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/naya_foriraq/82273" target="_blank">📅 04:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82272">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مسؤول أمريكي:
عدم شن الجيش الأمريكي ضربات جديدة على إيران الخميس جاء نتيجة جهود إقليمية لخفض التصعيد</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/naya_foriraq/82272" target="_blank">📅 02:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82271">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbYNg025CI-blCw4OTxzlW-_OikwY5A4TkicQ_cm_caF7KBJrV_6AVSW9jqDSDYVs_qcE5OSiosJv1B2eqW6NZp34Ld7VBgBT6F1wnZmhOb1HPjXFf4vuIAEPtwCKGy1J_zGK0Q-8RtXTtacKbkJYdlXLSC7QjImsSdsCui9cnI2OsMwwANSKBtX2fg2b9XAfaLpAX2hZMMyLmDmTDrRhhwpM2Cjr0Vf2SUOEWqsovTPToE3OF5nzcv3bsz4__TAvmOI0rHG-lj3_cmpusdmYp3xtjDCFPb7rKqpgb0wmOKmyqNZa90MLxYfvSvhuNiiqopLmEveZVc3zKE7n6i9AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الآن تم دفن أمامنا القائد
💔
الصلاة الصلاة يرحمكم الله
#قوموا_لله
🏴</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/naya_foriraq/82271" target="_blank">📅 01:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82270">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇷
مصدر إيراني: لم يحدث أي حادث أمني قرب مرقد الإمام الرضا (ع) أو على طول مسار تشييع جثمان الشهداء.  "بلوار سرافرازان" في غرب مشهد، ويبعد أكثر من 15 كيلومترًا عن مرقد الإمام الرضا (ع).</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/naya_foriraq/82270" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇰🇵
كوريا الديمقراطية الشعبية العظمى : بيونغ يانغ قررت تعزيز قواتها النووية نوعيا وكميا</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/naya_foriraq/82269" target="_blank">📅 01:10 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
