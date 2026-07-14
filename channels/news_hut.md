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
<img src="https://cdn4.telesco.pe/file/A30rNUImDgbZtrdOEwN72fCZhlVSAC3wdWgGmZ7NZiExaSq_rHFn25IQnVS_19CDI_IloM-GFhqATBKOJ4REVyLgL_t4aVRnKrO5G0efEKaPCkMs9xPZ8pa9byzR-yC8F0VA0ypehS36FKpfsZlJhQWaBDF1E0yRqN9N1kfKB4ljtxavlSTEXcw5g5uNZtWAYo6xQWlVB_QXt-jCKgWq_WMo7NUvSRxiV6SkRmipEydCq1skjoxRcxiBuUerfGOKYCr1680l0VN6SBnJ4Yeh2ofaa8KuJmn87BObUInvQvZeBBWu-6iug8XnjsyJ8WQtt-sWDTKnkWouc2Loh_5kiQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 173K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 16:14:42</div>
<hr>

<div class="tg-post" id="msg-68085">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=pD0DYNc8dfaNUHP3l_C-Z4_o9A69ZIqB-myf0zNcfyXLx-PVlVHyANTJ5L1fMmhYVZz3j1ZglL1cfOTl6yGW6uGMgbscE5Hr9ZBwY4JiIY78IkO-5KbfHkhu3GPXxU7di34JkXVRLnMVQoO2aCPEkj93Q76Ct8m9r3giEEMsytqEJyFL1-mcRf39uzCweEcJ9N1nL1YGKCjzqlpBY8zacyeOAGCAhuo-xmbvmYFWcWtSze8kBBKFukENZRydczdO-P9fwXbnhfjB0C1eUofihabcI5az5FXkS_4Tz89P07jJ9L6sRzneW7J6EuFaTdPK_UP36lGNczQ-2atcs-u1Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=pD0DYNc8dfaNUHP3l_C-Z4_o9A69ZIqB-myf0zNcfyXLx-PVlVHyANTJ5L1fMmhYVZz3j1ZglL1cfOTl6yGW6uGMgbscE5Hr9ZBwY4JiIY78IkO-5KbfHkhu3GPXxU7di34JkXVRLnMVQoO2aCPEkj93Q76Ct8m9r3giEEMsytqEJyFL1-mcRf39uzCweEcJ9N1nL1YGKCjzqlpBY8zacyeOAGCAhuo-xmbvmYFWcWtSze8kBBKFukENZRydczdO-P9fwXbnhfjB0C1eUofihabcI5az5FXkS_4Tz89P07jJ9L6sRzneW7J6EuFaTdPK_UP36lGNczQ-2atcs-u1Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام ویدیو ای از حملات به ایران در طول شب منتشر کرد.
در اواسط ویدیو نشان میدهد که لانچرها در فضای باز هدف قرار میگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://telegram.me/news_hut/68085" target="_blank">📅 16:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68084">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdI6sQNg8c9l8npIlxZLOwyJLwcAFqR7qEHebaztYVJl4aJdjvcp8TLdhlFwIjwykE0bkkhxxLmy09wvpK9hA-CfRVNFbudqoqJzK4dnXq1OKmT-9cHvoyVGPzctO7W5B1xwygFw713AWQYCM2Z2zTWmJy1IovSYiQvJZHc03CrT6f1fuoEb8NAfODxIMeXxqCeSE0SuBZum8CkniOfnE9KItk3p4KgienAFO3JJO2EO69bFqDlou1KlYSKExyyw1Nrq73C7Du2wxNgdEfxP3eQtnzdzmou-aWHoiGmjhvR09xqKICwQXH_ASBU6jeA3etamyliirK872E_OGEgilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیکتاتور قالیباف
؛
سید محمود نبویان نائب رئیس کمیسیون امنیت ملی مجلس و ابراهیم عزیزی سخنگوی کمیسیون را که از مخالفان سرسخت توافق بودند از هیأت رئیسه کمیسیون امنیت ملی حذف کرد.
عباس مقتدایی نماینده اصفهان و از حامیان دوآتشه عراقچی به عنوان نایب رئیس اول و حسن قشقاوی از دیپلماتهای حامی برجام به عنوان سخنگوی این کمیسیون انتخاب شدند
.
بهنام سعیدی از نمایندگان نزدیک به قالیباف و یعقوب رضازاده نماینده سلماس که اخیرا در مناظره‌ای با ثابتی از توافق با امریکا حمایت کرده بود نیز به عنوان دبیران اول و دوم این کمیسیون انتخاب شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://telegram.me/news_hut/68084" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68083">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=j2tllj09FH1F0UR21kFQlXCM6r8raP4SoE81IzUZQdKXxbqG_pSVNXWSgD5bH6cdTnoxFr_8OnVi7dwW1PG09e7-yY52-X1J6Tlsdc0KVQ_wb8NEg3CTJlxtNhIt74zNMJdaIuyZW6n8V_qAuWSUrSuWfZlhYQcR0RayCMWT_y7mJPHkEtjJQdcyGERL7UI0-FK1DFpUgn1AzpE_KOlU38tU6b5utqia91U54b4e5cf8WOm4DnpkhveVcIQcuVnob8EEgstQMvUtF0Htdunagz49_Nan2g4TDX5aX3JH-_2CoegB3qK4EZOHjtkOGAlooD3woRMPpvVVMzxEj2vAmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=j2tllj09FH1F0UR21kFQlXCM6r8raP4SoE81IzUZQdKXxbqG_pSVNXWSgD5bH6cdTnoxFr_8OnVi7dwW1PG09e7-yY52-X1J6Tlsdc0KVQ_wb8NEg3CTJlxtNhIt74zNMJdaIuyZW6n8V_qAuWSUrSuWfZlhYQcR0RayCMWT_y7mJPHkEtjJQdcyGERL7UI0-FK1DFpUgn1AzpE_KOlU38tU6b5utqia91U54b4e5cf8WOm4DnpkhveVcIQcuVnob8EEgstQMvUtF0Htdunagz49_Nan2g4TDX5aX3JH-_2CoegB3qK4EZOHjtkOGAlooD3woRMPpvVVMzxEj2vAmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده(سنتکام):
ملوانان آمریکایی بر روی ناو «یو‌اس‌اس جورج اچ. دابلیو. بوش» (CVN 77) عملیات پروازی انجام می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://telegram.me/news_hut/68083" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68082">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXTap9VgC4JfqwDNhOrltsVIHBdcIanzBfW9exqMz4L7liDNqWJa3-vsptbmylmamve9DLiEcNyFPy56Lemeuk8_J3wLBQDTctXW3iufQp8P1m3kW0iqZMYOUMDTe5WhTUmbwJ3WKNtEUnTjdQWo1IITZt_3nTpeLyifmvF7fS1jrzHPEzr_w1osLfvp56zM4wKwkvhvNcg_i3LI0RpzVc7Lh5_wJK1CTzFhlDOjxEfljdRr4hNLNvqYq2Tgq9sCD2k60ivZstiXH2YpBn9loIw10_KsLiMIp7FzZse3D8nVtQbnLdFz9VjjHbnBiv467cs34nGnaSZR_7CDlwguTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لبنان و اسرائیل مذاکرات خود را در رم از سر گرفتند؛ در حالی که لبنان به پیشرفت در جهت عقب‌نشینی ارتش اسرائیل و اسرائیل به پیشرفت در جهت خلع سلاح حزب‌الله امید دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://telegram.me/news_hut/68082" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68081">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=dTVnRD-k-inLNcnWaE2Sj3_jgifxlcg_uHRpuAZwA-jPnWtQy2UFhUBtal2zYGKxv9FuT5Z1N_5J27YMtymKFRQdxEPZJamEv1Hh8gS_Nqt0Y-qoMlDoY1RB_HgOucLskczrrlNFrml05KCVaIvL0zCvcZc72lCxyNITuVZUWuLFeeQTR3vvN_2J81uhlZx-m9ynm7TxqmlTaX2F-FQi7lC3dsVVVAhS8ij9s4VOCFeUfeWilZh0IptMXyzf4HyZcDs1bd7hZU3L_3VlbDR1icTJgnwr0qbJuly7BRvsvJsQQXJWjLa6N-a89eP3jYibKdoV--T4pE6qu4mPmgEMWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=dTVnRD-k-inLNcnWaE2Sj3_jgifxlcg_uHRpuAZwA-jPnWtQy2UFhUBtal2zYGKxv9FuT5Z1N_5J27YMtymKFRQdxEPZJamEv1Hh8gS_Nqt0Y-qoMlDoY1RB_HgOucLskczrrlNFrml05KCVaIvL0zCvcZc72lCxyNITuVZUWuLFeeQTR3vvN_2J81uhlZx-m9ynm7TxqmlTaX2F-FQi7lC3dsVVVAhS8ij9s4VOCFeUfeWilZh0IptMXyzf4HyZcDs1bd7hZU3L_3VlbDR1icTJgnwr0qbJuly7BRvsvJsQQXJWjLa6N-a89eP3jYibKdoV--T4pE6qu4mPmgEMWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:  اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد. در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://telegram.me/news_hut/68081" target="_blank">📅 13:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68080">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
معاون استاندار بوشهر:
چهار نقطه در شهر بوشهر مورد اصابت بمباران آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://telegram.me/news_hut/68080" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68079">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Szc0KHvvpEMER4Yb6nqgoaAo1mQpXZhPruviNxWMaH5PYxFrCo7r_m55mU9JGq-ySjVtnhd7X--HSkSsLGCxO0brQy8bNJBnVa5yxiDauIXB6nv6ECmTerDtj_1bZx4qwUxpJ97dktFzt5-VeuRTY5uTmVi4l1MUfyoPUFIHC08MEhCEk9fSFLyto9nzQwqddQUGcJ_mTRJ38Pu6xKSc6b9c9ZLVmfjT_tv-TGzncDcUgBJfvA120j4FAagvFrP73R6SlDwUgBawF6P3FlE5icsr136Two40XYWdF8Jap44HWFdqUp1okD8_0RxVs46S4NLjzVhuqEzYbf7Q6zKJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نمایی دیگر از بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://telegram.me/news_hut/68079" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68078">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJUIOEMoN6Jp-DX4XEq_L1xZhP3HJyvfqCOaPBnmsLQ-XYvIR_Oiz1kgIjzqMySP5wHfTlhiMoTL6CTqJecDSBPHhGjPd8cv6Uc0g000XyEdNT5p0U0bvRCmc8JeOpgbOGa_8NE6V5xZgJaw4w34Ut_L9QOuYjRXfZSVUJvz52I2Dlb10N999rAAEEQM5Xa8HDCzGJ4a6XUlemvYKErAd38w4fnZr8FC6adxOOFAGe2svqn5xRFLhs-A13AzMp76SI3KBHydc9BMTyKKdUDdpVJvFlKSv5_5pK9kM0V5m3zod3XfMqTiIkt6xZkzpcNtaclqml-VPb8yKbizHwzTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://telegram.me/news_hut/68078" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68077">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://telegram.me/news_hut/68077" target="_blank">📅 12:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68076">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
🚨
پنج انفجار در بندرعباس
@News_hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://telegram.me/news_hut/68076" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68075">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید در بحرین
@News_hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://telegram.me/news_hut/68075" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68074">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ گزارش های اولیه و #غیررسمی از حمله سپاه به سفارت اسرائیل در بحرین  @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://telegram.me/news_hut/68074" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68073">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
#مهم
؛ گزارش های اولیه و
#غیررسمی
از حمله سپاه به سفارت اسرائیل در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://telegram.me/news_hut/68073" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68072">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=aUds1vC2UWKvKWBpSvVqgJaVqrHe9cjmXU7DAseTAC85DmL6tcPZzmtiYB7tWoX61wR7S6v8jHLwaYIUJ-Cx9g23yU___U_B2kcA0oOYORMOuypFXiGUr4uhLAUWsNIWD1Tdy6CGCpsNc0RrFZfnUZd6RqJHsTCWFgt1jRg4jBWB88aDh8ZVhyJkkKdml_lNp0r6UQ61kTf-uCwRk2YW7l-dCKtNt7bTjI22k-ez3oC3TKpKwWFcEkXRyDsnChryZ-8CGqpfXkM6WvhZPCiLxa_S-6ZGuzzSG5FTNRJ6yAt6yMyfjz-Wcg4oIP8vqpESPljInkAxkhFuOZIgTLpPoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=aUds1vC2UWKvKWBpSvVqgJaVqrHe9cjmXU7DAseTAC85DmL6tcPZzmtiYB7tWoX61wR7S6v8jHLwaYIUJ-Cx9g23yU___U_B2kcA0oOYORMOuypFXiGUr4uhLAUWsNIWD1Tdy6CGCpsNc0RrFZfnUZd6RqJHsTCWFgt1jRg4jBWB88aDh8ZVhyJkkKdml_lNp0r6UQ61kTf-uCwRk2YW7l-dCKtNt7bTjI22k-ez3oC3TKpKwWFcEkXRyDsnChryZ-8CGqpfXkM6WvhZPCiLxa_S-6ZGuzzSG5FTNRJ6yAt6yMyfjz-Wcg4oIP8vqpESPljInkAxkhFuOZIgTLpPoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداسیما داشت خلاصه‌ی یه سریال رو پخش میکرد که تو یه تیکش اگه فقط صدارو گوش کنید، فکرمیکنید صداسیما در حال پخش پورنه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://telegram.me/news_hut/68072" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68071">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=FO9mF45-ozmA6u3oJaSv3VPM0qo3T09hlokq0yMatQJI_Rt-2XWmFXpL6LneqIqb6TDdDlxYAzuVd6daks9VoKtbPPFrAkfevw7TloLn6UTlfeuR4ldA7W6U6gvnkWRqBzANf3eur-zBwSbum8j_elUDRpHqqzfKIcRD2JMbTjmkfy4-4can9auLygAYYAijCdVLx7dNY4k4PN55yRkc0i5AjZ8GVvlxj71OPGn4gUPEVxgYQoazBrwIRw-25SsmgzdXcmZEfdrNEvGlhWtLMa7rGUG3vokgf37FmvDRE_ZE7ivtL7aeDT6LRTX_jt__mWS5v0ma-Ta8ORrR9Bje7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=FO9mF45-ozmA6u3oJaSv3VPM0qo3T09hlokq0yMatQJI_Rt-2XWmFXpL6LneqIqb6TDdDlxYAzuVd6daks9VoKtbPPFrAkfevw7TloLn6UTlfeuR4ldA7W6U6gvnkWRqBzANf3eur-zBwSbum8j_elUDRpHqqzfKIcRD2JMbTjmkfy4-4can9auLygAYYAijCdVLx7dNY4k4PN55yRkc0i5AjZ8GVvlxj71OPGn4gUPEVxgYQoazBrwIRw-25SsmgzdXcmZEfdrNEvGlhWtLMa7rGUG3vokgf37FmvDRE_ZE7ivtL7aeDT6LRTX_jt__mWS5v0ma-Ta8ORrR9Bje7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمران رئیس شورای شهر تهران به سوالی درباره قطعی برق بدون اطلاع قبلی:
اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://telegram.me/news_hut/68071" target="_blank">📅 11:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68070">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu-xxJSYmkUHLYRHUa2xzSyq9W6cNPeR8FPLBNjsRoF4O2nVuXZVy-inED8S5S9DEwWbmmPbH5_QHwqvSIVjh9eNO6K5kyua0LonoCojF2V4QJBVZq6u3mKjtdDRmBSJZYVNV0N1qedBWtzXXOQVgn6GFhbphaZcTCCqjht5chxnGtI2tJD8y4qk-xfMJKiQmgKmm-tjxdqfNOTN-sjYhduZGmsRmvf-gScUBmh5cAY_Zy5MPvxAbZOhH-mBRqch5DmjOM5rFREbacwQ7zMpSk36Qwz_x29iJSEgCYzKVqM0L0NTunbW_5KUYoFiHEq9PpUDq6I3H0iWfXo__AHntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی بریتانیا:
گزارشی از یک حادثه در فاصله ۱۳ مایل دریایی جنوب شرقی لیماه، عمان، دریافت کردیم
یک نفتکش گزارش داده است که هنگام تردد در مسیر جنوبی به سمت خارج، مورد اصابت موشک قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://telegram.me/news_hut/68070" target="_blank">📅 11:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68069">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=XUVdsk3HdRUGFCCEIRNpx908KxeFyqNm6ZjKZvsvQc3QOm-CFA528oNwQmWX4Yca5u5VP64tQZzfZt8gU-g_AWV4LlF3PY0r1Bb_QfQw40M-ShbbwNH8qSLqHy9PJxsHb21FZAlS7Zv7rQIjgCVrPCZzcK5OqC7V6-Lk9eM_OaxVeIqnwDzcfRHZtNy3Fo7xwK7FSFidxgI7nG7r3jXdhZeXkz0juPI0uLFF-PVnXjTjhfHMOZocP20hFCxDqD8jJZI7C2LBzfj_c23s2V5UdzE250J4FN7xLt35xHujclfk_tF1g6-qIWWxZfIcqYCINWKYDzJd9GFMRJxAxGi9cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=XUVdsk3HdRUGFCCEIRNpx908KxeFyqNm6ZjKZvsvQc3QOm-CFA528oNwQmWX4Yca5u5VP64tQZzfZt8gU-g_AWV4LlF3PY0r1Bb_QfQw40M-ShbbwNH8qSLqHy9PJxsHb21FZAlS7Zv7rQIjgCVrPCZzcK5OqC7V6-Lk9eM_OaxVeIqnwDzcfRHZtNy3Fo7xwK7FSFidxgI7nG7r3jXdhZeXkz0juPI0uLFF-PVnXjTjhfHMOZocP20hFCxDqD8jJZI7C2LBzfj_c23s2V5UdzE250J4FN7xLt35xHujclfk_tF1g6-qIWWxZfIcqYCINWKYDzJd9GFMRJxAxGi9cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی،تحلیلگر ارشد اینترنشنال:
چشم انداز موجود تشدید جنگه،پاکستانم دیگه نمیتونه بین ایران و آمریکا میانجیگری کنه.
جنگ سوم بین دو کشور تو روزای آینده شروع میشه.
اگه اسرائیلم وارد بشه یه لایه دیگه از سران جمهوری اسلامی رو حذف میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://telegram.me/news_hut/68069" target="_blank">📅 11:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68068">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdbTWQbQWRmZnT9S61uaRPlTPv_uvchP-giGxKZGf-J0SCtKcQsd4MASyZd9FFmUNpjwklVb_ACo9Le290l0pVoGBVZpJjTjwGD0MFumeR_kZ9qo6c9UJdmRjDH4o-_cXekzKgrFFcZnN9rOkR_FqO_99icrHP6HLfu6EO3WXKJLR6T7LPkdgMJkKLSSjTisZY63kWZzTPhUWBP7OEEas9Fnitm9tEUiKQqbEbRQelQuYAprw-6j1KDOhC8MK7T9U2VfoYKndXCnRIyntJ8Gw8bjCFIGLkGoI0K6RafVDbDPJLv7DkeB_V0T1-gb9AWhLlvIQag7vfFLaEgo28gRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) آخرین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب (به وقت شرقی) روز ۱۳ ژوئیه به پایان رساند.
در جریان این عملیات پنج‌ساعته، نیروهای آمریکایی با هدف تضعیف بیشتر توانایی ایران در حمله به کشتی‌های تجاری، با موفقیت به اهداف نظامی در نقاط مختلف ایران از جمله بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردند.
نیروهای سنتکام برای هدف قرار دادن سامانه‌های پدافند ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران، از مهمات دقیق‌زن استفاده کردند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند.
نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار باقی مانده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://telegram.me/news_hut/68068" target="_blank">📅 10:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68067">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=rjsxCYhe_xym79mv5b-55FsawrhtcVTDrZBEAmabvR2jSvcYyJC9KCNPJ_qrpt0jxQdvyG5bJ38LCBnWF5aZMRLum5Qb4ZNsBTLPXzHX-jThpKF9vEKYdNVgb815-9kWK_5pz0QoXuY8LyePD7kxCnHZ6tC4OoERPb81yYXuMYROC8edWIGCKwchrlrMqO1F4bkvLXfhR6257PTL1HkJeFT7ATfjGkd8yjidVtugixm6fihAyIIXoUnxxSPA_GaJXZHWe128vMdK0FPFSmbfCqZFTSxLFCTQ-6IGwwic603U_2-E7sYCiQl_CPecOxenRxDU4ep8EdwWw5ekREXpCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=rjsxCYhe_xym79mv5b-55FsawrhtcVTDrZBEAmabvR2jSvcYyJC9KCNPJ_qrpt0jxQdvyG5bJ38LCBnWF5aZMRLum5Qb4ZNsBTLPXzHX-jThpKF9vEKYdNVgb815-9kWK_5pz0QoXuY8LyePD7kxCnHZ6tC4OoERPb81yYXuMYROC8edWIGCKwchrlrMqO1F4bkvLXfhR6257PTL1HkJeFT7ATfjGkd8yjidVtugixm6fihAyIIXoUnxxSPA_GaJXZHWe128vMdK0FPFSmbfCqZFTSxLFCTQ-6IGwwic603U_2-E7sYCiQl_CPecOxenRxDU4ep8EdwWw5ekREXpCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخطار پلمب، مانکنت نامتعارفه !!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://telegram.me/news_hut/68067" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68066">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AidDyfRlCLd7noFF5qyL-PeqsY5i7h562-Hxdm_nmla2Uoq41i6WHYuK1EuTcYnyhSzf0418XgYy3U3uVclC9T-7hoAnHQb5KNKPlVlWxKEu0EnXBHhOjb9XplWVtU3TnsviOq2RhK5wzslx1qGkUjP_Q0TShvJEgGWaM51YJIIgqIfGnS5zcSg2L2HbfQmYl1FetiEW_0a-tERqnSXQOjZ8TSnvMJDy4ZNSOaTgCW1Uq1sQwHTK5Mt5S14AoANuuQw5k1jKdW9LWTd5307qws3Zb0Gr5xofCgJdPdpwCUdaxPb1ZnoMXL0nXY1ifyaESFTXsWhaSIqL9fUMYDD4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:
اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد.
در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای خارجی، از جمله در مجارستان، با احمدی‌نژاد دیدارهای محرمانه‌ای برگزار کردند و از رویدادهای دانشگاهی به‌عنوان پوشش این ملاقات‌ها استفاده کردند.
این طرح در جریان جنگ ایران و اسرائیل در سال ۲۰۲۶ به اوج خود رسید؛ زمانی که مأموران موساد پس از حمله هوایی اسرائیل به محل اقامت احمدی‌نژاد در تهران، او را از آنجا خارج کرده و به یک خانه امن در داخل ایران منتقل کردند. این اقدام بخشی از یک عملیات گسترده‌تر برای تغییر حکومت بود.
این عملیات در نهایت ناکام ماند، زیرا احمدی‌نژاد تحت شرایطی نامشخص خانه امن را ترک کرد.
به گفته مقام‌های ایرانی، او اکنون پس از آنکه مقامات از تماس‌های ادعایی‌اش با اسرائیل مطلع شدند، در حصر خانگی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://telegram.me/news_hut/68066" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68065">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KspMF-b6hfGalArDJ8pXKJkps4Mv86AjnTp0nanP67TF5cVLJJCOrF8Z25QTyYcfkZkleMaQgkIZVa_KSrpfXZRpek2CLpVo7C_za6PLLShKvOkPU_XakaN30W_K2OxZZdb8N4m2-9aMBmdospMvuQ4uZ3ZLQxUWp7tQmU_T0w60za7qK8m2xUOpGzYi3kATZRZHLpQRkqbZCsgSAOH4C56AoJKbt4cEp1aYVu5_L5BfBQVsOM56pspt9ePhSDQNbYc9ObvI_sr_bBrYqHSO6eX_DPgAdGT5c8CViYtl_CkrDJZV0cOz7kkUd9KcnwnVmlCSO3yKuGdUlq96Neddxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
وین ریت 80٪
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇳🇴
وین شد
✅
🇦🇷
⚔️
🇨🇭
وین شد
✅
حالا هم دو تیم فینالیست مشخص و در کانال تلگراممون اطلاع رسانی شده
⏳
🇪🇸
⚔️
🇫🇷
‌
󐁢󐁥󐁮󐁧󐁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
t.me/bet__gg</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://telegram.me/news_hut/68065" target="_blank">📅 03:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68064">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=uC2BMCfMGxmtb8Yf4k5CL1EZVtU8qTOfbg_QSZDWHNrfCEsLHbGxiwkAzegR9PlwNNyRYgwr09gca1mmUnCLYGOK5NX62GzpWgnSw4GXJ6cj_-6ky5mMdK-lueg2xjwJ7COVRBsJYvs6eC-5O8NUWkYA2JVtTeXncA5f7p4-xT0XzMQ_BXBM38aSTpGzPalfep0tFGtCZAJJG7xEWswKphfJltvy5GNjh3T6hNgZp1Dn7F8iSnYRTjsjsMtWsAB6qE95o-efRslySFi9oScmwk4Xcp-38s1VuTFDxae16bxDopj4zPaYSoZLlnF6Ij7-1aCdt3b-uNlhKun5H7z0FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=uC2BMCfMGxmtb8Yf4k5CL1EZVtU8qTOfbg_QSZDWHNrfCEsLHbGxiwkAzegR9PlwNNyRYgwr09gca1mmUnCLYGOK5NX62GzpWgnSw4GXJ6cj_-6ky5mMdK-lueg2xjwJ7COVRBsJYvs6eC-5O8NUWkYA2JVtTeXncA5f7p4-xT0XzMQ_BXBM38aSTpGzPalfep0tFGtCZAJJG7xEWswKphfJltvy5GNjh3T6hNgZp1Dn7F8iSnYRTjsjsMtWsAB6qE95o-efRslySFi9oScmwk4Xcp-38s1VuTFDxae16bxDopj4zPaYSoZLlnF6Ij7-1aCdt3b-uNlhKun5H7z0FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو ای از حمله امشب آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://telegram.me/news_hut/68064" target="_blank">📅 02:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68063">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=RdUIOhGBH6-zWHgwwsF5KfD2omqI-o9aP0sBURaFORYw6Li1gW6h75k_bhtGYNufGfvEXJw2ZK1WdkBhv6_TaqiY5CsU9cYpktOBJDgQHhpIFPykxcUWOrVaRrozciJeR5TH43r-H-sLu4XDBJogUTRa4w2bn4j_8cgE8mEqft-gLtsR13WJRMtghoZQ7qvE7mMgpV9E5BwllefbZ4l_0qim3xrgyR26wguoaitLsefCEvksav9cxAp_P8wrhq9kDc2aOLaMbolW5fxB7btMiEai0Xsqn96C5Efr9GWJhkP01Ry39q6VBmlO7kRlw5xVBHPoA6G4NIqnSUuO57yOZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=RdUIOhGBH6-zWHgwwsF5KfD2omqI-o9aP0sBURaFORYw6Li1gW6h75k_bhtGYNufGfvEXJw2ZK1WdkBhv6_TaqiY5CsU9cYpktOBJDgQHhpIFPykxcUWOrVaRrozciJeR5TH43r-H-sLu4XDBJogUTRa4w2bn4j_8cgE8mEqft-gLtsR13WJRMtghoZQ7qvE7mMgpV9E5BwllefbZ4l_0qim3xrgyR26wguoaitLsefCEvksav9cxAp_P8wrhq9kDc2aOLaMbolW5fxB7btMiEai0Xsqn96C5Efr9GWJhkP01Ry39q6VBmlO7kRlw5xVBHPoA6G4NIqnSUuO57yOZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انفجار سراوان سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://telegram.me/news_hut/68063" target="_blank">📅 02:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68062">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
انفجار امیدیه
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://telegram.me/news_hut/68062" target="_blank">📅 02:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68061">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
حمله به سپاهِ سراوان در سیستان و بلوچستان
@News_hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://telegram.me/news_hut/68061" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68060">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=NlpS8k_qyF1AsDyG51RVT8xSFD81UXYJgzsf_utTJHQMGknBsYRSVuGjdSlTXtCk9gYgwJTsHUQ60hU8OMbTP4HRCaU0tGtSfu1sFZhPysuWXXh6UWLUw-StXgvvw-Hm305xTRpgHX8RBaYyAhwjCKFUiewyysu54YQBfQipTg8EwlPkbrrwWhEq3Qiho8NMSdXSetd4-Umkwn7wefB9IGE9hxrWrjWenjtexH3Xx2D-dhYMKWJHP0A9iujNrmYmVmg7nnyAWN0CkBG6-mwLl9ptpnd9JPXtwdwcKAHFRPlvTcaW_DtdngdS4KOBtq-3g0TIpiYiE0HBBxdkxaAwpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f42a8e75.mp4?token=NlpS8k_qyF1AsDyG51RVT8xSFD81UXYJgzsf_utTJHQMGknBsYRSVuGjdSlTXtCk9gYgwJTsHUQ60hU8OMbTP4HRCaU0tGtSfu1sFZhPysuWXXh6UWLUw-StXgvvw-Hm305xTRpgHX8RBaYyAhwjCKFUiewyysu54YQBfQipTg8EwlPkbrrwWhEq3Qiho8NMSdXSetd4-Umkwn7wefB9IGE9hxrWrjWenjtexH3Xx2D-dhYMKWJHP0A9iujNrmYmVmg7nnyAWN0CkBG6-mwLl9ptpnd9JPXtwdwcKAHFRPlvTcaW_DtdngdS4KOBtq-3g0TIpiYiE0HBBxdkxaAwpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیوهای رسیده به ایران‌اینترنشنال نشان می‌دهد شناورهای تندروی کلاس «گلف» سپاه پاسداران در بامداد سه‌شنبه ۲۳ تیر پس از حمله آمریکا به مواضع جمهوری اسلامی در بندرگاه و دریابانی کیش، در آتش می‌سوزند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://telegram.me/news_hut/68060" target="_blank">📅 02:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68059">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=Savb-u-aBuR_Y3_NLiSQr8kPc265cXmqrWQHxCO2brGwvydzxJbo5vHijmKjMOwPXP_FaKzXtCBudmqIhNq5p7As9s7X-iIb2aVx0B77eT6ds4coqXJX5MPywvW2vNq_lTV4CVy0wdeYwx-lL9ET_e865voet75-fxaF0gaJQG76XVUC20-q8MZ1bWlK76Ha9VuiaY82fW0-0fHAu6WlWmXkpJ_hSbG0XywcOVyPjvrK0z91xLlGaMC_anlq-C_RagyHLIzPi6Q5byai_XiPd67mcCzJN6nEFwI7jmxqBAY7hWhwjEHAozmXU-MVD-5spRsPUjzhyryy_oVlXSkkzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c797cee32c.mp4?token=Savb-u-aBuR_Y3_NLiSQr8kPc265cXmqrWQHxCO2brGwvydzxJbo5vHijmKjMOwPXP_FaKzXtCBudmqIhNq5p7As9s7X-iIb2aVx0B77eT6ds4coqXJX5MPywvW2vNq_lTV4CVy0wdeYwx-lL9ET_e865voet75-fxaF0gaJQG76XVUC20-q8MZ1bWlK76Ha9VuiaY82fW0-0fHAu6WlWmXkpJ_hSbG0XywcOVyPjvrK0z91xLlGaMC_anlq-C_RagyHLIzPi6Q5byai_XiPd67mcCzJN6nEFwI7jmxqBAY7hWhwjEHAozmXU-MVD-5spRsPUjzhyryy_oVlXSkkzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا فکر می‌کنید دستیابی به توافق با ایران همچنان ممکن است؟
🔴
املاکی هزار‌ پدر: بله، فکر می‌کنم توافق ممکن است
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://telegram.me/news_hut/68059" target="_blank">📅 02:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68058">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
ترامپ:  سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.  @News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://telegram.me/news_hut/68058" target="_blank">📅 02:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68057">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=Ni1Vztu2qH1OP51nBfgBncjSrSrpkwizjnU5nfHAxGxDtvZzyK8740N5MEfSZLQY37u-c94pr8F_H9SmGEccjoyhvrtm4QUxS5C-HovEvDHcr1jTgIi21ogsmb-lVoUfc5QTldeLyN6wYSjHTTR9GrrPIHv9_s2hN0DnbqXLKwFH11bk-SNmph__0Q4IcIA6AHCaSyZhK73bytrD7usGYR3nFfis821xkw7oNXVNjRZtlz05IlPMFhZz6odh9RMRF9m9fXG7RUcLxXHOknQyTioPlIcFqGxJKhu8Dw_M73GdEAYX8BtRyXhqmRU0nU8ntn8fPyJmbCbl38evVyBdgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbf86b6f2.mp4?token=Ni1Vztu2qH1OP51nBfgBncjSrSrpkwizjnU5nfHAxGxDtvZzyK8740N5MEfSZLQY37u-c94pr8F_H9SmGEccjoyhvrtm4QUxS5C-HovEvDHcr1jTgIi21ogsmb-lVoUfc5QTldeLyN6wYSjHTTR9GrrPIHv9_s2hN0DnbqXLKwFH11bk-SNmph__0Q4IcIA6AHCaSyZhK73bytrD7usGYR3nFfis821xkw7oNXVNjRZtlz05IlPMFhZz6odh9RMRF9m9fXG7RUcLxXHOknQyTioPlIcFqGxJKhu8Dw_M73GdEAYX8BtRyXhqmRU0nU8ntn8fPyJmbCbl38evVyBdgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ:
سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://telegram.me/news_hut/68057" target="_blank">📅 02:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68056">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
وزارت دفاع امارات متحده عربی:
دو نفتکش ملی به نام‌های "ممباسا" و "الباهیه" در آب‌های منطقه‌ای عمان، در بخش جنوبی تنگه هرمز، مورد هدف دو موشک ضدکشتی ایرانی قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://telegram.me/news_hut/68056" target="_blank">📅 02:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68055">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=KI0hjBaxtos2vh9KpbvImc5kso0Wmtq8RX04DedUp7pIsEBPLidMxzcp8Rzsq2B1I2rKoyJ75cSOJJkZI79zM6gw8xqPmHCc3af_RmmtskFbq-RUktw296lqOfgkuHD23ZYR-Bv5MaqhfhA9UieRfHHExrRzcD2HK_tCyxel-KKCHa-FVHCg3BcYvGHZ_RLdpc2C7XJzyY786aB1o1DlCAeNYbo6Z0CdG-JWbtGUB3_Yb740MX0K17npZhBFSyCWl2euzfqQ00lwDmxQ7srFvhWR9Ix4YbxqRJtXpmrJ2wHbKCuwdJWRE12gaMaYWERIxphJg8B91fF4kzJ2Gwt1Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f978bb3724.mp4?token=KI0hjBaxtos2vh9KpbvImc5kso0Wmtq8RX04DedUp7pIsEBPLidMxzcp8Rzsq2B1I2rKoyJ75cSOJJkZI79zM6gw8xqPmHCc3af_RmmtskFbq-RUktw296lqOfgkuHD23ZYR-Bv5MaqhfhA9UieRfHHExrRzcD2HK_tCyxel-KKCHa-FVHCg3BcYvGHZ_RLdpc2C7XJzyY786aB1o1DlCAeNYbo6Z0CdG-JWbtGUB3_Yb740MX0K17npZhBFSyCWl2euzfqQ00lwDmxQ7srFvhWR9Ix4YbxqRJtXpmrJ2wHbKCuwdJWRE12gaMaYWERIxphJg8B91fF4kzJ2Gwt1Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ: محاصره دریایی فقط مختص ایران است.
🔴
خبرنگار:
آیا می‌خواهید هزینه‌تان جبران شود؟
🔴
ترامپ:
بله. چون ما از بخش بسیار ثروتمندی از جهان محافظت می‌کنیم. قرار است هزینه محافظت ما جبران شود.
🔴
خبرنگار:
توسط چه کسی؟
🔴
ترامپ:
توسط کشورهایی که از آنها محافظت می‌کنیم. عربستان سعودی، امارات متحده عربی، قطر، کویت، بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://telegram.me/news_hut/68055" target="_blank">📅 02:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68054">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
خبرنگار: ماه هاست که ایران را بمباران می کنید.
🔴
ترامپ: ما 19 سال در ویتنام بودیم. ما چهار ماهه اینجاییم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://telegram.me/news_hut/68054" target="_blank">📅 02:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68053">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=SH6RKSK-XdEfJG80qyebauxTmPs6bii06f1Wmzm7X7zvMwyhC3eacq2Y7PJ2ZKg89LfcZhZ4-7g1cEuOr5uu7ecweRmGvFTBs_uqORvdLQZv1mDhKXI9jpl6Sn13RoyczM-Xp7IPvVrO8Jq22O6J1zLAgepLXYssyIL8Yli_isqNK5CqyQi8V0kcG68ZRvVccyzJQlRq9afpTbn-xs2zBh85R89074oXZ4esG154hbDK5c0WsYoPSU3YHKLWeYW6kAn4-XCFZhK86qekR8TuTGoC1sUOAMc22CtSf936ChiSbJqWPCC4GnFYvCdeGXpoQa9M2FYIPXY8gEUK1Mjfmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/438b08cd11.mp4?token=SH6RKSK-XdEfJG80qyebauxTmPs6bii06f1Wmzm7X7zvMwyhC3eacq2Y7PJ2ZKg89LfcZhZ4-7g1cEuOr5uu7ecweRmGvFTBs_uqORvdLQZv1mDhKXI9jpl6Sn13RoyczM-Xp7IPvVrO8Jq22O6J1zLAgepLXYssyIL8Yli_isqNK5CqyQi8V0kcG68ZRvVccyzJQlRq9afpTbn-xs2zBh85R89074oXZ4esG154hbDK5c0WsYoPSU3YHKLWeYW6kAn4-XCFZhK86qekR8TuTGoC1sUOAMc22CtSf936ChiSbJqWPCC4GnFYvCdeGXpoQa9M2FYIPXY8gEUK1Mjfmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما آنها را در موقعیتی داریم که هیچ نظامی ندارند. هیچ کاری نمی توانند در مورد آن انجام دهند.
تنها چیزی که آنها دارند اخبار جعلی است زیرا آنها اخبار جعلی را دارند و ترجیح می دهند ما در جنگ شکست بخوریم تا اینکه در جنگ پیروز شویم، که واقعاً به نوعی خیانت است.
ما امشب یک حمله بسیار بزرگ دیگر انجام می دهیم. آنها می خواهند معامله کنند. ما دو روز پیش معامله ای انجام دادیم و آنها می خواهند معامله کنند.
آنها 47 سال است که مذاکره می کنند، اما هیچ کس هرگز آنها را مورد حمله نظامی قرار نداده است. ما خیلی سخت به آنها ضربه می زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://telegram.me/news_hut/68053" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68052">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=QizN_6SIW903H8xa9ypKbMUu3qZYd8pOqVSvM_zG2RNm3cTqcR7CPHRfsiKwqA823O8y_9kpYHeG3Kpbrss1GdNosaKlOQpqjzu4wxBVvOoazI3JBatmUuSVooIehk4KNWmAY6wWjiVIYxpHGYcVKepbNt5aZboPiN1_qnzYswBudQkc6cAViuTI5BZZSneeo1Rij8rYof4lTko3BYgJVU4s9mc29N2cch4ayuXKyG7WNz66eP-rF64O6LZY4kY_G7r3A9KKi6oDbQvI6J22t2Qm2XjJ5Cm2m1dUnvgq-_x4CRx3nML56KaNkUwFlMxUWfw_P43dN9v_7fWmYowrjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0b220c65f.mp4?token=QizN_6SIW903H8xa9ypKbMUu3qZYd8pOqVSvM_zG2RNm3cTqcR7CPHRfsiKwqA823O8y_9kpYHeG3Kpbrss1GdNosaKlOQpqjzu4wxBVvOoazI3JBatmUuSVooIehk4KNWmAY6wWjiVIYxpHGYcVKepbNt5aZboPiN1_qnzYswBudQkc6cAViuTI5BZZSneeo1Rij8rYof4lTko3BYgJVU4s9mc29N2cch4ayuXKyG7WNz66eP-rF64O6LZY4kY_G7r3A9KKi6oDbQvI6J22t2Qm2XjJ5Cm2m1dUnvgq-_x4CRx3nML56KaNkUwFlMxUWfw_P43dN9v_7fWmYowrjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
چهار ماه پیش، این‌ها نیروی نظامی بسیار قدرتمندی داشتند؛ بی‌شک قوی‌ترین نیرو، احتمالاً در کل خاورمیانه. آن‌ها را «قلدر خاورمیانه» می‌نامیدند. اما حالا دیگر نیروی دریایی ندارند. ۱۵۹ فروند از کشتی‌هایشان به زیر آب رفته است. آن‌ها ۲۳۰ فروند هواپیما، یعنی هواپیمای تهاجمی، داشتند؛ که همگی از دست رفته‌اند. آن‌ها سیستم‌های راداری فوق‌العاده‌ای داشتند که همگی از بین رفته‌اند. پدافند هوایی بسیار قدرتمندی داشتند که آن هم از میان رفته است. متأسفانه، رهبری‌شان نیز از بین رفته است. رهبران رده‌اول و رده‌دوم همگی کشته شده‌اند. حتی برخی از رهبران رده‌سومشان ــ که کم‌وبیش با آن‌ها سروکار داریم ــ نیز از میان رفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://telegram.me/news_hut/68052" target="_blank">📅 01:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68051">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO81QOz9CEPRhb4J3MGEcWx9mu5KDzrtCavcrNTofF-x-pzcWQULlnag-vu26cxv17zMgzcSs1aRMNIE7mi62QQRs91UzjYorUcebTCfDR4x3dx6XdXP0RJ5U3yHEgwmWtxu6a8KvR9IKNBLPFmloHpvo_n89a6Xlg2ZzYPrzeERTI1-OYIOOpVIUbseWX31GUsBkLenlpF4vQTcIavz_5lHCMU5uxVs5-nwnEY6keZMPLnnLGVzJ6IqGvcw5YUt8Lyrlau6I91mtrkEXRtGRjTDcyBxKKTQJrn56V_j05xtLVy0Eg1SD7eLCQTiv9fXtLR7PIxmZtopSu8V746cfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرکز عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۴۰ مایل دریایی از منطقه قلهات در عمان هدف اصابت یک پرتابه قرار گرفته و این پرتابه به اتاق موتورخانه کشتی برخورد کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://telegram.me/news_hut/68051" target="_blank">📅 01:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68050">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=o2i7tPdnBBr8QHjI8SH4djKK3SSvrSY4hXx-5335dHdjGIgm8tnQE2W54rqNY-Zd793cMe-GXnGPqPU7eHc-pVuNj1J51L_YttcM5FH_kvfYssDv9HB04UCRq-C50TbkJglAHLqfWV4R_jParVroMA1jxGFhyXWHk3OoxGImJQzZGDe-HmcUCb16swe8iK2Qvyen2qWSO79lAVDzeD3NzR9n0xs1vDzUMgIZFFQYt3hLUPT1LEMofy8QV1p_0uD_9U-zqkZT72lyo_GaF5nW2GqDIhqUQS93TC9kErXH4ODt4tg7Z2tCtkboVcfLB455h8Hp9NHM-LZeZqdKlOlSsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53e6cb45ca.mp4?token=o2i7tPdnBBr8QHjI8SH4djKK3SSvrSY4hXx-5335dHdjGIgm8tnQE2W54rqNY-Zd793cMe-GXnGPqPU7eHc-pVuNj1J51L_YttcM5FH_kvfYssDv9HB04UCRq-C50TbkJglAHLqfWV4R_jParVroMA1jxGFhyXWHk3OoxGImJQzZGDe-HmcUCb16swe8iK2Qvyen2qWSO79lAVDzeD3NzR9n0xs1vDzUMgIZFFQYt3hLUPT1LEMofy8QV1p_0uD_9U-zqkZT72lyo_GaF5nW2GqDIhqUQS93TC9kErXH4ODt4tg7Z2tCtkboVcfLB455h8Hp9NHM-LZeZqdKlOlSsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
همان‌طور که می‌دانید، امشب ضربات سنگینی به آن‌ها وارد می‌کنیم.
ما حجم عظیمی از مهمات در اختیار داریم؛ موجودی ما در سطحی است که سال‌ها نظیر آن را نداشته‌ایم. ما ضربات بسیار سختی به آن‌ها می‌زنیم؛
این روند ادامه خواهد یافت و در نهایت خواهیم دید چه میشود.
ما در حال نابود کردن تمام توان تهاجمی آن‌ها و در کنترل گرفتن تنگه‌ها هستیم.
ما دوباره سیاست محاصره را اعمال می‌کنیم. شاید محاصره مؤثرتر از حملات مستقیم باشد، اما به گمانم ترکیبی از این دو روش است که واقعاً کارساز خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://telegram.me/news_hut/68050" target="_blank">📅 01:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68049">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=gIKa8IjVBJPKqTiJAO5P5VFmodtx23qVamLmU7mgU6vefMPWkk62fJugkWjXrHSymO6W538M8JP2ndy8udE4jQMvJzEvv1F5HgKpA8kQAusdNuoe9IZpW8-GU35jZ-Z4Ver8PB2F7tvn0Ta15wp9b1jUHcOEzx7Y_9Caq_hswNk6WPabc1e-rT5mrBvcnta_9ZhPfjp-5VWG4eTxLKqOYpaPTfXR594KD8uGyGo7vDRy4JIt5-E60lHoRQKaHnYUxjxRBKxRV_B_2u_b35NgaELrlo_w6O9rL7b84jazWusDUF-tRDVJbxwvY6mswrLxi3n-hhxJqAuHG7nyAXqEGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad5518ef1d.mp4?token=gIKa8IjVBJPKqTiJAO5P5VFmodtx23qVamLmU7mgU6vefMPWkk62fJugkWjXrHSymO6W538M8JP2ndy8udE4jQMvJzEvv1F5HgKpA8kQAusdNuoe9IZpW8-GU35jZ-Z4Ver8PB2F7tvn0Ta15wp9b1jUHcOEzx7Y_9Caq_hswNk6WPabc1e-rT5mrBvcnta_9ZhPfjp-5VWG4eTxLKqOYpaPTfXR594KD8uGyGo7vDRy4JIt5-E60lHoRQKaHnYUxjxRBKxRV_B_2u_b35NgaELrlo_w6O9rL7b84jazWusDUF-tRDVJbxwvY6mswrLxi3n-hhxJqAuHG7nyAXqEGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ما ارتش آن‌ها را درهم کوبیده‌ایم. ضربات بسیار سختی به آن‌ها وارد می‌کنیم.
ما همین دیروز یا پریروز توافقی داشتیم. کار تمام شده بود، اما آن‌ها بلافاصله توافق را برهم زدند، چون متوجه شدند نکته‌ای در آن وجود دارد که باب میلشان نیست.
طرز فکر و رفتار آن‌ها متفاوت است و ما چنین چیزی را تحمل نخواهیم کرد. ما فقط به پیش می‌رویم.
ما امشب به آن‌ها حمله می‌کنیم. ما تمام توانمندی‌هایشان را در هر زمینه‌ای که به تنگه هرمز مربوط می‌شود، از بین می‌بریم.
گمان می‌کنم در نهایت، کنترل کامل آنجا را در دست خواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://telegram.me/news_hut/68049" target="_blank">📅 01:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68047">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h4_IXhvc3_4HuuWPDAde5e28HN9qHRpN2JLg94CDoTb3jVrWLBMK_ikRZ185iZFitOS9Q6727laRRg91iHNdKi6xRmNJ_jgI9pZl8kHKp_7z6bgOy2wn_sZUMJVWY0bijGoG0H6ZGcxaq6vtw5C_A-0HXQ4GgNZ3oFmQr7jdphmJl0h2Ocy2rZen3wXhROj4tl_fbc4nLoBzGsO_nZ1S9bsIlavwJCYIxD8CJ32PdHmK9_woe-sA1cWYZV0et5bw2ihqsIDu0zaGmsw96mWD6pMTMYkKjPprKo5uXakbjVH3jSvzU4iDdk5KbxvQRhwzYq-s_2-9eH1YoQNzeix_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/StTMqr-vrBq713fG8v6vQbmb3Ni-E7mQrSRNMipK1uAL1ySPnaMb0s0gpvMNilxfKuBY6XEwb1ATjDaXG9hTF6fAw5tSRPQ2qfaYDfsw0ueTLsCft6fBJ688u9tT17wGWb1t1E78WhXQRd3ZKMhLDYIBpadyX6p2ik2xSwo9TDpP2G7mhFe9-NsVhlVKk1nzLZIWy_CSYkkPcR4W0Fy-MoHTxoZM6JYgH4a_mE5_rJ-jhgwP50TxFOXfcImXd6-pKLkbAoPbEWwh2-eU000UtdyS3UIZxpbybM3DrRHmRpq8GHAm6sg73ZYjDNmp-W3Jb9YTQjYxjxsYr0p00WHwog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویری دیگر از حملات آمریکا به جزیره کیش
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://telegram.me/news_hut/68047" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68046">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد  @News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://telegram.me/news_hut/68046" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68045">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع چندین انفجار در  کیش
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://telegram.me/news_hut/68045" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68044">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezhj9TNbPgKL8P7Y30pZxdy2cKs5gGIUNQItLXu2u84iGUv3Wmg_c5HwSWVKLtS-e5XYn8fRFkbN_OzuxDrSUtWrVaIxwfY98aC629Ago8BIAQ2HjjpSTL5v_ZHD_kf33OjQjzsMcd0o9TfF6aIPqSvzphsDt8dOx96BOsxEIZvdmO6s9x7TCb_z4b2Dcdz1xMUc2hf8Z1vkUo4uJVIqTN5FhgdQ_ZAkhgaO8oprsxKMgyQA4J3L8hZ6-cBd49b0yHhxS7k1qZmpeSUfrPPma8L00FG4YHA_20JGj0PhEU9z_GaKGQTSjaBDg7m5Bp7Bd0JZ9usbPsS19SZiHRfR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://telegram.me/news_hut/68044" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68043">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMrSm_-84_s79nMda8Vc3TdbJG--wj59hBh-QM8Xdwhttq9rkzw7Ncf_KgZZSb8rbijNO_hSGFKWiQmkcUiKQM59v7uCprCZm5r4KfpAK5PUPCpVkKNH8QyYbt4V5yUScukog6T-lWIS0olnX1imv9XWVJUFdvDJ-wxMsmkOjVL9JrWW5O1KZkSJ-9K4NGZ49T2mZDQmUMIobgcWBL2w7eq6crpXfMxsy5emF2oMsXhcrAssd4Vr7EOIFYSkyzVwYAYxMFrVJD0p7gdbIv4EAGQDbhByuHyTI822AbMDz7Tqu0dGeXhA0wIGMGpj1ws8IzrNVXz8ho1QDWxTgUIgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://telegram.me/news_hut/68043" target="_blank">📅 00:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68042">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a423066bec.mp4?token=oDkFSy1XPQpCXsAJ481Tv1JeI7HgtLAe1-48MJnpKFevzhe5jA8HPkTjnvaNui8L2GFs98ArL8LttfwiEda9fDz-UP95eBeSrDDXXe8nQi-1jTA3SszPH_tNQDK6OBHCvRvmW8ky51_b8EV2zvkFjdNbkafHGcVwcpTZrs4NdrmPXKzscrGN0N_dLNQLpzdeLOZQ64Ds7ukDh9XaKviSvE_8dguqYbQgugIyaFbi2bo77gp46-TEVnsAdoT9kIu432v9Xjt9UBs_d5Xr90vJQqma_R6kjc1GDKyrItK014m29cRw9g2N7tB7B_5--VSwnCa6e5xwkDn73HZzx7y3Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a423066bec.mp4?token=oDkFSy1XPQpCXsAJ481Tv1JeI7HgtLAe1-48MJnpKFevzhe5jA8HPkTjnvaNui8L2GFs98ArL8LttfwiEda9fDz-UP95eBeSrDDXXe8nQi-1jTA3SszPH_tNQDK6OBHCvRvmW8ky51_b8EV2zvkFjdNbkafHGcVwcpTZrs4NdrmPXKzscrGN0N_dLNQLpzdeLOZQ64Ds7ukDh9XaKviSvE_8dguqYbQgugIyaFbi2bo77gp46-TEVnsAdoT9kIu432v9Xjt9UBs_d5Xr90vJQqma_R6kjc1GDKyrItK014m29cRw9g2N7tB7B_5--VSwnCa6e5xwkDn73HZzx7y3Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
منتسب به سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://telegram.me/news_hut/68042" target="_blank">📅 00:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68041">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
انفجار ها در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://telegram.me/news_hut/68041" target="_blank">📅 00:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68040">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
تپه الله اکبر زدن بندرعباس ایستگاه رادیویی
گزارش ممبرای چنل
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://telegram.me/news_hut/68040" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68039">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
چندین انفجار در کیش
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://telegram.me/news_hut/68039" target="_blank">📅 00:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68038">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://telegram.me/news_hut/68038" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68037">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/symJ5oL0cwo5qZVe5fTS2xAu2u0AbGJo4dnnRThG9I5qAMRdOVya2U7harXI7p82vdQ3qtYOb51so-4h0hnUGs8PfEVcivFksfVDQidq5vxIBuyWR7qWUkZ4xHI3Tz7PMvdka_5u3NMDP6-G45CAAKxGrEQnsv0kKx6HTJtAr7Okcs0w3FBnh2uJ3o4r2rFh6NNejxH5IFhyEb_Ci1qjDuJuSelV-93wzP54J3jWl6rglP7SiGItNgEHKtDr78KUrfXqWmpZ8CIJBeT7VOh4PGFLUPXOEUXA4Ki69IRJE7qkXyyy2z-630qmobE5wPh_0iPgxfSj7cipd8TsxFeEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
امروز ساعت ۴:۴۵ بعدازظهر به وقت شرقی، فرماندهی مرکزی ایالات متحده به دستور فرمانده کل، سومین شبِ پیاپی حملات علیه ایران را آغاز کرد. این حملات همچنان هزینه‌های سنگینی را بر نیروهای ایرانی تحمیل کرده و توانایی آن‌ها را برای حمله به غیرنظامیان بی‌گناه و کشتی‌های تجاری در تنگه هرمز تضعیف خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://telegram.me/news_hut/68037" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68036">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های اولیه از وقوع دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://telegram.me/news_hut/68036" target="_blank">📅 00:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68035">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a4e2ce60.mp4?token=KN4Jfu2nLkDNrC87zX9r3yGIPihEKpCA2HbX0U1_Dv-gw4EKadSe-k5g0iMjceSGSg0TTAWW4Hyo989ZOqJcNApMN831swVzC582G7LjXdjDo08KrTUOSKMNbMPOCk3rJ2Bz3Bq7oL8Saxt1EEPjNqeNzbT-nOgNme1ebotvgnyq6dLz9Q6NoqmYrOI3TvDjMe7BOuUGYiodo_r63vw9nkZ_mik09OS9FR-QuWvyiJsGqHA63i4zSrJcHI5tnh-52QGCLvPZO-HLwIqgpbJNCyO8JmSzpP7vU6xMjCVcHQJdp3aplTgpD9uEMZvAnPnImYIoGC948t_rYxVJKuP6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a4e2ce60.mp4?token=KN4Jfu2nLkDNrC87zX9r3yGIPihEKpCA2HbX0U1_Dv-gw4EKadSe-k5g0iMjceSGSg0TTAWW4Hyo989ZOqJcNApMN831swVzC582G7LjXdjDo08KrTUOSKMNbMPOCk3rJ2Bz3Bq7oL8Saxt1EEPjNqeNzbT-nOgNme1ebotvgnyq6dLz9Q6NoqmYrOI3TvDjMe7BOuUGYiodo_r63vw9nkZ_mik09OS9FR-QuWvyiJsGqHA63i4zSrJcHI5tnh-52QGCLvPZO-HLwIqgpbJNCyO8JmSzpP7vU6xMjCVcHQJdp3aplTgpD9uEMZvAnPnImYIoGC948t_rYxVJKuP6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ :
«کوه پیکَکس رو از بین می‌بریم.
به ایرانی‌ها بگید که داریم میایم.
و هیچ کاری هم از دستشون برنمیاد!»
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://telegram.me/news_hut/68035" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68034">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5e2a3c36.mp4?token=O82iTTZVGoe1a6bHC9bMxfBqwndW7kXzStWPIG22g0IVH48KG6xsP7B7G3zXmSahjuNhpOnhjKT9yJf9GInadA22VSYVWTZl0ADDizz2De4PMjLnu4MB7L4o4NUJJyyT5du2geXmBJFfT53M3iGP2rN6M-IYiyufvH3eLCBpdfxYNKByyyyneQapNEspEH80oLKXIajtMU1Yw5lQ2ifNJ56XZzzos_p9Ba-8Y-LpbXhu6gRRx6Jt5fQ-Cyx0vOzUyJLp67KexyJb8LyG2YZ6rgSYvqyBUeO0oUNNNK-FD_iwaAToKrJJKimLAWz0DWko8kOUJG8wS-IMYnnZGEuzNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5e2a3c36.mp4?token=O82iTTZVGoe1a6bHC9bMxfBqwndW7kXzStWPIG22g0IVH48KG6xsP7B7G3zXmSahjuNhpOnhjKT9yJf9GInadA22VSYVWTZl0ADDizz2De4PMjLnu4MB7L4o4NUJJyyT5du2geXmBJFfT53M3iGP2rN6M-IYiyufvH3eLCBpdfxYNKByyyyneQapNEspEH80oLKXIajtMU1Yw5lQ2ifNJ56XZzzos_p9Ba-8Y-LpbXhu6gRRx6Jt5fQ-Cyx0vOzUyJLp67KexyJb8LyG2YZ6rgSYvqyBUeO0oUNNNK-FD_iwaAToKrJJKimLAWz0DWko8kOUJG8wS-IMYnnZGEuzNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره صالح محمدی کشتی گیر اعدام شده :
«اون کشتی‌گیر یکی از بهترین کشتی‌گیرهای دنیا بود.
فقط به خاطر اینکه درباره حکومت حرف زده بود، اون و دو تا از دوستاش رو کشتن؛ حتی حرف خیلی تندی هم نزده بود.»
این ادم ها خیلی وحشی ان!
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://telegram.me/news_hut/68034" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68033">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
خبرنگار:
«آیا تفاهم‌نامه‌ای که تیم مذاکره‌کننده شما از ایران آورد، از همون اول قرار بود شکست بخوره؟»
🔴
ترامپ:
«نه، اون برای آزمایش بود؛ یه تست بود. نمی‌دونستیم نتیجه چی می‌شه.
ببینید، وقتی با یه مشت آدم حقه‌باز طرف هستید، تفاهم‌نامه ارزش زیادی نداره.
البته حتی با آدم‌های قابل اعتماد هم تفاهم‌نامه خیلی ارزش حقوقی خاصی نداره؛ چون فقط یه تفاهم‌نامه‌ست.
من هم گفتم اصلاً چرا باید اول تفاهم‌نامه امضا کنیم؟ توی آمریکا معمولاً اول تفاهم‌نامه امضا می‌کنن و بعد میرن سراغ توافق نهایی.
من گفتم از همون اول برید سراغ خودِ توافق.
ولی در نهایت، اون تفاهم‌نامه یه جور آزمون بود و اونا توی این آزمون موفق نشدن؛ به تعهدشون عمل نکردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://telegram.me/news_hut/68033" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68032">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره هدف قرار دادن مقام‌های باقی‌مانده حکومت ایران:
«ما قطعاً اون‌ها رو زیر نظر داریم. آره، اطلاعات زیادی درباره این موضوع دارم، خیلی هم می‌دونم، اما فکر نمی‌کنم الان زمان مناسبی باشه که درباره‌ش حرف بزنم.
باید ببینیم چی پیش میاد. مثلاً امشب حسابی بهشون ضربه می‌زنیم و فردا هم همین‌طور. هیچ کاری هم از دستشون برنمیاد.
اونا هیچ چیزی ندارن؛ تنها کاری که بلدن اینه که لاف بزنن. و فکر می‌کنم کاری که من انجام دادم، کار خیلی درستی بود، چون باعث شد بیشتر باهاشون آشنا بشم...»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://telegram.me/news_hut/68032" target="_blank">📅 00:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68031">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbfd8c6550.mp4?token=GuwbvC2QEfvCodsgzjToage_LYRGctCgzHUhzuczT93hc32-QkBWWXSvbWC_m6exLgEQBQGFQbO1xr4oahlJM6557Mr-LbPtTf9FhDMzELc0DLR2RDhEdfCvoXD7GiGc3e6VlD_146GvxOa591VJiJe-k1Nk1resvkQfHFO5PNrkBu3zEGop65QvjwAJ-UI6Ij5RRxltxdGyCbKML80UXkV5T032oTKgysOErFc9QfVvJoJdxH0f08pOEF2OKMCjF0j4cVH0F955goJE2sjjxZsBlJ7sxPox6uA-DMjpaP003nza_UJ-WqsDLx2zSLu3mVtGDXS7glRzIcKHYCKYnWViaB8WYAeWNx_wQN5mEmxm9DTmBVpbM8SKdhE_by6EQ0R2MBG1clYR5eZLidZTOW4tfzpHjJ9Kpcl1yMEvKUXErQKHJc2fa6USUFz696c9X25VP-b3f04qzgZ_h6h0tVwGJySuPxyUbap_gJzkdXm6T2DX6qzT--fSSWDJ9gUlhiAwsXQuK80ht9_0V8bSpku72fVaPwPwzEj1C3g_FLEEKFG-rjc_Oxbi_UHVA5SK_Fk58ij_PgdlY3wXRVp9hbNtSoaUMYlHest2RMWSwMZ2GWlzHx3GkaW6nZCwDhfUwvlxtXDB4CmIl8oK6XCgOYT713e4Nlf5CzIGARTc3ak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbfd8c6550.mp4?token=GuwbvC2QEfvCodsgzjToage_LYRGctCgzHUhzuczT93hc32-QkBWWXSvbWC_m6exLgEQBQGFQbO1xr4oahlJM6557Mr-LbPtTf9FhDMzELc0DLR2RDhEdfCvoXD7GiGc3e6VlD_146GvxOa591VJiJe-k1Nk1resvkQfHFO5PNrkBu3zEGop65QvjwAJ-UI6Ij5RRxltxdGyCbKML80UXkV5T032oTKgysOErFc9QfVvJoJdxH0f08pOEF2OKMCjF0j4cVH0F955goJE2sjjxZsBlJ7sxPox6uA-DMjpaP003nza_UJ-WqsDLx2zSLu3mVtGDXS7glRzIcKHYCKYnWViaB8WYAeWNx_wQN5mEmxm9DTmBVpbM8SKdhE_by6EQ0R2MBG1clYR5eZLidZTOW4tfzpHjJ9Kpcl1yMEvKUXErQKHJc2fa6USUFz696c9X25VP-b3f04qzgZ_h6h0tVwGJySuPxyUbap_gJzkdXm6T2DX6qzT--fSSWDJ9gUlhiAwsXQuK80ht9_0V8bSpku72fVaPwPwzEj1C3g_FLEEKFG-rjc_Oxbi_UHVA5SK_Fk58ij_PgdlY3wXRVp9hbNtSoaUMYlHest2RMWSwMZ2GWlzHx3GkaW6nZCwDhfUwvlxtXDB4CmIl8oK6XCgOYT713e4Nlf5CzIGARTc3ak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت
ترامپ:
«به نظرم اینا یه کم دیوونه‌ان؛ در واقع فکر می‌کنم همشون همین‌طورن.
اول رژیم اولشون رو از بین بردیم، بعد رژیم دومشون رو زدیم و بعد هم حدود ۲۵ درصد از این رژیم رو نابود کردیم. اینا طرز فکر متفاوتی دارن.
دیروز به یه توافق رسیده بودیم؛ تقریباً همه‌چیز ۱۰۰ درصد نهایی شده بود. اما یه دفعه یه تماس تلفنی گرفتن و همشون از اتاق بیرون رفتن.
این آدم‌ها واقعاً دیوونه‌ان. ما به توافقی رسیده بودیم که همه‌چیز به نفع ما بود، اما اونا دوباره زیرش زدن. از نظر اونا، توافق برای اینه که بعداً نقضش کنن.
اصلاً نمی‌شه بهشون اعتماد کرد و راستش رو بخواید، اگه یه روز به سلاح هسته‌ای دست پیدا کنن، ظرف یک روز ازش استفاده می‌کنن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://telegram.me/news_hut/68031" target="_blank">📅 00:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68030">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
خبرنگار:
«
آیا شما یا ارتش آمریکا، یا حتی ارتش اسرائیل، می‌تونید به فرمانده‌های رده سوم، چهارم و پنجم ایران برسید؟ می‌دونید کجا هستن؟ می‌تونید اون‌ها رو از بین ببرید؟»
🔴
ترامپ:
«آره، می‌دونم. ولی نمی‌خوایم درباره اون صحبت کنیم. البته که زیر نظرشون داریم.
من اطلاعات زیادی درباره این موضوع دارم، اما فکر نمی‌کنم الان زمان مناسبی برای حرف زدن درباره‌ش باشه.
ولی... امشب حسابی بهشون ضربه می‌زنیم و فردا هم همین‌طور. هیچ کاری هم از دستشون برنمیاد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://telegram.me/news_hut/68030" target="_blank">📅 00:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68029">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
تاسیسات اتمی  خاصی در منطقه کوهستانی موسوم به " کوه کلنگ " در جنوب نطنز قرار‌ دارد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://telegram.me/news_hut/68029" target="_blank">📅 00:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68028">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ccfca9a7.mp4?token=nIiNUKcLEHlcbNe32aeKfqEAYqcrn_nH0QedsXonIWfAwYluzGWPvIG7wy8YhGvr7Psv27Pmi1QX_l27SjhfEmzWaIsnjgNbw2adyw21qjI16wMXNp-H57cerzETNkqfKwdo3gMgk0EpIeTPggxNNjnQ8UpUpE_UEI69Ou_FpgoGk7ze8GgUXUHFnE1Gaq2pVwdkRroy3S2tSdCL3Hcqkrqpl8kP2UK1gmSYUOjSVz5KfSG8d51Y4U6sQiHFhppJ50hbanCB62X_QqrLYU2OPkDILjE114eMLxtXyHItsOuq7dYrIXOGMzRqF_5__XY7b5atbEmH68X3AbHi-XtDzlN-tZcuzHA92boZPCz5E1Gf4jI-Myq8r-FNbQ2SgnyJkK6-To4e89OxrzEEGFuDsK4wEpkXEP8z9qDull60LnOJ_CxyHOaQFft8y51bPeXNSJ2r_2ioFJLc3tGUboWabDn0z3_nazDI4y3Y--cEiKJe5bZLjlfgzQzmkujK8MMLPS6IJjQStGKoZAvaSBj3Ya8HQiK1e5TU2D8FcGIpHmDzhZTtENUkB5eJ2FPRUb-aoczfWfVU2wNabfPxV8yUipHccVxr7JqKaUeaRjQ8ee_5klT-eVp6N5XzZbHijWevePtBdpDPURGoD9YBEtuALorhKK_93ghixoM87zeCBPE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ccfca9a7.mp4?token=nIiNUKcLEHlcbNe32aeKfqEAYqcrn_nH0QedsXonIWfAwYluzGWPvIG7wy8YhGvr7Psv27Pmi1QX_l27SjhfEmzWaIsnjgNbw2adyw21qjI16wMXNp-H57cerzETNkqfKwdo3gMgk0EpIeTPggxNNjnQ8UpUpE_UEI69Ou_FpgoGk7ze8GgUXUHFnE1Gaq2pVwdkRroy3S2tSdCL3Hcqkrqpl8kP2UK1gmSYUOjSVz5KfSG8d51Y4U6sQiHFhppJ50hbanCB62X_QqrLYU2OPkDILjE114eMLxtXyHItsOuq7dYrIXOGMzRqF_5__XY7b5atbEmH68X3AbHi-XtDzlN-tZcuzHA92boZPCz5E1Gf4jI-Myq8r-FNbQ2SgnyJkK6-To4e89OxrzEEGFuDsK4wEpkXEP8z9qDull60LnOJ_CxyHOaQFft8y51bPeXNSJ2r_2ioFJLc3tGUboWabDn0z3_nazDI4y3Y--cEiKJe5bZLjlfgzQzmkujK8MMLPS6IJjQStGKoZAvaSBj3Ya8HQiK1e5TU2D8FcGIpHmDzhZTtENUkB5eJ2FPRUb-aoczfWfVU2wNabfPxV8yUipHccVxr7JqKaUeaRjQ8ee_5klT-eVp6N5XzZbHijWevePtBdpDPURGoD9YBEtuALorhKK_93ghixoM87zeCBPE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«آیا الان وقتشه که مردم ایران دوباره به خیابون‌ها بیان؟»
🔴
ترامپ:
«نه، اونا نمی‌تونن این کار رو بکنن. چون سلاحی ندارن و فعلا وقت قیام نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://telegram.me/news_hut/68028" target="_blank">📅 00:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68027">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c72608b58f.mp4?token=JhlN46WqVPIgQcesps-_VRMqJabdvg4dDP-4EN06Zwqo3Nkbp_k-V8KEw-DuZIPBCvp95EEfj0XlvDotcYGBmNNKPhPLkbvtqTI7riGU4YuoIelDJkOD8JMpX91rrdWE8lOwrEAOgXCa7ge1HnuWHbzZ6ynwGVN6vcQg_CSOP1JOYcI1HJ-eoJk0GNxTqA0G7VY_msTSwetquTBz2Yue6PZj5FuHMaj1cdaznbEsVJbOqzDDCZp2zMJwDT2BGVwXxj2FxNCkzfxs1_ucqJ4UBLF3g93BlBLA_wyzicLsG5NcqB7OW7MCsUE3z_-pA6u722t1s-cHJDPw6OW3n8NIuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c72608b58f.mp4?token=JhlN46WqVPIgQcesps-_VRMqJabdvg4dDP-4EN06Zwqo3Nkbp_k-V8KEw-DuZIPBCvp95EEfj0XlvDotcYGBmNNKPhPLkbvtqTI7riGU4YuoIelDJkOD8JMpX91rrdWE8lOwrEAOgXCa7ge1HnuWHbzZ6ynwGVN6vcQg_CSOP1JOYcI1HJ-eoJk0GNxTqA0G7VY_msTSwetquTBz2Yue6PZj5FuHMaj1cdaznbEsVJbOqzDDCZp2zMJwDT2BGVwXxj2FxNCkzfxs1_ucqJ4UBLF3g93BlBLA_wyzicLsG5NcqB7OW7MCsUE3z_-pA6u722t1s-cHJDPw6OW3n8NIuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند تا از حامیان حکومت توی آلمان تجمع کرده بودن که یکی از مخالفان حکومت اینطوری یکیشون رو سورپرایز کرد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://telegram.me/news_hut/68027" target="_blank">📅 00:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68026">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf3b137e2a.mp4?token=uMUEdUtcrfmEIORC02UpRgyCnTJLE_SPe_BZfLLIHcVyp_UCaRoaWX8zZPJn4PaDrLw5KOJbIRGp_3H7E--b54Mpp8lHwYwKMuK5W_WtvAOfpm_Ut93NGmFVNH_VWFJzW5ObRjMwXRenNfpZaGEE3NnKOYxiqke4WL-hkF7qOZ8A4XrLAzyiNJjcr5h1IgGFn3Npl4smfc1PehGeg6Lm3UnIkFDgRS8yuyqF4ZIb5AWymXzuMGuJiFDWS2PS5vJZBSXHxnInK2UEtXxxyXRqE1ECH82kB0kblJ1CXj4M7TTkFTpR42rwC40xiAM1Bn0qGQd0zkUx_4abb0RxLJ6I5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf3b137e2a.mp4?token=uMUEdUtcrfmEIORC02UpRgyCnTJLE_SPe_BZfLLIHcVyp_UCaRoaWX8zZPJn4PaDrLw5KOJbIRGp_3H7E--b54Mpp8lHwYwKMuK5W_WtvAOfpm_Ut93NGmFVNH_VWFJzW5ObRjMwXRenNfpZaGEE3NnKOYxiqke4WL-hkF7qOZ8A4XrLAzyiNJjcr5h1IgGFn3Npl4smfc1PehGeg6Lm3UnIkFDgRS8yuyqF4ZIb5AWymXzuMGuJiFDWS2PS5vJZBSXHxnInK2UEtXxxyXRqE1ECH82kB0kblJ1CXj4M7TTkFTpR42rwC40xiAM1Bn0qGQd0zkUx_4abb0RxLJ6I5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ خطاب به مردم ایران:
«کشور ما می‌خواد به شما کمک کنه و دوست داریم همه‌چیز به‌خوبی حل‌وفصل بشه.
افرادی رو داریم که آماده، مشتاق و توانمند هستن، اما اول باید بدونن شما خودتون چه تصمیمی می‌خواید بگیرید؛
این انتخاب با خود شماست.
ممنونم و خدا نگهدار ایران باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://telegram.me/news_hut/68026" target="_blank">📅 00:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68024">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یکم بالاترو نشونه بگیر املاکیِ پدراشتراکی، بیچاره جنوبیا خسته شدن #hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://telegram.me/news_hut/68024" target="_blank">📅 23:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68022">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:   امشب و فردا با قدرت به ایران ضربه خواهیم زد  @News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://telegram.me/news_hut/68022" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68021">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
یاداشت تفاهم با ایران یک آزمایش بود و آنها به آن پایبند نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://telegram.me/news_hut/68021" target="_blank">📅 23:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68020">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
امشب و فردا با قدرت به ایران ضربه خواهیم زد
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://telegram.me/news_hut/68020" target="_blank">📅 23:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68019">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
صحبت های امروز ترامپ با زیرنویس فارسی
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://telegram.me/news_hut/68019" target="_blank">📅 23:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68018">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
تسنیم:
چند کشتی متخلف در تنگه هرمز هدف قرار گرفته شدند
.
منابع محلی از هدف قرار دادن چند کشتی متخلف در تنگه هرمز خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://telegram.me/news_hut/68018" target="_blank">📅 22:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68017">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c2989693.mp4?token=WrJ3I0Q-UtDISaZgZWIHrJmBc9DiaM923JPFzVSyUSaAlRg3zTsR9Uj_g8mXyxCWyETluzgvhgvKJZnb36B8J6IljD68oi01qkp9hjNCtHumUETzCNiLQWRO7LtTvp6zmv8wrKj83iJaAm0HeTAdGaqZCOCvlaIwxdmlEU24g3aKFU51RoWo1cZlGJX5N0LABRv_nlNmwNrJNpY5Y0vLCsErrtKypU_eotLUMIfdPSAh0gRAJ4b8eXFWlq88CeHU9UoVgkDuCCzcx4868qcMlOefRJSvw02c4jWFedLIsPOFFX-1iTfESoqpgeBVtxPXVsDiHCNKcTXp32kxPwRZYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c2989693.mp4?token=WrJ3I0Q-UtDISaZgZWIHrJmBc9DiaM923JPFzVSyUSaAlRg3zTsR9Uj_g8mXyxCWyETluzgvhgvKJZnb36B8J6IljD68oi01qkp9hjNCtHumUETzCNiLQWRO7LtTvp6zmv8wrKj83iJaAm0HeTAdGaqZCOCvlaIwxdmlEU24g3aKFU51RoWo1cZlGJX5N0LABRv_nlNmwNrJNpY5Y0vLCsErrtKypU_eotLUMIfdPSAh0gRAJ4b8eXFWlq88CeHU9UoVgkDuCCzcx4868qcMlOefRJSvw02c4jWFedLIsPOFFX-1iTfESoqpgeBVtxPXVsDiHCNKcTXp32kxPwRZYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
انفجارهایی در شهر کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://telegram.me/news_hut/68017" target="_blank">📅 22:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68016">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
بیرجند، چابهار و سایت موشکی لار لحظاتی قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://telegram.me/news_hut/68016" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68015">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNOWRincBDVbu4o6SEZtiSkfd-DQJz8_jjhlk3zpApjXO9rGZFE2LvEGpWi-jMK77iqPXWL9fyF-5_Ws9tpk9ajooRd20curRObhbLVZ-Nn1fgM_-XGGJIcC-j_paTwTambIgeqQ-cRI7uG7JmPPyuLUOz1i-RsAe2yDLe5oSsifzIWFNBeiwU_qyHOmKcW8MfuSI1ADBsMRB_0vFWac0FiK6F-38-qb6lpocIrmz7QIvrYiKuc4aiQmbMRyiPUBrc8IrQizmV1Sp0eCXNGw2MxTGMPP3D9nDVR4hsaFwJtqNYyTqBjOjtKatih0I-6eJaKBsEmPs9SjYGQ6ihzegw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:
رئیس جمهور ترامپ پنجشنبه شب، ساعت 9 شب به وقت شرقی، خطاب به ملت سخنرانی خواهد کرد.
از توجه شما به این موضوع متشکرم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://telegram.me/news_hut/68015" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68014">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1_HqaCn83Tjljnov1yc6SZV4do-fGiD2pCHLTT-ol-j6jmDQ_fzrm95GajCLmDOjCbOS2rEv5z3KpKNo31RrpRWO3hUUHMK6q2gphYPlegO_P5WMhUN4rJxSR4dO68_Atu3eH0GxY8sOFfPjIWb0bMsgWN4G7Uih9gSZ5OoOvwnlOtrza2_YRawxKhNHjO5iCTJqApKlrZFTbfjOHrgFJgza6xaujVZ3NDr4ml92BDz_NmWad66zeu1TznCxOvGoeZdDCdLiUXzCYfFm3dN0yp6YgWJKq1UOqRzqSaoO8mcv-YvTmnihADRJYM3APP6djQ-oKc1lr3FlWLk6tem_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عباس عراقچی، وزیر خارجه جمهوری اسلامی:
رئیس‌جمهور آمریکا کاملاً حق دارد. هر کسی که عبور امن و ایمن کشتی‌های تجاری از تنگه هرمز را تأمین کند، باید بابت این خدمت پاداش دریافت کند. ایران همواره «نگهبان» این تنگه بوده و «برای همیشه» چنین خواهد ماند. البته ۲۰ درصد رقم بسیار بالایی است؛ ما منصفانه عمل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://telegram.me/news_hut/68014" target="_blank">📅 22:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68013">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار سنگین در بندرعباس و کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://telegram.me/news_hut/68013" target="_blank">📅 22:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68012">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoM6kpAlG-b8EOhLJAhDuqwS_4XDW9nvT1dGedY-nDm2CdWk3B5ddMA8TTe38owySvve8BPE97hkdXJra_LgONIY8xUTQOrOaf3_BtmgQKfVzcr7DxPbFr3zRl4h7qXElwS0hY5ie8SMYGmjARmtMXl1rlNx2V-HYpjaDZ4WUu3H5umYiqP80Dk8m5HfCwUnEVot1D7_-Y-zLqH8S9zgLZ8QxXjsJLarCd9oHYCQyoAGtycRY-Tot5Ad5KlsLoJs47lHcBjINzx7-71ONCQ1mcvl4jaYiXPPkgjAdkEIB3j9lt_Ay4pJ-HX5p2kOiTsyQz0DQr2rqXxg2OvFY3dfgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
فووووری؛ نیویورک تایمز: ترامپ به کنگره رسما اطلاع داده که درگیری با ایران از سر گرفته شده
آمریکا و ایران بار دیگر به لبه جنگ نزدیک می‌شوند. ترامپ اعلام کرد که امریکا، محاصره دریایی بنادر ایران را از سر گرفته و قصد دارد 20 درصد مالیات بر کالاهایی که از تنگه هرمز عبور می‌کنند، وضع کند.
پس از یک شب دیگر از حملات، به نظر می‌رسد که آمریکا و ایران به درگیری‌های شدیدتری که قبل از آتش‌بس وجود داشت، بازگشته‌اند، زیرا طرفین با اظهارات تحریک‌آمیز به یکدیگر پاسخ می‌دادند و رئیس‌جمهور ترامپ اعلام کرد که محاصره دریایی بنادر ایران را از سر گرفته است.
آقای ترامپ همچنین رسما به کنگره اطلاع داده است که درگیری با ایران از سر گرفته شده،
که اعترافی به فروپاشی آتش‌بس است و این موضوع، جدالی بر سر اختیارات جنگی حیاتی را تشدید می‌کند. کنگره به رئیس‌جمهور دستور داده است که یا جنگ را پایان دهد یا برای ادامه آن درخواست تاییدیه کند، اما آقای ترامپ اصرار دارد که او تنها کسی است که حق تصمیم‌گیری در این زمینه را دارد. این نامه که روز جمعه ارسال شده بود، روز دوشنبه توسط روزنامه نیویورک تایمز به دست آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://telegram.me/news_hut/68012" target="_blank">📅 21:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68010">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_g2Mzlx54ceOJm4lnsN7dSQO_zRzCE2N5Uo5TC81E6SGDwlt2Pe9QPHOrYAaQl4xnwFC9iXj-C1I8ZkeatRcoxgz2XB-uHWSn6m92shpV8XJ7IVcHM1rcGq5zx-Gzi3ilikrojPo20vNUqNDIXQrSaiJ1CPwRFXQXQn0AfgcAv3DX09AfwaOPd0f3NpsLHZ4SkJE3WQFpmAkPHbaXKOeE-BykzLWKR78osvPBUFlVAWg8fmuCokM6kl9qblr6-1bGe-880yhO0JJ9bICACJP8YxQEbNfd6yOgDZQ5UZCj9MB2smI5Ibpo3q3Ho_hU1VZrvC2QmBwnr_K_zUgDXFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛ایالات متحده اعلام کرده است که از ساعت ۲۰:۰۰ به وقت گرینویچ(۲۳:۳۰ به وقت ایران) در روز ۱۴ ژوئیه، محاصره دریایی تمامی بنادر و آب‌های ساحلی ایران را به اجرا خواهد گذاشت و تمامی کشتی‌ها — صرف‌نظر از پرچم کشورشان — مشمول این اقدام خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://telegram.me/news_hut/68010" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68009">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrSEKlFG3zfW__j2Qe-AsmGfi9GcmeaE5npZWSpcV7h3wNjqGLQp33ulI_xAseJSjPAO3L4W6IWCLMRkQqu6ZnYGabZ6g0HwJFt-zpsX2Vew0KNvv03tRVq7yvop0As-nXtN6VItgXi9OQT1v54Q3_5BG2H06bsGlkbeQgAuLDBmB4jKzBWeBB9l_4nfR0kNwsBnnvhyyGTLTFFM327bNawBV_ZIrQ_VRUPXge9vVnhxcxVkF0tYCyZ2XWQzEFaypQ2Ko6uWw5Fu8-2jhVyIpkPgWXmHZ-tPBnGU-HtT3TMgO-IoQfL9RM-ukDPvrhmhAnzTph_FkzF20vvRw17QGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://telegram.me/news_hut/68009" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68008">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
هواپیما جمهوری اسلامی داشت میرفت سمت فرودگاه صنعا، این فرودگاه بلافاصله توسط جنگنده های عربستانی بمباران شد.  @News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://telegram.me/news_hut/68008" target="_blank">📅 21:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68007">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33092f28c9.mp4?token=u15UVo6EQsTZ0_pER-lmX5XUBnGt4b-ok8dh-f93Al3Xzf6SxgpjIWSdamFZVMPhsBIl-1jt1fvKrp1aVKdOeualWSApMZjnBGxAqWjpURtsZudq05htk7AqNinwaIckmXIhmf9LJGkCZYw3Q3vHtl8u16xMwB3eRFrPkBiJKko7gXNXxD3NtmCJEWV3tqBiUBJrMkueXF1FwOv1B9JV5I32CQ3FtyJCZq5T6-jUlEcmzpDHF3QTUzO2SIE2wl_YrriA64Omh3FAI-b1GEdyxYVqfcITkyvyHW8jSKPmsWRX6NHCmJJ3QBn_eNYqFGfnRSv9EAILyUWDexozooOIb4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33092f28c9.mp4?token=u15UVo6EQsTZ0_pER-lmX5XUBnGt4b-ok8dh-f93Al3Xzf6SxgpjIWSdamFZVMPhsBIl-1jt1fvKrp1aVKdOeualWSApMZjnBGxAqWjpURtsZudq05htk7AqNinwaIckmXIhmf9LJGkCZYw3Q3vHtl8u16xMwB3eRFrPkBiJKko7gXNXxD3NtmCJEWV3tqBiUBJrMkueXF1FwOv1B9JV5I32CQ3FtyJCZq5T6-jUlEcmzpDHF3QTUzO2SIE2wl_YrriA64Omh3FAI-b1GEdyxYVqfcITkyvyHW8jSKPmsWRX6NHCmJJ3QBn_eNYqFGfnRSv9EAILyUWDexozooOIb4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی اقتدار و وطن‌پرستی محمدرضا شاه پهلوی و قدرت ایران، جهان غرب را به واکنش واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://telegram.me/news_hut/68007" target="_blank">📅 20:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68006">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c93097e540.mp4?token=mAYw8-H-1ulTL9TUTQoa1uCEh9XdZ_3KFo1WqF81jcybvuqsZ3JUErSVKT4edVomOp4oMo5Q1rgKI3OcFWW1eDv5HfpjgTWCIUay_WpVk7YL8L3pnEpL7p0AdYXNonGfLRznhqzU-IK99dqx9qoHtEF97J-U0mco_el2OBbGOthi92mHbcXP-Wq1VL7fixOsA1yeRc1EOrlMt2yRA88IPZvsnIA0cEJOb60a42ePiq3nZphueg8ztXcJPGc5B3SeeggMFRc2IE_7UiP7YxCsJQZ5ND-3M3vblU98GEanBzR--z7d9YenKNejO8yxpxoXTU12fWVSvD9aVas2HCs4sgL-JrhxRGt3JIua-8Jqow-1ZQHGy11D3ZP5ux_jfj5rL4OTDznAPTwS2_K-Aw_sXPnL90-e3jsCyPtCvzGZty5PpbyTKFIiPi1wGeBftYRbSEjcjmHxd9Rp6ElBosA82O0qtichg0Ek2kDFokA5U6XhbI5RKkhqzlUe7CUomfow-m_RBEFTxCpxuZJwegOUYl1F2rl4_KWi3NS3Fndy6z08QW18OoRKSmyoKU9cWtWraBkh1s8S0VqP9tm7smHytqgSOgjN6-dB-Bf0PdSpr8tc3vnIhCzfOv1nc13gyUPuaFz_L3yPPOEl0n4zvnlhPhmVE8IO2mI_HjJQamfs460" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c93097e540.mp4?token=mAYw8-H-1ulTL9TUTQoa1uCEh9XdZ_3KFo1WqF81jcybvuqsZ3JUErSVKT4edVomOp4oMo5Q1rgKI3OcFWW1eDv5HfpjgTWCIUay_WpVk7YL8L3pnEpL7p0AdYXNonGfLRznhqzU-IK99dqx9qoHtEF97J-U0mco_el2OBbGOthi92mHbcXP-Wq1VL7fixOsA1yeRc1EOrlMt2yRA88IPZvsnIA0cEJOb60a42ePiq3nZphueg8ztXcJPGc5B3SeeggMFRc2IE_7UiP7YxCsJQZ5ND-3M3vblU98GEanBzR--z7d9YenKNejO8yxpxoXTU12fWVSvD9aVas2HCs4sgL-JrhxRGt3JIua-8Jqow-1ZQHGy11D3ZP5ux_jfj5rL4OTDznAPTwS2_K-Aw_sXPnL90-e3jsCyPtCvzGZty5PpbyTKFIiPi1wGeBftYRbSEjcjmHxd9Rp6ElBosA82O0qtichg0Ek2kDFokA5U6XhbI5RKkhqzlUe7CUomfow-m_RBEFTxCpxuZJwegOUYl1F2rl4_KWi3NS3Fndy6z08QW18OoRKSmyoKU9cWtWraBkh1s8S0VqP9tm7smHytqgSOgjN6-dB-Bf0PdSpr8tc3vnIhCzfOv1nc13gyUPuaFz_L3yPPOEl0n4zvnlhPhmVE8IO2mI_HjJQamfs460" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه از هیجان پایین جنگ ایران و آمریکا خسته شدین؛
پیشنهاد میکنم این شوخی معمولی پسرونه بچه‌های بلوچ رو تا آخر ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://telegram.me/news_hut/68006" target="_blank">📅 19:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68005">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e510433ba3.mp4?token=d8KDoYHRML3fSV1e2b65INjZJu2fTD9FV8iPvs7UoY0h7FzYYZ40hY7q6Lp1oEEbahFqICAIgfhZCCRk9LuxmY9GxtiggA-sKmKEB1vtfPDRM6ySr8gSyef_YvFIQwfAVxhhsA5pfbZrp8mVgMwHmjqzV7E5WFuxHRdsKPcMZcp8MGPCY573ctJdIX0uUO_nD0iBYjkqTqrBuO7n_uO7Yamd8c07IHdWoR4xTDSSKkD3u9ikgdKQuCFoOB_y7ZyauYtKvLJQ0zVwlU-CDKf2NtW0m7u4_8Nju7v2hEnAXb8EPrAeto7R-8Zdg2zkjgpvQ-Lfg08KQTBZu3s5Y5ZWd02L_lz4IaHaAVqJiGGQrvZdLqsNk_tuu23VxHca7xMcaU0rh6e6ij2ip7C-AFevSXHdoG9XlXSP6F_ec3EIRDsPI893aEdVCMQkfkcVidvLRFVc3vBZGdge2CMVKcdkyTRC2JUWUNn8D5qnIxqXUmDsVZtMu0UstfcmYZF_sGBMS5WCjs_ExB4lmmF5QGvSd2dcmgA3fErsXOeUkmIIYm-yzl0xSxA3T5huNs1Nhw0TayP_EBXiVdh9hufs04T_6QfExXaNNY1tjE52vj-waJBlQ57PV_YfoQqmHH7hvVTwHomwhF1zbzF92hzMA2xDEAzGA4SPfvqDfOYDFBnCnBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e510433ba3.mp4?token=d8KDoYHRML3fSV1e2b65INjZJu2fTD9FV8iPvs7UoY0h7FzYYZ40hY7q6Lp1oEEbahFqICAIgfhZCCRk9LuxmY9GxtiggA-sKmKEB1vtfPDRM6ySr8gSyef_YvFIQwfAVxhhsA5pfbZrp8mVgMwHmjqzV7E5WFuxHRdsKPcMZcp8MGPCY573ctJdIX0uUO_nD0iBYjkqTqrBuO7n_uO7Yamd8c07IHdWoR4xTDSSKkD3u9ikgdKQuCFoOB_y7ZyauYtKvLJQ0zVwlU-CDKf2NtW0m7u4_8Nju7v2hEnAXb8EPrAeto7R-8Zdg2zkjgpvQ-Lfg08KQTBZu3s5Y5ZWd02L_lz4IaHaAVqJiGGQrvZdLqsNk_tuu23VxHca7xMcaU0rh6e6ij2ip7C-AFevSXHdoG9XlXSP6F_ec3EIRDsPI893aEdVCMQkfkcVidvLRFVc3vBZGdge2CMVKcdkyTRC2JUWUNn8D5qnIxqXUmDsVZtMu0UstfcmYZF_sGBMS5WCjs_ExB4lmmF5QGvSd2dcmgA3fErsXOeUkmIIYm-yzl0xSxA3T5huNs1Nhw0TayP_EBXiVdh9hufs04T_6QfExXaNNY1tjE52vj-waJBlQ57PV_YfoQqmHH7hvVTwHomwhF1zbzF92hzMA2xDEAzGA4SPfvqDfOYDFBnCnBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری ۸سال پیش روح‌الله زم:
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://telegram.me/news_hut/68005" target="_blank">📅 19:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68004">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97484f7b84.mp4?token=S9NMhaRfOImldOf6YQt0dITJ77vAmtZV-3RjIqYCm52e-xL6Vru_JGybi7JAy0wx2lRJqx9tu8Qc6txPs--s0BRvCAwDA5gSyn8hSFdeKHoMNtfJHqGx-qzFByQ-p3nPOEM0PYiMDAZwv2JGEzJIPaNWF_aBxfnER_JzKz4Vfvi7DZioyQqmnTpY_lJWxcIIdtSLBetG7q2_IKps9Few86Qt6IAdbDr-vicEj75-wiSL4MAfKzfUMtcgCY1gT8nqIXlUHc3EQHwo1agbTsxbZl6jzm4ODTnjkb1XGQ1R6NoEEcFdXP2kq1oJCMwAYFXLGpV8sqmDwzy_uQ_D18DFmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97484f7b84.mp4?token=S9NMhaRfOImldOf6YQt0dITJ77vAmtZV-3RjIqYCm52e-xL6Vru_JGybi7JAy0wx2lRJqx9tu8Qc6txPs--s0BRvCAwDA5gSyn8hSFdeKHoMNtfJHqGx-qzFByQ-p3nPOEM0PYiMDAZwv2JGEzJIPaNWF_aBxfnER_JzKz4Vfvi7DZioyQqmnTpY_lJWxcIIdtSLBetG7q2_IKps9Few86Qt6IAdbDr-vicEj75-wiSL4MAfKzfUMtcgCY1gT8nqIXlUHc3EQHwo1agbTsxbZl6jzm4ODTnjkb1XGQ1R6NoEEcFdXP2kq1oJCMwAYFXLGpV8sqmDwzy_uQ_D18DFmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💪
سنتکام: برای اولین بار با استفاده از شهپاد (شناور هدایت‌پذیر از راه دور) یک تأسیسات دریایی ایران در بندرعباس را هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://telegram.me/news_hut/68004" target="_blank">📅 18:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68003">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouvrBMx6DqAVQ9LKFbD-SE7VcZnOyRd6gRy2HIvZVQQMXu6AOwtbjOZYrZcNaD8CoTmwYqL_zXZGpITclx3RVCb8KGxjHQ4-r-AeffrF2f0gpLIzsaU5YJIbVZ1tWMmzDJK3y6SkEc05KEAcbnGY9qhQzOFg2fG3fkpbkaTVo6q-X5jMTA1h7Aon8ecdsAdz6Q31hWkF7ds-N7f96dO9PlyG66z1n2ulOH3mm1tVbjhsYt37b3H1NJWOe7DhuG8b6YoYXBzJblF0W0oNHraNHBgZXQ5W_1Kqq0cTIRPtg-dTMmPx48q6sJuI51t7alWleib7Mp5kLxYhMTS8pKARMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
رئیس‌جمهور ترامپ تروث سوشال:
تنگه هرمز باز است و با حضور یا بدون حضور ایران، باز خواهد ماند.
ما «محاصره ایران» را دوباره اعمال می‌کنیم؛ نامی که بدین دلیل انتخاب شده است که این اقدام صرفاً مانع از ورود یا خروج کشتی‌ها یا مشتریان ایران می‌شود.
سایر کشورها از دسترسی عادلانه و آزاد به این تنگه برخوردار خواهند بود. ایالات متحده از این پس به عنوان «حافظ تنگه هرمز» شناخته خواهد شد؛
اما در همین راستا و بر اساس اصل انصاف، بابت تمامی هزینه‌های لازم برای تأمین ایمنی و امنیت این منطقه بسیار پرالتهاب جهان، معادل ۲۰ درصد از ارزش کل محموله‌های ارسالی را به عنوان هزینه دریافت خواهد کرد.
فرایند و سازوکار اجرایی این طرح بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://telegram.me/news_hut/68003" target="_blank">📅 17:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68002">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛ترامپ دستور داد محاصره دریایی علیه ایران دوباره اعمال شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://telegram.me/news_hut/68002" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68001">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89a2b70f10.mp4?token=VJO-mlfSrMmn5T4HereqSh0z3QHoZmBkvZXZe5V6xl8iiuKUzl5P3XwXQnXfx57JoLf82NI6P3OK1ZzgLXR2lbabRsrqO8D6PXggsX-i-FFMKq9Y3aBEm7GZhPfe3kdRbmW4nt7BKTpI4c7LoH6IyPGsp1-WsO8B9-_rRDJ_BFSltN49vXd2zqaeQpcqMBFNP9YDHeHda444eFXqCVev2Mxd5ZEM9gVH8rghD6sNNy_cd_QrB1R0CIu3ZzfBVVfSCGKZo1qwWXs_M-L_zV_kcw3vHfDscNLFXNy3CKRahpaOcz8pIIbDjky11CdF5avGYSnJvuw92fnlgW0KgXVzOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89a2b70f10.mp4?token=VJO-mlfSrMmn5T4HereqSh0z3QHoZmBkvZXZe5V6xl8iiuKUzl5P3XwXQnXfx57JoLf82NI6P3OK1ZzgLXR2lbabRsrqO8D6PXggsX-i-FFMKq9Y3aBEm7GZhPfe3kdRbmW4nt7BKTpI4c7LoH6IyPGsp1-WsO8B9-_rRDJ_BFSltN49vXd2zqaeQpcqMBFNP9YDHeHda444eFXqCVev2Mxd5ZEM9gVH8rghD6sNNy_cd_QrB1R0CIu3ZzfBVVfSCGKZo1qwWXs_M-L_zV_kcw3vHfDscNLFXNy3CKRahpaOcz8pIIbDjky11CdF5avGYSnJvuw92fnlgW0KgXVzOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
من سلیمانی را کشتم. سلیمانی یکی از آدم‌های واقعاً، واقعاً بد در تمام این قضایا بود. اما در کاری که می‌کرد مهارت داشت.
او ژنرال بسیار باهوشی بود. من فکر می‌کنم کشتن سلیمانی یکی از بزرگ‌ترین کارها بود.
من فکر می‌کنم اگر من با بمب‌افکن‌های B-2 حمله نکرده بودم، آن‌ها الآن سلاح هسته‌ای داشتند و در حال حاضر خاورمیانه، به شکل فعلی‌اش، دیگر وجود نداشت
.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://telegram.me/news_hut/68001" target="_blank">📅 17:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67999">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d51dbf16e.mp4?token=Gy4AouaE1O4HE0tCcoYB3V1pp2d-5QUpiWmD9iT3BETuO16EDY3xVoHc8GG6GJIA2N9daHb46hvyfkk_BW50gbl3mL3x4WMwfe2IWjXkA9CSx5GT_jqhprZgv3ujqZv_vQxt9of1piHfGQk7vWC5vCX970U02v1ChVEw1fwDhPHqcArSxPKZD94LuKuCMrhxy-VLs7mDnvTtXsh7zgPHAXYo16FMxNjzDvwgfkDw-sm5RaGLry6tEAHF485LlXWbdxED3uu0ISlnrRfcTaKRw4VvNkksiQs716hSnAX83B8RaeRRoHaDRNuHgjI3mF9Vu2-nMhLT5Kshc9mcaY-hIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d51dbf16e.mp4?token=Gy4AouaE1O4HE0tCcoYB3V1pp2d-5QUpiWmD9iT3BETuO16EDY3xVoHc8GG6GJIA2N9daHb46hvyfkk_BW50gbl3mL3x4WMwfe2IWjXkA9CSx5GT_jqhprZgv3ujqZv_vQxt9of1piHfGQk7vWC5vCX970U02v1ChVEw1fwDhPHqcArSxPKZD94LuKuCMrhxy-VLs7mDnvTtXsh7zgPHAXYo16FMxNjzDvwgfkDw-sm5RaGLry6tEAHF485LlXWbdxED3uu0ISlnrRfcTaKRw4VvNkksiQs716hSnAX83B8RaeRRoHaDRNuHgjI3mF9Vu2-nMhLT5Kshc9mcaY-hIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها هیچ‌چیز ندارند. هیچ نیروی دریایی ندارند، هیچ نیروی هوایی ندارند، همه‌چیز از بین رفته است. پدافند ضد هوایی‌شان نابود شده است.
رهبران‌شان همگی کشته شده‌اند. بهترین رهبران‌شان کشته شده‌اند. آن‌ها از بین رفته‌اند. خمینی کشته شده است، پسرش هم ۹۰ درصد کارش تمام است.
آن‌وقت نیویورک تایمز مقاله‌ای می‌نویسد که وضعیت آن‌ها امروز بهتر شده است... آن‌ها تورم ۳۵۰ درصدی دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://telegram.me/news_hut/67999" target="_blank">📅 17:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67998">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebd104df8.mp4?token=ujdIhtnQfdJ4JNwC2p_PS3z-vJ_r5ryCmTosZFVFqpg5J-khF34TzOzxpvS1z_NBXKpv_OdBHg1Ins9e8wXjYKdbBypi0Rijxg_w7eoRgE8KDMAuioKsBREt0i2dkLf5dLC6zodukOkTtGznJFLRP21t4feLhwafHyBq7AGbNPLQCb8ooCLXEoulpmWF2A5FMM2bL-OmYtvsE8dR6--E0JwCMJ7RnFw7wLApPwDy_8ueLAF7v0k-cl-hbfb8xCR1TJgeNlE3zH5fZDz7K07fivoWq3HNW05y5_EeMXwEZRnJguAAg4K6HxeXwoKlWGdkhzGgw_IxIAaMwsL9jqDpYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebd104df8.mp4?token=ujdIhtnQfdJ4JNwC2p_PS3z-vJ_r5ryCmTosZFVFqpg5J-khF34TzOzxpvS1z_NBXKpv_OdBHg1Ins9e8wXjYKdbBypi0Rijxg_w7eoRgE8KDMAuioKsBREt0i2dkLf5dLC6zodukOkTtGznJFLRP21t4feLhwafHyBq7AGbNPLQCb8ooCLXEoulpmWF2A5FMM2bL-OmYtvsE8dR6--E0JwCMJ7RnFw7wLApPwDy_8ueLAF7v0k-cl-hbfb8xCR1TJgeNlE3zH5fZDz7K07fivoWq3HNW05y5_EeMXwEZRnJguAAg4K6HxeXwoKlWGdkhzGgw_IxIAaMwsL9jqDpYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
ایالات متحده شب گذشته ضربات سنگینی به تجهیزات آن‌ها وارد کرده و ممکن است کنترل دائمی عملیات‌های امنیتی در خاورمیانه را بر عهده بگیرد.
«بیشتر تجهیزاتشان از بین رفته است. ما دیشب ضربات بسیار سختی به سامانه‌های ضدهوایی آن‌ها وارد کردیم.
«هر بار که پهپادی می‌فرستند، ضربه سختی به آن‌ها می‌زنیم
.
«اما ما توافقی داشتیم... و آن‌ها آن را نقض کردند. آن‌ها همیشه توافق را زیر پا می‌گذارند.
بنابراین ما هم ضربات سختی به آن‌ها وارد خواهیم کرد، کنترل تنگه را حفظ می‌کنیم و احتمالاً خودمان اداره امور را در دست می‌گیریم
.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://telegram.me/news_hut/67998" target="_blank">📅 17:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67997">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060cc64d0d.mp4?token=bjmozVqowRcLlPD9uHjAAi-VRA4xrOqQ-wahBTkDXZZLZH37n7EkgxJy6Vvd43wS4ctvAsEv8WQGCUUfQoi6GubxayCt5Z_SZSuKFgxFJi26N9UGQNbgz3G6KFHswEQC3GEeilK4bp8lkOEWgFaLgvJh2mt7s3yas7fvglxZ95Xmbwb_fEWv8op8GZkDGPyeg1bYcIpYf9ynZ9bAOdXC3V__QyFa6fCjjJY_9IwSTv1CAVeELZGgDpK0zLduuRlS77DIB246Cjzcyg9H9JQOxe4MHgKW50yMQQncD-9yAGJwoHljkLb4GVkycJDJ5muflhzei0yNgeXN3oJgy17taQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060cc64d0d.mp4?token=bjmozVqowRcLlPD9uHjAAi-VRA4xrOqQ-wahBTkDXZZLZH37n7EkgxJy6Vvd43wS4ctvAsEv8WQGCUUfQoi6GubxayCt5Z_SZSuKFgxFJi26N9UGQNbgz3G6KFHswEQC3GEeilK4bp8lkOEWgFaLgvJh2mt7s3yas7fvglxZ95Xmbwb_fEWv8op8GZkDGPyeg1bYcIpYf9ynZ9bAOdXC3V__QyFa6fCjjJY_9IwSTv1CAVeELZGgDpK0zLduuRlS77DIB246Cjzcyg9H9JQOxe4MHgKW50yMQQncD-9yAGJwoHljkLb4GVkycJDJ5muflhzei0yNgeXN3oJgy17taQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
🇬🇧
دولت بریتانیا رسما سپاه پاسداران انقلاب اسلامی(IRGC) رو در فهرست سازمان‌های تروریستی قرار داد.
در حال حاضر، ایالات متحده، اتحادیه اروپا، بریتانیا، کانادا و استرالیا سپاه پاسداران را به عنوان سازمان تروریستی ثبت کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://telegram.me/news_hut/67997" target="_blank">📅 17:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67996">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4923d848c0.mp4?token=NFd6DvK1PjNhpO6_zlLNI88_PUF52R7_YajsCZrZjmIwMoHAYZ4Kg5HBJKkQ4kQ3Vb28d3ciwJkAd2yn5DHTniUQHaaPNSsaz0b-KbaPXeL7tarj9_PFZEnLoQUTyZsFnKxAfgMUWxsssgpokqvMEfHc5GPyDYfN4ExE1hEqGCnNVKIU3W93_lV7fFJxuEEMFdfW1UVQONBiOBFC-P5-29-ffZcXHXSChRgZH50OvLP_gFKZ7zid0WEkY9JKnEXtsJtIvXaPqAm2WKMw3WJoK6XFJVmzdggVWEitxoYvDgUbJm3XdpZTg7iJPpifNcmQvurkgo41sKxkQbACscKpiw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4923d848c0.mp4?token=NFd6DvK1PjNhpO6_zlLNI88_PUF52R7_YajsCZrZjmIwMoHAYZ4Kg5HBJKkQ4kQ3Vb28d3ciwJkAd2yn5DHTniUQHaaPNSsaz0b-KbaPXeL7tarj9_PFZEnLoQUTyZsFnKxAfgMUWxsssgpokqvMEfHc5GPyDYfN4ExE1hEqGCnNVKIU3W93_lV7fFJxuEEMFdfW1UVQONBiOBFC-P5-29-ffZcXHXSChRgZH50OvLP_gFKZ7zid0WEkY9JKnEXtsJtIvXaPqAm2WKMw3WJoK6XFJVmzdggVWEitxoYvDgUbJm3XdpZTg7iJPpifNcmQvurkgo41sKxkQbACscKpiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند
:
اونجا وقت برا دوش گرفتن هم بهمون نمیدادن.
از بس بهمون سخت گذشت که تعداد زیادی از بچه ها شورتشون اونجا موند.
مثلا من خودم شورتم جا مونده آمریکا.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://telegram.me/news_hut/67996" target="_blank">📅 17:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67995">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34b88bf07.mp4?token=Ecb0y82fA7O93hgwZIQtl1eW3rm3R2tbJrb9ey7nB59K1lClwsdxDfAoKac5GMvH3Oc2AH47luef76FgUA1RIIj4Dgcna2lnqDKk-5WNtw7Pp5vsbs4ooXwIOrXcDVeEjSmjhADLpgogojmzGnPtddV7eC2fOkSQeG9XmsHhZ-gOwO1zasC0MRCnpOI_cyBKYczUptlEGWTcFmAXzdRxX5olpu08rchtEESbviDwxQAeKkZNiAfYPtUxCUw_0d2eyVuHXlcFImR4dufJp6AGBRP1XDVRgXRktdhHE_oLmfHWsmNFKc5KJabOVv3uwsPVJfG-v4yfiyTo3OTgJKDFIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34b88bf07.mp4?token=Ecb0y82fA7O93hgwZIQtl1eW3rm3R2tbJrb9ey7nB59K1lClwsdxDfAoKac5GMvH3Oc2AH47luef76FgUA1RIIj4Dgcna2lnqDKk-5WNtw7Pp5vsbs4ooXwIOrXcDVeEjSmjhADLpgogojmzGnPtddV7eC2fOkSQeG9XmsHhZ-gOwO1zasC0MRCnpOI_cyBKYczUptlEGWTcFmAXzdRxX5olpu08rchtEESbviDwxQAeKkZNiAfYPtUxCUw_0d2eyVuHXlcFImR4dufJp6AGBRP1XDVRgXRktdhHE_oLmfHWsmNFKc5KJabOVv3uwsPVJfG-v4yfiyTo3OTgJKDFIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
🇺🇸
سپاه ویدیو ای از حملات موشکی بامداد امروز به پایگاه های آمریکا در منطقه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://telegram.me/news_hut/67995" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67994">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8627adc5f4.mp4?token=VcN3CyfaIqXg2w3DOwcnCHVGemBoA24ZdIqi7ezUQO6-Ja9SLbUOhx__o_5ZmVikvQ1wG0Awifejkw1GvGHozEgYAdOIYSkEgchfctopkfZk-kG7F6DkSUnQvHM_tI-h3nedeWDSxcNTZuzHjbgoW0OOtb_PDVzUzqijA8vJY8oI9ARVIU5AQuYICYyXuPg82vbaqLkihDszk81D8fhDrQzQOiX9gRtffXSlxIaEQz8QMF68z2-l-YaIwkHCpG-5jkuQPpbF0ANz_7I8XXI8PiJSH0Ynllk-h2dGeKpwDSX2hERIwLVE-EEPuUckIn7oNCvFCAcEWMxNFTLpwz0wAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8627adc5f4.mp4?token=VcN3CyfaIqXg2w3DOwcnCHVGemBoA24ZdIqi7ezUQO6-Ja9SLbUOhx__o_5ZmVikvQ1wG0Awifejkw1GvGHozEgYAdOIYSkEgchfctopkfZk-kG7F6DkSUnQvHM_tI-h3nedeWDSxcNTZuzHjbgoW0OOtb_PDVzUzqijA8vJY8oI9ARVIU5AQuYICYyXuPg82vbaqLkihDszk81D8fhDrQzQOiX9gRtffXSlxIaEQz8QMF68z2-l-YaIwkHCpG-5jkuQPpbF0ANz_7I8XXI8PiJSH0Ynllk-h2dGeKpwDSX2hERIwLVE-EEPuUckIn7oNCvFCAcEWMxNFTLpwz0wAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لیندسی گراهام، دوست وفادار ملت آزادی‌خواه ایران
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://telegram.me/news_hut/67994" target="_blank">📅 15:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67993">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a38d8e8e.mp4?token=VoByReyXHoyr4AVpWrcr-sdtIHfYlcriNQBX3eIkX41NC8jnorGUoh8tAANhuazMADP6iAxYARf6VvZYDNKdfUqvo3koMyVYlTmzFYXuhYGSLk1A7Dhw59v8d75AJTlcPhTQbCuZhbuRgXNLMQHSoehDWiGnSRvbGOE824Q-mD8a3Jc1qgiQRuGs8iVxt-Ra2v5ZedMtjUQWE98JYz24m94g4ypQCPytQZRTPMVw--vFoxR_0n_hdVltGo3YSmCyTirxBFEeW24h8IISkW5aUT6S5NazoRfzrNMJS8sUAeuDr6gQ6DP-C_-1iNbejDkF5ekJKsYjnbVCJh1JLZvfGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a38d8e8e.mp4?token=VoByReyXHoyr4AVpWrcr-sdtIHfYlcriNQBX3eIkX41NC8jnorGUoh8tAANhuazMADP6iAxYARf6VvZYDNKdfUqvo3koMyVYlTmzFYXuhYGSLk1A7Dhw59v8d75AJTlcPhTQbCuZhbuRgXNLMQHSoehDWiGnSRvbGOE824Q-mD8a3Jc1qgiQRuGs8iVxt-Ra2v5ZedMtjUQWE98JYz24m94g4ypQCPytQZRTPMVw--vFoxR_0n_hdVltGo3YSmCyTirxBFEeW24h8IISkW5aUT6S5NazoRfzrNMJS8sUAeuDr6gQ6DP-C_-1iNbejDkF5ekJKsYjnbVCJh1JLZvfGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇺🇸
سنتکام ویدیو‌ ای از حملات دیشب ارتش آمریکا به اهداف نظامی جمهوری اسلامی منتشر کرد.
در این عملیات سامانه‌های پدافندی، رادارهای ساحلی، توان موشکی و پهپادی و شناورهای نظامی هدف قرار گرفتند
.
همچنین برای نخستین بار از پهپادهای انتحاری دریایی استفاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://telegram.me/news_hut/67993" target="_blank">📅 14:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67992">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3c5be180.mp4?token=JIlEVuGMcG0JS2CfPIQgQn6T-lALbuM4r7xmVmB9Ycu7ssxGgBOEVh2KoUN4BWItYG4jPTd3eYUV0wIF4JD36V2JsJFYwehVDj6St3nF5TRn5Oh3V5A3hN1XQIBBzddUv728pO_7PrRN_2-qvrWgRj_s17A_nE55t808N-Qr6XqkwolkER77DCOAbTCNs5I2h1fsYXmTxXyDgitlJ5dR5nDvJ_9XmBjaSkmaPVEs5eu5xsTEWEyfrwMaTrWNo_dgmh3s9ZAeB22YlY-fCcHHTGd5rTf9wyjWD1zOkd0EBrUGWpBaZrCGENTzjn--1a6hLSDcKxDuG--_ccOn1ZdsGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3c5be180.mp4?token=JIlEVuGMcG0JS2CfPIQgQn6T-lALbuM4r7xmVmB9Ycu7ssxGgBOEVh2KoUN4BWItYG4jPTd3eYUV0wIF4JD36V2JsJFYwehVDj6St3nF5TRn5Oh3V5A3hN1XQIBBzddUv728pO_7PrRN_2-qvrWgRj_s17A_nE55t808N-Qr6XqkwolkER77DCOAbTCNs5I2h1fsYXmTxXyDgitlJ5dR5nDvJ_9XmBjaSkmaPVEs5eu5xsTEWEyfrwMaTrWNo_dgmh3s9ZAeB22YlY-fCcHHTGd5rTf9wyjWD1zOkd0EBrUGWpBaZrCGENTzjn--1a6hLSDcKxDuG--_ccOn1ZdsGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تازه‌ترین ویدئو از حمله هوایی به فرودگاه صنعا
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://telegram.me/news_hut/67992" target="_blank">📅 14:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67991">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWThV1GxHYrB_O6X2gQCOLQpApc9R2c6s98kZwn2cxzw3hzKEFkgQMBMYNxC8Vsmz3JytBlcXehDxOAi6iQpygZwYyfW3z1Is2nA9rGDTO1hCgAFrftH0t77NVPblQCTcA0PqBHgrJCXX3Qec7wNGp2zXICaZvlCCjgMrxlP6JlAvXtupeaJmLLUIrxUW2cnvUVy9w_CSUOlyyG2bSHG3NgbemfWQwG47BVsFRtqCLIkTZQMIKXMtxnY1mkpVyB0h8ncre5lvEG6O91tE7dU86wCMNuMljyXaDSG8716nDCVoaM3HG_YRVbbqPgAknAkV-ZWM7XrFnFKR_TdUr0sJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
هواپیما جمهوری اسلامی داشت میرفت سمت فرودگاه صنعا، این فرودگاه بلافاصله توسط جنگنده های عربستانی بمباران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://telegram.me/news_hut/67991" target="_blank">📅 14:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67990">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFH8-N4KSZjKUIzyeAkvOEO4Xt4wIJ5vGWEmsPdqe-_U0G3RtwQ25wNzGmiasUZlcpbBY077jI2pMhSW-IJ0wEvFhMUuUJWXBhSoFEJ1q3mWP7R75-t1k1G6GWD53QM7vw792bP_QSQMqaMdBUPxFyBFk4SKuv2cEgep-oMEN7PDrvPMJopOkmSPG7BZQxVUFH85xTPT0UxRMtOTXHLWeS3eGtJQ2_p-XUGkw98jspATIhy3zn4VyXHHSkaGhblxliSuzruQ5pMl0CMZIdjPggKIbqehgP7k_vh3_HPqyL-ahHvE6rZloLrCTVXUmIyxZwkQr4aNrHj5W7bFwC_rng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی، خواننده وآهنگساز ایرانی، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
جاستین بیبر، شکیرا، مدونا و گروه بی‌تی‌اس در این اجرا حضور خواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://telegram.me/news_hut/67990" target="_blank">📅 14:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67989">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u0XfcUH-QK_TpDunY_9OYHzsDUJc5gfIMemfk5tJsfShoz6WrR6gCJc93tD9o80Y2tisApyfDG3noeWUSAroQzL3PtKAYU5Hj1RwI63v1HAKfPX1h6uhYP5QeIk0qOaHRjrP5-biTFn224ySFwq2jbz1Dqig6QFA3svC2yslVswgP4d6oLIfcfEoA6abYqfbggZUThrJX08ZYGJ5PYBOK0hma_2RZs7WfKQja1IXTWxF54iXdJzjsfSTSnQImJV_bSfuomY1-UHhYEG-Qn21AIqfcULwaM2rq_TFcpelgJhj6yKn8OirxxyEXzwg6zSrUkoCjQ8VsH1opRjITMlExw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های داخلی وابسته حکومت این لیست ترور رو منتشر کردن و نوشتن لیندزی گراهام اولیش بود تا نفر آخر بی‌خیال نمی‌شیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://telegram.me/news_hut/67989" target="_blank">📅 13:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67988">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
تنگه هرمز دعوا شده
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://telegram.me/news_hut/67988" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67987">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7891d1b9.mp4?token=r0l0e3IkD1BwwHqnH0lK39mCoiiw218zi_S3U1rz9vAwRqr--0S9rF5wsOxTBbYgTZw-pTM9kUkig30FP8udAy8Y9ZXkksocZgyaRNtGsyE8-i9P-cYhJxed02MBw_o9vH5uVqT2lc8lVsQN5T5zGFNiZPU0jP_iwe8iiYvmaVXcFvpWF8fK7CU8ZO-GRGbG2POB5cdz3_4U9z8H2dLRKowtWbE2ixDLb-GobMmoRdnOIOLt6AduebVdrRrGVOoHPa-3xE7EdJZPNPHMEUWlA2egZ26ntbEN8UqD_CMysVwr_TmDMsvyEDe07k28WVFBqtO-mq55naMT17cXyHBTOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7891d1b9.mp4?token=r0l0e3IkD1BwwHqnH0lK39mCoiiw218zi_S3U1rz9vAwRqr--0S9rF5wsOxTBbYgTZw-pTM9kUkig30FP8udAy8Y9ZXkksocZgyaRNtGsyE8-i9P-cYhJxed02MBw_o9vH5uVqT2lc8lVsQN5T5zGFNiZPU0jP_iwe8iiYvmaVXcFvpWF8fK7CU8ZO-GRGbG2POB5cdz3_4U9z8H2dLRKowtWbE2ixDLb-GobMmoRdnOIOLt6AduebVdrRrGVOoHPa-3xE7EdJZPNPHMEUWlA2egZ26ntbEN8UqD_CMysVwr_TmDMsvyEDe07k28WVFBqtO-mq55naMT17cXyHBTOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:با درخواست گروسی برای بازدید از تاسیسات هسته‌ای موافقت میکنید؟
🔴
بقایی:خیر
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://telegram.me/news_hut/67987" target="_blank">📅 12:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67986">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://telegram.me/news_hut/67986" target="_blank">📅 12:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67985">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=f-CAS1C1_LcMtwTlW4vGv7jKqGeMzndlXswpEHj3wwAK0IMSMG24nkbXRTj-0Q_7hyOrBCnCRtHHKAngNQsuoZEkiOJ1a1_ZFzldl136EVb3GXYj0CpS9K0c0OcSb8lvlAlOAs6ysTdCLRrsMSCkE_sDEzTk5O14ZrOJ2uZMMRV60tXFEY9-SUPX-Gkh3Vm51Jvbz8eVYNDWd768GPthk4Qc6FYQmLkrdJfkbnKqCMs791hAt2XmaFWCdLQw3yxlTmdpwUAHMi0KH8o5sp0flzeKehCHcgeemgu-Hbcbmri5rUj-gRrtBPYJIxvzCvxqb3dKrrsR0lw6fmc8MVLuEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=f-CAS1C1_LcMtwTlW4vGv7jKqGeMzndlXswpEHj3wwAK0IMSMG24nkbXRTj-0Q_7hyOrBCnCRtHHKAngNQsuoZEkiOJ1a1_ZFzldl136EVb3GXYj0CpS9K0c0OcSb8lvlAlOAs6ysTdCLRrsMSCkE_sDEzTk5O14ZrOJ2uZMMRV60tXFEY9-SUPX-Gkh3Vm51Jvbz8eVYNDWd768GPthk4Qc6FYQmLkrdJfkbnKqCMs791hAt2XmaFWCdLQw3yxlTmdpwUAHMi0KH8o5sp0flzeKehCHcgeemgu-Hbcbmri5rUj-gRrtBPYJIxvzCvxqb3dKrrsR0lw6fmc8MVLuEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
ایالات متحده مسئولیت مستقیم تحولات اخیر در تنگه هرمز را بر عهده دارد. آمریکایی‌ها از همان روز نخست زیر قول خود زدند؛ آن‌ها تلاش می‌کنند مسیر امنِ هماهنگ‌شده با ایران را دور بزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://telegram.me/news_hut/67985" target="_blank">📅 12:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67984">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ae996e.mp4?token=uS3Zjvo81mHEPPf_dnTNpcCszZsBt7TMKtWvm-OEJJ4frIeCr6IYMrwbHAWstMlfsuDZEs_LMFPQzsqbAQS_rVu2Vk94GX7pCwLqtWt2PWZZBCzM7OniAMf598yfExwHA4dHvZ3K0TQm__i8W8O1oQebMHy5Dp-ASIIoBKlgBzaZfpIZX4nrE5rGDK1mDRwCmV7zkn1upFiDR_1ibYern8o6KkdNg1JD9y9BVbIFRtkS50KbanGJA1sfmSG7uxR38rQSBOji940ms8SppB4SIhuE5frHUcSZSX21q6JyjBl7acmtgyFWyL_tMB5MeM-sCekG-jQ__5N7_M6jFOOXdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ae996e.mp4?token=uS3Zjvo81mHEPPf_dnTNpcCszZsBt7TMKtWvm-OEJJ4frIeCr6IYMrwbHAWstMlfsuDZEs_LMFPQzsqbAQS_rVu2Vk94GX7pCwLqtWt2PWZZBCzM7OniAMf598yfExwHA4dHvZ3K0TQm__i8W8O1oQebMHy5Dp-ASIIoBKlgBzaZfpIZX4nrE5rGDK1mDRwCmV7zkn1upFiDR_1ibYern8o6KkdNg1JD9y9BVbIFRtkS50KbanGJA1sfmSG7uxR38rQSBOji940ms8SppB4SIhuE5frHUcSZSX21q6JyjBl7acmtgyFWyL_tMB5MeM-sCekG-jQ__5N7_M6jFOOXdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
پیگیری عدالت برای رهبر شهید، یک اصل جدی و مطالبه‌ای همگانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://telegram.me/news_hut/67984" target="_blank">📅 12:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67983">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=rA3x45XYMv7Hr9GmNivXxk171BM5Om9VpVoL0HUKFx4oRHpVns1t9QNU-I0SC6LOqlD9_rleDlywj0fJCDuQVVUsLFyoW76T3xoxkzUbsDZSc7DxXb6Jij3PNjWlUfgUqKR4pXX0b3ywzYx8SnSWVa9UK1YOOSL0FTUmXUxSF0h8Z3J_c0jZhs5FGXBcL1kx7UNZR9XWQaMmQs_B5xa9BxYMtIQLnqcGAQ6tQEp277-5SXBKtjFGP0rQCDYJJDWwffh6Rvr67xeRISncRF7dZ4ywUq-U6KIRmvxZTcgZ2f3oeODRd5yAM4-1oWl5fa7IkbYQhd-09jpACX_U6eu21g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=rA3x45XYMv7Hr9GmNivXxk171BM5Om9VpVoL0HUKFx4oRHpVns1t9QNU-I0SC6LOqlD9_rleDlywj0fJCDuQVVUsLFyoW76T3xoxkzUbsDZSc7DxXb6Jij3PNjWlUfgUqKR4pXX0b3ywzYx8SnSWVa9UK1YOOSL0FTUmXUxSF0h8Z3J_c0jZhs5FGXBcL1kx7UNZR9XWQaMmQs_B5xa9BxYMtIQLnqcGAQ6tQEp277-5SXBKtjFGP0rQCDYJJDWwffh6Rvr67xeRISncRF7dZ4ywUq-U6KIRmvxZTcgZ2f3oeODRd5yAM4-1oWl5fa7IkbYQhd-09jpACX_U6eu21g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای آمریکایی با استفاده از مهمات سنگرشکن، یک تأسیسات موشکی زیرزمینی در پایگاه چهارم شکاری تاکتیکی ایران در نزدیکی دزفول را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://telegram.me/news_hut/67983" target="_blank">📅 11:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67982">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCnj0XNzA7FuqsuZFn3XzILLrzldCy-Nml_v8TULkDY7mzPEtufqcrxk4sroipjOsZ5I77RvVWOSs23B0ZO7pq6g42zCtxy6YWHL4g1NNc2MkecgubZ57TY8vni7iu9giNOS4EE6-wuqtL9xYZbLp1Vnh62d2x-5SYPZmvJhwKttvfiaKmmNLwfSIjk8xFSXnw3d_Iv2n8lPJyHlaisLFQPStSP_gdwG-M61vaNBkAq2SIMXbuGIjJVjqWXQN4DnILZvVMRcWNT0i2HEsXmTI9OWIJmJVXD3tAjhMptGt2ikhzMpMu6e3OkBJSqC3pom0NeOaibnb0XpXxenbF2rfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
پرزیدنت ترامپ در تروث سوشال تصویری از لیندسی گراهام منتشر کرده با کلاه معروف:
Make Iran Great Again
ایران را دوباره با عظمت کن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://telegram.me/news_hut/67982" target="_blank">📅 11:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67980">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rB-LkrjacyT_8foGTkYmZ-vWfyQ05RLbHomUXMyNdxUh5C7XFTBcey4w4bv6hqj5S7lJNwiquKiBB6QjrEyKBIRVNK7nezOlAIrjCHvExA42n1BtpiYKJMUAZI8xLsMFEa8Uuo2tDaapUcmrZK-LIF4i9DmWnqEbcZdYVUcnQLffyGqU0-HMAeHXVbrbeteLQsL5RDpUkF7hkJWZyR49giXF90ErARJvDZZyggN6ypscDcSFJaup5vc0eNFjiNwoyuUTrKdQ3Bw959bg9jgbcLWAaDtaELvUI0bnWoahDRwvw_B5bFtLq_QBkfPuLy1qMTd7X3hEwHA_E58Q0S-xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwlHL6LWJsIk7S0BTRkChquNdhUcCoByDOOBj3kUQNK49-mtIK3-lXhy1UyEcbq43GhCzWk7rTq0zopITHfW0mWct60X-xJOn9wZ7Vh0NQSsCxvRUPB0V4GFhE7INq-_xsFDGJ-rAwRDVYpvOJSHHBG_JhWWTm3wzigjHXmetti2SpbMAttw7cu3L_seBqqOZx2Pkyj_L0aDXgjBGzscJsTehAapFthTGW7lNNRj0742gMoOxUpXzPg_Ee13QsCvZAt4m3Ozw6ofyIqzWbLiutbAp54Q1q8AgfWF5p88b4JNtTz53lxMYvypQHy0tLkzvCNhj2JDYRfNvXjU_EzKgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
انهدام پهپاد انتحاری لوکاس آمریکایی توسط پدافند رژیم در بندرعباس.
آمریکا در بامداد امروز برخی مواضع نظامی جمهوری اسلامی را با پهپاد لوکاس هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://telegram.me/news_hut/67980" target="_blank">📅 10:22 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
