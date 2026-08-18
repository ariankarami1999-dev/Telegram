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
<img src="https://cdn4.telesco.pe/file/Inx2ztDzVVgsf73jZ8rExwmA-v89JafQG7RPLBwq5hVlhx8ezbTC_HoXyY6AX6lv76T8m76bl52XhiDofr5Dv0gtNcEuQFahvfPCzIyojQRDkf6xxWpD26tILV7SC3CWursswFObvyjqhCQzjW0R3C-KafKZCcKZUBuEgmGCvd79tJKoiWPwHkWNYOnIv7eNkqzmotYXcfdiNtPntqIBXIZj2ASUqYOqke2B0vAQoweJ2yy1iPK00L0G98R2f0qtreqR7y2PbXNhWdOLKXWFa4X3TKYKvsRnhbDiG0yQ8SGCWailEbkulOPba4nG5nuFXo9_QQ6Kf88EYO-A2biJJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 271K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 18:29:11</div>
<hr>

<div class="tg-post" id="msg-88079">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 9 · <a href="https://t.me/naya_foriraq/88079" target="_blank">📅 18:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88078">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/naya_foriraq/88078" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88077">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هجوم صاروخي على دبي</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/naya_foriraq/88077" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88076">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRdosakbMm_fPMlXAq_v1gzazJ8wM__uNaRi4F_40XMjtWgY7qI6T-5S0UBAF72CHVTAVrHWCAJs3KgbgiykxF_yPrV5h7Ubf4pMYqwClNojWbZpM17zh7xNSo9hb5cofXNBmfkkOtQA8gs5O4raVSXB_hcYxagj8XRWcRXgWwFyrVmW6s_YeN_xYsoq4rxqHiZACUvOGNTlt5xxtdQl_Bnz_oWJpuGRNwZCwvZeDu-M7dNycPmJ1GzPsnTb-0PgWwmdm9lBZQm_VgjvRdByZBb3ESJwHNY9G5vyQGZFqnr2RtrwCFPcuhVe-4_znJObWzElad9BM0F9f3hTFTCGkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/naya_foriraq/88076" target="_blank">📅 18:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88075">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوي صافرات الإنذار في دبي</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/naya_foriraq/88075" target="_blank">📅 18:23 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88074">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/naya_foriraq/88074" target="_blank">📅 18:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88073">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/naya_foriraq/88073" target="_blank">📅 18:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88072">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/naya_foriraq/88072" target="_blank">📅 17:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88071">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA43BM8fCNiQdtQCRihtWGME5fh3CPjNiVW7TRVsF7kS8xwsAkWExq6lIdmLW2zLNO7uXqtP6Mk4TIB8IODZR7YCuM4pfdqOL3n84B4SD5lvtLxoydRGipJwL9TdtLRuXwRBk4pzoOKreN2o8BXWiu7O9RWayHw6rdS8ikMiDs-PKz7epvO6giGENV9ZALvJkzo5mVL_6qIpHE8KCz315SFWANKIMmKiXCyKq_vmh9SMxLHy1ArtEL4KDi157_Ko2eUwe1v2hlkwGI9juZ4OcZjcrLbOqwzdLS0uEuThg-YYuYbn2pIawBWTT8IA8Ou5ZvRuJLT7eOsE8rqHJa9oUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدث بحري قرب سواحل عمان</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/naya_foriraq/88071" target="_blank">📅 17:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88070">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏مدير الوكالة الدولية للطاقة الذرية: تم العثور في سوريا على أطنان من المواد النووية التي يمكن استخدامها استخدامًا سيئًا.</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/naya_foriraq/88070" target="_blank">📅 17:26 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88069">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">الكويت تقول ‏ان ثلاث مغذيات فرعية من محطة التحويل الرئيسية الرميثية (B) خرجت عن الخدمة .</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/naya_foriraq/88069" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88068">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfZcIXsj6UwLV0SegijR_0hxGq6pCHVbtkpwYnR1Zb2ECS4vS3MJTtL10QYZenQ9vbEX9V74QwNUIDagOcW2yzmGs_qPTFQunCopLfQ6e3QbpQU02a0MUdEFMVlfcZZ1O_QTOnMk_N1f9bSxKXs_6TwblQolrJEy0Wb5vN4t8lGuBkd06DcGZ_9DgLrVjqqIYcskAjnyEBc11CZhMpnA4qDiM32mtPDGu5QBlKnxGj40Mz8kjkfgR-MKZHgdUtiah5rblrGSXZFOKlMPdZJDGbDejCaMw7ii3xy8RztPxgEHHbuKujRHEZPYcjXhRSA7zs-bWKy3soXD_ZlSw-qqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🌟
‏
ترامب:
لا توجد أي محادثات أو حوارات جارية، أو مُجدولة، مع الجمهورية الإسلامية الإيرانية. الحصار البحري لا يزال ساري المفعول بالكامل. مضيق هرمز مفتوح ويعمل. جميع الألغام المائية قد أُزيلت أو فُجّرت.</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/88068" target="_blank">📅 17:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88067">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الوكالة الدولية للطاقة الذرية:
انفجار لطائرة مسيرة في محطة زابوروجيا للطاقة النووية الاوكرانية، وذلك في حوالي الساعة 06:00 صباح اليوم. مما أسفر عن 16 إصابة، بما في ذلك وفاة شخص وإصابة ثلاثة آخرين بجروح خطيرة، بين العاملين والمقاولين. ولم ترد أي تقارير عن أضرار تتعلق بالسلامة النووية أو الأمن.</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/naya_foriraq/88067" target="_blank">📅 16:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88066">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇸🇴
النائب الصومالي عبدي حاشي عبد الله: أصبحت الصومال ساحة معركة بين إسرائيل وتركيا.</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/naya_foriraq/88066" target="_blank">📅 16:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88065">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">والي العراق والشام توم باراك: ‏ نشعر بقلق بالغ إزاء الغارات الجوية الإسرائيلية المؤكدة على قاعدة أبو الظهور الجوية، والتي تشكل تصعيداً غير ضروري لا يساهم في تعزيز الاستقرار الإقليمي.  ‏لم تتبنَّ حكومة الشرع موقفاً عدوانياً، ولم تُبقِ على قواتٍ بالوكالة. بل…</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/88065" target="_blank">📅 16:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88064">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇶
🔻
حماة الأرض .. حشد الأرض
مستعدون للدفاع عن العراق امام كل خطر</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/88064" target="_blank">📅 16:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88063">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1_i40flI94VspcYujWaKePvPJMWnwcSVnwVqZuV2MugOfjWu9WqlNDJUo72tCAawV9qTLtkjFcMvPhKwppKE5VXag8MNYcBrAZOk-5eYuFtjHx-uTrk3Uqe6r6pXYp328N5qMpMq_nCBDqrw-e9FJW1koHYsKfCFQlpjyZVgNi_zilebDEmvvXgb7Y3OSHsq7CAcYq6W-S1SyRec0qRe-Xb-fov3QIBo-RnYEZNfjECL6d3BoNm1zLn-0X7jC5aKf2RmrkvYSm6Fs_aZKQBeo-cnXKQWT5JgYQH17jTYCF5jJLBHEUvTvxtwK3h-zGKzgHQqk5HIldpPseW7XnwTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطار أبو الظهور بعد الغارات الاسرائيلية</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/88063" target="_blank">📅 15:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88062">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUhkYKwaSzck9SLNIG8gHtHb6KsiB49XmcssE3BvloC8B5pMnsHgHO8Pek2Ttma3OGg6l2DBw8iUjcml7WPMxDa-ePTh0AdYqgtciiWJwjPPJzq2CQJWEfz0rpeDPlJUCKMfo2ItGj7I7Z9KZqsbd2LsxvHN6K2hLKlxUZx4YMMr0FmDqSKWGydqG2Sr9HKbSdpHp3croSceqXkuqMwNkh5I5MqvAyuC1klftcA1_oJhXdHLECWNdZ2ZG-70mpBrkXdEvSmvG2PVjOQIfGe-F3MucHmd8mEK7JGX1zi2UCo81cc042BICS-vpLRwg5z4AIQJWrJbPwykVfyZvFSMew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الغارات الاسرائيلية على ريف ادلب</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/88062" target="_blank">📅 15:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88061">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/452a2d8719.mp4?token=k0oqdd5rXtAEpQAs7CTjmOBSkrD38NX7aG4xsJCB-hWyFqkAbqAJwgNg7raBbB1-Ru9m7rafGhmay1-zh6i_7hc-27iMrUOoatRcVzx8j9kRUMF6sb2SH_sZG3mdmSNdOWocXFSTaB94SIyZ7Cp38uhuI0CDEHzcQTTf7SW4dh0ITX4tPqZucWVK3IL_vh4tosEKh_XncV_Vs_rSvSIniS7OCgPJWRhY79uY4ZZnwAVgsvGUB3h1SD7id3yEMMbRomuVDom6qHcdmRuKt9pbocQUZ2427Sk9jX8G8mjSjZ02rtxLAMqKE19jNTirt2mYGs8IQ8TtgCXaP6iWrNsfxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/452a2d8719.mp4?token=k0oqdd5rXtAEpQAs7CTjmOBSkrD38NX7aG4xsJCB-hWyFqkAbqAJwgNg7raBbB1-Ru9m7rafGhmay1-zh6i_7hc-27iMrUOoatRcVzx8j9kRUMF6sb2SH_sZG3mdmSNdOWocXFSTaB94SIyZ7Cp38uhuI0CDEHzcQTTf7SW4dh0ITX4tPqZucWVK3IL_vh4tosEKh_XncV_Vs_rSvSIniS7OCgPJWRhY79uY4ZZnwAVgsvGUB3h1SD7id3yEMMbRomuVDom6qHcdmRuKt9pbocQUZ2427Sk9jX8G8mjSjZ02rtxLAMqKE19jNTirt2mYGs8IQ8TtgCXaP6iWrNsfxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/88061" target="_blank">📅 15:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88060">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">غارات اسرائيلية جديدة تهز مطار أبو الظهور في ريف إدلب الشرقي</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/88060" target="_blank">📅 15:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88059">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
‏ترامب: مضيق هرمز - أرض أمريكية جديدة</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/88059" target="_blank">📅 15:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88058">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjZhnO3puBESBPhDpopADMFTQCJBAzwAP7uWhwP53dpyB2mL2XoKtB2-d6Lbb6IiTQoWIjaJKulpYkBdym55gZuvUrO9Rd58w6b0xxCZtY5aUYCvVHutRLjYQBrcTqKKhOnuR6PN9GgHLSgvkKouXygBA5nmwuvlGc18tKVG3ZVj_h6l-ei7lS6WJnJRj_9lkMjyMcKvCX3MbzYDUr5M-XHk6ZeqojwZtoKRxpGPTe2JlINBSXcT_th1UIGMloSN4uM7c-94TcXC3rSEzKZpPUhAo0k8xz6K3j7cngUAQKxFTPtjlaH2eTtE2I9Mt4Vf3SjtAGGUwN3fI2ZsLDJM-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
‏
ترامب:
مضيق هرمز - أرض أمريكية جديدة</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/88058" target="_blank">📅 14:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88057">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇶
المرجع الديني السيد علي الأكبر الحائري
: فإنّنا نؤكّد أكثر من أيّ وقت مضى ضرورة الحفاظ على الطاقات والقدرات التي اكتسبها المقاتلون الذين شاركوا في مواجهة داعش، وعدم المساس بها، بل الاستفادة منها وتسخيرها في خدمة العراق والدفاع عن حدوده وأمنه، بما ينسجم مع الدستور والقانون وتحت سلطة الدولة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/88057" target="_blank">📅 14:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88056">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRKqXJTUvePpPJjiMxn4fZG4P1Wtj2P_cfdH_GsBQKFBlSQvpD9YdmWtErRK2AESBtJxiSV_b_DvHQAO3QRLhOLtABdrVaOP4N8oRuh-tUsRVC66W6bJ8GIN1LnNhv7xUB8jxuNRzW47Vn7vn86Afo97s9yw8cRnf7W2Ee02-2tn7jzWnLw4TY1mOIRWV6uujm5KL6AxuqFMdMo8buCnXtsZaPXSnQUcja3IUTb-vAfRsvDnu9awWL5xZf_9rN1nXPrEGtdXDWz-I5aw4b4nzpVu8U01mphG1OfGQnpCjhiqzZpmHIXQQ7k6q9X0z_dmcqBPRA99XVp3xyZZml5LyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">والي العراق والشام توم باراك:
‏
نشعر بقلق بالغ إزاء الغارات الجوية الإسرائيلية المؤكدة على قاعدة أبو الظهور الجوية، والتي تشكل تصعيداً غير ضروري لا يساهم في تعزيز الاستقرار الإقليمي.
‏لم تتبنَّ حكومة الشرع موقفاً عدوانياً، ولم تُبقِ على قواتٍ بالوكالة. بل إنها أبدت مراراً وتكراراً تفضيلها لخفض التصعيد مع إسرائيل. وقد استضافت الولايات المتحدة في الماضي، وستستمر في المستقبل، حواراتٍ لتشجيع الحوار الدبلوماسي بدلاً من اللجوء إلى العنف العسكري الذي يُحبط كلا البلدين.
‏تُبنى اتفاقيات خفض التصعيد الدائمة من خلال حوارات مستمرة مع جميع الدول والأطراف المعنية.
‏لا تزال الولايات المتحدة تؤمن بأن ضبط النفس والحوار هما المسار الأكثر بناءً. ونشجع جميع الأطراف على إعطاء الأولوية للحوار المنطقي على حساب المزيد من الحوادث العسكرية.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/88056" target="_blank">📅 14:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88055">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee33539d.mp4?token=HljtKL7W52ZYCE1qBO3f0klTaGcU0332MQ6uaC16a4aD7kS_5OUeC9Rka1Ff6ZYGP4SvF-_F63CtNvznrYM0SO6rXKyinmB-o8MOuGkrpEsNWa3TMmoPxBTC_K2ghjmAo5zWD_EFufgXZ20puEOQC9rnr-1fMcGeBo-799g7kJyfGC9oTZea9Q7Jp4fojBHjOr4r5spC1TZeTFZytMZu5diqSrNOV_OqOuuV7c6aQhJqDtdx-o95oYIFS5CgftD0H9i1tPwAjts34R3Dbzn2EUaI8isem9L8aSB2sip6jwLKlH-6pkAQdC1EddZevVCy_LuzQiJdUrTaNVkDGjJn1TA-zduWr8A7OJW0pFuys5aD1x9cdDT4ePzWu6JxhtSGj6uxNuvs9zWScwZ0bqVb1zYhVW6BXwvbtXjs-FIBunAIuH5xlb7I1eerbVDxJkDHTN4_Zjsc08q1ep_phW22RWVGw8MW-svIMlomJX8ukGWlZh--76J0SwR4_Gp8wSzEaS0CInwWZ5NicLy2ht5ryzB2Uilbfa9Gzx0gWWyu30aZkkVaV7CTKwQqZ-0Yba5LRQfTfZTyencMVTwKDnrS1dMINVyzn3oWCgqBRtSQ1U_SXV1xMPw9rnxc-vBpXoH7rU85zqTZC5LN6fdsjliY72eRHkhFqDPHzA-XXu7NLJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee33539d.mp4?token=HljtKL7W52ZYCE1qBO3f0klTaGcU0332MQ6uaC16a4aD7kS_5OUeC9Rka1Ff6ZYGP4SvF-_F63CtNvznrYM0SO6rXKyinmB-o8MOuGkrpEsNWa3TMmoPxBTC_K2ghjmAo5zWD_EFufgXZ20puEOQC9rnr-1fMcGeBo-799g7kJyfGC9oTZea9Q7Jp4fojBHjOr4r5spC1TZeTFZytMZu5diqSrNOV_OqOuuV7c6aQhJqDtdx-o95oYIFS5CgftD0H9i1tPwAjts34R3Dbzn2EUaI8isem9L8aSB2sip6jwLKlH-6pkAQdC1EddZevVCy_LuzQiJdUrTaNVkDGjJn1TA-zduWr8A7OJW0pFuys5aD1x9cdDT4ePzWu6JxhtSGj6uxNuvs9zWScwZ0bqVb1zYhVW6BXwvbtXjs-FIBunAIuH5xlb7I1eerbVDxJkDHTN4_Zjsc08q1ep_phW22RWVGw8MW-svIMlomJX8ukGWlZh--76J0SwR4_Gp8wSzEaS0CInwWZ5NicLy2ht5ryzB2Uilbfa9Gzx0gWWyu30aZkkVaV7CTKwQqZ-0Yba5LRQfTfZTyencMVTwKDnrS1dMINVyzn3oWCgqBRtSQ1U_SXV1xMPw9rnxc-vBpXoH7rU85zqTZC5LN6fdsjliY72eRHkhFqDPHzA-XXu7NLJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اختفاء وفقدان ثلاثة شبان من محافظة اربيل في اقليم كردستان العراق منذ ما يقارب الأسبوع بعد ان حاولوا الذهاب تهريب الى اليونان عبر الاراضي التركية وكان هذا اخر فيديو لهم. وتأتي موجة الهجرة المتواصلة في الاقليم بسبب الفساد والوضع الاقتصادي وانشغال العوائل الحاكمة بزيادة ثروتها وتكديسها وترك الشعب يعاني.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/88055" target="_blank">📅 14:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88054">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇶🇦
وزارة الخارجية القطرية:
المبعوثون ينتظرون وصول سلطنة عمان وإيران إلى اتفاق ثنائي بشأن مضيق هرمز قبل العودة إلى المفاوضات الأوسع بين الولايات المتحدة وإيران.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/88054" target="_blank">📅 13:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88053">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
🇺🇸
رئيس ائتلاف دولة القانون نوري المالكي للقائم بأعمال سفارة الولايات المتحدة لدى العراق: الدولة ومؤسساتها الدستورية هي المرجعية في إدارة الملفات الأمنية والعسكرية وحصر السلاح.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88053" target="_blank">📅 13:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88052">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IawvEM86zeYe8WHJ0_VpStwiC3dk7qym2WFKIV_JeNg2W9N_FOwiICwhGhmiI3G8Aihb3aMaugO3W5sR-WjXbYRpF3U0ZzNPKDKtnMT1h4XtzE7oAgSddlL8iTSPwvf7x_EAZacOpgaP28DLajJJEXUVDVdeou5TmZK996Un5F-nh0Brkl7rVhX9dGS5SkM8wN6TocWrvWrLCKgaMl6HWt1bLhRHufadNbgK0Zy6vjWvWo3sFqxwEeje5w-Md9EJD0bdNmXynYCm9IPfvuac-tC7py8tbAVRGZY9V7WTv-e8MTegQD1DL7pegkiO4cmBQS1CZB6hM4xo4HMX5MA-qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج هادي العامري:
ندعو الأطراف كافة الى التحلي بلغة الإعتدال والتهدئة، وتجنب الإحتقان في المواقف والتمسك بمقومات القوة والمنعة للعراق الذي نتوق له جميعا، سيدا موقرا عزيزا، ونبذ كل ما من شأنه أن يخلق الفجوات ويغذي الخلافات.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88052" target="_blank">📅 13:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88051">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
علي الزيدي حول الهجوم على أربيل:
الدولة لن تتهاون في حماية أمن العراق وسيادته وأن الجهات المختصة ستتولى التحقيق في ملابسات هذه الاعتداءات وملاحقة المسؤولين عنها وفق القانون.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/88051" target="_blank">📅 13:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88050">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قالیباف:
لن يفتح مضيق هرمز قبل رفع الحصار، وتحرير الأموال المجمدة، وإلغاء العقوبات النفطية، وإنهاء التهديدات والعمليات العسكرية في جميع الجبهات. إيران مستعدة، بما يتناسب مع الإجراءات والتعديات التي يرتكبها العدو، لإلحاق هزيمة أثقل منه سابقًا.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88050" target="_blank">📅 12:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88049">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇷
🇮🇶
مصدر إيراني: قالیباف يزور غدًا العراق على رأس وفد برلماني رفيع المستوى، بهدف إجراء حوارات حول التطورات الإقليمية، وتعزيز التعاون الاستراتيجي بين طهران وبغداد، واستكشاف الحلول المشتركة للمساهمة في تحقيق الاستقرار والأمن في غرب آسيا.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/88049" target="_blank">📅 12:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88048">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بعد قليل سوف يتم استلام المخطوف إلى أمن الحشد</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88048" target="_blank">📅 11:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88047">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
‏
رويترز:
شركتا شحن صينيتان عملاقتان توقفان إرسال ناقلات النفط عبر مضيقي هرمز وباب المندب.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88047" target="_blank">📅 11:29 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88046">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12b581c02b.mp4?token=nxHni_b-l9I-sf89g3BkIsAsVmXep3mKJ_oRbr4EQND2GUu_e0Fe2N3eJsEUISjaepGSBb6fErQ2UR-GEYHTrJ6lS4fF5BjMGDkqLOw8LiHgmBMokmfCYJiDpWt9eVaw-oHG7oI8di065BxauuGYQeoOITOYNiZbrViH0QhUyicjHX1FGW-KyIkD-R5xmuscpcJfPFcIclFozDdrOwGgTux2GfpxH92r0lTCvccM5yzVFnrOMn9V8SOdfhbyuIaIQ9JeBPCiqZi4bqOfyRGsHTqJ0QcE03ntP_xaUXaexknEIe3dTxJyWfn8wb-Y8_ZyHqgReVX6U9m5Pr2gbArbkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12b581c02b.mp4?token=nxHni_b-l9I-sf89g3BkIsAsVmXep3mKJ_oRbr4EQND2GUu_e0Fe2N3eJsEUISjaepGSBb6fErQ2UR-GEYHTrJ6lS4fF5BjMGDkqLOw8LiHgmBMokmfCYJiDpWt9eVaw-oHG7oI8di065BxauuGYQeoOITOYNiZbrViH0QhUyicjHX1FGW-KyIkD-R5xmuscpcJfPFcIclFozDdrOwGgTux2GfpxH92r0lTCvccM5yzVFnrOMn9V8SOdfhbyuIaIQ9JeBPCiqZi4bqOfyRGsHTqJ0QcE03ntP_xaUXaexknEIe3dTxJyWfn8wb-Y8_ZyHqgReVX6U9m5Pr2gbArbkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صباح العزة والكرامة و الآباء
🇮🇶
النجباء بالميدان</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/88046" target="_blank">📅 11:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88045">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdMS7_irrQcXvyniPsxTRA83pwGjbGACLLJjiOBFBIU8l_LVYRDwvQmkRQK88fL8THSOiaQ12ldHD4Nn6m9Xv0_o5p4YIGFFoGsqpU7yxIE9D2_SucQFkGMfxclrsJ_zibFMdB2bmoYlzNuXtKk5bqf2oELI_GevrezUuoCodUM8pmNCzqRrtMps1F8FKIqZ--nLlR7qhnjx4xvH2wWw32tDy7LGtC2DGvsOEH0otlE7oNPbhojq2vdeRxyZhdu3Faio8Bi-3yj-ZAJefpO-4Fkc09UsjYlBzeOCdpUERQrTrdo1J9hsMoKeddu24CPg5HwJ1eKzX0shYFf-wd583g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
بعد عدوانها الغاشم على العراق ومقرات الحشدالشعبي..
السعودية تدين وتستنكر باشد العبارات الاعتداء على اقليم كردستان وتصفه بالإنتهاك السافر لسيادة جمهورية العراق!!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88045" target="_blank">📅 11:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc90a1fcd.mp4?token=X4iC2N8LfygBTunLaLoDA1ozgxMVQcUCTzoFzqEY0CJRjf5zPazl76lSI5mhTiD4_IvDlt3oxWSdJJYyqVqiud_KB589ALKprLUKPwuSaw02tLXWbgW8f1P8DPKHqN52C_Vn8SHuWOhArYjKHst1lN5Zt2UOs7eseRqaY2mgS8pQljuSoM-o5hxuA8LfZJfKClnkQkPIiPIgFRZ7xqg647oImQglDzkS_3IJGOsnvP9h50N_mCe3Yy8VwHOsD6I6krePTwFY2O0xu50joG_u_deCl4rkPsqKzujzVfKLbOEuPSbIwbdiKc2L6TGRKcHN5hyCFQB-jY-58hGgtpOb1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc90a1fcd.mp4?token=X4iC2N8LfygBTunLaLoDA1ozgxMVQcUCTzoFzqEY0CJRjf5zPazl76lSI5mhTiD4_IvDlt3oxWSdJJYyqVqiud_KB589ALKprLUKPwuSaw02tLXWbgW8f1P8DPKHqN52C_Vn8SHuWOhArYjKHst1lN5Zt2UOs7eseRqaY2mgS8pQljuSoM-o5hxuA8LfZJfKClnkQkPIiPIgFRZ7xqg647oImQglDzkS_3IJGOsnvP9h50N_mCe3Yy8VwHOsD6I6krePTwFY2O0xu50joG_u_deCl4rkPsqKzujzVfKLbOEuPSbIwbdiKc2L6TGRKcHN5hyCFQB-jY-58hGgtpOb1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إعتداء القوات الحكومية على الفلاحين المطالبين بمستحقاتهم المتأخرة خلال مظاهرة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/88044" target="_blank">📅 11:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88043">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5ewIMe8zEwaZq4K05XW9kEsXx4KkyQQ3zXSmKXJqSQ9RfGMkFdF6z6uXD2GwIpedBwdmVH6SinS8srVTn0uZdVmHHH6-a1hQhpU_FgM3ObeEieKrixlc9rZxZ1ky_kUGk9URbh0UYTUi8tsOCh9y4Xv4Cx4BwtkSRuBOqbfD296qhpPOESPXJg7TOlKwcZlgHh6nFSn3uS0ri_EoJFDKdkLTuP8zUzV2DivHljyvoiBL9RC8K4VPkf9wQD3iWfWqs11cJp4EWcAjpAlyV6vZiV6FHH7H9z5WhjUvOIeSoqD4nAZ3WPhravC9BjLfFHxHlj8CIyNmaLoGSt0ZB6oTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
في وقت سابق من هذا الشهر، سأل جانيش كومار، رئيس لجنة الانتخابات الهندية، إدارتنا: "كيف يمكنكم إجراء انتخابات في الولايات المتحدة بدون بطاقة هوية شخصية صالحة؟"
بلغ عدد الناخبين في الانتخابات الهندية الأخيرة 646 مليون ناخب. أقل من 1٪ صوتوا عن طريق البريد، وكان على كل ناخب تقديم وثيقة هوية شخصية صالحة.
نحن بحاجة إلى تمرير "قانون إنقاذ أمريكا" الآن!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88043" target="_blank">📅 11:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88042">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
هيئة الإعلام والإتصالات تصدر قرار تحذير لقناة الرشيد الفضائية ومنع ظهور أحمد الطيب وإيقاف برنامج.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/88042" target="_blank">📅 11:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88041">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcdc5a1a2.mp4?token=qr39hUhxJu8txY0DwV97nNT-NkUZsPP7dQ_aBTHAFapB4pgmn0J2sFbU2sPiPacBkzGyoWD-HBHIt0OGQUvEfDb1yYm1yWjr_WH6WFWOkqtdF3q6GYfQ3ZE2t2YWJer7desuqGLhHLreLyASHqmWuesPvnYud_yaEaW0D3SVfJjySHAbMxnZw4OcB4_MvzBuEyP4U5_KJWzJqber4auVsixLzFcg7ZLwdaN9V2_cSxvV4UjPm92U_l7L71sa5dAbrRp9CXgKjQkIYT2PwM7Bwf5Rq-4h8WybOxRxYTuiI50R0VwVu9Th7Nwdqcm8kveg0kLoR7S4bU_FKuJANGwQ9bTnFCC_4180tUsUpF_JdD9xv3naSBZneNKI4YBgq5FnFsl-B05ceVt7rXQpNvIEe5m1AvLbb1-8EL-Z66hRUKi8eDYJMaB4bmslpv__x6Sge0dqSsORfwNPmN5Vh6RGmdsFZcNg-m2_zd-_dS-tHf0icdjrttfKn2atdmGp_haGLQZiVzzr_HJeHPOxbMhpNvz2aoUeh1NLrpaQsgDVeVoEFXcMEW7A0XUA5VeZSkGH2T1ioY5uAtScw3cJTKhLHiLxDe9THrPgb3PeCPrjRuxCtAPbchcg4RYiaJ82DiTAph3i18TI1nLO0DfzADatTs87jv5yGZmY4Lt8IolG7RM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcdc5a1a2.mp4?token=qr39hUhxJu8txY0DwV97nNT-NkUZsPP7dQ_aBTHAFapB4pgmn0J2sFbU2sPiPacBkzGyoWD-HBHIt0OGQUvEfDb1yYm1yWjr_WH6WFWOkqtdF3q6GYfQ3ZE2t2YWJer7desuqGLhHLreLyASHqmWuesPvnYud_yaEaW0D3SVfJjySHAbMxnZw4OcB4_MvzBuEyP4U5_KJWzJqber4auVsixLzFcg7ZLwdaN9V2_cSxvV4UjPm92U_l7L71sa5dAbrRp9CXgKjQkIYT2PwM7Bwf5Rq-4h8WybOxRxYTuiI50R0VwVu9Th7Nwdqcm8kveg0kLoR7S4bU_FKuJANGwQ9bTnFCC_4180tUsUpF_JdD9xv3naSBZneNKI4YBgq5FnFsl-B05ceVt7rXQpNvIEe5m1AvLbb1-8EL-Z66hRUKi8eDYJMaB4bmslpv__x6Sge0dqSsORfwNPmN5Vh6RGmdsFZcNg-m2_zd-_dS-tHf0icdjrttfKn2atdmGp_haGLQZiVzzr_HJeHPOxbMhpNvz2aoUeh1NLrpaQsgDVeVoEFXcMEW7A0XUA5VeZSkGH2T1ioY5uAtScw3cJTKhLHiLxDe9THrPgb3PeCPrjRuxCtAPbchcg4RYiaJ82DiTAph3i18TI1nLO0DfzADatTs87jv5yGZmY4Lt8IolG7RM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
إعتداء القوات الحكومية على الفلاحين المطالبين بمستحقاتهم المتأخرة خلال مظاهرة في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/88041" target="_blank">📅 10:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇾🇪
🇸🇦
هجوم بأسراب من المسيرات على مواقع مرتزقة السعودية في مديرية حيس جنوبي محافظة الحديدة اليمنية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88040" target="_blank">📅 10:42 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇷
مصدر إيراني:
تم تحديد واعتقال شخص في العاصمة طهران قام بجمع وإرسال صور وإحداثيات لبعض المواقع الاستراتيجية والأمنية في البلاد إلى جماعات معارضة للجمهورية الإسلامية.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88039" target="_blank">📅 10:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔻
إنفجار لغم في بادية محافظة السماوة جنوبي العراق؛ إصابة منتسب حدود كحصيلة أولية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88038" target="_blank">📅 10:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88037">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇷🇺
الدفاع الروسية:
دفاعتنا الجوية دمرت 791 مسيرة أوكرانية في أجواء عدة مناطق روسية خلال الليلة الماضية.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88037" target="_blank">📅 09:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88036">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي:
تم إطلاق صاروخ اعتراضي نحو هدف في منطقة زرعيت عند الحدود اللبنانية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88036" target="_blank">📅 09:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88035">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
🇮🇶
مصدر إيراني:
قالیباف يزور غدًا العراق على رأس وفد برلماني رفيع المستوى، بهدف إجراء حوارات حول التطورات الإقليمية، وتعزيز التعاون الاستراتيجي بين طهران وبغداد، واستكشاف الحلول المشتركة للمساهمة في تحقيق الاستقرار والأمن في غرب آسيا.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/88035" target="_blank">📅 08:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88034">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By6N0LLjdT6chtp48bZ6IcLCwgBJEJCM7f1RIYAVnBSIs75YuxufSLaU0UMGh3di5vb5r9en95Z88b2TrdYlTUm0gYz8Es6LrdKqliG2KaedVOJxXBhliMeofJyE-ckKK8Y7tZkVAJzpWimx0fYMC73ZKWhRvOFSwpy-bFZzGtnRgYgDw0wRZgGVyP-lXrP5SI8SazvngV6ND07M1vMqNf7g9ofP2ijHCRaCdsMx7-B4ozE0bghxzOu_p_kQPGK3p1zL8ttLGxtvciHNd21r1oQ1pX18-VHE5VCBiqSdf16FTx6sE6TkYtknCbC4NH12RVIYWHHCDLS8igG2znYDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جمهور فصائل المقاومة العراقية يريد نسخة عامري الأهوار …</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/88034" target="_blank">📅 08:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88033">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇮🇱
🇱🇧
انفجار عبوة ناسفة في الجليل المحتل مستوطنة المطلة اصابة خمسة مستوطنين كحصيلة اولية ..</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88033" target="_blank">📅 08:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88032">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044201b963.mp4?token=UYs6oWR63JBhkvZeTZcSPjIATiAtHlqMCIbSUA9bJyQlazaE9z-MH7rJN4bKsF4_ExuSK8Pay5NLiPLctq3i4WCSFqpYHgeLbBxeMMRpRtbiCYKKcHsUKc9sM65XJ9aYNpZ4M-2SlJRUPLAdN6HJIUZx99Q5uI4JAmhV_meCnnE2NZ7S24JQPoQPO4MfRfbdFYt0pVu4A5PgZtFteyYLzwJ9l3xqifey4OHYytPJxzB113vlXgyB_p3HRc0F9SF2EkdhLbOkqrEL6yTSLj1nehFM8iVsh6CA33By0wHDqYlpXd9JJesI65VBCVe9RKpWjkufCCQanHtZnfZjZqvMxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044201b963.mp4?token=UYs6oWR63JBhkvZeTZcSPjIATiAtHlqMCIbSUA9bJyQlazaE9z-MH7rJN4bKsF4_ExuSK8Pay5NLiPLctq3i4WCSFqpYHgeLbBxeMMRpRtbiCYKKcHsUKc9sM65XJ9aYNpZ4M-2SlJRUPLAdN6HJIUZx99Q5uI4JAmhV_meCnnE2NZ7S24JQPoQPO4MfRfbdFYt0pVu4A5PgZtFteyYLzwJ9l3xqifey4OHYytPJxzB113vlXgyB_p3HRc0F9SF2EkdhLbOkqrEL6yTSLj1nehFM8iVsh6CA33By0wHDqYlpXd9JJesI65VBCVe9RKpWjkufCCQanHtZnfZjZqvMxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
نيران لا تتوقف من موقع الحادث وانباء عن قتلى ومصابيين داخل مستودع الوقود في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/88032" target="_blank">📅 01:58 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88031">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba96102ee.mp4?token=BihqvcyK2duBxF3q0j07dEtI0eCY9ym-a4naotcWzLKf8idQX8Vae5eqKrAG-xoMnT9UuNGOiHAyntlq2qeEPamLZfFVY98kBwJtqR5LKpkRamFliwe6WW4WfDByO38Zgcp9ZfrKZ89w71Val2yFW20xXyeALGE5MH0d6RYjlyK2TuhbHDxinaIaynAYptnWs4Wr33tjB7LfjTOzvEjpEVtfgtOuyu8-0pCFYGmtbs4DVhhryu1ebzehp9BajMSyu9-6XWydCie5wkBuFD-H47HTFz3cqI3Y3js71KieNYYX_JC9U-LdlJTrYhk_reR5BhEKFharqOoamrC3pZ77zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba96102ee.mp4?token=BihqvcyK2duBxF3q0j07dEtI0eCY9ym-a4naotcWzLKf8idQX8Vae5eqKrAG-xoMnT9UuNGOiHAyntlq2qeEPamLZfFVY98kBwJtqR5LKpkRamFliwe6WW4WfDByO38Zgcp9ZfrKZ89w71Val2yFW20xXyeALGE5MH0d6RYjlyK2TuhbHDxinaIaynAYptnWs4Wr33tjB7LfjTOzvEjpEVtfgtOuyu8-0pCFYGmtbs4DVhhryu1ebzehp9BajMSyu9-6XWydCie5wkBuFD-H47HTFz3cqI3Y3js71KieNYYX_JC9U-LdlJTrYhk_reR5BhEKFharqOoamrC3pZ77zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
توسع رقعة الحريق بعد اندلاع حريق مجهول في خزان للوقود في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/88031" target="_blank">📅 01:57 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88030">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d70a886426.mp4?token=YDnz_VvL6skFyKVijU_9r8INWNn0z7klYitzhOtvhJeBYe0w1QyZkrSSwblbYONtmt6xFejO04Rk3xViuMmucpHy62du5Da4f7V89AsBxLnQCrtdwuPr6cSK89xHvQCmJ9JClC2GQX0fSy4UgADVBTWGQEDFjtcpuPdVLFa0oSfL-Dsrg2aS5DxE8WBKB7UROJoyzQb25MYWsNHb9B516u3acJyYBE87-QG54y7q3EKBhIPh4V2-08iJ1UZTfuS2mmknQ0M4KtgrG2QikO14HW1nUIeCgeMWwmuLp6lxpKyzUaRzcU3XPJnl7BrculRC7AEaSLIDdwkCsvk5INuMdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d70a886426.mp4?token=YDnz_VvL6skFyKVijU_9r8INWNn0z7klYitzhOtvhJeBYe0w1QyZkrSSwblbYONtmt6xFejO04Rk3xViuMmucpHy62du5Da4f7V89AsBxLnQCrtdwuPr6cSK89xHvQCmJ9JClC2GQX0fSy4UgADVBTWGQEDFjtcpuPdVLFa0oSfL-Dsrg2aS5DxE8WBKB7UROJoyzQb25MYWsNHb9B516u3acJyYBE87-QG54y7q3EKBhIPh4V2-08iJ1UZTfuS2mmknQ0M4KtgrG2QikO14HW1nUIeCgeMWwmuLp6lxpKyzUaRzcU3XPJnl7BrculRC7AEaSLIDdwkCsvk5INuMdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حريق خزان وقود في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/88030" target="_blank">📅 01:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انباء عن سماع دوي انفجار في محافظة اربيل</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/88029" target="_blank">📅 01:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88027">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🇺🇸
🇹🇷
‏
الرئاسة التركية:
أردوغان أبلغ ترمب أهمية مواصلة المحادثات مع إيران.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88027" target="_blank">📅 01:09 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88026">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف: ننتظر من الإخوة الكبار وحكمائهم العمل على تصحيح الاعوجاج الأمني الذي تسبب فيه الرئيس المكلف كي لا تبقى حجة لأحد، ولضمان الاستقرار وصون الكرامة وعدم الانجرار إلى ما يسر الأعداء.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/88026" target="_blank">📅 00:40 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88025">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2ulKireePSMk0Yt3e85bh4cVkyHyUI4dQDeY8SrEJXR3Ia7NSCuohA2jBpBfI_eWiSaGIML-pIAK4T4DiW9syV8jze-qS36vQIb9gmCIuJvucECScFf3V9dcHV-EK0bQftEPJDRhLAq6jDJEjCcHbMr69b8H92zTMo3S9vJCxszhpp07r1BN6lPjYU7dYzknJX-JUwTxgrJPI3cgQ4voKTGYvB8OLl9gj3uFsCLs-M3bZLtyYR1DkKS_sCfSGzUlUKVQpSRHCNCPGqbF-FcXnuG6lcqshL3iO6LX3xxhcGhbtlqgUv20tH78EBeww5ptReG6WYF75G531KE_MCWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الحاج ابو مجاهد العساف:
ننتظر من الإخوة الكبار وحكمائهم العمل على تصحيح الاعوجاج الأمني الذي تسبب فيه الرئيس المكلف كي لا تبقى حجة لأحد، ولضمان الاستقرار وصون الكرامة وعدم الانجرار إلى ما يسر الأعداء.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/88025" target="_blank">📅 00:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88024">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/owebqe0n9r9g-buGrnCI0sq7tGDw17nRh4jSqZ34kZL1PobB5QflwW-TIPZfcgRp0DF8tHOXxPQj8KXAH1LqoSguYi1_ju1jRvM5hBK5G_wubrczDS3HvzFt2jmfmVTbtX2nDnmzPJvTnUjPL_QjUou6KnpQYzg7UP3H4wVFZJf0O9jmvmMEVklNXhS-LZOhtROk_uLkqTfa68UgLZ-Iq5IBmxG1-BxX5SlaaM780adl_DGHEEPCvKD09GypLL3gfPzkB3406_ltb6ljMKqcLeH2idMwxCjxNE2n6gv_NQK2uJP6rBYUlVLmefAVm88AZGyYWMq4SFhOfjoPaV08lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">يوبخ ترامب صحفيًا من سي ان ان: اصمت! أنت تتصرف بقلة احترام أمام هذا الشاب. ألا ترى أنها تتصرف بقلة احترام؟ إنه يفهم. اصمت! أنت تنشر أخبارًا كاذبة. اصمت! أنت صحفي مزيف.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88024" target="_blank">📅 00:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88022">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02a9f19058.mp4?token=a3Dv5NCh5XCaPjj2PGsn85GE62baz08aEL9dAl3rxxEC90F1xWMIdYwbK-7VnXFQUL3kZ0Pn39UGPFe0aGFmSgHX1c4IjBHv6q-oA8FVEi6wH1226Bu98SqrfKo-p3sRV5f4hl8qWRYBLpfq6GyUBoPcIlPCOp1BoRlDD_Cxyj2GJvxBzy1jKHG1AQtwkMnbYB9Hlnks-Ir5SEhcSK4JoAUomMPlqr2-f_xAMC276MWgdWczuEiewz6lIChIncuAQUFLA_YArnBB8obkMeleSLc9F9Ds5OIHXG_fSDN1cuE2Px9dW9oS7obR6wbshKDfCcxJYR5ylmRfLDe7H24f1o2A8F1bnvo6nbaf4T6HaS2l930N08MJ9Q4ePCXB3kqgV0O_1HlVZU3924c_0e2bqWf1VXVzM3LquaLoYYOJX8c_rPv98EpcZyxnlQE4LJSUWbmbVuJqgc4-bVJXfRkgcgCzmKm2UbPsTQzqq6fsATDGX4O1IHZdEaEorrlwSKajbG7StJcSYK83QecI2nhZnf8rK6946QWM0kfW1AUk-wlWtgWQdHpK1OJyvc3Q8Auhr2H0dvzLUZ8g99RGqOAXY9OYsxG4j8oSi678xxC6ynl9H3rDujWM83mIOTHTBRP0CeEN5-OB09pBxhQWjxVBDG2uNjRl0QI9sLpCA6K5DUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02a9f19058.mp4?token=a3Dv5NCh5XCaPjj2PGsn85GE62baz08aEL9dAl3rxxEC90F1xWMIdYwbK-7VnXFQUL3kZ0Pn39UGPFe0aGFmSgHX1c4IjBHv6q-oA8FVEi6wH1226Bu98SqrfKo-p3sRV5f4hl8qWRYBLpfq6GyUBoPcIlPCOp1BoRlDD_Cxyj2GJvxBzy1jKHG1AQtwkMnbYB9Hlnks-Ir5SEhcSK4JoAUomMPlqr2-f_xAMC276MWgdWczuEiewz6lIChIncuAQUFLA_YArnBB8obkMeleSLc9F9Ds5OIHXG_fSDN1cuE2Px9dW9oS7obR6wbshKDfCcxJYR5ylmRfLDe7H24f1o2A8F1bnvo6nbaf4T6HaS2l930N08MJ9Q4ePCXB3kqgV0O_1HlVZU3924c_0e2bqWf1VXVzM3LquaLoYYOJX8c_rPv98EpcZyxnlQE4LJSUWbmbVuJqgc4-bVJXfRkgcgCzmKm2UbPsTQzqq6fsATDGX4O1IHZdEaEorrlwSKajbG7StJcSYK83QecI2nhZnf8rK6946QWM0kfW1AUk-wlWtgWQdHpK1OJyvc3Q8Auhr2H0dvzLUZ8g99RGqOAXY9OYsxG4j8oSi678xxC6ynl9H3rDujWM83mIOTHTBRP0CeEN5-OB09pBxhQWjxVBDG2uNjRl0QI9sLpCA6K5DUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلية الاعلام الامني:
نفذ صقور القوة الجوية بواسطة طائرات F-16 ضربتين جويتين ناجحتين ومباشرتين استهدفتا الموقع المحدد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88022" target="_blank">📅 00:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88021">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXbhZnS-dCKoI7ydR6d6RGvB2QoOMAvHXNYpaBHYpaOaDB26XksuAv9CVy689J5Q1B0-3Zzavg0NI4wy7PZ7vKQnA7Ay91FmArKZxniSMGYw7VqRa2NfzD9XrUTu7YRM4QH3j7vg7EWaviLgqALV7SQ6cEOc5C023VEy6g6o5f9jlLe7HOwWNS7r7ShZbKgE8Y-eNaxeg3qhmysYDt3lIDld_o2hx1KMJPuEKp6vNV0FiLefD51sVsUMzuO_hG4Pu2RPJbLFSyhUwiB5WUCV2o7EFwt1vf5ffRVhYAMyqur3lGvCDenuMR0_RGkFuJyLlm26XS315JrCPRP8UwT2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب ينشر:</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88021" target="_blank">📅 00:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88019">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb50f87ee1.mp4?token=ZSwMXZXOXM9MQbNLqo6o0NuTHw3UYbkMieCugzaLjCmX8ghKUWpW_Gs7k1b5PVZ8f-YeXRKral3-dd5Rkgs3gIwqkR2GySdOSHlqMUODjcfIc1DnHMQomphH8eR_WbueDwqzH6T2L0FJxZo8FcASFFQA7GG3xT_K_vVC3Sx2jj3tXptOy1SIWTdPIbPSGIwR5hED4XOLmh6ae6-zQ288HB0MyNYIYCvgSNp2W6h-gU21LWOWLoR5soLKwcxkHOP2YK4ASVRqeWoTac821PUB1SgJICdu4IirUyNIvx4rPVGyIk7pDdU0AyyiyJU4An728bWFIqYrUl52J1RG5zessw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb50f87ee1.mp4?token=ZSwMXZXOXM9MQbNLqo6o0NuTHw3UYbkMieCugzaLjCmX8ghKUWpW_Gs7k1b5PVZ8f-YeXRKral3-dd5Rkgs3gIwqkR2GySdOSHlqMUODjcfIc1DnHMQomphH8eR_WbueDwqzH6T2L0FJxZo8FcASFFQA7GG3xT_K_vVC3Sx2jj3tXptOy1SIWTdPIbPSGIwR5hED4XOLmh6ae6-zQ288HB0MyNYIYCvgSNp2W6h-gU21LWOWLoR5soLKwcxkHOP2YK4ASVRqeWoTac821PUB1SgJICdu4IirUyNIvx4rPVGyIk7pDdU0AyyiyJU4An728bWFIqYrUl52J1RG5zessw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
القوات الحكومية تداهم منطقة العمارات الملح في محافظة ميسان جنوبي العراق بعد اندلاع تظاهرات تطالب بالخدمات</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88019" target="_blank">📅 00:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88018">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سيصدر بعد قليل بيان هام للمسؤول الامني لكتائب حزب الله الحاج أبو مجاهد العساف.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88018" target="_blank">📅 00:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88017">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
ألمانيا
: هجوم إلكتروني على وزارتين في حكومة ولاية برلين.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88017" target="_blank">📅 23:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88014">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOUxYnC86k3YKNqd1ajJoL5Xo_cVTt0FwVbuVU12fGLyH9uMquwC-VM5_8BRz54zxqwXo_WZkeCfwAj553vZowGK7Kvt4MEblW0fzmNPcyfjpk5OvzQRTaxrC53iyR4nl-YlID9bFmGPY-asGed07TlaS6NuuTwvt6rnA0AVmaIgkMZ6_4DWZ_LZmU8HvXFjVE_MZKK-pWGKEnnHXjrTcZ71lsSuUOOndO128m2PvkF0OzYBzjZ-oLRiYMvgHtaFa-yaBBfH6e1Uj-SqEyA7xYocdW9E-eYBfM662NsoMbOTSzQGeYrzYw2A2ECYK3bpXCjtgtUWR90Gg4q5DNZrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azQirVIbuyzV_-DhJn-xkU1TucxH8JiVDf9TFJOg_jWEOOc9uaZc_GztfbM1QQxgrvWri9IOkrZeee7qiwAuCp_dss4C2t7bdiNIblVpVCfxvYUmPCYGCEHUXuitMozid9mrNT95X6Qv0oJD7ptLo1y7NJXo-iYRRXuojuhYzye_71omMom8r6tVn5hLhEdY-x0IeApCinZiOi6cHiCM8Aqss7zrIoxtACqj5RKKMnZ5FXEilc931DuS_hUeZk7osPaGY8oMaLhROOxAUQbwl9K5-weMNIAOnXtRpVDYUfGuAgLmX0YwuRH-u6YWHg0G8KZPU-P942JJVQBlKD16Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NEsFV6t9eJf0MEFeVNAInJS5lnz52j1Cs91iDkJP7ZXq4g1qOwUHJQyjsnKemyZvLjl04qOs34Mkquf0nFQcb69SdYwcLNktshrHbx1SFOHZ3mBPPY8dalYkK3zySvRGUlVGqyqEvfATa2PH_GpI4UwTxyWUOjXmxZNas8J2-3s7EusZi82zv5Vjh5zEmEBpPEwk2x2o1CoOge6LCq4xurI6zaKGLak2lEIUXf17Khv80PsTtE6xvTmG9SgJ_3ChknH3APWFxDC3-cemWFJFmC9dqcLEFilpumJf15ekqDNpuRZy4fiWSi3bVV7Jx47TG9iehE5NpirfyQ9QpptMaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امتناع عدد من الطائرات المدنية عن الهبوط في مطار دبي، واتخاذها مسارات دائرية في الأجواء، لأسباب لا تزال مجهولة.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88014" target="_blank">📅 23:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88013">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏كوشنر: محادثاتنا مع إيران إيجابية وفعالة لكن لم نصل لتفاهم بعد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/88013" target="_blank">📅 22:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88012">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY0hMvXjQzE9mcNSbPVs6yCa8cCHI2JBwDrtJHr3kwDXKKZkOCUFPG6Y3iVDL-lJHtK2hrSk7B6Y8YvsDZVG4IMb5wB8ha0p2V_2_PfmirFG9LPX2LOuRm7r7knROrElMOPtQdQvxD9zE1S2wuipUAQlNA9fRAYcCb0ShIcGM0L2KZrrM_OzFhF9LlrDz0v7YDc9HXc4O5cO2onc4INV19YCQhd1WYh9xixDscDeSdsz7M0JDlsAc4kWboAIeDM5GGkf3rTamzgpMRBJJxC7S8jVh-fUqBe4YsuwkwA4pnvqeerNZLqxUGYt9OSc4JZvsn6_rpddZkzoB5EJVLahyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رويترز
: العقود الآجلة لخام برنت تصعد بما يعادل 2.65 % مسجلة 90.87 دولارا للبرميل عند التسوية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88012" target="_blank">📅 22:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88011">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt6BxsHWXx53l9hThsJubZZ6sECMgreHaPOwUTUDQKrTB4NnisgjsMQWEC1x5gR13j4a5P_EPFLPTzgCDNkAFOv5kvTQ_2KgJyKCkVN3I0VZ7Sqkk2Qh75irjpIyttpT-lPL8xVK13rye3LoY1mgdKBy_6e8NZGonC5ao7E2dqPC68eXGhFkWqNGZON_8BoP8e1DB0WOigmn4b7B44O7KlUcaUCEeslba4jZqnBPKs3K767qkAWCsPl1wBeDfLaLueoK3mFpOrpn8JwBKqXSpQCZIXsipOxfhxIpNovSrKd_Qxm5kKcy7PQCgeWjQabuTkiuSWeLryLiYKj1SvJkTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي
: لا شيء يبرر الهجوم المتهور على مكتب رئيس الوزراء بارزاني. يجب على الأصدقاء الأكراد توخي الحذر من المؤامرات المفتعلة التي تهدف إلى زرع الفتنة بين الجيران.
لقد حمينا أصدقاءنا الأكراد من صدام وداعش، ونحن ممتنون للأمن الذي وفروه على حدودنا.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88011" target="_blank">📅 22:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88010">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def859cee1.mp4?token=Ee8N0AZzygQJXZ-10yVAjg20xIx56J1CpsePH4xeCVDsQzji3UgppUXCiIpZyHHD_wj2HSKLbklWwAYXrK-ryeNepb59BHJLPdElZICxAhJ4YJ1vHrYcGpu3ZrNgScXcsncL8Vhe1UkQBwmymo791vHtYUHMbtgLaaBy1IJXatsFfOzeMk4T_7_yqYnuICuLBRXntQydHbKG26Q5HgVQFSda_CiX1s17X_3xdhOl6lXztwbOLpJROfXxAXAWeomPBxc96x2-1y6EkgQKJ41ayZughF5vWWxVWDK2XkVLXtDkltAfm-JBuQ24QsS-pFiFkscZ3quggQa9rFk7SQ8WdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def859cee1.mp4?token=Ee8N0AZzygQJXZ-10yVAjg20xIx56J1CpsePH4xeCVDsQzji3UgppUXCiIpZyHHD_wj2HSKLbklWwAYXrK-ryeNepb59BHJLPdElZICxAhJ4YJ1vHrYcGpu3ZrNgScXcsncL8Vhe1UkQBwmymo791vHtYUHMbtgLaaBy1IJXatsFfOzeMk4T_7_yqYnuICuLBRXntQydHbKG26Q5HgVQFSda_CiX1s17X_3xdhOl6lXztwbOLpJROfXxAXAWeomPBxc96x2-1y6EkgQKJ41ayZughF5vWWxVWDK2XkVLXtDkltAfm-JBuQ24QsS-pFiFkscZ3quggQa9rFk7SQ8WdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يوبخ ترامب صحفيًا من سي ان ان: اصمت! أنت تتصرف بقلة احترام أمام هذا الشاب. ألا ترى أنها تتصرف بقلة احترام؟ إنه يفهم. اصمت! أنت تنشر أخبارًا كاذبة. اصمت! أنت صحفي مزيف.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88010" target="_blank">📅 21:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88009">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8452420aca.mp4?token=HC-mAktWj8HdhlwmHMuuzF_dCxsFmWAxuRSarXQfuQfhAWXAIc6ua2dPM1wHdZ1tCasfdMwSyctqL_tzQWTIVmB1wzVeFZrA9zlHGr5w6TzOax02B1_yWGZaQ0rkm8dl2b2nlMW8QDJa9VPxk5NW6qqcf-kpyueOBrQlJWjG1akRsJDOVSjwKMnfy2rqMyyrYpY8zz-uv3393OLv5DwiYmz5lV9VmBmgocOgRTNIRqCR_HZZfM-gkZjDrIiBASlCdbyOP4o3-tIQCdfz5UWn44saLFSjPx4GEfEPwS-0wB_05_7pWiY2pwdFbNMg6jxfuTUOESX59Nd_Rw7f_jhWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8452420aca.mp4?token=HC-mAktWj8HdhlwmHMuuzF_dCxsFmWAxuRSarXQfuQfhAWXAIc6ua2dPM1wHdZ1tCasfdMwSyctqL_tzQWTIVmB1wzVeFZrA9zlHGr5w6TzOax02B1_yWGZaQ0rkm8dl2b2nlMW8QDJa9VPxk5NW6qqcf-kpyueOBrQlJWjG1akRsJDOVSjwKMnfy2rqMyyrYpY8zz-uv3393OLv5DwiYmz5lV9VmBmgocOgRTNIRqCR_HZZfM-gkZjDrIiBASlCdbyOP4o3-tIQCdfz5UWn44saLFSjPx4GEfEPwS-0wB_05_7pWiY2pwdFbNMg6jxfuTUOESX59Nd_Rw7f_jhWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: هدوء، هدوء، هدوء. أنتم وقحون للغاية. هدوء. من معكم؟  الصحفي: أنا من شبكة سي إن إن.  ترامب: أنتم تنشرون أخبارًا كاذبة. اهدأوا، اهدأوا، اهدأوا. أنتم صحفي كاذب.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88009" target="_blank">📅 21:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88008">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311dd58f45.mp4?token=OolYRq31ooNpIi8kKaYgc9b2BJEcTKHOO93JCOCw-VxlzScoV_wwqDRPbflDIc2n02TEJiG0yfL_F3aKzTz8qcLsdhWwR-Ehz45SEqkLFbx8-cqQcWXKJOA32e43M7FAHFaPm3P7ldkW3tCBDtI2rsYhoMQL-gDgjnh9ELCj6LUYNqI6oxnBMY_DZy1DnPY-hXwQWLNE2zy_Cu-L6H40epm9wnff1QYf9LNOPDsOQBQZ0HkZQPHoIGMhouXrLPVpjg2atRsRz6TAfaXj08XJIhlnV300g9ibtea__iOsFeqANRJjrKi9ZnmgPrDtdyowN7QVuY_1jt3le_iYTjugHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311dd58f45.mp4?token=OolYRq31ooNpIi8kKaYgc9b2BJEcTKHOO93JCOCw-VxlzScoV_wwqDRPbflDIc2n02TEJiG0yfL_F3aKzTz8qcLsdhWwR-Ehz45SEqkLFbx8-cqQcWXKJOA32e43M7FAHFaPm3P7ldkW3tCBDtI2rsYhoMQL-gDgjnh9ELCj6LUYNqI6oxnBMY_DZy1DnPY-hXwQWLNE2zy_Cu-L6H40epm9wnff1QYf9LNOPDsOQBQZ0HkZQPHoIGMhouXrLPVpjg2atRsRz6TAfaXj08XJIhlnV300g9ibtea__iOsFeqANRJjrKi9ZnmgPrDtdyowN7QVuY_1jt3le_iYTjugHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: هدوء، هدوء، هدوء. أنتم وقحون للغاية. هدوء. من معكم؟  الصحفي: أنا من شبكة سي إن إن.  ترامب: أنتم تنشرون أخبارًا كاذبة. اهدأوا، اهدأوا، اهدأوا. أنتم صحفي كاذب.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/88008" target="_blank">📅 21:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88007">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d95f5147a.mp4?token=M8MqsDec3kPx-T28-bKmPAyQUgAIymcY6RYiMGUUGeJ3plxPOP1lMfgR6tKM12tlT5K-wRqDsh-315hbbNc0F8AWhbjwh3bZYX1g8Go1jkY6CahN_a0G9WJOz16dbYXYoIXtawm_eE2An6e_aXu_1M_q3FkiG3Fr6seX4smdHLewWKuY48lYfTyZrIAL3JDiOsutAqF0IinnTA_uQwl8MyKnWbdOfsVpRh3CmrWBGdWMo9PoLvqcGxDLwWxuKdPrhWjVPtCHk7zB80kR5uM2wfj8b1uY_JThcvPZWYUxwolOSwJfHZnOxX81i4-ZUWk7pptfaq2sVdL8sOf9r1WBwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d95f5147a.mp4?token=M8MqsDec3kPx-T28-bKmPAyQUgAIymcY6RYiMGUUGeJ3plxPOP1lMfgR6tKM12tlT5K-wRqDsh-315hbbNc0F8AWhbjwh3bZYX1g8Go1jkY6CahN_a0G9WJOz16dbYXYoIXtawm_eE2An6e_aXu_1M_q3FkiG3Fr6seX4smdHLewWKuY48lYfTyZrIAL3JDiOsutAqF0IinnTA_uQwl8MyKnWbdOfsVpRh3CmrWBGdWMo9PoLvqcGxDLwWxuKdPrhWjVPtCHk7zB80kR5uM2wfj8b1uY_JThcvPZWYUxwolOSwJfHZnOxX81i4-ZUWk7pptfaq2sVdL8sOf9r1WBwoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترمب: سنقوم بإنهاء الاتفاق مع إيران.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/88007" target="_blank">📅 21:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88006">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4d_yw7VlnwJF6vUsUnQCHQtd9Yo4QxM29yMZs4qu-FCz44uqEKk7eKCz-TFp4fsFlkosiBaJHefztY87EbLWxgP0MIxKITrtIHmjs9m9iNqPazr0Rx6n4GlaBMvK8VWhXAiUcnfpJgJ3RgNiFt-ZMMqI2hFQwxbw0k1y2M6UmmAqdbXSv067nhRZkhI3ovaZfeHF6TYl7W2kAK66d7lVUbURXHhdEhD7GBfAyj9x213YC0z10fl0m7VXvwiWkNbNFFMmrmqs5KriF2OkRQMhG7qA9Hto5xIidepPNDIoG05weSo_tbsHa9k6opujwOcDrAE6FEsam7WWx27t4zfRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدر لنايا
العامري في اجتماع الإطار التنسيقي كل بنادق فصائل المقاومة في العراق هي بنادق بدر قبل ان تكون بنادق جهات محترمة بالمقاومة …</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88006" target="_blank">📅 21:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88005">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
ترامب: قال لي رئيس جمهورية كوريا الجنوبية إنه يفضل عدم التدخل في الملف الإيراني.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/88005" target="_blank">📅 21:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88004">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
ترامب
: قال لي رئيس جمهورية كوريا الجنوبية إنه يفضل عدم التدخل في الملف الإيراني.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88004" target="_blank">📅 21:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88003">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOizaZnOyRnv7QitGkfPHxavCH92LBhJQvvHuoLXm_DHXFlMFDFAGIGEkYTU7bN1GIJmd63nMGO1vflu_TeA8-WhWjWqQusZRWB00pG4Ugr_LL02YkiFiX_5CfDyNUMJn6bLPH4b0ccSfCniEl4FH1oOn_gHLowB-NggKrjcf92Ko4kJB9JYIIkYS65v4QCSSh-KqiSDo3MnxVwYxlH5du6YKwUU9DQO8LAH7UAY_gQwNIMTuG88FMznU5twYvBFRxyHP-dZW93mPMuOCsFT2ZMRTDgBSTtJYLFABiyu7hhUqVhO6yB5WxWUB5Jh4OGLmwHr0Kn0fXDaTahh3LTeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وَدَّ الَّذِينَ كَفَرُوا لَوْ تَغْفُلُونَ عَنْ أَسْلِحَتِكُمْ وَأَمْتِعَتِكُمْ فَيَمِيلُونَ عَلَيْكُم مَّيْلَةً وَاحِدَةً ۚ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/88003" target="_blank">📅 21:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88002">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7AxmeJNVVG_fDizDbA9wjY-ZWi1C53A0EhFXXMs0iCNny_P33wQOqjPav_vBHi_7QI0ol9kxqpvPz_1ydLq1775BQlbnJauR7jdJNdxZ6wMBnYCaaDRjOf_yzrzTZY6jXItO0mnshmIdYmzWOpXBFgm1veEn260aAAl8RsuicLrlXhiagpik4LGL5gSsOUgsnvfGQoA_eeWVb_zkqFX51P-Zfs7OAuKuglvFpRhCqXCYfYbeClB9v2Z4FMTUFWRmX3WdyquP9rb2dZcDV0QnH_LdGPY_O5wXSmsBcLZG65Q-k15BkNWu6dc2mxkPiOGmWwMFsYqytJ4qaqzphHG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السيد مقتدى الصدر:
أكرر قولي على الإخوة في الحرس الثوري عدم ضرب الأراضي العراقية فهذا عين شماتة الأعداء.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/88002" target="_blank">📅 21:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88001">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">العامري يسوگ عليهم باجتماع الإطار من مكتب سيد عمار الان   العامري يتصل على ابو فدك والفياض اطلقوا سراح سيد عباس فورا</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/88001" target="_blank">📅 21:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88000">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPB3Y2kK9-89fmdagBTMbdUct24IdI7Pe74WeOOCDVvvIkYsxSxc37Z16NxYW12QZxiIZadVBQ2lQKmabX27EA_Tj150cAC1Z5L38HY1nsORbBLIhwyLhNSQKYSRsmSqS9ArmNeJlP-3dsaDBx5yqYo5rham7YzMlSLWka27wsiBAMfxjb890Jp9P2CJIlhHU2W6Ytsq9S5gcSFoKI0l7LjDIRTI9wffhE3CloFuufaZpuhkGpq66g4BuLl-J0lMn-32LGzlxlSz3oh2KVTyBU6adNZfCj73EbxcUrZFPEZObr01CzJD0yiBnEc9upxx206kzgQgFgmfchWTHU0d9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد قليل سوف يتم استلام المخطوف إلى أمن الحشد</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/88000" target="_blank">📅 21:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87999">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/87999" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
عاشت المقاومة العراقية البطلة وسلاحها الموجه نحو الاحتلال</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/87999" target="_blank">📅 21:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بعد قليل سوف يتم استلام المخطوف إلى أمن الحشد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87997" target="_blank">📅 21:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">العامري يسوگ عليهم باجتماع الإطار من مكتب سيد عمار الان   العامري يتصل على ابو فدك والفياض اطلقوا سراح سيد عباس فورا</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87996" target="_blank">📅 21:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87994">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLdDfIv4W9_D4SBqyWH3QA_PjDO3_dDRd_XxDZ528CXWL65HzfqqT-D_9RYz_xhAu8Tz3bPjWahrQY_gS2dNP2E8tGPISl3PfF0Lm0PrJCh6brrYg9Kg6iQKQe8SUcGMJQ0kx5fIINF3WU0Z5z55ShmbY6fBGiwCsTUsApYaCC9HdPhZTFlypJc8EltfU3hDJEqFFPS7vs2rvX9RumMxtY2dz-7LF1Fyt_ISdx49MGzXPLfE9dQSxZscSZZsxjMiSfVckKYfB8z7zYF1HTlcm5JRvjBfTEsXs1fP81_HL9lsbHEGbAhYOvGBkHANqaSra1q3mBYdzdGabQqOEh3zHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f8d8b486d.mp4?token=rZLx7o5lf7qgQ-U46tpKcAByoiF47dQ8wiAR5x6LHYKWoxhXeCxWo6FP1adCYNqPEwX9BGUv06lXN_4w1ElOXJngoSlwP76RvoBva6g-r65MBQLK_adqrX-aDT20BodsfAIjKN89i2lgBbgCz-8bPnaiJiHWyvNTzRDVWuK2kLt6a9MalFjVlpH1SXaDdnhoS0lA47p0PeuJSWUkF6Fk_JYV92SOZaxQSygaJen0d_k-wqwjCV8qZaYG2j3l3_uj9lZ8SqzXXcnHkALU7RsZ2mpdR3uf8y8VAfyb7-ByCKOvPIzg81ckm-mX-zYGyuLY4hKg895Miju-TYizWhF_sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f8d8b486d.mp4?token=rZLx7o5lf7qgQ-U46tpKcAByoiF47dQ8wiAR5x6LHYKWoxhXeCxWo6FP1adCYNqPEwX9BGUv06lXN_4w1ElOXJngoSlwP76RvoBva6g-r65MBQLK_adqrX-aDT20BodsfAIjKN89i2lgBbgCz-8bPnaiJiHWyvNTzRDVWuK2kLt6a9MalFjVlpH1SXaDdnhoS0lA47p0PeuJSWUkF6Fk_JYV92SOZaxQSygaJen0d_k-wqwjCV8qZaYG2j3l3_uj9lZ8SqzXXcnHkALU7RsZ2mpdR3uf8y8VAfyb7-ByCKOvPIzg81ckm-mX-zYGyuLY4hKg895Miju-TYizWhF_sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
إستهداف سفينة تابعة لمرتزقة السعودية في  باب المندب بعدة صواريخ والنيران تشتعل فيها.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87994" target="_blank">📅 21:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87993">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">العامري يسوگ عليهم باجتماع الإطار من مكتب سيد عمار الان   العامري يتصل على ابو فدك والفياض اطلقوا سراح سيد عباس فورا</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87993" target="_blank">📅 20:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87992">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb1YiZKpAhBRM38Ro--wvwsKjSbbrfZzK2bvvcBoi8UBEylfy_BThycsMMtMoCY87H4gGDV99K8ZlYJUUmaFzqkqQMN7Y71j_HQJA3lCCCe6BDhye4MxaYkEXM9qc-Q8067mbjiBbPwXZ09514jk0Dgt_iR8bpV8BgWy1-WFaSAnWhoPNStPfz3VX2eLib9CT8ObS4M6DqmzWFjoPNghnxjbB11MxWZoPHHBvsB6N1C9ONpnDpf0vegend-ykUmFuML7bpDzno6ewBsZJkUQWjFMWHaSTEmN5t2bpc_IEhHsis-xXNUM_GEEnNJG4N1mcnmfhWp_MsBzxoGneVsy9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العامري يسوگ عليهم باجتماع الإطار من مكتب سيد عمار الان
العامري يتصل على ابو فدك والفياض اطلقوا سراح سيد عباس فورا</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/87992" target="_blank">📅 20:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87991">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/031b28e167.mp4?token=kdqdZReEY2_ecgCYDHc94rHHtfM-9KvTlaiAjsHn5ioGK2b8-p7qIY-u4JZ6xD2NnvzMlr-SBvGgZUw3VzNhrSfDlHD14xi_gjeC_m2IhUzKdGbBb5u8_fVOWV_FO0HaMNAHd-4lRcsEXXF60iwn-vSWcJdIx5IbDaNXfkDM2oQya67ACJfQwXWAWLLMcGXONyet2usANQOx7T4EYPlbKTcW6EsIdOR39itChT8_SnSaEkNeZH7wDvC_86wFFm03__N0DhhZDgG5BZDRtjn44rqSgM7uJBUSPIElZDNKxPRd7pQ9ITfwKp_xD5Y67aweXCvUGMUVbYMR1EU-iT38rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/031b28e167.mp4?token=kdqdZReEY2_ecgCYDHc94rHHtfM-9KvTlaiAjsHn5ioGK2b8-p7qIY-u4JZ6xD2NnvzMlr-SBvGgZUw3VzNhrSfDlHD14xi_gjeC_m2IhUzKdGbBb5u8_fVOWV_FO0HaMNAHd-4lRcsEXXF60iwn-vSWcJdIx5IbDaNXfkDM2oQya67ACJfQwXWAWLLMcGXONyet2usANQOx7T4EYPlbKTcW6EsIdOR39itChT8_SnSaEkNeZH7wDvC_86wFFm03__N0DhhZDgG5BZDRtjn44rqSgM7uJBUSPIElZDNKxPRd7pQ9ITfwKp_xD5Y67aweXCvUGMUVbYMR1EU-iT38rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
طيران مروحي مجهول يحلق فوق العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87991" target="_blank">📅 20:43 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87990">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الاميركية في بغداد: إن مثل هذا العدوان على حلفائنا الأكراد الموثوقين أمر غير مقبول.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87990" target="_blank">📅 20:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87988">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjzoofGMM7sq8rlFHz28kfURtGmAtHtW92pfnr4o8iScGIzkyxLVqNds5V6JcEABw-0mcnHoSiVgqbCK8xqJQ86BYhV-5c340rI3QcJAzC89xn5ae28Oe4ttuuwbC9cJ1Z-FSAkpuv3hz3pJESroCmYIKvIyPk8zf5aBs5npSA4LNkgySqV1kjhQXvvBdBM-oIWwToxt4_br7b4eSwZmKNw824N3Sd5bGBwv4GPac0u2uEvpfHiDbjEUHGzVJb-y27Mz5NBJmJ2evprTz5d8hoj1gGeEQsVVHL06uw70WMzXTwxoX3MPw4mRr93WBx7dWnS1I5_JDFYDD4mpfUpmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f99415a6.mp4?token=d7XMae4eAPMNRm0WIZEDb10T5Lvcru1FGlsB_wbkucQxxK5eGpfl2p3xbVBdwsH2O_O9uAxPwBnCPYUjer--J6Fn2CqfWt3y0v8bsUeB4s7Y2_l0dkvuLiQD2u--7NnmtyHxepHYy4IYqLoze_AxmN1MLgC653cfSXfQydx1WQOZiPQTnJhmI5s_E0uFV-r-0h_1Zk2Aaodjb214g8S93gPPwERFxoBWf1qoTMzyC6EaLmi2reNJOMwzaRUMJsG8GigtLSJeUVsPxvQeL3srGSUI0R-mTAn6efkT4BykGZRElOUhvwWsbxm2b1q95Tf3DaPCLSEAyrJcovqXOBmlk4T1HRuinVYS01ut2mft34hAOfNtLnEQOAXZf8_blZleWUPnz5d2n3VpolhY2H-q3pwbndZNLi9LZCt17XkxcUvde8E6zpPZXOx-pwLrdFGdNk9p3_5Bo-dQexXPFM8cBF31cVhXkzBiqobakP_YVZJiYvVtYJmWIzx2k8xKoWFVPhLr6xltN2mi8rvadlB5h5VOD01SUV7YOZIYBhYPZ1-ARAFsj_fbr2fO2wgHYbaTxK2GokYaGwjt80wZFaX3dZJNeO4dIveT8rUjxhA9Zfc6ZkI__8zBrlJeYthH1H1mpCTstUbP1WFdrVLC4JhG97Glqq1RIalCUGCwuqjj7XI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f99415a6.mp4?token=d7XMae4eAPMNRm0WIZEDb10T5Lvcru1FGlsB_wbkucQxxK5eGpfl2p3xbVBdwsH2O_O9uAxPwBnCPYUjer--J6Fn2CqfWt3y0v8bsUeB4s7Y2_l0dkvuLiQD2u--7NnmtyHxepHYy4IYqLoze_AxmN1MLgC653cfSXfQydx1WQOZiPQTnJhmI5s_E0uFV-r-0h_1Zk2Aaodjb214g8S93gPPwERFxoBWf1qoTMzyC6EaLmi2reNJOMwzaRUMJsG8GigtLSJeUVsPxvQeL3srGSUI0R-mTAn6efkT4BykGZRElOUhvwWsbxm2b1q95Tf3DaPCLSEAyrJcovqXOBmlk4T1HRuinVYS01ut2mft34hAOfNtLnEQOAXZf8_blZleWUPnz5d2n3VpolhY2H-q3pwbndZNLi9LZCt17XkxcUvde8E6zpPZXOx-pwLrdFGdNk9p3_5Bo-dQexXPFM8cBF31cVhXkzBiqobakP_YVZJiYvVtYJmWIzx2k8xKoWFVPhLr6xltN2mi8rvadlB5h5VOD01SUV7YOZIYBhYPZ1-ARAFsj_fbr2fO2wgHYbaTxK2GokYaGwjt80wZFaX3dZJNeO4dIveT8rUjxhA9Zfc6ZkI__8zBrlJeYthH1H1mpCTstUbP1WFdrVLC4JhG97Glqq1RIalCUGCwuqjj7XI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
منصة دفاع جوي "باتريوت" أوكرانية، كانت متوقفة في حقل ذرة بالقرب من كييف، وكانت جميع أنظمتها الـ 16 فارغة.
لم تطلق أي صاروخ منذ حوالي 10 أسابيع.
قال كبير المهندسين فيها:
الصواريخ الباليستية تحلق فوق رؤوسكم وأنتم غير قادرين على فعل أي شيء حيال ذلك، وخلفكم، يوجد مدنيون.
لقد ألقى باللوم في نقص أنظمة الاعتراض العالمية على الحرب مع إيران:
لقد صُدمنا من عدد الصواريخ التي أطلقوها - تلك الصواريخ التي كان بإمكاننا استخدامها ضد الصواريخ الباليستية الروسية.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87988" target="_blank">📅 20:37 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87987">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEQWiMRbjUtVGnn-KWui8WtaO8TtsE40h-P_IgFciEyRoBU8TBQh6iQ312jhfewfU8e7AUzSg84t6glt2yylacg_YL5l5-htWoa-2_vsdAt8RAwc7AcduU0Mj5_bTLnWq7Wcux9xAD9evYu8IKOfsyVLBH7_MzjbHxGl2X1WRnJh1Xfm4dQYN9Er_1gfNN1pLDYyLTMWNSbkxQomtnE13zxVJtTP5syaA-SpqFHXOr9mivOmKnKCMgtOsVpEwMjXA_GGiPz7mVdORj91feb1AaXnabNVtZrNOYOSqh99CKNHapdHqhWEgD45aBVjNL2ZCee8Y4tEGASBMRTtk7zivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الاميركية في بغداد:
إن مثل هذا العدوان على حلفائنا الأكراد الموثوقين أمر غير مقبول.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/87987" target="_blank">📅 20:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87986">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoozeGV8XoV-QDeXWHzRjrLOlku6kHyitWfGWMcPuTsbvqtR9K0rJpBsM2xTTTJJAmV00rqudQJTxAh-40tox7sL4MzHTb4d79-V9J9nKxMiA8rq3nlIIZ5HX86oiWv9aQbPc7nouy5C-BOf3qXs2HTyt-LW-JG9AKxYsetbgk_lqetfLsz_3FMz4IfFWwHw4kXyeS1xp-QbGac0oAsJB-MZjhANr6dEqrJ7H3VW3PVlpXe3AqHTqiZTpyNF3AmI3qESbwQsHhxM8CfvM90btYlG0q_CD2AfGmkwWQi4nwpsfGONNAt1OR9VeWrVvhvBjBkZJZ1c93qDejVJxwIvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
توم باراك:
نحن ندعم بشكل كامل قيادة رئيس الوزراء في استعادة السيادة الكاملة للعراق وضمان بقاء جميع الأسلحة وقوات الأمن تحت سلطة الدولة العراقية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/87986" target="_blank">📅 19:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87985">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">الحرائق تلتهم خزانات الغاز في امريكا</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87985" target="_blank">📅 19:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87982">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlJQvX0OpVEArV3eaCzFfjayR3e5uUPhr8-WctmDfEPZjj1mgVzkI7GKIvsr0zaRKh-krBs2Um9UYAAYz8P79tr5ki38u1IVoNrVjI2w-sjgWEkTay2cmbgfKWZxMrunT4Vc932tp0Ss1959ALVdSge2hWPA_iZ4I8jao5smL_jIXCDMSAoeGI-sFB2hIz_lnL_m0KnnKTurEAcVo0fb1IPvxfZGMM__dWi-9fIQs2CXoBRYYJs0-hK7IsWmzBmbG6GZUoBeADV-z2K6XYdua6etyOLaSa-DjQQ_qPaA7eNjtGE5Hl2mpbIcYqPXBG1I1TDdD8iTzn0emQnp-mDpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGNZ-fzpQ6js3YX5IteB3zdBIZYq1npp2KkmPFZdcCCh6JiOEAU8qig-t4PZA7pgCN-7j0aZ1jMCDpyIa-bEGV6NzOnax-ohM5xGvdSMxeOBwbEc3zEREe-n54iV39DZGW7MIepWnilVQJtXXmA9atMjdL3rx7g41BT_IN56uGECfAfqj9a6fGFPve1v-ZN832SswbuT9kRu4dgnV4sytk9HVYHq69hFJbIV5rydyGaKzI0pZ4TVY0ndsd2nvIgX0NltQwcCiZWY1CWA0ha9liVR-IQrUgFZJAQDd41SYtGBF_XkyvHhJewK1dfqxIa5L4bu7EcYamrHVcP25mdImg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حريق كبير يلتهم مخزن ضخم للغاز الطبيعي في مدينة غلينبول الامريكية والنظام يبدأ باجلاء السكان من المدينة</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/87982" target="_blank">📅 19:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87981">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98bd6e08e6.mp4?token=id0Vz9wD7t8XS0KR3ACjQH04c4yzRQiuYU1odACcMTXZDnrlZ0COBXF1c85-4qG2Q6BEsp-VDYEVhkrC2a2jWvhuxVg6WZTCpGfCDiXXFOarKOqQowl4BmeGk7_TjOp69CPKLL8SNulYm7rsrqSv3vTg7-yBCIBB8MmXdS6j8uAglpIPBN7JRjInSn2NXlMOrMHznNCA0SRzXz-H58dNYzBM46I3fQN1D-RZHKAOfESYu7klOwbkhLSxI18eS-erA5duOUTrtIgUnZ-xjUoOca9DbAaCKb9si0tjVfcj_AWr29Kl_-_VY9b5UNn-pogpmexWRlNndtRcmO_6-6bC_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98bd6e08e6.mp4?token=id0Vz9wD7t8XS0KR3ACjQH04c4yzRQiuYU1odACcMTXZDnrlZ0COBXF1c85-4qG2Q6BEsp-VDYEVhkrC2a2jWvhuxVg6WZTCpGfCDiXXFOarKOqQowl4BmeGk7_TjOp69CPKLL8SNulYm7rsrqSv3vTg7-yBCIBB8MmXdS6j8uAglpIPBN7JRjInSn2NXlMOrMHznNCA0SRzXz-H58dNYzBM46I3fQN1D-RZHKAOfESYu7klOwbkhLSxI18eS-erA5duOUTrtIgUnZ-xjUoOca9DbAaCKb9si0tjVfcj_AWr29Kl_-_VY9b5UNn-pogpmexWRlNndtRcmO_6-6bC_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
الفضلية بالناصرية جنوب العراق تنتفض  على خلفية اختطاف قيادي بالحشد الشعبي من قبل قوة مجهولة " مسؤول وحدة استخبارات قيادة عمليات حزام بغداد " دعوات جماهيرية للتجمهر والاعتصام المفتوح من عشائر الناصرية امام مركز شرطة ناحية القديم الساعة الخامسة والنصف ..</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/87981" target="_blank">📅 18:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87980">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
نائب رئيس البرلمان الإيراني: بحر قزوين غير قابل للتفاوض
.
- ستُحال اتفاقية بحر قزوين إلى لجنة الأمن القومي للمراجعة، وسيدرس البرلمان بعناية ما يضمن تحقيق مصالح البلاد على النحو الأمثل.
- بحر قزوين لا يقل أهميةً لدينا عن مضيق هرمز، ولا يختلف عن مضيق هرمز والخليج وبحر عُمان؛ فبحر قزوين شرفٌ لإيران.
- بحر قزوين غير قابل للتفاوض من جميع النواحي، سواءً البيئية أو الاقتصادية أو المتعلقة بالأمن القومي، ويجب ضمان مصالح جميع الدول المطلة عليه معًا.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/87980" target="_blank">📅 18:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87979">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KehVjaZD4UgqGtlUu8K3begpPLvFJ0w5FNO0TR8JOPz7mRPbF03TkheXBNmH3mEuxVC7BDuNmLVkGAKye7nygbqCaax5h1m2gnxccIX3qr1Nfk2FLzwQStRU3vhmkILBH8O5nZNBAS6VG9jG5wO9g2bBbmJ_IcCz5GvXSUicsCPuhdS2OBFyswpR9KvQPZsW33aaGZ-mxYxe59hy-6B2KuhQZg0ICybGEdwXvpvFQJdUX-AaAW3domZIzdmon0ybzw2saPvdcdmdAM6Ya_FZkYSdqugIucyEMwhQZ244uMQVKYYd7SWCHwq6S9GaiOHbhkLlgO4Scwl59hopF2F83A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
طائرة امريكية تحلق في الاجواء العراقية انطلقت من تل أبيب.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/87979" target="_blank">📅 18:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87978">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن لاسباب مجهولة</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/87978" target="_blank">📅 18:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87977">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن لاسباب مجهولة</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/87977" target="_blank">📅 18:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87976">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde4f1ad56.mp4?token=LEkkADjTbAFmtTrf9UdRX8pJmrw_txXujQiNejF_rvugT-AIJUGYWqTtEVTMICZUK5VyVxCUBxyD5jlt3wc3_kYL95CkzabICy3vXcNI-vwYuuM3p4hJkJ1Qc0ZjMvORKChg4_g2XiPZh2bj29GuNSBEbavENPxw1hHfyb_3Qm4N4Qj4maWUqrC63jot2D4aga0HpU15U_xjyFtS1V_5D6h46kadlslTaIfaRI0yiE8aEnE26nHSQ7DkZcryooQHTCAyNKW9YYUYIbN8DSWsY8SZfJStKeERGa41nfqXftQyxsd7SwPgUqFrTYCUheCsX2H6TzSvqkv4nm5zKX_vLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde4f1ad56.mp4?token=LEkkADjTbAFmtTrf9UdRX8pJmrw_txXujQiNejF_rvugT-AIJUGYWqTtEVTMICZUK5VyVxCUBxyD5jlt3wc3_kYL95CkzabICy3vXcNI-vwYuuM3p4hJkJ1Qc0ZjMvORKChg4_g2XiPZh2bj29GuNSBEbavENPxw1hHfyb_3Qm4N4Qj4maWUqrC63jot2D4aga0HpU15U_xjyFtS1V_5D6h46kadlslTaIfaRI0yiE8aEnE26nHSQ7DkZcryooQHTCAyNKW9YYUYIbN8DSWsY8SZfJStKeERGa41nfqXftQyxsd7SwPgUqFrTYCUheCsX2H6TzSvqkv4nm5zKX_vLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
قوات الاحتلال الامريكي تعيد رفع بالون التجسس في سماء محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87976" target="_blank">📅 18:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87975">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3805200e49.mp4?token=tRw5gxNdCieG-pNyMCGVDuSPTYrQnO0TyNxNul9zFi6rYai2cQMtfSR1o50go8jHqeXCnHixCW92i45lxUMiuXtFKkCygmbWget-imY8LFlp7gk_tib58JgXPAQX2M-enM-6y2V7e3DobWdcMdn_s0MAMa9NTxZcKT1Sn0CHvKbZAVwYnttX2x0TnopyOQ8D3X3AEENocRwm1VOBRyPJeZ6kYvhmVSXVDYGzwGAl_BAe8qb3cpe-4qJ5RN1wRg5isgF7_O1mxlGhTS_QlMoESlyMk2Ab3UAo89Cj_qjMLr2N1prQ3sJHyCGFx0qFykK8kAkKyAWffadscZLurxmDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3805200e49.mp4?token=tRw5gxNdCieG-pNyMCGVDuSPTYrQnO0TyNxNul9zFi6rYai2cQMtfSR1o50go8jHqeXCnHixCW92i45lxUMiuXtFKkCygmbWget-imY8LFlp7gk_tib58JgXPAQX2M-enM-6y2V7e3DobWdcMdn_s0MAMa9NTxZcKT1Sn0CHvKbZAVwYnttX2x0TnopyOQ8D3X3AEENocRwm1VOBRyPJeZ6kYvhmVSXVDYGzwGAl_BAe8qb3cpe-4qJ5RN1wRg5isgF7_O1mxlGhTS_QlMoESlyMk2Ab3UAo89Cj_qjMLr2N1prQ3sJHyCGFx0qFykK8kAkKyAWffadscZLurxmDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
قوات الاحتلال الامريكي تعيد رفع بالون التجسس في سماء محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/87975" target="_blank">📅 18:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87974">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLQztF6L03KTOVh3peRPRhT_aNKp1atLiKVVkO10cqKbT6Paw9GPKR_lbhESAlM-fG6pHglhwihtLOt5aAwkrocoiqBHVULbezC4CDENVYVGSa9UfpcHokqHB0qs3ure4s4iIcUYY4vo70XZ3hLeVvecYlu-f2E80OVyIHU_rR1hvBV-h1KmArx6vZwe82755QTD2rBZZWOqfMwjU6hF1fflKaSNg_e8eu8V5zszrx7mlyG3YKjSc7i6Q_EGiEElBwy8D2m-mIMu6yszdV1nlyqhdvN-8sc-O9vz2Iw6Bip6p5rrSUgvki_-d_QN_0C4G8mNw732mNTgHnLetQZBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الاعلام والاتصالات العراقية تصدر حزمة عقوبات بحق قناة الفلوجة:
- إيقاف بث برنامج حوار التاسعة لمدة (10) أيام تبدأ من تاريخ صدور قرارنا هذا المخالفته لائحة قواعد البث الإعلامي
- منع الظهور الإعلامي بحق مقدم البرنامج السيد (علي فرحان) لمدة (10) أيام
- فرض غرامة مالية قدرها 25 مليون دينار عراقي لمخالفة البرنامج وحصاد الأخبار لائحة مخالفات الجهات الإعلامية العاملة في العراق</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/87974" target="_blank">📅 17:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87973">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">📰
🇮🇶
وكالة رويترز عن مصادر:
خطط العراق لتصدير النفط عبر خط أنابيب يمرّ في سوريا قد تتطلّب 4 سنوات بكلفة لا تقل عن 15 مليار دولار.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/87973" target="_blank">📅 17:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87972">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
دبلوماسي في وزارة الخارجية الايرانية:
كانت دول المنطقة أول من عرقل تفاهم إسلام آباد، وبالطبع دفعت ثمن ذلك.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/87972" target="_blank">📅 16:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87970">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">الكويت تقول ‏ان ثلاث مغذيات فرعية من محطة التحويل الرئيسية الرميثية (B) خرجت عن الخدمة .</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/87970" target="_blank">📅 16:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87969">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhsIkdJYctScA7cXzJ0qXbUiuZFsTJ_S7PZTcxmBBkGsJOZ4JBzqYqm3ROJlIhRI537-_w8qxhWcW4F6JGDRUFG7brMfnOC1uZkLgiEa9ZVnj6wqlOisycJdzup_xiYNkA-cYz_2opaUD9wEufbsdOp6rKTDfq46JD_1CuXqpcpfxdBULBy4XpvLmijyZIeYL6QNokQ8lnx0vw4PiBOXMO4rScclFzBVO2QHZa96o0Qy17pt3StPy5HS9fzhztJp3An6M7JBgRhfCvV92FDTVMqkMkXH9JCfmg6D4HPr_Y1-ypqNQUn6mfNeOO067m3glJWN0Mt2NfWB-IdojTnfyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
اختطاف المشهور ابو الجود المنتسب بالحشد الشعبي
من قبل قوة امنية مجهولة في العاصمة بغداد بمنطقة البلديات .</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/87969" target="_blank">📅 16:43 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
