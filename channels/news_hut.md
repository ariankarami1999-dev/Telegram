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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-23 18:12:24</div>
<hr>

<div class="tg-post" id="msg-68087">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به ۱۱ شناور در دریای آزوف — شامل پنج نفت‌کش، پنج کشتی باری و یک یدک‌کش — حمله کردند؛ اقدامی که نهمین روز پیاپی از کارزار حملات گسترده علیه ناوگان کشتیرانی روسیه را رقم زد. نیروهای سامانه‌های بدون‌سرنشین اوکراین اعلام کردند که در بازه زمانی ۶ تا ۱۴ ژوئیه، به ۱۱۶ شناور روسی حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/news_hut/68087" target="_blank">📅 17:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68086">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=GFzSpVhTRYMSj-goHjL0X1Pjacfgn_o41nI-dMO-zVx8IcV2gE9BRbTxWJG5zYz9mLbeb82hRZn4A3kP9wg7UhHa978ixJnCxKZJh8aLmxKTi5Tk7UKJ19GNZ3yzuxMBsL0AVLRxmIBkBSJVHTiAAVyicIKMq-VF914-Ti6GTqT4hpMcwnCU4EPMab0zyFR75bExHzs9VKJ-caqKKMDZMvg5vxJ6ixPupIUKvntvJT0lH_8QnwAuKM37L9qp0itjIN5Oqphc4BFPoxJl3we3kLEFLjXPTxArPGS5hYMwyqyJzD6baPYlE_i7xmcHl5ZdfRcjgUINg-DJCJuca9EOvXbVd0k_KrzKG4CM7IZFqgYH3ZdhWaa1FM23bKqmk-ET7gYqtuVSoNDd2QS9nlxMzBcWgV5TwroZcpLVZpIjVmmNIJNuZxiqBl-CRu7BbdEwxqvPTya-7iP3TrPvtscskI1UNKSpzulQJ-x2BTEK8Q2D7DnFS9CMCUgVjw3TRmNhDqi8uYiOu4LBpvDJ0NI4FWGnP6pkCH8bnBfI8Cu56t5ZILZ-hpPwe3n8ZGh9rOa4pidKsFhDyQGDfl1VOp4K0HpaNwFC4ierrpLMtZmAsLCr_laAIX_E_-7w7DJfHCvMAyvXivSR2XwfgTCWtOctiE-SK0qC_xRCaNt2cwm40TI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=GFzSpVhTRYMSj-goHjL0X1Pjacfgn_o41nI-dMO-zVx8IcV2gE9BRbTxWJG5zYz9mLbeb82hRZn4A3kP9wg7UhHa978ixJnCxKZJh8aLmxKTi5Tk7UKJ19GNZ3yzuxMBsL0AVLRxmIBkBSJVHTiAAVyicIKMq-VF914-Ti6GTqT4hpMcwnCU4EPMab0zyFR75bExHzs9VKJ-caqKKMDZMvg5vxJ6ixPupIUKvntvJT0lH_8QnwAuKM37L9qp0itjIN5Oqphc4BFPoxJl3we3kLEFLjXPTxArPGS5hYMwyqyJzD6baPYlE_i7xmcHl5ZdfRcjgUINg-DJCJuca9EOvXbVd0k_KrzKG4CM7IZFqgYH3ZdhWaa1FM23bKqmk-ET7gYqtuVSoNDd2QS9nlxMzBcWgV5TwroZcpLVZpIjVmmNIJNuZxiqBl-CRu7BbdEwxqvPTya-7iP3TrPvtscskI1UNKSpzulQJ-x2BTEK8Q2D7DnFS9CMCUgVjw3TRmNhDqi8uYiOu4LBpvDJ0NI4FWGnP6pkCH8bnBfI8Cu56t5ZILZ-hpPwe3n8ZGh9rOa4pidKsFhDyQGDfl1VOp4K0HpaNwFC4ierrpLMtZmAsLCr_laAIX_E_-7w7DJfHCvMAyvXivSR2XwfgTCWtOctiE-SK0qC_xRCaNt2cwm40TI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بخشی از مستند "عمامه صورتی" که در سال ۱۴۰۲ تولید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/news_hut/68086" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68085">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/68085" target="_blank">📅 16:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68084">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdI6sQNg8c9l8npIlxZLOwyJLwcAFqR7qEHebaztYVJl4aJdjvcp8TLdhlFwIjwykE0bkkhxxLmy09wvpK9hA-CfRVNFbudqoqJzK4dnXq1OKmT-9cHvoyVGPzctO7W5B1xwygFw713AWQYCM2Z2zTWmJy1IovSYiQvJZHc03CrT6f1fuoEb8NAfODxIMeXxqCeSE0SuBZum8CkniOfnE9KItk3p4KgienAFO3JJO2EO69bFqDlou1KlYSKExyyw1Nrq73C7Du2wxNgdEfxP3eQtnzdzmou-aWHoiGmjhvR09xqKICwQXH_ASBU6jeA3etamyliirK872E_OGEgilA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیکتاتور قالیباف
؛
سید محمود نبویان نائب رئیس کمیسیون امنیت ملی مجلس و ابراهیم عزیزی سخنگوی کمیسیون را که از مخالفان سرسخت توافق بودند از هیأت رئیسه کمیسیون امنیت ملی حذف کرد.
عباس مقتدایی نماینده اصفهان و از حامیان دوآتشه عراقچی به عنوان نایب رئیس اول و حسن قشقاوی از دیپلماتهای حامی برجام به عنوان سخنگوی این کمیسیون انتخاب شدند
.
بهنام سعیدی از نمایندگان نزدیک به قالیباف و یعقوب رضازاده نماینده سلماس که اخیرا در مناظره‌ای با ثابتی از توافق با امریکا حمایت کرده بود نیز به عنوان دبیران اول و دوم این کمیسیون انتخاب شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/68084" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68083">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/68083" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68082">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXTap9VgC4JfqwDNhOrltsVIHBdcIanzBfW9exqMz4L7liDNqWJa3-vsptbmylmamve9DLiEcNyFPy56Lemeuk8_J3wLBQDTctXW3iufQp8P1m3kW0iqZMYOUMDTe5WhTUmbwJ3WKNtEUnTjdQWo1IITZt_3nTpeLyifmvF7fS1jrzHPEzr_w1osLfvp56zM4wKwkvhvNcg_i3LI0RpzVc7Lh5_wJK1CTzFhlDOjxEfljdRr4hNLNvqYq2Tgq9sCD2k60ivZstiXH2YpBn9loIw10_KsLiMIp7FzZse3D8nVtQbnLdFz9VjjHbnBiv467cs34nGnaSZR_7CDlwguTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لبنان و اسرائیل مذاکرات خود را در رم از سر گرفتند؛ در حالی که لبنان به پیشرفت در جهت عقب‌نشینی ارتش اسرائیل و اسرائیل به پیشرفت در جهت خلع سلاح حزب‌الله امید دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68082" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68081">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=dTVnRD-k-inLNcnWaE2Sj3_jgifxlcg_uHRpuAZwA-jPnWtQy2UFhUBtal2zYGKxv9FuT5Z1N_5J27YMtymKFRQdxEPZJamEv1Hh8gS_Nqt0Y-qoMlDoY1RB_HgOucLskczrrlNFrml05KCVaIvL0zCvcZc72lCxyNITuVZUWuLFeeQTR3vvN_2J81uhlZx-m9ynm7TxqmlTaX2F-FQi7lC3dsVVVAhS8ij9s4VOCFeUfeWilZh0IptMXyzf4HyZcDs1bd7hZU3L_3VlbDR1icTJgnwr0qbJuly7BRvsvJsQQXJWjLa6N-a89eP3jYibKdoV--T4pE6qu4mPmgEMWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=dTVnRD-k-inLNcnWaE2Sj3_jgifxlcg_uHRpuAZwA-jPnWtQy2UFhUBtal2zYGKxv9FuT5Z1N_5J27YMtymKFRQdxEPZJamEv1Hh8gS_Nqt0Y-qoMlDoY1RB_HgOucLskczrrlNFrml05KCVaIvL0zCvcZc72lCxyNITuVZUWuLFeeQTR3vvN_2J81uhlZx-m9ynm7TxqmlTaX2F-FQi7lC3dsVVVAhS8ij9s4VOCFeUfeWilZh0IptMXyzf4HyZcDs1bd7hZU3L_3VlbDR1icTJgnwr0qbJuly7BRvsvJsQQXJWjLa6N-a89eP3jYibKdoV--T4pE6qu4mPmgEMWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:  اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد. در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68081" target="_blank">📅 13:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68080">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
معاون استاندار بوشهر:
چهار نقطه در شهر بوشهر مورد اصابت بمباران آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68080" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68079">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Szc0KHvvpEMER4Yb6nqgoaAo1mQpXZhPruviNxWMaH5PYxFrCo7r_m55mU9JGq-ySjVtnhd7X--HSkSsLGCxO0brQy8bNJBnVa5yxiDauIXB6nv6ECmTerDtj_1bZx4qwUxpJ97dktFzt5-VeuRTY5uTmVi4l1MUfyoPUFIHC08MEhCEk9fSFLyto9nzQwqddQUGcJ_mTRJ38Pu6xKSc6b9c9ZLVmfjT_tv-TGzncDcUgBJfvA120j4FAagvFrP73R6SlDwUgBawF6P3FlE5icsr136Two40XYWdF8Jap44HWFdqUp1okD8_0RxVs46S4NLjzVhuqEzYbf7Q6zKJ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نمایی دیگر از بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68079" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68078">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJUIOEMoN6Jp-DX4XEq_L1xZhP3HJyvfqCOaPBnmsLQ-XYvIR_Oiz1kgIjzqMySP5wHfTlhiMoTL6CTqJecDSBPHhGjPd8cv6Uc0g000XyEdNT5p0U0bvRCmc8JeOpgbOGa_8NE6V5xZgJaw4w34Ut_L9QOuYjRXfZSVUJvz52I2Dlb10N999rAAEEQM5Xa8HDCzGJ4a6XUlemvYKErAd38w4fnZr8FC6adxOOFAGe2svqn5xRFLhs-A13AzMp76SI3KBHydc9BMTyKKdUDdpVJvFlKSv5_5pK9kM0V5m3zod3XfMqTiIkt6xZkzpcNtaclqml-VPb8yKbizHwzTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68078" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68077">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68077" target="_blank">📅 12:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68076">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
پنج انفجار در بندرعباس
@News_hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68076" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68075">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید در بحرین
@News_hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68075" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68074">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ گزارش های اولیه و #غیررسمی از حمله سپاه به سفارت اسرائیل در بحرین  @News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68074" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68073">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
#مهم
؛ گزارش های اولیه و
#غیررسمی
از حمله سپاه به سفارت اسرائیل در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68073" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68072">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68072" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68071">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68071" target="_blank">📅 11:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68070">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu-xxJSYmkUHLYRHUa2xzSyq9W6cNPeR8FPLBNjsRoF4O2nVuXZVy-inED8S5S9DEwWbmmPbH5_QHwqvSIVjh9eNO6K5kyua0LonoCojF2V4QJBVZq6u3mKjtdDRmBSJZYVNV0N1qedBWtzXXOQVgn6GFhbphaZcTCCqjht5chxnGtI2tJD8y4qk-xfMJKiQmgKmm-tjxdqfNOTN-sjYhduZGmsRmvf-gScUBmh5cAY_Zy5MPvxAbZOhH-mBRqch5DmjOM5rFREbacwQ7zMpSk36Qwz_x29iJSEgCYzKVqM0L0NTunbW_5KUYoFiHEq9PpUDq6I3H0iWfXo__AHntQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی بریتانیا:
گزارشی از یک حادثه در فاصله ۱۳ مایل دریایی جنوب شرقی لیماه، عمان، دریافت کردیم
یک نفتکش گزارش داده است که هنگام تردد در مسیر جنوبی به سمت خارج، مورد اصابت موشک قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68070" target="_blank">📅 11:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68069">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68069" target="_blank">📅 11:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdbTWQbQWRmZnT9S61uaRPlTPv_uvchP-giGxKZGf-J0SCtKcQsd4MASyZd9FFmUNpjwklVb_ACo9Le290l0pVoGBVZpJjTjwGD0MFumeR_kZ9qo6c9UJdmRjDH4o-_cXekzKgrFFcZnN9rOkR_FqO_99icrHP6HLfu6EO3WXKJLR6T7LPkdgMJkKLSSjTisZY63kWZzTPhUWBP7OEEas9Fnitm9tEUiKQqbEbRQelQuYAprw-6j1KDOhC8MK7T9U2VfoYKndXCnRIyntJ8Gw8bjCFIGLkGoI0K6RafVDbDPJLv7DkeB_V0T1-gb9AWhLlvIQag7vfFLaEgo28gRtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) آخرین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب (به وقت شرقی) روز ۱۳ ژوئیه به پایان رساند.
در جریان این عملیات پنج‌ساعته، نیروهای آمریکایی با هدف تضعیف بیشتر توانایی ایران در حمله به کشتی‌های تجاری، با موفقیت به اهداف نظامی در نقاط مختلف ایران از جمله بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردند.
نیروهای سنتکام برای هدف قرار دادن سامانه‌های پدافند ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران، از مهمات دقیق‌زن استفاده کردند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند.
نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار باقی مانده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68068" target="_blank">📅 10:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68067">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68067" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68066">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AidDyfRlCLd7noFF5qyL-PeqsY5i7h562-Hxdm_nmla2Uoq41i6WHYuK1EuTcYnyhSzf0418XgYy3U3uVclC9T-7hoAnHQb5KNKPlVlWxKEu0EnXBHhOjb9XplWVtU3TnsviOq2RhK5wzslx1qGkUjP_Q0TShvJEgGWaM51YJIIgqIfGnS5zcSg2L2HbfQmYl1FetiEW_0a-tERqnSXQOjZ8TSnvMJDy4ZNSOaTgCW1Uq1sQwHTK5Mt5S14AoANuuQw5k1jKdW9LWTd5307qws3Zb0Gr5xofCgJdPdpwCUdaxPb1ZnoMXL0nXY1ifyaESFTXsWhaSIqL9fUMYDD4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:
اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد.
در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای خارجی، از جمله در مجارستان، با احمدی‌نژاد دیدارهای محرمانه‌ای برگزار کردند و از رویدادهای دانشگاهی به‌عنوان پوشش این ملاقات‌ها استفاده کردند.
این طرح در جریان جنگ ایران و اسرائیل در سال ۲۰۲۶ به اوج خود رسید؛ زمانی که مأموران موساد پس از حمله هوایی اسرائیل به محل اقامت احمدی‌نژاد در تهران، او را از آنجا خارج کرده و به یک خانه امن در داخل ایران منتقل کردند. این اقدام بخشی از یک عملیات گسترده‌تر برای تغییر حکومت بود.
این عملیات در نهایت ناکام ماند، زیرا احمدی‌نژاد تحت شرایطی نامشخص خانه امن را ترک کرد.
به گفته مقام‌های ایرانی، او اکنون پس از آنکه مقامات از تماس‌های ادعایی‌اش با اسرائیل مطلع شدند، در حصر خانگی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68066" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68065">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68065" target="_blank">📅 03:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68064">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68064" target="_blank">📅 02:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68063">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68063" target="_blank">📅 02:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68062">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
انفجار امیدیه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68062" target="_blank">📅 02:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68061">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
حمله به سپاهِ سراوان در سیستان و بلوچستان
@News_hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68061" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68060">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68060" target="_blank">📅 02:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68059">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68059" target="_blank">📅 02:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68058">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
ترامپ:  سلیمانی به دنبال این بود که بسیاری از تأسیسات نظامی ما در عراق و ایران را از بین ببرد
😂
من او را قبل از اینکه ما را بگیرد گرفتم.  @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68058" target="_blank">📅 02:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68057">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68057" target="_blank">📅 02:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68056">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
وزارت دفاع امارات متحده عربی:
دو نفتکش ملی به نام‌های "ممباسا" و "الباهیه" در آب‌های منطقه‌ای عمان، در بخش جنوبی تنگه هرمز، مورد هدف دو موشک ضدکشتی ایرانی قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68056" target="_blank">📅 02:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68055">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68055" target="_blank">📅 02:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68054">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
خبرنگار: ماه هاست که ایران را بمباران می کنید.
🔴
ترامپ: ما 19 سال در ویتنام بودیم. ما چهار ماهه اینجاییم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68054" target="_blank">📅 02:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68053">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68053" target="_blank">📅 01:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68052">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68052" target="_blank">📅 01:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68051">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO81QOz9CEPRhb4J3MGEcWx9mu5KDzrtCavcrNTofF-x-pzcWQULlnag-vu26cxv17zMgzcSs1aRMNIE7mi62QQRs91UzjYorUcebTCfDR4x3dx6XdXP0RJ5U3yHEgwmWtxu6a8KvR9IKNBLPFmloHpvo_n89a6Xlg2ZzYPrzeERTI1-OYIOOpVIUbseWX31GUsBkLenlpF4vQTcIavz_5lHCMU5uxVs5-nwnEY6keZMPLnnLGVzJ6IqGvcw5YUt8Lyrlau6I91mtrkEXRtGRjTDcyBxKKTQJrn56V_j05xtLVy0Eg1SD7eLCQTiv9fXtLR7PIxmZtopSu8V746cfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرکز عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۴۰ مایل دریایی از منطقه قلهات در عمان هدف اصابت یک پرتابه قرار گرفته و این پرتابه به اتاق موتورخانه کشتی برخورد کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/68051" target="_blank">📅 01:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68050">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/68050" target="_blank">📅 01:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68049">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68049" target="_blank">📅 01:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68047">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h4_IXhvc3_4HuuWPDAde5e28HN9qHRpN2JLg94CDoTb3jVrWLBMK_ikRZ185iZFitOS9Q6727laRRg91iHNdKi6xRmNJ_jgI9pZl8kHKp_7z6bgOy2wn_sZUMJVWY0bijGoG0H6ZGcxaq6vtw5C_A-0HXQ4GgNZ3oFmQr7jdphmJl0h2Ocy2rZen3wXhROj4tl_fbc4nLoBzGsO_nZ1S9bsIlavwJCYIxD8CJ32PdHmK9_woe-sA1cWYZV0et5bw2ihqsIDu0zaGmsw96mWD6pMTMYkKjPprKo5uXakbjVH3jSvzU4iDdk5KbxvQRhwzYq-s_2-9eH1YoQNzeix_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/StTMqr-vrBq713fG8v6vQbmb3Ni-E7mQrSRNMipK1uAL1ySPnaMb0s0gpvMNilxfKuBY6XEwb1ATjDaXG9hTF6fAw5tSRPQ2qfaYDfsw0ueTLsCft6fBJ688u9tT17wGWb1t1E78WhXQRd3ZKMhLDYIBpadyX6p2ik2xSwo9TDpP2G7mhFe9-NsVhlVKk1nzLZIWy_CSYkkPcR4W0Fy-MoHTxoZM6JYgH4a_mE5_rJ-jhgwP50TxFOXfcImXd6-pKLkbAoPbEWwh2-eU000UtdyS3UIZxpbybM3DrRHmRpq8GHAm6sg73ZYjDNmp-W3Jb9YTQjYxjxsYr0p00WHwog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویری دیگر از حملات آمریکا به جزیره کیش
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68047" target="_blank">📅 01:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68046">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد  @News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68046" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68045">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع چندین انفجار در  کیش
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68045" target="_blank">📅 01:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68044">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBBEq80J46meICTI72Y1FQvaPRu_4zr1X_w5MVkPsycG5TdMVjeY-hr-_yVJoYmojbezmWfvz9ye7p1aJAF2LTja0XqJtaRdHikFA5hOG_9mvguWPrjWjVoV8NxXSbjREwjusHL6wtCg122lXMfBKW54MjW3lWtH5UdsJs6k-1QIgwRVOINjrdBOkvEXof01wNw_E0Oj6-KQxCHyGUHLmNNg7QYXicXDGPndG6aibpGXJiKMV6uhVjO09het3Lltbf1tmKcfAqf4DLWI8hmflsZU_YRNe_4Ehi66GTujlNIch4jFvOjRPV2SDshZHTcrFfLqxzB_nXLY-ohVQBHPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:بندرگاه کیش رو زد
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68044" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68043">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvNkSG0Q233ktgWl0HWACiq4jTHkXjo--wxrue6fz1WAAQD8wRcXwiYAJvCeMZiDFVztdGpYmxilKlKVQ5os8MSyOqXz-Yfliy0mnA9I2K08ayac2tZk0PRTo0xggtEDyzbbtPuzKn9LGwdLiKGkdqJQoNLeW1jif0Ptz0mxW1sKlrREI_WN2_75_-tjX0vrsLrIu4hfWntuxGVToc2od88xTS3DiMFfm0CeQYj9H6Q1oZEeyRQQsOOgIYgrjDZ0npoKNkyq6xwMaZCjNgwbUKRUD849j1bOMHA3o4KzluSBYM2ImCtv4Acos4XedJ4L1IwBvZZHnw2oCZGTSif-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68043" target="_blank">📅 00:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68042">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a423066bec.mp4?token=t2c4sQd2-Ejx3kZI1NU4vdDS20ymwqxpbjqNYLYIb3ToT3VkyeXW7IJ9SegFQgiSKcHCCNwpr7A3a7MrXLMHVNPj9jvLjYj3n0m-_VIKBdiDd7hZ3OPhtZhUoaWNtT_YOdDjGpqHgPhKQucuWo_ucJAFOLBGVkofMEPaFZI5NRiWkf3xvr2GdK4l0K4UdDzEhhVQ0cDYMesw_6O2kJR0UagW-5ht_GGiLQBobPp6Zi_Jx1ocExFdy6uWxTesuY_tOJQ7ySdBjrIZy6LqTC2udsIQX8Aa1ynGYHGd3uzsUQjkIbu7LQLz3YvnYfLtoYJogtETabavBOS29Vgxv2nOvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a423066bec.mp4?token=t2c4sQd2-Ejx3kZI1NU4vdDS20ymwqxpbjqNYLYIb3ToT3VkyeXW7IJ9SegFQgiSKcHCCNwpr7A3a7MrXLMHVNPj9jvLjYj3n0m-_VIKBdiDd7hZ3OPhtZhUoaWNtT_YOdDjGpqHgPhKQucuWo_ucJAFOLBGVkofMEPaFZI5NRiWkf3xvr2GdK4l0K4UdDzEhhVQ0cDYMesw_6O2kJR0UagW-5ht_GGiLQBobPp6Zi_Jx1ocExFdy6uWxTesuY_tOJQ7ySdBjrIZy6LqTC2udsIQX8Aa1ynGYHGd3uzsUQjkIbu7LQLz3YvnYfLtoYJogtETabavBOS29Vgxv2nOvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
منتسب به سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68042" target="_blank">📅 00:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68041">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
انفجار ها در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68041" target="_blank">📅 00:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68040">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
تپه الله اکبر زدن بندرعباس ایستگاه رادیویی
گزارش ممبرای چنل
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68040" target="_blank">📅 00:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68039">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
چندین انفجار در کیش
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68039" target="_blank">📅 00:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68038">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما حملات ارتش آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68038" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68037">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/symJ5oL0cwo5qZVe5fTS2xAu2u0AbGJo4dnnRThG9I5qAMRdOVya2U7harXI7p82vdQ3qtYOb51so-4h0hnUGs8PfEVcivFksfVDQidq5vxIBuyWR7qWUkZ4xHI3Tz7PMvdka_5u3NMDP6-G45CAAKxGrEQnsv0kKx6HTJtAr7Okcs0w3FBnh2uJ3o4r2rFh6NNejxH5IFhyEb_Ci1qjDuJuSelV-93wzP54J3jWl6rglP7SiGItNgEHKtDr78KUrfXqWmpZ8CIJBeT7VOh4PGFLUPXOEUXA4Ki69IRJE7qkXyyy2z-630qmobE5wPh_0iPgxfSj7cipd8TsxFeEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
امروز ساعت ۴:۴۵ بعدازظهر به وقت شرقی، فرماندهی مرکزی ایالات متحده به دستور فرمانده کل، سومین شبِ پیاپی حملات علیه ایران را آغاز کرد. این حملات همچنان هزینه‌های سنگینی را بر نیروهای ایرانی تحمیل کرده و توانایی آن‌ها را برای حمله به غیرنظامیان بی‌گناه و کشتی‌های تجاری در تنگه هرمز تضعیف خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68037" target="_blank">📅 00:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68036">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های اولیه از وقوع دو انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68036" target="_blank">📅 00:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68035">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68035" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68034">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68034" target="_blank">📅 00:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68033">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68033" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68032">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ درباره هدف قرار دادن مقام‌های باقی‌مانده حکومت ایران:
«ما قطعاً اون‌ها رو زیر نظر داریم. آره، اطلاعات زیادی درباره این موضوع دارم، خیلی هم می‌دونم، اما فکر نمی‌کنم الان زمان مناسبی باشه که درباره‌ش حرف بزنم.
باید ببینیم چی پیش میاد. مثلاً امشب حسابی بهشون ضربه می‌زنیم و فردا هم همین‌طور. هیچ کاری هم از دستشون برنمیاد.
اونا هیچ چیزی ندارن؛ تنها کاری که بلدن اینه که لاف بزنن. و فکر می‌کنم کاری که من انجام دادم، کار خیلی درستی بود، چون باعث شد بیشتر باهاشون آشنا بشم...»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68032" target="_blank">📅 00:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68031">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68031" target="_blank">📅 00:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68030">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68030" target="_blank">📅 00:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68029">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
تاسیسات اتمی  خاصی در منطقه کوهستانی موسوم به " کوه کلنگ " در جنوب نطنز قرار‌ دارد
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68029" target="_blank">📅 00:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68028">
<div class="tg-post-header">📌 پیام #42</div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68028" target="_blank">📅 00:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68027">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68027" target="_blank">📅 00:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68026">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68026" target="_blank">📅 00:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68024">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یکم بالاترو نشونه بگیر املاکیِ پدراشتراکی، بیچاره جنوبیا خسته شدن #hjAly‌</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68024" target="_blank">📅 23:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68022">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:   امشب و فردا با قدرت به ایران ضربه خواهیم زد  @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68022" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68021">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
یاداشت تفاهم با ایران یک آزمایش بود و آنها به آن پایبند نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68021" target="_blank">📅 23:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68020">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
امشب و فردا با قدرت به ایران ضربه خواهیم زد
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68020" target="_blank">📅 23:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68019">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
صحبت های امروز ترامپ با زیرنویس فارسی
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68019" target="_blank">📅 23:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68018">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
تسنیم:
چند کشتی متخلف در تنگه هرمز هدف قرار گرفته شدند
.
منابع محلی از هدف قرار دادن چند کشتی متخلف در تنگه هرمز خبر می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68018" target="_blank">📅 22:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68017">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c2989693.mp4?token=Wnmb8lf5v22IpW_xr2usTlPEvRCmVTC-dJfPB1kcsg93GFwM92CXRii6LOVwxn6zhv9mofieggfhFx0V8LJPfNVSRQWBvdpjCoGN0lmYEUMsYNNT0dsoQAIKHAnc4zOn71jaZq07-zmrDysRdqtnqxDumjQJ6VX8b2e3GWGZixXIjz0wI2nsO2qnhyY_pA2fJ35BwpZRCjnmeywqWrELRw8i0ad2-RYDint3reLryyEHv0zPpIWloPYVW3NLzjh_TV30kcMILj7yjkhROZxLrrqmaTwjnT4_5Ra_DpzNtvZxG764capGEcaqzHZGdgun_XHYlRLmdlBq7I7ROjtR-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c2989693.mp4?token=Wnmb8lf5v22IpW_xr2usTlPEvRCmVTC-dJfPB1kcsg93GFwM92CXRii6LOVwxn6zhv9mofieggfhFx0V8LJPfNVSRQWBvdpjCoGN0lmYEUMsYNNT0dsoQAIKHAnc4zOn71jaZq07-zmrDysRdqtnqxDumjQJ6VX8b2e3GWGZixXIjz0wI2nsO2qnhyY_pA2fJ35BwpZRCjnmeywqWrELRw8i0ad2-RYDint3reLryyEHv0zPpIWloPYVW3NLzjh_TV30kcMILj7yjkhROZxLrrqmaTwjnT4_5Ra_DpzNtvZxG764capGEcaqzHZGdgun_XHYlRLmdlBq7I7ROjtR-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
انفجارهایی در شهر کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68017" target="_blank">📅 22:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68016">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
بیرجند، چابهار و سایت موشکی لار لحظاتی قبل هدف حمله آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68016" target="_blank">📅 22:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68015">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBC8FnlpOeyzXir57Z5P1MqUswdqw4Phvx2D2VcBBsFdYnrtp4cjTzO6IvthCDXDo-BW6lxYkT0uZBnA7is9jmwqAGFnWl9zQWp07NQ3nVpY73LFYJ87oA2IsJBKFIVgZlFrr0wNpLfuotc51Pc3HgsIkJYYvc22EaiK9GjqgDCb2ahennoAlN01sO5AV0ZJo7W07FGm3OmMnNByDXLIY64X2vnfi0DTjayAuM5n4iQD6zhQ3lcHEc3b4VRNbav_xZqwfmRJXky7iVg0M5le9u7oc-nXVYLX6l9mTBBDMZEBRfZ9jn4VV2kqrDfawvI6JjIE0eOxTi_hK3bEmGGeJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
پرزیدنت ترامپ:
رئیس جمهور ترامپ پنجشنبه شب، ساعت 9 شب به وقت شرقی، خطاب به ملت سخنرانی خواهد کرد.
از توجه شما به این موضوع متشکرم!
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68015" target="_blank">📅 22:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68014">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErhZySRIJH1xXsJZay9HentPKoLROiSoXAq3zncMvjZ_95fyhdnz9lyJOmp5jyneEkGBPAxvqwcJ5D_Lh6IsKxs3g8Ee6LRNrqwNO4LDPQTlTtu4lZwQwINLYoWvKcB2UAVaH4VQ8tD4z4qpNeNq4RNO8ZvzMyb0UKbYg7FTAC00CpNZqaDHfkENq64ntpEGgNHkubVH3WRw9SJFmsO0nNjdzjVypnwgolhMIf3iobKM4UiH82CZluI2E7e3PGWKIruG5dVbC5yCSQnPVjqv3lhhBCE11WtxdVVjoYPWhBKkG-KcIIZJb7Vy6GEOnjcxjWiCfgkP6vZgj7_7Zi_Chg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عباس عراقچی، وزیر خارجه جمهوری اسلامی:
رئیس‌جمهور آمریکا کاملاً حق دارد. هر کسی که عبور امن و ایمن کشتی‌های تجاری از تنگه هرمز را تأمین کند، باید بابت این خدمت پاداش دریافت کند. ایران همواره «نگهبان» این تنگه بوده و «برای همیشه» چنین خواهد ماند. البته ۲۰ درصد رقم بسیار بالایی است؛ ما منصفانه عمل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68014" target="_blank">📅 22:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68013">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار سنگین در بندرعباس و کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68013" target="_blank">📅 22:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68012">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtVKMJIYunRdLQ5q7YpMZidcaJilMVjG9Z_NNU9i0mT2FyoPW_M3OQShJ1bn6mjkWcHaPawTkR7J1EN_PkcEZnQqzoUQFjRMAIZLUAxqnWLyUT6M7k4qvG28i9gUHYA7nTPEUL1133OWmlIm6ctUSIuFyr2PEJQgn__OmNTZioMrUeZPYKfM5JmiIg75PstrrCWO44mfUyuWF3xqlkQ8nDg3_qd5Pw8gGNbq-ycdVAS3gYCF3OnyLsyGp4cUc3WCji3svRR-Xl_RUYMnG31lgEYiCXBwTYIn6A_EzQglpMGu69PNp_5KhQ4-iSqb2ASuhexKc7Nht65cdnbiFTtRXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
فووووری؛ نیویورک تایمز: ترامپ به کنگره رسما اطلاع داده که درگیری با ایران از سر گرفته شده
آمریکا و ایران بار دیگر به لبه جنگ نزدیک می‌شوند. ترامپ اعلام کرد که امریکا، محاصره دریایی بنادر ایران را از سر گرفته و قصد دارد 20 درصد مالیات بر کالاهایی که از تنگه هرمز عبور می‌کنند، وضع کند.
پس از یک شب دیگر از حملات، به نظر می‌رسد که آمریکا و ایران به درگیری‌های شدیدتری که قبل از آتش‌بس وجود داشت، بازگشته‌اند، زیرا طرفین با اظهارات تحریک‌آمیز به یکدیگر پاسخ می‌دادند و رئیس‌جمهور ترامپ اعلام کرد که محاصره دریایی بنادر ایران را از سر گرفته است.
آقای ترامپ همچنین رسما به کنگره اطلاع داده است که درگیری با ایران از سر گرفته شده،
که اعترافی به فروپاشی آتش‌بس است و این موضوع، جدالی بر سر اختیارات جنگی حیاتی را تشدید می‌کند. کنگره به رئیس‌جمهور دستور داده است که یا جنگ را پایان دهد یا برای ادامه آن درخواست تاییدیه کند، اما آقای ترامپ اصرار دارد که او تنها کسی است که حق تصمیم‌گیری در این زمینه را دارد. این نامه که روز جمعه ارسال شده بود، روز دوشنبه توسط روزنامه نیویورک تایمز به دست آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68012" target="_blank">📅 21:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68010">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Znhx_D2gWyHJxVlmBaXk5C023GBLZqOQF83S03OZDSbwevdxScRxjrLY7qPXLobDcXPhlK7hfbe24EDOrMiVcjNJgKIXsWZAbyM0MOw1Bn2AyjIiPGf4Pq7gkdIez0kY-e_nngWbtp3zt3tTh24VnyoPc09V1R1f1CyA2ukOswSMRCZ87MqWvYuvh18xwafz8EQDs-r2P4tDrgPeceW_62IN0YEEApkChouo0CsW_BHWCheXlOZs36laeWZ_n91GUIdhUVkO6hkc8X5kK95EquIPhG6B9KD4WYQi-5B1xOO-LiE_RefD4Njz_GZTlyHqLf2cq-3IVinELmYhJGV0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛ایالات متحده اعلام کرده است که از ساعت ۲۰:۰۰ به وقت گرینویچ(۲۳:۳۰ به وقت ایران) در روز ۱۴ ژوئیه، محاصره دریایی تمامی بنادر و آب‌های ساحلی ایران را به اجرا خواهد گذاشت و تمامی کشتی‌ها — صرف‌نظر از پرچم کشورشان — مشمول این اقدام خواهند بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68010" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68009">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2WdsZTVFeNUMm_3gTsk6XsYAFrQPeKCjYWmgTXMBSUwf_FhrsRh83D5elLq94HmqupvD8Qp_gskN00vgH-VM6XqYpym-jXsyc37onBLMtiDRO5v2GeleLeS2uGi_0dpAj_kQmrTNeyqAsKr0_TMMYa79eoYRFy7CcXoou1t-gYcEmrY_cwRX_wk21O4V__Y7ge6RNDiJ61W6B7AsM3UIi3JZpuhnfWxrc8U7hDKbY-YrszlfxGBRfD2-qhYlSu_zh0jxYuhuv_n0uTQQbTcvrOp8qGkSyCpHJpfIcxCfYRLqOTALyy3q0b93ea_ciaWhKmVBOJe_Dv1x-yh91Az0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/news_hut/68009" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68008">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
هواپیما جمهوری اسلامی داشت میرفت سمت فرودگاه صنعا، این فرودگاه بلافاصله توسط جنگنده های عربستانی بمباران شد.  @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68008" target="_blank">📅 21:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68007">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33092f28c9.mp4?token=omVp1glPI_L2zYsbcKJTwlHFf9Q1Fbvq8GV9VVCcDRQDEE5D5HbfqqHCG_eH5UqTvcxA0FXEVivloFBRsLsL2FqSrOGp0NiYlwuvdD5QB5CGpi4BBW5QZtscrLTLfsjnZS93IQgvPPSnNbYjRmgCGlh7NDaIiLXoUD2SGSO6Rtf2RG7-puhgxpCGKyKh-cekzKjxbEx2YGbhuBfH4LuMuTlYIyBbxty0tJjlmoB-rZ4Ordf-ouZ24VSyATXggu_EkPUYjN9McZXCTh114SR4kxEAF7jjvloilv6TOH2TCt76PoE8yt7z8WdRRi5xsHg6GbyFEfXWh1iZGwHB4J5AyYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33092f28c9.mp4?token=omVp1glPI_L2zYsbcKJTwlHFf9Q1Fbvq8GV9VVCcDRQDEE5D5HbfqqHCG_eH5UqTvcxA0FXEVivloFBRsLsL2FqSrOGp0NiYlwuvdD5QB5CGpi4BBW5QZtscrLTLfsjnZS93IQgvPPSnNbYjRmgCGlh7NDaIiLXoUD2SGSO6Rtf2RG7-puhgxpCGKyKh-cekzKjxbEx2YGbhuBfH4LuMuTlYIyBbxty0tJjlmoB-rZ4Ordf-ouZ24VSyATXggu_EkPUYjN9McZXCTh114SR4kxEAF7jjvloilv6TOH2TCt76PoE8yt7z8WdRRi5xsHg6GbyFEfXWh1iZGwHB4J5AyYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی اقتدار و وطن‌پرستی محمدرضا شاه پهلوی و قدرت ایران، جهان غرب را به واکنش واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68007" target="_blank">📅 20:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68006">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c93097e540.mp4?token=Mvd9uCQQ-Mdqf4r7biOUVlNJAZGL9nFe38CRWsXj0FpvAitBDxWEpxojiJlkneaInHRkKsSYAtQl_oDutdlMME8u_CAxZNzsRh5nYEEBaZD4RFDLMxOYA9ZZ-0KnrkgQRZxozdt0FzwB4nParIvAIArL6ECOXeRP2pbYjnGqStlHRsvDETPDr6R3AxBqCs5WBBwpSBDpZ1-U9E4jfcQpVLJIC3ozoBIOF8IafTLVRAX-sgb0jBEpcgieRFtoQSckQ1Dsm5s32DLo5VH7a1P9wxbZBq7_CfsmGZ5I9ZPdOQtZGsHXYLPzKCKq8C9sR0MJuo26Zg7P2kJZ_-k8hOP0DUZ8m4O-CjLBIhppQ4OyZotTnb4ykVD40ZSx7Ib3JhGOd04xlIqXFEcjKEDTsj1ljLrzNN3kgkkwFwTXdNz7FxiTWV2fJ_EOU_j9MKUquX1D4gwUhz0IJQFR1xoGWsbnPrL4FPJACXwqF_z3svrvk8Zus6SYJ02scCdpG5NvkZBIWbc59zTiN4yyf91-lfpT1RJ_u4AkXAF3hQ2A1527DVsS8kzOUG82QoSBDQx8LU7ok6A0GtcxbTMn7x6KvmkVhI7hfuJfUEN0Y2Qn1WrRATlffvV4QriDQMTyTCmzm1wleVL_p3SWJXWWtDPGwKAvdA2Q5bjStIk-LtCYT6lIIqU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c93097e540.mp4?token=Mvd9uCQQ-Mdqf4r7biOUVlNJAZGL9nFe38CRWsXj0FpvAitBDxWEpxojiJlkneaInHRkKsSYAtQl_oDutdlMME8u_CAxZNzsRh5nYEEBaZD4RFDLMxOYA9ZZ-0KnrkgQRZxozdt0FzwB4nParIvAIArL6ECOXeRP2pbYjnGqStlHRsvDETPDr6R3AxBqCs5WBBwpSBDpZ1-U9E4jfcQpVLJIC3ozoBIOF8IafTLVRAX-sgb0jBEpcgieRFtoQSckQ1Dsm5s32DLo5VH7a1P9wxbZBq7_CfsmGZ5I9ZPdOQtZGsHXYLPzKCKq8C9sR0MJuo26Zg7P2kJZ_-k8hOP0DUZ8m4O-CjLBIhppQ4OyZotTnb4ykVD40ZSx7Ib3JhGOd04xlIqXFEcjKEDTsj1ljLrzNN3kgkkwFwTXdNz7FxiTWV2fJ_EOU_j9MKUquX1D4gwUhz0IJQFR1xoGWsbnPrL4FPJACXwqF_z3svrvk8Zus6SYJ02scCdpG5NvkZBIWbc59zTiN4yyf91-lfpT1RJ_u4AkXAF3hQ2A1527DVsS8kzOUG82QoSBDQx8LU7ok6A0GtcxbTMn7x6KvmkVhI7hfuJfUEN0Y2Qn1WrRATlffvV4QriDQMTyTCmzm1wleVL_p3SWJXWWtDPGwKAvdA2Q5bjStIk-LtCYT6lIIqU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه از هیجان پایین جنگ ایران و آمریکا خسته شدین؛
پیشنهاد میکنم این شوخی معمولی پسرونه بچه‌های بلوچ رو تا آخر ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68006" target="_blank">📅 19:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68005">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e510433ba3.mp4?token=Zh05Ax8wb-eklTr_CkLABBgldQR13WWetseJLJ675hMFtD-_NrHjiP-11xiwD2GyaFeSQ8VuhEHcys92QvupHDF_gcvO6h-LZz9D9MDX6MPpTYEi79IC11wAbuH1uWMOcEiXOYz908-vXgRSpGwOHoMxwaNf_wirlOiC_eBZGj0HI_sZ278SCLzc_PRZE-joL3IDVZOQFg5sO2_l1OcsYaBtkW0XcQGICs2yB1WojnDQEOoD52mDlaz0oURLtWB2ctuVBElVDQFt7rfhLPzn1lMesR1QgQF6D_NrWMSiL1jUAO1NwtOhf-QWs3iq-qYgIFgjJwf0-ELN52RHIUrGOWe9ShqqUYyMQ4nBViwCc39q-BTgdFOEl8fukSow3ZHVfKe5M_T557TWdRze88K48JRwnB-uUhUTtrVBnkPERaus8Q61SYFfk7Y99FALSJ2DW-ZJeiWzD5PTEIwYRQfVuWqAkWOpWdQotlkx5my_9CgJ6stVbqoG2E9jDCnWzp2Q-itXRrvj69GJ9MO2DmVhVkyN8xdpHwhs0SqMMkzBCIIk8vonrzUF9tvP1vha8qwP1HUeVrtgWmbtnGCE-3fqzSB4jfcg8yrzbFS_YtiWkmNp6D6-ru7GPZavw01g5bXtJ1GrbIJ93QzpnUCCe1NEYqdthiE9OsLSEf1cfdiihug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e510433ba3.mp4?token=Zh05Ax8wb-eklTr_CkLABBgldQR13WWetseJLJ675hMFtD-_NrHjiP-11xiwD2GyaFeSQ8VuhEHcys92QvupHDF_gcvO6h-LZz9D9MDX6MPpTYEi79IC11wAbuH1uWMOcEiXOYz908-vXgRSpGwOHoMxwaNf_wirlOiC_eBZGj0HI_sZ278SCLzc_PRZE-joL3IDVZOQFg5sO2_l1OcsYaBtkW0XcQGICs2yB1WojnDQEOoD52mDlaz0oURLtWB2ctuVBElVDQFt7rfhLPzn1lMesR1QgQF6D_NrWMSiL1jUAO1NwtOhf-QWs3iq-qYgIFgjJwf0-ELN52RHIUrGOWe9ShqqUYyMQ4nBViwCc39q-BTgdFOEl8fukSow3ZHVfKe5M_T557TWdRze88K48JRwnB-uUhUTtrVBnkPERaus8Q61SYFfk7Y99FALSJ2DW-ZJeiWzD5PTEIwYRQfVuWqAkWOpWdQotlkx5my_9CgJ6stVbqoG2E9jDCnWzp2Q-itXRrvj69GJ9MO2DmVhVkyN8xdpHwhs0SqMMkzBCIIk8vonrzUF9tvP1vha8qwP1HUeVrtgWmbtnGCE-3fqzSB4jfcg8yrzbFS_YtiWkmNp6D6-ru7GPZavw01g5bXtJ1GrbIJ93QzpnUCCe1NEYqdthiE9OsLSEf1cfdiihug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری ۸سال پیش روح‌الله زم:
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68005" target="_blank">📅 19:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68004">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97484f7b84.mp4?token=uX4nbZqDcrqb0-abYDnZFnsBKmzxheWz6mXldkOiOZ6Lb4pQ-S4pd2shQwzKsReIynvvxSsO9WN9YPvVWA4b6cDU2cs2okvMPd74jUs5wGE6fngQFI3p6QtAujE6YwOkvnLYsUdRkcNUQK19Roh3YQQkf7opzG5ajTzcOmCtHw31tuNuItT6Xm5rEUGp7rtMD41-l_QyQ6BKMxBqlOSWVg1eONNC5iGgKmErXRRDM6q65mbMuO-5V3nZzs17cczYBVP-aCXfhNMnq_VrmJNup_WXhMVYTLDe9nruhQiTzGrisXUhdvV3M2OrCuSZ89qazsntpBP2EckjJ8PcaYntYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97484f7b84.mp4?token=uX4nbZqDcrqb0-abYDnZFnsBKmzxheWz6mXldkOiOZ6Lb4pQ-S4pd2shQwzKsReIynvvxSsO9WN9YPvVWA4b6cDU2cs2okvMPd74jUs5wGE6fngQFI3p6QtAujE6YwOkvnLYsUdRkcNUQK19Roh3YQQkf7opzG5ajTzcOmCtHw31tuNuItT6Xm5rEUGp7rtMD41-l_QyQ6BKMxBqlOSWVg1eONNC5iGgKmErXRRDM6q65mbMuO-5V3nZzs17cczYBVP-aCXfhNMnq_VrmJNup_WXhMVYTLDe9nruhQiTzGrisXUhdvV3M2OrCuSZ89qazsntpBP2EckjJ8PcaYntYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💪
سنتکام: برای اولین بار با استفاده از شهپاد (شناور هدایت‌پذیر از راه دور) یک تأسیسات دریایی ایران در بندرعباس را هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68004" target="_blank">📅 18:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68003">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsbBMaxVgjrZubc-hCpyr2A9KJNatO0bEx02X0FWrqHBAFoWUXzh2qSQ8dpdg_GfCExFJanVrAQK3ZqtQAIyx3XF-T6l0htNPymFcT0TOa1YbL3r0Ujv81ITAMP0CC3-NBZgKLM6H3rs9yPLLh9k0YhkUv9j9G-p26YEfmNxM2I52R3ONRk97s_oV1II7uy-B1mVEmW3b8Lrfy1WFY7eHJ88aFQi7fvFG_R0YlbX4tOlm_qaOa_lL-95ka1Cq1btElydGhUZXrm-n4GesmgeXYfLtDSZcNEw8P4K7YknjBH2g-mX9XBPbnfFZJdCwVoVPT-RKYyEay--7Q9Mm1bEPQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68003" target="_blank">📅 17:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68002">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووری
؛ترامپ دستور داد محاصره دریایی علیه ایران دوباره اعمال شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68002" target="_blank">📅 17:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68001">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68001" target="_blank">📅 17:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67999">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d51dbf16e.mp4?token=et_PU5iQMiAIJ9oPg_yTeNJd3Oz62kbVUjkUaRswH522CUldrym0Y1CoP85fvBtZi-JLcbY_ugdtGhCs1vLvYjEQRw43Wpw9bAoYkVInLRBW7vJIzkmfjSJNUToZ9NT5JsZLDIKk7z693hOiNmoer7RjYaZIp-W5VXMkdwEtRKOT6Qi8a-7r2GlbXJ1A0jIle6eTVhitlr1HJBvm12Q-cLJia9mOO_2bMytuDElrz0ca0gU-7xcjg8EAbH8ZESOw69P8UQAa3ahJ2W36N6W6fz11DyjUNSM0FGCZSI1jrKRjF9f_oV96Nv_WcyzDZkr45jxMZeRMmfjqCeikTg6YgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d51dbf16e.mp4?token=et_PU5iQMiAIJ9oPg_yTeNJd3Oz62kbVUjkUaRswH522CUldrym0Y1CoP85fvBtZi-JLcbY_ugdtGhCs1vLvYjEQRw43Wpw9bAoYkVInLRBW7vJIzkmfjSJNUToZ9NT5JsZLDIKk7z693hOiNmoer7RjYaZIp-W5VXMkdwEtRKOT6Qi8a-7r2GlbXJ1A0jIle6eTVhitlr1HJBvm12Q-cLJia9mOO_2bMytuDElrz0ca0gU-7xcjg8EAbH8ZESOw69P8UQAa3ahJ2W36N6W6fz11DyjUNSM0FGCZSI1jrKRjF9f_oV96Nv_WcyzDZkr45jxMZeRMmfjqCeikTg6YgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها هیچ‌چیز ندارند. هیچ نیروی دریایی ندارند، هیچ نیروی هوایی ندارند، همه‌چیز از بین رفته است. پدافند ضد هوایی‌شان نابود شده است.
رهبران‌شان همگی کشته شده‌اند. بهترین رهبران‌شان کشته شده‌اند. آن‌ها از بین رفته‌اند. خمینی کشته شده است، پسرش هم ۹۰ درصد کارش تمام است.
آن‌وقت نیویورک تایمز مقاله‌ای می‌نویسد که وضعیت آن‌ها امروز بهتر شده است... آن‌ها تورم ۳۵۰ درصدی دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/67999" target="_blank">📅 17:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67998">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ebd104df8.mp4?token=KE29Zw_W4_HCSFMhuk1jPQMwYQrAkn4OVLCziwNJEvJvEvtrT4lEFWQgEQihlxCKfuXVZnu_JhXDJRxvDZRSAADQru9QGX9AJDyqjKxO3-0cGa8jU7EKrI6uIMuL7KUXKVJepfSNhLgxodi82MyHVOn1bTQ09SrJ-qHZf5zOykqLKo4rLI7usWn93h2761eHBnooxCLX4Mw0FF0Kuuvctl-C32Tip21KPDL-Tz-bMcGZzuDSSe23KLHMbQKknAlqcc6SQ2XHaMJ8cXGttCaqRt93rLb3MpugwVNJ1fIdXnKhFBKnPhEvkj8tJ2yfjdqTwj6pZ8prMzpmXZT72ZcR6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ebd104df8.mp4?token=KE29Zw_W4_HCSFMhuk1jPQMwYQrAkn4OVLCziwNJEvJvEvtrT4lEFWQgEQihlxCKfuXVZnu_JhXDJRxvDZRSAADQru9QGX9AJDyqjKxO3-0cGa8jU7EKrI6uIMuL7KUXKVJepfSNhLgxodi82MyHVOn1bTQ09SrJ-qHZf5zOykqLKo4rLI7usWn93h2761eHBnooxCLX4Mw0FF0Kuuvctl-C32Tip21KPDL-Tz-bMcGZzuDSSe23KLHMbQKknAlqcc6SQ2XHaMJ8cXGttCaqRt93rLb3MpugwVNJ1fIdXnKhFBKnPhEvkj8tJ2yfjdqTwj6pZ8prMzpmXZT72ZcR6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67998" target="_blank">📅 17:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67997">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060cc64d0d.mp4?token=BvS5p7z7u_UsHfftePc0BlXISJI0zXHMivQLeo5l8saki7OwOISmrT_sdwZT2y_Fx8bSZED3R5X3k5zuLp_jGjdN0AdqSfEepUtOr_wJpENJGccg0YapoSV2UgAMNIqZGW4d5WX-GBWeIJWuKTfzDGGOeZuK5VA_5EF0U_FZswWgk2ja2lQ1fhQT24GcEPChIYcCD3OsCS_bDAkAsg4TCbWVd42591AQLS5-yw2jV9k10BrZxGiqk9cuyUbOjearfO23PiBZCZ3AtEEu5YlC6lC_aPNrXEQV3LUaTgz_wgAosrk1QdSTq0QfstmwARtGWgiLRljdCUxEg7xLG7z_kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060cc64d0d.mp4?token=BvS5p7z7u_UsHfftePc0BlXISJI0zXHMivQLeo5l8saki7OwOISmrT_sdwZT2y_Fx8bSZED3R5X3k5zuLp_jGjdN0AdqSfEepUtOr_wJpENJGccg0YapoSV2UgAMNIqZGW4d5WX-GBWeIJWuKTfzDGGOeZuK5VA_5EF0U_FZswWgk2ja2lQ1fhQT24GcEPChIYcCD3OsCS_bDAkAsg4TCbWVd42591AQLS5-yw2jV9k10BrZxGiqk9cuyUbOjearfO23PiBZCZ3AtEEu5YlC6lC_aPNrXEQV3LUaTgz_wgAosrk1QdSTq0QfstmwARtGWgiLRljdCUxEg7xLG7z_kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
🇬🇧
دولت بریتانیا رسما سپاه پاسداران انقلاب اسلامی(IRGC) رو در فهرست سازمان‌های تروریستی قرار داد.
در حال حاضر، ایالات متحده، اتحادیه اروپا، بریتانیا، کانادا و استرالیا سپاه پاسداران را به عنوان سازمان تروریستی ثبت کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67997" target="_blank">📅 17:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67996">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4923d848c0.mp4?token=DNd5BWx4Adep4G0RRDml6wxE2VH-LUejtY06Ban7R07V9Wl_itX3iOXpRotHI89Nr2CoHUPVVA96S3es2n4EXHFZeLR43vQMOVuTlBOkYO6-8K6bbVXrB5Kn8FNzjU3UkK5188p3iPMJ5BYaYjYVAf9xJxdV9AWwTuSa3X_N2PTkV1XD6D2Jg3Zpm2_699tGAr_zk5lkTRf1P-K1F0dIxxg8KAi4dyooKpixcobGcrKKPvrpabcm4zADoKjALPbeJx3CvheKmWuz0ZsES8fjTFY48J6Ha9obeOczVmxsPLV8mCVEelpdaRUxszmPt8tTG4R3cGzdkKNI-nX3B9lqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4923d848c0.mp4?token=DNd5BWx4Adep4G0RRDml6wxE2VH-LUejtY06Ban7R07V9Wl_itX3iOXpRotHI89Nr2CoHUPVVA96S3es2n4EXHFZeLR43vQMOVuTlBOkYO6-8K6bbVXrB5Kn8FNzjU3UkK5188p3iPMJ5BYaYjYVAf9xJxdV9AWwTuSa3X_N2PTkV1XD6D2Jg3Zpm2_699tGAr_zk5lkTRf1P-K1F0dIxxg8KAi4dyooKpixcobGcrKKPvrpabcm4zADoKjALPbeJx3CvheKmWuz0ZsES8fjTFY48J6Ha9obeOczVmxsPLV8mCVEelpdaRUxszmPt8tTG4R3cGzdkKNI-nX3B9lqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند
:
اونجا وقت برا دوش گرفتن هم بهمون نمیدادن.
از بس بهمون سخت گذشت که تعداد زیادی از بچه ها شورتشون اونجا موند.
مثلا من خودم شورتم جا مونده آمریکا.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67996" target="_blank">📅 17:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67995">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67995" target="_blank">📅 16:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67994">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8627adc5f4.mp4?token=gewUhIMr2nPiP5OQt2EmE-6vWSq8HkGRcueLpZpyi9YHBy3pqsd_Ut8nPYj1gWGPQLlX08sN9I0KBajskzgiEx1T0CInMgRjgLOiqT1n_2lyjImTza2H1C4Op-nco-kRP4kMXjfWJKvhFDXNAXBKpJ_-GzHYQ1jt0is7buMVeZGspeD2yiAsHik0_42aGJqRy7yQIto6PuGPUkP030vvzGS0ki4CI-5lWLrVk5ExFQGX98np79_xycdX_0DxepLXzXdVCx5U-3t6mo0mSDRVYF0WgyoJViEmEwVJmUi-yuJ2iFVM4T1dCPZ4YSM61jU-I5oj50fh8xz4DPeGlo2fPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8627adc5f4.mp4?token=gewUhIMr2nPiP5OQt2EmE-6vWSq8HkGRcueLpZpyi9YHBy3pqsd_Ut8nPYj1gWGPQLlX08sN9I0KBajskzgiEx1T0CInMgRjgLOiqT1n_2lyjImTza2H1C4Op-nco-kRP4kMXjfWJKvhFDXNAXBKpJ_-GzHYQ1jt0is7buMVeZGspeD2yiAsHik0_42aGJqRy7yQIto6PuGPUkP030vvzGS0ki4CI-5lWLrVk5ExFQGX98np79_xycdX_0DxepLXzXdVCx5U-3t6mo0mSDRVYF0WgyoJViEmEwVJmUi-yuJ2iFVM4T1dCPZ4YSM61jU-I5oj50fh8xz4DPeGlo2fPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
لیندسی گراهام، دوست وفادار ملت آزادی‌خواه ایران
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67994" target="_blank">📅 15:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67993">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a38d8e8e.mp4?token=XyUWlqCboguyPmjlEcNwbsX0N2QucrWUGYKY-A6DWWirYx5XFYBA5agK75KGboxxir1izLgM4Db4kEckq13LW4xf-sKoliL212bl4-cjNX940blURRJ-RjW9nx3mJd-FMcR1D2EylTEYv1mOXncsM-xzD3VkvnTKCLmrpauOvoAQg0YbgzElEqnrurHHDx8ndN1kKgugrrSJ3c1EkudwukAVRLOPKBWedLpUtRiJ_uZe2K2QznPfKitUUL5KgC4hh9AjcxBFgnobIBgkQfIWSl7xEm-8WUQG7kDbpov1i5vlirM7He9kxF1PVjGgnU1mv7x_gMrZkczpbr4JOz6Ohg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a38d8e8e.mp4?token=XyUWlqCboguyPmjlEcNwbsX0N2QucrWUGYKY-A6DWWirYx5XFYBA5agK75KGboxxir1izLgM4Db4kEckq13LW4xf-sKoliL212bl4-cjNX940blURRJ-RjW9nx3mJd-FMcR1D2EylTEYv1mOXncsM-xzD3VkvnTKCLmrpauOvoAQg0YbgzElEqnrurHHDx8ndN1kKgugrrSJ3c1EkudwukAVRLOPKBWedLpUtRiJ_uZe2K2QznPfKitUUL5KgC4hh9AjcxBFgnobIBgkQfIWSl7xEm-8WUQG7kDbpov1i5vlirM7He9kxF1PVjGgnU1mv7x_gMrZkczpbr4JOz6Ohg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇺🇸
سنتکام ویدیو‌ ای از حملات دیشب ارتش آمریکا به اهداف نظامی جمهوری اسلامی منتشر کرد.
در این عملیات سامانه‌های پدافندی، رادارهای ساحلی، توان موشکی و پهپادی و شناورهای نظامی هدف قرار گرفتند
.
همچنین برای نخستین بار از پهپادهای انتحاری دریایی استفاده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67993" target="_blank">📅 14:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67992">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e3c5be180.mp4?token=poUFiVP8rEAiVXNaKMDaIep44tGYEkkzSILSdTThzAS9L3RcJOZJK5sqmEUcqqBC0L6L2SpxqXEi5VKMsRmCD58OhP2aUOzvtcs-Xlb_pE2Mc_Z3OSl-aqEMI3P7KRkSnInKQs8l3k5A0KUHd1QDy8XQLyfLAkzc7tNWTavBUBrcMB4Cxblr7liQtuHPfz7dYOKWkBei3TFm0JGNqQBH5AwefeA53NvHrNp7dIDVXTw77A1GsC5Qe7B6Fh8gd_EVNI6oetjMhWaij2hy3gmUldtwPk9S__bgFZM6EnrenjTsLWdPekeotduJgV9tOkpyhusuGzhUvspBF05Ba5GnVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e3c5be180.mp4?token=poUFiVP8rEAiVXNaKMDaIep44tGYEkkzSILSdTThzAS9L3RcJOZJK5sqmEUcqqBC0L6L2SpxqXEi5VKMsRmCD58OhP2aUOzvtcs-Xlb_pE2Mc_Z3OSl-aqEMI3P7KRkSnInKQs8l3k5A0KUHd1QDy8XQLyfLAkzc7tNWTavBUBrcMB4Cxblr7liQtuHPfz7dYOKWkBei3TFm0JGNqQBH5AwefeA53NvHrNp7dIDVXTw77A1GsC5Qe7B6Fh8gd_EVNI6oetjMhWaij2hy3gmUldtwPk9S__bgFZM6EnrenjTsLWdPekeotduJgV9tOkpyhusuGzhUvspBF05Ba5GnVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تازه‌ترین ویدئو از حمله هوایی به فرودگاه صنعا
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67992" target="_blank">📅 14:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67991">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2PxLG80trKhGsQykfypfYsp5ekinfROJFSqFMw66MX-quvgpmD8aPeM6GXt_y1SElJksEOi75JR69f98OpqaWiLrjKdmgAkuvnG7gbEvw_1YpoplqV3yTbUZjGX6687P5QET7_a5c3gxNhZwXPZd8ZV8lP6y5_q39zNdVmtI8btNtfJ0EnG59rw3UczLpoe83aZd2xFAQErg5YIQBSVKCKdhtowUI8Qt5IESozW2ERdxM_1oZXQ5b5Vo8cVIi-FrZiLKzSbkPQ7TrO44l0isjVXiz0mtBIpc-0-Nb_uzOjUoH0gGwAsOeEHu6pqDMizIlkndu9BZX4W9aW6iNQWLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
هواپیما جمهوری اسلامی داشت میرفت سمت فرودگاه صنعا، این فرودگاه بلافاصله توسط جنگنده های عربستانی بمباران شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67991" target="_blank">📅 14:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67990">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE_68tD11PcrhsDXRhwyfjU4winuymok8YlVolcjm03x47vQdkdl_CfuPxJOXnclz42KevoGfLn5scIsgKPW8Sr2jUXdGaoR75i7akpBWlGk-CdxftHx3tOTZP91by-paF9Vpz80oyq--cBREIQA0UVLMMqsiii0MESITLzB5Io-yph5-d3HoqitfBuD5Ll-nYShi9EkJrW_FhQv8z_e1YwaP_Vx1kf6KVHkoAqhXRmKFztagqiXD0tf6wTjxQxmhqaTf_UwWXR3fk5-IrliWs-maW69UHrH1ljVrgMhpEjkRnAw8p-xk43GjMyPM01uDUSlohMHjo98bJb4ENpjlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی، خواننده وآهنگساز ایرانی، با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت.
جاستین بیبر، شکیرا، مدونا و گروه بی‌تی‌اس در این اجرا حضور خواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67990" target="_blank">📅 14:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67989">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dT0W-XVnlzkqeZDboT6gDrFaXd-hkDho_MnUWfb2n33UaskGamGN6tSjFkYSSW7aUcqF08moKPvBQT8qzGVCnpN-sCfAyp47GdpIM8b2cjxehTPuECur7OHP6LArAg2T2Y_Y3eMk0sCJw2fpDkwhTTsmMxdoOo0GuzLaE9UgR2mEgy4WoWhtfaUq8gixOb0yexmJnrEg0jbr8TO88r2RkTgaut-VTw3T6zUbK9AlaC2zh1WRQCNrixu7GEEMdEnTHbfbE1h5VKFBR4qWqz1RiGsMvszswdt36OJS6vEEuUSAUQyYcPL_7CZ3euZjzXMDod6QaZ4hKmjA-PeWVTcgog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های داخلی وابسته حکومت این لیست ترور رو منتشر کردن و نوشتن لیندزی گراهام اولیش بود تا نفر آخر بی‌خیال نمی‌شیم
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67989" target="_blank">📅 13:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67988">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
تنگه هرمز دعوا شده
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/67988" target="_blank">📅 13:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67987">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7891d1b9.mp4?token=eNny95Ai7vXpJJct4G8apfaDiTMcVHiJFtETmH98S2pEMr76RrpSUbox0QkAPY2Rhq8hop45iRnD99mHIMiFXKfJa6ivYDka5tEeRG4SPXk3Nlu0II_pWlD2y5w7qVGoBEh6-SS-iI-6i_hq0rRO5V8DtI9dMcqMx865AXIwCuTPlei64Q_MnKauZgBByIS3wX5KHIiIYPGfI6EnFnfqYwbxxQRwJZzUQUrr20W72oTfVfoxI_IgY_uJxkD7T_2Dla8chOwH8oFHefC2vIIwYsDTCUx1a0tx_33JnmqDycnVYBGj1vbQI-31b9wg-GObENZd8bYRcAfz-sdos_pgSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7891d1b9.mp4?token=eNny95Ai7vXpJJct4G8apfaDiTMcVHiJFtETmH98S2pEMr76RrpSUbox0QkAPY2Rhq8hop45iRnD99mHIMiFXKfJa6ivYDka5tEeRG4SPXk3Nlu0II_pWlD2y5w7qVGoBEh6-SS-iI-6i_hq0rRO5V8DtI9dMcqMx865AXIwCuTPlei64Q_MnKauZgBByIS3wX5KHIiIYPGfI6EnFnfqYwbxxQRwJZzUQUrr20W72oTfVfoxI_IgY_uJxkD7T_2Dla8chOwH8oFHefC2vIIwYsDTCUx1a0tx_33JnmqDycnVYBGj1vbQI-31b9wg-GObENZd8bYRcAfz-sdos_pgSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:با درخواست گروسی برای بازدید از تاسیسات هسته‌ای موافقت میکنید؟
🔴
بقایی:خیر
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/67987" target="_blank">📅 12:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67986">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
گزارش ها از وقوع انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/67986" target="_blank">📅 12:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67985">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=frecYHBTy9andYtSeSN8rAx0k7LxafFR0Sath4j3gCp2nnkhT7sInfRu2449RiXWfggeqjKz3yiiozO9iXiY2-nHbrueBj6nDO2h4iIx5dUF9bT2PP6H0F840U_LGOqBCn2s_u-kKRUFtc7hDBNxTK6JrLgiL5Vkh_3OtTaW8FWPlKMl4_41Pwu9_LWuYCcNa4u6jxhbOMj1WFf3tqHa-O4vlGyWugOQtwwsPSHYoqpyuwJqCdIO2Jal4O7ZwtByv2GwIPaD_e014R2FtJcwnYSvf-esECJ7PoVJlDrbusgzjnxf1ncnZqbCMrJom6eyCOzms7gm0OWpUmUg24rZYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2159365f.mp4?token=frecYHBTy9andYtSeSN8rAx0k7LxafFR0Sath4j3gCp2nnkhT7sInfRu2449RiXWfggeqjKz3yiiozO9iXiY2-nHbrueBj6nDO2h4iIx5dUF9bT2PP6H0F840U_LGOqBCn2s_u-kKRUFtc7hDBNxTK6JrLgiL5Vkh_3OtTaW8FWPlKMl4_41Pwu9_LWuYCcNa4u6jxhbOMj1WFf3tqHa-O4vlGyWugOQtwwsPSHYoqpyuwJqCdIO2Jal4O7ZwtByv2GwIPaD_e014R2FtJcwnYSvf-esECJ7PoVJlDrbusgzjnxf1ncnZqbCMrJom6eyCOzms7gm0OWpUmUg24rZYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
ایالات متحده مسئولیت مستقیم تحولات اخیر در تنگه هرمز را بر عهده دارد. آمریکایی‌ها از همان روز نخست زیر قول خود زدند؛ آن‌ها تلاش می‌کنند مسیر امنِ هماهنگ‌شده با ایران را دور بزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67985" target="_blank">📅 12:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67984">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c1ae996e.mp4?token=e3kPIxs0lr_H1NgcZsFEd91VeJbUBOOJRhznXXU_mOSQgb5X6d0A4S1NYV-iO8v0dOqgXs5kIIL5Ozhz4Ni52WgK_ak6xW_H262Kl2qpzahlyd--o33XfrBAPHu1df0BGxUKTmfOPsKkr94onEfgmKzcZQE9FLJvvL5kAmOfYha-ZQeCrr97TPnypfPw8JicioiZ---XGfDGhN0MBk0-FIopWIT7FBrGelZ4Az3iitr6A5UVYOPj_0vhfTaytEkGDGfTPEVuGRGX7KzH6cI2FejPp9jbRPlAMrc9GciBYotn0f9dVzxS9YOWRg14ZoLwijGfLw7Ldr1wHgdbeQn6PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c1ae996e.mp4?token=e3kPIxs0lr_H1NgcZsFEd91VeJbUBOOJRhznXXU_mOSQgb5X6d0A4S1NYV-iO8v0dOqgXs5kIIL5Ozhz4Ni52WgK_ak6xW_H262Kl2qpzahlyd--o33XfrBAPHu1df0BGxUKTmfOPsKkr94onEfgmKzcZQE9FLJvvL5kAmOfYha-ZQeCrr97TPnypfPw8JicioiZ---XGfDGhN0MBk0-FIopWIT7FBrGelZ4Az3iitr6A5UVYOPj_0vhfTaytEkGDGfTPEVuGRGX7KzH6cI2FejPp9jbRPlAMrc9GciBYotn0f9dVzxS9YOWRg14ZoLwijGfLw7Ldr1wHgdbeQn6PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اسماعیل بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
پیگیری عدالت برای رهبر شهید، یک اصل جدی و مطالبه‌ای همگانی است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/67984" target="_blank">📅 12:09 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67983">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=MbXovoTPYrmAMLhG-7uRmkWQ9caXQfZ8vcZyeedMJrTgthT7ZKJtIfvMUqj5nDSfcxFsc0h-KEiOQlDi5x5Gizou-iqBS7Msb5_rMVQKjgYPd-kcMru4dDwJUR_WhlOxZJ2YXvUrZlZSGBj2cSVexxgVHEEgiJTjWDqYtH3uhYs3ni6XlUN4TlTyzeU7dhYwc1fMi6sCax86W8YVItG3FM-6pCjmfKZTg0-_sb-bxdtpuT8DcwSH3scxStJcI0l7ljZgdZNMntD4CSgzTD2QrFummqE-7kWNeegAdy9yjHCvmSLMeZVFytsUf6D3WLtW8UbKGG-bn78R2AlSI8LKGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb543b9b84.mp4?token=MbXovoTPYrmAMLhG-7uRmkWQ9caXQfZ8vcZyeedMJrTgthT7ZKJtIfvMUqj5nDSfcxFsc0h-KEiOQlDi5x5Gizou-iqBS7Msb5_rMVQKjgYPd-kcMru4dDwJUR_WhlOxZJ2YXvUrZlZSGBj2cSVexxgVHEEgiJTjWDqYtH3uhYs3ni6XlUN4TlTyzeU7dhYwc1fMi6sCax86W8YVItG3FM-6pCjmfKZTg0-_sb-bxdtpuT8DcwSH3scxStJcI0l7ljZgdZNMntD4CSgzTD2QrFummqE-7kWNeegAdy9yjHCvmSLMeZVFytsUf6D3WLtW8UbKGG-bn78R2AlSI8LKGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
نیروهای آمریکایی با استفاده از مهمات سنگرشکن، یک تأسیسات موشکی زیرزمینی در پایگاه چهارم شکاری تاکتیکی ایران در نزدیکی دزفول را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67983" target="_blank">📅 11:29 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
