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
<img src="https://cdn4.telesco.pe/file/Z_iIBA8Tzs3ynxtEJINwZHW3sR23xg6IbiNQDaQMzXb4QxYXHmm8wJVkEzvpC-pP4V4lu2Yb6BdAE3dK9oj-o4Ev9VqIIeT2Rar_nRGwNrZcY3wy_53c6ZcHOvi7OogE2mOboFTrcq6d0lm8DZcjPpFTchce3l0PFkbO-lUVH37zMTlKZwYoGXYifDipzX4cRnB8fRqc6_DIxakMcsMbFCyZd4DcqNtKyKK9RxoqtPSQJ6UJnS9AnS_CAmS0xI2rZmTon3alfwUnjNKT2wczm8I9iodMoSoTXRBm819UrVu6m07qjq6TCDQO5jVfw_QXX8Ug-jwSPJPv99PNRNongQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 16:01:22</div>
<hr>

<div class="tg-post" id="msg-90871">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">الرئيس الفرنسي:
نعمل لإنشاء خط أنابيب لنقل الغاز والنفط من العراق إلى السوق الأوروبي.</div>
<div class="tg-footer">👁️ 774 · <a href="https://t.me/naya_foriraq/90871" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90870">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9358732c7d.mp4?token=IcmCN1CwI0pTGkW1wwp5hFVNy1nD1sIGRbAP9w8zVuw5XdKiekHxzXBZMcdjP4hk_ak8UJmXrtwm-WvIAlA89uNo6qbhk_OLOClzr8ymxCNAYMefTAWcNjBu5Vd3eJif2R9iXQEYs3NZd03mrv_ZLo7rhoBXiFjXjubRQ1WaBtRHNXz3BITSG-vDw2CsMAh59bZf0v-LUx5l11Ki3cEzjypjrEclabns1J2c6jLLxfD_9plHO-bu6o9xYG2cBQ6_yLqU9cVhRpit2kOJQW0q7x-0Fv6r57-lrZsvuLGBQjZlZBGCUwkhMHl1-_5Ikg1yQ_ULq9ff4SZo6sQYvaxODg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9358732c7d.mp4?token=IcmCN1CwI0pTGkW1wwp5hFVNy1nD1sIGRbAP9w8zVuw5XdKiekHxzXBZMcdjP4hk_ak8UJmXrtwm-WvIAlA89uNo6qbhk_OLOClzr8ymxCNAYMefTAWcNjBu5Vd3eJif2R9iXQEYs3NZd03mrv_ZLo7rhoBXiFjXjubRQ1WaBtRHNXz3BITSG-vDw2CsMAh59bZf0v-LUx5l11Ki3cEzjypjrEclabns1J2c6jLLxfD_9plHO-bu6o9xYG2cBQ6_yLqU9cVhRpit2kOJQW0q7x-0Fv6r57-lrZsvuLGBQjZlZBGCUwkhMHl1-_5Ikg1yQ_ULq9ff4SZo6sQYvaxODg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتلى وجرحى في محافظة دير الزور السورية بانفجار هز بلدة عياش</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/naya_foriraq/90870" target="_blank">📅 15:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90869">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebNvvxhIxohgLt6NBDqMjD3SJCiv6CgA0uLBacVUloI9YzWb4sYgG1_cVSW4qnSBa4YWrdlyhO5W6hy2gjvHv3w7wu6d-OYfj6T8htMxvOpcnRgCku0uo8D5KWVsD3SaQWYnoJ3dXs42jjfixR9FPH16aRWEI4tEWTrNs9BaeLaqc-q3z1SyX0WN6k4KpJLBgKgc4bnF4Jh48C1n0YUpwyaaGYBH_vHaAMrApC8sZVHTD93t4ZcMqYmOtEs70baPhlM89eO2XGLPCppNEjwy8fZxT10TwDEPBGZQS2gAXjnoNvZ6RR5VYxtYTE_SJGONlXiC8sH-gmiYckaxeWh_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
‏السفير التركي في سوريا الجولاني يفتتح "مدرسة رجب طيب أردوغان التركية الدولية" في العاصمة السورية دمشق.
ورجعت أصالة عالشام
😂</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/naya_foriraq/90869" target="_blank">📅 15:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90868">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏
🇷🇺
🔵
ماكرون: استُهدفت فرنسا بهجمات روسية هجينة في الأسابيع القليلة الماضية</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/naya_foriraq/90868" target="_blank">📅 15:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90867">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be089790b.mp4?token=LXgbAp7ObVcE5So5HGqmEiYMWRpXQyTesVOv3fAkYG2-47mt1iHEZNTgy94QqchYb7Vz4Dr9VxA91sR0WCbIvlmQ189QLtJsxMGpsEa8pPYc2qeDD8Q2oyrYi6ATG-wv2NzsEMga63Nzbm7LgIntCEExMfUosQPO4cYTqpVVOEy4TlffNqvNu0R9zGlpYJ239e-Yr-2sSJL7mHguMDLALFL59HSQdsrIyR6YcOZNv15QpcNRTUJqcjOl3JmD5e5LBXAbzI01i-17Hdf2D0u8CcJzwyoacHCLqKv1gH4T5Fke3D2whgk1nedKuol-QDtewYZrb6bRMUH5Fhw4AVMtubvcTjYdBYEHMwhAF09al_O0wu7ybhUcgYxNUdbCzg-5tzPJaNSsnorFG4AGFjQf6YCzHxnTnrUN41NIkRw-34U0k5kIdX9SwfoJWy6Ai7f8mpHk1SQ1vzettzvX8kaSvNCT2w_25yaLfsX88JVTmaLwTFediid5yLfRdWQ_qwVXGNI7Q_tfzQbS1XEP35bBC-wAZ4bTQbwULb2SIcQPqfP13oFMZShAVeXR-DTWppCIDobDJd-kjgoVtwVhe6ARxAx5JmDZbcRrDRL-Bj_39z4UvNoLzxjVtjsN6-Bl446ei14ub1iX36v5TJ_au1LjDXta70ZvyY_YfmXsT2xUvrs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be089790b.mp4?token=LXgbAp7ObVcE5So5HGqmEiYMWRpXQyTesVOv3fAkYG2-47mt1iHEZNTgy94QqchYb7Vz4Dr9VxA91sR0WCbIvlmQ189QLtJsxMGpsEa8pPYc2qeDD8Q2oyrYi6ATG-wv2NzsEMga63Nzbm7LgIntCEExMfUosQPO4cYTqpVVOEy4TlffNqvNu0R9zGlpYJ239e-Yr-2sSJL7mHguMDLALFL59HSQdsrIyR6YcOZNv15QpcNRTUJqcjOl3JmD5e5LBXAbzI01i-17Hdf2D0u8CcJzwyoacHCLqKv1gH4T5Fke3D2whgk1nedKuol-QDtewYZrb6bRMUH5Fhw4AVMtubvcTjYdBYEHMwhAF09al_O0wu7ybhUcgYxNUdbCzg-5tzPJaNSsnorFG4AGFjQf6YCzHxnTnrUN41NIkRw-34U0k5kIdX9SwfoJWy6Ai7f8mpHk1SQ1vzettzvX8kaSvNCT2w_25yaLfsX88JVTmaLwTFediid5yLfRdWQ_qwVXGNI7Q_tfzQbS1XEP35bBC-wAZ4bTQbwULb2SIcQPqfP13oFMZShAVeXR-DTWppCIDobDJd-kjgoVtwVhe6ARxAx5JmDZbcRrDRL-Bj_39z4UvNoLzxjVtjsN6-Bl446ei14ub1iX36v5TJ_au1LjDXta70ZvyY_YfmXsT2xUvrs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
تلبية لدعوة السيد عبدالملك الحوثي.. حشود جماهيرية كبيرة في مدينة صعدة اليمنية تشارك في وقفة رافضة لمزاعم آل سعود حول الإعتداء على مكة المكرمة من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/naya_foriraq/90867" target="_blank">📅 15:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90866">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شركة أرامكو السعودية تبلغ مصافي النفط الأوروبية بأنها لن تتلقى أي شحنات من النفط الخام الشهر المقبل بعد تعرض خط أنابيب الشرق والغرب السعودي لأضرار</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/naya_foriraq/90866" target="_blank">📅 14:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90865">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxQSPuM3cH70RY98qJLT4HxDJwDo0nZyTLbg95kbyJePlMIAnvdFp0vys9jryb8ndGciXe_Cw1b04mq4K7b15GFi4E5Xs7XS_JKi9LZ3lwrQaIU40ut6obbww83BRfFXtROFqlMM6xZWifQUL3sGrVxULQmH7dqZtkdsTXMXWydKffLl-RwICj_gaNhsxR_GGh69ITE0gOWznyAlMUcODr-GJjBvSDpnf-jv7unHULSnRjOTucNRaaAJATYe7w0o_TZ8_IRs-z5J_42FnI8TqMr04w9njn6j_u6Bf9-uieg0CDWCmFgb2FYcInU8VmiFG1kp-XpnsbmNKFvaCILAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان فدا
شبه لهم يا حسين
ما طحت انت من ميمونك</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/naya_foriraq/90865" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90864">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
🇷🇺
وزارة الخارجية الروسية: روسيا تطالب اليابان بسحب صواريخ "تايفون" الأميركية من أراضيها</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/naya_foriraq/90864" target="_blank">📅 14:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90863">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0b95a2fe6.mp4?token=v1Rfo8Z7t3X8ObVXuJeGkuzPR_bzBYwg-vu4qkvzrBbGDgSHvaJm9IZzu0zqEGmGznQER0XJhmqEj1EQZGTRyL5yyKWotprAY4wFX3JPV4F5e2rTTCr3IU_j10Q2ajlRaEXJHtiAbsM3H6Gp4oMINRHagYkz3D9iMMg6V5EaRj5hpHHmNmotajulPFIt5iZSqKRAW1joVtw3hLl_-ewTaDIaTYvv5p6GQRlFENy401fhzzFTYInhRMoRnqZptK45UPKOU2MCUFCyc49qdy2TsbGd9X21Sv5PALfmlGLIaTQ7BSjnSSnVJFrV5jz0I9mLVM83VXdlafv1amzBHpMxDYi1VqiKfYHbSZsOFB9J7csYqmvFLNlVCyJMQqQwdrs86xHTIStPSQ7fH3mHSDa6gFvM_UTiC4tdLT4EZu6HCj513NupsrK4UR6H3dRmzUxmxCIQlLQaBeA1hSnY_16Z7uWD7JldEEk1bThjfV8DLZXRIeqkmWRlTdRcivVAs8XO5C5WdpWW18MXBSDvw3qrWmT3teuvasINmYG9LDe84E7QYX8ZVuj59IBiRHVeF4U_Zt_3TzAe3wEJCDkN9eWhEe7i2u4u8v5R6zVC4TTYdA86i0S_SJf-cOPymOxF30DnTeOh4Fw3GRCHd1lOedgbAlDk00VX1BMo5pdts0RWsT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0b95a2fe6.mp4?token=v1Rfo8Z7t3X8ObVXuJeGkuzPR_bzBYwg-vu4qkvzrBbGDgSHvaJm9IZzu0zqEGmGznQER0XJhmqEj1EQZGTRyL5yyKWotprAY4wFX3JPV4F5e2rTTCr3IU_j10Q2ajlRaEXJHtiAbsM3H6Gp4oMINRHagYkz3D9iMMg6V5EaRj5hpHHmNmotajulPFIt5iZSqKRAW1joVtw3hLl_-ewTaDIaTYvv5p6GQRlFENy401fhzzFTYInhRMoRnqZptK45UPKOU2MCUFCyc49qdy2TsbGd9X21Sv5PALfmlGLIaTQ7BSjnSSnVJFrV5jz0I9mLVM83VXdlafv1amzBHpMxDYi1VqiKfYHbSZsOFB9J7csYqmvFLNlVCyJMQqQwdrs86xHTIStPSQ7fH3mHSDa6gFvM_UTiC4tdLT4EZu6HCj513NupsrK4UR6H3dRmzUxmxCIQlLQaBeA1hSnY_16Z7uWD7JldEEk1bThjfV8DLZXRIeqkmWRlTdRcivVAs8XO5C5WdpWW18MXBSDvw3qrWmT3teuvasINmYG9LDe84E7QYX8ZVuj59IBiRHVeF4U_Zt_3TzAe3wEJCDkN9eWhEe7i2u4u8v5R6zVC4TTYdA86i0S_SJf-cOPymOxF30DnTeOh4Fw3GRCHd1lOedgbAlDk00VX1BMo5pdts0RWsT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇰
إنفجار داخل مسجد في باكستان؛ 17 قتيلا وعشرات المصابين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/90863" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90862">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇺🇸
سي إن إن:
‏الجيش الأمريكي ينقل طائرات بدون طيار إلى أمريكا الجنوبية استعدادًا لعمليات مكافحة التمرد المتوقعة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/90862" target="_blank">📅 12:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90861">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
هجوم بالرمانات اليدوية على منزل في العاصمة العراقية بغداد منطقة السيدية ..</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/90861" target="_blank">📅 12:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90860">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇾🇪
تلبية لدعوة السيد عبدالملك الحوثي..
حشود جماهيرية كبيرة في مدينة صعدة اليمنية تشارك في وقفة رافضة لمزاعم آل سعود حول الإعتداء على مكة المكرمة من قبل القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/90860" target="_blank">📅 11:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90859">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
وزير الدفاع الإيطالي:
إصابة طائرة تابعة للجيش الإيطالي خلال هجمات على قاعدة جوية في مدينة الطائف السعودية.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/90859" target="_blank">📅 11:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90858">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROYwEqtnQC_tMBdRPRqBbslkZ8T8dbf2BnYvEOFN5jnV0VdGYv2iSiVmvaxwm9nldCCaa2cVlzUoYTy5-Xvo7GPeaHm_Ib_0QXaOCXcHyCBT9enwrihYsLhb0sf5tMpb42Qem70gLmgPVu3KELgmGotFSq9NWDucji1xh_jbJIBhBaI2rW14swhULoD4AsUCc0dS4LvSDz5ImQQf2VQiJfk_flG5YCqRTZU2v6GzuS21UGsy6rwBsIxnaOYiaiBXfpZALYjPD86TnvwifNDCT1o7t8s4rC-Mx-3-x88j46jcQTMX7nA24t1IoNgc-yTIERUfW6byA0qtA0P9sbNauw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
إستهداف ناقلة نفط بمقذوف حربي في مضيق هرمز، أدى إلى اندلاع حريق كبير فيها.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90858" target="_blank">📅 11:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90857">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvJ7lEUy5aPTx4GcFEW4LSssWKV9S-vKbB5oDXdsgVMkCScNKBbLmgldWqmiJb8nhe0Rqt7-I5zRlcZXl2RtO46Y2rfNF4rNOKXrvJ7J8E5Xwcig97nFEc2S4OFGBDk9-Jla571mGbtiFG4m6SXrVAfCRlbezfmlwx7TZAdPiaPtIQrbpdYIgy6_AiIZjJNEeCCzLl_vToPfeymi6B4E6xsPfESzNaXpLjodnu9i40J9FMS2_fM5vyIHzdnKUHVCiD1Ol1JshFJ_d-awPVNPvxOwuJvLNjjCeJGQFp2-5fN5sgoNkk26h5jFTMKFunW0n6ilBKklkX5cAAc_SCJZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/90857" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90856">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/90856" target="_blank">📅 10:49 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90855">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇱
إعلام العدو:
الشاباك والشرطة أوقفا مواطنًا عربيًا إسرائيليًا من سكان مجد الكروم للاشتباه بارتكابه مخالفات أمنية تتعلق بالتواصل مع عميل أجنبي من لبنان.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/90855" target="_blank">📅 10:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90854">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c3faab547.mp4?token=FYZBN50DQbjOzVt1VqpXTbrx6uto1fFAPc4NYl3sNcvdIKz1oz03Ro9Sc8DS3UV9H-1F4YO50rFjdjZoD3qSMW2RbLMpk2aobuy9QTPz34YD8NKhav7gKWvEyMZcCtxY_LITXSG3EpQR3GYSsVpIYnpcm8Lw0TDieV9pZmQegA0WuNou3ljLSjzXpyZ0DAcDkY7P9GCmISph62nWMIfMdehcTN8-m6gfDUwSX4iV4a52Yko1FB3TDwjMJOw2MBsUjZsHUvNeWUuv2V7qixDxoOdmPGpvOqEQR53GXyZSzORs_giMDcZm3QHClximWeppJjbtTmqB--rflmEBrPMNaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c3faab547.mp4?token=FYZBN50DQbjOzVt1VqpXTbrx6uto1fFAPc4NYl3sNcvdIKz1oz03Ro9Sc8DS3UV9H-1F4YO50rFjdjZoD3qSMW2RbLMpk2aobuy9QTPz34YD8NKhav7gKWvEyMZcCtxY_LITXSG3EpQR3GYSsVpIYnpcm8Lw0TDieV9pZmQegA0WuNou3ljLSjzXpyZ0DAcDkY7P9GCmISph62nWMIfMdehcTN8-m6gfDUwSX4iV4a52Yko1FB3TDwjMJOw2MBsUjZsHUvNeWUuv2V7qixDxoOdmPGpvOqEQR53GXyZSzORs_giMDcZm3QHClximWeppJjbtTmqB--rflmEBrPMNaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
مشاهد تظهر إقتحام وزير الأمن القومي الصهيوني "بن غفير" لحائط البراق غربي المسجد الأقصى الليلة الماضية، حيث أدى طقوساً تلمودية برفقة عشرات المستوطنين الصهاينة.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/90854" target="_blank">📅 10:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90853">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d614117ed.mp4?token=OohfE5vZjLTm0jURWeAGcz4J1y95WZzwwmrNLUzSvv-pr95qbXO4C0zrKpyoa7-0flycpXu1WnP2wG5aLb836A2mdqiZYYB2Eb_1YSW9qvd2g28vzBPGaArGepXwUc_CkcIfKF6wmsKM2HUn7rYoTc_F1_K3IOM_sq0SkZ-mFA8r2wx2fY313JxiMLP-OdhcSIHqFk0ZMAFNOFi5U8kzSenqYGBEstJYt23jLXGMaybTEr9mKy5RnQVMWTmTVVgRdRgYaCo4WP1B_XtuVycndkkzx__jN_fEpRKQcaXFAkhTpU8rpSoRro-i9ZkxYxL8_DZ5JOZ2H_sWsf6Eskv_eBjB3s0GF1Vuq9u-nibYJ1dX5kOLIB9VFs9tAq42k3vbGhMOFkFnJvJhkpX7zyaFIs8neCx8t7UwMQoZ88bYCdg36W6DF9o9aQ-Kox6w84WzFWW48rfoSyRIpZ-LQKIypvqcQr7dGV5MsKoUk3_jgtUgaB9FssdqJUAKXwr-AhtylbGXaYbdAJummEc1WZRqPJubjlaDxwzCGFqq5i8PwjoUacKQBHnmddHZG9cBaZKLQnAgRQ7OGiYilZvySZgXH249dSBv4_RPAbMMVwTiRqcGVJGvFw58AaNtWwZm7vTzUArDwMigEJNe8FLvPJi4svYLMLMkWwuEqqHdkK3PXps" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d614117ed.mp4?token=OohfE5vZjLTm0jURWeAGcz4J1y95WZzwwmrNLUzSvv-pr95qbXO4C0zrKpyoa7-0flycpXu1WnP2wG5aLb836A2mdqiZYYB2Eb_1YSW9qvd2g28vzBPGaArGepXwUc_CkcIfKF6wmsKM2HUn7rYoTc_F1_K3IOM_sq0SkZ-mFA8r2wx2fY313JxiMLP-OdhcSIHqFk0ZMAFNOFi5U8kzSenqYGBEstJYt23jLXGMaybTEr9mKy5RnQVMWTmTVVgRdRgYaCo4WP1B_XtuVycndkkzx__jN_fEpRKQcaXFAkhTpU8rpSoRro-i9ZkxYxL8_DZ5JOZ2H_sWsf6Eskv_eBjB3s0GF1Vuq9u-nibYJ1dX5kOLIB9VFs9tAq42k3vbGhMOFkFnJvJhkpX7zyaFIs8neCx8t7UwMQoZ88bYCdg36W6DF9o9aQ-Kox6w84WzFWW48rfoSyRIpZ-LQKIypvqcQr7dGV5MsKoUk3_jgtUgaB9FssdqJUAKXwr-AhtylbGXaYbdAJummEc1WZRqPJubjlaDxwzCGFqq5i8PwjoUacKQBHnmddHZG9cBaZKLQnAgRQ7OGiYilZvySZgXH249dSBv4_RPAbMMVwTiRqcGVJGvFw58AaNtWwZm7vTzUArDwMigEJNe8FLvPJi4svYLMLMkWwuEqqHdkK3PXps" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حضور الرئيس الإيراني مسعود بزشكيان في مناورات "فدائيون إيران" العسكرية بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/90853" target="_blank">📅 10:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90850">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64e7763e61.mp4?token=vElBuThBekOqlKd2hihEb9WjlgYKuQKEFvzX1orI8X94eRXKT-83xbmqlX9tzuktbkkaQF0ma5fNB50k6kGwag5G7sBV7LGbYbE1yVkTieOFWll0A-Yf6ZbJcWKlrlnXsONZwrQzLpiDhz82ViYWVVWT8JEOU1hufXZzjfy5v8pwQiVyLbMS2pVBSMjGRHApR95oCOj7pERB0g-g1mQ5OjkI5NTQRBGRSAs8KnygcOvMuKRyBkBP_k0GXuFzU6kjZoSSu_qvkilXMdXk8dfNMi8fWA0s8yQiRxAC6qmMsDF8TQXr2qBl9HmYhh44Z6sT-4jLZ07kfVBi5lfb1UPeqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64e7763e61.mp4?token=vElBuThBekOqlKd2hihEb9WjlgYKuQKEFvzX1orI8X94eRXKT-83xbmqlX9tzuktbkkaQF0ma5fNB50k6kGwag5G7sBV7LGbYbE1yVkTieOFWll0A-Yf6ZbJcWKlrlnXsONZwrQzLpiDhz82ViYWVVWT8JEOU1hufXZzjfy5v8pwQiVyLbMS2pVBSMjGRHApR95oCOj7pERB0g-g1mQ5OjkI5NTQRBGRSAs8KnygcOvMuKRyBkBP_k0GXuFzU6kjZoSSu_qvkilXMdXk8dfNMi8fWA0s8yQiRxAC6qmMsDF8TQXr2qBl9HmYhh44Z6sT-4jLZ07kfVBi5lfb1UPeqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تقيم الجمهورية الإسلامية الإيرانية مناورات "فدائيين إيران" وبحضور 313 ألف عنصر في العاصمة طهران وبشعار "لبیک یا خامنئي".</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90850" target="_blank">📅 09:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">قوات عسكرية من عامة الشعب تبدأ مناوراتها في عدة مدن ايرانية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90849" target="_blank">📅 08:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517cb8fa6a.mp4?token=T4tVtOV-kUD01l1bxtUYXpnMKnB5Mtvz8CmQ3wJK4E6i94RGeABdGQ2wv5uiXBCcJm78eTE1-cB8h4jayfMSVz8JVuEtHhTaGyZ-ia_zR5SuyMRyglu_s4VPBlQO3PL-bFKnK5GqPZGMarE2qhs5bCyNEDbRp8R4BYhTea_wsZsWBgIBGXg_NxNqvlASOaqdxmH7ywTy4tDYFe5WMPy02CjmL2j6veNR1F91cHtQJGyEdNBnLthzLu9UxlyBzE92b9AS4lzqMwT1b5piRPn-SoBkyliF5uDFPKdBYWN2XvD6BFdPKRMZsuyYLkJ59KyN79o6dFBbXQct21hzhboTGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517cb8fa6a.mp4?token=T4tVtOV-kUD01l1bxtUYXpnMKnB5Mtvz8CmQ3wJK4E6i94RGeABdGQ2wv5uiXBCcJm78eTE1-cB8h4jayfMSVz8JVuEtHhTaGyZ-ia_zR5SuyMRyglu_s4VPBlQO3PL-bFKnK5GqPZGMarE2qhs5bCyNEDbRp8R4BYhTea_wsZsWBgIBGXg_NxNqvlASOaqdxmH7ywTy4tDYFe5WMPy02CjmL2j6veNR1F91cHtQJGyEdNBnLthzLu9UxlyBzE92b9AS4lzqMwT1b5piRPn-SoBkyliF5uDFPKdBYWN2XvD6BFdPKRMZsuyYLkJ59KyN79o6dFBbXQct21hzhboTGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إيران تريد عقد صفقة؛ لكنها ليست مستعدة، في رأيي. إما أن نعقد صفقة جيدة، أو لن نعقد صفقة على الإطلاق."</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/90848" target="_blank">📅 02:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نايا - NAYA
pinned «
إِذْ يُوحِي رَبُّكَ إِلَى الْمَلَائِكَةِ أَنِّي مَعَكُمْ فَثَبِّتُوا الَّذِينَ آمَنُوا ۚ سَأُلْقِي فِي قُلُوبِ الَّذِينَ كَفَرُوا الرُّعْبَ
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/90847" target="_blank">📅 02:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90846">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">إِذْ يُوحِي رَبُّكَ إِلَى الْمَلَائِكَةِ أَنِّي مَعَكُمْ فَثَبِّتُوا الَّذِينَ آمَنُوا ۚ سَأُلْقِي فِي قُلُوبِ الَّذِينَ كَفَرُوا الرُّعْبَ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/90846" target="_blank">📅 02:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90845">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تفعيل الدفاعات الجوية في مدينة جدة السعودية</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/90845" target="_blank">📅 01:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90844">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwcJ8ddnCn4fTkBEOR6Q_E_zY2hVqWBEFGxpGnUvte1sLAo7yYqlES8D1rdTKbQl1iM6OoB4Af7bzJfH8ftJlKbUgZjtsfaP30UiS4Ef1ZwPH5JeX6c5Kea3HuzAaL5T6071xwvqXvEJGct72RHL6_WyHO0LeLkEvTDGTfPMjIQzYCeOp1QdLxtKqsXFiJCaYXJnoOwd62SkUfaG3TIO2hV-FBE3WdLq_ngZ4OBVpm9D2boRoPTlJyixX6p1sb-oRn4OO93lkVcGiaXTiDyHt7ELWiHBIZ5LU4atabgshpG9L2BU4whWVWrPs-Jiyw4plAb6Wb38zyTHbz3ID7aLNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
الانسحاب المذل للقوات الأمريكية من محافظات اقليم كوردستان العراق مروراً بمدينة البغدادي بأتجاه سريع الأنبار الأردن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/90844" target="_blank">📅 01:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90843">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3ee316d91.mp4?token=S2LQNJRc4u-UjtrYNHsa4qLW1k2WaGKGms3sbsvF9AB476pFEek1kE-hhlNjSkiLVD9oRcVxqJNdH3uW0kBmv59NEJwYQWHWpB71GWXv161WC61UcFXROZjtc26XAaHZJtbQT5TSeUO-EfmZsePLu1BjtzZ1gwIqDxIUsQQ4k4t6oVlhPNd15pW1nYxesmSfi0pAytkzaThtsvWtkwAvkLcZx1KQGP1bBWZUGfkooLnkEBahx-S-T7weaOtVy0yhVmE9oFETbegNJnVFE1X4OsD-u0mPdpFmaPXiXX0xLQ0U71B5pFEaNWvNpmDQ-7Y4cvnLzBGfn2Ij5jUnrD-PLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3ee316d91.mp4?token=S2LQNJRc4u-UjtrYNHsa4qLW1k2WaGKGms3sbsvF9AB476pFEek1kE-hhlNjSkiLVD9oRcVxqJNdH3uW0kBmv59NEJwYQWHWpB71GWXv161WC61UcFXROZjtc26XAaHZJtbQT5TSeUO-EfmZsePLu1BjtzZ1gwIqDxIUsQQ4k4t6oVlhPNd15pW1nYxesmSfi0pAytkzaThtsvWtkwAvkLcZx1KQGP1bBWZUGfkooLnkEBahx-S-T7weaOtVy0yhVmE9oFETbegNJnVFE1X4OsD-u0mPdpFmaPXiXX0xLQ0U71B5pFEaNWvNpmDQ-7Y4cvnLzBGfn2Ij5jUnrD-PLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بين ياسر المالكي وقاسم عطا المكصوصي من سيختار تيار الحكمة الوطني وزيرا للداخلية العراقية ؟</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/90843" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90842">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وزارة الدفاع الأمريكية : خلال فترة ترامب، تدرس خططًا لسحب الطائرات والسفن والأسلحة وأكثر من 25 ألف جندي أمريكي من أوروبا.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/90842" target="_blank">📅 00:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un4ADKrh1gy715XKacikjVf0vPNoV_JBhAin09fEb4ohCciwD_B_jc1tjQlrIkK6v6n7BE9YFIUTiEP0dfbVDTtBdU5TAmZO9GfnQr_idESQZBzdMjPSahpFVDVHzPv7Jx0myDoKkcfwQ2oZWxeoJ2_p4U2H3SSIkrmxcomK2d774p4uNqMEwAgHqmzBMZ2CuwAJWdKKy4y_2l2MwnOX9zBmt9LjQ6J7gfSlNUncdbZEvsfJ9saRemHA58hvvNm6MQ6rFQiU9QSlca0usYXqzc7-cddOoqyaWyAwy4Bhq3Dfl8t1MHILjQ-__mzOi7UrSwq2YYVbeBRckCqdmE-WIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر صور الأقمار الصناعية لاندسات 8-9 الملتقطة اليوم أضرارًا إضافية محتملة في محطة أبها لتخزين النفط الخام جنوب غرب المملكة العربية السعودية، وذلك في أعقاب هجمات الحوثيين هذا الأسبوع. ويبدو أن ما تبقى من خزانات تخزين النفط في المحطة قد تعرض للهجوم والتدمير.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90841" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90840">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kByKmKegOk66liXDrcbXoMxKsIJjNmKtPzA6IdJmQ49kMVgEQxUz2Ripyf9-A0xNUBx-oDATYyavQfQOfev5ADsDmZE17OI-RlqgeL5ZceRS4rImmmEypOyqB8zpyac3DXano5qavXT0L_jUh9gaIhsE67_0AUHmk_kNWo8X37mnPHh_0_8MnYRXgz7S1vjCTaLStNLETGBL1aS0_wvBdy8GCr8ponjrW2une84e04VwbzPX0RsuvLHtICsgW1Y7H5N9MrcGcJPMXeikCPycD7WI4_aM0KHGg2uTGIMLt3PvA5y5mrExj2IZl3qbD8v5WnSP4FTaSgEOEDw5ldszEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر
استهداف سفينة في مضيق هرمز</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/90840" target="_blank">📅 23:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90839">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvnCW7WWFMX2D66MCLSNXIp-KoD5gFEDA9J2X_slYAp4ZCKT7p8Xo8Fats6lO7IAlCHJz8yPD-3aMHOgo8Lm8rkNGJ1ksvLygz0CSAAVYR2SgFJJzFvTxAU2eZSUO_NRGFwIB_ezBW_al_73Bh3EpvLFLECnX6FlmdYKEl_OIk-Pwynq6w28Nn8n-o2wkI2k5gb-R4wnBhb1ehe4LMBXhS9C7ad7bxgjnmodubHHpoDcfbQOoRmHcDBflUqVqNbajtzwrCt6Y41hsnVOMOcef2X4uuJn0LLfWwWWkOLnAU5oXAHIl_Gv3nbVhb3g5UaQG0PN3iBJbSqRF9qqPUQcDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
: ‏انتهى النظام الأحادي القطب الذي ينتزع فيه طرف واحد التنازلات بالقوة والإكراه. وقد رفضت الصين وروسيا، باستخدام حق النقض (الفيتو)، الاستغلال السياسي لمجلس الأمن، وأكدتا سيادة القانون. يجب علينا الدفاع عن التعددية؛ فالأحادية لا تخدم مصالح أحد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90839" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90838">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90838" target="_blank">📅 22:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90837">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/90837" target="_blank">📅 22:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90836">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu6MtomqVP3RaLE7qKzugu1-UpA2LvxU87CT9InPNF7YwscGPCyR0EJS-VdCtC56B9GMD_6fQkaSGk2OlZv_wmF49jYZ9ocU3ek2BgsEtWhHiTmQOYPp1GRAsMb-zCOzLuaKEm8U8HNu57jivuEyWocW5OfBOIUiaJNfkhTsY0QK5MUjhUgjsgAPWKyL6Zc8zSVSbmA42ZhU-FxNebSyUCmVRb24vSmMy7aL4lvS2bIs5NnVSqx5MUJRi6BErvtj29xmEUYD2tS6BtaaEfTrf7on6l1hlXR2cfic-ih8621xsfAac2gRIoU32kByiBh_3pvKf3vafIRVO18dXXTlow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
وردت أنباء أولية الآن عن تحطم طائرة من طراز إف-16 في مقاطعة بلير بولاية ميشيغان.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/90836" target="_blank">📅 22:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
🇮🇷
الخارجية الاميركية:
واشنطن تمنح تأشيرات دخول لإيران لحضور اجتماعات الأمم المتحدة .</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90835" target="_blank">📅 22:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
‏شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 37 غارة جوية بطائرات نوع "F15" أقلعت من قاعدة خميس مشيط الجوية واستهدفت محافظات تعز وحجة وخلفت شهداء وجرحى من المدنيين.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/90834" target="_blank">📅 22:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90833">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇶
🇨🇳
حادث سير عنيف في محافظة ذي قار اصابة اكثر من ٨ افراد بينهم افراد من الجنسية الصينية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/90833" target="_blank">📅 22:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90832">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇸🇦
🇾🇪
طيران العدو السعودي يغير على المدنيين في محافظة تعز.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/90832" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90831">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇸🇦
المعارضة السعودية تنشر:
سَنْطِيح مَلْكُكُمْ وَكُلُّ حصونِكُمْ.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/90831" target="_blank">📅 21:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90830">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امريكا تفرض عقوبات على منصة بتبانك للعملات الرقمية بتهمة العمل مع ايران
وعقوبات إضافية على كوبا</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/90830" target="_blank">📅 21:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90829">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b77cfc018.mp4?token=JRYrIsZkhAMWelBmXRCg81gZDv7n6-NgezDED0y_8wQ-_F5wnFWhhX8ZBxWxeQx35-Dcv3u3Wphx1je5P3ly4LHUmFF-g2XqyP75X7MpyHz1h5g3f0ae3hJkDjbimr-AsQ0H5uWeu8tKA3Ri1AocKyMqm2oodaVYSmPQLYukm4HOhgSQ2hQVa8jY6GWZrJhxB5MjeMPptuAFHZC_2FYJztEiLigZUDr_llwE3jwwN3lXaCqlpJvblrb5BenwWKY_hvQiXVyvDHlvNVrQhb3P7e2hp5RdxUvVTiSqnM9XdMH6XCIFEB0FYEXDBV9GFR9vHy_3V28aWxzOcVkxf2ma-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b77cfc018.mp4?token=JRYrIsZkhAMWelBmXRCg81gZDv7n6-NgezDED0y_8wQ-_F5wnFWhhX8ZBxWxeQx35-Dcv3u3Wphx1je5P3ly4LHUmFF-g2XqyP75X7MpyHz1h5g3f0ae3hJkDjbimr-AsQ0H5uWeu8tKA3Ri1AocKyMqm2oodaVYSmPQLYukm4HOhgSQ2hQVa8jY6GWZrJhxB5MjeMPptuAFHZC_2FYJztEiLigZUDr_llwE3jwwN3lXaCqlpJvblrb5BenwWKY_hvQiXVyvDHlvNVrQhb3P7e2hp5RdxUvVTiSqnM9XdMH6XCIFEB0FYEXDBV9GFR9vHy_3V28aWxzOcVkxf2ma-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇸🇦
‏الخارجية الأميركية: صفقة بيع مقاتلات إف 35 لايتنينغ 2 للسعودية تقدر بـ 24.3 مليار دولار</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90829" target="_blank">📅 21:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90828">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6c6c51e3.mp4?token=YeuSbIKA_OFwMPX7sbYg_TExl586L72q8fv0vDjkxM3aLg7w6u8UmATX9dPodnbbTAFpBIV4mM2UyD3ROV0ZVy2bcUfdUHuduIe31c8tpzyLDkZRlgvy5HS2MBUOmw3pPyyUtlCqeB8aj7gSlL-BExbTWUYAPl4O9v31uxGxor8ASgOYWHZCN7krNerOh3_bwAVOORxrICRcTXV6W_eIUVm4ChXrWoZoMV5VdyzomiirMEzbHc9cuv9sWmBCGHwDNu1ylTrP_4p7CeM1DbQTZqHNuRgb-pjVH2Hck41ErO8kv0fgMsDeLCRa3oYKTGzphHvkBwDZj7xC2OXKDZHbaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6c6c51e3.mp4?token=YeuSbIKA_OFwMPX7sbYg_TExl586L72q8fv0vDjkxM3aLg7w6u8UmATX9dPodnbbTAFpBIV4mM2UyD3ROV0ZVy2bcUfdUHuduIe31c8tpzyLDkZRlgvy5HS2MBUOmw3pPyyUtlCqeB8aj7gSlL-BExbTWUYAPl4O9v31uxGxor8ASgOYWHZCN7krNerOh3_bwAVOORxrICRcTXV6W_eIUVm4ChXrWoZoMV5VdyzomiirMEzbHc9cuv9sWmBCGHwDNu1ylTrP_4p7CeM1DbQTZqHNuRgb-pjVH2Hck41ErO8kv0fgMsDeLCRa3oYKTGzphHvkBwDZj7xC2OXKDZHbaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
إصابة سفينة الشحن التركية «ماريام إم» بمسيّرة روسية في قناة دلتا الدانوب داخل الأراضي الأوكرانية قرب الحدود الرومانية.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90828" target="_blank">📅 20:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90827">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QII8cjcyWw-0S4SueRWL-iauJLqQQin_1m85Ga38QVBiXEW58eGFrhmEplex_WeWa5bDagpjhbJPn93jfyDwaT1e8Y2BXKXETOhJ2qscWu7K0VlMopAEG3JFvj6pZvqJIGvXfJWokNogWRWuzurAChAkwl0thIhAr1r3OmH_AAOR5NSWNlLxhsYpajbpXCSivTgpusWt5Vb4XcmcbtzBgxxgIHvTGd9WhIYXBIfSlpeD8FJj1dJEJAI1cm1WXvwHVWBR4YpbYNIQoieGATSwi2F52iZQZKxGb-QMNUSe3eKg76Hkyn4vNJGA9zNDXBsTDYnDO41Re6UYxFO6AZ_MiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
أخبار رائعة! بفضل القيادة الجريئة لصديقي كارول ناوروكي، رئيس بولندا، يتم إحراز تقدم كبير نحو إنشاء الولايات المتحدة.
قاعدة الجيش في بولندا. إذا حدث هذا، فسيتم الإعلان عن الموقع قريبا جدا. ستكون هذه خطوة تاريخية للولايات المتحدة العظمى. /التحالف البولندي.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90827" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90826">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
🇸🇦
‏
الخارجية الأميركية:
صفقة بيع مقاتلات إف 35 لايتنينغ 2 للسعودية تقدر بـ 24.3 مليار دولار</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90826" target="_blank">📅 20:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90825">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gL1VHqpXEEWCRfJl8wzAROTZp40qAaTpLbqUs0HLN5k7eTVP0YAImNVjveWuP0zIEsyRxF7O433hJE7s9wU1k4cAKzqtkIhoxcxkFhEUbsVvbgry2cw8jToh4s-vpKrJFEBTXx0MBk5tXPw3z9TGIilpZb_zfU0ZydYUk4tlEH-b0j-dN791n3rXQ9-iwFWTgrzyhNQOcMvTJ8wb8kVHKGYA6yhUZT1kA40ohERYnISjTCpB7Ggq7azMqUJDDw3Cinb3TqcnlCAzBcqTXwnhw56mX8QRJqyZwdF-ZyVnKPkgt8z_SDUnZVNOdtzDYSXnirFHGJ3oUEx0IaWrUe4Yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
آیا ایمان لازم برای انجام این کار رو دارید؟
@Naya_Press</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90825" target="_blank">📅 20:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90824">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇶
متحدث باسم الحكومة العراقية:
رئيس الوزراء سيذهب إلى الولايات المتحدة الأسبوع المقبل.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/90824" target="_blank">📅 20:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90823">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران: لدي قرار كبير قادم، أنا اقترب من منعطف كبير في الحرب مع إيران.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/90823" target="_blank">📅 20:36 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90822">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب حول إيران:
لدي قرار كبير قادم، أنا اقترب من منعطف كبير في الحرب مع إيران.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90822" target="_blank">📅 20:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90821">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597f82b7a4.mp4?token=HdPPGsLR8lBsDjzIb3didhuw3e7sAUe31714lSjyWB2ngMqnF_ljlhcfcN_d0Jpwr6J8Knm3qURjxDj69PmtL5GpKat1tb5GYsKvxnrsvDQHaj1US-FvpowZ4uvKPaCFmW4Bx5GAKCmPSU5qeuD_kPc469RN9zjsYVxGWXzdZXVgK-0hUdD-RQEy3TovTEqAu9VwZReeuDZL44RPPHSzdKYUS-9HbJHZ4dUmi2tUoGROpiqF9JmbOv3R86_78_MwLxQ3MIpilwCh0EXzTmb8CtBEOLhJNWRYScsGbvoc87FD8YgWJHO9in0RgTpml7H0nYuuFp4yD1kO2DmbfF6k4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597f82b7a4.mp4?token=HdPPGsLR8lBsDjzIb3didhuw3e7sAUe31714lSjyWB2ngMqnF_ljlhcfcN_d0Jpwr6J8Knm3qURjxDj69PmtL5GpKat1tb5GYsKvxnrsvDQHaj1US-FvpowZ4uvKPaCFmW4Bx5GAKCmPSU5qeuD_kPc469RN9zjsYVxGWXzdZXVgK-0hUdD-RQEy3TovTEqAu9VwZReeuDZL44RPPHSzdKYUS-9HbJHZ4dUmi2tUoGROpiqF9JmbOv3R86_78_MwLxQ3MIpilwCh0EXzTmb8CtBEOLhJNWRYScsGbvoc87FD8YgWJHO9in0RgTpml7H0nYuuFp4yD1kO2DmbfF6k4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏المندوب السوري في مجلس الأمن: إسرائيل قابلت رغبتنا في السلام والدبلوماسية بالقصف والتوغلات
القدس تنتظرنا يا اخوان</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/90821" target="_blank">📅 20:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90820">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">إعلام صهيوني : إسقاط طائرة مسيرة تابعة لسلاح الجو الإسرائيلي في البحر قبالة شاطئ بالماتشيم</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90820" target="_blank">📅 20:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90819">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اندلاع حريق داخل مبنى وزارة الداخلية العراقية
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90819" target="_blank">📅 20:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90818">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قوات عسكرية من عامة الشعب تبدأ مناوراتها في عدة مدن ايرانية</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/90818" target="_blank">📅 19:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90817">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQIjT3jByE-W3EKnrHIHhXTrQ4NtzKMTxTlOQ_AckAzsJymT5c-aR3fqD2BbF43xEl83id3Kzx9w55mW2V7J1B0KZfu-jQBd0pQBqamU0cszG0pu2RRbIr6rcRTMptHUrzWSOAwXPh3CM2jelLzYjjRuvsHGStQ4l7bMLAVdK-7kJFlTXU8EA6fQ9AZ1-2pOT5761Ls3emaGePOv-42uv5i-WJUv9a_nUIBhGipgoDQYc1IWmDf_I8fXV12d1Txnb9SjtD-fmmq5LpKbmbEMbuk4xqL3WyPgu4pXDEc3wPKx3A0BCdxN46dkMLWs7H8dFko6ZbYvWW3mUFPHi_FIvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة معتدية قرب عدن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/90817" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90816">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90816" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90815">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇸🇦
الاعلام الغربي:
تضررت ثلاث محطات ضخ على طول خط أنابيب النفط الذي يمتد من الشرق إلى الغرب في المملكة العربية السعودية، في هجوم وقع الأسبوع الماضي.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90815" target="_blank">📅 19:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90814">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdAJ1kjoMjPPP1l_BUrtSzndrSZRQTV6_Jk3N2No0byvPeQ5JyTfJbcZrL_HIpPHPzGSUXcxM8gJjjkb1WIS5fADpZOp-AratD-3TxoPxHQIFssXebhNMAKEt-6_OR8nZRpkS7GIG_u7gb0fNFFej_6xhCPsTy4byhejkU60WkhzMG76zJArdc_M2gIOkroWTrR6jQ4sDegzVh7YIJRTONeU3HR5egFL8JcYVaCC7ffJ5Rbcr3W0hV7QHfhmiajcdkca4DbOs52HDLLTWUXNZYQgyBoFfNA5h6oLWTezUVhLqzxoXVfJ_4gnrQlaRPbIWscpAm6Vmr_Qdkn_TQYWQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇮🇶
السفير الروسي يغادر العاصمة بغداد قريبا ..</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/90814" target="_blank">📅 18:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90813">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">السيد الحوثي: لن نسكت على البهتان السعودي وادعو شعبنا للخروج يوم غد في صنعاء والمحافظات للدفاع عن شرفه الاسلامي</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/90813" target="_blank">📅 18:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90812">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">السيد الحوثي: هناك تبعات شرعية وقانونية لهذا البهتان تجاه شعبنا ولذلك نحتفظ بحقنا في الرد على هذا الظلم والاساءة</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/90812" target="_blank">📅 18:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90811">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
وزارة الخارجية الإيرانية:
استدعاء السفير الألماني في طهران على خلفية تصريحات مسؤولين ألمان ضد إيران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90811" target="_blank">📅 18:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90810">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">السيد الحوثي: الانظمة التي تلقفت البهتان السعودي يتحملون مع السعودي جنبا الى جنب كامل المسؤولية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/90810" target="_blank">📅 18:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90809">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">السيد الحوثي: كل من ادان البهتان السعودي باستهداف مكة المكرمة هو شريك في العار. انها اساءة لشعبنا</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/90809" target="_blank">📅 18:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90807">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">السيد الحوثي: نحن كشعب يمني أنفسنا وأرواحنا وحياتنا وأموالنا وما نملك فداءً لمكة المكرمة فداءً للمقدسات الإسلامية بكلها.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90807" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">السيد الحوثي: قارون العصر السعودي المفتري يحمل راية هذا البهتان ضد شعبنا وهو قرن الشيطان ومنبع الزلازل والفتن.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90806" target="_blank">📅 17:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">السيد الحوثي يدعو الشعوب الاسلامية لرفض استخدام مكة المكرمة من قبل ال سعود لخدمة عدوانهم الظالم على الشعب اليمني.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90805" target="_blank">📅 17:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">السيد الحوثي: العدو السعودي يسعى لحرب مباشرة تدخل فيها كل الاطراف الاقليمية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90804" target="_blank">📅 17:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90803">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مجلس الأمن الدولي يعقد اجتماعاً ويصوّت على فرض عقوبات على إيران.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90803" target="_blank">📅 17:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90802">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">السيد الحوثي: استهداف مكة المكرمة كذبة كبرى وقبيحة وشنيعة للغاية كررها العدو السعودي عسى ان تلقى بعض الرواج.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90802" target="_blank">📅 17:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90801">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">السيد الحوثي: المعتدي السعودي استهدف في بلدنا كل شيء ولم يرع أي حرمة على الإطلاق</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90801" target="_blank">📅 17:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90800">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انباء اولية عن انفجار دراجة مفخخة استهدفت مركزا أمنيا في العاصمة اليمنية صنعاء</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90800" target="_blank">📅 17:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90799">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مجلس الأمن الدولي يعقد اجتماعاً ويصوّت على فرض عقوبات على إيران.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90799" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90798">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">السيد الحوثي: شعبنا العزيز لم يقبل مصادرة حقوقه وتصدى للعدوان ولم يهاجم سوى القواعد العسكرية والثروة النفطية السعودية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90798" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90797">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">السيد الحوثي: العدو السعودي يتصور ان قوته واستقراره وتحقيقه لطموحاته يكون بوضع شعبنا ضعيف ومستعبد ومقهورا تصادر حريته ويصادر استقراره ومشتت ومتفرقا</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90797" target="_blank">📅 17:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90796">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">السيد الحوثي: العدو السعودي ينفذ عدوانه على اليمن بدعم امريكي واشراف اسرائيلي</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90796" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90795">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">السيد الحوثي يبارك للشعب اليمني انتصاراته</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/90795" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90794">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بدأ كلمة المرگض ال سعود السيد الحوثي</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90794" target="_blank">📅 17:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90793">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">الكلمة بعد دقائق عند الساعة 4:45م</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90793" target="_blank">📅 17:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90792">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">كلمة مرتقبة للسيد القائد عبدالملك بدرالدين الحوثي حول آخر التطورات والمستجدات</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90792" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90791">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/90791" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قولو له الرياض اقرب</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90791" target="_blank">📅 16:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90790">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/os1-A0eE2TE3Fqfm38TfMyLD5DLgIV21HfooET_oep_2GNNdICyc_wC-udtdC6hy6izLBFt-12N2DBDc86vXVZ4t2bN7X68FU5ejawAOswCY53FAgrn-Nm9JEhiiB_jPR5ooPbBnIdqWFOVMberRqESMjt2TFMQ0AJEVHIKXFq3fUTL_f_BsOjVTTquYb_ebvWPCaK_OoqXz3onmA2a00-LunaqeBGJSSqB_bOWVIAhpjq-VC1yFP4gP8ZDqxcEKD-OLyjjcuv5EuuWeqLwApC8C2Dd-yMylwWE5TK9895ibiFhacHC5JQ7TfJPUHxBH4Hl707-h7ftRTFasU4uLjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صور الاقمار الصناعية: حفر انصار الله ما يقرب من 20 كيلومترًا من الخنادق حول منطقة باب المندب، على الأرجح استعدادًا للمرحلة التالية من الحرب</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90790" target="_blank">📅 16:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90789">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae63336bfe.mp4?token=surWPPykMQY70CfTkZ6FtMA8kTscqr2iTMSlYEDPxZkdZ9Cc3XU5u9xtqgkDbyyhwvuS0nZMB1wxM76Sfx3L0a_vb8Uu63MU8i8zqHaVdHj8bdIvpXusjxvFf2jNPI6Eh-B2Y-0ZNJHwmScKJhS9doGmwA3MLfFokOxD-6E8VSfpbFlGMsO6r6J5lm3mTUmXU1feaO4vbcj6lmsqVE0D_Sh3beB8_6By1t28D2uQqP13Av0sOndX_tJTALRizRNfsa8xFedWVMnYclb-AQZYO-225Q9mrpPYv5wqEc_MmimXArxYwyVYW2MGkEJwYSjNLYKJrOgsvPGji3NnCBQKIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae63336bfe.mp4?token=surWPPykMQY70CfTkZ6FtMA8kTscqr2iTMSlYEDPxZkdZ9Cc3XU5u9xtqgkDbyyhwvuS0nZMB1wxM76Sfx3L0a_vb8Uu63MU8i8zqHaVdHj8bdIvpXusjxvFf2jNPI6Eh-B2Y-0ZNJHwmScKJhS9doGmwA3MLfFokOxD-6E8VSfpbFlGMsO6r6J5lm3mTUmXU1feaO4vbcj6lmsqVE0D_Sh3beB8_6By1t28D2uQqP13Av0sOndX_tJTALRizRNfsa8xFedWVMnYclb-AQZYO-225Q9mrpPYv5wqEc_MmimXArxYwyVYW2MGkEJwYSjNLYKJrOgsvPGji3NnCBQKIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور الاقمار الصناعية: حفر انصار الله ما يقرب من 20 كيلومترًا من الخنادق حول منطقة باب المندب، على الأرجح استعدادًا للمرحلة التالية من الحرب</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/90789" target="_blank">📅 16:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90788">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f88721f31.mp4?token=hoV6P2G86Y090cWschpR3r2BU1geHlJeOrsTIeWBbhpDayIu-Oo1z-HgzjH5E5N4EuRxdKsenQJIWfitKiJPEk8BgnTwqCUQUOG4A3vmQDjGS22VgiyHnqTZYGT6OuHWwyCw5VrKtZZahwjKvaS_pWdiuvMH7KaGT8BEfCLv2TIevRbQMW93sdFY4UjehioyJZ4lXFQv667DuOMEezyFzhZiDdwoFmjRUyyc-50JzzeIl_QT2sap3wRwFuT_jT4z9VYP3TWgnqveRuZ5peWB_MiKHELl4iDCsf57IGUG_Zh0VKYwNQlZIXS3KDbamMBsZ2GmiVsBRMt8gFY_4aPWwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f88721f31.mp4?token=hoV6P2G86Y090cWschpR3r2BU1geHlJeOrsTIeWBbhpDayIu-Oo1z-HgzjH5E5N4EuRxdKsenQJIWfitKiJPEk8BgnTwqCUQUOG4A3vmQDjGS22VgiyHnqTZYGT6OuHWwyCw5VrKtZZahwjKvaS_pWdiuvMH7KaGT8BEfCLv2TIevRbQMW93sdFY4UjehioyJZ4lXFQv667DuOMEezyFzhZiDdwoFmjRUyyc-50JzzeIl_QT2sap3wRwFuT_jT4z9VYP3TWgnqveRuZ5peWB_MiKHELl4iDCsf57IGUG_Zh0VKYwNQlZIXS3KDbamMBsZ2GmiVsBRMt8gFY_4aPWwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من اسقاط الطائرة المسيرة السعودية في اجواء محافظة ذمار</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90788" target="_blank">📅 16:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90787">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db63aa4992.mp4?token=S1GOJWiusTVGpoxFh2Z--ifTbT0xOyq7vNYfSra-aS9HCTQCDINF91IUNp-F9KWsOzM0R6fHRNMyw4ZCS7PVDvHTSKXqTkiwZYGSF8Kh76GjnVgMur4Zuas_e_H1HJyS4FUbRXIVcRSVr5qU9u3OxdQW43v3whdwQJGV1ixTffoQlpYzuLztH0lu9T0-LchMu1CjZuh5Yguk9zgowEcNNUdWfW1RIHfr890PSLTfYkXKmbxi7dQ2HNwloOu_6L7o1nan5ZDpt2FzwkLY2mCdKDrXVegfuEBZnrHhEy5axS8eRvN58xSXUFKlPoYMhZEmd6AtF2LOsh_sCh4ctN309mhxphDXwC-gwpCGqByN5fZ56L3HetEGmmipLQLf3mkOLkPKR1UxAu5iMwpy0BjGLWF4HiOPh0eZX-_IT7pZFfsiWpofRHAmJmrDWS6dNH3Ip7bfd-arXgMJwmXSwOsDqgTFNBmJxxGI8riI-WPbNUASLlclHS6wgeBWTdmDrqKwpxEjAVOPvedo2TV9oh3df23V5QDfhiL5iI9-wTQIUCEjm3DmMh2r3FTcSvXiMwwRrc-VcMDaq8__covb_b0fulTPlEUG8IWmJkwSkIHzJu1HIXxoe2EonQ0kow49wds9_kICFAGgecpl4zQphp8wTf5vQ09PvaLnCAA1KSMWW5k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db63aa4992.mp4?token=S1GOJWiusTVGpoxFh2Z--ifTbT0xOyq7vNYfSra-aS9HCTQCDINF91IUNp-F9KWsOzM0R6fHRNMyw4ZCS7PVDvHTSKXqTkiwZYGSF8Kh76GjnVgMur4Zuas_e_H1HJyS4FUbRXIVcRSVr5qU9u3OxdQW43v3whdwQJGV1ixTffoQlpYzuLztH0lu9T0-LchMu1CjZuh5Yguk9zgowEcNNUdWfW1RIHfr890PSLTfYkXKmbxi7dQ2HNwloOu_6L7o1nan5ZDpt2FzwkLY2mCdKDrXVegfuEBZnrHhEy5axS8eRvN58xSXUFKlPoYMhZEmd6AtF2LOsh_sCh4ctN309mhxphDXwC-gwpCGqByN5fZ56L3HetEGmmipLQLf3mkOLkPKR1UxAu5iMwpy0BjGLWF4HiOPh0eZX-_IT7pZFfsiWpofRHAmJmrDWS6dNH3Ip7bfd-arXgMJwmXSwOsDqgTFNBmJxxGI8riI-WPbNUASLlclHS6wgeBWTdmDrqKwpxEjAVOPvedo2TV9oh3df23V5QDfhiL5iI9-wTQIUCEjm3DmMh2r3FTcSvXiMwwRrc-VcMDaq8__covb_b0fulTPlEUG8IWmJkwSkIHzJu1HIXxoe2EonQ0kow49wds9_kICFAGgecpl4zQphp8wTf5vQ09PvaLnCAA1KSMWW5k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تسقط طائرة مسيرة سعودية في أجواء مديرية الحداء بمحافظة ذمار</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90787" target="_blank">📅 16:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90786">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18dcda2654.mp4?token=TbDdqtuDdwwoD9hl435PbiS2X7H6irzctQ2r83oXDu3BVP6bZI32A4H13Sn22qhB2QNrEtnDKOMVkCJnMWIe8VtSM8QYwtz_-1d1MXsDRJrysgBi-cCUYnayP_EYiytRGSVeeBho8YRDvoLDOkYQjPQtiuaqeXg4dYLk6CeYqLFMe9L0EdgJo-rLrwSAS694EH2h76rNrAq5EgBldKO9ntu46QTDt-4FHzyxBLaiy2LlxlQbhx64Ce8iDAixO0Aum1rYHEME4u7cUIjqSgNomkEQBVe2yml_-vgpkIX03qTVSfbri5rOx4o0uTAXPJSXs1J304sd4kcU-VcHcvqtLyMPK2zflfw8_59H5KdIrlYVQbQjvpPst3xbS14fqOX8-6cuBMX7iSAo44IFwPpBSCjxe5gwGElIPSRCXUFHrvwcLBMEXy8kQQaOMtab9HFTwYUP6wfP-R32eMJpMsGqNkk6j9Q8t4wW_-xjsJKiS_kUhuPvL5XRdiHIsp_kfaf56EVWTMMlWJq2gYJZ9tDlhC4cyyIuki73Ipo5EKcj_NU_mkuLb-mt6YVLsOZRVD-IiPU4jLffbn6586V7EPYTcSUn3k3Eg2gUhlsQ0fcqWaHKB08Tf8E9mMKuk0wU3jvjCbs5T7qtapIdnTT_thbjMyCYvk97ZbEQe8-KaB7ej1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18dcda2654.mp4?token=TbDdqtuDdwwoD9hl435PbiS2X7H6irzctQ2r83oXDu3BVP6bZI32A4H13Sn22qhB2QNrEtnDKOMVkCJnMWIe8VtSM8QYwtz_-1d1MXsDRJrysgBi-cCUYnayP_EYiytRGSVeeBho8YRDvoLDOkYQjPQtiuaqeXg4dYLk6CeYqLFMe9L0EdgJo-rLrwSAS694EH2h76rNrAq5EgBldKO9ntu46QTDt-4FHzyxBLaiy2LlxlQbhx64Ce8iDAixO0Aum1rYHEME4u7cUIjqSgNomkEQBVe2yml_-vgpkIX03qTVSfbri5rOx4o0uTAXPJSXs1J304sd4kcU-VcHcvqtLyMPK2zflfw8_59H5KdIrlYVQbQjvpPst3xbS14fqOX8-6cuBMX7iSAo44IFwPpBSCjxe5gwGElIPSRCXUFHrvwcLBMEXy8kQQaOMtab9HFTwYUP6wfP-R32eMJpMsGqNkk6j9Q8t4wW_-xjsJKiS_kUhuPvL5XRdiHIsp_kfaf56EVWTMMlWJq2gYJZ9tDlhC4cyyIuki73Ipo5EKcj_NU_mkuLb-mt6YVLsOZRVD-IiPU4jLffbn6586V7EPYTcSUn3k3Eg2gUhlsQ0fcqWaHKB08Tf8E9mMKuk0wU3jvjCbs5T7qtapIdnTT_thbjMyCYvk97ZbEQe8-KaB7ej1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تسقط طائرة مسيرة سعودية في أجواء مديرية الحداء بمحافظة ذمار</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90786" target="_blank">📅 16:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90785">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏الدفاع المدني السعودي: حالة وفاة وإصابتان بسقوط شظايا إثر اعتراض مسيّرة في محافظة الطائف</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/90785" target="_blank">📅 16:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90784">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1iSioW0NyDobVqhhq0eBbjnONcm_cfLaKx5jY49bRgHZCUg9e5vArJaFCoFo1xGzrRW_EOrr3ls4ajqH_F-h8lr7JX0GDSKf5l4GTLQ9xC8DThIupthR1_tjP1Z7-ScvyaCEswiVN5eerFxFMWatgWPUc2i2h43bZxyQeFY2wCxA3-t6_zizOqSdAe-9ioTrUi8dDU5ttt6xhI-7m08JXr_FCLPOX6l9wDFoYjstgHEr6iHpwufuNUxKCTKK_7m6DTaTL7G2rXSxmu2ZwkfIJMLaFPwTtCLDk7GmOuK5FWlvhkMnfTfsqCcg2_eRbUddlPDESL61pPbnVgOhVXBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏الدفاع المدني السعودي: حالة وفاة وإصابتان بسقوط شظايا إثر اعتراض مسيّرة في محافظة الطائف</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/90784" target="_blank">📅 16:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90783">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇶
وزارة التربية العراقية تقرر بدء الدوام المدرسي في 1 تشرين الأول بعد استكمال استعداداتها لانطلاق العام الدراسي الجديد.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90783" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90782">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وسائل اعلام: السعودية تطلب من سلطنة عمان التوسط لدى أنصار الله لهدنة لمدة أسبوعين يبحث خلالها كافة المطالب الإنسانية وتنتهي بنهاية الأسبوع بإعلان اتفاق</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90782" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90781">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHytpUy1mj6S__wL9utQtQhall3bttbaR20l6fumGGGQxj-osCBX9mdyW-tnA1T8OG1A9TIIzzW0FfX6d4H-flxEkm1qsaz9LYKnGVklFm-XsduAkl2LjB3dm6AkJzEMMq3rLLrVHwWi25O1rELIwPVHMijz0s0k7-ioVaIqOCitvHxuQEKGyZ63ct3dHEKlXkM-K43VVfhtMBtqhd9TfUQ1ToRy2S6brR4ClGa6JqFBzdfvZp8Nk-PC5GezbrMzV8bS0HXiaRd7CWMbWb5yBTDUobV3Y3nOjGlyotKXngQrYDo_CGAIABX_73CZ-8-5W82rrff8eDeoCuGHDLCD5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام امريكي: السعودية تلجأ للصين وتطلب منها الضغط على ايران لاحتواء انصار الله.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/90781" target="_blank">📅 15:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90780">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اعلام امريكي: السعودية تلجأ للصين وتطلب منها الضغط على ايران لاحتواء انصار الله.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/90780" target="_blank">📅 15:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90779">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تواصل تصاعد اعمدة الدخان في شمال الكيان بعد تسلل ناجح لطائرات مسيرة</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/90779" target="_blank">📅 15:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90778">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WptKBVIpJVzY1JTyU-5bryBbgmxbFypV6TCgKxIMReICAuvMk_EzISPQw5Std5vIkQcECZo4kpnWGVO6VCRXTrzFokohblaJDfT5ErBDEeVpg_8-IRNAawGyeiSMYCTphYSw9bu8LrJq6bNc5g8r_SIIpt4-immJXaJpZDab5mC6ZUFAFTxfPBp-x3ybWTKL0cnZq9PFKQtCjLOVv_4KI-eFEDQpRMwVyEqivDDI04UseUhaVEcOxzS2X6h-3Za1TJbOJ_DJts8eIqzUuxbV8Tj_m2IjQ9X8Bxb19hZ5zuAh0NZl7Gk28L-DO8sr2V9as_hN71ede32XovI2abEjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من تفعيل الدفاعات الصهيونية في شمال الكيان</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/90778" target="_blank">📅 15:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90777">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4b3c39fe7.mp4?token=tPTl2zad33E2UYBDcS4a9YpzYLqzPBK6RsXf_YtnzjUQVBjIYeF3Bk8ZRHfz04CgrURx_BYiHm9gO2zBBGxfVGVEVVhmo1kNipiT9zG9KBckAECjPZj7g5lTfm8-NV8M0GnFDBKOOzP5YTtPInTUEd0sZy7uXK72LDeKZapVK9Zrf-lWzNRAViE4pXjAfHTG-FXy1UY4RxM30CLnByl8xtiPI2L6o8pOK43soIY4fXIEK10lUS6HOrvMjv20uz840rkbF6lpU4-xWT-D9nLW6Ikc8m3NK6_7cWEzN3a3WoLFky8Nl5wCu9NX56F3G1bthUkOyVO8FpvH7QLxUIKVyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4b3c39fe7.mp4?token=tPTl2zad33E2UYBDcS4a9YpzYLqzPBK6RsXf_YtnzjUQVBjIYeF3Bk8ZRHfz04CgrURx_BYiHm9gO2zBBGxfVGVEVVhmo1kNipiT9zG9KBckAECjPZj7g5lTfm8-NV8M0GnFDBKOOzP5YTtPInTUEd0sZy7uXK72LDeKZapVK9Zrf-lWzNRAViE4pXjAfHTG-FXy1UY4RxM30CLnByl8xtiPI2L6o8pOK43soIY4fXIEK10lUS6HOrvMjv20uz840rkbF6lpU4-xWT-D9nLW6Ikc8m3NK6_7cWEzN3a3WoLFky8Nl5wCu9NX56F3G1bthUkOyVO8FpvH7QLxUIKVyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدخان يتصاعد من كيبوتس دان</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90777" target="_blank">📅 15:17 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90776">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اعمدة الدخان تتصاعد من شمال الكيان</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/90776" target="_blank">📅 15:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90775">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaRiYgDtJOwHhaEYGGixNiZsQySqB5ghZm-h8Ws-QONOJ3Xc8yxjY-DCtYXlb0PfHWspn9zdEPH8Skt0C2qt6KBmEX9v6wukDpUmqV2s7hQX_fErO23fzvlKo7pWEcrpx05AvQ7evnRg1sk0NM3FZ9AfHSa-VcQyMHdxQWHAoj3VAZqfOeIUK34LjaKYdYMgwAep3JGkT4ukVGWCluFFZxk-pfSbcYco54ViZ0mPCiYmrU2vSsG1gFak5bU2QjbEIKlQQBHzmE0ZGx-Ie-mA9nimvxPSqV-lQ_uyS_D6VXFsskqs0TnYAgsCrZj2QMKG6V5mhyysDsKSpqJbPK59nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من شمال الكيان بعد تسلل طائرات مسيرة</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90775" target="_blank">📅 15:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90774">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39633299af.mp4?token=DmALfqDt10VIEtDO4FSW_I8tOyIOCK1-sVkW2Dn9DtndaRhtwLDweYEWoJekj_Ne76TV4HFwRcYV-mkR3jAQkcV_xOx4-Oo0GFMTcGd9gbtze5cBEkSPn1HIQEpGymLVGdwiL92vhmP2K1giekBduUXIBrWW0gPWSqZV6gI_7wOfl1aDFJpk5UXSajz_x2eLpGzxJ-jm9O9huy4o8iMHXaf-bw9_m9XVGAakLWM0RzB26rKLRcH0hh1q6C3l-v2xeTyDbFmzQfik-RXb1BnXNMOQ4CwCSPx0310StNLJSg1pw13NhwcaMfswlcg7QOCAlZBybVUWFQzxckuvhT8Wvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39633299af.mp4?token=DmALfqDt10VIEtDO4FSW_I8tOyIOCK1-sVkW2Dn9DtndaRhtwLDweYEWoJekj_Ne76TV4HFwRcYV-mkR3jAQkcV_xOx4-Oo0GFMTcGd9gbtze5cBEkSPn1HIQEpGymLVGdwiL92vhmP2K1giekBduUXIBrWW0gPWSqZV6gI_7wOfl1aDFJpk5UXSajz_x2eLpGzxJ-jm9O9huy4o8iMHXaf-bw9_m9XVGAakLWM0RzB26rKLRcH0hh1q6C3l-v2xeTyDbFmzQfik-RXb1BnXNMOQ4CwCSPx0310StNLJSg1pw13NhwcaMfswlcg7QOCAlZBybVUWFQzxckuvhT8Wvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات ضخمة تسمع شمال إصبع الجليل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/90774" target="_blank">📅 15:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90773">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محاولات للتصدي في شمال الكيان</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/90773" target="_blank">📅 15:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90772">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ks3ITcDYJ3_Dx9rDgT07wuM-M0GuMVQe-8BMuhGHIfxxbGJ5ZnK1CVjdT3R7tPKOLCUWI_aEGiUSquBP510U3ITf1Zt7mxYjLYpHT_m7NF7eZ01ymRGtdAmy9okoH8Axl-7u3-rl7upy4pLmPxMiom0yN1INEUkOhtj-T7Dwy9Hmz8tuOaj3DPt9BvgW2YA96jxl0K1DaUDUzwLiEjN7KK8ZRXQi1Ck2P14Cl8jxcQCNce2XoV-5hiwm012LD5JpZEHroomPckf2MrDgzviddzZAI9UJ90_L1UojKWYbj-BXFr2a-Z5xlulSk8g1L_QpXaybzbOBhEWpkcaTHqecKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفعيل الدفاعات الصهيونية في المستوطنات الشمالية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/90772" target="_blank">📅 15:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90771">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">تفعيل أنظمة الإنذار في منطقة منارة ومرجليوت</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/90771" target="_blank">📅 15:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90770">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل طائرة مسيرة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/90770" target="_blank">📅 15:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90769">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇱
صافرات الانذار تدوي في المستوطنات الشمالية بعد تسلل طائرة مسيرة.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90769" target="_blank">📅 15:04 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
