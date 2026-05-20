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
<img src="https://cdn4.telesco.pe/file/iz54KqZGxxenZRN5HpD9-CVtCYmBCncXmdTdFR_Bk3FY2xGNxMVdDRzerKtztbLuHe4phb7ZqExW23bmQ8FfuRyBWZW8XO7fX_k2QAAGjsunZyWn3uk0a2H5CjT_Lc2ZIpLYHcUsM5fbWUJAjoFaupffnB-8WRCjz_6HdkbB_moH3bF2VyfiAU-gVRr0U1ocoz43MrGbTUOJp4SOEtH65vrIW9W5sT9zN1h4W7z_t_vdUgMukr_Q6kOGtsKsP5A7bmJyGV7Tnh13q7Xho7d5PtymIMLjwblzzkkU4EIApPX0UnfgZpDlFoozouChvBT88hbecsjhRkUsEDURvrQNOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 253K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 08:13:19</div>
<hr>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKoy1UntyaBdw2d8vgl0OIpipZY5bSzC-D6XcmCAu1d7cONUyQtnbloNETX3kLSTM5G6JL9NbndAixX0iYeWpUTmqmsu5F0Ck6-gjYe47WN8zsp1gUp7H36Uiz8v4zPkbJYnCvNqdCcYyDvyxdibd8TD4iWo4zOJbpkUfTgJzF7X4oeUWrzL5frdta8c6Lr1EFrybEL2MluyvPmYG2E6qEouDKO7sP13Tyty6kxlWSAlD56V9EPoXkaHvl8JGyBdxNQ8s6Nd3z5Ewtrx4EVHqrLGR8K_sRT8uN7lY2Ffcq--ZJ3HPtx6FdlXWa3iO5bFnXbORm-XwSL7EOgzzSqOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نيوورك تايمز: يخطط الاتحاد الدولي لكرة القدم (FIFA) لحظر المشجعين مرة أخرى من إحضار علم "الأسد والشمس" قبل الثورة الإيرانية والملابس ذات الصلة إلى ملاعب كأس العالم خلال بطولة 2026.  تم أيضًا تقييد العلم في كأس العالم قطر 2022.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/75714" target="_blank">📅 01:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLahdOJ-mNArpLLsce7g98tALbqNoD2LVY0Jron_qgQuUgI98S56aw-QxXAwy2ble05zyfrafRXriVMPn7_3t-DrS1g6tB8tStQgPi8-Prd80xBLFTMt1-5wZBuG9eoO1tcwDuw0lToXhedbTb3wr944iiIixPzUOYEo-FFTxjbNaXzbv2f70kMSnfG5gpH7MeY0HAA46b4OHrK7uZDXWMjnWV0hiZ4ADeXNzoI6IsJGXEQh3ju_lCQD0pq3nsmyMbaQoUcGcvLIYTvMR-FsR3B6w6qBqCYsj_qb13FqVx3Fu1cKE4hbN8YqJ1ETdcs6cORSjWJt9UDw6sYuKmHXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجولاني يشكر دونالد ترامب على “كرمه الزايد حيل” بعد إهدائه شيشتين عطر، ويعتبرهن “الأساس المتين” للعلاقات السورية الأميركية، وسط ترقب شعبي لمعرفة إذا المرحلة الجاية تشمل بخاخ جسم لو مزيل عرق دبلوماسي.
القدس تنتظرنا يا اخوة
😄</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75713" target="_blank">📅 00:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75712">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFTZ0krJ6fwyJ3FWftT414Gev9VrodS0TWLcBhpdN3Bj8SrNcfG-AnRaYeqwcCSC9Fpnkyom0wKnTPWLPo45tF_4k-hAJ73Mu7HU__cuK0Odh5_J-8qOXvkCrRljC3EsMqANNT3gp2_r_i4frrgJlkWMcMxLvj8B3KpEH0zFR99O5CkaEx-ErDanVoMNeh9YNzCBGoUY7VpJwFRVot9fzVWRWArvBlWPdicA8Y1j9jZmqFJK25IYN1-iyALvcFJ4M4woin3jWITBDcJW27H2qsHByCGXveSTlio416DqJgVO-XWMmgtUNJCIyu7fO0ckg4Vz3ufzBZxpc8i3JOYyUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
بعد أشهر من بدء الحرب على إيران، يعترف الكونغرس الأمريكي بفقدان عشرات الطائرات التي تبلغ قيمتها مليارات الدولارات.
تم تأكيد قواتنا المسلحة القوية كأول من يضرب طائرة F-35 التي توصف.
مع الدروس المستفادة والمعرفة التي اكتسبناها، ستضم العودة إلى الحرب العديد من المفاجآت.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75712" target="_blank">📅 00:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75711">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🌟
🏴‍☠️
قوات حزب الله البطلة تشتبك مع عناصر جيش العدو في بلدة حداثا بجنوب لبنان وتتمكن من إستهداف وإحراق دبابة ميركافا وإصابة عدد من الصهاينة والمعارك مستمرة حتى اللحظة.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75711" target="_blank">📅 00:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌟
🏴‍☠️
قوات حزب الله البطلة تشتبك مع عناصر جيش العدو في بلدة حداثا بجنوب لبنان وتتمكن من إستهداف وإحراق دبابة ميركافا وإصابة عدد من الصهاينة والمعارك مستمرة حتى اللحظة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75710" target="_blank">📅 00:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbad0422a.mp4?token=FN8CLgsKuAMRwDllRhCm-MfogZ2IvjxATLEGwB8g52epIV_ndx881EhAZ2_7CweT7vHukzaLzrJcKSs7e8Usf9Eu6mE5UrahOHQZKfBHsZGO5XT86y3Z_a_Zh_U7osmg_adIFcCHLcTO-1SkJNqkIMpgeB-P_qbOCXnh41BLQcPdV8rLeiA0caToR2UZAF4QP-ylRKNT6gJb--FPJNdNs6z9TjsFW8iwyquy-um3nrTUwOuWFrNHB3yCGYWWhd_TDN6qt9SLuaeiFFoazgu51aR5-P8CQGM42EJaTsygfO8cGaoe--8L4xTXd1TABE6c-zZlgaZca2gAXCqjDXO-nJV7NP5Yr3Wq6M5PdGbEkgCqqc5sgR2rwbDxAR4GTUB_BVgcO7G8x2sa0qI6HyjhuLo1GCR1URRapyaANdvj8RKvzEt0DYgq48VEerag_8yiyrZtt31cxRYVHFp5WqOZzaMxkEhBPFY-fZAm0FIehsFO5kVgmpbVGe9gNrBgLF-DTv9DqrpICL9T1je1yl82nvM4utrwm6tICtqUGWVuISDHv5zVVsHp6BScqKQLZ9082gB7w_HnjLr9oKfDXdBCHuikrLxwPMN-mvI8a7v9WTgr03pZZoLeUD5vU1qxUmHZxCbP9gi0f5cyGjnf3V3NbKZnC1MQTtrBEeqOMtxC19o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbad0422a.mp4?token=FN8CLgsKuAMRwDllRhCm-MfogZ2IvjxATLEGwB8g52epIV_ndx881EhAZ2_7CweT7vHukzaLzrJcKSs7e8Usf9Eu6mE5UrahOHQZKfBHsZGO5XT86y3Z_a_Zh_U7osmg_adIFcCHLcTO-1SkJNqkIMpgeB-P_qbOCXnh41BLQcPdV8rLeiA0caToR2UZAF4QP-ylRKNT6gJb--FPJNdNs6z9TjsFW8iwyquy-um3nrTUwOuWFrNHB3yCGYWWhd_TDN6qt9SLuaeiFFoazgu51aR5-P8CQGM42EJaTsygfO8cGaoe--8L4xTXd1TABE6c-zZlgaZca2gAXCqjDXO-nJV7NP5Yr3Wq6M5PdGbEkgCqqc5sgR2rwbDxAR4GTUB_BVgcO7G8x2sa0qI6HyjhuLo1GCR1URRapyaANdvj8RKvzEt0DYgq48VEerag_8yiyrZtt31cxRYVHFp5WqOZzaMxkEhBPFY-fZAm0FIehsFO5kVgmpbVGe9gNrBgLF-DTv9DqrpICL9T1je1yl82nvM4utrwm6tICtqUGWVuISDHv5zVVsHp6BScqKQLZ9082gB7w_HnjLr9oKfDXdBCHuikrLxwPMN-mvI8a7v9WTgr03pZZoLeUD5vU1qxUmHZxCbP9gi0f5cyGjnf3V3NbKZnC1MQTtrBEeqOMtxC19o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انيميشن بأسلوب الليغو يوثّق المسار الذي خاضه رئيسٌ شعبيّ للجمهورية الإسلامية الإيرانية
نُشر بمناسبة ذكرى استشهاد الشهيد رئيسي ورفاقه الشهداء</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75709" target="_blank">📅 23:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75708">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇺🇸
حاكم كاليفورنيا:
إنهم يحاولون تزوير الانتخابات. دونالد ترامب يعلم أنه سيُهزم بشدة في شهر تشرين الثاني.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75708" target="_blank">📅 22:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
انتحار جندي من الجيش الإسرائيلي داخل دورة مياه في "الكرياه" بتل أبيب.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75707" target="_blank">📅 22:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75706">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🌟
🏴‍☠️
مراسم تنكيس علم العدو الإسرائيلي الغاصب في مقر اللواء 226 التابع لجيش العدو في بلدة البياضة جنوبيّ لبنان بتاريخ 17-05-2026</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75706" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75705">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
‏احتجزت الولايات المتحدة ناقلة نفط مرتبطة بإيران في المحيط الهندي ليلاً، في الوقت الذي يهدد فيه ترامب باستئناف الضربات العسكرية على إيران.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75705" target="_blank">📅 21:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75704">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
‏
جي دي فانس:
خياران أمام إيران إما الاتفاق أو استئناف الحرب.
نعتقد أن الإيرانيين يريدون إبرام اتفاق لكن نؤكد أنه لدينا دائما خطة بديلة.
‏لا أحد يريد عودة الحرب والفرصة متاحة أمام إيران.
إيران بلد معقد للغاية ونرى مواقف متشددة من جانب فريقها المفاوض.
أوضحنا للإيرانيين خطوطنا الحمراء.
لا أعتقد أن الإيرانيين سيكونون متحمسين لنقل ما لديهم من يورانيوم مخصب لأمريكا أو روسيا.
مخططنا ليس نقل اليورانيوم الإيراني المخصب إلى روسيا ولم يكن ذلك أبدا ما نخطط له.
لا نريد فقط التزاما من الإيرانيين بعدم امتلاك سلاح نووي بل بألا يعيدوا بناء قدراتهم النووية مستقبلا.
هذه ليست حربًا أبدية. سنتولى الأمور ونعود إلى ديارنا. هذا ما تعهد به ترامب، وهذا ما سيحققه.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/75704" target="_blank">📅 21:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🏴‍☠️
‏
هيئة البث الإسرائيلية:
الاستعدادات الأميركية – الإسرائيلية لاستئناف الحرب ضد إيران اكتملت.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75703" target="_blank">📅 20:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75702">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjCf8MfaTrAKuSlYVMyYXsAzD336XJa0HK4ALfZmtm3K8U_84EN0O8GdWbmViYe3ghDnH-4KXtpmucs-Q4FOZSYkItLxmWXglUtHhLXBZ0eJ9RSUDHYIVgQwq7icDMk-Pf7aIGF44rgTD5cNUBgHts6u0WvQ19Qa2r6u-7f8sN5zoxBxGMzznJyjgcRMApGEvDQyfwVS7_R-sc7RN1MMTHakXDld95LZizjePIUZT0kjyu3kf9uybxgmkDhdVtOFnhl9Z3a0vssoOZi0ZbWm4qHiyCnATKFDlSqOU3W9Cixf4hWUoW3rll0ran05Ti9i-3uX7ukHUzrFdWmcLkvKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
وزير السيد مقتدى الصدر ينشر عبر حسابه الشخصي.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75702" target="_blank">📅 20:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏ اعتقال موظفة في السفارة الأمريكية في بغداد تدعى قند محمد فرج ذياب الجنابي بتهمة الرشوة والفساد !!!!
‏</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75701" target="_blank">📅 20:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حدث امني خطير في بغداد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75700" target="_blank">📅 20:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6woGBmaX00JZhO9vkjsAxe8Beyv78a-piOZkqMmrV932S6PGisMXtjXRQEz8-1g1c1ttwCMw5kLOTLAOC2vH2P7kP48Ojdnwq2cFyOEKxcdEOCuHkm4hPgC9_aqnllmBpTDMQzsEcGSJbCmnjMt6eS2rZ9wc0WUaM2CzB36hCJ-VvvADP2ATWFCzWbiqUqW7ioELgYspRtKz8S2JaQBZEow90q-Ext2o1SQ33xnQeOdN024UoGadYxkSDPvI2mHfThjHzZwhviFvc-oEbEsJ3Wq1ZsM0pjRke3s7mVAe_dLv6FTXfzA2msa7lY-66qwetTr9g8dvxbkx9bx2SIR5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
مقتل جندي إسرائيلي في جنوب لبنان.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75699" target="_blank">📅 20:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
حزب الله ينشر:
ترقبوا... مراسم تنكيس علم العدو الإسرائيلي الغاصب في مقر اللواء 226 في البياضة.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75698" target="_blank">📅 19:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75697">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⭐️
ذا أتلانتيك:
اصطدمت طائرتان لإعادة التزود بالوقود من طراز KC-135 Stratotanker فوق غرب العراق في 12 آذار خلال الحرب الأمريكية-الإسرائيلية ضد إيران، مما أدى إلى مقتل ستة من أفراد الخدمة الأمريكية بعد تحطم إحدى الطائرتين بينما تمكنت الأخرى من الهبوط مع أضرار شديدة في الذيل.
صرحت قيادة مركز القيادة المشتركة (CENTCOM) علنًا أن التصادم وقع في "مجال جوي صديق" ولم يكن بسبب نيران معادية. ومع ذلك، تظهر تقارير المخابرات الأولية أن نشاطًا مضادًا للطائرات تم اكتشافه من ميليشيات مدعومة من إيران في المنطقة في وقت تحطم الطائرة، مما يثير احتمال أن يكون الطيارون قد اتخذوا إجراءات تفادية قبل التصادم.
رفضت قيادة مركز القيادة المشتركة (CENTCOM) لاحقًا هذه التقارير، مستنتجة أن الإطلاقات المكتشفة كانت على الأرجح صواريخ موجهة إلى أهداف أرضية وليس طائرات.
من المتوقع أن يحدد تحقيق مستمر لسلاح الجو الأمريكي ما إذا كان الحادث كان خطأً يمكن تجنبه من قبل الطيارين بسبب ازدحام المجال الجوي بدلاً من عمل العدو.
شمل الأفراد الستة الذين قُتلوا ثلاثة طيارين في الخدمة الفعلية من السرب السادس لإعادة التزود بالوقود في فلوريدا وثلاثة من أفراد الحرس الوطني للطيران في أوهايو من السرب 121 لإعادة التزود بالوقود.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/75697" target="_blank">📅 19:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75696">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6863208b.mp4?token=V_UzbAd9t9qoJrBrGsa__94-Og2uNmfhNf3MF-b5c-bZmnMDXxWRnVJ0cXrNfjAEqy_g0tgVPSztFJBQUyTU5b84aBR6EixplLAyaiOCs8etrkSXZPw3AGESdR67RPXDC8R3DWOwXd1C9abNZGiurEDNoG9FhsQNuQWhIfO-WBULPEfo89qeSAw86E-czqygxUryRMJuZ_FF2d8gNsBzH4B04uEsjvBDaysZcWQEFN4NXqkHKcx4YxF5PiHzIdgM2Mor2LepB-5P1OS3yOjMp3mEa5Ly0pOiU92UGsP0SBK_CXbMjt2kHSrBbtSH8eBOU1bSFVofKcpnU5CkHRSjskMImPgbw2A2jAe8Qvh4HBWRTxrHO6gcL9XUY-ZZehdWMrdRlACpWRYgXQU7xq4fJs_iYtkyusqb88IeNUSeeDtuvrgMUuQd7CW8JmUhLnu0K6TgKcWkEk36V0xPIRth2GbQII2oy9hxJca8xYpotuee3QorypI-Qn0GC8RarC8Sc99MDYBoXm9roUFjNSIXkN4z0cX94vghjQDPUk_ZAUz2xfgmo5jcKyR2418S6B6kk5eeibamGlKsgFKB_0B2m1wSGU0AF0jOHG0AmCVWnCMUWao1JEsEOd7rDhrWfVZHxTozy-bTbDQox6jFO3kAMwnQwTJWHdRxmhotyrtSt0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6863208b.mp4?token=V_UzbAd9t9qoJrBrGsa__94-Og2uNmfhNf3MF-b5c-bZmnMDXxWRnVJ0cXrNfjAEqy_g0tgVPSztFJBQUyTU5b84aBR6EixplLAyaiOCs8etrkSXZPw3AGESdR67RPXDC8R3DWOwXd1C9abNZGiurEDNoG9FhsQNuQWhIfO-WBULPEfo89qeSAw86E-czqygxUryRMJuZ_FF2d8gNsBzH4B04uEsjvBDaysZcWQEFN4NXqkHKcx4YxF5PiHzIdgM2Mor2LepB-5P1OS3yOjMp3mEa5Ly0pOiU92UGsP0SBK_CXbMjt2kHSrBbtSH8eBOU1bSFVofKcpnU5CkHRSjskMImPgbw2A2jAe8Qvh4HBWRTxrHO6gcL9XUY-ZZehdWMrdRlACpWRYgXQU7xq4fJs_iYtkyusqb88IeNUSeeDtuvrgMUuQd7CW8JmUhLnu0K6TgKcWkEk36V0xPIRth2GbQII2oy9hxJca8xYpotuee3QorypI-Qn0GC8RarC8Sc99MDYBoXm9roUFjNSIXkN4z0cX94vghjQDPUk_ZAUz2xfgmo5jcKyR2418S6B6kk5eeibamGlKsgFKB_0B2m1wSGU0AF0jOHG0AmCVWnCMUWao1JEsEOd7rDhrWfVZHxTozy-bTbDQox6jFO3kAMwnQwTJWHdRxmhotyrtSt0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇨🇳
لحظة وصول الرئيس الروسي فلاديمير بوتين إلى بكين، واستقباله من قبل وزير الخارجية الصيني وانغ يي.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/75696" target="_blank">📅 19:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75695">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQKMr3ww9nSvfdBJmi3R6lEJD2X4kmA3hBJS23Fgy9HnE62iBbxkD5mOu__HFqKoKthS9uDf__CfpEXYHLEykrb9j9DcDFxpulm0H-evwnz1A0vfDBaPCqwfyUiDg4NriWihOJXLUiBd_kLU3r4Pv0dG6-zJ1nG2StbnePRwi-lyx5x26IOOBXQcp8jLyGBiS_vs7a72g84vynwBNeUCve1B8cG_4TSoI0gBSp6iDvgcQSs07uRAU9eI56wdivPOtieiaYoCJWjkoDrn2UYRKGciaI_Fqo0LLfjGAHr7vxBF-9D21mYbu2eTGQxvq1RSR5PhKOURYlKGrWKl195q5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رد قائد الثورة الإسلامية على رسالة جمعٍ من الناشطين الشعبيين في مجال السكّان:
أشار قائد الثورة الإسلامية، آية الله السيد مجتبى الخامنئي،  في معرض رده على رسالة الإعراب عن المحبة والتعزية المرفوعة من قِبل جمعٍ من الناشطين الشعبيين في مجال السكان بمناسبة استشهاد قائد الثورة (قدّس الله نفسه الزكية)، إلى مسألة زيادة السكان وارتباطها بقوة إيران الإسلامية وحضارتها، مؤكدًا على تكثيف الجهود المتزايدة للناشطين الشعبيين في هذا الحقل وضرورة ترويج ثقافة الإنجاب.
🔻
وجاء نص رد قائد الثورة الإسلاميّة، الذي نُشِر بمناسبة اليوم الوطني للسكان، على النحو الآتي:
📖
بسم الله الرحمن الرحيم
بعد توجيه التحيّة والشّكر على إعرابكم عن المحبة والشعور بالمسؤولية، أيها الناشطون المُخلصون في مجال السكان؛ فإنّ من بين الإنجازات القيّمة للدفاع المقدس الثالث، والنعمة العظيمة لبعثة الشعب الفريدة التي تجلّت للجميع، صعود إيران إلى مستوى قوة كُبرى ومؤثرة. ولا شكّ في أن استمرار هذا الوضع وبلوغ مستوى أفضل منه، يرتبط ارتباطًا مباشرًا بقضيّة السكان.
▪️
إنّ قضية وجوب زيادة عدد السكان يُنظر إليها من منظار تعويض النقص الناجم عن بعض سياسات الماضي؛ ولكن إضافة إلى ذلك، فإنه من خلال المتابعة الجادة للسياسة الصحيحة والحتمية لزيادة عدد السكان، سيكون الشعب الإيراني العظيم قادرًا في المستقبل على خوض غمار أدوار كبرى وطفرات استراتيجية، وقطع خطوات واسعة في اتجاه إرساء الحضارة الحديثة في إيران الإسلامية. ومن هذا المنطلق، فإن الجهود المتزايدة للناشطين الشعبيين في مجال السكان وترويج ثقافة الإنجاب، يمكن أن يكون لها أثر بالغ الأهمية في سبيل تأمين هذا المستقبل المشرق.
⏺️
ومن جهة أخرى، فقد كان هذا الأمر أحد أهم هواجس قائدنا العظيم الشهيد (أعلى الله مقامه الشريف)، الذي طالما أكد عليه في الكثير من اللقاءات، والمداولات، والاجتماعات العامة والخاصة، ولا يزال يُعدّ من أهم القضايا الاستراتيجية للنظام. يُؤمل أن تؤدي جهودكم المخلصة، أيها الأعزاء، في ظل الدعاء المستجاب لسيدنا (عجل الله تعالى فرجه الشريف) إلى نتائج مثمرة، إن شاء الله.
✍
السيد مجتبى الحسيني الخامنئي
🗓
19 أيار/ مايو 2026</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75695" target="_blank">📅 19:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75694">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e2efce8f.mp4?token=eWirmBzS21VVkY5pm9VyLIwzC0mMMtJwJX-5gfA0GALKwfAtHhT8DWaRshymp_D9XHIDk9Dvx10nx1mY3zVK-D_qwm9xxNQpTY2jY7RDwg7qwK_KPNo_jR0GOlbwTYdbyjmGbWsknivcyeLMkx80gDy5kAD7RUwyBRab7I_2cVVRr6c4sl_3nucZkvGoEM5U2iMzSfd3iN5DWinJOGpPY2Ft-yRXYBHVAigVYXXcVixPPjtD75brdGWiWTRaJx8f7vbYzyGGN8kELx-xKRavVU2nrKC0huPQJnx4fiPO8VgFO3bxU3ZyCAKC0uN3NpP0nkJvYOhVH9UcGoIgT2e9MoPapuAKO1dDMlyKfAFaOgTYwsMlg2zJH51YxMriFLZmHdMO-ObXYmILRrFJAd7uTjHrbBZ0YGP3dyNoDKa59C9P2bkqIdxD9gMeGvVMAKQDsBtvW6zA5oQS3VZGGuV8DLYp-munFf0Loj9UDH2DMCCL34SM_D33TMw1JyHbNgvvhSShj2kq5u0-GmNMtVxOix99gAqUvPzmSNL9g5hj0xby1nFzNZ9bfZUFYhaR2HuMFM9y7PFAV9Dg5aZ5rAhYkYDc5Qx7MxAuz68DxYvRAmtVmony3V0Tll4r3wBKpajslTNJQGQys4J4zSwYVLcR463M5cXaPm6iP61gEkjNKME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e2efce8f.mp4?token=eWirmBzS21VVkY5pm9VyLIwzC0mMMtJwJX-5gfA0GALKwfAtHhT8DWaRshymp_D9XHIDk9Dvx10nx1mY3zVK-D_qwm9xxNQpTY2jY7RDwg7qwK_KPNo_jR0GOlbwTYdbyjmGbWsknivcyeLMkx80gDy5kAD7RUwyBRab7I_2cVVRr6c4sl_3nucZkvGoEM5U2iMzSfd3iN5DWinJOGpPY2Ft-yRXYBHVAigVYXXcVixPPjtD75brdGWiWTRaJx8f7vbYzyGGN8kELx-xKRavVU2nrKC0huPQJnx4fiPO8VgFO3bxU3ZyCAKC0uN3NpP0nkJvYOhVH9UcGoIgT2e9MoPapuAKO1dDMlyKfAFaOgTYwsMlg2zJH51YxMriFLZmHdMO-ObXYmILRrFJAd7uTjHrbBZ0YGP3dyNoDKa59C9P2bkqIdxD9gMeGvVMAKQDsBtvW6zA5oQS3VZGGuV8DLYp-munFf0Loj9UDH2DMCCL34SM_D33TMw1JyHbNgvvhSShj2kq5u0-GmNMtVxOix99gAqUvPzmSNL9g5hj0xby1nFzNZ9bfZUFYhaR2HuMFM9y7PFAV9Dg5aZ5rAhYkYDc5Qx7MxAuz68DxYvRAmtVmony3V0Tll4r3wBKpajslTNJQGQys4J4zSwYVLcR463M5cXaPm6iP61gEkjNKME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-05-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بصاروخٍ موجّه.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75694" target="_blank">📅 19:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75693">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇺🇸
🇮🇷
قائد القيادة المركزية الأمريكية:
القوات الأمريكية تعرضت في 7 إبريل لإطلاق نار من إيران وقمنا بالرد.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/75693" target="_blank">📅 18:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75692">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇺🇸
ترامب: ‏الجميع يقول لي ان الحرب على ايران غير شعبية، لكنني أعتقد أنها تحظى بشعبية كبيرة. عندما يسمعون أنها تتعلق بأسلحة نووية قادرة على تدمير لوس أنجلوس، عندما نشرح الأمر للناس - ليس لديّ الوقت الكافي لشرحه لهم.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75692" target="_blank">📅 18:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75691">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc14bff42.mp4?token=J71TU5xmyN672tMq7ieFnaOWG64bshpOe7brPZKw-97qqbGQl1M6vTTx1Za5lSdNEMKUmSENUavTKhX6zLLAKyL_9YydgC6-allyi5y136oVvFEVVUG-CzTToo1r1o8G14kruuyAwphsKh3X2ipp_yVxxXkTA16Jl156scQEJssGe37aVg1jASu_wQUi_xqQjs_zbDf26oDNi42GyhEXFmrkqHnp9Zq8_6UGnA9RJht-D1peXZbBP4QmRxSCglj36CHsUdPnhQU089NtdFc0z-SZJ4882Q6cLNZrcJQnoYa_MNynR7FWlf8cktIeSGywsxZgBVG8eeTZjLY8aCQrSJz_EwFqEPqjDNVaOviocYOwidUtXskMsa4DYQndL71cwFNKZym6ZX-xqlUBwXIH_nzY6DAz0DtEwTbKxklrn6CKtWERIXLKWf_R_ydr4t--dH3hV4S9XA0fSKfdBqv1TrWOasyxPc5l0fX16MPvf3ESJvRzlYlxraga3P4RW69zITqysFVwtxH1Ni9LQvV48MSsIQSizRh80LfroMCtDub_tGdhkEmmg2IQsg6hXgn8ChR7fOS9b0Tl_uv_oUr-U_JKAMzDw2DLXtcji84cJxgR13dYLIeENVoP-CMJpsY2GO9-NtyTtPgUnUE5Nq81cwjOIJDEcNb2fBwbueeTon0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc14bff42.mp4?token=J71TU5xmyN672tMq7ieFnaOWG64bshpOe7brPZKw-97qqbGQl1M6vTTx1Za5lSdNEMKUmSENUavTKhX6zLLAKyL_9YydgC6-allyi5y136oVvFEVVUG-CzTToo1r1o8G14kruuyAwphsKh3X2ipp_yVxxXkTA16Jl156scQEJssGe37aVg1jASu_wQUi_xqQjs_zbDf26oDNi42GyhEXFmrkqHnp9Zq8_6UGnA9RJht-D1peXZbBP4QmRxSCglj36CHsUdPnhQU089NtdFc0z-SZJ4882Q6cLNZrcJQnoYa_MNynR7FWlf8cktIeSGywsxZgBVG8eeTZjLY8aCQrSJz_EwFqEPqjDNVaOviocYOwidUtXskMsa4DYQndL71cwFNKZym6ZX-xqlUBwXIH_nzY6DAz0DtEwTbKxklrn6CKtWERIXLKWf_R_ydr4t--dH3hV4S9XA0fSKfdBqv1TrWOasyxPc5l0fX16MPvf3ESJvRzlYlxraga3P4RW69zITqysFVwtxH1Ni9LQvV48MSsIQSizRh80LfroMCtDub_tGdhkEmmg2IQsg6hXgn8ChR7fOS9b0Tl_uv_oUr-U_JKAMzDw2DLXtcji84cJxgR13dYLIeENVoP-CMJpsY2GO9-NtyTtPgUnUE5Nq81cwjOIJDEcNb2fBwbueeTon0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: تلقيت مكالمة يوم امس وقالوا لي "سيدي هل يمكنك الانتظار؟ نحن قريبين من صفقة"  سأمنح إيران مهلة يومين أو ثلاثة ربما حتى الجمعة أو السبت. فترة زمنية محدودة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75691" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75690">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bf75e59c.mp4?token=sGoNQ0q4ev1bAdRXT3zX_7Hjwqd1hfuLZ3DC5Smdj-TSNxo1h1vuvdIh57gbJlsXBKGQI1_Zpegz5QoQ35Qq6cB-EPtgh3Tfjf2jn3VqHYfJR76uuzt0TTcVvyjA_I67nOosrrqtPFfeOjCS4bmNnWXNJ3rlF2APjnlNimlpWSnQLkQJuR5hiu8YMD70GYqRdlvY3lO5yTeU3CNvIyKERDG_ww6aMvh919ruDv1i66rVWX5-zT9JEU3XGilo5vu4q_bmsdgpULz3uhkPyJ0-80JjBMj9eXTj07I0pDNb0i4FBQiunoKJH_ufu7cIYXZeyTV45Lp0Mg_xKogDxvS-WI7SnE8zJCRSh4IqrY8rjYULmdhassvdtGM2Q_v0rhipB-OVY9ehUp0N1gRdwmhWMQHy860tYvHCsCJ9YnxkH64F1AnBKG1cYOZgdVPXDxq_UgXiauFv1zmpcYslE7ML1alecQXv8tHE_qMMhaDGF_gN-YYPtW_TuN-LuZXy0gzWawR2eSVu-k0vWRM9XgRAWpy15Rtf1QXIEu65X2RDfk5Z3UM3M26-Srp_7hoPPC-3f8cBB4lYSid3HJTzgKO6pW37O3XhQrc6IYSc5J_a6KpIHd1OdhIyBnzp-0cTL4rED-R8oQJmADJLEEw3j4TCEvECsHQIBuUmtkuLFCw9UW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bf75e59c.mp4?token=sGoNQ0q4ev1bAdRXT3zX_7Hjwqd1hfuLZ3DC5Smdj-TSNxo1h1vuvdIh57gbJlsXBKGQI1_Zpegz5QoQ35Qq6cB-EPtgh3Tfjf2jn3VqHYfJR76uuzt0TTcVvyjA_I67nOosrrqtPFfeOjCS4bmNnWXNJ3rlF2APjnlNimlpWSnQLkQJuR5hiu8YMD70GYqRdlvY3lO5yTeU3CNvIyKERDG_ww6aMvh919ruDv1i66rVWX5-zT9JEU3XGilo5vu4q_bmsdgpULz3uhkPyJ0-80JjBMj9eXTj07I0pDNb0i4FBQiunoKJH_ufu7cIYXZeyTV45Lp0Mg_xKogDxvS-WI7SnE8zJCRSh4IqrY8rjYULmdhassvdtGM2Q_v0rhipB-OVY9ehUp0N1gRdwmhWMQHy860tYvHCsCJ9YnxkH64F1AnBKG1cYOZgdVPXDxq_UgXiauFv1zmpcYslE7ML1alecQXv8tHE_qMMhaDGF_gN-YYPtW_TuN-LuZXy0gzWawR2eSVu-k0vWRM9XgRAWpy15Rtf1QXIEu65X2RDfk5Z3UM3M26-Srp_7hoPPC-3f8cBB4lYSid3HJTzgKO6pW37O3XhQrc6IYSc5J_a6KpIHd1OdhIyBnzp-0cTL4rED-R8oQJmADJLEEw3j4TCEvECsHQIBuUmtkuLFCw9UW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: دول الخليج تتفاوض وإسرائيل أيضاً.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/75690" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75689">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
‏ترامب: كنت على بُعد ساعة من توجيه ضربة لإيران، وكان ذلك سيحدث الآن. القوارب والسفن مُحمّلة ونحن على أهبة الاستعداد للبدء.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/75689" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27acce6b15.mp4?token=M0_qvQIedcIOX35hBrFthBFcwMkjODTF87Jk9J4aWBhtupEfVoADgROYBSmmq90o6IkANhvsLwEz4Jdg00n9LUJzXI5qVV2j0fGtdZIM7W2Q5k8-oEmladWspNudJTjleMtg24qCPxo08VktQixhpvZ3SUXytxEDUCXD-NJAE9zzpT3J19X0j_RCP5bXeyLe3zliEbltLn1OIzDcUho4g-mLuJzERwfu11x_xhvji2fJNGtCiR64rZG53FFR3kMKC1BQBABELbSRVB4mxkRqRfiaDTEmgmia75AoiBYtcP0Q-sYBtF07VMBtgNUdvLk3C_-O9Lc_FhkiXr6rpMBB-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27acce6b15.mp4?token=M0_qvQIedcIOX35hBrFthBFcwMkjODTF87Jk9J4aWBhtupEfVoADgROYBSmmq90o6IkANhvsLwEz4Jdg00n9LUJzXI5qVV2j0fGtdZIM7W2Q5k8-oEmladWspNudJTjleMtg24qCPxo08VktQixhpvZ3SUXytxEDUCXD-NJAE9zzpT3J19X0j_RCP5bXeyLe3zliEbltLn1OIzDcUho4g-mLuJzERwfu11x_xhvji2fJNGtCiR64rZG53FFR3kMKC1BQBABELbSRVB4mxkRqRfiaDTEmgmia75AoiBYtcP0Q-sYBtF07VMBtgNUdvLk3C_-O9Lc_FhkiXr6rpMBB-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: ستعرفون قريبًا جدًا ما إذا كنا بحاجة لضربة كبيرة أخرى.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/75688" target="_blank">📅 18:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏ترامب: قد نضطر إلى توجيه ضربة أخرى لإيران، لست متأكداً.</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75687" target="_blank">📅 18:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75686">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏ترامب: قد نضطر إلى توجيه ضربة أخرى لإيران، لست متأكداً.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/75686" target="_blank">📅 18:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
‏
مجلس الوزراء العراقي يقرر ما يأتي:
‏
تعطيل الدوام الرسمي في الوزارات ومؤسسات الدولة كافة، ابتداءً من يوم الثلاثاء الموافق 26 أيار ولغاية يوم السبت الموافق 30 أيار بمناسبة عيد الأضحى، على أن يُستأنف الدوام الرسمي يوم الأحد الموافق 31 أيار.
‏تعطيل الدوام الرسمي يوم الخميس الموافق 4 حزيران في الوزارات والمؤسسات الحكومية كافة، بمناسبة عيد الغدير.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/75685" target="_blank">📅 18:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75684">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامب من موقع بناء قاعة الرقص في البيت الابيض: "إنها مقاومة للطائرات المسيّرة".
يبدو ان المسيرات مصدر قلق لترامب
😄</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75684" target="_blank">📅 18:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
وزارة الخزانة الأمريكية تفرض عقوبات على أربعة أشخاص في أسطول الصمود الانساني الذي يحاول كسر الحصار عن قطاع غزة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75683" target="_blank">📅 18:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الايراني:
- تقول الولايات المتحدة إنها أوقفت الهجوم على إيران "مؤقتًا" لإتاحة الوقت للمفاوضات؛ لكنها في الوقت نفسه تتحدث عن استعدادها لشن هجوم واسع النطاق في أي لحظة. هذا يعني اعتبار التهديد فرصة للسلام!
- إيران موحدة ومستعدة بحزم لمواجهة أي عدوان عسكري.
- بالنسبة لنا، الاستسلام لا يعني شيئًا؛ إما أن ننتصر أو نصبح شهداء. وكما قال الشهيد رجب بيجي: نحن أمة عظيمة، فلنسجل اسمنا في التاريخ؛ من بين كل الألوان، اخترنا الأحمر، ومن بين كل أنواع الموت، اخترنا الشهادة.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75682" target="_blank">📅 17:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏
قائد حلف الناتو:
سيتم سحب 5000 جندي أمريكي من أوروبا.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75681" target="_blank">📅 17:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دويلة الامارات تزعم ان الهجمات التي طالتها قادمة من الاراضي العراقية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/75680" target="_blank">📅 17:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75679">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏الولايات المتحدة تفرض عقوبات جديدة على إيران</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75679" target="_blank">📅 17:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">📰
مجلة
فورين بوليسي الامريكية:
إيران تتفوق في معركة الرأي العام. قبل مئة يوم كانت إيران "دولة منبوذة" أما اليوم فهي الشخصية الرئيسية على الإنترنت</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75678" target="_blank">📅 17:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75677">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdfd32e5e.mp4?token=g7nkJ0t6Deul77mFJS7UHx9HmgqiWYBU_9QaDs2IQgF-xdubeHOdDCFtR3Lpn4Q48h3B5LX6p4Cv75cCe7eBMiKstQnnbcHqS53oV3mZpHAL0KEV4QNT9b7b1yzw59be0qdEkF8VJX-KrD0LQddptmvgqe4fa-5CC6aWV38od3-5RZFNC9INz9LDkTEBiD3niXbObr7Bn0qTYjcd2fp3kGf8jd-5pwGmwB8OfusAWGERIfUne2e0MGuTPhMcjG9EQEFFu-eaC3Tk9l81BYg8oTi0vcJ478MejX5aL4BfBqFdt8MuTZ1XiO-GtOJwmlYD9AH6xjObEKMm0qT2D-CUAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdfd32e5e.mp4?token=g7nkJ0t6Deul77mFJS7UHx9HmgqiWYBU_9QaDs2IQgF-xdubeHOdDCFtR3Lpn4Q48h3B5LX6p4Cv75cCe7eBMiKstQnnbcHqS53oV3mZpHAL0KEV4QNT9b7b1yzw59be0qdEkF8VJX-KrD0LQddptmvgqe4fa-5CC6aWV38od3-5RZFNC9INz9LDkTEBiD3niXbObr7Bn0qTYjcd2fp3kGf8jd-5pwGmwB8OfusAWGERIfUne2e0MGuTPhMcjG9EQEFFu-eaC3Tk9l81BYg8oTi0vcJ478MejX5aL4BfBqFdt8MuTZ1XiO-GtOJwmlYD9AH6xjObEKMm0qT2D-CUAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#متداول
نفاذ الوقود يتسبب في توقف سيارة إسعاف تنقل مريضاً وسط احد شوارع محافظة ميسان</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75677" target="_blank">📅 17:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgA2h8KDfnDBR6EQEm_nHwO0ehTShqxyKkLI8zvxLypLhRrvYFWpDNRsu5jhPd-n6MD-SUNVwUhb91UhNJp0ax5swTHLQEk_PW0FOjnJGmwT0hxDkuchiOLKZPPVmlM0ie4dyd7SLRXwDCrto7OF0KOf6W27DP5oF36A_xhLz3sGxZe0t8DuHjwVzGHI4EY9eZHDaWvkY2UGwwQrj6_LQRUiUn_f7X5vspvlyYR1GijaeiCxB1IL2uOAqDpLdGFwBYZFK4x9jfZCcnndE9wLwFM9nFL68iFAcooV_gC-BNE8YYb9KbSDErLIiGk33jWOl2qiqIG7ujIXjsjZ6D8dKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mq5TLwZe-NX9lK3PN8p0eCdTt7e6OXtLh21PH7GbbVVaUcWrMQDXQSE6NM4qjr1XF-R6Bi6hDp1pvF0wS6P1oB6mIAqvpMWx0aodbEkeqbk1bECCp8sqn7wGIzU_EaZstUNyybNyqATuBCHy_DYog5d_pKQ3d2oqso3UNVP0awMF1fCE_5K1SKvc0fH44hqaQGhy5aD_CVxo7DZaT2mIMiFLpPldwrp_Qx93NYTfURhdGpSgXUmUNdjXYUG51OeU9vnybHtksZYN-EGhIvrXJgNWqU0UQmgsEYTuq8mtqbpNGK_kyqp1_zz7yYdASg574251myIk8H0HDhLaoJgqxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">النائب سعود الساعدي يكشف عن هدر مالي بقيمة (4) ترليون دينار في هيئة الإعلام والاتصالات كمبالغ ضريبية بذمة شركة كورك لم يتم استيفاؤها للخزينة العامة مطالبا بتحديد المسؤول عن توقيع عقد التسوية مع الشركة دون استكمال إجراءات التحقق الضريبي، ملوّحاً باتخاذ إجراءات قانونية وقضائية بحق المقصرين في حال عدم الإجابة خلال المدة القانونية المحددة.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75675" target="_blank">📅 17:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
‏
وزير الخزانة الأمريكي متوسلا:
من المتوقع أن يدعم الشركاء الأوروبيون العقوبات المفروضة على إيران من خلال منع مموليها، وإغلاق فروعها المصرفية، وكشف شركاتها الوهمية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75673" target="_blank">📅 16:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">#رياضة
⚽️
قرعة كأس الخليج
مجموعة A:
السعودية
العراق
الكويت
عمان
مجموعة B :
الامارات
اليمن
البحرين
قطر</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75672" target="_blank">📅 16:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 16-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75671" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‏وزارة دفاع الجولاني تزعم تفكيك عبوة كانت مزروعة بسيارة ثانية في "باب شرقي" بدمشق وتعلن مقتل احد عناصرها واصابة اخرين</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75670" target="_blank">📅 16:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDnqCn1RPWL5NiH74mDD4zMHI83O7PyBnQa6zJMNRItGJkz4fYpu_OVTJ17toZFsAtLi-ffMSZqXPKF-vISCSDvUUzYuwXC-lCleXqSV5fUu1afu33g6YJYoOq_SWW2E-iX39F6cstZwlbnixSZvk7fEUeVMnIrPqUxYwHS2V6O0h5r7H_b8EsWp77IUdSucxNUXRN1JjF--aECKh43PfJNxCnUsTsk74V7U8eUM2vsDSuZ8WqfuSI-wbgnCZMVRTfvQ26PCPXgTJ_8mHdtuVIhy5WBIUp4d4Kxc3Kz9can8mSFNsK7RAZM37t092y5rwNnE2bU2Bco7cMuLl6teyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظة الانفجار في دمشق واطلاق النار العشوائي من قبل عصابات الجولاني بعد الانفجار</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75669" target="_blank">📅 15:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwaVt-KX7-Gol74tT62xh9FN1nu9N2PsPnvAWP7hvwrSgLIGu7uWhDm2vp7nf12OaIew9Vgx2fyCn1N6pYzgPAQIatVou6Dvq-SuTBuiRK-zEEWIhgn_cHscOrhF_mQRGoN5Higub2p5dK5HRKbpzGKyvWvwAXcO9d2h7RQq8_L6byXZulV9pueiY-Kh2xKVWq8q1fXxf2u2hpPRgxSZE11CNtI6rKsg_PJ2i4dL2ZHzcPvmuQtYgDta8B5zd7RpGczhhU2YHNCqob-7aqBIODZIUJTOUmbbRe8azbuungU1DTTokDjsxXBxbJvEeK2_Ia8Rf2BD4ZKb0COYd-M_gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد مقتدى الصدر:
لن أغفر لمن يتهمني بالعمالة للثالوث المشؤوم او اني عدو لآل البيت عليهم السلام لا في الدنيا ولا في الآخرة وسأقاضيهم وإن لم يأخذ القضاء مجراه فسأتعامل معهم وفق الشرع ولن أسكت عنهم</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75668" target="_blank">📅 15:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇬🇧
‏
بريطانيا:
العالم يسير بسرعة نحو أزمة غذاء عالمية بسبب إغلاق إيران لمضيق هرمز وعشرات الملايين مهددون بالمجاعة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75667" target="_blank">📅 15:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75666">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🛡
قائد عمليات الفرات الأوسط في الحشد الشعبي اللواء علي الحمداني:
نحمل القائد العام للقوات المسلحة، أي رئيس الوزراء، مسؤولية نشر قوات في الصحراء الغربية لمحافظتَي النجف وكربلاء لمنع حدوث خرق مستقبلاً، أن إفراغ هذه المناطق من القطعات العسكرية في السابق كان مخطّطاً هدفه التمهيد لمحاولة إنشاء قاعدة للكيان فيها</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75666" target="_blank">📅 15:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75665">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3002a10155.mp4?token=CBFdjuho-dv5lJHeeQ-eyYwBhr9SbfftJs39LmlYxEQDDsRfX7WESyaWuQED6miH_oHPUQkpWG89-nEkuAdTLHL2dSrS0d0FDPApKaayRpEfD9lbc1uZS5ncPieTQe9teJkAij6OFb_sKxTisxDsa-9bozboURcIX9orB2e0N6FeHWpeRZigW_-87R0pgp_a20dlImvpjhsDJ8fWjnDa6rsPrKZbYB9yz3-Bi7nHiu3J67hlthwlqsUmsPbGbdIwDw7m8z2oz-ibIpHflB28c30g8BJo7BRcFTyqZFTUoM0Rdifz_lEF8r906v0Dmy4UzcYyb1d8xok3IVY52OVqjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3002a10155.mp4?token=CBFdjuho-dv5lJHeeQ-eyYwBhr9SbfftJs39LmlYxEQDDsRfX7WESyaWuQED6miH_oHPUQkpWG89-nEkuAdTLHL2dSrS0d0FDPApKaayRpEfD9lbc1uZS5ncPieTQe9teJkAij6OFb_sKxTisxDsa-9bozboURcIX9orB2e0N6FeHWpeRZigW_-87R0pgp_a20dlImvpjhsDJ8fWjnDa6rsPrKZbYB9yz3-Bi7nHiu3J67hlthwlqsUmsPbGbdIwDw7m8z2oz-ibIpHflB28c30g8BJo7BRcFTyqZFTUoM0Rdifz_lEF8r906v0Dmy4UzcYyb1d8xok3IVY52OVqjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الانفجار في دمشق</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75665" target="_blank">📅 15:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75664">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c91c7a93.mp4?token=g7XWfrGW6BnVNNE45ubHpxnRAEKuoXEr9Zi1nZtkV9rCkXhHiVKXFV6vINwH0kcLXH6LKZhEcGcqWBDqX2qq7fUcI34mxcSFYKf8tcsjuV0lAZrsyjf9w-FIJpllSJ0TryCr4SPaCB1o54JuHQNRhu3EAArDFBn5qxVzhsBvVQI5uJBzfoBltP40Op8Lxna9GpAOQEWUdRBxAjQhcYbt8ycSdLmroWtUJMkdFby3-NiyqyQrZuDTB3Q02z_IGK2Ad94fD7c3QRwKN34bAzwiK_5VrTF-P5ZKI7JYrFuoGtgQ9xNNhkmYvb1vhAT1VfgNNqBHdJXNmrZbNtVChpgIcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c91c7a93.mp4?token=g7XWfrGW6BnVNNE45ubHpxnRAEKuoXEr9Zi1nZtkV9rCkXhHiVKXFV6vINwH0kcLXH6LKZhEcGcqWBDqX2qq7fUcI34mxcSFYKf8tcsjuV0lAZrsyjf9w-FIJpllSJ0TryCr4SPaCB1o54JuHQNRhu3EAArDFBn5qxVzhsBvVQI5uJBzfoBltP40Op8Lxna9GpAOQEWUdRBxAjQhcYbt8ycSdLmroWtUJMkdFby3-NiyqyQrZuDTB3Q02z_IGK2Ad94fD7c3QRwKN34bAzwiK_5VrTF-P5ZKI7JYrFuoGtgQ9xNNhkmYvb1vhAT1VfgNNqBHdJXNmrZbNtVChpgIcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام عصابات الجولاني: عبوة ناسفة في سيارة تستهدف مركز إدارة الأسلحة في دمشق.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75664" target="_blank">📅 15:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75663">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF3vMBpd-vU8tjmniYAS6FjcoKk0sPwNkpg-jussKHD1BVFmtJQ-Pd4kbBn41YsB4Cjo3jwqDf6TD1ILjwIeB349l2PfWFsmoOVbf927VL7CGM2GxW9J2fPYO7R6vNNlSExGn_j-8YLCa2BSbQMf-vT4YUSrHiHzh43WmO1KZqeHqHwk3FnUtQW-Cfn_skjJSVgUVtEzi4UcWCVtfJ1J94-LkjwjBEWz5XE4oeMUbUgv5XJe4C2ojKByeMWJRRxy0phxuzF353kHOFM1OBZ7UFgZpGRyfZxs80IwW1OtoMaE4I1ibCZ1TcIeFYIDwfeXW5AsIcL-CaxIVR2JGzn7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار سيارة مفخخة في العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75663" target="_blank">📅 15:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75662">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7388a4652.mp4?token=ayAxSW5EK4VTRB5qMqSc5KYRDOY78Zzj-vuq0sPRp16wtZw2DhZfTMqvUktFRxQZXtC2s1RcoThQ4NuJ3MbwM0V50mUueC4piL2wcYLRwA0DXbN8u6wCIa9IcecUc6B92q0I4R3q-p-ISzoAURF3h75-jQeU3iMfdlOz86ouJnZ0yJAKoViv3FShdFjAn9YsMH-7yjVNCLIJGDXnvc-oPS-s0KwUza1LjgZpG-hBCtt5b7jrcLrOCQoU-qtJmOGFhY9w6do2rRh61BaPkh3mSb-E17Xbroz1EOK895QcwE8QPqpVc2kMAcTOQ3YWiDO2NrYwmqFz8ZgfI7M40tBqNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7388a4652.mp4?token=ayAxSW5EK4VTRB5qMqSc5KYRDOY78Zzj-vuq0sPRp16wtZw2DhZfTMqvUktFRxQZXtC2s1RcoThQ4NuJ3MbwM0V50mUueC4piL2wcYLRwA0DXbN8u6wCIa9IcecUc6B92q0I4R3q-p-ISzoAURF3h75-jQeU3iMfdlOz86ouJnZ0yJAKoViv3FShdFjAn9YsMH-7yjVNCLIJGDXnvc-oPS-s0KwUza1LjgZpG-hBCtt5b7jrcLrOCQoU-qtJmOGFhY9w6do2rRh61BaPkh3mSb-E17Xbroz1EOK895QcwE8QPqpVc2kMAcTOQ3YWiDO2NrYwmqFz8ZgfI7M40tBqNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار سيارة مفخخة في العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75662" target="_blank">📅 15:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75661">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وكالة مهر: سماع دوي انفجارات مجهولة في جزيرة قشم.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/75661" target="_blank">📅 14:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75660">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وكالة مهر:
سماع دوي انفجارات مجهولة في جزيرة قشم.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75660" target="_blank">📅 14:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75659">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
تقارير أولية عن محلّقة مفخخة استهدفت سيارة على طريق مسكافعام في إصبع الجليل ويوجد إصابات في المكان.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75659" target="_blank">📅 14:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75658">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">"نيويورك تايمز": إسقاط طائرة إف-15إي وإصابة طائرة إف-35 كشفا أن تكتيكات الطيران الأميركية أصبحت قابلة للتنبؤ بشكل كبير</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75658" target="_blank">📅 13:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75657">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بلومبرغ: الروبل يتصدر أفضل العملات العالمية حيث ارتفع مقابل الدولار بنحو 12% منذ بداية أبريل.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75657" target="_blank">📅 12:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75656">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5330bf0831.mp4?token=KH-nyopkni_l9cYNcUJp1bkdLK0fnXAnOw8nzyKWrnoQU36Ia_g6XmU6mA-QmmnniadpiD9bLcPGt0ZFHZyalndFNKETTHZa6dDfVSC7FZtA78eenxY4n9c8gxGJiE62qeHN8-GogvwQmU4S6Vy_9e3y37xeRURHNsQgt7TiFfb_UyXODQ_qWqsqT1_cIxGTkvSz60VtYsYDySpkmt5UKW4cSHOuVay27wPmmIYx5y3cIvkwJlvhT4BE8gb7fWxTPfA9YRdDfQ_jLEBno51lKqHWhPkuOnyqY2cVZo5hvF2FjozZzgYmV-KPUK4dcfM-9qWMAwWlQOoFvhS_dqxkMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5330bf0831.mp4?token=KH-nyopkni_l9cYNcUJp1bkdLK0fnXAnOw8nzyKWrnoQU36Ia_g6XmU6mA-QmmnniadpiD9bLcPGt0ZFHZyalndFNKETTHZa6dDfVSC7FZtA78eenxY4n9c8gxGJiE62qeHN8-GogvwQmU4S6Vy_9e3y37xeRURHNsQgt7TiFfb_UyXODQ_qWqsqT1_cIxGTkvSz60VtYsYDySpkmt5UKW4cSHOuVay27wPmmIYx5y3cIvkwJlvhT4BE8gb7fWxTPfA9YRdDfQ_jLEBno51lKqHWhPkuOnyqY2cVZo5hvF2FjozZzgYmV-KPUK4dcfM-9qWMAwWlQOoFvhS_dqxkMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليق طيران حربي فوق سماء محافظة واسط العراقية.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/75656" target="_blank">📅 12:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75655">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏الصحة العالمية: قلق بالغ جراء سرعة انتشار فيروس إيبولا</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/75655" target="_blank">📅 11:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75654">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خفر السواحل الأمريكي: رصد تسرب نفطي قرب عاصمة ولاية هاواي الأمريكية</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/75654" target="_blank">📅 09:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75653">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوي انفجارات في حيفا بعد هجوم من حزب الله</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/75653" target="_blank">📅 09:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75652">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي في البرلمان الإيراني: نعمل على إطار قانوني سيقره مجلس الشورى لإدارة مضيق هرمز</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/75652" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75651">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇷
قائد مقر خاتم الأنبياء التابع للحرس الثوري الإيراني:
نُعلن لأمريكا وحلفائها عدم تكرار الأخطاء الاستراتيجية وسوء التقدير.  عليهم أن يعلموا أن إيران الإسلامية وقواتها المسلحة أكثر استعدادًا وقوة من ذي قبل، وأنها على أهبة الاستعداد، وسترد بسرعة وحسم وقوة وشمولية على أي عدوان متجدد من أعداء الوطن والأمة الشجاعة. لقد اختبر الأعداء الصهاينة الأمريكيون مرارًا وتكرارًا شجاعة الشعب الإيراني وقواته المسلحة الجبارة.لقد أثبتنا بعظمتنا وإرادة الله أننا سنُظهر سلطتنا وقدرتنا للأعداء في ساحة المعركة، وإذا ارتكب أعداؤنا خطأً آخر، فسنتعامل معه بقوة وقدرة تفوق بكثير حرب رمضان المفروضة، وسندافع عن حقوق الشعب الإيراني بكل ما أوتينا من قوة، وسنقطع يد أي معتدٍ.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/75651" target="_blank">📅 00:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75650">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaVzPwqAV1K7TzMIZ09SLjlf87cD29ebVKaaZZe40MZhV2W84o4jEUYLKNocE2vdi2H4qvJ5gloYlLDBfS5jgaH9TC1eCqc9adUCNP3l0W-Zn4CJ1A4vFzRPelm9JFm3EfDJJpUhsVXZqE-V07EB8XQBM0pltbkQs5hfpIe-ma9S2YhRlnjISVRZMTDOAujufRgVX6qTffy-ugfTBBg5Ya0hDGegktHWqMx7yPw-xnafx75tP42hTHAS1CAJLkkEeMfiiCS6mk77da-tYMburqimGpfcOVqUsi4iMSjPgAd9RXOCgGUdKWqUt7p9qK2lhHw4bm4osYd2r6Ui8F2BSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
عصابات الجولاني الإرهابية تختطف مواطن لبناني من الطائفة الشيعية من قرية كوكران الحدودية بين لبنان وسوريا وتطالب بفدية قدرها 500 ألف دولار.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/75650" target="_blank">📅 00:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75649">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjAHziouQciZtf3Jmm_BI5wgCE4Nr4TznGStwk0RWvN6NNywdpqUjwn6ZET3zlugBViHLjs1h91gKOahY-E2Gq9vlmS6gKLh6XrWzkSdMJJ_Vzc7bC4cKg5OVyLrHNrb1njhYGbQwzRXf1hMBtxfMlNlyLGbMcjLyW0WZ9tedugkoT140o9qOkZcasJESDGRkpMFlWF3DXgcTefJ0vL8bH4O721Ti3MBT6Qd38_3CFMQW_4gp1vbqqrjqkEqIpVXUKuGV6CPvTZc01YXPL3nJopad3cYcJcr0tLN07o9RlHbeSO9iFMOHOywXsw7z9jsEJhhdd97y6BtcAH748ej3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية إسماعيل بقائي:
السيد فريدريش ميرز، ‏النفاق صارخ. فالهجمات العلنية التي تشنها الولايات المتحدة والنظام الإسرائيلي على المنشآت النووية الإيرانية المحصنة لا تُقابل بالإدانة، بل بالأعذار والتبريرات. ومع ذلك، عندما تقع عملية يُزعم أنها عملية مُفبركة - والتي رفضت حتى الإمارات العربية المتحدة نسبها رسمياً إلى إيران - تلجأ هذه الأصوات نفسها فجأة إلى لغة "القانون الدولي" و"الأمن الإقليمي" الرنانة.
‏إذا كانت الهجمات على المنشآت النووية تهدد شعوب المنطقة، فيجب أن ينطبق هذا المبدأ بالتساوي على جميع الدول - وليس فقط عندما يخدم المصلحة السياسية للغرب.
‏هذا الإحساس الانتقائي بالعدالة يذكرنا بالقاضي آدم في قصة هاينريش فون كلايست "الإبريق المكسور": رجل يستدعي سوء سلوكه الذي لا يغتفر عملياً إصدار حكم، ولكنه، في غطرسة وتبرير ذاتي، يتجرأ على أخذ مكانه على منصة القضاء.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/75649" target="_blank">📅 00:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75648">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⭐️
تفعيل الدفاعات الجوية الإيرانية في مدينة أصفهان.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/75648" target="_blank">📅 23:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75647">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3da62d1b00.mp4?token=PJm14dhfpldHufk4nBWAE03S-5hANrmeSKSXzitdnx87XKDFdOFOCPdRvSQdNFqKeIbubP6U1mBoBLhfdco2qTPHFLnrvN3517clGJaxC-pMNbMjHxcBZne90eeO84a8hPMa0YyPCY3d89RFuupOKJUHbgUO4CgEIBChLMyFBFHf61AIYZN77TsC5m_XyG9Bn1akd2cDS6yhaTTk7hRrYQsK9h01rvdETN79Hzdi976R-BIKt34gv-YRuQ49rmQcMeAcoos_mDvS9mxGqJFiuJJGCqPKm0LWP6y--yfnjDMA-M3iFx2iQ0GdU5n8W6mQZ6V4dfM3WcbwwoaffxD-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3da62d1b00.mp4?token=PJm14dhfpldHufk4nBWAE03S-5hANrmeSKSXzitdnx87XKDFdOFOCPdRvSQdNFqKeIbubP6U1mBoBLhfdco2qTPHFLnrvN3517clGJaxC-pMNbMjHxcBZne90eeO84a8hPMa0YyPCY3d89RFuupOKJUHbgUO4CgEIBChLMyFBFHf61AIYZN77TsC5m_XyG9Bn1akd2cDS6yhaTTk7hRrYQsK9h01rvdETN79Hzdi976R-BIKt34gv-YRuQ49rmQcMeAcoos_mDvS9mxGqJFiuJJGCqPKm0LWP6y--yfnjDMA-M3iFx2iQ0GdU5n8W6mQZ6V4dfM3WcbwwoaffxD-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
اندلاع اشتباكات بين قوات جيش الإحتلال الصهيوني ومسلحين في منطقة حوض اليرموك بريف محافظة درعا السورية.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/75647" target="_blank">📅 23:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75646">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62de0d755e.mp4?token=JtarAwVRu5UZvQyOO9eivTKpLf2lGzfKKxo0GGPObjlHjaSkMiQ4A1bkWG-xGexoZ1AikvRU_9ExklB8MhgQknSsVVGsGPoknpcttO7NOnxBzpuw8BaoLAUiZCfwAnFBBIYiu2CLN8qdGSWgVSDeywqIyaugblCKK02LZ3jlzjl2uW7eDUKdwWQ_kLeEB1xY0YDAiQkKLWGnSwU6TZHPtKdfAjG5wDMD0LoNgYUTJX24jk9oBG9iU1pZw7dubsAU7yDaNQJSGkkkQ-8Hkyu_wUPQGqkatdkI8v4wm9BMgupiQb0UthPPsNeSazakHc-u8rVSyWl0_K7Ohj7s-sq7Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62de0d755e.mp4?token=JtarAwVRu5UZvQyOO9eivTKpLf2lGzfKKxo0GGPObjlHjaSkMiQ4A1bkWG-xGexoZ1AikvRU_9ExklB8MhgQknSsVVGsGPoknpcttO7NOnxBzpuw8BaoLAUiZCfwAnFBBIYiu2CLN8qdGSWgVSDeywqIyaugblCKK02LZ3jlzjl2uW7eDUKdwWQ_kLeEB1xY0YDAiQkKLWGnSwU6TZHPtKdfAjG5wDMD0LoNgYUTJX24jk9oBG9iU1pZw7dubsAU7yDaNQJSGkkkQ-8Hkyu_wUPQGqkatdkI8v4wm9BMgupiQb0UthPPsNeSazakHc-u8rVSyWl0_K7Ohj7s-sq7Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تفعيل الدفاعات الجوية في جزيرة قشم الإيرانية بعد رصد أجسام معادية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/75646" target="_blank">📅 23:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75645">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GYMGNi7FeAD9zyvz1u5_FrSpRa2mAl_9nJdlNLmAtBS-g9d1YvOFQrCg7Ao0zoe53DZakcV6y9_u-eS84_7NAfZgqnHge6o2macKPA0vd9ju66zx9MA0LKVCQqYt7EfWt_LxoWRYCB4qlCm4PjTsO5lCRp7rUOm1sfVgwRzEaQX89PZj7S2kcjV-aVrECTjsEQKqt4Ge_AgkkVfOYyVQz7pgh1gWUCQALjoPEawdZlxvYM8C5Fq93LG083aEUZTltOEriKaWqIGg5onM06rmI8ZayzvI1pg1rHbfB0pxGr7YrZI2uymvRa3zVAxVlzZ-n2xcNF2ZaxwdiAHWslR-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
في ولاية ماريلاند، أرسلوا 500,000 بطاقة اقتراع بريدية غير قانونية، وتم القبض عليهم! والآن، سيرسلون 500,000 بطاقة اقتراع بريدية أخرى، لكن لا أحد يعرف ما يحدث مع أول 500,000 بطاقة أرسلوها. بالإضافة إلى ذلك، ذهبت العديد من هذه البطاقات إلى الديمقراطيين، لذلك لا توجد فرصة لأي جمهوري يترشح في ماريلاند! تم ذلك من قبل حاكم الولاية الفاسد، ويس مور. لقد سمح بحدوث ذلك للتأكد من فوز الديمقراطيين. لم يكن من المنطقي بالنسبة لي أبدًا أن تُعتبر ماريلاند ولاية ديمقراطية تلقائيًا، لكنني الآن أفهم السبب. أنا متأكد من أن هذا استمر لسنوات. سأطلب من المدعي العام للولايات المتحدة ووزارة العدل إجراء تحقيق فوري في هذا الوضع.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75645" target="_blank">📅 23:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75644">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b5c3d572.mp4?token=CBjgVtpQNsv9uGBX-qvq006LqhbxVYif8s_XbgflkpGz5pRYIlIDEuzu-QEEvR4oMcLDRR4IrMVi2T20B8f926MRvcfvUaBaemDoAZa0tg9RQd9Z1kRVVKiwmzYK9zKdzhG1Vnx6WBod4wg_DhJ_TAH7KC0Ac7JJQXknVIXQKWdsqkDUmtYl0KQ2goRX6_JIL0wOzTgn6wz7MDT3zY-k98iGgSADU8fqSp4nR5KctEZfLWuXmwE4bV8k-OtBhv2DChW6fNpq1C8fuL5F7qGRq_oUCEQ7Ocz2aGmKnId7SVufpRIk0ooMZEehIR-pZIYwEJlm7JWxiMjg2hOrDFhRHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b5c3d572.mp4?token=CBjgVtpQNsv9uGBX-qvq006LqhbxVYif8s_XbgflkpGz5pRYIlIDEuzu-QEEvR4oMcLDRR4IrMVi2T20B8f926MRvcfvUaBaemDoAZa0tg9RQd9Z1kRVVKiwmzYK9zKdzhG1Vnx6WBod4wg_DhJ_TAH7KC0Ac7JJQXknVIXQKWdsqkDUmtYl0KQ2goRX6_JIL0wOzTgn6wz7MDT3zY-k98iGgSADU8fqSp4nR5KctEZfLWuXmwE4bV8k-OtBhv2DChW6fNpq1C8fuL5F7qGRq_oUCEQ7Ocz2aGmKnId7SVufpRIk0ooMZEehIR-pZIYwEJlm7JWxiMjg2hOrDFhRHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
إنفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75644" target="_blank">📅 23:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75643">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">⭐️
إنفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75643" target="_blank">📅 23:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75642">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd6f7973f.mp4?token=NG8TyaXq-_UOxjED8FJxep3N7W5KPu1i1mWJUVsq38osi-LSgROMRQWaOwOuAZI9nBBNuOvfLAxCgkV6Z2kiLYi0P4aBK1SAs2BzNE1233OC2FJBaxzB7sIeQGqJXQSjN5BlZPgj4FoiaNzKufnUKIlC35XjaoB8IUdh_n3z5RU2wExzjwd6SC-G_JIbNcH3Xhay9Zy7pvgBFHmmULK0EQ0GTA29FCnpVaT9SWI31Wu4Gj3ym5aF6-lHNHU9P6TFmr0zKRSg65yPI0fMoY2Ir_PQ3qPXGqn8ihe89SqbYseBTgVZ6xVxCkboAyv58e6yQTUVkWIN8jvKEyaiCRzyVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd6f7973f.mp4?token=NG8TyaXq-_UOxjED8FJxep3N7W5KPu1i1mWJUVsq38osi-LSgROMRQWaOwOuAZI9nBBNuOvfLAxCgkV6Z2kiLYi0P4aBK1SAs2BzNE1233OC2FJBaxzB7sIeQGqJXQSjN5BlZPgj4FoiaNzKufnUKIlC35XjaoB8IUdh_n3z5RU2wExzjwd6SC-G_JIbNcH3Xhay9Zy7pvgBFHmmULK0EQ0GTA29FCnpVaT9SWI31Wu4Gj3ym5aF6-lHNHU9P6TFmr0zKRSg65yPI0fMoY2Ir_PQ3qPXGqn8ihe89SqbYseBTgVZ6xVxCkboAyv58e6yQTUVkWIN8jvKEyaiCRzyVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
مقتل شخصين على الأقل وإصابة آخرين في إطلاق نار على مسجد في مدينة سان دييغو بولاية كاليفرنيا الأمريكية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/75642" target="_blank">📅 23:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75641">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX4d5lW6Vv36u-yn8wE5sOEAAltPvR8OOdEKAS7W4El9EiPVY1BLjh5MD532beGcEFQrRe_zmYr9fVsW1oIYph2CgDZKzY0he2RxSkfuVmek7GahgTO20u1bxHdOOP1c2gJN7Am8-3EqHApKJv9ABWPoQP4javZhux0vaMg2im_nUlDRqq3tgAQ1dvK1ezeOBiA0d9_aUorrcvLi0u1GKugmak08hggHzkYUqBhiSu--nLHX7vmv1Wi3CEyxoufSijVaEfk0bszQHoGXLRdn7NGAtsAMbmmXqyD6zYY9_SfUskT1Wg8t5LX7ExGkW9eP6-2LDoo1v4R96Ag7l5uCBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
ترامب يجبن أمام إيران الإسلامية:
لقد طُلب مني من قبل أمير قطر، تميم بن حمد آل ثاني، وولي عهد المملكة العربية السعودية، محمد بن سلمان آل سعود، ورئيس دولة الإمارات العربية المتحدة، محمد بن زايد آل نهيان، أن نؤجل هجومنا العسكري المخطط له ضد جمهورية إيران الإسلامية، والذي كان من المقرر أن يحدث غدًا، حيث أن مفاوضات جادة تجري الآن، وفي رأيهم، كقادة كبار وحلفاء، سيتم التوصل إلى اتفاق سيكون مقبولًا للغاية للولايات المتحدة الأمريكية، وكذلك جميع الدول في الشرق الأوسط، وخارجها. سيشمل هذا الاتفاق، على نحو مهم، عدم وجود أسلحة نووية لإيران! بناءً على احترامي للقادة المذكورين أعلاه، أوعزت إلى وزير الحرب، بيت هيغسيث، ورئيس هيئة الأركان المشتركة، الجنرال دانيال كين، والجيش الأمريكي، أننا لن نشن هجومًا مجدولًا على إيران غدًا، لكنني أوعزهم أيضًا أن يكونوا مستعدين للشروع في هجوم واسع النطاق على إيران، في أي لحظة، في حالة عدم التوصل إلى اتفاق مقبول. شكرًا لكم على اهتمامكم بهذا الأمر!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75641" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75640">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
تفعيل الدفاعات الجوية في جزيرة قشم الإيرانية بعد رصد أجسام معادية.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75640" target="_blank">📅 22:23 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75639">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZF5M5qKCntNFBl9LucgwuZKGKhdtz6L8DcGnPOsXrmfd6gCJSgNMZ713ph3VVBwKCV0JL2N9shq6Xx-DNmYdeLTseOHQuWEr2ORZjDYPKa8Ocodv_6llBYZJJjZlQi6dcjtotVCvklCByuY78GngKPAgjJHmQh6AaSbDn8d5FuKgJO1DoGnZmYrRt-Rd1zZEbuOlplFxjDQ2impt4ulr5qKZnc6tKEydc2bqVzqKguiDLWF4MBRNQEgOeYyJWyJ_N9u6hpWQ-H6yKDkouXoGYIqDk-J3x3TJ_omXCMe_nN9FMGxuwlIIRFKiK2eLsNQTweK-EdChqQAnGyNB7_fTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
أسعار النفط ترتفع لتتجاوز 112 دولاراً للبرميل الواحد.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/75639" target="_blank">📅 22:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75638">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6kqyg8dL3vWow0NLCbjnbDVoKBVr5AY6aZP_kqy9obWM2DrkVC4aXXCQbf3JZzFRAdIblz-kiNOH-qMB9gbn_-5buU3YOIrD1oCdXI1E9iyw24cLhpVaW76AVl-KdQJsv1SA3oidcW1RdWb0MZUS8_HDLAxqEyS3mNVqq--ngkScPyjOi_zKksmpY-PYZFPDmG5McoCd7rnrLIU6Ct4UZNWs1AdJAl7bi5r9QwLL9zX40I7uC4YAox5AxS72VQTGPUQ7TWFTsLi5j4D50iXKlObv1ydZL6zURcm5bJP3uloUy6FH-I2Od1t7PVTlsaZqZIcvyQkQoA_bJsjxKX7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بزشكيان:‏
الحوار لا يعني الاستسلام. تدخل الجمهورية الإسلامية الإيرانية في حوارٍ بكرامةٍ وسلطةٍ وحمايةٍ لحقوق الأمة، ولن تتراجع بأي حالٍ من الأحوال عن الحقوق القانونية للشعب والبلاد. سنخدم الشعب ونحمي مصالح إيران وكرامتها بالمنطق وبكل قوتنا حتى آخر رمق.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75638" target="_blank">📅 21:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75637">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea61dffae.mp4?token=jxqt0VUajtl1GipcyjjAfUpDkpGodmvP9qg3jn-7BALp2-5EYqoBZJzSIJcskCW61LupC4Hrv4DSadiOKNE8XbqNvi4_jj0eU-mVfnzvhkPemF_TedYN5Zf3EHPGLoD-n9pOMBQMTWjrgSB9HPTTp_neeLR70dtVnYeqjmzM44L8MN7rGZ1I7RAEd00LLU2rL9xnVHT3NbX5GVGbiOnTWb0bRI_Qc5sJoyaw7X0VGBuAmBXHNVLUhQouSpxkWEuNvNPlLZs3hz2WbZfQgQfWec_pLCYK7xEWr_HoUAFfAgbrzcwnaDw-uA3pwuR_vr7DpphRXwDwBvw-8IMcuJbfFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea61dffae.mp4?token=jxqt0VUajtl1GipcyjjAfUpDkpGodmvP9qg3jn-7BALp2-5EYqoBZJzSIJcskCW61LupC4Hrv4DSadiOKNE8XbqNvi4_jj0eU-mVfnzvhkPemF_TedYN5Zf3EHPGLoD-n9pOMBQMTWjrgSB9HPTTp_neeLR70dtVnYeqjmzM44L8MN7rGZ1I7RAEd00LLU2rL9xnVHT3NbX5GVGbiOnTWb0bRI_Qc5sJoyaw7X0VGBuAmBXHNVLUhQouSpxkWEuNvNPlLZs3hz2WbZfQgQfWec_pLCYK7xEWr_HoUAFfAgbrzcwnaDw-uA3pwuR_vr7DpphRXwDwBvw-8IMcuJbfFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بيت هيغسيث يقوم بتقليد ترامب.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/75637" target="_blank">📅 21:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75636">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyIrqkbf6mSdEz8-psZdxaHMjGXoar4QLJ3DBdKz73L78IOJdcrfVXOtmWvoR75ErHX0fdCPF-pK6yVoSpBU3OdTMRKDDu4FvNXmhIc9eMMk0Xb8SoTfhlFHgkVs9o20zXolRKnEeaz2oClwPk_gdhxc9t4hNONy8EF6CsYXLGAqVdWWxjYo2zhW5Qdw2W6458plnjt4hZSwxZatKC9vUqaTLRsdi2Hs3nRbISavYjwevaDv-IjLsS8Nz_axooZmx2CO3RJ8ZL4ASApNuAKBhwu9UMSs7xVdRd7yxGMM2y86x2AmK2eu7qu2Pyz1pYSXwKVJuHAO-30phxHkTXlD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
يجب طرد عضو الكونغرس من الدرجة الثالثة توماس ماسي، وهو جمهوري ضعيف ومثير للشفقة من ولاية كنتاكي العظيمة، وهي مكان أحبه، وقد فاز ست مرات، بما في ذلك جميع الانتخابات التمهيدية، من منصبه في أسرع وقت ممكن! إنه أسوأ عضو كونغرس "جمهوري" في التاريخ، حيث صوت ضد تخفيضات الضرائب، والجدار، وإنفاذ القانون، ولصالح تشويه المتحولين جنسيًا لأطفالنا، ولعب الرجال في الرياضات النسائية، والعديد من الأشياء الفظيعة الأخرى.
لقد منحنا الشعب الرائع للدائرة الرابعة في ولاية كنتاكي تفويضًا لجعل أمريكا عظيمة مرة أخرى، والشخص الذي سيساعدنا في القيام بذلك هو ضابط البحرية الخاص، وضابط رينجرز الجيش، ومزارع من الجيل الخامس في كنتاكي، الكابتن إد جالرين، وهو وطني حقيقي يضع أمريكا أولاً
بصفته جنديًا مخضرمًا شجاعًا، يعرف إد الحكمة والشجاعة اللازمتين للدفاع عن بلدنا، ودعم جيشنا/قدامى المحاربين، وضمان السلام من خلال القوة. بالإضافة إلى ذلك، وبصفته رجل أعمال ناجحًا للغاية، يعرف إد كيفية خلق وظائف رائعة، وخفض الضرائب واللوائح، والترويج للمنتجات المصنوعة في الولايات المتحدة الأمريكية، ودعم مزارعينا المذهلين والزراعة الأمريكية، وإطلاق العنان للهيمنة الأمريكية في مجال الطاقة، والدفاع عن العصر الذهبي لأمتنا. في الكونغرس، سيناضل بلا كلل للحفاظ على أمن حدودنا، ووقف جرائم المهاجرين، والدفاع عن التعديل الثاني لدستورنا الذي يتعرض دائمًا للهجوم
شعب كنتاكي العظيم يدرك حقيقة ماسي. إنه يصوت فقط ضد الحزب الجمهوري، مما يسهل الأمور على اليسار الراديكالي. على عكس ماسي "الخفيف"، الخاسر غير الفعال الذي خذلنا بشدة، فإن الكابتن إد غالرين فائز ولن يخذلكم. يوم الانتخابات هو الثلاثاء 19 مايو. صوتوا لإد غالرين - إنه يحظى بتأييدي الكامل والتام. لنجعل أمريكا عظيمة مرة أخرى!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/75636" target="_blank">📅 21:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75635">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🌟
🏴‍☠️
توثيق آثار بعض استهدافات المقاومة الإسلامية لآليات وتموضعات جيش العدو الإسرائيلي في بلدة طيرحرفا جنوبيّ لبنان.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/75635" target="_blank">📅 21:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75634">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
السيد عبدالملك الحوثي:
على المستوى العسكري نحن جاهزون إن شاء الله لكل التطورات.
ثابتون على مواقفنا المبدئية الواضحة التي أكدنا عليها مرارا وبشكل عملي، وجاهزون لأي تطورات قادمة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75634" target="_blank">📅 21:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75633">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d7fed53b3.mp4?token=o0BBBTt5uvXekcqchhpXd1SfrZGL3HseDB8gP4J0KreKQAVzrIwXiKaKoBMYRfARzhzc-Ug6CnN2Z1NAEV7cHIixanCzvB6Zd2hM1xM15GHSQrgUZDL_ev95AfZeDge4YM1gCUoQOIjjr_i1P_sHkAVakXAKL52rsIVrTMBrG51DuuhJqJ5T_ws3Wy2XwgBJxEyjW70ywEsUE4bcUXYUeM3ZUZgvY0c0K784BJrckHtAqcFyWqRbIYjfiKQWbxfsw5b7ugenogoysaGziedtY5HbDxbkZIeGhkGbjvJP_i_eSAqnPA2G8pyrFlF5sYMRcbnc8q7SZSnVAWrg397EIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d7fed53b3.mp4?token=o0BBBTt5uvXekcqchhpXd1SfrZGL3HseDB8gP4J0KreKQAVzrIwXiKaKoBMYRfARzhzc-Ug6CnN2Z1NAEV7cHIixanCzvB6Zd2hM1xM15GHSQrgUZDL_ev95AfZeDge4YM1gCUoQOIjjr_i1P_sHkAVakXAKL52rsIVrTMBrG51DuuhJqJ5T_ws3Wy2XwgBJxEyjW70ywEsUE4bcUXYUeM3ZUZgvY0c0K784BJrckHtAqcFyWqRbIYjfiKQWbxfsw5b7ugenogoysaGziedtY5HbDxbkZIeGhkGbjvJP_i_eSAqnPA2G8pyrFlF5sYMRcbnc8q7SZSnVAWrg397EIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
حادث سير في تل أبيب المحتلة ؛ مقتل وإصابة 10 مستوطنين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75633" target="_blank">📅 21:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75632">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف طائرة حربية بصاروخ ارض جو في البقاع الغربي اللبناني.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75632" target="_blank">📅 20:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75631">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇺🇸
🇮🇷
رويترز: أميركا ترفض المقترح الإيراني الجديد.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75631" target="_blank">📅 20:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75630">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🌟
🏴‍☠️
حزب الله يعلن عن استهداف آليّة قائد الّلواء 300 التّابع لجيش العدوّ الإسرائيليّ في مستوطنة شوميرا بمحلّقة انقضاضية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75630" target="_blank">📅 19:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75629">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭐️
أكسيوس:  أن البيت الأبيض لا يرى في اقتراح إيران الجديد تحسينًا مجديًا أو كافيًا للتوصل إلى اتفاق.   وقال مسؤول إن الاقتراح يحتوي على تغييرات طفيفة فقط مقارنة بالإصدارات السابقة. وفي حين أنه يوسع النص حول عدم سعي إيران للحصول على سلاح نووي، إلا أنه لا يزال…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75629" target="_blank">📅 18:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75628">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">⭐️
أكسيوس:
أن البيت الأبيض لا يرى في اقتراح إيران الجديد تحسينًا مجديًا أو كافيًا للتوصل إلى اتفاق.
وقال مسؤول إن الاقتراح يحتوي على تغييرات طفيفة فقط مقارنة بالإصدارات السابقة. وفي حين أنه يوسع النص حول عدم سعي إيران للحصول على سلاح نووي، إلا أنه لا يزال يفتقر إلى التزامات مفصلة بشأن تعليق تخصيب اليورانيوم أو التخلي عن المخزونات الحالية من اليورانيوم عالي التخصيب.
ورفض المسؤول أيضًا التقارير التي تفيد بأن واشنطن وافقت على تخفيف العقوبات، قائلاً: "لن يحدث أي تخفيف للعقوبات مجانًا" دون اتخاذ خطوات متبادلة من جانب طهران.
وقال المسؤول: "نحن حقًا لا نحرز الكثير من التقدم. نحن في موقف خطير للغاية اليوم". وأضاف: "إذا لم يحدث ذلك، فسيكون لدينا محادثة من خلال القنابل، وسيكون ذلك أمرًا مؤسفًا".</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/75628" target="_blank">📅 18:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75627">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6FiM4HrbMPnWFeLIZ3Fu--3L1Rn-mAg-su_7qZEOo6xeejZpUW6DvKCgS_kJRiNCvEzaa2oiyBMsVRCd_Qpzm274zD3OrDZe772Dx2vAHj_BXWClhDgAHJmCY1kUmaFXysDgD7NdtYhAlzpo7begi1NgPDWPg3ZBYCzuWO7c-1CZS8hVy0ayINwTRqCUW1_L50nqhwNkdROQRWhmmtg3qxMfMVWhloLh5_miF2V1bAJPoj6NpE9ybz8VFfCNqRjHrMMFYuJRMamLE0-upZbdjqn-n8xIrVnojdIL9c4hG085gh23bsa_yTcFVyYR6IZ1sN0ajKof8Z6Rkek7datqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐦
بيان للمسؤول الأمني لكتائب حزب الله أبو مجاهد العساف</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75627" target="_blank">📅 18:17 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75626">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1ux8pk2pUlIIcb6LaOQPsb_HTBVx0e6cI8gt0mZwfmKuR8XMtaO1u_l1odSOZB5kmrx9MkM1IHSGqPdVIfniS4eP09S5Q9IoOA0x-MGk3HQtGXCKjRnjUWuXPWAK6I8V47JJ5sZS3xkRxfJXgLXjSE_LbWYNAjlYoDHpnU3TAb28tX33MwObI9qaEpEiYudvjp_vNU9Bf4rX_b_uAl4rCeDb18OaQY74VPHuQD81UhLBMRJOVHIdUZMKlbxzIOiUzeSXTY4FudBZtFXATvl4e0gHPgXAcJ6WzT_uYkrkvNnXdTCZzTLercEr2Cn_S7fCRcJSkOwUZW6Xh5NwtB5IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
دونالد ترامب:
إذا استسلمت إيران، واعترفت بأن أسطولها البحري قد غرق في قاع البحر، وأن قواتها الجوية لم تعد موجودة، وإذا خرج جيشها بأكمله من طهران، وقد ألقوا أسلحتهم ورفعوا أيديهم عالياً، وهم يهتفون "أستسلم، أستسلم" بينما يلوحون بالراية البيضاء، وإذا وقّع جميع قادتها المتبقين على "وثائق الاستسلام" اللازمة، واعترفوا بهزيمتهم أمام القوة العظمى للولايات المتحدة الأمريكية، فإن صحيفة نيويورك تايمز الفاشلة، وصحيفة تشاينا ستريت جورنال (وول ستريت جورنال!)، وقناة سي إن إن الفاسدة والتي فقدت مصداقيتها، وجميع وسائل الإعلام الأخرى التي تنشر الأخبار الكاذبة، ستنشر عناوين رئيسية مفادها أن إيران حققت نصراً باهراً على الولايات المتحدة الأمريكية، وأن الأمر لم يكن متقارباً على الإطلاق. لقد ضلّ الديمقراطيون ووسائل الإعلام طريقهم تماماً. لقد جنّوا تماماً!!! الرئيس ترامب"</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75626" target="_blank">📅 18:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75625">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzfv4nftA-Me8RpZpNkQYNtDxN7YltPs8ljgdnEIhWpwB4Qbk2JPuSqBQVkfD9uM7rmKrNcbOwRJzXhOR3Fl2K93jU0zYUQLbupuBrQVFVH-9kl7fXhTcmyEu00kdiq_d-qU9-ONSM2boQYp5oU-JZ5OistE6KhFCScDe_CFWwJRTR7oPVyqJEIK7ULcjlpGMv_PyayEoWrw_dvTFSMYUztn7yE5pS3XhtEG6N871UjgVz-Xu32Qn0WRYooczFit2_1dHCZYDBPe8Yadu-rDe7j9LkK1b1gktT7HMyh4NIwYkANi7nAsWOndRl4Q3ObpZZYmIkiIUqzM5dqg2ju9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐦
بيان للمسؤول الأمني لكتائب حزب الله أبو مجاهد العساف</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/75625" target="_blank">📅 18:10 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75624">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سوالف الگهوة
رئيس الوزراء الباكستاني يزور العراق يوم الخميس القادم</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75624" target="_blank">📅 17:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75623">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
‏مصدر إيراني لرويترز: أميركا أبدت مرونة فيما يخص القيود المفروضة على البرنامج النووي، سنناقش القضية النووية في مراحل لاحقة.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/75623" target="_blank">📅 17:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75622">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇮🇷
‏
مصدر إيراني لرويترز:
أميركا أبدت مرونة فيما يخص القيود المفروضة على البرنامج النووي، سنناقش القضية النووية في مراحل لاحقة.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/75622" target="_blank">📅 17:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75621">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
وزارة الخارجية العراقية:
لم يتم تأشير أي معلومة من خلال وسائل الدفاع الجوي والمعدات البصرية العراقية لاستهداف السعودية من الاراضي العراقية وفي هذا الإطار، تدعو الوزارة الجهات المعنية في المملكة العربية السعودية الشقيقة إلى التعاون وتبادل المعلومات ذات الصلة، بما يسهم في التوصل إلى معلومات دقيقة تعزز الأمن والاستقرار لدى البلدين الشقيقين.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/75621" target="_blank">📅 16:45 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75620">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇱🇧
🇮🇶
إعلام لبناني: قدّم العراق للبنان نفطاً بقيمة ملياري دولار لمنع العتمة الشاملة ولم تقدّم الحكومة اللبنانية إدانة للإنزال الإسرائيلي في صحراء النجف</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/75620" target="_blank">📅 16:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75619">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUfTNnOeXuNcX-Fl1m-mjv79dr7k_ykvhMr4JoYnf3IjvWq_YYaZqQqxLh0rJUHtUxu5BtUeNoPiKDj7vTJlRL4pL5fpwVaRUEHISemcK8H4XFXXWqvHjkoSjRxEYQA8_19wpGDGn8SnPCQSsdMssget8MlAQW3Abx5Y5s5m2ViM0FBO5gMQEu56DzOieOe3LkvefhmfveEylxKxqBxtw7SVKbWhGeZB-tTJeZTX4JpnQlC2eP-55DNHubcpJkZw3qL_LTzB_0v4h5GW0kdeIEtOvc2VKVAMcieK-gXSg4DWkdj_LbKOtVZ8wH68Hs0JinC33CziSItX-XDKbj-LDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئاسة جامعة الإسراء توضح حقيقة الملابسات عن ما حدث في جامعة الإسراء الأهلية في العاصمة بغداد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75619" target="_blank">📅 16:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75618">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📰
‏
نيويورك تايمز:
أميركا وإسرائيل تستعدان بشكل مكثف لاحتمال استئناف حرب إيران هذا الأسبوع، الاستعدادات هي الأكبر منذ وقف النار</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/75618" target="_blank">📅 15:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75617">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صافرات الانذار تدوي في كريات شمونة ومحيطها بعد هجوم صاروخي لحزب الله</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75617" target="_blank">📅 15:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75616">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
وكالة تسنيم عن مصدر مقرب من فريق التفاوض:
الأمريكيين خلافاً لما ورد في نصوصهم السابقة، وافقوا في النص الجديد على رفع العقوبات عن النفط الإيراني خلال فترة المفاوضات. رفع العقوبات يعني رفعها مؤقتاً. تُصرّ إيران على أن رفع جميع العقوبات المفروضة عليها يجب أن يكون جزءاً من التزامات الولايات المتحدة.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/75616" target="_blank">📅 15:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75615">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بعد منع ناقلة تحمل نفط عراقي من المرور.. المتحدث باسم القيادة المركزية الامريكية: قواتنا منعت ناقلة النفط آجيوس فانوريوس من عبور هرمز لانتهاكها الحصار. ناقلة النفط كانت ترفع علم مالطا ولم تكن محملة بنفط إيراني</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75615" target="_blank">📅 15:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75614">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تصرفات معيبة وممارسات غير أخلاقية من بعض المحسوبين على العتبة العباسية بحق رجل دين كرس جهده للعمل الإنساني وخدمة المظلومين بعد مشاركته في حملات دعم إنسانية للشعب الإيراني المظلوم خلال حرب رمضان، هذه المواقف النبيلة قوبلت بالتضييق والاستهداف داخل العتبة وانعكست بشكل مباشر على وظيفته حتى وصل الأمر إلى ظلمه وإجباره على التقاعد بطريقة تفتقر للإنصاف والوفاء لتاريخه ومواقفه الإنسانية</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75614" target="_blank">📅 14:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75613">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الانسحابات متواصلة.. انسحاب النائب عمار يوسف من ائتلاف السوداني.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/75613" target="_blank">📅 14:43 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
