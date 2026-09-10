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
<img src="https://cdn4.telesco.pe/file/JK7-_qx5xkL0QfOBTABpiRDGfAP6DZIezg0aiFdXkUxBC-Zrb4VPuPPuNw_Bc0m-qOXRa2QeRVvJdSivWR8cY5psj5ZKwB_VwPEk1fmL7x_nnb9nbLKl60rRRIfU7ou7EgnlirDMo-k-zJ17l2rk1qNQi8puLcKLXptNaWF6cAf_hNkOG_ev-lYeDfpOBcgZ6RoiPSp6G42MFmWVWYQBY_HPueEknxznaj11sMoWobfyZ3wUBAae7FmYMFp2zZDjnf2AbqPOl4g0NyaC3soCUbT-AK_Ob9UYSiCdRWnEm-NcABo1pfy9gV9bN0uFW1_mlMPuY7UEKckFlsiD21t7wQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 19:02:49</div>
<hr>

<div class="tg-post" id="msg-90072">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9003eba0.mp4?token=e4R-XlfTx7wzCAe840gaC63AEedoUTlbQ99okv5wKTKof0BN-L6644-culcdj1FfsMFbPHQtK93W_SJorh74o79IhvAMM9CNgdl794Lm5Mk9xwPuZjcLGbFQygcurTauIGGKZm2pVg_oLJZVHx22P9qALnNIyZ9_Bp2qMkD1WTqSH2DDf7Ex-EMBrINzyiHvCEJo__rqzM7ARK9zezskSm-OktLv4GRjG1bAF11slbLfGrLTvVOIVEpdnbspNX-VMk96U1N_ZMFvP9hY0IeyT9LEkF3biIVqxnp-xdW-Cu8KJVFsaNqCIlAF7LdScKaU23YwUdDVLEVB5akXpc2FmS3Typ6K6yrEHy_98q2SIpCQYH1oPvW02PbWylXBkfpsd2tvCF21Zj7pArAh954Zc2I6KdPpfKHaKKNrlTuETWQXhjZbgBOcleJSQxSiBHWy5QB5F_gxIZoTm7iOA_mygSI1tlo-xvV0luf1kostIWVXAcvBAYpgXbvEQ4_lX1tO-jRQOFT6bE8Mog3ITmfN0OOfOqOJsXlCVJJp-iAOx9C1hOzz6Z12iHhSEp9FYNLiR8WThDNkNaZne-c29hWPrWARlHmhB8QGynYZNw_mcP5p8porJ84dUJhcf4szukyCGbUo2jAwJVWeuXlY-CNV8g7yPpM288IGSgP1cQEqnfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9003eba0.mp4?token=e4R-XlfTx7wzCAe840gaC63AEedoUTlbQ99okv5wKTKof0BN-L6644-culcdj1FfsMFbPHQtK93W_SJorh74o79IhvAMM9CNgdl794Lm5Mk9xwPuZjcLGbFQygcurTauIGGKZm2pVg_oLJZVHx22P9qALnNIyZ9_Bp2qMkD1WTqSH2DDf7Ex-EMBrINzyiHvCEJo__rqzM7ARK9zezskSm-OktLv4GRjG1bAF11slbLfGrLTvVOIVEpdnbspNX-VMk96U1N_ZMFvP9hY0IeyT9LEkF3biIVqxnp-xdW-Cu8KJVFsaNqCIlAF7LdScKaU23YwUdDVLEVB5akXpc2FmS3Typ6K6yrEHy_98q2SIpCQYH1oPvW02PbWylXBkfpsd2tvCF21Zj7pArAh954Zc2I6KdPpfKHaKKNrlTuETWQXhjZbgBOcleJSQxSiBHWy5QB5F_gxIZoTm7iOA_mygSI1tlo-xvV0luf1kostIWVXAcvBAYpgXbvEQ4_lX1tO-jRQOFT6bE8Mog3ITmfN0OOfOqOJsXlCVJJp-iAOx9C1hOzz6Z12iHhSEp9FYNLiR8WThDNkNaZne-c29hWPrWARlHmhB8QGynYZNw_mcP5p8porJ84dUJhcf4szukyCGbUo2jAwJVWeuXlY-CNV8g7yPpM288IGSgP1cQEqnfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية من داخل مدرج مطار المخا الدولي.</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/naya_foriraq/90072" target="_blank">📅 18:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90071">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">العدو السعودي يشن نحو 10 غارات على مديرية ذو باب.</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/naya_foriraq/90071" target="_blank">📅 18:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90070">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">العدو السعودي يشن نحو 10 غارات على مديرية ذو باب.</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/naya_foriraq/90070" target="_blank">📅 18:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90069">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجارات تهز مضيق هرمز</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/naya_foriraq/90069" target="_blank">📅 18:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90068">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇾🇪
🇾🇪
‏مركز تنسيق العمليات الإنسانية في اليمن يُبلغ جميع شركات الشحن العالمية بأن الملاحة في البحر الأحمر آمنة لجميع الشركات، باستثناء الحظر السابق على السفن السعودية.</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/naya_foriraq/90068" target="_blank">📅 18:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90067">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇾🇪
🇾🇪
‏
الاستاذ محمد عبدالسلام - الناطق الرسمي لانصار الله:
‏إن ما قامت به القوات المسلحة اليمنية في بعض المناطق الساحلية عملية وطنية في إطار فرض السيادة اليمنية، والتعامل مع التحديات والأطماع التي تهدد السلم الأهلي.
‏إن السلام الحقيقي والعادل والمشرف كان وسيبقى خيارنا الاستراتيجي، وأن على الجميع أن يدرك بأن خيار السلام مع اليمن هو الأقل كلفة والأقصر طريقا نحو إعادة تنظيم العلاقات وفق مبادئ حسن الجوار والاحترام المتبادل والمصالح المشتركة.
‏إننا نؤكد أن الجمهورية اليمنية ليست لديها أي مطامع في أي دولة من دول الجوار أو الدول العربية والإسلامية وغيرها من دول العالم، ولم تعتدي على أي دولة بل هي من تم الاعتداء عليها بما يتنافى مع الأخوة الإسلامية والعربية.
‏أما بشأن حرية الملاحة وحركة التجارة الدولية في البحر الأحمر وباب المندب فهي آمنة ومنتظمة، ولا داعي لأي قلق دولي حيالها، فليس عليها أي خطر من جهة اليمن، والعمليات الجارية حالياً هي محددة الأهداف وفق ما تم الإعلان عنه سابقا وتأتي في الإطار الدفاعي، ومتى ما توقف العدوان على اليمن وتم رفع الحصار عنه، فسوف تتوقف العمليات الحالية .</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/naya_foriraq/90067" target="_blank">📅 17:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90066">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f39dbddee2.mp4?token=KfgwbqNIyZnOWqujcSmPzFdt05YnFB6Zii1JFRW3TnDlVnjx1LgDZ1jYvmejLYM3ENQ3cAxgAW1M5bJDYtc8EATE348DdJZx8jV-p7bgxl1wRi-q8boswAdLHOTWGw1whEM_FWRDhm9bq6_hXyK38kvp_Mq8-Rz7M8UytBhoXYVp_Cg5TyAX6TsLEwRSwJJHd6IR2b1xfcX18tSKAJ1cB2-xdolImf3bOxkuMLawPrduWjSMwWkCv05WjgrU-QY9zP6IhW2l1qJPNajVitRyFdQC7RjyNvjMdvdcMQqh-EP0oN-JGehWqWYZG_Jx9UhvB6cB_OoYoeIPFaboeFVlzBmT7XEJi5V04rbtSp7izbAwhkfGfN7zCoJ4ojvaE8xHwAZ3WYHlKSW6AoRNKMdpp7mV6JvKdoPf7eZ1pCKjb72hUIXM4p6Dmh-PDSLRA1bYS_34pEEqkN53ehJ5ZxihGhJ3FFzVkBejt9cXYtvtjJKmHoCITqyowCa0WQJG_D7uJ-cErI5bOqOP0Tlyt4sfZaDhQXIj664VKsryuct4rOCRgCJusj8JxpyAW08v8pXS7agMXP7jfT5TvMSd-gBxs0JtC34Slf3cI4xUUlONnsp_nZvnX6OKFvizlWXWAOU1trHZB4VeuRMXzoYXVzb-a1V43x56BZ30nb3wBsCdF1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f39dbddee2.mp4?token=KfgwbqNIyZnOWqujcSmPzFdt05YnFB6Zii1JFRW3TnDlVnjx1LgDZ1jYvmejLYM3ENQ3cAxgAW1M5bJDYtc8EATE348DdJZx8jV-p7bgxl1wRi-q8boswAdLHOTWGw1whEM_FWRDhm9bq6_hXyK38kvp_Mq8-Rz7M8UytBhoXYVp_Cg5TyAX6TsLEwRSwJJHd6IR2b1xfcX18tSKAJ1cB2-xdolImf3bOxkuMLawPrduWjSMwWkCv05WjgrU-QY9zP6IhW2l1qJPNajVitRyFdQC7RjyNvjMdvdcMQqh-EP0oN-JGehWqWYZG_Jx9UhvB6cB_OoYoeIPFaboeFVlzBmT7XEJi5V04rbtSp7izbAwhkfGfN7zCoJ4ojvaE8xHwAZ3WYHlKSW6AoRNKMdpp7mV6JvKdoPf7eZ1pCKjb72hUIXM4p6Dmh-PDSLRA1bYS_34pEEqkN53ehJ5ZxihGhJ3FFzVkBejt9cXYtvtjJKmHoCITqyowCa0WQJG_D7uJ-cErI5bOqOP0Tlyt4sfZaDhQXIj664VKsryuct4rOCRgCJusj8JxpyAW08v8pXS7agMXP7jfT5TvMSd-gBxs0JtC34Slf3cI4xUUlONnsp_nZvnX6OKFvizlWXWAOU1trHZB4VeuRMXzoYXVzb-a1V43x56BZ30nb3wBsCdF1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتال مرتزقة السعودية الهاربين تتكدس امام عدن وسط رفض مرتزقة الامارات من ادخالهم</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/90066" target="_blank">📅 17:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90065">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a357cb919.mp4?token=XMIiXwhG3AFQwAMyB76kR-RxCGkfWMnWr6wHlyhftviFdPrdgBhziQ_NF63BiPVt_P4uJ--ipaX89OsyDXMCmNGWwie2L39eTJIF-X-6qEdTvOGxxP5VcGpAhVgWjB5B2HlceE7Y6s-IwTDsxceH34NF1cMtwiWimS2jSpBJPJqBLff1SFCd9IuGpQGpXa5kbvRej5PM1WJtHwMRIX8bFdAmdBzE61S4aaPwQ_DjG5ZprtuMTfnv_UaHg0hFebjyG9xNTuqnlyGfwbyVGiUyRnWQZuseyyH9aI3xya97muBVLuDkR7hi6WhglTboLlRQKLerNeB4FS16rgQ0b8aJiKVWHPUbU6tafdYOz91Bf3PLwBBcVBL2ulT2tOVwji2axuJCHrQnRKotliw4MvnZWnqSPWHNtR4pj87blIBNTTxsKi3fPmTgTLojHOWaWOX0JxDq8KnFqznhJw-n-M3_38Krz3rXriThkfbHnC125Kao-3yJUKgiL0hFxTzFcQJbDddQdD7SWYYoAFazxkJTXCpjpEnUydB7_VepL6M6pAUJpQua2nP9yfX7ArTrSAIAiObjrirTblDNtrRszz2zXL2C2Ex-KVusJ1_dNJmqHtYO4CrcZN3i2EGcUL2_wn8Z97Jwcl8Z4IgXoJkzEKBlYqnLx_3fb7vrpyCu_qFxxdI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a357cb919.mp4?token=XMIiXwhG3AFQwAMyB76kR-RxCGkfWMnWr6wHlyhftviFdPrdgBhziQ_NF63BiPVt_P4uJ--ipaX89OsyDXMCmNGWwie2L39eTJIF-X-6qEdTvOGxxP5VcGpAhVgWjB5B2HlceE7Y6s-IwTDsxceH34NF1cMtwiWimS2jSpBJPJqBLff1SFCd9IuGpQGpXa5kbvRej5PM1WJtHwMRIX8bFdAmdBzE61S4aaPwQ_DjG5ZprtuMTfnv_UaHg0hFebjyG9xNTuqnlyGfwbyVGiUyRnWQZuseyyH9aI3xya97muBVLuDkR7hi6WhglTboLlRQKLerNeB4FS16rgQ0b8aJiKVWHPUbU6tafdYOz91Bf3PLwBBcVBL2ulT2tOVwji2axuJCHrQnRKotliw4MvnZWnqSPWHNtR4pj87blIBNTTxsKi3fPmTgTLojHOWaWOX0JxDq8KnFqznhJw-n-M3_38Krz3rXriThkfbHnC125Kao-3yJUKgiL0hFxTzFcQJbDddQdD7SWYYoAFazxkJTXCpjpEnUydB7_VepL6M6pAUJpQua2nP9yfX7ArTrSAIAiObjrirTblDNtrRszz2zXL2C2Ex-KVusJ1_dNJmqHtYO4CrcZN3i2EGcUL2_wn8Z97Jwcl8Z4IgXoJkzEKBlYqnLx_3fb7vrpyCu_qFxxdI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم كميات كبيرة من الاسلحة كانت بحوزة مرتزقة السعودية في حيس</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/90065" target="_blank">📅 17:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90064">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">القوات المسلحة اليمنية تغتنم كميات كبيرة من الاسلحة كانت بحوزة مرتزقة السعودية في حيس</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/90064" target="_blank">📅 17:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90063">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czmZUlAQX9KvR0ILwlXqiet-VcuvNN6f-xGNep_TrJ2fhhS0cUj3Gre0Jdb4vgaLUoh7Q9mZyF2nlfidWLLJH2nOvM108upYxZBeT5xaJYMeVJS3Yh1K9M1kAJ1oCWvunzA22yGSt1b2OuX_Bb9ElTiuspeh3-qJsOO3FiZcIcmAwyQAkpc2HP0vlSE2zUkWDRLz5AKRI6_p1q_jePvVlj3KKcRLpriDDnkXvZkt5n9QKI1x5ooaU2Ob4a4vfBAt4cdLj-mwpXeWv5CbQxkRjI7-xCrj0WbqRsDRFtaut1_wLiGvERxfY6slaLEks_0dlGcbxSxQnrnVKL17HbnS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية من داخل مطار المخا الدولي.</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/naya_foriraq/90063" target="_blank">📅 17:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90062">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c28fafdac.mp4?token=Z-j9GnQAKyqeqs9medsYzb-KvHxMiYH8rA2yIq0nELnsRKw_Q0QcLosBd1y5Vr46QnBpKRUfRSttAJuv_Kwko9Aacto1L46sSm6dWxLTYMqonPk2WHtkUVC2vcsvFvdXROWnzaU-HHWwEdkqemLR2ir9XkbteV-sHlFsgWgOCmQJauuFQG3bk6DyjxtBFNPqhhCv2270WR9lLR8kNwgp0KPsXwHzOrzJFarBb73BefBFzL51KAtvG3O3GwpLrDw6SdaEz0WkSgE-swWU9rivTfbSXa0rMUhgngJsAyThILASQt6Vi5u6FztmHxVU1kGBbfQZ45dDGlymta-1ScVdYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c28fafdac.mp4?token=Z-j9GnQAKyqeqs9medsYzb-KvHxMiYH8rA2yIq0nELnsRKw_Q0QcLosBd1y5Vr46QnBpKRUfRSttAJuv_Kwko9Aacto1L46sSm6dWxLTYMqonPk2WHtkUVC2vcsvFvdXROWnzaU-HHWwEdkqemLR2ir9XkbteV-sHlFsgWgOCmQJauuFQG3bk6DyjxtBFNPqhhCv2270WR9lLR8kNwgp0KPsXwHzOrzJFarBb73BefBFzL51KAtvG3O3GwpLrDw6SdaEz0WkSgE-swWU9rivTfbSXa0rMUhgngJsAyThILASQt6Vi5u6FztmHxVU1kGBbfQZ45dDGlymta-1ScVdYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تستعرض داخل مدينة المخا بعد طرد مرتزقة السعودية منها</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/naya_foriraq/90062" target="_blank">📅 17:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90061">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f352cc8f3.mp4?token=BOZQnn8nEGm6vXlNYB5mMgcz1fh1P1qtVkbw7c-_WsprGCtRFvL_pKnvO4qP74TyByT-B2zWfQEzgwV1d-_Q5QL6V1TQR060Iy_eF4es39_3IEoBwbDHLt6f9lY4yuZPoxFntI31zfT6qj-XD7_1zvw_K6PQVai2BKhVKxED6LkAKLPYcW8f0hPK1LV4SJnBKkEa4TCEEn2AMIXRvw9lZmXrJGfNs7YWb0mOEOJTP6LcuFU9Ga1g0o5adyY3kQ9cd7NwADyFK_09DcmGufHiJI2dxoKTQ1DRq0IZ6YZlq26Q5wM-qhxHmqbYFsTHZM_6yPwxamN-wENgGInmFX5JC6tJgG7y_XEcCaca5q662uVkzYkyZVYZPlusfUm6c3x8am0WwRo1dHU7aV8C4m_RKTq-Vrh7Y8cUkm6hi-ttpcmJ4rnt95BHL7-D41tX6IXK_43-QgKbI_eunfrQ1F4-uXzaXvVHRf3aySnV0wLhP075ScAPHVVUQRnNN6yZ3D99042cHFcgk-pSaiaZxRNIRdTlEzUZ1B9jDayKer2V82zJKU3aRsX50t019UFHr_dFnfi2LlGNktD-cmiQzTTsnp8I_ho0G2LdHSKdL8Ye8lAypz3faGXHBrvHK41mK3ccMR66RQm-sCfbWMxh_VYZgvzoXDbJQ0okK9pmU0uY1Bk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f352cc8f3.mp4?token=BOZQnn8nEGm6vXlNYB5mMgcz1fh1P1qtVkbw7c-_WsprGCtRFvL_pKnvO4qP74TyByT-B2zWfQEzgwV1d-_Q5QL6V1TQR060Iy_eF4es39_3IEoBwbDHLt6f9lY4yuZPoxFntI31zfT6qj-XD7_1zvw_K6PQVai2BKhVKxED6LkAKLPYcW8f0hPK1LV4SJnBKkEa4TCEEn2AMIXRvw9lZmXrJGfNs7YWb0mOEOJTP6LcuFU9Ga1g0o5adyY3kQ9cd7NwADyFK_09DcmGufHiJI2dxoKTQ1DRq0IZ6YZlq26Q5wM-qhxHmqbYFsTHZM_6yPwxamN-wENgGInmFX5JC6tJgG7y_XEcCaca5q662uVkzYkyZVYZPlusfUm6c3x8am0WwRo1dHU7aV8C4m_RKTq-Vrh7Y8cUkm6hi-ttpcmJ4rnt95BHL7-D41tX6IXK_43-QgKbI_eunfrQ1F4-uXzaXvVHRf3aySnV0wLhP075ScAPHVVUQRnNN6yZ3D99042cHFcgk-pSaiaZxRNIRdTlEzUZ1B9jDayKer2V82zJKU3aRsX50t019UFHr_dFnfi2LlGNktD-cmiQzTTsnp8I_ho0G2LdHSKdL8Ye8lAypz3faGXHBrvHK41mK3ccMR66RQm-sCfbWMxh_VYZgvzoXDbJQ0okK9pmU0uY1Bk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرتزقة الامارات تتأهب للنزول لشوارع عدن وطرد مرتزقة السعودية الفارين من المعارك منها</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/90061" target="_blank">📅 17:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90060">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مرتزقة الامارات تتأهب للنزول لشوارع عدن وطرد مرتزقة السعودية الفارين من المعارك منها</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/naya_foriraq/90060" target="_blank">📅 17:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90059">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏رئيس المرتزقة المقيم في الرياض يدعو لتدخل العرب والعالم لحماية الساحل الغربي</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/90059" target="_blank">📅 17:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90058">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‏رئيس المرتزقة المقيم في الرياض يدعو لتدخل العرب والعالم لحماية الساحل الغربي</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/90058" target="_blank">📅 17:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90057">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اعلام مرتزقة السعودية: ‏الحوثيون يسيطرون على جزر زقر وحنيش الكبرى والصغرى الاستراتيجية قبالة الخوخة في البحر الأحمر.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/90057" target="_blank">📅 17:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90056">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcrfPwbymIPf7J8XXJKyi_RVXmPvwXXGKC5ivfrTvCZe8qNUibedMqzhf5TW22NF_xh3gem3C6XWHrVPUxXzjLx50NLqyUQSOyO3yGHy4CQ_tNMzkwkXGUidgF3wewxB0uwKHSCww3WUh6PIVs4OzkwuciqHAAh7xryvOrtGyytjTKguSB5PZfx9PAavR9jAVGk1PAR9SvIXiJ9yTff3RObh4T9enbCGkFYgP5fDo2_SEQl2BWimKN0vUawoj9z3v2To9Exdf2UDJOgMNEfjpWMp7K_dQxQJk4s41lTSCEHjXyj3axeuJRqmsiPbu5AFdh9aze4R-OB6r3QSzVnSCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/90056" target="_blank">📅 16:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90055">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/90055" target="_blank">📅 16:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90054">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مرتزقة الامارات يمنعون مرتزقة السعودية من دخول عدن بعد فرارهم من المخا</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/90054" target="_blank">📅 16:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90053">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060ab4db91.mp4?token=ORQPqWth0HKGC1U_VjW5Li0Fq1CnIHOXLVFSE6IrERSRKcUDyeipWQyDiStrNeG4zTf4jLRjqRfS7lKV4i2WzZWlnIXbkY9k0KjQ6nR4tQVPiht5w5xESzwPuDIj-ZL2_lD99w1bk1eHl2gTM-i8l-HdPDngPdJO3ICNOqLcKJx5H849OG6rig_a0RirTssOOiASpNNal9DVjws9GqtP9jqr-lIPme2TKklOtgX2wZbpYN0dzerFFsBxohniKksAvje5MHtBsuWNhE9aFo-AIIl2l8ma9HuDluGPHbsRxipdii6OVjeTVQNrFql1GoRrnHT2XMBC-wszHuBdxQXnQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060ab4db91.mp4?token=ORQPqWth0HKGC1U_VjW5Li0Fq1CnIHOXLVFSE6IrERSRKcUDyeipWQyDiStrNeG4zTf4jLRjqRfS7lKV4i2WzZWlnIXbkY9k0KjQ6nR4tQVPiht5w5xESzwPuDIj-ZL2_lD99w1bk1eHl2gTM-i8l-HdPDngPdJO3ICNOqLcKJx5H849OG6rig_a0RirTssOOiASpNNal9DVjws9GqtP9jqr-lIPme2TKklOtgX2wZbpYN0dzerFFsBxohniKksAvje5MHtBsuWNhE9aFo-AIIl2l8ma9HuDluGPHbsRxipdii6OVjeTVQNrFql1GoRrnHT2XMBC-wszHuBdxQXnQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرتزقة الامارات يمنعون مرتزقة السعودية من دخول عدن بعد فرارهم من المخا</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/90053" target="_blank">📅 16:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90052">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
مصدر يمني لنايا:
الجبهات الاخرى التي فتحها مرتزقة السعودية لايقاف تقدم القوات المسلحة على الساحل الغربي تشهد اليوم توقف شبه كامل بسبب انهيار معنوياتهم وتواصل تقدم قواتنا المسلحة وسيطرتها على مواقع استراتيجية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/90052" target="_blank">📅 16:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90051">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ باقتحام منطقة ذو باب المطلة على مضيق باب المندب</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/90051" target="_blank">📅 16:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90050">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f93171897c.mp4?token=Be4fNk4gTs9C1tGvoBPGSc6bpi1yo0iiYqA8KQ4cQuWooL3ZdXNQAF8Zoi_FA9hoR4FDnohR4Q3TlqjZ4Ss88J65Ibid_ck-Gy1Cl1KT-W39-fGqxuhLT3KjgFLQEYOprWStJi-czZVGy3EWoC74t7sr09knbyXxPNSBIQ-JhJWPEdpPsGIeWi87tUnUV3xLURbYibAr9guv_frNmznUcNdXogTEnIlBQeu2vFDEVJB6CePyB28D9-f_ocnau0nJR1hdSAYyBxWcCKi_JtnTKL4WyBGZpkTCXLNSE7OWds_EHstJTCXcbU969gKzNzBllsY2NHRXkqiB24f6v0MZUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f93171897c.mp4?token=Be4fNk4gTs9C1tGvoBPGSc6bpi1yo0iiYqA8KQ4cQuWooL3ZdXNQAF8Zoi_FA9hoR4FDnohR4Q3TlqjZ4Ss88J65Ibid_ck-Gy1Cl1KT-W39-fGqxuhLT3KjgFLQEYOprWStJi-czZVGy3EWoC74t7sr09knbyXxPNSBIQ-JhJWPEdpPsGIeWi87tUnUV3xLURbYibAr9guv_frNmznUcNdXogTEnIlBQeu2vFDEVJB6CePyB28D9-f_ocnau0nJR1hdSAYyBxWcCKi_JtnTKL4WyBGZpkTCXLNSE7OWds_EHstJTCXcbU969gKzNzBllsY2NHRXkqiB24f6v0MZUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية في ميناء المخا</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/90050" target="_blank">📅 16:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90049">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4Ek10Xm3JqWVGRWBo09lwjAwtvEHMqfnXwIqdBfrQ1UAl0fulkqmstqtk6Vf2_czM9CyDbg0-_lJZz5w1ve21AQSpfv2epw9JG9aKrJerXnDk5X8nmjIJ6nqva0cj-YQY-NpYWUTP3aB15EVCPsCLsDb23CxHC8Dow_utluInx6q2E9FM-icWz1aIgiJ8iPzvD5K6gGaRZSZ23H9EDuE7lm1qUmHCkvmhKXnvJb5u_Jctliqb3KfDL2mpNZwN2YxlHEflqvxi9L_zfo3JZ7PoF5ocGOlXnbsNI4WD0ziVlV9mQobbKfg9A1fI6q_BQf7ScxV4XoK2eAFK0-d_cZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية في ميناء المخا</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/90049" target="_blank">📅 16:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90048">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902b8b8c56.mp4?token=N0b4mUJjkNn9z7NFwDWG1gpXeqAQk47ER3Ng9tPj9w18y74TU_69msr5Yuc3FikCZxCeQt-LPOi-STcTOG8svkxlP0OQaYW8Ti2fjmLZ6t9bAXpNWXuzl8Vs2nQMi9u7khKV4_Cyzr67jqR-M5onlluRMw9muWu1meZqajIVM4v4uuGWElQuduM0kyXQcqDAw-sKUiCksqwvhQuizAdhN41VenEAwf5pny-j6XKdq8I5YBn8yvz8dlCszaCj8XKgE5xD69j5t_05UtIHxGHUF4TsnAqSqj-ysAqF1zkGVGzuLyrF7dc0-z25GfewJcV51ipJGQdBJDnvEFksefd5OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902b8b8c56.mp4?token=N0b4mUJjkNn9z7NFwDWG1gpXeqAQk47ER3Ng9tPj9w18y74TU_69msr5Yuc3FikCZxCeQt-LPOi-STcTOG8svkxlP0OQaYW8Ti2fjmLZ6t9bAXpNWXuzl8Vs2nQMi9u7khKV4_Cyzr67jqR-M5onlluRMw9muWu1meZqajIVM4v4uuGWElQuduM0kyXQcqDAw-sKUiCksqwvhQuizAdhN41VenEAwf5pny-j6XKdq8I5YBn8yvz8dlCszaCj8XKgE5xD69j5t_05UtIHxGHUF4TsnAqSqj-ysAqF1zkGVGzuLyrF7dc0-z25GfewJcV51ipJGQdBJDnvEFksefd5OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية في ميناء المخا</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/90048" target="_blank">📅 16:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90047">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/90047" target="_blank">📅 16:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90046">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/90046" target="_blank">📅 16:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90045">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDMaQuS_r3F1khY7hVbqh9Wpq-Nh9Rtp59ZsoPIGR_B-QbYPHFcWMBfbSMt-XV5GuIuPhCg1NgoB2hx6W7eKrWhvmz2CyH4jizBQv_IAw2dXfTK_PphgLHa9OIIwFyU82dfPuWvBpDCKM_4bHuKwv3Ap_UhpLmjUJIORBXuVIjwJhInQev2Ggqifrv_0v15KUrMOipKsxxwmyaQ4Nc8SfYprzhrBlcCcLJQGdEuyyhQRswpaxRDOlor3X3H3ISPCeTlVQZkhlOAycTsvkr3A5rm9tehV7tDga4n3IXB8BExWzTYh5YtQmlPbGy3i0obQWHTkePFAOz-Xm0rtLD_PCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇾🇪
بعد سيطرتها الكاملة:
القوات المسلحة اليمنية تعيد فتح الطرقات الرئيسية خط البرح ـ مفرق الحناية ـ العوشقة ـ الوازعية البرح ـ خط الحديدة ـ مفرق المخا ـ مدينة المخا " أمام المواطنين والمسافرين والطرقات الرابطة بين مديريات حيس والخوخة مع باقي مديريات محافظة الحديدة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/90045" target="_blank">📅 16:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90044">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LSTVIFhasYA3vy6O0rl_cq-Vw3dHQ6UMtJTP8nsm-kL9uNIhdka4sh7gTvxcY9SrPTnEKul_KvE2CIb9OgLwn5CzSLxRb4WExGYCJQs_iGnRawswvQficIqlO9eTgPcF8Z2dhxKnO7OyMjE2XZchmWXrJzoaKg3j5DOU91DNRJJ-J_Om1v_ipV4-_L7UCuDUDzzPRltuhaqzFopYkzIRIZeH66xmBH5blhguUV2NzmTN1-htPV3Cj62lH4oLPjX4CyYzJj2Q9IK-FbAUsrFt04bql5Kot1b42Cr2d6K6ktWVwbrq0uR08dUMysy0LZz80j0oElyCpHpBzjPvId_Dkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اذهب إلى فرعون إِنَّهُ طَغَى
المسيرة القرانية تنتصر على محور بعل و ابستن</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/90044" target="_blank">📅 16:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90043">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hESl2_d8MiAL88ClK5j38y21y7mBJ01mXoSFNCFagvn0cYPxbTwlwPyjWrlsIYwAP1ZA-6tPONO9vCuptZFP-VgTUtexC4xFY4DiXnnjLuMIIzCTC-yRzrgMflyJBsi3FN0lRvGTCjs6od67M2B1WcGSdpt8CBnUmy-pJSAOd8LhQkdiqrR_HjpUgz3DP1woSNr0J_gl1wQgQrs6uyJxJyc5J9XBiYiVV71CJNVtlCEkeH6NO23xolmXEm96EM2wcD1-nBikQo5LLnNucdWSHgLzTqjMECgaAPKYrhktrZbPvKuwu-PunlgsCLUfrd1yvgVN-Lp8AU6pfm0eBlWfBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ارتفاع اسعار النفط الى 105$ للبرميل
.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/90043" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90042">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇾🇪
مصدر من الحكومة اليمنية لنايا
لا نفكر بالوقت الحالي للزحف نحو مكة المكرمة .</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/90042" target="_blank">📅 16:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90041">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igeL7Oes7Pgs48pqKBD0MLtlZhVTirfN0c19s67nGRU-PP1wsC-WxpoEHuTTuM_gMZW83gdLAf1zLp8D5JjUeGo5STZoA-0noXsdmDCFEijWie0dmWoETaLV0Cb7nFm9_Zcj5SHE_Oxc1M_fO4URTQ7MCU572HXA5Di4EwbVFS25510TS7Pe7mPk7jPyBSkazGpOExK1rDjCynl37a1WzpYduC2aqCdmy9c0nYAxMrpVB2uZZEjEJ89VkU9ikWNWvBgGUAW-kmHJR7omDehhEGQ_xgVBPVKCa6G2Nafi-0WgjyOnU2IlBQkSNHi0L2bhg2T6z5aZnJ6eI0_YOyYvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسؤولي انصار الله يبدأون بالاستماع إلى احتياجات المواطنين في الخوخة وقضاء حوائجهم بعد هروب مرتزقة السعودية من المدينة</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/90041" target="_blank">📅 16:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90040">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzMtimX8Dc3ep2e5eoOLDkBkHUcGbnB5gk3FUKsWd7jXwk40Br-zzwv1uZ7H2gsbRKJsDparOsOmenkdiVTABm-YD8w5MZBUyFzoFhbyMf3RFcKnk3yJ4iyvVGBZiJ012TldWY36TwtQPq1Jm5Gnfb9KQ2xY_Wo4no-Xu8R4ZPbmsQd4jiHYX7VPDHJvBrJJuL3clJlRDi5PGBPumlAI6N67iAO6sf8tm4tLa9xYFRynb5bbNeRH9yWNswDJDnHZg3WXWh2s7JpgMaDByrIj4XkRDgIRqNTBLtn68_dbyFrKQKy47SW--GdR_0LkW933yaZG5LMCIcSMg0vCjsuNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار النفط تصل إلى 104 دولارات للبرميل بعد تقارير سعودية عن انخفاض في الإنتاج</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/90040" target="_blank">📅 15:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90037">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utiHsrqO3bZLTYB9yHYhEzlKPxmFjsqUQdxpsOIHsXd-yzEmsrIk1-FMleG1aHowTd8yVyjCweA-vEdgNX--nUKG3Yi4H2qfQYE9JQ5K-RFzeUD6XvUbnv7k5DQkGxplC8nAc_3REmh7HcA_6j9bvt8JI-nRMmHsUhAW1gHG9CbxHyRh8AccBW7cYLK2zJDf48mOfOtMOHLerIWsYFNft6zvlS031I3bLuPgdqKb5RcTRsfjuXCNZE_TIDN3iPdy1M-0tfFPMk0yqwvmh3tmiOCjxQGRMR06OsXWEyNkS6XL6YUFwK7sGrSX1I3xon8xTx_LiUOeQjbfArTJxybgjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUIog9EIGdEOpdLOhBc_EfG_e7y6_zljh2KQQy7MYNXX4Tid0ogqg6t_nGzEJNauuHrRUxakCPCp33DinOwOm4MSJgf45Ng2MY7n90X8vCSYn3SwZJP9Bg7GmN52pv_h9bR0bONwQ8y-DqdFJI5VaQPE3_DATkArVI9fI9OGgxXZ0kHpUVR_5Vw3Ybg6FgAoMb_5EYw7nT_22jgiNG1LJ2g1i92oEniiP7TLmZP-DpomvwfraQO3HfxHJS-S3gc-glC814kO5INL-9J6awg-r3aJjEmye61OaTRMFcHh9TfACQXtLRw7-imRgtq6xBNbyE8IVMbwJIoF1wwOFfOsyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UB2NgXp7IPMlPwBdRypPyth41hPXzpyH_pByg07beeN9nbCBsmGwdOHAv23uw5et6MSQCpEerSboO5nZh1otjPf34MzqMXqZ2XTPd_tAcxsWgsuTLBUw8NTJncIMlSEao_LoTnLUxRvDJkwV7oDuxS3jRKd4qcZEDuvgkmYvpb_b9ToCS-xtu4Q8a_IKM50bJIgpCXQWdhKKNAWd8sSy-bvYZjKHrlNFsX2QgtldOCBJIuR7TRNwTY1e6jrUpsMo6WI4GT6lB7lqUKTAKDY9hZnhNUXkJyRvfKQhIHn-fjdhKiEp0VUFbi0ZK8rG4A0eWrHbHSJYsiTv1o5rGDEw9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇾🇪
رجال القوات المسلحة اليمنية من داخل مديرية الخوخة بعد تحريرها وطرد مرتزقة السعودية منها.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/90037" target="_blank">📅 15:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90036">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aed8f88d4.mp4?token=mJVvqX3G26VZmyWePLSqgtQ6mRMIGVe1EW7vJI5ozypsVXw0aH7EafV8xQUUTLEcXQ68ao0SHWzpDqgh0Z6Wk5ZGKVdBE3UmNecxadP-G20cE-hQEXKNvnEdhuazdahqUl4uvz5n2pv3TRg71C0wRuDr29Tbc0WHIxN5BAzWEB0jG9CtHTeKUdMf6MxHarEPMVMjjjmj728bqAduJFelAaKorEChjnB4edfuGl9InRGAFJjVrzKAR38qTvwqPnrZIQVjaznFVa0uIclUG_YgyhKssN8ZK7sQPOsJ-aANGLugs3zuXCY0doOoiHNeqau1pq8o-Jfc3UuAlkqFpJVzEVARW-_hsWuP8eVbRH_JqHxX3yQgjJHEOVj6rsLwdfTkWoplK92XkBpx0PM9FGzIjLnuJmQj9h1a3F1yR827tdPGLNABcvK_RmQnyYWkNwu6G0aHeQMct5n2TBnWWFbCalii3FB1e_OhLjeg2unrTrkwQ1Zz3U1_rz7dIs1kcJyiutjcqs_ZNqlm6dGhrG7wWGfcg4d2NdnSAYT35FfcD53FVr1qBFm25jYbNh6nTUJkwc0yI4676Hpu7N8wLvVtclddWgnqzRJ12FZqfzj9_w0FxkTc7X6aE4k0vxcz4AEGl1H_kDAyQLRh4mt-FRdEx1w1Jq16FVqya-cvNYpEaDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aed8f88d4.mp4?token=mJVvqX3G26VZmyWePLSqgtQ6mRMIGVe1EW7vJI5ozypsVXw0aH7EafV8xQUUTLEcXQ68ao0SHWzpDqgh0Z6Wk5ZGKVdBE3UmNecxadP-G20cE-hQEXKNvnEdhuazdahqUl4uvz5n2pv3TRg71C0wRuDr29Tbc0WHIxN5BAzWEB0jG9CtHTeKUdMf6MxHarEPMVMjjjmj728bqAduJFelAaKorEChjnB4edfuGl9InRGAFJjVrzKAR38qTvwqPnrZIQVjaznFVa0uIclUG_YgyhKssN8ZK7sQPOsJ-aANGLugs3zuXCY0doOoiHNeqau1pq8o-Jfc3UuAlkqFpJVzEVARW-_hsWuP8eVbRH_JqHxX3yQgjJHEOVj6rsLwdfTkWoplK92XkBpx0PM9FGzIjLnuJmQj9h1a3F1yR827tdPGLNABcvK_RmQnyYWkNwu6G0aHeQMct5n2TBnWWFbCalii3FB1e_OhLjeg2unrTrkwQ1Zz3U1_rz7dIs1kcJyiutjcqs_ZNqlm6dGhrG7wWGfcg4d2NdnSAYT35FfcD53FVr1qBFm25jYbNh6nTUJkwc0yI4676Hpu7N8wLvVtclddWgnqzRJ12FZqfzj9_w0FxkTc7X6aE4k0vxcz4AEGl1H_kDAyQLRh4mt-FRdEx1w1Jq16FVqya-cvNYpEaDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
طفل يمني يوجه كلمة الى ابن سعود ونظامه الاجرامي بعد قصف الطيران السعودي لمنزله في مديرية الزاهر.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/90036" target="_blank">📅 15:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90035">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الرئيس اليمني مهدي المشاط:
استتباب الوضع في مديريات الساحل الغربي بعد الانتهاء من ضرب تحشيدات العدو السعودي</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/90035" target="_blank">📅 15:41 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90034">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2I9K0rcSe0tVt2NJvSHibl6wkyaWf2yEVomCYyIrLCnFOnkIHB7-bAuhrExsM8oMnsR4QtbNEHRNnZvaSRRYk5K94NWO4KWAblQ43qZxn3jxASocw9JjaGkW_ZyaqXL3eBVLMzeeqBJDwQgVqPuZeVh-bjCGqMlZ3VvknVJXMRr1t0rAy6jgikLluEHZedkB7PpB6er3xfW25nL8UOnrvGeKP9pCOH6-u_ZvLtzEJeHxYjHN-Ekf-9TDcanG_b3ubFsyBM9jkXCgNc5GEUYayuXuwKfriYcV8TSEicgOuTECBcL7iOErkwTi-YTWW1z0VAh64bKgw76gnatVknbxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السعودية تخبر منظمة أوبك أن الانتاج انخفض إلى أدنى مستوى منذ عام 1990</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/90034" target="_blank">📅 15:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90033">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">القوات المسلحة اليمنية من امام مديرية شرطة الخوخة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/90033" target="_blank">📅 15:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90032">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/90032" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90031">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/90031" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90030">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">انصار الله يسيطرون على جزيرة زقر الواقعة في الممر الملاحي الدولي جنوبي البحر الأحمر</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/90030" target="_blank">📅 15:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90029">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏
سي ان ان الأمريكية :
بدأ المتمردون الحوثيون في اليمن، ⁦ ⁩ أقوى حلفاء إيران الإقليميين، هجوماً قد يُمكّنهم من السيطرة على جزيرة بريم، وبالتالي منع السفن من المرور عبر هذا الممر الضيق من البحر الأحمر.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/90029" target="_blank">📅 15:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90028">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انباء اولية عن تحرير القوات المسلحة اليمنية لجزيرة ميون في قلب مضيق باب المندب</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/90028" target="_blank">📅 15:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90027">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ باقتحام منطقة ذو باب المطلة على مضيق باب المندب</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/90027" target="_blank">📅 14:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90026">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حادثة على بعد 98 ميل بحري جنوب غرب المكلا اليمنية</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/90026" target="_blank">📅 14:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90025">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAskaqOrQxFQ4Q7QuZxswZmORUK-W_vaz0GlxHsvPEIF93WYLYi-aEZi6zeoWS_H8TCQYMWrKshLrMddzvKDfmY0UVt3cI070HH5zh2tWe3nYuS_3GUAEVmSnNu3A3sjH92rMBXfodGpxjRyX9D7k1nr543rKyYYmzNfa5c7kkwEc6MtKT_Sq4Aq0luNPn22Wkb1PF1RyPu2zqFPP6KW2rhH9fQ_TQCJExqxmGV5qVyUNunMXwtgqsNxkR2oIYRACGThftDUqpOwfWHxpvDQFyA-WR7u9bArdPEyLf9ShveCxqvhbG3U4T6ztZQzDJPQ2Vkh47Fo1Un3urmQ0xOIeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثة على بعد 98 ميل بحري جنوب غرب المكلا اليمنية</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/90025" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90024">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">العراق يعلن عن مناقصة لشراء ناقلتين نفطيتين عملاقتين لمدة 180 يوم لمرورهما بمضيق هرمز</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/90024" target="_blank">📅 14:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90023">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سقوط عدد كبير من القتلى إثر اندلاع حريق في سفينة أجنبية في مرفأ صيني</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/90023" target="_blank">📅 14:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90022">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAP9jl9fckZhbDzoAudUgTndlOBR3VvujlGCguurG1kLhrKXTJFEX9TKwqpb52C2MuS6x-m2QId2Xb24I6I4N4Mj9YHLx7K9XPak8dyPSk42K047nIsoT_Yd1wBZlf36vmZlQnd_6DfZ8I6y4xll3u8Ylt5Tw_UvYbZhoiZgDVDiU08H0BwP8fJ-yrfLQZvjAkcOgHbgM8JVx2pGSVtiKcMLdkzfeJiRk-2tcv9GjapZf-8IdDvjOjJ4DAUdYJ1oDNLcfOMZmEHneY2ElJJ1x5AmndiLyJx6ofATQnUf75mi7I-n38E4WRTgJlp4aHQSFNBX1oBMvV_9YIottlMQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد مقتدى الصدر مغردا</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90022" target="_blank">📅 13:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90021">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترفيهي
الاعلام السعودي: ‏قوات المرتزقة تنفذ عملية إعادة تموضع في الساحل الغربي.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90021" target="_blank">📅 13:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90020">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مرتزقة الامارات تمنع مرتزقة السعودية المنسحبين من الساحل الغربي من العبور باتجاه عدن وتشتبك معهم بمختلف الأسلحة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90020" target="_blank">📅 13:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90019">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مرتزقة الامارات تمنع مرتزقة السعودية المنسحبين من الساحل الغربي من العبور باتجاه عدن وتشتبك معهم بمختلف الأسلحة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90019" target="_blank">📅 13:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90018">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWwZU__QWY_-rR4UIQFrD3GbtiApdXeZKsKUmtavStjyqiF3aRcw7I1nPY_KjvfcgObXmOv6U_83SwdDgHhr_rw1_iRmBpi6FDjQy-EwHDBGMVnicUEedUSsciHb2gpZ8gO0Y008A-S8MCMJdC8dTXY8AVqxU8XJeeD908bXhgz05FGzVlEtjKWFfnZBAAI56loaluDItmpal6uvlS7d7S5OJ9jDuHMF3xo3bUzoZ1sAu0Btw0MOEXiieZ5Ls2bIrfAcXzVoo56VjZ_SGj0aUpIusbyIqp_6YChj1YiuKq9gXF15sFHvJE5f0J2zyOTSPkmL_I2NmI8BS8BZVfcI9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تتجاوز 102 دولار للبرميل.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/90018" target="_blank">📅 13:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90017">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90017" target="_blank">📅 13:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90016">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90016" target="_blank">📅 13:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90015">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📰
رويترز تقول ان باكستان سترد على الحوثيين وفق اتفاقية مكة من يبيض الديج.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/90015" target="_blank">📅 12:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90014">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سقوط عدد كبير من القتلى إثر اندلاع حريق في سفينة أجنبية في مرفأ صيني</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/90014" target="_blank">📅 12:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90013">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8265c7835.mp4?token=od5QJ2UoYpIhYxxbZ9JtcGDmqwufA498EnuX1stBKQP9X7qslIOG06SpIzKWWqbqlPR-WytiV9hUiCiqxMc8X1WrKb1n70lEwQkEI3pZtvZbtBxhax-7OLGIP-lhYK-DJosvt9iQTkSLFjwA4RJC0FDGWHQwHTcn91yorrMLSeDZS0-2ZqP3mvWUjRy1RHlWlQmJK2GeJ4gOGEkj4jM7fNv9B4giBIRVuNprF8D0PeoUaBKTsyJqK2IwL399ZBAIbO6Atvb-LodXRUb_lacYRDPbh-OTWE8_8dM2iJhbwevZMj5JLki8r92qTqbdOAO2BY9q2Wa_HtXbuFY_evUZUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8265c7835.mp4?token=od5QJ2UoYpIhYxxbZ9JtcGDmqwufA498EnuX1stBKQP9X7qslIOG06SpIzKWWqbqlPR-WytiV9hUiCiqxMc8X1WrKb1n70lEwQkEI3pZtvZbtBxhax-7OLGIP-lhYK-DJosvt9iQTkSLFjwA4RJC0FDGWHQwHTcn91yorrMLSeDZS0-2ZqP3mvWUjRy1RHlWlQmJK2GeJ4gOGEkj4jM7fNv9B4giBIRVuNprF8D0PeoUaBKTsyJqK2IwL399ZBAIbO6Atvb-LodXRUb_lacYRDPbh-OTWE8_8dM2iJhbwevZMj5JLki8r92qTqbdOAO2BY9q2Wa_HtXbuFY_evUZUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصادر لنايا:
رتل امريكي شوهد في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90013" target="_blank">📅 12:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90012">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIffS4Np6hECGR1KJYsfMhlTNJGZh3ir2mByGS-8cz6D4rS7I5udfj90HwFnu32p2piVjZo2FtZZiieEXqTBGbzSEIQPrPlzq1t-MGAaw8UErfGWOmtSAbGa7uC8trxvO62gUbq8MBdnB0Q2yKa0Dj07Ak6pZV98uPoqM_HYeSkXpn6Y0iC7rDGPrgnuY3cbvR7GmXNbn5m_L8djE4yjD36-j4HOu1l0549tfHKYFtlbQkB7yqtRMftmosQVAqkgCuH3LKT4EEF3wFTspuAE2ryiql9dvKlGrtGFzlfdzFkv_K1DRj6m_t2C9rAO4FhgMpiFlouO-FzWGk1fx6K1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية والاعلام اليمني داخل مدينة الخوخة بعد السيطرة عليها</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/90012" target="_blank">📅 12:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90011">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoRomSBNRsOB3RAQQ7c4rZUDqsvrSoncaKWvnkdL44uAgawd45DocerhcHs5P-d3wJWEADGR6gkufq6e-0ji6vIjsrxtUBEPfWkN4uS5fPt28X-RT75AfNe-iGAQgXNEKQiEoeQqvgkAhoOXLDJ7XK42guKZVTePPRrENC-Kq7xBwOzjE0Mf6a2YMgExqrAIQwotdcRLTw_HeFCH5LoAAWLPCIszr7_IQZSVVLGkkqaUB03C_6NVrD5_v4EUS2LqfEpFZy3l0wnit3vagJV46mbHoZkDLfi5ArP6YfwVhzux-1E8G1wBAeZ9QErJCItvwI3TRaZjYSedmYe0IopvOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اسعار النفط تتجاوز 102 دولار للبرميل.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/90011" target="_blank">📅 12:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90010">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
الناطق باسم القائد العام للقوات المسلحة العراقية:
منظومات الدفاع الجوي ستصل قريباً من كوريا الجنوبية وتركيا والولايات المتحدة، لا توجد مهلة محددة مع الفصائل لتنظيم السلاح.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90010" target="_blank">📅 12:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90009">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇾🇪
الجيش اليمني:
تمكنت القوات المسلحة اليمنية بعون الله من إسقاط طائرة استطلاع مسلح نوع كاريال تابعة للعدو السعودي وذلك أثناء قيامها بأعمال عدائية في أجواء محافظة حجة، وتم إسقاطها بسلاح مناسب.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/90009" target="_blank">📅 11:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90008">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇾🇪
🇾🇪
قراءة سريعة / ماذا حدث  البارحة في اليمن ؟
- حققت قوات أنصار الله في اليمن مكاسب كبيرة على الأرض، حيث سيطرت على مدينة المخا الساحلية، بما في ذلك مينائها الرئيسي ومطارها.
‏- تتمتع المدينة بأهمية استراتيجية، إذ تقع على ساحل البحر الأحمر اليمني بالقرب من ممر باب المندب، أحد أكثر الممرات البحرية حساسية في العالم.
‏كان ميناء ومطار المخا بمثابة قاعدة عسكرية إماراتية قبل أن تستخدمهما لاحقاً القوات الحكومية اليمنية المدعومة من السعودية بعد انسحاب الإمارات من اليمن .</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/90008" target="_blank">📅 11:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90006">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi9dfVheuXZKPFgZlDfJQIRn5UBERysfou-YUAUuvMlK6qz7hrMW-f_rukSw6xF55gkJxNqMQwlNc24VCNoOwzRo6rCq2cmbEw5wOtYXaH6ED5HJMqkhYuI6qeBYG8LnKSKh4qw34xp5GnjsHIjLB6gxl4SVPQzRe0vnZNkrsgoE5KzcvQ9ERs2KDLpzviG6l0n6OhQyLjKm4HMO5wY-_4njuqCVh0VNiEuPK6C7eEB1ijBS7xUyTpKhUdQdUgXfD-V_DjkTH6mKvyoNhi9Mgdam7d17PdYvpuWWYx3hq4Z3GIp3wgWVugHJNBCfqw5tc9B9SA1UjKTJ_zK1yV9XtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43657329e5.mp4?token=oEkRCmp2BmULQuhHUz5gNf9XGg9pDm6O510sF4kzbxJ9o2lP_wtokpX_f3riXexHDcfdA922rZBYuHc6iVN7KkGRxMH5YVSTu_miKncnnsh5-sm3RqB2nUV4iieq1f-o6ushrz7kTSJDmqSX2L7v4_d-pXSO5w1vSttbfQDr6hhoY7JlbxUYjA9-QnZTaHhDVkdrBnXtKETrj66QZRPqFqzNy2ne-ZeBHrjp1p0SY6fzCLOETzlEWpnewmItMB2yqROx-M1BP89sjoqZJfaJ2Y5sRxVP85SXWIUQnkA4KncX46hccAJQ44Z99bmuBPkfE3j7JUvS86n15q8VbcmxYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43657329e5.mp4?token=oEkRCmp2BmULQuhHUz5gNf9XGg9pDm6O510sF4kzbxJ9o2lP_wtokpX_f3riXexHDcfdA922rZBYuHc6iVN7KkGRxMH5YVSTu_miKncnnsh5-sm3RqB2nUV4iieq1f-o6ushrz7kTSJDmqSX2L7v4_d-pXSO5w1vSttbfQDr6hhoY7JlbxUYjA9-QnZTaHhDVkdrBnXtKETrj66QZRPqFqzNy2ne-ZeBHrjp1p0SY6fzCLOETzlEWpnewmItMB2yqROx-M1BP89sjoqZJfaJ2Y5sRxVP85SXWIUQnkA4KncX46hccAJQ44Z99bmuBPkfE3j7JUvS86n15q8VbcmxYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
صور الأقمار الصناعية من 9 سبتمبر تظهر أضرارًا كبيرة في مصفاة جازان التابعة لأرامكو السعودية، مع تدمير ما لا يقل عن أربعة مستودعات تخزين نفط على الأقل في الضربات الحوثية الأخيرة.
‏كما يظهر أثر حرق/سحابة دخان غير عادية في منطقة معالجة النفط داخل المنشأة.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90006" target="_blank">📅 10:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90005">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇸🇦
🇾🇪
عدوان سعودي على محافظة الحديدة اليمنية.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90005" target="_blank">📅 08:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90004">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stUfEhNTZrNIMPZkAsSqCIqd3uF9huGxQ_Jg9-kFkIiqDFsQICwxmW3tSMonUgHUxDBd8A0zTsSDtyjJLyC5UKxBKDMJGhTqNVwMNekSqTCDrDtAThTXPfbQ4jl0aPo2zLDgKH-MWpoqPsoDr3F3UT-KPvYToHC7bm0LpPKpP5Rl1kNITwQpxdpxe3WUp2jBVNWAu_NKnuaGAH2Yr6nFY_reaZyJeCbHjE8PWlLqy1S4GzdWx0_BnBZw-qPRc6FwbO1Y4IffJYhKSvMlNkdu4vbs6G8j6EtXimpd6_77SiT11Ho4nK76vykU3fsBOME_QLHkc9vi26Cwy5B3VvuIWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الملك عبدالعزيز في جدة بالسعودية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/90004" target="_blank">📅 07:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90003">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOYuciyMiN_6P_FUEBhJvPZ0vKdoUVPy75gpKG3nEHDW_bWc5WDrYSOL3nKZM7TWM-0sXOmzKcQei3RRJEDh3IBZDg012OV1yra3-el88UJECKJ_XVvVEindPO7VUiUj0D9_mkFMnGS87dyq4z8fLfrPOH96bZ-ccXSs1PItx1nlla0GssrcwOKoev6VPcrtBkMW_RSD9hzLWos-5YY3Pc70hs8_Z5RtMBRnY1b1y1iszWQnnp36R7n5Eh0yJiG9z0BpNi7VBhhZD-f9zCbobl5SMd5ncGaZkE3zhQzxobnFI4AGqOIpjfEHNsV0Hup63_VTvscvvZ40mQ4IQwIzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربات صاروخية تدك خميس مشيط</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/90003" target="_blank">📅 07:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90002">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/90002" target="_blank">📅 07:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90001">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات عنيفة تهز السعودية</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/90001" target="_blank">📅 07:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-90000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/990b969f2e.mp4?token=cCInFw6TyxGueCafRFSULT1_fB5SQLFoUW0tZMNQihG_v02SHHRpICmlUPFSpXsyA8m0YYimKentHbIWYz3sTTZHvWIv2mn88bOoSsQ81Kb83RladxZpJGJ3W2ISAiFiJXMjH0czdySiYQ0XsNFdS7qoEyFlQnWTog0GMAYJjfB6P1RvJfNpf2-eLcF-Xatno_0gQwluh8wwDXFQfvloqFXeYgpV_T6qUs4G7f_1MZdrMnrgzcYWqfgy-C4PItp_OLuh31kfb2siUQZaj1Lm0EMvsv5G_uuqo65Fw-5Y_nhZK5eA2v3uSd-4PU-m1VKtG76wEY_e-dXUYJ_mhDoLM2XHPkBtksJ2nsHzC-RoWth3AMuuaSjnDP9oc-A-m8wxDS0AkqOkEqnuR1zDojZ7q7pvZZKCf0blH3TgEf8VwqxyGHKA48D6Y6FMAt2ZXYtXycpvS2C_FZSN_fsCjvIRTtAjf-86fEDieaNuaVv2CjM0BPXOmZet_GJY_t7u5yq6wFkKkI8vZOfIqwdnsZzvbc6QmEGQCdYxFtra2wsSPUsEvknpndywgC65vtNx1XhdCXBTw2DZJpFQ6YLJV4k2_xC7t8iy_3He5Wtpsvc8760aPNL1nTFuAd3fQ57mh0IMDkcrwrrSGTLtMQ4iXiBZ9yFAIT0Wi9jwwEuqNOaXaC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/990b969f2e.mp4?token=cCInFw6TyxGueCafRFSULT1_fB5SQLFoUW0tZMNQihG_v02SHHRpICmlUPFSpXsyA8m0YYimKentHbIWYz3sTTZHvWIv2mn88bOoSsQ81Kb83RladxZpJGJ3W2ISAiFiJXMjH0czdySiYQ0XsNFdS7qoEyFlQnWTog0GMAYJjfB6P1RvJfNpf2-eLcF-Xatno_0gQwluh8wwDXFQfvloqFXeYgpV_T6qUs4G7f_1MZdrMnrgzcYWqfgy-C4PItp_OLuh31kfb2siUQZaj1Lm0EMvsv5G_uuqo65Fw-5Y_nhZK5eA2v3uSd-4PU-m1VKtG76wEY_e-dXUYJ_mhDoLM2XHPkBtksJ2nsHzC-RoWth3AMuuaSjnDP9oc-A-m8wxDS0AkqOkEqnuR1zDojZ7q7pvZZKCf0blH3TgEf8VwqxyGHKA48D6Y6FMAt2ZXYtXycpvS2C_FZSN_fsCjvIRTtAjf-86fEDieaNuaVv2CjM0BPXOmZet_GJY_t7u5yq6wFkKkI8vZOfIqwdnsZzvbc6QmEGQCdYxFtra2wsSPUsEvknpndywgC65vtNx1XhdCXBTw2DZJpFQ6YLJV4k2_xC7t8iy_3He5Wtpsvc8760aPNL1nTFuAd3fQ57mh0IMDkcrwrrSGTLtMQ4iXiBZ9yFAIT0Wi9jwwEuqNOaXaC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أرتال القوات اليمنية تبدء بالإنتشار في مدينة المخا.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/90000" target="_blank">📅 07:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89999">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9f44cc781.mp4?token=QMpfDvi5PodHMllUSPYhGRANZuXiFrF4RdfwVE5GXB8BDnSBmedIs4xsvftyCvpQwYda6xSYGKMUGjWlfVwKY2QH7OyDgRtjTA4OIQ900pBEa80fC8ln77HFey72gT1xH2qHmnBiXT5xQ1leNG9FZJcm4esry-Khhql2TNGfmDqobL2BenQ3cXKpurkXRFRYfGh7Qod0Y6YwoAPvPCzNIT2_1F4vvL0Q5oMCV25XkT3HzR629Z18oDzG7SY61LJ0f2spgCkqFfzcNkJUw94GESNtI-X7Kpa8MIIEKyerwJC1mp5Qvsp0pr0w0b7WMsCEIp0J96CaqqdXPBAD-IVWYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9f44cc781.mp4?token=QMpfDvi5PodHMllUSPYhGRANZuXiFrF4RdfwVE5GXB8BDnSBmedIs4xsvftyCvpQwYda6xSYGKMUGjWlfVwKY2QH7OyDgRtjTA4OIQ900pBEa80fC8ln77HFey72gT1xH2qHmnBiXT5xQ1leNG9FZJcm4esry-Khhql2TNGfmDqobL2BenQ3cXKpurkXRFRYfGh7Qod0Y6YwoAPvPCzNIT2_1F4vvL0Q5oMCV25XkT3HzR629Z18oDzG7SY61LJ0f2spgCkqFfzcNkJUw94GESNtI-X7Kpa8MIIEKyerwJC1mp5Qvsp0pr0w0b7WMsCEIp0J96CaqqdXPBAD-IVWYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر
🇾🇪
القوات اليمنية تصل إلى مطار مدينة المخا.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/89999" target="_blank">📅 06:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OI_PESWuv8GRNSwZCu1xngfPQ6PzZN54Em1G1yipYJK3Z9IAZHPFXmtSjiTvHIPlaPgcKNe6eEtJZiI5E8_aEiD_6xa2XczdpODzxteLO-AQkWH3VctaQrPABEgo-Hu6PPmKxlNBADbqN4ie6uxVczdMHSfOf-ESXbG1J0qApnCkRa8w6zPxNyLrZyTiZq0fTp3f56YsoAqz5LXF88vGHiliiorvdsMpsLFH768XleQlMy7jLb67HOeNvBPOBXok43ojYEI20T0togOn7Rrj07ZLJ0_jGq4K7Z1j00p7Py-jB0D87r0X_wZr_vEjA7SAoxA50YDxFMUKYmhQPf5kYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
السلام على زيد بن علي
اليوم يومك يـ الشريط الساحلي
من با يرد السيل لا روس التباب
من بعد يختل و المخاء والهاملي
من كل باب الزحف قادم يا ذُباب</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/89998" target="_blank">📅 05:43 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇾🇪
🇸🇦
هروب مرتزقة السعودية من مدينة المخا عقب سيطرة القوات اليمنية على يختل والتقدم نحوها.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/89997" target="_blank">📅 05:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
بعد أن زعم الإنتصار على إيران.. ‏ترامب: سينخفض ​​سعر النفط بمجرد أن ننتصر في الحرب مع إيران.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/89996" target="_blank">📅 05:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89995">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcba18ca4e.mp4?token=tXu0BtxOki5weztiKxwG1WhS0GoQICsEKVGys5fv9tyjKOQO8a8ItN3QutpGXgr2CcxuyAaEfrL9Ulyui07qsVUGV4YyMqnLQ_KaUx5q4xlo1zC9xFAxp6n9xAaF-pPlZnYzo6I-Ou5hPzYy5w_2k2b36Ytowov56CRH7NEURV7VwFz-LFPH6-jhApybb6jJJ8T0EA3PJDUxhoVq-aW82lWWZeiqIb_eI2Wcwu6dcShxoyGMw9pYR12nqi1EJUDHPkBLWs2pYanaM0nI-Be1gcYAQjiWvzKjQm53j_ra2Qka3iTXHkDHstQhw-ODvzxcPh8HDGxfo1W4abohbAZNAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcba18ca4e.mp4?token=tXu0BtxOki5weztiKxwG1WhS0GoQICsEKVGys5fv9tyjKOQO8a8ItN3QutpGXgr2CcxuyAaEfrL9Ulyui07qsVUGV4YyMqnLQ_KaUx5q4xlo1zC9xFAxp6n9xAaF-pPlZnYzo6I-Ou5hPzYy5w_2k2b36Ytowov56CRH7NEURV7VwFz-LFPH6-jhApybb6jJJ8T0EA3PJDUxhoVq-aW82lWWZeiqIb_eI2Wcwu6dcShxoyGMw9pYR12nqi1EJUDHPkBLWs2pYanaM0nI-Be1gcYAQjiWvzKjQm53j_ra2Qka3iTXHkDHstQhw-ODvzxcPh8HDGxfo1W4abohbAZNAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب
😭
: لقد انتصرنا في حربنا على إيران.  ‏يجب تسمية مضيق هرمز بمضيق ترامب.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/89995" target="_blank">📅 05:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89994">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGNVhMwPn_Kj-dB7xrK3QKFx40ZhmZLIgSaBM_t2jxMUY2TIKTHYkLUBTDV-wR6eA68Ol6ktadWuVnKtSzHAjgptxVn6jRyU0VhbRlzC_9stVNFf6__WybddtLsmLwr6_h4X_A7l1NcYp6b5sDvjGrg3SMNEg8nFdiKnz2iKjHBlO6XkY54MFueo5gZagPrUqTpWqf1knX5VYUrwrQ6lSdgV8g0fvlrmgJOUzZ3yOhx8fvGmX4xHI8D67vdUVG9foWfNK3QqN9Hf3VnMjHdeW8la8Ib8v76LfTgj6HJfDmzFQ2OShCuj1KnGboKNHOSQsp7s-gDz6qIkORa1GhV9BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب
😭
: لقد انتصرنا في حربنا على إيران.  ‏يجب تسمية مضيق هرمز بمضيق ترامب.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/89994" target="_blank">📅 05:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89993">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9641772f6.mp4?token=YsZjQgXca3c8ER6rsvq8MNbVgzO9D9bmTsDzfwXM87E1OYjhR8Qw2chBsCI0cf6cqe8P7L8ocw10tgvxLOmPQPPqPVXtEPwuoS44Qq-FR2G_QEJNH4LVovF06jN62WRMTWG-SvJIbQMThkwyRZnE_igUoAd4D_JC74aZjsoxKQzMxdGuEdeRn3jcCYOZjkOe99OvuIw4562Tq0Dxxt5F9ZO_FC3qUlREcqIVSMPN1MarEQtKs1KWb-_cKXF2eb2_8hT6ybVvK20Bpp0ICJVLueeOZlnF7FdpOJpIgkaCRc_qfMzO8AIXOBFT53_7Qys16B9M97gssw2OwIr6vpEeyIFUoWauvCUWc1qba4mVyBJLGBjxqYc1Hq5h7L27jPCjVUqTHo4UZ7YFfjf-GVnD0448QB06aXRQMYd2gO-vqA1cH02SrcZI6d9DpYvnkYDq6WNczuMGUO-gPES5yAi4aTHW3z4AHq9JwXRxxiPqFlTaLFZUMLbqrzJYnaghsziw0LB_H8ONF-u9IIRq0TlrxMZ3hOg3caVsD8SFurHMhaqh8ZgRb9gjFNhX1E-ozSxmMoEgrvmWD7uVNB7HMlkgmuT8TcoK-oVJ80JsPP73C0xZGKk8kC3cSHzbuglAlG4lWxnstMwyzd6O5QzviJ63BgQx_swOLEYtzXkjzttzrsI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9641772f6.mp4?token=YsZjQgXca3c8ER6rsvq8MNbVgzO9D9bmTsDzfwXM87E1OYjhR8Qw2chBsCI0cf6cqe8P7L8ocw10tgvxLOmPQPPqPVXtEPwuoS44Qq-FR2G_QEJNH4LVovF06jN62WRMTWG-SvJIbQMThkwyRZnE_igUoAd4D_JC74aZjsoxKQzMxdGuEdeRn3jcCYOZjkOe99OvuIw4562Tq0Dxxt5F9ZO_FC3qUlREcqIVSMPN1MarEQtKs1KWb-_cKXF2eb2_8hT6ybVvK20Bpp0ICJVLueeOZlnF7FdpOJpIgkaCRc_qfMzO8AIXOBFT53_7Qys16B9M97gssw2OwIr6vpEeyIFUoWauvCUWc1qba4mVyBJLGBjxqYc1Hq5h7L27jPCjVUqTHo4UZ7YFfjf-GVnD0448QB06aXRQMYd2gO-vqA1cH02SrcZI6d9DpYvnkYDq6WNczuMGUO-gPES5yAi4aTHW3z4AHq9JwXRxxiPqFlTaLFZUMLbqrzJYnaghsziw0LB_H8ONF-u9IIRq0TlrxMZ3hOg3caVsD8SFurHMhaqh8ZgRb9gjFNhX1E-ozSxmMoEgrvmWD7uVNB7HMlkgmuT8TcoK-oVJ80JsPP73C0xZGKk8kC3cSHzbuglAlG4lWxnstMwyzd6O5QzviJ63BgQx_swOLEYtzXkjzttzrsI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب:  أتوقع أن تنتهي حرب إيران عقب انتخابات التجديد النصفي مباشرة.  ‏أطلب منكم أن تسمحوا لنا بإكمال المهمة التي بدأناها خلال أعظم عامين في تاريخ الرئاسة. لقد كان هذان العامان الأكثر نجاحًا في تاريخ الرئاسة.‏  خسراتنا للانتخابات النصفية يعني خسارة الكثير…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89993" target="_blank">📅 05:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89990">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0685f235c.mp4?token=VAGV1zcCUUmAPoAIs1LwSJMJpgsoHArryXL7k1t96VvQ3wE_Lpnb06ytNfqR7cFK88a2Ilzx62vMi_DIZRvxJr9hbFjJ8UNGJzdyqVYNwkOIg4Ghtgr9zyqR3L6LCubGR2tuNsjwE_LgYZsIqJwFU2hFpLxUkFglQFbodQHGJ4O4nWL4nx8qOcxYc9LsSY-EZ48wpd-5FUB2VshtoClYg75zefhDFzmnsE6t16MyLZtjTxoINDKTRtTjvwtnZ50SCnHvucaTO3JqoP7FBO5WjnObeUHbBYr-zxcuFdIxA8u2YogE259lQ8d97tiHMgY9CuvUZZ-t-ufxs-biEfZ_uHqBCgVCBsLgGLoUSgsCI4ypnFR9PHokYIiHel74O52iM3bUp7elf103bE4OsdRgqiK0C3cYOpQmQh4aAoHTx-g5SZiKUKsv_04C6hplxdBL3B_8hxrxKZZVMDRQWeOODRNL66WpgAemuWw8jsdPBmU39smEeiOv886UrUMS2oCLHpdHoyYKqzfCFOIA5H6QidT1YOavYwzUoFd_tRm2AeOkRvKAcreXN5nllJ03V0Lmv4Cw1TZS6Ju_QaJOui85Y2QzJ4fN7Jz4LDz2bVuHxera_CKKlCAlSgoQNgO9Rc9KVJEOKenmi7zSPVGuBb1F7TXGTzsgWZzhzBkqrkzZb34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0685f235c.mp4?token=VAGV1zcCUUmAPoAIs1LwSJMJpgsoHArryXL7k1t96VvQ3wE_Lpnb06ytNfqR7cFK88a2Ilzx62vMi_DIZRvxJr9hbFjJ8UNGJzdyqVYNwkOIg4Ghtgr9zyqR3L6LCubGR2tuNsjwE_LgYZsIqJwFU2hFpLxUkFglQFbodQHGJ4O4nWL4nx8qOcxYc9LsSY-EZ48wpd-5FUB2VshtoClYg75zefhDFzmnsE6t16MyLZtjTxoINDKTRtTjvwtnZ50SCnHvucaTO3JqoP7FBO5WjnObeUHbBYr-zxcuFdIxA8u2YogE259lQ8d97tiHMgY9CuvUZZ-t-ufxs-biEfZ_uHqBCgVCBsLgGLoUSgsCI4ypnFR9PHokYIiHel74O52iM3bUp7elf103bE4OsdRgqiK0C3cYOpQmQh4aAoHTx-g5SZiKUKsv_04C6hplxdBL3B_8hxrxKZZVMDRQWeOODRNL66WpgAemuWw8jsdPBmU39smEeiOv886UrUMS2oCLHpdHoyYKqzfCFOIA5H6QidT1YOavYwzUoFd_tRm2AeOkRvKAcreXN5nllJ03V0Lmv4Cw1TZS6Ju_QaJOui85Y2QzJ4fN7Jz4LDz2bVuHxera_CKKlCAlSgoQNgO9Rc9KVJEOKenmi7zSPVGuBb1F7TXGTzsgWZzhzBkqrkzZb34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد من التحرير والسيطرة الكاملة لمديريتي حيس والخوخة ومثلث المخا من قبل القوات اليمنية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/89990" target="_blank">📅 05:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89989">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
🇺🇸
رويترز:
تعرضت عدة طائرات عسكرية أمريكية لأضرار خلال هجمات ليلية استهدفت قاعدة موفق السلطي الجوية في الأردن.
إصابة طائرة أي 10 ثاندربولت وتضرر 8 مقاتلات من طراز إف 15.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/89989" target="_blank">📅 05:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89988">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65019f0f60.mp4?token=buBbUF0k90ZlGi5_NjnCwfuedEqTSTQSguhen7hdkZY4Ob9aORGr3BgqhG6GTI_HjkxVlHCMp72QGIMAFK3ZSkQZoSz-J01amoLeDF7SSPB9u8ZObHp6afYS5EVgvKl60azxZu6EqrxacZe9151wynlflolRR00_7epi4SKQQv6QkCfuC86YQ6uxOfzFH1MbPriHQ0Elq_M3ywHRf02t8U2dOewxRmkJxsgrcxr-dweIrpS-qBJpWd3b6tJawI5X9BOYXWOENAjfVao0LDWCFcjhG9NhcaMy9Bhz3Y7fLerPmrkbwUplwNs3H1NXIiQQQlIstw0wCxQWjs1eP6gvfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65019f0f60.mp4?token=buBbUF0k90ZlGi5_NjnCwfuedEqTSTQSguhen7hdkZY4Ob9aORGr3BgqhG6GTI_HjkxVlHCMp72QGIMAFK3ZSkQZoSz-J01amoLeDF7SSPB9u8ZObHp6afYS5EVgvKl60azxZu6EqrxacZe9151wynlflolRR00_7epi4SKQQv6QkCfuC86YQ6uxOfzFH1MbPriHQ0Elq_M3ywHRf02t8U2dOewxRmkJxsgrcxr-dweIrpS-qBJpWd3b6tJawI5X9BOYXWOENAjfVao0LDWCFcjhG9NhcaMy9Bhz3Y7fLerPmrkbwUplwNs3H1NXIiQQQlIstw0wCxQWjs1eP6gvfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات اليمنة تتحرك نحو المخا بعد السيطرة على يختل.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/89988" target="_blank">📅 05:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89987">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
ترامب:
أتوقع أن تنتهي حرب إيران عقب انتخابات التجديد النصفي مباشرة.
‏أطلب منكم أن تسمحوا لنا بإكمال المهمة التي بدأناها خلال أعظم عامين في تاريخ الرئاسة. لقد كان هذان العامان الأكثر نجاحًا في تاريخ الرئاسة.‏
خسراتنا للانتخابات النصفية يعني خسارة الكثير من الإنجازات التي تحققت.‏
أطلب منكم أن تتصرفوا وكأنني أنا المرشح في بطاقة الاقتراع!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/89987" target="_blank">📅 04:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89986">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXN0nTe1TnwoyKd2bVxdFC9EBng29tU9gp2qRvFVUNlAeRXgpFEZKQicTOfYjDW_eTUa92LzsA7jIzBIDTf4cN9M5DbS3aEc4rvI96B5Ks0b-OuvI-rodfPu5Bz_uPL9m70c9_yYQwbuKzFOqdHZwk76ZHRACkikOH1M6HUkbH4OXUKINDS8OhJtgbtT2GZWrGo5SDBYkmNSOnf8n4rygrYRuPk194G4DgMnG1wLRnFkXtW8JcH5_fIAuus1vbJHyEfGVXcCp_WNPhtZ2SBtnB3uoKhxEiIfFGl09S_l-fpERAGxcbmVb8SUJB34erGll9llLL5Rvwzh1wtg0PLqqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
🇸🇦
مصدر يمني لنايا: تم إستهداف قاعدة خالد الجوية في خميس مشيط بعدد من الصواريخ والمسيرات الإنقضاضية.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/89986" target="_blank">📅 04:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89985">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">انفجارات في ابها وخميس مشيط</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89985" target="_blank">📅 04:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89984">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجارات تهز السعودية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/89984" target="_blank">📅 04:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89983">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">الله اكير</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89983" target="_blank">📅 04:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89982">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">الله اكير</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89982" target="_blank">📅 04:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89981">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8305181b5.mp4?token=QVeN-N4y_2GuzOSHwVVIbR8PQnA0BOBMeYaw3RcmSaq8v-BilviFUEJ8GfmlpGj8zLCahbQ_3bQS_mcqnoYKQgzUmickoaAOl1st3EZ_ahKVHSmSuHxLqEleNtuJqDIXxzI1lceCp_pi0oGqCNI73WgF-szQ6zjLlFrD_gSrPuLFmsOWNVKFN8o9pZffRpAnz0tGEkOXQuiWz4ZAXCLbC1VMrBIk3kCj_wrbiC5__Inp2mAeT0vUDYMSjrQdnZJjvxi4lyXPz5GJje2Jl0uVIQXadBYAG9iodW9L7rndGNXwPDupYaAG8_lT0QWtcNiWEzyaHWdj9Jz1cqZFnw3EyVzhbcGhYL7UQVD6eGBpiJKCaUo1cBYomLGqsibYdX29SBOjrvIe4cBxzP3mHcTtuJ2ms7BUh2zK8sErNLk4J51TMTNvu09mQP3QX-Hw4uPkSTfSlZh6Lx7KBv7aHc1E7ymLlmHIrQI1p4sB16tjaxj5JC0o_sDIJ4VtYfHOi7M5D0teitYFAoCHqHcSqNenq30ixrxXbNeqpcZdripmVYmwTwXj-JmzXBCApxPG1jIIxVLafuN_969VhfxTQEBKldB-NSN81fCyB82m73csN564Gas-hEsgq9iCtwxMwD0r9fDzwLDJvCa3o-clO4TaoLGSc3sppZDRHJjiQl0ZZCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8305181b5.mp4?token=QVeN-N4y_2GuzOSHwVVIbR8PQnA0BOBMeYaw3RcmSaq8v-BilviFUEJ8GfmlpGj8zLCahbQ_3bQS_mcqnoYKQgzUmickoaAOl1st3EZ_ahKVHSmSuHxLqEleNtuJqDIXxzI1lceCp_pi0oGqCNI73WgF-szQ6zjLlFrD_gSrPuLFmsOWNVKFN8o9pZffRpAnz0tGEkOXQuiWz4ZAXCLbC1VMrBIk3kCj_wrbiC5__Inp2mAeT0vUDYMSjrQdnZJjvxi4lyXPz5GJje2Jl0uVIQXadBYAG9iodW9L7rndGNXwPDupYaAG8_lT0QWtcNiWEzyaHWdj9Jz1cqZFnw3EyVzhbcGhYL7UQVD6eGBpiJKCaUo1cBYomLGqsibYdX29SBOjrvIe4cBxzP3mHcTtuJ2ms7BUh2zK8sErNLk4J51TMTNvu09mQP3QX-Hw4uPkSTfSlZh6Lx7KBv7aHc1E7ymLlmHIrQI1p4sB16tjaxj5JC0o_sDIJ4VtYfHOi7M5D0teitYFAoCHqHcSqNenq30ixrxXbNeqpcZdripmVYmwTwXj-JmzXBCApxPG1jIIxVLafuN_969VhfxTQEBKldB-NSN81fCyB82m73csN564Gas-hEsgq9iCtwxMwD0r9fDzwLDJvCa3o-clO4TaoLGSc3sppZDRHJjiQl0ZZCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  القوات اليمنية تتمكن من السيطرة على مدينة يختل.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/89981" target="_blank">📅 04:22 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89980">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏القوات المسلحة اليمنية تدمر 5 مدرعات لمرتزقة السعودية في مدينة يختل</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/89980" target="_blank">📅 04:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89979">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏القوات المسلحة اليمنية تدمر 5 مدرعات لمرتزقة السعودية في مدينة يختل</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/89979" target="_blank">📅 04:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89978">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892188075c.mp4?token=WO-fcU78JtAHTApIjJbjO4yzvDExcLQp0S1PYQBhgwYbd5pIMqPac-vyU89Be_5rUN0s21aHGUKr4NdAzM5iw26TrGIxfM6ZSo443TOrVVtoxSsE9EE0a0z-vVRdLas5c0ZKqq8ZSyp5IQKgRDj21td-vuBhqBqbJdR5zB_fRGVBQHfuhbzraxUdoFBoKtDXonhEj3T2kuGfOypn-D1Zp3apqjKs5LIvALp7PneLKUrZ-u3dBpSx07EeJM00qa2GmFUEcfoiAGN2xyutmOOj78UhdaOFDxm1PxgdIeqassEmqby6E4nhIrEcPPczZl4me0V1TtgpgnOxX7cb8nag-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892188075c.mp4?token=WO-fcU78JtAHTApIjJbjO4yzvDExcLQp0S1PYQBhgwYbd5pIMqPac-vyU89Be_5rUN0s21aHGUKr4NdAzM5iw26TrGIxfM6ZSo443TOrVVtoxSsE9EE0a0z-vVRdLas5c0ZKqq8ZSyp5IQKgRDj21td-vuBhqBqbJdR5zB_fRGVBQHfuhbzraxUdoFBoKtDXonhEj3T2kuGfOypn-D1Zp3apqjKs5LIvALp7PneLKUrZ-u3dBpSx07EeJM00qa2GmFUEcfoiAGN2xyutmOOj78UhdaOFDxm1PxgdIeqassEmqby6E4nhIrEcPPczZl4me0V1TtgpgnOxX7cb8nag-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏القوات المسلحة اليمنية تدمر 5 مدرعات لمرتزقة السعودية في مدينة يختل</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/89978" target="_blank">📅 04:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89977">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8ca1cfd7.mp4?token=KfWeRM01LoidqaWxq6l91kIGVV4S8ahzYKYoyiJK4M_xWhY3vP4dIYTy4nDIVxn9-AzGliFbm6QIxO_w5F0khpoIk5f04aTL6DU5meJp3DwN1Phtzi3QQqh0BcG3OEmtsEm3kp_ihAo5kpvY3xp0Yh921502F7YrsTtjY4MK1VFSpI7NW1NFvGvvzfILtpaBNAHNexkS96nooF2t7xi3Tb-3kdDnmwk_V1Cf309oGWK8u8PWGQzymCDWHPMYyB7XSTu7Xi3bW6d0L4QK94xoDd9tB_ZgwEY3qAqiFVNd8Y41iMKq_AD3udPwr5S_uAK_ZKMs1zQmocoH3cCu0wLmK4ovFUasJk1rGfWJTtbJCKtYY2PcQJqiMo5bbssM2reTL-BwISb7ZLasQpADIYV4y1Wsl5ANJOxmcV8Ns0T4jQofFsFxiGu3iADZ2HgfnlLSCX5WTh-L2n2frqz2yHe5htKhiZAXtW1jKpAmrDcR0W-MEdzIufyktRFnHgtEleVWS8hfeSzUbmUv7n4_UiL4rJVPVNjGP29RH1IpIsvoXqUUp5Z1Ay-hbDOgN_hxssooGWU7Loq5AzWtRMgiH5cfEUvOWAUS2X2oWb-r1NtNg9dFxl8dwrZVIQKiqhBLupf0ITmwAZRQ0yjZM8ahsiG_nBisWP8ZtecPjfgUMCQ-jQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8ca1cfd7.mp4?token=KfWeRM01LoidqaWxq6l91kIGVV4S8ahzYKYoyiJK4M_xWhY3vP4dIYTy4nDIVxn9-AzGliFbm6QIxO_w5F0khpoIk5f04aTL6DU5meJp3DwN1Phtzi3QQqh0BcG3OEmtsEm3kp_ihAo5kpvY3xp0Yh921502F7YrsTtjY4MK1VFSpI7NW1NFvGvvzfILtpaBNAHNexkS96nooF2t7xi3Tb-3kdDnmwk_V1Cf309oGWK8u8PWGQzymCDWHPMYyB7XSTu7Xi3bW6d0L4QK94xoDd9tB_ZgwEY3qAqiFVNd8Y41iMKq_AD3udPwr5S_uAK_ZKMs1zQmocoH3cCu0wLmK4ovFUasJk1rGfWJTtbJCKtYY2PcQJqiMo5bbssM2reTL-BwISb7ZLasQpADIYV4y1Wsl5ANJOxmcV8Ns0T4jQofFsFxiGu3iADZ2HgfnlLSCX5WTh-L2n2frqz2yHe5htKhiZAXtW1jKpAmrDcR0W-MEdzIufyktRFnHgtEleVWS8hfeSzUbmUv7n4_UiL4rJVPVNjGP29RH1IpIsvoXqUUp5Z1Ay-hbDOgN_hxssooGWU7Loq5AzWtRMgiH5cfEUvOWAUS2X2oWb-r1NtNg9dFxl8dwrZVIQKiqhBLupf0ITmwAZRQ0yjZM8ahsiG_nBisWP8ZtecPjfgUMCQ-jQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"سيتفاجأ العدو بتقنيات غير مسبوقة في البر كما تفاجأ في البحر" | سيد القول والفعل</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/89977" target="_blank">📅 03:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89976">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">عضو المكتب السياسي لانصار الله حزام الاسد: ‏سواحلنا الغربية جمهورية يمنية لا ملكية سعودية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89976" target="_blank">📅 03:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89975">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a08c86dfa5.mp4?token=CBU7xNxlukJGpF_kkj_n64plfvk4NPKY7NMs5NOfenXDOiMh78Sqxu53YlM_CaMpD5wt8CvktyPnrIjdtIl6uvIvSzKrG4pbIbuBBmInkUzPh90ggotkPumclDAxXLQtxJKDONjTCvuVnb36ccX6YRIMex7TjCG5kZ6J-0w6ovOSdqZqmkWYvIlYCIjnqgCjaHUooIaZJCUoOU5_WKU5HE7JdECbCZk1WB3RukgVdUTXgAxi-Gd-DWcedjlnfliRXF14Lc8zJi-SyjCBi5Mt9G45txxTQnW1sTeybEkay6m39LTzleXDDqsGTejBDhq7wyNJSCY0ae1n_N7c4mdJRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a08c86dfa5.mp4?token=CBU7xNxlukJGpF_kkj_n64plfvk4NPKY7NMs5NOfenXDOiMh78Sqxu53YlM_CaMpD5wt8CvktyPnrIjdtIl6uvIvSzKrG4pbIbuBBmInkUzPh90ggotkPumclDAxXLQtxJKDONjTCvuVnb36ccX6YRIMex7TjCG5kZ6J-0w6ovOSdqZqmkWYvIlYCIjnqgCjaHUooIaZJCUoOU5_WKU5HE7JdECbCZk1WB3RukgVdUTXgAxi-Gd-DWcedjlnfliRXF14Lc8zJi-SyjCBi5Mt9G45txxTQnW1sTeybEkay6m39LTzleXDDqsGTejBDhq7wyNJSCY0ae1n_N7c4mdJRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية تشن هجمات صاروخية ومسيرة على تجمعات المرتزقة في مدينة المخا.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/89975" target="_blank">📅 03:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89974">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇸🇦
🇾🇪
‏فيديو يوثق هروب مرتزقة السعودية من الخوخة وترك الأسلحة الثقيلة بجانب الطريق بعد دخول القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/89974" target="_blank">📅 03:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89973">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇸🇦
🇾🇪
‏فيديو يوثق هروب مرتزقة السعودية من الخوخة وترك الأسلحة الثقيلة بجانب الطريق بعد دخول القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/89973" target="_blank">📅 03:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89972">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇸🇦
🇾🇪
‏فيديو يوثق هروب مرتزقة السعودية من الخوخة وترك الأسلحة الثقيلة بجانب الطريق بعد دخول القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/89972" target="_blank">📅 03:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89971">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9b73cba78.mp4?token=RBxrLc2MQ99WhQNjWFraduz1hwY_qKMiJZeTgCCSjsNQT3ZRZdxkDsdqYP_iahyevt0T-jl3lbs_DJdbHK1uPYUyDi89ikTBqECrRuTYFmYzJwypzpG1Bu02QT9b4pJv6ISo3sFnsTov2A1x5YTpznJ_bbekUQPzaTVrLIfO9sz-7kqRNy9N4Ibt2itVwzxPLOguI_rVJmYoah0tXTaGOrlWr27gf11iMp7HiRVUxHodNfoi4X6n-qIJa-Fq9VmPh4I-h5njU0rsgP96Jm8bivmXPy9-qS-enClCO14YQ3CtZ3mZARnfZ5AkipIzjULTXLci0Dt9VnIIj9-LP7AKrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9b73cba78.mp4?token=RBxrLc2MQ99WhQNjWFraduz1hwY_qKMiJZeTgCCSjsNQT3ZRZdxkDsdqYP_iahyevt0T-jl3lbs_DJdbHK1uPYUyDi89ikTBqECrRuTYFmYzJwypzpG1Bu02QT9b4pJv6ISo3sFnsTov2A1x5YTpznJ_bbekUQPzaTVrLIfO9sz-7kqRNy9N4Ibt2itVwzxPLOguI_rVJmYoah0tXTaGOrlWr27gf11iMp7HiRVUxHodNfoi4X6n-qIJa-Fq9VmPh4I-h5njU0rsgP96Jm8bivmXPy9-qS-enClCO14YQ3CtZ3mZARnfZ5AkipIzjULTXLci0Dt9VnIIj9-LP7AKrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هجوم مسلح من قبل مجهولين يطال عجلة في محافظة ميسان جنوبي العراق؛ مقتل 2 كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/89971" target="_blank">📅 03:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89970">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4b99828a1.mp4?token=uAtrKl-Oh72uYTn0jvCtS2kf9UEJi7qJDQM9G2kEVQo_3MTB1VtRyYmfgVg1uH5BUybfmGMHxg4Pkd2fUcLFCfCrQoyU-KU7B4jEcAI-vCB3GaiVBFf-g6y20dhV1DIvke6EzaLBkjx5yyMjaSRLfIJhLCqdbHYAiU54PNDqnZHFDjQJ_hfA1TgeA2dvCIbQ04ow1Ki-rZOM2OaJvolqerInAuGmay5de_Wvtx9AV-jw-zRWEjc4VPxvdzdnVsniJxQRREUxQFIn_eW4GuU671vXUHRfmYeAhl9RGITrMn7Dg3AsqYAYbItbiKHAlkZ1RTd-Xvyb9mKWoZwJG6absA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4b99828a1.mp4?token=uAtrKl-Oh72uYTn0jvCtS2kf9UEJi7qJDQM9G2kEVQo_3MTB1VtRyYmfgVg1uH5BUybfmGMHxg4Pkd2fUcLFCfCrQoyU-KU7B4jEcAI-vCB3GaiVBFf-g6y20dhV1DIvke6EzaLBkjx5yyMjaSRLfIJhLCqdbHYAiU54PNDqnZHFDjQJ_hfA1TgeA2dvCIbQ04ow1Ki-rZOM2OaJvolqerInAuGmay5de_Wvtx9AV-jw-zRWEjc4VPxvdzdnVsniJxQRREUxQFIn_eW4GuU671vXUHRfmYeAhl9RGITrMn7Dg3AsqYAYbItbiKHAlkZ1RTd-Xvyb9mKWoZwJG6absA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرتزقة الإمارات تلقي القبض على مرتزقة السعودية أثناء الهروب من المخا نحو عدن.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/89970" target="_blank">📅 03:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89969">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318d8f857b.mp4?token=tXHIk8I0JVnqYYkU7B7WqxGV9PSpRQ8X0JMRFP6_nfQrxY6h2Wyavy6hWt4nLq_knjkoqD5F7431qrZiLxxo5Z1cyx9FVvCASgnXZyJfj6llBHIoQTeL2A5uiBtTIWK2G1v0of4019zpQ65E90AUtiGzSOUnb-SfP4x0cpbZe8NXjrBiYeqgPpyXGx8Ku8QDAGvCJ1JQ6xEQZwnVdbvWTFLoiTTSrXL3B6RRVMMRd1_UdWFdd_os_thMsLnlVxbMP3lPOCrNxefT9HVSMHcgXhxTRfAZ8m8LpS8gBVdsvC3yJh656CxeapCvm74xcV8_1VIb7adQaAEKQwspNWAUzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318d8f857b.mp4?token=tXHIk8I0JVnqYYkU7B7WqxGV9PSpRQ8X0JMRFP6_nfQrxY6h2Wyavy6hWt4nLq_knjkoqD5F7431qrZiLxxo5Z1cyx9FVvCASgnXZyJfj6llBHIoQTeL2A5uiBtTIWK2G1v0of4019zpQ65E90AUtiGzSOUnb-SfP4x0cpbZe8NXjrBiYeqgPpyXGx8Ku8QDAGvCJ1JQ6xEQZwnVdbvWTFLoiTTSrXL3B6RRVMMRd1_UdWFdd_os_thMsLnlVxbMP3lPOCrNxefT9HVSMHcgXhxTRfAZ8m8LpS8gBVdsvC3yJh656CxeapCvm74xcV8_1VIb7adQaAEKQwspNWAUzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ياليتنا كنت معكم</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/89969" target="_blank">📅 03:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-89968">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJV5_OYUCMemKVNwzsMoxm9r74D62k-vUQAM2jzDFY8ID77ApvfAcaMM0gfGssBnjjQ6StraYCi6cTr0LVnIJHHAjmfpEIMqZpspGgveOtoWgjFGXm2gp4wdh5vGUBAwAK6nm7rQo5ZWDVpL_Be9WaVV5ZtNAfGKeN8_sK-H40M8avYNjrarg6b0IJZ_R2UQeltd9kAWRdvbHKz6OMfQodgA0YaUvh7sDiG0zYu5hEikOD8J23PxxL5mzX6UwliNq0c0e2mHZEkm0T6VDccLdYPg2b9KkEMxlMFiqzjvM2Xd9hrCzUn3sswV2l1mJbYEYYjRSZ6t5erhTKi3l9ezGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالة من الرعب يعيشها مرتزقة السعودية داخل مدينة المخا مع اقتراب انصار الله منها والبعض يبدأ بتسليم سلاحه للاستفادة من العفو الذي اعلنه الانصار</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/89968" target="_blank">📅 03:00 · 19 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
